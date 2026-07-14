# NI DOCUMENT BUNDLE: flexlogger

<!--NI_BUNDLE_CHUNK bundle=flexlogger start=1 end=96 -->
<!--NI_TOPIC bundle=flexlogger path=accessing-ni-documentation.html language=enus -->
## TOPIC 00001: Accessing the Documentation

- bundle_id: `flexlogger`
- source_path: `accessing-ni-documentation.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/accessing-ni-documentation.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can find the most up-to-date documentation for your NI products online on ni.com/docs. By default, links from your NI product open the online NI Product Documentation Center. If you do not have internet access, you can update your NI Help Preferences to use the NI Offline Help Viewer. The NI Off

### Accessing the Documentation

You can find the most up-to-date documentation for your NI products online on
 ni.com/docs.

By default, links from your NI product open the online *NI Product Documentation
 Center*. If you do not have internet access, you can update
 your NI Help Preferences to use the NI Offline Help Viewer. The NI Offline
 Help Viewer is automatically installed with supported products and provides
 a similar experience to the online documentation.

Related information:

- Using the NI Offline Help Viewer
- How to Use the NI Product Documentation Center

<!--NI_TOPIC bundle=flexlogger path=adding-a-pdk-plug-in.html language=enus -->
## TOPIC 00002: Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project

- bundle_id: `flexlogger`
- source_path: `adding-a-pdk-plug-in.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-a-pdk-plug-in.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Extend the functionality of FlexLogger by adding a custom plug-in to your project using the FlexLogger Plug-in Development Kit. Introduced in FlexLogger 2019 R3FlexLogger installs with some plug-ins by default, such as the Min-Max plug-in and the Output Sequencer plug-in. The Min-Max plug-in helps y

### Adding a FlexLogger Plug-In Development Kit
 Plug-In to Your Project

Extend the functionality of FlexLogger by adding a custom plug-in to your project
 using the FlexLogger Plug-in Development Kit.

Introduced in FlexLogger 2019 R3

Note

Note

#### FlexLogger Plug-In Development Kit Overview

The FlexLogger Plug-In Development Kit allows you to interact with third-party hardware and
 write custom calculations. Create FlexLogger plug-ins in LabVIEW and import the plug-ins to
 operate within the FlexLogger environment.

The FlexLogger Plug-In Development Kit guides you through planning, creating, and testing
 your custom plug-ins in LabVIEW. FlexLogger automatically generates the user interface for
 configuring plug-in measurements after you import the plug-ins.

To create and configure your custom plug-in, install the FlexLogger Plug-In Development Kit
 from NI Package Manager. For complete information on how to create and configure a
 FlexLogger plug-in, refer to the *FlexLogger Plug-In Development Kit User
 Manual*.

Complete the following steps to add your custom plug-in to
 your FlexLogger project.

1. On the Channel Specification toolbar, select Add channels»Plug-in and select the desired plug-in from the menu. 
 When FlexLogger detects valid plug-ins, Plug-in appears as an
 option for the Add channels button. FlexLogger loads plug-ins from
 the following location: %public%\Documents\National
 Instruments\FlexLogger\Plugins\IOPlugins. For more information on importing
 plug-ins into FlexLogger, refer to the *FlexLogger Plug-In Development Kit User
 Manual*. 
 The selected plug-in appears in the Channel Specification
 under its host system.
2. Select Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] at the right edge of
 the plug-in header to open the plug-in parameters configuration dialog.
3. Hover over an individual channel to see the Configure gear
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] for that channel. Select the gear to open the dialog box for the
 channel parameters configuration. 
 FlexLogger applies channel-level parameters only to the selected
 channel.

You can find PDK plug-ins for many new
 capabilities on the FlexLogger Community Plug-Ins repository on GitHub.

Parent topic:

Adding a Plug-In to Your Project

Related information:

- FlexLogger Plug-in Development Kit Manual
- FlexLogger Community Plug-ins Repository

<!--NI_TOPIC bundle=flexlogger path=adding-a-plug-in.html language=enus -->
## TOPIC 00003: Adding a Plug-In to Your Project

- bundle_id: `flexlogger`
- source_path: `adding-a-plug-in.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-a-plug-in.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug-ins allow you to extend the functionality of FlexLogger and create specialized analysis, integration, and automation capabilities for your project. Running FlexLogger projects that contain plug-ins requires a FlexLogger Professional license. Refer to FlexLogger Editions for more information.

### Adding a Plug-In to Your Project

Plug-ins allow you to extend the functionality of FlexLogger and create specialized
 analysis, integration, and automation capabilities for your project.

Note

FlexLogger Editions

- [Choosing What Type of Plug-in to Develop for Your Project](choose-plug-in.html) You can add custom functionality to FlexLogger by developing a plug-in using the FlexLogger Plug-In Development Kit , or by creating a Measurement plug-in.
- [Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project](adding-a-pdk-plug-in.html) Extend the functionality of FlexLogger by adding a custom plug-in to your project using the FlexLogger Plug-in Development Kit.
- [Adding a Measurement Plug-In to Your FlexLogger Project](adding-measurement-plugin.html) Extend the functionality of FlexLogger by adding a measurement plug-in to your project.

Parent topic:

Extending FlexLogger Functionality

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adding-alarms.html language=enus -->
## TOPIC 00004: Adding an Alarm

- bundle_id: `flexlogger`
- source_path: `adding-alarms.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-alarms.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Channel Configuration to monitor your signals and trigger an alarm when the selected value conditions are met. Introduced in FlexLogger 2019 R3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Select one or more chann

### Adding an Alarm

Use the Channel Configuration to monitor your signals and trigger an alarm when the
 selected value conditions are met.

Introduced in FlexLogger 2019 R3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. Select one or more channels you wish to add an alarm to.
2. Hover over a channel row to see the Configure gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. Click the gear for the channel you wish
 to add an alarm to.
3. Select the Alarms tab in the Channel Configuration dialog.
4. Based on the channel type, specify one of the following actions to monitor to trigger
 the alarm: 
 Table 33.Channel Alarm OptionsChannel Type
 Option
 DescriptionAnalog
 Rises above value
 Alarm is triggered when the signal value rises above the specified
 value.
 Falls below value
 Alarm is triggered when the signal value falls below the specified
 value.
 Enters range
 Alarm is triggered when the signal value enters the specified
 range.
 Leaves range
 Alarm is triggered when the signal leaves the specified range.
 Digital
 Is low
 Alarm is triggered when the signal transitions to low (0).
 Is high
 Alarm is triggered when the signal transitions to high (1).
5. Select the alarm types you wish to enable: Critical and
 Warning.
6. Specify the values for the alarm type you are using. 
 Note 
 If you are using both alarm types, the values specified for the
 Critical alarm must be more restrictive than the
 Warning alarm values.
 Values are also constrained by the Physical Minimum and
 Physical Maximum range specified in the Channel
 Configuration. Alarm values set outside of the Physical range will be coerced to
 within the set Physical limits.
7. For analog input channels, specify the Hysteresis. Hysteresis is
 the threshold relative to the alarm value. Specify the hysteresis to prevent FlexLogger
 from clearing the alarm if the data varies due to noise or jitter in the signal.

Alarms are enabled when the test is running. Alarm conditions are not monitored when the
 test is not running.

Parent topic:

Configuring I/O Channels

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adding-event.html language=enus -->
## TOPIC 00005: Adding an Event

- bundle_id: `flexlogger`
- source_path: `adding-event.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-event.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Test Specification to create an event trigger to generate a response from your system. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. In your Test Specification document, click Add Event to launch the Configure Even

### Adding an Event

Use the Test Specification to create an event trigger to generate a response from
 your system.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. In your Test Specification document, click Add Event to launch
 the Configure Event dialog.
2. Create the If condition that will trigger the event. 
 Table 46.Options for Event If ConditionOption
 DescriptionChannel value change
 Click Select channel in the
 If condition section and map to a configured
 channel that the event will monitor for a value change.
 Specify the type of Value change the
 If condition will use to determine the event
 trigger.
 Specify the data Value that will trigger the
 event.
 For analog triggers, specify the Hysteresis for the
 If condition, which is the threshold relative to
 the Value, to prevent re-triggering of the event if
 the data varies due to noise or jitter in the signal.
 Critical alarm on channel(s)
 Click Select channel in the
 If condition section and map to channel(s) that have
 configured Critical alarms.
 Warning alarm on channel(s)
 Click Select channel in the
 If condition section and map to channel(s) that have
 configured Warning alarms.
 Test time elapsed
 Specify the total duration time of the test. When the test duration is
 complete, the event will trigger the output action.
 Test stopped
 Select to trigger the output action when the test is manually or
 automatically stopped.
 Button pressed
 Click Select action button in the
 If condition section and choose an action button on the
 Screen document.
 Note Multiple events set to trigger on the
 same condition execute asynchronously and the order of execution cannot be controlled by
 the user.
3. Create the Then condition that will determine the action
 generated by the event. 
 Table 47.Options for Event Then ConditionOption
 DescriptionSet analog output
 Click Select channel in the
 Then condition section and map to a configured
 channel that the event controls.
 Specify the Value to generate.
 Set digital output
 Click Select channel in the
 Then condition section and map to a configured
 channel that the event controls.
 Specify the Value to generate.
 Reset output channels
 Click Select channel in the
 Then condition section and map to a channel with
 enabled reset values.
4. Click OK to create the event. 
 The event appears and can be edited or deleted from the Test
 Specification document.
5. Click RUN to begin the test and enable the event. 
 You can disable or enable an event while running a test. To disable/enable the event
 during testing, hover over the event row and click Disable.

Notice

Parent topic:

Defining Your Test Configuration

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adding-measurement-plugin.html language=enus -->
## TOPIC 00006: Adding a Measurement Plug-In to Your FlexLogger Project

- bundle_id: `flexlogger`
- source_path: `adding-measurement-plugin.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-measurement-plugin.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Extend the functionality of FlexLogger by adding a measurement plug-in to your project. Before adding a measurement plug-in to your FlexLogger project, you must first develop the measurement plug-in using LabVIEW or Python. Refer to the Measurement Plug-Ins User Manual for more information. On the C

### Adding a Measurement Plug-In to Your
 FlexLogger Project

Extend the functionality of FlexLogger by adding a measurement plug-in to your
 project.

Measurement Plug-Ins User Manual

1. On the Channel Specification toolbar, select Add channels»Measurement Plug-in. 
 A configuration dialog opens.
2. Click Data source and select the desired measurement
 plug-in from the menu. 
 Note The menu displays all discoverable measurement
 plug-ins on your system. 
 FlexLogger immediately runs the measurement plug-in after you select it
 from the menu. The plug-in runs continuously with the default values until you
 change the input values in the configuration dialog. FlexLogger continuously
 runs the plug-in regardless if you develop the measurement plug-in to run only
 once and finish.Tip You can add multiple
 measurement plug-ins to a FlexLogger project. You can also add multiple
 instances of the same measurement plug-in to your channel specification. To
 differentiate between instances, enter a unique Display
 name in the configuration dialog.
3. In the configuration dialog for the plug-in, configure the input values. 
 You must configure any repeated inputs to point to another channel in your
 FlexLogger project.
 If the measurement plug-in has repeated inputs, FlexLogger applies the
 maximum sample rate of the input channels to all output channels. If there
 are no repeated inputs, each output has a configurable data type value. To
 change the sample rate of the output channels, configure the
 dt parameter.

Create channel

Parent topic:

Adding a Plug-In to Your Project

Related information:

- Measurement Plug-Ins User Manual

<!--NI_TOPIC bundle=flexlogger path=adding-metadata-to-a-project.html language=enus -->
## TOPIC 00007: Adding Test Properties to a Project

- bundle_id: `flexlogger`
- source_path: `adding-metadata-to-a-project.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-metadata-to-a-project.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add test properties to your project to include supplemental information in your log files. Introduced in FlexLogger 2018 R4 You can use test properties as placeholders when you configure your log file name and location. Refer to Using Test Metadata as Placeholders for Log File Names and Locations fo

### Adding Test Properties to a Project

Add test properties to your project to include supplemental information in your log
 files.

Introduced in FlexLogger 2018 R4

Note

Using Test
 Metadata as Placeholders for Log File Names and Locations

1. Optional: 
 In your Logging Specification, specify values for the
 Operator and DUT in the
 Test properties section. 
 The fields for Operator and DUT
 are auto-populated, but can be changed or deleted. The logged-in user account
 name is the default value for Operator.
2. To add arbitrary test properties, click Add property. 
 FlexLogger adds a new line to the table.
3. Enter the Property name and Property
 value. Use the following guidelines. 
 Property names must begin with a letter and cannot contain symbols. Duplicate
 property names will automatically be appended with sequential numbering.
 Property values can begin with or contain any characters supported by your system
 encoding.
4. Select Prompt on start for any test properties that you
 wish to be reminded to update before the test begins.

Data

Figure 9.

[IMAGE alt='image' src='GUID-41D68E61-F60B-4A0A-868D-787AE342D47D-a5.png']

Parent topic:

Configuring a Log File

Related tasks:

- Using Test Metadata as Placeholders for Log File Names and Locations

<!--NI_TOPIC bundle=flexlogger path=adding-signals-to-can-lin.html language=enus -->
## TOPIC 00008: Adding Signals to Your CAN/LIN Module Channel Specification

- bundle_id: `flexlogger`
- source_path: `adding-signals-to-can-lin.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-signals-to-can-lin.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure your CAN or LIN module for use in your application by adding signals to the Channel Specification. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Before adding CAN and LIN signals to your Channel Specifica

### Adding Signals to Your CAN/LIN Module Channel Specification

You can configure your CAN or LIN module for use in your application by adding
 signals to the Channel Specification.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Before adding CAN and LIN signals to your Channel Specification, you might need to create
 or manage the databases that provide the signal definitions and scaling information for your
 application.

1. Click theAdd Signals button on the port that you wish to configure.
2. Using the 
 Database drop-down menu, select the database file that contains your signal definitions.
3. Using the 
 Cluster drop-down menu, select the desired cluster from your database. 
 All available frames and the signals they contain display in the
 Signals pane.
4. (CAN only) Select an Application
 protocol to apply to the database, if necessary.
5. (LIN only) The Current Interface Schedule
 Settings displays the LIN schedule used by the database. 
 The Signals pane displays schedule information alongside the
 corresponding frames in the Signals pane. The details column of
 the corresponding signal in the Channel Specification also
 displays this information.
6. Specify the signal Direction.
7. Check the associated boxes next to any signals you wish to add to the associated port. To select all signals within the frame, check the associated box next to the frame. 
 Note The Signals pane
 is organized by frames. Each frame contains a grouping of signals. The Signals Search
 filter searches for signal names only. Complete the following steps to locate a specific
 frame within the database:Search for a signal contained by the frame.
 Select the signal.
 Clear the search results.
 Note Frames cannot be in use on the same
 port in more than one program at a time. For example, frames that are in use on port 1
 of a module in FlexLogger cannot be used on port 1 of that module in another program,
 and vice versa.
8. Click 
 OK. 
 The signals appear in the Channel specification under the associated port. Note FlexLogger automatically tries to connect
 to a CAN/LIN module when a signal is configured. To avoid this behavior, check
 Disable for any port to stop all signals and measurements on
 that port. FlexLogger closes all CAN/LIN connections to the port, allowing other
 software to use the port.
9. Optional: 
 For output signals, specify a channel output value or map the channel to a
 source.
  1. Hover over a channel row and click the Configure
 gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'].
  2. Specify the Output Value for the channel or map
 to an input channel to use as the channel Output
 Source.
  3. Click Done.

Parent topic:

Configuring an Automotive Bus

Related concepts:

- CAN Databases
- LIN Databases

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adding-user-notes.html language=enus -->
## TOPIC 00009: Adding User Notes to a Log File During a Running Test

- bundle_id: `flexlogger`
- source_path: `adding-user-notes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adding-user-notes.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add timestamped notes to your log file while the test is running. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. While the test is running, click the Add Note button in the toolbar. A dialog will open, timestamped with the

### Adding User Notes to a Log File During a Running Test

Add timestamped notes to your log file while the test is running.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. While the test is running, click the 
 Add Note button 
 [IMAGE alt='image' src='GUID-4C65A8BA-5F8D-463A-BCBD-69F32BE68B3D-a5.png'] in the toolbar. 
 A dialog will open, timestamped with the time the button was clicked.
2. Record any information you wish to include in the log file. 
 Note text will be added to the Channel Contents in your data log file.

[IMAGE alt='image' src='GUID-AC4C7F50-08E9-4C85-9A21-AE2A0D786557-a5.png']

Parent topic:

Running a Test

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adjusting-can-port-interface-settings.html language=enus -->
## TOPIC 00010: Adjusting Port/Interface Settings

- bundle_id: `flexlogger`
- source_path: `adjusting-can-port-interface-settings.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adjusting-can-port-interface-settings.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Change or configure the interface (port) settings from within FlexLogger in the Interface Settings dialog. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. CAN interfaces are software representations of physical ports. Comple

### Adjusting Port/Interface Settings

Change or configure the interface (port) settings from within FlexLogger in the
 Interface Settings dialog.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

CAN interfaces are software representations of physical ports. Complete the following steps to adjust the port settings.

1. Enable 
 Termination, if necessary. 
 Improperly configured Termination schemes might result in bus
 error frames or missed data. Refer to *High-Speed CAN Cable Termination* or
 *Low-Speed CAN Cable Termination* for more information on proper termination.
2. Enable the 
 Listen only option, if necessary. 
 Note If you have multiple nodes connected to an ECU, the 
 Listen only option can prevent acknowledgment activity on lines that do not require monitoring to interfere with the activity of lines being monitored. Also, if you are receiving data but the transmitting node is not receiving the acknowledgment, the 
 Listen only option can help prevent a bus load condition that could result in a fault. If you only have two nodes on the bus, 
 Listen only mode should be turned off to allow acknowledgments and prevent bus errors.
3. Use the 
 Baud rate pull-down menu to select an applicable baud rate to all clusters, if necessary. 
 Notice The port will use the
 baud rate that is defined by the selected database. A Baud rate
 set to an unsupported value might result in bus error frames or missed data.
4. (Optional) After the 
 Baud rate is selected, the option to 
 Enable raw frame logging is enabled. Selecting this option will allow FlexLogger to log data without associating the port to a database.
5. (FD baud rate) Select the applicable 
 I/O Mode to enable the 
 FD baud rate pull-down menu, if necessary. The following table explains the available I/O Modes. 
 Table 35.I/O Mode Options for CAN Baud RateOption
 DescriptionCAN
 The default CAN 2.0 standard I/O mode as defined in ISO 11898-1:2003. A
 fixed baud rate is used for transfer. The payload length is limited to 8
 bytes.
 CAN FD (FD baud rate enabled)
 The CAN FD mode as specified in the CAN with Flexible Data-Rate
 specification, version 1.0. Payload lengths up to 64 are allowed, but are
 transmitted at a single fixed baud rate.
 CAN FD + BRS (FD baud rate enabled)
 The CAN FD as specified in the CAN with Flexible Data-Rate specification,
 version 1.0, with the optional Baud Rate Switching enabled. The same payload
 lengths as CAN FD mode are allowed; additionally, the data portion of the CAN
 frame is transferred at a different (higher) baud rate.
6. Select the 
 FD baud rate from the pull-down menu to select an applicable fast data baud rate for all clusters.

Parent topic:

CAN Databases

Related reference:

- High-Speed CAN Cable Termination
- Low-Speed CAN Cable Termination

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=adjusting-lin-port-interface-settings.html language=enus -->
## TOPIC 00011: Adjusting Port/Interface Settings

- bundle_id: `flexlogger`
- source_path: `adjusting-lin-port-interface-settings.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/adjusting-lin-port-interface-settings.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: You can change or configure the interface (port) settings from within software using the Interface Settings dialog box, if necessary. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. LIN interfaces are software representation

### Adjusting Port/Interface Settings

You can change or configure the interface (port) settings from within software using
 the Interface Settings dialog box, if necessary.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

LIN interfaces are software representations of physical ports. Complete the following steps to adjust the port settings.

1. Enable 
 Termination, if necessary. 
 Notice Improperly configured
 Termination schemes might result in bus error frames or missed
 data. Refer to *LIN Cable Termination* for more information on proper
 termination.
 Note Termination settings can only be configured or changed when the test is
 not running.
2. Use the 
 Baud rate pull-down menu to select an applicable baud rate to all clusters, if necessary. 
 Notice The port will use the
 baud rate that is defined by the selected database. A Baud rate
 set to an unsupported value might result in bus error frames or missed data.
3. Optional: 
 After the Baud rate is selected, the option to Enable
 raw frame logging is enabled. Selecting this option will allow FlexLogger to
 log data without associating the port to a database.
4. Using the Database drop-down menu, select the database
 file that contains your signal definitions.
5. Using the Cluster drop-down menu, select the desired
 cluster from your database. 
 FlexLogger shows all available frames and the signals that the frames contain in the
 Signals pane.
6. Using the LIN schedule drop-down menu, select the
 desired LIN schedule. 
 Note The following considerations apply to LIN
 schedule assignment:
 Assigning a schedule to a LIN port automatically specifies that port as
 master.
 LIN ports will not show data if a master port is not specified.
 LIN schedules can only be configured or changed when the test is not
 running. 
 Schedule information will be displayed in the details column of the corresponding
 signal in the Channel Specification.

Parent topic:

LIN Databases

Related reference:

- LIN Cable Termination

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=applying-j1939-application-protocol.html language=enus -->
## TOPIC 00012: Applying J1939 Application Protocol

- bundle_id: `flexlogger`
- source_path: `applying-j1939-application-protocol.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/applying-j1939-application-protocol.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Apply J1939 Application protocol to your CAN signals. Click Add Signals on the CAN port you want to configure. Select the Database that contains the signals you want to update. Select the Cluster that contains the signals you want to apply J1939 to. Select J1939 from the Application protocol pull-do

### Applying J1939 Application Protocol

Apply J1939 Application protocol to your CAN signals.

1. Click 
 Add Signals on the CAN port you want to configure.
2. Select the Database that contains the signals you want to update.
3. Select the Cluster that contains the signals you want to apply J1939 to.
4. Select 
 J1939 from the 
 Application protocol pull-down menu.
5. Select the desired signals from the 
 Signals pane. 
 Note The Signals
 pane is organized by frames. Each frame contains a grouping of signals. The Signals
 Search filter searches for signal names only. To locate a specific frame within the
 database, search for a signal contained by the frame, select the signal, and then clear
 the search results.
6. Click 
 Okay.

Parent topic:

J1939 Application Protocol Basics

<!--NI_TOPIC bundle=flexlogger path=automatically-exporting-data-to-csv.html language=enus -->
## TOPIC 00013: Automatically Exporting Data Files to CSV File Format

- bundle_id: `flexlogger`
- source_path: `automatically-exporting-data-to-csv.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/automatically-exporting-data-to-csv.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure your Logging Specification to automatically export your data files to the CSV file format. Introduced in FlexLogger 2018 R3 On the Logging Specification document, select Export automatically to CSV file format when logging completes. Specify the CSV file data rate, if necessary. All logged

### Automatically Exporting Data Files to CSV File Format

Configure your Logging Specification to automatically export
 your data files to the CSV file format.

Introduced in FlexLogger 2018 R3

1. On the Logging Specification document, select Export
 automatically to CSV file format when logging completes.
2. Specify the 
 CSV file data rate, if necessary. 
 Note All logged data channels are mapped to a common CSV data rate. The CSV data rate is applied as follows: 
 The common CSV start time is the first time stamp of all logged channels.Each CSV time stamp uses the logged value in each channel that occurs just before or at the same time as the time stamp.This CSV data rate mapping runs while any channel provides data. Exported log files from mapped channels might contain gaps at the end if any channel stopped providing data.
3. Click the 
 Preferences button to set the export format settings, if desired.
4. Select File»Save All to save the Logging Specification for your project.

The data file export will begin automatically when the logging action completes.

Parent topic:

Viewing, Analyzing, and Exporting Data

<!--NI_TOPIC bundle=flexlogger path=automating-flexlogger-tests-using-python.html language=enus -->
## TOPIC 00014: Automating FlexLogger Tests Using Python

- bundle_id: `flexlogger`
- source_path: `automating-flexlogger-tests-using-python.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/automating-flexlogger-tests-using-python.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FlexLogger Python APIs to modify the configuration of existing FlexLogger projects and control the execution of FlexLogger test sessions. Introduced in FlexLogger 2020 R3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more informatio

### Automating FlexLogger Tests Using
 Python

Use the FlexLogger Python APIs to modify the configuration of existing
 FlexLogger projects and control the execution of FlexLogger test sessions.

Introduced in FlexLogger 2020 R3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Refer to the related information links to learn more about the FlexLogger Python API.

Parent topic:

Extending FlexLogger Functionality

Related information:

- Get started with the FlexLogger Python API.
- Learn about FlexLogger Python API classes and methods.
- Contribute to the FlexLogger Python API.
- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=calculation-formula-options.html language=enus -->
## TOPIC 00015: Calculation Formula Options

- bundle_id: `flexlogger`
- source_path: `calculation-formula-options.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/calculation-formula-options.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use standard math operators, functions, and constants to customize hardware channels. All formulas must adhere to the following rules: Every formula must contain a reference to at least one channel. Channel references are contained within single quotes ('channel name'). Element-wise calculation will

### Calculation Formula Options

Use standard math operators, functions, and constants to customize hardware channels.

All formulas must adhere to the following rules:

- Every formula must contain a reference to at least one channel.
- Channel references are contained within single
 quotes ('channel name').
- Element-wise calculation will be done when one of the operands is a channel or the parameter is a channel.
- Decimal separators on literal numbers must be periods. Alternative separators such as commas are not supported.
- Angle measurements must be reported in radians.

Refer to the following table for examples of formula formats that you can use to configure a calculated channel.

| Description | Formula Format | Example |
| --- | --- | --- |
| Element-wise arithmetic addition | 'channel name' + x | 'AI7' + 1 |
| 'channel name x' + 'channel name y' | 'AI7' + 'AI8' |  |
| Element-wise arithmetic subtraction | 'channel name' - x | 'AI7' - 1 |
| 'channel name x' - 'channel name y' | 'AI7' - 'AI8' |  |
| Element-wise arithmetic multiplication | 'channel name' * x | 'AI7' * 5 |
| 'channel name x' * 'channel name y' | 'AI7' * 'AI8' |  |
| Element-wise arithmetic division | 'channel name' / x | 'AI7' / 5 |
| 'channel name x' / 'channel name y' | 'AI7' / 'AI8' |  |
| Apply the function to the channel element | function('channel name') | sin('AI7') |
| Arithmetic equation | (x + y) * z / 'channel name' | (2 + 3) * 4 / 'AI7' |
| Number with scientific representation | 'channel name' + 1.23e-5 | 'AI8' + 1.23e-5 |
| Constant usage | function(constant * 'channel name') | sin(pi * 'AI7') See Supported Functions, Operators, and Constants table. |
| Unary plus (a no-op) | +'channel name' | +'AI7' |
| Power operator | 'channel name'^x | 'AI7'^3 or 'AI7'^0.5 |
| Unary minus | -'channel name' | -'AI7' |
| Note The data type for all numeric values is double-precision, floating-point. |  |  |

Refer to the following table for examples of formula elements that you can use to configure
 a calculated channel.

|  | Formula Element | Signal Type | Definition |
| --- | --- | --- | --- |
| Supported Functions | sin | Analog | Sine |
| cos | Analog | Cosine |  |
| tan | Analog | Tangent |  |
| arcsin | Analog | Inverse of sine |  |
| arccos | Analog | Inverse of cosine |  |
| arctan | Analog | Inverse of tangent |  |
| abs | Analog | Absolute value of any number |  |
| log | Analog | Logarithm |  |
| log10 | Analog | Common logarithm (logarithm to base 10) |  |
| Supported Operators | + | Analog | Addition |
| - | Analog | Subtraction |  |
| * | Analog | Multiplication |  |
| / | Analog | Division |  |
| ( ) | Analog, digital | Bracket; contents are evaluated first |  |
| ^ | Analog | Calculate the base raised to the power of the exponent You can use this operator to take the root of the base. For example, to take the square root, use x^0.5. |  |
| < | Analog | Less than |  |
| > | Analog | Greater than |  |
| <= | Analog | Less than or equal to |  |
| >= | Analog | Greater than or equal to |  |
| = | Analog, digital | Equal |  |
| != | Analog, digital | Not equal |  |
| & | Digital | Logical and |  |
| \| | Digital | Logical or |  |
| ~ | Digital | Negation |  |
| ? : | Analog, digital | Ternary operator indicating condition ? valueIfTrue : valueIfFalse. The data type of valueIfTrue and valueIfFalse must be the same. |  |
| Supported Constants | pi | Analog | Pi (π) constant |
| e | Analog | Natural logarithm base constant (𝑒) |  |
| true | Digital | Is TRUE |  |
| false | Digital | Is FALSE |  |

Parent topic:

Configuring Calculated Channels

<!--NI_TOPIC bundle=flexlogger path=calibrating-multiple-channels.html language=enus -->
## TOPIC 00016: Calibrating Multiple Channels Simultaneously

- bundle_id: `flexlogger`
- source_path: `calibrating-multiple-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/calibrating-multiple-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Calibrate more than one channel at the same time. Introduced in FlexLogger 2019 R4 In your Channel Specification document, select all configured channels you wish to calibrate. In your Channel Specification document toolbar, click Calibrate channels . Select one of the following calibration options:

### Calibrating Multiple Channels
 Simultaneously

Calibrate more than one channel at the same time.

Introduced in FlexLogger 2019 R4

1. In your Channel Specification document, select all configured
 channels you wish to calibrate.
2. In your Channel Specification document toolbar, click
 Calibrate channels
 [IMAGE alt='image' src='GUID-22C25013-8604-470C-833E-582156DD9C00-a5.png'].
3. Select one of the following calibration options: 
 OptionDescriptionZero
 To get a zero reading, apply an offset to the analog input channels. Zero
 calibration is only available for Linear and Sensitivity scaling types.Null offset
 Perform offset nulling calibration on the strain channels to adjust the output
 of the bridge to 0 V.Shunt calibrate
 Adjust for errors on your bridge circuits caused by resistance of the lead wires
 between the EX pins on the device and the strain gage. For more information, refer to
 *Shunt Calibrating One or More Channels*.

Note

Parent topic:

Configuring I/O Channels

Related tasks:

- Shunt Calibrating One or More Channels

<!--NI_TOPIC bundle=flexlogger path=can-databases.html language=enus -->
## TOPIC 00017: CAN Databases

- bundle_id: `flexlogger`
- source_path: `can-databases.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/can-databases.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Manage your embedded networks using CAN databases. CAN databases provide a consistent set of parameters for all nodes in the network. To have a consistent set of network parameters for all nodes in the network, NI highly recommends using a database. CAN databases allow you to store frames and the si

### CAN Databases

Manage your embedded networks using CAN databases. CAN databases provide a consistent
 set of parameters for all nodes in the network.

To have a consistent set of network parameters for all nodes in the network, NI highly
 recommends using a database.

CAN databases allow you to store frames and the signals running on the network in a database.
 CAN databases allow you to store information about which ECU is transmitting or receiving
 which data. This information is needed for each node in the network.

- Cluster —The basic entity of a
 database. A cluster is the description of a single network (for example, a CAN bus).
- Frame —A single message that is
 exchanged on the cluster.
- Signal —The basic data exchange
 unit on the network. These signals are equivalent to CAN channels.

Parent topic:

Configuring an Automotive Bus

<!--NI_TOPIC bundle=flexlogger path=choose-plug-in.html language=enus -->
## TOPIC 00018: Choosing What Type of Plug-in to Develop for Your Project

- bundle_id: `flexlogger`
- source_path: `choose-plug-in.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/choose-plug-in.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add custom functionality to FlexLogger by developing a plug-in using the FlexLogger Plug-In Development Kit, or by creating a Measurement plug-in. FlexLogger Plug-In Development Kit Plug-insFlexLogger Plug-In Development Kit (PDK) plug-ins extend FlexLogger software to support custom in-line

### Choosing What Type of Plug-in to Develop for
 Your Project

You can add custom functionality to FlexLogger by developing a plug-in using the FlexLogger Plug-In Development Kit, or by creating a Measurement plug-in.

#### FlexLogger Plug-In Development Kit
 Plug-ins

FlexLogger Plug-In Development Kit (PDK) plug-ins extend FlexLogger
 software to support custom in-line calculations and data acquisition from third-party
 hardware devices. FlexLogger Plug-In Development Kit plug-ins make use of a state machine that
 allow you to easily write initialization, measurement, and cleanup code for your
 acquisition. FlexLogger automatically generates the user interface required to configure the
 plug-in measurements or calculations. LabVIEW and the LabVIEW Application Builder Module are
 required to write and compile your plug-ins for use with FlexLogger.

FlexLogger Plug-In Development Kit

- Performing on-the-fly calculations.
- Integrating third-party hardware.
- Adding custom measurement channels.

#### Measurement Plug-ins

Measurement plug-ins are versatile tools that
 allow integration with third-party applications and hardware as well as NI software. You can
 develop Measurement plug-ins using LabVIEW, Python, and multiple other languages.
 Measurement plug-ins serve as a framework for embedding measurement logic and user
 interfaces across multiple applications, including InstrumentStudio and TestStand. They are
 designed to support interactive validation workflows and automated testing, enabling you to
 integrate measurement functionality with minimal coding. Measurement plug-ins utilize
 services such as gRPC for session management and instrument driver interactions. Measurement
 plug-ins are stateless.

#### Key Differences

PDK plug-ins are generally better integrated into the
 FlexLogger environment and offer advanced, specific control capabilities. Measurement
 plug-ins are generally more reusable and allow you to integrate more third-party tools and
 platforms into your project. Keep the following differences in mind when choosing a format
 for your FlexLogger plug-in.

| Criteria | FlexLogger Plug-In Development Kit Plug-Ins | Measurement Plug-Ins |
| --- | --- | --- |
| Flexibility | You must write FlexLogger Plug-In Development Kit plug-ins in LabVIEW. | You can write Measurement plug-ins in LabVIEW, Python, and other languages. |
| Scope | FlexLogger Plug-In Development Kit plug-ins focus on specific capabilities and features within FlexLogger. | Measurement plug-ins are more generic and adaptable. You can use Measurement plug-ins in multiple applications and on multiple platforms. |
| State Machine | FlexLogger Plug-In Development Kit plug-ins feature a state machine that allows you to initialize custom hardware, acquire data in a loop, and release the resources. | Measurement plug-ins are stateless, and do not provide separate initialization and cleanup capabilities. Measurement plug-ins run as a single piece of code in a loop. |
| Learning Curve | Developing FlexLogger Plug-In Development Kit plug-ins is more complex and requires greater knowledge of FlexLogger internal functionality. | Developing Measurement plug-ins is more accessible, as you can develop them in multiple languages and don't need thorough integration with FlexLogger. |

Parent topic:

Adding a Plug-In to Your Project

Related tasks:

- Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project
- Adding a Measurement Plug-In to Your FlexLogger Project

Related information:

- FlexLogger Plug-in Development Kit User Manual
- Measurement Plug-Ins User Manual

<!--NI_TOPIC bundle=flexlogger path=components.html language=enus -->
## TOPIC 00019: Components of a FlexLogger System

- bundle_id: `flexlogger`
- source_path: `components.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/components.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: A FlexLogger system includes FlexLogger, test hardware, drivers, and optional add-ons and extensions. 1 Components of a FlexLogger System Component Type Component Notes Software FlexLogger Install FlexLogger using NI Package Manager. For additional information, refer to Installing, Updating, Repairi

### Components of a FlexLogger System

A FlexLogger system includes FlexLogger, test hardware, drivers, and optional add-ons and
 extensions.

| Component Type | Component | Notes |
| --- | --- | --- |
| Software | FlexLogger | Install FlexLogger using NI Package Manager. For additional information, refer to Installing, Updating, Repairing, and Removing NI Software. |
| Hardware | FlexLogger supports an extensive list of hardware devices. | For additional information, refer to Supported Hardware. |
| Optional Add-on | FlexLogger Plug-In Development Kit | Install the FlexLogger Plug-In Development Kit using NI Package Manager. For additional information, refer to Adding a Plug-In to Your Project. |
| Optional Extension | FlexLogger Step for TestStand | For additional information, refer to Automating FlexLogger Operations Using TestStand. |
| Optional Extension | FlexLogger Python API | For additional information, refer to Automating FlexLogger Tests Using Python. |

Related concepts:

- Automating FlexLogger Tests Using Python

Related tasks:

- Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project
- Automating FlexLogger Operations Using TestStand

Related reference:

- FlexLogger Supported Hardware

Related information:

- Installing, Updating, Repairing, and Removing NI
 Software

<!--NI_TOPIC bundle=flexlogger path=configuring-a-log-file.html language=enus -->
## TOPIC 00020: Configuring a Log File

- bundle_id: `flexlogger`
- source_path: `configuring-a-log-file.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-a-log-file.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Logging Specification document to configure the details of your logged data files such as file name, location, duration, and export options. In the Channel Specification, hover over a channel and click Disable logging to stop logging that channel. Specify the base path for the location where

### Configuring a Log File

Use the Logging Specification document to configure the details of
 your logged data files such as file name, location, duration, and export options.

Channel Specification

Disable logging

[IMAGE alt='image' src='GUID-C90BC748-60E1-411C-B0B4-B7559C23CD7A-a5.png']

1. Specify the base path for the location where your data file will be saved and
 file name. 
 You can use test properties as placeholders in your data log file name and location.
 First, add the test properties to your project. Refer to *Adding Test Properties to a
 Project* and *Using Test Metadata as Placeholders for Log File Names and
 Locations* for more information.
2. Optional: 
 Add a description to your log file.
