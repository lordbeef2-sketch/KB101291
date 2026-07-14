# NI DOCUMENT BUNDLE: ni-industrial-communications-ethercat

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-ethercat start=1 end=48 -->
<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=accessing-a-parameter.html language=enus -->
## TOPIC 00001: Accessing a Parameter

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `accessing-a-parameter.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/accessing-a-parameter.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: A complex EtherCAT SubDevice has an object dictionary containing the parameters for the device-specific configuration use. You can access an EtherCAT SubDevice parameter in the following ways: Read the parameter on the EtherCAT:Parameters page of the Online Slave Device State dialog box. You can rea

### Accessing a Parameter

A complex EtherCAT SubDevice has an
 object dictionary containing the parameters for the device-specific
 configuration use. You can access an EtherCAT SubDevice parameter in
 the following ways:

- Read the parameter on the
 EtherCAT:Parameters page of the
 Online Slave Device State
 dialog box. You can read the parameter value in the online
 SubDevice.
- Configure the initial commands on the
 EtherCAT:Advanced:Initial Commands
 Property page of the EtherCAT
 Slave Device Properties dialog box. With
 these commands, you can set some SubDevice
 parameters during the mode transition.
- Use a Property node to read
 SubDevice parameter values by wiring a
 SubDevice reference to the node.

Parent topic:

Configuring the EtherCAT Network

Related tasks:

- Reading and Writing Properties at Run Time

Related information:

- EtherCAT:Parameters
- Online Device State Dialog Box
- EtherCAT:Advanced:Initial Commands Property Page
- EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=adding-editing-or-removing-an-ethercat-module.html language=enus -->
## TOPIC 00002: Adding, Editing, or Removing an EtherCAT Module

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `adding-editing-or-removing-an-ethercat-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/adding-editing-or-removing-an-ethercat-module.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some powerful EtherCAT SubDevices from NI and other vendors have multiple modules for flexible usages. NI-Industrial Communications for EtherCAT supports Modular Device Profiles since version 2.2. You must import a device profile before loading the profile in a LabVIEW Project. Adding an Online Ethe

### Adding, Editing, or Removing an EtherCAT Module

Some powerful EtherCAT SubDevices from NI and other vendors have multiple modules for
 flexible usages.

Note

#### Adding an Online EtherCAT
 Module

Complete the following steps to add a module after connecting the module to the
 SubDevice:

1. Right-click the SubDevice item in the LabVIEW Project
 Explorer and select New»Targets and Devices to display the Add Targets and Devices 
 dialog box.
2. Select Existing Target or Device and expand the
 EtherCAT Module category to discover available
 EtherCAT modules.
3. Select an EtherCAT module and click OK .

Tip

#### Adding an Offline EtherCAT
 Module

Follow these steps to add a module that is not connected to a physical
 SubDevice:

1. Right-click the SubDevice item in the LabVIEW Project Explorer and
 select New»Targets and Devices to display the
 Add Targets and Devices dialog box.
2. Select New Target or Device and expand the
 EtherCAT Module category.
3. Select the EtherCAT module type and click OK .
4. Select C Series Module and click
 OK to display the C Series
 Module dialog box.
5. Select the proper settings and click OK . Click
 Help in the dialog box for more information.

#### Editing an EtherCAT Module

To edit an EtherCAT module item, right-click the module item in the LabVIEW Project
 Explorer and select Properties to display the *C Series
 Module Properties* dialog box.

Note

C
 Series Module Properties

#### Removing an EtherCAT Module

To remove an EtherCAT module item, right-click the module item in the LabVIEW
 Project Explorer and select Remove from
 Project.

Parent topic:

Configuring the EtherCAT Network

Related information:

- LabVIEW Project Items
- Import Device Profile Box
- C Series Module Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=adding-editing-or-removing-an-ethercat-slave.html language=enus -->
## TOPIC 00003: Adding, Editing, or Removing an EtherCAT SubDevice

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `adding-editing-or-removing-an-ethercat-slave.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/adding-editing-or-removing-an-ethercat-slave.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adding an Online EtherCAT SubDevice Complete the following steps to add a SubDevice after you connect a SubDevice to the EtherCAT Ethernet adapter of a controller. Right-click the MainDevice item in the LabVIEW Project Explorer and select New Targets and Devices to display the Add Targets and Device

### Adding, Editing, or Removing an EtherCAT
 SubDevice

#### Adding an Online EtherCAT
 SubDevice

Complete the following steps to add a SubDevice after you connect a
 SubDevice to the EtherCAT Ethernet adapter of a controller.

1. Right-click the MainDevice item in the LabVIEW Project
 Explorer and select New»Targets and Devices to display the Add Targets and Devices 
 dialog box.
2. Select Existing Target or Device and expand the
 EtherCAT Device category to discover the available
 EtherCAT SubDevices.
3. Select an EtherCAT device and click OK .
4. (Optional) For the NI-9145, if you have programmed the FPGA, a
 Discover dialog box appears. Click
 Discover to add an FPGA target, C Series modules that
 operate in FPGA mode, and user-defined variables. You also can select the
 Do Not Discover option to skip this operation.

Attention

#### Adding an Offline EtherCAT
 SubDevice

Complete the following steps to add a SubDevice that is not connected to a
 physical MainDevice.

1. Right-click the MainDevice item in the LabVIEW Project Explorer and select New»Targets and Devices to display the Add Targets and Devices 
 dialog box.
2. Select New Target or Device and expand the
 EtherCAT Device category.
3. Select the EtherCAT SubDevice type and click
 OK .

#### Editing an EtherCAT
 SubDevice

To edit an EtherCAT SubDevice item, right-click the SubDevice item in
 the LabVIEW Project Explorer and select
 Properties to display the EtherCAT Slave Device
 Properties dialog box.

#### Removing an EtherCAT
 SubDevice

To remove an EtherCAT SubDevice item, right-click the SubDevice item
 in the LabVIEW Project Explorer and select Remove
 from Project.

Parent topic:

Configuring the EtherCAT Network

Related tasks:

- Configuring the Ethernet Adapter

Related reference:

- NI-Industrial Communications for EtherCAT 2025 Q4 Changes

Related information:

- LabVIEW Project Items
- EtherCAT Slave Device Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=adding-editing-or-removing-ethercat-masters.html language=enus -->
## TOPIC 00004: Adding, Editing, or Removing EtherCAT MainDevices

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `adding-editing-or-removing-ethercat-masters.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/adding-editing-or-removing-ethercat-masters.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adding an Online EtherCAT MainDevice Complete the following steps to add a MainDevice if your computer can access the controller through Ethernet: Right-click the controller item in the LabVIEW Project Explorer and select New Targets and Devices to display the Add Targets and Devices dialog box. Sel

### Adding, Editing, or Removing EtherCAT
 MainDevices

#### Adding an Online EtherCAT
 MainDevice

Complete the following steps to add a MainDevice if your computer can access the
 controller through Ethernet:

1. Right-click the controller item in the LabVIEW Project
 Explorer and select New»Targets and Devices to display the Add Targets and Devices 
 dialog box.
2. Select Existing Target or Device and expand the
 EtherCAT Master Device category to discover the
 available EtherCAT Ethernet adapters. If no adapter is available, be sure to
 configure an EtherCAT Ethernet adapter.
3. Select an available EtherCAT Ethernet adapter and click
 OK to add the MainDevice and SubDevices
 automatically.
4. (Optional) For the NI-9145, if you have programmed the FPGA, a
 Discover dialog box appears. Click
 Discover to add an FPGA target, C Series modules that
 operate in FPGA mode, and user-defined variables. You also can select the
 Do Not Discover option to skip this operation.

Attention

#### Adding an Offline EtherCAT
 MainDevice

Complete the following steps to add a MainDevice that is not connected to a physical
 real-time controller:

1. Right-click the controller item in the LabVIEW Project
 Explorer and select New»Targets and Devices to display the Add Targets and Devices 
 dialog box.
2. Select New Target or Device and expand the
 EtherCAT Device category.
3. Select the Offline EtherCAT Master EtherCAT MainDevice
 type and click OK .

Note

Tip

1. Right-click the MainDevice item and select the
 Properties menu to display the
 EtherCAT Master Properties dialog box.
2. On the General property page, change the physical adapter from
 Offline Adapter to a physical adapter with a MAC
 address that is not 00-00-00-00-00-00 .

#### Editing an EtherCAT
 MainDevice

To edit an EtherCAT MainDevice item, right-click the MainDevice item in the LabVIEW
 Project Explorer and select
 Properties to display the EtherCAT Master
 Properties dialog box.

#### Removing an EtherCAT MainDevice

To remove an EtherCAT MainDevice item, right-click the MainDevice item in the LabVIEW
 Project Explorer and select Remove from
 Project.

Parent topic:

Configuring the EtherCAT Network

Related tasks:

- Configuring the Ethernet Adapter

Related information:

- LabVIEW Project Items
- EtherCAT Master Properties Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=cable-redundancy.html language=enus -->
## TOPIC 00005: Cable Redundancy

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `cable-redundancy.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/cable-redundancy.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: In cable redundancy mode, a second redundant EtherCAT adapter is used in addition to the primary EtherCAT adapter. The OUT port of the last SubDevice in the chain is connected to the redundant adapter on the same target to create two circular links. EtherCAT telegrams are sent simultaneously from bo

### Cable Redundancy

Figure 2.

[IMAGE alt='Normal mode vs. cable redundancy mode EtherCAT networks, showing device behavior after a cable break.' src='GUID-0B493998-ADC1-4127-A425-1869AB6EFAFD-a5.png']

Parent topic:

Configuring the EtherCAT Network

#### Configuring the Hardware for Cable
 Redundancy

Two Ethernet adapters are dedicated to EtherCAT. Complete the following steps to configure
 the hardware for cable redundancy.

1. Plug two Ethernet adapters on a real-time target.
2. Configure both adapters for EtherCAT use in MAX.
3. Connect the IN port of the first SubDevice in the chain
 to one adapter.
4. Connect the OUT port of the last SubDevice in the chain
 to the other adapter.

#### Using Cable Redundancy Mode

- Enable the cable redundancy mode. 
 After setting up the hardware, use the Refresh Modules VI to enable
 cable redundancy automatically and discover devices. Use the EtherCAT MainDevice
 properties Cable Redundacy.Enable and Cable
 Redundancy.Redundancy Master ID to check whether the cable redundancy mode is
 enabled on the MainDevice. Use the properties to verify if the redundant adapter is
 associated with the MainDevice. Note Enabling the cable redundancy mode automatically disables the
 Logical Read Write (LRW) when possible.
- Disable the cable redundancy mode. 
 To disable the cable redundancy mode, unplug the cable that is connected to the
 redundant adapter and call the Refresh Modules VI again.
- Detect broken cables. 
 When a cable is broken while reading/writing I/O variables, LabVIEW reports a warning.
 The warning indicates that a cable is broken and the values of I/O variables are still
 valid. To detect broken connections, use the EtherCAT SubDevice method
 GetPortLinkStatus.
- Manage distributed clocks. 
 In cable redundancy mode, if you enable distributed clocks for SubDevices, the
 target time distributes to the SubDevice. Synchronize the SubDevices that
 enable distributed clock by using SYNC0 in the SafeOP state or the
 OP state. If one of the cables disconnects in the network, the primary MainDevice keeps
 distributing the time to the SubDevices. The SubDevices that connect to
 the primary MainDevice synchronize. The SubDevices that connect to the redundant
 MainDevice might run out of sync after a certain period of time.

Related information:

- Cable Master Properties
- GetPortLinkStatus

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=changing-the-scan-period.html language=enus -->
## TOPIC 00006: Changing the Scan Period

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `changing-the-scan-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/changing-the-scan-period.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: You must set the scan period to less than or equal to 10 ms. Otherwise, EtherCAT experiences serious performance degradation. The EtherCAT scan period is the same as the scan period in the target NI Scan Engine. The NI Scan Engine executes at regular intervals determined by the scan period. To chang

