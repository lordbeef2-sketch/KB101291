# NI DOCUMENT BUNDLE: ni-dcpower

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower start=1 end=27 -->
<!--NI_TOPIC bundle=ni-dcpower path=advanced-sequencing.html language=enus -->
## TOPIC 00001: Advanced Sequencing

- bundle_id: `ni-dcpower`
- source_path: `advanced-sequencing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/advanced-sequencing.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use advanced sequencing instead of the NI-DCPower Set Sequence function when you want more options for configuring a channel differently between sequence steps. In each advanced sequence step, you can specify the state of an individual channel by configuring a large selection of properties. For more

### Advanced Sequencing

Use advanced sequencing instead of the NI-DCPower Set Sequence
 function when you want more options for configuring a channel differently between sequence
 steps.

In each advanced sequence step, you can specify the state of an individual channel by configuring
 a large selection of properties.

Note

Set Sequence

#### Differences Between Advanced Sequencing and Simple Sequencing

- Simple sequencing is configured using NI-DCPower Set Sequence . Advanced
 sequencing is configured using a combination of NI-DCPower properties, the
 NI-DCPower Create Advanced Sequence With Channels function,
 and the Create Advanced Sequence Step With Channels 
 function.
- In an advanced sequence, you can change a greater selection of properties in each step than you
 can in a simple sequence.
  - Simple sequencing configures a series of voltage or current outputs and,
 optionally, corresponding source delays. Simple sequences are configured
 using Set Sequence .
  - Advanced sequencing allows you to choose which properties to change
 between sequence steps. Advanced sequences are configured using a
 combination of NI-DCPower properties, the Create Advanced
 Sequence function, and the Create Advanced
 Sequence Step With Channels function. For example, in an
 advanced sequence, you could also change the measurement aperture time
 for each step, or switch between voltage and current output for each
 step.
- In an advanced sequence, you can create a Commit step to configure channels to a known state
 before the sequence runs.
- Programming a device with advanced sequencing requires you to use specific advanced sequencing
 functions that are not used in simple sequencing.
- You can use the Export Attribute Configuration and Import Attribute
 Configuration functions to transfer advanced sequences between
 sessions, but not simple sequences.

Refer to the NI-DCPower Advanced Sequence Changing Aperture Time.vi or
 NI-DCPower Advanced Sequence Changing Output Function.vi
 examples in the LabVIEW Example Finder. For an example of simple sequencing using
 the niDCPower Set Sequence VI, refer to the NI-DCPower
 Hardware-Timed Voltage Sweep.vi example.

#### Support for Advanced Sequencing

The following devices do not support advanced sequencing:

- PXI-4110
- PXIe-4112/4113
- PXI-4130
- PXI-4132
- PXIe-4154

Note

Parent topic:

Programming with NI-DCPower

Related concepts:

- NI-DCPower Sequence Source Mode

Related tasks:

- NI-DCPower Typical Sequence Operation

<!--NI_TOPIC bundle=ni-dcpower path=configuring-channels.html language=enus -->
## TOPIC 00002: Configuring Channels

- bundle_id: `ni-dcpower`
- source_path: `configuring-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/configuring-channels.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channels have two basic source modes: Single point and sequence. The sequence source mode encompasses both simple sequences and advanced sequences. In each of these modes, you can output constant or pulsed voltage or current. Attribute values do not persist between sessions. If you close a sessio

### Configuring Channels

Channels have two basic source modes: *Single point* and *sequence*.
 The sequence source mode encompasses both simple sequences and advanced sequences. In each of
 these modes, you can output constant or pulsed voltage or current.

Note

- Attribute values do not persist between sessions. If you close a session and open a new
 session, all attributes assume their default values. However, the default values are not
 committed to hardware until the channels enter the Committed or Running state.
- Some NI-DCPower instruments have resources that are shared by different sessions to the
 same instrument. You cannot configure these resources independently by channel.

#### Configuring Channels in Single Point Source
 Mode

Complete the following steps to configure channels in
 single point source mode.

1. Set the Source Mode to Single Point
 using NI-DCPower Configure Source Mode With Channels.
2. Configure the source unit.
3. (Optional) Configure the measure unit.

#### Configuring Channels in Sequence Source
 Mode

Complete the following steps to configure
 channels in sequence source mode.

1. Set the Source Mode to Sequence
 using NI-DCPower Configure Source Mode With Channels.
2. Configure the source unit.
3. Create a simple sequence with NI-DCPower Set Sequence, or
 create an advanced sequence with NI-DCPower Create Advanced Sequence
 With Channels.
4. (Optional) Configure the measure unit.

<!--NI_TOPIC bundle=ni-dcpower path=constant-power-resistance-dcpower.html language=enus -->
## TOPIC 00003: Constant Resistance and Constant Power

- bundle_id: `ni-dcpower`
- source_path: `constant-power-resistance-dcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/constant-power-resistance-dcpower.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DCPower electronic loads support sinking at both a constant configured resistance and a constant configured power. When you configure your electronic load to sink at a constant resistance, the device maintains a constant ratio between voltage and current being sunk, which is useful in any scenari

### Constant Resistance and Constant Power

NI-DCPower electronic loads support
 sinking at both a constant configured resistance and a constant configured
 power.

When you configure your electronic load to sink at a constant resistance, the device
 maintains a constant ratio between voltage and current being sunk, which is useful in
 any scenario where you want to test a power source connected to a resisted load.

P

=

V

I

- P is power,
- V is voltage, and
- I is current.

This is useful for cases like emulating a DC-DC converter
 for battery discharge testing, or testing the power output of a source across a voltage
 range.

NI-DCPower

Constant
 Resistance

Constant Power

NI-DCPower

Output Function

| Constant Resistance | Constant Power |
| --- | --- |
| Constant Resistance Level | Constant Power Level |
| Constant Resistance Level Range | Constant Power Level Range |
| Constant Resistance Current Limit | Constant Power Current Limit |
| Constant Resistance GBW | Constant Power GBW |
| Constant Resistance Compensation Freq | Constant Power Compensation Freq |
| Constant Resistance Pole-Zero Ratio | Constant Power Pole-Zero Ratio |

Note

NI-DCPower

Constant
 Resistance

Constant Resistance Current Limit

Note

NI-DCPower

Constant Power

Constant Power Current Limit

NI-DCPower

NI-DCPower Constant
 Resistance and Constant Power.vi

C:\Program
 Files\NI\LVAddons\nidcpower\1\examples\instr\niDCPower\Electronic Load

Note

NI-DCPower

Constant Power

Parent topic:

Programming with NI-DCPower

Related information:

- NI-DCPower Constant Power Properties
- NI-DCPower Constant Resistance Properties
- NI-DCPower Custom Transient Response Constant Power
 Properties
- NI-DCPower Custom Transient Response Constant Resistance
 Properties

<!--NI_TOPIC bundle=ni-dcpower path=detecting-internalauxiliary-power.html language=enus -->
## TOPIC 00004: Detecting Internal/Auxiliary Power

- bundle_id: `ni-dcpower`
- source_path: `detecting-internalauxiliary-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/detecting-internalauxiliary-power.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an auxiliary power source to enable the full-power capabilities of NI instruments that support this feature. NI-DCPower can dynamically query whether the auxiliary power is connected to the device. The NI-DCPower Auxiliary Power Source Available property returns TRUE if auxiliary power is connec

### Detecting Internal/Auxiliary Power

Use an auxiliary power source to enable the full-power capabilities of NI instruments
 that support this feature. NI-DCPower can dynamically query whether the auxiliary power is
 connected to the device.

The NI-DCPower Auxiliary Power Source Available property returns
 TRUE if auxiliary power is connected to the device and
 FALSE if only internal power is available on the device.

NI instruments cannot differentiate between an auxiliary power loss or a blown fuse on the
 auxiliary power input line. If auxiliary power is properly connected and Auxiliary
 Power Source Available returns FALSE, you might need to replace
 the auxiliary power input fuse.

