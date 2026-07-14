# NI DOCUMENT BUNDLE: ecu-test-system-maintenance-software

<!--NI_BUNDLE_CHUNK bundle=ecu-test-system-maintenance-software start=1 end=16 -->
<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=check-continuity.html language=enus -->
## TOPIC 00001: Check Continuity

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `check-continuity.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/check-continuity.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Check Continuity operation ensures all components that shipped with the test system are correctly routed to their assigned pins in the mass interconnect. When running this operation, Test System Maintenance Software prompts you to connect an FDT.

Check Continuity

The Check Continuity operation ensures all components that
 shipped with the test system are correctly routed to their assigned pins in the mass
 interconnect. When running this operation, Test System Maintenance Software prompts you to
 connect an FDT.

Parent topic:

Maintenance Operations

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=com-port-binding.html language=enus -->
## TOPIC 00002: COM Port Binding

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `com-port-binding.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/com-port-binding.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure COM port bindings to be consistent with your system design. Test System Maintenance Software detects errors in your system configuration, including incorrect COM port binding assignments. The Verify System Configuration operation checks whether your COM port bindings match your system conf

COM Port Binding

Configure COM port bindings to be consistent with your system design.

Test System Maintenance Software detects errors in your system configuration,
 including incorrect COM port binding assignments. The [Verify System
 Configuration operation](verify-components.html) checks whether your COM port bindings match your
 system configuration file.

generated report

Ports with Problems

```text
The serial port binding, COM{#}, does not match the serial port binding from the system definition, COM{#}.
Automatic adjustment of serial port bindings is not supported. 
See the help file for details on how to manually modify serial port bindings.
```

- PXI
 Controller COM Port Binding
- NI Serial
 Module COM Port Bindings

Note

Parent topic:

Reports

Related concepts:

- Verify Components

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=config-switch-term-blocks-topos.html language=enus -->
## TOPIC 00003: Configuring Switch Terminal Blocks and Topologies

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `config-switch-term-blocks-topos.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/config-switch-term-blocks-topos.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `task`
- source_description: Switch terminal blocks delivered with NI systems are configured to associate with the switch modules specified in the system design. Some NI switch terminal blocks used with NI PXI switches cannot be detected by software. For example, the TB-2640B switch terminal block used with the PXIe-2532B switc

Configuring Switch Terminal Blocks and
 Topologies

Switch terminal blocks delivered with NI systems are configured to associate with
 the switch modules specified in the system design. Some NI switch terminal blocks used
 with NI PXI switches cannot be detected by software. For example, the TB-2640B switch
 terminal block used with the PXIe-2532B switch module cannot be detected by software.
 Test System Maintenance Software may not operate correctly if you alter the
 configurations of these undetectable switch terminal blocks in NI MAX. Enabling
 Configuring Switch Terminal Blocks and Topologies ensures
 that the configuration of these switch terminal blocks matches the original system
 design.

Note

- TB-2640B
- TB-2641B
- TB-2642B
- TB-2643B
- TB-2644B
- TB-2645B
- TB-2646B

Note

When you enable the Configuring Switch Terminal Blocks and
 Topologies setting, Test System Maintenance Software restores the
 switch terminal block to the configuration originally specified in the system design
 in NI MAX. To enable this setting, complete the following steps.

1. Go to the Settings page in Test System Maintenance
 Software and click the Configuring Switch Terminal Blocks and
 Topologies checkbox.
2. Run the Verify Components operation to verify that Test
 System Maintenance Software detects the terminal switch block.

Note

Verify Components

Parent topic:

Test System Maintenance Software Manual

Related concepts:

- Verify Components

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=environment-reference.html language=enus -->
## TOPIC 00004: Environment Reference

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `environment-reference.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/environment-reference.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `reference`
- source_description: Test System Maintenance Software UI consists of a single window containing a File menu, Help menu, Home page, Report page, and Settings page. File Menu The File menu contains the following options: Open Report Folder...—Opens a directory of previously generated reports. Exit—Exits the Test System Ma

Environment Reference

Test System Maintenance Software UI consists of a single window containing a File menu,
 Help menu, Home page, Report page, and Settings page.

#### File Menu

The File menu
 contains the following options:

- Open Report Folder... —Opens a directory of previously generated
 reports.
- Exit —Exits the Test System Maintenance Software.

#### Help
 Menu

The Help menu contains the following options:

- Test System Maintenance Help... —Launches the Test System
 Maintenance Software Help.

#### Home