### Changing the Scan Period

Note

The EtherCAT scan period is the same as the scan period in the target NI Scan Engine. The NI Scan
 Engine executes at regular intervals determined by the scan period.

To change the scan period, complete the following steps.

1. Right-click the controller item and select Utilities»Scan Engine Mode»Switch to Configuration.
2. Right-click the controller item and select Properties to display the Real-Time CompactRIO/PXI Properties dialog box.
3. On the Scan Engine property page, change the
 Scan Period.
4. Right-click the controller item and select Utilities»Scan Engine Mode»Switch to Active.
5. Right-click the EtherCAT MainDevice item and select
 Deploy.

Parent topic:

Configuring the EtherCAT Network

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=comparing-the-ethercat-configurations.html language=enus -->
## TOPIC 00007: Comparing the EtherCAT Configurations

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `comparing-the-ethercat-configurations.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/comparing-the-ethercat-configurations.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to compare the EtherCAT network configuration in the LabVIEW project with the one on the real-time controller: Right-click the controller item in the LabVIEW Project Explorer and select Utilities»Compare Project & System to display the Project & System Comparison dialog

### Comparing the EtherCAT Configurations

Complete the following steps to compare the EtherCAT network configuration in the LabVIEW project
 with the one on the real-time controller:

1. Right-click the controller item in the LabVIEW Project Explorer and select Utilities»Compare Project & System to display the Project & System Comparison dialog box.
2. Compare the differences between the related EtherCAT items.

If an item icon has a red overlay on the top right side, the item settings in the project differ from the settings in the real-time controller due to the following reasons:

- The real-time controller is undeployed. You can deploy the items to the controller.
- Your project is empty. You can upload the EtherCAT items from the controller to the project.
- Some obsolete EtherCAT SubDevice settings are on the controller. You can undeploy these
 items from the controller.
- The same items are in the project and controller, but settings such as name or properties are different. You can either deploy the project settings or upload the controller settings.

#### Deploying EtherCAT Items

Complete the following steps to deploy the EtherCAT items.

1. Select the EtherCAT items in the Project window and click
 Deploy to mark the items as
 Deploy .
2. Click Apply .

#### Uploading EtherCAT Items

Complete the following steps to upload the EtherCAT items.

1. Select the EtherCAT items in the System window and click
 Upload to mark the items as
 Upload .
2. Click Apply .

#### Undeploying EtherCAT Items

Complete the following steps to undeploy the EtherCAT items.

1. Select the EtherCAT items in the System window and click
 Undeploy to mark the items as
 Undeploy .
2. Click Apply .

Parent topic:

Configuring the EtherCAT Network

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=compiling-downloading-and-running-an-fpga-vi.html language=enus -->
## TOPIC 00008: Compiling, Downloading, and Running an FPGA VI

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `compiling-downloading-and-running-an-fpga-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/compiling-downloading-and-running-an-fpga-vi.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: You must compile an FPGA VI before you can download and run the FPGA VI on the FPGA target. Before downloading an FPGA VI to the FPGA target on the NI-9145, ensure that you deploy the NI-9145 item. Also ensure that you switch the NI Scan Engine to Configuration Mode. You can compile and download F

### Compiling, Downloading, and Running an FPGA VI

You must compile an FPGA VI before you can download and run the FPGA VI on the FPGA target.

Note

You can compile and download FPGA VIs in the following ways:

- Click the Run button on the front panel or block diagram. LabVIEW compiles the FPGA VI and downloads the bitfile to the FPGA target automatically after the compile completes. LabVIEW does not compile the FPGA VI if you have already compiled the VI. LabVIEW does not download the FPGA VI if the VI is already on the FPGA target.
- Right-click the FPGA VI in the Project Explorer window and
 select Create Build Specification from the shortcut menu.
 LabVIEW generates a build specification item with the same name of the FPGA VI
 under the Build Specification container in the
 Project Explorer.
- Right-click the generated build specification and select Build to Compile the FPGA VI. If there are no updates on the FPGA VI since the last compile, LabVIEW does not recompile the VI unless you force LabVIEW to compile the VI by right-clicking the build specification, and selecting Rebuild.

After compilation, right-click the build specification and select Download to download the bitfile. LabVIEW does not download the FPGA VI if you have already downloaded the VI.

NI-9145 Online State Panel

1. Right-click the NI-9145 item in the Project Explorer 
 and select Online Device State .
2. In the EtherCAT:Online:State page, change the device
 state to Bootstrap and click the Download
 Firmware button.
3. In the Download Firmware dialog box, navigate to the
 bitfile and click Download .

After successfully downloading the bitfile to the FPGA target on the NI-9145, the VI begins
 executing.

Tip

Parent topic:

Programming the FPGA on the NI-9145

Related tasks:

- Deploying or Undeploying an EtherCAT Configuration
- NI Scan Engine Mode Transition
- Creating and Discovering the FPGA Target and Module

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=configuring-an-ni-industrial-communications-f.html language=enus -->
## TOPIC 00009: Configuring the EtherCAT Network

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `configuring-an-ni-industrial-communications-f.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/configuring-an-ni-industrial-communications-f.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following sections for more information about configuring the EtherCAT network.

### Configuring the EtherCAT Network

Refer to the following sections for more information about configuring the EtherCAT network.

- [Cable Redundancy](cable-redundancy.html#GUID-1280516B-482D-40EA-BB75-A9DD3D0E90E6)
- [Adding, Editing, or Removing EtherCAT MainDevices](adding-editing-or-removing-ethercat-masters.html)
- [Adding, Editing, or Removing an EtherCAT SubDevice](adding-editing-or-removing-an-ethercat-slave.html)
- [Adding, Editing, or Removing an EtherCAT Module](adding-editing-or-removing-an-ethercat-module.html)
- [Discovering EtherCAT Devices Programmatically](discovering-ethercat-devices-programmatically.html)
- [Changing the Scan Period](changing-the-scan-period.html)
- [Deploying or Undeploying an EtherCAT Configuration](deploying-or-undeploying-an-ethercat-configur.html)
- [Uploading an EtherCAT Configuration](uploading-an-ethercat-configuration.html)
- [Comparing the EtherCAT Configurations](comparing-the-ethercat-configurations.html)
- [Accessing a Parameter](accessing-a-parameter.html)
- [Monitoring Device States](monitoring-device-states.html)
- [Sending and Receiving Raw Data](sending-and-receiving-raw-data.html#GUID-67706865-B170-4DD3-AD0D-1FDB01BB85A2) Raw data is the original binary data on a SubDevice. The raw data is an array of U8. A SubDevice separates the raw data differently depending on which mode the SubDevice is in.
- [Downloading the EtherCAT SubDevice Firmware](downloading-the-ethercat-slave-device-firmwar.html)

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=configuring-the-ethernet-adapter.html language=enus -->
## TOPIC 00010: Configuring the Ethernet Adapter

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `configuring-the-ethernet-adapter.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/configuring-the-ethernet-adapter.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: EtherCAT requires a special Ethernet adapter on the real-time controller to access the EtherCAT network. To configure an Ethernet adapter for EtherCAT, complete the following steps. Connect the real-time controller to the network. By default, some real-time controllers, such as real-time desktop con

### Configuring the Ethernet Adapter

EtherCAT requires a special Ethernet adapter on the real-time controller to access the EtherCAT
 network. To configure an Ethernet adapter for EtherCAT, complete the following
 steps.

1. Connect the real-time controller to the network. Note By default, some real-time
 controllers, such as real-time desktop controllers, do not have the special
 Ethernet adapter to connect to the network. Refer to *Supported
 Hardware* for more information about the additional adapters that
 you can add.
2. Launch NI Measurement & Automation Explorer (MAX).
3. To discover the real-time controller, double-click Remote
 Systems in the configuration tree. 
 Note MAX discovers
 and displays all devices in the network. The device discovery might take a
 few minutes. If you cannot find the real-time controller, select
 Remote Systems and press <F5> to refresh
 the list. If this operation does not work, ensure that you connect the
 real-time controller to the network with required software installed or
 contact NI.
4. Double-click the real-time controller to launch the advanced configuration page.
5. Click the Network Settings tab. 
 Note If the
 real-time controller has a customized Ethernet adapter, you must enable the
 customized adapter before selecting the adapter for the EtherCAT mode. Refer
 to the documentation of the real-time controller for more information about
 how to enable the customized adapter. 
 MAX displays all physical adapters available.
6. Click the Log in button on the
 toolbar to log in to the target with an account.
7. Choose the adapter for an EtherCAT network and select EtherCAT from the Adapter Mode pull-down menu. Note The primary adapter for the
 EtherCAT mode is reserved for configuration and programming. Do not select
 the primary adapter to control the EtherCAT SubDevice.
8. Specify the EtherCAT Master ID within the range of
 0-255. 
 If you do not specify the ID, MAX automatically assigns the smallest number
 available to the MainDevice ID.
9. If you use a PXI or an Industrial Controller, repeat
 steps 7 and 8 to configure multiple adapters for EtherCAT. 
 Make sure that the MainDevice IDs are unique for each adapter. If you use a
 CompactRIO Controller, you can assign only one network adapter for
 EtherCAT.
10. Click Save on the toolbar to apply the settings.

MAX restarts the real-time controller.

Note

Parent topic:

Installing the Software and Configuring the Ethernet Adapter

Related reference:

- Supported Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=configuring-the-third-party-master-for-the-ni.html language=enus -->
## TOPIC 00011: Configuring the Third-Party MainDevice for the NI-9145 in FPGA Mode

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `configuring-the-third-party-master-for-the-ni.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/configuring-the-third-party-master-for-the-ni.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: To generate a user-defined I/O variables profile, you must compile and download an FPGA VI on the FPGA target. The profile is used for the third-party EtherCAT MainDevice software recognizing the user-defined I/O variables. Before downloading an FPGA VI to the FPGA target on the NI-9145, ensure th

### Configuring the Third-Party MainDevice for the
 NI-9145 in FPGA Mode

Note

After
 successfully downloading the bitfile to the FPGA target on the NI-9145, LabVIEW
 generates a new XML file. This XML file is the user-defined variables profile and
 has the same file name as the FPGA bitfile.

Configure the third-party
 EtherCAT MainDevice for the NI-9145 in FPGA mode by completing the following
 steps.

1. Copy NI9145slots.xml, all the files in the
 Modules folder, and the generated XML file to the
 third-party EtherCAT MainDevice's IO configuration folder. 
 Note The
 generated XML file must be in the same directory with the
 Modules folder at
 \LabVIEW\resource\Framework\Providers\indcomecat\DD\Modules.
2. Open NI9145slots.xml with a text editor, add the generated XML
 file path at the end of the <InfoReference> section, and
 save the changes. 
 For example,
 <InfoReference>Modules\example_9145_FPGA.lvbitx.xml</InfoReference>.
3. Restart the third-party EtherCAT MainDevice system service.

Use the third-party EtherCAT MainDevice to discover the NI-9145 that contains the FPGA target. In
 the LabVIEW project, explore to the NI-9145 item. You can locate the FPGA target
 item under the NI-9145 item.

Parent topic:

Programming the FPGA on the NI-9145

Related tasks:

- Compiling, Downloading, and Running an FPGA VI

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=creating-and-discovering-the-fpga-target-and.html language=enus -->
## TOPIC 00012: Creating and Discovering the FPGA Target and Module

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `creating-and-discovering-the-fpga-target-and.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/creating-and-discovering-the-fpga-target-and.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a LabVIEW project to manage FPGA VIs and targets. Complete the following steps to create an FPGA target and set the FPGA LED in the NI-9145 using the FPGA VI. The following steps assume you have a MainDevice and NI-9145 connected to the network, and the Scan Mode personality is loaded on the N

