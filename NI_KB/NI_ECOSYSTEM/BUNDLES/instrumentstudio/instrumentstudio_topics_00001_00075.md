# NI DOCUMENT BUNDLE: instrumentstudio

<!--NI_BUNDLE_CHUNK bundle=instrumentstudio start=1 end=75 -->
<!--NI_TOPIC bundle=instrumentstudio path=add-pin-map-file.html language=enus -->
## TOPIC 00001: Add Pin Map Files to a Project

- bundle_id: `instrumentstudio`
- source_path: `add-pin-map-file.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/add-pin-map-file.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use pin maps that you create outside of InstrumentStudio by adding the existing pin map file to your project. Select FileNewPin Map. Select a pin map file (.pinmap). Click OK to add the file to your project. To open the Pin Map Editor and update the pin map, double-click the file in the proj

### Add Pin Map Files to a Project

You can use pin maps that you create outside of InstrumentStudio by adding the existing
 pin map file to your project.

1. Select File»New»Pin Map.
2. Select a pin map file (.pinmap).
3. Click OK to add the file to your project.
4. Optional: 
 To open the Pin Map Editor and update the pin map, double-click
 the file in the project files pane.

Make
 active

Parent topic:

Pin Maps

<!--NI_TOPIC bundle=instrumentstudio path=add-remote-panel-layout.html language=enus -->
## TOPIC 00002: Add a Remote RFmx Panel to Your Layout

- bundle_id: `instrumentstudio`
- source_path: `add-remote-panel-layout.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/add-remote-panel-layout.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can view RFmx hardware measurements remotely using an InstrumentStudio panel after you complete these steps. Before you can view RFmx hardware measurements remotely, you must configure your system. For more information, see Configure your System for Remote Panels. Enable the Remote RFmx panel fe

### Add a Remote RFmx Panel to Your Layout

You can view RFmx hardware measurements remotely using an InstrumentStudio panel after
 you complete these steps.

Configure your System for
 Remote Panels

1. Enable the Remote RFmx panel feature in the
 InstrumentStudio settings.
2. Click Add remote host connection.
3. Select Remote Instrument as the Host
 type.
4. Enter the IP address (or hostname) and the port number of the server that you
 want to connect to.
5. Click OK to add a panel for the remote RFmx device to
 your layout.
6. Continue setting up your layout as needed.

**Device
 Name-Model
 Number(Remote)**

Note

Parent topic:

Configure Remote RF Signal Analyzer Panels

Related tasks:

- Configuring a gRPC Server for Remote RF Signal Analyzer Panels in InstrumentStudio

#### Manage Remote Connection Preferences

You can remove a remote connection or select a default remote device.

1. Go to File»Preferences»Remote connections.
2. Choose one of the following options to manage remote connections: 
 OptionDescriptionRemove a Connection
 Right-click Remove device.Select a Default Device
 Right-click a device from the list of available devices and select
 Make default device. InstrumentStudio uses
 this device when you create layouts automatically.

<!--NI_TOPIC bundle=instrumentstudio path=apply-pin-filter.html language=enus -->
## TOPIC 00003: Apply a Pin Filter