The Home page contains the following information:

- Recent Maintenance History — A list of links to the most
 recent reports created.
- System Information — Details about your system.
- Run Maintenance — Configure your system maintenance operations.
  - Maintenance Operations — Click the Gear button to
 select which maintenance operations you want to perform on your test
 system.
  - Run Operations — Click to run the selected
 operations.
  - Component List — Click the top box to run maintenance operations on all
 components or select individual components from the list.

#### Reports

The Reports page contains the overall result of operations
 run on your test system, as well as information on system configuration, system
 components, and detailed information about each operation run.

#### Settings

The Settings page contains information about Test System Maintenance Software. You can also
 use this page to configure settings like the number of reports stored, naming of test system
 components, and configurations of switch terminal block components.

Parent topic:

Test System Maintenance Software Manual

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=get-cal-temp-info.html language=enus -->
## TOPIC 00005: Get Calibration and Temperature Information

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `get-cal-temp-info.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/get-cal-temp-info.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Get Calibration and Temperature Information operation returns the following information for each test system component: This operation is not supported on all devices. Some devices may not support all the information listed below. For example, PXI controllers can report current temperature, but

Get Calibration and Temperature
 Information

The Get Calibration and Temperature Information operation
 returns the following information for each test system component:

Note

External Calibration Date

External Calibration Temperatures

Recommended External Calibration Interval

Self-Calibration Date and Time

Self-Calibration Temperatures

Current Temperatures

A blank entry in the table indicates that the component does not provide that data.

Parent topic:

Maintenance Operations

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=maintenance-ops.html language=enus -->
## TOPIC 00006: Maintenance Operations

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `maintenance-ops.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/maintenance-ops.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the operations you want the Test System Maintenance Software to run by clicking the Gear button () in the Home page and checking the boxes of the operations you want to perform. You cannot change the settings in the Run Configurations panel while executing operations. Some operations require

Maintenance Operations

Select the operations you want the Test System Maintenance Software to run by
 clicking theGearbutton ([IMAGE alt='1378' src='GUID-DEB02933-5F50-482E-B278-895A233BA642-a5.png']) in the
 **Home** page and checking the boxes of the operations you want to
 perform.

Note

Run Configurations

Verify
 System Configuration

Parent topic:

Test System Maintenance Software Manual

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=manual-overview.html language=enus -->
## TOPIC 00007: Test System Maintenance Software Manual

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/manual-overview.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Test System Maintenance Software Manual contains reference information about monitoring and performing maintenance operations on components of your test system. Top Tasks What do you want to do? Where to go Configure maintenance operations to perform on selected components within your test syste

Test System Maintenance Software
 Manual

The Test System Maintenance Software Manual contains reference information about
 monitoring and performing maintenance operations on components of your test system.

#### Top Tasks

| What do you want to do? | Where to go |
| --- | --- |
| Configure maintenance operations to perform on selected components within your test system or view recent maintenance history and system information. | Go to the application Home page. |
| View a detailed report with the results of maintenance operations performed on your test system. | Go to the application Reports page. |
| Configure Test System Maintenance Software settings. | Go to the application Settings page. |

#### Important Concepts

| What do you want to learn? | Where to go |
| --- | --- |
| How to perform maintenance operations on selected components within your test system. | Maintenance Operations |
| How to find test system components or ports that are not appearing or behaving as expected in Test System Maintenance Software. | Verify Components |
| How to generate a detailed report with the results of maintenance operations performed on your test system. | Reports |
| How to rename system components to match the names originally specified in the test system configuration file. | Renaming Components |
| How to configure switch terminal block components to match the configurations originally specified in the test system configuration file. | Configuring Switch Terminal Blocks and Topologies |
| How to navigate Test System Maintenance Software and change application settings. | Environment Reference |