### Creating and Discovering the FPGA Target and Module

Note

1. Create an empty project in LabVIEW.
2. Add the real-time controller to the project.
3. Right-click the controller item and select New»Targets and Devices to display the Add Targets and Devices
 dialog box.
4. Select Existing Target or Device and expand the EtherCAT Master Device category to discover the available EtherCAT Ethernet adapters.
5. Select an available EtherCAT Ethernet adapter and click
 OK. 
 LabVIEW automatically adds the NI-9145 item and all modules to the
 project.
6. Right-click the SubDevice item and select New»FPGA Target to create a new FPGA target under the NI-9145 item.
7. To use a module in FPGA Mode, drag and drop the module from the NI-9145 item
 under the FPGA target item. In the Project Explorer window,
 you can drag and drop modules between the NI-9145 item and the FPGA target item
 to switch between Scan Mode and FPGA Mode.
8. Right-click the FPGA target item and select New»VI. 
 LabVIEW adds a VI under the FPGA target item.
9. Double-click to open the new VI.
10. Drag and drop the I/O (Chassis I/O or Module I/O) from the Project
 Explorer on the block diagram. The following figure shows the
 block diagram of an FPGA VI that sets the FPGA LEDs. 
 [IMAGE alt='LabVIEW FPGA VI block diagram showing a write to an FPGA LED in a While Loop.' src='GUID-108D6A6D-9E50-48FC-B04C-367AFC50B703-a5.gif']

LabVIEW automatically compiles, downloads, and runs the FPGA VI on the FPGA target
 when you click the Run button in the FPGA VI. LabVIEW does
 not download the FPGA VI if the VI already is on the FPGA target.

In the NI-9145, if the FPGA LED blinks at the rate you set in the FPGA VI, LabVIEW
 has downloaded the VI and the VI is running successfully.

Tip

Download

Parent topic:

Programming the FPGA on the NI-9145

Related tasks:

- Compiling, Downloading, and Running an FPGA VI

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=creating-discovering-and-deploying-a-user-def.html language=enus -->
## TOPIC 00013: Creating, Discovering, and Deploying a User-Defined I/O Variable

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `creating-discovering-and-deploying-a-user-def.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/creating-discovering-and-deploying-a-user-def.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: This procedure assumes that the following prerequisite tasks are complete: Connect the MainDevice and NI-9145 to the network. Load the Scan Mode personality on the NI-9145. To create a user-defined variable, complete the following steps. Use the variable to transfer control from the host VI to the F

### Creating, Discovering, and Deploying a User-Defined I/O Variable

- Connect the MainDevice and NI-9145 to the network.
- Load the Scan Mode personality on the NI-9145.

To create a user-defined variable, complete
 the following steps. Use the variable to transfer control from the host VI to the FPGA
 VI and set the FPGA LED in NI-9145.

1. Create the FPGA target in the LabVIEW Project
 Explorer.
2. Right-click the NI-9145 item and select Add User-Defined
 Variable.
3. In the Shared Variable Properties dialog box, name this
 variable Set FPGA LED. Ensure that the data type of the
 variable matches the FPGA I/O that the variable maps to. In this example, select
 Boolean.
4. Set the Direction as Host to FPGA
 and click OK. 
 LabVIEW creates a User-Defined Variables
 container and adds this user-defined variable under the container.
5. Right-click the real-time controller and select New»VI. Rename this VI My Host VI.
6. Drag and drop the Set FPGA LED variable from the
 Project Explorer on the block diagram.
7. Wire a Boolean control to Set FPGA LED as shown in the
 following figure. 
 [IMAGE alt='LabVIEW block diagram wiring a Boolean control to the Set FPGA LED variable.' src='GUID-FF5FBEBB-E6F3-4CEC-81A3-0E9993AB259C-a5.gif']
8. Right-click the real-time controller and select Deploy All.
9. Use one of the following methods to ensure that the Scan Engine is in
 Configuration Mode.
  - Right-click the real-time controller from the Project
 Explorer and select Utilities»View in System Manager .
  - You can also use the NI Distributed System Manager. Select the real-time
 target in the left tree, and in the Scan Engine tab,
 ensure Scan Engine Mode»Configuration is green. If the color is not green, click the
 Change to Configuration button.
10. Right-click the FPGA target and select New»VI. Rename this VI My FPGA VI.
11. Drag and drop the FPGA LED from Project Explorer»FPGA Target»Chassis I/O on the block diagram.
12. Drag and drop the Set FPGA LED variable from the
 Project Explorer on the block diagram. Wire its data
 out to FPGA LED as shown in the following figure. 
 [IMAGE alt='Block diagram wiring data out from Set FPGA LED to the FPGA LED node.' src='GUID-BE2E2245-C75B-4CA8-820C-F88863000D69-a5.gif']
13. Click the Run button. 
 LabVIEW automatically compiles, downloads, and runs the FPGA VI on the
 FPGA target.
14. Right-click the real-time controller and select Utilities»Scan Engine Mode»Switch to Active.
15. Double-click My Host VI.vi in the Project
 Explorer.
16. Click the Run button.
17. Click the LED control in the front panel. 
 Then the application starts to control the FPGA LED in the
 NI-9145.

Parent topic:

Programming the FPGA on the NI-9145

Related concepts:

- User-Defined Variable

Related tasks:

- Compiling, Downloading, and Running an FPGA VI

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=deploying-or-undeploying-an-ethercat-configur.html language=enus -->
## TOPIC 00014: Deploying or Undeploying an EtherCAT Configuration

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `deploying-or-undeploying-an-ethercat-configur.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/deploying-or-undeploying-an-ethercat-configur.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: To deploy an EtherCAT network configuration explicitly to the real-time controller, right-click an EtherCAT MainDevice item and select Deploy. To remove an EtherCAT network configuration from the real-time controller, right-click an EtherCAT MainDevice item and select Undeploy. The EtherCAT MainDevi

### Deploying or Undeploying an EtherCAT Configuration

- To deploy an EtherCAT network configuration explicitly to the real-time
 controller, right-click an EtherCAT MainDevice item and select
 Deploy.
- To remove an EtherCAT network configuration from the real-time controller,
 right-click an EtherCAT MainDevice item and select
 Undeploy. 
 The EtherCAT MainDevice stops communication with the EtherCAT
 SubDevices.

Parent topic:

Configuring the EtherCAT Network

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=developing-an-ethercat-application-in-scan-mo.html language=enus -->
## TOPIC 00015: Developing an EtherCAT Application in Scan Mode

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `developing-an-ethercat-application-in-scan-mo.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/developing-an-ethercat-application-in-scan-mo.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an EtherCAT application, you can use the I/O variables and the EtherCAT references, or monitor I/O in NI Distributed System Manager. Using the I/O VariableAfter you configure your system, I/O variables are under the EtherCAT SubDevice and module items in the LabVIEW Project Explorer. Foll

### Developing an EtherCAT Application in Scan Mode

To develop an EtherCAT application, you can use the I/O variables and the EtherCAT references, or
 monitor I/O in NI Distributed System Manager.

#### Using the I/O Variable

After you configure your system, I/O variables are under the EtherCAT SubDevice and
 module items in the LabVIEW Project Explorer. Follow these steps to use the I/O
 variables in your VI:

1. Create or open a VI in your LabVIEW project.
2. Drag the I/O variables under the EtherCAT items and drop them in the VI block diagram. You now can use these I/O variables in the VI to access the EtherCAT network.

#### Using EtherCAT Reference and Procedures

You can use Property nodes and Invoke nodes to access an
 EtherCAT network.

#### Monitoring I/O in NI Distributed System Manager

- Right-click the real-time target item and select Utilities»View in System Manager to display the NI Distributed System
 Manager dialog box.
- Use the dialog box to monitor and change the I/O variables on the
 controller. 
 The controller and I/O variables are located under My
 Systems. If you cannot see the deployed I/O variables, press
 <F5> to refresh the item list.

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=discovering-ethercat-devices-programmatically.html language=enus -->
## TOPIC 00016: Discovering EtherCAT Devices Programmatically

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `discovering-ethercat-devices-programmatically.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/discovering-ethercat-devices-programmatically.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Refresh Modules VI in the Configuration mode to discover EtherCAT devices and configure these devices. Use the Search Variable Container function to list the configured devices. If you use third-party EtherCAT devices, you must copy the SubDevice information files to the /ni-rt/system/IndCom

### Discovering EtherCAT Devices Programmatically

- Use the Refresh Modules VI in the Configuration mode to
 discover EtherCAT devices and configure these devices.
- Use the Search Variable Container function to list the
 configured devices. 
 If you use third-party EtherCAT devices, you must copy the SubDevice
 information files to the /ni-rt/system/IndComECAT/DD folder on
 the device to discover the device. Refer to the *LabVIEW User Manual*
 for more information about using these two VIs.

Read Property.lvproj

labview\examples\indcomecat\Read Properties\

Parent topic:

Configuring the EtherCAT Network

Related information:

- LabVIEW User Manual

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=downloading-the-ethercat-slave-device-firmwar.html language=enus -->
## TOPIC 00017: Downloading the EtherCAT SubDevice Firmware

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `downloading-the-ethercat-slave-device-firmwar.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/downloading-the-ethercat-slave-device-firmwar.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: This operation may damage or destroy the EtherCAT SubDevice. Read the device manual and consult your device vendor before performing this operation. Before you complete this operation, you must obtain the SubDevice firmware from the device vendor. Complete the following steps to download the EtherCA

### Downloading the EtherCAT SubDevice
 Firmware

Attention

Note

Complete the following steps to download the EtherCAT SubDevice firmware to upgrade the
 EtherCAT SubDevice.

1. Right-click the EtherCAT SubDevice item and select Online Device
 State to display the Online Slave Device State dialog
 box and switch to the EtherCAT:Online:State page. 
 Note If the Online
 Device State menu is disabled, check the following items: Be sure the target controller and SubDevice are connected.
 Be sure the target item in the project has the correct IP address.
 Be sure the EtherCAT MainDevice item has the correct adapter. You can change the
 physical adapter on the General page of the
 EtherCAT Master Properties dialog box.
 Be sure you have deployed the MainDevice settings by right-clicking the MainDevice
 item and selecting the Deploy menu.
2. Click Change to Bootstrap to change the SubDevice mode
 to Bootstrap. 
 Note Before downloading
 firmware, you should change the scan engine to Configuration mode by right-clicking the
 controller item and selecting Utilities»Scan Engine Mode»Switch to Configuration.
3. Click Download Firmware to display the Download Firmware dialog box. Note You can also use this dialog box to
 download a precompiled FPGA bitfile to the FPGA
 target item under the NI-9145 item.
4. Select the firmware file and click
 Download. 
 The firmware download might take
 several seconds.

Parent topic:

Configuring the EtherCAT Network

Related tasks:

- Compiling, Downloading, and Running an FPGA VI

Related information:

- LabVIEW Project Items

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=enabling-the-device-monitor.html language=enus -->
## TOPIC 00018: Enabling the Device Monitor

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `enabling-the-device-monitor.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/enabling-the-device-monitor.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: You must add a MainDevice to a LabVIEW project before enabling the device monitor.To enable the device monitor, complete the following steps. Create a blank VI in the Project Explorer window. Set the NI Scan Engine to Configuration mode by using the Set Scan Engine Mode VI in the blank VI. Drag and

