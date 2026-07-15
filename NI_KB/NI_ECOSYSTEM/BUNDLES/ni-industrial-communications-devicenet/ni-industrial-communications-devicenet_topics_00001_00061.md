# NI DOCUMENT BUNDLE: ni-industrial-communications-devicenet

<!--NI_BUNDLE_CHUNK bundle=ni-industrial-communications-devicenet start=1 end=61 -->
<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=accessing-a-parameter.html language=enus -->
## TOPIC 00001: Accessing a Parameter

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `accessing-a-parameter.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/accessing-a-parameter.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can access a parameter value in one of the following ways: Access the parameter in the project data Use to edit the parameter value saved in the project. You can deploy the parameters to the target during deployment and write the data to the slave device when the NI Scan Engine changes to Active

### Accessing a Parameter

You can access a parameter value in one of the following ways:

Access the parameter in the project data

Active

Access the parameter in the device data

Note

Project
 Data, Scan Engine Data, and Device Data

#### Accessing a Parameter in the Project
 Data

1. Right-click the slave item and select Properties . The
 DeviceNet Slave Device Properties dialog box
 appears.
2. Switch to the DeviceNet Parameters to read and edit
 parameter values.

#### Accessing a Parameter in the Device Data

1. Right-click the slave item and select Utilities»Online Test
 Panel . The Online Test Panel dialog box
 appears.
2. Switch to the DeviceNet Parameters page.
3. In the Online Access section click the
 Read and Write buttons to
 access the device parameters.

Parent topic:

Configuring the DeviceNet Network

Related concepts:

- Project Data, Scan Engine Data, and Device Data

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=actions-that-load-or-unload-the-bit-file-on-t.html language=enus -->
## TOPIC 00002: Actions that Load or Unload the Bit File on the CompactRIO RT Controller

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `actions-that-load-or-unload-the-bit-file-on-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/actions-that-load-or-unload-the-bit-file-on-t.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following tables list the actions that cause NI-Industrial Communications for DeviceNet to load or unload the corresponding bit file on the real-time CompactRIO controller. The loading process causes a delay when you open a DeviceNet interface. The term DeviceNet-enabled FPGA VI refers to an FPG

### Actions that Load or Unload the Bit File on the CompactRIO RT Controller

The following tables list the actions that cause NI-Industrial Communications for
 DeviceNet to load or unload the corresponding bit file on the real-time CompactRIO
 controller. The loading process causes a delay when you open a DeviceNet interface.

The term DeviceNet-enabled FPGA VI refers to an *FPGA VI*
 compiled with a project that contains at least one NI-IndCom for DeviceNet module. The
 term DeviceNet-disabled FPGA VI refers to an FPGA VI compiled with no
 NI-IndCom for DeviceNet modules.

| Action | Description |
| --- | --- |
| Invoke the Open FPGA VI Reference function with a DeviceNet-enabled FPGA VI. | NI-IndCom for DeviceNet loads regardless of whether you select the Run the FPGA VI checkbox in the configuration dialog box. |
| Run a DeviceNet-enabled FPGA VI using interactive front panel communication. |  |

Note

| Action | Description |
| --- | --- |
| Invoke the Close FPGA VI Reference function. The default shortcut option is Close and Reset if Last Reference. | NI-IndCom for DeviceNet remains loaded when you do not close this reference. Shortcut options Close and Close and Abort without Reference Counting do not unload NI-IndCom for DeviceNet. |
| Power down CompactRIO. |  |
| Run a DeviceNet-disabled FPGA VI. | NI-IndCom for DeviceNet unloads when you use the Open FPGA VI Reference function or interactive front panel communication. |
| Invoke Reset using the Invoke Method node of the FPGA Interface. | A reset of an open FPGA reference causes NI-IndCom for DeviceNet to unload, and then immediately load again. If you are using NI-IndCom for DeviceNet interfaces during the reset, the interfaces becomes invalid. Other methods such as Abort do not unload NI-IndCom for DeviceNet. |
| Run a different DeviceNet-enabled FPGA VI from the DeviceNet-enabled FPGA VI currently loaded. | When you change FPGA VIs, the effect is the same as the reset method. NI-IndCom for DeviceNet unloads, and then immediately loads again. |

Note

Related concepts:

- Waiting to Detect Interfaces
- Running an FPGA VI to Load DeviceNet

Related information:

