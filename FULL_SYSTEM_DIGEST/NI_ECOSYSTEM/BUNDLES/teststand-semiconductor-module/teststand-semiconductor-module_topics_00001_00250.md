# NI DOCUMENT BUNDLE: teststand-semiconductor-module

<!--NI_BUNDLE_CHUNK bundle=teststand-semiconductor-module start=1 end=250 -->
<!--NI_TOPIC bundle=teststand-semiconductor-module path=accelerometer-dotnet.html language=enus -->
## TOPIC 00001: Accelerometer with .NET

- bundle_id: `teststand-semiconductor-module`
- source_path: `accelerometer-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/accelerometer-dotnet.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates several features of TSM in a test program that makes common measurements with the NI-Digital Pattern driver to test an imagined accelerometer part. You can use this example as a starting point for your test programs. Example File Locations <TestStand Public> \Examples\NI_Se

### Accelerometer with .NET

This example demonstrates several features of TSM in a test program that makes common
 measurements with the NI-Digital Pattern driver to test an imagined accelerometer part. You
 can use this example as a starting point for your test programs.

| Example File Locations | <TestStand Public> \\Examples\\NI_SemiconductorModule\\Accelerometer\\DotNET\\Accelerometer.seq |
| --- | --- |
| Highlighted Features | Pin map Multisite Custom instruments Binning Specifications Limits files Test program configurations Virtual pins Offline Mode |
| Major API | TSM Code Module API |
| Prerequisites | You must have NI-Digital Pattern Driver 19.0 or later installed, and you must have two NI-Digital Pattern instruments named HSD_6570_C1_S02 and HSD_6570_C1_S04, respectively, as defined in Measurement & Automation Explorer (MAX). You must have NI-DCPower 20.6 or later installed, and you must have two NI-DCPower instruments named SMU_4143_C1_S06 and SMU_4143_C1_S07, respectively, as defined in MAX. You must have NI-SCOPE 15.0 or later installed, and you must have an NI-SCOPE instrument named SCOPE_5105_C1_S08 as defined in MAX. You must have NI-SWITCH 17.0 or later installed, and you must have a PXI-2567 relay driver module named RELAY_2567_C1_S09, as defined in MAX. (Offline Mode) You must meet the requirements to run the test program in Offline Mode. You must have .NET 4.0 support for the NI-DCPower .NET Class Libraries 1.1 or later installed. You must have .NET 4.0 support for the NI-SCOPE .NET Class Libraries 2.0 or later installed. You must have .NET 4.0 support for the NI-SWITCH .NET Class Libraries 1.1 or later installed. This example uses the Batch process model. Note You can view the test program in the TestStand Sequence Editor and code modules in a C# source code editor without the required NI instrument drivers installed. Visit ni.com/info and enter the Info Code NETAPIdriversupport for information about the available NI .NET APIs and the versions of the NI drivers each supports. (Offline Mode) The NI-Digital Pattern, NI-DCPower, and NI-SCOPE instruments and the PXI-2567 relay driver module are not required to run this example in Offline Mode, but you must install the required instrument drivers. |

Complete the steps in the following sections to learn about the test
 program components. You can also use this example in offline mode.

1. Select Semiconductor Module»Edit Pin Map File or click the Edit Pin Map File[IMAGE alt='image' src='GUID-F141357B-5D8A-42A4-99E9-9C309A69F0FF-a5.png'] button on the TSM toolbar
 to open the Accelerometer pin map file in the Pin Map Editor. 
 The pin map file defines the following information: Two NI-Digital Pattern instruments named
 HSD_6570_C1_S02 and
 HSD_6570_C1_S04. Both instruments belong to the
 same group so that code modules can access all digital pins on the
 tester using a single instrument session.Two NI-DCPower instruments named SMU_4143_C1_S06 and
 SMU_4143_C1_S07.One NI-SCOPE instrument named SCOPE_5105_C1_S08.One PXI-2567 relay driver module named RELAY_2567_C1_S09.Ten DUT pins named Vcc, Gnd,
 SCLK, MOSI, MISO,
 CS, RST, MODE,
 Vref_DIO, and Vref_OScope. The
 Vref_DIO and Vref_OScope pins are
 virtual pins that refer to a single Vref DUT pin and
 are used to connect the pin to two different types of instruments,
 NI-Digital Pattern and NI-SCOPE.One relay named SCOPE_ENABLE_RELAY per site. The test
 program uses the SCOPE_ENABLE_RELAY relay to control a
 physical relay that connects the Vref DUT pin to the
 NI-Digital Pattern instrument or to the NI-SCOPE instrument.One relay named NOISE_ENABLE_RELAY per site. The test
 program uses the NOISE_ENABLE_RELAY relay to control a
 physical relay that connects the Vref DUT pin to a
 noise source, rather than to the NI-Digital Pattern or NI-SCOPE
 instruments.Three pin groups named SPI_Port,
 Digital, and AllDUTPins.One system relay named POWER_RELAY. The test program
 uses the POWER_RELAY relay to control a physical relay
 that controls a power source.Four sites on the tester.A series of connections for each site, in which each connection
 specifies a DUT pin, a site number, an instrument, and an instrument
 channel.Site relay connections that specify to which control line of a relay
 driver module the SCOPE_ENABLE_RELAY relay is connected
 for a given site.Site relay connections that specify to which control line of a relay
 driver module the NOISE_ENABLE_RELAY relay is connected
 for a given site.A system relay connection that specifies whether the power source
 connected to the POWER_RELAY relay is enabled.
2. Complete the following steps to review the Test Program Configurations that
 this test program uses.
  1. Select Semiconductor Module»Edit Test Program: Accelerometer.seq or click the Edit Test Program:
 Accelerometer.seq[IMAGE alt='image' src='GUID-87E58653-7373-4FF8-A391-D94F811EC4FE-a5.png'] button on the TSM
 toolbar.
  2. Select the Configuration Definition panel. 
 This test program specifies two test conditions that each test program
 configuration must define: TestFlowId—Defines an identifying name for the
 test flow.TestTemperature—Defines the temperature at
 which to perform the tests.
  3. Select each of the individual Configuration panels to review the values
 each test program configuration gives to the specified test
 conditions.
3. Use the TestStand Sequence Editor to review the bin definitions file associated
 with the test program. Select Semiconductor Module»Edit Bin Definitions File or click the Edit Bin Definitions File[IMAGE alt='image' src='GUID-F141357B-5D8A-42A4-99E9-9C309A69F0FF-a5.png'] button on the TSM
 toolbar. 
 The bin definitions file defines software bins that the test program uses and
 the hardware bins associated with the software bins.
4. Complete the following steps to review the MainSequence,
 ProcessSetup, and ProcessCleanup sequences
 that this test program uses.
  1. On the Sequences pane, select the MainSequence
 sequence and review the objectives each step performs and optionally
 review the LabVIEW code associated with each step: 
 In the Setup section, if the current test program configuration
 uses the Hot test temperature setting, the test
 program waits until the temperature controller reaches the
 specified temperature.
To prepare for digital tests, the test program configures the
 relay for the Vref pin to the Digital Pattern
 instrument.
The test program tests continuity, leakage, and idle power
 consumption on all digital pins.
The test program resets the DUT in preparation for SPI port
 communication.
The test program enables test mode on the DUT using the SPI
 port.
The test program checks the part number of the DUT by reading a
 register through the SPI port.
If the current TestFlowId is set to Quality the
 test program checks the part number at different Vcc
 levels.
To prepare for analog tests, the test program configures the
 relay for the Vref pin to the NI-SCOPE
 instrument.
The test program checks the minimum, maximum, and RMS voltage
 value on the Vref and uses the value to trim each DUT.
The test program sets and verifies the Vref register on the DUT
 based on the previous Vref measurement.
In the Cleanup section, the test program turns off all
 instrument output to the DUT in preparation for physical binning
 by the handler.
  2. On the Sequences pane, select the ProcessSetup
 sequence. TestStand calls this sequence once before starting testing.
 The steps in this sequence initialize the instruments and store the
 instrument sessions in the SemiconductorModuleContext. There are other
 steps in this sequence to configure a temperature controller, and to
 toggle the power source.
  3. On the Sequences pane, select the ProcessCleanup
 sequence. TestStand calls this sequence once after testing completes.
 The steps in this sequence close and reset the instruments.
5. Select Semiconductor Module»Launch Digital Pattern Editor or click the Launch Digital Pattern Editor[IMAGE alt='image' src='GUID-026EB6E7-4B7B-471B-B4FC-D92BB577C71A-a5.png'] button on the TSM toolbar
 to open the Digital Pattern Editor. Open the <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\DotNET\Accelerometer.digiproj
 digital pattern project file in the Digital Pattern Editor. Use the Digital
 Pattern Editor to review the following files the Accelerometer test program
 uses: 
 Accelerometer.specs — Defines a set of variables
 and associated numeric values that you can reference in pin levels, time
 sets, other specifications files, and Shmoo operations.
Accelerometer.digitiming — Defines configuration
 components of the time sets, including the format and edge placement
 that shape the digital waveform on a per-pin basis.
Accelerometer.digilevels — Defines voltage levels
 for digital pins and pin groups connected to a Digital Pattern
 Instrument and for pins and pin groups connected to an NI-DCPower
 instrument.
SPI - Read Part Number.digipat — Pattern that reads
 the part number register from the DUT.
SPI - Set Test Mode.digipat — Pattern that sets the
 test mode by setting a register on the DUT.
SPI - Set Vref Value.digipat — Pattern that sets
 the Vref register on the DUT using a source waveform and reads it back
 using a capture waveform.
Set Vref Value Waveform.tdms — Source waveform
 configuration used to set the Vref register value.
Get Vref Value Waveform.digicapture — Capture
 waveform configuration used to obtain the Vref register value.
6. Use a text editor or spreadsheet software to open and review the <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\DotNET\Limits\Production
 Limits.txt file, which is the tests limits file for the
 Production configuration of this test program. The test limits file is loaded at
 run time based on the current test configuration. This file specifies the values
 to use to evaluate whether a measurement passes or fails. The test program
 stores the limits loaded from the file with the results.
7. You must meet all the prerequisites to run the test program. To run the test
 program, click the Start/Resume Lot[IMAGE alt='image' src='GUID-502D8EC4-9E5A-4442-A9FC-A7AF315CCD74-a5.png'] button on the TSM
 toolbar.
8. You must install the required instrument drivers and meet all the
 prerequisites to run the test program on a computer without access to NI
 instruments. Complete the following steps to simulate the instruments the test
 program needs.
  1. Click the Enable Offline Mode button [IMAGE alt='image' src='GUID-A213210F-13FD-4FD8-A9B3-8E78D25942D4-a5.png'] on the TSM
 toolbar. To run the test program, click the Start/Resume
 Lot[IMAGE alt='image' src='GUID-502D8EC4-9E5A-4442-A9FC-A7AF315CCD74-a5.png'] button on the TSM
 toolbar.
  2. Launch the Test Program
 Editor and select the Offline Mode
 panel to view the path to the Offline Mode system configuration file TSM
 uses to create simulated instruments for
 Accelerometer.seq.
  3. Click the Disable Offline Mode button [IMAGE alt='image' src='GUID-E0419593-1D7B-46BC-9CC3-46B3E3CBF2BB-a5.png'] to return to the
 default TSM behavior.

Parent topic:

Accelerometer (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=accelerometer-labview.html language=enus -->
## TOPIC 00002: Accelerometer with LabVIEW

- bundle_id: `teststand-semiconductor-module`
- source_path: `accelerometer-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/accelerometer-labview.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates several features of TSM in a test program that makes common measurements with the NI-Digital Pattern driver to test an imagined accelerometer part. You can use this example as a starting point for your test programs. Example File Locations <TestStand Public>\Examples\NI_Sem

### Accelerometer with LabVIEW

This example demonstrates several features of TSM in a test program that makes common
 measurements with the NI-Digital Pattern driver to test an imagined accelerometer part. You
 can use this example as a starting point for your test programs.

| Example File Locations | <TestStand Public>\\Examples\\NI_SemiconductorModule\\Accelerometer\\LabVIEW\\Accelerometer.seq |
| --- | --- |
| Highlighted Features | Pin map Multisite Custom instruments Binning Specifications files Limits files Test program configurations Virtual pins Offline Mode |
| Major API | TSM Code Module API |
| Prerequisites | You must have the LabVIEW Development System installed, and you must configure the LabVIEW Adapter to use the LabVIEW Development System. You must have NI-Digital Pattern Driver 19.0 or later installed, and you must have two NI-Digital Pattern instruments named HSD_6570_C1_S02 and HSD_6570_C1_S04, respectively, as defined in Measurement & Automation Explorer (MAX). You must have NI-DCPower 20.6 or later installed, and you must have two NI-DCPower instruments named SMU_4143_C1_S06 and SMU_4143_C1_S07, respectively, as defined in MAX. You must have NI-SCOPE 15.0 or later installed, and you must have an NI-SCOPE instrument named SCOPE_5105_C1_S08 as defined in MAX. You must have NI-SWITCH 17.0 or later installed, and you must have a PXI-2567 relay driver module named RELAY_2567_C1_S09, as defined in MAX. (Offline Mode) You must meet the requirements to run the test program in Offline Mode. This example uses the Batch process model. Note You can view the test program in the TestStand Sequence Editor and partial code modules in LabVIEW without the required NI instrument drivers installed. Install the drivers to view the full code modules in LabVIEW. Visit ni.com/info and enter the Info Code rddrau to access the latest software drivers and updates. (Offline Mode) The NI-Digital Pattern, NI-DCPower, and NI-SCOPE instruments and the PXI-2567 relay driver module are not required to run this example in Offline Mode, but you must install the required instrument drivers. |

Complete the steps in the following sections to learn about the test program
 components. You can also use this example in offline mode.

1. Select Semiconductor Module»Edit Pin Map File or click the Edit Pin Map File[IMAGE alt='image' src='GUID-F141357B-5D8A-42A4-99E9-9C309A69F0FF-a5.png'] button on the TSM toolbar to
 open the Accelerometer pin map file in the Pin Map Editor. 
 The pin map file defines the following information: Two NI-Digital Pattern instruments named
 HSD_6570_C1_S02 and
 HSD_6570_C1_S04. Both instruments belong to the
 same group so that code modules can access all digital pins on the
 tester using a single instrument session.Two NI-DCPower instruments named SMU_4143_C1_S06 and
 SMU_4143_C1_S07.One NI-SCOPE instrument named SCOPE_5105_C1_S08.One PXI-2567 relay driver module named RELAY_2567_C1_S09.Ten DUT pins named Vcc, Gnd,
 SCLK, MOSI, MISO,
 CS, RST, MODE,
 Vref_DIO, and Vref_OScope. The
 Vref_DIO and Vref_OScope pins are
 virtual pins that refer to a single Vref DUT pin and
 are used to connect the pin to two different types of instruments,
 NI-Digital Pattern and NI-SCOPE.One relay named SCOPE_ENABLE_RELAY per site. The test
 program uses the SCOPE_ENABLE_RELAY relay to control a
 physical relay that connects the Vref DUT pin to the
 NI-Digital Pattern instrument or to the NI-SCOPE instrument.One relay named NOISE_ENABLE_RELAY per site. The test
 program uses the NOISE_ENABLE_RELAY relay to control a
 physical relay that connects the Vref DUT pin to a
 noise source, rather than to the NI-Digital Pattern or NI-SCOPE
 instruments.Three pin groups named SPI_Port,
 Digital, and AllDUTPins.One system relay named POWER_RELAY. The test program
 uses the POWER_RELAY relay to control a physical relay
 that controls a power source.Four sites on the tester.A series of connections for each site, in which each connection
 specifies a DUT pin, a site number, an instrument, and an instrument
 channel.Site relay connections that specify to which control line of a relay
 driver module the SCOPE_ENABLE_RELAY relay is connected
 for a given site.Site relay connections that specify to which control line of a relay
 driver module the NOISE_ENABLE_RELAY relay is connected
 for a given site.A system relay connection that specifies whether the power source
 connected to the POWER_RELAY relay is enabled.
2. Complete the following steps to review the Test Program Configurations that
 this test program uses.
  1. Select Semiconductor Module»Edit Test Program: Accelerometer.seq or click the Edit Test Program:
 Accelerometer.seq[IMAGE alt='image' src='GUID-87E58653-7373-4FF8-A391-D94F811EC4FE-a5.png'] button on the TSM
 toolbar.
  2. Select the Configuration Definition panel. 
 This test program specifies two test conditions that each test program
 configuration must define: TestFlowId—Defines an identifying name
 for the test flow.TestTemperature—Defines the temperature
 at which to perform the tests.
  3. Select each of the individual Configuration panels to review the values
 each test program configuration gives to the specified test
 conditions.
3. Use the TestStand Sequence Editor to review the bin definitions file associated
 with the test program. Select Semiconductor Module»Edit Bin Definitions File or click the Edit Bin Definitions File[IMAGE alt='image' src='GUID-1C184611-6EBF-4EA5-B526-282013078C14-a5.png'] button on the TSM toolbar. 
 The bin definitions file defines software bins that the test program uses and
 the hardware bins associated with the software bins.
4. Complete the following steps to review the MainSequence,
 ProcessSetup, and ProcessCleanup sequences
 that this test program uses.
  1. On the Sequences pane, select the MainSequence
 sequence and review the objectives each step performs and optionally
 review the LabVIEW code associated with each step: 
 In the Setup section, if the current test program configuration
 uses the Hot test temperature setting, the test
 program waits until the temperature controller reaches the
 specified temperature.
To prepare for digital tests, the test program configures the
 relay for the Vref pin to the Digital Pattern
 instrument.
The test program tests continuity, leakage, and idle power
 consumption on all digital pins.
The test program resets the DUT in preparation for SPI port
 communication.
The test program enables test mode on the DUT using the SPI
 port.
The test program checks the part number of the DUT by reading a
 register through the SPI port.
If the current TestFlowId is set to Quality the
 test program checks the part number at different Vcc
 levels.
To prepare for analog tests, the test program configures the
 relay for the Vref pin to the NI-SCOPE
 instrument.
The test program checks the minimum, maximum, and RMS voltage
 value on the Vref and uses the value to trim each DUT.
The test program sets and verifies the Vref register on the DUT
 based on the previous Vref measurement.
In the Cleanup section, the test program turns off all
 instrument output to the DUT in preparation for physical binning
 by the handler.
  2. On the Sequences pane, select the ProcessSetup
 sequence. TestStand calls this sequence once before starting testing.
 The steps in this sequence initialize the instruments and store the
 instrument sessions in the SemiconductorModuleContext. There are other
 steps in this sequence to configure a temperature controller, and to
 toggle the power source.
  3. On the Sequences pane, select the ProcessCleanup
 sequence. TestStand calls this sequence once after testing completes.
 The steps in this sequence close and reset the instruments.
5. Select Semiconductor Module»Launch Digital Pattern Editor or click the Launch Digital Pattern
 Editor[IMAGE alt='image' src='GUID-026EB6E7-4B7B-471B-B4FC-D92BB577C71A-a5.png'] button on the TSM toolbar to open the Digital Pattern
 Editor. Open the <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\LabVIEW\Accelerometer.digiproj
 digital pattern project file in the Digital Pattern Editor. Use the Digital
 Pattern Editor to review the following files the Accelerometer test program
 uses: 
 Accelerometer.specs—Defines a set of variables
 and associated numeric values that you can reference in pin levels, time
 sets, other specifications files, and Shmoo operations.
 Accelerometer.digitiming—Defines configuration
 components of the time sets, including the format and edge placement
 that shape the digital waveform on a per-pin basis.
 Accelerometer.digilevels—Defines voltage levels
 for digital pins and pin groups connected to a Digital Pattern
 Instrument and for pins and pin groups connected to an NI-DCPower
 instrument.
 SPI - Read Part Number.digipat—Pattern that reads
 the part number register from the DUT.
 SPI - Set Test Mode.digipat—Pattern that sets the
 test mode by setting a register on the DUT.
 SPI - Set Vref Value.digipat—Pattern that sets
 the Vref register on the DUT using a source waveform and reads it back
 using a capture waveform.
 Set Vref Value Waveform.tdms—Source waveform
 configuration used to set the Vref register value.
 Get Vref Value Waveform.digicapture—Capture
 waveform configuration used to obtain the Vref register value.
6. Use a text editor or spreadsheet software to open and review the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\LabVIEW\Limits\Production
 Limits.txt file, which is the tests limits file for the
 Production configuration of this test program. The test limits file is loaded at
 run time based on the current test configuration. This file specifies the values
 to use to evaluate whether a measurement passes or fails. The test program
 stores the limits loaded from the file with the results.
7. You must meet all the prerequisites to run the test program. To run the test
 program, click the Start/Resume Lot[IMAGE alt='image' src='GUID-502D8EC4-9E5A-4442-A9FC-A7AF315CCD74-a5.png']
 button on the TSM toolbar.
8. You must install the required instrument drivers and meet all the
 prerequisites to run the test program on a computer without access to NI
 instruments. Complete the following steps to simulate the instruments the test
 program needs.
  1. Click the Enable Offline Mode button [IMAGE alt='image' src='GUID-A213210F-13FD-4FD8-A9B3-8E78D25942D4-a5.png'] on the TSM
 toolbar. To run the test program, click the Start/Resume
 Lot[IMAGE alt='image' src='GUID-502D8EC4-9E5A-4442-A9FC-A7AF315CCD74-a5.png'] button on the TSM
 toolbar.
  2. Launch the Test Program
 Editor and select the Offline Mode
 panel to view the path to the Offline Mode system configuration file TSM
 uses to create simulated instruments for
 Accelerometer.seq.
  3. Click the Disable Offline Mode button [IMAGE alt='image' src='GUID-E0419593-1D7B-46BC-9CC3-46B3E3CBF2BB-a5.png'] to return to the
 default TSM behavior.

Parent topic:

Accelerometer (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=accelerometer.html language=enus -->
## TOPIC 00003: Accelerometer (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `accelerometer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/accelerometer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\NI_SemiconductorModule\Accelerometer directory contains the following examples: Accelerometer with LabVIEW Accelerometer with .NET The NI TestStand 2016 Semiconductor Module and later natively support digital pattern instruments that use the NI-Digital Pattern Driver

### Accelerometer (TSM)

The <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer
 directory contains the following examples:

- Accelerometer with LabVIEW
- Accelerometer with .NET

Note

Parent topic:

TSM Example Programs

Related tasks:

- Accelerometer with LabVIEW
- Accelerometer with .NET

<!--NI_TOPIC bundle=teststand-semiconductor-module path=access-lot-settings-test-program.html language=enus -->
## TOPIC 00004: Accessing Lot Settings from a Test Program (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `access-lot-settings-test-program.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/access-lot-settings-test-program.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Get Test Information step to access standard and custom lot settings in a test program sequence file. The following table lists the properties of the NI_SemiconductorModule_StandardLotSettings data type, the fields of the Master Information Record (MIR) of the Standard Test Data Format (STDF

### Accessing Lot Settings from a Test Program (TSM)

Use the Get Test
 Information step to access standard and custom lot
 settings in a test program sequence file.

The following table lists the properties of the
 NI_SemiconductorModule_StandardLotSettings data type, the fields of the Master Information
 Record (MIR) of the Standard Test Data Format (STDF) version 4 specification that the STDF Log result processing
 plug-in sets using the properties, or other purpose of each property.

Note

| Property Name | Corresponding STDF Record Field or Other Purpose |
| --- | --- |
| ActiveConfigurationName | Specifies the name of the test program configuration to use to obtain standard lot settings and custom test conditions. |
| AuxiliaryDataFile | MIR: AUX_FILE |
| BurnInTime | MIR: BURN_TIM |
| CommandModeCode | MIR: CMOD_COD |
| CorrelationOffsetsFileAbsolutePath | Contains the absolute path of the correlation offsets file the Load Correlation Offsets step loads. Do not set this property. TSM sets this property at run time. If the test program does not use correlation offsets, this property is an empty string. If the test program executes multiple Load Correlation Offsets steps, this property contains the path loaded by the step that executed last. |
| DateCode | MIR: DATE_COD |
| DeviceDesignRevision | MIR: DSGN_REV |
| EngineeringLotId | MIR: ENG_ID |
| FabricationProcessId | MIR: PROC_ID |
| JobName | MIR: JOB_NAM (Default value is the test program sequence filename without the file extension.) |
| JobRevision | MIR: JOB_REV (Default value is the test program sequence file version.) |
| LimitsFileAbsolutePath | Contains the absolute path of the test limits file that TSM used to import test limits at run time. Do not set this property. TSM sets this property at run time. |
| LimitsFileRelativePath | Specifies the test limits file to use for importing test limits at run time. Use the Test Program Editor to specify the limits file for a test program configuration. TSM sets this property at run time to the limits file the active test program configuration specifies. |
| LimitsFileReplaceTests | Specifies whether TSM deletes existing tests before importing limits from a test limits file that LimitsFileRelativePath specifies. A value of True corresponds to the Replace all tests in matching steps import mode. A value of False corresponds to the Update limits in matching tests import mode. |
| LotId | MIR: LOT_ID |
| LotSize | Corresponds to the Estimated Lot Size option in the Configure Lot Settings dialog box. An inline QA algorithm can use this property to determine for which DUTs to enable inline QA. |
| MainSequenceFilePath | Specifies the file path of the test program main sequence file to use with the current test lot. |
| MIRUserText | MIR: USER_TXT |
| OperationFrequency | MIR: OPER_FRQ |
| OperatorName | MIR: OPER_NAM |
| PackageType | MIR: PKG_TYP |
| PartType | MIR: PART_TYP |
| ProductFamilyId | MIR: FAMLY_ID |
| ProtectionCode | MIR: PROT_COD |
| RequireEveryStepToBeInLimitsFile | Specifies whether TSM requires that every step or test in the test program sequence file have a corresponding entry in the test limits file when importing limits from a test limits file. |
| RetestCodeRetestCount* | MIR: RTST_COD |
| ROMCodeId | MIR: ROM_COD |
| SetupTime | MIR: SETUP_T This value represents the setup time in seconds since midnight (00:00:00), January 1, 1970, coordinated universal time (UTC). UTC is also known as Greenwich mean time. The STDF Log result processing plug-in converts this value to local time when storing the value in the SETUP_T field. |
| SublotId | MIR: SBLOT_ID TSM sets the SBLOT_ID field to the wafer ID obtained from the prober driver when you enable the Generate One File per Wafer STDF option and the SublotId lot setting property value is empty. |
| SupervisorName | MIR: SUPR_NAM |
| TestCode | MIR: TEST_COD |
| TestFlowId | MIR: FLOW_ID |
| TestModeCode | MIR: MODE_COD |
| TestSetupId | MIR: SETUP_ID |
| TestSpecificationName | MIR: SPEC_NAM |
| TestSpecificationVersion | MIR: SPEC_VER |
| TestTemperature | MIR: TST_TEMP |
| UseEmbeddedLimitsFileData | Indicates whether the limits file data is embedded in the test program sequence file. Do not set this property. TSM sets this property at run time based on the active configuration. |
| Wafer.WaferSize | WCR: WAFR_SZ |
| Wafer.DieHeight | WCR: DIE_HT |
| Wafer.DieWidth | WCR: DIE_WID |
| Wafer.Units | WCR: WF_UNITS |
| Wafer.FlatOrientation | WCR: WF_FLAT |
| Wafer.CenterXCoordinate | WCR: CENTER_X |
| Wafer.CenterYCoordinate | WCR: CENTER_Y |
| Wafer.PositiveXDirection | WCR: POS_X |
| Wafer.PositiveYDirection | WCR: POS_Y |
| * If (RetestCode is not empty string) then RTST_COD = RetestCode Else If (RetestCount is in the range [0-9]) then RTST_COD = '0' - '9' Else RTST_COD = space |  |

Parent topic:

Specifying Settings for the Current Lot under Test (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=access-station-settings.html language=enus -->
## TOPIC 00005: Accessing Station Settings from a Test Program (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `access-station-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/access-station-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Get Test Information step to access standard and custom station settings in a test program sequence file. The following table lists the properties of the NI_SemiconductorModule_StandardStationSettings data type, the fields of the Master Information Record (MIR) or Site Description Record (SD

### Accessing Station Settings from a Test Program (TSM)

Use the Get Test
 Information step to access standard and custom
 station settings in a test program sequence file.

The following table lists the properties of the
 NI_SemiconductorModule_StandardStationSettings data type, the fields
 of the Master Information Record (MIR) or Site Description Record
 (SDR) of the Standard Test Data Format (STDF) version 4
 specification that the
 STDF Log result processing plug-in
 sets using the properties, or other purpose of each property.

Note

| Property Name | Corresponding STDF Record Field or Other Purpose |
| --- | --- |
| AllowMorePinMapSitesThanTestSockets | Specifies whether TSM runs a test program with a pin map with more sites than the number of test sockets configured in the model options. If you disable this option, TSM reports a run-time error if the pin map has more sites than test sockets. |
| AllowFewerPinMapSitesThanTestSockets | Specifies whether TSM runs a test program with a pin map with fewer sites than the number of test sockets configured in the model options. If you disable this option, TSM reports a run-time error if the pin map has fewer sites than test sockets. |
| AvailableSiteNumbers | Specifies which site numbers from a pin map for a test program to use when running the test program. Other sites in the pin map are ignored. For example, you can set this property to disable specific sites or to use the particular connections of a pin map that match the DIB for the test station. If you leave this array empty, TSM uses the first N sites in the pin map, where N is the number of available test sockets in the station model up to the total number of sites in the pin map. The default Configure Lot Settings dialog box sets this property based on the Enabled Sites control. |
| DIBBoardId | SDR: DIB_ID |
| DIBBoardType | SDR: DIB_TYP |
| ExtraEquipmentId | SDR: EXTR_ID |
| ExtraEquipmentType | SDR: EXTR_TYP |
| GenerateUniquePartIds | Specifies whether TSM generates unique values for the PartId field of Part Results Records (PRRs) of the STDF log file. Set this value to False to generate unique PartId values using a custom algorithm you implement. When the GenerateUniquePartIds property is True, TSM reassigns the same unique Part ID to the part when it is retested. Complete the following steps to assign a new unique Part ID to a part when it is retested: Using a text editor, open the RuntimeSettings.ini.example file located in the <TestStand Application Data>\\Cfg\\NI_SemiconductorModule directory. Set the value of the GenerateUniquePartIdsForRetestedParts key to true. Go to File » Save as and rename the modified file to RuntimeSettings.ini. |
| HandlerContactorId | SDR: CONT_ID |
| HandlerContactorType | SDR: CONT_TYP |
| HandlerDriverSequenceFilePath | Stores the absolute path and sequence filename of the real or simulated handler/prober driver. When the value of the HandlerMode property is 0, TSM does not use this property. |
| HandlerId | SDR: HAND_ID |
| HandlerMode | Stores the current handler/prober mode. |
| HandlerType | SDR: HAND_TYP (Default value depends on the handler/prober mode. It is the handler/prober driver sequence filename or "No Handler" or "Simulated Handler".) |
| InlineQAEnabled | Specifies whether you enabled inline QA. |
| InlineQAAlgorithmSequenceFilePath | Stores the absolute path of the inline QA algorithm sequence file. |
| InterfaceCableId | SDR: CABL_ID |
| InterfaceCableType | SDR: CABL_TYP |
| LaserId | SDR: LASR_ID |
| LaserType | SDR: LASR_TYP |
| LoadBoardId | SDR: LOAD_ID |
| LoadBoardType | SDR: LOAD_TYP |
| NodeName | MIR: NODE_NAM (Default value is the TestStand Station ID.) |
| PartCountWindowSize | Specifies the number of part test results tracked per site. The site status indicators in the default operator interface display the results of the last n parts, where this option specifies n. |
| TimeStatisticsWindowSize | Specifies the number of parts used to compute the average cycle time displayed in the default operator interface. Use a negative value to use the default, which is 10 *n, where n is the number of sites. Use a value of 0 to use the cycle time of all tested parts. Regardless of the setting value, TSM never includes the cycle time of the first part in the average. |
| OfflineMode | Specifies whether Offline Mode is enabled, which allows you to develop, run, and debug test programs only on a computer without access to NI instruments. |
| ProbeCardId | SDR: CARD_ID |
| ProbeCardType | SDR: CARD_TYP |
| StationNumber | MIR: STAT_NUM |
| TesterSerialNumber | MIR: SERL_NUM |
| TesterType | MIR: TSTR_TYP (Default value is "National Instruments".) |
| TestFacilityId | MIR: FACIL_ID |
| TestFloorId | MIR: FLOOR_ID |

Parent topic:

Specifying Settings for the Current Test Station (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=add-connection-to-pinmap.html language=enus -->
## TOPIC 00006: Adding a Connection in the Pin Map Editor (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `add-connection-to-pinmap.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/add-connection-to-pinmap.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Connections section on the Pin Map tab to specify mappings among pins, relays, sites, instruments, instrument channels, relay driver modules, and relay driver control lines. Navigate to Semiconductor Module Edit Pin Map File to launch the Pin Map Editor. In the Pin Map tab, click <Add Connec

### Adding a Connection in the Pin Map Editor
 (TSM)

Use the Connections section on the Pin
 Map tab to specify mappings among pins, relays, sites, instruments,
 instrument channels, relay driver modules, and relay driver control lines.

1. Navigate to Semiconductor Module»Edit Pin Map File to launch the Pin Map Editor.
2. In the Pin Map tab, click <Add Connections
 Here> to open the Connections pane.
3. Click the connection type you want to add. Select from the options below. 
 Connection Type
 DescriptionConnection
 A connection between a DUT pin and an instrument channel
 for one or more sites
 System Connection
 A direct connection between a system pin and an
 instrument channel
 Multiplexed Connection
 A multiplexed connection between the same DUT pin on
 multiple sites and a single instrument channel
 Relay Connection
 A connection between a site relay and a relay control
 line for one or more sites
 System Relay Connection
 A direct connection between a system relay and a relay
 control line
4. Configure the connection. 
 The Pin Map Editor automatically adds the connection to the
 Connections section.
5. Optional: 
 Click a connection to view and edit it in the
 Connections pane. 
 You can also view and edit all connections in the
 Connections table.
6. Optional: 
 Add a comment to help keep connections organized. 
 
 TSM displays the comment above the connection.
  1. Click on the connection where you want to add a comment.
  2. In the Connections pane, click Comment.
  3. Add your comment in the Comment field.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)

Related tasks:

- Viewing and Editing Connections in the Connections Table (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=add-mbi-to-pinmap.html language=enus -->
## TOPIC 00007: Adding a Model-Based Instrument to Your Pin Map (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `add-mbi-to-pinmap.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/add-mbi-to-pinmap.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Instruments tab of the Pin Map Editor to add and modify instances of Model-Based Instruments in the pin map. Navigate to Semiconductor Module Edit Pin Map File to launch the Pin Map Editor. In the Pin Map tab, select <Add Instruments Here>. TSM displays the instrument types that you can add.

### Adding a Model-Based Instrument to Your Pin
 Map (TSM)

Use the Instruments tab of the Pin Map Editor to add and modify instances of
 Model-Based Instruments in the pin map.

1. Navigate to Semiconductor Module»Edit Pin Map File to launch the Pin Map Editor.
2. In the Pin Map tab, select <Add Instruments Here>. 
 TSM displays the instrument types that you can add.
3. Click Model-Based Instrument to launch the configuration
 window.
4. In the Name field, specify the name of the instrument
 that will appear in the pin map.
5. Select the instrument model description file from the Instrument
 Model drop-down menu. 
 TSM will display the category and subcategory of the Model-Based Instrument
 you select.
6. Specify any additional instrument or resource properties.
7. Click OK.

Parent topic:

Model-Based Instruments (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=adding-dtrs-for-wafer-testing.html language=enus -->
## TOPIC 00008: Adding DTRs for Wafer Testing When the Generate One Filer per Wafer Option is Enabled

- bundle_id: `teststand-semiconductor-module`
- source_path: `adding-dtrs-for-wafer-testing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/adding-dtrs-for-wafer-testing.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: If the Generate One File per Wafer option is enabled, the STDF Log result processor writes summary records (TSRs, HBRs, SBRs, and PCR) and closes the STDF file when it encounters the end of the wafer in the Model Plugin - Batch Done entry point. To ensure that DTRs are included in the wafer STDF fil

### Adding DTRs for Wafer Testing When the Generate One Filer per Wafer Option is Enabled

If the Generate One File per Wafer option is enabled, the STDF Log result processor writes summary records (TSRs, HBRs, SBRs, and PCR) and closes the STDF file when it encounters the end of the wafer in the Model Plugin - Batch Done entry point. To ensure that DTRs are included in the wafer STDF file, you must add the DTRs before the STDF Log result processor Model Plugin - Batch Done entry point is called.

The custom result processor that you create must appear before the STDF Log result processor in the order of result processors in the Result Processing dialog box. The following table lists the sequences to modify to create the DTR for various locations in the STDF log file. In some cases, you must use a custom result processor because there is no test program callback sequence that generates the desired results.

| Desired Location of DTR | Test Program Sequence File Callback Sequence | Custom Result Processor Entry Point |
| --- | --- | --- |
| At beginning of each wafer log (after initial records) using Batch process model |  | Model Plugin - Pre Batch Execute step only if SemiconductorModuleManager.BatchRuntimeData.IsStartOfWafer is True . |
| At beginning of each wafer log (after initial records) using Sequential process model |  | Model Plugin - Pre UUT Execute step only if SemiconductorModuleManager.BatchRuntimeData.IsStartOfWafer is True. |
| With each batch (after last PRR of previous batch and before first PIR of current batch) | PreBatch | Model Plugin - Pre Batch or Model Plugin - Batch Done |
| With each part using Sequential process model | PreUUT | Model Plugin - Pre UUT or Model Plugin - UUT Done |
| With last batch before end of each wafer log using Batch process model |  | Model Plugin - Batch Done Execute step only if SemiconductorModuleManager.BatchRuntimeData.IsEndOfWafer is True |
| With last part before end of each wafer log using Sequential process model |  | Model Plugin - UUT Done Execute step only if SemiconductorModuleManager.BatchRuntimeData.IsEndOfWafer is True. |

Parent topic:

Adding DTRs to the STDF Log File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=adding-dtrs-to-stdf-log-file.html language=enus -->
## TOPIC 00009: Adding DTRs to the STDF Log File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `adding-dtrs-to-stdf-log-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/adding-dtrs-to-stdf-log-file.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the TSM STDF result processor, you can insert Datalog Text Records (DTR) in various locations in the STDF log file. The method for creating DTRs differs depending on the following conditions and locations at which you insert the DTR.

### Adding DTRs to the STDF Log File (TSM)

Using the TSM STDF result processor, you can insert Datalog Text Records (DTR) in various
 locations in the STDF log file. The method for creating
 DTRs differs depending on the following conditions and locations at
 which you insert the DTR.

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=adjust-bios.html language=enus -->
## TOPIC 00010: Adjust BIOS CPU Settings (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `adjust-bios.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/adjust-bios.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some configuration options can lead to slower than expected test times when using the TestStand Semiconductor Module. You might be able to improve performance of a test program by disabling hyper-threading or by reducing the number of cores the CPU uses. Always measure performance before and after m

### Adjust BIOS CPU Settings (TSM)

Some configuration options can lead to slower than expected test times when using the TestStand
 Semiconductor Module. You might be able to improve performance of a
 test program by disabling hyper-threading or by reducing the number
 of cores the CPU uses. Always measure performance before and after
 making any changes to determine how the change affects
 performance.

Use the BIOS settings on the computer to disable hyper-threading or to change the number of CPU cores. Typically, you enter the BIOS settings screen by pressing the <Delete> (DEL) key after you restart the computer.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=advanced-tab.html language=enus -->
## TOPIC 00011: Advanced Tab

- bundle_id: `teststand-semiconductor-module`
- source_path: `advanced-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/advanced-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Advanced tab contains the following options: Result Processing—Launches the Result Processing dialog box, in which you specify and configure the result processors to execute during test program execution. Station Options—Launches the Station Options dialog box, in which you configure advanced op

### Advanced Tab

The Advanced tab contains the following options:

- Result Processing —Launches the Result
 Processing dialog box, in which you specify
 and configure the result processors to execute during test
 program execution.
- Station Options —Launches the Station
 Options dialog box, in which you configure
 advanced options for the test station.
- Search Directories —Launches the Edit Search
 Directories dialog box, in which you
 configure the search directories to use to find files during
 execution.
- LabVIEW Adapter —Launches the LabVIEW Adapter
 Configuration dialog box, in which you
 specify options for calling LabVIEW code. Select the
 Development System option for
 debugging. Select the LabVIEW Run-Time
 Engine option for execution.

Parent topic:

Configure Station Settings Dialog Box (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=alarms-panel.html language=enus -->
## TOPIC 00012: Alarms Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `alarms-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/alarms-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you open the Alarms panel, TSM checks the pin map and queries each instrument driver to determine which alarms the instrument supports. The Alarms panel lists the pins connected to instruments with alarms support and the supported alarm types for each pin. Use this panel to enable alarms and sp

### Alarms Panel

When you open the Alarms panel, TSM checks the pin map and queries each instrument driver to
 determine which alarms the instrument supports. The Alarms panel lists the pins connected to instruments with
 alarms support and the supported alarm types for each pin. Use this panel to enable alarms and specify the
 run-time behavior for each pin and alarm combination. When a test runs, TSM checks for alarms after each test
 step and executes the behavior you specified.

The Alarms panel contains the following options:

- Alarms enabled —Specifies whether alarms are enabled.
 Enable alarms if you want TSM to check for alarms after each step and execute
 the action specified in the Behavior column. Test times
 may increase when you enable alarms. Note Code modules can temporarily disable
 and re-enable alarms for specific pins using the TSM Code Module API.
- Pin —Specifies the pin.
- Alarm Type —Specifies the type of alarm. Refer to
 *Using Alarms to Report Error Conditions at Runtime* for
 information about supported alarm types.
- Filter by Pin, Pin Group or Alarm Type —Type to filter the
 list of alarms by Pin, Pin Group or Alarm Type. Enter
 pin:<text> ,
 pingroup:<text> or
 alarm: to restrict search to Pin, Pin Group or Alarm
 type column.
- Pin Group —A comma-separated list of all Pin Groups to
 which the pin belongs.
- Behavior —Specifies the action that TSM will execute if the alarm is raised. When you
 enable alarms and specify Log , Fail step and any tests in step ,
 or Error step and bin part to alarm bin in the Behavior drop-down menu,
 TSM displays a warning in the Output pane for each raised alarm. Select
 one of the following behaviors:
  - Ignore —Ignore the alarm.
  - Log —Log the alarm in the STDF
 Log file. TSM logs alarm information in the following STDF
 Log file records based on the test result data acquired:
    - Parametric Test Records (PTR) or Functional Test Records
 (FTR)—Logs the alarm type and associated pin in the ALARM_ID
 field.
    - Datalog Text Record (DTR)—Creates a new record for each alarm
 occurrence and displays the alarm type and associated pin.
    - Test Results Record (TSR)—Increments the alarm count stored in
 the ALRM_CNT field.
  - Fail step and any tests in step —Set the step status to Failed and assign the default fail bin to the DUT.
 Note If the test is part of a Semiconductor Multi Test step,
 all tests in the step are set to Failed and the fail bin
 you specified for the Semiconductor Multi Test step is assigned to the DUT. If no bin is
 specified, the default fail bin is assigned to the DUT.
  - Error step and bin part to alarm bin —Set the step status to
 Error and generate a run-time error. If
 executing in the sequence editor, TSM will launch the Semiconductor
 Module Run-Time Error dialog box. The alarm bin you specified in the
 bin definitions file for the test program is assigned to the
 DUT. Note If
 the test is part of a Semiconductor Multi Test step, all tests in
 the step are set to Failed.

Parent topic:

Test Program Editor (TSM)

Related tasks:

- Using Alarms to Report Error Conditions at Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=assign-values-to-pat-algorithm.html language=enus -->
## TOPIC 00013: Assigning Values to PAT Algorithm Settings

- bundle_id: `teststand-semiconductor-module`
- source_path: `assign-values-to-pat-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/assign-values-to-pat-algorithm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the PAT Algorithm Settings panel of the Test Program Editor to set values for the PAT algorithm setting so that each test program can use unique values.

### Assigning Values to PAT Algorithm Settings

Use the PAT Algorithm Settings panel of the Test Program Editor to set values for the PAT algorithm setting so that each test program can use unique values.

Parent topic:

Part Average Testing Algorithm Settings (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=asynchronous-analysis.html language=enus -->
## TOPIC 00014: Asynchronous Analysis (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `asynchronous-analysis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/asynchronous-analysis.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates a test program that must perform lengthy analysis on data acquired from an instrument. The test program performs the analysis in an asynchronous thread. The following two figures demonstrate how performing the analysis asynchronously to the data acquisition reduces the over

### Asynchronous Analysis (TSM)

This example demonstrates a test program that must perform lengthy analysis on data
 acquired from an instrument. The test program performs the analysis in an asynchronous
 thread. The following two figures demonstrate how performing the analysis asynchronously to
 the data acquisition reduces the overall duration of the test program.

The following table shows a test program thread usage without asynchronous analysis.

| Site 1 | Acquire Data1 | Analyze Data1 | Acquire Data2 | Analyze Data2 | Acquire Data3 | Analyze Data3 |
| --- | --- | --- | --- | --- | --- | --- |
| Site 1 | Acquire Data1 | Analyze Data1 | Acquire Data2 | Analyze Data2 | Acquire Data3 | Analyze Data3 |
| Site 1 | Acquire Data1 | Analyze Data1 | Acquire Data2 | Analyze Data2 | Acquire Data3 | Analyze Data3 |
| Site 1 | Acquire Data1 | Analyze Data1 | Acquire Data2 | Analyze Data2 | Acquire Data3 | Analyze Data3 |

The following table shows a test program thread usage with asynchronous
 analysis.

| Site 1 | Acquire Data1 | Acquire Data2 | Acquire Data3 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Analyze Data1 | Analyze Data2 | Analyze Data3 |  |  |  |
| Site 2 | Acquire Data1 | Acquire Data2 | Acquire Data3 |  |  |  |
|  | Analyze Data1 | Analyze Data2 | Analyze Data3 |  |  |  |
| Site 3 | Acquire Data1 | Acquire Data2 | Acquire Data3 |  |  |  |
|  | Analyze Data1 | Analyze Data2 | Analyze Data3 |  |  |  |
| Site 4 | Acquire Data1 | Acquire Data2 | Acquire Data3 |  |  |  |
|  | Analyze Data1 | Analyze Data2 | Analyze Data3 |  |  |  |

| Example File Locations | <TestStand Public>\\Examples\\NI_SemiconductorModule\\Test Optimizations\\Asynchronous Analysis\\LabVIEW\\Asynchronous Analysis.seq |
| --- | --- |
| Highlighted Features | Multisite Asynchronous code modules |
| Major API | None |
| Prerequisites | You must have the LabVIEW Development System installed, and you must configure the LabVIEW Adapter to use the LabVIEW Development System. This example uses the Batch process model. |

1. Complete the following steps to review the pin map file associated with the test
 program.
  1. Select Semiconductor Module»Edit Pin Map File , click the Edit Pin Map File button on the TSM
 toolbar, or launch the Test Program Editor and click the Open
 file for edit button located to the
 right of the Pin Map File Path display on the Pin Map panel to launch
 the Pin Map Editor. Open the <TestStand
 Public> \Examples\NI_SemiconductorModule\Test
 Optimizations\Asynchronous Analysis\LabVIEW\Asynchronous
 Analysis.pinmap file in the Pin Map Editor. The pin map
 file defines the following information:
    - One DUT pin named A .
    - One custom instrument named Dev1 with an
 instrumentTypeId attribute value of
 CustomInstrument and one channel group that
 contains four channels.
    - Four sites on the tester.
    - A series of connections for each site, in which each connection
 specifies DUT pin A , a site number, the custom
 instrument Dev1 , and an instrument
 channel.
2. Open <TestStand
 Public> \Examples\NI_SemiconductorModule\Test
 Optimizations\Asynchronous Analysis\LabVIEW\Asynchronous
 Analysis.seq and review the steps in the sequence.
  - Each Acquire Test Data step is a Semiconductor Multi Test Step that runs
 a LabVIEW code module that acquires data for each site and exports a
 reference to the data to a local variable. Because the pin map specifies
 a channel for each site connected to pin A , the test
 runs one instance of the code module that acquires data for all four
 sites.
  - Each Analyze Test Data step runs a VI asynchronously to perform analysis
 on the data acquired in the preceding Acquire Test Data step. TestStand
 passes to the VI the local variable that contains the reference to the
 test data and stores the analysis result the VI returns in another local
 variable.
  - Each Wait for Analysis of Test Data step waits for the asynchronous
 thread running the analysis VI to complete.
  - Each Evaluate Analysis Result step is a Semiconductor Multi Test step
 with no code module. The step evaluates the value of the local variable
 that contains the analysis result against a set of limits. The Tests tab
 in the Step Settings pane shows the limits. If the value of the analysis
 result is within the limits, the test passes. Otherwise, the test fails.
3. On the Sequences pane, select the ProcessSetup sequence. The
 Launch Resource Usage Profile step launches the Execution Profiler to
 demonstrate how the analysis threads run in parallel to the data acquisition
 threads. The Open and Store Instrument Sessions step in this sequence
 initializes the custom instrument.
4. On the Sequences pane, select the ProcessCleanup sequence. The
 Close Instrument Sessions step in this sequence closes the custom instrument
 session.
5. Open <TestStand
 Public> \Examples\NI_SemiconductorModule\Test
 Optimization\Asynchronous Analysis\LabVIEW\Asynchronous
 Analysis.lvproj to review the code modules the test program
 uses.
6. Complete the following steps to execute the test program.
  1. Select Configure»Model Options to launch the Model Options dialog box.
  2. Set the Number of Test Sockets to
 4 and click OK to close the
 Model Options dialog box.
  3. Click the Start Lot button on the TSM
 toolbar to run the test program.
  4. The Execution Profiler automatically launches when execution begins. The
 profiler shows each thread running in the test program and demonstrates
 that the analysis steps are running in parallel with the acquisition
 steps.

Parent topic:

TSM Example Programs

<!--NI_TOPIC bundle=teststand-semiconductor-module path=basic-test-program-labview.html language=enus -->
## TOPIC 00015: Tutorial: Exploring a Basic Semiconductor Test Program with LabVIEW

- bundle_id: `teststand-semiconductor-module`
- source_path: `basic-test-program-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/basic-test-program-labview.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Open an existing sequence file and configure it to create a basic semiconductor test program with LabVIEW. Completed solution files are located in the <TestStand Public>\Tutorial\NI_SemiconductorModule\Basic Test Program\LabVIEW\Solution directory. Open <TestStand Public>\Tutorial\NI_SemiconductorMo

### Tutorial: Exploring a Basic Semiconductor Test
 Program with LabVIEW

Open an existing sequence file and configure it to create a basic semiconductor test
 program with LabVIEW.

Note

<TestStand
 Public>

\Tutorial\NI_SemiconductorModule\Basic Test
 Program\LabVIEW\Solution

1. Open <TestStand
 Public>\Tutorial\NI_SemiconductorModule\Basic Test
 Program\LabVIEW\Basic Test Program.seq. 
 This sequence file contains the following sequences:MainSequence—Contains a single test step that performs
 a continuity test on all pins.
 ProcessSetup—Simulates instrument initialization.
 ProcessCleanup—Simulates instrument clean up.
2. Complete the following steps to specify a pin map file to define the
 instrumentation on the tester, define the pins on the DUT, and define how the
 DUT pins are connected to the tester instrumentation for each test site.
  1. Select Semiconductor Module»Edit Test Program: Basic Test Program.seq or click the Edit Test Program: Basic Test
 Program.seq[IMAGE alt='image' src='GUID-87E58653-7373-4FF8-A391-D94F811EC4FE-a5.png'] button on the TSM
 toolbar to launch the Test
 Program Editor for the sequence file.
  2. Select the Pin Map panel and enter Basic Test
 Program.pinmap in the Pin Map File
 Path control. The file name you enter is a relative path
 from the sequence file to the pin map file, Basic Test
 Program.pinmap, which is located in the same directory as
 the sequence file. Click the Open file for edit[IMAGE alt='image' src='GUID-F141357B-5D8A-42A4-99E9-9C309A69F0FF-a5.png'] button located to
 the right of the Pin Map File Path display to open the Basic
 Test Program.pinmap file in the Pin
 Map Editor. Review the pin map and click
 OK to close the pin map editor.
  3. Click OK to close the Test Program
 Editor.
  4. After you specify a pin map file,
 select the MainSequence sequence in the sequence file.
 This sequence contains the Continuity Test step, which is an instance of
 the Semiconductor Multi Test step type and uses the LabVIEW
 Adapter.
  5. Select the Continuity Test step and select the Tests
 tab of the Step Settings pane. You can use the Tests tab to define tests
 for individual pins or pin groups, and you can write code modules that
 refer to pin or pin group names without needing to know how each pin is
 connected to an instrument.
3. Complete the following steps to specify a bin definitions file to define the
 hardware bins and software bins, define how the software bins relate to hardware
 bins, and define the default software bins in the test program. 
 
 After you specify a bin definitions file, you can use the Tests tab of
 the Step Settings pane to define a software bin for each test.
  1. Select Semiconductor Module»Edit Test Program: Basic Test Program.seq.
  2. Select the Bin Definitions panel and enter
 Basic Test Program.bins in the Bin
 Definitions File Path control. The file name you enter
 is a relative path from the sequence file to the bin definitions file,
 Basic Test Program.bins, which is located in
 the same directory as the sequence file.
  3. Click the Open file for edit[IMAGE alt='image' src='GUID-1C184611-6EBF-4EA5-B526-282013078C14-a5.png'] button located to
 the right of the Bin Definitions File Path display to open the
 Basic Test Program.bins file in the Bin
 Definitions Editor.
  4. Review the bin definitions and click OK to close
 the Bin Definitions Editor.
  5. Click OK to close the Test Program
 Editor.
4. Complete the following steps to create a test program configuration and specify
 a test limits file to load limits values into Semiconductor Multi Test step
 tests at run time. When you use this technique, you can use the same test
 program with multiple configurations that each specify different limits for the
 tests.
  1. Select Semiconductor Module»Edit Test Program: Basic Test Program.seq.
  2. Select the Test Limits Files panel and click the
 Add Test Limits File button to add a new file
 reference to the test program.
  3. Enter Production Limits as the name to identify
 the new test limits file in the test program.
  4. Enter ProductionLimits.txt in the
 Test Limits File Path control. The file name
 you enter is a relative path from the sequence file to the test limits
 file, ProductionLimits.txt, which is located in
 the same directory as the sequence file.
  5. Select the Configurations panel and click the
 Add Configuration button to add a new
 configuration to the test program.
  6. Enter Production as the name of the
 configuration.
  7. Select the newly created Production panel. Each
 configuration you specify uses a corresponding Configuration panel that contains a table of the test
 conditions in the test program and fields for configuring the test
 limits file for the configuration.
  8. Select Production Limits in theTest
 Limits File control.
5. Complete the following steps to add a test condition to the test program and
 specify a value for the test condition in the Production configuration.
  1. Select the Configuration Definition panel and
 click the Add Condition button to add a new test
 condition to the test program.
  2. Select TestFlowId from the Standard
 Condition option and click the
 Add button to add a new test condition for
 which each configuration can provide a unique value.
  3. Select the Production panel and enter Production
 for the value of the TestFlowId test condition in the table.
  4. Click OK to close the Test Program
 Editor.
6. Complete the following steps to obtain the value of the TestFlowId test
 condition in the test program.
  1. Select the ProcessSetup sequence.
  2. Add a Get Test Information step after the Open Sessions step.
  3. On the Step Settings pane, click the Get Test
 Information tab.
  4. Enter TestFlowId for the
 Name in the first row of the table.
  5. Set the Destination Expression to
 Locals.Flow.
  6. Highlight and right-click Locals.Flow and select Create "Locals.Flow"»String from the context menu to create a new local variable.
  7. Add a Message Popup step after the Get Test Information step in the
 Setup step group.
  8. On the Step Settings pane, click the Text and
 Buttons tab.
  9. Set the Message Expression to "Starting test flow: " +
 Locals.Flow.
7. Complete the following steps to specify a code module for the Continuity Test
 step.
  1. Select the MainSequence sequence and the Continuity
 Test step.
  2. On the Step Settings pane, click the Module
 tab.
  3. Click the Browse for VI[IMAGE alt='image' src='GUID-81ED2825-036D-43C5-8CEA-ABA4F4464B14-a5.png'] button located to
 the right of the VI Path control.
  4. Browse to <TestStand
 Public>\Tutorial\NI_SemiconductorModule\Basic
 Test Program\LabVIEW\Code Modules\Continuity Test.vi and
 click Open. Select the Use a relative
 path for the file you selected option when prompted and
 click OK.
  5. In the VI Parameter Table, configure the following parameter
 values: 
 Parameter
ValueSemiconductor Module Context
Step.SemiconductorModuleContext
Pins
{"AllPins"}
8. Save the sequence file.
9. Complete the following steps to configure the Built-in Simulated Handler Driver.
  1. Select Semiconductor Module»Configure Station or click the Configure Station[IMAGE alt='image' src='GUID-2B9000DD-463B-439C-8854-FD935DD21D0F-a5.png'] button on the TSM
 toolbar to launch the Configure Station Settings dialog box.
  2. On the General tab of the Configure Station Settings
 dialog box, place a check-mark in the Enable Handler/Prober
 Driver (Real or Simulated) check-box.
  3. Select Built-in Simulated Handler Driver from
 the Handler/Prober Driver drop-down menu.
  4. Click the Configure Handler/Prober Driver button
 to launch the Configure Built-in Simulated Handler dialog
 box.
  5. Set the Number of DUTs to Test option to
 10 to specify how many DUTs the simulated lot
 contains and click OK to close theConfigure Built-in Simulated Handler dialog box.
  6. Select the Advanced tab in the Configure Station Settings
 dialog box and click the Result Processing button
 to launch the Result Processing dialog box.
  7. Enable the Debug Test Results Log result
 processing plug-in.
  8. Disable the TestStand Report result processing
 plug-in.
  9. Enable the Display option for the Lot Summary
 Report result processing plug-in.
  10. Click OK to close the Result Processing dialog
 box, and click OK to close the Configure Station
 Settings dialog box.
10. Complete the following steps to configure a lot to run.
  1. Select Semiconductor Module»Configure Lot or click the Configure Lot[IMAGE alt='image' src='GUID-D3E4D875-0906-4F98-96C8-0B05B5695284-a5.png'] button on the TSM toolbar to launch the
 Configure Lot Settings dialog box.
  2. Select Production in the Test Program
 Configuration option.
  3. Click OK to close the Configure Lot
 Settings dialog box. 
 Note You can also use the Active Configuration
 drop-down menu on the TSM toolbar to set the configuration. TSM uses
 previously set values for the other lot settings that appear in the
 Configure Lot Settings dialog box.
11. Click the Show Lot Statistics Viewer button [IMAGE alt='image' src='GUID-9528D0A6-B4E2-400F-8BA8-59B10F090872-a5.png'] on the TSM toolbar to
 launch a floating window that shows the binning results of the test program
 execution. The execution control buttons, such as Start/Resume
 Lot and End Lot and the
 Configuration drop-down menu are also available in
 the Lot Statistics Viewer for convenience.
12. Click the Start Lot button on the TSM toolbar or in the
 Lot Statistics Viewer to execute the test program. The test program launches a
 dialog box that shows the value of the TestFlowId test condition. Click
 OK to close the dialog box. TestStand generates and
 displays the Lot Summary Report on the Report pane of the Execution window.
 Review the results of the lot.
13. Click the Active Report button to switch to the Debug
 Test Results Log and review the results of each test. 
 Note The Production configuration overrides the test limits the sequence
 specifies. The ProductionLimits.txttest limits file
 provides the test limits values to use for each test instead of the values
 entered in the Semiconductor Multi Test step.
14. Close the Execution and Sequence File
 windows.

Parent topic:

Getting Started with TSM

Related concepts:

- Test Program Editor (TSM)
- Pin Map Panel
- Pin Map Editor (TSM)
- Semiconductor Multi Test Step
- Tests Tab
- Bin Definitions Panel
- Bin Definitions Editor (TSM)
- Test Limits Files Panel
- Configurations Panel
- Configuration Panels
- NI Built-in Simulated Handler Driver (TSM)
- Configure Station Settings Dialog Box (TSM)
- General Tab
- Configure Built-in Simulated Handler Dialog Box (TSM)
- Advanced Tab
- Configure Lot Settings Dialog Box (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=bin-definitions-editor.html language=enus -->
## TOPIC 00016: Bin Definitions Editor (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `bin-definitions-editor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/bin-definitions-editor.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Bin Definitions Editor to view, create, modify, and save bin definitions files instead of editing the XML files directly. Use the Bin Definitions panel in the Test Program Editor to specify a bin definitions file for a test program. Select Semiconductor ModuleEdit Bin Definitions File or cli

### Bin Definitions Editor (TSM)

Use the Bin Definitions Editor to view, create, modify, and save bin definitions files instead of
 editing the XML files directly. Use the Bin Definitions panel in the Test
 Program Editor to specify a bin definitions file for
 a test program.

Select Semiconductor Module»Edit Bin Definitions File or click the Edit Bin Definitions
 File button on the TSM toolbar to launch the Bin Definitions
 Editor. Alternatively, you can select Semiconductor Module»Edit Test Program and then select Bin
 Definitions in the Test Program Editor to launch
 the Bin Definitions panel. Click the Open file for
 edit[IMAGE alt='image' src='GUID-1C184611-6EBF-4EA5-B526-282013078C14-a5.png'] button to launch
 the Bin Definitions Editor.

The Bin Definitions Editor validates the fields of the hardware and software tabs and uses a red
 error icon on the tab and in the corresponding fields to indicate
 errors to resolve, such as duplicate bin numbers, duplicate bin
 names, or software bins without assigned hardware bins. Hover over
 the error icon to display a tooltip with specific error information.
 You must resolve errors before you can save the file or close the
 editor using the OK button. The editor does
 not load files that are invalid according to the Bin Definitions schema.

When you close the editor, a dialog box prompts you to discard changes or return to the editor to save or cancel the changes to the bin definitions file if the file has been edited since you opened it in the editor.

#### Configuring Bin
 Definitions Files

The Bin Definitions Editor includes the
 following options and tabs:

- Bin Definitions File Path —Specifies the
 bin definitions file loaded.
- Undo —Removes the last edit made.
- Redo —Reinstates the last edit
 removed.
- Open —Launches the Select Bin Definitions
 File dialog box, in which you can browse to the bin
 definitions file to load.
- Save —Displays a context menu that
 includes a Save option to save the
 file to the current path and a Save
 As option to launch as Save As dialog
 box. The Save button is disabled when
 validation errors exist in the bin definitions file.
- New —Creates a new bin definitions file.
 If the file currently open in the editor has unsaved
 changes, a dialog box prompts you to discard the changes or
 return to the editor to save or cancel the changes to the
 file before creating a new file.
- Hardware Bins tab —Displays an editable
 table that defines a set of hardware bins. You can edit the
 cells directly or copy and paste rows of the table. The
 table includes the following sortable columns:
  - Number —Specifies the
 hardware bin number.
  - Name —Specifies the
 hardware bin name.
  - Type —Specifies an
 existing bin type. Options include Pass, Fail, and
 Other.
- Software Bins tab —Displays an editable
 table that defines a set of software bins. You can edit the
 cells directly or copy and paste rows of the table. The
 table includes the following sortable columns:
  - Number —Specifies the
 software bin number.
  - Name —Specifies the
 software bin name.
  - Hardware Bin —Specifies an
 existing hardware bin.
  - Type —Displays the
 existing hardware bin type. The specified hardware
 bin determines the value of this field.
- Default Bins tab —Displays the following
 options for the default bins to use when no bin is assigned
 to a DUT:
  - Default Error —The
 software bin to which TSM assigns a DUT when the
 main test sequence errors. The software bin must
 be associated with a hardware bin of the Fail or
 Other type.
  - Default Pass —The software
 bin to which TSM assigns a DUT when the main test
 sequence passes and the DUT has not yet been
 assigned to a bin. The software bin must be
 associated with a hardware bin of the Pass
 type.
  - Default Fail —The software
 bin to which TSM assigns a DUT when the main test
 sequence fails and the DUT has not yet been
 assigned to a bin. The software bin must be
 associated with a hardware bin of the Fail or
 Other type.
  - Alarm —The software bin to
 which TSM assigns a DUT when an alarm is raised
 and the behavior assigned to the alarm is
 Error step and bin part to alarm
 bin . You can assign the alarm behavior
 from the Alarms panel in the Test Program Editor.
- Add Bin —Adds a new hardware bin when on
 the Hardware Bins tab or a new software bin when on the
 Software Bins tab.
- Delete Bin —Deletes the selected bin or
 bins.
- Software Bins Only —Hides the Hardware
 Bins tab to specify only software bins, which can be helpful
 when a tester configuration does not support hardware bins,
 such as for wafer testing. Enabling this option clears the
 hardware bins. Use Undo to recover hardware bin information.
 Disable this option to return to normal editing mode. The
 editor saves this setting in the bin definitions file.

Parent topic:

Environment Reference

<!--NI_TOPIC bundle=teststand-semiconductor-module path=bin-definitions-file-xml-structure.html language=enus -->
## TOPIC 00017: Bin Definitions File XML Structure (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `bin-definitions-file-xml-structure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/bin-definitions-file-xml-structure.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The bin definitions XML schema, located at <TestStand>\Components\Schemas\NI_SemiconductorModule\BinDefinitions.xsd, defines the following structure for a bin definitions XML file: Legend Root element> Element Attribute BinDefinitions schemaVersion—Specifies the version of the schema file. softwareB

### Bin Definitions File XML Structure
 (TSM)

The bin definitions XML schema, located at <TestStand>\Components\Schemas\NI_SemiconductorModule\BinDefinitions.xsd,
 defines the following structure for a bin definitions XML file:

| Legend |
| --- |
| Root element> |
| Element |
| Attribute |

[IMAGE alt='image' src='GUID-AF15E1E5-268F-45F0-B835-47595C4B20C3-a5.png']

BinDefinitions

- schemaVersion —Specifies the version of the schema
 file.
- softwareBinsOnlyMode —(Optional) Specifies whether the bin
 definitions editor displays only software bins and no hardware bins. The bin
 definitions editor sets this attribute when you enable the Software Bins Only option. This option can be useful when
 you perform wafer testing using software bins exclusively. When this
 attribute is True , the bin definitions editor ensures that
 a unique hardware bin exists for each software bin.
- HardwareBins —Specifies the hardware bins available
 to the handler or prober.
  - Bin —Specifies an individual hardware
 bin.
    - name —(Optional) A short descriptive
 name for the hardware bin. TSM stores the name in the
 Hardware Bin Record (HBR) of a Standard Test Data Format
 (STDF) log file.
    - number —A unique number the handler or
 prober uses to place the device under test (DUT). The number
 must be a valid 16-bit unsigned integer.
    - type —Specifies a value of
 Pass , Fail , or
 Other .
- SoftwareBins —Specifies the software bins to define
 for the test program.
  - errorBin —The software bin number TSM assigns
 to a DUT when the main test sequence errors. The software bin must
 be associated with a hardware bin of the Fail or
 Other type.
  - defaultFailBin —(Optional) The software bin
 number TSM assigns to a DUT when the main test sequence fails and a
 bin has not yet been assigned to the DUT. The software bin must be
 associated with a hardware bin of the Fail or
 Other type. You can omit the default fail bin
 from the bin definitions file. In this case, TSM uses the
 errorBin for the
 defaultFailBin .
  - defaultPassBin —The software bin number TSM
 assigns to a DUT when the main test sequence passes and a bin has
 not yet been assigned to the DUT. The software bin must be
 associated with a hardware bin of the Pass 
 type.
  - Bin —Specifies an individual software
 bin.
    - name —(Optional) A short descriptive
 name for the software bin. The Semiconductor Multi Test step
 displays this name in the Software
 Bin column on the Tests tab when you select
 the software bin for a DUT. TSM stores the name in the
 Software Bin Record (SBR) of an STDF log file.
    - number —A unique number to identify
 the software bin. The number must be a valid 16-bit unsigned
 integer.
    - hardwareBin —The hardware bin number
 to associate with the software bin. The type of the software
 bin is inferred from the associated hardware bin. The
 Software Bin column on the Tests tab of the Semiconductor
 Multi Test step lists only software fail bins. TSM ensures
 that the test status of a DUT corresponds to the type of
 software bin assigned to the DUT. For example, TSM reports a
 run-time error if a test program causes TSM to assign a
 software pass bin to a failed DUT.

Parent topic:

Binning DUTs Based on Test Results (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=bin-definitions-panel.html language=enus -->
## TOPIC 00018: Bin Definitions Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `bin-definitions-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/bin-definitions-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Bin Definitions panel contains the following options: Bin Definitions File Path—Specifies the pathname of the bin definitions file to use in the test program. A red exclamation point indicates that the file is invalid or that the file does not conform to the bin definitions XML schema. A tooltip

### Bin Definitions Panel

The Bin Definitions panel contains the following options:

- Bin Definitions File Path —Specifies the pathname of the bin definitions file to use in
 the test program. A red exclamation point indicates that
 the file is invalid or that the file does not
 conform to the bin definitions XML schema. A
 tooltip displays the error message. If errors exist
 in the file, you make changes in the dialog box, and
 click OK, TSM commits those
 changes. Do not proceed without reviewing the errors
 in the bin definitions file.
- Open file for edit 
 —Launches the bin definitions file in the Bin Definitions Editor.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=binning-duts.html language=enus -->
## TOPIC 00019: Binning DUTs Based on Test Results (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `binning-duts.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/binning-duts.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A handler moves each tested device under test (DUT) from its test site to an appropriate physical bin (hardware bin), depending on the test results. The tester software assigns each tested DUT to a hardware bin and communicates with the handler to ensure that the handler places the DUT in the approp

### Binning DUTs Based on Test Results (TSM)

A handler moves each
 tested device under test (DUT) from its test site to an appropriate
 physical bin (hardware bin), depending on the test results. The
 tester software assigns each tested DUT to a hardware bin and
 communicates with the handler to ensure that the handler places the
 DUT in the appropriate hardware bin.

Typically, the handler places passed DUTs in one or more hardware bins, depending on the grade of the DUT, and places failed
 DUTs in multiple hardware bins, depending on the type or condition
 of failure.

Because handlers have a limited quantity of hardware bins available, the tester software also
 assigns each DUT to a virtual bin defined in software (software bin)
 to provide a more detailed classification of test results. The
 tester software records the software bin for each DUT in a Standard
 Test Data Format (STDF) log file for additional analysis after
 testing completes. When wafer testing, the prober assigns hardware
 bins to individual die based on the test results. Because probers
 generally do not have the same limitations as handlers on the number
 of hardware bins they support, the set of software bins can be
 identical to the set of hardware bins when testing wafers. Use the
 Bin Definitions Editor and enable the Software Bins
 Only option to ensure that software bins and
 hardware bins are the same.

#### TSM
 Implementation

Use the Bin Definitions Editor to define the
 software bins and hardware bins for the test program, define how the
 software bins relate to hardware bins, and define the default
 software bins in the test program. The TSM installs a bin definitions XML schema, located at
 <TestStand>\Components\Schemas\NI_SemiconductorModule\BinDefinitions.xsd,
 which you can use to create a valid bin definitions file. Use the
 Bin Definitions File Path control on
 the Bin Definitions panel of the Test Program Editor to specify the bin
 definitions file to use with the test program.

The test
 program refers only to software bins. Because each software bin is
 associated with a hardware bin, the tester assigns a hardware bin to
 a DUT when it assigns the associated software bin to the
 DUT.

Each instance of the Semiconductor Multi Test step contains
 one or more tests for which you can specify the software bin to
 assign to the DUT when a test fails. When you specify a valid bin
 definitions file on the Bin Definitions panel of the Test Program
 Editor, you can use the Software Bin column on the Tests tab to select a software bin
 defined in the bin definitions file.

Note

In addition, you can use a Set and Lock Bin step to arbitrarily
 assign a software bin to a DUT. Use the Bin
 Expression control on the Set and Lock Bin tab to specify an
 expression that evaluates at run
 time to a valid software bin number defined in the bin definitions
 file. The step assigns a software bin to the DUT and locks the bin
 by preventing tests on subsequent Semiconductor Multi Test steps
 from assigning a bin to the DUT when the test fails. You can use the
 Set and Lock Bin step to implement grading in the test
 program.

#### Assigning Default
 Fail Bins and Pass Bins

- A test program sequence fails for any reason
- The test program does not set the bin with either a
 failing test on a Semiconductor Multi Test 
 step or the Set And Lock Bin step

Set and Lock Bin

RuntimeSettings.ini

1. Open the RuntimeSettings.ini.example file
 located in the <TestStand Application
 Data>\Cfg\NI_SemiconductorModule 
 directory. You can use any text editor to open and edit this
 file.
2. Set the value of the
 BinPassingPartsWithNoTestsToErrorBin 
 setting to true .
3. Select File»Save as . Rename the modified file to
 RuntimeSettings.ini . Save the new
 RuntimeSetting.ini file to the
 <TestStand Application
 Data>\Cfg\NI_SemiconductorModule 
 directory.

<!--NI_TOPIC bundle=teststand-semiconductor-module path=builtin-sim-handler-driver.html language=enus -->
## TOPIC 00020: NI Built-in Simulated Handler Driver (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `builtin-sim-handler-driver.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/builtin-sim-handler-driver.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When developing, testing, or debugging a semiconductor test program, the test developer might not have access to a real handler or prober. In such cases, the test developer can use the NI Built-in Simulated Handler Driver to verify that the test program behaves correctly without a handler or prober.

### NI Built-in Simulated Handler Driver (TSM)

When developing, testing, or debugging a semiconductor test program, the test developer might not have access to a real handler or prober. In such cases, the test developer can use the NI Built-in Simulated Handler Driver to verify that the test program behaves correctly without a handler or prober.

Note

#### Enabling and Configuring the NI Built-in
 Simulated Handler Driver

Complete the following steps to
 enable and configure the NI Built-in Simulated Handler
 Driver.

Note

1. (TestStand Sequence Editor) Select Semiconductor Module»Configure Station to launch the default Configure Station Settings dialog box.
 (Operator Interface) Click the
 Configure Station
 button.
2. In the Enable Handler/Prober Driver (Real or
 Simulated) section on the General tab of the Configure Station
 Settings dialog box, select Built-in Simulated
 Handler Driver in the
 Handler/Prober Driver option
 to enable the NI Built-in Simulated Handler Driver for the
 test program. TSM uses only one active handler driver
 sequence file at a time because the lot of DUTs (test lot)
 can use just one type of handler at a time.
3. Click Configure Handler/Prober to launch
 the Configure Built-in Simulated Handler dialog
 box.

Parent topic:

Configuring Handler or Prober Support for a Test Program (TSM)

Related concepts:

- Configuring Handler or Prober Support for a Test Program (TSM)
- Start of Test Dialog Box (TSM)
- End of Test Dialog Box (TSM)
- Configure Station Settings Dialog Box (TSM)
- General Tab
- Configure Built-in Simulated Handler Dialog Box (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=changing-report-orientation.html language=enus -->
## TOPIC 00021: Changing Report Orientation

- bundle_id: `teststand-semiconductor-module`
- source_path: `changing-report-orientation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/changing-report-orientation.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, the Debug Test Results Log uses portrait orientation. Landscape orientation uses wider columns for tests with long test numbers or test names. Complete the following steps to change the report orientation of the Debug Test Results Log. Launch the Debug Test Results Log Options dialog box

### Changing Report Orientation

By default, the Debug Test Results Log uses portrait orientation. Landscape orientation uses wider columns for tests with long test numbers or test names. Complete the following steps to change the report orientation of the Debug Test Results Log.

1. Launch the Debug Test Results Log Options
 dialog box.
2. Use the drop-down menu of the Report Orientation option to select Portrait or Landscape .

Parent topic:

Debug Test Results Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=cleanup-handler-entry-point.html language=enus -->
## TOPIC 00022: Cleanup Handler/Prober Driver Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `cleanup-handler-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/cleanup-handler-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Cleanup entry point to perform required handler/prober finalization tasks. The Cleanup entry point accepts the following parameters: Parameter Type Description HandlerDriverData Input or Output Container that stores handler-specific settings, prober-specific settings, or run-time data. In a

### Cleanup Handler/Prober Driver Entry Point (TSM)

Use the Cleanup entry point to perform required handler/prober finalization tasks.

The Cleanup entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| HandlerDriverData | Input or Output | Container that stores handler-specific settings, prober-specific settings, or run-time data. In a handler/prober driver sequence file, you can modify the default structure of this parameter, such as by changing the data type from the default Container to a custom container data type. However, the Configure entry point must create, and optionally assign, each field of this parameter using the TestStand API, such as the PropertyObject.NewSubProperty method or a PropertyObject Set value method, such as SetValNumber.Do not enable the Check Type option for this parameter. Right-click the parameter and remove the checkmark from Check Type in the context menu to disable the Check Type option. |
| SemiconductorModuleManager | Input or Output | Object reference to an instance of a Semiconductor Module Manager. Use this object reference with the TSM Application API to get information about the currently configured lot. |

Parent topic:

Handler/Prober Driver Entry Points (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=closing-switch-sessions.html language=enus -->
## TOPIC 00023: Closing Switch Sessions (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `closing-switch-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/closing-switch-sessions.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the ProcessSetup callback sequence of a test program, you must close all instrument sessions and switch sessions stored in the Semiconductor Module context. Refer to the Close Switch Sessions VI in the Switching example for an example of how to clean up switch sessions. Pass NISimulatedMultiplexe

### Closing Switch Sessions (TSM)

In the ProcessSetup callback sequence of a test program, you must close all
 instrument sessions and switch sessions stored in the Semiconductor Module context.
 Refer to the Close Switch Sessions VI in the Switching example
 for an example of how to clean up switch sessions.

Pass NISimulatedMultiplexer for the Multiplexer Type ID
 parameter of the Get All Switch
 Sessions VI to obtain an array of switch
 sessions from the pin map. In a For Loop, iterate
 through each session in the Session Data array and
 close the session. Because the session data is an
 array of variant data types to allow for any
 session type, use the Variant To Data function
 inside the For Loop to convert the variant data
 type to the correct switch session type.

Parent topic:

Switching (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=code-module-development.html language=enus -->
## TOPIC 00024: Code Module Development (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `code-module-development.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/code-module-development.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Semiconductor Multi Test and the Semiconductor Action steps call a single code module for all the sites that synchronize at a certain location, which means the code module executes on multiple sites at the same time. The Semiconductor Multi Test or Semiconductor Action step creates a Semiconduct

### Code Module Development (TSM)

The Semiconductor Multi
 Test and the Semiconductor Action steps call a single code module
 for all the sites that synchronize at a certain location, which
 means the code module executes on multiple sites at the same time.
 The Semiconductor Multi Test or Semiconductor Action step creates a
 SemiconductorModuleContext object that
 contains the information about the sites on which the code module
 executes. Pass the Step.SemiconductorModuleContext
 property to the code module to use the TSM Code Module API.

#### Code Module
 Development Guidance

As you develop each part of the test
 program, consider the functionality that belongs in code modules and
 the functionality that belongs in test sequences. In general, use
 the following guidelines:

- Code Modules—Use code modules written in LabVIEW or in .NET for
 instrument driver calls to configure instruments and acquire
 data. Additionally, use code modules for other code
 necessary to perform a specific DUT test or other specific
 actions so you can reuse the code modules in other test
 programs.
- Test Sequences—Use test sequences to call code modules and
 evaluate results the code modules generate.

#### Use Test Sequence for
 Test Flow

Use the TSM test sequence instead of code
 modules to determine test flow. For example, if the test program
 requires you to execute a certain test only if a previous test
 fails, ensure that the test sequence contains the logic for
 executing tests in a specific order. Use this development strategy
 to make the flow of the test program more apparent to other test
 engineers and to help generalize code modules for potential reuse in
 other test programs.

#### Evaluate Results in
 TSM

Use code modules to execute specific tests, but do not
 use code modules to evaluate numeric results of tests. Use the
 Publish Data TSM Code Module API to transfer test measurement data to the
 Semiconductor Multi Test step.
 Configure the Semiconductor Multi Test step to evaluate the
 measurement against a set of limits or a specific value. Because
 test limits might change throughout the life cycle of a DUT,
 evaluating the measurements in TSM rather than in code modules
 enables you to more easily adjust the test limits as needed.
 Additionally, using this technique helps to generalize code modules
 for potential reuse in other test programs.

You might need to
 perform calculations on the test measurements before evaluating the
 data because TSM does not offer the functionality you need or
 because you need to attain maximum performance for a
 processor-intensive calculation. For example, use a code module to
 calculate the FFT of a waveform, and use a Semiconductor Multi Test
 step in TSM to perform the final test evaluation.

#### Implement Loops in
 Code Modules for High Performance

Implement loops in code
 modules when execution speed is critical. For example, if a test
 needs to sweep an instrument parameter over a range of values as
 quickly as possible, use a For loop in a code module rather than
 executing the loop in TSM. Additionally, using parallel For Loops in LabVIEW
 code modules to apply the same settings to multiple instruments at
 once is much faster than implementing loops in TSM.

#### Use Per-Site Data to
 Store Data within Code Modules

Use the Set Site Data VI or
 SetSiteData .NET method and the Get Site
 Data VI or GetSiteData .NET method in the TSM Code Module API to store data that
 you need to access in another code module later.
 Using this development strategy provides an advantage over storing
 data in TSM variables because the API maintains unique data for each
 site. Additionally, you can access the data directly within code
 modules instead of passing the data from TSM as a parameter.

#### Specify Pin Names as
 Parameters to Code Modules

Use parameters to pass pin
 names into code modules from TSM instead of hard coding pin names
 within the code modules. Using this technique improves the
 readability of the test program by making the use of each pin in the
 code module more apparent to test engineers. It also generalizes
 code modules for potential reuse in other test
 programs.

#### Other
 Suggestions

Additionally, consider the following issues
 during code module development:

- Querying pins and sessions
- Using parallel For Loops
- Grouping Instruments or
 Channels
- Specifying input
 parameters
- Obtaining values from specifications
 files
- Sharing data between code
 modules
- Publishing results
- Sharing instrument sessions between
 LabVIEW and .NET code modules
- Using LabVIEW VI Analyzer
- Using LabVIEW Classes

<!--NI_TOPIC bundle=teststand-semiconductor-module path=code-modules-with-multiplexed-routes.html language=enus -->
## TOPIC 00025: Code Modules with Multiplexed Routes (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `code-modules-with-multiplexed-routes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/code-modules-with-multiplexed-routes.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a code module you call from a Semiconductor Multi Test step, you must connect DUT pins connected to multiplexers to the corresponding switch route before you can perform a test on that DUT pin. At the end of the test, disconnect the route. Refer to the Switching Example Test Code VI in the Switch

### Code Modules with Multiplexed Routes (TSM)

In a code module you call from a Semiconductor Multi Test step, you must
 connect DUT pins connected to multiplexers to the corresponding
 switch route before you can perform a test on that DUT pin. At the
 end of the test, disconnect the route. Refer to the Switching
 Example Test Code VI in the Switching example for an example of how
 to perform a measurement on multiplexed connections.

Note

In the code module, pass NISimulatedMultiplexer for the Multiplexer Type
 ID parameter of the Pin to Switch Sessions VI to
 obtain an array of switch sessions, switch route names, and
 Semiconductor Module contexts for each site in the subsystem. Each
 element in the Semiconductor Module contexts array represents a
 single site on which the test code must execute serially. Use the
 Semiconductor Module context object to query the pin map and publish
 data for the site. In a For Loop, use the switch session and the
 corresponding route name to connect the switch route. Because the
 session data is an array of variant data types to allow for any
 session type, use the Variant To Data function inside the For Loop
 to convert the variant data type to the correct switch session type.
 Because auto-indexing is enabled on the For Loop, it ensures that
 the switch session, switch route name, and Semiconductor Module
 context correspond to each other for each iteration of the For Loop.

Note

After you connect the route, call the Pin Query VI inside the For Loop to query the pin map for the instrument session. Each iteration of the For Loop uses a separate instance of the Semiconductor Module context from the array the Pin To Switch Sessions VI returns. Use the instrument session to perform the measurement on the pin. Use the Publish Data VI to publish the measurement by passing the Pin Query Context the Pin Query VI returns to the Publish Data VI. After you publish the measurement, you must close the Semiconductor Module context reference because the reference was generated in LabVIEW, and the code module must manage the reference. You do not need to close the reference for the Semiconductor Module context that you pass as a parameter from TestStand.

Before exiting the For Loop, use the same switch session and switch route name to disconnect the switch route.

Parent topic:

Switching (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=command-button-class.html language=enus -->
## TOPIC 00026: Command Button Class (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `command-button-class.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/command-button-class.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Command Button class binds the buttons displayed on the front panel of the default operator interface to command objects in the TSM Application API. This class inherits from the Control class. The TSM Application API includes the following types of commands: Configure Lot—Launches a dialog box t

### Command Button Class (TSM)

The Command Button class binds the buttons displayed on the front panel of the default operator
 interface to command objects in the TSM Application API. This class
 inherits from the Control class.

The TSM Application API includes the following types of commands:

- Configure Lot—Launches a dialog box to configure a lot.
- Configure Station—Launches a dialog box to configure the station.
- Open STS Maintenance Software—Launches STS Maintenance Software 17.1 or later.
- Perform Single Part Test—Starts a lot and tests a single DUT for each site if no lot is active
 and pauses between DUTs when complete or, if paused between
 DUTs, tests a single DUT for each site before pausing
 again.
- Start Lot—Starts testing a new lot.
- Start/Resume Lot—Starts testing a new lot, resumes a suspended sequence execution at a
 breakpoint, or resumes a sequence execution that is paused
 between DUTs.
- Pause Lot—Pauses testing of the lot. Testing pauses between DUTs after completing the tests for
 the current DUTs on each site and before TSM sends the
 end-of-test (EOT) signal to the handler or prober.
- Pause/Resume Lot—Pauses execution of the lot after the current DUT for each site completes
 testing, resumes a suspended sequence execution at a
 breakpoint, or resumes a sequence execution that is paused
 between DUTs. If the sequence execution is suspended at a
 breakpoint, you cannot use this command to pause the
 execution of the lot.
- Retest—After a single test completes or when you pause a lot, retests a single DUT for each site
 for the active sequence file and then pauses execution.
- End Lot—Ends execution of the lot.
- View Mid Lot Summary—Generates a Mid-Lot Summary text report and displays the report in a
 floating panel.
- View Reports—Displays the reports for the current execution in a floating panel.
- Login/Logout—Logs an operator in or out.
- Exit—Closes the operator interface.

Parent topic:

Control Class (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=common-use-case.html language=enus -->
## TOPIC 00027: Common Use Cases for Measuring Test Program Performance (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `common-use-case.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/common-use-case.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Test Program Performance Analyzer to complete the following common tasks. Use Case Task Identify Slow Test Times Load a data set log file. Select Test Time in the Sorting Method section of the analyzer. The analyzer sorts the steps by the highest average test time of the maximum number of si

### Common Use Cases for Measuring Test Program Performance (TSM)

Use the Test Program
 Performance Analyzer to complete the following common tasks.

| Use Case | Task |
| --- | --- |
| Identify Slow Test Times | Load a data set log file. Select Test Time in the Sorting Method section of the analyzer. The analyzer sorts the steps by the highest average test time of the maximum number of sites configuration. Select Code Module Time in the Timing Method section of the analyzer to view times for changes you make to code modules in the test program. Click a bar in the graph to display a graph of the single step times for that step name and the number of sites, which can be helpful to determine if unexpected poor performance is related to particular cycles or sites. |
| Identify Low Parallel Test Efficiency (PTE) Values | Load a data set log file. Select PTE in the Sorting Method section of the analyzer. The analyzer sorts the steps by the worst calculated PTE values. The bars on the graph display the test time, and the diamonds on the graph display the calculated PTE of the test time relative to the site configuration test time. |
| Display Socket Time and Calculated PTE Values | Load a data set log file. Select Socket Times/PTE in the Graph Type control of the analyzer. The analyzer displays the overall socket time and the calculated PTE value for each site configuration. Use the Target Test Time section of the analyzer to enter the target PTE% you want to reach and to specify the single site test time to use to calculate the target test time. The graph displays the target times that each site configuration would need to meet to achieve the PTE% you set. |

Parent topic:

Measuring Test Program Performance (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=compare-data-in-performance-analyzer.html language=enus -->
## TOPIC 00028: Comparing Data in the Test Program Performance Analyzer (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `compare-data-in-performance-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/compare-data-in-performance-analyzer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Compare Data Sets in the Mode section of the Test Program Performance Analyzer to display two data set log files in the analyzer graph. Use the Base Log File Path and Modified Log File Path controls to select the data set log files to compare. If the Modified Log File Path control is empty wh

### Comparing Data in the Test Program Performance Analyzer (TSM)

Select Compare Data Sets in the Mode section of the Test Program
 Performance Analyzer to display two data set log files in the
 analyzer graph. Use the Base Log File Path
 and Modified Log File Path controls to select
 the data set log files to compare. If the Modified Log
 File Path control is empty when you change
 display modes, the analyzer launches a browse dialog box for you to
 select the file you want to use as the modified log file to compare
 against the existing base log file.

The analyzer graph displays the data in the following colors to indicate differences:

- Gray—Base data values.
- Green—A modified data value that is less than the base data value indicates a performance
 increase.
- Red—A modified data value that is greater than the base data value indicates a performance
 decrease.
- Blue—A modified data value that has a difference in performance from the base data value that is
 less than the percentage value specified in the
 Highlight Differences Above 
 control in the Mode section of the analyzer.

By default, the analyzer highlights differences only when the difference between the modified
 data value and the base data value is greater than 1%. Use the
 Highlight Differences Above control
 in the Mode section of the analyzer to change this threshold.

When you complete a test program performance measurement while the analyzer is already comparing
 two data sets, TSM prompts you to compare the newly generated data set to the
 current base data set displayed in the analyzer or to the current modified data set
 displayed in the analyzer.

Parent topic:

Test Program Performance Analyzer (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=compliance-alarm.html language=enus -->
## TOPIC 00029: Compliance Alarm

- bundle_id: `teststand-semiconductor-module`
- source_path: `compliance-alarm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/compliance-alarm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A compliance alarm indicates when an instrument channel enters a compliance state. Introduced in TestStand 2020 Semiconductor Module You must install NI-DCPower 20.1 or later to enable compliance alarm. You must install NI-DCPower 2024 Q2 or later to differentiate current and voltage compliance alar

### Compliance Alarm

A *compliance alarm* indicates when an instrument channel enters a
 compliance state.

Introduced in TestStand 2020 Semiconductor Module

Note

NI-DCPower 20.1

Note

NI-DCPower 2024 Q2

TSM supports compliance alarms for the following hardware models:

- PXIe-4135/6/7/8/9
- PXIe-4140/1/2/3/4/5/7
- PXIe-4162/3

- PXIe-4137/9
- PXIe-4147
- PXIe-4162/3

A channel enters a compliance state when, due to load conditions, the channel cannot
 reach the requested output level because it has already reached a programmed limit. A
 compliance alarm does not track transient compliance behavior during source value
 changes. This alarm activates only after the configured settling time once the SMU is
 operating in a steady state.

Note

SMU Best Practices:
 Understanding Compliance and Device Protection Errors

Overload
 Protection

Note

#### Example: Compliance alarm behavior
 when channel enters current compliance state

The following figure shows an example of compliance alarm behavior in TSM when an SMU
 channel enters compliance. In this example, the channel cannot reach a requested
 voltage because it reaches the current limit first which causes the channel to enter
 the current compliance state.

[IMAGE alt='image' src='GUID-D7F8F9F7-24EC-4D24-83D7-7081C4F9F066-a5.svg']

1. Channel reaches current limit and enters current compliance state. Deviation in
 voltage output begins.
2. Source delay ends and alarm raises.

Parent topic:

Using Alarms to Report Error Conditions at Runtime

Related information:

- SMU Best Practices: Understanding Compliance and Device Protection
 Errors
- TestStand Semiconductor Module Code Module .NET API
- TestStand Semiconductor Module Code Module VIs Help

<!--NI_TOPIC bundle=teststand-semiconductor-module path=config-presets-tsm.html language=enus -->
## TOPIC 00030: Configuration Presets (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `config-presets-tsm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/config-presets-tsm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: A configuration presets allow users to switch between predefined TestStand and TSM configurations without restarting the TestStand environment. A configuration is a group of setting values for TestStand and TSM options. Applying a configuration preset changes the TestStand and TSM options to the val

### Configuration Presets (TSM)

A configuration presets allow users to switch between predefined
 TestStand and TSM configurations without restarting
 the TestStand environment.

A configuration is a group of setting values for TestStand and
 TSM options. Applying a configuration preset changes the
 TestStand and TSM options to the values
 specified in the configuration. You can use premade generic
 Production or Development configurations, load
 your custom configuration using preset .json files, or save the
 current configuration as a preset.

To load or save a custom preset file, navigate to Semiconductor
 Module » Configuration Presets. By default,
 preset files are stored in the CustomPresets folder relative to the
 currently selected sequence file. Saving a custom preset creates
 the folder if it does not exist. You can also save or load custom
 preset files by browsing to the specific disk location manually.

Note

custom preset

CustomPresets

Configuration changes made after loading a custom preset do no affect or
 update the custom preset file. You must save the changes to update
 the custom preset.

Note

The following table lists TestStand and TSM
 configurations supported with configuration presets.

| TestStand/TSM Property | Key in Preset File | Property Values | Default Value for Development | Default Value for Production |
| --- | --- | --- | --- | --- |
| Execute Menu - Break on Sequence Failure | BreakOnSequenceFailure | True, False | False | False |
| Execute Menu - Break on Step Failure | BreakOnStepFailure | True, False | False | False |
| Execute Menu - Break on First Step | BreakOnFirstStep | True, False | False | False |
| Debug Menu - Sequence Analyzer - Toggle Analyze File Before Executing | AnalyzeSeqFileBeforeExecuting | True, False | True | False |
| Enable Breakpoints | EnableBreakpoints | True, False | True | False |
| Enable Tracing | EnableTracing | True, False | True | False |
| Immediately Goto Cleanup On Sequence Failure | GotoCleanupOnSequenceFailure | True, False | False | True |
| Interactive Executions - Branching Mode | InteractiveBranchingMode | InteractiveBranchMode_None, InteractiveBranchMode_Ignore, InteractiveBranchMode_GotoEnd, InteractiveBranchMode_RaiseRTE, InteractiveBranchMode_AllowAll | InteractiveBranchMode_Ignore | InteractiveBranchMode_Ignore |
| Interactive Executions - Propagate Failures and Errors from Nested Interactive Execution to Calling Execution | InteractivePropagateStatus | True, False | True | True |
| On Run-Time Error | RunTimeErrorOption | RTEOption_ShowDialog, RTEOption_Continue, RTEOption_Ignore, RTEOption_Abort, RTEOption_Retry | RTEOption_ShowDialog | RTEOption_Continue |
| Enable Breakpoints - Honor Breakpoints while Terminating | HonorBreakpointsOnTerminating | True, False | True | False |
| Allow Break While in Code Modules | BreakWhileInCodeModules | True, False | True | False |
| Enable Tracing - Allow Tracing into Setup/Cleanup | TraceIntoSetupCleanup | True, False | True | False |
| Enable Tracing - Allow Tracing into Pre-/Post-Step Callbacks | TraceIntoPrePostSetupCallbacks | True, False | False | False |
| Enable Tracing - Allow Tracing into Post Action Callbacks | TraceIntoPostActionCallbacks | True, False | False | False |
| Enable Tracing - Trace into Separate Execution Callbacks | TraceIntoSeparateExecutionCallbacks | True, False | False | False |
| Enable Tracing - Trace into Entry Points | TraceIntoEntryPoints | True, False | False | False |
| Enable Tracing - Allow Tracing into Sequence Calls Marked with Tracing "Disabled" | TraceIntoSequenceCallsMarkedTraceOff | True, False | False | False |
| Enable Tracing - Allow Tracing While Terminating | TraceWhileTerminating | True, False | False | False |
| Interactive Executions - Record Results | InteractiveRecordResults | True, False | True | False |
| Interactive Executions - Run Setup and Cleanup | InteractiveRunSetupCleanup | True, False | True | False |
| Interactive Executions - Evaluate Preconditions | InteractiveEvaluatePreconditions | True, False | True | False |
| Disable Result Recording for All Sequences | ResultsDisabled | True, False | False | False |
| Selecting a LabVIEW Server - LabVIEW Runtime (Auto detect using VI version) | LabVIEWServerToUse | RuntimeAutoDetect, DevActiveVersion | DevActiveVersion | RuntimeAutoDetect |
| Selecting a LabVIEW Server - Development System (Active Version) | LabVIEWServerToUse | RuntimeAutoDetect, DevActiveVersion | DevActiveVersion | RuntimeAutoDetect |
| Reserve Loaded VIs for Execution | ReserveLoadedVIsForExecution | True, False | True | True |
| Always run VI in Packed Project Library | LabVIEWModuleOverrideOption | LabVIEWModuleOverrideOption_Default, LabVIEWModuleOverrideOption_PPL | LabVIEWModuleOverrideOption_Default | LabVIEWModuleOverrideOption_Default |
| Automatically Build Packed Project Libraries at the Start of Execution | AutomaticallyBuildPPLAtStart | True, False | False | False |
| Handler/Prober Driver | HandlerProberDriver | 0, 1, 2… | 1 | 1 |
| Enable Inline QA | InlineQAEnabled | True, False | False | True |
| Standard Test Data Format (STDF) Log | EnableSTDFLog | True, False | True | True |
| Lot Summary Report | EnableLotSummaryReport | True, False | False | True |
| CSV Test Results Log | EnableCSVTestsResultLog | True, False | False | False |
| Debug Test Results Log | EnableDebugTestResultsLog | True, False | True | False |

<!--NI_TOPIC bundle=teststand-semiconductor-module path=config-result-processing-plugins.html language=enus -->
## TOPIC 00031: Enabling and Configuring TSM Result Processing Plug-ins

- bundle_id: `teststand-semiconductor-module`
- source_path: `config-result-processing-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/config-result-processing-plugins.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to enable and configure one or more TSM result processing plug-ins to generate TSM reports and data logs for the current lot of DUTs (test lot). In the TestStand Sequence Editor, select ConfigureResult Processing to launch the Result Processing dialog box. If the Output

### Enabling and Configuring TSM Result Processing Plug-ins

Complete the following steps to enable and configure one or more TSM result processing plug-ins to generate TSM reports and data logs for the current lot of DUTs (test lot).

1. In the TestStand Sequence Editor, select Configure»Result Processing to launch the
 Result Processing
 dialog box.
2. If the Output Name column already contains an item for the type of report or data log you want
 to generate, skip to step 5 to configure the result
 processing plug-in.
3. Enable the Show More Options control to display additional options to insert or delete instances of result processing plug-ins.
4. Click the Insert New 
 button and select the item from the list of result
 processing plug-ins that corresponds to the type of report
 or data log you want to generate. The result processing
 plug-in you selected now appears in the Output Name
 column.
5. Ensure that the Enabled column contains a checkmark for the type of report or data log that you want to generate.
6. Click the Options 
 button for the result processing plug-in to launch the
 related result processing plug-in Options dialog box.
7. In the Destination Directory option, specify the absolute path of the directory in which you
 want TSM to create the report or data log file. Leave the control blank if you want TSM to
 create the report or data log file in the same directory as the test program main sequence
 file. Note TSM result
 processing plug-ins use the combination of the destination directory you specify in the
 Options dialog box and the report or data log filename the GetReportFileName callback sequence returns to determine
 the absolute path of the report or data log file. You can modify a copy of the
 GetReportFileName sequence to customize the
 destination directory and filename of the report or data log file.
8. Click OK to close the result processing plug-in Options dialog box and click OK again to close the Result Processing dialog box.

Parent topic:

Reports and Data Logs (TSM)

Related concepts:

- GetReportFileName Callback (TSM)
- Specifying Report and Data Log Filenames (TSM)

Related information:

- Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configuraiton-definition-panel.html language=enus -->
## TOPIC 00032: Configuration Definition Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `configuraiton-definition-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configuraiton-definition-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configuration Definition panel specifies a table of standard and custom test conditions available for use in the test program. Each test program configuration specifies a value for the test conditions. The Configuration Definition panel contains the following options: Test Condition Type—Specifi

### Configuration Definition Panel

The Configuration Definition panel specifies a table of standard and custom test conditions available for use in the test program. Each test program configuration specifies a value for the test conditions.

The Configuration Definition panel contains the following options:

- Test Condition Type —Specifies the data type of the test condition. You
 can modify the type only or custom test conditions. When you
 modify a test condition type, each configuration resets the
 test condition value to a default value.
- Test Condition Name —Specifies the name of the test condition. Only custom
 test condition names can be modified. A red exclamation
 point indicates that the custom test condition name is
 invalid. A tooltip displays the error message.
- Add Condition —Launches the Specify New Condition Name dialog box, in
 which you can add a new test condition. You can select a
 standard test condition from a list or create a new custom
 test condition.
- Delete Condition —Removes the test condition you select from the test
 program and the test program configurations.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configuration-panels.html language=enus -->
## TOPIC 00033: Configuration Panels

- bundle_id: `teststand-semiconductor-module`
- source_path: `configuration-panels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configuration-panels.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each configuration you specify uses a corresponding Configuration panel that contains a table to specify test condition values and fields for configuring the test limits file for the configuration. The Configuration panels contains the following options: Test Condition Name—Displays the name of the

### Configuration Panels

Each configuration you specify uses a corresponding Configuration panel that contains a table to specify test condition values and fields for configuring the test limits file for the configuration.

The Configuration panels contains the following options:

- Test Condition Name —Displays the name of the test condition.
- Test Condition Value —Specifies the value
 for the test condition for the configuration.
- Test Limits File —Specifies the test limits file the configuration loads
 when test program execution begins.
- Open for edit 
 —Launches the test limits file in the default application
 associated with the file extension on the computer.
- Test Limits File Import Mode —Specifies whether the test limits file replaces only matching tests or
 deletes and adds new tests when loaded into
 the test program.
- Require every step to be in test limits file —Returns a run-time error and
 does not import the file if a test or step exists in the
 sequence but does not exist in the limits file. If you do
 not enable this option, the Import/Export Test Limits tool
 imports only matching tests or steps in the limits
 file.
- Import into Sequence File —Imports the test limits file into the sequence
 file.

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configurations-panel.html language=enus -->
## TOPIC 00034: Configurations Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `configurations-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configurations-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configurations panel specifies a list of configurations available for use in the test program. When you specify a new configuration, the Test Program Editor updates with a new panel that matches the name of the configuration you added. Use the corresponding Configuration panel to specify test co

### Configurations Panel

The Configurations panel specifies a list of configurations available for use in the test
 program. When you specify a new configuration, the Test Program
 Editor updates with a new panel that matches the name of the
 configuration you added. Use the corresponding Configuration panel to specify test
 condition values and fields for configuring the test limits file for
 the configuration.

The Configurations panel contains the following options:

- Configuration Name —Specifies the name of the configuration. A red
 exclamation point indicates that the configuration name is
 invalid. A tooltip displays the error message.
- Add Configuration —Adds a configuration to the list.
- Delete Configuration —Removes the configuration you select from the
 list.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configure-builtin-sim-handler-dialog.html language=enus -->
## TOPIC 00035: Configure Built-in Simulated Handler Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configure-builtin-sim-handler-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configure-builtin-sim-handler-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configure Built-in Simulated Handler dialog box contains the following options: Number of DUTs to Test—Specifies the number of DUTs to test before the simulated handler driver notifies the tester to stop testing. When you start testing by clicking the Start Lot button on the TSM toolbar, the sim

### Configure Built-in Simulated Handler Dialog Box (TSM)

The Configure Built-in Simulated Handler dialog box contains the following options:

- Number of DUTs to Test —Specifies the number of DUTs to test before the simulated handler driver notifies the tester to stop testing. When you start testing by clicking the Start Lot button on the TSM toolbar, the simulated handler driver stores an internal count of the number of DUTs that have completed testing.
- Simulated Index Time —Specifies the amount of time, in milliseconds, to elapse before the simulated handler driver notifies the tester to begin the next iteration of testing. When you start testing by clicking the Start Lot button on the TSM toolbar, the simulated handler driver waits the specified simulated index time from the end of the EndOfTest simulated handler driver entry point before sending the start-of-test notification, which allows the StartOfTest simulated handler driver entry point to begin the next iteration of testing. When you execute a test using the Single Pass Execution entry point, the simulated handler driver ignores any value specified in this control and performs only a single test iteration.
- Show Handler Dialogs —When you enable this option, the simulated handler driver launches a dialog box when invoking the StartOfTest and EndOfTest simulated handler driver entry points.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configure-handler-prober-entry-point.html language=enus -->
## TOPIC 00036: Configure Handler/Prober Driver Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configure-handler-prober-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configure-handler-prober-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure entry point to provide a mechanism for end users to configure the handler/prober driver and to persist the settings for multiple lots. The General tab of the default Configure Station Settings dialog box contains a Configure Handler/Prober button that calls the Configure entry poin

### Configure Handler/Prober Driver Entry Point (TSM)

Use the Configure entry point to provide a mechanism for end users to configure the handler/prober driver and to persist the settings for multiple lots.

The General tab of
 the default Configure Station Settings dialog box
 contains a Configure Handler/Prober button
 that calls the Configure entry point of the handler/prober driver
 sequence file that the
 Standard.HandlerDriverSequenceFilePath
 property of the station settings specifies.

The Configure entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| HandlerDriverData | Input or Output | Container that stores handler-specific or prober-specific settings or run-time data. In a handler/prober driver sequence file, you can modify the default structure of this parameter, such as by changing the data type from the default Container to a custom container data type. However, the Configure entry point must create, and optionally assign, each field of this parameter using the TestStand API, such as the PropertyObject.NewSubProperty method or a PropertyObject Set value method, such as SetValNumber.Do not enable the Check Type option for this parameter. Right-click the parameter and remove the checkmark from Check Type in the context menu to disable the Check Type option. |
| Canceled | Output | Boolean value that notifies TSM whether the handler/prober settings have been modified and must be saved to disk. A value of True indicates that the handler/prober settings have not changed. A value of False indicates that the handler/prober settings have been modified and must be saved to disk. |
| SemiconductorModuleManager | Input or Output | Object reference to an instance of a Semiconductor Module Manager. Use this object reference with the TSM Application API to get information about the currently configured lot. |

#### Persisting
 Handler/Prober Configuration Settings

TSM automatically
 persists the configuration settings that the Configure entry point
 returns in the HandlerDriverData parameter to
 disk when the Canceled parameter is
 False. TSM stores configurations settings
 for all handler/prober drivers in the <TestStand
 Config>\NI_SemiconductorModule\HandlerProberDrivers.cfg
 file.

Parent topic:

Handler/Prober Driver Entry Points (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configure-lot-settings-dialog.html language=enus -->
## TOPIC 00037: Configure Lot Settings Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configure-lot-settings-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configure-lot-settings-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor ModuleConfigure Lot in the TestStand Sequence Editor, click the Configure Lot button on the TSM toolbar, or click the Configure Lot button in the default TSM operator interface to launch the Configure Lot Settings dialog box, in which you can specify settings for the current lot

### Configure Lot Settings Dialog Box (TSM)

Select Semiconductor Module»Configure Lot in the TestStand Sequence Editor, click the
 Configure Lot button on the TSM
 toolbar, or click the Configure Lot button in
 the default TSM operator interface to launch the Configure Lot
 Settings dialog box, in which you can specify settings for the
 current lot under test.

Note

The Configure Lot Settings dialog box contains the following options:

- Test Program Path —When the Test Program Directory option on the General tab of the Configure Station Settings dialog box is empty, use this option to browse to a file path. If you specify a value for the Test Program Directory option, this control lists the sequence files in the directory you specified.
- Test Program Configuration —Specifies the test program configuration to execute. This option is available only when you define configurations for a test program.
- Part Type —Populates the
 LotSettings.Standard.PartType 
 property, which specifies the PART_TYP field in an STDF MIR
 record.
- Lot ID —Populates the
 LotSettings.Standard.LotId 
 property, which specifies the LOT_ID field in an STDF MIR
 record.
- Estimated Lot Size —Populates the
 LotSettings.Standard.LotSize 
 property, which an inline QA algorithm can use to determine
 for which DUTs to enable inline QA.
- Test Flow —Populates the
 LotSettings.Standard.TestFlowId 
 property, which specifies the FLOW_ID field in an STDF MIR
 record.
- Test Temperature —Populates the
 LotSettings.Standard.TestTemperature 
 property, which specifies the TST_TMP field in an STDF MIR
 record.
- Operator Name —Displays the value of the
 LotSettings.Standard.OperatorName 
 property, if it exists. If this property is blank, this
 field displays the user name of the currently logged in
 user. TSM uses this value to specify the OPER_NAM field in
 an STDF MIR record.
- Enabled Sites —Populates the
 StationSettings.Standard.AvailableSiteNumbers 
 property, which specifies which site numbers to use when
 running a test program. TSM obtains the sites to display in
 this list from the pin map for the test program or from the
 number of test sockets specified in the
 Model Options
 dialog box if the test program does not use a pin map. You
 must enable at least one site. If the test program uses the
 Sequential
 process model, you can enable only one site.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configure-station-settings-dialog.html language=enus -->
## TOPIC 00038: Configure Station Settings Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configure-station-settings-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configure-station-settings-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure Station Settings dialog box to set options for the current test station in TestStand Semiconductor Module. Select Semiconductor ModuleConfigure Station in the TestStand Sequence Editor, click the Configure Station button on the TSM toolbar, or click the Configure Station button in

### Configure Station Settings Dialog Box (TSM)

Use the Configure Station Settings dialog box to set options for the current test
 station in TestStand Semiconductor Module.

Select Semiconductor Module»Configure Station in the TestStand Sequence Editor, click the
 Configure Station button on the TSM
 toolbar, or click the Configure Station
 button in the TSM operator interface to launch the Configure Station
 Settings dialog box, in which you can specify settings for the
 current test station.

The Configure Station Settings dialog box contains the following tabs:

- General—Configures settings for the handler/prober mode, Inline QA, and step failure mode.
- Advanced—Contains
 buttons to launch the Result Processing, Station Options,
 Edit Search Directories, and LabVIEW Adapter Configuration
 dialog boxes.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configurelotsettings-callback.html language=enus -->
## TOPIC 00039: ConfigureLotSettings Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configurelotsettings-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configurelotsettings-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default implementation of the ConfigureLotSettings callback sequence launches the default Configure Lot Settings dialog box, in which the operator can configure the lot settings. You can override this callback sequence to customize the behavior. You can also use the ConfigureLotWhenStartingLot o

### ConfigureLotSettings Callback (TSM)

The default implementation of the ConfigureLotSettings callback sequence
 launches the default Configure Lot Settings dialog box, in which the operator can
 configure the lot settings. You can override this callback sequence to customize the
 behavior. You can also use the ConfigureLotWhenStartingLot option on the
 Semiconductor Module Manager to customize an operator interface to automatically
 call the ConfigureLotSettings callback sequence at the beginning of
 the execution of each lot.

The ConfigureLotSettings callback sequence accepts the following parameters:

- LotSettings [In/Out]—An instance of the
 NI_SemiconductorModule_LotSettings data type. Configure the
 ConfigureLotSettings callback sequence to assign values for
 all the properties that you require. If you implement a dialog box for users
 to manually enter lot information, ensure that the dialog box obtains values
 for all the properties of the LotSettings parameter that
 you require. If the default properties of the LotSettings
 parameter do not meet your requirements, you can add properties to the
 NI_SemiconductorModule_CustomLotSettings data type. The properties you add
 to the data type appear in the Custom container of the
 LotSettings parameter. The
 LotSettings.Standard.MainSequenceFilePath property
 specifies the file path of the test program main sequence file to use with
 the current test lot. TSM records the lot setup time in the
 LotSettings.Standard.SetupTime property and saves lot
 settings to disk when the ConfigureLotSettings callback
 sequence sets the Canceled parameter to
 False. The value of the
 LotSettings.Standard.SetupTime property determines the
 value of the SETUP_T field in the Master Information Record (MIR) of
 version 4 of the Standard Test Data Format (STDF).
- Canceled [Out]—Configure the ConfigureLotSettings callback sequence to set this parameter to True if the operator cancels edits in the Configure Lot Settings dialog box. TSM saves the values of the LotSettings and StationSettings parameters to disk only when the Canceled parameter is False .
- SemiconductorModuleManager [In]—A reference to the
 Semiconductor Module Manager object that you use to call utility methods in the
 TSM Application API.
- StationSettings [In/Out]—An instance of the
 NI_SemiconductorModule_StationSettings data type. Use this parameter to modify
 station settings you require. Typically, the ConfigureStationSettings callback
 sequence sets station settings, but you might want to set certain station
 settings while configuring lot settings. TSM saves station settings to disk when
 the ConfigureLotSettings callback sequence sets the Canceled 
 parameter to False .

Parent topic:

Customizing the Behavior for Obtaining Lot Settings (TSM)

Related concepts:

- Configure Lot Settings Dialog Box (TSM)
- Customizing the Behavior for Obtaining Lot Settings (TSM)
- NI_SemiconductorModule_LotSettings Data Type
- TSM Application API
- NI_SemiconductorModule_StationSettings Data Type
- ConfigureStationSettings Callback (TSM)
- ConfigureLotSettings Callback (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configurestationsettings-callback.html language=enus -->
## TOPIC 00040: ConfigureStationSettings Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configurestationsettings-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configurestationsettings-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default implementation of the ConfigureStationSettings callback sequence launches the default Configure Station Settings dialog box, in which the test engineer or technician can configure the station settings. You can override this callback sequence to customize the behavior. You can also use th

### ConfigureStationSettings Callback (TSM)

The default implementation of the ConfigureStationSettings callback sequence
 launches the default Configure
 Station Settings dialog box, in which the test
 engineer or technician can configure the station settings. You can
 override this callback sequence to customize the behavior. You can also
 use the GetStationSettings callback sequence to
 programmatically obtain station settings when the test program
 begins executing without requiring much, if any, test engineer or
 technician interaction.

The ConfigureStationSettings callback sequence accepts the following parameters:

- StationSettings [In/Out]—An instance of the NI_SemiconductorModule_StationSettings data type. Configure the ConfigureStationSettings callback sequence to assign values for all
the properties that you require.
 If you implement a dialog box for users to manually configure station information, ensure that the dialog box obtains values for all the properties of the StationSettings parameter that you require. If the default properties of the StationSettings parameter do not meet your requirements, you can add properties to the NI_SemiconductorModule_CustomStationSettings data type. The properties you add to the data type appear in the Custom container of the StationSettings parameter.
TSM saves station settings to disk when the ConfigureStationSettings callback sequence sets the Canceled parameter to False .
- Canceled [Out]—Configure the ConfigureStationSettings callback sequence to set this parameter to True if the test engineer or technician cancels edits in the Configure Station Settings dialog box. TSM saves the values of the StationSettings parameter to disk only when the Canceled parameter is False .
- SemiconductorModuleManager [In]—A reference to the Semiconductor Module Manager object that you use to call utility methods in the TSM Application API.

Parent topic:

Customizing the Behavior for Obtaining Station Settings (TSM)

Related concepts:

- Configure Station Settings Dialog Box (TSM)
- Customizing the Behavior for Obtaining Station Settings (TSM)
- GetStationSettings Callback (TSM)
- NI_SemiconductorModule_StationSettings Data Type
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configuring-handler-or-prober-support-for-a-test-program.html language=enus -->
## TOPIC 00041: Configuring Handler or Prober Support for a Test Program (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configuring-handler-or-prober-support-for-a-test-program.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configuring-handler-or-prober-support-for-a-test-program.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Semiconductor testers often use handlers and probers to complete the following tasks: Place untested DUTs in test sites (Handlers) Move tested DUTs from test sites to an appropriate hardware bin, depending on the test results Potentially notify the tester to stop the test when no DUTs remain The tes

### Configuring Handler or Prober Support for a Test Program (TSM)

Semiconductor testers often use handlers and probers to complete the following tasks:

- Place untested DUTs in test sites
- (Handlers) Move tested DUTs from test sites to an appropriate
 hardware bin,
 depending on the test results
- Potentially notify the tester to stop the test when no DUTs remain

The tester software must be able to communicate with the handler or prober to execute tests correctly. Handlers and probers use a variety of different communication protocols and command sets. Test program developers might need to ensure that the tester can use different types of handlers or probers.

#### TSM
 Implementation

Use the TSM handler/prober driver plug-in
 architecture to write and enable handler/prober driver sequence
 files. A handler/prober driver sequence file contains handler/prober driver entry point
 sequences that TSM calls during execution to
 accomplish handler-related or prober-related tasks.

Use the
 NI Built-in Simulated Handler Driver to
 simulate handler functionality without requiring access to a real
 handler. To integrate a real handler or prober in the handler/prober
 driver plug-in architecture, you must create a new handler/prober driver sequence
 file. TSM uses only one active handler/prober driver
 sequence file at a time because the lot of DUTs (test lot) can use
 just one type of handler or prober at a time.

Related concepts:

- Handler/Prober Driver Entry Points (TSM)
- NI Built-in Simulated Handler Driver (TSM)

Related tasks:

- Creating a Handler/Prober Driver Sequence File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=configuring-switches-with-switch-executive.html language=enus -->
## TOPIC 00042: Configuring Switches with Switch Executive (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `configuring-switches-with-switch-executive.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/configuring-switches-with-switch-executive.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends using Switch Executive to configure complex switching routes. Switch Executive provides a user interface to configure routes and route groups in Measurement & Automation Explorer. Refer to the Switch Executive Help for more information about configuring switch routes. You can deploy th

### Configuring Switches with Switch Executive (TSM)

NI recommends using Switch Executive to configure complex switching routes. Switch Executive
 provides a user interface to configure routes and route groups in
 Measurement & Automation Explorer. Refer to the *Switch
 Executive Help* for more information about configuring
 switch routes.

You can deploy the route configuration to production test systems by exporting the virtual device
 as part of an NI Configuration Export File that Measurement &
 Automation Explorer generates and then including the file in a TestStand
 deployment.

Parent topic:

Switching (TSM)

Related information:

- Including Hardware Configuration Information in a Deployment

<!--NI_TOPIC bundle=teststand-semiconductor-module path=connect-shared-resource-dut-pin.html language=enus -->
## TOPIC 00043: Connecting a Shared Resource to One or More Sites using DUT Pins and Site Relays

- bundle_id: `teststand-semiconductor-module`
- source_path: `connect-shared-resource-dut-pin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/connect-shared-resource-dut-pin.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: For each DUT pin and site relay, the Pin Map Editor assumes there is one connection per site and displays a row for each site in the Connections table. Complete the following steps in the Pin Map Editor to create a connection for a DUT Pin or site relay that multiple sites share. Select Connections

### Connecting a Shared Resource to One or More Sites using DUT Pins and Site Relays

For each DUT pin and site relay, the Pin Map Editor assumes there is one connection per site and displays a row for each site in the Connections table. Complete the following steps in the Pin Map Editor to create a connection for a DUT Pin or site relay that multiple sites share.

1. Select Connections on the Pin Map tab.
2. In the View Connections for drop-down menu, select All Pins and Relays .
3. In the Connections table, select the instrument and channel or relay driver module and control line from the Instrument and Channel column cells for one of the rows associated with the DUT pin or site relay.
4. Repeat step 3 for the remaining sites, using the same instrument channel or relay driver module control line for the sites that share the resource. The Pin Map Editor automatically combines the rows that use the same resource into a single row. Alternatively, you can enter a comma-separated list of site numbers in the Site column to specify which sites share the resource.

When you save the pin map file, the Pin Map Editor automatically removes any duplicate site connections from the Connections table.

When you define a shared resource in the pin map, the results of your Pin Query VI
 or .NET method and Publish Data VI or Publish .NET method
 will be affected as follows:

- Pin Query VI or .NET method—Only one entry is included for a shared
 resource.
- Publish Data VI or Publish .NET method—The result is
 duplicated for each site that uses the shared resource.

Parent topic:

Connecting Shared Resources in the Pin Map (TSM)

Related concepts:

- Pin and Session Queries (TSM)
- Publishing Results (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=connect-shared-resource-system-pin.html language=enus -->
## TOPIC 00044: Connecting a Shared Resource using System Pins and System Relays

- bundle_id: `teststand-semiconductor-module`
- source_path: `connect-shared-resource-system-pin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/connect-shared-resource-system-pin.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: For each system pin and system relay in the pin map, the Pin Map Editor displays a row in the Connections table. Complete the following steps in the Pin Map Editor to create a connection for a system pin or system relay that all sites share. Select Connections on the Pin Map tab. In the View Connect

### Connecting a Shared Resource using System Pins and System Relays

For each system pin and system relay in the pin map, the Pin Map Editor displays a row in the
 Connections table. Complete the following steps in the Pin Map Editor to create a
 connection for a system pin or system relay that all sites share.

1. Select Connections on the Pin Map tab.
2. In the View Connections for drop-down menu, select All Pins
 and Relays .
3. In the Connections table, select the instrument and channel or relay driver module and control line from the Instrument and Channel column cells of the system pin or system relay for which you want to create a connection.

Parent topic:

Connecting Shared Resources in the Pin Map (TSM)

Related concepts:

- Pin Map Editor (TSM)

Related tasks:

- Viewing and Editing Connections in the Connections Table (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=connecting-shared-resources-in-pinmap.html language=enus -->
## TOPIC 00045: Connecting Shared Resources in the Pin Map (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `connecting-shared-resources-in-pinmap.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/connecting-shared-resources-in-pinmap.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: A shared resource is a device on the tester or DIB that is connected to an instrument or relay driver module and shared by multiple sites. To specify a connection between a shared resource and an instrument channel or relay driver module control line, use the following criteria to decide how to defi

### Connecting Shared Resources in the Pin Map (TSM)

A shared resource is a device on the tester or DIB that is connected to an instrument or relay driver module and shared by multiple sites. To specify a connection between a shared resource and an instrument channel or relay driver module control line, use the following criteria to decide how to define a shared resource in the pin map.

1. If the resource is a relay:
  1. If there is a single relay shared by all sites, define a system relay.
  2. If there are multiple relays in which each relay is associated with multiple sites, define a site relay.
2. If the resource is not a relay:
  1. If the resource is shared by all sites and you do not need to burst patterns to the resource using an NI-Digital Pattern instrument, define a system pin.
  2. Otherwise, define a DUT pin.

Parent topic:

Mapping DUT Pins to Instrument Channels (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=control-class.html language=enus -->
## TOPIC 00046: Control Class (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `control-class.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/control-class.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Control class is the base class for many of the controls displayed on the front panel of the operator interface. You can override the Refresh Callback VI in the Control class to update the appearance of controls when the operator interface changes state, such as updating the counts on a statisti

### Control Class (TSM)

The Control class is the base class for many of the controls displayed on the front panel of the operator interface. You can override the Refresh Callback VI in the Control class to update the appearance of controls when the operator interface changes state, such as updating the counts on a statistics control at a fixed interval.

The following classes inherit from the Control class to display additional information in the operator interface:

- Bin Table—Displays information about the binning of DUTs of the current lot, such as the names
 of the soft bins, the associated hard bins, and the DUT
 counts for each site.
- Command Button—Binds a LabVIEW button to a command object in the
 TSM Application API,
 such as Start Lot, End Lot, Login/Logout, or Configure Lot.
 The command object handles the functionality of the button
 when a user clicks the button and updates the enabled state
 and text of the button when the state of the command
 changes.
- InlineQA Label—Displays a label for the statistics and status of inline QA. The label and
 statistics controls are hidden when inline QA is disabled.
- Last N Parts Label—Displays a label for the column of site status controls and the number of
 DUTs included in the site status.
- Site Label—Displays a label for the statistics and status of a particular site.
- Site Status—Displays a color-coded status of the most recent n DUTs that have
 been tested, where the Site Status Part Count station
 setting specifies n . The red portion of the
 bar indicates the number of DUTs that failed. The green
 portion of the bar indicates the number of DUTs that passed.
 The ratio of the two colors in the bar indicates the recent
 yield of DUTs tested in a particular site.
- Site Testing Icon—Displays an icon that indicates whether the handler has placed a DUT in the
 site or the prober is testing on the site.
- Statistics Control—Displays statistical information for a lot execution, such as cycle time and
 socket time or site part counts. When binding this control,
 specify the site and statistics type to display.
- Test Program Info—Displays the value of relevant station settings and lot settings for the
 loaded test program. The
 OISettingsTable.cfg 
 configuration file determines the list of settings to
 display and how to format the settings values.
- Tester Status—Displays the current status of the tester, such as if a lot is testing or if any
 errors have occurred.

Parent topic:

LabVIEW Operator Interface Architecture (TSM)

Related concepts:

- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=control-sts-test-head-step.html language=enus -->
## TOPIC 00047: Control STS Test Head Step (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `control-sts-test-head-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/control-sts-test-head-step.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Control STS Test Head step to control properties of the STS. The step must be run only on an STS with STS Maintenance Software 19.0 or later. Configuring the Step Use the Control STS Test Head edit tab in the TestStand Sequence Editor to specify the list of STS properties and settings.

### Control STS Test Head Step (TSM)

Use the Control STS Test Head step to control properties of the STS. The step must be run only on an STS with STS Maintenance Software 19.0 or later.

#### Configuring the
 Step

Use the Control STS Test Head edit
 tab in the TestStand Sequence Editor to specify the
 list of STS properties and settings.

Parent topic:

TSM Step Types

Related concepts:

- Control STS Test Head Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=control-sts-test-head-tab.html language=enus -->
## TOPIC 00048: Control STS Test Head Tab (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `control-sts-test-head-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/control-sts-test-head-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Control STS Test Head tab contains a table that lists the STS properties the step controls. Modifying the Layout and Entering Data Use the buttons located to the right of the table to add, remove, or reorder per-site inputs. You can enter data in the table in the following ways: Enter data when

### Control STS Test Head Tab (TSM)

The Control STS Test Head tab contains a table that lists the STS properties the step controls.

#### Modifying the Layout
 and Entering Data

Use the buttons located to the right of
 the table to add, remove, or reorder per-site inputs.

You can
 enter data in the table in the following ways:

- Enter data when a cell is highlighted.
- Click in a cell when it is highlighted.
- Double-click a cell.
- Select a value from a drop-down menu.
- Drag a variable or property from the
 Variables
 pane to a text or expression cell.

#### Columns

The
 table contains the following columns:

- Name—The name of the STS property to control. You can choose one
 of the items from the drop-down menu, or you can type any
 part of the property name and select the item from the
 drop-down menu of suggestions.
- Source Expression—An expression that specifies the value to set
 for the STS property. The following table lists the STS
 properties you can access from this step. NameTypeDescription12VPowerSupplyEnabledBooleanEnables or disables the 12 V pins on STS CX
 and STS DX systems. The pins are disabled by
 default at STS power up and when a load board is
 not installed or locked down on the STS, such as
 when the value of the DIBPresent
 property is False. These signals
 are available on the system cable for STS CX
 systems and on the P143 system block for STS DX
 systems.48VPowerSupplyEnabledBooleanEnables or disables the 48 V pins on STS CX
 and STS DX systems. The pins are disabled by
 default at STS power up and when a load board is
 not installed or locked down on the STS, such as
 when the value of the DIBPresent
 property is False. These signals
 are available on the system cable for STS CX
 systems and on the P143 system block for STS DX
 systems.

Parent topic:

Control STS Test Head Step (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=create-inline-qa-algorithm-sequence.html language=enus -->
## TOPIC 00049: Creating an Inline QA Algorithm Sequence File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `create-inline-qa-algorithm-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/create-inline-qa-algorithm-sequence.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the InlineQAAlgorithm.seq file, located in the <TestStand>\Components\Modules\NI_SemiconductorModule\Templates directory, as a starting point for an inline QA algorithm sequence file you create. Copy the InlineQAAlgorithm.seq file from the <TestStand>\Components\M

### Creating an Inline QA Algorithm Sequence File (TSM)

Complete the following steps to use the InlineQAAlgorithm.seq file, located
 in the <TestStand>\Components\Modules\NI_SemiconductorModule\Templates
 directory, as a starting point for an inline QA algorithm sequence
 file you create.

1. Copy the InlineQAAlgorithm.seq file from the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates 
 directory to the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\InlineQA 
 directory.
2. Rename the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\InlineQA\InlineQAAlgorithm.seq 
 file using the
 <CompanyName> _ <InlineQAAlgorithmName>.seq 
 convention.
3. Open the inline QA algorithm sequence file.
4. Add steps to the GetNextInlineQAStateQueueItems callback
 sequence to populate the
 NextInlineQAStateQueueItems 
 sequence parameter with a queue of inline QA states.
5. Save the inline QA algorithm sequence file.

Parent topic:

Performing Inline Quality Assurance Testing (TSM)

Related concepts:

- GetNextInlineQAStateQueueItems Callback (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=create-tsm-manager-object.html language=enus -->
## TOPIC 00050: Creating or Obtaining the Semiconductor Module Manager Object

- bundle_id: `teststand-semiconductor-module`
- source_path: `create-tsm-manager-object.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/create-tsm-manager-object.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Applications that use the TSM Application API must first create or obtain an instance of the Semiconductor Module Manager object, which implements most of the methods in the TSM Application API. For applications that control a test system, such as an operator interface, you must create a new Semicon

### Creating or Obtaining the Semiconductor Module Manager Object

Applications that use the TSM Application API must first create or obtain an instance of the Semiconductor Module Manager object, which implements most of the methods in the TSM Application API.

For applications that control a test system, such as an operator interface, you must create a
 new Semiconductor Module Manager object. For custom reports,
 callbacks used to set lot of station settings, and other programs
 for monitoring a test system, you must obtain the existing
 Semiconductor Module Manager object that the TestStand Sequence
 Editor or an operator interface created.

#### Creating an Instance
 of the Semiconductor Module Manager

Before you create the
 Semiconductor Module Manager object, you must first create a
 TestStand Application Manager control and a
 SequenceFileView Manager control in
 the TestStand user interface.

To create the
 Semiconductor Module Manager object in LabVIEW, use the Create
 Semiconductor Module Manager VI. To create the object in .NET, call
 the NewSemiconductorModuleManager static method on
 the SemiconductorModuleManagerFactory
 class.

#### Obtaining an Existing
 Instance of the Semiconductor Module Manager

To obtain the
 existing Semiconductor Module Manager object in LabVIEW, use the Get
 Semiconductor Module Manager VI. To obtain the existing object in
 .NET, call the GetSemiconductorModuleManager static
 method on the SemiconductorModuleManagerFactory
 class.

Parent topic:

TSM Application API

Related concepts:

- TSM Application API
- Operator Interfaces (TSM)

Related information:

- Application Manager
- SequenceFileView Manager
- Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand-semiconductor-module path=creating-custom-instrument-panels.html language=enus -->
## TOPIC 00051: Creating Custom Instrument Panels

- bundle_id: `teststand-semiconductor-module`
- source_path: `creating-custom-instrument-panels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/creating-custom-instrument-panels.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must create the following components to implement a custom instrument panel you can launch from the Semiconductor Module menu: A custom instrument panel callback sequence file that meets the following requirements: The file must reside in the <TestStand Public>\Components\Modules\NI_Semiconducto

### Creating Custom Instrument Panels

You must create the following components to implement a custom instrument panel you can launch from the Semiconductor Module menu:

- A custom instrument panel callback sequence file that meets the following requirements:
  - The file must reside in the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\CustomInstrumentPanels 
 directory. Note After you add custom instrument panel components
 to this directory, you must restart TestStand to
 register the custom instrument panel and update
 the Semiconductor Module»Custom Instrument Panels menu.
  - The file must contain a LaunchCustomInstrumentPanel callback sequence that includes a TestStand Action step to launch the custom instrument panel VI. Ensure that you enable the Show VI Front Panel option on the Module tab of the step. The LaunchCustomInstrumentPanel callback sequence must also include a Parameters variable of type Object Reference named SemiconductorModuleManager .
  - The file must include a file global variable named
 CustomInstrumentPanelDisplayName .
 This variable must include a unique value to
 display in the Semiconductor Module»Custom Instrument Panels menu.
  - The file can include an optional file global variable named
 CustomInstrumentPanelIcon to
 specify the filename of an icon to display in the Semiconductor Module»Custom Instrument Panels menu. The icon must be located in
 the C:\Users\Public\Documents\National
 Instruments\<TestStand>\Components\Icons 
 directory.
- A custom instrument panel VI, for example, TopLevel.vi , that implements debugging tasks for the instrument and that meets the following requirements:
  - You must call the VI from a TestStand Action step in the LaunchCustomInstrumentPanel callback sequence.
  - You must use the Parameters.SemiconductorModuleManager string to pass the
 Semiconductor Module Manager object reference to
 the VI. Note NI
 recommends that custom instrument panel VI source
 code resides in the <TestStand
 Public>\Components\Modules\NI_SemiconductorModule\CustomInstrumentPanels
 directory along with the required custom
 instrument panel callback sequence
 file.

Refer to the following resources that you can use as starting points for custom instrument panels you create:

- Examples located in the <TestStand
 Public> \Examples\NI_SemiconductorModule\Custom
 Instrument Panels directory
- A template for the required custom instrument panel callback sequence file named
 CustomInstrumentPanel.seq located in the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates 
 directory
- A template for the required corresponding custom instrument panel LabVIEW project files located
 in the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates\CustomInstrumentPanelTemplate 
 directory

Note

<TestStand
 Public>

Parent topic:

Custom Instrument Panels (TSM)

Related information:

- TestStand Directory Structure
- Copying Read-Only Files to Modify

<!--NI_TOPIC bundle=teststand-semiconductor-module path=creating-pat-algorithm-settings.html language=enus -->
## TOPIC 00052: Creating PAT Algorithm Settings

- bundle_id: `teststand-semiconductor-module`
- source_path: `creating-pat-algorithm-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/creating-pat-algorithm-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a PAT algorithm setting, add string, number, Boolean, and enumeration properties to the FileGlobals.PartAverageTestingDescription.AlgorithmSettings container property. To further refine how TSM displays the setting in the PAT Algorithm Settings panel of the Test Program Editor, add an attr

### Creating PAT Algorithm Settings

To create a PAT algorithm setting, add string, number, Boolean, and enumeration properties to the
 FileGlobals.PartAverageTestingDescription.AlgorithmSettings
 container property. To further refine how TSM displays the setting
 in the PAT Algorithm Settings panel of the
 Test Program Editor, add an attribute to the setting
 property that is an instance of the
 NI_SemiconductorModule_PATAlgorithmSettingUIAttribute data type and
 name the attribute UI. Set the following properties
 in the UI container to control how TSM treats the
 setting:

- DisplayName —Specifies the text to display in the Name column for the setting. If this property is an empty string, TSM uses the algorithm setting property name.
- Description —Specifies an additional description of the setting that the PAT Algorithm Settings panel displays as a tooltip for the setting.
- BrowseButtonOption —Specifies whether TSM displays a browse button in the Value column for finding files or directories. Use this property to indicate whether the setting is a file or a directory.
- RequireAbsolutePath —Specifies whether TSM inserts absolute paths by default when browsing for a file or directory. TSM uses this property only if the BrowseButtonOption is set to Display file browse button or Display directory file browse button .
- MinimumNumberValue —Specifies the minimum value for a Number setting. This property has a default value of -Inf .
- MaximumNumberValue —Specifies the maximum value for a Number setting. This property has a default value of +Inf .
- DisplaySoftwareBinComboBox —Specifies that the Number setting corresponds to a bin number. TSM displays a combobox with the list of software bins for the current test program in the Value column. Bins must be defined in the bin definitions file.

Note

PartAverageTestingAlgorithmDescription

PartAverageTestingCallbacks.seq

Update
 Test Program Settings

Parent topic:

Part Average Testing Algorithm Settings (TSM)

Related concepts:

- PAT Algorithm Settings Panel
- Test Program Editor (TSM)
- Binning DUTs Based on Test Results (TSM)

Related information:

- PropertyObject Attributes

<!--NI_TOPIC bundle=teststand-semiconductor-module path=csv-test-results-log-options.html language=enus -->
## TOPIC 00053: CSV Test Results Log Options Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `csv-test-results-log-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/csv-test-results-log-options.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable and configure the TSM result processing plug-ins to launch the CSV Test Results Log Options dialog box, in which you can specify settings for the CSV Test Results Log. The CSV Test Results Log Options dialog box contains the following options: CSV Log Destination Directory—Absolute path of th

### CSV Test Results Log Options Dialog Box (TSM)

Enable and configure the TSM result processing plug-ins to launch the CSV Test Results Log Options dialog box, in which you can specify settings for the CSV Test Results Log.

The CSV Test Results Log Options dialog box contains the following options:

- CSV Log Destination Directory —Absolute path of the directory in which you
 want TSM to create the CSV data log file. Leave the control
 blank if you want TSM to create the CSV data log file in the
 same directory as the test program main sequence file.
 During testing, the CSV Test Results Log result
 processor writes data to a temporary file with an extension
 of .csvtemp in this directory at the
 end of each batch. When the file completes, the CSV Test
 Results Log result processor renames the file to the final
 report filename you
 specify.
- Generate One File per Wafer —Specifies to create a separate CSV log file
 for each tested wafer. This option has no effect when
 testing without a wafer probe. Each new log file resets the
 batch number to 1 .
- Log Wafer Data —Specifies to create columns in the CSV log file for the
 following data:
  - Wafer ID
  - Die X Coordinate
  - Die Y Coordinate
- Log Code Module Execution Time —Specifies to create a column in the CSV
 log file for the code module execution time for each
 test.
- Limit Number of Test Data Records —Specifies to limit the number of
 individual part test records in the CSV log file to one of
 out every N DUTs you specify per
 site. When you enable the Generate One File per
 Wafer option, this option applies to
 each CSV file independently and not to the entire lot. Each
 wafer CSV file includes test records for one out of every
 N DUTs per site.

Parent topic:

Dialog Boxes and Windows

Related concepts:

- CSV Test Results Logs (TSM)
- Specifying Report and Data Log Filenames (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=csv-test-results-logs.html language=enus -->
## TOPIC 00054: CSV Test Results Logs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `csv-test-results-logs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/csv-test-results-logs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a DUT completes testing, you can generate a CSV Test Results Log that contains data in a comma-separated values text file, which provides better performance than the Test Results Log result processor in a production environment. The CSV Test Results Log result processor generates a single file

### CSV Test Results Logs (TSM)

When a DUT completes testing, you can generate a CSV Test Results Log that contains data in a
 comma-separated values text file, which provides better performance
 than the Test Results Log result processor in a
 production environment. The CSV Test Results Log result processor
 generates a single file for all sites in the test program. You can
 open the .csv file directly in a spreadsheet
 application for analysis or to correlate test results.

Note

The CSV Test Results Log contains the following sections for each DUT:

- Wafer ID—Enables the Log Wafer Data option in the CSV Test Results Log Options
 dialog box.
- Batch Number
- Site Number
- Part ID
- Die X Coordinate—Enables the Log Wafer Data option in the CSV Test
 Results Log Options dialog box.
- Die Y Coordinate—Enables the Log Wafer Data option in the CSV Test
 Results Log Options dialog box.
- Sequence Name
- Step Name
- Test Number
- Test Name
- Result
- Low Limit
- Value—The CSV Test Results Log does not scale data values.
- High Limit
- Correlation Offset
- Units
- Code Module Time—Enables the Log Code Module Execution Time option in the
 CSV Test Results Log Options dialog box.

Note

Parent topic:

Reports and Data Logs (TSM)

Related concepts:

- Debug Test Results Logs (TSM)
- CSV Test Results Log Options Dialog Box (TSM)
- Offline Mode (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=custom-instrument-panels.html language=enus -->
## TOPIC 00055: Custom Instrument Panels (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `custom-instrument-panels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/custom-instrument-panels.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use custom pin- and site-aware instrument panel VIs to control and measure pins during test program execution at a breakpoint, which can be useful during test program development and troubleshooting. Custom instrument panels obtain active instrument sessions stored in Semiconductor Module co

### Custom Instrument Panels (TSM)

You can use custom pin- and site-aware instrument panel VIs to control and measure pins during test program execution at a breakpoint, which can be useful during test program development and troubleshooting. Custom instrument panels obtain active instrument sessions stored in Semiconductor Module context objects using the Set Session VIs or .NET methods in TSM Code Module API. During active test program execution, TSM disables the custom instrument panel to avoid conflicts.

Parent topic:

Debugging

Related concepts:

- TSM Code Module API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=custom-instruments.html language=enus -->
## TOPIC 00056: Custom Instruments (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `custom-instruments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/custom-instruments.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: TSM provides built-in support for commonly used instruments, such as NI-DCPower and NI-HSDIO. If you need to use an instrument TSM does not natively support, complete the following steps to define a custom instrument. Based on the instrument driver behavior in a multisite environment, complete the f

### Custom Instruments (TSM)

TSM provides built-in support for commonly used instruments, such as NI-DCPower and NI-HSDIO. If you need to use an instrument TSM does not natively support, complete the following steps to define a custom instrument.

1. Based on the instrument driver behavior in a multisite environment, complete the following step:
  - If each channel operates independently and can be accessed in separate
 threads with different timing, the instrument operates with one session
 per channel, similar to NI-DCPower instruments. Copy the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Custom Instruments\Session
 per Channel\LabVIEW directory to a new location and open
 the Session per Channel.seq file in the new
 location.
  - If all channels operate synchronously, such that they must all be
 accessed together, the instrument operates with one session per
 instrument, similar to NI-HSDIO instruments. Copy the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Custom Instruments\Session
 per Instrument\LabVIEW directory to a new location and
 open the Session per Instrument.seq file in the new
 location.
  - If the instrument has groups of channels that must be accessed
 synchronously, the instrument operates with one session per channel
 group. Copy the <TestStand
 Public>\Examples\NI_SemiconductorModule\Custom Instruments\Session
 per Channel Group\LabVIEW directory to a new location and
 open the Session per Channel Group.seq in the new
 location.
2. Use the Pin Map Editor to specify instrument channels and IDs.
3. Modify the related VI code modules in the example project to create a communication layer between the pin map and the instrument. Ensure that you update the session data inputs and outputs to a datatype that matches the expected data for the custom instrument.

Parent topic:

TSM Example Programs

Related concepts:

- Pin Map Editor (TSM)

Related tasks:

- Session per Channel (TSM)
- Session per Instrument (TSM)
- Session per Channel Group (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customize-filenames.html language=enus -->
## TOPIC 00057: Customizing Filename

- bundle_id: `teststand-semiconductor-module`
- source_path: `customize-filenames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customize-filenames.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you customize the log filename, use unique filenames for each test site. The Debug Test Results Log result processing plug-in appends results from each DUT to the corresponding site log.

### Customizing Filename

When you customize the log filename, use unique filenames for each test site. The Debug Test Results Log result processing plug-in appends results from each DUT to the corresponding site log.

Parent topic:

Debug Test Results Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customize-obtain-lot-settings.html language=enus -->
## TOPIC 00058: Customizing the Behavior for Obtaining Lot Settings (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customize-obtain-lot-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customize-obtain-lot-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Customize how TSM obtains lot settings for a test program. ConfigureLotSettings callback sequence—TSM calls the ConfigureLotSettings callback sequence when you trigger the ConfigureLotSettings command in the TSM operator interface or the TestStand Sequence Editor. If you set the ConfigureLotWhenStar

### Customizing the Behavior for Obtaining Lot Settings (TSM)

Customize how TSM obtains lot settings for a test program.

- ConfigureLotSettings callback sequence—TSM
 calls the ConfigureLotSettings callback
 sequence when you trigger the ConfigureLotSettings command
 in the TSM operator interface or the TestStand Sequence
 Editor. If you set the
 ConfigureLotWhenStartingLot 
 property on the SemiconductorModuleManager object using the
 TSM Application API to true, TSM also calls this callback
 sequence just before execution begins, when an operator
 initiates the start of a lot using the Start Lot or Perform
 Single Part Test button. Use this callback sequence to
 launch a dialog box to prompt an operator to enter lot
 information or to retrieve lot information programmatically,
 such as from a database. The default implementation of the
 ConfigureLotSettings callback
 sequence launches the default Configure Lot Settings dialog
 box.
- ConfigureLotWhenStartingLot option—Set this property on the
 SemiconductorModuleManager object
 using the TSM Application API to true when you want to
 customize an operator interface to automatically retrieve
 lot settings at the beginning of the execution of each lot.
 When you start the execution of a lot, TSM calls the
 ConfigureLotSettings callback
 sequence, which you can configure to retrieve lot
 information programmatically, such as from a database. The
 default setting for the
 ConfigureLotWhenStartingLot 
 property is False .
- GetLotSettings callback—TSM calls the
 GetLotSettings callback sequence as
 execution begins. Use this callback if you want to
 programmatically override a lot setting that might have been
 set in the ConfigureLotSettings callback
 sequence and you want to always do so at run time. The
 default implementation of the
 GetLotSettings callback sequence
 sets the LotSettings.Standard.JobName and
 LotSettings.Standard.JobRevision 
 values based on the value of
 LotSettings.Standard.MainSequenceFilePath .

Complete the following steps to override the default ConfigureLotSettings or GetLotSettings callback sequence and customize the behavior for obtaining lot settings.

1. Determine whether a sequence file named SemiconductorModuleCallbacks.seq 
 exists in the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule 
 directory. If the sequence file does not exist, create it
 and ensure that it does not contain any sequences.
2. Copy the ConfigureLotSettings or GetLotSettings callback
 sequences from the
 <TestStand> \Components\Modules\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq 
 file to the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file and make changes to the copy.
3. To customize the default Configure Lot Settings dialog box in the
 ConfigureLotSettings callback
 sequence, complete the following additional steps.
  1. Copy the Display Configure Lot Settings Dialog
 step from the
 ConfigureLotSettings callback
 sequence of the
 <TestStand> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file to the ConfigureLotSettings 
 callback sequence of the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file.
  2. Copy the contents of
 <TestStand> \Components\Callbacks\NI_SemiconductorModule\LotSettingsDialogs 
 to
 <TestStand Public> \Components\Callbacks\NI_SemiconductorModule\LotSettingsDialogs 
 and make changes to the copy of the LabVIEW
 project. If you are making extensive
 customizations to the LabVIEW project, use the
 Debugging the Lot Settings 
 dialog box to enable automatic testing when you
 makes changes to the lot settings.
  3. Rebuild the packed project library build
 specification in the project to update the copy of
 the LabVIEW packed project library.

Complete the following steps to change the value of the ConfigureLotWhenStartingLot property in the default operator interface.

1. Copy the contents of the
 <TestStand>\UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory to
 the <TestStand
 Public> \UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory.
 Note You must manually create the
 <TestStand
 Public>\UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory if it
 does not already exist.
2. Modify the files in the <TestStand
 Public>\UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory to
 find a reference to the SemiconductorModuleManager object
 and set the ConfigureLotWhenStartingLot 
 property to True .

Parent topic:

Specifying Settings for the Current Lot under Test (TSM)

Related concepts:

- ConfigureLotSettings Callback (TSM)
- TSM Application API
- Configure Lot Settings Dialog Box (TSM)
- GetLotSettings Callback (TSM)

Related tasks:

- Debugging the Lot Settings Dialog Box (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customize-obtain-station-settings.html language=enus -->
## TOPIC 00059: Customizing the Behavior for Obtaining Station Settings (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customize-obtain-station-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customize-obtain-station-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM obtains station settings by calling the following callback sequences, located in the <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq file: ConfigureStationSettings—The Configure Station button in the default TSM operator interface or the Semiconductor Mod

### Customizing the Behavior for Obtaining Station Settings (TSM)

TSM obtains station settings by calling the following callback sequences, located in the <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 file:

- ConfigureStationSettings—The
 Configure Station button in
 the default TSM operator interface or the Semiconductor Module»Configure Station menu item in the TestStand Sequence Editor
 calls the ConfigureStationSettings callback
 sequence to obtain the settings for the current test
 station. Use the ConfigureStationSettings 
 callback sequence to prompt a test engineer or technician to
 manually configure station settings in a dialog box or to
 use another mechanism that requires user input. The default
 implementation of the
 ConfigureStationSettings callback
 sequence launches the default
 Configure Station Settings
 dialog box.
- GetStationSettings—Use the GetStationSettings callback sequence to programmatically obtain station settings when the test program begins executing without requiring much, if any, test engineer or technician interaction. For example, you can specify that the callback sequence queries a database for the station information related to a barcode or DUT type. The default implementation of the GetStationSettings callback sequence does not perform any operations.

Complete the following steps to override the default ConfigureStationSettings or GetStationSettings callback sequence and customize the behavior for obtaining station settings.

1. Determine whether a sequence file named SemiconductorModuleCallbacks.seq 
 exists in the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule 
 directory. If the sequence file does not exist, create it
 and ensure that it does not contain any sequences.
2. Copy the ConfigureStationSettings or GetStationSettings callback sequences from the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq 
 file to the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file, and make changes to the copy.
3. To customize the default Configure Station Settings dialog box in the ConfigureStationSettings callback sequence, complete the following additional steps.
  1. Copy the Display Configure Station Settings Dialog step from the
 ConfigureStationSettings callback
 sequence of the <TestStand> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq file to the
 ConfigureStationSettings callback
 sequence of the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file.
  2. Copy the contents of <TestStand> \Components\Callbacks\NI_SemiconductorModule\StationSettingsDialogs 
 to <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\StationSettingsDialogs 
 and make changes to the copy of the LabVIEW
 project. If you are making extensive
 customizations to the LabVIEW project, use the
 Debugging the Station
 Settings dialog box to enable automatic
 testing when you makes changes to the station
 settings.
  3. Rebuild the packed project library build specification in the project to update the copy of the LabVIEW packed project library.

Parent topic:

Specifying Settings for the Current Test Station (TSM)

Related concepts:

- Configure Station Settings Dialog Box (TSM)
- GetStationSettings Callback (TSM)

Related tasks:

- Debugging the Station Settings Dialog Box (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customize-report-header.html language=enus -->
## TOPIC 00060: Customizing the Lot Summary Report Header (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customize-report-header.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customize-report-header.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Lot Summary Report result processing plug-in sets the information in the Lot Summary Report header by using the values of the properties in the NI_SemiconductorModule_LotSettings and NI_SemiconductorModule_StationSettings data types. You can modify the following station settings and lot settings

### Customizing the Lot Summary Report Header (TSM)

The Lot Summary Report result processing plug-in sets the information in the Lot Summary Report header by using the values of the properties in the NI_SemiconductorModule_LotSettings and NI_SemiconductorModule_StationSettings data types.

You can modify the following station settings and lot settings values to customize the values the Lot Summary Report result processing plug-in sets in the Lot Summary Report header.

- Station Settings
  - NodeName
  - HandlerType
- Lot Settings
  - JobName
  - JobRevision
  - PartType
  - LotId
  - TestFlowId
  - TestTemperature
  - OperatorName

Parent topic:

Lot Summary Reports (TSM)

Related concepts:

- NI_SemiconductorModule_LotSettings Data Type
- NI_SemiconductorModule_StationSettings Data Type

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customize-stdf-mir-sdr-wcr.html language=enus -->
## TOPIC 00061: Customizing STDF MIR, SDR, and WCR Field Values (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customize-stdf-mir-sdr-wcr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customize-stdf-mir-sdr-wcr.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The STDF Log result processing plug-in sets the fields in the Master Information Record (MIR), Site Description Record (SDR), and Wafer Configuration Record (WCR) of the STDF version 4 specification by using the values of the properties in the Standard containers of the NI_SemiconductorModule_LotSet

### Customizing STDF MIR, SDR, and WCR Field
 Values (TSM)

The STDF Log result processing plug-in sets the fields in the Master Information
 Record (MIR), Site Description Record (SDR), and Wafer Configuration Record (WCR) of
 the STDF version 4 specification by using the values of the properties in the
 Standard containers of the NI_SemiconductorModule_LotSettings
 and NI_SemiconductorModule_StationSettings data types. The
 LotSettings.Standard.Wafer container contains the property
 values that determine the WCR field values. TSM uses the following callback
 sequences, located in the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 or
 <TestStand>\Components\Module\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq
 file, to obtain the values of these data types:

- ConfigureLotSettings
- GetLotSettings
- ConfigureStationSettings
- GetStationSettings

You can create custom versions of these callback sequences to modify the values TSM
 obtains for the NI_SemiconductorModule_LotSettings and
 NI_SemiconductorModule_StationSettings data types, and therefore to modify the
 values the STDF Log result processing plug-in sets in the MIR, SDR, and WCR
 fields.

When using a handler/prober driver, TSM calls the handler/prober driver Setup entry
 point sequence after calling the GetLotSettings and GetStationSettings callbacks.
 The Setup entry point sequence can modify the values of the properties in the
 LotSettings and StationSettings parameters,
 which determine the values used in the MIR, SDR, and WCR fields. Typically, a prober
 driver sets the properties for the WCR fields by setting the property values in the
 LotSettings.Standard.Wafer container.

#### Customizing the MIR EXEC_TYPE
 Value

Complete the following steps to customize the MIR EXEC_TYPE value:

1. Using a text editor, open the StdfGenerator.ini.example 
 file located in the <TestStand Application Data> \Cfg\NI_SemiconductorModule directory.
2. Modify the StdfGenerator.ini.example file to specify the
 MIR EXEC_TYPE value you want. MIR EXEC_TYPE Value
 Steps
 Custom
 Update the ExecType key with the
 EXEC_TYPE value you want. For
 example, ExecType =
 "iniExecType".
 Verify that the
 UseTSMVersionBasedExecTypeFromRegistry key is set to
 false.
 Based on registry key
 Set the
 UseTSMVersionBasedExecTypeFromRegistry key to true. If STS
 Software is installed, the MIR EXEC_TYPE
 value will be updated to NI STS Development Software. If STS
 Software is not installed, the MIR
 EXEC_TYPE value will be updated to
 TestStand <year-based version>
 Semiconductor Module Runtime (32 bit or 64 bit)
 based on the TestStand version specified in the registry
 key.
3. Go to File»Save as and rename the modified file to
 StdfGenerator.ini .

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related concepts:

- NI_SemiconductorModule_LotSettings Data Type
- NI_SemiconductorModule_StationSettings Data Type
- ConfigureLotSettings Callback (TSM)
- GetLotSettings Callback (TSM)
- Configure Station Settings Dialog Box (TSM)
- GetStationSettings Callback (TSM)
- Setup Handler/Prober Driver Entry Point (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizing-operator-interfaces.html language=enus -->
## TOPIC 00062: Customizing Operator Interfaces (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizing-operator-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizing-operator-interfaces.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to customize the default LabVIEW operator interface or STS Operator Tool interface. Copy the contents of the <TestStand>\UserInterfaces\NI_SemiconductorModule\<LabVIEW or CSharp> directory to the <TestStand Public>\UserInterfaces\NI_SemiconductorModule\<LabVIEW or CSharp

### Customizing Operator Interfaces (TSM)

Complete the following steps to customize the default LabVIEW operator interface or STS Operator
 Tool interface.

1. Copy the contents of the <TestStand> \UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory to the <TestStand
 Public> \UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory. Note Create the
 <TestStand
 Public>\UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory if it does not already
 exist.
2. Modify the files in the <TestStand
 Public> \UserInterfaces\NI_SemiconductorModule\<LabVIEW
 or CSharp> directory to meet your requirements.

The operator interfaces use the TSM Application API extensively. Review the LabVIEW operator
 interface architecture to better understand how the LabVIEW source code
 is structured.

Note

Parent topic:

Operator Interfaces (TSM)

Related concepts:

- TSM Application API
- LabVIEW Operator Interface Architecture (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizing-stdf-prr-values.html language=enus -->
## TOPIC 00063: Customizing STDF PRR Field Values (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizing-stdf-prr-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizing-stdf-prr-values.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The STDF Log result processing plug-in sets the PART_ID, PART_TXT, X_COORD, and Y_COORD fields in the Part Results Record (PRR) of the STDF version 4 specification by using the values of properties on the UUT data type as described in the following table. The handler/prober driver StartOfTest entry

### Customizing STDF PRR Field Values (TSM)

The STDF Log result processing plug-in sets the PART_ID, PART_TXT, X_COORD, and Y_COORD fields in the Part Results Record (PRR) of the STDF version 4 specification by using the values of properties on the UUT data type as described in the following table. The handler/prober driver StartOfTest entry point can set any of these fields by setting the values of the output parameters to the StartOfTest entry point.

| STDF PRR Field | UUT Property | Handler/Prober StartOfTest Output Parameter |
| --- | --- | --- |
| PART_ID | SerialNumber | SitePartIds Note By default, if the handler/prober driver does not set the values in the SitePartIds parameter, TSM automatically assigns sequential numeric values to the SerialNumber property, which results in unique PART_ID field values. To disable the default behavior, set the GenerateUniquePartIds property of the NI_SemiconductorModule_StationSettings data type to False in the ConfigureStationSettings or GetStationSettings callback sequence.When the GenerateUniquePartIds property is True, TSM reassigns the same unique Part ID to the part when it is retested. Customize the behavior of GenerateUniquePartIds to assign a new unique Part ID to a part when it is retested . |
| PART_TXT | AdditionalData.NI.SemiconductorModule.PartText | SitePartTexts |
| X_COORD, Y_COORD | AdditionalData.NI.SemiconductorModule.DieCoordinates | SiteDieCoordinates |

You can modify the PART_ID field value in the test program by setting the SerialNumber property value on the UUT object. You can modify the PART_TXT field value in the test program by setting the AdditionalData.NI.SemiconductorModule.PartText property value on the UUT object. You can access the UUT object using a parameter in the PreMainSequence or PreBatch callback sequence or by using the expression RunState.Root.Locals.UUT in a Statement step.

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related concepts:

- NI_SemiconductorModule_StationSettings Data Type
- ConfigureStationSettings Callback (TSM)
- GetStationSettings Callback (TSM)
- Accessing Station Settings from a Test Program (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizing-stdf-wir-wrr-values.html language=enus -->
## TOPIC 00064: Customizing STDF WIR and WRR Field Values (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizing-stdf-wir-wrr-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizing-stdf-wir-wrr-values.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The STDF Log result processing plug-in sets the fields in the Wafer Information Record (WIR) and Wafer Result Record (WRR) of the STDF log file by using the values returned in the WaferRuntimeData parameter of the StartOfTest handler/prober driver entry point as shown in the following table. STDF WI

### Customizing STDF WIR and WRR Field Values
 (TSM)

The STDF Log result processing plug-in sets the fields in the Wafer Information
 Record (WIR) and Wafer Result Record (WRR) of the STDF log file by using the values
 returned in the WaferRuntimeData parameter of the StartOfTest
 handler/prober driver entry point as shown in the following table.

| STDF WIR or WRR Field | Handler/Prober StartOfTest Output Parameter |
| --- | --- |
| WAFER_ID | WaferRuntimeData.Identity.WaferId Note TSM automatically generates unique wafer IDs by setting the WaferRuntimeData.Identity.WaferId parameter value before calling the StartOfTest entry point. A prober driver can override the wafer IDs by modifying the parameter value. |
| FABWF_ID | WaferRuntimeData.Identity.FabWaferId |
| FRAME_ID | WaferRuntimeData.Identity.FrameId |
| MASK_ID | WaferRuntimeData.Identity.MaskId |
| USR_DESC | WaferRuntimeData.Identity.UserDescription |
| EXC_DESC | WaferRuntimeData.Identity.ExecDescription |

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizing-the-settings-table.html language=enus -->
## TOPIC 00065: Customizing the Settings Table (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizing-the-settings-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizing-the-settings-table.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The settings table on the right side of the default operator interface displays common lot and station settings. You can configure the list of settings to display in the table by editing the OISettingsTable.cfg file located in the <TestStand Application Data>\Cfg\NI_SemiconductorModule directory. Th

### Customizing the Settings Table (TSM)

The settings table on the right side of the default operator interface displays common lot and
 station settings. You can configure the list of settings to display in the table by
 editing the OISettingsTable.cfg file located in the
 <TestStand Application
 Data>\Cfg\NI_SemiconductorModule directory.
 The
 <TestStand>\Components\Schemas\NI_SemiconductorModule\OISettingsTable.xsd
 schema file describes the format of the configuration file.

The SemiconductorModuleManager class in the TSM Application API uses the OISettingsTable.cfg configuration file to determine the list of settings the GetSettingsToDisplay method returns. All default TSM operator interfaces use the GetSettingsToDisplay method to populate the settings table.

Note

OISettingsTable.cfg

OISettingsTable.cfg

Parent topic:

Customizing Operator Interfaces (TSM)

Related concepts:

- TSM Application API

Related reference:

- Operator Interface Settings Table File XML Structure (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizing-treatment-of-pre-lot-testing-failures.html language=enus -->
## TOPIC 00066: Customizing the Treatment of Pre-Lot Testing Failures

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizing-treatment-of-pre-lot-testing-failures.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizing-treatment-of-pre-lot-testing-failures.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Customize how TSM handles pre-lot testing failures. Introduced in TSM 2024 Q3.1TSM calls the HandlePreLotTestingFailures callback sequence if any site fails pre-lot testing. By default, HandlePreLotTestingFailures launches the Pre-lot Testing Failed dialog box so you can select how to proceed. To ch

### Customizing the Treatment of Pre-Lot Testing
 Failures

Customize how TSM handles pre-lot testing failures.

Introduced in
 TSM 2024 Q3.1

HandlePreLotTestingFailures

HandlePreLotTestingFailures

Pre-lot Testing
 Failed

HandlePreLotTestingFailures

1. Locate the SemiconductorModuleCallbacks.seq file in the
 <TestStand
 Public>Components\Callbacks\NI_SemiconductorModule
 directory. If the file does not exist, create it.
2. Open SemiconductorModuleCallbacks.seq and ensure that the
 file does not contain any sequences.
3. Copy the HandlePreLotTestingFailures callback sequence from
 the
 <TestStand>\Components\Modules\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq
 file to the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 file.
4. In the copy of the callback sequence, set the
 PreLotTestingFailureAction output parameter to one of the
 following values listed in the
 Locals.PreLotTestingFailureActions container. 
 OptionDescriptionEndLot
 TSM ends the lot without testing any parts.RunLotOnPassedSites
 TSM continues testing parts only on sites that passed pre-lot
 testing.Note Be careful when using this
 option. Some handlers and probers require the you disable sites
 manually. Of those handlers and probers, you must disable the sites
 manually before proceeding. By default, the
 HandlePreLotTestingFailures callback warns the
 operator before it uses this action.RerunPreLotTestsOnFailedSites
 TSM runs the PreLotTesting sequence again on sites
 that previously failed. If pre-lot testing fails again, TSM calls the
 HandlePreLotTestingFailures callback again to
 determine how to proceed.RerunPreLotTestsOnAllSites
 TSM runs the PreLotTesting sequence again on all
 sites. If pre-lot testing fails again, TSM calls the
 HandlePreLotTestingFailures callback again to
 determine how to proceed.RunLotOnAllSites
 TSM continues testing parts on all sites. The default
 HandlePreLotTestingFailures does not use the
 option.
5. Optional: 
 You can use the SemiconductorModuleManager parameter to call
 methods and properties in the TSM Application API and the
 SitesFailingPreLotTesting parameter to get the site numbers
 of the sites that failed pre-lot testing.

Parent topic:

Performing Tasks before Lot Testing Begins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=customizingt-the-lottestingcomplete-callback.html language=enus -->
## TOPIC 00067: Customizing the LotTestingComplete Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `customizingt-the-lottestingcomplete-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/customizingt-the-lottestingcomplete-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: TSM calls the LotTestingComplete callback sequence, located in the <TestStand Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq or <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq file, when a lot completes testing. Complete

### Customizing the LotTestingComplete Callback (TSM)

TSM calls the LotTestingComplete callback sequence, located in the <TestStand Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 or <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 file, when a lot completes testing.

Complete the following steps to override the default LotTestingComplete callback sequence and customize the tasks to complete when a lot completes testing.

1. Determine whether a sequence file named SemiconductorModuleCallbacks.seq 
 exists in the <TestStand Public> \Components\Callbacks\NI_SemiconductorModule 
 directory. If the sequence file does not exist, create it
 and ensure that it does not contain any sequences.
2. Copy the LotTestingComplete callback sequences from the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq 
 file to the <TestStand Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file and make changes to the copy.

Parent topic:

Performing Tasks when Lot Testing Completes (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=data-management-recommendations.html language=enus -->
## TOPIC 00068: Data Management Recommendations (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `data-management-recommendations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/data-management-recommendations.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table summarizes available data mechanisms in TestStand, in the TestStand Semiconductor Module (TSM), and in the programming environment you use. Refer to the following Data Mechanisms Selection section for more information about issues to resolve before selecting a data mechanism. Typ

### Data Management Recommendations (TSM)

The following table summarizes available data mechanisms in TestStand, in the TestStand
 Semiconductor Module (TSM), and in the programming environment you use. Refer to the
 following *Data Mechanisms Selection* section for more information about issues
 to resolve before selecting a data mechanism.

| Type of Data | Used Only in TestStand | Used Only in Code Modules | Used in TestStand and in Code Modules |
| --- | --- | --- | --- |
| Per-site | Sequence local variables and parameters TSM executes a unique run-time sequence for each site. Use the TestStand sequence local variables and parameters to create per-site variables in TestStand. | Site Data API (TSM Code Module API)Because TSM can execute a code module on multiple sites in parallel, managing per-site data in a code module can be complex. Use the use the Set Site Data VI or SetSiteData .NET method and the Get Site Data VI or GetSiteData .NET method in the TSM Code Module API to get and set arbitrary per-site data in a code module. With the site data API, you associate each per-site data value with a data ID at run time to uniquely identify the data with a name. | TestStand—Semiconductor Action step parameter Code Module—TSM Site Data API Because TestStand and TSM code modules use different data mechanisms for storing per-site data, you must pass the data between TestStand and each code module to share data. To pass per-site data stored in a TestStand variable into a code module, use the Set Site Data VI or SetSiteData .NET method and the Get Site Data VI or GetSiteData .NET method in the TSM Code Module API to create a separate code module to store the data and call the code module from a Semiconductor Action step configured to use the One thread per site value in the Multisite Option control. Pass the unique data ID and the TestStand variable as an array of one element into the code module to store the variable value in per-site data for code modules to use. To pass per-site data stored in a code module into TestStand, use the Set Site Data VI or SetSiteData .NET method and the Get Site Data VI or GetSiteData .NET method in the TSM Code Module API to create a separate code module to get the data and call the code module from a Semiconductor Action step configured to use the One thread per site value in the Multisite Option control. The code module must extract the data from the first element of the array the set data API in the TSM Code Module API returns. Pass the unique data ID and the TestStand variable to receive the data in the code module. |
| Global | Sequence file global variable (after changing Sequence File Globals option to All Executions Share the Same File Globals) You can use sequence file global variables to manage global data in TestStand, but you must change the default value of the Sequence File Globals option on the General tab of the Sequence File Properties dialog box from Separate File Globals for Each Execution to All Executions Share the Same File Globals to ensure that the sequence file global variables are shared for all sites. If you do not change the value of this option in the Sequence File Properties dialog box, the sequence file global variables store per-site data only. | Language specific data, Global Data API (TSM Code Module API) For global data used only in code modules, use the data mechanism that the language the code module uses to achieve the best performance. For example, use LabVIEW global variables or functional global variables to share global data among LabVIEW code modules. You can also use the Set Global Data VI or SetGlobalData .NET method and the Get Global Data VI or GetGlobalData .NET method in the TSM Code Module API. | TestStand—Sequence file global variable (after changing Sequence File Globals option to All Executions Share the Same File Globals) Code Module—Step module parameter To use global data in code modules and in TestStand, use sequence file global variables to manage the data in TestStand. You must change the default value of the Sequence File Globals option on the General tab of the Sequence File Properties dialog box from Separate File Globals for Each Execution to All Executions Share the Same File Globals to ensure that the sequence file global variables are shared for all sites. If you do not change the value of this option in the Sequence File Properties dialog box, the sequence file global variables store per-site data only. Within the code modules, use the data mechanism that the language the code module uses to achieve the best performance. For example, use LabVIEW global variables or functional global variables to share global data among LabVIEW code modules. You can also use the Set Global Data VI or SetGlobalData .NET method and the Get Global Data VI or GetGlobalData .NET method in the TSM Code Module API. Pass the global data into and out of code modules using parameters to the code modules. |
| Global constants | Test conditions You can use the same mechanism described in the table cell. Alternatively, you can define test conditions in the Test Program Editor. You can use the Get Test Information step to reference the test conditions in a sequence. You can create multiple test program configurations that use different values for each test condition that you define. Test conditions support only numbers, strings, and Boolean values. | Specifications You can use the same data mechanism described in the table cell. Alternatively, you can use a specifications file to define named expressions that evaluate to constants at run time. Use the Digital Pattern Editor to edit specifications files. Use the TSM Code Module API to get the value of a specification. Specifications support only numbers. | TestStand—Test conditions Code Module—Step module parameter To use global constants in code modules and in TestStand, use test conditions or a sequence file global variable to define and access the constant in TestStand. Pass the global constant into a code module using parameters to the code modules. |

TSM site numbers do not always directly correspond to test socket indexes. Use the Get Site
 Runtime Data VI or the GetSiteRuntimeData .NET method of the TSM Application API
 or use the Get Test
 Information step to obtain specific site numbers.

#### Data Mechanisms
 Selection

Before selecting a data mechanism to use, you
 must understand how and where the test program uses the data.
 Consider the following questions as you select a data
 mechanism:

- How should the test program access the data? Some data
 mechanisms work best in code modules, and others work best in TestStand. Sharing data
 between code modules and TestStand is more complicated than using the data in only one
 environment or the other. Refer to the Accessible Locations column in the following
 table.
- Where should the test program define the data? Some data
 mechanisms define the data in an external file that you access from TestStand or from code
 modules. Some data mechanisms define the data while editing the test program, and others
 create the data at run time. Refer to the Defined Location column in the following
 table.
- What type of data does the test program use? Some data
 mechanisms are limited to specific types of data, such as numbers, strings, and Boolean
 values. Refer to the Data Types column in the following table.
- Does the data remain constant throughout testing or does the
 test program modify the data? Refer to the Constant or Dynamic column in the following
 table.
- Does each site use unique data values or do all sites share the
 same data values? Refer to the Per-Site or Global column in the following table.

#### Data Mechanisms Table

The following
 table outlines the different mechanisms for managing data in TestStand, in TSM, and in the
 programming environment you use.

| Data Mechanism | Purpose | Accessible Locations | Defined Location | Data Types | Constant or Dynamic | Per-Site or Global | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Language specific data (LabVIEW global variables or .NET variables) | Manage per-site or global data in code modules | Code modules | Code module | Any language-specific type | Dynamic | Per-site or global | Difficult to manage per-site data efficiently |
| Site Data API (TSM Code Module API) | Manage per-site data in code modules | Code modules | Code module | Any language-specific type, except LabVIEW classes | Dynamic | Per-site | Does not support LabVIEW classes |
| Global Data API (TSM Code Module API) | Manage global data in code modules | Code modules | Code module | Any language-specific type, except LabVIEW classes | Dynamic | Global | Does not support LabVIEW classes; potentially slower than language-specific data |
| Step Input Data API (TSM Code Module API) | Pass per-site data from TestStand into a code module | TSM steps, code modules | TestStand variable | Numbers, strings, and Boolean values | Dynamic | Per-site | Supports only numbers, strings, and Boolean values |
| Step module parameters | Pass global data from TestStand into a code module | TSM steps, code modules | TestStand variable | Any TestStand type | Dynamic | Global | — |
| Sequence local variables and parameters | Manage per-site data in TestStand | TestStand | TestStand variable | Any TestStand type | Dynamic | Per-site | — |
| Sequence file global variables | Manage per-site data or global data in TestStand | TestStand | TestStand variable | Any TestStand type | Dynamic | Per-site or global, depending on a sequence file setting | Supports per-site or global data but not both; requires changing a sequence file setting to support global data instead of per-site data |
| Specifications | Specify constant expressions that code modules and digital timing and levels sheets use | Digital Pattern Editor, code modules | Specifications file | Numbers | Constant | Global | Supports only numbers |
| Test Conditions | Specify constant test conditions associated with current test configuration | Test Program Editor, TSM Operator Interface | Test Program Editor | Numbers, strings, and Boolean values | Constant | Global | Supports only numbers, strings, and Boolean values |
| Station and Lot Settings | Specifies settings associated with station or current lot | TSM Operator Interface | TestStand type | Any TestStand type | Constant | Global | — |

Related concepts:

- TSM Code Module API
- Semiconductor Action Options Tab
- Configuration Definition Panel
- Get Test Information Step (TSM)
- Specifications Files (TSM)
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debug-test-results-log-options.html language=enus -->
## TOPIC 00069: Debug Test Results Log Options Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debug-test-results-log-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debug-test-results-log-options.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable and configure the TSM result processing plug-ins to launch the Debug Test Results Log Options dialog box, in which you can specify settings for the Debug Test Results Log. The Debug Test Results Log Options dialog box contains the following options: Debug Test Results Log Destination Director

### Debug Test Results Log Options Dialog Box (TSM)

Enable and configure the TSM result processing plug-ins to launch the Debug Test Results Log Options dialog box, in which you can specify settings for the Debug Test Results Log.

The Debug Test Results Log Options dialog box contains the following options:

- Debug Test Results Log Destination Directory —Absolute path of the directory in which you want TSM to create the data log file. Leave the control blank if you want TSM to create the data log file in the same directory as the test program main sequence file.
- Report Orientation —Specifies the orientation of the Debug Test Results Log. The default is portrait orientation. Landscape orientation uses wider columns for tests with long test numbers or test names. Landscape orientation does not maintain report column alignment when test names exceed 101 characters.
- Log Results Only for DUT Failures —Includes results in the Debug Test Results Log only if the DUT fails testing, as determined by the bin assignment for the DUT. If a DUT passes testing, TSM does not update the Debug Test Results Log.
- Limit Number of Results Displayed in Report View —Limits the number of results to display in the report views in the TSM Operator Interface and TestStand Sequence Editor to the number of DUTs you specify.

Parent topic:

Dialog Boxes and Windows

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debug-test-results-logs.html language=enus -->
## TOPIC 00070: Debug Test Results Logs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debug-test-results-logs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debug-test-results-logs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When testing a lot, you can generate a Debug Test Results Log of human-readable text that contains the measurement values and test limits for tests on all test steps that execute on each site. The Debug Test Results Log result processor generates a separate file for each site in the test program. Yo

### Debug Test Results Logs (TSM)

When testing a lot, you can generate a Debug Test Results Log of human-readable text that
 contains the measurement values and test limits for tests on all
 test steps that execute on each site.
 The Debug Test Results Log result processor generates a separate
 file for each site in the test program. You can use this data to
 debug test and chip design issues and to diagnose test issues on the
 tester itself.

Note

- Enabling the Debug Test Results Log might affect the
 performance of a test program. Perform the following
 benchmark to ensure there is no performance loss
 when enabling the Debug Test Results Log: In the
 operator interface, enable the Debug Test Results
 Log and run the test program. When the test program
 execution completes, subtract the socket time from the cycle time displayed in the
 statistics indicator to calculate the
 tester index. If the tester
 index time is less than handler/prober index time,
 enabling the Debug Test Results Log will not impact
 performance.
- You can configure the Debug Test Results Logs in the
 Result Processing
 dialog box to display in the Report pane in the
 sequence editor and in the reports dialog box in the
 default operator interface.

The Debug Test Results Log contains the following sections for each DUT:

- Header—Contains the Site Number, Batch Number, Part ID, and state of Offline Mode for each DUT
 tested. The Batch Number refers to the loop iteration when testing multiple DUTs. The
 Debug Test Results Log result processing plug-in populates the Part ID field from the
 TestStand SerialNumber property, which TSM sets to the values returned in
 the SitePartIds parameter of the StartOfTest 
 handler/prober entry point. Note By default, if the handler/prober driver does not set the values in the
 SitePartIds parameter, TSM automatically assigns sequential
 numeric values to the SerialNumber property, which results in unique
 PART_ID field values. To disable the default behavior, set the
 GenerateUniquePartIds property of the
 NI_SemiconductorModule_StationSettings data type to False in the
 ConfigureStationSettings or GetStationSettings
 callback sequence.When the GenerateUniquePartIds
 property is True, TSM reassigns the same unique Part ID to the part
 when it is retested. Customize the behavior of GenerateUniquePartIds
 to assign a new unique Part ID to a part when it is retested .
- Step Results—Contains the Step Name, Step Result, and all the corresponding tests. If an alarm
 is raised during step execution, an alarm indicator appears in this section.
- Test Results—Contains the Test Number, Result, Test Name, Low Limit, Measurement Value,
 Correlation Offset (if used), High Limit, and Units.
- Step Alarm Information—Contains information about alarms that were raised during step
 execution..
- Part Summaries—Contains summaries for each part. Summaries include the following
 information:
  - Number of tests executed
  - Bins assigned to the part
  - Alarms that were raised while testing the part

Parent topic:

Reports and Data Logs (TSM)

Related concepts:

- Test Steps and Flow (TSM)
- Execution Timing Overview (TSM)
- Operator Interfaces (TSM)
- Offline Mode (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)
- NI_SemiconductorModule_StationSettings Data Type
- ConfigureStationSettings Callback (TSM)
- GetStationSettings Callback (TSM)
- Accessing Station Settings from a Test Program (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-lot-settings-dialog.html language=enus -->
## TOPIC 00071: Debugging the Lot Settings Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-lot-settings-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-lot-settings-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: If you customize the Lot Settings dialog box, you can use the following steps to automatically test new changes you make to the lot settings. With these settings configured, TestStand Semiconductor Module (TSM) calls the VIs directly when configuring the lot settings so any changes you make are refl

### Debugging the Lot Settings Dialog Box (TSM)

If you customize the Lot
 Settings dialog box, you can use the following steps to automatically
 test new changes you make to the lot settings. With these settings configured,
 TestStand Semiconductor Module (TSM) calls the VIs directly when configuring the lot
 settings so any changes you make are reflected immediately. You do not have to
 rebuild the packed project library.

1. Complete the following steps to configure TSM to call the Lot Settings dialog box source VIs instead of a packed project library.
  1. In the TestStand Sequence Editor, select Configure»Adapters and select LabVIEW .
  2. Click Configure and select LabVIEW Development System .
  3. Click OK in the LabVIEW Adapter Configuration dialog box.
  4. Click Done to close the Adapter Configuration dialog box.
  5. Open the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file.
  6. In the Display Configure Lot Settings Dialog step of the ConfigureLotSettings sequence, click the Module tab.
  7. Click Advanced Settings and remove the checkmark from the Always Run VI in LabVIEW Run-Time Engine checkbox.
  8. Click Close to close the LabVIEW Advanced Settings dialog box.
  9. On the Module tab, change the VI path from the default value of LotSettingsDialogs.lvlibp\Configure Lot Settings.vi to Configure Lot Settings.vi .
  10. Save the sequence file.
2. Complete the following steps to configure the Lot Settings dialog box VIs for debugging.
  1. Open the Configure Lot Settings VI.
  2. Select File»VI Properties to open the VI Properties dialog box.
  3. In the Category drop-down menu, select Window Appearance .
  4. Click Customize to open the Customize Window Appearance dialog box. View and record the current custom settings so you can restore these settings when you finish debugging.
  5. Close the Customize Window Appearance dialog box.
  6. In the VI Properties dialog box, select Default .
  7. Click OK to close the VI Properties dialog box.
  8. Save the VI.
3. Debug the Lot Settings dialog box VIs.
4. When you finish debugging the VIs, complete the following steps to restore the settings to the previous state.
  1. Open the Configure Lot Settings VI.
  2. Select File»VI Properties to open the VI Properties dialog box.
  3. In the Category drop-down menu, select Window Appearance .
  4. Select Custom and then click Customize to launch the Customize Window Appearance dialog box.
  5. Restore the custom settings you recorded in step 2d.
  6. Click OK to close the Customize Window Appearance dialog box.
  7. Click OK to close the VI Properties dialog box.
  8. Save the VI.
5. Rebuild the packed project library specification as instructed in the Customizing the Behavior for Obtaining Lot Settings topic to use the modified version of the dialog box with the restored settings.
6. Complete the following steps to restore TSM to call a packed project library instead of the Lot Settings dialog box.
  1. In the Display Configure Lot Settings Dialog step of the ConfigureLotSettings sequence, click the Module tab.
  2. Click Advanced settings and select the Always Run VI in LabVIEW Run-Time Engine checkbox.
  3. On the Module tab, set the VI path to the LotSettingsDialogs.lvlibp\Configure Lot Settings.vi .
  4. Save the sequence file.

Parent topic:

Customizing the Behavior for Obtaining Lot Settings (TSM)

Related concepts:

- Customizing the Behavior for Obtaining Lot Settings (TSM)
- Customizing the Behavior for Obtaining Station Settings (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-rf-sessions.html language=enus -->
## TOPIC 00072: Debugging RF Sessions (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-rf-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-rf-sessions.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can enable debugging for RF instruments so that you can use an NI-RFmx soft front panel to debug opened sessions for the instruments. Because enabling debugging for RF instruments might incur a performance penalty, TSM automatically disables debugging for VST and RFSA instruments on the system w

### Debugging RF Sessions (TSM)

You can enable debugging for RF instruments so that you can use an NI-RFmx soft front panel to debug opened sessions for the instruments. Because enabling debugging for RF instruments might incur a performance penalty, TSM automatically disables debugging for VST and RFSA instruments on the system when you run a test program in an operator interface. TSM automatically enables debugging for those instruments when you run a test program in the sequence editor so you can use a soft front panel to debug NI-RFmx sessions while running in the sequence editor.

To prevent TSM from automatically changing the debugging option for RF instruments, change the
 file extension on the <TestStand>\Components\Models\ModelPlugins\Addons\NI_SemiconductorModule_RFmxDebugToggle.seq
 file to something other than .seq.

Parent topic:

Debugging

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-station-settings-dialog.html language=enus -->
## TOPIC 00073: Debugging the Station Settings Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-station-settings-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-station-settings-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: If you customize the Station Settings dialog box, you can use the following steps to automatically test new changes you make to the station settings. With these settings configured, TestStand Semiconductor Module (TSM) calls the VIs directly when configuring the station settings so any changes you m

### Debugging the Station Settings Dialog Box (TSM)

If you customize the Station
 Settings dialog box, you can use the following steps to automatically
 test new changes you make to the station settings. With these settings configured,
 TestStand Semiconductor Module (TSM) calls the VIs directly when configuring the
 station settings so any changes you make are reflected immediately. You do not have
 to rebuild the packed project library.

1. Complete the following steps to configure TSM to call the Station Settings dialog box source VIs instead of a packed project library.
  1. In the TestStand Sequence Editor, select Configure»Adapters and select LabVIEW .
  2. Click Configure and select LabVIEW Development System .
  3. Click OK in the LabVIEW Adapter Configuration dialog box.
  4. Click Done to close the Adapter Configuration dialog box.
  5. Open the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file.
  6. In the Display Configure Station Settings Dialog step of the ConfigureStationSettings sequence, click the Module tab.
  7. Click Advanced Settings and remove the checkmark from the Always Run VI in LabVIEW Run-Time Engine checkbox.
  8. Click Close to close the LabVIEW Advanced Settings dialog box.
  9. On the Module tab, change the VI path from the default value of StationSettingsDialogs.lvlibp\Configure Station Settings.vi to Configure Station Settings.vi .
  10. Save the sequence file.
2. Complete the following steps to configure the Station Settings dialog box VIs for debugging.
  1. Open the Configure Station Settings VI.
  2. Select File»VI Properties to open the VI Properties dialog box.
  3. In the Category drop-down menu, select Window Appearance .
  4. Click Customize to open the Customize Window Appearance dialog box. View and record the current custom settings so you can restore these settings when you finish debugging.
  5. Close the Customize Window Appearance dialog box.
  6. In the VI Properties dialog box, select Default .
  7. Click OK to close the VI Properties dialog box.
  8. Save the VI.
3. Debug the Station Settings dialog box VIs.
4. When you finish debugging the VIs, complete the following steps to restore the settings to the previous state.
  1. Open the Configure Station Settings VI.
  2. Select File»VI Properties to open the VI Properties dialog box.
  3. In the Category drop-down menu, select Window Appearance .
  4. Select Custom and then click Customize to launch the Customize Window Appearance dialog box.
  5. Restore the custom settings you recorded in step 2d.
  6. Click OK to close the Customize Window Appearance dialog box.
  7. Click OK to close the VI Properties dialog box.
  8. Save the VI.
5. Rebuild the packed project library specification as instructed in the Customizing
 the Behavior for Obtaining Station Settings topic to use the modified
 version of the dialog box with the restored settings.
6. Complete the following steps to restore TSM to call a packed project library instead of calling the VIs directly.
  1. In the Display Configure Station Settings Dialog step of the ConfigureStationSettings sequence, click the Module tab.
  2. Click Advanced settings and select the Always Run VI in LabVIEW Run-Time Engine checkbox.
  3. On the Module tab, set the VI path to the StationSettingsDialogs.lvlibp\Configure Station Settings.vi .
  4. Save the sequence file.

Parent topic:

Customizing the Behavior for Obtaining Station Settings (TSM)

Related concepts:

- Customizing the Behavior for Obtaining Station Settings (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-test-programs.html language=enus -->
## TOPIC 00074: Debugging Test Programs in Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-test-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-test-programs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although simulated instruments behave as closely as possible to real instruments, measurements and data differ in Offline Mode. Additionally, custom code that processes results, test time performance, instrument functionality, and error reporting might differ in Offline Mode and can result in differ

### Debugging Test Programs in Offline Mode (TSM)

Note

You can use standard debugging techniques and tools, such as InstrumentStudio, the Digital Pattern Editor, and standard or custom soft front panels to interact with simulated instruments and data in Offline Mode. You can also use LabVIEW and .NET debugging tools to debug applications.

Parent topic:

Offline Mode Workflow (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-teststand-test-programs.html language=enus -->
## TOPIC 00075: Debugging TestStand Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-teststand-test-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-teststand-test-programs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn common ways to debug TestStand test programs, including how to control and inspect sequence execution by using breakpoints, watch expressions, and execution tools. Also learn how to debug code modules and related files—such as LabVIEW VIs, packed libraries, DLLs, and .NET assemblies. Consider

### Debugging TestStand Test Programs

Learn common ways to debug TestStand test programs, including how to control and
 inspect sequence execution by using breakpoints, watch expressions, and execution
 tools. Also learn how to debug code modules and related files—such as LabVIEW VIs,
 packed libraries, DLLs, and .NET assemblies.

Consider the following common approaches to debug the following components of a TestStand test program.

#### Sequence
 Execution

Sequences can be in a running or suspended testing state. Testing runs
 when continuously testing DUTs. When testing runs, each test socket
 executes tests for one DUT. TestStand suspends testing when one or
 more TestStand test socket executions suspends at a breakpoint. One
 test socket can suspend while other test sockets run. The Execution
 window background changes to yellow to indicate a suspended
 execution. You can examine sequence variables only in suspended
 executions.

Use the following techniques to debug sequence execution:

- Set Sequence Breakpoints—To suspend testing at a specific step,
 set a breakpoint on the step. To set a Sequence
 breakpoint: Testing suspends when the execution reaches the step
 breakpoint. A yellow arrow icon, called the execution
 pointer, appears on the left of the step. The execution
 pointer indicates the next step to execute when testing
 resumes. Click the breakpoint icon to remove the
 breakpoint.
  1. In the Steps pane of the Sequence File or in the
 Execution window, click in the column to the left
 of the step name.
  2. Right-click the breakpoint stop sign icon and
 select Breakpoint»Breakpoint Settings . The Breakpoint Settings dialog box
 launches.
  3. In the Breakpoint Setting dialog box, specify an
 expression to set a conditional breakpoint.
- Set Data Breakpoints —You can suspend testing when the
 value of a variable changes or when it has a specific value.
 In this scenario, use the Watch View pane to enter an
 expression for the variable. Then, edit the watch expression
 to specify a break condition. TestStand evaluates these
 break conditions when each step executes. TestStand then
 suspends the testing if the variable meets the break
 conditions. Note Delete unneeded watch expressions.
 Unnecessary watch expressions can negatively affect
 execution performance.
- Control Test Program and Step Execution—You can control test
 program and step execution in one of the following places
 during testing suspension:
  - The Debug menu or Debug toolbar
  - The Steps pane context menu in the Execution
 window
  - Debug Menu/Toolbar
    - Step Into —Enters and
 suspends inside the code module associated with
 the step to which the execution pointer
 points.
    - Step Over —Executes the
 step to which the execution pointer points and
 suspends execution on the next step in the
 sequence.
    - Step Out —Resumes
 execution through the end of the current sequence
 and suspends execution on the next step in the
 calling sequence.
  - Steps Pane Context Menu
    - Run Mode»Skip (temporarily skips step)—Select
 Skip to prevent the step
 from executing in the current execution. Changing
 the step run mode in an execution does not persist
 the setting to the step in the sequence file.
 Consequently, after execution ends, the setting
 reverts to the original run mode that preceded the
 change. Change the run mode on the step in the
 Sequence File window to persist the setting in the
 sequence file.
    - Set Next Step to Cursor —Moves the execution pointer to point
 to a different step to change which step executes
 next.
    - Run Selected
 Steps —Select one or more arbitrary
 steps in the sequence to execute before resuming
 normal execution. TestStand executes the selected
 steps in the order the steps appear in the
 sequence. If a breakpoint suspends execution of
 the selected steps, the Steps pane displays the
 interactive execution pointer. The interactive
 execution pointer differs from the normal
 execution pointer.
- View and Modify Variable and Expression Values —Use the
 following techniques to view or modify variable values and
 to monitor expression values:
  - When testing is suspended, use the Variables
 pane to view and modify the values of any
 variables and properties that are accessible in
 the current execution context.
  - To monitor the value of an expression while
 testing, enter the expression in the Watch
 View pane when testing is suspended. You can
 also use the Edit Breakpoints/Watch
 Expression dialog box to enter expressions
 when testing is not in progress. When you enable
 tracing, the sequence editor updates the values
 after each step executes.
- Display Debug Messages —To display messages to the
 Output pane while testing, use the OutputMessage expression
 function in a Statement step.
- Use Execution Profiler —The Execution Profiler 
 records the following types of data: event, operation, item, thread, and execution data,
 .
  - Event data
  - Operation data
  - Item data
  - Thread data
  - Execution data—This data includes the duration
 of steps, code modules, and other resources a
 multithreaded TestStand system uses over a period
 of time.

#### Code Modules and
 Related Files

The TestStand Sequence Editor integrates
 with common code module development environments to help streamline
 debugging tasks.

#### LabVIEW

When executing VIs in the LabVIEW Development System, you can debug the
 VI code modules loaded in memory. To debug using this method, set
 breakpoints and probes in the VIs. When setting these breakpoints
 and probes, you must use the same version of LabVIEW in which the
 VIs are executing. After the TestStand execution reaches the VI, the
 first breakpoint is triggered in a new instance of the VI. Add
 additional breakpoints or probes to this instance of the VI, if
 necessary. To make changes to the VI after debugging, right-click
 the front panel of the debugging instance of the VI and select Remote Debugging»Quit Debug Session.

The LabVIEW Development System can also debug applications that
 execute VIs using the LabVIEW Runtime. Such applications include VIs
 executed using the TestStand LabVIEW Adapter and
 LabVIEW-built DLLs executed using the TestStand C/C++ DLL
 Adapter.

When the TestStand LabVIEW Adapter loads a VI code module, it
 reserves the VI in LabVIEW to prevent edits to the VI. To edit a
 reserved VI, you must first unload the step code module. Click the
 Unload and Open VI button on the
 LabVIEW Module tab to unload a
 LabVIEW step code module and open the VI for editing. The button is
 enabled only if all executions are suspended. If the button tooltip
 is disabled due to actively running executions, use the
 Break All button on the
 Debug toolbar to suspend all
 executions.

You can also use the LabVIEW Desktop Execution Trace Toolkit to collect
 various types of trace data from LabVIEW applications.

#### Packed
 Libraries

LabVIEW packed libraries, or .lvlibp files, contain
 compiled LabVIEW code that you can execute from TestStand. By
 default, you cannot debug VIs in packed libraries as these VIs do
 not contain any source code. To create a packed library that you can
 debug, select the Enable Debugging option in
 the Advanced page of the Packed Library Properties dialog box. You
 can debug VIs in a debuggable packed library the same way you debug
 stand-alone VIs. To debug these VIs, execute the VIs using the
 Development System option in the
 TestStand LabVIEW Adapter Configuration dialog
 box.

#### LabVIEW,
 LabWindows/CVI, and .NET DLLs

To debug a DLL TestStand calls, first create the DLL with debugging
 enabled in the application development environment (ADE). Then,
 launch the TestStand Sequence Editor or TestStand User
 Interface executable from the ADE. You can also attach
 the DLL to the sequence editor or user interface process from the
 ADE, when supported.

#### .NET

To debug a .NET assembly, first open the source code project in
 Microsoft Visual Studio and ensure the output
 assembly is configured and built with debugging enabled. Then, use
 Visual Studio to launch the sequence editor or user
 interface as the Start action for the project. Alternatively, use
 Visual Studio to attach to an in-progress instance
 of the sequence editor or user interface process.

You cannot
 view any TestStand sequence variables or interact with the
 TestStand Sequence Editor user interface while
 suspended at a breakpoint in Visual
 Studio.

Visual Studio 2019 version 16.11
 and later provides a feature called Hot Reload. The Hot
 Reload feature enables you to edit code modules and
 apply the code changes immediately to a running application. Once
 Visual Studio applies the code changes, the new
 code is in effect the next time your application executes the code.
 To use this feature with Visual Studio 2019, NI recommends starting
 the debugging process from Visual Studio. To use this feature with
 Visual Studio 2022, use either of the options in the following
 table:

| Starting the Process from Visual Studio | Attaching to an In-Progress Process |
| --- | --- |
| Open the project to debug in Visual Studio. Set the Start action for the project to Start external program. Then, enter the file path of the executable for the sequence editor or user interface you are debugging, including the .exe file extension. Refer to Configuring Sequence Editor and User Interface Startup Options for more information. Press F5 or select Start Debugging to start the application and attach Visual Studio. | Before you start the debugging process, create an environment variable named COMPLUS_ForceENC with a value of 1. Open the project to debug in Visual Studio. Select Attach to Process in the Debug menu to attach Visual Studio to an in-progress process. |

Note

COMPLUS_ForceENC

COMPLUS_ForceENC

Hot Reload

- Hot Reload (Visual Studio
 2022)
- Apply Code Changes (Visual Studio
 2019)

Note

Visual Studio

Hot Reload

Visual Studio

Stop Debugging

Visual Studio

Visual Studio

If you are not using Hot Reload, you cannot
 modify .NET assemblies while TestStand has the assemblies loaded.
 TestStand typically loads assemblies automatically when starting
 executions. These assemblies might remain loaded after execution
 completes unless you explicitly unload them. Before you can
 successfully rebuild a .NET assembly loaded by TestStand, you must
 unload the assembly and all other assemblies the .NET Adapter is
 using from within the TestStand Sequence Editor. Closing the
 TestStand process unloads all assembly references.

#### Unloading an Assembly

1. End and close all execution windows.
2. Clear any references to .NET objects stored in station
 globals.
3. Select File»Unload All Modules .

To unload .NET code modules, TestStand must unload the .NET
 appdomain that it uses with the .NET Adapter and can do so safely
 only when the .NET appdomain is no longer in use.

#### Analysis and Rule
 Configuration Modules

If you use the TestStand Sequence Analyzer, you can debug custom
 analysis modules and rule configuration modules by setting a
 breakpoint in the module and then calling the module from the
 TestStand Sequence Analyzer.

#### Memory
 Management

Visit ni.com/info and enter the Info Code
 tsmemory to access the 
 tutorial. This tutorial provides information about efficiently
 managing memory in test sequences and code modules.

#### Deployments

Ensure that you have followed the suggested deployment process to plan,
 design, implement, execute, and validate a full or patch deployment
 for a TestStand-based test system.

The TestStand Deployment Utility generates several errors and warnings
 specifically related to debugging patch deployments. Additionally,
 you can use the Build Status tab of the deployment utility
 to view information about the patch deployment.

Parent topic:

Debugging

Related information:

- TestStand Directory Structure
- Debugging Code Module VIs with LabVIEW
- Debugging and Tracing of VIs Executed Using the LabVIEW Runtime
- Reserving Loaded VIs for Execution
- Tracing with the DETT
- Debugging DLLs
- Debugging .NET Assemblies
- Troubleshooting Memory Growth Issues in TestStand Systems
- Deployment Process Overview
- Before You Begin
- Deploying TestStand Systems
- Patching Deployments
- Debugging a Patch Deployment
- Write and Debug Running Code with Hot Reload in Visual
 Studio
- Configuring Sequence Editor and User Interface Startup
 Options

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging-tsm-test-programs.html language=enus -->
## TOPIC 00076: Debugging TSM Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging-tsm-test-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging-tsm-test-programs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to following common approaches to debug components of a TestStand test program, consider the following additional approaches to debug components of a TSM test program Sequence Execution Sequences can be in a running or suspended testing state. Testing is running when continuously testing

### Debugging TSM Test Programs

In addition to following common approaches to debug components of a TestStand test program, consider the
 following additional approaches to debug components of a TSM test
 program

#### Sequence
 Execution

Sequences can be in a running or suspended
 testing state. Testing is running when continuously testing DUTs.
 When testing is running, each test socket is executing tests for one
 DUT. Testing is suspended when one or more TestStand test socket
 executions are suspended at a breakpoint. One test socket can be
 suspended while other test sockets are running. The background of
 the Execution window changes to yellow to indicate that the
 execution is suspended. You can examine sequence variables only in
 executions that are suspended.

Pausing a lot does not suspend
 executions the way using the default TestStand Sequence Editor Debug»Break or Break All menu items do.
 When you pause a lot with the Pause button,
 testing continues until each site completes testing its current DUT.
 The executions then wait for operator input before sending the End
 of Test signal to the handler or prober and proceeding with testing
 the next batch of DUTs. To suspend test socket executions to examine
 variables or to step into code modules, set a breakpoint on the step
 where you want to suspend. You cannot examine variables in the
 sequence editor for executions that are not suspended, even if they
 are paused between DUTs.

Use the following techniques to debug
 TSM sequence execution:

- Use TSM Toolbar —Use the TSM toolbar buttons to control
 execution and view lot statistics while debugging a
 sequence. Avoid using the default TestStand Sequence Editor Debug»Terminate , Terminate All ,
 Abort , and Abort
 All menu items because they might not
 clean up and close instrument sessions correctly.
- Step Into TSM Steps—For Semiconductor Multi Test and
 Semiconductor Action steps that execute test code for
 multiple sites, the test sockets for all the sites that the
 step is testing must be suspended at the same step before
 you can use the Step Into Debug menu item or toolbar button.
 For LabVIEW 2020 and newer, when you step into a VI from
 TestStand and click Run , TSM opens
 the block diagram, suspends execution on the first node, and
 automatically enables Retain Wire
 Values . You can also edit the executing VI in
 LabVIEW and continue execution of the lot in
 TestStand.

#### Lot Statistics
 Viewer

To monitor the bin counts for each site while
 testing in the sequence editor, use the Lot Statistics Viewer, in which you can
 view lot statistics while running or debugging a sequence in the
 sequence editor. You can also control test program execution in the
 Lot Statistics Viewer.

#### Simulated Handler or
 Prober

When developing, testing, or debugging a
 semiconductor test program, the test developer might not have access
 to a real handler or prober. In such cases, the
 test developer can use the NI Built-in Simulated Handler Driver to
 verify that the test program behaves correctly without a handler or
 prober.

Parent topic:

Debugging

Related concepts:

- Debugging TestStand Test Programs
- Editing an Executing VI in LabVIEW
- Lot Statistics Viewer (TSM)
- Configuring Handler or Prober Support for a Test Program (TSM)
- NI Built-in Simulated Handler Driver (TSM)

Related reference:

- Semiconductor Module Toolbar Buttons

<!--NI_TOPIC bundle=teststand-semiconductor-module path=debugging.html language=enus -->
## TOPIC 00077: Debugging

- bundle_id: `teststand-semiconductor-module`
- source_path: `debugging.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/debugging.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following information to learn about debugging your test programs.Debugging TestStand Test ProgramsDebugging TSM Test ProgramsEditing an Executing VI in LabVIEWDebugging RF SessionsCustom Instrument PanelsViewing Multisite Data in Code Modules

### Debugging

- Debugging TestStand Test Programs
- Debugging TSM Test Programs
  - Editing an Executing VI in LabVIEW
- Debugging RF
 Sessions
- Custom Instrument
 Panels
- Viewing Multisite
 Data in Code Modules

Related concepts:

- Debugging TestStand Test Programs
- Debugging TSM Test Programs
- Editing an Executing VI in LabVIEW
- Debugging RF Sessions (TSM)
- Custom Instrument Panels (TSM)
- Viewing Multisite Data in Code Modules (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=default-tsm-oi.html language=enus -->
## TOPIC 00078: Running a Test from a Default TSM Operator Interface

- bundle_id: `teststand-semiconductor-module`
- source_path: `default-tsm-oi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/default-tsm-oi.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to test a lot using the TSM default LabVIEW operator interface or the STS Operator Tool interface. Default LabVIEW Operator Interface Launch the operator interface. When the Login dialog box launches, enter or select a username and enter the password. Complete the follow

### Running a Test from a Default TSM Operator Interface

Complete the following steps to test a lot
 using the TSM default LabVIEW operator interface or the STS Operator Tool
 interface.

#### Default LabVIEW Operator Interface

1. Launch the operator interface.
2. When the Login dialog box launches, enter or select a username and enter the
 password.
3. Complete the following steps to configure the lot.
  1. Click Configure Lot .
  2. Enter the lot information in the Configure Lot Settings dialog box and click
 OK .
4. Click Start Lot to begin testing at lot. Use the
 Pause and Resume buttons to
 pause the lot between DUTs. To test a single batch of DUTs and automatically
 pause after testing of those DUTs completes, click Single
 Test .
5. Click End Lot to stop testing the lot.
6. Repeat steps 3–5 to test a new lot.
7. Click View Mid-Lot Summary to generate and display a
 Mid-Lot
 Summary test report. You can view, refresh, and print the report any
 time during or after testing.
8. Click View Reports to view
 reports for the current lot any time during or after testing.
9. Click the Exit button to close the test application.

#### Default STS Operator Tool Interface

1. Launch the operator interface.
2. When the Login dialog box launches, enter or select a username and enter the
 password.
3. Complete the following steps to configure the lot.
  1. Select Configure Lot from the drop-down
 menu.
  2. Enter the lot information in the Configure Lot Settings dialog box and click
 OK .
4. Click Start Lot to begin testing at lot. Use the
 Pause and Resume buttons to
 pause the lot between DUTs. To test a single batch of DUTs and automatically
 pause after testing of those DUTs completes, click Single
 Test .
5. Click the End Lot button to stop testing the lot.
6. Repeat steps 3–5 to test a new lot.
7. Select View Mid-Lot Summary from the drop-down menu to
 generate and display a Mid-Lot Summary test report. You can view, refresh, and
 print the report any time during or after testing.
8. Select View Reports from the drop-down menu to view
 reports for the current lot any time during or after testing.
9. Click the X button to close the test application.

Parent topic:

Operator Interfaces (TSM)

Related concepts:

- Operator Interfaces (TSM)
- Configure Lot Settings Dialog Box (TSM)
- Lot Summary Reports (TSM)
- Reports and Data Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=deploy-lv-code-module.html language=enus -->
## TOPIC 00079: Deploying LabVIEW Code Modules with TSM Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `deploy-lv-code-module.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/deploy-lv-code-module.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Build LabVIEW code modules into packed project libraries for deployment by enabling the Output VIs to a Packed Project Library option in the LabVIEW VI Options dialog box of the deployment utility. Benefits of using packed project libraries include faster load and execution times, less disk space, a

### Deploying LabVIEW Code Modules with TSM Test Programs

Build LabVIEW code modules into packed project libraries for deployment by enabling the Output VIs to a Packed Project Library option in the LabVIEW VI Options dialog box of the deployment utility. Benefits of using packed project libraries include faster load and execution times, less disk space, and automatic version control for installers.

If you need to debug a test program on a production system, NI recommends that you build separate release and debug deployment installers. In the debug deployment, enable the Enable Debugging option in the LabVIEW VI Options dialog box to create a debuggable version of the packed project library that includes LabVIEW block diagrams for the VIs the packed project library contains. When debugging is enabled, you can debug VIs in the library on a target system with the LabVIEW Development System installed. NI recommends debug versions of the packed project libraries only for debugging, not for production testing, because the debug versions have a negative performance impact and use more memory.

You cannot modify VIs in a packed project library, even when you enable the Enable Debugging option. Enable the Include Source for Rebuilding Packed Project Libraries option in the Packed Project Library Options dialog box to include the source VIs for the packed project library in the deployment if you need to modify the VIs and then rebuild the packed project library on a target system.

Parent topic:

Deploying TSM Test Programs

Related information:

- Customizing Components You Deploy
- Debugging and Tracing of VIs Executed Using the LabVIEW Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=deploying-dotnet-code-modules.html language=enus -->
## TOPIC 00080: Deploying .NET Code Modules with TSM Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `deploying-dotnet-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/deploying-dotnet-code-modules.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends that you do not include the TSM Code Module API assembly (NationalInstruments.TestStand.SemiconductorModule.CodeModuleAPI.dll) or any referenced NI hardware assemblies in a test program deployment. Instead, use TSM or corresponding driver installer to install these components as part o

### Deploying .NET Code Modules with TSM Test Programs

NI recommends that you do not include the TSM Code Module API assembly (NationalInstruments.TestStand.SemiconductorModule.CodeModuleAPI.dll) or any referenced NI hardware assemblies in a test program deployment. Instead, use TSM or corresponding driver installer to install these components as part of the system configuration to help ensure a stable test system configuration.

If you need to debug a test program on a production system, NI recommends that you create
 separate release and debug deployments. In the debug deployment,
 include the code module assembly built with a debug configuration
 and the program database file
 (<assembly_name>.pdb
 file) that contains the debug symbols for the assembly. NI
 recommends debug versions of the assemblies only for debugging, not
 for production testing, because the debug versions negatively affect
 performance and use more memory.

Parent topic:

Deploying TSM Test Programs

Related concepts:

- TSM Code Module API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=deploying-tsm-test-programs.html language=enus -->
## TOPIC 00081: Deploying TSM Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `deploying-tsm-test-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/deploying-tsm-test-programs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the TestStand Deployment Utility to deploy a test program. Complete the following steps on the Mode tab of the deployment utility: Select the Deployable Image Only option.Select the Create new Full Deployment option. NI recommends that you create a new Full Deploy

### Deploying TSM Test Programs

Complete the following steps to use the TestStand Deployment Utility to deploy a test program.

1. Complete the following steps on the Mode tab of the deployment utility:
  1. Select the Deployable Image Only option.
  2. Select the Create new Full Deployment option.
 NI recommends that you create a new Full Deployment, save the deployment to increment the Deployment Version , and store the deployment in a source code control system each time you create or update a deployment.
2. Complete the following steps on the System Source tab:
  1. Place a checkmark in the From Directory checkbox and specify the test program directory.
  2. Place a checkmark in the Include Subdirectories checkbox.
  3. In the Location of Deployable Image field, specify the location in which to save the deployable image.
3. Click the Distributed Files tab and select Yes to analyze the source files.
4. Click the Build Status tab to display the analysis results. Resolve any issues before completing the next step.
5. Complete the following steps on the Distributed Files tab:
  1. Select the files to include in the distribution. Use the Distributed Files pull-down menu to filter the display.
  2. Click the LabVIEW Options button to launch the LabVIEW VI Options dialog box, which you use to specify LabVIEW options.
6. In the LabVIEW VI Options dialog box, enable the following options in the Packed Project Library Options section of the dialog box and use the default values for the other options in this dialog box.
 

 Enabling these options increases the size of the distribution but allows the test program to more easily run in the LabVIEW Run-Time Engine (RTE).
  - Output VIs to a Packed Project Library ()
  - Copy files from vi.lib before Build
  - Copy files from user.lib before Build
  - Copy files from instr.lib before Build
7. Click OK in the LabVIEW VI Options dialog box.
8. Complete the following steps on the Distributed Files tab:
  1. Click the Save As button if this is the first time you are configuring a deployment for the test program to save the distribution configuration for the deployment. Click the Save button when you modify an existing deployment to increment the version number of the deployment.
  2. Click the Build button to build the distribution.
  3. Click the Save button to auto-increment the Deployment Version field on the Mode tab.
9. Complete the remaining tasks in the Deployment Process Overview to transfer the deployment to a tester and validate the deployment.

Consider the NI recommendations for installers, LabVIEW
 code modules, .NET code modules, and protections for
 test programs and test limits as you design and create deployments for a
 semiconductor test system.

Related concepts:

- Installer Settings for Deploying TSM Test Programs
- Deploying LabVIEW Code Modules with TSM Test Programs
- Deploying .NET Code Modules with TSM Test Programs
- Protecting Test Programs and Test Limits from Editing and Viewing (TSM)

Related information:

- Deploying TestStand Systems
- Deployment Process Overview

<!--NI_TOPIC bundle=teststand-semiconductor-module path=dialog-boxes-and-windows.html language=enus -->
## TOPIC 00082: Dialog Boxes and Windows

- bundle_id: `teststand-semiconductor-module`
- source_path: `dialog-boxes-and-windows.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/dialog-boxes-and-windows.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Familiarize yourself with the setting in the various TSM dialog boxes and windows.

### Dialog Boxes and Windows

Familiarize yourself with the setting in the various TSM dialog boxes and windows.

Parent topic:

Environment Reference

<!--NI_TOPIC bundle=teststand-semiconductor-module path=digital-pattern-project-panel.html language=enus -->
## TOPIC 00083: Digital Pattern Project Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `digital-pattern-project-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/digital-pattern-project-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Digital Pattern Project panel contains the following options: Digital Pattern Project File Path—Specifies the pathname of the digital pattern project file to use in the test program. A red exclamation point indicates that an issue exists for the file. A tooltip displays the error message. Do not

### Digital Pattern Project Panel

The Digital Pattern Project panel contains the following options:

- Digital Pattern Project File Path —Specifies the pathname of the digital
 pattern project file to use in the test program. A red
 exclamation point indicates that an issue exists for
 the file. A tooltip displays the error message. Do
 not proceed without reviewing the errors for the
 file.
- Open file for edit 
 —Launches the digital pattern project file in the Digital
 Pattern Editor.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=digital-patterns.html language=enus -->
## TOPIC 00084: Digital Patterns (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `digital-patterns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/digital-patterns.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Digital pattern files contain a collection of vectors, or instructions, to execute on an NI-Digital Pattern instrument. Components of the binary pattern file include time sets, labels, opcodes, vector numbers, pin state data that indicates drives and compares, and comments for each vector. You can e

### Digital Patterns (TSM)

Digital pattern files contain a collection of vectors, or instructions, to execute on an NI-Digital Pattern instrument. Components of the binary pattern file include time sets, labels, opcodes, vector numbers, pin state data that indicates drives and compares, and comments for each vector. You can edit pattern files in the Digital Pattern Editor.

#### TSM
 Implementation

Select Semiconductor Module»Launch Digital Pattern Editor or click the Launch Digital Pattern
 Editor[IMAGE alt='image' src='GUID-026EB6E7-4B7B-471B-B4FC-D92BB577C71A-a5.png'] button on the
 TSM toolbar to open digital pattern project files in the Digital
 Pattern Editor. Additionally, you can use the Digital Pattern
 Project panel of the Test Program Editor to specify the pathname of
 the digital pattern project file to use in the test program.

The TSM Pin Map Editor and pin map schema natively support NI-Digital
 Pattern instruments.

Use the TSM Code Module API for the NI-Digital Pattern instruments to
 manage digital pattern instruments and sessions, to manage digital
 pattern waveform data, and to access digital pattern project
 files.

Note

You can create a basic test program from a digital pattern project.
 Select Semiconductor Module»Create Test Program from Digital Pattern
 Project to launch the Create Test Program from Digital
 Pattern Project dialog box.

Related concepts:

- Digital Pattern Project Panel
- Test Program Editor (TSM)
- Pin Map Editor (TSM)
- TSM Code Module API

Related reference:

- Pin Map File XML Structure (TSM)

Related information:

- Create Test Program from Digital Pattern Proje…

<!--NI_TOPIC bundle=teststand-semiconductor-module path=disable-tracing-in-teststand.html language=enus -->
## TOPIC 00085: Disable Tracing in TestStand (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `disable-tracing-in-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/disable-tracing-in-teststand.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Enabling tracing to display each step as it executes is useful for debugging but adds significant performance overhead to the execution of test programs in the TestStand Sequence Editor and in the TestStand Semiconductor Module (TSM) operator interface. TSM automatically disables tracing for operato

### Disable Tracing in TestStand (TSM)

Enabling tracing to display each step as it executes is useful for debugging but adds significant
 performance overhead to the execution of test programs in the
 TestStand Sequence Editor and in the TestStand Semiconductor Module
 (TSM) operator interface. TSM automatically disables tracing for
 operator interfaces. Typically, you do not need to disable tracing
 unless a custom operator interface enables tracing.

Complete the following steps to disable tracing from the sequence editor.

1. Select Configure»Station Options to launch the Station Options dialog
 box.
2. On the Execution tab, disable the Enable Tracing 
 option.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=disable-unnecessary-result-processors.html language=enus -->
## TOPIC 00086: Disable Unnecessary Result Processors (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `disable-unnecessary-result-processors.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/disable-unnecessary-result-processors.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: For each result processor enabled in the Result Processing dialog box, TestStand calls sequences associated with the result processor to process test results during testing, which can add time to test execution. Although the TestStand Semiconductor Module (TSM) STDF Log generator, Lot Summary Report

### Disable Unnecessary Result Processors (TSM)

For each result processor enabled in the Result Processing dialog box, TestStand calls sequences
 associated with the result processor to process test results during
 testing, which can add time to test execution. Although the
 TestStand Semiconductor Module (TSM) STDF Log generator, Lot Summary
 Report generator, and CSV Test Results Log generator do not
 contribute significantly to test execution time, the TestStand
 Report generator and TSM Debug Test Results Log generator can cause
 performance and memory usage issues. To limit the effect of the
 Debug Test Results Log generator, enable the Limit Number
 of Results Displayed in Report View option or
 the Log Results Only for DUT Failures option
 in the Debug Test Results Log Options dialog
 box. Disable any result processors you do not need during production
 testing.

Complete the following steps to disable result processors from the TestStand Sequence Editor.

1. Select Configure»Result Processing to launch the Result
 Processing dialog box.
2. Remove the checkmark from the Enabled option for the result processor you want to disable.

Complete the following steps to disable result processors from the TSM Operator Interface.

1. Click the Configure Station button to launch the Configure
 Station Settings dialog box.
2. On the Advanced tab, click the Result Processing 
 button to launch the Result Processing dialog box.
3. Remove the checkmark from the Enabled option for the result processor you want to disable.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

Related concepts:

- Debug Test Results Log Options Dialog Box (TSM)
- Configure Station Settings Dialog Box (TSM)
- Advanced Tab

<!--NI_TOPIC bundle=teststand-semiconductor-module path=disabling-offline-mode.html language=enus -->
## TOPIC 00087: Disabling Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `disabling-offline-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/disabling-offline-mode.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor Module»Disable Offline Mode or click the Disable Offline Mode button on the TSM toolbar to disable Offline Mode and return to the default behavior of TSM. The Disable Offline Mode button icon changes to indicate the current state of Offline Mode and the main menu bar no longer d

### Disabling Offline Mode (TSM)

Select Semiconductor Module»Disable Offline Mode or click the
 Disable Offline Mode[IMAGE alt='image' src='GUID-E0419593-1D7B-46BC-9CC3-46B3E3CBF2BB-a5.png'] button on the TSM toolbar to disable Offline Mode and return to the default behavior of
 TSM. The Disable Offline Mode button icon changes to indicate the
 current state of Offline Mode and the main menu bar no longer displays the
 Offline Mode indicator. The OfflineMode property
 of the NI_SemiconductorModule_StandardStationSettings data type also indicates the current
 state of Offline Mode.

When you disable Offline Mode, TSM deletes simulated versions of all the instruments defined in the Offline Mode system configuration file.

Parent topic:

Offline Mode Workflow (TSM)

Related concepts:

- Accessing Station Settings from a Test Program (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=display-specific-site-number.html language=enus -->
## TOPIC 00088: Displaying Specific Site Numbers in Operator Interfaces (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `display-specific-site-number.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/display-specific-site-number.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disable specific sites or use the particular connections of a pin map that match the DIB for the test station. When you disable sites in the default Configure Lot Settings dialog box or use the AvailableSiteNumbers property on the NI_SemiconductorModule_StationSettings data type to specify w

### Displaying Specific Site Numbers in Operator Interfaces (TSM)

You can disable specific sites or use the particular connections of a pin map that match the DIB for the test station.

When you disable sites in the default
 Configure Lot Settings
 dialog box or use the AvailableSiteNumbers property
 on the
 NI_SemiconductorModule_StationSettings
 data type to specify which site numbers from a pin map for a test
 program to use when running the test program, the default TSM
 operator interfaces display only the sites you specify.

TSM 2016 and earlier default operator interfaces and custom operator interfaces based on those
 versions display site numbers starting at 0 and increasing by 1, up
 to the number of sites. You must make the following changes to
 custom LabVIEW or C# operator interfaces based on the TSM
 2016 and earlier operator interfaces to display the configured site
 numbers when you disable sites in the default Configure Lot Settings
 dialog box or use the AvailableSites station setting:

- Query the Semiconductor Module Manager to retrieve information about which site numbers the running test program includes.
- Update the site status labels to show the correct site numbers.
- Update the bin table to show the correct site numbers.
- Update code to avoid an error in the case that the Semiconductor Module Manager is using 0 sites, which can happen only when you disable sites in the default Configure Lot Settings dialog box or use the AvailableSites station setting.

Parent topic:

Customizing Operator Interfaces (TSM)

Related concepts:

- Configure Lot Settings Dialog Box (TSM)
- NI_SemiconductorModule_StationSettings Data Type

Related tasks:

- Displaying Specific Site Numbers in Custom LabVIEW Operator Interfaces (TSM)
- Displaying Specific Site Numbers in Custom C# Operator Interfaces (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=displaying-site-numbers-lv-oi.html language=enus -->
## TOPIC 00089: Displaying Specific Site Numbers in Custom LabVIEW Operator Interfaces (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `displaying-site-numbers-lv-oi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/displaying-site-numbers-lv-oi.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You must complete the following steps to modify custom LabVIEW operator interfaces based on TSM 2016 and earlier operator interfaces to display the configured site numbers when you disable sites in the default Configure Lot Settings dialog box or use the AvailableSites station setting. Refer to the

### Displaying Specific Site Numbers in Custom LabVIEW Operator Interfaces (TSM)

You must complete the following steps to modify custom LabVIEW operator interfaces based on TSM 2016 and earlier operator interfaces to display the configured site numbers when you disable sites in the default Configure Lot Settings dialog box or use the AvailableSites station setting. Refer to the LabVIEW source code for the operator interface for an example.

1. Open a copy of the
 LVSemiOI.lvproj project in the <TestStand
 Public> \UserInterfaces\NI_SemiconductorModule\<LabVIEW> 
 directory.
2. Complete the following steps to update the site status labels to show the correct site numbers.
  1. Open the Controls/Site Label.lvclass/Site Label.ctl control.
  2. Change the label for the numeric in the private data from Site Number to Site Index to more accurately reflect what it represents.
  3. Complete the following steps to add a VI to update the site label text for a site number.
    1. Right-click the Site Label.lvclass and select New::VI From Dynamic Dispatch Template from the context menu.
    2. Add an Operator Interface State.lvclass control and a numeric control (for Site Number )
    3. Use the Read Engine VI to get the engine reference from the Operator Interface State wire.
    4. Use an ActiveX Invoke Node to call the GetResourceString method on the engine reference. Pass in NI_SEMICONDUCTOR_OPERATOR_INTERFACE for the category and SITE_NUMBER for the symbol.
    5. Wire the Site Number input to a Number to Decimal String node.
    6. Use a Search and Replace String node by using the result from the GetResourceString method as the input string and replacing %1 with the result from the Number to Decimal String node.
    7. Use the Read Control Refnum VI to get the control refnum from the Site Label in input.
    8. Use a Property Node to set the Value property of the control refnum to the resulting string from the Search and Replace String node.
    9. Set up proper error wiring for the VI and save it as Update Site Label Text.vi .
  4. Complete the following steps to add a VI to update the site number for a site label.
    1. Right-click the Site Label.lvclass and select New::VI From Dynamic Dispatch Template from the context menu.
    2. Add an Operator Interface State.lvclass control.
    3. Use the Read Semiconductor Module Manager VI to get the manager reference from the operator interface state.
    4. Use the Get Site Numbers VI from the TSM Application API to get the current set of site numbers from the manager reference.
    5. Use the Unbundle By Name node to get the Site Index from the Site Label input.
    6. Use Index Array on the array of site numbers using the Site Index as the index.
    7. Pass the result from the Index Array to the Update Site Label Text VI you created previously.
    8. Set up proper error wiring for the VI and save it as Update Site Number.vi .
  5. Complete the following steps to add a call to the Update Site Number VI in the Refresh Callback VI for the site label.
    1. Open the Controls/Site Label.lvclass/Refresh Callback.vi .
    2. After the call to the Display Site Control VI, insert a call to the Update Site Number VI you created previously.
3. Complete the following steps to update the bin table to show the correct site numbers.
  1. Open the Controls/Bin Table.lvclass/Refresh Callback.vi .
  2. Copy the Site Lot Statistics array control from the front panel.
  3. Open the Controls/Bin Table.lvclass/Get Column Headers.vi and complete the following steps.
    1. Paste the Site Lot Statistics array control on the front panel.
    2. Wire the Site Lot Statistics array to the right-most For Loop and enable auto-indexing.
    3. Remove the wire from the Number of Sites input that connects to the Count terminal of the For Loop.
    4. Inside the For Loop, wire the Lot Statistics reference to an ActiveX Property Node to retrieve the SiteNumber property.
    5. Delete the wire from the For Loop iteration node to the Number to Decimal String node.
    6. Wire the result from the SiteNumber property to the Number to Decimal String node.
    7. Delete the Number of Sites control.
    8. Make the Site Lot Statistics array control a required input on the connector pane.
  4. In the Refresh Callback VI, which you should already have open, delete the Array Size node and wire the Site Lot Statistics array directly to the Get Column Headers call.
4. Complete the following steps to update the code to avoid an error in the case that the Semiconductor Module Manager is using 0 sites, which can happen only when you disable sites in the default Configure Lot Settings dialog box or use the AvailableSites station setting.
  1. Open the Controls/Last N Parts Label.lvclass/Refresh Callback.vi .
  2. Delete the Index Array , the numeric constant node, and any connected wire segments.
  3. Wire the All Site Lot Statistics reference to the property node for PartCountWindowSize.

Parent topic:

Displaying Specific Site Numbers in Operator Interfaces (TSM)

Related concepts:

- Configure Lot Settings Dialog Box (TSM)
- Operator Interfaces (TSM)
- TSM Application API

Related tasks:

- Customizing Operator Interfaces (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=dtrs-for-non-wafer-testing.html language=enus -->
## TOPIC 00090: Adding DTRs for Non-Wafer Testing or When the Generate One Filer per Wafer Option is Disabled

- bundle_id: `teststand-semiconductor-module`
- source_path: `dtrs-for-non-wafer-testing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/dtrs-for-non-wafer-testing.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The custom result processor that you create must appear after the STDF Log result processor in the order of result processors in the Result Processing dialog box. The following table lists the sequences to modify to create the DTR for various locations in the STDF log file. Location of DTR Test Prog

### Adding DTRs for Non-Wafer Testing or When the Generate One Filer per Wafer Option is Disabled

The custom result processor that you create must appear after the STDF Log result processor in the order of result processors in the Result Processing dialog box. The following table lists the sequences to modify to create the DTR for various locations in the STDF log file.

| Location of DTR | Test Program Sequence File Callback Sequence | Custom Result Processor Entry Point |
| --- | --- | --- |
| At beginning of log (after initial records) | ProcessSetup | Model Plugin - Begin |
| After each batch (after last PRR of current batch and before first PIR of next batch) | PostBatch | Model Plugin - Batch Done |
| With each part using Sequential process model | PostUUT | Model Plugin - UUT Done |
| At end of log (before TSRs, HBRs, SBRs, and PCR) | ProcessCleanup | Model Plugin - Pre Batch Add the following precondition to the step: !Parameters.ContinueTesting |

Parent topic:

Adding DTRs to the STDF Log File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=edit-executing-vidita.html language=enus -->
## TOPIC 00091: Editing an Executing VI in LabVIEW

- bundle_id: `teststand-semiconductor-module`
- source_path: `edit-executing-vidita.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/edit-executing-vidita.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For LabVIEW 2020 and newer, when you step into a VI from a TestStand step, LabVIEW displays the Edit VI and reset step execution button on both the front panel and block diagram toolbars. Use this button to stop executing the VI and to open it for editing. When you click Edit VI and reset step execu

### Editing an Executing VI in LabVIEW

For LabVIEW 2020 and newer, when you step into a VI from a TestStand step, LabVIEW displays the
 Edit VI and reset step execution[IMAGE alt='image' src='GUID-B99033B7-B700-45B4-85C7-0B02A72B89CD-a5.png'] button on
 both the front panel and block diagram toolbars. Use this button to
 stop executing the VI and to open it for editing. When you click
 Edit VI and reset step execution,
 TestStand resets the step execution to the step that you stepped
 into. Continuing execution of the lot in TestStand will execute the
 VI with the modifications you made.

Parent topic:

Debugging TSM Test Programs

<!--NI_TOPIC bundle=teststand-semiconductor-module path=enable-inline-qa-on-station.html language=enus -->
## TOPIC 00092: Enabling Inline QA on the Test Station (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `enable-inline-qa-on-station.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/enable-inline-qa-on-station.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the ConfigureStationSettings or GetStationSettings callback sequences to set the StationSettings.Standard.InlineQAEnabled Boolean property to True or False to enable or disable inline QA on the test station. The General tab of the default Configure Station Settings dialog box contains an Enable

### Enabling Inline QA on the Test Station (TSM)

Use the ConfigureStationSettings or GetStationSettings callback sequences
 to set the StationSettings.Standard.InlineQAEnabled Boolean
 property to True or False to
 enable or disable inline QA on the test station.

The General tab of the default Configure Station Settings dialog box contains an Enable Inline QA option that also sets the value of the StationSettings.Standard.InlineQAEnabled property.

When you enable inline QA on the test station, you must set the value of the StationSettings.Standard.InlineQAAlgorithmSequenceFilePath
 property to the absolute path of the inline QA algorithm sequence file you
 want to use on the test station. You can also use the
 Inline QA Algorithm control in the
 default Configure Station Settings dialog box
 to specify the inline QA algorithm sequence file.

Parent topic:

Performing Inline Quality Assurance Testing (TSM)

Related concepts:

- Configure Station Settings Dialog Box (TSM)
- GetStationSettings Callback (TSM)
- Accessing Station Settings from a Test Program (TSM)
- General Tab

Related tasks:

- Creating an Inline QA Algorithm Sequence File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=enable-parallel-for-loops-lv.html language=enus -->
## TOPIC 00093: Enable Parallel For Loop Iterations in VIs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `enable-parallel-for-loops-lv.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/enable-parallel-for-loops-lv.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In many cases, VIs that test multiple sites or pins contain For Loop structures that perform computationally expensive or time consuming operations for multiple instruments. Often, you can improve execution speed by enabling parallel iterations on the For Loop structure. Not all For Loops can run wi

### Enable Parallel For Loop Iterations in VIs (TSM)

In many cases, VIs that test multiple sites or pins contain For Loop structures that perform
 computationally expensive or time consuming operations for multiple
 instruments. Often, you can improve execution speed by enabling
 parallel iterations on the For Loop structure. Not all For Loops can
 run with parallel iterations, and in some cases, a For Loop does not
 benefit from parallelization. Additionally, you can adjust thread settings for parallel For
 Loops to improve performance.

Refer to the *Parallel Iterations: Improving For Loop Execution Speed* topic in the
 *LabVIEW Help* to determine whether you can
 improve performance by enabling parallel For Loop iterations in VI
 test code modules. In LabVIEW, select Help»LabVIEW Help to launch the *LabVIEW Help*.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

Related concepts:

- Thread Settings for Maximum Parallelism (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=enabling-offline-mode.html language=enus -->
## TOPIC 00094: Enabling Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `enabling-offline-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/enabling-offline-mode.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to enable Offline Mode on a computer without access to NI instruments. Offline Mode remains enabled, including after you exit and relaunch TSM, until you disable it. You cannot enable Offline Mode on an STS or from a TSM Operator Interface. Install STS Software 19.0 or l

### Enabling Offline Mode (TSM)

Complete the following steps to enable Offline Mode on a computer without access to NI
 instruments. Offline Mode remains enabled, including after you exit
 and relaunch TSM, until you disable it.

Note

1. Install STS Software 19.0 or later or ensure you meet the requirements on the computer on
 which you want to use Offline Mode.
2. Obtain an Offline
 Mode system configuration file and associate it with the test
 program you want to execute in Offline Mode.
 If you do not associate an Offline Mode system configuration
 file with the test program, TSM prompts you for an Offline
 Mode system configuration file when you enable Offline Mode,
 but the TSM Operator Interface does not.
3. Select Semiconductor Module»Enable Offline Mode or click the Enable Offline
 Mode 
 button on the TSM toolbar to enable Offline Mode. The
 Enable Offline Mode button
 icon changes to indicate the current state of Offline Mode
 and the main menu bar displays an Offline
 Mode indicator to the right of the
 Help menu. Additionally, the
 OfflineMode 
 property of the NI_SemiconductorModule_StandardStationSettings 
 data type indicates the current state of Offline Mode. You
 can also use the Get Offline Mode VI or the
 IsSemiconductorModuleInOfflineMode 
 .NET method to check the current status of the Offline Mode
 setting.

When you enable Offline Mode, TSM creates simulated versions of all instruments defined in the
 Offline Mode system configuration file. The simulated instruments
 persist until you disable Offline Mode or execute a test program
 with a different Offline Mode system configuration file. TSM also
 renames all physical instruments that conflict with the instruments
 defined in the Offline Mode system configuration file with an
 NI_Offline_ prefix to avoid conflicts with
 simulated instruments and to prevent accidental damage to real
 instruments. Disabling Offline Mode restores the
 instrument configuration.

Note

Enabling Offline Mode might fail when the computer on which you want to use Offline Mode does not
 include a required instrument driver, an
 instrument driver does not support simulation for an instrument, or
 an error exists in the Offline Mode system configuration file. Use
 the following techniques to resolve the issue:

- Install any missing drivers.
- Modify the test program to remove dependencies on unsupported instruments.
- Fix any errors in the Offline Mode system configuration file.

Parent topic:

Offline Mode Workflow (TSM)

Related concepts:

- Disabling Offline Mode (TSM)
- Offline Mode Requirements (TSM)
- Accessing Station Settings from a Test Program (TSM)

Related tasks:

- Obtaining an Offline Mode System Configuration File (TSM)
- Offline Mode Workflow (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=end-of-test-dialog.html language=enus -->
## TOPIC 00095: End of Test Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `end-of-test-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/end-of-test-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Built-in Simulated Handler Driver launches the End of Test dialog box to display hardware and software bin information during the EndOfTest entry point when you enable the Show Handler Dialogs option on the Configure Built-in Simulated Handler Driver dialog box and you use the Batch or Sequen

### End of Test Dialog Box (TSM)

The NI Built-in Simulated Handler Driver launches the End of Test dialog box to display hardware
 and software bin information during the EndOfTest entry point when you enable
 the Show Handler Dialogs option on the Configure Built-in Simulated Handler
 Driver dialog box and you use the Batch or Sequential process model.

The End of Test dialog box contains the following elements:

- Site Bins —Displays the hardware and software bins that correspond to the DUT tested at each site on a per-test basis.
- Bin Totals —Displays the total number of DUTs per hardware and software bin on a per-lot basis.
- Show/Hide Details —Shows or hides the Bin Totals table.
- Do not show this dialog again for this lot —Enable this option to hide the dialog box for the remainder of lot testing.

Parent topic:

Dialog Boxes and Windows

Related concepts:

- EndOfTest Handler/Prober Driver Entry Point (TSM)
- NI Built-in Simulated Handler Driver (TSM)

Related information:

- Batch Process Model
- Sequential Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=endoftest-hand-prob-entry-point.html language=enus -->
## TOPIC 00096: EndOfTest Handler/Prober Driver Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `endoftest-hand-prob-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/endoftest-hand-prob-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the EndOfTest entry point to send the end-of-test notification to move DUTs from test sites to hardware bins. TSM sends the hardware bin results of the current DUTs to the EndOfTest entry point. The EndOfTest entry point accepts the following parameters: Parameter Type Description HandlerDriverD

### EndOfTest Handler/Prober Driver Entry Point (TSM)

Use the EndOfTest entry point to send the end-of-test notification to move DUTs from test sites to hardware bins.

TSM sends the hardware bin results of the current DUTs to the EndOfTest entry point.

The EndOfTest entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| HandlerDriverData | Input or Output | Container that stores handler-specific settings, prober-specific settings, or run-time data. In a handler/prober driver sequence file, you can modify the default structure of this parameter, such as by changing the data type from the default Container to a custom container data type. However, the Configure entry point must create, and optionally assign, each field of this parameter using the TestStand API, such as the PropertyObject.NewSubProperty method or a PropertyObject Set value method, such as SetValNumber.Do not enable the Check Type option for this parameter. Right-click the parameter and remove the checkmark from Check Type in the context menu to disable the Check Type option. |
| HardwareBinData | Input | Array of hardware bin numbers that specify the hardware bins assigned to each part on each site. The index to the array corresponds to the site number of the test site. A hardware bin value of -1 indicates that TSM did not assign a hardware bin for the site for one of the following reasons: When you execute tests using the Batch process model, you disabled the site.When you execute tests using the Parallel process model and the site is not the currently executing site. |
| SoftwareBinData | Input | An array of software bins assigned to each part on each site. The index to the array corresponds to the site number of the test site. A software bin value of -1 indicates that TSM did not assign a software bin for the site for one of the following reasons: When you execute tests using the Batch process model, you disabled the site.When you execute tests using the Parallel process model and the site is not the currently executing site. |
| EndOfWafer | Output | Boolean value that indicates whether the tester just finished testing the last batch of parts on a wafer. Set this property to True when the prober indicates that there are no more die to test on the wafer. TSM uses this property to determine when to generate Wafer Results Records (WRR) of the STDF log file and to determine when to finish writing STDF logs and Lot Summary Reports when you enable the Generate One File per Wafer option for those report generators.This output parameter is optional when you execute with the Batch process model. If the prober driver does not set this parameter when executing with the Batch process model, TSM infers the end of the wafer when the prober sets the WaferRuntimeData.StartOfWafer parameter to true in the StartOfTest handler/prober driver entry point. When using the Batch process model, omitting the wait for an end-of-wafer status message to set the EndOfWafer parameter in the EndOfTest entry point might improve performance of the test system. |
| BinTypes | Input | Array of numbers that specifies the types of the bins assigned to each part on each site. Each element in the array has one of the following values to indicate the type of bin of the corresponding element in the SoftwareBinData and HardwareBinData parameter arrays: 0—The bin is a Pass bin.1—The bin is a Fail bin.2—The bin is an Other bin.-1—TSM did not assign a bin for the part tested on that site. |
| SemiconductorModuleManager | Input or Output | Object reference to an instance of a Semiconductor Module Manager. Use this object reference with the TSM Application API to get information about test execution, obtain test statistics, monitor the state of the test system, and so on.Note If one or more test sockets in a batch execution prematurely stop running, such as when you abort a test socket, TSM stops all tests without calling the EndOfTest entry point for the current DUTs. |

Parent topic:

Handler/Prober Driver Entry Points (TSM)

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- Using the Semiconductor Module Manager Object
- TSM Application API

Related information:

- Batch Process Model
- Parallel Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=environment-reference.html language=enus -->
## TOPIC 00097: Environment Reference

- bundle_id: `teststand-semiconductor-module`
- source_path: `environment-reference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/environment-reference.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TSM environment consists of dialog boxes and windows that allow you to build and modify various components of a project. Refer to the following for information about the various components of the TSM environment. TSM Sequence Editor UI Configuration Test Program Editor (TSM) Bin Definitions Edit

### Environment Reference

The TSM environment consists of dialog boxes and windows that allow you to build and
 modify various components of a project.

- TSM Sequence Editor UI Configuration
- Test Program Editor (TSM)
- Bin Definitions Editor (TSM)
- Pin Map Editor (TSM)
- TSM Step TypesDialog Boxes and Windows

Related concepts:

- TSM Sequence Editor UI Configuration
- Test Program Editor (TSM)
- Bin Definitions Editor (TSM)
- Pin Map Editor (TSM)
- TSM Step Types
- Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=error-handling-prallel-for-loops.html language=enus -->
## TOPIC 00098: Error Handling with Parallel For Loops in LabVIEW

- bundle_id: `teststand-semiconductor-module`
- source_path: `error-handling-prallel-for-loops.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/error-handling-prallel-for-loops.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: If you enable parallelism in a For Loop, any shift registers on error wires automatically become error registers, which allow for errors to be merged across all iterations of the For Loop, as illustrated in the previous graphic. Because you cannot use shift registers in parallel For Loops, you must

### Error Handling with Parallel For Loops
 in LabVIEW

If you enable parallelism in a For Loop, any shift registers on error wires automatically
 become error registers, which allow for errors to be merged across all iterations of the For
 Loop, as illustrated in the previous graphic.

Because you cannot use shift registers in parallel For Loops, you must build error clusters into an array and then merge the errors. Complete the following steps to structure error wires so that you can handle all potential errors.

1. If no iterations of the parallel For Loop execute, which can occur when a previous error exists, the loop does not record any errors you pass into the loop. To avoid this situation, branch the error wire before it enters the parallel For Loop and connect the new segment around the loop to the top input terminal of the Merge Errors node. Using this wire connection strategy ensures that you can track errors that occurred earlier during execution outside of the loop.
2. Enable indexing for the error output tunnel exiting the loop. If you do not enable indexing, only the error information from the final iteration of the loop is maintained.
3. Use the Merge Errors node to capture error information from the code that executed before the loop execution and also each of the loop iterations.

Parent topic:

Parallel For Loops (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=example-programs.html language=enus -->
## TOPIC 00099: TSM Example Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `example-programs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/example-programs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TSM example programs, located in the <TestStand Public>\Examples\NI_SemiconductorModule directory, to learn more about how to solve specific issues in a semiconductor test program.

### TSM Example Programs

Use the TSM example programs, located in the <TestStand
 Public>\Examples\NI_SemiconductorModule
 directory, to learn more about how to solve specific issues in a
 semiconductor test program.

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=execute-code-modules-lv.html language=enus -->
## TOPIC 00100: Execute Test Code Modules Using the LabVIEW Run-Time Engine (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `execute-code-modules-lv.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/execute-code-modules-lv.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The TestStand LabVIEW Adapter can execute VI code modules in the LabVIEW Development System process or in the TestStand process using the LabVIEW Run-Time Engine (RTE). Executing test code in the LabVIEW Development System process is useful for debugging but adds significant performance overhead to

### Execute Test Code Modules Using the LabVIEW Run-Time Engine (TSM)

The TestStand LabVIEW Adapter can execute VI code modules in the LabVIEW Development System process or in the TestStand process using the LabVIEW Run-Time Engine (RTE). Executing test code in the LabVIEW Development System process is useful for debugging but adds significant performance overhead to the execution of test programs. To reduce this overhead, execute VIs in the TestStand process using the LabVIEW RTE.

Complete the following steps to configure the LabVIEW Adapter to use the LabVIEW RTE from the TestStand Sequence Editor.

1. Select Configure»Adapters .
2. Select the LabVIEW Adapter in the list control and click Configure to launch the LabVIEW Adapter Configuration dialog box.
3. Enable the LabVIEW Run-Time Engine option.

Complete the following steps to configure the LabVIEW Adapter to use the LabVIEW RTE from the
 TestStand Semiconductor Module operator interface.

1. Click the Configure Station button to launch the Configure Station Settings dialog box.
2. On the Advanced tab, click the LabVIEW Adapter button to launch the LabVIEW Adapter Configuration dialog box.
3. Enable the LabVIEW Run-Time Engine option.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

Related concepts:

- Configure Station Settings Dialog Box (TSM)
- Advanced Tab

<!--NI_TOPIC bundle=teststand-semiconductor-module path=execute-in-offline-mode.html language=enus -->
## TOPIC 00101: Executing Test Programs in Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `execute-in-offline-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/execute-in-offline-mode.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Although simulated instruments behave as closely as possible to real instruments, measurements and data differ in Offline Mode. Additionally, custom code that processes results, test time performance, instrument functionality, and error reporting might differ in Offline Mode and can result in differ

### Executing Test Programs in Offline Mode (TSM)

Note

Complete the following steps to execute a test program in Offline Mode on a computer without access to NI instruments.

1. Confirm that Offline Mode is enabled.
2. Click the Start Lot 
 button or the Single Test 
 button on the TSM toolbar. Note TSM
 and the TSM Operator Interface update the simulated
 instruments to match the Offline Mode system
 configuration file associated with the test program
 before the test program begins execution. TSM does
 not automatically update the simulated instruments
 when you run test programs any other way.
3. Review the
 results.

Parent topic:

Offline Mode Workflow (TSM)

Related tasks:

- Enabling Offline Mode (TSM)
- Measuring and Publishing Values in Offline Mode (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=execution-data-properties.html language=enus -->
## TOPIC 00102: Execution Data Properties

- bundle_id: `teststand-semiconductor-module`
- source_path: `execution-data-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/execution-data-properties.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the execution data properties you can access from this step. NameTypeDescriptionAccess RestrictionsBinTypeNumber or NI_SemiconductorModule_BinTypeType of the bin assigned to the part tested on the current site. (0=Pass, 1=Fail, 2=Other)Test Socket Threads OnlyValid in PostU

### Execution Data Properties

| Name | Type | Description | Access Restrictions |
| --- | --- | --- | --- |
| BinType | Number or NI_SemiconductorModule_BinType | Type of the bin assigned to the part tested on the current site. (0=Pass, 1=Fail, 2=Other) | Test Socket Threads OnlyValid in PostUUT |
| BinTypes | Array of numbers or array of NI_SemiconductorModule_BinType | The types of the bins assigned to each part on each site. (0=Pass, 1=Fail, 2=Other) | Valid in PostBatch |
| CSVTestResultsLogFilePath | String | Returns the absolute file path of the last CSV Test Results Log generated for the current lot. | Valid in MainSequence |
| CSVTestResultsLogFilePaths | Array of strings | Returns the absolute file paths of all CSV Test Results Logs generated for the current lot. If the Generate One File per Wafer option is enabled, one path is returned for each wafer processed in the lot so far. Otherwise, the length of the array is 1. | Valid in MainSequence |
| DebugTestResultsLogFilePath | String | Returns the absolute file path of the Debug Test Results Log generated for the current site. | Valid in MainSequence |
| DebugTestResultsLogFilePaths | Array of strings | Returns the absolute file paths of the Debug Test Results Logs generated for all sites in the current lot. | Controller Thread Only |
| DidInlineQABlockExecute | Boolean | Returns true if an InlineQA step executed its block of steps for this site. | Test Socket Threads OnlyValid in MainSequence |
| DieCoordinateX | Number | Returns the X wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. This property corresponds to the X_COORD field in the Part Results Record (PRR) in the STDF log file. | Test Socket Threads OnlyValid in MainSequence |
| DieCoordinateY | Number | Returns the Y wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. This property corresponds to the Y_COORD field in the Part Results Record (PRR) in the STDF log file. | Test Socket Threads OnlyValid in MainSequence |
| HardwareBinName | String | Returns the name of the hardware bin that the tester assigned to the last part that was tested on this site. | Test Socket Threads OnlyValid in PostUUT |
| HardwareBinNames | Array of strings | The names of the hardware bins that the tester assigned to the parts in the current batch. | Valid in PostBatch |
| HardwareBinNumber | Number | The number of the hardware bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. | Test Socket Threads OnlyValid in PostUUT |
| HardwareBinNumbers | Array of numbers | The numbers of the hardware bins that the tester assigned to the parts in the current batch. | Valid in PostBatch |
| IsDuplicateDieCoordinates | Boolean | Returns true if a part with the same die coordinates as the current part was tested previously in the current wafer. | Test Socket Threads OnlyValid in MainSequence |
| IsDuplicatePartId | Boolean | Returns true if a part with the same part ID as the current part was tested previously in the current lot. | Test Socket Threads OnlyValid in MainSequence |
| IsRetesting | Boolean | Returns true if the tester is currently retesting the same parts from the previous batch because the operator requested a retest. | Valid in PreBatch |
| IsStartOfWafer | Boolean | Returns true if the current batch is the first batch of parts of a new wafer. This property remains true if the first batch of parts are retested. | Valid in PreBatch |
| LotSummaryReportFilePath | String | Returns the absolute file path of the last Lot Summary Report generated for the current lot. | Valid in MainSequence |
| LotSummaryReportFilePaths | Array of strings | Returns the absolute file paths of all Lot Summary Reports generated for the current lot. If the Generate One File per Wafer option is enabled, one path is returned for each wafer processed in the lot so far. Otherwise, the length of the array is one. | Valid in MainSequence |
| NumberOfSites | Number | The number of sites that are testing the current lot. | — |
| PartId | String | Returns the part identifier for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartIds parameter in the StartOfTest handler driver entry point sequence. If the handler/prober driver does not set this property, the tester sets the value to a unique value if the GenerateUniquePartIds station settings is set to true. This property corresponds to the PART_ID field in the Part Results Record (PRR) in the STDF log file.When the GenerateUniquePartIds property is True, TSM reassigns the same unique Part ID to the part when it is retested. Customize the behavior of GenerateUniquePartIds to assign a new unique Part ID to a part when it is retested . | Test Socket Threads OnlyValid in MainSequence |
| PartText | String | Returns the part description text for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartTexts parameter in the StartOfTest handler driver entry point sequence. This property corresponds to the PART_TXT field in the Part Results Record (PRR) in the STDF log file. | Test Socket Threads OnlyValid in MainSequence |
| SiteNumber | Number | Site number of the current site. | Test Socket Threads Only |
| SiteNumbers | Array of numbers | The site numbers that are testing the current lot. |  |
| SiteTestTimeInSeconds | Number | Returns the time to execute the MainSequence sequence for the last part that was tested on this site. | Test Socket Threads OnlyValid in PostUUT |
| SoftwareBinName | String | The name of the software bin that the tester assigned to the last part that was tested on this site. | Test Socket Threads OnlyValid in PostUUT |
| SoftwareBinNames | Array of strings | The names of the software bins that the tester assigned to the parts in the current batch. | Valid in PostBatch |
| SoftwareBinNumber | Number | The number of the software bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. | Test Socket Threads OnlyValid in PostUUT |
| SoftwareBinNumbers | Array of numbers | The numbers of the software bins that the tester assigned to the parts in the current batch. | Valid in PostBatch |
| StdfLogFilePath | String | Returns the absolute file path of the last STDF log file generated for the current lot. | Valid in MainSequence |
| StdfLogFilePaths | Array of strings | Returns the absolute file paths of all STDF log files generated for the current lot. If the Generate One File per Wafer option is enabled, one path is returned for each wafer processed in the lot so far. Otherwise, the length of the array is one. | Valid in MainSequence |
| WaferRuntimeData.ExecDescription | String | Returns the wafer description supplied by exec. This property corresponds to the EXC_DESC field in the Wafer Results Record (WRR) in the STDF log file. | Valid in PreBatch |
| WaferRuntimeData.FabWaferId | String | Returns the fab wafer ID. This property corresponds to the FABWF_ID field in the Wafer Results Record (WRR) in the STDF log file. | Valid in PreBatch |
| WaferRuntimeData.FrameId | String | Returns the wafer frame ID. This property corresponds to the FRAME_ID field in the Wafer Results Record (WRR) in the STDF log file. | Valid in PreBatch |
| WaferRuntimeData.MaskId | String | Returns the wafer mask ID. This property corresponds to the MASK_ID field in the Wafer Results Record (WRR) in the STDF log file. | Valid in PreBatch |
| WaferRuntimeData.UserDescription | String | Returns the wafer description supplied by user. This property corresponds to the USR_DESC field in the Wafer Results Record (WRR) in the STDF log file. | Valid in PreBatch |
| WaferRuntimeData.WaferId | String |  | Valid in PreBatch |

#### Access Restrictions

- Some properties are valid only when accessed from certain process model threads. If you
 access these properties from an unsupported model thread, the step reports a
 run-time error. 
 Some properties are valid only at certain times during execution. If you
 access these properties before they are valid, the step either returns
 default values or reports a run-time error as described below.
  - Test Socket Threads Only —You must access these
 site-specific properties from a test socket thread. The step reports a
 run-time error if you access the property in a sequence that executes in
 a controller thread, such as ProcessSetup when
 executing the Batch process model. You can access these properties from
 any sequence when using the Sequential process model.
  - Controller Thread Only —You must access these
 properties from a process model callback sequence that executes in a
 controller thread, such as ProcessCleanup . The step
 reports a run-time error if you access the property in a sequence that
 executes in a test socket thread, such as MainSequence 
 or PreUUT .
  - Valid in PreBatch —TSM assigns values to these
 properties before testing starts for the current batch. These properties
 have meaningful values only in the following locations. The step returns
 default values if you access the property from other locations. The step
 returns default values if you access the property from other locations.
    - In the Model Plugin – Pre
 Batch entry point and beyond in model plug-ins when
 using the Batch process model.
    - In the Model Plugin – Pre
 UUT entry point and beyond in model plug-ins when
 using the Sequential process model.
    - In the PreUUT Model
 callback and beyond in test programs.
  - Valid in MainSequence —TSM assigns values to these
 site-specific properties before testing starts for the current part.
 These properties have meaningful values only in the following locations.
 The step returns default values if you access the property from other
 locations.
    - In the Model Plugin – Pre
 UUT entry point and beyond in model plug-ins.
    - In the MainSequence sequence and beyond in test
 programs.
  - Valid in Post UUT —TSM assigns values to
 site-specific properties after testing completes for the current part.
 These properties have meaningful values only in the following locations.
 The step reports a run-time error if you access these properties from
 other locations.
    - In the Model Plugin – UUT
 Done entry point and beyond in model plug-ins.
    - In the PostUUT Model
 callback and beyond in test programs.
  - Valid in Post Batch —TSM assigns values to these
 properties after testing completes for all sites. These properties have
 meaningful values only in the following locations. The step reports a
 run-time error if you access these properties from other locations.
    - In the Model Plugin – Batch
 Done entry point and beyond in model plug-ins when
 using the Batch process model.
    - In the Model Plugin – UUT
 Done entry point and beyond in model plug-ins when
 using the Sequential process model.
    - In the PostBatch callback
 and beyond in test programs when using the Batch process model.
    - In the PostUUT callback
 and beyond in test programs when using the Sequential process
 model.

Parent topic:

Get Test Information Tab (TSM)

Related concepts:

- Accessing Station Settings from a Test Program (TSM)

Related information:

- Process Model Thread Types
- Model Plugin – Pre Batch
- Model Plugin – Pre UUT
- Model Callbacks in the Batch Process Model
- Model Plugin – UUT Done
- Model Plugin – Batch Done
- Model Callbacks in the Sequential Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=execution-timing-overview.html language=enus -->
## TOPIC 00103: Execution Timing Overview (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `execution-timing-overview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/execution-timing-overview.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram illustrates how TSM coordinates test program execution and handler/prober actions. Executing a test program in a TSM operator interface is typically faster than executing the test program in the TestStand Sequence Editor development environment. Batch ModelWhen you execute test

### Execution Timing Overview (TSM)

The following diagram illustrates how TSM coordinates test program execution and handler/prober actions.

Note

[IMAGE alt='image' src='GUID-3421253E-4FA2-4D2E-9D9D-3FAC0FC573E3-a5.png']

#### Batch Model

When you
 execute tests using the Batch process model, a controller thread controls the core
 tester software functionality and sends notifications to and receives notifications
 from a separate thread for each site execution.

[IMAGE alt='image' src='GUID-BD6A5F33-CECD-4144-9885-0B7247676360-a5.png']

#### Sequential Process Model

[IMAGE alt='image' src='GUID-141518AC-9566-44E7-A4FF-E743E75EDB87-a5.png']

Related information:

- Batch Process Model
- Process Model Thread Types

<!--NI_TOPIC bundle=teststand-semiconductor-module path=export-correlation-offsets-template-file.html language=enus -->
## TOPIC 00104: Exporting a Correlation Offsets Template File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `export-correlation-offsets-template-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/export-correlation-offsets-template-file.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can apply correlation offset values to test results on a per-site basis at run time before evaluating the test result data against limits. Use the Load Correlation Offsets Step and associated edit tab to load and apply a correlation offset file. Select Semiconductor ModuleExport Correlation Offs

### Exporting a Correlation Offsets Template File (TSM)

You can apply correlation offset values to test results on a per-site basis at run time before
 evaluating the test result data against limits. Use the Load Correlation Offsets Step and
 associated edit tab to load and apply a
 correlation offset file.

Select Semiconductor Module»Export Correlation Offset Template file based on
 <filename> to generate a tab-delimited correlation offsets
 template file (.txt) based on the numerical
 limit tests in the selected sequence file. If you make changes,
 export the file again, and select an existing file, the content of
 the existing file is overwritten, including any custom correlation
 offset values you set.

The correlation offsets template file contains entries (0.0) for all
 numerical limits tests for all defined sites in the sequence file.
 You can use the template file as a starting point for a custom
 correlation offsets file.

The file does not contain correlation offsets entries for external sequence files referenced in the sequence file from which you export the correlation offsets template file.

The correlation offsets template file contains the following test data for every sequence in the sequence file:

| Data Item | Description |
| --- | --- |
| SequenceName | Always included in the file. |
| StepName | Always included in the file. |
| StepId | Always included in the file. |
| TestNumber | Always included in the file. If a step does not contain any tests, this field displays "No Tests". |
| Site_0_Offset to Site_n_Offset | n is the number of sites defined for the station. If no sites are defined, only Site_0_Offset will exist. The default value is 0.0. You do not have to assign a custom correlation offset value to every test in the file. |

Parent topic:

Exporting and Importing Test Limits with Text Files

Related concepts:

- Load Correlation Offsets Step (TSM)
- Load Correlation Offsets Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=export-import-test-limits-tle.html language=enus -->
## TOPIC 00105: Exporting and Importing Test Limits with Text Files

- bundle_id: `teststand-semiconductor-module`
- source_path: `export-import-test-limits-tle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/export-import-test-limits-tle.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use a tab-delimited text file to export and import test limits from and to Semiconductor Multi Test steps and Semiconductor Sequence Call steps in a single sequence file at edit time or run time. During development, export all the tests in a test program to review and edit and then import the change

### Exporting and Importing Test Limits with Text
 Files

Use a tab-delimited text
 file to export and import
 test limits from and to Semiconductor Multi Test steps and Semiconductor Sequence
 Call steps in a single sequence file at edit time or run time. During
 development, export all the tests in a test program to review and edit and
 then import the changes back into the test program. At run time, load and execute a
 different set of test limits from separate text files based on the test program
 configuration you select by exporting the test limits and creating
 multiple copies of the file to edit for each unique set of test limits you want to
 use. To protect the test limits files from viewing or editing when deploying a test
 program, embed
 the test limits in the test program sequence file and use the TestStand
 password protection option to lock the sequence
 file.

Select Semiconductor Module»Edit Test Program and select Test Limits Files in the Test Program
 Editor to specify one or more test limits files to make available to the
 test program configurations. The test program
 configuration specifies the test limits file that loads before running a
 test lot.

Create a test limits file by selecting Semiconductor Module»Export Test Limits from or by clicking the Export Test Limits from button [IMAGE alt='image' src='GUID-A2CE1F57-BAB2-455A-AB84-5C91525B77A9-a5.png'] on the TSM toolbar to export test limits from a sequence
 file into a tab-delimited test limits text file. Import a test limits file by
 selecting Semiconductor Module»Import Test Limits to or by clicking the Import Test Limits to
 button [IMAGE alt='image' src='GUID-E83195DD-33A6-4A53-8413-0AF0D7EC9340-a5.png'] on the TSM toolbar to import test
 limits from a tab-delimited test limits text file into a sequence file. When you
 assign a base limits file for a test program, importing a test limits file will
 automatically merge the values of the file with the values of the base file,
 overriding or inheriting values accordingly. TSM imports the merged value. When you
 import test limits from a text file, you can update limits in matching tests or
 replace all tests in matching steps.

- [Exporting Test Limits from Sequence Files](export-test-limits-from-sequence-tle.html)
- [Opening Test Limits Text Files in Microsoft Excel (TSM)](open-test-limits-in-excel.html)
- [Importing Test Limits from Text Files (TSM)](import-test-limits.html)
- [Exporting a Correlation Offsets Template File (TSM)](export-correlation-offsets-template-file.html)

Related concepts:

- Exporting Test Limits from Sequence Files
- Importing Test Limits from Text Files (TSM)
- Semiconductor Multi Test Step
- Semiconductor Sequence Call Step
- Test Program Editor (TSM)
- Test Limits Files Panel
- Test Settings Relationships (TSM)

Related information:

- Editing Test Limits Files in Test Limits Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=export-test-limits-from-sequence-tle.html language=enus -->
## TOPIC 00106: Exporting Test Limits from Sequence Files

- bundle_id: `teststand-semiconductor-module`
- source_path: `export-test-limits-from-sequence-tle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/export-test-limits-from-sequence-tle.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor ModuleExport Test Limits from <filename> to export test limits from all test steps in a sequence file to a new or existing tab-delimited test limits text file at edit time. Selecting an existing file overwrites the content of the file. When you export test limits, the text file

### Exporting Test Limits from Sequence
 Files

Select Semiconductor Module»Export Test Limits from <filename> to export test limits from all test steps
 in a sequence file to a new or existing tab-delimited test limits text file
 at edit time. Selecting an existing file overwrites the content of the file.

When you export test limits, the text file includes the following test data for every sequence in
 the sequence file:

- Sequence name, Step name,
 UniqueStepId,
 Test name— Always included.
- Test number— If a step does not contain any tests, this field displays No Tests. Note Use the
 Semiconductor Action step instead of the Semiconductor Multi Test step if
 the step does not contain any tests.
- Pin or pin group—TSM does not export the test data associated with the generated tests for the
 pins in the pin group.
- Low limit expression, High limit expression—For Pass/Fail tests, these fields are blank.
- Scaling factor—Included only when non-empty scaling factors exist for any test in the sequence
 file and scaling factors are the same within each test. The Units Prefix column
 of the Supported Scaling factors table lists values for exported scaling
 factors.
- Low limit scaling factor, High limit scaling factor, Data limit scaling factor—Included only
 when non-empty for any test in the sequence file and the data and limits scaling
 factors differ in at least one test in the sequence file. The Units Prefix
 column of the Supported Scaling Factors table lists values for
 exported scaling factors.
- Evaluation comparison mode—Included only when at least one step contains non-default value. For
 Pass/Fail tests, this field is blank.
- Base units—For Pass/Fail tests, this field is blank.
- Evaluation type, Software bin— Always included.
- Test name expression, Test number expression, Software bin expression, Published data ID, Test
 data source expression, Export data to expression—Included only when non-empty
 values exist for any tests in the sequence file.
- Test numeric display format—Included only when non-default test numeric display formats exist
 for any tests in the sequence file.
- PAT base test number—Included only when non-empty PAT base test numbers exist for any tests in
 the sequence file. A blank value is exported for a test when the Enable Dynamic
 PAT and Enable Static PAT columns on the Semiconductor
 Multi Test Part Average Testing (PAT) tab do not include a checkmark
 for the test.
- Enable dynamic PAT—Included only when the Enable Dynamic PAT column on the Semiconductor Multi
 Test Part Average Testing tab includes a checkmark in the sequence file.
- Dynamic PAT test number, Dynamic PAT test name, Dynamic PAT software bin, Dynamic PAT low limit,
 Dynamic PAT high limit—Included only when non-empty values exist for any tests
 in the sequence file. A blank value is exported for a test when the Enable
 Dynamic PAT column on the Semiconductor Multi Test Part Average Testing tab does
 not include a checkmark for the test.
- Enable static PAT—Included only when the Enable Static PAT column on the Semiconductor Multi
 Test Part Average Testing tab includes a checkmark in the sequence file.
- Static PAT test number, Static PAT test name, Static PAT software bin—Included only when
 non-empty values exist for any tests in the sequence file. A blank value is
 exported for a test when the Enable Static PAT column on the Semiconductor Multi
 Test Part Average Testing tab does not include a checkmark for the test.

The file does not contain test data for external sequence files referenced in the sequence file from
 which you export the test limits.

Note

- For
 Semiconductor Multi Test
 steps in the sequence that have no tests, the file contains a row with the
 step information and the value No Tests for the Test Name.
 All other columns are blank. Use the
 Semiconductor Action
 step instead of the Semiconductor Multi Test step if the step does not
 contain any tests.
- For
 Semiconductor Sequence Call
 steps in the sequence that have no tests, the file contains a row with the
 step information and the value No Tests for the Test Name.
 All other columns are blank. Use the
 TestStand Sequence Call
 step instead of the Semiconductor Sequence Call step if the step does not
 contain any tests.
- If a field name begins with a mathematical sign, Microsoft Excel might
 interpret the contents of the cell as a formula and return an error for the
 cell. To work around this issue, format the cell in Excel as text data.
- In some cases when a limit has a large number of digits, Microsoft Excel
 might truncate the decimal portion of the number. To work around this issue,
 format the columns that contain the limit numbers in Excel as text
 data.
- Exporting PAT limits does not honor settings you specify in the
 StepSettingsPaneUI property of the
 FileGlobals.PartAverageTestingAlgorithmDescription.EnvironmentSettings 
 container of the PartAverageTestingCallbacks.seq 
 file.

Parent topic:

Exporting and Importing Test Limits with Text Files

Related concepts:

- Test Steps and Flow (TSM)
- Scaling Measurement and Limit Data (TSM)
- Semiconductor Multi Test Part Average Testing Tab
- Semiconductor Multi Test Step
- Semiconductor Action Step
- Semiconductor Sequence Call Step

Related information:

- Test Limits Editor User Manual
- Test Limits Text File Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=extended-support-changes.html language=enus -->
## TOPIC 00107: Updates and Changes for TestStand Semiconductor Module Extended Support Versions

- bundle_id: `teststand-semiconductor-module`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/extended-support-changes.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in TestStand Semiconductor Module versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information abo

### Updates and Changes for TestStand Semiconductor Module Extended Support Versions

Browse updates and changes made in TestStand Semiconductor Module versions
 on extended support.

Note

Release Notes

Related information:

- TSM Release Notes

#### TSM 2024 Q3.1 Changes

Learn about new features, behavior changes, and other updates in TSM 2024
 Q3.1.

- Perform tasks before lot testing begins with the PreLotTesting 
 callback sequence. Pre-lot testing tasks include calibration or DIB initialization.
- View, compare, and modify test limits files in TSM Test Limits
 Editor .
- Save and load files that contain configuration presets for production or development.
 Configuration presets allow you to use the same configuration across multiple stations.
 You can save and load files with presets for TestStand and TSM. To load or save a
 presets file, navigate to Semiconductor Module»Configuration Preset .
- For a given sequence file, TSM notifies you when an instrument in the pin map is
 missing from the Offline Mode system configuration file.

Related concepts:

- Performing Tasks before Lot Testing Begins

Related tasks:

- Obtaining an Offline Mode System Configuration File (TSM)

Related information:

- Editing Test Limits Files in Test Limits Editor (TSM)

#### TSM 2024 Q3 Changes

Learn about new features, behavior changes, and other updates in TSM 2024
 Q3.

- Automatically generate test numbers for Semiconductor Multi Test steps.
- Raise an alarm when a lead in remote sense measurements disconnects.
- Raise an alarm when a current or voltage measurement circuit is saturated.
- Differentiate when a compliance alarm is for an instrument entering a current or
 voltage compliance state.
- Control relays with digital output lines of DAQmx devices.
- Batch configure the data evaluated in Offline Mode for all tests in a Semiconductor Multi
 Test step.
- Pause and debug a .NET code module at publish time without freezing the TSM Runtime
 Data Viewer.
- View the tester channel information of your STS in the Pin Map Editor .
- Use new API methods to query alarm status, change its behavior, and report alarm information
 when an alarm latches.

Related concepts:

- Semiconductor Multi Test Options Tab
- Open Lead Alarm
- Compliance Alarm
- Measurement Saturation Alarm

Related tasks:

- Viewing TSM Data at Publish Time
- Using Alarms to Report Error Conditions at Runtime
- Measuring and Publishing Values in Offline Mode (TSM)
- Viewing and Editing Connections in the Connections Table (TSM)

#### TSM 2024 Q1 Changes

Learn about new features, behavior changes, and other updates in TSM 2024
 Q1.

- Run TSM with TestStand 2023 .
- Use LabVIEW 2023 Q3 to run TSM examples and tutorials and develop TSM code
 modules.
- Use a new API method to enable and disable alarms.
- View triggered alarms and publish time data in the Runtime Data
 Viewer .

Related concepts:

- Alarms Panel

Related tasks:

- Viewing TSM Data at Publish Time

#### TSM 2023 Q1 Changes

Learn about new features, behavior changes, and other updates in TSM 2023
 Q1.

- Use the TSM Runtime Data Viewer to see test results and debug issues at
 runtime.
- See which alarms were raised during the execution of a test program in the Lot
 Summary Report .
- When used with STS Software 23.0 and later, TSM uses the STS blind-mate
 port names for RF instruments instead of the instrument driver port names. TSM
 displays the blind-mate port names in the Pin Map Editor and returns the blind-mate
 port names as the channel names for RF pin queries.

Related concepts:

- Lot Summary Reports (TSM)

Related tasks:

- Viewing TSM Data at Runtime

#### TSM 2022 Q2 Changes

Learn about new features, behavior changes, and other updates in TSM 2022
 Q2.

- Run TSM with TestStand 2021.
- Use LabVIEW 2021 to run TSM examples and tutorials and develop TSM code modules.
- Quickly debug Semiconductor Sequence Call steps by reviewing test results on the
 Tests tab at runtime.
- Get and set sessions through the Model-Based Instruments API.
- Write code modules with the Mixed-Signal TSM Python API.
- TSM no longer includes step type templates. TSM continues to provide the mechanism
 for other add-ons to install step type templates.
- TSM drops support for LabVIEW 2017. TSM examples and tutorials that use LabVIEW are
 no longer located within year-specific folders. For example, the Accelerometer with
 LabVIEW 2018 example is now located in <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\LabVIEW\Accelerometer.seq 
 instead of in <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer\LabVIEW\2018\Accelerometer.seq .

Related concepts:

- TSM Example Programs
- Semiconductor Sequence Call Step
- Tests Tab

Related information:

- Mixed-Signal TSM Python API
- TestStand Directory Structure

#### TSM 2021 Q4 Changes

Learn about new features, behavior changes, and other updates in TSM 2021
 Q4.

- Use the Perform Part Average Testing step to perform part average testing for any
 tests with part average testing enabled that have already been performed for the
 current part. Use the Perform Part Average Testing step to determine whether to
 perform part average testing before or after inline QA and other steps.
- Call larger and more complex test sequences with the Semiconductor Sequence Call
 step. Use the Semiconductor Sequence Call step's Step Name.Published Data Id field
 to assign tests to Semiconductor Multi Test steps, even if multiple Semiconductor
 Multi Test steps in the called sequence publish the same data ID.
- Analyze sequences that include the Semiconductor Sequence Call step in the TestStand
 Sequence Analyzer to resolve errors and warnings before deploying your test program.
- Customize the MIR EXEC_TYPE field in your STDF records to simplify downstream STDF tools and
 scripts.
- The default value of the Master Information Record (MIR) EXEC_TYPE field has changed
 to NI STS Software and is no longer dependent on the version of the STS Software you
 have installed. You can also customize the EXEC_TYPE field value.

Related concepts:

- Perform Part Average Testing Step (TSM)
- Part Average Testing (TSM)
- Semiconductor Sequence Call Step
- Customizing STDF MIR, SDR, and WCR Field Values (TSM)
- Logging Custom Data to the STDF Log File (TSM)

Related reference:

- TSM Sequence Analyzer Rules Descriptions

Related information:

- TestStand Semiconductor Module Release Notes

#### TSM 2020 Changes

Learn about new features, behavior changes, and other updates in TSM
 2020.

##### Alarms

Note

ComplianceAlarm

ComplianceAlarm

##### Grouping NI-DCPower Instrument
 Channels for Use in Multi-Channel Sessions

You can group multiple NI-DCPower instrument channels and treat them as a single
 logical instrument and control them in one session. When all NI-DCPower instrument
 channels belong to a single group you can avoid using session loops in code modules.
 The instrument driver performs most operations on multiple channels in a single
 function call in parallel to achieve improved multisite efficiency. Refer to the
 instrument driver help for information about hardware limitations that prevent
 certain instruments from operating together as a single instrument.

By
 default, when you create a new NI-DCPower instrument in the pin map file, TSM
 creates a single channel group containing all instrument channels. TSM creates a
 single session for each channel group of NI-DCPower instruments in the pin map file.
 TSM 2019 and earlier do not allow for channel grouping and pin maps created with
 older versions of TSM do not contain channel group information. You must convert all
 NI-DCPower instruments in these pin maps to use channel groups.

##### Offline Mode

The default main menu now displays an Offline Mode indicator
 to the right of the Help menu when you enable Offline Mode.
 When you disable Offline Mode, the default main menu no longer displays the
 Offline Mode indicator.

##### Semiconductor Sequence Call
 Step

Use the Semiconductor Sequence Call step to call a sequence and pass tests to
 Semiconductor Multi Test steps in the called sequence.

##### Set Relays Step

Use the Set Relays step to control relays and to apply relay configurations.

##### Test Program Performance
 Analyzer

- You can add notes and additional metadata to Test Program Performance
 Measurement Data Logs for improved record keeping during performance
 optimization.
- Use the Log Browser Window to specify a directory of performance log files, view
 log files and their metadata, and select log files to open and/or compare.
 For improved performance while loading data in the in the Test Program
 Performance Analyzer, you can load only a sample of log files within a
 directory by specifying the Log Data Sample
 Rate.

##### Additional
 Improvements

- Use Semiconductor Multi Test steps and Semiconductor Action steps in most types of loops without
 the possibility of incorrect results. There remain some limitations to using
 TSM steps in loops but the steps report run-time errors in those situations
 instead of producing incorrect results.
- Specify the relays you use in your code module on the Options tab of a Semiconductor Multi Test
 or Semiconductor Action step that uses the code module.
- New TSM sequence analyzer rules return errors in the following situations:
  - When instruments defined in the pin map are missing from Measurement
 & Automation Explorer (MAX)
  - When the Specify DUT Pins or
 Specify Site Relays option on the Options
 tab of a Semiconductor Multi Test step or a Semiconductor Action
 step is enabled, but some of the included DUT pins or relays are not
 in the pin map file.
- Create a basic TSM test program from a digital pattern project. Select Semiconductor Module»Create Test Program from Digital Pattern Project to launch the Create Test Program from Digital Pattern
 Project dialog box.
- Use an expression to determine the software bin at run time. The
 Result.Evaluations property of the Semiconductor Multi
 Test step type includes a new FailBinExpr property, which
 is an expression that determines the software bin at run time. If the test
 fails and this expression is not empty, the Semiconductor Multi Test step
 evaluates the expression and copies the evaluated value to the
 FailBin property.
- Support for logging failed cycle information from NI-Digital Pattern Drivers in .NET
 applications.
- The Create Multisite Data for Analog Output VI and corresponding .NET method
 have been updated. The Create Multisite Data for Analog Output VI for DAQmx
 now supports multiple task pin queries and the Site Pin
 Data indicator for the Per Site Data instance of this VI has
 improved data representation. Outputs from the TSM .NET API more closely
 match the DAQmx API and the samplesPerSitePerPin
 parameter of the
 CreatePerSiteMultisiteDataForDAQmxAnalogOutput .NET
 method, which supplants the
 CreatePerSiteMultisiteDataForAnalogOutput .NET
 method, has improved data representation.

##### Compatibility

- You cannot use multiple Semiconductor Multi Test steps or Semiconductor
 Action steps configured to use multiple threads in While loops, in Do While
 loops or in For loops that use the Custom Loop option when performing
 multisite testing. The steps report a run-time error in these situations.
 Use other types of loops instead, such as For loops that use the Fixed
 Number of Iterations option. Previously, NI recommended not to use
 Semiconductor Multi Test steps or Semiconductor Action steps in loop
 blocks that the TestStand For step and For Each step create because
 using multiple Semiconductor Multi Test steps or Semiconductor Action
 steps in a loop can result in incorrect step results in certain
 multisite situations. NI previously recommended making the last step in
 the loop block a Semiconductor Multi Test step or a Semiconductor Action
 step with the Multisite Option set to
 One thread only to avoid incorrect behavior
 of Semiconductor Multi Test steps or Semiconductor Action steps in a
 loop.
- For code modules that use relays, you must specify the relays on the Options
 tab of the Semiconductor Multi Test step or Semiconductor Action step that
 uses the code module. Previously, TSM included all relays in the
 SemiconductorModuleContext for all steps. As a
 result, a test step that uses relays and executes successfully in
 previous versions of TSM might generate a run-time error in version
 2020. To prevent the run-time error, specify the relays that the code
 module uses on the Options tab.

Related concepts:

- Alarms Panel
- Grouping Instruments or Channels (TSM)
- Disabling Offline Mode (TSM)
- Semiconductor Sequence Call Step
- Set Relays Step (TSM)
- Test Program Performance Measurement Data Logs (TSM)
- Log Browser Window (TSM)
- Loading Data in the Test Program Performance Analyzer (TSM)
- Semiconductor Multi Test Step
- Semiconductor Action Step
- Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)
- Compliance Alarm

Related tasks:

- Enabling Offline Mode (TSM)

Related reference:

- Pin Map File XML Structure (TSM)
- TSM Sequence Analyzer Rules Descriptions

Related information:

- Create Test Program from Digital Pattern Project Dialog
 Box
- Flow Control Step Types

#### TSM 2019 Changes

Learn about new features, behavior changes, and other updates in TSM
 2019.

- Offline Mode—Use Offline Mode in TSM to develop, run, and debug
 test programs only on a computer without access to NI instruments. Ensure you meet the
 requirements on the computer on which you want to use Offline Mode.
- Grouping Instruments for Use in Multi-Instrument Sessions—You
 can group multiple NI-Digital Pattern instruments or multiple NI-SCOPE instruments
 together and treat them as a single instrument. When all the instruments of the same type
 belong to a single group or when the instruments of the same type in a subsystem belong to
 a single group, you do not need to use parallel For Loops to iterate over the instrument
 driver sessions. The instrument driver specific to the grouped instruments performs most
 operations on all channels in parallel to achieve improved multisite efficiency. Refer to
 the instrument driver help for information about hardware limitations that prevent certain
 instruments from operating together as a single instrument. By default, when you create
 a new NI-Digital Pattern instrument or a new NI-SCOPE instrument in the pin map file,
 TSM sets the group attribute to Digital or to
 Scope so that all newly created NI-Digital Pattern instruments or
 NI-SCOPE instruments belong to the same group. TSM creates a single session for each
 group of NI-Digital Pattern instruments in the pin map file. TSM 2017 and earlier do not
 automatically group NI-Digital Pattern instruments or NI-SCOPE instruments together in
 pin map files. Use the Pin Map Editor to modify existing pin map files to change the
 value of the Group option for each instrument to assign the
 instrument to the same group.
- Instrument Model Library—The Instrument Model Library is a
 collection of XML files that describe instruments. Instrument model description files
 include general information, details for connection components (channels, ports,
 resources), and configuration properties of the instrument and its resources. The
 instrument model description file does not include session information. Use the
 Instruments tab of the Pin Map Editor to add and modify instances of model-based
 instruments in the pin map. Use the following new TSM Code Module API VIs to
 return the names, properties, and values of model-based instruments:
  - Get All Model-Based Instrument Names—Use this VI to return the instrument names and
 models for all model-based instruments in the Semiconductor Module context. You can
 use instrument names to query the model properties for the information needed to
 create the appropriate sessions to drive the instrument.
  - Get Model-Based Instrument Property List—Use this VI to return an object containing
 the name of the model and an array of ModelBasedInstrumentProperty objects that
 contain the names and values of the instrument properties.
  - Get Model-Based Instrument Resource Property List—Use this VI to return an array of
 IModelBasedInstrumentResourcePropertyList objects where each element contains the name
 of a resource as well as an array of ModelBasedInstrumentProperty objects that contain
 the names and values of the instrument resource properties.
  - Get Model-Based Instrument Property Value—Use this VI to return the value of a named
 property and a Boolean value indicating whether or not the named property was found in
 the property list supplied.
  - Get Model-Based Instrument Resource Property Value—Use this VI to return the value
 of a named property from a named resource and a Boolean value indicating whether or
 not the named property was found in the array of resource property lists
 supplied.
- Connecting Shared Resources in a Pin Map—Use the Connections
 table to connect shared resources in a pin map. A shared resource is a device on the
 tester or DIB that is connected to an instrument or relay driver module and shared by
 multiple sites. You can connect shared resources using system pins and system relays, or
 by using DUT pins and site relays.
- Relay Configurations—
  - In the Pin Map Editor, you can now create relay configurations to set multiple
 relays to a state defined in the pin map.
  - Use the Apply Relay Configuration VI or the ApplyRelayConfiguration 
 .NET method to perform relay actions on the relays in the relay configuration.
- CSV Test Results Log—You can now enable and configure the new
 CSV Test Results Log to store data in a comma-separated values text file, which provides
 better performance than the Debug Test Results Log result processor in a production
 environment. The CSV Test Results Log result processor generates a single file for all
 sites in the test program. You can open the .csv file directly in a
 spreadsheet application for analysis or to correlate test results. The Test Results Log
 is now the Debug Test Results Log.
- InstrumentStudio Integration—
  - Use the InstrumentStudio toolbar button to launch InstrumentStudio, which is a pin-
 and site-aware, software-based front panel application you can use to monitor,
 control, and record measurements from supported devices.
  - You can also use the InstrumentStudio Project Panel in the Test Program Editor to
 launch InstrumentStudio, or to specify an InstrumentStudio configuration file to use
 in a test program. Note If
 you launch InstrumentStudio in any other way, such as from the Microsoft Windows
 Start menu, InstrumentStudio is not pin and site aware.
- Multisite Scaling Improvements—TSM 2019 includes extensive
 optimizations for multisite testing with improved parallel test efficiency (PTE). These
 performance improvements can significantly increase throughput for systems, depending
 heavily on the specifications of the system.
- Test Program Development and Debugging Improvements—
  - You can now configure TSM-specific environments. TSM is enabled by default in custom
 TSM environments you create. You can disable and re-enable TSM in a custom TSM
 environment. Use the Configure Environment dialog box to create, load, and edit an
 environment.
  - You can now use the Site Data Exists and the Global Data Exists TSM Code Module API
 to check for the existence of per-site or global data.
  - Switching settings for are disabled. Use relays in the pin map to perform switching
 operations.
  - The Test Program Performance Analyzer graphs include the following changes:
    - The Average Step Times graph is now the Step Time Statistics
 graph with options to show average step times, PTE%, and a
 distribution box plot.
    - You can now view statistical distribution of test times as a
 scatter distribution.
  - You can log failed cycle information from the NI-Digital Pattern Driver to STDF Log
 files.
  - Use the Per-Instrument to Per-Site Pattern Results VI to convert Pass/Fail pattern
 burst results from a call to the NI-Digital Pattern driver into per-site results that
 you can use in per-site loops in code modules.
  - Use the Per-Instrument to Per-Site Data VI or
 PerInstrumentToPerSiteData .NET method to transform data that is
 arranged by instruments and channels into data arranged by sites and pins.
  - The LabVIEW VI Analyzer now verifies that VIs use the High Resolution Polling
 Waiting VI instead of other wait functions to improve wait time precision.
  - TSM now supports pin-based per-site publishing. Use the optional
 Pin and Published Data Id parameters
 of the Publish Data VI or PublishPerSite .NET method to publish data
 for each site to tests that have non-empty Pin and
 Published Data Id fields.
  - You can now use the Publish Data VI to publish data for a single value from a single
 site.
  - In LabVIEW, you can now use the TSM controls instead of string controls to select
 from the pins, relays, relay configurations, specifications, published data IDs, and
 input data IDs of a linked sequence file. To use this feature, you must link a LabVIEW
 project file to a TSM sequence file.
  - Updated step templates better conform to suggested NI code style guidelines and test
 program structure. The step templates include the following major changes: Type of Change
 DetailsSource File/Directory Structure
 LabVIEW version-specific directories
 Template-specific directories
 Template_ prefix changed to Template -.
 Behavior of Adding to Test Program
 Template-specific default location
 Instantiating a .NET template contained within a .NET assembly with
 the same name as a template that has already been instantiated
 automatically references the existing assembly
 Significant Coding Style Changes
 Use of the High Resolution Polling Wait VI for increased precision in
 wait times
 Use of re-entrant VIs
 Disabled automatic error handling
 VIs no longer contain compiled code
 Changed connector panes
 Eliminated coercion dots by explicitly converting data
 Renamed error and TSM context controls and indicators
- Additional Improvements—The NI TestStand 2019 Semiconductor
 Module includes the following additional enhancements:
  - The STDF Log now includes the correlation offsets file path you specify in the Load
 Correlation Offsets step as a DTR.
  - In the Pin Map Editor, you can now change the type of an instrument and maintain the
 relevant property values and existing connections among pins, relays, instruments, and
 channels. Right-click the instrument and select Change to in
 the context menu or use the Instrument Type drop-down menu to
 select the new instrument type.
  - The TSM Operator interface now displays the active STS Software installed on the
 system.
  - The Pin(s) to NI-Digital Pattern Session(s) VI and the GetNIDigitalPatternSession(s)
 .NET methods now support pin queries for single or multiple pins that return a single
 NI-Digital instrument.
  - The Set Site Data VI is now a polymorphic VI that allows the use of 2D arrays, in
 which each row of the array contains data corresponding to one site.
  - You can now use the generic versions of the GetSiteData and GetGlobalData .NET
 methods to specify a data type to cast the retrieved data to before returning it.
  - If you configure the LabVIEW Adapter to use the LabVIEW Development System, the
 window title of the VI clone displays a comma-separated list of the site numbers
 executing on that VI clone. For example, the window title for a VI clone that executes
 sites 1 and 2 for the Continuity VI will read: Continuity.vi: Site(s) 1,2.
  - The Lot Summary Report now includes a Test Results section that contains a table of
 test evaluation results by site for all the tests that executed at least once in the
 lot, sorted by execution order. You can use this data to compare the results of lots,
 which can be helpful during debugging. You can programmatically obtain the same data
 with the Test Results Statistics TSM Application API.
  - The Test Results Log is now the Debug Test Results Log. With the new performance
 improvements to the Debug Test Results Log, you can now leave the Debug Test Results
 Log enabled during production. Enabling the Debug Test Results Log might affect the
 performance of a test program. Perform a benchmark to ensure no performance loss
 exists when you enable the Debug Test Results Log.

##### Compatibility

- TSM 2019 modifies the behavior of the Control Relay VI Multiple Relays - Multiple
 Actions polymorphic instance and the ControlRelay .NET method. Final
 relay state positions are now determined sequentially, based on the order of the input
 relays or relay groups. The following table demonstrates the change in relay behavior
 between TSM 2017 and TSM 2019: Relays/Relay Groups (Input)
 States (Input)
 Final States (TSM 2017)
 Final States (TSM 2019)Rly1, Rly2, Rly3, Rly1
 Open Relay, Close Relay, Open Relay, Close Relay
 Rly1:Closed, Rly2:Closed, Rly3:Open
 Rly1:Closed, Rly2:Closed, Rly3:Open
 Rly1, Rly2, Rly3, Rly1
 Close Relay, Close Relay, Open Relay, Open Relay
 Rly1:Closed, Rly2:Closed, Rly3:Open
 Rly1:Open, Rly2:Closed, Rly3:Open
 Grp1 (Rly1, Rly2, Rly3), Rly1
 Close Relay, Open Relay
 Rly1: Closed, Rly2: Closed, Rly3: Closed
 Rly1: Open, Rly2: Closed, Rly3: Closed
 Rly1, Grp1 (Rly1, Rly2, Rly3)
 Close Relay, Open Relay
 Rly1: Closed, Rly2: Open, Rly3: Open
 Rly1: Open, Rly2: Open, Rly3: Open
- You can group multiple NI-Digital Pattern instruments or multiple NI-SCOPE instruments
 together and treat them as a single instrument. When all the instruments of the same type
 belong to a single group or when the instruments of the same type in a subsystem belong to
 a single group, you do not need to use parallel For Loops to iterate over the instrument
 driver sessions. The instrument driver specific to the grouped instruments performs most
 operations on all channels in parallel to achieve improved multisite efficiency. Refer to
 the instrument driver help for information about hardware limitations that prevent certain
 instruments from operating together as a single instrument. By default, when you create a
 new NI-Digital Pattern instrument or a new NI-SCOPE instrument in the pin map file, TSM
 sets the group attribute to Digital or to
 Scope so that all newly created NI-Digital Pattern instruments or
 NI-SCOPE instruments belong to the same group. TSM creates a single session for each group
 of NI-Digital Pattern instruments in the pin map file. TSM 2017 and earlier do not
 automatically group NI-Digital Pattern instruments or NI-SCOPE instruments together in pin
 map files. Use the Pin Map Editor to modify existing pin map files to change the value of
 the Group option for each instrument to assign the instrument to
 the same group.
- The Test Results Log is now the Debug Test Results Log.
- The following table lists how TSM 2019 changes the error reporting behavior when you
 enable or disable the STDF Log. Conditions
 STDF Log Enabled
 STDF Log DisabledMultiple tests with 0 as a test number or blank test numbers and different
 test names or evaluation types
 Error in TSM 2017No error in TSM 2019
 No error in TSM 2017No error in TSM 2019
 Multiple tests with non-zero test numbers and different test names or
 evaluation types
 Error in TSM 2017Error in TSM 2019
 No error in TSM 2017Error in TSM 2019
- The Get Site Data VI and the GetSiteData .NET method now return an
 error if the site data does not exist for all the sites in the Semiconductor Module
 Context.
- TSM 2019 stores the path of the simulated handler driver in the
 HandlerDriverSequenceFilePath station setting property when you enable
 the NI built-in simulated handler driver. TSM 2017 or earlier leaves that property
 unchanged when you enable the simulated handler driver.
- Names for NI instruments in the pin map file are no longer case sensitive. Names for
 custom instruments in the pin map file remain case sensitive.
- TSM 2019 renames the Limit Number of Results Reported option in
 the Debug Test Results Log Options dialog box to Limit Number of Results
 Displayed in Report View . The option no longer applies to the Debug Test
 Results Log file and now applies only to the Report View.
- TSM 2019 updates the directories for some LabVIEW examples and tutorials. Verify the
 example and tutorial directories before using them.
- If you modified any TSM step templates, compare the modified versions to the updated
 versions of the step templates in NI TestStand 2019 Semiconductor Module.

Related concepts:

- Offline Mode (TSM)
- Grouping Instruments or Channels (TSM)
- Subsystems and Pin Maps (TSM)
- Pin Map Editor (TSM)

Related reference:

- Pin Map File XML Structure (TSM)

#### TSM 2017 Changes

Learn about new features, behavior changes, and other updates in TSM
 2017.

##### Step Templates

TSM includes the
 following new step types with template code:

- NI-DAQmx Create AI Voltage Tasks
- NI-DAQmx Acquire AI Voltage Waveforms
- NI-DAQmx Clear Tasks

##### Additional Instrument Support

The
 TSM Code Module API now includes support for the PXI-2567 relay
 driver module. Install NI-SWITCH 17.0 or later to use the built-in
 support for the PXI-2567 relay driver module in TSM.

Use the
 Relay Driver Module section of the System View in the Digital
 Pattern Editor 18.0 to control and monitor relays.

##### TSM Sequence Editor UI Configuration

The default TSM UI Configuration of the TestStand Sequence Editor
 includes the following changes to streamline semiconductor test
 program development.

- Simplified toolbar, including the following changes: Toolbar
 Change
 Standard
 No change
 Debug
 Removed
 Environment
 The following items have been removed: Selected Adapter
 User Manager
 Find Previous
 Find NextThe Lock/Unlock UI Configuration toggle
 button is set to Lock.
 Navigation
 No change
 Help
 The following items have been removed: Guide to Documentation
 Getting Started
 Web Resources
 Discussion Forum
 Sequence Hierarchy
 Removed
 Sequence Analyzer
 No change
 Semiconductor Module
 The following debug items have been added:
 Step Into
 Step Over
 Step OutThe Launch
 InstrumentStudio button has been
 added.
- Altered Execute menu that replaces the
 Test UUTs and Single Pass items with the Start Lot and
 Single Test items
- Modified Insertion Palette pane that displays the Semiconductor
 Module folder and the Action Step at the top of the Step
 Types list
- More detailed Steps pane, including the following changes:
  - The Steps pane of the Sequence File window
 expands the Description 
 column to include the VI name or
 ClassName:MethodName for the associated code
 module. The pane also includes new Num
 Tests , Pins ,
 and Multisite Option 
 columns.
  - The Steps pane of the Execution window includes
 a new Module Time column.

When you launch TSM for the first time or enable TSM, it loads the
 TSM UI Configuration, named
 NI_SemiconductorModule, and saves the
 most recently active UI configuration as
 NI_SemiconductorModule_SavedLayout.
 When you disable TSM, TestStand loads the
 NI_SemiconductorModule_SavedLayout UI
 configuration. You can modify the TSM UI Configuration and restore
 it to the default state.

##### Test Program Performance Analysis

During the test program development phase, you can now
 use built-in TSM tools to measure test program performance and then
 analyze the resulting data with the Test Program Performance
 Analyzer. Some common use cases include identifying the slowest test
 times, identifying low parallel test efficiency (PTE) values, and
 displaying the overall socket time and the calculated PTE value for
 each site configuration.

##### Static Code Analysis

TSM now
 includes general, performance, best practices, and statistics rules
 to use in the TestStand Sequence Analyzer. The TSM rules are enabled
 by default.

TSM now installs the following test, enabled by
 default, to the LabVIEW VI Analyzer in the TestStand
 Semiconductor Module section:

- TSM Context Closing —Verifies that a VI
 properly closes Semiconductor Module Context references.
 Detects cases where the output of a Semiconductor Module
 Context reference is not wired or not wired to a Close
 Reference function. Closing references in LabVIEW frees up
 memory that LabVIEW allocates for the references. Failure to
 close references causes reference leaks, which can
 negatively affect the performance of the VI over time.

Refer to the *LabVIEW Help* for more information about
 the LabVIEW VI Analyzer. In LabVIEW, select Help»LabVIEW Help to launch the *LabVIEW
 Help*.

##### Enabling Sites

The default
 Configure Lot Settings dialog box now
 sets the number of sites to the number of sites in the test program
 pin map. You can use the Enabled Sites
 control in the dialog box to enable or disable specific sites. You
 can no longer use the Configure Station
 Settings dialog box to specify the number of
 sites to test.

##### Examples, Tutorials, and Step Templates
 Support LabVIEW 2018 Features

The TSM examples,
 tutorials, and step templates incorporate LabVIEW 2018 support for
 Parallel For Loops with error registers and the High Resolution
 Polling Wait VI. Refer to the *LabVIEW Help* for more
 information about these LabVIEW features. In LabVIEW, select Help»LabVIEW Help to launch the *LabVIEW Help*.

The
 examples and tutorials include LabVIEW 2017 and earlier and LabVIEW
 2018 and later directories for support files based on the version of
 LabVIEW you want to use.

When you use TSM step templates, TSM
 selects the version of the VI template that corresponds to the
 active version of LabVIEW on the computer. You can save
 version-specific or version-neutral custom templates in the
 <TestStand Public> directory.

##### Support for Correlation Offsets

You can generate a tab-delimited correlation offsets
 template file based on the numerical limit tests in a sequence file
 by selecting Semiconductor Module»Export Correlation Offset Template file based on
 <filename>. You can use the template file as a starting point
 for a custom correlation offsets file.

Use the Load
 Correlation Offsets Step and associated edit tab to load and apply
 correlation offset values to test results on a per-site basis at run
 time before evaluating the test result data against limits. The Test
 Results Log includes the correlation offset values.

##### Get Test Information Step

The
 Get Test Settings step was redesigned and renamed to Get Test
 Information. Use the step and the associated edit tab to more easily
 obtain the values for lot settings, station settings, STS state,
 execution data, and custom test conditions.

##### Control STS Test Head Step

Use
 the Control STS Test Head step and associated edit tab to control
 properties of the STS. The step requires STS Maintenance Software
 17.1 or later and must be run on an STS. Use the Get Test
 Information step to obtain the
 TestHead.TestHeadAvailable property at run
 time to determine whether you can access the STS
 properties.

##### Additional Improvements

The NI
 TestStand 2017 Semiconductor Module includes the following
 additional enhancements:

- Custom execution captions—The Windows pane and the Execution
 window now display the site number and part ID in addition
 to the sequence filename and testing state.
- Pin Group and Relay Group API—Use the Get Pins in Pin Group(s)
 API to obtain a list of pins contained in the pin group or
 list of pin groups you specify. Use the Get Relays in Relay
 Group(s) API to obtain a list of relays contained in the
 relay group or list of relay groups you specify.
- Numerical order of site numbers—The Get Site Numbers VI and the
 SiteNumbers .NET property now
 return site numbers in numerical order instead of in a
 random order determined by the order in which sites execute.
- OnSiteTestingComplete—Use the OnSiteTestingComplete callback
 sequence to perform actions on a DUT or on instruments after
 all DUT tests have completed and TSM has assigned a bin to
 the DUT. TSM calls the sequence after the MainSequence
 sequence, after all PAT tests complete, and after TSM
 assigns a bin to the DUT.
- Report Orientation of Test Results Log—You can now specify the
 orientation of the Test Results Log. The default is portrait
 orientation. Landscape orientation uses wider columns for
 tests with long test numbers or test names.
- SemiconductorModuleManager parameter in handler/prober driver
 entry points—The handler/prober driver entry points now
 include a SemiconductorModuleManager 
 parameter, which is an object reference to an instance of a
 Semiconductor Module Manager that you can use in
 applications that use the TSM Application API. Use this
 object reference to get information about test execution,
 obtain test statistics, monitor the state of the test
 system, and so on.
- Menu and Toolbar Improvements—You can now use the
 Semiconductor Module menu or
 the TSM toolbar to launch InstrumentStudio.
- Operator Interface Improvements—The default TSM operator
 interfaces now include an Open STS Maintenance
 Software button to launch STS
 Maintenance Software 17.1 or later. The operator interfaces
 also display the status of an STS running STS Maintenance
 Software 18.0 or later. The operator interfaces disable the
 Start Lot and Single Test buttons when
 STS Maintenance Software 18.0 or later is using the tester.
- Adding text data to Test Results Log—You can now add data that
 is not a measurement or test limit to the Test Results Log.

##### Compatibility

Refer to the List of Known Issues in
 NI TestStand 2017 Semiconductor Module on the NI website for a list
 of known issues in NI TestStand 2017 Semiconductor Module (TSM).

- TSM removed support for custom operator interfaces based on the
 default NI TestStand 2013 Semiconductor Module LabVIEW
 operator interface. Those operator interfaces might not
 function correctly in NI TestStand 2017 Semiconductor
 Module. NI TestStand 2014 Semiconductor Module introduced
 the TSM Application API and significant changes to the
 default operator interfaces to simplify operator interface
 implementation. You must upgrade custom operator interfaces
 to use this new technology.
- TSM removed many custom properties from the
 NI.SemiconductorModule container in the attributes of the
 ModelData container passed to process model plug-ins.
 Previous versions of TSM used these properties to
 communicate information among TSM process model plug-ins.
 This information is now available only in the TSM
 Application API and the Get Test Information step.
- TSM 2017 installs SeqEdit.exe.config in the
 <TestStand>\Bin directory
 and overwrites any existing file with the same filename in
 that directory. If you have created a custom
 SeqEdit.exe.config file ,
 complete the following steps to preserve the custom file.
  1. Move the existing
 eqEdit.exe.config file to a
 location outside the
 <TestStand> 
 directory.
  2. Install TSM 2017.
  3. Compare the
 SeqEdit.exe.config file TSM
 2017 installed to the custom version of the file
 and merge the custom changes into the file TSM
 2017 installed.

Related concepts:

- TSM Code Module API
- TSM Sequence Editor UI Configuration
- TSM Steps Pane
- Test Program Performance Analyzer (TSM)
- Common Use Cases for Measuring Test Program Performance (TSM)
- Using LabVIEW VI Analyzer (TSM)
- Configure Lot Settings Dialog Box (TSM)
- Exporting a Correlation Offsets Template File (TSM)
- Load Correlation Offsets Step (TSM)
- Debug Test Results Logs (TSM)
- Get Test Information Step (TSM)
- Get Test Information Tab (TSM)
- Control STS Test Head Step (TSM)
- Control STS Test Head Tab (TSM)
- Part Average Testing (TSM)
- Using the Semiconductor Module Manager Object
- TSM Application API
- Semiconductor Module Menu

Related tasks:

- Measuring Test Program Performance (TSM)

Related reference:

- TSM Sequence Analyzer Rules Descriptions
- Overview of Test Program Components
- Semiconductor Module Toolbar Buttons

Related information:

- TestStand Directory Structure

#### TSM 2016 SP1 Changes

Learn about new features, behavior changes, and other updates in TSM 2016
 SP1.

##### Step Templates

Use the TSM step types with template code
 to perform common operations, such as setting up and closing
 instruments, powering up a DUT, or executing common tests. You can
 modify the code to customize the behavior of the step within a test
 program.

TSM provides template code for the following step
 types:

- Setup and Close
  - NI-DCPower Close
  - NI-DCPower Initialize
  - NI-Digital Pattern Close
  - NI-Digital Pattern Initialize
- DUT Power Up
- DUT Power Down
- Burst Pattern
- Continuity Test
- Leakage Test

##### Additional Instrument Support

The TSM Code Module API now
 includes implementations for NI-DAQmx, NI-DMM, NI-FGEN, and
 NI-SCOPE.

##### Custom Instrument Panels

You can now create custom pin-
 and site-aware instrument panel VIs to debug instruments during test
 program execution at a breakpoint, which can be useful during test
 program development and troubleshooting. Custom instrument panels
 obtain active instrument sessions stored in Semiconductor Module
 context objects using the Set Session VIs or .NET
 methods in the TSM Code Module API. During active test program
 execution, TSM disables the custom instrument panel to avoid
 conflicts.

The custom instrument panel components must reside
 in the <TestStand
 Public>\Components\Modules\NI_SemiconductorModule\InstrumentPanels
 directory for the panels to appear in the Semiconductor Module
 menu.

Refer to the Parametric I/V Instrument Panel example and
 the following resources that you can use as starting points for
 custom instrument panels you create:

- Examples located in the <TestStand
 Public>\Examples\NI_SemiconductorModule\Custom
 Instrument Panels directory
- A template for the required custom instrument panel callback
 sequence file named
 CustomInstrumentPanel.seq 
 located in the
 <TestStand>\Components\Modules\NI_SemiconductorModule\Templates 
 directory
- A template for the required corresponding custom instrument
 panel LabVIEW project files located in the
 <TestStand>\Components\Modules\NI_SemiconductorModule\Templates\CustomInstrumentPanelTemplate 
 directory

Note

<TestStand
 Public>

##### Toolbar Improvements

You can now use the TSM toolbar
 buttons instead of the default TestStand toolbar buttons to resume
 sequence execution from a breakpoint for lot or part
 testing.

##### LabVIEW VI Analyzer Test

TSM now installs the following
 test, enabled by default, to the LabVIEW VI Analyzer in the
 TestStand Semiconductor Module
 section:

- For Loop Error Handling—Verifies error handling in VIs that use
 For Loops. Confirms that errors from the For Loop are merged
 with any errors that occurred before the loop executed to
 ensure that errors that occur before the loop executes are
 propagated correctly.

Refer to the *LabVIEW Help* for more information about
 the LabVIEW VI Analyzer. In LabVIEW, select Help»LabVIEW Help to launch the *LabVIEW
 Help*.

##### Part Average Testing Support

Part average testing (PAT) is
 a method based on statistical analysis to identify and fail parts
 that have characteristics significantly outside the normal
 distribution of other parts in the same lot. TSM does not install a
 default implementation of part average testing. You must use the TSM
 PAT plug-in architecture to customize and perform part average
 testing with TSM. The TSM PAT plug-ins include a required PAT
 callback sequence file and corresponding code modules. The PAT
 callback sequence file contains PAT entry point sequences that TSM
 calls during execution to accomplish part average testing. Use the
 example PAT plug-in, located in the <TestStand
 Public>\Examples\NI_SemiconductorModule\Part Average
 Testing\Example Part Average Testing Plug-In
 directory, as a starting point for custom PAT plug-ins you
 create.

Refer to the Part Average Testing Examples for
 information about enabling and performing part average testing (PAT)
 in a test program.

##### Additional Improvements

The NI TestStand 2016 SP1
 Semiconductor Module includes the following additional
 enhancements:

- The Standard Test Data Format (STDF) Log result processing
 plug-in now generates summary records for the Hardware Bin
 Record (HBR), Software Bin Record (SBR), Test Synopsis
 Record (TSR), and Part Count Record (PCR) records. The
 records are included at the end of the STDF log file and
 have a HEAD_NUM value of 255 to indicate
 that they are summary records. Visit ni.com/info and enter
 the Info Code exr3v6 for information about disabling these
 summary records.
- TSM now uses the EXEC_TYPE and
 EXEC_VER fields in the Master
 Information Record (MIR) of the STDF log file to record
 whether STS Software is installed and which version is
 installed.
- You can now log results only when a DUT fails. Use the
 Log Results Only for DUT
 Failures option in the Test
 Results Logs Options dialog box during
 debugging to record only failures instead of all test
 results.
- You can now use the AvailableSiteNumbers 
 property on the
 NI_SemiconductorModule_StationSettings 
 data type to specify which site numbers from a pin map for a
 test program to use when running the test program. For
 example, you can set this property to disable specific sites
 or to use the particular connections of a pin map that match
 the DIB for the test station. The default TSM operator
 interfaces and the Lot Statistics
 Viewer display only the sites you
 specify. Update existing custom LabVIEW or C# operator
 interfaces to display the configured site numbers when you
 use the AvailableSites station setting. Additionally, you
 can modify the ConfigureStationSettings callback to provide
 a custom operator interface to set the AvailableSites
 station setting. Ensure that any custom handler driver you
 created reads the Boolean values from the
 RequestedSiteState parameter
 in the StartOfTest callback to determine which sites
 to test. If you use the
 AvailableSiteNumbers property to
 specify the set of site numbers for the test program
 to use, the RequestedSiteState
 array contains True values for each site number the
 test uses and False values for each site number the
 test does not use.
- In the Pin Map Editor, you can now manually enter relative file
 paths or manually modify existing file paths to be relative.
 Browsing to a file using the Select Pin Map File dialog box
 always uses an absolute path. The Get All FPGA
 Instrument Names, Get All
 NI-RFPM Instrument Names, Get
 All NI-RFPM De-embedding Data,
 Get All NI-5530 RF Port Module
 Names, and Pin(s) To NI-RFPM
 Sessions TSM Code Module API VIs and the
 GetFpgaInstrumentNames,
 GetNIRfpmInstrumentNames,
 GetNIRfpmSessions, and
 GetAllNIRfpmDeembeddingData TSM
 Code Module API .NET class library methods now
 resolve file paths differently. If the path is an
 absolute path, the VI or method returns the absolute
 path whether the file exists or not. If the path is
 a relative path and the file exists relative to the
 path of the pin map file, the VI or method returns
 the absolute path of the existing file. Otherwise,
 the VI or method returns a string without error.
 This change in behavior breaks any test programs
 that use the previous versions of these VIs or
 methods that expect relative file paths to remain
 unresolved.
- You can now specify and obtain the orientation of data in S2P
 files that characterize the de-embedding network for each
 port. The pin map XML schema now includes a
 deembeddingOrientation attribute
 on the Connection,
 SystemConnection, and
 MultiplexedDUTPinRoute
 elements that you can use with the
 deembeddingFilePath attribute to
 specify the orientation of the data in the S2P file
 relative to the port the channel attribute
 specifies. Valid values are Port1TowardDUT and
 Port2TowardDUT. The Get All NI-RFPM
 De-embedding Data VI and the
 Pin(s) To NI-RFPM Sessions VI
 now include a De-embedding Files indicator that
 returns the path and orientation of the data in the
 S2P file relative to the port you specify. The
 connector pane for these VIs have changed, which
 will not break existing code. However, if you want
 to use the new De-embedding Files indicator, you
 must replace existing VIs with the new versions of
 the VIs on the NI-RFPM VIs palette.
- You can now use the Select All checkboxes
 on the DUT Pins, System Pins, or Pin Groups tabs of the Pin
 Map tab of the Pin Map Editor to add or remove pins from the
 pin group.
- Refer to the Query Pin/Site Measurement for Unsupported
 Measurement Type example in the Multisite Programming
 Scenarios example for information about how to query for
 measurement data for a pin and site combination if the
 Extract Pin Data VI does not
 support the measurement type.

##### Compatibility

Refer to the List of Known Issues in
 NI TestStand 2016 SP1 Semiconductor Module on the NI website for a
 list of known issues in NI TestStand 2016 SP1 Semiconductor Module
 (TSM).

- The default TSM operator interfaces display only the sites you
 specify when you use the
 AvailableSiteNumbers property on
 the NI_SemiconductorModule_StationSettings 
 data type to specify which site numbers from a pin map for a
 test program to use when running the test program. The TSM
 2016 and earlier default operator interfaces and custom
 operator interfaces based on those versions display site
 numbers starting at 0 and increasing by 1, up to the number
 of sites. You must update existing custom LabVIEW or C#
 operator interfaces to display the configured site numbers
 when you use the AvailableSites station
 setting.
- In previous versions of TSM, the RequestedSiteState array in
 the StartOfTest callback contained only True values. Ensure
 that any custom handler driver you created reads the Boolean
 values from the RequestedSiteState 
 parameter in the StartOfTest callback to determine which
 sites to test. If you use the
 AvailableSiteNumbers property to
 specify the set of site numbers for the test program to use,
 the RequestedSiteState array contains True values for each
 site number the test uses and False values for each site
 number the test does not use.
- The version number of the pin map XML schema changed from 1.2 to
 1.3. The schema is not backward compatible with NI TestStand
 2016 Semiconductor Module.
- The Get All FPGA Instrument Names ,
 Get All NI-RFPM Instrument Names ,
 Get All NI-RFPM De-embedding
 Data , Get All NI-5530 RF Port Module
 Names , and Pin(s) To NI-RFPM
 Sessions TSM Code Module API VIs and the
 GetFpgaInstrumentNames ,
 GetNIRfpmInstrumentNames ,
 GetNIRfpmSessions , and
 GetAllNIRfpmDeembeddingData TSM
 Code Module API .NET class library methods now resolve file
 paths differently. If the path is an absolute path, the VI
 or method returns the absolute path whether the file exists
 or not. If the path is a relative path and the file exists
 relative to the path of the pin map file, the VI or method
 returns the absolute path of the existing file. Otherwise,
 the VI or method returns a string without error. This change
 in behavior breaks any test programs that use the previous
 versions of these VIs or methods that expect relative file
 paths to remain unresolved.
- The Get All NI-RFPM De-embedding Data VI and
 the Pin(s) To NI-RFPM Sessions VI now
 include a De-embedding Files indicator that returns the path
 and orientation of the data in the S2P file relative to the
 port you specify. The connector pane for these VIs have
 changed, which will not break existing code. However, if you
 want to use the new De-embedding Files indicator, you must
 replace existing VIs with the new versions of the VIs on the
 NI-RFPM VIs palette.
- TSM now uses the EXEC_TYPE and
 EXEC_VER fields in the Master
 Information Record (MIR) of the STDF log file to record
 whether STS Software is installed and which version is
 installed.

Related concepts:

- TSM Code Module API
- Custom Instrument Panels (TSM)
- Using LabVIEW VI Analyzer (TSM)
- Part Average Testing (TSM)
- Standard Test Data Format (STDF) Log (TSM)
- Debug Test Results Log Options Dialog Box (TSM)
- NI_SemiconductorModule_StationSettings Data Type
- Operator Interfaces (TSM)
- Lot Statistics Viewer (TSM)
- Displaying Specific Site Numbers in Operator Interfaces (TSM)
- ConfigureStationSettings Callback (TSM)
- Pin Map Editor (TSM)
- Common XML Validation Error Messages (TSM)

Related tasks:

- Parametric I/V Instrument Panel (TSM)
- Query Pin/Site Measurement for Unsupported Measurement Type (TSM)
- Multisite Programming Scenarios (TSM)

Related reference:

- Semiconductor Module Toolbar Buttons
- Schema Version Policy (TSM)
- Pin Map File XML Structure (TSM)

Related information:

- TestStand Directory Structure

#### TSM 2016 Changes

Learn about new features, behavior changes, and other updates in TSM
 2016.

##### Semiconductor Action Step

Use the Semiconductor Action step to
 perform an action, such as instrument configuration, with access to
 the pin map and per-site inputs. You can configure multisite and
 per-site input options directly on the step.

##### Support for the Digital Pattern Editor and the NI-Digital Pattern
 Driver

- Select Semiconductor Module Launch Digital Pattern Editor or click the Launch Digital
 Pattern Editor button on the TSM toolbar
 to open digital pattern project files in the Digital Pattern
 Editor.
- Use the Digital Pattern Project panel of the Test Program Editor
 to specify the pathname of the digital pattern project file
 to use in the test program. You can use the Specifications
 Files panel of the Test Program Editor to view the
 specifications files in a digital pattern project.
- The Pin Map schema now includes native support for Digital
 Pattern instruments with the
 NIDigitalPatternInstrument 
 element.
- The NI TestStand 2016 Semiconductor Module natively supports
 digital pattern instruments that use the NI-Digital Pattern
 Driver, such as the PXIe-6570, and legacy digital waveform
 instruments that use the NI-HSDIO driver, such as the
 PXIe-6556. Use the TSM Code Module API that corresponds to
 the type of digital instrument the test system includes. For
 example, use the NI-Digital Pattern VIs to manage digital
 pattern instruments and sessions, to manage digital pattern
 waveform data, and to access digital pattern project files.
 Note The VIs on this palette are available only in
 64-bit LabVIEW.
- The Accelerometer and Multisite Programming Scenarios examples
 now use the NI-Digital Pattern driver. Versions of these
 examples that use the NI-HSDIO driver remain available.

##### Customizing Operator Interface Run-Time Error Behavior

The default
 operator interfaces now write a message to an error log file and
 continue testing when the MainSequence sequence returns a run-time
 error from a source other than TSM, such as a code module or an
 instrument driver. You can change the operator interface run-time
 error behavior by using the two new TSM Application API properties
 EndLotOnCodeModuleRuntimeError and
 DisplayDialogOnCodeModuleRuntimeError to specify whether to end the
 lot and display error dialog boxes when the MainSequence sequence
 returns a run-time error from a source other than TSM.

##### C# NI-RFmx and NI-RFPM TSM Code Module API Support

The TSM Code Module
 API now includes C# implementations for NI-RFmx and
 NI-RFPM.

##### Additional Improvements

The NI TestStand 2016 Semiconductor Module
 includes the following additional enhancements:

- Expression to Determine Test Number at Run Time—The
 Result.Evaluations property of the
 Semiconductor Multi Test step type includes a new
 TestNumberExpr field, which is an
 expression that determines the test number at run time. If
 this expression is not empty, the Semiconductor Multi Test
 step evaluates the expression and copies the evaluated value
 to the TestNumber property.
- Indicating End of Wafer using Batch Process Model—Prober drivers
 no longer need to set the EndOfWafer 
 parameter of the EndOfTest handler/prober driver entry point
 to indicate the end of each wafer when using the Batch
 process model. The NI TestStand 2016 Semiconductor Module
 determines the end of the wafer from the
 WaferRuntimeData.StartOfWafer 
 parameter in the StartOfTest handler/prober driver entry
 point. When using the Batch process model, omitting the wait
 for an end-of-wafer status message to set the
 EndOfWafer parameter in the
 EndOfTest entry point might improve performance of the test
 system. Prober drivers must set the
 EndOfWafer parameter at the
 end of each wafer when using the Sequential process
 model.
- Bin Types Passed to Handler—TSM passes an array of bin types to
 the EndOfTest handler/prober driver entry point. Each
 element in the array indicates the type of bin (Pass, Fail,
 and so on) of the corresponding element in the
 SoftwareBinData and
 HardwareBinData parameter
 arrays.
- Temporary STDF File—During testing, the STDF Log result
 processor writes data to a temporary file with an extension
 of .stdtemp in the destination directory you specify in the
 STDF Log Options dialog box.
 When the file completes, the STDF Log result processor
 renames the file to the final report filename you specify.

##### Compatibility

Refer to the List of Known Issues in
 TestStand NI 2016 Semiconductor Module on the NI website for a list
 of known issues in NI TestStand 2016 Semiconductor Module (TSM).

- The default TSM operator interfaces no longer display an error
 message and end testing when the MainSequence sequence
 returns a run-time error from a source other than TSM, such
 as a code module or an instrument driver. Instead, the
 default operator interfaces now write the error message to
 an error log file and continue testing the lot. The change
 in behavior does not affect operator interfaces based on
 source code from previous versions of TSM. You can change
 the operator interface run-time error behavior by setting
 TSM Application API properties on or by handling events from
 the SemiconductorModuleManager object in
 the operator interface source code. By default, when any
 run-time error occurs, TSM assigns the current part to the
 Default Error bin the bin definitions file specifies.
- The file extensions for pin map files and bin definitions files
 have changed from .xml to .pinmap and .bins, respectively.
 You can continue to load pin map files and bin definitions
 files with .xml file extensions without error or warning.
- The Accelerometer examples, located in the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer 
 directory, now use the NI-Digital Pattern driver. Refer to
 the examples in the <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer
 - Legacy Digital directory for
 Accelerometer examples that use the NI-HSDIO driver.
- TSM detects a retested part by comparing the part IDs or die
 coordinates that the handler or prober provides for the part
 to the part IDs and die coordinates that the handler or
 prober provided for previously tested parts. TSM determines
 the number of passing and failing parts and the number of
 parts per bin based on the test results of the last time it
 tested the part. In the STDF log file, TSM sets the PART_FLG
 field of the Part Result Records (PRR) that represent
 results of retested parts and sets the RTST_CNT field of the
 Wafer Result Record (WRR) and the Part Count Record (PCR) to
 the number of parts retested one or more times. Previous
 versions of TSM did not distinguish between the first test
 of a part and subsequent tests of the same part except when
 you clicked the Retest toolbar button in the sequence
 editor. As a result, the part counts that previous versions
 of TSM generate differ from the part counts that the NI
 TestStand 2016 Semiconductor Module generates if the handler
 or prober retests one or more parts. The affected STDF
 fields include the following:
  - PRR.PART_FLG
  - WCR.GOOD_CNT
  - WCR.PART_CNT
  - WCR.RTST_CNT
  - PCR.GOOD_CNT
  - PCR.PART_CNT
  - PCR.RTST_CNT
  - HBR.HBIN_CNT
  - SBR.SBIN_CNT
- The name of the NamespacedSymbol(s)ToValue(s) 
 VI on the Specifications palette has changed to Get
 Specification(s) Value(s) . The name change
 does not require changes to VIs that use the old name.

Related concepts:

- Semiconductor Action Step
- Testing Multiple Sites in Parallel (TSM)
- Subsystem Considerations (TSM)
- Subsystems and Pin Maps (TSM)
- Multisite Programming with Switches (TSM)
- Semiconductor Action Per-Site Inputs Tab
- Digital Pattern Project Panel
- Specifications Files Panel
- TSM Code Module API
- Handling Errors in Operator Interfaces (TSM)
- TSM Application API
- Semiconductor Multi Test Step
- Semiconductor Multi Test Step Execution Overview
- Semiconductor Multi Test Step Properties
- Semiconductor Multi Test Step Constants
- Semiconductor Multi Test Edit Tabs
- Tests Tab
- Scaling Measurement and Limit Data (TSM)
- Semiconductor Multi Test Part Average Testing Tab
- Semiconductor Multi Test Per-Site Inputs Tab
- Semiconductor Multi Test Options Tab
- EndOfTest Handler/Prober Driver Entry Point (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)
- Reports and Data Logs (TSM)
- Specifying Report and Data Log Filenames (TSM)
- GetReportFileName Callback (TSM)
- Standard Test Data Format (STDF) Log (TSM)
- Logging Custom Data to the STDF Log File (TSM)
- Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)
- Customizing STDF MIR, SDR, and WCR Field Values (TSM)
- Customizing STDF PRR Field Values (TSM)
- Adding DTRs to the STDF Log File (TSM)
- Inserting a DTR after a Test Record
- Lot Summary Reports (TSM)
- Customizing the Lot Summary Report Header (TSM)
- Debug Test Results Logs (TSM)
- Customizing Filename
- Logging Text Data
- CSV Test Results Logs (TSM)
- Generating One File per Wafer
- STDF Log Options Dialog Box (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins
- Fetching and Publishing Failed Cycle Information in LabVIEW Code Modules (TSM)
- Fetching and Publishing Failed Cycle Information in .NET Code Modules (TSM)
- Modifying Number of Results to Include in STDF Log Files (TSM)
- Inserting a DTR between Parts
- Modifying Number of Results to Include
- Changing Report Orientation
- Modifying Number of Results to Include

Related reference:

- Failed Cycle Information in Functional Test Records (FTRs) (TSM)
- Customizing STDF WIR and WRR Field Values (TSM)
- Adding DTRs for Non-Wafer Testing or When the Generate One Filer per Wafer Option is Disabled
- Adding DTRs for Wafer Testing When the Generate One Filer per Wafer Option is Enabled

Related information:

- TestStand Directory Structure

#### TSM 2014 SP1 Changes

Learn about new features, behavior changes, and other updates in TSM 2014
 SP1.

##### RFmx Pin Map API

The Pin Map API now supports the RFmx
 Instrument Sessions.

##### NI-RFPM Pin Map API

The Pin Map API now supports the RF
 Port Module (NI-RFPM) API. This API serves as a replacement for the
 NI-5530 Port Module API. It provides several usability enhancements
 for developing multi-port RF measurements.

##### Custom Model Plug-in API

TSM now has an easier way to
 access lot statistics, start times, end times, wafer information,
 and handler/prober information in a custom result processor so you
 can create custom reports and log files.

##### Execution Profiler

Use the Execution Profiler window to
 view and record duration of steps, code modules, and other resources
 a multithreaded TestStand system uses over a period of time. You can
 review the recorded data in graphs and sortable tables to identify
 performance bottlenecks and design flaws and to gain insight into
 the behavior and timing of complex multithreaded systems. You can
 copy the information to external applications, such as Microsoft
 Word or Excel.

##### Additional Improvements

NI TestStand 2014 Semiconductor
 Module SP1 includes the following additional enhancements:

- Base Deployment License—The NI TestStand Semiconductor Module
 Base Deployment License is the minimum license required for
 all deployed TSM-based applications. Activate this license
 to deploy the NI TestStand Semiconductor Module Runtime, the
 TestStand Runtime, and the Switch Executive Runtime. The
 Base Deployment License enables you to run a TSM operator
 interface and test programs on the single test station to
 which the license applies. This license does not grant the
 ability to perform any development tasks using the TestStand
 Sequence Editor, a TestStand custom sequence editor, or the
 TestStand API.
- Improved Getting Started Content—The getting started content now
 includes a brief tour of TSM, an overview of test program
 components, and a new example that demonstrates several
 features of TSM in a test program that makes common
 measurements to test an imagined accelerometer part.
- Start Lot Without Configuring—You can customize the operator
 interface to run without requiring a Configure
 Lot button by implementing the
 ConfigureLotSettings callback to
 programmatically set the LotSettings 
 instead of using a dialog box.
- End of Test dialog box—This dialog box
 launches at the end of each test and displays hardware and
 software bin information on a per test or per lot basis when
 you use the Batch or Sequential process model with the NI
 Simulated Handler Driver.
- Toolbar Enhancements—You can now use the Selected
 Configuration control on the TSM toolbar
 to select the test program configuration to use when
 testing. The available items correspond to the
 configurations in the active sequence file. The value
 initially corresponds to the value of the
 LotSettings.Standard.ActiveConfigurationName 
 property in the lot settings. If the active sequence file
 does not contain a configuration that corresponds to the
 ActiveConfigurationName lot
 setting, the control displays one of the configurations in
 the sequence file. Changing the selected configuration with
 this control does not modify the
 ActiveConfigurationName lot
 setting. You can also use the Configure Lot
 Settings dialog box to change the test
 program configuration.
- .NET (C#) Example Code—Code module development topics include
 .NET example code.

##### Compatibility

Refer to the List of Known Issues in
 NI TestStand 2014 Semiconductor Module SP1 on the NI website for a
 list of known issues in NI TestStand 2014 Semiconductor SP1 (TSM).

- The method for creating custom DTRs has changed when you enable
 the Generate One File per Wafer 
 option.
- The EndOfTest handler/prober driver entry point includes a new
 EndOfWafer parameter, which
 must be set to True at the end of each wafer for the
 Generate One File per Wafer option
 to function correctly and to generate Wafer Result Records
 (WRR).
- To better comply with STDF standards, the START_T field of the
 Master Information Record (MIR) is recorded at the time the
 handler or prober sends the initial start-of-test (SOT)
 signal. In NI TestStand 2014 Semiconductor Module, the
 START_T field contains the time that the operator clicked
 the Start Test button.
- The SemiconductorModuleContext object on any
 instance of a Semiconductor Multi Test step includes only
 the pins specified on the Options tab unless you call the
 step from a process model callback sequence, such as
 ProcessSetup and ProcessCleanup, in which case the
 SemiconductorModuleContext object
 includes all pins in the pin map. In previous versions of
 TSM, when executing with the Sequential or Parallel
 process models,
 SemiconductorModuleContext
 objects included all the pins in the pin map
 regardless of the settings on the Options tab.
 Semiconductor Multi Test steps that execute without
 errors using the Sequential or Parallel process
 models in NI TestStand 2014 Semiconductor Module
 might generate run-time errors in NI TestStand 2014
 Semiconductor Module SP1 if the code module for the
 step attempts to use pins that you did not specify
 on the Options tab. To correct the error, specify
 all necessary pins on the Options tab of the
 Semiconductor Multi Test step.

Related concepts:

- Accelerometer (TSM)
- End of Test Dialog Box (TSM)
- Configure Lot Settings Dialog Box (TSM)
- EndOfTest Handler/Prober Driver Entry Point (TSM)

Related tasks:

- Getting Started with TSM
- Tutorial: Exploring a Basic Semiconductor Test Program with LabVIEW
- Tutorial: Exploring a Basic Semiconductor Test Program with .NET
- Tutorial: Importing Test Limits from a File
- Accelerometer with LabVIEW
- Accelerometer with .NET

Related reference:

- Overview of Test Program Components
- Semiconductor Module Toolbar Buttons

<!--NI_TOPIC bundle=teststand-semiconductor-module path=failed-cycle-info-functional-test.html language=enus -->
## TOPIC 00108: Failed Cycle Information in Functional Test Records (FTRs) (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `failed-cycle-info-functional-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/failed-cycle-info-functional-test.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you publish failed cycle information for a test a Semiconductor Multi Test step defines, TSM stores the failed cycle information in the Functional Test Record (FTR) for that test. Because an FTR can contain failed cycle information only for a single cycle, TSM writes multiple FTRs to the STDF L

### Failed Cycle Information in Functional Test Records (FTRs) (TSM)

When you publish failed cycle information for a test a Semiconductor Multi Test step defines,
 TSM stores the failed cycle information in the Functional Test
 Record (FTR) for that test. Because an FTR can contain failed cycle
 information only for a single cycle, TSM writes multiple FTRs to the
 STDF Log file if the data contains information for multiple failed
 cycles.

TSM stores the failed cycle information in the following fields of the FTR:

| Field | Value |
| --- | --- |
| CYCL_CNT | Cycle number from the NI-Digital Pattern Driver History RAM information. If this value is larger than a 32-bit number, TSM does not set this field. |
| REL_VADR | Vector number from the NI-Digital Pattern Driver History RAM cycle information. |
| NUM_FAIL | Number of pins in the pattern with 1 or more failures. |
| RTN_ICNT | Number of actual pin states from the NI-Digital Pattern Driver History RAM cycle information. |
| PGM_ICNT | Number of expected pin states from the NI-Digital Pattern Driver History RAM cycle information. |
| RTN_INDX | Array of pin indexes that corresponds to the actual pin states from the NI-Digital Pattern Driver History RAM cycle information. Each pin index refers to a pin index defined in a Pin Map Record (PMR) for the pin. |
| RTN_STAT | Actual pin states from the NI-Digital Pattern Driver History RAM cycle information. |
| PGM_INDX | Array of pin indexes that corresponds to the expected pin states from the NI-Digital Pattern Driver History RAM cycle information. Each pin index refers to a pin index defined in a PMR for the pin. |
| PGM_STAT | Expected pin states from the NI-Digital Pattern Driver History RAM cycle information. |
| FAIL_PIN | Bitfield that corresponds to the values in the per-pin pass fail array from the NI-Digital Pattern Driver History RAM cycle information. Each bit corresponds to a pin index defined in a PMR record. For example, if the bit in position 1 is set, the pin defined in the PMR with a pin index of 1 failed for the cycle. |
| VECT_NAM | Pattern name from the NI-Digital Pattern Driver History RAM cycle information. |
| TIME_SET | Time set name from the NI-Digital Pattern Driver History RAM cycle information. |

#### Expected Pin State Information in STDF Log
 Files

The failed cycle information includes the expected pin states from the
 NI-Digital Pattern Driver History RAM cycle information. TSM stores this information in the
 PGM_STAT field of the FTR. The pin states from the NI-Digital Pattern Driver History RAM
 cycle information correspond to the pin states defined in the STDF V4 specification
 according to the following table.

| NI-Digital Pattern Driver Pin State | STDF Pin State Value | STDF Pin State Description |
| --- | --- | --- |
| 0 | 0 | Drive Low |
| 1 | 1 | Drive High |
| L | 2 | Expect Low |
| H | 3 | Expect High |
| M | 4 | Expect Midband |
| V | 5 | Expect Valid (not midband) |
| X | 6 | Do not drive or compare |

#### Actual Pin State Information in STDF Log
 Files

The failed cycle information includes the actual pin states from the
 NI-Digital Pattern Driver History RAM cycle information. TSM stores this information in the
 RTN_STAT field of the FTR. The pin states from the NI-Digital Pattern Driver History RAM
 cycle information correspond to the pin states defined in the STDF V4 specification
 according to the following table.

| NI-Digital Pattern Driver Pin State | STDF Pin State Value | STDF Pin State Description |
| --- | --- | --- |
| L | 0 | 0 or Low |
| H | 1 | 1 or High |
| M | 2 | Midband |
| V* | 11 | — |

* This pin state is not defined in the STDF specification. The NI-Digital Pattern
 Driver uses this state only when V<sub>ol</sub> > V<sub>oh</sub> and the pin voltage
 level is between V<sub>ol</sub> and V<sub>oh</sub>.

#### Edge Multiplier Representation

When
 a pin uses an edge multiplier of 2, the NI-Digital Pattern Driver includes two pin states
 for that pin in the History RAM cycle information. For these pins, the FTR contains
 duplicate pin indexes to represent both pin states in the PGM_STAT and RTN_STAT
 fields.

For example, if the pattern uses two pins with PMR pin indexes 1 and 2, and
 pin index 1 uses an edge multiplier of 2, but pin index 2 uses an edge multiplier of 1, the
 pin index and pin state fields in the FTR appear as shown in the following table.

| Field | Value |
| --- | --- |
| PGM_INDX | [1, 1, 2] |
| PGM_STAT | [L, L, H] |
| RTN_INDX | [1, 1, 2] |
| RTN_STAT | [0, 0, 1] |

Parent topic:

Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=fetch-publish-failed-cycle-cs.html language=enus -->
## TOPIC 00109: Fetching and Publishing Failed Cycle Information in .NET Code Modules (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `fetch-publish-failed-cycle-cs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/fetch-publish-failed-cycle-cs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Fetch and publish failed cycle information from an NI-Digital Pattern Driver with your .NET application. Use the following NI-Digital Pattern Driver API in code modules to configure your NI-Digital Pattern instruments to acquire failed cycle information and log this information in the TSM STDF Log f

### Fetching and Publishing Failed Cycle
 Information in .NET Code Modules (TSM)

Fetch and publish failed cycle information from an NI-Digital Pattern Driver with
 your .NET application.

1. Use the following NI-Digital Pattern Driver API in code modules
 to configure your NI-Digital Pattern instruments to acquire
 failed cycle information and log this information in the TSM
 STDF Log file. 
 // Configure the instrument to start acquiring information on the first failed cycle 
session.Trigger.HistoryRamTrigger.TriggerType = HistoryRamTriggerType.FirstFailure;
// Configure the instrument to acquire only failed cycles
session.HistoryRam.CyclesToAcquire = HistoryRamCycle.Failed;
// Set the maximum number of failed cycles you want to acquire per site
session.HistoryRam.MaximumSamplesToAcquirePerSite = 10;
2. After configuring the NI-Digital Pattern instrument and
 bursting a pattern, use the
 FetchMultisiteHistoryRamInformation
 extension method to fetch the failed cycle information and
 organize the information into a format the TSM Code Module API can
 consume. 
 Note The
 TSM .NET code module API provides the
 FetchMultisiteHistoryRamInformation
 extension method for the NIDigital .NET class. It is
 not part of the NI-Digital Pattern Driver
 API.
3. Pass the return value from the
 FetchMultisiteHistoryRamInformation method to the
 historyRamCycleInformation parameter of the
 PublishPatternResults method on the pin query context class
 in the TSM .NET code module API. TSM logs the failed cycle information in
 Functional Test Records (FTRs) in the STDF Log file.

```text
public static void PerformTest(ISemiconductorModuleContext
semiconductorModuleContext, string patternName, string[] patternPins)
{
   var pinQueryContext = semiconductorModuleContext.GetNIDigitalPatternSessionsForPattern(patternPins, out var sessions, out var siteLists);
   var passFailResultsPerSession = new bool[sessions.Length][];
   var historyRamCycleInformationPerSession = new NIDigitalHistoryRamCycleInformation[sessions.Length];
   
   Parallel.For(0, sessions.Length, i =>
   {
      var session = sessions[i];
      var siteList = siteLists[i];

      // Configure instrument to acquire cycle information only for first 10 failed cycles
      session.Trigger.HistoryRamTrigger.TriggerType = HistoryRamTriggerType.FirstFailure;
      session.HistoryRam.MaximumSamplesToAcquirePerSite = 10;
      session.HistoryRam.CyclesToAcquire = HistoryRamCycle.Failed;
      
      // Burst pattern
      passFailResultsPerSession[i] = session.PatternControl.BurstPattern(patternName, patternName, true, new TimeSpan(0, 0, 2));
      
      // Fetch history RAM cycle information
      historyRamCycleInformationPerSession[i] = session.FetchMultisiteHistoryRamInformation(siteList, patternName);
   });
   pinQueryContext.PublishPatternResults(passFailResultsPerSession, historyRamCycleInformationPerSession, "PassFail");
}
```

Parent topic:

Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)

Related concepts:

- TSM Code Module API

Related reference:

- Failed Cycle Information in Functional Test Records (FTRs) (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=fetch-publish-failed-cycle-lv.html language=enus -->
## TOPIC 00110: Fetching and Publishing Failed Cycle Information in LabVIEW Code Modules (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `fetch-publish-failed-cycle-lv.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/fetch-publish-failed-cycle-lv.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Fetch and publish failed cycle information from an NI-Digital Pattern Driver with your LabVIEW application. To configure the NI-Digital Pattern Driver to acquire failed cycle information, place an niDigital property node on the block diagram and set the following properties: Triggers History RAM Typ

### Fetching and Publishing Failed Cycle
 Information in LabVIEW Code Modules (TSM)

Fetch and publish failed cycle information from an NI-Digital Pattern Driver with
 your LabVIEW application.

1. To configure the NI-Digital Pattern Driver to acquire failed
 cycle information, place an niDigital property node on the
 block diagram and set the following properties:
  1. Triggers»History RAM»Type—Set to First
 Failure to start acquiring information
 on the first failed cycle.
  2. History RAM»Cycles to Acquire—Set to Failed
 Cycles to acquire only failed
 cycles.
  3. History RAM»Max Samples to Acquire per
 Site—Set to the maximum number of failed
 cycles you want to acquire per site.
2. After configuring the NI-Digital Pattern instrument and
 bursting a pattern, use the niDigital Fetch Multi-Site
 History RAM Information VI to fetch the failed cycle
 information and organize the information into a format the
 TSM Code Module API can
 consume. 
 Note The
 niDigital Fetch Multi-Site History RAM Information
 VI does not appear on the NI-Digital Pattern Driver
 palette. Browse to and select the VI from the
 NI-Digital Pattern Driver library file
 (niDigital.llb), located in
 the
 <LabVIEW>\instr.lib\niDigital
 directory.
3. Wire the output of the niDigital Fetch Multi-Site History RAM
 Information VI to the History RAM
 Information input of the
 Publish Pattern Results VI in
 the TSM Code Module API. TSM logs the failed cycle
 information in Functional Test Records (FTRs) in the
 STDF Log file.

[IMAGE alt='image' src='GUID-94891EA6-EE75-4019-8B67-1103A5B194FF-a5.png']

Parent topic:

Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)

Related concepts:

- TSM Code Module API

Related reference:

- Failed Cycle Information in Functional Test Records (FTRs) (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=filter-data-verbose.html language=enus -->
## TOPIC 00111: Filtering Runtime Data in the Detailed View

- bundle_id: `teststand-semiconductor-module`
- source_path: `filter-data-verbose.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/filter-data-verbose.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Filter the data you see in the Detailed tab of the Runtime Data Viewer. You can filter data in the Detailed view with the following options: Display Settings—Click to access these settings. You can configure the following options with Display Settings: Show last N batches—Limits the displayed result

### Filtering Runtime Data in the Detailed
 View

Filter the data you see in the Detailed tab
 of the Runtime Data Viewer.

You can filter data in the Detailed view with the following
 options:

- Display Settings —Click to access these settings.
 You can configure the following options with
 Display Settings :
  - Show last N
 batches —Limits the displayed results
 to the most recent batches, up to the specified
 number. This setting only affects what data the
 table displays, but it does not remove data from
 memory. The value specified in Show
 last N batches cannot exceed
 Max History . Refer to
 Viewing TSM Data at Runtime for
 information on configuring the Max
 History setting.
  - Columns To View —This
 setting allows you to reveal or hide specified
 columns.
- The icon in each each table
 column allows you to set filters for that
 column.

Parent topic:

Viewing TSM Data at Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=filter-runtime-data-summary.html language=enus -->
## TOPIC 00112: Filtering Runtime Data in the Summary View

- bundle_id: `teststand-semiconductor-module`
- source_path: `filter-runtime-data-summary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/filter-runtime-data-summary.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filter the data you see in the Summary tab of the Runtime Data Viewer. The Summary tab provides two options for filtering displayed data: the Filter Options panel and the Filter bar at the top of the tab. The Filter bar refines results as you type. The Filter Options panel applies values when you cl

### Filtering Runtime Data in the Summary
 View

Filter the data you see in the Summary tab of the Runtime Data Viewer.

The Summary tab provides two options for filtering displayed data: the Filter
 Options panel and the Filter bar at the top
 of the tab. The Filter bar refines results as you type. The Filter
 Options panel applies values when you click <Enter> or exit
 the field.

Both filtering options are synchronized. Filtering configurations applied in the
 Filter Options panel immediately populate in the
 Filter bar. Conversely, filtering configurations applied
 in the Filter bar immediately populate the corresponding
 filters in the Filter Options panel.

#### Using the Filter Options
 Panel

Click the Filter Options[IMAGE alt='image' src='GUID-78DDB1FE-F738-40B9-A081-4984BC4ED65A-a5.png'] button
 to open the panel. Refer to the following table for Filter
 Options configuration information.

| Filter Option | Description |
| --- | --- |
| Max Parts to Show | Controls how many of the most recent part columns display. Runtime Data Viewer applies this setting after all other filter configurations. Reducing this number improves rendering performance when testing many parts. |
| Part Status Filter | Shows only parts that match one or more of the following statuses: Failed Error Running Passed |
| Alarm Filter | Show only rows or columns that contain alarms. Show Alarmed Tests Only—Hides test rows with no alarmed results in any part column. Show Alarmed Parts Only—Hides part columns with no alarms. |
| Numeric Range Filters | Filter by number or a numeric range of the following filter types: Die X coordinates Die Y coordinates Batch number Site number SW Bin number Test number Note Die X and Die Y filters appear only when at least one tested part includes die coordinate data. Define values in the following formats: Single value (3) Comma-separated list (0, 1, 3) Continuous range (0-3) Combination of single values and ranges (0, 3, 5-9) When a configuration is invalid, the field border turns red and displays a tooltip with the error description. |
| Text Filters | The following filters support partial text matches: Part ID Step Name Test Name Filter entries are not case-sensitive. Use commas to separate multiple values. |

Note

Numeric Range Filters

Text Filters

Filter
 Options

#### Using the Filter Bar

You
 can also type filter information directly in the text field of the
 Filter bar. Filter entries must observe exact filter
 syntax (key:value). Separate multiple filter requirements with a
 comma. For example, site:0, batch:1-5, test#:100-102,
 step:Continuity.

Note

In the Filter bar, a comma always separates two filter expressions,
 however, a comma does not separate multiple values for the same key. To match
 multiple values for one category, you must always designate the key. For
 example, site:0, site:3 is a valid configuration, but
 site:0,3 is an invalid configuration. The Filter
 Options panel value fields accept comma-separated lists (for
 example, 1-3, 5, 15). Configurations entered in the Filter
 Options panel automatically expand into the correct format in
 the Filter bar.

| Category | Key | Value Format | Example |
| --- | --- | --- | --- |
| Site number | site | Single number or range | site:0 |
| Batch number | batch | Single number or range | batch:10-20 |
| Test number | test# | Single number or range | test#:100, test#:105 |
| SW bin number | swbin or softwarebin | Single number or range | swbin:5 |
| Die X coordinate | x or diex | Single number or range | diex:5-10 |
| Die Y coordinate | y or diey | Single number or range | y:1-9 |
| Part ID | partid | Text (substring) | partid:ABC |
| Step name | step or stepname | Text (substring) | step:open short, step:Continuity |
| Test name | test or testname | Text (substring) | test:vcc 1.8v |
| Part status | status | Failed Passed Running Error | status:failed, status:error |
| Alarm (rows) | alarm | tests | alarm:tests |
| Alarm (columns) | alarm | parts | alarm:parts |

Note

Runtime Data Viewer

site:0, status:failed

Runtime Data
 Viewer

status:fail, status:error

Parent topic:

Viewing TSM Data at Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=funcl-test-using-digital.html language=enus -->
## TOPIC 00113: Functional Test Using NI-Digital Pattern Driver (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `funcl-test-using-digital.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/funcl-test-using-digital.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to use the Digital Pattern Instrument for a multisite functional test. This example includes the following main tasks: Query for the sessions for the digital I/O pins under test. Use a parallel For Loop to iterate on every required instrument to burst a pattern. Use th

### Functional Test Using NI-Digital Pattern Driver (TSM)

The following figure shows how to use the Digital Pattern Instrument for a multisite functional test.

[IMAGE alt='image' src='GUID-9B02FC02-54E1-4F4E-990C-9D7F445780A4-a5.png']

This example includes the following main tasks:

1. Query for the sessions for the digital I/O pins under test.
2. Use a parallel For Loop to iterate on every required instrument to burst a pattern.
3. Use the Publish Pattern Results VI to publish per-site Boolean results from the pattern burst.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following test, which evaluates one Boolean result, as
 shown in the following figure:

[IMAGE alt='image' src='GUID-0C3D175A-9444-4C8A-838A-44333567A7BB-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=function-test-milti-reg-hsdio.html language=enus -->
## TOPIC 00114: Functional Test for Multiple Registers Using NI-HSDIO (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `function-test-milti-reg-hsdio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/function-test-milti-reg-hsdio.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to read multiple register values from a digital waveform. This example includes the following main tasks: Query for the sessions for the digital I/O pins. Use a parallel For Loop to fetch the digital waveforms. Rearrange the digital waveforms from per-instrument wavefo

### Functional Test for Multiple Registers Using NI-HSDIO (TSM)

The following figure shows how to read multiple register values from a digital waveform.

[IMAGE alt='image' src='GUID-4A4357C5-BC32-407F-A27A-91654B7904D7-a5.png']

This example includes the following main tasks:

1. Query for the sessions for the digital I/O pins.
2. Use a parallel For Loop to fetch the digital waveforms.
3. Rearrange the digital waveforms from per-instrument waveforms to per-site waveforms.
4. Use a For Loop to scan each per-site waveform to obtain register values for four addresses.
5. Transpose the 2D array so that the first dimension corresponds to sites.
6. Use a site-based instance of the Publish Data VI to publish the register value using the address as a hex string for the Published Data Id.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following tests, where each test evaluates one numeric
 value per register, as shown in the following figure:

[IMAGE alt='image' src='GUID-5F4A1D6B-2F03-4749-9807-4ECC0A98E74C-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=general-tab.html language=enus -->
## TOPIC 00115: General Tab

- bundle_id: `teststand-semiconductor-module`
- source_path: `general-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/general-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The General tab contains the following options: Enable Handler/Prober Driver (Real or Simulated)—Specifies handler/prober options. Handler/Prober Driver—Specifies the handler/prober driver to use. The drop-down menu lists the Built-in Simulated Handler Driver first and any other installed drivers in

### General Tab

The General tab contains the following options:

- Enable Handler/Prober Driver (Real or Simulated) —Specifies handler/prober options.
  - Handler/Prober Driver —Specifies the handler/prober driver to use. The
 drop-down menu lists the Built-in Simulated
 Handler Driver first and any other installed
 drivers in alphabetical order. Select the
 Built-in Simulated Handler
 Driver option to use the NI Built-in
 Simulated Handler Driver. The NI Built-in
 Simulated Handler Driver simulates handler
 functions when you do not have access to a real
 handler.
  - Configure Handler/Prober —Launches a dialog box, which you use to specify handler options.
- Enable Inline QA —Specifies whether to enable inline QA. When you enable this
 option, specify a sequence file to determine the frequency
 of inline QA in the Inline QA
 Algorithm control. The drop-down menu
 displays only algorithms located in the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\InlineQA 
 directory.
- Test Program Directory —(Optional) Limits the selection of the test program to the directory you specify.
- Step Failure Mode —Specifies how the test program continues after a failure occurs. This option mimics the functionality of the Immediately Goto Cleanup On Sequence Failure option on the Execution tab of the Station Options dialog box.
  - Continue on Step Failure —Specifies to continue testing after a failure occurs.
  - Goto Cleanup on Step Failure —Specifies to stop testing after a failure occurs.
- Site Status Part Count —Specifies the number of part test results tracked per site. The site status indicators in the operator interface display the results of the last n parts, where this option specifies n .
- Prevent Execution Tiling —Specifies
 whether to disable tiled execution. When you enable this
 option, specify the site count threshold in the
 if site count is greater than 
 control. This setting automatically disables tiled execution
 when the number of active sites exceeds the specified
 value.

Parent topic:

Configure Station Settings Dialog Box (TSM)

Related concepts:

- NI Built-in Simulated Handler Driver (TSM)
- Performing Inline Quality Assurance Testing (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=generating-one-file-per-wafer.html language=enus -->
## TOPIC 00116: Generating One File per Wafer

- bundle_id: `teststand-semiconductor-module`
- source_path: `generating-one-file-per-wafer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/generating-one-file-per-wafer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable the Generate One File per Wafer option on the CSV Test Results Log Options dialog box to create a log file for each wafer you test. Each new log file resets the batch number to 1.

### Generating One File per Wafer

Enable the Generate One File per Wafer option on the CSV Test Results Log
 Options dialog box to create a log file for each wafer you test.
 Each new log file resets the batch number to 1.

Parent topic:

CSV Test Results Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=get-pat-algorithm-setting-runtime.html language=enus -->
## TOPIC 00117: Obtaining PAT Algorithm Settings at Run Time

- bundle_id: `teststand-semiconductor-module`
- source_path: `get-pat-algorithm-setting-runtime.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/get-pat-algorithm-setting-runtime.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the PartAverageTestingAlgorithmSettings property on the SetupPartAverageTestingCallbackArgs parameter of the PAT Setup entry point sequence to obtain the values of PAT algorithm settings at run time. Refer to the IPartAverageTestingAlgorithmSettings interface in the TSM Application API for more

### Obtaining PAT Algorithm Settings at Run Time

Use the PartAverageTestingAlgorithmSettings property on the
 SetupPartAverageTestingCallbackArgs
 parameter of the PAT Setup entry point sequence to obtain
 the values of PAT algorithm settings at run time. Refer to the
 IPartAverageTestingAlgorithmSettings
 interface in the TSM Application API for more
 information.

Parent topic:

Part Average Testing Algorithm Settings (TSM)

Related concepts:

- Part Average Testing Setup Entry Point (TSM)
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=get-test-information-step.html language=enus -->
## TOPIC 00118: Get Test Information Step (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `get-test-information-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/get-test-information-step.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Get Test Information step to obtain the values for lot settings, station settings, STS state, execution data, and custom test conditions. Store the value of the items in TestStand local variables so that any step in the sequence can access the values. Configuring the Step Use the Get Test In

### Get Test Information Step (TSM)

Use the Get Test Information step to obtain the values for lot settings, station settings, STS state, execution data, and custom test conditions. Store the value of the items in TestStand local variables so that any step in the sequence can access the values.

#### Configuring the
 Step

Use the Get Test Information edit tab in the TestStand Sequence
 Editor to specify the list of lot settings, station settings, STS
 state, execution data, and custom test conditions and the locations
 to store the values.

Parent topic:

TSM Step Types

Related concepts:

- Get Test Information Tab (TSM)

Related information:

- Sequence Local Variables

<!--NI_TOPIC bundle=teststand-semiconductor-module path=get-test-information-tab.html language=enus -->
## TOPIC 00119: Get Test Information Tab (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `get-test-information-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/get-test-information-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Get Test Information tab contains a table that lists the items the step accesses. Modifying the Layout and Entering Data Use the buttons located to the right of the table to add, remove, or reorder per-site inputs. You can enter data in the table in the following ways: Enter data when a cell is

### Get Test Information Tab (TSM)

The Get Test Information tab contains a table that lists the items the step accesses.

#### Modifying the Layout
 and Entering Data

Use the buttons located to the right of
 the table to add, remove, or reorder per-site inputs.

You can
 enter data in the table in the following ways:

- Enter data when a cell is highlighted.
- Click in a cell when it is highlighted.
- Double-click a cell.
- Select a value from a drop-down menu.
- Drag a variable or property from the
 Variables
 pane to a text or expression cell.

#### Columns

The
 test information table contains the following columns:

- Filter—Drop-down menu of the category types for the item you
 want to access. Select All to display
 items from all the categories. Categories include the
 following:
  - Lot and Station Settings—You can access the
 standard lot and station settings and custom
 lot and station settings you create from this
 step.
  - STS Test Head— The following table lists the STS properties you can access from this step.
 Except for the TestHeadAvailable property, these queries must be
 run only on an STS with STS Maintenance Software 19.0 or later. Name
 Type
 Description12VPowerSupplyEnabled
 Boolean
 Returns whether the 12 V pins on STS CX and STS DX systems are enabled.
 The pins are disabled by default at STS power up and when a load board is
 not installed or locked down on the STS, such as when the value of the
 DIBPresent property is False. These
 signals are available on the system cable for STS CX systems and on the P143
 system block for STS DX systems. Note You can successfully make this query
 only on STS M2 systems. Otherwise, the step returns a run-time
 error.
 48VPowerSupplyEnabled
 Boolean
 Returns whether the 48 V pins on STS CX and STS DX systems are enabled.
 The pins are disabled by default at STS power up and when a load board is
 not installed or locked down on the STS, such as when the value of the
 DIBPresent property is False. These
 signals are available on the system cable for STS CX systems and on the P143
 system block for STS DX systems. Note The step returns a run-time error if
 you make this query on STS T1 M1 systems.
 CurrentRunTime
 String
 Reads from the system controller of the STS the amount of time the STS
 has been running since the last power-on event.
 DIBLocked
 Boolean
 Returns the locked state of the DIB locker.
 DIBPresent
 Boolean
 Returns whether a load board is installed by detecting whether the load
 board shorts the DIB_INTERLOCK pin to GND. The DIB_INTERLOCK and GND signals
 are available on the system cable for STS CX systems and on the P143 system
 block for STS DX systems. Note You must design the load board to connect
 DIB_INTERLOCK to GND to activate STS DIB detection. Refer to the DIB
 Design Kit for more information about designing load boards.
 FramePartNumber
 String
 Returns the unique identifier and revision of the STS.
 FrameSerialNumber
 String
 Returns the unique serial number of the STS.
 LoadBoardIDPROM.ChecksumPassed
 Boolean
 Returns whether the checksum of the load board passed.
 LoadBoardIDPROM.DateManufactured
 String
 Returns the manufacture date of the load board.
 LoadBoardIDPROM.Description
 String
 Returns the description of the load board.
 LoadBoardIDPROM.Format
 Number
 Returns the version number of the format that describes how the raw
 data from the IDPROM is converted into IDPROM values.
 LoadBoardIDPROM.Manufacturer
 String
 Returns the manufacturer of the load board.
 LoadBoardIDPROM.PartNumber
 String
 Returns the part number of the load board. By default, TSM writes this
 property to the LoadBoardType station settings and logs the
 value to the corresponding STDF record field if
 LoadBoardIDPROM.ChecksumPassed is true. You can override
 this behavior in the GetStationSettings and
 ConfigureStationSettings callback sequences of the
 SemiconductorModuleCallbacks.seq sequence
 file.
 LoadBoardIDPROM.Revision
 Number
 Returns the revision number of the load board.
 LoadBoardIDPROM.SerialNumber
 Number
 Returns the serial number of the load board. By default, TSM writes
 this property to the LoadBoardId station settings and logs
 the value to the corresponding STDF record field if
 LoadBoardIDPROM.ChecksumPassed is true. You can override
 this behavior in the GetStationSettings and
 ConfigureStationSettings callback sequences of the
 SemiconductorModuleCallbacks.seq sequence
 file.
 SystemPartNumber
 String
 Returns the unique identifier and revision of the STS
 configuration.
 SystemSerialNumber
 String
 Returns the unique serial number of the STS configuration. Note If the
 STS does not return a serial number or the serial number is NOTSET, this
 property returns the same value as the FrameSerialNumber
 property.
 TestHeadAvailable
 Boolean
 Returns whether TSM can access the STS. The following conditions
 prevent TSM from accessing the STS: STS Maintenance Software is not installed.
 The version of STS Maintenance Software is earlier than version 19.0.
 An error occurred when trying to communicate with the STS.
 TotalRunTime
 String
 Reads from the system controller of the STS the amount of time the STS
 has run over its entire lifetime.
  - Execution Data— The following table lists the execution data properties you can access from
 this step. Name
 Type
 Description
 Access RestrictionsBinType
 Number or NI_SemiconductorModule_BinType
 Type of the bin assigned to the part tested on the current site.
 (0=Pass, 1=Fail, 2=Other)
 Test Socket Threads OnlyValid in PostUUT
 BinTypes
 Array of numbers or array of NI_SemiconductorModule_BinType
 The types of the bins assigned to each part on each site. (0=Pass,
 1=Fail, 2=Other)
 Valid in PostBatch
 CSVTestResultsLogFilePath
 String
 Returns the absolute file path of the last CSV Test Results Log
 generated for the current lot.
 Valid in MainSequence
 CSVTestResultsLogFilePaths
 Array of strings
 Returns the absolute file paths of all CSV Test Results Logs generated
 for the current lot. If the Generate One File per Wafer option is enabled,
 one path is returned for each wafer processed in the lot so far. Otherwise,
 the length of the array is 1.
 Valid in MainSequence
 DebugTestResultsLogFilePath
 String
 Returns the absolute file path of the Debug Test Results Log generated
 for the current site.
 Valid in MainSequence
 DebugTestResultsLogFilePaths
 Array of strings
 Returns the absolute file paths of the Debug Test Results Logs
 generated for all sites in the current lot.
 Controller Thread Only
 DidInlineQABlockExecute
 Boolean
 Returns true if an InlineQA step executed its block of steps for this
 site.
 Test Socket Threads OnlyValid in MainSequence
 DieCoordinateX
 Number
 Returns the X wafer coordinate of the current die being tested on this
 site. The handler/prober driver sets this property
 value by setting values in the
 WaferRuntimeData.SiteDieCoordinates parameter in the
 StartOfTest handler driver entry point sequence.
 This property corresponds to the X_COORD field in
 the Part Results Record (PRR) in the STDF log
 file.
 Test Socket Threads OnlyValid in MainSequence
 DieCoordinateY
 Number
 Returns the Y wafer coordinate of the current die being tested on this
 site. The handler/prober driver sets this property value by setting values
 in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest
 handler driver entry point sequence. This property corresponds to the
 Y_COORD field in the Part Results Record (PRR) in the STDF log file.
 Test Socket Threads OnlyValid in MainSequence
 HardwareBinName
 String
 Returns the name of the hardware bin that the tester assigned to the
 last part that was tested on this site.
 Test Socket Threads OnlyValid in PostUUT
 HardwareBinNames
 Array of Strings
 The names of the hardware bins that the tester assigned to the parts in
 the current batch.
 Valid in PostBatch
 HardwareBinNumber
 Number
 The number of the hardware bin that the tester assigned to the last
 part that was tested on this site. Returns -1 if the tester has not yet
 assigned a bin to the part or a value between 0 and 65535 if the bin was
 assigned.
 Test Socket Threads OnlyValid in PostUUT
 HardwareBinNumbers
 Array of Numbers
 The numbers of the hardware bins that the tester assigned to the parts
 in the current batch.
 Valid in PostBatch
 IsDuplicateDieCoordinates
 Boolean
 Returns true if a part with the same die coordinates as the current
 part was tested previously in the current wafer.
 Test Socket Threads OnlyValid in MainSequence
 IsDuplicatePartId
 Boolean
 Returns true if a part with the same part ID as the current part was
 tested previously in the current lot.
 Test Socket Threads OnlyValid in MainSequence
 IsRetesting
 Boolean
 Returns true if the tester is currently retesting the same parts from
 the previous batch because the operator requested a retest.
 Valid in PreBatch
 IsStartOfWafer
 Boolean
 Returns true if the current batch is the first batch of parts of a new
 wafer. This property remains true if the first batch of parts are
 retested.
 Valid in PreBatch
 LotSummaryReportFilePath
 String
 Returns the absolute file path of the last Lot Summary Report generated
 for the current lot.
 Valid in MainSequence
 LotSummaryReportFilePaths
 Array of strings
 Returns the absolute file paths of all Lot Summary Reports generated
 for the current lot. If the Generate One File per Wafer option is enabled,
 one path is returned for each wafer processed in the lot so far. Otherwise,
 the length of the array is one.
 Valid in MainSequence
 NumberOfSites
 Number
 The number of sites that are testing the current lot.
 —
 PartId
 String
 Returns the part identifier for the current part being tested on this
 site. The handler/prober driver sets this property
 value by setting values in the SitePartIds parameter
 in the StartOfTest handler driver entry point
 sequence. If the handler/prober driver does not set
 this property, the tester sets the value to a unique
 value if the GenerateUniquePartIds station settings
 is set to true. This property corresponds to the
 PART_ID field in the Part Results Record (PRR) in
 the STDF log file. When the GenerateUniquePartIds
 property is True, TSM reassigns the same unique Part
 ID to the part when it is retested. Customize the
 behavior of GenerateUniquePartIds to assign a new
 unique Part ID to a part when it is
 retested.
 Test Socket Threads OnlyValid in MainSequence
 PartText
 String
 Returns the part description text for the current part being tested on
 this site. The handler/prober driver sets this property value by setting
 values in the SitePartTexts parameter in the StartOfTest handler driver
 entry point sequence. This property corresponds to the PART_TXT field in the
 Part Results Record (PRR) in the STDF log file.
 Test Socket Threads OnlyValid in MainSequence
 SiteNumber
 Number
 Site number of the current site.
 Test Socket Threads Only
 SiteNumbers
 Array of Numbers
 The site numbers that are testing the current lot.
 —
 SiteTestTimeInSeconds
 Number
 Returns the time to execute the MainSequence sequence for the last part
 that was tested on this site.
 Test Socket Threads OnlyValid in PostUUT
 SoftwareBinName
 String
 The name of the software bin that the tester assigned to the last part
 that was tested on this site.
 Test Socket Threads OnlyValid in PostUUT
 SoftwareBinNames
 Array of Strings
 The names of the software bins that the tester assigned to the parts in
 the current batch.
 Valid in PostBatch
 SoftwareBinNumber
 Number
 The number of the software bin that the tester assigned to the last
 part that was tested on this site. Returns -1 if the tester has not yet
 assigned a bin to the part or a value between 0 and 65535 if the bin was
 assigned.
 Test Socket Threads OnlyValid in PostUUT
 SoftwareBinNumbers
 Array of Numbers
 The numbers of the software bins that the tester assigned to the parts
 in the current batch.
 Valid in PostBatch
 StdfLogFilePath
 String
 Returns the absolute file path of the last STDF log file generated for
 the current lot.
 Valid in MainSequence
 StdfLogFilePaths
 Array of strings
 Returns the absolute file paths of all STDF log files generated for the
 current lot. If the Generate One File per Wafer option is enabled, one path
 is returned for each wafer processed in the lot so far. Otherwise, the
 length of the array is one.
 Valid in MainSequence
 WaferRuntimeData.ExecDescription
 String
 Returns the wafer description supplied by exec. This property
 corresponds to the EXC_DESC field in the Wafer Results Record (WRR) in the
 STDF log file.
 Valid in PreBatch
 WaferRuntimeData.FabWaferId
 String
 Returns the fab wafer ID. This property corresponds to the FABWF_ID
 field in the Wafer Results Record (WRR) in the STDF log file.
 Valid in PreBatch
 WaferRuntimeData.FrameId
 String
 Returns the wafer frame ID. This property corresponds to the FRAME_ID
 field in the Wafer Results Record (WRR) in the STDF log file.
 Valid in PreBatch
 WaferRuntimeData.MaskId
 String
 Returns the wafer mask ID. This property corresponds to the MASK_ID
 field in the Wafer Results Record (WRR) in the STDF log file.
 Valid in PreBatch
 WaferRuntimeData.UserDescription
 String
 Returns the wafer description supplied by user. This property
 corresponds to the USR_DESC field in the Wafer Results Record (WRR) in the
 STDF log file.
 Valid in PreBatch
 WaferRuntimeData.WaferId
 String
 Returns the wafer ID. This property corresponds to the WAFER_ID field
 in the Wafer Information Record (WIR) and Wafer Results Record (WRR) in the
 STDF log file.
 Valid in PreBatch
  - Custom Test Conditions—Access the custom test
 conditions you created in the Test Program Editor.
- Name —The name of the lot setting, station
 setting, STS state, execution data, or custom test condition
 to access. You can choose one of the items from the
 drop-down menu, or you can type any part of the item name
 and select the item from the drop-down menu of
 suggestions.
- Destination Expression —An expression that
 specifies the location to copy the value. You typically
 specify a local variable that you can
 use throughout the sequence.

Parent topic:

Get Test Information Step (TSM)

Related concepts:

- Accessing Lot Settings from a Test Program (TSM)
- Accessing Station Settings from a Test Program (TSM)
- Configuration Definition Panel
- Customizing the Behavior for Obtaining Lot Settings (TSM)
- Standard Test Data Format (STDF) Log (TSM)
- Test Program Editor (TSM)

Related reference:

- STS Test Head Properties
- Execution Data Properties

Related information:

- Sequence Local Variables
- Process Model Thread Types
- Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getlotsettings-callback.html language=enus -->
## TOPIC 00120: GetLotSettings Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `getlotsettings-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getlotsettings-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM calls the GetLotSettings callback sequence to programmatically obtain lot settings without requiring much, if any, operator interaction when execution begins. You can also use the ConfigureLotWhenStartingLot option on the Semiconductor Module Manager to customize an operator interface to automat

### GetLotSettings Callback (TSM)

TSM calls the GetLotSettings callback sequence to programmatically obtain lot settings without requiring much, if any, operator interaction when execution begins. You can also use the ConfigureLotWhenStartingLot option on the Semiconductor Module Manager to customize an operator interface to automatically call the ConfigureLotSettings callback sequence at the beginning of the execution of each lot.

The default implementation of the GetLotSettings callback sequence sets the
 LotSettings.Standard.JobName and
 LotSettings.Standard.JobRevision values based on the value of
 LotSettings.Standard.MainSequenceFilePath. You can override
 this callback sequence to customize the behavior for when TSM attempts to determine
 lot settings values at run time. You can also use the ConfigureLotSettings callback sequence to prompt an operator to manually
 enter lot information in a dialog box or to use another mechanism that requires user
 input.

The GetLotSettings callback sequence accepts the following parameters:

- LotSettings [In/Out]—An instance of the NI_SemiconductorModule_LotSettings data type. Enter values for all
 the properties that you require. If you implement a mechanism for
 programmatically obtaining lot information, ensure that the mechanism
 obtains values for all the properties of the
 LotSettings parameter that you require. If the
 default properties of the LotSettings parameter do
 not meet your requirements, you can add properties to the
 NI_SemiconductorModule_CustomLotSettings data type. The properties you add
 to the data type appear in the Custom container of the
 LotSettings parameter. TSM records the lot
 setup time in the LotSettings.Standard.SetupTime property
 when the GetLotSettings callback sequence sets the
 UpdateSetupTime parameter to
 True. When you customize the
 GetLotSettings callback sequence, set the
 UpdateSetupTime parameter to
 True when the callback sequence updates the
 LotSettings parameter.
- UpdateSetupTime [Out]—Configure the
 GetLotSettings callback sequence to set this parameter to
 True when the callback sequence modifies the values of the
 LotSettings parameter. If the callback sequence does
 not modify the values of the LotSettings parameter, configure the callback
 sequence to set this parameter to False . TSM records the lot
 setup time in the LotSettings.Standard.SetupTime property
 when the GetLotSettings callback sequence sets this
 parameter to True. The value of the
 LotSettings.Standard.SetupTime property determines the
 value of the SETUP_T field in the Master Information Record (MIR) of
 version 4 of the Standard Test Data Format (STDF).

Parent topic:

Customizing the Behavior for Obtaining Lot Settings (TSM)

Related concepts:

- Customizing the Behavior for Obtaining Lot Settings (TSM)
- ConfigureLotSettings Callback (TSM)
- NI_SemiconductorModule_LotSettings Data Type

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getnextinlineqastatequeueitems-callback.html language=enus -->
## TOPIC 00121: GetNextInlineQAStateQueueItems Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `getnextinlineqastatequeueitems-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getnextinlineqastatequeueitems-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM calls the GetNextInlineQAStateQueueItems callback sequence in the inline QA algorithm sequence file specified for the test station. The GetNextInlineQAStateQueueItems callback sequence specifies a queue of inline QA states, where each state represents an enabled or disabled state that indicates

### GetNextInlineQAStateQueueItems Callback (TSM)

TSM calls the GetNextInlineQAStateQueueItems callback sequence in the inline QA algorithm sequence file
 specified for the test station.

The GetNextInlineQAStateQueueItemscallback sequence specifies a queue of inline QA states, where each state represents an enabled or disabled state that indicates whether to perform inline QA for a particular DUT. When the queue does not contain enough inline QA states for the next set of DUTs to test, TSM calls the GetNextInlineQAStateQueueItems callback sequence to obtain additional inline QA states.

The GetNextInlineQAStateQueueItems callback sequence accepts the following parameters:

- MinimumInlineQAStateQueueItemsRequired [In]—The minimum number of inline
 QA states the GetNextInlineQAStateQueueItems callback sequence must return for TSM to
 successfully perform inline QA testing. To improve
 performance, return more than the minimum number of required
 states this parameter specifies to limit the number of times
 TSM calls the GetNextInlineQAStateQueueItems callback sequence.
- LotSettings [In]—An instance of the
 NI_SemiconductorModule_LotSettings
 data type.
- StationSettings [In]—An instance of the
 NI_SemiconductorModule_StationSettings
 data type.
- NextInlineQAStateQueueItems [Out]—Array of Boolean values, where each
 Boolean value corresponds to an inline QA state. The
 GetNextInlineQAStateQueueItems 
 callback sequence must resize this array and populate it
 with the next inline QA state for the TSM queue of inline QA
 states. The number of inline QA states populated must be
 greater than or equal to the number of required inline QA
 states the
 MinimumInlineQAStateQueueItemsRequired 
 parameter specifies.

Parent topic:

Creating an Inline QA Algorithm Sequence File (TSM)

Related concepts:

- NI_SemiconductorModule_LotSettings Data Type
- NI_SemiconductorModule_StationSettings Data Type

Related tasks:

- Creating an Inline QA Algorithm Sequence File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getreportfilename-callback.html language=enus -->
## TOPIC 00122: GetReportFileName Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `getreportfilename-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getreportfilename-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The STDF Log, Lot Summary Report, CSV Test Results Log, and Debug Test Results Log result processing plug-ins determine the name of the report or data log file by calling the GetReportFileName callback sequence once for each active result processing plug-in instance. The STDF Log, CSV Test Results L

### GetReportFileName Callback (TSM)

The STDF Log, Lot Summary Report, CSV Test Results Log, and Debug Test Results
 Log result processing plug-ins determine the name of the report or data log
 file by calling the GetReportFileName callback sequence once for each active
 result processing plug-in instance. The STDF Log, CSV Test Results Log, and
 Lot Summary Report result processing plug-ins call the callback once per
 wafer when you enable the Generate One File per Wafer option. The
 GetReportFileName callback sequence is located in
 the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 or <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 file.

The GetReportFileName callback sequence accepts the following
 parameters:

- ModelPlugin [In] —An instance of the NI_ModelPlugin data type. Use the
 Parameters.ModelPlugin.Base.SequenceFileName 
 property to determine which result processing plug-in called the
 callback sequence. Possible values include the following:
  - STDF Log:
 NI_SemiconductorModule_StdfGenerator.seq
  - Lot Summary Report:
 NI_SemiconductorModule_LotSummaryReportGenerator.seq
  - Debug Test Results Log:
 NI_SemiconductorModule_TestResultsLogGenerator.seq
  - CSV Test Results Log:
 NI_SemiconductorModule_CSVTestResultsLogGenerator.seq
- ModelThreadType [In] —An instance of the NI_ModelThreadType data type. Use
 values in this container to determine whether the filename
 corresponds to a specific site or to all sites. For example, the
 STDF Log result processing plug-in creates a single file for all
 sites, and the Debug Test Results Log result processing plug-in
 calls the GetReportFileName callback once for each
 site to create a separate file for each site.
- ModelData [In] —Contains information about the
 process model used to test the current lot.
- LotSettings [In] —An instance of the NI_SemiconductorModule_LotSettings data
 type. Use values in this container to append lot settings, such as
 Standard.JobName and
 Standard.LotId , to the filename. The TSM
 result processing plug-ins call the
 GetReportFileName callback sequence after
 the ConfigureLotSettings and GetLotSettings callback sequences,
 which might have set values in this container.
- StationSettings [In] —An instance of the NI_SemiconductorModule_StationSettings
 data type. Use values in this container to append station settings,
 such as Standard.NodeName and
 Standard.TestFacilityId , to the filename.
 TSM result processing plug-ins call the
 GetReportFileName callback sequence after
 the ConfigureStationSettings and GetStationSettings callback sequences,
 which might have set values in this container.
- StartDate [In]—An instance of the DateDetails
 data type that represents the date that testing began. For the STDF
 Log and Lot Summary Report, this parameter contains the date that
 the current wafer started testing if the Generate One File per Wafer
 option is enabled. Use values in this container to append the lot
 test start date to the filename.
- StartTime [In]—An instance of the TimeDetails
 data type that represents the time that testing began. For the STDF
 Log and Lot Summary Report, this parameter contains the time that
 the current wafer started testing if the Generate One File per Wafer
 option is enabled. Use values in this container to append the lot
 test start time to the filename.
- ReportDestinationDirectory [In/Out]—Contains the
 report or data log file destination directory, which you configured
 in the related result processing plug-in Options dialog box. Change
 the value of this parameter to store the report or data log file in
 a different location.
- ReportFileName [Out]—The report or data log
 filename. TSM concatenates the values of the
 ReportDestinationDirectory and
 ReportFileName parameters to generate
 the report or data log file absolute path.

In addition to using the parameters to generate a report filename, you can use
 the TSM
 Application API in a code module the
 GetReportFilename callback sequence calls to access
 batch and site run-time data, including wafer information.

Parent topic:

Specifying Report and Data Log Filenames (TSM)

Related concepts:

- NI_SemiconductorModule_LotSettings Data Type
- ConfigureLotSettings Callback (TSM)
- GetLotSettings Callback (TSM)
- NI_SemiconductorModule_StationSettings Data Type
- Configure Station Settings Dialog Box (TSM)
- GetStationSettings Callback (TSM)
- TSM Application API

Related information:

- TestStand Directory Structure
- NI_ModelPlugin
- Process Model Thread Types

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getstationsettings-callback.html language=enus -->
## TOPIC 00123: GetStationSettings Callback (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `getstationsettings-callback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getstationsettings-callback.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM calls the GetStationSettings callback sequence to programmatically obtain station settings without requiring much, if any, test engineer or technician interaction when execution begins. The default implementation of the GetStationSettings callback sequence sets some standard station settings, su

### GetStationSettings Callback (TSM)

TSM calls the GetStationSettings callback sequence to programmatically obtain station settings without requiring much, if any, test engineer or technician interaction when execution begins.

The default implementation of the GetStationSettings callback sequence sets some
 standard station settings, such as
 Standard.HandlerType,
 Standard.NodeName, and
 Standard.TesterType. You can override this
 callback sequence to customize the behavior for when TSM
 attempts to determine station settings values at run time. You can
 also use the ConfigureStationSettings callback
 sequence to prompt a test engineer or technician to manually
 configure station settings in a dialog box or to use another
 mechanism that requires user input.

The GetStationSettings callback sequence accepts the following parameters:

- StationSettings [In/Out]—An instance of the NI_SemiconductorModule_StationSettings data type. Enter values for all the properties that you require.
 If you implement a mechanism for programmatically obtaining station information, ensure that the mechanism obtains values for all the properties of the StationSettings parameter that you require. If the default properties of the StationSettings parameter do not meet your requirements, you can add properties to the NI_SemiconductorModule_CustomStationSettings data type. The properties you add to the data type appear in the Custom container of the StationSettings parameter.

Parent topic:

Customizing the Behavior for Obtaining Station Settings (TSM)

Related concepts:

- Customizing the Behavior for Obtaining Station Settings (TSM)
- Configure Station Settings Dialog Box (TSM)
- NI_SemiconductorModule_StationSettings Data Type

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getting-started.html language=enus -->
## TOPIC 00124: Getting Started with TSM

- bundle_id: `teststand-semiconductor-module`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getting-started.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use TestStand and TSM with other NI development tools to build, debug, customize, and deploy semiconductor characterization and production test systems. Brief Tour of TSM You must have the LabVIEW Development System installed to use this example. From the TestStand Sequence Editor, open Getting Star

### Getting Started with TSM

Use TestStand and TSM with other NI development tools to build, debug, customize, and
 deploy semiconductor characterization and production test systems.

#### Brief Tour of TSM

Note

1. From the TestStand Sequence Editor, open Getting Started with Semiconductor
 Module.seq . Open the file from the <TestStand
 Public>\Examples\NI_SemiconductorModule\Getting Started with Semiconductor
 Module\LabVIEW directory. The Getting Started with
 Semiconductor Module.seq sequence file is a simple example semiconductor
 test program that demonstrates a multisite test program that uses LabVIEW code modules
 with simulated test results. The example is configured to test up to four DUTs in
 parallel, each on a separate test site.
2. Review the following TSM toolbar
 buttons to use to control execution and view lot statistics while executing and
 debugging a sequence. [IMAGE alt='image' src='GUID-A9C3EAD9-FADA-4392-BA97-F37BBEAB5F26-a5.png'] 1. Edit Test Program
8. Export Test Limits from
15. Step Over
2. Edit Pin Map File
9. Single Test
16. Step Out
3. Edit Bin Definitions File
10. Start/Resume Lot
17. Show Lot Statistics Viewer
4. Configure Station
11. Pause
18. Launch Digital Pattern Editor
5. Configure Lot
12. Retest
19. Launch InstrumentStudio
6. Active Configuration
13. End Lot
20. Enable/Disable Offline Mode
7. Import Test Limits into
14. Step Into
3. Click the Start/Resume Lot button to begin testing. Each Execution
 window represents a test site. The sequence editor traces each step during execution.
 Note Depending on the
 current sequence editor settings, when you click the Start/Resume
 Lot button, TestStand might display the Found Analysis
 Errors dialog box to indicate that errors exist in the sequence file.
 Click the Continue Execution button to ignore these errors
 because the sequence file adjusts certain settings at run time to fix these
 errors.
4. Click the Show Lot Statistics Viewer 
 button to view per-site binning
 information. The Lot Statistics Viewer window includes the same buttons as on the TSM toolbar
 for controlling execution.
5. Click the End Lot button to stop testing.
6. Close the Lot Statistics Viewer window.
7. Press <Ctrl-D> to close the Execution windows.

#### Debugging LabVIEW Steps

1. In the Getting Started with Semiconductor Module.seq , click in the
 blank column to the left of the Leakage step to set a breakpoint .
2. Click the Start/Resume Lot button to begin testing. Each
 Execution window pauses when it reaches the breakpoint at the Leakage step. The background
 color of the Execution window changes to yellow to indicate that the execution is
 paused.
3. Click the Step Into button 
 on the TSM toolbar to transfer execution to the LabVIEW Development System, which suspends
 within the Leakage VI the Leakage step calls. You can now use the built-in LabVIEW
 debugging tools.
4. In LabVIEW, click the Run button 
 and then click the Return to Caller button to return execution to the sequence editor.
5. Click the End Lot button to stop testing.

- Explore the components of a test program.
- Complete the Exploring a Basic Semiconductor Test Program with LabVIEW or .NET
 tutorial.
- Review the Accelerometer with LabVIEW or .NET example, located in the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Accelerometer 
 directory.
- Use the TestStand and TSM example programs, located in the <TestStand Public>\Examples 
 directory, as a starting point for applications you create.
- Refer to the NI STS Technical Support Community on ni.com for information about TSM
 custom instruments for instrument drivers, custom debug panels, and custom handler/prober
 drivers. You can work directly with NI services personnel contracted on your project or
 contact stssupport@ni.com to request to be added to the NI STS Technical Support
 Community.

Related concepts:

- Lot Statistics Viewer (TSM)

Related tasks:

- Tutorial: Exploring a Basic Semiconductor Test Program with LabVIEW
- Tutorial: Exploring a Basic Semiconductor Test Program with .NET
- Accelerometer with LabVIEW
- Accelerometer with .NET

Related reference:

- Semiconductor Module Toolbar Buttons
- Overview of Test Program Components

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=getting-values-for-specifications.html language=enus -->
## TOPIC 00125: Getting Values for Specifications (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `getting-values-for-specifications.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/getting-values-for-specifications.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specification files (.specs) define a set of variables and associated numeric values that you reference in code modules to configure hardware or provide input to tests procedures. Use the Get Specification(s) Value(s) VI or the GetSpecificationsValue or GetSpecificationsValues .NET methods to query

### Getting Values for Specifications (TSM)

Specification files (.specs) define a set of variables and associated numeric values that you reference in code modules to configure hardware or provide input to tests procedures. Use the Get Specification(s) Value(s) VI or the GetSpecificationsValue or GetSpecificationsValues .NET methods to query one variable or an array of variables and return the calculated value or values. The VI and methods return an error or exception when you reference a variable that does not exist in the specifications file, which can result in a run-time error when the sequence executes.

| LabVIEW |  |
| --- | --- |
| .NET (C#) | public static void ExampleCodeModule(ISemiconductorModuleContext semiconductorModuleContext, string[] pins) { NIDCPower[] dcPowerSessions; string[] channelStrings; var pinQuery = semiconductorModuleContext.GetNIDCPowerSessions(pins, out dcPowerSessions, out channelStrings); double vccMax = semiconductorModuleContext.GetSpecificationsValue("DC.vcc_max"); SetupMeasurement(dcPowerSessions, channelStrings, vccMax); var results = PerformMeasurement(dcPowerSessions, channelStrings); pinQuery.Publish(results); } |

Parent topic:

Code Module Development (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=glossary.html language=enus -->
## TOPIC 00126: Glossary

- bundle_id: `teststand-semiconductor-module`
- source_path: `glossary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/glossary.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: A active site Site that is currently testing DUTs and not disabled. B batch A set of DUTs you test simultaneously. bin definitions file Defines the hardware bins and software bins, defines how the software bins relate to hardware bins, and defines the default software bins for the test program main

### Glossary

#### A

active site

#### B

batch

bin definitions file

binning

#### C

channel

channel group

configuration

connection

custom instrument

cycle time

#### D

device

DIB

DUT

DUT pin

- A specific pin on the DUT.
- A resource on the tester or DIB that has instrument connections and
 that is associated with one or more sites. This resource can have
 one connection per site or can have one connection per group of
 sites.

#### G

Grading

#### H

handler

handler/prober index time

hardware bin

hardware configuration file

#### I

index time

inline QA

instrument

#### L

lot

#### M

multisite

#### P

part

pin

pin group

pin map

prober

PTE

#### R

result

#### S

Semiconductor Module context

site

Get Site Runtime Data

GetSiteRuntimeData

site relay

socket time

software bin

software fail bin

software pass bin

STDF

STS

subsystem

system pin

system relay

#### T

test cell

test code

test condition

test limits file

test lot

test number

test program

test program main sequence

test socket

Get Site Runtime
 Data

GetSiteRuntimeData

test station

test step

tester

tester index time

tester software

TSM

#### V

virtual pin

#### W

working site

<!--NI_TOPIC bundle=teststand-semiconductor-module path=grading-passed-duts.html language=enus -->
## TOPIC 00127: Grading Passed DUTs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `grading-passed-duts.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/grading-passed-duts.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use a Set and Lock Bin step to grade a passed DUT, in which the test program evaluates the DUT with different test criteria and assigns a pass bin to the DUT depending on the level of criteria the DUT met. Complete the following steps to implement grading in a TSM test program. Set the defau

### Grading Passed DUTs (TSM)

You can use a Set and Lock
 Bin step to grade a passed DUT, in which the test
 program evaluates the DUT with different test criteria and assigns a
 pass bin to the DUT depending on the level of criteria the DUT
 met.

Complete the following steps to implement grading in a TSM test program.

1. Set the default pass bin in the bin definitions file to the software bin associated with the lowest passing grade.
2. Insert a Semiconductor Multi Test step in the sequence and complete the following steps to configure the step to test the highest grade.
  1. On the Module tab of the Step Settings pane, specify a code module that takes a measurement to use for determining the DUT grade.
  2. On the Tests tab, add a single test and use the Export Measurement To column to specify a local variable to use for storing the measurement value, which you will use in subsequent steps.
  3. Use the Low Limit and High Limit columns to specify the limit set that determines the highest passing grade.
  4. Leave the Software Bin column empty because a failure on a high-grade test must not assign the DUT to a fail bin.
  5. Disable the Step Failure Causes Sequence Failure option on the Run Options panel of the Properties tab.
3. Insert another Semiconductor Multi Test step and complete the following steps to configure the step to test the next lower grade.
  1. On the Preconditions panel of the Properties tab, specify a precondition expression so that the step executes only if the step for the next higher grade fails. TSM does not need to perform this test if the DUT already passed a higher grade test.
  2. On the Tests tab, add a single test and use the Test Data
 Source column to specify the
 local variable in which you stored the measurement
 value in step 2b.
  3. Use the Low Limit and High Limit columns to specify the limit set that determines the passing grade.
  4. If this step does not test the lowest passing grade, leave the Software Bin column empty. Otherwise, specify the software bin to assign if the DUT fails the lowest passing grade.
  5. If this step does not test the lowest passing grade, disable the Step Failure Causes Sequence Failure option on the Run Options panel. If the step tests the lowest passing grade, enable the Step Failure Causes Sequence Failure option.
4. Repeat step 3 to add additional Semiconductor Multi Test steps and configure the steps to test each of the next lower grades until the lowest passing grade.
5. At the end of the sequence, insert a Set and Lock Bin step for each grade, starting from the second lowest to the highest, and complete the following steps to configure each Set and Lock Bin step.
  1. On the Set and Lock
 Bin tab, use the Bin
 Expression control to specify the
 software pass bin you want to associate with the
 grade.
  2. On the Preconditions panel of the Properties tab, specify a precondition expression so that the
 step executes only if the sequence passed
 ( !RunState.SequenceFailed ) and
 all the tests for the grade passed.

Parent topic:

Binning DUTs Based on Test Results (TSM)

Related concepts:

- Set and Lock Bin Step (TSM)
- Bin Definitions Editor (TSM)
- Semiconductor Multi Test Step
- Tests Tab
- Set and Lock Bin Tab (TSM)

Related information:

- Expressions

<!--NI_TOPIC bundle=teststand-semiconductor-module path=grading.html language=enus -->
## TOPIC 00128: Grading (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `grading.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/grading.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates how to use the Set and Lock Bin step to grade DUTs based on different test criteria. Example File Locations <TestStand Public> \Examples\NI_SemiconductorModule\Grading\LabVIEW\Grading.seq Highlighted Features Binning Set and Lock Bin step Major API None Prerequisites You mu

### Grading (TSM)

This example demonstrates how to use the Set and Lock Bin step to grade DUTs
 based on different test criteria.

| Example File Locations | <TestStand Public> \\Examples\\NI_SemiconductorModule\\Grading\\LabVIEW\\Grading.seq |
| --- | --- |
| Highlighted Features | Binning Set and Lock Bin step |
| Major API | None |
| Prerequisites | You must have the LabVIEW Development System installed, and you must configure the LabVIEW Adapter to use the LabVIEW Development System. This example uses the Batch process model. |

Complete the following steps to use this example.

1. Use the TestStand Sequence Editor to complete the following
 steps to review the bin definitions file associated with the
 test program.
  1. Select Semiconductor Module»Edit Bin Definitions File or click the Edit Bin
 Definitions File 
 button on the TSM toolbar.
  2. The bin definitions file defines one Fail bin,
 one Error bin, and three Pass bins. The Pass bins
 correspond to the following three different
 grades: Good, Better, and Best.
2. Review the three Semiconductor Multi
 Test steps in the MainSequence sequence.
  1. The first step takes and stores the measurement in a local variable
 ( Locals.Measurement ).
  2. Each step compares the measurement against a different set of limits.
  3. Preconditions on the lower grade tests prevent those tests from running if the DUT
 passed a higher grade test.
  4. The Step Failure Option on the higher grade tests ensure that the DUT does not fail
 if the higher grade tests fail.
3. Review the If block at the end of the
 MainSequence sequence.
  1. The steps in the block execute only if the DUT
 passed all tests.
  2. The Set and Lock Bin steps assign a bin to the
 DUT based on the highest grade test that
 passed.
4. Click the Start Lot 
 button on the TSM toolbar to run the test program.

Parent topic:

TSM Example Programs

Related concepts:

- Binning DUTs Based on Test Results (TSM)
- Set and Lock Bin Step (TSM)
- Semiconductor Multi Test Step

Related information:

- TestStand Directory Structure
- Batch Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=group-channels-with-dcpower.html language=enus -->
## TOPIC 00129: Grouping Channels with the NI-DCPower Driver

- bundle_id: `teststand-semiconductor-module`
- source_path: `group-channels-with-dcpower.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/group-channels-with-dcpower.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, when you create a new NI-DCPower instrument in the pin map file, TSM 2020 and later will create a single channel group containing all instrument channels. TSM creates a single session for each channel group of NI-DCPower instruments in the pin map file. TSM 2019 and earlier do not allow

### Grouping Channels with the NI-DCPower Driver

By default, when you create a new NI-DCPower instrument in the pin map file, TSM 2020 and later
 will create a single channel group containing all instrument channels. TSM creates a single session for each
 channel group of NI-DCPower instruments in the pin map file. TSM 2019 and earlier do not allow
 for channel grouping and pin maps created with older versions of TSM do not contain channel group information.
 Complete the following steps to convert all NI-DCPower instruments in the pin map to use channel groups:

1. Open the Pin Map Editor.
2. Select the NI-DCPower instrument in the Instruments section on the Pin Map tab.
3. Click the Convert NI-DCPower Instruments button.
4. Click Yes in the Convert all NI-DCPower Instruments dialog box to complete the conversion.

Note

- To use NI-DCPower channel groups you will need the correct combination of
 TSM 2020 and NI-DCPower Driver 2020. Both the driver and TSM are fully
 backwards compatible but the methods used and VI calls made by TSM and the
 driver must be changed when channel groups are used.
- TSM does not allow a combination of NI-DCPower instruments with channel
 groups and NI-DCPower instruments without channel groups.

Parent topic:

Grouping Instruments or Channels (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=group-instruments-with-digital.html language=enus -->
## TOPIC 00130: Grouping Instruments with NI-Digital Pattern Driver

- bundle_id: `teststand-semiconductor-module`
- source_path: `group-instruments-with-digital.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/group-instruments-with-digital.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, when you create a new NI-Digital Pattern instrument in the pin map file, the NI TestStand 2019 Semiconductor Module (TSM) and later set the group attribute to Digital so that all newly created NI-Digital Pattern instruments belong to the same group. TSM creates a single session for each

### Grouping Instruments with NI-Digital Pattern Driver

By default, when you create a new NI-Digital Pattern instrument in the pin map file, the NI
 TestStand 2019 Semiconductor Module (TSM) and later set the group
 attribute to Digital so that all newly created
 NI-Digital Pattern instruments belong to the same group. TSM creates a single
 session for each group of NI-Digital Pattern instruments in the pin map file. TSM
 2017 and earlier do not automatically group NI-Digital Pattern instruments together
 in pin map files. Use the Pin Map Editor to modify
 existing pin map files to change the value of the Group
 option for each instrument to assign the instrument to the same group.

Parent topic:

Grouping Instruments or Channels (TSM)

Related concepts:

- Pin Map Editor (TSM)

Related reference:

- Pin Map File XML Structure (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=group-instruments-with-scope.html language=enus -->
## TOPIC 00131: Grouping Instruments with NI-SCOPE Driver

- bundle_id: `teststand-semiconductor-module`
- source_path: `group-instruments-with-scope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/group-instruments-with-scope.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, when you create a new NI-SCOPE instrument in the pin map file, the TSM 2019 and later set the group attribute to Scope so that all newly created NI-SCOPE instruments belong to the same group. TSM creates a single session for each group of NI-SCOPE instruments in the pin map file. TSM 201

### Grouping Instruments with NI-SCOPE Driver

By default, when you create a new NI-SCOPE instrument in the pin map file, the TSM 2019 and later
 set the group attribute to
 Scope so that all newly created NI-SCOPE
 instruments belong to the same group. TSM creates a single session
 for each group of NI-SCOPE instruments in the pin map file. TSM 2017
 and earlier do not automatically group NI-SCOPE instruments together
 in pin map files. Use the Pin Map
 Editor to modify existing pin map files to change the
 value of the Group option for each instrument
 to assign the instrument to the same group.

Parent topic:

Grouping Instruments or Channels (TSM)

Related concepts:

- Pin Map Editor (TSM)

Related reference:

- Pin Map File XML Structure (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=grouping-instruments-or-channels.html language=enus -->
## TOPIC 00132: Grouping Instruments or Channels (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `grouping-instruments-or-channels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/grouping-instruments-or-channels.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can group certain instruments or channels together and treat them as a single entity. When all the instruments of the same type belong to a single group or when the instruments of the same type in a subsystem belong to a single group, you can use the versions of the pin query VIs and .NET method

### Grouping Instruments or Channels (TSM)

You can group certain instruments or channels together and treat them as a single entity. When
 all the instruments of the same type belong to a single group or when the
 instruments of the same type in a subsystem
 belong to a single group, you can use the versions of the pin query VIs and .NET
 methods that return a single session and you do not need to use parallel For Loops
 to iterate over the instrument driver sessions. The instrument driver specific to
 the grouped instruments performs most operations on all channels in parallel to
 achieve improved multisite efficiency. Refer to the instrument driver help for
 information about hardware limitations that prevent certain instruments from
 operating together as a single instrument.

Parent topic:

Code Module Development (TSM)

Related concepts:

- Subsystems and Pin Maps (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=handler-driver-captures-start-notifications.html language=enus -->
## TOPIC 00133: Ensuring That a Handler or Prober Driver Captures All Start-of-Test Notifications (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `handler-driver-captures-start-notifications.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/handler-driver-captures-start-notifications.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A handler or prober driver coordinates a connected computer with the tester by using the driver entry point sequences to wait for a start-of-test (SOT) signal before beginning a test. Missing an SOT signal might cause the tester to wait indefinitely. To ensure that a driver captures each SOT signal,

### Ensuring That a Handler or Prober Driver Captures All Start-of-Test Notifications (TSM)

A handler or prober driver coordinates a connected computer with the tester by using the driver entry point sequences to wait
 for a start-of-test (SOT) signal before beginning a test. Missing an
 SOT signal might cause the tester to wait indefinitely.

To ensure that a driver captures each SOT signal, the instrument communicating with the handler
 or prober must be armed for capturing the SOT signal before sending
 the end-of-test (EOT) signal. The handler or prober driver can
 capture the SOT signal if it occurs when the tester performs tasks
 during the tester index time or continue waiting until the SOT
 signal arrives.

Implement the following functionality in the driver entry points to ensure that the handler or prober driver captures all SOT signals:

| Entry Point | Functionality to Implement |
| --- | --- |
| Setup | Open instrument sessions with which the handler or prober communicates. Configure the instrument with any armed triggers or monitoring ports for capturing the SOT signal. Query for any machine or lot information. Send any initialization routine to the handler or prober, such as load first wafer. |
| StartOfTest | Determine whether the SOT signal was received. Continue monitoring for an end-of-lot (EOL) signal while waiting for the SOT signal. Check until the trigger arrives or the tester sends an EOL signal. |
| EndOfTest | Reconfigure the instrument to capture the next SOT signal. Send the EOT signal, including any test results. |
| Cleanup | Send a signal to stop the handler or prober. Close instrument sessions. |

Parent topic:

Creating a Handler/Prober Driver Sequence File (TSM)

Related concepts:

- Handler/Prober Driver Entry Points (TSM)
- Setup Handler/Prober Driver Entry Point (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)
- EndOfTest Handler/Prober Driver Entry Point (TSM)
- Cleanup Handler/Prober Driver Entry Point (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=handler-prober-driver-entry-points.html language=enus -->
## TOPIC 00134: Handler/Prober Driver Entry Points (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `handler-prober-driver-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/handler-prober-driver-entry-points.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM invokes a handler/prober driver by calling the following set of required entry point sequences, which specify a predefined set of parameters, at specific points during an execution: Configure—Provides a mechanism for end users to configure the handler/prober driver. Setup—Performs required handl

### Handler/Prober Driver Entry Points (TSM)

TSM invokes a handler/prober driver by calling the following set of required entry point sequences, which specify a predefined set of parameters, at specific points during an execution:

- Configure—Provides a
 mechanism for end users to configure the handler/prober
 driver.
- Setup—Performs
 required handler or prober initialization tasks.
- StartOfTest—Determines when the handler or prober
 has placed untested DUTs in test sites by waiting for the
 handler start-of-test notification.
- EndOfTest—Sends the
 end-of-test notification to the handler or prober to move
 DUTs from test sites to hardware bins.
- Cleanup—Performs
 required handler or prober finalization tasks.

Parent topic:

Creating a Handler/Prober Driver Sequence File (TSM)

Related concepts:

- Configure Handler/Prober Driver Entry Point (TSM)
- Setup Handler/Prober Driver Entry Point (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)
- EndOfTest Handler/Prober Driver Entry Point (TSM)
- Cleanup Handler/Prober Driver Entry Point (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=handler-prober-driver-sequence-file.html language=enus -->
## TOPIC 00135: Creating a Handler/Prober Driver Sequence File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `handler-prober-driver-sequence-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/handler-prober-driver-sequence-file.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the HandlerProberDriver.seq file, located in the <TestStand>\Components\Modules\NI_SemiconductorModule\Templates directory, as a starting point for a handler/prober driver sequence file you create. Copy the HandlerProberDriver.seq file from the <TestStand>\Compone

### Creating a Handler/Prober Driver Sequence File (TSM)

Complete the following steps to use the HandlerProberDriver.seq file,
 located in the <TestStand>\Components\Modules\NI_SemiconductorModule\Templates
 directory, as a starting point for a handler/prober driver sequence
 file you create.

1. Copy the HandlerProberDriver.seq file from the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates 
 directory to the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\HandlersAndProbers 
 directory. Note Create the <TestStand
 Public>\Components\Modules\NI_SemiconductorModule\HandlersAndProbers
 directory if it does not already exist.
2. Rename the <TestStand
 Public> \Components\Modules\NI_SemiconductorModule\HandlersAndProbers\HandlerProberDriver.seq 
 file using the
 <CompanyName> _ <HandlerOrProberName> .seq
 convention.
3. Open the handler/prober driver sequence file.
4. Modify each of the handler/prober driver entry point sequences
 to meet the requirements of the test system. A
 handler/prober driver sequence file must contain each
 handler/prober driver entry point except Configure. You can
 leave an entry point empty if you do not want the entry
 point to perform any functionality.
5. Save the handler/prober driver sequence file.

Parent topic:

Configuring Handler or Prober Support for a Test Program (TSM)

Related concepts:

- Handler/Prober Driver Entry Points (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=handler-prober-modes.html language=enus -->
## TOPIC 00136: Handler/Prober Modes (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `handler-prober-modes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/handler-prober-modes.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: TSM stores the handler/prober modes as one of the following numeric values for the Standard.HandlerMode property of the station settings.Numeric ValueDescription0Specifies no handler or prober interaction.1Specifies to use the NI Built-in Simulated Handler Driver to interact with dialog boxes to sim

### Handler/Prober Modes (TSM)

Standard.HandlerMode

| Numeric Value | Description |
| --- | --- |
| 0 | Specifies no handler or prober interaction. |
| 1 | Specifies to use the NI Built-in Simulated Handler Driver to interact with dialog boxes to simulate the behavior of a handler and to view the test results. |
| 2 | Specifies to use a real or simulated handler/prober driver other than the NI Built-in Simulated Handler Driver. |

Parent topic:

Configuring Handler or Prober Support for a Test Program (TSM)

Related concepts:

- Specifying Settings for the Current Test Station (TSM)
- NI Built-in Simulated Handler Driver (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=handling-errors-in-operator-interfaces.html language=enus -->
## TOPIC 00137: Handling Errors in Operator Interfaces (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `handling-errors-in-operator-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/handling-errors-in-operator-interfaces.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure TSM operator interfaces to write a message to an error log file when any run-time error is raised and execute the behavior you specify in the SemiconductorModuleManager when a code module run-time error is raised. To specify how TSM treats run-time errors in TSM Operator interfaces

### Handling Errors in Operator Interfaces (TSM)

You can configure TSM operator interfaces to write a message to an error log file when any run-time error is raised and execute the behavior you specify in the SemiconductorModuleManager when a code module run-time error is raised.

To specify how TSM treats run-time errors in TSM Operator interfaces, complete the following steps:

1. Select Configure»Station Options to launch the Station Options dialog
 box.
2. Select Show Dialog Box from the On Run-Time Error drop-down menu.
3. Click OK .
4. Optional. Use the following TSM Application API property and event to customize error handling for the operator interface:
  - ErrorLogFilePath —Specifies the location of the error log
 file. The default setting for this property is
 <TestStand
 Public> \ErrorLogs\NI_SemiconductorModule\OperatorInterfaceErrors.log
  - ErrorOccurred event—Generated when any error occurs.

Code module run-time errors are a class of run-time errors. A *code module run-time*
 error is raised when the
 MainSequence sequence
 returns a run-time error from a source other than TSM, such as a
 code module or an instrument driver.

To specify how TSM treats code module run-time errors in TSM Operator interfaces, set the following TSM Application API properties on the SemiconductorModuleManager object in the operator interface source code:

- EndLotOnCodeModuleRuntimeError —Determines whether testing ends immediately after the MainSequence sequence returns a code module run-time error. The default setting for this property is False .
- DisplayDialogOnCodeModuleRuntimeError —Determines whether the operator interface displays the run-time error dialog box when the MainSequence sequence returns a code module run-time error. The default setting for this property is False .

Note

Parent topic:

Operator Interfaces (TSM)

Related concepts:

- TSM Application API

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=high-level-classes.html language=enus -->
## TOPIC 00138: High-Level Classes (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `high-level-classes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/high-level-classes.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TSM LabVIEW operator interface uses the following high-level class to hold data the operator interface uses and to make customization easier. Operator Interface State—Holds references and keeps track of state information for the execution of the operator interface, including the following exampl

### High-Level Classes (TSM)

The TSM LabVIEW operator interface uses the following high-level class to hold data the operator interface uses and to make customization easier.

- Operator Interface State —Holds references and keeps track of state information for the execution of the operator interface, including the following examples:
  - An array of references to the controls on the front panel
  - A reference to events that command buttons generate and that the event structure in the main execution loop of the Top-Level VI handles
  - TestStand manager controls
  - TestStand Engine
  - Custom events that notify the main execution thread of changes
  - A reference to the Semiconductor Module Manager object, a component of the TSM Application API that manages most of test execution

Parent topic:

LabVIEW Operator Interface Architecture (TSM)

Related concepts:

- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=hsdio-hardware-compare.html language=enus -->
## TOPIC 00139: Functional Test Using NI-HSDIO Hardware Compare (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `hsdio-hardware-compare.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/hsdio-hardware-compare.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to use the NI-HSDIO hardware compare engine for a multisite functional test. This example includes the following main tasks: Query for the sessions for the digital I/O pins under test. Use a parallel For Loop to iterate on every required instrument to start digital har

### Functional Test Using NI-HSDIO Hardware Compare (TSM)

The following figure shows how to use the NI-HSDIO hardware compare engine for a multisite functional test.

[IMAGE alt='image' src='GUID-9FC564CB-995F-4DB6-A549-FD0B0AC01A7D-a5.png']

This example includes the following main tasks:

1. Query for the sessions for the digital I/O pins under test.
2. Use a parallel For Loop to iterate on every required instrument to start digital hardware compare and to obtain the cumulative error masks.
3. Use the Pin Query Context to obtain the digital per-instrument, per-site channel masks.
4. Compare the per-instrument error masks to the per-site, per-instruments masks to identify sites that failed.
5. Query for measurement data for sites that failed. The source code for the query is in the Failure Pin Site Data VI.
6. Use the Publish Data VI to publish per-site Boolean results.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following test, which evaluates one Boolean result, as
 shown in the following figure:

[IMAGE alt='image' src='GUID-1EAC7BF0-5CE9-466E-8EE8-7F1525D0BCC1-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=import-test-limits.html language=enus -->
## TOPIC 00140: Importing Test Limits from Text Files (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `import-test-limits.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/import-test-limits.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor ModuleImport Test Limits into <filename> to import test limits from a tab-delimited test limits text file into all test steps in a sequence file at edit time. When you import test limits from a text file, you can replace only the tests defined in the test limits file or you can

### Importing Test Limits from Text Files (TSM)

Select Semiconductor Module»Import Test Limits into
 <filename> to import test limits from a tab-delimited test limits text file
 into all test
 steps in a sequence file at edit time. When you import test limits from a
 text file, you can replace only the tests defined in the test limits file or you can
 delete all the tests in the sequence file and recreate each test from the contents
 of the test limits file.

The Import/Export Test Limits tool uses the SequenceName, StepName, and StepId columns in the test
 limits file to match tests in the sequence file. When you update the limits in matching tests from the test
 limits file, the tool also uses the TestNumber column to identify the test. If one of these identifier columns
 does not exist in the test limits file, the tool imports data into any step or test that matches the remaining
 identifiers and a row in the test limits file might update multiple locations in the sequence
 file. If more than one location in the sequence file matches the identifiers in a row in the test limits file,
 TSM imports data from that row into all the matching locations.

When you assign a base test limits file for a test program, importing a test limits
 file will automatically merge the values of the base file, overriding or inheriting
 values accordingly. TSM imports the merged values.

The Import/Export Test Limits tool returns an error and fails to import a test limits file if:

- A row in the test limits file does not match any location in the sequence file.
- A single test in the sequence file matches more than one row in the test limits file.
- A location in the sequence file does not match any row in the test limits file and the Require every
 step to be in test limits file option is enabled.
- A row in the test limits file matches a Semiconductor Sequence Call step in the sequence file and the Test
 Data Source column contains a value.
- There is a base test limits file assigned for the test program, and the base
 test limits file contains any <inherit> 
 values.
- There is a base test limits file assigned for the test program, and the test
 limits file being imported has a unique test with one or more
 <inherit> values, but that unique test is not
 found in the base file.

The Import Test Limits into Sequence File dialog box contains the following options:

- Update limits in matching tests —Finds any test in the sequence file that matches the
 SequenceName, StepName, StepId, and TestNumber identifier columns in the test limits file and sets the
 property values in the sequence file to the corresponding values in the test limits file. If one of these
 identifier columns other than TestNumber does not exist in the test limits file, the tool sets the
 corresponding property values for any step that matches the remaining identifiers.
 
 Note You cannot change the test number for tests in the sequence
 file when you select this mode. You must use the Replace all tests in matching
 steps option if you want to change the test number. 

 The tool modifies only the tests and properties that exist in the test limits file. Tests and properties
 defined in the sequence file but not in the test limits file remain in the sequence file unchanged.
 
 Select this option when you want to set only certain test properties at run time.
- Replace all tests in matching steps —Deletes all the tests that correspond to steps in
 the test limits file and recreates each test from the contents of the test limits file by adding tests to
 any step that matches the SequenceName, StepName, and StepId identifier columns in the test limits file. If
 one of these identifier columns does not exist in the test limits file, the tool adds a test to any step
 that matches the remaining identifiers. For columns that do not exist in the test limits file, the tool sets
 the corresponding property to the default value in the sequence file. The test limits file must include the
 columns in which you use non-default values; otherwise, the tool uses default values for those properties in
 the sequence file. If any step in the test limits file has a value of No
 Tests for the Test Number, the tool deletes all tests for any matching steps.
 
 Note Use the Semiconductor Action
 step instead of the Semiconductor Multi Test step if the step
 does not contain any tests. 

 Select this option when you want to use limit files with different numbers of tests. For example, you might
 want to include more tests in a normal testing mode than you include in a QA testing mode.
- Require every step to be in test limits file —Returns an error and does not import the
 file if a test or step exists in the sequence but does not exist in the limits file. If you do not enable
 this option, the Import/Export Test Limits tool returns a warning and imports only matching tests or steps
 in the limits file.

Parent topic:

Exporting and Importing Test Limits with Text Files

Related concepts:

- Test Steps and Flow (TSM)

Related information:

- Test Limits Text File Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=initializing-switch-sessions.html language=enus -->
## TOPIC 00141: Initializing Switch Sessions (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `initializing-switch-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/initializing-switch-sessions.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the ProcessSetup callback sequence of a test program, you must initialize all instrument sessions and switch sessions and store them in the Semiconductor Module context. Refer to the Add Switch Sessions VI in the Switching example for an example of how to initialize a set of switch sessions. Pass

### Initializing Switch Sessions (TSM)

In the ProcessSetup callback sequence of a test program, you must initialize all
 instrument sessions and switch sessions and store them in the
 Semiconductor Module context. Refer to the Add Switch Sessions VI in
 the Switching example for an example of how
 to initialize a set of switch sessions.

Pass NISimulatedMultiplexer for the Multiplexer Type ID parameter of the Get All Switch Names VI to obtain an array of switch instrument names from the pin map. In a For Loop, iterate through each name in the Switches Names array and create a session for each switch instrument. In the same For Loop, use the Set Switch Session VI to associate a switch name with a switch session in the Semiconductor Module context.

Parent topic:

Switching (TSM)

Related tasks:

- Switching (TSM)
- Switch Executive (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=inline-qa-test-block-step.html language=enus -->
## TOPIC 00142: Inline QA Test Block Step (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `inline-qa-test-block-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/inline-qa-test-block-step.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Inline QA Test Block step to insert in the MainSequence sequence of the test program main sequence file a block of Inline QA Test Block and End steps, in which you can insert additional steps that call code modules that perform the inline QA tests. The steps within the block execute only whe

### Inline QA Test Block Step (TSM)

Use the Inline QA Test Block step to insert in the MainSequence sequence of the test program main sequence file a block of Inline QA Test Block and End steps, in which you can insert additional steps that call code modules that perform the inline QA tests. The steps within the block execute only when all of the following conditions are true:

- The StationSettings.Standard.InlineQAEnabled Boolean property is
 True .
- The Step.ConditionExpr property of the Inline QA Test Block step specifies an expression that evaluates to True .
- The next inline QA state, which is the next Boolean value removed from the TSM queue of inline QA states, is True .

Note

- If multiple inline QA test blocks exist in the sequence,
 only the first one that executes dequeues the inline
 QA state for the DUT. Subsequent inline QA test
 blocks use the inline QA state that the first inline
 QA test block dequeued.
- The default expression for the
 Step.ConditionExpr 
 property evaluates to
 True when the
 MainSequence 
 sequence has not yet encountered a sequence failure.
 You can modify the expression the
 Step.ConditionExpr 
 property specifies to customize the condition for
 which the inline QA test block executes.
- You can place multiple Inline QA Test Block step type
 instances at any location in any test sequence, but
 NI recommends that you place only a single instance
 after all standard test steps in the
 MainSequence 
 sequence of the test program main sequence
 file.

Parent topic:

TSM Step Types

Related concepts:

- Performing Inline Quality Assurance Testing (TSM)
- Accessing Station Settings from a Test Program (TSM)

Related information:

- Expressions

<!--NI_TOPIC bundle=teststand-semiconductor-module path=input-parameters.html language=enus -->
## TOPIC 00143: Input Parameters (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `input-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/input-parameters.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Parameter Table of the Module tab to pass the same parameter values for all sites from the sequence file directly into a code module. In some cases, you might want to use different values for each site, such as setting different register values when trimming or using different calibration va

### Input Parameters (TSM)

Use the Parameter Table of the Module tab to pass
 the same parameter values for all sites from the sequence file
 directly into a code module.

In some cases, you might want to use different values for each site, such as setting different
 register values when trimming or using different calibration values
 for each site. Use the Per-Site Inputs tab of the Semiconductor Multi Test or the Semiconductor Action step to specify
 different parameter values within each test sequence for each site.
 Use the Get Input Data VI or the
 GetInputDataAsBooleans,
 GetInputDataAsDoubles, or
 GetInputDataAsStrings .NET methods in a
 code module to obtain the appropriate values for each site. These
 VIs and .NET methods return an array of values—one for each site
 that is part of the subsystem calling the code module.

| LabVIEW |  |
| --- | --- |
| .NET (C#) | public static void ExampleCodeModule (ISemiconductorModuleContext semiconductorModuleContext) { var serialNumbers = semiconductorModuleContext.GetInputDataAsStrings(inputDataId: "DUT Serial Number"); Parallel.For(0, waveformInputData.Length, i => { WriteSerialNumber(serialNumbers[i]); }); } |

Parent topic:

Code Module Development (TSM)

Related concepts:

- Semiconductor Multi Test Per-Site Inputs Tab
- Semiconductor Multi Test Step
- Semiconductor Action Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=insert-dtr-after-test-record.html language=enus -->
## TOPIC 00144: Inserting a DTR after a Test Record

- bundle_id: `teststand-semiconductor-module`
- source_path: `insert-dtr-after-test-record.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/insert-dtr-after-test-record.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Additional Results edit tab to add an additional result to the step with the name "NI.STDF.DTR" to insert a DTR after all Parametric Test Records (PTR) or Functional Test Records (FTR) associated with the step. Set the Value to Log option for the additional result to the value to store in th

### Inserting a DTR after a Test Record

Use the Additional Results edit tab to add an additional result to the step with the name "NI.STDF.DTR" to insert a DTR after all Parametric Test Records (PTR) or Functional Test Records (FTR) associated with the step. Set the Value to Log option for the additional result to the value to store in the TEXT_DAT field of the DTR. The STDF Log result processor inserts a DTR into the STDF log file for each additional result with the name NI.STDF.DTR on steps in the main sequence. If the text in the Value to Log option is longer than 255 characters, the STDF Log result processor splits the text into character groups that are 255 characters or less and inserts a DTR for each group.

Note

Parent topic:

Adding DTRs to the STDF Log File (TSM)

Related tasks:

- Inserting a DTR between Parts

<!--NI_TOPIC bundle=teststand-semiconductor-module path=inserting-a-dtr-between-parts.html language=enus -->
## TOPIC 00145: Inserting a DTR between Parts

- bundle_id: `teststand-semiconductor-module`
- source_path: `inserting-a-dtr-between-parts.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/inserting-a-dtr-between-parts.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You must call a method on the StdfResultProcessor class defined in the TSM assembly (NationalInstruments.TestStand.SemiconductorModule) to insert a DTR at locations other than between test records. Complete the following steps to call the CreateDtr method to insert a DTR in the STDF log file. Create

### Inserting a DTR between Parts

You must call a method on the StdfResultProcessor class defined in the TSM assembly (NationalInstruments.TestStand.SemiconductorModule) to insert a DTR at locations other than between test records. Complete the following steps to call the CreateDtr method to insert a DTR in the STDF log file.

1. Create a .NET Action step in the sequence.
2. Complete the following steps on the Module tab:
  1. Set the Assembly option to NationalInstruments.TestStand.SemiconductorModule.dll .
  2. Set the Root Class option to NationalInstruments.TestStand.SemiconductorModule.StdfResultProcessor .
  3. Set the .NET Invocation option to StdfResultProcessorSingleton.CreateDtr(System.String) .
  4. In the Parameters Table, use the Value column for the text parameter to insert the text to add to the TEXT_DAT field of the DTR. If the text in the Value column is longer than 255 characters, the STDF Log result processor splits the text into character groups that are 255 characters or less and inserts a DTR for each group.

You can add DTRs using callback sequences in the test
 program sequence file or by creating a custom result processor model
 plug-in. The actual implementation differs depending
 on whether you are performing wafer testing and whether you enable
 the Generate One File per Wafer option. In both cases, the custom
 result processor must not attempt to create DTRs if the STDF Log
 result processor is disabled. Confirm whether the STDF Log result
 processor is disabled at run-time and disable the custom result
 processor in the Model Plugin - Initialize entry point.

Parent topic:

Adding DTRs to the STDF Log File (TSM)

Related information:

- Callback Sequences
- Creating Process Model Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=install-tsm.html language=enus -->
## TOPIC 00146: Installation Instructions

- bundle_id: `teststand-semiconductor-module`
- source_path: `install-tsm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/install-tsm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Download the TestStand Semiconductor Module installer from ni.com/downloads. NI software includes NI Package Manager to handle the installation. After installing your software, you will need to activate it. Activating your software verifies the licenses associated with your NI account, so you can st

### Installation Instructions

TestStand Semiconductor Module

NI Package Manager

After installing your software, you will need to activate
 it. Activating your software verifies the licenses associated with your NI account,
 so you can start using your software. You have different options for activation,
 based on your software and how it was purchased. Please visit ni.com/activate for
 more information on activation methods.

If Windows Update is enabled, the
 installation process might hang if Windows Update interferes with the installation
 of Microsoft Visual C++ 2015 Run-Time. Visit ni.com/r/exjq43 for more information
 and steps to resolve this issue.

If you purchased this product with an NI
 Software Suite or NI Product Bundle, use the installation method of the Suite or
 Bundle.

The TestStand Semiconductor Module installation program installs files
 for TestStand and LabVIEW, including the LabVIEW 2020 Run-Time Engine.

Note

- TestStand 2023 Semiconductor Module 2024 Q1 installs
 SeqEdit.exe.config in the
 <TestStand>\Bin directory and overwrites any
 existing file with the same filename in that directory. If you have created
 a custom SeqEdit.exe.config file, complete the
 following steps to preserve the custom file.
  1. Move the existing SeqEdit.exe.config file to a
 location outside the <TestStand> 
 directory.
  2. Install TestStand 2023 Semiconductor Module 2024 Q1 .
  3. Compare the SeqEdit.exe.config file
 TestStand 2023 Semiconductor Module 2024 Q1 installed
 to the custom version of the file and merge the custom changes into
 the file TestStand 2023 Semiconductor Module 2024 Q1 
 installed.
- If you are installing more than one NI product, visit ni.com/r/tsminstall 
 for information about installation order. If you install or update LabVIEW
 after you install TestStand or TestStand Semiconductor Module ,
 close and restart TestStand or run the TestStand Version Selector 
 to properly configure LabVIEW, TestStand, and TestStand Semiconductor
 Module .
- NI recommends that you exit all programs before running the TestStand
 Semiconductor Module installer. Applications that run in the
 background, such as virus scanning utilities, might cause the installer to
 take longer than necessary to complete.
- Visit ni.com/support and enter the Info Code rddrau to
 access the latest software drivers and updates.

Related concepts:

- TestStand Semiconductor Module Licensing Options

Related information:

- Software and Driver Downloads
- Installing, Updating, Repairing, and Removing NI
 Software
- License Setup and Activation
- NI Installer Hangs While Installing Visual C++ 2015
 Run-Time
- Installation Order for Multiple NI Software Products

<!--NI_TOPIC bundle=teststand-semiconductor-module path=installer-settings-for-deploying.html language=enus -->
## TOPIC 00147: Installer Settings for Deploying TSM Test Programs

- bundle_id: `teststand-semiconductor-module`
- source_path: `installer-settings-for-deploying.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/installer-settings-for-deploying.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following recommended settings to create a simple installer with the deployment utility: Use the Deployment Version option on the Mode tab of the deployment utility to specify a version for the distribution. Increment the version with each release of the test program distribution. Do not ena

### Installer Settings for Deploying TSM Test Programs

Use the following recommended settings to create a simple installer with the deployment utility:

- Use the Deployment Version option on the Mode tab of the deployment utility to specify a version for the distribution. Increment the version with each release of the test program distribution.
- Do not enable the Install TestStand Runtime option or include any software in the Drivers and Components dialog box. Do not use the test program deployment to control the software installed on a semiconductor test station.
- Enable the Do not Ask User for Installation Directory option on the Installer Options tab of the deployment utility and set the Default Installation Directory option to install the test program in the same location on all test stations.

After you create a deployment, save the deployment specification file (.tsd) so you can use the same configuration to build newer versions of the installer or to create patches. Additionally, on the Build Status tab of the deployment utility, save the deployment build status log files to use to troubleshoot issues.

Parent topic:

Deploying TSM Test Programs

<!--NI_TOPIC bundle=teststand-semiconductor-module path=instrument-multiplexed-across-sites-multimeas.html language=enus -->
## TOPIC 00148: Instrument Multiplexed Across Sites, Multiple Measurements (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `instrument-multiplexed-across-sites-multimeas.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/instrument-multiplexed-across-sites-multimeas.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to take multiple measurements using an instrument multiplexed across multiple sites. Run-time site order is not guaranteed to be in any particular order. Site order depends on the arrival order at the executing step. This example includes the following main tasks: Quer

### Instrument Multiplexed Across Sites, Multiple Measurements (TSM)

The following figure shows how to take multiple measurements using an instrument
 multiplexed across multiple sites.

Note

[IMAGE alt='image' src='GUID-99B400C1-80A5-4AF2-A18E-699A0CC4A14A-a5.png']

This example includes the following main tasks:

1. Query the multiplexer sessions and routes for the multiplexed pin.
2. Use a For Loop to complete the following tasks for each multiplexed site:
  1. Connect the required multiplexer route for the site under test.
  2. Use the Semiconductor Module context created for each site to query for the instrument session for the pin.
  3. Use a For Loop to complete the following tasks for each measurement condition:
    1. Take a measurement for a single site and a single condition.
    2. Use the Pin Query Context and the unique Published Data Id with a pin-based instance of the Publish Data VI to publish the measurement.
  4. Disconnect the multiplexer route.
  5. Close the single site Semiconductor Module context.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following tests, where each test evaluates one
 measurement for each measurement condition, as shown in the
 following figure:

[IMAGE alt='image' src='GUID-8E6622C6-F162-4504-9DD5-F3A534E04C2B-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=instrument-multiplexed-across-sites.html language=enus -->
## TOPIC 00149: Instrument Multiplexed Across Sites (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `instrument-multiplexed-across-sites.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/instrument-multiplexed-across-sites.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to take a measurement using an instrument connected to multiple sites through a multiplexer. Run-time site order is not guaranteed to be in any particular order. Site order depends on the arrival order at the executing step. This example includes the following main tas

### Instrument Multiplexed Across Sites (TSM)

The following figure shows how to take a measurement using an instrument
 connected to multiple sites through a multiplexer.

Note

[IMAGE alt='image' src='GUID-0FA35429-8C7E-4116-97A1-50A665F66751-a5.png']

This example includes the following main tasks:

1. Query the multiplexer sessions and routes for the multiplexed pin.
2. Use a For Loop to complete the following tasks for each multiplexed site:
  1. Connect the required multiplexer route for the site under test.
  2. Use the Semiconductor Module context created for each site to query for the instrument session for the pin.
  3. Take a measurement for a single site.
  4. Use the Pin Query Context with a pin-based instance of the Publish Data VI to publish the measurement.
  5. Disconnect the multiplexer route.
  6. Close the single site Semiconductor Module context.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following test, which evaluates one measurement for the
 multiplexed pin, as shown in the following figure:

[IMAGE alt='image' src='GUID-5AA253CA-738E-4155-B479-B5D4925AC2DC-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=instruments.html language=enus -->
## TOPIC 00150: Instruments (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `instruments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/instruments.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Instruments section on the Pin Map tab to specify the type of instruments required to execute the test program and the name and attributes of each instrument. You can right-click any item in the section you want to edit and use the context menu to complete common tasks. Choose one of the fol

### Instruments (TSM)

Use the Instruments section on the Pin Map tab to specify the type of
 instruments required to execute the test program and the name and attributes of each
 instrument. You can right-click any item in the section you want to edit and use the
 context menu to complete common tasks.

Choose one of the following options to add an instrument to the pin map file:

- Click <Add Instruments Here> to display the Instruments pane, and click the button of the instrument type you want to add.
- Right–click <Add Instruments Here> and select the instrument type you want to add from the context menu.

The Pin Map Editor automatically adds the instrument to the Instruments section. Select an instrument in the Instruments section to display the Instruments pane, where you can edit the attributes of the instrument.

You can also cut, copy, and paste instruments, or add comments in the Instruments pane. Use the Comment button to specify a comment for the selected instrument. Comments display beneath the instrument they modify.

Note

- Consider using the following instrument naming convention for semiconductor
 test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation ,
 for example, HSD_657x_C2_S03 , where
 InstrumentType is an ASCII
 description of the instrument,
 ModelNumber is the model number as
 defined on ni.com ,
 PXIChassisLocation uses a single
 digit to identify the PXI chassis ( Cx ),
 and SlotLocation uses double digits to
 identify the slot location ( Sxx ).
- Names for NI instruments in the pin map file are not case sensitive.

TSM supports the following instrument types and instrument attributes:

- DCPower —Defines an NI-DCPower instrument.
  - Name —Name of the instrument, as defined in Measurement & Automation Explorer (MAX).
  - Number of Channels —Number of channels available on the instrument.
  - Channel Group Name/Channels(s) table —Lists the channel groups and the channels assigned to each group. By default, the Pin Map Editor creates one channel group containing all instrument channels. Use the plus (+) or minus (-) buttons to add or remove channel groups.
 Note A channel group is a collection of channels controlled by the same instrument session. NI-DCPower channel groups can contain channels from different physical NI-DCPower instruments.
    - Channel Group Name —Name of the channel group(s). The Channel Group Name is case sensitive and must not duplicate an instrument name or a group name on another instrument type.
 Note NI-DCPower channels cannot be added to groups of other instruments.
    - Channel(s) —Channel(s) assigned to a channel group. When you add a new channel group, the Pin Map Editor prompts you to add channels to the new group. Define the channels as a comma-separated list (e.g., 0,1,3,..,n), a continuous range (e.g., 0:3), or as a combination of the two (e.g., 0:1,3).
 Note All channels for all instruments must be assigned to a channel group and no channel can assigned to more than one group.
- Digital Pattern —Defines an NI-Digital Pattern instrument.
  - Name —Name of the instrument, as defined in MAX.
  - Number of Channels —Number of channels available on the instrument.
  - Group —Name of the group that contains the instrument. By default, the Pin Map Editor sets this attribute to Digital when you add NI–Digital Pattern instruments to the pin map file. By using the same group name for all NI-Digital Pattern instruments, TSM combines all instruments into a single session so you can avoid session loops in code modules. To create multiple NI-Digital Pattern sessions, use a unique name for each set of instruments for which you want to create a session. Refer to the Digital Pattern Help for information about hardware limitations that prevent certain instruments from operating together as a single instrument.
 Note Instrument group names must be unique and must not duplicate instrument names in the pin map file.
- RFSA —Defines an NI-RFSA instrument. NI-RFSA instruments define a channel named In .
  - Name —Name of the instrument, as defined in MAX.
- RFSG —Defines an NI-RFSG instrument. NI-RFSG instruments define a channel named Out .
  - Name —Name of the instrument, as defined in MAX.
- VST —Defines an NI-VST instrument that can hold RFSA, RFSG, and FPGA sessions. NI-VST instruments define a channel named In and another channel named Out .
  - Name —Name of the instrument, as defined in MAX.
  - Custom FPGA File —(Optional) path to the FPGA file relative to the path of the pin map file. You can manually specify an absolute file path.
- RFPM —Defines an RF Port Module instrument that can hold RFPM, RFmx, RFSA, RFSG, and FPGA sessions.
  - Name —Name of the VST instrument, as defined in MAX, that is part of the RF port module subsystem.
  - Custom FPGA File —(Optional) path to the FPGA file relative to the path of the pin map file. You can manually specify an absolute file path.
  - Calibration File —Path, relative to the path of the pin map file, to the TDMS files that contain the calibration data for the RF Port Module instrument. You can manually specify an absolute file path.
  - IVI Switch Resource Name —IVI Switch resource name associated with the port module, as defined in MAX.
  - Ports List —Defines the ports available in the RF Port Module in a comma-separated list of numbers or ranges of numbers separated by a hyphen. Port number ranges are inclusive and must be in ascending order, for example, channelList="2,3,4-8" .
- HSDIO —Defines an NI-HSDIO instrument.
  - Name —Name of the instrument, as defined in MAX.
  - Number of Channels —Number of channels available on the instrument.
  - PFI Lines —(Optional) Defines the PFI lines available in the NI-HSDIO instrument in a comma-separated list of numbers or ranges of numbers separated by a hyphen. PFI number ranges are inclusive and must be in ascending order, for example, PFILines="2,3,4-8" .
- DMM —Defines an NI-DMM instrument. NI-DMM instruments define a single channel, displayed within TSM as channel 0 .
  - Name —Name of the instrument, as defined in MAX.
- SCOPE —Defines an NI-SCOPE instrument.
  - Name —Name of the instrument, as defined in MAX.
  - Number of Channels —Number of channels available on the instrument.
  - Group —Name of the group that contains the instrument. By default, the Pin Map Editor sets this attribute to Scope when you add NI–SCOPE instruments to the pin map file. By using the same group name for all NI-SCOPE instruments, TSM combines all instruments into a single session so you can avoid session loops in code modules. To create multiple NI-SCOPE sessions, use a unique name for each set of instruments for which you want to create a session. Refer to the NI-SCOPE Help for information about hardware limitations that prevent certain instruments from operating together as a single instrument.
 Note Instrument group names must be unique and must not duplicate instrument names in the pin map file.
- FGEN —Defines an NI-FGEN instrument.
  - Name —Name of the instrument, as defined in MAX.
  - Number of Channels —Number of channels available on the instrument.
- DAQmx —Defines an NI-DAQmx task, not an instrument.
  - Name —Name of the task, as defined in test program
 code modules.
  - Task Type —Category of the task. Pin queries that
 return tasks of more than one task type return an error.
  - Channel List —List of physical channels associated
 with the task.
  - Use as Relay Driver —Specifies whether to use this
 task as a relay driver.
- Relay Driver —Defines a PXI-2567 relay driver module.
  - Name —Name of the relay driver module, as defined in MAX.
  - Number of Control Lines —Number of control lines available on the relay driver module.
- Multiplexer —Defines a switching instrument to use as a multiplexer across multiple test sites. You can use one instrument multiplexed across multiple test sites or multiple instruments multiplexed across multiple test sites.
  - Name —Name of the Switch Executive virtual device, as defined in MAX.
  - Multiplexer Type —(Optional) String that identifies the switch type, family, class, or product group. You cannot specify a value that begins with ni . This value is a string that you define in the pin map and is not a predefined value from some other source, such as a name in MAX, that you select. Use this value to identify all instances of a particular switch type. Switches of the same type typically have the same session data type and same driver API.
- Custom Instrument —Defines an instrument that TSM does not natively
 support. Use the TSM Code Module API to set any type of session data on
 a channel, group of channels, or instrument. Refer to the <TestStand
 Public> \Examples\NI_SemiconductorModule\Custom
 Instruments directory for examples of using TSM pin map files and VIs to perform tests using
 instruments that TSM does not natively support.
  - Name —Identifies the instrument. For instruments
 that NI provides but that TSM does not natively support, specify the
 name of the instrument, as defined in MAX. Note Names for custom
 instruments in the pin map file are case sensitive.
  - Instrument Type Id —String that identifies the
 instrument type, family, class, or product group. You cannot specify a
 value that begins with ni . This value is a string that
 you define in the pin map and is not a predefined value from some other
 source, such as a name in MAX, that you select. Use this value to
 identify all instances of a particular instrument type. Instruments of
 the same type typically have the same session data type and same driver
 API.
- Model-Based Instrument —Defines a Model-Based Instrument.
  - Name —Unique string that identifies the instance of the Model-Based
 Instrument in the pin map.
  - Instrument Model —List of installed model
 description files in the Instrument Model Library.
  - Category —Category of the ModelBasedInstrument.
 The category is set in the instrument model and cannot be changed.
  - Subcategory —Subcategory of the
 ModelBasedInstrument. The subcategory is set in the instrument model and
 cannot be changed.
  - Property/Value Tables —Editable tables of
 instrument and resource properties as defined in the model description
 file. The first table contains properties for the entire instrument.
 Subsequent tables contain properties for specific resources of the
 instrument.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)
- Pin Map Editor (TSM)
- TSM Code Module API
- Model-Based Instruments (TSM)

Related tasks:

- Custom Instruments (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=instrumentstudio-project-panel.html language=enus -->
## TOPIC 00151: InstrumentStudio Project Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `instrumentstudio-project-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/instrumentstudio-project-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The InstrumentStudio Project panel contains the following options: InstrumentStudio Project File Path—Specifies the pathname of the InstrumentStudio project file to use in the test program. A red exclamation point indicates that an issue exists for the file. A tooltip displays the error message. Do

### InstrumentStudio Project Panel

The InstrumentStudio Project panel contains the following options:

- InstrumentStudio Project File Path —Specifies the pathname of the
 InstrumentStudio project file to use in the test program.
 A red exclamation point indicates that an issue
 exists for the file. A tooltip displays the error
 message. Do not proceed without reviewing the errors
 for the file.
- Open file for edit 
 —Launches InstrumentStudio. If you specify an
 InstrumentStudio project file, this project opens in
 InstrumentStudio, otherwise the most recent project
 loads.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=labview-operator-interface-architecture.html language=enus -->
## TOPIC 00152: LabVIEW Operator Interface Architecture (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `labview-operator-interface-architecture.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/labview-operator-interface-architecture.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LVSemiOI.lvproj, located in the <TestStand>\UserInterfaces\NI_SemiconductorModule\LabVIEW directory, includes the TestStand Semiconductor Module Operator Interface.lvlib, which is the primary library for the operator interface.

### LabVIEW Operator Interface Architecture (TSM)

The LVSemiOI.lvproj, located in the <TestStand>\UserInterfaces\NI_SemiconductorModule\LabVIEW
 directory, includes the TestStand Semiconductor Module
 Operator Interface.lvlib, which is the primary
 library for the operator interface.

Parent topic:

Operator Interfaces (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=labview-project-panel.html language=enus -->
## TOPIC 00153: LabVIEW Project Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `labview-project-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/labview-project-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Project panel to link a sequence file to a LabVIEW project file, which allows the selected sequence file to populate pin, relay, relay configuration, specification, published data ID, and input data ID controls in the specified LabVIEW project file. If you link multiple sequence file

### LabVIEW Project Panel

Use the LabVIEW Project panel to link a sequence file to a LabVIEW project file, which allows the selected sequence file to populate pin, relay, relay configuration, specification, published data ID, and input data ID controls in the specified LabVIEW project file. If you link multiple sequence files with different pin map or specification files, TSM combines the values into a single list when populating the controls. The LabVIEW Project panel contains the following options:

- LabVIEW Project File Path —Specifies the pathname of the LabVIEW project file to associate with the sequence file.
- Open file for edit 
 —Launches the specified LabVIEW project file in
 LabVIEW.
- Link/Unlink —Links or removes the link from the selected LabVIEW project file to the sequence file currently open. The LabVIEW project file stores the sequence file link as a relative path. If the LabVIEW project file is currently open in LabVIEW, LabVIEW prompts you to save the project.

You can also link a LabVIEW project file to a sequence file in LabVIEW. Refer to *Linking a Sequence File to a LabVIEW Project File (TSM)* in the *LabVIEW Help* for more information.

Parent topic:

Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=launching-custom-instrument-panels.html language=enus -->
## TOPIC 00154: Launching Custom Instrument Panels

- bundle_id: `teststand-semiconductor-module`
- source_path: `launching-custom-instrument-panels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/launching-custom-instrument-panels.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor Module Custom Instrument Panels and select from the available options to launch the corresponding custom instrument panel VI. Click the Close (X) button on the custom instrument panel VI title bar to end the execution of the VI. Although you can launch a custom instrument panel

### Launching Custom Instrument Panels

Select Semiconductor Module»Custom Instrument Panels and select from the available options to launch the corresponding
 custom instrument panel VI. Click the Close (X) button on the
 custom instrument panel VI title bar to end the execution of the VI.

Although you can launch a custom instrument panel at any time, the VI will not have access to a valid Semiconductor Module context object reference for pin- and site-aware instrument sessions until all test program executions are at a breakpoint. Additionally, the Semiconductor Module context object reference is not available to custom instrument panel VIs when any test program execution is at a breakpoint in the ProcessCleanup callback.

Parent topic:

Custom Instrument Panels (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=licensing-options.html language=enus -->
## TOPIC 00155: TestStand Semiconductor Module Licensing Options

- bundle_id: `teststand-semiconductor-module`
- source_path: `licensing-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/licensing-options.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you install TSM, you must use the NI Activation Wizard to activate the software or initiate the evaluation period for the software. When you activate TSM, you need the serial number and the name of the software kit. You can find both of these items on the Certificate of Ownership card included

### TestStand Semiconductor Module
 Licensing
 Options

After you install TSM, you must use the NI Activation Wizard to activate the software or
 initiate the evaluation period for the software. When you activate TSM, you need the serial
 number and the name of the software kit. You can find both of these items on the Certificate
 of Ownership card included in your software kit.

NI offers a variety of licenses for the different ways you can use TSM in development and
 deployment applications. You can select from the following types of
 licenses: TestStand Semiconductor Module Development License and
 TestStand Semiconductor Module Debug Deployment Environment
 License.

Use the following descriptions only as a reference for the licensing options. Refer to
 ni.com/activate for more information about activating TestStand licenses.
 Contact a local NI representative for more information or for questions about specific
 licensing needs.

Note

<National
 Instruments>\Shared\MDF\Legal\license\NIReleased

Related information:

- License Setup and Activation

#### TestStand Semiconductor Module
 Evaluation Package

When you run TSM in Evaluation Mode, the software expires after 7 days. The software runs as a fully functional Development System during the evaluation period.

You can use an ni.com User Profile to extend the evaluation period for an additional 45 days. You
 can activate a license at any point during or after the evaluation
 period.

#### TestStand Semiconductor Module
 Development License (783522-35)

Activate the TestStand Semiconductor Module Development System License to develop and edit test
 programs within the TestStand Sequence Editor. You must have an
 ni.com User Profile to activate an TestStand Semiconductor Module
 Development System License.

#### TestStand Semiconductor Module Debug
 Deployment Environment License (779991-35)

The TestStand Semiconductor Module Debug Deployment Environment License offers the most
 flexibility for deploying TestStand, LabVIEW-based, Measurement
 Studio-based systems.

Activate this license to install the development versions of TestStand, LabVIEW, Measurement Studio, Switch Executive, TSM, and any corresponding add-on toolkits on a single test station so you can debug deployed test applications on the test station. This license grants the ability to make minor edits to fix bugs in deployed test applications but does not grant the ability to perform any development tasks using TestStand, LabVIEW, or Measurement Studio on the test station.

You cannot activate and deactivate the TestStand Semiconductor Module Debug Deployment
 Environment License and reuse it on multiple computers. If you need
 to use a single debug license across multiple computers, contact NI
 for more information about the Concurrent TestStand Semiconductor
 Module Debug Deployment Environment License.

#### TestStand Semiconductor Module Base
 Deployment License (784608-35)

The TestStand Semiconductor Module Base Deployment License is the minimum license required for
 all deployed TSM-based applications. Activate this license to deploy
 the TSM Runtime, the TestStand Runtime, and the Switch Executive
 Runtime. The Base Deployment License enables you to run a TSM
 operator interface and test programs on the single test station to
 which the license applies. This license does not grant the ability
 to perform any development tasks using the TestStand Sequence
 Editor, a TestStand custom sequence editor, or the TestStand
 API.

<!--NI_TOPIC bundle=teststand-semiconductor-module path=load-correlatin-offsets-step.html language=enus -->
## TOPIC 00156: Load Correlation Offsets Step (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `load-correlatin-offsets-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/load-correlatin-offsets-step.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Load Correlation Offsets step only in the ProcessSetup sequence to load and apply correlation offset values to test results on a per-site basis. The step applies correlation offset values at run time before evaluating the test result data against limits. The step stores the offset value to a

### Load Correlation Offsets Step (TSM)

Use the Load Correlation Offsets step only in the ProcessSetup
 sequence to load and apply correlation offset values to test results on a per-site
 basis. The step applies correlation offset values at run time before evaluating the test
 result data against limits. The step stores the offset value to apply in the
 Step.Result.Evaluations[index].NumericLimit.CorrelationOffset
 property on Semiconductor Multi Test steps. The Semiconductor Multi Test step adds the
 correlation offset to the test result data before evaluating against limits. The Debug
 Test Results Log and CSV Test Results Log include the correlation offset values. The
 STDF Log includes the correlation offsets file path as a DTR with an
 NIDTR: prefix to record the path of the correlation offsets file in
 a <CorrelationOffsetsFilePath> XML tag. For example, if you
 specify C:\Data\TestPrograms\mypath.txt in the Correlation
 Offsets File Path option of the Load Correlation Offsets step edit tab,
 the STDF Log includes the following information:

NIDTR:<CorrelationOffsetsFilePath>C:\Data\TestPrograms\mypath.txt</CorrelationOffsetsFilePath>

If the length of the text to add is more than 255 characters, TSM splits the text
 among multiple DTRs, each with an NIDTR: prefix.

When this step is used to load a correlation offsets file, it stores the file
 path in the CorrelationOffsetsFileAbsolutePath lot settings
 property. To access this file path or determine whether correlation offsets
 have been loaded at runtime, use the Get Test Information step to read the
 value of this property.

#### Configuring the
 Step

Use the Load Correlation Offsets Step edit tab in the TestStand Sequence
 Editor to specify the correlation offsets file to use.

Parent topic:

TSM Step Types

Related concepts:

- Exporting a Correlation Offsets Template File (TSM)
- Semiconductor Multi Test Step Properties
- Semiconductor Multi Test Step
- Debug Test Results Logs (TSM)
- Standard Test Data Format (STDF) Log (TSM)
- Adding DTRs to the STDF Log File (TSM)
- Load Correlation Offsets Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=load-correlation-offsets-tab.html language=enus -->
## TOPIC 00157: Load Correlation Offsets Tab (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `load-correlation-offsets-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/load-correlation-offsets-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Load Correlation Offsets tab contains the following options: Correlation Offsets File Path—Path to the correlation offsets file to use. TSM sets the CorrelationOffsetsFileAbsolutePath property at run time with this value. Specify by Expression—Enable this option to use an expression to specify t

### Load Correlation Offsets Tab (TSM)

The Load Correlation Offsets tab contains the following options:

- Correlation Offsets File Path —Path to the correlation offsets file to
 use. TSM sets the CorrelationOffsetsFileAbsolutePath property
 at run time with this value.
- Specify by Expression —Enable this option to use an expression to specify the path to the correlation offsets file to use.

Parent topic:

Load Correlation Offsets Step (TSM)

Related concepts:

- Exporting a Correlation Offsets Template File (TSM)
- Accessing Lot Settings from a Test Program (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=load-data-in-performance-analyzer.html language=enus -->
## TOPIC 00158: Loading Data in the Test Program Performance Analyzer (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `load-data-in-performance-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/load-data-in-performance-analyzer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test Program Performance Analyzer automatically launches after you complete a test program performance measurement and loads the data TSM generates. If an instance of the Test Program Performance Analyzer is already running when you complete a test program performance measurement, the most recen

### Loading Data in the Test Program Performance Analyzer (TSM)

The Test Program Performance Analyzer automatically launches after you complete a test program performance measurement and loads the data TSM generates.

If an instance of the Test Program Performance Analyzer is already running when you complete a test program performance measurement, the most recently launched instance of the analyzer handles the data TSM generates in the following ways:

- If the analyzer is not displaying any data, displays the newly generated data set.
- If the analyzer is displaying a single data set, prompts you to compare the newly generated
 data set to the previous data set displayed in the analyzer
 or to replace the previous data set displayed in the
 analyzer with the newly generated data set.
- If the analyzer is already comparing two data sets, prompts you to
 compare the newly generated data set to the previous base
 data set displayed in the analyzer or to the previous
 modified data set displayed in the analyzer.
  - When you click the Compare with Base
 Data button, TSM replaces the previous
 modified data set displayed in the analyzer with
 the newly generated data set.
  - When you click the Compare with
 Modified Data button, TSM completes
 the following actions:
    - Discards the previous base data set displayed
 in the analyzer.
    - Converts the previous modified data set
 displayed in the analyzer to the current base data
 set to display in the analyzer.
    - Replaces the previous modified data set
 displayed in the analyzer with the newly generated
 data set.

You can also use the Log File Path control and Load button near the upper right corner of the Test Program Performance Analyzer to manually specify and load a log file for a single data set to display in the analyzer. When you select the Compare Data Sets mode, you can use the Base Log File Path and the Modified Log File Path controls and Load buttons to manually specify and load log files for two data sets to display and compare in the analyzer.

Loading large log files can cause performance and memory usage issues. To improve performance and avoid memory usage issues, load a sample of the batches in a log file by enabling the Log Data Sample Rate checkbox and specifying the sample rate. When the Log Data Sample Rate checkbox is enabled, one out of every N batches in a log file will be loaded when you click the Load button, where N is the specified sample rate.

To view the metadata of log files, including notes, click the Log Browser
 button to open the Log Browser Window.

Parent topic:

Test Program Performance Analyzer (TSM)

Related concepts:

- Comparing Data in the Test Program Performance Analyzer (TSM)
- Log Browser Window (TSM)

Related tasks:

- Measuring Test Program Performance (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=log-browser-window.html language=enus -->
## TOPIC 00159: Log Browser Window (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `log-browser-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/log-browser-window.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the Log Browser button near the upper right corner of the Test Program Performance Analyzer to open the Log Browser window, which you can use to view or compare multiple log files that represent different modifications of a test program. Complete the following steps to view or compare log file

### Log Browser Window (TSM)

Click the Log Browser button near the upper right corner of the Test Program Performance Analyzer to open the Log Browser window, which you can use to view or compare multiple log files that represent different modifications of a test program.

Complete the following steps to view or compare log files.

1. In the Log Directory path control, select the top-level directory that contains the log files you want to view to compare. The column on the left displays relative subdirectories.
2. Complete the following steps to view file(s) in Single Data Set mode or Compare Data Sets mode.
  1. Single Data Set – Double-click the row of the file you want to load. The background row color turns blue.
  2. Compare Data Sets – Right-click the row of the base log file you want to load and chose Select Base Log File from the context menu. The background row color of the base log file you selected turns gray. Right-click the row of the modified log file you want to load and chose Select Modified Log File from the context menu. The background row color of the modified log file you selected turns blue.

Parent topic:

Test Program Performance Analyzer (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=log-browser-window_2.html language=enus -->
## TOPIC 00160: Log Browser Window (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `log-browser-window_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/log-browser-window_2.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the Log Browser button near the upper right corner of the Test Program Performance Analyzer to open the Log Browser window, which you can use to view or compare multiple log files that represent different modifications of a test program. Complete the following steps to view or compare log file

### Log Browser Window (TSM)

Click the Log Browser button near the upper right corner of the Test Program Performance Analyzer to open the Log Browser window, which you can use to view or compare multiple log files that represent different modifications of a test program.

Complete the following steps to view or compare log files.

1. In the Log Directory path control, select the top-level directory that contains the log files you want to view to compare. The column on the left displays relative subdirectories.
2. Complete the following steps to view file(s) in Single Data Set mode or Compare Data Sets mode.
  1. Single Data Set – Double-click the row of the file you want to load. The background row color turns blue.
  2. Compare Data Sets – Right-click the row of the base log file you want to load and chose Select Base Log File from the context menu. The background row color of the base log file you selected turns gray. Right-click the row of the modified log file you want to load and chose Select Modified Log File from the context menu. The background row color of the modified log file you selected turns blue.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=log-custom-data-to-stdf.html language=enus -->
## TOPIC 00161: Logging Custom Data to the STDF Log File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `log-custom-data-to-stdf.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/log-custom-data-to-stdf.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The STDF Log result processing plug-in automatically logs data to the STDF log file about the tester configuration and test execution. You can customize tester, part, wafer, and text data to log in the STDF log file. Type of Data Description Tester The Master Information Record (MIR), Site Descripti

### Logging Custom Data to the STDF Log File (TSM)

The STDF Log result processing plug-in automatically logs data to the STDF log file about the tester configuration and test execution. You can customize tester, part, wafer, and text data to log in the STDF log file.

| Type of Data | Description |
| --- | --- |
| Tester | The Master Information Record (MIR), Site Description Record (SDR), and Wafer Configuration Record (WCR) in the STDF log file store information about the configuration of the tester itself. TSM automatically logs data from the NI_SemiconductorModule_StandardLotSettings and NI_SemiconductorModule_StandardStationSettings data types to these records. You can customize the data stored in the STDF log records by using callbacks to modify the data in the containers within TestStand. TSM stores the following values in the MIR in addition to values TSM obtains from the NI_SemiconductorModule_LotSettings and NI_SemiconductorModule_StationSettings data types:MIR Field NameValueEXEC_TYPENI STS Software Note You can customize this field.EXEC_VERIf STS Software is installed: <STS Software Version>Otherwise: <TSM year-based version (<TSM full version>)>For example, 2016 (16.0.0.49152). |
| MIR Field Name | Value |
| EXEC_TYPE | NI STS Software Note You can customize this field. |
| EXEC_VER | If STS Software is installed: <STS Software Version>Otherwise: <TSM year-based version (<TSM full version>)>For example, 2016 (16.0.0.49152). |
| Part | The Part Results Record (PRR) in the STDF log file stores information about each tested part, including the Part ID, X and Y coordinates of the location of the part on the die, and a text description for the part. You can customize the data TSM logs from the UUT container to these fields within the PRR record. |
| Wafer | The Wafer Information Record (WIR) and Wafer Result Record (WRR) in the STDF log file store information related to wafer tests. If you are performing wafer testing, you can customize the data stored in these records by modifying the value of the WaferRuntimeData parameter in the StartOfTest handler/prober driver entry point. |
| Text | If the data you want to add to the STDF log file is not included in any of the above records, you can include text data as a Datalog Text Record (DTR) in the STDF log file by using the following techniques: Adding Text Data for a Part Using Additional Results—You can use the Additional Results panel of the Step Settings pane to add a DTR record after all the part test records associated with the step. To configure the Additional Results panel to generate a DTR record, set the Name option of the result to NI.STDF.DTR and set the Value to Log option to the value you want to store in the DTR record. You can create multiple results with the name NI.STDF.DTR, and each result appears in the STDF log file as a separate DTR record.Adding Text Data between Parts—If the text data you want to log is not associated with a specific part, you can insert DTR records between parts using a .NET Action step in a callback sequence or in a custom result processor model plug-in. |

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- NI_SemiconductorModule_LotSettings Data Type
- NI_SemiconductorModule_StationSettings Data Type
- Customizing STDF MIR, SDR, and WCR Field Values (TSM)
- Customizing STDF PRR Field Values (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)
- Adding DTRs to the STDF Log File (TSM)

Related reference:

- Customizing STDF WIR and WRR Field Values (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=log-failed-cycle-to-stdf.html language=enus -->
## TOPIC 00162: Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `log-failed-cycle-to-stdf.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/log-failed-cycle-to-stdf.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can fetch and publish failed cycle information from the NI-Digital Pattern Driver and log the information in the STDF Log file. TSM does not support logging failed cycles when using multiple NI-Digital Pattern Driver sessions to burst a pattern for a site. If you need multiple instruments to bur

### Logging Failed Cycle Information from NI-Digital Pattern Driver to STDF Log File (TSM)

You can fetch and
 publish failed cycle information from the NI-Digital
 Pattern Driver and log the information in the STDF Log
 file.

Note

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related tasks:

- Fetching and Publishing Failed Cycle Information in LabVIEW Code Modules (TSM)

Related reference:

- Failed Cycle Information in Functional Test Records (FTRs) (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=logging-text-data.html language=enus -->
## TOPIC 00163: Logging Text Data

- bundle_id: `teststand-semiconductor-module`
- source_path: `logging-text-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/logging-text-data.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to add data to the Debug Test Results Log that is not a measurement or test limit, you can include text data in the Debug Test Results Log by using the following techniques: Adding Text Data for a Step Using Additional Results—You can use the Additional Results panel of the Step Settings

### Logging Text Data

If you want to add data to the Debug Test Results Log that is not a measurement or test limit, you can include text data in the Debug Test Results Log by using the following techniques:

- Adding Text Data for a Step Using Additional Results —You can use the
 Additional Results
 panel of the
 Step Settings
 pane to add text data after all the measurements and test
 limits for the tests associated with the step. To configure
 the Additional Results panel to generate text data in the
 Debug Test Results Log, set the Name 
 option of the result to NI.TestResultsLog 
 and set the Value to Log option to
 the value you want to add to the log file. You can
 optionally add a text label for the data by adding it to the
 end of the Name field in the form
 NI.TestResultsLog.CustomTextLabel ,
 where CustomTextLabel is the text you
 want to display as a label in the log file.
- Adding Text Data between Test Steps —If the text data you want to log is not associated with a specific step, you can use the Additional Results step type to add text data to the Debug Test Results Log. Use the Additional Results panel of the Step Settings pane as described above to add data to the log file.

Parent topic:

Debug Test Results Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=logging-trace-data.html language=enus -->
## TOPIC 00164: Logging Trace Data

- bundle_id: `teststand-semiconductor-module`
- source_path: `logging-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/logging-trace-data.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use trace logging to track all test activity, including instrument I/O and test operations. Introduced in TestStand Semiconductor Module 26.0 You can enable trace logging in the TestStand Sequence Editor. You can also enable trace logging in both the .NET and LabVIEW TSM Operator Interfaces. The TSM

### Logging Trace Data

Use trace logging to track all test activity, including instrument I/O and test
 operations.

Introduced in TestStand Semiconductor Module
 26.0

You can enable trace logging in the TestStand Sequence Editor. You can also enable
 trace logging in both the .NET and LabVIEW TSM Operator Interfaces.

- TSM-level events, such as OnLotConfigured and
 StartLot
- .NETCodeModuleAPI calls, such as Publish,
 GetNIDCPowerSession
- Driver calls

- A category, such as TSM or IO Trace
- The executing test socket
- The test sockets contained within the call

The default storage location for trace logs is C:\Users\Public\Documents\National
 Instruments\TestStand <version> \TraceLogs. TestStand Semiconductor Module generates three intermediate log files at
 the start of each run. These files capture the logs from different sources. TestStand Semiconductor Module combines all three logs at the end of a run
 into a single shared log file.

#### Enabling
 Trace Logging

- Sequence Editor toolbar—Click the Enable Trace Logging button in the toolbar.
- .NET Operator Interfaces—Select Enable Trace Logging 
 from the pull-down menu.
- LabVIEW Operator Interfaces—Click the Enable Trace
 Logging button in the toolbar.

Write Log Messages to Output

Semiconductor Module

Sequence
 Editor

- An attached debugger output window. If the process running a sequence
 includes a debugging output window, log messages appear in this window.
- The TestStand Output window pane.

You can also access trace logging in .NET with the
 ISemiconductorModuleManager.TraceLogger property. This property
 also allows users to toggle other properties such as
 LogDirectoryPath and
 IncludeTimestampInLogEntries.

Parent topic:

Debugging

Related concepts:

- Semiconductor Module Menu

Related reference:

- Semiconductor Module Toolbar Buttons

<!--NI_TOPIC bundle=teststand-semiconductor-module path=lot-statistics-viewer.html language=enus -->
## TOPIC 00165: Lot Statistics Viewer (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `lot-statistics-viewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/lot-statistics-viewer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor Module»Show Lot Statistics Viewer or click the Show Lot Statistics Viewer button on the TSM toolbar to launch the Lot Statistics Viewer window, in which you can view lot statistics, including per-site bin counts, while running or debugging a sequence in the sequence editor. You

### Lot Statistics Viewer (TSM)

Select Semiconductor Module»Show Lot Statistics Viewer or click the Show Lot Statistics Viewer button on the TSM toolbar to launch the Lot Statistics Viewer window, in which you can view lot statistics, including per-site bin counts, while running or debugging a sequence in the sequence editor. You can also control test program execution in the Lot Statistics Viewer.

The Lot Statistics Viewer displays a new tab for each test program sequence file you execute. The tab includes a table of the software bin statistics for each site and highlights the cell for each updated DUT result. When execution completes, the table dims. Click the expand/collapse button to the left of the software bin name to collapse the view to show only the total part count or to expand the view to show part counts for each software bin.

When you use the AvailableSiteNumbers property on the NI_SemiconductorModule_StationSettings
 data type to specify which site numbers from a pin map for a test
 program to use when running the test program, the Lot Statistics
 Viewer displays only the sites you specify.

The Lot Statistics Viewer window includes the following options:

- Configuration —Configures the lot with the selected configuration for the test program that corresponds to the active sequence file. This control is disabled if the active sequence file has no configurations.
- Single Test —Starts a lot and tests a single DUT for each site for the active sequence file if no lot is active and pauses when complete or, if paused, tests a single DUT for each site before pausing again.
- Start/Resume Lot —Starts testing a new lot, resumes a suspended sequence execution at a breakpoint, or resumes a sequence execution that is paused between DUTs.
- Pause —Pauses testing of the lot. Testing pauses between DUTs after completing the tests for the current DUTs on each site and before TSM sends the end-of-test (EOT) signal to the handler or prober.
- Retest —After a single test completes or when you pause a lot, retests a single DUT for each site for the active sequence file and then pauses execution. The lot statistics update to include only the results from the last retest for a given DUT.
- End Lot —Ends testing the current lot. Click this button
 instead of selecting the Debug»Terminate All menu item to safely end a lot.
- Hide Empty Bins —Removes the empty bins from the display. This option is enabled by default.

Parent topic:

Dialog Boxes and Windows

Related concepts:

- NI_SemiconductorModule_StationSettings Data Type

<!--NI_TOPIC bundle=teststand-semiconductor-module path=lot-summary-options-dialog-box.html language=enus -->
## TOPIC 00166: Lot Summary Options Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `lot-summary-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/lot-summary-options-dialog-box.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable and configure the TSM result processing plug-ins to launch the Lot Summary Options dialog box, in which you can specify settings for the STDF Log file. The Lot Summary Options dialog box contains the following options: Lot Summary Report Destination Directory—Absolute path of the directory in

### Lot Summary Options Dialog Box (TSM)

Enable and configure the TSM result processing plug-ins to launch the Lot Summary Options dialog box, in which you can specify settings for the STDF Log file.

The Lot Summary Options dialog box contains the following options:

- Lot Summary Report Destination Directory —Absolute path of the directory in which you want TSM to create the report file. Leave the control blank if you want TSM to create the report file in the same directory as the test program main sequence file.
- Generate One File per Wafer —Specifies to create a separate Lot Summary Report file for each tested wafer. This option has no effect when testing without a wafer probe.

Parent topic:

Dialog Boxes and Windows

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=lot-summary-reports.html language=enus -->
## TOPIC 00167: Lot Summary Reports (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `lot-summary-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/lot-summary-reports.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When testing completes, you can generate a test Lot Summary Report that provides information about testing results. You can enable the Lot Summary Report in the Results Processing dialog box. The Lot Summary Report includes the following sections: Lot Description Header—Contains lot and station sett

### Lot Summary Reports (TSM)

When testing completes, you can generate a test Lot Summary Report that provides information about testing results. You can enable the Lot Summary Report in the Results Processing dialog box. The Lot Summary Report includes the following sections:

- Lot Description Header —Contains lot and station settings information and
 execution data, such as start and end time, that describe or
 identify the test cell, test conditions, state of Offline Mode, and DUTs
 tested.
- Lot Results —Contains results of all DUTs from all sites, including the percent-of-total yield. The Lot Results section also includes subsections for all tests and Inline QA only (if available) tests. You can use this data as a metric to judge the overall quality of the test lot.
- Site Results —Contains a table of test lot statistics by site. You can use this data as a metric to compare the test quality among different sites.
- Software Bin Results —Contains a table of software bin numbers, associated hardware bin numbers, software bin descriptions, total counts, and percent-of-total yield. You can use this data to identify specific types of failures reported during testing.
- Hardware Bin Results —Contains a table of hardware bin numbers, hardware bin descriptions (if available), total counts, and percent-of-total yield. You can use this data to separate DUTs with different failure modes or passing grades and to reconcile tester software counts with physical DUT counts.
- Test Results —Contains a table of test evaluation results
 by site for all the tests that executed at least once in the lot, sorted by
 execution order. You can use this data to compare the results of lots, which can
 be helpful during debugging. If alarms are enabled, the table includes the
 number of alarms raised when executing each test step.
- Alarms —If alarms are enabled, this section contains a
 table with the number of alarms of a given type that were raised during test
 program execution, on each site, pin, and step.

Note

Parent topic:

Reports and Data Logs (TSM)

Related concepts:

- Offline Mode (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=measure-and-publish-values-offline.html language=enus -->
## TOPIC 00168: Measuring and Publishing Values in Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `measure-and-publish-values-offline.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/measure-and-publish-values-offline.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Although simulated instruments behave as closely as possible to real instruments, measurements and data differ in Offline Mode. Additionally, custom code that processes results, test time performance, instrument functionality, and error reporting might differ in Offline Mode and can result in differ

### Measuring and Publishing Values in Offline
 Mode (TSM)

Note

Complete the following step to measure and publish values in Offline Mode:

TestStand Sequence
 Editor

1. Select one of the following options from the Offline Mode Data
 Option drop-down menu on the Options tab. 
 OptionDescriptionUse Passing Values
 (Default) TSM uses passing values and ignores the values the test code module
 publishes.For Numeric Limit tests with limits, TSM uses the
 average of the limits. For Numeric Limit tests without limits, TSM
 logs 0. For Pass/Fail tests, TSM uses the value
 True.Use Published Values
 TSM uses the values the test code module publishes.Use SimulatedData Property
 TSM uses the values you specify in the
 SimulatedDataUsageType property for each test.
2. If you select Use SimulatedData Property, specify a
 single value for all sites and how to specify values per site for a test. 
 Type of Test
 Single Value for All Sites
 Specific Value Per SiteNumeric Limit
 Set the
 Step.Result.Evaluations[i].NumericLimit.SimulatedData.SimulatedDataUsageType
 property to AllSites.
 Specify the value you want to use in the
 Step.Result.Evaluations[i].NumericLimit.SimulatedData.AllSites
 property.
 Set the
 Step.Result.Evaluations[i].NumericLimit.SimulatedData.SimulatedDataUsageType
 property to PerSite.
 Specify the values you want to use in the
 Step.Result.Evaluations[i].NumericLimit.SimulatedData.PerSite
 property.
 Pass/Fail
 Set the
 Step.Result.Evaluations[i].PassFail.SimulatedData.SimulatedDataUsageType
 property to AllSites.
 Specify the value you want to use in the
 Step.Result.Evaluations[i].PassFail.SimulatedData.AllSites
 property.
 Set the
 Result.Evaluations[i].PassFail.SimulatedData.SimulatedDataUsageType
 property to PerSite.
 Specify the values you want to use in the
 Result.Evaluations[i].PassFail.SimulatedData.PerSite
 property.

You can view the published values in data logs and
 reports.

Parent topic:

Executing Test Programs in Offline Mode (TSM)

#### Data Logs and Reports in Offline Mode

The following table lists how data logs and reports include the state of Offline Mode
 to indicate that the file includes real or simulated data.

| File | Implementation |
| --- | --- |
| STDF log file | NIDTR:<OfflineMode>Disabled</OfflineMode> NIDTR:<OfflineMode>Enabled</OfflineMode> |
| Lot Summary Report | Offline Mode entry in lot description header |
| Debug Test Results Log | Offline Mode entry in header |
| Test Program Performance Analyzer summary log file | Offline Mode entry |

Note

<!--NI_TOPIC bundle=teststand-semiconductor-module path=measurement-saturation-alarm.html language=enus -->
## TOPIC 00169: Measurement Saturation Alarm

- bundle_id: `teststand-semiconductor-module`
- source_path: `measurement-saturation-alarm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/measurement-saturation-alarm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A measurement saturation alarm indicates when a current or voltage measurement circuit is saturated. Introduced in TestStand 2023 Semiconductor Module 2024 Q3 You must install NI-DCPower 2024 Q3 or later to enable measurement saturation alarm. TSM supports measurement saturation alarms for the follo

### Measurement Saturation Alarm

A *measurement saturation alarm* indicates when a current or voltage
 measurement circuit is saturated.

Introduced in TestStand 2023 Semiconductor Module 2024 Q3

Note

NI-DCPower 2024 Q3

TSM supports measurement saturation alarms for the following hardware models:

- PXIe-4137/9
- PXIe-4147
- PXIe-4162/3

A measurement saturation alarm latches only when you fetch a measurement result from the
 instrument.

Parent topic:

Using Alarms to Report Error Conditions at Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=measuring-performance.html language=enus -->
## TOPIC 00170: Measuring Performance (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `measuring-performance.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/measuring-performance.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use TSM, LabVIEW, and TestStand tools to measure execution times so you can determine how changes you make affect performance. TSM During the test program development phase, you can use built-in TSM tools to measure test program performance and then analyze the resulting data with the Test P

### Measuring Performance (TSM)

You can use TSM, LabVIEW, and TestStand tools to measure execution times so
 you can determine how changes you make affect performance.

#### TSM

During the test program
 development phase, you can use built-in TSM tools to measure test program
 performance and then analyze the resulting data with the Test Program Performance Analyzer.
 Some common use
 cases include identifying the slowest test times, identifying low parallel test
 efficiency (PTE) values, and displaying the overall socket time and the calculated PTE value
 for each site configuration.

One way to measure overall performance of the test system
 is to test a number of DUTs using the TSM operator interface and study the values of the
 Socket Time and Cycle Time controls. The socket time primarily corresponds to the time it
 takes to perform test code. The cycle time includes the socket time and the time required to
 perform other tasks, such as binning, placing DUTs, and generating reports.

When you
 measure performance, test enough DUTs to obtain consistent results and minimize the number
 of processes running simultaneously that could affect the performance of the TSM operator
 interface. The first batch in a lot typically takes longer to load than the following
 batches because you must also load resources.

Note

#### LabVIEW

Use
 the following tools to help analyze the performance of VIs:

- LabVIEW VI Analyzer —A static code
 analyzer that identifies potential performance
 problems.
- LabVIEW Desktop Execution Trace
 Toolkit —Performs dynamic code analysis to
 identify problems that might negatively affect performance,
 such as memory leaks and reference leaks.
- Profile Performance and Memory
 window —Built-in LabVIEW tool that determines how
 an individual VI spends time and how the VI uses memory.
 Complete the following steps to use the Profile Performance
 and Memory window:
  1. Configure the TestStand LabVIEW Adapter to
 execute VIs in the LabVIEW Development System
 process.
  2. Open the LabVIEW project that contains the VIs
 you want to analyze.
  3. Select Tools»Profile»Performance and Memory to launch the Profile Performance
 and Memory window.
  4. Click the Start button to
 begin collecting performance data.
  5. Use the TSM operator interface to test a number
 of DUTs to execute VIs you want to profile
 multiple times.
  6. Click the Snapshot button
 in the Profile Performance and Memory window to
 acquire execution time data for the VIs.

#### TestStand

During test program development, use the
 Execution Profiler
 to view and record duration the of steps, code modules, and other
 resources a multithreaded TestStand system uses over a period of
 time. For example, you can identify parts of the test program that
 take longest to execute or identify what shared tester resources
 cause throughput bottlenecks.

You can also use the
 Model Plug-in - Basic Step Time Report
 example tool to measure step execution times. The example includes a
 sample report generator that generates a report in Microsoft Excel
 format that includes time data for individual steps. Use the
 TestStand Execution Profiler to measure execution times of steps and
 code modules.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

Related concepts:

- Execution Timing Overview (TSM)
- Test Program Performance Analyzer (TSM)
- Common Use Cases for Measuring Test Program Performance (TSM)

Related tasks:

- Measuring Test Program Performance (TSM)

Related information:

- Model Plug-in - Basic Step Time Report

<!--NI_TOPIC bundle=teststand-semiconductor-module path=measuring-test-program-performance.html language=enus -->
## TOPIC 00171: Measuring Test Program Performance (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `measuring-test-program-performance.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/measuring-test-program-performance.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: During the test program development phase, you can run a series of executions with varying site configurations to characterize the performance of a test program as the site configuration changes. Complete the following steps to measure test program performance using a consistent environment. Open th

### Measuring Test Program Performance (TSM)

During the test program development phase, you can run a series of executions with varying site configurations to characterize the performance of a test program as the site configuration changes.

Complete the following steps to measure test program performance using a consistent environment.

1. Open the test program you want to measure. The test program must use the Batch or Sequential process model.
2. Verify that the test program specifies a pin map.
3. Select Semiconductor Module»Measure Performance of
 <filename> .
4. Set the options in the Test
 Program Performance Measurement Configuration
 dialog box that launches.
5. Click the Configure Lot Settings button to launch the Configure Lot Settings dialog box. Configure the settings and click OK . 
 Note The Configure Lot Settings dialog box does not display the Enabled Sites list because you use the Test Program Performance Measurement Configuration dialog box to specify site configurations.
6. Click OK in the Test Program Performance Measurement Configuration dialog box.
7. The test program executes in the operator interface that launches. TSM logs the test program
 performance data during execution. TSM automatically
 discards performance data from the first batch in a lot.
8. When the test program execution completes, the operator interface automatically closes, and TSM launches the Test Program Performance Analyzer for you to view and analyze the resulting data.

Parent topic:

Test Program Performance Analyzer (TSM)

Related concepts:

- Test Program Performance Measurement Testing Environment (TSM)
- Test Program Performance Measurement Configuration Dialog Box (TSM)
- Configure Lot Settings Dialog Box (TSM)
- Test Program Performance Measurement Data Logs (TSM)
- Test Program Performance Analyzer (TSM)

Related information:

- Batch Process Model
- Sequential Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=model-based-instruments.html language=enus -->
## TOPIC 00172: Model-Based Instruments (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `model-based-instruments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/model-based-instruments.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use a Model-Based Instrument to specify pin map channels and instrument properties so you can connect TSM to a third-party instrument. Unlike Custom Instruments, Model-Based Instruments can be reused across test programs and pin maps. A Model-Based Instrument is defined in an instrument model descri

### Model-Based Instruments (TSM)

Use a Model-Based Instrument to specify pin map channels and instrument
 properties so you can connect TSM to a third-party instrument. Unlike Custom
 Instruments, Model-Based Instruments can be reused across test programs and
 pin maps.

A Model-Based Instrument is defined in an instrument model description file. The
 instrument model description file is an XML file that follows the Automatic
 Test Markup Language (ATML) schema, the standard for interfacing test system
 components using XML. The instrument model description file includes general
 information, details for connection components (channels, ports, resources),
 and configuration properties of the instrument and its resources. Reuse an
 instrument description file across multiple test programs and pin maps.

Instrument model description files installed by NI are saved in the Instrument
 Model library, located in individual subdirectories under the
 <Program Files>\National
 Instruments\Shared\InstrumentLibrary\SystemDescriptions\ModelDescriptions
 directory.

You can also define your own Model-Based Instrument. Create the following
 directory and save your model description file in it:
 <Public>\Documents\National
 Instruments\InstrumentLibrary\SystemDescriptions\ModelDescriptions.

The specific connection components of a Model-Based Instrument are defined in the
 model description file for all instances of the model. However, in
 individual systems, connection components can have different names, or
 aliases. These aliases correspond one-to-one with the names in the model
 description file. This mapping is defined in a system description file. When
 the mapping is defined in a system description file, the Pin Map Editor
 displays the aliased resource names, rather than the model description
 resource names.

If present, the system description file is located in the following path:
 <Program Files>\National
 Instruments\Shared\InstrumentLibrary\SystemDescriptions\SystemDescription.xml.
 You can define your own system description file and copy it to
 <Public>\Documents\National
 Instruments\InstrumentLibrary\SystemDescriptions\SystemDescription.xml.

Parent topic:

Mapping DUT Pins to Instrument Channels (TSM)

Related concepts:

- Instruments (TSM)
- Pin Map Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=modify-tsm-ui-configuration.html language=enus -->
## TOPIC 00173: Modifying the TSM UI Configuration

- bundle_id: `teststand-semiconductor-module`
- source_path: `modify-tsm-ui-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/modify-tsm-ui-configuration.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to modify the TSM UI Configuration. Customize the toolbars and menus and arrange the sequence editor panes to create the layout you want. Select ConfigureSequence Editor Options and click the UI Configuration tab. Select NI_SemiconductorModule in the Saved Configurations

### Modifying the TSM UI Configuration

Complete the following steps to modify the TSM UI Configuration.

1. Customize the toolbars and menus and arrange the sequence editor panes to create the layout you want.
2. Select Configure»Sequence Editor Options and click the
 UI Configuration
 tab.
3. Select NI_SemiconductorModule in the
 Saved
 Configurations list and click the
 Save Current 
 button to overwrite the existing TSM UI Configuration with
 the UI configuration you just created and to ensure TSM
 loads the modified UI configuration when you launch TSM for
 the first time or enable TSM. Note When
 you first launch the sequence editor after
 installing TSM or when you enable TSM, TSM loads
 only the UI configuration named
 NI_SemiconductorModule.

Parent topic:

TSM Sequence Editor UI Configuration

<!--NI_TOPIC bundle=teststand-semiconductor-module path=modifying-number-of-results-to-csv.html language=enus -->
## TOPIC 00174: Modifying Number of Results to Include

- bundle_id: `teststand-semiconductor-module`
- source_path: `modifying-number-of-results-to-csv.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/modifying-number-of-results-to-csv.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, the CSV Test Results Log includes all test results. You can change the default behavior. Complete the following steps to limit the number of results to include in the CSV Test Results Log. Launch the CSV Test Results Log Options dialog box. Enable the Limit Number of Test Data Records op

### Modifying Number of Results to Include

By default, the CSV Test Results Log includes all test results. You can change the default behavior.

Complete the following steps to limit the number of results to include in the CSV Test Results Log.

1. Launch the CSV Test Results Log Options
 dialog box.
2. Enable the Limit Number of Test Data Records option.
3. Use the Log test data for only one out of every option to specify the number of tests to include in the CSV Test Results Log.

Parent topic:

CSV Test Results Logs (TSM)

Related concepts:

- CSV Test Results Log Options Dialog Box (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=modifying-the-testing-environment.html language=enus -->
## TOPIC 00175: Modifying the Testing Environment

- bundle_id: `teststand-semiconductor-module`
- source_path: `modifying-the-testing-environment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/modifying-the-testing-environment.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to modify the testing environment to simulate a specific production environment. Copy the NI_SemiconductorModule_ PerformanceMeasurement.seq file from the <TestStand>\Components\Modules\NI_SemiconductorModule directory and make changes to the copy. Modify the steps in th

### Modifying the Testing Environment

Complete the following steps to modify the testing environment to simulate a specific production environment.

- Copy the NI_SemiconductorModule_ PerformanceMeasurement.seq file from the
 <TestStand> \Components\Modules\NI_SemiconductorModule 
 directory and make changes to the copy.
- Modify the steps in the Setup and Cleanup step groups to meet the needs of the environment you want to simulate. For example, the Configure Result Processors step contains arrays of result processor names and enabled states. You can modify the step to include additional result processors or remove existing ones.
- Save the changes to the sequence file.
- In the Test
 Program Performance Measurement Configuration
 dialog box, modify the Operator Interface Command
 Line option in the
 Advanced section by replacing
 the path to the NI_SemiconductorModule_PerformanceMeasurement.seq 
 file with the path to the new sequence file you just created
 and modified.

Parent topic:

Test Program Performance Measurement Testing Environment (TSM)

Related concepts:

- Test Program Performance Measurement Configuration Dialog Box (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multi-test-pat-tab.html language=enus -->
## TOPIC 00176: Semiconductor Multi Test Part Average Testing Tab

- bundle_id: `teststand-semiconductor-module`
- source_path: `multi-test-pat-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multi-test-pat-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a part average testing (PAT) callbacks sequence file exists in the <TestStand Public>\Components\Callbacks\NI_SemiconductorModule directory, the Part Average Testing tab contains a table that lists PAT settings for the tests the step performs. Entering Data You can enter data in the table in th

### Semiconductor Multi Test Part Average Testing Tab

When a part average testing
 (PAT) callbacks sequence file exists in the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule
 directory, the Part Average Testing tab contains a table that lists
 PAT settings for the tests the step performs.

#### Entering
 Data

You can enter data in the table in the following
 ways:

- Enter data when a cell is highlighted.
- Click in a cell when it is highlighted.
- Double-click a cell.
- Select a value from a drop-down menu.
- Drag a variable or property from the
 Variables
 pane to a text or expression cell.

#### Copying and Pasting
 Data

You can copy and paste data in the Tests table in the
 following ways:

- Press <Ctrl-C> to copy the contents of selected table
 rows, columns, or cells to the clipboard.
- Press <Ctrl-V> to insert data from the clipboard into the
 table starting from the top left selected cell. If the
 number of rows of data on the clipboard is greater than the
 number of tests in the Tests table, the paste command adds
 new tests to the step to match the clipboard data.
- You can copy data to tests on the same
 Semiconductor Multi Test
 or
 Semiconductor Sequence Call
 step, to tests on other Semiconductor Multi Test or
 Semiconductor Sequence Call steps, or to a Microsoft Excel
 spreadsheet.
- When you modify the data in Excel and paste it back to a
 Semiconductor Multi Test or Semiconductor Sequence Call
 step, the step returns an error if the modified data is
 invalid for a test.

#### Columns

The
 Part Average Testing table contains the following columns:

Note

- The current PAT environment settings
 determine which of the following columns are
 visible.
- Part average testing is available only for tests with a
 Numeric Limit evaluation
 type.

- Test Number —The read-only test number for
 the test to which the PAT settings apply. This column is
 always visible.
- Test Name —The read-only test name of the
 test to which the PAT settings apply. This column is always
 visible.
- PAT Base Test Number —A base test number a
 PAT algorithm can use to automatically generate PAT test
 numbers. PAT plug-ins that use this setting typically hide
 and ignore the Dynamic PAT Test
 Number and Static PAT Test
 Number settings.
- Enable Dynamic PAT —Enables dynamic part
 average testing for the test and enables editing of the
 other dynamic PAT settings for the test. When this setting
 is enabled, TSM automatically generates a PAT test
 associated with the test. The PAT algorithm customizes,
 assigns limits to, and performs the dynamic PAT tests after
 all other tests in the MainSequence 
 sequence complete or during the execution of a Perform Part Average Testing
 step.
- Dynamic PAT Test Number —The test number
 for the dynamic PAT test. This setting is available only
 when Enable Dynamic PAT is
 enabled.
- Dynamic PAT Test Name —The test name for
 the dynamic PAT test. This setting is available only when
 Enable Dynamic PAT is
 enabled.
- Dynamic PAT Software Bin —The software bin
 for the dynamic PAT test. This bin must be a valid fail bin
 defined in the bin definitions file. This
 setting is available only when Enable Dynamic
 PAT is enabled.
- Dynamic PAT Low Limit —The low limit for
 the dynamic PAT test specified in standard deviations from
 the mean. A typical PAT algorithm uses this setting to
 convert the test measurement data to standard deviations
 before performing the PAT test. This setting is available
 only when Enable Dynamic PAT is
 enabled.
- Dynamic PAT High Limit —The high limit for
 the dynamic PAT test specified in standard deviations from
 the mean. A typical PAT algorithm uses this setting to
 convert the test measurement data to standard deviations
 before performing the PAT test. This setting is available
 only when Enable Dynamic PAT is
 enabled.
- Enable Static PAT —Enables static part
 average testing for the test and enables editing of the
 other static PAT settings for the test. When this setting is
 enabled, TSM automatically generates a static PAT test
 associated with the test. The PAT algorithm obtains static
 PAT limits, sets the limits on the static PAT tests, and
 performs the static PAT tests after all other tests in the
 MainSequence sequence complete or
 when a Perform Part Average Testing step executes.
- Static PAT Test Number —The test number
 for the static PAT test. This setting is available only when
 Enable Static PAT is
 enabled.
- Static PAT Test Name —The test name for
 the static PAT test. This setting is available only when
 Enable Static PAT is
 enabled.
- Static PAT Software Bin —The software bin
 for the static PAT test. This bin must be a valid fail bin
 defined in the bin definitions file. This
 setting is available only when Enable Static
 PAT is enabled.

Parent topic:

Semiconductor Multi Test Edit Tabs

Related concepts:

- Part Average Testing Plug-In Architecture (TSM)
- Semiconductor Multi Test Step
- Semiconductor Sequence Call Step
- Part Average Testing Environment Settings (TSM)
- Tests Tab
- Perform Part Average Testing Step (TSM)
- Binning DUTs Based on Test Results (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multi-test-step-execution.html language=enus -->
## TOPIC 00177: Semiconductor Multi Test Step Execution Overview

- bundle_id: `teststand-semiconductor-module`
- source_path: `multi-test-step-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multi-test-step-execution.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Semiconductor Multi Test step uses the following process when executing: Creates a SemiconductorModuleContext object and stores it on the Step.SemiconductorModuleContext property if the site that executes the step is the working site. The SemiconductorModuleContext object describes a subset of p

### Semiconductor Multi Test Step Execution Overview

The Semiconductor Multi Test step uses the following process when
 executing:

1. Creates a SemiconductorModuleContext object and stores it on the Step.SemiconductorModuleContext property if the site that executes
 the step is the working site. The SemiconductorModuleContext 
 object describes a subset of pins, relays, sites, and instruments on a test
 system.
2. Replaces each test that specifies a pin group with a set of tests that are equivalent to the pin group test
 and deletes the pin group test, except for the following differences:
 Note This replacement happens the first time the step executes.
  - The Pin is set to the name of the pin in the pin group.
  - The Test Number is computed by adding the test number specified for the pin group test to the
 zero-based index of the pin in the pin group.
  - The Test Name is computed by appending the name of the pin in the pin group to the test name
 specified for the pin group test.
3. Calls a code module that completes the following actions:
  1. Receives the Step.SemiconductorModuleContext property as an input
 parameter.
  2. Obtains instrument channel and session information using the TSM Code Module API.
  3. Performs measurements.
  4. Publishes measurement data using the TSM Code Module API.
4. Performs tests. For each test, the step completes the following actions:
  1. Obtains the measurement value from the published measurement data or from the expression, if specified,
 in the Test Data Source column on the Tests tab.
  2. Adds the correlation offset specified in the currently loaded correlation offsets file, if any, to the
 measurement value.
  3. Compares the measurement value against the specified limits.
  4. Sets the test status depending on the evaluation type, limits, or measurement value, as shown in
 the following table. Evaluation TypeConditionStatusNumeric LimitYou specify a low limit and high limitPassed or FailedYou do not specify a low limit and high
 limitDonePass/FailThe measurement value is
 TruePassedThe measurement value is
 FalseFailedNoneNoneDone Note When
 you enable the Stop Performing Tests after First
 Failure option on the Options tab and a test fails, TSM sets the status of the
 remaining Numeric Limit and Pass/Fail tests to Skipped. The step
 sets the status for tests with the None
 evaluation type to Done regardless of whether any
 test fails.
  5. Stores the measurement value in the expression, if specified, in the Export Data To 
 column on the Tests tab.
  6. Assigns a software bin to the DUT if the test fails and a bin has not yet been assigned to the DUT.
 If you have already assigned a bin using the Set and Lock Bin step and
 the test fails, the step reports a run-time error.
  7. Continues or stops performing tests depending on whether a test failed and whether you enable the
 Stop Performing Tests after First Failure option on the Options tab. The step
 stores the measurement value in the Export Data To expression for tests with the
 None evaluation type, regardless of whether a test failed.
5. Sets the step status to Passed if all tests pass. Otherwise, sets the step
 status to Failed or Error .

Parent topic:

Semiconductor Multi Test Step

Related concepts:

- Semiconductor Multi Test Step Properties
- TSM Code Module API
- Tests Tab
- Load Correlation Offsets Step (TSM)
- Semiconductor Multi Test Options Tab
- Set and Lock Bin Step (TSM)

Related information:

- Expressions

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multiple-measurements-on-multiple-pins.html language=enus -->
## TOPIC 00178: Multiple Measurements on Multiple Pins (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `multiple-measurements-on-multiple-pins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multiple-measurements-on-multiple-pins.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to take multiple measurements on multiple pins. This example includes the following main tasks: Query for the sessions for the pins. Use a For Loop to iterate on the different measurement conditions. For each condition, use a parallel For Loop to iterate on every instr

### Multiple Measurements on Multiple Pins (TSM)

The following figure shows how to take multiple measurements on multiple pins.

[IMAGE alt='image' src='GUID-589CD06D-CDD6-412A-BFB1-DE2AC433DBA2-a5.png']

This example includes the following main tasks:

1. Query for the sessions for the pins.
2. Use a For Loop to iterate on the different measurement conditions.
3. For each condition, use a parallel For Loop to iterate on every instrument you need to call to take the measurement on all pins in all sites.
4. For each condition, use the original Pin Query Context and a unique Published Data Id with a pin-based instance of the Publish Data VI to publish the measurement for each condition. You do not need to query for sessions inside the For Loop because multiple queries will return the same sessions. You can use the same Pin Query Context to publish multiple times as long as the Published Data Id is unique.
5. Probe the measurement value for every pin and site combination. The source code for the probe is in the Probe Pin Site Data VI.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following tests, where each test evaluates one
 measurement for each digital I/O pin and each unique Published Data
 Id, as shown in the following figure:

[IMAGE alt='image' src='GUID-E8D99A36-DD44-4651-8258-3DFA50604259-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multiple-registers-using-digital.html language=enus -->
## TOPIC 00179: Functional Test for Multiple Registers Using NI-Digital Pattern Driver (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `multiple-registers-using-digital.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multiple-registers-using-digital.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to read multiple register values from captured waveforms. This example includes the following main tasks: Query for the sessions for the digital I/O pins. Use a parallel For Loop to burst patterns and fetch capture waveforms. Convert the per-instrument waveform data to

### Functional Test for Multiple Registers Using NI-Digital Pattern Driver (TSM)

The following figure shows how to read multiple register values from captured waveforms.

[IMAGE alt='image' src='GUID-2C692240-94C8-44C4-A3A1-9B638D07957E-a5.png']

This example includes the following main tasks:

1. Query for the sessions for the digital I/O pins.
2. Use a parallel For Loop to burst patterns and fetch capture waveforms.
3. Convert the per-instrument waveform data to per-site waveforms.
4. Use a For Loop to scan each per-site waveform to obtain register values for four addresses.
5. Transpose the 2D array so that the first dimension corresponds to sites.
6. Use a site-based instance of the Publish Data VI to publish the register value using the address as a hex string for the Published Data Id.

The Semiconductor Multi
 Test step that calls the code module shown above
 contains the following tests, where each test evaluates one numeric
 value per register, as shown in the following figure:

[IMAGE alt='image' src='GUID-C49DA655-6D5F-4749-97E8-4688F89FA8E4-a5.png']

Parent topic:

Multisite Programming Scenarios (TSM)

Related concepts:

- Semiconductor Multi Test Step

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multisite-programming-scenarios.html language=enus -->
## TOPIC 00180: Multisite Programming Scenarios (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `multisite-programming-scenarios.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multisite-programming-scenarios.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates how to address several multisite use cases. Example File Locations <TestStand Public>\Examples\NI_SemiconductorModule\Multisite Programming Scenarios\LabVIEW\MultisiteScenarios.seq Highlighted Features Testing Multiple Sites in Parallel Major API TSM Code Module API Prerequ

### Multisite Programming Scenarios (TSM)

This example demonstrates how to address several multisite use cases.

| Example File Locations | <TestStand Public>\\Examples\\NI_SemiconductorModule\\Multisite Programming Scenarios\\LabVIEW\\MultisiteScenarios.seq |
| --- | --- |
| Highlighted Features | Testing Multiple Sites in Parallel |
| Major API | TSM Code Module API |
| Prerequisites | You must have the LabVIEW Development System installed, and you must configure the LabVIEW Adapter to use the LabVIEW Development System. This example uses the Batch process model. |

Complete the following steps to use this example.

1. Open <TestStand
 Public> \Examples\NI_SemiconductorModule\Multisite Programming
 Scenarios\LabVIEW\MultisiteScenarios.seq .
2. Review the following steps and corresponding code modules:
  - Simple Parametric
 Measurement
  - Query Pin/Site Measurement for
 Unsupported Measurement Type
  - Source-Wait-Measure Parametric
 Test
  - Source Power Supply Pins and Measure
 Digital Pins
  - Multiple Measurements on Multiple
 Pins
  - Source All Digital Pins,
 Source-Wait-Measure Each Digital Pin
  - Functional Test Using NI-Digital
 Pattern Driver
  - Functional Test for Multiple
 Registers Using NI-Digital Pattern
 Driver
  - Functional Test Using NI-HSDIO
 Hardware Compare
  - Functional Test for Multiple
 Registers
  - Instrument Multiplexed Across
 Sites
  - Instrument Multiplexed Across Sites,
 Multiple Measurements

Parent topic:

TSM Example Programs

Related concepts:

- Testing Multiple Sites in Parallel (TSM)
- TSM Code Module API

Related tasks:

- Simple Parametric Measurement (TSM)
- Query Pin/Site Measurement for Unsupported Measurement Type (TSM)
- Source-Wait-Measure Parametric Test (TSM)
- Source Power Supply Pins and Measure Digital Pins (TSM)
- Multiple Measurements on Multiple Pins (TSM)
- Source All Digital Pins, Source-Wait-Measure Each Digital Pin (TSM)
- Functional Test Using NI-Digital Pattern Driver (TSM)
- Functional Test for Multiple Registers Using NI-Digital Pattern Driver (TSM)
- Functional Test Using NI-HSDIO Hardware Compare (TSM)
- Functional Test for Multiple Registers Using NI-HSDIO (TSM)
- Instrument Multiplexed Across Sites (TSM)
- Instrument Multiplexed Across Sites, Multiple Measurements (TSM)

Related information:

- TestStand Directory Structure
- Batch Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=multisite-programming-with-switches.html language=enus -->
## TOPIC 00181: Multisite Programming with Switches (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `multisite-programming-with-switches.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/multisite-programming-with-switches.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you must share a channel between the same DUT pin on multiple sites, use a switch to control which pin the device is connected to when executing a test. The Switching example demonstrates how to write a test program that uses multiplexed routes in a multisite test program. The example uses an S

### Multisite Programming with Switches (TSM)

When you must share a channel between the same DUT pin on multiple sites, use a switch to control
 which pin the device is connected to when executing a test. The
 Switching example demonstrates how to
 write a test program that uses multiplexed routes in a multisite
 test program. The example uses an Switch Executive Virtual Device,
 but you can use the same programming methods with any switch
 instrument.

Parent topic:

Testing Multiple Sites in Parallel (TSM)

Related tasks:

- Switching (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=natively-supported-and-custom-instruments.html language=enus -->
## TOPIC 00182: Natively Supported and Custom Instruments (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `natively-supported-and-custom-instruments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/natively-supported-and-custom-instruments.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TSM natively supports the following types of instruments for LabVIEW and .NET: NI Instrument Pin Map Instrument Type Instrument Driver and Pin Map API Support Preferred Method of Interacting with Instrument Digital Pattern Instrument NIDigitalPatternInstrument NI-Digital Pattern Digital Pattern

### Natively Supported and Custom Instruments
 (TSM)

The TSM natively supports the following types of instruments for LabVIEW and .NET:

| NI Instrument | Pin Map Instrument Type | Instrument Driver and Pin Map API Support | Preferred Method of Interacting with Instrument |
| --- | --- | --- | --- |
| Digital Pattern Instrument | NIDigitalPatternInstrument | NI-Digital Pattern | Digital Pattern Editor |
| DC Power Supply or Source-Measure Unit (SMU) | NIDCPowerInstrument | NI-DCPower | Digital Pattern Editor |
| Data Acquisition and Signal Conditioning (DAQ) | NIDAQmxTask | NI-DAQmx | — |
| Digital Multimeter (DMM) | NIDmmInstrument | NI-DMM | InstrumentStudio |
| Arbitrary Waveform and Function Generator | NIFGenInstrument | NI-FGEN | InstrumentStudio |
| High-Speed Digitizer | NIScopeInstrument | NI-SCOPE | InstrumentStudio |
| High-Speed Digital I/O | NIHSDIOInstrument | NI-HSDIO | — |
| RF Signal Analyzer | NIRFSAInstrument | NI-RFSANI-RFmx | RFmx SFP |
| RF Signal Generator | NIRFSGInstrument | NI-RFSG | RFmx SFP |
| Vector Signal Transceiver | NIVSTInstrument | NI-RFSANI-RFSGNI-RFmxFPGA (LabVIEW only) | RFmx SFP |
| RF Port Module | NIRFPMInstrument | NI-RFPM | RFmx SFP |
| Relay Driver Module | NIRelayDriverModule | NI-SWITCH | Digital Pattern Editor |

Note

- The NI TestStand 2016 Semiconductor Module and later
 natively support digital pattern instruments that use the NI-Digital Pattern Driver and
 legacy digital waveform instruments that use the NI-HSDIO driver, such as the PXIe-6556.
 Use the TSM Code
 Module API that corresponds to the type of digital instrument the test system
 includes.
- Consider using the following instrument naming
 convention for semiconductor test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation ,
 for example, HSD_657x_C2_S03 ,
 where InstrumentType is an ASCII
 description of the instrument,
 ModelNumber is the model number
 as defined on ni.com,
 PXIChassisLocation uses a
 single digit to identify the PXI chassis
 ( Cx ), and
 SlotLocation uses double digits
 to identify the slot location
 ( Sxx ).

#### Custom Instruments

You can use
 other types of instruments in a pin map by using the generic <Instrument> tag in the pin map file. Refer to the example sequence
 files, pin map files, and LabVIEW code module VIs located in the <TestStand Public>\Examples\Custom
 Instruments directory for examples of using TSM pin map files and VIs to
 perform tests using instruments that TSM does not natively support.

You can create
 custom site and pin
 aware instrument panel VIs to control and measure pins during test program
 execution at a breakpoint, which can be useful during test program development and
 troubleshooting.

Parent topic:

Mapping DUT Pins to Instrument Channels (TSM)

Related concepts:

- TSM Code Module API
- Custom Instrument Panels (TSM)

Related tasks:

- Custom Instruments (TSM)

Related reference:

- Pin Map File XML Structure (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=new-features-and-changes.html language=enus -->
## TOPIC 00183: TestStand Semiconductor Module New Features and Changes

- bundle_id: `teststand-semiconductor-module`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/new-features-and-changes.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of TestStand Semiconductor Module. Discover what is new in the latest releases of TestStand Semiconductor Module.If you cannot find new features and changes for your version, it might not include user-facing

### TestStand Semiconductor Module
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of TestStand Semiconductor Module.

TestStand Semiconductor Module

Note

Release Notes

Related information:

- TSM Release Notes

#### TestStand Semiconductor Module
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in TSM 2026
 Q1.

##### New
 Features

This version of the TestStand Semiconductor Module adds support for the following features:

- Improved Runtime Data Viewer functionality.
  - Redesigned Runtime Data Viewer to sustain real-time display with a responsive UI
 throughout long test runs.
  - Improved filtering on the Summary tab. A new collapsible Filter
 Options panel allows for easier filtering without having to remember
 precise syntax options. The Filter Options panel also includes
 input validation and inline error feedback. The Filter Options 
 panel also include two new filters:
    - Alarm—Shows only alarmed tests or parts
    - SW Bin—Filters by software bin number. SW Bin is also now shown in the part
 column headers.
  - A new Settings dialog lets you set a Max History limit, implementing a cap on the
 number of batches Runtime Data Viewer retains. This feature limits memory
 usage during long test runs.
- Added Test Number Generation Override . This feature allows users to populate
 Test Numbers and detect test number conflicts.
- Added a new Station Settings option that disables tiled execution
 windows when the specified number of sites is exceeded.
- Added Trace Logging for the following operations and APIs:
  - Hardware calls
  - Sequence-level events
  - TSM Code Module .NET API
  - User-supplied calls
- Improved Alarm configuration options. Users can now view the pin groups associated with
 each pin in the new Pin Groups column. User can also now filter the
 Alarm configuration table by pin, pin group, or alarm type.
- Steps within a sequence called by a Semiconductor Sequence Call disable certain columns
 in the Tests tab. The test values defined in the Semiconductor Sequence Call determine
 which columns to override.
- Semiconductor Sequence Call step now supports autocomplete of the following
 parameters:
  - Step Names from available steps
  - Published Data Ids within the selected subsequence
- Debug Test Results Log now includes pass/fail status and alarm
 details for each step. The Debug Test Results Log also includes an improved part summary,
 with assigned binning information and alarm details.
- Added an option to enable TSM to automatically set the bin to the default Error bin.
 This action happens if no test was performed for a given part. TSM disables this option by
 default. You must explicitly enable this option.

##### Behavior Changes

- The Show last batches display filter now appears at the top of
 the Display Settings panel on the Detailed 
 tab. The filter defaults to enabled with a value of 100, improving display performance on
 long test runs.
- Step Over and Resume debug commands in TestStand Sequence Editor updated to apply to all
 executions TSM batches together. The current step Multisite Option configuration
 determines the application of this feature.

##### Additional Changes

- TSM no longer supports the ability to create a test program from a Digital Pattern
 project.

Related concepts:

- Semiconductor Module Menu
- Semiconductor Sequence Call Step
- General Tab
- Alarms Panel
- Debug Test Results Logs (TSM)
- Binning DUTs Based on Test Results (TSM)

Related tasks:

- Viewing TSM Data at Runtime

Related reference:

- Logging Trace Data

#### TSM 2024 Q3.1 Patch 2 Changes

TSM 2024 Q3.1 Patch 2 includes only bug fixes. Refer to the TSM bug fix list for a list
 of bug fixes.

#### TSM 2024 Q3.1 Patch 1 Changes

TSM 2024 Q3.1 Patch 1 includes only bug fixes. Refer to the TSM bug fix list for a list
 of bug fixes.

<!--NI_TOPIC bundle=teststand-semiconductor-module path=ni-semiconductormodule-lotsettings-data-type.html language=enus -->
## TOPIC 00184: NI_SemiconductorModule_LotSettings Data Type

- bundle_id: `teststand-semiconductor-module`
- source_path: `ni-semiconductormodule-lotsettings-data-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/ni-semiconductormodule-lotsettings-data-type.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI_SemiconductorModule_LotSettings data type defines the properties for each instance of the LotSettings sequence parameter, which the test program can access. TSM obtains the values for the NI_SemiconductorModule_LotSettings data type from the ConfigureLotSettings and GetLotSettings callback se

### NI_SemiconductorModule_LotSettings Data Type

The NI_SemiconductorModule_LotSettings data type defines the properties for each instance of the
 LotSettings sequence parameter, which
 the test program can access.

TSM obtains the values for the NI_SemiconductorModule_LotSettings data type from the ConfigureLotSettings and GetLotSettings callback sequences. The
 NI_SemiconductorModule_LotSettings data type contains the following
 properties:

- Standard —An instance of the NI_SemiconductorModule_StandardLotSettings data type. This property contains the standard lot settings TSM recognizes.
- Custom —An instance of the NI_SemiconductorModule_CustomLotSettings data type. By default, this property is an empty container. You can add properties to the NI_SemiconductorModule_CustomLotSettings data type to add custom lot settings that appear in this container.
- CustomTestConditions —An empty container. TSM adds properties to this container at run time that match the custom test conditions in the active test program configuration.

Parent topic:

Specifying Settings for the Current Lot under Test (TSM)

Related concepts:

- Specifying Settings for the Current Lot under Test (TSM)
- Accessing Lot Settings from a Test Program (TSM)
- ConfigureLotSettings Callback (TSM)
- GetLotSettings Callback (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=number-of-results-debug-test.html language=enus -->
## TOPIC 00185: Modifying Number of Results to Include

- bundle_id: `teststand-semiconductor-module`
- source_path: `number-of-results-debug-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/number-of-results-debug-test.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, the Debug Test Results Log includes all test results. You can change the default behavior. Complete the following steps to log results only when a DUT fails. Launch the Debug Test Results Log Options dialog box. Enable the Log Results Only for DUT Failures option. Complete the following

### Modifying Number of Results to Include

By default, the Debug Test
 Results Log includes all test results. You can change
 the default behavior.

Complete the following steps to log results only when a DUT fails.

1. Launch the Debug Test Results Log Options dialog box.
2. Enable the Log Results Only for DUT Failures option.

Complete the following steps to limit the number of results to display for the Debug Test Results Log.

1. Launch the Debug Test Results Log Options dialog box.
2. Enable the Limit Number of Results Displayed in Report View option.
3. Use the Display Results for Last option to specify the number of tests to display in the Report View for the Debug Test Results Log.

Parent topic:

Debug Test Results Logs (TSM)

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- Debug Test Results Log Options Dialog Box (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=number-of-results-to-stdf.html language=enus -->
## TOPIC 00186: Modifying Number of Results to Include in STDF Log Files (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `number-of-results-to-stdf.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/number-of-results-to-stdf.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, the STDF log file includes all test results. You can change the default behavior. Complete the following steps to limit the number of results to include in the STDF log file. Launch the STDF Log Options dialog box. Enable the Limit Number of Test Data Records option. Use the Log test dat

### Modifying Number of Results to Include in STDF Log Files (TSM)

By default, the STDF log file includes all test results. You can change the default behavior.

Complete the following steps to limit the number of results to include in the STDF log file.

1. Launch the STDF Log Options dialog
 box.
2. Enable the Limit Number of Test Data Records option.
3. Use the Log test data for only one out of every option to specify the number of tests to include in the STDF log file.

Parent topic:

Standard Test Data Format (STDF) Log (TSM)

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- STDF Log Options Dialog Box (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=obtain-offline-config-file.html language=enus -->
## TOPIC 00187: Obtaining an Offline Mode System Configuration File (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `obtain-offline-config-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/obtain-offline-config-file.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The Offline Mode system configuration file defines the instruments on a specific STS. On the STS you want to simulate in Offline Mode, complete the following steps to export the Offline Mode system configuration file. Launch STS Maintenance Software. Select FileExport Offline Mode System Configurati

### Obtaining an Offline Mode System Configuration File (TSM)

The Offline Mode system configuration file defines the instruments on a specific STS.

On the STS you want to simulate in Offline Mode, complete the following steps to export the Offline Mode system configuration file.

1. Launch STS Maintenance Software.
2. Select File»Export Offline Mode System
 Configuration .
3. Save the Offline Mode system configuration file in a Supporting Materials\Offline Mode
 Configurations\subdirectory 
 located in the same directory as the test program.

If you do not have access to the STS you want to simulate in Offline Mode, use one of the following methods to obtain the Offline Mode system configuration file.

- Copy the TSM Accelerometer example Offline Mode system configuration file
 ( OfflineModeSystemConfigurationForAccelerometerExample.offlinecfg )
 and modify the file to include the instruments on the STS
 you want to simulate in Offline Mode.
- Copy and modify an existing Offline Mode system configuration file to include the instruments on the STS you want to simulate in Offline Mode.
- Use the Offline Mode system
 configuration file XML structure to manually
 create the file.
- Contact NI to obtain the Offline Mode system configuration file for the specific STS you want to simulate in Offline Mode.

Parent topic:

Offline Mode Workflow (TSM)

Related reference:

- Offline Mode System Configuration File XML Structure (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=offline-config-xml.html language=enus -->
## TOPIC 00188: Offline Mode System Configuration File XML Structure (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `offline-config-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/offline-config-xml.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Offline Mode system configuration XML schema, located at <Program Files>\National Instruments\Shared\OfflineMode\SystemConfiguration.xsd, defines the following structure for an Offline Mode system configuration XML file:Legend<Root element><Element>Attribute<SystemConfiguration>schemaVersion—Spe

### Offline Mode System Configuration File XML
 Structure (TSM)

<Program Files>\National
 Instruments\Shared\OfflineMode\SystemConfiguration.xsd

| Legend |
| --- |
| <Root element> |
| <Element> |
| Attribute |

[IMAGE alt='image' src='GUID-AF15E1E5-268F-45F0-B835-47595C4B20C3-a5.png']

<SystemConfiguration>

- schemaVersion —Specifies the version of the schema file.
- <PartNumber> —Specifies the part number of the system
 configuration if the system configuration is based on an STS.
  - Value —Specifies the part number of the STS.
- <PXIChassis> —Defines a PXI chassis and the PXI
 instruments it contains.
  - Number —Specifies the number of the PXI
 chassis.
  - Model —Specifies the model of the PXI chassis.
  - <PXI> —Defines a PXI instrument and all
 components of the PXI instrument. Note Consider using
 the following instrument naming convention for semiconductor
 test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation,
 for example, HSD_6570_C2_S03, where
 InstrumentType is an ASCII description of
 the instrument, ModelNumber is the model number
 as defined on ni.com,
 PXIChassisLocation uses a single digit to
 identify the PXI chassis (Cx), and
 SlotLocation uses double digits to identify
 the slot location (Sxx).
    - Name —Specifies the name of the PXI
 instrument.
    - Model —Specifies the model of the PXI
 instrument, for example, NI PXIe-6570 .
    - Slot —Specifies the slot number of the PXI
 instrument.
    - NeedsIvi —(Optional) Specifies whether the
 PXI instrument requires IVI logical names and IVI driver
 sessions. Set the attribute value to True to create IVI
 logical names and IVI driver sessions for the PXI
 instrument.
    - <PortControlModule> —Defines a port
 control module and the port modules the port control module
 controls. A PXI instrument can contain only one port control
 module. Note Consider
 using the following instrument naming convention for
 semiconductor test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation_PCM,
 for example, VST_5840_C3_S10_PCM, where
 InstrumentType is an ASCII
 description of the instrument,
 ModelNumber is the model number as
 defined on ni.com,
 PXIChassisLocation uses a single
 digit to identify the PXI chassis (Cx),
 and SlotLocation uses double digits to
 identify the slot location
 (Sxx).
      - Name —(Optional) Specifies the name
 of the port control module. If you do not specify a
 name, Offline Mode uses the instrument naming
 convention to provide a name.
      - Model —Specifies the model of the
 port control module, for example, NI
 STS-5532 .
      - <PortModule> —Defines a port
 module, cascaded port modules, and port
 configurations. Note Consider using the following instrument naming
 convention for semiconductor test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation_PCM_PortModule,
 for example,
 VST_5840_C3_S10_PCM_PM1, where
 InstrumentType is an ASCII
 description of the instrument,
 ModelNumber is the model number
 as defined on ni.com,
 PXIChassisLocation uses a single
 digit to identify the PXI chassis
 (Cx),
 SlotLocation uses double digits
 to identify the slot location
 (Sxx), and
 PortModule uses a single digit to
 identify the port module under the port control
 module (PMx).
        - Name —(Optional) Specifies the
 name of the port module. If you do not specify a
 name, Offline Mode uses the instrument naming
 convention to provide a name.
        - Model —Specifies the model of the
 port module, for example, NI
 STS-5531 .
        - DigitalSlot —Specifies the digital
 slot number of the port module.
        - AnalogChannel —Specifies the
 analog channel of the port module.
        - <Port> —(Optional) Defines a
 port configuration. If you do not specify a port
 configuration, STS Maintenance Software uses the
 default port type (for STS-5531) or not connected
 (for STS-5533 and STS-5534).
          - Number —Specifies the number of
 the port. Port numbering starts at
 0 .
          - Type —Specifies the type of the
 port. ModelNumberSupported TypesNI STS-55310, 1, 2, 3NI5531 (Optional)NI STS-55330, 1, 2, 3NI5533_DRANI STS-55340, 1, 2, 3NI5534_RXNI5534_TX
        - <PortModule> —Defines a
 cascaded port module and port configurations. A
 port module can contain only one cascaded port
 module. Note Consider using the following instrument naming
 convention for semiconductor test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation_PCM_PortModule,
 for example,
 VST_5840_C3_S10_PCM_PM2, where
 InstrumentType is an ASCII
 description of the instrument,
 ModelNumber is the model number
 as defined on ni.com,
 PXIChassisLocation uses a single
 digit to identify the PXI chassis
 (Cx),
 SlotLocation uses double digits
 to identify the slot location
 (Sxx), and
 PortModule uses a single digit to
 identify the port module under the port control
 module (PMx).
          - Name —(Optional) Specifies the
 name of the port module. If you do not specify a
 name, Offline Mode uses the instrument naming
 convention to provide a name.
          - Model —Specifies the model of the
 port module, for example, NI
 STS-5531 .
          - DigitalSlot —Specifies the digital
 slot number of the port module.
          - <Port> —(Optional) Defines a
 port configuration. If you do not specify a port
 configuration, STS Maintenance Software uses the
 default port type (for STS-5531) or not connected
 (for STS-5533 and STS-5534).
            - Number —Specifies the number of
 the port. Port numbering starts at
 0 .
            - Type —Specifies the type of the
 port. ModelNumberSupported TypesNI STS-55310, 1, 2, 3NI5531 (Optional)NI STS-55330, 1, 2, 3NI5533_DRANI STS-55340, 1, 2, 3NI5534_RXNI5534_TX
- <MmRadioHead> —Defines a mmWave Radio Head and the
 mmWave Switches the mmWave Radio Head contains. A PXI instrument can contain
 up to two mmWave Radio Heads. Note Consider using the
 following instrument naming convention for semiconductor test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation_MMRadioHead,
 for example, IF_3622_C2_S04_RH1, where
 InstrumentType is an ASCII description of the
 instrument, ModelNumber is the model number as defined
 on ni.com, PXIChassisLocation uses a
 single digit to identify the PXI chassis (Cx),
 SlotLocation uses double digits to identify the
 slot location (Sxx), and MMRadioHead
 uses a single digit to identify the mmWave Radio Head
 (RHx).
  - Name —(Optional) Specifies the name of the mmWave
 Radio Head. If you do not specify a name, Offline Mode uses the
 instrument naming convention to provide a name.
  - Model —Specifies the model of the mmWave Radio Head,
 for example, NI mmRH-5581 .
  - Number —Specifies the number of the mmWave Radio
 Head. mmWave Radio Head numbering starts at 0 .
  - <MmSwitch> —Defines a mmWave Switch. A mmWave
 Radio Head can contain up to two mmWave Switches. Note Consider using
 the following instrument naming convention for semiconductor
 test programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation_MMRadioHead_MMSwitch,
 for example, IF_3622_C2_S04_RH1_SW1, where
 InstrumentType is an ASCII description of
 the instrument, ModelNumber is the model number
 as defined on ni.com,
 PXIChassisLocation uses a single digit to
 identify the PXI chassis (Cx),
 SlotLocation uses double digits to identify
 the slot location (Sxx),
 MMRadioHead uses a single digit to identify
 the mmWave Radio Head (RHx), and
 MMSwitch uses a single digit to identify
 the mmWave Switch (SWx).
    - Name —(Optional) Specifies the name of the
 mmWave Switch. If you do not specify a name, Offline Mode
 uses the instrument naming convention to provide a
 name.
    - Model —Specifies the model of the mmWave
 Switch, for example, NI mmSW-2795 .
    - Number —Specifies the number of the mmWave
 Switch. mmWave Switch numbering starts at
 0 .
  - <Devices> —Specifies instruments not contained
 in a PXI chassis.
    - <USB> —Defines a USB instrument. Note Consider
 using the following instrument naming convention for
 semiconductor test programs:
 InstrumentType_ModelNumber_USB,
 for example, DIO_6509_USB, where
 InstrumentType is an ASCII
 description of the instrument and
 ModelNumber is the model number as
 defined on ni.com.
      - Name —Specifies the name of the USB
 instrument.
      - Model —Specifies the model of the
 USB instrument, for example, NI
 USB-6509 .
    - <PCI> —Defines a PCI instrument. Note Consider
 using the following instrument naming convention for
 semiconductor test programs:
 InstrumentType_ModelNumber_PCI,
 for example, MIO_6221_PCI, where
 InstrumentType is an ASCII
 description of the instrument and
 ModelNumber is the model number as
 defined on ni.com.
      - Name —Specifies the name of the PCI
 instrument.
      - Model —Specifies the model of the
 PCI instrument, for example, NI
 PCI-6221 .
  - <DeviceAssociations> —Specifies associations
 between previously defined instruments.
    - <DeviceAssociation> —Defines an
 association between a parent instrument and a child
 instrument for a specific purpose.
      - ParentDeviceName —Specifies the name
 of the parent instrument. The value must match the
 value of the Name attribute of a
 <PXI> ,
 <USB> , or
 <PCI> element.
      - ChildDeviceName —Specifies the name
 of the child instrument. The value must match the
 value of the Name attribute of a
 <PXI> ,
 <USB> , or
 <PCI> element.
      - Purpose —Specifies the purpose of
 the association. The value must be
 Digitizer ,
 Baseband , LO ,
 RFConditioner ,
 RFInLO , or
 RFOutLO .

#### Example

```text
<SystemConfiguration>
   <PXIChassis Number="3" Model="NI PXIe-1095">
      <PXI Name="VST_5820_C3_S02" Model="NI PXIe-5820" Slot="2" /> 
      <PXI Name="IF_3622_C3_S04" Model="NI PXIe-3622" Slot="4">
         <MmRadioHead Model="NI mmRH-5581" Number="0">
            <MmSwitch Model="NI mmSW-2795" Number="0"/>
            <MmSwitch Model="NI mmSW-2795" Number="1"/>
         </MmRadioHead>
         <MmRadioHead Model="NI mmRH-5581" Number="1">
            <MmSwitch Model="NI mmSW-2795" Number="0"/>
         </MmRadioHead>
      </PXI>
      <PXI Name="LO_5653_C3_S06" Model="NI PXIe-5653" Slot="6" />
   </PXIChassis>
   <DeviceAssociations>
      <DeviceAssociation ParentDeviceName="IF_3622_C3_S04" ChildDeviceName="VST_5820_C3_S02" Purpose="Baseband" />
      <DeviceAssociation ParentDeviceName="IF_3622_C3_S04" ChildDeviceName="LO_5653_C3_S06" Purpose="LO" />
   </DeviceAssociations>
</SystemConfiguration>
```

Parent topic:

Offline Mode (TSM)

Related reference:

- Schema Version Policy (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=offline-mode-panel.html language=enus -->
## TOPIC 00189: Offline Mode Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `offline-mode-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/offline-mode-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The optional Offline Mode panel contains the following options: Offline Mode System Configuration File Path—Specifies the Offline Mode system configuration file you want to associate with the test program.

### Offline Mode Panel

The optional Offline
 Mode panel contains the following options:

- Offline Mode System Configuration File Path —Specifies the Offline Mode system configuration
 file you want to associate with the test
 program.

Parent topic:

Test Program Editor (TSM)

Related concepts:

- Offline Mode (TSM)

Related tasks:

- Obtaining an Offline Mode System Configuration File (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=offline-mode-requirements.html language=enus -->
## TOPIC 00190: Offline Mode Requirements (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `offline-mode-requirements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/offline-mode-requirements.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must have a valid TSM license to use Offline Mode. STS Software 19.0 or later includes the required software versions to use Offline Mode. Offline Mode requires NI DAQmx 19.1 or later and PXI Platform Services 19.1 or later. Additionally, you must install the following instrument drivers to simu

### Offline Mode Requirements (TSM)

Note

- You must have a valid TSM license to use Offline Mode.
- STS Software 19.0 or later includes the required software
 versions to use Offline Mode.

Offline Mode requires NI DAQmx 19.1 or later and PXI Platform Services 19.1 or later. Additionally, you must install the following instrument drivers to simulate the corresponding instruments:

- NI-DCPower 19.1 or later
- NI-Digital Pattern Driver 19.0 or later
- NI-DMM 19.1 or later
- NI-FGEN 19.1 or later
- NI-HSDIO 19.0 or later
- NI-RFPM 19.0 or later, including IVI shared components
- NI-RFSA 19.1 or later
- NI-RFSG 19.1 or later
- NI-SCOPE 19.1 or later
- NI-SWITCH 19.1 or later
- NI-Sync 19.0 or later

Parent topic:

Offline Mode (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=offline-mode-workflow.html language=enus -->
## TOPIC 00191: Offline Mode Workflow (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `offline-mode-workflow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/offline-mode-workflow.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to develop, run, and debug test programs only on a computer without access to NI instruments: Install STS Software 19.0 or later or ensure you meet the requirements on the computer on which you want to use Offline Mode. If necessary, copy the test program and supporting

### Offline Mode Workflow (TSM)

Complete the following steps to develop, run, and debug
 test programs only on a computer without access to NI instruments:

1. Install STS Software 19.0 or later or ensure you meet the requirements on the
 computer on which you want to use Offline Mode.
2. If necessary, copy the test program and supporting files from the STS you want
 to simulate in Offline Mode to the computer on which you want to use Offline
 Mode.
3. Obtain an Offline Mode system configuration file.
4. Copy the Offline Mode system configuration file to a Supporting
 Materials\Offline Mode
 Configurations\subdirectory located in the
 same directory as the test program on the computer on which you want to use
 Offline Mode.
5. On the computer on which you want to use Offline Mode, open the test program
 you want to execute in Offline Mode.
6. In the Offline Mode panel in Test Program
 Editor, and specify the Offline Mode system configuration file to
 associate with the test program.
7. Enable Offline Mode by clicking Enable Offline Mode[IMAGE alt='image' src='GUID-A213210F-13FD-4FD8-A9B3-8E78D25942D4-a5.png'] on the TSM toolbar.
8. Optional: 
 Configure the measurement values for tests in Semiconductor Multi Test steps. 
 Refer to *Measuring and Publishing Values in Offline Mode (TSM)*
 for more information.
9. Execute the test program.
10. Debug the test program.
11. Disable Offline Mode by clicking Disable Offline Mode[IMAGE alt='image' src='GUID-E0419593-1D7B-46BC-9CC3-46B3E3CBF2BB-a5.png'] on
 the TSM toolbar.
12. If necessary, copy the test program and supporting files from the computer on
 which you are using Offline Mode to the STS.

Parent topic:

Offline Mode (TSM)

Related concepts:

- Offline Mode Requirements (TSM)
- Debugging Test Programs in Offline Mode (TSM)
- Disabling Offline Mode (TSM)

Related tasks:

- Obtaining an Offline Mode System Configuration File (TSM)
- Enabling Offline Mode (TSM)
- Executing Test Programs in Offline Mode (TSM)
- Measuring and Publishing Values in Offline Mode (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=offline-mode.html language=enus -->
## TOPIC 00192: Offline Mode (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `offline-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/offline-mode.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Offline Mode to develop, run, and debug test programs only on a computer without access to NI instruments. Offline Mode simulates the NI instruments the test program needs. Using Offline Mode does not require changes to the test program. Use the Accelerometer example to explore Offline Mode. Usi

### Offline Mode (TSM)

Use Offline Mode to develop,
 run, and debug test programs only on a computer
 without access to NI instruments. Offline Mode simulates the NI
 instruments the test program needs. Using Offline Mode does not
 require changes to the test program. Use the Accelerometer example
 to explore Offline Mode.

Using Offline Mode can be helpful when multiple people are developing a test program at the same time and must share access to a tester, when you do not have access to a tester, or when you want to explore different test program approaches that require different instruments.

Related tasks:

- Offline Mode Workflow (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=oi-settings-table-xml.html language=enus -->
## TOPIC 00193: Operator Interface Settings Table File XML Structure (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `oi-settings-table-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/oi-settings-table-xml.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The operator interface settings table XML schema, located at <TestStand>\Components\Schemas\NI_SemiconductorModule\OISettingsTable.xsd, defines the following structure for an operator interface settings table configuration file: Legend <Root element> <Element> Attribute OISettingsTable Settings—Spec

### Operator Interface Settings Table File XML Structure (TSM)

The operator interface settings table XML schema, located at <TestStand>\Components\Schemas\NI_SemiconductorModule\OISettingsTable.xsd,
 defines the following structure for an operator interface settings table configuration
 file:

| Legend |
| --- |
| <Root element> |
| <Element> |
| Attribute |

[IMAGE alt='image' src='GUID-AF15E1E5-268F-45F0-B835-47595C4B20C3-a5.png']

OISettingsTable

- Settings —Specifies the list of settings to display in the
 table. The order of the items in this list determines the order in which the settings
 appear in the table.
  - Setting —Specifies a setting to display in a row in the
 table.
    - label —Label to
 display in the left column of the table. TSM localizes the label using the
 strings in the [NI_SEMICONDUCTORMODULE_OI_SETTINGS_TABLE] 
 section of a language resource file.
    - valueExpr —TestStand expression TSM evaluates to determine the
 value to display in the right column of the table. The expression can refer to
 LotSettings and StationSettings variables to access the current lot settings and
 station settings.
    - visibleExpr —(Optional) TestStand expression TSM evaluates to
 determine whether to display the setting in the table. The expression can refer
 to LotSettings and StationSettings variables to access the current lot settings
 and station settings. If this attribute is missing, TSM uses a default value of
 true .
    - displayFileName —(Optional) Boolean value that indicates
 whether the settings table displays a simple filename when the
 valueExpr expression evaluates to an absolute path. If this
 attribute is missing, TSM uses a default value of false .

Parent topic:

Customizing the Settings Table (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=open-lead-alarm.html language=enus -->
## TOPIC 00194: Open Lead Alarm

- bundle_id: `teststand-semiconductor-module`
- source_path: `open-lead-alarm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/open-lead-alarm.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: An open lead alarm indicates when Force leads disconnect from Sense leads in a remote sense configuration. Introduced in TestStand 2023 Semiconductor Module 2024 Q3 You must install NI-DCPower 2024 Q3 or later to enable open lead alarm. In a remote sense configuration, the difference between the out

### Open Lead Alarm

An *open lead alarm* indicates when Force leads disconnect from Sense
 leads in a remote sense configuration.

Introduced in TestStand 2023 Semiconductor Module 2024 Q3

Note

NI-DCPower 2024 Q3

In a remote sense configuration, the difference between the output and sense voltages is
 within a given proximity. NI-DCPower continuously monitors the output and sense voltages
 and reports disconnected pins to TSM when the difference between the voltages is greater
 than a threshold.

TSM supports open lead alarms for the following pins on the following hardware
 models:

| Model | Pin |  |  |  |
| --- | --- | --- | --- | --- |
| Output HI | Output LO | Sense HI | Sense LO |  |
| PXIe-4137/9 | √ | √ | — | — |
| PXIe-4147 | √ | √ | — | — |
| PXIe-4162/3 with the PXIe-416x Open-Sense Protection Accessory | √ | — | — | — |
| PXIe-4162/3 without the PXIe-416x Open-Sense Protection Accessory | √ | √ | √ | √ |

Note

PXIe-4162/3

PXIe-416x

Open-Sense Protection Accessory

If you add open-sense
 protection to PXIe-4162/3 by connecting a resistor
 between the Output HI and Sense HI pins and between the Output LO and Sense LO pins,
 TSM supports open lead alarm for the Output HI and Output LO pins.

#### Considerations for Using Open Lead Alarm

Take the following
 considerations when using open lead alarm:

- When Force leads disconnect from Sense leads, open lead alarm may not latch if the current
 level or current limit of the instrument channel is less than 1 mA . In this case, compliance alarm may latch
 to indicate an issue with the remote sense configuration.
- While PXIe-4139 allows up to 3
 V lead drop per lead, a lead drop greater than 1.5 V may trigger an open lead alarm on PXIe-4139 . To avoid false open lead
 alarm, NI recommends designing your application circuitry to ensure
 that the lead drop per lead does not exceed 1.5
 V and/or configuring the instrument driver to use a slow transient
 response.
- PXIe-4162/3 and PXIe-4147 
 share LO between channels. Disconnecting some but not all Output LO
 connections may suppress open lead alarm.

Note

SMU
 Best Practices: Understanding Compliance and Device Protection Errors

Overload
 Protection

Parent topic:

Using Alarms to Report Error Conditions at Runtime

Related concepts:

- Compliance Alarm

Related information:

- Power Supply Fundamentals: Modes of Operation, Remote Sense,
 Ripple, and Noise

<!--NI_TOPIC bundle=teststand-semiconductor-module path=open-test-limits-in-excel.html language=enus -->
## TOPIC 00195: Opening Test Limits Text Files in Microsoft Excel (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `open-test-limits-in-excel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/open-test-limits-in-excel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to open a test limits text file in Microsoft Excel. In Excel, select Open. Select All Files in the drop-down menu of file types. Select the test limits file you want to open and click the Open button. In the Text Import Wizard, select Delimited in the Original data type

### Opening Test Limits Text Files in Microsoft Excel (TSM)

Complete the following steps to open a test limits text file in Microsoft Excel.

1. In Excel, select Open . Select All Files in the drop-down menu of file types.
2. Select the test limits file you want to open and click the Open button.
3. In the Text Import Wizard, select Delimited in the Original data type option and click Next .
4. Select Tab in the Delimiters option and click Next .
5. Select General in the Column data format option and click Finish .

Alternatively, you can drag and drop a test limits text file into Excel to open the file.

When you save a modified test limits file that you opened or edited in Excel, Excel might return a message that the Excel file contains features that are not compatible with the tab-delimited text format. Click Yes in the prompt to save the workbook in text format. The Import/Export Test Limits tool is unable to parse any additional formatting information Excel adds to the file.

Note

- If a field name begins with a mathematical sign,
 Microsoft Excel might interpret the contents of the
 cell as a formula and return an error for the cell.
 To work around this issue, format the cell in Excel
 as text data.
- In some cases when a limit has a large number of digits,
 Microsoft Excel might truncate the decimal portion
 of the number. To work around this issue, format the
 columns that contain the limit numbers in Excel as
 text data.

Parent topic:

Exporting and Importing Test Limits with Text Files

Related information:

- Test Limits Text File Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=operator-interfaces.html language=enus -->
## TOPIC 00196: Operator Interfaces (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `operator-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/operator-interfaces.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TSM default LabVIEW operator interface or STS Operator Tool interface to run tests and monitor test status. You can customize each TSM default operator interface to change the permissions, menu items, and controls an operator can access. The TSM default operator interfaces do not support exe

### Operator Interfaces (TSM)

Use the TSM default LabVIEW operator
 interface or STS Operator Tool interface to run tests
 and monitor test status. You can customize
 each TSM default operator interface to change the permissions, menu items, and
 controls an operator can access.

Note

#### Default LabVIEW Operator Interface

The
 default LabVIEW operator interface contains the following features:

- Configure Station —Launch the Configure
 Station Settings dialog box.
- Configure Lot —Launch the Configure Lot
 Settings dialog box.
- Open STS Maintenance Software —Launch STS Maintenance
 Software.
- Login/Logout —Log in or out of the operator
 interface.
- Exit —Exit the operator interface.
- Command Buttons —Run, pause, or stop a single test or a
 test lot. You might notice a delay after you click the
 Pause button or the End Lot 
 button because tests in progress must complete before pausing or ending the
 lot.
- Statistics Indicator —Displays statistical information for
 a lot execution, such as cycle time and socket time or site part counts.
- Tester Status Message —Displays the status of the
 tester.
- Site Execution Data —Displays statistical and status
 information for each site.
- Active STS Software —Displays the name of the active STS
 Software installed on the system.
  - If any component in the active STS Software is missing from the system,
 an error icon appears with a tooltip directing you to open STS Version
 Selector for more information.
  - If STS Version Selector is not installed, the installed TSM version is
 displayed.
- Settings Table —Displays station and lot settings for the test
 program. You can customize this table.
- View Mid-Lot Summary —Generate and display a Mid-Lot
 Summary test report.
- View Reports —Generate and display reports for the current lot.
- Bin Table —Displays information about the binning of DUTs
 for the current lot, such as the names of the soft bins, the associated hard
 bins, and the DUT counts for each site.

#### Default STS Operator Tool Interface

The
 default STS Operator Tool interface contains the following features:

- A drop-down menu with the following options:
  - Configure Lot —Launch the Configure Lot Settings dialog box.
  - Configure Station —Launch the Configure Station Settings dialog box.
  - View Mid-Lot Summary —Generate and display a Mid-Lot Summary test report.
  - View Reports —Generate and display reports or the current lot.
  - Open STS Maintenance Software —Launch STS
 Maintenance Software.
- Command Buttons —Run, pause, or stop a single test or test
 lot. You might notice a delay after you click the Pause 
 button or the End Lot button because tests in progress
 must complete before pausing or ending the lot.
- System Status —Displays the status of the system.
- User Icon —Displays the user. Log in or out of the operator interface.
 Use the User Icon to temporarily access administrative privileges and view
 additional Failure Analysis details by clicking the 
 button.
- Yield —Displays the socket, index, and cycle times.
- Test Settings —Displays station and lot settings for the
 test program.
- Failure Analysis —Displays detailed statistics for the lot or last 10
 tests. Use the drop-down menu to specify which set of statistics to show. Use
 the or buttons to toggle between
 the list view and grid view data visualization layouts, respectively. In grid
 view, hover over each cell in the table to see a tooltip with additional
 information.

Related concepts:

- Configure Station Settings Dialog Box (TSM)
- Configure Lot Settings Dialog Box (TSM)
- Customizing the Settings Table (TSM)
- Lot Summary Reports (TSM)
- Reports and Data Logs (TSM)

Related tasks:

- Running a Test from a Default TSM Operator Interface
- Customizing Operator Interfaces (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=organization-of-mesurement-data.html language=enus -->
## TOPIC 00197: Organization of Measurement Data (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `organization-of-mesurement-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/organization-of-mesurement-data.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sometimes test code needs to process, make calculations with, or otherwise manipulate measurement data on a per-site basis before publishing it to TestStand tests for evaluation. However, typical TSM test code modules produce data organized in an array indexed by instrument session instead of by sit

### Organization of Measurement Data (TSM)

Sometimes test code needs to process, make calculations with, or otherwise manipulate measurement data on a per-site basis before publishing it to TestStand tests for evaluation. However, typical TSM test code modules produce data organized in an array indexed by instrument session instead of by site. Use the following TSM VIs and .NET methods to convert per-instrument data to per-site data. TSM always orders per-site data in the same order as the sites returned by the Get Site Numbers VI or SiteNumbers .NET property.

- Extract Pin Data VI and
 ExtractPinData .NET
 method—Extract measurement data for a single pin in the pin
 query from per-instrument measurement data and return
 per-site data. If you are using pin groups in a pin query
 and want to extract pin data for each pin in the group, you
 can use the Get Pins in Pin Group VI or GetPinsInPinGroup
 .NET method to convert a pin group into an array of pin
 names.
- Per-Instrument to Per-Site Data VI and
 PerInstrumentToPerSiteData 
 .NET method—Convert per-instrument measurement data to
 per-site data in an array organized by site and pin.
- Per-Instrument to Per-Site Pattern Results VI and
 PerInstrumentToPerSitePatternResults 
 .NET method—Convert per-instrument digital pattern results
 obtained from the NI-Digital Pattern Driver into per-site
 data.
- Per-Instrument to Per-Site Waveforms VI and
 PerInstrumentToPerSiteWaveforms 
 .NET method—Convert per-instrument digital pattern waveforms
 captured by the NI-Digital Pattern Driver into waveforms
 organized by site.
- Per-Site to Per-Instrument Waveforms VI and
 PerSiteToPerInstrumentWaveforms 
 .NET method—Convert per-site waveforms into waveforms
 organized by instrument that you can use as source waveforms
 with the NI-Digital Pattern Driver.

To publish per-site data to TestStand tests for evaluation, use the site-based polymorphic
 instances of the Publish Data VI and the
 PublishPerSite .NET method on
 the ISemiconductorModuleContext interface. These
 VIs and .NET methods expect per-site data as inputs. Like the other
 Publish Data VIs and Publish .NET methods, these VIs and .NET
 methods attach the per-site data to the appropriate test on the
 TestStand steps for evaluation.

Parent topic:

Code Module Development (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=overview-test-program-components.html language=enus -->
## TOPIC 00198: Overview of Test Program Components

- bundle_id: `teststand-semiconductor-module`
- source_path: `overview-test-program-components.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/overview-test-program-components.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: A semiconductor test program can include a pin map file, a main sequence file, subordinate sequence files, code modules, specifications, timing files, levels files, pattern files, source and capture waveforms, test limits files, a bin definitions file, and configurations. Use the Test Program Editor

### Overview of Test Program Components

A semiconductor test program can include a pin map file, a main sequence file,
 subordinate sequence files, code modules, specifications, timing files, levels files,
 pattern files, source and capture waveforms, test limits files, a bin definitions file, and
 configurations.

- Specify the pin map, bin definitions, specifications, digital pattern project,
 and test limits files
- Create and edit test program configurations
- Configure other settings for the test program

Select Semiconductor Module»Edit Test Program: <filename> or click theEdit Test Program:
 <filename> button on the TSM toolbar to
 launch the Test Program Editor for the sequence file.

Use the TestStand
 Sequence Editor to complete test program development, configuration, debugging, and
 execution tasks.

Use the following figure and table to learn about the
 components of test programs and test stations.

[IMAGE alt='image' src='GUID-565D53FE-E3E0-4E17-9609-3312BF8C6D9B-a5.png']

| Component | Description |
| --- | --- |
| TestStand Sequence Editor | The TestStand Sequence Editor is the development environment in which you create, edit, execute, and debug sequences and the tests sequences call.Complete the following steps to launch the sequence editor.(Windows 8.1/8) Click the NI Launcher tile on the Start screen and select TestStand » TestStand Sequence Editor.(Windows 7) Select Start » All Programs » National Instruments » TestStand » TestStand Sequence Editor.(Windows 10) Select Start » NI TestStand.The sequence editor launches the main window and the Login dialog box.Use the default user name, administrator, in the User Name ring control. Leave the Password field empty. You can use the TestStand User Manager to customize user setting and permissions.Click OK. |
| Pin Map | A pin map defines the instrumentation on the tester, defines the pins on the DUT, and defines how the DUT pins are connected to the tester instrumentation for each test site. Use the Pin Map Editor to view, create, modify, and save pin map files. The pin map file also serves as the channel map file.Select Semiconductor Module » Edit Pin Map File or click the Edit Pin Map File button on the TSM toolbar to launch the Pin Map Editor. Alternatively, you can select Semiconductor Module » Edit Test Program and then select Pin Map in the Test Program Editor to launch the Pin Map panel. Click the Open file for edit button to launch the Pin Map Editor. |
| Bin Definitions File | A bin definitions file defines the hardware bins and software bins, defines how the software bins relate to hardware bins, and defines the default software bins for the test program main sequence file. Use the Bin Definitions Editor to view, create, modify, and save bin definitions files.Select Semiconductor Module » Edit Bin Definitions File or click the Edit Bin Definitions File button on the TSM toolbar to launch the Bin Definitions Editor. Alternatively, you can select Semiconductor Module » Edit Test Program and then select Bin Definitions in the Test Program Editor to launch the Bin Definitions panel. Click the Open file for edit button to launch the Bin Definitions Editor. |
| Specifications Files | Specifications files define a set of symbols, or variables, and associated numeric values of DUT attributes that you can reference in test program code modules instead of using constants to set testing specifications. You can modify specifications files to set new values without changing test program files.Select Semiconductor Module » Edit Test Program and select Specifications Files in the Test Program Editor to specify one or more specifications files to load in the test program. |
| Digital Pattern Project | Use the Digital Pattern Editor with a Digital Pattern Instrument and the NI-Digital Pattern Driver software for digital testing of semiconductors, or devices under test (DUTs). Use digital pattern project files to organize and access pattern files and the following types of digital configuration files: Pin and channel maps (.pinmap) Specifications (.specs) Digital timing (.digitiming) Digital levels (.digilevels) Digital patterns (.digipat) Source waveforms (.tdms) Capture waveform configurations (.digicapture) |
| Timing Files | Timing files contain configuration components of digital pattern time sets, which define the behavior of a digital signal on a pin for a particular cycle. Timing files also include the format and edge placement that shape the digital waveform on a per-pin basis for a digital pattern instrument. Edit timing files in the Digital Pattern Editor. |
| Levels Files | Levels files contain voltage and current levels to drive and compare for digital pins and pin groups connected to an NI digital pattern instrument and for pins and pin groups connected to an NI-DCPower instrument. Edit levels files in the Digital Pattern Editor. |
| Pattern Files | Pattern files contain a collection of vectors, or instructions, to execute on an NI digital pattern instrument. Components of the binary pattern file include time sets, labels, opcodes, vector numbers, pin state data that indicates drives and compares, and comments for each vector. Edit pattern files in the Digital Pattern Editor. |
| Source and Capture Waveforms | You can source or capture a variable waveform that is not defined at compile time on an NI digital pattern instrument. Edit source waveform and capture waveform configuration files in the Digital Pattern Editor. |
| Correlation Offsets File | You can apply correlation offset values to test results on a per-site basis at run time before evaluating the test result data against limits. Use the Load Correlation Offsets Step and associated edit tab to load and apply a correlation offset file. |
| Test Program Configurations | Test program configurations define values for conditions that a test program can reference at run time and the test limits file that loads before running a test lot. A test program can use multiple configurations to implement multiple test flows using the same sequences and code modules. For example, you can create configurations for Hot and Cold flows or for QA and Production lots.Select Semiconductor Module » Edit Test Program and then select Configuration Definition in the Test Program Editor to define configuration settings. |
| Test Limits Files | Test limits files define test limits the test program loads before running a test lot. The test program replaces test limits in test steps in the sequence file with those specified in the test limits file. You can embed test limits in the sequence file to prevent viewing or tampering with the limits.Select Semiconductor Module » Edit Test Program and select Test Limits Files in the Test Program Editor to specify one or more test limits files to make available to the test program configurations. The test program configuration specifies the test limits file that loads before running a test lot. You can create a test limits file by selecting Semiconductor Module » Export Test Limits from or by clicking the Export Test Limits from button on the TSM toolbar to export test limits from a sequence file into a tab-delimited test limits text file. You can import a test limits file by selecting Semiconductor Module » Import Test Limits to or by clicking the Import Test Limits to button on the TSM toolbar to import test limits from a tab-delimited test limits text file into a sequence file. When you import test limits from a text file, you can update limits in matching tests or replace all tests in matching steps. |
| Test Conditions | Test conditions specify historical information, descriptive information, such as DUT numbers or package types, and conditions under which to test the DUTs, such as temperature or voltage. The test program can use test conditions to determine how to execute tests. For example, test conditions might dictate which steps execute, what temperature to apply to a DUT, what voltage to use, and so on.Select Semiconductor Module » Edit Test Program and select an option in the Configurations list of the Test Program Editor to edit configuration settings. |
| Main Sequence File | The main sequence file contains the sequences that define the test flow by specifying the test steps to execute and the order in which to execute them. The sequence file contains one main sequence named MainSequence and can optionally include one or more subsequences with corresponding test steps. You can use multiple sequences in a test program to keep the test code modular and organized. The ProcessSetup and ProcessCleanup sequences are special sequences that TestStand calls at certain times. TestStand calls ProcessSetup once before starting execution and calls ProcessCleanup after execution completes. Initialization and cleanup of instrumentation typically occurs within these sequences. |
| Test Steps | Test steps call test code in code modules that control the instrumentation on the tester. The test steps perform tests by comparing measurement values obtained by the code modules to test limits stored on the step and assign a bin to the DUT if the comparison fails. You can also assign a bin to the DUT when the comparison fails. Test steps are instances of the Semiconductor Multi Test step type, in which you also define test numbers and names. |
| OnSiteTestingComplete | Use the OnSiteTestingComplete callback sequence to perform actions on a DUT or on instruments after all DUT tests have completed and TSM has assigned a bin to the DUT.To use the OnSiteTestingComplete callback, add a sequence with no parameters to the test program sequence file and name the new sequence OnSiteTestingComplete. TSM calls the sequence after the MainSequence sequence, after all PAT tests complete, and after TSM assigns a bin to the DUT. Use the Get Test Information step in the callback sequence to determine the bin assigned to the DUT. You cannot use Semiconductor Multi Test steps in the OnSiteTestingComplete callback because all tests must execute before TSM assigns a bin to the DUT and before TSM calls the callback. Use the Semiconductor Action step to perform operations with the instruments and DUT.You cannot change the bin assigned to a DUT in the OnSiteTestingComplete callback. You cannot use the Set and Lock Bin step in the OnSiteTestingComplete callback.You can use the Cleanup step group of the MainSequence sequence to perform similar actions as the OnSiteTestingComplete callback if you do not need to know the bin assigned to the DUT to perform the actions. If your test program uses part average testing, you should precede those actions with a Perform Part Average Testing step, so that you can ensure that they run after all part average testing is completed. If you don't use a Perform Part Average Testing step, TSM performs part average testing after executing all step groups of the MainSequence sequence. |
| Code Modules | Use LabVIEW or .NET to create, edit, and debug test code in code modules to control the instrumentation on the tester, take measurements from the DUT, and pass the measurement values back to the test step. Code modules are program modules, such as a LabVIEW VI or a Microsoft Windows DLL, that contain one or more functions that perform a specific test or other action. |
| Station Settings | You can specify test station configuration options for the tester, such as handler configuration or data logging preferences, that apply to all test lots and that persist during restart and shutdown operations. The test program can use station information to determine how to execute tests. For example, station settings might specify the type of handler to use with the test program, which reports to generate, or whether the test station performs inline quality assurance testing. When a test station is reconfigured, such as to specify a different handler or to change the functionality of the tester, the station settings must be updated to account for the changes. You can customize how TSM obtains and processes the settings.Select Semiconductor Module » Configure Station in the TestStand Sequence Editor or click the Configure Station button in the default TSM operator interface to launch the Configure Station Settings dialog box. |
| Lot Settings | The test program can use lot information to determine how to execute tests. For example, lot settings might dictate which steps execute, what temperature to apply to a DUT, what voltage to use, and so on. You can customize how TSM obtains the settings.Select Semiconductor Module » Configure Lot in the TestStand Sequence Editor or click the Configure Lot button in the default TSM operator interface to launch the Configure Lot Settings dialog box. |
| Reporting and Data Logging | You can generate TSM reports and data logs, such as Standard Test Data Format (STDF) log files, Lot Summary Reports, and Test Results Logs. Enable and configure the corresponding TSM result processing plug-in to generate the report or data log. You can customize the destination directory and filename of the report or data log file. |
| Lot Statistics Viewer | The Lot Statistics Viewer window provides a way to view lot statistics, including per-site bin counts, while running or debugging a sequence in the sequence editor. You can also control test program execution in the Lot Statistics Viewer.Select Semiconductor Module » Show Lot Statistics Viewer or click the Show Lot Statistics Viewer button on the TSM toolbar to launch the Lot Statistics Viewer window. |
| Test Code Debugging Tools | TestStand includes several tools for debugging sequences and related components in a TestStand test program and in TSM test programs. Additionally, the TestStand Sequence Editor integrates with supported application development environments to debug code modules. |
| TestStand Execution Profiler | Use the Execution Profiler to view and record duration of steps, code modules, and other resources a multithreaded TestStand system uses over a period of time. In an effort to improve test time performance, you can optimize test time by identifying parts of the test program that take longest to execute or by identifying what shared tester resources cause throughput bottlenecks. |
| Test Program Performance Analyzer | Use the Test Program Performance Analyzer to view data TSM generates when you measure the performance of a test program. You can filter, graph, compare, and save the data in various ways to identify performance issues in a test program. |
| Operator Interfaces | Use TSM default operator interface applications to execute test sequences on a test station. The operator interface source code is available in LabVIEW and C#. You can fully customize them to meet specific needs. |
| Instrument Drivers | NI provides instrument drivers to configure, customize, and implement your instrument control applications. TSM has native support for multiple NI instrument drivers. You can integrate other NI or third-party drivers into the multisite pin map by using custom instruments. You can download TSM custom instruments for more drivers from the NI STS Technical Support Community on ni.com. You can work directly with NI services personnel contracted on your project or contact stssupport@ni.com to request to be added to the NI STS Technical Support Community.Note The NI TestStand 2016 Semiconductor Module natively supports NI digital pattern instruments that use the NI-Digital Pattern Driver and legacy digital waveform instruments that use the NI-HSDIO driver, such as the PXIe-6556. Use the TSM Code Module API that corresponds to the type of digital instrument the test system includes. |
| Soft Front Panels | Most NI modular instruments include soft front panels (SFP) to allow you to quickly configure, troubleshoot, or debug your instrument or DUT. Launch the soft front panels from MAX by selecting Tools » Soft Front Panels. TSM also provides tools to create custom debug panels in LabVIEW or C#. You can launch custom debug panels when debugging a test program, and you can use them to configure and control multiple instrument drivers.You can also use InstrumentStudio, a software-based front panel application, to monitor, control, and record measurements from supported devices. Before you create a custom debug panel, search the NI STS Technical Support Community on ni.com for an existing one. You can work directly with NI services personnel contracted on your project or contact stssupport@ni.com to request to be added to the NI STS Technical Support Community. |
| Offline Mode System Configuration File | The Offline Mode system configuration file defines the instruments on a specific STS. |
| Instrument Model Library | The Instrument Model Library is a collection of XML files that describe instruments. Instrument model description files include general information, details for connection components (channels, ports, resources), and configuration properties of the instrument and its resources. |
| Measurement and Automation Explorer | The TSM pin map defines the instruments required for a test. Measurement & Automation Explorer (MAX) helps you configure the instrument connected to the system. For a test program to execute properly, the instrument names in the pin map must correspond with instrument names configured in the system.MAX helps you complete the following tasks:Configure NI hardware and software and third-party IVI hardware and softwareView and edit instruments names in the systemCreate and edit channels, tasks, interfaces, scales, and virtual instrumentsExecute system diagnostics and run soft front panelsUpdate NI software(Windows 8.1/8) Click the NI Launcher tile on the Start screen and select NI MAX to launch MAX. (Windows 7) Select Start » NI MAX to launch MAX. |
| Handler or Prober Integration | The TSM handler/prober driver plug-in architecture enables you to write and enable handler/prober drivers. A handler/prober driver contains entry point sequences that TSM calls during execution to accomplish handler-related or prober-related tasks.Use the NI Built-in Simulated Handler Driver to simulate handler functionality without requiring access to a real handler. Custom handler/prober drivers are available from the NI STS Technical Support Community on ni.com. You can work directly with NI services personnel contracted on your project or contact stssupport@ni.com to request to be added to the NI STS Technical Support Community. |
| Part Average Testing Support | Part average testing (PAT) is a method based on statistical analysis to identify and fail parts that have characteristics significantly outside the normal distribution of other parts in the same lot. TSM does not install a default implementation of part average testing. You must use the TSM PAT plug-in architecture to customize and perform part average testing with TSM. TSM PAT plug-ins include a required PAT callback sequence file and corresponding code modules. The PAT callback sequence file contains PAT entry point sequences that TSM calls during execution to accomplish part average testing. |

Parent topic:

Getting Started with TSM

Related concepts:

- Test Program Editor (TSM)
- Mapping DUT Pins to Instrument Channels (TSM)
- Pin Map Editor (TSM)
- Binning DUTs Based on Test Results (TSM)
- Bin Definitions Editor (TSM)
- Specifications Files (TSM)
- Load Correlation Offsets Step (TSM)
- Load Correlation Offsets Tab (TSM)
- Test Settings Relationships (TSM)
- Exporting and Importing Test Limits with Text Files
- Configuration Panels
- Test Steps and Flow (TSM)
- Semiconductor Multi Test Step
- Part Average Testing (TSM)
- Get Test Information Step (TSM)
- Semiconductor Action Step
- Set and Lock Bin Step (TSM)
- Perform Part Average Testing Step (TSM)
- Specifying Settings for the Current Test Station (TSM)
- Specifying Settings for the Current Lot under Test (TSM)
- Reports and Data Logs (TSM)
- Standard Test Data Format (STDF) Log (TSM)
- Lot Summary Reports (TSM)
- Debug Test Results Logs (TSM)
- Specifying Report and Data Log Filenames (TSM)
- Lot Statistics Viewer (TSM)
- Debugging TestStand Test Programs
- Debugging TSM Test Programs
- Test Time Reduction and Test System Performance Improvements (TSM)
- Test Program Performance Analyzer Filters (TSM)
- Test Program Performance Analyzer Graphs (TSM)
- Comparing Data in the Test Program Performance Analyzer (TSM)
- Saving Data in the Test Program Performance Analyzer (TSM)
- Operator Interfaces (TSM)
- TSM Code Module API
- Offline Mode (TSM)
- Model-Based Instruments (TSM)
- Configuring Handler or Prober Support for a Test Program (TSM)
- NI Built-in Simulated Handler Driver (TSM)
- Part Average Testing Plug-In Architecture (TSM)
- Part Average Testing Entry Points (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins
- Measuring Test Program Performance (TSM)
- Custom Instruments (TSM)

Related reference:

- Semiconductor Module Toolbar Buttons

Related information:

- Managing Users
- Code Modules

<!--NI_TOPIC bundle=teststand-semiconductor-module path=parallel-for-loops.html language=enus -->
## TOPIC 00199: Parallel For Loops (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `parallel-for-loops.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/parallel-for-loops.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you obtain multiple sessions, you will usually use a parallel For Loop to control the instruments in parallel to increase multisite efficiency. You do not need to use a parallel For Loop for NI-Digital Pattern, NI-SCOPE, or NI-DCPower pin queries if all instruments or channels belong to the sam

### Parallel For Loops (TSM)

When you obtain multiple sessions, you will usually use a parallel For Loop to control the instruments in parallel to increase multisite efficiency. You do not need to use a parallel For Loop for NI-Digital Pattern, NI-SCOPE, or NI-DCPower pin queries if all instruments or channels belong to the same group in the pin map file. By default, TSM groups all NI-Digital Pattern instruments into the same NI-Digital Pattern instrument group, all NI-SCOPE instruments into the same NI-SCOPE instrument group, and all NI-DCPower channels into the same NI-DCPower channel group. You can edit instrument or channel groups in the Pin Map Editor.

| LabVIEW | Right-click a For Loop and select Configure Iteration Parallelism from the context menu to create a parallel For Loop. Index the session and channel list arrays in the For Loop to access each instrument in parallel. |
| --- | --- |
| .NET (C#) | One option for parallel For Loops in .NET is the System.Threading.Tasks.Parallel.For method. The following example demonstrates how to use this method to perform a measurement with each instrument session in parallel. public static void ExampleCodeModule(ISemiconductorModuleContext semiconductorModuleContext, string dcPowerPins) { NIDCPower[] dcPowerSessions; string[] dcPowerChannelStrings; semiconductorModuleContext.GetNIDCPowerSessions(dcPowerPins, out dcPowerSessions, out dcPowerChannelStrings); var measurements = new double[dcPowerSessions.Length]; Parallel.For(0, dcPowerSessions.Length, i => { measurements[i] = PerformMeasurement(dcPowerSessions[i], dcPowerChannelStrings[i]); }); } |

Parent topic:

Code Module Development (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=parametric-i-v-instrument-panel.html language=enus -->
## TOPIC 00200: Parametric I/V Instrument Panel (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `parametric-i-v-instrument-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/parametric-i-v-instrument-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates how to use the custom instrument panel infrastructure to provide pin-aware debugging and control of NI-DCPower and NI-Digital SMU, power supply, and PPMU instruments during execution of a TSM test sequence. Example File Locations <TestStand Public> \Examples\Custom Instrume

### Parametric I/V Instrument Panel (TSM)

This example demonstrates how to use the custom instrument panel infrastructure
 to provide pin-aware debugging and control of NI-DCPower and NI-Digital SMU, power
 supply, and PPMU instruments during execution of a TSM test sequence.

| Example File Locations | <TestStand Public> \\Examples\\Custom Instrument Panels\\LabVIEW\\Parametric I V Instrument Panel |
| --- | --- |
| Installed File Locations | <TestStand Public> \\Components\\Modules\\NI_SemiconductorModule\\CustomInstrumentPanels\\Parametric I V Instrument Panel |
| Highlighted Features | Custom instrument panels |
| Major API | NI-DCPower NI-Digital Pattern Driver (PPMU only) |
| Prerequisites | NI-Digital Pattern Driver NI-DCPower |

Complete the following steps to use this example.

- Open <TestStand
 Public> \Examples\NI_SemiconductorModule\Accelerometer\LabVIEW\Accelerometer.seq 
 and set a breakpoint on a step in the Main section of the
 MainSequence sequence.
- Click the Start Lot button on the TSM toolbar to run the test program.
- When the execution stops at the breakpoint, select Semiconductor Module»Custom Instrument Panels»Parametric I/V Instrument Panel to launch the corresponding custom instrument panel VI.
- In the Parametric I/V Instrument Panel VI, select Site number or
 System pins to update the available pins list and then select a
 pin.
- Update the hardware settings controls to change the state of the pin. The custom
 instrument panel immediately commits the changes you make to the pin you selected. The
 hardware settings controls display the current state of the pin.
  - The custom instrument panel VI uses the configured settings to continuously run a
 software-timed current (I) and voltage (V) measurement on the selected pin, performing
 the measurement approximately once every 500ms.
  - The Current and Voltage charts display
 the measurement results and provide a historical view of the state of the selected
 pin. Note You can click
 the Pause button to pause the continuous measurements.
 Clicking the Pause button does not change the state of the
 selected pin and pauses only the measurements the custom instrument panel VI
 performs on the selected pin.
- Click the Close (X) button in the title bar of the Parametric I/V
 Instrument Panel VI to end the execution of the custom instrument panel VI.

Parent topic:

TSM Example Programs

Related concepts:

- Custom Instrument Panels (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=part-average-testing-environment-settings.html language=enus -->
## TOPIC 00201: Part Average Testing Environment Settings (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `part-average-testing-environment-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/part-average-testing-environment-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The part average testing (PAT) environment settings define characteristics of the PAT algorithm TSM uses to customize the TSM environment for the PAT algorithm. Specify these settings in the following properties in the FileGlobals.PartAverageTestingAlgorithmDescription.EnvironmentSettings container

### Part Average Testing Environment Settings (TSM)

The part average testing (PAT) environment settings define characteristics of the PAT algorithm TSM uses to customize the TSM environment for the PAT algorithm. Specify these settings in the following properties in the FileGlobals.PartAverageTestingAlgorithmDescription.EnvironmentSettings container property:

- TestNumberOffsetForPinGroupTests —Specifies the offset that the Semiconductor Multi Test step adds to the
 Dynamic PAT Test Number , to
 the Static PAT Test Number , and to
 the Base PAT Test Number when the
 step creates additional tests for pins in a pin group. When
 a test specifies a pin group in the
 Pin column in the Tests table
 on the Tests tab, the Tests table
 inserts a test for each pin in the pin group. The
 Test Number column is
 computed by adding the test number specified for the pin
 group test to the zero-based index of the pin in the pin
 group. Although the Part Average Testing tab does not
 display the inserted tests for pin group tests, if part
 average testing is enabled for a test that specifies a pin
 group, the step creates PAT tests for each inserted test.
 The values for the Dynamic PAT Test Number, Static PAT Test
 Number, and Base PAT Test Number are computed by adding the
 test number specified by the pin group test to the product
 of the zero-based index of the pin in the pin group and the
 value of
 TestNumberOffsetForPinGroupTests .
- AllowExecutionWithDefaultSettingValues —Indicates whether TSM executes a test program that does not include any PAT algorithm settings. TSM uses this setting only when no PAT algorithm settings exist in the test program. When this setting is True , TSM uses the default values for PAT algorithm settings stored in the FileGlobals.PartAverageTestingAlgorithmDescription.AlgorithmSettings property in the PAT callback sequence file. When this setting is False , TSM reports a run-time error.
- EnablePerformPartAverageTestingStep —Enables
 the Perform Part Average Testing
 step in the PAT algorithm. By default, this setting is False
 and the Perform Part Average Testing step is disabled.
- StepSettingsPaneUI —Contains Boolean properties that specify which of the following columns to display on the Part Average Testing tab of the Semiconductor Multi Test step.
  - EnableBaseTestNumberColumn —Specifies whether the PAT Base Test Number column is visible.
  - EnableDynamicEnableColumn —Specifies whether the Enable Dynamic PAT column is visible.
  - EnableDynamicTestNumberColumn —Specifies whether the Dynamic PAT Test Number column is visible.
  - EnableDynamicTestNameColumn —Specifies whether the Dynamic PAT Test Name column is visible.
  - EnableDynamicSoftwareBinColumn —Specifies whether the Dynamic PAT Software Bin column is visible.
  - EnableDynamicLowLimitColumn —Specifies whether the Dynamic PAT Low Limit column is visible.
  - EnableDynamicHighLimitColumn —Specifies whether the Dynamic PAT High Limit column is visible.
  - EnableStaticEnableColumn —Specifies whether the Enable Static PAT column is visible.
  - EnableStaticTestNumberColumn —Specifies whether the Static PAT Test Number column is visible.
  - EnableStaticTestNameColumn —Specifies whether the Static PAT Test Name column is visible.
  - EnableStaticSoftwareBinColumn —Specifies whether the Static PAT Software Bin column is visible.

Parent topic:

Part Average Testing Plug-In Architecture (TSM)

Related concepts:

- Semiconductor Multi Test Step
- Semiconductor Multi Test Edit Tabs
- Perform Part Average Testing Step (TSM)
- PAT Algorithm Settings Panel

<!--NI_TOPIC bundle=teststand-semiconductor-module path=part-average-testing.html language=enus -->
## TOPIC 00202: Part Average Testing (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `part-average-testing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/part-average-testing.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Part average testing (PAT) is a method based on statistical analysis to identify and fail parts that have characteristics significantly outside the normal distribution of other parts in the same lot. The substantial difference of these parts, which might still fall within the test program limits, co

### Part Average Testing (TSM)

Part average testing (PAT) is a method based on statistical analysis to identify and fail parts that have characteristics significantly outside the normal distribution of other parts in the same lot. The substantial difference of these parts, which might still fall within the test program limits, could indicate the potential for early part failure.

Generally, part average testing collects data from previously tested parts and compares each measurement for the current part to the mean of the previous measurements. If the measurements for the current part are outside a certain number of standard deviations from the mean, the part fails.

Refer to the *Guidelines for Part Average Testing* document (AEC - Q001 Rev-D version)
 published by the Automotive Electronics Council for more information
 about part average testing.

#### TSM
 Implementation

TSM does not install a default
 implementation of part average testing. You must use the TSM PAT plug-in architecture to
 customize and perform part average testing with TSM. TSM PAT
 plug-ins include a required PAT callback sequence file and
 corresponding code modules. The PAT callback sequence file contains
 PAT entry point sequences that TSM
 calls during execution to accomplish part average testing. Use the
 example PAT plug-in, located in the
 <TestStand
 Public>\Examples\NI_SemiconductorModule\Part Average
 Testing\Example Part Average Testing Plug-In
 directory, as a starting point for custom PAT plug-ins you
 create.

Use the PAT Algorithm Settings panel of the
 Test Program Editor to edit settings the PAT callback sequence file
 defines to customize the behavior of the algorithm execution for
 each test program.

Use the Part Average Testing tab of the Semiconductor Multi Test step to enable
 and configure part average testing for individual tests in a test
 program. The PAT environment settings determine
 which settings to display in the Part Average Testing tab.

Refer to the Part Average Testing Examples for
 information about enabling and performing part average testing (PAT)
 in a test program.

#### Execution

The first time a PAT-enabled test executes, TSM
 automatically generates one or more additional PAT tests associated
 with the original test. After executing all tests in the
 MainSequence sequence of the test program,
 TSM calls the PAT entry point sequences to customize and perform the
 PAT tests. TSM appends PAT test results to the
 MainSequence sequence test results so that
 PAT test results appear in the data logs and
 reports.

Alternatively, you can insert one or more Perform Part Average Testing steps in
 your test program to perform the PAT tests at specific points during
 program execution. Use the result from PAT tests performed by these
 steps to control the execution flow of the program. Tests that are
 performed by a Perform Part Average Testing step are not performed
 after the MainSequence sequence of the test
 program.

#### Static Limits
 File

Use the
 IPartAverageTestingStaticLimitLoader.LoadStaticLimits
 method in the
 TSM Application API
 to load a static limits file that uses the same structure as a TSM
 test limits file. To read and use limits from a different file
 format, you must implement a custom file reader and a custom data
 structure to store the limits.

Related concepts:

- Part Average Testing Plug-In Architecture (TSM)
- Part Average Testing Entry Points (TSM)
- Part Average Testing Examples (TSM)
- PAT Algorithm Settings Panel
- Test Program Editor (TSM)
- Part Average Testing Algorithm Settings (TSM)
- Semiconductor Multi Test Part Average Testing Tab
- Semiconductor Multi Test Step
- Part Average Testing Environment Settings (TSM)
- Perform Part Average Testing Step (TSM)
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=part-averge-testing-entry-points.html language=enus -->
## TOPIC 00203: Part Average Testing Entry Points (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `part-averge-testing-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/part-averge-testing-entry-points.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: At specific points during test program execution, TSM calls the following set of required part average testing (PAT) entry point sequences in the <TestStand Public>\Components\Callbacks\NI_SemiconductorModule\PartAverageTestingCallbacks.seq file. TSM calls the entry point sequences for each site ind

### Part Average Testing Entry Points (TSM)

At specific points during test program execution, TSM calls the following set
 of required part average testing (PAT) entry point sequences in the
 <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule\PartAverageTestingCallbacks.seq
 file. TSM calls the entry point sequences for each site
 independently.

- Setup—Initializes
 the PAT algorithm for the site.
- Customize—Customizes
 all the PAT tests for the site.
- Perform—Performs
 part average testing for the site by setting limits and
 evaluating PAT tests.
- Cleanup—Performs
 finalization tasks.

Parent topic:

Part Average Testing Plug-In Architecture (TSM)

Related concepts:

- Part Average Testing (TSM)
- Part Average Testing Setup Entry Point (TSM)
- Part Average Testing Customize Entry Point (TSM)
- Part Average Testing Perform Entry Point (TSM)
- Part Average Testing Cleanup Entry Point (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=part-averge-testing-plugin-architecture.html language=enus -->
## TOPIC 00204: Part Average Testing Plug-In Architecture (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `part-averge-testing-plugin-architecture.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/part-averge-testing-plugin-architecture.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the example PAT plug-in, located in the <TestStand Public>\Examples\NI_SemiconductorModule\Part Average Testing\Example Part Average Testing Plug-In directory, as a starting point for custom PAT plug-ins you create. Refer to the Part Average Testing Examples for information about enabling and pe

### Part Average Testing Plug-In Architecture (TSM)

Use the example PAT plug-in, located in the <TestStand
 Public>\Examples\NI_SemiconductorModule\Part
 Average Testing\Example Part Average Testing
 Plug-In directory, as a starting point for custom
 PAT plug-ins you create. Refer to the Part Average Testing Examples
 for information about enabling and performing part average testing
 (PAT) in a test program.

You must create and deploy the following plug-in files to implement custom part average testing (PAT) for a test program:

- A PAT callback sequence file that meets the following requirements:
  - The filename must be PartAverageTestingCallbacks.seq .
  - The file must reside in the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule 
 directory.
  - The file must include a sequence file global variable named
 PartAverageTestingAlgorithmDescription 
 that is an instance of the
 NI_SemiconductorModule_PATAlgorithmDescription
 data type to describe the environment settings and
 algorithm settings.
  - The file must implement each of the PAT entry point sequences TSM
 calls at specific points during test program
 execution.
- Code modules that implement specific PAT algorithm tasks and settings.

[IMAGE alt='image' src='GUID-FC933C92-5E59-49B5-966D-E829CC376562-a5.png']

Parent topic:

Part Average Testing (TSM)

Related concepts:

- Part Average Testing Environment Settings (TSM)
- Part Average Testing Algorithm Settings (TSM)
- Part Average Testing Entry Points (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=part-setup-entry-point.html language=enus -->
## TOPIC 00205: Part Average Testing Setup Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `part-setup-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/part-setup-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the part average testing (PAT) Setup entry point to perform initialization tasks for a single site. TSM calls the entry point for each site when starting a new lot. The Setup entry point typically obtains values of PAT algorithm settings from the test program, obtains limits for static PAT tests

### Part Average Testing Setup Entry Point (TSM)

Use the part average testing (PAT) Setup entry point to perform initialization tasks for a single site. TSM calls the entry point for each site when starting a new lot. The Setup entry point typically obtains values of PAT algorithm settings from the test program, obtains limits for static PAT tests, and initializes data structures for computing limits for dynamic PAT tests.

The Setup entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| ModelPluginConfiguration | Input | An instance of the NI_ModelPluginConfiguration data type that contains the configuration and run-time variables for the set of all active process model plug-in instances. Use this parameter to extract information, such as report paths and directories. |
| ModelData | Input | Contains information about the process model used for the lot testing. |
| SetupPartAverageTestingCallbackArgs | Input | A reference to an object that implements the ISetupPartAverageTestingCallbackArgs interface in the TSM Application API. This interface provides properties to obtain values of PAT algorithm settings, the site index, and other information. |
| PartAverageTestingRuntimeData | Output | An object reference that stores run-time data, such as test statistics, to access in the other entry points. TSM passes a reference to this object to each of the other PAT entry points. |

Parent topic:

Part Average Testing Entry Points (TSM)

Related concepts:

- TSM Application API
- Part Average Testing Entry Points (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-algorithm-settings-panel.html language=enus -->
## TOPIC 00206: PAT Algorithm Settings Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-algorithm-settings-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-algorithm-settings-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the test program settings do not match the PAT algorithm settings defined in the PAT callbacks sequence file, TSM displays one of the following buttons for you to take the appropriate action to ensure that the PAT algorithm settings match in both locations: Remove Test Program Settings—Removes th

### PAT Algorithm Settings Panel

If the test program settings do not match the PAT algorithm settings defined in the
 PAT callbacks sequence file, TSM
 displays one of the following buttons for you to take the
 appropriate action to ensure that the PAT algorithm settings match
 in both locations:

- Remove Test Program Settings —Removes the existing PAT algorithm settings from the test program if no PAT plug-in is installed or if the PAT callbacks sequence file does not include any PAT algorithm settings. If you remove the settings from the test program, you can add the settings back when you install a PAT plug-in that includes PAT algorithm settings.
- Add Test Program Settings —Adds the missing PAT algorithm settings to the test program when an installed PAT callbacks sequence file includes PAT algorithm settings.
- Update Test Program Settings —When applicable, updates the PAT algorithm settings in the test program to match the PAT algorithm settings defined in the installed PAT callbacks sequence file.

The Part Average Testing Algorithm Settings panel contains the following options when a PAT plug-in exists in the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule
 directory:

- Name —Specifies the display name of the PAT algorithm setting. If the
 PAT algorithm setting defines a
 description for the setting, a tooltip displays the
 description.
- Value —Specifies the value to use for the PAT algorithm setting in the test program.
A red exclamation point indicates that an issue exists with the value, such as when a value is higher than the maximum value of the setting. A tooltip displays the error message. If errors exist in any value, you make changes in the dialog box, and click OK , TSM commits those changes. Do not proceed without reviewing the errors for the PAT algorithm settings.

Parent topic:

Test Program Editor (TSM)

Related concepts:

- Part Average Testing Algorithm Settings (TSM)
- Part Average Testing Plug-In Architecture (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-algorithm-settings.html language=enus -->
## TOPIC 00207: Part Average Testing Algorithm Settings (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-algorithm-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-algorithm-settings.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The part average testing (PAT) algorithm settings are custom settings that define the behavior of a specific PAT algorithm. By default, a PAT algorithm does not include algorithm settings. You must create each setting for a PAT algorithm, and you must assign default values to each setting.

### Part Average Testing Algorithm Settings (TSM)

The part average testing (PAT) algorithm settings are custom settings that define the behavior of a specific PAT algorithm. By default, a PAT algorithm does not include algorithm settings. You must create each setting for a PAT algorithm, and you must assign default values to each setting.

Parent topic:

Part Average Testing Plug-In Architecture (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-cleanup-entry-point.html language=enus -->
## TOPIC 00208: Part Average Testing Cleanup Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-cleanup-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-cleanup-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the part average testing (PAT) Cleanup entry point to perform finalization tasks and to dispose of data structures. The Cleanup entry point accepts the following parameters: Parameter Type Description ModelPluginConfiguration Input An instance of the NI_ModelPluginConfiguration data type that co

### Part Average Testing Cleanup Entry Point (TSM)

Use the part average testing (PAT) Cleanup entry point to perform finalization tasks and to dispose of data structures.

The Cleanup entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| ModelPluginConfiguration | Input | An instance of the NI_ModelPluginConfiguration data type that contains the configuration and run-time variables for the set of all active process model plug-in instances. Use this parameter to extract information, such as report paths and directories. |
| ModelData | Input | Contains information about the process model used for the lot testing. |
| PartAverageTestingRuntimeData | Input | The object reference created in the Setup entry point that stores run-time data, such as test statistics. |

Parent topic:

Part Average Testing Entry Points (TSM)

Related concepts:

- Part Average Testing Setup Entry Point (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-customize-entry-point.html language=enus -->
## TOPIC 00209: Part Average Testing Customize Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-customize-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-customize-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the part average testing (PAT) Customize entry point to customize PAT tests before the PAT tests execute on a site. TSM calls this entry point if a PAT-enabled test is executed for the first time while testing the current DUT. TSM calls this entry point after executing the MainSequence sequence

### Part Average Testing Customize Entry Point (TSM)

Use the part average testing (PAT) Customize entry point to customize PAT tests before the PAT
 tests execute on a site. TSM calls this entry point if a PAT-enabled test is executed for
 the first time while testing the current DUT. TSM calls this entry point after executing the
 MainSequence sequence or when executing a Perform Part Average
 Testing step. TSM passes the PAT-enabled tests and their associated PAT tests to
 the entry point sequence.

Some typical customizations the entry point performs include setting limits on static PAT tests, setting PAT test numbers and test names, and creating PAT tests associated with a PAT-enabled test.

The Customize entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| ModelPluginConfiguration | Input | An instance of the NI_ModelPluginConfiguration data type that contains the configuration and run-time variables for the set of all active process model plug-in instances. Use this parameter to extract information, such as report paths and directories. |
| ModelData | Input | Contains information about the process model used for the lot testing. |
| PartAverageTestingRuntimeData | Input | The object reference created in the Setup entry point that stores run-time data, such as test statistics. |
| CustomizePartAverageTestingCallbackArgs | Input | A reference to an object that implements the ICustomizePartAverageTestingCallbackArgs interface in the TSM Application API. This interface provides the list of PAT-enabled tests and associated PAT tests to customize. The tests this object references include only the tests that executed for the first time while testing the current DUT. |

Parent topic:

Part Average Testing Entry Points (TSM)

Related concepts:

- Perform Part Average Testing Step (TSM)
- Part Average Testing Setup Entry Point (TSM)
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-examples.html language=enus -->
## TOPIC 00210: Part Average Testing Examples (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-examples.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-examples.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\NI_SemiconductorModule\Part Average Testing directory contains the following examples: Part Average Testing with LabVIEW Part Average Testing with .NET Example Part Average Testing Plug-In The <TestStand Public>\Examples\NI_SemiconductorModule\Part Average Testing\Exa

### Part Average Testing Examples (TSM)

The <TestStand
 Public>\Examples\NI_SemiconductorModule\Part
 Average Testing directory contains the following
 examples:

- Part Average Testing with
 LabVIEW
- Part Average Testing with
 .NET

#### Example Part Average
 Testing Plug-In

The <TestStand
 Public>\Examples\NI_SemiconductorModule\Part
 Average Testing\Example Part Average Testing
 Plug-In directory contains a part average testing
 (PAT) plug-in that you can use as a starting point for custom PAT
 plug-ins you create.

Note

The example PAT plug-in consists of the following files:

- PartAverageTestingCallbacks.seq —PAT
 callback sequence file
- PartAverageTestingAlgorithmExample.dll —.NET
 assembly that contains code modules the callback sequence
 file calls

Opening the Part Average Testing Example.seq file in
 the TestStand Sequence Editor automatically copies the example PAT
 plug-in files from the <TestStand
 Public>\Examples\NI_SemiconductorModule\Part
 Average Testing\Example Part Average Testing
 Plug-In directory to the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule
 directory. Closing the Part Average Testing
 Example.seq file removes the example PAT plug-in
 files from the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule
 directory.

Parent topic:

TSM Example Programs

Related tasks:

- Part Average Testing with LabVIEW (TSM)
- Part Average Testing with .NET (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-perform-entry-point.html language=enus -->
## TOPIC 00211: Part Average Testing Perform Entry Point (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-perform-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-perform-entry-point.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the part average testing (PAT) Perform entry point to perform the PAT tests after all the tests in the MainSequence sequence have executed on a site or during the execution of a Perform Part Average Testing step. TSM calls this entry point if any PAT-enabled tests executed while testing the curr

### Part Average Testing Perform Entry Point (TSM)

Use the part average testing (PAT) Perform entry point to perform the PAT tests after all the
 tests in the MainSequence sequence have executed on a site or during the
 execution of a Perform
 Part Average Testing step. TSM calls this entry point if any PAT-enabled tests
 executed while testing the current DUT. The Perform entry point sets the limits on dynamic
 PAT tests and executes each dynamic and static PAT test.

The Perform entry point accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| ModelPluginConfiguration | Input | An instance of the NI_ModelPluginConfiguration data type that contains the configuration and run-time variables for the set of all active process model plug-in instances. Use this parameter to extract information, such as report paths and directories. |
| ModelData | Input | Contains information about the process model used for the lot testing. |
| PartAverageTestingRuntimeData | Input | The object reference created in the Setup entry point that stores run-time data, such as test statistics. |
| CustomizePartAverageTestingCallbackArgs | Input | A reference to an object that implements the ICustomizePartAverageTestingCallbackArgs interface in the TSM Application API. This interface provides the list of PAT tests to execute. |

Parent topic:

Part Average Testing Entry Points (TSM)

Related concepts:

- Perform Part Average Testing Step (TSM)
- Part Average Testing Setup Entry Point (TSM)
- TSM Application API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-with-dotnet.html language=enus -->
## TOPIC 00212: Part Average Testing with .NET (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-with-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-with-dotnet.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates how to enable and perform part average testing (PAT) in a test program. Example File Locations <TestStand Public> \Examples\NI_SemiconductorModule\Part Average Testing\DotNET\Part Average Testing Example.seq Highlighted Features TSM PAT plug-in architecture Test Program Edi

### Part Average Testing with .NET (TSM)

This example demonstrates how to enable and perform part average testing (PAT) in
 a test program.

| Example File Locations | <TestStand Public> \\Examples\\NI_SemiconductorModule\\Part Average Testing\\DotNET\\Part Average Testing Example.seq |
| --- | --- |
| Highlighted Features | TSM PAT plug-in architecture Test Program Editor PAT Algorithm Settings panel Semiconductor Multi Test Part Average Testing tab Perform Part Average Testing step Static PAT limits file OnSiteTestingComplete callback sequence |
| Major API | TSM Application API |
| Prerequisites | Note To perform part average testing, you must place the PAT plug-in files in the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. Opening the Part Average Testing Example.seq file in the TestStand Sequence Editor automatically copies the example PAT plug-in files from the <TestStand Public>\\Examples\\NI_SemiconductorModule\\Part Average Testing\\Example Part Average Testing Plug-In directory to the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. Closing the Part Average Testing Example.seq file removes the example PAT plug-in files from the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. You must have NI-DCPower 15.1 or later installed. You do not need an NI-DCPower instrument because this example uses simulated instrument sessions. You must have .NET 4.0 support for the NI-DCPower .NET Class Libraries 1.1 or later installed. This example uses the Batch process model. Note You can view the test program in the TestStand Sequence Editor and code modules in a C# source code editor without the required NI instrument drivers installed. Visit ni.com/info and enter the Info Code NETAPIdriversupport for information about the available NI .NET APIs and the versions of the NI drivers each supports. |

Complete the steps in the following sections to learn about TSM PAT
 plug-ins, to access and modify the PAT settings, and to enable,
 disable, and configure part average testing for individual
 tests.

1. Select Semiconductor Module»Edit Test Program: Part Average Testing
 Example.seq or click the Edit Test Program:
 Part Average Testing Example.seq button
 on the TSM toolbar to launch the Test Program Editor for the
 sequence file.
2. Select the PAT Algorithm Settings panel
 and review the following settings the test program specifies
 for the PAT plug-ins to use.
  - Disable Static Part Average
 Testing —Disables all static part
 average testing for the test program.
  - Disable Dynamic Part Average
 Testing —Disables all dynamic part
 average testing for the test program.
  - Static PAT Limits
 File —Specifies a relative path to a
 file that contains static limits for all tests
 enabled for static part average testing in the
 test program. This example PAT algorithm uses the
 IPartAverageTestingStaticLimitLoader.LoadStaticLimits 
 method in the TSM Application API to load a static limits file that
 uses the same structure as a TSM test limits file.
 To read and use limits from a different file
 format, you must implement a custom file reader
 and a custom data structure to store the
 limits.
  - Statistics Type —Specifies
 the type of statistics to use to calculate dynamic
 PAT limits.
  - Window Size —Specifies how
 many measurements of previously tested DUTs to use
 to calculate the dynamic limits for the DUT
 currently being tested.
  - Early Part
 Count —Specifies how many parts in a
 lot must complete testing before considering the
 computed dynamic limits statistically valid. DUTs
 that complete testing before this value are called
 early parts. This example PAT algorithm sets the
 dynamic limits for early parts to the test program
 limits.
3. Select the Continuity step in the MainSequence 
 sequence. The example will perform part average testing for
 the tests in this step when it executes the Perform Part
 Average Testing step.
4. Click the Part Average Testing tab.
5. Add a checkmark to or remove a checkmark from the checkboxes in
 the Enable Dynamic PAT and
 Enable Static PAT 
 columns.
6. Set test numbers, test names, and software fail bins for the
 tests with dynamic or static part average testing enabled.
 Bins must be defined in the bin definitions file.
7. Enable and display the Debug Test Results Log by placing a checkmark in the
 Enabled column and in the
 Display column of the
 Result Processing dialog box.
8. Ensure that you meet the prerequisites, then click the
 Single Test button on the TSM
 toolbar to test a single part on each site.
9. Click the End Lot button.
10. Click the Report pane of the Execution window and
 review the Debug Test Results Log to see the PAT tests that
 executed during the MainSequence 
 sequence.

Parent topic:

Part Average Testing Examples (TSM)

Related concepts:

- Part Average Testing Plug-In Architecture (TSM)
- PAT Algorithm Settings Panel
- Semiconductor Multi Test Part Average Testing Tab
- Perform Part Average Testing Step (TSM)
- Part Average Testing (TSM)
- TSM Application API
- Test Program Editor (TSM)
- Binning DUTs Based on Test Results (TSM)
- Debug Test Results Logs (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

Related reference:

- Overview of Test Program Components

Related information:

- TestStand Directory Structure
- Batch Process Model
- .NET Resources for NI Hardware and Software

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pat-with-lv.html language=enus -->
## TOPIC 00213: Part Average Testing with LabVIEW (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pat-with-lv.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pat-with-lv.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: This example demonstrates how to enable and perform part average testing (PAT) in a test program. Example File Locations <TestStand Public> \Examples\NI_SemiconductorModule\Part Average Testing\LabVIEW\Part Average Testing Example.seq Highlighted Features TSM PAT plug-in architecture Test Program Ed

### Part Average Testing with LabVIEW (TSM)

This example demonstrates how to enable and perform part average testing (PAT) in
 a test program.

| Example File Locations | <TestStand Public> \\Examples\\NI_SemiconductorModule\\Part Average Testing\\LabVIEW\\Part Average Testing Example.seq |
| --- | --- |
| Highlighted Features | TSM PAT plug-in architecture Test Program Editor PAT Algorithm Settings panel Semiconductor Multi Test Part Average Testing tab Perform Part Average Testing step Static PAT limits file OnSiteTestingComplete callback sequence |
| Major API | TSM Application API |
| Prerequisites | Note To perform part average testing, you must place the PAT plug-in files in the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. Opening the Part Average Testing Example.seq file in the TestStand Sequence Editor automatically copies the example PAT plug-in files from the <TestStand Public>\\Examples\\NI_SemiconductorModule\\Part Average Testing\\Example Part Average Testing Plug-In directory to the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. Closing the Part Average Testing Example.seq file removes the example PAT plug-in files from the <TestStand Public>\\Components\\Callbacks\\NI_SemiconductorModule directory. You must have the LabVIEW Development System installed, and you must configure the LabVIEW Adapter to use the LabVIEW Development System. You must have NI-DCPower 15.1 or later installed. You do not need an NI-DCPower instrument because this example uses simulated instrument sessions. This example uses the Batch process model. Note You can view the test program in the TestStand Sequence Editor and partial code modules in LabVIEW without the required NI instrument drivers installed. Install the drivers to view the full code modules in LabVIEW. Visit ni.com/info and enter the Info Code rddrau to access the latest software drivers and updates. |

Complete the steps in the following sections to learn about TSM PAT
 plug-ins, to access and modify the PAT settings, and to enable,
 disable, and configure part average testing for individual
 tests.

1. Select Semiconductor Module»Edit Test Program: Part Average Testing
 Example.seq or click the Edit Test Program:
 Part Average Testing Example.seq button
 on the TSM toolbar to launch the Test Program Editor for the
 sequence file.
2. Select the PAT Algorithm Settings panel
 and review the following settings the test program specifies
 for the PAT plug-in to use.
  - Disable Static Part Average
 Testing —Disables all static part
 average testing for the test program.
  - Disable Dynamic Part Average
 Testing —Disables all dynamic part
 average testing for the test program.
  - Static PAT Limits
 File —Specifies a relative path to a
 file that contains static limits for all tests
 enabled for static part average testing in the
 test program. The example PAT algorithm uses the
 IPartAverageTestingStaticLimitLoader.LoadStaticLimits 
 method in the TSM Application API to load a static limits file that
 uses the same structure as a TSM test limits file.
 To read and use limits from a different file
 format, you must implement a custom file reader
 and a custom data structure to store the
 limits.
  - Statistics Type —Specifies
 the type of statistics to use to calculate dynamic
 PAT limits.
  - Window Size —Specifies how
 many measurements of previously tested DUTs to use
 to calculate the dynamic limits for the DUT
 currently being tested.
  - Early Part
 Count —Specifies how many parts in a
 lot must complete testing before considering the
 computed dynamic limits statistically valid. DUTs
 that complete testing before this value are called
 early parts. This example PAT algorithm sets the
 dynamic limits for early parts to the test program
 limits.
3. Select the Continuity step in the MainSequence 
 sequence. The example will perform part average testing for
 the tests in this step when it executes the Perform Part
 Average Testing step.
4. Click the Part Average Testing tab.
5. Add a checkmark to or remove a checkmark from the checkboxes in
 the Enable Dynamic PAT and
 Enable Static PAT 
 columns.
6. Set test numbers, test names, and software fail bins for the
 tests with dynamic or static part average testing enabled.
 Bins must be defined in the bin definitions file.
7. Enable and display the Debug Test Results Log by placing a checkmark in the
 Enabled column and in the
 Display column of the
 Result Processing dialog box.
8. Ensure that you meet the prerequisites, then click the
 Single Test button on the TSM
 toolbar to test a single part on each site.
9. Click the End Lot button.
10. Click the Report pane of the Execution window and
 review the Debug Test Results Log to see the PAT tests that
 executed during the MainSequence 
 sequence.

Parent topic:

Part Average Testing Examples (TSM)

Related concepts:

- Part Average Testing Plug-In Architecture (TSM)
- PAT Algorithm Settings Panel
- Semiconductor Multi Test Part Average Testing Tab
- Perform Part Average Testing Step (TSM)
- Part Average Testing (TSM)
- TSM Application API
- Test Program Editor (TSM)
- Binning DUTs Based on Test Results (TSM)
- Debug Test Results Logs (TSM)

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

Related reference:

- Overview of Test Program Components

Related information:

- TestStand Directory Structure
- Batch Process Model
- Latest Software Drivers and Updates

<!--NI_TOPIC bundle=teststand-semiconductor-module path=per-site-input-tab.html language=enus -->
## TOPIC 00214: Semiconductor Action Per-Site Inputs Tab

- bundle_id: `teststand-semiconductor-module`
- source_path: `per-site-input-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/per-site-input-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Per-Site Inputs tab contains a table that lists the site-specific inputs to the code module for the step. Use per-site inputs when the data you need to send to the code module has the potential to be different for each site. Specify the data value in the Per-Site Inputs table and use the TSM Cod

### Semiconductor Action Per-Site Inputs Tab

The Per-Site Inputs tab contains a table that lists the site-specific inputs to the code module for the step. Use per-site inputs when the data you need to send to the code module has the potential to be different for each site. Specify the data value in the Per-Site Inputs table and use the TSM Code Module API in the code module to obtain the data.

#### Modifying the Layout
 and Entering Data

You can modify the layout of the
 Per-Site Inputs table in the following ways:

- Use the buttons located to the right of the table to add,
 remove, or reorder per-site inputs.
- Drag column headers to reorder columns.

You can enter data in the table in the following ways:

- Enter data when a cell is highlighted.
- Click in a cell when it is highlighted.
- Double-click a cell.
- Select a value from a drop-down menu.
- Drag a variable or property from the
 Variables
 pane to a text or expression cell.

#### Columns

The
 Per-Site Inputs table contains the following columns:

| Column Name | Description |
| --- | --- |
| Pin | The pin associated with the data. If you do not specify a pin, you must specify a non-empty Input Data Id string. When you specify a valid pin map file on the Pin Map panel of the Test Program Editor, this cell contains a drop-down menu that includes the DUT and system pins the pin map defines. If the pin map file is invalid or if you do not specify a pin map file, this cell contains an editable string. |
| Input Data Id | A string that identifies the input data. If you do not specify a value for this string, you must specify a pin. |
| Data Source | An expression that specifies the input data to send to the code module. The expression must evaluate to a Boolean, number, or string value. |

The order of the per-site inputs in the table is not
 significant.

Parent topic:

Semiconductor Action Edit Tabs

Related concepts:

- TSM Code Module API
- Pin Map Panel
- Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=per-site-inputs-tab.html language=enus -->
## TOPIC 00215: Semiconductor Multi Test Per-Site Inputs Tab

- bundle_id: `teststand-semiconductor-module`
- source_path: `per-site-inputs-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/per-site-inputs-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Per-Site Inputs tab contains a table that lists the site-specific inputs to the code module for the step. Use per-site inputs when the data you need to send to the code module has the potential to be different for each site. Specify the data value in the Per-Site Inputs table and use the TSM Cod

### Semiconductor Multi Test Per-Site Inputs Tab

The Per-Site Inputs tab contains a table that lists the site-specific inputs to the code module for the step. Use per-site inputs when the data you need to send to the code module has the potential to be different for each site. Specify the data value in the Per-Site Inputs table and use the TSM Code Module API in the code module to obtain the data.

#### Modifying the Layout
 and Entering Data

You can modify the layout of the
 Per-Site Inputs table in the following ways:

- Use the buttons located to the right of the table to add,
 remove, or reorder per-site inputs.
- Drag column headers to reorder columns.

You can enter data in the table in the following ways:

- Enter data when a cell is highlighted.
- Click in a cell when it is highlighted.
- Double-click a cell.
- Select a value from a drop-down menu.
- Drag a variable or property from the
 Variables
 pane to a text or expression cell.

#### Columns

The
 Per-Site Inputs table contains the following columns:

- Pin —The pin associated with the data. If
 you do not specify a pin, you must specify a non-empty
 Input Data Id string. When
 you specify a valid pin map file on the Pin Map panel of the Test Program Editor, this cell
 contains a drop-down menu that includes the DUT and system
 pins the pin map defines. If the pin map file is invalid or
 if you do not specify a pin map file, this cell contains an
 editable string.
- Input Data Id —A string that identifies
 the input data. If you do not specify a value for this
 string, you must specify a pin.
- Data Source —An expression that specifies
 the input data to send to the code module. The expression
 must evaluate to a Boolean, number, or string value.

The order of the per-site inputs in the table is not
 significant.

Parent topic:

Semiconductor Multi Test Edit Tabs

Related concepts:

- TSM Code Module API
- Pin Map Panel
- Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=perform-analyze-with-meas.html language=enus -->
## TOPIC 00216: Perform Analysis in Parallel with Measurements (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `perform-analyze-with-meas.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/perform-analyze-with-meas.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a test program spends significant time analyzing measurement data, you might be able to improve performance by executing the analysis portion of the test in parallel with the measurement portion of the test.

### Perform Analysis in Parallel with Measurements (TSM)

If a test program spends significant time analyzing measurement data, you might be able to improve performance by executing the analysis portion of the test in parallel with the measurement portion of the test.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=perform-part-average-testing-step.html language=enus -->
## TOPIC 00217: Perform Part Average Testing Step (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `perform-part-average-testing-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/perform-part-average-testing-step.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Perform Part Average Testing step to perform part average testing for any tests that have part average testing enabled and have already executed for the current DUT. Specify the Perform Part Average Testing step settings in the PAT Algorithm Settings panel of the Test Program Editor. Tests p

### Perform Part Average Testing Step
 (TSM)

Use the Perform Part Average Testing step to perform part average testing for any
 tests that have part average testing enabled and have already executed for the current
 DUT. Specify the Perform Part Average Testing step settings in the PAT Algorithm
 Settings panel of the Test Program Editor. Tests performed by the Perform Part
 Average Testing step will not be performed after the MainSequence
 sequence of the test program executes.

Result.Status

| Status | Test Results |
| --- | --- |
| Done | The step did not execute any tests. |
| Passed | The step executed at least one test and all tests passed. |
| Failed | The step executed at least one test and at least one test failed. |
| Error | A run-time error occurred when executing the PAT algorithm. |

#### Configuring the Step

To enable the step,
 set the value of the
 PartAverageTestingAlgorithmDescription.EnvironmentSettings.EnablePerformPartAverageTestingStep
 file global variable to True in the PAT callback
 sequence file. TSM reports a run-time error if it executes a Perform Part
 Average Testing step and this step type is not enabled.

You do not need to
 configure the Step Settings pane for the step to perform part average tests. The
 step displays the test results under the Tests tab
 of the Step Settings pane during program execution, after the step executes. Once
 the test program finishes executing, the Tests tab is empty.

Parent topic:

TSM Step Types

Related concepts:

- Part Average Testing (TSM)
- Part Average Testing Algorithm Settings (TSM)
- Test Program Editor (TSM)
- Part Average Testing Plug-In Architecture (TSM)
- Tests Tab

<!--NI_TOPIC bundle=teststand-semiconductor-module path=perform-tasks-before-lot-testing-begins.html language=enus -->
## TOPIC 00218: Performing Tasks before Lot Testing Begins

- bundle_id: `teststand-semiconductor-module`
- source_path: `perform-tasks-before-lot-testing-begins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/perform-tasks-before-lot-testing-begins.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM calls the PreLotTesting callback sequence in the test program sequence file to perform tasks before starting lot testing. Pre-lot testing tasks include calibration or DIB initialization. Introduced in TSM 2024 Q3.1 TSM supports pre-lot testing only for the Batch process model. The PreLotTesting

### Performing Tasks before Lot Testing
 Begins

TSM calls the PreLotTesting callback sequence in the test program
 sequence file to perform tasks before starting lot testing. Pre-lot testing tasks include
 calibration or DIB initialization.

Introduced in TSM 2024 Q3.1

Note

PreLotTesting

ProcessSetup

PreLotTesting

Single
 Test

PreLotTesting

MainSequence

TSM does not interact with the handler or prober when running pre-lot testing. Therefore,
 the test sockets contain no parts while the PreLotTesting sequence is
 executing.

#### Treatment of Pre-Lot Testing Failures

Pre-lot Testing Failed

Pre-lot Testing Failed

- Continue testing on sites that passed pre-lot testing : TSM
 disables the sites that failed pre-lot testing and starts testing the lot.
- End lot : TSM does not test the lot.
- Rerun pre-lot testing on sites that failed : TSM disables the
 sites that passed and runs the PreLotTesting sequence with only the
 sites that failed.
  - If the sites pass, TSM re-enables all sites and continues testing the lot.
  - If any sites fail again, TSM launches the Pre-lot Testing
 Failed dialog box again.
- Rerun pre-lot testing on all sites : TSM runs the
 PreLotTesting sequence again for all sites.
  - If all sites pass, TSM continues testing the lot.
  - If any sites fail again, TSM launches the Pre-lot Testing
 Failed dialog box again.

You can customize how TSM treats pre-lot testing failures. Refer to
 *Related tasks* for more information.

#### Reports

Except for the Debug Test Results Log, TSM creates a separate report for
 the pre-lot testing. By default, the pre-lot testing reports have the same names as the lot
 reports with a _PreLotTesting suffix. You can change how TSM names
 pre-lot testing reports by customizing the GetReportFileName callback.
 Refer to *Related concepts* for more information.

If some sites fail
 pre-lot testing and you selected Continue testing on passed sites,
 the lot reports include the sites that failed pre-lot testing. Since the handler did not
 place parts on the sites that failed, the part counts and test counts are zero for those
 sites.

Related concepts:

- GetReportFileName Callback (TSM)

Related tasks:

- Customizing the Treatment of Pre-Lot Testing Failures

<!--NI_TOPIC bundle=teststand-semiconductor-module path=perform-tasks-lot-testing-complete.html language=enus -->
## TOPIC 00219: Performing Tasks when Lot Testing Completes (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `perform-tasks-lot-testing-complete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/perform-tasks-lot-testing-complete.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM calls the LotTestingComplete callback sequence to perform tasks when a lot completes testing, such as sending generated reports to a central server or displaying a message on the tester to indicate that the tester is idle. The default implementation of the LotTestingComplete callback sequence is

### Performing Tasks when Lot Testing Completes (TSM)

TSM calls the LotTestingComplete callback sequence to perform tasks when a lot completes testing, such as sending generated reports to a central server or displaying a message on the tester to indicate that the tester is idle.

The default implementation of the LotTestingComplete callback sequence is empty.
 You can override this callback to customize the tasks to perform when a
 lot completes testing. TSM calls the
 LotTestingComplete callback after all other
 process model plug-ins complete execution.

The LotTestingComplete callback sequence accepts the following parameters:

- LotSettings [In]—An instance of the NI_SemiconductorModule_LotSettings data type that contains the settings used during the lot that completed testing.
- StationSettings [In]—An instance of the NI_SemiconductorModule_StationSettings data type that contains the station settings used during the lot that completed testing.
- ModelPluginConfiguration [In]—An instance of the NI_ModelPluginConfiguration data type that contains the configuration and run-time variables for the set of all active process model plug-in instances. Use this parameter to extract information, such as report paths and directories.
- ModelData [In]—Contains information about the process model used for the lot that completed testing.

Related concepts:

- NI_SemiconductorModule_LotSettings Data Type
- NI_SemiconductorModule_StationSettings Data Type

Related tasks:

- Customizing the LotTestingComplete Callback (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=performance-meas-config-dialog.html language=enus -->
## TOPIC 00220: Test Program Performance Measurement Configuration Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `performance-meas-config-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/performance-meas-config-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor ModuleMeasure Performance of <filename> in the TestStand Sequence Editor to launch the Test Program Performance Measurement Configuration dialog box, in which you can specify settings for measuring test program performance. The changes you make persist in the dialog box. The Tes

### Test Program Performance Measurement Configuration Dialog Box (TSM)

Select Semiconductor Module»Measure Performance of<filename> in the TestStand Sequence Editor to launch the Test
 Program Performance Measurement Configuration dialog box, in which
 you can specify settings for measuring test program performance. The
 changes you make persist in the dialog box.

The Test Program Performance Measurement Configuration dialog box contains the following options:

- Test Program —Displays the test program on which to measure performance.
- Process Model —Displays the process model the test program uses.
- Operator Interface Path —By default, specifies the absolute path to the default LabVIEW operator interface TSM installs. Use the browse button to navigate to a custom operator interface to use instead of the default TSM LabVIEW operator interface or paste the path to the executable into the control. This control cannot be empty.
- Output File Directory —Specifies the directory in which to write the log files. Use the browse button to navigate to a custom output directory or paste the path to the directory into the control. The path must be an absolute path.
- Number of Parts Per Site —Specifies the number of parts to run on each site.
- Site Configurations —Each row corresponds to a lot and contains a
 comma-separated list of integers or integer ranges that
 specifies the sites the lot contains, for example: 0, 1,
 2-7. The sites must exist in the pin map. Use the
 Add Site Configuration and
 Delete Site Configuration 
 buttons to add and delete rows. TSM ignores empty rows at
 run time. Note If
 you are using the Sequential process model,
 Site Configurations
 displays a single configuration that contains a
 single site (0). If you switch back to using the
 Batch process model, Site
 Configurations displays the previous
 set of configurations.
- Configure Lot Settings —Launches the Configure Lot Settings dialog box. If you have not configured lot settings for the active test program, TSM disables the OK button and displays a warning to prompt you to configure the lot settings.

Click the expand/collapse button to view or hide the Advanced section of the dialog box, which includes the following option that configures the testing environment to simulate a production environment:

- Operator Interface Command Line —The default command line is /NoCompatibilityIssuesDialog /run "Measure Test Program Performance"
 "<TestStand>\Components\Modules\NI_SemiconductorModule\NI_SemiconductorModule_PerformanceMeasurement.seq"
 /quit , which configures the execution environment. If
 you use a custom sequence file instead of the default NI_SemiconductorModule_PerformanceMeasurement.seq file to
 configure the environment for performance testing, modify the command line to call the
 custom sequence file. Note If
 you use an operator interface with a custom command-line parser, modify the command-line
 arguments to ensure that the operator interface calls the Measure Test Program
 Performance sequence of the NI_SemiconductorModule_
 PerformanceMeasurement.seq file located in the <TestStand>\Components\Modules\NI_SemiconductorModuledirectory.
- Reset to Default —Reverts the value of the Operator Interface Command Line option to use the default command-line value.
- Allow execution with LabVIEW Development Environment Adapter —By default,
 when you select the LabVIEW Development Environment adapter in TestStand, the adapter
 temporarily switches to use the LabVIEW Run-Time Engine to simulate production
 performance. Enabling this option disables the switch to the LabVIEW Run-Time Engine,
 allowing performance measurement with the LabVIEW Development Environment adapter. This
 increases test time. This option is disabled if the LabVIEW adapter is already set to use
 the LabVIEW Run-Time Engine. Note Changing any option under
 Advanced causes the section to remain expanded until the next
 time the dialog box is opened.

Parent topic:

Test Program Performance Analyzer (TSM)

Related concepts:

- Test Program Performance Measurement Data Logs (TSM)
- Configure Lot Settings Dialog Box (TSM)
- Test Program Performance Measurement Testing Environment (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=performance-meas-config-dialog_2.html language=enus -->
## TOPIC 00221: Test Program Performance Measurement Configuration Dialog Box (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `performance-meas-config-dialog_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/performance-meas-config-dialog_2.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Semiconductor ModuleMeasure Performance of <filename> in the TestStand Sequence Editor to launch the Test Program Performance Measurement Configuration dialog box, in which you can specify settings for measuring test program performance. The changes you make persist in the dialog box. The Tes

### Test Program Performance Measurement Configuration Dialog Box (TSM)

Select Semiconductor Module»Measure Performance of<filename> in the TestStand Sequence Editor to launch the Test
 Program Performance Measurement Configuration dialog box, in which
 you can specify settings for measuring test program performance. The
 changes you make persist in the dialog box.

The Test Program Performance Measurement Configuration dialog box contains the following options:

- Test Program —Displays the test program on which to measure performance.
- Process Model —Displays the process model the test program uses.
- Operator Interface Path —By default, specifies the absolute path to the default LabVIEW operator interface TSM installs. Use the browse button to navigate to a custom operator interface to use instead of the default TSM LabVIEW operator interface or paste the path to the executable into the control. This control cannot be empty.
- Output File Directory —Specifies the directory in which to write the log files. Use the browse button to navigate to a custom output directory or paste the path to the directory into the control. The path must be an absolute path.
- Number of Parts Per Site —Specifies the number of parts to run on each site.
- Site Configurations —Each row corresponds to a lot and contains a
 comma-separated list of integers or integer ranges that
 specifies the sites the lot contains, for example: 0, 1,
 2-7. The sites must exist in the pin map. Use the
 Add Site Configuration and
 Delete Site Configuration 
 buttons to add and delete rows. TSM ignores empty rows at
 run time. Note If
 you are using the Sequential process model,
 Site Configurations
 displays a single configuration that contains a
 single site (0). If you switch back to using the
 Batch process model, Site
 Configurations displays the previous
 set of configurations.
- Configure Lot Settings —Launches the Configure Lot Settings dialog box. If you have not configured lot settings for the active test program, TSM disables the OK button and displays a warning to prompt you to configure the lot settings.

Click the expand/collapse button to view or hide the Advanced section of the dialog box, which includes the following option that configures the testing environment to simulate a production environment:

- Operator Interface Command Line —The default command line is /NoCompatibilityIssuesDialog /run "Measure Test Program Performance"
 "<TestStand>\Components\Modules\NI_SemiconductorModule\NI_SemiconductorModule_PerformanceMeasurement.seq"
 /quit , which configures the execution environment. If
 you use a custom sequence file instead of the default NI_SemiconductorModule_PerformanceMeasurement.seq file to
 configure the environment for performance testing, modify the command line to call the
 custom sequence file. Note If
 you use an operator interface with a custom command-line parser, modify the command-line
 arguments to ensure that the operator interface calls the Measure Test Program
 Performance sequence of the NI_SemiconductorModule_
 PerformanceMeasurement.seq file located in the <TestStand>\Components\Modules\NI_SemiconductorModuledirectory.
- Reset to Default —Reverts the value of the Operator Interface Command Line option to use the default command-line value.
- Allow execution with LabVIEW Development Environment Adapter —By default,
 when you select the LabVIEW Development Environment adapter in TestStand, the adapter
 temporarily switches to use the LabVIEW Run-Time Engine to simulate production
 performance. Enabling this option disables the switch to the LabVIEW Run-Time Engine,
 allowing performance measurement with the LabVIEW Development Environment adapter. This
 increases test time. This option is disabled if the LabVIEW adapter is already set to use
 the LabVIEW Run-Time Engine. Note Changing any option under
 Advanced causes the section to remain expanded until the next
 time the dialog box is opened.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=performance-meas-data-logs.html language=enus -->
## TOPIC 00222: Test Program Performance Measurement Data Logs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `performance-meas-data-logs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/performance-meas-data-logs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you measure test program performance, TSM generates a performance log file with the data gathered during the series of test executions and a summary log file that describes the testing environment. The Test Program Performance Analyzer uses the performance log file to analyze and display the pe

### Test Program Performance Measurement Data Logs (TSM)

When you measure test program performance, TSM generates a performance log file with the data gathered during the series of test executions and a summary log file that describes the testing environment.

The Test Program Performance Analyzer uses the performance log file to analyze and display the performance measurement data.

#### Performance Log
 File

The performance log file contains measurement data for each execution in the
 performance measurement operation. The performance log file stores data in a comma-separated
 values (.csv) format and includes the following information about each
 step in the test program execution.

| Column Name | Notes |
| --- | --- |
| NumberOfSites | Use this information to distinguish among the site configurations the log file includes. |
| Site | — |
| SequenceFile | Blank for entries in the log file that correspond to the steps in the process model, such as the MainSequence Callback step. |
| Sequence | Blank for entries in the log file that correspond to the steps in the process model, such as the MainSequence Callback step. |
| StepGroup | Setup, Main, or Cleanup |
| StepName | — |
| StepId | — |
| StepType | — |
| SitesTested | String that contains a comma-separated list of sites on which the code module executed. This value corresponds to the subsystem information on the Options tab of a Semiconductor Action or Multi Test step. |
| LoopIndex | 1-indexed number of the batches tested during the execution. |
| ModuleTime | Execution time for the code module associated with the step. This value is 0 if the step does not call a code module. |
| TotalTime | Total execution time for the step, including the module time if the step calls a code module. For Sequence Call steps, includes the execution time of the entire sequence called from the step. |
| Status | Result.Status for each step, such as Passed, Failed, Done, or Error. |
| SocketTime | Total execution time of the main sequence. This value is logged only once for each loop of the main sequence and is left blank for rows that correspond to individual steps. |

#### Summary Log
 File

The summary log file contains information about the
 testing environment. The summary log file stores data in a plain
 text (.txt) format and includes the following information:

- Test Program
- Active Configuration
- Offline Mode
- Process Model Path
- Operator Interface
- Operator Interface Arguments
- LabVIEW Adapter Server
- Enabled Result Processors
- Notes
- TestStand Version
- Number of Sites

Parent topic:

Test Program Performance Analyzer (TSM)

Related concepts:

- Test Program Performance Analyzer (TSM)
- Semiconductor Action Step
- Semiconductor Multi Test Step
- Offline Mode (TSM)

Related tasks:

- Measuring Test Program Performance (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=performance-meas-test-env.html language=enus -->
## TOPIC 00223: Test Program Performance Measurement Testing Environment (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `performance-meas-test-env.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/performance-meas-test-env.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To ensure that the testing environment is consistent while you measure test program performance, the NI_SemiconductorModule_PerformanceMeasurement.seq file configures the environment in the following ways when TSM launches the operator interface you specify to simulate a production environment. The

### Test Program Performance Measurement Testing Environment (TSM)

To ensure that the testing environment is consistent while you measure test program performance,
 the
 NI_SemiconductorModule_PerformanceMeasurement.seq
 file configures the environment in the following ways when TSM
 launches the operator interface you specify to
 simulate a production environment. The sequence file is located in
 the <TestStand>\Components\Modules\NI_SemiconductorModule
 directory.

- Configures the LabVIEW Adapter to use the LabVIEW Run-Time Engine. After testing completes, restores the original setting for the adapter.
- Enables or disables result processors. After testing completes, restores the original settings for the result processors.
  - Enables the following result processors:
    - NI_SemiconductorModule_LotSummaryReportGenerator.seq
    - NI_SemiconductorModule_StdfGenerator.seq
  - Disables the following result processors:
    - NI_DatabaseLogger.seq
    - NI_OfflineResultsGenerator.seq
    - NI_ReportGenerator.seq
    - NI_SemiconductorModule_LotTestingComplete.seq
    - NI_SemiconductorModule_TestResultsLogGenerator.seq
- The Test Program Performance Analyzer uses its own simulated handler driver and does not support the NI Built-in Simulated Handler Driver or any custom handler drivers.

Parent topic:

Test Program Performance Analyzer (TSM)

Related concepts:

- Test Program Performance Measurement Configuration Dialog Box (TSM)
- NI Built-in Simulated Handler Driver (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=performing-inline-qa-testing.html language=enus -->
## TOPIC 00224: Performing Inline Quality Assurance Testing (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `performing-inline-qa-testing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/performing-inline-qa-testing.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A tester might need to perform periodic or random quality assurance (QA) tests to identify errors or unintended behavior in some component of the test system. Typically, a QA test specifies limits that are wider than those of a normal test. Because an actual test might pass with a value that is very

### Performing Inline Quality Assurance Testing (TSM)

A tester might need to perform periodic or random quality assurance (QA) tests to identify errors or unintended behavior in some component of the test system. Typically, a QA test specifies limits that are wider than those of a normal test. Because an actual test might pass with a value that is very close to a limit, wider limits ensure that an inline QA failure occurs only when a problem exists with the tester.

A technician or operator might run a dedicated QA test—separate from a standard test sequence—on a tester as part of the manufacturing process or to perform an audit on the test system. However, in some cases, the test engineer might want to perform inline QA testing, in which one or more QA tests exists within a standard test sequence.

#### TSM
 Implementation

Use a station setting TSM provides to
 enable or disable inline QA testing functionality for the test
 station. When you enable inline QA testing for the test station, you
 must specify an inline QA algorithm that specifies the inline QA
 testing behavior. In the test program main sequence file, insert an
 Inline QA Test Block step to specify a
 block of steps that perform inline QA testing only under certain
 conditions. TSM maintains a queue of inline QA states, where each
 state is a Boolean value that indicates whether to perform inline QA
 for a DUT.

The steps within the inline QA test block execute
 only when all of the following conditions are true:

- The StationSettings.Standard.InlineQAEnabled
 Boolean property is True .
- The Step.ConditionExpr property of the Inline
 QA Test Block step specifies an expression that evaluates to
 True .
- The next inline QA state, which is the next Boolean value
 removed from the TSM queue of inline QA states, is
 True . Note If multiple inline QA test blocks exist
 in the sequence, only the first one that executes
 dequeues the inline QA state for the DUT. Subsequent
 inline QA test blocks use the inline QA state that
 the first inline QA test block dequeued.

Complete the following steps to implement inline QA testing
 functionality for a test program.

1. Create an inline QA algorithm sequence
 file and edit the GetNextInlineQAStateQueueItems callback
 sequence.
2. Enable inline QA on the test
 station and specify the inline QA algorithm
 sequence file you created in step 1 as the inline QA
 algorithm sequence file to use for the test station.
3. Insert a single Inline QA Test Block step instance in the
 MainSequence sequence of the test
 program main sequence file.
4. Insert additional steps within the Inline QA Test Block that
 call code modules that perform the inline QA tests.

Note

- The default expression for the
 Step.ConditionExpr property
 evaluates to True when the
 MainSequence sequence has not yet
 encountered a sequence failure. You can modify the
 expression the Step.ConditionExpr 
 property specifies to customize the condition for
 which the inline QA test block executes.
- You can place multiple Inline QA Test Block step type
 instances at any location in any test sequence, but
 NI recommends that you place only a single instance
 after all standard test steps in the
 MainSequence sequence of the test
 program main sequence file.

Related concepts:

- Inline QA Test Block Step (TSM)
- Accessing Station Settings from a Test Program (TSM)
- GetNextInlineQAStateQueueItems Callback (TSM)
- Enabling Inline QA on the Test Station (TSM)

Related tasks:

- Creating an Inline QA Algorithm Sequence File (TSM)

Related information:

- Expressions

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-and-session-queries.html language=enus -->
## TOPIC 00225: Pin and Session Queries (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-and-session-queries.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-and-session-queries.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI instrument drivers refer to sessions and channel lists rather than to sites and pins. When you take a measurement using an NI instrument driver, you must first perform a pin query to look up the associated instrument sessions and channel lists. To conduct a pin query, you must first know the type

### Pin and Session Queries (TSM)

NI instrument drivers refer to sessions and channel lists rather than to sites and pins. When you take a measurement using an NI instrument driver, you must first perform a pin query to look up the associated instrument sessions and channel lists.

To conduct a pin query, you must first know the type of instrument to which the pins are connected. Each instrument type has a corresponding pin query VI or .NET method.

The following figure and code snippet shows how to use the Pin(s) To NI-DCPower Session(s)
 polymorphic VI or the GetNIDCPowerSessions .NET
 method to obtain the associated sessions and channel lists for a set
 of pins using an NI-DCPower instrument.

| LabVIEW |  |
| --- | --- |
| .NET (C#) | public static void ExampleCodeModule(ISemiconductorModuleContext semiconductorModuleContext, string dcPowerPins) { NIDCPower[] dcPowerSessions; string[] dcPowerChannelStrings; semiconductorModuleContext.GetNIDCPowerSessions(dcPowerPins, out dcPowerSessions, out dcPowerChannelStrings); } The Semiconductor Module context provides information to the VI about which sites the subsystem includes. The pin query returns an array of instrument sessions and channel lists. Each element with the same index in each array is associated. The pin query returns the order of the sessions and channels in a deterministic manner based on the active sites and pins. Different instrument types might return different outputs depending on the information required to control the instrument. For example, some instruments do not have channels and thus do not return a channel list. Other instruments might return multiple session arrays. |

#### LabVIEW Polymorphic Instances of Pin(s) to
 Session(s) VIs

The Pin(s) to Session(s) VIs offer a subset
 of the following polymorphic instances:

- Multiple Pins - Multiple Instruments or Sessions
- Single Pin - Multiple Instruments or Sessions
- Multiple Pins - Single Instrument or Session
- Single Pin - Single Instrument or Session

Depending on the instrument type, some of these options might not be
 available. If you operate on multiple pins, you must select the
 Multiple Pins options. If you operate on a single pin, select the
 Single Pin options. You can build the pin name into an array of
 strings and use the Multiple Pin options if a Single Pin option is
 not available for an instrument type.

You can use different
 instances of the same VI in multiple locations of a code module. For
 example, if you want to set the voltage of all pins to
 0, you can use the Multiple Pins - Multiple
 Sessions instance to access the instrumentation. If you then want to
 force a current on a single pin, use the Single Pin - Multiple
 Sessions instance of the VI.

Note

#### .NET Method Overloads

The .NET
 API provides overloads for the pin query methods. The overloaded
 parameters allow you to specify a single pin or an array of pins and
 output a single instrument session or an array of instrument
 sessions. The type of the return value depends on which overload you
 use and provides a publish method that matches the pin query method
 overload. Depending on the instrument type, some method overloads
 might not be available.

You can use different method
 overloads in multiple locations of a code module. For example, if
 you want to set the voltage of all pins to 0, you can use the
 overload that takes an array of pins and outputs an array of
 sessions to access the instrumentation. If you then want to force a
 current on a single pin, use the overload that takes a single pin
 and outputs an array of sessions.

Note

#### Single Sessions or Multiple
 Sessions

Select a Single Session VI instance or the .NET
 method overload that outputs a single session only under the
 following conditions:

- You are using a NI-Digital Pattern pin query and all NI-Digital
 Pattern instruments belong to the same group in the pin map
 file. By default, TSM groups all NI-Digital Pattern
 instruments together.
- You are using a NI-SCOPE pin query and all NI-SCOPE instruments
 belong to the same group in the pin map file. By default,
 TSM groups all NI-SCOPE instruments together.
- You are using a NI-DCPower pin query and all NI-DCPower channels
 belong to the same group in the pin map file. By default,
 TSM groups all NI-DCPower channels together.
- You use only a single session of a given type for the
 tester.
- You know that the instruments of that type are and will always
 be the limiting factor when creating a subsystem.

Select a Multiple Sessions VI instance or use the .NET method
 overload that outputs an array of sessions if you are not sure
 whether to return multiple sessions or a single session. Using this
 technique helps you avoid having to modify code modules if a pin map
 changes or if you convert a test program to run on other testers or
 with other pin maps. Using a Single Session VI instance or the .NET
 method overload that outputs a single session with a set of pins and
 sites that returns multiple sessions results in a run-time error.

Parent topic:

Code Module Development (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-groups.html language=enus -->
## TOPIC 00226: Pin Groups (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-groups.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-groups.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pin Groups section on the Pin Map tab to specify a grouping of pins that you can reference with a single name. Choose one of the following options to add a pin group to the pin map file: Click <Add Pin Groups Here> to display the Pin Groups pane, and click the Pin Group button. Right–click <

### Pin Groups (TSM)

Use the Pin Groups section on the Pin Map tab to specify a grouping of pins that you can reference with a single name.

Choose one of the following options to add a pin group to the pin map file:

- Click <Add Pin Groups Here> to display the Pin Groups pane, and click the Pin Group button.
- Right–click <Add Pin Groups Here> and select Pin Group from the context menu.

The Pin Map Editor automatically adds the pin group to the Pin Groups section. Select a pin group in the Pin Groups section to display the Pin Groups pane, where you can change the pin group name and use the individual checkboxes or the Select All checkbox to add or remove DUT pins, system pins, or pin groups from the selected pin group.

Note

Once you create a pin group, you can also add pins or other pin groups to the pin group using one of the following options:

- Click <Add Pin References Here> , and click the Pin Reference button in the Pin Groups pane to display a drop–down menu of available pins and pin groups.
- Right–click <Add Pin References Here> , and select Pin Reference from the context menu to display a drop–down menu of available pins and pin groups.
- Drag pins or pins groups from the Pins or Pin Groups section into a pin group.

You can also cut, copy, and paste pins, or add comments in the Pin Groups pane. Use the Comment button to specify a comment for the selected pin group. Comments display beneath the pin group they modify.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-map-editor.html language=enus -->
## TOPIC 00227: Pin Map Editor (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-map-editor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-map-editor.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pin Map Editor to view, create, modify, and save pin map files instead of editing the XML files directly. Use the Pin Map panel in the Test Program Editor to specify a pin map file for a test program. The pin map file also serves as the channel map file. Select Semiconductor ModuleEdit Pin M

### Pin Map Editor (TSM)

Use the Pin Map Editor to view, create, modify, and save pin map files instead of editing the XML files directly. Use the Pin Map panel in the Test Program Editor to specify a pin map file for a test program. The pin map file also serves as the channel map file.

Select Semiconductor Module»Edit Pin Map File or click the Edit Pin Map File
 button on the TSM
 toolbar
 to launch the Pin Map Editor. Alternatively, you can select Semiconductor Module»Edit Test Program and then select Pin Map in the
 Test Program Editor to launch the Pin Map panel. Click the
 Open file for edit[IMAGE alt='image' src='GUID-F141357B-5D8A-42A4-99E9-9C309A69F0FF-a5.png'] button to
 launch the Pin Map Editor.

The Pin Map Editor uses a red error icon in the Errors and Warnings window to indicate that the
 file does not conform to the Pin Map schema. Click the error icon or
 double-click the error message to highlight the error on
 the XML tab. The Errors and Warnings window displays a warning in
 orange text when the file conforms to the Pin Map schema but will
 generate an error at run time.

When you close the editor with the Cancel button and the pin map file has been edited since you opened it in the editor, a dialog box prompts you to discard changes or return to the editor. When you close the editor with the OK button, the file is updated on disk with the changes you made in the editor.

#### Configuring Pin Map
 Files

The Pin Map Editor includes the following options
 and tabs:

- Pin Map File —Specifies the pin map file
 to load. You can manually enter a relative file path.
- Undo —Removes the last edit made.
- Redo —Reinstates the last edit
 removed.
- Open —Launches the Select Pin Map File
 dialog box, in which you can browse to the pin map file to
 load.
- Save —Displays a context menu that
 includes a Save option to save the
 file to the current path and a Save
 As option to launch as Save As dialog
 box. The Save button is disabled when
 errors exist in the pin map file.
- New —Creates a new pin map file. If the
 file currently open in the editor has unsaved changes, a
 dialog box prompts you to discard the changes or return to
 the editor to save or cancel the changes to the file before
 creating a new file.
- Pin Map tab—Displays
 an editable, hierarchical view of the instruments, pins, pin
 groups, relays, relay groups, relay configurations, sites,
 and connections in the pin map file. For each item, you can
 edit the attributes of the item, insert new items, or insert
 comments in the file.
- XML tab —Displays the pin map file in a
 text format that you can edit.
- Errors and Warnings window —Displays
 issues to resolve. Click the Goto Error in
 XML error icon to highlight the error on
 the XML tab.

Parent topic:

Environment Reference

Related concepts:

- Pin Map Panel
- Test Program Editor (TSM)
- Common XML Validation Error Messages (TSM)
- Pin Map Tab (TSM)

Related reference:

- Semiconductor Module Toolbar Buttons
- Pin Map File XML Structure (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-map-file-xml-structure.html language=enus -->
## TOPIC 00228: Pin Map File XML Structure (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-map-file-xml-structure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-map-file-xml-structure.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The pin map XML schema, located at <TestStand>\Components\Schemas\NI_SemiconductorModule\PinMap.xsd, defines the following structure for a pin map XML file: Legend Root element> Element Attribute PinMap schemaVersion—Specifies the version of the schema file. Instruments—Specifies the type of instrum

### Pin Map File XML Structure (TSM)

<TestStand>\Components\Schemas\NI_SemiconductorModule\PinMap.xsd

| Legend |
| --- |
| Root element> |
| Element |
| Attribute |

[IMAGE alt='image' src='GUID-AF15E1E5-268F-45F0-B835-47595C4B20C3-a5.png']

PinMap

- schemaVersion —Specifies the version of the schema
 file.
- Instruments —Specifies the type of instruments
 connected to the tester, the name of each instrument, and the number of
 channels available for each instrument. Note Consider
 using the following instrument naming convention for semiconductor test
 programs:
 InstrumentType_ModelNumber_PXIChassisLocation_SlotLocation,
 for example, HSD_657x_C2_S03, where
 InstrumentType is an ASCII description of the
 instrument, ModelNumber is the model number as defined
 on ni.com, PXIChassisLocation uses a
 single digit to identify the PXI chassis (Cx), and
 SlotLocation uses double digits to identify the
 slot location (Sxx).
  - NIDigitalPatternInstrument —Defines an
 NI-Digital Pattern instrument.
    - name —Name of the instrument, as
 defined in Measurement & Automation Explorer (MAX).
    - numberOfChannels —Number of channels
 available on the instrument.
    - group —Name of the group that contains
 the instrument. Group names are case sensitive. By default,
 the Pin Map Editor sets this attribute to
 Digital when you add NI-Digital Pattern
 instruments to the pin map file. By using the same group
 name for all NI-Digital Pattern instruments, TSM combines
 all instruments into a single session so you can avoid
 session loops in code modules. To create multiple NI-Digital
 Pattern sessions, use a unique name for each set of
 instruments for which you want to create a session. Refer to
 the Digital Pattern Help for information about
 hardware limitations that prevent certain instruments from
 operating together as a single instrument.
  - NIDCPowerInstrument —Defines an
 NI-DCPower instrument.
    - name —Name of the instrument, as
 defined in MAX.
    - numberOfChannels —Number of channels
 available on the instrument.
    - ChannelGroup —Defines a group
 of channels controlled by one session. By grouping channels
 into a single session, you can avoid using session loops in
 code modules. By default, the Pin Map Editor creates one
 channel group containing all instrument channels. To create
 multiple, custom groups, use a unique name for the set of
 instrument channels for which you want to create a session.
 Note that channels within a group do not have to be from the
 same NI-DCPower instrument. Refer to the NI-DCPower Help for
 information about independent channels.
      - name —Name of a group of
 channels. Group names are case sensitive.
      - channels —Channel(s) that are
 assigned to a group. If not defined, TSM will assign
 all channels from the instrument. Channels can be
 defined as a comma-separated list (e.g.,
 0,1,3,..,n), a continuous range (e.g., 0:3), or as a
 combination of the two (e.g., 0:1,3). All channels
 from an instrument must be assigned to a group and a
 channel cannot be in multiple groups.
  - NIDAQmxTask —Defines an NI-DAQmx task,
 not an instrument.
    - name —Name of the task, as defined in
 test program code modules.
    - taskType —Category of the task. Pin
 queries that return tasks of more than one task type return
 an error.
    - channelList —List of physical channels
 associated with the task.
    - useAsRelayDriver —Specifies whether
 the task is used as a relay driver. Note Setting this attribute to
 true allows the DAQmx device to be
 used as a Relay Module to make connections to relays
 instead of pins. Only one DAQmx digital output line can
 be defined within the channelList. You
 must define separate DAQmx tasks in the pin map for each
 digital output line you want to connect to a relay. The
 logic state for relay close is the digital high from the
 digital output line.
  - NIDmmInstrument —Defines an NI-DMM
 instrument. NI-DMM instruments define a single channel, displayed
 within TSM as channel 0.
    - name —Name of the instrument, as
 defined in MAX.
  - NIFGenInstrument —Defines an NI-FGEN
 instrument.
    - name —Name of the instrument, as
 defined in MAX.
    - numberOfChannels —Number of channels
 available on the instrument.
  - NIScopeInstrument —Defines an NI-SCOPE
 instrument.
    - name —Name of the instrument, as
 defined in MAX.
    - numberOfChannels —Number of channels
 available on the instrument.
    - group —Name of the group that contains
 the instrument. Group names are case sensitive. By default,
 the Pin Map Editor sets this attribute to
 Scope when you add NI-SCOPE instruments
 to the pin map file. Group names are case sensitive. By
 using the same group name for all NI-SCOPE instruments, TSM
 combines all instruments into a single session so you can
 avoid session loops in code modules. To create multiple
 NI-SCOPE sessions, use a unique name for each set of
 instruments for which you want to create a session. Refer to
 the NI-SCOPE Help for information about
 hardware limitations that prevent certain instruments from
 operating together as a single instrument.
  - NIHSDIOInstrument —Defines an NI-HSDIO
 instrument.
    - name —Name of the instrument, as
 defined in MAX.
    - numberOfChannels —Number of channels
 available on the instrument.
    - PFILines —(Optional) Defines the PFI
 lines available in the NI-HSDIO instrument in a
 comma-separated list of numbers or ranges of numbers
 separated by a hyphen. PFI number ranges are inclusive and
 must be in ascending order. Example:
 PFILines=2,3,4-8
  - NIRFSAInstrument —Defines an NI-RFSA
 instrument. NI-RFSA instruments define a channel named
 In .
    - name —Name of the instrument, as
 defined in MAX.
  - NIRFSGInstrument —Defines an NI-RFSG
 instrument. NI-RFSG instruments define a channel named
 Out .
    - name —Name of the instrument, as
 defined in MAX.
  - NIVSTInstrument —Defines an NI-VST
 instrument that can hold RFSA, RFSG, and FPGA sessions. NI-VST
 instruments define a channel named In and another
 channel named Out .
    - name —Name of the instrument, as
 defined in MAX.
    - fpgaFilePath —(Optional) Path to the
 FPGA file relative to the path of the pin map file. You can
 manually specify an absolute file path.
  - NIRFPMInstrument —Defines an RF Port
 Module instrument that can hold RFPM, RFmx, RFSA, RFSG, and FPGA
 sessions .
    - name —Name of the VST instrument, as
 defined in MAX, that is part of the RF port module
 subsystem.
    - portsList —Defines the ports available
 in the RF Port Module in a comma-separated list of numbers
 or ranges of numbers separated by a hyphen. Port number
 ranges are inclusive and must be in ascending order, for
 example, channelList="2,3,4-8" .
    - calibrationFilePath —Path, relative to
 the path of the pin map file, to the TDMS files that contain
 the calibration data for the RF Port Module instrument. You
 can manually specify an absolute file path.
    - iviSwitchName —IVI Switch resource
 name associated with the port module, as defined in
 MAX.
    - fpgaFilePath —(Optional) Path to the
 FPGA file relative to the path of the pin map file. You can
 manually specify an absolute file path.
  - NI5530RFPortModule —Defines an NI-5530
 RF Port Module instrument. You can use the NI-5530 RF Port Module to
 multiplex one RF instrument across multiple test sites or multiple
 RF instruments across multiple test sites. This element is replaced
 by the NIRFPMInstrument .
    - name —Name of the instrument, as
 defined in MAX.
    - calibrationFilePath —Path, relative to
 the path of the pin map file, to the TDMS files that contain
 the calibration data for the RF Port Module instrument. You
 can manually specify an absolute file path.
  - NIRelayDriverModule —Defines a
 PXI-2567 relay driver module.
    - name —Name of the relay driver module,
 as defined in MAX.
    - numberOfControlLines —Number of
 control lines available on the relay driver module.
  - Instrument —Defines an instrument that
 TSM does not natively support. Use the TSM Code Module API to set
 any type of session data on a channel, group of channels, or
 instrument. Refer to the example sequence files, pin map files, and
 LabVIEW code module VIs located in the <TestStand
 Public>\Examples\NI_SemiconductorModule\Custom
 Instruments directory for examples of using TSM pin
 map files and VIs to perform tests using instruments that TSM does
 not natively support.
    - name —String that identifies the
 instrument. For instruments that NI provides but that TSM
 does not natively support, specify the name of the
 instrument, as defined in MAX.
    - instrumentTypeId —String that
 identifies the instrument type, family, class, or product
 group. You cannot specify a value that begins with
 ni . This value is a string that you
 define in the pin map and is not a predefined value from
 some other source, such as a name in MAX, that you select.
 Use this value to identify all instances of a particular
 instrument type. Instruments of the same type typically have
 the same session data type and same driver API.
    - ChannelGroup —Defines a
 synchronized group of channels. Specify individual
 Channel elements with unique
 IDs within the channel group.
      - id —Unique ID for the channel
 group. An instrument cannot contain more than one
 channel group with the same ID.
      - Channel —Channel within
 the channel group.
        - id —Unique ID for the channel.
 An instrument cannot contain more than one channel
 with the same ID.
    - Channel —Channel on the
 instrument.
      - id —Unique ID for the channel.
 An instrument cannot contain more than one channel
 with the same ID.
  - NIModelBasedInstrument —Defines a
 Model-Based Instrument.
    - name —Unique string that identifies
 the instrument.
    - instrumentModel —Installed model
 description files in the model library.
    - category —String that specifies the
 category to which the instrument belongs. The instrument
 model description defines the category for the instrument
 model.
    - subcategory —(Optional) String that
 specifies the subcategory to which the instrument belongs.
 The instrument model description defines the subcategory for
 the instrument model.
    - Resource —(Optional) If
 required by the model description file, specifies the
 instrument resource name in Measurement & Automation
 Explorer (MAX).
      - owner —Specifies the instrument
 resource in the model description file to which the
 attribute values of the
 UserData element apply.
      - UserData —Contains the
 properties from the model description file you can
 assign.
        - propertyName —Name of the
 property defined in the model description file.
        - propertyValue —Value you assign
 to the property.
  - Multiplexer —Defines a switching
 instrument to use as a multiplexer across multiple test sites. You
 can use one instrument multiplexed across multiple test sites or
 multiple instruments multiplexed across multiple test sites.
    - name —Name of the Switch Executive
 virtual device, as defined in MAX.
    - multiplexerTypeId —(Optional) String
 that identifies the switch type, family, class, or product
 group. You cannot specify a value that begins with
 ni . This value is a string that you
 define in the pin map and is not a predefined value from
 some other source, such as a name in MAX, that you select.
 Use this value to identify all instances of a particular
 switch type. Switches of the same type typically have the
 same session data type and same driver API.
- Pins —Specifies the pins on the DUT and the pins
 on the tester that the test program associated with the pin map file
 references.
  - DUTPin —Defines a DUT pin, which is a
 pin on a DUT or a resource on the tester or DIB that is associated
 with one or more sites.
    - name —String that identifies the DUT
 pin.
  - SystemPin —Defines a system pin, which
 is resource on the tester or DIB that is connected to an
 instrument.
    - name —String that identifies the
 system pin.
- PinGroups —Specifies named grouping of
 pins.
  - PinGroup —Defines a group of pins that
 you can reference with a single name.
    - name —String that identifies the group
 of pins.
    - PinReference —Specifies a pin
 or a group of pins within the pin group.
      - pin —String that specifies the
 name of an existing pin or pin group.
- Relays —Specifies the relays on the site and
 the relays on the tester that the test program associated with the pin map
 file references
  - SiteRelay —Defines a site relay, which
 is a relay on the tester or DIB that is connected to a relay driver
 module and that is associated with one or more sites.
    - name —String that identifies the site
 relay.
    - openStateDisplayLabel —(Optional) A
 description of the connections when the relay is in the open
 state. This attribute is only for informational and display
 purposes for the Digital Pattern Editor.
    - closedStateDisplayLabel —(Optional) A
 description of the connections when the relay is in the
 closed state. This attribute is only for informational and
 display purposes for the Digital Pattern Editor.
  - SystemRelay —Defines a system relay,
 which is a relay on the tester or DIB that is connected to a relay
 driver module and that is associated with all sites.
    - name —String that identifies the
 system relay.
    - openStateDisplayLabel —(Optional) A
 description of the connections when the relay is in the open
 state. This attribute is only for informational and display
 purposes for the Digital Pattern Editor.
    - closedStateDisplayLabel —(Optional) A
 description of the connections when the relay is in the
 closed state. This attribute is only for informational and
 display purposes for the Digital Pattern Editor.
- RelayGroups —Specifies named grouping of
 relays.
  - RelayGroup —Defines a group of relays
 that you can reference with a single name.
    - name —String that identifies the group
 of relays.
    - RelayReference —Specifies a
 relay or a group of relays within the relay group.
      - relay —String that specifies the
 name of an existing relay or relay group.
- RelayConfigurations —Specifies a grouping of
 relay configurations.
  - RelayConfiguration —Defines a relay
 configuration. A relay configuration is the name assigned to a set
 of relays and their positions.
    - name —String that identifies the relay
 configuration.
    - RelayPosition —Specifies a
 relay and its position.
      - relay —String that specifies the
 name of an existing relay or relay group.
      - position —String that specifies
 the position of the relay or relay group. Valid
 values are Open or
 Closed .
- Sites —Specifies the sites on the tester.
  - Site —Defines a site to test.
    - siteNumber —Number that identifies the
 site. Site numbers must start at 0 and be
 consecutive without gaps.
- Connections —Specifies mappings among pins,
 sites, instruments, and instrument channels.
  - Connection —Defines a connection
 between a DUT pin and an instrument channel.
    - pin —Name of the DUT pin to connect.
 The value must match the value of the name 
 attribute of a DUTPin element.
    - siteNumber —The site or group of sites
 associated with the connection. The value must match the
 value of the siteNumber attribute of one of
 the Site elements or it must be a
 comma-separated list of site numbers.
    - instrument —Name of the instrument or
 DAQmx task to connect. The value must match the value of the
 name attribute of an
 Instrument element.
    - channel —ID of the instrument channel
 or physical channel ID of the DAQmx task to connect.
    - deembeddingFilePath —Path, relative to
 the path of the pin map file, to the S2P file for
 de-embedding an RF Port Module connection. You can manually
 specify an absolute path.
    - deembeddingOrientation —(Optional)
 Used with the deembeddingFilePath attribute
 to specify the orientation of the data in the S2P file
 relative to the port the channel attribute
 specifies. Valid values are Port1TowardDUT 
 or Port2TowardDUT .
  - SystemConnection —Defines a direct
 connection between a system pin and an instrument channel.
    - pin —Name of the system pin to
 connect. The value must match the value of the
 name attribute of a
 SystemPin element.
    - instrument —Name of the instrument to
 connect. The value must match the value of the
 name attribute of an
 Instrument element.
    - channel —(Optional) ID of the
 instrument channel to connect.
    - deembeddingFilePath —Path, relative to
 the path of the pin map file, to the S2P file for
 de-embedding an RF Port Module connection. You can manually
 specify an absolute path.
    - deembeddingOrientation —(Optional)
 Used with the deembeddingFilePath attribute
 to specify the orientation of the data in the S2P file
 relative to the port the channel attribute
 specifies. Valid values are Port1TowardDUT 
 or Port2TowardDUT .
  - MultiplexedConnection —Defines a
 multiplexed connection between the same DUT pin on multiple sites
 and a single instrument channel.
    - instrument —Name of the instrument to
 connect. The value must match the value of the
 name attribute of an
 Instrument element.
    - channel —ID of the instrument channel
 to connect.
    - MultiplexedDUTPinRoute —Specifies
 the route required to connect a DUT pin on a specific site
 to the instrument channel.
      - pin —Name of the DUT pin to
 connect. The value must match the value of the
 name attribute of a
 DUTPin element.
      - siteNumber —Site for the DUT pin
 in the system. The value must match the value of the
 siteNumber attribute of a
 Site element.
      - multiplexer —String that
 identifies the multiplexer required to create the
 route. The value must match the value of the
 name attribute of a
 Multiplexer element.
      - routeName —String that
 identifies the multiplexer route required to connect
 the pin and site to the instrument and channel.
      - deembeddingFilePath —Path,
 relative to the path of the pin map file, to the S2P
 file for de-embedding an RF Port Module connection.
 You can manually specify an absolute path.
      - deembeddingOrientation —(Optional)
 Used with the deembeddingFilePath 
 attribute to specify the orientation of the data in
 the S2P file relative to the port the
 channel attribute specifies.
 Valid values are Port1TowardDUT or
 Port2TowardDUT .
  - RelayConnection —Defines a connection
 between a site relay and a control line of a relay driver module.
    - relay —Name of the site relay to
 connect. The value must match the value of the
 name attribute of a
 SiteRelay element.
    - siteNumber —The site or group of sites
 associated with the connection. The value must match the
 value of the siteNumber attribute of one of
 the Site elements or it must be a
 comma-separated list of site numbers.
    - relayDriverModule —Name of the relay
 driver module to connect. The value must match the value of
 the name attribute of an
 NIRelayDriverModule element.
    - controlLine —ID of the physical
 control line of the relay driver module to connect.
  - SystemRelayConnection —Defines a
 direct connection between a system relay and a control line of a
 relay driver module.
    - relay —Name of the system relay to
 connect. The value must match the value of the name
 attribute of a SystemRelay element.
    - relayDriverModule —Name of the relay
 driver module to connect. The value must match the value of
 the name attribute of an
 NIRelayDriverModule element.
    - controlLine —ID of the physical
 control line of the relay driver module to connect.

Parent topic:

Mapping DUT Pins to Instrument Channels (TSM)

Related concepts:

- Pin Map Editor (TSM)
- TSM Code Module API
- Model-Based Instruments (TSM)

Related tasks:

- Custom Instruments (TSM)

Related reference:

- Schema Version Policy (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-map-panel.html language=enus -->
## TOPIC 00229: Pin Map Panel

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-map-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-map-panel.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Pin Map panel contains the following options: Pin Map File Path—Specifies the relative pathname to the pin map file to use in the test program. A red exclamation point indicates that an issue exists with the file, such as the file is invalid or that the file does not conform to the Pin Map XML s

### Pin Map Panel

The Pin Map panel contains the following options:

- Pin Map File Path —Specifies the relative pathname to the pin map file to use in the test
 program. A red exclamation point indicates that an issue
 exists with the file, such as the file is invalid or
 that the file does not conform to the Pin Map XML schema. A tooltip
 displays the error message. If errors exist in the
 file, you make changes in the dialog box, and click
 OK, TSM commits those
 changes. Do not proceed without reviewing the errors
 for the pin map file.
- Open file for edit 
 —Launches the pin map file in the Pin
 Map Editor.

Parent topic:

Test Program Editor (TSM)

Related concepts:

- Mapping DUT Pins to Instrument Channels (TSM)
- Pin Map Editor (TSM)

Related reference:

- Pin Map File XML Structure (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-map-tab.html language=enus -->
## TOPIC 00230: Pin Map Tab (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-map-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-map-tab.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Pin Map tab contains the following sections: Instruments—Use this section to specify the instruments required to execute the test program. Pins—Use this section to specify the DUT pins and other pin types connected to the tester. Pin Groups—Use this section to specify a grouping of pins that you

### Pin Map Tab (TSM)

The Pin Map tab contains the following sections:

- Instruments—Use this section to specify the instruments required to execute the test program.
- Pins—Use this
 section to specify the DUT pins and other pin types
 connected to the tester.
- Pin Groups—Use this
 section to specify a grouping of pins that you can reference
 with a single name.
- Relays—Use this
 section to specify the relays on the tester that the test
 program associates with the pin map file references.
- Relay Groups—Use
 this section to specify a grouping of relays that you can
 reference with a single name.
- Relay
 Configurations—Use this section to specify a set of
 relays and their positions.
- Sites—Use this
 section to specify the sites on the tester.
- Connections—Use this
 section to specify mappings from pins to instrument channels
 for every site and for system resources.

Parent topic:

Pin Map Editor (TSM)

Related concepts:

- Instruments (TSM)
- Pins (TSM)
- Pin Groups (TSM)
- Relays (TSM)
- Relay Groups (TSM)
- Relay Configurations (TSM)
- Sites (TSM)

Related tasks:

- Adding a Connection in the Pin Map Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pin-map.html language=enus -->
## TOPIC 00231: Mapping DUT Pins to Instrument Channels (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pin-map.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pin-map.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A semiconductor test program must communicate information from the tester instrumentation to the DUT to which the instrumentation is connected. To handle this communication in a test program, test engineers must consider the following requirements for instrument sessions and channels for all resourc

### Mapping DUT Pins to Instrument Channels (TSM)

A semiconductor test program must communicate information from the tester instrumentation to the
 DUT to which the instrumentation is connected. To handle this communication in a test
 program, test engineers must consider the following requirements for instrument sessions and
 channels for all resources in the test system:

- Develop test program code that uses the names of actual connections on the DUT (DUT pins) to
 refer to channels on the instrument.
- Manage a large number of instrument channels.
- Scale test code to test multiple sites in parallel to improve tester efficiency.
- Support multiple types of instruments because different instruments might use channels and sessions in different ways.

Typically, instrument driver software provides test engineers with software tools for communicating with the DUT in terms of the instrument channels and sessions. However, instrument drivers have no information about the actual pins on the DUT. To develop test code that uses DUT pin names, a test engineer must use a pin map to associate each DUT pin name with the name, channel, and session of the instrument connected to that particular DUT pin.

#### TSM Implementation

Use
 the Pin Map
 Editor to view, create, modify, and save pin map files. The pin map XML schema,
 located at <TestStand>\Components\Schemas\NI_SemiconductorModule\PinMap.xsd,
 defines the structure for a pin map file. Use the Pin Map File Path
 control on the Pin
 Map panel of the Test Program Editor to specify the pin map file to use with the test
 program.

The pin map file can support multiple test sites
 and multiple instrument types.

In addition, use the TSM Code Module API to query
 instrument names, obtain all open sessions, and translate DUT pin names or pin groups to
 instrument channels and sessions. The Semiconductor Multi Test and the Semiconductor Action
 steps create the SemiconductorModuleContext object that you can pass to a
 LabVIEW or .NET code module to use the TSM Code Module API. The
 SemiconductorModuleContext object describes a subset of pins, relays,
 sites, and instruments on a test system.

Related concepts:

- Pin Map Editor (TSM)
- Pin Map Panel
- Test Program Editor (TSM)
- Testing Multiple Sites in Parallel (TSM)
- TSM Code Module API

Related reference:

- Pin Map File XML Structure (TSM)

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=pins.html language=enus -->
## TOPIC 00232: Pins (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `pins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/pins.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pins section on the Pin Map tab to specify the DUT pins and other pin types connected to the tester. You can right–click any item in the section you want to edit and use the context menu to complete common tasks. Choose one of the following options to add a pin connection to the pin map file

### Pins (TSM)

Use the Pins section on the Pin Map tab to specify the DUT pins and other pin types connected to the tester. You can right–click any item in the section you want to edit and use the context menu to complete common tasks.

Choose one of the following options to add a pin connection to the pin map file:

- Click <Add Pins Here> to display the Pins pane, and click the button of the pin type you want to add.
- Right–click <Add Pins Here> and select the pin type you want to add from the context menu.

The Pin Map Editor automatically adds the pin connection to the Pins section. Select a pin connection in the Pins section to display the Pins pane, where you can edit the pin’s name.

Note

You can also cut, copy, and paste pins, or add comments in the Pins pane. Use the Comment button to specify a comment for the selected pin. Comments display beneath the pin they modify.

TSM supports the following pin connection types:

- DUT pin —Specifies a DUT pin, which is a pin on a DUT or a resource on the
 tester or DIB that is associated with one or more sites.
- System pin —Specifies a system pin, which is resource on
 the tester or DIB that is connected to an instrument.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=programm-in-csharp.html language=enus -->
## TOPIC 00233: Programming with TSM APIs in C#

- bundle_id: `teststand-semiconductor-module`
- source_path: `programm-in-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/programm-in-csharp.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In C#, you can access TSM APIs by adding the corresponding component as a reference in a project. API Component TSM Code Module API NationalInstruments.TestStand.SemiconductorModule.CodeModuleAPI TSM Application API NationalInstruments.TestStand.SemiconductorModule.ApplicationAPI TSM installs .NET a

### Programming with TSM APIs in C#

In C#, you can access TSM APIs by adding the corresponding component as a reference in a project.

| API | Component |
| --- | --- |
| TSM Code Module API | NationalInstruments.TestStand.SemiconductorModule.CodeModuleAPI |
| TSM Application API | NationalInstruments.TestStand.SemiconductorModule.ApplicationAPI |

TSM installs .NET assemblies for the TSM Code Module and Application APIs in the <TestStand>\API\DotNet\Assemblies\CurrentVersion directory and in the Global Assembly Cache (GAC). The assemblies support .NET 4.0 and later.

To add a reference to TSM API assemblies in Visual Studio, select the project in the Solution
 Explorer and select Project»Add Reference. If the assemblies do not appear in the corresponding
 dialog box, exit all running copies of Visual Studio, launch the
 TestStand Version Selector,
 select the current version of TestStand, and click the
 Make Active button.

Note

<TestStand>\API\DotNet\Assemblies\CurrentVersion

After you add one of the TSM API components as a reference in a project, add the following directive at the top of the source file:

using NationalInstruments.TestStand.SemiconductorModule;

or

using NationalInstruments.TestStand.SemiconductorModule.CodeModuleAPI;

All TSM classes, methods, and properties are available in the Microsoft Visual Studio object browser and are accessible from the C# source code. Help text for classes, methods, and properties appears in Microsoft IntelliSense.

To control NI instruments from a .NET assembly, you must also complete the following tasks:

- Install the appropriate NI driver for the instrument you want to control. Ensure you install the correct NI .NET API for the version of the NI driver you installed. For some NI drivers, you must manually select .NET support options in the installer.
- Add a reference to the corresponding NI driver .NET API assembly to the project. The Accelerometer with .NET and the Part Average Testing with
 .NET examples include Visual Studio projects that reference the TSM Code Module
 API and some NI .NET APIs and demonstrate how to invoke those APIs.

Visit ni.com/info and enter the Info Code NETAPIdriversupport for
 information about the available NI .NET APIs and the versions of the NI drivers each
 supports.

#### Upgrading
 TSM

(TSM 2019 or later) When you upgrade to TSM 2019 or
 later, you do not need to update .NET assembly references to the TSM
 Application API or TSM Code Module API assemblies in Visual Studio
 projects. The TSM installer ensures that references to earlier
 versions of the API assemblies are automatically redirected to the
 current version of the assembly.

(TSM 2017 or earlier) When
 you upgrade to a full, non-service pack version of TSM and you want
 to continue to use existing code modules and applications in the
 later version, you must update the .NET assembly references in
 Visual Studio projects. The assemblies you build using TSM APIs are
 compatible only with the version of TSM, including service packs,
 you reference in Visual Studio projects.

#### Upgrading Instrument
 Drivers

When you upgrade to a later version of an
 instrument driver .NET API, you do not need to update the .NET
 assembly references in Visual Studio projects. NI instrument driver
 .NET API installers ensure that references to earlier versions of
 the instrument driver .NET API assembly are automatically redirected
 to the current version of the assembly if the earlier version
 assembly does not exist.

The following table lists the minimum
 version of instrument driver .NET APIs TSM supports.

| NI Driver | Assembly Name | Minimum Version |
| --- | --- | --- |
| NI-DAQmx | NationalInstruments.DAQmx.dll | 16.1 |
| NI-DCPower | NationalInstruments.ModularInstruments.NIDCPower.Fx40.dll | 1.1 |
| NI-Digital Pattern | NationalInstruments.ModularInstruments.NIDigital.Fx40.dll | 16.0 |
| NI-DMM | NationalInstruments.ModularInstruments.NIDmm.Fx40.dll | 15.2 |
| NI-FGEN | NationalInstruments.ModularInstruments.NIFgen.Fx40.dll | 16.0 |
| NI-RFmx | NationalInstruments.RFmx.InstrMX.Fx40.dll | 19.0 |
| NI-RFPM | NationalInstruments.ModularInstruments.NIRfpm.Fx40.dll | 14.5 |
| NI-RFSA | NationalInstruments.ModularInstruments.NIRfsa.Fx40.dll | 19.0 |
| NI-RFSG | NationalInstruments.ModularInstruments.NIRfsg.Fx40.dll | 19.0 |
| NI-SCOPE | NationalInstruments.ModularInstruments.NIScope.Fx40.dll | 2.0 |
| NI-SWITCH | NationalInstruments.ModularInstruments.NISwitch.Fx40.dll | 1.1 |

Parent topic:

Code Module Development (TSM)

Related concepts:

- TSM Code Module API
- TSM Application API

Related tasks:

- Accelerometer with .NET
- Part Average Testing with .NET (TSM)

Related information:

- .NET Resources for NI Hardware and Software

<!--NI_TOPIC bundle=teststand-semiconductor-module path=protect-test-programs-and-limits.html language=enus -->
## TOPIC 00234: Protecting Test Programs and Test Limits from Editing and Viewing (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `protect-test-programs-and-limits.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/protect-test-programs-and-limits.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can password protect sequence files to deter editing and viewing sequence files in the sequence editor and in operator interfaces. To protect test limits files, use the Embed Test Limits File option on the Test limits Files panel of the Test Program Editor to embed the external test limits files

### Protecting Test Programs and Test Limits from Editing and Viewing (TSM)

You can password protect sequence files to
 deter editing and viewing sequence files in the sequence editor and
 in operator interfaces. To protect test limits files, use the
 Embed Test Limits File option on the
 Test limits Files panel of the Test Program Editor to embed the
 external test limits files in the test program sequence file before
 you password-protect the test program sequence file.

Note

Parent topic:

Deploying TSM Test Programs

Related concepts:

- Test Limits Files Panel
- Test Program Editor (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=publishing-results.html language=enus -->
## TOPIC 00235: Publishing Results (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `publishing-results.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/publishing-results.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you take measurements, you typically publish the results to the test sockets to evaluate and log. It might become difficult to know which piece of data to associate with each site and pin because you typically take measurement using multiple instruments connected to multiple DUTs and return ar

### Publishing Results (TSM)

After you take measurements, you typically publish the results to the test sockets to evaluate
 and log. It might become difficult to know which piece of data to
 associate with each site and pin because you typically take
 measurement using multiple instruments connected to multiple DUTs
 and return arrays with the measurements mixed among each site. Use
 the appropriate Pin Query VI or .NET method with the
 Publish Data VI or Publish .NET method to return
 data to the correct site. Because the Publish Data VI and
 Publish .NET method manage arrays of
 different dimensions and extract the required data in the required
 order, you do not need to manage arrays before publishing
 measurements. The Pin Query VI or .NET method returns a Pin Query
 Context to associate a pin query operation with a matching instance
 of the publish operation.

Note

The following figure shows how to publish pin-based data from a measurement taken with an NI-DCPower instrument.

#### LabVIEW

[IMAGE alt='image' src='GUID-6FE56872-5C79-496C-AD05-8778183F6B8C-a5.png']

#### .NET
 (C#)

```text
public static void ExampleCodeModule(ISemiconductorModuleContext semiconductorModuleContext, string[] pins)
{
        NIDCPower[] dcPowerSessions;
        string[] dcPowerChannelStrings;
        var pinQuery = semiconductorModuleContext.GetNIDCPowerSessions(pins, out dcPowerSessions, out dcPowerChannelStrings);
        var measurementResults = new double[dcPowerSessions.Length];
        Parallel.For(0, dcPowerSessions.Length, i =>
        {
                measurementResults[i] = PerformMeasurement(dcPowerSessions[i], dcPowerChannelStrings[i]);
        });
        pinQuery.Publish(measurementResults);
}
```

In
 C# use the var keyword to declare the variable to
 store the Pin Query Context return value of the Pin Query method
 with a dynamic type. Using this technique can make it easier to
 select the correct Pin Query Context type based on which overload of
 the Pin Query method you select.

#### Per-Site Publishing

You can also
 use a site-based instance of the Publish Data VI or the
 Publish method on the
 SemiconductorModuleContext .NET object to publish values for each
 site. Use the optional Pin and
 Published Data Id parameters of the
 Publish Data VI or PublishPerSite .NET method to
 publish data for each site to tests that have non-empty
 Pin and Published Data
 Id fields.

#### LabVIEW

[IMAGE alt='image' src='GUID-97C1F808-BA0E-4BE5-99A6-729B63B29D8A-a5.png']

#### .NET
 (C#)

```text
public static void ExampleCodeModule(ISemiconductorModuleContext semiconductorModuleContext, string comparisonPin1, string comparisonPin2, double comparisonTolerance)
{
        NIDCPower[] dcPowerSessions;
        string[] channelStrings; string[] pins = {comparisonPin1, comparisonPin2};
        var pinQuery = semiconductorModuleContext.GetNIDCPowerSessions(pins, out dcPowerSessions, out channelStrings);

        var results = PerformComparisonMeasurement(dcPowerSessions, channelStrings);

        var perSiteDataForPin1 = pinQuery.ExtractPinData(results, comparisonPin1);
        var perSiteDataForPin2 = pinQuery.ExtractPinData(results, comparisonPin2);

        int numSites = semiconductorModuleContext.SiteNumbers.Count;
        bool[] comparisonResult = new bool[numSites];
        for (int siteIndex = 0; siteIndex < numSites; siteIndex++)
        {
                comparisonResult[siteIndex] = Math.Abs(perSiteDataForPin1[siteIndex] - perSiteDataForPin2[siteIndex]) < comparisonTolerance;
        }
        semiconductorModuleContext.PublishPerSite(comparisonResult);
}
```

Parent topic:

Code Module Development (TSM)

Related concepts:

- Pin and Session Queries (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=query-pinsite-meas-unsupported-type.html language=enus -->
## TOPIC 00236: Query Pin/Site Measurement for Unsupported Measurement Type (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `query-pinsite-meas-unsupported-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/query-pinsite-meas-unsupported-type.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The following figure shows how to query for measurement data for a pin and site combination if the Extract Pin Data VI does not support the measurement type. This example includes the following main tasks: Query for the custom instrument sessions for the pin(s) connected to the NI-DCPower instrument

### Query Pin/Site Measurement for Unsupported Measurement Type (TSM)

The following figure shows how to query for measurement data for a pin and site combination if the Extract Pin Data VI does not support the measurement type.

[IMAGE alt='image' src='GUID-48C9F493-0328-481E-8C06-B3CB829DE36C-a5.png']

This example includes the following main tasks:

1. Query for the custom instrument sessions for the pin(s) connected to the NI-DCPower instrument.
2. Use a parallel For Loop to iterate on every instrument to create simulated data.
3. Query for measurement data for a specific pin and site combination.

Parent topic:

Multisite Programming Scenarios (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=reduce-setting-times.html language=enus -->
## TOPIC 00237: Reduce Settling Times in Test Code Modules (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `reduce-setting-times.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/reduce-setting-times.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: It is common to add a settling time before taking measurements to achieve the required precision. Once a test program is running well, evaluate the settling times to reduce them to the minimum settling time required for an accurate measurement.

### Reduce Settling Times in Test Code Modules (TSM)

It is common to add a settling time before taking measurements to achieve the required precision. Once a test program is running well, evaluate the settling times to reduce them to the minimum settling time required for an accurate measurement.

Parent topic:

Test Time Reduction and Test System Performance Improvements (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=relay-configurations.html language=enus -->
## TOPIC 00238: Relay Configurations (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `relay-configurations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/relay-configurations.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Relay Configurations section on the Pin Map tab to specify a set of relays and their relay position states. You can set the relay state position of all relays with a single call to the TSM Code Module API. You can right–click any item in the section you want to edit and use the context menu

### Relay Configurations (TSM)

Use the Relay Configurations section on the Pin Map tab to specify a set of relays and their relay position states. You can set the relay state position of all relays with a single call to the TSM Code Module API. You can right–click any item in the section you want to edit and use the context menu to complete common tasks.

Choose one of the following options to add a relay configuration to the pin map file:

- Click <Add Relay Configurations Here> to display the Relay Configurations pane, and click the Relay Configuration button.
- Right–click <Add Relay Configurations Here> and select Relay Configuration from the context menu.

The Pin Map Editor automatically adds the relay configuration to the Relay Configurations section. Select a relay configuration in the Relay Configurations section to display the Relay Configuration pane, where you can change the relay configuration name, select the relay position state, view the final relay state, and change the order of relays and relay groups. Relay state positions are applied sequentially in the order in which the relay or relay group appears in the Relay Configuration pane. You can change the order of a relay or relay group by using the Up and Down buttons to move the selected relay or relay group.

Alternatively, when you create a new relay configuration, you can click <Add Relay Positions Here>, then click the Relay Position button. Select the relay or relay group you want to add from the top drop–down menu, then select the relay position state from the bottom drop–down menu. Use the Relay Configuration pane to make additional changes.

Click the Relay Configurations section to display the Relay Configurations table, which includes a column for each relay and a column for each relay configuration. Each relay configuration column shows the final relay state of the corresponding relay(s).

You can also cut, copy, and paste relay configurations, or add comments in the Relay Configurations pane. Use the Comment button to specify a comment for the selected relay configuration. Comments display beneath the relay configuration they modify.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)
- TSM Code Module API

<!--NI_TOPIC bundle=teststand-semiconductor-module path=relay-groups.html language=enus -->
## TOPIC 00239: Relay Groups (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `relay-groups.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/relay-groups.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Relay Groups section on the Pin Map tab to specify a grouping of relays that you can reference with a single name. You can right–click any item in the section you want to edit and use the context menu to complete common tasks. Choose one of the following options to add a relay group to the p

### Relay Groups (TSM)

Use the Relay Groups section on the Pin Map tab to specify a grouping of relays that you can reference with a single name. You can right–click any item in the section you want to edit and use the context menu to complete common tasks.

Choose one of the following options to add a relay group to the pin map file:

- Click <Add Relay Groups Here> to display the Relay Groups pane, and click the Relay Group button.
- Right–click <Add Relay Groups Here> and select Relay Group from the context menu.

The Pin Map Editor automatically adds the relay group to the Relay Groups section. Select a relay group in the Relay Groups section to display the Relay Groups pane, where you can change the relay group name and use the individual checkboxes or the Select All checkbox to add or remove site relays, system relays, or relay groups from the selected relay group.

Note

Once you create a relay group, you can also add relays or other relay groups to the relay group using one of the following options:

- Click <Add Relay References Here> , and click the Relay Reference button in the Relay Groups pane to display a drop–down menu of available relays and relay groups.
- Right–click <Add Relay References Here> , and select Relay Reference from the context menu to display a drop–down menu of available relays and relay groups.
- Drag relays or relay groups from the Relays or Relay Groups section into a relay group.

You can also cut, copy, and paste relay groups, or add comments in the Relay Groups pane. Use the Comment button to specify a comment for the selected relay group. Comments display beneath the relay group they modify.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=relays.html language=enus -->
## TOPIC 00240: Relays (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `relays.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/relays.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Relays section on the Pin Map tab to specify the relays on the site and the relays on the tester that the test program associates with the pin map file references. You can right–click any item in the section you want to edit and use the context menu to complete common tasks. Choose one of th

### Relays (TSM)

Use the Relays section on the Pin Map tab to specify the relays on the site and the relays on the tester that the test program associates with the pin map file references. You can right–click any item in the section you want to edit and use the context menu to complete common tasks.

Choose one of the following options to add a relay to the pin map file:

- Click <Add Relays Here> to display the Relays pane, and click the button of the relay type you want to add.
- Right–click <Add Relays Here> and select the relay type you want to add from the context menu.

The Pin Map Editor automatically adds the relay to the Relays section. Select a relay in the Relays section to display the Relays pane, where you can edit the relay’s name, open state display label, and closed state display label.

Note

You can also cut, copy, and paste relays, or add comments in the Relays pane. Use the Comment button to specify a comment for the selected relay. Comments display beneath the relay they modify.

TSM supports the following relay types:

- Site relay —Specifies a site relay, which is a relay on the tester or DIB that is connected to a relay driver module and that is associated with one or more sites.
- System relay —Specifies a system relay, which is a relay on the tester or DIB that is connected to a relay driver module and that is associated with all sites.

Parent topic:

Pin Map Tab (TSM)

Related concepts:

- Pin Map Tab (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=report-and-data-log-filenames.html language=enus -->
## TOPIC 00241: Specifying Report and Data Log Filenames (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `report-and-data-log-filenames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/report-and-data-log-filenames.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: TSM result processing plug-ins determine the name of the report or data log file by calling the GetReportFileName callback sequence once for each active result processing plug-in instance. The GetReportFileName callback sequence is located in the <TestStand Public>\Components\Callbacks\NI_Semiconduc

### Specifying Report and Data Log Filenames (TSM)

TSM result processing plug-ins determine the name of the report or data log file by calling the
 GetReportFileName callback sequence
 once for each active result processing plug-in instance. The
 GetReportFileName callback sequence is
 located in the <TestStand
 Public>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 or <TestStand>\Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq
 file.

TSM result processing plug-ins use the combination of the destination directory you specify in the corresponding result processing plug-in Options dialog box and the report or data log filename the GetReportFileName callback sequence returns to determine the absolute path of the report or data log file. When you customize the log filename for the Debug Test Results Log, use unique filenames for each test site. The Debug Test Results Log result processing plug-in appends results from each DUT to the corresponding site log.

You can customize the filenames and locations in which TSM result processing plug-ins create
 report and data log files by modifying the
 GetReportFileName callback. The
 GetReportFileName callback sequence
 contains parameters that specify result
 processing plug-in information, lot information, station
 information, date and time information, and a destination directory.
 You can use the TSM Application API in a code module
 the GetReportFilename callback sequence calls to
 access batch and site run-time data, including wafer
 information.

Complete the following steps to customize TSM report and data log filenames.

1. Determine whether a sequence file named SemiconductorModuleCallbacks.seq 
 exists in the
 <TestStand Public>\Components\Callbacks\NI_SemiconductorModule 
 directory. If the sequence file does not exist, create it
 and ensure that it does not contain any sequences.
2. Copy the GetReportFileName callback sequence from the <TestStand> \Components\Modules\NI_SemiconductorModule\Templates\SemiconductorModuleCallbacks.seq 
 file to the <TestStand
 Public> \Components\Callbacks\NI_SemiconductorModule\SemiconductorModuleCallbacks.seq 
 file and make changes to the copy. You can use the
 ModelPlugin ,
 ModelThreadType ,
 ModelData ,
 LotSettings ,
 StationSettings ,
 StartDate , and
 StartTime sequence parameters, as
 necessary, to assign a value to the
 ReportFileName sequence parameter
 and optionally to the
 ReportDestinationDirectory sequence
 parameter.

Parent topic:

Reports and Data Logs (TSM)

Related concepts:

- GetReportFileName Callback (TSM)
- TSM Application API

Related information:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand-semiconductor-module path=reports-and-data-logs.html language=enus -->
## TOPIC 00242: Reports and Data Logs (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `reports-and-data-logs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/reports-and-data-logs.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate the following types of TSM reports and data logs. Enable and configure the corresponding TSM result processing plug-in to generate the report or data log. Standard Test Data Format (STDF) Log—Standard file format for storing test station information, lot information, and semiconduct

### Reports and Data Logs (TSM)

You can generate the following types of TSM reports and data logs. Enable and configure the corresponding TSM result processing plug-in to generate the report or data log.

- Standard Test Data Format
 (STDF) Log—Standard file format for storing
 test station information, lot information, and semiconductor
 test result data. Use the STDF Log to generate an STDF log
 file that complies with the STDF version 4 specification.
 Use the STDF Log Options dialog box to
 specify settings for the STDF log.
- Lot Summary
 Report—Text file that contains a summary of the
 semiconductor test results for the current lot of DUTs (test
 lot). Use the Lot Summary Report to gather lot, site,
 software bin, and hardware bin results in a human-readable
 ASCII text format. Use the Lot Summary Options dialog box
 to specify settings for the Lot Summary Report.
- Debug Test Results Log—Human-readable text file that contains the measurement values and test limits for each test that executes on each site. The Debug Test Results Log result processor generates separate files for each site in the test program. Use the Debug Test Results Log to debug measurements and test configurations as a lot executes. Use the Debug Test Results Log Options dialog box to specify settings for the Debug Test Results Log.
 Note Enabling the Debug Test Results Log might affect the performance of a test program.
- CSV Test Results
 Log—Human-readable text file that contains data in a
 comma-separated values text file, which provides better
 performance than the Debug Test Results Log result processor in a
 production environment. The CSV Test Results Log result
 processor generates a single file for all sites in the test
 program. You can open the .csv file
 directly in a spreadsheet application for analysis or to
 correlate test results. Use the CSV Test Results Log Options
 dialog box to specify settings for the CSV Test Results
 Log.

Note

- Keeping the Report pane open during execution negatively
 affects performance.
- The STDF Log, the Debug Test Results Log, and the CSV
 Test Results Log contain only semiconductor test
 result data from
 Semiconductor Multi Test
 steps. These data logs do not contain result data
 from other types of steps. If you use a
 Sequence Call
 step to call a sequence that contains Semiconductor
 Multi Test steps, the data logs do contain the test
 result data from those steps unless you use the Use
 New Thread sequence call option or the Use New
 Execution sequence call option. When using these
 sequence call options to execute a sequence
 asynchronously, you must use a
 Wait
 step to wait for the thread or execution for the
 data logs to contain the test result data from the
 sequence.
- You can configure the Lot Summary Report and Debug Test
 Results Logs in the
 Result Processing
 dialog box to display in the Report pane in the
 sequence editor and in the reports dialog box in the
 default operator interface. You cannot view the STDF
 Log or CSV Test Results Log in the sequence editor
 or default operator interface.

You can disable result recording by selecting the Disable Result Recording for All Sequences option on the Execution tab of the Station Options dialog box.

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- STDF Log Options Dialog Box (TSM)
- Lot Summary Reports (TSM)
- Debug Test Results Log Options Dialog Box (TSM)
- Debug Test Results Logs (TSM)
- CSV Test Results Logs (TSM)
- CSV Test Results Log Options Dialog Box (TSM)
- Semiconductor Multi Test Step

Related tasks:

- Enabling and Configuring TSM Result Processing Plug-ins

<!--NI_TOPIC bundle=teststand-semiconductor-module path=restore-tsm-ui-config.html language=enus -->
## TOPIC 00243: Restoring TSM UI Configuration to Default State

- bundle_id: `teststand-semiconductor-module`
- source_path: `restore-tsm-ui-config.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/restore-tsm-ui-config.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to restore the default TSM UI Configuration Select ConfigureSequence Editor Options and click the UI Configuration tab. Select NI_SemiconductorModule in the Saved Configurations list and click the Delete Selected button to delete the UI configuration. Select Semiconducto

### Restoring TSM UI Configuration to Default State

Complete the following steps to restore the default TSM UI Configuration

1. Select Configure»Sequence Editor Options and click the
 UI Configuration
 tab.
2. Select NI_SemiconductorModule in the Saved Configurations list and click the Delete Selected button to delete the UI configuration.
3. Select Semiconductor Module»Disable Semiconductor Module to disable TSM.
4. Select Semiconductor Module»Enable Semiconductor Module to re-enable TSM, which loads the default TSM
 UI Configuration
 NI_SemiconductorModule .

Parent topic:

TSM Sequence Editor UI Configuration

<!--NI_TOPIC bundle=teststand-semiconductor-module path=retesting-a-dut.html language=enus -->
## TOPIC 00244: Retesting a DUT (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `retesting-a-dut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/retesting-a-dut.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can initiate a retest from the TestStand Sequence Editor, an operator interface, or a handler/prober. The STDF log file includes retest information. Manually Initiating a Retest from the TestStand Sequence Editor or Operator Interfaces Click the Retest button on the TSM toolbar or in the Lot Sta

### Retesting a DUT (TSM)

You can initiate a retest from the TestStand Sequence Editor, an operator interface, or a handler/prober. The STDF log file includes retest information.

#### Manually Initiating a
 Retest from the TestStand Sequence Editor or Operator
 Interfaces

Click the Retest button
 on the TSM toolbar or in the Lot Statistics Viewer while execution
 is paused to manually initiate a retest. In a custom operator
 interface, you can create a button bound to the
 PerformSinglePartRetest command to
 perform the same functionality as the Retest
 button.

When you manually initiate a retest, TSM retests the
 DUT without calling the EndOfTest or StartOfTest callbacks in the
 handler/prober driver and discards the bin results of the previous
 test for the retested DUT.

#### Initiating a Retest
 from a Handler/Prober

A handler/prober can initiate a
 retest by sending a Part ID or part die coordinates that match a
 previously tested part. TSM detects this condition, tracks the test
 as a retest of the previous matching DUT, discards the bin results
 of the previous test for that DUT, and does not increment the part
 counts.

#### STDF File Contents
 after Retesting a DUT

When you retest a DUT, the STDF file
 includes the PIR, PRR, PTR, and FTR records for every test run,
 including retests. The WRR, PCR, HBR, and SBR summary records
 include only the results of the last retest and do not include
 retested results. The TSR summary record includes the counts of all
 tests run, including retests.

Related concepts:

- Standard Test Data Format (STDF) Log (TSM)
- Lot Statistics Viewer (TSM)
- EndOfTest Handler/Prober Driver Entry Point (TSM)
- StartOfTest Handler/Prober Driver Entry Point (TSM)

Related reference:

- Semiconductor Module Toolbar Buttons

<!--NI_TOPIC bundle=teststand-semiconductor-module path=runtime-data-viewer-publish.html language=enus -->
## TOPIC 00245: Viewing TSM Data at Publish Time

- bundle_id: `teststand-semiconductor-module`
- source_path: `runtime-data-viewer-publish.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/runtime-data-viewer-publish.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the TSM Runtime Data Viewer to view test results and triggered alarms and debug a test program at publish time. Set a breakpoint on your code module after a call to the Publish Data VI or Publish method. Open the Runtime Data Viewer from Semiconductor Module Show Runtime Data Viewer . Start test

### Viewing TSM Data at Publish Time

Runtime Data
 Viewer

1. Set a breakpoint on your code module after a call to the Publish
 Data VI or Publish method.
2. Open the Runtime Data Viewer from Semiconductor Module»Show Runtime Data Viewer.
3. Start testing by clicking Start Lot or Single
 Test on the TSM toolbar. 
 Your test program executes and then suspends at the breakpoint.
4. View your data in the Runtime Data Viewer. 
 Note On the first run of a new lot, test results
 published at a breakpoint in a code module are displayed in the
 Detailed view of the Runtime Data Viewer
 only. For subsequent batch runs, publish time values are displayed in both
 the Summary and Detailed
 views. The publish-time values are not evaluated against limits until after
 the code module returns to TestStand.

Viewing TSM Data at Runtime

Runtime Data Viewer

Parent topic:

Viewing TSM Data at Runtime

<!--NI_TOPIC bundle=teststand-semiconductor-module path=runtime-data-viewer.html language=enus -->
## TOPIC 00246: Viewing TSM Data at Runtime

- bundle_id: `teststand-semiconductor-module`
- source_path: `runtime-data-viewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/runtime-data-viewer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Runtime Data Viewer to view test results and triggered alarms in order to debug issues at runtime. To start logging, open the Runtime Data Viewer from Semiconductor Module Show Runtime Data Viewer . Start testing by clicking Start Lot or Single Test on the TSM toolbar. You can specify the nu

### Viewing TSM Data at Runtime

Runtime Data Viewer

1. To start logging, open the Runtime Data Viewer from Semiconductor Module»Show Runtime Data Viewer.
2. Start testing by clicking Start Lot or Single
 Test on the TSM toolbar. 
 Note You can specify the number of batches to store in memory in the
 Max History setting. To access this setting,
 click the gear icon ([IMAGE alt='Settings' src='GUID-07CDD7C4-6F49-4194-B5B5-3D7487DE4B98-a5.png']) in the top right of the Runtime Data Viewer window.
 Controlling the number of batches frees memory resources. This setting does
 not affect data logged by report plugins.
3. Click between the following tabs to view your data in different formats.
  - Summary —Each row represents a test and each column represents a
 part. Runtime Data Viewer adds new parts on the left as the tests
 proceed. Runtime Data Viewer shows the test result value for
 numeric tests and a blank cell for pass/fail tests. For each result, a
 green-colored cell indicates a passed test, a red-colored cell indicates
 a failed test, and red borders indicate a triggered alarm.
  - Detailed — Runtime Data Viewer shows each test on each
 part in the order of execution.
4. Optional: 
 Filter the data you view.
  - Click on the Summary tab to apply and configure
 filters. You can also specify the maximum number of columns (parts) to show.
 Fewer visible results improve Runtime Data Viewer 
 performance.
  - Click on the Detailed tab to show or hide columns.
 You can also limit the number of results to the last specified number of
 batches. Fewer visible results improve Runtime Data Viewer 
 performance.
  - Click on each column on the Detailed tab to set filters
 for the selected column.
5. Optional: 
 Click [IMAGE alt='Copy filtered list to clipboard' src='GUID-2F4A27B5-3334-427B-ABBD-22126CDD4048-a5.png'] to copy the filtered data.
6. Optional: 
 Click [IMAGE alt='Clear all test results' src='GUID-6D07B701-0065-4021-8F4C-E752306F8B49-a5.png'] to clear all results. 
 Runtime Data Viewer automatically clears all results when you start a new lot.
7. To stop logging, close the Runtime Data Viewer.

Parent topic:

Dialog Boxes and Windows

<!--NI_TOPIC bundle=teststand-semiconductor-module path=runtime-error-dialog.html language=enus -->
## TOPIC 00247: Semiconductor Module Run-Time Error Dialog Box

- bundle_id: `teststand-semiconductor-module`
- source_path: `runtime-error-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/runtime-error-dialog.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Semiconductor Module Run-Time Error dialog box launches when a run-time error occurs in an execution that uses a process model if TSM is enabled. The dialog box contains a description of the error and the step, sequence, and sequence file where the error occurred. The dialog box includes an erro

### Semiconductor Module Run-Time Error Dialog Box

The Semiconductor Module Run-Time Error dialog box launches when a run-time error occurs in an execution that uses a process model if TSM is enabled. The dialog box contains a description of the error and the step, sequence, and sequence file where the error occurred. The dialog box includes an error code only for TestStand errors unrelated to TSM. Use the More Options and Fewer Options buttons to show or hide the controls that specify how to handle the run-time error.

The Semiconductor Module Run-Time Error dialog box contains the following run-time error handling options:

- End lot after running cleanup —Execution proceeds to the Cleanup step group for the sequence, and lot testing ends.
- Run cleanup and continue testing —Execution proceeds to the Cleanup step group for the sequence, and lot testing continues with the next DUT.
- Retry —TestStand executes the step again.
- Ignore —TestStand does not set the status of the sequence to Error . Instead, TestStand sets the Error.Occurred property of the step to False , and execution continues normally with the next step in the sequence. The Result.Status property of the step remains set to Error .
- Abort immediately —TestStand stops execution immediately without running any Cleanup steps.

The text on the following buttons change depending on the option you select for handling the run-time error:

- Break, Then Option —TestStand suspends execution at the step that caused the run-time error. If you resume the execution after closing the dialog box, TestStand performs the actions for the selected run-time error handling option as described above. This button is hidden when you select the Abort immediately option.
- Option —TestStand performs the actions for the selected run-time error handling option as described above.

The Semiconductor Module Run-Time Error dialog box also provides the following options that change how TestStand handles subsequent run-time errors:

- Do this for all Run-Time Errors in this Execution —Performs the selected run-time error handling option for any run-time errors that occur later in the execution without displaying the Semiconductor Module Run-Time Error dialog box.
- Do this for all Run-Time Errors in this Batch —Performs the selected run-time error handling option for any run-time errors that occur later in any execution that is associated with the current batch without displaying the Semiconductor Module Run-Time Error dialog box. This option is available only when you use the Batch process model.

Parent topic:

Dialog Boxes and Windows

Related information:

- Batch Process Model

<!--NI_TOPIC bundle=teststand-semiconductor-module path=save-data-in-erformance-analyzer.html language=enus -->
## TOPIC 00248: Saving Data in the Test Program Performance Analyzer (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `save-data-in-erformance-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/save-data-in-erformance-analyzer.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can export the data set(s) the Test Program Performance Analyzer displays as an image or as a comma-separated values file. Click the Export Graph to .PNG button to export the current graph display as a .png file. Click the Export Log Files(s) button to export the filtered data set the current gr

### Saving Data in the Test Program Performance Analyzer (TSM)

You can export the data set(s) the Test Program Performance Analyzer displays as an image or as a comma-separated values file.

Click the Export Graph to .PNG button to export the current graph display as a .png file.

Click the Export Log Files(s) button to export the filtered data set the current graph displays to a new .csv file. If you are comparing data sets in the analyzer, TSM creates two .csv files of the filtered data the graph displays.

Parent topic:

Test Program Performance Analyzer (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=scaling-measurement-and-limit-data.html language=enus -->
## TOPIC 00249: Scaling Measurement and Limit Data (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `scaling-measurement-and-limit-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/scaling-measurement-and-limit-data.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Scaling Factor column in the Tests table on the Tests tab of the Semiconductor Multi Test step and the Semiconductor Sequence Call step to specify the scaling factor for the base units for test limits and measurements. Changing the scaling factor in the Scaling Factor column in the Tests tab

### Scaling Measurement and Limit Data (TSM)

Use the Scaling Factor column in the Tests table on the Tests tab of the Semiconductor Multi Test step and the Semiconductor Sequence Call step to specify
 the scaling factor for the base units for test limits and measurements.

Changing
 the scaling factor in the Scaling Factor column in the Tests table sets the same scaling factor for the limits
 and the measurement.

To specify different scaling factors for each limit and the measurement, use the Property Browser
 panel on the Properties tab of the Step Settings pane and set the following
 properties:

| Property | Description |
| --- | --- |
| Step.Result.Evaluations[i].NumericLimit.DataScalingExponent | Measurement scaling factor |
| Step.Result.Evaluations[i].NumericLimit.LowLimitScalingExponent | Low limit scaling factor |
| Step.Result.Evaluations[i].NumericLimit.HighLimitScalingExponent | High limit scaling factor |

The Semiconductor Multi Test step and the Semiconductor Sequence Call step use the scaling factors
 in the following ways:

- Measurement Value Scaling Factor —The steps assume the measurement values that code
 modules publish use base units. At
 run time, the steps use the measurement
 scaling factor to display the measurement value in scaled units in the Data column of the Tests table. The
 STDF Log result processing plug-in stores the corresponding scaling
 exponent in the RES_SCAL field of the PTRs. The Debug Test Results Log result processing plug-in uses the
 measurement scaling factor to format the values and units in the Measurement Value column of the Debug Test
 Results Log.
- Limits Scaling Factors —The steps assume the limit values in the Low Limit and High
 Limit columns use scaled units. At
 run time, the steps use the limit scaling
 factors to convert the limit values to base units to compare the measurement value to the limit values. The
 STDF Log result processing plug-in stores the corresponding scaling
 exponents for the low limit and high limit scaling factors in the LLM_SCAL and HLM_SCAL fields of the PTRs.
 The Debug Test Results Log result processing plug-in uses the limit scaling factors to add units to the
 values in the Low Limit and High Limit columns of the Debug Test Results Log.

#### Supported Scaling Factors

TSM
 recognizes the following scaling factors, which correspond to the recognized values for the
 RES_SCAL, HLM_SCAL, and LLM_SCAL fields of the STDF Parametric Test Records
 (PTRs):

| Scaling Factor Name | Scaling Factor Value | Units Prefix | DataScalingExponent, LowLimitScalingExponent, and HighLimitScalingExponent Property Values | STDF _SCAL Field Value |
| --- | --- | --- | --- | --- |
| femto | 10-15 | f | -15 | 15 |
| pico | 10-12 | p | -12 | 12 |
| nano | 10-9 | n | -9 | 9 |
| micro | 10-6 | u | -6 | 6 |
| milli | 10-3 | m | -3 | 3 |
| percent | 10-2 | % | -2 | 2 |
| <blank> | 1 |  | 0 | 0 |
| kilo | 103 | K | 3 | -3 |
| mega | 106 | M | 6 | -6 |
| giga | 109 | G | 9 | -9 |
| tera | 1012 | T | 12 | -12 |

Parent topic:

Tests Tab

Related concepts:

- Tests Tab
- Semiconductor Multi Test Step
- Semiconductor Sequence Call Step
- Reports and Data Logs (TSM)

<!--NI_TOPIC bundle=teststand-semiconductor-module path=schema-version-policy.html language=enus -->
## TOPIC 00250: Schema Version Policy (TSM)

- bundle_id: `teststand-semiconductor-module`
- source_path: `schema-version-policy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-semiconductor-module/raw/resource/enus/schema-version-policy.html
- document_id: `teststand-semiconductor-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: The schema version uses a major.minor notation. The version of the schema reflects changes to the schema, not changes to TSM. Changes to the schema version indicate breaking changes to the schema. TSM does not load files that use a later schema version than the version specified for that version of

### Schema Version Policy (TSM)

The schema version uses a major.minor notation. The version of the
 schema reflects changes to the schema, not changes to TSM.

Changes to the schema version indicate breaking changes to the schema. TSM does not
 load files that use a later schema version than the version specified for that
 version of TSM.

Use the following table to map schema versions and TSM versions.

| Schema Version | TSM Version |
| --- | --- |
| PinMap.xsd version 1.0 BinDefinitions.xsd version 1.0 | NI TestStand 2013 Semiconductor Module |
| PinMap.xsd version 1.1 BinDefinitions.xsd version 1.1 Specifications.xsd version 1.0 | NI TestStand 2014 Semiconductor Module |
| PinMap.xsd version 1.2 BinDefinitions.xsd version 1.1 Specifications.xsd version 1.0 | NI TestStand 2014 Semiconductor Module SP1 NI TestStand 2016 Semiconductor Module |
| PinMap.xsd version 1.3 BinDefinitions.xsd version 1.1 Specifications.xsd version 1.0 | NI TestStand 2016 SP1 Semiconductor Module |
| PinMap.xsd version 1.4 BinDefinitions.xsd version 1.1 Specifications.xsd version 1.0 | NI TestStand 2017 Semiconductor Module |
| PinMap.xsd version 1.5 BinDefinitions.xsd version 1.1 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.0 | NI TestStand 2019 Semiconductor Module |
| PinMap.xsd version 1.6 BinDefinitions.xsd version 1.2 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.1 | NI TestStand 2020 Semiconductor Module TestStand 2020 Semiconductor Module 2021 Q4 |
| PinMap.xsd version 1.7 BinDefinitions.xsd version 1.2 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.1 | TestStand 2021 Semiconductor Module 2022 Q2 |
| PinMap.xsd version 1.7 BinDefinitions.xsd version 1.2 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.4 | TestStand 2021 Semiconductor Module 2023 Q1 |
| PinMap.xsd version 1.7 BinDefinitions.xsd version 1.2 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.5 | TestStand 2023 Semiconductor Module 2024 Q1 |
| PinMap.xsd version 1.9 BinDefinitions.xsd version 1.2 Specifications.xsd version 1.0 SystemConfiguration.xsd version 1.6 | TestStand 2023 Semiconductor Module 2024 Q3 |

Parent topic:

Pin Map File XML Structure (TSM)