### Enabling the Device Monitor

You must add a MainDevice to a
 LabVIEW project before enabling the device monitor.

To enable the device monitor, complete the
 following steps.

1. Create a blank VI in the Project Explorer window.
2. Set the NI Scan Engine to Configuration mode by using the Set Scan
 Engine Mode VI in the blank VI.
3. Drag and drop the MainDevice from the Project Explorer
 window to the block diagram of this VI. 
 A reference of the MainDevice appears.
4. Add a Property node to the block diagram and wire the
 reference of the MainDevice to the reference input of the
 Property node.
5. Click the white area of the node and select Enable Device Monitor from the hierarchical menu that appears.
6. Right-click the white area of the node and select Change To Write from the shortcut menu.
7. Set Enable Device Monitor to TRUE
 by wiring a TRUE Boolean value to this input. 
 Note Ensure the
 Set Scan Engine Mode VI runs before the MainDevice
 Property node runs. The Property
 node cannot enable the device monitor if the NI Scan Engine is not in
 Configuration mode.
8. Run this VI to enable the device monitor.

You can read the SubDevice number
 and get the states of deployed and refreshed SubDevices after you enable the
 device monitor.

Parent topic:

Monitoring Device States

Related concepts:

- NI-Industrial Communications for EtherCAT and the NI Scan Engine

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ethercat-reference-and-procedures.html language=enus -->
## TOPIC 00019: Reading and Writing Properties at Run Time

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ethercat-reference-and-procedures.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ethercat-reference-and-procedures.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: You can read and write some properties of an EtherCAT MainDevice/SubDevice, or a C Series module, at run time using Property nodes. You can also call some procedures using Invoke nodes in an RT VI. To use this programming technique, complete the following common steps. Use the Set Mode VI located in

### Reading and Writing Properties at Run
 Time

You can read and write some properties of an EtherCAT MainDevice/SubDevice,
 or a C Series module, at run time using Property nodes. You can also call
 some procedures using Invoke nodes in an RT VI.

To use this programming technique, complete
 the following common steps.

1. Use the Set Mode VI located in the Measurement I/O»NI Scan Engine palette to set the scan engine to Configuration mode.
2. Use the Refresh Modules VI located in the Measurement I/O»NI Scan Engine palette to discover modules on the target. 
 Attention If the
 scan engine is in Active mode, LabVIEW reports an error.
3. Add an EtherCAT MainDevice/SubDevice reference or a C Series module
 reference to the RT VI.
4. Use Property nodes to read or write some properties of an
 EtherCAT MainDevice/SubDevice reference (or a C Series module
 reference). Or use Invoke nodes to call some procedures of an
 EtherCAT SubDevice reference.
5. Use the Open Variable Connection VI to open a shared
 variable using the output reference from the Property
 node/Invoke node.
6. After finishing all the configurations, use the Set Mode VI
 to set the scan engine to Active mode.
7. Use the Close Variable Connection VI to disconnect the
 shared variable after you finish all related operations. Refer to the
 *LabVIEW User Manual* for more information about how to use the
 shared variable.

Related information:

- LabVIEW User Manual

#### Reading and Writing EtherCAT
 MainDevice/SubDevice Properties at Run Time

You can read and write properties of an EtherCAT MainDevice/SubDevice at run time using
 Property nodes and call
 SubDevice procedures with
 Invoke nodes.

##### Adding an EtherCAT
 MainDevice/SubDevice Reference to an RT VI

- To add an EtherCAT MainDevice reference to an RT VI, drag the
 MainDevice item from the Project Explorer window on the block diagram
 of the VI. Right-click the resulting constant to create a MainDevice property node to use
 with the MainDevice.
- To add an EtherCAT SubDevice reference to an RT VI, drag the
 SubDevice item under an EtherCAT MainDevice item from the Project
 Explorer window on the block diagram of the VI. Right-click the resulting
 constant to create a SubDevice property or invoke node or a SubDevice
 method to use with the SubDevice. 
 Note You also can enumerate
 all EtherCAT MainDevice/SubDevice references by using the Searching
 Variable Container VI in Data Communication»Shared
 Variable»Search Variable Container.

Related information:

- Master Properties
- Slave Properties
- Slave Methods

#### Reading and Writing a C Series Module Property at Run Time

You can read all C Series module and channel properties, and write some C Series module and
 channel properties, at run time using Property nodes in an
 RT VI.

##### Adding a C Series Module Reference to an RT VI

1. To add a C Series module reference to an RT VI, drag the
 module item from the Project Explorer window on the block
 diagram of the VI.
2. Right-click the resulting constant to create properties and methods to use with
 the module. 
 Note If you make
 any configuration changes on a module properties page and deploy the
 settings, LabVIEW reverses all configuration changes you have made using
 Property nodes and Invoke nodes.

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ethercat-slave-device-state-transition.html language=enus -->
## TOPIC 00020: EtherCAT SubDevice State Transition

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ethercat-slave-device-state-transition.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ethercat-slave-device-state-transition.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can change the state of a SubDevice in the EtherCAT:Online:State page. You can change the state of a SubDevice independently from the NI Scan Engine mode with the following restrictions: You cannot place a SubDevice into Operational or Safe-Operational state unless the NI Scan Engine is in an eq

### EtherCAT SubDevice State
 Transition

You can change the state of a SubDevice in the EtherCAT:Online:State
 page. You can change the state of a SubDevice independently from the NI Scan
 Engine mode with the following restrictions:

- You cannot place a SubDevice into Operational or Safe-Operational state
 unless the NI Scan Engine is in an equivalent state (Active mode).
- You cannot place your device into Bootstrap state unless the NI Scan Engine is in
 Configuration mode.

The following diagram describes the EtherCAT SubDevice state transition.

Figure 4.

[IMAGE alt='State diagram showing EtherCAT SubDevice transitions between Bootstrap, Init, Pre-Operational, Safe-Operational, and Operational.' src='GUID-1ED4F290-E08A-4EFA-8B89-0FF151298D4C-a5.gif']

Parent topic:

NI-Industrial Communications for EtherCAT and the NI Scan Engine

Related information:

- Online Device State Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=fpga-mode.html language=enus -->
## TOPIC 00021: FPGA Mode

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `fpga-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/fpga-mode.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: In FPGA mode, you can use C Series modules from the FPGA VIs that you download to the NI-9145. You can configure modules from an RT VI or an FPGA VI. You can use the LabVIEW FPGA programming to add more flexibility, customization, and deterministic timing to the applications in the FPGA VI. To add c

### FPGA Mode

In FPGA mode, you can use C Series modules from the FPGA VIs that you download to
 the NI-9145. You can configure modules from an RT VI or an FPGA VI.

You can use the LabVIEW FPGA programming to add more flexibility, customization, and
 deterministic timing to the applications in the FPGA VI. To add custom timing, signal
 manipulation, and inline processing, program the FPGA.

#### Locating C Series Modules in
 LabVIEW

- Modules accessible from an RT VI—In the LabVIEW Project
 Explorer window, view accessible modules under the NI-9145 item.
 The I/O channels appear as I/O variables under the module items, just as in Scan
 mode.
- Modules accessible from an FPGA VI—In the LabVIEW Project
 Explorer window, view accessible modules directly under the FPGA
 target item. The I/O channels appear as FPGA I/O items under the FPGA target. To
 access the I/O channels, configure FPGA I/O nodes in FPGA VIs.

#### Requirements for Using the NI-9145
 in FPGA Mode

To use the NI-9145 in FPGA mode, ensure that you have either of the following:

- The LabVIEW FPGA Module installed on your host computer.
- Access to a compiled bit file that you can download to the FPGA.

To move from Scan mode to FPGA mode, you must download a LabVIEW FPGA application to
 the NI-9145 when the application compilation is complete.

#### Developing RT VIs and FPGA VIs

To develop RT VIs or FPGA VIs for a module, complete the following actions in the
 LabVIEW Project Explorer window:

1. To develop RT VIs for a module, drag and drop a module under the NI-9145
 item.
2. To develop FPGA VIs for a module, drag and drop a module to the FPGA target
 item. When you compile the FPGA VIs, the bit file contains the logic of
 the FPGA VI. The bit file also includes the logic necessary for
 communicating with modules from the RT VI. Note When compiling the FPGA VI,
 ensure that a module item is under the NI-9145 item. If a module item is not
 under the NI-9145 item in the Project Explorer window
 for a certain slot, the RT VI cannot access that slot.

Parent topic:

Programming the FPGA on the NI-9145

Related tasks:

- Compiling, Downloading, and Running an FPGA VI

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=getting-started-with-ni-industrial-communicat.html language=enus -->
## TOPIC 00022: Getting Started with NI-Industrial Communications for EtherCAT

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `getting-started-with-ni-industrial-communicat.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/getting-started-with-ni-industrial-communicat.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following sections to configure your system and get started with NI-Industrial Communications for EtherCAT.Complete the following steps to use NI-Industrial Communications for EtherCAT.

### Getting Started with NI-Industrial Communications for EtherCAT

Refer to the following sections to configure your system and get started with NI-Industrial Communications for
 EtherCAT.

Complete the following steps to use NI-Industrial Communications for EtherCAT.

1. Building the Hardware Network Connect a host, real-time controller, and EtherCAT SubDevices to build your EtherCAT network.
2. Installing the Software and Configuring the Ethernet Adapter Install the prerequisite software on the host, install NI-Industrial Communications for EtherCAT on the controller, and configure the Ethernet adapter.
3. Adding a Real-Time Controller to the LabVIEW Project
4. Adding an EtherCAT MainDevice and SubDevices to the LabVIEW Project
5. Using the I/O Variables in a VI

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=installing-sw-on-host.html language=enus -->
## TOPIC 00023: Installing Software on the Host

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `installing-sw-on-host.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/installing-sw-on-host.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the following prerequisite software, including NI-Industrial Communications for EtherCAT on the host. LabVIEW LabVIEW Real-Time Module NI CompactRIO Device Drivers For more information about compatible software versions, refer to NI-Industrial Communications for EtherCAT and LabVIEW Compatib

### Installing Software on the Host

NI-Industrial Communications for
 EtherCAT

- LabVIEW
- LabVIEW Real-Time Module
- NI CompactRIO Device Drivers

Note

NI-Industrial Communications for EtherCAT and
 LabVIEW Compatibility

NI-Industrial Communications for
 EtherCAT and NI CompactRIO Driver Compatibility

Note

Note

x

Parent topic:

Installing the Software and Configuring the Ethernet Adapter

Related information:

- NI-Industrial Communications for EtherCAT and LabVIEW
 Compatibility
- NI-Industrial Communications for EtherCAT and NI CompactRIO Driver
 Compatibility

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=installing-the-software-on-a-real-time-contro.html language=enus -->
## TOPIC 00024: Installing the Software on a Real-Time Controller

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `installing-the-software-on-a-real-time-contro.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/installing-the-software-on-a-real-time-contro.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to install the NI-Industrial Communications for EtherCAT software on a NI real-time controller. If you use a PXI Controller, follow the instructions to install the software on the PXI Controller. Launch NI Measurement & Automation Explorer (MAX). Double-click Remote Syst