- Open DeviceNet Interface VI

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=add-fpga-target-9882.html language=enus -->
## TOPIC 00003: Adding an FPGA Target and the NI-9882 Module to the LabVIEW Project

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `add-fpga-target-9882.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/add-fpga-target-9882.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: To compile an FPGA VI with the required communication logic, add the NI-9882 module to the LabVIEW project. Adding an FPGA Target Add a controller to the LabVIEW project. If the controller is online: right-click the project item, select New»Targets and Devices»Existing target or device from the shor

### Adding an FPGA Target and the NI-9882 Module to the LabVIEW Project

To compile an FPGA VI with the required communication logic, add the NI-9882 module to the LabVIEW project.

#### Adding an FPGA Target

1. Add a controller to the LabVIEW project.
  - If the controller is online: right-click the project item, select
 New»Targets and Devices»Existing target or
 device from the shortcut menu, and select the controller
 under Ethernet RIO , Real-Time
 CompactRIO or Real-Time Single-Board
 RIO .
  - If the controller is offline: select New target or
 device to add a chassis.
2. When you add the controller, if LabVIEW displays the Select
 Programming Mode dialog box, select LabVIEW FPGA
 Interface as the chassis mode to support compilation of an FPGA
 VI. Note If
 LabVIEW displays the Discover C Series Modules?
 dialog box, click the Do Not Discover button.
3. If LabVIEW reports that LabVIEW FPGA is not supported, ignore this error message
 and click Continue .
4. If the controller is online, LabVIEW adds the FPGA target automatically. If the
 controller is offline, add the FPGA target by right-clicking the chassis item
 under the controller, and select New»FPGA Target . Then
 proceed to the Adding the NI 9882 Module for DeviceNet section of this
 topic.

#### Adding the NI-9882
 Module for DeviceNet

1. Right-click the chassis item under the controller, not under FPGA. Select
 New»C Series Modules»Existing target or device from
 the shortcut menu.
2. Expand the C Series Module tree and select the
 NI-9882 module that you want to use. If you have
 multiple NI-9882 modules, hold the
 <Shift> key to select the modules that you want to
 use from this tree.
3. Click OK to add the modules to the project.
4. (Optional) You can also add NI-9882 modules
 offline by right-clicking the chassis item under the controller and selecting
 New»C Series Modules»New target or device from the
 shortcut menu. Select C Series Module in the
 Add Targets and Devices on Chassis dialog box. In the
 New C Series Module dialog box, select
 NI-9882 from the Type 
 pull-down menu and select an appropriate slot from the
 Location pull-down menu.

Note

NI-Industrial Communications for
 DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-devicenet-master-slave.html language=enus -->
## TOPIC 00004: Adding a DeviceNet Master and Connected Slave Devices

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-devicenet-master-slave.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-devicenet-master-slave.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: To add a DeviceNet master and connected Slave devices to the LabVIEW project, complete the following steps . If you only want to use DeviceNet VIs, you only need to complete Step 1 and start using the VIs. Installing the DeviceNet Interface Card on the Host Right-click My Computer and choose Propert

### Adding a DeviceNet Master and Connected Slave
 Devices

Note

Step 1

#### Installing the DeviceNet Interface Card on the Host

1. Right-click My Computer and choose
 Properties , switch to Scan
 Engine page, and select the Start Scan Engine on
 Deploy checkbox.
2. Right-click My Computer in the LabVIEW Project Explorer
 and select New»Targets and Devices to display the
 Add Targets and Devices dialog box. Then go to the
 Common Steps section of current topic.

#### Installing the DeviceNet Interface Card on the NI
 Real-Time Controller

1. Launch LabVIEW. Create a new empty project by selecting Empty
 Project under the new heading. Save this project using the name
 desired, for example, DeviceNet.lvproj .
2. Add the controller you want to use to this empty project and right-click the
 controller item and select Connect to connect the
 controller.
3. Right-click the controller item in the LabVIEW Project Explorer and select
 New»Targets and Devices to display the Add
 Targets and Devices dialog box. Then go to the Common Steps
 section of current topic.

#### Common Steps

1. Expand the DeviceNet Master Interface category to view
 the available DeviceNet masters. Note If you do not find any
 master interface available, make sure that you have an NI-DeviceNet hardware
 interface card installed.
2. Select an available DeviceNet master interface and click
 OK to display the Master
 Settings dialog box.
3. Keep the default options and click OK to add the master
 and connected slave devices automatically.
4. You can see the new items in the LabVIEW Project Explorer. If you cannot see the
 connected slave devices in the project tree, make sure that you connect the
 DeviceNet slave devices to the DeviceNet network.
5. DeviceNet master —A DeviceNet master interface.
6. DeviceNet slave —A DeviceNet slave device.

Parent topic:

Getting Started with NI I/O Variable and Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-editing-removing-a-devicenet-i-o-varia.html language=enus -->
## TOPIC 00005: Adding/Editing/Removing a DeviceNet I/O Variable

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-editing-removing-a-devicenet-i-o-varia.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-editing-removing-a-devicenet-i-o-varia.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following operations on the DeviceNet I/O variables: Adding a DeviceNet I/O Variable Editing a DeviceNet I/O Variable Removing a DeviceNet I/O Variable Adding a DeviceNet I/O Variable Complete the following steps to add an I/O variable. Right-click the slave item and select Confi

### Adding/Editing/Removing a DeviceNet I/O Variable

You can perform the following operations on the DeviceNet I/O variables:

- Adding a DeviceNet I/O Variable
- Editing a DeviceNet I/O Variable
- Removing a DeviceNet I/O Variable

#### Adding a DeviceNet I/O Variable

Complete the following steps to add
 an I/O variable.

1. Right-click the slave item and select Configure I/O from the
 shortcut menu.
2. Select the variable direction (Input or Output) from the
 Variables list.
3. Click the Add button to open the I/O Item Editor 
 dialog box.
4. Set the I/O item name and data type. Adjust the location of the I/O item by clicking the
 Move Up or Move Down button.
5. Click OK to exit the I/O Item Editor 
 dialog box.
6. (Optional) Repeat this process from step 2 to step 5 to add other variables.
7. Click OK to exit the Property dialog
 box.

#### Editing a DeviceNet I/O Variable

Complete the following steps to edit the DeviceNet properties of an I/O variable.

1. Right-click the slave item, select Properties and switch to the
 DeviceNet:I/O Configuration page. Or, you can select
 Configure I/O from the shortcut menu to access this page.
2. Select the I/O variable item you want to edit from the Variables 
 list.
3. Click the Edit button to open the I/O Item
 Editor dialog box and edit the I/O item name and data type. You also can
 adjust the location of the I/O variable by clicking the Move Up or
 Move Down button.
4. Click OK to exit the I/O Item Editor dialog
 box.
5. (Optional) Repeat this process from step 2 to step 4 to edit other variables.
6. Click OK to exit the property dialog box.

Complete the following steps to edit the general properties of an I/O
 variablean.

1. Right-click an I/O variable item and select Properties .
2. Edit the properties in the I/O Variable Properties dialog box.
3. Click OK to exit the property dialog box.

#### Removing a DeviceNet I/O Variable

Complete the following steps to
 remove an I/O variable.

1. Right-click the slave item, select Properties and switch to the
 DeviceNet:I/O Configuration page. You can also right-click and
 select Configure I/O from the shortcut menu to access this
 page.
2. Select the I/O variable item you want to remove from the
 Variables list.
3. Click the Remove button.
4. (Optional) Repeat this process from step 2 to step 3 to edit other variables.
5. Click OK to close the property dialog box.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-editing-removing-a-devicenet-master-it.html language=enus -->
## TOPIC 00006: Adding/Editing/Removing a DeviceNet Master Item

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-editing-removing-a-devicenet-master-it.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-editing-removing-a-devicenet-master-it.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following operations on the DeviceNet Master item: Add a DeviceNet master item Edit a DeviceNet master item Remove a DeviceNet master item Adding a Discovered DeviceNet Master Item Right-click the host or real-time target and select New»Targets and Devices to display the Add Targ

### Adding/Editing/Removing a DeviceNet Master Item

You can perform the following operations on the DeviceNet Master item:

- Add a DeviceNet master item
- Edit a DeviceNet master item
- Remove a DeviceNet master item

#### Adding a Discovered DeviceNet Master Item

1. Right-click the host or real-time target and select New»Targets and Devices to display the Add Targets and Devices dialog box.
2. Select Existing target or device .
3. Expand DeviceNet Master Interface and select the master you want to add into the project.
4. Click OK to confirm the setting. The Master Setting dialog box appears.
5. Select the MAC ID and Baud Rate for the master.
6. Select whether you want to discover devices immediately after you add the master.
7. Click OK to close the dialog box.

#### Adding a Specified DeviceNet Master
 Item

1. Right-click the host or real-time target and select New»Targets and
 Devices to display the Add Targets and
 Devices dialog box.
2. Select New Target or Device .
3. Select DeviceNet Master Interface .
4. Click OK to confirm the setting. The Master
 Setting dialog box appears.
5. Select the Master Interface , MAC
 ID , and Baud Rate for the master.
6. Select whether you want to discover devices immediately after you add the
 master.
7. Click OK to close the dialog box.

#### Editing a DeviceNet Master Item

1. Right-click the master in the project tree, select
 Properties from the shortcut menu to display the
 DeviceNet Master Interface Properties dialog box.
  - Select General to show the General 
 page and edit the Name and Physical
 Interface .
  - Select DeviceNet:Basic to show the
 DeviceNet:Basic page and edit the MAC
 ID and Baud Rate .
  - Select DeviceNet:I/O Configuration to show the
 DeviceNet:I/O Configuration page and edit the poll mode
 of the master.
2. Click OK to confirm the change and close the dialog
 box.

#### Removing a DeviceNet Master Item

1. Select the master you want to remove.
2. Right-click the item and select Remove from Project from
 the shortcut menu.
3. Click OK in the Remove Items 
 dialog box to confirm the change.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-editing-removing-a-devicenet-slave-dev.html language=enus -->
## TOPIC 00007: Adding/Editing/Removing a DeviceNet Slave Device

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-editing-removing-a-devicenet-slave-dev.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-editing-removing-a-devicenet-slave-dev.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following operations on the DeviceNet slave item: Add a DeviceNet slave item Edit a DeviceNet slave item Remove a DeviceNet slave item Adding a DeviceNet Slave Item Add a slave device item in one of the following ways: Adding a discovered DeviceNet slave Item Complete the followi

### Adding/Editing/Removing a DeviceNet Slave Device

You can perform the following operations on the DeviceNet slave item:

- Add a DeviceNet slave item
- Edit a DeviceNet slave item
- Remove a DeviceNet slave item

Adding a DeviceNet Slave Item

Add a slave device item in one of the following ways:

#### Adding a discovered DeviceNet slave
 Item

Complete the following steps to add a discovered DeviceNet slave.

1. Right-click the master item and select New»Targets and
 Devices to show the Add Targets and
 Devices dialog box.
2. Select Existing target or device .
3. Expand DeviceNet Slave Device and select the slave device
 you want to add into the project.
4. Click OK to confirm the setting.

#### Adding a Specified DeviceNet Slave
 Item

Complete the following steps to add a specified DeviceNet slave.

1. Right-click the master item and select New»Targets and
 Devices to show the Add Targets and
 Devices dialog box.
2. Select New Target and Device . Click
 OK to confirm the setting.
3. Slave Setting dialog box appears. Set the
 Address and Data Sheet for the
 device.
4. Click OK .

#### Editing a DeviceNet Slave Item

Complete the following steps to edit a DeviceNet Device:

1. Right-click the slave device item in the project tree and select
 Properties from the shortcut menu to display the
 DeviceNet Slave Device Properties dialog box.
  - Select General to show the General 
 page.
  - Select DeviceNet:Basic to show the
 DeviceNet:Basic page.
  - Select DeviceNet:Option to show the
 DeviceNet:Option page.
  - Select DeviceNet:Parameters to show the
 DeviceNet:Parameters page.
  - Select DeviceNet:I/O Configuration to show the
 DeviceNet:I/O Configuration page.
2. Click OK to confirm the change and close the dialog
 box.

#### Removing a DeviceNet Slave Item

Complete the following steps to remove a DeviceNet Slave.

1. Select the slave item you want to remove.
2. Right-click the item and select Remove from Project from
 the shortcut menu.
3. Click OK in the Remove Items 
 dialog box to confirm the change.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-editing-removing-a-real-time-controlle.html language=enus -->
## TOPIC 00008: Adding/Editing/Removing a Real-Time Controller

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-editing-removing-a-real-time-controlle.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-editing-removing-a-real-time-controlle.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform the following operations for a real-time controller: Add a Real-Time Controller Edit a Real-Time Controller Remove a Real-Time Controller Complete the following procedures to add, edit, or remove a real-time controller. Adding a Discovered Real-Time Controller Right-click the Project

### Adding/Editing/Removing a Real-Time Controller

You can perform the following operations for a real-time controller:

- Add a Real-Time Controller
- Edit a Real-Time Controller
- Remove a Real-Time Controller

Complete the following procedures to add, edit, or remove a real-time controller.

#### Adding a Discovered Real-Time Controller

1. Right-click the Project item and select New»Targets and Devices . The Add Targets and Devices dialog box appears.
2. Select Existing target or device from the dialog box.
3. If you know the IP address of the real-time controller and select Specify a target or device by IP address , you can select Properties from the shortcut menu, switch to the General page, and enter the IP address. Otherwise, select Discover an existing target(s) or device(s) .
4. Select the type of your real-time controller from the Targets and Devices tree.
5. Click the OK button to add the target.

#### Adding a Specified Real-Time
 Controller

1. Right-click the Project item and select
 New»Targets and Devices from the shortcut menu. The
 Add Targets and Devices dialog box appears.
2. Select New target or device from the dialog box.
3. Select the type of your real-time controller from the Targets and
 Devices tree.
4. Click the OK button to add the target.

#### Editing a Real-Time Controller

1. Right-click the real-time target and select Properties 
 from the shortcut menu.
2. Edit the properties of this target.
3. Click OK to confirm the changes.

#### Removing a Real-Time Controller

1. Select the real-time controller which you want to remove.
2. Right-click the item and select Remove from Project. from
 the shortcut menu
3. Click OK in the Remove Items 
 dialog box to confirm the change.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=adding-rt-controller.html language=enus -->
## TOPIC 00009: Adding a Real-Time Controller

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `adding-rt-controller.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/adding-rt-controller.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use an NI real-time controller, you can begin to configure the system after preparing the hardware and software. If you only want to use DeviceNet VIs, you can start using the VIs after completing Step 1 without completing the following steps. To add an NI real-time controller to a LabVIEW

### Adding a Real-Time Controller

Note

To add an NI real-time controller to a LabVIEW project, complete the following steps.

1. Launch LabVIEW. Create a new empty project by selecting Empty Project under the new heading. Save this project using the name desired, for example, DeviceNet.lvproj .
2. In the LabVIEW Project Explorer, right-click the Project root item and select New»Targets and Devices to display the Add Targets and Devices dialog box.
3. Expand the related controller category to access the online controller. For a PXI controller, expand the Real-Time PXI category. If no controller is listed under the category, ensure that your controller is connected to your host.
4. Select your controller and click OK .

Parent topic:

Getting Started with NI I/O Variable and Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=assigning-or-changing-a-device-datasheet.html language=enus -->
## TOPIC 00010: Assigning or Changing a Device Datasheet

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `assigning-or-changing-a-device-datasheet.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/assigning-or-changing-a-device-datasheet.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must assign a device datasheet file to a slave device before editing parameters and retrieving the description of the I/O connection. Assigning or Changing a Datasheet to a New Device When you add a DeviceNet slave device, click the Browse button in the DeviceNet Slave Settings dialog box to loc

### Assigning or Changing a Device Datasheet

You must assign a device datasheet file to a slave device before editing parameters and
 retrieving the description of the I/O connection.

#### Assigning or Changing a Datasheet to a New Device

When you add a DeviceNet slave device, click the
 Browse button in the DeviceNet Slave
 Settings dialog box to locate and assign the datasheet.

#### Assigning or Changing a Datasheet to an Existing
 Device

Complete the following steps to change or assign a datasheet to an
 existing device.

1. Right-click the DeviceNet slave and select Datasheet . The
 Datasheet dialog box will appear.
2. Select the datasheet in Data Sheet List . When you select
 a data sheet, the related information is shown in Data Sheet
 Information .
3. Click OK to assign the selected datasheet to the slave
 device and exit the dialog box.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=cabling.html language=enus -->
## TOPIC 00011: Cabling

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `cabling.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/cabling.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Cabling RequirementsCables meet the requirements of the DeviceNet Specification. Belden cable (3084A) is suitable for most applications. Cable Length The characteristics of the cabling and the desired bit transmission rates affect the allowable cable length. Detailed cable length requirements are av

### Cabling

#### Cabling Requirements

Cables meet the
 requirements of the *DeviceNet Specification*.

Belden cable
 (3084A) is suitable for most applications.

#### Cable Length

The characteristics of the
 cabling and the desired bit transmission rates affect the allowable cable length.
 Detailed cable length requirements are available in the *DeviceNet
 Specification*. The following table provides DeviceNet cable length
 specifications.