Parent topic:

Programming with NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower path=driver-setup-string.html language=enus -->
## TOPIC 00005: Driver Setup String

- bundle_id: `ni-dcpower`
- source_path: `driver-setup-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/driver-setup-string.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DriverSetup keyword is set using the driver setup string, and comprises the resource name (multi-instrument sessions only), instrument model number, and bus connector. When you specify the driver setup string, NI-DCPower uses the option string parameter of niDCPower Initialize With Independent C

### Driver Setup String

The DriverSetup keyword is set using the driver setup string, and
 comprises the resource name (multi-instrument sessions only), instrument model number, and
 bus connector.

When you specify the driver setup string, NI-DCPower uses the option
 string parameter of niDCPower Initialize With Independent
 Channels to determine the following:

- How many instruments to simulate;
- Which channel numbers to use; and
- Which channels belong on which simulated instrument.

If you do not specify the driver setup string, NI-DCPower simulates the device specified
 in the resource name parameter.

You do not have to specify a value for all the option string
 properties. If you do not specify a value for a property, NI-DCPower uses the default
 value. If you specify a Model but not a BoardType, the
 driver infers the board type. If you specify neither the driver setup string nor the
 resource name parameter, or if you do include a driver setup
 string that excludes a Model, NI-DCPower simulates the device by
 default.

Parent topic:

Simulating an Instrument with NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower path=dynamic-reconfiguration.html language=enus -->
## TOPIC 00006: Dynamic Reconfiguration

- bundle_id: `ni-dcpower`
- source_path: `dynamic-reconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/dynamic-reconfiguration.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: While in the Running state, you can edit the source configuration dynamically using any VI, function, property or attribute listed in the tables below. When editing the source configuration dynamically, the changes are immediately applied. For sessions that include multiple channels and were created

### Dynamic Reconfiguration

While in the Running state, you can edit the source configuration dynamically using any VI,
 function, property or attribute listed in the tables below. When editing the source
 configuration dynamically, the changes are immediately applied. For sessions that include
 multiple channels and were created with NI-DCPower Initialize With Independent
 Channels, changes are applied to the channels in parallel.

The following output functions support dynamic reconfiguration:

- DC Voltage
- DC Current
- Constant Resistance
- Constant Power

Note

| VI | Function |
| --- | --- |
| niDCPower Configure Voltage Level | niDCPower_ConfigureVoltageLevel |
| niDCPower Configure Voltage Level Range | niDCPower_ConfigureVoltageLevelRange |
| niDCPower Configure Voltage Limit | niDCPower_ConfigureVoltageLimit |
| niDCPower Configure Voltage Limit Range | niDCPower_ConfigureVoltageLimitRange |
| niDCPower Configure Current Level | niDCPower_ConfigureCurrentLevel |
| niDCPower Configure Current Level Range | niDCPower_ConfigureCurrentLevelRange |
| niDCPower Configure Current Limit | niDCPower_ConfigureCurrentLimit |
| niDCPower Configure Current Limit Range | niDCPower_ConfigureCurrentLimitRange |
| niDCPower Configure Output Enabled | niDCPower_ConfigureOutputEnabled |

| Property | Attribute |
| --- | --- |
| Voltage Level | NIDCPOWER_ATTR_VOLTAGE_LEVEL |
| Voltage Level Range | NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE |
| Current Level | NIDCPOWER_ATTR_CURRENT_LEVEL |
| Current Level Range | NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE |
| Constant Resistance Level | NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL |
| Constant Resistance Level Range | NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE |
| Constant Power Level | NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL |
| Constant Power Level Range | NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE |
| Voltage Limit | NIDCPOWER_ATTR_VOLTAGE_LIMIT |
| Voltage Limit High | NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH |
| Voltage Limit Low | NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW |
| Voltage Limit Range | NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE |
| Current Limit | NIDCPOWER_ATTR_CURRENT_LIMIT |
| Current Limit High | NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH |
| Current Limit Low | NIDCPOWER_ATTR_CURRENT_LIMIT_LOW |
| Current Limit Range | NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE |
| Constant Resistance Current Limit | NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT |
| Constant Power Current Limit | NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT |
| Output Enabled | NIDCPOWER_ATTR_OUTPUT_ENABLED |
| Output Connected | NIDCPOWER_ATTR_OUTPUT_CONNECTED |
| Output Shorted | NIDCPOWER_ATTR_OUTPUT_SHORTED |
| Output Resistance | NIDCPOWER_ATTR_OUTPUT_RESISTANCE |
| OVP Enabled | NIDCPOWER_ATTR_OVP_ENABLED |
| Self Calibration Persistence | NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE |
| Source Delay | NIDCPOWER_ATTR_SOURCE_DELAY |
| Requested Power Allocation | NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION |

Dynamic reconfiguration is only available when Source trigger is disabled. Therefore, in Single
 Point source mode, the device can wait for and accept only one Source trigger and apply a
 single source configuration. If you want the device to wait for another Source trigger before
 reconfiguring the source, either use Sequence source mode or call NI-DCPower Abort
 With Channels followed by Initiate With Channels to start a new
 Single Point generation that waits for a trigger.

Parent topic:

Single Point Source Mode

Related concepts:

- Programming States

Related information:

- NI-DCPower LabVIEW Reference

<!--NI_TOPIC bundle=ni-dcpower path=extended-support-changes.html language=enus -->
## TOPIC 00007: Updates and Changes for NI-DCPower Extended Support Versions

- bundle_id: `ni-dcpower`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/extended-support-changes.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in NI-DCPower versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible chang

### Updates and Changes for NI-DCPower Extended Support Versions

Browse updates and changes made in NI-DCPower versions
 on extended support.

Note

Release Notes

#### NI-DCPower 2024 Q3 New Features and
 Changes

- Support for PXIe-4162/4163 Merged Channels
- Support for PXIe-4150

Related information:

- PXIe-4162 Merged Channels
- PXIe-4163 Merged Channels

#### NI-DCPower 2024 Q1 New Features and
 Changes

- Added Accessory Detection support for ACC-4162-3 and ACC-4163-3

#### NI-DCPower 2023 Q4 New Features and
 Changes

- Support for OpenSUSE 15.5
- Dropped support for OpenSUSE 15.3
- Support for PXIe-4151
- Support for PXIe-4051
  - Added programmable current level slew rate support for PXIe-4051
  - Enabled setting Conduction Voltage threshold for PXIe-4051
  - New mode supported by the Instrument Mode property: E_LOAD
- Enhanced Output Cutoff feature for PXIe-4135/4136/4137/4138/4139
- Accessory Detection support for ACC-4162-1 and ACC-4163-1

#### NI-DCPower 2023 Q3 New Features and Changes

- Support for PXIe-4162 Asymmetrical Compliance Limit
- Support for PXIe-4162 Measurement Autorange

#### NI-DCPower 2023 Q2 New Features and Changes

- LCR Source Aperture Time attribute for PXIe-4190
- Customizable DC Bias Transient Response for PXIe-4190
- Detection of unbalanced conditions on PXIe-4190

#### NI-DCPower 2023 Q1 New Features and
 Changes

- Support for PXIe-4163 Remote Sense Over Voltage Protection (OVP)
- Support for PXIe-4162 Remote Sense Over Voltage Protection (OVP)
- Support for PXIe-4190 DC Bias Automatic Level Control Off
- Support for PXIe-4190 "As Configured" as an LCR Open/Short/Load Compensation Data Source
- Support for PXIe-4190 SMU Measurement Autorange

<!--NI_TOPIC bundle=ni-dcpower path=importexport-attribute-configuration-mapping-.html language=enus -->
## TOPIC 00008: NI-DCPower Import/Export Attribute Configuration Mapping Behavior