### Installing the Software on a Real-Time Controller

Complete the following steps to install the NI-Industrial Communications for EtherCAT software on
 a NI real-time controller.

Note

1. Launch NI Measurement & Automation Explorer (MAX).
2. Double-click Remote Systems in the configuration tree to discover the real-time controller. Note MAX discovers all devices in the
 network, which takes a few seconds. If you cannot find the real-time
 controller after MAX displays all devices, select Remote
 Systems and press <F5> to refresh the list. If this
 does not work, make sure that you connect the real-time controller to the
 network with required software installed or contact NI.
3. Locate and expand the real-time controller, right-click
 Software, and select Add/Remove
 Software from the shortcut menu. 
 The LabVIEW Real-Time Software Wizard opens.
4. Choose one of the following options to install the software. 
 OptionDescriptionRecommended Software Set
 Enables you to install the NI recommended software set to the
 real-time controller.Select the recommended software set and click
 Next.
 Select NI-Industrial Communications for EtherCAT
 x, where
 x is the
 version number.Custom Software Installation
 Enables you to customize the installation.Select the software that you want to install, including
 NI-Industrial Communications for EtherCAT
 x, where
 x is the
 version number.
 Click Next.

Parent topic:

Installing the Software and Configuring the Ethernet Adapter

#### Installing the Software on a PXI
 Controller

To install the software on a PXI Controller,
 complete the following steps.

1. Power off the PXI chassis.
2. Remove the Ethernet PXI board from the PXI chassis. Power on the chassis.
3. Install the NI-Industrial Communications for EtherCAT software on the PXI
 Controller. Power off the chassis.
4. Connect the Ethernet PXI board into the PXI chassis. Power on the PXI
 chassis.

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=monitoring-device-states.html language=enus -->
## TOPIC 00025: Monitoring Device States

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `monitoring-device-states.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/monitoring-device-states.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can monitor all the EtherCAT SubDevice states in the Online Master State dialog box and monitor an EtherCAT SubDevice state on the EtherCAT:Online:State page of the Online Slave Device State dialog box. You also can enable the device monitor to programmatically read the number of SubDevices on a

### Monitoring Device States

You can monitor all the EtherCAT SubDevice states in the Online Master
 State dialog box and monitor an EtherCAT SubDevice state on the
 EtherCAT:Online:State page of the Online Slave Device
 State dialog box.

You also can enable the device monitor to programmatically read the number of SubDevices
 on a MainDevice and get the states of deployed and refreshed SubDevices. The
 MainDevice updates the slave states in every scan cycle of the NI Scan Engine. You can
 read the slave states in a timed loop that synchronizes to the scan cycles.

Parent topic:

Configuring the EtherCAT Network

Related information:

- Online Master State Dialog Box
- EtherCAT:Online:State Page
- Online Device State Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=new-features-and-changes.html language=enus -->
## TOPIC 00026: NI-Industrial Communications for EtherCAT New Features and Changes

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-Industrial Communications for EtherCAT. Discover what is new in the latest releases of NI-Industrial Communications for EtherCAT.If you cannot find new features and changes for your version, it might n

### NI-Industrial Communications for
 EtherCAT
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-Industrial Communications for
 EtherCAT.

NI-Industrial Communications for
 EtherCAT

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-Industrial Communications for
 EtherCAT
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 EtherCAT 2025 Q4.

##### New
 Features

This version of the NI-Industrial Communications for
 EtherCAT provides
 support for the following features:

- Added support for Linux Kernel 6.12.
- Fixed the importing and the loading of EtherCAT Slave Information (ESI) files that use a
 DictionaryFile Reference.

Related concepts:

- Adding, Editing, or Removing an EtherCAT SubDevice

#### NI-Industrial Communications for EtherCAT
 2025 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial
 Communications for EtherCAT 2025 Q2.

- Added support for the PXIe-8842 and PXIe-8862 PXI controllers
- Performance improvements for EtherCAT 64-bit support

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ni-9145-fpga-i-o.html language=enus -->
## TOPIC 00027: NI-9145 FPGA I/O

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ni-9145-fpga-i-o.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ni-9145-fpga-i-o.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: After adding the NI-9145 item to your LabVIEW project, you can add an FPGA target item. The I/O in the following table appears as Chassis I/O. 4 FPGA I/O FPGA I/O Attribute Description Chassis Temperature Read Only The Chassis Temperature output returns 16-bit values for the temperature. You can con

### NI-9145 FPGA I/O

After adding the NI-9145 item to your LabVIEW project, you can add an FPGA target item.

The I/O in the following table appears as Chassis I/O.

| FPGA I/O | Attribute | Description |
| --- | --- | --- |
| Chassis Temperature | Read Only | The Chassis Temperature output returns 16-bit values for the temperature. You can convert this value into meaningful engineering units. Refer to Configuring the Chassis I/O (FPGA Interface) in the NI CompactRIO Device Drivers manual for more information. |
| Input Virtual Point | Read Only | Input Virtual Point reflects the point in time when all RSI module inputs are latched. Refer to NI-9145 Timing Diagram for details. If the mode is not polling, use the Wait on Edge method for this signal. If the mode is polling, use a single cycle loop. This signal is held high for 50 ns. |
| Output Virtual Point | Read Only | Output Virtual Point reflects the point in time when all RSI module outputs are latched. Refer to NI-9145 Timing Diagram for details. If the mode is not polling, use the Wait on Edge method for this signal. If the mode is polling, use a single cycle loop. This signal is held high for 50 ns. |
| FPGA LED | Read/Write | Writing a 1 to the FPGA LED turns on the LED indicator on the front of the NI-9145 labeled FPGA. |
| EtherCAT State | Read Only | Returns the EtherCAT network state. 0 — No State 1 — Init 2 — PreOp 3 — Bootstrap 4 — SafeOp 5 — Operational |
| Scan Clock | Read Only | You can use a Scan Clock I/O item to monitor when the NI Scan Engine transfers data between the FPGA VI and the RT host VI. Refer to Synchronizing FPGA VIs with the NI Scan Engine (FPGA Interface) in the NI CompactRIO Device Drivers manual for more information. |
| Sleep | Write Only | The Sleep I/O item is only available for NI-9145. When the NI-9145 chassis enters sleep mode, the power consumption of all RSI modules is minimum. |

Parent topic:

Programming the FPGA on the NI-9145

Related concepts:

- NI-9145 Timing Diagram

Related information:

- NI CompactRIO Device Drivers — Configuring the Chassis I/O (FPGA
 Interface)
- NI CompactRIO Device Drivers — Synchronizing FPGA VIs with the NI
 Scan Engine (FPGA Interface)

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ni-9145-timing-diagram.html language=enus -->
## TOPIC 00028: NI-9145 Timing Diagram

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ni-9145-timing-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ni-9145-timing-diagram.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Processing in EtherCAT as part of the scan interface occurs in two phases: the scan phase and the application/update phase. 3 Timing Diagram Timing diagram showing scan period with scan and application/update phases, and points to update outputs and latch inputs. Scan phase A phase for communication

### NI-9145 Timing Diagram

Processing in EtherCAT as part of the scan interface occurs in two phases: the
 *scan* phase and the *application/update* phase.

Figure 3.

[IMAGE alt='Timing diagram showing scan period with scan and application/update phases, and points to update outputs and latch inputs.' src='GUID-A8460F9F-530E-4C5E-8E87-E373F487116E-a5.gif']

Scan

Application/update

Output virtual point

update outputs

Input virtual point

latch inputs

For the FPGA, the virtual points appear in the form of two Boolean I/O variables available under
 the FPGA target. The rising edge of the I/O variables represents the appropriate virtual
 point. The FPGA code can synchronize with the virtual points of the EtherCAT network.

A Scan Clock I/O variable is for the FPGA. The rising edge indicates the
 beginning of the *update* phase. The falling edge terminates the
 *update* phase.

Parent topic:

Programming the FPGA on the NI-9145

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ni-industrial-communications-for-ethercat-and.html language=enus -->
## TOPIC 00029: NI-Industrial Communications for EtherCAT and the NI Scan Engine

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ni-industrial-communications-for-ethercat-and.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ni-industrial-communications-for-ethercat-and.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Industrial Communications for EtherCAT leverages the NI Scan Engine to provide the I/O variable. The NI Scan Engine allows access to coherent sets of data channels, such as I/O channels. The NI Scan Engine uses a scan that stores data in a global memory map. The NI Scan Engine also updates all va

### NI-Industrial Communications for EtherCAT and the NI Scan Engine

NI-Industrial Communications for EtherCAT leverages the NI Scan Engine to provide
 the I/O variable.

The NI Scan Engine allows access to coherent sets of data channels, such as I/O channels. The NI
 Scan Engine uses a scan that stores data in a global memory map. The NI Scan Engine also
 updates all values at a single rate, known as the scan period. Refer to the
 *LabVIEW User Manual* for the more information about the NI Scan Engine.

#### EtherCAT State and NI Scan Engine
 Mode

The NI Scan Engine controls the NI-Industrial Communications for EtherCAT MainDevice. The
 following table shows the modes of the NI Scan Engine.

| Mode | Description |
| --- | --- |
| Configuration | The required mode for configuring NI Scan Engine settings and hardware on the EtherCAT network. I/O variables are not updated with real data. |
| Active | In this mode, the NI Scan Engine actively updates I/O variables with real data from the EtherCAT network. |

EtherCAT SubDevices have the following states.

| State | Description |
| --- | --- |
| Operational | The EtherCAT SubDevice supports full process communication and the mailbox functionality in this state. |
| Safe-Operational | The EtherCAT SubDevice supports mailbox functionality, but only input process communication. The output process communication of the SubDevice does not function in this state. |
| Pre-Operational | The state in which the EtherCAT SubDevice supports mailbox functionality such as SDO. The SubDevice process communication, PDO, does not function. |
| Init | In this state, the EtherCAT SubDevice does not communicate on the application layer. |
| Bootstrap | The state in which you can download the SubDevice firmware. |

#### Automatic Mode Transition

The NI-Industrial Communications for EtherCAT MainDevice changes the states of the
 SubDevices. The following rules outline how the MainDevice automatically controls
 the NI Scan Engine modes and the states of the EtherCAT devices.

- When the NI Scan Engine is in Active mode, the MainDevice transitions all
 SubDevices to their Operational states. The operation might fail if the devices
 are not properly configured.
- When the NI Scan Engine goes to Configuration mode, the MainDevice transitions all
 SubDevices to their Pre-Operational states.
- Deploying any changes to the project or undeploying the EtherCAT MainDevice
 automatically transitions the NI Scan Engine to Configuration mode.
- With the default settings after new settings are deployed, the NI Scan Engine
 automatically transitions to Active mode. To control this behavior, you can adjust the
 Scan Engine settings for the real-time controller. In the settings, you can choose to
 report automatic mode transitions as conflicts.
- If nothing new is detected in the LabVIEW project, deployments do not trigger a NI Scan
 Engine change.
- Running a VI automatically triggers a deployment. The current NI Scan Engine mode and
 whether anything deploys to the target determine if a mode change occurs.

Related concepts:

- Using the I/O Variable

Related information:

- LabVIEW User Manual

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=ni-scan-engine-mode-transition.html language=enus -->
## TOPIC 00030: NI Scan Engine Mode Transition

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `ni-scan-engine-mode-transition.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/ni-scan-engine-mode-transition.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: You can change the NI Scan Engine mode manually or programmatically. To change the NI Scan Engine mode manually, right-click the target item in the LabVIEW Project Explorer. Select Utilities Scan Engine Mode Switch to Active (or Switch to Configuration). To change the NI Scan Engine mode programmati