| Baud Rate | Trunk Length | Drop Length Maximum | Drop Length Cumulative |
| --- | --- | --- | --- |
| 500 Kb/s | 100 m (328 ft) | 6 m (20 ft) | 39 m (128 ft) |
| 250 Kb/s | 250 m (820 ft) | 6 m (20 ft) | 78 m (256 ft) |
| 125 Kb/s | 500 m (1,640 ft) | 6 m (20 ft) | 156 m (512 ft) |

#### Maximum Number of Devices

The maximum
 number of devices that you can connect to a DeviceNet port depends on the electrical
 characteristics of the devices on the network. If all of the devices on the network
 meet the DeviceNet specifications, you can connect 64 devices to the network.

#### Connectors

DeviceNet hardware has a D-Sub terminal connector.

Figure 1.

[IMAGE alt='9-Pin D-Sub Connector' src='GUID-6BC02CE2-AE9D-4650-95F6-79B9E4BB95E3-a5.gif']

| Signal | Description |
| --- | --- |
| NC | No connection. |
| CAN_L | CAN_L bus line. |
| V- | CAN reference ground. |
| NC | No connection. |
| (SHLD) | Optional CAN shield. |
| (COM) | Optional CAN reference ground. |
| CAN_H | CAN_H bus line. |
| NC | No connection. |
| (V+) | Also referred to as Ext_Vbat, this is an optional CAN power supply if you already have bus power/external VBAT. |

#### 5-Pin Combicon Connector

Some DeviceNet devices, including older DeviceNet hardware products such as PCI-DNET,
 PCMCIA-DNET, and PXI-8461/D, use a Combicon-style pluggable screw terminal
 connector. The 5-pin Combicon-style pluggable screw terminal follows the pinouts as
 the *DeviceNet Specification* requires. The following figure shows the
 pinouts for this connector.

Figure 2.

[IMAGE alt='5-Pin Combicon Connector' src='GUID-110BD4E4-7DD1-4BEC-873E-197790D12B96-a5.gif']

1. V—
2. CAN_L
3. GND
4. CAN_H
5. V+

| Signal Name | Description |
| --- | --- |
| V— | CAN reference ground. |
| CAN_L | CAN_L bus line. |
| GND | Ground |
| CAN_H | CAN_H bus line. |
| (V+) | Also referred to as Ext_Vbat, this is an optional CAN power supply if you already have bus power/external VBAT. |

#### Bus Power Requirements

For the supported
 DeviceNet products, the physical layer is completely powered internally. You do not
 need to supply bus power using V+ and V-.

Some DeviceNet devices, including
 old DeviceNet hardware products, require a bus power supply. The following table
 provides power requirements. Reference these requirements to determine the
 requirements of the bus power supply for the system.

| Characteristic | Specification |
| --- | --- |
| Voltage Requirement | 10 to 30 VDC |
| Current Requirement | 40 mA typical, 100 mA maximum |

#### Termination

The pair of signal wires (CAN_H and CAN_L)
 constitutes a transmission line. If the transmission line is not terminated, each
 signal change on the line causes reflections that may cause communication
 failures.

Because communication flows both ways on the DeviceNet bus,
 DeviceNet requires that you need to terminate both ends of the cable. However, this
 requirement does not mean that every device has a termination resistor. If multiple
 devices are placed along the cable, only the devices on the ends of the cable should
 have termination resistors.

The termination resistors on a cable match the
 nominal impedance of the cable. DeviceNet requires a cable with a nominal impedance
 of 120 Ω; therefore, a 120
 Ω resistor is at each end of the cable. Each termination resistor can
 dissipate at least 0.25 W of power.

#### Cabling Examples

The following figure
 shows a cable connecting two DeviceNet devices.

Figure 3.

[IMAGE alt='Cable Connecting Two DeviceNet Devices' src='GUID-E1B4C533-1224-4F3A-8E10-8409B78DC321-a5.gif']

The following picture shows an example of where termination resistors are in a
 system with more than two devices.

Figure 4.

[IMAGE alt='Termination Resistors Location' src='GUID-DD23D8EB-B2B1-42EA-9AED-903288004478-a5.gif']

Parent topic:

DeviceNet Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=changing-a-slave-device-address.html language=enus -->
## TOPIC 00012: Changing a Slave Device Address

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `changing-a-slave-device-address.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/changing-a-slave-device-address.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to change the address of a slave device. Right-click the DeviceNet master item and select Utilities»Change Slave Address. The Change Slave Address dialog box appears. Select the device you want to change from the Device List list. Select the new address you want to set f

### Changing a Slave Device Address

Complete the following steps to change the address of a slave device.

1. Right-click the DeviceNet master item and select Utilities»Change Slave Address . The Change Slave Address dialog box appears.
2. Select the device you want to change from the Device List list.
3. Select the new address you want to set from the New Address list.
4. Click Apply to confirm the change. The Change Slave
 Address dialog box displays the result of the operation.

After the device address change succeeds the address of the related slave item changes automatically.

device
 data

DeviceNet:Basic Page

project data

Note

Online Test Panel

Parent topic:

Configuring the DeviceNet Network

Related concepts:

- Project Data, Scan Engine Data, and Device Data

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=changing-a-slave-device-baud-rate.html language=enus -->
## TOPIC 00013: Changing a Slave Device Baud Rate

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `changing-a-slave-device-baud-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/changing-a-slave-device-baud-rate.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to change the baud rate of a slave device. Right-click the DeviceNet master item and select Utilities»Change Slave Baud Rate. The Change Slave Baud Rate dialog box appears. Select the device you want to change from the Device List list. Select the new baud rate you want

### Changing a Slave Device Baud Rate

Complete the following steps to change the baud rate of a slave device.

1. Right-click the DeviceNet master item and select Utilities»Change Slave Baud
 Rate . The Change Slave Baud Rate dialog box
 appears.
2. Select the device you want to change from the Device List list.
3. Select the new baud rate you want to set from the New Baud Rate list.
4. Click Apply to confirm the change. The Change Slave Baud
 Rate dialog box displays the result of the operation.
5. If the baud rate change is successful, you need to circulate power or re-connect the slave device to enable the baud rate change.

Note

Online Test Panel

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=changing-the-scan-period.html language=enus -->
## TOPIC 00014: Changing the Scan Period

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `changing-the-scan-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/changing-the-scan-period.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The scan period is the period of the NI Scan Engine, and the DeviceNet I/O variable updates according to this period. If you use DeviceNet VIs, you do not need to configure the NI Scan Engine. Change the scan period according to your needs. Complete the following steps to change the scan period: Rig

### Changing the Scan Period

The scan period is the period of the NI Scan Engine, and the DeviceNet I/O variable updates
 according to this period. If you use DeviceNet VIs, you do not need to configure the NI
 Scan Engine. Change the scan period according to your needs. Complete the following
 steps to change the scan period:

1. Right-click the target item and select Properties from the shortcut menu. The Target Properties dialog box appears.
2. Switch to the Scan Engine page and change the scan period.
3. Click OK to close the dialog box.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=comparing-the-devicenet-configurations.html language=enus -->
## TOPIC 00015: Comparing the DeviceNet Configurations

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `comparing-the-devicenet-configurations.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/comparing-the-devicenet-configurations.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can compare the project data and the scan engine data. Complete the following steps to compare the DeviceNet network configuration in the LabVIEW project with the configuration on the target. Right-click the target item in the LabVIEW Project Explorer and select Utilities»Compare Project & Syste

### Comparing the DeviceNet Configurations

You can compare the project data and the scan engine data.

Complete the following steps to compare the DeviceNet network configuration in the LabVIEW project with the configuration on the target.

1. Right-click the target item in the LabVIEW Project Explorer and select Utilities»Compare Project & System to display the Project & System Comparison dialog box.
2. Compare the differences between the related DeviceNet items.

If an item icon has a red overlay on the top right side, the item settings in the project differ from the settings in the target. The Conflict Message box displays the detailed conflict information. If you have multiple conflict messages, use Previous Diff and Next Diff to switch them.

You may cause a configuration conflict in the following operations:

- You do not deploy the target, so you do not have any DeviceNet settings on the target. Deploy the items to the target.
- Your project is empty. Upload the DeviceNet items from the target to the project.
- The same items are in the project and target, but settings such as the name or properties are different. Deploy the project settings or upload the target settings.
- You have some obsolete DeviceNet item settings on the target. Undeploy these obsolete items from the target.

#### Deploying, Uploading, and Undeploying DeviceNet
 Items

Complete the following steps to deploy, upload, or undeploy
 DeviceNet items.

1. Select the DeviceNet items in the Project window and click
 Deploy , Upload , or
 Undeploy accordingly to mark the items as
 Deploy , Upload , or
 Undeploy .
2. Click Apply .

Parent topic:

Configuring the DeviceNet Network

Related concepts:

- Project Data, Scan Engine Data, and Device Data

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=configuring-the-devicenet-network.html language=enus -->
## TOPIC 00016: Configuring the DeviceNet Network

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `configuring-the-devicenet-network.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/configuring-the-devicenet-network.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Industrial Communications for DeviceNet provides the following features to help you configure a DeviceNet network.

### Configuring the DeviceNet Network

NI-Industrial Communications for DeviceNet provides the following features to help you configure a DeviceNet network.

- [Adding/Editing/Removing a Real-Time Controller](adding-editing-removing-a-real-time-controlle.html)
- [Adding/Editing/Removing a DeviceNet Master Item](adding-editing-removing-a-devicenet-master-it.html)
- [Adding/Editing/Removing a DeviceNet Slave Device](adding-editing-removing-a-devicenet-slave-dev.html)
- [Adding/Editing/Removing a DeviceNet I/O Variable](adding-editing-removing-a-devicenet-i-o-varia.html)
- [Enabling the NI Scan Engine on Windows](enabling-the-ni-scan-engine-on-windows.html)
- [Changing the Scan Period](changing-the-scan-period.html)
- [Deploying and Undeploying a DeviceNet Configuration](deploying-and-undeploying-a-devicenet-configu.html)
- [Uploading a DeviceNet Configuration](uploading-a-devicenet-configuration.html)
- [Comparing the DeviceNet Configurations](comparing-the-devicenet-configurations.html)
- [Accessing a Parameter](accessing-a-parameter.html)
- [Monitoring the Slave Device State](monitoring-the-slave-device-state.html)
- [Assigning or Changing a Device Datasheet](assigning-or-changing-a-device-datasheet.html)
- [Importing a Device Datasheet](importing-a-device-datasheet.html)
- [Changing a Slave Device Address](changing-a-slave-device-address.html)
- [Changing a Slave Device Baud Rate](changing-a-slave-device-baud-rate.html)

Parent topic:

Legacy

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=connection-type.html language=enus -->
## TOPIC 00017: Connection Type

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `connection-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/connection-type.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The connection type specifies the type of master/slave I/O connections. DeviceNet has the following connection types: Poll Master/slave I/O connection in which the master sends a poll command to a slave, and then receives a poll response from that slave. Strobe Master/slave I/O connection in which t

