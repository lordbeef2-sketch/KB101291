# NI DOCUMENT BUNDLE: ni-compactrio

<!--NI_BUNDLE_CHUNK bundle=ni-compactrio start=1 end=250 -->
<!--NI_TOPIC bundle=ni-compactrio path=abort-transmit-sbrio.html language=enus -->
## TOPIC 00001: Abort Transmit

- bundle_id: `ni-compactrio`
- source_path: `abort-transmit-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/abort-transmit-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Abort a pending CAN frame transmission.Since the determinism of CAN depends on the prioritization of frames based on ID, the TCAN4550 CAN controller allows you to abort a pending transmit to replace it with a higher priority ID.When implementing protocols that require abort, ensure that only one tra

### Abort Transmit

Abort a pending CAN frame transmission.

Since the determinism of CAN depends on the prioritization of frames based on ID, the TCAN4550
 CAN controller allows you to abort a pending transmit to replace it with a higher
 priority ID.

When implementing protocols that require abort, ensure that only one transmit is pending. Call
 Wait on Transmit Complete before or after each call to
 CAN Output. If more than one transmit is pending at the time
 Abort Transmit is called, the Transmit
 Success Boolean could refer to any one of those pending frames.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

#### Node
 Outputs

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Transmit Success?

- Returns FALSE when the pending transmit
 successfully aborted.
- Returns TRUE when the pending frame transmitted
 successfully on the network prior to the Abort
 Transmit .

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=abort-transmit.html language=enus -->
## TOPIC 00002: Abort Transmit

- bundle_id: `ni-compactrio`
- source_path: `abort-transmit.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/abort-transmit.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Abort a pending CAN frame transmission. Since the determinism of CAN depends on the prioritization of frames based on ID, the SJA1000 CAN controller allows you to abort a pending transmit to replace it with a higher priority ID. When implementing protocols that require abort, ensure that only one tr

### Abort Transmit

Abort a pending CAN frame transmission.

Since the determinism of CAN depends on the prioritization of frames based on ID, the SJA1000 CAN controller allows you to abort a pending transmit to replace it with a higher priority ID.

When implementing protocols that require abort, ensure that only one transmit is pending. Call
 Wait on Transmit Complete before (or after) each call to
 CAN Output. If more than one transmit is pending at the time
 Abort Transmit is called, the Transmit
 Success Boolean could refer to any one of those pending frames.

Refer to the *I/O Methods* introduction for step by step instructions to place this
 method in your LabVIEW diagram.

#### Node Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Timeout

–1

#### Node Outputs

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Timed Out?

Timed Out?

TRUE

Timed
 Out?

Timeout

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Transmit Success?

Timed Out?

FALSE

FALSE

TRUE

Abort
 Transmit

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=accessing-teds-information-from-a-module-fpga.html language=enus -->
## TOPIC 00003: Accessing TEDS Information from a Module (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `accessing-teds-information-from-a-module-fpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/accessing-teds-information-from-a-module-fpga.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the modules that support TEDS-compatible transducers.96 C Series Modules that Support TEDS-Compatible Transducers NI 9218 NI 9219 NI 9230 NI 9231 NI 9232 NI 9234 NI 9237 NI 9250 Access Transducer Electronic Data Sheet (TEDS) information from TEDS-compatible transducers conn

### Accessing TEDS Information from a Module (FPGA Interface)

The following table lists the modules that support TEDS-compatible transducers.

| NI 9218 NI 9219 NI 9230 | NI 9231 NI 9232 NI 9234 | NI 9237 NI 9250 |
| --- | --- | --- |

Access Transducer Electronic Data Sheet (TEDS) information from TEDS-compatible transducers
 connected to the channels of the module.

Before you can read TEDS information, enable TEDS support for the module. Access TEDS
 information only from the host VI.

#### Example

For an example about how to access TEDS information, refer to the
 module Getting Started (FPGA) VI in the
 labview\examples\CompactRIO\Module
 Specific\<module>\<module>
 Getting Started directory.

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=acquiring-data-from-a-module-fpga-interface.html language=enus -->
## TOPIC 00004: Acquiring Data from a Module (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `acquiring-data-from-a-module-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/acquiring-data-from-a-module-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The information in this topic applies to analog input modules with a master timebase.94 Analog Input Modules with a Master Timebase NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 NI 9252

### Acquiring Data from a Module (FPGA Interface)

The information in this topic applies to analog input modules with a master timebase.

| NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 | NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 | NI 9246 NI 9247 NI 9250 NI 9251 NI 9252 NI 9253 NI 9770 NI 9775 |
| --- | --- | --- |

The module input channels are sampled simultaneously at the data rate configured for the
 module. Use the Start and Stop channels to
 put the module in and out of acquisition mode.

- You can not access module properties when a module is in acquisition mode.
- You can not access TEDS information, if supported, when a module is in
 acquisition mode.

Note

#### Example

The module Getting Started (FPGA) VI at
 labview\examples\CompactRIO\Module
 Specific\<module>\<module>
 Getting Started shows how to read from a module.

Parent topic:

Analog Input Modules

#### Putting the Module in Acquisition Mode

Complete the following steps to put the module in acquisition mode.

1. Configure an FPGA I/O Node with the Start channel of the
 module.
2. Wire a Boolean constant set to TRUE to the
 Start input of the FPGA I/O Node. 
 A synchronization pulse is sent to the module. The module starts
 acquiring data at the data rate you configure.

#### Reading Data from the Module

When the module starts acquiring data, you can use an FPGA I/O Node to read data from the
 module.

Connect the AI output of the FPGA I/O Node <sup>[[1]](#note-d23333e255)</sup>[<sup>1</sup>](#fnsrc_1-d23333e255) For the NI 9770, connect the RF In/I or RF
 In/Q items. to various types of functions, including an FPGA Memory function or
 an FPGA FIFO function.

To ensure that the VI reads the data synchronously when reading multiple channels on the
 module, place the channels in the same FPGA I/O Node.

The module internally acquires data at a specified rate. The FPGA I/O Node does not
 return data until new data has been acquired by the module.

Note

I/O Not Start error 65582

#### Exiting Acquisition Mode

Complete the following steps to exit acquisition mode.

1. Configure an FPGA I/O Node with the Stop channel of the
 module.
2. Write a TRUE to the Stop input. 
 The module is no longer in acquisition mode. You can now access its
 properties or, for some modules, TEDS information.

[<sup>1</sup>](#note_ref-d23333e255) For the NI 9770, connect the RF In/I or RF
 In/Q items.

<!--NI_TOPIC bundle=ni-compactrio path=acquiring-data-from-synchronized-c-series-m.html language=enus -->
## TOPIC 00005: Acquiring Data from Synchronized C Series Modules

- bundle_id: `ni-compactrio`
- source_path: `acquiring-data-from-synchronized-c-series-m.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/acquiring-data-from-synchronized-c-series-m.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Note the following when synchronizing multiple C Series modules: All modules must start acquisition mode at the same time. A single FPGA I/O Node function must read the synchronous data. Block Diagram Objects used to Synchronize Multiple C Series ModulesUse the FPGA I/O Property Node, FPGA I/O Node,

### Acquiring Data from Synchronized C Series
 Modules

- All modules must start acquisition mode at the same time.
- A single FPGA I/O Node function must read the synchronous data.

#### Block Diagram Objects used to Synchronize Multiple
 C Series Modules

Use the FPGA I/O Property Node, FPGA I/O Node, and
 FPGAMethod Node block diagram objects to synchronize multiple C Series
 modules.

Figure 3.

[IMAGE alt='FPGA I/O Property Node' src='GUID-E845507C-743C-4FDB-B430-9E843215BF2D-a5.svg']

Figure 4.

[IMAGE alt='FPGA I/O Node' src='GUID-D61A8A5A-74AC-4549-897A-6C03F82C915E-a5.svg']

Figure 5.

[IMAGE alt='FIFO Method Node' src='GUID-4B8C0DC1-AC97-4239-AA64-98502846678B-a5.svg']

#### Creating the Block Diagram

Reference the
 following image when creating a block diagram to synchronize multiple C Series
 modules. Customize the gray sections for your unique programming goals.

Figure 6.

[IMAGE alt='Block Diagram for Synchronizing Multiple C Series Modules' src='GUID-B569E90D-12C1-48B1-B7F0-327893A646A0-a5.svg']

1. Configure FPGA I/O Property Nodes for the master module and slave modules
 and wire a control to each Node.
2. Configure an FPGA I/O Node with Start channels for
 the modules you want to synchronize and wire a Boolean constant set to TRUE
 to each Start channel.
3. Configure an FPGA I/O Node with all of the channels from which you want to
 synchronously sample.
4. Configure an FPGA I/O Node with Stop channels for the
 modules you want to synchronize and wire a Boolean constant set to TRUE to
 each Stop channel.

Tip

You can acquire data from synchronized modules with
 different rates.

Note

Loop
 Timer

Wait

Note

Always wire the error in terminal and the error out terminal

#### Examples

Refer to the Synchronizing NI
 923x Modules (FPGA) VI in the labview\examples\CompactRIO\Module Specific\NI
 923x\Synchronizing NI 923x Modules\Synchronizing NI 923x Modules.lvproj
 for an example of synchronizing multiple modules with the same data rate.

Parent topic:

Synchronizing Multiple C Series Modules

#### What happens if I change the master timebase
 source?

Data Rate

Note

Data
 Rate

<!--NI_TOPIC bundle=ni-compactrio path=add-targets-and-devices.html language=enus -->
## TOPIC 00006: Adding Targets and Devices

- bundle_id: `ni-compactrio`
- source_path: `add-targets-and-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/add-targets-and-devices.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the CAN module before creating an FPGA VI. Before you can configure the CAN module, add the module to your CompactRIO configuration. Refer to Add Targets and Devices dialog box for information about how to add the CAN module to your CompactRIO configuration. To add the CAN module to the Pr

### Adding Targets and Devices

Configure the CAN module before creating an FPGA VI.

Before you can configure the CAN module, add the module to your CompactRIO
 configuration. Refer to Add Targets and Devices dialog box
 for information about how to add the CAN module to your CompactRIO
 configuration.

1. To add the CAN module to the Project Explorer window,
 select the CAN module from the list of modules in the New C Series
 Module dialog box.
2. To open the Module Configuration dialog box, right-click
 the NI 9852 or NI 9853 module in the Project Explorer window and select
 Properties from the shortcut menu.

Parent topic:

CAN Module Configuration

<!--NI_TOPIC bundle=ni-compactrio path=adding-a-chassis-item.html language=enus -->
## TOPIC 00007: Adding a Chassis Item

- bundle_id: `ni-compactrio`
- source_path: `adding-a-chassis-item.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-a-chassis-item.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a CompactRIO, Ethernet RIO, MXIe-RIO, Single-Board RIO, myRIO, roboRIO, or NI ELVIS RIO Control Module (NI ELVIS RIO CM) chassis item to your project. Complete the following steps to add a chassis item to your project. Right-click the target in the Project Explorer window and select New»Targets

### Adding a Chassis Item

Add a CompactRIO, Ethernet RIO, MXIe-RIO, Single-Board RIO, myRIO, roboRIO, or NI
 ELVIS RIO Control Module (NI ELVIS RIO CM) chassis item to your project.

Complete the following steps to add a chassis item to your project.

1. Right-click the target in the Project Explorer window and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box.
2. Click the New target or device radio button.
3. Select the appropriate device.
4. Click the OK button. 
 Note A chassis item is automatically added to your project for cRIO integrated
 controller and chassis and sbRIO devices. 
 LabVIEW adds the chassis item to the project. Table 13.LabVIEW Chassis Item
 IconsItem Icon
 Device
 Description[IMAGE alt='image' src='GUID-E49E6B79-64D2-4C79-BF91-FF8E66A59685-a5.svg']
 CompactRIO chassis, Ethernet RIO chassis
 LabVIEW adds this chassis item when you configure a
 project with a CompactRIO reconfigurable chassis, CompactRIO
 integrated chassis and controller, or Ethernet RIO
 chassis.
 [IMAGE alt='image' src='GUID-63CC6D8A-83C2-4986-88EF-03906B9FC617-a5.svg']
 MXIe-RIO chassis
 LabVIEW adds this chassis item when you configure a
 project with a MXIe-RIO chassis. You can add a MXIe-RIO
 chassis to a real-time target or the host PC.
 [IMAGE alt='image' src='GUID-D33AEF39-A7CE-4DB7-BCD6-D77CB89357C6-a5.svg']
 Single-Board RIO, myRIO, roboRIO, or NI ELVIS RIO CM
 device
 LabVIEW adds this chassis item when you configure a
 project with a Single-Board RIO, myRIO, roboRIO, or NI ELVIS
 RIO CM device.

Parent topic:

Configuring a Project with Offline Hardware

#### Adding an R Series Expansion Chassis Item

You can add an R Series expansion chassis to the *FPGA target* for an R Series
 device in your project.

Enter the prerequisites here (optional).

Enter the context of your task here (optional).

1. Right-click the FPGA Target for the R Series device in
 the Project Explorer window and select New»R
 Series Expansion Chassis from the shortcut menu to display the
 New R Series Expansion Chassis dialog box.
2. Click the OK button. LabVIEW adds a chassis item to the
 project.

1. Right-click the FPGA Target for the R Series device in
 the Project Explorer window and select New»R
 Series Expansion Chassis from the shortcut menu to display the
 New R Series Expansion Chassis dialog box. 
 Enter the result of your step here (optional).
2. Click the OK button. 
 LabVIEW adds a chassis item to the project.Table 14.LabVIEW R Series
 Chassis Item IconItem Icon
 Device
 Description[IMAGE alt='image' src='GUID-8AECDEC0-722C-4670-A06F-2C6F7DEF9523-a5.svg']
 R Series Expansion chassis
 LabVIEW adds this chassis item when you configure a
 project with an R Series expansion chassis.

Related tasks:

- Adding an FPGA Target

<!--NI_TOPIC bundle=ni-compactrio path=adding-a-clip-for-a-single-board-rio-device-t.html language=enus -->
## TOPIC 00008: Adding a CLIP for a Single-Board RIO Device to a LabVIEW Project

- bundle_id: `ni-compactrio`
- source_path: `adding-a-clip-for-a-single-board-rio-device-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-a-clip-for-a-single-board-rio-device-t.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, use the sbRIO CLIP Generator to generate a unique socketed CLIP. Complete the following steps to add the CLIP you created using the sbRIO CLIP Generator for a Single-Board RIO target to a LabVIEW project. Create a new project. Add an FPGA target to the project. In the Add Targets a

### Adding a CLIP for a Single-Board RIO Device to a LabVIEW Project

Before you begin, use the sbRIO CLIP Generator to generate a unique socketed
 CLIP.

Complete the following steps to add the CLIP you created using the sbRIO CLIP
 Generator for a Single-Board RIO target to a LabVIEW project.

1. Create a new project.
2. Add an FPGA target to the project. In the Add Targets and Devices dialog box,
 select Real-Time Single-Board RIO and then select your
 device.
3. In the Project Explorer window, right-click the Chassis
 item and select New»FPGA Target.
4. Right-click the RMC Socket or sbRIO-9651
 Socket item and select Properties to
 launch the Component-Level IP Properties or RMC Socket
 Properties dialog box.
5. On the General page, use the RMC or sbRIO-9651
 Socketed Component Level IP Declaration drop-down list to select
 the CLIP you created.
6. On the Clock Selections page, configure any clocks that you
 specified on the Clock Settings page of the sbRIO CLIP Generator.
7. Click OK to close the Component-Level IP
 Properties dialog box.

Implementing FPGA VIs for the sbRIO-9651

Parent topic:

sbRIO-9651

Related tasks:

- Implementing FPGA VIs for the sbRIO-9651

<!--NI_TOPIC bundle=ni-compactrio path=adding-a-controller-target.html language=enus -->
## TOPIC 00009: Adding a Controller Target

- bundle_id: `ni-compactrio`
- source_path: `adding-a-controller-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-a-controller-target.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: A controller target can be a CompactRIO controller, Ethernet RIO chassis, Single-Board RIO device, myRIO device, roboRIO device, or NI ELVIS RIO Control Module (NI ELVIS RIO CM) device.Complete the following steps to add a controller target to your project. Create a new project or open an existing p

### Adding a Controller Target

A controller target can be a CompactRIO controller, Ethernet RIO chassis,
 Single-Board RIO device, myRIO device, roboRIO device, or NI ELVIS RIO Control Module (NI
 ELVIS RIO CM) device.

Complete the following steps to add a controller target to your project.

1. Create a new project or open an existing project.
2. Right-click the project root in the Project Explorer window and select
 New»Targets and Devices from the shortcut menu to display
 the Add Targets and Devices dialog box.
3. Click the New target or device radio button.
4. Select the appropriate target or device.
5. Click the OK button. 
 LabVIEW adds the controller target icon to the project. Table 12.LabVIEW Controller
 Target IconsTarget Icon
 Device
 Description[IMAGE alt='image' src='GUID-CF208E95-909F-4816-8BE5-1365E3B846A4-a5.svg']
 CompactRIO controller
 LabVIEW adds this controller target when you configure a
 project with a CompactRIO real-time controller or CompactRIO
 integrated controller and chassis.
 [IMAGE alt='image' src='GUID-68D692CE-AA5A-478A-8677-5DEE6AA16F65-a5.svg']
 Ethernet RIO chassis
 LabVIEW adds this target when you configure a project
 with an Ethernet RIO chassis. The Ethernet RIO chassis is
 not a real-time target, but it can add expansion I/O to a
 real-time target.
 [IMAGE alt='image' src='GUID-B83FEB6B-D53C-4CF7-9E69-BC06C3F35447-a5.svg']
 Single-Board RIO device
 LabVIEW adds this controller target when you configure a
 project with a Single-Board RIO device.
 [IMAGE alt='image' src='GUID-F07E1D8C-A170-49BA-AEBF-D147DA0CF400-a5.svg']
 myRIO device
 LabVIEW adds this controller target when you configure a
 project with a myRIO-1900.
 [IMAGE alt='image' src='GUID-B0183442-AA63-49BA-A823-01E22BB294A8-a5.svg']
 myRIO device
 LabVIEW adds this controller target when you configure a
 project with a myRIO-1950.
 [IMAGE alt='image' src='GUID-787B6E2A-0FC3-4355-B92A-5ED73D5E09DD-a5.svg']
 roboRIO device
 LabVIEW adds this controller target when you configure a
 project with a roboRIO.
 [IMAGE alt='image' src='GUID-E7D5B3CD-A713-456F-BC62-18968D3D2150-a5.svg']
 NI ELVIS RIO Control Module (NI ELVIS RIO CM)
 device
 LabVIEW adds this controller target when you configure a
 project with an NI ELVIS RIO CM.

Parent topic:

Configuring a Project with Offline Hardware

<!--NI_TOPIC bundle=ni-compactrio path=adding-additional-hardware.html language=enus -->
## TOPIC 00010: Adding Additional Hardware

- bundle_id: `ni-compactrio`
- source_path: `adding-additional-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-additional-hardware.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW cannot discover all compatible hardware. Complete the following steps to add an R Series expansion chassis or RIO mezzanine cards to your project. Adding an R Series Expansion Chassis Right-click My Computer in the Project Explorer window and select New»Targets and Devices from the shortcut

### Adding Additional Hardware

LabVIEW cannot discover all compatible hardware. Complete the following steps to add an R Series expansion chassis or RIO mezzanine cards to your
 project.

Parent topic:

Configuring a Project with Connected Hardware

#### Adding an R
 Series Expansion Chassis

1. Right-click My Computer in the Project
 Explorer window and select New»Targets and
 Devices from the shortcut menu to display the Add Targets and
 Devices dialog box.
2. Select the appropriate R Series device and click the OK
 button. LabVIEW adds an FPGA target item for the R Series device to the
 project.
3. Right-click the FPGA Target for the R Series device in
 the Project Explorer window and select New»R
 Series Expansion Chassis from the shortcut menu to display the
 New R Series Expansion Chassis dialog box.
4. Select the connector to which the R Series Expansion chassis is connected in
 the Location pull-down menu.
5. Check the Discover C Series modules checkbox and click
 the OK button to add the items to the project.
6. Right-click a module in the Project Explorer window and
 select Properties from the shortcut menu to configure
 module-specific settings.Enter your first step here. 
 LabVIEW adds the following target to your project. Table 10.Project/Target
 IconItem Icon
 Device
 Description[IMAGE alt='image' src='GUID-8AECDEC0-722C-4670-A06F-2C6F7DEF9523-a5.svg']
 R Series Expansion Chassis or RIO Mezzanine Card
 LabVIEW adds this target/item to a project for a R Series
 expansion chassis and RIO Mezzanine cards.Enter the result of your step here (optional).

Enter an example that illustrates the current task (optional).

Enter the tasks the user should do after finishing this task (optional).

#### Adding a RIO Mezzanine Card

1. Right-click the FPGA Target in the
 Project Explorer window and
 select New»RIO Mezzanine Card from
 the shortcut menu 
 The New RIO Mezzanine Card dialog box
 opens.
2. Select the appropriate RIO mezzanine card from the
 Type pull-down menu and click
 the OK button. 
 LabVIEW adds a RIO mezzanine card item and FPGA I/O items for
 I/O to the project.
3. To configure RIO mezzanine card specific settings, right-click
 the RIO mezzanine card item in the Project
 Explorer window and select
 Properties from the shortcut
 menu. 
 Note 
 LabVIEW discovers any C Series modules connected
 to RIO mezzanine cards with C Series slots after you
 add the card to the project.

| Item Icon | Device | Description |
| --- | --- | --- |
|  | R Series Expansion Chassis or RIO Mezzanine Card | LabVIEW adds this target/item to a project for a R Series expansion chassis and RIO Mezzanine cards. |

<!--NI_TOPIC bundle=ni-compactrio path=adding-an-fpga-target.html language=enus -->
## TOPIC 00011: Adding an FPGA Target

- bundle_id: `ni-compactrio`
- source_path: `adding-an-fpga-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-an-fpga-target.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: You do not need to add an FPGA target to your project when programming in Scan Interface Mode, Real-Time Mode, or Real-Time Scan Mode.Complete the following steps to add an FPGA target to your project. Real-Time Mode and Real-Time Scan Mode are only available on cRIO-904x and cRIO-905x controllers

### Adding an FPGA Target

You do not need to add an FPGA target to your project when programming in Scan
 Interface Mode, Real-Time Mode, or Real-Time Scan Mode.

Note

Real-Time Mode

Real-Time Scan Mode

x

x

1. Right-click the chassis item in the Project Explorer window and select New»FPGA Target from the shortcut menu.
2. If the Deploy CompactRIO Chassis Settings? dialog box
 appears, click the Deploy Later button to return to the
 project. 
 LabVIEW adds an FPGA target item for the chassis to the project and puts
 the system into LabVIEW FPGA Interface mode.Table 15.LabVIEW FPGA Target
 IconTarget Icon
 Device
 Description[IMAGE alt='image' src='GUID-CA42ABF0-77A8-43C5-8F8F-B9F39563D082-a5.svg']
 FPGA
 LabVIEW adds this FPGA target when you configure a
 project with a CompactRIO chassis, Ethernet RIO chassis,
 MXIe-RIO chassis, or Single-Board RIO device in the FGPA
 Interface.

Parent topic:

Configuring a Project with Offline Hardware

Related concepts:

- Programming Interfaces
- Programming Modes

Related tasks:

- Adding a Controller Target for the cRIO-904x/cRIO-905x

<!--NI_TOPIC bundle=ni-compactrio path=adding-i-o-items.html language=enus -->
## TOPIC 00012: Adding I/O Items

- bundle_id: `ni-compactrio`
- source_path: `adding-i-o-items.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-i-o-items.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: An I/O item can be a RIO mezzanine card or a C Series module. RIO mezzanine cards have I/O or slots for C Series modules. RIO Mezzanine Cards Complete the following steps to add an RIO mezzanine card in FPGA Interface Mode to a project. Right-click the FPGA Target in the Project Explorer window and

### Adding I/O Items

An I/O item can be a RIO mezzanine card or a C Series module. RIO mezzanine cards
 have I/O or slots for C Series modules.

Parent topic:

Configuring a Project with Offline Hardware

#### RIO Mezzanine Cards

Complete the following steps to add an RIO mezzanine card in FPGA
 Interface Mode to a project.

1. Right-click the FPGA Target in the Project
 Explorer window and select New»RIO Mezzanine
 Card from the shortcut menu to display the New RIO
 Mezzanine Card dialog box.
2. Select the appropriate RIO mezzanine card from the
 Type pull-down menu and click the
 OK button. LabVIEW adds an RIO mezzanine card item
 and FPGA I/O items for I/O to the project.
3. Right-click the RIO mezzanine card item in the Project
 Explorer window and select Properties
 from the shortcut menu to configure RIO mezzanine card specific settings or
 select New»C Series Modules to add C Series
 modules. 
 LabVIEW adds the mezzanine card icon to the project. Table 16.LabVIEW RIO Mezzanine
 Card IconItem Icon
 Description[IMAGE alt='image' src='GUID-8AECDEC0-722C-4670-A06F-2C6F7DEF9523-a5.svg']
 LabVIEW adds this icon when you configure a project with
 a RIO mezzanine card.

Related concepts:

- Programming Interfaces

#### C Series Modules

Enter a short description of your task here (optional).

Note

x

x

1. Right-click one of the resource items from the following table in the
 Project Explorer window and select New»C
 Series Modules from the shortcut menu to display the
 Add Targets and Devices dialog box. 
 For This Mode
 Right-Click This Resource ItemFPGA Interface Mode
 FPGA Target
 Scan Interface Mode
 Real-Time Scan Resources Item
 Real-Time Mode
 Real-Time Resources Item
2. Click the New target or device radio button, select
 C Series Module, and click the
 OK button to display the New C Series
 Module dialog box.
3. Select the appropriate C Series module from the Module
 Type pull-down menu and click the OK
 button. LabVIEW adds a module item and FPGA I/O items for the module I/O to the
 project.
4. Repeat steps 1 through 3 to add additional C Series modules to the
 project.
5. Right-click a module item in the Project Explorer window
 and select Properties from the shortcut menu to configure
 module-specific settings. 
 LabVIEW adds a C Series module icon to the project.

| Item Icon | Device | Description |
| --- | --- | --- |
|  | C Series Modules | LabVIEW adds this module item when you configure a project with C Series modules. |
|  | Onboard C Series Modules | LabVIEW adds this module item when you configure a project with a Single-Board RIO device that has onboard modules. LabVIEW adds onboard modules to the project in Scan Interface Mode. You can drag the onboard module item to FPGA target to place the module in the FPGA interface mode. |

Related concepts:

- Programming Interfaces
- Programming Modes
- C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=adding-peripherals-to-a-clip.html language=enus -->
## TOPIC 00013: Adding Peripherals to a CLIP

- bundle_id: `ni-compactrio`
- source_path: `adding-peripherals-to-a-clip.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/adding-peripherals-to-a-clip.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: A peripheral is user-configurable capability of the NI sbRIO device that requires pins, FPGA space, or both pins and FPGA space in order to function. A peripheral can be a Serial, CAN, or secondary Ethernet port.Complete the following steps to select the processor peripherals to implement in the CLI

### Adding Peripherals to a CLIP

A peripheral is user-configurable capability of the NI sbRIO device that
 requires pins, FPGA space, or both pins and FPGA space in order to function. A peripheral
 can be a Serial, CAN, or secondary Ethernet port.

Complete the following steps to select the processor peripherals to implement in the CLIP design.

To

1. Open the Peripherals page of the sbRIO CLIP Generator .
2. Enable the Enabled
 column of the Additional
 Peripherals pane for each peripheral
 you want to add to the CLIP.
3. Configure the enabled peripheral with the
 Configuration pane. Refer
 to the following notes for information about
 peripherals specific to different NI sbRIO
 targets.
4. To configure additional peripherals, repeat
 steps 1 and 2.
5. Click Next to continue
 to the Pin Configuration
 page. 
 Use the Pin Configuration to configure the pins that each
 peripheral uses.

Note

- You might not need to configure all the lines for a selected peripheral to function,
 depending on the needs of your application. For example, if you enable the
 Serial2 port, you might not need to configure any RTS or Modem
 lines for your application.
- If you do not select a pin, the sbRIO CLIP Generator does not automatically assign a
 pin for you. An unassigned pin may open a pin configuration warning.
- Peripherals cannot reserve the same pins. If a peripheral uses a specific DIO pin and
 another peripheral attempts to request it, the Enabled column for the
 second peripheral becomes disabled and a warning icon appears.
- Serial ports may be notated differently depending on the environment in which you are
 working. Refer to Serial Port Naming Conventions for additional
 information.

SD Card

RMC Connector
 Design Guide

ETH2

Eth2

Bank 2

Note

Eth2

Serial2

Caution

Parent topic:

Creating a Component-Level IP for an NI sbRIO Target

Related concepts:

- Serial Port Naming Conventions

Related tasks:

- Configuring I/O Pins on the Target
- Creating a Component-Level IP for an NI sbRIO Target

Related information:

- RMC Connector Design Guide

<!--NI_TOPIC bundle=ni-compactrio path=advanced-can-port-properties.html language=enus -->
## TOPIC 00014: Advanced CAN Port Properties

- bundle_id: `ni-compactrio`
- source_path: `advanced-can-port-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/advanced-can-port-properties.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the CAN Advanced Port Configuration dialog box to configure advanced properties for the CAN port. Open this dialog from the Module Configuration dialog box.

### Advanced CAN Port Properties

Use the CAN Advanced Port Configuration dialog box to configure advanced
 properties for the CAN port. Open this dialog from the Module
 Configuration dialog box.

Parent topic:

CAN Module Configuration

Related concepts:

- Bit Timing
- Module Configuration
- Error Terminals
- Arbitration
- CAN Input

<!--NI_TOPIC bundle=ni-compactrio path=analog-input-modules.html language=enus -->
## TOPIC 00015: Analog Input Modules

- bundle_id: `ni-compactrio`
- source_path: `analog-input-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/analog-input-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 35 C Series Analog Input Modules C Series Analog Input Module Description NI-9201 ±10 V, 500 kS/s, 12-Bit, 8-Channel C Series Voltage Input Module NI-9202 ±10 V, 10 kS/s, 24-Bit, 16-Channel C Series Voltage Input Module NI-9203 200 kS/s, ±20 mA, 8-Channel C Series Current Input Module NI-9205 ±10 V,

### Analog Input Modules

| C Series Analog Input Module | Description |
| --- | --- |
| NI-9201 | ±10 V, 500 kS/s, 12-Bit, 8-Channel C Series Voltage Input Module |
| NI-9202 | ±10 V, 10 kS/s, 24-Bit, 16-Channel C Series Voltage Input Module |
| NI-9203 | 200 kS/s, ±20 mA, 8-Channel C Series Current Input Module |
| NI-9205 | ±10 V, 250 kS/s, 16-Bit, 32-Channel C Series Voltage Input Module |
| NI-9206 | ±10 V, 250 kS/s, 16-Bit, 32-Channel, 600 VDC Isolation C Series Voltage Input Module |
| NI-9207 | 500 S/s, 16-Channel C Series Voltage and Current Input Module |
| NI-9208 | 500 S/s, ±20 mA, 16-Channel C Series Current Input Module |
| NI-9209 | ±10 V, 500 S/s, 16-Channel C Series Voltage Input Module |
| NI-9210 | 4-Channel, 14 S/s Aggregate, ±80 mV C Series Temperature Input Module |
| NI-9211 | 4-Channel, 14 S/s, ±80 mV C Series Temperature Input Module |
| NI-9212 | 8-Channel, 95 S/s/ch Simultaneous, ±78 mV C Series Temperature Input Module |
| NI-9213 | 16 channel, up to 75 S/s per channel, ±78 mV C Series Temperature Input Module |
| NI-9214 | 16-Channel, 68 S/s Aggregate, ±78 mV, Isothermal C Series Temperature Input Module |
| NI-9215 | ±10 V, 100 kS/s/ch, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9216 | 8-Channel, 400 S/s Aggregate, 0 Ω to 400 Ω, PT100 RTD C Series Temperature Input Module |
| NI-9217 | 4-Channel, 400 S/s Aggregate, 0 Ω to 400 Ω, PT100 RTD C Series Temperature Input Module |
| NI-9218 | 51.2 kS/s/ch, 2-Channel C Series Universal Analog Input Module |
| NI-9219 | 100 S/s/ch, 4-Channel C Series Universal Analog Input Module |
| NI-9220 | ±10 V, 100 kS/s/ch, 16-Bit, Simultaneous Input, 16-Channel C Series Voltage Input Module |
| NI-9221 | ±10 V, 1 MS/s, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9222 | ±10 V, 500 kS/s/ch, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9223 | ±10 V, 1 MS/s, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9224 | ±10 V, 1 kS/s/ch, 24-Bit, Simultaneous Input, 8-Channel C Series Voltage Input Module |
| NI-9225 | ±10 V, 1 kS/s/ch, 24-Bit, Simultaneous Input, 8-Channel C Series Voltage Input Module |
| NI-9226 | 8-Channel, 400 S/s Aggregate, 0 Ω to 4000 Ω, PT1000 RTD C Series Temperature Input Module |
| NI-9227 | 50 kS/s/ch, 5 Arms, 24-Bit, 4-Channel C Series Current Input Module |
| NI-9228 | ±60 V, 1 kS/s/ch, 24-Bit, Simultaneous Input, 8-Channel C Series Voltage Input Module |
| NI-9229 | ±60 V, 50 kS/s/ch, 24-Bit, Simultaneous Input, 4-Channel C Series Voltage Module |
| NI-9230 | 3-Channel, 12.8 kS/s/channel, ±30 V, C Series Sound and Vibration Input Module |
| NI-9231 | 8-Channel, 51.2 kS/s/channel, -5 V to 5 V, C Series Sound and Vibration Input Module |
| NI-9232 | 3-Channel, 102.4 kS/s/channel, ±30 V, C Series Sound and Vibration Input Module |
| NI-9233 | 4-Channel, 50kS/s/channel, ±5 V, C Series Sound and Vibration Input Module |
| NI-9234 | 4-Channel, 51.2 kS/s/channel, ±5 V, C Series Sound and Vibration Input Module |
| NI-9235 | 10 kS/s/channel, 120 Ω Quarter-Bridge Strain Gage, 8-Channel C Series Strain/Bridge Input Module |
| NI-9236 | 10 kS/s/channel, 350 Ω Quarter-Bridge Strain Gage, 8-Channel C Series Strain/Bridge Input Module |
| NI-9237 | 50 kS/s/channel, Bridge Analog Input, 4-Channel C Series Strain/Bridge Input Module |
| NI-9238 | ±500 mV, 50 kS/s/ch, 24-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9239 | ±10 V, 50 kS/s/ch, 24-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI-9242 | 250 Vrms L-N, 400 Vrms L-L, 50 kS/s/ch, 24-Bit, 3-Phase C Series Voltage Input Module |
| NI-9244 | 400 Vrms L-N, 690 Vrms L-L, 50 kS/s/ch, 24-Bit, 3-Phase C Series Voltage Input Module |
| NI-9246 | 50 kS/s/ch, 20 Arms, 30 Apk, 24-Bit, 3-Channel C Series Current Input Module |
| NI-9247 | 50 kS/s/ch, 50 Arms, 147 Apk, 24-Bit, 3-Channel C Series Current Input Module |
| NI-9250 | 2-Channel, 102.4 kS/s/ch Simultaneous, ±5 V, C Series Sound and Vibration Input Module |
| NI-9251 | 3 Vrms, 102.4 kS/s/ch Simultaneous, 2-Channel C Series Voltage Input Module |
| NI-9252 | ±10 V, 50 kS/s/ch, 24-Bit, 8-Channel C Series Voltage Input Module |
| NI-9253 | 50 kS/s/ch, ±20 mA, 24-Bit, 8-Channel C Series Current Input Module |
| NI-9320 | ±10 V, 200 kS/s/ch, 16-Bit, Simultaneous Input, 16-Channel C Series Voltage Input Module |
| NI-9381 | 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunction I/O Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=analog-output-modules.html language=enus -->
## TOPIC 00016: Analog Output Modules

- bundle_id: `ni-compactrio`
- source_path: `analog-output-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/analog-output-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 295 C Series Analog Output Modules C Series Analog Output Module Description NI-9260 51.2 kS/s/ch Simultaneous, 3 Vrms, 2-Channel C Series Voltage Output Module NI-9262 1 MS/s/ch Simultaneous, ±10 V, 6-Channel C Series Voltage Output Module NI-9263 100 kS/s/ch Simultaneous, ±10 V, 4-Channel C Series

### Analog Output Modules

| C Series Analog Output Module | Description |
| --- | --- |
| NI-9260 | 51.2 kS/s/ch Simultaneous, 3 Vrms, 2-Channel C Series Voltage Output Module |
| NI-9262 | 1 MS/s/ch Simultaneous, ±10 V, 6-Channel C Series Voltage Output Module |
| NI-9263 | 100 kS/s/ch Simultaneous, ±10 V, 4-Channel C Series Voltage Output Module |
| NI-9264 | 25 kS/s/ch Simultaneous, ±10 V, 16-Channel C Series Voltage Output Module |
| NI-9265 | 4-Channel C Series Current Output Module |
| NI-9266 | 8-Channel C Series Current Output Module |
| NI-9269 | 100 kS/s/ch Simultaneous, ±10 V, Isolated, 4-Channel C Series Voltage Output Module |
| NI-9381 | 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunction I/O Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=arbitration.html language=enus -->
## TOPIC 00017: Arbitration

- bundle_id: `ni-compactrio`
- source_path: `arbitration.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/arbitration.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each CAN port uses dedicated resources in LabVIEW FPGA, as well as distinct communication paths between LabVIEW FPGA and the module. When you access two different CAN ports in your FPGA VI, the nodes in the LabVIEW FPGA VI block diagram execute independently. For example, if you output a CAN frame t

### Arbitration

Each CAN port uses dedicated resources in LabVIEW FPGA, as well as distinct communication paths
 between LabVIEW FPGA and the module. When you access two different CAN ports in your
 FPGA VI, the nodes in the LabVIEW FPGA VI block diagram execute independently.

For example, if you output a CAN frame to CAN0 and simultaneously
 output a CAN frame to CAN1, the two CAN Output nodes execute
 independently. As another example, access to CAN0 on a module in
 slot 1 occurs independently from access to CAN0 on a module in
 slot 2.

When two or more nodes in the LabVIEW FPGA VI block diagram access the same CAN port at the same
 time, arbitration can occur to determine which node executes first. This arbitration may
 cause delays or jitter in your application. For example, if you want to transmit a
 specific CAN frame when a digital input trigger is detected in LabVIEW FPGA, arbitration
 between the CAN Output node and other CAN nodes can cause jitter from the digital input
 pulse to the start of the CAN frame.

#### Node Arbitration

For the same CAN port,
 CAN nodes of the same type must arbitrate. There are four types of CAN nodes:

- CAN Input
- CAN Output
- I/O Method Node
- I/O Property Node

CAN nodes of different type do not arbitrate at the node level.

For most
 applications, CAN node arbitration does not occur, and when it does the jitter
 introduced is small. For example, you would not normally use two CAN Input nodes
 simultaneously on the same CAN port, because neither node would return the correct
 sequence of CAN frames.

The most common situation in which CAN node
 arbitration occurs is use of a Wait I/O Method simultaneously with another I/O
 Method. For example, if you invoke Wait on Transmit Complete with a
 Timeout of 10 seconds, then invoke Abort Transmit soon
 after, node-level arbitration causes the Abort Transmit to execute after the Wait on
 Transmit Complete (possibly 10 seconds after invocation). When using multiple I/O
 Methods, you can avoid this behavior by polling for the event using
 Timeout of 0.

#### Output Path Arbitration

For each CAN
 port, two communication paths exist between LabVIEW FPGA and the CAN module. The
 output path transfers information from LabVIEW FPGA to the CAN port, and the input
 path transfers information from the CAN port to LabVIEW FPGA.

When two or
 more nodes in the LabVIEW FPGA VI block diagram access the same CAN port,
 arbitration can occur for the underlying output path. This arbitration is different
 than the usual node arbitration in LabVIEW FPGA, which is limited to multiple
 instances of a node. For example, if you write a frame to
 CAN0, and read a property on CAN0
 at the same time, arbitration occurs for the output path, because the CAN Output
 Node and the I/O Property
 Node both
 send information from LabVIEW FPGA to the CAN port.

The following nodes use
 the output path to the CAN port:

- CAN Output
- I/O Method Node: Abort Transmit
- I/O Method Node: Reset
- I/O Method Node: Start
- I/O Method Node: Stop
- I/O Property Node: Read any property
- I/O Property Node: Write any property

When two or more of these nodes execute simultaneously for the same CAN port,
 arbitration occurs to force sequential execution, and some jitter may result. When
 arbitration occurs in the same FPGA clock cycle, CAN Output is prioritized first,
 then the I/O Method
 Node, then the
 I/O Property
 Node. When
 the nodes are the same, CAN node arbitration occurs.

The output path is
 implemented as a FIFO. This allows multiple frames to be sent to the CAN module for
 transmit, thus enabling tests that generate full bus load.

All nodes in the
 preceding list use the output FIFO with the exception of the Stop and Reset method.
 Since these methods stop CAN communication, they must execute regardless of pending
 transmit frames. Once the Stop or Reset method arbitrates successfully for the
 output path, it bypasses the FIFO and transfers the method to the CAN port for
 immediate execution.

When the output FIFO is full, a node in the preceding
 list (except Stop and Reset) must wait for an element to become available. This
 generally occurs when a frame from a previous CAN Output transmits successfully onto
 the network. The Output Timeout (ms) in the *CAN
 Advanced Port Configuration* dialog box specifies how long to wait for a
 new element to become available. Therefore, the Output Timeout
 (ms) applies to any CAN node in the preceding list, not just the CAN
 Output node.

If you specify Output Timeout (ms) of 0,
 the node simply checks to see if a new element is available (non-blocking). If an
 element exists, the node executes and error status of FALSE is returned (success).
 If no element exists, the node fails to execute, and error status of TRUE is
 returned (error). Therefore, in order to poll (such as writing frames without
 waiting), you must enable *Error Terminals* for the node. When an error
 is returned, you must attempt to execute the node again at a later time.

#### Input Path Arbitration

For the input path
 from the CAN port to LabVIEW FPGA, arbitration does not occur within LabVIEW FPGA.
 As soon as the CAN module has data for LabVIEW FPGA nodes, the data transfers
 immediately.

When the CAN port attempts to transfer information for two or
 more nodes back to LabVIEW FPGA, arbitration for the input path occurs within the
 CAN module. For example, if a CAN frame is received at the same time that a property
 is read, the CAN module must decide which node's data to transfer first. Although
 this input path arbitration can cause jitter, that jitter is minimal compared to the
 effects you can see from CAN node arbitration or CAN output path arbitration.

#### Module Configuration

The configuration
 information in Module Configuration is transferred from LabVIEW FPGA to the CAN
 module when the FPGA VI runs. Although this transfer occurs automatically as soon as
 the VI begins to run, all CAN nodes must wait for this one-time configuration to
 complete. The time required for configuration can be up to 1 second.

If your
 FPGA VI does not execute a CAN node before the configuration time elapses, you will
 not notice any delay. If a CAN node is executed before the
 configuration time elapses, the CAN node will wait for configuration to complete,
 then execute normally. If you execute CAN nodes in a manner that does not depend on
 timing, this behavior is not a concern. However, if you require the first CAN Input
 or CAN Output in your FPGA VI to execute without delay, you can do this by adding
 one of the following to the beginning of your VI (before the main loop):

- 1 second delay
- CAN Property or Method node (for instance, a Start method
 node)

#### Summary

When an FPGA VI is limited to CAN
 Input and CAN Output for each CAN port, the jitter between node execution and CAN
 frame transfer is very small. This is due to the fact that each CAN port uses a
 distinct communication path for input data and output data.

When you mix
 methods or properties along with input/output, you may see increased jitter between
 node invocation and CAN frame transfer. This jitter is due to the arbitration. The
 jitter is typically only a few microseconds, so it will generally be well within the
 limits for your application.

Parent topic:

Controller Area Network (CAN) Interface Module Reference

Related concepts:

- Advanced CAN Port Properties
- CAN Input
- Error Terminals

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9375.html language=enus -->
## TOPIC 00018: Avoiding Timing Uncertainty with the NI 9375 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9375.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9375.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To avoid introducing timing uncertainty into DI and DO Node calls, adhere to the following guidelines: Use a single I/O Node to access DI and DO operations to ensure proper sequencing. Do not perform the following operations concurrently: DI Node call DO Node call For an example of the recommended w

### Avoiding Timing Uncertainty with the NI 9375 (FPGA Interface)

To avoid introducing timing uncertainty into DI and DO Node calls, adhere to the following
 guidelines:

- Use a single I/O Node to access DI and DO operations to ensure proper sequencing.
- Do not perform the following operations concurrently:
  - DI Node call
  - DO Node call

For an example of the recommended way to use the DIO subsystems, refer to the NI 9375
 Digital Port Input Output VI in
 labview\examples\CompactRIO\Module Specific\NI 9375\NI 9375 Digital Port
 Input Output\NI 9375 Digital Port Input Output.lvproj.

Parent topic:

NI 9375 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9375_2.html language=enus -->
## TOPIC 00019: Avoiding Timing Uncertainty with the NI 9375 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9375_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9375_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To avoid introducing timing uncertainty into DI and DO Node calls, adhere to the following guidelines: Use a single I/O Node to access DI and DO operations to ensure proper sequencing. Do not perform the following operations concurrently: DI Node call DO Node call For an example of the recommended w

### Avoiding Timing Uncertainty with the NI 9375 (FPGA Interface)

To avoid introducing timing uncertainty into DI and DO Node calls, adhere to the following
 guidelines:

- Use a single I/O Node to access DI and DO operations to ensure proper sequencing.
- Do not perform the following operations concurrently:
  - DI Node call
  - DO Node call

For an example of the recommended way to use the DIO subsystems, refer to the NI 9375
 Digital Port Input Output VI in
 labview\examples\CompactRIO\Module Specific\NI 9375\NI 9375 Digital Port
 Input Output\NI 9375 Digital Port Input Output.lvproj.

Parent topic:

NI 9375 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9381.html language=enus -->
## TOPIC 00020: Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9381.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9381.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO Node, and Set Output Data method calls. Failing to follow these guidelines may result in lost data points for DO Node calls or Set Output Data method calls when either of them are made from inside a single-

### Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO
 Node, and Set Output Data method calls. Failing to follow these
 guidelines may result in lost data points for DO Node calls or Set Output Data method
 calls when either of them are made from inside a single-cycle Timed Loop.

- Use a single I/O Node to access AI and AO operations to ensure proper sequencing.
- Do not run the Set Output Enable method when an AI, AO, or DO subsystems is
 active.
- Do not perform the following operations concurrently:
  - AI Node call
  - AO Node call
  - Set Output Enable method call
  - Automatic line direction change when a DO call is made under the following
 conditions:
    - The call is made from outside of a single-cycle Timed Loop.
    - The Allow programmatic DIO line direction 
 checkbox is enabled in the C Series Module
 Properties dialog box.
    - The DIO channel is configured as an input at the time when the DO
 node is called.

For an example of the recommended way to use the AI, AO , and DIO subsystems, refer to the
 NI 9381 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9381\NI 9381 Advanced IO\NI
 9381 Advanced IO.lvproj.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9381_2.html language=enus -->
## TOPIC 00021: Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9381_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9381_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO Node, and Set Output Data method calls. Failing to follow these guidelines may result in lost data points for DO Node calls or Set Output Data method calls when either of them are made from inside a single-

### Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO
 Node, and Set Output Data method calls. Failing to follow these
 guidelines may result in lost data points for DO Node calls or Set Output Data method
 calls when either of them are made from inside a single-cycle Timed Loop.

- Use a single I/O Node to access AI and AO operations to ensure proper sequencing.
- Do not run the Set Output Enable method when an AI, AO, or DO subsystems is
 active.
- Do not perform the following operations concurrently:
  - AI Node call
  - AO Node call
  - Set Output Enable method call
  - Automatic line direction change when a DO call is made under the following
 conditions:
    - The call is made from outside of a single-cycle Timed Loop.
    - The Allow programmatic DIO line direction 
 checkbox is enabled in the C Series Module
 Properties dialog box.
    - The DIO channel is configured as an input at the time when the DO
 node is called.

For an example of the recommended way to use the AI, AO , and DIO subsystems, refer to the
 NI 9381 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9381\NI 9381 Advanced IO\NI
 9381 Advanced IO.lvproj.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9381_3.html language=enus -->
## TOPIC 00022: Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9381_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9381_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO Node, and Set Output Data method calls. Failing to follow these guidelines may result in lost data points for DO Node calls or Set Output Data method calls when either of them are made from inside a single-

### Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO
 Node, and Set Output Data method calls. Failing to follow these
 guidelines may result in lost data points for DO Node calls or Set Output Data method
 calls when either of them are made from inside a single-cycle Timed Loop.

- Use a single I/O Node to access AI and AO operations to ensure proper sequencing.
- Do not run the Set Output Enable method when an AI, AO, or DO subsystems is
 active.
- Do not perform the following operations concurrently:
  - AI Node call
  - AO Node call
  - Set Output Enable method call
  - Automatic line direction change when a DO call is made under the following
 conditions:
    - The call is made from outside of a single-cycle Timed Loop.
    - The Allow programmatic DIO line direction 
 checkbox is enabled in the C Series Module
 Properties dialog box.
    - The DIO channel is configured as an input at the time when the DO
 node is called.

For an example of the recommended way to use the AI, AO , and DIO subsystems, refer to the
 NI 9381 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9381\NI 9381 Advanced IO\NI
 9381 Advanced IO.lvproj.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9381_4.html language=enus -->
## TOPIC 00023: Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9381_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9381_4.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO Node, and Set Output Data method calls. Failing to follow these guidelines may result in lost data points for DO Node calls or Set Output Data method calls when either of them are made from inside a single-

### Avoiding Timing Uncertainty with the NI 9381 (FPGA Interface)

Follow the guidelines below to avoid introducing timing uncertainty into AI node, AO Node, DO
 Node, and Set Output Data method calls. Failing to follow these
 guidelines may result in lost data points for DO Node calls or Set Output Data method
 calls when either of them are made from inside a single-cycle Timed Loop.

- Use a single I/O Node to access AI and AO operations to ensure proper sequencing.
- Do not run the Set Output Enable method when an AI, AO, or DO subsystems is
 active.
- Do not perform the following operations concurrently:
  - AI Node call
  - AO Node call
  - Set Output Enable method call
  - Automatic line direction change when a DO call is made under the following
 conditions:
    - The call is made from outside of a single-cycle Timed Loop.
    - The Allow programmatic DIO line direction 
 checkbox is enabled in the C Series Module
 Properties dialog box.
    - The DIO channel is configured as an input at the time when the DO
 node is called.

For an example of the recommended way to use the AI, AO , and DIO subsystems, refer to the
 NI 9381 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9381\NI 9381 Advanced IO\NI
 9381 Advanced IO.lvproj.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-ni-9683.html language=enus -->
## TOPIC 00024: Avoiding Timing Uncertainty with the NI 9683 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-ni-9683.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-ni-9683.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow these guidelines to avoid introducing timing uncertainty into scanned AI Node and AO Node method calls. Use a single I/O Node to access scanned AI and AO operations to ensure proper sequencing. Do not perform the following operations concurrently: Scanned AI Node call AO Node call Simultane

### Avoiding Timing Uncertainty with the NI 9683 (FPGA Interface)

Follow these guidelines to avoid introducing timing uncertainty into scanned AI Node and AO Node method calls.

- Use a single I/O Node to access scanned AI and AO operations to ensure proper sequencing.
- Do not perform the following operations concurrently:
  - Scanned AI Node call
  - AO Node call

Note

Parent topic:

sbRIO-9683 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=avoiding-timing-uncertainty-with-the-sbrio-96.html language=enus -->
## TOPIC 00025: Avoiding Timing Uncertainty with the sbRIO-9684 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `avoiding-timing-uncertainty-with-the-sbrio-96.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/avoiding-timing-uncertainty-with-the-sbrio-96.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow these guidelines to avoid introducing timing uncertainty into scanned AI Node and AO Node method calls. Use a single I/O Node to access scanned AI and AO operations to ensure proper sequencing. Do not perform the following operations concurrently: 664 – Scanned AI Node call – AO Nod

### Avoiding Timing Uncertainty with the sbRIO-9684 (FPGA Interface)

Follow these guidelines to avoid introducing timing uncertainty into scanned AI Node and AO Node method calls.

- Use a single I/O Node to access scanned AI and AO operations to ensure proper sequencing.
- Do not perform the following operations concurrently:

|  | – Scanned AI Node call |
| --- | --- |
|  | – AO Node call |

Note

Parent topic:

sbRIO-9684 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=baud-rate-advanced.html language=enus -->
## TOPIC 00026: Baud Rate Advanced

- bundle_id: `ni-compactrio`
- source_path: `baud-rate-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/baud-rate-advanced.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 610 Baud Rate Advanced Property Field Data Type Permissions Read While Stopped? Read While Running? Write While Stopped? Write While Running? Tq Write No No Yes No SJW Write No No Yes No TSEG1 Write No No Yes No TSEG2 Write No No Yes No This property allows you to configure the custom CAN baud rate

### Baud Rate Advanced

| Field | Data Type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- | --- |
| Tq |  | Write | No | No | Yes | No |
| SJW |  | Write | No | No | Yes | No |
| TSEG1 |  | Write | No | No | Yes | No |
| TSEG2 |  | Write | No | No | Yes | No |

This property allows you to configure the custom CAN baud rate by setting the nominal bit
 timing and prescaler register of the CAN controller. You can set the following fields.

| Field | Description | Valid Values |
| --- | --- | --- |
| Time quantum (Tq) | Programs the baud rate prescaler | 25 to 12,800 in increments of 0x19 (25 decimal)Note that the actual hardware interpretation of this value is one more than the programmed value |
| Synchronization Jump Width (SJW) | The maximum number of time quanta by which a bit sampling period can be extended or shortened as a result of re-synchronization. | 0 to 127 |
| Time Segment 1 (TSEG1) | The time segment before the sample point. | 1 to 0xFF (1 to 255 decimal) |
| Time Segment 2 (TSEG2) | The time segment after the sample point. | 0 to 0x7F (0 to 127 decimal) |

The time quantum is calculated by the following formula.

Time quantum = (BRP + 1) * 25

- BRP = nominal bit rate prescaler value

Use the custom sample point calculator on the FPGA I/O Properties page under CAN0»Baud
 Rate»<Custom> to determine the values to enter in this field to
 obtain the desired sample point.

Invalid Parameter or Error 65545 is returned if you insert an
 invalid input.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=baud-rate.html language=enus -->
## TOPIC 00027: Baud Rate

- bundle_id: `ni-compactrio`
- source_path: `baud-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/baud-rate.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 609 Data typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesNoEach CAN baud rate selection configures the correspond Baud Rate for the transceiver when in classical CAN mode or when transmitting data before the BRS bit when in CAN FD + BRS mode

### Baud Rate

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

Each CAN baud rate selection configures the correspond Baud Rate for the transceiver when in classical CAN mode or when transmitting data before the BRS bit when in CAN FD + BRS mode. This property must always be set even when I/O Mode is set to CAN FD + BRS as the CAN FD + BRS protocol always has a portion of the frame that transfer in classical CAN mode.

The supported values in kb/s are 5.00, 6.150, 10.00, 12.5, 16.00, 20.00, 25.00, 31.25, 33.33,
 40.00, 50.00, 62.50, 80.00, 83.33, 100.0, 125.0, 160.0, 200.0, 250.0, 400.0, 500.0,
 800.0, and 1000. These bit fields are selected to create the desired baud rate with a
 default sample point of 87.5 percent.

This property converts the baud rate as selected into corresponds Synchronization Jump Width (SJW), Nominal Bit Rate Prescaler (BRP), Nominal Time Segment Before Sample Point (TSEG1), and Nominal Time Segment After Sample Point (TSEG2).

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=bias-resistors.html language=enus -->
## TOPIC 00028: Bias Resistors

- bundle_id: `ni-compactrio`
- source_path: `bias-resistors.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/bias-resistors.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RS485 transmission line enters an indeterminate state if no nodes are transmitting on it. This indeterminate state can cause the receivers to receive invalid data bits from noise picked up on the cable. To prevent a line from receiving invalid data bits, force the transmission line into a known s

### Bias Resistors

An RS485 transmission line enters an indeterminate state if no nodes are transmitting on it. This
 indeterminate state can cause the receivers to receive invalid data bits from noise
 picked up on the cable.

Note

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=bit-timing.html language=enus -->
## TOPIC 00029: Bit Timing

- bundle_id: `ni-compactrio`
- source_path: `bit-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/bit-timing.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 543 Bit Timing Property Data typePermissionsWrite while stopped?Write while running?WriteYesNoEach CAN baud rate corresponds to multiple values for two Bit Timing Registers (BTR). The bit fields in these registers are consistent across almost all CAN controllers. This property specifies the baud rat

### Bit Timing

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

Each CAN baud rate corresponds to multiple values for two Bit Timing Registers (BTR). The bit fields in these registers are consistent across almost all CAN controllers. This property specifies the baud rate as values for the Bit Timing Registers. The least significant byte is BTR0, and the most significant byte is BTR1.

The default value for this property comes from Module Configuration. The Baud
 Rate property is converted to commonly used BTR values, or you can
 specify BTR values directly in the CAN Advanced Port Configuration
 dialog.

For information on CAN Bit Timing Registers, refer to the Philips SJA1000 standalone CAN
 controller datasheet. This document is available for download on
 www.nxp.com.

Parent topic:

I/O Properties for CAN Modules

Related concepts:

- Module Configuration
- Advanced CAN Port Properties

<!--NI_TOPIC bundle=ni-compactrio path=building-and-troubleshooting-an-application.html language=enus -->
## TOPIC 00030: Building and Troubleshooting a CompactRIO Embedded Application

- bundle_id: `ni-compactrio`
- source_path: `building-and-troubleshooting-an-application.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/building-and-troubleshooting-an-application.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### Building and Troubleshooting a CompactRIO
 Embedded Application

- [CompactRIO Interface Methods (FPGA Interface)](compactrio-interface-methods-fpga-interface.html)
- [Converting the Temperature of a CompactRIO Chassis, Ethernet RIO Chassis, MXIe-RIO Chassis, or a Single-Board RIO Device (FPGA Interface)](converting-the-temperature-of-a-compactrio-ch.html)
- [Synchronizing FPGA VIs with the NI Scan Engine (FPGA Interface)](synchronizing-fpga-vis-with-the-ni-scan-engin.html)
- [FPGA Interface C API](fpga-interface-c-api.html)
- [Synchronizing Multiple C Series Modules](synchronizing-multiple-cseriies-mods.html)
- [Using C Series Modules in a LabVIEW Project](using-c-series-modules-in-a-labview-project.html)
- [Configuring the C Series Module Data Rate (FPGA Interface)](configuring-the-c-series-module-data-rate-fpg.html#GUID-F8CB108B-E7F8-4884-821C-2650962A2D34)
- [Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)](simultaneously-reading-from-or-writing-to-mul.html)
- [Reading from C Series Channels](reading-from-c-series-channels.html#GUID-343DDBD7-2917-4DD0-9052-0099A9341296)
- [Writing to C Series Channels](writing-to-c-series-channels.html#GUID-667770A0-6894-4B42-ACF1-939BD7B813FF)
- [Configuring the cRIO I/O Node Name Control (FPGA Module)](configuring-the-crio-i-o-node-name-control-fp.html)
- [Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)](understanding-power-on-and-startup-output-sta.html)
- [Supporting External Data Value References](supporting-external-data-value-references.html)
- [Configuring the Host Memory Buffer](configuring-the-host-memory-buffer.html)

Parent topic:

NI CompactRIO Device Drivers

<!--NI_TOPIC bundle=ni-compactrio path=c-series-drive-interface-modules.html language=enus -->
## TOPIC 00031: C Series Motor Drive Interface Modules

- bundle_id: `ni-compactrio`
- source_path: `c-series-drive-interface-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/c-series-drive-interface-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 594 C Series Motor Drive Interface Modules Motion Module Description NI-9512 Stepper, 1-Axis, Single Encoder C Series Motor Drive Interface Module NI-9514 Servo, 1-Axis, Single Encoder C Series Motor Drive Interface Module NI-9516 Servo, 1-Axis, Dual Encoder C Series Motor Drive Interface Module Use

### C Series Motor Drive Interface Modules

| Motion Module | Description |
| --- | --- |
| NI-9512 | Stepper, 1-Axis, Single Encoder C Series Motor Drive Interface Module |
| NI-9514 | Servo, 1-Axis, Single Encoder C Series Motor Drive Interface Module |
| NI-9516 | Servo, 1-Axis, Dual Encoder C Series Motor Drive Interface Module |

Use the NI-9512/9514/9516 drive interface modules in Scan Interface
 Mode.

Parent topic:

Motion Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=c-series-drive-modules.html language=enus -->
## TOPIC 00032: C Series Drive Motion Modules

- bundle_id: `ni-compactrio`
- source_path: `c-series-drive-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/c-series-drive-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 573 C Series Drive Motion Modules Motion Module Description NI-9501 Bipolar Chopper Stepper C Series Drive Motion Module NI-9502 Brushless Servo C Series Motor Drive Module NI-9503 PWM Stepper C Series Motor Drive Module NI-9505 PWM Stepper C Series Motor Drive Module Use the NI 9501/9502/9503/9505

### C Series Drive Motion Modules

| Motion Module | Description |
| --- | --- |
| NI-9501 | Bipolar Chopper Stepper C Series Drive Motion Module |
| NI-9502 | Brushless Servo C Series Motor Drive Module |
| NI-9503 | PWM Stepper C Series Motor Drive Module |
| NI-9505 | PWM Stepper C Series Motor Drive Module |

Use the NI 9501/9502/9503/9505 motor drive modules in FPGA Interface
 Mode.

Parent topic:

Motion Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=c-series-module-ids.html language=enus -->
## TOPIC 00033: C Series Module IDs

- bundle_id: `ni-compactrio`
- source_path: `c-series-module-ids.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/c-series-module-ids.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Module ID property with the FPGA I/O Property Node to read the IDs associated with C Series modules. You also can wire a reference to a module in Scan Interface mode to a generic-class property node in a VI block diagram, and select the ProductID property to read the ID programmatica

### C Series Module IDs

You can use the Module ID property with the FPGA I/O Property Node to read
 the IDs associated with C Series modules. You also can wire a reference to a module in
 Scan Interface mode to a generic-class property node in a VI block diagram, and select
 the ProductID property to read the ID programmatically. Note that
 the ProductID output will be displayed in decimal by default, and
 the following IDs are in hexadecimal. By ID

| ID | Module |
| --- | --- |
| 0x709C | NI 9435 |
| 0x709D | NI 9411 |
| 0x709E | NI 9423 |
| 0x709F | NI 9421 with screw terminal |
| 0x70A0 | NI 9474 |
| 0x70A1 | NI 9472 with screw terminal |
| 0x70A2 | NI 9481 |
| 0x70A3 | NI 9211 |
| 0x70A4 | NI 9201 |
| 0x70A5 | NI 9221 |
| 0x70A6 | NI 9215 with screw terminal |
| 0x70A7 | NI 9263 |
| 0x7129 | NI 9203 |
| 0x712A | NI 9205 with DSUB |
| 0x712B | NI 9217 |
| 0x712C | NI 9265 |
| 0x712E | NI 9421 with DSUB |
| 0x712F | NI 9425 |
| 0x7130 | NI 9401 |
| 0x7131 | NI 9403 |
| 0x7132 | NI 9472 with DSUB |
| 0x7133 | NI 9476 |
| 0x7135 | NI 9215 with BNC |
| 0x714F | NI 9853 |
| 0x71A1 | NI 9201 with DSUB |
| 0x71A2 | NI 9221 with DSUB |
| 0x71C2 | NI 9239 with screw terminal |
| 0x71C3 | NI 9237 with RJ-50 |
| 0x71C4 | NI 9204 with spring terminal |
| 0x71CA | NI 9422 |
| 0x71CB | NI 9477 |
| 0x71EA | NI 9205 with spring terminal |
| 0x71EB | NI 9206 |
| 0x71ED | NI 9505 |
| 0x71F3 | NI 9852 |
| 0x71F6 | NI 9485 |
| 0x72B5 | NI 9234 |
| 0x72F6 | NI 9264 |
| 0x72FD | NI 9229 with screw terminal |
| 0x7304 | NI 9375 |
| 0x7305 | NI 9870 |
| 0x7306 | NI 9871 |
| 0x730C | NI 9219 |
| 0x731A | NI 9478 |
| 0x7328 | NI 9402 |
| 0x732A | NI 9235 |
| 0x732B | NI 9236 |
| 0x736A | NI 9426 |
| 0x7367 | NI 9239 with BNC |
| 0x7368 | NI 9229 with BNC |
| 0x7377 | NI 9475 |
| 0x7383 | NI 9225 with screw terminal |
| 0x73A4 | NI 9237 with DSUB |
| 0x73E0 | NI 9220 with spring terminal |
| 0x7408 | NI 9225E |
| 0x7409 | NI 9481E |
| 0x740A | NI 9211E |
| 0x740B | NI 9203E |
| 0x740C | NI 9403E |
| 0x740D | NI 9215E |
| 0x7415 | NI 9269 with screw terminal |
| 0x7416 | NI 9227 with screw terminal |
| 0x741C | NI 9239E |
| 0x741D | NI 9229E |
| 0x741E | NI 9263E |
| 0x741F | NI 9237E |
| 0x743A | NI 9213E |
| 0x743B | NI 9478E |
| 0x743F | NI 9870E |
| 0x7440 | NI 9871E |
| 0x7441 | NI 9219E |
| 0x7442 | NI 9265E |
| 0x7445 | NI 9222 with screw terminal |
| 0x7446 | NI 9222E |
| 0x7447 | NI 9264E |
| 0x7449 | NI 9213 |
| 0x744B | NI 9205E |
| 0x744C | NI 9227E |
| 0x744D | NI 9269E |
| 0x745D | NI 9215E with BNC |
| 0x747A | NI 9375 with DSUB |
| 0x749B | NI 9201E with screw terminal |
| 0x749C | NI 9221E with screw terminal |
| 0x749D | NI 9201E with DSUB |
| 0x749E | NI 9221E with DSUB |
| 0x74A1 | NI 9505E |
| 0x74AA | NI 9207E with DSUB |
| 0x74AB | NI 9208E with DSUB |
| 0x74AC | NI 9208 with DSUB |
| 0x74AD | NI 9207 with DSUB |
| 0x74EC | NI 9223 |
| 0x74ED | NI 9223E |
| 0x74EE | NI 9214 |
| 0x753F | NI 9232 with screw terminal |
| 0x7615 | NI 9220 with DSUB |
| 0x7642 | NI 9381 |
| 0x76E3 | NI 9482 |
| 0x76E8 | NI 9244 |
| 0x7733 | NI 9222 with BNC |
| 0x7734 | NI 9223 with BNC |
| 0x7750 | NI 9238 with screw terminal |
| 0x77EA | NI 9250 |
| 0x77B8 | NI 9247 |
| 0x77C5 | NI 9344 |
| 0x77CC | NI 9230 with screw terminal |
| 0x77E3 | NI 9246 |
| 0x77E9 | NI 9251 |
| 0x777E | NI 9361 |
| 0x7786 | NI 9260 with BNC |
| 0x778C | NI 9260 with mini XLR |
| 0x780D | NI 9224 |
| 0x780E | NI 9228 |
| 0x7827 | NI 9770 |
| 0x7866 | NI 9232 with BNC |
| 0x7867 | NI 9230 with BNC |
| 0x7889 | NI 9775 |
| 0x788A | NI 9202 with DSUB |
| 0x788C | NI 9202 with spring terminal |
| 0x788F | NI 9266 |
| 0x78B1 | NI 9210 |
| 0x78B6 | NI 9262 with DSUB |
| 0x7900 | NI 9476 with spring terminal |
| 0x7930 | NI 9231 |
| 0x79C4 | NI 9253 |
| 0x79C8 | NI 9252 with screw terminal |
| 0x79CA | NI 9252 with DSUB |
| 0x7A59 | NI 9470 |
| 0x7A5E | NI 9326 |
| 0x7B3B | NI 9204 with DSUB |
| 0x7B45 | NI 9222 with snap in terminal |
| 0x7B47 | NI 9223 with snap in terminal |
| 0x7B49 | NI 9225 with snap in terminal |
| 0x7B4B | NI 9227 with snap in terminal |
| 0x7B4D | NI 9230 with snap in terminal |
| 0x7B4F | NI 9232 with snap in terminal |
| 0x7B51 | NI 9238 with snap in terminal |
| 0x7B53 | NI 9269 with snap in terminal |
| 0x7B55 | NI 9229 with snap in terminal |
| 0x7B57 | NI 9239 with snap in terminal |
| 0x7B5C | NI 9320 with spring terminal |
| 0x7B5D | NI 9320 with DSUB |

| Module | ID |
| --- | --- |
| NI 9201 | 0x70A4 |
| NI 9201 with DSUB | 0x71A1 |
| NI 9201E with DSUB | 0x749D |
| NI 9201E with screw terminal | 0x749B |
| NI 9202 with DSUB | 0x788A |
| NI 9202 with spring terminal | 0x788C |
| NI 9203 | 0x7129 |
| NI 9203E | 0x740B |
| NI 9204 with DSUB | 0x7B3B |
| NI 9204 with spring terminal | 0x71C4 |
| NI 9205 with DSUB | 0x712A |
| NI 9205 with spring terminal | 0x71EA |
| NI 9205E | 0x744B |
| NI 9206 | 0x71EB |
| NI 9207 with DSUB | 0x74AD |
| NI 9207E with DSUB | 0x74AA |
| NI 9208 with DSUB | 0x74AC |
| NI 9208E with DSUB | 0x74AB |
| NI 9210 | 0x78B1 |
| NI 9211 | 0x70A3 |
| NI 9211E | 0x740A |
| NI 9213 | 0x7449 |
| NI 9213E | 0x743A |
| NI 9214 | 0x74EE |
| NI 9215 with BNC | 0x7135 |
| NI 9215 with screw terminal | 0x70A6 |
| NI 9215E with BNC | 0x745D |
| NI 9215E with screw terminal | 0x740D |
| NI 9217 | 0x712B |
| NI 9219 | 0x730C |
| NI 9219E | 0x7441 |
| NI 9220 with spring terminal | 0x73E0 |
| NI 9220 with DSUB | 0x7615 |
| NI 9221 | 0x70A5 |
| NI 9221 with DSUB | 0x71A2 |
| NI 9221E with DSUB | 0x749E |
| NI 9221E with screw terminal | 0x749C |
| NI 9221E with screw terminal | 0x749C |
| NI 9222 with BNC | 0x7733 |
| NI 9222 with screw terminal | 0x7445 |
| NI 9222 with snap in terminal | 0x7B45 |
| NI 9222E | 0x7446 |
| NI 9223 with BNC | 0x7734 |
| NI 9223 with screw terminal | 0x74EC |
| NI 9223 with snap in terminal | 0x7B47 |
| NI 9223E | 0x74ED |
| NI 9224 | 0x780D |
| NI 9225 with screw terminal | 0x7383 |
| NI 9225E | 0x7408 |
| NI 9225 with snap in terminal | 0x7B49 |
| NI 9227 with screw terminal | 0x7416 |
| NI 9227 with snap in terminal | 0x7B4B |
| NI 9227E | 0x744C |
| NI 9228 | 0x780E |
| NI 9229 with screw terminal | 0x72FD |
| NI 9229E | 0x741D |
| NI 9229 with BNC | 0x7368 |
| NI 9229 with snap in terminal | 0x7B55 |
| NI 9230 with BNC | 0x7867 |
| NI 9230 with screw terminal | 0x77CC |
| NI 9230 with snap in terminal | 0x7B4D |
| NI 9231 | 0x7930 |
| NI 9232 with BNC | 0x7866 |
| NI 9232 with screw terminal | 0x753F |
| NI 9232 with snap in terminal | 0x7B4F |
| NI 9234 | 0x72B5 |
| NI 9235 | 0x732A |
| NI 9236 | 0x732B |
| NI 9237 with DSUB | 0x73A4 |
| NI 9237 with RJ-50 | 0x71C3 |
| NI 9237E | 0x741F |
| NI 9238 with screw terminal | 0x7750 |
| NI 9238 with snap in terminal | 0x7B51 |
| NI 9239 with screw terminal | 0x71C2 |
| NI 9239E | 0x741C |
| NI 9239 with BNC | 0x7367 |
| NI 9239 with snap in terminal | 0x7B57 |
| NI 9244 | 0x76E8 |
| NI 9246 | 0x77E3 |
| NI 9247 | 0x77B8 |
| NI 9250 | 0x77EA |
| NI 9251 | 0x77E9 |
| NI 9252 with screw terminal | 0x79C8 |
| NI 9252 with DSUB | 0x79CA |
| NI 9253 | 0x79C4 |
| NI 9260 with BNC | 0x7786 |
| NI 9260 with mini XLR | 0x778C |
| NI 9262 with DSUB | 0x78B6 |
| NI 9263 | 0x70A7 |
| NI 9263E | 0x741E |
| NI 9264 | 0x72F6 |
| NI 9264E | 0x7447 |
| NI 9265 | 0x712C |
| NI 9265E | 0x7442 |
| NI 9266 | 0x788F |
| NI 9269 with screw terminal | 0x7415 |
| NI 9269 with snap in terminal | 0x7B53 |
| NI 9269E | 0x744D |
| NI 9320 with spring terminal | 0x7B5C |
| NI 9320 with DSUB | 0x7B5D |
| NI 9326 | 0x7A5E |
| NI 9344 | 0x77C5 |
| NI 9361 | 0x777E |
| NI 9375 | 0x7304 |
| NI 9375 with DSUB | 0x747A |
| NI 9381 | 0x7642 |
| NI 9401 | 0x7130 |
| NI 9402 | 0x7328 |
| NI 9403 | 0x7131 |
| NI 9403E | 0x740C |
| NI 9411 | 0x709D |
| NI 9421 with DSUB | 0x712E |
| NI 9421 with screw terminal | 0x709F |
| NI 9422 | 0x71CA |
| NI 9423 | 0x709E |
| NI 9425 | 0x712F |
| NI 9426 | 0x736A |
| NI 9435 | 0x709C |
| NI 9470 | 0x7A59 |
| NI 9472 with DSUB | 0x7132 |
| NI 9472 with screw terminal | 0x70A1 |
| NI 9474 | 0x70A0 |
| NI 9475 | 0x7377 |
| NI 9476 | 0x7133 |
| NI 9476 with spring terminal | 0x7900 |
| NI 9477 | 0x71CB |
| NI 9478 | 0x731A |
| NI 9478E | 0x743B |
| NI 9481 | 0x70A2 |
| NI 9481E | 0x7409 |
| NI 9482 | 0x76E3 |
| NI 9485 | 0x71F6 |
| NI 9505 | 0x71ED |
| NI 9505E | 0x74A1 |
| NI 9770 | 0x7827 |
| NI 9775 | 0x7889 |
| NI 9852 | 0x71F3 |
| NI 9853 | 0x714F |
| NI 9870 | 0x7305 |
| NI 9870E | 0x743F |
| NI 9871 | 0x7306 |
| NI 9871E | 0x7440 |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=c-series-modules-reference.html language=enus -->
## TOPIC 00034: C Series Module Reference

- bundle_id: `ni-compactrio`
- source_path: `c-series-modules-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/c-series-modules-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use C Series modules with NI CompactRIO Device Drivers in LabVIEW. When programming in FPGA Programming mode, C Series modules support FPGA I/O functions, I/O resources, arbitration options, methods, and properties. When programming in Scan Interface mode, C Series modules support I/O variab

### C Series Module
 Reference

You can use C Series modules with NI CompactRIO Device
 Drivers in LabVIEW.

- When programming in FPGA Programming 
 mode, C Series 
 modules support FPGA I/O functions, I/O resources,
 arbitration options, methods, and properties.
- When programming in Scan Interface 
 mode, C Series 
 modules support I/O variables and properties.

Refer to the C Series module topics for details on specific
 support.

- [C Series Module IDs](c-series-module-ids.html)
- [Analog Input Modules](analog-input-modules.html)
- [Analog Output Modules](analog-output-modules.html)
- [Counter Input Modules](counter-input-modules.html)
- [Digital Input Modules](digital-input-modules.html)
- [Digital Output Modules](digital-output-modules.html)
- [Functional Safety Modules](functional-safety-modules.html)
- [Modular Instruments Modules](modular-instruments-modules.html)

<!--NI_TOPIC bundle=ni-compactrio path=can-input-sbrio.html language=enus -->
## TOPIC 00035: CAN Input

- bundle_id: `ni-compactrio`
- source_path: `can-input-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-input-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for a CAN frame to be received, then return that frame. Complete the following steps to read from a CAN port using CAN Input. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select P

### CAN Input

Wait for a CAN frame to be received, then return that frame.

Complete the following steps to read from a CAN port using CAN Input.

1. Use the Add Targets and Devices dialog box to add the CAN
 module to your CompactRIO configuration. Right-click the CAN module in the
 Project Explorer window and select Properties to specify
 the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under
 My Computer in the Project
 Explorer window, selecting New»FPGA I/O , and
 then adding CAN0 to the FPGA I/O list.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI
 diagram.
4. Right-click the I/O Node and select Select FPGA
 I/O»CAN0 .
5. Right-click the I/O Node and select Change to Read to use the
 I/O node for CAN Input.
6. Right-click the I/O Node and choose Properties to select the
 Data Type .

Start communication on the CAN port prior to using CAN Input. Enable Auto Start in the Module Configuration, or invoke the *Start* method to start communication.

The Input Timeout (ms) of the CAN Advanced Port Configuration dialog box specifies how long to wait for a new frame to be received. If you specify Input Timeout (ms) of 0, the CAN Input node will simply check to see if a new frame has arrived (non-blocking).

CAN Input can store the result of two received packets. Receiving an additional packet without calling CAN Input will cause an overflow error. NI recommends placing CAN Input in a loop that is executed when the device receives a data packet.

Note

Add Element

Select FPGA

Parent topic:

sbRIO-9603/9608/9609/9628/9638/9629 CAN API

#### Properties Dialog

The Data Type selects the type for the CAN frame returned by the CAN Input
 node. The available values are Cluster (default) and
 Array of U32.

The benefits of using the Cluster data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front panel)

The benefit of the Array of U32 data type, and handshaking integers to the
 host VI one at a time, is that it is faster for transfer to/from host VI.

Refer to the *Using Clusters and Arrays in LabVIEW FPGA Application Note* for more
 information on the use of clusters and arrays.

#### Node Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error
 Terminals

#### Node Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error
 Terminals

Input Timeout (ms)

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

x

Data Type

Cluster

| Data Type | Element | Description |
| --- | --- | --- |
|  | Timestamp High, Timestamp Low | Timestamp of when the frame was received. The timestamp is acquired at the end of the CAN frame. The high and low U32 represent a single U64 timestamp. The timestamp is large enough to avoid handling rollover. The timestamp is zero-based (relative). The time starts ticking at zero when CAN communication starts. The resolution is 100 ns. |
|  | Identifier | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). |
|  | Type | Type of frame. Data Frame: 0 Remote Frame: 1 Bus Error: 6 Transceiver Fault: 7 CAN FD Data Frame: 16 CAN FD+BRS Data Frame:24 |
|  | InfoA | Reserved for future use. |
|  | InfoB | Reserved for future use. |
|  | Data Length | For data frames, this provides the number of bytes in Data (0–8 for CAN and 0–64 for CAN FD). For remote frames, this indicates the number of bytes requested. |
|  | Data | For data frames, this provides the data bytes. The array uses a fixed size of 64 bytes. Values above Data Length are not valid and should be ignored. For remote frames, the values contained in Data are not valid and should be ignored. If the Data Type is defined as Array of U32, the CAN frame is represented as an array of U32 values, as shown in the following table. |

| Most significant byte | ... | ... | Least significant byte |
| --- | --- | --- | --- |
| Timestamp (upper U32) |  |  |  |
| Timestamp (lower U32) |  |  |  |
| Identifier |  |  |  |
| Type | InfoA | InfoB | Data Length |
| Data[0] | Data[1] | Data[2] | Data[3] |
| Data[4] | Data[5] | Data[6] | Data[7] |
| Data[8] | Data[9] | Data[10] | Data[11] |
| Data[12] | Data[13] | Data[14] | Data[15] |
| Data[16] | Data[17] | Data[18] | Data[19] |
| Data[20] | Data[21] | Data[22] | Data[23] |
| Data[24] | Data[25] | Data[26] | Data[27] |
| Data[28] | Data[29] | Data[30] | Data[31] |
| Data[32] | Data[33] | Data[34] | Data[35] |
| Data[36] | Data[37] | Data[38] | Data[39] |
| Data[40] | Data[41] | Data[42] | Data[43] |
| Data[44] | Data[45] | Data[46] | Data[47] |
| Data[48] | Data[49] | Data[50] | Data[51] |
| Data[52] | Data[53] | Data[54] | Data[55] |
| Data[56] | Data[57] | Data[58] | Data[59] |
| Data[60] | Data[61] | Data[62] | Data[63] |

In the table above, the meaning of each element is the same as the
 Cluster data type.

<!--NI_TOPIC bundle=ni-compactrio path=can-input.html language=enus -->
## TOPIC 00036: CAN Input

- bundle_id: `ni-compactrio`
- source_path: `can-input.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-input.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for a CAN frame to be received, then return that frame. Complete the following steps to read from a CAN port using CAN Input. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select P

### CAN Input

Wait for a CAN frame to be received, then return that frame.

Complete the following steps to read from a CAN port using CAN Input.

1. Use the Add Targets and Devices dialog box to add the CAN module to your
 CompactRIO configuration. Right-click the CAN module in the Project
 Explorer window and select Properties to specify the configuration
 properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My
 Computer in the Project Explorer window,
 selecting New»FPGA I/O , and then adding CAN»NI
 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or
 CAN»NI 9852»CAN1 (or CAN»NI
 9853»CAN1 ) to the FPGA I/O list.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI
 diagram.
4. Right-click the I/O Node and select Select FPGA I/O»CAN»NI 9852»CAN0 (or Select FPGA I/O»CAN»NI 9853»CAN0 ) or Select FPGA I/O»CAN»NI 9852»CAN1 (or Select FPGA I/O»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Node and select Change to Read to use the I/O node for CAN Input.
6. Right-click the I/O Node and choose Properties to select the Data
 Type .

Start communication on the CAN port prior to using CAN Input. Enable Auto
 Start in the Module Configuration, or invoke the
 Start method to start communication.

The Input Timeout (ms) of the CAN Advanced Port
 Configuration dialog box specifies how long to wait for a new frame to be
 received. If you specify Input Timeout (ms) of 0, the CAN Input
 node will simply check to see if a new frame has arrived (non-blocking).

Arbitration

Note

Add
 Element

Select FPGA

Parent topic:

Controller Area Network (CAN) Interface Module Reference

Related concepts:

- Module Configuration
- Advanced CAN Port Properties
- Arbitration
- Error Terminals

#### Properties Dialog

The Data Type selects the type for the CAN frame returned by the CAN Input node. The available values are Cluster (default) and Array of 6 U32.

The benefits of using the Cluster data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front panel)

The benefits of the Array of 6 U32 data type, and handshaking integers to the host VI one at a time, are:

- Faster for transfer to/from host VI
- Fewer FPGA gates

Refer to the *Using Clusters and Arrays in LabVIEW FPGA Application Note* for more
 information on the use of clusters and arrays.

#### Node Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error
 Terminals

#### Node Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error
 Terminals

Input Timeout (ms)

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

x

Data Type

Cluster

| Data Type | Element | Description |
| --- | --- | --- |
|  | Timestamp High, Timestamp Low | Timestamp of when the frame was received. The timestamp is acquired at the end of the CAN frame. The high and low U32 represent a single U64 timestamp. The timestamp is large enough to avoid handling rollover. The timestamp is zero-based (relative). The time starts ticking at zero when CAN communication starts. The resolution is 100 ns. |
|  | Identifier | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). |
|  | Type | Type of frame. Data Frame: 0 Remote Frame: 1 Bus Error: 6 Transceiver Fault: 7 |
|  | InfoA | Reserved for future use. |
|  | InfoB | Reserved for future use. |
|  | Data Length | For data frames, this provides the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. |
|  | Data | For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. For remote frames, the values contained in Data are not valid and should be ignored. If the Data Type is defined as Array of 6 U32, the CAN frame is represented as an array of 6 U32 values, as shown in the following table. |

| Most significant byte | ... | ... | Least significant byte |
| --- | --- | --- | --- |
| Timestamp (upper U32) |  |  |  |
| Timestamp (lower U32) |  |  |  |
| Identifier |  |  |  |
| Type | InfoA | InfoB | DataLength |
| Data[0] | Data[1] | Data[2] | Data[3] |
| Data[4] | Data[5] | Data[6] | Data[7] |

In the table above, the meaning of each element is the same as the
 Cluster data type.

<!--NI_TOPIC bundle=ni-compactrio path=can-module-configuration.html language=enus -->
## TOPIC 00037: CAN Module Configuration

- bundle_id: `ni-compactrio`
- source_path: `can-module-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-module-configuration.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### CAN Module Configuration

- [Adding Targets and Devices](add-targets-and-devices.html)
- [Module Configuration](module-configuration.html)
- [Advanced CAN Port Properties](advanced-can-port-properties.html)

Parent topic:

Controller Area Network (CAN) Interface Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=can-module-properties.html language=enus -->
## TOPIC 00038: CAN Module Properties

- bundle_id: `ni-compactrio`
- source_path: `can-module-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-module-properties.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Module tab provides configuration properties that apply to all CAN ports on the module. Module Clock Performance of the I/O, methods, and properties is determined by the speed of communication between LabVIEW FPGA and the module. On a CompactRIO Reconfigurable Embedded system, communication spee

### CAN Module Properties

The Module tab provides configuration properties that apply to all
 CAN ports on the module.

#### Module Clock

- On a CompactRIO Reconfigurable Embedded system, communication speed is
 limited to 20 MHz . Note To write CAN applications with consistent performance regardless of
 LabVIEW FPGA target, use the Module Clock
 property to select 10MHz. This setting is compatible
 with the CompactRIO R Series Expansion system.
- On a CompactRIO R Series Expansion system, communication speed is limited to
 10 MHz . This is the only setting
 available in the Module Clock property.

Parent topic:

Module Configuration

<!--NI_TOPIC bundle=ni-compactrio path=can-modules-reference.html language=enus -->
## TOPIC 00039: Controller Area Network (CAN) Interface Module Reference

- bundle_id: `ni-compactrio`
- source_path: `can-modules-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-modules-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 526 C Series CAN Interface Modules CAN Interface Module Description NI-9852 2-Port, Low-Speed/Fault Tolerant C Series CAN Interface Module NI-9853 2-Port, High-Speed C Series CAN Interface Module In this document, CAN module refers to the NI-9852 and NI-9853 C Series modules. Within CompactRIO softw

### Controller Area Network (CAN) Interface Module
 Reference

| CAN Interface Module | Description |
| --- | --- |
| NI-9852 | 2-Port, Low-Speed/Fault Tolerant C Series CAN Interface Module |
| NI-9853 | 2-Port, High-Speed C Series CAN Interface Module |

In this document, *CAN module* refers to the NI-9852 and NI-9853 C Series modules.
 Within CompactRIO software, the NI-9852 is designated as cRIO-9852, and the NI-9853 is
 designated as cRIO-9853.

- [C Series CAN Interface Modules](can-modules.html)
- [CAN Module Configuration](can-module-configuration.html)
- [CAN Input](can-input.html#GUID-76AAC511-49E6-4F09-B9DD-54F8F68D8D75)
- [CAN Output](can-output.html#GUID-C5D81067-80F2-4DA0-B655-FB129EB46A6D)
- [I/O Methods for CAN Modules](io-methods-can.html)
- [I/O Properties for CAN Modules](i-o-properties-can.html)
- [Module Properties](module-properties.html#GUID-C28BD621-6A83-4562-81E1-F0C886DF0C1A)
- [Arbitration](arbitration.html)
- [Error Terminals](error-terminals.html)
- [Converting Frames To and From Channels (Signals)](converting-frames-to-and-from-channels-signal.html)

<!--NI_TOPIC bundle=ni-compactrio path=can-modules.html language=enus -->
## TOPIC 00040: C Series CAN Interface Modules

- bundle_id: `ni-compactrio`
- source_path: `can-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 527 CAN Interface Modules for CompactRIO CAN Interface Module Description NI-9852 2-Port, Low-Speed/Fault Tolerant C Series CAN Interface Module NI-9853 2-Port, High-Speed C Series CAN Interface Module

### C Series CAN Interface Modules

| CAN Interface Module | Description |
| --- | --- |
| NI-9852 | 2-Port, Low-Speed/Fault Tolerant C Series CAN Interface Module |
| NI-9853 | 2-Port, High-Speed C Series CAN Interface Module |

Parent topic:

Controller Area Network (CAN) Interface Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=can-output-sbrio.html language=enus -->
## TOPIC 00041: CAN Output

- bundle_id: `ni-compactrio`
- source_path: `can-output-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-output-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Write a CAN frame to be transmitted. Complete the following steps to write to a CAN port using CAN Output. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the

### CAN Output

Write a CAN frame to be transmitted.

Complete the following steps to write to a CAN port using CAN Output.

1. Use the Add Targets and Devices dialog box to add the CAN module to your
 CompactRIO configuration. Right-click the CAN module in the Project
 Explorer window and select Properties to specify the configuration
 properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My
 Computer in the Project Explorer window,
 selecting New»FPGA I/O , and then adding
 CAN0 to the FPGA I/O list. Refer to New FPGA I/O dialog
 box (FPGA Module) for more information about creating and adding FPGA I/O to your
 CompactRIO configuration.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI diagram.
4. Right-click the I/O Node and select Select FPGA I/O»CAN0 .
5. Right-click the I/O Node and select Change to Write to use the I/O node for CAN Output.
6. Right-click the I/O Node and choose Properties to select the Data Type.

Start communication on the CAN port prior to using CAN Output. Enable Auto Start in the Module Configuration, or invoking the *Start* method to start communication.

The communication path from LabVIEW FPGA to the CAN port on the module is implemented as a FIFO. The CAN Output node waits for an available element in the FIFO, then writes the frame to the FIFO. If no other CAN frame exists in the FIFO, the CAN frame will begin to transmit immediately.

CAN Output does not wait for the requested transmit to complete on the network (acknowledgment). Call CAN Output followed by *Wait on Transmit Complete* (I/O Method) if you want to transmit CAN frames one at a time.

Write multiple frames to the output FIFO if you want to transmit CAN frames as fast as possible. The CAN module will submit these frames to the TCAN4550 controller as fast as possible.

When the output FIFO is full, the CAN Output node waits for an element to become available, then writes the frame to the FIFO. The Output Timeout (ms) of the CAN Advanced Port Configuration dialog box specifies how long to wait for a new element to become available, which occurs when a frame from a previous CAN Output transmits successfully onto the network. If you specify Output Timeout (ms) of 0, the CAN Output node returns an error status of TRUE (error) if a new element is not available (non-blocking). When an error is returned, you must attempt CAN Output of the same frame again at a later time.

Output Timeout (ms)

Note

Add Element

Select FPGA I/O

Note

Parent topic:

sbRIO-9603/9608/9609/9628/9638/9629 CAN API

#### Properties Dialog

Selects the Data Type for the CAN frame written to the CAN Input
 node. The available values are Cluster (default) and
 Array of U32.

The benefits of using the Cluster data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front
 panel)

The benefits of the Array of U32 data type, and handshaking
 integers to the host VI one at a time, are:

- Faster for transfer to/from host VI
- Fewer FPGA gates

Refer to the *Using Clusters and Arrays in LabVIEW FPGA Application Note* for
 more information on the use of clusters and arrays.

#### Node Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

x

Data Type

Cluster

| Data Type | Element | Description |
| --- | --- | --- |
|  | Timestamp High, | Ignored. The transmit request always occurs as soon as possible (not timed). |
|  | Timestamp Low | Ignored. The transmit request always occurs as soon as possible (not timed). |
|  | Identifier | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). |
|  | Type | Type of frame: Data Frame: 0 Remote Frame: 1 CAN FD Data Frame: 16 CAN FD+BRS Data Frame:24 |
|  | InfoA | Reserved for future use. |
|  | InfoB | Reserved for future use. |
|  | Data Length | For data frames, this provides the number of bytes in Data (0–8 for CAN and 0–64 for CAN FD). For remote frames, this indicates the number of bytes requested. |
|  | Data | For data frames, this provides the data bytes. The array uses a fixed size of 64 bytes. If the Data Type is defined as Array of U32, the CAN frame is represented as an array of U32 values, as shown in the following table. |

| Most significant byte | ... | ... | Least significant byte |
| --- | --- | --- | --- |
| Timestamp (upper U32) |  |  |  |
| Timestamp (lower U32) |  |  |  |
| Identifier |  |  |  |
| Type | InfoA | InfoB | Data Length |
| Data[0] | Data[1] | Data[2] | Data[3] |
| Data[4] | Data[5] | Data[6] | Data[7] |
| Data[8] | Data[9] | Data[10] | Data[11] |
| Data[12] | Data[13] | Data[14] | Data[15] |
| Data[16] | Data[17] | Data[18] | Data[19] |
| Data[20] | Data[21] | Data[22] | Data[23] |
| Data[24] | Data[25] | Data[26] | Data[27] |
| Data[28] | Data[29] | Data[30] | Data[31] |
| Data[32] | Data[33] | Data[34] | Data[35] |
| Data[36] | Data[37] | Data[38] | Data[39] |
| Data[40] | Data[41] | Data[42] | Data[43] |
| Data[44] | Data[45] | Data[46] | Data[47] |
| Data[48] | Data[49] | Data[50] | Data[51] |
| Data[52] | Data[53] | Data[54] | Data[55] |
| Data[56] | Data[57] | Data[58] | Data[59] |
| Data[60] | Data[61] | Data[62] | Data[63] |

In the table above, the meaning of each element is the same as the
 Cluster data type.

#### Node Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error
 Terminals

Output Timeout (ms)

<!--NI_TOPIC bundle=ni-compactrio path=can-output.html language=enus -->
## TOPIC 00042: CAN Output

- bundle_id: `ni-compactrio`
- source_path: `can-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-output.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Write a CAN frame to be transmitted. Complete the following steps to write to a CAN port using CAN Output. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the

### CAN Output

Write a CAN frame to be transmitted.

Complete the following steps to write to a CAN port using CAN Output.

1. Use the Add Targets and Devices dialog box to add the CAN module to your
 CompactRIO configuration. Right-click the CAN module in the Project Explorer window
 and select Properties to specify the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My
 Computer in the Project Explorer window, selecting
 New»FPGA I/O , and then adding CAN»NI
 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or
 CAN»NI 9852»CAN1 (or CAN»NI 9853»CAN1 ) to
 the FPGA I/O list. Refer to New FPGA I/O dialog box (FPGA Module) for more information about
 creating and adding FPGA I/O to your CompactRIO configuration.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI
 diagram.
4. Right-click the I/O Node and select Select FPGA I/O»CAN»NI 9852»CAN0 (or Select FPGA I/O»CAN»NI 9853»CAN0 ) or Select FPGA I/O»CAN»NI 9852»CAN1 (or Select FPGA I/O»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Node and select Change to Write to use the I/O node for CAN Output.
6. Right-click the I/O Node and choose Properties to select the Data Type.

Start communication on the CAN port prior to using CAN Output. To start communication, enable
 Auto Start in the Module Configuration, or invoke the
 Start method.

The communication path from LabVIEW FPGA to the CAN port on the module is implemented as a FIFO. The CAN Output node waits for an available element in the FIFO, then writes the frame to the FIFO. If no other CAN frame exists in the FIFO, the CAN frame will begin to transmit immediately.

CAN Output does not wait for the requested transmit to complete on the network (acknowledgement).
 Call CAN Output followed by Wait on Transmit Complete
 (I/O Method) if you want to transmit CAN frames one at a time.

Write multiple frames to the output FIFO if you want to transmit CAN frames as fast as possible.
 The CAN module submits these frames to the SJA1000 controller as fast as possible, thus
 generating close to 100% busload.

When the output FIFO is full, the CAN Output node waits for an element to become available, then
 writes the frame to the FIFO. The Output Timeout (ms) of the
 CAN Advanced Port Configuration dialog box specifies how long to wait
 for a new element to become available, which occurs when a frame from a previous CAN Output
 transmits successfully onto the network. If you specify Output Timeout
 (ms) of 0, the CAN Output node returns an error status of TRUE
 (error) if a new element is not available (non-blocking). When an error is returned, attempt
 CAN Output of the same frame again at a later time.

Output Timeout (ms)

Output Timeout (ms)

Arbitration

Note

Add Element

Select FPGA I/O

Parent topic:

Controller Area Network (CAN) Interface Module Reference

Related concepts:

- Error Terminals
- Module Configuration
- Arbitration

#### Properties Dialog

Selects the Data Type for the CAN frame written to the CAN Input
 node. The available values are Cluster (default) and
 Array of 6 U32.

The benefits of using the Cluster data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front
 panel)

The benefits of the Array of 6 U32 data type, and handshaking
 integers to the host VI one at a time, are:

- Faster for transfer to/from host VI
- Fewer FPGA gates

Refer to the *Using Clusters and Arrays in LabVIEW FPGA Application Note* for
 more information on the use of clusters and arrays.

#### Node Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error
 Terminals

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

x

Data Type

Cluster

| Data Type | Element | Description |
| --- | --- | --- |
|  | Timestamp High | Ignored. The transmit request always occurs as soon as possible (not timed). |
|  | Timestamp Low | Ignored. The transmit request always occurs as soon as possible (not timed). |
|  | Identifier | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). This representation of the CAN identifier is the same as NI-CAN. |
|  | Type | Type of frame. Data Frame: 0 Remote Frame: 1 |
|  | InfoA | Reserved for future use. |
|  | InfoB | Reserved for future use. |
|  | Data Length | For data frames, this provides the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. |
|  | Data | For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. If the Data Type is defined as Array of 6 U32, the CAN frame is represented as an array of 6 U32 values, as shown in the following table. |

| Most significant byte | ... | ... | Least significant byte |
| --- | --- | --- | --- |
| Timestamp (upper U32) |  |  |  |
| Timestamp (lower U32) |  |  |  |
| Identifier |  |  |  |
| Type | InfoA | InfoB | DataLength |
| Data[0] | Data[1] | Data[2] | Data[3] |
| Data[4] | Data[5] | Data[6] | Data[7] |

In the table above, the meaning of each element is the same as the
 Cluster data type.

#### Node Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error
 Terminals

Output Timeout (ms)

<!--NI_TOPIC bundle=ni-compactrio path=can-port-bit-timing.html language=enus -->
## TOPIC 00043: Bit Timing

- bundle_id: `ni-compactrio`
- source_path: `can-port-bit-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-port-bit-timing.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When Specify Baud Rate as Bit Timing Registers is FALSE (unchecked), the baud rate for the CAN port is selected using the Baud Rate in the Module Configuration dialog box. The SJA1000 bit timing registers for the corresponding baud rate are grayed out. When Specify Baud Rate as Bit Timing Registers

### Bit Timing

When Specify Baud Rate as Bit Timing Registers is
 FALSE (unchecked), the baud rate for the CAN port is selected
 using the Baud Rate in the *Module Configuration*
 dialog box. The SJA1000 bit timing registers for the corresponding baud rate are grayed
 out.

When Specify Baud Rate as Bit Timing Registers is
 TRUE (checked), the Baud Rate in the
 Module Configuration dialog box is ignored. Two integer controls
 BTR0 and BTR1 set the baud rate for
 the CAN port.

BTR0

BTR1

Note

Philips SJA1000 standalone CAN controller

www.nxp.com

Parent topic:

Advanced CAN Port Properties

<!--NI_TOPIC bundle=ni-compactrio path=can-port-input-filter-property.html language=enus -->
## TOPIC 00044: Input Filter

- bundle_id: `ni-compactrio`
- source_path: `can-port-input-filter-property.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-port-input-filter-property.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Input Filter selection controls the acceptance filter registers of the SJA1000 CAN controller. The acceptance filter enables the SJA1000 to filter out certain CAN frames so that your FPGA VI can work with reduced overall traffic. The acceptance filter applies only to received frames. The accepta

### Input Filter

The Input Filter selection controls the acceptance filter
 registers of the SJA1000 CAN controller.

The acceptance filter enables the SJA1000 to filter out certain CAN frames so that your
 FPGA VI can work with reduced overall traffic. The acceptance filter applies only to
 received frames. The acceptance filter does not apply to transmitted frames.

The Input Filter selection determines how you specify the
 following filter values in the dialog box:

Receive All

SJA1000 Filter Mode

SJA1000
 Mask

SJA1000 Code

Receive Selected

| Identifier Controls | Description |
| --- | --- |
| ID Format | Selects whether your CAN network uses Standard identifiers (11-bit) or Extended identifiers (29-bit). |
| ID Display | Selects whether to use Decimal or Hexadecimal for the identifiers in the Add control and Selected IDs list. |
| Add From Database | Opens a file dialog from which you can select a CANdb file (.DBC) or an NI-CAN database file (.NCD). When you click the OK button in the file dialog, the identifiers for all messages in the database are added to the Selected IDs. The Add From Database button requires features of NI-CAN 2.3 or higher in order to import identifiers. If you do not have NI-CAN 2.3 or higher installed on your Windows system, the Add From Database button is grayed out. |
| Add | Enter a single identifier using the control to the right, then click this button to add the identifier to the Selected IDs. |
| Delete | Select a single identifier within the Selected IDs list, then click this button to delete that identifier from the list. |
| Delete All | Deletes all identifiers in Selected IDs. |
| Selected IDs | List of identifiers that you have selected using controls to the left. The dialog calculates the SJA1000 filters from this list, and the resulting register values are shown in SJA1000 Filter Mode, SJA1000 Mask, and SJA1000 Code (grayed). If you change the Input Filter from Receive Selected to SJA1000 Format, the register values in SJA1000 Filter Mode, SJA1000 Mask, and SJA1000 Code retain their calculated values. This allows you to use Receive Selected to calculate filters for the identifiers, then change the registers directly for advanced filtering, such as checks for patterns in the data bytes. |
| Number of Unwanted IDs | Given the current filter calculation, this displays the number of identifiers that your FPGA VI will receive which are not listed in Selected IDs. Since the SJA1000 registers filter using bitwise masking, the filter efficiency is rarely 100%. If you use ID Format of Extended, this number can be large due to the 29 total bits used for identifiers. |

SJA1000 Format

SJA1000 Format

Note

Philips SJA1000 standalone CAN
 controller

www.nxp.com

| SJA1000 Format Control | Description |
| --- | --- |
| SJA1000 Filter Mode | Controls the Acceptance Filter Mode bit of the SJA1000 Mode register. Dual (0) specifies use of two filters, and Single (1) specifies use of a single filter. |
| SJA1000 Mask | Controls the SJA1000 Acceptance Mask 0–3 registers. The value is specified as hexadecimal. The least significant byte of the value is stored in register offset 3 (AMR3), the next least significant in offset 2 (AMR2), and so on. |
| SJA1000 Code | Controls the SJA1000 Acceptance Code 0–3 registers. The value is specified as hexadecimal. The least significant byte of the value is stored in register offset 3 (ACR3), the next least significant in offset 2 (ACR2), and so on. |

Parent topic:

Advanced CAN Port Properties

<!--NI_TOPIC bundle=ni-compactrio path=can-port-properties.html language=enus -->
## TOPIC 00045: CAN Port Properties

- bundle_id: `ni-compactrio`
- source_path: `can-port-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-port-properties.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CAN0 and CAN1 tabs provide configuration properties for their respective CAN port. Baud Rate This specifies the baud rate (bit rate) to use for CAN communication. Typical CAN baud rates are listed as kilobits per second (kbps). The default baud rate for the NI 9852 module is 125.0 kbps. 125.0 kb

### CAN Port Properties

The CAN0 and CAN1 tabs provide
 configuration properties for their respective CAN port.

#### Baud Rate

This specifies the baud rate (bit rate) to use for CAN communication. Typical CAN
 baud rates are listed as kilobits per second (kbps).

The default baud rate
 for the NI 9852 module is 125.0 kbps. 125.0
 kbps is the typical baud rate used for low-speed transceivers.

The default baud rate for the NI 9853 module is 500.0
 kbps. 500.0 kbps is the typical baud rate
 used for high-speed transceivers. If you prefer to specify the baud rate as bit
 timing register values, refer to *CAN Advanced Port Configuration*.

#### Auto Start

This Boolean property indicates whether to invoke the
 Start method automatically when the FPGA VI runs. The
 default is TRUE (enabled).

When Auto
 Start is TRUE (enabled), the
 Start method is invoked automatically when the FPGA VI
 runs, and the Stop method is invoked automatically when the
 FPGA VI stops running. This enables your FPGA VI diagram to begin using CAN Input
 and CAN Output nodes without first using an explicit Start
 method.

When Auto Start is FALSE
 (disabled), the Start method is not
 invoked automatically. You must use the Start method in your
 FPGA VI diagram to start communication. The behavior for Stop
 is the same as when Auto Start is TRUE, in
 that the Stop method is invoked automatically when the FPGA
 VI stops running.

#### Listen Only

This Boolean control indicates whether to enable the
 Listen Only feature for passive monitoring of the
 network. The default is FALSE (disabled).

When
 Listen Only is FALSE (disabled), you
 can transmit CAN messages normally using CAN Output. When CAN messages are received,
 those messages are acknowledged.

When Listen Only is
 TRUE (enabled), you cannot transmit CAN messages. When CAN
 messages are received, those messages are not acknowledged. The Philips
 SJA1000 CAN controller enters error passive state when
 Listen Only is enabled. Checking Listen
 Only enables passive monitoring of network traffic, which can be
 useful for debugging scenarios in which only one device exists on the network.

#### LS/FT Termination

The LS/FT Termination control applies to NI 9852 low-speed,
 fault-tolerant modules. This control enables you to set the LS/FT port termination
 to 1 kiloohm or 5 kiloohm.

#### Advanced

The
 Advanced button displays a dialog to configure advanced
 properties for the CAN port. Refer to *CAN Advanced Port Configuration*
 for more information.

Parent topic:

Module Configuration

<!--NI_TOPIC bundle=ni-compactrio path=can-port-timeouts.html language=enus -->
## TOPIC 00046: Timeouts

- bundle_id: `ni-compactrio`
- source_path: `can-port-timeouts.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/can-port-timeouts.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enter a short description of your concept here (optional). Timeouts The Input Timeout (ms) and Output Timeout (ms) properties specify timeout values to use with CAN nodes in the FPGA VI block diagram. Each timeout is a signed 32-bit integer with a resolution of milliseconds, thus allowing a maximum

### Timeouts

Enter a short description of your concept here (optional).

Timeouts

The Input Timeout (ms) and Output Timeout
 (ms) properties specify timeout values to use with CAN nodes in the FPGA
 VI block diagram.

Each timeout is a signed 32-bit integer with a resolution of milliseconds, thus allowing
 a maximum value of approximately 25 days. Special values of 0 (do not
 wait) and –1 (wait indefinitely) are supported.

The CAN Input function waits for a new CAN frame to be received, then returns that frame.
 The Input Timeout (ms) specifies how long to wait for a new frame
 to be received.

If you specify Input Timeout (ms) of 0, the CAN Input node will
 simply check to see if a new frame has arrived (non-blocking). If a new frame exists,
 CAN Input returns the frame with an error status of FALSE (success).
 If no new frame exists, CAN Input returns an error status of TRUE
 (error). Therefore, in order to poll for new frames using an input timeout of 0, you
 must enable Error Terminals for the CAN Input node. When an error
 is returned, you must invoke CAN Input again at a later time to ensure no data is lost.

The communication path from LabVIEW FPGA to the CAN port is implemented as a FIFO. This
 allows multiple frames to be sent to the CAN module for transmit, thus enabling VIs that
 generate full bus load.

When the output FIFO is full, the CAN Output node waits for an element to become
 available, then writes the frame to the FIFO. Output Timeout (ms)
 specifies how long to wait for a new element to become available, which occurs when a
 frame from a previous CAN Output transmits successfully onto the network. If you specify
 Output Timeout (ms) of 0, the CAN Output node returns an
 error status of TRUE (error) if a new element is not available in the FIFO
 (non-blocking). When an error is returned, you must attempt CAN Output of the same frame
 again at a later time.

In addition to the CAN Output node, Output Timeout (ms) also
 applies to most methods and properties. For example, if Output Timeout
 (ms) is 0, the Abort Transmit method returns an error if the output FIFO
 is full. Refer to the *Arbitration* topic for more information on the output
 path from LabVIEW FPGA to the CAN port.

Parent topic:

Advanced CAN Port Properties

<!--NI_TOPIC bundle=ni-compactrio path=comm-state.html language=enus -->
## TOPIC 00047: Comm State

- bundle_id: `ni-compactrio`
- source_path: `comm-state.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/comm-state.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 544 Comm State Property Data type Permissions Read while stopped? Read while running? Write while stopped? Write while running? Read Yes Yes N/A N/A This property describes the current communication state of the CAN controller. The values are: 0: Error Active 1: Error Passive 2: Bus Off Use the Wait

### Comm State

| Data type | Permissions | Read while stopped? | Read while running? | Write while stopped? | Write while running? |
| --- | --- | --- | --- | --- | --- |
|  | Read | Yes | Yes | N/A | N/A |

This property describes the current communication state of the CAN controller.

- 0: Error Active
- 1: Error Passive
- 2: Bus Off

Use the Wait on Comm State Change method to detect changes in this property.

When you initially start communication, the CAN port will begin in the Error Active state as
 specified in the CAN standard (except when Listen Only is
 enabled). After bus errors cause a transition to Error Passive or Bus Off, that state
 will be retained even after you stop communication and restart. Use the
 Reset method to reset back to the Error Active
 state.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=comm-state_2.html language=enus -->
## TOPIC 00048: Comm State

- bundle_id: `ni-compactrio`
- source_path: `comm-state_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/comm-state_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 615 Comm State Property Data type Permissions Read while stopped? Read while running? Write while stopped? Write while running? Read Yes Yes N/A N/A This property describes the current communication state of the CAN controller. The values are: 0: Error Active 1: Error Passive 2: Bus Off Use the Wait

### Comm State

| Data type | Permissions | Read while stopped? | Read while running? | Write while stopped? | Write while running? |
| --- | --- | --- | --- | --- | --- |
|  | Read | Yes | Yes | N/A | N/A |

This property describes the current communication state of the CAN controller.

- 0: Error Active
- 1: Error Passive
- 2: Bus Off

Use the Wait on Comm State Change method to detect changes in this property.

When you initially start communication, the CAN port will begin in the Error Active state as
 specified in the CAN standard (except when Listen Only is
 enabled). After bus errors cause a transition to Error Passive or Bus Off, that state
 will be retained even after you stop communication and restart. Use the
 Reset method to reset back to the Error Active
 state.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-controller-and-chassis-reference.html language=enus -->
## TOPIC 00049: CompactRIO Controller and Chassis Reference

- bundle_id: `ni-compactrio`
- source_path: `compactrio-controller-and-chassis-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-controller-and-chassis-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use CompactRIO controllers and chassis with NI CompactRIO Device Drivers in LabVIEW.

### CompactRIO Controller and Chassis Reference

Use CompactRIO controllers and chassis with NI CompactRIO Device Drivers in
 LabVIEW.

- [CompactRIO Reconfigurable Chassis](compactrio-reconfigurable-chassis.html)
- [NI CompactRIO Controllers](crio-controllers-cseries.html)
- [Ethernet RIO Chassis](enet-rio-chassis.html#GUID-02E15551-498F-407E-848C-71DB81C5A3CE)
- [MXIe-RIO Chassis](mxie-rio-chassis-cseries.html#GUID-52D6234E-B5B4-46A2-A6A2-C6AE68C3049B)

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-device-drivers-and-labview-compati.html language=enus -->
## TOPIC 00050: NI CompactRIO Device Drivers and LabVIEW Compatibility

- bundle_id: `ni-compactrio`
- source_path: `compactrio-device-drivers-and-labview-compati.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-device-drivers-and-labview-compati.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Each version of NI CompactRIO Device Drivers supports the following LabVIEW versions: The following table lists LabVIEW compatibility support. The version of LabVIEW that released with the version of NI CompactRIO Device Drivers The three previous LabVIEW service pack versions For driver versions re

### NI CompactRIO Device
 Drivers and
 LabVIEW Compatibility

Each version of NI CompactRIO Device
 Drivers supports the following
 LabVIEW versions:

- The version of LabVIEW that released with the version of NI CompactRIO Device
 Drivers
- The three previous LabVIEW service pack versions

Note

For driver versions released after February 2017, refer to *NI Driver and
 Development Software Compatibility* in *Related
 information*.

| NI CompactRIO Device Drivers Version | LabVIEW Version Support |
| --- | --- |
| February 2017 | 2017 2016 SP1 2015 SP1 2014 SP1 |
| August 2016 | 2016 2015 SP1 2014 SP1 2013 SP1 |
| February 2016 | 2015 SP1 2014 SP1 2013 SP1 2012 SP1 |
| August 2015 | 2015 2014 SP1 2013 SP1 2012 SP1 |
| 14.5 14.0.5 | 2014 SP1 2013 SP1 2012 SP1 2011 SP1 |
| 14.0.1 14.0 | 2014 2013 SP1 2012 SP1 2011 SP1 |
| 13.1.1 13.1 | 2013 SP1 2012 SP1 2011 SP1 2010 SP1 |
| 13.0.1 13.0 | 2013 2012 SP1 2011 SP1 2010 SP1 |
| 12.1 | 2012 SP1 2011 SP1 2010 SP1 2009 SP1 |
| 12.0 | 2012 2011 SP1 2010 SP1 2009 SP1 |
| 4.1 | 2011 SP1 2010 SP1 2009 SP1 8.6.1 |
| 4.0 | 2011 2010 SP1 2009 SP1 8.6.1 |
| 3.6.1 3.6 | 2010 SP1 2009 SP1 8.6.1 8.5.1 |
| 3.5.1 | 2010 2009 SP1 8.6.1 8.5.1 |
| 3.4 | 2009 SP1 8.6.1 8.5.1 8.2.1 |
| 3.3.1 3.3 | 2009 8.6.1 8.5.1 8.2.1 |
| 3.2.1 | 2009 8.6.1 8.5.1 8.2.1 |
| 3.1.1 | 8.6.1 8.5.1 8.2.1 |
| 3.0.1 3.0 | 8.6 8.5.1 8.2.1 |
| 2.4.1 2.4 | 8.5.1 8.2.1 8.0 |
| 2.3.1 | 8.5 8.2.1 8.0 |
| 2.1.3 2.1.2 2.1.1 | 8.2.1 8.0 |
| 2.1 | 8.2 8.0 |
| 2.0.2 2.0.1 2.0 | 8.0 |

Parent topic:

NI CompactRIO Device Drivers

Related reference:

- NI CompactRIO Device Driver Versions

Related information:

- NI Driver and Development Software Compatibility

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-device-drivers-version-numbers.html language=enus -->
## TOPIC 00051: NI CompactRIO Device Driver Versions

- bundle_id: `ni-compactrio`
- source_path: `compactrio-device-drivers-version-numbers.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-device-drivers-version-numbers.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `reference`
- source_description: To optimize product performance, update to the most recent driver version. The NI CompactRIO Device Drivers software might appear under different names depending on the version. 1 NI CompactRIO Device Driver Versions Driver Version NI CompactRIO Device Driver Name 4.1 or earlier NI-RIO 12.0 (August

### NI CompactRIO Device
 Driver Versions

Tip

The NI CompactRIO Device Drivers software might appear under different
 names depending on the version.

| Driver Version | NI CompactRIO Device Driver Name |
| --- | --- |
| 4.1 or earlier | NI-RIO |
| 12.0 (August 2012) through 14.5 (February 2015) | NI-RIO Device Drivers |
| 15.0 (August 2015) or later | NI CompactRIO Device Drivers NI R Series Multifunction RIO Device Drivers [1]1 Prior to version 15.0, both the NI CompactRIO Device Drivers and NI R Series Multifunction RIO Device Drivers were included in the NI-RIO Device Drivers. |

Parent topic:

NI CompactRIO Device Drivers

Related reference:

- NI CompactRIO Device Drivers and LabVIEW Compatibility

[<sup>1</sup>](#note_ref-d17846e89) Prior to
 version 15.0, both the NI CompactRIO Device Drivers and NI R
 Series Multifunction RIO Device Drivers were included in the
 NI-RIO Device Drivers.

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-dram-interface.html language=enus -->
## TOPIC 00052: CompactRIO DRAM Interface

- bundle_id: `ni-compactrio`
- source_path: `compactrio-dram-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-dram-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Several CompactRIO targets contain onboard DRAM that is directly accessible from the LabVIEW FPGA VI. LabVIEW allows DRAM to be accessible as an FPGA Memory Item. To determine the available amount of onboard DRAM, refer to the Specifications document of the CompactRIO target. Using DRAM Effectively

### CompactRIO DRAM Interface

Several CompactRIO targets contain onboard DRAM that is directly accessible from the LabVIEW FPGA
 VI. LabVIEW allows DRAM to be accessible as an FPGA Memory Item.

To determine the available amount of onboard DRAM, refer to the
 *Specifications* document of the CompactRIO target.

Parent topic:

NI CompactRIO Controllers

#### Using DRAM Effectively with CompactRIO

The following design considerations can affect the throughput and storage capacity that you can achieve with the dynamic random access memory (DRAM) interface of the FPGA on CompactRIO devices:

- Access size and frequency
- Request pipelining
- Sequential access

##### Access Size and Frequency

The access size
 is the amount of information stored in one memory address. You can set up memory to
 use a variety of data types. To achieve the best performance and to utilize the
 maximum amount of data, use a data type that matches the access size of the
 controller. The access size is the exact number of bits that are written and read in
 a given memory access.

The following table shows the specifications for
 CompactRIO targets that support FPGA-accessible DRAM, including the optimum access
 size.

| CompactRIO Target | Number of DRAM Banks | Size per Bank | Maximum Theoretical Bandwidth per Bank | Access Size |
| --- | --- | --- | --- | --- |
| cRIO-9034 | 1 | 128 MB | 1.6 GB/s | 128 Bits |
| cRIO-9039 | 1 | 128 MB | 1.6 GB/s | 128 Bits |

##### Data Recommendations

If you use a data type that is smaller than the access size, the remaining bits
 receive an unknown and invalid value, but still get written and take up both space
 and bandwidth. For example, if the access size is 128 bits wide and you choose a
 32-bit data type when configuring the DRAM, the remaining 96 bits are of an unknown
 and invalid data type. The following figure shows an optimized memory element and a
 memory element in which the data type is smaller than the access size.

Figure 8.

[IMAGE alt='image' src='GUID-1F673878-01B6-439B-A1D1-B539A78FC43B-a5.svg']

Push data into the memory item interface within the DRAM clock
 domain, which is 100 MHz. Right-click the FPGA target in a LabVIEW project, select
 New»FPGA Base Clock, and choose the DRAM
 Clock resource. Bandwidth is maximized when data is pushed into the
 memory item interface at the clock rate.

Note

##### Request Pipelining

The DRAM architecture
 is highly pipelined, resulting in relatively long latency between data requests and
 the execution of the requests. NI recommends that prerequest samples, which helps
 maintain high throughput.

To prerequest samples, request the samples you want
 to read without waiting for the data valid strobe of the retrieve method. Even
 though each individual request is still subject to latency and some non-determinism,
 you now get much higher transfer rates because DRAM can access several pieces of
 data sequentially instead of treating each request separately.

##### Sequential Access

DRAM is optimized for
 high storage density and high bandwidth. DRAM accesses data sequentially and in
 large blocks. For example, you have to read the data in address 0x1 after you have
 read the data in address 0x0 and the processor reads large blocks of memory into
 cache, even if the program being executed requests a single byte.

To maximize
 performance, avoid switching between reading and writing, accessing non-contiguous
 addresses, or writing to memory in decrementing-address fashion. The most efficient
 access strategy is to perform only one type of access, either reading or writing, on
 a large number of sequential addresses. Although this is optimal, it is not
 practical for most applications. A more practical approach is to maximize the amount
 of sequential data being accessed and minimizing changes in access
 modes.

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-embedded-system.html language=enus -->
## TOPIC 00053: CompactRIO Embedded System

- bundle_id: `ni-compactrio`
- source_path: `compactrio-embedded-system.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-embedded-system.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A CompactRIO embedded system includes a Real-Time processor, CompactRIO chassis, user-configurable FPGA, and C Series I/O modules.1 Components in a CompactRIO Embedded System Real-Time processor CompactRIO chassis User-configurable FPGA C Series I/O modules Real-Time ProcessorCompactRIO controllers

### CompactRIO Embedded System

A CompactRIO embedded system includes a Real-Time processor, CompactRIO chassis,
 user-configurable FPGA, and C Series I/O
 modules.

Figure 1.

[IMAGE alt='image' src='GUID-27E335CC-3E84-487D-B2CA-1A78879FBC8C-a5.svg']

1. Real-Time processor
2. CompactRIO chassis
3. User-configurable FPGA
4. C Series I/O modules

#### Real-Time Processor

CompactRIO
 controllers feature a real-time processor that deterministically executes LabVIEW
 applications.

#### CompactRIO Chassis

CompactRIO chassis
 feature a user-configurable FPGA that controls the digital and analog I/O lines on
 the reconfigurable embedded chassis.

#### User-configurable FPGA

The FPGA chip embedded within the
 chassis connects to the C Series I/O modules in a star topology. The
 star topology provides direct access to each module for precise
 control and flexibility in timing, triggering, and
 synchronization.

To change the functionality of the chassis
 FPGA, use the LabVIEW FPGA Module and NI CompactRIO Device
 Drivers to create a custom VI.
 Download the custom VI to the FPGA.

#### C
 Series I/O Modules

C Series I/O modules provide integrated
 signal conditioning and connection terminals for different
 measurement types.

Parent topic:

NI CompactRIO Device Drivers

Related concepts:

- Configuring a Project

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-interface-methods-fpga-interface.html language=enus -->
## TOPIC 00054: CompactRIO Interface Methods (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `compactrio-interface-methods-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-interface-methods-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to the methods described in the LabVIEW API topic Invoke Method, you can use the Read TEDS method with the LabVIEW API Invoke Method function for CompactRIO devices. Read TEDs MethodRead TEDS method reads TEDSTransducer Electronic Data Sheet. A TEDS contains the critical information need

### CompactRIO Interface Methods (FPGA Interface)

In addition to the methods described in the LabVIEW API topic *Invoke
 Method*, you can use the Read TEDS method with the LabVIEW API
 Invoke Method function for CompactRIO devices.

#### Read
 TEDs Method

Read TEDS method reads TEDS<sup>[[1]](#note-d6269e41)</sup>[<sup>1</sup>](#fnsrc_1-d6269e41) Transducer
 Electronic Data Sheet. A TEDS contains the critical information needed by an
 instrument or measurement system to identify, characterize, interface, and
 properly use the signal from an analog sensor. information from a C Series
 module that has TEDS support enabled.

[IMAGE alt='image' src='GUID-3791AA24-ADBE-4D88-B48F-4F4B6CAAFED6-a5.svg']

Connector

Open FPGA VI
 Reference

[IMAGE alt='image' src='GUID-3791AA24-ADBE-4D88-B48F-4F4B6CAAFED6-a5.svg']

Slot

N

N

[IMAGE alt='image' src='GUID-3791AA24-ADBE-4D88-B48F-4F4B6CAAFED6-a5.svg']

Channel

Invoke
 Method

[IMAGE alt='image' src='GUID-752B9BED-6A53-4C06-A319-586FE93074CA-a5.svg']

TEDS Binary

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

v0.9 (TEDS)

v0.9

TRUE

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related information:

- Invoke Method

[<sup>1</sup>](#note_ref-d6269e41) Transducer
 Electronic Data Sheet. A TEDS contains the critical information needed by an
 instrument or measurement system to identify, characterize, interface, and
 properly use the signal from an analog sensor.

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-reconfigurable-chassis.html language=enus -->
## TOPIC 00055: CompactRIO Reconfigurable Chassis

- bundle_id: `ni-compactrio`
- source_path: `compactrio-reconfigurable-chassis.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-reconfigurable-chassis.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 22 CompactRIO reconfigurable chassis ChassisDescription cRIO-9111CompactRIO 4-Slot, Virtex-5 LX30 Reconfigurable Chassis cRIO-9112CompactRIO 8-Slot, Virtex-5 LX30 Reconfigurable Chassis cRIO-9113CompactRIO 4-Slot, Virtex-5 LX50 Reconfigurable Chassis cRIO-9114CompactRIO 8-Slot, Virtex-5 LX50 Reconfi

### CompactRIO Reconfigurable Chassis

| Chassis | Description |
| --- | --- |
| cRIO-9111 | CompactRIO 4-Slot, Virtex-5 LX30 Reconfigurable Chassis |
| cRIO-9112 | CompactRIO 8-Slot, Virtex-5 LX30 Reconfigurable Chassis |
| cRIO-9113 | CompactRIO 4-Slot, Virtex-5 LX50 Reconfigurable Chassis |
| cRIO-9114 | CompactRIO 8-Slot, Virtex-5 LX50 Reconfigurable Chassis |
| cRIO-9116 | CompactRIO 8-Slot, Virtex-5 LX85 Reconfigurable Chassis |
| cRIO-9118 | CompactRIO 8-Slot, Virtex-5 LX110 Reconfigurable Chassis |

Parent topic:

CompactRIO Controller and Chassis Reference

Related concepts:

- Configuring a Project with Connected Hardware
- Configuring a Project with Offline Hardware
- Configuring the Chassis I/O (FPGA Interface)
- Converting the Temperature of a CompactRIO Chassis, Ethernet RIO Chassis, MXIe-RIO Chassis, or a Single-Board RIO Device (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=compactrio-reconfigurable-embedded-chassis-fp.html language=enus -->
## TOPIC 00056: CompactRIO Reconfigurable Embedded Chassis (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `compactrio-reconfigurable-embedded-chassis-fp.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/compactrio-reconfigurable-embedded-chassis-fp.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A user-reconfigurable FPGA controls the digital and analog I/O lines on the CompactRIO reconfigurable embedded chassis. The FPGA chip is embedded within the CompactRIO chassis and is connected to the C Series I/O modules in a star topology, providing direct access to each module for precise control

### CompactRIO Reconfigurable Embedded Chassis (FPGA Interface)

A user-reconfigurable FPGA controls the digital and analog I/O lines on the CompactRIO reconfigurable embedded chassis. The FPGA chip is embedded within the CompactRIO chassis and is connected to the C Series I/O modules in a star topology, providing direct access to each module for precise control and flexibility in timing, triggering, and synchronization. You can *configure the CompactRIO system* and change the functionality of the FPGA on the CompactRIO chassis in LabVIEW using the LabVIEW FPGA Module and NI CompactRIO Device Drivers to create and download a custom VI to the FPGA.

Parent topic:

CompactRIO Interface Methods (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-channel-for-pulse-width-modulat.html language=enus -->
## TOPIC 00057: Configuring a Channel for Pulse-Width Modulation

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-channel-for-pulse-width-modulat.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-channel-for-pulse-width-modulat.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a digital output channel to output a signal with a set frequency and period. Use a control on the front panel of a VI to control the on time (also called the active time or duty cycle) of the pulse. Pulse-Width Modulation Example Refer to the Pulse Width Modulation (Host) VI in the

### Configuring a Channel for Pulse-Width Modulation

You can configure a digital output channel to output a signal with a set frequency and period. Use a control on the front panel of a VI to control the on time (also called the active time or duty cycle) of the pulse.
Pulse-Width Modulation Example

Refer to the Pulse Width Modulation (Host) VI in the labview\examples\CompactRIO\NI Scan Engine\Advanced\Specialty Digital Configuration - PWM\Specialty Digital Configuration - Pulse-Width Modulation Mode.lvproj for an example of pulse-width modulation. The example uses an *NI 9474*, but you can modify it to use a different digital output module.

Parent topic:

Configuring Specialty Digital Functions

Related concepts:

- NI 9474 (Scan Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-counter-to-count-edges.html language=enus -->
## TOPIC 00058: Configuring a Counter to Count Edges

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-counter-to-count-edges.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-counter-to-count-edges.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a counter to count signal edges and perform an action on another channel when the count reaches a specified number called the terminal count. If you make any configuration changes, the counter resets. You can configure the following options for edge counting. Input FilterYou can ad

### Configuring a Counter to Count Edges

You can configure a counter to count signal edges and perform an action on another channel when
 the count reaches a specified number called the *terminal count*. If you make
 any configuration changes, the counter resets.

You can configure the following options for edge counting.

#### Input Filter

You can add an input filter to all input channels of the
 module. A filter removes noise, glitches, and spikes on inputs by rejecting signals
 with periods shorter than the specified length. The following filter options are
 available:

Disabled

1 µs

1 µs

1 µs

2 µs

2 µs

16 µs

16 µs

16 µs

32 µs

32 µs

256 µs

256 µs

512 µs

512 µs

4096 µs

4096 µs

4096 µs

8192 µs

8192 µs

#### Counter Event

Rising Edge

Falling Edge

Any Edge

#### Counter Source

This Channel

Terminal Count of Previous Channel

#### Count Direction

Count Up

Count Down

#### Terminal Count

You can specify a terminal
 count up to a maximum of 2<sup>32</sup> = 4,294,967,296. When the counter reaches
 the terminal count, it resets and starts counting again from zero.

#### Terminal Count Output Mode

You can select
 one of the following four actions to perform on a digital output channel on another
 module when the counter reaches the specified terminal count.

Toggle, Reset Off

Toggle, Reset On

On Pulse

Off Pulse

Note

counter-driven output

#### Gate
 Mode

- Always Enabled —The counter increments on each edge of the
 type selected with the Counter Event control.
- Next Channel —The counter increments only on edges that
 occur when the next higher channel is in the on state.

Parent topic:

Configuring Counters

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-counter-to-measure-frequency.html language=enus -->
## TOPIC 00059: Configuring a Counter to Measure Frequency

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-counter-to-measure-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-counter-to-measure-frequency.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a counter to measure the frequency of a signal connected to the channel. The counter counts the number of rising or falling signal edges during the length of the Frequency Timebase, divides that number by the Frequency Timebase in µs, and returns the frequency in kHz. You can confi

### Configuring a Counter to Measure Frequency

You can configure a counter to measure the frequency of a signal connected to the channel. The
 counter counts the number of rising or falling signal edges during the length of the
 Frequency Timebase, divides that number by the Frequency Timebase in µs, and returns the
 frequency in kHz.

You can configure the following options for a frequency measurement counter.

#### Input Filter

You can add an input filter
 to all input channels of the module. A filter removes noise, glitches, and spikes on
 inputs by rejecting signals with periods shorter than the specified length. You can
 select one of the following options.

Disabled

1 µs

16 µs

256 µs

4096 µs

#### Measurement Edge

Rising

Falling

#### Frequency Timebase

Selecting a
 Frequency Timebase is a tradeoff between resolution and
 response speed. A shorter timebase provides lower resolution but the data it returns
 is more up to date. A longer timebase provides higher resolution but may lag behind
 or miss changes in signal frequency. The guidelines below for selecting a timebase
 for different frequency ranges will result in a maximum error of approximately 1%.
 If you require higher resolution and can tolerate less frequent updates, use a
 longer timebase than indicated.

256 µs

512 µs

1024 µs

2048 µs

4096 µs

8192 µs

16384 µs

32768 µs

Note

measure period

#### Frequency Measurement Example

Refer to
 the Frequency Measurement (Host) VI in the labview\examples\CompactRIO\NI
 Scan Engine\Advanced\Specialty Digital Configuration - Counter Mode\Specialty
 Digital Configuration - Counter Mode.lvproj for an example of frequency
 measurement. The example uses an *NI 9401*, but you can modify it to use
 a different digital input module.

Parent topic:

Configuring Counters

Related concepts:

- NI 9401 (Scan Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-counter-to-measure-period.html language=enus -->
## TOPIC 00060: Configuring a Counter to Measure Period

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-counter-to-measure-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-counter-to-measure-period.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a digital input channel as a counter to measure the period of a signal connected to the channel. The counter returns data in µs. You can configure the following options for a period measurement counter. Input FilterYou can add an input filter to all input channels of the module. A

### Configuring a Counter to Measure Period

You can configure a digital input channel as a counter to measure the period of a signal
 connected to the channel. The counter returns data in µs.

You can configure the following options for a period measurement counter.

#### Input Filter

You can add an input filter to all input channels of the
 module. A filter removes noise, glitches, and spikes on inputs by rejecting signals
 with periods shorter than the specified length. You can select one of the following
 options.

Disabled

1 µs

16 µs

256 µs

4096 µs

#### Measurement Edge

Rising Edge

Falling Edge

Parent topic:

Configuring Counters

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-counter-to-measure-pulse-width.html language=enus -->
## TOPIC 00061: Configuring a Counter to Measure Pulse Width

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-counter-to-measure-pulse-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-counter-to-measure-pulse-width.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a digital input channel as a counter to measure the pulse width of a signal connected to the channel. The counter returns data in µs. You can configure the following options for a pulse-width measurement counter. Input FilterYou can add an input filter to all input channels of the

### Configuring a Counter to Measure Pulse Width

You can configure a digital input channel as a counter to measure the pulse width of a signal
 connected to the channel. The counter returns data in µs. You can configure the
 following options for a pulse-width measurement counter.

#### Input Filter

You can add an input filter
 to all input channels of the module. A filter removes noise, glitches, and spikes on
 inputs by rejecting signals with periods shorter than the specified length. You can
 select one of the following options.

Disabled

1 µs

16 µs

256 µs

4096 µs

#### Measurement Type

High Pulse

Low Pulse

Most Recent

Parent topic:

Configuring Counters

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-module-for-quadrature-input.html language=enus -->
## TOPIC 00062: Configuring a Module for Quadrature Input

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-module-for-quadrature-input.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-module-for-quadrature-input.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a digital input module for quadrature input. A quadrature input returns position and velocity data based on the values of three channels. In quadrature input mode, channels 0, 1, and 2 are the A, B, and Index channels, respectively, of Quadrature0. If the module has six or more cha

### Configuring a Module for Quadrature Input

You can configure a digital input module for quadrature input.

A quadrature input returns position and velocity data based on the values of three
 channels. In quadrature input mode, channels 0, 1, and 2 are the A, B, and Index
 channels, respectively, of Quadrature0.

If the module has six or more channels, channels 3, 4, and 5 can form a second quadrature
 input, Quadrature1. A C Series module can have only two quadrature inputs. Quadrature
 inputs return position data in counts and velocity in counts per second.

You can configure the following options for quadrature input.

#### Input Filter

You can add an input filter to all input channels of the
 module. A filter removes noise, glitches, and spikes on inputs by rejecting signals
 with periods shorter than the specified length. You can select one of the following
 options.

Disabled

1 µs

16 µs

256 µs

4096 µs

#### Velocity Timebase

Selecting a
 Velocity Timebase is a tradeoff between resolution and
 response speed. A shorter timebase provides lower resolution but the data it returns
 is more up to date. A longer timebase provides higher resolution but may lag behind
 or miss changes in velocity.

256 µs

512 µs

1024 µs

2048 µs

4096 µs

8192 µs

16384 µs

32768 µs

#### Index Mode

If you enable an Index Mode,
 the position is reset to zero when A and B have the specified values and the Index
 is in the on state.

Disabled

Phase B0 A0

Phase B0 A1

Phase B1 A0

Phase B1 A1

Parent topic:

Configuring Specialty Digital Functions

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-project-with-connected-hardware.html language=enus -->
## TOPIC 00063: Configuring a Project with Connected Hardware

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-project-with-connected-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-project-with-connected-hardware.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure your project to discover installed hardware.

### Configuring a Project with Connected Hardware

Configure your project to discover installed hardware.

- [Discovering your Hardware](discovering-your-hardware.html#GUID-AA90C3E7-FCF9-4C3C-960F-98E2DBF977BB)
- [Adding Additional Hardware](adding-additional-hardware.html#GUID-FF648286-94AD-4BCA-825B-E24993808947)

Parent topic:

Configuring a Project

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-project-with-daqmx.html language=enus -->
## TOPIC 00064: Configuring a Project with DAQmx (cRIO-904x and cRIO-905x)

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-project-with-daqmx.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-project-with-daqmx.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO with DAQmx is only supported on cRIO-904x and cRIO-905x controllers. Adding a Controller Target for the cRIO-904x/cRIO-905x Complete the following steps to add a controller target for the cRIO-904x or cRIO-905x to a project. Create a new project in LabVIEW or open an existing project. Rig

### Configuring a Project with DAQmx (cRIO-904x
 and cRIO-905x)

CompactRIO with DAQmx is only supported on cRIO-904x and cRIO-905x
 controllers.

Parent topic:

Configuring a Project

#### Adding a Controller Target for the cRIO-904x/cRIO-905x

Complete the following steps to add a controller target
 for the cRIO-904x or cRIO-905x to a project.

1. Create a new project in LabVIEW or open an existing project.
2. Right-click the project root in the Project Explorer
 window and select New»Targets and Devices from the
 shortcut menu. 
 The Add Targets and Devices dialog box
 opens.
3. Enable the applicable checkbox: 
 Click the Existing target or device radio button
 if your hardware is *connected*.
 Click the New target or device radio button if
 your hardware is *offline*.
4. Select your cRIO-904x or cRIO-905x controller from the Real-Time
 CompactRIO folder.
5. Click the OK button. 
 LabVIEW adds the target item to the project.

Related tasks:

- Adding an FPGA Target

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-project-with-offline-hardware.html language=enus -->
## TOPIC 00065: Configuring a Project with Offline Hardware

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-project-with-offline-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-project-with-offline-hardware.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure a project with C Series modules when you do not have hardware installed, perform these procedures.

### Configuring a Project with Offline Hardware

To configure a project with C Series modules when you do not have hardware installed, perform
 these procedures.

- [Adding a Controller Target](adding-a-controller-target.html) A controller target can be a CompactRIO controller, Ethernet RIO chassis, Single-Board RIO device, myRIO device, roboRIO device, or NI ELVIS RIO Control Module (NI ELVIS RIO CM) device.
- [Adding a Chassis Item](adding-a-chassis-item.html#GUID-3E41560B-49C1-49A6-8BF7-71D4477BCBDC) Add a CompactRIO, Ethernet RIO, MXIe-RIO, Single-Board RIO, myRIO, roboRIO, or NI ELVIS RIO Control Module (NI ELVIS RIO CM) chassis item to your project.
- [Adding an FPGA Target](adding-an-fpga-target.html) You do not need to add an FPGA target to your project when programming in Scan Interface Mode, Real-Time Mode, or Real-Time Scan Mode.
- [Adding I/O Items](adding-i-o-items.html#GUID-1A3A1A13-F9F0-4615-A9A6-103F4758F881) An I/O item can be a RIO mezzanine card or a C Series module. RIO mezzanine cards have I/O or slots for C Series modules.

Parent topic:

Configuring a Project

<!--NI_TOPIC bundle=ni-compactrio path=configuring-a-project.html language=enus -->
## TOPIC 00066: Configuring a Project

- bundle_id: `ni-compactrio`
- source_path: `configuring-a-project.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-a-project.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a LabVIEW project with connected hardware or offline hardware. Use a LabVIEW project to work with NI CompactRIO Device Drivers and C Series modules. Configure the project with targets and items for your hardware devices: Target Any device on which you can run LabVIEW VIs, such as CompactRI

### Configuring a Project

Configure a LabVIEW project with connected hardware or offline hardware.

Use a LabVIEW project to work with NI CompactRIO Device Drivers and C Series modules. Configure
 the project with targets and items for your hardware devices:

Target

Item

The following figure shows a LabVIEW project configured with targets and items.

[IMAGE alt='image' src='GUID-0BB5D602-3E42-4477-998B-1EDFB4476F8E-a5.svg']

1. Controller Target
2. Chassis Item
3. Real-Time Scan Resources Item
4. C Series Module Items (Scan Interface)
5. FPGA Target
6. C Series Module Item (FPGA Interface)

Note

For an example of a LabVIEW project using C Series I/O, refer to the *Using the Scan
 Interface with FPGA Interface* LabVIEW project in the
 labview\examples\CompactRIO\NI Scan Engine\Getting Started\Using Scan
 Interface with FPGA Interface\Using Scan Interface with FPGA
 Interface.lvproj .

Parent topic:

Getting Started with a CompactRIO System in LabVIEW

Related concepts:

- Single-Board RIO System
- Using C Series Modules in a LabVIEW Project
- Using the Scan Interface with Individual Modules

<!--NI_TOPIC bundle=ni-compactrio path=configuring-channels-on-the-ni-9470.html language=enus -->
## TOPIC 00067: Configuring Channels on the NI 9470

- bundle_id: `ni-compactrio`
- source_path: `configuring-channels-on-the-ni-9470.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-channels-on-the-ni-9470.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure the channels of the NI 9470. Right-click an NI 9470 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Click the Channel Configuration button to open the Channel Configuration dialog box. S

### Configuring Channels on the NI 9470

Complete the following steps to configure the channels of the NI 9470.

1. Right-click an NI 9470 C Series module in the Project Explorer window and
 select Properties from the shortcut menu to
 display this dialog box.
2. Click the Channel Configuration button to open the Channel Configuration dialog box.
3. Select a channel to configure.
4. Configure the following settings. Output Mode—Specifies the output mode for the selected channel.
 Duty Cycle—Sets the channel to open loop mode without any internal control mechanism. You will have to implement your own control loop in your application.
Average Current—Sets the channel to closed loop mode using an internal PID control loop. This PID control executes based on the PID coefficients.
PWM Divisor—Specifies the PWM divisor value for the selected channel.
 Each channel runs based on the PWM frequency,
 which is derived by the formula
 Data Rate ÷
 PWM Divisor. Supported
 values range 2 to 511. You can only set the PWM
 Divisor to a value of 1 if the data rate is set to
 2,000 S/s or 2,048 S/s.
PID Response—Specifies the PID response for the selected channel. This option is only available if the channel's Output Mode is set to Average Current.
 Slow—The proportional, integral, and derivative gain coefficients are pre-set to provide a slow PID response speed. The output current will arrive at the intended setpoint at a slower rate.
Medium—The proportional, integral, and derivative gain coefficients are pre-set to provide a medium PID response speed. The output current will arrive at the intended setpoint at a moderate rate.
Fast—The proportional, integral, and derivative gain coefficients are pre-set to provide a fast PID response speed. The output current will arrive at the intended setpoint at a faster rate.
Custom—Customize your own PID response by entering your own Proportional Gain, Integral Gain, and Derivative Gain. 
 Proportional Gain—Specifies the proportional gain coefficient for the
 selected channel. Specified in units of
 (duty cycle %) ÷
 Amps.
Integral Gain—Specifies the integral gain coefficient for the selected
 channel. Specified in units of
 (duty cycle %) ÷
 Amps.
Derivative Gain—Specifies the derivative gain coefficient for the
 selected channel. Specified in units of
 (duty cycle %) ÷
 Amps.
Dither Amplitude—Specifies the dither amplitude for the selected channel. Represents the dither peak amplitude for the channel. You can disable dither by setting this parameter to 0. The range depends on which Output Mode the channel is set.
 Output ModeRangeDuty Cycle0% to 100%Average Current0 A to 3.999 A
Dither Divisor—Specifies the Dither Divisor for the selected channel,
 which controls the dither frequency. Dither
 frequency is derived using the formula
 PWM Frequency ÷
 Dither Divisor.
5. Click OK to close the Channel Configuration dialog box.
6. Click OK to close the Module Properties Dialog Box.

Parent topic:

NI 9470 (FPGA Interface)

Related concepts:

- NI 9470 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-chassis-io-fpga-int.html language=enus -->
## TOPIC 00068: Configuring the Chassis I/O (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-chassis-io-fpga-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-chassis-io-fpga-int.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### Configuring the Chassis I/O (FPGA Interface)

- [Enabling Sleep Mode on a CompactRIO Chassis, Ethernet RIO Chassis, MXIe-RIO Chassis, or sbRIO Device](enabling-sleep-mode-crio-enet-mxierio-chassis-sbrio-device.html)
- [Programmatically Resetting the System on a CompactRIO Chassis or sbRIO Device](programmatically-reset-system-on-crio-chassis-or-sbrio-device.html)
- [Programming the FPGA LED](programming-fpga-led.html#GUID-9FF1831B-5A16-4339-B939-D25E64E6D8B7)
- [Reading the Temperature of a CompactRIO Chassis, Ethernet RIO Chassis, MXIe-RIO Chassis, or sbRIO Device](reading-temp-chassis-or-device.html)

Parent topic:

Configuring Devices

Related concepts:

- Configuring a Project with Connected Hardware

<!--NI_TOPIC bundle=ni-compactrio path=configuring-clock-resources-for-a-clip.html language=enus -->
## TOPIC 00069: Configuring Clock Resources for a CLIP

- bundle_id: `ni-compactrio`
- source_path: `configuring-clock-resources-for-a-clip.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-clock-resources-for-a-clip.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the Clock Settings page of the sbRIO CLIP Generator to do the following: Specify the pins to connect to LabVIEW FPGA clock lines Reserve additional clock resources in the CLIP for the NI sbRIO target. The sbRIO CLIP Generator will create the VHDL logic required to

### Configuring Clock Resources for a CLIP

Clock Settings

- Specify the pins to connect to LabVIEW FPGA clock lines
- Reserve additional clock resources in the CLIP for the NI sbRIO target.

1. From the Available Pins control, select a pin. 
 The Clock Capability column specifies one of the
 following configurations for each pin: None—The pin does not provide a direct connection
 to the clock distribution network on the FPGA.
 Single-region—The pin provides a direct
 connection to the clock distribution network on a specific region, or
 bank of pins, on the FPGA.
 Multi-region—The pin provides a direct connection
 to the clock distribution network on the entire FPGA.
2. From the Clock Direction control, select one of the following options: **To CLIP**—Exports a clock signal from LabVIEW FPGA to the CLIP.
 **From CLIP**—Imports a clock signal from the CLIP to LabVIEW FPGA.
 
Note For best performance, National
 Instruments recommends that you configure From CLIP clocks to use pins with
 single- or multi-region clock capability, depending on how widely your CLIP
 design will use this clock in the FPGA. Select
 Multi-region if you are not sure which region to
 select. You can still configure a clock line for a pin that is not
 clock-capable, but the sbRIO CLIP Generator displays a warning icon for the
 clock to indicate that performance from this pin might diminish.
3. Click Add. 
 The LabVIEW Clocks table lists the created clock
 line.
4. If you specified a From CLIP clock, configure the following
 options in the Clock Parameters section. This is required
 for the LabVIEW FPGA Module to handle the clock signal
 correctly: 
 **Frequency in MHz**—The minimum and maximum frequencies the clock signal supports. If
 the clock signal has a fixed frequency, specify the same value for
 the minimum and maximum.
 **Duty Cycle**—The minimum and maximum percentage of time the clock signal is
 high.
 **Accuracy in PPM**—The amount, in parts per million (PPM), that the clock signal may
 deviate from its specified frequency under normal operating
 conditions.
 **Jitter in Picoseconds**—The acceptable absolute difference, in picoseconds, between any one
 clock period and the average clock period. Jitter may also be called
 frequency stability.
 **Supports Derived Clocks**—When you enable this option, the sbRIO CLIP Generator adds a
 Source Clock Ready signal and
 Derived Clocks Valid signal to the
 generated VHDL file for the CLIP.
5. In the Additional Clock Resources Reserve section, configure the following options if your CLIP design will include any clock management resources from the FPGA. 
 **MMCMs**—The number of mixed-mode clock manager (MMCM) resources to
 reserve.
 **BUFGs**—The number of global clock buffer (BUFG) resources to reserve.
6. Repeat the preceding steps to create additional clock lines for the CLIP. 
 You can drag and drop created clock lines in the LabVIEW Clocks table.
7. Click Next to continue to the CLIP
 Summary page. 
 Use the CLIP Summary page to finish the CLIP design.

Parent topic:

Creating a Component-Level IP for an NI sbRIO Target

Related concepts:

- Finishing the CLIP Design

Related tasks:

- Creating a LabVIEW I/O Node Interface for a CLIP

<!--NI_TOPIC bundle=ni-compactrio path=configuring-controller-startup-settings-in-max.html language=enus -->
## TOPIC 00070: Configuring Controller Startup Settings in MAX

- bundle_id: `ni-compactrio`
- source_path: `configuring-controller-startup-settings-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-controller-startup-settings-in-max.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following information applies to NI CompactRIO Controllers cRIO-903x, 904x, and 905x. Perform the following steps to configure controller startup settings in Measurement & Automation Explorer (MAX): Select the controller under Remote Systems. Select the System Settings tab in the center pane. In

### Configuring Controller Startup Settings in
 MAX

Note

Perform the following steps to configure controller startup settings in Measurement &
 Automation Explorer (MAX):

1. Select the controller under Remote Systems .
2. Select the System Settings tab in the center pane.
3. In the Startup Settings section of the System
 Settings tab, place a check in the box for the startup setting you want to
 enable.
4. Click the Restart button in MAX to restart the system.

You can configure the following controller startup settings in MAX:

- Force Safe Mode —Launch only the services necessary for updating
 configuration and installing software. Do not launch LabVIEW RT or any startup
 applications.
- Enable Console Out —Redirect output to the serial port. You can use
 a serial port terminal to read the IP address and firmware version of the controller.
- Disable RT Startup App —Do not run any LabVIEW RT startup
 applications.
- Disable FPGA Startup App —Do not autoload any FPGA applications.
 Note If you restart the
 system at any time by disconnecting and reconnecting power, the system will disregard the
 Disable FPGA Startup App setting and load an FPGA startup
 application if one is present.
- Enable Secure Shell Server (sshd) —Enables login over SSH, an
 encrypted communication protocol. Visit ni.com/info and enter the Info Code
 openssh for more information about SSH.
- LabVIEW Project Access —Enables adding the target to a LabVIEW
 project.
- Enable Embedded UI —Enables the embedded UI the next time the target
 is restarted. When you enable the embedded UI, you can interact with the front panels of VIs
 running on the target using input and display devices connected directly to the target. You
 also can browse and edit files on the target within a graphical working environment.

Note

Parent topic:

NI CompactRIO Controllers

<!--NI_TOPIC bundle=ni-compactrio path=configuring-counter-driven-outputs.html language=enus -->
## TOPIC 00071: Configuring Counter-Driven Outputs

- bundle_id: `ni-compactrio`
- source_path: `configuring-counter-driven-outputs.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-counter-driven-outputs.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Counter-driven output channels respond in a predetermined way when a counter channel on a digital input module reaches the terminal count. You must configure a digital input channel on another module for edge counting and select an action for the Terminal Count Output Mode. Then you select the digit

### Configuring Counter-Driven Outputs

Counter-driven output channels respond in a predetermined way when a counter channel on a digital
 input module reaches the terminal count. You must configure a digital input channel on
 another module for *edge counting* and select an action for the Terminal
 Count Output Mode. Then you select the digital output channel with the same channel
 number and configure it as a counter-driven output. You can configure the following
 options for a counter-driven output.

#### Drive from Slot

Use this control to
 select a slot with a digital input module that has at least one channel configured
 to count edges. Refer to the Project Explorer window and
 select a slot that has a channel called CTRx, where
 x is the number of the selected output channel.

#### Counter Driven

Use this control to
 enable or disable counter-driven output for the selected output channel. If you
 select Enabled, the counter selected with the
 Drive from Slot control drives the selected output
 channel. If counter-driven output is enabled for the selected channel, LabVIEW
 removes the I/O variable for the selected channel from the Project
 Explorer window. If an I/O variable for the selected channel is used
 in a block diagram of a VI, the VI will not run.

Parent topic:

Configuring Specialty Digital Functions

<!--NI_TOPIC bundle=ni-compactrio path=configuring-counters.html language=enus -->
## TOPIC 00072: Configuring Counters

- bundle_id: `ni-compactrio`
- source_path: `configuring-counters.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-counters.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure channels of some C Series digital input modules as counters. Counter channels measure digital signals. Counters are used commonly to count edges. Counters are also used for time measurements, such as measuring the frequency or period of a signal. Input FilterYou can add an input fi

### Configuring Counters

You can configure channels of some C Series digital input modules as counters. Counter channels
 measure digital signals. Counters are used commonly to count edges. Counters are also
 used for time measurements, such as measuring the frequency or period of a signal.

#### Input Filter

You can add an input filter to all module input channels. A
 filter removes noise, glitches, and spikes on inputs by rejecting signals with
 periods shorter than the specified length. The following filter options are
 available:

Disabled

1 µs

16 µs

256 µs

4096 µs

#### Counter Measurement Modes

- Count Edges
- Period Measurement
- Pulse-Width Measurement
- Frequency Measurement

Parent topic:

Configuring Specialty Digital Functions

<!--NI_TOPIC bundle=ni-compactrio path=configuring-current-limits-for-the-ni-9478-fp.html language=enus -->
## TOPIC 00073: Configuring Current Limits for the NI 9478 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-current-limits-for-the-ni-9478-fp.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-current-limits-for-the-ni-9478-fp.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the active current limit for each channel and the current limit thresholds at edit time using the C Series Module Properties dialog box. You can programmatically change these settings at run time using the FPGA I/O Property Node. The execution of an I/O Property Node that is config

### Configuring Current Limits for the NI 9478 (FPGA Interface)

You can configure the active current limit for each channel and the current limit thresholds at edit time using the *C Series Module Properties* dialog box. You can programmatically change these settings at run time using the FPGA I/O Property Node. The execution of an I/O Property Node that is configured with a Current Limit property overwrites the value you configured in the C Series Module Properties dialog box.
Configuring Current Limits Using the C Series Module Properties Dialog Box

Complete the following steps to configure the active current limit for each channel and the current limit thresholds for the NI 9478 using the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9478.
2. Right-click the NI 9478 in the Project Explorer window and select Properties from the shortcut menu to display the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the active current limit from the Channels table. You can select more than one channel by holding the < Ctrl > or < Shift > key when selecting channels.
4. Select the active current limit for the channel(s) from the Active Limit pull-down menu.
5. Enter a value between 0 and 5.1 in the Current Limit text box that corresponds to the active current limit for the selected channel(s).
6. Place a checkmark in the Enable Overcurrent Refresh checkbox and set the time in the Overcurrent Refresh Period text box if you want to enable a channel to automatically recover if the channel exceeds its active current limit threshold.
7. Click the OK button.
8. Select File»Save All in the Project Explorer window.

Configuring Current Limits Using the FPGA I/O Property Node

Complete the following steps to configure the active current limit for each channel and the current limit thresholds using the FPGA I/O Property Node.

1. Place three FPGA I/O Property Nodes on the block diagram and configure them for the NI 9478.
2. Click the Property section on the first Property Node and select the Active Current Limit property from the shortcut menu.
3. Right-click the Active Current Limit input and select Create»Control from the shortcut menu.
4. On the front panel of the VI, select the active current limit for each channel from the Active Current Limit array.
5. Click the Property section on the second Property Node and select the Current Limit A property from the shortcut menu.
6. Right-click the Current Limit A input and select Create»Control from the shortcut menu.
7. Click the Property section on the third Property Node and select the Current Limit B property from the shortcut menu.
8. Right-click the Current Limit B input and select Create»Control from the shortcut menu.
9. On the front panel of the VI, enter binary values in the Current Limit controls to set the current limit thresholds. You can use the following equation in the host VI to calculate the binary value from amperes:
 Binary Value = ( Current Value / 5.12 A) × 256

Parent topic:

NI 9478 (FPGA Interface)

Related concepts:

- Configuring a Project

<!--NI_TOPIC bundle=ni-compactrio path=configuring-data-rate-with-cseries-module-properties-diag.html language=enus -->
## TOPIC 00074: Configuring the Data Rate Using the C Series Module Properties Dalog Box

- bundle_id: `ni-compactrio`
- source_path: `configuring-data-rate-with-cseries-module-properties-diag.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-data-rate-with-cseries-module-properties-diag.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure the data rate for the module using the C Series Module Properties dialog box. Configure the CompactRIO system and add the module. Right-click the module in the Project Explorer window and select Properties to launch the C Series Module Properties dialog box.

### Configuring the Data Rate Using the C Series
 Module Properties Dalog Box

Complete the following steps to configure the data rate for the module using the
 C Series Module Properties dialog box.

1. Configure the CompactRIO system and add the module.
2. Right-click the module in the Project Explorer window
 and select Properties to launch the C Series
 Module Properties dialog box.
3. Select the rate from the Data Rate pull-down menu.
4. Click the OK button.
5. Select File»Save All in the Project
 Explorer window.

Parent topic:

Configuring the Data Rate for a Module (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-data-rate-with-fpga-io-property-node.html language=enus -->
## TOPIC 00075: Configuring the Data Rate Using the FPGA I/O Property Node

- bundle_id: `ni-compactrio`
- source_path: `configuring-data-rate-with-fpga-io-property-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-data-rate-with-fpga-io-property-node.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure the data rate for the module using the FPGA I/O Property Node. Place an FPGA I/O Property Node on the block diagram and configure it for the module. Click the Property section and select Data Rate from the shortcut menu. Right-click the Data Rate input and s

### Configuring the Data Rate Using the FPGA I/O
 Property Node

Complete the following steps to configure the data rate for the module using the FPGA
 I/O Property Node.

1. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module.
2. Click the Property section and select Data
 Rate from the shortcut menu.
3. Right-click the Data Rate input and select
 Create»Control from the shortcut menu.
4. On the front panel of the VI, select a rate from the Data
 Rate pull-down menu.

You can change the data rate at run time by writing to the control from the host VI.
 Refer to the module Getting Started (FPGA) VI at
 labview\examples\CompactRIO\Module
 Specific\<module>\<module>
 Getting Started for an example of configuring the data rate using the
 FPGA I/O Property Node.

The Data Rate property might return *error 65538*
 if the module is acquiring data. Use the Stop channel to stop
 acquiring data before you can write properties to the module.

Parent topic:

Configuring the Data Rate for a Module (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-devices.html language=enus -->
## TOPIC 00076: Configuring Devices

- bundle_id: `ni-compactrio`
- source_path: `configuring-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-devices.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure I/O functions on installed devices and chassis hardware.

### Configuring Devices

Configure I/O functions on installed devices and chassis hardware.

- [Configuring Specialty Digital Functions](specialty-digital-functions.html)
- [Configuring the Chassis I/O (FPGA Interface)](configuring-chassis-io-fpga-int.html)

Parent topic:

Getting Started with a CompactRIO System in LabVIEW

<!--NI_TOPIC bundle=ni-compactrio path=configuring-i-o-pins-on-the-target.html language=enus -->
## TOPIC 00077: Configuring I/O Pins on the Target

- bundle_id: `ni-compactrio`
- source_path: `configuring-i-o-pins-on-the-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-i-o-pins-on-the-target.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Click the Import from CSV or Export to CSV buttons on the bottom left of this page to import or export pin configuration data in a CSV file. The options on the Pin Configuration page of the of the sbRIO CLIP Generator correspond to Xilinx I/O standards and attributes. Complete the following steps to

### Configuring I/O Pins on the Target

Click the Import from CSV or Export to
 CSV buttons on the bottom left of this page to import or export pin
 configuration data in a CSV file.

Note

- The options on the Pin Configuration page of the of the
 sbRIO CLIP Generator correspond to Xilinx I/O standards and
 attributes.
- Complete the following steps to use the Pin
 Configuration page of the sbRIO CLIP Generator to configure
 the I/O pins on the NI sbRIO target.

1. Select a pin in the CLIP Pins table.
2. Use the Pin Settings pane to configure the following options for the pin: **I/O Standard**—The I/O standard of the I/O buffer for the pin.
 **Direction**—The direction of the I/O buffer for the pin. 
 Note 
 The direction you select is independent of the direction of a
 LabVIEW port or clock. For example, if you select
 Input for the pin direction you can
 still use the pin in a Read/Write LabVIEW
 FPGA I/O node, but writing to the pin will have no effect.
 **Drive Strength**—The output drive strength, in mA, for the pin.
 **Slew**—The output slew rate, which is the rate of transition between output
 levels, for the pin.
 **Pull**—The pull behavior for the pin. Select one of the following
 options: 
 None—Does not affect the input
 pin.
 Up—Drives the input pin to its high
 value when the pin is not being driven.
 Down—Drives the input pin to its low
 value when the pin is not being driven.
 Keeper—Preserves the last value of
 the pin when the pin is not being driven.
 
Note 
Refer to Xilinx documentation for more information about these and other I/O standards and
 attributes.
Some pins that a peripheral uses may allow you to specify a pin setting value of Custom. For such pins to function correctly, you must *modify the generated CLIP files* after you finish using the sbRIO CLIP Generator to supply the required custom value.
3. Use the Bank Voltage Levels pane to specify the voltage level supplied to each bank of pins. Note 
Not all configurations of pin settings and bank voltage levels are valid. You must specify a valid configuration to enable the Next button and continue in the sbRIO CLIP Generator. If you specify an invalid configuration, the Next button is disabled and the CLIP Pins table displays a warning icon. Hover over the warning icon to display a tooltip that includes information about the error to resolve.
If you configure a pin to use a differential I/O standard, the pin and its positive or negative pair function as a single input or output. For example, if you configure the DIO_23 pin to use the LVDS25 I/O standard, the DIO_23_N pin becomes disabled in the CLIP Pins table and all of its settings match those of the DIO_23 pin. This change occurs because the value of the DIO_23 pin now represents the voltage differential between the DIO_23 and DIO_23_N pins, and therefore the DIO_23_N pin no longer has a meaningful value.
Caution 

 Although the sbRIO CLIP Generator provides error-checking to ensure that your pin settings are valid, nothing prevents you from supplying a different voltage to the physical bank than the voltage specified in software.
4. Click Next to continue to the LabVIEW
 Interface page.

Parent topic:

Creating a Component-Level IP for an NI sbRIO Target

Related concepts:

- Finishing the CLIP Design

Related tasks:

- Adding Peripherals to a CLIP
- Creating a LabVIEW I/O Node Interface for a CLIP

<!--NI_TOPIC bundle=ni-compactrio path=configuring-modes-and-ranges-for-the-ni-9219.html language=enus -->
## TOPIC 00078: Configuring Modes and Ranges for the NI 9219 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-modes-and-ranges-for-the-ni-9219.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-modes-and-ranges-for-the-ni-9219.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the mode and range for each channel on the NI 9219 at edit time using the C Series Module Properties dialog box. Programmatically change the range for each channel at run time using the FPGA I/O Property Node. The execution of an I/O Property Node that is configured with a Range property o

### Configuring Modes and Ranges for the NI 9219 (FPGA Interface)

Configure the mode and range for each channel on the NI 9219 at edit time using the *C
 Series Module Properties* dialog box. Programmatically change the range for
 each channel at run time using the FPGA I/O Property Node. The execution of an I/O
 Property Node that is configured with a Range property overwrites
 the value you configured in the C Series Module Properties dialog
 box.

#### Configuring Modes and Ranges Using the C Series
 Module Properties Dialog Box

Complete the following steps to configure
 the channel(s) mode and range using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9219.
2. Right-click the NI 9219 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the mode and range from
 the Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the mode for the channel(s) from the Channel Mode 
 pull-down menu. If you select Digital In mode, skip the
 following steps and set the threshold . If you select
 Open Contact mode, skip the following step.
5. Select the range from the Range pull-down menu for the
 selected channel(s).
6. Click the OK button.
7. Select File»Save All in the Project
 Explorer window.

#### Configuring Ranges Using the FPGA I/O Property
 Node

Complete the following steps to configure the channel range using
 the FPGA I/O Property Node.

1. Create FPGA I/O items for the channel of the NI 9219 for which you want to
 configure a Range property. The channel must be set to
 Voltage mode, Resistance mode, RTD mode, Quarter Bridge mode, or Full Bridge
 mode.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 NI 9219 channel for which you want to configure the range.
3. Click the Property section and select the
 Range property from the shortcut menu.
4. Right-click the Range input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select a rate from the
 Range pull-down menu.

You can change the channel range at run time by writing to the control from the
 host VI. Refer to the NI 9219 Getting Started VI in the
 labview\examples\CompactRIO\Module Specific\NI 9219\NI 9219 Getting
 Started\NI 9219 Getting Started.lvproj for an example of changing a
 channel range using the FPGA I/O Property Node.

Parent topic:

NI 9219 (FPGA Interface)

Related concepts:

- Configuring a Project
- Configuring the Digital In Threshold for the NI 9219 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-crio-i-o-node-name-control-fp.html language=enus -->
## TOPIC 00079: Configuring the cRIO I/O Node Name Control (FPGA Module)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-crio-i-o-node-name-control-fp.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-crio-i-o-node-name-control-fp.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use cRIO I/O name controls to create reentrant subVIs with configurable I/O items. When you use a cRIO I/O control as an input on a subVI, the input accepts only I/O items that support a superset of the methods and properties you enable for the cRIO I/O control. All enabled methods must matc

### Configuring the cRIO I/O Node Name Control (FPGA Module)

You can use cRIO I/O name controls to create reentrant subVIs with configurable I/O items. When you use a cRIO I/O control as an input on a subVI, the input accepts only I/O items that support a superset of the methods and properties you enable for the cRIO I/O control. All enabled methods must match in name, and their parameters must match in name, order, and data type. All enabled properties must match in name and data type.

Complete the following steps to configure the cRIO I/O name control using the Configure cRIO I/O Name Control Type dialog box.

1. Right-click a cRIO I/O Device and select Configure I/O Type from the shortcut menu to display the Configure cRIO I/O Name Control Type dialog box.
2. Select a cRIO I/O item from the I/O Items list that supports all the methods and properties you plan to use with the cRIO I/O control. The methods and properties of the I/O item you select appear in the I/O Item Type list.
3. Click the Replace All button to copy all the methods and
 properties from the I/O Item Type list to the
 I/O Name Control Type list. 
 You cannot move individual I/O item types to the I/O Name Control
 Type box.
4. Click the Remove button to remove methods and properties
 from the I/O Name Control Type list that you do not want
 to require of I/O items passed to the control. 
 To make the control broadly reusable, remove any resource-specific methods and
 properties that you do not want to use with the cRIO I/O control. You can click
 an item in the I/O Name Control Type list and read about
 the item in the I/O Name Control Type Details section.
5. Click the OK button to close the dialog box.

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-data-rate-for-a-module-fpga-i.html language=enus -->
## TOPIC 00080: Configuring the Data Rate for a Module (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-data-rate-for-a-module-fpga-i.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-data-rate-for-a-module-fpga-i.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 95 C Series Modules with a Configurable Data Rate NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 NI 9252 NI 9253 NI 9260 NI 9770 NI 9775 You can configure the rate at which the module acq

### Configuring the Data Rate for a Module (FPGA Interface)

| NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 | NI 9230 NI 9231 NI 9232 NI 9234 NI 9235 | NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 | NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 | NI 9252 NI 9253 NI 9260 NI 9770 NI 9775 |
| --- | --- | --- | --- | --- |

You can configure the rate at which the module acquires and returns data at edit time using the
 C Series Module Properties dialog box.

To programmatically change the data rate at run time, use the FPGA I/O Property Node. The
 execution of an I/O Property Node that is configured with a Data Rate
 property overwrites the value you configured in the C Series Module Properties dialog box.

Parent topic:

Analog Input Modules

Related concepts:

- Loop Timing for the NI 9218 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-digital-in-threshold-for-the.html language=enus -->
## TOPIC 00081: Configuring the Digital In Threshold for the NI 9219 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-digital-in-threshold-for-the.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-digital-in-threshold-for-the.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channels in Digital In mode on the NI 9219 have a 0–60 V unipolar threshold. The default value of the Digital In mode threshold is 1.5 V. Configure the threshold at edit time using the C Series Module Properties dialog box. Programmatically change the threshold at run time using the FPGA I/O Propert

### Configuring the Digital In Threshold for the NI 9219 (FPGA Interface)

Channels in Digital In mode on the NI 9219 have a 0–60 V unipolar threshold. The default value of
 the Digital In mode threshold is 1.5 V. Configure the threshold at edit time using the
 *C Series Module Properties* dialog box. Programmatically change the
 threshold at run time using the FPGA I/O Property Node. The execution of an I/O Property
 Node that is configured with a Digital Threshold property
 overwrites the value you configured in the C Series Module
 Properties dialog box.

#### Configuring the Digital In Threshold Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the Digital In threshold for the NI 9219 using the C Series
 Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9219.
2. Right-click the NI 9219 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the Digital In threshold
 from the Channels table. You can select more than one
 channel by holding the < Ctrl > or
 < Shift > key when selecting channels.
4. Select Digital In from the Channel
 Mode pull-down menu.
5. Enter a value between 0 and 60 in the Threshold text box
 for the selected channel(s).
6. Click the OK button.
7. Select File»Save All in the Project
 Explorer window.

#### Configuring the Digital In Threshold Using the FPGA
 I/O Property Node

Complete the following steps to configure the Digital In
 threshold using the FPGA I/O Property Node.

1. Create FPGA I/O items for the channel of the NI 9219 for which you want to
 configure the Digital Threshold property. The channel
 must be set to Digital In mode.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 NI 9219 channel for which you want to configure the Digital In threshold.
3. Click the Property section and select Digital
 Threshold from the shortcut menu.
4. Right-click the Digital Threshold input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, enter a binary value in the Digital
 Threshold control. You can use the following equation in the
 host VI to calculate the threshold value: Threshold (binary) 
 = Threshold (volts) x 2 24 ÷ 60

You can change the Digital In threshold at run time by writing to the control
 from the host VI. Refer to the NI 9219 Digital Threshold VI in the
 labview\examples\CompactRIO\Module Specific\NI 9219\NI 9219 Digital
 Threshold\NI 9219 Digital Threshold.lvproj for an example of
 configuring the NI 9219 Digital In threshold using the FPGA I/O Property Node.

Parent topic:

NI 9219 (FPGA Interface)

Related concepts:

- Configuring a Project

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-host-memory-buffer.html language=enus -->
## TOPIC 00082: Configuring the Host Memory Buffer

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-host-memory-buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-host-memory-buffer.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some FPGA targets contain a host memory buffer that you can access directly from the FPGA VI. Use the memory item interface in the project to use the host memory buffer in the same way you use block memory and LUT. Host memory buffer items appear in the Project Explorer window under the FPGA target.

### Configuring the Host Memory Buffer

Some FPGA targets contain a host memory buffer that you can access directly from the FPGA VI. Use the memory item interface in the project to use the host memory buffer in the same way you use block memory and LUT. Host memory buffer items appear in the Project Explorer window under the FPGA target.

Most FPGA applications using the host memory buffer can take advantage of the usability and VHDL
 optimization that the FPGA memory item interface provides. You cannot use VI-defined
 memory items to configure the host memory buffer.

#### Determining Whether Host Memory Buffer is
 Available

Complete the following steps to determine whether host memory
 buffer is available for your target.

1. Display the Project Explorer window.
2. Right-click the FPGA target and select Memory Properties.
3. Open the Implementation drop-down list and select DRAM.
4. Open the DRAM bank drop-down list. If host memory buffer is available, it will
 be included in the list.

#### Partitioning the Physical Host Memory Buffer into
 Multiple Memory Items

You can use the FPGA memory item interface to
 partition the physical host memory buffer banks available on a target into multiple
 memory items. Use the Memory Properties dialog box to create and configure memory
 partitions on a host memory buffer bank. For example, if a target has two physical
 host memory buffer banks, you could partition one bank into three different memories
 and the other bank into five memories, as shown below. LabVIEW treats each memory
 independently of each other.

#### Understanding Latency and Host Memory Buffer

Access to the host memory buffer involves some non-deterministic latency.
 To compensate for this latency, use the Request Data and Retrieve Data methods to
 read data from the host memory buffer. You can queue multiple requests for data
 using the Request Data method and retrieve requested data using the Retrieve Data
 method. The host memory buffer returns requested data when you indicate you are
 ready to receive it using handshaking signals.

#### Data Recommendations

If you use a data
 type that is smaller than the access size, the remaining bits receive an unknown and
 invalid value, but still get written and take up both space and bandwidth. For
 example, if the access size is 64 bits wide and you choose a 32-bit data type when
 configuring the host memory buffer, the remaining 32 bits are of an unknown and
 invalid data type. The following figure shows an optimized memory element and a
 memory element in which the data type is smaller than the access size.

Figure 7.

[IMAGE alt='image' src='GUID-1F673878-01B6-439B-A1D1-B539A78FC43B-a5.svg']

NI recommends using data types that are exactly the same width as the access
 size of the host memory buffer to ensure that each access is optimized. Memory items
 accept clusters to be used as data types, and information can be packaged into
 clusters to achieve data types larger than those native to LabVIEW.

NI
 recommends that you push data into the memory item interface within the 40 MHz
 onboard clock domain. Right-click the FPGA target in a LabVIEW project, select
 New»Memory. Bandwidth is maximized when data is pushed
 into the memory item interface at the clock rate.

#### Request Pipelining

The host memory
 buffer architecture is highly pipelined, resulting in relatively long latency
 between data requests and the execution of the requests. NI recommends that
 prerequest samples, which helps maintain high throughput. To prerequest samples,
 request the samples you want to read without waiting for the data valid strobe of
 the retrieve method.

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-initial-line-direction-for-th.html language=enus -->
## TOPIC 00083: Configuring the Initial Line Direction for the NI 9401 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-initial-line-direction-for-th.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-initial-line-direction-for-th.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9401 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9401 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Initial Line Direction for the NI 9401 (FPGA Interface)

Each digital port on the NI 9401 is initially configured as a digital input. You can configure
 the initial line direction for each port on the NI 9401 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

#### Configuring Line Direction Using the C Series
 Module Properties Dialog Box

Complete the following steps to configure
 the line direction of each digital port using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9401.
2. Right-click the NI 9401 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the direction for each port from the Initial Line
 Direction pull-down menus.
4. Click the OK button.
5. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O
 Method Node

Complete the following steps to configure the line direction
 of each digital port using the FPGA I/O Method Node.

1. Place an FPGA I/O Method Node on the block diagram and configure it for the
 NI 9401.
2. Click the Method section and select the Set Line
 Direction method from the shortcut menu.
3. Right-click each digital port input and select
 Create»Control from the shortcut menu.
4. On the front panel of the VI, select the direction for each port from the
 digital port pull-down menus.

Parent topic:

NI 9401 (FPGA Interface)

Related concepts:

- NI 9401 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-initial-line-direction-for-th_2.html language=enus -->
## TOPIC 00084: Configuring the Initial Line Direction for the NI 9401 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-initial-line-direction-for-th_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-initial-line-direction-for-th_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9401 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9401 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Initial Line Direction for the NI 9401 (FPGA Interface)

Each digital port on the NI 9401 is initially configured as a digital input. You can configure
 the initial line direction for each port on the NI 9401 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

#### Configuring Line Direction Using the C Series
 Module Properties Dialog Box

Complete the following steps to configure
 the line direction of each digital port using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9401.
2. Right-click the NI 9401 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the direction for each port from the Initial Line
 Direction pull-down menus.
4. Click the OK button.
5. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O
 Method Node

Complete the following steps to configure the line direction
 of each digital port using the FPGA I/O Method Node.

1. Place an FPGA I/O Method Node on the block diagram and configure it for the
 NI 9401.
2. Click the Method section and select the Set Line
 Direction method from the shortcut menu.
3. Right-click each digital port input and select
 Create»Control from the shortcut menu.
4. On the front panel of the VI, select the direction for each port from the
 digital port pull-down menus.

Parent topic:

NI 9401 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-line-direction-for-the-ni-940-2.html language=enus -->
## TOPIC 00085: Configuring the Line Direction for the NI 9402 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-line-direction-for-the-ni-940-2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-line-direction-for-the-ni-940-2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9402 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9402 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Line Direction for the NI 9402 (FPGA Interface)

Each digital port on the NI 9402 is initially configured as a digital input. You can
 configure the initial line direction for each port on the NI 9402 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

The execution of an FPGA I/O Node configured for output automatically configures the line for
 output and overwrites the values you configured in the C Series Module
 Properties dialog box or using the Set Output Enable
 method.

#### Configuring Line Direction Using the C Series Module Properties Dialog Box

Complete the following steps to configure the line direction of each
 digital port using the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9402.
2. Right-click the NI 9402 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the line direction from
 the Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the direction for the channel(s) from the
 Direction pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O Method Node

Complete the
 following steps to configure the line direction of each digital port using the FPGA
 I/O Method Node.

1. Create FPGA I/O items for the channel of the NI 9402 for which you want to
 configure the line direction.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 channel.
3. Click the Method section and select the Set Line
 Direction method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, click the Enable Boolean
 control to set it to TRUE if you want to set the line
 direction of the channel to digital output.

#### Configuring Line Direction of Multiple Channels
 Using the FPGA I/O Method Node

Complete the following steps to set the
 line direction of multiple channels using the FPGA I/O Method Node.

1. Create FPGA I/O items for the DIO3:0 digital port of the NI 9402.
2. Place an FPGA I/O Method Node on the block diagram and configure it for the
 DIO3:0 digital port.
3. Click the Method section and select the Set Output
 Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. The
 Enable control appears as an unsigned 8-bit integer.
 Each bit in the integer represents the line direction of one channel of the
 NI 9402.
5. On the front panel of the VI, use the Enable control to
 enter the line direction for each channel in the port. Change a bit to 1 to set
 the line direction of the corresponding channel to digital output. Leave a bit
 as 0 to set the line direction of the corresponding channel to digital input.
 Refer to the table below for examples of what to enter in the
 Enable control. Table 389.Enable Control
 ValuesChannel Line Direction Configuration
 Enable Control(Floating Point)
 Enable Control(Binary)
 Enable Control(Hex)Change all channels to input
 0
 0000
 0x00
 Change all channels to output
 15
 1111
 0x0F
 Change channel 0 to output
 1
 0001
 0x01

Parent topic:

NI 9402 (FPGA Interface)

Related concepts:

- NI 9402 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-line-direction-for-the-ni-940-2_2.html language=enus -->
## TOPIC 00086: Configuring the Line Direction for the NI 9402 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-line-direction-for-the-ni-940-2_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-line-direction-for-the-ni-940-2_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9402 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9402 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Line Direction for the NI 9402 (FPGA Interface)

Each digital port on the NI 9402 is initially configured as a digital input. You can
 configure the initial line direction for each port on the NI 9402 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

The execution of an FPGA I/O Node configured for output automatically configures the line for
 output and overwrites the values you configured in the C Series Module
 Properties dialog box or using the Set Output Enable
 method.

#### Configuring Line Direction Using the C Series Module Properties Dialog Box

Complete the following steps to configure the line direction of each
 digital port using the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9402.
2. Right-click the NI 9402 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the line direction from
 the Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the direction for the channel(s) from the
 Direction pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O Method Node

Complete the
 following steps to configure the line direction of each digital port using the FPGA
 I/O Method Node.

1. Create FPGA I/O items for the channel of the NI 9402 for which you want to
 configure the line direction.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 channel.
3. Click the Method section and select the Set Line
 Direction method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, click the Enable Boolean
 control to set it to TRUE if you want to set the line
 direction of the channel to digital output.

#### Configuring Line Direction of Multiple Channels
 Using the FPGA I/O Method Node

Complete the following steps to set the
 line direction of multiple channels using the FPGA I/O Method Node.

1. Create FPGA I/O items for the DIO3:0 digital port of the NI 9402.
2. Place an FPGA I/O Method Node on the block diagram and configure it for the
 DIO3:0 digital port.
3. Click the Method section and select the Set Output
 Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. The
 Enable control appears as an unsigned 8-bit integer.
 Each bit in the integer represents the line direction of one channel of the
 NI 9402.
5. On the front panel of the VI, use the Enable control to
 enter the line direction for each channel in the port. Change a bit to 1 to set
 the line direction of the corresponding channel to digital output. Leave a bit
 as 0 to set the line direction of the corresponding channel to digital input.
 Refer to the table below for examples of what to enter in the
 Enable control. Table 453.Enable Control
 ValuesChannel Line Direction Configuration
 Enable Control(Floating Point)
 Enable Control(Binary)
 Enable Control(Hex)Change all channels to input
 0
 0000
 0x00
 Change all channels to output
 15
 1111
 0x0F
 Change channel 0 to output
 1
 0001
 0x01

Parent topic:

NI 9402 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-line-direction-for-the-ni-940.html language=enus -->
## TOPIC 00087: Configuring the Line Direction for the NI 9403 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-line-direction-for-the-ni-940.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-line-direction-for-the-ni-940.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9403 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9403 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Line Direction for the NI 9403 (FPGA Interface)

Each digital port on the NI 9403 is initially configured as a digital input. You can
 configure the initial line direction for each port on the NI 9403 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

The execution of an FPGA I/O Node configured for output automatically configures the line
 for output and overwrites the values you configured in the C Series Module
 Properties dialog box or using the Set Output Enable
 method.

#### Configuring Line Direction Using the C Series Module Properties Dialog Box

Complete the following steps to configure the line direction of each
 digital port using the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9403.
2. Right-click the NI 9403 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the line direction from
 the Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the direction for the channel(s) from the
 Direction pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O Method Node

Complete the
 following steps to configure the line direction of each digital port using the FPGA
 I/O Method Node.

1. Create FPGA I/O items for the channel of the NI 9403 for which you want to
 configure the line direction.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 channel.
3. Click the Method section and select the Set
 Output Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. Each bit in
 the integer represents the line direction of one channel of the NI 9403.
5. On the front panel of the VI, click the Enable Boolean
 control to set it to TRUE if you want to set the line
 direction of the channel to digital output.

#### Configuring Line Direction of Multiple Channels Using the FPGA I/O Method Node

Complete the following steps to set the line direction of multiple
 channels using the FPGA I/O Method Node.

1. Create FPGA I/O items for the digital port of the NI 9403 that contains the
 channels you want to configure.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 digital port.
3. Click the Method section and select the Set
 Output Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. Each bit in the integer represents the line direction of one channel of
 the NI 9403.
  - If you configured the FPGA I/O Method Node for the DIO7:0, DIO15:8,
 DIO23:16, or DIO31:24 digital port, the Enable control appears as an
 unsigned 8-bit integer.
  - If you configured the FPGA I/O Method Node for the DIO31:0 digital port,
 the Enable control appears as an unsigned 32-bit integer.
5. On the front panel of the VI, use the Enable control to
 enter the line direction for each channel in the port. Change a bit to 1 to set
 the line direction of the corresponding channel to digital output. Leave a bit
 as 0 to set the line direction of the corresponding channel to digital input.
 Refer to the table below for examples of what to enter in the
 Enable control if you configured the FPGA I/O Method
 Node for the DIO7:0 digital port. Table 394.Enable Control Values
 (DIO7:0)Channel Line Direction Configuration
 Enable Control (Hex)
 Enable Control (Binary)Change all channels to input
 0x00
 0b00000000
 Change all channels to output
 0xFF
 0b11111111
 Change channel 0 to output
 0x01
 0b00000001
 Change channels 0 through 5 to output
 0x3F
 0b00111111
 Change channels 3 and 7 to output
 0x88
 0b10001000 Refer to the table below for examples of what to enter in the
 Enable control if you configured the FPGA I/O Method
 Node for the DIO31:0 digital port. Table 395.Enable Control Values (DIO31:0)Channel Line Direction Configuration
 Enable Control (Hex)
 Enable Control (Binary)Change all channels to input
 0x00000000
 0b0000000000000000 0000000000000000
 Change all channels to output
 0xFFFFFFFF
 0b1111111111111111 1111111111111111
 Change channel 0 to output
 0x00000001
 0b0000000000000000 0000000000000001
 Change channels 0 through 5 to output
 0x0000003F
 0b0000000000000000 0000000000111111
 Change channels 3 and 7 to output
 0x00000088
 0b0000000000000000 0000000010001000

Parent topic:

NI 9403 (FPGA Interface)

Related concepts:

- NI 9403 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-line-direction-for-the-ni-940_2.html language=enus -->
## TOPIC 00088: Configuring the Line Direction for the NI 9403 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-line-direction-for-the-ni-940_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-line-direction-for-the-ni-940_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each digital port on the NI 9403 is initially configured as a digital input. You can configure the initial line direction for each port on the NI 9403 at edit time using the C Series Module Properties dialog box. Programmatically change the line direction for each port at run time using the FPGA I/O

### Configuring the Line Direction for the NI 9403 (FPGA Interface)

Each digital port on the NI 9403 is initially configured as a digital input. You can
 configure the initial line direction for each port on the NI 9403 at edit time using the
 C Series Module Properties dialog box.

Programmatically change the line direction for each port at run time using the FPGA I/O
 Method Node. The execution of an I/O Method Node that is configured with a Set
 Line Direction method overwrites the value you configured in the
 C Series Module Properties dialog box.

The execution of an FPGA I/O Node configured for output automatically configures the line
 for output and overwrites the values you configured in the C Series Module
 Properties dialog box or using the Set Output Enable
 method.

#### Configuring Line Direction Using the C Series Module Properties Dialog Box

Complete the following steps to configure the line direction of each
 digital port using the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an NI 9403.
2. Right-click the NI 9403 in the Project Explorer window
 and select Properties from the shortcut menu to display
 the C Series Module Properties dialog box.
3. Select the channel(s) for which you want to configure the line direction from
 the Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the direction for the channel(s) from the
 Direction pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring Line Direction Using the FPGA I/O Method Node

Complete the
 following steps to configure the line direction of each digital port using the FPGA
 I/O Method Node.

1. Create FPGA I/O items for the channel of the NI 9403 for which you want to
 configure the line direction.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 channel.
3. Click the Method section and select the Set
 Output Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. Each bit in
 the integer represents the line direction of one channel of the NI 9403.
5. On the front panel of the VI, click the Enable Boolean
 control to set it to TRUE if you want to set the line
 direction of the channel to digital output.

#### Configuring Line Direction of Multiple Channels Using the FPGA I/O Method Node

Complete the following steps to set the line direction of multiple
 channels using the FPGA I/O Method Node.

1. Create FPGA I/O items for the digital port of the NI 9403 that contains the
 channels you want to configure.
2. Place an FPGA I/O Method Node on the block diagram and configure it for this
 digital port.
3. Click the Method section and select the Set
 Output Enable method from the shortcut menu.
4. Right-click the Enable input and select
 Create»Control from the shortcut menu. Each bit in the integer represents the line direction of one channel of
 the NI 9403.
  - If you configured the FPGA I/O Method Node for the DIO7:0, DIO15:8,
 DIO23:16, or DIO31:24 digital port, the Enable control appears as an
 unsigned 8-bit integer.
  - If you configured the FPGA I/O Method Node for the DIO31:0 digital port,
 the Enable control appears as an unsigned 32-bit integer.
5. On the front panel of the VI, use the Enable control to
 enter the line direction for each channel in the port. Change a bit to 1 to set
 the line direction of the corresponding channel to digital output. Leave a bit
 as 0 to set the line direction of the corresponding channel to digital input.
 Refer to the table below for examples of what to enter in the
 Enable control if you configured the FPGA I/O Method
 Node for the DIO7:0 digital port. Table 458.Enable Control Values
 (DIO7:0)Channel Line Direction Configuration
 Enable Control (Hex)
 Enable Control (Binary)Change all channels to input
 0x00
 0b00000000
 Change all channels to output
 0xFF
 0b11111111
 Change channel 0 to output
 0x01
 0b00000001
 Change channels 0 through 5 to output
 0x3F
 0b00111111
 Change channels 3 and 7 to output
 0x88
 0b10001000 Refer to the table below for examples of what to enter in the
 Enable control if you configured the FPGA I/O Method
 Node for the DIO31:0 digital port. Table 459.Enable Control Values (DIO31:0)Channel Line Direction Configuration
 Enable Control (Hex)
 Enable Control (Binary)Change all channels to input
 0x00000000
 0b0000000000000000 0000000000000000
 Change all channels to output
 0xFFFFFFFF
 0b1111111111111111 1111111111111111
 Change channel 0 to output
 0x00000001
 0b0000000000000000 0000000000000001
 Change channels 0 through 5 to output
 0x0000003F
 0b0000000000000000 0000000000111111
 Change channels 3 and 7 to output
 0x00000088
 0b0000000000000000 0000000010001000

Parent topic:

NI 9403 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-master-module.html language=enus -->
## TOPIC 00089: Configuring the Master Module

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-master-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-master-module.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure the master module. Configure the system. Right-click the module you want to configure as the master in the Project Explorer window and select Properties. to display . The C Series Module Properties dialog box opens. Select <Onboard Clock> from the Master Tim

### Configuring the Master Module

Complete the following steps to configure the master module.

1. Configure the system.
2. Right-click the module you want to configure as the master in the
 Project Explorer window and select
 Properties. to display . 
 The C Series Module Properties dialog box opens.
3. Select <Onboard Clock> from the Master Timebase Source pull-down menu.
4. Enable the Export Onboard Clock checkbox.
5. Click the OK button.

Parent topic:

Synchronizing Multiple C Series Modules

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-master-timebase-source-for-a.html language=enus -->
## TOPIC 00090: Configuring the Master Timebase Source for a C Series Module (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-master-timebase-source-for-a.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-master-timebase-source-for-a.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: C Series modules with a selectable timebase source are listed in the following table.45 C Series Modules with a Selectable Timebase Source NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 N

### Configuring the Master Timebase Source for a
 C Series Module (FPGA Interface)

C Series modules with a selectable timebase source are
 listed in the following table.

| NI 9202 NI 9218 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 | NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 | NI 9242 NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 NI 9252 | NI 9253 NI 9260 NI 9469 NI 9770 NI 9775 NI 9470 |
| --- | --- | --- | --- |

In a system that contains more than one of these modules, you can configure one module as the
 master timebase source (master) and configure the other modules to
 use that master timebase source (slaves).

Sharing the same master timebase source allows you to synchronize multiple modules. The
 master timebase source is divided to acquire data at the data rate you configure.

Note

Note

Note

#### Configuring the Onboard Clock of a Module as the
 Master Timebase Source

Complete the following steps to configure the
 internal Onboard Clock of one module as the master timebase source.

1. Configure the CompactRIO system and add a module.
2. Right-click the module in the Project Explorer window and
 select Properties to launch the C Series
 Module Properties dialog box.
3. Select <Onboard Clock> from the Master
 Timebase Source pull-down menu.
4. Click the OK button.
5. Select File»Save All in the Project
 Explorer window.

#### Configuring a Master Module to Share the Master
 Timebase Source with Slaves

Complete the following steps to configure the
 master timebase source for a master module and share that timebase with slave
 modules.

1. Configure the CompactRIO system and add the module to use as the master.
2. Right-click the module in the Project Explorer window and
 select Properties to launch the C Series
 Module Properties dialog box.
3. Select <Onboard Clock> from the Master
 Timebase Source pull-down menu.
4. Enable the Export Onboard Clock checkbox.
5. Add a module you want to use as a slave.
6. Right-click the slave module in the Project Explorer 
 window and select Properties to display the C
 Series Module Properties dialog box.
7. Select the name of the master module from the Master Timebase
 Source pull-down menu.
8. Repeat steps 5 through 7 for each slave module you want to configure.
9. Click the OK button.
10. Select File»Save All in the Project
 Explorer window.

Parent topic:

Synchronizing Multiple Modules (FPGA Interface)

Related concepts:

- Configuring the Data Rate for a Module (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-minimum-time-between-conversi.html language=enus -->
## TOPIC 00091: Configuring the Minimum Time Between Conversions for the NI 9201/9221 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-minimum-time-between-conversi.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-minimum-time-between-conversi.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the minimum time between conversions for the NI 9201/9221 in the C Series Module Properties dialog box. Complete the following steps to configure the minimum time between conversions for the NI 9201/9221. Configure the CompactRIO system, and add an NI 9201/9221. Right-click the NI

### Configuring the Minimum Time Between Conversions for the NI 9201/9221 (FPGA Interface)

You can configure the minimum time between conversions for the NI 9201/9221 in the C
 Series Module Properties dialog box.

Complete the following steps to configure the minimum time between conversions for the NI 9201/9221.

1. Configure the CompactRIO system, and add an NI 9201/9221.
2. Right-click the NI 9201/9221 in the Project Explorer window and select
 Properties from the shortcut menu to display the C Series
 Module Properties dialog box.
3. Enter a value between 0 and 10 µs in increments of 25 ns in the Minimum Time Between Conversions text box.
4. Click the OK button.
5. Select File»Save All in the Project Explorer window.

Note

Minimum Time Between Conversions

The following table lists the minimum time between conversions when you are using a chassis
 *other than* the NI 9151 R Series Expansion chassis.

| Module | Sampling Data from a Singleor Channel or Multiple Channels? | Minimum Time Between Conversions | Able to Achieve the Specified Time Between Conversions? (Refer to the following Note) | Module Accuracy |
| --- | --- | --- | --- | --- |
| NI 9201 | Single | ≥ 1.25 µs | Yes | Module accuracy not affected |
| < 1.25 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2 µs | Yes | Module accuracy not affected |  |
| < 2 µs | No | Module accuracy degrades |  |  |
| NI 9221 | Single | ≥ 1.25 µs | Yes | Module accuracy not affected |
| < 1.25 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 1.25 µs | Yes | Module accuracy not affected |  |
| < 1.25 µs | No | Module accuracy degrades |  |  |

Set the minimum time between conversions in the C Series Module
 Properties dialog box.

Note

- Yes indicates that it is possible to write an FPGA VI
 that can sustain the minimum time between conversions specified in the C
 Series Module Properties dialog box.
- No indicates that the minimum time between conversions
 specified in the C Series Module Properties dialog box is too low and you
 may not be able to write an FPGA VI that can sustain the specified time.

The following table lists the minimum time between conversions when you are using the NI
 9151 R Series Expansion chassis.

| Module | Sampling Data from a Single Channel or Multiple Channels? | Minimum Time Between Conversions | Able to Achieve the Specified Time Between Conversions? (Refer to the following Note) | Module Accuracy |
| --- | --- | --- | --- | --- |
| NI 9201 | Single | ≥ 2.1 µs | Yes | Module accuracy not affected |
| < 2.1 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2.1 µs | Yes | Module accuracy not affected |  |
| < 2.1 µs and ≥ 2 µs | No | Module accuracy not affected |  |  |
| < 2 µs | No | Module accuracy degrades |  |  |
| NI 9221 | Single | ≥ 2.1 µs | Yes | Module accuracy not affected |
| < 2.1 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2.1 µs | Yes | Module accuracy not affected |  |
| < 2.1 µs and ≥ 1.25 µs | No | Module accuracy not affected |  |  |
| < 1.25 µs | No | Module accuracy degrades |  |  |

Set the minimum time between conversions in the C Series Module
 Properties dialog box.

Note

- Yes indicates that it is possible to write an FPGA VI
 that can sustain the minimum time between conversions specified in the C
 Series Module Properties dialog box.
- No indicates that the minimum time between conversions
 specified in the C Series Module Properties dialog box is too low and you
 may not be able to write an FPGA VI that can sustain the specified time.

Parent topic:

NI 9201 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-minimum-time-between-conversi_2.html language=enus -->
## TOPIC 00092: Configuring the Minimum Time Between Conversions for the NI 9201/9221 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-minimum-time-between-conversi_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-minimum-time-between-conversi_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the minimum time between conversions for the NI 9201/9221 in the C Series Module Properties dialog box. Complete the following steps to configure the minimum time between conversions for the NI 9201/9221. Configure the CompactRIO system, and add an NI 9201/9221. Right-click the NI

### Configuring the Minimum Time Between Conversions for the NI 9201/9221 (FPGA Interface)

You can configure the minimum time between conversions for the NI 9201/9221 in the C
 Series Module Properties dialog box.

Complete the following steps to configure the minimum time between conversions for the NI 9201/9221.

1. Configure the CompactRIO system, and add an NI 9201/9221.
2. Right-click the NI 9201/9221 in the Project Explorer window and select
 Properties from the shortcut menu to display the C Series
 Module Properties dialog box.
3. Enter a value between 0 and 10 µs in increments of 25 ns in the Minimum Time Between Conversions text box.
4. Click the OK button.
5. Select File»Save All in the Project Explorer window.

Note

Minimum Time Between Conversions

The following table lists the minimum time between conversions when you are using a chassis
 *other than* the NI 9151 R Series Expansion chassis.

| Module | Sampling Data from a Singleor Channel or Multiple Channels? | Minimum Time Between Conversions | Able to Achieve the Specified Time Between Conversions? (Refer to the following Note) | Module Accuracy |
| --- | --- | --- | --- | --- |
| NI 9201 | Single | ≥ 1.25 µs | Yes | Module accuracy not affected |
| < 1.25 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2 µs | Yes | Module accuracy not affected |  |
| < 2 µs | No | Module accuracy degrades |  |  |
| NI 9221 | Single | ≥ 1.25 µs | Yes | Module accuracy not affected |
| < 1.25 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 1.25 µs | Yes | Module accuracy not affected |  |
| < 1.25 µs | No | Module accuracy degrades |  |  |

Set the minimum time between conversions in the C Series Module
 Properties dialog box.

Note

- Yes indicates that it is possible to write an FPGA VI
 that can sustain the minimum time between conversions specified in the C
 Series Module Properties dialog box.
- No indicates that the minimum time between conversions
 specified in the C Series Module Properties dialog box is too low and you
 may not be able to write an FPGA VI that can sustain the specified time.

The following table lists the minimum time between conversions when you are using the NI
 9151 R Series Expansion chassis.

| Module | Sampling Data from a Single Channel or Multiple Channels? | Minimum Time Between Conversions | Able to Achieve the Specified Time Between Conversions? (Refer to the following Note) | Module Accuracy |
| --- | --- | --- | --- | --- |
| NI 9201 | Single | ≥ 2.1 µs | Yes | Module accuracy not affected |
| < 2.1 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2.1 µs | Yes | Module accuracy not affected |  |
| < 2.1 µs and ≥ 2 µs | No | Module accuracy not affected |  |  |
| < 2 µs | No | Module accuracy degrades |  |  |
| NI 9221 | Single | ≥ 2.1 µs | Yes | Module accuracy not affected |
| < 2.1 µs | No | Module accuracy not affected |  |  |
| Multiple | ≥ 2.1 µs | Yes | Module accuracy not affected |  |
| < 2.1 µs and ≥ 1.25 µs | No | Module accuracy not affected |  |  |
| < 1.25 µs | No | Module accuracy degrades |  |  |

Set the minimum time between conversions in the C Series Module
 Properties dialog box.

Note

- Yes indicates that it is possible to write an FPGA VI
 that can sustain the minimum time between conversions specified in the C
 Series Module Properties dialog box.
- No indicates that the minimum time between conversions
 specified in the C Series Module Properties dialog box is too low and you
 may not be able to write an FPGA VI that can sustain the specified time.

Parent topic:

NI 9221 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9230-9232-9234-channel-inp.html language=enus -->
## TOPIC 00093: Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9230-9232-9234-channel-inp.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9230-9232-9234-channel-inp.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is

### Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit
 time using the C Series Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the channel input modes using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA
 I/O Property Node

Complete the following steps to configure the channel
 input modes using the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

Change the channel input modes at run time by writing to the control from the
 host VI. For examples of how to configure the input modes using the FPGA I/O
 Property Node, refer to the following getting started VIs.

| Module | Example File Path |
| --- | --- |
| NI 9230 | labview\\examples\\CompactRIO\\Module Specific\\NI 9230\\NI 9230 Getting Started\\NI 9230 Getting Started.lvproj |
| NI 9232 | labview\\examples\\CompactRIO\\Module Specific\\NI 9232\\NI 9232 Getting Started\\NI 9232 Getting Started.lvproj |
| NI 9234 | labview\\examples\\CompactRIO\\Module Specific\\NI 9234\\NI 9234 Getting Started\\NI 9234 Getting Started.lvproj |

Note

Input Configuration

error
 65538

Stop
 channel

Parent topic:

NI 9230 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9230-9232-9234-channel-inp_2.html language=enus -->
## TOPIC 00094: Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9230-9232-9234-channel-inp_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9230-9232-9234-channel-inp_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is

### Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit
 time using the C Series Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the channel input modes using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA
 I/O Property Node

Complete the following steps to configure the channel
 input modes using the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

Change the channel input modes at run time by writing to the control from the
 host VI. For examples of how to configure the input modes using the FPGA I/O
 Property Node, refer to the following getting started VIs.

| Module | Example File Path |
| --- | --- |
| NI 9230 | labview\\examples\\CompactRIO\\Module Specific\\NI 9230\\NI 9230 Getting Started\\NI 9230 Getting Started.lvproj |
| NI 9232 | labview\\examples\\CompactRIO\\Module Specific\\NI 9232\\NI 9232 Getting Started\\NI 9232 Getting Started.lvproj |
| NI 9234 | labview\\examples\\CompactRIO\\Module Specific\\NI 9234\\NI 9234 Getting Started\\NI 9234 Getting Started.lvproj |

Note

Input Configuration

error
 65538

Stop
 channel

Parent topic:

NI 9232 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9230-9232-9234-channel-inp_3.html language=enus -->
## TOPIC 00095: Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9230-9232-9234-channel-inp_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9230-9232-9234-channel-inp_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is

### Configuring the NI 9230/9232/9234 Channel Input Modes (FPGA Interface)

You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit
 time using the C Series Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the channel input modes using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA
 I/O Property Node

Complete the following steps to configure the channel
 input modes using the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

Change the channel input modes at run time by writing to the control from the
 host VI. For examples of how to configure the input modes using the FPGA I/O
 Property Node, refer to the following getting started VIs.

| Module | Example File Path |
| --- | --- |
| NI 9230 | labview\\examples\\CompactRIO\\Module Specific\\NI 9230\\NI 9230 Getting Started\\NI 9230 Getting Started.lvproj |
| NI 9232 | labview\\examples\\CompactRIO\\Module Specific\\NI 9232\\NI 9232 Getting Started\\NI 9232 Getting Started.lvproj |
| NI 9234 | labview\\examples\\CompactRIO\\Module Specific\\NI 9234\\NI 9234 Getting Started\\NI 9234 Getting Started.lvproj |

Note

Input Configuration

error
 65538

Stop
 channel

Parent topic:

NI 9234 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9231-channel-input-modes-f.html language=enus -->
## TOPIC 00096: Configuring the NI 9231 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9231-channel-input-modes-f.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9231-channel-input-modes-f.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is

### Configuring the NI 9231 Channel Input Modes (FPGA Interface)

You can configure the input mode for each channel of the NI 9230, NI 9232, or NI 9234 at
 edit time using the C Series Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the channel input modes using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA
 I/O Property Node

Complete the following steps to configure the channel
 input modes using the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

You can change the channel input modes at run time by writing to the control
 from the host VI. Refer to the following getting started VIs for examples of how to
 configure the input modes using the FPGA I/O Property Node.

| Module | Example File Path |
| --- | --- |
| NI 9231 | labview\\examples\\CompactRIO\\Module Specific\\NI 9231\\NI 9231 Getting Started\\NI 9231 Getting Started.lvproj |

Note

Input Configuration

error
 65538

Stop
 channel

Parent topic:

NI 9231 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9250-channel-input-modes-f.html language=enus -->
## TOPIC 00097: Configuring the NI 9250 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9250-channel-input-modes-f.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9250-channel-input-modes-f.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the input mode for each channel at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is configured with an Input Configuration prop

### Configuring the NI 9250 Channel Input Modes (FPGA Interface)

Configure the input mode for each channel at edit time using the C Series
 Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C Series Module Properties Dialog Box

Complete the following steps to configure the channel input modes using
 the C Series Module Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA I/O Property Node

Complete the following steps to configure the channel input modes using
 the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

Change the channel input modes at run time by writing to the control from the
 host VI. For an example of how to configure the input modes using the FPGA I/O
 Property Node, refer to labview\examples\CompactRIO\Module Specific\NI
 9250\NI 9250 Getting Started\NI 9250 Getting Started.lvproj.

Note

Input
 Configuration

error 65538

Stop channel

Parent topic:

NI 9250 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-ni-9251-channel-input-modes-f.html language=enus -->
## TOPIC 00098: Configuring the NI 9251 Channel Input Modes (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-ni-9251-channel-input-modes-f.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-ni-9251-channel-input-modes-f.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the input mode for each channel at edit time using the C Series Module Properties dialog box. Programmatically change the input mode for each channel at run time using the FPGA I/O Property Node. The execution of an FPGA I/O Property Node that is configured with an Input Configuration prop

### Configuring the NI 9251 Channel Input Modes (FPGA Interface)

Configure the input mode for each channel at edit time using the C Series
 Module Properties dialog box.

Programmatically change the input mode for each channel at run time using the FPGA I/O
 Property Node. The execution of an FPGA I/O Property Node that is configured with an
 Input Configuration property overwrites the value you
 configured in the C Series Module Properties dialog box for the
 corresponding channel.

#### Configuring the Channel Input Modes Using the C
 Series Module Properties Dialog Box

Complete the following steps to
 configure the channel input modes using the C Series Module
 Properties dialog box.

1. Configure the CompactRIO system, and add an module.
2. Right-click the module in the Project Explorer window and
 select Properties to display the C Series
 Module Properties dialog box.
3. Select the channel(s) for which you want to configure the input mode from the
 Channels table. You can select more than one channel
 by holding the < Ctrl > or < Shift >
 key when selecting channels.
4. Select the input mode for the selected channel(s) from the Input
 Configuration pull-down menu.
5. Click the OK button.
6. Select File»Save All in the Project
 Explorer window.

#### Configuring the Channel Input Modes Using the FPGA I/O Property Node

Complete the following steps to configure the channel input modes using
 the FPGA I/O Property Node.

1. Create FPGA I/O items for the channels of the module for which you want to
 configure the Input Configuration property.
2. Place an FPGA I/O Property Node on the block diagram and configure it for the
 module channel for which you want to configure the input mode.
3. Click the Property section and select Input
 Configuration from the shortcut menu.
4. Right-click the Input Configuration input and select
 Create»Control from the shortcut menu.
5. On the front panel of the VI, select an input mode for the channel from the
 Input Configuration pull-down menu.

Change the channel input modes at run time by writing to the control from the
 host VI. For an example of how to configure the input modes using the FPGA I/O
 Property Node, refer to labview\examples\CompactRIO\Module Specific\NI
 9251\NI 9251 Getting Started\NI 9251 Getting Started.lvproj.

Note

Input
 Configuration

error 65538

Stop channel

Parent topic:

NI 9251 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=configuring-the-slave-modules.html language=enus -->
## TOPIC 00099: Configuring the Slave Modules

- bundle_id: `ni-compactrio`
- source_path: `configuring-the-slave-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/configuring-the-slave-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure the slave modules. Right-click the module you want to configure as a slave in the Project Explorer window and select Properties. The C Series Module Properties dialog box opens. Select the name of the master module from the Master Timebase Source pull-down m

### Configuring the Slave Modules

Complete the following steps to configure the slave modules.

1. Right-click the module you want to configure as a slave in the
 Project Explorer window and select
 Properties. 
 The C Series Module Properties dialog box opens.
2. Select the name of the master module from the Master Timebase Source pull-down menu.
3. Repeat steps 1 and 2 for each slave module you want to configure.
4. Click the OK button.
5. Select File»Save All in the Project Explorer window.

Parent topic:

Synchronizing Multiple C Series Modules

<!--NI_TOPIC bundle=ni-compactrio path=confirming-state-of-sleep-channel.html language=enus -->
## TOPIC 00100: Confirming the State of the Sleep Channel

- bundle_id: `ni-compactrio`
- source_path: `confirming-state-of-sleep-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/confirming-state-of-sleep-channel.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to read the state of the Sleep channel. Place another FPGA I/O Node function on the block diagram. This FPGA I/O Node must execute after the FPGA I/O Node you added above. Click the element section of the FPGA I/O Node and select Chassis I/O»Sleep or Onboard I/O»Sleep. R

### Confirming the State of the Sleep
 Channel

Complete the following steps to read the
 state of the Sleep channel.

1. Place another FPGA I/O Node function on the block diagram. This FPGA I/O Node
 must execute after the FPGA I/O Node you added above.
2. Click the element section of the FPGA I/O Node and select Chassis
 I/O»Sleep or Onboard I/O»Sleep.
3. Right-click the FPGA I/O Node and select Change to
 Read.
4. Right-click the Sleep output of the FPGA I/O Node and
 select Create»Indicator.

Parent topic:

Enabling Sleep Mode on a CompactRIO Chassis, Ethernet RIO Chassis, MXIe-RIO Chassis, or sbRIO Device

<!--NI_TOPIC bundle=ni-compactrio path=connecting-hall-effect-sensors-for-trapezoida.html language=enus -->
## TOPIC 00101: Connecting Hall Effect Sensors for Trapezoidal Commutation (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `connecting-hall-effect-sensors-for-trapezoida.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/connecting-hall-effect-sensors-for-trapezoida.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Hall 1 input, Hall 2 input, and Hall 3 inputs to connect the motor Hall effect sensors. For proper phase switching to occur during Trapezoidal commutation mode, the Hall sensors from the motor must be connected to the correct Hall inputs on the NI 9502 module. The Hall sensor phase sequence

### Connecting Hall Effect Sensors for Trapezoidal Commutation (FPGA Interface)

Use the Hall 1 input, Hall 2 input, and Hall 3 inputs to connect the motor Hall effect sensors.
 For proper phase switching to occur during Trapezoidal commutation mode, the Hall
 sensors from the motor must be connected to the correct Hall inputs on the NI 9502
 module. The Hall sensor phase sequence is motor-dependent, so selecting the correct
 inputs may require manually testing the motor wiring.

The following tutorial walks you through the Hall sensor connections for the NI 9502 using the 9502 Trapezoidal Commutation example installed in the labview\examples\CompactRIO\Module Specific\NI 9502\Trapezoidal Commutation directory. It is recommended that you print out this topic so that you can fill in the table provided below.

1. Connect the motor and Hall sensor inputs to the drive, but do not connect the motor to a load.
2. Open the 9502 Trapezoidal Commutation example.
3. Configure the example for your FPGA target.
 Refer to *Moving Examples to Another FPGA
 Target* at zone.ni.com for
 information about how to do this.
4. Open the 9502 Trapezoidal Commutation desktop VI.
5. Ensure that the NI 9502 is in Trapezoidal Commutation mode by right-clicking the NI 9502 item in the Project Explorer window and selecting Properties from the shortcut menu.
6. Compile the FPGA VI.
7. Run the RT VI.
8. With the hall wiring property set to the default of 1, 2, 3, enter a very small positive velocity (such as 20 RPM) in the Velocity Setpoint (rpm) control.
9. Click the Enable button to enable the drive and move the motor.
10. Record the highest velocity returned in the Positive Velocity column. The velocity is returned in the Velocity (rpm) graph on the front panel: Figure 140.Velocity Graph on the Front Panel[IMAGE alt='image' src='GUID-C2CDE0A9-5E06-49FB-8348-6CC2CF8073FB-a5.svg']
Note 

 If the motor moves erratically or not at all, place an X in both velocity columns, as this wiring scheme can be eliminated.
11. Click the Enable button again to disable the drive and stop the motor.
12. Enter the same velocity as a negative number in the Velocity Setpoint control.
13. Click the Enable Drive button to enable the drive and move the motor.
14. Record the highest velocity returned in the Negative Velocity column.
15. Click the Enable Drive button again to disable the drive and stop the motor.
16. Repeat steps 8 through 15 for the other five possible wiring combinations.
17. Stop the VI using the Stop button.

When the table is complete, look for the hall wiring value where the
 velocities in both directions were closest to the
 setpoint. This is the setting to use for your
 system. If these steps did not provide a conclusive
 result, repeat the test with a higher
 Velocity Setpoint. Once you
 have the correct hall wiring
 setting configure the PID gains as appropriate for
 your system and complete your application.

| Hall Wiring Property Setting | Positive Velocity | Negative Velocity |
| --- | --- | --- |
| 1, 2, 3 |  |  |
| 1, 3, 2 |  |  |
| 2, 1, 3 |  |  |
| 2, 3, 1 |  |  |
| 3, 1, 2 |  |  |
| 3, 2, 1 |  |  |

Parent topic:

NI 9502 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=conversion-timing-9204-05-06.html language=enus -->
## TOPIC 00102: Conversion Timing for the NI 9204/9205/9206 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `conversion-timing-9204-05-06.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/conversion-timing-9204-05-06.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9204, NI 9205, and NI 9206 modules implement a two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only) channels. This pipeline results in maximum sample rate and maximum sample quality. The Trig channel has a parallel data path that bypasses the pipeline.When using th

### Conversion Timing for the NI 9204/9205/9206
 (FPGA Interface)

The *NI 9204*, *NI 9205*, and *NI 9206* modules implement a
 two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only)
 channels. This pipeline results in maximum sample rate and maximum sample quality. The
 Trig channel has a parallel data path that bypasses the pipeline.

When using the FPGA I/O Node to sample channels, the pipeline is automatically managed by the
 FPGA I/O Node, and the channels within the FPGA I/O Node are sampled in numerical order
 regardless of the order they appear in the node.

If the first two channel requests in the FPGA I/O Node do not match the two channel requests stored in the module pipeline, there will be a delay before the first channel sample occurs. This delay is caused by the FPGA I/O Node automatically updating the module channel sample pipeline, which takes two channel sample cycles.

To minimize the need for the pipeline updates, each FPGA I/O Node leaves the module pipeline primed to repeat itself. If you use only one FPGA I/O Node in a looping structure, only the first iteration of the loop will incur the two-cycle time delay. All subsequent iterations operate with no delay.

IO Sample

- To read one channel, that channel configuration must be requested two cycles
 before the time it is to be sampled. The U16 configuration value for an AI
 channel sample contains the channel number, channel input range, and terminal
 mode. The U16 configuration value also can represent an access to the DIO or DOO
 (NI 9205/9206 only) channels, which is treated the same as an AI operation.

The following diagram illustrates how the pipeline works within a sequence structure. A typical
 application uses a loop structure to continuously iterate through a scan list. The scan
 list is a predefined list of configurations. The sequence structure and art elements
 show how data moves into the NI 9204/9205/9206 pipeline and then is converted. The
 IO Sample method first converts the configuration that is in the
 ADC, and then shifts the configuration values through the pipeline to prepare for the
 next time LabVIEW calls the IO Sample method.

Figure 25.

[IMAGE alt='image' src='GUID-8F414C3E-A9AF-412E-9CA0-6BB87C9C2F60-a5.svg']

The simplest form of pipeline management is to force the pipeline on every set of samples. This assumes that the pipeline is always wrong at the first sample, and sends all IO Sample requests in order. The last two data points need some configuration to be requested, but it does not matter, in this use case, what configuration that is.

Tip

- Smaller on FPGA—With large channel count, the IO Sample method is more efficient with FPGA resources, and thus requires less space on the FPGA for the same application.
- Sample flexibility—The IO Sample method gives you more flexibility to change channel range, terminal mode, and channel order at run time and at full sample rate.
- Application timing flexibility—The IO Sample method returns all sample data as soon as it is available. The FPGA I/O Node will gather data for all requested samples and then return all at once.

The Minimum Time Between Conversions control you can set in the *C Series Module Properties* dialog box determines the shortest possible time between any two conversions. For channels sampled within the same FPGA I/O Node, the time you set determines the exact time between conversions. For channels sampled within separate FPGA I/O Nodes or for conversions caused by looping on an FPGA I/O Node, the time you set may be less than the actual time between conversions. However, the minimum time you set is never greater than the time between conversions. If the application tries to execute an FPGA I/O Node or IO Sample method faster than the specified minimum time between conversions, the conversion is delayed until the minimum time you set is satisfied.

The default minimum time between conversions for the NI 9204/9205/9206 is 8 µs. The accuracy
 specifications in the NI 9204, NI 9205, and NI 9206 hardware documentation on
 ni.com/docs are based on this default value. If you set the minimum time between
 conversions to at least 8 µs, the accuracy of the module is not affected. If you set the
 minimum time between conversions to less than 8 µs, the accuracy of the module degrades
 if you sample data from multiple channels.

#### Examples

Refer to the NI 9204 Advanced IO VI in thelabview\examples\CompactRIO\Module Specific\NI 9204\NI 9204 Advanced IO\NI 9204
 Advanced IO.lvproj for an example of conversion timing on the NI 9204 C
 Series Module.

Refer to the NI 9205 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9205\NI 9205 Advanced
 IO\NI 9205 Advanced IO.lvproj for an example of conversion timing on
 the NI 9205 and NI 9206 C Series Modules.

Parent topic:

NI 9204 (FPGA Interface)

Related concepts:

- NI 9204 (FPGA Interface)
- NI 9205 (FPGA Interface)
- NI 9206 (FPGA Interface)
- IO Sample Method (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=conversion-timing-9204-05-06_2.html language=enus -->
## TOPIC 00103: Conversion Timing for the NI 9204/9205/9206 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `conversion-timing-9204-05-06_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/conversion-timing-9204-05-06_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9204, NI 9205, and NI 9206 modules implement a two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only) channels. This pipeline results in maximum sample rate and maximum sample quality. The Trig channel has a parallel data path that bypasses the pipeline.When using th

### Conversion Timing for the NI 9204/9205/9206
 (FPGA Interface)

The *NI 9204*, *NI 9205*, and *NI 9206* modules implement a
 two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only)
 channels. This pipeline results in maximum sample rate and maximum sample quality. The
 Trig channel has a parallel data path that bypasses the pipeline.

When using the FPGA I/O Node to sample channels, the pipeline is automatically managed by the
 FPGA I/O Node, and the channels within the FPGA I/O Node are sampled in numerical order
 regardless of the order they appear in the node.

If the first two channel requests in the FPGA I/O Node do not match the two channel requests stored in the module pipeline, there will be a delay before the first channel sample occurs. This delay is caused by the FPGA I/O Node automatically updating the module channel sample pipeline, which takes two channel sample cycles.

To minimize the need for the pipeline updates, each FPGA I/O Node leaves the module pipeline primed to repeat itself. If you use only one FPGA I/O Node in a looping structure, only the first iteration of the loop will incur the two-cycle time delay. All subsequent iterations operate with no delay.

IO Sample

- To read one channel, that channel configuration must be requested two cycles
 before the time it is to be sampled. The U16 configuration value for an AI
 channel sample contains the channel number, channel input range, and terminal
 mode. The U16 configuration value also can represent an access to the DIO or DOO
 (NI 9205/9206 only) channels, which is treated the same as an AI operation.

The following diagram illustrates how the pipeline works within a sequence structure. A typical
 application uses a loop structure to continuously iterate through a scan list. The scan
 list is a predefined list of configurations. The sequence structure and art elements
 show how data moves into the NI 9204/9205/9206 pipeline and then is converted. The
 IO Sample method first converts the configuration that is in the
 ADC, and then shifts the configuration values through the pipeline to prepare for the
 next time LabVIEW calls the IO Sample method.

Figure 27.

[IMAGE alt='image' src='GUID-8F414C3E-A9AF-412E-9CA0-6BB87C9C2F60-a5.svg']

The simplest form of pipeline management is to force the pipeline on every set of samples. This assumes that the pipeline is always wrong at the first sample, and sends all IO Sample requests in order. The last two data points need some configuration to be requested, but it does not matter, in this use case, what configuration that is.

Tip

- Smaller on FPGA—With large channel count, the IO Sample method is more efficient with FPGA resources, and thus requires less space on the FPGA for the same application.
- Sample flexibility—The IO Sample method gives you more flexibility to change channel range, terminal mode, and channel order at run time and at full sample rate.
- Application timing flexibility—The IO Sample method returns all sample data as soon as it is available. The FPGA I/O Node will gather data for all requested samples and then return all at once.

The Minimum Time Between Conversions control you can set in the *C Series Module Properties* dialog box determines the shortest possible time between any two conversions. For channels sampled within the same FPGA I/O Node, the time you set determines the exact time between conversions. For channels sampled within separate FPGA I/O Nodes or for conversions caused by looping on an FPGA I/O Node, the time you set may be less than the actual time between conversions. However, the minimum time you set is never greater than the time between conversions. If the application tries to execute an FPGA I/O Node or IO Sample method faster than the specified minimum time between conversions, the conversion is delayed until the minimum time you set is satisfied.

The default minimum time between conversions for the NI 9204/9205/9206 is 8 µs. The accuracy
 specifications in the NI 9204, NI 9205, and NI 9206 hardware documentation on
 ni.com/docs are based on this default value. If you set the minimum time between
 conversions to at least 8 µs, the accuracy of the module is not affected. If you set the
 minimum time between conversions to less than 8 µs, the accuracy of the module degrades
 if you sample data from multiple channels.

#### Examples

Refer to the NI 9204 Advanced IO VI in thelabview\examples\CompactRIO\Module Specific\NI 9204\NI 9204 Advanced IO\NI 9204
 Advanced IO.lvproj for an example of conversion timing on the NI 9204 C
 Series Module.

Refer to the NI 9205 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9205\NI 9205 Advanced
 IO\NI 9205 Advanced IO.lvproj for an example of conversion timing on
 the NI 9205 and NI 9206 C Series Modules.

Parent topic:

NI 9205 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=conversion-timing-9204-05-06_3.html language=enus -->
## TOPIC 00104: Conversion Timing for the NI 9204/9205/9206 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `conversion-timing-9204-05-06_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/conversion-timing-9204-05-06_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9204, NI 9205, and NI 9206 modules implement a two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only) channels. This pipeline results in maximum sample rate and maximum sample quality. The Trig channel has a parallel data path that bypasses the pipeline.When using th

### Conversion Timing for the NI 9204/9205/9206
 (FPGA Interface)

The *NI 9204*, *NI 9205*, and *NI 9206* modules implement a
 two-element deep pipeline for access to the AI, DI0, and DO0 (NI 9205/9206 only)
 channels. This pipeline results in maximum sample rate and maximum sample quality. The
 Trig channel has a parallel data path that bypasses the pipeline.

When using the FPGA I/O Node to sample channels, the pipeline is automatically managed by the
 FPGA I/O Node, and the channels within the FPGA I/O Node are sampled in numerical order
 regardless of the order they appear in the node.

If the first two channel requests in the FPGA I/O Node do not match the two channel requests stored in the module pipeline, there will be a delay before the first channel sample occurs. This delay is caused by the FPGA I/O Node automatically updating the module channel sample pipeline, which takes two channel sample cycles.

To minimize the need for the pipeline updates, each FPGA I/O Node leaves the module pipeline primed to repeat itself. If you use only one FPGA I/O Node in a looping structure, only the first iteration of the loop will incur the two-cycle time delay. All subsequent iterations operate with no delay.

IO Sample

- To read one channel, that channel configuration must be requested two cycles
 before the time it is to be sampled. The U16 configuration value for an AI
 channel sample contains the channel number, channel input range, and terminal
 mode. The U16 configuration value also can represent an access to the DIO or DOO
 (NI 9205/9206 only) channels, which is treated the same as an AI operation.

The following diagram illustrates how the pipeline works within a sequence structure. A typical
 application uses a loop structure to continuously iterate through a scan list. The scan
 list is a predefined list of configurations. The sequence structure and art elements
 show how data moves into the NI 9204/9205/9206 pipeline and then is converted. The
 IO Sample method first converts the configuration that is in the
 ADC, and then shifts the configuration values through the pipeline to prepare for the
 next time LabVIEW calls the IO Sample method.

Figure 29.

[IMAGE alt='image' src='GUID-8F414C3E-A9AF-412E-9CA0-6BB87C9C2F60-a5.svg']

The simplest form of pipeline management is to force the pipeline on every set of samples. This assumes that the pipeline is always wrong at the first sample, and sends all IO Sample requests in order. The last two data points need some configuration to be requested, but it does not matter, in this use case, what configuration that is.

Tip

- Smaller on FPGA—With large channel count, the IO Sample method is more efficient with FPGA resources, and thus requires less space on the FPGA for the same application.
- Sample flexibility—The IO Sample method gives you more flexibility to change channel range, terminal mode, and channel order at run time and at full sample rate.
- Application timing flexibility—The IO Sample method returns all sample data as soon as it is available. The FPGA I/O Node will gather data for all requested samples and then return all at once.

The Minimum Time Between Conversions control you can set in the *C Series Module Properties* dialog box determines the shortest possible time between any two conversions. For channels sampled within the same FPGA I/O Node, the time you set determines the exact time between conversions. For channels sampled within separate FPGA I/O Nodes or for conversions caused by looping on an FPGA I/O Node, the time you set may be less than the actual time between conversions. However, the minimum time you set is never greater than the time between conversions. If the application tries to execute an FPGA I/O Node or IO Sample method faster than the specified minimum time between conversions, the conversion is delayed until the minimum time you set is satisfied.

The default minimum time between conversions for the NI 9204/9205/9206 is 8 µs. The accuracy
 specifications in the NI 9204, NI 9205, and NI 9206 hardware documentation on
 ni.com/docs are based on this default value. If you set the minimum time between
 conversions to at least 8 µs, the accuracy of the module is not affected. If you set the
 minimum time between conversions to less than 8 µs, the accuracy of the module degrades
 if you sample data from multiple channels.

#### Examples

Refer to the NI 9204 Advanced IO VI in thelabview\examples\CompactRIO\Module Specific\NI 9204\NI 9204 Advanced IO\NI 9204
 Advanced IO.lvproj for an example of conversion timing on the NI 9204 C
 Series Module.

Refer to the NI 9205 Advanced IO VI in the
 labview\examples\CompactRIO\Module Specific\NI 9205\NI 9205 Advanced
 IO\NI 9205 Advanced IO.lvproj for an example of conversion timing on
 the NI 9205 and NI 9206 C Series Modules.

Parent topic:

NI 9206 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=conversion-timing-for-the-ni-elvis-iii-fpga-i.html language=enus -->
## TOPIC 00105: Conversion Timing for the NI ELVIS III (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `conversion-timing-for-the-ni-elvis-iii-fpga-i.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/conversion-timing-for-the-ni-elvis-iii-fpga-i.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI ELVIS III implements a one-element deep pipeline to access the AI channels per connector. This pipeline results in maximum sample rate, but may not result in the best resolution. To achieve better resolution, you will need to add your own loop delay and slow down the sampling rate. When using

### Conversion Timing for the NI ELVIS III (FPGA Interface)

The NI ELVIS III implements a one-element deep pipeline to access the AI channels per connector.
 This pipeline results in maximum sample rate, but may not result in the best resolution.
 To achieve better resolution, you will need to add your own loop delay and slow down the
 sampling rate. When using the FPGA I/O Node to sample channels, the pipeline is
 automatically managed by the FPGA I/O Node, and the channels within the FPGA I/O Node
 are sampled in numerical order regardless of the order they appear in the node.

If the first channel request in the FPGA I/O Node does not match the first channel request stored in the module pipeline, there will be a delay before the first sample occurs. This delay is caused by the input settling time, which is required for the input value to reach a steady level before starting conversion.

If the next channel request in the FPGA I/O Node matches the previous channel request, no delay
 occurs because that channel has already settled. If a change occurs in the
 Voltage Range setting and Terminal Mode
 setting,the FPGA I/O Node waits for the settling delay.

Conversion Time

40 ticks

40,000 ticks

25 ns

75 ticks

- Set Conversion Time to 40 ticks 
 to scan through the channel list at 1 MS/s at a
 lower resolution.
- Set Conversion Time to 40,000
 ticks to scan through the channel list at 1
 kS/s at a higher resolution.

When using the IO Sample method, take steps to manage this pipeline in the
 VIs. To read one channel,make the request one cycle before the sample time.

The following diagram illustrates how the pipeline works within a sequence structure. A
 typical application would use a loop structure to iterate through a scan list, which is
 a predefined list of channels and settings, continuously. The sequence structure shows
 how data moves into the ELVIS III pipeline and then is converted.

Figure 194.

[IMAGE alt='NI Elvis III Pipeline Sequence Structure, Typical' src='GUID-8F414C3E-A9AF-412E-9CA0-6BB87C9C2F60-a5.svg']

Parent topic:

NI ELVIS III (FPGA Interface)

Related concepts:

- NI ELVIS III (FPGA Interface)
- IO Sample Method (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ai-for-sbrio-9628-29-38.html language=enus -->
## TOPIC 00106: Converting Analog Input Values for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ai-for-sbrio-9628-29-38.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ai-for-sbrio-9628-29-38.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure the FPGA I/O Node to return calibrated, fixed-point data for the onboard analog input module, set the Calibration Mode to Calibrated in the Module Properties dialog box for the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns uncalibrated, binary values. Convert th

### Converting Analog Input Values for the sbRIO-9628/9629/9638 (FPGA Interface)

To configure the FPGA I/O Node to return calibrated, fixed-point data for the onboard
 analog input module, set the Calibration Mode to
 Calibrated in the Module Properties dialog box
 for the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns uncalibrated, binary values. Convert the binary values to
 calibrated volts by applying the calibration constants. The conversion of binary data to
 calibrated data can be done in the host VI.

#### Using an Equation to Convert and Calibrate Values

Use the following equation in the host VI to convert binary analog input
 values to calibrated volts:

Volts =
 (Binary Value × LSB Weight -
 Offset)

where

- Binary Value is the signed value returned by the FPGA I/O
 Node.
- LSB Weight is the value returned by the LSB Weight
 property.
- Offset is the value returned by the Offset property.
- The LSB Weight property is returned in units of pV/LSB. The
 Offset property is returned in units of nV.

To convert to calibrated volts, use the FPGA I/O Property Node to read the
 LSB Weight and Offset properties for the
 desired input range. If you do not want to read the LSB Weight and Offset values
 from the module, you can convert to uncalibrated engineering units by using the
 following typical values for Offset and LSB
 Weight:

Offset = 0 V

The typical LSB Weight depends on the input
 range. The following table lists the LSB weight value for each input
 range.

| Input Range | Typical LSB Weight |
| --- | --- |
| ±10 V | 320 µV/LSB |
| ±5 V | 160 µV/LSB |
| ±2 V | 64 µV/LSB |
| ±1 V | 32 µV/LSB |

Parent topic:

sbRIO-9628

<!--NI_TOPIC bundle=ni-compactrio path=converting-ai-for-sbrio-9628-29-38_2.html language=enus -->
## TOPIC 00107: Converting Analog Input Values for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ai-for-sbrio-9628-29-38_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ai-for-sbrio-9628-29-38_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure the FPGA I/O Node to return calibrated, fixed-point data for the onboard analog input module, set the Calibration Mode to Calibrated in the Module Properties dialog box for the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns uncalibrated, binary values. Convert th

### Converting Analog Input Values for the sbRIO-9628/9629/9638 (FPGA Interface)

To configure the FPGA I/O Node to return calibrated, fixed-point data for the onboard
 analog input module, set the Calibration Mode to
 Calibrated in the Module Properties dialog box
 for the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns uncalibrated, binary values. Convert the binary values to
 calibrated volts by applying the calibration constants. The conversion of binary data to
 calibrated data can be done in the host VI.

#### Using an Equation to Convert and Calibrate Values

Use the following equation in the host VI to convert binary analog input
 values to calibrated volts:

Volts =
 (Binary Value × LSB Weight -
 Offset)

where

- Binary Value is the signed value returned by the FPGA I/O
 Node.
- LSB Weight is the value returned by the LSB Weight
 property.
- Offset is the value returned by the Offset property.
- The LSB Weight property is returned in units of pV/LSB. The
 Offset property is returned in units of nV.

To convert to calibrated volts, use the FPGA I/O Property Node to read the
 LSB Weight and Offset properties for the
 desired input range. If you do not want to read the LSB Weight and Offset values
 from the module, you can convert to uncalibrated engineering units by using the
 following typical values for Offset and LSB
 Weight:

Offset = 0 V

The typical LSB Weight depends on the input
 range. The following table lists the LSB weight value for each input
 range.

| Input Range | Typical LSB Weight |
| --- | --- |
| ±10 V | 320 µV/LSB |
| ±5 V | 160 µV/LSB |
| ±2 V | 64 µV/LSB |
| ±1 V | 32 µV/LSB |

Parent topic:

sbRIO-9638

<!--NI_TOPIC bundle=ni-compactrio path=converting-and-calibrating-compactrio-analog.html language=enus -->
## TOPIC 00108: Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-and-calibrating-compactrio-analog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-and-calibrating-compactrio-analog.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the calibration mode for an analog input module using the C Series Module Properties dialog box for the module. Available options are Calibrated and Raw. The Calibrated option configures the FPGA I/O Node to return calibrated, fixed-point data for the analog input module. The Raw option co

### Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

C Series
 Module Properties

Calibrated

Raw

- The Calibrated option configures the FPGA I/O Node to return
 calibrated, fixed-point data for the analog input module.
- The Raw option configures the FPGA I/O Node to return
 uncalibrated, binary values for the following analog input modules.

| NI 9201 NI 9203 NI 9204 NI 9205 NI 9206 NI 9215 NI 9216 NI 9217[1]1 After converting binary values to engineering units for the NI-9217, you can convert the nominal resistance values to temperature. NI 9218 | NI 9220 NI 9221 NI 9222 NI 9223 NI 9225 NI 9226 NI 9227 NI 9229 NI 9230 | NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9246 NI 9247 NI 9381 |
| --- | --- | --- |

When Calibrated is set to Raw, you must convert the
 binary values into meaningful engineering units and apply calibration constants. for
 higher accuracy. Convert and calibrate the values in the host VI.

The binary data returned by some modules is already calibrated. The following table lists
 the modules that return calibrated, binary data.

| NI 9202 NI 9207 NI 9208 NI 9211 NI 9212 NI 9213 | NI 9214 NI 9219 NI 9224 NI 9228 NI 9231 NI 9242 | NI 9244 NI 9250 NI 9251 NI 9252 NI 9253 NI 9320 |
| --- | --- | --- |

To convert the calibrated, binary values to engineering units, refer to the
 *Converting <module> Data (FPGA Interface)* topic for each hardware
 module.

Parent topic:

Analog Input Modules

[<sup>1</sup>](#note_ref-d33164e94) After converting binary values to engineering
 units for the NI-9217, you can convert the nominal
 resistance values to temperature.

<!--NI_TOPIC bundle=ni-compactrio path=converting-ao-for-sbrio-9628-29-38.html language=enus -->
## TOPIC 00109: Converting Analog Output Values for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ao-for-sbrio-9628-29-38.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ao-for-sbrio-9628-29-38.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure the FPGA I/O Node to accept calibrated, fixed-point data in units of volts for the onboard analog output module, set the Calibration Mode to Calibrated in the Module Properties dialog box for the module. When Calibration Mode is set to Raw, the FPGA I/O Node accepts only binary values.

### Converting Analog Output Values for the sbRIO-9628/9629/9638 (FPGA Interface)

To configure the FPGA I/O Node to accept calibrated, fixed-point data in units of volts
 for the onboard analog output module, set the Calibration Mode to
 Calibrated in the Module Properties dialog box
 for the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node accepts only binary values. Convert output voltage values to binary values
 using the calibration constants before writing them to the FPGA I/O node. The conversion
 of voltage values to binary values can be done in the host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation in the host VI to convert the analog output
 values to binary values:

Binary Value =
 (Voltage Value - Offset) ÷
 LSB Weight

where

- Binary Value is the value you write to the FPGA I/O Node.
- Voltage Value is the voltage in V that you want the channel
 to output.
- Offset is the value returned by the Offset property.
- LSB Weight is the value returned by the LSB Weight property.

LSB Weight

Offset

LSB Weight

Offset

Offset

LSB
 Weight

- Offset = 0 V
- LSB Weight = 320 µV/LSB

Parent topic:

sbRIO-9628

<!--NI_TOPIC bundle=ni-compactrio path=converting-ao-for-sbrio-9628-29-38_2.html language=enus -->
## TOPIC 00110: Converting Analog Output Values for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ao-for-sbrio-9628-29-38_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ao-for-sbrio-9628-29-38_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure the FPGA I/O Node to accept calibrated, fixed-point data in units of volts for the onboard analog output module, set the Calibration Mode to Calibrated in the Module Properties dialog box for the module. When Calibration Mode is set to Raw, the FPGA I/O Node accepts only binary values.

### Converting Analog Output Values for the sbRIO-9628/9629/9638 (FPGA Interface)

To configure the FPGA I/O Node to accept calibrated, fixed-point data in units of volts
 for the onboard analog output module, set the Calibration Mode to
 Calibrated in the Module Properties dialog box
 for the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node accepts only binary values. Convert output voltage values to binary values
 using the calibration constants before writing them to the FPGA I/O node. The conversion
 of voltage values to binary values can be done in the host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation in the host VI to convert the analog output
 values to binary values:

Binary Value =
 (Voltage Value - Offset) ÷
 LSB Weight

where

- Binary Value is the value you write to the FPGA I/O Node.
- Voltage Value is the voltage in V that you want the channel
 to output.
- Offset is the value returned by the Offset property.
- LSB Weight is the value returned by the LSB Weight property.

LSB Weight

Offset

LSB Weight

Offset

Offset

LSB
 Weight

- Offset = 0 V
- LSB Weight = 320 µV/LSB

Parent topic:

sbRIO-9638

<!--NI_TOPIC bundle=ni-compactrio path=converting-current-values-to-binary-values-fo-2.html language=enus -->
## TOPIC 00111: Converting Current Values to Binary Values for the NI 9265 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-current-values-to-binary-values-fo-2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-current-values-to-binary-values-fo-2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9265 if you want the FPGA I/O Node to accept fixed-point data in units of amps when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only binary values when writing

### Converting Current Values to Binary Values for the NI 9265 (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9265 if you
 want the FPGA I/O Node to accept fixed-point data in units of amps when writing to the
 module.

If you set the Calibration Mode to Raw, the FPGA
 I/O Node accepts only binary values when writing to the module. Convert output voltage
 values to binary values before you write them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

You can use the following
 equation in the host VI to convert the analog output values to binary values:

Binary Value = (Current
 Value × 10<sup>12</sup> – Offset) ÷
 LSB Weight

- Binary Value is the value you write to the FPGA I/O
 Node.
- Current Value is the current in mA that you want the
 channel to output.
- Offset is the value returned by the Offset property.
- LSB Weight is the value returned by the LSB Weight
 property.

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties.

If you do not want to read the LSB Weight and Offset
 values from the module, convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = 20.6 mA ÷
 2<sup>DAC Resolution</sup> × 10<sup>12</sup>

- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9265 (FPGA Interface)

Related concepts:

- NI 9265 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-current-values-to-binary-values-fo.html language=enus -->
## TOPIC 00112: Converting Current Values to Binary Values for the NI 9266 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-current-values-to-binary-values-fo.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-current-values-to-binary-values-fo.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9266 if you want the FPGA I/O Node to accept fixed-point data in units of amps when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only binary values when writing

### Converting Current Values to Binary Values for the NI 9266 (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9266 if you
 want the FPGA I/O Node to accept fixed-point data in units of amps when writing to the
 module.

If you set the Calibration Mode to Raw, the FPGA
 I/O Node accepts only binary values when writing to the module. Convert output voltage
 values to binary values before you write them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following
 equation in the host VI to convert the analog output values to binary values:

Binary Value = (Current
 Value × 10<sup>12</sup> – Offset) ÷
 LSB Weight

- Binary Value is the value you write to the FPGA I/O
 Node.
- Current Value is the current in mA that you want the
 channel to output.
- Offset is the value returned by the Offset property.
- LSB Weight is the value returned by the LSB Weight
 property.

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties.

If you do not want to read the LSB Weight and Offset
 values from the module, convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = 20.89 mA ÷
 2<sup>DAC Resolution</sup> × 10<sup>12</sup>

- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9266 (FPGA Interface)

Related concepts:

- NI 9266 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-frames-to-and-from-channels-signal.html language=enus -->
## TOPIC 00113: Converting Frames To and From Channels (Signals)

- bundle_id: `ni-compactrio`
- source_path: `converting-frames-to-and-from-channels-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-frames-to-and-from-channels-signal.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CAN Input and CAN Output nodes in LabVIEW FPGA access CAN data as frames. Frames are the raw unit of transfer on the CAN bus. For some applications, it is useful to access CAN data as channels, also known as signals. A CAN channel represents a field in the data of a frame with specific CAN ident

### Converting Frames To and From Channels (Signals)

The CAN Input and CAN Output nodes in LabVIEW FPGA access CAN data as frames. Frames are the raw
 unit of transfer on the CAN bus.

channels

signals

- A CAN channel represents a field in the data of a frame with specific CAN
 identifier.

Vector
 CANdb

NI-CAN is the software for National Instruments PCI, PXI, and PCMCIA cards for CAN. The NI-CAN
 software provides features to enable conversion of CAN frames to/from channels. This
 frame to channel conversion can be used with the CompactRIO CAN module, even if you do
 not use an NI CAN PCI, PXI, or PCMCIA card.

- Any PXI controller
- cRIO-9002 CompactRIO Real-Time Controller
- cRIO-9004 CompactRIO Real-Time Controller

Remote Systems

Some examples of CompactRIO applications that use NI-CAN frame to channel conversion:

- Logging : The rugged enclosure and real-time capabilities of CompactRIO make it an ideal product for data logging in the field, such as drive testing of an automobile. For logging applications, the LabVIEW application on CompactRIO is simple: read CAN frames and store them in a file. When the CAN log file is later transferred from CompactRIO to a lab computer (usually running Windows), the application on the lab computer can read frames from the log file, and use NI-CAN to display the frames as CAN channel waveforms. In addition, if the LabVIEW application on CompactRIO stores a second log file with analog/digital samples, that data can be displayed on the lab computer as waveforms synchronized with the CAN channels.
- Triggering/Filtering : In a logging or other test application, you may need to evaluate CAN data to trigger some other task. For example, you may want to log a 5 second window of CAN/analog data when the "rpm" channel in CAN ID 5 first exceeds 4000 RPM. Although you could evaluate the raw data in CAN ID 5 to trigger the log, in some cases it is easier to simply evaluate the channel named "rpm" as defined in a CAN database. By installing NI-CAN on a CompactRIO Real-Time Controller such as the cRIO-9004, you can transfer CAN frames to NI-CAN, then read the "rpm" channel to detect when the value is greater than 4000.00.
- Prototyping/Simulation : For applications in which you must execute a control model within the CompactRIO Real-Time Controller, you typically wire CAN channels as inputs and outputs to the control model. In order to implement this, you can install NI-CAN on the CompactRIO Real-Time Controller. Your LabVIEW FPGA VI reads and writes CAN frames, and transfers those CAN frames to/from LabVIEW RT as you would any other I/O. Your LabVIEW RT VI uses NI-CAN to convert the CAN frames to/from CAN channels, which are then wired into the control model.

Parent topic:

Controller Area Network (CAN) Interface Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9202-data-fpga-interface.html language=enus -->
## TOPIC 00114: Converting NI 9202 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9202-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9202-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9202 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. Set the Calibration Mode to Raw if you want the FPGA I/O Node to return calibrated, binary data from the module. I

### Converting NI 9202 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 C Series Module Properties dialog box for the NI 9202 if you
 want the FPGA I/O Node to return calibrated, fixed-point data from the module.

Set the Calibration Mode to Raw if you want the
 FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, convert the
 binary values to engineering units. Convert these values in the host VI. For an example,
 refer to labview\examples\CompactRIO\Module Specific\NI 9202\NI 9202 Scaling\NI
 9202 Raw To Scaled.lvproj.

The binary values are not uniform across data rates. To get the Corrected
 Raw, multiply the binary value with the Gain
 Correction with respect to the data rate used. For an example, refer to
 labview\examples\CompactRIO\Module Specific\NI 9202\NI 9202 Raw
 Correction\NI 9202 Raw Correction.lvproj.

| Data Rates[1] | Scaling | Gain Correction |
| --- | --- | --- |
| 10 kS/s, 5 kS/s | Volts = Binary Value × 2018176 pV/LSB | Corrected Binary Value = Binary Value × 1.6 |
| 60 S/s[2] | Volts = Binary Value × 1356704 pV/LSB | Corrected Binary Value = Binary Value × 1.07563 |
| 400 S/s, 200 S/s, 100 S/s, 10 S/s[2] | Volts = Binary Value × 1291512 pV/LSB | Corrected Binary Value = Binary Value × 1.024 |
| 2 kS/s, 1 kS/s, 500 S/s, 250 S/s, 125 S/s, 50 S/s[2] | Volts = Binary Value × 1614448 pV/LSB | Corrected Binary Value = Binary Value × 1.28 |
| 60 S/s[3] | Volts = Binary Value × 2274057 pV/LSB | Corrected Binary Value = Binary Value × 1.802817 |
| 10 S/s[3], 50 S/s[3], Others | Volts = Binary Value × 1261244 pV/LSB | Corrected Binary Value = Binary Value × 1 |

where

- Binary Value is the value returned by the FPGA I/O Node.

<sup>1</sup> The actual data rate changes with the master timebase when using an external master timebase. In order to provide power line frequency rejection when using master timebase frequencies of both 12.8 MHz and 13.1072 MHz, there are two sets of settings for the data rates of 10 S/s, 50 S/s and 60 S/s. Refer to the following footnotes for the correct scaling constants and gain corrections, depending on your master timebase frequency.

<sup>2</sup> Data rates setting when using internal master timebase or an external master timebase of 12.8 MHz.

<sup>3</sup> Data rates setting when using an external master timebase of 13.1072 MHz.

Parent topic:

NI 9202 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9208-data-fpga-interface.html language=enus -->
## TOPIC 00115: Converting NI 9208 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9208-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9208-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9208 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of amps. Set the Calibration Mode to Raw if you want the FPGA I/O Node to return calibrated, binary data f

### Converting NI 9208 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9208* if
 you want the FPGA I/O Node to return calibrated, fixed-point data from the module in
 units of amps. Set the Calibration Mode to
 Raw if you want the FPGA I/O Node to return calibrated,
 binary data from the module. If you set the Calibration Mode to
 Raw, you must convert the binary current values to amps. You
 must convert these values in the host VI.

Use the following equation in the host VI to convert binary current values to amperes:

Amps = Binary Value × 0.022 A ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O Node.

Parent topic:

NI 9208 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9211-data-fpga-interface.html language=enus -->
## TOPIC 00116: Converting NI 9211 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9211-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9211-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9211 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. If you set the Calibration Mode to Calibrated, you must convert the fixed-point CJC data to bina

### Converting NI 9211 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9211* if
 you want the FPGA I/O Node to return calibrated, fixed-point data from the module in
 units of volts. If you set the Calibration Mode to
 Calibrated, you must convert the fixed-point CJC data to
 binary CJC data and then convert the binary CJC data to temperature.

Calibration Mode

Raw

Calibration Mode

Raw

Note

#### Using a VI to Convert Data to Temperature

Refer to the Convert to Temperature (NI 9211) polymorphic VI in the
 labview\examples\CompactRIO\Module Specific\NI 9211\NI 9211 Support
 Files.llb for an example of converting calibrated or raw data to
 temperature. You can use the Convert to Temperature (NI 9211) VI
 as a subVI in the host VI.

Use the following equation in the host VI to
 convert binary thermocouple values to voltage:

Voltage = Binary Value
 × 80 mV ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

#### Using an Equation to Convert Fixed-Point CJC Data
 to Binary CJC Data

Use the following equation in the host VI to convert
 fixed-point CJC data to binary CJC data:

Binary CJC Data =
 (Fixed-Point CJC Data) ÷ (0.160 ÷ (2<sup>24</sup> – 1))

- Fixed-Point CJC Data is the value returned by the FPGA
 I/O Node.

#### Using Equations to Convert Binary CJC Data to
 Temperature

Use the following equations in the host VI to convert binary
 CJC data to temperature:

Calculate the resistance of the thermistor:

R<sub>T</sub> = (10000 × Binary CJC Data)
 ÷ (2<sup>23</sup> – Binary CJC Data)

Calculate the CJC temperature:

T = [ 1 ÷
 [A + B(ln(R<sub>T</sub>)) +
 C(ln(R<sub>T</sub>))<sup>3</sup>]] – (273.15 +
 OffsetConstant)

- T = temperature in °C
- A = 1.2873851 × 10 -3
- B = 2.3575235 × 10 -4
- C = 9.4978060 × 10 -8
- R T = thermistor resistance reading
- OffsetConstant [[1]](#note-d16162e209) [<sup>1</sup>](#fnsrc_1-d16162e209) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction. = 0.7

Refer to the National Institute of Standards and Technology (NIST)
 Monograph 175 thermocouple reference tables for more information about converting
 and adjusting thermocouple values.

Parent topic:

NI 9211 (FPGA Interface)

[<sup>1</sup>](#note_ref-d16162e209) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction.

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9212-data-fpga-interface.html language=enus -->
## TOPIC 00117: Converting NI 9212 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9212-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9212-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9212 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. If you set the Calibration Mode to Calibrated, you must convert the CJC data from voltage to tem

### Converting NI 9212 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9212* if
 you want the FPGA I/O Node to return calibrated, fixed-point data from the module in
 units of volts. If you set the Calibration Mode to
 Calibrated, you must convert the CJC data from voltage to
 temperature.

Set the Calibration Mode to Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, you must
 convert the binary thermocouple and CJC values to voltage and then convert the CJC data
 from voltage to temperature. You must convert these values in the host VI.

#### Using a VI to Convert Data to Temperature

Refer to the NI 9212 Convert to Temperature
 polymorphic VI in the labview\examples\CompactRIO\Module Specific\NI 9212\NI
 9212 Getting Started\NI 9212 Getting Started.lvproj for an example of
 converting calibrated or raw data to temperature. Use the NI 9212 Convert
 to Temperature VI as a subVI in the host VI.

Use the following
 equation in the host VI to convert the binary thermocouple and CJC values to
 voltage:

Voltage = Binary Value
 × 78.125 mV ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

#### Converting CJC Data from Voltage to
 Temperature

The NI 9212Convert Thermistor ReadingVI is
 a subVI in the NI 9212 Convert to Temperature polymorphic VI that
 converts CJC data from voltage to temperature.

The VI uses the following
 equation to calculate the resistance of the thermistor:

R<sub>T</sub>
 = [(CJC Data ÷ 0.078125) ÷ (1 – (CJC Data
 ÷ 0.078125))] × 28,000

Using the resistance of the thermistor,
 the VI references a look-up table to interpolate the CJC temperature.

Refer
 to the National Institute of Standards and Technology (NIST) Monograph 175
 thermocouple reference tables for more information about converting and adjusting
 thermocouple values.

Parent topic:

NI 9212 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9213-data-fpga-interface.html language=enus -->
## TOPIC 00118: Converting NI 9213 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9213-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9213-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9213 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. If you set the Calibration Mode to Calibrated, you must convert the CJC data from voltage to tem

### Converting NI 9213 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9213 if you want the FPGA I/O Node to
 return calibrated, fixed-point data from the module in units of volts. If you set the
 Calibration Mode to Calibrated, you
 must convert the CJC data from voltage to temperature.

Calibration Mode

Raw

Calibration Mode

Raw

Note

#### Using a VI to Convert Data to Temperature

Refer to the NI 9213 Convert to Temperature polymorphic VI in the
 labview\examples\CompactRIO\Module Specific\NI 9213\NI 9213 Getting
 Started\NI 9213 Getting Started.lvproj for an example of converting
 calibrated or raw data to temperature. Use the NI 9213 Convert to
 Temperature VI as a subVI in the host VI.

#### Using an Equation to Convert Binary Values to
 Voltage

Use the following equation in the host VI to convert the binary
 thermocouple and CJC values to voltage:

Voltage =
 Binary Value × 78.125 mV ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

#### Using Equations to Convert CJC Data from Voltage to
 Temperature

Use the following equations in the host VI to convert CJC data
 from volts to temperature:

Calculate the resistance of the thermistor:

R<sub>T</sub> = (10000 × CJC Data × 32) ÷
 (2.5 – CJC Data × 32)

Calculate the CJC
 temperature:

T = [ 1 ÷ [A +
 B(ln(R<sub>T</sub>)) +
 C(ln(R<sub>T</sub>))<sup>3</sup>]] – (273.15 +
 OffsetConstant)

- T = temperature in °C
- A = 1.2873851 × 10 -3
- B = 2.3575235 × 10 -4
- C = 9.4978060 × 10 -8
- R T = thermistor resistance reading
- OffsetConstant [[1]](#note-d17430e177) [<sup>1</sup>](#fnsrc_1-d17430e177) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction. = 1

Refer to the National Institute of Standards and Technology (NIST)
 Monograph 175 thermocouple reference tables for more information about converting
 and adjusting thermocouple values.

Parent topic:

NI 9213 (FPGA Interface)

[<sup>1</sup>](#note_ref-d17430e177) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction.

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9214-data-fpga-interface.html language=enus -->
## TOPIC 00119: Converting NI 9214 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9214-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9214-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9214 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. If you set the Calibration Mode to Calibrated, you must convert the CJC data from voltage to tem

### Converting NI 9214 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9214* if
 you want the FPGA I/O Node to return calibrated, fixed-point data from the module in
 units of volts. If you set the Calibration Mode to
 Calibrated, you must convert the CJC data from voltage to
 temperature.

Set the Calibration Mode to Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, you must
 convert the binary thermocouple and CJC values to voltage and then convert the CJC data
 from voltage to temperature. You must convert these values in the host VI.

#### Using a VI to Convert Data to Temperature

Refer to the NI 9214 Convert to Temperature
 polymorphic VI in the labview\examples\CompactRIO\Module Specific\NI 9214\NI
 9214 Getting Started\NI 9214 Getting Started.lvproj for an example of
 converting calibrated or raw data to temperature. Use the NI 9214 Convert
 to Temperature VI as a subVI in the host VI.

Use the following
 equation in the host VI to convert the binary thermocouple and CJC values to
 voltage:

Voltage = Binary Value
 × 78.125 mV ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

#### Converting CJC Data from Voltage to Temperature

The NI 9214 Convert Thermistor Reading VI is a subVI
 in the NI 9214 Convert to Temperature polymorphic VI that
 converts CJC data from voltage to temperature.

The VI uses the following
 equation to calculate the resistance of the thermistor:

R<sub>T</sub>
 = [(CJC Data ÷ 0.078125) ÷ (1 – (CJC Data
 ÷ 0.078125))] × 20,000

Using the resistance of the thermistor,
 the VI references a look-up table to interpolate the CJC temperature.

Refer
 to the National Institute of Standards and Technology (NIST) Monograph 175
 thermocouple reference tables for more information about converting and adjusting
 thermocouple values.

Parent topic:

NI 9214 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9219-data-fpga-interface.html language=enus -->
## TOPIC 00120: Converting NI 9219 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9219-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9219-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9219 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. If you set the Calibration Mode to Calibrated and an NI 9219 channel is in Thermocouple mode, do the following: Co

### Converting NI 9219 Data (FPGA Interface)

Calibration Mode

Calibrated

Calibration
 Mode

Calibrated

Thermocouple

- Convert the fixed-point CJC data to binary CJC data.
- Convert the binary CJC data to temperature.

Calibration Mode

Raw

range

Calibration
 Mode

Raw

Calibration Mode

Raw

Thermocouple

Note

#### Using a VI to Convert and Adjust Binary Values

Refer to the NI 9219 Binary to Nominal VI in the
 labview\examples\CompactRIO\Module Specific\NI 9219\NI 9219 Scaling
 Utility directory for an example of converting and adjusting binary
 input values. Use the polymorphic NI 9219 Binary to Nominal VI as
 a subVI in the host VI to convert and adjust binary input values.

#### Using an Equation to Convert Binary Values

Use the following equation in
 the host VI to convert the binary input values to engineering units for each
 channel:

Engineering Units<sup>[[1]](#note-d8749e103)</sup>[<sup>1</sup>](#fnsrc_1-d8749e103) Engineering
 units are equivalent to the units of the mode input range listed in the NI 9219
 hardware documentation on ni.com/manuals.= Binary
 Value × (Range High – Range
 Low) ÷ 2<sup>24</sup>

- Binary Value is the value returned by the FPGA I/O
 Node.
- Range High is the upper value of the input range
 [[2]](#note-d8749e132) [<sup>2</sup>](#fnsrc_2-d8749e132) Refer to the NI 9219 hardware documentation on ni.com/manuals for
 the input ranges for each mode. For modes that have only one input range
 value, use 0 as the lower value of the input range.
- Range Low is the lower value of the input range.

Digital In Mode

- FALSE is equivalent to any voltage below the specified
 threshold.
- TRUE is equivalent to any voltage above the specified
 threshold.

Open Contact Mode

- FALSE indicates a closed circuit.
- TRUE indicates a open circuit.

#### Using an Equation to Convert Fixed-Point CJC Data

You can use the
 following equation in the host VI to convert fixed-point CJC data to binary CJC
 data:

Binary CJC Data = (Fixed-Point CJC
 Data) ÷ (0.250 ÷ (2<sup>24</sup> – 1))

#### Using Equations to Convert Binary CJC Data

Use the following equations in the host VI to convert binary CJC data to temperature:

Calculate the resistance of the thermistor:

R<sub>T</sub> =
 10000 ÷ [(2<sup>16</sup> ÷ Binary CJC Data) –
 1]

Calculate the CJC temperature:

T = [ 1 ÷ [A +
 B(ln(R<sub>T</sub>)) +
 C(ln(R<sub>T</sub>))<sup>3</sup>]] – (273.15 +
 OffsetConstant)

- T = temperature in °C
- A = 1.2873851 × 10 -3
- B = 2.3575235 × 10 -4
- C = 9.4978060 × 10 -8
- R T = thermistor resistance reading
- OffsetConstant [[3]](#note-d8749e279) [<sup>3</sup>](#fnsrc_3-d8749e279) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction. = 0.1.5

Refer to the National Institute of Standards and Technology (NIST)
 Monograph 175 thermocouple reference tables for more information about converting
 and adjusting thermocouple values.

Parent topic:

NI 9219 (FPGA Interface)

[<sup>1</sup>](#note_ref-d8749e103) Engineering
 units are equivalent to the units of the mode input range listed in the NI 9219
 hardware documentation on ni.com/manuals.

[<sup>2</sup>](#note_ref-d8749e132) Refer to the NI 9219 hardware documentation on ni.com/manuals for
 the input ranges for each mode. For modes that have only one input range
 value, use 0 as the lower value of the input range.

[<sup>3</sup>](#note_ref-d8749e279) The OffsetConstant
 is the typical temperature gradient between the CJC sensor and the
 thermocouple cold junction.

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9224-data-fpga-interface.html language=enus -->
## TOPIC 00121: Converting NI 9224 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9224-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9224-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9224 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. Set the Calibration Mode to Raw if you want the FPGA I/O Node to return calibrated, binary data

### Converting NI 9224 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9224 if you want the FPGA I/O Node to
 return calibrated, fixed-point data from the module in units of volts.

Set the Calibration Mode to Raw if you want the
 FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, convert the
 binary values to engineering units. Convert these values in the host VI.

#### Using an Equation to Convert Binary Values to Voltage

Use the following
 equation in the host VI to convert binary voltage values to volts:

Voltage = Binary Value
 × 1257533 pV/LSB

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9224 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9228-data-fpga-interface.html language=enus -->
## TOPIC 00122: Converting NI 9228 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9228-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9228-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9228 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the

### Converting NI 9228 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9228 if you want the FPGA I/O Node
 to return calibrated, fixed-point data from the module in units of volts.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns calibrated, binary data from the module. Convert the binary values
 to engineering units. Convert these values in the host VI.

#### Using an Equation to Convert Binary Values to
 Voltage

Use the following equation in the host VI to convert binary
 voltage values to volts:

Voltage = Binary
 Value × 7602677 pV/LSB

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9228 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9231-data-fpga-interface.html language=enus -->
## TOPIC 00123: Converting NI 9231 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9231-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9231-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9231 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. Set the Calibration Mode to Raw if you want the FPGA I/O Node to return calibrated, binary data from the module. I

### Converting NI 9231 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9231 if you want the FPGA I/O Node to
 return calibrated, fixed-point data from the module.

Set the Calibration Mode to Raw if you want the
 FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, convert the binary
 values to engineering units. Convert these values in the host VI.

You can use the following equations in the host VI to convert binary voltage values to volts:

Volts = Binary Value × 610714.8 pV/LSB

- Binary Value is the value returned by the FPGA I/O Node.

Parent topic:

NI 9231 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9242-and-ni-9244-data-fpga-inte.html language=enus -->
## TOPIC 00124: Converting NI 9242 and NI 9244 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9242-and-ni-9244-data-fpga-inte.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9242-and-ni-9244-data-fpga-inte.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9242 and NI 9242 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the module

### Converting NI 9242 and NI 9244 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9242 and NI 9242 if you want the
 FPGA I/O Node to return calibrated, fixed-point data from the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns calibrated, binary data from the module. Convert the binary values
 to engineering units. You must convert these values in the host VI.

#### Using an Equation to Convert Binary Values to Voltage

You can use the
 following equations in the host VI to convert binary voltage values to volts: NI
 9242

Use the following equation in the host VI to convert binary voltage
 values to volts:

NI 9242: Volts = Binary
 Value × 500 V ÷ 8,388,607

NI 9244:
 Volts = Binary Value × 997.5 V
 ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9242 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9242-and-ni-9244-data-fpga-inte_2.html language=enus -->
## TOPIC 00125: Converting NI 9242 and NI 9244 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9242-and-ni-9244-data-fpga-inte_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9242-and-ni-9244-data-fpga-inte_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9242 and NI 9242 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the module

### Converting NI 9242 and NI 9244 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9242 and NI 9242 if you want the
 FPGA I/O Node to return calibrated, fixed-point data from the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns calibrated, binary data from the module. Convert the binary values
 to engineering units. You must convert these values in the host VI.

#### Using an Equation to Convert Binary Values to Voltage

You can use the
 following equations in the host VI to convert binary voltage values to volts: NI
 9242

Use the following equation in the host VI to convert binary voltage
 values to volts:

NI 9242: Volts = Binary
 Value × 500 V ÷ 8,388,607

NI 9244:
 Volts = Binary Value × 997.5 V
 ÷ 8,388,607

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9244 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9251-data-fpga-interface.html language=enus -->
## TOPIC 00126: Converting NI 9251 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9251-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9251-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9251 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the module. Convert th

### Converting NI 9251 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9251 if you want the FPGA I/O Node
 to return calibrated, fixed-point data from the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns calibrated, binary data from the module. Convert the binary values
 to engineering units. You must convert these values in the host VI.

#### Using an Equation to Convert Binary Voltage Values
 to Volts

Use the following equation in the host VI to convert binary
 voltage values to volts:

Volts = Binary
 Value × 515589 pV/LSB

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9251 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9252-data-fpga-interface.html language=enus -->
## TOPIC 00127: Converting NI 9252 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9252-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9252-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9252 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the module. Convert th

### Converting NI 9252 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9252 if you want the FPGA I/O Node
 to return calibrated, fixed-point data from the module.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns calibrated, binary data from the module. Convert the binary values
 to engineering units. You must convert these values in the host VI.

#### Using an Equation to Convert Binary Voltage Values
 to Volts

Use the following equation in the host VI to convert binary
 voltage values to volts:

Volts = Binary
 Value × 1261243 pV/LSB

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9252 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9253-data-fpga-interface.html language=enus -->
## TOPIC 00128: Converting NI 9253 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9253-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9253-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9253 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module. When Calibration Mode is set to Raw, the FPGA I/O Node returns calibrated, binary data from the module. Convert th

### Converting NI 9253 Data (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9253 if you want the FPGA I/O Node
 to return calibrated, fixed-point data from the module.

When Calibration Mode is set to Raw, the FPGA I/O
 Node returns calibrated, binary data from the module. Convert the binary values to
 engineering units. Convert these values in the host VI.

#### Using an Equation to Convert Binary Current Values to Amperes

Use the
 following equation in the host VI to convert binary current values to amperes:

Current = Binary Value
 × 2615.02 pA/LSB

- Binary Value is the value returned by the FPGA I/O
 Node.

Parent topic:

NI 9253 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-ni-9320-data-fpga-interface.html language=enus -->
## TOPIC 00129: Converting NI 9320 Data (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-ni-9320-data-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-ni-9320-data-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9320 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of volts. Set the Calibration Mode to Raw if you want the FPGA I/O Node to return calibrated, binary data

### Converting NI 9320 Data (FPGA
 Interface)

Set the Calibration Mode to Calibrated in the
 C Series Module Properties dialog box for the
 *NI 9320* if you want the FPGA I/O Node to return calibrated, fixed-point
 data from the module in units of volts.

Set the Calibration Mode to Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you set the
 Calibration Mode to Raw, you must
 convert the binary values to engineering units in the host VI. Use the following
 equations to convert binary voltage values to volts in the host VI.

V

o

l

t

s

=

B

i

n

a

r

y

V

a

l

u

e

×

320

,

435

n

V

L

S

B

where Binary Value is the value returned by the FPGA I/O Node.

Parent topic:

NI 9320 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-nominal-values-to-temperature-valu-1.html language=enus -->
## TOPIC 00130: Converting Nominal Values to Temperature Values for the NI 9226 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-nominal-values-to-temperature-valu-1.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-nominal-values-to-temperature-valu-1.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9226 if you want the FPGA I/O Node to return calibrated, fixed-point data from the module in units of ohms. When Calibration Mode is set to Raw, the FPGA I/O Node returns uncalibrated, binary values for th

### Converting Nominal Values to Temperature Values for the NI 9226 (FPGA Interface)

Set the Calibration Mode to Calibrated in
 the C Series Module Properties dialog box for the NI 9226 if you want the FPGA I/O Node
 to return calibrated, fixed-point data from the module in units of ohms.

When Calibration Mode is set to Raw, the
 FPGA I/O Node returns uncalibrated, binary values for the module. After converting these
 binary values to nominal values, convert the nominal resistance values into temperature
 values. Convert these values in the host VI.

#### Using a VI to Convert Values

For an
 example of converting nominal resistance values to temperature, refer to the
 RTD to Temp VI in the
 labview\examples\CompactRIO\Module Specific\NI 9226\NI 9226 Getting
 Started\NI 9226 Getting Started.lvproj. Use the RTD to Temp
 VI as a subVI in the host VI to convert nominal resistance values to
 temperature.

Use a linearization curve known as the Callendar-Van Dusen
 equation in the host VI to measure the temperature of RTDs.

Parent topic:

NI 9226 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-nominal-values-to-temperature-valu-2.html language=enus -->
## TOPIC 00131: Converting Nominal Values to Temperature Values for the NI 9216 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-nominal-values-to-temperature-valu-2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-nominal-values-to-temperature-valu-2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9216 if you want the FPGA I/O Node to return calibrated, fixed-point data for the module in units of ohms. If you set the Calibration Mode to Raw, the FPGA I/O Node returns uncalibrated, binary values for

### Converting Nominal Values to Temperature Values for the NI 9216 (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9216* if
 you want the FPGA I/O Node to return calibrated, fixed-point data for the module in
 units of ohms. If you set the Calibration Mode to
 Raw, the FPGA I/O Node returns uncalibrated, binary values
 for the module. After you convert these binary values to nominal values, you can convert
 the nominal resistance values into temperature values. Convert these values in the host
 VI.

#### Using a VI to Convert Values

Refer to the RTD to Temp VI in the
 labview\examples\CompactRIO\Module Specific\NI 9216\NI 9216 Getting
 Started\NI 9216 Getting Started.lvproj for an example of converting
 nominal resistance values to temperature. Use the RTD to Temp VI as
 a subVI in the host VI to convert nominal resistance values to temperature.

Use a linearization curve known as the Callendar-Van Dusen equation in the
 host VI to measure the temperature of RTDs.

Parent topic:

NI 9216 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-nominal-values-to-temperature-valu.html language=enus -->
## TOPIC 00132: Converting Nominal Values to Temperature Values for the NI 9217 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-nominal-values-to-temperature-valu.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-nominal-values-to-temperature-valu.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9217 if you want the FPGA I/O Node to return calibrated, fixed-point data for the module in units of ohms. If you set the Calibration Mode to Raw, the FPGA I/O Node returns uncalibrated, binary values for

### Converting Nominal Values to Temperature Values for the NI 9217 (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 *C Series Module Properties* dialog box for the *NI 9217* if
 you want the FPGA I/O Node to return calibrated, fixed-point data for the module in
 units of ohms. If you set the Calibration Mode to
 Raw, the FPGA I/O Node returns uncalibrated, binary values
 for the module. After you convert these binary values to nominal values, you can convert
 the nominal resistance values into temperature values. Convert these values in the host
 VI.

#### Using a VI to Convert Values

Refer to the
 RTD to Temp VI in the
 labview\examples\CompactRIO\Module Specific\NI 9217\NI 9217 Getting
 Started\NI 9217 Getting Started.lvproj for an example of converting
 nominal resistance values to temperature. Use the RTD to Temp VI
 as a subVI in the host VI to convert nominal resistance values to temperature.

Use a linearization curve known as the Callendar-Van Dusen equation in the
 host VI to measure the temperature of RTDs.

Parent topic:

NI 9217 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo-2_2.html language=enus -->
## TOPIC 00133: Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo-2_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo-2_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 C Series Module Properties dialog box for the
 NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data
 in units of volts when writing to the module.

If you set the Calibration Mode to Raw, the FPGA
 I/O Node accepts only binary values when writing to the module. Convert output voltage
 values to binary values before you write them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

You can use the following
 equation in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value × 10<sup>9</sup> – Offset) ÷ LSB
 Weight

- Binary Value is the value you write to the FPGA I/O
 Node
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the Offset property
- LSB Weight is the value returned by the LSB Weight
 property.

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties.

If you do not want to read the LSB Weight and Offset
 values from the module, convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = Typical
 Output Span ÷ 2<sup>DAC Resolution</sup> ×
 10<sup>9</sup>

- Typical Output Span is 21.4 V for the NI 9263, 21 V for
 the NI 9264, and 20.98 V for the NI 9269.
- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9263 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo-2_3.html language=enus -->
## TOPIC 00134: Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo-2_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo-2_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 C Series Module Properties dialog box for the
 NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data
 in units of volts when writing to the module.

If you set the Calibration Mode to Raw, the FPGA
 I/O Node accepts only binary values when writing to the module. Convert output voltage
 values to binary values before you write them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

You can use the following
 equation in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value × 10<sup>9</sup> – Offset) ÷ LSB
 Weight

- Binary Value is the value you write to the FPGA I/O
 Node
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the Offset property
- LSB Weight is the value returned by the LSB Weight
 property.

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties.

If you do not want to read the LSB Weight and Offset
 values from the module, convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = Typical
 Output Span ÷ 2<sup>DAC Resolution</sup> ×
 10<sup>9</sup>

- Typical Output Span is 21.4 V for the NI 9263, 21 V for
 the NI 9264, and 20.98 V for the NI 9269.
- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9264 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo-2_4.html language=enus -->
## TOPIC 00135: Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo-2_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo-2_4.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)

Set the Calibration Mode to Calibrated in the
 C Series Module Properties dialog box for the
 NI 9262/NI 9263/NI 9264/NI 9269 if you want the FPGA I/O Node to accept fixed-point data
 in units of volts when writing to the module.

If you set the Calibration Mode to Raw, the FPGA
 I/O Node accepts only binary values when writing to the module. Convert output voltage
 values to binary values before you write them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

You can use the following
 equation in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value × 10<sup>9</sup> – Offset) ÷ LSB
 Weight

- Binary Value is the value you write to the FPGA I/O
 Node
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the Offset property
- LSB Weight is the value returned by the LSB Weight
 property.

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties.

If you do not want to read the LSB Weight and Offset
 values from the module, convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = Typical
 Output Span ÷ 2<sup>DAC Resolution</sup> ×
 10<sup>9</sup>

- Typical Output Span is 21.4 V for the NI 9263, 21 V for
 the NI 9264, and 20.98 V for the NI 9269.
- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9269 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo-3.html language=enus -->
## TOPIC 00136: Converting Voltage Values to Binary Values for the NI 9260 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo-3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo-3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9260 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. If you set the Calibration Mode to Raw, the FPGA I/O Node accepts only binary values when writing

### Converting Voltage Values to Binary Values for the NI 9260 (FPGA Interface)

Calibration Mode

Calibrated

C
 Series Module Properties

Note

#### Using an Equation to Convert Voltage to Binary

You can use the following
 equation in the host VI to convert the analog output values to binary:

Binary Value = (Voltage
 Value - (Offset × 10<sup>-9</sup>)) ×
 (LSB Weight × 10<sup>-12</sup>)

- Binary Value is the value returned by the FPGA I/O
 Node.
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the
 Offset property
- LSB Weight is the value returned by the LSB
 Weight property

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties. If you do not want to read the LSB Weight and Offset values from
 the module, you can convert uncalibrated voltage values by using the following
 values for Offset and LSB Weight:

Offset = 0

LSB Weight = Typical
 Output Span ÷ 2<sup>DAC Resolution</sup> ×
 10<sup>12</sup>

- Typical Output Span is 8.71 V for the NI 9260
- DAC Resolution is the DAC resolution of the module. Refer
 to the module hardware documentation for this value.

Parent topic:

NI 9260 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo.html language=enus -->
## TOPIC 00137: Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9381 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. When Calibration Mode is set to Raw when writing to the module, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9381 if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the module.

When Calibration Mode is set to Raw when writing
 to the module, the FPGA I/O Node accepts only binary values. Convert output voltage
 values to binary values before writing them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation
 in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value – Offset) ÷ LSB Weight

- Binary Value is the value returned by the FPGA I/O
 Node.
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the
 Offset property
- LSB Weight is the value returned by the LSB
 Weight property

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties. If you do not want to read the LSB Weight and Offset values from
 the module, convert uncalibrated voltage values by using the following values for
 Offset and LSB Weight:

Offset = –5249

LSB Weight = 5.105 V ÷
 2<sup>DAC Resolution</sup>

- DAC Resolution is the DAC resolution value. Refer to the
 NI 9381 hardware documentation for the DAC resolution value.

Parent topic:

NI 9381 (FPGA Interface)

Related concepts:

- NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo_2.html language=enus -->
## TOPIC 00138: Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9381 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. When Calibration Mode is set to Raw when writing to the module, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9381 if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the module.

When Calibration Mode is set to Raw when writing
 to the module, the FPGA I/O Node accepts only binary values. Convert output voltage
 values to binary values before writing them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation
 in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value – Offset) ÷ LSB Weight

- Binary Value is the value returned by the FPGA I/O
 Node.
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the
 Offset property
- LSB Weight is the value returned by the LSB
 Weight property

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties. If you do not want to read the LSB Weight and Offset values from
 the module, convert uncalibrated voltage values by using the following values for
 Offset and LSB Weight:

Offset = –5249

LSB Weight = 5.105 V ÷
 2<sup>DAC Resolution</sup>

- DAC Resolution is the DAC resolution value. Refer to the
 NI 9381 hardware documentation for the DAC resolution value.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo_3.html language=enus -->
## TOPIC 00139: Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9381 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. When Calibration Mode is set to Raw when writing to the module, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9381 if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the module.

When Calibration Mode is set to Raw when writing
 to the module, the FPGA I/O Node accepts only binary values. Convert output voltage
 values to binary values before writing them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation
 in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value – Offset) ÷ LSB Weight

- Binary Value is the value returned by the FPGA I/O
 Node.
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the
 Offset property
- LSB Weight is the value returned by the LSB
 Weight property

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties. If you do not want to read the LSB Weight and Offset values from
 the module, convert uncalibrated voltage values by using the following values for
 Offset and LSB Weight:

Offset = –5249

LSB Weight = 5.105 V ÷
 2<sup>DAC Resolution</sup>

- DAC Resolution is the DAC resolution value. Refer to the
 NI 9381 hardware documentation for the DAC resolution value.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=converting-voltage-values-to-binary-values-fo_4.html language=enus -->
## TOPIC 00140: Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `converting-voltage-values-to-binary-values-fo_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/converting-voltage-values-to-binary-values-fo_4.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the Calibration Mode to Calibrated in the C Series Module Properties dialog box for the NI 9381 if you want the FPGA I/O Node to accept fixed-point data in units of volts when writing to the module. When Calibration Mode is set to Raw when writing to the module, the FPGA I/O Node accepts only bi

### Converting Voltage Values to Binary Values for the NI 9381 (FPGA Interface)

Set the Calibration Mode to Calibrated in the C
 Series Module Properties dialog box for the NI 9381 if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the module.

When Calibration Mode is set to Raw when writing
 to the module, the FPGA I/O Node accepts only binary values. Convert output voltage
 values to binary values before writing them to the module. Convert these values in the
 host VI.

#### Using an Equation to Convert Voltage to Binary

Use the following equation
 in the host VI to convert the analog output values to binary values:

Binary Value = (Voltage
 Value – Offset) ÷ LSB Weight

- Binary Value is the value returned by the FPGA I/O
 Node.
- Voltage Value is the voltage in V that
 you want the channel to output
- Offset is the value returned by the
 Offset property
- LSB Weight is the value returned by the LSB
 Weight property

NI recommends using calibrated values for analog output. To convert
 calibrated voltage values, use the FPGA I/O Property Node to read the LSB Weight and
 Offset properties. If you do not want to read the LSB Weight and Offset values from
 the module, convert uncalibrated voltage values by using the following values for
 Offset and LSB Weight:

Offset = –5249

LSB Weight = 5.105 V ÷
 2<sup>DAC Resolution</sup>

- DAC Resolution is the DAC resolution value. Refer to the
 NI 9381 hardware documentation for the DAC resolution value.

Parent topic:

NI 9381 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=counter-input-modules.html language=enus -->
## TOPIC 00141: Counter Input Modules

- bundle_id: `ni-compactrio`
- source_path: `counter-input-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/counter-input-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 338 C Series Counter Input Modules C Series Counter Input Module Description NI-9326 6-Channel, 150 V, 128 kHz C Series Frequency Input Module NI-9361 32-Bit, 8-Channel C Series Counter Input Module

### Counter Input Modules

| C Series Counter Input Module | Description |
| --- | --- |
| NI-9326 | 6-Channel, 150 V, 128 kHz C Series Frequency Input Module |
| NI-9361 | 32-Bit, 8-Channel C Series Counter Input Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=create-clip.html language=enus -->
## TOPIC 00142: Creating a New CLIP

- bundle_id: `ni-compactrio`
- source_path: `create-clip.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/create-clip.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Create CLIP page of the sbRIO CLIP Generator to create a new CLIP. On the Create CLIP page, configure the following options: CLIP Name The name of the CLIP as it appears in LabVIEW and the name of the VHDL entity. The sbRIO CLIP Generator creates a folder with this name in the Documents\LabV

### Creating a New CLIP

Use the Create CLIP page of the sbRIO CLIP
 Generator to create a new CLIP.

1. On the Create CLIP page, configure the following options: 
 **CLIP Name**—The name of the CLIP as it appears in LabVIEW and the name of the
 VHDL entity. The sbRIO CLIP Generator creates a folder with this
 name in the Documents\LabVIEW
 Data\CompactRIO\CLIPs\<target>
 directory. The folder contains generated files that also use this
 name, such as
 <clipname>.vhd,
 <clipname>.xml,
 and <clipname>.xdc.Note To
 distribute CLIP files after creating them, install the CLIP
 files to the <National
 Instruments>\Shared\CompactRIO\CLIPs\<target>
 directory. CLIP files installed to this directory are available
 for selection in the Component-Level IP
 Properties dialog box for the NI sbRIO target to
 a LabVIEW project.
 **Create New CLIP**—Specifies the options to use for configuring the state of the sbRIO
 CLIP Generator. The following options are available:Create a new CLIP with no existing configuration.
 Load the configuration for a previously saved CLIP to use as
 the basis for a new CLIP. Note To
 change an existing CLIP after it has been created,
 manually edit the generated CLIP files. You cannot use
 the sbRIO CLIP Generator to edit an existing CLIP.
 **Target Type**—The NI sbRIO device in your application.
 **CLIP Description**—The CLIP description appears on the General page of the
 Component-Level IP Properties dialog box in
 the LabVIEW project.
2. Click Next to continue to the
 Peripherals page. 
 Use the Peripherals page to add peripherals to the
 CLIP.

Parent topic:

Creating a Component-Level IP for an NI sbRIO Target

<!--NI_TOPIC bundle=ni-compactrio path=crio-controller-serial-ports.html language=enus -->
## TOPIC 00143: Serial Ports

- bundle_id: `ni-compactrio`
- source_path: `crio-controller-serial-ports.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/crio-controller-serial-ports.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The cRIO-903x and 904x feature RS-232 and RS-485 Ethernet ports. RS-232 Serial Port 9 RS-232 Serial Port Pinout Pin Signal 1 No Connect 2 RI 3 CTS 4 RTS 5 DSR 6 GND 7 DTR 8 TXD 9 RXD 10 DCD RS-485 Serial Port 10 RS-485 Serial Port Pinout Pin Signal Description 1 No Connect 2 TXD- 3 TXD+ 4 No Connect

### Serial Ports

Note

#### RS-232 Serial Port

Figure 9.

[IMAGE alt='image' src='GUID-6C8B5918-A321-4736-B80F-CE7B41A6A48E-a5.svg']

| Pin | Signal |
| --- | --- |
| 1 | No Connect |
| 2 | RI |
| 3 | CTS |
| 4 | RTS |
| 5 | DSR |
| 6 | GND |
| 7 | DTR |
| 8 | TXD |
| 9 | RXD |
| 10 | DCD |

#### RS-485 Serial Port

Figure 10.

[IMAGE alt='image' src='GUID-6C8B5918-A321-4736-B80F-CE7B41A6A48E-a5.svg']

| Pin | Signal Description |
| --- | --- |
| 1 | No Connect |
| 2 | TXD- |
| 3 | TXD+ |
| 4 | No Connect |
| 5 | No Connect |
| 6 | RXD- |
| 7 | RXD+ |
| 8 | No Connect |
| 9 | No Connect |
| 10 | Isolated GND |

Parent topic:

NI CompactRIO Controllers

<!--NI_TOPIC bundle=ni-compactrio path=crio-controllers-cseries.html language=enus -->
## TOPIC 00144: NI CompactRIO Controllers

- bundle_id: `ni-compactrio`
- source_path: `crio-controllers-cseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/crio-controllers-cseries.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### NI CompactRIO
 Controllers

- [CompactRIO DRAM Interface](compactrio-dram-interface.html#GUID-E281C121-F80B-4AB3-94D3-3F3AC626F503)
- [Serial Ports](crio-controller-serial-ports.html)
- [Configuring Controller Startup Settings in MAX](configuring-controller-startup-settings-in-max.html)
- [cRIO-903x Controllers](crio-903x-controllers.html#GUID-3AF3DC08-BFF2-47EC-944C-CAFC29C71580)
- [cRIO-904x Controllers](crio-904x-controllers.html#GUID-8B1DF2F1-6221-4951-9AD0-9275E98E6912)
- [cRIO-905x Controllers](crio-905x-controllers.html#GUID-4C21DF20-BFBA-4130-8750-0016E3E2E628)
- [cRIO-906x Controllers](crio-906x-controllers.html#GUID-510627C6-E3CA-4C06-A109-FA398DAAC66F)

Parent topic:

CompactRIO Controller and Chassis Reference

<!--NI_TOPIC bundle=ni-compactrio path=detecting-out-of-range-ch-crio-ai.html language=enus -->
## TOPIC 00145: Detecting Out-of-Range Channels for CompactRIO Analog Input Channels (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `detecting-out-of-range-ch-crio-ai.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/detecting-out-of-range-ch-crio-ai.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can detect an out-of-range CompactRIO analog input channel when you read the channel. If you set Calibration Mode to Calibrated in the C Series Module Properties dialog box, and the FPGA I/O Node returns a value greater than the minimum operating range value, the channel might be out of range. R

### Detecting Out-of-Range Channels for CompactRIO
 Analog Input Channels (FPGA Interface)

You can detect an out-of-range CompactRIO analog input channel when you *read* the
 channel.

Calibration Mode

Calibrated

C Series Module Properties

FPGA I/O Node

Note

Specifications

The FPGA I/O Node returns the full-scale binary value if a channel is out of range and
 Calibration Mode is set to Raw.

| Module | Full-Scale Binary Value |
| --- | --- |
| NI 9201 | –2,048 (0xF800) or 2,047 (0x7FF) |
| NI 9202* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9203 | 0 (0x0000) or 65,535 (0xFFFF) |
| NI 9204* | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9205* | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9206* | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9207 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9208 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9209 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9210 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9211 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9212 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9213 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9214 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9215 | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9217 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9218 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9219 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9220 | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9221 | –2,048 (0xF800) or 2,047 (0x7FF) |
| NI 9222 | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9223 | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9224* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9225 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9227 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9228* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9229 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9230 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9231* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9232 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9234 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9235 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9236 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9237 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9238 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9239 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9242* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9244* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9246 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9247 | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9250* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9251* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9252* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9253* | –8,388,608 (0xFF800000) or 8,388,607 (0x7FFFFF) |
| NI 9320 | –32,768 (0x8000) or 32,767 (0x7FFF) |
| NI 9381 | 0 (0x0000) or 4,095 (0x0FFF) |

<sup>*</sup>For the NI 9202/9204/9205/9206/9224/9228/9231/9242/9244/9250/9251/9252/9253,
 a channel might be out of range before the FPGA I/O Node reaches the minimum or maximum
 full-scale binary value.

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=digital-input-modules.html language=enus -->
## TOPIC 00146: Digital Input Modules

- bundle_id: `ni-compactrio`
- source_path: `digital-input-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/digital-input-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 373 C Series Digital Input Modules C Series Digital Input Module Description NI-9344 4-Channel C Series User Interface Module NI-9375 30 V, 32-Channel (Sinking Input, Sourcing Output), 7 µs (Input)/500 µs (Output) C Series Digital Module NI-9381 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunction

### Digital Input Modules

| C Series Digital Input Module | Description |
| --- | --- |
| NI-9344 | 4-Channel C Series User Interface Module |
| NI-9375 | 30 V, 32-Channel (Sinking Input, Sourcing Output), 7 µs (Input)/500 µs (Output) C Series Digital Module |
| NI-9381 | 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunction I/O Module |
| NI-9401 | 5 V/TTL, 8 Bidirectional Channels, 100 ns C Series Digital Module |
| NI-9402 | LVTTL, 4 Bidirectional Channels, 55 ns C Series Digital Module |
| NI-9403 | 5 V/TTL, 32 Bidirectional Channels, 7 µs C Series Digital Module |
| NI-9411 | ±5 V to 24 V, 6 Differential/Single-Ended Channels, 500 ns C Series Digital Module |
| NI-9421 | 24 V, 8-Channel (Sinking Input), 100 µs C Series Digital Module |
| NI-9422 | 24 V to 60 V, 8 Channel (Sinking/Sourcing Input), 250 µs C Series Digital Module |
| NI-9423 | 24 V, 8 Channel (Sinking Input), 1 µs C Series Digital Module |
| NI-9425 | 24 V, 32-Channel (Sinking Input), 7 µs C Series Digital Module |
| NI-9426 | 24 V, 32 Channel (Sourcing Input), 7 µs C Series Digital Module |
| NI-9435 | ±5 VDC to ±250 VDC/10 VAC to 250 VAC, 4-Channel (Sinking/Sourcing Input), 3 ms C Series Digital Module |
| NI-9436 | 120 VDC to 240 VDC/120 VAC to 240 VAC, 8 Channel (Sinking/Sourcing Input), 20 ms C Series Digital Module |
| NI-9437 | 24 VDC to 250 VDC, 8-Channel (Sinking Input), 1 µs C Series Digital Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=digital-output-modules.html language=enus -->
## TOPIC 00147: Digital Output Modules

- bundle_id: `ni-compactrio`
- source_path: `digital-output-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/digital-output-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 438 C Series Digital Output Modules C Series Digital Output Module Description NI-9344 4-Channel C Series User Interface Module NI-9375 30 V, 32-Channel (Sinking Input, Sourcing Output), 7 µs (Input)/500 µs (Output) C Series Digital Module NI-9381 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunctio

### Digital Output Modules

| C Series Digital Output Module | Description |
| --- | --- |
| NI-9344 | 4-Channel C Series User Interface Module |
| NI-9375 | 30 V, 32-Channel (Sinking Input, Sourcing Output), 7 µs (Input)/500 µs (Output) C Series Digital Module |
| NI-9381 | 8 AI, 8 AO, 4 DIO, 0 V to 5 V, C Series Multifunction I/O Module |
| NI-9401 | 5 V/TTL, 8 Bidirectional Channels, 100 ns C Series Digital Module |
| NI-9402 | LVTTL, 4 Bidirectional Channels, 55 ns C Series Digital Module |
| NI-9403 | 5 V/TTL, 32 Bidirectional Channels, 7 µs C Series Digital Module |
| NI-9470 | 5 VDC to 30 VDC, 8-Channel (Sourcing Output), 2 kHz C Series Digital Module |
| NI-9472 | 24 V, 8-Channel (Sourcing Output), 100 µs C Series Digital Module |
| NI-9474 | 30 V, 8-Channel (Sourcing Output), 1 µs C Series Digital Module |
| NI-9475 | 60 V, 8-Channel (Sourcing Output), 1 µs C Series Digital Module |
| NI-9476 | 36 V, 32-Channel (Sourcing Output), 500 µs C Series Digital Module |
| NI-9477 | 60 V, 32-Channel (Sinking Output), 8 µs C Series Digital Module |
| NI-9478 | 50 V, 16-Channel (Sinking Output), 50 µs C Series Digital Module |
| NI-9481 | 4-Channel, SPST Relay, 60 VDC(1 A)/ 250 Vrms (2 A) C Series Relay Output Module |
| NI-9482 | 4-Channel, SPST Relay, 60 VDC (1 A)/250 VAC (1.5 A) C Series Relay Output Module |
| NI-9485 | 8-Channel, SSR Relay, 60 VDC/30 Vrms, 750 mA C Series Relay Output Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=discovering-your-hardware.html language=enus -->
## TOPIC 00148: Discovering your Hardware

- bundle_id: `ni-compactrio`
- source_path: `discovering-your-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/discovering-your-hardware.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to discover your hardware in a project. Create a new project in LabVIEW or open an existing project. Right-click the project root in the Project Explorer window and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box. S

### Discovering your Hardware

Complete the following steps to discover your hardware in a project.

1. Create a new project in LabVIEW or open an existing project.
2. Right-click the project root in the Project Explorer
 window and select New»Targets and Devices from the
 shortcut menu to display the Add Targets and Devices
 dialog box.
3. Select the appropriate device from the Targets and Devices list. Note If you cannot find the appropriate
 device, you may not have configured it for your network using Measurement
 & Automation Explorer (MAX). Launch MAX and refer to the MAX help for
 CompactRIO.
4. Click the OK button.
5. If the Select Programming Mode dialog box appears,
 select LabVIEW FPGA Interface or Scan
 Interface as appropriate.
6. Click the Continue button.
7. If the Discover C Series Modules? dialog box appears, click the Discover button.
8. Right-click a module in the Project Explorer window and select Properties from the shortcut menu to configure module-specific settings.
9. Repeat steps 2 through 8 to add an expansion chassis or additional expansion chassis to the project.

Parent topic:

Configuring a Project with Connected Hardware

Related concepts:

- Programming Interfaces

#### Project Targets and Items

LabVIEW adds targets and items to your project for the hardware in your system.

The following table shows the target icons LabVIEW displays in the project.

| Target Icon | Device | Description |
| --- | --- | --- |
|  | CompactRIO controller | LabVIEW adds this controller target to a project for a CompactRIO controller. |
|  | Ethernet RIO chassis | LabVIEW adds this target to a project for a Ethernet RIO chassis. The Ethernet RIO chassis is not a real-time target, but it can add expansion I/O to a real-time target. |
|  | Single-Board RIO device | LabVIEW adds this controller target to a project for a Single-Board RIO device. |
|  | myRIO device | LabVIEW adds this controller target to a project for a myRIO-1900. |
|  | myRIO device | LabVIEW adds this controller target to a project for a myRIO-1950. |
|  | roboRIO device | LabVIEW adds this controller target to a project for a roboRIO. |
|  | NI ELVIS RIO Control Module (NI ELVIS RIO CM) device | LabVIEW adds this controller target to a project for an NI ELVIS RIO CM. |

The following table shows the item icons LabVIEW displays in the project.

| Item Icon | Device | Description |
| --- | --- | --- |
|  | CompactRIO chassis, Ethernet RIO chassis | LabVIEW adds this chassis target to a project for a CompactRIO chassis or Ethernet RIO chassis. |
|  | MXIe-RIO chassis | LabVIEW adds this chassis target to a project for a MXIe-RIO chassis. You can add a MXIe-RIO chassis to a real-time controller or the host PC. |
|  | Single-Board RIO, myRIO, roboRIO, or NI ELVIS RIO CM device | LabVIEW adds this chassis target to a project for a Single-Board RIO, myRIO, roboRIO, or NI ELVIS RIO CM device. |
|  | FPGA | LabVIEW adds this FPGA target to a project for the FPGA on a CompactRIO chassis, Ethernet RIO chassis, MXIe-RIO chassis, or Single-Board RIO device in the FGPA Interface. |
|  | C Series modules | LabVIEW adds this module target to a project for C Series modules. |
|  | Onboard C Series modules | LabVIEW adds this module target to a project for C Series modules onboard a Single-Board RIO device. |

<!--NI_TOPIC bundle=ni-compactrio path=does-the-serial-hardware-have-built-in-suppor.html language=enus -->
## TOPIC 00149: Does the serial hardware have built-in support for protocols such as SDLC and ModBus?

- bundle_id: `ni-compactrio`
- source_path: `does-the-serial-hardware-have-built-in-suppor.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/does-the-serial-hardware-have-built-in-suppor.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the serial hardware uses UARTs for communication, protocols such as SDLC and ModBus are not supported in hardware. However, these protocols (or their derivatives) can be supported by software applications that handle the protocol translation.

### Does the serial hardware have built-in support for protocols such as SDLC and ModBus?

Because the serial hardware uses UARTs for communication, protocols such as SDLC and ModBus are not supported in hardware. However, these protocols (or their derivatives) can be supported by software applications that handle the protocol translation.

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=downloading-firmware-to-an-ni-951x-module.html language=enus -->
## TOPIC 00150: Downloading Firmware to an NI 951x Module

- bundle_id: `ni-compactrio`
- source_path: `downloading-firmware-to-an-ni-951x-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/downloading-firmware-to-an-ni-951x-module.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the C Series Module Properties dialog box for the NI 9512, NI 9514, or NI 9516 to check the current firmware version on the NI 951x module and to download firmware to the module. Downloading the Firmware to the NI 951x Module Before downloading firmware to the NI 951x module ensure that

### Downloading Firmware to an NI 951x Module

You can use the *C Series Module Properties* dialog box for the NI 9512, NI 9514, or NI 9516 to check the current firmware version on the NI 951x module and to download firmware to the module.

Downloading the Firmware to the NI 951x Module

Note

Complete the following steps to download firmware to the module.

1. Right-click the NI 951x module in the Project Explorer window and select Properties from the shortcut menu to open the C Series Module Properties dialog box.
2. Click Check Version . The 951x Firmware Update Utility checks the firmware version on the module and displays the version number in Firmware Version on Module .
  - To upgrade firmware on the module, check that the version is greater than the version displayed in Available Firmware Version .
  - To downgrade firmware on the module, check that the version is less than the version displayed in Available Firmware Version .
3. Click Download . The firmware on the host is transferred to the module. This process may take several minutes.

Note

If the firmware update process is interrupted during transfer by removing the module or disconnecting power, click Download to restart the transfer. Firmware updates on NI 951x modules is supported only on legacy compactRIO controllers such as the cRIO-902x and cRIO-907x. It is not supported on Linux targets such as cRIO-906x and cRIO 903x.

Parent topic:

C Series Motor Drive Interface Modules

<!--NI_TOPIC bundle=ni-compactrio path=duplex-architectures.html language=enus -->
## TOPIC 00151: Duplex Architectures

- bundle_id: `ni-compactrio`
- source_path: `duplex-architectures.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/duplex-architectures.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Duplex refers to the means of bandwidth usage in a serial system. The two common means of bi-directional serial communication are full duplex and half duplex. Half-duplex communication involves a transmitter and a receiver connected to each end of the same wire or pair of wires. Because the same tra

### Duplex Architectures

*Duplex* refers to the means of bandwidth usage in a serial system.

The two common means of bi-directional serial communication are full duplex and half
 duplex.

Half-duplex communication involves a transmitter and a receiver connected to each end of
 the same wire or pair of wires. Because the same transmission line both sends and
 receives data, devices cannot send data in both directions at the same time. First, one
 device transmits over the wire(s) to the receiver of the second device. When the first
 device finishes transmitting, both devices switch the connections from their transmitter
 to their receiver, or vice versa. The device that was receiving data can then transmit
 over the line.

In full-duplex communication, the devices use a separate wire (or pair of wires) for simultaneous
 transmission in each direction. The devices do not switch between transmitting and
 receiving.

In a differential serial bus, such as RS422 or RS485, a half-duplex system transmits and receives
 over the same twisted pair of wires. Half-duplex communication is often referred to as
 two-wire communication. Likewise, full-duplex communication is
 often referred to as four-wire communication because the full-duplex
 system uses a separate pair of wires for communication in each direction.

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=error-terminals.html language=enus -->
## TOPIC 00152: Error Terminals

- bundle_id: `ni-compactrio`
- source_path: `error-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/error-terminals.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To detect errors, right-click the CAN node in the diagram and select Error Terminals. The resulting Error In and Error Out terminals provide the standard LabVIEW error cluster for error handling. NI recommends using Error Terminals for CAN development. For some CAN nodes, the error terminals are ess

### Error Terminals

To detect errors, right-click the CAN node in the diagram and select Error Terminals. The resulting Error In and Error Out terminals provide the standard LabVIEW error cluster for error handling.

NI recommends using Error Terminals for CAN development. For some CAN
 nodes, the error terminals are essential. For example, you need to evaluate
 Error Out from a CAN Input node to determine if a CAN frame
 was received within the specified Input Timeout (ms). The only
 cost of using error terminals is slight FPGA gate usage, not performance.

When an error occurs, use the LabVIEW Explain Error Help dialog box for a
 description of the error code. Right-click an error cluster and select
 Explain Error from the shortcut menu for more information
 about the error. You also can select Explain Error and enter the
 returned error code into the dialog box.

The error descriptions in the Explain Error dialog box are generic to all
 CompactRIO (C Series) modules. The following sections provide information specific to
 the CAN module.

#### Module Communication Error

Error Code: 65536

This error occurs when there is a
 catastrophic error with communication to the CAN module. Catastrophic errors can
 result when the following events occur:

- Unplug the CAN module.
- Invoke a CAN node while the CompactRIO Sleep line is asserted. This error does
 not occur for the Sleep feature of the CAN transceiver ( Transceiver
 Mode property).
- Invoke a CAN node before the CAN module has reconfigured itself after the
 CompactRIO Sleep line deasserts (approximately 1 second).
- An invalid data transfer between LabVIEW FPGA and the CAN module.

#### Incorrect Module Error

Error Code: 65537

This error occurs if the user plugs in
 another CompactRIO module into a slot configured for a CAN module.

#### Timeout Error

Error Code: 65538

This error occurs when:

- CAN Input does not receive a valid CAN frame within the specified
 Input Timeout (ms) .
- CAN Output does not detect an available element in the output FIFO within the
 specified Output Timeout (ms) .
- An I/O Method or
 I/O Property
 node does not detect an available element in the output FIFO within the
 specified Output Timeout (ms) . Refer to
 Arbitration for more information.

This error is not returned when a Wait or Abort Transmit method times out. Those
 methods indicate a timeout in the Timed Out?
 terminal.

#### Data Overflow Error

Error Code 65539

This error occurs from the CAN Input
 node. This indicates that you did not invoke CAN Input fast enough, and one or more
 CAN frames were lost. Since LabVIEW FPGA executes at a much faster rate than CAN
 frames are received, this can only happen when you introduce artificial delays in
 your FPGA VI. Invoke CAN Input at least once every 50 microseconds to avoid this
 error.

#### Not Run Mode Error

Error Code: 65540

This error occurs when communication
 is stopped and you use a CAN feature that requires communication to be started
 first. Refer to the preceding documentation to determine which features require
 running communication.

- enable Auto Start in the Module Configuration.
- Invoke the Start method.

#### Run Mode Error

Error Code 65541

This error occurs when communication is
 started and you use a CAN feature that requires communication to be stopped. Refer
 to the preceding documentation to determine which feature cannot be used while
 communication is running.

Stop communication on the CAN port before using the
 feature (usually writing a property). To set initial properties, disable
 Auto Start in the *Module Configuration*, then
 set the desired properties, invoke the *Start* method, and proceed with
 your remaining application. To set properties in your main application loop, invoke
 the *Stop* method, set the relevant properties, then invoke the
 *Start* method.

#### Feature Not Supported Error

Error Code 65546

This error is returned by the CAN
 Property node when a property selected for reading or writing is not supported on
 the specified module.

#### Too Many Error Frames Warning

Error Code 65547

This warning occurs when a serious
 fault is detected on the node, resulting in a burst of error frames. This warning
 indicates that one or more error frames may not be reported to LabVIEW FPGA. All
 valid CAN data frames are reported.

Verify that cabling, baud rate, and
 termination of all nodes on the network are correct, and that proper bus power is
 supplied.

Parent topic:

Controller Area Network (CAN) Interface Module Reference

Related concepts:

- Advanced CAN Port Properties
- Transceiver Mode
- Arbitration
- CAN Output
- Module Configuration
- Start
- Stop

<!--NI_TOPIC bundle=ni-compactrio path=fd-baud-rate-advanced.html language=enus -->
## TOPIC 00153: FD Baud Rate Advanced

- bundle_id: `ni-compactrio`
- source_path: `fd-baud-rate-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/fd-baud-rate-advanced.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 613 FD Baud Rate Advanced Property, Output Data Type Field Data Type Permissions Read While Stopped? Read While Running? Write While Stopped? Write While Running? Tq Write No No Yes No SJW Write No No Yes No TSEG1 Write No No Yes No TSEG2 Write No No Yes No TDC Write No No Yes No TDCF Write No No Ye

### FD Baud Rate Advanced

| Field | Data Type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- | --- |
| Tq |  | Write | No | No | Yes | No |
| SJW |  | Write | No | No | Yes | No |
| TSEG1 |  | Write | No | No | Yes | No |
| TSEG2 |  | Write | No | No | Yes | No |
| TDC |  | Write | No | No | Yes | No |
| TDCF |  | Write | No | No | Yes | No |
| TDCO |  | Write | No | No | Yes | No |

This property allows you to configure the custom CAN FD baud rate by setting the nominal bit
 timing and prescaler register of the CAN controller. The table below lists the available
 fields.

| Field | Description | Valid Values |
| --- | --- | --- |
| Transmitter Delay Compensation (TDC) | Enables or disables this feature. | FALSE = disabledTRUE = enabled |
| Transmitter Delay Compensation Offset (TDCO) | Defines the distance between the delay from transmit to receive point and secondary sample point. | 0 to 127 |
| Transmitter Delay Compensation Filter Window Length (TDCF) | Defines the minimum value for the secondary sample point position. Enabled when TDCF is greater than TDCO. | 0 to 127 |
| Time quantum (Tq) | Programs the baud rate prescaler | 25 to 800 in increments of 25 ns |
| Time Segment 1 (TSEG1) | The time segment before the sample point. | 0 to 31 |
| Time Segment 2 (TSEG2) | The time segment after the sample point. | 0 to 15 |
| Synchronization Jump Width (SJW) | The maximum number of time quanta by which a bit sampling period can be extended or shortened as a result of re-synchronization. | 0 to 15Note that the actual hardware interpretation of this value is one more than the programmed value |

The time quantum is calculated by the following formula.

Time quantum = (BRP + 1) * 25

- BRP = nominal bit rate prescaler value

Use the custom sample point calculator on the FPGA I/O Properties page under
 CAN0»Baud Rate»<Custom> to determine the values to enter
 in this field to obtain the desired sample point.

Invalid Parameter or Error 65545 is returned if you
 insert an invalid input.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=fd-baud-rate.html language=enus -->
## TOPIC 00154: FD Baud Rate

- bundle_id: `ni-compactrio`
- source_path: `fd-baud-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/fd-baud-rate.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 612 FD Baud Rate PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesNoThis property sets the baud rate for the transceiver when in FD + BRS CAN mode when transmitting data after the BRS bit. FD Baud Rate or FD Baud Rate Advanced pr

### FD Baud Rate

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

This property sets the baud rate for the transceiver when in FD + BRS CAN mode when transmitting
 data after the BRS bit. FD Baud Rateor FD Baud Rate
 Advanced property only need to be set when I/O mode is set to CAN FD + BRS.

The supported values in kb/s are 200, 250, 400, 500, 800, 1000, 1250, 1600, 2000, 2500, 4000 and 5000. These bit fields are selected to create the desired baud rate with a default sample point of 87.5%

This property converts the baud rate as selected into corresponds Time Quantum (TQ), Synchronization Jump Width (SJW), Data Time Segment Before Sample Point (TSEG1), Data Time Segment After Sample Point (TSEG2), Transmitter Delay Compensation Enabler(TDC) and Transmitter Delay Compensation Filter Window Length (TDCF).

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=finishing-the-clip-design.html language=enus -->
## TOPIC 00155: Finishing the CLIP Design

- bundle_id: `ni-compactrio`
- source_path: `finishing-the-clip-design.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/finishing-the-clip-design.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to finish using the sbRIO CLIP Generator. Review the information on the CLIP Summary page, including any warnings listed in the Configuration Warnings control. Make any changes and resolve warnings that are critical to your application, and click Finish. Review the gener

### Finishing the CLIP Design

Complete the following steps to finish using the sbRIO CLIP Generator.

1. Review the information on the CLIP Summary page, including any warnings listed in the Configuration Warnings control.
2. Make any changes and resolve warnings that are critical to your application, and click Finish .
3. Review the generated CLIP files in the Documents\LabVIEW Data\CompactRIO\CLIPs\<target>\<clipname> directory.
 
 Note 

 If you want to make changes to an existing CLIP after it has been created, you must manually edit the generated CLIP files. You cannot use the sbRIO CLIP Generator to edit an existing CLIP.

#### Optional Tasks to Extend the Generated CLIP Files

(Optional) To support
 additional CLIP design considerations, complete the following steps to manually edit
 the generated CLIP files.

1. To add any custom IP or make modifications to your CLIP design, edit the
 <clipname>.vhd file.
2. To reference a file that the sbRIO CLIP Generator did not generate, complete the
 following steps to edit the
 <clipname>.xml file:
  1. Search for the <ImplementationList> tag.
  2. Within the <ImplementationList> tag, add the
 following code:
 <Path Name="relative path to file">
 <SimulationFileList>
 <SimulationModelType>Same as synthesis</SimulationModelType>
 </SimulationFileList>
</Path>
3. To add timing constraints to your CLIP design, edit the
 <clipname>.xdc file.

After you finish using the sbRIO CLIP Generator, you can complete the following
 tasks:

- Add the CLIP you created for the NI sbRIO target to a LabVIEW project.
- Implement a LabVIEW FPGA VI that interacts with the CLIP I/O for the NI sbRIO
 target.

To view information about completing these tasks, open the installed LabVIEW
 Help and navigate to NI CompactRIO Device Drivers»Devices»Single-Board
 RIO.

Parent topic:

Creating a Component-Level IP for an NI sbRIO Target

Related tasks:

- Configuring Clock Resources for a CLIP

<!--NI_TOPIC bundle=ni-compactrio path=full-duplex.html language=enus -->
## TOPIC 00156: Full Duplex

- bundle_id: `ni-compactrio`
- source_path: `full-duplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/full-duplex.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A typical full-duplex multidrop bus architecture involves a master-slave protocol. Only one device, the master, can control access to the bus. All other devices are slaves. Slave devices must wait for the master to give them access to the bus. In a typical full-duplex system, one transmission line c

### Full Duplex

A typical full-duplex multidrop bus architecture involves a master-slave protocol. Only one
 device, the master, can control access to the bus. All other devices are slaves. Slave
 devices must wait for the master to give them access to the bus.

In a typical full-duplex system, one transmission line connects the bus master
 transmitter to all of the slave receivers. A second transmission line connects all of
 the slave transmitters to the bus master receiver.

Because each transmission line has two separate wires, a full-duplex system is often
 referred to as a four-wire system. The master uses four-wire mode, and the slaves use
 two-wire mode.

The following figure shows a typical full-duplex system.

Figure 123.

[IMAGE alt='Typical Full-Duplex System' src='GUID-CA631A4D-5AE5-4BD9-9FEF-8D4FFF122635-a5.svg']

Parent topic:

Duplex Architectures

<!--NI_TOPIC bundle=ni-compactrio path=functional-safety-modules.html language=enus -->
## TOPIC 00157: Functional Safety Modules

- bundle_id: `ni-compactrio`
- source_path: `functional-safety-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/functional-safety-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 505 C Series Functional Safety Modules C Series Functional Safety Module Description NI-9350 8-Channel C Series Functional Safety Module NI-9351 4-Channel C Series Functional Safety Module

### Functional Safety Modules

| C Series Functional Safety Module | Description |
| --- | --- |
| NI-9350 | 8-Channel C Series Functional Safety Module |
| NI-9351 | 4-Channel C Series Functional Safety Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=getting-started-with-a-compactrio-system-in-l.html language=enus -->
## TOPIC 00158: Getting Started with a CompactRIO System in LabVIEW

- bundle_id: `ni-compactrio`
- source_path: `getting-started-with-a-compactrio-system-in-l.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/getting-started-with-a-compactrio-system-in-l.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the information in this section to help you complete the following tasks as you get started with a CompactRIO embedded system in LabVIEW. Learn Programming Techniques Configure a LabVIEW Project Configure Your Device Use devices in Scan Interface mode, FPGA Interface mode, or Hybrid mode. Set u

### Getting Started with a CompactRIO System in LabVIEW

Use the information in this section to help you complete the following tasks as you get started
 with a CompactRIO embedded system in LabVIEW.

| Learn Programming Techniques | Configure a LabVIEW Project | Configure Your Device |
| --- | --- | --- |
| Use devices in Scan Interface mode, FPGA Interface mode, or Hybrid mode. | Set up a LabVIEW project to use hardware you have installed or hardware you have not installed. | Configure the I/O on your installed hardware. |

- [Programming Interfaces](programming-interfaces.html) Communicate with devices using Scan Interface mode, FPGA Interface mode, or Hybrid mode.
- [Programming Modes](programming-modes.html#GUID-53B1DFF0-F51A-41CF-9E8D-A3E45128385E) Configure the programming mode for each slot on a chassis.
- [Configuring a Project](configuring-a-project.html) Configure a LabVIEW project with connected hardware or offline hardware.
- [Configuring Devices](configuring-devices.html) Configure I/O functions on installed devices and chassis hardware.

Parent topic:

NI CompactRIO Device Drivers

<!--NI_TOPIC bundle=ni-compactrio path=getting-started-with-the-sbrio-9651-in-labvie.html language=enus -->
## TOPIC 00159: Getting Started with the sbRIO-9651 in LabVIEW

- bundle_id: `ni-compactrio`
- source_path: `getting-started-with-the-sbrio-9651-in-labvie.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/getting-started-with-the-sbrio-9651-in-labvie.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sbRIO-9651 System on Module (SOM) requires a mated carrier board in order to function as a complete LabVIEW FPGA and LabVIEW Real-Time target. The sbRIO-9651 reserves some connector pins for specific functionality, such as primary Ethernet and USB ports. The sbRIO-9651 also provides several bank

### Getting Started with the sbRIO-9651 in LabVIEW

The sbRIO-9651 System on Module (SOM) requires a mated carrier board in order to function as a
 complete LabVIEW FPGA and LabVIEW Real-Time target. The sbRIO-9651 reserves some
 connector pins for specific functionality, such as primary Ethernet and USB ports. The
 sbRIO-9651 also provides several banks of additional pins that you can configure for
 purposes specific to your application.

The sbRIO-9651 SOM Development Kit includes a reference carrier board. This
 board demonstrates how to implement additional I/O functionality, such as Serial, CAN,
 and secondary Ethernet.

To use the sbRIO-9651 as a LabVIEW FPGA and LabVIEW Real-Time target in a LabVIEW project, first
 create a socketed component-level IP (CLIP) that defines the I/O configuration to use in
 your application.

Use this tutorial to create a CLIP for the sbRIO-9651 and add it to a LabVIEW project.

Before You Begin:

- Before you write any software, use the sbRIO-9651 System on Module Carrier Board Design
 Guide to plan the layout of your carrier board and define the purpose of
 each pin on the connector. Gather the following information to create a CLIP for the
 sbRIO-9651:
  - Processor peripherals to enable
  - Pins to use
  - I/O standards and drive strength to use for the pins
  - Required I/O voltage level
  - LabVIEW FPGA I/O Nodes the application requires
  - Timing constraints or clock resources

After gathering this information, proceed to *Creating a Component-Level IP for the
 sbRIO-9651*.

Parent topic:

sbRIO-9651

Related concepts:

- sbRIO-9651

Related tasks:

- Creating a Component-Level IP for the sbRIO-9651

Related information:

- sbRIO-9651 SOM Carrier Board Design Guide

<!--NI_TOPIC bundle=ni-compactrio path=half-duplex.html language=enus -->
## TOPIC 00160: Half Duplex

- bundle_id: `ni-compactrio`
- source_path: `half-duplex.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/half-duplex.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: A typical half-duplex multidrop bus architecture also involves a master-slave protocol. In a half-duplex system, all transmitters and receivers are connected to the same transmission line. A half-duplex system is often referred to as a two-wire system. The following figure shows a typical half-duple

### Half Duplex

A typical half-duplex multidrop bus architecture also involves a master-slave protocol. In a
 half-duplex system, all transmitters and receivers are connected to the same
 transmission line.

A half-duplex system is often referred to as a two-wire system.

The following figure shows a typical half-duplex system.

Figure 124.

[IMAGE alt='Typical Half-Duplex System' src='GUID-F5877A7D-C4FE-4C21-89C1-E1F7782E3D04-a5.svg']

Parent topic:

Duplex Architectures

<!--NI_TOPIC bundle=ni-compactrio path=how-do-i-use-9-data-bit-framing.html language=enus -->
## TOPIC 00161: How do I use 9 data bit framing?

- bundle_id: `ni-compactrio`
- source_path: `how-do-i-use-9-data-bit-framing.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/how-do-i-use-9-data-bit-framing.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: While the C-Series serial modules directly support only 5, 6, 7, and 8 data bits, it may be possible to use the parity function to create a ninth data bit, depending on your application. To create and control a ninth data bit, enable parity and set parity mark or parity space for a ninth bit of eith

### How do I use 9 data bit framing?

While the C-Series serial modules directly support only 5, 6, 7, and 8 data bits, it may be possible to use the parity function to create a ninth data bit, depending on your application. To create and control a ninth data bit, enable parity and set parity mark or parity space for a ninth bit of either a 1 or 0, respectively. However, you must do this every time the ninth bit changes state, and thus it may not work for high-throughput applications.

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=i-o-mode.html language=enus -->
## TOPIC 00162: I/O Mode

- bundle_id: `ni-compactrio`
- source_path: `i-o-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/i-o-mode.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 617 I/O Mode PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesNoThis property configures the CAN operating mode. The following table lists property values. 618 I/O Mode Property Values Property Description CAN(default) The defaul

### I/O Mode

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

This property configures the CAN operating mode. The following table lists property values.

| Property | Description |
| --- | --- |
| CAN(default) | The default CAN 2.0 A/B standard I/O mode as defined in ISO 11898-1:2003. A fixed baud rate is used for transfer, and the payload length is limited to 8 bytes. |
| CAN FD | The CAN FD mode as specified in the CAN with Flexible Data-Rate specification, version 1.0. Payload lengths up to 64 are allowed, but they are transmitted at a single fixed baud rate. |
| CAN FD + BRS | The CAN FD as specified in the CAN with Flexible Data-Rate specification, version 1.0, with the optional Baud Rate Switching enabled. The same payload lengths as CAN FD mode are allowed; additionally, the data portion of the CAN frame is transferred at a different (higher) baud rate. |

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=implementing-fpga-vis-for-the-sbrio-9651.html language=enus -->
## TOPIC 00163: Implementing FPGA VIs for the sbRIO-9651

- bundle_id: `ni-compactrio`
- source_path: `implementing-fpga-vis-for-the-sbrio-9651.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/implementing-fpga-vis-for-the-sbrio-9651.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following tasks before performing this procedure. Use the sbRIO CLIP Generator to generate a unique socketed CLIP. dd the CLIP to a LabVIEW project. Connect the sbRIO-9651 to your computer with a USB cable or through a network. Configure the sbRIO-9651 with Measurement & Automation Expl

### Implementing FPGA VIs for the sbRIO-9651

- Use the sbRIO CLIP Generator to generate
 a unique socketed CLIP .
- dd the CLIP to a LabVIEW project.
- Connect the sbRIO-9651 to your computer with a
 USB cable or through a network.
- Configure the sbRIO-9651 with Measurement
 & Automation Explorer (MAX).

Complete the following steps to implement a LabVIEW FPGA VI for the sbRIO-9651.

1. Create and compile your FPGA VI.
2. If you enabled any peripherals in your CLIP,
 such as secondary ethernet, CAN, or serial,
 download your FPGA VI to the flash of the
 sbRIO-9651 to load on boot in order to ensure that
 the driver for the peripheral can load properly at
 boot time.

You should now be able to run and deploy the system just like any other sbRIO
 device.

Parent topic:

sbRIO-9651

Related tasks:

- Creating a Component-Level IP for the sbRIO-9651
- Adding a CLIP for a Single-Board RIO Device to a LabVIEW Project

<!--NI_TOPIC bundle=ni-compactrio path=input-timeout.html language=enus -->
## TOPIC 00164: Input Timeout

- bundle_id: `ni-compactrio`
- source_path: `input-timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/input-timeout.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 619 Input Timeout PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesNoThis property specifies the time to wait for the reading of CAN frame using CAN Input. The resolution is in milliseconds. The timeout value of -1 (infinite wait

### Input Timeout

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

This property specifies the time to wait for the reading of CAN frame using CAN Input. The resolution is in milliseconds.

The timeout value of -1 (infinite wait) is supported.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=io-methods-sbrio.html language=enus -->
## TOPIC 00165: I/O Methods for sbRIO Devices

- bundle_id: `ni-compactrio`
- source_path: `io-methods-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/io-methods-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### I/O Methods for sbRIO Devices

- [Reset](reset-sbrio.html)
- [Start](start_2.html)
- [Stop](stop_2.html)
- [Abort Transmit](abort-transmit-sbrio.html)
- [Wait on Comm State Change](wait-on-comm-state-change_2.html)
- [Wait on Transceiver Wakeup](wait-on-transceiver-wakeup_2.html)
- [Wait on Transmit Complete](wait-on-transmit-complete_2.html)

Parent topic:

sbRIO-9603/9608/9609/9628/9638/9629 CAN API

<!--NI_TOPIC bundle=ni-compactrio path=io-sample-method-fpga-interface-9204.html language=enus -->
## TOPIC 00166: IO Sample Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `io-sample-method-fpga-interface-9204.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/io-sample-method-fpga-interface-9204.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method acquires a single sample from the module. The channel number, terminal mode, and voltage range are all configurable at run time. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. NI suggests that you do no

### IO Sample Method (FPGA Interface)

This module method acquires a single sample from the module. The channel number, terminal
 mode, and voltage range are all configurable at run time. To use this module method,
 select it in an FPGA I/O Method Node that is configured for the
 appropriate device and/or channel.

Note

IO Sample

IO Sample

|  | Configuration [i+2] contains encoded configuration information that gets loaded into the module conversion pipeline. This configuration information controls the data to be sampled two iterations into the future. Refer to the Conversion Timing topic for more information. Refer to the Configuration Encoding table below for an example of how the configuration information is encoded. |
| --- | --- |

|  | Data [i] Returns the data from the current sample. |
| --- | --- |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

#### Configuration Encoding Table

The following table describes how to construct the Configuration [i+2] value to write to the IO Sample method to perform a particular operation. The Operation column lists the types of operations that can be performed using the IO Sample method. The Configuration Bit Fields column lists the bit positions within the Configuration [i+2] number that need to be set. The Values column specifies the binary value to apply to the specified Configuration Bit Fields.

| Operation | Configuration Bit Fields | Values |
| --- | --- | --- |
| AI Read | 15:11 | 001b |
| 10:8 | 000b for channels 0 or 8, 001b for channels 1 or 9, … 110b for channels 6 or 14, 111b for channels 7 or 15 |  |
| 7:6 | 00b |  |
| 5:4 | 00b for NRSE mode11b for RSE or DIFF modes |  |
| 3:2 | 11b for channels 8-15, 01b for DIFF mode on channels 0-7, 10b for RSE or NRSE mode on channels 0-7 |  |
| 1:0 | 00b for ±10 V, 01b for ±5 V, 10b for ±1 V, 11b for ±200 mV |  |
| DI0 Read | 15:0 | 0000000000000000b |

#### Using this Method

The IO Sample method provides an efficient and flexible interface to the module. You can use this method to acquire a single sample from any of the channels on the module, at any range, and with any available input mode.

When this method is executed, the module performs a single conversion on the next channel present in the conversion pipeline on the module. The data from this conversion is returned via the Data [i] method output. At the same time that the conversion data is read from the module, the new configuration information specified by the Configuration [i+2] input is loaded into the configuration pipeline on the module. The pipeline is two samples deep. So, the configuration information specified on one execution of the IO Sample method determines which channel will be sampled by the IO Sample method two iterations into the future. Refer to the *Conversion Timing* topic for more details.

#### Examples

Refer to the NI 9204 Basic IO VI and the NI 9204 Advanced IO VI in the labview\examples\CompactRIO\Module Specific\NI 9204\NI 9204 Basic IO\NI 9204 Basic IO.lvproj and labview\examples\CompactRIO\Module Specific\NI 9204\NI 9204 Advanced IO\NI 9204 Advanced IO.lvproj for examples of the IO concepts discussed above.

Parent topic:

NI 9204 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=io-sample-method-fpga-interface-9205-6.html language=enus -->
## TOPIC 00167: IO Sample Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `io-sample-method-fpga-interface-9205-6.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/io-sample-method-fpga-interface-9205-6.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method acquires a single sample from the module. The channel number, terminal mode, and voltage range are all configurable at run time. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. NI suggests that you do no

### IO Sample Method (FPGA Interface)

Note

|  | Configuration [i+2] contains encoded configuration information that gets loaded into the module conversion pipeline. This configuration information controls the data to be sampled two iterations into the future. Refer to the Conversion Timing topic for more information. Refer to the Configuration Encoding table below for an example of how the configuration information is encoded. |
| --- | --- |

|  | Data [i] Returns the data from the current sample. |
| --- | --- |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

#### Configuration Encoding

The following table describes how to construct the
 Configuration [i+2] value to write to the IO Sample method to
 perform a particular operation.

- The Operation column lists the types of operations
 that can be performed using the IO Sample method.
- The Configuration Bit Fields column lists the bit
 positions within the Configuration [i+2] number that
 need to be set.
- The Values column specifies the binary value to apply
 to the specified Configuration Bit Fields .

| Operation | Configuration Bit Fields | Values |
| --- | --- | --- |
| AI Read | 15:13 | 001b |
| 12:11 | 01b for channels 0-1510b for channels 16-31 |  |
| 10:8 | 000b for channels 0, 8, 16, or 24 001b for channels 1, 9, 17, or 25…110b for channels 6, 14, 22, or 30111b for channels 7, 15, 23, or 31 |  |
| 7:6 | 00b |  |
| 5:4 | 00b for NRSE mode11b for RSE or DIFF modes |  |
| 3:2 | 11b for channels 8-15 or 24-31 01b for DIFF mode on channels 0-7 or 16-2310b for RSE or NRSE mode on channels 0-7 or 16-23 |  |
| 1:0 | 00b for ±10 V01b for ±5 V10b for ±1 V11b for ±200 mV |  |
| DI0 Read | 15:0 | 0000000000000000b |
| DO0 Write | 15:1 | 010000000000000b |
| 0 | Binary value to write to DO0 |  |

#### Using this Method

The IO Sample method provides an
 efficient and flexible interface to the module. You can use this method to acquire a
 single sample from any of the channels on the module, at any range, and with any
 available input mode.

When this method is executed, the module performs a
 single conversion on the next channel present in the conversion pipeline on the
 module. The data from this conversion is returned via the Data
 [i] method output. At the same time that the conversion data is read
 from the module, the new configuration information specified by the
 Configuration [i+2] input is loaded into the
 configuration pipeline on the module. The pipeline is two samples deep. So, the
 configuration information specified on one execution of the IO Sample method
 determines which channel will be sampled by the IO Sample method two iterations into
 the future. Refer to the *Conversion Timing* topic for more details.

#### Examples

Refer to the NI 9205 Basic IO VI
 and the NI 9205 Advanced IO VI in the labview\examples\CompactRIO\Module
 Specific\NI 9205\NI 9205 Basic IO\NI 9205 Basic IO.lvproj and
 labview\examples\CompactRIO\Module Specific\NI 9205\NI 9205 Advanced
 IO\NI 9205 Advanced IO.lvproj for examples of the IO concepts discussed
 above.

Parent topic:

NI 9205 (FPGA Interface)

Related concepts:

- Conversion Timing for the NI 9204/9205/9206 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=io-sample-method-fpga-interface-9205-6_2.html language=enus -->
## TOPIC 00168: IO Sample Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `io-sample-method-fpga-interface-9205-6_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/io-sample-method-fpga-interface-9205-6_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method acquires a single sample from the module. The channel number, terminal mode, and voltage range are all configurable at run time. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. NI suggests that you do no

### IO Sample Method (FPGA Interface)

Note

|  | Configuration [i+2] contains encoded configuration information that gets loaded into the module conversion pipeline. This configuration information controls the data to be sampled two iterations into the future. Refer to the Conversion Timing topic for more information. Refer to the Configuration Encoding table below for an example of how the configuration information is encoded. |
| --- | --- |

|  | Data [i] Returns the data from the current sample. |
| --- | --- |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |

#### Configuration Encoding

The following table describes how to construct the
 Configuration [i+2] value to write to the IO Sample method to
 perform a particular operation.

- The Operation column lists the types of operations
 that can be performed using the IO Sample method.
- The Configuration Bit Fields column lists the bit
 positions within the Configuration [i+2] number that
 need to be set.
- The Values column specifies the binary value to apply
 to the specified Configuration Bit Fields .

| Operation | Configuration Bit Fields | Values |
| --- | --- | --- |
| AI Read | 15:13 | 001b |
| 12:11 | 01b for channels 0-1510b for channels 16-31 |  |
| 10:8 | 000b for channels 0, 8, 16, or 24 001b for channels 1, 9, 17, or 25…110b for channels 6, 14, 22, or 30111b for channels 7, 15, 23, or 31 |  |
| 7:6 | 00b |  |
| 5:4 | 00b for NRSE mode11b for RSE or DIFF modes |  |
| 3:2 | 11b for channels 8-15 or 24-31 01b for DIFF mode on channels 0-7 or 16-2310b for RSE or NRSE mode on channels 0-7 or 16-23 |  |
| 1:0 | 00b for ±10 V01b for ±5 V10b for ±1 V11b for ±200 mV |  |
| DI0 Read | 15:0 | 0000000000000000b |
| DO0 Write | 15:1 | 010000000000000b |
| 0 | Binary value to write to DO0 |  |

#### Using this Method

The IO Sample method provides an
 efficient and flexible interface to the module. You can use this method to acquire a
 single sample from any of the channels on the module, at any range, and with any
 available input mode.

When this method is executed, the module performs a
 single conversion on the next channel present in the conversion pipeline on the
 module. The data from this conversion is returned via the Data
 [i] method output. At the same time that the conversion data is read
 from the module, the new configuration information specified by the
 Configuration [i+2] input is loaded into the
 configuration pipeline on the module. The pipeline is two samples deep. So, the
 configuration information specified on one execution of the IO Sample method
 determines which channel will be sampled by the IO Sample method two iterations into
 the future. Refer to the *Conversion Timing* topic for more details.

#### Examples

Refer to the NI 9205 Basic IO VI
 and the NI 9205 Advanced IO VI in the labview\examples\CompactRIO\Module
 Specific\NI 9205\NI 9205 Basic IO\NI 9205 Basic IO.lvproj and
 labview\examples\CompactRIO\Module Specific\NI 9205\NI 9205 Advanced
 IO\NI 9205 Advanced IO.lvproj for examples of the IO concepts discussed
 above.

Parent topic:

NI 9206 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=io-sample-method-fpga-interface.html language=enus -->
## TOPIC 00169: IO Sample Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `io-sample-method-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/io-sample-method-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IO Sample Method module method acquires a single sample from the module. The channel number, terminal mode, and voltage range are configurable at run time. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. Do not confi

### IO Sample Method (FPGA Interface)

IO Sample Method

Note

[IMAGE alt='image' src='GUID-C4C7CFE5-B359-429A-8151-558E55221959-a5.svg']

Voltage Range [i+1]

Conversion Timing

[IMAGE alt='image' src='GUID-C4C7CFE5-B359-429A-8151-558E55221959-a5.svg']

Terminal Mode [i+1]

Conversion Timing

[IMAGE alt='image' src='GUID-C4C7CFE5-B359-429A-8151-558E55221959-a5.svg']

Channel Number [i+1]

Conversion Timing

[IMAGE alt='image' src='GUID-71A21FE7-1CF7-4FC2-8997-44F98BF9AF87-a5.svg']

Data [i]

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

error in

no error

error in

error out

error out

error
 in

error out

error out

error in

| status | Returns TRUE (X) if an error occurred before this VI or function ran.Returns FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
| --- | --- |
| code | The error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
| source | Always contains an empty string. Strings are not supported in LabVIEW FPGA. |

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

error out

error in

error out

error out

Explain Error

| status | Returns TRUE (X) if an error occurred before this VI or function ran.Returns FALSE (checkmark) to indicate a warning or that no error has occurred. |
| --- | --- |
| code | The error code number identifying an error. The default is 0. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
| source | Always contains an empty string. Strings are not supported in LabVIEW FPGA. |

#### Using This Method

The IO
 Sample method provides an efficient and flexible interface to the
 module. Use this method to acquire a single sample from any of the channels on the
 module, at any range and with any available input mode.

When this method
 executes, the module performs a single conversion on the next channel present in the
 conversion pipeline on the module. The data from this conversion is returned via the
 Data [i] method output. While the conversion data is read
 from the module, the new configuration information specified by the three method
 inputs (Voltage Range [i+1], Terminal Mode
 [i+1], and Channel Number [i+1]) is loaded
 into the configuration pipeline on the module. The pipeline is one sample deep. The
 configuration information specified on one execution of the IO
 Sample method determines which channel will be sampled by the
 IO Sample method one iteration into the future. Refer to the
 *Conversion Timing* topic for more details.

Parent topic:

NI ELVIS III (FPGA Interface)

Related concepts:

- Conversion Timing for the NI ELVIS III (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=listen-only.html language=enus -->
## TOPIC 00170: Listen Only

- bundle_id: `ni-compactrio`
- source_path: `listen-only.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/listen-only.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 545 Listen Only Property Data type Permissions Read while stopped? Read while running? Write while stopped? Write while running? Write No No Yes No This property controls Listen Only mode for passive monitoring/logging. FALSE disables Listen Only mode. Received frames are acknowledged, and frames ca

### Listen Only

| Data type | Permissions | Read while stopped? | Read while running? | Write while stopped? | Write while running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

This property controls Listen Only mode for passive
 monitoring/logging.

- FALSE disables Listen Only mode. Received
 frames are acknowledged, and frames can be transmitted using CAN
 Output .
- TRUE enables Listen Only mode. The CAN
 port can only receive frames. The port does not transmit on the network. No
 acknowledgment is transmitted when a frame is received. When listen-only is enabled,
 the Comm State property begins in the Error Passive 
 state.

Parent topic:

I/O Properties for CAN Modules

Related concepts:

- I/O Properties for CAN Modules
- Module Configuration
- Comm State

<!--NI_TOPIC bundle=ni-compactrio path=listen-only_2.html language=enus -->
## TOPIC 00171: Listen Only

- bundle_id: `ni-compactrio`
- source_path: `listen-only_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/listen-only_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 616 Listen Only Property Data type Permissions Read while stopped? Read while running? Write while stopped? Write while running? Write No No Yes No This property controls Listen Only mode for passive monitoring/logging. FALSE disables Listen Only mode. Received frames are acknowledged, and frames ca

### Listen Only

| Data type | Permissions | Read while stopped? | Read while running? | Write while stopped? | Write while running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | No |

This property controls Listen Only mode for passive
 monitoring/logging.

- FALSE disables Listen Only mode. Received
 frames are acknowledged, and frames can be transmitted using CAN
 Output .
- TRUE enables Listen Only mode. The CAN
 port can only receive frames. The port does not transmit on the network. No
 acknowledgment is transmitted when a frame is received. When listen-only is enabled,
 the Comm State property begins in the Error Passive 
 state.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=log-bus-errors-sbrio.html language=enus -->
## TOPIC 00172: Log Bus Errors

- bundle_id: `ni-compactrio`
- source_path: `log-bus-errors-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/log-bus-errors-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 621 Log Bus Errors PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesYesThis property enables the logging of bus errors as frames that can be read using the CAN Input node. The bus error frame is logged when the Texas Instruments

### Log Bus Errors

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | Yes |

This property enables the logging of bus errors as frames that can be read using the CAN Input node.

The bus error frame is logged when the Texas Instruments TCAN4550 CAN controller detects a bus error.

- FALSE indicates that the bus errors will not be logged and cannot
 be read using the CAN Input node (default).
- TRUE indicates that the bus errors will be logged as frames and
 can be read using the CAN Input node.

The bus error frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 5 |
| Type | 6 |
| Data | Bytes 0—Comm State (see below) 1—Transmit Error Counter 2—Receive Error Counter 3—Detected Bus Error 4—X 5—X 6—X 7—X |

Note

X

Reserved

Don't Care

- 0: Error Active
- 1: Error Passive
- 2: Bus Off

- 0: None
- 1: Stuff
- 2: Form
- 3: Ack
- 4: Bit 1
- 5: Bit 0
- 6: CRC

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=log-bus-errors.html language=enus -->
## TOPIC 00173: Log Bus Errors

- bundle_id: `ni-compactrio`
- source_path: `log-bus-errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/log-bus-errors.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 546 Log Bus Errors Property Data type Permissions Write while stopped? Write while running? Write Yes Yes This property enables the logging of bus errors as frames that can be read using the CAN Input node. The bus error frame is logged when the Philips SJA1000 CAN controller detects a bus error and

### Log Bus Errors

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property enables the logging of bus errors as frames that can be read using the CAN Input
 node.

The bus error frame is logged when the Philips SJA1000 CAN controller detects a bus error and the Bus Error Interrupt occurs.

- FALSE indicates that the bus errors will not be logged and cannot
 be read using the CAN Input node (default).
- TRUE indicates that the bus errors will be logged as frames and
 can be read using the CAN Input node.

The bus error frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 4 |
| Type | 6 |
| Data | Bytes 0—Comm State (see below) 1—Transmit Error Counter 2—Receive Error Counter 3—ECC Register 4—X 5—X 6—X 7—X |

Note

X

Reserved

Don't Care

- 0—Error Active
- 1—Error Passive
- 2—Bus Off

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=log-transceiver-faults-14.html language=enus -->
## TOPIC 00174: Log Transceiver Faults

- bundle_id: `ni-compactrio`
- source_path: `log-transceiver-faults-14.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/log-transceiver-faults-14.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 548 Log Transceiver Faults PropertyData typePermissionsWrite while stopped?Write while running?WriteYesYesThis property enables the logging of transceiver faults as frames that can be read using the CAN Input node. FALSE indicates that the transceiver faults will not be logged as frames (default). T

### Log Transceiver Faults

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property enables the logging of transceiver faults as frames that can be read using the *CAN Input* node.

- FALSE indicates that the transceiver faults will not be logged as
 frames (default).
- TRUE indicates that logging is enabled and the transceiver faults
 will be logged as frames which can be monitored using the CAN Input node.

Note

The transceiver fault frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 1 |
| Type | 7 |
| Data | Bytes 0—Transceiver fault. 0=fault cleared, 1=fault present 1—X 2—X 3—X 5—X 6—X 7—X |

Note

X

Reserved

Don't Care

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=log-transceiver-faults-sbrio.html language=enus -->
## TOPIC 00175: Log Transceiver Faults

- bundle_id: `ni-compactrio`
- source_path: `log-transceiver-faults-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/log-transceiver-faults-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 623 Log Transceiver Faults PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesYesThis property enables the logging of transceiver faults as frames that can be read using the CAN Input node. FALSE indicates that the transceiver faul

### Log Transceiver Faults

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | Yes |

This property enables the logging of transceiver faults as frames that can be read using the CAN Input node.

- FALSE indicates that the transceiver faults will not be logged as
 frames (default).
- TRUE indicates that logging is enabled and the transceiver faults
 will be logged as frames which can be monitored using the CAN Input node.

The transceiver fault frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 1 |
| Type | 7 |
| Data | Bytes 0—Transceiver fault. 0=fault cleared, 1=fault present 1—X 2—X 3—X 5—X 6—X 7—X |

Note

X

Reserved

Don't Care

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=loop-timing-for-the-ni-9218-fpga-interface.html language=enus -->
## TOPIC 00176: Loop Timing for the NI 9218 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `loop-timing-for-the-ni-9218-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/loop-timing-for-the-ni-9218-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9218 uses an internal master timebase. When creating a loop with an I/O Node that acquires data from the NI 9218, do not use the Loop Timer or Wait functions. If the loop execution time is slower than the data rate of the NI 9218, the FPGA I/O Node returns an overrun warning and continues to

### Loop Timing for the NI 9218 (FPGA Interface)

The NI 9218 uses an internal master timebase. When creating a loop with an I/O Node that acquires
 data from the NI 9218, do not use the Loop Timer or
 Wait functions. If the loop execution time is slower than the
 data rate of the NI 9218, the FPGA I/O Node returns an overrun warning and continues to
 read from the module.

The overrun warning means that the data the FPGA I/O Node returns is valid, but the function
 missed one or more data points since the last time it read data from the NI 9218.

The function returns the overrun warning when all of the following conditions are true:

- The NI 9218 is in acquisition mode.
- An FPGA I/O Node that is acquiring data from the module executes at least once after you put the module in acquisition mode.
- The FPGA I/O Node did not read one or more data points since the previous time the function executed.

Avoiding Overrun Warnings with the NI 9218

Follow these guidelines when developing an FPGA VI to avoid overrun warnings.

- Ensure that the loop does not execute slower than the data rate of the NI 9218.
- When reading from the NI 9218 and an additional internally timed module in the same loop, use one FPGA I/O Node to read all module channels. You also must synchronize the NI 9218 and the additional internally timed module.
- You can read from an NI 9218 and a non-internally timed analog input module in the same loop if the other module can acquire data as fast or faster than the data rate of the NI 9218. If you use the same FPGA I/O Node to read data from the modules, the FPGA I/O Node does not return data for the other module until the NI 9218 acquires data.
- Use different loops for the NI 9218 and another analog input module that acquires data slower than the NI 9218.

Note

Parent topic:

NI 9218 (FPGA Interface)

Related concepts:

- Configuring the Data Rate for a Module (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ls-ft-termination.html language=enus -->
## TOPIC 00177: LS/FT Termination

- bundle_id: `ni-compactrio`
- source_path: `ls-ft-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ls-ft-termination.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This property applies only to the ports on the NI 9852 low-speed/fault-tolerant module. 550 LS/FT Termination Property Data type Permissions Write while stopped? Write while running? Write Yes No This property enables the setting of the low-speed/fault-tolerant transceiver termination on the NI-9852

### LS/FT Termination

Note

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property enables the setting of the low-speed/fault-tolerant transceiver termination on the
 NI-9852 module to either 1 kiloohm (1.11 kΩ) or 5 kiloohm
 (4.99 kΩ).

This termination affects both R<sub>RTH</sub> and R<sub>RTL</sub>. For more information on
 determining the required termination for your LS/FT node, refer to the ISO 11898-3
 specification (CAN fault-tolerant transmission). You can also refer to the
 Connectors and Cables section of the *NI-CAN Hardware and
 Software Manual*.

- 1 kiloohm indicates that the termination for the LS/FT CAN
 port will be 1 kΩ (default).
- 5 kiloohm indicates that the termination for the LS/FT CAN
 port will be 5 kΩ.

Parent topic:

I/O Properties for CAN Modules

Related concepts:

- I/O Properties for CAN Modules

Related information:

- New NI-CAN Hardware and Software Manual

<!--NI_TOPIC bundle=ni-compactrio path=modular-instruments-modules.html language=enus -->
## TOPIC 00178: Modular Instruments Modules

- bundle_id: `ni-compactrio`
- source_path: `modular-instruments-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/modular-instruments-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 512 C Series Modular Instruments Modules C Series Modular Instruments Module Description NI-9770 30 kHz to 100 MHz, C Series RF Receiver Module NI-9775 ±10 V, Up to 20 MS/s/ch, 14-Bit, 4-Channel C Series Digitizer Module

### Modular Instruments Modules

| C Series Modular Instruments Module | Description |
| --- | --- |
| NI-9770 | 30 kHz to 100 MHz, C Series RF Receiver Module |
| NI-9775 | ±10 V, Up to 20 MS/s/ch, 14-Bit, 4-Channel C Series Digitizer Module |

Parent topic:

C Series Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=module-configuration.html language=enus -->
## TOPIC 00179: Module Configuration

- bundle_id: `ni-compactrio`
- source_path: `module-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/module-configuration.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configuration properties are downloaded to the CAN module each time the FPGA VI runs.Separate configuration properties are provided for each CAN port on the module. Configuration properties are labeled as CAN0 tab and CAN1 tab. Module configuration properties apply to all CAN ports on the module.Con

### Module Configuration

Configuration properties are downloaded to the CAN module each time the FPGA VI runs.

Separate configuration properties are provided for each CAN port on the module. Configuration
 properties are labeled as CAN0 tab and
 CAN1 tab.

Module configuration properties apply to all CAN ports on the
 module.

Configuration properties are downloaded to the CAN module each time the FPGA VI runs.
 Configuration properties are saved as part of the LabVIEW project file and the FPGA VI
 image.

This module configuration often makes it possible for you to avoid setting properties in the VI,
 and focus on CAN Input/Output within the FPGA VI diagram.

Parent topic:

CAN Module Configuration

Related concepts:

- Bit Timing
- Advanced CAN Port Properties
- CAN Input
- Error Terminals
- Start

<!--NI_TOPIC bundle=ni-compactrio path=module-properties.html language=enus -->
## TOPIC 00180: Module Properties

- bundle_id: `ni-compactrio`
- source_path: `module-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/module-properties.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module properties apply to the entire module. To select a module property, right-click the I/O Property Node and select FPGA I/O»NI 9852 or FPGA I/O»NI 9853. Module ID559 Module ID PropertyData typePermissionsWrite while stopped?Write while running?ReadN/AN/AThis property returns the module identifi

### Module Properties

Module properties apply to the entire module.

To select a module property, right-click the I/O Property Node and select FPGA
 I/O»NI 9852 or FPGA I/O»NI 9853.

Parent topic:

Controller Area Network (CAN) Interface Module Reference

Related concepts:

- Module ID
- Serial Number
- Vendor ID

#### Module ID

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

- The module identifier for the NI 9852 CAN module is hexadecimal 71F3.
- The module identifier for the NI 9853 CAN module is hexadecimal 714F.

Related concepts:

- I/O Properties for CAN Modules

#### Serial Number

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property returns the serial number of the CAN module.

#### Vendor ID

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property returns the vendor identifier of the module. The vendor identifier for National
 Instrumentsi s hexadecimal 1093.

Related concepts:

- I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=motion-modules-reference.html language=enus -->
## TOPIC 00181: Motion Module Reference

- bundle_id: `ni-compactrio`
- source_path: `motion-modules-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/motion-modules-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 572 C Series Motion Modules Motion Module Description NI-9501 Bipolar Chopper Stepper C Series Drive Motion Module NI-9502 Brushless Servo C Series Motor Drive Module NI-9503 PWM Stepper C Series Motor Drive Module NI-9505 PWM Stepper C Series Motor Drive Module NI-9512 Stepper, 1-Axis, Single Encod

### Motion Module Reference

| Motion Module | Description |
| --- | --- |
| NI-9501 | Bipolar Chopper Stepper C Series Drive Motion Module |
| NI-9502 | Brushless Servo C Series Motor Drive Module |
| NI-9503 | PWM Stepper C Series Motor Drive Module |
| NI-9505 | PWM Stepper C Series Motor Drive Module |
| NI-9512 | Stepper, 1-Axis, Single Encoder C Series Motor Drive Interface Module |
| NI-9514 | Servo, 1-Axis, Single Encoder C Series Motor Drive Interface Module |
| NI-9516 | Servo, 1-Axis, Dual Encoder C Series Motor Drive Interface Module |

Use the NI 9501/9502/9503/9505 motor drive modules in FPGA Interface
 Mode.

Use the NI-9512/9514/9516 drive interface modules in Scan Interface
 Mode.

<!--NI_TOPIC bundle=ni-compactrio path=mxie-rio-chassis-cseries.html language=enus -->
## TOPIC 00182: MXIe-RIO Chassis

- bundle_id: `ni-compactrio`
- source_path: `mxie-rio-chassis-cseries.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/mxie-rio-chassis-cseries.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists MXIe-RIO Chassis. 32 MXIe-RIO Chassis MXIe-RIO Chassis Model Description NI-9154 8-Slot, Virtex-5 LX50 FPGA, MXI-Express CompactRIO Chassis NI-9155 8-Slot, Virtex-5 LX85 FPGA, MXI-Express CompactRIO Chassis NI-9157 14-Slot, Virtex-5 LX85 FPGA, MXI-Express CompactRIO Chassis

### MXIe-RIO Chassis

The following table lists MXIe-RIO Chassis.

| MXIe-RIO Chassis Model | Description |
| --- | --- |
| NI-9154 | 8-Slot, Virtex-5 LX50 FPGA, MXI-Express CompactRIO Chassis |
| NI-9155 | 8-Slot, Virtex-5 LX85 FPGA, MXI-Express CompactRIO Chassis |
| NI-9157 | 14-Slot, Virtex-5 LX85 FPGA, MXI-Express CompactRIO Chassis |
| NI-9159 | 14-Slot, Virtex-5 LX110 FPGA, MXI-Express CompactRIO Chassis |

Parent topic:

CompactRIO Controller and Chassis Reference

#### MXI-RIO Chassis Front Panel

Figure 20.

[IMAGE alt='image' src='GUID-10530804-A483-4C77-BB77-807A14A6C249-a5.svg']

1. LEDs
2. Upstream Port
3. MXI-Express LINK LEDs
4. Downstream Port
5. Power Connector
6. DIP Switches

#### Reading the MXIe-RIO Chassis Switch State (FPGA Interface)

The MXIe-RIO reconfigurable embedded chassis has USER FPGA DIP switches. Complete the
 following steps to read the switch state of DIP switches on the FPGA.

1. Configure the MXIe-RIO system.
2. Verify that the USER FPGA Switch I/O item is added to the MXIe-RIO
 system.
3. To add a new VI to the MXIe-RIO system, right-click the FPGA target in the Project
 Explorer window and select New»VI from the
 shortcut menu.
4. Place an FPGA I/O Node on the block diagram of the VI.
5. Click the element section of the FPGA I/O Node and select Chassis I/O»USER FPGA1 Switch from the shortcut menu. USER FPGA2 Switch and USER FPGA3 Switch function the same as USER FPGA1 Switch.
6. Right-click the USER FPGA1 Switch output of the FPGA I/O Node and select Create»Indicator from the shortcut menu.

Refer to the 915x Switches and LEDs VI in the labview\examples\CompactRIO\Chassis
 Specific\915x Switches and LEDs\915x Switches and LEDs.lvproj for an
 example of reading USER FPGA switches.

Related concepts:

- Configuring a Project with Connected Hardware

<!--NI_TOPIC bundle=ni-compactrio path=myrio-1900-fpga-interface.html language=enus -->
## TOPIC 00183: myRIO-1900 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `myrio-1900-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/myrio-1900-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 679 Terminals in Software Terminal Description Audiox AudioIn/Left, AudioIn/Right, AudioOut/Left, AudioOut/Right ConnectorA/AIx Analog input channel x, w

### myRIO-1900 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Audiox | AudioIn/Left, AudioIn/Right, AudioOut/Left, AudioOut/Right |
| ConnectorA/AIx | Analog input channel x, where x is the number of the channel. Connector A has AI channels 0 to 3. |
| ConnectorA/AOx | Analog output channel x, where x is the number of the channel. Connector A has AO channels 0 to 1. |
| ConnectorA/DIOy | Digital input/output channel y on Connector A, where y is the number of the channel. Connector A has channels 0 to 15. Use the FPGA I/O Node, the Set Data Output method, or the Set Data Enable method to access this channel. |
| ConnectorA/DIO7:0 | Digital port consisting of channels 0 to 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| ConnectorA/DIO15:8 | Digital port consisting of channels 8 to 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| ConnectorB/AIx | Analog input channel x, where x is the number of the channel. Connector B has AI channels 0 to 3. |
| ConnectorB/AOx | Analog output channel x, where x is the number of the channel. Connector B has AO channels 0 to 1. |
| ConnectorB/DIOy | Digital input/output channel y on Connector B, where y is the number of the channel. Connector B has channels 0 to 15. Use the FPGA I/O Node, the Set Data Output method, or the Set Data Enable method to access this channel. |
| ConnectorB/DIO7:0 | Digital port consisting of channels 0 to 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| ConnectorB/DIO15:8 | Digital port consisting of channels 8 to 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| ConnectorC/AIx | Analog input channel x, where x is the number of the channel. Connector C has AI channels 0 to 1. |
| ConnectorC/AOx | Analog output channel x, where x is the number of the channel. Connector C has AO channels 0 to 1. |
| ConnectorC/DIOy | Digital input/output channel y on Connector C, where y is the number of the channel. Connector C has channels 0 to 7. Use the FPGA I/O Node, the Set Data Output method, or the Set Data Enable method to access this channel. |
| Onboard I/O | AccelerationX, AccelerationY, and AccelerationZ. Use the FPGA I/O Node to access these channels. |
| Onboard I/O | Button0, LED0, LED1, LED2, and LED3. Use the FPGA I/O Node to access these channels. |

#### Arbitration

Configure the arbitration settings for the DIO channels of
 this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. The default arbitration
 setting is Never Arbitrate.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not support any module methods.

#### Properties

This device does not support
 any properties.

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed Loop
 for digital I/O only. To configure the number of output synchronizing registers or
 input synchronizing registers for the channels on this device, use the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

myRIO-1900

<!--NI_TOPIC bundle=ni-compactrio path=myrio-1900.html language=enus -->
## TOPIC 00184: myRIO-1900

- bundle_id: `ni-compactrio`
- source_path: `myrio-1900.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/myrio-1900.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI myRIO-1900 User Guide and Specifications ships with the LabVIEW myRIO Toolkit.myRIO-1900 Pinouts 186 Connector A Pinout myRIO-1900 Connector A Pinout 187 Connector B Pinout myRIO-1900 Connector B Pinout 188 Connector C Pinout myRIO-1900 Connector C Pinout

### myRIO-1900

The *NI myRIO-1900 User Guide and Specifications* ships with the LabVIEW myRIO
 Toolkit.

#### myRIO-1900 Pinouts

Figure 186.

[IMAGE alt='myRIO-1900 Connector A Pinout' src='GUID-1A74DC11-E084-4FC0-950F-E763780A031A-a5.svg']

Figure 187.

[IMAGE alt='myRIO-1900 Connector B Pinout' src='GUID-1A74DC11-E084-4FC0-950F-E763780A031A-a5.svg']

Figure 188.

[IMAGE alt='myRIO-1900 Connector C Pinout' src='GUID-116D38FC-EE8D-493C-8B8F-C2243C2BFD9E-a5.svg']

Parent topic:

myRIO Module Reference

Related concepts:

- Programming Interfaces
- Configuring a Project with Connected Hardware
- Configuring a Project with Offline Hardware

<!--NI_TOPIC bundle=ni-compactrio path=myrio-1950-fpga-interface.html language=enus -->
## TOPIC 00185: myRIO-1950 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `myrio-1950-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/myrio-1950-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 681 Terminals in Software Terminal Description ConnectorA/AIx Analog input channel x, where x is the number of the channel. Connector A has AI channels 0

### myRIO-1950 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| ConnectorA/AIx | Analog input channel x, where x is the number of the channel. Connector A has AI channels 0 to 3. |
| ConnectorA/AOx | Analog output channel x, where x is the number of the channel. Connector A has AO channels 0 to 1. |
| ConnectorA/DIOy | Digital input/output channel y on Connector A, where y is the number of the channel. Connector A has channels 0 to 15. Use the FPGA I/O Node, the Set Data Output method, or the Set Data Enable method to access this channel. |
| ConnectorA/DIO7:0 | Digital port consisting of channels 0 to 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| ConnectorA/DIO15:8 | Digital port consisting of channels 8 to 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| ConnectorB/AIx | Analog input channel x, where x is the number of the channel. Connector B has AI channels 0 to 3. |
| ConnectorB/AOx | Analog output channel x, where x is the number of the channel. Connector B has AO channels 0 to 1. |
| ConnectorB/DIOy | Digital input/output channel y on Connector B, where y is the number of the channel. Connector B has channels 0 to 15. Use the FPGA I/O Node, the Set Data Output method, or the Set Data Enable method to access this channel. |
| ConnectorB/DIO7:0 | Digital port consisting of channels 0 to 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| ConnectorB/DIO15:8 | Digital port consisting of channels 8 to 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| Onboard I/O | AccelerationX, AccelerationY, and AccelerationZ. Use the FPGA I/O Node to access these channels. |
| Onboard I/O | Button0, LED0, LED1, LED2, and LED3. Use the FPGA I/O Node to access these channels. |

#### Arbitration

Configure the arbitration settings for the DIO channels of
 this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. The default arbitration
 setting is Never Arbitrate.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not support any module methods.

#### Properties

This device does not support
 any properties.

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed Loop
 for digital I/O only. To configure the number of output synchronizing registers or
 input synchronizing registers for the channels on this device, use the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

myRIO-1950

<!--NI_TOPIC bundle=ni-compactrio path=myrio-1950.html language=enus -->
## TOPIC 00186: myRIO-1950

- bundle_id: `ni-compactrio`
- source_path: `myrio-1950.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/myrio-1950.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI myRIO-1950 User Guide and Specifications ship with the LabVIEW myRIO Toolkit.myRIO-1950 Pinouts 189 Connector A Pinout myRIO-1950 Connector A Pinout 190 Connector B Pinout myRIO-1950 Connector B Pinout 191 Connector C Pinout myRIO-1950 Connector C Pinout

### myRIO-1950

The *NI myRIO-1950 User Guide and Specifications* ship with the LabVIEW myRIO
 Toolkit.

#### myRIO-1950 Pinouts

Figure 189.

[IMAGE alt='myRIO-1950 Connector A Pinout' src='GUID-F501FED8-0F61-40FB-8D38-0F4D1D796A31-a5.svg']

Figure 190.

[IMAGE alt='myRIO-1950 Connector B Pinout' src='GUID-F501FED8-0F61-40FB-8D38-0F4D1D796A31-a5.svg']

Figure 191.

[IMAGE alt='myRIO-1950 Connector C Pinout' src='GUID-4011733A-6737-4379-9B1E-677F37F8FE4E-a5.svg']

Parent topic:

myRIO Module Reference

Related concepts:

- Programming Interfaces

<!--NI_TOPIC bundle=ni-compactrio path=myrio-module-reference.html language=enus -->
## TOPIC 00187: myRIO Module Reference

- bundle_id: `ni-compactrio`
- source_path: `myrio-module-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/myrio-module-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use myRIO modules with NI CompactRIO Device Drivers in LabVIEW. For information about creating applications for myRIO modules, refer to Getting Started with the myRIO Toolkit. 678 myRIO Devices myRIO Module Description myRIO-1900 Portable, reconfigurable I/O module. 10 AI channels, 6 AO channels, 40

### myRIO Module Reference

NI CompactRIO Device
 Drivers

Tip

Getting Started with the
 myRIO Toolkit

| myRIO Module | Description |
| --- | --- |
| myRIO-1900 | Portable, reconfigurable I/O module. 10 AI channels, 6 AO channels, 40 DIO channels, Xilinx Z-7010 FPGA |
| myRIO-1950 | Portable, reconfigurable I/O module. 10 AI channels, 6 AO channels, 40 DIO channels, Xilinx Z-7010 FPGA |
| NI ELVIS | Portable, reconfigurable I/O control module. 8 AI channels, 4 AO channels, 32 DIO channels, Xilinx Z-7010 FPGA |
| NI ELVIS III | Reconfigurable I/O module. 16 AI channels, 4 AO channels, 40 DIO channels, Xilinx Z-7020 FPGA |

Note

NI Engineering Laboratory Virtual Instrumentation Suite

Related information:

- Getting Started with the myRIO Toolkit
- myRIO-1900 Getting Started Guide and Specifications
- myRIO-1950 Getting Started Guide and Specifications

<!--NI_TOPIC bundle=ni-compactrio path=new-features-and-changes.html language=enus -->
## TOPIC 00188: NI CompactRIO New Features and Changes

- bundle_id: `ni-compactrio`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI CompactRIO. Discover what is new in the latest releases of NI CompactRIO.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version mi

### NI
 CompactRIO
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI
 CompactRIO.

NI
 CompactRIO

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI
 CompactRIO
 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in NI
 CompactRIO 2026 Q2.

##### New
 Features

This version of NI
 CompactRIO
 adds support for the following features:

- Added Scan Interface support for the NI 9204.

#### NI CompactRIO 2025
 Q4 Changes

Learn about new features, behavior changes, and other updates in NI CompactRIO 2025 Q4.

##### Hardware Support

- Added support for the following NI CompactRIO devices:
  - NI 9320

#### NI CompactRIO 2025
 Q1 Changes

Learn about new features, behavior changes, and other updates in NI CompactRIO 2025 Q1.

##### Hardware Support

- Added connector variants for the following NI CompactRIO 
 devices:
  - NI 9222
  - NI 9223
  - NI 9225
  - NI 9227
  - NI 9228
  - NI 9229
  - NI 9230
  - NI 9232
  - NI 9238
  - NI 9239
  - NI 9269

#### NI CompactRIO 2024
 Q4 Changes

Learn about new features, behavior changes, and other updates in NI CompactRIO 2024 Q4.

##### Hardware Support

- Added support for the following NI CompactRIO devices:
  - NI 9204

<!--NI_TOPIC bundle=ni-compactrio path=ni-9201-fpga-interface.html language=enus -->
## TOPIC 00189: NI 9201 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9201-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9201-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in Software To access the following terminals for this device, use the FPGA I/O Node. 99 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9201 has

### NI 9201 (FPGA Interface)

#### FPGA I/O Node

Use an FPGA I/O
 Node configured for reading with this
 device.

#### Terminals in Software

To access the
 following terminals for this device, use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9201 has AI channels 0 to 7. |

You can configure the minimum time between conversions and the channels to
 scan.

#### Arbitration

This device only supports the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure
 arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following properties for this device, use the
 FPGA I/O Property Node.

| Property | I/O Type | Description |
| --- | --- | --- |
| LSB Weight | AO | Returns the LSB weight in nV/LSB for the channel. Use this value to convert data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset | AO | Returns the calibration offset in nV for the channel. Use this value to convert data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Module Properties

To access the following module properties for this
 device, use the FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x70A4. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9201

<!--NI_TOPIC bundle=ni-compactrio path=ni-9201-scan-interface.html language=enus -->
## TOPIC 00190: NI 9201 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9201-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9201-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module ChannelsThe NI 9201 has the following channels. 104 Module

### NI 9201 (Scan Interface)

#### Module I/O Variables

To use I/O from
 this module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for the channels return calibrated floating-point data in volts.

#### Module Channels

The NI 9201 has the
 following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9201, x is 0 to 7. |

#### C Series Module Properties Dialog Box

Use
 the C Series Module Properties dialog box to configure the module. Right-click the
 module in the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9201

<!--NI_TOPIC bundle=ni-compactrio path=ni-9201.html language=enus -->
## TOPIC 00191: NI 9201

- bundle_id: `ni-compactrio`
- source_path: `ni-9201.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9201.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±10 V, 12-Bit Analog Input Module NI 9201 Pinout 21 NI 9201 Pinout

### NI 9201

CompactRIO 8-Channel, ±10 V, 12-Bit Analog Input Module

#### NI 9201 Pinout

Figure 21.

[IMAGE alt='image' src='GUID-ECD491D1-C7ED-417D-9A4E-17E734622F8C-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9202-fpga-interface.html language=enus -->
## TOPIC 00192: NI 9202 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9202-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9202-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in Software To access the following terminals for this device, use the FPGA I/O Node. 105 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9202 has

### NI 9202 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device,
 use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9202 has channels 0 to 15. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The onboard clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle timed loop to access this channel. Export the onboard clock of the NI 9202 to access this channel. |
| Start | Channel that controls when the NI 9202 starts acquiring data. If TRUE is written to the Start channel, the NI 9202 starts acquiring data. When the NI 9202 is acquiring data, you must write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9202 stops acquiring data. If TRUE is written to the Stop channel, the NI 9202 stops acquiring data. When the NI 9202 is acquiring data, you must write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device only supports the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure
 arbitration settings for this device.

#### Module Properties

To access the following
 module properties for this device, use the FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9202 acquires data. |
| Module ID | Returns the module ID, 0x788C for the spring terminal and 0x788A for the DSUB variant. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |
| Input Delay | Returns the filter delay based on the data rate and filter setting. |
| Filter Frequency Config | Sets the frequency of the first notch in the filter response. |

Note

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9202

<!--NI_TOPIC bundle=ni-compactrio path=ni-9202-max-rate-synch.html language=enus -->
## TOPIC 00193: NI 9202

- bundle_id: `ni-compactrio`
- source_path: `ni-9202-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9202-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9202 derives its sample rate from the internal master timebase. 46 NI 9202 internal master timebase and sample rate Internal master timebase 12.8 MHz Maximum sample rate when using the internal master timebase 10 kS/s (12.8 MHz/1280) When the module uses the internal master timebase, it can n

### NI 9202

The NI 9202 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 12.8 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 10 kS/s (12.8 MHz/1280) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9202 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9202 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 10 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 10.24 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9202.html language=enus -->
## TOPIC 00194: NI 9202

- bundle_id: `ni-compactrio`
- source_path: `ni-9202.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9202.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 16-Channel, 24-Bit Differential Analog Input Module NI 9202 Pinout 22 NI 9202 Pinout

### NI 9202

CompactRIO 16-Channel, 24-Bit Differential Analog Input Module

#### NI 9202 Pinout

Figure 22.

[IMAGE alt='image' src='GUID-C8872DA4-DB48-48FF-8727-76810A6F1B48-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9203-fpga-interface.html language=enus -->
## TOPIC 00195: NI 9203 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9203-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9203-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 107 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9203 has AI

### NI 9203 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

Use the
 FPGA I/O Node to access the following terminals for this
 device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9203 has AI channels 0 to 7. |

#### Arbitration

This device supports only the
 Arbitrate if Multiple Requestors Only option for
 arbitration. You cannot configure arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

To access the following method for this device, use the
 FPGA I/O Method Node.

| Method | Description |
| --- | --- |
| Set Input Range | Sets the input range for a channel as either 0–20 mA or ±20 mA. This method overwrites the value you configure in the C Series Module Properties dialog box. |

#### I/O
 Properties

To access the following properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight (±20 mA range) | Returns the LSB weight in pA/LSB for the channel. Use this value to convert and calibrate NI 9203 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box, and you set the input range to ±20 mA. |
| LSB Weight (4–20 mA range) | Returns the LSB weight in pA/LSB for the channel. Use this value to convert and calibrate NI 9203 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box, and you set the input range to 0–20 mA. |

#### Module Properties

Use the FPGA I/O Property Node
 to access the following properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x7129. |
| Offset (±20 mA range) | Returns the calibration offset in pA for the channel. Use this value to convert and calibrate NI 9203 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box, and you set the input range to ±20 mA. |
| Offset (4–20 mA range) | Returns the calibration offset in pA for the channel. Use this value to convert and calibrate NI 9203 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box, and you set the input range to 0–20 mA. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does
 not support the single-cycle Timed Loop.

Parent topic:

NI 9203

<!--NI_TOPIC bundle=ni-compactrio path=ni-9203-scan-interface.html language=enus -->
## TOPIC 00196: NI 9203 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9203-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9203-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in amps. Module Channels 109 Module Channels Channel Description AIx Analog

### NI 9203 (Scan Interface)

#### Module I/O Variables

To use I/O from
 this module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for the channels return calibrated floating-point data in amps.

#### Module Channels

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9203, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use the C Series Module Properties
 dialog box to configure the module. Right-click the module in the Project
 Explorer window and select Properties to
 display this dialog box. You can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channel Configuration —You can specify the input range for
 each channel.
  - Channels —Specifies the channel(s) for which you
 want to select the input range.
  - Input Range —Specifies the input range for the
 selected channel(s) as either 0–20 mA or ±20 mA.

Parent topic:

NI 9203

<!--NI_TOPIC bundle=ni-compactrio path=ni-9205.html language=enus -->
## TOPIC 00197: NI 9205

- bundle_id: `ni-compactrio`
- source_path: `ni-9205.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9205.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 32-Channel Single-Ended/16-Channel Differential, ±200 mV to ±10 V, 16-Bit Analog Input Module NI 9205 Pinout 26 NI 9205 Pinout

### NI 9205

CompactRIO 32-Channel Single-Ended/16-Channel Differential, ±200 mV to ±10 V, 16-Bit Analog Input Module

#### NI 9205 Pinout

Figure 26.

[IMAGE alt='image' src='GUID-8F0331B2-707D-44B6-868A-BB9F5C36C9C1-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9207-fpga-interface.html language=enus -->
## TOPIC 00198: NI 9207 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9207-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9207-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareTo access the following terminals for this device, use the FPGA I/O Node. 119 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9207 has A

### NI 9207 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device,
 use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9207 has AI channels 0 to 15. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

This device does not support any module
 methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

To access the following module properties for this
 device, use the FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Options are High Speed or High Resolution. This property overwrites the value configured in the C Series Module Properties dialog box.Returns the conversion time setting when configured to read.Refer to the NI 9207 hardware documentation for more information about conversion times. |
| Module ID | Returns the module ID, 0x74AD. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9207

<!--NI_TOPIC bundle=ni-compactrio path=ni-9207-scan-interface.html language=enus -->
## TOPIC 00199: NI 9207 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9207-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9207-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for channels AI0–AI7 return calibrated floating-point data in volts. The I/O variables for channels AI8–AI15 return calibrated floa

### NI 9207 (Scan Interface)

#### Module I/O Variables

To use I/O from
 this module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for channels AI0–AI7 return calibrated floating-point data in volts. The I/O
 variables for channels AI8–AI15 return calibrated floating-point data in
 amps.

#### Module Channels

The NI 9207 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9207, x is 0 to 15. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. To display this dialog box, right-click the module in the Project
 Explorer window and select Properties. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Determines the time it takes to acquire
 one point of data from one or more channels. Select High
 Speed or High Resolution . For more
 information about the conversion times, refer to the NI 9207 hardware
 documentation.

Parent topic:

NI 9207

<!--NI_TOPIC bundle=ni-compactrio path=ni-9212-fpga-interface.html language=enus -->
## TOPIC 00200: NI 9212 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9212-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9212-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareTo access the following terminals for this device, use the FPGA I/O Node. 135 Terminals in Software Terminal Description TCx Thermocouple input channel x, where x is the number of the channel. The NI 9212

### NI 9212 (FPGA Interface)

#### FPGA I/O
 Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device, use the
 FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| TCx | Thermocouple input channel x, where x is the number of the channel. The NI 9212 has TC channels 0 to 7. |
| CJC | Cold-junction compensation channel x, where x is the number of the channel. The NI 9212 has CJC channels 0 to 1. For the best accuracy, read the appropriate CJC channel in the same FPGA I/O Node as the corresponding thermocouple input channels. Convert the CJC data to temperature. CJC 0—corresponds to thermocouple input channels TC0, TC1, TC2, and TC3. CJC 1—corresponds to thermocouple input channels TC4, TC5, TC6, and TC7. |

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module
 Methods

To access the following method for this device, use the FPGA I/O Method
 Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether the channel was out of range or had an open thermocouple since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Force Status Read—When the value of this input is FALSE, the method returns the cached status information since the last time that the Check Cached Status method executed. When the value is TRUE, the method forces the FPGA I/O Node to read all channels and update the status information. Forcing a status read can introduce jitter into an analog input loop. Open—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open thermocouple on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

This device does not support any I/O properties.

#### Module
 Properties

To access the following module properties for this device, use the FPGA
 I/O Property Node.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Select High Speed, Best 60 Hz Rejection, Best 50 Hz Rejection, or High Resolution. Refer to the NI 9212 with NI TB-9212 Specifications for more information about the conversion times. This property overwrites the value configured in the C Series Module Properties dialog box. Returns the conversion time setting when configured to read. |
| Module ID | Returns the module ID, 0x7705. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle Timed
 Loop.

Parent topic:

NI 9212

Related information:

- NI-9212 with TB-9212 Specifications

<!--NI_TOPIC bundle=ni-compactrio path=ni-9212-scan-interface.html language=enus -->
## TOPIC 00201: NI 9212 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9212-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9212-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. The Sc

### NI 9212 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

Note

#### Module Channels

The NI 9212 has the
 following channels.

| Channel | Description |
| --- | --- |
| TCx | Analog input channel x, where x is the number of the channel. For the NI 9212, x is 0 to 7. |

#### Module-Specific Errors

The NI 9212 can
 return the following module-specific error.

| Error Code | Description |
| --- | --- |
| –65582 | An open thermocouple was detected. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. To display this dialog box, right-click the module in the Project
 Explorer window and select Properties. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Determines the time it takes to acquire
 one point of data from one or more channels. Select High
 Speed , Best 60 Hz Rejection ,
 Best 50 Hz Rejection , or High
 Resolution . Refer to the NI 9212 with NI TB-9212
 Specifications for more information about the conversion
 times.
- Channels —Specifies the channel(s) for which you want to
 configure settings.
- Thermocouple Type —Specifies the type of thermocouple
 connected to the channel.
- Measurement Units —Specifies the units you want data to be
 returned in for the channel. You can select Raw Volts ,
 Degrees Kelvin , Degrees
 Celsius , Degrees Fahrenheit , or
 Degrees Rankine .
- Enable Open Thermocouple Detection —If this box is
 checked, the NI 9212 returns a zero value and reports an error if it detects an
 open thermocouple on any channel. This box is checked by default. If you do not
 check this box, each channel of the NI 9212 independently returns full-scale
 data and the NI 9212 does not report an error if an open thermocouple is
 detected. Note Enabling or disabling open thermocouple detection
 on the NI 9212 has no effect on the accuracy of the measurement because this
 option on the module is implemented entirely from software.

Parent topic:

NI 9212

<!--NI_TOPIC bundle=ni-compactrio path=ni-9212.html language=enus -->
## TOPIC 00202: NI 9212

- bundle_id: `ni-compactrio`
- source_path: `ni-9212.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9212.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±78 mV, 24-Bit Channel-to-Channel Isolated Thermocouple Input Module NI 9212 Pinout 35 NI 9212 Pinout The NI TB-9212 provides connections for eight thermocouple channels on the NI 9212. 36 NI TB-9212 Pinout

### NI 9212

CompactRIO 8-Channel, ±78 mV, 24-Bit Channel-to-Channel Isolated Thermocouple Input Module

#### NI 9212 Pinout

Figure 35.

[IMAGE alt='image' src='GUID-3B3EA9AD-ABEA-466C-8EFE-BDB1590066A2-a5.svg']

The NI TB-9212 provides connections for eight thermocouple channels on the NI
 9212.

Figure 36.

[IMAGE alt='image' src='GUID-49B78CE3-E6FE-4A01-AE61-AEF5454DEF10-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9213-fpga-interface.html language=enus -->
## TOPIC 00203: NI 9213 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9213-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9213-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareTo access the following terminals for this device, use the FPGA I/O Node. 140 Terminals in Software Terminal Description TCx Thermocouple input channel x, where x is the number of the channel. The NI 9213

### NI 9213 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device,
 use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| TCx | Thermocouple input channel x, where x is the number of the channel. The NI 9213 has TC channels 0 to 15. |
| Autozero | Autozero channel. For the best accuracy, read the Autozero channel in the same FPGA I/O Node as the thermocouple input channels. |
| CJC | Cold-junction compensation channel. For the best accuracy, read the CJC channel in the same FPGA I/O Node as the thermocouple input channels. Convert the CJC data to temperature. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Module Methods

To access the following method for this device, use the
 FPGA I/O Method Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns a Boolean value for each channel that indicates whether the channel was out of range or had an open thermocouple since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Force Status Read—When the value of this input is FALSE, the method returns the cached status information since the last time that the Check Cached Status method executed. When the value is TRUE, the method forces the FPGA I/O Node to read all channels and update the status information. Forcing a status read can introduce jitter into an analog input loop. Out of Range—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index exceeded the common-mode voltage range at some point after the last time that the Check Cached Status method executed. Open—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open thermocouple on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

To access the following module properties for this
 device, use the FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Select High Speed or High Resolution. Refer to the NI 9212 with NI TB-9212 Specifications for more information about the conversion times. This property overwrites the value configured in the C Series Module Properties dialog box. Returns the conversion time setting when configured to read. |
| Module ID | Returns the module ID, 0x7449. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9213

<!--NI_TOPIC bundle=ni-compactrio path=ni-9213-scan-interface.html language=enus -->
## TOPIC 00204: NI 9213 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9213-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9213-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. The Sc

### NI 9213 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

Note

#### Module Channels

The NI 9213 has the
 following channels.

| Channel | Description |
| --- | --- |
| TCx | Analog input channel x, where x is the number of the channel. For the NI 9213, x is 0 to 15. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. To display this dialog box, right-click the module in the Project
 Explorer window and select Properties. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Determines the time it takes to acquire
 one point of data from one or more channels. Select High Speed 
 or High Resolution . Refer to the NI 9213 hardware documentation
 for more information about the conversion times.
- Channels —Specifies the channel(s) for which you want to
 configure settings.
- Thermocouple Type —Specifies the type of thermocouple
 connected to the channel.
- Measurement Units —Specifies the units you want data to be
 returned in for the channel. You can select Raw Volts ,
 Degrees Kelvin , Degrees Celsius ,
 Degrees Fahrenheit , or Degrees
 Rankine .
- Enable Open Thermocouple Detection —If this box is
 checked, the NI 9213 returns a zero value and reports an error if it detects an
 open thermocouple on any channel. This box is checked by default. If you do not
 check this box, each channel of the NI 9213 independently returns full-scale
 data and the NI 9213 does not report an error if an open thermocouple is
 detected. Note Enabling or disabling open thermocouple detection
 on the NI 9213 has no effect on the accuracy of the measurement because this
 option on the module is implemented entirely from software.

Parent topic:

NI 9213

<!--NI_TOPIC bundle=ni-compactrio path=ni-9213.html language=enus -->
## TOPIC 00205: NI 9213

- bundle_id: `ni-compactrio`
- source_path: `ni-9213.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9213.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 16-Channel, ±78 mV, 24-Bit Thermocouple Input Module NI 9213 Pinout 37 NI 9213 Pinout

### NI 9213

CompactRIO 16-Channel, ±78 mV, 24-Bit Thermocouple Input Module

#### NI 9213 Pinout

Figure 37.

[IMAGE alt='image' src='GUID-1735E8F2-E6DA-4B68-A36D-FC221A681B3A-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9217.html language=enus -->
## TOPIC 00206: NI 9217

- bundle_id: `ni-compactrio`
- source_path: `ni-9217.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9217.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 24-Bit, 100 Ω RTD Analog Input Module NI 9217 Pinout 41 NI 9217 Pinout

### NI 9217

CompactRIO 4-Channel, 24-Bit, 100 Ω RTD Analog Input Module

#### NI 9217 Pinout

Figure 41.

[IMAGE alt='image' src='GUID-AA6E4F0F-44D6-46B6-9767-E6236F6C8A58-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9218-data-rates.html language=enus -->
## TOPIC 00207: NI 9218 Data Rates

- bundle_id: `ni-compactrio`
- source_path: `ni-9218-data-rates.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9218-data-rates.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frequency of a master timebase (f[M]) controls the data rate (f[s]) of the NI 9218. The NI 9218 includes an internal master timebase with a frequency of 13.1072 MHz, but the module can also accept an external master timebase or export its own master timebase. Internal Master Timebase The followi

### NI 9218 Data Rates

The frequency of a master timebase (f<sub>M</sub>) controls the data rate (f<sub>s</sub>) of the
 NI 9218. The NI 9218 includes an internal master timebase with a frequency of 13.1072
 MHz, but the module can also accept an external master timebase or export its own master
 timebase.

#### Internal Master Timebase

The
 following equation provides the available data rates for the NI 9218 with the
 internal master timebase.

[IMAGE alt='image' src='GUID-06BD16EC-83B6-45C8-927C-613B349376C1-a5.svg']

- n is any integer from 1 to 31.

Refer to the following table for the available data rates with the internal
 master timebase.

| 51.200 | 5.689 | 3.012 | 2.048 |
| --- | --- | --- | --- |
| 25.600 | 5.120 | 2.845 | 1.969 |
| 17.067 | 4.654 | 2.695 | 1.896 |
| 12.800 | 4.267 | 2.560 | 1.829 |
| 10.240 | 3.938 | 2.438 | 1.765 |
| 8.533 | 3.657 | 2.328 | 1.707 |
| 7.314 | 3.413 | 2.226 | 1.652 |
| 6.400 | 3.200 | 2.133 | — |

#### External Master Timebase

The NI 9218 has
 a different set of data rates when using an external master timebase with a
 frequency other than 13.1072 MHz. To synchronize the data rate of an NI 9218 with
 other modules that use master timebases to control sampling, all of the modules must
 share a single master timebase source.

Parent topic:

NI 9218 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9218-fpga-interface.html language=enus -->
## TOPIC 00208: NI 9218 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9218-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9218-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9218 with other modules that have a selectable timebase source. Terminals in Software 162 Terminals in Software Terminal Description AIx AI input channel x, where x is the number of the channel. T

### NI 9218 (FPGA Interface)

#### FPGA I/O
 Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9218 has RTD channels 0 to 1. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1072 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9218 to access this channel. |
| Start | Channel that controls when the NI 9218 starts acquiring data. To acquire data, write TRUE to the Start channel. When the NI 9218 is acquiring data, you must write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the NI 9218 stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the NI 9218 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

You can read TEDS information from the NI 9218.

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure arbitration
 settings for this device.

#### Module
 Methods

To access the following method for this device, use the FPGA I/O Method
 Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was an excitation fault or open loop on the channel since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Excitation Fault—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an excitation fault on the channel at some point after the last time that the Check Cached Status method executed. Open Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open loop on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

To access the following I/O properties for this device, use the FPGA
 I/O Property Node.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of ten modes: ±60 V; ±16 V; ±16 V, 12 V Ex.; ±65 mV; ±65 mV, 12 V Ex.; ±20 mA; ±20 mA, 12 V Ex.; ±22 mV/V Bridge, 2 V Ex.; ±22 mV/V Bridge, 3.3 V Ex.; ±5 V IEPE AC Coupled. |
| LSB Weight (±16 V range) | Returns the LSB weight in pV/LSB for the ±16 V range. |
| LSB Weight (±20 mA range) | Returns the LSB weight in fV/LSB for the ±20 mA range. |
| LSB Weight (±22 mV/V range) | Returns the LSB weight in fV/LSB for the ±22 mV/V range. |
| LSB Weight (±5 V IEPE range) | Returns the LSB weight in pV/LSB for the ±5 V IEPE range. |
| LSB Weight (±65 mV range) | Returns the LSB weight in fV/LSB for the ±65 mV range. |
| LSB Weight (±60 V range) | Returns the LSB weight in pV/LSB for the ±60 V range. |
| Offset (±16 V range) | Returns the calibration offset in nV for the ±16 V range. |
| Offset (±20 mA range) | Returns the calibration offset in nV for the ±20 mA range. |
| Offset (±22 mV/V range) | Returns the calibration offset in nV for the ±22 mV/V range. |
| Offset (±5 V IEPE range) | Returns the calibration offset in nV for the ±5 V IEPE range. |
| Offset (±65 mV range) | Returns the calibration offset in nV for the ±65 mV range. |
| Offset (±60 V range) | Returns the calibration offset in nV for the ±60 V range. |
| Offset Cal Enable | Enables offset calibration. This disconnects both signal input pins and internally connects a short to the ADC driver circuitry. |
| Shunt Cal Enable | Controls the shunt calibration switch for each channel. |

#### Module
 Properties

Use the FPGA I/O Property Node to access the following module
 properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI-9218 acquires data. |
| Module ID | Returns the module ID, 0x7757. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Excitation Protection

- The voltage supplied to the external power connector on the NI 9218 is below the
 minimum required voltage.
- The excitation pins on the NI 9218 are shorted together.
- The connected load exceeds the powered sensor output current limit.

error 65654

- If a warning occurs, only the channel(s) with the fault are affected and all other
 channels on the module continue to function properly without interruption.
- If an error occurs, the module is unable to recover from the fault condition and you
 must restart the module after the fault is removed.

#### Single-Cycle Timed Loop

This device does not support the single-cycle Timed
 Loop.

Parent topic:

NI 9218

<!--NI_TOPIC bundle=ni-compactrio path=ni-9218-scan-interface.html language=enus -->
## TOPIC 00209: NI 9218 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9218-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9218-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. Module C

### NI 9218 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

#### Module Channels

The NI 9218 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9218, x 0 to 1. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 configure settings.
- Input Configuration —Sets the input configuration of the
 corresponding channel to one of ten modes: ±60 V; ±16 V; ±16 V, 12 V Ex.; ±65
 mV; ±65 mV, 12 V Ex.; ±20 mA; ±20 mA, 12 V Ex.; ±22 mV/V Bridge, 2 V Ex.; ±22
 mV/V Bridge, 3.3 V Ex.; ±5 V IEPE AC Coupled.

Parent topic:

NI 9218

<!--NI_TOPIC bundle=ni-compactrio path=ni-9218.html language=enus -->
## TOPIC 00210: NI 9218

- bundle_id: `ni-compactrio`
- source_path: `ni-9218.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9218.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 2-Channel, 24-Bit Dynamic Universal Analog Input Module NI 9218 Pinout 42 NI 9218 Pinout 161 NI 9218 Pin Assignments by Mode Pin Mode Bridge Voltage IEPE TEDS ±22 mV/V ±65 mV ±16 V ±5 V Class 1 1 EX+ EX+^* EX+^* — — 2 — — — AI+ TEDS+ 3 EX- EX-^* AI-, EX-^* AI- TEDS- 4 RS+ — — — — 5 RS- —

### NI 9218

CompactRIO 2-Channel, 24-Bit Dynamic Universal Analog Input Module

#### NI 9218 Pinout

Figure 42.

[IMAGE alt='image' src='GUID-762ECC6E-851E-4916-A87A-357EA67A9386-a5.svg']

| Pin | Mode |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Bridge | Voltage | IEPE | TEDS |  |  |
| ±22 mV/V | ±65 mV | ±16 V | ±5 V | Class 1 |  |
| 1 | EX+ | EX+* | EX+* | — | — |
| 2 | — | — | — | AI+ | TEDS+ |
| 3 | EX- | EX-* | AI-, EX-* | AI- | TEDS- |
| 4 | RS+ | — | — | — | — |
| 5 | RS- | — | — | — | — |
| 6 | AI+ | AI+ | AI+ | — | — |
| 7 | AI- | AI-† | — | — | — |
| 8 | SC | — | — | — | — |
| 9 | SC | — | — | — | — |
| *Optional sensor excitation. †In ±65 mV mode, you must tie pin 7 (AI-) to pin 3 (EX-). |  |  |  |  |  |

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9219-fpga-interface.html language=enus -->
## TOPIC 00211: NI 9219 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9219-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9219-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in Software 170 Terminals in Software Terminal Description CHx Channel x, where x is the number of the channel. The NI 9219 has channels 0 to 3. CJCx Cold-junction compensation channel x, where x is the number of th

### NI 9219 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| CHx | Channel x, where x is the number of the channel. The NI 9219 has channels 0 to 3. |
| CJCx | Cold-junction compensation channel x, where x is the number of the channel. The NI 9219 has CJC channels 0 to 3. If a channel is in Thermocouple mode, you can read CJC data for the channel. Convert the CJC data to temperature. |

You can read TEDS information from the NI 9219.

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any
 methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Voltage Range | Sets the range of a channel in Voltage mode. |
| Resistance Range | Sets the range of a channel in Resistance mode. |
| RTD Range | Sets the range of a channel in RTD mode. |
| Quarter Bridge Range | Sets the range of a channel in Quarter Bridge mode. |
| Full Bridge Range | Sets the range of a channel in Full Bridge mode. |
| Digital Threshold | Sets the threshold of a channel in Digital In mode. |

#### Module Properties

To access the following module properties for this
 device, use the FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Select High Speed, Best 60 Hz Rejection, Best 50 Hz Rejection, or High Resolution. Refer to the NI 9219 Specifications for more information about the conversion times. This property overwrites the value configured in the C Series Module Properties dialog box. |
| Module ID | Returns the module ID, 0x730C. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Excitation Protection

The NI 9219 excitation circuit is protected from
 overcurrent and overvoltage fault conditions. The circuit is automatically disabled
 in the event of a fault condition. Whenever possible, a channel automatically
 recovers after the fault is removed.

error 65654

error 65548

- If a warning occurs, only the channel(s) with the fault are affected and all
 other channels on the module continue to function properly without
 interruption.
- If an error occurs, the module is unable to recover from the fault
 condition and you must restart the module after the fault is removed.

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9219

Related information:

- NI-9219 Specifications

<!--NI_TOPIC bundle=ni-compactrio path=ni-9219-scan-interface.html language=enus -->
## TOPIC 00212: NI 9219 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9219-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9219-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data or Boolean data in units determined by the measurement mode you select on the

### NI 9219 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables for
 the channels return calibrated floating-point data or Boolean data in units
 determined by the measurement mode you select on the C Series Module
 Properties dialog box. The following table shows the units for the
 different modes.

| Mode | Data Units |
| --- | --- |
| Voltage | Volts |
| Current | Amps |
| Resistance | Ohms |
| Thermocouple | Volts or Temperature Units |
| RTD | Ohms or Temperature Units |
| Bridge | Volts/Volt |
| Digital In | Boolean |
| Open Contact | Boolean |

Note

#### Module Channels

The NI 9219 has the
 following channels.

| Channel | Description |
| --- | --- |
| CHx | Analog input channel x, where x is the number of the channel. For the NI 9219, x is 0 to 3. |

#### C Series Module Properties Dialog Box

Use this dialog box to configure the NI 9219. Right-click the NI 9219 in
 the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 configure settings.
- Mode —Specifies the measurement mode for the selected
 channel(s).
- Range —Specifies the range for the selected
 channel(s).
- Thermocouple Type —Specifies the type of thermocouple
 connected to a channel in thermocouple mode.
- Measurement Units —Specifies the units for data to be
 returned from the selected channel(s) configured for thermocouple or RTD
 mode.
- RTD Type —Specifies the type of RTD connected to the
 channel by temperature coefficient of resistance (TCR). If you select
 Custom , enter the Callendar-Van
 Dusen Coefficients below.
  - Callendar-Van Dusen Coefficients —Specifies the
 coefficients to use in the Callendar-Van Dusen equation, a linearization
 curve for measuring the temperature of an RTD.
- Threshold —Specifies the minimum high level in volts for the
 selected channel(s) configured for Digital In mode. The range of valid threshold
 values is 0 to 60.
- Conversion Time —Determines the time it takes to read all
 channels of the module. Select High Speed ,
 Best 60 Hz Rejection , Best 50 Hz
 Rejection , or High Resolution . Refer to
 the NI 9219 hardware documentation on ni.com/manuals for more information about
 these conversion times.

Parent topic:

NI 9219

<!--NI_TOPIC bundle=ni-compactrio path=ni-9219.html language=enus -->
## TOPIC 00213: NI 9219

- bundle_id: `ni-compactrio`
- source_path: `ni-9219.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9219.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 24-Bit Universal Analog Input Module NI 9219 Pinout 43 NI 9219 Pinout 168 Signal Descriptions Terminal Signal Name Signal Description 1 T+ TEDS Data 2 T- TEDS COM 3 EX+/HI^1 Positive excitation or input signal 4 HI Positive input signal 5 EX-/LO^1 Negative excitation or input s

### NI 9219

CompactRIO 4-Channel, 24-Bit Universal Analog Input Module

#### NI 9219 Pinout

Figure 43.

[IMAGE alt='image' src='GUID-8C002DAE-17BF-456E-AE7B-24DCA4DC74A1-a5.svg']

| Terminal | Signal Name | Signal Description |
| --- | --- | --- |
| 1 | T+ | TEDS Data |
| 2 | T- | TEDS COM |
| 3 | EX+/HI1 | Positive excitation or input signal |
| 4 | HI | Positive input signal |
| 5 | EX-/LO1 | Negative excitation or input signal |
| 6 | LO | Negative input signal |
| 1 Depending on the mode, terminals 3 and 5 are either the excitation or input signals. |  |  |

| Mode | Terminal |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| Voltage | T+ | T- | — | HI | LO | — |
| Current | T+ | T- | HI | — | LO | — |
| 4-Wire Resistance | T+ | T- | EX+ | HI | EX- | LO |
| 2-Wire Resistance | T+ | T- | HI | — | LO | — |
| Thermocouple | T+ | T- | — | HI | LO | — |
| 4-Wire RTD | T+ | T- | EX+ | HI | EX- | LO |
| 3-Wire RTD | T+ | T- | EX+ | — | EX- | LO |
| Quarter-Bridge | T+ | T- | HI | — | LO | — |
| Half-Bridge | T+ | T- | EX+ | HI | EX- | — |
| Full-Bridge | T+ | T- | EX+ | HI | EX- | LO |
| Digital In | T+ | T- | — | HI | LO | — |
| Contact | T+ | T- | HI | — | LO | — |

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9220-fpga-interface.html language=enus -->
## TOPIC 00214: NI 9220 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9220-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9220-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9220. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). User-Controlled I/O Sampling You can use the following User-

### NI 9220 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

#### User-Controlled I/O Sampling

You can use
 the following User-Controlled I/O Sampling functions to perform
 I/O with more specific control over the I/O hardware on the FPGA.

| Function | Type |
| --- | --- |
| Generate I/O Sample Pulse Method | Module function |
| Get I/O Read Status Method | I/O function |
| Read I/O Method | I/O function |
| Reset I/O Method | Module function |

Note

Reset I/O

#### Terminals in Software

Use the FPGA I/O Node or User-Controlled I/O
 Sampling functions to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9220 has AI channels 0 to 15. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any
 methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in nV/LSB for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x7757. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9220

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9220-scan-interface.html language=enus -->
## TOPIC 00215: NI 9220 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9220-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9220-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9220 has the following channels. 179 Module

### NI 9220 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9220 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9220 has AI channels 0 to 15. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9220

<!--NI_TOPIC bundle=ni-compactrio path=ni-9220.html language=enus -->
## TOPIC 00216: NI 9220

- bundle_id: `ni-compactrio`
- source_path: `ni-9220.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9220.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 16-Channel, ±10 V, 16-Bit Simultaneous Analog Input Module NI 9220 Pinout 44 NI 9220 Pinout

### NI 9220

CompactRIO 16-Channel, ±10 V, 16-Bit Simultaneous Analog Input Module

#### NI 9220 Pinout

Figure 44.

[IMAGE alt='image' src='GUID-7BA1BD21-CC2F-4846-B398-B915883ABDF9-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9221-fpga-interface.html language=enus -->
## TOPIC 00217: NI 9221 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9221-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9221-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 180 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9221 has AI

### NI 9221 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9221 has AI channels 0 to 7. |

You can configure the minimum time between conversions.

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any
 methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in nV/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x70A5. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9221

<!--NI_TOPIC bundle=ni-compactrio path=ni-9221-scan-interface.html language=enus -->
## TOPIC 00218: NI 9221 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9221-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9221-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9221 has the following channels. 185 Module

### NI 9221 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9221 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9221 has AI channels 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9221

<!--NI_TOPIC bundle=ni-compactrio path=ni-9221.html language=enus -->
## TOPIC 00219: NI 9221

- bundle_id: `ni-compactrio`
- source_path: `ni-9221.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9221.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±60 V, 12-Bit Analog Input Module NI 9221 Pinout 45 NI 9221 Pinout

### NI 9221

CompactRIO 8-Channel, ±60 V, 12-Bit Analog Input Module

#### NI 9221 Pinout

Figure 45.

[IMAGE alt='image' src='GUID-ECD491D1-C7ED-417D-9A4E-17E734622F8C-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9222-fpga-interface.html language=enus -->
## TOPIC 00220: NI 9222 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9222-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9222-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9222. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). User-Controlled I/O Sampling You can use the following User-

### NI 9222 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading From or
 Writing to Multiple CompactRIO Channels (FPGA
 Interface)

#### User-Controlled I/O Sampling

You can use the following
 User-Controlled I/O Sampling functions to perform I/O with
 more specific control over the I/O hardware on the FPGA.

| Function | Type |
| --- | --- |
| Generate I/O Sample Pulse method | Module function |
| Get I/O Read Status method | I/O function |
| Read I/O method | I/O function |
| Reset I/O method | Module function |

Note

Reset I/O

#### Terminals in Software

Use the FPGA I/O Node or User-Controlled I/O
 Sampling functions to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9222 has AI channels 0 to 3. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in nV/LSB for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x7445. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9222

Related concepts:

- Reading from C Series Channels
- Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9222-scan-interface.html language=enus -->
## TOPIC 00221: NI 9222 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9222-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9222-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9222 has the following channels. 190 Module

### NI 9222 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9222 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9222 has AI channels 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9222

<!--NI_TOPIC bundle=ni-compactrio path=ni-9222.html language=enus -->
## TOPIC 00222: NI 9222

- bundle_id: `ni-compactrio`
- source_path: `ni-9222.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9222.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous, Channel-to-Channel Isolated Analog Input Module NI 9222 Pinout 46 NI 9222 Pinout NI-9222 Pinouts

### NI 9222

CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous, Channel-to-Channel Isolated Analog Input Module

#### NI 9222 Pinout

Figure 46.

[IMAGE alt='NI-9222 Pinouts' src='GUID-A513F836-0E9D-4BB4-B551-7D52B84E88D2-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9223-fpga-interface.html language=enus -->
## TOPIC 00223: NI 9223 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9223-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9223-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9222. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). User-Controlled I/O Sampling You can use the following User-

### NI 9223 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading
 From or Writing to Multiple CompactRIO Channels (FPGA
 Interface)

#### User-Controlled I/O Sampling

You can use the following
 User-Controlled I/O Sampling functions to perform I/O with
 more specific control over the I/O hardware on the FPGA.

| Function | Type |
| --- | --- |
| Generate I/O Sample Pulse method | Module function |
| Get I/O Read Status method | I/O function |
| Read I/O method | I/O function |
| Reset I/O method | Module function |

Note

Reset I/O

#### Terminals in Software

Use the FPGA I/O Node or User-Controlled I/O
 Sampling functions to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9223 has AI channels 0 to 3. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in nV/LSB for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate NI 9220 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x74EC. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9223

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9223-scan-interface.html language=enus -->
## TOPIC 00224: NI 9223 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9223-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9223-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9223 has the following channels. 195 Module

### NI 9223 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9223 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9223 has AI channels 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9223

<!--NI_TOPIC bundle=ni-compactrio path=ni-9223.html language=enus -->
## TOPIC 00225: NI 9223

- bundle_id: `ni-compactrio`
- source_path: `ni-9223.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9223.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous, Channel-to-Channel Isolated Analog Input Module NI 9223 Pinout 47 NI 9223 Pinout NI-9223 Pinouts

### NI 9223

CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous, Channel-to-Channel Isolated Analog Input Module

#### NI 9223 Pinout

Figure 47.

[IMAGE alt='NI-9223 Pinouts' src='GUID-A513F836-0E9D-4BB4-B551-7D52B84E88D2-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9224-fpga-interface.html language=enus -->
## TOPIC 00226: NI 9224 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9224-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9224-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 196 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9224 has AI

### NI 9224 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9224 has AI channels 0 to 7. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Select High Speed, Best 60 Hz Rejection, Best 50 Hz Rejection, or High Resolution. This property overwrites the value configured in the C Series Module Properties dialog box. Returns the conversion time setting when configured to read. |
| Module ID | Returns the module ID, 0x780D. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9224

<!--NI_TOPIC bundle=ni-compactrio path=ni-9224-scan-interface.html language=enus -->
## TOPIC 00227: NI 9224 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9224-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9224-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. Module C

### NI 9224 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

#### Module Channels

The NI 9224 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9224 has AI channels 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Determines the time it takes to acquire one
 point of data from one or more channels. Select Medium Speed ,
 High Speed , Medium Resolution , or
 High Resolution . Refer to the NI 9224 hardware
 documentation for more information about the conversion times.

Parent topic:

NI 9224

<!--NI_TOPIC bundle=ni-compactrio path=ni-9224.html language=enus -->
## TOPIC 00228: NI 9224

- bundle_id: `ni-compactrio`
- source_path: `ni-9224.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9224.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±10V 24-Bit Simultaneous Analog Input Module NI 9224 Pinout 48 NI 9224 Pinout

### NI 9224

CompactRIO 8-Channel, ±10V 24-Bit Simultaneous Analog Input Module

#### NI 9224 Pinout

Figure 48.

[IMAGE alt='image' src='GUID-8EC9BAFC-CAAA-4F72-BEE7-8AD0989B79EA-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9225-fpga-interface.html language=enus -->
## TOPIC 00229: NI 9225 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9225-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9225-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9225. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). Terminals in Software 199 Terminals in Software Terminal Des

### NI 9225 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading
 From or Writing to Multiple CompactRIO Channels (FPGA
 Interface)

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9225 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9225 to access this channel. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, you must write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

Note

Getting Started

labview\examples\CompactRIO\Module Specific\NI 9225\NI 9225
 Getting Started\NI 9225 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in μV for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID, 0x7383. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock channel in
 the single-cycle Timed Loop. You cannot use the other channels on the NI 9225 with
 the single-cycle Timed Loop. Refer to *Understanding Loop Timing (FPGA
 Interface)* for information about loop timing for this
 module.

Parent topic:

NI 9225

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)
- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9225-scan-interface.html language=enus -->
## TOPIC 00230: NI 9225 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9225-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9225-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9225 has the following channels. 202 Module

### NI 9225 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9225 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9225, x 0 to 2. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9225

<!--NI_TOPIC bundle=ni-compactrio path=ni-9225.html language=enus -->
## TOPIC 00231: NI 9225

- bundle_id: `ni-compactrio`
- source_path: `ni-9225.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9225.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 3-Channel, 300 V[rms], 24-Bit Simultaneous Analog Input Module NI 9225 Pinout NI-9225 Pinouts

### NI 9225

CompactRIO 3-Channel, 300 V<sub>rms</sub>, 24-Bit Simultaneous Analog Input Module

#### NI 9225 Pinout

[IMAGE alt='NI-9225 Pinouts' src='GUID-A00A5B3C-63FB-431E-A8F8-4F7F7BC2044D-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9226-fpga-interface.html language=enus -->
## TOPIC 00232: NI 9226 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9226-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9226-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareTo access the following terminals for this device, use the FPGA I/O Node. 203 Terminals in Software Terminal Description RTDx RTD input channel x, where x is the number of the channel. The NI 9226 has RTD

### NI 9226 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device,
 use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| RTDx | RTD input channel x, where x is the number of the channel. The NI 9226 has RTD channels 0 to 7. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pΩ/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in µΩ for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time in milliseconds it takes to acquire conversion data. This property overwrites the value you configure in the C Series Module Properties dialog box. |
| Module ID | Returns the module ID, 0x77C8 (NI 9226 with spring terminal) or 0x77E0 (NI 9226 with DSUB). |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9226

Related concepts:

- Reading from C Series Channels
- Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9226-scan-interface.html language=enus -->
## TOPIC 00233: NI 9226 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9226-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9226-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. Module C

### NI 9226 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

#### Module Channels

The NI 9226 has the following channels.

| Channel | Description |
| --- | --- |
| RTDx | RTD input channel x, where x is the number of the channel. The NI 9226 has RTD channels 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Specifies the time it takes to acquire one
 point of data from all channels. Select 200 ms or 2.5
 ms .
- Channels —Specifies the channel(s) for which you want to
 configure settings.
- Measurement Units —Specifies the units you want data to be
 returned in for the channel. You can select Raw Ohms ,
 Degrees Kelvin , Degrees Celsius ,
 Degrees Fahrenheit , or Degrees
 Rankine .
- RTD Type —Specifies the type of RTD connected to the channel by
 temperature coefficient of resistance (TCR). If you select
 Custom , enter the Callendar-Van Dusen
 Coefficients below.
  - Callendar-Van Dusen Coefficients —Specifies the
 coefficients to use in the Callendar-Van Dusen equation. the
 Callendar-Van Dusen equation is a linearization curve for measuring the
 temperature of an RTD.

Parent topic:

NI 9226

<!--NI_TOPIC bundle=ni-compactrio path=ni-9226.html language=enus -->
## TOPIC 00234: NI 9226

- bundle_id: `ni-compactrio`
- source_path: `ni-9226.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9226.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 24-Bit, 1000 Ω RTD Analog Input Module NI 9226 Pinout 49 NI 9226 Pinout

### NI 9226

CompactRIO 8-Channel, 24-Bit, 1000 Ω RTD Analog Input Module

#### NI 9226 Pinout

Figure 49.

[IMAGE alt='image' src='GUID-FEAAA884-628A-4AA6-B622-63B2D1167D53-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9227-fpga-interface.html language=enus -->
## TOPIC 00235: NI 9227 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9227-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9227-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9227. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). Terminals in Software 207 Terminals in Software Terminal Des

### NI 9227 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading
 From or Writing to Multiple CompactRIO Channels (FPGA
 Interface)

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9227 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9227 to access this channel. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

Note

Getting Started

labview\examples\CompactRIO\Module Specific\NI 9227\NI 9227 Getting Started\NI
 9227 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pA/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nA for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID, 0x7416. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock channel in
 the single-cycle Timed Loop. You cannot use the other channels on the NI 9227 with
 the single-cycle Timed Loop. Refer to *Understanding Loop Timing (FPGA
 Interface)* for information about loop timing for this
 module.

Parent topic:

NI 9227

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9227-scan-interface.html language=enus -->
## TOPIC 00236: NI 9227 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9227-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9227-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in amps. Module Channels The NI 9227 has the following channels. 210 Module

### NI 9227 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in amps.

#### Module Channels

The NI 9227 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9227, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9227

<!--NI_TOPIC bundle=ni-compactrio path=ni-9227.html language=enus -->
## TOPIC 00237: NI 9227

- bundle_id: `ni-compactrio`
- source_path: `ni-9227.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9227.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 5 A[rms], 24-Bit Simultaneous Analog Input Module NI 9227 Pinout 50 NI 9227 Pinout NI-9227 Pinouts

### NI 9227

CompactRIO 4-Channel, 5 A<sub>rms</sub>, 24-Bit Simultaneous Analog Input Module

#### NI 9227 Pinout

Figure 50.

[IMAGE alt='NI-9227 Pinouts' src='GUID-D17534D5-234D-4909-A0E1-A56E450ECD00-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9228-fpga-interface.html language=enus -->
## TOPIC 00238: NI 9228 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9228-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9228-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. Terminals in SoftwareTo access the following terminals for this device, use the FPGA I/O Node. 211 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9228 has A

### NI 9228 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

#### Terminals in Software

To access the following terminals for this device,
 use the FPGA I/O Node.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9228 has AI channels 0 to 7. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Conversion Time | Sets the time it takes to acquire one point of data from one or more channels in a single FPGA I/O Node. Select High Speed (1k S/s), Medium Speed (100 S/s), Medium Resolution (50/60Hz rejection – 12 S/s), or High Resolution (50/60Hz rejection – 2 S/s). This property overwrites the value configured in the C Series Module Properties dialog box. Returns the conversion time setting when configured to read. |
| Module ID | Returns the module ID, 0x780E. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9228

<!--NI_TOPIC bundle=ni-compactrio path=ni-9228-scan-interface.html language=enus -->
## TOPIC 00239: NI 9228 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9228-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9228-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in units as specified on the C Series Module Properties dialog box. Module C

### NI 9228 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in units as specified on the C Series Module
 Properties dialog box.

#### Module Channels

The NI 9228 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9228, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. Use this field to give the module a
 descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Conversion Time —Determines the time it takes to acquire one
 point of data from one or more channels. You can select Medium
 Speed , High Speed , Medium Resolution , or High Resolution . Refer to the NI 9228 hardware
 documentation for more information about the conversion times.

Parent topic:

NI 9228

<!--NI_TOPIC bundle=ni-compactrio path=ni-9228.html language=enus -->
## TOPIC 00240: NI 9228

- bundle_id: `ni-compactrio`
- source_path: `ni-9228.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9228.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±60V 24-Bit Simultaneous Analog Input Module NI 9228 Pinout 51 NI 9228 Pinout

### NI 9228

CompactRIO 8-Channel, ±60V 24-Bit Simultaneous Analog Input Module

#### NI 9228 Pinout

Figure 51.

[IMAGE alt='image' src='GUID-3951835A-05AD-4A24-9A34-A06130010714-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9229-fpga-interface.html language=enus -->
## TOPIC 00241: NI 9229 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9229-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9229-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9229. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). You also can synchronize the NI 9229 with other modules that

### NI 9229 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

Simultaneously Reading
 From or Writing to Multiple CompactRIO Channels (FPGA Interface)

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9229 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9229 to access this channel. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

Note

Getting Started

labview\examples\CompactRIO\Module Specific\NI 9229\NI 9229 Getting Started\NI
 9229 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock channel in
 the single-cycle Timed Loop. You cannot use the other channels on the NI 9229 with
 the single-cycle Timed Loop. Refer to *Understanding Loop Timing (FPGA
 Interface)* for information about loop timing for this
 module.

Parent topic:

NI 9229

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)
- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9229-scan-interface.html language=enus -->
## TOPIC 00242: NI 9229 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9229-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9229-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9229 has the following channels. 217 Module

### NI 9229 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9229 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9229, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9229

<!--NI_TOPIC bundle=ni-compactrio path=ni-9229.html language=enus -->
## TOPIC 00243: NI 9229

- bundle_id: `ni-compactrio`
- source_path: `ni-9229.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9229.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±60 V, 24-Bit Simultaneous Analog Input Module NI 9229 Pinout 52 NI 9229 Pinout NI-9229 Pinouts

### NI 9229

CompactRIO 4-Channel, ±60 V, 24-Bit Simultaneous Analog Input Module

#### NI 9229 Pinout

Figure 52.

[IMAGE alt='NI-9229 Pinouts' src='GUID-A513F836-0E9D-4BB4-B551-7D52B84E88D2-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9230-fpga-interface.html language=enus -->
## TOPIC 00244: NI 9230 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9230-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9230-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device.You can synchronize an NI 9230 with other modules that have a selectable timebase source. Terminals in Software 218 Terminals in Software Terminal Description AIx AI input channel x, where x is the number of the channel. The N

### NI 9230 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9230 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1072 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9230 to access this channel. If you do not export the onboard clock and try to access the Onboard Clock channel, LabVIEW returns a code generation error when you try to compile the FPGA VI. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

Note

Getting Started

labview\examples\CompactRIO\Module Specific\NI 9230\NI 9230 Getting Started\NI
 9230 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

To access the following method for this device, use the FPGA I/O
 Method Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was a short circuit or open loop on the channel since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Short Circuit—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected a short circuit on the channel at some point after the last time that the Check Cached Status method executed. Open Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open loop on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of three modes: AC coupled, DC coupled, or IEPE AC coupled. |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9230

<!--NI_TOPIC bundle=ni-compactrio path=ni-9230.html language=enus -->
## TOPIC 00245: NI 9230

- bundle_id: `ni-compactrio`
- source_path: `ni-9230.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9230.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 3-Channel, ±30 V, 12.8 kS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module NI 9230 Pinout 53 NI 9230 Pinout NI-9230 Pinouts

### NI 9230

CompactRIO 3-Channel, ±30 V, 12.8 kS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module

#### NI 9230 Pinout

Figure 53.

[IMAGE alt='NI-9230 Pinouts' src='GUID-2A1D74D4-9DDA-4EDE-9B1E-68EAC218DD9D-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9231-fpga-interface.html language=enus -->
## TOPIC 00246: NI 9231 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9231-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9231-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device.You can synchronize an NI 9231 with other modules that have a selectable timebase source. Terminals in Software 223 Terminals in Software Terminal Description AIx AI input channel x, where x is the number of the channel. The N

### NI 9231 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9231 has AI channels 0 to 7. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1072 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9231 to access this channel. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

To access the following method for this device, use the FPGA I/O
 Method Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was a short circuit or open loop on the channel since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Short Circuit—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected a short circuit on the channel at some point after the last time that the Check Cached Status method executed. Open Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open loop on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of three modes: AC coupled, DC coupled, or IEPE AC coupled. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9231

<!--NI_TOPIC bundle=ni-compactrio path=ni-9231.html language=enus -->
## TOPIC 00247: NI 9231

- bundle_id: `ni-compactrio`
- source_path: `ni-9231.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9231.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 8 AI, ±5 V, 24 Bit, 51.2 kS/s/ch Simultaneous, AC/DC Coupling, IEPE AC Coupling NI 9231 Pinout 54 NI 9231 Pinout

### NI 9231

8 AI, ±5 V, 24 Bit, 51.2 kS/s/ch Simultaneous, AC/DC Coupling, IEPE AC Coupling

#### NI 9231 Pinout

Figure 54.

[IMAGE alt='image' src='GUID-6F0A6696-89BA-426F-8C86-DCAA45F0EA17-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9232-fpga-interface.html language=enus -->
## TOPIC 00248: NI 9232 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9232-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9232-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device.You can synchronize an NI 9232 with other modules that have a selectable timebase source. Terminals in Software 228 Terminals in Software Terminal Description AIx AI input channel x, where x is the number of the channel. The N

### NI 9232 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for
 reading with this device.

Note

#### Terminals in Software

| Terminal | Description |
| --- | --- |
| AIx | AI input channel x, where x is the number of the channel. The NI 9232 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1072 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9232 to access this channel. If you do not export the onboard clock and try to access the Onboard Clock channel, LabVIEW returns a code generation error when you try to compile the FPGA VI. |
| Start | Channel that controls when the module starts acquiring data. To acquire data, write TRUE to the Start channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. No operation is performed when writing FALSE to the Start channel. |
| Stop | Channel that controls when the module stops acquiring data. To stop acquiring data, write TRUE to the Stop channel. When the module is acquiring data, write TRUE to the Stop channel before you can access properties for the module. No operation is performed when writing FALSE to the Stop channel. |

Note

Getting Started

labview\examples\CompactRIO\Module Specific\NI 9232\NI 9232 Getting Started\NI
 9232 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

To access the following method for this device, use the FPGA I/O
 Method Node.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was a short circuit or open loop on the channel since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Short Circuit—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected a short circuit on the channel at some point after the last time that the Check Cached Status method executed. Open Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an open loop on the channel at some point after the last time that the Check Cached Status method executed. |

#### I/O
 Properties

To access the following I/O properties for this device, use the
 FPGA I/O Property Node.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of three modes: AC coupled, DC coupled, or IEPE AC coupled. |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the module acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9232

<!--NI_TOPIC bundle=ni-compactrio path=ni-9232.html language=enus -->
## TOPIC 00249: NI 9232

- bundle_id: `ni-compactrio`
- source_path: `ni-9232.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9232.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 3-Channel, ±30 V, 102.4 kS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module NI 9232 Pinout 55 NI 9232 Pinout NI-9232 Pinouts

### NI 9232

CompactRIO 3-Channel, ±30 V, 102.4 kS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module

#### NI 9232 Pinout

Figure 55.

[IMAGE alt='NI-9232 Pinouts' src='GUID-2A1D74D4-9DDA-4EDE-9B1E-68EAC218DD9D-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9234-fpga-interface.html language=enus -->
## TOPIC 00250: NI 9234 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9234-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9234-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9234 with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 233 Terminals in Software Terminal De

### NI 9234 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9234 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | 13.1072 MHz internal clock of the NI 9234. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the onboard clock of the NI 9234 to access this channel. If you do not export the onboard clock, when you try to access the Onboard Clock channel, LabVIEW returns a code generation error when you compile the FPGA VI. |
| Start | Channel that controls when the NI 9234 starts acquiring data. If TRUE is written to the Start channel, the NI 9234 starts acquiring data. When the NI 9234 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9234 stops acquiring data. If TRUE is written to the Stop channel, the NI 9234 stops acquiring data. When the NI 9234 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module Specific\NI 9234\NI 9234 Getting
 Started\NI 9234 Getting Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any
 methods.

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following I/O properties for this device.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of three modes: AC coupled, DC coupled, or IEPE AC coupled. |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate NI 9234 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert and calibrate NI 9234 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9234 acquires data. |
| Module ID | Returns the module ID, 0x72B5. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9234 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9234

Related concepts:

- Understanding Loop Timing (FPGA Interface)
