# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_map.pinmap sha256=9430ff41491a2e5351f6e24aa6f82436828832cfe06fce856a623a8d42c57e25 bytes=4613 -->
## FILE: src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/pin_map.pinmap`
- sha256: `9430ff41491a2e5351f6e24aa6f82436828832cfe06fce856a623a8d42c57e25`
- bytes: 4613

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="LO4" />
		<DUTPin name="LO5" />
		<DUTPin name="LO6" />
		<DUTPin name="LO7" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
		<DUTPin name="HI4" />
		<DUTPin name="HI5" />
		<DUTPin name="HI6" />
		<DUTPin name="HI7" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI4" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI4" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI5" siteNumber="0" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI5" siteNumber="1" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI6" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI6" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI7" siteNumber="0" instrument="PXI1Slot2" channel="14" />
		<Connection pin="HI7" siteNumber="1" instrument="PXI1Slot2" channel="15" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO4" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO4" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO5" siteNumber="0" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO5" siteNumber="1" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO6" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO6" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO7" siteNumber="0" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO7" siteNumber="1" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/test.digiproj sha256=6b55c35697949514faf708d32454812a8b63aaa6c3e383a1696501ad6cdff3a4 bytes=3714 -->
## FILE: src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/test.digiproj`
- sha256: `6b55c35697949514faf708d32454812a8b63aaa6c3e383a1696501ad6cdff3a4`
- bytes: 3714

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2CA9426E370A5815736836DADB520257" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
			<FileReference Id="23" ModelDefinitionType="SourceWaveformDefinition" Name="source_waveform\.tdms" StoragePath="source_waveform.tdms" />
			<FileReference Id="24" ModelDefinitionType="CaptureWaveformDefinition" Name="capture_waveform\.digicapture" StoragePath="capture_waveform.digicapture" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_capture_waveform_serial/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_map.pinmap sha256=8a5a6a960f5fa13b20ee04b5a15c001df32fc782573a467d94c4bbfe6d0944fd bytes=1679 -->
## FILE: src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_source_waveform_serial/pin_map.pinmap`
- sha256: `8a5a6a960f5fa13b20ee04b5a15c001df32fc782573a467d94c4bbfe6d0944fd`
- bytes: 1679

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_source_waveform_serial/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_create_source_waveform_serial/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_source_waveform_serial/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_source_waveform_serial/test.digiproj sha256=54fefaed2fe54c05e2650256b828def3a3c25dabc1b324dd4880dac1b20727e0 bytes=3556 -->
## FILE: src/nidigital/system_tests/test_files/test_create_source_waveform_serial/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_source_waveform_serial/test.digiproj`
- sha256: `54fefaed2fe54c05e2650256b828def3a3c25dabc1b324dd4880dac1b20727e0`
- bytes: 3556

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2F4362CB23B1FEFAB9D0591B15212CB1" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
			<FileReference Id="23" ModelDefinitionType="SourceWaveformDefinition" Name="source_waveform\.tdms" StoragePath="source_waveform.tdms" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_create_source_waveform_serial/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/test_create_source_waveform_serial/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_create_source_waveform_serial/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_levels.digilevels sha256=2748b207cbe7a8100f12e37d142219367486c7b1f8fc379f0471639ae96c4a4d bytes=579 -->
## FILE: src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_levels.digilevels`
- sha256: `2748b207cbe7a8100f12e37d142219367486c7b1f8fc379f0471639ae96c4a4d`
- bytes: 579

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="PinGroup1">
        <Vil>0</Vil>
        <Vih>3.3</Vih>
        <Vol>0.8</Vol>
        <Voh>2</Voh>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_map.pinmap sha256=99e95d7e501edddaaf4b75f4081f4bd1053aad58208a48ccae9bd96a4b499866 bytes=1496 -->
## FILE: src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_enable_match_fail_combination/pin_map.pinmap`
- sha256: `99e95d7e501edddaaf4b75f4081f4bd1053aad58208a48ccae9bd96a4b499866`
- bytes: 1496

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.2">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<DUTPin name="DUTPin4" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
			<PinReference pin="DUTPin4" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="DUTPin4" siteNumber="0" instrument="PXI1Slot2" channel="3" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI1Slot5" channel="0" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="PXI1Slot5" channel="1" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="PXI1Slot5" channel="2" />
		<Connection pin="DUTPin4" siteNumber="1" instrument="PXI1Slot5" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_enable_match_fail_combination/specifications.specs sha256=82fcd2afa60bd93a85a9e0d1c43a4b074a33d9be0c8ab8c482e71eebb290a80a bytes=377 -->
## FILE: src/nidigital/system_tests/test_files/test_enable_match_fail_combination/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_enable_match_fail_combination/specifications.specs`
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_enable_match_fail_combination/timing.digitiming sha256=ed53e324ee7209f9552b62c6d702201d469d865a773a42d8acd10e10becdcdd2 bytes=826 -->
## FILE: src/nidigital/system_tests/test_files/test_enable_match_fail_combination/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_enable_match_fail_combination/timing.digitiming`
- sha256: `ed53e324ee7209f9552b62c6d702201d469d865a773a42d8acd10e10becdcdd2`
- bytes: 826

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
              <On>0 ns</On>
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_map.pinmap sha256=9430ff41491a2e5351f6e24aa6f82436828832cfe06fce856a623a8d42c57e25 bytes=4613 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/pin_map.pinmap`
- sha256: `9430ff41491a2e5351f6e24aa6f82436828832cfe06fce856a623a8d42c57e25`
- bytes: 4613

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="LO4" />
		<DUTPin name="LO5" />
		<DUTPin name="LO6" />
		<DUTPin name="LO7" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
		<DUTPin name="HI4" />
		<DUTPin name="HI5" />
		<DUTPin name="HI6" />
		<DUTPin name="HI7" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI4" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI4" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI5" siteNumber="0" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI5" siteNumber="1" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI6" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI6" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI7" siteNumber="0" instrument="PXI1Slot2" channel="14" />
		<Connection pin="HI7" siteNumber="1" instrument="PXI1Slot2" channel="15" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO4" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO4" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO5" siteNumber="0" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO5" siteNumber="1" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO6" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO6" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO7" siteNumber="0" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO7" siteNumber="1" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/test.digiproj sha256=6b55c35697949514faf708d32454812a8b63aaa6c3e383a1696501ad6cdff3a4 bytes=3714 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/test.digiproj`
- sha256: `6b55c35697949514faf708d32454812a8b63aaa6c3e383a1696501ad6cdff3a4`
- bytes: 3714

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2CA9426E370A5815736836DADB520257" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
			<FileReference Id="23" ModelDefinitionType="SourceWaveformDefinition" Name="source_waveform\.tdms" StoragePath="source_waveform.tdms" />
			<FileReference Id="24" ModelDefinitionType="CaptureWaveformDefinition" Name="capture_waveform\.digicapture" StoragePath="capture_waveform.digicapture" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_capture_waveform_parallel/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_map.pinmap sha256=845a9304a3e5548026072c412d1f818bc2da64213ad9b8a5b7f6dbf8d27327fd bytes=2655 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/pin_map.pinmap`
- sha256: `845a9304a3e5548026072c412d1f818bc2da64213ad9b8a5b7f6dbf8d27327fd`
- bytes: 2655

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="7" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="23" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/test.digiproj sha256=6439d0d60790b7879db624d6fa058f5702105a35ef4811ffce34447f2866fce8 bytes=3415 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/test.digiproj`
- sha256: `6439d0d60790b7879db624d6fa058f5702105a35ef4811ffce34447f2866fce8`
- bytes: 3415

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E3A8965ACB2DA3FB3488B870364FC0F5" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/timing.digitiming sha256=76ac51c294de1cb930383e46a4a5123acc8ec306046ba1020f9f422349fe8ad9 bytes=2154 -->
## FILE: src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_fetch_history_ram_cycle_information/timing.digitiming`
- sha256: `76ac51c294de1cb930383e46a4a5123acc8ec306046ba1020f9f422349fe8ad9`
- bytes: 2154

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
      <TimeSet name="tScan">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
      <TimeSet name="t2X">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins" edgeMultiplier="2x">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.5</Return>
              <Data2>AC.Period * 0.7</Data2>
              <Return2>AC.Period * 0.9</Return2>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.4</Strobe>
              <Strobe2>AC.Period * 0.8</Strobe2>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_map.pinmap sha256=8a5a6a960f5fa13b20ee04b5a15c001df32fc782573a467d94c4bbfe6d0944fd bytes=1679 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/pin_map.pinmap`
- sha256: `8a5a6a960f5fa13b20ee04b5a15c001df32fc782573a467d94c4bbfe6d0944fd`
- bytes: 1679

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/test.digiproj sha256=54fefaed2fe54c05e2650256b828def3a3c25dabc1b324dd4880dac1b20727e0 bytes=3556 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/test.digiproj`
- sha256: `54fefaed2fe54c05e2650256b828def3a3c25dabc1b324dd4880dac1b20727e0`
- bytes: 3556

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2F4362CB23B1FEFAB9D0591B15212CB1" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
			<FileReference Id="23" ModelDefinitionType="SourceWaveformDefinition" Name="source_waveform\.tdms" StoragePath="source_waveform.tdms" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_broadcast/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_map.pinmap sha256=3bae84465d605db05f2af1113df6437f2a40a1952d04fbf9caf804dd816d57a5 bytes=4610 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/pin_map.pinmap`
- sha256: `3bae84465d605db05f2af1113df6437f2a40a1952d04fbf9caf804dd816d57a5`
- bytes: 4610

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="LO4" />
		<DUTPin name="LO5" />
		<DUTPin name="LO6" />
		<DUTPin name="LO7" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
		<DUTPin name="HI4" />
		<DUTPin name="HI5" />
		<DUTPin name="HI6" />
		<DUTPin name="HI7" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="LO4" />
			<PinReference pin="LO5" />
			<PinReference pin="LO6" />
			<PinReference pin="LO7" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
			<PinReference pin="HI4" />
			<PinReference pin="HI5" />
			<PinReference pin="HI6" />
			<PinReference pin="HI7" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI4" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI4" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI5" siteNumber="0" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI5" siteNumber="1" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI6" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI6" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI7" siteNumber="0" instrument="PXI1Slot2" channel="14" />
		<Connection pin="HI7" siteNumber="1" instrument="PXI1Slot2" channel="15" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO4" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO4" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO5" siteNumber="0" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO5" siteNumber="1" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO6" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO6" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO7" siteNumber="0" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO7" siteNumber="1" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/test.digiproj sha256=88567a8a522166de518760812c6aef880b6ab92e481f54f0381792da90012f89 bytes=3711 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/test.digiproj`
- sha256: `88567a8a522166de518760812c6aef880b6ab92e481f54f0381792da90012f89`
- bytes: 3711

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2CA9426E370A5815736836DADB520257" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
			<FileReference Id="23" ModelDefinitionType="SourceWaveformDefinition" Name="source_waveform\.tdms" StoragePath="source_waveform.tdms" />
			<FileReference Id="24" ModelDefinitionType="CaptureWaveformDefinition" Name="capture_waveform\.digicapture" StoragePath="capture_waveform.digicapture" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/test_source_waveform_parallel_site_unique/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_system_nidigital.py sha256=c3d507562b85bfbf83fe9fcb85d6c1e9a1f5381b60e13a797de341c31a078d03 bytes=75757 -->
## FILE: src/nidigital/system_tests/test_system_nidigital.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_system_nidigital.py`
- sha256: `c3d507562b85bfbf83fe9fcb85d6c1e9a1f5381b60e13a797de341c31a078d03`
- bytes: 75757

````python
import array
import collections
import os
import pathlib
import sys

import grpc
import hightime
import numpy
import pytest

import nidigital

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

instruments = ['PXI1Slot2', 'PXI1Slot5']
test_files_base_dir = os.path.join(os.path.dirname(__file__), 'test_files')


class SystemTests:
    @pytest.fixture(scope='function')
    def multi_instrument_session(self, session_creation_kwargs):
        with nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def single_instrument_session(self, session_creation_kwargs):
        with nidigital.Session(resource_name=instruments[0], options='Simulate=1, DriverSetup=Model:6570', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    def test_close(self, session_creation_kwargs):
        session = nidigital.Session(resource_name=','.join(instruments), options='Simulate=1, DriverSetup=Model:6570', **session_creation_kwargs)
        session.vil = 1
        session.close()
        try:
            session.vil = 1
            assert False
        except nidigital.Error as e:
            assert e.code == -1074130544

    def test_reset(self, multi_instrument_session):
        multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
        multi_instrument_session.reset()
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT

    def test_reset_device(self, multi_instrument_session):
        multi_instrument_session.selected_function = nidigital.SelectedFunction.PPMU
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.PPMU
        multi_instrument_session.reset_device()
        assert multi_instrument_session.selected_function == nidigital.SelectedFunction.DISCONNECT

    def test_self_test(self, multi_instrument_session):
        multi_instrument_session.self_test()

    def test_get_error(self, multi_instrument_session):
        try:
            multi_instrument_session.supported_instrument_models = ''
            assert False
        except nidigital.Error as e:
            assert e.code == -1074135027
            assert e.description.find('Attribute is read-only.') != -1

    def test_self_calibrate(self, multi_instrument_session):
        multi_instrument_session.self_calibrate()

    def test_channels_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.vil = 1
        ch_0_63 = multi_instrument_session.get_channel_names(indices=[0, 63])
        multi_instrument_session.channels[ch_0_63].vil = 2
        assert multi_instrument_session.pins[ch_0_63].vil == pytest.approx(2, abs=1e-3)
        ch_1 = multi_instrument_session.get_channel_names(indices=1)
        assert multi_instrument_session.pins[ch_1].vil == pytest.approx(1, abs=1e-3)

    def test_sites_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        multi_instrument_session.sites[0, 1].disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()

    def test_pins_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        # Channel-based properties
        multi_instrument_session.vil = 1
        multi_instrument_session.pins['PinA', 'PinB', 'PinC'].vil = 2
        assert multi_instrument_session.pins['DutPins'].vil == pytest.approx(2, abs=1e-3)
        assert multi_instrument_session.pins['SysPins'].vil == pytest.approx(1, abs=1e-3)

        # Methods that accept channel_list parameter
        states = multi_instrument_session.pins['PinA', 'PinB'].read_static()
        assert len(states) == 4    # 2 sites per pin

        # Methods that accept pin_list parameter
        multi_instrument_session.create_time_set('t0')
        multi_instrument_session.pins['PinA', 'PinB'].configure_time_set_drive_format(
            time_set_name='t0',
            drive_format=nidigital.DriveFormat.RL)
        drive_format = multi_instrument_session.pins['PinA', 'PinB'].get_time_set_drive_format(time_set_name='t0')
        assert drive_format == nidigital.DriveFormat.RL

    def test_chained_sites_pins_rep_cap(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.vil = 1
        multi_instrument_session.sites[0, 1].pins['PinA', 'PinB', 'PinC'].vil = 2
        assert multi_instrument_session.sites[0].pins['DutPins'].vil == pytest.approx(2, abs=1e-3)
        assert multi_instrument_session.sites[1].pins['DutPins'].vil == pytest.approx(2, abs=1e-3)

    def test_instruments_rep_cap(self, multi_instrument_session):
        multi_instrument_session.timing_absolute_delay_enabled = True
        delay0 = hightime.timedelta(microseconds=5e-3)
        delay1 = hightime.timedelta(microseconds=-5e-3)
        multi_instrument_session.instruments[instruments[0]].timing_absolute_delay = delay0
        multi_instrument_session.instruments[instruments[1]].timing_absolute_delay = delay1
        assert multi_instrument_session.instruments[instruments[0]].timing_absolute_delay == delay0
        assert multi_instrument_session.instruments[instruments[1]].timing_absolute_delay == delay1

        for instrument in instruments:
            assert multi_instrument_session.instruments[instrument].serial_number == '0'

        for instrument in instruments:
            assert multi_instrument_session.instruments[instrument].instrument_firmware_revision == '0.0.0d0'

    def test_pattern_opcode_events_rep_cap(self, multi_instrument_session):
        assert '' == multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == multi_instrument_session.pattern_opcode_events[3].exported_pattern_opcode_event_output_terminal

    def test_conditional_jump_triggers_rep_cap(self, multi_instrument_session):
        assert nidigital.TriggerType.NONE == multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type

        requested_trigger_type = nidigital.TriggerType.DIGITAL_EDGE
        multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type = requested_trigger_type
        assert requested_trigger_type == multi_instrument_session.conditional_jump_triggers[3].conditional_jump_trigger_type

    def test_rio_events_rep_cap(self, single_instrument_session):
        assert '' == single_instrument_session.rio_events[3].exported_rio_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        single_instrument_session.rio_events[3].exported_rio_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == single_instrument_session.rio_events[3].exported_rio_event_output_terminal

    def test_rio_triggers_rep_cap(self, single_instrument_session):
        assert nidigital.TriggerType.NONE == single_instrument_session.rio_triggers[3].rio_trigger_type

        requested_trigger_type = nidigital.TriggerType.DIGITAL_EDGE
        single_instrument_session.rio_triggers[3].rio_trigger_type = requested_trigger_type
        assert requested_trigger_type == single_instrument_session.rio_triggers[3].rio_trigger_type

    def test_property_boolean(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range = True
        assert multi_instrument_session.channels[channel].ppmu_allow_extended_voltage_range is True

    def test_property_int32(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].termination_mode = nidigital.TerminationMode.HIGH_Z
        assert multi_instrument_session.channels[channel].termination_mode == nidigital.TerminationMode.HIGH_Z

    def test_property_int64(self, multi_instrument_session):
        multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
        assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42

    def test_property_real64(self, multi_instrument_session):
        channel = multi_instrument_session.get_channel_names(indices=42)
        multi_instrument_session.channels[channel].ppmu_voltage_level = 4
        assert multi_instrument_session.channels[channel].ppmu_voltage_level == pytest.approx(4, rel=1e-3)

    def test_property_string(self, multi_instrument_session):
        multi_instrument_session.start_label = 'foo'
        assert multi_instrument_session.start_label == 'foo'

    def test_get_channel_names(self, multi_instrument_session):
        expected_string = [f'{instruments[0]}/{x}' for x in range(12)]
        # Sanity test few different types of input. No need for test to be exhaustive
        # since all the various types are covered by converter unit tests.
        channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
        assert multi_instrument_session.get_channel_names(indices=channel_indices) == expected_string

    def test_tdr_all_channels(self, multi_instrument_session):
        applied_offsets = multi_instrument_session.tdr(apply_offsets=False)
        assert len(applied_offsets) == multi_instrument_session.channel_count

        multi_instrument_session.apply_tdr_offsets(applied_offsets)

        channels = multi_instrument_session.get_channel_names(range(0, multi_instrument_session.channel_count))
        fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
        assert fetched_offsets == applied_offsets

    def test_tdr_some_channels(self, multi_instrument_session):
        channels = multi_instrument_session.get_channel_names([63, 0, 49, 24])
        applied_offsets = multi_instrument_session.channels[channels].tdr(apply_offsets=False)
        assert len(applied_offsets) == len(channels)

        multi_instrument_session.channels[channels].apply_tdr_offsets(applied_offsets)

        fetched_offsets = [multi_instrument_session.channels[i].tdr_offset for i in channels]
        assert fetched_offsets == applied_offsets

    def test_burst_pattern_burst_only(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=False)
        assert result is None

    def test_burst_pattern_pass_fail(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        result = multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=True)
        assert result == {0: True, 1: True, 2: True, 3: True}

    def test_source_waveform_parallel_broadcast(self, multi_instrument_session):
        '''Test methods for using source waveform with parallel sourcing and broadcast data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_broadcast
        '''
        test_name = self.test_source_waveform_parallel_broadcast.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST)

        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[i for i in range(4)])

        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def configure_session(self, session, test_name):
        session.load_pin_map(self.get_test_file_path(test_name, 'pin_map.pinmap'))

        session.load_specifications_levels_and_timing(
            specifications_file_paths=self.get_test_file_path(test_name, 'specifications.specs'),
            levels_file_paths=self.get_test_file_path(test_name, 'pin_levels.digilevels'),
            timing_file_paths=self.get_test_file_path(test_name, 'timing.digitiming'))
        session.apply_levels_and_timing(levels_sheet='pin_levels', timing_sheet='timing')

    def get_test_file_path(self, test_name, file_name):
        return os.path.join(test_files_base_dir, test_name, file_name)

    @pytest.fixture(params=[array.array, numpy.array, list])
    def source_waveform_type(self, request):
        return request.param

    def test_source_waveform_parallel_site_unique(self, multi_instrument_session, source_waveform_type):
        '''Test methods for using source waveform with parallel sourcing and site-unique data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        '''
        test_name = self.test_source_waveform_parallel_site_unique.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        num_samples = 256
        multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.SITE_UNIQUE)

        if source_waveform_type == array.array:
            source_waveform = {
                1: array.array('L', [i for i in range(num_samples)]),
                0: array.array('L', [i for i in reversed(range(num_samples))])}
        elif source_waveform_type == numpy.array:
            source_waveform = {
                1: numpy.array([i for i in range(num_samples)], dtype=numpy.uint32),
                0: numpy.array([i for i in reversed(range(num_samples))], dtype=numpy.uint32)}
        elif source_waveform_type == list:
            source_waveform = {
                1: [i for i in range(num_samples)],
                0: [i for i in reversed(range(num_samples))]}
        else:
            assert False, f"Invalid source waveform data type: {source_waveform_type}"

        multi_instrument_session.write_source_waveform_site_unique(
            waveform_name='src_wfm',
            waveform_data=source_waveform)

        multi_instrument_session.pins['HighPins'].create_capture_waveform_parallel(waveform_name='capt_wfm')

        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Pattern burst is configured to fetch num_samples samples
        fetched_waveforms = multi_instrument_session.fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)

        assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
        assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)

    @pytest.fixture(params=[tuple, int, str])
    def source_waveform_wrong_type(self, request):
        return request.param

    def test_source_waveform_parallel_site_unique_wrong_type(self, multi_instrument_session, source_waveform_wrong_type):
        '''Test methods for passing wrong types write_source_waveform_site_unique .

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        '''
        test_name = self.test_source_waveform_parallel_site_unique.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        num_samples = 256
        multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.SITE_UNIQUE)

        if source_waveform_wrong_type == tuple:
            source_waveform = ([i for i in range(num_samples)], [i for i in reversed(range(num_samples))])
        elif source_waveform_wrong_type == int:
            source_waveform = num_samples
        elif source_waveform_wrong_type == str:
            source_waveform = {
                str(1): [str(i) for i in range(num_samples)],
                str(0): [str(i) for i in reversed(range(num_samples))]}
        else:
            assert False, f"Invalid source waveform data type: {source_waveform_wrong_type}"

        with pytest.raises(TypeError):
            multi_instrument_session.write_source_waveform_site_unique(
                waveform_name='src_wfm',
                waveform_data=source_waveform)

    def test_fetch_capture_waveform_parallel(self, multi_instrument_session):
        '''Test methods for using capture waveform with parallel acquisition.

        - create_capture_waveform_parallel
        - fetch_capture_waveform
        '''
        test_name = self.test_fetch_capture_waveform_parallel.__name__
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        num_samples = 256
        multi_instrument_session.write_sequencer_register(reg=nidigital.SequencerRegister.REGISTER0, value=num_samples)

        multi_instrument_session.pins['LowPins'].create_source_waveform_parallel(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST)
        source_waveform = [i for i in range(num_samples)]
        multi_instrument_session.write_source_waveform_broadcast(waveform_name='src_wfm', waveform_data=source_waveform)

        multi_instrument_session.pins['HighPins'].create_capture_waveform_parallel(waveform_name='capt_wfm')

        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Pattern burst is configured to fetch num_samples samples
        samples_per_fetch = 8
        waveforms = collections.defaultdict(list)
        for i in range(num_samples // samples_per_fetch):
            fetched_waveform = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
                waveform_name='capt_wfm',
                samples_to_read=samples_per_fetch)
            for site in fetched_waveform:
                waveforms[site] += fetched_waveform[site]

        assert sorted(waveforms.keys()) == sorted([0, 1])
        assert all(len(waveforms[site]) == num_samples for site in waveforms)

        # Burst on subset of sites and verify fetch_capture_waveform()
        multi_instrument_session.sites[1].burst_pattern(start_label='new_pattern')
        fetched_waveform = multi_instrument_session.fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)

        assert len(fetched_waveform) == 1
        fetched_site = next(iter(fetched_waveform))
        assert fetched_site == 1
        assert len(fetched_waveform[fetched_site]) == num_samples

    def test_get_pin_results_pin_information(self, multi_instrument_session):
        # Also tests load_pin_map
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        fully_qualified_channels = [instruments[1] + '/0', instruments[0] + '/1', instruments[1] + '/11']
        pin_info = multi_instrument_session.channels[fully_qualified_channels].get_pin_results_pin_information()

        pins = [i.pin_name for i in pin_info]
        sites = [i.site_number for i in pin_info]
        channels = [i.channel_name for i in pin_info]

        assert pins == ['PinA', 'PinB', '']
        assert sites == [1, 0, -1]
        assert channels == fully_qualified_channels

    def test_history_ram_cycle_information_representation(self):
        cycle_info = nidigital.HistoryRAMCycleInformation(
            pattern_name='pat',
            time_set_name='t0',
            vector_number=42,
            cycle_number=999,
            scan_cycle_number=13,
            expected_pin_states=[[nidigital.PinState.D, nidigital.PinState.D], [nidigital.PinState.V, nidigital.PinState.V]],
            actual_pin_states=[[nidigital.PinState.PIN_STATE_NOT_ACQUIRED, nidigital.PinState.PIN_STATE_NOT_ACQUIRED],
                               [nidigital.PinState.NOT_A_PIN_STATE, nidigital.PinState.NOT_A_PIN_STATE]],
            per_pin_pass_fail=[[True, True], [False, False]])
        recreated_cycle_info = eval(repr(cycle_info))
        assert str(recreated_cycle_info) == str(cycle_info)

    def test_history_ram_cycle_information_string(self):
        cycle_info = nidigital.HistoryRAMCycleInformation(
            pattern_name='pat',
            time_set_name='t0',
            vector_number=42,
            cycle_number=999,
            scan_cycle_number=13,
            expected_pin_states=[[nidigital.PinState.D, nidigital.PinState.V], [nidigital.PinState.V, nidigital.PinState.D]],
            actual_pin_states=[[nidigital.PinState.PIN_STATE_NOT_ACQUIRED, nidigital.PinState.NOT_A_PIN_STATE], [nidigital.PinState.ZERO, nidigital.PinState.ONE]],
            per_pin_pass_fail=[[True, True], [False, False]])
        print(cycle_info)
        expected_string = '''Pattern Name        : pat
Time Set Name       : t0
Vector Number       : 42
Cycle Number        : 999
Scan Cycle Number   : 13
Expected Pin States : [[D, V], [V, D]]
Actual Pin States   : [[Pin State Not Acquired, Not a Pin State], [0, 1]]
Per Pin Pass Fail   : [[True, True], [False, False]]
'''
        assert str(cycle_info) == expected_string

    def test_fetch_history_ram_cycle_information_without_site(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='Site number on which to retrieve pattern information must be specified via sites repeated capability.'):
            multi_instrument_session.fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)

    def test_fetch_history_ram_cycle_information_position_negative(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='position should be greater than or equal to 0.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=-1, samples_to_read=-1)

    def configure_for_history_ram_test(self, session):
        test_files_folder = 'test_fetch_history_ram_cycle_information'
        self.configure_session(session, test_files_folder)

        session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        session.history_ram_trigger_type = nidigital.HistoryRAMTriggerType.FIRST_FAILURE
        session.history_ram_cycles_to_acquire = nidigital.HistoryRAMCyclesToAcquire.ALL
        session.history_ram_pretrigger_samples = 0
        session.history_ram_number_of_samples_is_finite = True

        session.sites[1].burst_pattern(start_label='new_pattern')

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_position_last(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
            position=6,
            samples_to_read=-1)

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    def test_fetch_history_ram_cycle_information_is_finite_invalid(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)
        multi_instrument_session.history_ram_number_of_samples_is_finite = False

        expected_error_description = (
            'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument '
            'is configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
        with pytest.raises(RuntimeError, match=expected_error_description):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        assert multi_instrument_session.sites[1].get_history_ram_sample_count() == 7

        multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=3)

        expected_error_description = (
            'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
        with pytest.raises(ValueError, match=expected_error_description):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)

    def test_fetch_history_ram_cycle_information_samples_to_read_negative(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        with pytest.raises(ValueError, match='samples_to_read should be greater than or equal to -1.'):
            multi_instrument_session.sites[1].fetch_history_ram_cycle_information(position=0, samples_to_read=-2)

    def test_fetch_history_ram_cycle_information_samples_to_read_zero(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=0)

        assert len(history_ram_cycle_info) == 0

    @pytest.mark.skip(reason="TODO(sbethur): Enable running on simulated session. GitHub issue #1273")
    def test_fetch_history_ram_cycle_information_samples_to_read_all(self, multi_instrument_session):
        self.configure_for_history_ram_test(multi_instrument_session)

        history_ram_cycle_info = multi_instrument_session.sites[1].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=-1)

        assert len(history_ram_cycle_info) == 7
        assert all([i.pattern_name == 'new_pattern' for i in history_ram_cycle_info])

        time_set_names = [i.time_set_name for i in history_ram_cycle_info]
        assert time_set_names == ['t0', 'tScan', 'tScan', 't2X', 't2X', 't2X', 't0']

        vector_numbers = [i.vector_number for i in history_ram_cycle_info]
        assert vector_numbers == [5, 6, 6, 7, 7, 8, 9]

        cycle_numbers = [i.cycle_number for i in history_ram_cycle_info]
        assert cycle_numbers == list(range(5, 12))

        scan_cycle_numbers = [i.scan_cycle_number for i in history_ram_cycle_info]
        assert scan_cycle_numbers == [-1, 0, 1, -1, -1, -1, -1]

        pin_names = multi_instrument_session.get_pattern_pin_names('new_pattern')
        assert pin_names == ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]

        expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
        assert expected_pin_states == [
            [[nidigital.PinState.ZERO, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]

        # If test expects actual pin state to be 'X', then value returned by the returned can be anything.
        # So, need to skip those pin states while comparing.
        actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
        actual_pin_states_expected_by_test = [
            [[nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X], [nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        assert len(actual_pin_states) == len(actual_pin_states_expected_by_test)
        for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, actual_pin_states_expected_by_test):
            for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
                for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                    if pin_state_expected_by_test is not nidigital.PinState.X:
                        assert pin_state == pin_state_expected_by_test

        # Only the first cycle returned is expected to have failures
        per_pin_pass_fail = [i.per_pin_pass_fail for i in history_ram_cycle_info]
        assert per_pin_pass_fail == [
            [[True, False, True, True, False, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
        ]

    def test_fetch_history_ram_cycle_information_no_failures(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=-1)
        assert len(history_ram_cycle_info) == 0

        history_ram_cycle_info = multi_instrument_session.sites[0].fetch_history_ram_cycle_information(
            position=0,
            samples_to_read=0)
        assert len(history_ram_cycle_info) == 0

    def test_get_pattern_pin_names(self, multi_instrument_session):
        # Also tests load_pattern
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        pattern_pin_names = multi_instrument_session.get_pattern_pin_names(start_label='new_pattern')

        assert pattern_pin_names == ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]

    def test_get_site_pass_fail(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)

        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        multi_instrument_session.burst_pattern(start_label='new_pattern')

        pass_fail = multi_instrument_session.get_site_pass_fail()
        assert pass_fail == {0: True, 1: True, 2: True, 3: True}

        pass_fail = multi_instrument_session.sites[3, 0].get_site_pass_fail()
        assert pass_fail == {3: True, 0: True}

    def test_get_fail_count(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        fail_count = multi_instrument_session.get_fail_count()
        assert fail_count == [0] * multi_instrument_session.channel_count

        fail_count = multi_instrument_session.pins['site0/LO0', 'site0/HI1', 'site2/HI3'].get_fail_count()
        assert fail_count == [0] * 3

    def test_ppmu_measure(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        voltage_measurements = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_measure(
            nidigital.PPMUMeasurementType.VOLTAGE)

        assert len(voltage_measurements) == 2

    def test_ppmu_source(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.pins['site0/LO0', 'site1/HI0'].ppmu_source()

    def test_read_static(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        pin_states = multi_instrument_session.pins['site0/LO0', 'site1/HI0'].read_static()

        assert pin_states == [nidigital.PinState.L] * 2

    def test_write_static(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)

        multi_instrument_session.pins['site0/LO0', 'site1/HI0'].write_static(
            nidigital.WriteStaticPinState.ONE)

    def test_read_sequencer_flag(self, multi_instrument_session):
        flag_state = multi_instrument_session.read_sequencer_flag(nidigital.SequencerFlag.FLAG1)
        assert flag_state is False

    def test_write_sequencer_flag(self, multi_instrument_session):
        multi_instrument_session.write_sequencer_flag(nidigital.SequencerFlag.FLAG2, True)

    def test_read_sequencer_register(self, multi_instrument_session):
        register_value = multi_instrument_session.read_sequencer_register(
            nidigital.SequencerRegister.REGISTER10)
        assert register_value == 0

    def test_write_sequencer_register(self, multi_instrument_session):
        multi_instrument_session.write_sequencer_register(
            nidigital.SequencerRegister.REGISTER15,
            65535)

    def test_configure_voltage_levels(self, multi_instrument_session):
        assert multi_instrument_session.vil == pytest.approx(0.0, abs=1e-4)
        assert multi_instrument_session.vih == pytest.approx(3.3, rel=1e-3)
        assert multi_instrument_session.vol == pytest.approx(1.6, rel=1e-3)
        assert multi_instrument_session.voh == pytest.approx(1.7, rel=1e-3)
        assert multi_instrument_session.vterm == pytest.approx(2.0, rel=1e-3)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_voltage_levels(
            vil=1.0,
            vih=2.0,
            vol=3.0,
            voh=4.0,
            vterm=5.0)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vil == pytest.approx(1.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vih == pytest.approx(2.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vol == pytest.approx(3.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].voh == pytest.approx(4.0, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].vterm == pytest.approx(5.0, rel=1e-3)

    def test_configure_active_load_levels(self, multi_instrument_session):
        assert multi_instrument_session.active_load_iol == pytest.approx(0.0015, rel=1e-3)
        assert multi_instrument_session.active_load_ioh == pytest.approx(-0.0015, rel=1e-3)
        assert multi_instrument_session.active_load_vcom == pytest.approx(2.0, rel=1e-3)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_active_load_levels(
            iol=0.024,
            ioh=-0.024,
            vcom=3.0)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_iol == pytest.approx(0.024, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_ioh == pytest.approx(-0.024, rel=1e-3)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].active_load_vcom == pytest.approx(3.0, rel=1e-3)

    def test_clock_generator_abort(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].clock_generator_abort()

    def test_clock_generator_generate_clock(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].clock_generator_generate_clock(
            1e6,
            True)

    def test_frequency_counter_measure_frequency(self, multi_instrument_session):
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].frequency_counter_measurement_time = hightime.timedelta(milliseconds=5)
        frequencies = multi_instrument_session.pins['site0/PinA', 'site1/PinC'].frequency_counter_measure_frequency()
        assert frequencies == [0] * 2

    def test_create_get_delete_time_sets(self, multi_instrument_session):
        '''Test basic time set methods.

        - create_time_set
        - delete_all_time_sets
        '''
        time_set_a = 'time_set_abc'
        time_set_b = 'time_set_123'
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_a)
        multi_instrument_session.create_time_set(time_set_b)
        multi_instrument_session.delete_all_time_sets()

    def test_configure_get_time_set_period(self, multi_instrument_session):
        '''Test time set period methods.

        - configure_time_set_period
        - get_time_set_period
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        assert multi_instrument_session.get_time_set_period(time_set_name) == hightime.timedelta(microseconds=1)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        assert multi_instrument_session.get_time_set_period(time_set_name) == time_set_period

    def test_configure_get_time_set_drive_format(self, multi_instrument_session):
        '''Test time set drive format methods.

        - configure_time_set_drive_format
        - get_time_set_drive_format
        '''
        time_set_name = 'time_set_abc'
        time_set_drive_format = nidigital.DriveFormat.SBC
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == nidigital.DriveFormat.NR
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_format(time_set_name, time_set_drive_format)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format

    def test_configure_get_time_set_edge(self, multi_instrument_session):
        '''Test time set individual edge methods.

        - configure_time_set_edge
        - get_time_set_edge
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_on = time_set_period * 0.5
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))

        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == hightime.timedelta(seconds=0)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON,
            time_set_drive_on)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on

    def test_configure_time_set_drive_edges(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_format = nidigital.DriveFormat.RL
        time_set_drive_on = time_set_period * 0.1
        time_set_drive_data = time_set_period * 0.2
        time_set_drive_return = time_set_period * 0.8
        time_set_drive_off = time_set_period * 0.9

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_edges(
            time_set_name,
            time_set_drive_format,
            time_set_drive_on,
            time_set_drive_data,
            time_set_drive_return,
            time_set_drive_off)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA) == time_set_drive_data
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN) == time_set_drive_return
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_OFF) == time_set_drive_off

    def test_configure_time_set_compare_edges_strobe(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_strobe = time_set_period * 0.5

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_compare_edges_strobe(
            time_set_name,
            time_set_strobe)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE) == time_set_strobe

    def test_configure_get_time_set_edge_multiplier(self, multi_instrument_session):
        '''Test time set edge multiplier methods.

        - configure_time_set_edge_multiplier
        - get_time_set_edge_multiplier
        '''
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_edge_multiplier = 2

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)

        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge_multiplier(time_set_name) == 1
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, time_set_edge_multiplier)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge_multiplier(time_set_name) == time_set_edge_multiplier

    def test_configure_time_set_drive_edges2x(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_drive_format = nidigital.DriveFormat.RL
        time_set_drive_on = time_set_period * 0.1
        time_set_drive_data = time_set_period * 0.2
        time_set_drive_return = time_set_period * 0.5
        time_set_drive_data2 = time_set_period * 0.7
        time_set_drive_return2 = time_set_period * 0.9
        time_set_drive_off = time_set_period * 0.9

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, 2)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_drive_edges2x(
            time_set_name,
            time_set_drive_format,
            time_set_drive_on,
            time_set_drive_data,
            time_set_drive_return,
            time_set_drive_off,
            time_set_drive_data2,
            time_set_drive_return2)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_drive_format(time_set_name) == time_set_drive_format
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_ON) == time_set_drive_on
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA) == time_set_drive_data
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN) == time_set_drive_return
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_OFF) == time_set_drive_off
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_DATA2) == time_set_drive_data2
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.DRIVE_RETURN2) == time_set_drive_return2

    def test_configure_time_set_compare_edges_strobe2x(self, multi_instrument_session):
        time_set_name = 'time_set_abc'
        time_set_period = hightime.timedelta(microseconds=10)
        time_set_strobe = time_set_period * 0.4
        time_set_strobe2 = time_set_period * 0.8

        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        multi_instrument_session.create_time_set(time_set_name)
        multi_instrument_session.configure_time_set_period(time_set_name, time_set_period)
        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_edge_multiplier(time_set_name, 2)

        multi_instrument_session.pins['site0/PinA', 'site1/PinC'].configure_time_set_compare_edges_strobe2x(
            time_set_name,
            time_set_strobe,
            time_set_strobe2)
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE) == time_set_strobe
        assert multi_instrument_session.pins['site0/PinA', 'site1/PinC'].get_time_set_edge(
            time_set_name,
            nidigital.TimeSetEdgeType.COMPARE_STROBE2) == time_set_strobe2

    def test_enable_disable_sites_single(self, multi_instrument_session):
        '''Test methods for single site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        '''
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        assert multi_instrument_session.sites[1].is_site_enabled()

        # Single site configuration
        multi_instrument_session.sites[1].disable_sites()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.sites[1].enable_sites()
        assert multi_instrument_session.sites[1].is_site_enabled()

    def test_enable_disable_sites_multiple(self, multi_instrument_session):
        '''Test methods for multiple site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        '''
        multi_instrument_session.load_pin_map(os.path.join(test_files_base_dir, "pin_map.pinmap"))
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        # Multiple site configuration
        multi_instrument_session.sites[0, 1].disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.sites[0, 1].enable_sites()
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

        # All site configuration
        multi_instrument_session.disable_sites()
        assert not multi_instrument_session.sites[0].is_site_enabled()
        assert not multi_instrument_session.sites[1].is_site_enabled()
        multi_instrument_session.enable_sites()
        assert multi_instrument_session.sites[0].is_site_enabled()
        assert multi_instrument_session.sites[1].is_site_enabled()

    def test_load_get_unload_patterns(self, multi_instrument_session):
        '''Test basic pattern methods.

        - load_pattern
        - unload_all_patterns
        '''
        test_name = 'multiple_patterns'
        multi_instrument_session.load_pin_map(self.get_test_file_path(test_name, 'pin_map.pinmap'))

        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_a.digipat'))
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_b.digipat'))

        multi_instrument_session.unload_all_patterns(unload_keep_alive_pattern=True)

    def test_configure_pattern_burst_sites(self, multi_instrument_session):
        # Also tests initiate
        test_name = 'multiple_patterns'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern_b.digipat'))
        multi_instrument_session.start_label = 'second_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL

        multi_instrument_session.sites[0, 2, 3].configure_pattern_burst_sites()

        multi_instrument_session.initiate()
        multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))
        result = multi_instrument_session.sites[0, 1, 3].get_site_pass_fail()
        assert result == {0: True, 3: True}

    def test_commit(self, multi_instrument_session):
        multi_instrument_session.cycle_number_history_ram_trigger_cycle_number = 42
        multi_instrument_session.commit()
        assert multi_instrument_session.cycle_number_history_ram_trigger_cycle_number == 42

    def test_initiate_context_manager_and_wait_until_done(self, multi_instrument_session):
        '''Test initiate's context manager and pattern completion methods.

        - with initiate
        - wait_until_done
        - is_done
        '''
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL

        with multi_instrument_session.initiate():
            # note that wait_until_done will return immediately with simulated hardware
            multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))
        assert multi_instrument_session.is_done()

    def test_abort(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.initiate()

        multi_instrument_session.abort()

    def test_abort_keep_alive(self, multi_instrument_session):
        test_name = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.start_label = 'new_pattern'
        multi_instrument_session.selected_function = nidigital.SelectedFunction.DIGITAL
        multi_instrument_session.initiate()

        multi_instrument_session.abort_keep_alive()

    def test_create_source_waveform_serial(self, multi_instrument_session):
        test_name = 'test_create_source_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.pins['LO0'].create_source_waveform_serial(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST,
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)

        # load and burst the waveform to confirm that configuration went okay
        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[1, 2])
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_create_source_waveform_from_file_tdms(self, multi_instrument_session):
        test_name = 'test_source_waveform_parallel_broadcast'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=True)

        # burst the waveform to confirm that configuration and loading went okay
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_write_source_waveform_data_from_file_tdms(self, multi_instrument_session):
        test_name = 'test_source_waveform_parallel_broadcast'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))

        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=False)
        try:  # confirm that the waveform is not yet loaded
            multi_instrument_session.burst_pattern(start_label='new_pattern')
            assert False
        except nidigital.Error as e:
            assert e.code == -1074118614
            assert e.description.find('The source waveform(s) used in the pattern(s) to be burst have not been written to source memory.'
                                      ' Ensure that you write source waveforms with niDigital Write Source Waveform.') != -1

        multi_instrument_session.write_source_waveform_data_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'))

        # burst the waveform to confirm that configuration and loading went okay
        pass_fail = multi_instrument_session.burst_pattern(start_label='new_pattern')
        assert pass_fail == {0: True, 1: True}

    def test_create_capture_waveform_serial(self, multi_instrument_session):
        test_name = 'test_create_capture_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        num_samples = 2

        multi_instrument_session.pins['HI0'].create_capture_waveform_serial(
            waveform_name='capt_wfm',
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)

        # The pattern references a wfm 'src_wfm', so we have to load it before we can burst
        multi_instrument_session.pins['LO0'].create_source_waveform_serial(
            waveform_name='src_wfm',
            data_mapping=nidigital.SourceDataMapping.BROADCAST,
            sample_width=2,
            bit_order=nidigital.BitOrder.LSB)
        multi_instrument_session.write_source_waveform_broadcast(
            waveform_name='src_wfm',
            waveform_data=[1, 2])
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Fetch to confirm that configuration went okay
        fetched_waveforms = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)
        assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
        assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)

    def test_create_capture_waveform_from_file_digicapture(self, multi_instrument_session):
        test_name = 'test_create_capture_waveform_serial'
        self.configure_session(multi_instrument_session, test_name)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        num_samples = 2

        multi_instrument_session.create_capture_waveform_from_file_digicapture(
            waveform_name='capt_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'capture_waveform.digicapture'))

        # The pattern references a wfm 'src_wfm', so we have to load it before we can burst
        multi_instrument_session.create_source_waveform_from_file_tdms(
            waveform_name='src_wfm',
            waveform_file_path=self.get_test_file_path(test_name, 'source_waveform.tdms'),
            write_waveform_data=True)
        multi_instrument_session.burst_pattern(start_label='new_pattern')

        # Fetch to confirm that configuration went okay
        fetched_waveforms = multi_instrument_session.sites[1, 0].fetch_capture_waveform(
            waveform_name='capt_wfm',
            samples_to_read=num_samples)
        assert sorted(fetched_waveforms.keys()) == sorted([0, 1])
        assert all(len(fetched_waveforms[site]) == num_samples for site in fetched_waveforms)

    def test_send_software_edge_trigger(self, multi_instrument_session):
        test_files_folder = 'simple_pattern'
        self.configure_session(multi_instrument_session, test_files_folder)
        multi_instrument_session.load_pattern(self.get_test_file_path(test_files_folder, 'pattern.digipat'))

        multi_instrument_session.start_trigger_type = nidigital.TriggerType.SOFTWARE
        multi_instrument_session.burst_pattern(start_label='new_pattern', wait_until_done=False)
        multi_instrument_session.send_software_edge_trigger(
            trigger=nidigital.SoftwareTrigger.START,
            trigger_identifier='')

        # We shouldn't time out, having sent the trigger, though in simulation it might complete, anyway
        multi_instrument_session.wait_until_done(timeout=hightime.timedelta(seconds=5.0))

    def test_specifications_levels_and_timing_single(self, multi_instrument_session):
        '''Test methods for loading, applying and unloading specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_single', 'pin_map.pinmap')
        specs = self.get_test_file_path('specifications_levels_and_timing_single', 'specs.specs')
        # Levels and timing files contain references to variables in specs1
        levels = self.get_test_file_path('specifications_levels_and_timing_single', 'levels.digilevels')
        timing = self.get_test_file_path('specifications_levels_and_timing_single', 'timing.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)
        multi_instrument_session.load_specifications_levels_and_timing(
            specifications_file_paths=specs,
            levels_file_paths=levels,
            timing_file_paths=timing)

        # Verify the loaded levels and timing sheets can be applied to hardware
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels', timing_sheet='timing')

        multi_instrument_session.unload_specifications(file_paths=specs)

        # Verify reapplying the loaded levels and timing sheets throws
        try:
            multi_instrument_session.apply_levels_and_timing(levels_sheet='levels', timing_sheet='timing')
            assert False
        except nidigital.Error as e:
            assert e.code == -1074118494
            assert e.description.find('An error occurred while getting values from a levels sheet.') != -1

    def test_specifications_levels_and_timing_multiple(self, multi_instrument_session):
        '''Test methods for loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

        specs1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
        # Contains reference to variables in specs1
        specs2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

        # All levels and timing files contain references to variables in specs1 and specs2
        levels1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
        levels2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
        timing1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
        timing2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)
        multi_instrument_session.load_specifications_levels_and_timing(
            specifications_file_paths=[specs1, specs2],  # list
            levels_file_paths=(levels1, levels2),  # tuple
            timing_file_paths=[timing1, timing2])

        # Verify the loaded levels and timing sheets can be applied to hardware
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels2', timing_sheet='timing1')

        multi_instrument_session.unload_specifications(file_paths=[specs1, specs2])

        # Verify reapplying the loaded levels and timing sheets throws
        try:
            multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
            assert False
        except nidigital.Error as e:
            assert e.code == -1074118494
            assert e.description.find('An error occurred while getting values from a levels sheet.') != -1

    def test_specifications_levels_and_timing_load_sequentially(self, multi_instrument_session):
        '''Test methods for separately loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        '''
        pinmap = self.get_test_file_path('specifications_levels_and_timing_multiple', 'pin_map.pinmap')

        specs1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs1.specs')
        # Contains reference to variables in specs1
        specs2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'specs2.specs')

        # All levels and timing files contain references to variables in specs1 and specs2
        levels1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels1.digilevels')
        levels2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'levels2.digilevels')
        timing1 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing1.digitiming')
        timing2 = self.get_test_file_path('specifications_levels_and_timing_multiple', 'timing2.digitiming')

        multi_instrument_session.load_pin_map(file_path=pinmap)

        # Load just the specs files first, in two separate calls
        multi_instrument_session.load_specifications_levels_and_timing(specifications_file_paths=specs1)
        multi_instrument_session.load_specifications_levels_and_timing(specifications_file_paths=[specs2])

        # Then load both the levels together
        multi_instrument_session.load_specifications_levels_and_timing(levels_file_paths=[levels2, levels1])

        # Then load the two timing files in two separate calls
        multi_instrument_session.load_specifications_levels_and_timing(timing_file_paths=[timing2])
        multi_instrument_session.load_specifications_levels_and_timing(timing_file_paths=[timing1])

        # Verify the loaded levels and timing sheets can be applied to hardware
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
        multi_instrument_session.apply_levels_and_timing(levels_sheet='levels2', timing_sheet='timing1')

        multi_instrument_session.unload_specifications(file_paths=specs1)
        multi_instrument_session.unload_specifications(file_paths=(specs2))

        # Verify reapplying the loaded levels and timing sheets throws
        try:
            multi_instrument_session.apply_levels_and_timing(levels_sheet='levels1', timing_sheet='timing2')
            assert False
        except nidigital.Error as e:
            assert e.code == -1074118494
            assert e.description.find('An error occurred while getting values from a levels sheet.') != -1

    def test_apply_levels_and_timing_initial_states(self, multi_instrument_session):
        self.configure_session(multi_instrument_session, 'simple_pattern')
        multi_instrument_session.sites[0, 2].apply_levels_and_timing(
            levels_sheet='pin_levels',
            timing_sheet='timing',
            initial_state_high_pins=['HI0', 'LowPins'],
            initial_state_tristate_pins='HI1, HI2')

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, multi_instrument_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(multi_instrument_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, multi_instrument_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            multi_instrument_session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    def test_enable_match_fail_combination(self, multi_instrument_session):
        import nisync

        test_name = self.test_enable_match_fail_combination.__name__
        multi_instrument_session.load_pin_map(self.get_test_file_path(test_name, 'pin_map.pinmap'))
        multi_instrument_session.load_pattern(self.get_test_file_path(test_name, 'pattern.digipat'))
        multi_instrument_session.load_specifications_levels_and_timing(
            specifications_file_paths=self.get_test_file_path(test_name, 'specifications.specs'),
            levels_file_paths=self.get_test_file_path(test_name, 'pin_levels.digilevels'),
            timing_file_paths=self.get_test_file_path(test_name, 'timing.digitiming'))
        multi_instrument_session.apply_levels_and_timing(levels_sheet='pin_levels', timing_sheet='timing')
        with nisync.Session('6674T') as sync_session:
            multi_instrument_session.enable_match_fail_combination(sync_session)
            multi_instrument_session.burst_pattern(start_label='new_pattern')
            multi_instrument_session.read_sequencer_flag(nidigital.SequencerFlag.FLAG0)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = nidigital.GrpcSessionOptions(grpc_channel, "")
        return {'grpc_options': grpc_options}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/_grpc_stub_interpreter.py/enable_match_fail_combination.py.mako sha256=36e56f0e50919195ded2afc55e697f5cf6c004d59de2561c24f82fa25bd4969c bytes=436 -->
## FILE: src/nidigital/templates/_grpc_stub_interpreter.py/enable_match_fail_combination.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/_grpc_stub_interpreter.py/enable_match_fail_combination.py.mako`
- sha256: `36e56f0e50919195ded2afc55e697f5cf6c004d59de2561c24f82fa25bd4969c`
- bytes: 436

````mako
## This file is empty. We won't support gRPC, for now.
## Even though gRPC Device supports the function, the nisync Python API lacks gRPC support, so there's no point.
## If a user tries to call enable_match_fail_combination with a session runing on a gRPC Device Server, they will get an error
## because the method does not exist in _grpc_stub_interpreter.py.
## Most likely it will be an AttributeError, though it hasn't been tested.
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/_grpc_stub_interpreter.py/fancy_fetch_capture_waveform.py.mako sha256=fdca410b5a056f12f0dfb3d32431a166a10bbf2b4ef5fe4d06cfd160b6442fc0 bytes=560 -->
## FILE: src/nidigital/templates/_grpc_stub_interpreter.py/fancy_fetch_capture_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/_grpc_stub_interpreter.py/fancy_fetch_capture_waveform.py.mako`
- sha256: `fdca410b5a056f12f0dfb3d32431a166a10bbf2b4ef5fe4d06cfd160b6442fc0`
- bytes: 560

````mako

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchCaptureWaveformU32,
            grpc_types.FetchCaptureWaveformU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, samples_to_read=samples_to_read, timeout=timeout),
        )
        ## Modified (vs. default generated code) to return bytes() and both size outputs
        return bytes(response.data), response.actual_num_waveforms, response.actual_samples_per_waveform
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/_library_interpreter.py/enable_match_fail_combination.py.mako sha256=d078418fc20bb0a5ef325c0d62071a41b94a5f4036dae944500c5dcc045a5dce bytes=621 -->
## FILE: src/nidigital/templates/_library_interpreter.py/enable_match_fail_combination.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/_library_interpreter.py/enable_match_fail_combination.py.mako`
- sha256: `d078418fc20bb0a5ef325c0d62071a41b94a5f4036dae944500c5dcc045a5dce`
- bytes: 621

````mako

    def enable_match_fail_combination(self, sessions, sync_session):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        sync_session_ctype = _visatype.ViSession(sync_session)  # case S110
        error_code = self._library.niDigital_EnableMatchFailCombination(session_count_ctype, sessions_ctype, sync_session_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/_library_interpreter.py/fancy_fetch_capture_waveform.py.mako sha256=ea5f7a35ba7edbdd4c941748e12676c270432f6806994a440298b04d7ac83eb6 bytes=2662 -->
## FILE: src/nidigital/templates/_library_interpreter.py/fancy_fetch_capture_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/_library_interpreter.py/fancy_fetch_capture_waveform.py.mako`
- sha256: `ea5f7a35ba7edbdd4c941748e12676c270432f6806994a440298b04d7ac83eb6`
- bytes: 2662

````mako

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        # We cannot use codegen without major modifications to the code generator
        # This function uses two 'ivi-dance' parameters and then multiplies them together - see
        # the (modified) line below
        # Also, we want to return the two sizes that normally wouldn't be returned
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value)  # case S200 (modified)
        data_size = actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value  # case B620 (modified)
        data_array = array.array("L", [0]) * data_size  # case B620
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViUInt32)  # case B620
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, actual_num_waveforms_ctype.value, actual_samples_per_waveform_ctype.value  # (modified)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_burst_pattern.py.mako sha256=4823fdbbcf5e2731f7a7bc6c789e8e9cd77d847f26c1dd7f122ddcdec140dca7 bytes=682 -->
## FILE: src/nidigital/templates/session.py/fancy_burst_pattern.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_burst_pattern.py.mako`
- sha256: `4823fdbbcf5e2731f7a7bc6c789e8e9cd77d847f26c1dd7f122ddcdec140dca7`
- bytes: 682

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _burst_pattern(). If wait_until_done is True, calls get_site_pass_fail() to obtain the pass/fail
    results and returns it to the caller.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._burst_pattern(start_label, select_digital_function, wait_until_done, timeout)

        if wait_until_done:
            return self.get_site_pass_fail()
        else:
            return None
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_enable_match_fail_combination.py.mako sha256=6dd387fd0c7cd52a19138b84a275a52f4a481496cf1779b3bb176abd845686a7 bytes=374 -->
## FILE: src/nidigital/templates/session.py/fancy_enable_match_fail_combination.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_enable_match_fail_combination.py.mako`
- sha256: `6dd387fd0c7cd52a19138b84a275a52f4a481496cf1779b3bb176abd845686a7`
- bytes: 374

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
%>\
    def ${f['python_name']}(self, sync_session):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._interpreter.enable_match_fail_combination([self._interpreter.get_session_handle()], sync_session.session_handle)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_fetch_capture_waveform.py.mako sha256=734d1c14df9c48a7f62e2ba0a65f03577766b3f7fd4024b056f9f4006bae698c bytes=1110 -->
## FILE: src/nidigital/templates/session.py/fancy_fetch_capture_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_fetch_capture_waveform.py.mako`
- sha256: `734d1c14df9c48a7f62e2ba0a65f03577766b3f7fd4024b056f9f4006bae698c`
- bytes: 1110

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        data, actual_num_waveforms, actual_samples_per_waveform = self._interpreter.fetch_capture_waveform(self._repeated_capability, waveform_name, samples_to_read, timeout)

        # Get the site list
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        waveforms = {}

        mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            waveforms[site_list[i]] = mv[start:end]

        return waveforms
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_fetch_history_ram_cycle_information.py.mako sha256=8b2359411c4803d1ddedf243f791c111907d6b9aa620394f7bc4cda073789935 bytes=4479 -->
## FILE: src/nidigital/templates/session.py/fancy_fetch_history_ram_cycle_information.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_fetch_history_ram_cycle_information.py.mako`
- sha256: `8b2359411c4803d1ddedf243f791c111907d6b9aa620394f7bc4cda073789935`
- bytes: 4479

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to History RAM fetch functions'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Extract the site number and pin list from repeated capability
        repeated_capability_lists = _converters.convert_chained_repeated_capability_to_parts(self._repeated_capability)
        site = repeated_capability_lists[0]
        if not site.startswith('site'):
            raise ValueError('Site number on which to retrieve pattern information must be specified via sites repeated capability.')
        pins = '' if len(repeated_capability_lists) == 1 else repeated_capability_lists[1]

        # Put site back into repeated capability container; it will be used by other
        # sites-rep-cap-based methods that will be called later.
        self._repeated_capability = site

        if position < 0:
            raise ValueError('position should be greater than or equal to 0.')

        if samples_to_read < -1:
            raise ValueError('samples_to_read should be greater than or equal to -1.')

        # site is passed as repeated capability
        samples_available = self.get_history_ram_sample_count()
        if position > samples_available:
            raise ValueError('position: Specified value = {}, Maximum value = {}.'.format(position, samples_available - 1))

        if samples_to_read == -1:
            with _NoChannel(session=self):
                if not self.history_ram_number_of_samples_is_finite:
                    raise RuntimeError(
                        'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument is '
                        'configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
            samples_to_read = samples_available - position

        if position + samples_to_read > samples_available:
            raise ValueError(
                'position: Specified value = {}, samples_to_read: Specified value = {}; Samples available = {}.'
                .format(position, samples_to_read, samples_available - position))

        pattern_names = {}
        time_set_names = {}
        cycle_infos = []
        for _ in range(samples_to_read):

            # site is passed as repeated capability
            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._${f['python_name']}(position)

            if pattern_index not in pattern_names:
                # Repeated capability is not used
                pattern_names[pattern_index] = self._get_pattern_name(pattern_index)
            pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                # Repeated capability is not used
                time_set_names[time_set_index] = self._get_time_set_name(time_set_index)
            time_set_name = time_set_names[time_set_index]

            # site is passed as repeated capability
            scan_cycle_number = self._fetch_history_ram_scan_cycle_number(position)

            vector_expected_pin_states = []
            vector_actual_pin_states = []
            vector_per_pin_pass_fail = []
            for dut_cycle_index in range(num_dut_cycles):
                # site is passed as repeated capability
                cycle_expected_pin_states, cycle_actual_pin_states, cycle_per_pin_pass_fail = self._fetch_history_ram_cycle_pin_data(pins, position, dut_cycle_index)
                vector_expected_pin_states.append(cycle_expected_pin_states)
                vector_actual_pin_states.append(cycle_actual_pin_states)
                vector_per_pin_pass_fail.append(cycle_per_pin_pass_fail)

            cycle_infos.append(history_ram_cycle_information.HistoryRAMCycleInformation(
                pattern_name=pattern_name,
                time_set_name=time_set_name,
                vector_number=vector_number,
                cycle_number=cycle_number,
                scan_cycle_number=scan_cycle_number,
                expected_pin_states=vector_expected_pin_states,
                actual_pin_states=vector_actual_pin_states,
                per_pin_pass_fail=vector_per_pin_pass_fail))
            position += 1

        return cycle_infos
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_get_pin_results_pin_information.py.mako sha256=ac5a0efaf08d882a29d381117c20462d908f33e02f23a81f84b50f34f29e7aaf bytes=1231 -->
## FILE: src/nidigital/templates/session.py/fancy_get_pin_results_pin_information.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_get_pin_results_pin_information.py.mako`
- sha256: `ac5a0efaf08d882a29d381117c20462d908f33e02f23a81f84b50f34f29e7aaf`
- bytes: 1231

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch()/_read() with a nicer interface'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        PinInfo = collections.namedtuple('PinInformation', ['pin_name', 'site_number', 'channel_name'])

        pin_indexes, site_numbers, channel_indexes = self._${f['python_name']}()
        assert len(pin_indexes) == len(site_numbers), "length of returned arrays don't match"
        assert len(pin_indexes) == len(channel_indexes), "length of returned arrays don't match"

        pin_infos = []
        for i in range(len(pin_indexes)):
            pin_name = "" if pin_indexes[i] == -1 else self._get_pin_name(pin_indexes[i])
            channel_names = self.get_channel_names(channel_indexes[i] - 1)  # channel_indexes are 1-based
            assert 1 == len(channel_names)
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_names[0]))

        return pin_infos
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_get_site_pass_fail.py.mako sha256=c7d456a375310a239eedc6b56d4bc320c8ecbbc5b64b6a7349b6192ec97de76d bytes=790 -->
## FILE: src/nidigital/templates/session.py/fancy_get_site_pass_fail.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_get_site_pass_fail.py.mako`
- sha256: `c7d456a375310a239eedc6b56d4bc320c8ecbbc5b64b6a7349b6192ec97de76d`
- bytes: 790

````mako
<%page args="f, config, method_template"/>\
<%
    '''Gets pass/fail results and site numbers corresponding to them, then returns
    dictionary where each key is a site number and value is a bool indicating pass/fail'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # For site_list, we just use the repeated capability
        result_list = self._get_site_pass_fail()
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.PASS_FAIL)
        assert len(site_list) == len(result_list)

        return dict(zip(site_list, result_list))
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_load_specifications_levels_and_timing.py.mako sha256=10e0b72df85338101f6d3d63603c7f5562fda9aee8004462bb7816ed8caf3511 bytes=973 -->
## FILE: src/nidigital/templates/session.py/fancy_load_specifications_levels_and_timing.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_load_specifications_levels_and_timing.py.mako`
- sha256: `10e0b72df85338101f6d3d63603c7f5562fda9aee8004462bb7816ed8caf3511`
- bytes: 973

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _load_specifications(), _load_levels(), and _load_timing().'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._call_method_with_iterable(self._load_specifications, specifications_file_paths)
        self._call_method_with_iterable(self._load_levels, levels_file_paths)
        self._call_method_with_iterable(self._load_timing, timing_file_paths)

    ## Define the private method below the public method so that lock decorator gets added to the public method
    def _call_method_with_iterable(self, method, files):
        if files is None:
            return
        if isinstance(files, str):
            files = [files]
        for f in files:
            method(f)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_unload_specifications.py.mako sha256=bd0c8ce67d2ac4c4ff31cba368b58fc2cb986ea3494bba6a1b4ea942515de448 bytes=446 -->
## FILE: src/nidigital/templates/session.py/fancy_unload_specifications.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_unload_specifications.py.mako`
- sha256: `bd0c8ce67d2ac4c4ff31cba368b58fc2cb986ea3494bba6a1b4ea942515de448`
- bytes: 446

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _unload_specifications().'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._call_method_with_iterable(self._unload_specifications, file_paths)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/templates/session.py/fancy_write_source_waveform_site_unique.py.mako sha256=8ee12114f938a7b58c9ba592c66c95e5f0637817f3adc62bee07d97d1c378684 bytes=2811 -->
## FILE: src/nidigital/templates/session.py/fancy_write_source_waveform_site_unique.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidigital/templates/session.py/fancy_write_source_waveform_site_unique.py.mako`
- sha256: `8ee12114f938a7b58c9ba592c66c95e5f0637817f3adc62bee07d97d1c378684`
- bytes: 2811

````mako
<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        from collections.abc import Mapping
        if not isinstance(waveform_data, Mapping):
            raise TypeError("Expecting waveform_data to be a dictionary but got {}".format(type(waveform_data)))
        site_list = []
        # We assume all the entries are the same length (we'll check later) to make the array the correct size
        # Get an entry from the dictionary from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
        if len(waveform_data) == 0:
            actual_samples_per_waveform = 0
        else:
            actual_samples_per_waveform = len(waveform_data[next(iter(waveform_data))])
        data = array.array('L', [0]) * (len(waveform_data) * actual_samples_per_waveform)
        mv = memoryview(data)

        i = 0
        for site in waveform_data:
            if len(waveform_data[site]) != actual_samples_per_waveform:
                raise ValueError('Mismatched length of waveforms. All must be the same length.')
            # Check the type by using string comparison so that we don't import numpy unnecessarily.
            if str(type(waveform_data[site])).find("'numpy.ndarray'") != -1:
                import numpy
                if waveform_data[site].dtype == numpy.uint32:
                    wfm = array.array('L', waveform_data[site])
                else:
                    raise TypeError("Unsupported dtype for waveform_data array element type. Is {}, expected {}".format(waveform_data[site].dtype, numpy.int32))

            elif isinstance(waveform_data[site], array.array):
                if waveform_data[site].typecode == 'L':
                    wfm = waveform_data[site]
                else:
                    raise TypeError('Wrong waveform_data array element type. Must be unsigned 32 bit int ("L"), was {}'.format(waveform_data[site].typecode))

            elif isinstance(waveform_data[site], list):
                wfm = array.array('L', waveform_data[site])

            else:
                raise TypeError('Unknown array type: {}'.format(type(waveform_data[site])))

            site_list.append(site)

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = wfm

            i += 1

        self.sites[site_list]._write_source_waveform_site_unique_u32(waveform_name, len(waveform_data), actual_samples_per_waveform, data)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/unit_tests/test_nidigital.py sha256=ab5bdad4c60f120ee1a6d5d9723e9e83a8908ed8693f01536b39ca238d32e7a3 bytes=27168 -->
## FILE: src/nidigital/unit_tests/test_nidigital.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/unit_tests/test_nidigital.py`
- sha256: `ab5bdad4c60f120ee1a6d5d9723e9e83a8908ed8693f01536b39ca238d32e7a3`
- bytes: 27168

````python
import _mock_helper

import nidigital
import nitclk

import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

session_id_for_test = 42


class TestSession:
    class PatchedLibrary(nidigital._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niDigital_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    class PatchedTClkLibrary(nitclk._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niTClk_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nidigital._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.patched_tclk_library = self.PatchedTClkLibrary(None)
        self.patched_tclk_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=self.patched_tclk_library)
        self.patched_tclk_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

        # The side effect must be set for this, because it's called.
        # No need to set argument values; the method is tested in nifake unit tests, not here.
        self.patched_library.niDigital_SetRuntimeEnvironment.side_effect = self.side_effects_helper.niDigital_SetRuntimeEnvironment

        self.patched_library.niDigital_InitWithOptions.side_effect = self.side_effects_helper.niDigital_InitWithOptions
        self.side_effects_helper['InitWithOptions']['newVi'] = session_id_for_test

        self.patched_library.niDigital_close.side_effect = self.side_effects_helper.niDigital_close

        self.patched_library.niDigital_LockSession.side_effect = self.side_effects_helper.niDigital_LockSession
        self.side_effects_helper['LockSession']['callerHasLock'] = True

        self.patched_library.niDigital_UnlockSession.side_effect = self.side_effects_helper.niDigital_UnlockSession
        self.side_effects_helper['UnlockSession']['callerHasLock'] = True

        # For trying to set `_all_channels_in_session` in the Session constructor
        self.patched_library.niDigital_GetAttributeViInt32.side_effect = self.side_effects_helper.niDigital_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['value'] = 1  # channel_count
        self.patched_library.niDigital_GetChannelNameFromString.side_effect = self.side_effects_helper.niDigital_GetChannelNameFromString
        self.side_effects_helper['GetChannelNameFromString']['name'] = '0'  # get_channel_names()

        # for niDigital_FetchHistoryRAMCycleInformation_looping
        self.pattern_indices_looping = [0, 0, 0, 0, 0, 0, 0]
        self.time_set_indices_looping = [0, 1, 1, 2, 2, 2, 0]
        self.vector_numbers_looping = [5, 6, 6, 7, 7, 8, 9]
        self.cycle_numbers_looping = [5, 6, 7, 8, 9, 10, 11]
        self.num_duty_cycles_looping = [1, 1, 1, 2, 2, 2, 1]

        # for niDigital_GetTimeSetName_looping
        self.time_set_name_looping = ['t0', 'tScan', 't2X']

        # for niDigital_FetchHistoryRAMScanCycleNumber_looping
        self.scan_cycle_number_looping = [-1, 0, 1, -1, -1, -1, -1]

        # for niDigital_FetchHistoryRAMCyclePinData_looping
        self.expected_pin_states_looping = [
            [[nidigital.PinState.ZERO, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        self.actual_pin_states_looping = [
            [[nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        self.per_pin_pass_fail_looping = [
            [[True, False, True, True, False, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
        ]

        # for niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        self.expected_pin_list_check_pins_looping = None
        self.expected_pin_states_check_pins_looping = [[[nidigital.PinState.ZERO, nidigital.PinState.H]]]
        self.actual_pin_states_check_pins_looping = [[[nidigital.PinState.L, nidigital.PinState.L]]]
        self.per_pin_pass_fail_check_pins_looping = [[[True, False]]]

        # for niDigital_GetHistoryRAMSampleCount_check_site_looping
        self.iteration_check_site_looping = 0
        self.site_numbers_looping = [0, 1, 2]

    def teardown_method(self, method):
        self.patched_tclk_library_singleton_get.stop()
        self.patched_library_singleton_get.stop()

    # API Tests

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
                session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_last(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['patternIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['timeSetIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['vectorNumber'] = 9
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['cycleNumber'] = 11
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['numDutCycles'] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.side_effects_helper.niDigital_GetTimeSetName
        self.side_effects_helper['GetTimeSetName']['name'] = 't0'
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        self.side_effects_helper['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCyclePinData
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualNumPinData'] = 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['expectedPinStates'] = [nidigital.PinState.X.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualPinStates'] = [nidigital.PinState.NOT_A_PIN_STATE.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['perPinPassFail'] = [True] * 8
        with nidigital.Session('') as session:
            history_ram_cycle_info = session.sites[1].fetch_history_ram_cycle_information(
                position=6,
                samples_to_read=-1)
            self.patched_library.niDigital_FetchHistoryRAMCycleInformation.assert_called_once()
            assert self.patched_library.niDigital_GetPatternName.call_count == 2
            assert self.patched_library.niDigital_GetTimeSetName.call_count == 2
            self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.assert_called_once()
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 2

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite

        with nidigital.Session('') as session:
            assert session.sites[1].get_history_ram_sample_count() == 7

            expected_error_description = (
                'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
            with pytest.raises(ValueError, match=expected_error_description):
                session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCycleInformation_looping(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        sample_index_int = int(sample_index.value)
        pattern_index.contents.value = self.pattern_indices_looping[sample_index_int]
        time_set_index.contents.value = self.time_set_indices_looping[sample_index_int]
        vector_number.contents.value = self.vector_numbers_looping[sample_index_int]
        cycle_number.contents.value = self.cycle_numbers_looping[sample_index_int]
        num_dut_cycles.contents.value = self.num_duty_cycles_looping[sample_index_int]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_GetTimeSetName_looping(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        time_set_index_int = int(time_set_index.value)
        if int(name_buffer_size.value) == 0:
            return (len(self.time_set_name_looping[time_set_index_int]))
        bytes_to_copy = self.time_set_name_looping[time_set_index_int].encode('ascii')
        for i in range(0, len(bytes_to_copy)):
            name[i] = bytes_to_copy[i]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMScanCycleNumber_looping(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        sample_index_int = int(sample_index.value)
        scan_cycle_number.contents.value = self.scan_cycle_number_looping[sample_index_int]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCyclePinData_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(self.expected_pin_states_looping[sample_index_int][dut_cycle_index_int])
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_looping[sample_index_int][dut_cycle_index_int][i].value
            actual_pin_states[i] = self.actual_pin_states_looping[sample_index_int][dut_cycle_index_int][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_looping[sample_index_int][dut_cycle_index_int][i]
        return 0

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_all(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.niDigital_FetchHistoryRAMCycleInformation_looping
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.niDigital_GetTimeSetName_looping
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.niDigital_FetchHistoryRAMScanCycleNumber_looping
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.niDigital_FetchHistoryRAMCyclePinData_looping
        self.patched_library.niDigital_GetPatternPinList.side_effect = self.side_effects_helper.niDigital_GetPatternPinList
        pin_list = ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]
        self.side_effects_helper['GetPatternPinList']['pinList'] = ','.join(pin_list)
        with nidigital.Session('') as session:
            history_ram_cycle_info = session.sites[1].fetch_history_ram_cycle_information(
                position=0,
                samples_to_read=-1)
            assert self.patched_library.niDigital_FetchHistoryRAMCycleInformation.call_count == 7
            assert self.patched_library.niDigital_GetPatternName.call_count == 2  # there's only one pattern, so this is a 2
            assert self.patched_library.niDigital_GetTimeSetName.call_count == 6  # 3 time sets, so this is a 6
            assert self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.call_count == 7
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 20  # 10 DUT cycles

            assert len(history_ram_cycle_info) == 7
            assert all([i.pattern_name == 'new_pattern' for i in history_ram_cycle_info])

            time_set_names = [i.time_set_name for i in history_ram_cycle_info]
            assert time_set_names == ['t0', 'tScan', 'tScan', 't2X', 't2X', 't2X', 't0']

            vector_numbers = [i.vector_number for i in history_ram_cycle_info]
            assert vector_numbers == [5, 6, 6, 7, 7, 8, 9]

            cycle_numbers = [i.cycle_number for i in history_ram_cycle_info]
            assert cycle_numbers == list(range(5, 12))

            scan_cycle_numbers = [i.scan_cycle_number for i in history_ram_cycle_info]
            assert scan_cycle_numbers == [-1, 0, 1, -1, -1, -1, -1]

            pin_names = session.get_pattern_pin_names('new_pattern')
            assert self.patched_library.niDigital_GetPatternPinList.call_count == 2
            assert pin_names == pin_list

        expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
        assert expected_pin_states == self.expected_pin_states_looping

        # If test expects actual pin state to be 'X', then value returned by the API can be anything.
        # So, need to skip those pin states while comparing.
        actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
        assert len(actual_pin_states) == len(self.actual_pin_states_looping)
        for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, self.actual_pin_states_looping):
            for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
                for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                    if pin_state_expected_by_test is not nidigital.PinState.X:
                        assert pin_state == pin_state_expected_by_test

        # Only the first cycle returned is expected to have failures
        per_pin_pass_fail = [i.per_pin_pass_fail for i in history_ram_cycle_info]
        assert per_pin_pass_fail == self.per_pin_pass_fail_looping

    # Helper function for validating pin list behavior in fetch_history_ram_cycle_information.
    def niDigital_FetchHistoryRAMCyclePinData_check_pins_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(self.expected_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int])
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int][i].value
            actual_pin_states[i] = self.actual_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_check_pins_looping[sample_index_int][dut_cycle_index_int][i]
        assert self.expected_pin_list_check_pins_looping is not None
        assert pin_list.value.decode('ascii') == self.expected_pin_list_check_pins_looping
        return 0

    def test_fetch_history_ram_cycle_information_pin_list(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 1
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['patternIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['timeSetIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['vectorNumber'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['cycleNumber'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['numDutCycles'] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.side_effects_helper.niDigital_GetTimeSetName
        self.side_effects_helper['GetTimeSetName']['name'] = 't0'
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        self.side_effects_helper['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        with nidigital.Session('') as session:
            self.expected_pin_list_check_pins_looping = 'PinA,PinB'
            session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)
            self.expected_pin_list_check_pins_looping = ''
            session.sites[0].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 4

    # Helper function for validating site behavior in fetch_history_ram_cycle_information.
    def niDigital_GetHistoryRAMSampleCount_check_site_looping(self, vi, site, sample_count):  # noqa: N802
        assert site.value.decode('ascii') == f'site{self.site_numbers_looping[self.iteration_check_site_looping]}'
        sample_count.contents.value = 0  # we don't care if this is right as long as the fetch does not error
        self.iteration_check_site_looping += 1
        return 0

    def test_fetch_history_ram_cycle_information_site_n(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.niDigital_GetHistoryRAMSampleCount_check_site_looping
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 1

        with nidigital.Session('') as session:
            for s in self.site_numbers_looping:
                session.sites[s].fetch_history_ram_cycle_information(position=0, samples_to_read=0)
            assert self.patched_library.niDigital_GetHistoryRAMSampleCount.call_count == len(self.site_numbers_looping)

    def test_pin_state_enum_print(self):

        assert str(nidigital.PinState.ZERO) == '0'
        assert str(nidigital.PinState.ONE) == '1'
        assert str(nidigital.PinState.NOT_A_PIN_STATE) == 'Not a Pin State'
        assert str(nidigital.PinState.PIN_STATE_NOT_ACQUIRED) == 'Pin State Not Acquired'
        assert str(nidigital.PinState.L) == 'L'
        assert str(nidigital.PinState.H) == 'H'
        assert str(nidigital.PinState.X) == 'X'
        assert str(nidigital.PinState.M) == 'M'
        assert str(nidigital.PinState.V) == 'V'
        assert str(nidigital.PinState.D) == 'D'
        assert str(nidigital.PinState.E) == 'E'

    def test_write_static_pin_state_enum_print(self):

        assert str(nidigital.WriteStaticPinState.ZERO) == '0'
        assert str(nidigital.WriteStaticPinState.ONE) == '1'
        assert str(nidigital.WriteStaticPinState.X) == 'X'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/examples/nidmm_fetch_waveform.py sha256=b9d5b901ab06f1623b52cee4fcebd02abd6674ed7d5f6558f3c819d5a6bc87e8 bytes=2218 -->
## FILE: src/nidmm/examples/nidmm_fetch_waveform.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/examples/nidmm_fetch_waveform.py`
- sha256: `b9d5b901ab06f1623b52cee4fcebd02abd6674ed7d5f6558f3c819d5a6bc87e8`
- bytes: 2218

````python
#!/usr/bin/python

import argparse
import nidmm
import sys
import time


def example(resource_name, options, function, range, points, rate):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_waveform_acquisition(measurement_function=nidmm.Function[function], range=range, rate=rate, waveform_points=points)
        with session.initiate():
            while True:
                time.sleep(0.1)
                backlog, acquisition_state = session.read_status()
                if acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG:
                    break
                measurements = session.fetch_waveform(array_size=backlog)
                print(measurements)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a waveform acquisition using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-f', '--function', default='WAVEFORM_VOLTAGE', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-p', '--points', default=10, type=int, help='Specifies the number of points to acquire before the waveform acquisition completes.')
    parser.add_argument('-s', '--rate', default=1000, type=int, help='Specifies the rate of the acquisition in samples per second.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.points, args.rate)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'WAVEFORM_VOLTAGE', 10, 10, 1000)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/examples/nidmm_measurement.py sha256=5efe92e9e65ab78411c241de56a700822520ea54f99cae0a790c4058761b0487 bytes=1706 -->
## FILE: src/nidmm/examples/nidmm_measurement.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/examples/nidmm_measurement.py`
- sha256: `5efe92e9e65ab78411c241de56a700822520ea54f99cae0a790c4058761b0487`
- bytes: 1706

````python
#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, option_string, function, range, digits):
    with nidmm.Session(resource_name=resource_name, options=option_string) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        print(session.read())


def _main(argsv):
    supported_functions = list(nidmm.Function.__members__.keys())
    parser = argparse.ArgumentParser(description='Performs a single measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-f', '--function', default=supported_functions[0], choices=supported_functions, type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 6.5)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/examples/nidmm_multi_point_measurement.py sha256=4c58decd72ba4008b01fa9bddd8413dbb64db786cde435fa18fe3e20e100953a bytes=2138 -->
## FILE: src/nidmm/examples/nidmm_multi_point_measurement.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/examples/nidmm_multi_point_measurement.py`
- sha256: `4c58decd72ba4008b01fa9bddd8413dbb64db786cde435fa18fe3e20e100953a`
- bytes: 2138

````python
#!/usr/bin/python

import argparse
import nidmm
import sys


def example(resource_name, options, function, range, digits, samples, triggers):
    with nidmm.Session(resource_name=resource_name, options=options) as session:
        session.configure_measurement_digits(measurement_function=nidmm.Function[function], range=range, resolution_digits=digits)
        session.configure_multi_point(trigger_count=triggers, sample_count=samples)
        measurements = session.read_multi_point(array_size=samples)
        print('Measurements: ', measurements)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a multipoint measurement using the NI-DMM API.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digital multimeter.')
    parser.add_argument('-f', '--function', default='DC_VOLTS', choices=nidmm.Function.__members__.keys(), type=str.upper, help='Measurement function.')
    parser.add_argument('-r', '--range', default=10, type=float, help='Measurement range.')
    parser.add_argument('-d', '--digits', default=6.5, type=float, help='Digits of resolution for the measurement.')
    parser.add_argument('-s', '--samples', default=10, type=int, help='The number of measurements the DMM makes.')
    parser.add_argument('-t', '--triggers', default=1, type=int, help='Sets the number of triggers you want the DMM to receive before returning to the Idle state.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.function, args.range, args.digits, args.samples, args.triggers)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '4082', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'DC_VOLTS', 10, 6.5, 10, 1)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nidmm/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nidmm/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/__init__.py sha256=35e07284af0fefbd69c13414db63aadf646ee423ca4a38040965a315657d20d8 bytes=1921 -->
## FILE: src/nidmm/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/__init__.py`
- sha256: `35e07284af0fefbd69c13414db63aadf646ee423ca4a38040965a315657d20d8`
- bytes: 1921

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

if 'note' not in config['functions']['_init_function']['parameters'][3]:
    config['functions']['_init_function']['parameters'][3]['note'] = []
if not isinstance(config['functions']['_init_function']['parameters'][3]['note'], list):
    config['functions']['_init_function']['parameters'][3]['note'] = [config['functions']['_init_function']['parameters'][3]['note']]

config['functions']['_init_function']['parameters'][3]['note'].append(
'''
Supported Combinations:

+-------+---------------------+
| Model | Board Type          |
+=======+=====================+
| 4065  | PXI, PCI, PCIe, USB |
+-------+---------------------+
| 4070  | PXI, PCI            |
+-------+---------------------+
| 4071  | PXI                 |
+-------+---------------------+
| 4072  | PXI                 |
+-------+---------------------+
| 4080  | PXIe                |
+-------+---------------------+
| 4081  | PXIe                |
+-------+---------------------+
| 4082  | PXIe                |
+-------+---------------------+

If the Instrument Descriptor parameter and the Driver Setup property are not specified, an
NI PXI-4070 is simulated by default. If the Driver Setup string is not provided, and the
Instrument Descriptor parameter specifies a valid device, the device of the Instrument
Descriptor property is simulated. If the Driver Setup string is specified, the Instrument
Descriptor property is ignored.
''')
__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/attributes.py sha256=46822d392729cbe22d6adc8fb348d431aa2ae7f68b2055393c3d8d83c63b6758 bytes=38187 -->
## FILE: src/nidmm/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/attributes.py`
- sha256: `46822d392729cbe22d6adc8fb348d431aa2ae7f68b2055393c3d8d83c63b6758`
- bytes: 38187

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 24.8.0f126
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver functions perform range checking and  call IVI Get and Set functions, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver functions return calculated values.\nThe default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to  override this setting.\nSimulate can only be set within the InitWithOptions function.  The attribute value cannot be changed outside of the function.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates the Driver Setup string that the user specified when  initializing the driver.\nSome cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.\nIf the user does not specify a Driver Setup string, this attribute returns  an empty string.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates the number of channels that the specific instrument driver  supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag  attribute is set, the IVI engine maintains a separate cache value for each  channel.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the resource descriptor of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument models supported by the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050503: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the major version number of this instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Major Version',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050504: {
        'access': 'read only',
        'documentation': {
            'description': '\nThe minor version number of this instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Minor Version',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument firmware revision number.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the manufacturer of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument model.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the vendor of the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing a description of the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about this specific  instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  niDMM_ConfigureMeasurementDigits, NI-DMM sets this attribute to NIDMM_VAL_IVIDMM_MODE.  When you call niDMM_ConfigureWaveformAcquisition, NI-DMM sets this attribute to NIDMM_VAL_WAVEFORM_MODE.  If you are programming attributes directly, you must set this attribute before  setting other configuration attributes.\n'
        },
        'enum': 'OperationMode',
        'lv_property': 'Configuration:Advanced:Operation Mode',
        'name': 'OPERATION_MODE',
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': 'For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.'
        },
        'lv_property': 'Waveform Acquisition:Waveform Rate',
        'name': 'WAVEFORM_RATE',
        'type': 'ViReal64'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.\n'
        },
        'lv_property': 'Waveform Acquisition:Waveform Points',
        'name': 'WAVEFORM_POINTS',
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the ADC calibration mode.\n'
        },
        'enum': 'ADCCalibration',
        'lv_property': 'Configuration:Measurement Options:ADC Calibration',
        'name': 'ADC_CALIBRATION',
        'type': 'ViInt32'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, enables or disables offset compensated ohms.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Offset Compensated Ohms',
        'name': 'OFFSET_COMP_OHMS',
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current source provided during diode measurements.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Current Source',
        'name': 'CURRENT_SOURCE',
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the DC noise rejection mode.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'enum': 'DCNoiseRejection',
        'lv_property': 'Configuration:Measurement Options:DC Noise Rejection',
        'name': 'DC_NOISE_REJECTION',
        'type': 'ViInt32'
    },
    1150027: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.\n'
        },
        'enum': 'WaveformCoupling',
        'lv_property': 'Waveform Acquisition:Waveform Coupling',
        'name': 'WAVEFORM_COUPLING',
        'type': 'ViInt32'
    },
    1150028: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the settling time in seconds. To override the default settling time,  set this attribute. To return to the default, set this attribute to  NIDMM_VAL_SETTLE_TIME_AUTO (-1).\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'grpc_enum': 'SettleTime',
        'lv_property': 'Configuration:Advanced:Settle Time',
        'name': 'SETTLE_TIME',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input resistance of the instrument.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Input Resistance',
        'name': 'INPUT_RESISTANCE',
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Advanced:Number Of Averages',
        'name': 'NUMBER_OF_AVERAGES',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSize in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to NIDMM_VAL_BUFFER_SIZE_AUTO (-1), NI-DMM chooses the buffer size.\n'
        },
        'grpc_enum': 'BufferSize',
        'lv_property': 'Multi Point Acquisition:Advanced:Buffer Size',
        'name': 'BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read only',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this attribute is the same as that of  NIDMM_ATTR_FREQ_VOLTAGE_RANGE.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Frequency Voltage Auto Range Value',
        'name': 'FREQ_VOLTAGE_AUTO_RANGE',
        'type': 'ViReal64'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'enum': 'CableCompensationType',
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type',
        'name': 'CABLE_COMP_TYPE',
        'type': 'ViInt32'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance',
        'name': 'SHORT_CABLE_COMP_REACTANCE',
        'type': 'ViReal64'
    },
    1150047: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance',
        'name': 'SHORT_CABLE_COMP_RESISTANCE',
        'type': 'ViReal64'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance',
        'name': 'OPEN_CABLE_COMP_SUSCEPTANCE',
        'type': 'ViReal64'
    },
    1150049: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance',
        'name': 'OPEN_CABLE_COMP_CONDUCTANCE',
        'type': 'ViReal64'
    },
    1150052: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.\n'
        },
        'enum': 'LCCalculationModel',
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model',
        'name': 'LC_CALCULATION_MODEL',
        'type': 'ViInt32'
    },
    1150053: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, controls the available DC bias for capacitance measurements.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias',
        'name': 'DC_BIAS',
        'type': 'ViInt32'
    },
    1150054: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the serial number of the instrument. This attribute corresponds  to the serial number label that is attached to most products.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average',
        'name': 'LC_NUMBER_MEAS_TO_AVERAGE',
        'type': 'ViInt32'
    },
    1150061: {
        'access': 'read only',
        'documentation': {
            'description': 'The PCI product ID.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Product ID',
        'name': 'INSTRUMENT_PRODUCT_ID',
        'type': 'ViInt32'
    },
    1150120: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of RTD used to measure temperature. The default value is NIDMM_VAL_TEMP_RTD_PT3851.\nRefer to the NIDMM_ATTR_TEMP_RTD_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.\n'
        },
        'enum': 'RTDType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type',
        'name': 'TEMP_RTD_TYPE',
        'type': 'ViInt32'
    },
    1150121: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A',
        'name': 'TEMP_RTD_A',
        'type': 'ViReal64'
    },
    1150122: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B',
        'name': 'TEMP_RTD_B',
        'type': 'ViReal64'
    },
    1150123: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C',
        'name': 'TEMP_RTD_C',
        'type': 'ViReal64'
    },
    1150124: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of thermistor used to measure the temperature. The default value is  NIDMM_VAL_TEMP_THERMISTOR_44006.\nRefer to the NIDMM_ATTR_TEMP_THERMISTOR_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.\n'
        },
        'enum': 'ThermistorType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type',
        'name': 'TEMP_THERMISTOR_TYPE',
        'type': 'ViInt32'
    },
    1150125: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor A',
        'name': 'TEMP_THERMISTOR_A',
        'type': 'ViReal64'
    },
    1150126: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor B',
        'name': 'TEMP_THERMISTOR_B',
        'type': 'ViReal64'
    },
    1150127: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor C',
        'name': 'TEMP_THERMISTOR_C',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement function.\nRefer to the NIDMM_ATTR_FUNCTION topic in  the NI Digital Multimeters Help for device-specific information.\nIf you are setting this attribute directly, you must also set the NIDMM_ATTR_OPERATION_MODE attribute,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming attributes directly, you must set the NIDMM_ATTR_OPERATION_MODE attribute before  setting other configuration attributes. If the NIDMM_ATTR_OPERATION_MODE attribute is set to NIDMM_VAL_WAVEFORM_MODE,  the only valid function types are NIDMM_VAL_WAVEFORM_VOLTAGE and NIDMM_VAL_WAVEFORM_CURRENT. Set the  NIDMM_ATTR_OPERATION_MODE attribute to NIDMM_VAL_IVIDMM_MODE to set all other function values.\n'
        },
        'enum': 'Function',
        'lv_property': 'Configuration:Function',
        'name': 'FUNCTION',
        'type': 'ViInt32'
    },
    1250002: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the NIDMM_ATTR_FUNCTION attribute. For  example, if NIDMM_ATTR_FUNCTION is set to NIDMM_VAL_VOLTS, the units are  volts.\nThe NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.\nNIDMM_VAL_AUTO_RANGE_ON -1.0\nNI-DMM performs an Auto Range before acquiring the measurement.\nNIDMM_VAL_AUTO_RANGE_OFF -2.0\nNI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range  for all subsequent measurements until the measurement configuration is changed.\nNIDMM_VAL_AUTO_RANGE_ONCE -3.0\nNI-DMM performs an Auto Range before acquiring the next measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE  is stored and used for all subsequent measurements until the measurement configuration is changed.\n'
        },
        'grpc_enum': 'Range',
        'lv_property': 'Configuration:Range',
        'name': 'RANGE',
        'type': 'ViReal64'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement resolution in digits. Setting this  attribute to higher values increases the measurement accuracy. Setting this  attribute to lower values increases the measurement speed.\nNI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE attribute.\n'
        },
        'lv_property': 'Configuration:Digits Resolution',
        'name': 'RESOLUTION_DIGITS',
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the trigger source. When niDMM_Initiate is called, the DMM waits  for the trigger specified with this attribute. After it receives the trigger,  the DMM waits the length of time specified with the NIDMM_ATTR_TRIGGER_DELAY  attribute. The DMM then takes a measurement.\nThis attribute is not supported on the NI 4050.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'TriggerSource',
        'lv_property': 'Trigger:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'type': 'ViInt32'
    },
    1250005: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.\nThe NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.\nOn the NI 4060, if this attribute is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.\nWhen using the NI 4050, this attribute must be set to AUTO DELAY (-1).\nUse positive values to set the trigger delay in seconds.\nValid Range: NIDMM_VAL_AUTO_DELAY (-1.0), 0.0-12.0 seconds (NI 4060 only)\nDefault Value: NIDMM_VAL_AUTO_DELAY\n'
        },
        'grpc_enum': 'TriggerDelays',
        'lv_property': 'Trigger:Trigger Delay',
        'name': 'TRIGGER_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250006: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum frequency component of the input signal for AC  measurements. This attribute affects the DMM only when you set the  NIDMM_ATTR_FUNCTION attribute to AC measurements.\nThe valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Min Frequency',
        'name': 'AC_MIN_FREQ',
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum frequency component of the input signal for AC  measurements. This attribute is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This attribute affects the DMM only when you set the   NIDMM_ATTR_FUNCTION attribute to AC measurements.\nThe valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Max Frequency',
        'name': 'AC_MAX_FREQ',
        'type': 'ViReal64'
    },
    1250008: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement resolution in absolute units. Setting this  attribute to higher values increases the measurement accuracy. Setting this  attribute to lower values increases the measurement speed.\nNI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE attribute.\n'
        },
        'lv_property': 'Configuration:Absolute Resolution',
        'name': 'RESOLUTION_ABSOLUTE',
        'type': 'ViReal64'
    },
    1250101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum amplitude of the input signal for frequency  measurements.\n'
        },
        'grpc_enum': 'FrequencyVoltageRange',
        'lv_property': 'Configuration:Measurement Options:Frequency Voltage Range',
        'name': 'FREQ_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1250201: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of device used to measure the temperature. The default value is NIDMM_VAL_4_THERMOCOUPLE.\n'
        },
        'enum': 'TransducerType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Transducer Type',
        'name': 'TEMP_TRANSDUCER_TYPE',
        'type': 'ViInt32'
    },
    1250231: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of thermocouple used to measure the temperature. The default value is NIDMM_VAL_TEMP_TC_J.\n'
        },
        'enum': 'ThermocoupleType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type',
        'name': 'TEMP_TC_TYPE',
        'type': 'ViInt32'
    },
    1250232: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, NIDMM_VAL_TEMP_REF_JUNC_FIXED, is fixed.\n'
        },
        'enum': 'ThermocoupleReferenceJunctionType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type',
        'name': 'TEMP_TC_REF_JUNC_TYPE',
        'type': 'ViInt32'
    },
    1250233: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction',
        'name': 'TEMP_TC_FIXED_REF_JUNC',
        'type': 'ViReal64'
    },
    1250242: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance',
        'name': 'TEMP_RTD_RES',
        'type': 'ViReal64'
    },
    1250301: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.\n'
        },
        'grpc_enum': 'SampleCount',
        'lv_property': 'Multi Point Acquisition:Sample Count',
        'name': 'SAMPLE_COUNT',
        'type': 'ViInt32'
    },
    1250302: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the sample trigger source.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'SampleTrigger',
        'lv_property': 'Multi Point Acquisition:Sample Trigger',
        'name': 'SAMPLE_TRIGGER',
        'type': 'ViInt32'
    },
    1250303: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the amount of time in seconds the DMM waits between measurement cycles.  This attribute only applies when the NIDMM_ATTR_SAMPLE_TRIGGER attribute is set to INTERVAL.\nOn the NI 4060, the value for this attribute is used as the settling time.  When this attribute is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.\nThe NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.\nOnly positive values are valid when setting the sample interval.\nThe NI 4050 is not supported.\n'
        },
        'grpc_enum': 'SampleInterval',
        'lv_property': 'Multi Point Acquisition:Sample Interval',
        'name': 'SAMPLE_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250304: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of triggers the DMM receives before returning to the  Idle state.\nThis attribute can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.\nThe NI 4050 and NI 4060 support this attribute being set to 1.\nRefer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.\n'
        },
        'grpc_enum': 'TriggerCount',
        'lv_property': 'Multi Point Acquisition:Trigger Count',
        'name': 'TRIGGER_COUNT',
        'type': 'ViInt32'
    },
    1250305: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination of the measurement complete (MC) signal.\nThe NI 4050 is not supported.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'MeasurementCompleteDest',
        'lv_property': 'Trigger:Measurement Complete Dest',
        'name': 'MEAS_COMPLETE_DEST',
        'type': 'ViInt32'
    },
    1250321: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To  override the default aperture, set this attribute to the desired  aperture time after calling niDMM_ConfigureMeasurement. To return to the  default, set this attribute to NIDMM_VAL_APERTURE_TIME_AUTO (-1).\nOn the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.\nOn the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.\nOn the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.\n'
        },
        'grpc_enum': 'ApertureTime',
        'lv_property': 'Configuration:Advanced:Aperture Time',
        'name': 'APERTURE_TIME',
        'type': 'ViReal64'
    },
    1250322: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the units of aperture time for the current configuration.\nThe NI 4060 does not support an aperture time set in seconds.\n'
        },
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Configuration:Advanced:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'type': 'ViInt32'
    },
    1250331: {
        'access': 'read only',
        'documentation': {
            'description': '\nSpecifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this attribute is set during a read operation.\n'
        },
        'lv_property': 'Configuration:Auto Range Value',
        'name': 'AUTO_RANGE_VALUE',
        'type': 'ViReal64'
    },
    1250332: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the AutoZero mode.\nThe NI 4050 is not supported.\n'
        },
        'enum': 'AutoZero',
        'lv_property': 'Configuration:Measurement Options:Auto Zero',
        'name': 'AUTO_ZERO',
        'type': 'ViInt32'
    },
    1250333: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the NIDMM_ATTR_APERTURE_TIME  attribute in powerline cycles (PLCs).\nAfter configuring powerline frequency, set the NIDMM_ATTR_APERTURE_TIME_UNITS attribute to PLCs.  When setting the NIDMM_ATTR_APERTURE_TIME attribute, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Powerline Frequency',
        'name': 'POWERLINE_FREQ',
        'type': 'ViReal64'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nidmm/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/config.py sha256=a7e8269350453bd54525edce9f202166a82ccd9a97a5884b05bd218f6d56e71a bytes=1188 -->
## FILE: src/nidmm/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/config.py`
- sha256: `a7e8269350453bd54525edce9f202166a82ccd9a97a5884b05bd218f6d56e71a`
- bytes: 1188

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 24.8.0f126
config = {
    'api_version': '24.8.0f126',
    'c_function_prefix': 'niDMM_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-DMM',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiDmm',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidmm',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidmm_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidmm_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nidmm',
    'repeated_capabilities': [
    ],
    'session_class_description': 'An NI-DMM session to an NI digital multimeter',
    'session_handle_parameter_name': 'vi'
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/config_addon.py sha256=7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2 bytes=259 -->
## FILE: src/nidmm/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/config_addon.py`
- sha256: `7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2017',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/enums.py sha256=588a818baf89fedc006a1b4114b97f39687ea4319d11eaf187a2f9abf129bdce bytes=27928 -->
## FILE: src/nidmm/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/enums.py`
- sha256: `588a818baf89fedc006a1b4114b97f39687ea4319d11eaf187a2f9abf129bdce`
- bytes: 27928

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 24.8.0f126
enums = {
    'ADCCalibration': {
        'values': [
            {
                'documentation': {
                    'description': 'The DMM enables or disables ADC calibration for you.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'The DMM does not compensate for changes to the gain.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The DMM measures an internal reference to calculate the correct gain for the  measurement.'
                },
                'name': 'NIDMM_VAL_ADC_CALIBRATION_ON',
                'value': 1
            }
        ]
    },
    'AcquisitionStatus': {
        'values': [
            {
                'documentation': {
                    'description': 'Running'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_RUNNING',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Finished with **Backlog**'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_FINISHED_WITH_BACKLOG',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Finished with no **Backlog**'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_FINISHED_WITH_NO_BACKLOG',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Paused'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_PAUSED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'No acquisition in progress'
                },
                'name': 'NIDMM_VAL_ACQUISITION_STATUS_NO_ACQUISITION_IN_PROGRESS',
                'value': 4
            }
        ]
    },
    'ApertureTimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Seconds'
                },
                'name': 'NIDMM_VAL_SECONDS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Powerline Cycles'
                },
                'name': 'NIDMM_VAL_POWER_LINE_CYCLES',
                'value': 1
            }
        ]
    },
    'AutoZero': {
        'values': [
            {
                'documentation': {
                    'description': 'The drivers chooses the AutoZero setting based on the configured function  and resolution.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Disables AutoZero.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_ON',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.'
                },
                'name': 'NIDMM_VAL_AUTO_ZERO_ONCE',
                'value': 2
            }
        ]
    },
    'CableCompensationType': {
        'values': [
            {
                'documentation': {
                    'description': 'No Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Open Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Short Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Open and Short Cable Compensation'
                },
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            }
        ]
    },
    'DCNoiseRejection': {
        'values': [
            {
                'documentation': {
                    'description': 'The driver chooses the DC noise rejection setting based on the configured  function and resolution.'
                },
                'name': 'NIDMM_VAL_DCNR_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs all samples equally.'
                },
                'name': 'NIDMM_VAL_DCNR_NORMAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing function.'
                },
                'name': 'NIDMM_VAL_DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing function.'
                },
                'name': 'NIDMM_VAL_DCNR_HIGH_ORDER',
                'value': 2
            }
        ]
    },
    'Function': {
        'values': [
            {
                'documentation': {
                    'description': 'DC Voltage'
                },
                'name': 'NIDMM_VAL_DC_VOLTS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AC Voltage'
                },
                'name': 'NIDMM_VAL_AC_VOLTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'DC Current'
                },
                'name': 'NIDMM_VAL_DC_CURRENT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'AC Current'
                },
                'name': 'NIDMM_VAL_AC_CURRENT',
                'value': 4
            },
            {
                'documentation': {
                    'description': '2-Wire Resistance'
                },
                'name': 'NIDMM_VAL_2_WIRE_RES',
                'python_name': 'TWO_WIRE_RES',
                'value': 5
            },
            {
                'documentation': {
                    'description': '4-Wire Resistance'
                },
                'name': 'NIDMM_VAL_4_WIRE_RES',
                'python_name': 'FOUR_WIRE_RES',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Frequency'
                },
                'name': 'NIDMM_VAL_FREQ',
                'value': 104
            },
            {
                'documentation': {
                    'description': 'Period'
                },
                'name': 'NIDMM_VAL_PERIOD',
                'value': 105
            },
            {
                'documentation': {
                    'description': 'NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.'
                },
                'name': 'NIDMM_VAL_TEMPERATURE',
                'value': 108
            },
            {
                'documentation': {
                    'description': 'AC Voltage with DC Coupling'
                },
                'name': 'NIDMM_VAL_AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Diode'
                },
                'name': 'NIDMM_VAL_DIODE',
                'value': 1002
            },
            {
                'documentation': {
                    'description': 'Waveform voltage'
                },
                'name': 'NIDMM_VAL_WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Waveform current'
                },
                'name': 'NIDMM_VAL_WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'documentation': {
                    'description': 'Capacitance'
                },
                'name': 'NIDMM_VAL_CAPACITANCE',
                'value': 1005
            },
            {
                'documentation': {
                    'description': 'Inductance'
                },
                'name': 'NIDMM_VAL_INDUCTANCE',
                'value': 1006
            }
        ]
    },
    'LCCalculationModel': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-DMM chooses the algorithm based on function and range'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-DMM uses the series impedance model to calculate capacitance and inductance'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-DMM uses the parallel admittance model to calculate capacitance and inductance'
                },
                'name': 'NIDMM_VAL_CALC_MODEL_PARALLEL',
                'value': 1
            }
        ]
    },
    'MeasurementCompleteDest': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_NONE',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG0',
                'value': 1003
            }
        ]
    },
    'MeasurementDestinationSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'OperationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'IviDmm Mode'
                },
                'name': 'NIDMM_VAL_IVIDMM_MODE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Waveform acquisition mode'
                },
                'name': 'NIDMM_VAL_WAVEFORM_MODE',
                'value': 1
            }
        ]
    },
    'RTDType': {
        'values': [
            {
                'documentation': {
                    'description': '\nPerforms Callendar-Van Dusen RTD scaling with the user-specified A, B,\nand C coefficients.\n'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3750 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3851 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3911 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3916 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3920 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Performs scaling for a Pt 3928 RTD.'
                },
                'name': 'NIDMM_VAL_TEMP_RTD_PT3928',
                'value': 6
            }
        ]
    },
    'SampleTrigSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'SampleTrigger': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 0'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Software Trigger'
                },
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Interval Trigger'
                },
                'name': 'NIDMM_VAL_INTERVAL',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'AUX I/0 Connector Trigger Line 1'
                },
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'ThermistorType': {
        'values': [
            {
                'documentation': {
                    'description': 'Custom'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'documentation': {
                    'description': '44004'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44004',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44004',
                'value': 1
            },
            {
                'documentation': {
                    'description': '44006'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44006',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44006',
                'value': 2
            },
            {
                'documentation': {
                    'description': '44007'
                },
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44007',
                'python_name': 'TEMP_THERMISTOR_THERMISTOR_44007',
                'value': 3
            }
        ]
    },
    'ThermocoupleReferenceJunctionType': {
        'values': [
            {
                'documentation': {
                    'description': '\nThermocouple reference juction is fixed at the user-specified\ntemperature.\n'
                },
                'name': 'NIDMM_VAL_TEMP_REF_JUNC_FIXED',
                'value': 2
            }
        ]
    },
    'ThermocoupleType': {
        'values': [
            {
                'documentation': {
                    'description': 'Thermocouple type B'
                },
                'name': 'NIDMM_VAL_TEMP_TC_B',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Thermocouple type E'
                },
                'name': 'NIDMM_VAL_TEMP_TC_E',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Thermocouple type J'
                },
                'name': 'NIDMM_VAL_TEMP_TC_J',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Thermocouple type K'
                },
                'name': 'NIDMM_VAL_TEMP_TC_K',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Thermocouple type N'
                },
                'name': 'NIDMM_VAL_TEMP_TC_N',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Thermocouple type R'
                },
                'name': 'NIDMM_VAL_TEMP_TC_R',
                'value': 9
            },
            {
                'documentation': {
                    'description': 'Thermocouple type S'
                },
                'name': 'NIDMM_VAL_TEMP_TC_S',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Thermocouple type T'
                },
                'name': 'NIDMM_VAL_TEMP_TC_T',
                'value': 11
            }
        ]
    },
    'TransducerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Thermocouple'
                },
                'name': 'NIDMM_VAL_THERMOCOUPLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Thermistor'
                },
                'name': 'NIDMM_VAL_THERMISTOR',
                'value': 2
            },
            {
                'documentation': {
                    'description': '2-wire RTD'
                },
                'name': 'NIDMM_VAL_2_WIRE_RTD',
                'python_name': 'TWO_WIRE_RTD',
                'value': 3
            },
            {
                'documentation': {
                    'description': '4-wire RTD'
                },
                'name': 'NIDMM_VAL_4_WIRE_RTD',
                'python_name': 'FOUR_WIRE_RTD',
                'value': 4
            }
        ]
    },
    'TriggerSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edgs'
                },
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'TriggerSource': {
        'values': [
            {
                'documentation': {
                    'description': 'No Trigger'
                },
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 0'
                },
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Software Trigger'
                },
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 0'
                },
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 1'
                },
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 2'
                },
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 3'
                },
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 4'
                },
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 5'
                },
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 6'
                },
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Trigger Line 7'
                },
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'AUX I/O Connector Trigger Line 1'
                },
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Internal Trigger Line of a PXI/SCXI Combination Chassis'
                },
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'WaveformCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC Coupled'
                },
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC Coupled'
                },
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nidmm/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/functions.py sha256=721208653042eb62add0eecba1b6c95ec282b9de596a33704d585bb3c654ac1c bytes=128506 -->
## FILE: src/nidmm/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/functions.py`
- sha256: `721208653042eb62add0eecba1b6c95ec282b9de596a33704d585bb3c654ac1c`
- bytes: 128506

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 24.8.0f126
functions = {
    'Abort': {
        'documentation': {
            'description': '\nAborts a previously initiated measurement and returns the DMM to the\nIdle state.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementAbsolute': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_ABSOLUTE.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a **range** that exceeds the\nvalue that you are measuring. For example, you must type in 10 V if you\nare measuring 9 V. **range** values are coerced up to the closest input\n**range**. Refer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute resolution for the measurement. NI-DMM sets\nNIDMM_ATTR_RESOLUTION_ABSOLUTE to this value. The PXIe-4080/4081/4082\nuses the resolution you specify. The NI 4065 and NI 4070/4071/4072\nignore this parameter when the **Range** parameter is set to\nNIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE\n(-3.0). The default is 0.001 V.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionAbsolute',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementDigits': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_DIGITS.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a range that exceeds the value\nthat you are measuring. For example, you must type in 10 V if you are\nmeasuring 9 V. range values are coerced up to the closest input range.\nRefer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the resolution of the measurement in digits. The driver sets\nthe `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a\nlist of valid ranges. The driver sets NIDMM_ATTR_RESOLUTION_DIGITS\nattribute to this value. The PXIe-4080/4081/4082 uses the resolution you\nspecify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when\nthe **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or\nNIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionDigits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiPoint': {
        'documentation': {
            'description': '\nConfigures the attributes for multipoint measurements. These attributes\ninclude NIDMM_ATTR_TRIGGER_COUNT, NIDMM_ATTR_SAMPLE_COUNT,\nNIDMM_ATTR_SAMPLE_TRIGGER, and NIDMM_ATTR_SAMPLE_INTERVAL.\n\nFor continuous acquisitions, set NIDMM_ATTR_TRIGGER_COUNT or\nNIDMM_ATTR_SAMPLE_COUNT to zero. For more information, refer to\n`Multiple Point\nAcquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of triggers you want the DMM to receive before returning\nto the Idle state. The driver sets NIDMM_ATTR_TRIGGER_COUNT to this\nvalue. The default value is 1.\n'
                },
                'grpc_enum': 'TriggerCount',
                'name': 'triggerCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of measurements the DMM makes in each measurement\nsequence initiated by a trigger. The driver sets\nNIDMM_ATTR_SAMPLE_COUNT to this value. The default value is 1.\n'
                },
                'grpc_enum': 'SampleCount',
                'name': 'sampleCount',
                'type': 'ViInt32'
            },
            {
                'default_value': 'SampleTrigger.IMMEDIATE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **sample_trigger** source you want to use. The driver\nsets NIDMM_ATTR_SAMPLE_TRIGGER to this value. The default is\nImmediate.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'SampleTrigger',
                'name': 'sampleTrigger',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the amount of time in seconds the DMM waits between measurement\ncycles. The driver sets NIDMM_ATTR_SAMPLE_INTERVAL to this value.\nSpecify a sample interval to add settling time between measurement\ncycles or to decrease the measurement rate. **sample_interval** only\napplies when the **Sample_Trigger** is set to INTERVAL.\n\nOn the NI 4060, the **sample_interval** value is used as the settling\ntime. When sample interval is set to 0, the DMM does not settle between\nmeasurement cycles. The NI 4065 and NI 4070/4071/4072 use the value\nspecified in **sample_interval** as additional delay. The default value\n(-1) ensures that the DMM settles for a recommended time. This is the\nsame as using an Immediate trigger.\n',
                    'note': 'This attribute is not used on the NI 4080/4081/4082 and the NI 4050.'
                },
                'grpc_enum': 'SampleInterval',
                'name': 'sampleInterval',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom RTD.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is 3.9083e-3 (Pt3851)\n'
                },
                'name': 'rtdA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -5.775e-7 (Pt3851).\n'
                },
                'name': 'rtdB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -4.183e-12 (Pt3851).\n'
                },
                'name': 'rtdC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDType': {
        'documentation': {
            'description': 'Configures the RTD Type and RTD Resistance parameters for an RTD.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of RTD used to measure the temperature resistance.\nNI-DMM uses this value to set the RTD Type property. The default is\nNIDMM_VAL_TEMP_RTD_PT3851.\n',
                    'table_body': [
                        [
                            'Callendar-Van Dusen Coefficient'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3851',
                            'IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751',
                            'Platinum',
                            '.003851',
                            '100 Ω 1000 Ω',
                            'A = 3.9083 × 10\\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`',
                            'Most common RTDs'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3750',
                            'Low-cost vendor compliant RTD\\*',
                            'Platinum',
                            '.003750',
                            '1000 Ω',
                            'A = 3.81 × 10\\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3916',
                            'JISC 1604',
                            'Platinum',
                            '.003916',
                            '100 Ω',
                            'A = 3.9739 × 10\\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\\ :sup:`–12`',
                            'Used in primarily in Japan'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3920',
                            'US Industrial Standard D-100 American',
                            'Platinum',
                            '.003920',
                            '100 Ω',
                            'A = 3.9787 × 10\\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3911',
                            'US Industrial Standard American',
                            'Platinum',
                            '.003911',
                            '100 Ω',
                            'A = 3.9692 × 10\\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3928',
                            'ITS-90',
                            'Platinum',
                            '.003928',
                            '100 Ω',
                            'A = 3.9888 × 10\\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\\ :sup:`–12`',
                            'The definition of temperature'
                        ],
                        [
                            '\\*No standard. Check the TCR.'
                        ]
                    ],
                    'table_header': [
                        'Enum',
                        'Standards',
                        'Material',
                        'TCR (α)',
                        'Typical R\\ :sub:`0` (Ω)',
                        'Notes'
                    ]
                },
                'enum': 'RTDType',
                'name': 'rtdType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to\nset the RTD Resistance property. The default is 100 (Ω).\n'
                },
                'name': 'rtdResistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom thermistor.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart A coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.0295e-3 (44006).\n'
                },
                'name': 'thermistorA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart B coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 2.391e-4 (44006).\n'
                },
                'name': 'thermistorB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart C coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.568e-7 (44006).\n'
                },
                'name': 'thermistorC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermocouple': {
        'documentation': {
            'description': '\nConfigures the thermocouple type and reference junction type for a\nchosen thermocouple.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of thermocouple used to measure the temperature.\nNI-DMM uses this value to set the Thermocouple Type property. The\ndefault is NIDMM_VAL_TEMP_TC_J.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_TEMP_TC_B',
                            'Thermocouple type B'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_E',
                            'Thermocouple type E'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_J',
                            'Thermocouple type J'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_K',
                            'Thermocouple type K'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_N',
                            'Thermocouple type N'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_R',
                            'Thermocouple type R'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_S',
                            'Thermocouple type S'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_T',
                            'Thermocouple type T'
                        ]
                    ]
                },
                'enum': 'ThermocoupleType',
                'name': 'thermocoupleType',
                'type': 'ViInt32'
            },
            {
                'default_value': 'ThermocoupleReferenceJunctionType.FIXED',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of reference junction to be used in the reference\njunction compensation of a thermocouple measurement. NI-DMM uses this\nvalue to set the Reference Junction Type property. The only supported\nvalue is NIDMM_VAL_TEMP_REF_JUNC_FIXED.\n'
                },
                'enum': 'ThermocoupleReferenceJunctionType',
                'name': 'referenceJunctionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'documentation': {
            'description': '\nConfigures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more\ninformation.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **trigger_source** that initiates the acquisition. The\ndriver sets NIDMM_ATTR_TRIGGER_SOURCE to this value. Software\nconfigures the DMM to wait until niDMM_SendSoftwareTrigger is called\nbefore triggering the DMM.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'TriggerSource',
                'name': 'triggerSource',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the time that the DMM waits after it has received a trigger\nbefore taking a measurement. The driver sets the\nNIDMM_ATTR_TRIGGER_DELAY attribute to this value. By default,\n**trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM\nwaits an appropriate settling time before taking the measurement. On the\nNI 4060, if you set **trigger_delay** to 0, the DMM does not settle\nbefore taking the measurement. The NI 4065 and NI 4070/4071/4072 use the\nvalue specified in **trigger_delay** as additional settling time.\n',
                    'note': '\nWhen using the NI 4050, **Trigger_Delay** must be set to\nNIDMM_VAL_AUTO_DELAY (-1).\n'
                },
                'grpc_enum': 'TriggerDelays',
                'name': 'triggerDelay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformAcquisition': {
        'documentation': {
            'description': '\nConfigures the DMM for waveform acquisitions. This feature is supported\non the NI 4080/4081/4082 and the NI 4070/4071/4072.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used in a waveform acquisition.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_WAVEFORM_VOLTAGE (default)',
                            '1003',
                            'Voltage Waveform'
                        ],
                        [
                            'NIDMM_VAL_WAVEFORM_CURRENT',
                            '1004',
                            'Current Waveform'
                        ]
                    ]
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the expected maximum amplitude of the input signal and sets\nthe **range** for the **Measurement_Function**. NI-DMM sets\nNIDMM_ATTR_RANGE to this value. **range** values are coerced up to the\nclosest input **range**. The default is 10.0.\n\nFor valid ranges refer to the topics in\n`Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.\n\nAuto-ranging is not supported during waveform acquisitions.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **rate** of the acquisition in samples per second. NI-DMM\nsets NIDMM_ATTR_WAVEFORM_RATE to this value.\n\nThe valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced\nto the closest integer divisor of 1,800,000. The default value is\n1,800,000.\n'
                },
                'name': 'rate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of points to acquire before the waveform\nacquisition completes. NI-DMM sets NIDMM_ATTR_WAVEFORM_POINTS to this\nvalue.\n\nTo calculate the maximum and minimum number of waveform points that you\ncan acquire in one acquisition, refer to the `Waveform Acquisition\nMeasurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.\n\nThe default value is 500.\n'
                },
                'name': 'waveformPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. If a measurement is in\nprogress when this function is called, the measurement is aborted.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Fetch': {
        'documentation': {
            'description': '\nReturns the value from a previously initiated measurement. You must call\nniDMM_Initiate before calling this function. Value is in base units.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPoint': {
        'documentation': {
            'description': '\nReturns an array of values from a previously initiated multipoint\nmeasurement. The number of measurements the DMM makes is determined by\nthe values you specify for the **Trigger_Count** and **Sample_Count**\nparameters of niDMM_ConfigureMultiPoint. You must first call\nniDMM_Initiate to initiate a measurement before calling this function. Values are in base units.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of\nvalues from a previously initiated waveform acquisition. You must call\nniDMM_Initiate before calling this function.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**Waveform Array** is an array of measurement values stored in waveform\ndata type.\n'
                },
                'name': 'waveformArray',
                'numpy': True,
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n   You must provide a ViChar array to serve as a buffer for the value.\n   You pass the number of bytes in the buffer as the Array Size\n   parameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\n**Attribute_Value** parameter.\n\nIf the current value of the attribute, including the terminating NULL\nbyte, contains more bytes that you indicate in this parameter, the\nfunction copies **buffer_size**—1 bytes into the buffer, places an\nASCII NUL byte at the end of the buffer, and returns the buffer size you\nmust pass to get the entire value. For example, if the value is "123456"\nand the **buffer_size** is 4, the function places "123" into the buffer\nand returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value. If you pass 0,\nyou can pass VI_NULL for the **Attribute_Value** buffer parameter.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the **Buffer_Size** parameter.\n\nIf you specify 0 for the **Buffer_Size** parameter, you can pass\nVI_NULL for this parameter.\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_cal_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDevTemp': {
        'documentation': {
            'description': 'Returns the current **Temperature** of the device.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Reserved.'
                },
                'name': 'options',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current **temperature** of the device.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with the\n**Instrument_Handle**. This function retrieves and then clears the\nerror information for the session. If you leave the\n**Instrument_Handle** unwired, this function retrieves and then clears\nthe error information for the process.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **error_code** for the session or execution thread. If you\npass 0 for the **Buffer_Size**, you can pass VI_NULL for this\nparameter.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Description** parameter. If the error description, including the\nterminating NULL byte, contains more bytes than you indicate in this\nparameter, the function copies **buffer_size** –1 bytes into the\nbuffer, places an ASCII NULL byte at the end of the buffer, and returns\nthe **buffer_size** you must pass to get the entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value. If you pass 0, you can pass\nVI_NULL for the **Description** buffer parameter. The default value is\nNone.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error **description** for the IVI session or execution\nthread. If there is no **description**, the function returns an empty\nstring. The buffer must contain at least as many elements as the value\nyou specify with the **Buffer_Size** parameter. If you pass 0 for the\n**Buffer_Size**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the recommended interval between external recalibration in\n**Months**.\n',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the recommended number of **months** between external\ncalibrations.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastCalTemp': {
        'documentation': {
            'description': 'Returns the **Temperature** during the last calibration procedure.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'documentation': {
            'description': '\nReturns a Boolean value that expresses whether or not the DMM that you\nare using can perform self-calibration.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether Self Cal is supported for the device specified by the\ngiven session.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            '1',
                            'The DMM that you are using can perform self-calibration.'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'The DMM that you are using cannot perform self-calibration.'
                        ]
                    ]
                },
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': "\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__\n",
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function completes the following tasks:\n\n-  Creates a new IVI instrument driver session and, optionally, sets the\n   initial state of the following session attributes:\n   NIDMM_ATTR_RANGE_CHECK, NIDMM_ATTR_QUERY_INSTR_STATUS,\n   NIDMM_ATTR_CACHE, NIDMM_ATTR_SIMULATE,\n   NIDMM_ATTR_RECORD_COERCIONS.\n-  Opens a session to the device you specify for the **Resource_Name**\n   parameter. If the **ID_Query** parameter is set to VI_TRUE, this\n   function queries the instrument ID and checks that it is valid for\n   this instrument driver.\n-  If the **Reset_Device** parameter is set to VI_TRUE, this function\n   resets the instrument to a known state. Sends initialization commands\n   to set the instrument to the state necessary for the operation of the\n   instrument driver.\n-  Returns a ViSession handle that you use to identify the instrument in\n   all subsequent instrument driver function calls.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nAll IVI names for the **Resource_Name**, such as logical names or\nvirtual names, are case-sensitive. If you use logical names, driver\nsession names, or virtual names in your program, you must make sure that\nthe name you use matches the name in the IVI Configuration Store file\nexactly, without any variations in the case of the characters in the\nname.\n',
                    'description': '\n| Contains the **resource_name** of the device to initialize. The\n  **resource_name** is assigned in Measurement & Automation Explorer\n  (MAX). Refer to `Related\n  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__\n  for the *NI Digital Multimeters Getting Started Guide* for more\n  information about configuring and testing the DMM in MAX.\n| Valid Syntax:\n\n-  NI-DAQmx name\n-  DAQ::NI-DAQmx name[::INSTR]\n-  DAQ::Traditional NI-DAQ device number[::INSTR]\n-  IVI logical name\n'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nVerifies that the device you initialize is one that the driver supports.\nNI-DMM automatically performs this query, so setting this parameter is\nnot necessary.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the instrument during the initialization\nprocedure.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\n| Sets the initial value of certain attributes for the session. The\n  following table specifies the attribute name, attribute constant, and\n  default value for each attribute that you can use in this parameter:\n\nThe format of this string is, "AttributeName=Value." To set multiple\nattributes, separate their assignments with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for the attributes. You can override the default\nvalues by assigning a value explicitly in an **option_string**\nparameter. You do not have to specify all of the attributes and may\nleave any of them out (those left out use the default value).\n\nRefer to `Simulating NI Digital\nMultimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more\ninformation.\n',
                    'table_body': [
                        [
                            'Check',
                            'NIDMM_ATTR_RANGE_CHECK',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIDMM_ATTR_QUERY_INSTR_STATUS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'Cache',
                            'NIDMM_ATTR_CACHE',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'Simulate',
                            'NIDMM_ATTR_SIMULATE',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'RecordCoercions',
                            'NIDMM_ATTR_RECORD_COERCIONS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'DriverSetup',
                            'NIDMM_ATTR_DRIVER_SETUP',
                            '"" (empty string)',
                            '""'
                        ]
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition. After you call this function, the DMM leaves\nthe Idle state and enters the Wait-for-Trigger state. If trigger is set\nto Immediate mode, the DMM begins acquiring measurement data. Use\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform to\nretrieve the measurement data.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nThis function obtains a multithread lock on the instrument session.\nBefore it does so, it waits until all other execution threads have\nreleased their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the\nfollowing ways:\n\n-  The user application called this function.\n-  A call to the instrument driver locked the session.\n-  A call to the IVI Library locked the session.\n\nAfter your call to this function returns successfully, no other threads\ncan access the instrument session until you call niDMM_UnlockSession.\n\nUse this function and niDMM_UnlockSession around a sequence of calls to\ninstrument driver functions if you require that the instrument retain\nits settings through the end of the sequence. You can safely make nested\ncalls to this function within the same thread.\n\nTo completely unlock the session, you must balance each call to this\nfunction with a call to niDMM_UnlockSession. If, however, you use the\n**Caller_Has_Lock** parameter in all calls to this function and\nniDMM_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to this function. This feature allows you to call\nniDMM_UnlockSession just once at the end of the function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and, therefore, need to unlock\nthe session. To use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to this function or niDMM_UnlockSession in the same function.\n\nThe parameter is an input/output parameter. This function and\nniDMM_UnlockSession each inspect the current value and take the\nfollowing actions:\n\nIf the value is VI_TRUE (1), this function does not lock the session\nagain. If the value is VI_FALSE, this function obtains the lock and\nsets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, niDMM_UnlockSession does not attempt to\nunlock the session. If the value is VI_TRUE, niDMM_UnlockSession\nreleases the lock and sets the value of the parameter to VI_FALSE.\nThus, you can, call niDMM_UnlockSession at the end of your function\nwithout worrying about whether you actually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\n| ViStatus error = VI_SUCCESS;\n| ViBoolean haveLock = VI_FALSE;\n| if (flags & BIT_1)\n\n| {\n| viCheckErr( NIDMM_LockSession(vi, &haveLock;));\n| viCheckErr( TakeAction1(vi));\n| if (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PerformOpenCableComp': {
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, performs the open cable compensation\nmeasurements for the current capacitance/inductance range, and returns\nopen cable compensation **Conductance** and **Susceptance** values. You\ncan use the return values of this function as inputs to\nniDMM_ConfigureOpenCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**conductance** is the measured value of open cable compensation\n**conductance**.\n'
                },
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**susceptance** is the measured value of open cable compensation\n**susceptance**.\n'
                },
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformShortCableComp': {
        'documentation': {
            'description': '\nPerforms the short cable compensation measurements for the current\ncapacitance/inductance range, and returns short cable compensation\n**Resistance** and **Reactance** values. You can use the return values\nof this function as inputs to niDMM_ConfigureShortCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**resistance** is the measured value of short cable compensation\n**resistance**.\n'
                },
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**reactance** is the measured value of short cable compensation\n**reactance**.\n'
                },
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value in base units.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMultiPoint': {
        'documentation': {
            'description': '\nAcquires multiple measurements and returns an array of measured values.\nThe number of measurements the DMM makes is determined by the values you\nspecify for the **Trigger_Count** and **Sample_Count** parameters in\nniDMM_ConfigureMultiPoint.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatus': {
        'documentation': {
            'description': '\nReturns measurement backlog and acquisition status. Use this function to\ndetermine how many measurements are available before calling\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform.\n',
            'note': 'The NI 4050 is not supported.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe number of measurements available to be read. If the backlog\ncontinues to increase, data is eventually overwritten, resulting in an\nerror.\n',
                    'note': '\nOn the NI 4060, the **Backlog** does not increase when autoranging. On\nthe NI 4065, the **Backlog** does not increase when Range is set to AUTO\nRANGE ON (-1), or before the first point is fetched when Range is set to\nAUTO RANGE ONCE (-3). These behaviors are due to the autorange model of\nthe devices.\n'
                },
                'name': 'acquisitionBacklog',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates status of the acquisition. The following table shows the\nacquisition states:\n',
                    'table_body': [
                        [
                            '0',
                            'Running'
                        ],
                        [
                            '1',
                            'Finished with backlog'
                        ],
                        [
                            '2',
                            'Finished with no backlog'
                        ],
                        [
                            '3',
                            'Paused'
                        ],
                        [
                            '4',
                            'No acquisition in progress'
                        ]
                    ]
                },
                'enum': 'AcquisitionStatus',
                'name': 'acquisitionStatus',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform\nand returns data as an array of values or as a waveform data type. The\nnumber of elements in the **Waveform_Array** is determined by the\nvalues you specify for the **Waveform_Points** parameter in\nniDMM_ConfigureWaveformAcquisition.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'grpc_enum': 'TimeLimit',
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Waveform_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'waveformArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the DMM. The initialization commands set the DMM settings to the\nstate necessary for the operation of NI-DMM. All user-defined default\nvalues associated with a logical name are applied after setting the DMM.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the\nself-calibration routine to maintain measurement accuracy.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nSends a command to trigger the DMM. Call this function if you have\nconfigured either the NIDMM_ATTR_TRIGGER_SOURCE or\nNIDMM_ATTR_SAMPLE_TRIGGER attributes. If the\nNIDMM_ATTR_TRIGGER_SOURCE and/or NIDMM_ATTR_SAMPLE_TRIGGER\nattributes are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\\ *n*, you\ncan use this function to override the trigger source that you configured\nand trigger the device. The NI 4050 and NI 4060 are not supported.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViBoolean attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViInt32 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_enum': 'NiDmmInt32AttributeValues',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViReal64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_enum': 'NiDmmReal64AttributeValues',
                'grpc_mapped_enum': 'NiDmmReal64AttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. NI DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nThis function releases a lock that you acquired on an instrument session\nusing niDMM_LockSession. Refer to niDMM_LockSession for additional\ninformation on session locks.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nobtain a lock and, therefore, need to unlock the session.\n\nTo use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to niDMM_LockSession or this function in the same function.\n\nThe parameter is an input/output parameter. niDMM_LockSession and this\nfunction each inspect the current value and take the following actions:\n\nIf the value is VI_TRUE (1), niDMM_LockSession does not lock the\nsession again. If the value is VI_FALSE, niDMM_LockSession obtains the\nlock and sets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, this function does not attempt to unlock the\nsession. If the value is VI_TRUE, this function releases the lock and\nsets the value of the parameter to VI_FALSE. Thus, you can, call this\nfunction at the end of your function without worrying about whether you\nactually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\nViStatus error = VI_SUCCESS;\n\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n\n{\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction1(vi));\n\nif (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nTakes the **Error_Code** returned by the instrument driver functions,\ninterprets it, and returns it as a user-readable string.\n',
            'note': '\nWhen using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.\n'
        },
        'grpc_name': 'GetErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe **error_code** returned from the instrument. The default is 0,\nindicating VI_SUCCESS.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted into a string.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM. Zero\nindicates success. \n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'note': [
                'Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.',
                'This function calls niDMM_reset, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.'
            ]
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the instrument. The initialization commands set instrument settings\nto the state necessary for the operation of the instrument driver.\n'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the value returned from the instrument self-test. Zero\nindicates success.\n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n',
                    'note': '\nSelf-test does not check the fuse on the NI 4065, NI 4071, and\nNI 4081. Hence, even if the fuse is blown on the device, self-test does\nnot return error code 1013.\n'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter contains the string returned from the instrument\nself-test. The array must contain at least 256 elements.\n\nFor the NI 4050 and NI 4060, the error codes returned for self-test\nfailures include the following:\n\n-  NIDMM_ERROR_AC_TEST_FAILURE\n-  NIDMM_ERROR_DC_TEST_FAILURE\n-  NIDMM_ERROR_RESISTANCE_TEST_FAILURE\n\nThese error codes indicate that the DMM should be repaired.\n\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code\nreturned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.\nThis error code indicates that the DMM should be repaired.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/nidmm/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/metadata/nidmm.proto sha256=a2f5fc47d040ae13fb9349f2e1fa12d1b1b0a86cdf5132ded4f4a9a40167bc19 bytes=45814 -->
## FILE: src/nidmm/metadata/nidmm.proto

- repository: `ni/nimi-python`
- source_path: `src/nidmm/metadata/nidmm.proto`
- sha256: `a2f5fc47d040ae13fb9349f2e1fa12d1b1b0a86cdf5132ded4f4a9a40167bc19`
- bytes: 45814

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-DMM API metadata version 24.8.0f126
//---------------------------------------------------------------------
// Proto file for the NI-DMM Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.dmm";
option java_outer_classname = "NiDmm";
option csharp_namespace = "NationalInstruments.Grpc.Dmm";

package nidmm_grpc;

import "session.proto";

service NiDmm {
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetErrorMessage(GetErrorMessageRequest) returns (GetErrorMessageResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc GetMeasurementPeriod(GetMeasurementPeriodRequest) returns (GetMeasurementPeriodResponse);
  rpc ConfigureTrigger(ConfigureTriggerRequest) returns (ConfigureTriggerResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc Fetch(FetchRequest) returns (FetchResponse);
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc IsOverRange(IsOverRangeRequest) returns (IsOverRangeResponse);
  rpc IsUnderRange(IsUnderRangeRequest) returns (IsUnderRangeResponse);
  rpc ConfigureACBandwidth(ConfigureACBandwidthRequest) returns (ConfigureACBandwidthResponse);
  rpc ConfigureFrequencyVoltageRange(ConfigureFrequencyVoltageRangeRequest) returns (ConfigureFrequencyVoltageRangeResponse);
  rpc ConfigureMeasCompleteDest(ConfigureMeasCompleteDestRequest) returns (ConfigureMeasCompleteDestResponse);
  rpc ConfigureMultiPoint(ConfigureMultiPointRequest) returns (ConfigureMultiPointResponse);
  rpc ReadMultiPoint(ReadMultiPointRequest) returns (ReadMultiPointResponse);
  rpc FetchMultiPoint(FetchMultiPointRequest) returns (FetchMultiPointResponse);
  rpc ConfigureTriggerSlope(ConfigureTriggerSlopeRequest) returns (ConfigureTriggerSlopeResponse);
  rpc SendSoftwareTrigger(SendSoftwareTriggerRequest) returns (SendSoftwareTriggerResponse);
  rpc GetApertureTimeInfo(GetApertureTimeInfoRequest) returns (GetApertureTimeInfoResponse);
  rpc GetAutoRangeValue(GetAutoRangeValueRequest) returns (GetAutoRangeValueResponse);
  rpc ConfigureAutoZeroMode(ConfigureAutoZeroModeRequest) returns (ConfigureAutoZeroModeResponse);
  rpc ConfigurePowerLineFrequency(ConfigurePowerLineFrequencyRequest) returns (ConfigurePowerLineFrequencyResponse);
  rpc ConfigureMeasurementDigits(ConfigureMeasurementDigitsRequest) returns (ConfigureMeasurementDigitsResponse);
  rpc ConfigureMeasurementAbsolute(ConfigureMeasurementAbsoluteRequest) returns (ConfigureMeasurementAbsoluteResponse);
  rpc ConfigureMeasCompleteSlope(ConfigureMeasCompleteSlopeRequest) returns (ConfigureMeasCompleteSlopeResponse);
  rpc ConfigureSampleTriggerSlope(ConfigureSampleTriggerSlopeRequest) returns (ConfigureSampleTriggerSlopeResponse);
  rpc ReadStatus(ReadStatusRequest) returns (ReadStatusResponse);
  rpc Control(ControlRequest) returns (ControlResponse);
  rpc ConfigureADCCalibration(ConfigureADCCalibrationRequest) returns (ConfigureADCCalibrationResponse);
  rpc ConfigureOffsetCompOhms(ConfigureOffsetCompOhmsRequest) returns (ConfigureOffsetCompOhmsResponse);
  rpc ConfigureCurrentSource(ConfigureCurrentSourceRequest) returns (ConfigureCurrentSourceResponse);
  rpc ConfigureCableCompType(ConfigureCableCompTypeRequest) returns (ConfigureCableCompTypeResponse);
  rpc PerformOpenCableComp(PerformOpenCableCompRequest) returns (PerformOpenCableCompResponse);
  rpc PerformShortCableComp(PerformShortCableCompRequest) returns (PerformShortCableCompResponse);
  rpc ConfigureOpenCableCompValues(ConfigureOpenCableCompValuesRequest) returns (ConfigureOpenCableCompValuesResponse);
  rpc ConfigureShortCableCompValues(ConfigureShortCableCompValuesRequest) returns (ConfigureShortCableCompValuesResponse);
  rpc ConfigureWaveformAcquisition(ConfigureWaveformAcquisitionRequest) returns (ConfigureWaveformAcquisitionResponse);
  rpc ConfigureWaveformCoupling(ConfigureWaveformCouplingRequest) returns (ConfigureWaveformCouplingResponse);
  rpc FetchWaveform(FetchWaveformRequest) returns (FetchWaveformResponse);
  rpc ReadWaveform(ReadWaveformRequest) returns (ReadWaveformResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc GetSelfCalSupported(GetSelfCalSupportedRequest) returns (GetSelfCalSupportedResponse);
  rpc GetCalDateAndTime(GetCalDateAndTimeRequest) returns (GetCalDateAndTimeResponse);
  rpc GetLastCalTemp(GetLastCalTempRequest) returns (GetLastCalTempResponse);
  rpc GetDevTemp(GetDevTempRequest) returns (GetDevTempResponse);
  rpc ConfigureTransducerType(ConfigureTransducerTypeRequest) returns (ConfigureTransducerTypeResponse);
  rpc ConfigureThermocouple(ConfigureThermocoupleRequest) returns (ConfigureThermocoupleResponse);
  rpc ConfigureFixedRefJunction(ConfigureFixedRefJunctionRequest) returns (ConfigureFixedRefJunctionResponse);
  rpc ConfigureRTDType(ConfigureRTDTypeRequest) returns (ConfigureRTDTypeResponse);
  rpc ConfigureRTDCustom(ConfigureRTDCustomRequest) returns (ConfigureRTDCustomResponse);
  rpc ConfigureThermistorType(ConfigureThermistorTypeRequest) returns (ConfigureThermistorTypeResponse);
  rpc ConfigureThermistorCustom(ConfigureThermistorCustomRequest) returns (ConfigureThermistorCustomResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
}

enum NiDmmAttribute {
  NIDMM_ATTRIBUTE_UNSPECIFIED = 0;
  NIDMM_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIDMM_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIDMM_ATTRIBUTE_CACHE = 1050004;
  NIDMM_ATTRIBUTE_SIMULATE = 1050005;
  NIDMM_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIDMM_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDMM_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIDMM_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIDMM_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIDMM_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIDMM_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIDMM_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIDMM_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIDMM_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIDMM_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIDMM_ATTRIBUTE_FUNCTION = 1250001;
  NIDMM_ATTRIBUTE_RANGE = 1250002;
  NIDMM_ATTRIBUTE_RESOLUTION_ABSOLUTE = 1250008;
  NIDMM_ATTRIBUTE_RESOLUTION_DIGITS = 1250003;
  NIDMM_ATTRIBUTE_TRIGGER_DELAY = 1250005;
  NIDMM_ATTRIBUTE_TRIGGER_SOURCE = 1250004;
  NIDMM_ATTRIBUTE_AC_MAX_FREQ = 1250007;
  NIDMM_ATTRIBUTE_AC_MIN_FREQ = 1250006;
  NIDMM_ATTRIBUTE_FREQ_VOLTAGE_RANGE = 1250101;
  NIDMM_ATTRIBUTE_MEAS_COMPLETE_DEST = 1250305;
  NIDMM_ATTRIBUTE_SAMPLE_COUNT = 1250301;
  NIDMM_ATTRIBUTE_SAMPLE_INTERVAL = 1250303;
  NIDMM_ATTRIBUTE_SAMPLE_TRIGGER = 1250302;
  NIDMM_ATTRIBUTE_TRIGGER_COUNT = 1250304;
  NIDMM_ATTRIBUTE_APERTURE_TIME = 1250321;
  NIDMM_ATTRIBUTE_APERTURE_TIME_UNITS = 1250322;
  NIDMM_ATTRIBUTE_AUTO_RANGE_VALUE = 1250331;
  NIDMM_ATTRIBUTE_AUTO_ZERO = 1250332;
  NIDMM_ATTRIBUTE_POWERLINE_FREQ = 1250333;
  NIDMM_ATTRIBUTE_TRIGGER_SLOPE = 1250334;
  NIDMM_ATTRIBUTE_SAMPLE_TRIGGER_SLOPE = 1150010;
  NIDMM_ATTRIBUTE_MEAS_DEST_SLOPE = 1150002;
  NIDMM_ATTRIBUTE_ADC_CALIBRATION = 1150022;
  NIDMM_ATTRIBUTE_OFFSET_COMP_OHMS = 1150023;
  NIDMM_ATTRIBUTE_NUMBER_OF_AVERAGES = 1150032;
  NIDMM_ATTRIBUTE_CURRENT_SOURCE = 1150025;
  NIDMM_ATTRIBUTE_DC_NOISE_REJECTION = 1150026;
  NIDMM_ATTRIBUTE_SETTLE_TIME = 1150028;
  NIDMM_ATTRIBUTE_INPUT_RESISTANCE = 1150029;
  NIDMM_ATTRIBUTE_LATENCY = 1150034;
  NIDMM_ATTRIBUTE_BUFFER_SIZE = 1150037;
  NIDMM_ATTRIBUTE_SHUNT_VALUE = 1150003;
  NIDMM_ATTRIBUTE_OPERATION_MODE = 1150014;
  NIDMM_ATTRIBUTE_WAVEFORM_RATE = 1150018;
  NIDMM_ATTRIBUTE_WAVEFORM_POINTS = 1150019;
  NIDMM_ATTRIBUTE_WAVEFORM_COUPLING = 1150027;
  NIDMM_ATTRIBUTE_FREQ_VOLTAGE_AUTO_RANGE_VALUE = 1150044;
  NIDMM_ATTRIBUTE_CABLE_COMP_TYPE = 1150045;
  NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_REACTANCE = 1150046;
  NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_RESISTANCE = 1150047;
  NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_SUSCEPTANCE = 1150048;
  NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_CONDUCTANCE = 1150049;
  NIDMM_ATTRIBUTE_LC_CALCULATION_MODEL = 1150052;
  NIDMM_ATTRIBUTE_DC_BIAS = 1150053;
  NIDMM_ATTRIBUTE_LC_NUMBER_MEAS_TO_AVERAGE = 1150055;
  NIDMM_ATTRIBUTE_SERIAL_NUMBER = 1150054;
  NIDMM_ATTRIBUTE_CONFIG_PRODUCT_NUMBER = 1150061;
  NIDMM_ATTRIBUTE_TEMP_TRANSDUCER_TYPE = 1250201;
  NIDMM_ATTRIBUTE_TEMP_TC_REF_JUNC_TYPE = 1250232;
  NIDMM_ATTRIBUTE_TEMP_TC_TYPE = 1250231;
  NIDMM_ATTRIBUTE_TEMP_TC_FIXED_REF_JUNC = 1250233;
  NIDMM_ATTRIBUTE_TEMP_RTD_TYPE = 1150120;
  NIDMM_ATTRIBUTE_TEMP_RTD_RES = 1250242;
  NIDMM_ATTRIBUTE_TEMP_RTD_A = 1150121;
  NIDMM_ATTRIBUTE_TEMP_RTD_B = 1150122;
  NIDMM_ATTRIBUTE_TEMP_RTD_C = 1150123;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_TYPE = 1150124;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_A = 1150125;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_B = 1150126;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_C = 1150127;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION = 1050503;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION = 1050504;
}

enum Function {
  FUNCTION_UNSPECIFIED = 0;
  FUNCTION_NIDMM_VAL_DC_VOLTS = 1;
  FUNCTION_NIDMM_VAL_AC_VOLTS = 2;
  FUNCTION_NIDMM_VAL_DC_CURRENT = 3;
  FUNCTION_NIDMM_VAL_AC_CURRENT = 4;
  FUNCTION_NIDMM_VAL_2_WIRE_RES = 5;
  FUNCTION_NIDMM_VAL_4_WIRE_RES = 101;
  FUNCTION_NIDMM_VAL_FREQ = 104;
  FUNCTION_NIDMM_VAL_PERIOD = 105;
  FUNCTION_NIDMM_VAL_TEMPERATURE = 108;
  FUNCTION_NIDMM_VAL_AC_VOLTS_DC_COUPLED = 1001;
  FUNCTION_NIDMM_VAL_DIODE = 1002;
  FUNCTION_NIDMM_VAL_WAVEFORM_VOLTAGE = 1003;
  FUNCTION_NIDMM_VAL_WAVEFORM_CURRENT = 1004;
  FUNCTION_NIDMM_VAL_CAPACITANCE = 1005;
  FUNCTION_NIDMM_VAL_INDUCTANCE = 1006;
}

enum TriggerSource {
  TRIGGER_SOURCE_UNSPECIFIED = 0;
  TRIGGER_SOURCE_NIDMM_VAL_IMMEDIATE = 1;
  TRIGGER_SOURCE_NIDMM_VAL_EXTERNAL = 2;
  TRIGGER_SOURCE_NIDMM_VAL_SOFTWARE_TRIG = 3;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG0 = 111;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG1 = 112;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG2 = 113;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG3 = 114;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG4 = 115;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG5 = 116;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG6 = 117;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG7 = 118;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_STAR = 131;
  TRIGGER_SOURCE_NIDMM_VAL_AUX_TRIG1 = 1001;
  TRIGGER_SOURCE_NIDMM_VAL_LBR_TRIG1 = 1004;
}

enum SampleTrigger {
  SAMPLE_TRIGGER_UNSPECIFIED = 0;
  SAMPLE_TRIGGER_NIDMM_VAL_IMMEDIATE = 1;
  SAMPLE_TRIGGER_NIDMM_VAL_EXTERNAL = 2;
  SAMPLE_TRIGGER_NIDMM_VAL_SOFTWARE_TRIG = 3;
  SAMPLE_TRIGGER_NIDMM_VAL_INTERVAL = 10;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG0 = 111;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG1 = 112;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG2 = 113;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG3 = 114;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG4 = 115;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG5 = 116;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG6 = 117;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG7 = 118;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_STAR = 131;
  SAMPLE_TRIGGER_NIDMM_VAL_AUX_TRIG1 = 1001;
  SAMPLE_TRIGGER_NIDMM_VAL_LBR_TRIG1 = 1004;
}

enum TriggerSlope {
  TRIGGER_SLOPE_NIDMM_VAL_POSITIVE = 0;
  TRIGGER_SLOPE_NIDMM_VAL_NEGATIVE = 1;
}

enum SampleTrigSlope {
  SAMPLE_TRIG_SLOPE_NIDMM_VAL_POSITIVE = 0;
  SAMPLE_TRIG_SLOPE_NIDMM_VAL_NEGATIVE = 1;
}

enum PowerLineFrequencies {
  POWER_LINE_FREQUENCIES_UNSPECIFIED = 0;
  POWER_LINE_FREQUENCIES_NIDMM_VAL_50_HERTZ = 50;
  POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ = 60;
}

enum ApertureTimeUnits {
  APERTURE_TIME_UNITS_NIDMM_VAL_SECONDS = 0;
  APERTURE_TIME_UNITS_NIDMM_VAL_POWER_LINE_CYCLES = 1;
}

enum CompensatedOhms {
  COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_OFF = 0;
  COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_ON = 1;
}

enum CalibrationType {
  CALIBRATION_TYPE_NIDMM_VAL_INTERNAL_AREA = 0;
  CALIBRATION_TYPE_NIDMM_VAL_EXTERNAL_AREA = 1;
}

enum ThermocoupleReferenceJunctionType {
  THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_UNSPECIFIED = 0;
  THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_NIDMM_VAL_TEMP_REF_JUNC_FIXED = 2;
}

enum ThermocoupleType {
  THERMOCOUPLE_TYPE_UNSPECIFIED = 0;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_B = 1;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_E = 4;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_J = 6;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_K = 7;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_N = 8;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_R = 9;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_S = 10;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_T = 11;
}

enum RtdType {
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_CUSTOM = 0;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3750 = 1;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3851 = 2;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3911 = 3;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3916 = 4;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3920 = 5;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3928 = 6;
}

enum AcquisitionStatus {
  ACQUISITION_STATUS_NIDMM_VAL_RUNNING_ANTICOLLISION = 0;
  ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_BACKLOG = 1;
  ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_NO_BACKLOG = 2;
  ACQUISITION_STATUS_NIDMM_VAL_PAUSED = 3;
  ACQUISITION_STATUS_NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS = 4;
}

enum ApertureTime {
  APERTURE_TIME_UNSPECIFIED = 0;
  APERTURE_TIME_NIDMM_VAL_APERTURE_TIME_AUTO = -1;
  APERTURE_TIME_NIDMM_VAL_1_PLC = 1;
  APERTURE_TIME_NIDMM_VAL_5_PLC = 5;
  APERTURE_TIME_NIDMM_VAL_6_PLC = 6;
  APERTURE_TIME_NIDMM_VAL_10_PLC = 10;
  APERTURE_TIME_NIDMM_VAL_12_PLC = 12;
  APERTURE_TIME_NIDMM_VAL_100_PLC = 100;
  APERTURE_TIME_NIDMM_VAL_120_PLC = 120;
}

enum ControlCommit {
  CONTROL_COMMIT_NIDMM_VAL_CONTROL_COMMIT = 0;
}

enum FrequencyVoltageRange {
  FREQUENCY_VOLTAGE_RANGE_UNSPECIFIED = 0;
  FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_ON = -1;
  FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_OFF = -2;
}

enum SampleCount {
  SAMPLE_COUNT_NIDMM_VAL_SAMPLE_COUNT_INFINITE = 0;
}

enum SampleInterval {
  SAMPLE_INTERVAL_UNSPECIFIED = 0;
  SAMPLE_INTERVAL_NIDMM_VAL_AUTO_DELAY = -1;
}

enum TimeLimit {
  TIME_LIMIT_UNSPECIFIED = 0;
  TIME_LIMIT_NIDMM_VAL_TIME_LIMIT_AUTO = -1;
}

enum TriggerCount {
  TRIGGER_COUNT_NIDMM_VAL_TRIG_COUNT_INFINITE = 0;
}

enum TriggerDelays {
  TRIGGER_DELAYS_UNSPECIFIED = 0;
  TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_ON = -1;
  TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_OFF = -2;
}

enum NiDmmInt32AttributeValues {
  option allow_alias = true;
  NIDMM_INT32_UNSPECIFIED = 0;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_OFF = 0;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_AUTO = -1;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_ON = 1;
  NIDMM_INT32_APERTURE_TIME_UNITS_VAL_SECONDS = 0;
  NIDMM_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES = 1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_OFF = 0;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_AUTO = -1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ON = 1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ONCE = 2;
  NIDMM_INT32_BUFFER_SIZE_VAL_BUFFER_SIZE_AUTO = -1;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_NONE = 0;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN = 1;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_SHORT = 2;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN_AND_SHORT = 3;
  NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_OFF = 0;
  NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_ON = 1;
  NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_OFF = 0;
  NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_ON = 1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_NORMAL = 0;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_AUTO = -1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_SECOND_ORDER = 1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_HIGH_ORDER = 2;
  NIDMM_INT32_FUNCTION_VAL_DC_VOLTS = 1;
  NIDMM_INT32_FUNCTION_VAL_AC_VOLTS = 2;
  NIDMM_INT32_FUNCTION_VAL_DC_CURRENT = 3;
  NIDMM_INT32_FUNCTION_VAL_AC_CURRENT = 4;
  NIDMM_INT32_FUNCTION_VAL_2_WIRE_RES = 5;
  NIDMM_INT32_FUNCTION_VAL_4_WIRE_RES = 101;
  NIDMM_INT32_FUNCTION_VAL_FREQ = 104;
  NIDMM_INT32_FUNCTION_VAL_PERIOD = 105;
  NIDMM_INT32_FUNCTION_VAL_TEMPERATURE = 108;
  NIDMM_INT32_FUNCTION_VAL_AC_VOLTS_DC_COUPLED = 1001;
  NIDMM_INT32_FUNCTION_VAL_DIODE = 1002;
  NIDMM_INT32_FUNCTION_VAL_WAVEFORM_VOLTAGE = 1003;
  NIDMM_INT32_FUNCTION_VAL_WAVEFORM_CURRENT = 1004;
  NIDMM_INT32_FUNCTION_VAL_CAPACITANCE = 1005;
  NIDMM_INT32_FUNCTION_VAL_INDUCTANCE = 1006;
  NIDMM_INT32_LATENCY_VAL_LATENCY_AUTO = -1;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_SERIES = 0;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_AUTO = -1;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_PARALLEL = 1;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_NONE = -1;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_EXTERNAL = 2;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_LBR_TRIG0 = 1003;
  NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_OPERATION_MODE_VAL_IVIDMM_MODE = 0;
  NIDMM_INT32_OPERATION_MODE_VAL_WAVEFORM_MODE = 1;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_CUSTOM = 0;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3750 = 1;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3851 = 2;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3911 = 3;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3916 = 4;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3920 = 5;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3928 = 6;
  NIDMM_INT32_SAMPLE_COUNT_VAL_SAMPLE_COUNT_INFINITE = 0;
  NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_IMMEDIATE = 1;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_EXTERNAL = 2;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_SOFTWARE_TRIG = 3;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_INTERVAL = 10;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_STAR = 131;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_AUX_TRIG1 = 1001;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_LBR_TRIG1 = 1004;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_CUSTOM = 0;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44004 = 1;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44006 = 2;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44007 = 3;
  NIDMM_INT32_THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_VAL_TEMP_REF_JUNC_FIXED = 2;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_B = 1;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_E = 4;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_J = 6;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_K = 7;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_N = 8;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_R = 9;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_S = 10;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_T = 11;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMOCOUPLE = 1;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMISTOR = 2;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_2_WIRE_RTD = 3;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_4_WIRE_RTD = 4;
  NIDMM_INT32_TRIGGER_COUNT_VAL_TRIG_COUNT_INFINITE = 0;
  NIDMM_INT32_TRIGGER_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_TRIGGER_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE = 1;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_EXTERNAL = 2;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG = 3;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_STAR = 131;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_AUX_TRIG1 = 1001;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_LBR_TRIG1 = 1004;
  NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_AC = 0;
  NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_DC = 1;
}

enum NiDmmReal64AttributeValues {
  option allow_alias = true;
  NIDMM_REAL64_UNSPECIFIED = 0;
  NIDMM_REAL64_APERTURE_TIME_VAL_APERTURE_TIME_AUTO = -1;
  NIDMM_REAL64_APERTURE_TIME_VAL_1_PLC = 1;
  NIDMM_REAL64_APERTURE_TIME_VAL_5_PLC = 5;
  NIDMM_REAL64_APERTURE_TIME_VAL_6_PLC = 6;
  NIDMM_REAL64_APERTURE_TIME_VAL_10_PLC = 10;
  NIDMM_REAL64_APERTURE_TIME_VAL_12_PLC = 12;
  NIDMM_REAL64_APERTURE_TIME_VAL_100_PLC = 100;
  NIDMM_REAL64_APERTURE_TIME_VAL_120_PLC = 120;
  NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_ON = -1;
  NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_OFF = -2;
  NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ = 50;
  NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ = 60;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ON = -1;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_OFF = -2;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ONCE = -3;
  NIDMM_REAL64_SAMPLE_INTERVAL_VAL_AUTO_DELAY = -1;
  NIDMM_REAL64_SETTLE_TIME_VAL_SETTLE_TIME_AUTO = -1;
  NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_ON = -1;
  NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_OFF = -2;
}

enum NiDmmReal64AttributeValuesMapped {
  NIDMM_REAL64_MAPPED_UNSPECIFIED = 0;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MICROAMP = 1;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_10_MICROAMP = 2;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_100_MICROAMP = 3;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MILLIAMP = 4;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_1_MEGAOHM = 5;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_10_MEGAOHM = 6;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_GREATER_THAN_10_GIGAOHM = 7;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string description = 3;
}

message GetErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message GetErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message SelfCalRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message GetMeasurementPeriodRequest {
  nidevice_grpc.Session vi = 1;
}

message GetMeasurementPeriodResponse {
  int32 status = 1;
  double period = 2;
}

message ConfigureTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_source_enum {
    TriggerSource trigger_source = 2;
    sint32 trigger_source_raw = 3;
  }
  oneof trigger_delay_enum {
    TriggerDelays trigger_delay = 4;
    double trigger_delay_raw = 5;
  }
}

message ConfigureTriggerResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
}

message ReadResponse {
  int32 status = 1;
  double reading = 2;
}

message FetchRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
}

message FetchResponse {
  int32 status = 1;
  double reading = 2;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message InitiateRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message IsOverRangeRequest {
  nidevice_grpc.Session vi = 1;
  double measurement_value = 2;
}

message IsOverRangeResponse {
  int32 status = 1;
  bool is_over_range = 2;
}

message IsUnderRangeRequest {
  nidevice_grpc.Session vi = 1;
  double measurement_value = 2;
}

message IsUnderRangeResponse {
  int32 status = 1;
  bool is_under_range = 2;
}

message ConfigureACBandwidthRequest {
  nidevice_grpc.Session vi = 1;
  double ac_minimum_frequency_hz = 2;
  double ac_maximum_frequency_hz = 3;
}

message ConfigureACBandwidthResponse {
  int32 status = 1;
}

message ConfigureFrequencyVoltageRangeRequest {
  nidevice_grpc.Session vi = 1;
  oneof voltage_range_enum {
    FrequencyVoltageRange voltage_range = 2;
    double voltage_range_raw = 3;
  }
}

message ConfigureFrequencyVoltageRangeResponse {
  int32 status = 1;
}

message ConfigureMeasCompleteDestRequest {
  nidevice_grpc.Session vi = 1;
  sint32 meas_complete_destination = 2;
}

message ConfigureMeasCompleteDestResponse {
  int32 status = 1;
}

message ConfigureMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_count_enum {
    TriggerCount trigger_count = 2;
    sint32 trigger_count_raw = 3;
  }
  oneof sample_count_enum {
    SampleCount sample_count = 4;
    sint32 sample_count_raw = 5;
  }
  oneof sample_trigger_enum {
    SampleTrigger sample_trigger = 6;
    sint32 sample_trigger_raw = 7;
  }
  oneof sample_interval_enum {
    SampleInterval sample_interval = 8;
    double sample_interval_raw = 9;
  }
}

message ConfigureMultiPointResponse {
  int32 status = 1;
}

message ReadMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message ReadMultiPointResponse {
  int32 status = 1;
  repeated double reading_array = 2;
  sint32 actual_number_of_points = 3;
}

message FetchMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message FetchMultiPointResponse {
  int32 status = 1;
  repeated double reading_array = 2;
  sint32 actual_number_of_points = 3;
}

message ConfigureTriggerSlopeRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_slope_enum {
    TriggerSlope trigger_slope = 2;
    sint32 trigger_slope_raw = 3;
  }
}

message ConfigureTriggerSlopeResponse {
  int32 status = 1;
}

message SendSoftwareTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message SendSoftwareTriggerResponse {
  int32 status = 1;
}

message GetApertureTimeInfoRequest {
  nidevice_grpc.Session vi = 1;
}

message GetApertureTimeInfoResponse {
  int32 status = 1;
  ApertureTime aperture_time = 2;
  double aperture_time_raw = 3;
  ApertureTimeUnits aperture_time_units = 4;
  sint32 aperture_time_units_raw = 5;
}

message GetAutoRangeValueRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAutoRangeValueResponse {
  int32 status = 1;
  double actual_range = 2;
}

message ConfigureAutoZeroModeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 auto_zero_mode = 2;
}

message ConfigureAutoZeroModeResponse {
  int32 status = 1;
}

message ConfigurePowerLineFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  oneof power_line_frequency_hz_enum {
    PowerLineFrequencies power_line_frequency_hz = 2;
    double power_line_frequency_hz_raw = 3;
  }
}

message ConfigurePowerLineFrequencyResponse {
  int32 status = 1;
}

message ConfigureMeasurementDigitsRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double resolution_digits = 5;
}

message ConfigureMeasurementDigitsResponse {
  int32 status = 1;
}

message ConfigureMeasurementAbsoluteRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double resolution_absolute = 5;
}

message ConfigureMeasurementAbsoluteResponse {
  int32 status = 1;
}

message ConfigureMeasCompleteSlopeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 meas_complete_slope = 2;
}

message ConfigureMeasCompleteSlopeResponse {
  int32 status = 1;
}

message ConfigureSampleTriggerSlopeRequest {
  nidevice_grpc.Session vi = 1;
  oneof sample_trigger_slope_enum {
    SampleTrigSlope sample_trigger_slope = 2;
    sint32 sample_trigger_slope_raw = 3;
  }
}

message ConfigureSampleTriggerSlopeResponse {
  int32 status = 1;
}

message ReadStatusRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadStatusResponse {
  int32 status = 1;
  sint32 acquisition_backlog = 2;
  AcquisitionStatus acquisition_status = 3;
  sint32 acquisition_status_raw = 4;
}

message ControlRequest {
  nidevice_grpc.Session vi = 1;
  oneof control_action_enum {
    ControlCommit control_action = 2;
    sint32 control_action_raw = 3;
  }
}

message ControlResponse {
  int32 status = 1;
}

message ConfigureADCCalibrationRequest {
  nidevice_grpc.Session vi = 1;
  sint32 adc_calibration = 2;
}

message ConfigureADCCalibrationResponse {
  int32 status = 1;
}

message ConfigureOffsetCompOhmsRequest {
  nidevice_grpc.Session vi = 1;
  oneof offset_comp_ohms_enum {
    CompensatedOhms offset_comp_ohms = 2;
    sint32 offset_comp_ohms_raw = 3;
  }
}

message ConfigureOffsetCompOhmsResponse {
  int32 status = 1;
}

message ConfigureCurrentSourceRequest {
  nidevice_grpc.Session vi = 1;
  double current_source = 2;
}

message ConfigureCurrentSourceResponse {
  int32 status = 1;
}

message ConfigureCableCompTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 cable_comp_type = 2;
}

message ConfigureCableCompTypeResponse {
  int32 status = 1;
}

message PerformOpenCableCompRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformOpenCableCompResponse {
  int32 status = 1;
  double conductance = 2;
  double susceptance = 3;
}

message PerformShortCableCompRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformShortCableCompResponse {
  int32 status = 1;
  double resistance = 2;
  double reactance = 3;
}

message ConfigureOpenCableCompValuesRequest {
  nidevice_grpc.Session vi = 1;
  double conductance = 2;
  double susceptance = 3;
}

message ConfigureOpenCableCompValuesResponse {
  int32 status = 1;
}

message ConfigureShortCableCompValuesRequest {
  nidevice_grpc.Session vi = 1;
  double resistance = 2;
  double reactance = 3;
}

message ConfigureShortCableCompValuesResponse {
  int32 status = 1;
}

message ConfigureWaveformAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double rate = 5;
  sint32 waveform_points = 6;
}

message ConfigureWaveformAcquisitionResponse {
  int32 status = 1;
}

message ConfigureWaveformCouplingRequest {
  nidevice_grpc.Session vi = 1;
  sint32 waveform_coupling = 2;
}

message ConfigureWaveformCouplingResponse {
  int32 status = 1;
}

message FetchWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message FetchWaveformResponse {
  int32 status = 1;
  repeated double waveform_array = 2;
  sint32 actual_number_of_points = 3;
}

message ReadWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message ReadWaveformResponse {
  int32 status = 1;
  repeated double waveform_array = 2;
  sint32 actual_number_of_points = 3;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
    NiDmmReal64AttributeValuesMapped attribute_value_mapped = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
    NiDmmReal64AttributeValuesMapped attribute_value_mapped = 6;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetSelfCalSupportedRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalSupportedResponse {
  int32 status = 1;
  bool self_cal_supported = 2;
}

message GetCalDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  oneof cal_type_enum {
    CalibrationType cal_type = 2;
    sint32 cal_type_raw = 3;
  }
}

message GetCalDateAndTimeResponse {
  int32 status = 1;
  sint32 month = 2;
  sint32 day = 3;
  sint32 year = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetLastCalTempRequest {
  nidevice_grpc.Session vi = 1;
  oneof cal_type_enum {
    CalibrationType cal_type = 2;
    sint32 cal_type_raw = 3;
  }
}

message GetLastCalTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetDevTempRequest {
  nidevice_grpc.Session vi = 1;
  string options = 2;
}

message GetDevTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message ConfigureTransducerTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 transducer_type = 2;
}

message ConfigureTransducerTypeResponse {
  int32 status = 1;
}

message ConfigureThermocoupleRequest {
  nidevice_grpc.Session vi = 1;
  oneof thermocouple_type_enum {
    ThermocoupleType thermocouple_type = 2;
    sint32 thermocouple_type_raw = 3;
  }
  oneof reference_junction_type_enum {
    ThermocoupleReferenceJunctionType reference_junction_type = 4;
    sint32 reference_junction_type_raw = 5;
  }
}

message ConfigureThermocoupleResponse {
  int32 status = 1;
}

message ConfigureFixedRefJunctionRequest {
  nidevice_grpc.Session vi = 1;
  double fixed_reference_junction = 2;
}

message ConfigureFixedRefJunctionResponse {
  int32 status = 1;
}

message ConfigureRTDTypeRequest {
  nidevice_grpc.Session vi = 1;
  oneof rtd_type_enum {
    RtdType rtd_type = 2;
    sint32 rtd_type_raw = 3;
  }
  double rtd_resistance = 4;
}

message ConfigureRTDTypeResponse {
  int32 status = 1;
}

message ConfigureRTDCustomRequest {
  nidevice_grpc.Session vi = 1;
  double rtd_a = 2;
  double rtd_b = 3;
  double rtd_c = 4;
}

message ConfigureRTDCustomResponse {
  int32 status = 1;
}

message ConfigureThermistorTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 thermistor_type = 2;
}

message ConfigureThermistorTypeResponse {
  int32 status = 1;
}

message ConfigureThermistorCustomRequest {
  nidevice_grpc.Session vi = 1;
  double thermistor_a = 2;
  double thermistor_b = 3;
  double thermistor_c = 4;
}

message ConfigureThermistorCustomResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/nidmm.mak sha256=d70252cad61bac702125e82513575f9aa85e6f56f0370ac687adde1617fac1b0 bytes=379 -->
## FILE: src/nidmm/nidmm.mak

- repository: `ni/nimi-python`
- source_path: `src/nidmm/nidmm.mak`
- sha256: `d70252cad61bac702125e82513575f9aa85e6f56f0370ac687adde1617fac1b0`
- bytes: 379

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out rep_caps.rst,$(DEFAULT_RST_FILES_TO_GENERATE))

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/system_tests/grpc_server_config.json sha256=453da06ac823ef5f733913282d322bd4ecfb73e1d4cccf8a992010a64577f288 bytes=156 -->
## FILE: src/nidmm/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/nidmm/system_tests/grpc_server_config.json`
- sha256: `453da06ac823ef5f733913282d322bd4ecfb73e1d4cccf8a992010a64577f288`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31762,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidmm/system_tests/test_system_nidmm.py sha256=8652711d2323b7caac64bb57ce5d7b621f0a48d44f1da60034552496f091fc4d bytes=16839 -->
## FILE: src/nidmm/system_tests/test_system_nidmm.py

- repository: `ni/nimi-python`
- source_path: `src/nidmm/system_tests/test_system_nidmm.py`
- sha256: `8652711d2323b7caac64bb57ce5d7b621f0a48d44f1da60034552496f091fc4d`
- bytes: 16839

````python
import math
import os
import pathlib
import sys
import tempfile
import time

import grpc
import hightime
import numpy
import pytest

import nidmm

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, session_creation_kwargs):
        with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    # Basic usability tests
    def test_take_simple_measurement_works(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        assert session.read() != 0  # Assumes DMM reading is not exactly zero to support non-connected modules and simulated modules.

    def test_acquisition(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        with session.initiate():
            session.fetch()
        with session.initiate():
            session.fetch()

    def test_multi_point_acquisition(self, session):
        session.configure_multi_point(4, 2)
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 1, 5.5)
        measurements = session.read_multi_point(8)
        assert len(measurements) == 8

    # Attribute tests
    def test_vi_string_attribute(self, session):
        assert session.instrument_model == 'NI PXIe-4082'
        try:
            session.instrument_model = 'NI PXIe-4081'
        except nidmm.Error as e:
            assert e.code == -1074135027  # Attribute is read-only

    def test_vi_int32_attribute(self, session):
        session.sample_count = 5
        assert 5 == session.sample_count

    def test_vi_real64_attribute(self, session):
        session.range = 50  # Coerces up!
        assert 100 == session.range

    def test_enum_attribute(self, session):
        session.function = nidmm.Function.AC_CURRENT
        assert session.function == nidmm.Function.AC_CURRENT
        assert type(session.function) is nidmm.Function
        try:
            session.function = nidmm.LCCalculationModel.SERIES
            assert False
        except TypeError:
            pass

    def test_writeonly_attribute(self, session):
        try:
            session.channel_count = 5
            assert False
        except nidmm.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.

    # Function tests
    def test_method_configure_trigger(self, session):
        # Calling Configure Trigger function and asserting True if any error occurred while function call.
        try:
            session.configure_trigger(nidmm.TriggerSource.IMMEDIATE)
        except nidmm.Error:
            assert True

    def test_method_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_method_get_dev_temp(self, session):
        temperature = session.get_dev_temp('')
        assert 20 <= temperature <= 50

    def test_method_reset_with_defaults(self, session):
        assert session.reset_with_defaults() is None

    def test_method_get_self_cal_supported(self, session):
        assert session.get_self_cal_supported() in [True, False]

    def test_method_read_status(self, session):
        backlog, status = session.read_status()
        assert isinstance(backlog, int)
        assert backlog == 0

    def test_fetch_error_while_not_initiated(self, session):
        try:
            session.fetch()
            assert False
        except nidmm.Error as e:
            assert e.code == -1074118641   # called fetch before calling Initiate or after calling Abort

    def test_multi_point_acquisition_with_measurement_absolute(self, session):
        session.configure_multi_point(4, 2)
        session.configure_measurement_absolute(nidmm.Function.DC_VOLTS, 0.02, 0.001)
        measurements = session.read_multi_point(8)
        assert len(measurements) == 8

    def test_disable(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        with session.initiate():
            time.sleep(0.1)
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_BACKLOG
            session.disable()
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS

    def test_fetch_multiple(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.configure_multi_point(sample_count=10, trigger_count=1)
        with session.initiate():
            measurements = session.fetch_multi_point(5)
            assert len(measurements) == 5
            measurements = session.fetch_multi_point(5)
            backlog, acquisition_state = session.read_status()
            assert acquisition_state == nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG

    def test_get_auto_range_value(self, session):
        with session.initiate():
            session.fetch()
            auto_range_value_property = session.auto_range_value
            assert auto_range_value_property == 300   # simulated device auto_range_value to maximum 300

    def test_get_cal_date_time(self, session):
        last_cal = session.get_cal_date_and_time(0)
        assert last_cal.month == 3
        assert last_cal.day == 1
        assert last_cal.year == 1940
        assert last_cal.hour == 0
        assert last_cal.minute == 0   # cal_date_and_time should be 03/01/1940:00:00 for simulated 408x devices; 407x and 4065 returns 00/00/0000:00:00

    def test_get_last_cal_temperature(self, session):
        last_cal_temp = session.get_last_cal_temp(0)
        assert last_cal_temp == 25   # last_cal_temp should be 25 for simulated 408x devices; 407x and 4065 returns 0

    def test_trigger_max_time_exceeded_errror(self, session):
        try:
            session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
            session.configure_multi_point(sample_count=10, trigger_count=1)
            session.read_multi_point(15)
            assert False
        except nidmm.Error as e:
            assert e.code == -1074126845  # Max Time exceeded before operation completed

    def test_self_cal(self, session):
        try:
            session.self_cal()
        except nidmm.Error:
            assert False

    def test_configure_rtd(self, session):
        session.configure_rtd_type(nidmm.RTDType.CUSTOM, 110)
        assert session.temp_rtd_type == nidmm.RTDType.CUSTOM
        assert session.temp_rtd_res == 110
        session.configure_rtd_custom(0.1, 0.2, 0.3)
        assert session.temp_rtd_a == 0.1
        assert session.temp_rtd_b == 0.2
        assert session.temp_rtd_c == 0.3

    def test_configure_thermistor(self, session):
        session.temp_thermistor_type = nidmm.ThermistorType.CUSTOM
        session.configure_thermistor_custom(0.1, 0.2, 0.3)
        assert session.temp_thermistor_a == 0.1
        assert session.temp_thermistor_b == 0.2
        assert session.temp_thermistor_c == 0.3

    def test_configure_thermocouple(self, session):
        session.configure_thermocouple(nidmm.ThermocoupleType.K, nidmm.ThermocoupleReferenceJunctionType.FIXED)
        assert session.temp_tc_type == nidmm.ThermocoupleType.K
        assert session.temp_tc_ref_junc_type == nidmm.ThermocoupleReferenceJunctionType.FIXED

    def test_configure_waveform_acquisition(self, session):
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 100, 1800000, 400)
        assert session.function == nidmm.Function.WAVEFORM_VOLTAGE
        assert session.range == 100
        assert session.waveform_rate == 1800000
        assert session.waveform_points == 400

    def test_fetch_waveform(self, session):
        number_of_points_to_read = 100
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
        with session.initiate():
            measurements = session.fetch_waveform(number_of_points_to_read)
            assert len(measurements) == number_of_points_to_read
            assert isinstance(measurements[1], float)

    def test_fetch_waveform_error(self, session):
        number_of_points_to_read = 100
        try:
            session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
            with session.initiate():
                session.fetch_waveform(number_of_points_to_read * 2, maximum_time=hightime.timedelta(milliseconds=1))   # trying to fetch points more than configured
                assert False
        except nidmm.Error as e:
            assert e.code == -1074126845  # Max Time exceeded before operation completed

    def test_perform_cable_compensation(self, session):
        session.configure_measurement_digits(nidmm.Function.CAPACITANCE, 0.002, 5.5)
        conductance, susceptance = session.perform_open_cable_comp()
        assert conductance == 0   # simulated device should return conductance, susceptance as 0
        assert susceptance == 0
        resistance, reactance = session.perform_short_cable_comp()
        assert resistance == 0   # simulated device should return resistance,reactance as 0
        assert reactance == 0

    def test_read_waveform(self, session):
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, 1000)
        with session.initiate():
            number_of_points_to_read = 100
            measurements = session.read_waveform(number_of_points_to_read)
            assert len(measurements) == number_of_points_to_read
            assert isinstance(measurements[1], float)

    def test_send_software_trigger(self, session):
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
        session.configure_multi_point(sample_count=0, sample_trigger=nidmm.SampleTrigger.SOFTWARE_TRIG, trigger_count=1)
        with session.initiate():
            session.send_software_trigger()    # Send_software_trigger will send triggers automatically for simulated devices. This line of code confirms there is no error while calling send_trigger function
            session.fetch_multi_point(3)

    def test_reset_method(self, session):
        default_function = session.function
        session.function = nidmm.Function.PERIOD
        session.reset()
        function_after_reset = session.function
        assert default_function == function_after_reset

    def test_import_export_buffer(self, session):
        test_value_1 = 1
        test_value_2 = 2
        session.sample_count = test_value_1
        assert session.sample_count == test_value_1
        buffer = session.export_attribute_configuration_buffer()
        session.sample_count = test_value_2
        assert session.sample_count == test_value_2
        session.import_attribute_configuration_buffer(buffer)
        assert session.sample_count == test_value_1

    def test_import_export_file(self, session):
        test_value_1 = 1
        test_value_2 = 2
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        session.sample_count = test_value_1
        assert session.sample_count == test_value_1
        session.export_attribute_configuration_file(path)
        session.sample_count = test_value_2
        assert session.sample_count == test_value_2
        session.import_attribute_configuration_file(path)
        assert session.sample_count == test_value_1
        os.remove(path)

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe', **session_creation_kwargs):
                assert False
        except nidmm.Error as e:
            assert e.code == -1074134964
            assert e.description.find('The option string parameter contains an entry with an unknown option value.') != -1

    # No boolean attributes that aren't IVI
    '''
    def test_vi_boolean_attribute(self, session):
        assert session.interchange_check is False

    def test_set_boolean_attribute(self, session):
        session.cache = False
        assert session.cache is False
        session.cache = True
        assert session.cache is True
    '''

    def test_get_ext_cal_recommended_interval(self, session):
        interval = session.get_ext_cal_recommended_interval()
        assert interval.days == 730

    def test_locks_are_reentrant(self, session):
        with session.lock():
            with session.lock():
                interval = session.get_ext_cal_recommended_interval()
                assert interval.days == 730

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    def test_fetch_waveform_into(self, session):
        number_of_points_to_read = 100
        session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, 10, 1800000, number_of_points_to_read)
        with session.initiate():
            waveform = numpy.empty(number_of_points_to_read, dtype=numpy.float64)
            # Initialize with NaN so we can later verify all samples were overwritten by the driver.
            waveform.fill(float('nan'))
            session.fetch_waveform_into(waveform)
        for sample in waveform:
            assert not math.isnan(sample)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, '')
        return {'grpc_options': grpc_options}

    def test_new_session_already_exists(self, grpc_channel):
        session_name = 'existing_session'
        expected_error_message = "Cannot initialize '" + session_name + "' when a session already exists."
        expected_grpc_error = grpc.StatusCode.ALREADY_EXISTS
        init_behavior = nidmm.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, session_name, initialization_behavior=init_behavior)
        with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', grpc_options=grpc_options):
            try:
                with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', grpc_options=grpc_options):
                    assert False
            except nidmm.Error as e:
                assert e.rpc_code == expected_grpc_error
                assert e.description == expected_error_message
                assert str(e) == f'{expected_grpc_error}: {expected_error_message}'

    def test_attach_to_non_existent_session(self, grpc_channel):
        session_name = 'non_existent_session'
        expected_error_message = "Cannot attach to '" + session_name + "' because a session has not been initialized."
        expected_grpc_error = grpc.StatusCode.FAILED_PRECONDITION
        init_behavior = nidmm.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
        grpc_options = nidmm.GrpcSessionOptions(grpc_channel, session_name, initialization_behavior=init_behavior)
        try:
            with nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4082; BoardType:PXIe', grpc_options=grpc_options):
                assert False
        except nidmm.Error as e:
            assert e.rpc_code == expected_grpc_error
            assert e.description == expected_error_message
            assert str(e) == f'{expected_grpc_error}: {expected_error_message}'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/custom_types/custom_struct.py sha256=a94d67bd1b3a7360b5c4bf85a25d3a98a7fc2fbb21115c17778cf9191115b00e bytes=1582 -->
## FILE: src/nifake/custom_types/custom_struct.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/custom_types/custom_struct.py`
- sha256: `a94d67bd1b3a7360b5c4bf85a25d3a98a7fc2fbb21115c17778cf9191115b00e`
- bytes: 1582

````python
import ctypes

import nifake._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_CustomStruct(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()


class CustomStruct:
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def _create_copy(self, target_class):
        return target_class(struct_int=self.struct_int, struct_double=self.struct_double)

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/custom_types/custom_struct_nested_typedef.py sha256=4945f5fb3dbd8e7d62062595649762a1eeab969b4e5c6bb37edf891f513163ae bytes=2363 -->
## FILE: src/nifake/custom_types/custom_struct_nested_typedef.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/custom_types/custom_struct_nested_typedef.py`
- sha256: `4945f5fb3dbd8e7d62062595649762a1eeab969b4e5c6bb37edf891f513163ae`
- bytes: 2363

````python
import ctypes

import nifake.custom_struct as custom_struct
import nifake.custom_struct_typedef as custom_struct_typedef


class struct_CustomStructNestedTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_custom_struct', custom_struct.struct_CustomStruct),
        ('struct_custom_struct_typedef', custom_struct_typedef.struct_CustomStructTypedef),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_custom_struct = custom_struct.struct_CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = custom_struct.struct_CustomStruct()
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef()


class CustomStructNestedTypedef:
    def __init__(
        self,
        data=None,
        struct_custom_struct=custom_struct.CustomStruct(),
        struct_custom_struct_typedef=custom_struct_typedef.CustomStructTypedef()
    ):
        if data is not None:
            self.struct_custom_struct = custom_struct.CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = struct_custom_struct
            self.struct_custom_struct_typedef = struct_custom_struct_typedef

    def _create_copy(self, target_class):
        sample_object = target_class()
        return target_class(
            struct_custom_struct=self.struct_custom_struct._create_copy(
                type(sample_object.struct_custom_struct)
            ),
            struct_custom_struct_typedef=self.struct_custom_struct_typedef._create_copy(
                type(sample_object.struct_custom_struct_typedef)
            ),
        )

    def __repr__(self):
        return '{}(data=None, struct_custom_struct={}, struct_custom_struct_typedef={})'.format(
            self.__class__.__name__,
            repr(self.struct_custom_struct),
            repr(self.struct_custom_struct_typedef)
        )

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/custom_types/custom_struct_typedef.py sha256=be78d97161bdae9a5886f24a56ec10d128035da22248361ecb04b91e57e66bc1 bytes=1246 -->
## FILE: src/nifake/custom_types/custom_struct_typedef.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/custom_types/custom_struct_typedef.py`
- sha256: `be78d97161bdae9a5886f24a56ec10d128035da22248361ecb04b91e57e66bc1`
- bytes: 1246

````python
import ctypes

import nifake._visatype


class struct_CustomStructTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = 0
            self.struct_double = 0.0


class CustomStructTypedef:
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def _create_copy(self, target_class):
        return target_class(struct_int=self.struct_int, struct_double=self.struct_double)

    def __repr__(self):
        return '{}(data=None, struct_int={}, struct_double={})'.format(
            self.__class__.__name__,
            self.struct_int,
            self.struct_double
        )

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nifake/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/attributes.py sha256=9e85b5067b8fa15aa84bf5ff88b6d95379c4fcdfc3e7ee43992a4fbeb9a8fb76 bytes=5533 -->
## FILE: src/nifake/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/attributes.py`
- sha256: `9e85b5067b8fa15aa84bf5ff88b6d95379c4fcdfc3e7ee43992a4fbeb9a8fb76`
- bytes: 5533

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 25.8.0d9999
attributes = {
    1000000: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type bool with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'type': 'ViBoolean'
    },
    1000001: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type float with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Float',
        'name': 'READ_WRITE_DOUBLE',
        'type': 'ViReal64'
    },
    1000002: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type string with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write String',
        'name': 'READ_WRITE_STRING',
        'type': 'ViString'
    },
    1000003: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type Color with read/write access.'
        },
        'enum': 'Color',
        'lv_property': 'Fake attributes:Read Write Color',
        'name': 'READ_WRITE_COLOR',
        'type': 'ViInt32'
    },
    1000004: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Int',
        'name': 'READ_WRITE_INTEGER',
        'type': 'ViInt32'
    },
    1000005: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'An attribute with an enum that is also a float'
        },
        'enum': 'FloatEnum',
        'lv_property': 'Fake attributes:Float enum',
        'name': 'FLOAT_ENUM',
        'type': 'ViReal64'
    },
    1000006: {
        'access': 'read-write',
        'documentation': {
            'description': 'An attribute of type 64-bit integer with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write long long',
        'name': 'READ_WRITE_INT64',
        'type': 'ViInt64'
    },
    1000007: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Attribute in seconds'
        },
        'lv_property': 'Fake attributes:Read Write Double with Converter',
        'name': 'READ_WRITE_DOUBLE_WITH_CONVERTER',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1000008: {
        'access': 'read-write',
        'attribute_class': 'AttributeViInt32TimeDeltaMilliseconds',
        'documentation': {
            'description': 'Attribute in milliseconds'
        },
        'lv_property': 'Fake attributes:Read Write Int with Converter',
        'name': 'READ_WRITE_INTEGER_WITH_CONVERTER',
        'type': 'ViInt32',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
    },
    1000009: {
        'access': 'read-write',
        'name': 'READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1000010: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringRepeatedCapability',
        'documentation': {
            'description': 'An attribute with read/write access, that represents a repeated capability'
        },
        'lv_property': 'Fake attributes:Read Write String Repeated Capability',
        'name': 'READ_WRITE_STRING_REPEATED_CAPABILITY',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString',
        'type_in_documentation': "Any repeated capability type, as defined in nimi-python:\n        - str\n        - str - Comma delimited list\n        - str - Range (using '-' or ':')\n        - int\n        - Basic sequence types (list, tuple, range, slice) of other supported types"
    },
    1000011: {
        'access': 'read-write',
        'enum': 'EnumWithConverter',
        'grpc_enum': None,
        'name': 'READ_WRITE_ENUM_WITH_CONVERTER',
        'type': 'ViInt32'
    },
    1000012: {
        'access': 'read-write',
        'grpc_enum': 'SampleCount',
        'name': 'SAMPLE_COUNT',
        'type': 'ViInt32'
    },
    1000013: {
        'access': 'read-write',
        'grpc_enum': 'SampleInterval',
        'name': 'SAMPLE_INTERVAL',
        'type': 'ViReal64'
    },
    1000014: {
        'access': 'read-write',
        'attribute_class': 'AttributeViInt32TimeDeltaMonths',
        'documentation': {
            'description': 'Attribute in months'
        },
        'lv_property': 'Fake attributes:Read Write Int with month Converter',
        'name': 'READ_WRITE_INTEGER_WITH_MONTH_CONVERTER',
        'type': 'ViInt32',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in months'
    },
    1000015: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'documentation': {
            'description': 'An attribute of type comma separated string with read/write access.'
        },
        'lv_property': 'Fake attributes:Read Write Comma Separated String',
        'name': 'READ_WRITE_COMMA_SEPARATED_STRING',
        'type': 'ViString'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nifake/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/config.py sha256=7f6d6ea5e0741a5ba0c467a67f69d075c409653c8c578e0bc62ea8234d073304 bytes=2266 -->
## FILE: src/nifake/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/config.py`
- sha256: `7f6d6ea5e0741a5ba0c467a67f69d075c409653c8c578e0bc62ea8234d073304`
- bytes: 2266

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 25.8.0d9999
config = {
    'api_version': '25.8.0d9999',
    'c_function_prefix': 'niFake_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'FakeCustomStruct',
            'python_name': 'CustomStruct'
        },
        {
            'ctypes_type': 'struct_CustomStructTypedef',
            'file_name': 'custom_struct_typedef',
            'grpc_name': 'CustomStructTypedef',
            'python_name': 'CustomStructTypedef'
        },
        {
            'ctypes_type': 'struct_CustomStructNestedTypedef',
            'file_name': 'custom_struct_nested_typedef',
            'grpc_name': 'CustomStructNestedTypedef',
            'python_name': 'CustomStructNestedTypedef'
        }
    ],
    'driver_name': 'NI-FAKE',
    'enum_whitelist_suffix': [
        '_POINT_FIVE'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiFake',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifake',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifake_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifake_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nifake',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/config_addon.py sha256=59bae42e3d2ae4a3830a7b86bb818d88da16629b620c9ec1fdc2d35979bdab92 bytes=167 -->
## FILE: src/nifake/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/config_addon.py`
- sha256: `59bae42e3d2ae4a3830a7b86bb818d88da16629b620c9ec1fdc2d35979bdab92`
- bytes: 167

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/enums.py sha256=018c813fbe3191ebd6a3e08daa02b24b6f80e8649803892488b02c6d8b2b324c bytes=9524 -->
## FILE: src/nifake/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/enums.py`
- sha256: `018c813fbe3191ebd6a3e08daa02b24b6f80e8649803892488b02c6d8b2b324c`
- bytes: 9524

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 25.8.0d9999
enums = {
    'AltColor': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'BeautifulColor': {
        'values': [
            {
                'name': 'NIFAKE_VAL_PINK',
                'value': 44
            },
            {
                'name': 'NIFAKE_VAL_AQUA',
                'value': 43
            },
            {
                'name': 'NIFAKE_VAL_GREEN',
                'value': 45
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'Color': {
        'values': [
            {
                'documentation': {
                    'description': 'Like blood.'
                },
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Like the sky.'
                },
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Like a banana.'
                },
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'documentation': {
                    'description': "Like this developer's conscience."
                },
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'ColorObsolete': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'ColorPrivate': {
        'values': [
            {
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'DecimalMixedNumber': {
        'values': [
            {
                'name': 'NIFAKE_VAL_TWENTY_TWO',
                'value': 22.0
            },
            {
                'name': 'NIFAKE_VAL_TWO_POINT_TWO',
                'value': 2.2
            },
            {
                'name': 'NIFAKE_VAL_NEGATIVE_THREE',
                'value': -3.0
            },
            {
                'name': 'NIFAKE_VAL_MAX_INT_32',
                'value': 2147483647.0
            },
            {
                'name': 'NIFAKE_VAL_MAX_INT_32_PLUS_ONE',
                'value': 2147483648.0
            },
            {
                'name': 'NIFAKE_VAL_MIN_INT_32',
                'value': -2147483648.0
            },
            {
                'name': 'NIFAKE_VAL_MIN_INT_32_MINUS_ONE',
                'value': -2147483649.0
            }
        ]
    },
    'DecimalWholeNumberMapped': {
        'values': [
            {
                'name': 'NIFAKE_VAL_NEGATIVE_ONE',
                'value': -1.0
            },
            {
                'name': 'NIFAKE_VAL_TWENTY_TWO',
                'value': 22.0
            },
            {
                'name': 'NIFAKE_VAL_ZERO',
                'value': 0.0
            }
        ]
    },
    'EnumWithConverter': {
        'codegen_method': 'public',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {
                'converts_to_value': True,
                'name': 'NIFAKE_VAL_RED',
                'value': 1
            },
            {
                'converts_to_value': False,
                'name': 'NIFAKE_VAL_BLUE',
                'value': 2
            },
            {
                'converts_to_value': 'yellow',
                'name': 'NIFAKE_VAL_YELLOW',
                'value': 5
            },
            {
                'converts_to_value': 42,
                'name': 'NIFAKE_VAL_BLACK',
                'value': 42
            }
        ]
    },
    'EnumWithGrpcNameValues': {
        'values': [
            {
                'name': 'NIFAKE_VAL_ONE',
                'value': 1
            },
            {
                'name': 'NIFAKE_VAL_TWO',
                'value': 2
            }
        ]
    },
    'FloatEnum': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies 3.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_THREE_POINT_FIVE',
                'value': 3.5
            },
            {
                'documentation': {
                    'description': 'Specifies 4.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_FOUR_POINT_FIVE',
                'value': 4.5
            },
            {
                'documentation': {
                    'description': 'Specifies 5.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_FIVE_POINT_FIVE',
                'value': 5.5
            },
            {
                'documentation': {
                    'description': 'Specifies 6.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_SIX_POINT_FIVE',
                'value': 6.5
            },
            {
                'documentation': {
                    'description': 'Specifies 7.5 digits resolution.'
                },
                'name': 'NIFAKE_VAL_SEVEN_POINT_FIVE',
                'value': 7.5
            }
        ]
    },
    'IntFlagEnum': {
        'class': 'IntFlag',
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Flag A option.'
                },
                'name': 'NIFAKE_VAL_FLAG_A',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Flag B option.'
                },
                'name': 'NIFAKE_VAL_FLAG_B',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Flag E option.'
                },
                'name': 'NIFAKE_VAL_FLAG_E',
                'value': 1073741824
            }
        ]
    },
    'MobileOSNames': {
        'values': [
            {
                'documentation': {
                    'description': 'Most popular OS.'
                },
                'name': 'NIFAKE_VAL_ANDROID',
                'value': 'Android'
            },
            {
                'documentation': {
                    'description': 'Most secure OS.'
                },
                'name': 'NIFAKE_VAL_IOS',
                'value': 'iOS'
            },
            {
                'documentation': {
                    'description': 'Remember Symbian?.'
                },
                'name': 'NIFAKE_VAL_NONE',
                'value': 'None'
            }
        ]
    },
    'NotGeneratedStringEnum': {
        'values': [
            {
                'name': 'NIFAKE_VAL_ANDROID',
                'value': 'Android'
            },
            {
                'name': 'NIFAKE_VAL_IOS',
                'value': 'iOS'
            },
            {
                'name': 'NIFAKE_VAL_NONE',
                'value': 'None'
            }
        ]
    },
    'SampleCount': {
        'values': [
            {
                'name': 'NIFAKE_VAL_SAMPLE_COUNT_INFINITE',
                'value': 0
            }
        ]
    },
    'SampleInterval': {
        'values': [
            {
                'name': 'NIFAKE_VAL_AUTO_DELAY',
                'value': -1.0
            }
        ]
    },
    'Turtle': {
        'values': [
            {
                'documentation': {
                    'description': 'Wields two katanas.'
                },
                'name': 'NIFAKE_VAL_LEONARDO',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses a bo staff.'
                },
                'name': 'NIFAKE_VAL_DONATELLO',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Has a pair of sai.'
                },
                'name': 'NIFAKE_VAL_RAPHAEL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Owns nunchucks.'
                },
                'name': 'NIFAKE_VAL_MICHELANGELO',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nifake/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/functions.py sha256=ac4dd7d64be5ac77feb7148ae307d04b126e37aee7c7cd41b17692af46b734ff bytes=109619 -->
## FILE: src/nifake/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/functions.py`
- sha256: `ac4dd7d64be5ac77feb7148ae307d04b126e37aee7c7cd41b17692af46b734ff`
- bytes: 109619

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 25.8.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Aborts a previously initiated thingie.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Accepts list of hightime.timedelta or datetime.timedelta or float instances representing time delays.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Count of input values.'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A collection of time delay values.'
                },
                'name': 'delays',
                'python_api_converter_name': 'convert_timedeltas_to_seconds_real64',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayOutputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of booleans.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains an array of booleans'
                },
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureABC': {
        'documentation': {
            'description': 'TBD'
        },
        'grpc_name': 'ConfigureAbc',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CustomNestedStructRoundtrip': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'nestedCustomTypeIn',
                'type': 'CustomStructNestedTypedef'
            },
            {
                'direction': 'out',
                'name': 'nestedCustomTypeOut',
                'type': 'CustomStructNestedTypedef'
            }
        ],
        'returns': 'ViStatus'
    },
    'DoubleAllTheNums': {
        'documentation': {
            'description': 'Test for buffer with converter'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the number array'
                },
                'name': 'numberCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'numbers is an array of numbers we want to double.'
                },
                'name': 'numbers',
                'python_api_converter_name': 'convert_double_each_element',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberCount'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumArrayOutputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of enums, stored as 16 bit integers under the hood.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains an array of enums, stored as 16 bit integers under the hood '
                },
                'enum': 'Turtle',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes one parameter other than the session, which happens to be an enum and has a default value.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'Turtle.LEONARDO',
                'direction': 'in',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': 'Export configuration buffer.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns waveform data.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to return'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Samples fetched from the device. Array should be numberOfSamples big.'
                },
                'name': 'waveformData',
                'numpy': True,
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of samples actually fetched.'
                },
                'name': 'actualNumberOfSamples',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FunctionWithIntflagParameter': {
        'codegen_method': 'public',
        'documentation': {
            'description': "Calls a function that takes a flag parameter which can be OR'd from multiple enum values."
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A flag parameter that can be a combination (bitwise OR) of IntFlagEnum values.'
                },
                'enum': 'IntFlagEnum',
                'grpc_enum': None,
                'name': 'flag',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FunctionWithRepeatedCapabilityType': {
        'documentation': {
            'description': 'A function with a parameter that specifies repeated_capability_type.'
        },
        'has_repeated_capability': True,
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A list of sites.'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'GetABoolean': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a boolean.',
            'note': 'This function rules!'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetANumber': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number.',
            'note': 'This function rules!'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringOfFixedMaximumSize': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Illustrates returning a string of fixed size.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'String comes back here. Buffer must be 256 big.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringUsingPythonCode': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a string of length aNumber.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'a_number'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceCharArray': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'charArray',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayForPythonCodeCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array of custom type using python-code size mechanism'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayForPythonCodeDouble': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array for use in python-code size mechanism.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array of double using python-code size mechanism'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.get_array_size_for_python_code()'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArraySizeForPythonCode': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns the size of the array for use in python-code size mechanism.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Size of array'
                },
                'name': 'sizeOut',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayUsingIviDance': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns an array of float whose size is determined with the IVI dance.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the buffer for copyint arrayOut onto.'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The array returned by this function'
                },
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
                },
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViReal attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes in attributeValue. You can IVI-dance with this.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the attribute.'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).'
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalInterval': {
        'documentation': {
            'description': 'Returns the recommended maximum interval, in **months**, between external calibrations.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the recommended maximum interval, in **months**, between external calibrations.'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelNames': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns a list of channel names for the given channel indices.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.'
                },
                'name': 'indices',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for names.'
                },
                'name': 'nameSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.'
                },
                'name': 'names',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns a custom type.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomTypeArray': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns a custom type.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Get using custom type'
                },
                'name': 'cs',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomTypeTypedef': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function returns a custom type with typedef and a custom type with nested typedef.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An object of a custom type with typedef'
                },
                'name': 'cst',
                'type': 'CustomStructTypedef'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An object of a custom type with nested typedef'
                },
                'name': 'csnt',
                'type': 'CustomStructNestedTypedef'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEnumValue': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns an enum value',
            'note': 'Splinter is not supported.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This is an amount.',
                    'note': 'The amount will be between -2^31 and (2^31-1)'
                },
                'name': 'aQuantity',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the error information associated with the session.'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns errorCode for the session. If you pass 0 for bufferSize, you can pass VI_NULL for this.'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes in description buffer.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'At least bufferSize big, string comes out here.'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).'
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'returns': 'ViStatus'
    },
    'GetParameterWithOverriddenGrpcName': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_name': 'overridden_parameter',
                'name': 'originalParameter',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'enum': 'Turtle',
                'grpc_name': 'enum_parameter_raw',
                'name': 'enumParameter',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': 'Import configuration buffer.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBufferEx': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViAddr[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates a new IVI instrument driver session.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': 'This is just some string.',
                    'description': 'Contains the **resource_name** of the device to initialize.'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'NI-FAKE is probably not needed.',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether to reset',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Some options'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a ViSession handle that you use.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Initiates a thingie.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': 'Lock.'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Optional'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'MethodUsingWholeAndFractionalNumbers': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'out',
                'grpc_enum': 'DecimalWholeNumber',
                'name': 'wholeNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_enum': 'DecimalMixedNumber',
                'name': 'fractionalNumber',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithGrpcOnlyParam': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'simpleParam',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithProtoOnlyParameter': {
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArrayTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Receives and returns multiple types of arrays.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of the array that will be returned.'
                },
                'name': 'outputArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Array that will be returned.',
                    'note': 'The size must be at least outputArraySize.'
                },
                'name': 'outputArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'outputArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of doubles with fixed size.'
                },
                'name': 'outputArrayOfFixedLength',
                'size': {
                    'mechanism': 'fixed',
                    'value': 3
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of inputArrayOfFloats and inputArrayOfIntegers'
                },
                'name': 'inputArraySizes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of floats'
                },
                'name': 'inputArrayOfFloats',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViReal64[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.'
                },
                'name': 'inputArrayOfIntegers',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSize': {
        'documentation': {
            'description': 'Function to test multiple arrays that use the same size'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 1 of same size.'
                },
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 2 of same size.'
                },
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 3 of same size.'
                },
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array 4 of same size.'
                },
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size for all arrays'
                },
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'OneInputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes one parameter other than the session.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number'
                },
                'name': 'aNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParametersAreMultipleTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Has parameters of multiple types.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a 32-bit integer.'
                },
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a 64-bit integer.'
                },
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A float enum.'
                },
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'An IVI dance string.'
                },
                'name': 'aString',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PoorlyNamedSimpleFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes no parameters other than the session.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'simple_function',
        'returns': 'ViStatus'
    },
    'PublicGetChannelNames': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns a list of channel names for the given channel indices.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'get_channel_names'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.'
                },
                'name': 'indices',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViString',
                'type_in_documentation': 'basic sequence types or str or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for names.'
                },
                'name': 'nameSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.'
                },
                'name': 'names',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameSize'
                },
                'type': 'ViString',
                'type_in_documentation': 'list of str'
            }
        ],
        'python_name': 'get_channel_names',
        'render_in_session_base': True,
        'returns': None
    },
    'Read': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in seconds.'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadFromChannel': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **maximum_time** allowed in milliseconds.'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnANumberAndAString': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a number.'
                },
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a string. Buffer must be 256 bytes or larger.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnDurationInSeconds': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a hightime.timedelta instance.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Duration in seconds.'
                },
                'name': 'timedelta',
                'python_api_converter_name': 'convert_seconds_real64_to_timedelta',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a list of hightime.timedelta instances.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in output.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a list of hightime.timedelta instances.'
                },
                'name': 'timedeltas',
                'python_api_converter_name': 'convert_seconds_real64_to_timedeltas',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnMultipleTypes': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns multiple types.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a boolean.'
                },
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a 32-bit integer.'
                },
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains a 64-bit integer.'
                },
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates a ninja turtle',
                    'table_body': [
                        [
                            '0',
                            'Leonardo'
                        ],
                        [
                            '1',
                            'Donatello'
                        ],
                        [
                            '2',
                            'Raphael'
                        ],
                        [
                            '3',
                            'Mich elangelo'
                        ]
                    ]
                },
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value.'
                },
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A float enum.'
                },
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of measurements to acquire.'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': 'The size must be at least arraySize.'
                },
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of bytes allocated for aString'
                },
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An IVI dance string.'
                },
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'stringSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViBoolean attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViInt32 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_enum': 'NiFakeInt32AttributeValues',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViInt64 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViReal64 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_enum': 'NiFakeReal64AttributeValues',
                'grpc_mapped_enum': 'NiFakeReal64AttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function sets the value of a ViString attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'This is the channel(s) that this function will apply to.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomType': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes a custom type.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomTypeArray': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes an array of custom types.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the array.'
                },
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Set using custom type'
                },
                'name': 'cs',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'StringValuedEnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes one parameter other than the session, which happens to be a string-valued enum and has a default value.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi**'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'MobileOSNames.ANDROID',
                'direction': 'in',
                'documentation': {
                    'description': 'Indicates a Mobile OS',
                    'table_body': [
                        [
                            'ANDROID',
                            'Android'
                        ],
                        [
                            'IOS',
                            'iOS'
                        ],
                        [
                            'NONE',
                            'None'
                        ]
                    ]
                },
                'enum': 'MobileOSNames',
                'name': 'aMobileOSName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TwoInputFunction': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'This function takes two parameters other than the session.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a number'
                },
                'name': 'aNumber',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Contains a string'
                },
                'name': 'aString',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': 'Unlock'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Optional'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Use64BitNumber': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a number and a string.',
            'note': 'This function rules!'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A big number on its way in.'
                },
                'name': 'input',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A big number on its way out.'
                },
                'name': 'output',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Writes waveform to the driver'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'How many samples the waveform contains.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform data.'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformNumpyComplex64': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'A function that writes a waveform of numpy complex64 samples.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the message signal.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumberF32[]',
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformNumpyComplex128': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'A function that writes a waveform of numpy complex128 samples.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the message signal.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformNumpyComplexInterleavedI16': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'A function that writes a waveform of numpy complex i16 samples.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the message signal.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'complex_array_representation': 'interleaved_real_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexI16[]',
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Function that takes a 3D numpy array of numpy complex128 as an input parameter.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the 3D array of numpy complex numbers to write.'
                },
                'name': 'multidimensionalArray',
                'type': 'NIComplexNumber[]',
                'numpy': True,
                'use_in_python_api': True,
                'array_dimensions': 3
            },
        ],
        'python_name': 'function_with_3d_numpy_array_of_numpy_complex128_input_parameter',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Takes the errorCode returned by a functiona and returns it as a user-readable string.'
        },
        'grpc_name': 'ErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The errorCode returned from the instrument.'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted into a string.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Performs a self-test'
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'MultipleArraysDifferentSize': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Test function with multiple arrays that have different size parameters. This tests the length handling mechanism where different array parameters can reference different size parameters.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of double values with its own size parameter.'
                },
                'name': 'valuesArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'valuesArraySize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the values array.'
                },
                'name': 'valuesArraySize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of integer values with a different size parameter.'
                },
                'name': 'dataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'ViInt32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the data array.'
                },
                'name': 'dataArraySize',
                'type': 'ViInt32',
                'use_array': False
            }
        ],
        'returns': 'ViStatus'
    },
    'MixedIviDanceAndLenMechanism': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Test function with mixed size mechanisms: one len-sized input array and one IVI-dance output array.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Input array of doubles using len size mechanism.'
                },
                'name': 'inputValues',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputValuesSize'
                },
                'type': 'ViReal64[]',
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of elements in inputValues.'
                },
                'name': 'inputValuesSize',
                'type': 'ViInt32',
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the output array for IVI dance.'
                },
                'name': 'outputSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Output array using IVI-dance size mechanism.'
                },
                'name': 'outputArray',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'outputSize'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Performs a self-test.'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niFake_InitWithOptions.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Contains the value returned from the instrument self-test. Zero indicates success.'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/nifake/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/metadata/nifake.proto sha256=37fab5cc6fbb1e3c58bac9fbbb5b29258197227750dd11f41b0f5d67481a6c16 bytes=38454 -->
## FILE: src/nifake/metadata/nifake.proto

- repository: `ni/nimi-python`
- source_path: `src/nifake/metadata/nifake.proto`
- sha256: `37fab5cc6fbb1e3c58bac9fbbb5b29258197227750dd11f41b0f5d67481a6c16`
- bytes: 38454

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-FAKE API metadata version 24.8.0f100
//---------------------------------------------------------------------
// Proto file for the NI-FAKE Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.fake";
option java_outer_classname = "NiFake";
option csharp_namespace = "NationalInstruments.Grpc.Fake";

package nifake_grpc;

import "session.proto";

service NiFake {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc BoolArrayOutputFunction(BoolArrayOutputFunctionRequest) returns (BoolArrayOutputFunctionResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc EnumArrayOutputFunction(EnumArrayOutputFunctionRequest) returns (EnumArrayOutputFunctionResponse);
  rpc EnumInputFunctionWithDefaults(EnumInputFunctionWithDefaultsRequest) returns (EnumInputFunctionWithDefaultsResponse);
  rpc StringValuedEnumInputFunctionWithDefaults(StringValuedEnumInputFunctionWithDefaultsRequest) returns (StringValuedEnumInputFunctionWithDefaultsResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc FetchWaveform(FetchWaveformRequest) returns (FetchWaveformResponse);
  rpc GetABoolean(GetABooleanRequest) returns (GetABooleanResponse);
  rpc GetANumber(GetANumberRequest) returns (GetANumberResponse);
  rpc GetAStringOfFixedMaximumSize(GetAStringOfFixedMaximumSizeRequest) returns (GetAStringOfFixedMaximumSizeResponse);
  rpc GetAnIviDanceCharArray(GetAnIviDanceCharArrayRequest) returns (GetAnIviDanceCharArrayResponse);
  rpc GetArrayUsingIviDance(GetArrayUsingIviDanceRequest) returns (GetArrayUsingIviDanceResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetCalDateAndTime(GetCalDateAndTimeRequest) returns (GetCalDateAndTimeResponse);
  rpc GetCalInterval(GetCalIntervalRequest) returns (GetCalIntervalResponse);
  rpc GetEnumValue(GetEnumValueRequest) returns (GetEnumValueResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc MultipleArrayTypes(MultipleArrayTypesRequest) returns (MultipleArrayTypesResponse);
  rpc MultipleArraysSameSize(MultipleArraysSameSizeRequest) returns (MultipleArraysSameSizeResponse);
  rpc MultipleArraysDifferentSize(MultipleArraysDifferentSizeRequest) returns (MultipleArraysDifferentSizeResponse);
  rpc MixedIviDanceAndLenMechanism(MixedIviDanceAndLenMechanismRequest) returns (MixedIviDanceAndLenMechanismResponse);
  rpc OneInputFunction(OneInputFunctionRequest) returns (OneInputFunctionResponse);
  rpc ParametersAreMultipleTypes(ParametersAreMultipleTypesRequest) returns (ParametersAreMultipleTypesResponse);
  rpc PoorlyNamedSimpleFunction(PoorlyNamedSimpleFunctionRequest) returns (PoorlyNamedSimpleFunctionResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc ReadFromChannel(ReadFromChannelRequest) returns (ReadFromChannelResponse);
  rpc ReturnANumberAndAString(ReturnANumberAndAStringRequest) returns (ReturnANumberAndAStringResponse);
  rpc ReturnMultipleTypes(ReturnMultipleTypesRequest) returns (ReturnMultipleTypesResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc TwoInputFunction(TwoInputFunctionRequest) returns (TwoInputFunctionResponse);
  rpc Use64BitNumber(Use64BitNumberRequest) returns (Use64BitNumberResponse);
  rpc WriteWaveform(WriteWaveformRequest) returns (WriteWaveformResponse);
  rpc WriteWaveformNumpyComplex128(WriteWaveformNumpyComplex128Request) returns (WriteWaveformNumpyComplex128Response);
  rpc WriteWaveformNumpyComplex64(WriteWaveformNumpyComplex64Request) returns (WriteWaveformNumpyComplex64Response);
  rpc WriteWaveformNumpyComplexInterleavedI16(WriteWaveformNumpyComplexInterleavedI16Request) returns (WriteWaveformNumpyComplexInterleavedI16Response);
  rpc SetCustomType(SetCustomTypeRequest) returns (SetCustomTypeResponse);
  rpc SetCustomTypeArray(SetCustomTypeArrayRequest) returns (SetCustomTypeArrayResponse);
  rpc GetCustomType(GetCustomTypeRequest) returns (GetCustomTypeResponse);
  rpc GetCustomTypeArray(GetCustomTypeArrayRequest) returns (GetCustomTypeArrayResponse);
  rpc GetAnIviDanceWithATwistArray(GetAnIviDanceWithATwistArrayRequest) returns (GetAnIviDanceWithATwistArrayResponse);
  rpc GetAnIviDanceWithATwistString(GetAnIviDanceWithATwistStringRequest) returns (GetAnIviDanceWithATwistStringResponse);
  rpc DoubleAllTheNums(DoubleAllTheNumsRequest) returns (DoubleAllTheNumsResponse);
  rpc AcceptListOfDurationsInSeconds(AcceptListOfDurationsInSecondsRequest) returns (AcceptListOfDurationsInSecondsResponse);
  rpc ReturnDurationInSeconds(ReturnDurationInSecondsRequest) returns (ReturnDurationInSecondsResponse);
  rpc ReturnListOfDurationsInSeconds(ReturnListOfDurationsInSecondsRequest) returns (ReturnListOfDurationsInSecondsResponse);
  rpc ConfigureAbc(ConfigureAbcRequest) returns (ConfigureAbcResponse);
  rpc ConfigureEnums(ConfigureEnumsRequest) returns (ConfigureEnumsResponse);
  rpc ExportAttributeConfigurationBufferEx(ExportAttributeConfigurationBufferExRequest) returns (ExportAttributeConfigurationBufferExResponse);
  rpc ImportAttributeConfigurationBufferEx(ImportAttributeConfigurationBufferExRequest) returns (ImportAttributeConfigurationBufferExResponse);
  rpc FetchWithCustomSize(FetchWithCustomSizeRequest) returns (FetchWithCustomSizeResponse);
  rpc GetParameterWithOverriddenGrpcName(GetParameterWithOverriddenGrpcNameRequest) returns (GetParameterWithOverriddenGrpcNameResponse);
  rpc IviDanceWithTwistWithMultipleArraysAndOneBufferSize(IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest) returns (IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse);
  rpc FunctionWithOverriddenGrpcName2x(FunctionWithOverriddenGrpcName2xRequest) returns (FunctionWithOverriddenGrpcName2xResponse);
  rpc FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest) returns (FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse);
  rpc StringValuedEnumNoEnumGenerated(StringValuedEnumNoEnumGeneratedRequest) returns (StringValuedEnumNoEnumGeneratedResponse);
  rpc IviDanceWithATwistCalculatedSizeOut(IviDanceWithATwistCalculatedSizeOutRequest) returns (IviDanceWithATwistCalculatedSizeOutResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc Control4022(Control4022Request) returns (Control4022Response);
  rpc AcceptViSessionArray(AcceptViSessionArrayRequest) returns (AcceptViSessionArrayResponse);
  rpc AcceptViUInt32Array(AcceptViUInt32ArrayRequest) returns (AcceptViUInt32ArrayResponse);
  rpc BoolArrayInputFunction(BoolArrayInputFunctionRequest) returns (BoolArrayInputFunctionResponse);
  rpc CloseExtCal(CloseExtCalRequest) returns (CloseExtCalResponse);
  rpc CommandWithReservedParam(CommandWithReservedParamRequest) returns (CommandWithReservedParamResponse);
  rpc CreateConfigurationList(CreateConfigurationListRequest) returns (CreateConfigurationListResponse);
  rpc CustomNestedStructRoundtrip(CustomNestedStructRoundtripRequest) returns (CustomNestedStructRoundtripResponse);
  rpc GetBitfieldAsEnumArray(GetBitfieldAsEnumArrayRequest) returns (GetBitfieldAsEnumArrayResponse);
  rpc GetAnIviDanceWithATwistArrayOfCustomType(GetAnIviDanceWithATwistArrayOfCustomTypeRequest) returns (GetAnIviDanceWithATwistArrayOfCustomTypeResponse);
  rpc GetAnIviDanceWithATwistArrayWithInputArray(GetAnIviDanceWithATwistArrayWithInputArrayRequest) returns (GetAnIviDanceWithATwistArrayWithInputArrayResponse);
  rpc GetAnIviDanceWithATwistByteArray(GetAnIviDanceWithATwistByteArrayRequest) returns (GetAnIviDanceWithATwistByteArrayResponse);
  rpc GetAnIviDanceWithATwistStringStrlenBug(GetAnIviDanceWithATwistStringStrlenBugRequest) returns (GetAnIviDanceWithATwistStringStrlenBugResponse);
  rpc GetArraySizeForCustomCode(GetArraySizeForCustomCodeRequest) returns (GetArraySizeForCustomCodeResponse);
  rpc GetArrayViUInt8WithEnum(GetArrayViUInt8WithEnumRequest) returns (GetArrayViUInt8WithEnumResponse);
  rpc GetViUInt8(GetViUInt8Request) returns (GetViUInt8Response);
  rpc GetViInt32Array(GetViInt32ArrayRequest) returns (GetViInt32ArrayResponse);
  rpc GetViUInt32Array(GetViUInt32ArrayRequest) returns (GetViUInt32ArrayResponse);
  rpc MethodUsingEnumWithGrpcNameValues(MethodUsingEnumWithGrpcNameValuesRequest) returns (MethodUsingEnumWithGrpcNameValuesResponse);
  rpc MethodWithGetLastErrorParam(MethodWithGetLastErrorParamRequest) returns (MethodWithGetLastErrorParamResponse);
  rpc MethodWithGrpcOnlyParam(MethodWithGrpcOnlyParamRequest) returns (MethodWithGrpcOnlyParamResponse);
  rpc MethodUsingWholeAndFractionalNumbers(MethodUsingWholeAndFractionalNumbersRequest) returns (MethodUsingWholeAndFractionalNumbersResponse);
  rpc MethodUsingWholeMappedNumbers(MethodUsingWholeMappedNumbersRequest) returns (MethodUsingWholeMappedNumbersResponse);
  rpc MethodWithGrpcFieldNumber(MethodWithGrpcFieldNumberRequest) returns (MethodWithGrpcFieldNumberResponse);
  rpc MethodWithProtoOnlyParameter(MethodWithProtoOnlyParameterRequest) returns (MethodWithProtoOnlyParameterResponse);
  rpc ReadDataWithInOutIviTwist(ReadDataWithInOutIviTwistRequest) returns (ReadDataWithInOutIviTwistResponse);
  rpc ReadDataWithMultipleIviTwistParamSets(ReadDataWithMultipleIviTwistParamSetsRequest) returns (ReadDataWithMultipleIviTwistParamSetsResponse);
  rpc InitExtCal(InitExtCalRequest) returns (InitExtCalResponse);
  rpc InitWithVarArgs(InitWithVarArgsRequest) returns (InitWithVarArgsResponse);
  rpc MultipleArraysSameSizeWithOptional(MultipleArraysSameSizeWithOptionalRequest) returns (MultipleArraysSameSizeWithOptionalResponse);
  rpc UseATwoDimensionParameter(UseATwoDimensionParameterRequest) returns (UseATwoDimensionParameterResponse);
  rpc ViUInt8ArrayInputFunction(ViUInt8ArrayInputFunctionRequest) returns (ViUInt8ArrayInputFunctionResponse);
  rpc ViUInt8ArrayOutputFunction(ViUInt8ArrayOutputFunctionRequest) returns (ViUInt8ArrayOutputFunctionResponse);
  rpc ViInt16ArrayInputFunction(ViInt16ArrayInputFunctionRequest) returns (ViInt16ArrayInputFunctionResponse);
}

enum NiFakeAttribute {
  NIFAKE_ATTRIBUTE_UNSPECIFIED = 0;
  NIFAKE_ATTRIBUTE_READ_WRITE_BOOL = 1000000;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE = 1000001;
  NIFAKE_ATTRIBUTE_READ_WRITE_STRING = 1000002;
  NIFAKE_ATTRIBUTE_READ_WRITE_COLOR = 1000003;
  NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER = 1000004;
  NIFAKE_ATTRIBUTE_FLOAT_ENUM_NAME_OVERRIDE = 1000005;
  NIFAKE_ATTRIBUTE_READ_WRITE_INT64 = 1000006;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_CONVERTER = 1000007;
  NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER_WITH_CONVERTER = 1000008;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY = 1000009;
  NIFAKE_ATTRIBUTE_READ_WRITE_STRING_REPEATED_CAPABILITY = 1000010;
  NIFAKE_ATTRIBUTE_SAMPLE_COUNT = 1000012;
  NIFAKE_ATTRIBUTE_SAMPLE_INTERVAL = 1000013;
}

enum GrpcColorOverride {
  GRPC_COLOR_OVERRIDE_UNSPECIFIED = 0;
  GRPC_COLOR_OVERRIDE_RED = 1;
  GRPC_COLOR_OVERRIDE_BLUE = 2;
  GRPC_COLOR_OVERRIDE_YELLOW = 5;
  GRPC_COLOR_OVERRIDE_BLACK = 42;
}

enum FloatEnum {
  FLOAT_ENUM_UNSPECIFIED = 0;
  FLOAT_ENUM_THREE_POINT_FIVE = 1;
  FLOAT_ENUM_FOUR_POINT_FIVE = 2;
  FLOAT_ENUM_FIVE_POINT_FIVE = 3;
  FLOAT_ENUM_SIX_POINT_FIVE = 4;
  FLOAT_ENUM_SEVEN_POINT_FIVE = 5;
}

enum Turtle {
  TURTLE_LEONARDO = 0;
  TURTLE_DONATELLO = 1;
  TURTLE_RAPHAEL = 2;
  TURTLE_MICHELANGELO = 3;
}

enum MobileOSNames {
  MOBILE_OS_NAMES_UNSPECIFIED = 0;
  MOBILE_OS_NAMES_ANDROID = 1;
  MOBILE_OS_NAMES_IOS = 2;
  MOBILE_OS_NAMES_NONE = 3;
}

enum Bitfield {
  BITFIELD_UNSPECIFIED = 0;
  BITFIELD_FLAG_A = 1;
  BITFIELD_FLAG_B = 2;
  BITFIELD_FLAG_C = 4;
  BITFIELD_FLAG_D = 8;
}

enum DecimalWholeNumber {
  DECIMAL_WHOLE_NUMBER_ZERO = 0;
  DECIMAL_WHOLE_NUMBER_NEGATIVE_ONE = -1;
  DECIMAL_WHOLE_NUMBER_TWENTY_TWO = 22;
}

enum DecimalWholeNumberMapped {
  DECIMAL_WHOLE_NUMBER_MAPPED_UNSPECIFIED = 0;
  DECIMAL_WHOLE_NUMBER_MAPPED_ZERO = 1;
  DECIMAL_WHOLE_NUMBER_MAPPED_NEGATIVE_ONE = 2;
  DECIMAL_WHOLE_NUMBER_MAPPED_TWENTY_TWO = 3;
}

enum DecimalMixedNumber {
  DECIMAL_MIXED_NUMBER_UNSPECIFIED = 0;
  DECIMAL_MIXED_NUMBER_TWENTY_TWO = 1;
  DECIMAL_MIXED_NUMBER_TWO_POINT_TWO = 2;
  DECIMAL_MIXED_NUMBER_NEGATIVE_THREE = 3;
  DECIMAL_MIXED_NUMBER_MAX_INT_32 = 4;
  DECIMAL_MIXED_NUMBER_MAX_INT_32_PLUS_ONE = 5;
  DECIMAL_MIXED_NUMBER_MIN_INT_32 = 6;
  DECIMAL_MIXED_NUMBER_MIN_INT_32_MINUS_ONE = 7;
}

enum EnumWithGrpcNameValues {
  ENUM_WITH_GRPC_NAME_VALUES_UNSPECIFIED = 0;
  ENUM_WITH_GRPC_NAME_VALUES_ALTERED_GRPC_NAME_ONE = 1;
  ENUM_WITH_GRPC_NAME_VALUES_TWO = 2;
}

enum SampleCount {
  SAMPLE_COUNT_SAMPLE_COUNT_INFINITE = 0;
}

enum SampleInterval {
  SAMPLE_INTERVAL_UNSPECIFIED = 0;
  SAMPLE_INTERVAL_AUTO_DELAY = -1;
}

enum NiFakeInt32AttributeValues {
  option allow_alias = true;
  NIFAKE_INT32_UNSPECIFIED = 0;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_RED = 1;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLUE = 2;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_YELLOW = 5;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLACK = 42;
  NIFAKE_INT32_SAMPLE_COUNT_SAMPLE_COUNT_INFINITE = 0;
}

enum NiFakeReal64AttributeValues {
  NIFAKE_REAL64_UNSPECIFIED = 0;
  NIFAKE_REAL64_SAMPLE_INTERVAL_AUTO_DELAY = -1;
}

enum NiFakeReal64AttributeValuesMapped {
  NIFAKE_REAL64_MAPPED_UNSPECIFIED = 0;
  NIFAKE_REAL64_FLOAT_ENUM_THREE_POINT_FIVE = 1;
  NIFAKE_REAL64_FLOAT_ENUM_FOUR_POINT_FIVE = 2;
  NIFAKE_REAL64_FLOAT_ENUM_FIVE_POINT_FIVE = 3;
  NIFAKE_REAL64_FLOAT_ENUM_SIX_POINT_FIVE = 4;
  NIFAKE_REAL64_FLOAT_ENUM_SEVEN_POINT_FIVE = 5;
}

message FakeCustomStruct {
  sint32 struct_int = 1;
  double struct_double = 2;
}

message CustomStructNestedTypedef {
  FakeCustomStruct struct_custom_struct = 1;
  CustomStructTypedef struct_custom_struct_typedef = 2;
}

message CustomStructTypedef {
  sint32 struct_int = 1;
  double struct_double = 2;
}

message NIComplexI16_struct {
  sint32 real = 1;
  sint32 imaginary = 2;
}

message NIComplexNumber_struct {
  double real = 1;
  double imaginary = 2;
}

message NIComplexNumberF32_struct {
  float real = 1;
  float imaginary = 2;
}

message StringAndTurtle {
  string string_arg = 1;
  Turtle turtle = 2;
}

message CustomNamedType {
  string string_arg = 1;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message BoolArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message BoolArrayOutputFunctionResponse {
  int32 status = 1;
  repeated bool an_array = 2;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message EnumArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message EnumArrayOutputFunctionResponse {
  int32 status = 1;
  repeated Turtle an_array = 2;
  repeated sint32 an_array_raw = 3;
}

message EnumInputFunctionWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
  oneof a_turtle_enum {
    Turtle a_turtle = 2;
    sint32 a_turtle_raw = 3;
  }
}

message EnumInputFunctionWithDefaultsResponse {
  int32 status = 1;
}

message StringValuedEnumInputFunctionWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
  oneof a_mobile_os_name_enum {
    MobileOSNames a_mobile_os_name_mapped = 2;
    string a_mobile_os_name_raw = 3;
  }
}

message StringValuedEnumInputFunctionWithDefaultsResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message FetchWaveformRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_samples = 2;
}

message FetchWaveformResponse {
  int32 status = 1;
  repeated double waveform_data = 2;
  sint32 actual_number_of_samples = 3;
}

message GetABooleanRequest {
  nidevice_grpc.Session vi = 1;
}

message GetABooleanResponse {
  int32 status = 1;
  bool a_boolean = 2;
}

message GetANumberRequest {
  nidevice_grpc.Session vi = 1;
}

message GetANumberResponse {
  int32 status = 1;
  sint32 a_number = 2;
}

message GetAStringOfFixedMaximumSizeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAStringOfFixedMaximumSizeResponse {
  int32 status = 1;
  string a_string = 2;
}

message GetAnIviDanceCharArrayRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceCharArrayResponse {
  int32 status = 1;
  string char_array = 2;
}

message GetArrayUsingIviDanceRequest {
  nidevice_grpc.Session vi = 1;
}

message GetArrayUsingIviDanceResponse {
  int32 status = 1;
  repeated double array_out = 2;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetCalDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 cal_type = 2;
}

message GetCalDateAndTimeResponse {
  int32 status = 1;
  sint32 month = 2;
  sint32 day = 3;
  sint32 year = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetCalIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetCalIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetEnumValueRequest {
  nidevice_grpc.Session vi = 1;
}

message GetEnumValueResponse {
  int32 status = 1;
  sint32 a_quantity = 2;
  Turtle a_turtle = 3;
  sint32 a_turtle_raw = 4;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string description = 3;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  bool new_session_initialized = 3;
}

message MultipleArrayTypesRequest {
  nidevice_grpc.Session vi = 1;
  sint32 output_array_size = 2;
  repeated double input_array_of_floats = 3;
  repeated sint32 input_array_of_integers = 4;
}

message MultipleArrayTypesResponse {
  int32 status = 1;
  repeated double output_array = 2;
  repeated double output_array_of_fixed_length = 3;
}

message MultipleArraysSameSizeRequest {
  nidevice_grpc.Session vi = 1;
  repeated double values1 = 2;
  repeated double values2 = 3;
  repeated double values3 = 4;
  repeated double values4 = 5;
}

message MultipleArraysSameSizeResponse {
  int32 status = 1;
}

message MultipleArraysDifferentSizeRequest {
  nidevice_grpc.Session vi = 1;
  repeated double values_array = 2;
  repeated sint32 data_array = 3;
}

message MultipleArraysDifferentSizeResponse {
  int32 status = 1;
}

message MixedIviDanceAndLenMechanismRequest {
  nidevice_grpc.Session vi = 1;
  repeated double input_values = 2;
}

message MixedIviDanceAndLenMechanismResponse {
  int32 status = 1;
  repeated sint32 output_array = 2;
}

message OneInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 a_number = 2;
}

message OneInputFunctionResponse {
  int32 status = 1;
}

message ParametersAreMultipleTypesRequest {
  nidevice_grpc.Session vi = 1;
  bool a_boolean = 2;
  sint32 an_int32 = 3;
  int64 an_int64 = 4;
  oneof an_int_enum_enum {
    Turtle an_int_enum = 5;
    sint32 an_int_enum_raw = 6;
  }
  double a_float = 7;
  oneof a_float_enum_enum {
    FloatEnum a_float_enum_mapped = 8;
    double a_float_enum_raw = 9;
  }
  string a_string = 10;
}

message ParametersAreMultipleTypesResponse {
  int32 status = 1;
}

message PoorlyNamedSimpleFunctionRequest {
  nidevice_grpc.Session vi = 1;
}

message PoorlyNamedSimpleFunctionResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  double maximum_time = 2;
}

message ReadResponse {
  int32 status = 1;
  double reading = 2;
}

message ReadFromChannelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 maximum_time = 3;
}

message ReadFromChannelResponse {
  int32 status = 1;
  double reading = 2;
}

message ReturnANumberAndAStringRequest {
  nidevice_grpc.Session vi = 1;
}

message ReturnANumberAndAStringResponse {
  int32 status = 1;
  sint32 a_number = 2;
  string a_string = 3;
}

message ReturnMultipleTypesRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_size = 2;
}

message ReturnMultipleTypesResponse {
  int32 status = 1;
  bool a_boolean = 2;
  sint32 an_int32 = 3;
  int64 an_int64 = 4;
  Turtle an_int_enum = 5;
  sint32 an_int_enum_raw = 6;
  double a_float = 7;
  FloatEnum a_float_enum_mapped = 8;
  double a_float_enum_raw = 9;
  repeated double an_array = 10;
  string a_string = 11;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFakeInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFakeReal64AttributeValues attribute_value = 4;
    NiFakeReal64AttributeValuesMapped attribute_value_mapped = 5;
    double attribute_value_raw = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message TwoInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  double a_number = 2;
  string a_string = 3;
}

message TwoInputFunctionResponse {
  int32 status = 1;
}

message Use64BitNumberRequest {
  nidevice_grpc.Session vi = 1;
  int64 input = 2;
}

message Use64BitNumberResponse {
  int32 status = 1;
  int64 output = 2;
}

message WriteWaveformRequest {
  nidevice_grpc.Session vi = 1;
  repeated double waveform = 2;
}

message WriteWaveformResponse {
  int32 status = 1;
}

message WriteWaveformNumpyComplex128Request {
  nidevice_grpc.Session vi = 1;
  repeated NIComplexNumber_struct waveform_data_array = 2;
}

message WriteWaveformNumpyComplex128Response {
  int32 status = 1;
}

message WriteWaveformNumpyComplex64Request {
  nidevice_grpc.Session vi = 1;
  repeated NIComplexNumberF32_struct waveform_data_array = 2;
}

message WriteWaveformNumpyComplex64Response {
  int32 status = 1;
}

message WriteWaveformNumpyComplexInterleavedI16Request {
  nidevice_grpc.Session vi = 1;
  repeated NIComplexI16_struct waveform_data_array = 2;
}

message WriteWaveformNumpyComplexInterleavedI16Response {
  int32 status = 1;
}

message SetCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
  FakeCustomStruct cs = 2;
}

message SetCustomTypeResponse {
  int32 status = 1;
}

message SetCustomTypeArrayRequest {
  nidevice_grpc.Session vi = 1;
  repeated FakeCustomStruct cs = 2;
}

message SetCustomTypeArrayResponse {
  int32 status = 1;
}

message GetCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetCustomTypeResponse {
  int32 status = 1;
  FakeCustomStruct cs = 2;
}

message GetCustomTypeArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message GetCustomTypeArrayResponse {
  int32 status = 1;
  repeated FakeCustomStruct cs = 2;
}

message GetAnIviDanceWithATwistArrayRequest {
  nidevice_grpc.Session vi = 1;
  string a_string = 2;
}

message GetAnIviDanceWithATwistArrayResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistStringRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceWithATwistStringResponse {
  int32 status = 1;
  string a_string = 2;
  sint32 actual_size = 3;
}

message DoubleAllTheNumsRequest {
  nidevice_grpc.Session vi = 1;
  repeated double numbers = 2;
}

message DoubleAllTheNumsResponse {
  int32 status = 1;
}

message AcceptListOfDurationsInSecondsRequest {
  nidevice_grpc.Session vi = 1;
  repeated double delays = 2;
}

message AcceptListOfDurationsInSecondsResponse {
  int32 status = 1;
}

message ReturnDurationInSecondsRequest {
  nidevice_grpc.Session vi = 1;
}

message ReturnDurationInSecondsResponse {
  int32 status = 1;
  double timedelta = 2;
}

message ReturnListOfDurationsInSecondsRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message ReturnListOfDurationsInSecondsResponse {
  int32 status = 1;
  repeated double timedeltas = 2;
}

message ConfigureAbcRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureAbcResponse {
  int32 status = 1;
}

message ConfigureEnumsRequest {
  nidevice_grpc.Session vi = 1;
  oneof sample_count_enum {
    SampleCount sample_count = 2;
    sint32 sample_count_raw = 3;
  }
  oneof sample_interval_enum {
    SampleInterval sample_interval = 4;
    double sample_interval_raw = 5;
  }
}

message ConfigureEnumsResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferExRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferExResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferExRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferExResponse {
  int32 status = 1;
}

message FetchWithCustomSizeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_waveforms = 2;
  sint32 number_of_samples = 3;
}

message FetchWithCustomSizeResponse {
  int32 status = 1;
  repeated double waveform_data = 2;
}

message GetParameterWithOverriddenGrpcNameRequest {
  nidevice_grpc.Session vi = 1;
  oneof enum_parameter_raw_enum {
    Turtle enum_parameter_raw = 2;
    sint32 enum_parameter_raw_raw = 3;
  }
}

message GetParameterWithOverriddenGrpcNameResponse {
  int32 status = 1;
  sint32 overridden_parameter = 2;
}

message IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest {
  nidevice_grpc.Session vi = 1;
}

message IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse {
  int32 status = 1;
  repeated sint32 array1 = 2;
  repeated sint32 array2 = 3;
  repeated sint32 array3 = 4;
  sint32 actual_num_elements = 5;
}

message FunctionWithOverriddenGrpcName2xRequest {
  nidevice_grpc.Session vi = 1;
}

message FunctionWithOverriddenGrpcName2xResponse {
  int32 status = 1;
}

message FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest {
  nidevice_grpc.Session vi = 1;
  repeated NIComplexNumber_struct multidimensional_array = 2;
}

message FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse {
  int32 status = 1;
}

message StringValuedEnumNoEnumGeneratedRequest {
  nidevice_grpc.Session vi = 1;
  string a_string_enum = 2;
}

message StringValuedEnumNoEnumGeneratedResponse {
  int32 status = 1;
}

message IviDanceWithATwistCalculatedSizeOutRequest {
  nidevice_grpc.Session vi = 1;
}

message IviDanceWithATwistCalculatedSizeOutResponse {
  int32 status = 1;
  repeated uint32 data = 2;
  sint32 actual_num_waveforms = 3;
  sint32 actual_samples_per_waveform = 4;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message Control4022Request {
  string resource_name = 1;
  sint32 configuration = 2;
}

message Control4022Response {
  int32 status = 1;
}

message AcceptViSessionArrayRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session session_array = 2;
}

message AcceptViSessionArrayResponse {
  int32 status = 1;
}

message AcceptViUInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  repeated uint32 u_int32_array = 2;
}

message AcceptViUInt32ArrayResponse {
  int32 status = 1;
}

message BoolArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
  repeated bool an_array = 3;
}

message BoolArrayInputFunctionResponse {
  int32 status = 1;
}

message CloseExtCalRequest {
  nidevice_grpc.Session vi = 1;
  sint32 action = 2;
}

message CloseExtCalResponse {
  int32 status = 1;
}

message CommandWithReservedParamRequest {
  nidevice_grpc.Session vi = 1;
}

message CommandWithReservedParamResponse {
  int32 status = 1;
}

message CreateConfigurationListRequest {
  repeated NiFakeAttribute list_attribute_ids = 1;
}

message CreateConfigurationListResponse {
  int32 status = 1;
}

message CustomNestedStructRoundtripRequest {
  CustomStructNestedTypedef nested_custom_type_in = 1;
}

message CustomNestedStructRoundtripResponse {
  int32 status = 1;
  CustomStructNestedTypedef nested_custom_type_out = 2;
}

message GetBitfieldAsEnumArrayRequest {
}

message GetBitfieldAsEnumArrayResponse {
  int32 status = 1;
  repeated Bitfield flags_array = 2;
  int64 flags_raw = 3;
}

message GetAnIviDanceWithATwistArrayOfCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceWithATwistArrayOfCustomTypeResponse {
  int32 status = 1;
  repeated FakeCustomStruct array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistArrayWithInputArrayRequest {
  repeated sint32 data_in = 1;
}

message GetAnIviDanceWithATwistArrayWithInputArrayResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistByteArrayRequest {
}

message GetAnIviDanceWithATwistByteArrayResponse {
  int32 status = 1;
  bytes array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistStringStrlenBugRequest {
}

message GetAnIviDanceWithATwistStringStrlenBugResponse {
  int32 status = 1;
  string string_out = 2;
  sint32 actual_size = 3;
}

message GetArraySizeForCustomCodeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetArraySizeForCustomCodeResponse {
  int32 status = 1;
  sint32 size_out = 2;
}

message GetArrayViUInt8WithEnumRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetArrayViUInt8WithEnumResponse {
  int32 status = 1;
  repeated GrpcColorOverride u_int8_enum_array = 2;
  bytes u_int8_enum_array_raw = 3;
}

message GetViUInt8Request {
  nidevice_grpc.Session vi = 1;
}

message GetViUInt8Response {
  int32 status = 1;
  uint32 a_uint8_number = 2;
}

message GetViInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetViInt32ArrayResponse {
  int32 status = 1;
  repeated sint32 int32_array = 2;
}

message GetViUInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetViUInt32ArrayResponse {
  int32 status = 1;
  repeated uint32 u_int32_array = 2;
}

message MethodUsingEnumWithGrpcNameValuesRequest {
  oneof using_enum_enum {
    EnumWithGrpcNameValues using_enum = 1;
    sint32 using_enum_raw = 2;
  }
}

message MethodUsingEnumWithGrpcNameValuesResponse {
  int32 status = 1;
}

message MethodWithGetLastErrorParamRequest {
}

message MethodWithGetLastErrorParamResponse {
  int32 status = 1;
  string last_error = 2 [deprecated = true];
}

message MethodWithGrpcOnlyParamRequest {
  sint32 simple_param = 1;
}

message MethodWithGrpcOnlyParamResponse {
  int32 status = 1;
  sint32 grpc_only_param = 2;
}

message MethodUsingWholeAndFractionalNumbersRequest {
}

message MethodUsingWholeAndFractionalNumbersResponse {
  int32 status = 1;
  DecimalWholeNumber whole_number = 2;
  sint32 whole_number_raw = 3;
  DecimalMixedNumber fractional_number_mapped = 4;
  double fractional_number_raw = 5;
}

message MethodUsingWholeMappedNumbersRequest {
}

message MethodUsingWholeMappedNumbersResponse {
  int32 status = 1;
  DecimalWholeNumberMapped whole_number_mapped = 2;
  double whole_number_raw = 3;
}

message MethodWithGrpcFieldNumberRequest {
  sint32 attribute_value = 5;
}

message MethodWithGrpcFieldNumberResponse {
  int32 status = 1;
}

message MethodWithProtoOnlyParameterRequest {
  sint32 attribute_value = 1;
}

message MethodWithProtoOnlyParameterResponse {
  int32 status = 1;
}

message ReadDataWithInOutIviTwistRequest {
}

message ReadDataWithInOutIviTwistResponse {
  int32 status = 1;
  repeated sint32 data = 2;
  sint32 buffer_size = 3;
}

message ReadDataWithMultipleIviTwistParamSetsRequest {
}

message ReadDataWithMultipleIviTwistParamSetsResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
  repeated sint32 other_array_out = 4;
  sint32 other_actual_size = 5;
}

message InitExtCalRequest {
  string session_name = 1;
  string resource_name = 2;
  string calibration_password = 3;
}

message InitExtCalResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
}

message InitWithVarArgsRequest {
  string session_name = 1;
  string resource_name = 2;
  repeated StringAndTurtle name_and_turtle = 3;
}

message InitWithVarArgsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
}

message MultipleArraysSameSizeWithOptionalRequest {
  nidevice_grpc.Session vi = 1;
  repeated double values1 = 2;
  repeated double values2 = 3;
  repeated double values3 = 4;
  repeated double values4 = 5;
  repeated FakeCustomStruct values5 = 6;
}

message MultipleArraysSameSizeWithOptionalResponse {
  int32 status = 1;
}

message UseATwoDimensionParameterRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 array = 2;
  repeated sint32 array_lengths = 3;
}

message UseATwoDimensionParameterResponse {
  int32 status = 1;
}

message ViUInt8ArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
  bytes an_array = 3;
}

message ViUInt8ArrayInputFunctionResponse {
  int32 status = 1;
}

message ViUInt8ArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message ViUInt8ArrayOutputFunctionResponse {
  int32 status = 1;
  bytes an_array = 2;
}

message ViInt16ArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 an_array = 2;
}

message ViInt16ArrayInputFunctionResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/nifake.mak sha256=80832b84362bbd50a78bdea2cd20a12b1658c0d11a63b001e9ec358e6b4a066c bytes=485 -->
## FILE: src/nifake/nifake.mak

- repository: `ni/nimi-python`
- source_path: `src/nifake/nifake.mak`
- sha256: `80832b84362bbd50a78bdea2cd20a12b1658c0d11a63b001e9ec358e6b4a066c`
- bytes: 485

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE) _complextype.py

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

# We are not building any nifake documentation
# RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)
# SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)

CUSTOM_TYPES_TO_COPY += \
    custom_struct.py \
    custom_struct_typedef.py \
    custom_struct_nested_typedef.py \

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/unit_tests/test_converters.py sha256=51960a6e9bda494a06bdc5a6e01d947bad9b2366139564cb7d5679afd7fb6f64 bytes=22272 -->
## FILE: src/nifake/unit_tests/test_converters.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/unit_tests/test_converters.py`
- sha256: `51960a6e9bda494a06bdc5a6e01d947bad9b2366139564cb7d5679afd7fb6f64`
- bytes: 22272

````python
import nifake._converters as _converters
import nifake.errors as errors

import hightime
import pytest


def test_convert_init_with_options_dictionary():
    assert _converters.convert_init_with_options_dictionary('') == ''
    assert _converters.convert_init_with_options_dictionary('Simulate=1') == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, }) == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': False, }) == 'Simulate=0'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(seconds=10))
    assert test_result == 10.0
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(nanoseconds=-0.5))
    assert test_result == pytest.approx(-5e-10)
    test_result = _converters.convert_timedelta_to_seconds_real64(10.5)
    assert test_result == 10.5
    test_result = _converters.convert_timedelta_to_seconds_real64(-1)
    assert test_result == -1


def test_convert_timedelta_to_milliseconds_int32():
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=10))
    assert test_result == 10000
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=-5))
    assert test_result == -5000
    test_result = _converters.convert_timedelta_to_milliseconds_int32(10.5)
    assert test_result == 10500
    test_result = _converters.convert_timedelta_to_milliseconds_int32(-1)
    assert test_result == -1000


def test_convert_timedeltas_to_seconds_real64():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_timedeltas_to_seconds_real64(time_values)
    assert all([actual == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    test_input = [hightime.timedelta(seconds=10.5), hightime.timedelta(nanoseconds=-0.5)]
    test_result = _converters.convert_timedeltas_to_seconds_real64(test_input)
    assert all([actual == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])


def test_convert_timedelta_to_months_int32():
    # 1 month = 60*60*24*30.4167 seconds = 2628002.88 seconds
    seconds_per_month = 60 * 60 * 24 * 30.4167
    test_result = _converters.convert_timedelta_to_months_int32(hightime.timedelta(seconds=seconds_per_month))
    assert test_result == 1
    test_result = _converters.convert_timedelta_to_months_int32(hightime.timedelta(seconds=-5 * seconds_per_month))
    assert test_result == -5
    test_result = _converters.convert_timedelta_to_months_int32(seconds_per_month * 2)
    assert test_result == 2
    test_result = _converters.convert_timedelta_to_months_int32(-seconds_per_month)
    assert test_result == -1


def test_convert_seconds_real64_to_timedelta():
    time_value = -5e-10
    test_result = _converters.convert_seconds_real64_to_timedelta(time_value)
    assert test_result.total_seconds() == pytest.approx(time_value)
    assert isinstance(test_result, hightime.timedelta)


def test_convert_seconds_real64_to_timedeltas():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_seconds_real64_to_timedeltas(time_values)
    assert all([actual.total_seconds() == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(x, hightime.timedelta) for x in test_result])


# Tests - repeated capabilities
def test_repeated_capabilities_string_channel():
    test_result_list = _converters.convert_repeated_capabilities('0')
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities('r0')
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities('0,1')
    assert test_result_list == ['0', '1']


def test_repeated_capabilities_string_prefix():
    test_result_list = _converters.convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']


def test_repeated_capabilities_list_channel():
    test_result_list = _converters.convert_repeated_capabilities(['0'])
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(['r0'])
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1, '3'])
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilities_list_prefix():
    test_result_list = _converters.convert_repeated_capabilities(['ScriptTrigger0', 'ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_tuple_channel():
    test_result_list = _converters.convert_repeated_capabilities(('0'))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(('0,1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1, '3'))
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilities_tuple_prefix():
    test_result_list = _converters.convert_repeated_capabilities(('ScriptTrigger0,ScriptTrigger1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(('0'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_unicode():
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_raw():
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_slice_channel():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2))
    assert test_result_list == ['0', '1']


def test_repeated_capabilities_mixed_channel():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'])
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']


def test_repeated_capabilities_mixed_prefix():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']


def test_invalid_repeated_capabilities():
    try:
        _converters.convert_repeated_capabilities('6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(['5', '6-8-10'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(('5', '6-8-10'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities('5,6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(5.0)
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities([5.0, '0'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities((5.0, '0'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass


def test_repeated_capabilities_slice_prefix():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_without_prefix():
    test_result = _converters.convert_repeated_capabilities_without_prefix((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result == '0,2,4,5,6,7,8,9,11,12,13,14,16,17'


def test_repeated_capabilities_string_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1')
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1,Dev2')
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1/0')
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1/0:1, Dev2/0-1')
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1, Dev2/0-2')
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_list_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1'])
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', 'Dev2'])
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1/0'])
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1/0:1', 'Dev2/0-1'])
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', 'Dev2/0-2'])
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_tuple_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1'))
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1', 'Dev2'))
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1/0'))
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1/0:1', 'Dev2/0-1'))
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1', 'Dev2/0-2'))
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_mixed_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', ('Dev2/0', 'Dev2/1'), ['Dev3/0:1', 'Dev4/1:2'], 'Dev5/1'])
    assert test_result_list == 'Dev1,Dev2/0,Dev2/1,Dev3/0:1,Dev4/1:2,Dev5/1'


def test_repeated_capabilities_invalid_resource_names():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('/')
    assert test_result_list == '/'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev/')
    assert test_result_list == 'Dev/'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev,')
    assert test_result_list == 'Dev,'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev/1/1,')
    assert test_result_list == 'Dev/1/1,'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('0/1:2,')
    assert test_result_list == '0/1:2,'


def test_expand_channel_string_non_fully_qualified_channel_names():
    test_result_list = _converters.expand_channel_string('1', ['0', '1', '2', '3'])
    assert test_result_list == ['1']
    test_result_list = _converters.expand_channel_string('0-2', ['0', '1', '2', '3'])
    assert test_result_list == ['0', '1', '2']
    test_result_list = _converters.expand_channel_string('0:2', ['0', '1', '2', '3'])
    assert test_result_list == ['0', '1', '2']
    test_result_list = _converters.expand_channel_string('0:2,4', ['0', '1', '2', '3', '4', '5'])
    assert test_result_list == ['0', '1', '2', '4']
    test_result_list = _converters.expand_channel_string('4,1:2', ['1', '2', '4'])
    assert test_result_list == ['4', '1', '2']
    test_result_list = _converters.expand_channel_string(' 1 : 2 , 4 ', ['1', '2', '4'])
    assert test_result_list == ['1', '2', '4']


def test_expand_channel_string_fully_qualified_channel_names():
    test_result_list = _converters.expand_channel_string(
        '2:3,0',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/2', 'Dev1/3', 'Dev1/0']
    test_result_list = _converters.expand_channel_string(
        'Dev1/1',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/1']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0-2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0:2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0:2,4',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/4']
    test_result_list = _converters.expand_channel_string(
        '4,Dev1/1:2',
        ['Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/4', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/4,Dev1/2,Dev1/3',
        ['Dev1/2', 'Dev1/3', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/4', 'Dev1/2', 'Dev1/3']
    test_result_list = _converters.expand_channel_string(
        'Dev1/1,Dev2/2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3']
    )
    assert test_result_list == ['Dev1/1', 'Dev2/2']
    test_result_list = _converters.expand_channel_string(
        ' Dev1 / 1 : 2 , 4 ',
        ['Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/1', 'Dev1/2', 'Dev1/4']
    test_result_list = _converters.expand_channel_string(
        'DEV1/0-1    , Dev1/3',
        ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3']
    )
    assert test_result_list == ['dev1/0', 'dev1/1', 'dev1/3']


def test_convert_chained_repeated_capability_to_parts_three_parts():
    chained_rep_cap = ('site0/test/PinA,site0/test/PinB,site0/test/PinC,'
                       'site1/test/PinA,site1/test/PinB,site1/test/PinC')
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts(chained_rep_cap)
    assert rep_cap_list == ['site0,site1', 'test', 'PinA,PinB,PinC']


def test_convert_chained_repeated_capability_to_parts_single_part():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('site0, site1')
    assert rep_cap_list == ['site0,site1']


def test_convert_chained_repeated_capability_to_parts_empty_string():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('')
    assert rep_cap_list == ['']


def test_string_to_list_channel():
    test_result = _converters._convert_repeated_capabilities('r0', '')
    assert test_result == ['r0']
    test_result = _converters._convert_repeated_capabilities(['0-2'], '')
    assert test_result == ['0', '1', '2']
    test_result = _converters._convert_repeated_capabilities(['3:7'], '')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['2-0'], '')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['2:0'], '')
    assert test_result == ['2', '1', '0']


def test_string_to_list_prefix():
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3-ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3:ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2-ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2:ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']


def test_convert_comma_separated_string_to_list():
    out_list = _converters.convert_comma_separated_string_to_list(' PinA ,  PinB , PinC  ')
    assert out_list == ['PinA', 'PinB', 'PinC']


def test_convert_list_to_comma_separated_string():
    out_string = _converters.convert_list_to_comma_separated_string(['PinA', 'PinB', 'PinC'])
    assert out_string == 'PinA,PinB,PinC'


def test_convert_list_to_comma_separated_string_invalid_input():
    with pytest.raises(TypeError) as error_info:
        _converters.convert_list_to_comma_separated_string('PinA,PinB,PinC')
    assert str(error_info.value) == 'Input must be a list or tuple of str'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/unit_tests/test_grpc.py sha256=0052a2984291996f78a37bdb936492ba4b4d3b28f2a38b6ba0ffbdf3340a7677 bytes=55634 -->
## FILE: src/nifake/unit_tests/test_grpc.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/unit_tests/test_grpc.py`
- sha256: `0052a2984291996f78a37bdb936492ba4b4d3b28f2a38b6ba0ffbdf3340a7677`
- bytes: 55634

````python
import array
import collections
import grpc
import math
import nifake
import nifake.errors
import numpy
import pytest
import session_pb2
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

GRPC_SESSION_OBJECT_FOR_TEST = session_pb2.Session(name="TestSession", id=42)


Metadatum = collections.namedtuple('Metadatum', ('key', 'value'))


class MyRpcError(grpc.RpcError):
    def __init__(self, error_code, error_message, grpc_error=grpc.StatusCode.UNKNOWN):
        super().__init__()
        self._grpc_error = grpc_error
        self._error_code = error_code
        self._error_message = error_message

    def code(self):
        return self._grpc_error

    def details(self):
        return self._error_message

    def trailing_metadata(self):
        if self._error_code is None:
            return []
        else:
            return [Metadatum('ni-error', str(self._error_code))]


class TestGrpcStubInterpreter:

    class PatchedGrpcTypes:
        def __init__(self):
            for f in dir(nifake._grpc_stub_interpreter.grpc_types):
                if f.endswith('Request'):
                    real_func = getattr(nifake._grpc_stub_interpreter.grpc_types, f)
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=real_func, side_effect=error_func))
                else:
                    setattr(self, f, getattr(nifake._grpc_stub_interpreter.grpc_types, f))

    class PatchedGrpcStub(nifake._grpc_stub_interpreter.nifake_grpc.NiFakeServicer):
        def _sample_func(self, request, metadata=None):
            pass

        def __init__(self):
            for f in dir(self):
                if not f.startswith('_') and f not in {'get_session_handle', 'set_session_handle'}:
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=self._sample_func, side_effect=error_func))

        def __call__(self, grpc_channel):
            self._grpc_channel = grpc_channel
            return self

    def setup_method(self, method):
        self.patched_grpc_types = self.PatchedGrpcTypes()
        self.patched_grpc_stub = self.PatchedGrpcStub()
        self.real_grpc_types = nifake._grpc_stub_interpreter.grpc_types
        self.grpc_types_patch = patch('nifake._grpc_stub_interpreter.grpc_types', self.patched_grpc_types)
        self.grpc_stub_patch = patch('nifake._grpc_stub_interpreter.nifake_grpc.NiFakeStub', side_effect=self.patched_grpc_stub)
        self.grpc_types_patch.start()
        self.grpc_stub_patch.start()

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.grpc_stub_patch.stop()
        self.grpc_types_patch.stop()

    def _get_initialized_stub_interpreter(self, grpc_channel=object()):
        session_options = nifake.GrpcSessionOptions(grpc_channel, '', initialization_behavior=nifake.SessionInitializationBehavior.AUTO)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(session_options)
        assert interpreter._client is self.patched_grpc_stub
        assert interpreter.get_session_handle().id == 0
        assert interpreter.get_session_handle().name == ""
        assert self.patched_grpc_stub._grpc_channel is grpc_channel
        interpreter.set_session_handle(GRPC_SESSION_OBJECT_FOR_TEST)
        return interpreter

    def _check_fields(self, response_class, **kwargs):
        fields = dict(kwargs)
        response_fields = {x.name: x for x in response_class.DESCRIPTOR.fields}

        unexpected_fields = set(fields) - set(response_fields)
        assert not unexpected_fields, 'Unexpected fields: ' + str(list(sorted(unexpected_fields)))

        for f in response_fields:
            if f.endswith('_raw') and f[:-4] in response_fields:
                fields.setdefault(f, fields[f[:-4]])
                fields.setdefault(f[:-4], fields[f])

        missing_fields = set(response_fields) - set(fields)
        assert not missing_fields, 'Missing fields: ' + str(list(sorted(missing_fields)))

        for field, value in fields.items():
            rf = response_fields[field]
            field_type = rf.type
            if field_type == rf.TYPE_ENUM:
                if (field + '_raw') not in fields:
                    assert field.endswith('_mapped')
                    raw_field = field.rpartition('_mapped')[0] + '_raw'
                    assert raw_field in fields
                    assert kwargs.get(raw_field)
                    if rf.label == rf.LABEL_REPEATED:
                        assert len(kwargs[raw_field]) == len(value)
                expected_py_type = int
            elif field_type == rf.TYPE_BOOL:
                expected_py_type = bool
            elif field_type == rf.TYPE_STRING:
                expected_py_type = str
            elif field_type == rf.TYPE_BYTES:
                expected_py_type = bytes
            elif field_type in {rf.TYPE_DOUBLE, rf.TYPE_FLOAT}:
                expected_py_type = float
            elif field_type in {rf.TYPE_INT32, rf.TYPE_INT64, rf.TYPE_FIXED64, rf.TYPE_FIXED32}:
                expected_py_type = int
            elif field_type in {rf.TYPE_UINT32, rf.TYPE_UINT64}:
                expected_py_type = int
            elif field_type in {rf.TYPE_SINT32, rf.TYPE_SINT64, rf.TYPE_SFIXED32, rf.TYPE_SFIXED64}:
                expected_py_type = int
            elif field_type == rf.TYPE_MESSAGE:
                expected_py_type = object
            elif field_type == rf.TYPE_GROUP:
                assert False, 'GROUP types not yet supported here'
            else:
                assert False, f'Unknown type {field_type}'

            if rf.label == rf.LABEL_REPEATED:
                for x in value:
                    assert isinstance(x, expected_py_type)
            else:
                assert isinstance(value, expected_py_type), (field, field_type)

        return fields

    def _set_side_effect(self, function_name, side_effect=None, **kwargs):
        if side_effect is None:
            kwargs.setdefault('status', 0)
            response_class = getattr(self.real_grpc_types, function_name + 'Response')
            kwargs = self._check_fields(response_class, **kwargs)
            side_effect = [response_class(**kwargs)]
        else:
            assert not kwargs, 'Do not use both side_effect and kwargs'

        request_object = object()
        getattr(self.patched_grpc_types, function_name + 'Request').side_effect = [request_object]
        getattr(self.patched_grpc_stub, function_name).side_effect = side_effect
        return request_object

    def _assert_call(self, function_name, request_object, metadata=None):
        func = getattr(self.patched_grpc_stub, function_name)
        func.assert_called_once_with(request_object, metadata=metadata)
        return getattr(self.patched_grpc_types, function_name + 'Request')

    # gRPC errors

    def test_server_unavailable(self):
        library_func = 'InitWithOptions'
        grpc_error = grpc.StatusCode.UNAVAILABLE
        expected_error_message = 'Failed to connect to server'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, '', grpc_error=grpc_error))
        grpc_options = nifake.GrpcSessionOptions(object(), '', initialization_behavior=nifake.SessionInitializationBehavior.AUTO)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == expected_error_message
            assert str(e) == f'StatusCode.UNAVAILABLE: {expected_error_message}'

    def test_function_not_implemented(self):
        library_func = 'PoorlyNamedSimpleFunction'
        grpc_error = grpc.StatusCode.UNIMPLEMENTED
        expected_error_message_intro = 'This operation is not supported'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, '', grpc_error=grpc_error))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description.startswith(expected_error_message_intro)
            assert str(e).startswith(f'StatusCode.UNIMPLEMENTED: {expected_error_message_intro}')

    # Methods

    def test_api_key_sent_to_init(self):
        library_func = 'InitWithOptions'
        expected_metadata = (('ni-api-key', nifake.MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY),)
        from session_pb2 import Session as GrpcSession
        grpc_session_object = GrpcSession(id=42, name='')
        response_object = self._set_side_effect(library_func, new_session_initialized=True, vi=grpc_session_object)
        init_behavior = nifake.SessionInitializationBehavior.AUTO
        grpc_options = nifake.GrpcSessionOptions(object(), '', initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        interpreter.init_with_options('dev1', False, False, '')
        self._assert_call(library_func, response_object, metadata=expected_metadata).assert_called_once_with(
            resource_name='dev1', id_query=False, reset_device=False, option_string='', session_name='', initialization_behavior=init_behavior,
        )

    def test_new_session_already_exists(self):
        library_func = 'InitWithOptions'
        session_name = 'existing_session'
        error_message = "Cannot initialize '" + session_name + "' when a session already exists."
        grpc_error = grpc.StatusCode.ALREADY_EXISTS
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.ALREADY_EXISTS: {error_message}'

    def test_attach_to_non_existent_session(self):
        library_func = 'InitWithOptions'
        session_name = 'non_existent_session'
        error_message = "Cannot attach to '" + session_name + "' because a session has not been initialized."
        grpc_error = grpc.StatusCode.FAILED_PRECONDITION
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.FAILED_PRECONDITION: {error_message}'

    @pytest.mark.timeout(2)
    def test_lock_unlock(self):
        # Note: this is purely local; don't set up any grpc mocks
        interpreter = self._get_initialized_stub_interpreter()
        interpreter.lock()
        interpreter.lock()  # ensure recurive locking is allowed
        interpreter.unlock()
        interpreter.unlock()

    def test_simple_function(self):
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.simple_function() is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_number(self):
        library_func = 'GetANumber'
        test_number = 16
        response_object = self._set_side_effect(library_func, a_number=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_one_input_function(self):
        library_func = 'OneInputFunction'
        test_number = 1
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.one_input_function(test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number
        )

    def test_vi_int_64_function(self):
        library_func = 'Use64BitNumber'
        input_value = 2 ** 40
        output_value = 2 ** 41
        response_object = self._set_side_effect(library_func, output=output_value)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, input=input_value
        )

    def test_two_input_function(self):
        library_func = 'TwoInputFunction'
        test_number = 1.5
        test_string = 'test'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.two_input_function(test_number, test_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number, a_string=test_string
        )

    def test_get_enum_value(self):
        library_func = 'GetEnumValue'
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        response_object = self._set_side_effect(library_func, a_quantity=test_number, a_turtle=test_turtle.value)
        interpreter = self._get_initialized_stub_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_enums(self):
        library_func = 'EnumArrayOutputFunction'
        test_list = [1, 1, 0]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_get_a_boolean(self):
        library_func = 'GetABoolean'
        response_object = self._set_side_effect(library_func, a_boolean=True)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.get_a_boolean()
        assert test_result is True
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_booleans(self):
        library_func = 'BoolArrayOutputFunction'
        test_list = [True, True, False]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert actual_value is expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_single_point_read_nan(self):
        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        response_object = self._set_side_effect(library_func, reading=test_reading)
        interpreter = self._get_initialized_stub_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )

    def test_fetch_waveform(self):
        library_func = 'FetchWaveform'
        expected_waveform_list = [1.0, 0.1, 42.0, 0.42]
        response_object = self._set_side_effect(library_func, waveform_data=expected_waveform_list, actual_number_of_samples=len(expected_waveform_list))
        interpreter = self._get_initialized_stub_interpreter()
        actual_waveform = interpreter.fetch_waveform(len(expected_waveform_list))
        assert isinstance(actual_waveform[0], float)
        assert len(actual_waveform) == len(expected_waveform_list)
        for i in range(len(actual_waveform)):
            assert actual_waveform[i] == expected_waveform_list[i]
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_samples=len(expected_waveform_list)
        )

    def test_fetch_waveform_into(self):
        interpreter = self._get_initialized_stub_interpreter()
        waveform = numpy.empty(4, numpy.float64)
        try:
            interpreter.fetch_waveform_into(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_write_waveform(self):
        library_func = 'WriteWaveform'
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self._get_initialized_stub_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.write_waveform(expected_array) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, waveform=expected_array
        )

    def test_write_waveform_numpy(self):
        waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.write_waveform_numpy(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_write_waveform_numpy_complex128(self):
        library_func = 'WriteWaveformNumpyComplex128'
        waveform = numpy.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=numpy.complex128)
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumber(real=value.real, imaginary=value.imag)
            for value in waveform.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex128(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_write_waveform_numpy_complex64(self):
        library_func = 'WriteWaveformNumpyComplex64'
        waveform = numpy.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=numpy.complex64)
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumberF32(real=value.real, imaginary=value.imag)
            for value in waveform.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex64(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_write_waveform_numpy_complex_interleaved_i16(self):
        library_func = 'WriteWaveformNumpyComplexInterleavedI16'
        waveform = numpy.array([32767, 0, 123, -456], dtype=numpy.int16)
        assert len(waveform) % 2 == 0
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexI16(real=waveform[i], imaginary=waveform[i + 1])
            for i in range(0, len(waveform), 2)
        ]
        assert len(grpc_waveform) == len(waveform) // 2
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex_interleaved_i16(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self):
        library_func = 'FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter'
        array_3d = numpy.array(
            [[[1.0 + 2.0j, 3.0 + 4.0j], [5.0 + 6.0j, 7.0 + 8.0j]], [[9.0 + 10.0j, 11.0 + 12.0j], [13.0 + 14.0j, 15.0 + 16.0j]]],
            dtype=numpy.complex128,
        )
        grpc_array = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumber(real=value.real, imaginary=value.imag)
            for value in array_3d.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d) is None
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            multidimensional_array=grpc_array,
        )

    def test_return_multiple_types(self):
        library_func = 'ReturnMultipleTypes'
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        expected_enum_val = nifake.Turtle.LEONARDO
        enum_val = nifake._grpc_stub_interpreter.grpc_types.Turtle.TURTLE_LEONARDO
        float_val = 1.23
        expected_float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        float_enum_val = nifake._grpc_stub_interpreter.grpc_types.FloatEnum.FLOAT_ENUM_SIX_POINT_FIVE
        raw_float_enum_val = 6.5
        array_val = [0.0, 1.0, 2.0]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(
            library_func,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum=enum_val,
            a_float=float_val,
            a_float_enum_mapped=float_enum_val,
            a_float_enum_raw=raw_float_enum_val,
            an_array=array_val,
            a_string=string_val,
        )
        interpreter = self._get_initialized_stub_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
        assert result_boolean == boolean_val
        assert isinstance(result_boolean, bool)
        assert result_int32 == int32_val
        assert isinstance(result_int32, int)
        assert result_int64 == int64_val
        assert isinstance(result_int64, int)
        assert result_enum == expected_enum_val
        assert isinstance(result_enum, nifake.Turtle)
        assert result_float == float_val
        assert isinstance(result_float, float)
        assert result_float_enum == expected_float_enum_val
        assert isinstance(result_float_enum, nifake.FloatEnum)
        assert result_array == array_val
        # assert `list` duck typing (in reality, it's a google._upb._message.RepeatedScalarContainer
        assert isinstance(result_array, collections.abc.Sequence)
        assert isinstance(result_array[0], float)
        assert result_string == string_val
        assert isinstance(result_string, str)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, array_size=array_size
        )

    def test_multiple_array_types(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_stub_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=input_array_of_integers,
        )

    def test_multiple_array_types_none_input(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_stub_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=None,
        )

    def test_multiple_arrays_same_size(self):
        library_func = 'MultipleArraysSameSize'
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=input_array_of_floats2,
            values3=input_array_of_floats3,
            values4=input_array_of_floats4,
        )

    def test_multiple_arrays_same_size_none_input(self):
        library_func = 'MultipleArraysSameSize'
        response_object = self._set_side_effect(library_func)
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=None,
            values3=None,
            values4=None,
        )

    def test_multiple_arrays_different_size(self):
        library_func = 'MultipleArraysDifferentSize'
        response_object = self._set_side_effect(library_func)
        values_array = [1.1, 2.2, 3.3]
        data_array = [10, 20, 30, 40, 50]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_different_size(values_array, data_array) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values_array=values_array,
            data_array=data_array,
        )

    def test_multiple_arrays_different_size_none_input(self):
        library_func = 'MultipleArraysDifferentSize'
        response_object = self._set_side_effect(library_func)
        values_array = [1.1, 2.2, 3.3]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_different_size(values_array, None) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values_array=values_array,
            data_array=None,
        )

    def test_mixed_ivi_dance_and_len_mechanism(self):
        library_func = 'MixedIviDanceAndLenMechanism'
        input_values = [1.1, 2.2, 3.3]
        expected_output = [4, 5]
        response_object = self._set_side_effect(library_func, output_array=expected_output)
        interpreter = self._get_initialized_stub_interpreter()
        result_array = interpreter.mixed_ivi_dance_and_len_mechanism(input_values)
        assert result_array == expected_output
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            input_values=input_values,
        )

    def test_multiple_arrays_same_size_wrong_size(self):
        library_func = 'MultipleArraysSameSize'
        # grpc-device server checks this server-side and errors with ::grpc::INVALID_ARGUMENT
        self._set_side_effect(library_func, side_effect=MyRpcError(
            None,
            'The sizes of linked repeated fields [values1, values2, values3, values4] do not match',
            grpc_error=grpc.StatusCode.INVALID_ARGUMENT,
        ))
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
            assert False
        except ValueError:
            pass

    def test_parameters_are_multiple_types(self):
        library_func = 'ParametersAreMultipleTypes'
        response_object = self._set_side_effect(library_func)
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum_raw=enum_val.value,
            a_float=float_val,
            a_float_enum_raw=float_enum_val.value,
            a_string=string_val,
        )

    def test_method_with_error(self):
        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = -42
        test_error_desc = 'The answer to the ultimate question'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.simple_function() is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_array_types(10) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2]) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code, reading=test_reading)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        library_func = 'GetAStringOfFixedMaximumSize'
        test_string = 'A string no larger than the max size of 256 allowed by the function.'
        response_object = self._set_side_effect(library_func, a_string=test_string)
        interpreter = self._get_initialized_stub_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_return_a_number_and_a_string(self):
        library_func = 'ReturnANumberAndAString'
        test_string = 'this string'
        test_number = 13
        response_object = self._set_side_effect(library_func, a_string=test_string, a_number=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert returned_string == test_string
        assert returned_number == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_an_ivi_dance_char_array(self):
        library_func = 'GetAnIviDanceCharArray'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, char_array=string_val)
        interpreter = self._get_initialized_stub_interpreter()
        result_string = interpreter.get_an_ivi_dance_char_array()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_string_ivi_dance_error(self):
        library_func = 'GetAttributeViString'
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = 'ascending order'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.get_attribute_vi_string('', read_write_string_attribute_id) is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        library_func = 'GetAnIviDanceWithATwistString'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, a_string=string_val, actual_size=len(string_val))
        interpreter = self._get_initialized_stub_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_array_using_ivi_dance(self):
        library_func = 'GetArrayUsingIviDance'
        response_object = self._set_side_effect(library_func, array_out=[1.1, 2.2])
        interpreter = self._get_initialized_stub_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    # Attributes

    def test_get_attribute_int32(self):
        library_func = 'GetAttributeViInt32'
        attribute_id = 1000004
        test_number = 3
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert attr_int == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int32(self):
        library_func = 'SetAttributeViInt32'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000004
        test_number = -10
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_int32('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_real64(self):
        library_func = 'GetAttributeViReal64'
        attribute_id = 1000001
        test_number = 1.5
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_real64(self):
        library_func = 'SetAttributeViReal64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_real64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_string(self):
        library_func = 'GetAttributeViString'
        attribute_id = 1000002
        string = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, attribute_value=string)
        interpreter = self._get_initialized_stub_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_string(self):
        library_func = 'SetAttributeViString'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_string('', attribute_id, attrib_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw='This is test string',
        )

    def test_get_attribute_boolean(self):
        library_func = 'GetAttributeViBoolean'
        attribute_id = 1000000
        response_object = self._set_side_effect(library_func, attribute_value=True)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_boolean(self):
        library_func = 'SetAttributeViBoolean'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id, attribute_value=True
        )

    def test_get_attribute_int64(self):
        library_func = 'GetAttributeViInt64'
        attribute_id = 1000006
        test_number = 6000000000
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert attr_int == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int64(self):
        library_func = 'SetAttributeViInt64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_int64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    # Error descriptions

    def test_error_message_returns_error(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        test_error_code = 42
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_msg_response_object = self._set_side_effect('ErrorMessage', side_effect=MyRpcError(-3, 'ErrorMessage failed'))
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert 'Failed to retrieve error description.' in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_msg_response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code)

    # Custom types

    def test_set_custom_type(self):
        library_func = 'SetCustomType'
        response_object = self._set_side_effect(library_func)
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_custom_type(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type(self):
        library_func = 'GetCustomType'
        expected_cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_stub_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == expected_cs.struct_int
        assert cs.struct_double == expected_cs.struct_double
        assert isinstance(cs, type(expected_cs))
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_set_custom_type_array(self):
        library_func = 'SetCustomTypeArray'
        response_object = self._set_side_effect(library_func)
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_custom_type_array(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type_array(self):
        library_func = 'GetCustomTypeArray'
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_stub_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs))
        assert len(cs_test) == len(cs)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double
            assert isinstance(actual, type(expected))
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(cs)
        )

    def test_get_custom_type_typedef(self):
        library_func = 'CustomNestedStructRoundtrip'
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        grpc_csnt = nifake._grpc_stub_interpreter.grpc_types.CustomStructNestedTypedef(
            struct_custom_struct=nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake._grpc_stub_interpreter.grpc_types.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        response_object = self._set_side_effect(library_func, nested_custom_type_out=grpc_csnt)
        interpreter = self._get_initialized_stub_interpreter()
        csnt_test = interpreter.custom_nested_struct_roundtrip(nested_custom_type_in=csnt)
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double
        assert isinstance(csnt_test.struct_custom_struct, type(csnt.struct_custom_struct))
        assert isinstance(csnt_test.struct_custom_struct_typedef, type(csnt.struct_custom_struct_typedef))
        assert isinstance(csnt_test, type(csnt))
        request_object = self._assert_call(library_func, response_object)
        request_object.assert_called_once()
        call = request_object.call_args_list[0]
        assert len(call) == 2
        call_args, call_kwargs = call
        assert not call_args
        assert 'nested_custom_type_in' in call_kwargs
        sent_csnt = call_kwargs['nested_custom_type_in']
        assert sent_csnt.struct_custom_struct.struct_int == grpc_csnt.struct_custom_struct.struct_int
        assert sent_csnt.struct_custom_struct.struct_double == grpc_csnt.struct_custom_struct.struct_double
        assert sent_csnt.struct_custom_struct_typedef.struct_int == grpc_csnt.struct_custom_struct_typedef.struct_int
        assert sent_csnt.struct_custom_struct_typedef.struct_double == grpc_csnt.struct_custom_struct_typedef.struct_double
        assert isinstance(sent_csnt.struct_custom_struct, type(grpc_csnt.struct_custom_struct))
        assert isinstance(sent_csnt.struct_custom_struct_typedef, type(grpc_csnt.struct_custom_struct_typedef))
        assert isinstance(sent_csnt, type(grpc_csnt))

    def test_get_cal_date_time(self):
        library_func = 'GetCalDateAndTime'
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        response_object = self._set_side_effect(
            library_func, month=month, day=day, year=year, hour=hour, minute=minute
        )
        interpreter = self._get_initialized_stub_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cal_type=0
        )

    # Import/Export functions

    def test_import_attribute_configuration_buffer(self):
        library_func = 'ImportAttributeConfigurationBuffer'
        configuration = b'abcd'
        interpreter = self._get_initialized_stub_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.import_attribute_configuration_buffer(configuration) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, configuration=configuration
        )

    def test_missing_function(self):
        library_func = 'Abort'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, 'not found', grpc_error=grpc.StatusCode.NOT_FOUND))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.abort()
            assert False
        except nifake.errors.DriverTooOldError as e:
            message = e.args[0]
            assert message == 'A function was not found in the NI-FAKE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/unit_tests/test_library_interpreter.py sha256=a4286dfd1f62fd504566c117bc95f8b60c3a994c92c414b169ca76ae85b9f332 bytes=67532 -->
## FILE: src/nifake/unit_tests/test_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/unit_tests/test_library_interpreter.py`
- sha256: `a4286dfd1f62fd504566c117bc95f8b60c3a994c92c414b169ca76ae85b9f332`
- bytes: 67532

````python
import array
import ctypes
import math
import nifake
import nifake.errors
import numpy
import pytest
import warnings

from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import _matchers
import _mock_helper

SESSION_NUM_FOR_TEST = 42


class TestLibraryInterpreter:

    class PatchedLibrary(nifake._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niFake_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nifake._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niFake_SetRuntimeEnvironment.side_effect = self.side_effects_helper.niFake_SetRuntimeEnvironment

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    def get_initialized_library_interpreter(self):
        interpreter = nifake._library_interpreter.LibraryInterpreter('windows-1251')
        interpreter._vi = SESSION_NUM_FOR_TEST
        return interpreter

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None):
        ret_val = self.get_ctypes_pointer_for_buffer_side_effect_items[self.get_ctypes_pointer_for_buffer_side_effect_count]
        self.get_ctypes_pointer_for_buffer_side_effect_count += 1
        return ret_val

    # Methods

    def test_simple_function(self):
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.simple_function()
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self.patched_library.niFake_GetANumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.one_input_function(test_number)
        self.patched_library.niFake_OneInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 2 ** 40
        output_value = 2 ** 41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self.patched_library.niFake_Use64BitNumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt64Matcher(input_value), _matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.two_input_function(test_number, test_string)
        self.patched_library.niFake_TwoInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_number), _matchers.ViStringMatcher(test_string))

    def test_get_enum_value(self):
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        self.patched_library.niFake_GetEnumValue.side_effect = self.side_effects_helper.niFake_GetEnumValue
        self.side_effects_helper['GetEnumValue']['aQuantity'] = test_number
        self.side_effects_helper['GetEnumValue']['aTurtle'] = 0
        interpreter = self.get_initialized_library_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self.patched_library.niFake_GetEnumValue.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32PointerMatcher(), _matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViInt16BufferMatcher(len(test_list)))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_boolean()
        assert isinstance(test_result, bool)
        assert test_result
        self.patched_library.niFake_GetABoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, bool)
            assert actual_value == bool(expected_value)
        self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViBooleanBufferMatcher(len(test_list)))

    def test_single_point_read_nan(self):
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        interpreter = self.get_initialized_library_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))

    def test_fetch_waveform(self):
        expected_waveform_list = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform_list
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform_list)

        # Because we are mocking _get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_waveform = array.array('d', [0]) * len(expected_waveform_list)
        expected_waveform_ctypes = ctypes.cast(expected_waveform.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViReal64 * len(expected_waveform_list)))

        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform_ctypes]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            # Because we have mocked away _get_ctypes_pointer_for_buffer(), we ignore the return values here and look at our already allocated arrays to make
            # sure they are filled in correctly
            interpreter.fetch_waveform(len(expected_waveform_list))
        assert isinstance(expected_waveform[0], float)
        assert len(expected_waveform) == len(expected_waveform_list)
        for i in range(len(expected_waveform)):
            assert expected_waveform[i] == expected_waveform_list[i]
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_fetch_waveform_into(self):
        expected_waveform = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform)
        interpreter = self.get_initialized_library_interpreter()
        waveform = numpy.empty(len(expected_waveform), numpy.float64)
        interpreter.fetch_waveform_into(waveform)
        assert numpy.array_equal(waveform, expected_waveform)
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_write_waveform(self):
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.write_waveform(expected_array)
        self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_array))

    def test_write_waveform_numpy(self):
        expected_waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy(expected_waveform)
        self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform))

    def test_return_multiple_types(self):
        self.patched_library.niFake_ReturnMultipleTypes.side_effect = self.side_effects_helper.niFake_ReturnMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        array_val = [0, 1, 2]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        self.side_effects_helper['ReturnMultipleTypes']['return'] = len(string_val)
        self.side_effects_helper['ReturnMultipleTypes']['aBoolean'] = boolean_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt32'] = int32_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt64'] = int64_val
        self.side_effects_helper['ReturnMultipleTypes']['anIntEnum'] = enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['aFloat'] = float_val
        self.side_effects_helper['ReturnMultipleTypes']['aFloatEnum'] = float_enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['anArray'] = array_val
        self.side_effects_helper['ReturnMultipleTypes']['aString'] = string_val
        self.side_effects_helper['ReturnMultipleTypes']['return'] = 0
        interpreter = self.get_initialized_library_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
        assert result_boolean == boolean_val
        assert isinstance(result_boolean, bool)
        assert result_int32 == int32_val
        assert isinstance(result_int32, int)
        assert result_int64 == int64_val
        assert isinstance(result_int64, int)
        assert result_enum == enum_val
        assert isinstance(result_enum, nifake.Turtle)
        assert result_float == float_val
        assert isinstance(result_float, float)
        assert result_float_enum == float_enum_val
        assert isinstance(result_float_enum, nifake.FloatEnum)
        assert result_array == array_val
        assert isinstance(result_array, list)
        assert isinstance(result_array[0], float)
        assert result_string == string_val
        assert isinstance(result_string, str)
        assert self.patched_library.niFake_ReturnMultipleTypes.call_count == 2

    def test_multiple_array_types(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(output_array_size),
            _matchers.ViReal64BufferMatcher(output_array_size),
            _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
            _matchers.ViInt32Matcher(len(input_array_of_integers)),
            _matchers.ViReal64BufferMatcher(input_array_of_floats),
            _matchers.ViInt16BufferMatcher(input_array_of_integers),
        )

    def test_multiple_array_types_none_input(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(output_array_size),
            _matchers.ViReal64BufferMatcher(output_array_size),
            _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
            _matchers.ViInt32Matcher(len(input_array_of_floats)),
            _matchers.ViReal64BufferMatcher(input_array_of_floats),
            None
        )

    def test_multiple_arrays_same_size(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
        self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(input_array_of_floats1),
            _matchers.ViReal64BufferMatcher(input_array_of_floats2),
            _matchers.ViReal64BufferMatcher(input_array_of_floats3),
            _matchers.ViReal64BufferMatcher(input_array_of_floats4),
            _matchers.ViInt32Matcher(len(input_array_of_floats1)),
        )

    def test_multiple_arrays_same_size_none_input(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None)
        self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(input_array_of_floats1),
            None,
            None,
            None,
            _matchers.ViInt32Matcher(len(input_array_of_floats1)),
        )

    def test_multiple_arrays_different_size(self):
        self.patched_library.niFake_MultipleArraysDifferentSize.side_effect = self.side_effects_helper.niFake_MultipleArraysDifferentSize
        values_array = [1.1, 2.2, 3.3]
        data_array = [10, 20, 30, 40, 50]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_different_size(values_array, data_array)
        self.patched_library.niFake_MultipleArraysDifferentSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(values_array),
            _matchers.ViInt32Matcher(len(values_array)),
            _matchers.ViInt32BufferMatcher(data_array),
            _matchers.ViInt32Matcher(len(data_array)),
        )

    def test_multiple_arrays_different_size_none_input(self):
        self.patched_library.niFake_MultipleArraysDifferentSize.side_effect = self.side_effects_helper.niFake_MultipleArraysDifferentSize
        values_array = [1.1, 2.2, 3.3]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_different_size(values_array, None)
        self.patched_library.niFake_MultipleArraysDifferentSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(values_array),
            _matchers.ViInt32Matcher(len(values_array)),
            None,
            _matchers.ViInt32Matcher(0),
        )

    def test_mixed_ivi_dance_and_len_mechanism(self):
        self.patched_library.niFake_MixedIviDanceAndLenMechanism.side_effect = self.side_effects_helper.niFake_MixedIviDanceAndLenMechanism
        expected_output = [4, 5]
        self.side_effects_helper['MixedIviDanceAndLenMechanism']['outputArray'] = expected_output
        interpreter = self.get_initialized_library_interpreter()
        result_array = interpreter.mixed_ivi_dance_and_len_mechanism([1.1])
        assert result_array == expected_output
        assert self.patched_library.niFake_MixedIviDanceAndLenMechanism.call_count == 2

    def test_parameters_are_multiple_types(self):
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
        self.patched_library.niFake_ParametersAreMultipleTypes.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanMatcher(boolean_val), _matchers.ViInt32Matcher(int32_val), _matchers.ViInt64Matcher(int64_val), _matchers.ViInt16Matcher(enum_val.value), _matchers.ViReal64Matcher(float_val), _matchers.ViReal64Matcher(float_enum_val.value), _matchers.ViStringMatcher(string_val))

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types(10)
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2])
            assert False
        except TypeError:
            pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            interpreter.simple_function()
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read.side_effect = self.niFake_read_warning
        self.error_code_return = test_error_code
        self.reading = test_reading
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_library_interpreter_always_uses_same_library_instance(self):
        interpreter1 = self.get_initialized_library_interpreter()
        interpreter2 = self.get_initialized_library_interpreter()
        assert interpreter1 is not interpreter2
        assert interpreter1._library is interpreter2._library

    def test_set_runtime_environment_is_called_once_if_present(self):
        nifake._library_interpreter._was_runtime_environment_set = None
        self.get_initialized_library_interpreter()
        self.get_initialized_library_interpreter()
        self.patched_library.niFake_SetRuntimeEnvironment.assert_called_once()

    def test_set_runtime_environment_not_present_in_driver_runtime(self):
        class TypesLibrary:
            item = ""

        nifake._library_interpreter._was_runtime_environment_set = None
        self.patched_library._library = TypesLibrary()
        interpreter = self.get_initialized_library_interpreter()
        with pytest.raises(nifake.errors.DriverTooOldError):
            interpreter._library._get_library_function('niFake_SetRuntimeEnvironment')

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViCharBufferMatcher(256))

    def test_get_a_string_of_size_python_code(self):
        test_size = 4
        expected_string_size = test_size - 1
        test_string = "A string that is larger than test_size."
        expected_string = test_string[:expected_string_size]
        self.patched_library.niFake_GetAStringUsingPythonCode.side_effect = self.side_effects_helper.niFake_GetAStringUsingPythonCode
        self.side_effects_helper['GetAStringUsingPythonCode']['aString'] = expected_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_using_python_code(test_size)
        assert returned_string == expected_string
        self.patched_library.niFake_GetAStringUsingPythonCode.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(test_size), _matchers.ViCharBufferMatcher(test_size))

    def test_return_a_number_and_a_string(self):
        test_string = "this string"
        test_number = 13
        self.patched_library.niFake_ReturnANumberAndAString.side_effect = self.side_effects_helper.niFake_ReturnANumberAndAString
        self.side_effects_helper['ReturnANumberAndAString']['aString'] = test_string
        self.side_effects_helper['ReturnANumberAndAString']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert returned_string == test_string
        assert returned_number == test_number
        self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher(), _matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_char_array(self):
        self.patched_library.niFake_GetAnIviDanceCharArray.side_effect = self.side_effects_helper.niFake_GetAnIviDanceCharArray
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceCharArray']['charArray'] = string_val
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_char_array()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)))
        ]
        self.patched_library.niFake_GetAnIviDanceCharArray.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceCharArray.call_count == 2

    def test_get_string_ivi_dance_error(self):
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.get_attribute_vi_string('', read_write_string_attribute_id)
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        self.patched_library.niFake_GetAnIviDanceWithATwistString.side_effect = self.side_effects_helper.niFake_GetAnIviDanceWithATwistString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceWithATwistString']['aString'] = string_val
        self.side_effects_helper['GetAnIviDanceWithATwistString']['actualSize'] = len(string_val)
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None, _matchers.ViInt32PointerMatcher()),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)), _matchers.ViInt32PointerMatcher())
        ]
        self.patched_library.niFake_GetAnIviDanceWithATwistString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceWithATwistString.call_count == 2

    def test_get_array_using_ivi_dance(self):
        self.patched_library.niFake_GetArrayUsingIviDance.side_effect = self.side_effects_helper.niFake_GetArrayUsingIviDance
        self.side_effects_helper['GetArrayUsingIviDance']['arrayOut'] = [1.1, 2.2]
        interpreter = self.get_initialized_library_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        attribute_id = 1000004
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert attr_int == test_number
        self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int32('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        attribute_id = 1000001
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_real64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        attribute_id = 1000002
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        interpreter = self.get_initialized_library_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(15), _matchers.ViCharBufferMatcher(len(string)))
        ]
        self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_string('', attribute_id, attrib_string)
        self.patched_library.niFake_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        attribute_id = 1000000
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool)
        self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanMatcher(True))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert attr_int == test_number
        self.patched_library.niFake_GetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64Matcher(test_number))

    # Error descriptions

    def test_get_error_returns_mismatched_error_code(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question, only positive"
        wrong_error_code = 54
        wrong_error_desc = "What is six times nine"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = wrong_error_code
        self.side_effects_helper['GetError']['description'] = wrong_error_desc
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    def test_get_error_and_error_message_returns_error(self):
        test_error_code = -42
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = "Also shouldn't get this"
        self.side_effects_helper['error_message']['return'] = -3
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == 'Failed to retrieve error description.'

    def test_get_error_description_error_message_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    def test_get_error_description_error_message_after_session_reset(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc

        def error_message_side_effect(vi, error_code, error_message_buf):
            if vi.value == SESSION_NUM_FOR_TEST:
                return -3
            return self.side_effects_helper.niFake_error_message(vi, error_code, error_message_buf)

        self.patched_library.niFake_error_message.side_effect = error_message_side_effect
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        assert self.patched_library.niFake_error_message.call_count == 2
        self.patched_library.niFake_error_message.assert_has_calls([
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256)),
            call(_matchers.ViSessionMatcher(0), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256)),
        ])

    # Custom types

    def test_set_custom_type(self):
        self.patched_library.niFake_SetCustomType.side_effect = self.side_effects_helper.niFake_SetCustomType
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type(cs)
        self.patched_library.niFake_SetCustomType.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs)))

    def test_get_custom_type(self):
        self.patched_library.niFake_GetCustomType.side_effect = self.side_effects_helper.niFake_GetCustomType
        cs_ctype = nifake.struct_CustomStruct(struct_int=42, struct_double=4.2)
        self.side_effects_helper['GetCustomType']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == cs_ctype.struct_int
        assert cs.struct_double == cs_ctype.struct_double

    def test_set_custom_type_array(self):
        self.patched_library.niFake_SetCustomTypeArray.side_effect = self.side_effects_helper.niFake_SetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type_array(cs)
        self.patched_library.niFake_SetCustomTypeArray.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(cs)), _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype))

    def test_get_custom_type_array(self):
        self.patched_library.niFake_GetCustomTypeArray.side_effect = self.side_effects_helper.niFake_GetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetCustomTypeArray']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs_ctype))
        assert len(cs_test) == len(cs_ctype)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double

    def test_get_custom_type_typedef(self):
        self.patched_library.niFake_GetCustomTypeTypedef.side_effect = self.side_effects_helper.niFake_GetCustomTypeTypedef
        cst = nifake.CustomStructTypedef(struct_int=42, struct_double=4.2)
        cst_ctype = nifake.struct_CustomStructTypedef(cst)
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        csnt_ctype = nifake.struct_CustomStructNestedTypedef(csnt)
        self.side_effects_helper['GetCustomTypeTypedef']['cst'] = cst_ctype
        self.side_effects_helper['GetCustomTypeTypedef']['csnt'] = csnt_ctype
        interpreter = self.get_initialized_library_interpreter()
        cst_test, csnt_test = interpreter.get_custom_type_typedef()
        assert cst_test.struct_int == cst.struct_int
        assert cst_test.struct_double == cst.struct_double
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double

    # python-code size mechanism

    def test_get_array_using_python_code_double(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeDouble.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeDouble
        array_out = [42.0, 43.0, 44.0]
        array_out_ctype = (nifake._visatype.ViReal64 * len(array_out))(*array_out)
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(array_out)
        self.side_effects_helper['GetArrayForPythonCodeDouble']['arrayOut'] = array_out_ctype
        interpreter = self.get_initialized_library_interpreter()
        array_out_test = interpreter.get_array_for_python_code_double()
        assert len(array_out_test) == len(array_out)
        for actual, expected in zip(array_out_test, array_out):
            assert actual == expected

    def test_get_array_using_python_code_custom_type(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeCustomType.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeCustomType
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(cs)
        self.side_effects_helper['GetArrayForPythonCodeCustomType']['arrayOut'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_array_for_python_code_custom_type()
        assert len(cs_test) == len(cs)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double

    def test_get_cal_date_time(self):
        self.patched_library.niFake_GetCalDateAndTime.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.side_effects_helper['GetCalDateAndTime']['return'] = 0
        self.side_effects_helper['GetCalDateAndTime']['month'] = month
        self.side_effects_helper['GetCalDateAndTime']['day'] = day
        self.side_effects_helper['GetCalDateAndTime']['year'] = year
        self.side_effects_helper['GetCalDateAndTime']['hour'] = hour
        self.side_effects_helper['GetCalDateAndTime']['minute'] = minute
        interpreter = self.get_initialized_library_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal

    # Import/Export functions

    def test_import_attribute_configuration_buffer_list_i8(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = expected_list
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = b'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytearray(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = bytearray(b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_array_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = array.array('b', b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_str(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = 'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_write_waveform_numpy_complex128_valid_input(self):
        from nifake._complextype import NIComplexNumber

        waveform_data = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex128)
        number_of_samples = len(waveform_data)

        waveform_data_ctypes = (NIComplexNumber * number_of_samples)(
            *[NIComplexNumber(real=0.707, imag=0.707) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexNumber))
        self.patched_library.niFake_WriteWaveformNumpyComplex128.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplex128
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex128(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplex128.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexNumberPointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_waveform_numpy_complex64_valid_input(self):
        from nifake._complextype import NIComplexNumberF32

        waveform_data = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex64)
        number_of_samples = len(waveform_data)

        waveform_data_ctypes = (NIComplexNumberF32 * number_of_samples)(
            *[NIComplexNumberF32(real=0.707, imag=0.707) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexNumberF32))
        self.patched_library.niFake_WriteWaveformNumpyComplex64.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplex64
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex64(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplex64.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexNumberF32PointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_waveform_numpy_complex_interleaved_i16_valid_input(self):
        from nifake._complextype import NIComplexI16

        waveform_data = numpy.array([32767, 0] * 1000, dtype=numpy.int16)
        number_of_samples = len(waveform_data) // 2
        waveform_data_ctypes = (NIComplexI16 * number_of_samples)(
            *[NIComplexI16(real=32767, imag=0) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexI16))
        self.patched_library.niFake_WriteWaveformNumpyComplexInterleavedI16.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplexInterleavedI16
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex_interleaved_i16(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplexInterleavedI16.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexI16PointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_3d_numpy_array_of_numpy_complex128(self):
        from nifake._complextype import NIComplexNumber

        array_3d = numpy.full((2, 3, 4), 1.0 + 2.0j, dtype=numpy.complex128)
        number_of_samples = array_3d.size
        flattened_array = array_3d.flatten()
        complex_array = (NIComplexNumber * len(flattened_array))()
        for i, value in enumerate(flattened_array):
            complex_array[i] = NIComplexNumber(value.real, value.imag)
        flattened_array_ptr = ctypes.cast(complex_array, ctypes.POINTER(NIComplexNumber))
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.side_effect = self.side_effects_helper.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter
        interpreter = self.get_initialized_library_interpreter()
        interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d)
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.NIComplexNumberPointerMatcher(flattened_array_ptr, number_of_samples)
        )

    def test_no_memorycopy_with_multi_dimensional_numpy_complex128_array(self):
        array_3d = numpy.full((2, 3, 4), 1.0 + 2.0j, dtype=numpy.complex128)
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.side_effect = self.side_effects_helper.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter
        interpreter = self.get_initialized_library_interpreter()
        interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d)
        args, kwargs = self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.call_args
        actual_pointer = args[1]
        input_address = array_3d.__array_interface__['data'][0]
        address_passed_to_library = ctypes.addressof(actual_pointer.contents)
        assert input_address == address_passed_to_library, f"Addresses do NOT match: input_address={input_address}, address_passed_to_library={address_passed_to_library}"

    def test_no_memorycopy_with_numpy_complex64_array(self):
        array_1d = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex64)
        self.patched_library.niFake_WriteWaveformNumpyComplex64.side_effect = (
            self.side_effects_helper.niFake_WriteWaveformNumpyComplex64
        )
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex64(array_1d)
        args, kwargs = self.patched_library.niFake_WriteWaveformNumpyComplex64.call_args
        actual_pointer = args[2]
        input_address = array_1d.__array_interface__['data'][0]
        address_passed_to_library = ctypes.addressof(actual_pointer.contents)
        assert input_address == address_passed_to_library, (
            f"Addresses do NOT match: input_address={input_address}, address_passed_to_library={address_passed_to_library}"
        )

    def test_matcher_prints(self):
        assert _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViSessionMatcher(" + str(nifake._visatype.ViSession) + ", 42)"
        assert _matchers.ViAttrMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViAttrMatcher(" + str(nifake._visatype.ViAttr) + ", 42)"
        assert _matchers.ViInt32Matcher(4).__repr__() == "ViInt32Matcher(" + str(nifake._visatype.ViInt32) + ", 4)"
        assert _matchers.ViStringMatcher('0-24').__repr__() == "ViStringMatcher('0-24')"
        assert _matchers.ViReal64Matcher(-42.0).__repr__() == "ViReal64Matcher(" + str(nifake._visatype.ViReal64) + ", -42.0)"
        assert _matchers.ViReal64PointerMatcher().__repr__() == "ViReal64PointerMatcher(" + str(nifake._visatype.ViReal64) + ")"
        assert _matchers.ViInt32PointerMatcher().__repr__() == "ViInt32PointerMatcher(" + str(nifake._visatype.ViInt32) + ")"
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        assert _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs[0])).__repr__() == "CustomTypeMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, struct_CustomStruct(data=None, struct_int=42, struct_double=4.2))"
        assert _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype).__repr__() == "CustomTypeBufferMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, [struct_CustomStruct(data=None, struct_int=42, struct_double=4.2), struct_CustomStruct(data=None, struct_int=43, struct_double=4.3), struct_CustomStruct(data=None, struct_int=42, struct_double=4.3)])"
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/unit_tests/test_library_singleton.py sha256=118b5ad6e0656d0db8e69ce148a6e1aee5574e4a0fbfedb41efe621e76d747ae bytes=208 -->
## FILE: src/nifake/unit_tests/test_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/unit_tests/test_library_singleton.py`
- sha256: `118b5ad6e0656d0db8e69ce148a6e1aee5574e4a0fbfedb41efe621e76d747ae`
- bytes: 208

````python
import nifake
import pytest


def test_driver_runtime_not_installed_raises_driver_not_installed_error():
    with pytest.raises(nifake.errors.DriverNotInstalledError):
        nifake._library_singleton.get()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifake/unit_tests/test_session.py sha256=27c8aa0fd32c7af6de4defb174955f1bf63a8a9ecfbbe5d79b88fc34a1986449 bytes=51612 -->
## FILE: src/nifake/unit_tests/test_session.py

- repository: `ni/nimi-python`
- source_path: `src/nifake/unit_tests/test_session.py`
- sha256: `27c8aa0fd32c7af6de4defb174955f1bf63a8a9ecfbbe5d79b88fc34a1986449`
- bytes: 51612

````python
import array
import datetime
import hightime
import nifake
import nifake.errors
import numpy
import pytest

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

SESSION_NUM_FOR_TEST = 42
GRPC_SESSION_OBJECT_FOR_TEST = object()


class TestSession:

    class PatchedLibraryInterpreter(nifake._library_interpreter.LibraryInterpreter):
        def __init__(self, encoding):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_library_interpreter = self.PatchedLibraryInterpreter(None)
        self.patched_library_interpreter_ctor = patch('nifake.session._library_interpreter.LibraryInterpreter', return_value=self.patched_library_interpreter)
        self.patched_library_interpreter_ctor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        # We shouldn't call into grpc
        self.patched_grpc_interpreter = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', side_effect=AssertionError('Called into grpc!'))
        self.patched_grpc_interpreter.start()

        def interpreter_init(*args, **kwargs):
            self.patched_library_interpreter._close_on_exit = True
            return SESSION_NUM_FOR_TEST

        self.patched_library_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_library_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_library_interpreter.lock.side_effect = lambda *args: None
        self.patched_library_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_interpreter.stop()
        self.patched_library_interpreter_ctor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1')
        self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', 'Some string', True, True)
        self.patched_library_interpreter.init_with_options.assert_called_once_with('FakeDevice', True, True, 'Some string')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_close(self):
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert isinstance(session, nifake.Session)
            self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
            assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            nifake.Session('dev1')
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            session.close()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert isinstance(session, nifake.Session)
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_session_context_manager_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert isinstance(session, nifake.Session)
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1') as session:
            session.lock()
            self.patched_library_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1') as session:
            session.unlock()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1') as session:
            with session.lock():
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1') as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1') as session:
            session.self_test()

    def test_self_test_fail(self):
        test_error_code = 1
        test_error_message = 'error message'
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, test_error_message)]
        with nifake.Session('dev1') as session:
            try:
                session.self_test()
                assert False
            except nifake.errors.SelfTestError as e:
                assert e.code == test_error_code
                assert e.message == test_error_message

    def test_acquisition_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library_interpreter.initiate.assert_called_once_with()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_acquisition_no_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.initiate()
            self.patched_library_interpreter.initiate.assert_called_once_with()
            session.abort()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_single_point_read_timedelta(self):
        test_maximum_time_ns = 1    # nanoseconds
        test_maximum_time_s = 1e-9  # seconds
        test_maximum_time_timedelta = hightime.timedelta(nanoseconds=test_maximum_time_ns)
        test_reading = 5
        self.patched_library_interpreter.read.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time_timedelta)
            self.patched_library_interpreter.read.assert_called_once_with(test_maximum_time_s)

    def test_enum_input_function_with_defaults(self):
        default_turtle = nifake.Turtle.LEONARDO
        test_turtle = nifake.Turtle.DONATELLO
        self.patched_library_interpreter.enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.enum_input_function_with_defaults()
            session.enum_input_function_with_defaults(test_turtle)
            from unittest.mock import call
            calls = [call(default_turtle), call(test_turtle)]
            self.patched_library_interpreter.enum_input_function_with_defaults.assert_has_calls(calls)

    def test_string_valued_enum_input_function_with_defaults(self):
        default_mobile_os_name = nifake.MobileOSNames.ANDROID
        test_mobile_os_name = nifake.MobileOSNames.IOS
        self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.string_valued_enum_input_function_with_defaults()
            session.string_valued_enum_input_function_with_defaults(test_mobile_os_name)
            from unittest.mock import call
            calls = [call(default_mobile_os_name), call(test_mobile_os_name)]
            self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.assert_has_calls(calls)

    def test_fetch_waveform_into_wrong_type(self):
        length = 10
        with nifake.Session('dev1') as session:
            waveforms = [
                10,
                10.5,
                "Not a numpy.ndarray",
                range(length),
                [i + 0.0 for i in range(length)],
                numpy.empty(length, numpy.int32),
                numpy.empty(length, numpy.uint8)
            ]
            for w in waveforms:
                try:
                    session.fetch_waveform_into(w)
                    assert False
                except TypeError:
                    pass

    def test_parameters_are_multiple_types_error(self):
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, 123, float_val, float_enum_val, string_val)
                assert False
            except TypeError:
                pass
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, 0.123, string_val)
                assert False
            except TypeError:
                pass

    def test_error_with_rep_cap(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.channels['100'].read_write_double = 5.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types(10)
                assert False
            except TypeError:
                pass

    def test_enum_input_function_with_defaults_bad_type_error(self):
        test_turtle = 123
        with nifake.Session('dev1') as session:
            try:
                session.enum_input_function_with_defaults(test_turtle)
                assert False
            except TypeError:
                pass

    def test_get_channel_names(self):
        channel_indices = [0, 3, 2]
        channel_indices_string = '0,3,2'
        expected_channel_names_string = 'ch0,ch3,ch2'
        expected_channel_names = ['ch0', 'ch3', 'ch2']
        self.patched_library_interpreter.get_channel_names.side_effect = [expected_channel_names_string]
        with nifake.Session('dev1') as session:
            channel_names_from_session = session.get_channel_names(channel_indices)
            assert channel_names_from_session == expected_channel_names
            self.patched_library_interpreter.get_channel_names.assert_called_once_with(channel_indices_string)

    # Repeated Capabilities

    def test_repeated_capability_method_on_session_timedelta(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_timedelta = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time_timedelta)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('', test_maximum_time_ms)
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.channels['3'].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('3', test_maximum_time_ms)
        assert value == test_reading

    def test_device_method_not_exist_on_repeated_capability_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['3'].simple_function()
                assert False, 'Method has no repeated capability so it shouldn\'t exist on _RepeatedCapability'
            except AttributeError:
                pass

    def test_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.channels['r0']._repeated_capability_list == ['r0']

    def test_chained_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.sites[0, 1].channels[2, 3]._repeated_capability_list == ['site0/2', 'site0/3', 'site1/2', 'site1/3']

    def test_chained_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.sites[0, 1].channels[2, 3].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('site0/2,site0/3,site1/2,site1/3', test_maximum_time_ms)
        assert value == test_reading

    def test_function_with_repeated_capability_type(self):
        self.patched_library_interpreter.function_with_repeated_capability_type.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.channels['0-3'].function_with_repeated_capability_type()
            self.patched_library_interpreter.function_with_repeated_capability_type.assert_called_once_with('0,1,2,3')

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)

    def test_set_attribute_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_int32_with_converter(self):
        attribute_id = 1000008
        test_number_ms = 3
        test_number_s = 0.003
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number_ms]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_converter
            assert attr_timedelta.total_seconds() == test_number_s
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_int32_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000008
        test_number_ms = -10000
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_converter = hightime.timedelta(milliseconds=test_number_ms)
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number_ms)

    def test_get_attribute_int32_with_month_converter(self):
        attribute_id = 1000014
        test_number_months = 2
        test_number_s = 5256005.76
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number_months]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_month_converter
            assert attr_timedelta.total_seconds() == test_number_s
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_int32_with_month_converter(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000014
        test_number_months = 3
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_month_converter = hightime.timedelta(seconds=60 * 60 * 24 * 30.4167 * test_number_months)
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number_months)

    def test_get_attribute_real64(self):
        attribute_id = 1000001
        test_number = 1.5
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_real64_with_converter(self):
        attribute_id = 1000007
        test_number = 1e-9
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_double_with_converter
            assert attr_timedelta.total_seconds() == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000007
        test_number = 1e-9
        with nifake.Session('dev1') as session:
            session.read_write_double_with_converter = hightime.timedelta(nanoseconds=1)
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_string(self):
        string = 'Testing is fun?'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000002
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, 'This is test string')

    def test_get_attribute_comma_separated_string(self):
        comma_separated_string = 'PinA,PinB,PinC'
        expected_list = ['PinA', 'PinB', 'PinC']
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [comma_separated_string]
        attribute_id = 1000015
        with nifake.Session('dev1') as session:
            attr_list = session.read_write_comma_separated_string
            assert attr_list == expected_list
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_comma_separated_string(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000015
        attrib_list = ['PinA', 'PinB', 'PinC']
        expected_string = 'PinA,PinB,PinC'
        with nifake.Session('dev1') as session:
            session.read_write_comma_separated_string = attrib_list
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, expected_string)

    def test_get_attribute_string_with_converter(self):
        string = 'not that interesting'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string_repeated_capability
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            session.read_write_string_repeated_capability = 42
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, '42')

    def test_get_attribute_boolean(self):
        self.patched_library_interpreter.get_attribute_vi_boolean.side_effect = [1]
        attribute_id = 1000000
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library_interpreter.get_attribute_vi_boolean.assert_called_once_with('', attribute_id)

    def test_set_attribute_boolean(self):
        self.patched_library_interpreter.set_attribute_vi_boolean.side_effect = [None]
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library_interpreter.set_attribute_vi_boolean.assert_called_once_with('', attribute_id, True)

    def test_get_attribute_enum_int32(self):
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [nifake.Color.BLUE]
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_real64(self):
        enum_value = nifake.FloatEnum.SIX_POINT_FIVE
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        enum_value = nifake.FloatEnum.FIVE_POINT_FIVE
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.read_write_enum_with_converter == converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_get_attribute_enum_with_converter_invalid_value_from_driver(self):
        invalid_value_from_driver = 0
        expected_error_message = 'The NI-FAKE runtime returned an unexpected value. This can occur if it is too new for the nifake Python module. Upgrade the nifake Python module.'
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [invalid_value_from_driver]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter
                assert False
            except nifake.errors.DriverTooNewError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_message
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.read_write_enum_with_converter = converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_set_attribute_enum_with_converter_invalid_input(self):
        invalid_input_value = 'invalid'
        expected_error_description = "Invalid value: invalid"
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter = invalid_input_value
                assert False
            except ValueError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_description
            assert not self.patched_library_interpreter.set_attribute_vi_int32.called

    def test_get_attribute_channel(self):
        test_number = 100
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        attribute_id = 1000004
        with nifake.Session('dev1') as session:
            attr_int = session.channels[['0', '1']].read_write_integer
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('0,1', attribute_id)

    def test_set_attribute_channel(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session.channels[range(24)].read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23', attribute_id, test_number)

    def test_get_attribute_int64(self):
        attribute_id = 1000006
        test_number = 6000000000
        self.patched_library_interpreter.get_attribute_vi_int64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int64.assert_called_once_with('', attribute_id)

    def test_set_attribute_int64(self):
        self.patched_library_interpreter.set_attribute_vi_int64.side_effect = [None]
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library_interpreter.set_attribute_vi_int64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_error(self):
        test_error_code = -123
        test_error_desc = "ascending order"
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_set_attribute_error(self):
        attribute_id = 1000001
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double = -42.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, -42.0)

    def test_add_properties_to_session_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_session_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['0'].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.channels['0'].non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_set_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be Color not int'

    def test_set_wrong_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = nifake.FloatEnum.SIX_POINT_FIVE
            except TypeError as e:
                assert str(e) == 'must be Color not FloatEnum'

    def test_multiple_arrays_same_size_wrong_size_2(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_3(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_4(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00, 45.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_different_size_none_input(self):
        values_array = [1.1, 2.2, 3.3]
        self.patched_library_interpreter.multiple_arrays_different_size.side_effect = [None]
        with nifake.Session('dev1') as session:
            assert session.multiple_arrays_different_size(values_array, None) is None
            self.patched_library_interpreter.multiple_arrays_different_size.assert_called_once_with(values_array, None)

    def test_get_cal_date_time(self):
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.patched_library_interpreter.get_cal_date_and_time.side_effect = [(month, day, year, hour, minute)]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_date_and_time(0)
            assert isinstance(last_cal, hightime.datetime)
            assert hightime.datetime(year, month, day, hour, minute) == last_cal

    def test_get_cal_interval(self):
        self.patched_library_interpreter.get_cal_interval.side_effect = [24]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_interval()
            assert isinstance(last_cal, hightime.timedelta)
            assert 730 == last_cal.days

    # Import/Export functions - Invalid types

    def test_import_attribute_configuration_buffer_list_i8_big(self):
        expected_list = [ord('a') * 100, ord('b') * 100, ord('c') * 100, ord('d') * 100]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except ValueError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_float(self):
        expected_list = [ord('a') * 1.0, ord('b') * 1.0, ord('c') * 1.0, ord('d') * 1.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_big_float(self):
        expected_list = [ord('a') * 100.0, ord('b') * 100.0, ord('c') * 100.0, ord('d') * 100.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_export_attribute_configuration_buffer(self):
        expected_buffer_list = [ord('a'), ord('b'), ord('c'), ord('d'), ]
        self.patched_library_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer_list]
        with nifake.Session('dev1') as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer_list)
        self.patched_library_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    def test_channel_on_session(self):
        with nifake.Session('dev1') as session:
            try:
                session['100'].read_write_double = 5.0
                assert False
            except TypeError:
                pass

    def test_function_name(self):
        with nifake.Session('dev1') as session:
            # Pick a function that uses @ivi_synchronized
            assert session.bool_array_output_function.__name__ == 'bool_array_output_function'
            # Pick several functions that do not use @ivi_synchronized to make sure they don't break in the future
            assert session.lock.__name__ == 'lock'
            assert session._error_message.__name__ == '_error_message'
            assert session.initiate.__name__ == 'initiate'
            # Cannot use session.<property>.__name__ since that invokes the get attribute value and the returned value
            # (string, int, float) don't have __name__ properties

    def test_buffer_converter(self):
        self.patched_library_interpreter.double_all_the_nums.side_effect = [None]
        nums = [1, 2, 3, 4.2]
        nums_x2 = [x * 2 for x in nums]
        with nifake.Session('dev1') as session:
            session.double_all_the_nums(nums)
            self.patched_library_interpreter.double_all_the_nums.assert_called_once_with(nums_x2)

    def test_nitclk_integration(self):
        with nifake.Session('dev1') as session:
            assert str(type(session.tclk)) == "<class 'nitclk.session.SessionReference'>"

    def test_accept_list_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        delays = [-1.5, 2.0]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(delays)

    def test_accept_array_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2.0]
        delays = array.array('d', time_values)
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_accept_list_of_time_values_as_timedelta_instances(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2e-9]
        delays = [datetime.timedelta(seconds=-1.5), hightime.timedelta(nanoseconds=2)]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_return_timedelta(self):
        time_value = -1.5
        expected_timedelta = hightime.timedelta(seconds=time_value)
        self.patched_library_interpreter.return_duration_in_seconds.side_effect = [time_value]
        with nifake.Session('dev1') as session:
            returned_timedelta = session.return_duration_in_seconds()
            assert returned_timedelta == expected_timedelta
            self.patched_library_interpreter.return_duration_in_seconds.assert_called_once_with()

    def test_return_timedeltas(self):
        time_values = [-1.5, 2.0]
        expected_timedeltas = [hightime.timedelta(seconds=i) for i in time_values]
        self.patched_library_interpreter.return_list_of_durations_in_seconds.side_effect = [time_values]
        with nifake.Session('dev1') as session:
            returned_timedeltas = session.return_list_of_durations_in_seconds(len(expected_timedeltas))
            assert len(returned_timedeltas) == len(expected_timedeltas)
            assert returned_timedeltas == expected_timedeltas
            self.patched_library_interpreter.return_list_of_durations_in_seconds.assert_called_once_with(len(time_values))

    def test_with_valid_intflag_parameter(self):
        flags = nifake.IntFlagEnum.E | nifake.IntFlagEnum.A
        self.patched_library_interpreter.function_with_intflag_parameter.side_effect = None
        self.patched_library_interpreter.function_with_intflag_parameter.return_value = None
        with nifake.Session('dev1') as session:
            session.function_with_intflag_parameter(flags)
        self.patched_library_interpreter.function_with_intflag_parameter.assert_called_once_with(1073741825)

    def test_with_intflag_parameter_invalid(self):
        invalid_flag = 5
        with nifake.Session('dev1') as session:
            try:
                session.function_with_intflag_parameter(invalid_flag)
                assert False
            except TypeError:
                pass

    def test_session_write_waveform_numpy_complex64_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex128)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=complex64, is complex128"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex64(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message

    def test_session_write_waveform_numpy_complex128_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex64)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=complex128, is complex64"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex128(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message

    def test_session_write_waveform_numpy_complex_interleaved_i16_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex64)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=int16, is complex64"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex_interleaved_i16(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message


class TestGrpcSession:

    class PatchedGrpcInterpreter(nifake._grpc_stub_interpreter.GrpcStubInterpreter):
        def __init__(self, grpc_options):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_grpc_interpreter = self.PatchedGrpcInterpreter(None)
        self.patched_grpc_constructor = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', return_value=self.patched_grpc_interpreter)
        self.patched_grpc_constructor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        def interpreter_init(*args, **kwargs):
            self.patched_grpc_interpreter._close_on_exit = True
            return GRPC_SESSION_OBJECT_FOR_TEST

        self.patched_grpc_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_grpc_interpreter._close_on_exit = True
        self.patched_grpc_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_grpc_interpreter.lock.side_effect = lambda *args: None
        self.patched_grpc_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_constructor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), ''))
        self.patched_grpc_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == GRPC_SESSION_OBJECT_FOR_TEST
        session.close()
        self.patched_grpc_interpreter.close.assert_called_once_with()

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.lock()
            self.patched_grpc_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.unlock()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            with session.lock():
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_grpc_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.self_test()

    def test_export_attribute_configuration_buffer(self):
        expected_buffer = b'abcd'
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer)
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_grpc_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            attr_int = session.read_write_integer
            assert attr_int == test_number
            self.patched_grpc_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)


# not session tests per se
def test_diagnostic_information():
    info = nifake.print_diagnostic_information()
    assert isinstance(info, dict)


def test_dunder_version():
    print(f'Version = {nifake.__version__}')
    assert type(nifake.__version__) is str
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/examples/nifgen_arb_waveform.py sha256=62359ef319e1f91267a8258821d263fe1a0b944fd4c9d3df48c801a5796db205 bytes=2149 -->
## FILE: src/nifgen/examples/nifgen_arb_waveform.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/examples/nifgen_arb_waveform.py`
- sha256: `62359ef319e1f91267a8258821d263fe1a0b944fd4c9d3df48c801a5796db205`
- bytes: 2149

````python
#!/usr/bin/python

import argparse
import math
import nifgen
import sys
import time


def create_waveform_data(number_of_samples):
    waveform_data = []
    angle_per_sample = (2 * math.pi) / number_of_samples
    for i in range(number_of_samples):
        waveform_data.append(math.sin(i * angle_per_sample) * math.sin(i * angle_per_sample * 20))
    return waveform_data


def example(resource_name, options, samples, gain, offset, gen_time):
    waveform_data = create_waveform_data(samples)
    with nifgen.Session(resource_name=resource_name, options=options) as session:
        session.output_mode = nifgen.OutputMode.ARB
        waveform = session.create_waveform(waveform_data_array=waveform_data)
        session.configure_arb_waveform(waveform_handle=waveform, gain=gain, offset=offset)
        with session.initiate():
            time.sleep(gen_time)


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI arbitrary waveform generator.')
    parser.add_argument('-s', '--samples', default=100000, type=int, help='Number of samples')
    parser.add_argument('-g', '--gain', default=1.0, type=float, help='Gain')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.samples, args.gain, args.offset, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 100000, 1.0, 0.0, 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/examples/nifgen_script.py sha256=be32e759c086e89ab7bc757ed9b6d81f6a22e0166cbf2e5843825628b6043d07 bytes=4663 -->
## FILE: src/nifgen/examples/nifgen_script.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/examples/nifgen_script.py`
- sha256: `be32e759c086e89ab7bc757ed9b6d81f6a22e0166cbf2e5843825628b6043d07`
- bytes: 4663

````python
#!/usr/bin/python

import argparse
import nifgen

import math
import sys
import time

# waveform size should be a multiple of the quantum, which is 4, 2 or 1, for all devices
# minimum waveform size needed to prevent underflow varies with sample rate and device.
# If underflow occurs, increase this value.
NUMBER_OF_SAMPLES = 2096


# waveforms finish just short of 360 degrees, so that we don't repeat the first point
# if we repeat the waveform
SINE_WAVE = [math.sin(math.pi * 2 * x / (NUMBER_OF_SAMPLES)) for x in range(NUMBER_OF_SAMPLES)]
RAMP_UP = [x / (NUMBER_OF_SAMPLES) for x in range(NUMBER_OF_SAMPLES)]
RAMP_DOWN = [-1.0 * x for x in RAMP_UP]
SQUARE_WAVE = [1.0 if x < (NUMBER_OF_SAMPLES / 2) else -1.0 for x in range(NUMBER_OF_SAMPLES)]
SAWTOOTH_WAVE = RAMP_UP[::2] + [(-1 + x) for x in RAMP_UP][::2]


SCRIPT_ALL = '''
script scriptmulti
  repeat until scriptTrigger0
    generate rampup
    generate sine
    generate rampdown
  end repeat
  repeat until scriptTrigger0
    generate rampdown
    generate square
    generate rampup
  end repeat
  repeat until scriptTrigger0
    generate rampup
    generate rampdown
  end repeat
  repeat until scriptTrigger0
    generate sine
  end repeat
  repeat until scriptTrigger0
    generate sawtooth
  end repeat
  repeat until scriptTrigger0
    generate rampdown
    generate rampup
  end repeat
end script

script scriptsine
  repeat until scriptTrigger0
    generate sine
  end repeat
end script

script scriptrampup
  repeat until scriptTrigger0
    generate rampup
  end repeat
end script

script scriptrampdown
  repeat until scriptTrigger0
    generate rampdown
  end repeat
end script

script scriptsquare
  repeat until scriptTrigger0
    generate square
  end repeat
end script

script scriptsawtooth
  repeat until scriptTrigger0
    generate sawtooth
  end repeat
end script
'''


def example(resource_name, options, shape, channel):
    with nifgen.Session(resource_name=resource_name, options=options, channel_name=channel) as session:
        # CONFIGURATION
        # 1 - Set the mode to Script
        session.output_mode = nifgen.OutputMode.SCRIPT

        # 2 - Configure Trigger:
        # SOFTWARE TRIGGER: used in the script
        session.script_triggers[0].script_trigger_type = nifgen.ScriptTriggerType.SOFTWARE_EDGE  # TRIG_NONE / DIGITAL_EDGE / DIGITAL_LEVEL / SOFTWARE_EDGE
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING  # RISING / FAILING

        # 3 - Calculate and write different waveform data to the device's onboard memory
        session.channels[channel].write_waveform('sine', SINE_WAVE)        # (waveform_name, data)
        session.channels[channel].write_waveform('rampup', RAMP_UP)
        session.channels[channel].write_waveform('rampdown', RAMP_DOWN)
        session.channels[channel].write_waveform('square', SQUARE_WAVE)
        session.channels[channel].write_waveform('sawtooth', SAWTOOTH_WAVE)

        # 4 - Script to generate
        # supported shapes: SINE / SQUARE / SAWTOOTH / RAMPUP / RAMPDOWN / MULTI
        script_name = f'script{shape.lower()}'
        num_triggers = 6 if shape.upper() == 'MULTI' else 1  # Only multi needs multiple triggers, all others need one

        session.channels[channel].write_script(SCRIPT_ALL)
        session.script_to_generate = script_name

        # LAUNCH
        with session.initiate():
            for x in range(num_triggers):
                time.sleep(10)
                session.script_triggers[0].send_software_edge_trigger()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generate different shape waveforms.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI arbitrary waveform generator.')
    parser.add_argument('-s', '--shape', default='SINE', help='Shape of the signal to generate')
    parser.add_argument('-c', '--channel', default='0', help='Channel to use when generating')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.shape.upper(), args.channel)


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'SINE', '0')


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', '--channel', '0', ]
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/examples/nifgen_standard_function.py sha256=ca29369790a2da73e47c5a7bf8f420a57cdf8578b154ddb8a6e381cdf0993924 bytes=2216 -->
## FILE: src/nifgen/examples/nifgen_standard_function.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/examples/nifgen_standard_function.py`
- sha256: `ca29369790a2da73e47c5a7bf8f420a57cdf8578b154ddb8a6e381cdf0993924`
- bytes: 2216

````python
#!/usr/bin/python

import argparse
import nifgen
import sys
import time


def example(resource_name, options, waveform, frequency, amplitude, offset, phase, gen_time):
    with nifgen.Session(resource_name=resource_name, options=options) as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform[waveform], amplitude=amplitude, frequency=frequency, dc_offset=offset, start_phase=phase)
        with session.initiate():
            time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Generates the standard function.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI function generator.')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
    parser.add_argument('-f', '--frequency', default=1000, type=float, help='Frequency (Hz)')
    parser.add_argument('-a', '--amplitude', default=1.0, type=float, help='Amplitude (Vpk-pk)')
    parser.add_argument('-o', '--offset', default=0.0, type=float, help='DC offset (V)')
    parser.add_argument('-p', '--phase', default=0.0, type=float, help='Start phase (deg)')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.waveform, args.frequency, args.amplitude, args.offset, args.phase, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 'SINE', 1000, 1.0, 0.0, 0.0, 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/examples/nifgen_trigger.py sha256=aad7999dd815c0e73da4d64474fcfdf24b01ac5ca73a68894acedb03497a49c9 bytes=2516 -->
## FILE: src/nifgen/examples/nifgen_trigger.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/examples/nifgen_trigger.py`
- sha256: `aad7999dd815c0e73da4d64474fcfdf24b01ac5ca73a68894acedb03497a49c9`
- bytes: 2516

````python
import argparse
import nifgen
import sys
import time


def example(resource_name1, resource_name2, options, waveform, gen_time):
    with nifgen.Session(resource_name=resource_name1, options=options) as session1, nifgen.Session(resource_name=resource_name2, options=options) as session2:
        session_list = [session1, session2]
        for session in session_list:
            session.output_mode = nifgen.OutputMode.FUNC
            session.configure_standard_waveform(waveform=nifgen.Waveform[waveform], amplitude=1.0, frequency=1000, dc_offset=0.0, start_phase=0.0)
        session1.start_trigger_type = nifgen.StartTriggerType.SOFTWARE_EDGE
        session2.start_trigger_type = nifgen.StartTriggerType.DIGITAL_EDGE
        session2.digital_edge_start_trigger_edge = nifgen.StartTriggerDigitalEdgeEdge.RISING
        session2.digital_edge_start_trigger_source = '/' + resource_name1 + '/0/StartTrigger'
        with session2.initiate():
            with session1.initiate():
                session1.send_software_edge_trigger(nifgen.Trigger.START)
                time.sleep(gen_time)


def _main(argsv):
    supported_waveforms = list(nifgen.Waveform.__members__.keys())[:-1]  # no support for user-defined waveforms in example
    parser = argparse.ArgumentParser(description='Triggers one device on the start trigger of another device.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', '--resource-name1', default='PXI1Slot2', help='Resource name of an NI function generator.')
    parser.add_argument('-n2', '--resource-name2', default='PXI1Slot3', help='Resource name of an NI function generator.')
    parser.add_argument('-w', '--waveform', default=supported_waveforms[0], choices=supported_waveforms, type=str.upper, help='Standard waveform')
    parser.add_argument('-t', '--time', default=5.0, type=float, help='Generation time (s)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name1, args.resource_name2, args.option_string, args.waveform, args.time)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5433 (2CH)', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', 'PXI1Slot3', options, 'SINE', 5.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nifgen/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nifgen/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/__init__.py sha256=9924e5295b922db560a782cff8865ca266c1c530a09a28110e183dde9fab77e7 bytes=2079 -->
## FILE: src/nifgen/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/__init__.py`
- sha256: `9924e5295b922db560a782cff8865ca266c1c530a09a28110e183dde9fab77e7`
- bytes: 2079

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

if 'note' not in config['functions']['_init_function']['parameters'][3]:
    config['functions']['_init_function']['parameters'][3]['note'] = []
if not isinstance(config['functions']['_init_function']['parameters'][3]['note'], list):
    config['functions']['_init_function']['parameters'][3]['note'] = [config['functions']['_init_function']['parameters'][3]['note']]

config['functions']['_init_function']['parameters'][3]['note'].append(
'''
+--------------+----------------------------------------------------------------------------------------------------------+
| Device       | options driver_setup syntax                                                                              |
+==============+==========================================================================================================+
| NI PXI-5404  | { 'driver_setup': { 'Model': '5404', 'BoardType': 'PXI' } }                                              |
+--------------+----------------------------------------------------------------------------------------------------------+
| NI PCI-5411  | { 'driver_setup': { 'Model': '5411', 'BoardType': 'PCI', 'MemorySize': '8000000' } }                     |
+--------------+----------------------------------------------------------------------------------------------------------+
| NI PXIe-5450 | { 'driver_setup': { 'Model': '5450', 'Channels': '0-1', 'BoardType': 'PXIe', 'MemorySize': '8000000' } } |
+--------------+----------------------------------------------------------------------------------------------------------+
''')

__version__ = config['module_version']
````