### Connection Type

The connection type specifies the type of master/slave I/O connections. DeviceNet has the following connection types:

Poll

Strobe

COS

Cyclic

DeviceNet Specification

- You cannot open two polled I/O connections for the same device.
- You can use multiple connections of different types for each device.

Note

Change-of-State (COS)

Cyclic

The NI-Industrial Communications for
 DeviceNet
 network acknowledges the COS and Cyclic I/O
 connections by default. To suppress acknowledgments for these I/O connections, wire a
 Boolean to set the COS/Cyclic Ack Suppress driver attribute of the attribute
 ID parameter in the Set Driver Attribute VI to
 TRUE before starting communication.

Parent topic:

DeviceNet Fundamentals

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=creating-app-devicenet-vis.html language=enus -->
## TOPIC 00018: Creating Applications by Using the DeviceNet VIs

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `creating-app-devicenet-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/creating-app-devicenet-vis.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use interfaces that are detected by NI-Industrial Communications for DeviceNet software. Use DeviceNet VIs to read and write data.

### Creating Applications by Using the DeviceNet
 VIs

You can use interfaces that are detected by NI-Industrial Communications for
 DeviceNet software. Use DeviceNet VIs to read
 and write data.

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=creating-app-w-devicenet-vis.html language=enus -->
## TOPIC 00019: Creating Applications by Using the DeviceNet VIs

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `creating-app-w-devicenet-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/creating-app-w-devicenet-vis.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use interfaces that are detected by NI-Industrial Communications for DeviceNet software. Use DeviceNet VIs to read and write data.

### Creating Applications by Using the DeviceNet
 VIs

You can use interfaces that are detected by NI-Industrial Communications for
 DeviceNet software. Use DeviceNet VIs to read and write
 data.

Parent topic:

Creating Applications on CompactRIO Targets with NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=creating-applications-on-crio-targets-w-rt.html language=enus -->
## TOPIC 00020: Creating Applications on CompactRIO Targets with NI Linux Real-Time

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `creating-applications-on-crio-targets-w-rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/creating-applications-on-crio-targets-w-rt.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create applications on CompactRIO targets with NI Linux Real-Time, complete the following steps.

### Creating Applications on CompactRIO Targets with NI Linux Real-Time

To create applications on CompactRIO targets with NI Linux Real-Time, complete the following
 steps.

1. Installing the Software on the Host
2. Installing NI-Industrial Communications for DeviceNet on the CompactRIO RT Controller
3. Creating Applications by Using the DeviceNet VIs

Parent topic:

Tutorial: Creating Applications on Different Types of Chassis and Controllers

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=creating-applications-on-crio-targets-wo-rt.html language=enus -->
## TOPIC 00021: Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `creating-applications-on-crio-targets-wo-rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/creating-applications-on-crio-targets-wo-rt.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module is required to create applications on CompactRIO targets with operating systems other than NI Linux Real-time. Use the LabVIEW FPGA Module to build and run an FPGA VI to establish communication between the NI-Industrial Communications for DeviceNet RT driver and the NI-9882 m

### Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

The LabVIEW FPGA Module is required to create applications on CompactRIO targets with
 operating systems other than NI Linux Real-time. Use the LabVIEW FPGA Module to build and run
 an FPGA VI to establish communication between the NI-Industrial Communications for
 DeviceNet RT
 driver and the NI-9882 module.

To create applications on CompactRIO targets with operating systems other than NI Linux
 Real-Time, complete the following steps.

1. Installing the Software on the Host
2. Installing NI-Industrial Communications for DeviceNet on the CompactRIO RT Controller 2
3. Adding an FPGA Target and the NI-9882 Module to the LabVIEW Project
4. Running an FPGA VI to Load DeviceNet
5. Waiting to Detect Interfaces
6. Creating Applications by Using the DeviceNet VIs

Parent topic:

Tutorial: Creating Applications on Different Types of Chassis and Controllers

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=creating-applications-on-pci-and-pxi.html language=enus -->
## TOPIC 00022: Creating Applications on PCI and PXI

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `creating-applications-on-pci-and-pxi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/creating-applications-on-pci-and-pxi.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Build the DeviceNet network using one of these methods: A DeviceNet network without an NI real-time controller Install the DeviceNet interface card on the host, such as a PCI device. A DeviceNet network with an NI real-time controller Install the DeviceNet interface card on a real-time controller, s

### Creating Applications on PCI and PXI

Build the DeviceNet network using one of these methods:

A DeviceNet network without an NI real-time controller

A DeviceNet network with an NI real-time controller

Use the DeviceNet VIs to develop your applications for PCI and PXI. To install the
 software on the host, complete the following steps.

1. Install the prerequisite software on the host according to the NI-Industrial Communications for DeviceNet Readme .
2. Install the NI-Industrial Communications for
 DeviceNet software on the host.
3. If you install the DeviceNet interface card on an NI real-time controller, install the NI-Industrial Communications for DeviceNet software on the real-time controller.

Parent topic:

Tutorial: Creating Applications on Different Types of Chassis and Controllers

Related concepts:

- Related Documentation

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=deploying-and-undeploying-a-devicenet-configu.html language=enus -->
## TOPIC 00023: Deploying and Undeploying a DeviceNet Configuration

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `deploying-and-undeploying-a-devicenet-configu.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/deploying-and-undeploying-a-devicenet-configu.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deploying a DeviceNet Configuration Deployment is the process through which you deploy the project data to the NI scan engine data. To deploy a DeviceNet configuration to the target, right-click DeviceNet master item and select Deploy from the shortcut menu. Undeploying a DeviceNet ConfigurationUnde

### Deploying and Undeploying a DeviceNet Configuration

#### Deploying a DeviceNet Configuration

Deployment is the process through which you deploy the project data to
 the NI scan engine data.

To deploy a DeviceNet configuration to the target,
 right-click *DeviceNet master item* and select
 Deploy from the shortcut menu.

#### Undeploying a DeviceNet
 Configuration

Undeployment is the process through which you remove the
 DeviceNet configuration data from the scan engine data. This process disconnects the
 DeviceNet interface from the DeviceNet network.

To remove a DeviceNet
 configuration from the target, right-click a DeviceNet master item and select
 Undeploy from the shortcut menu.

Parent topic:

Configuring the DeviceNet Network

Related concepts:

- Project Data, Scan Engine Data, and Device Data

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=developing-the-devicenet-application-in-labvi.html language=enus -->
## TOPIC 00024: Developing the DeviceNet Application in LabVIEW

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `developing-the-devicenet-application-in-labvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/developing-the-devicenet-application-in-labvi.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Develop the DeviceNet application in LabVIEW by using I/O controls, function blocks and I/O variables. The following topics describe DeviceNet application development: Read the Notice to Develop the DeviceNet Application in LabVIEW before developing DeviceNet applications in LabVIEW. Notice to Devel

### Developing the DeviceNet Application in LabVIEW

Develop the DeviceNet application in LabVIEW by using I/O controls, function blocks and I/O variables. The following topics describe DeviceNet application development:

Note

Notice to
 Develop the DeviceNet Application in LabVIEW

Parent topic:

Legacy

Related information:

- DeviceNet Explicit Message Function Block

#### Notice to Develop the DeviceNet Application in LabVIEW

Follow these requirements when developing DeviceNet applications in LabVIEW:

- If you install the DeviceNet interface in the Windows host, enable the Scan Engine in Windows .
- Use the Set Scan Engine Mode VI in the LabVIEW palette Measure
 I/O»NI Scan Engine to set the NI Scan Engine Mode to
 Active before using any DeviceNet I/O variables or VIs for your
 application.
- If your application VI only uses the DeviceNet VIs, deploy the configuration before running the
 VIs.

Related concepts:

- Enabling the NI Scan Engine on Windows
- NI Scan Engine Mode
- Deploying and Undeploying a DeviceNet Configuration

#### I/O Variable

After you configure your project, you can find the *I/O variables* under the DeviceNet slave device.

Utilities»View in System Manager

NI Distributed System Manager

Note

Related concepts:

- Using the I/O Variables

#### Palette

DeviceNet Palette: Access all common DeviceNet VIs at
 Industrial Communications»DeviceNet.

Advanced Palette: Access all advanced DeviceNet VIs at
 Industrial Communications»DeviceNet»Advanced.

Function Block Palette: Access DeviceNet Function Block at
 Industrial Communications»DeviceNet»Advanced»Function Block.

Related information:

- DeviceNet VIs
- DeviceNet Advanced VIs
- DeviceNet Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=devicenet-fundamentals.html language=enus -->
## TOPIC 00025: DeviceNet Fundamentals

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `devicenet-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/devicenet-fundamentals.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: According to the DeviceNet protocol, NI-Industrial Communications for DeviceNet contains the following fundamental concepts:

### DeviceNet Fundamentals

According to the DeviceNet protocol, NI-Industrial Communications for
 DeviceNet contains the following fundamental concepts:

- [Connection Type](connection-type.html)
- [Expected Packet Rate](expected-packet-rate.html)
- [Explicit Messaging Object](explicit-messaging-object.html)
- [Interface Object](interface-object.html)
- [I/O Object](i-o-object.html)
- [Poll Mode](poll-mode.html)
- [Reset Request Message Format](reset-request-message-format.html)

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=devicenet-hardware.html language=enus -->
## TOPIC 00026: DeviceNet Hardware

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `devicenet-hardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/devicenet-hardware.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: CANopen hardware supported by NI-Industrial Communications for DeviceNet software are listed below. These CANopen products are fully compliant with the CANopen Specification. Supported Hardware Products NI-9882 Compliant with the DeviceNet Specification. This hardware allows you to use your CompactR

### DeviceNet Hardware

CANopen hardware supported by NI-Industrial Communications for
 DeviceNet software are
 listed below. These CANopen products are fully compliant with the *CANopen
 Specification*.

#### Supported Hardware Products

NI-9882

DeviceNet Specification

PCI-8532

PCI Local Bus Specification

PXI-8532

PXI Specification

CompactPCI Specification

Note

NI-Industrial Communications for
 DeviceNet

x

#### Isolation

High-voltage spikes on the target bus may damage your
 equipment. All of the supported DeviceNet products protect your equipment from this
 damage. All bus ports are galvanically isolated up to 500
 VDC (2 seconds maximum withstand)
 channel-to-channel and channel-to-bus.

#### Transceiver

All of the supported
 DeviceNet products use the Philips PCA82C251
 High-Speed CAN transceiver. The Philips PCA82C251 is
 fully compatible with the ISO 11898 standard.

PCA82C251

- 125 Kb/s
- 250 Kb/s
- 500 Kb/s

#### LED Indicator

Each supported DeviceNet
 product has bi-color (green/red) LED indicators to show status.

LED 1

LED 2

LED 3

LED 4

| LED State | Description |
| --- | --- |
| Off | No application is using the DeviceNet hardware interface. |
| Flashing Green | The DeviceNet hardware port is ready to use. |
| Green | The DeviceNet hardware port is online. |
| Red | The DeviceNet hardware encounters the duplicate MAC ID error. |

| LED State | Description |
| --- | --- |
| Off | No application uses the DeviceNet hardware interface. |
| Flashing Green | The DeviceNet hardware port is ready to use. |
| Green | The DeviceNet interface has started. |
| Red | The DeviceNet interface encounters the Bus Off error. |

Related information:

- NI-9882 Specifications
- PCI/PXI-8532 Specifications

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=enabling-the-ni-scan-engine-on-windows.html language=enus -->
## TOPIC 00027: Enabling the NI Scan Engine on Windows

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `enabling-the-ni-scan-engine-on-windows.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/enabling-the-ni-scan-engine-on-windows.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Scan Engine used by the DeviceNet I/O variable is not enabled on Windows by default. If your DeviceNet interface hardware is installed on the local host, complete the following steps to enable the NI Scan Engine on Windows. Right-click the local host target item, and select Properties. The ta