- bundle_id: `ni-dcpower`
- source_path: `importexport-attribute-configuration-mapping-.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/importexport-attribute-configuration-mapping-.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to map import/export configurations between NI-DCPower sessions, ensure correct channel mapping, and handle errors for seamless integration across different channels. When you export and import configurations between NI-DCPower sessions, the channels can differ in several ways, including t

### NI-DCPower Import/Export Attribute Configuration Mapping Behavior

Learn how to map import/export configurations between NI-DCPower sessions, ensure correct channel
 mapping, and handle errors for seamless integration across different channels.

NI-DCPower

- Properties
- Attributes
- Values

#### Mapping Rules

NI-DCPower maps the configurations
 from the exporting channels to the importing channels. This mapping relies on the order
 of resources that you specify in the resource name input of the
 Initialize With Independent Channels node for each session.

NI-DCPower

- Both sessions initialize the same number of channels.
- The model of each exporting channel matches the model of the corresponding
 exporting channel.

NI-DCPower

#### Mapping Examples

The following scenarios describe how NI-DCPower maps channels when you export and import configurations
 between sessions. Each scenario outlines the resource order for the exporting session
 and the importing session, then lists the Exporting → Importing channel mappings.

Single instrument per session

- Exporting resources: PXI1Slot3/0-1
- Importing resources: PXI1Slot4/1-2
- Channel mappings:
  - PXI1Slot3/0 → PXI1Slot4/1
  - PXI1Slot3/1 → PXI1Slot4/2

Multiple instruments per session, equal count

- Exporting resources: PXI1Slot4/3 ,
 PXI1Slot5/3
- Importing resources: PXI1Slot2/0 ,
 PXI1Slot3/0
- Channel mappings:
  - PXI1Slot4/3 → PXI1Slot2/0
  - PXI1Slot5/3 → PXI1Slot3/0

Importing to fewer instruments

- Exporting resources: PXI1Slot4/3 ,
 PXI1Slot5/3
- Importing resources: PXI1Slot3/0-1
- Channel mappings:
  - PXI1Slot4/3 → PXI1Slot3/0
  - PXI1Slot5/3 → PXI1Slot3/1

Importing to more instruments

- Exporting resources: PXI1Slot3/0-1
- Importing resources: PXI1Slot4/3 ,
 PXI1Slot5/3
- Channel mappings:
  - PXI1Slot3/0 → PXI1Slot4/3
  - PXI1Slot3/1 → PXI1Slot5/3

#### Mapping Exceptions

Some properties have unique import/export mapping behavior.

- For the Merged Channels property, NI-DCPower remaps only the
 instrument name, not the channel name. Example: Importing the
 PXI1Slot2/0 value to a session on PXI1Slot3/1
 remaps the configuration to PXI1Slot3/0.

#### Mapping Behavior Overview for Fully
 Qualified Terminal Names

NI-DCPower

- whether the Engine number you specify in the name matches the engine number of
 the channel
- whether the terminal name includes an Engine number
- whether the instrument alias specified for a terminal matches an instrument alias
 in the session

Note

NI-DCPower

NI-DCPower

- Table 4.Terminal Mappings for Equal
 Instrument Count
- Table 5.Terminal Mappings for Exporting to
 Fewer Instruments
- Table 6.Terminal Mappings for Exporting to
 More Instruments

#### Mapping Scenario: Equal Instrument
 Count

When both sessions contain the same number of instruments, the channel assignments are
 as follows.

- Exporting session: Dev1/0 and Dev2/0
- Importing session: Dev3/1 and Dev4/1

| Source Terminal Name | Target Terminal Name |
| --- | --- |
| /Dev1/PXI_Trig0 | /Dev3/PXI_Trig0 |
| /Dev2/PXI_Trig3 | /Dev4/PXI_Trig3 |
| /Dev1/Engine0/MeasureTrigger | /Dev3/Engine1/MeasureTrigger |
| /Dev2/Engine0/MeasureTrigger | /Dev4/Engine1/MeasureTrigger |
| /Dev1/Engine5/MeasureTrigger | /Dev3/Engine5/MeasureTrigger |
| Engine0/MeasureTrigger | Engine0/MeasureTrigger |
| /Dev5/Engine0/MeasureTrigger | /Dev5/Engine0/MeasureTrigger |

#### Mapping Scenario: Exporting to Fewer
 Instruments

When you export data, you use two instruments. During the import process, you combine
 these channels onto one instrument. The channel assignments are as follows.

- Exporting session: Dev1/0 and Dev2/0
- Importing session: Dev3/0-1

| Source Terminal Name | Target Terminal Name |
| --- | --- |
| /Dev1/PXI_Trig0 | /Dev3/PXI_Trig0 |
| /Dev2/PXI_Trig3 | /Dev3/PXI_Trig3 |
| /Dev1/Engine0/MeasureTrigger | /Dev3/Engine0/MeasureTrigger |
| /Dev2/Engine0/MeasureTrigger | /Dev3/Engine1/MeasureTrigger |
| /Dev1/Engine5/MeasureTrigger | /Dev3/Engine5/MeasureTrigger |
| Engine0/MeasureTrigger | Engine0/MeasureTrigger |
| /Dev5/Engine0/MeasureTrigger | /Dev5/Engine0/MeasureTrigger |

#### Mapping Scenario: Exporting to More
 Instruments

When you export a session using one instrument with multiple channels, the system
 initially groups the channels together. During the import process, you can separate
 these channels across two instruments. The channel assignments in this scenario are as
 follows.

- Exporting session: Dev1/0-1
- Importing session: Dev2/0 and Dev3/0

| Source Terminal Name | Target Terminal Name |
| --- | --- |
| /Dev1/PXI_Trig0 | /Dev2/PXI_Trig0 |
| /Dev1/PXI_Trig3 | /Dev2/PXI_Trig3 |
| /Dev1/Engine0/MeasureTrigger | /Dev2/Engine0/MeasureTrigger |
| /Dev1/Engine1/MeasureTrigger | /Dev3/Engine0/MeasureTrigger |
| /Dev1/Engine5/MeasureTrigger | /Dev2/Engine5/MeasureTrigger |
| Engine0/MeasureTrigger | Engine0/MeasureTrigger |
| /Dev5/Engine0/MeasureTrigger | /Dev5/Engine0/MeasureTrigger |

#### Session Behavior on Import

In addition to channel and terminal mapping, importing a configuration has side effects
 on the state of the NI-DCPower
 session.

When you import an attribute configuration, the NI-DCPower session must be idle.

If the session is running, call Abort before importing the
 configuration.

1. Resets the session to a known initial state.
2. Applies all attribute values from the imported configuration.
3. Leaves the session in an idle state.

To begin sourcing or measuring, call Initiate.

If you need to modify attributes after import, apply the changes programmatically and
 then initiate the session.

- Import requires an idle session.
- Import performs a reset, applies attribute values on the session, but does not
 commit them to the device.
- The session remains idle after the import.
- To begin sourcing or measuring, call Initiate .

Note

Parent topic:

Programming with NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower path=instrumentstudio.html language=enus -->
## TOPIC 00009: Using InstrumentStudio with Your NI-DCPower Instrument

- bundle_id: `ni-dcpower`
- source_path: `instrumentstudio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/instrumentstudio.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can monitor, control, and record measurements from supported NI-DCPower instruments using InstrumentStudio. Use InstrumentStudio to perform interactive measurements on several different device types, including instruments, in a single program. Accessing InstrumentStudio InstrumentStudio is insta

### Using InstrumentStudio with Your NI-DCPower
 Instrument

You can monitor, control, and record measurements from supported NI-DCPower
 instruments using InstrumentStudio. Use InstrumentStudio to perform interactive measurements
 on several different device types, including instruments, in a single program.

#### Accessing InstrumentStudio

InstrumentStudio is installed with NI-DCPower. You can access InstrumentStudio in one
 of the following ways:

- From the Start menu. InstrumentStudio launches with a soft front panel that is
 populated with devices that are detected on your system.
- From Measurement & Automation Explorer (MAX), select a device and then click
 Test Panels... . InstrumentStudio launches with a soft
 front panel for the device you select.