### NI Scan Engine Mode Transition

You can change the NI Scan Engine mode manually or programmatically.

- To change the NI Scan Engine mode manually, right-click the target item in the
 LabVIEW Project Explorer. Select Utilities»Scan Engine Mode»Switch to Active (or Switch to Configuration).
- To change the NI Scan Engine mode programmatically, use the Set Scan
 Engine Mode VI in the Measurement I/O»NI Scan Engine palette.

To receive notifications of all NI Scan Engine mode transitions, complete the following
 steps.

1. Right-click the target item in the LabVIEW Project Explorer and select
 Properties .
2. Check the report automatic scan mode transitions as conflicts option on the Scan Engine page.

Note

The following figure describes the NI Scan Engine mode transitions.

Figure 5.

[IMAGE alt='Diagram of NI Scan Engine transitions between Active Mode and Configuration Mode.' src='GUID-8651F0CE-A0E2-48CB-AF15-C1421D99DF9A-a5.gif']

Parent topic:

NI-Industrial Communications for EtherCAT and the NI Scan Engine

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=optimizing-an-fpga-application.html language=enus -->
## TOPIC 00031: Optimizing an FPGA Application

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `optimizing-an-fpga-application.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/optimizing-an-fpga-application.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use one of the following techniques to optimize the usage of the NI-9145 physical memory and increase the compiling speed. Refer to the LabVIEW FPGA Module User Manual for more information about optimizing FPGA VIs. Limit the number of user-defined variables. The number of user-defined variables tha

### Optimizing an FPGA Application

Use one of the following techniques to optimize the usage of the NI-9145 physical memory and
 increase the compiling speed. Refer to the *LabVIEW FPGA Module User Manual*
 for more information about optimizing FPGA VIs.

- Limit the number of user-defined variables. The number of user-defined variables
 that can fit in the NI-9145 depends on many factors, including:
  - The number and type of C Series modules used in Scan Mode
  - The number and type of user-defined variables
  - The user logic on the LabVIEW FPGA diagram
- Use the smallest data type, if possible. Use the smallest data type for non-constant
 values to decrease the size and increase the speed of an FPGA VI.
- Shorten the length of the user-defined variable name. The user-defined variable name
 is stored in the NI-9145 Object Dictionary (OD) after you compile and download the
 FPGA VI. Shortening the name reduces the usage of the OD table.

Parent topic:

Programming the FPGA on the NI-9145

Related information:

- LabVIEW FPGA Module User Manual

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=overview.html language=enus -->
## TOPIC 00032: NI-Industrial Communications for EtherCAT Overview

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/overview.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Industrial Communications for EtherCAT software provides an EtherCAT MainDevice driver to support real-time EtherCAT network operations. Use the software with the LabVIEW Real-Time Module to configure the EtherCAT network and map the EtherCAT device signals to the LabVIEW I/O variables. Ether

### NI-Industrial Communications for
 EtherCAT
 Overview

The NI-Industrial Communications for
 EtherCAT software provides an EtherCAT MainDevice
 driver to support real-time EtherCAT network operations. Use the software with the LabVIEW
 Real-Time Module to configure the EtherCAT network and map the EtherCAT device signals to
 the LabVIEW I/O variables.

#### EtherCAT

EtherCAT is a high-performance industrial communication protocol for deterministic
 Ethernet. EtherCAT extends IEEE 802.3 Ethernet standard to transfer data with
 predictable timing and precise synchronization. This open standard is published as
 part of IEC 61158 specification. The standard is commonly used in applications such
 as machine design and motion control.

EtherCAT implements a MainDevice/SubDevice architecture over a standard
 Ethernet cabling, as shown in the following figure. NI EtherCAT MainDevices consist
 of real-time controllers with dual Ethernet adapters, such as CompactRIO and PXI.
 Each NI SubDevice also contains two adapters that permit daisy-chaining from
 the MainDevice controller.

Figure 1.

[IMAGE alt='Diagram of an EtherCAT network with a host computer, NI cRIO MainDevice, and daisy-chained SubDevice chassis.' src='GUID-13F85F4C-3318-438C-A880-F579601CA819-a5.gif']

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=programming-the-fpga-on-the-ni-9145.html language=enus -->
## TOPIC 00033: Programming the FPGA on the NI-9145

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `programming-the-fpga-on-the-ni-9145.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/programming-the-fpga-on-the-ni-9145.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: You need the LabVIEW FPGA Module to program and compile LabVIEW FPGA.

### Programming the FPGA on the NI-9145

Note

- [Scan Mode](scan-mode.html) You can use Scan mode to access C Series modules directly from the LabVIEW Real-Time Module.
- [FPGA Mode](fpga-mode.html) In FPGA mode, you can use C Series modules from the FPGA VIs that you download to the NI-9145. You can configure modules from an RT VI or an FPGA VI.
- [NI-9145 FPGA I/O](ni-9145-fpga-i-o.html)
- [NI-9145 Timing Diagram](ni-9145-timing-diagram.html) Processing in EtherCAT as part of the scan interface occurs in two phases: the scan phase and the application/update phase.
- [User-Defined Variable](user-defined-variable.html) User-defined variables transfer custom FPGA-processed data between an FPGA VI and an RT VI.
- [Creating and Discovering the FPGA Target and Module](creating-and-discovering-the-fpga-target-and.html)
- [Creating, Discovering, and Deploying a User-Defined I/O Variable](creating-discovering-and-deploying-a-user-def.html)
- [Compiling, Downloading, and Running an FPGA VI](compiling-downloading-and-running-an-fpga-vi.html)
- [Removing an FPGA VI from the NI-9145](removing-an-fpga-vi-from-the-ni-9145.html)
- [Optimizing an FPGA Application](optimizing-an-fpga-application.html)
- [Configuring the Third-Party MainDevice for the NI-9145 in FPGA Mode](configuring-the-third-party-master-for-the-ni.html)

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=reading-the-total-number-and-states-of-device.html language=enus -->
## TOPIC 00034: Reading the Total Number and States of Devices

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `reading-the-total-number-and-states-of-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/reading-the-total-number-and-states-of-device.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: After you enable the device monitor, you can use the GetDeviceCount and GetSlaveStates Invoke nodes. You must have a LabVIEW project that contains a VI and a MainDevice to use these Invoke nodes. Complete the following steps to read the number of SubDevices on a MainDevice and get the states of depl

### Reading the Total Number and States of Devices

After you enable the device monitor, you can use the GetDeviceCount and
 GetSlaveStates
 Invoke nodes. You must have a LabVIEW project that contains a VI
 and a MainDevice to use these Invoke nodes. Complete the
 following steps to read the number of SubDevices on a MainDevice and get the
 states of deployed and refreshed SubDevices.

1. Add the Set Scan Engine Mode VI to the block diagram of the existing VI.
2. Set the mode input of the Set Scan Engine Mode VI to
 Active Mode.
3. Drag and drop the MainDevice from the Project Explorer
 window to the block diagram. A reference of the MainDevice appears.
4. Add an Invoke Node to the block diagram and wire the reference of the
 MainDevice to the reference input of the Property Node.
5. Click the white area of the node and select GetDeviceCount or GetSlaveStates from the hierarchical menu that appears.
  - GetDeviceCount : Returns the total number of
 SubDevices that connect to the MainDevice.
  - GetSlaveStates : Returns the states of all
 deployed and refreshed SubDevices that connect to the MainDevice. If
 you select this method, you must wire an array of U32 to the
 Slave State input. The Invoke 
 node allocates memory for SubDevice states according to the size of
 this array.
6. Run this VI to read information from SubDevices.

Parent topic:

Monitoring Device States

Related information:

- GetDeviceCount
- GetSlaveStates

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=remote-i-o.html language=enus -->
## TOPIC 00035: Remote I/O

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `remote-i-o.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/remote-i-o.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Remote I/O is a modular I/O system for measurement, machine control, and industrial automation. NI provides Remote I/O API for communicating with Remote I/O devices in an EtherCAT environment. Remote I/O includes the following components.7 Remote I/O ComponentsComponentDescriptionREM-11100Analog inp

### Remote I/O

Remote I/O is a modular I/O system for measurement, machine control, and industrial automation. NI provides Remote I/O API for communicating with Remote I/O devices in an EtherCAT environment.

Remote I/O includes the following components.

| Component | Description |
| --- | --- |
| REM-11100 | Analog input module with 4 voltage inputs |
| REM-11102 | Analog input module with 4 current inputs |
| REM-11115 | Analog output module with 4 outputs |
| REM-11120 | Temperature input module with 4 inputs |
| REM-11152 | Digital input module with 16 inputs |
| REM-11154 | Digital input module with 32 inputs |
| REM-11175 | Digital output module with 16 outputs |
| REM-11178 | Digital output module with 32 outputs |
| REM-11180 | Bus coupler |
| REM-11190 | Power module |

Refer to the documentation for your remote I/O component at *ni.com/docs*.

Related concepts:

- Getting Started with NI-Industrial Communications for EtherCAT
- Configuring the EtherCAT Network

Related tasks:

- Reading and Writing Properties at Run Time

Related information:

- Remote I/O VIs

#### Accessing Remote I/O VIs

Getting Started

1. In the LabVIEW Project Explorer window, right-click the RT
 target and select New»VI.
2. Select Window»Show Block Diagram to view the block diagram of the VI.
3. Select View»Functions Palette and navigate to Industrial Communications»EtherCAT»Remote I/O».

- The labview\examples\indcomecat\Remote IO directory
- In the NI Example Finder window, located at Hardware Input and Output»NI-Industrial Communications»EtherCAT»Remote IO

Related concepts:

- Getting Started with NI-Industrial Communications for EtherCAT

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=removing-an-fpga-vi-from-the-ni-9145.html language=enus -->
## TOPIC 00036: Removing an FPGA VI from the NI-9145

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `removing-an-fpga-vi-from-the-ni-9145.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/removing-an-fpga-vi-from-the-ni-9145.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: To remove an FPGA VI from the NI-9145, complete the following steps. Right-click the NI-9145 item in the LabVIEW project. Select Utilities Revert to Scan Mode . Change the scan engine to Configuration mode before reverting. Otherwise, LabVIEW displays an error. The reverting operation might take s

### Removing an FPGA VI from the NI-9145

To remove an FPGA VI from the NI-9145, complete the following steps.

1. Right-click the NI-9145 item in the LabVIEW project.
2. Select Utilities»Revert to Scan Mode.

Note

Parent topic:

Programming the FPGA on the NI-9145

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=scan-mode.html language=enus -->
## TOPIC 00037: Scan Mode

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `scan-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/scan-mode.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Scan mode to access C Series modules directly from the LabVIEW Real-Time Module. By default, the NI-9145 is in Scan mode. Locating Modules Modules in Scan mode appear directly under the NI-9145 item in the LabVIEW Project Explorer window. The I/O channels appear as I/O variables under th