### Enabling the NI Scan Engine on Windows

The NI Scan Engine used by the DeviceNet I/O variable is not enabled on Windows by default. If your DeviceNet interface hardware is installed on the local host, complete the following steps to enable the NI Scan Engine on Windows.

1. Right-click the local host target item, and select Properties . The target properties dialog box appears.
2. Switch to the Scan Engine page and place a checkmark in the Start Scan Engine on Deploy checkbox.
3. Click OK to close the dialog box.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=expected-packet-rate.html language=enus -->
## TOPIC 00028: Expected Packet Rate

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `expected-packet-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/expected-packet-rate.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Expected Packet Rate (EPR) is the expected rate of I/O message production in milliseconds. Use the EPR to trigger data productions. You also can use the EPR for the watchdog timer to verify that a remote device still exists and is producing data as expected. The EPR of each I/O connection is a m

### Expected Packet Rate

The Expected Packet Rate (EPR) is the expected rate of I/O message production in
 milliseconds.

Use the EPR to trigger data productions. You also can use the EPR for the watchdog timer to
 verify that a remote device still exists and is producing data as expected. The EPR of
 each I/O connection is a major factor in determining the overall performance of your
 DeviceNet network. You can set the EPR according to your needs.

You can configure your Interface Object to use the following combinations of
 *connection type* and *poll modes*.

Strobe or Poll connection type with Automatic poll mode

I/O Objects

NI-Industrial Communications for
 DeviceNet

Strobe connection type with Scanned or Individual poll mode

NI-Industrial Communications for
 DeviceNet

Poll connection type with Scanned poll mode

two groups

100
 ms

500 ms

Poll connection type with Individual poll mode

Change-of-State (COS) connection type with any poll mode

NI-Industrial Communications for
 DeviceNet

Cyclic connection type with any poll mode

Note

60,000

Parent topic:

DeviceNet Fundamentals

Related concepts:

- Interface Object
- Connection Type
- Poll Mode
- I/O Object

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=explicit-messaging-object.html language=enus -->
## TOPIC 00029: Explicit Messaging Object

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `explicit-messaging-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/explicit-messaging-object.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Explicit Messaging Object represents an Explicit Messaging connection to a remote DeviceNet device. A remote DeviceNet device is a physical device that a DeviceNet cable attaches to your interface. Because a device can only have one Explicit Messaging connection, use the Explicit Messaging Objec

### Explicit Messaging Object

The Explicit Messaging Object represents an Explicit Messaging connection to a
 remote DeviceNet device.

A remote DeviceNet device is a physical device that a DeviceNet cable attaches to your
 interface. Because a device can only have one Explicit Messaging connection, use the
 Explicit Messaging Object for features that apply to the device as a whole.

Use the Explicit Messaging Object to complete the following tasks:

- Execute the Get Attribute Single service on the remote device by using the Get DeviceNet Attribute VI.
- Execute the Set Attribute Single service on the remote device by using the Set DeviceNet Attribute VI.
- Send any other Explicit Message request to the remote device and receive the associated Explicit
 Message response by using the Write DeviceNet Explicit Message VI
 and the Read DeviceNet Explicit Message VI.
- Configure the settings for the remote devices.

For information about these VIs, refer to the *NI-Industrial Communications for
 DeviceNet Programming Reference Manual.*

Parent topic:

DeviceNet Fundamentals

Related information:

- NI-Industrial Communications for DeviceNet Programming Reference
 Manual

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=getting-started-with-ni-i-o-variable-and-func.html language=enus -->
## TOPIC 00030: Getting Started with NI I/O Variable and Function Block

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `getting-started-with-ni-i-o-variable-and-func.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/getting-started-with-ni-i-o-variable-and-func.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to use NI I/O Variable and Function Block to develop your applications.

### Getting Started with NI I/O Variable and Function Block

Complete the following steps to use NI I/O Variable and Function Block to develop your applications.

1. Installing the Software
2. Adding a Real-Time Controller
3. Adding a DeviceNet Master and Connected Slave Devices
4. Using NI I/O Variable and Function Block to Develop Applications

Parent topic:

Legacy

Related concepts:

- Using the I/O Variables
- Using the DeviceNet Explicit Message Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=i-o-object.html language=enus -->
## TOPIC 00031: I/O Object

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `i-o-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/i-o-object.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The I/O Object represents an I/O connection to a remote DeviceNet device. The I/O Object usually represents I/O communication as a master with a remote slave device. If you use your computer as the primary controller of your DeviceNet devices, configure I/O communication as a master. You can also co

### I/O Object

The I/O Object represents an I/O connection to a remote DeviceNet device. The I/O Object usually represents I/O communication as a master with a remote slave device. If you use your computer as the primary controller of your DeviceNet devices, configure I/O communication as a master.

You can also configure the I/O Object for I/O communication as a slave with a remote master. If you use your computer as a peripheral device for another primary controller, you can configure I/O communications as a slave. Set the device MAC ID of the I/O Objects the same as the interface MAC ID of the Interface Object to configure I/O communication as a slave.

The I/O Object supports all master/slave I/O connections that the DeviceNet Specification (version 2.0) defines. You can use polled, strobed, and COS/cyclic I/O connections simultaneously for a given device.

Use the I/O Object to complete the following tasks:

- Read data from the most recent message received on the I/O connection by using the Read DeviceNet IO VI.
- Write data to the next message produced on the I/O connection by using the Write DeviceNet IO VI.

Parent topic:

DeviceNet Fundamentals

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=importing-a-device-datasheet.html language=enus -->
## TOPIC 00032: Importing a Device Datasheet

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `importing-a-device-datasheet.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/importing-a-device-datasheet.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to import other datasheet files into the NI-Industrial Communications for DeviceNetsoftware. Right-click a slave item and select Datasheet to display the Datasheet dialog box. Click the Add Files button to open the EDS File Under Path dialog box. Navigate to the path whe

### Importing a Device Datasheet

Complete the following steps to import other datasheet files into the NI-Industrial Communications for
 DeviceNetsoftware.

1. Right-click a slave item and select Datasheet to display the Datasheet dialog box.
2. Click the Add Files button to open the EDS File Under Path dialog box.
3. Navigate to the path where the datasheet file is located and select the file. Click the OK button to add the file to the tree.

After you add the datasheet file, you can see the Add EDS File(s)—Result
 dialog box. If you import the file successfully, the import result displays
 Succeed. If not, an invalid format may cause unsuccessful import.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=install-software-on-host-non-rt-os.html language=enus -->
## TOPIC 00033: Installing the Software on the Host

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `install-software-on-host-non-rt-os.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/install-software-on-host-non-rt-os.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the required software on the host in the following order. LabVIEW and LabVIEW Real-Time Module NI CompactRIO Device Drivers NI-Industrial Communications for DeviceNet

### Installing the Software on the Host

Install the required software on the host in the following order.

1. LabVIEW and LabVIEW Real-Time Module
2. NI CompactRIO Device Drivers
3. NI-Industrial Communications for DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=install-software-on-host.html language=enus -->
## TOPIC 00034: Installing the Software on the Host

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `install-software-on-host.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/install-software-on-host.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Install the required software on the host in the following order: LabVIEW, LabVIEW FPGA Module, and LabVIEW Real-Time Module NI CompactRIO Device Drivers NI-Industrial Communications for DeviceNet

### Installing the Software on the Host

Install the required software on the host in the following order:

1. LabVIEW, LabVIEW FPGA Module, and LabVIEW Real-Time Module
2. NI CompactRIO Device Drivers
3. NI-Industrial Communications for DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=installing-ni-indcomm-with-rt.html language=enus -->
## TOPIC 00035: Installing NI-Industrial Communications for DeviceNet on the CompactRIO RT Controller

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `installing-ni-indcomm-with-rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/installing-ni-indcomm-with-rt.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use NI Measurement & Automation Explorer (MAX) to locate the CompactRIO RT controller under Remote Systems in the left pane. Expand the located CompactRIO, right-click Software, and select Add/Remove Software from the shortcut menu to launch the installation wizard. You can install the required comp

### Installing NI-Industrial Communications for
 DeviceNet on the CompactRIO RT Controller

Use NI Measurement & Automation Explorer (MAX) to locate the CompactRIO RT controller under Remote Systems in the left pane. Expand the located CompactRIO, right-click Software, and select Add/Remove Software from the shortcut menu to launch the installation wizard. You can install the required components using one of the following methods:

NI CompactRIO

NI CompactRIO

Next

x

Custom software installation

x

After installing NI-Industrial Communications for
 DeviceNet on the CompactRIO RT controller, use the options below to detect
 interfaces:

Devices and Interfaces

Devices and Interfaces

System API

NI-Industrial Communications for
 DeviceNet

System Configuration

NI-Industrial Communications for
 DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=installing-ni-indcomm-wo-rt.html language=enus -->
## TOPIC 00036: Installing NI-Industrial Communications for DeviceNet on the CompactRIO RT Controller 2

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `installing-ni-indcomm-wo-rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/installing-ni-indcomm-wo-rt.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use NI Measurement & Automation Explorer (MAX) to locate the CompactRIO RT controller under Remote Systems in the left pane. To launch the installation wizard, expand the located CompactRIO, right-click Software, and select Add/Remove Software from the shortcut menu. Install the required components

### Installing NI-Industrial Communications for
 DeviceNet on the CompactRIO RT Controller 2

Use NI Measurement & Automation Explorer (MAX) to locate the CompactRIO RT controller under
 Remote Systems in the left pane.

To launch the installation wizard, expand the located CompactRIO, right-click
 Software, and select Add/Remove
 Software from the shortcut menu.

Install the required components using one of the following methods.

NI CompactRIO

NI CompactRIO

Next

x

Custom software installation

x

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=installing-software.html language=enus -->
## TOPIC 00037: Installing the Software

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `installing-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/installing-software.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to install the software on the host and controller. Install the prerequisite software on the host according to the NI-Industrial Communications for DeviceNet Readme. Install the NI-Industrial Communications for DeviceNet software on the host. If you install the DeviceNet