Related information:

- InstrumentStudio Overview

<!--NI_TOPIC bundle=ni-dcpower path=max-help-for-ni-dcpower.html language=enus -->
## TOPIC 00010: Using Measurement & Automation Explorer for NI-DCPower

- bundle_id: `ni-dcpower`
- source_path: `max-help-for-ni-dcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/max-help-for-ni-dcpower.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Measurement & Automation Explorer (MAX) to complete the following common tasks for NI-DCPower. Running the Test Panels Use test panels to interactively test the functionality of your device. To run the test panels, right-click the device name in the MAX configuration tree, and select Test Panels

### Using Measurement & Automation Explorer
 for NI-DCPower

Use Measurement & Automation Explorer (MAX) to complete the following common
 tasks for NI-DCPower.

#### Running the Test Panels

Use test panels to interactively test the functionality of your device. To run the test
 panels, right-click the device name in the MAX configuration tree, and select
 Test Panels.

#### Removing Your Device

To remove the device from your configuration, right-click the device name in the
 configuration tree and select Delete. This option is only
 valid if the physical device is no longer present in the system.

#### Viewing or Changing Device Properties

To view or change device properties, right-click the device name in the configuration
 tree and select Properties.

<!--NI_TOPIC bundle=ni-dcpower path=new-features-and-changes.html language=enus -->
## TOPIC 00011: NI-DCPower New Features and Changes

- bundle_id: `ni-dcpower`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-DCPower. Discover what is new in the latest releases of NI-DCPower.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might in

### NI-DCPower
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-DCPower.

NI-DCPower

Note

Release Notes

Related information:

- Software and Driver Downloads
- NI-DCPower Release Notes

#### NI-DCPower 2025 Q2 New Features and
 Changes

- Support for Constant Resistance and Constant Power operation modes added.
- Added support for Output Shorted property for PXIe-4051 .
- Prevent overshoot at low current when using the DC Current output function with the
 PXIe-4051 by updating the Normal presets of the PXIe-4051 current custom transient
 response properties.

Related concepts:

- Constant Resistance and Constant Power

Related information:

- Output Shorted

#### NI-DCPower 2025 Q1 New Features and
 Changes

- Support for INHIBIT pin added to the following modules:
  - PXIe-4051
  - PXIe-4150
  - PXIe-4151

<!--NI_TOPIC bundle=ni-dcpower path=ni-dcpower-examples.html language=enus -->
## TOPIC 00012: NI-DCPower Examples

- bundle_id: `ni-dcpower`
- source_path: `ni-dcpower-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/ni-dcpower-examples.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI installs example code with your software or driver that demonstrates the functionality of NI-DCPower. Use these examples to learn about the product or accelerate your own application development. Most NI products install examples that you can access directly or from within NI software. The exampl

### NI-DCPower Examples

NI installs example code with your software or driver that demonstrates the
 functionality of NI-DCPower. Use these examples to learn about the product or accelerate
 your own application development.

Most NI products install examples that you can access directly or from within NI
 software. The example experience can differ slightly across products and versions.

#### Installed Example Locations

| Option | Installed Example Locations |  |
| --- | --- | --- |
| LabVIEW | <LabVIEW>\\examples\\instr\\nidcpower, where <LabVIEW> is the LabVIEW directory for the specific LabVIEW version you installed on your system. |  |
| LabWindows/CVI | Users\\Public\\Documents\\National Instruments\\CVI\\samples\\niDCPower |  |
| .NET | 4.0 | Users\\Public\\Documents\\National Instruments\\NI-DCPower\\Examples\\DotNET 4.0 |
| 4.5 | Users\\Public\\Documents\\National Instruments\\NI-DCPower\\Examples\\DotNET 4.5 |  |

#### Common NI-DCPower Examples

| NI-DCPower Example | Description |
| --- | --- |
| NI-DCPower Source DC Voltage | Demonstrates how to force an output voltage. |
| NI-DCPower Source DC Current | Demonstrates how to force an output current. |
| NI-DCPower Hardware-Timed Voltage Sweep | Demonstrates how to sweep the voltage on a single channel and display the results in a graph. |
| NI-DCPower Measure Record | Demonstrates how to take multiple measurements in succession. |
| NI-DCPower Measure Step Response | Demonstrates how to measure the output while it is changing. |

<!--NI_TOPIC bundle=ni-dcpower path=ni-dcpower-overview.html language=enus -->
## TOPIC 00013: NI-DCPower Overview

- bundle_id: `ni-dcpower`
- source_path: `ni-dcpower-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/ni-dcpower-overview.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DCPower instrument driver supports NI power supplies, source measure units (SMUs), and electronic loads (E-loads). This User Manual provides detailed descriptions of the driver functionality. This User Manual refers to power supplies, SMUs, and E-loads inclusively as instruments. If informati

### NI-DCPower Overview

The NI-DCPower instrument driver supports NI power supplies, source measure units (SMUs), and
 electronic loads (E-loads). This User Manual
 provides detailed descriptions of the driver
 functionality.

Note

<!--NI_TOPIC bundle=ni-dcpower path=programming-flow.html language=enus -->
## TOPIC 00014: Programming Flow

- bundle_id: `ni-dcpower`
- source_path: `programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/programming-flow.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to program your instrument. Opening a Session To open a session, call NI-DCPower Initialize With Independent Channels. For any application you write, you must open a session to establish communication with the specified device(s) or channel(s) by initializing. Initializi

### Programming Flow

Complete the following steps to program your instrument.

Parent topic:

Programming with NI-DCPower

Related concepts:

- Programming States
- Single Point Source Mode
- NI-DCPower Sequence Source Mode
- Advanced Sequencing
- Pulsing

#### Opening a Session

To open a session, call NI-DCPower Initialize With Independent
 Channels.

For any application you write, you must open a session to establish communication
 with the specified device(s) or channel(s) by initializing.

Initializing returns an instrument handle with the session configured to a known
 state. Initialization can take a significant amount of time compared to other
 NI-DCPower functions, so you should not include it in a loop when repeatedly
 acquiring data. Ideally, your program should call NI-DCPower Initialize
 With Independent Channels one time. If the reset
 parameter is set to TRUE, device channels are reset to the
 default state, which may include resetting relays.

#### Initiating Generation and Acquisition

To apply the configuration and start generation, use NI-DCPower Initiate
 With Channels.

#### Measuring, Querying, or Fetching

The source mode that you select for configuring channels
 determines how NI-DCPower acquires measurements.

To acquire measurements in single point source mode complete the following steps.

1. Measure with NI-DCPower Measure Multiple .
2. To query the output state, call NI-DCPower Query In
 Compliance .

NI-DCPower automatically acquires measurements when you configure the following
 functions:

- NI-DCPower Create Advanced Sequence With Channels
- NI-DCPower Set Sequence
- NI-DCPower Configure Output Function set to Pulse
 Voltage or Pulse Current

NI-DCPower automatically acquires the measurements by coercing the NI-DCPower
 Measure When property to Automatically After Source
 Complete. NI-DCPower returns the measurement values in an array.

Tip

Measure When

Automatically After Source Complete

#### Closing the Session

To close a session, use NI-DCPower Close.

Closing a session is essential for freeing resources, including deallocating memory,
 destroying threads, and freeing operating system resources. Ensure that you close
 every session that you initialize, even if an error occurs during the program. When
 debugging your application, it is common to abort execution before you close.

Note

The channels continue to operate in their last configured state when you close a
 session. If you close a session while the output channels are enabled and actively
 sourcing or sinking power, the channels continue to source or sink power until you
 disable or reset them.

<!--NI_TOPIC bundle=ni-dcpower path=programming-states.html language=enus -->
## TOPIC 00015: Programming States