3. Optional: 
 Specify any additional logging options:
  - Back up your data log files by saving the files to an additional location. To
 enable data log file backup, check Back up file and specify the
 Backup path location. [IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more
 information.
  - Segment your data log files based on file size or time span so the files are more
 manageable. Enable Segment into multiple files and specify how
 the files will be segmented.
  - Reduce the data logging rate to make log files more manageable.
  - Automatically export data log files in CSV format at a specified data
 rate.

Parent topic:

Defining Your Test Configuration

Related tasks:

- Adding Test Properties to a Project
- Using Test Metadata as Placeholders for Log File Names and Locations

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=configuring-ao-in-channel-spec.html language=enus -->
## TOPIC 00021: Configuring Analog Output in Your Channel Specification

- bundle_id: `flexlogger`
- source_path: `configuring-ao-in-channel-spec.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-ao-in-channel-spec.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: You can add your current or voltage output to the project by configuring signals in the Channel Specification. Configure current or voltage generation by enabling the channel and determining the output settings. Select one or more channels you wish to configure. Hover over a channel row and click th

### Configuring Analog Output in Your Channel Specification

You can add your current or voltage output to the project by configuring signals in the
 Channel Specification. Configure current or voltage generation by enabling the channel and
 determining the output settings.

1. Select one or more channels you wish to configure.
2. Hover over a channel row and click the Configure gear
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. 
 The configure gear appears only when selecting multiple channels of the same data type.
 Data types include analog, digital, counter, and calculated. If channels of different
 data types are selected, the configure gear will not appear.
3. Optional: 
 Specify the channel name in the Name field.
4. Select Current or Voltage from
 the Physical Generation drop-down menu. 
 Note Available output options
 vary by device.
5. If applicable, specify an output value for the channel by setting the output
 Value or mapping an input channel Source
 to the output channel. 
 Note FlexLogger does not support waveform
 output. Output signals are software timed and nondeterministic.
6. If applicable, specify the Signal Range minimum and
 maximum.
7. Apply any additional applicable configuration options to the output. Refer to
 *Configuring I/O Channels* for more information on available options. 
 Note FlexLogger does not log output
 channels.

Parent topic:

Configuring I/O Channels

Related concepts:

- Configuring I/O Channels

<!--NI_TOPIC bundle=flexlogger path=configuring-automotive-bus.html language=enus -->
## TOPIC 00022: Configuring an Automotive Bus

- bundle_id: `flexlogger`
- source_path: `configuring-automotive-bus.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-automotive-bus.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure an automotive bus in your test application by selecting the CAN or LIN databases that contain the signal definition and scaling information, and then adding signals from these databases to your project Channel Specification. This feature is available only as part of a complete FlexLogger l

### Configuring an Automotive Bus

Configure an automotive bus in your test application by selecting the CAN or LIN
 databases that contain the signal definition and scaling information, and then adding signals
 from these databases to your project Channel Specification.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. Select one of the following options depending on your automotive network:

- Use CAN databases—Manage and configure CAN
 databases to determine which signals to use in your Channel Specification.
- Use LIN databases—Manage and configure LIN
 databases to determine which signals to use in your Channel Specification.

1. Add signals to the Channel Specification.
2. Specify the Sample Rate for the module. The sample rate
 will be applied to all signals on the associated port.

Parent topic:

Configuring Device Channels

Related concepts:

- CAN Databases
- LIN Databases

Related tasks:

- Adding Signals to Your CAN/LIN Module Channel Specification

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=configuring-boolean-calculated-channels.html language=enus -->
## TOPIC 00023: Configuring Boolean Formula-Based Calculated Channels

- bundle_id: `flexlogger`
- source_path: `configuring-boolean-calculated-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-boolean-calculated-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a calculated Boolean channel to produce a high or low Boolean digital signal based on an analog or digital channel. Introduced in FlexLogger 2019 R4 On the Channel Specification toolbar, select Add channelCalculationBoolean formula. A calculated channel appears in the Channel Specification under

### Configuring Boolean Formula-Based Calculated
 Channels

Add a calculated Boolean channel to produce a high or low Boolean digital signal
 based on an analog or digital channel.

Introduced in FlexLogger 2019 R4

1. On the Channel Specification toolbar, select Add channel»Calculation»Boolean formula. 
 A calculated channel appears in the Channel
 Specification under its host system.
2. Configure the calculated channel. 
 
 After you configure the calculated channel, you can see the live value reflecting
 whether the signal is Low or High. You can use the formula-based calculated
 channel as an input for a trigger event, or like any other channel defined in
 the Channel Specification.
  1. Specify a name and description for the calculated channel. 
 Note For examples of formula syntax
 and a list of supported operators, constants, and functions, refer to
 *Calculation Formula Options*.
  2. Within the formula, enter the name of a hardware channel whose data you want to
 manipulate, ensuring that the channel name is enclosed in single quotes (for example,
 'cDAQ1Mod2/ai0' or
 'cDAQ1Mod2/port0/line1'). Available channel suggestions
 appear when you begin typing (‘).
  3. In Formula, specify a formula to apply to data
 from an existing channel. Suggested formulas appear when you begin
 typing.
  4. Click 
 Done.

Note

Defining Your Test Configuration

Parent topic:

Configuring Calculated Channels

Related tasks:

- Defining Your Test Configuration

Related reference:

- Calculation Formula Options

<!--NI_TOPIC bundle=flexlogger path=configuring-calculated-channels.html language=enus -->
## TOPIC 00024: Configuring Calculated Channels

- bundle_id: `flexlogger`
- source_path: `configuring-calculated-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-calculated-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Add a calculated channel to analyze or scale data from existing hardware channels. A calculated channel produces a new value based on calculations performed on other channels in the system. Calculated channel data is logged with all other channels configured in your Channel Specification. For more i

### Configuring Calculated Channels

Add a calculated channel to analyze or scale data from existing hardware channels.

A calculated channel produces a new value based on calculations performed on other channels in the system.

Note

Defining Your Test Configuration

- [Configuring Arithmetic Formula-Based Calculated Channels](configuring-formula-calculated-channels.html) Add a calculated channel to analyze or scale data from existing hardware channels.
- [Configuring Boolean Formula-Based Calculated Channels](configuring-boolean-calculated-channels.html) Add a calculated Boolean channel to produce a high or low Boolean digital signal based on an analog or digital channel.
- [Configuring Lowpass/Highpass Filter Channels](configuring-filter-channels.html) Add a channel produced by applying either a lowpass or a highpass Butterworth filter to an existing hardware channel.
- [Configuring Integral Channels](configuring-integral-channels.html) Add a channel that calculates the integral of the data in an existing hardware channel.
- [Configuring RMS Channels and Mean Channels](configuring-rms-mean-channels.html) Add a channel that applies RMS averaging or mean averaging to the data in an existing hardware channel.
- [Calculation Formula Options](calculation-formula-options.html) Use standard math operators, functions, and constants to customize hardware channels.
- [Creating Variable Channels](create-variable-channel.html) Create a variable channel you can edit at any time, such as while a test is running.

Parent topic:

Configuring Device Channels

<!--NI_TOPIC bundle=flexlogger path=configuring-counters-in-channel-spec.html language=enus -->
## TOPIC 00025: Configuring Counters in Your Channel Specification

- bundle_id: `flexlogger`
- source_path: `configuring-counters-in-channel-spec.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-counters-in-channel-spec.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add counters to a project by configuring signals in the Channel Specification. Complete the following steps to configure counters for counter modules, such as the NI-9361, and onboard counters. To learn more about onboard counters and how they behave differently from counter modules, refer to Onboar

### Configuring Counters in Your Channel
 Specification

Add counters to a project by configuring signals in the Channel
 Specification.

Complete the following steps to configure counters for counter modules, such as the
 NI-9361, and onboard counters.

Note

Onboard
 Counters

1. Select one or more channels to configure.
2. Hover over a channel row and click Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. 
 The configure gear appears only when selecting multiple channels of the same data type
 (analog, digital, counter, calculated, and so on). If channels of different data types
 are selected, the configure gear will not appear.
3. Optional: 
 Specify the channel name in the Name field.
4. Select the Physical Measurement you want to acquire for
 this channel. 
 Note For information on which physical
 counter measurement types are available for the sensor class you are using, refer to
 *Supported Sensor Class Types*.
5. Select the Sensor Class you want to use to take the
 counter measurement. 
 Additional options appear based on the selected sensor.
6. Optional: 
 Record any sensor information or test procedures in the Sensor
 Properties field. To edit the Sensor
 Properties field, complete the following steps: 
 
 The information populates the Sensor properties field of
 the channel configuration.
  1. Click the Sensor properties edit icon [IMAGE alt='image' src='GUID-128F4C7F-B36E-45D2-8BFB-B820A3BC51A3-a5.png'].
  2. Fill in the information in the Sensor Properties dialog.
7. Optional: 
 Set the configuration options to the desired settings for the corresponding
 counter connected to the channel. You can configure scaling, electrical, alarm,
 advanced, and filtering settings. 
 Note When selecting multiple
 channels, available configuration options may not be available for channels
 with different requirements and specifications. Available channel
 configuration options vary by counter measurement type. 
 After you select a sensor class, Raw value on the live
 graph shows the electrical value the sensor is measuring without scaling. Live
 value shows the sensor value with the scaling configurations applied. Raw
 values help validate the sensor configuration and are not logged to a data file. 
[IMAGE alt='image' src='GUID-F659475B-46EA-4220-A7F4-FF11C63D0BB6-a5.png']
8. Click Done to close the configuration dialog.
9. In the Channel Specification, choose the data rate level from the Data Rate
 Level pull-down selector. Refer to *Configuring Data Rates* for
 more information.

Parent topic:

Configuring I/O Channels

Related concepts:

- Onboard Counters

Related tasks:

- Configuring Data Rates

Related reference:

- Supported Sensor Class Types

<!--NI_TOPIC bundle=flexlogger path=configuring-data-rates.html language=enus -->
## TOPIC 00026: Configuring Data Rates

- bundle_id: `flexlogger`
- source_path: `configuring-data-rates.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-data-rates.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Customize the data ranges and set values for slow, medium, and fast data rates to configure your DAQ device's data acquisition rate. For devices that support downsampling, you can use an anti-aliased filter to downsample at 100 Hz. You can configure any analog input device to use the Slow, Medium, o

### Configuring Data Rates

Customize the data ranges and set values for slow, medium, and fast data rates to
 configure your DAQ device's data acquisition rate.

For devices that support downsampling, you can use an anti-aliased filter to downsample
 at 100 Hz.

You can configure any analog input device to use the Slow,
 Medium, or Fast data rate level.

Configure onboard counters, 62xx/63xx multifunction I/O device counters, and digital modules
 to use these data rate levels. However, you must first configure an analog input
 channel or digital channel in the same chassis to access these data rates.

CompactDAQ counter modules require a data rate resource at the
 Medium data rate level. When adding a CompactDAQ counter
 module, change modules using the Medium data rate to
 Slow or Fast.

Complete the following steps to configure the available data rates for your DAQ
 device:

1. Click Configure Data Rates 
 on the
 toolbar or click Configure from the Data Rate
 Level pull-down selector.
2. Specify each frequency in hertz or seconds (for intervals) for the desired slow, medium,
 fast, counter, or digital rates. Available data rate types vary by device.
3. Click Done to apply the rates.

#### Why is my module not sampling at the
 rate I specified?

- Modules support specific rates. Configure your module to sample at various rates; however,
 hardware limitations may adjust it to the nearest supported rate using
 FlexLogger. Note The
 coerced rate is faster than the rate you specify. For example, if you
 configure 11 Hz for a module that supports 10 Hz and 20 Hz, FlexLogger
 uses 20 Hz.
- Modules sample at the lowest common rate. If you configure multiple modules in the same chassis
 to the same rate and the modules support different data rates, FlexLogger
 sets a common, supported rate. Use a common rate to prevent data loss and
 ensure effective synchronization. For example, if you set the NI-9219 and
 the NI-9236 to Medium (200 Hz), the NI-9236 can't
 sample slow enough to meet the 200 Hz configuration. As a result, both
 modules use the actual rate of ~793 Hz because it's the common rate closest
 to the rate you configured.

Configure modules in the same chassis with different timing rates or place the modules in
 separate chassis to use supported rates.

#### Why does
 my module say the rate is downsampled?

Many modules support downsampling in software to meet a lower data rate than the modules
 support. Downsampling occurs when all the modules set to the same rate support
 downsampling. The available downsampling rate is 100 Hz.

#### Why is my module rate not
 downsampled?

If your module meets the requirements, but isn't downsampling, check the following
 items:

- An existing downsampling preview feature interferes with the default,
 anti-aliased downsampling filter. Navigate to File»Preferences»Preview features and disable the Enable downsampling from a coerced
 hardware sample rate to slower sample rate feature. Note The existing preview feature
 supports arbitrary data rates, but doesn't offer antialiasing.
- C Series Slow Sample Devices don't support downsampling. Refer to C Series Device
 Groupings in the NI-DAQmx User Manual for a list of slow
 sample devices. If you have one slow sample device set to the same rate as
 modules that support downsampling, it prevents downsampling for all the
 modules.

Parent topic:

Configuring I/O Channels

Related information:

- C Series Device Groupings - NI-DAQmx User Manual

<!--NI_TOPIC bundle=flexlogger path=configuring-device-channels.html language=enus -->
## TOPIC 00027: Configuring Device Channels

- bundle_id: `flexlogger`
- source_path: `configuring-device-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-device-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you can start your test and log data, add sensors and signals to your Channel Specification. Learn about the different ways you can configure device channels.

### Configuring Device Channels

Before you can start your test and log data, add sensors and signals to your Channel
 Specification. Learn about the different ways you can configure device channels.

- [Configuring I/O Channels](configuring-io-channels.html) Acquire data or output signals by configuring the individual channels of your DAQ device for the measurement or generation.
- [Configuring an Automotive Bus](configuring-automotive-bus.html) Configure an automotive bus in your test application by selecting the CAN or LIN databases that contain the signal definition and scaling information, and then adding signals from these databases to your project Channel Specification.
- [Configuring Calculated Channels](configuring-calculated-channels.html) Add a calculated channel to analyze or scale data from existing hardware channels.
- [Monitoring Computer Resources](monitoring-computer-resources.html) Add System Resource Monitor channels to track CPU usage, hard drive availability, memory usage, and network activity on your computer.

<!--NI_TOPIC bundle=flexlogger path=configuring-digital-in-channel-spec.html language=enus -->
## TOPIC 00028: Configuring Digital Lines in Your Channel Specification

- bundle_id: `flexlogger`
- source_path: `configuring-digital-in-channel-spec.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-digital-in-channel-spec.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add digital lines to a project by configuring signals in the Channel Specification. Select one or more channels you wish to configure. Hover over a channel row and click Configure . The configure gear appears only when selecting multiple channels of the same data type (analog, digital, counter, calc

### Configuring Digital Lines in Your Channel Specification

Add digital lines to a project by configuring signals in the Channel
 Specification.

1. Select one or more channels you wish to configure.
2. Hover over a channel row and click Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. 
 The configure gear appears only when selecting multiple channels of the same data type
 (analog, digital, counter, calculated, and so on). If channels of different data types
 are selected, the configure gear will not appear.
3. Optional: 
 Specify the channel name in the Name field.
4. Select 
 Digital from the 
 Physical Measurement pull-down selector. 
 Note Available channel configuration options vary for digital input or digital output. For digital input lines, 
 Line will automatically populate the 
 Sensor option. For digital output, you can select the output level.
5. Optional: 
 Open the Digital Settings dialog from the module header drop-down
 menu and specify the digital channels on your device used for digital output. 
 Note You can only set channels on the NI-9401 and NI-9403 to
 all input or all output. Use the Set all lines to input or
 Set all lines to output options in the module header drop-down
 menu to configure line direction for these devices. These options replace the
 Digital Settings dialog.
6. Optional: 
 For digital input, record any sensor information or test procedures in the
 Sensor Properties field. To edit the Sensor
 Properties field, complete the following steps: 
 
 The information populates the Sensor properties field of
 the channel configuration.
  1. Click the Sensor properties edit icon [IMAGE alt='image' src='GUID-128F4C7F-B36E-45D2-8BFB-B820A3BC51A3-a5.png'].
  2. Fill in the information in the Sensor Properties dialog that opens.
7. Optional: 
 For digital output, specify the output Value for the channel or
 map to an input channel Source to use as the channel output, if
 applicable. 
 Note FlexLogger does not support waveform
 output. Output signals are software timed and nondeterministic.
8. Apply any additional applicable configuration options to the line. Refer to
 *Configuring I/O Channels* for more information on available options. 
 For digital input, after the Physical Measurement is
 selected, Live value on the live graph shows the value of the
 signal the line is measuring.
9. Click Done to close the configuration dialog.
10. In the Channel Specification, choose the data rate level from the Data Rate
 Level pull-down selector. Refer to *Configuring Data Rates* for
 more information. 
 Note FlexLogger does not log output
 channels.

Parent topic:

Configuring I/O Channels

Related concepts:

- Configuring I/O Channels

Related tasks:

- Configuring Data Rates

<!--NI_TOPIC bundle=flexlogger path=configuring-ecu-measurements.html language=enus -->
## TOPIC 00029: Configuring ECU Measurements

- bundle_id: `flexlogger`
- source_path: `configuring-ecu-measurements.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-ecu-measurements.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Read and log measurements from your electronic control units (ECUs) alongside any other measurements that FlexLogger supports, such as CAN/LIN and physical or electrical DAQ measurements. Introduced in FlexLogger 2022 Q2 This feature is available only as part of a complete FlexLogger license. Refer

### Configuring ECU Measurements

Read and log measurements from your electronic control units (ECUs) alongside any other
 measurements that FlexLogger supports, such as CAN/LIN and physical or electrical
 DAQ measurements.

Introduced in FlexLogger 2022 Q2

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is
 available only as part of a complete FlexLogger license. Refer to
 *FlexLogger Editions* for more information.

- Install the ECU Measurement and Calibration (ECUMC) Toolkit.
 Note The ECUMC Toolkit enables you to create measurement
 and calibration applications for ECU design and
 validation using functions based on the Universal
 Measurement and Calibration Protocol (XCP) and CAN
 Calibration Protocol (CCP). These protocols enable
 you to read internal ECU variables and
 characteristics defined in your A2L database. Refer
 to the *ECU Measurement and Calibration
 Toolkit* documentation on
 ni.com/docs for more
 information.
- Identify the ASAM MCD 2MC ( .a2l ) database,
 which defines communication properties for your ECU, to add
 to your Channel Specification.

Open your Channel Specification and complete the following steps to
 integrate ECU measurements and calibration into your FlexLogger
 project.

1. Click Add Measurements to open the
 measurement configuration dialog box for the CAN module port
 you want to configure.
2. Under General settings, specify the
 calibration Protocol and Transport
 Layer to use when communicating with the
 target ECU.
3. Using the Database drop-down menu,
 select the A2L database that defines the communication
 properties required to connect with the target ECU.
4. Select the target ECU.
5. Using the Event channel drop-down menu,
 choose the rate at which the ECU sends measurement data to
 FlexLogger.
6. Under Measurements, check the boxes next
 to any measurements you want to add.
7. Click OK. 
 The measurements appear in the Channel Specification
 under the associated port.Note FlexLogger automatically tries to connect to an ECU
 when a measurement is configured. To avoid this,
 check Disable to stop all
 signals and measurements on a port. FlexLogger
 closes all CAN/LIN connections to the port. Closing
 CAN/LIN connections allows other software to use the
 port.
8. Optional: 
 To view the configuration for a measurement, hover over the
 measurement row and click the
 Configure gear ([IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']).

Parent topic:

Configuring an Automotive Bus

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=configuring-filter-channels.html language=enus -->
## TOPIC 00030: Configuring Lowpass/Highpass Filter Channels

- bundle_id: `flexlogger`
- source_path: `configuring-filter-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-filter-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a channel produced by applying either a lowpass or a highpass Butterworth filter to an existing hardware channel. The lowpass or highpass filter channel displays filtered data that excludes any noise in the signal outside of the selected range.Introduced in FlexLogger 2019 R2 On the Channel Spec

### Configuring Lowpass/Highpass Filter Channels

Add a channel produced by applying either a lowpass or a highpass Butterworth filter
 to an existing hardware channel. The lowpass or highpass filter channel displays
 filtered data that excludes any noise in the signal outside of the selected range.

Introduced in FlexLogger 2019 R2

1. On the Channel Specification toolbar, select Add channel»Calculation»Filter. 
 A configuration dialog opens.
2. Click Data source. Select the channel to which you want to apply
 the filter. 
 If no channels appear in the selector, ensure that you have configured channels in your
 Channel Specification.
3. Specify a 
 Name and 
 Description for the calculated channel, if necessary. 
 After you configure the calculated channel, you can see the live value reflecting the filter you applied to your data. You can use the filter calculated channel like any other channel defined in the 
 Channel Specification.
4. Select the 
 Filter type you want to apply, and specify the 
 Cutoff frequency for the filter.
5. Click 
 Done. 
 A calculated channel appears at the top of the 
 Channel Specification.

Note

Defining Your Test Configuration

Parent topic:

Configuring Calculated Channels

Related tasks:

- Defining Your Test Configuration

<!--NI_TOPIC bundle=flexlogger path=configuring-formula-calculated-channels.html language=enus -->
## TOPIC 00031: Configuring Arithmetic Formula-Based Calculated Channels

- bundle_id: `flexlogger`
- source_path: `configuring-formula-calculated-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-formula-calculated-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a calculated channel to analyze or scale data from existing hardware channels. A calculated channel produces a new value based on calculations performed on other channels in the system. On the Channel Specification toolbar, select Add channelCalculationArithmetic formula. A calculated channel ap

### Configuring Arithmetic Formula-Based
 Calculated Channels

Add a calculated channel to analyze or scale data from existing hardware channels. 
 A calculated channel produces a new value based on calculations performed on other channels in the system.

1. On the Channel Specification toolbar, select Add channel»Calculation»Arithmetic formula. 
 A calculated channel appears in the Channel
 Specification under its host system.
2. Configure the calculated channel. 
 
 After you configure the calculated channel, you can see the live value reflecting the formula you applied to your data. You can use the formula-based calculated channel like any other channel defined in the 
 Channel Specification.
  1. Specify a name, unit of measure, and description for the calculated channel. 
 Note For examples of formula syntax
 and a list of supported functions, operators, and constants, refer to
 *Calculation Formula Options*.
  2. In 
 Formula, specify a formula to apply to data from an existing channel. Suggested formulas appear when you begin typing.
  3. Within the formula, enter the name of a hardware channel whose data you want to
 manipulate. Ensure that the channel name is enclosed in single quotes. For example,
 'ai 0'. You can also input constants, such as
 pi.
  4. Click 
 Done.

Note

Defining Your Test Configuration

Notice

- all source channels are from modules in the same chassis
- all source channels are using the same data rate level ( Slow ,
 Medium , Fast )

Parent topic:

Configuring Calculated Channels

Related tasks:

- Defining Your Test Configuration

Related reference:

- Calculation Formula Options

<!--NI_TOPIC bundle=flexlogger path=configuring-integral-channels.html language=enus -->
## TOPIC 00032: Configuring Integral Channels

- bundle_id: `flexlogger`
- source_path: `configuring-integral-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-integral-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a channel that calculates the integral of the data in an existing hardware channel. The Integral channel produces a new value based on integrating the data in a channel in the system. On the Channel Specification toolbar, select Add channel Calculation Integral . FlexLogger opens a configuration

### Configuring Integral Channels

Add a channel that calculates the integral of the data in an existing hardware
 channel.

The Integral channel produces a new value based on integrating the data in a channel in the
 system.

1. On the Channel Specification toolbar, select Add channel»Calculation»Integral. 
 FlexLogger opens a configuration dialog.
2. Click Data source. Select the channel that generates the data
 you want to integrate. 
 If no channels appear in the selector, ensure that you have configured channels in your
 Channel Specification. 
 After you configure the data source, you can see the live value reflecting the
 integrated data. You can use the Integral channel like any other channel defined in the
 Channel Specification.
3. Optional: 
 Update the Name and specify a Description
 for the calculated channel.
4. Optional: 
 Specify the Unit that results from integrating the data.
5. Optional: 
 Check Reset when test starts to perform the calculation using
 all the data you collected for the channel since starting the test. Uncheck
 Reset when test starts to use all the data you collected for the
 channel since opening the project.
6. Click 
 Done. 
 FlexLogger adds the calculated channel at the top of the Channel
 Specification.

Note

Channel Specification

Defining Your Test Configuration

Parent topic:

Configuring Calculated Channels

Related tasks:

- Defining Your Test Configuration

<!--NI_TOPIC bundle=flexlogger path=configuring-io-channels.html language=enus -->
## TOPIC 00033: Configuring I/O Channels

- bundle_id: `flexlogger`
- source_path: `configuring-io-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-io-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Acquire data or output signals by configuring the individual channels of your DAQ device for the measurement or generation. Add and configure signals to use in your Channel specification.

### Configuring I/O Channels

Acquire data or output signals by configuring the individual channels of your DAQ
 device for the measurement or generation.

Channel
 specification

- [Configuring Sensors in Your Channel Specification](configuring-sensors-in-channel-spec.html) Add sensors to your project by configuring sensor settings and scaling options for the corresponding channels in the Channel Specification.
- [Configuring Digital Lines in Your Channel Specification](configuring-digital-in-channel-spec.html) Add digital lines to a project by configuring signals in the Channel Specification.
- [Configuring Analog Output in Your Channel Specification](configuring-ao-in-channel-spec.html) You can add your current or voltage output to the project by configuring signals in the Channel Specification. Configure current or voltage generation by enabling the channel and determining the output settings.
- [Configuring Counters in Your Channel Specification](configuring-counters-in-channel-spec.html) Add counters to a project by configuring signals in the Channel Specification.
- [Configuring Data Rates](configuring-data-rates.html) Customize the data ranges and set values for slow, medium, and fast data rates to configure your DAQ device's data acquisition rate.
- [Synchronization](synchronization.html) Synchronize your system to coordinate inputs within a module or device, between modules in a single chassis, or between multiple devices or chassis.
- [Scaling Electrical Values to Physical Values](scaling-electrical-values.html) Scale the electrical values of a device to the physical units of a sensor.
- [Calibrating Multiple Channels Simultaneously](calibrating-multiple-channels.html) Calibrate more than one channel at the same time.
- [Reducing Signal Noise](reducing-signal-noise.html) Configure hardware filters and software filters in FlexLogger to reduce noise in your signals.
- [Adding an Alarm](adding-alarms.html) Use the Channel Configuration to monitor your signals and trigger an alarm when the selected value conditions are met.
- [Selecting a Strain Gage](selecting-strain-gage.html) Select a strain gage that meets the needs of your system and application.

Parent topic:

Configuring Device Channels

<!--NI_TOPIC bundle=flexlogger path=configuring-rms-mean-channels.html language=enus -->
## TOPIC 00034: Configuring RMS Channels and Mean Channels

- bundle_id: `flexlogger`
- source_path: `configuring-rms-mean-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-rms-mean-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a channel that applies RMS averaging or mean averaging to the data in an existing hardware channel. The RMS or Mean channel produces a new value based on averaging performed on the data in a channel in the system. On the Channel Specification toolbar, select Add channelCalculationRMS or Mean, de

### Configuring RMS Channels and Mean
 Channels

Add a channel that applies RMS averaging or mean averaging to the data in an existing
 hardware channel. The RMS or Mean channel produces a new value based on averaging
 performed on the data in a channel in the system.

1. On the Channel Specification toolbar, select Add channel»Calculation»RMS or Mean, depending on the type of
 averaging you wish to perform. 
 FlexLogger opens a configuration dialog.
2. Click Data source. Select the channel from which you want the
 RMS calculation or mean calculation performed. 
 If no channels appear in the selector, ensure that you have configured channels in your
 Channel Specification.
3. Optional: 
 Update the Name and specify a Description
 for the calculated channel.
4. Select from the following Scope of calculation options. 
 OptionDescriptionFixed size blocks
 Perform the calculation for a subset of channel data based on an interval of
 time in seconds. Specify the interval of time in Requested block
 size.All channel data
 Perform the calculation using all the data you collected for the channel since
 starting the test. To use all the data you collected for the channel since opening the
 project, uncheck Reset when test starts. 
 After you configure the calculated channel, you can see the live value
 reflecting the averaging you applied to your data. You can use the RMS calculated channel
 or mean calculated channel like any other channel defined in the Channel
 Specification.
5. Click 
 Done. 
 FlexLogger adds the calculated channel at the top of the Channel
 Specification.

Note

Channel
 Specification

Defining
 Your Test Configuration

Parent topic:

Configuring Calculated Channels

Related tasks:

- Defining Your Test Configuration

<!--NI_TOPIC bundle=flexlogger path=configuring-sensors-in-channel-spec.html language=enus -->
## TOPIC 00035: Configuring Sensors in Your Channel Specification

- bundle_id: `flexlogger`
- source_path: `configuring-sensors-in-channel-spec.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/configuring-sensors-in-channel-spec.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add sensors to your project by configuring sensor settings and scaling options for the corresponding channels in the Channel Specification. Select one or more channels you wish to configure. Hover over a channel row to see the Configure gear . Click Configure for the channel or channels you wish to

### Configuring Sensors in Your Channel Specification

Add sensors to your project by configuring sensor settings and scaling options for the
 corresponding channels in the Channel Specification.

1. Select one or more channels you wish to configure.
2. Hover over a channel row to see the Configure gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. Click
 Configure for the channel or channels you wish to configure. 
 The configure gear appears when selecting multiple channels of the same data type
 (analog, digital, counter, calculated, and so on). If channels of different data types
 are selected, the configure gear will not be available.
3. Set channel configuration options as needed.
  1. Specify the channel name in the Name field, if
 necessary.
  2. Select the Physical Measurement you wish to
 acquire for this channel. 
 Note For information on which physical
 measurement types are available for the sensor class you are using, refer to
 *Supported Sensor Class Types*.
  3. Select the Sensor Class that will be used to
 take the physical measurement. 
 The applicable Physical,
 Electrical, and Scaling options that
 appear are specific to the selected sensor. Note When selecting multiple channels,
 available configuration options may not be available for channels with different
 requirements and specifications. Available channel configuration options vary by
 device measurement type.
  4. If applicable, set the configuration options to the desired settings
 for the corresponding sensor connected to the channel.
4. If applicable, record any sensor information or test procedures in the 
 Sensor Properties field. To edit the 
 Sensor Properties field, complete the following steps: 
 
 The information will populate the 
 Sensor Properties field of the channel configuration.
  1. Click the 
 Sensor Properties edit icon at the top right of the box.
  2. Fill in the information in the 
 Sensor Properties dialog that opens.
5. If necessary, apply any additional applicable configuration options to the sensor.
 Refer to *Configuring I/O Channels* for more information on available options.

After a Sensor Class is selected, Raw value shows the raw electrical
 value being measured from your sensor without any scaling applied to it.
 Live value shows the sensor value with any scaling
 configurations applied. Raw values are meant for validation of the sensor
 configuration and are not logged to a data file.

[IMAGE alt='image' src='GUID-E3CD2D2E-9347-4B13-AB48-5D097C5CBA1F-a5.png']

Parent topic:

Configuring I/O Channels

Related concepts:

- Configuring I/O Channels

Related reference:

- Supported Sensor Class Types

<!--NI_TOPIC bundle=flexlogger path=connecting-flexlogger-to-systemlink-server.html language=enus -->
## TOPIC 00036: Connecting FlexLogger to a Remote SystemLink Server

- bundle_id: `flexlogger`
- source_path: `connecting-flexlogger-to-systemlink-server.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/connecting-flexlogger-to-systemlink-server.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: SystemLink and SystemLink Client enable you to publish channel data and the backup files from your FlexLogger projects to a remote server. Introduced in FlexLogger 2020 R3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. To i

### Connecting FlexLogger to a Remote SystemLink
 Server

SystemLink and SystemLink Client enable you to publish channel data and the
 backup files from your FlexLogger projects to a remote server.

Introduced in FlexLogger 2020 R3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more information.

To install and to configure SystemLink and SystemLink
 Client, complete the following steps.

1. Using NI Package Manager, download and install SystemLink on the host computer.
 For detailed instructions, refer to *Setting Up a SystemLink
 Server*.
2. Using NI Package Manager, download and install SystemLink Client on the
 computer where you run FlexLogger. For detailed instructions, refer to
 *Setting Up a SystemLink Client for Windows Targets*. 
 Note To launch the NI SystemLink
 web application, open NI Web Server Configuration on the host computer and
 click the link in the Summary tab. 
 After successfully connecting to the host, your client computer appears
 in the list under Systems in the NI SystemLink web
 application. To view tags, files, and other information, click the client name.

Project

»

Settings

Parent topic:

Publishing Data and Backup Files to a Remote SystemLink Server

Related information:

- Setting Up a SystemLink Server
- Setting Up a SystemLink Client for Windows Targets
- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=create-project-spreadsheet.html language=enus -->
## TOPIC 00037: Creating a Project Using the Spreadsheet Importer

- bundle_id: `flexlogger`
- source_path: `create-project-spreadsheet.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/create-project-spreadsheet.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Spreadsheet Importer to quickly create a FlexLogger project populated with hardware, channels, and configured settings based on an Excel spreadsheet. Introduced in FlexLogger 2026 Q2 The Spreadsheet Importer supports configuring the following elements in a FlexLogger project: DAQ and PXI har

### Creating a Project Using the Spreadsheet
 Importer

Use the Spreadsheet Importer to quickly create a FlexLogger project
 populated with hardware, channels, and configured settings based on an Excel
 spreadsheet.

Introduced in FlexLogger 2026 Q2

- DAQ and PXI hardware
- Inputs and outputs
- Counters
- Calculated channels
- Variables
- Most channel configuration options in the Channel Specification document

Note

FlexLogger

Note

.xlsx

- [Creating Your Project Spreadsheet](creating-project-spreadsheet.html#GUID-F8923F8A-ED71-4239-AC60-0107B414CB04) You must construct source Excel spreadsheets for FlexLogger projects in a specific way to use them with the Spreadsheet Importer.
- [Using the Spreadsheet Importer Through FlexLogger](spreadsheet-importer-flexlogger.html) Use the Spreadsheet Importer UI in FlexLogger to easily create a FlexLogger project based on a source Excel spreadsheet.
- [Using the Spreadsheet Importer Through the Command Line](spreadsheet-importer-cmd.html) Use the command line to create a FlexLogger project using the Spreadsheet Importer without needing to launch FlexLogger.

Parent topic:

Creating a Project

<!--NI_TOPIC bundle=flexlogger path=create-project.html language=enus -->
## TOPIC 00038: Creating a Project

- bundle_id: `flexlogger`
- source_path: `create-project.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/create-project.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consult the following topics to create a new project in FlexLogger or use the Spreadsheet Importer to create a project based on an Excel spreadsheet.

### Creating a Project

Consult the following topics to create a new project in FlexLogger or use the Spreadsheet
 Importer to create a project based on an Excel spreadsheet.

- [Creating a New Project](creating-new-project.html) Create a new project in FlexLogger to configure hardware, specify logging properties, and run your test.
- [Creating a Project Using the Spreadsheet Importer](create-project-spreadsheet.html) Use the Spreadsheet Importer to quickly create a FlexLogger project populated with hardware, channels, and configured settings based on an Excel spreadsheet.

<!--NI_TOPIC bundle=flexlogger path=create-variable-channel.html language=enus -->
## TOPIC 00039: Creating Variable Channels

- bundle_id: `flexlogger`
- source_path: `create-variable-channel.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/create-variable-channel.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a variable channel you can edit at any time, such as while a test is running. Variable channels act as static integer value channels you can use to make changes to formulas during a test, such as changing a multiplier to zero to turn a signal off.Introduced in FlexLogger 2020 R4 This feature

### Creating Variable Channels

Create a variable channel you can edit at any time, such as while a test is
 running. Variable channels act as static integer value channels you can use to
 make changes to formulas during a test, such as changing a multiplier to zero to turn a signal
 off.

Introduced in FlexLogger 2020 R4

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png']
 This feature is available only as part of a complete FlexLogger license. Refer to
 *FlexLogger Editions* for more information.

1. In the Channel Specification, select Add channels»Variable in the toolbar. 
 A variable channel appears in the Channel Specification
 under its host system.
2. Configure the variable channel. 
 
 After you configure your variable, add it to new and existing
 formulas.
  1. Specify a name and description for the variable.
  2. Add an integer as the variable value.
  3. Optional: 
 Add a unit of measurement.

Calculation Formula Options

Parent topic:

Configuring Calculated Channels

Related reference:

- Calculation Formula Options

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=creating-new-project.html language=enus -->
## TOPIC 00040: Creating a New Project

- bundle_id: `flexlogger`
- source_path: `creating-new-project.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/creating-new-project.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a new project in FlexLogger to configure hardware, specify logging properties, and run your test. Launch FlexLogger. Select File New Project . To save the project, select FileSave All. Specify the project name and file location. Click Save. You can use only one FlexLogger project at a time. A

### Creating a New Project

Create a new project in FlexLogger to configure hardware, specify logging properties,
 and run your test.

1. Launch FlexLogger.
2. Select File»New»Project.
3. To save the project, select File»Save All.
4. Specify the project name and file location.
5. Click Save. 
 Note You can use only one FlexLogger
 project at a time.

After you create a new project, use FlexLogger to discover
 your hardware or simulate a USB DAQ device.

Parent topic:

Creating a Project

Related concepts:

- How FlexLogger Connects to Your Hardware

<!--NI_TOPIC bundle=flexlogger path=creating-project-spreadsheet.html language=enus -->
## TOPIC 00041: Creating Your Project Spreadsheet

- bundle_id: `flexlogger`
- source_path: `creating-project-spreadsheet.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/creating-project-spreadsheet.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: You must construct source Excel spreadsheets for FlexLogger projects in a specific way to use them with the Spreadsheet Importer. FlexLogger expects project source spreadsheets to store data in specific sheet and column names. You can create a source spreadsheet using FlexLogger or the command line

### Creating Your Project Spreadsheet

You must construct source Excel spreadsheets for FlexLogger projects in a specific way
 to use them with the Spreadsheet Importer.

Note

Parent topic:

Creating a Project Using the Spreadsheet Importer

#### Creating a Template Spreadsheet Using
 FlexLogger

You can create a template project spreadsheet from within FlexLogger.

1. Navigate to File»Copy empty spreadsheet template.
2. Specify the file path where you want to save the template spreadsheet.

Related tasks:

- Using the Spreadsheet Importer Through FlexLogger

#### Creating a Template Spreadsheet Using the
 Command Line

You can create a FlexLogger project spreadsheet without opening FlexLogger by using the
 command line.

1. Open a command prompt, terminal, or PowerShell window.
2. Enter cd "C:\Program Files\National Instruments\FlexLogger\"
 to navigate to your FlexLogger installation location.
3. Run ./flexloggercli.exe createtemplate with the following
 arguments to create your spreadsheet. 
 Table 18.Spreadsheet Template
 Creation Command Line OptionsArgument
 Description-f
 Specifies the file path you want to save the spreadsheet
 to.
 -n
 Specifies the spreadsheet name.
 -o
 Optional argument that overwrites any existing
 spreadsheets with the same name at your specified
 path.

```text
./flexloggercli.exe createtemplate -f "C:\Users\nitest\Documents\FlexLogger\ImporterProjects" -n "MyTemplate" -o
```

The
 Spreadsheet Importer creates a spreadsheet named
 MyTemplate.xlsx at
 C:\Users\nitest\Documents\FlexLogger\ImporterProjects\MyTemplate.xlsx.

Related tasks:

- Using the Spreadsheet Importer Through the Command Line

#### Populating Your Spreadsheet with Data

Once you have created your template spreadsheet, you can populate it with the hardware
 and channel information relevant to your project.

##### Specifying Hardware in Your
 Spreadsheet

| Column Name | Definition |
| --- | --- |
| Channel Name | User-defined channel name. |
| Chassis Model | Type of chassis, such as "NI PXIe-1083" or "NI cDAQ-9189". |
| Chassis Name | Name of the chassis defined in NI MAX or Hardware Configuration Utility. |
| Chassis Serial Number | (Optional) Chassis serial number. |
| Module Slot Number | The chassis slot containing the module. For FieldDAQ devices, this value is the bank number the channel is on. |
| Module Model | Type of module, such as "NI PXI-6289" or "NI 9205 (DSUB)". |
| Module Name | Name of the module defined in NI MAX or Hardware Configuration Utility. |
| Physical Channel | Name of the channel, such as "AI0" or "port0/line2". |

The following table contains examples of valid definitions for
 hardware channels. You only need to define the populated properties for each channel
 type to define hardware using that method.

| Channel Type | Channel Name | Chassis Model | Chassis Name | Module Slot Number | Module Model | Module Name | Physical Channel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chassis-defined channel | Channel1 | NI PXIe-1083 | MyPXIChassis | 2 | NI PXI-6289 | — | port1/line2 |
| Module-defined channel | Channel2 | — | — | — | NI 9219 | MyModule | AI3 |
| Onboard cDAQ chassis counter | Channel3 | NI cDAQ-9189 | MyDAQChassis | — | — | — | CTR0 |
| FieldDAQ channel | Channel4 | — | — | 1 | NI FD-11614 | MyFieldDAQ | AI0 |

##### Determining Valid Values

- Certain columns only accept values from a set list. These columns show the
 values they can accept when you try to populate them. For example, the
 Coupling column only accepts AC or
 DC as valid values.
- Certain columns must contain a numerical value.
- The following columns require specific value formatting:
  - You must format values in the Data Rate column as Level
 (Hertz Value) . For example, you can define your
 channel data rate as Medium (100) or
 Slow (5) .
  - You must format values in the Signal Range and Hardware Range
 columns as either Automatic or
 Manual (Min; Max) . For example, you can
 define a signal range as Manual (-10;
 10) .
  - You must format values in the Critical Range and Warning Range
 columns as (min; max) . For example, you can
 define a critical range as (-20; 20) .

Note

'channelName'

''channelName' < 10

If you enter an
 invalid value in a column, the Spreadsheet Importer output includes an error or
 warning which describes how to fix the invalid configuration.

##### Example
 Spreadsheets

C:\Program Files\National Instruments\FlexLogger\Examples\Spreadsheet
 Importer

| Example Name | Description |
| --- | --- |
| ChannelConfigurationReference.xlsx | This example contains at least one configured channel for each measurement type, which demonstrates valid values and how to fill out your source spreadsheet. |
| SimpleExample.xlsx | This spreadsheet contains 12 configured channels, and demonstrates what your source spreadsheet could look like. Some sheets and columns are not used in this example, so they have been deleted. |

<!--NI_TOPIC bundle=flexlogger path=defining-test-configuration.html language=enus -->
## TOPIC 00042: Defining Your Test Configuration

- bundle_id: `flexlogger`
- source_path: `defining-test-configuration.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/defining-test-configuration.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Set the conditions and logging behavior of your project. Before you define your test configuration options, create a FlexLogger project and configure your hardware. After defining your test configuration options, run your test.

### Defining Your Test Configuration

Set the conditions and logging behavior of your project.

Before you define your test configuration
 options, create a FlexLogger project and configure your hardware.

After defining your test configuration options, run your
 test.

1. Configuring a Log File Use the Logging Specification document to configure the details of your logged data files such as file name, location, duration, and export options.
2. Adding an Event Use the Test Specification to create an event trigger to generate a response from your system.
3. Initiating an Action with a Button Generate a response from your system with the click of a button.
4. Locking a Configured Project You can lock a configured project to prevent unwanted changes.

<!--NI_TOPIC bundle=flexlogger path=definition.html language=enus -->
## TOPIC 00043: FlexLogger Overview

- bundle_id: `flexlogger`
- source_path: `definition.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/definition.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexLogger is software for test engineers and technicians who need to acquire, visualize, and log mixed measurement data from electromechanical systems. Use FlexLogger to configure your hardware quickly and start logging data without programming. FlexLogger Key Features FlexLogger has the following

### FlexLogger
 Overview

FlexLogger is software for test engineers and
 technicians who need to acquire, visualize, and log mixed measurement data from
 electromechanical systems. Use FlexLogger to configure your
 hardware quickly and start logging data without programming.

#### FlexLogger Key
 Features

FlexLogger has the following features and the following
 capabilities.

- Automatic hardware discovery
- Sensor-specific configuration
- Intuitive user interface
- Measurement synchronization
- Live data visualization
- Custom test and data logging configuration
- Data review and export

<!--NI_TOPIC bundle=flexlogger path=determining-termination-resistance.html language=enus -->
## TOPIC 00044: Determining the Necessary Termination Resistance for Your Low-Speed CAN Device

- bundle_id: `flexlogger`
- source_path: `determining-termination-resistance.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/determining-termination-resistance.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Determine the correct termination resistor values for the Low-Speed CAN transceiver. Low-Speed CAN requires termination at the Low-Speed CAN transceiver instead of on the cable. The termination requires two resistors: RTH for CAN_H and RTL for CAN_L. This configuration allows the NXP fault-tolerant

### Determining the Necessary Termination Resistance for Your Low-Speed CAN Device

Determine the correct termination resistor values for the Low-Speed CAN transceiver.

Low-Speed CAN requires termination at the Low-Speed CAN transceiver instead of on the cable. The termination requires two resistors: RTH for CAN_H and RTL for CAN_L. This configuration allows the NXP fault-tolerant CAN transceiver to detect and recover from bus faults. You can use the CAN hardware to connect to a Low-Speed CAN network having from two to 32 nodes as specified by NXP (including the port on the CAN Low-Speed/Fault-Tolerant interface). You also can use the Low-Speed/Fault-Tolerant interface to communicate with individual Low-Speed CAN devices. It is important to determine the overall termination of the existing network, or the individual device termination, before connecting it to a Low-Speed/Fault-Tolerant port.

1. NXP recommends an overall RTH and RTL termination of 100-500 Ω (each) for a properly terminated low-speed network. Determine the overall network termination as follows: 
 1
 R
 RTH
 ⁢
 
 overall
 ⁢
 
 =
 
 1
 R
 RTH
 ⁢
 
 node 1
 ⁢
 ⁢
 ⁢
 +
 
 1
 R
 RTH
 ⁢
 
 node 2
 ⁢
 ⁢
 ⁢
 +
 
 1
 R
 RTH
 ⁢
 
 node 3
 ⁢
 ⁢
 ⁢
 +
 
 1
 R
 RTH
 ⁢
 
 node n
 ⁢
 ⁢
2. NXP also recommends an individual device RTH and RTL termination of 500 Ω-16 KΩ. After determining the existing network or device termination, use the following formula to indicate which nearest value the termination property needs to be set to produce the proper overall RTH and RTL termination of 100-500 Ω upon connection of the card: 
 R
 RTH
 ⁢
 overall
 ⁢
 =
 
 1
 (
 1
 R
 RTH of low-speed CAN interface
 ⁢
 +
 
 1
 R
 RTH of existing network or device
 ⁢
 )where R<sub>RTH</sub> overall should be 100-500 Ω.

125 Ω

5 KΩ

125 Ω

1 KΩ

Parent topic:

Low-Speed CAN Cable Termination

<!--NI_TOPIC bundle=flexlogger path=doc-reference-for-flexlogger-editions.html language=enus -->
## TOPIC 00045: Documentation Reference for FlexLogger Editions

- bundle_id: `flexlogger`
- source_path: `doc-reference-for-flexlogger-editions.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/doc-reference-for-flexlogger-editions.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn which parts of the documentation apply to FlexLogger and FlexLogger Lite. 13 Documentation for Configuring Device Channels Topic Title FlexLogger Lite FlexLogger Configuring Sensors in Your Channel Specification yes yes Configuring Digital Lines in Your Channel Specification yes yes Configurin

### Documentation Reference for FlexLogger
 Editions

Learn which parts of the documentation apply to FlexLogger and FlexLogger
 Lite.

| Topic Title | FlexLogger Lite | FlexLogger |
| --- | --- | --- |
| Configuring Sensors in Your Channel Specification | yes | yes |
| Configuring Digital Lines in Your Channel Specification | yes | yes |
| Configuring Analog Output in Your Channel Specification | yes | yes |
| Configuring Counters in Your Channel Specification | yes | yes |
| Configuring Data Rates | yes | yes |
| Setting Output Reset Values | yes | yes |
| Calibrating Multiple Channels Simultaneously | yes | yes |
| Reducing Signal Noise | yes | yes |
| Scaling Electrical Values to Physical Values | yes | yes |
| Selecting a Strain Gage | yes | yes |
| Configuring Arithmetic Formula-Based Calculated Channels | yes | yes |
| Configuring Boolean Formula-Based Calculated Channels | yes | yes |
| Configuring Lowpass/Highpass Filter Channels | yes | yes |
| Configuring Integral Channels | yes | yes |
| Configuring RMS and Mean Channels | yes | yes |
| Using TEDS Sensors in Your Channel Specification | no | yes |
| Using Network Synchronization in Your Project | no | yes |
| Using PXIe Synchronization in Your Project | no | yes |
| Adding an Alarm | no | yes |
| Configuring an Automotive Bus | no | yes |
| Adjusting Port/Interface Settings (CAN) | no | yes |
| Adjusting Port/Interface Settings (LIN) | no | yes |
| Adding Signals to Your CAN/LIN Module Channel Specification | no | yes |
| Configuring ECU Measurements | no | yes |
| Managing CAN/LIN Databases | no | yes |
| Creating Variable Channels | no | yes |
| Monitoring Computer Resources | no | yes |

| Topic Title | FlexLogger Lite | FlexLogger |
| --- | --- | --- |
| Configuring a Log File | yes1 | yes |
| Adding Test Properties to a Project | yes | yes |
| Enabling and Configuring Triggers for Data Logging | no | yes |
| Adding an Event | no | yes |
| Initiating an Action with a Button | no | yes |
| Locking a Configured Project | no | yes |

Note

1

FlexLogger Editions

| Topic Title | FlexLogger Lite | FlexLogger |
| --- | --- | --- |
| Running a Test | yes | yes |
| Adding User Notes to a Log File During a Running Test | no | yes |

| Topic Title | FlexLogger Lite | FlexLogger |
| --- | --- | --- |
| Visualizing Live Data with Indicators and Graphs | yes2 | yes |
| Viewing and Analyzing Logged Data with DIAdem | yes | yes |
| Viewing Logged Data in Excel | yes | yes |
| Manually Exporting Data Files to CSV File Format | yes | yes |
| Automatically Exporting Data Files to CSV File Format | yes | yes |

Note

2

FlexLogger Editions

| Feature | FlexLogger Lite | FlexLogger |
| --- | --- | --- |
| Adding a Plug-in to Your Project | no | yes |
| Using SystemLink to Share Data and Back Up Files | no | yes |
| Publish Data and Backup Files to a Remote SystemLink Server | no | yes |
| Connecting FlexLogger to a Remote SystemLink Server | no | yes |
| Publish Data to LabVIEW | no | yes |
| Automating FlexLogger Tests Using Python | no | yes |

Parent topic:

Accessing the Documentation

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=enabling-and-configuring-triggers-for-data-logging.html language=enus -->
## TOPIC 00046: Enabling and Configuring Triggers for Data Logging

- bundle_id: `flexlogger`
- source_path: `enabling-and-configuring-triggers-for-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/enabling-and-configuring-triggers-for-data-logging.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a trigger and configure the start and the stop conditions for logging data during a test. This feature is only available as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Add and configure data logging triggers in the Logging trigger section of your Log

### Enabling and Configuring Triggers for Data
 Logging

Add a trigger and configure the start and the stop conditions for logging data during
 a test.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is only available as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Logging trigger

Logging
 Specification

Logging Specification

Triggers

[IMAGE alt='image' src='GUID-5426AE8D-5175-4BDC-B225-8948BC939A23-a5.png']

1. Select from the following Start conditions. 
 OptionDescriptionTest start
 Manually begin logging by clicking RUN.Channel value change
 Begin logging when the value of the channel meets the specified Value
 change condition. When you select this condition, FlexLogger enables the
 logging trigger on the toolbar. To start logging before the channel meets the value
 change conditions, specify the Leading time to include.Note You cannot log data before the test
 starts.Absolute time
 Begin logging at a designated date and time. When you select this condition,
 FlexLogger enables the logging trigger on the toolbar.Note If the time is in the
 past, logging begins immediately when the test starts.
2. Select from the following Stop conditions. 
 OptionDescriptionTest stop
 Manually stop logging by clicking STOP.Channel value change
 Stop logging when the value of the channel meets the specified Value
 change condition. When you select this condition, FlexLogger enables the
 logging trigger on the toolbar.To log data each time the channel meets the trigger
 conditions, check Enable re-triggering.To keep logging
 after the channel meets the value change conditions, specify the Trailing
 time to include.Note When you pause a test, FlexLogger
 ignores the trigger condition. Data logging stops when the test
 stops.Test time elapsed
 Stop logging after a designated duration of time has elapsed. When you select
 this condition, FlexLogger enables the logging trigger on the toolbar.Note When you
 pause a test, FlexLogger pauses the duration timer.
3. Select the logging behavior you want while the trigger conditions are not met. 
 OptionDescriptionDo not log data
 FlexLogger does not log data.Log data at
 FlexLogger logs data at the rate you specify until the start condition is met.
 Then, FlexLogger logs at the channel rate until the stop condition is met. 
 FlexLogger summarizes the trigger conditions in the Logging
 summary. To revert to the default configuration, click Reset
 logging trigger.

| Logging rate | Scenario |
| --- | --- |
| Channel rate | The trigger conditions are met. |
| Logging rate you specify in When trigger conditions are not met | The trigger conditions are not met. |

RUN

Parent topic:

Configuring a Log File

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=exchange-data-with-labview.html language=enus -->
## TOPIC 00047: Exchanging Data with LabVIEW (Legacy)

- bundle_id: `flexlogger`
- source_path: `exchange-data-with-labview.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/exchange-data-with-labview.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use SystemLink tags to exchange data between FlexLogger and LabVIEW. Install LabVIEW 2017 or later (64-bit recommended). Install NI SystemLink Tag Support for LabVIEW. Open NI Package Manager and click Installed. Locate FlexLogger and click the Install or remove related packages gear. Select NI Syst

### Exchanging Data with LabVIEW
 (Legacy)

Use SystemLink tags to exchange data between FlexLogger and LabVIEW.

1. Install LabVIEW 2017 or later (64-bit recommended).
2. Install NI SystemLink Tag Support for LabVIEW.
  1. Open NI Package Manager and click Installed.
  2. Locate FlexLogger and click the Install or remove related
 packages gear.
  3. Select NI SystemLink Tag Support for LabVIEW
 <*version*> and click Next. 
 Note If you do not see NI SystemLink Tag Support for LabVIEW
 <*version*> listed, you automatically installed it
 with FlexLogger.
  4. Follow the instructions to complete installation.
3. Open the example LabVIEW project located at %Program Files%\National
 Instruments\FlexLogger <version>\Examples\SystemLink Integration\FlexLogger Tag
 Examples.lvproj. 
 This LabVIEW project contains several example VIs for sending I/O data points to
 FlexLogger, importing I/O from an existing FlexLogger project, or programmatically
 controlling output values in FlexLogger. NI recommends using Simulated
 Temperature Chamber Example.vi to get started with exchanging data using the
 SystemLink tags.

Parent topic:

Publish or Consume Data Locally (Legacy)

<!--NI_TOPIC bundle=flexlogger path=exporting-alarm-history.html language=enus -->
## TOPIC 00048: Exporting Alarm History to CSV File Format

- bundle_id: `flexlogger`
- source_path: `exporting-alarm-history.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/exporting-alarm-history.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: You can export your alarm notifications in the CSV format on demand. Introduced in FlexLogger 2019 R4 Click the Export button from the Alarm History pane. If necessary, specify the desired File location from the Export to CSV File Format dialog. If necessary, set the export format settings by going

### Exporting Alarm History to CSV File
 Format

You can export your alarm notifications in the CSV format on demand.

Introduced in FlexLogger 2019 R4

1. Click the Export button from the Alarm
 History pane. 
 [IMAGE alt='image' src='GUID-9F6D375D-7A16-46A4-8B8F-CCC40FFE0437-a5.svg']
2. If necessary, specify the desired File location from the
 Export to CSV File Format dialog.
3. If necessary, set the export format settings by going to File»Preferences and clicking the Export tab.

Parent topic:

Adding an Alarm

<!--NI_TOPIC bundle=flexlogger path=extended-support-changes.html language=enus -->
## TOPIC 00049: Updates and Changes for FlexLogger Extended Support Versions

- bundle_id: `flexlogger`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/extended-support-changes.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in FlexLogger versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible chang

### Updates and Changes for FlexLogger Extended Support Versions

Browse updates and changes made in FlexLogger versions
 on extended support.

Note

Release Notes

#### FlexLogger 2021 R4 New Features and
 Changes

FlexLogger 2021 R4 includes new hardware support, measurement offset compensation using
 the Auto Zero setting, and manual CAN/LIN port disabling through the
 Channel Specification.

- Support for PXIe-1090.
- Support for low-cost USB DAQ devices. Refer to Supported Hardware for specific model
 support information.
- Increase measurement accuracy by compensating for internal offsets with the auto zero
 setting. In your Channel Specification, click the drop-down menu ( ) for your module and select
 Auto Zero to configure the setting. Refer to
 Supported Hardware to learn which devices support auto zero.
- Stop all signals and measurements on a CAN/LIN port so it can be used by
 other software. In your Channel Specification, check
 Disable for the port you want to disable.
 FlexLogger closes all CAN/LIN connections.
- (Preview Feature) Test ECUs using A2L databases that rely on the CAN
 Calibration Protocol (CCP). In your Channel Specification, click
 Add measurements for the port you want to
 configure and specify the protocol.

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2021 R3 New Features and
 Changes

FlexLogger 2021 R3 includes new digital I/O module support, performance and throughput
 improvements, and expanded FlexLogger Automation API capabilities.

- Support for PXI and PXIe Digital I/O Modules. Refer to Supported Hardware for specific
 model support information.
- Better performance for large systems, including faster response times for
 viewing live data.
- Higher maximum data throughput for high speed systems.
- Locate FlexLogger project files and read elapsed test times with the Python-based
 FlexLogger Automation API.
- Log the synchronization status of devices synchronized across an Ethernet network.

Related concepts:

- Automating FlexLogger Tests Using Python

Related reference:

- FlexLogger Supported Hardware
- Synchronization Status

#### FlexLogger 2021 R2 New Features and
 Changes

FlexLogger 2021 R2 includes new hardware support, support for driving CAN/LIN outputs
 non-deterministically, support for project locking and test pausing, and integrated log file
 backup creation.

- Support for PXIe-6738 and PXIe-6739 Analog Output Modules. Refer to Supported Hardware for
 specific model support information.
- Support for NI-9326 C Series Frequency Input Module.
- Drive CAN/LIN output signals non-deterministically by mapping the output to another
 channel. Refer to Adding Signals to Your CAN/LIN Module Channel
 Specification for more information.
- Lock a configured project to prevent changes.
- Pause a test to suspend data logging, triggers, and time-based events. Refer to Running a
 Test for more information.
- Back up your data log files by saving them to an additional location. Refer to Configuring
 a Log File for more information.

Related tasks:

- Adding Signals to Your CAN/LIN Module Channel Specification
- Locking a Configured Project
- Running a Test
- Configuring a Log File

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2021 R1 New Features and
 Changes

FlexLogger 2021 R1 includes new hardware support, adds FlexLogger automation support,
 and adds data analysis functionality to the TDMS viewer.

- Support for USB X Series devices. Refer to Supported Hardware for specific model support
 information.
- Support for PXIe X Series counters.
- Drive DAQ output signals non-deterministically by mapping to another
 channel.
- Use test properties as placeholders in file names and locations.
- Automate FlexLogger with the Python-based FlexLogger Automation API.
- Onboard counter support for CompactDAQ chassis.
- Analyze logged data with the TDMS viewer using built-in analysis functions,
 including arithmetic and fast Fourier transform (FFT) analyses.

Related concepts:

- Automating FlexLogger Tests Using Python

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2020 R4 New Features and
 Changes

FlexLogger 2020 R4 includes PXIe X Series device support, multi-PXIe chassis
 synchronization support, and Python integration.

- Support for PXIe X Series devices. Refer Supported Hardware for specific model support
 information.
- Multi-PXIe chassis synchronization support using the high-density trigger ports. Refer to
 Supported Hardware for specific model support information.
- Create variable channels to act as static integer values.
- Use anti-aliased downsampling to acquire from DSA modules at 100 Hz.
- Use Python to interact with FlexLogger (compatible with 2020 R3 and 2020 R4). Refer to
 Exchanging Data with Python for more information.
- (Preview Feature) Onboard counter support for CompactDAQ chassis.
- (Preview Feature) Publish tags and files to SystemLink Cloud.

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2020 R3 New Features and
 Changes

FlexLogger 2020 R3 includes improved shunt calibration feedback, project-level TEDS
 sensor scanning, resistance measurement support, and support for LabVIEW 2020 in the
 FlexLogger PDK.

- Better shunt calibration feedback, including calculated values displayed in
 channel details and error messaging.
- Scan for TEDS sensors at the project level.
- Support for resistance measurements. Refer to Supported Hardware for specific model support
 information.
- Support for LabVIEW 2020 in the FlexLogger Plug-in Development Kit 1.3.
- (Preview Feature) Publish tags and files to a connected SystemLink Server. This preview
 feature requires a separate license for SystemLink Server.

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2020 R2 New Features and
 Changes

FlexLogger 2020 R2 includes expanded simultaneous channel configuration support,
 read-only channel support for TEDS sensors, and digital input plug-in channel support in the
 FlexLogger PDK.

- Configure multiple I/O channels simultaneously, including alarm
 configuration.
- Apply shunt calibration to multiple channels simultaneously.
- Added read-only channel support for TEDS sensors.
- Alarm and event information logged to test TDMS file.
- Support for digital input plug-in channels in the FlexLogger Plug-in Development Kit
 1.2.

#### FlexLogger 2020 R1 New Features and
 Changes

FlexLogger 2020 R1 includes new hardware support, support for data visualization with XY
 graphs on live data screens, and support for triggering events when a test
 concludes.

- Added PXI Express support for SC Express, sound and vibration, and automotive bus modules.
 Refer to the Supported Hardware section for specific model information.
- Added hardware support for NI-9262
- Added support for LVDT/RVDT sensors
- XY graph type added to Screens
- Event triggering on test stop

#### FlexLogger 2019 R4 New Features and
 Changes

FlexLogger 2019 R4 includes new hardware support, support for toast notifications and
 history exporting for alarms, new function and input support for formulas, and custom
 analysis PDK plugin support.

- Added hardware support for:
  - NI-9252
  - NI-9253
- Apply zero and null offset calibration to multiple channels
 simultaneously
- Export alarm history to CSV file format
- Save project as support for existing projects
- Event triggered on test time elapsed
- Toast notification support for channel alarms
- Integrated system health metric reporting
- Digital input support in arithmetic and Boolean formulas
- Calculation formula support for logarithm functions, ? : operator, and e,
 true, and false constants
- Configurable sample rate for CAN/LIN
- Support for custom analysis plug-ins created with the FlexLogger Plug-in Development Kit
 1.1

#### FlexLogger 2019 R3 New Features and
 Changes

FlexLogger 2019 R3 adds new FieldDAQ hardware support, input channel alarms, expanded
 support for LIN communication, custom PDK I/O plugin support, and offline access to the
 FlexLogger User Manual.

- Added hardware support for the FD-11605
- Alarms for input channels, including the following features:
  - Alarm history pane
  - Event triggering from alarms
- Reset values on output channels
- Additional measurement types for counter input modules:
  - Angular position
  - Linear position
  - Pulse
- Hardware filter support for FieldDAQ
- Support for custom I/O plug-ins created with the FlexLogger Plug-in Development Kit
 1.0
- Boolean logic for analog channels
- Digital input event triggering
- Output support for LIN
- LIN master support
- Offline FlexLogger manual access

#### FlexLogger 2019 R2 New Features and
 Changes

FlexLogger 2019 R2 adds new hardware support, enhances I/O support for CAN and LIN
 communication, and adds new information visualization methods such as timestamped test
 notes.

- Added hardware support for:
  - FD-11634
  - NI-9866
  - USB-8506
- Output support for CAN
- Input support for LIN
- Capability to add timestamped notes during test
- Lowpass and highpass Butterworth filter channels added to Channel
 Specification
- TSN synchronization feedback
- No limits on Slow/Medium/Fast/Digital sample rate configuration
- System memory monitoring and dynamic visualization settings
- Pull-up resistor support and threshold voltage support for the NI 9361
- Powered sensor support for the FD-11601

#### FlexLogger 2019 R1 New Features and
 Changes

FlexLogger 2019 R1 includes new hardware support and Channel Specification
 updates.

- Added hardware support for:
  - NI-9231
  - FD-11601
  - FD-11614
- Enhanced system visualization in Channel Specification
- RMS and Mean averaging of channels added to Channel Specification
- Screen visualization shows minimum and maximum data values in visible
 range

Note

FlexLogger Readme

#### FlexLogger 2018 R4 New Features and
 Changes

FlexLogger 2018 R4 adds support for static-level output through C Series modules,
 project metadata, and controlling channel set points through NI Skyline Data
 Services.

- Static-level output, including added hardware support for:
  - C Series Voltage Output Modules
  - C Series Current Output Modules
  - C Series Digital Modules
  - C Series User Interface Module
- Project metadata support
- Support for control of output channel set points through NI Skyline Data Services

<!--NI_TOPIC bundle=flexlogger path=extending-functionality.html language=enus -->
## TOPIC 00050: Extending FlexLogger Functionality

- bundle_id: `flexlogger`
- source_path: `extending-functionality.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/extending-functionality.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use additional interfaces to integrate third-party I/O, add custom calculations, and communicate with external systems to supplement your data acquisition system.

### Extending FlexLogger Functionality

Use additional interfaces to integrate third-party I/O, add custom calculations, and
 communicate with external systems to supplement your data acquisition system.

- [Adding a Plug-In to Your Project](adding-a-plug-in.html) Plug-ins allow you to extend the functionality of FlexLogger and create specialized analysis, integration, and automation capabilities for your project.
- [Using SystemLink to Share Data and Back Up Files](using-systemlink-to-exchange-data-back-up-files.html) Connect to SystemLink so you can automatically back up, share, and remotely monitor test data from your FlexLogger project.
- [Automating FlexLogger Operations Using TestStand](flexlogger-teststand.html) Use the FlexLogger TestStand step to automate FlexLogger operations from a TestStand sequence.
- [Automating FlexLogger Tests Using Python](automating-flexlogger-tests-using-python.html) Use the FlexLogger Python APIs to modify the configuration of existing FlexLogger projects and control the execution of FlexLogger test sessions.

<!--NI_TOPIC bundle=flexlogger path=flexlogger-teststand.html language=enus -->
## TOPIC 00051: Automating FlexLogger Operations Using TestStand

- bundle_id: `flexlogger`
- source_path: `flexlogger-teststand.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/flexlogger-teststand.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the FlexLogger TestStand step to automate FlexLogger operations from a TestStand sequence. Introduced in FlexLogger 2025 Q1Select FlexLogger Support for TestStand when installing FlexLogger to install the FlexLogger TestStand step. This step is selected by default if TestStand is already install

### Automating FlexLogger Operations Using
 TestStand

Use the FlexLogger TestStand step to automate FlexLogger operations from a TestStand
 sequence.

Introduced in
 FlexLogger 2025 Q1

FlexLogger Support for TestStand

Note

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more
 information.

- Opening and closing a FlexLogger project
- Starting and stopping a test
- Changing the value of a FlexLogger channel
- Getting and setting test metadata and logging information

You can open the shipping example in
 C:\Users\Public\Documents\National Instruments\TestStand <version>
 (64-bit)\Examples\FlexLogger to see how to use some FlexLogger
 operations from TestStand.

1. Launch your TestStand sequence and drag the FlexLogger
 step onto your sequence from the TestStand Step Types
 menu.
2. Configure the step settings for the FlexLogger step using the Step
 Settings window. You can select the FlexLogger operation you want
 to automate using the drop-down list at the top of the window.

Parent topic:

Extending FlexLogger Functionality

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=frequency-spectrum-graph.html language=enus -->
## TOPIC 00052: Frequency Spectrum Graph

- bundle_id: `flexlogger`
- source_path: `frequency-spectrum-graph.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/frequency-spectrum-graph.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexLogger can visualize the frequency spectrum of your signals using a Frequency Spectrum Graph. FlexLogger uses the LabVIEW FFT Power Spectrum and PSD VI to compute the magnitude of the averaged power spectrum of your input signal. FlexLogger reports the magnitude of the averaged power spectrum in

### Frequency Spectrum Graph

FlexLogger can visualize the frequency spectrum of your signals using a Frequency
 Spectrum Graph.

FlexLogger uses the LabVIEW FFT Power Spectrum and PSD VI to compute
 the magnitude of the averaged power spectrum of your input signal. FlexLogger reports
 the magnitude of the averaged power spectrum in decibels (dB).

FlexLogger converts the magnitude from input signal units to dB using the equation below,
 where *Y*<sub>i</sub> is the magnitude of the averaged power spectrum in dB
 and *X*<sub>i</sub> is the magnitude of the averaged power spectrum in the
 units of your input. For example, volts.

Y

i

⁢

=

10

*

log

⁡

10

(

X

i

)

For more information, refer to the LabVIEW documentation on
 ni.com/docs.

Parent topic:

Visualizing Live Data with Indicators and Graphs

<!--NI_TOPIC bundle=flexlogger path=high-speed-can-termination.html language=enus -->
## TOPIC 00053: High-Speed CAN Cable Termination

- bundle_id: `flexlogger`
- source_path: `high-speed-can-termination.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/high-speed-can-termination.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: The pair of signal wires (CAN_H and CAN_L) constitutes a transmission line. If the transmission line is not terminated, each signal change on the line causes reflections that may cause communication failures. Because communication flows both ways on the CAN bus, CAN requires that both ends of the ca

### High-Speed CAN Cable Termination

The pair of signal wires (CAN_H and CAN_L) constitutes a transmission line. If the transmission line is not terminated, each signal change on the line causes reflections that may cause communication failures.

Because communication flows both ways on the CAN bus, CAN requires that both ends of the cable be terminated. However, this requirement does not mean that every device should have a termination resistor. If multiple devices are placed along the cable, only the devices on the ends of the cable should have termination resistors. Refer to the following figure for an example of where termination resistors should be placed in a system with more than two devices.

Figure 7.

[IMAGE alt='image' src='GUID-20C5E953-CDE7-4581-8C66-67A369279278-a5.svg']

The termination resistors on a cable should match the nominal impedance of the cable. ISO 11898 requires a cable with a nominal impedance of 120 Ω, so you should use a 120 Ω resistor at each end of the cable. Each termination resistor should be capable of dissipating 0.25 W of power.

NI high-speed CAN devices feature software-selectable bus termination for High-Speed CAN transceivers. On the USB-8502 (in high-speed mode) and on CAN HS/FD and CAN XS Transceiver Cables, you can enable 120 Ω termination resistors between CAN_H and CAN_L through an API call.

Parent topic:

Adjusting Port/Interface Settings

<!--NI_TOPIC bundle=flexlogger path=how-flexlogger-connects-to-your-hardware.html language=enus -->
## TOPIC 00054: How FlexLogger Connects to Your Hardware

- bundle_id: `flexlogger`
- source_path: `how-flexlogger-connects-to-your-hardware.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/how-flexlogger-connects-to-your-hardware.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexLogger automatically discovers any installed hardware and displays it in the Channel Specification. If you do not have hardware that is installed, refer to What if I do not have hardware? to learn how to simulate a device. After creating a project, you can view your hardware in the Channel Speci

### How FlexLogger Connects to Your
 Hardware

FlexLogger automatically discovers any installed hardware and displays it in the
 Channel Specification.

If you do not have hardware that is installed, refer to *What if I do not have
 hardware?* to learn how to simulate a device.

Channel
 Specification

[IMAGE alt='image' src='GUID-0D9239A6-471B-4CAA-883D-4AC3D60AEC28-a5.png']

Available device channels are beneath the module information. Data acquisition modules show
 the model name and number along with the slot the modules are installed in. Automotive devices
 (CAN and LIN) display all available ports, and channels you add are listed beneath the device
 port information.

After FlexLogger discovers your hardware, you can see the hardware in your project and
 configure device channels.

#### What if my hardware does not
 appear?

Channel
 Specification

- Ensure you are using supported hardware.
- Confirm your devices are properly connected
 and powered.
- Open the Hardware Configuration Utility and confirm your device is listed. If your
 device is not listed, refer to the Related information to learn how to
 manage system hardware in the Hardware Configuration Utility. After adding your device
 in the Hardware Configuration Utility, click Refresh network
 hardware 
 in FlexLogger to see your reserved
 device.

#### What if my hardware appears grayed
 out?

- Click Reassign 
 to transfer the module project settings to
 another compatible module in your system. Note You cannot undo this
 operation.
- Click Delete 
 to remove the hardware from the
 project.

#### What if
 I do not have hardware?

Simulate a USB DAQ from FlexLogger. In the
 Channel Specification document, click Simulate a USB
 DAQ. FlexLogger creates a simulated USB-6421 and adds it to your
 Channel Specification.

You can simulate other NI-DAQmx devices
 from the Hardware Configuration Utility. For more information, refer to the *Related
 information*.

Related tasks:

- Configuring Device Channels

Related reference:

- FlexLogger Supported Hardware

Related information:

- Managing System Hardware

<!--NI_TOPIC bundle=flexlogger path=initiate-action-with-button.html language=enus -->
## TOPIC 00055: Initiating an Action with a Button

- bundle_id: `flexlogger`
- source_path: `initiate-action-with-button.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/initiate-action-with-button.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Generate a response from your system with the click of a button. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Add a button to a Screen document to trigger an event that you configure in your Test Specification or run a .b

### Initiating an Action with a Button

Generate a response from your system with the click of a button.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more information.

Screen

Test Specification

.bat

.exe

1. In your Screen document, click
 Actions in the palette located on the left side of
 the window.
2. Navigate to the Item configuration pane located on the
 right side of the Screen window.
3. Specify the type of action you want the button to initiate in the
 Action type drop-down menu. 
 Table 48.Action Button
 TypesOption
 DescriptionEXE
 Run an executable (.exe) located in
 the file path you specify. You can pass arguments to the
 executable file.
 BAT
 Run a batch (.bat) file located in
 the file path you specify. You can pass arguments to the
 batch file.
 Event
 Trigger an event. Enter a descriptive name for the action button.
 FlexLogger lists your action button by this name in
 the Test Specification.
 Click Open Test
 Specification. [IMAGE alt='image' src='GUID-29165645-5005-4E24-8E33-1A991EA369C5-a5.png']
 In the Test Specification, add
 and configure the event that you want to trigger
 with the action button. Select Button
 pressed in the
 If condition drop-down
 menu. For more information, refer to *Adding an
 Event*.

Parent topic:

Defining Your Test Configuration

Related tasks:

- Adding an Event

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=interface.html language=enus -->
## TOPIC 00056: Navigating FlexLogger

- bundle_id: `flexlogger`
- source_path: `interface.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/interface.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about the FlexLogger User Interface (UI) and FlexLogger project file structure so you can quickly create projects. Components of a FlexLogger ProjectA FlexLogger project (.flxproj) contains all the documents and files that configure your system, define test automation, and log and monitor your

### Navigating FlexLogger

Learn about the FlexLogger User Interface (UI) and FlexLogger project file structure so
 you can quickly create projects.

#### Components of a FlexLogger
 Project

A FlexLogger project (.flxproj) contains all
 the documents and files that configure your system, define test automation, and log
 and monitor your data. Additionally, the project allows you to view and track the
 logged data files.

Access your project documents and files in the Navigation
 pane on the left of your view.

[IMAGE alt='image' src='GUID-AB58BF64-030D-461E-95E8-FB978549AE27-a5.png']

#### Project Files Tab

Project Files

| Document | Description |
| --- | --- |
| Channel Specification (.flxio) | Configures the inputs and outputs of your measurement system. Specifies the conditions for triggering alarms. |
| Logging Specification (.flxcfg) | Specifies the name, structure, and location for your log files and configures logging and triggering behavior. |
| Test Specification (.flxtest) | Adds automation to your project to control output signals. |
| Screen (.flxscr) | Displays data visualizations so you can monitor live signals and control your test system. |

#### Data Tab

The Data tab stores the logged data files from your test
 procedures.

<!--NI_TOPIC bundle=flexlogger path=j1939-application-protocol-basics.html language=enus -->
## TOPIC 00057: J1939 Application Protocol Basics

- bundle_id: `flexlogger`
- source_path: `j1939-application-protocol-basics.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/j1939-application-protocol-basics.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic provides an overview of the J1939 application protocol. If there's a way we could shorten/condense this example, I can see a case for leaving it in this topic. But it's so much longer than the steps themselves the way it is now, which makes the topic less focused. We decided we definitely

### J1939 Application Protocol Basics

This topic provides an overview of the J1939 application protocol.

J1939 is set of SAE standards commonly used in diesel-powered applications for communication and diagnostics between application components. The J1939 standard enables a high-level protocol that allows for communication across large, complex networks used by manufacturers of large, industrial ECUs such as heavy duty vehicles, and mining, construction, or agricultural machinery.

The J1939 standard is defined in multiple documents corresponding to five of the seven OSI layers. J1939-11 defines the physical layer, J1939-21 defines the data link and transport layer, J1939-31 defines the network layer, and J1939-71/73 defines the application layer. J1939-81 describes network management.

J1939 application protocol uses a 29-bit extended frame identifier. The ID is divided into several parts, including the PGN, which identifies the frame and defines which signals it contains. You can send a frame to a global address (all nodes) or a specific address (node with this address). This information is coded inside the PGN, which comprise 18 of the 29-bit identifier.

For destination-specific messages, PS defines the destination address, so PF defines only 240 destination-specific PGNs (0-239).

If your application requires the J1939 application protocol, refer to *Applying J1939
 Application Protocol*.

Parent topic:

CAN Databases

Related tasks:

- Applying J1939 Application Protocol

<!--NI_TOPIC bundle=flexlogger path=led-behavior.html language=enus -->
## TOPIC 00058: LED Behavior

- bundle_id: `flexlogger`
- source_path: `led-behavior.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/led-behavior.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following tables to understand the meaning of different LED behaviors on your CAN or LIN module. Each LED can display two colors (red or green), which display in the following four patterns: 36 LED Display Patterns Pattern Meaning Off No LED illumination Solid LED fully illuminated Blin

### LED Behavior

Refer to the following tables to understand the meaning of different LED behaviors on
 your CAN or LIN module.

Each LED can display two colors (red or green), which display in the following four patterns:

| Pattern | Meaning |
| --- | --- |
| Off | No LED illumination |
| Solid | LED fully illuminated |
| Blink | Blinks at a constant rate of several times per second |
| Activity | Blinks in a pseudo-random pattern |

| Condition/State | LED 1 | LED 2 |
| --- | --- | --- |
| Port identification | Blinks green | Blinks green |
| Catastrophic error | Blinks red | Blinks red |
| No open session on hardware | Off | Off |
| Open session on hardware, port is properly powered, and hardware is not communicating | Solid green | Off |
| Open session on hardware, port is missing power | Solid red | Off |

Note

| Condition/State | LED 1 | LED 2 |
| --- | --- | --- |
| Hardware is communicating, and controller is in Error Active state | Solid green | Activity green (returns to idle/off one second after last TX or RX) |
| Hardware is communicating, and controller is in Error Passive state | Solid green | Activity red (returns to idle/off one second after last TX or RX) |
| Hardware is running, and controller transitioned to bus off | Solid green | Solid red |

Note

| Condition/State | LED 1 | LED 2 |
| --- | --- | --- |
| Hardware is communicating | Solid green | Activity green (returns to idle/off one second after last TX or RX) |

| Condition/State | Ready LED |
| --- | --- |
| Connected to a port supporting at least USB High Speed operation (USB 2.0+) and usable. | Solid red |
| Unusable | Off |

| Condition/State | Ready LED |
| --- | --- |
| Port identification | Blinks green |
| Catastrophic error | Blinks red |
| No open session on hardware | Off |
| Interface is configured, no activity, in error active state | Solid green |
| Open session on hardware, port is missing power from bus | Solid red |
| Hardware is communicating and controller is in Error Active state | Activity green |
| Hardware is communicating and controller is in Error Passive state | Activity red |
| Hardware is running and controller transitioned to bus off | Solid red |

| Condition/State | Ready LED |
| --- | --- |
| Port identification | Blinks green |
| Catastrophic error | Blinks red |
| No open session on hardware | Off |
| Open session on hardware port is properly powered, and hardware is not communicating | Solid green |
| Open session on hardware, port is missing power from bus | Solid red |
| Hardware is communicating | Activity green |

Parent topic:

Configuring an Automotive Bus

<!--NI_TOPIC bundle=flexlogger path=lin-cable-termination.html language=enus -->
## TOPIC 00059: LIN Cable Termination

- bundle_id: `flexlogger`
- source_path: `lin-cable-termination.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/lin-cable-termination.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI LIN devices are terminated at the transceiver, but master termination can be enabled in FlexLogger. Introduced in FlexLogger 2019 R2 LIN cables require no termination, as nodes are terminated at the transceiver, which utilizes slave nodes that are typically pulled up from the LIN bus to VBat with

### LIN Cable Termination

NI LIN devices are terminated at the transceiver, but master termination can be
 enabled in FlexLogger.

Introduced in FlexLogger 2019 R2

30 kΩ

1 kΩ

Termination

Interface Settings

Parent topic:

LIN Databases

<!--NI_TOPIC bundle=flexlogger path=lin-databases.html language=enus -->
## TOPIC 00060: LIN Databases

- bundle_id: `flexlogger`
- source_path: `lin-databases.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/lin-databases.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Manage your embedded networks using LIN databases, which provide a consistent set of parameters for all nodes in the network. Introduced in FlexLogger 2019 R2 LIN databases allow you to store frames and signals running on the network in a database, as well as information about which ECU is transmitt

### LIN Databases

Manage your embedded networks using LIN databases, which provide a consistent set of
 parameters for all nodes in the network.

Introduced in FlexLogger 2019 R2

LIN databases allow you to store frames and signals running on the network in a database, as
 well as information about which ECU is transmitting or receiving which data. This
 information also is needed for each node in the network.

Databases in FlexLogger consist of clusters, which contain a number of frames, which are
 comprised of the signals used to send data.

- Cluster —The basic entity of a database. A cluster is the description of a
 single network (for example, a LIN bus).
- Frame —A single message that is exchanged on the cluster.
- Signal —The basic data exchange unit on the network. These signals are
 equivalent to LIN channels.

Parent topic:

Configuring an Automotive Bus

<!--NI_TOPIC bundle=flexlogger path=locking-configured-project.html language=enus -->
## TOPIC 00061: Locking a Configured Project

- bundle_id: `flexlogger`
- source_path: `locking-configured-project.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/locking-configured-project.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: You can lock a configured project to prevent unwanted changes. Introduced in FlexLogger 2021 R2 Select ProjectLock project to launch the Lock project dialog box. Create and retype a memorable password. Click OK. FlexLogger locks all project documents and dims configuration options. You can still con

### Locking a Configured Project

You can lock a configured project to prevent unwanted changes.

Introduced in FlexLogger 2021 R2

1. Select Project»Lock project to launch the Lock project dialog box.
2. Optional: 
 Create and retype a memorable password.
3. Click OK. 
 FlexLogger locks all project documents and dims configuration options. Note You can still configure alarms for
 individual channels.
4. To unlock the project, select Project»Unlock project and enter the password.

Parent topic:

Defining Your Test Configuration

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=low-speed-can-termination.html language=enus -->
## TOPIC 00062: Low-Speed CAN Cable Termination

- bundle_id: `flexlogger`
- source_path: `low-speed-can-termination.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/low-speed-can-termination.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: The pair of signal wires (CAN_H and CAN_L) constitutes a transmission line. If the transmission line is not terminated, each signal change on the line causes reflections that may cause communication failures. Every device on the Low-Speed CAN network requires a termination resistor for each CAN data

### Low-Speed CAN Cable Termination

The pair of signal wires (CAN_H and CAN_L) constitutes a transmission line. If the transmission line is not terminated, each signal change on the line causes reflections that may cause communication failures.

Every device on the Low-Speed CAN network requires a termination resistor for each CAN data line: RRTH for CAN_H and RRTL for CAN_L. The following figure shows termination resistor placement in a Low-Speed CAN network.

Figure 8.

[IMAGE alt='image' src='GUID-F8D42696-4A8A-4EB3-8EF3-EC7E6D09551B-a5.svg']

To determine the correct termination resistor values for the Low-Speed CAN transceiver,
 refer to *Determining the Necessary Termination Resistance for Your Low-Speed CAN
 Device*.

Parent topic:

Adjusting Port/Interface Settings

Related tasks:

- Determining the Necessary Termination Resistance for Your Low-Speed CAN Device

<!--NI_TOPIC bundle=flexlogger path=managing-can-lin-databases.html language=enus -->
## TOPIC 00063: Managing CAN/LIN Databases

- bundle_id: `flexlogger`
- source_path: `managing-can-lin-databases.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/managing-can-lin-databases.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add, rename, or delete databases, or change the signals and properties within a database. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Go to FileManage CAN/LIN databases. Use the dialog that appears to add, remove, or ren

### Managing CAN/LIN Databases

Add, rename, or delete databases, or change the signals and properties within a
 database.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. Go to File»Manage CAN/LIN databases. 
 Use the dialog that appears to add, remove, or rename your available
 databases.
2. Double-click any database to launch the CAN/LIN Database Editor. 
 The CAN/LIN Database Editor is a small standalone tool for creating and
 maintaining embedded network databases. You can use the editor to perform any of
 the following actions to the selected database: Create a cluster for the database.Individually adjust cluster
 properties, including adding or removing frames from the cluster.Individually adjust frame
 properties, including adding or removing signals from the frame.Individually adjust signal
 properties.

Parent topic:

Configuring an Automotive Bus

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=manually-exporting-data-to-csv.html language=enus -->
## TOPIC 00064: Manually Exporting Data Files to CSV File Format

- bundle_id: `flexlogger`
- source_path: `manually-exporting-data-to-csv.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/manually-exporting-data-to-csv.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Export your data files in the CSV file format on demand. Introduced in FlexLogger 2018 R3 On the Data tab, right-click the log file and select Export. In the Export to CSV file format dialog, specify the desired File location to save your file, if necessary. The default is the same location as the T

### Manually Exporting Data Files to CSV File
 Format

Export your data files in the CSV file format on demand.

Introduced in FlexLogger 2018 R3

1. On the 
 Data tab, right-click the log file and select 
 Export.
2. In the 
 Export to CSV file format dialog, specify the desired 
 File location to save your file, if necessary. The default is the same location as the TDMS logging 
 Base path.
3. Specify the 
 CSV file data rate, if necessary. 
 Note All logged data channels are mapped to a common CSV data rate. The CSV data rate is applied as follows: 
 The common CSV start time is the first time stamp of all logged channels.Each CSV time stamp uses the logged value in each channel that occurs just before or at the same time as the time stamp.This CSV data rate mapping runs while any channel provides data. Exported log files from mapped channels might contain gaps at the end if any channel stopped providing data.
4. Click 
 OK to finish the data file export.

Parent topic:

Viewing, Analyzing, and Exporting Data

<!--NI_TOPIC bundle=flexlogger path=monitoring-computer-resources.html language=enus -->
## TOPIC 00065: Monitoring Computer Resources

- bundle_id: `flexlogger`
- source_path: `monitoring-computer-resources.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/monitoring-computer-resources.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add System Resource Monitor channels to track CPU usage, hard drive availability, memory usage, and network activity on your computer. Introduced in FlexLogger 2019 R2 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. In the C

### Monitoring Computer Resources

Add System Resource Monitor channels to track CPU usage, hard drive availability,
 memory usage, and network activity on your computer.

Introduced in FlexLogger 2019 R2

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. In the Channel Specification, select Add channels»System Resource Monitor in the toolbar. 
 FlexLogger adds channels to the Channel Specification to
 show CPU usage, hard drive availability, memory usage, and network activity.
2. Optional: 
 Change the name of one or more channels.
3. Optional: 
 Add an alarm to one or more channels.

Parent topic:

Configuring Device Channels

Related tasks:

- Adding an Alarm

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=network-synchronization-status.html language=enus -->
## TOPIC 00066: Synchronization Status

- bundle_id: `flexlogger`
- source_path: `network-synchronization-status.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/network-synchronization-status.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: FlexLogger displays the synchronization status of your system on the toolbar, helping you troubleshoot synchronization issues based on the status of your system. Introduced in FlexLogger 2019 R2 This feature is only available as part of a complete FlexLogger license. Refer to FlexLogger Editions for

### Synchronization Status

FlexLogger displays the synchronization status of your system on the toolbar, helping
 you troubleshoot synchronization issues based on the status of your system.

Introduced in FlexLogger 2019 R2

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is only available as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

FlexLogger supports network and PXIe synchronization for compatible devices. If your system
 does not require or support synchronization, you can disable this feature by going to File»Preferences and unchecking Enable multi-chassis and network
 synchronization on the General tab.

[IMAGE alt='image' src='GUID-EF957A8A-6E8A-4046-80F3-8638E9E1DAB3-a5.png']

| SYNC Status | Meaning | Troubleshooting Tips |
| --- | --- | --- |
| No SYNC status in toolbar | Your system has only one chassis or device. | - |
| Red | Not all devices are synchronized. Click SYNC to Display which supported devices in your system are synchronized. Display which devices don't support synchronization. | Your system meets synchronization conditions, but errors exist with the device or network setup. Verify that none of the following issues are present in your system: The IEEE 802.1AS or 1588 subnet does not support the external switch used in the network configuration. (Network sync) Devices are connected on the network in more than one subnet. (Network sync) The HDMI cables are connected to the incorrect "In" and "Out" ports. See your chassis manual for more information. (PXIe sync) Your device does not support synchronization. Your project displays a supported device with configured channels but the device is not present in the system. |
| Grey | Synchronization is disabled in Preferences. | Ensure that you enabled Enable multi-chassis and network synchronization at File » Preferences. |
| You did not correctly configure your project for synchronization. | Ensure that at least two chassis or devices support synchronization. Ensure you have one or more channels configured in at least two of the synchronization-supported devices. Devices without configured channels are not included. |  |
| Yellow | Multiple synchronization groups detected. Devices in the same sync group are synchronized. | Devices on the network are connected in more than one subnet, or are separated by a network switch that does not support 802.1AS. This is expected behavior if your network meets one of the following conditions: You have multiple sync groups on different subnets. You have both a PXI sync group and a TSN sync group. |
| Green | Synchronization is enabled and the device configuration is supported, but unavailable devices have one or more channels configured for synchronization. | Verify your hardware configuration has all devices available. |
| Synchronization is enabled and the device configuration is supported. | — |  |

Parent topic:

Synchronization

Related tasks:

- Using PXIe Synchronization in Your Project
- Using Network Synchronization in Your Project

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=new-features-and-changes.html language=enus -->
## TOPIC 00067: FlexLogger New Features and Changes

- bundle_id: `flexlogger`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/new-features-and-changes.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of FlexLogger. Discover what is new in the latest releases of FlexLogger.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### FlexLogger
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of FlexLogger.

FlexLogger

Note

Release Notes

Related information:

- Download FlexLogger
- FlexLogger Plug-in Development Kit Compatibility with FlexLogger
 and LabVIEW
- FlexLogger and LabVIEW Compatibility
- FlexLogger and TestStand Compatibility

#### FlexLogger
 2026 Q2 Changes

FlexLogger 2026 Q2 adds support for creating projects
 using Excel spreadsheets.

- Added a Spreadsheet Importer tool which allows users to create FlexLogger projects based
 on formatted Excel spreadsheets. The Spreadsheet Importer enables you to use the
 command line or the built-in FlexLogger UI to:
  - Create template spreadsheets to use as the basis for FlexLogger
 projects.
  - Import populated spreadsheets to create FlexLogger projects.

Related concepts:

- Creating a Project Using the Spreadsheet Importer

Related tasks:

- Creating a Template Spreadsheet Using FlexLogger
- Creating a Template Spreadsheet Using the Command Line
- Using the Spreadsheet Importer Through FlexLogger
- Using the Spreadsheet Importer Through the Command Line

Related reference:

- Creating Your Project Spreadsheet
- Populating Your Spreadsheet with Data

#### FlexLogger
 2026 Q1 Changes

FlexLogger 2026 Q1 includes support for multifunction
 I/O modules, myDAQ, additional thermocouple types, and the Output Sequencer plug-in.

- Added support for the following hardware:
  - PCIe-6345/6347/6355/6357 multifunction I/O devices
  - PXIe-6381/6383 multifunction I/O modules
- Added support for configuration and data logging on the myDAQ Student Data Acquisition
 Device. FlexLogger doesn't support myDAQ audio output.
- Use the Output Sequencer plug-in to create automated test sequences. NI created the
 Output Sequencer plug-in using the FlexLogger Plug-in Development Kit. The Output
 Sequencer plug-in installs with FlexLogger . To add the
 plug-in to your Channel Specification, select Add channels»Plug-in»Output Sequencer .
- Added support for A-type thermocouples and C-type thermocouples.

Related information:

- Output Sequencer | niflexlogger-plugins GitHub
 Repository

#### FlexLogger 2025
 Q4 Changes

FlexLogger 2025 Q4 adds new hardware support,
 improvements and expansions to data logging, and support for synchronizing multiple TSN sync
 groups.

- Added support for the NI-9320 C Series voltage input
 module.
- Added logging optimizations that reduce log file sizes for files that contain
 digital channels.
- Use the Elapsed Time logging trigger to start or change the logging
 rates for your tests after a certain amount of time passes.
- Use the Button Pressed logging control to manually control your
 test logging rate, raising it to the maximum sample rate to analyze
 operator-detected behaviors and lowering the logging rate afterward.
- Use the Save As function in the LabVIEW and Python automation APIs
 for FlexLogger to programmatically save a copy of
 your FlexLogger project.
- FlexLogger now supports synchronizing multiple TSN
 sync groups when using multi-chassis or network synchronization, instead of only
 synchronizing the largest sync group.
- FlexLogger 2025 Q4 has the following support and
 compatibility updates:
  - LabVIEW automation support for FlexLogger 
 2025 Q4 requires LabVIEW 2025 Q3 or later.
  - TestStand automation support for FlexLogger 
 2025 Q4 requires TestStand 2025 Q2 or later.
  - Added support for Python 3.11, 3.12, and 3.13 to the FlexLogger
 Python Automation API.

Related reference:

- Synchronization Status

Related information:

- niflexlogger-automation GitHub Repository

#### FlexLogger 2025 Q3 Changes

FlexLogger 2025 Q3 adds support for multiple PCIe and PXIe multifunction I/O
 devices.

- Added support for the following hardware:
  - PCIe-6340/6342/6350/6352 multifunction I/O devices
  - PXIe-6321/6323/6343/6351/6353/6357 multifunction I/O modules
- Find detailed API reference documentation for the FlexLogger Plug-In Development Kit
 in-product or online at ni.com/docs . Refer to the FlexLogger
 Plug-In Development Kit API Reference for more information.

Related concepts:

- Accessing the Documentation

Related reference:

- FlexLogger Supported Hardware

Related information:

- FlexLogger Plug-In Development Kit API Reference

#### FlexLogger 2025 Q2 Changes

FlexLogger 2025 Q2 adds new mioDAQ functionality support and support for Measurement
 Plug-Ins.

- Added support for the following mioDAQ functionality:
  - Configurable digital voltage levels
- Use Measurement Plug-Ins to transfer data and functionality between FlexLogger and
 other measurement applications using any programming language.

Related tasks:

- Adding a Measurement Plug-In to Your FlexLogger Project

Related information:

- Measurement Plug-In Overview

#### FlexLogger 2025 Q1 Changes

FlexLogger 2025 Q1 adds new hardware support, expanded mioDAQ functionality support,
 and support for TestStand integration using the FlexLogger TestStand step.

- Added support for the following devices:
  - cDAQ-9183/9187 Ethernet chassis
  - cDAQ-9173/9177 chassis
  - NI-9204
- Added support for the following mioDAQ functionality:
  - Built-in CJC thermocouples
  - PFI trigger filter
- Extend the functionality of FlexLogger with the FlexLogger step in TestStand.
- Find and download plug-ins created by FlexLogger users on the FlexLogger Community
 Plug-ins Github repository.
- Delete MAX configurations for simulated hardware from within FlexLogger without
 opening an additional program.

Related tasks:

- Automating FlexLogger Operations Using TestStand
- Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project

#### FlexLogger 2024 Q4 Changes

FlexLogger 2024 Q4 adds the FlexLogger LabVIEW API and support for connecting
 hardware using the Hardware Configuration Utility.

- Extend the functionality of FlexLogger with the FlexLogger LabVIEW API.
- Use the FlexLogger Python API or the FlexLogger LabVIEW API to programmatically
 disable channel logging.
- Connect your hardware to FlexLogger using the Hardware Configuration Utility instead
 of Measurement & Automation Explorer.
- Improve loading times when opening large projects. Navigate to File»Preferences»Preview features and enable Save and load engine configuration
 files .

Related concepts:

- How FlexLogger Connects to Your Hardware
- Automating FlexLogger Tests Using Python

Related information:

- FlexLogger LabVIEW API Reference

#### FlexLogger 2024 Q3.1 New Features and
 Changes

FlexLogger 2024 Q3.1 adds support for some USB NI mioDAQ devices.

- Added support for the following NI mioDAQ devices:
  - USB-6421
  - USB-6423
  - USB-6451
  - USB-6453

#### FlexLogger 2024 Q3 New Features and
 Changes

FlexLogger 2024 Q3 adds the Min-Max plugin for calculating the minimum and maximum
 value for a group of channels, and adds support for LabVIEW 2024 in the FlexLogger
 PDK.

- Support for LabVIEW 2024 in the FlexLogger Plug-in Development Kit 2024 Q3.
- Use the Min-Max plug-in to calculate the minimum or maximum value for a group of
 channels. NI created the Min-Max plug-in using the FlexLogger Plug-in Development
 Kit. The Min-Max plug-in installs with FlexLogger. Add the plug-in to your
 Channel Specification by selecting Add channels»Plug-in»Min-Max. Then, select the calculation type and the channels.

#### FlexLogger 2024 Q2 New Features and
 Changes

FlexLogger 2024 Q2 adds FlexLogger Lite, dynamic project logging rate configuration,
 and control over SystemLink tag retention.

- Discover which FlexLogger edition is right for you.
  - Use FlexLogger Lite, the free edition of FlexLogger, for your basic data
 logging applications.
  - Try a free trial of FlexLogger for advanced data logging applications.
  - Buy a complete FlexLogger license for your advanced data logging
 applications.
- Reduce disk space when logging by configuring your project to log at a lower rate.
 Use the Logging Specification to set trigger conditions and
 decrease the logging rate outside of events of interest.
- Define how you want to retain the SystemLink tags you publish from FlexLogger.

Related tasks:

- Publishing Data and Backup Files to a Remote SystemLink Server
- Enabling and Configuring Triggers for Data Logging

Related information:

- FlexLogger Editions

#### FlexLogger 2024 Q1 New Features and
 Changes

FlexLogger 2024 Q1 adds support for retrieving your FlexLogger version using the
 FlexLogger Python API.

- Use the FlexLogger Python API to programmatically get the version of FlexLogger you
 are using.

Related concepts:

- Automating FlexLogger Tests Using Python

#### FlexLogger 2023 Q4 New Features and
 Changes

FlexLogger 2023 Q4 adds a streamlined installation process, USB DAQ device
 simulation, support for triggering events with user input, and performance improvements for
 loading projects and Channel Specification sections.

- Install with less effort. FlexLogger offers streamlined installation so you do not
 have to make decisions about which additional software to install along with
 FlexLogger. You can still choose what to install by enabling Customize
 installation in NI Package manager.
- No hardware? No problem. Quickly add a simulated USB data acquisition device (DAQ)
 from FlexLogger so you can configure your project without hardware. Refer to
 How FlexLogger Connects to Your Hardware for more information.
- FlexLogger loads your projects faster. Notice up to 60% faster load times for
 high-channel-count projects that use formulas extensively.
- Trigger an event with the click of a button. Refer to Initiating an Action
 with a Button for more information.
- Define how FlexLogger displays the date and time on axes for time-series graphs,
 including the number of significant figures, so you can capture the precision of
 your time-series data. In your Screen document, click the time
 axis and modify the Display format settings in the
 Item configuration pane.
- FlexLogger preserves the layout of your Channel Specification so you see only the
 channels you want when you reopen a saved project.
- FlexLogger loads frequently viewed Channel Specification sections faster.
- Map multiple channels to a Frequency Spectrum graph. Refer to Visualizing Live
 Data with Indicators and Graphs for more information.
- More intuitive timing when logging your data. The toolbar timer and time-based
 triggers start when you click RUN .
- Add an Integral channel to your Channel Specification to
 calculate additional physical parameters for your system. For example, integrate
 your accelerometer data to get velocity and integrate velocity to get displacement
 over time.
- Support for USB-6008 and USB-6009 low-cost, multifunction DAQ devices. Refer to
 Supported Hardware for more information.
- Use the FlexLogger Python API to programmatically get and set trigger settings for
 your project.

Related concepts:

- How FlexLogger Connects to Your Hardware

Related tasks:

- Initiating an Action with a Button
- Visualizing Live Data with Indicators and Graphs

Related reference:

- FlexLogger Supported Hardware

#### FlexLogger 2023 Q3 New Features and
 Changes

FlexLogger 2023 Q3 includes new tools for graph data visualization and analysis, IEEE
 1588 TSN time synchronization for compatible CompactDAQ chassis, and expanded functionality
 for the FlexLogger PDK and FlexLogger Python API.

- FlexLogger now provides averaging on the undecimated data for high-speed graphs at
 any zoom level.
- FlexLogger no longer supports publishing or consuming data locally using the NI Web
 Server Configuration. Instead, publish FlexLogger data to LabVIEW using a remote
 SystemLink server. You can also automate FlexLogger using the FlexLogger Python API
 or design custom plug-ins for FlexLogger using the FlexLogger Plug-in Development
 Kit.
- Use the IEEE 1588 protocol to synchronize your time-sensitive networking
 (TSN)–enabled CompactDAQ chassis. In FlexLogger, navigate to File»Preferences»General , check Enable multi-chassis and network
 synchronization , and select 1588 .
- See a table with statistical information for all channels on a graph. On your
 Screen document, click a graph to open the
 Item configuration pane located on the right side of the
 window. In the Parts section, enable Statistics
 legend .
- Zoom in on all graphs simultaneously to get a closer look at your data. On your
 Screen document, click Pause all
 graphs 
 . Then, click Synchronize
 zoom of paused graphs 
 and zoom in on one graph.
 FlexLogger zooms in on the same interval of time on all graphs.
- Display strings published by plug-in channels you created with the FlexLogger
 Plug-in Development Kit and added to FlexLogger. In your FlexLogger
 Screen document, add a Text Box
 Indicator from the Text menu. Map the
 indicator to the plug-in string channel you want to see strings from.
- Support for LabVIEW 2023 in the FlexLogger Plug-in Development Kit 1.7.
- Use the FlexLogger Python API to programmatically register and handle alarms, log
 file events, and test session events. Log file events include creating and
 completing a log file and test session events include starting and stopping a
 test.
- Use the FlexLogger Python API to programmatically get the name of your FlexLogger
 project.

Related concepts:

- Automating FlexLogger Tests Using Python

Related tasks:

- Visualizing Live Data with Indicators and Graphs
- Publishing Data and Backup Files to a Remote SystemLink Server
- Adding a FlexLogger Plug-In Development Kit Plug-In to Your Project
- Using Network Synchronization in Your Project

#### FlexLogger 2023 Q2 New Features and
 Changes

FlexLogger 2023 Q2 includes support for configuring a sensor as a thermocouple CJC
 source, support for channel synchronization on multifunction I/O devices, and functionality
 expansions for the FlexLogger PDK, FlexLogger Python API, and Screen documents.

- Collect more accurate thermocouple measurements by using a sensor as your cold junction
 compensation (CJC) source instead of a constant value. In the thermocouple
 channel configuration dialog, set the CJC source to
 Sensor and map to another RTD or thermocouple
 channel in the same chassis to use as the CJC source.
- Synchronize digital lines in your 62xx multifunction I/O device with analog channels
 configured on the same device.
- Synchronize the onboard counters in your 62xx and 63xx multifunction I/O devices with
 analog channels configured on the same device.
- Configure FlexLogger to retry publishing files to SystemLink after restoring a lost
 connection.
- Send strings from third party devices to FlexLogger using the FlexLogger
 Plug-in Development Kit 1.6.
- Use the FlexLogger Python API to programmatically update the log file
 description and add or modify several test properties at once in your
 Logging Specification document.
- Halt or resume all graphs on your Screen document simultaneously by toggling
 Pause all graphs 
 .
- Avoid manual data entry when specifying multiple scaling factors for your
 channel. In the channel configuration, select Table 
 as the scaling type, copy two columns of space or tab separated values, and
 paste the values into the table.
- See the average value for a segment of data on a graph. In your Screen
 document, hover over the data to see statistical information.
- Configure your RMS and Mean channels to average all the data you collected
 for the channel since starting the test or opening a project.
- (Preview Feature) Reduce disk space when logging in FlexLogger by configuring your project
 to log at a low-fidelity rate. Use the Logging Specification to set trigger
 conditions and enable low-fidelity logging.

Related concepts:

- Automating FlexLogger Tests Using Python

Related tasks:

- Configuring Digital Lines in Your Channel Specification
- Configuring Counters in Your Channel Specification

Related information:

- FlexLogger Plug-in Development Kit

#### FlexLogger 2023 Q1 New Features and
 Changes

FlexLogger 2023 Q1 includes new hardware support, FlexLogger Python API updates, support
 for uploading renamed FlexLogger files directly to SystemLink, and support for LabVIEW 2022
 in the FlexLogger PDK.

- Support all 62xx multifunction I/O data acquisition devices: PCI, PCI
 Express (PCIe), PXI, PXI Express (PXIe), and USB. Refer to Supported
 Hardware for specific model support information.
- Support for PCIe 63xx multifunction I/O data acquisition devices. Refer to Supported
 Hardware for specific model support information.
- Use the FlexLogger Python API to programmatically configure the data acquisition rate of
 your channels.
- Use the FlexLogger Python API to programmatically save your FlexLogger projects.
- Upload data files you renamed in FlexLogger to SystemLink so you can keep
 track of project files across systems. Rename a data file in the FlexLogger
 Data tab. If you already published the file to
 SystemLink, FlexLogger launches the Rename dialog.
 Select Rename and upload file to upload the renamed
 file to SystemLink.
- Support for LabVIEW 2022 in the FlexLogger Plug-in Development Kit 1.5.

Related concepts:

- Using SystemLink to Share Data and Back Up Files
- Automating FlexLogger Tests Using Python

Related reference:

- FlexLogger Supported Hardware

Related information:

- FlexLogger Plug-in Development Kit

#### FlexLogger 2022 Q4 New Features and
 Changes

FlexLogger 2022 Q4 includes expanded SystemLink support, an option for hiding
 unconfigured channels, and support for copying and pasting formula-based calculated
 channels.

- Back up your FlexLogger data files to SystemLink Server or SystemLink Cloud without
 publishing test data as tags. Track the progress of your backup file uploads
 in the FlexLogger Data tab.
- See the connection status between FlexLogger and SystemLink on the toolbar of your Channel
 Specification.
- Show only configured channels so you can see your whole test system. In the Channel
 Specification, click Show configured channels 
 . FlexLogger hides all
 unconfigured channels and highlights the button to indicate that you have
 enabled the filter.
- Copy and paste formula-based calculated channels. Add and configure an arithmetic or
 Boolean formula channel in your Channel Specification. Right-click the
 channel to copy it. Paste the channel into an unconfigured or configured
 channel of the same type.

#### FlexLogger 2022 Q2 New Features and
 Changes

FlexLogger 2022 Q2 includes expanded ECU testing capabilities, adds support for
 disabling logging on specific channels, and allows you to scale values by directly mapping
 electrical values to physical units.

- Test ECUs using A2L databases that rely on the CAN Calibration Protocol (CCP).
- Set XNET output values outside of the minimum and maximum limits configured
 in your database so you can test the robustness of your ECUs.
- Deactivate logging on specific channels. In the Channel Specification, hover
 over a channel and click Disable logging ( ). FlexLogger will no longer
 bold this channel in the display.
- Scale the electrical values of a device to the physical units of a sensor using
 value-dependent scaling factors. Select Table as the
 scaling type and specify multiple electrical values and their corresponding
 physical values.

Related tasks:

- Configuring ECU Measurements
- Scaling Electrical Values to Physical Values

<!--NI_TOPIC bundle=flexlogger path=onboard-counters.html language=enus -->
## TOPIC 00068: Onboard Counters

- bundle_id: `flexlogger`
- source_path: `onboard-counters.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/onboard-counters.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactDAQ chassis and multifunction I/O devices have onboard counters that you can configure and use similarly to counter module channels. An onboard counter such as the NI-9361 appears as a module in FlexLogger but operates differently from a typical counter module. Introduced in FlexLogger 2020 R

### Onboard Counters

CompactDAQ chassis and multifunction I/O devices have onboard counters that you can
 configure and use similarly to counter module channels. An onboard counter such as the NI-9361
 appears as a module in FlexLogger but operates differently from a typical counter
 module.

Introduced in FlexLogger 2020 R4

When configuring and using onboard counters, keep in mind the following functionality:

- CompactDAQ chassis and multifunction I/O devices connect differently. You can use the
 available digital lines to connect to the onboard counter of multifunction I/O devices. To
 connect to the onboard counter of a CompactDAQ chassis, you must insert a supported digital
 C Series module into the chassis. For more information about supported digital modules,
 refer to Digital I/O Considerations for C Series and TestScale Devices in the
 NI-DAQmx User Manual .
- You must specify which digital line you want to use as the input terminal. You may have
 multiple options.
- Onboard counters can't create their own internal sample clock. FlexLogger uses the
 Frequency Output (FREQ OUT) signal to supply the clock source.
- Onboard counters have fixed sample rates but can sync to the data rate of an analog
 channel within the same chassis. Selecting Counter sets the onboard
 counter to use fixed data rates determined by the Frequency Output signal. The onboard
 counter can't synchronize with anything else on the board when you select
 Counter as the data rate. The Frequency Output signal only allows
 for data rates between 6.25 kHz and 20 MHz. Syncing to an analog channel in the same
 chassis allows the onboard counter to use the configured data rate level.
- You can configure onboard counters and counters on multifunction I/O devices to use the
 Slow , Medium , or
 Fast . You must first configure an analog input channel or digital
 channel in the same chassis to access these data rates.

For more information about onboard counters and the Frequency Output signal, refer to the
 device manuals for your cDAQ chassis or multifunction I/O devices. Navigate to Counters»Counter Timing Engine and Counters»Counter Output Applications»Frequency Generation.

Parent topic:

Configuring Counters in Your Channel Specification

Related information:

- Digital I/O Considerations for C Series and TestScale Devices - NI-DAQmx User
 Manual
- cDAQ Module Support for Accessing On-board Counters

<!--NI_TOPIC bundle=flexlogger path=physical-measurement-reference.html language=enus -->
## TOPIC 00069: Physical Measurement Type Reference

- bundle_id: `flexlogger`
- source_path: `physical-measurement-reference.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/physical-measurement-reference.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic lists the physical measurement types FlexLogger supports. The physical measurement types available in your system depend on your specific hardware configuration. 26 Physical Measurement Types Physical Measurement Type Compatible Sensors Description Voltage Voltage Find the difference of e

### Physical Measurement Type Reference

This topic lists the physical measurement types FlexLogger supports.

The physical measurement types available in your system depend on your specific hardware configuration.

| Physical Measurement Type | Compatible Sensors | Description |
| --- | --- | --- |
| Voltage | Voltage | Find the difference of electric potential between two points of a circuit, using a ground-referenced or differential reference point. |
| Current | Current Current Shunt Voltage | Find the flow rate of an electric charge in a circuit. |
| Temperature | Current RTD Thermocouple Voltage | The expression of cold and heat of an environment. |
| Pressure | Bridge Current Current Shunt Voltage | Measure the force applied to an area by a fluid |
| Force | Bridge Current Current Shunt Voltage IEPE | Determine the rate of acceleration or resistance on an object against another object. |
| Torque | Bridge Current Current Shunt Voltage | Determine the amount of force causing an object to rotate. |
| Strain | Bridge | Measure an object's tension or compression as expressed by small changes in resistance. |
| Acceleration | Current Voltage IEPE | Determine the change of the velocity of an object as demonstrated by static forces (gravity) or dynamic forces (vibrations and movement), with the accelerations conveyed as varying voltage or current levels. |
| Sound Pressure | Current Voltage IEPE | Measure the pressure difference of the ambient atmospheric pressure caused by a sound wave. |
| Linear Position | Current Voltage LVDT | Determine the linear movement of an object on a single plane as demonstrated by change in distance. |
| Linear Velocity | Current Voltage Encoder Frequency Counter IEPE | Measure the velocity of an object on a single plane over a time period. |
| Angular Position | Current Voltage RVDT | Determine the circular movement of a rotating object as demonstrated by change in rotational distance. |
| Angular Velocity | Current Voltage Encoder Frequency Counter | Measure the velocity of an object's circular rotation over time. |
| Frequency | Frequency Counter | Count the number of cycles that occur over a period of time, specifically waveform intervals. |
| Pulse | Pulse Counter | Count the number of amplitude changes (pulses) in the signal. |
| Pulse Width | Frequency Counter | The length of one cycle over a period of time, specifically a waveform interval. |
| Resistance | Resistance | Measure the opposition to passage of an electric current. |
| Custom | All | Configure a voltage, current, or bridge sensor using custom units. |

Parent topic:

Supported Sensor Class Types

<!--NI_TOPIC bundle=flexlogger path=publish-data-backup-files-remote-systemlink-server.html language=enus -->
## TOPIC 00070: Publishing Data and Backup Files to a Remote SystemLink Server

- bundle_id: `flexlogger`
- source_path: `publish-data-backup-files-remote-systemlink-server.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/publish-data-backup-files-remote-systemlink-server.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: To share data across your organization and back up your files, publish FlexLogger test data and files to your remote SystemLink server. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Before you begin, connect FlexLogger to

### Publishing Data and Backup Files to a Remote
 SystemLink Server

To share data across your organization and back up your files, publish FlexLogger
 test data and files to your remote SystemLink server.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more information.

Before you begin, connect FlexLogger
 to your remote SystemLink server.

1. In your configured FlexLogger project, navigate to Project»Settings.
2. Select SystemLink Server from the SystemLink
 deployment drop-down menu.
3. Optional: 
 To publish data as tags in real time, complete the following steps. 
 
 OptionDescriptionNone
 Do not keep the tags you publish.Duration
 Keep the tags you publish for a set amount of time. Specify the
 number of days in Retention
 duration.Count
 Keep a set number of the tags you publish.Specify the number in
 Retention count.Permanent
 Keep the tags you publish indefinitely. 
 Note When you change a tag
 retention setting in SystemLink, SystemLink does not transfer the change to
 FlexLogger. FlexLogger overrides the settings in SystemLink when you run a
 test.
  1. Enable Publish all input channels as tags while project is
 open.
  2. Specify how you want the tags retained in SystemLink. Select from the
 following options.
4. Optional: 
 To back up your logged data files to SystemLink, enable
 Automatically publish logged TDMS files. 
 You can also back up individual files after FlexLogger has created the files.
 In the Data tab, right-click the file and select Upload file to
 SystemLink.
5. Optional: 
 To automatically retry publishing files, enable Retry publishing
 files after restoring a lost connection. This option is only
 available if you have enabled Automatically publish logged TDMS
 files.
6. Click OK.

The FlexLogger toolbar shows the connection status between
 FlexLogger and SystemLink.

Data

Verifying Your Tag Data in Tags

Tip

Parent topic:

Using SystemLink to Share Data and Back Up Files

Related tasks:

- Connecting FlexLogger to a Remote SystemLink Server

Related information:

- Verifying Your Tag Data in Tags
- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=publish-data-to-labview.html language=enus -->
## TOPIC 00071: Publish Data to LabVIEW

- bundle_id: `flexlogger`
- source_path: `publish-data-to-labview.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/publish-data-to-labview.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Send data from FlexLogger to LabVIEW as SystemLink tags using a remote SystemLink Server. Introduced in FlexLogger 2023 Q3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Connect FlexLogger to a remote SystemLink Server. Ins

### Publish Data to LabVIEW

Send data from FlexLogger to LabVIEW as SystemLink tags using a remote SystemLink
 Server.

Introduced in FlexLogger 2023 Q3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Connect FlexLogger to a remote SystemLink Server.

1. Install 64-bit LabVIEW.
2. Install NI SystemLink Tag Support for LabVIEW.
  1. Open NI Package Manager and click Installed.
  2. Locate FlexLogger and click the Install or remove related
 packages gear.
  3. Select NI SystemLink Tag Support for LabVIEW
 <*version*> and click Next. 
 Note If you do not see NI SystemLink Tag Support for LabVIEW
 <*version*> listed, you automatically installed it
 with FlexLogger.
  4. Follow the instructions to complete installation.
3. Open the example LabVIEW project located at %Program Files%\National
 Instruments\FlexLogger <version>\Examples\SystemLink Integration\FlexLogger Tag
 Examples.lvproj. 
 This LabVIEW project contains the VI, Query and Display All FlexLogger
 Tags.vi, which allows you to read data in LabVIEW that you published from
 FlexLogger.

Parent topic:

Publishing Data and Backup Files to a Remote SystemLink Server

Related tasks:

- Connecting FlexLogger to a Remote SystemLink Server

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=publish-or-consume-data-locally.html language=enus -->
## TOPIC 00072: Publish or Consume Data Locally (Legacy)

- bundle_id: `flexlogger`
- source_path: `publish-or-consume-data-locally.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/publish-or-consume-data-locally.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the NI Web Server Configuration installed with FlexLogger to exchange test data locally between FlexLogger and Python or LabVIEW. Before you begin, create and configure a FlexLogger project. From the Windows Start menu, launch the NI Web Server Configuration. Select Simple local access and follo

### Publish or Consume Data Locally
 (Legacy)

Use the NI Web Server Configuration installed with FlexLogger to exchange test
 data locally between FlexLogger and Python or LabVIEW.

Before you begin, create and configure a FlexLogger
 project.

1. From the Windows Start menu, launch the NI Web Server Configuration.
2. Select Simple local access and follow the instructions
 to complete the setup.
3. In the Applications tab of the NI Web Server Configuration window, click the NI
 SystemLink URL to open the SystemLink web application.
4. In your configured FlexLogger project, navigate to Project»Settings.
5. Select Local from the SystemLink
 deployment drop-down menu.
6. To publish data, enable Publish all channels as tags while project
 is open.
7. To consume data, enable Import user-defined tags.
8. Click OK.

Tags

NI FlexLogger SystemLink
 Integration for Python Readme

Exchanging Data with LabVIEW

Parent topic:

Using SystemLink to Share Data and Back Up Files

Related tasks:

- Creating a New Project
- Exchanging Data with LabVIEW (Legacy)

Related information:

- FlexLogger SystemLink Integration for Python GitHub Repository
- NI Web Server

<!--NI_TOPIC bundle=flexlogger path=reducing-signal-noise.html language=enus -->
## TOPIC 00073: Reducing Signal Noise

- bundle_id: `flexlogger`
- source_path: `reducing-signal-noise.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/reducing-signal-noise.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure hardware filters and software filters in FlexLogger to reduce noise in your signals. FlexLogger supports both hardware filters and software filters for use in your project. Hardware filters offer antialiasing and noise reduction with no CPU usage or reduction in system performance. Hardwar

### Reducing Signal Noise

Configure hardware filters and software filters in FlexLogger to reduce noise in your
 signals.

FlexLogger supports both hardware filters and software filters
 for use in your project. Hardware filters offer antialiasing and noise reduction with no CPU
 usage or reduction in system performance. Hardware filters are only available on specific
 modules. Use software filters on all input channels of any hardware FlexLogger supports.
 Software filters require high CPU resource usage and also have higher latency.

#### Using Hardware Filters

FlexLogger applies the following hardware filters on supported devices. Refer to
 *Supported Hardware* for more information. Filter types vary depending on the
 module that you use.

1. Hover over the channel row to see the Configure gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. Select the gear for
 the channel you wish to configure the filter for.
2. From the Channel Configuration dialog, select the
 Filtering tab and choose from the following filter types. 
 Table 31.Lowpass FiltersFilter Type
 Description
 Notes
 Supported DevicesBrickwall
 Best antialiasing.
 FlexLogger automatically configures the filter to a cutoff frequency of
 half the data rate.
 All FlexLogger-supported devices
 Butterworth
 Better noise rejection, configurable filter order (2nd or 4th
 order).
 FlexLogger selects the default cutoff frequency that 's based on the timing
 configuration and selected cutoff band. FlexLogger applies changes to the
 cutoff settings to all module channels. Changes may affect other timing
 configurations on the module.
 All FieldDAQ devices.
 Better noise rejection.
 FlexLogger uses the highest cutoff frequency as the default.
 NI-9252/9253, NI-9326, PXIe-4300/4310
 Elliptical
 Better noise rejection.
 FlexLogger uses the highest cutoff frequency as the default.
 PXIe-4302/4303/4304/4305
 Digital Glitch
 Configurable input filter.
 FlexLogger rejects pulses shorter than the specified Pulse Width Cutoff.
 NI-9326, NI-9361
 Note For C Series and FieldDAQ devices,
 the system applies any changes you make to the filter configuration settings (if
 available) to all module channels.
 FlexLogger applies the lowpass filter when you select Filter
 Type or adjust the filter configuration, if available.
 Table 32.ADC Timing Mode-Based
 FiltersFilter Mode
 DescriptionAuto
 FlexLogger uses the highest resolution filter that's valid for the
 configured data rate.
 None (High Speed)
 The best sample rate and signal bandwidth, lower accuracy and noise
 rejection. This mode is the default filter applied to the channel.
 High Resolution
 The best accuracy and the best noise rejection. Rejects power line
 frequencies, and offers higher conversion time and lower signal
 bandwidth.
 Medium Resolution
 Better accuracy and noise rejection. Rejects power line frequencies, and
 offers higher conversion time and lower signal bandwidth.
 Medium Speed
 Better sample rate and signal bandwidth, lower accuracy and noise
 rejection.
 Variable Timing Modes
 Selectable timing modes ranging from High Resolution to High Speed, allowing
 for incremental selection of noise and accuracy ratios.
 Available on the PXIe-4353/PXIe-4357.
 (PXIe-4353): Timing mode 1 (High Resolution) to
 timing mode 7 (High Speed).
 (PXIe-4357): Timing mode 1 (High Resolution) to
 timing mode 9 (High Speed).
 Refer to the hardware documentation for additional ADC timing mode
 information on these modules, such as corresponding data rates and ADC
 conversion time.
 Best 50 Hz Rejection
 Optimizes 50 Hz noise rejection.
 Best 60 Hz Rejection
 Optimizes 60 Hz noise rejection.

FlexLogger applies the ADC timing mode filter when you select Filter
 Mode or adjust the filter configuration, if options are available.

#### Using a Software Filter

Refer to *Configuring Lowpass/Highpass Filter Channels* for information on
 creating and configuring a software-based Butterworth filter channel.

Parent topic:

Configuring I/O Channels

Related tasks:

- Configuring Lowpass/Highpass Filter Channels

Related reference:

- FlexLogger Supported Hardware

<!--NI_TOPIC bundle=flexlogger path=running-a-test.html language=enus -->
## TOPIC 00074: Running a Test

- bundle_id: `flexlogger`
- source_path: `running-a-test.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/running-a-test.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use your configured FlexLogger project to run tests and log data. Before you begin, configure your hardware device channels and test configuration. Click RUN to run a test and start logging data. FlexLogger starts logging your test data based on your data logging configuration. All channels are logg

### Running a Test

Use your configured FlexLogger project to run tests and log data.

Before you begin, configure your hardware
 device channels and test configuration.

1. Click RUN to run a test and start logging data. 
 FlexLogger starts logging your test data based on your data logging
 configuration.

Note

1. To pause a running test, click Pause test ([IMAGE alt='image' src='GUID-BF8B1715-A3B1-447A-BC34-4F0E2F08DD31-a5.png']). 
 When you pause a test, you temporarily suspend data logging, data logging
 triggers, and time-based events.

Note

Adding an
 Event

1. To resume a paused test, click Resume test.
2. To stop a running test, click STOP.

Data

Data

Related tasks:

- Configuring Device Channels
- Defining Your Test Configuration
- Adding an Event

<!--NI_TOPIC bundle=flexlogger path=scaling-electrical-values.html language=enus -->
## TOPIC 00075: Scaling Electrical Values to Physical Values

- bundle_id: `flexlogger`
- source_path: `scaling-electrical-values.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/scaling-electrical-values.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Scale the electrical values of a device to the physical units of a sensor. Open your Channel Specification and complete the following steps to apply scaling to your configured sensor. On the channel you want to scale, click the Configure gear (). Select the scaling type in the Scaling section of the

### Scaling Electrical Values to Physical Values

Scale the electrical values of a device to the physical units of a sensor.

Open your Channel Specification and
 complete the following steps to apply scaling to your configured sensor.

1. On the channel you want to scale, click the Configure gear
 ([IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']).
2. Select the scaling type in the Scaling section of the channel
 configuration dialog box. 
 Table 29.Options for Scaling Electrical
 Values to Physical ValuesDevice Type
 Scale Type
 DescriptionAnalog input
 Linear
 Scale the electrical values (x) to the physical values
 (y) linearly using the equation below, where
 m is the Slope and
 b is the Offset. y
 =
 m
 x
 +
 b
 Sensitivity
 Scale the electrical values (x) to the physical values
 (y) linearly using the equation below, where
 m is the Sensitivity and
 b is the Offset. y
 =
 x
 m
 +
 b
 Dynamic Sensitivity
 Scale the electrical values (x) to the physical values
 (y) linearly using the equation below, where
 m is the Sensitivityy
 =
 x
 m
 Table
 Scale the electrical values to the physical values using multiple
 electrical values and their corresponding physical values. Table scaling uses
 the formula below to calculate the slope (gain) and the intercept to calculate
 the offset for each consecutive set of values. (
 Physical Value b
 −
 Physical Value a
 )
 (
 Electrical Value b
 −
 Electrical Value a
 )
 Two Point
 Scale the electrical values to the physical values using the minimum and
 maximum expected electrical values and their corresponding physical values.
 Two-point scaling uses the formula below to calculate the slope (gain), and uses
 the intercept to calculate the offset. (
 Physical Value 2
 −
 Physical Value 1
 )
 (
 Electrical Value 2
 −
 Electrical Value 1
 )Electrical values are set using an immediate
 averaging of the signal reading when the From Average
 button is clicked. The chosen data rate determines the number of samples
 averaged.Data Rate
 Sample(s) Averaged<1 Hz
 Most recently read sample
 1 Hz–10 Hz
 Two samples after button clicked
 >20 Hz
 100 ms of samples after button clicked
 Strain
 Adjust the Gage Factor and Gage Type to specify sensitivity and strain gage
 configuration.
 Counter
 Angular Position Encoder
 Set the number of pulses per revolution and initial angle of the encoder.
 Initial Angle is the value the counter resets to when
 Restart All Counters is clicked during channel
 configuration.
 Linear
 Apply a linear scaling to the counter using slope. For Slope, scale your
 signal linearly by using the equation below, where m is the
 Slope and b is the
 Offset. y
 =
 m
 x
 +
 b
 Linear Position Encoder
 Set the distance per pulse and initial position of the encoder.
 Initial Position is the value the counter resets to
 when Restart All Counters is clicked during channel
 configuration.
 Pulse Counter
 Set the initial value of pulses. Initial Value is
 the value the counter resets to when Restart All Counters
 is clicked during channel configuration.
 Pulse Encoder
 Set the number of pulses per revolution of the encoder.
 Digital input
 Invert Line
 Invert the line in the channel. If applied, the line is at high logic when
 off and low logic when on.

Parent topic:

Configuring I/O Channels

<!--NI_TOPIC bundle=flexlogger path=selecting-strain-gage.html language=enus -->
## TOPIC 00076: Selecting a Strain Gage

- bundle_id: `flexlogger`
- source_path: `selecting-strain-gage.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/selecting-strain-gage.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Select a strain gage that meets the needs of your system and application. Hover over the channel row to see the Configure gear . Click the gear for the channel you wish to add a strain gage to. Select the desired Bridge Configuration. Specify the Bridge Resistance (if available), the Excitation Sour

### Selecting a Strain Gage

Select a strain gage that meets the needs of your system and application.

1. Hover over the channel row to see the Configure gear
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png']. Click the gear for the
 channel you wish to add a strain gage to.
2. Select the desired Bridge Configuration.
3. Specify the Bridge Resistance (if available), the
 Excitation Source, Excitation
 Value, Bridge Offset, and
 Scaling options for your strain gage.
4. In the Scaling section of the channel configuration dialog, select the desired
 Gage Type and additional gage characteristics as
 needed.

Use the following table to determine which strain-gage configuration your application
 requires.

| Bridge Configuration | Gage Type | Configuration Type |
| --- | --- | --- |
| Quarter Bridge | Single Element | Configuration Type I Measures axial or bending strain Requires a passive quarter-bridge completion resistor (known as a dummy resistor) Requires half-bridge completion resistors to complete the Wheatstone bridge R4 is an active strain gage measuring the tensile strain (+ε) Figure 1. Quarter-Bridge Strain Gage Configuration I |
| Half Bridge | Two Poisson Elements | Configuration Type I Measures axial or bending strain Requires half-bridge completion resistors to complete the Wheatstone bridge R4 is an active strain gage measuring the tensile strain (+ε) R3 is an active strain gage compensating for Poisson’s effect (-νε) Figure 2. Half-Bridge Strain Gage Configuration I |
| Half Bridge | Two Elements Opposite Sign | Configuration Type II Measures bending strain only Requires half-bridge completion resistors to complete the Wheatstone bridge R4 is an active strain gage measuring the tensile strain (+ε) R3 is an active strain gage measuring the compressive strain (-ε) Figure 3. Half-Bridge Strain Gage Configuration II |
| Half Bridge | Two Element Chevron | Chevron is typically for torque measurements. The two elements are at a 90 degree angle to each other to create a chevron shape (V-shaped). |
| Full Bridge | Four Element Poisson Same Sign | Configuration Type III Measures axial strain R1 and R3 are active strain gages measuring the compressive Poisson effect (–νε) R2 and R4 are active strain gages measuring the tensile strain (+ε) Figure 4. Full-Bridge Strain Gage Configuration III |
| Full Bridge | Four Element Poisson Opposite Sign | Configuration Type IISensitive to bending strain onlyR1 is an active strain gage measuring the compressive Poisson effect (–νε)R2 is an active strain gage measuring the tensile Poisson effect (+νε)R3 is an active strain gage measuring the compressive strain (–ε)R4 is an active strain gage measuring the tensile strain (+ε) Figure 5. Full-Bridge Strain Gage Configuration II |
| Full Bridge | Four Element Uniaxial | Configuration Type I Highly sensitive to bending strain only R1 and R3 are active strain gages measuring compressive strain (–ε) R2 and R4 are active strain gages measuring tensile strain (+ε) Figure 6. Full-Bridge Strain Gage Configuration I |
| Full Bridge | Four Element Dual Chevron | Chevron is typically for torque measurements. The two elements are at a 90 degree angle to each other to create a chevron shape (V shaped), twice. |

Parent topic:

Configuring I/O Channels

<!--NI_TOPIC bundle=flexlogger path=sensor-class-reference.html language=enus -->
## TOPIC 00077: Sensor Class Reference

- bundle_id: `flexlogger`
- source_path: `sensor-class-reference.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/sensor-class-reference.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn more about the available sensor class types. FlexLogger supports the following sensors. The sensor classes available in your system depend on your specific hardware configuration and the type of physical measurement you are acquiring. For descriptions and additional information of the supporte

### Sensor Class Reference

Learn more about the available sensor class types.

FlexLogger supports the following sensors. The sensor classes available in your system depend on your specific hardware configuration and the type of physical measurement you are acquiring.

For descriptions and additional information of the supported physical measurements, refer
 to the *Physical Measurement Type Reference*.

| Sensor Class | Description |
| --- | --- |
| Voltage | Determines the electrical potential difference between two points on a circuit. |
| Current | Determines the current in a circuit and generates a voltage or current reading proportional to the detected current. |
| Current Shunt | Measures current by determining the voltage drop across a low-resistance precision resistor. |
| Bridge | Bridge sensors operate by correlating a physical phenomena, such as strain, temperature, or force, to a change in resistance in one or more legs of a Wheatstone bridge. The general Wheatstone bridge is a network of four resistive legs with an excitation voltage (VEX) that is applied across the bridge. One or more of these legs can be active sensing elements. |
| IEPE | Integrated Electronics Piezoelectric (IEPE) transducer that is packaged with a built-in amplifier. Because the charge produced by some sensors is very small, the electrical signal produced by the transducer is susceptible to noise, and sensitive electronics must be used to amplify and condition the signal. An IEPE sensor integrates the sensitive electronics as close as possible to the transducer to ensure better noise immunity and convenient packaging. These sensors require a 4-20 mA current excitation to operate. |
| Thermocouple | Uses the temperature-dependent voltage produced at the junction of two dissimilar metals to measure temperature. This voltage is nonlinear with respect to temperature so thermocouples require signal conditioning. |
| Pulse Counter | Measures the number of non-zero inputs (pulses) in the signal over a specified time. |
| Encoder | (Angle) Measures 360-degree angular rotation using A, B and Z signals to determine position and direction. The signal can be only digital. (Linear) Measures displacement with any number of pulses per millimeter. |
| RTD | Temperature-sensing device with resistance that increases with temperature. An RTD is usually constructed with wire coil or deposited film of pure metal. RTDs can be made of different metals and have different nominal resistances, but the most popular RTD is platinum and has a nominal resistance of 100 Ω at 0 °C. |
| Frequency Counter | Measures the number of pulses of a periodic signal over a specified time. |
| LVDT | Determines linear displacement by converting the measurement of movement along a linear axis into an AC electrical signal. For information on wiring your LVDT sensor, refer to the Connecting LVDT and RVDT Signals section of the NI PXIe-4340 User Manual. |
| RVDT | Determines angular displacement by converting the measurement of movement along a rotational axis into an AC electrical signal. For information on wiring your RVDT sensor, refer to the Connecting LVDT and RVDT Signals section of the NI PXIe-4340 User Manual. |
| Resistance | Determines resistance by sending a current through a resistor and measuring the voltage drop from the signal before and after it crosses the resistor. |

Parent topic:

Supported Sensor Class Types

Related reference:

- Physical Measurement Type Reference

<!--NI_TOPIC bundle=flexlogger path=setting-graph-history-length.html language=enus -->
## TOPIC 00078: Setting the Graph History Length

- bundle_id: `flexlogger`
- source_path: `setting-graph-history-length.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/setting-graph-history-length.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the amount of data you can pause and view in graphs by specifying the history length. Use these methods to set the history length for graphs that support hold and pan viewing control. 50 Options for Setting the Graph History Length Set the Default History Length Determines the history length for

### Setting the Graph History Length

Set the amount of data you can pause and view in graphs by specifying the history
 length.

Use these methods to set the history length for graphs that support hold and pan viewing
 control.

| Set the Default History Length | Determines the history length for your graphs in all new projects. Go to File » Preferences and specify the history length for your graph type on the Project Defaults tab. |
| --- | --- |
| Set Project-Level History Length | Overrides the default graph history length for this project. In an open project, go Project » Settings and specify the history length for your graph type. |

Parent topic:

Visualizing Live Data with Indicators and Graphs

<!--NI_TOPIC bundle=flexlogger path=setting-output-reset-values.html language=enus -->
## TOPIC 00079: Setting Output Reset Values

- bundle_id: `flexlogger`
- source_path: `setting-output-reset-values.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/setting-output-reset-values.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Reset Value to return your output channel to a known value. Introduced in FlexLogger 2019 R3 You can set output channels to their reset value by creating an event and using the Reset output channels action. Hover over a channel row and click the Configure gear for the channel you wish to ena

### Setting Output Reset Values

Use the Reset Value to return your output channel to a known
 value.

Introduced in FlexLogger 2019 R3

You can set output channels to their reset value by creating an event and using the
 Reset output channels action.

1. Hover over a channel row and click the Configure gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] for the channel you wish to enable reset
 values on.
2. Select Enabled from the Channel Reset
 drop-down menu and specify the channel reset Value. 
 The reset value cannot exceed the maximum output range of your device. Refer to the
 device specifications on ni.com/docs for more information. Any
 channel reset Value set outside of device limits will be coerced
 to be within the maximum output range. When pasting a channel with Channel
 Reset enabled, the newly configured channel will automatically be set to
 the channel reset Value.
 Note You cannot set output reset values
 if you map your output channel to an input channel.

The output channel will automatically return to the specified channel reset
 Value if the channel is deleted, disabled or reassigned. The
 channel will also return to this value when the project is opened or closed.

Parent topic:

Configuring Analog Output in Your Channel Specification

<!--NI_TOPIC bundle=flexlogger path=shunt-calibrating-channels.html language=enus -->
## TOPIC 00080: Shunt Calibrating One or More Channels

- bundle_id: `flexlogger`
- source_path: `shunt-calibrating-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/shunt-calibrating-channels.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Apply shunt calibration to one or multiple bridge circuit channels simultaneously. Introduced in FlexLogger 2020 R2 Use shunt calibration to adjust for errors on your bridge circuits caused by resistance of the lead wires between the EX pins on the device and the strain gage. You must properly confi

### Shunt Calibrating One or More
 Channels

Apply shunt calibration to one or multiple bridge circuit channels simultaneously.

Introduced in FlexLogger 2020 R2

Use shunt calibration to adjust for errors on your bridge circuits caused by
 resistance of the lead wires between the EX pins on the device and the strain
 gage.

You must properly configure channels that support strain/bridge measurements to use shunt
 calibration. Specify Bridge Configuration and Bridge
 Resistance for any channels you want to perform a shunt calibration on. Refer
 to the supported hardware to confirm that your device supports strain/bridge
 measurements.

1. In your Channel Specification document, select all configured strain channels
 you want to calibrate.
2. In your Channel Specification document toolbar, click the Calibrate
 channels button [IMAGE alt='image' src='GUID-22C25013-8604-470C-833E-582156DD9C00-a5.png'].
3. Select the Shunt calibrate option.
4. Specify the shunt calibration parameters. 
 Table 30.Shunt Calibration ParametersParameter
 DescriptionSource
 Built-in—Use the internal shunt resistor of the
 module
 User-provided—Use an external shunt resistor
 Accessory—Use the internal shunt resistor of a
 connected accessory
 Location
 Specify the location of the shunt resistor on the bridge sensor.[IMAGE alt='image' src='GUID-7A145E90-37B6-4ACF-8802-06A60A34F41C-a5.svg']R1—Between V<sub>CH-</sub> and V<sub>EX+</sub>
 R2—Between V<sub>CH-</sub> and V<sub>EX-</sub>
 R3—Between V<sub>CH+</sub> and V<sub>EX-</sub>
 R4—Between V<sub>CH+</sub> and V<sub>EX+</sub>
 Value
 Specify the value of the resistor you are using. If you are using the
 Built-in option, refer to your device documentation for
 this value.
5. Click Calculate. Configure the channels and ensure they
 are not disabled or contain errors. You cannot perform shunt calibration on
 channels with errors. 
 The details of each channel update to display the calculated shunt gain adjustment
 value after you perform a calculation. If the calculated value is outside the valid
 range (0.5, 1.5), the channel fails the calculation. If any channels fail shunt
 calculation, the calibration toolbar displays an error icon along with the number of
 failed channels. Each failed channel displays an error in the Channel Specification
 document.
6. Resolve any shunt calibration errors. 
 A channel can receive an invalid calculated shunt gain adjustment value for
 following reasons:
 The channel received one or more unsupported shunt configuration
 parameters.
 An issue exists on the sensor, such as physical damage or data
 corruption.
 The sensor was disturbed or not at rest during calibration.
7. After resolving errors, select the affected channels and click
 Calculate to calculate a new shunt gain adjustment value. If the
 new calculated value is within the valid range, the error on the channel is cleared. 
 Note 
 You can clear shunt calibration errors If you cannot or do not want to fix the
 errors. You can clear shunt calibration errors in one of the following ways:
 Close the calibration toolbar. Uncalibrated channels retain their previous
 values.
 Choose a different calibration type, Null offset or
 Zero.
8. Click Apply all. 
 All channels with a valid calculated shunt gain adjustment value apply
 the value, completing the shunt calibration. The details of each channel update
 to display the applied value and a timestamp of when the value was applied. If
 no channels with an invalid calculated value remain, the calibration toolbar
 dismisses itself.
9. After the calibration toolbar dismisses, hover over the calibration icon [IMAGE alt='image' src='GUID-22C25013-8604-470C-833E-582156DD9C00-a5.png'] on
 any calibrated channel to see the values from the last calibration
 performed. 
 [IMAGE alt='image' src='GUID-4D131B90-EB29-464D-B96F-84F98B831D98-a5.png']

Parent topic:

Calibrating Multiple Channels Simultaneously

<!--NI_TOPIC bundle=flexlogger path=spreadsheet-importer-cmd.html language=enus -->
## TOPIC 00081: Using the Spreadsheet Importer Through the Command Line

- bundle_id: `flexlogger`
- source_path: `spreadsheet-importer-cmd.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/spreadsheet-importer-cmd.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the command line to create a FlexLogger project using the Spreadsheet Importer without needing to launch FlexLogger. Open a command prompt, terminal, or PowerShell window. Enter cd "C:\Program Files\National Instruments\FlexLogger\" to navigate to your FlexLogger installation location. Run ./fle

### Using the Spreadsheet Importer Through the
 Command Line

Use the command line to create a FlexLogger project using the Spreadsheet Importer
 without needing to launch FlexLogger.

1. Open a command prompt, terminal, or PowerShell window.
2. Enter cd "C:\Program Files\National Instruments\FlexLogger\"
 to navigate to your FlexLogger installation location.
3. Run ./flexloggercli.exe import with the following arguments to
 create your project. 
 Table 22.Spreadsheet Importer Command Line OptionsArgument
 Description-s
 Specifies the file path of your source
 spreadsheet.
 -f
 Specifies the file path the Spreadsheet Importer saves
 the project to.
 -p
 Specifies the project name.
 -o
 Optional argument that overwrites any existing projects
 with the same name at your specified path.

```text
./flexloggercli.exe import -s "C:\Users\nitest\Desktop\MySetup.xlsx" -f "C:\Users\nitest\Desktop" -p "MyProject" -o
```

The
 Spreadsheet Importer creates a project named MyProject.flxproj
 at
 C:\Users\nitest\Desktop\MyProject\MyProject.flxproj.

Parent topic:

Creating a Project Using the Spreadsheet Importer

<!--NI_TOPIC bundle=flexlogger path=spreadsheet-importer-flexlogger.html language=enus -->
## TOPIC 00082: Using the Spreadsheet Importer Through FlexLogger

- bundle_id: `flexlogger`
- source_path: `spreadsheet-importer-flexlogger.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/spreadsheet-importer-flexlogger.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Spreadsheet Importer UI in FlexLogger to easily create a FlexLogger project based on a source Excel spreadsheet. Navigate to File Create project from spreadsheet to open the Create Project from Spreadsheet window. Select your spreadsheet file location and project save location using the appr

### Using the Spreadsheet Importer Through
 FlexLogger

Use the Spreadsheet Importer UI in FlexLogger to easily create a FlexLogger project based
 on a source Excel spreadsheet.

1. Navigate to File»Create project from
 spreadsheet to open the Create Project from
 Spreadsheet window.
2. Select your spreadsheet file location and project save location
 using the appropriate file selection controls.
3. Enter your project name in the Project
 Name field.
4. Select Create project to create your
 project.

Show warnings

Show errors

Project Creation
 Results

Errors and
 Warnings from Project Creation

Open imported spreadsheet

Parent topic:

Creating a Project Using the Spreadsheet Importer

<!--NI_TOPIC bundle=flexlogger path=supported-hardware.html language=enus -->
## TOPIC 00083: FlexLogger Supported Hardware

- bundle_id: `flexlogger`
- source_path: `supported-hardware.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/supported-hardware.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: FlexLogger supports a number of NI devices. You can use supported hardware in FlexLogger without a network connection. CompactDAQ Chassis Consult the following table for information on CompactDAQ chassis supported by FlexLogger. 2 CompactDAQ Chassis Supported by FlexLogger Model Name Earliest Versio

### FlexLogger
 Supported Hardware

FlexLogger supports a number of NI devices.

Note

#### CompactDAQ Chassis

Consult the following table for information on CompactDAQ chassis supported by
 FlexLogger.

| Model Name | Earliest Version with Support | Notes |
| --- | --- | --- |
| cDAQ-9170 | 2025 Q1 | — |
| cDAQ-9171 | 2018 R2 | — |
| cDAQ-9173 | 2025 Q1 | — |
| cDAQ-9174 | 2018 R2 | — |
| cDAQ-9177 | 2025 Q1 | — |
| cDAQ-9178 | 2018 R2 | — |
| cDAQ-9179 | 2018 R2 | — |
| cDAQ-9181 | 2018 R2 | — |
| cDAQ-9183 | 2025 Q1 | This chassis supports network synchronization. Refer to Using Network Synchronization in Your Project for more information. |
| cDAQ-9184 | 2018 R2 | — |
| cDAQ-9185 | 2018 R2 | This chassis supports network synchronization. Refer to Using Network Synchronization in Your Project for more information. |
| cDAQ-9187 | 2025 Q1 | This chassis supports network synchronization. Refer to Using Network Synchronization in Your Project for more information. |
| cDAQ-9188 | 2018 R2 | — |
| cDAQ-9188XT | 2019 R1 | — |
| cDAQ-9189 | 2018 R2 | This chassis supports network synchronization. Refer to Using Network Synchronization in Your Project for more information. |
| cDAQ-9191 | 2018 R2 | — |

Related tasks:

- Using Network Synchronization in Your Project

#### C Series Modules

Consult the following table for information on C Series modules supported by
 FlexLogger.

| NI Product | Model Name | Earliest Version with Support | Notes |
| --- | --- | --- | --- |
| C Series Voltage Input Modules | NI-9201 | 2018 R2 | — |
| NI-9202 | 2019 R1 | — |  |
| NI-9204 | 2025 Q1 | — |  |
| NI-9205 | 2018 R2 | — |  |
| NI-9206 | 2018 R2 | — |  |
| NI-9209 | 2018 R2 | — |  |
| NI-9215 | 2018 R2 | — |  |
| NI-9220 | 2018 R2 | — |  |
| NI-9221 | 2018 R2 | — |  |
| NI-9222 | 2018 R2 | — |  |
| NI-9222 (Snap-In) | 2025 Q1 | — |  |
| NI-9223 | 2018 R2 | — |  |
| NI-9223 (Snap-In) | 2025 Q1 | — |  |
| NI-9224 | 2018 R3 | — |  |
| NI-9225 | 2018 R2 | — |  |
| NI-9225 (Snap-In) | 2025 Q1 | — |  |
| NI-9228 | 2018 R3 | — |  |
| NI-9229 | 2018 R2 | — |  |
| NI-9229 (Snap-In) | 2025 Q1 | — |  |
| NI-9238 | 2018 R2 | — |  |
| NI-9238 (Snap-In) | 2025 Q1 | — |  |
| NI-9239 | 2018 R2 | — |  |
| NI-9239 (Snap-In) | 2025 Q1 | — |  |
| NI-9242 | 2018 R3 | — |  |
| NI-9244 | 2018 R3 | — |  |
| NI-9251 | 2018 R3 | — |  |
| NI-9252 | 2019 R4 | This module supports hardware filtering. Refer to Reducing Signal Noise for more information. |  |
| NI-9320 | 2025 Q4 | — |  |
| C Series Voltage Output Modules | NI-9262 | 2018 R4 | — |
| NI-9263 | 2018 R4 | — |  |
| NI-9264 | 2018 R4 | — |  |
| NI-9269 | 2018 R4 | — |  |
| NI-9269 (Snap-In) | 2025 Q1 | — |  |
| C Series Current Input Modules | NI-9203 | 2018 R2 | — |
| NI-9208 | 2018 R2 | — |  |
| NI-9227 | 2018 R2 | — |  |
| NI-9227 (Snap-In) | 2025 Q1 | — |  |
| NI-9246 | 2018 R3 | — |  |
| NI-9247 | 2018 R3 | — |  |
| NI-9253 | 2019 R4 | This module supports hardware filtering. Refer to Reducing Signal Noise for more information. |  |
| C Series Current Output Modules | NI-9265 | 2018 R4 | — |
| NI-9266 | 2018 R4 | — |  |
| C Series Voltage and Current Input Module | NI-9207 | 2018 R3 | — |
| C Series Sound and Vibration Input Modules | NI-9230 | 2018 R2 | — |
| NI-9230 (Snap-In) | 2025 Q1 | — |  |
| NI-9231 | 2019 R1 | — |  |
| NI-9232 | 2018 R2 | — |  |
| NI-9232 (Snap-In) | 2025 Q1 | — |  |
| NI-9234 | 2018 R2 | — |  |
| NI-9250 | 2018 R2 | — |  |
| C Series Temperature Input Modules | NI-9210 | 2018 R3 | These modules support auto zero. Refer to the device documentation, available at ni.com/docs, for additional information. |
| NI-9211 | 2018 R2 |  |  |
| NI-9212 | 2018 R3 | — |  |
| NI-9213 | 2018 R2 | These modules support auto zero. Refer to the device documentation, available at ni.com/docs, for additional information. |  |
| NI-9214 | 2018 R3 |  |  |
| NI-9216 | 2018 R3 | FlexLogger supports resistance measurements for these modules. |  |
| NI-9217 | 2018 R3 |  |  |
| NI-9226 | 2018 R3 |  |  |
| C Series Universal Analog Input Modules | NI-9218 | 2018 R2 | You must configure all connectivity accessories in the Hardware Configuration Utility so they appear in your FlexLogger project. |
| NI-9219 | 2018 R2 | FlexLogger supports resistance measurements for this module. |  |
| C Series Strain/Bridge Input Modules | NI-9235 | 2018 R2 | — |
| NI-9236 | 2018 R2 | — |  |
| NI-9237 | 2018 R2 | — |  |
| C Series Frequency Input Module | NI-9326 | 2021 R2 | This module supports hardware filtering. Refer to Reducing Signal Noise for more information. FlexLogger supports input voltage threshold and hysteresis for this model. |
| C Series Counter Input Module | NI-9361 | 2018 R3 | FlexLogger supports pull-up resistor functionality and input voltage threshold for this module. |
| C Series Digital Modules (serial digital I/O) | NI-9375 | 2018 R4 | These modules can only use one port (input or output) at a time in a project. You cannot use parallel and serial modules on the same FlexLogger project unless they are installed in separate CompactDAQ chassis. |
| NI-9403 | 2018 R4 |  |  |
| NI-9425 | 2018 R4 |  |  |
| NI-9426 | 2018 R4 |  |  |
| NI-9476 | 2018 R4 |  |  |
| NI-9477 | 2018 R4 |  |  |
| NI-9478 | 2018 R4 |  |  |
| C Series Digital Modules (parallel digital I/O) | NI-9344 | 2018 R4 | You cannot use parallel and serial modules on the same FlexLogger project unless they are installed in separate CompactDAQ chassis. |
| NI-9401 | 2018 R4 |  |  |
| NI-9402 | 2018 R4 |  |  |
| NI-9411 | 2018 R4 |  |  |
| NI-9421 | 2018 R4 |  |  |
| NI-9422 | 2018 R4 |  |  |
| NI-9423 | 2018 R4 |  |  |
| NI-9435 | 2018 R4 |  |  |
| NI-9436 | 2018 R4 |  |  |
| NI-9437 | 2018 R4 |  |  |
| NI-9472 | 2018 R4 |  |  |
| NI-9474 | 2018 R4 |  |  |
| NI-9475 | 2018 R4 |  |  |
| NI-9481 | 2018 R4 |  |  |
| NI-9482 | 2018 R4 |  |  |
| NI-9485 | 2018 R4 |  |  |
| C Series CAN and Vehicle Multiprotocol Interface Modules | NI-9860 | 2018 R2 | FlexLogger supports all compatible transceiver cables for this module (TRC-8542, TRC-8543, and TRC-8546). |
| NI-9861 | 2018 R2 | — |  |
| NI-9862 | 2018 R2 | — |  |
| C Series LIN Interface Module | NI-9866 | 2019 R2 | — |

Related tasks:

- Reducing Signal Noise

#### FieldDAQ Devices

Consult the following table for information on FieldDAQ devices supported by
 FlexLogger.

Using Network Synchronization in Your Project

Except where noted, FieldDAQ devices support hardware filtering. Refer to
 *Reducing Signal Noise* for more information.

| NI Product | Model Name | Earliest Version with Support | Notes |
| --- | --- | --- | --- |
| Voltage Input Devices for FieldDAQ | FD-11601 | 2019 R1 | FlexLogger supports external powered sensor configuration. |
| FD-11603 | 2018 R3 | Revision B and later of this module support hardware filtering. Refer to Reducing Signal Noise for more information. |  |
| FD-11605 | 2019 R3 | — |  |
| Sound and Vibration Input Devices for FieldDAQ | FD-11634 | 2019 R2 | — |
| Strain/Bridge Input Devices for FieldDAQ | FD-11637 | 2018 R3 | Revision B and later of this module support hardware filtering. Refer to Reducing Signal Noise for more information. |
| Temperature Input Devices for FieldDAQ | FD-11613 | 2018 R3 | — |
| FD-11614 | 2019 R1 | — |  |

Related tasks:

- Reducing Signal Noise

#### PCI Devices

Consult the following table for information on PCI devices supported by
 FlexLogger.

| NI Product | Model Name | Compatible Accessories | Earliest Version with Support | Notes |
| --- | --- | --- | --- | --- |
| 62xx Multifunction I/O Devices | PCI-6220 | For information on compatible accessories, refer to 62xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | For digital lines, FlexLogger supports the 10 Hz data rate and synchronization with analog channels configured on the same device.FlexLogger does not support synchronization between multiple PCI 62xx devices. |
| PCI-6221 | 2023 Q1 |  |  |  |
| PCI-6224 | 2023 Q1 |  |  |  |
| PCI-6225 | 2023 Q1 |  |  |  |
| PCI-6229 | 2023 Q1 |  |  |  |
| PCI-6230 | 2023 Q1 |  |  |  |
| PCI-6232 | 2023 Q1 |  |  |  |
| PCI-6233 | 2023 Q1 |  |  |  |
| PCI-6236 | 2023 Q1 |  |  |  |
| PCI-6238 | 2023 Q1 |  |  |  |
| PCI-6239 | 2023 Q1 |  |  |  |
| PCI-6250 | 2023 Q1 |  |  |  |
| PCI-6251 | 2023 Q1 |  |  |  |
| PCI-6254 | 2023 Q1 |  |  |  |
| PCI-6255 | 2023 Q1 |  |  |  |
| PCI-6259 | 2023 Q1 |  |  |  |
| PCI-6280 | 2023 Q1 |  |  |  |
| PCI-6281 | 2023 Q1 |  |  |  |
| PCI-6284 | 2023 Q1 |  |  |  |
| PCI-6289 | 2023 Q1 |  |  |  |

Related information:

- 62xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility

#### PCIe Devices

Consult the following table for information on PCIe devices supported by
 FlexLogger.

| NI Product | Model Name | Compatible Accessories | Earliest Version with Support | Notes |
| --- | --- | --- | --- | --- |
| 62xx Multifunction I/O Devices | PCIe-6251 | For information on compatible accessories, refer to 62xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | For digital lines, FlexLogger supports the 10 Hz data rate and synchronization with analog channels configured on the same device.FlexLogger does not support synchronization between multiple PCIe 62xx devices. |
| PCIe-6259 | 2023 Q1 |  |  |  |
| 63xx Multifunction I/O Devices | PCIe-6320 | For information on compatible accessories, refer to 63xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | FlexLogger doesn't support synchronization between multiple PCIe 63xx devices. |
| PCIe-6321 | 2023 Q1 |  |  |  |
| PCIe-6323 | 2023 Q1 |  |  |  |
| PCIe-6340 | 2025 Q3 |  |  |  |
| PCIe-6341 | 2023 Q1 |  |  |  |
| PCIe-6342 | 2025 Q3 |  |  |  |
| PCIe-6343 | 2023 Q1 |  |  |  |
| PCIe-6345 | 2025 Q4 |  |  |  |
| PCIe-6346 | 2023 Q1 |  |  |  |
| PCIe-6347 | 2025 Q4 |  |  |  |
| PCIe-6350 | 2025 Q3 |  |  |  |
| PCIe-6351 | 2023 Q1 |  |  |  |
| PCIe-6352 | 2025 Q3 |  |  |  |
| PCIe-6353 | 2023 Q1 |  |  |  |
| PCIe-6355 | 2025 Q4 |  |  |  |
| PCIe-6357 | 2025 Q4 |  |  |  |
| PCIe-6361 | 2023 Q1 |  |  |  |
| PCIe-6363 | 2023 Q1 |  |  |  |
| PCIe-6374 | 2023 Q1 |  |  |  |
| PCIe-6376 | 2023 Q1 |  |  |  |

Related information:

- 62xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 63xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility

#### PXI Modules

Consult the following table for information on PXI modules supported by
 FlexLogger.

| NI Product | Model Name | Compatible Accessories | Earliest Version with Support | Notes |
| --- | --- | --- | --- | --- |
| 62xx Multifunction I/O Modules | PXI-6220 | For information on compatible accessories, refer to 62xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | For digital lines, FlexLogger supports the 10 Hz data rate and synchronization with analog channels configured on the same module. |
| PXI-6221 | 2023 Q1 |  |  |  |
| PXI-6224 | 2023 Q1 |  |  |  |
| PXI-6225 | 2023 Q1 |  |  |  |
| PXI-6229 | 2023 Q1 |  |  |  |
| PXI-6230 | 2023 Q1 |  |  |  |
| PXI-6232 | 2023 Q1 |  |  |  |
| PXI-6233 | 2023 Q1 |  |  |  |
| PXI-6236 | 2023 Q1 |  |  |  |
| PXI-6238 | 2023 Q1 |  |  |  |
| PXI-6239 | 2023 Q1 |  |  |  |
| PXI-6251 | 2023 Q1 |  |  |  |
| PXI-6254 | 2023 Q1 |  |  |  |
| PXI-6255 | 2023 Q1 |  |  |  |
| PXI-6259 | 2023 Q1 |  |  |  |
| PXI-6280 | 2021 R2 |  |  |  |
| PXI-6281 | 2021 R2 |  |  |  |
| PXI-6284 | 2021 R2 |  |  |  |
| PXI-6289 | 2021 R2 |  |  |  |
| Digital I/O Modules | PXI-6511 | For information on compatible accessories, refer to the 650x/651x/652x Models : DAQ Digital I/O Cable and Accessory Compatibility Guide on ni.com. | 2021 R3 | These modules are software-timed and do not support synchronization. |
| PXI-6512 | 2021 R3 |  |  |  |
| PXI-6513 | 2021 R3 |  |  |  |
| PXI-6514 | 2021 R3 |  |  |  |
| PXI-6515 | 2021 R3 |  |  |  |
| PXI-6521 | 2021 R3 |  |  |  |
| PXI-6528 | 2021 R3 |  |  |  |
| PXI-6529 | 2021 R3 |  |  |  |
| CAN Interface Module | PXI-8512 (1-port and 2-port) | — | 2020 R1 | These modules must be used in a PXI Express Hybrid Compatible slot of a supported PXI Express chassis. For more information on PXI compatibility with PXI Express chassis, refer to PXI Card Compatibility With PXIe Chassis on ni.com. |
| LIN Interface Module | PXI-8516 | — | 2020 R1 |  |

Related information:

- 62xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 63xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 650x/651x/652x Models : DAQ Digital I/O Cable and Accessory
 Compatibility Guide
- PXI Card Compatibility With PXIe Chassis

#### PXIe Chassis

Consult the following table for information on PXIe chassis supported by
 FlexLogger.

| NI Product | Model Name | Earliest Version with Support | Notes |
| --- | --- | --- | --- |
| PXIe Chassis | PXIe-1062Q | 2020 R1 | FlexLogger does not support any module used in a PXI peripheral slot. |
| PXIe-1065 | 2020 R1 |  |  |
| PXIe-1066DC | 2020 R1 |  |  |
| PXIe-1071 | 2020 R1 | — |  |
| PXIe-1073 | 2020 R1 | — |  |
| PXIe-1075 | 2020 R1 | — |  |
| PXIe-1078 | 2020 R1 | — |  |
| PXIe-1082 | 2020 R1 | — |  |
| PXIe-1082DC | 2020 R1 | — |  |
| PXIe-1083 | 2021 R3 | — |  |
| PXIe-1084 | 2020 R1 | This chassis supports multi-chassis synchronization. |  |
| PXIe-1085 (12 GB/s and 24GB/s) | 2020 R1 | — |  |
| PXIe-1088 | 2021 R3 | — |  |
| PXIe-1090 | 2021 R4 | — |  |
| PXIe-1092 | 2020 R1 | These chassis supports multi-chassis synchronization. |  |
| PXIe-1095 | 2020 R1 |  |  |

Note

#### PXIe Controllers

Consult the following table for information on PXIe controllers supported by
 FlexLogger.

Supported embedded controllers must meet the minimum system requirements. Refer to
 *FlexLogger System Requirements* for more information.

| NI Product | Model Name | Earliest Version with Support | Notes |
| --- | --- | --- | --- |
| PXIe Remote Control Modules | PXIe-8301 | 2020 R3 | — |
| PXIe-8360 | 2020 R3 | — |  |
| PXIe-8370 | 2020 R3 | — |  |
| PXIe-8375 | 2020 R3 | — |  |
| PXIe-8381 | 2020 R3 | — |  |
| PXIe-8388 | 2020 R3 | — |  |
| PXIe-8389 | 2020 R3 | — |  |
| PXIe-8394 | 2020 R3 | — |  |
| PXIe-8398 | 2020 R3 | — |  |
| PXIe-8399 | 2020 R3 | — |  |

Related reference:

- FlexLogger System Requirements

#### PXIe Modules

Consult the following table for information on PXIe modules supported by
 FlexLogger.

| NI Product | Model Name | Compatible Accessories | Earliest Version with Support | Notes |
| --- | --- | --- | --- | --- |
| Analog Input Modules | PXIe-4300 | TB-4300 TB-4300B TB-4300C | 2020 R1 | — |
| PXIe-4302 | TB-4302 RM-4302 TB-4302C | 2020 R1 | — |  |
| PXIe-4303 | TB-4302 RM-4302 TB-4302C | 2020 R1 | — |  |
| PXIe-4304 | TB-4304 RM-4304 | 2020 R1 | — |  |
| PXIe-4305 | TB-4304 RM-4304 | 2020 R1 | — |  |
| PXIe-4309 | TB-4309 (Mass Termination) TB-4309 (Screw Terminal) | 2020 R1 | This module supports auto zero. Refer to the device documentation, available at ni.com/docs for additional information. |  |
| PXIe-4310 | TB-4310 | 2020 R1 | — |  |
| PXIe-4481 | — | 2020 R2 | — |  |
| Strain/Bridge Input Modules | PXIe-4330 | TB-4330 RM-24999 | 2020 R1 | — |
| PXIe-4331 | TB-4330 RM-24999 | 2020 R1 | — |  |
| PXIe-4339 | TB-4339 TB-4339B TB-4339C RM-4339 | 2020 R1 | — |  |
| Displacement Input Module | PXIe-4340 | TB-4340 | 2020 R1 | — |
| Temperature Input Modules | PXIe-4353 | TB-4353 TC-4353 | 2020 R1 | This module supports auto zero. Refer to the device documentation, available at ni.com/docs, for additional information. |
| PXIe-4357 | TB-4357 | 2020 R1 | FlexLogger supports resistance measurements for this module. |  |
| Analog Output Modules | PXIe-4322 | TB-4322 | 2020 R1 | — |
| PXIe-6738 | For information on compatible accessories, refer to 67xx Models : DAQ Analog Output Cable and Accessory Compatibility on ni.com. | 2021 R2 | FlexLogger does not support waveform output. Output signals are software-timed and nondeterministic. |  |
| PXIe-6739 | 2021 R2 |  |  |  |
| Sound and Vibration Modules | PXIe-4464 | — | 2020 R1 | — |
| PXIe-4480 | — | 2020 R1 | FlexLogger does not support the Charge measurement type. |  |
| PXIe-4492 | — | 2020 R1 | FlexLogger automatically selects the Medium (100 Hz) data rate for the PXIe-449x. Using data rates between 1,000 Hz and 8,000 Hz with the PXIe-449x may cause delays when configuring channels. |  |
| PXIe-4496 | — | 2020 R1 |  |  |
| PXIe-4497 | — | 2020 R1 |  |  |
| PXIe-4498 | — | 2020 R1 |  |  |
| PXIe-4499 | — | 2020 R1 |  |  |
| 62xx Multifunction I/O Modules | PXIe-6251 | For information on compatible accessories, refer to 62xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | For digital lines, FlexLogger supports the 10 Hz data rate and synchronization with analog channels configured on the same module. |
| PXIe-6259 | 2023 Q1 |  |  |  |
| 63xx Multifunction I/O Modules | PXIe-6321 | For information on compatible accessories, refer to 63xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2025 Q3 | — |
| PXIe-6323 | 2025 Q3 | — |  |  |
| PXIe-6341 | 2020 R4 | — |  |  |
| PXIe-6343 | 2025 Q3 | — |  |  |
| PXIe-6345 | 2020 R4 | — |  |  |
| PXIe-6349 | 2020 R4 | — |  |  |
| PXIe-6351 | 2025 Q3 | — |  |  |
| PXIe-6353 | 2025 Q3 | — |  |  |
| PXIe-6355 | 2020 R4 | — |  |  |
| PXIe-6356 | 2020 R4 | — |  |  |
| PXIe-6357 | 2025 Q3 | — |  |  |
| PXIe-6358 | 2020 R4 | — |  |  |
| PXIe-6361 | 2020 R4 | — |  |  |
| PXIe-6363 | 2020 R4 | — |  |  |
| PXIe-6365 | 2020 R4 | — |  |  |
| PXIe-6366 | 2020 R4 | — |  |  |
| PXIe-6368 | 2020 R4 | — |  |  |
| PXIe-6375 | 2020 R4 | — |  |  |
| PXIe-6376 | 2020 R4 | — |  |  |
| PXIe-6378 | 2020 R4 | — |  |  |
| PXIe-6381 | 2025 Q4 | — |  |  |
| PXIe-6383 | 2025 Q4 | — |  |  |
| PXIe-6386 | 2020 R4 | — |  |  |
| PXIe-6396 | 2020 R4 | — |  |  |
| Digital I/O Modules | PXIe-6509 | For information on compatible accessories, refer to the 650x/651x/652x Models : DAQ Digital I/O Cable and Accessory Compatibility Guide on ni.com. | 2021 R3 | This module is software-timed and does not support synchronization. |
| PXIe-6535 | For information on compatible accessories, refer to Digital Instrument Cable and Accessory Compatibility on ni.com. | 2021 R3 | FlexLogger does not support synchronization for these hardware-timed modules. |  |
| PXIe-6536 | 2021 R3 |  |  |  |
| PXIe-6537 | 2021 R3 |  |  |  |
| Vehicle Multiprotocol Interface Module | PXIe-8510 (2-Port and 6-port) | TRC-8542 TRC-8543 TRC-8546 | 2020 R1 | — |

Related information:

- 62xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 63xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 650x/651x/652x Models : DAQ Digital I/O Cable and Accessory
 Compatibility Guide
- 67xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- Digital Instrument Cable and Accessory Compatibility

#### USB Devices

Consult the following table for information on USB devices supported by
 FlexLogger.

| NI Product | Model Name | Compatible Accessories | Earliest Version with Support | Notes |
| --- | --- | --- | --- | --- |
| Educational USB | myDAQ Student Data Acquisition Device | — | 2026 Q1 | FlexLogger doesn't support configuring audio output channels on this device. |
| Low-cost DAQ Devices | USB-6000 | — | 2021 R4 | Screw Terminal Models |
| USB-6001 | — | 2021 R4 |  |  |
| USB-6002 | — | 2021 R4 |  |  |
| USB-6003 | — | 2021 R4 |  |  |
| USB-6008 | — | 2023 Q4 |  |  |
| USB-6009 | — | 2023 Q4 |  |  |
| 62xx Multifunction I/O Devices | USB-6210 | For information on compatible accessories, refer to 62xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2023 Q1 | For digital lines, FlexLogger supports the 10 Hz data rate and synchronization with analog channels configured on the same device. |
| USB-6211 | 2023 Q1 |  |  |  |
| USB-6212 | 2023 Q1 |  |  |  |
| USB-6215 | 2023 Q1 |  |  |  |
| USB-6216 | 2023 Q1 |  |  |  |
| USB-6218 | 2023 Q1 |  |  |  |
| USB-6221 | 2023 Q1 |  |  |  |
| USB-6225 | 2023 Q1 |  |  |  |
| USB-6229 | 2023 Q1 |  |  |  |
| USB-6251 | 2023 Q1 |  |  |  |
| USB-6255 | 2023 Q1 |  |  |  |
| USB-6259 | 2023 Q1 |  |  |  |
| USB-6281 | 2023 Q1 |  |  |  |
| USB-6289 | 2023 Q1 |  |  |  |
| 63xx Multifunction I/O Devices | USB-6341 | For information on compatible accessories, visit 63xx Models : DAQ Multifunction I/O Cable and Accessory Compatibility on ni.com. | 2021 R1 | Screw Terminal or BNC Models |
| USB-6343 | 2021 R1 |  |  |  |
| USB-6346 | 2021 R1 |  |  |  |
| USB-6349 | 2021 R1 | Screw Terminal Models |  |  |
| USB-6351 | 2021 R1 |  |  |  |
| USB-6353 | 2021 R1 |  |  |  |
| USB-6356 | 2021 R1 |  |  |  |
| USB-6361 | 2021 R1 | Screw Terminal, BNC, or Mass Termination Models |  |  |
| USB-6363 | 2021 R1 |  |  |  |
| USB-6366 | 2021 R1 |  |  |  |
| NI mioDAQ | USB-6421 | — | 2024 Q3.1 | — |
| USB-6423 | — | 2024 Q3.1 | — |  |
| USB-6451 | — | 2024 Q3.1 | — |  |
| USB-6453 | — | 2024 Q3.1 | — |  |
| CAN Interface Devices | USB-8502 | — | 2018 R2 | — |
| LIN Interface Devices | USB-8506 | — | 2019 R2 | — |

Related information:

- 62xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility
- 63xx Models : DAQ Multifunction I/O Cable and Accessory
 Compatibility

<!--NI_TOPIC bundle=flexlogger path=supported-sensor-class-types.html language=enus -->
## TOPIC 00084: Supported Sensor Class Types

- bundle_id: `flexlogger`
- source_path: `supported-sensor-class-types.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/supported-sensor-class-types.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determine if your sensors are supported, and which physical measurements they can acquire in FlexLogger. FlexLogger supports the following sensors. The sensor classes available in your system depend on your specific hardware configuration and the type of physical measurement you are acquiring. For m

### Supported Sensor Class Types

Determine if your sensors are supported, and which physical measurements they can acquire in FlexLogger.

FlexLogger supports the following sensors. The sensor classes available in your system depend on your specific hardware configuration and the type of physical measurement you are acquiring.

For more detailed descriptions of the sensor class types, refer to the *Sensor Class
 Reference*.

For descriptions and additional information of the supported physical measurements, refer
 to the *Physical Measurement Type Reference*.

| Sensor Class | Supported Physical Measurements |
| --- | --- |
| Voltage | Acceleration |
| Angular Position |  |
| Angular Velocity |  |
| Current |  |
| Custom |  |
| Force |  |
| Frequency |  |
| Linear Position |  |
| Linear Velocity |  |
| Pressure |  |
| Pulse Width |  |
| Sound Pressure |  |
| Temperature |  |
| Voltage |  |
| Current | Acceleration |
| Angular Position |  |
| Angular Velocity |  |
| Current |  |
| Custom |  |
| Force |  |
| Linear Position |  |
| Linear Velocity |  |
| Pressure |  |
| Sound Pressure |  |
| Temperature |  |
| Torque |  |
| Current Shunt | Current |
| Custom |  |
| Force |  |
| Pressure |  |
| Torque |  |
| Bridge | Force |
| Custom |  |
| Pressure |  |
| Strain |  |
| Torque |  |
| IEPE | Acceleration |
| Force |  |
| Linear Velocity |  |
| Sound Pressure |  |
| Thermocouple | Temperature |
| Encoder | Angular Position |
| Angular Velocity |  |
| Linear Position |  |
| Linear Velocity |  |
| Pulse Counter | Pulse |
| RTD | Temperature |
| Frequency Counter | Angular Velocity |
| Frequency |  |
| Linear Velocity |  |
| Pulse Width |  |
| LVDT | Linear Position |
| RVDT | Angular Position |
| Resistance | Resistance |

Parent topic:

Configuring Sensors in Your Channel Specification

Related reference:

- Sensor Class Reference
- Physical Measurement Type Reference

<!--NI_TOPIC bundle=flexlogger path=synchronization.html language=enus -->
## TOPIC 00085: Synchronization

- bundle_id: `flexlogger`
- source_path: `synchronization.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/synchronization.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synchronize your system to coordinate inputs within a module or device, between modules in a single chassis, or between multiple devices or chassis. This feature is only available as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. When you synchronize device

### Synchronization

*Synchronize* your system to coordinate inputs within a module or device, between
 modules in a single chassis, or between multiple devices or chassis.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is only available as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

When you synchronize devices, FlexLogger correlates their inputs in time. If you do not
 synchronize devices, their inputs may have a large initial skew and drift over time.
 *Skew* refers to the difference between input start times (t<sub>0</sub>)
 relative to other channels. *Drift* refers to the change in skew over
 time.

Unless noted otherwise, inputs in FlexLogger are generally hardware-timed and support
 synchronization. For *hardware-timed* inputs, a digital signal such as a
 clock on your device controls the rate of generation.

#### Why is my data not synchronized?

Not all devices support synchronization and not all devices that support synchronization
 can be synchronized in FlexLogger. Inputs from some devices may have skewed start times and
 drift over time relative to other channels. For *software-timed* inputs, the rate
 at which the signals are generated is determined by the software and operating system. Since
 software-timed inputs are not timestamped using a hardware clock, they cannot be
 synchronized. To learn more about synchronization, visit *Synchronization Basics*
 on ni.com.

The following table describes some example scenarios where inputs may not be synchronized.
 For help with troubleshooting synchronization issues in your system, visit
 ni.com/support.

| Scenario | Notes |
| --- | --- |
| You are using multiple chassis. | Refer to Synchronization Status for more information. |
| You are using simulated inputs. | FlexLogger does not synchronize simulated inputs. |
| You are using a PXI or PXIe Digital I/O module. | The hardware-timed PXI or PXIe Digital I/O modules use their own sample clock that is not rate-locked. Inputs from PXI or PXIe Digital I/O modules cannot be synchronized with the inputs from other modules in the chassis. The inputs on the other modules in the chassis will be synchronized to one another. |
| You are using an NI-XNET module and a C Series Delta Sigma (DSA) module in the same USB or non-time sensitive networking (non-TSN) enabled Ethernet cDAQ chassis. | FlexLogger does not currently support synchronization between these types of modules. When you configure a DSA module, it generates the sample clock timebase that all DAQ modules in the chassis use, and the DSA module cannot share that clock with any NI-XNET modules. Refer to the hardware documentation for your module if you are unsure whether you have a DSA C Series module. |

Parent topic:

Configuring I/O Channels

Related tasks:

- Using Network Synchronization in Your Project
- Using PXIe Synchronization in Your Project

Related reference:

- Synchronization Status

Related information:

- Synchronization Basics
- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=system-requirements.html language=enus -->
## TOPIC 00086: FlexLogger System Requirements

- bundle_id: `flexlogger`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/system-requirements.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `reference`
- source_description: Your system must meet the following minimum requirements to run and use FlexLogger. Processor Pentium 4 G1 equivalent (Intel i5 equivalent or higher recommended) RAM Minimum 4 GB(8 GB or more recommended) Disk Minimum 12 GB Screen Resolution Minimum 1024 x 768 resolution(1366 x 768 or higher recomme

### FlexLogger System Requirements

Your system must meet the following minimum requirements to run and use FlexLogger.

Processor

(Intel i5 equivalent or higher recommended)

RAM

(8 GB or more recommended)

Disk

Screen Resolution

(1366 x 768 or higher recommended)

<!--NI_TOPIC bundle=flexlogger path=user-manual-welcome.html language=enus -->
## TOPIC 00087: FlexLogger User Manual

- bundle_id: `flexlogger`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/user-manual-welcome.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexLogger User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### FlexLogger
 User Manual

The FlexLogger User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Operating System Compatibility
- FlexLogger Editions
- Download FlexLogger
- License Setup and Activation
- FlexLogger Release Notes
- FlexLogger Python API Overview
- FlexLogger Python API Reference
- FlexLogger Plug-In Development Kit User Manual
- FlexLogger LabVIEW API Reference
- FlexLogger Plug-in Development Kit Compatibility with FlexLogger
 and LabVIEW
- FlexLogger and LabVIEW Compatibility
- FlexLogger and TestStand Compatibility

<!--NI_TOPIC bundle=flexlogger path=using-network-synchronization.html language=enus -->
## TOPIC 00088: Using Network Synchronization in Your Project

- bundle_id: `flexlogger`
- source_path: `using-network-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/using-network-synchronization.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Automatically synchronize acquisitions between systems across an Ethernet network. This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Synchronization-enabled devices must use the same protocol, either IEEE 802.1AS or 1588, to s

### Using Network Synchronization in Your
 Project

Automatically synchronize acquisitions between systems across an Ethernet
 network.

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete
 FlexLogger license. Refer to *FlexLogger Editions* for more information.

Synchronization-enabled devices must use the same protocol, either IEEE 802.1AS or 1588, to
 synchronize over the network.

1. Ensure that your system includes at least two devices that support network
 synchronization. Refer to *Supported Hardware* for more information.
2. Ensure that the synchronization-enabled devices in your system connected using
 a configuration that supports network synchronization. You can use the following
 topology configuration options: 
 
 Refer to your device documentation, available at
 ni.com/docs, for additional information on
 synchronization and networking.
  - Line topology—Also known as
 daisy-chaining or bus topology. The host communicates directly with all
 nodes through one bus line. A standard Ethernet device or switch can be
 added to the end of the chain. [IMAGE alt='image' src='GUID-659ED79F-51EB-4BBD-BD62-829D6B869E9B-a5.svg']
  - Ring topology—The host
 communicates with all nodes through the most effective path. You must use an
 external switch and configure the network properly before creating redundant
 links in the network. [IMAGE alt='image' src='GUID-06BDF79B-19CF-4C06-B9A5-54547A66FA03-a5.svg']
  - Star topology—The host
 communicates directly with each node through an external switch. Redundant
 links are recommended, but optional. You must use an external switch and
 configure the network properly before creating redundant links in the
 network. [IMAGE alt='image' src='GUID-1BD9CA11-3246-433E-8CE6-F858AEBAAA68-a5.svg'] Note For network
 synchronization, star topology configuration requires an external IEEE
 802.1AS or 1588 switch. All the devices and switches within the star
 topology must be compliant with the IEEE 802.1AS or 1588 protocol to
 enable synchronization.
3. To ensure that synchronization is enabled, navigate to File»Preferences»General and check Enable multi-chassis and network
 synchronization.
4. Select the network synchronization protocol you want to use. 
 OptionDescriptionDevice setting
 Use the protocol currently set on each TSN device. FlexLogger synchronizes using the
 protocol set on the majority of devices. Only devices set to the same
 protocol are synchronized. If an equal number of devices with
 configured channels are set to IEEE 802.1AS and 1588 protocol,
 FlexLogger uses the protocol for the first network FlexLogger
 discovers.1588
 Use 1588 protocol on all TSN devices802.1AS
 Use 802.1AS protocol on all TSN devices.

Synchronization Status

Parent topic:

Synchronization

Related reference:

- Synchronization Status

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=using-pxie-synchronization.html language=enus -->
## TOPIC 00089: Using PXIe Synchronization in Your Project

- bundle_id: `flexlogger`
- source_path: `using-pxie-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/using-pxie-synchronization.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Automatically synchronize devices between PXIe chassis. Introduced in FlexLogger 2020 R4 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Supported PXIe chassis with the optional timing and synchronization upgrade share trigg

### Using PXIe Synchronization in Your
 Project

Automatically synchronize devices between PXIe chassis.

Introduced in FlexLogger 2020 R4

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Supported PXIe chassis with the optional timing and synchronization upgrade share
 trigger and clock signals using HDMI cables.

1. Ensure that your system includes at least two chassis that support PXIe
 synchronization. Refer to the supported hardware topic for more information.
2. Ensure that the synchronization-enabled devices in your system are using the
 following configuration that supports synchronization: 
 Line topology—Also known as daisy-chaining or bus topology. The host communicates directly
 with all chassis and chassis share trigger and clock signals through one bus
 line. 
[IMAGE alt='image' src='GUID-5052B0DD-40EE-4DB7-9F38-714166A7B07D-a5.svg']
 You must properly connect to the In and Out ports on the chassis to enable
 synchronization. Refer to your chassis documentation on
 ni.com/docs for additional information on synchronization and
 networking.
3. Ensure that synchronization is enabled by going to File»Preferences and checking Enable multi-chassis and network
 synchronization on the General tab.

Synchronization
 Status

Parent topic:

Synchronization

Related reference:

- Synchronization Status

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=using-systemlink-to-exchange-data-back-up-files.html language=enus -->
## TOPIC 00090: Using SystemLink to Share Data and Back Up Files

- bundle_id: `flexlogger`
- source_path: `using-systemlink-to-exchange-data-back-up-files.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/using-systemlink-to-exchange-data-back-up-files.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to SystemLink so you can automatically back up, share, and remotely monitor test data from your FlexLogger project. Introduced in FlexLogger 2020 R3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Data from your Flex

### Using SystemLink to Share Data and Back Up
 Files

Connect to SystemLink so you can automatically back up, share, and remotely monitor
 test data from your FlexLogger project.

Introduced in FlexLogger 2020 R3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

Data from your FlexLogger channels is published as SystemLink tags. SystemLink tags transmit
 and store measurement data and are analogous to FlexLogger channels.

FlexLogger sets the read data rate at 1 Hz when using
 SystemLink tags. For channels that require a faster read data rate, consider using the FlexLogger Plug-In Development Kit to create a custom LabVIEW plug-in for your project. Refer to
 *Adding a Plug-In to Your Project* for more information.

- [Publishing Data and Backup Files to a Remote SystemLink Server](publish-data-backup-files-remote-systemlink-server.html) To share data across your organization and back up your files, publish FlexLogger test data and files to your remote SystemLink server.
- [Publish or Consume Data Locally (Legacy)](publish-or-consume-data-locally.html) Use the NI Web Server Configuration installed with FlexLogger to exchange test data locally between FlexLogger and Python or LabVIEW.

Parent topic:

Extending FlexLogger Functionality

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=using-teds-sensors-in-channel-spec.html language=enus -->
## TOPIC 00091: Using TEDS Sensors in Your Channel Specification

- bundle_id: `flexlogger`
- source_path: `using-teds-sensors-in-channel-spec.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/using-teds-sensors-in-channel-spec.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure your project channels with a transducer electronic data sheet (TEDS). Introduced in FlexLogger 2020 R3 This feature is available only as part of a complete FlexLogger license. Refer to FlexLogger Editions for more information. Click Scan project for TEDS in the toolbar. FlexLogger scans al

### Using TEDS Sensors in Your Channel
 Specification

Configure your project channels with a transducer electronic data sheet
 (TEDS).

Introduced in FlexLogger 2020 R3

[IMAGE alt='image' src='GUID-69A3BDCD-076D-4B97-8811-EFD596422E6A-a5.png'] This feature is available only as part of a complete FlexLogger
 license. Refer to *FlexLogger Editions* for more information.

1. Click Scan project for TEDS[IMAGE alt='image' src='GUID-D01CACF8-065D-499E-801F-1031BFEFB792-a5.png']
 in the toolbar. FlexLogger scans all channels in the project for any connected
 TEDS sensors. 
 The following table lists the possible results of the Scan project
 for TEDS action.Table 23.TEDS Sensor States and Corresponding Results in FlexLoggerSensor State
 Result in FlexLoggerTEDS sensor compatible with the channel is
 connected
 Channel is configured using data read from the TEDS scan.
 The TEDS sensor properties overwrite previously configured channels. Channel
 details are prefixed with "TEDS".
 No TEDS sensor is connected
 No changes occur. Channels retain their previous
 configuration.
 TEDS sensor is connected, but a device or FlexLogger does
 not support a sensor class read from TEDS
 Error appears on the channels. Resolve errors to run
 test.
 TEDS sensor is connected, but the device does not support
 a sensor property read from TEDS
 Error appears on the channels. Resolve errors to run
 test.
 TEDS sensor is connected, but data off the EEPROM is
 corrupted
 Error appears on the channels. Replace the TEDS
 sensor.
2. Hover over the channel and click Scan for
 TEDS[IMAGE alt='image' src='GUID-D01CACF8-065D-499E-801F-1031BFEFB792-a5.png']. FlexLogger scans all the channels you selected for connected TEDS
 sensors. 
 Note You can also multi-select channels
 and scan selected channels for TEDS in the channel configuration dialog.
3. Compare channel configuration properties against the TEDS
 data, if necessary. 
 
 Note Pasting a TEDS sensor
 channel configuration into a new channel does not automatically populate
 Sensor Properties with EEPROM contents. To ensure
 that the EEPROM contents are imported into the new channel, click the
 Scan for TEDS button.
  1. Hover over the channel row to see Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] and click the gear
 to open the channel configuration dialog. 
 In the channel configuration dialog, channels you have already scanned for TEDS
 with connected TEDS sensors display "TEDS" after the channel name. To see the
 timestamp of the last scan, hover over Scan for TEDS[IMAGE alt='image' src='GUID-D01CACF8-065D-499E-801F-1031BFEFB792-a5.png'].
  2. In the channel configuration dialog, click Edit
 [IMAGE alt='image' src='GUID-128F4C7F-B36E-45D2-8BFB-B820A3BC51A3-a5.png'] on the Sensor Properties field to view
 the contents of the sensor EEPROM from the last scan.

Parent topic:

Configuring Sensors in Your Channel Specification

Related information:

- FlexLogger Editions

<!--NI_TOPIC bundle=flexlogger path=using-test-metadata-as-placeholders.html language=enus -->
## TOPIC 00092: Using Test Metadata as Placeholders for Log File Names and Locations

- bundle_id: `flexlogger`
- source_path: `using-test-metadata-as-placeholders.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/using-test-metadata-as-placeholders.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Use test metadata, including test properties, time, and date, as placeholders for your data log file name and location. Introduced in FlexLogger 2021 R1 In the Base path, File name, or Backup path fields of your Logging Specification document, enter { to initiate a drop-down menu that lists metadata

### Using Test Metadata as Placeholders for Log
 File Names and Locations

Use test metadata, including test properties, time, and date, as placeholders for
 your data log file name and location.

Introduced in FlexLogger 2021 R1

1. In the Base path, File
 name, or Backup
 path fields of your Logging
 Specification document, enter { to
 initiate a drop-down menu that lists metadata
 placeholders.
2. Double-click the placeholder you want to add to your file name
 or locations.

Parent topic:

Adding Test Properties to a Project

<!--NI_TOPIC bundle=flexlogger path=viewing-data-in-excel.html language=enus -->
## TOPIC 00093: Viewing Logged Data in Excel

- bundle_id: `flexlogger`
- source_path: `viewing-data-in-excel.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/viewing-data-in-excel.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: View the data from your logged data files in Microsoft Excel. On the Data tab, right-click any log file and select Locate in Windows Explorer. Right-click the TDMS log file you want to open and select Open with Excel Importer .

### Viewing Logged Data in Excel

View the data from your logged data files in Microsoft Excel.

1. On the 
 Data tab, right-click any log file and select 
 Locate in Windows Explorer.
2. Right-click the TDMS log file you want to open and select Open with»Excel Importer.

Parent topic:

Viewing, Analyzing, and Exporting Data

<!--NI_TOPIC bundle=flexlogger path=viewing-data-with-diadem.html language=enus -->
## TOPIC 00094: Viewing and Analyzing Logged Data with DIAdem

- bundle_id: `flexlogger`
- source_path: `viewing-data-with-diadem.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/viewing-data-with-diadem.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: View and analyze the data from your logged data files with DIAdem. On the Data tab, double-click the data log file to launch the DIAdem-based FlexLogger TDMS Viewer. View your data and perform analyses including arithmetic calculations and fast Fourier transforms (FFT) using DIAdem ANALYSIS function

### Viewing and Analyzing Logged Data with
 DIAdem

View and analyze the data from your logged data files with DIAdem.

On the 
 Data tab, double-click the data log file to launch the DIAdem-based FlexLogger TDMS Viewer.

View your data and perform analyses including arithmetic calculations and fast Fourier
 transforms (FFT) using DIAdem ANALYSIS functions. For more information about each DIAdem
 ANALYSIS function, click Help in the configuration dialog box for
 each function to launch the DIAdem Help.

Note

If you have a separately licensed version of DIAdem installed, use the following steps to
 configure FlexLogger to launch that version in lieu of the FlexLogger TDMS Viewer.

1. Go to File»Preferences.
2. Under Data viewer options, select Launch a separately
 licensed edition of DIAdem instead of FlexLogger TDMS Viewer.

Parent topic:

Viewing, Analyzing, and Exporting Data

<!--NI_TOPIC bundle=flexlogger path=viewing-data.html language=enus -->
## TOPIC 00095: Viewing, Analyzing, and Exporting Data

- bundle_id: `flexlogger`
- source_path: `viewing-data.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/viewing-data.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `concept`
- source_description: Visualize data in real-time using indicators and graphs on your Screen document or view, analyze, and export logged data.

### Viewing, Analyzing, and Exporting
 Data

Visualize data in real-time using indicators and graphs on your Screen document or
 view, analyze, and export logged data.

- [Visualizing Live Data with Indicators and Graphs](visualizing-live-data-with-indicators-and-graphs.html) Add and configure indicators and graphs on the Screen document to visualize data from your acquisitions in real time.
- [Viewing and Analyzing Logged Data with DIAdem](viewing-data-with-diadem.html) View and analyze the data from your logged data files with DIAdem.
- [Viewing Logged Data in Excel](viewing-data-in-excel.html) View the data from your logged data files in Microsoft Excel.
- [Manually Exporting Data Files to CSV File Format](manually-exporting-data-to-csv.html) Export your data files in the CSV file format on demand.
- [Automatically Exporting Data Files to CSV File Format](automatically-exporting-data-to-csv.html) Configure your Logging Specification to automatically export your data files to the CSV file format.

<!--NI_TOPIC bundle=flexlogger path=visualizing-live-data-with-indicators-and-graphs.html language=enus -->
## TOPIC 00096: Visualizing Live Data with Indicators and Graphs

- bundle_id: `flexlogger`
- source_path: `visualizing-live-data-with-indicators-and-graphs.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger/raw/resource/enus/visualizing-live-data-with-indicators-and-graphs.html
- document_id: `flexlogger`
- page_type: `leaf`
- content_type: `task`
- source_description: Add and configure indicators and graphs on the Screen document to visualize data from your acquisitions in real time. The amount of data you can pause, analyze, and view on a graph is determined by the history length. Refer to Setting the Graph History Length for information on how to adjust the his

### Visualizing Live Data with Indicators and
 Graphs

Add and configure indicators and graphs on the Screen document to
 visualize data from your acquisitions in real time.

Note

Setting the
 Graph History Length

Before you begin, add and configure channels to your FlexLogger
 project.

1. On the Screen document, select an indicator or graph from the
 palette located on the left side of the window. 
 FlexLogger includes the following graph types. Table 49.Graph Types You Can Add to the
 Screen DocumentGraph Type
 DescriptionHigh-Speed Graph
 Visualize large amounts of data over short time
 periods.
 Long History Graph
 Visualize data over extended time periods.
 Frequency Spectrum Graph
 Visualize the frequency spectrum of your signals. Refer to
 *Frequency Spectrum Graph* for additional information on how
 FlexLogger generates this type of graph.
 XY Graph
 Visualize data from one or more channels relative to the data of another
 channel.
 Note To maintain performance,
 data is downsampled using a configurable finite impulse response (FIR)
 filter.
2. Drop the indicator or graph in the location you want on your
 Screen. 
 [IMAGE alt='image' src='GUID-D4FC2FC1-D183-4CAF-B2F0-F88627B8D20A-a5.png'] 
 When you place an indicator or graph, FlexLogger opens the associated channel
 mapping window.
3. Select one or more channels to map to the indicator or graph. After you select a
 channel, you will see the signal on the indicator or graph.
4. Optional: 
 To customize indicator or graph settings, click the item and modify settings in the
 Item configuration pane located on the right side of the
 Screen window. If the Item pane is not
 visible, click Expand
 [IMAGE alt='image' src='GUID-AA8C4459-8274-49A1-BE3F-87510B545236-a5.png'] to view the pane. The configuration options
 are specific to the part of the item you selected.
5. Optional: 
 To further customize different parts of an indicator or graph, right-click the part you
 want to customize and select options from the menu.
6. Optional: 
 To pause a graph and view the graph history, click Hold Data and
 use the pan controls.

Parent topic:

Viewing, Analyzing, and Exporting Data

Related concepts:

- Frequency Spectrum Graph
- Setting the Graph History Length

Related tasks:

- Configuring Device Channels