### Installing the Software

Complete the following steps to install the software on the host and controller.

1. Install the prerequisite software on the host according to the NI-Industrial Communications for DeviceNet Readme .
2. Install the NI-Industrial Communications for
 DeviceNet software on the host.
3. If you install the DeviceNet interface card on an NI real-time controller, install the NI-Industrial Communications for
 DeviceNet software on the real-time controller.

Notes:

- If you install the DeviceNet interface card on the real-time controller, go to (Step 2)
 Adding a Real-Time Controller and follow the remaining instructions.
- If you install the DeviceNet interface card on the host, skip Adding a Real-Time
 Controller and go to (Step 3) Adding a DeviceNet Master and
 Connected Slave Devices .
- After completing Step 1, you can use DeviceNet VIs.

Parent topic:

Getting Started with NI I/O Variable and Function Block

Related concepts:

- Related Documentation

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=interface-object.html language=enus -->
## TOPIC 00038: Interface Object

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `interface-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/interface-object.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Interface Object represents a DeviceNet interface. Because this interface acts as a device on the DeviceNet network, you can configure the Interface Object with its own MAC ID and baud rate. Use the Interface Object to complete the following tasks: Configure settings of the interface. Start and

### Interface Object

The Interface Object represents a DeviceNet interface. Because this interface acts as a device on the DeviceNet network, you can configure the Interface Object with its own MAC ID and baud rate.

Use the Interface Object to complete the following tasks:

- Configure settings of the interface.
- Start and stop communication for all NI-Industrial Communications for DeviceNet objects associated with the interface.

Parent topic:

DeviceNet Fundamentals

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=labview-and-devicenet-data-types.html language=enus -->
## TOPIC 00039: LabVIEW and DeviceNet Data Types

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `labview-and-devicenet-data-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/labview-and-devicenet-data-types.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW and DeviceNet support different data types. The following table lists each LabVIEW data type, its equivalent data type in the DeviceNet protocol, and a brief description. These data types apply to the Real-Time CompactRIO controller, PCI, and PXI. 1 LabVIEW and DeviceNet Data Types LabVIEW D

### LabVIEW and DeviceNet Data Types

LabVIEW and DeviceNet support different data types. The following table lists each LabVIEW data type, its equivalent data type in the DeviceNet protocol, and a brief description. These data types apply to the Real-Time CompactRIO controller, PCI, and PXI.

| LabVIEW | DeviceNet | Description |
| --- | --- | --- |
| I8 | SINT | 8-bit signed integer |
| I16 | INT | 16-bit signed integer |
| I32 | DINT | 32-bit signed integer |
| U8 | USINT | 8-bit unsigned integer |
| U16 | UINT | 16-bit unsigned integer |
| U32 | UDINT | 32-bit unsigned integer |
| TF (Boolean) | BOOL | Boolean value |
| String (0-FF hex) | SHORT_STRING | ASCII character string: The length of the string ranges from 0 to FF. |
| String (0-FFFF hex) | STRING | ASCII character string: The length of the string ranges from 0 to FFFF. |
| SGL | REAL | 32-bit floating point |
| DBL | LREAL | 64-bit floating point |

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=legacy-troubleshooting.html language=enus -->
## TOPIC 00040: Legacy Troubleshooting

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `legacy-troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/legacy-troubleshooting.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Conflict Message about the NI Scan Engine appears when DeviceNet master is being deployed on Windows The NI Scan Engine is not enabled on Windows by default, so you must enable the NI Scan Engine on Windows before deploying. The LabVIEW error (Hex 0x80DF0016) occurs when the I/O variable applicati

### Legacy Troubleshooting

A Conflict Message about the NI Scan Engine appears when DeviceNet master is
 being deployed on Windows

enable the NI Scan Engine on Windows

The LabVIEW error (Hex 0x80DF0016) occurs when the I/O variable application is
 running on Windows

The LabVIEW error (Hex 0x101EE) occurs while the I/O variable application is
 running

Active

The DeviceNet error (Hex 0x80054C97) occurs when a function block application is
 running

The DeviceNet warning (Hex 0x54C31) occurs when an I/O variable application is
 running, or the DeviceNet error (Hex 0x80054D20) occurs in a function block
 application

Notice to Develop the
 DeviceNet Application in LabVIEW

Note

Help»Explain Error

Explain
 Error

Parent topic:

Legacy

Related concepts:

- Enabling the NI Scan Engine on Windows
- NI Scan Engine Mode
- Deploying and Undeploying a DeviceNet Configuration
- Notice to Develop the DeviceNet Application in LabVIEW

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=legacy.html language=enus -->
## TOPIC 00041: Legacy

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `legacy.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/legacy.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about using DeviceNet with PCI and PXI, refer to the following topics.

### Legacy

For information about using DeviceNet with PCI and PXI, refer to the following topics.