- bundle_id: `ni-dcpower`
- source_path: `programming-states.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/programming-states.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI-DCPower channel has three main states: Uncommitted Committed Running Each channel in a session can move through these states independent of one another. 1 NI-DCPower Programming States Sessions created using the Initialize With Independent Channels function have different capabilities from tho

### Programming States

An NI-DCPower channel has three main states:

- Uncommitted
- Committed
- Running

Each channel in a session can move through these states independent of one
 another.

Figure 1.

[IMAGE alt='image' src='GUID-AC9C7DFC-5CEB-47C6-AE18-CCC6292B79D3-a5.png']

Note

#### Uncommitted

Channels enter the Uncommitted state when you call NI-DCPower
 Initialize With Independent Channels, or
 if you abort the session using NI-DCPower Abort With
 Channels.

NI-DCPower Reset With Channels and NI-DCPower
 Reset Device also place channels in the
 Uncommitted state.

Although you can configure properties in the Uncommitted state,
 NI-DCPower does not apply the properties until the Committed or
 Running states. For example, NI-DCPower Export Attribute
 Configuration verifies that the properties that
 you configure for a session are valid, but do not cause a transition
 to the Committed state. Thus, in the Uncommitted state, a channel
 remains in the same configuration as the last time that you commit a
 session.

#### Committed

Call NI-DCPower Commit With Channels to verify all
 properties, apply a select group of settings to channels, and
 transition to the Committed state.

NI-DCPower applies the following properties upon entering the Committed
 state.

- Aperture Time
- Aperture Time Units
- Auto Zero
- Current Compensation Frequency
- Current Gain Bandwidth
- Current Pole Zero Ratio
- Measure When
- Measure Record Length
- Measure Record Length Is Finite
- Merged Channels
- Output Capacitance
- Output Connected
- Output Resistance
- Power Line Frequency
- Power Source
- Pulse Bias Current Level
- Pulse Bias Current Limit
- Pulse Bias Current Limit High
- Pulse Bias Current Limit Low
- Pulse Bias Voltage Level
- Pulse Bias Voltage Limit
- Pulse Bias Voltage Limit High
- Pulse Bias Voltage Limit Low
- Reset Average Before Measurement
- Samples to Average
- Sense
- Sequence Loop Count Is Finite
- Sequence Loop Count
- Source Delay
- Source Mode
- Transient Response
- Voltage Compensation Frequency
- Voltage Gain Bandwidth
- Voltage Pole Zero Ratio
- All trigger-, event-, and routing-related properties

Note

If you configure a property on a channel multiple times, NI-DCPower
 applies only the most recent configuration upon entering the
 Committed state. If you modify any properties in the Committed
 state, the channel implicitly transitions back to the Uncommitted
 state, and the channel configuration continues to reflect the
 previously committed properties.

Call NI-DCPower Initiate With Channels from the
 Committed state to transition to the Running state.

#### Running

To place channels in the Running state, call NI-DCPower Initiate
 With Channels. In the Running state, a channel
 begins output signal generation and can acquire measurements.

Note

Initialize with Independent
 Channels

Initiate With Channels

In the Running state, the channel configuration determines the behavior
 of the channel. For example, a channel can either configure a single
 output point or step through a sequence of points. Additionally, a
 channel can be configured to wait for triggers before performing an
 operation.

While running in Single Point source mode some properties and attributes
 can be dynamically reconfigured. Properties and
 attributes reconfigured dynamically (in the Running state) are
 immediately applied.

Note

In the Running state, there are several functions that you can use to
 take measurements, fetch buffered measurements, query the output
 state, or query the device state. You can call the only the
 following functions in the Running state.

- NI-DCPower Measure
- NI-DCPower Measure Multiple
- NI-DCPower Fetch Multiple
- NI-DCPower Send Software Edge Trigger With
 Channels
- NI-DCPower Query In Compliance
- NI-DCPower Query Output State
- NI-DCPower Wait For Event With Channels

Tip

Abort With Channels

#### Differences Between
 Sessions Created With Independent Channels and Deprecated Initialize
 Functions

The NI-DCPower Initialize With Independent Channels
 function replaces all prior NI-DCPower Initialize
 functions. NI recommends using Initialize With Independent
 Channels for new programs. Initializing with
 independent channels allows you to configure multiple channels of
 the same instrument, or of multiple instruments, independently of
 one another.

Sessions initialized with independent channels have fewer limitations
 than sessions initialized with other initialize functions.

| Feature | Behavior in Session Initialized With |  |
| --- | --- | --- |
| Initialize With Independent Channels | Any Other NI-DCPower Initialize Function |  |
| Triggers and events | Configurable per channel | Not available in sessions that include multiple channels |
| Measure When property | Configurable per channel | Must be set to On Demand if a session includes multiple channels |
| Measure records | Available in sessions that include multiple channels | Not available in sessions that include multiple channels |
| Sequence source mode | Configurable per channel | Not available in sessions that include multiple channels |

Note

Initialize With Independent Channels

#### Fully Qualified
 Channel Names and Initialize With Independent Channels

NI-DCPower Initialize With Independent Channels allows
 you to include channels from multiple physical instruments and
 configure them independently of one another. If the session spans
 multiple physical instruments, you must use a *fully qualified
 channel name* or a *fully qualified channel
 range* to unambiguously identify and configure the
 channels.

Fully qualified channel name

PXI1Slot3/0

Fully qualified channel range

PXI1Slot3/0-23

PXI1Slot3/0:23

Note

0-23

0:23

Parent topic:

Programming with NI-DCPower

Related concepts:

- Single Point Source Mode
- Dynamic Reconfiguration
- NI-DCPower Sequence Source Mode
- Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower path=programming-with-ni-dcpower.html language=enus -->
## TOPIC 00016: Programming with NI-DCPower

- bundle_id: `ni-dcpower`
- source_path: `programming-with-ni-dcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/programming-with-ni-dcpower.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DCPower, an Interchangeable Virtual Instrument (IVI)–compliant instrument driver, is included with your NI instrument and communicates with all NI programmable instruments. NI-DCPower features a set of operations and properties that exercise the functionality of the instrument.

### Programming with NI-DCPower

NI-DCPower, an Interchangeable Virtual Instrument (IVI)–compliant instrument driver, is
 included with your NI instrument and communicates with all NI programmable instruments.
 NI-DCPower features a set of operations and properties that exercise the functionality of the
 instrument.