- bundle_id: `instrumentstudio`
- source_path: `apply-pin-filter.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/apply-pin-filter.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a pin filter to select which sites and system pins to view in an instrument panel. Pin filtering improves navigation in a panel. Before you apply pin filtering, you must select an active project pin map. For more information, see Set an Active Project Pin Map. Click the Pin Filter button ( Icon

### Apply a Pin Filter

Use a pin filter to select which sites and system pins to view in an instrument panel.
 Pin filtering improves navigation in a panel.

Set an Active Project Pin
 Map

1. Click the Pin Filter button ([IMAGE alt='Icon of the Pin Filter button with horizontal lines and a rectangle.' src='GUID-4B195C9C-FB5F-4A54-81C3-AE40DD77D98B-a5.png']) in your device or the instrument panel.
2. Enable the pins that you want to view in your panel.
3. Click OK.

Pins

Note

Note

Parent topic:

Using the Site Filter

Related tasks:

- Set an Active Project Pin Map

<!--NI_TOPIC bundle=instrumentstudio path=build-sequence.html language=enus -->
## TOPIC 00004: Build a Sequence

- bundle_id: `instrumentstudio`
- source_path: `build-sequence.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/build-sequence.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can add panels and steps to a sequence in a project that you already saved. Save you current project before you begin building a sequence. You cannot use the sequencer tool in an unsaved project. Navigate to the panel that you want to add to a sequence. Click the Add to Sequence ( An icon of a b

### Build a Sequence

You can add panels and steps to a sequence in a project that you already
 saved.

Note

1. Navigate to the panel that you want to add to a sequence.
2. Click the Add to Sequence ([IMAGE alt='An icon of a branching sequence.' src='GUID-988B5539-1046-46F3-8981-645708906295-a5.png']) button. 
 Tip You can hover
 over the Add to Sequence ([IMAGE alt='An icon of a branching sequence.' src='GUID-988B5539-1046-46F3-8981-645708906295-a5.png']) button to see a list of all associated steps that contain the
 selected panel.

To ensure that you added the correct steps to the sequence, open the
 Sequencer pane. Then, check the list of steps that appear
 in the Step list view.

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=capture-data.html language=enus -->
## TOPIC 00005: Capture Data

- bundle_id: `instrumentstudio`
- source_path: `capture-data.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/capture-data.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: With InstrumentStudio, you can capture data from an entire layout or a single panel. You can also take a screenshot without capturing data. By default, InstrumentStudio uses the .png file format to capture images and the .tdms file format to capture data. For more information on the .tdms file forma

### Capture Data

With InstrumentStudio, you can capture data from an entire layout or a single panel.
 You can also take a screenshot without capturing data.

By default, InstrumentStudio uses the .png file format to capture images
 and the .tdms file format to capture data. For more information on the
 .tdms file format, see *What is a TDMS File?* in the
 *Related Information* section.

File

»

Preferences

»

Capture data

- File name
- File format
- Destination directory

#### Capture Data from a Layout

Select the Capture data icon ([IMAGE alt='An icon of a bar graph that captures data in InstrumentStudio.' src='GUID-DFE8F0BC-98DF-429F-A6AC-5B4FE01E2C70-a5.gif']) from the instrument header menu to capture data from an entire layout.

When
 you capture data from a layout, InstrumentStudio saves a timestamped screenshot and a data
 file to the destination directory. The screenshot contains the view of the entire layout at
 the time the data was captured. The data file contains detailed information about the
 devices in the layout.

#### Capture Data from a Panel

Open the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']) and selecting Capture data to capture data from a single
 panel.

When you capture data from a panel, InstrumentStudio saves a timestamped
 screenshot and a data file to the destination directory. The screenshot contains the view of
 the panel at the time the data was captured. The data file contains detailed information
 about the devices in the panel.

#### Capture a Separate Screenshot

Select the Capture screenshot icon ([IMAGE alt='An icon of a digital camera that captures screenshots in InstrumentStudio.' src='GUID-59FEAF50-4B83-4033-9414-F433D32813D1-a5.gif']) from the instrument header menu to capture a screenshot but not a data file.
 InstrumentStudio attaches the screenshot to the clipboard.

#### Parse Captured Data

You can parse NI .tdms data files with LabVIEW, LabWindows/CVI,
 DIAdem, VeriStand, or with third-party applications.

.csv

.csv

- Channel
- Device
- Measurement type

.csv

- Individual measurements, such as mean and range
- Individual statistics, such as standard deviation

Related information:

- What is a TDMS File?

<!--NI_TOPIC bundle=instrumentstudio path=configure-device-settings.html language=enus -->
## TOPIC 00006: Configure Device Settings

- bundle_id: `instrumentstudio`
- source_path: `configure-device-settings.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/configure-device-settings.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information on how to configure different instruments and how to export these configurations:

### Configure Device Settings

The following sections contain information on how to configure different instruments
 and how to export these configurations:

- [Digital Multimeters (DMMs)](dmm.html#GUID-416F45DC-B659-45F3-9D72-D7321CAB6900) Use the Digital Multimeter panel to configure ranging modes and perform cable compensation for your Digital Multimeter instruments.
- [LCR Devices](lcr.html#GUID-3C4C141B-7650-4E6D-AEB2-6EE5DF7A84D4) Use the LCR panel to calibrate and perform cable compensation and LCR compensation on your LCR devices.
- [Oscilloscopes](osc.html#GUID-21FAC422-69F1-46A4-8310-9BEC68441B24) Use the Oscilloscope panel to set up and configure your Oscilloscope instruments.
- [Network Analyzers](network-analyzer.html#GUID-9BFEA41F-84B2-471D-9071-6FE96F659B9A) Use the Network Analyzer panel to characterize RF devices and apply corrections to your Network Analyzer instrument.
- [RF Signal Analyzers](rfsa.html#GUID-645B93A1-A3EA-4719-A7B6-357723FB682F) Use the RF Signal Analyzer panel to analyze RF signals, de-embed RF Signal Analyzer instruments, perform self-calibration, and import bitfile data.
- [RF Signal Generators](rfsg.html#GUID-C950F47C-2C5D-438F-8C9A-6518EE81F5C2) Use the RF Signal Generator panel to generate RF signals, de-embed RF Signal Generator instruments, and perform self-calibration.
- [SMU and VPS Devices](smu-vps.html#GUID-3BC84114-FBA4-42B4-A89E-B9075873AB77) Use the SMU/Power Supply panel to select a mode of operation and configure various settings for your SMU and VPS devices.
- [Waveform Generators](wave-gen.html#GUID-6B3F01F6-26A5-4028-B8E3-4BF96A42FDCA) Use the Waveform Generator panel to generate waveforms and configure your Waveform Generator instruments.
- [DAQ Analog Input Devices](daq-analog-input.html#GUID-427D2967-E8B5-4F23-959A-65FC5712244D) Use the DAQ Analog Input panel to configure timing, trigger, and channel settings for your DAQ Analog Input instruments.
- [DAQ Analog Output Devices](daq-analog-output.html#GUID-0E1A982B-7D63-4EB5-8504-FFB631ECD336) Use the DAQ Analog Output panel to configure timing, trigger, and channel settings for your DAQ Analog Output instruments.
- [Export Configurations](export-config.html#GUID-848365DE-E325-499F-9415-BEBC28565F68) You can export device configurations to different applications, such as LabVIEW and TestStand.

<!--NI_TOPIC bundle=instrumentstudio path=configure-steps.html language=enus -->
## TOPIC 00007: Configure Steps

- bundle_id: `instrumentstudio`
- source_path: `configure-steps.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/configure-steps.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Each sequence step is associated with an InstrumentStudio panel. The panel contains the step configuration. InstrumentStudio immediately applies any changes to the step.

### Configure Steps

Each sequence step is associated with an InstrumentStudio panel. The panel contains the
 step configuration. InstrumentStudio immediately applies any changes to the
 step.

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=connecting-to-plug-in-library.html language=enus -->
## TOPIC 00008: Connect to a Plug-In Library

- bundle_id: `instrumentstudio`
- source_path: `connecting-to-plug-in-library.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/connecting-to-plug-in-library.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: A plug-in library is an HTTP web API that contains services that allow you to find and download plug-ins. Plug-in libraries allow you to share and collaborate across teams. A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license. This feature is only

### Connect to a Plug-In Library

A *plug-in library* is an HTTP web API that contains services that allow you
 to find and download plug-ins. Plug-in libraries allow you to share and collaborate across
 teams.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

Plug-In
 Libraries

Related Information

1. Go to Edit Layout»Add remote host connections. 
 Note You can add a plug-in
 library to your project with the Edit Layout
 mode.
2. Click the Add button.
3. Select Plug-In Library as the Host
 type.
4. Enter the IP address (or hostname) and the port number of the plug-in library
 that you want to connect to.
5. Click OK.
6. Continue setting up your layout as needed.

Edit
 Layout

Running a Measurement Plug-In

Parent topic:

Plug-Ins

Related tasks:

- Running a Measurement Plug-In

Related information:

- Plug-In Libraries

<!--NI_TOPIC bundle=instrumentstudio path=create-new-pin-map.html language=enus -->
## TOPIC 00009: Create a New Pin Map

- bundle_id: `instrumentstudio`
- source_path: `create-new-pin-map.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/create-new-pin-map.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Pin Map Editor to create new pin maps in InstrumentStudio. To create a new pin map file (.pinmap), complete one of the following actions: Select File New Pin Map . Click Add in the project files pane toolbar. Use the Pin Map Editor to configure your pin mappings. The Pin Map tab displays map

### Create a New Pin Map

Use the Pin Map Editor to create new pin maps in
 InstrumentStudio.

1. To create a new pin map file (.pinmap), complete one of the
 following actions:
  - Select File»New»Pin Map .
  - Click Add in the project files pane toolbar.
2. Use the Pin Map Editor to configure your pin mappings. 
 The Pin Map tab displays mappable items. Use the left pane to
 browse and configure the mappings that you want to include in your pin map. To manually
 edit the pin map file text, click the XML tab.Note You can only create a new pin map in a
 saved project. InstrumentStudio prompts you to save the project before creating a new
 pin map.
3. Click OK to close the editor and return to your project.
 The new pin map is now the active project pin map.

Parent topic:

Pin Maps

<!--NI_TOPIC bundle=instrumentstudio path=creating-layout.html language=enus -->
## TOPIC 00010: Create and Edit a Layout

- bundle_id: `instrumentstudio`
- source_path: `creating-layout.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/creating-layout.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you can take measurements and monitor devices in InstrumentStudio, you must create a layout. You can create a layout from the Home screen, from the instrument header menu, or from any instrument settings menu ( A cogwheel icon for the instrument settings menu of InstrumentStudio. ). Create a

### Create and Edit a Layout

Before you can take measurements and monitor devices in InstrumentStudio, you must
 create a layout. You can create a layout from the Home screen, from the
 instrument header menu, or from any instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']).

Parent topic:

Configure Panels and Layouts

#### Create a Layout Automatically

InstrumentStudio detects the devices that you installed in your system and creates
 panels for each compatible device.

When you create a layout automatically, InstrumentStudio might not show all available
 devices. For more control over the devices that appear in the soft front panel, see [Create a Layout Manually](creating-layout.html#GUID-0835BF08-65A7-4320-99C0-6C117CDEA641__GUID-63CBB109-C745-4F93-806A-1CD3C7E0AADF).

To create a layout automatically, complete the following steps:

1. Install the devices that you want to use. Ensure that the installed devices appear in
 the Hardware Configuration Utility (HWCU) or Measurement & Automation Explorer
 (MAX).
2. Open InstrumentStudio.
3. Select the Auto create layout option from the
 Home screen or from File»New»Auto create layout.

InstrumentStudio creates a large or small
 panel for each compatible device that is installed in the system.

#### Create a Layout Manually

You can use the Edit Layout window to create a manual layout. In
 a manual layout, you can customize which devices the panel displays. You can also group devices
 of the same type into a single panel, except for oscilloscopes. You can only add oscilloscopes
 of the same model to the same panel.

See *Panels and Layouts* for more information on layout rules and
 restrictions.

Complete the following steps to create a
 layout manually:

1. Access the Edit Layout window in one of the following
 ways:
  - If an instrument panel is already open, click the Edit
 layout ( ) button in the instrument header menu.
  - From the Home 
 screen, select Manual layout... .
  - From the toolbar, select File»New»Manual layout... .
  - From an instrument settings menu
 ( ), select Add/Remove devices . Note If you access the Edit
 Layout window through an instrument settings menu, InstrumentStudio
 automatically applies a filter on the device list. This filter is based on which panel
 you selected the Add/Remove devices option from. You can remove
 or change this filter by clicking the filter icon ([IMAGE alt='An icon of a filter.' src='GUID-13C35A3D-99E2-41D4-9FB2-ED87361ADA62-a5.png']) next to the search field.
2. Search for the devices that you want to include in the layout. You can find a list of
 devices in the left panel of the Edit Layout window. 
 You can filter by device type by clicking the filter icon ([IMAGE alt='An icon of a filter.' src='GUID-13C35A3D-99E2-41D4-9FB2-ED87361ADA62-a5.png']) next to the search field.
3. Add the device to a panel by selecting Create large panel or
 Create small panel from the dropdown menu of the device. 
 The device appears in the panel that you select.Note You can remove a device from a panel by
 clicking the × icon to the right of the device
 name.
4. Optional: 
 Group devices of the same type together in a single panel. You can select a group name
 from the dropdown menu of a device.
5. Select OK to create the layout that you specified.

Related concepts:

- Panels and Layouts

#### Create a Single-Panel Layout

The single-panel layout option allows you to create a manual layout with a single large
 panel. You can customize which devices the panel displays. You can also group devices of the
 same type into a single panel, except for oscilloscopes. You can only add oscilloscopes of the
 same model to the same panel.

See *Panels and Layouts* for more information on layout rules and
 restrictions.

Complete the following steps to create or
 edit a single-panel layout:

1. From the toolbar, select File»New»Single panel layout.... 
 The Select Panel window opens.
2. Search for the devices that you want to include in the layout. 
 You can filter by device type by clicking the filter icon ([IMAGE alt='An icon of a filter.' src='GUID-13C35A3D-99E2-41D4-9FB2-ED87361ADA62-a5.png']) next to the search field.
3. Select the devices that you want to include in the layout.
4. Select OK to create the layout that you specified.

Related concepts:

- Panels and Layouts

#### Edit an Existing Layout

You can edit a layout through the Edit Layout
 window.

Edit Layout

- Click the Edit layout ( ) icon in the instrument header menu.
- Select the Add/Remove devices option from an instrument settings
 menu ( ). Note If you select the Add/Remove
 devices option from an instrument settings menu, InstrumentStudio applies
 a filter on the device list. This filter is based on which panel you selected the
 Add/Remove devices option from. You can remove or change this
 filter by clicking the filter icon ([IMAGE alt='An icon of a filter.' src='GUID-13C35A3D-99E2-41D4-9FB2-ED87361ADA62-a5.png']) next to the search field.

Related concepts:

- Panels and Layouts

<!--NI_TOPIC bundle=instrumentstudio path=daq-analog-input.html language=enus -->
## TOPIC 00011: DAQ Analog Input Devices

- bundle_id: `instrumentstudio`
- source_path: `daq-analog-input.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/daq-analog-input.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQ Analog Input panel to configure timing, trigger, and channel settings for your DAQ Analog Input instruments. Timing Settings By default, InstrumentStudio manages timing settings automatically based on the trigger settings and the channel settings. You can also configure timing settings m

### DAQ Analog Input Devices

Use the DAQ Analog Input panel to configure timing, trigger, and channel settings for
 your DAQ Analog Input instruments.

Parent topic:

Configure Device Settings

#### Timing Settings

By default, InstrumentStudio manages timing settings automatically based on the trigger
 settings and the channel settings. You can also configure timing settings manually.

To configure timing settings manually, click the blue icon to the right of the
 Mode dropdown menu. The following sections describe the effect of
 configuring each setting.

##### Timing
 Mode

Mode

Continuous

Finite

Software

Note

In Continuous mode, InstrumentStudio might skip samples to match the
 rate of the hardware acquisition. The channel statistics in the bottom pane do not
 consider skipped samples.

##### Sample Rate

You can only configure the
 Sample rate setting in the Continuous and the
 Finite timing modes.

The Sample rate setting
 defines the desired sample clock rate, which sets the time interval between
 samples.

The sample rate that you set must match one of the supported rates for your
 DAQ device. If you set the sample rate to an unsupported value, NI-DAQmx automatically
 changes the sample rate to a supported value. The Actual sample rate
 field shows the changed sample rate value.

##### Samples to Read

You can only configure the
 Samples to read setting in the Continuous and the
 Finite timing modes.

Samples to read

- In Continuous timing mode, the number of samples that appear on the
 graph at a time. The combination of the Sample rate setting and
 the Samples to read setting controls how often the graph
 updates.
- In Finite timing mode, the number of samples that InstrumentStudio
 acquires and graphs. After the acquisition completes, you can zoom in to view parts of
 the data in more detail.

#### Trigger Settings

You can configure the mode, the type, and the source of the trigger on the instrument
 panel.

##### Trigger
 Mode

Mode

None

Run

Stop

Start

Run

Reference

Run

##### Trigger
 Type

Type

Digital Edge

Digital Edge Trigger Settings

Analog Edge

Analog Edge Trigger Settings

Analog Window

Analog Window Trigger Settings

Note

Specifications

ni.com/docs

##### Trigger Source

Source

- For digital triggers, you can specify a digital terminal on the DAQ device that you
 are acquiring from. You can also specify a digital terminal that you can route over the
 PXI backplane.
- For analog triggers, you can specify a channel or an analog terminal on the DAQ device
 that you are acquiring from.

##### Trigger Status

Use the trigger status icon to
 determine the current state of a triggered acquisition. The trigger status icon is located
 to the right of the Run or the Stop button. The icon only
 appears when you set the trigger mode to Start or
 Reference.

| Icon | Status | Description |
| --- | --- | --- |
|  | Triggered | The device met the trigger condition and began an acquisition that is based on the specified trigger settings. |
|  | Stopped | Acquisition is stopped on the device. |
|  | Waiting | The device is waiting to start an acquisition until the trigger condition occurs. |

##### Reference Trigger Settings

When a reference-triggered acquisition ends, the graph
 displays a finite number of samples before and after the trigger. You can change the number
 of displayed samples by setting the values of the Pretrigger samples
 and the Samples to read fields.

The Pretrigger
 samples field determines the number of acquired samples that InstrumentStudio
 displays before the trigger occurs. The Samples to
 Read−Pretrigger Samples formula
 determines the number of acquired samples that InstrumentStudio displays after the trigger
 occurs.

##### Digital Edge Trigger Settings

You can set the Edge setting to one of the following
 options:

Rising

Falling

##### Analog Edge Trigger Settings

You can configure the level, slope, and hysteresis values of analog edge
 triggers.

###### Level

You can configure the value of the Level field to
 specify the signal level at which the trigger occurs.

When the trigger source is a
 channel, the trigger level has the same unit of measurement as the channel.

When the
 trigger source is an analog terminal, the trigger level always has volts as the unit of
 measurement.

###### Slope

Slope

Rising

Falling

###### Hysteresis

You can configure the value of the Hysteresis
 field to ensure that signal noise does not cause unwanted triggers.

A rising slope
 trigger is valid when the source signal passes below
 Level−Hysteresis,
 then passes above the Level value.

A falling slope trigger is
 valid when the source signal passes above
 Level+Hysteresis,
 then passes below the Level value.

##### Analog Window Trigger Settings

You can configure the window mode and the window limits of analog window
 triggers.

###### Window
 Mode

Window mode

Entering

Leaving

###### Window
 Limits

The values of the Bottom and the
 Top fields specify the two signal levels that define the
 window.

#### Channel Settings

You can configure various settings, such as signal types and input limits for DAQ
 Analog Input devices.

##### Channel
 Names

The Name setting specifies a display name or alias
 for the channel. To modify the channel name, click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button to open the Channel Settings window.

The
 physical channel name (for example, PXI1Slot3/ai0) appears at the top of
 the Channel Settings window.

##### Signal
 Types and Sensor Types

Signal type

Signal type

- Click the button to open the Channel Settings window.
- Select the dropdown menu that is in on the right of the channel name.

- Electrical
- Temperature
- Bridge
- Integrated Electronics Piezoelectric (IEPE) and Charge
- Position

Note

Idle

| Signal Type | Description |
| --- | --- |
| Charge | Measures electrical charge. |
| Current | Measures electrical current. |
| Custom voltage with excitation | Measures voltage or bridge ratios with DC voltage excitation. |
| Resistance | Measures electrical resistance. |
| Voltage | Measures electrical potential. |

| Signal Type | Description |
| --- | --- |
| Temperature (RTD) | Measures temperature with a resistance temperature detector (RTD). |
| Temperature (thermistor) | Measures temperature with a thermistor. |
| Temperature (thermocouple) | Measures temperature with a thermocouple. |

| Signal Type | Description |
| --- | --- |
| Force (bridge) | Measures force with a load cell. |
| Pressure (bridge) | Measures pressure with a bridge-based pressure sensor. |
| Strain | Measures strain with a strain gauge. |
| Torque (bridge) | Measures torque with a bridge-based torque sensor. |

| Signal Type | Description |
| --- | --- |
| Acceleration (charge) | Measures acceleration with a piezeoelectric accelerometer in charge mode. |
| Acceleration (IEPE) | Measures acceleration with an IEPE accelerometer. |
| Acceleration (4 wire DC voltage) | Measures acceleration with an accelerometer that uses DC voltage excitation. |
| Force (IEPE) | Measures dynamic force with an IEPE load cell or impact hammer. |
| Sound pressure (IEPE) | Measures sound pressure with an IEPE accelerometer. |
| Velocity (IEPE) | Measures dynamic velocity or vibration with an IEPE velocity transducer. |

| Signal Type | Description |
| --- | --- |
| Angular position (RVDT) | Measures angular position with a Rotary Variable Differential Transformer (RVDT). |
| Linear position (LVDT) | Measures linear position with a Linear Variable Differential Transformer (LVDT). |
| Proximity (eddy current) | Measures relative proximity with an eddy current proximity probe. |

By default, the signal type of the first channel is set to a device-specific
 default type. The signal type of the remaining channels is set to
 Idle.

To enable more channels, change their Signal
 type setting to the desired signal type. To disable channels, change their
 Signal type setting to Idle.

To show or hide
 idle channels, click the [IMAGE alt='An icon of an eye.' src='GUID-6A8C4C24-217E-4CDB-AB57-B346986D07F8-a5.png'] button that is in the upper-right corner of the graph. Then check or clear the
 checkbox under Show»Idle channels.

##### Input
 Limits, Units, and Hardware Range

You can specify the expected signal range for a
 channel by setting the values of the Minimum and the
 Maximum fields. These values are specified in units that are
 appropriate for the selected signal type.

1. Click the button to open the Channel Settings window.
2. Select a unit of measurement from the Units dropdown menu.

NI-DAQmx chooses the hardware range that best matches the input limits and other
 sensor settings. The Hardware range field displays the chosen range
 in electrical units such as volts, V/V, or ohms.

##### Signal-Specific Settings

To configure signal-specific settings, click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button to open the Channel Settings window.

For
 certain signal types, the front panel displays signal-specific read-only indicators. These
 indicators show the configuration of the channel.

1. Click the button on the right side of the channel pane.
2. Set View mode to Compact .

To unhide these characteristics, set View mode to
 Default.

##### Readback
 Display

Below the input limits and signal-specific indicators, each channel
 displays a readback of the sample that the channel most recently acquired.

##### Configure Multiple Channels

1. Click the button to open the Channel Settings window. Note You can configure multiple channels even if you open the
 Channel Settings window by clicking the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button. Use ctrl+click,
 shift+click, or ctrl+A to select
 multiple channels.
2. Configure the settings that the right side of the Channel
 Settings window displays. The window only displays the settings that the
 selected channels share.

If a setting has different, non-conflicting values on different channels, the
 control for that setting displays Mixed values.

If a setting has
 conflicting values on different channels, the control for that setting displays No
 common option. Conflicting values are, for example, a
 Units dropdown menu that displays Volt (V) for one
 channel and Ampere (A) for another channel.

##### Advanced
 and Device-Specific Settings

The Channel Settings window
 displays advanced settings, such as Coupling and Terminal
 configuration.

For certain devices, the Channel
 Settings window also displays device-specific settings, such as ADC
 timing mode or Filter frequency.

<!--NI_TOPIC bundle=instrumentstudio path=daq-analog-output.html language=enus -->
## TOPIC 00012: DAQ Analog Output Devices

- bundle_id: `instrumentstudio`
- source_path: `daq-analog-output.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/daq-analog-output.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQ Analog Output panel to configure timing, trigger, and channel settings for your DAQ Analog Output instruments. Timing Settings By default, InstrumentStudio manages timing settings automatically based on the trigger settings and the channel settings. You can also configure timing settings

### DAQ Analog Output Devices

Use the DAQ Analog Output panel to configure timing, trigger, and channel settings for
 your DAQ Analog Output instruments.

Parent topic:

Configure Device Settings

#### Timing Settings

By default, InstrumentStudio manages timing settings automatically based on the trigger
 settings and the channel settings. You can also configure timing settings manually.

To configure timing settings manually, click the blue icon to the right of the
 Mode dropdown menu. The following sections describe the effect of
 configuring each setting.

##### Timing
 Mode

Mode

Continuous

Finite

Software

##### Sample Rate

You can only configure the
 Sample rate setting in the Continuous and the
 Finite timing modes.

The Sample rate setting
 defines the desired sample clock rate, which sets the time interval between
 samples.

The sample rate that you set must match one of the supported rates for your
 DAQ device. If you set the sample rate to an unsupported value, NI-DAQmx automatically
 changes the sample rate to a supported value. The Actual sample rate
 field shows the changed sample rate value.

##### Samples
 per Channel

You can only configure the Samples per channel
 setting in the Continuous and the Finite timing
 modes.

Samples per channel

Continuous

Finite

#### Trigger Settings

You can configure the mode, the type, and the source of the trigger on the instrument
 panel.

##### Trigger
 Mode

Mode

None

Run

Stop

Start

Run

##### Trigger
 Type

Type

Digital Edge

Digital Edge
 Trigger Settings

Analog Edge

Analog Edge Trigger Settings

Analog Window

Analog Window
 Trigger Settings

Note

Specifications

ni.com/docs

##### Trigger Source

Source

- For digital triggers, you can specify a digital terminal on the DAQ device that you
 are acquiring from. You can also specify a digital terminal that you can route over the
 PXI backplane.
- For analog triggers, you can specify a channel or an analog terminal on the DAQ device
 that you are acquiring from. DAQ analog output panels do not support triggering on an
 analog input channel.

##### Trigger
 Status

Use the trigger status icon to determine the current state of a triggered
 generation. The trigger status icon is located to the right of the Run or
 the Stop button. The icon only appears when you set the trigger mode to
 Start.

| Icon | Status | Description |
| --- | --- | --- |
|  | Generating | The device met the trigger condition and began a generation that is based on the specified trigger settings. |
|  | Stopped | Generation is stopped on the device. |
|  | Waiting | The device is waiting to start a generation until the trigger condition occurs. |

##### Digital Edge Trigger Settings

You can set the Edge setting to one of the following
 options:

Rising

Falling

##### Analog Edge Trigger Settings

You can configure the level, slope, and hysteresis values of analog edge
 triggers.

###### Level

You can configure the value of the Level
 field to specify the signal level at which the trigger occurs.

###### Slope

Slope

Rising

Falling

###### Hysteresis

You can configure the value of the Hysteresis
 field to ensure that signal noise does not cause unwanted triggers.

A rising slope
 trigger is valid when the source signal passes below
 Level−Hysteresis,
 then passes above the Level value.

A falling slope trigger is
 valid when the source signal passes above
 Level+Hysteresis,
 then passes below the Level value.

##### Analog Window Trigger Settings

You can configure the window mode and the window limits of analog window
 triggers.

###### Window
 Mode

Window mode

Entering

Leaving

###### Window
 Limits

The values of the Bottom and the
 Top fields specify the two signal levels that define the
 window.

#### Channel Settings

You can configure various settings, such as signal types and output limits for DAQ
 Analog Output devices.

##### Channel
 Names

The Name setting specifies a display name or alias
 for the channel. To modify the channel name, click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button to open the Channel Settings window.

The
 physical channel name (for example, PXI1Slot3/ao0) appears at the top of
 the Channel Settings window.

##### Signal
 Types

Signal type

- Click the button to open the Channel Settings window.
- Select the dropdown menu that is in on the right of the channel name.

Current

[IMAGE alt='The letter A, representing current.' src='GUID-A3164B3E-E243-4839-B035-4B054D6BDCA7-a5.png']

Voltage

[IMAGE alt='The letter V, representing voltage.' src='GUID-1D32F9EB-F9CA-4400-A857-A66206A85F49-a5.png']

Note

Idle

By default, the
 signal type of the first channel is set to a device-specific default type. The signal type
 of the remaining channels is set to Idle.

To enable more channels,
 change their Signal type setting to the desired signal type. To
 disable channels, change their Signal type setting to
 Idle.

To show or hide idle channels, click the [IMAGE alt='An icon of an eye.' src='GUID-6A8C4C24-217E-4CDB-AB57-B346986D07F8-a5.png'] button that is in the upper-right corner of the graph. Then check or clear the
 checkbox under Show»Idle channels.

##### Output
 Limits, Units, and Hardware Range

You can specify the expected signal range for a
 channel by setting the values of the Minimum and the
 Maximum fields. These values are specified in units that are
 appropriate for the selected signal type.

NI-DAQmx chooses the hardware range that
 best matches the output limits. The Hardware range field displays the
 chosen range in volts or amperes.

##### Waveform
 Settings

Waveform type

Waveform type

- Constant DC ( ) Note Voltage or current, depending on the signal
 type.
- Sine ( )
- Square ( )
- Triangle ( )
- Sawtooth ( )
- Inverted Sawtooth ( )

By default, the waveform type of each channel is set to Constant
 DC ([IMAGE alt='A continuous line over a segmented line that represents the constant DC waveform type.' src='GUID-B1ED457A-04EC-4A3F-8B26-B2F25AA3D9B6-a5.png']).

##### Waveform-Specific Settings

You can configure waveform-specific settings for the different waveform
 types.

To configure waveform-specific settings, click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button to open the Channel Settings window.

For certain waveform types, the front panel displays signal-specific read-only
 indicators. These indicators show the configuration of the channel.

1. Click the button on the right side of the channel pane.
2. Set View mode to Compact .

To unhide these characteristics, set View mode to
 Default.

###### Constant DC Waveform Settings

You can configure the
 Offset setting to specify the voltage or current that the
 device outputs.

###### Standard Waveform Settings

- Sine ( )
- Square ( )
- Triangle ( )
- Sawtooth ( )
- Inverted Sawtooth ( )

Amplitude

Frequency

Note

InstrumentStudio configures the DAQ device to continuously
 regenerate data in the output buffer.

Certain timing settings and output buffer sizes might prevent
 InstrumentStudio from generating the desired frequency. In this
 case, InstrumentStudio automatically selects the closest
 possible frequency. You can see this frequency in the
 Actual frequency indicator. If the
 difference between the desired frequency and the actual
 frequency exceeds 10%, InstrumentStudio displays an error.

Offset

Phase

###### Square Waveform Settings

For Square waveforms ([IMAGE alt='A square wave that represents the square wave waveform type.' src='GUID-65007794-E9B9-4321-87EA-51E17DF9D585-a5.png']), you can open the Channel Settings window ([IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png']) to configure the Duty cycle setting. This setting
 specifies the percentage of the waveform period where the square wave outputs
 high.

###### Waveform Preview

The Waveform preview graph shows
 a preview of the waveforms that InstrumentStudio generates with the configured
 timing settings and channel settings. When you change a setting, the preview graph
 updates. This update occurs whether or not the panel is generating
 data.

###### Configure Multiple Channels

1. Click the button to open the Channel Settings 
 window. Note You can configure multiple channels
 even if you open the Channel Settings window by
 clicking the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button. Use ctrl+click,
 shift+click, or ctrl+A
 to select multiple channels.
2. Configure the settings that the right side of the Channel
 Settings window displays. The window only displays the
 settings that the selected channels share.

If a setting has different, non-conflicting values on different
 channels, the control for that setting displays Mixed
 values.

If a setting has conflicting values on different channels,
 the control for that setting displays No common option. Conflicting
 values are, for example, a Signal type dropdown menu that
 displays Voltage ([IMAGE alt='The letter V, representing voltage.' src='GUID-1D32F9EB-F9CA-4400-A857-A66206A85F49-a5.png']) for one channel and Current ([IMAGE alt='The letter A, representing current.' src='GUID-A3164B3E-E243-4839-B035-4B054D6BDCA7-a5.png']) for another channel.

<!--NI_TOPIC bundle=instrumentstudio path=debug-c-cplus-net.html language=enus -->
## TOPIC 00013: Enable Debugging with a C, C++, or .NET Application

- bundle_id: `instrumentstudio`
- source_path: `debug-c-cplus-net.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/debug-c-cplus-net.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable debugging with C, C++, and .NET applications in the Configure Debug Session window. Supporting communication with a device in C, C++, or .NET environments at breakpoints requires additional overhead that might affect performance. Select Configure debug session from the instrument settings men

### Enable Debugging with a C, C++, or .NET
 Application

Enable debugging with C, C++, and .NET applications in the Configure Debug
 Session window.

Note

1. Select Configure debug session from the instrument settings menu
 ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']). 
 The Configure Debug Session window opens.
2. Fill the Using Breakpoints in C/C++/.NET Applications checkbox
 next to the device that you want to debug.
3. Click OK. 
 InstrumentStudio enables breakpoints in C, C++, and .NET external
 applications.
4. Debug the application or device.
5. When you finish debugging, clear the Using Breakpoints in C/C++/.NET
 Applications checkbox in the Configure Debug Session
 window.
6. Restart the external application to apply the changes.

Parent topic:

Debug Programmatic Applications

<!--NI_TOPIC bundle=instrumentstudio path=debug-limitations.html language=enus -->
## TOPIC 00014: Limitations of Debug Mode

- bundle_id: `instrumentstudio`
- source_path: `debug-limitations.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/debug-limitations.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Debug mode has limitations when used with waveform generators and RF signal generators. Waveform Generator Debug Mode Limitations When you use debug mode with a waveform generator, consider the following limitations: Debug mode does not support arbitrary sequence mode or script mode. You cannot cont

### Limitations of Debug Mode

Debug mode has limitations when used with waveform generators and RF signal
 generators.

#### Waveform Generator Debug Mode
 Limitations

When you use debug mode with a waveform generator, consider the following
 limitations:

- Debug mode does not support arbitrary sequence mode or script mode. You cannot control
 arbitrary sequence mode or script mode sessions.
- List mode control is disabled when InstrumentStudio is in Monitor mode
 or Control mode.
- When InstrumentStudio is in Control mode, you cannot switch to list
 mode or sweep mode from another operation mode.
- When InstrumentStudio is in Monitor mode, you cannot take control of a
 panel with a mix of standard and arbitrary waveform channels.

For more information on Monitor and Control modes,
 see *Monitor and Control Devices Used in an External Session*.

#### RF Signal Generator Debug Mode
 Limitations

When you use debug mode with an RF signal generator, consider the following
 limitations:

- You cannot take control of an RF signal generator panel in the following cases:
  - Streaming is enabled
  - An active configuration list is present
- You cannot return to script mode after you click the Preset 
 button.
- Waveform-specific controls are read-only in Script mode.

Parent topic:

Debug Programmatic Applications

Related tasks:

- Monitor and Control Devices Used in an External Session

<!--NI_TOPIC bundle=instrumentstudio path=debug-monitor-control.html language=enus -->
## TOPIC 00015: Monitor and Control Devices Used in an External Session

- bundle_id: `instrumentstudio`
- source_path: `debug-monitor-control.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/debug-monitor-control.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You must enable debug mode to access the Monitor button and Control button. Select Monitor. InstrumentStudio obtains read-only access to the external session. InstrumentStudio also disables the controls of the device. You are now monitoring the device. Select Control. InstrumentStudio takes control

### Monitor and Control Devices Used in an
 External Session

You must enable debug mode to access the Monitor button and
 Control button.

1. Select Monitor. 
 InstrumentStudio obtains read-only access to the external session.
 InstrumentStudio also disables the controls of the device. You are now monitoring the
 device.
2. Select Control. 
 InstrumentStudio takes control of the device if an external application is not
 currently accessing the device. If you select Control,
 InstrumentStudio takes ownership of the device in the following cases:You are not monitoring any external application sessions.
 The external application is paused.Note 
 When you select Control, InstrumentStudio takes control of the
 device only until the external application calls the device again. Afterwards, the
 external application takes control of the device and InstrumentStudio returns to
 monitoring the session.
 You can use breakpoints to pause the external application. Pausing the external
 application allows InstrumentStudio to retain control of the device until you made
 your changes.
3. Edit the device settings.
4. Click Monitor to return to monitoring the session and return
 control of the device to the external session. 
 InstrumentStudio applies the updated device settings to the external
 session.

Parent topic:

Debug Programmatic Applications

<!--NI_TOPIC bundle=instrumentstudio path=debugging.html language=enus -->
## TOPIC 00016: Debug Programmatic Applications

- bundle_id: `instrumentstudio`
- source_path: `debugging.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/debugging.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the debug mode in InstrumentStudio to monitor and control devices that are in use by an external application. You can use InstrumentStudio to troubleshoot devices that are currently in use by an external application. An external application is an application that runs outside of InstrumentStudio

### Debug Programmatic Applications

Use the debug mode in InstrumentStudio to monitor and control devices that are in use
 by an external application.

- LabVIEW
- TestStand
- C, C++, or .NET applications

If you receive unexpected results from a device in an external application, you can monitor
 the device in InstrumentStudio. You can assess and troubleshoot the issue by changing the
 device settings in InstrumentStudio, then continue with the external application. For example,
 you can pause the external application where you suspect an error and edit the device settings
 in InstrumentStudio. Then, you can resume the application with the new settings.

Note

- InstrumentStudio does not support debugging
 features when using sweep mode in an SMU (Source Measure Unit) panel.
- When monitoring a device in debug mode,
 InstrumentStudio establishes a connection to the device session in the external
 application, not the device itself. Therefore, InstrumentStudio only monitors data that it
 fetches or reads from the external application that currently runs.

The following sections provide specific information on how to use debug mode in
 InstrumentStudio:

- [Limitations of Debug Mode](debug-limitations.html) Debug mode has limitations when used with waveform generators and RF signal generators.
- [Enter Debug Mode](enable-debug.html) InstrumentStudio has debug mode enabled by default. You can enter debug mode from the Home screen by selecting Debug .
- [Enable Debugging with a C, C++, or .NET Application](debug-c-cplus-net.html) Enable debugging with C, C++, and .NET applications in the Configure Debug Session window.
- [Monitor and Control Devices Used in an External Session](debug-monitor-control.html) You must enable debug mode to access the Monitor button and Control button.
- [Live Measurement View](live-measurement-view.html) When you monitor SMU/VPS devices in debug mode, InstrumentStudio automatically displays measurements of channel data in real time. InstrumentStudio displays this data even if external applications are not currently fetching device data.
- [Disable Debugging](disable-debug.html) You can disable debugging for individual devices in the Configure Debug Session window.

<!--NI_TOPIC bundle=instrumentstudio path=device-synchronization.html language=enus -->
## TOPIC 00017: Synchronize Devices

- bundle_id: `instrumentstudio`
- source_path: `device-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/device-synchronization.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: InstrumentStudio supports a variety of synchronization options for different panels. In InstrumentStudio, device synchronization falls under the following categories: Software Hardware Software Synchronization Hardware Synchronization An icon with three signals with different peaks and timings. An i

### Synchronize Devices

InstrumentStudio supports a variety of synchronization options for different
 panels.

- Software
- Hardware

| Software Synchronization | Hardware Synchronization |
| --- | --- |
|  |  |
| Channel acquisition and generation is sequenced in software. | Channel acquisition and generation is sequenced in hardware. |
| There is no strict timing guarantee between channels. | There is strict timing guarantee between channels. |

#### Panel Synchronization

- Digital multimeters (DMMs)
  - All channels are always software-synchronized.
- Waveform generators Note Channels within a 2-channel PXIe-5450 or
 PXIe-5451 waveform generator are always hardware-synchronized.
  - All channels are software-synchronized by default.
- Oscilloscopes
  - All channels on a single device are always hardware-synchronized.
  - All channels in a single panel are hardware-synchronized if every device is the
 same model and every device is in the same chassis. Channels across different
 physical devices are synchronized with NI-TClk technology.
  - You can trigger an oscilloscope from another instrument in the system. To do so,
 you must configure a digital trigger and select the source according to the device
 name.
- SMU and VPS devices
  - Every channel that you configure for a sequence or for pulse generation within a
 single SFP is automatically hardware-synchronized. You can configure routing options
 by clicking the icon.
  - Channels are software-synchronized ( ) in all other cases.
  - You can trigger an SMU from another instrument in the system. To do so, you must
 configure a digital trigger and select the source according to the device name.
- RF Signal Generators (RFSGs), RF Signal Analyzers (RFSAs), and Network Analyzers
- 
  - You can only have one device in a single panel.
  - You cannot synchronize devices.

Parent topic:

Configure Panels and Layouts

<!--NI_TOPIC bundle=instrumentstudio path=disable-debug.html language=enus -->
## TOPIC 00018: Disable Debugging

- bundle_id: `instrumentstudio`
- source_path: `disable-debug.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/disable-debug.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can disable debugging for individual devices in the Configure Debug Session window. Select Configure debug session from the instrument settings menu ( A cogwheel icon for the instrument settings menu of InstrumentStudio. ). The Configure Debug Session window opens. Clear the Debug Enabled checkb

### Disable Debugging

You can disable debugging for individual devices in the Configure Debug
 Session window.

1. Select Configure debug session from the instrument settings menu
 ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']). 
 The Configure Debug Session window opens.
2. Clear the Debug Enabled checkbox to disable debugging for a
 specific device.
3. Click OK.
4. Restart the external application to apply the changes.

Debugging is disabled for the specified
 device. This device cannot enter debug mode until debugging is enabled again.

Parent topic:

Debug Programmatic Applications

<!--NI_TOPIC bundle=instrumentstudio path=dmm.html language=enus -->
## TOPIC 00019: Digital Multimeters (DMMs)

- bundle_id: `instrumentstudio`
- source_path: `dmm.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/dmm.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Digital Multimeter panel to configure ranging modes and perform cable compensation for your Digital Multimeter instruments. Auto Range Modes Auto range modes automatically detect the signal range when the range for a signal is unknown. Auto range modes allow you to measure a signal when you

### Digital Multimeters (DMMs)

Use the Digital Multimeter panel to configure ranging modes and perform cable
 compensation for your Digital Multimeter instruments.

Parent topic:

Configure Device Settings

#### Auto Range Modes

Auto range modes automatically detect the signal range when the range for a signal is
 unknown.

Auto

[IMAGE alt='A blue icon with a dot in the middle and two curved arrows that form a circle.' src='GUID-502D20E6-E96D-41E4-94D2-21243F292161-a5.png']

Auto once

[IMAGE alt='A blue icon with a the number one in the middle and two curved arrows that form a circle.' src='GUID-6D4CAFCA-B2BB-4A37-8F13-3F9889BE21A2-a5.png']

Auto range modes allow the DMM to take a series of measurements. Then, the DMM adjusts the
 range until the measurement falls within the smallest range appropriate for that
 measurement.

Note

NI-DMM User Manual

User Manual

Related information:

- NI Digital Multimeters

##### Enable Automatic Level Range

Complete the following steps to enable automatic level ranging:

1. Click [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] to open the Channel Settings
 window.
2. Enable one of the auto range modes in the
 Range section of the
 window.
  - Click the icon to enable Auto 
 mode.
  - Click the icon to enable Auto once 
 mode.

[IMAGE alt='A blue icon with a dot in the middle and two curved arrows that form a circle.' src='GUID-502D20E6-E96D-41E4-94D2-21243F292161-a5.png']

[IMAGE alt='A blue icon with a the number one in the middle and two curved arrows that form a circle.' src='GUID-6D4CAFCA-B2BB-4A37-8F13-3F9889BE21A2-a5.png']

To disable an auto range mode, click the blue icon
 or select the other auto range mode.

Related reference:

- Export Configurations

#### Perform Cable Compensation

When you connect a DMM to a DUT with switches, fixtures, or cables, these instruments
 might introduce errors into the measurement. Open and short cable compensation minimizes these
 measurement errors when you take capacitance or inductance measurements.

- Measuring the error
- Applying the measured error to the actual measurement

none

##### Perform Open Compensation for
 Capacitance Measurements and Inductance Measurements

1. Disconnect the DUT from the DMM at the connection point on the DUT. Leave the cable
 connected to the DMM.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Open the settings ( ) for the DMM channel.
4. Click Renew under the Open cable
 compensation section of the settings window. Note These settings are not available for
 simulated DMM devices.
5. Click Continue in the Open Cable
 Compensation dialog box. Note Check the device panel. InstrumentStudio
 applied the compensation if the [IMAGE alt='An icon of a plug with a checkmark in the upper-right corner.' src='GUID-24E798F3-89E6-4D5E-BA29-94D9771A0A1E-a5.png'] symbol appears.

##### Perform Short Compensation for
 Capacitance Measurements and Inductance Measurements

1. Disconnect the DUT from the DMM at the connection point on the DUT. Leave the cable
 connected to the DMM.
2. Configure the DMM for capacitance or inductance at the desired range.
3. Set up a short condition with a low-impedance connection between the
 HI terminal and the LO terminal of the
 DMM. Use cables and switches with low capacitance and low path resistance.
4. Open the settings ( ) for the DMM channel.
5. Click Renew under the Short cable
 compensation section of the settings window. Note These settings are not available for
 simulated DMM devices.
6. Click Continue in the Short Cable
 Compensation dialog box. Note Check the device panel.
 InstrumentStudio applied the compensation if the [IMAGE alt='An icon of a plug with a checkmark in the upper-right corner.' src='GUID-24E798F3-89E6-4D5E-BA29-94D9771A0A1E-a5.png'] symbol appears.

<!--NI_TOPIC bundle=instrumentstudio path=edit-layout.html language=enus -->
## TOPIC 00020: Configure Panels and Layouts

- bundle_id: `instrumentstudio`
- source_path: `edit-layout.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/edit-layout.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections provide specific information on how to use the panels and layouts in InstrumentStudio:

### Configure Panels and Layouts

The following sections provide specific information on how to use the panels and
 layouts in InstrumentStudio:

- [Panels and Layouts](panels-and-layouts.html) An InstrumentStudio layout consists of one large panel and up to four small panels.
- [Create and Edit a Layout](creating-layout.html#GUID-B1C8E40E-84FD-484D-B688-D40808781C99) Before you can take measurements and monitor devices in InstrumentStudio, you must create a layout. You can create a layout from the Home screen, from the instrument header menu, or from any instrument settings menu ( ).
- [Configure Panels with the Instrument Settings Menu](instrument-settings-menu.html) The instrument settings menu ( ) in InstrumentStudio offers options for data management, device configuration, and panel controls.
- [Relink or Replace Missing Devices](missing-devices.html) Use relinking to re-establish a connection to a missing device. You can also use relinking to replace the missing device with a different device of the same model in an existing panel.
- [Synchronize Devices](device-synchronization.html) InstrumentStudio supports a variety of synchronization options for different panels.
- [Configure Remote RF Signal Analyzer Panels](remote_panel.html) You can add a remote RF signal analyzer panel to your project to use remote RFmx hardware.
- [SCPI Instrument Panels](scpi-panels.html#GUID-6C4CBAE3-F6FF-4F97-B400-213A284A1863) Use SCPI instrument panels to fetch data, take screenshots, and manage SCPI configuration.

<!--NI_TOPIC bundle=instrumentstudio path=edit-pin-map.html language=enus -->
## TOPIC 00021: Edit a Pin Map

- bundle_id: `instrumentstudio`
- source_path: `edit-pin-map.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/edit-pin-map.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Pin Map Editor to make changes to a project pin map. Double-click a pin map (.pinmap) in the project files pane to open the Pin Map Editor. Make the desired changes to your instruments, connections, and pins. Use the Pin map tab to view mappable items and change mappings. To manually change

### Edit a Pin Map

Use the Pin Map Editor to make changes to a project pin
 map.

1. Double-click a pin map (.pinmap) in the project files pane to open
 the Pin Map Editor.
2. Make the desired changes to your instruments, connections, and pins. 
 Use the Pin map tab to view mappable items and change mappings.
 To manually change the pin map file, click the XML tab.
3. Click OK to close the Pin Map
 Editor.

Parent topic:

Pin Maps

<!--NI_TOPIC bundle=instrumentstudio path=enable-debug.html language=enus -->
## TOPIC 00022: Enter Debug Mode

- bundle_id: `instrumentstudio`
- source_path: `enable-debug.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/enable-debug.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: InstrumentStudio has debug mode enabled by default. You can enter debug mode from the Home screen by selecting Debug. When you enter debug mode, InstrumentStudio searches for open device driver sessions. Then, based on the result of this search, InstrumentStudio creates a new layout. The devices in

### Enter Debug Mode

InstrumentStudio has debug mode enabled by default. You can enter debug mode from the
 Home screen by selecting Debug.

When you enter debug mode, InstrumentStudio searches for open device driver sessions. Then,
 based on the result of this search, InstrumentStudio creates a new layout. The devices in the
 newly created layout automatically enter debug mode.

- The device is placed in a layout
- The device is already part of an active layout

Take, for example, a scenario where you run an oscilloscope in an InstrumentStudio panel
 alongside a LabVIEW application that acquires measurements from that oscilloscope. In this
 case, the InstrumentStudio panel enters debug mode until the LabVIEW application (the external
 session using the oscilloscope) closes.

Devices that are currently in use by an external application display the external session
 icon ([IMAGE alt='Icon of a play button and a check mark that represents an external session.' src='GUID-A366B20D-AAD4-451D-BE1B-1AFC5AA84ED4-a5.gif']) in the Edit Layout window.

Note

1. Select Configure debug session from the instrument settings menu
 ( ). The Configure Debug Session window opens.
2. Fill the Configure Debug Session checkbox next to the device that
 you want to debug.
3. Click OK .

Configure Debug Session

Parent topic:

Debug Programmatic Applications

<!--NI_TOPIC bundle=instrumentstudio path=enabling-preview-features.html language=enus -->
## TOPIC 00023: Enable Preview Features

- bundle_id: `instrumentstudio`
- source_path: `enabling-preview-features.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/enabling-preview-features.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Preview features are new features in InstrumentStudio that support specific workflows. Preview features are not release-quality features, and might have functionality gaps. You must enable preview features in the Preferences menu. Go to File Preferences Preview Features . This menu is only visible i

### Enable Preview Features

Preview features are new features in InstrumentStudio that support specific workflows.
 Preview features are not release-quality features, and might have functionality gaps. You
 must enable preview features in the Preferences menu.

1. Go to File»Preferences»Preview Features.

Note

1. Click the toggle to enable the preview features that you want to use.
2. Close the Preferences panel.
3. Restart InstrumentStudio.

Parent topic:

Navigating InstrumentStudio

<!--NI_TOPIC bundle=instrumentstudio path=exec-seq.html language=enus -->
## TOPIC 00024: Execute a Sequence

- bundle_id: `instrumentstudio`
- source_path: `exec-seq.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/exec-seq.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Executing a sequence performs all the steps that are defined in the sequence. When the sequence ends, you can view the data that InstrumentStudio measured during the sequence. You can also view the sequence report to ensure that the sequence executed all defined steps successfully. Before you execut

### Execute a Sequence

Executing a sequence performs all the steps that are defined in the sequence. When the
 sequence ends, you can view the data that InstrumentStudio measured during the
 sequence. You can also view the sequence report to ensure that the sequence executed
 all defined steps successfully.

Before you execute a sequence, ensure that
 all required devices in your system are present, connected, and powered
 on.

Run

The timer in the sequencer pane starts, which indicates that the
 sequence is actively executing.

Note

Sequence Results

Sequence Results

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=export-config.html language=enus -->
## TOPIC 00025: Export Configurations

- bundle_id: `instrumentstudio`
- source_path: `export-config.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/export-config.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can export device configurations to different applications, such as LabVIEW and TestStand. Limitations of Exporting a Device Configuration You cannot export a configuration that includes a waveform generator with the following waveform characteristics: Standard waveforms with the List or the Swe

### Export Configurations

You can export device configurations to different applications, such as LabVIEW and
 TestStand.

Parent topic:

Configure Device Settings

#### Limitations of Exporting a Device
 Configuration

You cannot export a configuration that includes a waveform generator with the following
 waveform characteristics:

- Standard waveforms with the List or the Sweep operation
 mode.
- Standard waveforms of the User-defined waveform mode.
- Arbitrary waveforms that you create from a .csv waveform file.

#### Export a Device Configuration

After you configure a device in InstrumentStudio, you can export that configuration to
 a device configuration file. You can then import that configuration file to LabVIEW or another
 application to apply the device configuration to a different session.

1. Configure the device.
2. Open the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']).
3. Select Export»Driver configuration...
4. Select the location to save the configuration file.

#### Import a Device Configuration

You cannot import a device configuration file into InstrumentStudio. If you want to
 save a layout or a device configuration for future use in InstrumentStudio, complete one of the
 following actions:

- Save the entire project by clicking File»Save all .
- Save the soft front panel of the device by clicking File»Save [device name].sfp .

To apply device settings from a device configuration file to a device session in LabVIEW, you
 must import the device configuration file to LabVIEW. To import the configuration file, use
 the Import Attribute Configuration LabVIEW VI. The implementation of the
 Import Attribute Configuration VI is driver-specific. For more
 information, see the appropriate driver documentation in the *Related Information*
 section.

Related information:

- NI-SCOPE Import Attribute Configuration File
- NI-DCPower Import Attribute Configuration File
- NI-DMM Import Attribute Configuration File
- NI-FGEN Import Attribute Configuration File

#### Export Configurations to TestStand

You can export configurations to save time when you automate test sequences in
 TestStand.

After you configure your hardware in InstrumentStudio, you can export your configuration for
 use in TestStand sequences. You can export device and panel configurations to recent and
 supported 64-bit versions of TestStand. You can then use these configurations with LabVIEW,
 C#, C, or CVI automation code in a TestStand sequence.

#### Export an InstrumentStudio
 Configuration

You can use InstrumentStudio to create an IO configuration file. This IO file contains
 the driver configuration and the panel layout from InstrumentStudio.

- Use a recent and supported 64-bit version of TestStand.
- Instrument channels that you want to include in the export are not in the
 Idle operation mode. InstrumentStudio does not export the configuration
 of instrument channels in the Idle operation mode.
- Select a specific site in the site filter, or select the System
 pins option to only export system pins. You cannot export an
 InstrumentStudio configuration if you select the All sites option
 in the site filter.

You can configure the default format of the exported file name by selecting File»Preferences and navigating to the Export to TestStand
 section.

1. From the top toolbar or the instrument header menu, select the Export to
 TestStand button ([IMAGE alt='An icon of checkmark that exports settings to TestStand from InstrumentStudio.' src='GUID-D8F0E671-A332-48EF-9CFE-E5A4077ED5DC-a5.png']). 
 Note If the Export to
 TestStand ([IMAGE alt='An icon of checkmark that exports settings to TestStand from InstrumentStudio.' src='GUID-D8F0E671-A332-48EF-9CFE-E5A4077ED5DC-a5.png']) button does not appear, ensure that you have a recent and supported version of
 TestStand installed.
2. Specify a name for the exported configuration.

InstrumentStudio now creates an IO configuration file. The IO
 file contains the driver configuration and the panel layout from InstrumentStudio.

#### Insert an InstrumentStudio Configuration in
 a TestStand Sequence

You can insert your IO configuration file as a step within a TestStand
 sequence.

When you insert an IO configuration file into a TestStand sequence, TestStand creates a
 copy of the configuration file. You can specify the step in which TestStand copies the
 configuration file. When you run the sequence, this step creates sessions for the
 InstrumentStudio-configured instruments. Then, TestStand applies the configuration to the
 new sessions.

- Pass a session from the local variable to automation code in Action 
 steps
- Apply a new configuration to an existing session

For more information on using TestStand, see *TestStand User Manual* in the
 *Related Information* section.

Related information:

- TestStand User Manual

#### Edit an Exported Configuration

You can edit an exported configuration in a specific TestStand step. The changes to the
 configuration commit back to the TestStand step or the IO configuration file that you
 edited.

1. Import an InstrumentStudio configuration to TestStand.
2. Navigate to the TestStand step that you want to edit.
3. Select Edit. 
 InstrumentStudio opens in Edit mode and displays the
 instrument panels in the same layout as the document you exported the configuration
 from.
4. Edit the configuration in InstrumentStudio.
5. Click OK.

<!--NI_TOPIC bundle=instrumentstudio path=extended-support-changes.html language=enus -->
## TOPIC 00026: Updates and Changes for InstrumentStudio Extended Support Versions

- bundle_id: `instrumentstudio`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/extended-support-changes.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in InstrumentStudio versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible

### Updates and Changes for InstrumentStudio Extended Support Versions

Browse updates and changes made in InstrumentStudio versions
 on extended support.

Note

Release Notes

Related information:

- Release Notes

#### 2025 Q2

April 2025

- All instrument panels can be upgraded without upgrading the corresponding driver of the instrument panel. InstrumentStudio 2025 Q2 supports the same driver versions that were supported by InstrumentStudio 2025 Q1.

##### Network Analyzer

- Added support for trace math.
- Added marker enhancements, including target search and continuous marker
 mode.
- Added auto-detection of orientation for electronic calibration.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Sequencer Tool
  - Added support for parameter sweeps in instrument
 steps.
  - Added support for SCPI instruments (third-party
 instruments) in sequences.

Related concepts:

- Sequencer Tool

#### 2025 Q1

January 2025

##### Network Analyzer

- Added support for markers.
- Added support for memory traces.

##### RF
 Signal Analyzer (RFmx)

Spectrum Analyzer

LTE

Bluetooth

##### RF Signal Generator

- Added the ability to change the active script while debugging test code in
 script mode.
- Added the ability to switch to CW (continuous waveform) or Arb (arbitrary
 waveform) mode while debugging test code in script mode.

##### Oscilloscope

- Enhanced monitoring support: vertical scaling updates automatically based on
 test program settings.
- Added support for all PXIe-5172 onboard timebase rates.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Sequencer Tool
  - Added support for the following native instrument types: You can now add these panels to sequences.
    - FGEN
    - SCOPE
    - SMU/VPS
  - Added support for parameter sweeps in measurement plug-in steps.
- Measurement Plug-Ins
  - Added support for parameter sweeps for measurement plug-ins.

<!--NI_TOPIC bundle=instrumentstudio path=grpc-remote-panel-config.html language=enus -->
## TOPIC 00027: Configuring a gRPC Server for Remote RF Signal Analyzer Panels in InstrumentStudio

- bundle_id: `instrumentstudio`
- source_path: `grpc-remote-panel-config.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/grpc-remote-panel-config.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a gRPC server to enable remote connections to RF signal analyzer hardware from InstrumentStudio. InstrumentStudio connects to RF signal analyzer hardware through a gRPC server. Configure the server on the system that hosts the hardware. The server configuration defines network access and c

### Configuring a gRPC Server for Remote RF Signal
 Analyzer Panels in InstrumentStudio

Configure a gRPC server to enable remote connections to RF signal analyzer hardware from
 InstrumentStudio.

InstrumentStudio connects
 to RF signal analyzer hardware through a gRPC server. Configure the
 server on the system that hosts the hardware. The server
 configuration defines network access and connection behavior.

To configure your system for remote RF signal analyzer panels, complete
 the following steps.

1. Go to the *NI grpc-device repository* on
 *github.com*.
2. Install the NI gRPC server on the computer that is connected to
 the hardware. Follow the instructions provided in the
 repository.
3. Go to the install location.
4. Open server_config.json in an
 editor.
5. Add the following parameter to the configuration file. 
 "code_readiness": "RestrictedRelease"
6. Modify the value of "address" from
 "[::1]" to
 "[::]". 
 This setting allows connections from all network
 interfaces.
7. Optional: 
 Modify the value of "port" in the
 configuration file. 
 Note The default value for
 "port" is
 31763.
 Set a specific number to use that port. You must
 specify this port when you connect from InstrumentStudio.
 Set "port" to
 0 to allow the server to assign a
 port automatically. The server displays the
 assigned port in the console output when the
 server starts. Specify the assigned port when you
 connect from InstrumentStudio.
8. Run the gRPC server. Follow the instructions provided in the
 repository. 
 The gRPC server starts and listens on the configured
 port. The server now accepts connections from InstrumentStudio.

InstrumentStudio can now
 connect to and control RF signal analyzer hardware through the
 configured gRPC server.

#### Valid gRPC Server
 Configuration File

The following example shows a valid configuration file.

```text
{
  "address": "[::]",
  "port": 31763,
  "security": {
    "server_cert": "",
    "server_key": "",
    "root_cert": ""
  },
  "code_readiness": "RestrictedRelease"
}
```

For more detailed information about server configuration and usage, see
 *NI grpc-device
 Repository*.

Parent topic:

Configure Remote RF Signal Analyzer Panels

Related information:

- NI grpc-device Repository

<!--NI_TOPIC bundle=instrumentstudio path=hosted-plugins.html language=enus -->
## TOPIC 00028: InstrumentStudio Plug-Ins

- bundle_id: `instrumentstudio`
- source_path: `hosted-plugins.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/hosted-plugins.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use InstrumentStudio to create and host application-specific plug-ins written in LabVIEW or C#. These plug-ins run together with the InstrumentStudio panels that are used to configure PXI instruments. A teal ribbon that signals that a feature is only available with an InstrumentStudio Profes

### InstrumentStudio Plug-Ins

You can use InstrumentStudio to create and host application-specific plug-ins written
 in LabVIEW or C#. These plug-ins run together with the InstrumentStudio panels that are used to
 configure PXI instruments.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

Plug-ins have a runtime configuration and an edit-time configuration. You can export a
 plug-in configuration to TestStand to use it in a measurement step. In this case, the runtime
 configuration is provided to the sequence as a variable. Both of these configurations persist
 when you save the project that contains the configurations.

You cannot create plug-ins from the File»New menu. For information on how to create InstrumentStudio plug-ins, see
 *InstrumentStudio Plug-Ins on GitHub* in the *Related Information*
 section.

- Saving and loading
- Resizing the window
- Pulling out tabs
- Exporting the session to TestStand
- Stopping all outputs with LabVIEW plug-ins

For examples of InstrumentStudio plug-ins, see *InstrumentStudio Plug-Ins on
 GitHub* in the *Related Information* section.

#### Limitations of Plug-In Support

The following limitations apply when you host plug-ins in InstrumentStudio:

- Hosting plug-ins that are created in C# requires Visual Studio 2019 or newer and .NET
 6.0.
- Plug-ins built in the 2022 Q3 or earlier versions of InstrumentStudio are not
 compatible. You must rebuild the plug-ins in a newer version of InstrumentStudio.
- You cannot use Measurement Studio controls when you host plug-ins that are
 created in C#.

Parent topic:

Plug-Ins

Related information:

- InstrumentStudio Plug-Ins on GitHub

<!--NI_TOPIC bundle=instrumentstudio path=installing-swproduct.html language=enus -->
## TOPIC 00029: Install InstrumentStudio

- bundle_id: `instrumentstudio`
- source_path: `installing-swproduct.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/installing-swproduct.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can install InstrumentStudio and its required dependencies through Package Manager or with an .iso file offline. When you install certain instrument drivers, such as NI-SCOPE or NI-DMM, InstrumentStudio gets automatically installed as well. Install InstrumentStudio Using Package ManagerTo instal

### Install InstrumentStudio

You can install InstrumentStudio and its required dependencies through Package Manager or
 with an .iso file offline.

Note

#### Install InstrumentStudio Using Package Manager

InstrumentStudio

1. Go to the InstrumentStudio Download Page .
2. Log in to ni.com with your NI user account.
3. Click the Download button to download the
 ni-instrumentstudio_<version.number>_online.exe 
 executable.
4. Run the executable that you downloaded.
5. Follow the instructions that Package Manager provides. Note During installation, Package Manager prompts you to install additional software. For
 information on recommended additional software, see [Recommended Additional Software](installing-swproduct.html#GUID-30EE605D-4048-46D8-98B2-71A3B3769978__GUID-7F23CBD8-A4AC-4772-861C-27DA49B0A1AE).
6. Restart your device when the installation process finishes.

Package Manager User Manual

Related
 Information

Note

#### Install
 InstrumentStudio Offline

When you install InstrumentStudio offline, the .iso file contains
 all required dependencies. Package Manager does not connect to the Internet to download and
 install InstrumentStudio and its dependencies.

InstrumentStudio

1. Go to the InstrumentStudio Download Page .
2. Log in to ni.com with your NI user account.
3. Click the Install Offline button to download the
 ni-instrumentstudio_<version.number>_offline.iso 
 file. Note The .iso file is over 2.5 GB in size.
4. Mount the .iso image or burn the .iso image
 to a disk.
5. Run Install.exe .
6. Follow the instructions that Package Manager provides.
7. Restart your device when the installation process finishes.

Package Manager User Manual

Related
 Information

#### Install
 Additional Drivers

To use the panels in InstrumentStudio,
 you must install the appropriate drivers for the different instrument types. InstrumentStudio shows which version of which driver you must install
 for each panel.

If you choose offline installation, the .iso
 image contains the required drivers for all panel types. You can find the installer packages
 (.nipkg) for the drivers in the pool
 directory.

#### Install
 Additional Software

When you install InstrumentStudio using Package Manager, you
 can install additional optional software. Check the corresponding box for all additional
 software that you want to install. Package Manager checks some boxes in this section by
 default.

InstrumentStudio

| Software Name | Default Installation Status |
| --- | --- |
| Modular Instruments Support for TestStand | Checked by default |
| NI Certificates Installer | Checked by default |
| Plug-in Library CLI | Checked by default |
| Plug-in Library | Not checked by default |

InstrumentStudio

- LabVIEW Runtime (64-bit)
- LabWindows/CVI Shared Runtime
- License Manager
- Update Service
- TDM Excel Add-In
- .NET Desktop Runtime 8.0 (32-bit)
- .NET Desktop Runtime 8.0 (64-bit)
- ASP.NET Core Runtime 8.0 (32-bit)
- ASP.NET Core Runtime 8.0 (64-bit)
- DataSocket
- LabWindows/CVI .NET Library Runtime
- LabWindows/CVI Analysis Library Runtime
- LabWindows/CVI Network Streams Library Runtime
- LabWindows/CVI Shared Runtime Base
- LabWindows/CVI SQL Toolkit Runtime
- LabWindows/CVI TDM Streaming Library Runtime
- gRPC Device Server
- The most recent version of Measurement Plug-In Support for TestStand
- System Configuration .NET Runtime
- System Configuration Runtime
- Variable Engine
- TestStand Runtime

Related information:

- Package Manager User Manual

<!--NI_TOPIC bundle=instrumentstudio path=instrument-settings-menu.html language=enus -->
## TOPIC 00030: Configure Panels with the Instrument Settings Menu

- bundle_id: `instrumentstudio`
- source_path: `instrument-settings-menu.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/instrument-settings-menu.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The instrument settings menu ( A cogwheel icon for the instrument settings menu of InstrumentStudio. ) in InstrumentStudio offers options for data management, device configuration, and panel controls. The contents of the instrument settings menu depends on the panel type. To access the instrument se

### Configure Panels with the Instrument
 Settings Menu

The instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']) in InstrumentStudio offers options for data management, device configuration, and
 panel controls.

The contents of the instrument settings menu depends on the panel type. To access the
 instrument settings menu, click the [IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png'] icon in the upper-right corner of a panel. You can select, for example, the following
 options from the instrument settings menu:

Export

Export a Device Configuration

Capture data

.tdms

Capture Data

[Device name]

Add/Remove devices

Edit Layout

Create a Layout

Configure debug session

Configure Debug Session

Debug
 Programmatic Applications

Delete panel

Probe compensation

Parent topic:

Configure Panels and Layouts

Related concepts:

- Capture Data
- Debug Programmatic Applications

Related tasks:

- Export a Device Configuration
- Create and Edit a Layout
- Enable Debugging with a C, C++, or .NET Application
- Relink or Replace Missing Devices

<!--NI_TOPIC bundle=instrumentstudio path=interface.html language=enus -->
## TOPIC 00031: Navigating InstrumentStudio

- bundle_id: `instrumentstudio`
- source_path: `interface.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/interface.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about the InstrumentStudio UI and InstrumentStudio project file structure so you can quickly create projects. Overview 1 Example of a Scope Instrument A screenshot of an oscilloscope instrument panel from InstrumentStudio. Project File PaneThe project file panel displays all project files, suc

### Navigating InstrumentStudio

Learn about the InstrumentStudio UI and InstrumentStudio project file structure so you
 can quickly create projects.

#### Overview

Figure 1.

[IMAGE alt='A screenshot of an oscilloscope instrument panel from InstrumentStudio.' src='GUID-748FF75E-8130-4B02-85CE-2B460B1CFDB2-a5.png']

#### Project File Pane

- Data files
- Saved configurations
- Scripts
- Pin maps
- Other supporting files

- Create
- Rename
- Delete
- Import
- Export
- Search

[IMAGE alt='A screenshot of the project file pane of InstrumentStudio.' src='GUID-6072CAD8-6D1C-4DD1-AD7C-D7D70B76DF25-a5.png']

| File Type | Description |
| --- | --- |
| InstrumentStudio project (.isproj) | Contains the instrument panels added to your layout, device configurations, pin maps, captured data, and other project files. |
| Soft front panel (.sfp) | Contains the settings you choose for each instrument in your layout. |
| Pin map (.pinmap) | Defines how instruments and hardware connect to device under test (DUT) pins and sites. |
| Technical Data Management Stream (.tdms) | Stores data created by taking a snapshot of a graph. InstrumentStudio saves these files by default in the folder that contains your project. |
| Portable Network Graphic (.png) | An image of a graph created by taking a snapshot. InstrumentStudio saves these files by default in the folder that contains your project. |

#### Measurements Table

Measurements

- Measure signal properties
- Analyze signal characteristics
- Perform stimulus response tests

[IMAGE alt='A screenshot of the Measurements table of InstrumentStudio.' src='GUID-D3F0ABFB-714E-4CCC-BA34-D282EA9F2210-a5.png']

#### Instrument
 Configuration Panel

The instrument configuration panel allows you to
 configure instrument settings and view instrument status.

[IMAGE alt='A screenshot of the instrument configuration panel of InstrumentStudio.' src='GUID-CFE3D78B-1DAD-49DD-82E6-82CD916A7D5A-a5.png']

#### Instrument
 Settings Menu

[IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']

- Export and import configurations
- Capture data, which takes a screenshot of the measurement and generates a
 data file
- Access device-specific actions and information
- Add or remove devices, which opens the Edit Layout 
 window
- Configure debug sessions
- Delete panels
- Configure data sources
- Configure panel-specific settings, such as power line frequency

#### Instrument
 Header Menu

- Stop all outputs
- Create new instrument panels ( )
- Capture data ( ) and screenshots ( )
- Edit layouts ( )
- Export to TestStand ( )

[IMAGE alt='A screenshot of the instrument header menu in InstrumentStudio.' src='GUID-474AC742-F2CC-4F00-8576-862DB5CEA9D3-a5.png']

#### Measurement Graphs

The measurement graphs panel allows you to visualize
 data from connected instruments and interact with the graph. You can zoom, pan, and
 create annotations in the graphs.

[IMAGE alt='A screenshot of the measurement graph of an oscilloscope panel.' src='GUID-60D04C25-AC45-4510-80C9-B0C2B9E11243-a5.png']

#### Sequencer
 Tool

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

- Create and modify measurement sequences
- View measurement panels associated with sequence steps
- View a log that details the results of executing a sequence

[IMAGE alt='A screenshot of the sequencer tool.' src='GUID-EBA0213D-3B82-4B7E-B4EF-1D4430E12321-a5.png']

Related information:

- NI TDMS File Format - What is a TDMS File?

<!--NI_TOPIC bundle=instrumentstudio path=lcr.html language=enus -->
## TOPIC 00032: LCR Devices

- bundle_id: `instrumentstudio`
- source_path: `lcr.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/lcr.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the LCR panel to calibrate and perform cable compensation and LCR compensation on your LCR devices. Calibrate an LCR Device The accuracy of a device naturally drifts over time. You can perform self-calibration to compensate for this drift. Depending on your version of InstrumentStudio, you can p

### LCR Devices

Use the LCR panel to calibrate and perform cable compensation and LCR compensation on
 your LCR devices.

Parent topic:

Configure Device Settings

#### Calibrate an LCR Device

The accuracy of a device naturally drifts over time. You can perform self-calibration
 to compensate for this drift. Depending on your version of InstrumentStudio, you can perform
 self-calibration in Measurement & Automation Explorer (MAX) or in
 InstrumentStudio.

- Compensating for board-level temperature variations
- Compensating for device degradation
- Ensuring that the device operates in the ranges that you define in the test
 specifications

To calibrate an LCR device, complete the following steps:

1. In the LCR device instrument panel, open the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']).
2. Click Device Slot»Calibration»Self Calibrate.... 
 InstrumentStudio 2025 Q2 and earlier versions perform self-calibration in MAX. Later
 versions of InstrumentStudio perform self-calibration without MAX.

##### When to Calibrate an LCR Device

Performing self-calibration regularly ensures accuracy in your test
 measurements.

- You install the module in a chassis for the first time.
- You install, uninstall, or move another module in the same chassis as your LCR
 device.
- The ambient temperature in your test environment changed significantly.
- The onboard temperature of the LCR device drifted by at least ±5 °C since the last self-calibration.
- 24 hours passed since the previous self-calibration.

#### Perform Compensation on an LCR
 Device

When you connect an LCR device to a DUT with switches, fixtures, or cables, these
 instruments might introduce errors into the measurement. To prevent the measurement errors that
 these instruments introduce, apply compensation before you take the measurement.

- You make changes to the test system setup.
- You perform an LCR device calibration on a new LCR device.

When to Generate New
 Data for Custom Cable Compensation or LCR Compensation

For more information on how to perform compensation on an LCR device, see
 *Compensation of LCR Measurements* in the *Related Information*
 section.

To perform compensation on an LCR device, complete the following steps:

1. Calibrate the LCR device.
2. Determine the type of cable compensation to perform based on the following
 factors: 
 OptionRecommended When[Standard Cable Compensation](lcr.html#GUID-9A6E01C6-90AE-4292-8154-63A51466FC1B)
 You use a standard NI cable that has a Cable Length
 profile in the Instrument Settings dialog ([IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png']) and a simple test setup. That is, the test setup excludes complex circuitry,
 such as switches, that might affect LCR measurements.[Custom Cable Compensation](lcr.html#GUID-BEF329B5-DEDE-4849-A145-526C858A461C)
 You use non-NI cabling and a complex test setup. That is, the test setup
 includes complex circuitry, such as switches, that might affect LCR
 measurements. 
 Note Apply cable
 compensation for low-level LCR measurements where the effects of cabling might be
 significant relative to the quantity that you measure.Note Apply
 Short LCR Compensation first when you use custom non-NI cabling to
 ensure accurate measurements.
3. Determine the type of LCR compensation to perform based on the following factors: 
 OptionRecommended When[Open LCR Compensation](lcr.html#GUID-81E6059A-01F8-479B-9397-0294FD31F055)
 Stray admittance in your test setup influences the LCR measurements. Note Such stray admittance is present in
 most test setups.[Short LCR Compensation](lcr.html#GUID-9A5A127E-9F1D-482B-81C0-7458619D7043)
 The impedance of your DUT is <100 Ω. The
 residual impedance of cabling and fixtures might be a significant percentage of your
 DUT impedance.[Load LCR Compensation](lcr.html#GUID-6A828E0E-432C-4FBA-8DB2-A10E9539EAA9)
 The reference load value is similar to your DUT. Your test setup also includes
 complex circuitry, such as switches, that might affect LCR measurements. 
 Note To perform
 Load LCR Compensation, you must first perform Open LCR
 Compensation and Short LCR Compensation.

Related information:

- Compensation of LCR Measurements

##### Perform Standard Cable Compensation

Use the Instrument Settings window to select the appropriate
 cable length for your instrument. Use standard compensation if you use standard cables for your
 instruments.

1. Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon in your LCR device instrument panel to open the Instrument
 Settings window.
2. Select your cable length from the Cable type dropdown
 menu.

##### Perform Custom Cable Compensation

Use the Instrument Settings window to select custom
 compensation. Use custom compensation if you use custom cables for your instruments.

Note

1. Click Custom Compensation ([IMAGE alt='An icon with a double-sided arrow that allows for custom compensation in InstrumentStudio.' src='GUID-94102D63-A19C-491C-87FD-348A5636A6F5-a5.png']) in the instrument panel.
2. Click Renew.
3. Click Compensate.
4. Click OK.

1. Click the icon in your LCR device instrument panel to open the Instrument
 Settings window.
2. Select the Custom option from the Cable type 
 dropdown.

1. Click Custom Compensation ( ).
2. Check if Apply compensation is enabled.

For more information on how to perform compensation on an LCR device, see
 *Compensation of LCR Measurements* in the *Related Information*
 section.

Related information:

- Compensation of LCR Measurements

##### Perform Open LCR Compensation

Apply open compensation with the Open Compensation ([IMAGE alt='An icon of two parallel cables that allows for open compensation in InstrumentStudio.' src='GUID-D6597AD2-3C5C-4983-8F9A-742F1D0B9E78-a5.png']) option in the instrument panel.

Figure 3.

[IMAGE alt='Diagram showing an open configuration for setting up open LCR compensation.' src='GUID-C3644AC3-2B94-4936-8DAC-AAF4055AEEF0-a5.svg']

1. HI CUR
2. HI POT
3. LO POT
4. LO CUR
5. Connection between outer conductors

Open LCR Compensation

1. Click Open Compensation ([IMAGE alt='An icon of two parallel cables that allows for open compensation in InstrumentStudio.' src='GUID-D6597AD2-3C5C-4983-8F9A-742F1D0B9E78-a5.png']) in the instrument panel to open the compensation dialog.
2. Click Renew.
3. Optional: 
 Enter additional frequencies to compensate for.
4. Click Compensate.
5. Click OK.

1. Click Open Compensation ( ).
2. Check if Apply compensation is enabled.

For more information on how to perform compensation on an LCR device, see
 *Compensation of LCR Measurements* in the *Related Information*
 section.

Related information:

- Compensation of LCR Measurements

##### Perform Short LCR Compensation

Apply Short Compensation ([IMAGE alt='An icon of a curved cable that allows for short compensation in InstrumentStudio.' src='GUID-E2D75D62-3191-4EFB-ACF0-BBC6C3AF7394-a5.png']) option in the instrument panel. You must perform Short LCR
 Compensation when you use custom non-NI cabling.

Figure 4.

[IMAGE alt='Diagram showing a short configuration for setting up short LCR compensation.' src='GUID-3BCF59C1-8EB5-42C1-92F5-39BFA9DE35BF-a5.svg']

1. HI CUR
2. HI POT
3. LO POT
4. LO CUR
5. Connection between outer conductors

Note

Short LCR
 Compensation

Custom Cable
 Compensation

Short LCR
 Compensation

Short LCR Compensation

1. Click Short Compensation ([IMAGE alt='An icon of a curved cable that allows for short compensation in InstrumentStudio.' src='GUID-E2D75D62-3191-4EFB-ACF0-BBC6C3AF7394-a5.png']) in the instrument panel to open the compensation dialog.
2. Click Renew.
3. Optional: 
 Enter additional frequencies to compensate for.
4. Click Compensate.
5. Click OK.

1. Click Short Compensation ( ).
2. Check if Apply compensation is enabled.

For more information on how to perform compensation on an LCR device, see
 *Compensation of LCR Measurements* in the *Related Information*
 section.

Related information:

- Compensation of LCR Measurements

##### Perform Load LCR Compensation

Apply open compensation with the Load Compensation ([IMAGE alt='An icon of two parallel cables with load icons that allows for load compensation in InstrumentStudio.' src='GUID-69C279EF-C3B8-4277-AE3F-8346D5E4F39A-a5.png']) option in the instrument panel.

Figure 5.

[IMAGE alt='Diagram showing a load configuration for setting up load LCR compensation.' src='GUID-D96A9FBD-FC59-427B-B94C-0669C1CB9E0C-a5.svg']

1. HI CUR
2. HI POT
3. LO POT
4. LO CUR
5. Connection between outer conductors

Load LCR Compensation

1. Click Load Compensation ([IMAGE alt='An icon of two parallel cables with load icons that allows for load compensation in InstrumentStudio.' src='GUID-69C279EF-C3B8-4277-AE3F-8346D5E4F39A-a5.png']) in the instrument panel to open the compensation dialog.
2. Click Renew.
3. Optional: 
 Enter spots to compensate for.
4. Click Compensate.
5. Click OK.

1. Click Load Compensation ( ).
2. Check if Apply compensation is enabled.

For more information on how to perform compensation on an LCR device, see
 *Compensation of LCR Measurements* in the *Related Information*
 section.

Related information:

- Compensation of LCR Measurements

##### When to Generate New Data for Custom Cable
 Compensation or LCR Compensation

Performing a new custom cable and LCR device compensation ensures better accuracy in
 test measurements after you make changes to your test system setup.

Generate new custom cable compensation data or LCR compensation data in the following
 cases:

- You perform a new external calibration.
- You perform a new self-calibration.
- You add complex circuit elements, such as a switch, between the end of the cable
 and the fixture that contains your DUT.
- You change the length of the cabling in your test setup.
- You change the physical orientation of the cabling in your test setup.
- You begin testing a DUT with a different part number from the DUT for which you
 originally generated the compensation data. Note For
 Load LCR Compensation, choose a new reference load that
 is appropriate for the new DUT.

<!--NI_TOPIC bundle=instrumentstudio path=leftover-elements-after-uninst.html language=enus -->
## TOPIC 00033: Leftover Elements After Uninstallation

- bundle_id: `instrumentstudio`
- source_path: `leftover-elements-after-uninst.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/leftover-elements-after-uninst.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you uninstall InstrumentStudio, no additional software gets removed. Some files and data also remain on the system. SoftwareAll software installed with InstrumentStudio remains on your system after you uninstall InstrumentStudio. For a list of software that you can install with InstrumentStudio

### Leftover Elements After
 Uninstallation

When you uninstall InstrumentStudio, no additional software
 gets removed. Some files and data also remain on the system.

#### Software

All software
 installed with InstrumentStudio remains on your system
 after you uninstall InstrumentStudio. For a list of
 software that you can install with InstrumentStudio, see
 *Install InstrumentStudio*.

Note

#### Local Application Data

<UserName>

<version.number>

- ErrorReports
- PluginCache
- LauncherProjectStatus.xml
- Preferences.xml

#### Saved
 Projects and Documents

InstrumentStudio

- By default,
 C:\Users\<UserName>\Documents\InstrumentStudio
 Projects\
- A folder that you defined

InstrumentStudio

#### Exported Data

InstrumentStudio

| Data Type | File Location |
| --- | --- |
| Captured data | C:\\Users\\<UserName>\\Documents\\InstrumentStudio Projects\\ |
| Data exported to TestStand | C:\\Users\\Public\\Documents\\National Instruments\\TestStand\\Shared\\IO Configurations\\ |
| Exported driver configurations | User-defined |

All exported data remains on your system after you uninstall InstrumentStudio.

#### InstrumentStudio
 Plug-Ins

InstrumentStudio plug-ins that you added
 to the \<installation
 path>\InstrumentStudio\Addons\ directory remain on your
 system after you uninstall InstrumentStudio.

#### Measurement Plug-Ins

All measurement
 plug-ins remain on your system, including plug-ins that you statically registered in
 the C:\ProgramData\NationalInstruments\Plug-Ins\Measurements\
 directory.

#### Plug-In
 Library Data

- Plug-in Library
- Plug-in Library CLI

InstrumentStudio

#### SCPI Configurations

InstrumentStudio saves .json files for
 SCPI-capable instruments in the
 C:\ProgramData\NationalInstruments\Services\Scpi\ScriptDefinitions\
 directory by default. These .json configuration files remain on
 your system after you uninstall InstrumentStudio.

Parent topic:

Install InstrumentStudio

Related concepts:

- Install InstrumentStudio

<!--NI_TOPIC bundle=instrumentstudio path=live-measurement-view.html language=enus -->
## TOPIC 00034: Live Measurement View

- bundle_id: `instrumentstudio`
- source_path: `live-measurement-view.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/live-measurement-view.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you monitor SMU/VPS devices in debug mode, InstrumentStudio automatically displays measurements of channel data in real time. InstrumentStudio displays this data even if external applications are not currently fetching device data. InstrumentStudio does not support live measurement view for the

### Live Measurement View

When you monitor SMU/VPS devices in debug mode, InstrumentStudio automatically displays
 measurements of channel data in real time. InstrumentStudio displays this data even if external
 applications are not currently fetching device data.

- PXI-4110
- PXI-4130
- PXI-4132
- PXIe-4112
- PXIe-4113
- PXIe-4154
- PXIe-4162
- PXIe-4163
- PXIe-4190

Note

Measure

Fetch

Parent topic:

Debug Programmatic Applications

<!--NI_TOPIC bundle=instrumentstudio path=meas-plugins.html language=enus -->
## TOPIC 00035: Measurement Plug-Ins

- bundle_id: `instrumentstudio`
- source_path: `meas-plugins.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/meas-plugins.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A measurement plug-in helps you create reusable measurements for supported devices that function across multiple products. A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license. This feature is only available with an InstrumentStudio Professional l

### Measurement Plug-Ins

A measurement plug-in helps you create reusable measurements for supported
 devices that function across multiple products.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

- Measurement logic
- Metadata
- An optional UI

For more information on developing and using measurement plug-ins, see
 *Measurement Plug-Ins User Manual*.

Parent topic:

Plug-Ins

Related information:

- Measurement Plug-Ins User Manual
- Measurement Plug-Ins SDK for LabVIEW
- Measurement Plug-Ins SDK for Python

#### Running a Measurement Plug-In

1. On the Home screen, select Manual
 layout. 
 The Edit layout screen appears.
2. Locate your measurement plug-in in the list. 
 Note If your measurement
 plug-in does not appear in the Edit layout window,
 ensure that the plug-in is started. You can configure the plug-in to start
 automatically or you can start the plug-in manually. For more information,
 see *Statically Register a Measurement Service* in the
 *Developing a Measurement Plug-In with LabVIEW* section or
 the *Developing a Measurement Plug-In with Python* section of the
 *Measurement Plug-Ins User Manual*.
3. Select Create large panel in the drop-down list for your
 measurement plug-in. 
 The large panel updates to list the selected measurement
 plug-in.
4. Click OK. 
 InstrumentStudio opens a new project and displays the measurement
 UI.
5. Optional: 
 If the measurement plug-in requires a pin map, ensure that the project contains
 a referenced pin map. Also ensure that the pin map is marked as active.
6. Click Run in the measurement UI. 
 Tip You can change
 the behavior of the Run button so that the
 measurement runs continuously. Click the arrow at the side of the button and
 select Run Continuously to change the button
 behavior. Once the measurement is running, the button text changes. Click
 Stop to stop the measurement.

Related information:

- Developing a Measurement Plug-In with LabVIEW
- Developing a Measurement Plug-In with Python

#### Plug-In Versioning

You can manage, select, and synchronize plug-in versions in
 InstrumentStudio.

##### Versioned
 Plug-Ins

For more information on versioning measurement plug-ins with
 LabVIEW or Python, see *Plug-In Versioning* in the *Measurement
 Plug-Ins User Manual*.

##### Selecting A Measurement Plug-In
 Version

Edit layout

Manual layout

Note

##### Synchronizing Plug-In Versions within a Project

[IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-934AE2CB-A722-468F-98E6-429D375F232F-a5.png']

Synchronize Version

Note

Related information:

- Plug-In Versioning

<!--NI_TOPIC bundle=instrumentstudio path=measurement-types.html language=enus -->
## TOPIC 00036: Measurement Types

- bundle_id: `instrumentstudio`
- source_path: `measurement-types.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/measurement-types.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: InstrumentStudio features the following measurement types when you create oscilloscope channels: Oscilloscope Measurement Types Amplitude Positive Undershoot Period Fall Rate Peak-to-Peak Negative Undershoot Frequency Delta Time High Positive Overshoot Positive Duty Cycle Setup Time Low Negative Ove

### Measurement Types

InstrumentStudio features the following measurement types when you create oscilloscope
 channels:

| Amplitude | Positive Undershoot | Period | Fall Rate |
| --- | --- | --- | --- |
| Peak-to-Peak | Negative Undershoot | Frequency | Delta Time |
| High | Positive Overshoot | Positive Duty Cycle | Setup Time |
| Low | Negative Overshoot | Negative Duty Cycle | Hold Time |
| Maximum | RMS | Positive Pulse Width | Crosspoint Level |
| Minimum | Mean | Negative Pulse Width | Crosspoint Time |
| High Ref Level | Median | Rise Time | FFT Amplitude |
| Mid Ref Level | Cycle RMS | Fall Time | FFT Frequency |
| Low Ref Level | Cycle Mean | Rise Rate |  |

#### Amplitude

[IMAGE alt='Graph showing a waveform with a dotted line that shows the frequency difference between the most common value found in the upper 40% of the waveform and the most common value found in the lower 40% of the waveform.' src='GUID-488B2F92-F854-4980-91C8-577AA001E730-a5.png']

The [High](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-D00D26BA-F39B-4F4C-A675-ED3EEE68299A) measurement minus the [Low](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-F42BCE71-5A4D-423F-B563-9A4C2963A2BF) measurement.

#### Peak-to-Peak

[IMAGE alt='Graph showing a waveform with a dotted line that shows the frequency difference between the maximum measurement and the minimum measurement.' src='GUID-7665130B-1362-414D-BE93-EB880B982938-a5.png']

The [Maximum](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-AD8D034D-43A6-4F3A-9258-8E82837DA5DE)
 measurement minus the [Minimum](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-EF0E5798-18AD-48E3-9AB9-1C1DEEFC2771)
 measurement.

#### High

[IMAGE alt='Waveform with a dashed line indicating the most common value found in the upper 40% of the waveform.' src='GUID-48A62C5B-1EFD-4685-9180-11101BD8896A-a5.png']

The High measurement is calculated using the selected [High-Low Method](reference-levels-gating.html#GUID-C835ED6C-BF3D-4511-A3F9-47AA5B8ED74E). If you
 select the Histogram High-Low method, the High measurement
 is calculated using the most common value found in the upper 40% of the waveform. If you
 select the Peak High-Low method, the High measurement is
 calculated using the [Maximum](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-AD8D034D-43A6-4F3A-9258-8E82837DA5DE)
 measurement value of the waveform.

#### Low

[IMAGE alt='Waveform with a dashed line indicating the most common value found in the lower 40% of the waveform.' src='GUID-BACB84B5-0B39-4111-9262-8952ABA35F8C-a5.png']

The Low measurement is calculated using the selected [High-Low Method](reference-levels-gating.html#GUID-C835ED6C-BF3D-4511-A3F9-47AA5B8ED74E). If you
 select the Histogram High-Low method, the Low measurement
 is calculated using the most common value found in the lower 40% of the waveform. If you
 select the Peak High-Low method, the Low measurement is
 calculated using the [Minimum](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-EF0E5798-18AD-48E3-9AB9-1C1DEEFC2771)
 measurement value of the waveform.

#### Maximum

[IMAGE alt='Waveform with a dashed line indicating the maximum value of the waveform.' src='GUID-5A646D82-8429-4808-8B1F-FA3D5309E19F-a5.png']

The maximum value found in the waveform.

#### Minimum

[IMAGE alt='Waveform with a dashed line indicating the minimum value of the waveform.' src='GUID-BAAC0782-E0B2-4EA4-899E-3F1B9C498522-a5.png']

The minimum value found in the waveform.

#### High Ref Level

[IMAGE alt='Waveform with a dashed line indicating the high reference level.' src='GUID-3FFABC7F-A9BC-49E0-AACB-ECB95FC1F781-a5.png']

The level of the signal at the high reference level. If you set the reference level unit to
 Percentage, the High Ref Level measurement is calculated with the selected
 High-Low method. If you set the reference level unit to
 Absolute, the value that you set as the High reference
 level is used for the measurement.

#### Mid Ref Level

[IMAGE alt='Waveform with a dashed line indicating the mid reference level.' src='GUID-10BED970-2BB9-4598-A732-2C61E75E55E5-a5.png']

The level of the signal at the mid reference level. If you set the reference level unit to
 Percentage, the Mid Ref Level measurement is calculated with the selected
 High-Low method. If you set the reference level unit to
 Absolute, the value that you set as the Mid reference
 level is used for the measurement.

#### Low Ref Level

[IMAGE alt='Waveform with a dashed line indicating the low reference level.' src='GUID-4AF19153-D72E-40C6-B72E-53AF3FF8F390-a5.png']

The level of the signal at the low reference level. If you set the reference level unit to
 Percentage, the Low Ref Level measurement is calculated with the selected
 High-Low method. If you set the reference level unit to
 Absolute, the value that you set as the Low reference
 level is used for the measurement.

#### Positive Undershoot

[IMAGE alt='Graph showing a waveform at threshold level. The waveform then briefly falls below a low threshold and then rises until it levels well over the threshold level.' src='GUID-478EBC74-F723-4787-B731-13D67ABBE267-a5.png']

#### Negative Undershoot

[IMAGE alt='Graph showing a waveform at threshold level. The waveform then briefly rises above a high threshold and then falls until it levels well under the threshold level.' src='GUID-806884DD-78B0-4F91-85A6-F69BE8AE33C5-a5.png']

#### Positive Overshoot

[IMAGE alt='Graph showing a rising waveform that briefly went above a high threshold. Then the waveform falls to the threshold level and stays there.' src='GUID-B4499386-9B0B-473B-B8F9-E359FDF49971-a5.png']

#### Negative Overshoot

[IMAGE alt='Graph showing a falling waveform that briefly went below a lowthreshold. Then the waveform rises to the threshold level and stays there.' src='GUID-61D2006B-CED4-40C7-BEC6-A23D21E514DC-a5.png']

#### RMS

[IMAGE alt='Graph showing a waveform with two peaks, a median line, and an average line.' src='GUID-79457F28-A125-4F35-8877-3D69766FF267-a5.png']

The true root mean square voltage over the entire waveform. This measurement uses the
 following formula:

[IMAGE alt='Equation describing how to calculate RMS.' src='GUID-897C2F94-157F-454A-A443-3DD179FC69FC-a5.png']

#### Mean

[IMAGE alt='Graph showing a waveform with two peaks and a corresponding median line.' src='GUID-13E16EA9-A199-474A-A1B3-4B93EAE44C3C-a5.png']

The mean over the entire waveform.

#### Median

[IMAGE alt='Graph showing a waveform with a median line.' src='GUID-9FC7A7ED-F16A-4315-ADBC-696EBF570FBB-a5.png']

The median over the entire waveform. The points in the waveform are sorted
 according to the following formulas:

| Number of Points | Returned Value |
| --- | --- |
| Odd | Waveform n - 1 2 |
| Even | Waveform m 2 + Waveform n 2 + 1 2 |

#### Cycle RMS

[IMAGE alt='Graph of a sinusoidal waveform with a dashed line indicating RMS value.' src='GUID-56B72F9B-6BF3-4E6A-A2D5-3ACA5CDF815B-a5.png']

The true root mean square voltage over the first cycle of the waveform. The values you
 specify in the High, Mid, and Low Reference Level fields in the
 Settings tab of the Measurements window
 determine the first cycle. This measurement uses the following formula:

[IMAGE alt='Equation describing how to calculate cycle RMS.' src='GUID-150227DF-B6D4-40DB-B1B6-AA5AE98849B7-a5.png']

, where *waveform* is all the points in the first cycle of the
 waveform.

#### Cycle Mean

[IMAGE alt='Graph showing a sine wave with a dashed line indicating the mean cycle level.' src='GUID-84B48143-C28C-4B6A-B1F7-1BF260698301-a5.png']

The voltage average over the first cycle of the waveform. The values you specify in
 the High, Mid, and Low Reference Level fields in the
 Settings tab of the Measurements window
 determine the first cycle.

#### Period

[IMAGE alt='A graph that shows the time difference of a waveform that crosses a reference level twice.' src='GUID-391D8910-21FA-48E4-83E3-E4D029605935-a5.png']

The time of the first two Mid Reference Level crossings in the
 same direction. The High or Low Reference Levels are used
 to apply a hysteresis.

#### Frequency

[IMAGE alt='Diagram showing frequency as the inverse of time interval delta t.' src='GUID-781A93FE-1868-41A8-9A65-DB1F0C090A3A-a5.png']

1.0 divided by the [Period](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-FA6AEA23-4BA8-4502-827A-9BEB21728472) measurement, in Hz.

#### Positive Duty Cycle

[IMAGE alt='A diagram that shows a waveform that first falls below, then rises above a reference level. This repeats twice. The time difference between the first two crossings is marked by a line. The time difference between the second two crossings is marked by a dotted line.' src='GUID-9A1AB47C-D2C7-4370-B320-E24A84C28842-a5.png']

The [Positive Pulse Width](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-1E1F14AA-8103-4C2C-87AA-369CEFD9DE61) divided by the [Period](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-FA6AEA23-4BA8-4502-827A-9BEB21728472) times 100.

Positive Duty Cycle

=

Positive Pulse Width

Period

x

100

#### Negative Duty Cycle

[IMAGE alt='A diagram that shows a waveform that first rises above, then falls below a reference level. This repeats twice. The time difference between the first two crossings is marked by a line. The time difference between the second two crossings is marked by a dotted line.' src='GUID-6F0D46F7-CBB6-4805-8AD8-7723413AF6AF-a5.png']

The [Negative Pulse Width](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-AF872FC8-1133-4522-A691-6851E9D5DD6E) divided by the [Period](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-FA6AEA23-4BA8-4502-827A-9BEB21728472) times 100.

Negative Duty Cycle

=

Negative Pulse Width

Period

x

100

#### Positive Pulse Width

[IMAGE alt='A diagram that shows a waveform that first rises above, then falls below a reference level. The time difference between the two crossings is marked by a line.' src='GUID-FAF95A9A-B2D7-4632-9B8F-BCABF1A2F311-a5.png']

The time difference in seconds between the first two Mid Reference
 Level crossings, where the first slope is positive and the second is negative.
 The High or Low Reference Levels are used to apply a
 hysteresis.

#### Negative Pulse Width

[IMAGE alt='A diagram that shows a waveform that first falls below, then rises above a reference level. The time difference between the two crossings is marked by a line.' src='GUID-EA8C8C66-7C76-404B-B041-F985CA7C345E-a5.png']

The time difference in seconds between the first two Mid Reference
 Level crossings, where the first slope is negative and the second is positive.
 The High or Low Reference Levels are used to apply a
 hysteresis.

#### Rise Time

[IMAGE alt='Graph showing a linear increase over time with a high and a low reference level defined.' src='GUID-16CABBD5-526C-471F-8675-0372BE7D8FE5-a5.png']

A time span that begins when the first rising edge of the waveform crosses the Low
 Reference Level. The time span lasts until the same rising edge crosses the
 High Reference Level. The time span starts from the Low Reference
 Level crossing that immediately precedes the High Reference
 Level crossing.

#### Fall Time

[IMAGE alt='Graph showing a linear decrease over time with a high and a low reference level defined.' src='GUID-F3ED7CBC-54A3-4A71-9E57-E837FF89C4DF-a5.png']

A time span that begins when the first falling edge of the waveform crosses the
 High Reference Level. The time span lasts until the same falling edge
 crosses the Low Reference Level.

#### Rise Rate

[IMAGE alt='Diagram showing rise rate with delta V over delta T.' src='GUID-1B6C9909-1D87-4286-8CD6-73DE31B4960E-a5.png']

The [Rise Time](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-3A55A376-EE8C-47D6-9C8C-ACF2B6EF8AD7) divided by the High Reference Level minus the Low
 Reference Level.

Rise Rate

=

Rise Time

High Reference Level

-

Low Reference Level

#### Fall Rate

[IMAGE alt='Diagram showing fall rate with delta V over delta T.' src='GUID-8F5508C9-3A5B-4B81-B59C-A29D802FF912-a5.png']

The [Fall Time](measurement-types.html#GUID-59C04F07-941D-410E-91B5-645348FB111C__GUID-414D096A-7BC2-4CDD-A767-AB5B18724BB6) divided by the High Reference Level minus the Low
 Reference Level.

Fall Rate

=

Fall Time

High Reference Level

-

Low Reference Level

#### Delta Time

[IMAGE alt='Diagram showing a waveform and the delta time measurement.' src='GUID-E0216833-62C8-4574-99F4-6276523F4653-a5.png']

A time span that begins when the first edge of the waveform crosses the Mid
 Reference Level. The time span lasts until the second edge of the waveform
 crosses the Mid Reference Level. The second edge does not have to be on the
 same channel as the first edge.

#### Setup Time

[IMAGE alt='Diagram showing a clock channel and the setup time measurement.' src='GUID-E98F1FA6-2477-4BE6-AB24-0756FAA199FC-a5.png']

A time span that begins when the waveform crosses the Mid Reference
 Level. The time span lasts until the configured clock channel crosses the
 Mid Reference Level. The Setup Time measurement uses the
 crossing of the clock channel that is the closest to the middle of the graph.

#### Hold Time

[IMAGE alt='Diagram showing a clock channel and the hold time measurement.' src='GUID-395B88AB-595C-48AF-BC47-819E81F42B48-a5.png']

A time span that begins when the configured clock channel crosses the Mid
 Reference Level. The time span lasts until the waveform crosses the Mid
 Reference Level. The Hold Time measurement uses the crossing of
 the clock channel that is the closest to the middle of the graph.

#### Crosspoint Level

[IMAGE alt='Diagram showing two lines that intersect twice. There is a dashed horizontal line at the intersection that is closer to the middle of the graph.' src='GUID-6D479C3E-9D41-454F-8DB8-D96EC9FF08AC-a5.png']

The level at which two waveforms intersect. The second waveform does not have to be
 on the same channel as the first waveform. The Crosspoint Level measurement
 uses the intersection that is the closest to the middle of the graph.

#### Crosspoint Time

[IMAGE alt='Diagram showing two lines that intersect twice. There is a dashed vertical line at the intersection that is closer to the middle of the graph.' src='GUID-D45D2F04-D68C-4D42-85F4-35E4C16B7625-a5.png']

The time at which two waveforms intersect. The second waveform does not have to be on the
 same channel as the first waveform. The crosspoint time measurement uses the intersection
 that is the closest to the middle of the graph.

#### FFT Amplitude

[IMAGE alt='Graph showing FFT amplitude with peaks and troughs.' src='GUID-221D253F-F604-45C2-9BC7-8E609817372C-a5.png']

Calculates a real FFT and returns the maximum amplitude. The search ignores the DC
 bin of the FFT. Peaks that are close to the DC bin, but not in the DC bin, are still
 detected.

#### FFT Frequency

[IMAGE alt='Graph showing FFT frequency spectrum with peaks.' src='GUID-758DC927-0675-47B6-8C02-EB69CFA8C905-a5.png']

Calculates a real FFT and returns the frequency that corresponds to the maximum
 amplitude. The search ignores the DC bin of the FFT. Peaks that are close to the DC bin, but
 not in the DC bin, are still detected.

<!--NI_TOPIC bundle=instrumentstudio path=missing-devices.html language=enus -->
## TOPIC 00037: Relink or Replace Missing Devices

- bundle_id: `instrumentstudio`
- source_path: `missing-devices.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/missing-devices.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use relinking to re-establish a connection to a missing device. You can also use relinking to replace the missing device with a different device of the same model in an existing panel. InstrumentStudio flags devices as missing if you close InstrumentStudio and a device used in an InstrumentStudio pr

### Relink or Replace Missing Devices

Use relinking to re-establish a connection to a missing device. You can also use
 relinking to replace the missing device with a different device of the same model in an existing
 panel.

- The title bar of the panel is gray instead of blue.
- The panel displays a Missing hardware message.
- The caution icon ( ) appears next to the instrument header menu of the affected panel.
- The caution icon ( ) appears next to the missing device in the instrument settings menu.
- A notification appears in the Edit Layout window.

You can *relink* a missing device through the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']) or *replace* a missing device in the Edit Layout
 window. When you relink a missing device through the instrument settings menu,
 InstrumentStudio applies the existing configuration of the device to the relinked device.
 You can replace a missing device through the Edit Layout window. In
 this case, InstrumentStudio discards the existing device configuration and creates another
 configuration for the replacement device.

Note

You can also relink or locate a missing device through the Hardware Configuration Utility
 (HWCU) or Measurement & Automation Explorer (MAX). If InstrumentStudio is open,
 changes made in HWCU or MAX automatically apply to InstrumentStudio panels.

If a device went missing because it was renamed while InstrumentStudio was not open, you
 must relink the missing device. To relink the missing device, open the InstrumentStudio
 panel that contains the missing device. Then, change the name of the device in HWCU or MAX
 to match the name that InstrumentStudio is looking for.

#### Relink Missing Devices from the
 Instrument Settings Menu

You can use this method to link a different device of the
 same model to an existing panel. You can do this even if the original device is not missing.
 Replacing a device in a panel through relinking preserves device settings from the original
 device. This method also applies these settings to the replacement device.

1. Open the instrument settings menu ( ) of the panel with the missing device.
2. Select the missing device. The missing device
 has a caution icon ( ) next to it.
3. Select Relink .
4. Select the name of the device that you want to
 link to the panel. Note When
 relinking from the instrument settings menu, the relinked device must be the same model
 as the missing device. InstrumentStudio applies the existing device configuration to the
 new device when you link the new device.
5. Select Run on the
 relinked panel.

#### Replacing Missing Devices from the Edit
 Layout Window

You cannot directly relink a missing device from the Edit Layout
 window. To remove a missing device and replace it with a different device, complete the
 following steps:

1. Open the Edit Layout 
 window in one of the following ways:
  - From the instrument header menu, select the
 Edit layout icon ( ).
  - From an instrument settings menu ( ), select Add/Remove devices . Note If you access the Edit Layout window
 through an instrument settings menu, InstrumentStudio automatically applies a filter
 on the device list. This filter is based on which panel you selected the
 Add/Remove devices option from. You can remove or change
 this filter by clicking the filter icon ([IMAGE alt='An icon of a filter.' src='GUID-13C35A3D-99E2-41D4-9FB2-ED87361ADA62-a5.png']) next to the search field.
2. Locate the missing device. The missing device
 has a caution icon ( ) next to it.
3. Click the × icon next to
 the caution icon to remove the missing device from the layout. Note If the missing device was not part of a
 group, removing the device also removes the panel of the device.
4. For groups, add a replacement device of the
 same type to the panel. Alternatively, make a new panel with the replacement device. Note When you replace a missing device from
 the Edit Layout window, the new device must follow the layout
 guidelines. For more information on layout guidelines, see *Panels and
 Layouts*.
5. Select OK to save your
 changes.
6. Select Run on the edited
 panel.

Parent topic:

Configure Panels and Layouts

Related concepts:

- Panels and Layouts

<!--NI_TOPIC bundle=instrumentstudio path=mod-seq.html language=enus -->
## TOPIC 00038: Modify a Sequence

- bundle_id: `instrumentstudio`
- source_path: `mod-seq.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/mod-seq.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can modify existing sequences and panels that are part of a sequence. Changing Sequencer Panel ConfigurationsYou can change the configuration of a panel that is used in multiple steps. In this case, InstrumentStudio applies the changes to all instances of that panel in the sequence.Changes made

### Modify a Sequence

You can modify existing sequences and panels that are part of a sequence.

#### Changing Sequencer Panel
 Configurations

You can change the configuration of a panel that is used in
 multiple steps. In this case, InstrumentStudio applies the changes to all instances
 of that panel in the sequence.

Note

#### Reuse a
 Panel

If you want to use different configurations with the same panel, you
 must create a new panel. Click Duplicate Panel ([IMAGE alt='An icon of semi-overlapping grey rectangles that represent duplicating a panel in InstrumentStudio.' src='GUID-47EE201B-50EB-4EB5-ADE6-729A77C4ACC8-a5.png']) to quickly make a duplicate of the selected panel.

#### Reorder a
 Sequence

Drag and drop a step to the desired position in the sequence to
 change the order of the steps within a sequence.

#### View
 Steps

Double-click a step to quickly access and edit the panel associated
 with it.

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=network-analyzer.html language=enus -->
## TOPIC 00039: Network Analyzers

- bundle_id: `instrumentstudio`
- source_path: `network-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/network-analyzer.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Network Analyzer panel to characterize RF devices and apply corrections to your Network Analyzer instrument. InstrumentStudio supports the RFmx VNA personality for network analyzer instruments. Characterize RF Devices Use the network analyzer panel to perform measurements on and to character

### Network Analyzers

Use the Network Analyzer panel to characterize RF devices and apply corrections to your
 Network Analyzer instrument.

Note

Parent topic:

Configure Device Settings

#### Characterize RF Devices

Use the network analyzer panel to perform measurements on and to characterize RF
 devices.

1. Create a network analyzer panel by clicking New ([IMAGE alt='An icon of a plus sign with a dropdown menu that creates new instrument panels in InstrumentStudio.' src='GUID-5D359458-1C20-4043-9F6A-CB5CA3CED544-a5.png'])»Network Analyzer.
2. Configure your instrument. Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon to open the Network Analyzer Settings window. 
 Note 
 If you did not do so previously, calibrate your network analyzer instrument.
 Uncalibrated instruments might generate unexpected and inaccurate results when you
 take measurements. To calibrate your instrument, complete the following steps:Open the Network Analyzer Settings window.
 Select the Calibration tab.
 Choose a calibration method.
 Apply the corrections. For more information, see [Apply Corrections to Network Analyzers](network-analyzer.html#GUID-CB144BCA-8779-43BE-A707-43A4D09BB320).
3. Connect your DUT if it is not already connected.
4. Run the measurement by selecting one of the following options:
  - Click RUN to measure continuously.
  - Click SINGLE to capture a single measurement.

#### Apply Corrections to Network Analyzers

To ensure accurate measurements, you must apply the corrections that the calibration
 process generates.

- You already calibrated your device.
- You saved a calset ( .ncst ) file.

1. Click the + button next to the Active
 Calset setting.
2. Select the calibration data file that corresponds to your current
 configuration.
3. Click Open.
4. Ensure that the Correction setting is set to
 ON.

Adjustments are now automatically applied when you use this
 instrument.

Related information:

- PXIe-5842 Self-Calibration

#### Port Extension

When you add a switch, a fixture, or a cable to your Network Analyzer instrument after
 calibration, you introduce loss and additional electrical delay. The loss and the
 delay shift the measurement reference plane away from the DUT. Port extension
 compensates for these factors by restoring the reference plane to the correct
 location without requiring a new calibration. InstrumentStudio supports manual and
 automatic port extension.

1. Click the button to open the Network Analyzer
 Settings window.
2. Go to the Correction tab of the
 window.
3. In the Port Extension section, check the
 Enabled checkbox.

##### Automatic Port
 Extension

The automatic port extension feature
 automatically performs calculations related to port extension, such
 as delay, electrical length, and loss. You can use automatic port
 extension even when the added components have unknown electrical
 delay or electrical characteristics. To determine the appropriate
 delay correction, InstrumentStudio analyzes the measured response of
 a known open or short termination.

##### Perform Measurements with Automatic Port
 Extension

Complete the following steps to perform an open or short measurement with the
 automatic port extension feature:

Ensure that you have
 InstrumentStudio 2026 Q2 or later installed.

1. Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] button to open the Network Analyzer
 Settings window.
2. Go to the Correction tab of the
 window.
3. In the Port Extension section, check the
 Enabled checkbox.
4. Click Auto Port Extension to open the
 Auto Port Extension
 window.
5. In the Select Ports dropdown menu,
 select the ports that you want to measure.
6. Optional: 
 Configure the following settings: 
 Enable or disable loss measurements
 Apply regularization to loss measurements
 Change frequency modes
7. Click Measure Open or Measure
 Short. 
 Another Auto Port Extension
 window appears.
8. Follow the instructions of the Auto Port
 Extension window.

Network Analyzer Settings

<!--NI_TOPIC bundle=instrumentstudio path=new-features-and-changes.html language=enus -->
## TOPIC 00040: InstrumentStudio New Features and Changes

- bundle_id: `instrumentstudio`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/new-features-and-changes.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of InstrumentStudio. Discover what is new in the latest releases of InstrumentStudio.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your vers

### InstrumentStudio
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of InstrumentStudio.

InstrumentStudio

Note

Release Notes

Related information:

- Release Notes

#### InstrumentStudio
 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in InstrumentStudio 2026 Q2.

##### New Hardware Support

This version of InstrumentStudio adds support for the following hardware and panel
 type:

- Analog output panels for PXI DAQ

##### Layouts

Edit Layout

- The Edit Layout window displays each device only once.
- You can create multiple counter input panels for the same device.
- You can assign each subsystem of the same device to different panels. For example, you
 can assign analog input measurements to one panel and analog output measurements to a
 different panel for the same device.
- Searching for a specific instrument, such as Analog Input ,
 returns all devices that support that instrument type.

Note

##### RF
 Signal Generator

- Added functionality to configure script triggers.
- Added functionality to configure markers 1-3.

##### Network
 Analyzer

- Introduced the automatic port extension functionality.

Related concepts:

- Edit an Existing Layout

Related reference:

- NI-DAQmx
- RF Signal Generators
- Network Analyzers

#### InstrumentStudio
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in InstrumentStudio 2026 Q1.

##### New Hardware Support

This version of InstrumentStudio adds support for the following hardware and panel
 type:

- Analog input panels for PXI DAQ

##### RF
 Signal Analyzer

- Added autolevel capability for the Spectrum Analyzer RFmx
 personality.
- Added support for the Demod RFmx personality.

##### RF
 Signal Generator

- When you save an RF Signal Generator panel, InstrumentStudio
 saves the content of the scripts as well.

##### Network
 Analyzer

- InstrumentStudio now reports the correction level for each trace individually.

Related reference:

- NI-DAQmx
- RF Signal Analyzers
- RF Signal Generators
- Network Analyzers

#### 2025 Q4

October 2025

##### Oscilloscopes

- Added support for specifying the measurement units (in volts or amperes) of a
 connected probe.

##### RF
 Signal Generator

- Added support for additional file types for arbitrary waveform generation.
- Added support for editing script content when operating in
 Script mode.
- The use of Script mode is no longer limited to debugging an
 external session.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Sequencer Tool
  - Added support for the Network Analyzer panel type.
  - Added support for parameter sweeps in RF Signal Analyzer steps.
  - Added support for parameter sweeps in RF Signal Generator steps.

Related concepts:

- Sequencer Tool

Related reference:

- RF Signal Generators
- Oscilloscopes

Related information:

- Measurement Plug-Ins User Manual

#### 2025 Q3

July 2025

Added support for in-product calibration without Measurement and Automation Explorer
 (MAX).

##### Network Analyzer

- Added support for CW time sweep.
- Added group delay trace.

##### RF Signal Analyzer (RFmx)

- Added support for importing .s2p files to facilitate the
 configuration of the Noise Figure measurement.

##### SMU/Power Supply

- The PXIe-4051 now supports power and resistance channel operating modes.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Measurement Plug-Ins
  - Added support for the "1D array of XY data" data type for measurement
 plug-ins.
- Sequencer Tool
  - Added support for the RF Signal Analyzer panel type.
  - Added support for the RF Signal Generator panel type.
  - Added support for single-channel sweep and
 two-channel sweep modes to sequences on DC power instrument panels.

Related concepts:

- Sequencer Tool

Related reference:

- Network Analyzers
- RF Signal Analyzers

Related information:

- Measurement Plug-Ins User Manual

<!--NI_TOPIC bundle=instrumentstudio path=ni-daqmx-supported-hw.html language=enus -->
## TOPIC 00041: NI-DAQmx

- bundle_id: `instrumentstudio`
- source_path: `ni-daqmx-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-daqmx-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-DAQmx hardware with a DAQ Analog Input (AI) or Analog Output (AO) instrument in InstrumentStudio. 7 Supported DAQ Instruments Model Name First Available PXI-4461 2026 Q1 (AI), 2026 Q2 (AO) PXI-4462 2026 Q1 (AI) PXI-4472 2026 Q1 (AI) PXI-4495 2026 Q1 (AI) PXI-4496 2026 Q1

### NI-DAQmx

You can use the following NI-DAQmx hardware with a DAQ Analog Input (AI) or Analog
 Output (AO) instrument in InstrumentStudio.

| Model Name | First Available |
| --- | --- |
| PXI-4461 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-4462 | 2026 Q1 (AI) |
| PXI-4472 | 2026 Q1 (AI) |
| PXI-4495 | 2026 Q1 (AI) |
| PXI-4496 | 2026 Q1 (AI) |
| PXI-4498 | 2026 Q1 (AI) |
| PXI-6115 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6120 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6122 | 2026 Q1 (AI) |
| PXI-6123 | 2026 Q1 (AI) |
| PXI-6132 | 2026 Q1 (AI) |
| PXI-6133 | 2026 Q1 (AI) |
| PXI-6143 | 2026 Q1 (AI) |
| PXI-6220 | 2026 Q1 (AI) |
| PXI-6221 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6224 | 2026 Q1 (AI) |
| PXI-6225 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6229 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6230 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6232 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6233 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6236 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6238 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6239 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6250 | 2026 Q1 (AI) |
| PXI-6251 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6254 | 2026 Q1 (AI) |
| PXI-6255 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6259 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6280 | 2026 Q1 (AI) |
| PXI-6281 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6284 | 2026 Q1 (AI) |
| PXI-6289 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXI-6704 | 2026 Q2 (AO) |
| PXI-6711 | 2026 Q2 (AO) |
| PXI-6713 | 2026 Q2 (AO) |
| PXI-6722 | 2026 Q2 (AO) |
| PXI-6723 | 2026 Q2 (AO) |
| PXI-6733 | 2026 Q2 (AO) |
| PXIe-4300 | 2026 Q1 (AI) |
| PXIe-4302 | 2026 Q1 (AI) |
| PXIe-4303 | 2026 Q1 (AI) |
| PXIe-4304 | 2026 Q1 (AI) |
| PXIe-4305 | 2026 Q1 (AI) |
| PXIe-4309 | 2026 Q1 (AI) |
| PXIe-4310 | 2026 Q1 (AI) |
| PXIe-4322 | 2026 Q2 (AO) |
| PXIe-4330 | 2026 Q1 (AI) |
| PXIe-4331 | 2026 Q1 (AI) |
| PXIe-4339 | 2026 Q1 (AI) |
| PXIe-4340 | 2026 Q1 (AI) |
| PXIe-4353 | 2026 Q1 (AI) |
| PXIe-4357 | 2026 Q1 (AI) |
| PXIe-4463 | 2026 Q2 (AO) |
| PXIe-4464 | 2026 Q1 (AI) |
| PXIe-4466 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-4467 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-4468 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-4480 | 2026 Q1 (AI) |
| PXIe-4481 | 2026 Q1 (AI) |
| PXIe-4492 | 2026 Q1 (AI) |
| PXIe-4496 | 2026 Q1 (AI) |
| PXIe-4497 | 2026 Q1 (AI) |
| PXIe-4498 | 2026 Q1 (AI) |
| PXIe-4499 | 2026 Q1 (AI) |
| PXIe-6124 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6251 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6259 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6321 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6323 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6341 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6343 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6345 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6349 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6351 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6353 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6355 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6356 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6357 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6358 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6361 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6363 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6365 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6366 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6368 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6375 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6376 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6378 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6381 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6383 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6386 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6396 | 2026 Q1 (AI), 2026 Q2 (AO) |
| PXIe-6738 | 2026 Q2 (AO) |
| PXIe-6739 | 2026 Q2 (AO) |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=ni-dcpower-supported-hw.html language=enus -->
## TOPIC 00042: NI-DCPower

- bundle_id: `instrumentstudio`
- source_path: `ni-dcpower-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-dcpower-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-DCPower hardware with an SMU or VPS instrument in InstrumentStudio: 1 Supported SMU/VPS Devices Model Name First Available PXIe-4051 2023 PXIe-4112 2018 PXIe-4113 2018 PXIe-4135 2018 PXIe-4135 (40W) 2021 PXIe-4136 2018 PXIe-4137 2018 PXIe-4137 (40W) 2021 PXIe-4138 2018 P

### NI-DCPower

You can use the following NI-DCPower hardware with an SMU or VPS instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-4051 | 2023 |
| PXIe-4112 | 2018 |
| PXIe-4113 | 2018 |
| PXIe-4135 | 2018 |
| PXIe-4135 (40W) | 2021 |
| PXIe-4136 | 2018 |
| PXIe-4137 | 2018 |
| PXIe-4137 (40W) | 2021 |
| PXIe-4138 | 2018 |
| PXIe-4139 | 2018 |
| PXIe-4139 (40W) | 2020 |
| PXIe-4140 | 2018 |
| PXIe-4141 | 2018 |
| PXIe-4142 | 2018 |
| PXIe-4143 | 2018 |
| PXIe-4144 | 2018 |
| PXIe-4145 | 2018 |
| PXIe-4147 | 2019 SP1 |
| PXIe-4150 | 2024 |
| PXIe-4151 | 2023 |
| PXIe-4154 | 2018 |
| PXIe-4162 | 2018 |
| PXIe-4163 | 2018 |
| PXIe-4190 1 | 2021 Q4 |
| PXIe-4190 (500 kHz) 1 | 2022 Q3 |
| PXI-4110 | 2018 |
| PXI-4130 | 2018 |
| PXI-4132 | 2018 |
| 1The PXIe-4190 and PXIe-4190 (500 kHz) can be used with either an SMU/Power Supply instrument or an LCR meter in InstrumentStudio |  |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=ni-dmm-supported-hw.html language=enus -->
## TOPIC 00043: NI-DMM

- bundle_id: `instrumentstudio`
- source_path: `ni-dmm-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-dmm-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-DMM hardware with a Digital Multimeter instrument in InstrumentStudio: 2 Supported Digital Multimeters Model Name First Available PXIe-4080 2018 PXIe-4081 2018 PXIe-4082 2018 PXI-4065 2018 PXI-4070 2018 PXI-4071 2018 PXI-4072 2018 PCIe-4065 2018 PCI-4065 2018 USB-4065 20

### NI-DMM

You can use the following NI-DMM hardware with a Digital Multimeter instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-4080 | 2018 |
| PXIe-4081 | 2018 |
| PXIe-4082 | 2018 |
| PXI-4065 | 2018 |
| PXI-4070 | 2018 |
| PXI-4071 | 2018 |
| PXI-4072 | 2018 |
| PCIe-4065 | 2018 |
| PCI-4065 | 2018 |
| USB-4065 | 2018 |
| PCI-4070 | 2018 |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=ni-fgen-supported-hw.html language=enus -->
## TOPIC 00044: NI-FGEN

- bundle_id: `instrumentstudio`
- source_path: `ni-fgen-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-fgen-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-FGEN hardware with a Waveform Generator instrument in InstrumentStudio: 3 Supported Waveform Generators Model Name First Available PXIe-5413 (1-channel) 2018 PXIe-5413 (2-channel) 2018 PXIe-5423 (1-channel) 2018 PXIe-5423 (2-channel) 2018 PXIe-5433 (1-channel) 2018 PXIe-

### NI-FGEN

You can use the following NI-FGEN hardware with a Waveform Generator instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-5413 (1-channel) | 2018 |
| PXIe-5413 (2-channel) | 2018 |
| PXIe-5423 (1-channel) | 2018 |
| PXIe-5423 (2-channel) | 2018 |
| PXIe-5433 (1-channel) | 2018 |
| PXIe-5433 (2-channel) | 2018 |
| PXIe-5442 | 2018 |
| PXIe-5450 | 2018 |
| PXIe-5451 | 2018 |
| PXI-5402 | 2018 |
| PXI-5404 | 2018 |
| PXI-5406 | 2018 |
| PXI-5412 | 2018 |
| PXI-5421 | 2018 |
| PXI-5422 | 2018 |
| PXI-5441 | 2018 |
| PCI-5402 | 2018 |
| PCI-5406 | 2018 |
| PCI-5412 | 2018 |
| PCI-5421 | 2018 |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=ni-rfsg-supported-hw.html language=enus -->
## TOPIC 00045: NI-RFSG

- bundle_id: `instrumentstudio`
- source_path: `ni-rfsg-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-rfsg-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-RFSG hardware with a RF Signal Generator instrument in InstrumentStudio: 5 Supported RF Signal Generators Model Name First Available PXIe-5820 2021 PXIe-5830 2021 PXIe-5831 2021 PXIe-5832 2021 PXIe-5840 2021 PXIe-5841 2021 PXIe-5842 2022 PXIe-5860 2024 Q3

### NI-RFSG

You can use the following NI-RFSG hardware with a RF Signal Generator instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-5820 | 2021 |
| PXIe-5830 | 2021 |
| PXIe-5831 | 2021 |
| PXIe-5832 | 2021 |
| PXIe-5840 | 2021 |
| PXIe-5841 | 2021 |
| PXIe-5842 | 2022 |
| PXIe-5860 | 2024 Q3 |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=ni-scope-supported-hw.html language=enus -->
## TOPIC 00046: NI-SCOPE

- bundle_id: `instrumentstudio`
- source_path: `ni-scope-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/ni-scope-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-SCOPE hardware with an Oscilloscope instrument in InstrumentStudio: 4 Supported Oscilloscopes Model Name First Available PXIe-5105 2018 PXIe-5110 2018 PXIe-5111 2018 PXIe-5113 2018 PXIe-5113 2018 PXIe-5122 2018 PXIe-5160 (2-channel) 2018 PXIe-5160 (4-channel) 2018 PXIe-5

### NI-SCOPE

You can use the following NI-SCOPE hardware with an Oscilloscope instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-5105 | 2018 |
| PXIe-5110 | 2018 |
| PXIe-5111 | 2018 |
| PXIe-5113 | 2018 |
| PXIe-5113 | 2018 |
| PXIe-5122 | 2018 |
| PXIe-5160 (2-channel) | 2018 |
| PXIe-5160 (4-channel) | 2018 |
| PXIe-5162 (2-channel) | 2018 |
| PXIe-5162 (4-channel) | 2018 |
| PXIe-5163 | 2018 SP2 |
| PXIe-5164 | 2018 |
| PXIe-5170 (4-channel) | 2018 |
| PXIe-5170 (8-channel) | 2018 |
| PXIe-5171 (8-channel) | 2018 |
| PXIe-5172 (4-channel) | 2018 |
| PXIe-5172 (8-channel, 325T) | 2018 |
| PXIe-5172 (8-channel, 410T) | 2018 |
| PXIe-5185 | 2018 |
| PXIe-5185 (1MΩ) | 2018 |
| PXIe-5186 | 2018 |
| PXIe-5186 (1MΩ) | 2018 |
| PXIe-5622 | 2018 |
| PXIe-5622 (DD) | 2018 |
| PXI-5105 | 2018 |
| PXI-5114 | 2018 |
| PXI-5122 | 2018 |
| PXI-5124 | 2018 |
| PXI-5142 | 2018 |
| PXI-5152 | 2018 |
| PXI-5153 | 2018 |
| PXI-5154 | 2018 |
| PXI-5922 | 2018 |
| PCI-5105 | 2018 |
| PCI-5114 | 2018 |
| PCI-5122 | 2018 |
| PCI-5124 | 2018 |
| PCI-5142 | 2018 |
| PCI-5152 | 2018 |
| PCI-5153 | 2018 |
| PCI-5154 | 2018 |
| PCI-5922 | 2018 |
| PCIe-5155 | 2018 |
| USB-5132 | 2018 |
| USB-5133 | 2018 |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=osc.html language=enus -->
## TOPIC 00047: Oscilloscopes

- bundle_id: `instrumentstudio`
- source_path: `osc.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/osc.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Oscilloscope panel to set up and configure your Oscilloscope instruments. Oscilloscope Setup Actions You can configure the setup of an oscilloscope with the Auto setup or the Default setup option. To change setup mode, click the arrow next to the button that displays the currently selected s

### Oscilloscopes

Use the Oscilloscope panel to set up and configure your Oscilloscope
 instruments.

Parent topic:

Configure Device Settings

#### Oscilloscope Setup Actions

You can configure the setup of an oscilloscope with the Auto setup or
 the Default setup option.

To change setup mode, click the arrow next to the button that displays the currently
 selected setup mode.

Auto setup

Default setup

##### Settings Changed by Auto Setup

Setting an oscilloscope to Auto setup changes the following settings to
 the following values:

| General Settings | Value |
| --- | --- |
| Acquisition Mode | Normal |
| Reference Clock | Internal |

Note

Auto
 setup

Auto setup

| Vertical Settings | Value |
| --- | --- |
| Vertical Coupling | Unchanged by Auto setup |
| Vertical Bandwidth | Full |
| Vertical Range | Changed by Auto setup |
| Vertical Offset | 0 V |
| Probe Attenuation | Unchanged by Auto setup |
| Input Impedance | Unchanged by Auto setup |

| Horizontal Settings | Value |
| --- | --- |
| Sample Rate | Changed by Auto setup |
| Min Record Length | Changed by Auto setup |
| Enforce Realtime | True |
| Number of Records | 1 |

| Triggering Settings | Value |
| --- | --- |
| Trigger Type | Edge if signal present, otherwise Immediate |
| Trigger Channel | Lowest numbered channel with a signal present |
| Trigger Slope | Positive |
| Trigger Coupling | DC |
| Reference Position | 50% |
| Trigger Level | 50% of signal on trigger channel |
| Trigger Delay | 0 |
| Trigger Holdoff | 0 |
| Trigger Output | None |

#### Set the Sample Rate and the Record Length
 Manually

By default, InstrumentStudio optimizes the record length or the sample rate of an
 oscilloscope when taking measurements.

##### Configure the Record Length

Data Display

Live

On Demand

##### Manual Override Mode

To configure larger records, use Manual
 Override mode. Manual Override mode allows for the
 configuration of both the sample rate and the record length of an
 oscilloscope.

Note

Manual Override

Complete the
 following steps to enable Manual Override mode:

1. Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon for the instrument to open the Instrument
 Settings window.
2. On the Acquisition tab, click the Manual
 Override mode toggle. 
 The toggle is in the On position.
3. Enter the desired values for Sample Rate and
 Record Length.

Note

Manual
 Override

Sample
 rate

1 kS/s

Record length

3.5 MS

#### Acquisition Status

You can determine the current state of an acquisition by looking at the acquisition
 status icon. The acquisition status icon is in the Horizontal & Acq.
 header of an oscilloscope panel.

Triggered

Auto

Auto

Note

Auto

Waiting

Stopped

#### Interpolation Methods

You can set the interpolation method of an oscilloscope acquisition from the
 Instrument Settings window.

Click the dropdown menu for the Interpolation method setting in the
 Acquisition tab of the Instrument
 Settings window.

You can set interpolation to one of the following settings:

No interpolation

Auto

Note

Manual

Auto

On

On

- The Random Interleaved Sampling (RIS) sampling
 method is set for the oscilloscope.
- The acquisition uses the peak detect sample mode.
- The waveform has enough data and does not need interpolation.

#### Sampling Methods

Depending on the device, you can select different sampling methods from the
 Instrument Settings window.

Click the dropdown menu for the
 Sampling method setting in the Acquisition
 tab of the Instrument Settings window. You can set sampling to one of
 the following methods:

Real time

RIS

Note

#### Sample Modes

You can select different sample modes from the Instrument
 Settings window.

Sample mode

Acquisition

Instrument Settings

Sample

Peak detect

Peak detect

Averaging

#### Add FFT Channels and Markers

You can use FFT channels with an oscilloscope to measure the amplitude and the
 frequency of a sample. You can also fetch more detailed measurements and search for peaks with
 the help of markers.

##### Create FFT Channels

1. From a large oscilloscope panel, click the
 FFT button in the Add Channels section. A
 frequency graph appears.
2. Select a Source for the
 FFT channel. You can select any single channel that already exists.
3. Select a Window function
 for the FFT channel.
4. (Optional) Configure additional settings for
 the FFT channel by clicking the icon next to the FFT channel. For more information, see Search for and Compute Peaks .

##### Create Markers

A marker fetches the amplitude (y-location) of a particular sample at the specified
 frequency (x-location) of a particular sample.

Note

Complete the following steps to
 create markers:

1. Select the Markers 
 dropdown menu in the Frequency Graph header.
2. Select Markers: On to enable markers. The
 Markers table appears below the frequency graph.
3. From the Markers table,
 select the marker that you want to configure. By default, only Marker 0 
 is enabled. Note You can enable markers by
 selecting a marker from the Markers table. Then, change the
 marker mode from Off to Normal. You can enable up to
 12 markers.
4. Select the FFT channel that you want to measure
 with the selected marker.
5. Enter the frequency where you want to place the
 marker. The amplitude of the signal at the frequency of the marker is displayed in the
 Level section of the marker toolbar. Note You can view and edit the frequency of
 all enabled markers in the Markers table. The
 Markers table also displays the current level, mode, and source
 channel of the markers.

##### Identify and Compute Peaks

To use the peak search functions to locate peaks, you must first enable at least one
 FFT channel and one marker.

The controls for the peak search functions ([IMAGE alt='An icon of four graphs with different peaks that allow you to search for peaks.' src='GUID-BABB9A18-6A36-42A1-85BF-E1E8C21B151C-a5.png']) are on the left side of the Frequency tab.

- The highest peak
- The next highest peak
- A peak that is directly adjacent to the marker (both left or right)

###### Compute Peaks Using Peak Threshold and
 Peak Excursion

You can configure peak threshold and peak excursion settings by selecting the [IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png'] icon in the Frequency tab. The [IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png'] icon is directly to the right of the peak search functions ([IMAGE alt='An icon of four graphs with different peaks that allow you to search for peaks.' src='GUID-BABB9A18-6A36-42A1-85BF-E1E8C21B151C-a5.png']).

Peak threshold defines the minimum amplitude level that a sample must rise
 above to be considered a peak. You can set a peak threshold value without setting a peak
 excursion value. Without peak excursion, InstrumentStudio considers a peak eligible for
 every amplitude measurement that is above the peak threshold value.

Peak excursion
 defines the minimum amplitude variation that is required in a signal to be considered a
 peak. Peak excursion is always specified in relation to a peak threshold value.

- The signal rises above the threshold level
- The rise of the signal above the peak threshold matches or exceeds the peak excursion
 value
- The fall of the signal from above the peak threshold matches or exceeds the peak
 excursion value
- The signal falls below the threshold level

[IMAGE alt='A graph that explains how peak threshold and peak excursion values function.' src='GUID-FEE20D43-6E55-4F52-B314-45F618FFE6AD-a5.gif']

| Peak | Peak Eligibility | Peak Characteristics |
| --- | --- | --- |
| Peak 1 | Peak 1 meets the excursion condition and is an eligible peak. | Rises above the peak threshold The rise above the peak threshold matches or exceeds the peak excursion value The fall from above the peak threshold matches or exceeds the peak excursion value Falls below the threshold level |
| Peak 2 | Peak 2 does not meet the excursion condition and is not an eligible peak. | Rises above the peak threshold Does not rise above the peak threshold by at least the peak excursion value |
| Peak 3 | Peak 3 does not meet the excursion condition and is not an eligible peak. | Rises above the peak threshold The rise above the peak threshold matches or exceeds the peak excursion value The fall from above the peak threshold does not exceed the peak excursion value The signal rises above the amplitude level of Peak 3 |
| Peak 4 | Peak 4 meets the excursion condition and is an eligible peak. | Rises above the peak threshold During the rise, Peak 4 slightly falls, which happens after Peak 3 However, the rise above the peak threshold matches or exceeds the peak excursion value The fall from above the peak threshold matches or exceeds the peak excursion value Falls below the threshold level |
| Peak 5 | Peak 5 is not detected as a peak. | Does not rise above the threshold level |
| Peak 6 | Peak 6 meets the excursion condition and is an eligible peak. | Rises above the peak threshold The rise above the peak threshold matches or exceeds the peak excursion value During the fall, the signal slightly rises, which appears as Peak 7 However, the signal does not rise above the amplitude level of Peak 6 before the signal falls again The total fall, which starts at the amplitude level of Peak 6, exceeds the peak excursion value Falls below the peak threshold |
| Peak 7 | Peak 7 does not meet the excursion condition and is not an eligible peak. | Falls below the peak threshold The fall from above the peak threshold matches or exceeds the peak excursion value The rise above the peak threshold does not match or exceed the peak excursion value |

##### FFT Averaging Modes

You can perform averaged measurements on an FFT channel to improve measurement accuracy
 or to help compensate for a low signal-to-noise ratio.

To configure FFT averaging modes, click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon for the FFT channel, which opens the Software Channel
 Settings window.

Disabled

RMS

Peak hold

- Configuring a measurement system
- Applying limit testing to a frequency spectrum
- Applying upper limit testing to a frequency spectrum

##### Measure Power Spectral Density

Power spectral density measures the power content compared to the frequency of a
 signal. You can view the power spectral density of a signal when you analyze data in the
 frequency domain. Power spectral density helps you determine which frequency ranges have strong
 or weak variations in power.

1. Add an oscilloscope to the large panel.
2. [Create an FFT
 channel](osc.html#GUID-216237BC-8122-47EB-A6F8-43992F63D2FC) by selecting the FFT button in the Add
 Channels section of the large panel. 
 A frequency chart opens below the time chart of the large panel.
3. Configure the FFT Axis settings in the following way:
  1. In the header of the frequency chart, select the Chart
 Options button.
  2. In the Y-axis section, set Units to
 V/√(Hz) or dBm/Hz.
  3. In the X-axis section, set Scaling to
 Logarithmic.
4. Run the panel if it does not already run. 
 InstrumentStudio plots the power spectral density data on the
 Frequency chart.

Chart Options

<!--NI_TOPIC bundle=instrumentstudio path=overview.html language=enus -->
## TOPIC 00048: InstrumentStudio Overview

- bundle_id: `instrumentstudio`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/overview.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: InstrumentStudio provides an integrated approach to interactive PXI measurements. Use InstrumentStudio to unify your display, export instrument configurations to code, and monitor and debug an automated test system. You can use InstrumentStudio for free. You can also purchase an InstrumentStudio Pro

### InstrumentStudio
 Overview

InstrumentStudio provides an integrated approach to interactive PXI measurements. Use
 InstrumentStudio to unify your display, export instrument configurations to code, and
 monitor and debug an automated test system. You can use InstrumentStudio for free. You can
 also purchase an InstrumentStudio Professional license to access additional
 features.

#### InstrumentStudio Key
 Features

InstrumentStudio has the following key features and capabilities:

##### InstrumentStudio

- View PXI instrument data on unified displays
- Capture multi-instrument screenshots and measurement results
- Save project-level configurations for specific DUTs
- Export instrument configurations to different programming environments
- Debug running test applications

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] InstrumentStudio Professional

For more information on the
 Professional license, see *Select Your InstrumentStudio Software Edition*
 in the *Related Information* section.

- Support for SCPI instruments and SCPI instrument panels
- Create, edit, and configure sequences with the Sequencer Tool
- Connect to plug-in libraries
- Configure, control, and monitor measurement plug-ins
- Integration with TestStand through Measurement Plug-Ins

Note

Features that are only available with an InstrumentStudio Professional license
 are marked with the [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] symbol.

Related concepts:

- Sequencer Tool

Related information:

- Select Your InstrumentStudio Software Edition
- Measurement Plug-Ins User Manual

<!--NI_TOPIC bundle=instrumentstudio path=panels-and-layouts.html language=enus -->
## TOPIC 00049: Panels and Layouts

- bundle_id: `instrumentstudio`
- source_path: `panels-and-layouts.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/panels-and-layouts.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: An InstrumentStudio layout consists of one large panel and up to four small panels. The large panel is located in the center of the screen. The large panel includes a measurement graph. Small panels are located on the right sidebar. The small panels include channel settings. You can combine multiple

### Panels and Layouts

An InstrumentStudio layout consists of one large panel and up to four small
 panels.

The large panel is located in the center of the screen. The large panel includes a
 measurement graph.

Small panels are located on the right sidebar. The small panels include channel settings.

Note

Click the Edit layout ([IMAGE alt='An icon of a layout that contains one large and three small panels. You can use this button to edit layouts in InstrumentStudio.' src='GUID-D5ACAD8B-108A-4F3E-BA47-EB522506BDB1-a5.gif']) button in the instrument header menu to adjust the arrangement of the soft front
 panels and their associated devices.

- The layout must have exactly one large panel.
- The layout can have up to four small panels.
 Small panels are not required.
- Place oscilloscopes in a large panel.
- Only add oscilloscopes of the same model to the same panel.

Note

Parent topic:

Configure Panels and Layouts

<!--NI_TOPIC bundle=instrumentstudio path=pin-map-errors-warning.html language=enus -->
## TOPIC 00050: Pin Map Errors and Warnings

- bundle_id: `instrumentstudio`
- source_path: `pin-map-errors-warning.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/pin-map-errors-warning.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: InstrumentStudio highlights errors and warnings in project pin map files (.pinmap). Error and Warning Behavior Common causes of pin map errors and warnings include the following: Improperly formatted pin map files Pin map settings that do not correspond to configurations in your test system To deter

### Pin Map Errors and Warnings

InstrumentStudio highlights errors and warnings in project pin map files
 (.pinmap).

#### Error and Warning Behavior

- Improperly formatted pin map files
- Pin map settings that do not correspond to configurations in your test
 system

Pin Map Editor

| Notification Type | Expected Behavior |
| --- | --- |
| Error | Panels will not function with the selected pin map. InstrumentStudio reverts to using the default instrument and channel views. You must address the error before you can use the pin map file. |
| Warning | You can use the pin map, but errors might occur at run time. Determine the source of the warning and make the necessary corrections with the Pin Map Editor before run time. |

For detailed information on pin map files, see *Pin Map File XML
 Structure (TSM)* in the *Related Information* section.

Parent topic:

Pin Maps

Related information:

- Pin Map File XML Structure (TSM)

<!--NI_TOPIC bundle=instrumentstudio path=pin-maps.html language=enus -->
## TOPIC 00051: Pin Maps

- bundle_id: `instrumentstudio`
- source_path: `pin-maps.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/pin-maps.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pin maps define the following elements of a test site: Test instruments and hardware Sites and pins connected to a DUT How the test instruments and hardware connect to DUT pins InstrumentStudio preserves the mappings that are created in TestStand Semiconductor Module (TSM) pin maps. The following se

### Pin Maps

*Pin maps* define the following elements of a test site:

- Test instruments and hardware
- Sites and pins connected to a DUT
- How the test instruments and hardware connect to DUT pins

InstrumentStudio preserves the mappings that are created in TestStand Semiconductor Module
 (TSM) pin maps.

The following sections provide specific information on how to use pin maps in
 InstrumentStudio:

- [Set an Active Project Pin Map](set-active-project-pin-map.html) Set an active pin map to filter your view of connected sites, pins, and devices within your test system in InstrumentStudio.
- [Create a New Pin Map](create-new-pin-map.html) Use the Pin Map Editor to create new pin maps in InstrumentStudio.
- [Select a Default Pin Map](select-default-pin-map.html) You can select a default pin map to add that pin map to all new projects that you create in InstrumentStudio.
- [Remove a Default Pin Map](remove-default-pin-map.html) Complete the following steps to remove an existing default pin map preference:
- [Add Pin Map Files to a Project](add-pin-map-file.html) You can use pin maps that you create outside of InstrumentStudio by adding the existing pin map file to your project.
- [Edit a Pin Map](edit-pin-map.html) Use the Pin Map Editor to make changes to a project pin map.
- [Using the Site Filter](using-site-filter.html) After you set an active pin map in InstrumentStudio, the devices in your panel appear as pins. Use the site filter in the document toolbar to display pins from a selected site.
- [Pin Map Errors and Warnings](pin-map-errors-warning.html) InstrumentStudio highlights errors and warnings in project pin map files ( .pinmap ).

<!--NI_TOPIC bundle=instrumentstudio path=plug-ins.html language=enus -->
## TOPIC 00052: Plug-Ins

- bundle_id: `instrumentstudio`
- source_path: `plug-ins.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/plug-ins.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: With InstrumentStudio, you can host plug-in libraries, build application-specific plug-ins, and use measurement plug-ins that work across different products. A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license. This feature is only available with

### Plug-Ins

With InstrumentStudio, you can host plug-in libraries, build application-specific
 plug-ins, and use measurement plug-ins that work across different
 products.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

The following sections provide information on how to use plug-ins in
 InstrumentStudio:

- [InstrumentStudio Plug-Ins](hosted-plugins.html) You can use InstrumentStudio to create and host application-specific plug-ins written in LabVIEW or C#. These plug-ins run together with the InstrumentStudio panels that are used to configure PXI instruments.
- [Measurement Plug-Ins](meas-plugins.html#GUID-11917A5C-A31B-4F5E-9D24-78D8E4989B30) A measurement plug-in helps you create reusable measurements for supported devices that function across multiple products.
- [Connect to a Plug-In Library](connecting-to-plug-in-library.html) A plug-in library is an HTTP web API that contains services that allow you to find and download plug-ins. Plug-in libraries allow you to share and collaborate across teams.

<!--NI_TOPIC bundle=instrumentstudio path=reference-levels-gating.html language=enus -->
## TOPIC 00053: Customize Oscilloscope Measurements

- bundle_id: `instrumentstudio`
- source_path: `reference-levels-gating.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/reference-levels-gating.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use Reference Levels and Gating to customize the measurements displayed in the measurement table. Click Add/Remove in the Measurements section of an oscilloscope panel. Click the Settings tab of the Measurements window to configure oscilloscope measurements. Gating Use gating options to sele

### Customize Oscilloscope Measurements

You can use Reference Levels and Gating to customize
 the measurements displayed in the measurement table.

1. Click Add/Remove in the Measurements
 section of an oscilloscope panel.
2. Click the Settings tab of the
 Measurements window to configure oscilloscope measurements.

#### Gating

Use gating options to select the region of captured data that is used to perform
 measurements. This region of data appears in the measurement table.

Screen

Record

Custom

Position 1

Position 2

#### Reference Levels

You can customize the oscilloscope measurements that appear on the measurement table.
 Adjust the Reference Levels and the High-Low Method from the
 Settings tab of the Measurements
 window.

##### High, Mid, and Low Reference
 Levels

- Ascertain rise and fall times
- Calculate waveform cycles
- Customize certain oscilloscope measurement types

In InstrumentStudio, you must set reference levels by absolute levels or by the
 percentage of the waveform that you want to acquire. The following oscilloscope measurement
 types are calculated using reference levels:

| High Ref Level Mid Ref Level Low Ref Level Cycle RMS | Cycle Mean Period Rise Time | Fall Time Rise Rate Fall Rate |
| --- | --- | --- |

##### Reference Level Unit

Use the Reference Level Unit settings to specify whether reference
 levels are interpreted as percentages of the waveform or as absolute levels.

Percentage

High-Low

Absolute

##### High-Low Method

If you set the Reference Level Unit setting to
 Percentage, you can configure how the state levels are computed by
 selecting the High-Low method. The following configuration options are
 available:

Auto-select

Peak High-Low

Auto-select
 High-Low

- A square wave, by ignoring the overshoot and the undershoot
- A triangle wave, where the Histogram High-Low method fails

Histogram

Peak

Related reference:

- Export Configurations

<!--NI_TOPIC bundle=instrumentstudio path=remote_panel.html language=enus -->
## TOPIC 00054: Configure Remote RF Signal Analyzer Panels

- bundle_id: `instrumentstudio`
- source_path: `remote_panel.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/remote_panel.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add a remote RF signal analyzer panel to your project to use remote RFmx hardware. Consider the following limitations when you use a remote RF signal analyzer panel: You can only use the following personalities for remote a remote RF signal analyzer panel: Spectrum Analyzer LTE WLAN Bluetoot

### Configure Remote RF Signal Analyzer
 Panels

You can add a remote RF signal analyzer panel to your project to use remote RFmx
 hardware.

- You can only use the following personalities for remote a remote
 RF signal analyzer panel:
  - Spectrum Analyzer
  - LTE
  - WLAN
  - Bluetooth
  - NR
- The remote hardware must be present on the same network in order
 to be remotely connected.
- The remote panels perform best when the remote hardware is
 within your local facility topology.
- You cannot create a remote panel for a device that is in use by
 another remote client.
- You cannot remotely monitor a remote session that is hosted on
 another client.

#### Overview of Remote
 Panel Connections

The NI gRPC-device server facilitates
 remote panel connections. You do not need to install NI drivers on
 the client that you use to remotely access a remote RF signal
 analyzer panel. You must install the required drivers on the server
 that hosts the hardware.

Figure 2.

[IMAGE alt='Diagram showing the NI gRPC server-client architecture for remote RF Signal Analyzer panel connections.' src='GUID-8BA3A403-1211-4252-B0A1-1668440146B6-a5.png']

Parent topic:

Configure Panels and Layouts

<!--NI_TOPIC bundle=instrumentstudio path=remove-default-pin-map.html language=enus -->
## TOPIC 00055: Remove a Default Pin Map

- bundle_id: `instrumentstudio`
- source_path: `remove-default-pin-map.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/remove-default-pin-map.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to remove an existing default pin map preference: Go to File Preferences Pin and site mapping . Go to the Pin and site mapping section. Click the Clear button to remove the default pin map.

### Remove a Default Pin Map

Complete the following steps to remove an existing default pin map
 preference:

1. Go to File»Preferences»Pin and site mapping.
2. Go to the Pin and site mapping section.
3. Click the Clear button to remove the default pin map.

Parent topic:

Pin Maps

<!--NI_TOPIC bundle=instrumentstudio path=rfmx-supported-hw.html language=enus -->
## TOPIC 00056: NI-RFSA

- bundle_id: `instrumentstudio`
- source_path: `rfmx-supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/rfmx-supported-hw.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following NI-RFSA hardware with a RF Signal Analyzer instrument in InstrumentStudio: 6 Supported RF Signal Analyzers Model Name First Available PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5663 2022 Q3 PXIe-5663E 2022 Q3 PXIe-5665 2022 Q3 PXIe-5668 2022 Q3 PXIe-5668 wit

### NI-RFSA

You can use the following NI-RFSA hardware with a RF Signal Analyzer instrument in
 InstrumentStudio:

| Model Name | First Available |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5663 | 2022 Q3 |
| PXIe-5663E | 2022 Q3 |
| PXIe-5665 | 2022 Q3 |
| PXIe-5668 | 2022 Q3 |
| PXIe-5668 with PXIe-5698 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5830 | 2022 Q3 |
| PXIe-5831 | 2022 Q3 |
| PXIe-5832 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 | 2022 Q3 |
| PXIe-5842 | 2022 |
| PXIe-5860 | 2024 Q3 |

Parent topic:

Supported Hardware

<!--NI_TOPIC bundle=instrumentstudio path=rfsa.html language=enus -->
## TOPIC 00057: RF Signal Analyzers

- bundle_id: `instrumentstudio`
- source_path: `rfsa.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/rfsa.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RF Signal Analyzer panel to analyze RF signals, de-embed RF Signal Analyzer instruments, perform self-calibration, and import bitfile data. Analyzing RF Signals with an RF Signal Analyzer Create an RF signal analyzer panel to monitor RF signal analyzer instruments and configure related setti

### RF Signal Analyzers

Use the RF Signal Analyzer panel to analyze RF signals, de-embed RF Signal Analyzer
 instruments, perform self-calibration, and import bitfile data.

Parent topic:

Configure Device Settings

#### Analyzing RF Signals with an RF Signal
 Analyzer

Create an RF signal analyzer panel to monitor RF signal analyzer instruments and
 configure related settings in InstrumentStudio.

1. Create an RF signal analyzer panel by clicking New ([IMAGE alt='An icon of a plus sign with a dropdown menu that creates new instrument panels in InstrumentStudio.' src='GUID-5D359458-1C20-4043-9F6A-CB5CA3CED544-a5.png'])»RF Signal Analyzer. 
 The default spectrum analyzer view appears in the instrument
 panel.
2. Click the Personalities button at the top of the panel
 to select a personality for the measurement. 
 Note If a personality does not
 appear in the menu, ensure that InstrumentStudio [supports the
 personality](rfsa.html#GUID-16B63E00-E4F6-473F-9E73-DC9C667A0D31). Also ensure that the driver for that personality is
 installed. 
 The instrument panel and highlighted settings in the instrument
 configuration panel change based on selected personality.
3. Select the desired measurements from the settings panel using the
 ADD/REMOVE button.
4. Configure the signal directly through the panel or through the
 <Personality> Settings
 window. 
 Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon on the panel to access the
 <Personality> Settings
 window.
5. View the results and traces in the measurement pane.

##### Supported RFmx Personalities

The following list contains the RFmx personalities supported in InstrumentStudio for use
 with RF Signal Analyzer panels.

- Spectrum Analyzer
- GSM
- LTE / LTE-Advanced
- NR
- TD-SCDMA
- WCDMA
- Bluetooth
- WLAN
- Pulse
- Demod

#### De-Embedding RFSA Devices

*De-embedding* is the process of removing the effects of test fixture
 cabling and components. Applying de-embedding to an RF signal ensures more accurate results when
 reading data from your RF device. Once applied, the de-embedded signal you see at the device
 port matches the requested signal settings.

1. Click the icon to open the <Personality>
 Settings window.
2. On the Instrument tab, scroll down to the
 De-embedding section.

Enabled

Status

.s2p

Filename

.s2p

#### Perform RF Signal Analyzer
 Self-Calibration

Self-calibrate an RF signal analyzer device to ensure accurate measurements.

The accuracy of a device will naturally drift over time.
 Self-calibration ensures more accurate measurements by compensating for board-level
 temperature variations and device degradation. Self-calibration also ensures that the device
 operates within the ranges that appear in your test specifications.

##### Perform
 Self-Calibration

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»Self Calibrate... to begin self-calibration. Note InstrumentStudio warns you that the
 process might take several minutes to finish. InstrumentStudio also locks the
 instrument until the process completes.
3. Click Continue to proceed.

##### Perform Self-Calibration Range

Note

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»Self Calibrate Range... .
3. In the Steps to omit dialog box, select the steps that you want
 InstrumentStudio to skip during the self-calibration process.
4. In the Ranges field, enter the values for the desired ranges of
 self-calibration.
5. Click Continue to proceed, or Cancel to
 cancel self-calibration.

##### Check Calibration History

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»History .

#### Import Bitfile Data

Bitfiles define FPGA configurations, which allow you to customize your RF device for
 specific testing applications. Importing a bitfile to an InstrumentStudio RFSG or RFSA
 instrument loads the specified configuration on the device. The loading process also sets
 the file as the default file to associate with the device model in
 InstrumentStudio.

Note

Complete the following steps to import an existing bitfile
 for your RF device:

1. In the device panel, open the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']).
2. Click Bitfile. 
 Note The bitfile must be in
 the following
 folder:User\Public\Documents\National
 Instruments\FPGA Extensions Bitfiles\target
 name
3. Select the bitfile that you want to use and click
 OK. 
 InstrumentStudio prompts you to restart the application. You must
 restart InstrumentStudio for the changes to take effect.

InstrumentStudio now uses the selected bitfile as the
 default file for both RFSG and RFSA instruments for this device model.

Related information:

- NI-RFSA User Manual
- NI-RFSG User Manual

<!--NI_TOPIC bundle=instrumentstudio path=rfsg.html language=enus -->
## TOPIC 00058: RF Signal Generators

- bundle_id: `instrumentstudio`
- source_path: `rfsg.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/rfsg.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RF Signal Generator panel to generate RF signals, de-embed RF Signal Generator instruments, and perform self-calibration. Generate RF Signals with an RF Signal Generator Create an RF signal generator panel to monitor and configure RF signal generator settings in InstrumentStudio. Add an RF s

### RF Signal Generators

Use the RF Signal Generator panel to generate RF signals, de-embed RF Signal
 Generator instruments, and perform self-calibration.

Parent topic:

Configure Device Settings

#### Generate RF Signals with an RF Signal
 Generator

Create an RF signal generator panel to monitor and configure RF signal generator settings
 in InstrumentStudio.

1. Add an RF signal generator device to your panel by clicking New ([IMAGE alt='An icon of a plus sign with a dropdown menu that creates new instrument panels in InstrumentStudio.' src='GUID-5D359458-1C20-4043-9F6A-CB5CA3CED544-a5.png'])»RF Signal Generator.
2. Select a mode of operation with the dropdown menu on the device panel.
  - 
  - Continuous Waveform (CW) —Configures the RF signal generator to output a continuous waveform at the
 specified frequency and the specified level.
  - Arbitrary Waveform (Arb) —Configures the RF signal generator to output a complex signal according to the
 waveform and the waveform settings that are specified in an external file.
  - Script —Configures an RF signal generator to output a sequence of multiple waveforms
 according to the instructions specified in the script text. For more information
 on scripting, see NI-RFSG User Manual in the Related
 Information section.
3. Specify the type of signal to generate.
  - For a CW signal, specify the signal settings by opening the
 Instrument Settings ( ) window.
  - For an Arb signal, click the + button in
 the Selected Waveform section. Then browse for and select a
 waveform file. You can then specify the signal settings. Open the Instrument
 Settings ( ) window and go to the Arb waveform section.
4. Select Run and set the output to ON. The signal
 generates with the settings that you specify. 
 Note 
 In CW mode, the panel starts running immediately. To output a
 generated waveform, set the output switch on the device panel to
 ON.
 In Arb mode, you must first select a waveform, then press
 Run.
 In Arb mode, the panel continues to run and generate the waveform
 unless you set the Waveform repetition mode to
 Finite. You can configure this setting in the
 Instrument Settings ([IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png']) window. When you set this mode to Finite, the panel
 outputs the specified number of repetitions and then stop.

Related tasks:

- Create and Edit a Layout

Related information:

- NI-RFSG User Manual

##### Arbitrary Waveform Properties

Settings and values associated with waveforms generated in Arb
 mode.

When you change a waveform, the waveform property values update to reflect the settings for
 that waveform. When you download a waveform from a file, the property values automatically
 populate with the values that are in the file. Changes that you make to the waveform
 properties only apply to the selected waveform.

###### Debug Test Programs

The NI-RFSG 20.7 driver introduces waveform properties. Prior to the 20.7 release, not all
 waveform properties were available. These properties also apply globally to all waveforms.
 When you debug a test program that uses global properties, the global values appear for the
 selected waveform. However, changes that you make to the waveform properties in
 InstrumentStudio only apply to the selected waveform.

| Global Property Name | RFSG Arbitrary Waveform Property Name |
| --- | --- |
| IQ Rate | IQ Rate |
| Peak Power Adjustment | PAPR |
| Pre-filter Gain | Run time Scaling |
| Signal Bandwidth | Signal Bandwidth |

##### Waveform Properties in Script Mode

Settings and values associated with waveforms generated in Script mode.

Script

- The properties under the Script section correspond to the global
 properties that are used for the selected script.
- The properties under the Waveforms section correspond to the
 waveform properties and show the values for the selected waveform.

Waveform properties take precedence over the global properties.

#### Perform RF Signal Generator
 Self-Calibration

Self-calibrate an RF signal generator device to ensure accurate measurements.

The accuracy of a device will naturally drift over time.
 Self-calibration ensures more accurate measurements by compensating for board-level
 temperature variations and device degradation. Self-calibration also ensures that the device
 operates within the ranges that appear in your test specifications.

##### Perform
 Self-Calibration

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»Self Calibrate... to begin self-calibration. Note InstrumentStudio warns you that the
 process might take several minutes to finish. InstrumentStudio also locks the
 instrument until the process completes.
3. Click Continue to proceed.

##### Perform Self-Calibration Range

Note

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»Self Calibrate Range... .
3. In the Steps to omit dialog box, select the steps that you want
 InstrumentStudio to skip during the self-calibration process.
4. In the Ranges field, enter the values for the desired ranges of
 self-calibration.
5. Click Continue to proceed, or Cancel to
 cancel self-calibration.

##### Check Calibration History

1. In the device panel, open the instrument settings menu ( ).
2. Click Device Slot»Calibration»History .

#### RF Signal Generator Status

You can see the current generation status of the RF signal generator with the
 generation status icon. The generation status icon is at the top of the panel.

| Icon | Status | Description |
| --- | --- | --- |
|  | Generating output | Signal generation is running on this channel and the output appears in the device panel. This status might also mean that the channel is waiting for a trigger. |
|  | Not generating output | Signal generation is stopped on this channel. |
|  | Unknown status | The signal generation status is unknown. Run the panel to refresh the output status. |

Note

- Signal generation is running
- Output is set to ON

#### De-Embedding RFSG Devices

*De-embedding* is the process of removing the effects of test fixture cabling and
 components. Applying de-embedding to an RF signal ensures more accurate results when reading
 data from your RF device. Once applied, the de-embedded signal you see at the device port
 matches the requested signal settings.

1. Click the icon to open the Instrument Settings window.
2. On the RF tab, scroll down to the
 De-embedding section.

Type

None

Scalar

Vector

Status

.s2p

Filename

.s2p

Note

- S2P tables are used to incorporate S-parameters into signal de-embedding. S-parameters
 characterize the effects of a linear network on a signal when it passes from one port to
 another. Refer to the installed RF driver documentation for more information.
- You must configure de-embedding for each port when you use multi-port modules.

<!--NI_TOPIC bundle=instrumentstudio path=scpi-panels.html language=enus -->
## TOPIC 00059: SCPI Instrument Panels

- bundle_id: `instrumentstudio`
- source_path: `scpi-panels.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/scpi-panels.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license. Use SCPI instrument panels to fetch data, take screenshots, and manage SCPI configuration. A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional lice

### SCPI Instrument Panels

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Use SCPI instrument panels to fetch data, take screenshots, and manage SCPI
 configuration.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

You can create instrument panels that use SCPI-capable devices the same way you
 create instrument panels for native NI hardware. SCPI instrument panels do
 not include all of the capabilities present in native NI instruments. NI
 recommends that you use these panels as companions to third-party
 hardware.

#### Connecting to
 SCPI-Capable Devices using NI-VISA

InstrumentStudio can
 only detect your SCPI-capable device if you connect the device to
 your system with Hardware Configuration Utility (HWCU) or
 Measurement & Automation Explorer (MAX). For information on
 connecting VISA devices, see *Hardware Configuration Utility
 User Manual* or *Measurement & Automation
 Explorer Help*.

#### Adding SCPI
 Instrument Panels to a Project

You can add SCPI instrument
 panels to a project by selecting Manual
 Layout from the Home
 screen. Search for the devices that you want to include in the
 layout in the left panel of the Edit layout
 window under Instruments»VISA Instruments.

#### Additional Setup for
 SCPI Instrument Panels

You might see a device named
 Unknown Instrument when you select a
 SCPI-capable device from the Manual Layout
 window. This naming indicates that while InstrumentStudio discovered
 the device, the device and the instrument panel require additional
 setup. The following section describes how to perform this
 additional setup.

Parent topic:

Configure Panels and Layouts

Related information:

- Measurement & Automation Explorer (MAX) Help
- Hardware Configuration Utility (HWCU) User Manual

#### Configure a SCPI-Capable Device

InstrumentStudio supports SCPI-capable devices, but most devices require
 additional configuration.

1. Add your instrument to your system using HWCU or MAX.
2. From the InstrumentStudio Home screen,
 go to Manual layout.
3. Find your SCPI instrument and add it to a panel.
4. When you create an SCPI instrument panel that requires
 additional setup, InstrumentStudio prompts you to set up the
 panel. Click the appropriate button to proceed. 
 A file explorer window opens at the location of the new
 .json configuration file that
 is associated with the selected SCPI-capable
 device.
5. Open the new .json file by navigating to
 %PROGRAMDATA%\National
 Instruments\Services\Scpi\ScriptDefinitions.

Note

.json

[IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']

Open SCPI Support File
 Location

1. Read through the comments included in the
 .json file. 
 The comments describe what each section of the template does.
 The comments also explain how to modify the sections for
 your instrument. 
 For example, take the following section of the
 .json
 file:// List of all channels available on the instrument.
 "Channels": [
 {
 "DisplayName": "Channel 1",
 "ScpiName": "CHAN1"
 },
 {
 "DisplayName": "Channel 2",
 "ScpiName": "CHAN2"
 },
 {
 "DisplayName": "Channel 3",
 "ScpiName": "CHAN4"
 },
 {
 "DisplayName": "Channel 4",
 "ScpiName": "CHAN4"
 },
 ],You must ensure that the
 Channels section matches the number
 of available channels on your device. If you set up a
 two-channel instrument, you must remove the lines that
 pertain to channels 3 and 4.
2. Save and close the file. 
 Notice Do
 not change the name of the
 .json file or move the file
 from the folder that it was created in.
3. Open the instrument settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']) and select Refresh
 panel.

Using SCPI
 Instruments

Related tasks:

- Using SCPI Instruments

##### Additional Information About SCPI
 Instruments

The following sections provide additional details about SCPI instrument support in
 InstrumentStudio.

###### Supported
 SCPI Instrument Types

- Oscilloscopes
- SMUs
- DMMs

###### SCPI-Capable Device
 Vendors

- Agilent
- Keysight
- Tektronix
- Fluke
- Keithley

Note

###### SCPI-Capable Devices from Other Vendors

.json

.json

Note

###### Examples
 and Templates

A collection of configuration file examples and templates is
 installed with InstrumentStudio. Go to %PROGRAMFILES%\National
 Instruments\Shared\Services\Scpi\ScriptDefinitions\Examples to view
 these examples and templates. The examples provide additional details about
 different script types and associated device commands.

Note

<!--NI_TOPIC bundle=instrumentstudio path=scpi-use.html language=enus -->
## TOPIC 00060: Using SCPI Instruments

- bundle_id: `instrumentstudio`
- source_path: `scpi-use.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/scpi-use.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: The following sections contain instructions for performing common tasks using SCPI instruments. Fetch Data from a SCPI Instrument InstrumentStudio fetches data from the last time a SCPI instrument performed a measurement. Fetching SCPI instrument data does not trigger acquisition. Select the data th

### Using SCPI Instruments

The following sections contain instructions for performing common tasks using SCPI
 instruments.

#### Fetch Data from a SCPI Instrument

InstrumentStudio fetches data from the last time a SCPI instrument performed a
 measurement. Fetching SCPI instrument data does not trigger acquisition.

1. Select the data that you want to capture using the checkboxes in the instrument
 panel. 
 **Channels**—Select specific channels to fetch data from. This option sends a
 SetChannel SCPI command to the device.Important You must select
 at least one channel to fetch data.
 **Include screen image**—Captures an image of your SCPI instrument screen. The captured image
 is either in a .png or a
 .bmp format, depending on the device.
2. Click Fetch Data to fetch the data from the selected
 sources. 
 Note You can also fetch this
 data using Capture Data and Capture
 Screenshot.

To fetch new data, trigger data collection
 on your SCPI instrument and repeat this process.

#### SCPI Instrument Configuration
 Management

The following sections describe how to manage configuration settings within your
 project.

When you make changes to your device, such as turning a setting knob or pressing a
 button, the configuration settings for the device change. The device stores these
 changes. If you have a preferred configuration to perform a specific task, you can
 fetch and store these settings in your SCPI instrument panel.

##### Fetch Existing Configuration
 Settings

To fetch configuration settings from a device, open the
 instrument configuration utility by clicking the [IMAGE alt='An icon of a wrench that opens the instrument configuration utility in InstrumentStudio.' src='GUID-683795A8-D3BE-4EED-B912-269584403F7D-a5.png'] icon. Click the Fetch Configuration tab, then click
 Fetch to fetch the device configuration settings. The
 settings appear in the configuration utility window. To store the fetched
 configuration data in the selected panel, save your InstrumentStudio
 project.

##### Applying
 Configuration Setting

To apply device settings that are stored in a SCPI
 panel, open the instrument configuration utility ([IMAGE alt='An icon of a wrench that opens the instrument configuration utility in InstrumentStudio.' src='GUID-683795A8-D3BE-4EED-B912-269584403F7D-a5.png']). Then click the Fetch Configuration tab and click
 Apply.

#### Send Commands to a SCPI Device

Complete the following steps to send SCPI commands to your SCPI-capable devices using a
 SCPI instrument panel.

1. Click the [IMAGE alt='An icon of a wrench that opens the instrument configuration utility in InstrumentStudio.' src='GUID-683795A8-D3BE-4EED-B912-269584403F7D-a5.png'] icon to open the instrument configuration utility.
2. Click the Send Command tab.
3. Click Send Command to open the command editor.
4. Enter the SCPI command that you want to send to your SCPI-capable device in the
 textbox. 
 Note Refer to the user manual of
 your device for more information on supported SCPI commands.
5. Click Send to send the SCPI command to your
 device.

<!--NI_TOPIC bundle=instrumentstudio path=select-default-pin-map.html language=enus -->
## TOPIC 00061: Select a Default Pin Map

- bundle_id: `instrumentstudio`
- source_path: `select-default-pin-map.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/select-default-pin-map.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can select a default pin map to add that pin map to all new projects that you create in InstrumentStudio. Go to FilePreferencesPin and site mapping. Click the Browse button to open the Default pin map file dialog. Select a pin map file. InstrumentStudio adds the default pin map to the project fi

### Select a Default Pin Map

You can select a default pin map to add that pin map to all new projects that you
 create in InstrumentStudio.

1. Go to File»Preferences»Pin and site mapping.
2. Click the Browse button to open the Default pin map
 file dialog.
3. Select a pin map file.

InstrumentStudio adds the default pin map to the project files
 when you create a new project. InstrumentStudio also automatically uses the default pin map as
 the active project pin map.

Parent topic:

Pin Maps

<!--NI_TOPIC bundle=instrumentstudio path=seq-support-inst.html language=enus -->
## TOPIC 00062: Supported Panel Types

- bundle_id: `instrumentstudio`
- source_path: `seq-support-inst.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/seq-support-inst.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: The sequencer tool supports specific panel types only. The sequencer tool supports the following panel types and the following operations for each panel type: Panel Type Start Read Stop Digital Multimeter ✓ ✓ ✓ Measurement Plug-Ins ✓ Network Analyzer ✓ ✓ Oscilloscope ✓ ✓ RF Signal Analyzer ✓ ✓ RF Si

### Supported Panel Types

The sequencer tool supports specific panel types only.

| Panel Type | Start | Read | Stop |
| --- | --- | --- | --- |
| Digital Multimeter | ✓ | ✓ | ✓ |
| Measurement Plug-Ins |  | ✓ |  |
| Network Analyzer | ✓ | ✓ |  |
| Oscilloscope | ✓ | ✓ |  |
| RF Signal Analyzer | ✓ | ✓ |  |
| RF Signal Generator | ✓ |  | ✓ |
| SCPI Instrument |  | ✓ |  |
| SMU/Power Supply | ✓ | ✓ | ✓ |
| Waveform Generator | ✓ |  | ✓ |

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=seq.html language=enus -->
## TOPIC 00063: Sequencer Tool

- bundle_id: `instrumentstudio`
- source_path: `seq.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/seq.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sequencer tool allows you to perform a series of ordered tasks using instrument panels and measurement plug-ins. Automation with the sequencer tool allows you to efficiently perform multi-step measurements, saving time and ensuring consistency. A teal ribbon that signals that a feature is only a

### Sequencer Tool

The sequencer tool allows you to perform a series of ordered tasks using instrument
 panels and measurement plug-ins. Automation with the sequencer tool allows you to
 efficiently perform multi-step measurements, saving time and ensuring
 consistency.

Note

[IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png']

The following sections provide specific information on how to use the sequencer
 tool in InstrumentStudio:

- [Configure Steps](configure-steps.html) Each sequence step is associated with an InstrumentStudio panel. The panel contains the step configuration. InstrumentStudio immediately applies any changes to the step.
- [Supported Panel Types](seq-support-inst.html) The sequencer tool supports specific panel types only.
- [Accessing the Sequencer Tool](sqt_access.html) The sequencer tool requires an InstrumentStudio Professional license.
- [Build a Sequence](build-sequence.html) You can add panels and steps to a sequence in a project that you already saved.
- [Sweeps](sweeps.html) Sweeps allow you to repeat selected steps in a sequence. Sweeps also allow you to increment the values of parameters across the individual measurement steps within the sweep.
- [Modify a Sequence](mod-seq.html) You can modify existing sequences and panels that are part of a sequence.
- [Execute a Sequence](exec-seq.html) Executing a sequence performs all the steps that are defined in the sequence. When the sequence ends, you can view the data that InstrumentStudio measured during the sequence. You can also view the sequence report to ensure that the sequence executed all defined steps successfully.
- [View a Sequence Report](view-seq-report.html) A sequence report is a .pdf file that details the results of a sequence. InstrumentStudio generates a sequence report every time you execute a sequence.
- [View a Sequence Execution Log](view-sq-log.html) When you execute a sequence, InstrumentStudio creates an execution log in the sequencer pane. You can use the execution log to check the status and the execution time of each step.

<!--NI_TOPIC bundle=instrumentstudio path=set-active-project-pin-map.html language=enus -->
## TOPIC 00064: Set an Active Project Pin Map

- bundle_id: `instrumentstudio`
- source_path: `set-active-project-pin-map.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/set-active-project-pin-map.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: Set an active pin map to filter your view of connected sites, pins, and devices within your test system in InstrumentStudio. Open your InstrumentStudio project. Choose one of the following options to add a pin map to your project: Create a new pin map Use the Pin Map Editor to create a new pin map f

### Set an Active Project Pin Map

Set an active pin map to filter your view of connected sites, pins, and devices within
 your test system in InstrumentStudio.

1. Open your InstrumentStudio project.
2. Choose one of the following options to add a pin map to your project: 
 OptionDescriptionCreate a new pin map
 Use the Pin Map Editor to create a new pin map for your
 project.Set a default pin map
 Automatically add a selected pin map to new InstrumentStudio projects and set
 it as the active pin map.Add a pin map file to your project files
 Select File»New»Pin Map to add a pin map file (.pinmap) to your
 project. 
 Note InstrumentStudio automatically sets
 the first pin map file that you add as the active project pin map. The name of the
 active project pin map appears in bold in the project files pane.Note Only one pin map can be active within a
 project.
3. Confirm that the pin map is valid. An error icon appears next to the pin map file in
 the project files pane if InstrumentStudio detects a problem. For more information, see
 *Pin Map Errors and Warnings*.
4. Activate the pin map. Right-click the pin map file in the project files pane
 and select Make active.
5. Apply site filtering to view site pins in your panels. For more information on site
 filtering, see *Using the Site Filter*.
6. Apply pin filtering to view selected pins within a site in your panels. For more
 information on pin filtering, see *Apply a Pin Filter*.

To deactivate the pin map, right-click the active pin map in the project files pane. Then
 select Make inactive.

Note

Parent topic:

Pin Maps

Related tasks:

- Create a New Pin Map
- Select a Default Pin Map
- Add Pin Map Files to a Project
- Using the Site Filter
- Apply a Pin Filter

Related reference:

- Pin Map Errors and Warnings

<!--NI_TOPIC bundle=instrumentstudio path=smu-vps.html language=enus -->
## TOPIC 00065: SMU and VPS Devices

- bundle_id: `instrumentstudio`
- source_path: `smu-vps.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/smu-vps.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the SMU/Power Supply panel to select a mode of operation and configure various settings for your SMU and VPS devices. Modes of Operation When you use an SMU or a VPS device, you can use different device operating modes to acquire measurements. Device Operating Modes The following table describes

### SMU and VPS Devices

Use the SMU/Power Supply panel to select a mode of operation and configure various
 settings for your SMU and VPS devices.

Parent topic:

Configure Device Settings

#### Modes of Operation

When you use an SMU or a VPS device, you can use different device operating modes to
 acquire measurements.

##### Device Operating Modes

The following table describes the behaviors and uses of these device operating
 modes:

| Operating Mode | Sourcing Behavior | Large Panel Plotting Behavior | Pause Behavior | Potential Uses | Notes |
| --- | --- | --- | --- | --- | --- |
| Charting () | Allows one or more channels to source a supported signal. | Appends samples to the chart as the samples are measured. | Channels continue to source at the last configured level when you pause measurements. | Observe signals over an infinite duration. | – |
| Waveform () | Allows one or more channels to source a supported signal. | Plots samples to the graph all at once. Capture time determines the length of the graph. | Channels continue to source at the last configured level when you pause measurements. | Observe signals over a shorter, finite duration, similar to an oscilloscope. | InstrumentStudio automatically configures the device for a faster sample rate. InstrumentStudio also runs the output continuously in a loop. To change this behavior, click SINGLE. |
| Single-Channel Sweep()Two-Chanel Sweep () | Sweeps through configured steps for a single channel (Single-Channel Sweep) or two channels (Two-Channel Sweep). | Plots all sample step results on the graph as the step results are measured. | Both measurement and output channels stop running when you pause measurements. | Allows you to plot the relationship between current and voltage in an I-V curve. | When you use Two-Channel Sweep, the sweep acts as a nested loop. In this nested loop, the inner channel executes all the steps for each step that is configured in the outer channel. |
| Sweep (LCR mode) | Sweeps through configured frequency or DC bias steps for a single channel (Single-Channel Sweep). | Plots all sample step results on the graph as the step results are measured. | Both measurement and output channels stop running when you pause measurements. | Allows you to plot the relationship between frequency or DC bias and enables LCR readbacks. | – |

Note

Waveform

Sweep

- PXI-4110
- PXIe-4112
- PXIe-4113
- PXI-4130
- PXI-4132

Note

Waveform

Waveform

Note

Sweep

PXIe-4190

1. Click the icon in the device panel to open the Channel Settings 
 window.
2. Click the Mode dropdown menu.
3. Select the LCR meter option.

##### Channel Operating Modes

In addition to device operating modes, you can also specify an operating mode for each
 channel.

To change the operating mode of a channel, use the dropdown menu in the
 Channels section of the panel. A channel operating mode only
 appears in the dropdown menu if your current device supports that operating mode.

When
 you change the operating mode of a channel, InstrumentStudio pauses all panel measurements.
 All enabled outputs continue to generate signal at the last configured level. The updated
 operating mode of the channel does not take effect until the panel starts running
 again.

Idle

Idle

Voltage

Current

Power

Resistance

Note

sourcing

sinking

output

input

Pulse voltage

Pulse current

Note

Voltage sequence

Current
 sequence

.csv

Configure Sequences

Note

- If you import the step sequence from a
 .csv file, the .csv file must have
 the following two columns:
  - The first column must be for the level
  - The second column must be for the duration
- Voltage sequence and current sequence modes are not
 available on the following devices:
  - PXI-4110
  - PXIe-4112
  - PXIe-4113
  - PXI-4130
  - PXI-4132

#### Automatic Level Range

Automatic level range automatically determines the signal range when the range for a
 signal is unknown.

When a measured signal exceeds the manually specified range in InstrumentStudio, InstrumentStudio
 cannot accurately measure that signal.
 InstrumentStudio warns you that the measurement is
 overrange.

To avoid overranging, set the Voltage level
 range or the Current level range option to
 Auto. This setting allows InstrumentStudio to use incoming signal
 data to automatically set level ranges, which increases the accuracy of
 measurements.

##### Enable Automatic Level Range

1. Click [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] to open the Channel Settings
 window.
2. Select Auto in the dropdown menu of the
 Voltage/Current level range
 option.

Manual

Voltage/Current level range

Note

Voltage

Voltage level range

Current

Current level range

##### Configure Automatic Level Range

[IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png']

Channel Settings

Aperture time mode

Aperture time
 mode

Auto

Manual

Aperture time unit

Aperture time

Seconds

PLC

Aperture time mode

Manual

Aperture time

Aperture
 time mode

Manual

Note

Autorange behavior

Range up to limit then down

Range up

Range up and down

Minimum current range

Note

#### Configure Channel Sessions

You can change the session type to Multichannel or Single
 channel (compatibility). The default setting is Multichannel.
 InstrumentStudio version 202Q1 and newer have different default behavior.

##### NI-DCPower Independent Channel Sessions

InstrumentStudio versions 2020 Q1 and
 newer export a singular session configuration for all channels by default. However, using
 NI-DCPower independent channel sessions allows you to configure multiple channels within the
 same session independently. The channels within the session can belong to the same
 instrument or to multiple instruments.

##### Considerations When Configuring Sessions
 with SMU Devices

By default, InstrumentStudio creates a singular multichannel
 session for all devices in a single SMU device. To change session types, open the instrument
 settings menu ([IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']) of the device in your panel. Then, hover your cursor over Session
 Type and select the session type. You can set the session type to
 Multichannel or Single channel (compatibility). The
 default setting is Multichannel.

Session type

Single
 channel (compatibility)

- Exporting a session to a platform that does not support NI-DCPower independent channel
 sessions. These platforms include, for example, the following:
  - Python
  - LabWindows/CVI
  - LabVIEW NXG
  - Linux desktop
- Exporting a session to NI-DCPower version 20.5 and earlier.
- Exporting the session to end-user code that uses deprecated NI-DCPower
 Initialize functions in C/LabVIEW.
- Exporting the session to end-user code that uses deprecated constructors in .NET.

Note

[IMAGE alt='A cogwheel icon for the instrument settings menu of InstrumentStudio.' src='GUID-BD4AE800-BD2E-491C-9DCE-87008B8F7D57-a5.png']

Session type

#### SMU/VPS Output Status

You can see the current output status of non-idle channels with the output status icon.
 The output status icon is at the top of the Channels section of an
 SMU/Power Supply panel.

| Icon | Status | Description |
| --- | --- | --- |
|  | Generating output | One or more channels in the panel are sourcing voltage or current. |
|  | Not generating output | No channels in the panel are sourcing voltage or current. |
|  | Waiting for trigger | Channels in the panel are waiting to start an operation until the trigger condition occurs. |
|  | Unknown status | The output status of the channel in the panel is unknown. Run the panel to refresh the output status. |

Note

#### Configure SourceAdapt Parameters to Measure
 Transients

You can use SourceAdapt technology to customize the Source Measure Unit (SMU) response
 to any load.

NI SourceAdapt Next-Generation SMU Technology

Related Information

Note

1. Place a SourceAdapt-compatible SMU in the large panel.
2. Set the device operating mode of the SMU panel to Waveform ([IMAGE alt='An icon with a waveform that represents the waveform operating mode.' src='GUID-A65C5D42-3730-4A4A-9677-A08037CC1FCE-a5.png']).
3. Click [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] to open the Channel Settings window.
4. Scroll down to the SourceAdapt tuning parameters section of the
 Channel Settings window.
5. Select one of the following SourceAdapt presets:
  - Slow —Slows the control loop for a more stable response.
  - Normal —The default SourceAdapt preset, a balance between speed
 and stability.
  - Fast —Speeds up the control loop for a faster response.
6. Optional: 
 Make custom adjustments to the response by configuring the fields in the
 SourceAdapt tuning parameters section.

Related information:

- NI SourceAdapt Next-Generation SMU Technology

#### Configure Sequences

Power sequencing on an SMU/Power Supply allows you to output the desired power-up
 sequence for a DUT with multiple power sources.

Voltage Sequence

Current Sequence

- Power-up order
- Power-up timing
- Voltage or current level

Note

- Within the same panel, channels that operate in Voltage Sequence ,
 Current Sequence , Pulse Voltage , or Pulse
 Current mode are automatically hardware-synchronized. For more information on
 hardware and software synchronization within panels, see Synchronize
 Devices .
- Sequence channel operating modes are only available on power supplies that support
 advanced sequencing. For more information on advanced sequencing and supported devices,
 see Advanced Sequencing in the Related Information 
 section.

1. Place an SMU or a power supply in a panel. 
 If you place the device in a large panel, the graph shows a preview of the output
 sequence that the channel will generate.
2. Set the device operating mode to Waveform ([IMAGE alt='An icon with a waveform that represents the waveform operating mode.' src='GUID-A65C5D42-3730-4A4A-9677-A08037CC1FCE-a5.png']) or Charting ([IMAGE alt='An icon with a square waveform that represents the charting operating mode.' src='GUID-6F19F792-9B2A-445E-BEFA-C15C4BB98F52-a5.png']). 
 Setting the device operating mode to Waveform ([IMAGE alt='An icon with a waveform that represents the waveform operating mode.' src='GUID-A65C5D42-3730-4A4A-9677-A08037CC1FCE-a5.png']) allows for fast sampling. Waveform mode also allows you to
 visualize the sequence in more detail.
3. Set the channel operating mode to Voltage sequence or
 Current sequence. 
 A step table appears within the channel and the Channel
 Settings dialog box.
4. Edit the steps in the step table. 
 You can edit the steps in the following ways:Enter values manually
 Import data from a file
 Paste data from the clipboard
5. Optional: 
 Tune the output of the sequence with SourceAdapt parameters in the Channel
 Settings window.
6. Enable the channel output and run the panel to begin the sequence.

Related concepts:

- Synchronize Devices

Related reference:

- Export Configurations

Related information:

- Advanced Sequencing

<!--NI_TOPIC bundle=instrumentstudio path=sqt_access.html language=enus -->
## TOPIC 00066: Accessing the Sequencer Tool

- bundle_id: `instrumentstudio`
- source_path: `sqt_access.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/sqt_access.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: The sequencer tool requires an InstrumentStudio Professional license. Click the Sequencer pane at the top of the project window.

### Accessing the Sequencer Tool

The sequencer tool requires an InstrumentStudio Professional license.

Sequencer

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=supported-devices.html language=enus -->
## TOPIC 00067: Supported Hardware

- bundle_id: `instrumentstudio`
- source_path: `supported-devices.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/supported-devices.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following tables list hardware that can be used with InstrumentStudio, and the first available version of InstrumentStudio to support the hardware.

### Supported Hardware

The following tables list hardware that can be used with InstrumentStudio, and the
 first available version of InstrumentStudio to support the hardware.

- [NI-DCPower](ni-dcpower-supported-hw.html) You can use the following NI-DCPower hardware with an SMU or VPS instrument in InstrumentStudio:
- [NI-DMM](ni-dmm-supported-hw.html) You can use the following NI-DMM hardware with a Digital Multimeter instrument in InstrumentStudio:
- [NI-FGEN](ni-fgen-supported-hw.html) You can use the following NI-FGEN hardware with a Waveform Generator instrument in InstrumentStudio:
- [NI-SCOPE](ni-scope-supported-hw.html) You can use the following NI-SCOPE hardware with an Oscilloscope instrument in InstrumentStudio:
- [NI-RFSG](ni-rfsg-supported-hw.html) You can use the following NI-RFSG hardware with a RF Signal Generator instrument in InstrumentStudio:
- [NI-RFSA](rfmx-supported-hw.html) You can use the following NI-RFSA hardware with a RF Signal Analyzer instrument in InstrumentStudio:
- [NI-DAQmx](ni-daqmx-supported-hw.html) You can use the following NI-DAQmx hardware with a DAQ Analog Input (AI) or Analog Output (AO) instrument in InstrumentStudio.

<!--NI_TOPIC bundle=instrumentstudio path=sweeps.html language=enus -->
## TOPIC 00068: Sweeps

- bundle_id: `instrumentstudio`
- source_path: `sweeps.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/sweeps.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sweeps allow you to repeat selected steps in a sequence. Sweeps also allow you to increment the values of parameters across the individual measurement steps within the sweep. Add a Sweep Loop to a SequenceTo add a sweep loop to a sequence, click the add step button (+) for the steps that you want to

### Sweeps

Sweeps allow you to repeat selected steps in a sequence. Sweeps also allow you to
 increment the values of parameters across the individual measurement steps within the
 sweep.

#### Add a
 Sweep Loop to a Sequence

To add a sweep loop to a sequence, click the add
 step button (+) for the steps that you want to sweep. Then,
 select the Sweep loop option.

#### Sweep
 Behavior

When you run a sequence that contains a sweep, the sequence runs
 the steps within the sweep loop. You can configure the parameter settings that the
 sequence uses when you configure the sweep. In general, the sweep executes once for
 each new parameter value specified in the sweep settings.

For example, you
 want to run a test sequence. This test sequence sends a series of three different
 voltages to a device using an SMU panel. Then, the sequence reads data back from the
 device using a DMM panel. In this case, the sequence executes in the following
 order:

- Sweep 1, Step 1, Parameter Value 1: SMU[Start] sends 1.15 V to device.
- Sweep 1, Step 2: DMM reads output from device.
- Sweep 1, Step 3: SMU[Stop]
- Sweep 2, Step 1, Parameter Value 2: SMU sends 1.35
 V to device.
- Sweep 2, Step 2: DMM reads output from device.
- Sweep 2, Step 3: SMU[Stop]
- Sweep 3, Step 1, Parameter Value 3: SMU sends 1.5
 V to device.
- Sweep 3, Step 2: DMM reads output from device.
- Sweep 3, Step 3: SMU[Stop]

Once a sweep loop is completed, the next steps of the sequence
 execute.

#### Sweep
 Strategies

You can configure sweep loop behavior by opening the step
 settings panel ([IMAGE alt='A cogwheel icon for the step settings panel of the sequencer tool.' src='GUID-934AE2CB-A722-468F-98E6-429D375F232F-a5.png']). The following sweep strategies are available in the
 sequencer tool:

Start, Stop, Step

Start, Stop, Count

Array

#### Sweep Step
 Settings

Note

Sweep Name

Data Type

Strategy

Sweep Strategies

Distribution

Start

Stop

Start

Stop

Step

Start, Stop,
 Step

Count

Start, Stop,
 Count

Values

Array

#### Configuring Sweep Parameters for
 Sequence Steps

After you configure the sweep step settings, you can also
 configure how each step within the sweep handles the sweep parameter. You can
 configure sweep parameters in the step settings for each step within a sweep. Step
 settings allow you to use the sweep parameter for any appropriate step input. You
 can select the same sweep parameter on multiple step inputs.

When you
 correctly configure a step to a sweep, InstrumentStudio highlights the panel item
 that is associated with the sweep with a purple box.

#### Supported Panel
 Types

- Measurement plug-in steps
- All supported instrument panels, including SCPI instrument panels

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=uninstall-instrument-studio.html language=enus -->
## TOPIC 00069: Uninstall InstrumentStudio

- bundle_id: `instrumentstudio`
- source_path: `uninstall-instrument-studio.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/uninstall-instrument-studio.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can uninstall InstrumentStudio using Package Manager or through the Programs and Features functionality of Windows. When you uninstall InstrumentStudio, no additional software gets removed. Some files and data also remain on the system. For more information, see Leftover Elements After Uninstall

### Uninstall InstrumentStudio

You can uninstall InstrumentStudio using Package Manager or
 through the Programs and Features functionality of Windows.

Note

When you uninstall InstrumentStudio, no additional software gets removed. Some files
 and data also remain on the system. For more information, see *Leftover
 Elements After Uninstallation*.

#### Uninstall InstrumentStudio Using Package
 Manager

To uninstall InstrumentStudio and its
 components using Package Manager, complete the following steps:

1. Open Package Manager.
2. In the INSTALLED tab, select InstrumentStudio.
3. Click REMOVE .
4. In the Select tab of the NI Package
 Manager dialog box, click Allow Removal .
5. In the Review tab, click Next . Note The Review tab lists all
 InstrumentStudio components that the uninstaller removes.

The uninstaller removes InstrumentStudio and the InstrumentStudio components
 listed in the Review tab from your system.

#### Uninstall InstrumentStudio Manually

To uninstall
 InstrumentStudio and its components manually, complete
 the following steps:

1. Navigate to Programs and Features in Windows.
2. Locate NI Software .
3. Click Uninstall .
4. Select InstrumentStudio from the list of NI software.
5. Follow the instructions of the uninstallation wizard.

The uninstaller removes InstrumentStudio and its components from your
 system.

Parent topic:

Install InstrumentStudio

Related reference:

- Leftover Elements After Uninstallation

<!--NI_TOPIC bundle=instrumentstudio path=unsupported-versions.html language=enus -->
## TOPIC 00070: Updates and Changes for InstrumentStudio Unsupported Versions

- bundle_id: `instrumentstudio`
- source_path: `unsupported-versions.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/unsupported-versions.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Browse updates and changes made in InstrumentStudio versions that are no longer supported. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about no

### Updates and Changes for InstrumentStudio Unsupported Versions

Browse updates and changes made in InstrumentStudio versions
 that are no longer supported.

Note

Release
 Notes

ni.com

Related information:

- Release Notes

#### 2024 Q4

October 2024

- Added segmented sweeps to the Network Analyzer instrument.
- Improved pulsed S-parameters, data visualizations, and calibration for Network
 Analyzer instruments.
- Added channel merging capability to the SMU/Power Supply instrument. This
 capability allows you to combine multiple channels to achieve a higher output
 current.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Added support for SCPI-capable oscilloscopes. Refer to SCPI Instrument Panels for more information on using
 SCPI-capable devices with InstrumentStudio.
  - Fetch data and screenshot captures from SCPI instruments.
  - Fetch configurations from SCPI instruments.
  - Apply configurations to SCPI instruments.
- Sequencer Tool
  - Added support for digital multimeters in the Sequencer Tool. You can now
 create steps to read measurements from supported digital multimeters.
  - Added support for wait steps. You can now create wait steps in your
 sequences.
  - UI improvements to the sequencer tool. You can now view steps associated
 with measurement panels.
- Measurement Plug-Ins
  - Added support for measurement plug-in versioning. Refer to the
 Measurement Plug-In User Manual for more information
 measurement plug-in versioning.
  - Added support for displaying a link to measurement plug-in documentation
 in InstrumentStudio and TestStand

Related concepts:

- SCPI Instrument Panels

Related information:

- Measurement Plug-Ins User Manual

#### 2024 Q3

July 2024

- Pin maps are no longer required to use measurement plug-ins.
- Added several enhancements to the Network Analyzer instrument. For example, the
 ability to save S-parameter measurement results to Touchstone format
 ( .snp ) files.
- Added band power markers to the Spectrum measurement in the RF Signal Analyzer
 instrument.

##### [IMAGE alt='A teal ribbon that signals that a feature is only available with an InstrumentStudio Professional license.' src='GUID-F31DAF32-6D17-4C2D-ABC7-4E10C2F32C75-a5.png'] Professional License Only

The following new features are only
 available with an InstrumentStudio Professional license.

- Added support for measurement plug-ins. Refer to the Measurement
 Plug-Ins user manual for more information on developing
 measurements.
- Added the Sequencer Tool for sequencing measurements
 using measurement plug-ins.
- Added support for connecting to plug-in libraries.

Related concepts:

- Sequencer Tool

Related tasks:

- Connect to a Plug-In Library

Related information:

- Measurement Plug-Ins User Manual

#### 2024 Q2

April 2024

- Added manual calibration, pulse mode, triggering, and improved calset support to
 the Network Analyzer instrument.
- Reference waveform and de-embedding file paths are now stored with the RF Signal
 Analyzer configuration, allowing for automatic reload.
- Added several enhancements for Channel Sounding packets using the RF Signal
 Analyzer Bluetooth personality.

#### 2024 Q1

January 2024

- Added support for Fixed Markers using RF Signal Analyzer instruments.
- Added custom bitfile support for RF Signal Analyzer and RF Signal Generator
 instruments.

#### 2023 Q4

October 2023

- You can now undo and redo changes made to panel properties.
- Improved searching and filtering of instruments and measurements in the
 Edit Layout window.
- Use the Network Analyzer instrument to control supported vector network
 analyzers.
- Added support for capturing IQ data using the RF Signal Analyzer instrument.
- Added support for Channel Sounding packets using the RF Signal Analyzer
 Bluetooth personality.
- Added several enhancements to the RF Signal Analyzer Pulse personality. For
 example, support for multi-burst analysis and phase and frequency traces.

#### 2023 Q3

July 2023

- Added full support for the following personalities for the remote RF Signal
 Analyzer panel: These personalities are no longer preview features.
  - SpecAn
  - LTE
  - NR
  - WLAN
  - Bluetooth
- Added new remote connections section in the preferences menu.
- Added support for pulse measurements in the RF Signal Analyzer panel.

Related information:

- Configure Remote RF Signal Analyzer Panels
- Manage Remote Connection Preferences

#### 2023 Q2

April 2023

- Added LTE, NR, and WLAN personalities to remote RF Signal Analyzer panel preview
 feature. Note Preview features
 have limited functionality and are not fully supported.

#### 2023 Q1

January 2023

- Added SMU measurement auto-range support for PXIe-4190 and PXIe-4190 (500
 kHz).
- Added LCR Meter impedance measurement auto-range support in sweep mode.
- Added remote RF Signal Analyzer panel viewing as a preview feature. Note Preview features
 have limited functionality and are not fully supported.

#### 2022 Q4

October 2022

- Added oscilloscope Manual Override mode. This mode enables the
 simultaneous manual configuration of record length and sample size in
 oscilloscope settings.

#### 2022 Q3

July 2022

- SMU measurement auto-range support for DC Power devices that support it.
- Single-channel sweep mode support for PXIe-4190 when used in LCR mode.
- LCR Meter mode usability improvements for PXIe-4190.
- RF Signal Analyzer instrument with support for RFmx personalities.

#### 2022 Q2

April 2022

- Single-channel sweep mode measurement added as a preview feature for
 PXIe-4190 when used in LCR mode.

#### 2022 Q1

January 2022

- LCR panel debug monitor functionality and usability improvements for the LCR PXIe-4190
 module.
- Custom gating support for Scope measurements.

#### 2021 Q4

October 2021

- Added new LCR panel supporting interactive use with the PXIe-4190 module.
- Added access and visibility to pin maps.
- Improved UI responsiveness and added pin filtering for systems with high channel
 counts.

#### 2021

April 2021

- Added RFSG Signal Generator panel that supports interactive use and debugging with the
 following instruments:
  - PXIe-5820
  - PXIe-5830
  - PXIe-5831
  - PXIe-5832
  - PXIe-5840
  - PXIe-5841
- Added support for the PXIe-4135 (40W) and the PXIe-4137 (40W) source measure units.
 Supported in NI-DCPOWER 20.7.

#### 2020

November 2020

- Added support for the PXIe-4139(40W) source measure unit. Supported in NI-DCPower
 20.5.
- Added support for multichannel session in the SMU/Power Supply panel. Supported in
 NI-DCPower 20.6. Initializing an NI-DCPower session with independent
 channels allows you to use multiple instruments in the same session. With
 independent channels, you can configure multiple channels of the same
 instrument. You can also configure multiple channels of multiple instruments
 independent of one another within the same session.
- Added support for monitoring merged channels in debug mode on the PXIe-4147. Supported in
 NI-DCPower 20.6. Merging the channels of an SMU allows you to use multiple
 channels together. Using multiple channels together increases the current
 that you can source beyond the normal maximum for a single SMU channel.

Related information:

- Configure Channel Sessions

#### 2019 SP1

May 2020

- Added support for the PXIe-4147 source measure unit, newly supported in
 NI-DCPower 20.0.

#### 2019

September 2019

- You can synchronize multiple NI-SCOPE devices of the same model in the same oscilloscope
 panel.
- Added support for selecting trigger sources and events from other NI devices in your system.
- Added the following modes to SMU panels: These modes include automatic hardware synchronization across multiple
 devices.
  - Waveform graphing
  - Pulse current
  - Pulse voltage
  - Voltage sequence
  - Current sequence
- Added asymmetric limits and software-protected ranges to SMU/Power Supply panels.
- Added NI-DCPower SourceAdapt configuration to SMU panels, useful for transient
 measurements.
- Added channel views to the SMU/Power Supply panels to perform the following actions:
  - Hide idle channels
  - Show power calculations
  - Condense channel views
- Added inductance and capacitance measurements along with open and short cable compensation
 to digital multimeter (DMM) panels.
- Added the ability to generate waveforms from binary files to the waveform generator
 panel.
- Added debugging and monitoring support to the waveform generator panel.
- Added exporting configuration files from the waveform generator panel for use with the
 NI-FGEN driver.
- Added capability to export device configurations to TestStand for use in test step
 configuration.
- Added ability to use pin maps created in Digital Pattern Editor. Such pin maps allow you to
 group devices and channels by site. Such pin maps also allow you to use pin
 names for channel aliases.

#### 2018 SP2

January 2019

- Added support for the PXIe-5163 oscilloscope. Supported in NI-SCOPE 18.7.
- Added CSV file format for data capture.
- Added support for exporting instrument events to PXI chassis trigger lines.
- Added support for the following modes to Waveform Generator panels:
  - Arbitrary waveform generation
  - Frequency list
  - Sweep
- Added the following elements to Oscilloscope panels:
  - FFT channels
  - Frequency markers
  - FFT channel measurements
  - Additional two-channel measurements

Related information:

- Capture Data
- Waveform Modes
- Add FFT Channels and Markers

#### 2018 SP1

September 2018

- Added support for the following oscilloscopes: Supported in NI-SCOPE 18.6.
  - PXIe-5110
  - PXIe-5111
  - PXIe-5113

#### 2018

May 2018

- This was the initial release of InstrumentStudio.

<!--NI_TOPIC bundle=instrumentstudio path=user-manual-welcome.html language=enus -->
## TOPIC 00071: InstrumentStudio User Manual

- bundle_id: `instrumentstudio`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/user-manual-welcome.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The InstrumentStudio User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### InstrumentStudio
 User Manual

The InstrumentStudio User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- What is InstrumentStudio?
- Download InstrumentStudio
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- InstrumentStudio Plug-Ins on GitHub
- NI Learning Center

<!--NI_TOPIC bundle=instrumentstudio path=using-site-filter.html language=enus -->
## TOPIC 00072: Using the Site Filter

- bundle_id: `instrumentstudio`
- source_path: `using-site-filter.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/using-site-filter.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: After you set an active pin map in InstrumentStudio, the devices in your panel appear as pins. Use the site filter in the document toolbar to display pins from a selected site. InstrumentStudio filters your pins by the following characteristics: Sites System Pins Unmapped channels In your instrument

### Using the Site Filter

After you set an active pin map in InstrumentStudio, the devices in your panel appear
 as pins. Use the site filter in the document toolbar to display pins from a selected
 site.

- Sites
- System Pins
- Unmapped channels

1. In your instrument panel, click the Site filter drop-down menu
 in the toolbar at the top of the document window.
2. Select a site from the list to filter the view in the panel to the selected site.

Note

- You must select All sites in the site filter to view unmapped
 channels.
- Site filtering does not apply to RF signal generators, because you can map each
 device channel to multiple pins on multiple sites. You must select sites and pins in
 the RF signal generator panel settings ([IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png']).
- You cannot export an InstrumentStudio configuration to TestStand when the site filter
 is set to All sites. Select a specific site in the site filter or
 select System pins to only export system pins.

Parent topic:

Pin Maps

Related reference:

- Export Configurations

<!--NI_TOPIC bundle=instrumentstudio path=view-seq-report.html language=enus -->
## TOPIC 00073: View a Sequence Report

- bundle_id: `instrumentstudio`
- source_path: `view-seq-report.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/view-seq-report.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: A sequence report is a .pdf file that details the results of a sequence. InstrumentStudio generates a sequence report every time you execute a sequence. InstrumentStudio adds the sequence execution report files to the Project Files pane. You can also find the sequence report file in the Sequence Res

### View a Sequence Report

A sequence report is a .pdf file that details the results of a
 sequence. InstrumentStudio generates a sequence report every time you execute a
 sequence.

Project Files

Sequence Results

Sequence
 Results

1. Wait for the sequence to execute.
2. Click the View Report button. The generated report opens
 in the default .pdf viewer on your system.

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=view-sq-log.html language=enus -->
## TOPIC 00074: View a Sequence Execution Log

- bundle_id: `instrumentstudio`
- source_path: `view-sq-log.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/view-sq-log.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `task`
- source_description: When you execute a sequence, InstrumentStudio creates an execution log in the sequencer pane. You can use the execution log to check the status and the execution time of each step. The execution log updates in real time while the sequence runs. The execution log shows the current step and the steps

### View a Sequence Execution Log

When you execute a sequence, InstrumentStudio creates an execution log in the sequencer
 pane. You can use the execution log to check the status and the execution time of each
 step.

The execution log updates in real time while the sequence
 runs. The execution log shows the current step and the steps that InstrumentStudio
 already executed.

1. Open the Sequencer pane.
2. Click Execution log.

Parent topic:

Sequencer Tool

<!--NI_TOPIC bundle=instrumentstudio path=wave-gen.html language=enus -->
## TOPIC 00075: Waveform Generators

- bundle_id: `instrumentstudio`
- source_path: `wave-gen.html`
- source_url: https://docs-be.ni.com/bundle/instrumentstudio/raw/resource/enus/wave-gen.html
- document_id: `instrumentstudio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Waveform Generator panel to generate waveforms and configure your Waveform Generator instruments. Generate Waveforms with a Waveform Generator Use a waveform generator to monitor and configure waveforms in InstrumentStudio. Add a waveform generator device to the large panel. Select one of th

### Waveform Generators

Use the Waveform Generator panel to generate waveforms and configure your Waveform
 Generator instruments.

Parent topic:

Configure Device Settings

#### Generate Waveforms with a Waveform
 Generator

Use a waveform generator to monitor and configure waveforms in InstrumentStudio.

1. Add a waveform generator device to the large panel.
2. Select one of the following waveform modes from the dropdown menu of the device
 panel:
  - Standard
 waveform —Generates a waveform using the channel settings that you
 specify.
  - Arbitrary
 waveform —Generates a waveform using settings specified in a waveform file and
 any additional channel settings that you specify. Note For more information on waveform
 modes, see [Waveform Modes](wave-gen.html#GUID-FE4AC4F9-3586-4EAD-9A05-EC9913F00284).
3. Specify the type of the waveform.
  - For a standard waveform, you can
 select the waveform type with the Waveform dropdown menu. Note If you select a
 User-defined waveform, you must load a waveform file. User-defined
 waveform files must be in the .csv format, with the exact number
 of samples that the *Specifications* document of your device defines. For
 example, the PXIe-5433 requires 8192 samples for a user-defined waveform. The waveform
 samples must be in a single row or a single column.
  - For an arbitrary waveform, you must
 load a waveform file. Click the … button next to the
 Filename field to browse for the waveform file. The waveform
 file specifies the type of waveform to generate. Note Arbitrary waveform files can be in the
 .csv format or a binary format:**.csv**—For single-channel instruments, waveform samples must be in a single row or a
 single column. For two-channel instruments, the waveform samples for each
 channel must be in a separate column.
 **Binary**—For single-channel instruments, waveform samples can be 8-byte
 double-prevision or 2-byte half-precision floating point. The byte order can be
 little-endian or big-endian. For two-channel instruments, the samples of both
 channels must be interleaved.
4. Configure the waveform channel settings directly on the large panel or in the
 Channel Settings window. To open the Channel
 Settings window, click on the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon next to the channel. The settings that you can configure change based on the
 waveform mode and waveform type that you select. 
 Note If you generate an arbitrary
 waveform, you must select a trigger mode for the waveform. To select a trigger mode,
 complete the following steps:Click on the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon to open the Channel Settings window.
 Scroll down to the Triggers section.
 Use the dropdown menu of the Mode setting.For more information on arbitrary waveform trigger modes, see *Advanced
 Waveform Sequencing and Triggering on Arbitrary Waveform Generators* in the
 *Related Information* section.
5. Select Run.

The waveform generates with the specified settings.

Related information:

- Advanced Waveform Sequencing and Triggering on Arbitrary Waveform
 Generators

#### Waveform Modes

You can generate a waveform using one of the following modes:

Standard waveform

- Outputs waveforms according to the channel settings that you specify in
 InstrumentStudio or an external application.
- Allows you to generate different waveform types (for example, sine, square, or
 triangle) at precise frequencies.
- Allows you to change the output waveform frequency of a standard waveform with a
 short response time during waveform generation.
- The Sweep operation mode allows you to configure a range of
 frequencies to generate over a specified number of steps and a specified time
 duration.
- The List operation mode allows you to configure a sequence of
 frequencies to generate for specified durations.

Note

User-defined

Arbitrary Waveform

Arbitrary waveform

#### Configure Waveform Channels and
 Triggers

You can configure channels, triggers, and other parameters of the waveform generator
 from the Channel Settings window.

Click the [IMAGE alt='An icon of three horizontal dots.' src='GUID-E68BBAB0-F43D-46F6-866A-4EDA49C930FC-a5.png'] icon to open the Channel Settings window. You can select the
 channel that you want to configure on the left side of the window.

##### Waveform Channel Settings

devicename/channel_number

Channel Settings

Output Impedance

50 Ω

75 Ω

Load Impedance

Match output

High-Z

Custom

Digital Filter

Analog Filter

Terminal config.

Differential

Single-ended

##### Waveform General Settings

The settings in the Waveform section of the Channel
 Settings window correspond to the controls on the panel. The settings that
 appear in this section depend on the waveform mode and the type of the standard
 waveform.

##### Waveform Trigger Settings

Triggers

Channel Settings

Trigger Mode

Note

Advanced Waveform Sequencing and Triggering on Arbitrary Waveform
 Generators

Related Information

Trigger Type

Immediate

Software

Digital edge

##### Hardware Event Output Terminals

The settings in the Hardware event output terminals section of the
 Channel Settings window determine the chassis terminal to which
 InstrumentStudio exports hardware events.

Related information:

- Advanced Waveform Sequencing and Triggering on Arbitrary Waveform
 Generators

#### Waveform Generator Status

You can see the current generation status of non-idle channels in the
 Channel Settings window or through the generation status icon. The
 generation status icon is next to the Waveform dropdown menu of a
 channel.

| Icon | Status | Description |
| --- | --- | --- |
|  | Generating output | Waveform generation is running on this channel. |
|  | Not generating output | Waveform generation is stopped on this channel. |
|  | Waiting for trigger | The channel is waiting to start an operation until the trigger condition occurs. |
|  | Unknown status | The output status of the channel is unknown. Run the panel to refresh the output status. |

Note