- [Getting Started with NI I/O Variable and Function Block](getting-started-with-ni-i-o-variable-and-func.html)
- [Configuring the DeviceNet Network](configuring-the-devicenet-network.html)
- [Developing the DeviceNet Application in LabVIEW](developing-the-devicenet-application-in-labvi.html#GUID-F92B4F5F-B2C4-4602-BBDA-A593BA126A93)
- [Using the NI Scan Engine](using-the-ni-scan-engine.html)
- [Legacy Troubleshooting](legacy-troubleshooting.html)

Related information:

- Project Explorer Window Environment

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=measurement-automation-explorer-help-for-devi.html language=enus -->
## TOPIC 00042: Hardware Information when Using MAX

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `measurement-automation-explorer-help-for-devi.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/measurement-automation-explorer-help-for-devi.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Measurement & Automation Explorer (MAX) to configure and test DeviceNet hardware. DeviceNET Hardware Information Product The product name of the NI-Industrial Communications for DeviceNet device. Serial Number The serial number of the NI-Industrial Communications for DeviceNet device. In

### Hardware Information when Using MAX

You can use Measurement & Automation Explorer (MAX) to configure and test
 DeviceNet hardware.

#### DeviceNET Hardware Information

Product

NI-Industrial Communications for
 DeviceNet

Serial Number

NI-Industrial Communications for
 DeviceNet

Interface

NI-Industrial Communications for
 DeviceNet

Slot

NI-Industrial Communications for
 DeviceNet

Note

Note

Parent topic:

DeviceNet Hardware

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=monitoring-the-slave-device-state.html language=enus -->
## TOPIC 00043: Monitoring the Slave Device State

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `monitoring-the-slave-device-state.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/monitoring-the-slave-device-state.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Right-click the master item and select Utilities»Online Test Panel to display the Online Test Panel dialog box. This dialog box displays all of the slave device items added under the master item. The device state can be Connected or Disconnected, indicating whether a slave device is connected to the

### Monitoring the Slave Device State

Right-click the master item and select Utilities»Online Test Panel to
 display the Online Test Panel dialog box. This dialog box displays
 all of the slave device items added under the master item. The device state can be
 Connected or Disconnected, indicating whether a
 slave device is connected to the master interface.

Parent topic:

Configuring the DeviceNet Network

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=new-features-and-changes.html language=enus -->
## TOPIC 00044: NI-Industrial Communications for DeviceNet New Features and Changes

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-Industrial Communications for DeviceNet. Discover what is new in the latest releases of NI-Industrial Communications for DeviceNet.If you cannot find new features and changes for your version, it might

### NI-Industrial Communications for
 DeviceNet
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-Industrial Communications for
 DeviceNet.

NI-Industrial Communications for
 DeviceNet

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-Industrial Communications for
 DeviceNet
 2022 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 DeviceNet 2022 Q4.

##### New
 Features

This version of NI-Industrial Communications for
 DeviceNet provides
 support for the following features:

- Added support for LabVIEW 2022 (32-bit) and LabVIEW 2022 Real-Time Module.
- Extended the LabVIEW version support with NI Linux RealTime to include LabVIEW 2020 and
 later.

#### NI-Industrial Communications for
 DeviceNet
 21.5 Changes

Learn about new features, behavior changes, and other updates in NI-Industrial Communications for
 DeviceNet 21.5.

##### New
 Features

This version of NI-Industrial Communications for
 DeviceNet provides
 support for the following features:

- Added support for LabVIEW 2021 (32-bit) and LabVIEW 2021 Real-Time Module.
- Added support for PXI and PXIe controllers with NI Linux RealTime through
 .ipk installation.

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=ni-scan-engine-mode.html language=enus -->
## TOPIC 00045: NI Scan Engine Mode

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `ni-scan-engine-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/ni-scan-engine-mode.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists NI Scan Engine modes. 10 NI Scan Engine Modes Mode Description Configuration The required mode for configuring NI Scan Engine settings and hardware on the DeviceNet network. The I/O variables are not updated with real data in this mode. Active In this mode, the NI Scan Engi

### NI Scan Engine Mode

The following table lists NI Scan Engine modes.

| Mode | Description |
| --- | --- |
| Configuration | The required mode for configuring NI Scan Engine settings and hardware on the DeviceNet network. The I/O variables are not updated with real data in this mode. |
| Active | In this mode, the NI Scan Engine actively updates I/O variables with real data from the DeviceNet network. |

#### NI Scan Engine Mode Transition Impact on DeviceNet

When the Scan Engine mode changes from Configuration mode to Active mode,
 the NI-Industrial Communications for DeviceNet software connects the DeviceNet
 interface master device to the network and writes *Scan Engine data* to
 the DeviceNet slave devices.

Note

- The VI calls the Set Scan Engine Mode VI before
 it uses any I/O variables or function blocks.
- If the VI uses a function block to access a slave device, the DeviceNet
 master interface item must be added to the VI's LabVIEW project.

#### Changing the NI Scan Engine Mode

You can
 change the NI Scan Engine mode manually or programmatically.

- To change the NI Scan Engine mode manually, right-click the target item in the
 LabVIEW project explorer and select Utilities»Scan Engine Mode»Switch
 to Active (or Switch to
 Configuration ).
- Change the mode programmatically with the Set Scan Engine
 Mode VI in the Measurement I/O»NI Scan
 Engine palette.

Complete the following steps to receive notification of all NI Scan Engine mode
 transitions.

1. Right-click the target item in the LabVIEW project explorer and select
 Properties .
2. Check the Report automatic scan mode transitions as
 conflicts option on the Scan Engine 
 page.

Parent topic:

Using the NI Scan Engine

Related concepts:

- Project Data, Scan Engine Data, and Device Data

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=overview.html language=enus -->
## TOPIC 00046: Overview

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/overview.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: DeviceNetDeviceNet is a digital multi-drop communication network between industrial controllers and I/O devices. Each device and/or controller is a node on the network. DeviceNet supports multiple communication hierarchies and message prioritization as a producer-consumer network. You can configure

### Overview

#### DeviceNet

DeviceNet is a digital
 multi-drop communication network between industrial controllers and I/O devices.
 Each device and/or controller is a node on the network. DeviceNet supports multiple
 communication hierarchies and message prioritization as a producer-consumer network.
 You can configure DeviceNet systems to operate in a master-slave or distributed
 control architecture using peer-to-peer communication.

#### NI-Industrial Communications for
 DeviceNet

NI-Industrial Communications for
 DeviceNet enables you to configure
 and control DeviceNet devices on a DeviceNet network and to communicate with FPGA
 targets.

Hardware

NI-Industrial Communications for
 DeviceNet

Software

NI-Industrial Communications for
 DeviceNet

Related concepts:

- DeviceNet Hardware

Related information:

- DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=poll-mode.html language=enus -->
## TOPIC 00047: Poll Mode

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `poll-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/poll-mode.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The poll mode determines the communication scheme used for all polled I/O connections in which the interface acts as a master. The interface uses this scheme to transmit poll requests to slave devices. The default mode is Automatic. The NI-Industrial Communications for DeviceNet provides the followi

### Poll Mode

The poll mode determines the communication scheme used for all polled I/O connections in which the interface acts as a master. The interface uses this scheme to transmit poll requests to slave devices. The default mode is Automatic.

The NI-Industrial Communications for DeviceNet provides the following poll modes:

- Automatic —Use this mode if you do not want to specify timing for polled and strobed I/O connections. In Automatic mode, the NI-IndCom for DeviceNet software automatically calculates a safe rate for production of all poll requests and strobe requests. This mode is similar to Scanned mode, except that you do not need to specify a valid expected packet rate (EPR) for each polled/strobed I/O Object.
- Scanned —Use this mode to enable the traditional scanned I/O scheme for polled and strobed I/O connections. In Scanned mode, NI-IndCom for DeviceNet produces all poll requests and strobe requests in quick succession. After the production, NI-IndCom for DeviceNet waits to receive individual responses.
- Individual —Use this mode to configure poll rates individually for each polled I/O connection. In Individual mode, NI-IndCom for DeviceNet does not produce poll requests as a group, but as individual polled I/O connection that communicates at an independent rate. The EPR of the I/O Object determines the rate of each poll request. Use individual polling when you know the time of each device to perform the physical measurement or control function of each device. For example, if you have a discrete input device capable of acquiring a new measurement every 10 ms, an analog input device with a measurement rate of 45 ms, and a temperature sensor with a measurement rate of 200 ms, you can use individual polling to communicate with each device at the exact measurement rate. Because this communication occurs only at the specific rate that you manually trigger for each device, individual polling often provides optimum network usage.

Parent topic:

DeviceNet Fundamentals

Related concepts:

- Expected Packet Rate

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=project-data-scan-engine-data-and-device-data.html language=enus -->
## TOPIC 00048: Project Data, Scan Engine Data, and Device Data

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `project-data-scan-engine-data-and-device-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/project-data-scan-engine-data-and-device-data.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: DeviceNet uses the following kinds of data: Project Data The LabVIEW project file stores this data. The DeviceNet configuration includes both the master interface settings and connected slave settings. For example, the master baud rate and slave active I/O connection type are stored. Scan Engine Dat

### Project Data, Scan Engine Data, and Device Data

DeviceNet uses the following kinds of data:

Project Data

Scan Engine Data

deploy the
 DeviceNet configuration

Device Data

Active

NI-Industrial Communications for
 DeviceNet

DeviceNet Slave Device Online
 Test Panel

In most cases, do not edit the data manually. The NI Scan Engine and the NI-Industrial Communications for
 DeviceNet
 software manages the data. Use the following guidelines to ensure proper operation:

- If you install your DeviceNet interface card on the local host, enable the Scan Engine on the local host .
- Ensure that your VI calls the Set Scan Engine Mode VI before it uses any I/O
 variables or function blocks.
- If a VI uses a function block to access a slave device, you must add the DeviceNet master interface item to the LabVIEW project of this VI.

Parent topic:

Using the NI Scan Engine

Related concepts:

- Deploying and Undeploying a DeviceNet Configuration
- Enabling the NI Scan Engine on Windows

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=related-documentation.html language=enus -->
## TOPIC 00049: Related Documentation

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `related-documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/related-documentation.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-9882 Operating Instructions Use this manual to learn about the specifications of the C Series hardware. To access this manual, select Start»All Programs»National Instruments»NI-Industrial Communications for DeviceNet»NI 9882 Operating Instructions. NI-Industrial Communications for DeviceNet Readm

### Related Documentation

NI-9882

Operating
 Instructions

Start»All Programs»National
 Instruments»NI-Industrial Communications for DeviceNet»NI 9882 Operating
 Instructions

NI-Industrial Communications for DeviceNet Readme

readme_DeviceNet.html

Firmware Update Instructions

update your firmware

Firmware_Update_Instructions.html

Common Industrial Protocol
 (CIP™)

DeviceNet™ Adaptation of
 CIP

Integration of Modbus® Devices into
 the CIP Architecture

Related concepts:

- Upgrading the Firmware of the NI-9882 Module

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=reset-request-message-format.html language=enus -->
## TOPIC 00050: Reset Request Message Format

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `reset-request-message-format.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/reset-request-message-format.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can get a Reset request message by selecting Reset State from the attribute ID of the Get Driver Attribute VI. NI-Industrial Communications for DeviceNet provides the Reset request messages in hex by using the following format: Byte 3 specifies the class types that receive a Reset request. Bit 7

### Reset Request Message Format

You can get a Reset request message by selecting Reset State from the attribute ID of the *Get Driver Attribute* VI. NI-Industrial Communications for DeviceNet provides the Reset request messages in hex by using the following format:

- Byte 3 specifies the class types that receive a Reset request.
  - Bit 7 of this byte indicates whether the DeviceNet Object receives a Reset request. If Bit 7 is 0, the DeviceNet Object does not receive the Reset request from the master. If Bit 7 is 1, the DeviceNet Object receives the Reset request.
  - Bit 6 of this byte indicates whether the Identity Object receives a Reset request. If Bit 6 is 0, the Identity Object does not receive the Reset request from the master. If Bit 6 is 1, the Identity Object receives the Reset request.
  - Bit 0-5 of this byte are 0 only. NI-IndCom for DeviceNet does not specify the function of these bits.
- Byte 2 is 0 only. NI-IndCom for DeviceNet does not specify the function of this byte.
- Byte 1 specifies the Reset service parameter in the Reset request for the Identity Object.
- Byte 0 specifies the Reset service parameter in the Reset request for the DeviceNet Object.

For example, if the Reset request message is 0x80000100, the Identity Object receives Reset request with service parameter 01 hex.

If the Reset request message is 0xC0000102, the Identity Object receives a Reset request with service parameter 01 hex and the DeviceNet Object receives a Reset request with service parameter 02 hex.

Parent topic:

DeviceNet Fundamentals

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=run-fpga-vi-to-load-devicenet.html language=enus -->
## TOPIC 00051: Running an FPGA VI to Load DeviceNet

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `run-fpga-vi-to-load-devicenet.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/run-fpga-vi-to-load-devicenet.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default FPGA VI that ships with CompactRIO does not establish the communication between the NI-Industrial Communications for DeviceNet RT driver and the NI -9882 module. Run an FPGA VI to load the support file for the NI-Industrial Communications for DeviceNet software to the real-time controlle

### Running an FPGA VI to Load DeviceNet

The default FPGA VI that ships with CompactRIO does not establish the communication between the
 NI-Industrial Communications for
 DeviceNet RT
 driver and the NI -9882 module. Run an FPGA VI to load the support
 file for the NI-Industrial Communications for
 DeviceNet software to the real-time controllers. Building and Running a New FPGA VI

If you do not have an FPGA VI in your project, complete the following steps to build a new FPGA VI to load the bit file for DeviceNet:

1. Right-click the FPGA target in a LabVIEW project and select New»VI from the shortcut menu.
2. Save this VI and right-click Build Specifications and select New»Compilation from the shortcut menu.
3. In the My Compilation Properties dialog box, click the Source Files tab and select the new VI.
4. Click the Build button.
5. Run this VI and close the front panel. Even though the VI is empty, this VI can load the required NI-Industrial Communications for DeviceNet support file.

#### Rebuilding and Running an Existing FPGA VI

To
 rebuild an existing FPGA VI in your project, right-click the VI and select
 Rebuild from the shortcut menu. Run the FPGA VI after rebuilding.

Use the Open FPGA VI Reference function from a host VI.

Note

NI-Industrial Communications for
 DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

Related concepts:

- DeviceNet Hardware
- Actions that Load or Unload the Bit File on the CompactRIO RT Controller

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=troubleshooting.html language=enus -->
## TOPIC 00052: Troubleshooting

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/troubleshooting.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create or execute NI-Industrial Communications for DeviceNet applications, you may encounter the following issues. Follow the guidelines to troubleshoot those issues. You cannot open an interface on CompactRIO Ensure that you use the Open FPGA VI Reference function to load the NI-9882 modul

### Troubleshooting

When you create or execute NI-Industrial Communications for DeviceNet applications, you may encounter the following issues. Follow the guidelines to troubleshoot those issues.

You cannot open an interface on CompactRIO

Open FPGA VI Reference

NI-9882

The NI-IndCom for DeviceNet interfaces are not visible in NI Measurement &
 Automation Explorer (MAX).

All NI-IndCom for DeviceNet operations return failure

LabVIEW error (Hex 0xBFF62007) occurs when the device does not support closing
 Explicit Messaging Objects or I/O Objects

Explicit Messaging
 Objects

I/O Objects

The device does not support reading I/O Objects or reading/writing Explicit
 Messaging Objects before starting the interface.

Change does not take effect when you change a node ID or a baud rate in
 LabVIEW

The device does not get the current state

Related concepts:

- Explicit Messaging Object
- I/O Object

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=tutorial-creating-applications-on-different-t.html language=enus -->
## TOPIC 00053: Tutorial: Creating Applications on Different Types of Chassis and Controllers

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `tutorial-creating-applications-on-different-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/tutorial-creating-applications-on-different-t.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: In this tutorial, you use NI-Industrial Communications for DeviceNet to create applications on different types of chassis and controllers.

### Tutorial: Creating Applications on Different Types of Chassis and Controllers

In this tutorial, you use NI-Industrial Communications for DeviceNet to create applications on different types of chassis and controllers.

- [Creating Applications on CompactRIO Targets with NI Linux Real-Time](creating-applications-on-crio-targets-w-rt.html)
- [Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time](creating-applications-on-crio-targets-wo-rt.html)
- [Creating Applications on PCI and PXI](creating-applications-on-pci-and-pxi.html)

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=upgrading-the-firmware-of-ni-9882.html language=enus -->
## TOPIC 00054: Upgrading the Firmware of the NI-9882 Module

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `upgrading-the-firmware-of-ni-9882.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/upgrading-the-firmware-of-ni-9882.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Industrial Communications for DeviceNet software version 2.3 or later requires the NI-9882 module with the updated firmware. When you upgrade your software to version 2.3 or later, check the software version of the media shipped with your NI-9882. If the version is not 2.3 or later, or you are no

### Upgrading the Firmware of the NI-9882
 Module

NI-Industrial Communications for
 DeviceNet software
 version 2.3 or later requires the NI-9882 module with the
 updated firmware. When you upgrade your software to version 2.3 or later, check the
 software version of the media shipped with your NI-9882.
 If the version is not 2.3 or later, or you are not sure of the version number, NI
 recommends that you update the firmware.

To update the firmware of the NI-9882 module, open the
 Firmware_Update_Instructions.html file in the National
 Instruments\NI-IndCom for DeviceNet directory and follow the instructions
 to use a LabVIEW example project.

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=uploading-a-devicenet-configuration.html language=enus -->
## TOPIC 00055: Uploading a DeviceNet Configuration

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `uploading-a-devicenet-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/uploading-a-devicenet-configuration.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can upload the previous deployed configuration from the scan engine data to the project data. You also can access a parameter and read the parameter value from the slave device. Complete the following steps to upload the DeviceNet network configuration from the target. Right-click the target ite

### Uploading a DeviceNet Configuration

You can upload the previous deployed configuration from the scan engine data to the *project data*. You also can *access a parameter* and read the parameter value from the slave device.

Complete the following steps to upload the DeviceNet network configuration from the target.

1. Right-click the target item in the LabVIEW Project Explorer and select Utilities»Compare Project & System to display the Project & System Comparison dialog box.
2. Select the DeviceNet master, slave, or I/O variable in the right System column and click Upload .
3. Click Apply .

Parent topic:

Configuring the DeviceNet Network

Related concepts:

- Project Data, Scan Engine Data, and Device Data
- Accessing a Parameter

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=use-io-variable-and-function-block.html language=enus -->
## TOPIC 00056: Using NI I/O Variable and Function Block to Develop Applications

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `use-io-variable-and-function-block.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/use-io-variable-and-function-block.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: When NI-Industrial Communications for DeviceNet detects the interfaces, you are ready to use these interfaces. NI-Industrial Communications for DeviceNet also provides the following approaches to help you build applications. You can use the Devicenet VIs to read and write data after you complete Ste

### Using NI I/O Variable and Function Block to
 Develop Applications

NI-Industrial Communications for
 DeviceNet

NI-Industrial Communications for
 DeviceNet

Note

#### I/O Variables

I/O variables

Note

#### DeviceNet Explicit Message Function Block

Use the DeviceNet Explicit Message Function Block to
 perform Explicit Message operations that typically take a long time to
 complete.

Parent topic:

Getting Started with NI I/O Variable and Function Block

Related concepts:

- Using the I/O Variables

Related information:

- DeviceNet Explicit Message Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=user-manual-welcome.html language=enus -->
## TOPIC 00057: NI-Industrial Communications for DeviceNet User Manual

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-Industrial Communications for DeviceNet User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Re

### NI-Industrial Communications for
 DeviceNet
 User Manual

The NI-Industrial Communications for
 DeviceNet User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-Industrial Communications for DeviceNET
- NI-Industrial Communications for DeviceNET Release Notes
- NI-Industrial Communications for DeviceNET Programming Reference
 Manual
- NI-9882 Specifications
- PCI/PXI-8532 Specifications

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=using-io-variables.html language=enus -->
## TOPIC 00058: Using the I/O Variables

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `using-io-variables.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/using-io-variables.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you configure the DeviceNet network successfully, you can create I/O variables. National Instruments recommends you use DeviceNet VIs instead of the I/O variables. Right-click a slave item and select Configure I/O.... Click Add to add I/O variables for this slave. Refer to Add/Edit/Remove a D

### Using the I/O Variables

Note

DeviceNet VIs

1. Right-click a slave item and select Configure I/O... .
2. Click Add to add I/O variables for this slave. Refer to Add/Edit/Remove a DeviceNet I/O Variable for more information.
3. The newly added I/O variables is visible in the LabVIEW Project Explorer
  - I/O Variable —The physical channels of the slave device mapped to the I/O variables. A slave device can have several I/O variables.
4. Right-click My Computer or the controller item and select New»VI to create a VI. Save the VI.
5. Add the Set Scan Engine Mode VI to the VI diagram. You can find it in the LabVIEW palette Measurement I/O»NI Scan Engine»Set Scan Engine Mode VI .

 Note 

 Ensure that you use the Set Scan Engine Mode VI to set the *NI Scan Engine Mode* to Active before using any DeviceNet I/O variables or function blocks.
6. Drag the I/O variable under the slave items and drop it in the VI block diagram. Connect a control or indicator to the I/O variable.
7. Add a Timed Loop . You can find it in the LabVIEW palette Programming»Structures»Timed Structures»Timed Loop . Right-click the input node of the timed loop, and select Configure Input Node to show the Configure Timed Loop dialog box. In the Loop Timing Source section, ensure the Synchronize to Scan Engine is selected.
8. Click Run to run the VI. You now can use a VI to access the DeviceNet network.

Parent topic:

Using NI I/O Variable and Function Block to Develop Applications

Related concepts:

- Adding/Editing/Removing a DeviceNet I/O Variable
- NI Scan Engine Mode

Related information:

- DeviceNet VIs

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=using-the-devicenet-explicit-message-function.html language=enus -->
## TOPIC 00059: Using the DeviceNet Explicit Message Function Block

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `using-the-devicenet-explicit-message-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/using-the-devicenet-explicit-message-function.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DeviceNet Explicit Message Function Block is an asynchronous module to complete Explicit Message operations that typically take a long time to complete. Use this function block to send any request from your master interface to the remote slave device and receive the associated Explicit Message r

### Using the DeviceNet Explicit Message Function Block

Note

DeviceNet VIs

1. Right-click the DeviceNet master item and select Deploy .

 Note 

 Use an explicit deployment if your application VI uses the DeviceNet function block but does not use the related I/O variable.
2. Right-click My Computer or the controller item and select New»VI to create a VI. Save the VI.
3. Add the Set Scan Engine Mode VI to the VI diagram. It can be found in the palette by selecting Measurement I/O»NI Scan Engine»Set Scan Engine Mode VI .

 Note 

 Ensure that you use the Set Scan Engine Mode VI to set the *NI Scan Engine Mode* to Active before calling any DeviceNet I/O variables or function blocks.
4. Drag a DeviceNet slave item from the LabVIEW Project Explorer and drop it into the VI to create a DeviceNet I/O Control .
5. Add a DeviceNet Explicit Message Function Block . It can be found in the palette by selecting Industrial Communications»DeviceNet»Advanced»Function Block»DeviceNet Explicit Message .
6. Add a while loop to use the function block continuously. You can refer to the DeviceNet Function Block (Windows) VI in labview\examples\NI-Industrial Communications for DeviceNet\Legacy Examples\Windows\DeviceNet Function Block (Windows).vi .
7. Connect controls or indicators to the function block.
8. Input valid Explicit Message request data and then click Run to run the VI. You now can use a function block to complete the Explicit Message operation.

Note

multiple

NI Example Finder

Parent topic:

Explicit Messaging Object

Related concepts:

- NI Scan Engine Mode

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=using-the-ni-scan-engine.html language=enus -->
## TOPIC 00060: Using the NI Scan Engine

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `using-the-ni-scan-engine.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/using-the-ni-scan-engine.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-Industrial Communications for DeviceNet software leverages the NI Scan Engine to provide powerful features such as I/O variables and function blocks. The NI Scan Engine allows efficient access to coherent sets of data channels, such as I/O channels, using a scan that stores data in a global memor

### Using the NI Scan Engine

NI-Industrial Communications for
 DeviceNet software
 leverages the NI Scan Engine to provide powerful features such as I/O variables and
 function blocks.

The NI Scan Engine allows efficient access to coherent sets of data channels, such as I/O
 channels, using a scan that stores data in a global memory map. The NI Scan Engine also
 updates all values at a single rate, known as the scan period.

For detailed information about the NI-Industrial Communications for
 DeviceNet software and the NI Scan Engine:, refer to
 *NI Scan Engine Mode* and *Project Data, Scan Engine Data and Device
 Data*.

Parent topic:

Legacy

Related concepts:

- I/O Variable
- NI Scan Engine Mode
- Project Data, Scan Engine Data, and Device Data

Related information:

- DeviceNet Explicit Message Function Block

<!--NI_TOPIC bundle=ni-industrial-communications-devicenet path=waiting-to-detect-interfaces.html language=enus -->
## TOPIC 00061: Waiting to Detect Interfaces

- bundle_id: `ni-industrial-communications-devicenet`
- source_path: `waiting-to-detect-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/ni-industrial-communications-devicenet/raw/resource/enus/waiting-to-detect-interfaces.html
- document_id: `ni-industrial-communications-devicenet`
- page_type: `leaf`
- content_type: `concept`
- source_description: After the FPGA VI runs with the NI-Industrial Communications for DeviceNet support, the real-time CompactRIO controller may take a few seconds to detect the DeviceNet hardware and to load appropriate RT drivers. This delay occurs only after you perform actions that cause NI-Industrial Communications

### Waiting to Detect Interfaces

After the FPGA VI runs with the NI-Industrial Communications for
 DeviceNet support, the real-time CompactRIO controller may
 take a few seconds to detect the DeviceNet hardware and to load appropriate RT drivers.
 This delay occurs only after you perform actions that cause NI-Industrial Communications for
 DeviceNet
 to load.

After using the Open FPGA VI Reference function to load NI-Industrial Communications for
 DeviceNet,
 wait for a few seconds to use the Open DeviceNet Interface VI and any
 other application on the real-time CompactRIO controller.

If you start an application on the real-time CompactRIO controller immediately after
 using the Open FPGA VI Reference function, an error occurs and NI-Industrial Communications for
 DeviceNet
 fails to complete this application. Wait for a few seconds and reopen the DeviceNet
 interface.

Note

Use the following options to detect interfaces.

Devices and Interfaces

Devices and Interfaces

System API

NI System Configuration API

NI-Industrial Communications for
 DeviceNet

NI System
 Configuration API

NI-Industrial Communications for
 DeviceNet

Parent topic:

Creating Applications on CompactRIO Targets with Operating Systems Other Than NI Linux Real-Time

Related concepts:

- DeviceNet Hardware
- Actions that Load or Unload the Bit File on the CompactRIO RT Controller