© 2020–2022 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=pxi-com-port-binding.html language=enus -->
## TOPIC 00008: PXI Controller COM Port Binding

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `pxi-com-port-binding.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/pxi-com-port-binding.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure PXI Controller COM ports to be consistent with your system design if the System Verification operations reports a COM port number assignment error. Read the following instructions for information on how to correctly assign a PXI controller port number. Open Windows Device Manager. Select P

PXI Controller COM Port Binding

Configure PXI Controller COM ports to be consistent with your system design if the System
 Verification operations reports a COM port number assignment error. Read the following
 instructions for information on how to correctly assign a PXI controller port
 number.

1. Open Windows Device Manager.
2. Select Ports»Communications Port, and right-click to select Properties.
3. Click Advanced... and select a port binding from the
 COM Port Number drop-down list. 
 org.dita.html5/xsl/topic.xsl 455Note When swapping COM port number
 assignments between two ports, set one of them to an unused port number first to avoid
 setting two ports to the same port number.
 org.dita.html5/xsl/topic.xsl 455Note If you get an error when changing the
 COM port number, reboot the machine and try again.

After configuring new port bindings, close the Properties
 window, right-click the Communications Port in Windows Device
 Manager, and select Scan for Hardware changes to apply
 changes.

Devices and
 Interfaces

Note

Parent topic:

COM Port Binding

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=renaming-components.html language=enus -->
## TOPIC 00009: Renaming Components

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `renaming-components.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/renaming-components.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `task`
- source_description: Component names must match those present in your system configuration file. Test System Maintenance Software operations may not run properly if the names do not match. For example, if you reset the NI MAX database or manually change a resource name or alias from the default NI designated name, Test

Renaming Components

Component names must match those present in your system configuration file. Test
 System Maintenance Software operations may not run properly if the names do not match. For
 example, if you reset the NI MAX database or manually change a resource name or alias from the
 default NI designated name, Test System Maintenance Software may not recognize a component.
 The Renaming Components setting ensures test system component names
 match the names specified in the system configuration file. You must run the Verify
 Components operation after enabling this setting for the changes to take
 effect.

Renaming
 Components

1. Go to the Settings page in Test System Maintenance Software and
 click the Renaming Components checkbox.
2. Run the Verify Components operation to automatically rename and
 detect test system components.

Parent topic:

Test System Maintenance Software Manual

Related concepts:

- Verify Components

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=reports.html language=enus -->
## TOPIC 00010: Reports

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `reports.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/reports.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test System Maintenance Software generates a report containing information about the test system each time you run operations. The generated report displays information from the operations selected in the Home page. To view the most recent report, and a list of previous reports, go to the Report

Reports

The Test System Maintenance Software generates a report containing information
 about the test system each time you run operations.

Note

Note

The report contains the following information:

Overall Status

General Information

System Configuration Verification Summary

System Components — General Information

System Ports — General Information

System Components — Operations Performed

- Passed —The test for this component passed.
- Failed —The test for this component failed. Refer to the
 report footnote for additional details.
- N/A —The operation is not supported for this component.

System Components — Calibration Information and Current Temperatures

Parent topic:

Test System Maintenance Software Manual

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=reset.html language=enus -->
## TOPIC 00011: Reset

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `reset.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/reset.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Reset operation to reset test system components. The Reset operation initializes components to the power-on state. Resetting also clears the status of a component that exceeded a threshold such as temperature operating range. Before running the Reset operation, make sure no other operations

Reset

Use theReset operation to reset test system
 components.

Reset

Note

Reset

Note

Parent topic:

Maintenance Operations

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=self-calibrate.html language=enus -->
## TOPIC 00012: Self-Calibrate Components

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/self-calibrate.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Self-Calibrate Components operation performs self-calibration on test system instruments by verifying an instrument against an onboard standard and adjusting the performance of the instrument to compensate for any discrepancies. Typically, you perform self-calibration in the same environment in

Self-Calibrate Components

The Self-Calibrate Components operation performs
 self-calibration on test system instruments by verifying an instrument against an onboard
 standard and adjusting the performance of the instrument to compensate for any
 discrepancies.

Typically, you perform self-calibration in the same environment in which you use the
 instrument. By doing so, the self-calibration operation can compensate for factors such as
 ambient temperature and time drift.

Note

Self-Calibrate Components

Note

Parent topic:

Maintenance Operations

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=self-test.html language=enus -->
## TOPIC 00013: Self Test

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/self-test.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Self Test operation to verify baseline functionality of test system components. The level of verification varies by component, but minimally, this operation verifies that the system controller can communicate with the component. Before running the Self Test operation, make sure no other oper

Self Test

Use the Self Test operation to verify baseline functionality
 of test system components. The level of verification varies by component, but minimally, this
 operation verifies that the system controller can communicate with the component.

Self Test

Note

Parent topic:

Maintenance Operations

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=serial-com-port-binding.html language=enus -->
## TOPIC 00014: NI Serial Module COM Port Binding

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `serial-com-port-binding.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/serial-com-port-binding.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure NI Serial Module COM ports to be consistent with your system design if the System Verification operations reports a COM port number assignment error. Read the following instructions for information on how to correctly assign an NI serial module port number. Run the NI MAX application as an

NI Serial Module COM Port Binding

Configure NI Serial Module COM ports to be consistent with your system design if the
 System Verification operations reports a COM port number assignment error. Read the
 following instructions for information on how to correctly assign an NI serial module port
 number.

1. Run the NI MAX application as an administrator by right-clicking the
 application shortcut and selectingRun as Administrator.
 You must run the application as an administrator to enable COM port number
 changes.
2. Select the COM Port you want to update.
3. Click on the Advanced tab.
4. Change the COM port binding from the COM Port Numberdrop-down list. 
 org.dita.html5/xsl/topic.xsl 455Note When swapping COM port number assignments between two ports, set one of
 them to an unused port number first to avoid setting two ports to the same
 port number.
 org.dita.html5/xsl/topic.xsl 455Note If you get an error when changing the COM port number, reboot the machine
 and try again.

File

»

Save

Parent topic:

COM Port Binding

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=tb-topos.html language=enus -->
## TOPIC 00015: Terminal Block Topologies

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `tb-topos.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/tb-topos.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `reference`
- source_description: Some NI switch terminal blocks support both 1-wire and 2-wire topologies. Read the following to learn more about using switch terminal blocks with Test System Maintenance Software. Supported Topologies for NI Switch Terminal BlocksThe following table shows the supported topologies for NI switch term

Terminal Block Topologies

Some NI switch terminal blocks support both 1-wire and 2-wire topologies. Read the
 following to learn more about using switch terminal blocks with Test System Maintenance
 Software.

#### Supported
 Topologies for NI Switch Terminal Blocks

PXIe-2532B

Note

| Switch terminal block name | Supports 1-wire topology | Supports 2-wire topology |
| --- | --- | --- |
| TB-2640B | Yes | No |
| TB-2641B | Yes | No |
| TB-2642B | Yes | No |
| TB-2643B | Yes | Yes |
| TB-2644B | Yes | Yes |
| TB-2645B | Yes | Yes |
| TB-2646B | Yes | Yes |

#### Running
 Verify Components Operations

Configuring
 Switch Terminal Block Topologies

Verify Components

- If the switch terminal block type matches the switch terminal block type specified in the
 original system design, Test System Maintenance Software will not change the
 switch terminal block topology. For example, if you deliberately set a
 switch terminal block to use a 2-wire topology in NI MAX, Test System
 Maintenance Software will not change this configuration while running
 Verify Components with Configuring
 Switch Terminal Block Topologies enabled if the switch
 terminal block is the appropriate type to use with the associated switch
 device.
- If an incorrect switch terminal block type is configured in NI MAX, or if no
 switch terminal block type is configured, Test System Maintenance Software
 will configure the switch terminal block selected when the system was
 designed, and configure the switch terminal block to use a 1-wire
 topology. org.dita.html5/xsl/topic.xsl 455 Note If you
 need to use a 2-wire topology for a switch terminal block, you must
 configure this setting in NI MAX.

#### Running Continuity Test Operations

Continuity tests for the
 PXIe-2532B will result in a failure when the topology of the switch terminal block
 does not match the topology specified in the original system design for that switch
 terminal block.

Parent topic:

Configuring Switch Terminal Blocks and Topologies

<!--NI_TOPIC bundle=ecu-test-system-maintenance-software path=verify-components.html language=enus -->
## TOPIC 00016: Verify Components

- bundle_id: `ecu-test-system-maintenance-software`
- source_path: `verify-components.html`
- source_url: https://docs-be.ni.com/bundle/ecu-test-system-maintenance-software/raw/resource/enus/verify-components.html
- document_id: `ecu-test-system-maintenance-software`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Verify Components operation detects test system components discoverable by the Test System Maintenance Software and compares the results to the system configuration file to generate a list of test system components. The Verify Components operation generates a list of the following: Name changes

Verify Components

The Verify Components operation detects test system components
 discoverable by the Test System Maintenance Software and compares the results to the system
 configuration file to generate a list of test system components.

Verify Components

- Name changes
- Missing components
- Components with problems
- Components not expected but found
- Missing Ports
- Ports with problems
- Ports not expected but found

Note

Verify Components

Renaming
 Components

Configuring Switch Terminal Blocks and
 Topologies

Parent topic:

Maintenance Operations

Related tasks:

- Renaming Components
- Configuring Switch Terminal Blocks and Topologies

Related reference:

- COM Port Binding
