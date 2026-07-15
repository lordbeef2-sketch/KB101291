# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/data/test_create_capture_waveform_serial/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: source/tests/assets/data/test_create_capture_waveform_serial/pin_levels.digilevels

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/data/test_create_capture_waveform_serial/pin_levels.digilevels`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/data/test_create_capture_waveform_serial/pin_map.pinmap sha256=9430ff41491a2e5351f6e24aa6f82436828832cfe06fce856a623a8d42c57e25 bytes=4613 -->
## FILE: source/tests/assets/data/test_create_capture_waveform_serial/pin_map.pinmap

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/data/test_create_capture_waveform_serial/pin_map.pinmap`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/data/test_create_capture_waveform_serial/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: source/tests/assets/data/test_create_capture_waveform_serial/specifications.specs

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/data/test_create_capture_waveform_serial/specifications.specs`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/data/test_create_capture_waveform_serial/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: source/tests/assets/data/test_create_capture_waveform_serial/timing.digitiming

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/data/test_create_capture_waveform_serial/timing.digitiming`
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