### Scan Mode

You can use Scan mode to access C Series modules directly from the LabVIEW Real-Time
 Module.

Note

#### Locating Modules

Modules in Scan mode appear directly under the NI-9145 item in the LabVIEW
 Project Explorer window. The I/O channels appear as I/O
 variables under the modules.

To use I/O variables, drag and drop the variables to the RT VIs.

Restriction

Parent topic:

Programming the FPGA on the NI-9145

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=sending-and-receiving-raw-data.html language=enus -->
## TOPIC 00038: Sending and Receiving Raw Data

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `sending-and-receiving-raw-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/sending-and-receiving-raw-data.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Raw data is the original binary data on a SubDevice. The raw data is an array of U8. A SubDevice separates the raw data differently depending on which mode the SubDevice is in. SubDevice Modes A SubDevice has the following modes: Normal mode The SubDevice separates the raw data by channel. The Ether

### Sending and Receiving Raw Data

Raw data is the original binary data on a SubDevice. The raw data is an array
 of U8. A SubDevice separates the raw data differently depending on which mode the
 SubDevice is in.

#### SubDevice Modes

A SubDevice has the following modes:

Normal mode

Raw Data mode

Raw Data Invoke

#### EtherCAT Network with Multiple
 SubDevices

If an EtherCAT network contains multiple SubDevices, the MainDevice creates
 the following arrays:

Input raw data array

Output raw data array

The size of both arrays equals the total width of all SubDevice channels on
 this network. The MainDevice saves the raw data that it receives from the
 SubDevice to the corresponding elements of the input raw data array. The
 MainDevice reads the raw data from the output raw data array before sending the raw
 data to a SubDevice. The EtherCAT network layout and the SubDevice
 channels determine the mapping relation between the channels and the array elements.
 You can get the size of these arrays and the mapping relation by using the
 Get Input Raw Data Information node and the Get
 Output Raw Data Information Invoke node.

For example, an EtherCAT network contains three SubDevices. The following
 table lists the mode and channel information of these devices.

| Name | Mode | Channel Number | Channel Width |
| --- | --- | --- | --- |
| Device A | Raw Data | 1 | 16 bits |
| Device B | Normal | 1 | 16 bits |
| Device C | Raw Data | 2 | Channel 1: 16 bits Channel 2: 16 bits |

The MainDevice creates the input and the output raw data arrays for the three
 devices. In this example, the total width of all channels on this network is 64
 bits. The size of each array is also 64 bits. Because the data type of the array
 elements is U8, the size of an array element is 8 bits. Each array contains eight
 elements. The MainDevice saves the raw data it receives from the SubDevices
 to the corresponding elements of the input raw data array.

The following table shows mapping relation between the elements, bits, and data from
 devices.

| Element | Bit | Data |
| --- | --- | --- |
| 0-1 | 0-15 | Raw data from Device A |
| 2-3 | 16-31 | Blank |
| 4-7 | 32-63 | Raw data from Device C |

Note

EtherCAT
 Expansion Chassis Vendor Configurations Guide

If you enable the Raw Data mode on a SubDevice, you cannot access the data on
 this device by using I/O variables. You must use the Raw Data
 Invoke nodes to access and convert the data from this
 SubDevice.

Parent topic:

Configuring the EtherCAT Network

Related information:

- Get Input Raw Data Information
- Get Output Raw Data Information
- EtherCAT® Expansion Chassis Vendor Configurations
 Guide

#### Enabling Raw Data Mode

You must add the SubDevice to
 a LabVIEW project before enabling Raw Data mode on a SubDevice.

To enable Raw Data mode, complete the following steps.

1. Create a blank VI in the Project Explorer window.
2. Drag and drop the SubDevice from the Project
 Explorer window to the block diagram of the new VI. 
 A reference of the SubDevice appears.
3. Add a Property node to the block diagram.
4. Wire the reference of the SubDevice to the reference input of the
 Property node.
5. Click the white area of the node and select Enable Raw Data Mode from the hierarchical menu that appears.
6. Right-click the white area of the node and select Change To Write from the shortcut menu.
7. Set Enable Raw Data Mode to TRUE by
 wiring a TRUE Boolean value to this input.
8. Run the VI. 
 The SubDevice is in Raw Data mode.

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=step-1-building-the-hardware-network.html language=enus -->
## TOPIC 00039: Building the Hardware Network

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `step-1-building-the-hardware-network.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/step-1-building-the-hardware-network.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect a host, real-time controller, and EtherCAT SubDevices to build your EtherCAT network.Build the EtherCAT network by connecting the following hardware items. Select a host. A host is a desktop or laptop with Windows and LabVIEW. Use the host to configure the real-time controller and the EtherC

### Building the Hardware Network

Connect a host, real-time controller, and EtherCAT SubDevices to build your
 EtherCAT network.

Build the EtherCAT network by connecting the
 following hardware items.

- Select a *host*. A host is a desktop or laptop with Windows and
 LabVIEW. Use the host to configure the real-time controller and the EtherCAT
 SubDevices.
- Select a *real-time controller*. Ensure that NI-Industrial
 Communications for EtherCAT supports the controller. Refer to *Supported
 Hardware* for a list of supported hardware. The controller has the
 following Ethernet adapters: 
 *Adapter 1* is for communication between the host and
 controller through TCP/IP.
 *Adapter 2* is exclusively for EtherCAT communication between
 the EtherCAT MainDevice and the EtherCAT SubDevices. Adapter 2
 is referred to as the *EtherCAT adapter*.
- Select the *EtherCAT SubDevices* from NI and other
 vendors.

The following figure shows a typical EtherCAT network that you can build.

[IMAGE alt='Diagram of a host PC connected to an EtherCAT master, which connects to multiple EtherCAT slaves.' src='GUID-51C10E23-53BD-4A0C-860A-95CBF411AB1E-a5.gif']

Parent topic:

Getting Started with NI-Industrial Communications for EtherCAT

Related reference:

- Supported Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=step-2-installing-the-software.html language=enus -->
## TOPIC 00040: Installing the Software and Configuring the Ethernet Adapter

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `step-2-installing-the-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/step-2-installing-the-software.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the prerequisite software on the host, install NI-Industrial Communications for EtherCAT on the controller, and configure the Ethernet adapter.

### Installing the Software and Configuring the
 Ethernet Adapter

Install the prerequisite software on the host, install NI-Industrial Communications for
 EtherCAT on the controller, and configure the Ethernet
 adapter.

1. Installing Software on the Host
2. Installing the Software on a Real-Time Controller
3. Configuring the Ethernet Adapter

Parent topic:

Getting Started with NI-Industrial Communications for EtherCAT

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=step-3-adding-a-real-time-controller-to-the-l.html language=enus -->
## TOPIC 00041: Adding a Real-Time Controller to the LabVIEW Project

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `step-3-adding-a-real-time-controller-to-the-l.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/step-3-adding-a-real-time-controller-to-the-l.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: After configuring the hardware and installing the software, add a NI real-time controller to a LabVIEW project. Launch LabVIEW. Create a LabVIEW project and save the project. In the LabVIEW Project Explorer, right-click the Project root item and select New Targets and Devices . In the Add Target and

### Adding a Real-Time Controller to the LabVIEW
 Project

After configuring the hardware and installing the
 software, add a NI real-time controller to a LabVIEW project.

1. Launch LabVIEW.
2. Create a LabVIEW project and save the project.
3. In the LabVIEW Project Explorer, right-click the
 Project root item and select New»Targets and Devices.
4. In the Add Target and Devices dialog box that appears, add the controller to the LabVIEW project. If the controller is online, select Existing target or device and expand
 the related controller category to select the controller. Note If a
 controller does not appear under the category, make sure that you
 connect the controller to the host computer.
If the controller is offline, select New target or device to add the controller.
5. Click OK to exit.

Parent topic:

Getting Started with NI-Industrial Communications for EtherCAT

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=step-4-adding-an-ethercat-master-and-slaves-t.html language=enus -->
## TOPIC 00042: Adding an EtherCAT MainDevice and SubDevices to the LabVIEW Project

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `step-4-adding-an-ethercat-master-and-slaves-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/step-4-adding-an-ethercat-master-and-slaves-t.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: To add an EtherCAT MainDevice to the LabVIEW project, complete the following steps. Right-click the controller item and select Connect to connect the controller. Right-click the controller item in the LabVIEW Project Explorer and select New Targets and Devices . In the Add Targets and Devices dialog

### Adding an EtherCAT MainDevice and
 SubDevices to the LabVIEW Project

To add an EtherCAT MainDevice to the LabVIEW
 project, complete the following steps.

1. Right-click the controller item and select Connect to connect the controller.
2. Right-click the controller item in the LabVIEW
 Project Explorer and select New»Targets and Devices.
3. In the Add Targets and Devices dialog
 box that appears, expand the EtherCAT Master
 Device category to view the available
 EtherCAT Ethernet adapters. 
 Note If an
 adapter is not available, make sure that you have
 configured the Ethernet adapter for EtherCAT.
4. Select the EtherCAT Ethernet adapter and click
 OK to display the MainDevice
 and the SubDevices. 
 Note If
 you cannot see the SubDevice items in the
 project tree, ensure that the EtherCAT
 SubDevices are connected to the EtherCAT
 adapter of the real-time controller. **EtherCAT MainDevice**—One real-time controller usually has one
 MainDevice using the special Ethernet adapter for
 the EtherCAT network.
 **EtherCAT SubDevice**—An EtherCAT SubDevice from NI or a
 third-party vendor.
 **EtherCAT Module**—An EtherCAT SubDevice might contain
 one or more modules. Modules accessible from an RT
 VI appear directly under the SubDevice
 item. The I/O channels appear as I/O variables
 under the module items. Modules accessible from an
 FPGA VI appear directly under the FPGA target
 item. The I/O channels appear as FPGA I/O items
 under the FPGA target item.
 **I/O Variable**—The physical channels of the SubDevice
 and module maps to the I/O variables. A
 SubDevice or module can have several I/O
 variables.
 **FPGA Target**—You must add an FPGA target to the LabVIEW
 project before creating FPGA VIs and using the
 NI-9145 in FPGA mode.
 **User-Defined Variable**—User-defined variables transfer FPGA-processed
 data between an FPGA VI and an RT VI.
 Note The
 NI-9145 is the only EtherCAT SubDevice with
 FPGA support in LabVIEW.

Parent topic:

Getting Started with NI-Industrial Communications for EtherCAT

Related tasks:

- Configuring the Ethernet Adapter

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=step-5-using-the-i-o-variables-in-a-vi.html language=enus -->
## TOPIC 00043: Using the I/O Variables in a VI

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `step-5-using-the-i-o-variables-in-a-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/step-5-using-the-i-o-variables-in-a-vi.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create an application in the LabVIEW project using the EtherCAT signals. Right-click the controller item and select New VI to create a VI. Save the VI. Drag the I/O variable under the EtherCAT items and drop the variable on the block diagram of the VI. Wire a control

### Using the I/O Variables in a VI

Complete the following steps to create an application in the LabVIEW project using the
 EtherCAT signals.