- [Programming Flow](programming-flow.html#GUID-442C29BE-4498-4559-AD30-0CEE715F3876)
- [Using Properties and Attributes](using-properties-and-attributes.html) NI-DCPower contains high-level VIs and functions that set most of the properties and attributes in the NI-DCPower API.
- [Setting Properties and Attributes Before Reading Them](setting-properties-and-attributes-before-read.html)
- [Programming States](programming-states.html)
- [Single Point Source Mode](single-point-source-mode.html)
- [NI-DCPower Sequence Source Mode](sequence-source-mode.html) Learn what a sequence is, when to use it, and how NI-DCPower maps channels, terminals, and events in Sequence Source Mode.
- [Advanced Sequencing](advanced-sequencing.html) Use advanced sequencing instead of the NI-DCPower Set Sequence function when you want more options for configuring a channel differently between sequence steps.
- [Constant Resistance and Constant Power](constant-power-resistance-dcpower.html) NI-DCPower electronic loads support sinking at both a constant configured resistance and a constant configured power.
- [Pulsing](pulsing.html) The source unit can output configurable voltage pulses or current pulses.
- [Detecting Internal/Auxiliary Power](detecting-internalauxiliary-power.html) Use an auxiliary power source to enable the full-power capabilities of NI instruments that support this feature. NI-DCPower can dynamically query whether the auxiliary power is connected to the device.
- [Simulating an Instrument](simulating-an-instrument.html) Simulate an instrument using NI-DCPower or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware.
- [NI-DCPower Import/Export Attribute Configuration Mapping Behavior](importexport-attribute-configuration-mapping-.html) Learn how to map import/export configurations between NI-DCPower sessions, ensure correct channel mapping, and handle errors for seamless integration across different channels.

Related information:

- NI-DCPower LabVIEW Reference
- NI-DCPower C Function Reference
- NI-DCPower C# .NET Reference
- NI-DCPower Python Reference

<!--NI_TOPIC bundle=ni-dcpower path=pulsing.html language=enus -->
## TOPIC 00017: Pulsing

- bundle_id: `ni-dcpower`
- source_path: `pulsing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/pulsing.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: The source unit can output configurable voltage pulses or current pulses. Pulsing in Single Point Source Mode In Single Point source mode, the source unit generates a single pulse, then returns to the pulse bias level. 4 Single Pulse Cycle Graph showing pulse cycle with on time, off time, and bias l

### Pulsing

The source unit can output configurable voltage pulses or current pulses.

#### Pulsing in Single Point Source
 Mode

In Single Point source mode, the source unit generates a single pulse, then returns
 to the pulse bias level.

Figure 4.

[IMAGE alt='Graph showing pulse cycle with on time, off time, and bias level.' src='GUID-0E5BDB03-2B48-44A2-A592-79CEBB5E4605-a5.gif']

The following steps illustrate the typical operation of the source unit for
 each pulse when you initiate a pulse output function.

1. To enable pulsing, set NI-DCPower Output Function to
 Pulse Voltage or Pulse
 Current .
2. (Optional) In Sequence source mode, if this step is not the first step in a
 sequence, the source unit emits a Ready For Pulse Trigger event. Then, the
 source waits for a Pulse Trigger.
3. After receiving the Pulse Trigger, the source unit applies the pulse level
 configuration. In Sequence source mode, the pulse level is the next pulse level
 in the array.
4. After waiting the time specified by the source delay, the source unit generates
 a Source Complete event. If you set the source delay for each step in Sequence
 source mode, this time is the subsequent source delay in the array.
5. (Optional) To configure the measure unit to take a measurement and store it in a
 buffer on the device, set NI-DCPower Measure When to
 Automatically After Source Complete .
6. Once the pulse on time elapses, the source unit applies the pulse bias
 configuration.
7. After waiting the pulse bias delay, the source unit emits a Pulse Complete
 event.
8. The source unit waits the remainder of the pulse off time.
9. At commit, the bias settings are applied to the output.

#### Pulsing in Sequence Source
 Mode

In Sequence source mode, the source unit uses a list of pulse levels one after
 another, while maintaining the specified duty cycle. It does this by applying the
 defined Pulse On and Pulse Off times..
 The following figure illustrates a sequence consisting of two pulses. The sequence
 is repeated twice.

Figure 5.

[IMAGE alt='Graph showing a sequence of two pulses with triggers and delays.' src='GUID-8BC4529C-A06F-4268-ADEF-ED5BE1CBF92A-a5.gif']

Note

pulse on

pulse off
 time

pulse bias delay

#### Pulsing in an Advanced
 Sequence

Pulsing in an advanced sequence differs from pulsing in sequence source mode. The
 diference is because you can reconfigure all pulse-related properties per step in an
 advanced sequence.

#### Pulse Source Model

| Pulse Voltage | Pulse Current |
| --- | --- |
| Pulse Voltage Level | Pulse Current Level |
| Pulse Bias Voltage Level | Pulse Bias Current Level |
| Pulse Voltage Level Range | Pulse Current Level Range |
| Pulse Current Limit1 | Pulse Voltage Limit1 |
| Pulse Current Limit High2 | Pulse Voltage Limit High2 |
| Pulse Current Limit Low2 | Pulse Voltage Limit Low2 |
| Pulse Bias Current Limit1 | Pulse Bias Voltage Limit1 |
| Pulse Bias Current Limit High2 | Pulse Bias Voltage Limit High2 |
| Pulse Bias Current Limit Low2 | Pulse Bias Voltage Limit Low2 |
| Pulse Current Limit Range | Pulse Voltage Limit Range |

<sup>1</sup>Applied when NI-DCPower Compliance Limit
 Symmetry is
 Symmetric.

<sup>2</sup>Applied when NI-DCPower
 Compliance Limit Symmetry is
 Asymmetric.

- Source Delay
- Pulse Bias Delay
- Pulse On Time
- Pulse Off Time

#### Support for Pulsing

The following devices do not support pulsing.

- PXI-4110
- PXIe-4112/4113
- PXI-4130
- PXI-4132
- PXIe-4140/4141/4142/4143/4144/4145
- PXIe-4154
- PXIe-4162/4163

Parent topic:

Programming with NI-DCPower

Related concepts:

- NI-DCPower Sequence Source Mode
- Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower path=search-examples-ni-example-finder.html language=enus -->
## TOPIC 00018: Browsing and Searching for Examples in NI Example Finder

- bundle_id: `ni-dcpower`
- source_path: `search-examples-ni-example-finder.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/search-examples-ni-example-finder.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `task`
- source_description: Use NI Example Finder to browse and to search for examples. You can use NI Example Finder to find examples for the following products. LabVIEW LabWindows/CVI NI drivers accessible from LabVIEW NI drivers accessible from LabWindows/CVI Launch LabVIEW or LabWindows/CVI. Open NI Example Finder. LabVIEW

### Browsing and Searching for Examples in NI
 Example Finder

Use NI Example Finder to browse and to search for examples.

- LabVIEW
- LabWindows/CVI
- NI drivers accessible from LabVIEW
- NI drivers accessible from LabWindows/CVI

1. Launch LabVIEW or LabWindows/CVI.
2. Open NI Example Finder. 
 OptionDescriptionLabVIEW
 Select Help»Find Examples. from the menu bar.LabWindows/CVI
 Click Find Examples... from the
 Examples section of the Welcome
 Page. 
 NI Example Finder launches.
3. Optional: 
 Configure NI Example Finder for LabWindows/CVI. 
 
 NI Example Finder updates with all the examples for
 LabWindows/CVI.
  1. Click Setup. Configure Example
 Finder opens.
  2. In Configure Example Finder, click
 Software, then select LabWindows/CVI, and
 click OK.
4. Search the example VIs for your product. 
 OptionDescriptionClick the Browse tab.
 Choose Browse when you want to drill down
 through folders to find examples organized by task category.Tip Examples
 installed with NI drivers or third-party drivers are often found
 within the Hardware Input and Output folder.
 Examples installed with toolkits or modules are often found within
 the Toolkits and Modules
 folder.Click the Search tab.
 Choose Search when you want to find examples
 by searching for topics, products, or modules relevant to your
 application.
5. To open an example, double-click the folder or the example. 
 Tip You can modify
 an example VI to fit your application. You can also copy and paste from one
 or more examples into a VI that you create.

<!--NI_TOPIC bundle=ni-dcpower path=sequence-source-mode.html language=enus -->
## TOPIC 00019: NI-DCPower Sequence Source Mode

- bundle_id: `ni-dcpower`
- source_path: `sequence-source-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/sequence-source-mode.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn what a sequence is, when to use it, and how NI-DCPower maps channels, terminals, and events in Sequence Source Mode. What a Sequence is A sequence is a series of steps that apply voltage or current values on a NI-DCPower channel. In a simple sequence, each step sets a voltage or current level.

### NI-DCPower Sequence Source Mode

Learn what a sequence is, when to use it, and how NI-DCPower maps channels, terminals, and events in Sequence Source
 Mode.

#### What a Sequence is

A *sequence* is a series of steps that apply voltage or current values on a NI-DCPower channel. In a *simple
 sequence*, each step sets a voltage or current level. *Advanced
 sequencing* lets you configure multiple properties per step.

To customize per-step properties, see *Advanced Sequencing*.

#### Deterministic Operation

During a sequence, the channel steps through a predefined set of NI-DCPower configurations without any
 interaction with the host system or NI-DCPower.

Because the host system does not execute the NI-DCPower sequence changes, the transitions from one step in the sequence to
 the next are deterministic.

#### Support for Sequence Source Mode

- The following instruments do not support Sequence Source Mode on any channel:
  - PXI-4110
  - PXI-4130
- The system does not support using the NI-DCPower 
 Set Sequence and Advanced Sequence functions for the
 same channel in the same session.

Parent topic:

Programming with NI-DCPower

Related concepts:

- Advanced Sequencing
- Single Point Source Mode
- Pulsing

Related tasks:

- NI-DCPower Typical Sequence Operation

<!--NI_TOPIC bundle=ni-dcpower path=setting-properties-and-attributes-before-read.html language=enus -->
## TOPIC 00020: Setting Properties and Attributes Before Reading Them

- bundle_id: `ni-dcpower`
- source_path: `setting-properties-and-attributes-before-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/setting-properties-and-attributes-before-read.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Properties and attributes are modified when you set them or when you call a configuration VI or function that sets them, respectively. It is important to set the properties or attributes or call any configuration VIs or functions before reading back any property or attribute values for the following

### Setting Properties and Attributes Before Reading Them

Properties and attributes are modified when you set them or when you call a configuration
 VI or function that sets them, respectively. It is important to set the properties or
 attributes or call any configuration VIs or functions before reading back any property
 or attribute values for the following reasons:

- Values read are coerced depending on the current configuration of the session. If
 you read a property or attribute value and then set other properties or attributes,
 the value read may no longer be valid.
- The driver verifies that the configuration of the session is valid at the time the
 property or attribute is read. It is possible to get an error when reading a
 property or attribute if the configuration is not valid at that point, even when a
 setting later could make it valid.
- Reading properties or attributes causes the driver to verify the current
 configuration. If you change some of the settings later, those settings need to be
 validated again.

Parent topic:

Programming with NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower path=simulating-an-instrument-with-dcpower.html language=enus -->
## TOPIC 00021: Simulating an Instrument with NI-DCPower

- bundle_id: `ni-dcpower`
- source_path: `simulating-an-instrument-with-dcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/simulating-an-instrument-with-dcpower.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create and configure a simulated instrument using NI-DCPower. Run NI-DCPower Initialize With Independent Channels. Regardless of whether you want to simulate a single-instrument or multi-instrument session, set both the resource name and option string parameters. The

### Simulating an Instrument with
 NI-DCPower

Complete the following steps to create and
 configure a simulated instrument using NI-DCPower.

1. Run NI-DCPower Initialize With Independent Channels.
2. Regardless of whether you want to simulate a single-instrument or
 multi-instrument session, set both the resource name and
 option string parameters. The option
 string parameter is composed of the Simulate and
 Driver Setup keywords, as illustrated in the following
 example. 
 For a single-instrument session, use the following: 
 ParameterSyntaxresource name
 For single-instrument sessions:<resource
 name>For multi-instrument
 sessions:<resource name 1>,
 <resource name 2>Where
 resource name is either an instrument name
 (PXI1Slot2), a fully qualified channel name
 (PXI1Slot2/0), or a fully qualified channel
 range (PXI1Slot2/0-3).option string
 For single-instrument
 sessions:Simulate=1,DriverSetup=Model:<model
 number>;BoardType:<bus
 connector>For multi-instrument
 sessions:Simulate=1,DriverSetup=ResourceName:<resource
 name 1>;Model:<model
 number>;BoardType:<bus
 connector>&ResourceName:<resource name
 2>;Model:<model
 number>;BoardType:<bus
 connector> 
 Note The
 ResourceName entry of the option string may contain a
 single instrument names only (PXI1Slot2) and may contain
 only a single instrument name per ResourceName entry.

#### Simulation Examples

To simulate a single PXI-4110, use the following option string
 syntax: Simulate=1,DriverSetup=Model:4110;BoardType:PXI

You can also simulate a subset of channels for a single instrument using the
 resource name parameter of the Initialize With
 Independent Channels VI.

To simulate a multi-instrument session with a PXI-4110 and PXIe-4163, use the
 following syntax:

- resource name :
 PXI1Slot2/0-2,PXI1Slot3/0-23
- option string :
 Simulate=1,DriverSetup=ResourceName:PXI1Slot2;Model:4110;BoardType:PXI&ResourceName:PXI1Slot3;Model:4163;BoardType:PXIe

To simulate a multi-instrument session with these instruments that includes only a
 subset of their channels, use the following syntax:

- resource name :
 PXI1Slot2/0,PXI1Slot3/0,PXI1Slot3/2,PXI1Slot3/4,PXI1Slot3/6,PXI1Slot3/8,PXI1Slot3/12
- option string :
 Simulate=1,DriverSetup=ResourceName:PXI1Slot2;Model:4110;BoardType:PXI&ResourceName:PXI1Slot3;Model:4163;BoardType:PXIe

Only those channels that you explicitly include are simulated.

Parent topic:

Simulating an Instrument

<!--NI_TOPIC bundle=ni-dcpower path=simulating-an-instrument-with-max.html language=enus -->
## TOPIC 00022: Simulating an Instrument with MAX

- bundle_id: `ni-dcpower`
- source_path: `simulating-an-instrument-with-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/simulating-an-instrument-with-max.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create and to configure a simulated power supply in Measurement & Automation Explorer (MAX). Launch MAX. Right-click Devices and Interfaces in the MAX configuration tree, and select Create New.... Select Simulated NI-DAQmx Device or Modular Instrument, then click Fini

### Simulating an Instrument with MAX

Complete the following steps to create and
 to configure a simulated power supply in Measurement & Automation Explorer
 (MAX).

1. Launch MAX.
2. Right-click Devices and Interfaces in the MAX
 configuration tree, and select Create New....
3. Select Simulated NI-DAQmx Device or Modular Instrument,
 then click Finish.
4. In the Create Simulated NI-DAQmx Device window, expand
 Power Supplies.
5. Select the power supply to simulate, then click
 OK.

The power supply appears in the MAX configuration tree with
 a yellow icon indicating that the device is simulated.

Parent topic:

Simulating an Instrument

<!--NI_TOPIC bundle=ni-dcpower path=simulating-an-instrument.html language=enus -->
## TOPIC 00023: Simulating an Instrument

- bundle_id: `ni-dcpower`
- source_path: `simulating-an-instrument.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/simulating-an-instrument.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: Simulate an instrument using NI-DCPower or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated instrument to evaluate an

### Simulating an Instrument

Simulate an instrument using NI-DCPower or Measurement & Automation Explorer (MAX)
 to develop, modify, and/or test an application without hardware.

Using a simulated device to test an application eliminates the risk of hardware damage.
 Additionally, you can use a simulated instrument to evaluate an NI product for which you do
 not have hardware.

Tip

Parent topic:

Programming with NI-DCPower

Related concepts:

- Using InstrumentStudio with Your NI-DCPower Instrument

<!--NI_TOPIC bundle=ni-dcpower path=single-point-source-mode.html language=enus -->
## TOPIC 00024: Single Point Source Mode

- bundle_id: `ni-dcpower`
- source_path: `single-point-source-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/single-point-source-mode.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Single Point source mode, the source unit applies a single source configuration when it enters the Running state. You can then update the source configuration dynamically. Single Point Source Model The following steps illustrate the typical operation of the source unit when you initiate in Single

### Single Point Source Mode

In Single Point source mode, the source unit applies a single source configuration when it
 enters the Running state. You can then update the source configuration dynamically.

#### Single Point Source Model

The following steps illustrate the typical operation of the source unit when you initiate
 in Single Point source mode:

1. (Optional) The source unit waits for a Source trigger.
2. The source unit updates the source configuration.
3. After waiting the time specified by the NI-DCPower Source Delay property, the
 source unit generates a Source Complete Event, as
 illustrated in the following figure.
4. (Optional) If the NI-DCPower Measure When property is set to
 Automatically After Source
 Complete , the measure unit takes a
 measurement after the Source Complete event generates.

Note

None

Note

Parent topic:

Programming with NI-DCPower

Related concepts:

- Programming States
- Dynamic Reconfiguration
- NI-DCPower Sequence Source Mode

<!--NI_TOPIC bundle=ni-dcpower path=typical-sequence-operation.html language=enus -->
## TOPIC 00025: NI-DCPower Typical Sequence Operation

- bundle_id: `ni-dcpower`
- source_path: `typical-sequence-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/typical-sequence-operation.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a sequence with deterministic steps that can execute in parallel. Configure triggers and looping. Run the sequence and verify measurement behavior. Ensure that the session and the channels are initialized before executing a sequence operation. To run a typical sequence operation, complete

### NI-DCPower Typical Sequence Operation

Configure a sequence with deterministic steps that can execute in parallel. Configure
 triggers and looping. Run the sequence and verify measurement behavior.

Ensure that the session and the channels are
 initialized before executing a sequence operation.

To run a typical sequence operation,
 complete the following steps.

1. Start the sequence by completing one of the following actions. 
 ActionDescriptionInclude a Commit step (Advanced Sequencing only)
 When using Advanced Sequencing, include a Commit step if the channel
 is Uncommitted and the sequence includes a Commit step.
 Commit steps run before the normal sequence steps. A Commit step does
 the following:Applies its configured voltage or current.
 Waits for the source delay.
 Does not generate a Source Complete
 event.Skip Commit
 Proceed without a Commit step when the channel is already committed
 or the sequence does not include a Commit step. 
 The source unit waits for a Start Trigger to begin the
 sequence. During the first iteration, the source unit does not wait for a
 Source Trigger or a Sequence Advance
 Trigger.
2. Monitor the execution of the sequence. 
 For each step in the sequence, the system performs the following actions in
 order:Wait for a Source TriggerFor all steps except the
 first step, the source unit waits for a Source
 Trigger when Source Triggering is
 enabled. The source unit skips this wait only when both of the
 following conditions are met:Source Triggering is disabled.
 The system is executing the first step.
 Apply source and delayThe source unit applies the voltage or current
 specified for the step. The source unit then waits for the
 configured source delay.
 Generate Source CompleteAfter the source delay
 expires, the source unit generates a Source
 Complete event.
 Acquire a measurementWhen Measure When is set to
 Automatically After Source Complete, the
 measure unit acquires a measurement and stores it in the instrument
 buffer. When Measure When is set to a different
 value, the measure unit operates independently. The system takes no
 measurement as part of the step execution.These actions repeat for every step in the sequence.
3. Wait for the system to complete the iteration. 
 After the system completes the final step in the sequence, it generates a
 Sequence Iteration Complete event.
4. Control looping by completing one of the following actions. 
 ActionDescriptionLoop the sequence
 Continue running the sequence for additional iterations. On
 subsequent iterations, the device waits for a Sequence Advance
 Trigger when enabled. The device proceeds without waiting
 for a Start Trigger.Stop after one iteration
 End the sequence after a single pass through the steps.
5. Finish the sequence by completing one of the following actions. 
 ActionDescriptionSet Sequence Loop Count Is Finite to
 True
 Stop the sequence automatically after completing the number of
 iterations defined by Sequence Loop Count. After the
 final iteration, the system generates a Sequence Engine
 Done event.Set Sequence Loop Count Is Finite to
 False
 Run the sequence without a predefined end point. Stop the sequence
 manually by calling Abort With Channels or by closing
 the session.

| Symptom | What to check |
| --- | --- |
| Sequence does not start | Verify Start Trigger routing and enablement. |
| Unexpected waits between steps | Review Source Trigger configuration for steps after the first step. |
| No measurements recorded | Confirm the Measure When setting and verify buffer availability. |

#### Measuring After Source
 Complete

Figure 2.

- Measure When is set to Automatically After Source
 Complete .
- The source unit is not pulsing.

Figure 2.

NI-DCPower

[IMAGE alt='Flowchart showing a nested sequence with an outer loop for sequence iterations and an inner loop for steps. The diagram uses numbered callouts to indicate the execution order. Each step waits for a Source Trigger, applies source output, waits for a source delay, generates a Source Complete event, then performs a measurement before advancing to the next step. After all steps complete, the sequence generates a Sequence Iteration Complete event and, after the final iteration, a Sequence Engine Done event. A note indicates that triggers are not waited for during the first iteration.' src='GUID-B4B7641F-89F2-4BA2-ABEE-0D440FB286C2-a5.gif']

#### Measuring Independently of
 Source Complete

Figure 3.

- Measure When is not set to Automatically After
 Source Complete .
- The source unit is not pulsing.

Figure 3.

NI-DCPower

[IMAGE alt='Flowchart showing the same nested sequence and step structure, with numbered callouts indicating execution order. Each step applies source output, waits for a source delay, and generates a Source Complete event before advancing to the next step. Measurement is not shown as part of the step flow and is independent of the Source Complete event. After all steps complete, the sequence generates a Sequence Iteration Complete event and, after the final iteration, a Sequence Engine Done event. A note indicates that triggers are not waited for during the first iteration.' src='GUID-0806F3EA-D0B2-4F28-957D-FF27931AF435-a5.gif']

Parent topic:

NI-DCPower Sequence Source Mode

<!--NI_TOPIC bundle=ni-dcpower path=user-manual-welcome.html language=enus -->
## TOPIC 00026: NI-DCPower User Manual

- bundle_id: `ni-dcpower`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-DCPower User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-DCPower
 User Manual

The NI-DCPower User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-DCPower
- License Setup and Activation
- NI-DCPower Release Notes
- NI-DCPower LabVIEW Reference
- NI-DCPower C Function Reference
- NI-DCPower C# .NET Reference
- NI-DCPower Python Reference

<!--NI_TOPIC bundle=ni-dcpower path=using-properties-and-attributes.html language=enus -->
## TOPIC 00027: Using Properties and Attributes

- bundle_id: `ni-dcpower`
- source_path: `using-properties-and-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower/raw/resource/enus/using-properties-and-attributes.html
- document_id: `ni-dcpower`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-DCPower contains high-level VIs and functions that set most of the properties and attributes in the NI-DCPower API. Some properties and attributes are not accessible through the high-level VIs and functions. You must set the values for these properties and attributes using the appropriate propert

### Using Properties and Attributes

NI-DCPower contains high-level VIs and functions that set most of the properties
 and attributes in the NI-DCPower API.

Some properties and attributes are not accessible through the high-level VIs and functions. You
 must set the values for these properties and attributes using the
 appropriate property or attribute.

#### Accessing Properties in LabVIEW

In LabVIEW, properties are accessed through the NI-DCPower property node. To
 access properties in LabVIEW, complete the following steps:

1. Open a VI.
2. In the block diagram view, navigate to the NI-DCPower palette.
3. Add the property node icon to the block diagram.
4. Left-click the property node, and select the property that you want to use.
5. To add additional properties, resize the property node. To resize the property node,
 drag the resizing handle at the top or bottom of the node and release the mouse
 button.

#### When to Use an Active Channel

The Active Channel property defines the channels that channel-based properties
 apply to. The Active Channel is listed first in
 the property node.

You must pass an Active Channel in any of the following cases:

- For multichannel sessions, if you want to configure the channels differently from one
 another.
- For multichannel sessions, when reading a property where multiple channels may have different
 values for that property.
- For multichannel sessions where the channels span multiple physical instruments, if you are
 reading any instrument-based properties; in this case, pass
 the instrument name to Active Channel 
 rather than a channel name.

You do not need to pass an Active Channel, or can pass an empty string, in any
 of the following cases:

- If the properties you are using are neither channel-based nor instrument-based
- If your session includes only one channel
- If you want to configure all channels in a multichannel session identically
- If you want to read a property from all channels when all channels have the same
 property value or from an instrument-based property

#### Accessing Attributes

In C and Visual Basic 6.0, access the attributes with the Get Attribute and
 Set Attribute functions. The
 Get and Set Attribute
 functions exist for each supported data type in NI-DCPower.

Parent topic:

Programming with NI-DCPower