1. Right-click the controller item and select New»VI to create a VI.
2. Save the VI.
3. Drag the I/O variable under the EtherCAT items and drop the variable on the block diagram of the VI.
4. Wire a control or indicator to the I/O variable.
5. Run the VI.

After completing these steps, you can use a VI to access the EtherCAT network.

Parent topic:

Getting Started with NI-Industrial Communications for EtherCAT

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=supported-hardware.html language=enus -->
## TOPIC 00044: Supported Hardware

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `supported-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/supported-hardware.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-Industrial Communications for EtherCAT software provides support for hardware configured as EtherCAT MainDevices. The following table lists the supported hardware configured as EtherCAT MainDevices and the earliest supported version of the NI-Industrial Communications for EtherCAT. 1 Supporte

### Supported Hardware

The NI-Industrial Communications for
 EtherCAT software provides support for hardware
 configured as EtherCAT MainDevices.

The following table lists the supported hardware configured as EtherCAT MainDevices
 and the earliest supported version of the NI-Industrial Communications for
 EtherCAT.

| EtherCAT MainDevice | Earliest Supported Version | Latest Supported Version |
| --- | --- | --- |
| All PXIe controllers with NI Linux Real-Time with the PXIe-8245 or PXIe-8246 Ethernet interfaces | 21.3 | Current |
| All real-time embedded PXI controllers with the PXI-8231 or PXI-8232 Ethernet interface | 2.0 | 2023 Q3 |
| cDAQ-9132RT | 14.0 | Current |
| cDAQ-9133RT | 14.5 | Current |
| cDAQ-9134RT | 14.0 | Current |
| cDAQ-9135RT | 14.5 | Current |
| cDAQ-9136RT | 15.0 | Current |
| cDAQ-9137RT | 15.0 | Current |
| cRIO-902x | 1.2 | 20.0 |
| cRIO-9030 | 14.0 | Current |
| cRIO-9031 | 14.0 | Current |
| cRIO-9032 | 16.0 | Current |
| cRIO-9033 | 14.0 | Current |
| cRIO-9034 | 14.5 | Current |
| cRIO-9035 | 14.5 | Current |
| cRIO-9035 (Sync) | 16.0 | Current |
| cRIO-9036 | 14.5 | Current |
| cRIO-9037 | 16.0 | Current |
| cRIO-9038 | 14.5 | Current |
| cRIO-9039 | 14.5 | Current |
| cRIO-9039 (Sync) | 16.0 | Current |
| cRIO-904x | 17.6 | Current |
| cRIO-905x | 18.0 | Current |
| cRIO-9064 | 14.5 | Current |
| cRIO-9065 | 14.5 | Current |
| cRIO-9067 | 14.0 | Current |
| cRIO-9068 | 2.6 | Current |
| cRIO-907x | 1.0 | 20.0 |
| cRIO-9081 | 2.2 | 20.0 |
| cRIO-9082 | 2.2 | 20.0 |
| CVS-1458RT | 15.0 | Current |
| IC-3171 | 16.0 | Current |
| IC-3172 | 16.0 | Current |
| IC-3173 | 16.0 | Current |
| PCI-8232 | 2.0 | 2023 Q3 |
| PCIe-8231 | 2.0 | 2023 Q3 |
| PCIe-8233 | 2.0 | 2023 Q3 |
| PCIe-8235 | 2.0 | 2023 Q3 |
| PXI-8104 | 1.0 | 2023 Q3 |
| PXI-8106 | 1.0 | 2023 Q3 |
| PXI-8108 | 1.01 | 2023 Q3 |
| PXI-8109 | 2.5 | 2023 Q3 |
| PXI-8115 | 2.5 | 2023 Q3 |
| PXI-8119 | 14.0 | 2023 Q3 |
| PXI-8840 | 14.0 | 2023 Q3 |
| PXIe-8115 | 2.5 | 2023 Q3 |
| PXIe-8119 | 14.0 | 2023 Q3 |
| PXIe-8130 | 1.0 | 2023 Q3 |
| PXIe-8133 | 2.0 | 2023 Q3 |
| PXIe-8135 | 2.5 | 2023 Q3 |
| PXIe-8840 | 14.0 | 2023 Q3 |
| PXIe-8840 Quad-Core with NI Linux Real-Time | 18.5 | Current |
| PXIe-8842 | 2025 Q2 | Current |
| PXIe-8861 with NI Linux Real-Time | 19.0 | Current |
| PXIe-8862 | 2025 Q2 | Current |
| PXIe-8880 | 14.0 | 2023 Q3 |
| PXIe-8880 with NI Linux Real-Time | 18.5 | Current |
| PXIe-8881 | 21.5 | Current |
| RMC-8354RT | 2.5 | 2023 Q3 |
| RMC-8355RT | 2.5 | 2023 Q3 |
| sbRIO-9603 | 20.0 | Current |
| sbRIO-9605 | 1.1 | 20.0 |
| sbRIO-9606 | 1.1 | 20.0 |
| sbRIO-9607 | 15.0 | Current |
| sbRIO-9608 | 20.0 | Current |
| sbRIO-9609 | 20.0 | Current |
| sbRIO-9623 | 1.2 | 20.0 |
| sbRIO-9626 | 1.2 | 20.0 |
| sbRIO-9627 | 15.0 | Current |
| sbRIO-9628 | 20.0 | Current |
| sbRIO-9629 | 20.0 | Current |
| sbRIO-9633 | 2.2 | 20.0 |
| sbRIO-9636 | 2.2 | 20.0 |
| sbRIO-9638 | 20.0 | Current |
| sbRIO-9651 | 14.0 | Current |

Note

Note

Note

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=troubleshooting.html language=enus -->
## TOPIC 00045: Troubleshooting NI-Industrial Communications for EtherCAT

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/troubleshooting.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: Why Does an EtherCAT I/O Variable Return an Error? The error might occur if the related SubDevice or the module is disconnected. To find the error description, complete the following steps: In LabVIEW, select Help Explain Error to display the Explain Error dialog box. Enter the I/O variable error co

### Troubleshooting NI-Industrial Communications for
 EtherCAT

#### Why Does an EtherCAT I/O Variable
 Return an Error?

The error might occur if the related SubDevice or the module is
 disconnected.

To find the error description, complete the following steps:

1. In LabVIEW, select Help»Explain Error to display the Explain Error dialog
 box.
2. Enter the I/O variable error code to display the error description.

#### Why Does an EtherCAT I/O Variable
 Still Return an Error after I Reconnect a SubDevice or Module?

You can enable a reconnected SubDevice and module using one of the following
 methods.

- Click Clear Error on the EtherCAT:Online
 State page of the Online Slave Device State 
 dialog box. If you are trying to reconnect the reference clock while using
 the distributed clock, clearing the error is not efficient. To restore
 synchronization across your network with a distributed clock, complete the
 following steps:
  1. Switch the NI Scan Engine to the Configuration mode.
  2. Switch the NI Scan Engine to the Active mode.
- Clear the device error by changing the mode of the NI Scan Engine. To change the
 mode manually, complete the following steps: You can change the mode programmatically with the Set Scan
 Engine Mode VI in the Measurement I/O»NI Scan Engine palette.
  1. In the LabVIEW project explorer, right-click the target item and select Utilities»Scan Engine Mode»Switch to Configuration .
  2. Right-click the target item and select Utilities»Scan Engine Mode»Switch to Active .

#### What Is the Relationship between
 the NI Scan Engine Mode, EtherCAT MainDevice State, and EtherCAT SubDevice
 State? How Can I Change Their States?

Refer to *NI-Industrial Communications for EtherCAT and the NI Scan
 Engine* for information on the relationship between the NI Scan Engine
 mode and the EtherCAT state.

Refer to *EtherCAT SubDevice State Transition* for information on
 how to change an EtherCAT SubDevice state.

Refer to *NI Scan Engine Mode Transition* for information on how to change
 the NI Scan Engine mode.

#### Why Cannot I Install EtherCAT on the PXI Real-Time Target?

Configure the LabVIEW Real-Time target in MAX.

Related concepts:

- NI-Industrial Communications for EtherCAT and the NI Scan Engine
- EtherCAT SubDevice State Transition

Related tasks:

- NI Scan Engine Mode Transition

Related information:

- EtherCAT:Online:State Page
- Online Device State Dialog Box

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=uploading-an-ethercat-configuration.html language=enus -->
## TOPIC 00046: Uploading an EtherCAT Configuration

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `uploading-an-ethercat-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/uploading-an-ethercat-configuration.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to upload the EtherCAT network configuration from the real-time target. Right-click the controller item in the LabVIEW Project Explorer and select Utilities Compare Project & System to display the Project & System Comparison dialog box. Select the EtherCAT MainDevice ite

### Uploading an EtherCAT Configuration

Complete the following steps to upload the EtherCAT network configuration from the
 real-time target.

1. Right-click the controller item in the LabVIEW Project
 Explorer and select Utilities»Compare Project & System to display the Project & System
 Comparison dialog box.
2. Select the EtherCAT MainDevice item in the right Target
 column and click Upload.
3. Click Apply Changes.

Note

Parent topic:

Configuring the EtherCAT Network

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=user-defined-variable.html language=enus -->
## TOPIC 00047: User-Defined Variable

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `user-defined-variable.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/user-defined-variable.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: User-defined variables transfer custom FPGA-processed data between an FPGA VI and an RT VI. On the NI-9145, you can transfer data between the FPGA targets and the real-time targets only by using user-defined variables. Refer to the LabVIEW FPGA Module User Manual for more information about transfe

### User-Defined Variable

User-defined variables transfer custom FPGA-processed data between an FPGA VI and an
 RT VI.

Note

LabVIEW FPGA Module User Manual

You can add user-defined I/O variables to the block diagrams of FPGA VIs and RT VIs running on
 the target. Use the variables to communicate between the FPGA on the NI-9145 and host
 real-time target. All I/O variables are unidirectional, so you must configure the
 direction of each user-defined I/O variable. Configure the direction as either
 FPGA to Host or Host to FPGA.

For example, you can acquire analog I/O data and perform an FFT on the data in an FPGA
 VI. Use an FPGA to Host I/O variable to transfer the processed data to a control loop in
 an RT VI. Then use a Host to FPGA I/O variable to transfer output data from the RT
 control loop back to the FPGA for output to the physical I/O channel.

Note

LabVIEW User Manual

Parent topic:

Programming the FPGA on the NI-9145

Related information:

- LabVIEW FPGA Module User Manual — Transferring Data between the
 FPGA and Host

<!--NI_TOPIC bundle=ni-industrial-communications-ethercat path=user-manual-welcome.html language=enus -->
## TOPIC 00048: NI-Industrial Communications for EtherCAT User Manual

- bundle_id: `ni-industrial-communications-ethercat`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-ethercat/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-industrial-communications-ethercat`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Industrial Communications for EtherCAT User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Rel

### NI-Industrial Communications for
 EtherCAT
 User Manual

The NI-Industrial Communications for
 EtherCAT User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-Industrial Communications for EtherCAT
- NI-Industrial Communications for EtherCAT API Reference
- NI-Industrial Communications for EtherCAT and LabVIEW
 Compatibility
- EtherCAT® Expansion Chassis Vendor Configurations
 Guide
- NI-9145 Documentation
- ETG.1000.6: Application Layer Protocol Specification
- NI-Industrial Communications for EtherCAT Release Notes
- Interactive Activation Guide
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center
