# NI DOCUMENT BUNDLE: veristand

<!--NI_BUNDLE_CHUNK bundle=veristand start=1 end=250 -->
<!--NI_TOPIC bundle=veristand path=access-cold-junction-compensation.html language=enus -->
## TOPIC 00001: Accessing Cold-Junction Compensation Channels on SCXI Accessories

- bundle_id: `veristand`
- source_path: `access-cold-junction-compensation.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/access-cold-junction-compensation.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Manually add a Cold-Junction Compensation (CJC) channel to a system definition. Before you start, add a DAQ device and use MAX to configure the SCXI chassis, module, and accessory.For information on adding and configuring SCXI chassis and modules, refer to the Measurement & Explorer Help. CJC channe

### Accessing Cold-Junction Compensation Channels
 on SCXI Accessories

Manually add a Cold-Junction Compensation (CJC) channel to a system
 definition.

Note

Measurement & Explorer
 Help

System
 Explorer

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
4. Right-click a DAQ device and select Add SCXI
 Modules.
5. In the Add SCXI Module dialog box, specify the module type
 to add, set # Internal channels to 1, and click
 OK.
6. Under SCXI Chassis, click the SCXI Module you added.
7. Click Internal Channels»Channel 0.
8. In physical channel name field, enter _cjTemp.

Map a thermocouple scale to the _cjTemp internal channel
 to convert the acquired voltage values to temperature units.

Parent topic:

Adding and Configuring a DAQ Device

Related tasks:

- Creating a Thermocouple Scale

<!--NI_TOPIC bundle=veristand path=access-timing-id-xnet-frames.html language=enus -->
## TOPIC 00002: Accessing Timing and ID Information for Incoming NI-XNET Frames

- bundle_id: `veristand`
- source_path: `access-timing-id-xnet-frames.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/access-timing-id-xnet-frames.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Frame Information channels in VeriStand to monitor incoming NI-XNET frame timestamps, time differences, and frame IDs. Use these channels for mapping, logging, and prioritizing event-triggered frames. Before you begin, import an incoming XNET frame. Frame information channels store incoming NI-X

### Accessing Timing and ID Information for
 Incoming NI-XNET Frames

Use Frame Information channels in VeriStand to monitor incoming NI-XNET frame
 timestamps, time differences, and frame IDs. Use these channels for mapping,
 logging, and prioritizing event-triggered frames.

Before you begin, import an incoming XNET
 frame.

Frame information channels

- Receive Time —Contains the timestamp of the most recent frame.
- Time Difference —Contains the difference between the two most recent Receive
 Time timestamps.
- Frame ID —Contains the ID number that identifies the frame. This channel is
 for raw data format frames only.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET in the configuration tree.
4. Select an NI-XNET LIN, FlexRay, or CAN port.
5. Click Incoming and select a frame.
6. Click Add Information Channels
[IMAGE alt='image' src='GUID-C87E985E-D55D-426F-B25C-39319B550EC8-a5.gif'].
7. Expand Frame Information to view the channels.
8. Optional: 
 Specify a dedicated start value for a channel. 
 Channel typeHow to specify start valueReceive Time
Select a channel.
On the Receive Time configuration page, enter an initial
 value.Time Difference
Select a channel.
On the Time Difference configuration page, enter an initial
 value. 
 Note Raw data format frames also include
 Frame ID channels. VeriStand reads the value for this channel from the XNET database.
 You cannot modify it or specify an initial value through System
 Explorer. However, you can use frame IDs to prioritize
 event-triggered frames and to include or exclude frames from a data log file.
9. Save the system definition file.

After creating Frame Information channels, you can use them like other channels in
 VeriStand. For example, you can map them to other channels or to
 controls and indicators in the VeriStand Editor or Workspace.

Use the XNET page of the Options dialog box to configure VeriStand to
 create Frame Information channels when you import NI-XNET frames. You can also use the
 Import NI-XNET Frames dialog box to automatically create channels on
 a one-time basis when you import frames.

Parent topic:

Using NI-XNET Interfaces

<!--NI_TOPIC bundle=veristand path=act-faqs.html language=enus -->
## TOPIC 00003: Activation FAQ

- bundle_id: `veristand`
- source_path: `act-faqs.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/act-faqs.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to these common VeriStand activation questions. What Is Activation? Activation is the process of obtaining an activation code to enable your software to run on your computer. An activation code is an alphanumeric string that verifies the software, version, and computer ID to enable features on

### Activation FAQ

Refer to these common VeriStand activation questions.

#### What Is Activation?

Activation is the process of obtaining an activation code to enable your software to
 run on your computer. An activation code is an alphanumeric string that verifies the
 software, version, and computer ID to enable features on your computer. Activation
 codes are unique and are valid on only one computer.

#### What Is the NI Licensing
 Wizard?

The NI Licensing Wizard is a part of NI License Manager that leads you through the
 process of enabling software to run on your machine.

#### What Information Do I Need to
 Activate My NI Software?

You need your NI User account log-in, the product version and serial number, and a
 computer ID that uniquely identifies your computer. Certain activation methods may
 require additional information for delivery. This information is used only to
 activate your product. For complete disclosure of the NI software licensing
 information privacy policy, refer to the National Instruments Corporation Privacy Statement. If you optionally
 choose to register your software, your information is protected under the NI privacy
 policy, available at ni.com/privacy.

#### How Do I Find My Product Serial
 Number?

Your serial number uniquely identifies your purchase of NI software. For help
 finding the serial number on the Certificate of Ownership included in your software
 kit, refer to Finding the Serial Number or System Tag of My NI
 Product.

Help

»

About

#### What Is a Computer ID?

The computer ID is a 16-character value that uniquely identifies your computer. NI
 requires this information to enable your software. You can find your computer ID
 through the NI Licensing Wizard or by using NI License Manager, as follows:

- Launch the NI License Manager.
- Click Computer
 Information in the ribbon.

For more information about product activation and licensing, refer to
 *Activating NI Software Products*.

#### How Can I Evaluate NI
 Software?

You can evaluate most NI products in accordance with the license agreement.
 Evaluation terms vary, depending on which product you want to evaluate. Refer to
 your product documentation for specific information on the product's evaluation
 mode.

#### Moving Software after
 Activation

To transfer your software to another computer, uninstall the software on the first
 computer, then install and activate it on the second computer. You can transfer your
 software from one computer to another; you do not need to contact or inform NI of
 the transfer. Because activation codes are unique to each computer, you will need a
 new activation code. Refer to the *How do I Activate my Software?*
 section to learn how to acquire a new activation code and reactivate your software.

#### Deactivating a Product

To deactivate a product, open NI License Manager and navigate to the Local
 Licenses view. Select the product to be deactivated and click
 Deactivate. If the product was in evaluation mode before
 activation, the properties of the evaluation mode may not be restored.

If you
 cannot access NI License Manager on the host computer, contact NI to deactivate the
 product.

#### Using Windows Guest
 Accounts

NI License Manager does not support Microsoft Windows Guest accounts. You must log
 in to a non-Guest account to run licensed NI application software.

Parent topic:

VeriStand Licensing Options

Related tasks:

- Integrating Virtual ECUs

Related information:

- Installing, Updating, Repairing, and Removing NI
 Software
- Download VeriStand
- License Setup and Activation

<!--NI_TOPIC bundle=veristand path=adapt-c-template.html language=enus -->
## TOPIC 00004: Adapting the C Template to Model Code

- bundle_id: `veristand`
- source_path: `adapt-c-template.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/adapt-c-template.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the template.c file that the VeriStand Model Framework installs as a starting point for your model code. Before you begin, create a model header file. Browse to <RootDrive>\VeriStand\<xxxx>\ModelInterface\custom\examples, create a copy of template.c, and give the copy a new name. <RootDrive> is

### Adapting the C Template to Model Code

Use the template.c file that the VeriStand
 Model Framework installs as a starting point for your model code.

Before you begin, create a model header
 file.

1. Browse to
 <RootDrive>\VeriStand\<xxxx>\ModelInterface\custom\examples,
 create a copy of template.c, and give the copy a new name. 
 Note 
<RootDrive>
 is the drive where NI software installs and <xxxx> is the
 VeriStand version number.
2. Modify the following files. 
 File
Descriptiontemplate.c copy
Lists the code you must customize, which is marked with TO DO comments. This
 file also contains information about how to instantiate and access
 parameters.
ni_modelframework.h
Lists definitions for properties of outward-facing components of your model,
 such as inports, outports, parameters, and signals.Note This file is located in the
 RootDrive:\VeriStand\xxxx\ModelInterface\
 directory.

After you adapt the template, create a
 makefile to compile the model.

Parent topic:

Using Models from C and C++

Parent topic:

Model Code Components

<!--NI_TOPIC bundle=veristand path=add-alarm.html language=enus -->
## TOPIC 00005: Adding an Alarm

- bundle_id: `veristand`
- source_path: `add-alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-alarm.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add alarms to notify users that the value of a channel is outside a specified range or to trigger a procedure. Launch your project in the VeriStand Editor. Click View System Definition . In the System Definition Palette, right-click Alarms and select New Folder to create a sub-folder to organize you

### Adding an Alarm

Add alarms to notify users that the value of a channel is outside a specified range or to
 trigger a procedure.

1. Launch your project in the VeriStand Editor.
2. Click View»System Definition.
3. Optional: 
 In the System Definition Palette, right-click
 Alarms and select New»Folder to create a sub-folder to organize your alarms.
4. Right click Alarms or the sub-folder you created and
 select New»Alarm.
5. In the Create a New Alarm dialog box, configure the
 alarm. 
 Note If you need the
 Re-arm behavior to trigger based on a procedure,
 create the procedure first.
6. Click OK. The new alarm appears under
 Alarms or in the subfolder you selected. 
 Note You can update the alarm configuration by right-clicking the alarm and
 selecting Properties.
7. Save the system definition file.

Add status channel

Parent topic:

Adding and Configuring Alarms

Related tasks:

- Setting an Alarm Priority
- Assigning an Alarm Group

<!--NI_TOPIC bundle=veristand path=add-calculated-channel-mapping-diagram.html language=enus -->
## TOPIC 00006: Adding a Calculated Channel

- bundle_id: `veristand`
- source_path: `add-calculated-channel-mapping-diagram.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-calculated-channel-mapping-diagram.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations. Open VeriStand. In the VeriStand Editor, click Project Files. Right-click your system definition file (.nivsdf) and select Open. Click the Software palette and drag one of the followin

### Adding a Calculated Channel

Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations.

1. Open VeriStand.
2. In the VeriStand Editor, click Project Files.
3. Right-click your system definition file (.nivsdf) and
 select Open.
4. Click the Software palette and drag one of the following
 calculated channels onto the diagram. 
 Calculated channel
DescriptionAcceleration
Calculates the acceleration and velocity
 of the input channel.
Average
Calculates the average value of the input
 channel.
Conditional
Compares X with Y based on the configured
 condition. This channel outputs W for true and Z for
 false.
Formula
Calculates the result of the formula you
 specify.
Lowpass Filter
Applies a lowpass Butterworth filter to
 the input channel.
Maximum
Compares two values and returns the larger
 value.
Minimum
Compares two values and returns the
 smaller value.
Peak and Valley
Calculates the peak, valley, and offset of
 a cyclical waveform produced by the input channel. This
 calculation is performed by running the incoming value
 through a lowpass Butterworth filter and comparing the
 filtered value to previous maximum and minimum
 values.
5. Use the Configuration pane to configure the calculated
 channel.
6. Save the system definition file.

Parent topic:

Tailoring Channels

<!--NI_TOPIC bundle=veristand path=add-can-flexray-lin-port.html language=enus -->
## TOPIC 00007: Adding a CAN, FlexRay, or LIN Port

- bundle_id: `veristand`
- source_path: `add-can-flexray-lin-port.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-can-flexray-lin-port.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an NI-XNET CAN, FlexRay, or LIN port to a system definition file for in-vehicle network communication. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Click Targets Controller Hardware

### Adding a CAN, FlexRay, or LIN Port

Add an NI-XNET CAN, FlexRay, or LIN port to a system definition file for in-vehicle
 network communication.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET in the configuration tree.
4. Select the type of port you want to add.
5. Click Add CAN/FlexRay/LIN Port to display the
 Add New NI-XNET CAN/FlexRay/LIN Port dialog
 box.
6. Enter a port name, address, XNET database, and cluster within the database to
 associate with the port, and click OK.
7. Save the system definition file.

Expand the port to view sections for adding incoming and
 outgoing frames, data logging files, and other options. Use the CAN, FlexRay, or LIN
 Port configuration page to configure additional settings for the newly added
 port.

Parent topic:

Adding NI-XNET Devices

Related information:

- Using NI-XNET CAN, LIN, and FlexRay Interfaces

<!--NI_TOPIC bundle=veristand path=add-configure-alarm.html language=enus -->
## TOPIC 00008: Adding and Configuring Alarms

- bundle_id: `veristand`
- source_path: `add-configure-alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-alarm.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Notify users when a channel value is outside a specified range. Add and configure alarms with the VeriStand Editor, System Explorer, and Workspace. Depending on your goal, access the following locations to add and configure alarms. Goal Location How to Access Add a new alarm to the system definition

### Adding and Configuring Alarms

Notify users when a channel value is outside a specified range.

VeriStand
 Editor

System Explorer

Workspace

Depending on your goal, access the following locations to add and configure
 alarms.

| Goal | Location | How to Access |
| --- | --- | --- |
| Add a new alarm to the system definition file. Assign alarms to groups. Set alarm priorities. Configure alarm settings. | VeriStand Editor | Use the System Definition palette. |
| Configure an alarm to trigger for a specific channel value. | Use the Mapping Diagram. |  |
| Manage alarms at run time in the VeriStand Editor. View the current status of alarms in a deployed project. Acknowledge and unacknowledge alarms. Enable and disable alarms. View the history of triggered alarms and export the history to a file. | Click View » Alarm Monitor, |  |
| Add a new procedure to the system definition file. Configure the automated actions that occur during a procedure. | System Explorer | Click Targets » Controller » Procedures. |
| Manage alarms at run time in the Workspace. View the current status of alarms in a deployed project. Acknowledge alarms or mark them as unacknowledged. Enable and disable alarms. View the history of triggered alarms and export the history to a file. | Workspace | Open the Alarm Monitor tool. |

Parent topic:

Configuring a System Definition File

Related reference:

- VeriStand Environment

<!--NI_TOPIC bundle=veristand path=add-configure-controls-indicators.html language=enus -->
## TOPIC 00009: Adding and Configuring Controls and Indicators

- bundle_id: `veristand`
- source_path: `add-configure-controls-indicators.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-controls-indicators.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Workspace Controls palette to add controls and indicators, then configure item properties for a custom Workspace user interface. Open the Workspace. Select Screen Edit Mode to display the Workspace Controls palette and alignment grid. Click the Workspace Controls palette and drag a control o

### Adding and Configuring Controls and
 Indicators

Use the Workspace Controls palette to add controls and indicators, then configure
 item properties for a custom Workspace user interface.

1. Open the Workspace.
2. Select Screen»Edit Mode to display the Workspace
 Controls palette and alignment grid.
3. Click the Workspace Controls palette and
 drag a control or indicator onto the alignment grid.
4. In the Item Properties dialog box,
 configure the control or indicator. 
 Note If the
 Workspace contains simple or
 FFT graph controls and the project that owns the
 screen file connects to the VeriStand Gateway
 running on a remote target, you must set the
 TTL value to 128 on the
 Port Settings page of the
 Options dialog box.
 Otherwise, these graph controls will not update.

Parent topic:

Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=add-configure-custom-device.html language=enus -->
## TOPIC 00010: Adding and Configuring a Custom Device

- bundle_id: `veristand`
- source_path: `add-configure-custom-device.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-custom-device.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add and configure third-party custom devices to execute user-defined actions, determined by LabVIEW VIs. You can add a custom device to a system definition file without installing LabVIEW. However, you must install LabVIEW to create a custom device. Launch your project in the VeriStand Editor. In th

### Adding and Configuring a Custom Device

Add and configure third-party custom devices to execute user-defined actions, determined by LabVIEW VIs.

Note

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller in the configuration tree.
4. Right-click Custom Devices and select a device from the
 drop-down menu.
5. Configure the custom device.
6. Save the system definition file.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=add-configure-daq.html language=enus -->
## TOPIC 00011: Adding and Configuring a DAQ Device

- bundle_id: `veristand`
- source_path: `add-configure-daq.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-daq.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add NI DAQ devices to a VeriStand system definition, then configure DAQ channels for analog, digital, or counter I/O. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Click Targets Controll

### Adding and Configuring a DAQ Device

Add NI DAQ devices to a VeriStand system definition, then configure DAQ channels for
 analog, digital, or counter I/O.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
4. Choose to add one or all discoverable DAQ devices. 
 Number of DevicesHow to AddOne
Click Add DAQ Device.
Use the Add DAQ Devicedialog box to
 identify the DAQ device you want to add.
Click OK.All
Click Hardware Discovery Wizard and
 follow the onscreen instructions.
Right-click a device and select Add
 Channels to display the Add DAQ
 Channels dialog box.
5. Use the Add DAQ Channels dialog box to configure the type
 of physical channel to add and their properties. 
 Note For analog input channels,
 you must choose to acquire the signal a single point at a time or over a
 period of time as waveform.
6. Click Next.
7. Select the specific channels on the device you want to add to the system
 definition. 
 Note If the DAQ device does not contain channels of the type you specified,
 such as AO or DI, no channels are available to select.
8. Click Finish.
9. Save the system definition file.

After you add a DAQ device, you can add and configure
 more channels. Add an internal channel to a DAQ device by right-clicking
 the device and selecting Add Internal Channel.

You can also add a SCXI module to a DAQ device by right-clicking the device and
 selecting Add SCXI Modules. Use the Add SCXI Module dialog
 box to configure the module.

Parent topic:

Adding and Configuring a Hardware Device

<!--NI_TOPIC bundle=veristand path=add-configure-hardware-device.html language=enus -->
## TOPIC 00012: Adding and Configuring a Hardware Device

- bundle_id: `veristand`
- source_path: `add-configure-hardware-device.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-hardware-device.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add and configure NI hardware, timing and sync devices, and custom devices. Open a project in VeriStand. Depending on your hardware goal, complete any of the following tasks in System Explorer. Goal Task Adding and configuring an SLSC device Use SLSC devices to introduce signal conditioning and faul

### Adding and Configuring a Hardware
 Device

Add and configure NI hardware, timing and sync devices, and custom
 devices.

1. Open a project in VeriStand.
2. Depending on your hardware goal, complete any of the following
 tasks in System Explorer. 
 Goal
TaskAdding and configuring an SLSC
 device
Use SLSC
 devices to introduce signal conditioning and fault
 insertion into a real-time testing
 scheme.
Adding and configuring DAQ
 devices
Use DAQ devices
 to support analog, digital, and counter I/O
 functions such as acquiring waveform
 data.
Adding NI FPGA
 targets
Use NI FPGA
 targets to create customizable I/O, help with data
 preprocessing and postprocessing, add high-speed
 closed-loop control, and simulate a variety of
 sensors for hardware-in-the-loop testers
Adding NI-XNET
 devices
Use the
 NI-XNET platform to communicate with hardware
 using the CAN, LIN, and FlexRay
 protocols.
Adding reflective memory
 networks
Use a
 reflective memory card to split up a simulation
 model to execute simultaneously on different
 target systems.
Adding and configuring timing and
 sync devices
Use a
 timing and sync device to synchronize more than
 one chassis.
Synchronizing hardware and
 software
Synchronize the hardware and software components
 of a system to ensure consistency and optimal
 performance, enable data analysis, and time
 correlation.
Setting chassis master hardware
 synchronization devices
Use a
 chassis master hardware synchronization device to
 control the synchronization of all hardware in a
 chassis.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=add-configure-model.html language=enus -->
## TOPIC 00013: Adding and Configuring a Model

- bundle_id: `veristand`
- source_path: `add-configure-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-model.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect a model to other parts of the system and run the model on a hardware target. Before you begin, you must compile the model to use it. To learn more about models, refer to and . VeriStand executes each model in its own loop. If a system definition contains multiple models referencing the same

### Adding and Configuring a Model

Connect a model to other parts of the system and run the model on a hardware target.

Before you begin, you must compile the model to use it.
 To learn more about models, refer to and .

Note

1. Launch your project in the VeriStand Editor.
2. On the Mapping Diagram on the
 Palette, click Software»Simulation Model and drop the model node on the diagram.
3. In the Open dialog box, select a simulation model and
 click Open. 
 The Mapping Diagram will load the model.
4. In the Configuration pane, use the
 Item tab to modify the model.
  1. Set the Initial state of the model to Running or
 Paused. 
 Note To change the
 values of model parameters before the first time step, set the
 Initial state to
 Paused.
  2. Set the Decimation of the model rate.
  3. Click Import parameters.
  4. In the Import Parameters dialog box, select the
 parameters you want to import as channels and click
 OK. 
 The parameters you selected appears inside the node when you
 expand it. Note Importing too many parameters negatively impacts system
 performance.
  5. Click Import signals.
  6. In the Import Signals dialog box, select the
 signals you want to import as a channels and click
 OK. 
 The signals you selected appears inside the node when you expand
 it. Note Importing too
 many signals negatively impacts system
 performance.
  7. Optional: 
 If your model contains a vector inport or outport, set the
 Vector port specification as
 Segment into scalar channels or
 Maintain as vector channel. 
 Note Scalar channels
 provide greater flexibility than vector channels. Vector channels
 only map to models that contain a vector channel of the same size.
 You cannot map a vector channel to controls or indicators on your
 Workspace or use it with calculated
 channels, alarms, procedures, and others.
5. Wire the channels to create mappings.
6. Depending on your goal, complete the following tasks to configure the model
 further. 
 Goal
TaskSet
 model timing
Adjust the step size
 to have the model run at a different rate.
Set
 model parameters
Use the
 VeriStand Editor,
 Workspace, Model
 Parameter Manager, and Stimulus
 Profile Editor to set the values of model
 parameters.
Scope
 global parameters
Update the scope
 of all global parameters in a model to the target-level
 or model-level.
Set the
 default values for inports
Change the default
 value for an inport to prevent your models from using
 invalid values.
Configure the execution order of multiple
 models
Define the order
 that the Primary Control Loop (PCL) executes
 models.
7. Save the system definition file.

After adding the model to the system definition, use model execution
 channels to interact with models.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=add-configure-procedure.html language=enus -->
## TOPIC 00014: Adding and Configuring a Procedure

- bundle_id: `veristand`
- source_path: `add-configure-procedure.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-procedure.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Set the actions the VeriStand Engine executes in response to an alarm, when called from another procedure, or as a startup procedure. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Click

### Adding and Configuring a Procedure

Set the actions the VeriStand Engine executes in response to an alarm, when called from
 another procedure, or as a startup procedure.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Procedures in the configuration tree.
4. Click Add Procedure to add an empty procedure to the
 configuration tree.
5. Use the Procedure Configuration page that appears to the
 right of the configuration tree to configure the procedure.
6. Save the system definition file.

Now that you have added a procedure,
 you can call that
 procedure from multiple alarms.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=add-configure-slsc.html language=enus -->
## TOPIC 00015: Adding and Configuring an SLSC device

- bundle_id: `veristand`
- source_path: `add-configure-slsc.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-slsc.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an SLSC chassis to a VeriStand system definition, then configure module settings for signal conditioning and fault insertion. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Click Targ

### Adding and Configuring an SLSC device

Add an SLSC chassis to a VeriStand system definition, then configure module settings
 for signal conditioning and fault insertion.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»SLSC in the configuration tree.
4. Right-click SLSC and click Add SLSC
 Chassis.
5. In the Add SLSC Chassis dialog box, use the
 Connect with drop-down to specify whether to connect
 to the chassis using the chassis name or the host name or IP address.
6. Enter the chassis name, host name, or IP address.
7. Enter a Username and Password for
 the engine to log into the SLSC chassis. 
 Note Entering a user name and
 password removes the requirement for custom devices to separately log into
 the SLSC chassis. If the credentials are incorrect when the engine attempts
 to log into the SLSC chassis, VeriStand will undeploy the system definition.
 By default, the user name is anonymous and the
 password left empty.
8. Click OK.
9. In the configuration tree, navigate to SLSC Chassis»Modules under your SLSC chassis.
10. Use the drop-down menus under SLSC Modules Settings to select the modules in
 each of the chassis slots.
11. Save the system definition file.

Parent topic:

Adding and Configuring a Hardware Device

Related concepts:

- SLSC Systems in Real-Time Schemes

<!--NI_TOPIC bundle=veristand path=add-configure-timing-sync.html language=enus -->
## TOPIC 00016: Adding and Configuring Timing and Sync Devices

- bundle_id: `veristand`
- source_path: `add-configure-timing-sync.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-configure-timing-sync.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a timing and sync device to a VeriStand system definition to synchronize multiple chassis and configure device settings. You must add a timing and sync device to the Timing and Sync directory of VeriStand in order to add it to the system definition. VeriStand includes one example timing and sync

### Adding and Configuring Timing and Sync
 Devices

Add a timing and sync device to a VeriStand system definition to synchronize
 multiple chassis and configure device settings.

Timing and Sync

VeriStand includes one example timing and
 sync device. You can add a timing and sync device to a system definition
 file without installing LabVIEW. However, you must install the LabVIEW
 development environment to create a custom timing and sync device.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»Timing and Sync in the configuration tree.
4. Right-click Timing and Sync.
5. From the drop-down menu, select a timing and sync device.
6. Use the Timing and Sync Configuration page
 to configure the device.
7. Save the system definition file.

Parent topic:

Adding and Configuring a Hardware Device

Related information:

- Creating Custom Timing and Sync Devices

<!--NI_TOPIC bundle=veristand path=add-custom-files.html language=enus -->
## TOPIC 00017: Adding Custom Files

- bundle_id: `veristand`
- source_path: `add-custom-files.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-custom-files.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add custom files such as documentation to a project file so they appear in the Project Files tab. Launch your project in the VeriStand Editor. Set the Gateway IP address of the host running the VeriStand Gateway. Click New Add File. In the Select Item window, select a file, and click Open. The file

### Adding Custom Files

Add custom files such as documentation to a project file so they appear in the
 Project Files tab.

1. Launch your project in the VeriStand Editor.
2. Set the Gateway IP address of the host running the VeriStand Gateway.
3. Click New»Add File.
4. In the Select Item window, select a file, and click
 Open.

Project Files

Parent topic:

Configuring a Project File

<!--NI_TOPIC bundle=veristand path=add-edit-expressions.html language=enus -->
## TOPIC 00018: Adding and Editing Expressions in a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `add-edit-expressions.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-edit-expressions.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use expressions to access and act on the variables you define for a real-time sequence. Expressions are the building blocks of real-time sequence code. Depending on your goal, complete the following tasks. Goal Tasks Create a new, empty expression Drag an Expression primitive from the Expressions pa

### Adding and Editing Expressions in a Real-Time
 Sequence

Use expressions to access and act on the variables you define for a real-time
 sequence.

Expressions

1. Depending on your goal, complete the following tasks. 
 Goal
TasksCreate a new, empty expression
Drag an Expression primitive from the
 Expressions palette to the sequence
 code.
create an expression that automatically includes a
 variable.
Drag a declared variable from the
 Variables pane to the sequence
 code.
create an expression that automatically includes a
 sequence
Drag a real-time sequence from the
 Sequences palette or the
 References pane to the sequence
 code.
2. In the Property Browser, build the expression as a
 mathematical operation. 
 Note As you begin typing in the Expression field, a type-ahead menu appears
 with valid functions or variables you can include in the expression. You can
 connect these functions and variables with operators.

If the new expression contains a variable that is not
 already declared in the sequence, declare the variable.

Parent topic:

Creating Real-Time Sequences

<!--NI_TOPIC bundle=veristand path=add-fpga.html language=enus -->
## TOPIC 00019: Adding NI FPGA Targets

- bundle_id: `veristand`
- source_path: `add-fpga.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-fpga.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an NI FPGA target and FPGA configuration file to a system definition file for customizable I/O and control. You can add an FPGA target and corresponding FPGA configuration file to a system definition file without installing the LabVIEW FPGA Module. However, you must install the LabVIEW FPGA Modu

### Adding NI FPGA Targets

Add an NI FPGA target and FPGA configuration file to a system definition file for
 customizable I/O and control.

You can add an FPGA target and corresponding
 FPGA configuration file to a system definition file without installing the LabVIEW FPGA
 Module. However, you must install the LabVIEW FPGA Module to create a custom FPGA
 bitfile and configuration file.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»FPGA in the configuration tree.
4. Choose to add one or all discoverable FPGA targets. 
 Number of DevicesHow to AddOne
Click Add FPGA Target.
Select an FPGA configuration file
Click OK.All
Click Hardware Discovery Wizard and
 follow the onscreen instructions.
Select a target to display its configuration page.
In the path control, select the FPGA configuration file.
5. Save the system definition file.

You can configure the FPGA device and its individual
 channels with the FPGA Target and FPGA
 Channel configuration pages.

Parent topic:

Adding and Configuring a Hardware Device

Related information:

- Customizing an FPGA Target

<!--NI_TOPIC bundle=veristand path=add-on.html language=enus -->
## TOPIC 00020: Adding Custom Software

- bundle_id: `veristand`
- source_path: `add-on.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-on.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Integrate add-ons, plug-ins, and custom devices. You can use LabVIEW to create various types of custom add-ons and plug-ins to extend VeriStand. Add-on features for VeriStand include: Custom user interface objects for the Workspace. Custom devices that add support for additional hardware interfaces.

### Adding Custom Software

Integrate add-ons, plug-ins, and custom devices.

You can use LabVIEW to create various types of custom add-ons and plug-ins to extend
 VeriStand.

- Custom user interface objects for the Workspace .
- Custom devices that add support for additional hardware interfaces.
- Real-time engine functions.

The following table lists different types of add-ons.

| Type of add-on | Description |
| --- | --- |
| Installed with Veristand | Use NI supported custom devices included with the VeriStand suite installer. For example, the Embedded Data Logger is available from the suite. These custom devices are available for both offline and online installation. |
| Installed by another NI product | Purchase software packages that add specialized features to VeriStand. For example, the ECU Measurement and Calibration Toolkit adds the XCP or CCP Master custom device and workspace controls to VeriStand. |
| Available for download | Download VeriStand Add-ons from NI and the VeriStand community. |
| User created | Use LabVIEW to create various types of custom add-ons for VeriStand. VeriStand installs a full palette of VeriStand VIs and the VeriStand .NET APIs. You can access both from LabVIEW.Note To develop add-ons, you must install matching versions of LabVIEW and VeriStand. For example, you must use LabVIEW 2020 to develop add-ons for VeriStand 2020. |

#### System Requirements for Common
 Add-ons

Certain add-ons require additional LabVIEW modules, toolkits, or
 features not included with the Base Development System, such as the Application
 Builder.

The following table lists common add-ons you can develop using
 LabVIEW and any additional features they require.

| Add-on | Requirements |
| --- | --- |
| Custom devices | Application Builder1 |
| Custom timing and sync devices |  |
| Custom FPGA configuration files and bitfiles | Application Builder LabVIEW FPGA Module |
| Custom Workspace tools | — |
| Custom Workspace controls and indicators2 |  |
| Compiled models | Application Builder LabVIEW Control Design and Simulation Module |
| 1 The Application Builder is included with the LabVIEW Professional Development System. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder. 2 For more information on how to use LabVIEW to create custom workspace objects, refer to Creating Custom Workspace Objects for VeriStand. |  |

<!--NI_TOPIC bundle=veristand path=add-reflective-memory.html language=enus -->
## TOPIC 00021: Adding Reflective Memory Networks

- bundle_id: `veristand`
- source_path: `add-reflective-memory.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-reflective-memory.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add reflective memory cards to a VeriStand system definition to share data across multiple target systems in real time. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Click Targets Contro

### Adding Reflective Memory Networks

Add reflective memory cards to a VeriStand system definition to share data across
 multiple target systems in real time.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»Data Sharing in the configuration tree.
4. Choose to add one or all discoverable reflective memory cards. 
 Number of DevicesHow to AddOne
 Right-click Data Sharing.
 Select Add Reflective Memory.All
 Click Hardware Discovery Wizard and
 follow the onscreen instructions.Note The wizard
 lists reflective memory cards in the GE
 category.
5. Configure the reflective memory network using the Reflective Memory
 Configuration page.
6. Save the system definition file.

Parent topic:

Adding and Configuring a Hardware Device

<!--NI_TOPIC bundle=veristand path=add-services.html language=enus -->
## TOPIC 00022: Adding Custom VIs

- bundle_id: `veristand`
- source_path: `add-services.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-services.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a custom LabVIEW VI to a VeriStand system definition by importing a source distribution in the VeriStand Editor. Before you begin, build the VI into a source distribution. Open the VeriStand Editor. Set the Gateway IP address of the host running the VeriStand Gateway. Click New Add File. In the

### Adding Custom VIs

Add a custom LabVIEW VI to a VeriStand system definition by importing a source
 distribution in the VeriStand Editor.

Before you begin, build the VI into a source distribution.

1. Open the VeriStand Editor.
2. Set the Gateway IP address of the host running the VeriStand Gateway.
3. Click New»Add File.
4. In the Select Item window, select a custom VI and click
 OK.
5. Optional: 
 In the Project Files tab, right-click the custom VI and click
 Run On Deploy. 
 Note Enabling this option allows VeriStand
 to automatically run the VI when the system definition deploys.

Parent topic:

Creating a VI Source Distribution

<!--NI_TOPIC bundle=veristand path=add-system-definition.html language=enus -->
## TOPIC 00023: Adding and Activating a System Definition File

- bundle_id: `veristand`
- source_path: `add-system-definition.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-system-definition.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Reuse or add new system definition files to VeriStand projects. Before you begin, create a new system definition file. Launch your project in the VeriStand Editor. Click New Add File. In the Select Item window, select a system definition file (.nivssdf), and click Open. In the VeriStand Editor, clic

### Adding and Activating a System Definition
 File

Reuse or add new system definition files to VeriStand projects.

Before you begin, create a new system definition
 file.

1. Launch your project in the VeriStand Editor.
2. Click New»Add File.
3. In the Select Item window, select a system definition file
 (.nivssdf), and click Open.
4. In the VeriStand Editor, click the Project
 Files tab.
5. Right-click the new system definition file and click Make
 Active.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=add-user-channel.html language=enus -->
## TOPIC 00024: Adding a User Channel

- bundle_id: `veristand`
- source_path: `add-user-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-user-channel.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations. Extend user channel functionality by mapping a channel to other channels. For example, use a single user channel to start multiple models simultaneously by mapping the user channel to

### Adding a User Channel

Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations.

Note

1. Launch your project in the VeriStand Editor.
2. Click View»System Definition.
3. Optional: 
 In the System Definition Palette, right-click
 User Channels and select New»Folder to create a sub-folder for your user channels.
4. Right click User Channels or the sub-folder you created
 and select New»User Channel. 
 Note To add more than one user
 channel, select New»Multiple user channels and use the Create Multiple User
 Channels dialog box to configure the user channels.
5. In the Create a New User Channel dialog box, enter a
 Name, Description,
 Unit, and Initial Value.
6. Click OK.
7. Save the system definition file.

Mapping
 Diagram

Note

System Definition Palette

Delete

Properties

Parent topic:

Tailoring Channels

<!--NI_TOPIC bundle=veristand path=add-waveform-task-channels.html language=enus -->
## TOPIC 00025: Adding Waveform Task Channels

- bundle_id: `veristand`
- source_path: `add-waveform-task-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-waveform-task-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Analog Input (AI) channels with waveform tasks to control waveform acquisitions by DAQ devices, such as how VeriStand logs waveform data and defines triggers that start and stop acquisitions. As part of setting up an AI channel(s) to acquire waveforms, you need to specify the rate, size, and oth

### Adding Waveform Task Channels

Use Analog Input (AI) channels with waveform tasks to control waveform acquisitions
 by DAQ devices, such as how VeriStand logs waveform data and defines triggers that start and
 stop acquisitions.

task

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
4. Depending on your goal, add one of the following task channels. 
 Note You can write to these
 channels at run time.
 Goals
 Task Channel
 How to AddSet a task to an active, running
 state.
 Task Enabled
 Always available under each task.
 Specify if logging occurs during
 acquisitions.
 Logging Enabled
 In the Logging Configuration page,
 click Allow TDMS logging.
 Specify when logging stops and begins with
 a new file.
 Start New File
 Set a finite task to automatically restart
 itself and wait for a new trigger when the acquisition is
 complete.
 Retriggerable
 In the Triggers Configuration page,
 set Acquisition mode to
 Finite.
 Set a software start trigger to begin an
 acquisition.
 Start Trigger
 In the Triggers Configuration page,
 set Trigger type to
 Software.
5. Save the system definition file.

Parent topic:

Setting Up Timing and Logging Properties for Waveform Acquisitions

<!--NI_TOPIC bundle=veristand path=add-xnet-database.html language=enus -->
## TOPIC 00026: Adding NI-XNET Databases

- bundle_id: `veristand`
- source_path: `add-xnet-database.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-xnet-database.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an NI-XNET database to the VeriStand System Explorer to define embedded network communication fromFIBEX (.xml), CANdb (.dbc), NI-CAN (.ncd), or LDF (.ldf) files. Refer to the NI-XNET Hardware and Software Help for detailed information about NI-XNET databases. Launch your project in the VeriStand

### Adding NI-XNET Databases

Add an NI-XNET database to the VeriStand System Explorer to define embedded network
 communication fromFIBEX (.xml), CANdb (.dbc),
 NI-CAN (.ncd), or LDF (.ldf) files.

Note

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»XNET Databases in the configuration tree.
4. Click Add Database File
 [IMAGE alt='image' src='GUID-9AD8A9F0-14F5-4A6D-9F41-CBC57539FDBD-a5.png'] and choose where you want to add the database from. 
 Database locationHow to addA registered NI-XNET database
 Click Registered XNET Database.
 Select an Existing Alias from the
 drop-down menu.A database on disk
 Click New XNET Database.
 Enter an Alias.
 Click the Path folder.
 In the Select a File or Folder window,
 select a database file.
 Click OK.
5. Click OK. 
 Note If OK is disabled, confirm
 that you selected a valid database file and that the database does not
 already appear under XNET Databases.
6. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

<!--NI_TOPIC bundle=veristand path=add-xnet-port.html language=enus -->
## TOPIC 00027: Adding an NI-XNET Port

- bundle_id: `veristand`
- source_path: `add-xnet-port.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-xnet-port.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Hardware Discovery Wizard to find NI-XNET devices on connected targets and add NI-XNET ports. Associate each port with an XNET database and cluster for CAN, FlexRay, or LIN communication. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System

### Adding an NI-XNET Port

Use the Hardware Discovery Wizard to find NI-XNET devices on connected targets and
 add NI-XNET ports. Associate each port with an XNET database and cluster for CAN, FlexRay,
 or LIN communication.

1. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
2. Click Targets»Controller»Hardware»Chassis»NI-XNET in the configuration tree.
3. Click Hardware Discovery Wizard and follow the onscreen
 instructions. 
 The new NI-XNET device(s) appears under the appropriate section in the
 configuration tree.Note You can
 restrict the type of NI-XNET device to discover. Select
 CAN, FlexRay, or
 LIN, in the configuration tree and click
 Hardware Discovery Wizard.
4. Select each new port to display its configuration page.
5. Specify the XNET database and cluster within the database to associate with the
 port.
6. Save the system definition file.

Expand the port to view sections for adding incoming and
 outgoing frames, data logging files, and other options. Use the CAN, FlexRay, or LIN
 Port configuration page to configure additional settings for the newly added
 port.

Parent topic:

Adding NI-XNET Devices

Related information:

- Using NI-XNET CAN, LIN, and FlexRay Interfaces

<!--NI_TOPIC bundle=veristand path=add-xnet.html language=enus -->
## TOPIC 00028: Adding NI-XNET Devices

- bundle_id: `veristand`
- source_path: `add-xnet.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/add-xnet.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure an NI-XNET session by adding device ports under the selected protocol in the system definition file. NI-XNET supports CAN, LIN, and FlexRay communication on connected targets. You can configure an NI-XNET session by adding ports for your devices under the protocol you want to use. Dependin

### Adding NI-XNET Devices

Configure an NI-XNET session by adding device ports under the selected
 protocol in the system definition file. NI-XNET supports CAN, LIN, and
 FlexRay communication on connected targets.

You can configure an NI-XNET session by
 adding ports for your devices under the protocol you want to
 use.

Depending on your goal, complete any of the following tasks.

| Goal | Task |
| --- | --- |
| Adding any type of NI-XNET port | Discover all NI-XNET devices on connected targets and automatically add ports for them to the system definition file. |
| Adding a CAN, FlexRay, or LIN port | Add a CAN, FlexRay, or LIN port to a system definition file. |

Parent topic:

Adding and Configuring a Hardware Device

Related information:

- Using NI-XNET CAN, LIN, and FlexRay Interfaces

<!--NI_TOPIC bundle=veristand path=adding-a-custom-device-with-runtime-configurable-channels.html language=enus -->
## TOPIC 00029: Adding a Custom Device with Runtime-Configurable Channels

- bundle_id: `veristand`
- source_path: `adding-a-custom-device-with-runtime-configurable-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/adding-a-custom-device-with-runtime-configurable-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a custom device with channels that you can dynamically add, change, or remove during system operation. Open your system definition file in the VeriStand Editor and click Configure. Add the custom device and configure the static parameters. Navigate to the Custom Device Runtime Configuration Sect

### Adding a Custom Device with
 Runtime-Configurable Channels

Add a custom device with channels that you can dynamically add, change, or remove during
 system operation.

1. Open your system definition file in the VeriStand Editor and click
 Configure.
2. Add the custom device and configure the static parameters.
3. Navigate to the Custom Device Runtime Configuration Section
 Specification window defined by the custom device
 developer.
4. Configure the runtime-configurable channel settings.
  1. For Reserved Channel Capacity, specify the
 number of channels you can add under this section during system
 deployment. 
 Note Each element in a multidimentional channel
 counts as one channel.
  2. Enable Is Faultable to allow fault injection for
 channels within this section.
  3. Enable Is Scalable to allow scaling for channels
 withing this section.

Parent topic:

Overview of Runtime Configurability

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=adding-configuring-virtual-ecus.html language=enus -->
## TOPIC 00030: Adding and Configuring Virtual ECUs

- bundle_id: `veristand`
- source_path: `adding-configuring-virtual-ecus.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/adding-configuring-virtual-ecus.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Incorporate a virtual ECU with the system definition file. Launch your project in the VeriStand Editor. On the Mapping Diagram on the Palette, click Software Virtual ECU and drop the node on the diagram. In the Open dialog box, select a virtual ECU and click Open. The Mapping Diagram imports the vir

### Adding and Configuring Virtual ECUs

Incorporate a virtual ECU with the system definition file.

1. Launch your project in the VeriStand Editor.
2. On the Mapping Diagram on the
 Palette, click Software»Virtual ECU and drop the node on the diagram.
3. In the Open dialog box, select a virtual ECU and click
 Open. 
 The Mapping Diagram imports the virtual ECU you
 built.
4. In the Configuration pane, use the
 Item tab to configure the virtual ECU.
  1. Set the Initial state of the virtual ECU to
 Running or
 Paused. 
 Note To change the
 values of virtual ECU parameters before the first time step, set the
 Initial state to
 Paused.
  2. Set the Decimation of the virtual ECU
 rate.
  3. Click Import parameters.
  4. In the Import Parameters dialog box, select the
 parameters you want to import as channels and click
 OK. 
 The parameters you selected appear inside the node when you
 expand it. Note Importing too many parameters negatively impacts system
 performance.
  5. Click Import signals.
  6. In the Import Signals dialog box, select the
 signals you want to import as channels and click
 OK. 
 The signals you selected appear inside the node when you expand
 it. Note Importing too
 many signals negatively impacts system
 performance.
  7. Optional: 
 If your virtual ECU contains a vector inport or outport, set the
 Vector port specification as
 Segment into scalar channels or
 Maintain as vector channel. 
 Note Scalar channels
 provide greater flexibility than vector channels. Vector channels
 only map to virtual ECUs that contain a vector channel of the same
 size. You cannot map a vector channel to controls or indicators on
 your Workspace or use it with calculated
 channels, alarms, procedures, and others.
5. Wire the channels to create mappings.
6. Depending on your goal, complete the following tasks to configure the virtual
 ECU further. 
 Goal
 TaskSet virtual ECU timing
 Adjust the step size to have the virtual
 ECU run at a different rate. Note By
 default, VeriStand executes virtual ECUs at 0.01 second
 step size. To change the step size of a virtual ECU, you
 must modify virtual ECU Functional Mockup Unit
 (FMU).
 Set virtual ECU parameters
 Use the VeriStand
 Editor to set the values of virtual ECU
 parameters.
 Scope global parameters
 Update the scope of all global parameters
 in a virtual ECU to the target-level or virtual
 ECU-level.
 Set the default values for inports
 Change the default value for an inport to
 prevent your virtual ECU from using invalid values.
 Configure the execution order of multiple virtual
 ECUs
 Define the order that the Primary Control
 Loop (PCL) executes virtual ECUs.
7. Save the system definition file.

After adding all the virtual ECUs to your
 system, create and configure an ECU network cluster.

Parent topic:

Preparing a System Definition File for Virtual ECUs

Related tasks:

- Creating and Configuring an ECU Network Cluster

<!--NI_TOPIC bundle=veristand path=adding-ctrls.html language=enus -->
## TOPIC 00031: Adding and Configuring Components of a Screen

- bundle_id: `veristand`
- source_path: `adding-ctrls.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/adding-ctrls.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Add controls and indicators to a Screen to modify the user interface of a VeriStand project. The following image highlights the parts of the VeriStand Editor you use to add and configure controls and indicators. 1 System Definition palette—A palette that displays the targets and channels in the curr

### Adding and Configuring Components of a Screen

Add controls and indicators to a Screen to modify the user interface of a VeriStand
 project.

The following image highlights the parts of the VeriStand Editor you use
 to add and configure controls and indicators.

[IMAGE alt='image' src='GUID-F44DD75A-3DAD-4F0F-9AC6-D8C3D0CD665A-a5.png']

| 1 | System Definition palette—A palette that displays the targets and channels in the current system definition file. You can drag channels from the System Definition palette and drop them onto the screen to add controls and indicators for those channels. VeriStand selects an appropriate control or indicator type for the channel. |
| --- | --- |
| 2 | Controls and indicators—Objects you add to the screen to either enter or view data from the system definition. Each control or indicator can accept or display a single type of data, such as a number, a TRUE/FALSE value, or a text string. |
| 3 | Item tab—Collection of options for customizing a selected control or indicator. The options on the Item tab appear only when you select a control or indicator on a screen. |

Parent topic:

Visualizing System State

<!--NI_TOPIC bundle=veristand path=adding-tools-menu-item.html language=enus -->
## TOPIC 00032: Adding a Standard or Custom Tools Menu Item

- bundle_id: `veristand`
- source_path: `adding-tools-menu-item.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/adding-tools-menu-item.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add standard or custom Tools menu items in NI VeriStand to open Workspace dialog boxes for monitoring, calibration, and stimulus operations. Before you begin, build the custom Tools menu item into a source distribution. Use these dialog boxes to perform operations such as monitoring alarms, viewing

### Adding a Standard or Custom Tools Menu
 Item

Add standard or custom Tools menu items in NI VeriStand to open Workspace dialog
 boxes for monitoring, calibration, and stimulus operations.

Before you begin, build the custom Tools menu item into a source
 distribution.

Use these dialog boxes to
 perform operations such as monitoring alarms, viewing channel data, scaling
 and calibrating channels, or running stimulus profiles.

1. Open the VeriStand Editor.
2. Set the Gateway IP address of the host running the VeriStand Gateway.
3. Right-click Workspace and select
 Configure Tools.
4. Use the Tools Properties dialog box to add
 and configure Tools menu items.
5. Click OK.

Parent topic:

Creating a VI Source Distribution

<!--NI_TOPIC bundle=veristand path=advanced-primitives.html language=enus -->
## TOPIC 00033: Advanced Primitives

- bundle_id: `veristand`
- source_path: `advanced-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/advanced-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure advanced operations in the real-time sequence code. Palette object Description Yield A statement that causes the real-time sequence to pause while the Primary Control Loop iterates and then resumes executing the real-time sequence.

### Advanced Primitives

Configure advanced operations in the real-time sequence code.

| Palette object | Description |
| --- | --- |
| Yield | A statement that causes the real-time sequence to pause while the Primary Control Loop iterates and then resumes executing the real-time sequence. |

Parent topic:

Real-Time Sequence Primitives

<!--NI_TOPIC bundle=veristand path=ai-accelerometer.html language=enus -->
## TOPIC 00034: Accelerometer Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-accelerometer.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-accelerometer.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure an accelerometer's analog input (AI) channel properties to measure acceleration. For more information on accelerometers, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Ma

### Accelerometer Channel Properties (AI)

Configure an accelerometer's analog input (AI) channel properties to measure
 acceleration.

For more information on accelerometers, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Input Configuration | Specifies the input terminal configuration to apply to the device channels. Note If you select any configuration other than Same as device, it overrides the configuration you specify for the device on the DAQ Device Configuration page in System Explorer. Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |
| Sensitivity | The sensitivity of the sensor in the units you specify. Refer to the sensor documentation to determine this value. |
| Current Excitation Source | Specifies the source of excitation: External—Use an external excitation source instead of the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. None—Supply no excitation to the channel. For both internal and external current excitation sources, you must use the Current Excitation Value property. |
| Current Excitation Value | The amount of excitation to supply to the sensor. Refer to the sensor documentation to determine this value. |
| dB Reference | Specifies the decibel reference level. When you read samples as a waveform, the decibel reference level is included in the waveform attribute. |
| Coupling Mode | Specifies the coupling for the channel: AC—Removes the DC offset from the signal. DC—Allows VeriStand to measure all of the signal. |

Parent topic:

Adding and Configuring DAQ Device Channels

<!--NI_TOPIC bundle=veristand path=ai-bridge.html language=enus -->
## TOPIC 00035: Bridge Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-bridge.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-bridge.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure a bridge-based sensor's analog input (AI) channel properties to measure its output. For more information on bridge-based sensors, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibr

### Bridge Channel Properties (AI)

Configure a bridge-based sensor's analog input (AI) channel properties to measure its
 output.

For more information on bridge-based sensors, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Bridge Configuration | Specifies what type of bridge configuration to use: Full Bridge Half Bridge Quarter Bridge |
| Excitation Source | Specifies the source of excitation: External—Use an excitation source other than the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. For both internal and external excitation sources, you must use the Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Nominal Bridge Resistance | Specifies the resistance of the bridge while not under load. |
| Enable Offset Null | Specifies whether to perform a bridge offset nulling calibration. |
| Enable Shunt Calibration | Specifies whether to perform a shunt calibration. |
| Shunt Element Location | Specifies the location of the shunt resistor: R1—Between Vch- and Vex+ R2—Between Vch- and Vex- R3—Between Vch+ and Vex- R4—Between Vch+ and Vex+ |
| Shunt Resistance | Specifies the shunt resistance. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |
| In-Situ Calibration (supported devices only) | Specifies whether to perform an in-situ calibration and when to perform the calibration: Before deployment—Perform an in-situ calibration before the system definition is deployed. After undeployment—Perform an in-situ calibration after the system definition is no longer deployed. Both—Perform an in-situ calibration before the system definition is deployed and after the system definition is no longer deployed. None—Do not perform an in-situ calibration. |
| In-Situ Minimum Value (supported devices only) | The minimum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Maximum Value (supported devices only) | The maximum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Input Configuration (supported devices only) | Specifies the input terminal configuration to use when performing the in-situ calibration: Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |

Parent topic:

Adding and Configuring DAQ Device Channels

<!--NI_TOPIC bundle=veristand path=ai-current.html language=enus -->
## TOPIC 00036: Current Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-current.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-current.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure current. For more information on measuring current, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The maxim

### Current Channel Properties (AI)

Configure analog input (AI) channel properties to measure current.

For more information on measuring current, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Input Configuration | Specifies the input terminal configuration to apply to the device channels. Note If you select any configuration other than Same as device, it overrides the configuration you specify for the device on the DAQ Device Configuration page in System Explorer. Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |
| External Shunt Resistance | Specifies the external shunt resistance. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-force.html language=enus -->
## TOPIC 00037: Force Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-force.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-force.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure force. For more information on measuring force, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The maximum v

### Force Channel Properties (AI)

Configure analog input (AI) channel properties to measure force.

For more information on measuring force, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Bridge Configuration | Specifies what type of bridge configuration to use: Full Bridge Half Bridge Quarter Bridge |
| Excitation Source | Specifies the source of excitation: External—Use an excitation source other than the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. For both internal and external excitation sources, you must use the Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Nominal Bridge Resistance | Specifies the resistance of the bridge while not under load. |
| Electrical Units | Specifies from which electrical unit to scale the data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. |
| Scale: 1st Electrical Value | Specifies the first electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 1st Physical Value | Specifies the physical value that corresponds to the first electrical value. |
| Scale: 2nd Electrical Value | Specifies the second electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 2nd Physical Value | Specifies the physical value that corresponds to the second electrical value. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-pressure.html language=enus -->
## TOPIC 00038: Pressure Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-pressure.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-pressure.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure pressure. For more information on measuring pressure, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The max

### Pressure Channel Properties (AI)

Configure analog input (AI) channel properties to measure pressure.

For more information on measuring pressure, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Bridge Configuration | Specifies what type of bridge configuration to use: Full Bridge Half Bridge Quarter Bridge |
| Excitation Source | Specifies the source of excitation: External—Use an excitation source other than the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. For both internal and external excitation sources, you must use the Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Nominal Bridge Resistance | Specifies the resistance of the bridge while not under load. |
| Electrical Units | Specifies from which electrical unit to scale the data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. |
| Scale: 1st Electrical Value | Specifies the first electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 1st Physical Value | Specifies the physical value that corresponds to the first electrical value. |
| Scale: 2nd Electrical Value | Specifies the second electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 2nd Physical Value | Specifies the physical value that corresponds to the second electrical value. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-rtd.html language=enus -->
## TOPIC 00039: RTD Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-rtd.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-rtd.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure temperature from a Resistance Temperature Detector (RTD). Platinum RTDs use a linearization curve known as the Callendar-Van Dusen equation to measure the temperature of RTDs. For more information on measuring temperature, refer to the NI-DAQ

### RTD Channel Properties (AI)

Configure analog input (AI) channel properties to measure temperature from a Resistance
 Temperature Detector (RTD).

Platinum RTDs use a linearization curve known as the Callendar-Van Dusen equation to measure
 the temperature of RTDs. For more information on measuring temperature, refer to the
 NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Resistance Configuration | Specifies the number of wires to use for resistive measurements: 2-Wire 3-Wire 4-Wire |
| Excitation Source | Specifies the source of excitation: External—Use an external excitation source instead of the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. None—Supply no excitation to the channel. For both internal and external current excitation sources, you must use the Excitation Value property. |
| RTD Type | Specifies the type of RTD connected to the channel: Custom—Use a custom RTD. You must use the three Custom RTD Const properties to supply the coefficients for the Callendar-Van Dusen equation. Pt3750 Pt3851 Pt3911 Pt3916 Pt3920 Pt3928 |
| r0 | The sensor resistance at 0 degrees Celsius. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Custom RTD A const | Specifies the A constant of the Callendar-Van Dusen equation. VeriStand requires this value when you use a custom RTD and specify Custom for the RTD Type property. |
| Custom RTD B const | Specifies the B constant of the Callendar-Van Dusen equation. VeriStand requires this value when you use a custom RTD and specify Custom for the RTD Type property. |
| Custom RTD C const | Specifies the C constant of the Callendar-Van Dusen equation. VeriStand requires this value when you use a custom RTD and specify Custom for the RTD Type property. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Callendar-Van Dusen Equation
- NI-DAQmx Common Applications
- 2-Wire Resistance
- 3-Wire Resistance
- 4-Wire Resistance

<!--NI_TOPIC bundle=veristand path=ai-strain.html language=enus -->
## TOPIC 00040: Strain Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-strain.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-strain.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure strain. For more information on measuring strain, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The maximum

### Strain Channel Properties (AI)

Configure analog input (AI) channel properties to measure strain.

For more information on measuring strain, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Strain Configuration | Specifies what type of bridge configuration to use for the strain gages. For more information, refer to Bridge Configurations in the NI-DAQmx Manual. Full Bridge I Full Bridge II Full Bridge III Half Bridge I Half Bridge II Quarter Bridge I Quarter Bridge II |
| Excitation Source | Specifies the source of excitation: External—Use an external excitation source instead of the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. None—Supply no excitation to the channel. For both internal and external excitation sources, you must use the Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Lead Resistance | Specifies the amount of resistance in the lead wires. Ideally, this value is the same for all leads. |
| Initial Bridge Voltage | Specifies the output voltage of the bridge in the unloaded condition. VeriStand subtracts this value from any measurements before applying scaling equations. Perform a voltage measurement on the bridge with no strain applied to determine this value. |
| Gage Factor | Specifies the sensitivity of the strain gages and relates the change in electrical resistance to the change in strain. Each gage in the bridge must have the same gage factor. Refer to the sensor documentation to determine this value. |
| Nominal Gage Resistance | Specifies the resistance of the gages in an unstrained position. Each gage in the bridge must have the same nominal gage resistance. The resistance across arms of the bridge that do not have strain gages must also be the same as the nominal gage resistance. Refer to the sensor documentation to determine this value. |
| Poisson Ratio | Specifies the ratio of lateral strain to axial strain in the material you are measuring. |
| Enable Offset Null | Specifies whether to perform a bridge offset nulling calibration. |
| Enable Shunt Calibration | Specifies whether to perform a shunt calibration. |
| Shunt Element Location | Specifies the location of the shunt resistor: R1—Between Vch- and Vex+ R2—Between Vch- and Vex- R3—Between Vch+ and Vex- R4—Between Vch+ and Vex+ |
| Shunt Resistance | Specifies the shunt resistance. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |
| In-Situ Calibration (supported devices only) | Specifies whether to perform an in-situ calibration and when to perform the calibration: Before deployment—Perform an in-situ calibration before the system definition is deployed. After undeployment—Perform an in-situ calibration after the system definition is no longer deployed. Both—Perform an in-situ calibration before the system definition is deployed and after the system definition is no longer deployed. None—Do not perform an in-situ calibration. |
| In-Situ Minimum Value (supported devices only) | The minimum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Maximum Value (supported devices only) | The maximum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Input Configuration (supported devices only) | Specifies the input terminal configuration to use when performing the in-situ calibration: Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications
- Bridge Configurations

<!--NI_TOPIC bundle=veristand path=ai-thermistor-iex.html language=enus -->
## TOPIC 00041: Thermistor Iex Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-thermistor-iex.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-thermistor-iex.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure current excitation temperature using a thermistor. NI-DAQmx scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation. For more information on measuring temperature, refer to the NI-DAQmx Manual. Prop

### Thermistor Iex Channel Properties
 (AI)

Configure analog input (AI) channel properties to measure current excitation temperature
 using a thermistor.

NI-DAQmx scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation. For more information
 on measuring temperature, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Resistance Configuration | Specifies the number of wires to use for resistive measurements: 2-Wire 3-Wire 4-Wire |
| Excitation Source | Specifies the source of excitation: External—Use an external excitation source instead of the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. None—Supply no excitation to the channel. For both internal and external current excitation sources, you must use the Current Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| A | Specifies the A constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |
| B | Specifies the B constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |
| C | Specifies the C constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Thermistors
- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-thermistor-vex.html language=enus -->
## TOPIC 00042: Thermistor Vex Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-thermistor-vex.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-thermistor-vex.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure voltage excitation temperature using a thermistor. NI-DAQmx scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation. For more information on measuring temperature, refer to the NI-DAQmx Manual. Prop

### Thermistor Vex Channel Properties
 (AI)

Configure analog input (AI) channel properties to measure voltage excitation temperature
 using a thermistor.

NI-DAQmx scales the resistance of a thermistor to a temperature using the Steinhart-Hart thermistor equation. For more information
 on measuring temperature, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Resistance Configuration | Specifies the number of wires to use for resistive measurements: 2-Wire 3-Wire 4-Wire |
| Excitation Source | Specifies the source of excitation: External—Use an external excitation source instead of the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. None—Supply no excitation to the channel. For both internal and external current excitation sources, you must use the Current Excitation Value property. |
| r1 | Specifies the value of the reference resistor. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| A | Specifies the A constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |
| B | Specifies the B constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |
| C | Specifies the C constant for the Steinhart-Hart thermistor equation. Refer to the sensor documentation to determine values for these constants. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Thermistors
- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-thermocouple.html language=enus -->
## TOPIC 00043: Thermocouple Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-thermocouple.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-thermocouple.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure temperature using a thermocouple. Thermocouples require cold-junction compensation (CJC) for temperature references. For more information on measuring temperature, refer to Signal Conditioning Requirements for Thermocouples in the NI-DAQmx Ma

### Thermocouple Channel Properties (AI)

Configure analog input (AI) channel properties to measure temperature using a
 thermocouple.

Thermocouples require cold-junction compensation (CJC) for temperature references. For more
 information on measuring temperature, refer to *Signal Conditioning
 Requirements for Thermocouples* in the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Thermocouple Type | Specifies the type of thermocouples connected to the channel. Thermocouple types differ in composition and measurement range. B—B-type thermocouple. E—E-type thermocouple. J—J-type thermocouple. K—K-type thermocouple. N—N-type thermocouple. R—R-type thermocouple. S—S-type thermocouple. T—T-type thermocouple. |
| CJC Value | Specifies the temperature of the cold-junction if you set the CJC Source property to Constant Value. |
| CJC Source | Specifies the source of cold-junction compensation: Constant Value—Use the CJC Value property to specify the cold-junction temperature. Internal—Use a cold-junction compensation channel built into the terminal block. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Signal Conditioning Requirements for Thermocouples
- Thermocouples

<!--NI_TOPIC bundle=veristand path=ai-torque.html language=enus -->
## TOPIC 00044: Torque Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-torque.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-torque.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure torque. For more information on measuring torque, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The maximum

### Torque Channel Properties (AI)

Configure analog input (AI) channel properties to measure torque.

For more information on measuring torque, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Bridge Configuration | Specifies what type of bridge configuration to use: Full Bridge Half Bridge Quarter Bridge |
| Excitation Source | Specifies the source of excitation: External—Use an excitation source other than the built-in excitation source of the device. Internal—Use the built-in excitation source of the device. For both internal and external excitation sources, you must use the Excitation Value property. |
| Excitation Value | Specifies the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine this value. |
| Nominal Bridge Resistance | Specifies the resistance of the bridge while not under load. |
| Electrical Units | Specifies from which electrical unit to scale the data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. |
| Scale: 1st Electrical Value | Specifies the first electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 1st Physical Value | Specifies the physical value that corresponds to the first electrical value. |
| Scale: 2nd Electrical Value | Specifies the second electrical value used to calculate the slope and y-intercept of a two-point linear equation to scale electrical values to physical values. |
| Scale: 2nd Physical Value | Specifies the physical value that corresponds to the second electrical value. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ai-voltage.html language=enus -->
## TOPIC 00045: Voltage Channel Properties (AI)

- bundle_id: `veristand`
- source_path: `ai-voltage.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ai-voltage.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog input (AI) channel properties to measure voltage. For more information on measuring voltage, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The maxim

### Voltage Channel Properties (AI)

Configure analog input (AI) channel properties to measure voltage.

For more information on measuring voltage, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Input Configuration | Specifies the input terminal configuration to apply to the device channels. Note If you select any configuration other than Same as device, it overrides the configuration you specify for the device on the DAQ Device Configuration page in System Explorer. Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |
| Filter Type (supported devices only) | Specifies whether to apply a digital filter to the input signal: Disabled—No filter. Lowpass—Eliminates all signal frequency components above the cutoff frequency. |
| Filter Cutoff Frequency (supported devices only) | Specifies the cutoff frequency of the digital filter. |
| In-Situ Calibration (supported devices only) | Specifies whether to perform an in-situ calibration and when to perform the calibration: Before deployment—Perform an in-situ calibration before the system definition is deployed. After undeployment—Perform an in-situ calibration after the system definition is no longer deployed. Both—Perform an in-situ calibration before the system definition is deployed and after the system definition is no longer deployed. None—Do not perform an in-situ calibration. |
| In-Situ Minimum Value (supported devices only) | The minimum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Maximum Value (supported devices only) | The maximum value you expect to measure when VeriStand performs an in-situ calibration. |
| In-Situ Input Configuration (supported devices only) | Specifies the input terminal configuration to use when performing the in-situ calibration: Same as device—The same configuration specified for the DAQ device itself. To set the input terminal configuration at the device level, use the Input Configuration pull-down menu on the DAQ Device Configuration page. Default—At run time, NI-DAQmx chooses the default terminal configuration for the channel. RSE—Referenced single-ended mode. NRSE—Non-referenced single-ended mode. Differential—Differential mode. Pseudodifferential—Pseudodifferential mode. |
| Lowpass Cutoff Filter Frequency (supported devices only) | Specifies the frequency that corresponds to the -3dB cutoff of the analog filter. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=alarm-group-execution.html language=enus -->
## TOPIC 00046: Alarm Group Execution

- bundle_id: `veristand`
- source_path: `alarm-group-execution.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/alarm-group-execution.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Alarm groups and priorities determine when procedures execute. Only one alarm procedure executes at a time in an alarm group. Use the following table to learn the execution order of procedures based on the order of the alarms.If an alarm is set to Indicate Only mode, the alarm trips when the monitor

### Alarm Group Execution

Alarm groups and priorities determine when procedures execute.

Only one alarm procedure executes at a time in an alarm group.

Note

Indicate Only

| Order of alarms | Order of procedures |
| --- | --- |
| Multiple alarms go out of range simultaneously. | The alarm with the highest priority executes its procedure first. |
| A low-priority alarm trips before a high-priority alarm. | The high-priority procedure interrupts the low-priority alarm. After the high-priority procedure finishes and resets, the low-priority procedure resumes. |
| A high-priority alarm trips before a low-priority alarm. | The high-priority procedure executes, finishes, and resets the high-priority alarm. If the low-priority alarm condition is still met after the high-priority alarm resets, the low-priority alarm trips. Note If the channel value for the low-priority alarm returns to a normal range before the high-priority alarm resets, the low-priority procedure does not execute. |

Parent topic:

Assigning an Alarm Group

<!--NI_TOPIC bundle=veristand path=alarm-trigger-specific-channel-value.html language=enus -->
## TOPIC 00047: Triggering an Alarm for a Specific Channel Value

- bundle_id: `veristand`
- source_path: `alarm-trigger-specific-channel-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/alarm-trigger-specific-channel-value.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create an alarm that trips when a channel reaches an exact value. Launch your project in the VeriStand Editor. Create and configure a conditional calculated channel to represent your alarm trigger. On the Mapping Diagram, create a mapping wire from the conditional calculated channel’s X terminal to

### Triggering an Alarm for a Specific Channel
 Value

Create an alarm that trips when a channel reaches an exact value.

1. Launch your project in the VeriStand Editor.
2. Create and
 configure a conditional calculated channel to represent your alarm
 trigger.
  1. On the Mapping Diagram, create a mapping wire from
 the conditional calculated channel’s X terminal
 to the channel you want to monitor.
  2. In the configuration pane, use the Condition
 drop-down menu to select =.
  3. Enable Use constant Y value and enter
 a Y value that will trip the alarm.
  4. Enable Use constant W value and set the
 W value as 1.
  5. Enable Use constant Z value and set
 the Z Value as 0.
3. Add an
 alarm.
  1. Map the Source to the calculated channel.
  2. In the Upper Limit drop-down menu,
 select Constant and enter the
 Value as 0.000.
  3. In the Lower Limit drop-down menu,
 select Constant and enter the
 Value as 0.000. 
 Note When the calculated channel detects the channel value you
 specified (y value), the value of the calculated channel changes to
 1 and the alarm trips.
4. Save the system definition file.

Parent topic:

Adding and Configuring Alarms

Related tasks:

- Adding a Calculated Channel
- Adding an Alarm

<!--NI_TOPIC bundle=veristand path=alias-model-parameter.html language=enus -->
## TOPIC 00048: Aliasing Parameter Names in a Model Parameter File

- bundle_id: `veristand`
- source_path: `alias-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/alias-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a parameter alias file to map syntactically correct aliases in a model parameter file to model parameter paths in VeriStand. In addition to creating cleaner parameter files, aliasing parameter names can extend the reusability of a test by allowing you to simply update the alias file if you want

### Aliasing Parameter Names in a Model Parameter
 File

Use a parameter alias file to map syntactically correct aliases in a model
 parameter file to model parameter paths in VeriStand.

In addition to creating cleaner parameter
 files, aliasing parameter names can extend the reusability of a test by
 allowing you to simply update the alias file if you want to use the same
 test on a model with different parameter names.

1. Open a formatted text file (.txt or
 .m).
2. Replace the parameter names with syntactically correct
 aliases. 
 Note Each alias must start with a letter and contain only
 alphanumeric characters or underscores.
3. Create a new text (.txt) file and enter
 the aliases and their corresponding model parameter paths in
 the same format you used for the model parameter file. 
 Note The
 alias file must have a .txt file
 extension and use the same delimiter as the
 parameter file with which it corresponds.
4. Save the text files.
5. Configure VeriStand to use the parameter alias file path based
 on where the original model parameter text file is
 called. 
 Location
How to enterStimulus Profile Editor
Open a stimulus profile.
On the Edit tab, select
 Update Model Parameters from
 File.
Enter the Alias File
 path.
Initializing parameters
Use System Explorer to apply initial values for model parameters from a
 .txt file.
On the Simulation Models
 page, enter the Parameter alias file
 path.
Model Parameter Manager tab
Use the VeriStand Editor
 to import model parameters.
In the Configure Parameter
 Import dialog box, enter the
 Alias File Path.
Model Parameter Manager Workspace
 tool
Use the Workspace to
 import model parameters.
In the Select Model Calibration
 File dialog box, enter theParameter alias file path.
6. Set the Delimiter property to the
 delimiter type that both the parameter file and the alias
 file use.

When the feature that calls the top-level text file
 executes, VeriStand uses the alias file to map the aliases in the parameter
 file to actual model parameters.

Note

| File type | Example |
| --- | --- |
| Parameter | a 25 b 900 |
| Alias | a {model/environment temperature (C)} b {model/idle speed (RPM)} |

Parent topic:

Setting Model Parameters

<!--NI_TOPIC bundle=veristand path=ao-current.html language=enus -->
## TOPIC 00049: Current Channel Properties (AO)

- bundle_id: `veristand`
- source_path: `ao-current.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ao-current.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog output (AO) channel properties to generate current. For more information on generating current, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The ma

### Current Channel Properties (AO)

Configure analog output (AO) channel properties to generate current.

For more information on generating current, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=ao-voltage.html language=enus -->
## TOPIC 00050: Voltage Channel Properties (AO)

- bundle_id: `veristand`
- source_path: `ao-voltage.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ao-voltage.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure analog output (AO) channel properties to generate voltage. For more information on generating voltage, refer to the NI-DAQmx Manual. Property/Section Description Minimum Value The minimum value you expect to measure before VeriStand performs any scaling or calibration. Maximum Value The ma

### Voltage Channel Properties (AO)

Configure analog output (AO) channel properties to generate voltage.

For more information on generating voltage, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=api-veristand.html language=enus -->
## TOPIC 00051: APIs in VeriStand

- bundle_id: `veristand`
- source_path: `api-veristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/api-veristand.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: VeriStand provides a variety of Application Program Interfaces (APIs) to programmatically create, deploy and interact with system definitions. These APIs are made available by C# assemblies installed to the Global Assembly Cache (GAC). You can access the GAC from any .NET-compatible programming lang

### APIs in VeriStand

VeriStand provides a variety of Application Program Interfaces (APIs) to programmatically
 create, deploy and interact with system definitions.

These APIs are made available by C# assemblies installed to the Global Assembly Cache
 (GAC). You can access the GAC from any .NET-compatible programming language or
 environment, such as LabVIEW, Python, and NI TestStand.

If you are using LabVIEW to program VeriStand, you can access these APIs within the NI VeriStand»Execution palette.

<!--NI_TOPIC bundle=veristand path=apply-scale-factors-xnet-signals.html language=enus -->
## TOPIC 00052: How VeriStand Applies Scaling Factors to NI-XNET Signals

- bundle_id: `veristand`
- source_path: `apply-scale-factors-xnet-signals.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/apply-scale-factors-xnet-signals.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In NI-XNET software, you can assign a scaling factor to a signal. When VeriStand reads values from a signal that has a scaling factor, VeriStand scales the raw, prescaled values according to the scaling factor. For example, if you assign a scaling factor of 0.1 to a signal and Veristand reads a valu

### How VeriStand Applies Scaling Factors to
 NI-XNET Signals

In NI-XNET software, you can assign a scaling factor to a signal.

When VeriStand reads values from a signal that has a scaling factor, VeriStand scales the
 raw, prescaled values according to the scaling factor. For example, if you assign a
 scaling factor of 0.1 to a signal and Veristand reads a value of 3 from the signal, it
 scales the value to 0.3.

Conversely, VeriStand converts values to prescaled values before writing to signals. For
 example, if you write a value of 0.3 to a signal that has a scaling factor of 0.1,
 VeriStand writes a value of 3 to the bus.

Parent topic:

Using NI-XNET Interfaces

<!--NI_TOPIC bundle=veristand path=array-variables-primitives.html language=enus -->
## TOPIC 00053: Array Variables Primitives

- bundle_id: `veristand`
- source_path: `array-variables-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/array-variables-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Array Variables primitives to create variables that are arrays of values of a certain data type. Palette object Description Boolean Array An array of Boolean values. Double Array An array of double-precision, floating point numbers. Imported Double Array An array of double-precision, floatin

### Array Variables Primitives

Use the Array Variables primitives to create variables that are arrays of values of a
 certain data type.

| Palette object | Description |
| --- | --- |
| Boolean Array | An array of Boolean values. |
| Double Array | An array of double-precision, floating point numbers. |
| Imported Double Array | An array of double-precision, floating point numbers imported from a file. |
| Int32 Array | An array of 32-bit signed integers. |
| Int64 Array | An array of 64-bit signed integers. |
| UInt32 Array | An array of 32-bit unsigned integers. |
| UInt64 Array | An array of 64-bit unsigned integers. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=asam-xil-accessing-framework.html language=enus -->
## TOPIC 00054: ASAM XIL Framework C# Access

- bundle_id: `veristand`
- source_path: `asam-xil-accessing-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asam-xil-accessing-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To access the VeriStand ASAM XIL framework in your C# application, you must create a vendor-specific framework. Use the following values to create a framework for VeriStand.To run this code, you must reference the ASAM.XIL.Implementation.FrameworkFactory assembly in order to have access to the Frame

### ASAM XIL Framework C# Access

To access the VeriStand ASAM XIL framework in your C# application, you must create a
 vendor-specific framework.

Note

```text
IFrameworkFactory frameworkFactory = new FrameworkFactory();
IFramework framework = frameworkFactory.CreateVendorSpecificFramework(
vendorName:"National Instruments",
productVersion: "2020"); 
```

Parent topic:

ASAM XIL API - Generic Simulator Interface

<!--NI_TOPIC bundle=veristand path=asam-xil-accessing-testbench.html language=enus -->
## TOPIC 00055: Accessing the VeriStand ASAM XIL Testbench

- bundle_id: `veristand`
- source_path: `asam-xil-accessing-testbench.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asam-xil-accessing-testbench.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To access the VeriStand ASAM XIL testbench in your C# application, you must create a vendor-specific testbench. Use the following values as an example on how to create a testbench for VeriStand: ITestbenchFactory testbenchFactory = new TestbenchFactory(); ITestbench testbench = testbenchFactory.Crea

### Accessing the VeriStand ASAM XIL
 Testbench

To access the VeriStand ASAM XIL testbench in your C# application, you must create a
 vendor-specific testbench.

Use the following values as an example on how to create a testbench for VeriStand:

```text
ITestbenchFactory testbenchFactory = new TestbenchFactory(); 
ITestbench testbench = testbenchFactory.CreateVendorSpecificTestbench(
vendorName:"National Instruments",
productName:"NI VeriStand ASAM XIL Interface",
productVersion:"2020"); 
```

Parent topic:

ASAM XIL API - Generic Simulator Interface

<!--NI_TOPIC bundle=veristand path=asam-xil-implementation-differences.html language=enus -->
## TOPIC 00056: Implementation Differences and Limitations with the ASAM XIL Interface

- bundle_id: `veristand`
- source_path: `asam-xil-implementation-differences.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asam-xil-implementation-differences.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand's ASAM XIL implementation deviates from the ASAM XIL standard in areas such as signal generation and capturing. Implementation DifferencesThe following table displays implementation differences. Process Implementation differences Signal Generation ConditionWatcher definitions cannot be sav

### Implementation Differences and Limitations
 with the ASAM XIL Interface

VeriStand's ASAM XIL implementation deviates from the ASAM XIL standard in areas such as
 signal generation and capturing.

#### Implementation Differences

The following
 table displays implementation differences.

| Process | Implementation differences |
| --- | --- |
| Signal Generation | ConditionWatcher definitions cannot be saved in the STI format when a SignalDescriptionSet contains ConditionWatchers as StopTriggers. Signal generation operations cannot write to model parameters. Signal generation processes create temporary real-time sequence files in the temporary directory. |
| Capturing | When Capture.DurationUnit is set to eSAMPLES, VeriStand ASAM XIL assumes the data capture rate was set during capture creation. Capture.Stop() may take longer than expected to complete execution. The function only returns a value after flushing log data into files and finishing post-processing. Capture.Fetch() might not return the latest samples because of buffering. VeriStand logs data to TDMS despite what capture result writer you choose. The data is later processed by either an MDF or in-memory capture result writer. |
| Miscellaneous | Condition Watchers conditions support the syntax, operators, and expression functions that VeriStand real-time sequences support. Signal generation and capturing are not supported when the gateway is running on a machine other than localhost. |

#### Limitations

The following table displays
 known limitations.

| Process | Limitation |
| --- | --- |
| Capturing | Capture sessions ignore data logging errors. ASAM XIL API users will not receive an error notification. Instead, the capture will immediately enter the eFINISHED state and cease logging data. Untriggered captures also cause this state change. Capture results and .mdf files contain logging data until when the error occurred. |

Parent topic:

ASAM XIL API - Generic Simulator Interface

<!--NI_TOPIC bundle=veristand path=asam-xil-interface.html language=enus -->
## TOPIC 00057: ASAM XIL API - Generic Simulator Interface

- bundle_id: `veristand`
- source_path: `asam-xil-interface.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asam-xil-interface.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: VeriStand includes a Generic Simulator Interface for the Framework, MAPort and EESPort based on the 2.1 version of the ASAM XIL Standard The Association for Standardization of Automation and Measuring Systems (ASAM) is an organization that facilitates interoperability between measurement and automat

### ASAM XIL API - Generic Simulator
 Interface

VeriStand includes a Generic Simulator Interface for the Framework, MAPort and EESPort
 based on the 2.1 version of the ASAM XIL Standard

The Association for Standardization of Automation and Measuring Systems (ASAM) is an
 organization that facilitates interoperability between measurement and automation
 testing tools from different vendors.

MAPort

EES port

Framework

Note

Locate example VeriStand ASAM XIL testbench and framework files in <Common
 Data>\Examples\DotNet4.6.2\ASAM XIL.

Parent topic:

Running Tests

<!--NI_TOPIC bundle=veristand path=asam-xil-port-configuration-tag.html language=enus -->
## TOPIC 00058: ASAM XIL Port Configuration Tag Reference

- bundle_id: `veristand`
- source_path: `asam-xil-port-configuration-tag.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asam-xil-port-configuration-tag.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use specific XML elements and complex elements in the port configuration XML file to configure one or more VeriStand ASAM XIL testbench ports. The following table displays the XML elements you can use in a VeriStand ASAM XIL port configuration XML file. Tool Required? Element Type Min/Max Occurrence

### ASAM XIL Port Configuration Tag
 Reference

Use specific XML elements and complex elements in the port configuration XML file to
 configure one or more VeriStand ASAM XIL testbench ports.

The following table displays the XML elements you can use in a VeriStand ASAM XIL port
 configuration XML file.

| Tool | Required? | Element Type | Min/Max Occurrences | Description |
| --- | --- | --- | --- | --- |
| <NIVSPortConfig> | Yes | Top-level | 1/1 | The type of configuration file. |
| <Version> | Yes | VersionType | 1/1 | The version of the port configuration file. |
| <Project> | Yes | NonEmptyStringType | 1/1 | The path to the VeriStand project you want to connect to through the ASAM XIL Interface. |
| <ShowWorkspace> | No | xs:boolean | 0/1 | Specifies whether to display the workspace when a project is deployed. |
| <ShowVeriStandScreen> | No | xs:boolean | 0/1 | Specifies whether to display the VeriStand screen when a project is deployed. |
| <UndeployVeriStandProjectOnDisconnect> | No | xs:boolean | 0/1 | Specifies whether to undeploy the running VeriStand project when the port is disconnected. |
| <EESPortConfig> | No | EESPortConfigType | 0/1 | A container for the EESPort configuration options. |
| <HWTriggerChannelList> | No | HWTriggerChannelListType | 0/1 | The list of channels you want to use to fire EESPort hardware triggers. |
| <HWTriggerChannel> | No | HWTriggerChannelType | 0/unbounded | The path to the channel you want use as a hardware trigger. You can only set one hardware trigger channel per target.Note The hardware trigger only occurs if the channel value changes from 0 to any other value. |
| <SWTriggerChannelList> | No | SWTriggerChannelListType | 0/1 | A list of channels you want to use to fire EESPort software triggers. |
| <SWTriggerChannel> | No | SWTriggerChannelType | 0/unbounded | A path to the software channel you want to trigger. You can only set one software trigger channel per target.Note The software trigger only occurs if the channel value changes from 0 to any other value. Set the AutoReset attribute of this element to true to automatically set the channel back to zero after the trigger fires. If AutoReset is set to false, you must manually set the channel value back to zero. |
| <MAPortConfig> | No | MAPortConfigType | 0/1 | The container for the MAPort configuration options. |
| <LogFilePath> | No | NonEmptyStringType | 0/1 | Specifies the path of the temporary TDMS log file that is created during capturing. |
| <TaskList> | No | TaskListType | 0/1 | A list of user-defined tasks. |
| <Task> | No | TaskType | 0/unbounded | Specifies the task name and frequency. Use the format <TaskN>, where N is the frequency of the task in Hz. |
| <LogPostProcessPeriodMS> | No | xs:int | 0/1 | The length, in milliseconds, of the post-processing period.Note If you call Fetch () before post-processing completes, Fetch ()returns an empty result. If post-processing occurs periodically, a new TDMS file is created for each period, which adds overhead to the operation |
| <ChannelDataTypeOverrideList> | No | ChannelDataTypeOverrideListType | 0/1 | A list of channels that you want to override the default data type. In VeriStand, channels are double-precision, floating-point numerics by default. |
| <ChannelDataTypeOverride> | No | ChannelDataTypeOverrideType | 0/unbounded | A container for the channel name and data type. Channel names inside this container must be unique. |
| <ChannelName> | Yes* | NonEmptyStringType | 0/1 | The name of the channel for which you want to change the data type. |
| <DataType> | Yes* | DataTypeType | 0/1 | The data type you want the channel value to change to. |
| *Required child elements of optional parent elements are only required if you use the parent element. |  |  |  |  |

#### Types

- VersionType —Specifies version information. Attribute
 Required?
 Attribute TypeMajor
 Yes
 xs:unsignedInt
 Minor
 Yes
 xs:unsignedInt
 Fix
 Yes
 xs:unsignedInt
 Build
 Yes
 xs:unsignedInt
- NonEmptyString —Restricts the element to allow only
 non-empty strings. Restrictions
 Minimum Lengthxs:string
 1
- DataTypeType —Restricts the element to only allow int, uint,
 bool and float data types. Only scalars, vectors, and matrices are allowed
 from the data types.

Parent topic:

ASAM XIL API - Generic Simulator Interface

<!--NI_TOPIC bundle=veristand path=asan-xil-configuring-framework.html language=enus -->
## TOPIC 00059: Configuring the ASAM XIL Framework

- bundle_id: `veristand`
- source_path: `asan-xil-configuring-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/asan-xil-configuring-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: The ASAM XIL framework is the central class you use to manage and configure testbench ports, record data, and stimulate variables. You can use the ASAM XIL framework to complete tasks such as logging variables and stimulating values for variables. You can also create units, data types, and framework

### Configuring the ASAM XIL Framework

The ASAM XIL framework is the central class you use to manage and configure testbench
 ports, record data, and stimulate variables.

To configure the ASAM XIL framework, create the following XML
 configuration files:

- Port configuration XML file—Configures one or more VeriStand ASAM XIL testbench
 ports.
- Framework configuration XML file—Defines your ports, port configuration files,
 and mapping files.
- Framework mapping XML file—Defines the labels for the testbench and framework
 variables and then map them together.

\Examples\DotNet4.6.2\ASAM XIL

Parent topic:

ASAM XIL API - Generic Simulator Interface

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=assignment.html language=enus -->
## TOPIC 00060: Assignment Primitive

- bundle_id: `veristand`
- source_path: `assignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/assignment.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A simple expression statement that assigns a value to a variable. For example, VarName = 150 is an assignment that sets the value of a variable, VarName, to 150. Property/Section Description Expression Specifies the expression to evaluate. You can include real-time sequence variables, supported func

### Assignment Primitive

A simple expression statement that assigns a value to a variable.

For example, VarName = 150 is an assignment that sets the value of a
 variable, VarName, to 150.

| Property/Section | Description |
| --- | --- |
| Expression | Specifies the expression to evaluate. You can include real-time sequence variables, supported functions, and operators in an expression. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Expressions Primitives

<!--NI_TOPIC bundle=veristand path=atml-standard.html language=enus -->
## TOPIC 00061: Automatic Test Markup Language (ATML) Standard

- bundle_id: `veristand`
- source_path: `atml-standard.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/atml-standard.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: ATML is a military and aerospace industry standard for sharing data between different components of a test system and supports test program, test asset, and unit under test (UUT) interoperability within an automatic test environment. ATML accomplishes this through a standard XML schema for exchangin

### Automatic Test Markup Language (ATML)
 Standard

ATML is a military and aerospace industry standard for sharing data between different
 components of a test system and supports test program, test asset, and unit under test (UUT)
 interoperability within an automatic test environment.

ATML accomplishes
 this through a standard XML schema for exchanging UUT test and diagnostic information
 between components of the test system. ATML specifies standards for test environments
 that encompass the total product life cycle. ATML defines an integrated set of
 test-related information that supports the information needs of test environments for
 testing applications.

- Diagnostics
- Instrument Description
- Test Adapter
- Test Configuration
- Test Description
- Test Results and Session Information
- Test Station
- UUT Description

#### Purpose

- Facilitate the communication, sharing, and reuse of product design and test
 information for the purpose of testing the product.
- Facilitate test program set (TPS) portability and interoperability.
- Facilitate instrument interchangeability.
- Facilitate the development, integration, and use of test software and test
 software development tools.
- Support the application of integrated diagnostics.
- Support modular software architectures based upon a framework that supports
 reusable software products.

#### Test Results and Session Information

The
 ATML Test Results and Session Information schema provides the definition for the
 data collected when you execute a test or tests of a UUT using test procedures in an
 automated test environment, including the measured values, pass/fail results, and
 accompanying data, such as test operator, station information, environmental
 conditions, and so on. ATML Test Results is a component standard of IEEE 1636
 Software Interface for Maintenance Information Collection Analysis
 (SIMICA).

VeriStand generates XML reports that conform to the approved version
 6.0.1 of the Test Results and Session Information schema the ATML standard defines.
 The <Application Data>\Data Storage\ATML directory contains a
 copy of version 6.0.1 of the schema.

Parent topic:

Viewing Stimulus Profile Test Results

<!--NI_TOPIC bundle=veristand path=automating-diadem-vbscript.html language=enus -->
## TOPIC 00062: Automating Post-Processing in DIAdem with a VBScript

- bundle_id: `veristand`
- source_path: `automating-diadem-vbscript.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/automating-diadem-vbscript.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Automate the post-processing actions in DIAdem to analyze and process data by running a VBScript (.VBS). Click Edit settings on the data logging control. Select Post-Processing. Select Run script. In Script path, specify the path to the VBScript file you want to run.

### Automating Post-Processing in DIAdem with a
 VBScript

Automate the post-processing actions in DIAdem to analyze and process data by running a
 VBScript (.VBS).

1. Click Edit settings on the data logging control.
2. Select Post-Processing.
3. Select Run script.
4. In Script path, specify the path to the VBScript file
 you want to run.

Parent topic:

Loading a File in DIAdem

<!--NI_TOPIC bundle=veristand path=block.html language=enus -->
## TOPIC 00063: Block

- bundle_id: `veristand`
- source_path: `block.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/block.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organize your real-time sequence code. A block is a list of functional statements to execute. Because a block is itself a single statement, you also can use blocks to easily duplicate or move related statements. The predefined sections of a real-time sequence, Setup, Main, and Clean Up, are examples

### Block

Organize your real-time sequence code.

A *block* is a list of functional statements to execute. Because a block
 is itself a single statement, you also can use blocks to easily duplicate or move
 related statements. The predefined sections of a real-time sequence, Setup, Main,
 and Clean Up, are examples of code blocks. Blocks have no effect on the execution of
 the code.

| Property/Section | Description |
| --- | --- |
| Name | The name of the block. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Miscellaneous Primitives

<!--NI_TOPIC bundle=veristand path=boolean-array-variable.html language=enus -->
## TOPIC 00064: Boolean Array Variable

- bundle_id: `veristand`
- source_path: `boolean-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/boolean-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of Boolean values. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, wher

### Boolean Array Variable

An array of Boolean values.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=boolean.html language=enus -->
## TOPIC 00065: Boolean Variable

- bundle_id: `veristand`
- source_path: `boolean.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/boolean.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Boolean value. If you want to configure pass/fail notification for a real-time sequence, use a Boolean as the return variable. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to

### Boolean Variable

A Boolean value.

If you want to configure pass/fail notification for a real-time sequence, use a
 Boolean as the return variable.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=c-examples.html language=enus -->
## TOPIC 00066: C# Examples

- bundle_id: `veristand`
- source_path: `c-examples.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/c-examples.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example C# code helps you get started with NI software features and common programming workflows.

### C# Examples

Example C# code helps you get started with NI software features and common
 programming workflows.

- [Opening and Running a Project](c-opening-and-running-a-project.html) Use the NI VeriStand Execution API in C# to deploy a system definition to a target and read channel values.
- [Programming with the System Definition API in C#](programming-with-the-system-definition-api-c.html) Use C# with the NI VeriStand System Definition .NET API to programmatically create, open, and change system definition files.

Parent topic:

VeriStand Examples

<!--NI_TOPIC bundle=veristand path=c-modifying-a-daq-device-in-a-sys.html language=enus -->
## TOPIC 00067: Modifying a DAQ Device in a System Definition File

- bundle_id: `veristand`
- source_path: `c-modifying-a-daq-device-in-a-sys.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/c-modifying-a-daq-device-in-a-sys.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand System Definition .NET API in C# to configure DAQ devices in a system definition file. This example uses the System Definition API to programmatically configure a DAQ device in a system definition. public static void Main(string[] args) { // Locate the system definition file, Ex

### Modifying a DAQ Device in a System Definition
 File

Use the NI VeriStand System Definition .NET API in C# to configure DAQ devices in
 a system definition file. This example uses the System Definition API to programmatically
 configure a DAQ device in a system definition.

```text
public static void Main(string[] args)
{

// Locate the system definition file, ExampleSDF_ModifyDAQ.nivssdf, relative to the current directory.
string exampleSDFPath = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName + "\ExampleSDF_ModifyDAQ.nivssdf";


// Open an existing system definition file from disk.
SystemDefinition exampleSDF = newSystemDefinition(exampleSDFPath);


// Find the first target in the system definition file by traversing the following nodes in the system definition file, in descending order: root-level item, Targets section, all targets.
Target firstTarget = exampleSDF.Root.GetTargets().GetTargetList()[0];


// Find the first DAQ device in the DAQ section by traversing the following nodes in the system definition file, in descending order: first Target, Hardware section, first Chassis, DAQ section.
DAQDevice firstDAQDevice = firstTarget.GetHardware().GetChassisList()[0].GetDAQ().GetDeviceList()[0];

// Add new analog inputs DAQAnalogInputs daqAnalogInputsSection; // Instantiate class for Analog Inputs section.
DAQAnalogInput newAnalogInputChannel; // Instantiate class for analog input channel.
firstDAQDevice.GetAnalogInputSection().RemoveNode(); // Remove any existing analog inputs by removing the existing Analog Input section.
firstDAQDevice.CreateAnalogInputs(out daqAnalogInputsSection); // Create a new Analog Inputs section under the first DAQ device.
newAnalogInputChannel = newDAQAnalogInput("AI0", 0, DAQMeasurementType.AnalogInputVoltage, 0); // Create a new analog input named AI0.
daqAnalogInputsSection.AddAnalogInput(newAnalogInputChannel); // Add the new analog input channel to the Analog Input section.


// Add new analog outputs.
DAQAnalogOutputs daqAnalogOutputsSection; // Instantiate class for Analog Outputs section.
DAQAnalogOutput newAnalogOutputChannel; // Instantiate class for analog output channel.
firstDAQDevice.GetAnalogOutputSection().RemoveNode(); // Remove any existing analog outputs by removing the existing Analog Outputs section.
firstDAQDevice.CreateAnalogOutputs(out daqAnalogOutputsSection); // Create a new Analog Outputs section under the first DAQ device.
newAnalogOutputChannel = newDAQAnalogOutput("AO0", 0, DAQMeasurementType.AnalogOutputVoltage, 0); // Create new analog output channel named AO0.
daqAnalogOutputsSection.AddAnalogOutput(newAnalogOutputChannel); // Add the new analag output channel to the Analog Output section.


// Add new digital inputs
DAQDigitalInputs daqDigitalInputSection; // Instantiate class for Digital Input section.
DAQDigitalInput newDigitalInputChannel; // Instantiate class for digital input channel.
DAQDIOPort newDigitalInputPort; // Instantiate class for DAQ DIO port.
firstDAQDevice.GetDigitalInputSection().RemoveNode(); // Remove any existing digital inputs by removing the existing Digital Input section.
firstDAQDevice.CreateDigitalInputs(out daqDigitalInputSection); // Create a new Digital Input section under the first DAQ device.
newDigitalInputChannel = newDAQDigitalInput("DI0", 0, 0, true, DAQMeasurementType.DigitalInput); // Create a new digital input channel named DI0.
newDigitalInputPort = newDAQDIOPort(0, true); // Create a new DAQ DIO port.
newDigitalInputPort.AddDigitalInput(newDigitalInputChannel); // Add the new digital input channel to the DAQ DIO port.
daqDigitalInputSection.AddDIOPort(newDigitalInputPort); // Add the DAQ DIO port to the new Digital Input section.


// Add new digital outputs.
DAQDigitalOutputs daqDigitalOutputSection; // Instantiate class for Digital Ouput section.
DAQDigitalOutput newDigitalOutputChannel; // Instantiate class for digital output channel.
DAQDIOPort newDigitalOutputPort; // Instantiate class for DAQ DIO Port.
firstDAQDevice.GetDigitalOutputSection().RemoveNode(); // Remove any existing digital outputs by removing the existing Digital Outputs section.
firstDAQDevice.CreateDigitalOutputs(out daqDigitalOutputSection); // Create a new Digital Outputs section under the first DAQ device.
newDigitalOutputChannel = newDAQDigitalOutput("DO0", 0, 0, true, DAQMeasurementType.DigitalOutput); // Create a new digital output channel named DO0.
newDigitalOutputPort = newDAQDIOPort(0, false); // Create a new DAQ DIO port.
newDigitalOutputPort.AddDigitalOutput(newDigitalOutputChannel); // Add the digital output channel to the new DAQ DIO Port.
daqDigitalOutputSection.AddDIOPort(newDigitalOutputPort); // Add the DAQ DIO port to the new Digital Output section

// Create aliases for the new DAQ channels
exampleSDF.Root.GetAliases().AddNewAliasByReference("Analog_Input0", string.Empty, newAnalogInputChannel);
exampleSDF.Root.GetAliases().AddNewAliasByReference("Analog_Output0", string.Empty, newAnalogOutputChannel);
exampleSDF.Root.GetAliases().AddNewAliasByReference("Digital_Input0", string.Empty, newDigitalInputChannel);
exampleSDF.Root.GetAliases().AddNewAliasByReference("Digital_Output0", string.Empty, newDigitalOutputChannel);


// Create channel mappings such that AI0 maps to AO0 and DI0 maps to DO0. Note that the method AddChannelMappings requires arrays as parameters. This allows you to simultaneously create multiple channel mappings.
string[] daqChannelPathSources = new string[] { newAnalogInputChannel.NodePath, newDigitalInputChannel.NodePath };
string[] daqChannelPathDestinations = new string[] { newAnalogOutputChannel.NodePath, newDigitalOutputChannel.NodePath };
exampleSDF.Root.AddChannelMappings(daqChannelPathSources, daqChannelPathDestinations);


// Remove any aliases that have null references.
for (int i = 0; i <= exampleSDF.Root.GetAliases().GetAliasesList().Length - 1; i++)
{

if (exampleSDF.Root.GetAliases().GetAliasesList()[i].LinkedChannel == null)
{

    exampleSDF.Root.GetAliases().GetAliasesList()[i].RemoveNode();

}

}


// Remove any channel mappings that do not have a source.
string[] sdfChannelPathSources; // Declare arrays for the sources and destinations of all channel mappings in the system definition.
string[] sdfChannelPathDestinations;


exampleSDF.Root.GetChannelMappings(out sdfChannelPathSources, out sdfChannelPathDestinations); // Get all of the channel mappings.
List<string> channelMappingsToRemove = newList<string>(); // Initialize an empty List to store the channel mappings to remove.


// For any mappings that have an empty source, store the corresponding Destination Path.
for (int i = 0; i <= sdfChannelPathSources.Length - 1; i++)
{

if (sdfChannelPathSources[i] == string.Empty)
{

     channelMappingsToRemove.Add(sdfChannelPathDestinations[i]);

}

}


string[] channelMappingsToRemoveArray = channelMappingsToRemove.ToArray(); // Convert the List of mappings to delete to an array.
exampleSDF.Root.DeleteChannelMappings(channelMappingsToRemoveArray); // Delete the broken mappings using the DeleteChanelMappings method.


// Save the system definition file again and handle any errors.
string error;
bool saveError = exampleSDF.SaveSystemDefinitionFile(exampleSDFPath, out error);


if (saveError == true)
{

Console.WriteLine("\n\nSystem Definition File saved successfully");

}

else
{

Console.WriteLine("\n\nThere was an error saving the System Definition" + error);

}

}
```

Parent topic:

Programming with the System Definition API in C#

<!--NI_TOPIC bundle=veristand path=c-modifying-a-system-definition-f.html language=enus -->
## TOPIC 00068: Modifying a System Definition File

- bundle_id: `veristand`
- source_path: `c-modifying-a-system-definition-f.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/c-modifying-a-system-definition-f.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand System Definition .NET API in C# to edit a system definition file from disk. The example updates XNET CAN ports, databases, clusters, and incoming frames through System Explorer node classes. You can use any .NET-compatible programming language to access the NI VeriStand System

### Modifying a System Definition File

Use the NI VeriStand System Definition .NET API in C# to edit a system definition
 file from disk. The example updates XNET CAN ports, databases, clusters, and incoming frames
 through System Explorer node classes.

You can use any .NET-compatible programming language to access the NI VeriStand System Definition .NET API and programmatically control operation of the System Explorer window.

- Remove a CAN port from a system definition file
- Add a new CAN port with an associated XNET database, CAN cluster, and incoming
 frame

System Explorer

Figure 27.

[IMAGE alt='System Explorer tree showing an NI-XNET CAN1 port with incoming single-point frame.' src='GUID-946D779A-0B2B-41F0-869A-729C7CF6F13B-a5.gif']

```text
// Open an existing System Definition from disk
SystemDefinition xnetSysDef = new SystemDefinition("C:\Users\Public\Public Documents\National Instruments\NI VeriStand 2012\Projects\XNETAPIExample\XNETAPIExample.nivssdf");


// Find the first target in the system definition file by traversing the following nodes in the system definition file, in descending order: root-level item, Targets section, all targets
Target firstTarget = xnetSysDef.Root.GetTargets().GetTargetList()[0];


// Get a reference to the target's CAN section
canSection = firstTarget.GetHardware().GetChassisList()[0].GetXNET().GetCAN();


// Remove the first existing CAN port from the CAN section
canSection.GetCANPortList()[0].RemoveNode();


// Open an existing XNET database from disk
Database xnetTestDB = new Database("XNETTestDB");


// Create a CAN port associated with a cluster in the database you opened
CANPort car1CANPort = new CANPort("CAN1", 1, xnetTestDB, "Car1", 125000);


// Get the Single-Point Frame section that appears under the new CANPort
SinglePoint singlePointSection = car1CANPort.GetIncoming().GetSinglePoint();


// Add a frame to the database
singlePointSection.AddSignalBasedFrame(new SignalBasedFrame("Frame1",0,xnetTestDB,"Car1",8,-1,false,new string[]{"Signal11","Signal12","Signal13"}));


// Add the new CANPort to the target's CAN section
canSection.AddCANPort(car1CANPort);

// Save the changes to the system definition file
xnetSysDef.SaveSystemDefinitionFile;
```

Parent topic:

Programming with the System Definition API in C#

<!--NI_TOPIC bundle=veristand path=c-modifying-models-in-a-system-de.html language=enus -->
## TOPIC 00069: Modifying Models in a System Definition File

- bundle_id: `veristand`
- source_path: `c-modifying-models-in-a-system-de.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/c-modifying-models-in-a-system-de.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand System Definition .NET API in C# to add, configure, and remove models in a system definition file.The example C# code in this topic uses the System Definition API to perform the following actions. Add a model Configure the inports and outports of the model Remove a model As you

### Modifying Models in a System Definition
 File

Use the NI VeriStand System Definition .NET API in C# to add, configure, and remove
 models in a system definition file.

- Add a model
- Configure the inports and outports of the model
- Remove a model

System Explorer

Figure 28.

[IMAGE alt='System Explorer tree showing Targets » Controller » Simulation Models » Models with model nodes and ports.' src='GUID-17392366-11B6-47A1-A571-04167E66C9F0-a5.gif']

```text
public static void Main(string[] args)
{


// Locate the system definition file created for this example, ExampleSDF_ModifyModels.nivssdf.
string exampleSDFPath = "C:\Users\Public\Documents\National Instruments\NI VeriStand 2014\Examples\System Definition API\DotNET\Modify Models\ExampleSDF_ModifyModels.nivssdf";


// Open an existing system definition file from disk.
SystemDefinition exampleSDF = newSystemDefinition(exampleSDFPath);


// Instantiate class for the Models section of the system definition file.
Models modelsSection;


// Find the first target in the system definition file by traversing the following nodes in the system definition file, in descending order: root-level item, Targets section, all targets.
Target firstTarget = exampleSDF.Root.GetTargets().GetTargetList()[0];


// Get a reference to the first target's Models section.
modelsSection = firstTarget.GetSimulationModels().GetModels();


// Get the path for each of the example models that ship with NI VeriStand (Delay.dll, Random.dll, and Sinewave.dll).
string[] modeldllPaths = System.IO.Directory.GetFiles("C:\Users\Public\Documents\National Instruments\NI VeriStand 2014\Projects\Example\Models", "*.dll");


// Create an array of the model names. Additionally, create an array of aliases. You will link the aliases to channels later in the code.
string[] modeldllNames = new string[modeldllPaths.Length];
string[] modeldllAliases = new string[modeldllPaths.Length];


for (int i = 0; i <= modeldllPaths.Length - 1; i++)
{

int dllpathIndex = modeldllPaths[i].IndexOf("Models") + 7; // Add 7 to remove "Models/"
int dllpathLength = modeldllPaths[i].Length;
modeldllNames[i] = modeldllPaths[i].Substring(dllpathIndex, dllpathLength - dllpathIndex - 4); // Subtract 4 to remove ".dll"
modeldllAliases[i] = modeldllNames[i] + "_OutputAlias";
Console.Write("Adding new Model: " + modeldllNames[i]);

}


// Add each model to the system definition file using the Model constructor and AddModel method.
for (int i = 0; i <= modeldllPaths.Length - 1; i++)
{

modelsSection.AddModel(newModel(modeldllNames[i], string.Empty, modeldllPaths[i], 0, 1, 0, false, true, true));

}


// Link the first outport of each model to the corresponding alias in the array ModeldllAliases[] created previously.
for (int i = 0; i <= modeldllAliases.Length - 1; i++)
{

exampleSDF.Root.GetAliases().AddNewAliasByReference(modeldllAliases[i], string.Empty, modelsSection.GetModels()[i].GetOutportsSection().GetOutports()[0]);

}


//Remove the Delay model by name.
for (int i = 0; i <= modeldllNames.Length - 1; i++)
{

if (modelsSection.GetChildren()[i].Name == "Delay")
{

    modelsSection.RemoveNode();

}

}


// After removing the Delay model, check if any aliases contain empty links. If a broken alias is found, remove the alias.
for (int i = 0; i <= modeldllAliases.Length - 1; i++)
{

if (exampleSDF.Root.GetAliases().GetAliasesList()[i].LinkedChannel.Name == string.Empty)
{

     exampleSDF.Root.GetAliases().GetAliasesList()[i].RemoveNode();

}

}


>// Save the system definition file and handle any errors.
string error;
bool saveError = exampleSDF.SaveSystemDefinitionFile(exampleSDFPath, out error);

if (saveError == true)
{

Console.WriteLine("\n\nSystem Definition File saved successfully");

}
else
{

Console.WriteLine("\n\nThere was an error saving the System Definition" + error);

}

}
```

Parent topic:

Programming with the System Definition API in C#

<!--NI_TOPIC bundle=veristand path=c-opening-and-running-a-project.html language=enus -->
## TOPIC 00070: Opening and Running a Project

- bundle_id: `veristand`
- source_path: `c-opening-and-running-a-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/c-opening-and-running-a-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand Execution API in C# to deploy a system definition to a target and read channel values. The NI VeriStand Execution API is designed to automate the operation of an NI VeriStand application. For example, you can automate the following actions. Read and write channel data Control ru

### Opening and Running a Project

Use the NI VeriStand Execution API in C# to deploy a system definition to a
 target and read channel values.

- Read and write channel data
- Control running models
- Configure alarm states and read data from alarms
- Log real-time channel data to a TDMS file or text file on the
 host computer
- Access Workspace tools

- Deploy a system definition file to a target running the
 VeriStand Gateway.
- Read values from channels.
- Undeploy the system definition file.

```text
static void Main(string[] args)
{

// Create an array of channel names, as defined in the system definition file, whose values you want to read after deployment
String[] names = { "Aliases/Delay_Random Output", "Aliases/Delay_Sinewave Output", "Aliases/SineWave" };

// An array whose elements are the values of each channel
DataArray[] values;

// The value of a single channel
Double val;

// The maximum amount of time, in milliseconds, to wait for the connection process to complete before returning an error.
uint timeout = 60000;

// The path to the system definition file and the IP address of the target to which you want to deploy the system definition file
// Replace <version> with the installed VeriStand version year
String sineWavePath = "C:\Users\Public\Documents\National Instruments\NI VeriStand <version>\Examples\Sinewave Delay\Sinewave Delay.nivssdf";
String gatewayIP = "localhost";

// Initializes a new instance of the Factory class, which provides access to the NI VeriStand system and the various interfaces available in the Execution API. Any code you write using this API must include a Factory constructor to access NI VeriStand.
Factory FacRef = new Factory();

// Gets the IWorkspace2 interface, which you can use to manage connections between the VeriStand Gateway and one or more targets, to start and stop data logging operations, and to configure events for error and status notifications.
IWorkspace2 Workspace = FacRef.GetIWorkspace2(gatewayIP);

// Connects the VeriStand Gateway to one or more targets and deploys the system definition file.
ErrChk(Workspace.ConnectToSystem(sineWavePath, true, timeout));

Console.WriteLine("Deployed system.");

// Gets the values of multiple scalar channels running on the target.
for (int i = 0; i < 50; i++)
{

ErrChk(Workspace.GetChannelValues(names, out values));

Console.Write("Iteration" + i + ": " + values.Length+" ");

for (int j = 0; j < values.Length; j++)
{

val = values[j].Value[0];
Console.Write(val + ", ");

}
Console.WriteLine("");
System.Threading.Thread.Sleep(500);

}

// Disconnects the VeriStand Gateway from all connected targets.
ErrChk(Workspace.DisconnectFromSystem("", true));

}

private static void ErrChk(Error error)
{

if (error.IsError)

throw new Exception(String.Format("{0:X}", error.Code) + ": " + error.Message);

}
```

Parent topic:

C# Examples

<!--NI_TOPIC bundle=veristand path=calculation-formula-options.html language=enus -->
## TOPIC 00071: Formula Calculated Channel Options

- bundle_id: `veristand`
- source_path: `calculation-formula-options.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/calculation-formula-options.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use standard math operators and functions to create variables that customize calculated channels. All formulas must adhere to the following rules: Every formula must contain a reference to at least one variable. Variables must be contained in brackets. For example, [variable]. Element-wise calculati

### Formula Calculated Channel Options

Use standard math operators and functions to create variables that customize calculated
 channels.

All formulas must adhere to the following rules:

- Every formula must contain a reference
 to at least one variable.
- Variables must be contained in brackets. For
 example, [variable] .
- Element-wise calculation is done when
 one of the operands is a variable or the parameter is a variable.
- Decimal separators on literal numbers
 must be periods. Alternative separators, such as commas, are not supported.

Refer to the following table of supported formula formats for examples that you can
 use to configure a calculated variable.

| Formula format | Description | Example |
| --- | --- | --- |
| [<variable>] + x | Element-wise arithmetic addition | [Var0] + 1 |
| [<variable x>] + [variable y>] | [Var0] + [Var1] |  |
| [<variable>] - x | Element-wise arithmetic subtraction | [Var0] - 1 |
| [<variable x>] - [<variable y>] | [Var0] - [Var1] |  |
| [<variable>] * x | Element-wise arithmetic multiplication | [Var0] * 5 |
| [<variable x>] * [<variable y>] | [Var0] * [Var1] |  |
| [<variable>] / x | Element-wise arithmetic division | [Var0] / 5 |
| [<variable x>] / [<variable y>] | [Var0] / [Var1] |  |
| function([<variable>]) | Apply the function to the variable | sin([Var0]) |
| x + y * z / [<variable>] | Arithmetic equation | 2 + 3 * 4 / [Var0] |
| (x + y) * z / [<variable>] | Arithmetic equation | (2 + 3) * 4 / [Var0] |
| -[<variable>] | Unary minus | -[Var0] |
| +[<variable>] | Unary plus (a no-op) | +[Var0] |
| [<variable>]^x | Power operator | [Var0]^3 |
| Note The data type for all numerics is double-precision, floating-point. |  |  |

Refer to the following table of supported functions and operators for examples of formula
 elements that you can use to configure a calculated channel.

|  | Formula element | Definition |
| --- | --- | --- |
| Supported Function | sin(x) | Calculates the sine of x. Enter x in radians. |
| cos(x) | Calculates the cosine of x. Enter x in radians. |  |
| tan(x) | Calculates the tangent of x. Enter x in radians. |  |
| asin(x) | Calculates the inverse of sine of x. The result is in radians. |  |
| acos(x) | Calculates the inverse of cosine of x. The result is in radians. |  |
| atan(x) | Calculates the inverse of tangent of x. The result is in radians. |  |
| abs(x) | Returns the absolute value of x. |  |
| rand() | Generates a random number between 0 and 1. |  |
| exp(x) | Computes the value of e raised to the x power. |  |
| sqrt(x) | Calculates the square root of x. |  |
| sign(x) | Returns 1 if x is greater or less than 0. Returns 0 if x is equal to 0. |  |
| int(x) | Calculates the integer value of x. |  |
| Supported Operator | + | Addition |
| - | Subtraction |  |
| * | Multiplication |  |
| / | Division |  |
| ( ) | Parenthesis. The contents are evaluated first |  |
| ^ | Calculate the base raised to the power of the exponent |  |

Parent topic:

Adding a Calculated Channel

<!--NI_TOPIC bundle=veristand path=calibrate-harware-channel.html language=enus -->
## TOPIC 00072: Calibrating a Hardware Channel at Run Time

- bundle_id: `veristand`
- source_path: `calibrate-harware-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/calibrate-harware-channel.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Channel Calibration tool in VeriStand to apply polynomial calibration to hardware channel values during a running system definition. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard or Custom Tools Menu Item. You can cali

### Calibrating a Hardware Channel at Run
 Time

Use the Channel Calibration tool in VeriStand to apply polynomial calibration to
 hardware channel values during a running system definition.

Workspace

Tools

Note

VeriStand supports polynomial calibrations with up
 to ten coefficients. A simple polynomial calibration is a linear
 calibration, y = mx + b, where m is the
 first-order coefficient (a1) that serves as the scale and b is the
 constant (a0) that serves as an offset.

1. In the Workspace, select Tools»Channel Calibration to launch the tool. 
 Note The
 name of this menu item might differ depending on how
 you named it in the Tools
 Properties dialog box.
2. In the Channel Calibration tool under
 Scalable Channels, select a
 channel you want to calibrate.
3. Click Next.
4. On the User Information page, enter
 metadata about the specific calibration procedure you want
 to perform. 
 Note This
 information is used to store the history of
 calibrations performed for a channel. You can view
 the information by clicking View
 History on the main page of the
 Channel Calibration tool.
5. On the Polynomial Calibration Details
 page, enter coefficients to define the polynomial equation
 that will calibrate the channel. 
 Note You can
 click Build Table and then
 complete a procedure for automatically calculating
 polynomial coefficients that best fit raw sensor
 values to known input values.
6. Click Finish.

Scaled and Calibrated Value

Scalable Channels

When you close the Channel
 Calibration tool, the calibration remains
 applied to the channel. Even if you close the
 Workspace or undeploy and redeploy the
 system definition, the calibration remains active until you remove
 it.

You also can use the Calibration VIs in the LabVIEW
 Execution API to automate applying calibrations and reading raw values from
 hardware channels.

Parent topic:

Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=call-procedure-from-alarm.html language=enus -->
## TOPIC 00073: Calling One Procedure from Multiple Alarms

- bundle_id: `veristand`
- source_path: `call-procedure-from-alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/call-procedure-from-alarm.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure an Alarm Command step to trigger an alarm that executes a procedure without resetting/disabling the alarm and exiting the subroutine. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explor

### Calling One Procedure from Multiple
 Alarms

Configure an Alarm Command step to trigger an alarm that executes a procedure without
 resetting/disabling the alarm and exiting the subroutine.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Procedures in the configuration tree.
4. Click a procedure.
5. Click Add»Alarm Command.
6. Double-click the alarm command you added.
7. In the Alarm Command Step Configuration page, click the
 Function drop-down, and select an option that resets
 or disables the alarm. 
 Note The Alarm field should be
 grayed out, indicating that the step will execute for the calling alarm. If
 it is not, enable Apply settings to the alarm that tripped this
 procedure.
8. Save the system definition file.

Parent topic:

Adding and Configuring a Procedure

<!--NI_TOPIC bundle=veristand path=call-real-time-sequence-from-expression.html language=enus -->
## TOPIC 00074: Calling a Real-Time Sequence from an Expression

- bundle_id: `veristand`
- source_path: `call-real-time-sequence-from-expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/call-real-time-sequence-from-expression.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use expressions to call real-time sequences from within other real-time sequences. Add a reference to the real-time sequence you want to call. Enter the sequence alias, which appears to the right of the file name in the References pane, into the Expression component of the Property Browser. In paren

### Calling a Real-Time Sequence from an
 Expression

Use expressions to call real-time sequences from within other real-time
 sequences.

1. Add a reference to the real-time
 sequence you want to call.
2. Enter the sequence alias, which appears to the right of the
 file name in the References pane, into
 the Expression component of the
 Property Browser.
3. In parentheses following the alias, list each parameter of the
 sequence. 
 For example, if the alias is Sequence,
 and the sequence contains the parameters
 Parameter1 and
 Parameter2, the expression
 must contain:
 Sequence(Parameter1, Parameter2)

.nivsseq

Note

Parent topic:

Adding and Editing Expressions in a Real-Time Sequence

<!--NI_TOPIC bundle=veristand path=call-real-time-sequence-from-sequence.html language=enus -->
## TOPIC 00075: Calling a Real-Time Sequence from Another Sequence

- bundle_id: `veristand`
- source_path: `call-real-time-sequence-from-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/call-real-time-sequence-from-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Call real-time sequences by reference to run multiple sequences in parallel. You can add references to real-time sequences or CSV files that you call as sequences, and then call those references from expressions within an existing sequence. Create a real-time sequence to serve as the calling file. I

### Calling a Real-Time Sequence from Another
 Sequence

Call real-time sequences by reference to run multiple sequences in parallel.

You can add references to real-time sequences or CSV files that you
 call as sequences, and then call those references
 from expressions within an existing sequence.

1. Create a
 real-time sequence to serve as the calling file.
2. In the References pane, select
 References.
3. On the Home tab of the ribbon, click
 Reference.
4. Use the File dialog box to navigate to the real-time sequence
 (.nivsseq) or CSV file you want to reference. 
 Note If the real-time sequence or CSV file is saved in the same directory as
 the sequence you are editing, you can also drag the real-time sequence or
 CSV file from the Sequences pane to
 References to create the reference.

After you add the reference, you can use an expression to
 call the referenced real-time sequence.

Parent topic:

Creating Real-Time Sequences

<!--NI_TOPIC bundle=veristand path=call-real-time-sequence-stimulus-profile.html language=enus -->
## TOPIC 00076: Calling a Real-Time Sequence from a Stimulus Profile

- bundle_id: `veristand`
- source_path: `call-real-time-sequence-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/call-real-time-sequence-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Call a real-time sequence file from within a stimulus profile to define a specific task to execute on a unit under test (UUT). Before you begin, create a stimulus profile. Open the stimulus profile from which you want to call the sequence in the Stimulus Profile Editor. In the Steps palette, expand

### Calling a Real-Time Sequence from a Stimulus
 Profile

Call a real-time sequence file from within a stimulus profile to define a specific task
 to execute on a unit under test (UUT).

Before you begin, create a stimulus profile.

1. Open the stimulus profile from which you want to call the
 sequence in the Stimulus Profile
 Editor.
2. In the Steps palette, expand
 Real-Time Sequences.
3. Select Real-Time Sequence Call and
 drag it to the stimulus profile code.
4. In the Property Browser, enter a
 File Path where the real-time
 sequence (.nivsseq) file is located.
5. Use the Parameters section of the
 Property Browser to map the sequence input parameters to
 channels. 
 Note If the
 stimulus profile you are using is saved in the same
 directory as a real-time sequence,you can drag the
 real-time sequence file from the
 Sequences palette directly
 to the stimulus profile code to create a Real-Time
 Sequence Call step that calls that sequence.

Property Browser

Update
 Parameters

VeriStand also supports CSV files as real-time
 sequences. The process for calling real-time sequences defined in
 CSV files is the same as the process for calling
 .nivsseq files. However, you cannot view
 the real-time sequence defined by a CSV file in the
 Stimulus Profile Editor. If you want to
 make edits to the real-time sequence, you must use a text
 editor.

Parent topic:

Creating Stimulus Profiles

<!--NI_TOPIC bundle=veristand path=call-subscript-model-parameter.html language=enus -->
## TOPIC 00077: Calling a Subscript from a Model Parameter File

- bundle_id: `veristand`
- source_path: `call-subscript-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/call-subscript-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Call a subscript file from a model parameter text file to insert additional parameter updates at runtime in VeriStand. Before you begin, learn about the supported syntax for .txt files. Open a formatted .txt file. Create or open a second text file that updates parameters from the same model. This is

### Calling a Subscript from a Model Parameter
 File

Call a subscript file from a model parameter text file to insert additional
 parameter updates at runtime in VeriStand.

.txt

1. Open a formatted .txt file.
2. Create or open a second text file that updates parameters from
 the same model. 
 Note This is the subscript file. The subscript file must
 use the same delimiter as the calling file.
3. In the original file, create a new line to call the
 subscript.
4. Enter subscript in the
 parameter column and the path to
 the file to call in the value column. 
 Note The path can be absolute or relative to the directory
 that contains the calling file.

When the call to the top-level text file executes,
 VeriStand inserts the contents of the subscript file into the calling file
 at the line that contains the subscript call. You also can use subscript
 calls recursively to call subscripts from within subscripts.

ParameterUpdate2.txt

subfile.txt

Note

```text
{environment temperature (C)}     50 * tempConversionFactor
subscript     subfile.txt
```

This
 file is part of the Update Model Parameters example, available in
 the <Common Data>\Examples\Stimulus Profile\Engine
 Demo\Stimulus Profiles\ directory.

Parent topic:

Setting Model Parameters

<!--NI_TOPIC bundle=veristand path=case-statement.html language=enus -->
## TOPIC 00078: Case Statement

- bundle_id: `veristand`
- source_path: `case-statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/case-statement.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A functional statement under which you add code that executes if a test condition is met. A case statement executes if its Case Value matches the value of the Test Expression for the Switch statement that contains the case. To specify the code that the case executes, drag expressions and other primi

### Case Statement

A functional statement under which you add code that executes if a test condition is
 met.

A case statement executes if its Case Value
 matches the value of the Test Expression for the Switch
 statement that contains the case.

To specify the code that the case executes, drag expressions and other primitives to
 the case and configure them as you would any other section of sequence code.

| Property/Section | Description |
| --- | --- |
| Case Value | The value to check against the Test Expression for the Switch statement. If the two values match, this case executes. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Switch Statement Primitives

<!--NI_TOPIC bundle=veristand path=change-initial-model-parameter.html language=enus -->
## TOPIC 00079: Changing the Initial Value of Model Parameters

- bundle_id: `veristand`
- source_path: `change-initial-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/change-initial-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Apply initial model parameter values from a .txt file during system definition deployment in VeriStand. You can switch parameter sets between tests without recompiling the model. Before you begin, format the initial values in the .txt file to VeriStand supported syntax. By default, the initial value

### Changing the Initial Value of Model
 Parameters

Apply initial model parameter values from a .txt file during
 system definition deployment in VeriStand. You can switch parameter sets between tests
 without recompiling the model.

.txt

By default, the initial values of parameters
 are the values that were compiled into the model. However, VeriStand can automatically apply
 parameter values from a file when you deploy the system definition file. You can switch
 initial parameter values between tests without recompiling models.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Simulation Models in the configuration tree.
4. On the Model Configuration page, click Apply
 parameter values from a file at initialization.
5. Configure the paths to the parameter file and any dependent files. 
 Note You can only select one model parameter file for VeriStand to apply to models on the
 target that contain matching parameters. Use the main model parameter file to call
 subscripts saved in separate files.
6. Save the system definition file.

Parent topic:

Setting Model Parameters

<!--NI_TOPIC bundle=veristand path=channel-calibration.html language=enus -->
## TOPIC 00080: Channel Calibration

- bundle_id: `veristand`
- source_path: `channel-calibration.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/channel-calibration.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Channel Calibration tool displays channel information such as channel names, paths, values, and calibration dates you use to calibrate your hardware. The following image highlights the layout of the Channel Calibration tool you will interact with to calibrate values received from a hardware devi

### Channel Calibration

The Channel Calibration tool displays channel information such as
 channel names, paths, values, and calibration dates you use to calibrate your hardware.

The following image highlights the layout of the Channel
 Calibration tool you will interact with to calibrate values received
 from a hardware device.

[IMAGE alt='image' src='GUID-3071A9D6-9B7A-484F-B9B3-7A7D84531C8B-a5.png']

| 1 | Scalable Channels—Displays both the Raw Value the channel acquires or generates and the Scaled and Calibrated Value. Values in the latter column reflect both scales mapped to the channel in the system definition and calibrations you apply to the channel with this tool. |
| --- | --- |
| 2 | Units—Displays the units associated with the channel. If you map a scale to the channel, the units associated with the scale display. |
| 3 | Delete Calibration—Removes a selected channel. The button is disabled when a selected channel does not have a calibration applied to it. |
| 4 | Show hidden channels?—Displays hidden channels available for calibration in the Scalable Channels table. |
| 5 | View History—Displays information about previous calibrations performed for a channel, including the date and time it started and the calibration coefficients. |

Parent topic:

Calibrating a Hardware Channel at Run Time

<!--NI_TOPIC bundle=veristand path=channel-data-viewer.html language=enus -->
## TOPIC 00081: Viewing Channel Values at Run Time

- bundle_id: `veristand`
- source_path: `channel-data-viewer.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/channel-data-viewer.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Monitor channels with the Channel Data Viewer to view the current values of several channels together. In the VeriStand Editor, Click View Channel Data Viewer . In the Channel Data Viewer tab, click the Channel Filter pull-down menu and select the type of channels to display. Type of channel Descrip

### Viewing Channel Values at Run Time

Monitor channels with the Channel Data
 Viewer to view the current values of several channels
 together.

1. In the VeriStand Editor, Click View»Channel Data Viewer.
2. In the Channel Data Viewer tab, click the
 Channel Filter pull-down menu and select the type of
 channels to display. 
 Type of channelDescriptionChannels
 Displays all channels in the system definition file.Parameters
 Displays model parameters.Writable
 Displays all writable channels. To update the value of a writable
 channel, click inside the Pending Value cell for
 the channel, enter the desired value, and then click Apply
 Pending Changes.Aliases
 Displays all aliases defined in the system definition file.Custom
 Allows you to display channels of your choosing. To select the
 channels to display, click Select Channels and
 use the system definition configuration tree to select the channels to
 display.

Parent topic:

VeriStand Editor Tools

<!--NI_TOPIC bundle=veristand path=channel-group-step.html language=enus -->
## TOPIC 00082: Channel Group Step

- bundle_id: `veristand`
- source_path: `channel-group-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/channel-group-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Groups channels in a logging configuration. TDMS files arrange log data into groups of channels. The Channel Group Name you specify and the Channels you add to the group correspond to the group and channels that appear in the TDMS file. You can create multiple channel groups under a single logging c

### Channel Group Step

Groups channels in a logging configuration.

Note

| Property/Section | Description |
| --- | --- |
| Channel Group Name | Specifies the name of the channel group. |
| Channels | Specifies the channels that belong to the channel group. Click the search button to display an interactive system definition hierarchy tree. Place check marks next to the channels you want to add to the channel group. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Logging Steps

<!--NI_TOPIC bundle=veristand path=channel-value-force.html language=enus -->
## TOPIC 00083: Using Channel Value Forcing

- bundle_id: `veristand`
- source_path: `channel-value-force.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/channel-value-force.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Channel Value Forcing sets a fault value on a selected channel to test system behavior at specific values. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard or Custom Tools Menu Item. In the Workspace, select Tools Channel Fault M

### Using Channel Value Forcing

Channel Value Forcing sets a fault value on a selected channel to test system
 behavior at specific values.

Workspace

Tools

1. In the Workspace, select Tools»Channel Fault Manager to launch the tool. 
 Note The name of this menu item
 might differ depending on how you named it in the Tools
 Properties dialog box.
2. In the Channel Fault Manager tool, select a channel from
 the configuration tree and click Add Fault.
3. In the Fault Value dialog box, enter a fault value for the
 specified channel and click OK.

Channel Fault Manager

Parent topic:

Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=ci-count-up-down.html language=enus -->
## TOPIC 00084: Count Up/Count Down Channel Properties (CI)

- bundle_id: `veristand`
- source_path: `ci-count-up-down.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ci-count-up-down.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter input (CI) channel properties to count the rising or falling edges of a digital signal. For more information on counting edges, refer to the NI-DAQmx Manual. Property/Section Description Count Edge Specifies on which edges of the input signal to increment or decrement the count: Fa

### Count Up/Count Down Channel Properties
 (CI)

Configure counter input (CI) channel properties to count the rising or falling edges of
 a digital signal.

For more information on counting edges, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Count Edge | Specifies on which edges of the input signal to increment or decrement the count: Falling—Count falling edges. Rising—Count rising edges. |
| Count Direction | Specifies whether to increment or decrement the counter on each edge of the type you specify with the Count Edge property: Count down—Decrement counter. Count up—Increment counter. Externally Controlled—The state of a digital line controls the count direction. Each counter has a default count direction terminal. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Manual
- NI-DAQmx: Connecting Counter Signals

<!--NI_TOPIC bundle=veristand path=ci-frequency.html language=enus -->
## TOPIC 00085: Frequency Channel Properties (CI)

- bundle_id: `veristand`
- source_path: `ci-frequency.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ci-frequency.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter input (CI) channel properties to measure the frequency of a digital signal. VeriStand measures the frequency of a digital signal by counting observed edges and performing a software calculation over a period of time determined by your expected frequency range. This method uses a so

### Frequency Channel Properties (CI)

Configure counter input (CI) channel properties to measure the frequency of a digital
 signal.

Note

System Explorer

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. Note The minimum value of frequency determines, and is equal to, the measurement frequency resolution. The measurement time is equal to the reciprocal of the minimum frequency value. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Count Edge | Specifies on which edges of the input signal to increment or decrement the count: Falling—Count falling edges. Rising—Count rising edges. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related reference:

- Pulse Measurement Channel Properties (CI)

<!--NI_TOPIC bundle=veristand path=ci-position.html language=enus -->
## TOPIC 00086: Position Channel Properties (CI)

- bundle_id: `veristand`
- source_path: `ci-position.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ci-position.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter input (CI) channel properties for channels that use a linear encoder to measure linear position. For more information on encoders and measuring linear displacement, refer to Encoders and Measuring Linear Displacement in the NI-DAQmx Manual. Property/Section Description Z Index Mode

### Position Channel Properties (CI)

Configure counter input (CI) channel properties for channels that use a linear encoder
 to measure linear position.

For more information on encoders and measuring linear displacement, refer to
 *Encoders* and *Measuring Linear Displacement* in the
 NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Z Index Mode | Specifies the states at which signal A and signal B must be while signal Z is high for VeriStand to reset the measurement. Note If signal Z is never high while signal A and signal B are high, you must choose a phase other than A High B High. A High B High—Reset the measurement when signal A and signal B are high. A High B Low—Reset the measurement when signal A is high and signal B is low. A Low B High—Reset the measurement when signal A is low and signal B high. A Low B Low—Reset the measurement when signal A and signal B are low. When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B. |
| Decoding | Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. 2 Pulse Counting—Increment the count on rising edges of signal A. Decrement the count on rising edges of signal B. If you select this value, the Z Index Mode property is ignored. X1—If signal A leads signal B, count the rising edges of signal A. If signal B leads signal A, count the falling edges of signal A. X2— Count the rising and falling edges of signal A X4—Count the rising and falling edges of signal A and signal B. Note 2 Pulse Counting is valid only for two-pulse encoders. X2 and X4 decoding are more sensitive to smaller changes in position than X1 encoding, with X4 being the most sensitive. However, more sensitive decoding is more likely to produce erroneous measurements if vibration exists in the encoder or other noise exists in the signals. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Measuring Linear Displacement
- NI-DAQmx Common Applications
- Encoders

<!--NI_TOPIC bundle=veristand path=ci-pulse-measurement.html language=enus -->
## TOPIC 00087: Pulse Measurement Channel Properties (CI)

- bundle_id: `veristand`
- source_path: `ci-pulse-measurement.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ci-pulse-measurement.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter input (CI) channel properties to measure pulse specifications. A pulse specification is a pairing of high time and low time values. In addition to X Series DAQ devices, PXIe-6612 and PXIe-6614 devices also can perform a pulse measurement in VeriStand. VeriStand returns measurements

### Pulse Measurement Channel Properties
 (CI)

Configure counter input (CI) channel properties to measure pulse
 specifications.

pulse specification

Note

System
 Explorer

Note

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure before VeriStand performs any scaling or calibration. |
| Sample Clock Source | Specifies the name of the source terminal of the sample clock. You can use an internal counter timebase when performing counter measurements or an external timebase. For more information, refer to Terminal Names in the NI-DAQmx Manual. |
| Sample Clock Rate | Specifies in hertz the sampling rate in samples per channel per second. If you use an external source for the sample clock, set this input to the maximum expected rate of that clock. |
| Active Edge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge: Falling—Falling edge(s). Rising—Rising edge(s). |
| Timeout Value | Specifies an amount of time to wait for the channel to return valid data. VeriStand considers invalid data to be repeated values, which might occur if the system attempts to read data faster than the Sample Clock Rate property. When VeriStand reads invalid data, it continues to read from the channel while it counts until the Timeout Value. VeriStand will return values of NaN until the channel returns valid data again. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- Terminal Names

<!--NI_TOPIC bundle=veristand path=ci-time-period.html language=enus -->
## TOPIC 00088: Time Period Channel Properties (CI)

- bundle_id: `veristand`
- source_path: `ci-time-period.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ci-time-period.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter input (CI) channel properties to measure the period of a digital signal. With this measurement type, VeriStand measures the period of a digital signal by counting observed edges and performing a software calculation over a period of time determined by your expected range. This meth

### Time Period Channel Properties (CI)

Configure counter input (CI) channel properties to measure the period of a digital
 signal.

Note

System Explorer

| Property/Section | Description |
| --- | --- |
| Minimum Value | The minimum value you expect to measure before VeriStand performs any scaling or calibration. |
| Maximum Value | The maximum value you expect to measure, before VeriStand performs any scaling or calibration.Note The maximum value of the time period determines, and is equal to, the measurement time required. The maximum update rate of the measurement is equal to the reciprocal of the maximum time period. |
| Count Edge | Specifies on which edges of the input signal to increment or decrement the count: Falling—Count falling edges. Rising—Count rising edges. |

Note

Parent topic:

Adding and Configuring DAQ Device Channels

<!--NI_TOPIC bundle=veristand path=close-active-veristand-project.html language=enus -->
## TOPIC 00089: Close Active VeriStand Project

- bundle_id: `veristand`
- source_path: `close-active-veristand-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/close-active-veristand-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the active VeriStand project (.nivsprj) file. Property/Section Description Description Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor.

### Close Active VeriStand Project

Closes the active VeriStand project (.nivsprj) file.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Project Steps

<!--NI_TOPIC bundle=veristand path=close-workspace.html language=enus -->
## TOPIC 00090: Close VeriStand Workspace

- bundle_id: `veristand`
- source_path: `close-workspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/close-workspace.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the VeriStand workspace. Property/Section Description Description Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor.

### Close VeriStand Workspace

Closes the VeriStand workspace.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Workspace Steps

<!--NI_TOPIC bundle=veristand path=co-pulse-generation.html language=enus -->
## TOPIC 00091: Pulse Generation Channel Properties (CO)

- bundle_id: `veristand`
- source_path: `co-pulse-generation.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/co-pulse-generation.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure counter output (CO) channel properties to generate digital pulses. VeriStand generates digital pulses that are defined by pairs of frequency and duty cycle values. Provide these values for each counter output channel that generate pulses through two additional channels, Frequency and Duty

### Pulse Generation Channel Properties
 (CO)

Configure counter output (CO) channel properties to generate digital pulses.

VeriStand generates digital pulses that
 are defined by pairs of frequency and duty cycle values. Provide these values for
 each counter output channel that generate pulses through two additional channels,
 Frequency and Duty Cycle, that appear under the counter channels in System
 Explorer.

The following illustration shows the parts of a
 pulse.

[IMAGE alt='image' src='GUID-24C8335A-AB91-49EA-8C2D-8E4712B0855A-a5.png']

Note

False

True

| Property/Section | Description |
| --- | --- |
| Idle State | Specifies the resting state of the output terminal: High—Terminal is at a high state at rest. A pulse with a high idle state starts high, pulses to low, and returns to high. Low—Terminal is at a low state at rest. A pulse with a low idle state starts at the low value, pulses high, and returns to low. |
| Initial Delay | Specifies the amount of time the output remains at the idle state before generating the pulse. The idle state always replaces high time or low time for the first pulse of a generation, depending on the idle state. |
| Enable HWTSP | True—Generate pulses continuously using hardware timing without a buffer. This timing type is called hardware-timed single-point sample mode. False—Generates pulses continuously without specifying timing. This timing type is called implicit because the signal being measured is itself the timing signal or the timing is implicit in the rate of the generated pulse train.Note Implicit timing is appropriate when the measurement does not require sample timing, such as with counters for buffered frequency measurement, buffered period measurement, or pulse train generation. |
| HWTSP Clock Source | If the Enable HWTSP property is True, this property specifies the name of the source terminal of the sample clock. Otherwise, this property is ignored. You can use an internal counter timebase when performing counter measurements or an external timebase. For more information, refer to Terminal Names in the NI-DAQmx Manual.Note A DAQ analog channel with hardware-timed sample mode or an FPGA device must be configured as the chassis master hardware synchronization device on the Chassis Configuration page in System Explorer. Otherwise, the clock source is not available, and VeriStand returns an error during deployment. |
| HWTSP Clock Rate | If the Enable HWTSP property is True, this property specifies the sampling rate in samples per channel per second. Otherwise, this property is ignored. If you use an external source for the sample clock, set this input to the maximum expected rate of that |

Note

- If the Enable HWTSP property is set to False ,
 VeriStand ignores the new value and continues using the latest value you
 successfully set.
- If Enable HWTSP is set to True , VeriStand returns an
 error.

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications
- Terminal Names

<!--NI_TOPIC bundle=veristand path=command-shell.html language=enus -->
## TOPIC 00092: Command Shell Step

- bundle_id: `veristand`
- source_path: `command-shell.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/command-shell.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes the Windows Command Prompt, calls the application specified by Filename, and passes that application the specified arguments. You can configure whether the rest of the stimulus profile waits for the Command Prompt to return before completing execution. Property/Section Description Descriptio

### Command Shell Step

Invokes the Windows Command Prompt, calls the application specified by Filename, and
 passes that application the specified arguments.

You can configure whether the rest of the stimulus profile waits for the Command
 Prompt to return before completing execution.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Command Prompt | Includes the following properties that configure interaction with the Command Prompt: Filename—The name of the application to pass arguments to. You can enter a system command (for example, cmd notepad), a system variable, or the fully-qualified path to the executable. Arguments—The arguments to pass to the called application. Hide command shell—If True, runs the application in an inaccessible Command Prompt window. Note If Redirect Standard Error and Redirect Standard Output are both False, the stimulus profile ignores a True value for this option and always shows the Command Prompt. |
| Execution | Includes the following properties that configure step execution: Wait to Complete—If True, blocks execution of the remainder of the stimulus profile until the Command Prompt returns.Note The Command Prompt does not return until all applications it calls are properly closed. Wait Timeout—Specifies the time in milliseconds to wait for the Command Prompt to return before returning a timeout error. The default is -1 to specify an infinite timeout. Redirect Standard Error—If True, writes the standard error output of the Command Prompt to the ATML test results file for the stimulus profile. Redirect Standard Output—If True, writes the standard output of the Command Prompt to the ATML test results file for the stimulus profile. |

Parent topic:

Other Steps

<!--NI_TOPIC bundle=veristand path=comment.html language=enus -->
## TOPIC 00093: Comment

- bundle_id: `veristand`
- source_path: `comment.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/comment.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Document in your real-time sequence code. Comments have no effect on the execution of the code. Property/Section Description Comment The text of the comment. Description Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor.

### Comment

Document in your real-time sequence code.

Comments have no effect on the execution of the code.

| Property/Section | Description |
| --- | --- |
| Comment | The text of the comment. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Miscellaneous Primitives

<!--NI_TOPIC bundle=veristand path=common-issues.html language=enus -->
## TOPIC 00094: Common Issues with Models in VeriStand

- bundle_id: `veristand`
- source_path: `common-issues.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/common-issues.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your model crashes or does not execute as expected, isolate the issue and determine if its source is within the model or due to your system definition. To identify the source of an issue, replace your model in the system definition with a simple model, and then redeploy the system definition. If

### Common Issues with Models in VeriStand

If your model crashes or does not execute as expected, isolate the issue and determine if
 its source is within the model or due to your system definition.

To identify the source of an issue, replace your model in the system definition with a simple
 model, and then redeploy the system definition. If the simple model executes as
 expected, the source of the issue is within your model. However, if the simple model
 also experiences issues, the source of the issue is due to settings for your system
 definition.

The following table lists common model issues and solutions.

| Issue | Solutions |
| --- | --- |
| Model is crashing | Models often crash when an inport receives a value of 0 and the model attempts to divide by the inport value. This issue will occur during deployment if the initial state of the model is to run and the default value for an inport is 0. Depending on your system, complete the following troubleshooting solutions: Change the default value for the inport. Rewrite the model to remove the possibility of dividing by 0. Change the initial state of the model to be paused in System Explorer and implement a start-up procedure that ensures that the inport values are acceptable before you start the model. |
| Model runs too fast or slow | If your model is unstable because it runs too fast or too slow, ensure the actual model rate matches the rate at which the model was compiled to run. If the rates do not match, adjust the settings that determine the actual model rate until the following expressions are correct: actual model rate = compiled model rate actual model rate = PCL rate / decimation Adjust the model timing by configuring the following settings where specified: Compiled loop rate—Displays on the Model Configuration page, in Simulation model info. Model decimation—Set on the Model Configuration page, in the Decimation control. PCL rate—Set on the Controller Configuration page with the Target Rate control. |
| Model generated data is delayed | If other parts of your system that are mapped to your model do not receive data when you expect, consider adjusting the following system definition settings: PCL execution mode—Change the execution mode to low latency if data from models must be available for mapping during the same PCL iteration the model generates the data. The default mode, parallel, applies a one-cycle delay between when a model executes and when the data it produces is available for mapping. Execution order—Multiple models in a system execute in parallel unless you define an execution order. If you map an outport from one model to an inport of a second model and you want the second model to wait until the first model finishes executing before it runs, you must define the execution order. |
| Decreased system performance | If you suspect that models are causing your system to run slower than you desire, consider the following solutions to improve performance: Import only parameters and signals your system requires. Importing many parameters and signals can have a negative impact on the performance of the model even if the model is not running. If you do not need data from models to be available to the rest of the system on the same iteration of the PCL, set the PCL execution mode to parallel instead of low latency. Parallel mode causes a one-cycle delay between when a model executes and when the data it produces is available to the system, but increases the execution speed of the entire system. |

If you continue experiencing issues with your model, contact NI Support.

Parent topic:

Integrating and Executing Models

Related concepts:

- Primary Control Loop Step Execution in Models

Related tasks:

- Setting Default Values for Inports
- Adding and Configuring a Procedure
- Setting Model Timing
- Configuring the Execution Order of Models

Related information:

- NI Support

<!--NI_TOPIC bundle=veristand path=communicate-veristand-editor-stimulus-profile.html language=enus -->
## TOPIC 00095: Communicating with the VeriStand Editor Using Stimulus Profile Arguments

- bundle_id: `veristand`
- source_path: `communicate-veristand-editor-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/communicate-veristand-editor-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Send commands to the VeriStand Editor through a stimulus profile to specify a VeriStand project, a system definition, VeriStand Gateway IP address, or connect to a target from the system definition. Depending on your goal, use an argument to send a command to the VeriStand Editor. Goal Argument Exam

### Communicating with the VeriStand Editor Using
 Stimulus Profile Arguments

Send commands to the VeriStand Editor through a
 stimulus profile to specify a VeriStand project, a system definition, VeriStand Gateway
 IP address, or connect to a target from the system definition.

VeriStand Editor

| Goal | Argument | Example |
| --- | --- | --- |
| Specify the VeriStand project to run. | /nivsprj | /nivsprj "<Common Data>\\Examples\\Stimulus Profile\\Engine Demo\\Engine Demo.nivsprj" |
| Specify the system definition file to use. | /sysdef | /sysdef "<Common Data>\\Examples\\Stimulus Profile\\Engine Demo\\Engine Demo.nivssdf" |
| Specify the IP address of the VeriStand Gateway. | gateway | /gateway 10.0.38.64 |
| Tell the VeriStand editor to connect to the target defined by the system definition file. | /connect | /connect |

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

<!--NI_TOPIC bundle=veristand path=compile-fpga-vi-to-bitfile.html language=enus -->
## TOPIC 00096: Compiling a Custom FPGA VI into a Bitfile

- bundle_id: `veristand`
- source_path: `compile-fpga-vi-to-bitfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/compile-fpga-vi-to-bitfile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Prepare to use your FPGA VI in an FPGA target by compiling the VI into a bitfile. Before you begin, create a customized FPGA VI. FPGA VIs define the analog, digital, and pulse width modulation (PWM) inputs and outputs of an FPGA target. A bitfile contains the information that FPGA targets need to fu

### Compiling a Custom FPGA VI into a
 Bitfile

Prepare to use your FPGA VI in an FPGA target by compiling the VI into a
 bitfile.

Before you begin, create a customized
 FPGA VI.

bitfile

Note

LabVIEW Help

Help

»

LabVIEW Help

1. Open LabVIEW.
2. In Project Explorer, right-click the FPGA VI, and select
 Compile.

FPGA
 Bitfiles

<name of project>_<name of FPGA
 VI>.lvbitx

After creating a bitfile, create an FPGA
 configuration file.

Parent topic:

Customizing an FPGA Target

Related tasks:

- Customizing an FPGA VI
- Creating a Custom FPGA Configuration File

<!--NI_TOPIC bundle=veristand path=components.html language=enus -->
## TOPIC 00097: Components of a VeriStand System

- bundle_id: `veristand`
- source_path: `components.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/components.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A VeriStand system includes VeriStand, test hardware, add-ons, and extensions. Component Type Component Notes Software VeriStand Install VeriStand and recommended drivers using NI Package Manager. Hardware Real-time hardware device Use any hardware that runs NI Linux Real-Time (Intel x64-based). For

### Components of a VeriStand System

A VeriStand system includes VeriStand, test hardware, add-ons, and
 extensions.

| Component Type | Component | Notes |
| --- | --- | --- |
| Software | VeriStand | Install VeriStand and recommended drivers using NI Package Manager. |
| Hardware | Real-time hardware device | Use any hardware that runs NI Linux Real-Time (Intel x64-based). For more information, refer to the release notes. |
| Optional Add-ons | VeriStand custom devices Simulink models | Install VeriStand custom devices using NI Package Manager and GitHub. For more information, refer to NI GitHub. You can also develop your own custom devices. For more information refer to the VeriStand Custom Device Handbook. To use Simulink CPU models, refer to the VeriStand Model Generation Support toolbox. For Simulink FPGA targeted models, refer to HDL Coder Support Package for NI FPGA Hardware. |
| Optional Extensions | System Definition API Execution API | Use the System Definition API to automate the configuration of a VeriStand system. Use the Execution API to automate the orchestration of a VeriStand system. You can access these APIs from C#, Python, and LabVIEW. |

<!--NI_TOPIC bundle=veristand path=conditional-statements.html language=enus -->
## TOPIC 00098: Conditional Statements

- bundle_id: `veristand`
- source_path: `conditional-statements.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/conditional-statements.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Conditional statements to execute different code under different, specified conditions. Palette object Description If Else A statement that defines an expression to evaluate to determine whether to execute one section of code or another. Subpalette Description Switch Statement Primitives Use

### Conditional Statements

Use the Conditional statements to execute different code under different, specified
 conditions.

| Palette object | Description |
| --- | --- |
| If Else | A statement that defines an expression to evaluate to determine whether to execute one section of code or another. |

| Subpalette | Description |
| --- | --- |
| Switch Statement Primitives | Use the Switch Statement primitives to create different cases of code to execute based on the value of a test expression. |

Parent topic:

Structures Primitives

Related reference:

- If Else
- Switch Statement Primitives

<!--NI_TOPIC bundle=veristand path=configure-bios-real-time-controller.html language=enus -->
## TOPIC 00099: Configuring the BIOS Settings of the Controller

- bundle_id: `veristand`
- source_path: `configure-bios-real-time-controller.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-bios-real-time-controller.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase the performance of your real-time controller by enabling turbo boost and reducing the number of enabled cores. To configure the BIOS settings for VeriStand, complete any of the following tasks. Task Rationale Enable Turbo Boost Enabling Turbo Boost for Intel Core™ processors allows active p

### Configuring the BIOS Settings of the
 Controller

Increase the performance of your real-time controller by enabling turbo
 boost and reducing the number of enabled cores.

To configure the BIOS settings for VeriStand, complete any of the following
 tasks.

| Task | Rationale |
| --- | --- |
| Enable Turbo Boost | Enabling Turbo Boost for Intel Core™ processors allows active processor cores to run faster than the base operating frequency for short durations while other cores are idle. Note Enabling Turbo Boost can also increase application jitter. |
| Reduce the number of enabled cores. | When you activate Turbo Boost, the maximum frequency of a specific processing core depends on the number of active cores. Manually reducing the number of cores ensures the active cores receive the maximum increase in clock frequency. If your system does not contain asynchronous components, enable only one core to provide the greatest frequency boost. For example, the Intel Core i7-820QM quad-core processor used in an NI PXIe-8133 embedded controller has a base clock frequency of 1.73 GHz. If an application requires only one CPU core, Turbo Boost automatically increases the clock frequency of the active CPU core on the Intel Core i7-820QM processor to 3.06 GHz. |
| Enable two cores for VeriStand systems with asynchronous components, such as an asynchronous custom device. | Enabling two cores allows you to assign the asynchronous components to another CPU while still providing greater clock frequency to both active cores. |

For more information, refer to Top Eight Features of the
 Intel Core i7 Processors for Test, Measurement, and Control.

Parent topic:

Maximizing System Performance

Related information:

- Top Eight Features of the Intel Core i7 Processors for Test,
 Measurement, and Control

<!--NI_TOPIC bundle=veristand path=configure-can-cyclic-frame-faulting.html language=enus -->
## TOPIC 00100: Configuring NI-XNET CAN Cyclic Frame Faulting

- bundle_id: `veristand`
- source_path: `configure-can-cyclic-frame-faulting.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-can-cyclic-frame-faulting.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure NI-XNET CAN outgoing cyclic frame faulting in VeriStand with Skip Cyclic Frames or Transmit Time channels. Before you begin, import an outgoing CAN cyclic frame. In embedded networks, cyclic frames are frames that transmit at regular intervals. You can add the following frame fault channel

### Configuring NI-XNET CAN Cyclic Frame
 Faulting

Configure NI-XNET CAN outgoing cyclic frame faulting in VeriStand with Skip Cyclic
 Frames or Transmit Time channels.

Before you begin, import an outgoing CAN
 cyclic frame.

- Skip Cyclic Frames —Skips transmission of a specified number of cyclic
 frames across the bus.
- Transmit Time —Specifies the amount of time that must elapse between
 subsequent transmissions of a cyclic frame.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET»CAN in the configuration tree.
4. Click a port.
5. Click Outgoing»Cyclic.
6. Select a frame and click Add Faulting Channels
[IMAGE alt='image' src='GUID-F6095C5E-FC46-4836-A34C-50EE943E2404-a5.gif']. 
 VeriStand creates a Frame Faulting section under the frame in the configuration tree.
7. Click Frame Faulting.
8. Depending on your goal, complete the following tasks. 
 Goal
TasksSkip the transmission of a certain number of frames.
Click Skip Cyclic Frames to display the
 Skip Cyclic Frames Configuration page.
Specify the Skip N cycles for the number of cycles
 to skip .
Specify the Trigger channel to use to start
 skipping channels.
Note Skipping begins when this channel does not equal zero.
Specify an amount of time that must elapse between frame
 transmissions.
Click Transmit Time to display the
 Transmit Time Configuration page.
Specify the time that must elapse in the Transmit time
 [sec] field, or select Use trigger channel to set
 transmit time? and specify a trigger channel from which to get
 the time.
Note VeriStand uses the value of the channel as the transmit time, in
 seconds.
9. Save the system definition file.

After creating Frame Faulting channels, you can use them like other channels in VeriStand.
 For example, you can map them to other channels or to controls and indicators in the VeriStand Editor or
 Workspace.

Use the XNET page of the Options dialog box to configure VeriStand to
 always create faulting channels when you import NI-XNET frames. You can also use the
 Import NI-XNET Frames dialog box to automatically create channels on
 a one-time basis when you import frames.

Parent topic:

Using NI-XNET Interfaces

Related concepts:

- Configuring Controls and Indicators to Send and Receive Data

Related tasks:

- Importing NI-XNET Frames
- Mapping Channels and Aliases
- Adding and Configuring Controls and Indicators

<!--NI_TOPIC bundle=veristand path=configure-crc-counters-outgoing-can-frames.html language=enus -->
## TOPIC 00101: Configuring Cyclic Redundancy Checks (CRCs) and Counters for Outgoing NI-XNET CAN Frames

- bundle_id: `veristand`
- source_path: `configure-crc-counters-outgoing-can-frames.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-crc-counters-outgoing-can-frames.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure CRC and counter settings for outgoing NI-XNET CAN frames to verify data integrity and track frame transmissions. Before you begin, import an outgoing CAN frame. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select

### Configuring Cyclic Redundancy Checks (CRCs)
 and Counters for Outgoing NI-XNET CAN Frames

Configure CRC and counter settings for outgoing NI-XNET CAN frames to verify data
 integrity and track frame transmissions.

Before you begin, import an outgoing CAN
 frame.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET»CAN in the configuration tree.
4. Click a port.
5. On the CAN Port Configuration page, click the Automatic Frame
 Processing tab.
6. Click the Installed automatic frame processing binary
 files drop-down to select a file to use for frame
 processing. 
 Note VeriStand supports CRC-8
 and CRC-16 length polynomials.
7. Configure the CRC.
  1. In the Polynomial field, enter a generator polynomial for the
 CRC. 
 This field requires a decimal number. VeriStand converts this number
 to binary form to create the polynomial.
  2. In the Initial CRC field, enter an initial value to use for the CRC
 calculation. 
 This field requires a decimal number. VeriStand converts this number
 to binary form.
  3. In the Final XOR field, enter a value to XOR with the calculated
 CRC.
  4. Optional: 
 If you want to reverse the order of the bits in the CRC before writing
 data into the data stream, select
 Reflected.
8. In the configuration tree, under the CAN port, right-click an outgoing frame
 and select Add Automatic Frame Processing Data.
9. Expand Automatic Frame Processing to view the
 configuration pages for the CRC and counter.
10. Click CRC to display the CRC Configuration page, and
 configure CRC settings.
  1. Under CRC Settings, specify the first included byte and last included
 byte for the CRC.
  2. In the Storage offset [byte] field, specify a number of bytes to offset
 the byte where CRC data is stored. 
 Note The CRC is always the last byte in the data. Set this value to
 n-1, where n is the number of bytes in
 the data, to avoid dropping frame data from the CRC.
  3. Optional: 
 If you want to specify a trigger channel to trigger writing data, click
 Use alternate channel?.
11. Select Counter to display the XNET Counter
 Configuration page, and configure the counter.
  1. Under Counter Settings, enter the Width [bit] of
 the counter. 
 The maximum width is 8.
  2. Specify the Initial value to start the
 counter.
  3. Optional: 
 If you want to specify offsets for counter data, enter a
 Storage offset [byte] and a Bit
 offset [bit].
  4. Optional: 
 If you want to specify a trigger channel to use to trigger writing
 data, click Use alternate channel?.
12. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Importing NI-XNET Frames

<!--NI_TOPIC bundle=veristand path=configure-ethernet-controller.html language=enus -->
## TOPIC 00102: Configuring the Ethernet Settings of the Controller

- bundle_id: `veristand`
- source_path: `configure-ethernet-controller.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-ethernet-controller.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase the performance of your real-time controller by using line interrupt packet detection. Most NI Real-Time targets offer three options for packet detection: Line Interrupt, Polling, and Message Signal Interrupt. Line Interrupt provides the fastest performance as the device driver gets immedia

### Configuring the Ethernet Settings of the
 Controller

Increase the performance of your real-time controller by using line
 interrupt packet detection.

Note

1. Open NI MAX.
2. In the Packet Detection setting of the controller, select
 Line Interrupt. 
 Note If Line Interrupt is not available, select
 Polling and change the Polling Interval
 to 1 millisecond. Polling at a high rate provides high performance while introducing
 less jitter than interrupt, but increases CPU utilization.

Parent topic:

Maximizing System Performance

<!--NI_TOPIC bundle=veristand path=configure-project-file.html language=enus -->
## TOPIC 00103: Configuring a Project File

- bundle_id: `veristand`
- source_path: `configure-project-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-project-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a VeriStand project to complete tasks such as adding Tools menu items, services, alarm responses, and custom files. Launch your project in the VeriStand Editor. Depending on your goal, complete any of the following tasks. Goal Task Adding a custom Workspace Tools menu item to the project f

### Configuring a Project File

Configure a VeriStand project to complete tasks such as adding Tools
 menu items, services, alarm responses, and custom files.

1. Launch your project in the VeriStand Editor.
2. Depending on your goal, complete any of the following tasks. 
 Goal
TaskAdding
 a custom Workspace Tools menu item to the project
 file.
Add items to the Tools menu
 of the Workspace to display custom
 dialog boxes.
Adding
 custom VIs.
Add custom VIs by
 building a LabVIEW project into a source
 distribution.
Adding
 custom files to the project file.
Add custom files, such
 as documentation, to the project file.
Connecting multiple hosts to the same
 target.
Configure one or more
 host computers to communicate with the same target using
 the VeriStand Gateway.

Parent topic:

Configuring the System

Related tasks:

- Adding a Standard or Custom Tools Menu Item
- Adding Custom VIs
- Adding Custom Files
- Connecting Multiple Hosts to the Same Target

<!--NI_TOPIC bundle=veristand path=configure-run-project.html language=enus -->
## TOPIC 00104: Configuring the System

- bundle_id: `veristand`
- source_path: `configure-run-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-run-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Manage the system to fit your needs.

### Configuring the System

Manage the system to fit your needs.

1. Creating a New Project Create a new project in VeriStand to develop, prototype, and test control systems using hardware I/O and simulation models.
2. Configuring a Project File Configure a VeriStand project to complete tasks such as adding Tools menu items, services, alarm responses, and custom files.
3. Integrating and Executing Models Use models to mathematically represent real-world systems in your VeriStand project.
4. Configuring a System Definition File Modify a system definition file to complete tasks such as configuring the VeriStand engine, adding models, and creating aliases.
5. Integrating Virtual ECUs Use the VeriStand Virtual ECU Toolkit to integrate and execute virtual electronic control units (ECUs) you created using third-party software from a supported vendor.

<!--NI_TOPIC bundle=veristand path=configure-system-definition-file.html language=enus -->
## TOPIC 00105: Configuring a System Definition File

- bundle_id: `veristand`
- source_path: `configure-system-definition-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-system-definition-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify a system definition file to complete tasks such as configuring the VeriStand engine, adding models, and creating aliases. Before you begin, you must create a new system definition file. The system definition file contains the configuration settings of the VeriStand Engine, such as the system

### Configuring a System Definition File

Modify a system definition file to complete tasks such as configuring the
 VeriStand engine, adding models, and creating aliases.

Before you begin, you must create a new system
 definition file.

The system definition file contains the
 configuration settings of the VeriStand Engine, such as the system rate and the list of
 channels.

1. Open a project in VeriStand.
2. Depending on your goal, complete any of the following tasks.

- [Creating a New System Definition File](new-system-definiton.html) You can create a new system definition file without creating a new project with System Explorer .
- [Adding and Activating a System Definition File](add-system-definition.html) Reuse or add new system definition files to VeriStand projects.
- [Versioning a System Definition File](version-system-definition.html) Create and test modifications to your system definition file by duplicating the file in the VeriStand Editor.
- [Connecting to a Target System Definition](connect-target-system-definition.html) Connect to the target's deployed system definition to send and receive data.
- [Specifying a Target](specify-target.html) Select a target and designate its name, operating system, and IP address.
- [Configuring the VeriStand Engine](configure-veristand-engine.html) Control the timing of the system and the communication between the target and host computer.
- [Adding and Configuring a Procedure](add-configure-procedure.html) Set the actions the VeriStand Engine executes in response to an alarm, when called from another procedure, or as a startup procedure.
- [Adding and Configuring Alarms](add-configure-alarm.html) Notify users when a channel value is outside a specified range.
- [Adding and Configuring a Hardware Device](add-configure-hardware-device.html) Add and configure NI hardware, timing and sync devices, and custom devices.
- [Adding and Configuring a Custom Device](add-configure-custom-device.html) Add and configure third-party custom devices to execute user-defined actions, determined by LabVIEW VIs.
- [Adding and Configuring a Model](add-configure-model.html) Connect a model to other parts of the system and run the model on a hardware target.
- [Preparing a System Definition File for Virtual ECUs](ecu-preparing-system-definition-file.html) Use the VeriStand Virtual ECU Toolkit to configure your system definition file to integrate virtual ECUs you created using third-party software from a supported vendor.

Parent topic:

Configuring the System

Related tasks:

- Adding a User Channel
- Adding a Calculated Channel
- Creating an Alias
- Mapping Channels and Aliases

<!--NI_TOPIC bundle=veristand path=configure-veristand-engine.html language=enus -->
## TOPIC 00106: Configuring the VeriStand Engine

- bundle_id: `veristand`
- source_path: `configure-veristand-engine.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-veristand-engine.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Control the timing of the system and the communication between the target and host computer. Before you begin, you should understand the VeriStand Engine and the PCL execution mode steps. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.ni

### Configuring the VeriStand Engine

Control the timing of the system and the communication between the target and host
 computer.

Before you begin, you should understand the VeriStand Engine and
 the PCL execution mode
 steps.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Select Controller in the configuration tree.
4. Use the Controller Configuration page that appears to the right of
 the tree to configure the VeriStand Engine.
5. Save the system definition file.

Parent topic:

Configuring a System Definition File

Related concepts:

- VeriStand Engine
- Primary Control Loop Execution Steps

<!--NI_TOPIC bundle=veristand path=configure-watchdog-timer.html language=enus -->
## TOPIC 00107: Configuring the Watchdog Timer when Deploying to a Real-Time Target

- bundle_id: `veristand`
- source_path: `configure-watchdog-timer.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/configure-watchdog-timer.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can modify the timing watchdog that stops the execution of the VeriStand Engine if too much time elapses when you deploy a project to a real-time target. The timing watchdog is controlled by the Watchdog Timer Loop. This loop executes at a rate of 10 Hz and at a lower priority than the other loo

### Configuring the Watchdog Timer when Deploying
 to a Real-Time Target

You can modify the timing watchdog that stops the execution of the VeriStand Engine if
 too much time elapses when you deploy a project to a real-time target.

The Watchdog Timer Loop executes and resets
 the Watchdog Timer system channel every 500 milliseconds. When the Primary Control
 Loop executes, it evaluates whether the Watchdog Timer system channel reports a time
 greater than 1 second. If it does, VeriStand throws an error and stops execution of
 the VeriStand Engine.

To enable or disable watchdog functionality, complete
 the following steps:

1. Open System Explorer.
2. Select Controller from the configuration tree to display
 the Controller Configuration page.
3. Select Other Settings»Filter Watchdog Errors.

When you enable this option, VeriStand will filter errors
 reported by the timing watchdog. You can then monitor and respond to the Watchdog Timer
 system channel with custom alarms and procedures.

Parent topic:

Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=connect-hosts-to-target.html language=enus -->
## TOPIC 00108: Connecting Multiple Hosts to the Same Target

- bundle_id: `veristand`
- source_path: `connect-hosts-to-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/connect-hosts-to-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure one or more host computers to communicate with the same target using the VeriStand Gateway. Before you begin, you will need the IP address of the host that you want to run the VeriStand Gateway. Navigate to the Deployment Command Center from the VeriStand Editor by clicking the tab to the

### Connecting Multiple Hosts to the Same
 Target

Configure one or more host computers to communicate with the same target using the VeriStand Gateway.

Before you begin, you will need the IP address of
 the host that you want to run the VeriStand Gateway.

1. Navigate to the Deployment Command Center from the VeriStand Editor by clicking the tab to the right of the home icon.
2. Set the Gateway IP address of the host running the VeriStand Gateway.

The host you configured now connects to the instance
 of the VeriStand Gateway that runs on the host whose IP address you
 entered.

Parent topic:

Configuring a Project File

<!--NI_TOPIC bundle=veristand path=connect-individual-target.html language=enus -->
## TOPIC 00109: Connecting Individual Targets

- bundle_id: `veristand`
- source_path: `connect-individual-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/connect-individual-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect to an individual target to deploy the system definition in VeriStand. Use the Manage Targets tool to connect after maintenance. Connecting to a target deploys the system definition to the target. You must define the target in the system definition before connecting to a new target. Otherwise

### Connecting Individual Targets

Connect to an individual target to deploy the system definition in VeriStand. Use the
 Manage Targets tool to connect after maintenance.

Connecting to a target deploys the system
 definition to the target. You must define the target in the system definition before
 connecting to a new target. Otherwise, you must undeploy the system definition from all
 targets, define the new target, and redeploy to all targets.

1. In the VeriStand Editor, click Tool Launcher»Manage Targets.
2. In the Tool window's Manage Targets
 tab, select the target or targets that you want to connect.
3. Click Deploy. 
 Note If you are reconnecting a
 target that already has the system definition, select the target and click
 Connect.

Manage Targets

State

Parent topic:

Individual Target Management

<!--NI_TOPIC bundle=veristand path=connect-target-system-definition.html language=enus -->
## TOPIC 00110: Connecting to a Target System Definition

- bundle_id: `veristand`
- source_path: `connect-target-system-definition.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/connect-target-system-definition.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect to the target's deployed system definition to send and receive data. Before you begin, you must deploy the system definition to a real-time target. Open a project in VeriStand. In the VeriStand Editor, select Operate Connect .

### Connecting to a Target System
 Definition

Connect to the target's deployed system definition to send and receive data.

Before you begin, you must deploy the system
 definition to a real-time target.

1. Open a project in VeriStand.
2. In the VeriStand Editor, select Operate»Connect.

Parent topic:

Configuring a System Definition File

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=control-active-veristand-project.html language=enus -->
## TOPIC 00111: Control Active VeriStand Project Step

- bundle_id: `veristand`
- source_path: `control-active-veristand-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/control-active-veristand-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the active VeriStand project (.nivsprj) file. Property/Section Description Command Specifies the command that the step sends to the project: Run—Runs the project. Deploy—Deploys the system definition file associated with the project to the target. Connect—Connects the project on t

### Control Active VeriStand Project Step

Sends a command to the active VeriStand project (.nivsprj)
 file.

| Property/Section | Description |
| --- | --- |
| Command | Specifies the command that the step sends to the project: Run—Runs the project. Deploy—Deploys the system definition file associated with the project to the target. Connect—Connects the project on the host computer to a target. This option only establishes a connection to a target. It does not deploy the system definition. Disconnect—Disconnects the project from the target. This option does not stop execution of the system definition file on the target. Undeploy—Undeploys the system definition file associated with the project from the target. Undeploying the system definition file stops execution on the target. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Project Steps

<!--NI_TOPIC bundle=veristand path=control-monitor-model-execution.html language=enus -->
## TOPIC 00112: Controlling and Monitoring Model Execution

- bundle_id: `veristand`
- source_path: `control-monitor-model-execution.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/control-monitor-model-execution.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use model execution channels to interact with models. Before you begin, add a model to the system definition. Use model execution channels to accomplish tasks such as manually starting the execution of a model rather than allowing it to execute upon deployment. When you add a model to your VeriStand

### Controlling and Monitoring Model
 Execution

Use model execution channels to interact with
 models.

Before you begin, add a model to the system
 definition.

Use model execution channels to accomplish
 tasks such as manually starting the execution of a model rather than allowing it to
 execute upon deployment. When you add a model to your VeriStand project, model execution
 channels are created.

Workspace

Note

Targets

»

Controller

»

Simulation Models

»

Models

Execution

| Goal | Model execution channel |
| --- | --- |
| Run, pause, or stop the simulation | Model Command |
| Save the model state to file or restore the model state to file |  |
| View the model execution status | Model Status |
| View the time in the model | Model Time |
| View how long the current time step of the model has been running | Time Step Duration |

You can also use system
 channels to monitor the system while it is deployed and running.

Parent topic:

Integrating and Executing Models

Related concepts:

- Model Command
- Model Status
- Model Time
- Time Step Duration

Related tasks:

- Adding and Configuring a Model
- Adding and Configuring Controls and Indicators

Related reference:

- System Channels

<!--NI_TOPIC bundle=veristand path=copy-sample-fpga-vi-project.html language=enus -->
## TOPIC 00113: Copying the Sample FPGA VI and Project

- bundle_id: `veristand`
- source_path: `copy-sample-fpga-vi-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/copy-sample-fpga-vi-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a template by making a copy of a sample FPGA VI and project. To develop an FPGA VI and project, you must install matching versions of LabVIEW and VeriStand. For example, you must use LabVIEW 2020 to develop for VeriStand 2020. Browse to the <Common Data>\FPGA\Templates directory. Create a cop

### Copying the Sample FPGA VI and Project

Create a template by making a copy of a sample FPGA VI and
 project.

To develop an FPGA VI and project, you must install
 matching versions of LabVIEW and VeriStand. For example, you must use LabVIEW 2020 to
 develop for VeriStand 2020.

1. Browse to the <Common Data>\FPGA\Templates
 directory.
2. Create a copy of NI VeriStand IO PXI-7854R.lvproj in the
 same directory and open the copy in LabVIEW. 
 Note If you are using a CompactRIO FPGA target, create a copy of NI
 VeriStand FPGA IO cRIO.lvproj instead.
3. In Project Explorer, under My Computer, expand
 FPGA Target (PXI-7854R).
4. Optional: 
 To define a target other than PXI-7854R, add it to the project.
  1. Right-click My Computer and select New»Targets and Devices from the shortcut menu.
  2. In the Targets and Devices dialog box, select the New target or device.
  3. Select the device type from the list and click
 OK.
  4. In Project Explorer, under the FPGA Target
 (PXI-7854R), drag NI VeriStand FPGA DMA IO.vi to
 the new target.
  5. Under the FPGA Target (PXI-7854R) target, drag the
 DMA_WRITE FIFO and
 DMA_READ FIFO to the new target.
  6. Right-click the new target and select New»FPGA I/O to add the connectors available on the new target. 
 Note The FPGA VI
 displays broken wires from any FPGA I/O Nodes with undefined
 channels. For more information on adding I/O to a project, refer to
 the *LabVIEW FPGA Module Help*.
5. In Project Explorer, double-click NI VeriStand
 FPGA DMA IO.vi.
6. In the NI VeriStand FPGA DMA IO VI, select File»Save As.
7. Enable Substitute copy for original and click
 Continue.
8. Rename the VI and click Save.
9. In Project Explorer, save the project.

After creating your FPGA VI and project,
 customize the
 VI.

Parent topic:

Customizing an FPGA Target

Related tasks:

- Customizing an FPGA VI

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=create-alias.html language=enus -->
## TOPIC 00114: Creating an Alias

- bundle_id: `veristand`
- source_path: `create-alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-alias.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Set an alternate name for channels in a system definition file. Before you begin, you must add a model to the system definition. The VeriStand Editor will reference the alias instead of the full channel path.The alias' location in the system definition cannot be changed after the alias is created. L

### Creating an Alias

Set an alternate name for channels in a system definition file.

Before you begin, you must add a model to the
 system definition.

VeriStand Editor

Note

1. Launch your project in the VeriStand Editor.
2. Click View»System Definition.
3. Optional: 
 In the System Definition Palette, right-click
 Aliases and select New»Folder to create a sub-folder for your alias.
4. Navigate to the channel you want to create an alias for.
5. Right click the channel and select Create alias from
 selection.
6. In the Select Folder for New Aliases dialog box, select
 the location you want the alias to appear in the system definition and click
 OK.
7. Optional: 
 Configure the alias.
  1. Right click the alias you created and click
 Properties.
  2. In the Properties dialog box, enter a
 Name and
 Description.
  3. Select a new linked channel.
  4. Click OK.
8. Save the system definition file.

Mapping
 Diagram

Note

System Definition Palette

Delete

Parent topic:

Tailoring Channels

Related tasks:

- Adding and Configuring a Model

<!--NI_TOPIC bundle=veristand path=create-custom-device.html language=enus -->
## TOPIC 00115: Creating Custom Devices

- bundle_id: `veristand`
- source_path: `create-custom-device.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-custom-device.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Extend the functionality of VeriStand by packaging LabVIEW code into a form that you can add to the system definition file and deploy to a target. Before you begin, use Custom Device FAQs to decide if you have the necessary experience to create a custom device. You can also check the VeriStand Add-O

### Creating Custom Devices

Extend the functionality of VeriStand by packaging LabVIEW code into a form that you can
 add to the system definition file and deploy to a target.

Before you begin, use *Custom Device FAQs* to decide if you have the necessary
 experience to create a custom device. You can also check the
 *VeriStand Add-Ons and Custom Devices* page or
 with your hardware vendor for pre-built custom devices.

Note

You can use a custom device to execute on real-time systems and perform deterministic
 hardware-in-the-loop and real-time test procedures. With a custom device, you can
 control the configuration, execution, and user interface of a project. Custom
 devices appear in the System Explorer configuration tree.

A custom device can run either inline or in parallel (asynchronously) with the
 VeriStand Engine's Primary Control Loop, and can function as a timing and sync
 device. All custom devices communicate with the VeriStand
 Engine using configurable channels and properties.

1. Custom Device FAQs Answers to common questions about creating a custom device.
2. Custom Device Framework Follow the custom device framework to ensure your LabVIEW code interacts correctly with VeriStand.
3. Planning a Custom Device It is important to plan the major components of a custom device before writing any LabVIEW code.
4. Implementing a Custom Device Develop a custom device to fit your requirements.
5. Building a Custom Device Build a custom device for distribution to VeriStand.
6. Distributing Custom Devices Package a custom device to manually distribute it to VeriStand.
7. Overview of Runtime Configurability Runtime-configurable channels allow end users to dynamically add, change, or remove channels during system operation. This flexibility enables efficient testing and configuration without requiring system redeployment.

Parent topic:

Adding Custom Software

Related concepts:

- Custom Device FAQs
- Timing and Sync Custom Devices
- VeriStand Engine

Related information:

- VeriStand Add-Ons and Custom Devices
- Custom Device Handbook

<!--NI_TOPIC bundle=veristand path=create-fpga-configuration-file.html language=enus -->
## TOPIC 00116: Creating a Custom FPGA Configuration File

- bundle_id: `veristand`
- source_path: `create-fpga-configuration-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-fpga-configuration-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create an FPGA configuration file for the host computer. Before you begin, compile your custom bitfile. For each FPGA bitfile, VeriStand requires an FPGA configuration file. The FPGA configuration file is an XML file that the host computer uses to determine the DMA FIFO properties and how the FPGA d

### Creating a Custom FPGA Configuration
 File

Create an FPGA configuration file for the host computer.

Before you begin, compile your custom
 bitfile.

For each FPGA bitfile, VeriStand requires an FPGA configuration file. The *FPGA
 configuration file* is an XML file that the host computer uses to determine the DMA
 FIFO properties and how the FPGA device appears in System Explorer.

1. Navigate to the <Common Data>\FPGA directory and create a copy
 of an existing default configuration file.
2. Modify the FPGA configuration file using XML tags.
3. Save the file to the <Common Data>\FPGA directory using the
 .fpgaconfig file extension. 
 If you choose to save the file in a different directory, save a copy of the
 NI VeriStand FPGA DMA.xsd file, NI VeriStand FPGA
 DMA.xsl file, and the associated .lvbitx file in the
 same directory. If these files are not saved in the same directory, VeriStand cannot
 load the FPGA configuration file.Note FPGA configuration files must have at least one
 space in the file name.

Parent topic:

Customizing an FPGA Target

Related tasks:

- Compiling a Custom FPGA VI into a Bitfile

Related reference:

- FPGA Configuration File XML Tags

<!--NI_TOPIC bundle=veristand path=create-lookup-table.html language=enus -->
## TOPIC 00117: Creating a Lookup Table Scale

- bundle_id: `veristand`
- source_path: `create-lookup-table.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-lookup-table.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a Lookup Table scale in VeriStand to map pre-scaled values to scaled values using linear interpolation. VeriStand applies linear interpolation to values between the table values. This ensures that values scale proportionally. Launch your project in the VeriStand Editor. In the Project Files p

### Creating a Lookup Table Scale

Create a Lookup Table scale in VeriStand to map pre-scaled values to scaled values
 using linear interpolation.

VeriStand applies linear interpolation to
 values between the table values. This ensures that values scale
 proportionally.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Right-click Scales and select Add Scale»Lookup Table.
4. On the new scale's Lookup Table Configuration page, enter
 the scale Name and Units to
 associate with the scaled values. 
 Note The units you enter will
 supersede the units associated with the channel.
5. Enter and edit pairs of pre-scaled values and corresponding scaled values in
 the table.
6. Save the system definition file.

VeriStand clips samples that are outside the maximum and
 minimum scaled values found in the table.

Parent topic:

Scaling a Channel on Hardware Devices

<!--NI_TOPIC bundle=veristand path=create-makefile-compile-model.html language=enus -->
## TOPIC 00118: Creating a Makefile and Compiling Model Code

- bundle_id: `veristand`
- source_path: `create-makefile-compile-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-makefile-compile-model.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a makefile for the compiler and operating system your model will use. Before you begin, adapt the C template to your model code and determine which real-time (RT) operating system your RT target runs. For more information, refer to Adapting the C Template to Model Code and Real-Time Controlle

### Creating a Makefile and Compiling Model
 Code

Create a makefile for the compiler and operating system your model will
 use.

Adapting the C Template to Model Code

Real-Time Controllers and Real-Time Operating System Compatibility

For your model code to work with the
 VeriStand Model Framework, create an appropriate makefile to compile your model
 code.

1. Create a makefile (.mak) to compile the model source code. 
 For examples of makefiles designed to compile models that work with the VeriStand Model
 Framework, refer to the example .mak and .mk
 files installed in the
 <RootDrive>\VeriStand\<xxxx>\ModelInterface\custom\examples
 directory.
Note 
<RootDrive> is the drive where NI software installs and
 <xxxx> is the VeriStand version number.
2. Place your model
 code components in the same directory as the makefile.
3. Place your model
 framework components, ni_modelframework.h and
 ni_modelframework.c, in the same directory as the makefile.
4. Run the makefile to compile your model code.

Parent topic:

Using Models from C and C++

Related concepts:

- Model Code Components
- Model Framework Components

Related tasks:

- Adapting the C Template to Model Code

Related information:

- Real-Time Controllers and Real-Time Operating System
 Compatibility

<!--NI_TOPIC bundle=veristand path=create-model-header.html language=enus -->
## TOPIC 00119: Creating a Model Header File

- bundle_id: `veristand`
- source_path: `create-model-header.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-model-header.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a model.h header file that contains the type definitions for model properties and all user-visible parameters in your model. Create a header file and name it model.h. Create code in the file similar to the following code. #ifndef MODEL_h # define MODEL_h typedef struct { double a[2][2]; doubl

### Creating a Model Header File

Create a model.h header file that contains the
 type definitions for model properties and all user-visible parameters in your
 model.

1. Create a header file and name it model.h.
2. Create code in the file similar to the following code. 
 #ifndef MODEL_h
# define MODEL_h
typedef struct {
 double a[2][2];
 double b11;
 double c12;
 double idleRPM;
 double redlineRPM;
 double temperature_timeConstant;
 double temperature_roomTemp;
 double temperature_operatingTempDelta;
 double temperature_redlineTempDelta;
} Parameters;
#endif 
 The example code contains definitions for both scalar and vector double parameters.
For information about defining parameters whose data type is something other than double, refer
 to the TO DO comments in the template.c file installed by the
 VeriStand Model Framework.
3. Save the file.

After creating a model header file, adapt
 the template to your model code.

Parent topic:

Using Models from C and C++

Parent topic:

Model Code Components

Related concepts:

- Model Framework Components

Related tasks:

- Adapting the C Template to Model Code

<!--NI_TOPIC bundle=veristand path=create-polynomial-scale.html language=enus -->
## TOPIC 00120: Creating a Polynomial Scale

- bundle_id: `veristand`
- source_path: `create-polynomial-scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-polynomial-scale.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Convert values using a polynomial equation with up to ten coefficients. VeriStand requires two direction coefficients for a polynomial scale. They are a forward polynomial to convert pre-scaled values to scaled values and a reverse polynomial to convert scaled values to pre-scaled values. Launch you

### Creating a Polynomial Scale

Convert values using a polynomial equation with up to ten coefficients.

direction
 coefficients

forward

reverse

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Right-click Scales and select Add Scale»Polynomial Scale.
4. On the new scale's Polynomial Scale Configuration page,
 enter the scale Name and Units to
 associate with the scaled values. 
 Note The units you enter will
 supersede the units associated with the channel.
5. In the Coefficients drop-down menu, choose one of the
 following directions for the coefficients table. 
 DirectionDescriptionForward
 Coefficients table represents a polynomial from pre-scaled to scaled
 values.Reverse
 Coefficients table represents a polynomial from scaled to pre-scaled
 values.
6. Enter Coefficients for an order of the polynomial in the
 table control, where the coefficients are a0, a1,
 a2,...an for your polynomial scale y = a0 +
 a1x + a2x2 + … +
 anx<sup>n</sup>. 
 Note For forward coefficients,
 y is the scaled data and x
 is the raw data. For reverse coefficients, x is the
 scaled data and y is the raw data.
7. Save the system definition file.

Generate

Minimum

Maximum

OK

Parent topic:

Scaling a Channel on Hardware Devices

<!--NI_TOPIC bundle=veristand path=create-real-time-sequence.html language=enus -->
## TOPIC 00121: Creating Real-Time Sequences

- bundle_id: `veristand`
- source_path: `create-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use real-time sequences to define specific tasks for a unit under test (UUT). Before you begin, you should familiarize yourself with the Stimulus Profile Editor environment. Real-time sequences deploy to the target and can deterministically execute. Sequences test the UUT by reading from and writing

### Creating Real-Time Sequences

Use real-time sequences to define specific tasks for a unit under
 test (UUT).

Before you begin, you should familiarize yourself with the
 Stimulus Profile Editor environment.

Real-time sequences

Real-time sequences appear on the VeriStand
 Editor in the Project Files tab with the file
 extension .nivsseq. A real-time sequence cannot execute on its own
 and must belong to a stimulus profile.

1. In the VeriStand Editor, click Tool Launcher»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click File»New»Real-Time Sequence. 
 The sequence organizes your code into the Setup,
 Main, and Clean Up blocks. The
 Primitives palette contains programming building
 blocks, such as statements and variables, you can use to define the task the
 real-time sequence completes.
3. Create the variables your sequence code can access.
  1. Drag variables from the Primitives palette to one
 of the following sections of the Variables
 pane. 
 Section
 DescriptionReturn Variable
 The value the real-time sequence returns after it
 executes.
 Parameters
 The inputs and outputs that the sequence accepts
 when called and can pass out to other sequences or
 the stimulus profile.
 Local Variables
 Variables you want to access from statements
 within the current sequence.
 Channel References
 References that allow you to read/write system
 definition channels directly from a real-time
 sequence. Note Channel references bind to specific
 system definition channels when added to a
 real-time sequence. The sequence that contains
 them is bound to that system definition file. If
 you want to write a sequence that you can reuse
 across multiple system definition files, use
 Parameters.
 Note Use Double or Boolean primitives to create parameters that you
 want to map to system definition channels. All channels in VeriStand
 are 64-bit floating point numbers (doubles), but many can also
 accept Boolean values.
  2. To add channel references, right-click Channel Referencesand click Insert Channels.
4. Map parameters to system definition channels.
  1. Select a parameter in the Variables pane.
  2. In the Property Browser, give the parameter a
 unique Identifier.
  3. Next to Default Assignment, click
 Browse and navigate to the appropriate
 channel or click View aliases in the window to
 select a channel by its alias.
5. If you want to use Local Variables in statements or
 expressions, use the Property Browser to configure a unique
 Identifier and a Default Value
 for those variables
6. If you want to call another sequence from an expression in the current
 sequence, add the new sequence to the References pane. 
 You can drag variables from the Variables pane or
 sequences from the Sequences palette directly to the
 sequence code to automatically create expressions that act on those elements. In
 the case of sequences, VeriStand also creates references to the sequence.
7. Use expressions, structures, and other primitives to build the sequence code. 
 Select any item in the sequence code to configure it in the Property
 Browser.
8. Click Compile.
  1. Resolve any Warnings and Errors. 
 Note A sequence can run
 with warnings, but not errors. You can save the profile and resolve
 errors later.
9. Save the sequence.

After creating the real-time sequence, add a call for the real-time sequence to a
 stimulus profile. A sequence cannot execute independently of a stimulus profile. Run
 the stimulus profile to run the sequence.

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

<!--NI_TOPIC bundle=veristand path=create-stimulus-profile-editor-layout.html language=enus -->
## TOPIC 00122: Creating a Stimulus Profile Editor Layout

- bundle_id: `veristand`
- source_path: `create-stimulus-profile-editor-layout.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-stimulus-profile-editor-layout.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Customize the individual sections of the Stimulus Profile Editor environment and save that layout for later use. Before you begin, you should familiarize yourself with the Stimulus Profile Editor environment. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Prof

### Creating a Stimulus Profile Editor
 Layout

Customize the individual sections of the Stimulus Profile Editor
 environment and save that layout for later use.

Before you begin, you should familiarize yourself with the
 Stimulus Profile Editor environment.

1. In the VeriStand Editor, click Tool Launcher»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, modify the
 layout by dragging sections to other parts of the editor,
 close sections, or use the View tab
 to show or hide a section.
3. In the View tab, click Save
 Layout.
4. Enter a Layout File Name and click
 OK. 
 Note You can save as many layouts as you need, but you
 cannot rename or delete a layout after you save
 it.

View Tab

Available
 Layouts

Parent topic:

Navigating the Stimulus Profile Editor Environment

Related tasks:

- Navigating the Stimulus Profile Editor Environment

<!--NI_TOPIC bundle=veristand path=create-stimulus-profile.html language=enus -->
## TOPIC 00123: Creating Stimulus Profiles

- bundle_id: `veristand`
- source_path: `create-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use stimulus profiles to act as the test executive that defines the stimuli to apply to a unit under test (UUT). Before you begin, you should familiarize yourself with the Stimulus Profile Editor environment. In real-time test, a stimulus is a physical or logical input that incites a reaction from t

### Creating Stimulus Profiles

Use stimulus profiles to act as the test executive that defines
 the stimuli to apply to a unit under test (UUT).

Before you begin, you should familiarize yourself with the
 Stimulus Profile Editor environment.

stimulus

A *stimulus profile* contains specific
 tasks, called real-time sequences, that deploy to the UUT and execute in real-time.
 Stimulus profiles execute on the host computer and control some actions of the
 VeriStand environment. For example, stimulus profiles can open and close projects
 and user interface windows and log the results of test scenarios to TDMS files.

Stimulus profiles appear on the VeriStand Editor in the
 Project Files tab with the file extension
 .nivsstimprof. A single VeriStand project can contain multiple
 stimulus profiles that define different test scenarios. You can execute multiple
 stimulus profiles concurrently, and each stimulus profile can contain multiple
 real-time sequences.

1. In the VeriStand Editor, click Tool Launcher»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click File»New»Stimulus Profile. 
 The profile organizes your code into the Setup,
 Main, and Clean Up blocks.
3. Drag steps from the Steps palette to the appropriate block
 of the stimulus profile. 
 For example, you might launch a user interface as part of your
 Setup code and close the user interface as part of
 your Clean Up code. The Main block
 typically contains calls to real-time sequences, which are programs that define
 specific tasks to execute on the UUT. This block might also contain steps that
 configure data logging to TDMS.
4. For each step you add, click the step in the stimulus profile code and use the
 Property Browser to configure the step.
5. Click Compile.
  1. Resolve any Warnings and Errors. 
 Note A stimulus profile
 can run with warnings, but not errors. You can save the profile and
 resolve errors later.
6. Save the stimulus profile.

After you configure and save the stimulus profile and any
 real-time sequences it calls, you can run the profile. Deploy its associated
 system definition to run the stimulus profile.

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=create-test-scenarios.html language=enus -->
## TOPIC 00124: Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

- bundle_id: `veristand`
- source_path: `create-test-scenarios.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-test-scenarios.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the VeriStand Stimulus Profile Editor to create specific test scenarios for use in your real-time test applications. In addition to using the Stimulus Profile Editor environment, you can use the LabVIEW VIs on the Stimulus Profile palette in LabVIEW to execute and control stimulus profile and re

### Creating Real-Time Test Scenarios with
 Stimulus Profiles and Real-Time Test Sequences

Use the VeriStand Stimulus Profile Editor to create specific test
 scenarios for use in your real-time test applications.

Stimulus Profile

<LabVIEW>\examples\VeriStand\API\Execution
 API\Sequences

1. Create a stimulus profile—Use stimulus profiles to act as the test executive that defines
 the stimuli to apply to a unit under test (UUT).
2. Create a real-time sequence—Use real-time sequences to define specific tasks for a unit under
 test (UUT).
3. View test results—Enable the Stimulus Profile Editor to
 automatically open stimulus profile test results.
4. Log-real-time test data—Use stimulus profiles to log real-time test data to the host computer
 while a test executes on a target.
5. Use
 stimulus profile arguments to communicate with the
 VeriStand Editor—Send commands to the VeriStand Editor through a
 stimulus profile to specify a VeriStand project, a system definition, VeriStand Gateway
 IP address, or connect to a target from the system definition.

If you want to script your test sequences in Python, you can use the VeriStand Python Integration
 Package as an alternative to the Stimulus Profile Editor. This
 open-source package allows you to execute Python scripts as if they
 were VeriStand real-time sequences. To learn more about this
 feature, view the *VeriStand Python Documentation*.

Parent topic:

Running Tests

Related tasks:

- Navigating the Stimulus Profile Editor Environment
- Creating Stimulus Profiles
- Creating Real-Time Sequences
- Viewing Stimulus Profile Test Results
- Logging Real-Time Test Data with the Stimulus Profile Editor
- Communicating with the VeriStand Editor Using Stimulus Profile Arguments

Related information:

- VeriStand Python Integration Package
- VeriStand Python Documentation

<!--NI_TOPIC bundle=veristand path=create-thermocouple-scale.html language=enus -->
## TOPIC 00125: Creating a Thermocouple Scale

- bundle_id: `veristand`
- source_path: `create-thermocouple-scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/create-thermocouple-scale.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a thermocouple scale to convert temperature values to Kelvin, Celsius, Fahrenheit, or Rankine using cold-junction compensation. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Ri

### Creating a Thermocouple Scale

Configure a thermocouple scale to convert temperature values to Kelvin, Celsius,
 Fahrenheit, or Rankine using cold-junction compensation.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Right-click Scales and select Add Scale»Thermocouple Scale.
4. On the new scale's Thermocouple Scale Configuration page,
 enter the scale Name. 
 Note The units you enter will
 supersede the units associated with the channel.
5. Select the Thermocouple Type,Temperature
 Units, CJC Type (cold-junction
 compensation device), and CJC Sensor locations.
6. Save the system definition file.

Parent topic:

Scaling a Channel on Hardware Devices

<!--NI_TOPIC bundle=veristand path=creating-configuring-ecu-network-cluster.html language=enus -->
## TOPIC 00126: Creating and Configuring an ECU Network Cluster

- bundle_id: `veristand`
- source_path: `creating-configuring-ecu-network-cluster.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/creating-configuring-ecu-network-cluster.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create an ECU network cluster to connect your virtual ECUs and ECUs. Before you begin, add and configure one or more virtual ECUs. On the Mapping Diagram on the Palette, click Software ECU Network Cluster and drop the node on the diagram. VeriStand opens a dialog box. In the dialog box, select an ex

### Creating and Configuring an ECU Network Cluster

Create an ECU network cluster to connect your virtual ECUs and ECUs.

Before you begin, add and configure one or
 more virtual ECUs.

1. On the Mapping Diagram on the
 Palette, click Software»ECU Network Cluster and drop the node on the diagram. 
 VeriStand opens a dialog box.
2. In the dialog box, select an existing ECU network cluster or create a new one
 by specifying a name in File name.
3. Click Open.
4. Navigate to the Item tab in the Configuration
 pane and verify or configure the settings.
5. In the Behavior section, set the
 Initial state of the virtual ECU to
 Running or Paused. 
 Note To change the values of ECU
 network cluster parameters before the first time step, set the
 Initial state to Paused.
6. Set the Decimation of the ECU network cluster
 rate.
7. Select the Model processor to
 Automatic or Manual.
8. In the ECU network cluster configuration section, specify
 the Cluster name. You can find the name of the cluster in
 the following source code files for the virtual ECU. 
 Table 3.Source code files that contain the name of the cluster for the
 Virtual ECUProtocol type
 File name
 ParameterCAN
 Can_PBcfg.c
 CanController.SilverCanSvbConfig.SilverCanSvbConfigNetworkName
 LIN
 Lin_PBcfg.c
 LinController.SilverLinSvbConfig.SilverLinSvbConfigNetworkName
 Ethernet
 Eth_PBcfg.c
 EthController.SilverEthSvbConfig.SilverEthSvbConfigNetworkName
9. Set the Time step. The time step determines how
 frequently VeriStand transmits information between the virtual network and real
 network. Use a step size that is at least as fast as the fastest virtual ECU
 Functional Mockup Unit (FMU).
10. Select the Protocol you want to use.
  1. If you are using CAN protocol, specify the I/O
 mode and Baud rate.
  2. If you are using LIN protocol, specify the Baud
 rate.
11. Set the XNET interface. The XNET interface is the
 connector on NI XNET hardware that connects the virtual network to the real
 network. 
 Tip Use MAX to view
 your available NI-XNET hardware, including all devices and
 interfaces.
12. Select the Vendor that you used to build the virtual
 ECUs in the network cluster.
13. In the Virtual ECUs field, list the names of the virtual
 ECUs which are part of the ECU network cluster as a comma-separated list.
14. If you are using CAN protocol, select the Transceiver
 type from the following options. 
 OptionDescriptionAutoHigh-Speed
 Enables the High-Speed transceiver. This transceiver supports baud
 rates of 40.00 kBaud to 1.00 MBaud. When using a High-Speed transceiver,
 you can also communicate with a CAN FD bus. Refer to *NI-XNET
 Hardware Overview* to determine which CAN FD baud rates are
 supported.Low-Speed/Fault-Tolerant
 Enables the Low-Speed/Fault-Tolerant transceiver. This transceiver
 supports baud rates of 40.00 kBaud to 125.00 kBaud.Single Wire
 Enables the Single Wire transceiver. This transceiver supports baud
 rates of 33.33 kBaud and 83.33 kBaud.External
 Allows you to use an external transceiver to connect to your CAN
 bus. Refer to the XNET Session *Interface:CAN:External Transceiver
 Config* property for more information.Disconnect
 Allows you to disconnect the CAN controller chip from the connector.
 You can use this value when you physically change the external
 transceiver.
15. If you are using CAN protocol, select the CAN FD ISO
 Mode from the following options. This setting is valid only when
 the I/O mode is set to CAN-FD-BRS. 
 OptionDescriptionISO
 Indicates you are using the ISO CAN FD 11898-1:2015
 protocol.Non-ISO
 Indicates you are using the CAN FD 1.0 protocol.Legacy ISO
 Indicates you need to communicate with a legacy application. This
 mode behaves like the Non-ISO mode but can communicate with ISO CAN FD
 devices. Note Use this
 mode only for compatibility with existing
 applications. 
 Note Two ports using different
 standards cannot communicate with each other.
16. Save the system definition file.

After setting up the ECU network cluster,
 deploy the system definition file to the real-time target.

Parent topic:

Preparing a System Definition File for Virtual ECUs

<!--NI_TOPIC bundle=veristand path=csv-file-format-example.html language=enus -->
## TOPIC 00127: CSV File Formatting Examples

- bundle_id: `veristand`
- source_path: `csv-file-format-example.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/csv-file-format-example.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Format CSV files to run as real-time sequences or subroutines within a sequence in a stimulus profile. The following table displays examples of CSV files based on the goal. The formatting of the CSV file depends on whether you want to stimulate, fault, and/or evaluate a channel. Goal Example Stimula

### CSV File Formatting Examples

Format CSV files to run as real-time sequences or subroutines within a sequence in a
 stimulus profile.

The following table displays examples of CSV files based on the goal. The formatting
 of the CSV file depends on whether you want to stimulate, fault, and/or evaluate a
 channel.

| Goal | Example |
| --- | --- |
| Stimulating a Channel | The following CSV file stimulates a channel with the alias channelX by updating the value of the channel every 100 milliseconds. timestamp,channelX 0,0 100,5 200,10 300,20 400,30 500,40 |
| Stimulating Multiple Channels | The following CSV file stimulates two channels, channelX and channelY, by updating the channel values every 100 milliseconds. timestamp,channelX,channelY 0,0,-50.5 100,5,-49 200,10,-46 300,20,-40 400,30,-28 500,40,-4 |
| Faulting a Channel | The following CSV file alternates between faulting and clearing a fault on channelX every 100 milliseconds, and forces the value of channelX to 100 whenever it faults the channel. timestamp,#FLT_STATE#channelX,#FLT_VALUE#channelX 0,0,0 100,1,100 200,0,0 300,1,100 400,0,0 500,1,100 |
| Evaluating a Channel | The following CSV file tests channelX for an expected value, and updates the expected value every 100 milliseconds. In this example, the actual value of channelX can be within .05 of the expected value for a passing test, but no delay in reaching the value is allowed. timestamp,#EXP(.05;.05;0)#channelX 0,0 100,1 200,0 300,-1 400,0 500,1 Note Because you can specify delay on evaluation tasks, multiple evaluations can run at different intervals. If you evaluate multiple channels, VeriStand runs each channel evaluation in a separate, parallel task. |
| Stimulating, Faulting, and Evaluating a Channel | The following CSV file stimulates channelX, faults channelY, and evaluates channelZ every 100 milliseconds. timestamp,channelX,#FLT_STATE#channelY,#FLT_VALUE#channelY,#EXP(.05;.05;50)#channelZ 0,0,0,0,0 100,1,1,100,10 200,0,0,0,0 300,-1,1,100,-10 400,0,0,0,0 500,1,1,100,10 Note VeriStand runs the channel evaluation in one task and the faulting and stimulation in a separate, parallel task. |

Parent topic:

Using CSV Files as Real-Time Sequences

Related tasks:

- Using CSV Files as Real-Time Sequences
- Creating an Alias

<!--NI_TOPIC bundle=veristand path=csv-stimulate-fault-evaluate-channels.html language=enus -->
## TOPIC 00128: Using CSV Files as Real-Time Sequences

- bundle_id: `veristand`
- source_path: `csv-stimulate-fault-evaluate-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/csv-stimulate-fault-evaluate-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Comma Separated Values (.csv) files within stimulus profiles to stimulate, fault, and evaluate channels. Format your CSV file. Call the CSV file from a stimulus profile file as a real-time sequence or by reference from another real-time sequence file. CSV files that you call as real-time sequenc

### Using CSV Files as Real-Time Sequences

Use Comma Separated Values (.csv) files within stimulus profiles to
 stimulate, fault, and evaluate channels.

1. Format your CSV
 file.
2. Call the CSV file from a stimulus profile file as a real-time sequence or by reference from
 another real-time sequence file.

false

true

Parent topic:

Creating Real-Time Sequences

Related concepts:

- CSV File Formatting for Stimulus Profiles

Related tasks:

- Creating Real-Time Sequences
- Calling a Real-Time Sequence from Another Sequence

<!--NI_TOPIC bundle=veristand path=custom-device-action-vi-automation.html language=enus -->
## TOPIC 00129: Automating Responses to User Actions with Action VIs

- bundle_id: `veristand`
- source_path: `custom-device-action-vi-automation.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-action-vi-automation.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use action VI templates with the custom device XML file to automate responses to user actions. Before you begin, you should understand the action VI templates and the custom device XML file. Action VIs are dynamically called VIs that execute when a user performs a specific action in a custom device.

### Automating Responses to User Actions with
 Action VIs

Use action VI templates with the custom device XML file to automate
 responses to user actions.

Before you begin, you should understand the action VI
 templates and the custom device XML file.

Action VIs

1. Create a new VI from an action VI template.
  1. From the custom device LabVIEW project, navigate to Custom Device API.lvlib»Templates»Action VI.
  2. Right-click the action VI you want to customize and select
 New from Template.
  3. Save the new action VI to the same directory as the custom device
 project.
2. Declare the action VI in the Custom Device XML. 
 You declare the action VI within the declaration for a specific page. The
 action VI executes when a user performs the triggering action on that page.
  1. From the custom device LabVIEW project, open the custom device XML
 file.
  2. Locate the <Page> tags for the custom device
 item from which you want to call the action VI.
  3. Declare the action VI anywhere beneath the
 <Item2Launch> tag. 
 The following image gives an example of how to declare the action
 VI. 
[IMAGE alt='image' src='GUID-B92D06F9-D75C-4FAA-8EAD-FC0FF491CA52-a5.jpg']
3. Customize the action VI to meet your needs.
4. Add the action VI to the Configuration build specification of the custom
 device.
  1. From the custom device LabVIEW project, double-click Build Specifications»Configuration.
  2. Select Source Files from the Category menu.
  3. Under the Project Files menu, locate the action VI and move it to the
 Always Included list.
  4. In the Category menu, select Source File
 Settings.
  5. In the Project Files menu, select the action VI.
  6. From the Destination pull-down menu, select the Configuration
 .llb file.
  7. Click OK to save the new settings.

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-action-vi-template.html language=enus -->
## TOPIC 00130: Action VI Templates

- bundle_id: `veristand`
- source_path: `custom-device-action-vi-template.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-action-vi-template.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand contains eight action VI templates that are triggered by different actions. The following table displays the action VI templates provided by VeriStand in the Custom Device API library. Action VI Description ActionVIOnLoad Executes when VeriStand loads a custom device item into memory. This

### Action VI Templates

VeriStand contains eight action VI templates that are triggered by different actions.

| Action VI | Description |
| --- | --- |
| ActionVIOnLoad | Executes when VeriStand loads a custom device item into memory. This template helps create action VIs that launch background processes. For example, if your custom device requires large amounts of data, you can customize this template to start a daemon that runs processes or gathers data in the background. |
| ActionVIOnDeleteRequest | Executes when a user tries to delete an item from the custom device. This template helps create action VIs that prevent a user from deleting a custom device item or warn a user of the implications of deleting a custom device item. The template has the following unique parameters. Item Ref—The reference to the custom device item whose XML declaration calls this action VI. Refs that are about to get deleted—A 1D array of references to the items to be deleted. However, the 1D array will only contain one reference, as users can only delete one item at a time in the System Explorer window. Discard reason—An output you can use to capture the user's reason for deleting the item. Discard delete request?—Allows you to discard the delete request. After the action VI finishes executing, VeriStand will evaluate this output to determine whether or not to delete the item. If True, VeriStand will not delete the item. If False, VeriStand will delete the item. Additional items to delete—An array of references to additional items you want to delete. For example, if other custom device items depend on the item the user wants to delete, you can use this output to automatically delete those items. |
| ActionVIOnDelete | Executes after a user deletes an item from the custom device. You can customize this template to alert users which channel mappings break when they delete the custom device item. You can also customize this template to reconfigure hardware. For example, if the user deletes a page that specifies custom configuration data for your hardware, you can customize the template to return the configuration to default settings. |
| ActionVIOnSystemShutdown | Executes when System Explorer closes. You can customize this template to close hardware connections or to close daemons you launch from an ActionVIOnLoad action VI. The template has the following unique parameters. Device Item Ref—Reference to the custom device item whose XML declaration calls this action VI. Unload SDF?—Indicates whether or not the system definition file was unloaded. Unload SDF? is always True. Saved?—Indicates whether or not a user saved the system definition file before closing System Explorer. Path—Path on disk to the system definition file. System Explorer Shutdown?—Indicates whether or not System Explorer closed. This parameter is always True. |
| ActionVIOnSave | Executes when a user saves the system definition file. For example, you can customize this template to log each time the custom device is saved. |
| ActionVIOnDownload | Executes when a user deploys the system definition file containing the custom device to a real-time target. This action VI does not execute if a user deploys the system definition to a Windows target. This template helps create action VIs that finalize the target configuration after you deploy the system definition. You can also customize this template to deploy any additional files or dependencies your custom device requires. For example, if your custom device reads and writes to shared variables, you can deploy those variables. The template has the following unique parameters. Device Item Ref in—Reference to the custom device item whose XML declaration calls this action VI. ftp session—Open FTP session used to download the system definition to the target. You can use this open session to move additional files to the target. System Definition Dir—Path to the system definition file on disk. IP Address—IP address of the target. ftp session out—Open FTP session used to download the system definition file to the target. |
| ActionVIOnPaste | Executes when a user pastes a custom device item. This template helps create action VIs that check channel properties. For example, if the user pastes a page that configures a target, you can create an action VI to ensure that the new page does not attempt to reconfigure the target. You can also customize this template to prompt a user to enter new values for the pasted item. For example, if a user pastes a page that will conflict with existing pages, you can prompt the user to enter new values for the page. The template has the following unique parameters. Ptr in—Reference to the custom device item whose XML declaration calls this action VI. Parent—Reference to the parent of the custom device item whose XML declaration calls this action VI. All Ptrs—Array of references to the items the user pasted. You can only select one item to copy. This array only contains one reference that matches the Ptr in reference. |
| ActionVIOnCompile | Executes when VeriStand compiles the system definition file. Note If you deploy the system definition, then undeploy it, and then redeploy it without making changes, this template does not execute because the system definition does not recompile. You can customize this template to finish configuring your hardware. The system definition file compiles when a user deploys the system definition, so you can configure your hardware based on the final settings from the system definition. You can also customize the template to quickly gather host-side settings. For example, often the custom device RT Engine VI uses properties set in the system definition. You can customize this template to read the values on the host side, which is much faster than reading them from the real-time target. You can then gather the properties into a single cluster, convert that cluster to a data variant, and write the variant as a single item property. |

Parent topic:

Automating Responses to User Actions with Action VIs

<!--NI_TOPIC bundle=veristand path=custom-device-add-channel-waveforms.html language=enus -->
## TOPIC 00131: Adding Custom Device Channels and Waveforms

- bundle_id: `veristand`
- source_path: `custom-device-add-channel-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-add-channel-waveforms.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add channels and waveforms to a custom device by using the appropriate VI within a Custom Device Library VI that runs on the host computer. Before you begin, you should understand custom device channels and waveforms. Typically, you add channels in the Initialization VI so they appear when an operat

### Adding Custom Device Channels and
 Waveforms

Add channels and waveforms to a custom device by using the
 appropriate VI within a Custom Device Library VI that runs on the host
 computer.

Before you begin, you should understand custom device channels and waveforms.

Note

1. Open a Custom Device Library VI that runs on the host
 computer.
2. Based on the data exchange mechanism you want the custom device
 to use, add a VI from the Configurations VIs palette. 
 Mechanism
VI TypeChannel
Add Custom Device Channel
 VI
Waveform
Add Custom Device Waveform
 VI
3. Modify the following code in the VI. 
 Note The following image displays the Add Custom Device
 Channel VI customized to add two input channels and
 one output channel. The customizing process for the
 Add Custom Device Waveform VI is very
 similar.
 
[IMAGE alt='image' src='GUID-30CBB6D8-B7C3-4227-A38B-4DDA431808E4-a5.gif'] 

1
Device Item Ref in—Provides
 each instance of the Add Custom Device Channel VI
 with the reference to the custom device to which
 to add the channels.
2
Channel cluster—Defines the
 various properties of the channel, including the
 type, units, default value, faultability, and
 scalability of the channel. In this example, two
 input channels and one output channel will be
 created.
3
Channel Name—Specifies the
 name of the new channel. In this example, the
 channel names are A, B, and A+B. Each channel must
 have a unique name. If the name you specify
 already exists, this VI overwrites the existing
 channel settings. 
 With this configuration, the custom device will create
 three channels, A, B, and A+B, when you add it to a system
 definition.

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-add-error-code.html language=enus -->
## TOPIC 00132: Adding Custom Error Codes in a Custom Device

- bundle_id: `veristand`
- source_path: `custom-device-add-error-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-add-error-code.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Build custom error codes for your custom device using the General Error Handler VI or the Error Code File Editor. Create the error code file in LabVIEW. Move the error code file to the VeriStand errors folder located at <Base>\National Instruments\Shared\Errors\English. If VeriStand encounters your

### Adding Custom Error Codes in a Custom
 Device

Build custom error codes for your custom device using the General
 Error Handler VI or the Error Code File Editor.

1. Create the error code file in LabVIEW.
2. Move the error code file to the VeriStand errors folder located at <Base>\National Instruments\Shared\Errors\English.

If VeriStand encounters your custom error code, it will display the message you defined
 in the file.

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-add-glyph-shortcut-menu-toolbar-button.html language=enus -->
## TOPIC 00133: Adding Custom Glyphs, Shortcut Menus, and Toolbar Buttons

- bundle_id: `veristand`
- source_path: `custom-device-add-glyph-shortcut-menu-toolbar-button.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-add-glyph-shortcut-menu-toolbar-button.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use elements in the Custom Device XML to configure custom user interface components, such as glyphs, toolbar buttons, and shortcut menus. Before you begin, you should understand the custom device XML and the custom device specific XML tags. Open the LabVIEW project for your custom device. In Project

### Adding Custom Glyphs, Shortcut Menus, and
 Toolbar Buttons

Use elements in the Custom Device XML to configure custom user
 interface components, such as glyphs, toolbar buttons, and shortcut
 menus.

Before you begin, you should understand the custom device XML and the custom device specific XML tags.

1. Open the LabVIEW project for your custom device.
2. In Project Explorer, browse to My Computer»Custom Device
 <Name>.xml and open the XML file of your custom
 device.
3. Depending on your goal, complete any of the following tasks to
 configure the user interface of your custom device. 
 Goal
Description
TaskAdding glyphs
A *glyph* is the icon that
 appears next to an item System
 Explorer.
Within the <Page> tags for
 an item, you can use the
 <Glyph> tag to configure a
 custom glyph to display for the item. You can use
 any PNG file as a glyph.
A collection of glyphs that install with
 VeriStand is available in the
 <Application Data>\System
 Explorer\Glyphs directory.
Adding toolbar buttons
A *Toolbar button* appears in
 the toolbar of System
 Explorer. These buttons only appear
 when displaying the configuration page associated
 with the button.
Within the <Page> tags for
 an item, you can use the
 <ButtonList> tag to configure
 the toolbar buttons that appear with the item's
 configuration page. Each
 <Button> must include a unique
 <ID> string that identifies
 the button. The toolbar button displays by
 default.
However, in each page VI, you can use the
 Disable Dynamic Button VI and the Enable Dynamic
 Button VI to dynamically disable and enable a
 button for that page based on its unique ID. These
 VIs are useful when you want the toolbar button to
 appear only when certain conditions are true.
These VIs are located in the
 labview\vi.lib\NI VeriStand\Custom
 Device APIdirectory.
The following is an example framework you can
 use to implement a toolbar button. 
[IMAGE alt='image' src='GUID-54835733-0172-4906-AB85-52BF2BBCD19C-a5.gif']
Adding shortcut menus
A *shortcut menu* for an item is the
 menu that appears when you right-click the item in
 *System Explorer*.
Within the <Page> tags for
 an item, you can use the
 <RunTimeMenu> tag to configure
 the shortcut menu for the item. Each
 <MenuItem> you add under
 <RunTimeMenu> includes an
 <Item2Launch> section that
 specifies a VI to run when an operator selects the
 menu item.
The Custom Device API library includes a
 template for this VI, RunTimeMenu Custom Item 2
 Launch.vit, in the labview\vi.lib\NI
 VeriStand\Custom Device API directory.
The following is an example framework you can
 use to implement a shortcut menu. 
[IMAGE alt='image' src='GUID-03DBF393-BC8B-4162-9EF8-047E8F54161E-a5.gif']
4. Save and close the XML file.

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-add-item-properties.html language=enus -->
## TOPIC 00134: Adding Custom Device Item Properties

- bundle_id: `veristand`
- source_path: `custom-device-add-item-properties.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-add-item-properties.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use VIs on the Item Properties palette to get and set properties of custom device items. Before you begin, you should understand custom device item properties. While you can call Item Properties VIs from any VI within the custom device, you should call them from VIs that run before the engine is dep

### Adding Custom Device Item Properties

Use VIs on the Item Properties palette to get and set properties of
 custom device items.

Before you begin, you should understand custom device item
 properties.

While you can call Item Properties VIs from any VI within the custom device, you should
 call them from VIs that run before the engine is deployed, such as in a page VI or your
 Initialization VI. You cannot pass property information from the configuration to the engine
 after the engine is deployed.

The following image displays the hierarchy of a custom device modified to set and read
 properties.

[IMAGE alt='image' src='GUID-2F5FA21F-42EB-4449-8DCF-F0C5460F7A16-a5.gif']

- When a user selects a channel from the system definition, the configuration page for
 that channel initializes Filter Setting and Input Range. However, if the properties
 already have set values, the configuration page displays the values of the properties.
- The configuration page allows operators to enter new values for each property.
- When an operator deploys the custom device, the RT Driver VI gets the value for each
 item property so the RT Driver VI can use the values.

To implement this functionality, you have to modify your custom device code.

1. Modify the following code to set up the Initialization case to initialize the item
 properties Filter Setting and Input Range in a page VI for a selected channel. 
 When an operator selects a custom device channel in System
 Explorer, the page VI associated with that channel or section runs. The
 page VI then uses a reference to the selected channel or section to get and set the
 properties for that channel. If the properties are already initialized, the page VI gets
 the current values for the properties and displays them on the front panel.
 
[IMAGE alt='image' src='GUID-745BCE89-AE3E-412F-AB9B-D394E15EB987-a5.gif'] 

1
Node Ptr—Reference to the channel an operator selects in
 System Explorer.
2
Get Item Property VIs—Gets the values for the Filter Setting
 and Input Range properties of the selected channel and then populates the
 controls on the configuration page with that data. If a value does not already
 exist, Get Item Property VI initializes the property with Default Value. In
 this example, the default values are False for Filter Setting
 and 1 for Input Range.Note The names of properties are
 case sensitive strings. To reduce the risk of error, consider storing
 property names as global variables.
3
Get Item Description VI and Get Item Data
 VI—Get the description and name of the channel or section, and send that
 information to indicators on the front panel. These VIs are part of the
 template page VI.
2. Modify the following code to set up the cases that detect a change of an item property
 value in a page VI. 
 The page VI contains two Value Change event cases, one for the Input Range control and
 one for the Filter Setting control. If an operator changes the value of the item
 property using one of these controls, the page VI detects the change in value and the
 Set Item Property VI sets the new value. The following table shows these cases.
Control
Basic Architecture
PurposeInput Range
[IMAGE alt='image' src='GUID-CF0DCF97-F0F0-4CD3-BDBD-C1ECF5C8EE58-a5.gif']
Determine the appropriate range of each channel.
Filter Setting
[IMAGE alt='image' src='GUID-56D26569-9842-4129-BDB2-AB1E58F0F7C4-a5.gif']
Determines whether to filter each channel
3. Modify the following code to set up a RT Driver VI to get the property values of Filter
 Setting and Input Range for each channel. 
 [IMAGE alt='image' src='GUID-E403D5D8-1398-49AA-8A0A-B2D239B028D5-a5.gif'] 

1
Device Reference and Get Item Property VI—References custom
 device and gets the Device Name item property to pass to the Get Item
 Reference by Name VI.
2
Get Item Reference by Name VI—Searches under the custom
 device for the Hardware Inputs section and outputs the reference to that
 section.
3
Get Item Children VI—Returns an array containing all the
 references for all of the children, or items, under the Hardware Inputs
 section. In the hierarchy, channels ADDataFromCh<1...8> appear under
 Hardware Inputs, so the Get Item Children VI returns an array of references
 for the channels.
4
Get Item Property VIs—Returns the values for the
 Filter Setting and Input Range properties
 of each channel using the array of channel references.

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-add-page.html language=enus -->
## TOPIC 00135: Adding Custom Device Pages

- bundle_id: `veristand`
- source_path: `custom-device-add-page.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-add-page.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Add pages to a custom device by creating the extra page VIs and GUIDs, adding the extra pages to the custom device build specifications, and defining the pages in the Custom Device XML file. Before you begin, you should understand custom device pages. Create a page VI with the required reference usi

### Adding Custom Device Pages

Add pages to a custom device by creating the extra page VIs and GUIDs,
 adding the extra pages to the custom device build specifications, and defining the pages
 in the Custom Device XML file.

Before you begin, you
 should understand custom device pages.

1. Create a page VI with the required reference
 using the template VI included in the Custom
 Device API library.
  1. Open the LabVIEW project for your custom
 device.
  2. In Project Explorer,
 browse to My Computer»Custom Device API.lvlib»Templates»Subpanel Page VI»Page Template.vit.
  3. Right-click Page
 Template.vit and select New
 from Template.
  4. From the front panel of the new VI, save the
 VI in the folder containing the other VIs for your
 custom device, such as RT Driver VI and Main Page
 VI.
  5. Close the VI.
  6. In Project Explorer,
 drag the new VI to the Custom Device library.
2. Declare the page in the XML file of the custom
 device. 
 
 Note Every item with a unique page VI must have a page entry in the Custom Device XML
 file and a unique GUID. However, items with different GUIDs can reference the same page
 VI. If you want to create several configuration pages that are only slightly different,
 you can use the same page VI for each item by configuring the VI to check the associated
 item GUID at run time. For example, you can add a Case structure to the page VI with a
 case for each GUID.
  1. Open the LabVIEW project for your custom
 device.
  2. In Project Explorer,
 browse to My Computer»Custom Device <Name>.xml and open the XML file of your
 custom device.
  3. Under the Pages section of
 the XML file, locate the Page
 section for the main page of your custom
 device. 
 The declarations for the main page should be
 the first listed under the Pages
 section. The name of the main page corresponds to
 the name of the custom device.
  4. Copy the information between the Page tags,
 including the <Page> and
 </Page> declarations, and
 paste it between the <Pages>
 and </Pages>
 declarations.
  5. Replace the information between the
 <eng> and
 <loc> decelerations with the
 name of the new page. 
 For example, if you saved your page VI as
 ExtraPage.vi, enter ExtraPage.
  6. Replace the information between the Path tags
 with the file path to the new page. 
 Note You should only need to replace the last
 token in the path, <Name> Main
 Page.vi, with your page VI.
  7. Change the GUID between the <GUID>
 tags. 
 Note To reduce the risk of error when working with GUID string constants, consider
 using a LabVIEW global variable that is read only or creating a combo box control
 and saving it as a type definition.
  8. Save and close the XML file.
3. Add the page to the build specifications.
  1. Open the LabVIEW project for your custom
 device.
  2. In Project Explorer,
 expand Build
 Specifications, and double-click
 Configuration.
  3. In the Category menu, select
 Source Files.
  4. In Project Files, expand <Name>
 Custom Device.lvlib.
  5. Select the new page VI, and click Add Item. 
 The VI is added to the Always Included section.
  6. In the Category menu, select
 Source Files
 Settings.
  7. In Project Files, expand the
 <Name> Custom
 Device.lvlib.
  8. Select the new page VI, and from the
 Destination drop down box, select
 <Name> Configuration
 LLB.
  9. Click OK to close the
 build specification.
  10. Save the LabVIEW project.
4. Restart VeriStand.

If your new page is not created properly,
 you will receive a custom device page error when adding your
 custom device to the system definition:

Parent topic:

Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-api-library.html language=enus -->
## TOPIC 00136: Custom Device API Library

- bundle_id: `veristand`
- source_path: `custom-device-api-library.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-api-library.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Custom Device API library is a LabVIEW library that contains type definitions, template VIs, and the LabVIEW API a custom device needs to interact with VeriStand. To access the Custom Device API library, you must first install a compatible version of LabVIEW. When installing VeriStand, under Add

### Custom Device API Library

The *Custom Device API library* is a LabVIEW library that
 contains type definitions, template VIs, and the LabVIEW API a custom device needs to interact
 with VeriStand.

Note

Additional items you may wish to
 install

VeriStand Support for LabVIEW

The components of the library allows the custom device to communicate seamlessly in the VeriStand
 Engine. You can find the library in the labview\vi.lib\NI VeriStand\Custom Device
 API directory.

Note

| Template VI | Usage |
| --- | --- |
| Initialization VI Template.vit | Initialization VI. |
| Page Template.vit | Main Page VI or additional Page VI. |
| Asynchronous Custom Device Driver VI Template.vit | RT Driver VI for an asynchronous custom device. |
| Inline Custom Device Driver VI Template (HW Interface).vit | RT Driver VI for an Inline Hardware Interface custom device. |
| Inline Custom Device Driver VI Template (Model Interface).vit | RT Driver VI for an Inline Model Interface custom device. |
| Timing Source Initialization VI Template.vit | Timing Source Initialization VI for the Primary Control Loop. For VeriStand to call this VI, you must select the custom device as the Master Custom Device on the Controller configuration page. |
| RunTimeMenu Custom Item 2 Launch.vit | Runs when the user selects a custom shortcut menu item. |
| RunTimeMenu Custom Population.vit | Creates a custom shortcut menu. |
| RunTimeMenu Dependency.vit | Shows, removes, enables, or disables items in a custom shortcut menu. |
| ActionVIOnCompile Template.vit | Runs when an item is compiled. |
| ActionVIOnDelete Template.vit | Runs when a user successfully deletes an item. |
| ActionVIOnDownload Template.vit | Runs when the custom device downloads to the target. |
| ActionVIOnDeleteRequest Template.vit | Runs when a user attempts to delete an item. |
| ActionVIOnLoad Template.vit | Runs when VeriStand loads a system definition containing a custom device in System Explorer. |
| ActionVIOnPaste Template.vit | Runs when a user pastes an item in System Explorer. |
| ActionVIOnSave Template.vit | Runs when a user saves the system definition file. |
| ActionVIOnShutdown Template.vit | Runs when the VeriStand system shuts down. |

Parent topic:

Custom Device Framework

Related reference:

- Custom Device XML Tags

<!--NI_TOPIC bundle=veristand path=custom-device-asynchronous-driver-template.html language=enus -->
## TOPIC 00137: Using the Asynchronous Custom Device Driver Template

- bundle_id: `veristand`
- source_path: `custom-device-asynchronous-driver-template.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-asynchronous-driver-template.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the asynchronous custom device driver template to build the RT Driver VI for a custom device. You can use most of the Custom Device API VIs when building an asynchronous RT Driver VI. The Asynchronous Device Properties VIs and Asynchronous Device Channels VIs configure functionality exclusive to

### Using the Asynchronous Custom Device Driver
 Template

Use the asynchronous custom device driver template to build the RT Driver VI for a custom
 device.

You can use most of the Custom Device API
 VIs when building an asynchronous RT Driver VI. The Asynchronous
 Device Properties VIs and Asynchronous Device Channels VIs configure
 functionality exclusive to asynchronous custom devices.

An
 asynchronous custom device uses a two-loop architecture, one loop
 for receiving commands and one for transferring data, with sections
 of code for initialization and cleanup before and after the loops,
 respectively. The template VI uses a While Loop for data transfer,
 but you also can use a Timed Loop.

1. Navigate to the labview\vi.lib\NI VeriStand\Custom
 Device API directory and open
 Asynchronous Custom Device
 Template.vit.
2. Modify the following code to set up your controls and
 initialization for the custom device. 
 [IMAGE alt='image' src='GUID-260DDEF8-E5F9-4208-ABA7-2195DEA9CB2A-a5.gif'] 

 1
 Controls—The input controls
 are specially named controls that the VeriStand
 Engine will use to provide the asynchronous custom
 device loops with data. To function, the name of
 each control must match the following names. Device Clock—Device Clock
 specifies the name of a timing source that is
 ticked for every iteration of the Primary Control
 Loop after Custom Device FIFOs have been updated.
 If you change the data loop of your custom
 device to a Timed Loop, you can use Device Clock
 as the timing source of the Timed Loop to closely
 synchronize your asynchronous custom device with
 the Primary Control Loop. Device Clock is only
 populated if you set the Use Device Clock input of
 the Set Loop Type VI to True in
 one of the VIs for configuring the custom
 device.
 Initialization Status
 Notifier—You can use this optional input
 to send the VeriStand Engine the final status of
 the custom device initialization process. If this
 control exists on the custom device front panel,
 the VeriStand Engine will wait for a status update
 before starting up. If the custom device reports
 an error, that will abort the execution of the
 current configuration in the VeriStand Engine.
 Device Reference—Device
 Reference is an auto-populated reference to the
 custom device. Use it to read configuration
 properties, get a list of channels, etc.
 Device Outputs FIFO—The array
 of outputs sent to the system on the Device
 Outputs FIFO corresponds one-to-one to the Outputs
 array the Get Custom Device Channel List VI
 returns. By default, the VeriStand Engine reads
 the Device Outputs FIFO every iteration of the
 PCL.
 Device Inputs FIFO—The array
 of inputs received from the system on the Device
 Inputs FIFO corresponds one-to-one to the Inputs
 array the Get Custom Device Channel List VI
 returns. The VeriStand engine pushes data to the
 Device Inputs FIFO every iteration of the PCL. If
 the FIFO is full, the new data packet will
 overwrite the oldest data packet.
 Status Notifier—Notifies the
 engine of the last state of the custom device and
 indicates when the device completes execution. If
 you do not use this control, the device returns a
 default No Error value when it
 completes execution. By default, VeriStand does
 not check this error until shutdown, but you can
 use an output channel to send more immediate
 status values to the system.
 2
 Initialization Code—The
 template includes initialization code to do the
 following:Register custom engine events.
 Get the number of input and output channels
 and set up data buffers for the RT FIFOs.
 Read a final error status for the asynchronous
 custom device.
 If you use a Timed Loop for your data loop, you
 can also add code here to configure the Timed
 Loop.
3. Modify the following code to set up your command loop, data
 loop, and cleanup code for the custom device. 
 [IMAGE alt='image' src='GUID-F4F4D5E4-1FD3-4E8E-A091-CB0546CBF0D8-a5.gif'] 

 1
 Command Loop—The command loop
 allows you to send commands to and receive data
 from your custom device that you can not easily do
 using a DBL channel value. By using the Send
 Custom Device Message VI in a LabVIEW VI or
 calling a corresponding .NET method, you can use,
 for example, a custom workspace object or NI
 TestStand automation script to send a command to
 your custom device, which can then execute a
 response to that command.
 For example, a generic custom device for
 logging. If you need to change configuration data,
 such as the file path to which to save log files,
 at run time, you could create a custom workspace
 control to send this data to the command loop of
 the device, and then configure the command loop to
 update the configuration data when the data is
 received.
 The command loop contains the following three
 events:Message (Byte Array)—Receives
 and sends data as a byte array of 8-bit unsigned
 integer values.
 Message (String)—Receives and
 sends data as a string.
 Shut Down—The VeriStand
 Engine sends this command to indicate that the
 custom device should shut down.
 For an example custom device that uses Send
 Custom Device Message VI in a LabVIEW VI to
 communicate directly with the custom device, refer
 to the labview\examples\NI
 Veristand\Custom Devices\Communication
 Example directory.
 2
 Data Loop—Use this loop to
 read input data from the Device Inputs FIFO,
 update the data, and send the updated data via the
 Device Outputs FIFO to the rest of VeriStand. The
 template data loop contains code that reads the
 input data, adds it to a random number, and writes
 it back to the output channels. The data loop also
 executes shutdown if it receives a shut down
 notification from the command loop.
 3
 Cleanup Code—Use the
 optional Status Notifier control to publish the
 final error state of your device regardless of
 errors. If a Status Notifier control is present in
 the RT driver VI, VeriStand this as an indication
 that the device has shut down. Otherwise the
 VeriStand provides default status notification for
 the device.

Parent topic:

Asynchronous Custom Devices

<!--NI_TOPIC bundle=veristand path=custom-device-benchmark-debug.html language=enus -->
## TOPIC 00138: Custom Device Benchmarking and Debugging

- bundle_id: `veristand`
- source_path: `custom-device-benchmark-debug.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-benchmark-debug.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use tools provided by LabVIEW and VeriStand to benchmark and debug your custom device. You should perform benchmarking on a system that is similar to the target. Other components of the VeriStand system, such as models, calculated channels, alarms, and procedures, affect the ultimate executi

### Custom Device Benchmarking and
 Debugging

You can use tools provided by LabVIEW and VeriStand to benchmark and debug your custom
 device.

You should perform benchmarking on a system that is similar to the target. Other components
 of the VeriStand system, such as models, calculated channels, alarms, and procedures, affect
 the ultimate execution speed of the system.

| Tool | Purpose | Granularity | Location | Details |
| --- | --- | --- | --- | --- |
| LabVIEW Debugging Tools | Debugging | N/A | LabVIEW | You can merge debugged VIs into the Custom Device Framework manually. Timing can differ between standalone VIs and VIs in the Custom Device Framework. This tool is not available after VeriStand integration. For more information, refer to the Debugging Techniques topic in LabVIEW Help. |
| Custom Error Codes | Debugging | N/A | LabVIEW and VeriStand | You can define custom error codes in LabVIEW and distribute the codes to VeriStand with a custom device. Copy the custom errors.txt file to VeriStand in the <Base>\\National Instruments\\Shared\\Errors\\English directory and add the file as a dependency in custom device and Custom Device XML file. For RT targets, deploy the errors.txt file to the error directory on target to display error descriptions in Console Viewer. For more information, refer to the Defining Custom Error Codes to Distribute throughout Your Application topic in the LabVIEW Help |
| Print Debug String VI | Debugging | NA | LabVIEW | This VI prints messages to the RT console and the VeriStand data log. This tool works on Windows and RT targets. |
| NI Distributed System Manager | Benchmarking (CPU and RAM) | Medium | Installs with LabVIEW. | The manager works with network variables and manages remote target settings and the status of the Shared Variable Engine. This tool takes periodic snapshots. To use this tool, you must install System State Publisher on the RT target. CPU spikes and transients might not appear. |
| System Channels | Benchmarking and debugging | High | VeriStand | Useful system channels include: HP Count HP Loop Duration LP Count Model Count You can use these channels with alarms or procedures. |

Parent topic:

Implementing a Custom Device

Related concepts:

- Custom Device Framework
- Custom Device XML File

Related tasks:

- Viewing Real-Time Target Logs
- Adding and Configuring Alarms
- Adding and Configuring a Procedure

Related reference:

- VeriStand Directories and Aliases
- System Channels

<!--NI_TOPIC bundle=veristand path=custom-device-block-read-write.html language=enus -->
## TOPIC 00139: Implementing Channel Block Reading and Writing in Inline Custom Devices

- bundle_id: `veristand`
- source_path: `custom-device-block-read-write.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-block-read-write.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify an inline model interface custom device to use block data references to read and write channel data. Before you begin, create an inline model interface custom device. In an inline custom device, you can read or write channel data for multiple channels at a time using block data references. Bl

### Implementing Channel Block Reading and Writing
 in Inline Custom Devices

Modify an inline model interface custom device to use block data references to read and
 write channel data.

Before you begin, create an inline
 model interface custom device.

In an inline custom device, you can read or write channel data for multiple channels
 at a time using block data references. Block reading and writing is useful for
 custom devices with a large number of channels, as this technique runs faster than
 channel-by-channel access. Block reading and writing also simplifies your code, as
 referencing, reading and writing to a large number of channels individually can
 become large and complex.

- Get Channel Block Data References VI
- Get Channel Values by Block Data Reference VI
- Set Channel Values by Block Data Reference VI

1. Modify the Initialize case to obtain block data references. 
 [IMAGE alt='image' src='GUID-76FBD2D7-6865-4833-98A4-5B289C77C0A6-a5.gif'] 

1
Get Custom Device Channel List VI and
 Get Channel Block Data References
 VI—Replaces the For Loop and Get Channel Data Reference
 VI that attains Read Access channel data references in
 the inline model interface custom device template.
Get Custom Device Channel List VI and Get Channel Block
 Data References VI work together as follows: Get Custom Device Channel List VI returns an
 array of all the input channel references of the
 custom device.
Get Channel Block Data References VI uses this
 array to generate Block Data Refs for the input
 channels, or an array of 32-bit data references,
 and sets the Access to Read, allowing you to use
 the references to get channel data.
Get Channel Block Data References VI also
 returns the initial channel values as Values
 Array, which is used later in the Execute Model
 case.
2
Get Custom Device Channel List VI and
 Get Channel Block Data References
 VI—Replaces the For Loop and Get Channel Data Reference
 VI that attains Write Access channel data references in
 the inline model interface custom device template. Works
 similarly for output channels.
Get Custom Device Channel List VI and Get Channel Block
 Data References VI work together as follows:
Get Custom Device Channel List VI returns an array
 of all the output channel references of the custom
 device.
Get Channel Block Data References VI uses this array
 to generate Out Block Refs for the input channels,
 or an array of 32-bit data references, and sets the
 Access to Write, allowing you to use the references
 to write data to the channels.
Get Channel Block Data References VI also returns
 the initial channel values as Values Array, which is
 used later in the Execute Model case.
3
Block Data Refs and Values
 Array—Stored in a cluster for use in the
 Execute Model case. The refs and array are of both the input
 and output channels.
2. Modify the Execute Model case to read and write channel data with block
 references. 
 [IMAGE alt='image' src='GUID-B82DC98B-CF66-4623-A3FC-90E8B9BE75E2-a5.gif'] 

1
Get Channel Values by Block Data
 Reference VI—Uses the stored In Block Refs
 of the input channels to simultaneously get the value
 for each input channel.
2
Do Model Calculation Flat Sequence
 Structure—Sums all values in the Input Values array and
 saves them to the Output Values array.
3
Input Values and Output
 Values—Bundles arrays.
4
Set Channel Values by Block Data
 Reference VI—Uses the Block Data Refs of
 the output channels to simultaneously write the updated
 values, which are contained in Output Values array to
 the output channels.

Parent topic:

Inline Model Interface Custom Devices

Related concepts:

- Inline Model Interface Custom Devices
- Custom Device API Library

<!--NI_TOPIC bundle=veristand path=custom-device-build-specs.html language=enus -->
## TOPIC 00140: Custom Device Build Specifications

- bundle_id: `veristand`
- source_path: `custom-device-build-specs.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-build-specs.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Build Specifications in a custom device LabVIEW project includes the Configuration and Engine source distributions. The Configuration source distribution contains the source files that specify the configuration of the custom device when added to a VeriStand system definition. It also defines the

### Custom Device Build Specifications

The *Build Specifications* in a custom device LabVIEW project
 includes the Configuration and Engine source distributions.

The *Configuration* source distribution contains the source files that specify
 the configuration of the custom device when added to a VeriStand system definition. It
 also defines the user interface for the custom device in System
 Explorer.

- Initialization VI
- Main Page VI
- Custom Device XML file
- Any additional page VIs
- Any VIs the custom device configuration calls dynamically

The *Engine* source distribution contains the source files that configure how
 the custom device runs on the target. This build specification minimally includes the
 RT Driver VI. This specification also can include additional
 driver VIs and a timing source VI.

Both build specifications always include the Custom Device library, even though they do
 not both include every VI within that library.

#### Optional Source Distributions

- Configuration
- Engine (Windows)
- Engine (Linux x64)

After you configure the source distributions, you can choose between
 distributing the source files manually or using the LabVIEW Application Builder to
 build an installer.

Parent topic:

Custom Device Framework

<!--NI_TOPIC bundle=veristand path=custom-device-build.html language=enus -->
## TOPIC 00141: Building a Custom Device

- bundle_id: `veristand`
- source_path: `custom-device-build.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-build.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Build a custom device for distribution to VeriStand. Before you begin, you should start implementing your custom device. It will take several iterations of implementing and building to create your custom device. The process for building the source distribution for a custom device is the same as the

### Building a Custom Device

Build a custom device for distribution to VeriStand.

Before you begin, you should start
 implementing
 your custom device. It will take several iterations of implementing and
 building to create your custom device.

Configuration

Engine

Note

LabVIEW Help

Help

»

LabVIEW Help

1. Open your LabVIEW project.
2. Create a Configuration source distribution.
  1. In Project Explorer, right-click Build
 Specifications and select New»Source Distribution.
  2. In the My Source Distribution Properties dialog
 box, click Information, and enter the
 Build specification name as
 Configuration.
  3. Enter a Destination directory.
  4. Click Source Files and determine which files to
 include and exclude. 
 All dependency files that the custom device accesses on the target
 must exist in the LabVIEW project and appear in the Always Included
 list for the appropriate source distribution. You should include any
 dynamically-loaded dependencies, such as pages and the Initialization VI.
Note You must include
 the Custom Device XML file in the Configuration source distribution.
  5. Click Destinations and set the Destination type
 to LLB.
  6. Click Additional Exclusions, and disable
 Modify project library file after removing unused
 members. 
 Note This option can
 cause an error when you load the custom device in VeriStand.
  7. Click OK.
3. Create an Engine source distribution. 
 
 Note Use the same Destination
 directory as the Configuration source distribution. Using one directory
 makes it easier to distribute the custom device.
  1. In Project Explorer, right-click Build
 Specifications and select New»Source Distribution.
  2. In the My Source Distribution Properties dialog
 box, click Information, and enter the
 Build specification name as
 Engine.
  3. Enter a Destination directory.
  1. Click Source Files and determine which files to
 include and exclude.
  2. Click Destinations and set the Destination type
 to LLB.
  3. Click Additional Exclusions, and disable
 Modify project library file after removing unused
 members.
  4. Click OK.
4. Save the LabVIEW project.
5. Right-click Build Specifications and select
 Build All.

After building the custom device,
 distribute
 it.

Parent topic:

Creating Custom Devices

<!--NI_TOPIC bundle=veristand path=custom-device-channels-waveforms.html language=enus -->
## TOPIC 00142: Custom Device Channels and Waveforms

- bundle_id: `veristand`
- source_path: `custom-device-channels-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-channels-waveforms.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A custom device uses channels and waveforms to exchange data with the rest of the VeriStand system. Waveforms differ from channels in that VeriStand always sends channel data to the host computer, but VeriStand only streams waveform data upon request. You should acquire signals as waveforms when you

### Custom Device Channels and Waveforms

A custom device uses channels and waveforms to exchange data with the rest of the
 VeriStand system.

*Waveforms* differ from channels in that VeriStand always sends channel data to
 the host computer, but VeriStand only streams waveform data upon request. You should acquire
 signals as waveforms when you need to read at rates faster than the rate at which the system
 runs.

Channels

0 = FALSE

!0 =
 TRUE

Note

You can create input and output channels. Input channels get data from the rest of the
 VeriStand system. Output channels send data to the rest of the system. An operator can map
 each input channel to a single data source. However, an output channel can map to any number
 of sinks, such as simulation model inputs.

1. Handling data generated by the custom device after deployment.
2. Handling data generated elsewhere in the VeriStand system and used by the custom device
 after deployment.
3. Implementing dynamic properties.

Best practice is to implement channels with general use-cases in mind. For example, if you
 are writing a custom device to interface with third-party hardware, consider adding custom
 device channels for every physical channel of the hardware device and give the custom device
 operator the ability to remove channels while configuring the custom device in the system
 definition file.

Parent topic:

Planning a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-distribute.html language=enus -->
## TOPIC 00143: Distributing Custom Devices

- bundle_id: `veristand`
- source_path: `custom-device-distribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-distribute.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Package a custom device to manually distribute it to VeriStand. Before you begin, you must build the custom device. For information on building installers, refer to the LabVIEW Help. On your development machine, create a top-level directory to contain the custom device files. Within the new director

### Distributing Custom Devices

Package a custom device to manually distribute it to VeriStand.

Before you begin, you must build the custom
 device.

Note

LabVIEW Help

1. On your development machine, create a top-level directory to contain the custom device
 files.
2. Within the new directory, create two sub-directories and label them
 Build and Source.
3. Copy the source distributions you built from the custom device project into the
 Build directory. 
 Include both the LLBs and the Custom Device XML file.
4. Copy the LabVIEW project you used to create the custom device into the
 Source directory, along with any supporting files and dependencies.
5. On the same level as the Build and Source
 directories, create a readme file that includes any instructions an operator needs to
 install, license, use, and/or modify the custom device.
6. Create a ZIP file from the top-level directory.

<Common Data>\Custom
 Devices

<Common
 Data>\Timing and Sync

Note

To enable an operator with LabVIEW access to modify and rebuild the custom device, you can
 provide the files in the Source directory.

Parent topic:

Creating Custom Devices

Related tasks:

- Building a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-faq.html language=enus -->
## TOPIC 00144: Custom Device FAQs

- bundle_id: `veristand`
- source_path: `custom-device-faq.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-faq.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers to common questions about creating a custom device. Am I qualified to create a custom device? Creating a custom device requires specific knowledge and skills. The following table displays the specialized experience areas you need to successfully create a custom device. You can gain this expe

### Custom Device FAQs

Answers to common questions about creating a custom device.

#### Am I qualified to
 create a custom device?

Note

| Experience area | Description |
| --- | --- |
| LabVIEW Application Development | To develop a custom device, you must thoroughly understand LabVIEW programming and application architectures. NI recommends a Certified LabVIEW Developer (CLD) level of expertise before beginning development of a custom device. |
| LabVIEW Real-Time Application Development | As custom devices execute within real-time systems, you must be familiar with programming for real-time operating systems (RTOS) and specialized LabVIEW development techniques for developing real-time applications. |
| VeriStand Background | To develop a custom device, you must fully understand the VeriStand Engine. |

#### When do I need a
 custom device?

VeriStand supports most
 real-time testing applications. Before pursuing a custom device, you
 should first try to meet your needs with the built-in functionality.
 If you cannot meet your needs using the built-in VeriStand features,
 you can extend the functionality with a custom device. The following
 table lists situations where a custom device is best
 suited.

| Situation | Rationale |
| --- | --- |
| Integrating VeriStand with third-party hardware | If the hardware you need to integrate with VeriStand is not natively supported, you may be able to integrate it by creating a custom device. |
| Implementing a measurement or generation mode that VeriStand does not support | If VeriStand does not support the measurement or generation mode you need for your hardware type, you may be able to implement it using a custom device. For example, VeriStand supports single-point hardware-timed analog acquisition using DAQmx. However, VeriStand does not support force or torque measurements for analog DAQ channels. You can implement this measurement mode as a custom device. |
| Implementing additional features that VeriStand does not support | A VeriStand project may require a feature that VeriStand does not provide. You can extend VeriStand to meet your needs through a variety of methods. Custom devices are best suited for implementing features that require or use VeriStand channel data on the execution host. For example, the Embedded Data Logger allows you to log VeriStand channels to a TDMS file without first sending channel data back to the Workspace, as with high-speed streaming. However, if you need to display the previous test results on the workspace while running a new test, a custom workspace object may be more appropriate than a custom device. |

If you do not need the full range of custom device functionality,
 you can fulfill your requirements by converting a LabVIEW VI into a
 compiled model. Other alternatives include utilizing workspace
 tools, implementing custom FPGA bitfiles, and exploring the various
 LabVIEW and .NET APIs that ship with VeriStand.

#### When do I need a
 hardware custom device?

Before you begin developing a
 custom device to interact with unsupported or third-party hardware,
 NI recommends you evaluate the data requirements of the device and
 the availability of device drivers and APIs. To support third-party
 hardware, a custom device must call a hardware or instrument driver.
 If a hardware or instrument driver does not exist, you will need to
 either create the driver yourself or ask the vendor for that device
 for a driver.

Answering the following questions can help you
 determine whether a custom device is feasible for a specific
 hardware device:

- Does a LabVIEW instrument driver exist for the device? Note You can search for instrument drivers
 on the *Instrument Driver Network* and *NI Hardware Drivers*
 pages.
- Is a hardware driver/API available for the device and
 easy to use?
- If necessary, is the hardware driver executable in LabVIEW Real-Time Module? Note Refer to *Verify Your DLL Is
 Executable in LabVIEW Real-Time* for more information about testing DLLs for
 real-time support.
- Can you meet the hardware requirements by passing
 LabVIEW 64-bit double-precision floating point
 numbers to and from the custom device during steady
 state operation? Note If
 the hardware driver returns a vector, structure,
 or any non-DBL data, you cannot pass the data
 directly from the custom device to VeriStand. You
 must coerce the data or design an alternative
 communication mechanism to pass data from the
 custom device to the rest of the
 system.

Parent topic:

Creating Custom Devices

Related concepts:

- VeriStand Engine

Related information:

- NI Education Services
- Instrument Driver Network (IDNet)
- NI Hardware Drivers
- Verify Your DLL Is Executable in LabVIEW Real-Time

<!--NI_TOPIC bundle=veristand path=custom-device-framework.html language=enus -->
## TOPIC 00145: Custom Device Framework

- bundle_id: `veristand`
- source_path: `custom-device-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Follow the custom device framework to ensure your LabVIEW code interacts correctly with VeriStand. The custom device framework consists of type definitions, specifically named controls and indicators, template VIs, and a LabVIEW API. These items form the rules, or framework, that allow your code to

### Custom Device Framework

Follow the custom device framework to ensure your LabVIEW code interacts correctly with
 VeriStand.

The custom device framework consists of type definitions, specifically named controls and
 indicators, template VIs, and a LabVIEW API. These items form the rules, or framework,
 that allow your code to interact with VeriStand.

| Component | Description |
| --- | --- |
| Custom Device XML file | The Custom Device XML file enables you to define parts of the custom device in System Explorer, specify which VIs to call, and select the dependencies to deploy to an RT target. |
| Custom Device API Library | The Custom Device API library is a LabVIEW library that contains type definitions, template VIs, and the LabVIEW API a custom device needs to interact with VeriStand. |
| Custom Device Library | The Custom Device library is a LabVIEW library that contains the configuration and engine VIs for a custom device. The configuration and engine VIs may optionally be distributed in different LabVIEW libraries. |
| Build Specifications | The Build Specifications in a custom device LabVIEW project includes the Configuration and Engine source distributions. |

Parent topic:

Creating Custom Devices

Related concepts:

- Custom Device XML File
- Custom Device API Library
- Custom Device Library
- Custom Device Build Specifications

<!--NI_TOPIC bundle=veristand path=custom-device-hierachy.html language=enus -->
## TOPIC 00146: Custom Device Hierarchy

- bundle_id: `veristand`
- source_path: `custom-device-hierachy.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-hierachy.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A logically configured hierarchical structure allows operators to efficiently use your custom device. The hierarchy of a custom device is its appearance in System Explorer. The top level of the custom device hierarchy is the device itself, which appears under Custom Devices section of the configurat

### Custom Device Hierarchy

A logically configured hierarchical structure allows operators to efficiently use your
 custom device.

The *hierarchy* of a custom device is its appearance in System
 Explorer. The top level of the custom device hierarchy is the device
 itself, which appears under Custom Devices section of the configuration tree. Under the
 device, you can add any number of sections and channels to build the hierarchy.

Sections

Note

The following example shows the hierarchy of a typical power supply custom device.

[IMAGE alt='image' src='GUID-C27656AE-6135-43B0-9B6E-644A92483627-a5.gif']

Parent topic:

Planning a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-implement-hierarchy.html language=enus -->
## TOPIC 00147: Implementing a Custom Device Hierarchy

- bundle_id: `veristand`
- source_path: `custom-device-implement-hierarchy.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-implement-hierarchy.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Implement a flat or nested hierarchy for your custom device. Before you begin, you should understand custom device hierarchies. A flat hierarchy is a hierarchy in which all of the channels appear under one section in the configuration tree. A nested hierarchy includes additional sections under the m

### Implementing a Custom Device Hierarchy

Implement a flat or nested hierarchy for your custom
 device.

Before you begin, you
 should understand custom device
 hierarchies.

flat hierarchy

nested hierarchy

1. Use the following table to determine the type
 of hierarchy you want in your custom device. 
 Hierarchy type
Use caseFlat
Best suited for custom devices with a low
 number of channels.
Nested
Best suited for custom devices with many
 channels. A nested hierarchy makes the device
 easier to understand and operate for users.
2. Optional: 
 Modify the following code to create a flat hierarchy. 
 [IMAGE alt='image' src='GUID-1324969A-E3A4-4081-92BA-55E8911A7E33-a5.gif'] 

1
The Device Item Ref—Reference to the custom device, and
 specifies that each of the Add Custom Device Channel VIs will place the
 channels they create under the main section of the custom device in
 System Explorer.
2
Add Custom Device Channel VI—Creates an input channel named
 SMBTrig under the main section of the custom device.
3
Add Custom Device Channel VIs—Creates eight input channels
 named ADEnCh<1...8> and eight output channels named
 ADDataFromCh<1...8> under the main section of the custom device. 
 All channels will appear under the main custom device section when an operators
 adds the custom device to the system definition file. The following image displays what
 this hierarchy will look like in System Explorer. 
[IMAGE alt='image' src='GUID-191DA1C9-431A-4E31-8BFD-42398D2DA719-a5.gif']
3. Optional: 
 Modify the following code to create a nested hierarchy. 
 [IMAGE alt='image' src='GUID-2D443A40-0CC8-43C0-A1C3-F10C6CD0B10D-a5.gif'] 

1
Add Custom Device Section VIs—Creates two sections, Hardware
 Enables and Hardware Inputs, under the main section in System
 Explorer.
2
Add Custom Device Channel VI—Uses the Section
 Ptr reference to create eight channels, ADEnCh
 <1...8>, under the Hardware Enables section.
3
Add Custom Device Channel VI—Uses the Section
 Ptr reference to create eight channels, AddDataFromCh
 <1...8>, under the Hardware Inputs section.
4
Add Custom Device Channel VI—Creates SMBTrig to use
 Device Item Ref in. Therefore, SMBTrig will appear under
 the main custom device section. 
 All channels will appear under the main custom device section when an operators
 adds the custom device to the system definition file. The following image displays what
 this hierarchy will look like in System Explorer. 
[IMAGE alt='image' src='GUID-724854ED-FAE4-4394-87AF-78F9D591F08D-a5.gif']

Parent topic:

Implementing a Custom Device

Related concepts:

- Custom Device Hierarchy

<!--NI_TOPIC bundle=veristand path=custom-device-implement.html language=enus -->
## TOPIC 00148: Implementing a Custom Device

- bundle_id: `veristand`
- source_path: `custom-device-implement.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-implement.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Develop a custom device to fit your requirements. Before you begin, you should plan your custom device. Depending on your goal, complete any of the following tasks to configure the appearance and components of your custom device. Goal Task Add custom device channels and waveforms Add channels and wa

### Implementing a Custom Device

Develop a custom device to fit your requirements.

Before you begin, you should plan your custom
 device.

1. Depending on your goal, complete any of the following tasks to configure the
 appearance and components of your custom device. 
 Goal
TaskAdd custom device channels and
 waveforms
Add channels and waveforms to a custom device by using the
 appropriate VI within a Custom Device Library VI that runs on the host
 computer.
Add custom device item
 properties
Use VIs on the Item Properties palette to get and set properties of
 custom device items.
Add custom device pages
Add pages to a custom device by creating the extra page VIs and GUIDs,
 adding the extra pages to the custom device build specifications, and defining the pages
 in the Custom Device XML file.
Implement a custom device
 hierarchy
Implement a flat or nested hierarchy for your custom
 device.
Add custom glyphs, shortcut menus, and
 toolbar buttons
Use elements in the Custom Device XML to configure custom user
 interface components, such as glyphs, toolbar buttons, and shortcut
 menus.
Add custom error codes
Build custom error codes for your custom device using the General
 Error Handler VI or the Error Code File Editor.
Automate responses to user
 actions
Use action VI templates with the custom device XML file to automate
 responses to user actions.
2. Depending on your goal, complete any of the following tasks to customize the
 custom device engine by completing the following tasks. 
 Goal
TaskSync an asynchronous custom device with
 the PCL
Configure an asynchronous custom device to run synchronously with
 VeriStand by configuring the custom device to use the same timing source as the Primary
 Control Loop (PCL).
Read and write waveforms in the custom
 device engine
Use waveforms in custom devices to publish waveform data or
 read waveform data from other sources in the VeriStand Engine.
3. Use tools to benchmark and debug the custom device.

After implementing your custom device, build the custom
 device.

Parent topic:

Creating Custom Devices

Related concepts:

- Custom Device Benchmarking and Debugging

Related tasks:

- Planning a Custom Device
- Adding Custom Device Channels and Waveforms
- Adding Custom Device Item Properties
- Adding Custom Device Pages
- Implementing a Custom Device Hierarchy
- Adding Custom Glyphs, Shortcut Menus, and Toolbar Buttons
- Adding Custom Error Codes in a Custom Device
- Automating Responses to User Actions with Action VIs
- Synchronizing an Asynchronous Custom Device with the Primary Control Loop
- Reading and Writing Waveforms in the Custom Device Engine
- Building a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-inline-async-loop.html language=enus -->
## TOPIC 00149: Inline Custom Devices with Asynchronous Loops

- bundle_id: `veristand`
- source_path: `custom-device-inline-async-loop.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-inline-async-loop.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RT Driver VI of an inline custom device can communicate channel data with VeriStand while launching an asynchronous loop(s) to handle nondeterministic operations. One example of a nondeterministic operation is writing data to a log file. The RT Driver VI of the inline custom device communicates

### Inline Custom Devices with Asynchronous
 Loops

The RT Driver VI of an inline custom device can communicate channel data with VeriStand
 while launching an asynchronous loop(s) to handle nondeterministic operations.

One example of a nondeterministic operation is writing data to a log file. The RT Driver VI
 of the inline custom device communicates with the asynchronous loop(s) using RT FIFOs.

The following table displays the advantages and limitations of using this architecture when
 compared to inline and asynchronous custom devices.

| Device Type | Advantages | Limitations |
| --- | --- | --- |
| Inline custom devices | Allow you to read and write data to and from VeriStand in each iteration of the Primary Control Loop (PCL). Allow you to access VeriStand system channels outside of your custom device. | Can introduce latency into the PCL as inline custom devices run inline with the PCL. |
| Asynchronous custom devices | Allow you to execute large operations without introducing latency into the PCL. | While you can synchronize the loop to the PCL, making the custom device pseudo-synchronous, pseudo-synchronous loops are not guaranteed to iterate once per iteration of the PCL nor are they guaranteed to iterate deterministically with respect to the PCL. |
| Inline custom devices with asynchronous loops | Allow you to read and write data to and from VeriStand in each iteration of the Primary Control Loop (PCL). Asynchronous loop(s) handle nondeterministic operations, such as writing data to a log file, without introducing latency into the PCL. | Data must be consumed from the RT FIFOs at a fast enough rate or the mechanism will overflow. |

#### Example: Embedded Data Logger

The
 Embedded Data
 Logger is an inline hardware interface custom device that reads and writes data to
 and from VeriStand in each iteration of the PCL. The Embedded Data Logger launches an
 asynchronous loop to log the data it receives to a file to avoid causing latency in the PCL
 that is associated with file I/O.

Note

VeriStand Embedded Data Logger Custom
 Device

| Action | Description |
| --- | --- |
| Initializing RT FIFOs and launching an asynchronous loop | The Initialize case of the Embedded Data Logger RT Driver VI creates two RT FIFOs and launches an asynchronous loop. One RT FIFO communicates channel data from the Embedded Data Logger RT Driver VI to the asynchronous loop. The other RT FIFO communicates state information from the asynchronous loop to the Embedded Data Logger RT Driver VI. The following diagram illustrates how the Embedded Data Logger and asynchronous loop execute with respect to the PCL and how the Embedded Data Logger communicates to the asynchronous loop via RT FIFOs. |
| Reading the status of the asynchronous loop in the inline custom device | One of the RT FIFOs created in the Initialize case passes status information from the asynchronous loop to the Embedded Data Logger RT Driver VI. You can see how the Embedded Data Logger RT Driver VI reads data from the RT FIFO by examining the Read Data from HW case. In this case, the Embedded Data Logger checks the RT FIFO for a change in the error value. |
| Sending channel data from the inline custom device to the asynchronous loop | The other RT FIFO sends channel data from the Embedded Data Logger RT Driver VI to the asynchronous loop. This communication takes place in the Write Data to HW case, specifically in the Sample Group Data VI that executes in this case. This VI is responsible for getting the values of the channels to log from the PCL and writing them to the RT FIFO so the asynchronous loop can access them. |

Parent topic:

Custom Device Types

Related tasks:

- Synchronizing an Asynchronous Custom Device with the Primary Control Loop
- Logging Target Data with the Embedded Data Logger

Related information:

- VeriStand Embedded Data Logger Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-inline-hardware-interface-template.html language=enus -->
## TOPIC 00150: Using the Inline Hardware Interface Custom Device Driver Template

- bundle_id: `veristand`
- source_path: `custom-device-inline-hardware-interface-template.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-inline-hardware-interface-template.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the inline hardware interface custom device driver template to build the RT Driver VI for a custom device. The block diagram of the Inline Custom Device Driver VI Template (HW Interface).vit template VI contains a case structure with five cases to which you can add code to customize the device.

### Using the Inline Hardware Interface Custom
 Device Driver Template

Use the inline hardware interface custom device driver template to build the RT Driver VI
 for a custom device.

The block diagram of the Inline Custom Device Driver VI Template (HW
 Interface).vit template VI contains a case structure with five cases to which
 you can add code to customize the device.

[IMAGE alt='image' src='GUID-1E457FFF-2E21-41ED-B88D-D61D3CF68B83-a5.gif']

1. Navigate to the labview\vi.lib\NI VeriStand\Custom Device API
 directory and open Inline Custom Device Driver VI Template (HW
 Interface).vit.
2. Modify the following code to set up the Initialization case that executes before the
 PCL starts running. 
 Note Because the Initialize case executes before the PCL starts,
 you cannot read or write channel values in this case.
 
[IMAGE alt='image' src='GUID-ACBAE011-347B-429E-AE95-E2B87AF5F971-a5.gif'] 

 1
 Get Custom Device Channel List VI—Gets a list of all the
 input and output of channels of the custom device.
 2
 Get Channel Data Reference VI—Compiles a list of channel
 data references for the channels. In this case, you can also read device
 configuration information from properties that use a reference to the
 device.Note The Get Channel
 Data Reference VI does not appear on the Functions palette but belongs to
 the Custom Device API library. To avoid causing system instability or
 errors, do not call this VI or the Set Channel Data Reference VI outside of
 an inline RT Driver VI.
3. Modify the Start case that executes after initialization but before the PCL starts
 running. 
 If necessary, you can use this case to start device tasks, such as
 DAQ tasks, or to wait for start triggers. Because the Start case executes before the PCL
 starts, you cannot read or write channel values in this case.Note If you use a start trigger in the Start
 case, you should specify a timeout for waiting on the trigger. Failing to specify a
 timeout can cause your system to wait indefinitely if the start trigger does not occur
 as expected.
4. Modify the following code to set up a the Read Data from HW case that executes at the
 beginning of each iteration of the PCL before other components such as faults, alarms, and
 procedures. 
 [IMAGE alt='image' src='GUID-01CC0D78-68F7-4D91-B643-AA940F2E192A-a5.gif'] 

 1
 Read Hardware Channels—You can replace this flat sequence
 structure or the code inside it with the code necessary to obtain data from a
 hardware device. For example, you can use a hardware device's API calls to
 request an A/D sample.
 2
 Set Channel Value by Data Reference VI—Writes the data to
 a specified channel, making the data available to the other components of
 VeriStand for the remainder of the PCL iteration.
5. Modify the following code to set the Write Data to Hardware case that executes at the
 end of each iteration of the PCL after other components such as faults, alarms, and
 procedures. 
 [IMAGE alt='image' src='GUID-87647F86-4EC1-4666-AA75-698FB7476A5F-a5.gif'] 

 1
 Write Input Data to Hardware Channels—You can replace the
 code in this flat sequence structure with the code necessary to send data to a
 hardware device.
6. Modify the Close case that executes after the PCL finishes executing. 
 Use this case to close references and release resources. Because the close case
 executes after the PCL terminates, you cannot read or write channel values in this
 case.

Parent topic:

Inline Hardware Interface Custom Devices

<!--NI_TOPIC bundle=veristand path=custom-device-inline-hardware-interface.html language=enus -->
## TOPIC 00151: Inline Hardware Interface Custom Devices

- bundle_id: `veristand`
- source_path: `custom-device-inline-hardware-interface.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-inline-hardware-interface.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An inline hardware interface custom device executes inline with the VeriStand Engine's Primary Control Loop (PCL) and enables you to read and write data from and to a hardware device. You can create a standard inline hardware interface custom device from a template in the Custom Device API library.

### Inline Hardware Interface Custom
 Devices

An *inline hardware interface* custom device executes inline with the
 VeriStand Engine's Primary Control Loop (PCL) and enables you to read and write data from
 and to a hardware device.

You can create a standard inline hardware interface custom device from a template in the
 Custom Device
 API library. This also applies to the Inline Timing and Sync device type,
 which is an inline hardware interface device that you add to the system definition file
 as a timing and sync device.

An inline hardware interface custom device executes as a state machine, or action-engine.
 The device contains a Case structure, and the PCL calls each case at a specific time
 with respect to other components of the VeriStand Engine. Within the device, an
 uninitialized Feedback Node handles iterative data transfer between states.

Note

The inline hardware interface custom device is similar to the inline model interface
 custom device. An inline hardware interface custom device has two cases, or steps, that
 execute within an iteration of the PCL. An inline model interface custom device has only
 one step that executes within a PCL iteration.

Parent topic:

Custom Device Types

Related concepts:

- Custom Device API Library

Related tasks:

- Using the Inline Hardware Interface Custom Device Driver Template

<!--NI_TOPIC bundle=veristand path=custom-device-inline-model-interface-template.html language=enus -->
## TOPIC 00152: Using the Inline Model Interface Custom Device Driver Template

- bundle_id: `veristand`
- source_path: `custom-device-inline-model-interface-template.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-inline-model-interface-template.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the inline model interface custom device driver template to build the RT Driver VI for a custom device. The block diagram of the Inline Custom Device Driver VI Template (Model Interface).vit template VI contains a case structure with four cases to which you can add code to customize the device.

### Using the Inline Model Interface Custom Device
 Driver Template

Use the inline model interface custom device driver template to build the RT Driver VI
 for a custom device.

The block diagram of the Inline Custom Device Driver VI
 Template (Model Interface).vit template VI
 contains a case structure with four cases to which you can add code
 to customize the device.

[IMAGE alt='image' src='GUID-B3E890A0-4FAC-4E85-9DEB-0DCEE6F7FB58-a5.gif']

1. Navigate to the labview\vi.lib\NI VeriStand\Custom
 Device API directory and open
 Inline Custom Device Driver VI Template
 (Model Interface).vit.
2. Modify the following code to set up the Initialization case
 that executes before the PCL starts running. 
 Note Because the Initialize case executes before the PCL starts,
 you cannot read or write channel values in this case.
 
[IMAGE alt='image' src='GUID-70B99AF8-7FFF-41C0-BE66-EFCA9936A36E-a5.gif'] 

1
 Get Custom Device Channel List VI—Gets a list of all the
 input and output of channels of the custom device.
 2
 Get Channel Data Reference VI—Compiles a list of channel
 data references for the channels. In this case, you can also read device
 configuration information from properties that use a reference to the
 device.Note The Get Channel
 Data Reference VI does not appear on the Functions palette but belongs to
 the Custom Device API library. To avoid causing system instability or
 errors, do not call this VI or the Set Channel Data Reference VI outside of
 an inline RT Driver VI.
3. Modify the Start case that executes after initialization but
 before the PCL starts running. 
 If necessary, you can use this case to start device tasks, such as
 DAQ tasks, or to wait for start triggers. Because the Start case executes before the PCL
 starts, you cannot read or write channel values in this case.Note If you use a start trigger in the Start
 case, you should specify a timeout for waiting on the trigger. Failing to specify a
 timeout can cause your system to wait indefinitely if the start trigger does not occur
 as expected.
4. Modify the following code to set up the Execution case that
 executes in the middle of the PCL iteration. 
 [IMAGE alt='image' src='GUID-E895A9C4-10BC-4403-8AB2-8D43545B93C3-a5.gif'] 

This case reads input data, executes the model, and then
 writes output data to the rest of VeriStand.
 *Model* refers to a mathematical
 function. You may need to average channel data, or
 you can execute a LabVIEW or other model using the
 LabVIEW Model Interface Toolkit.
5. Modify the Close case that executes after the PCL finishes
 executing. 
 Use this case to close references and release resources.
 Because the close case executes after the PCL
 terminates, you cannot read or write channel values
 in this case.

If your custom device needs to read or write
 channel data for multiple channels at a time, consider using block data references in your code.

Parent topic:

Inline Model Interface Custom Devices

Related tasks:

- Implementing Channel Block Reading and Writing in Inline Custom Devices

<!--NI_TOPIC bundle=veristand path=custom-device-inline-model-interface.html language=enus -->
## TOPIC 00153: Inline Model Interface Custom Devices

- bundle_id: `veristand`
- source_path: `custom-device-inline-model-interface.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-inline-model-interface.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An inline model interface custom device executes inline with the VeriStand Engine's Primary Control Loop (PCL), which processes data acquired from hardware inputs and sends the processed values to hardware outputs without latency. You can create an inline model interface custom device from a templat

### Inline Model Interface Custom Devices

An *inline model interface* custom device executes inline with the VeriStand
 Engine's Primary Control Loop (PCL), which processes data acquired from hardware inputs and
 sends the processed values to hardware outputs without latency.

You can create an
 inline model interface custom device from a template in the Custom Device API
 library.

An inline model interface custom device executes as a state machine, or action-engine.
 The device contains a Case structure, and the PCL calls each case at a specific time
 with respect to other components of the VeriStand Engine. Within the device, an
 uninitialized Feedback Node handles iterative data transfer between states.

The inline model interface custom device is very similar to the inline hardware
 interface custom device. An inline model interface custom device has one
 case, or step, that executes within an iteration of the PCL, while an inline hardware
 interface custom device has two steps that execute within a PCL iteration.

Parent topic:

Custom Device Types

Related concepts:

- Custom Device API Library
- Inline Hardware Interface Custom Devices

Related tasks:

- Using the Inline Model Interface Custom Device Driver Template

<!--NI_TOPIC bundle=veristand path=custom-device-item-properties.html language=enus -->
## TOPIC 00154: Custom Device Item Properties

- bundle_id: `veristand`
- source_path: `custom-device-item-properties.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-item-properties.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Custom device item properties store and communicate state information about a custom device item, such as a section or channel. A custom device item is anything that appears in System Explorer, such as a channel within a custom device or the custom device itself. Use properties to transfer configura

### Custom Device Item Properties

Custom device item properties store and communicate state information about a custom
 device item, such as a section or channel.

A *custom device item* is anything that appears in System
 Explorer, such as a channel within a custom device or the custom device
 itself. Use *properties* to transfer configuration and state information
 from the configuration to the engine after an operator deploys the system definition
 file to the target. After deployment, the engine can read properties on the target, but
 it cannot write properties or exchange properties with the host computer.

For example, if you are creating a custom device for third-party hardware and you need to
 implement a range option for the channels you will use to communicate with the hardware,
 you should implement the range setting as a property. You can then customize the page
 VIs for those channels to accept a value for range, allowing you to define the value
 when configuring the channels in System Explorer. When the custom
 device is deployed, VeriStand will read the value for range and set the range of that
 channel when the system definition is deployed. After it is deployed, you can no longer
 change the value for range.

Unlike a channel, which must be a 64-bit floating point number, a property can be any
 standard LabVIEW data type. However, property names are case-sensitive strings.
 VeriStand saves property names and values with the system definition file. If you save
 and close the file or project, VeriStand retains the properties the next time you access
 the system definition file.

Parent topic:

Planning a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-library.html language=enus -->
## TOPIC 00155: Custom Device Library

- bundle_id: `veristand`
- source_path: `custom-device-library.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-library.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Custom Device library is a LabVIEW library that contains the configuration and engine VIs for a custom device. The configuration and engine VIs may optionally be distributed in different LabVIEW libraries. Custom device library VIs configure the initialization behavior of the custom device, its

### Custom Device Library

The *Custom Device library* is a LabVIEW library that
 contains the configuration and engine VIs for a custom device. The configuration and
 engine VIs may optionally be distributed in different LabVIEW
 libraries.

System Explorer

Note

The Custom Device library contains the following sets of VIs to modify your custom
 device.

#### VIs for Configuring the Custom Device

Configuration.llb

Note

System
 Explorer

| VI | Description |
| --- | --- |
| Initialization VI | Prepares the custom device for first use. This VI defines the initial list of channels and/or sections that appear in System Explorer, as well as sets their initial properties. The VI runs in the background every time an operator adds the custom device to the system definition file. It reads information from the Custom Device XML file and uses the data to add an instance of the custom device to System Explorer. The instance runs in the execution mode you specify and loads the correct dependency files. If the operator adds multiple instances of the device to the same system definition file, this VI runs for each new instance. |
| Main Page VI | Runs when the operator selects the custom device in System Explorer. The front panel of this VI serves as the configuration page for the custom device. You can modify this VI to add additional controls and indicators to the configuration page, and to configure responses to user events, such as when the operator enters a new item property value. |
| Extra Page VIs | Provides custom configuration pages for the sections and channels that appear under the custom device in System Explorer. You can configure these VIs in the same way you configure the Main Page VI. Every extra page you configure must have an entry in the <Pages> section of the Custom Device XML file. If you do not specify an extra page for a section or channel, VeriStand displays a default section or channel page when you select the item. You can use the Set Item GUID VI to change the page associated with an item at run time. |
| Action VIs | Allows the custom device to perform custom actions when specific events occur, such as when the system definition is loaded in System Explorer. |
| Shortcut Menus | Appears in a shortcut menu when a custom device item is right-clicked in the System Explorer. These may also appear as toolbar buttons. |

#### VIs for Customizing the Custom Device Engine

The
 custom device engine defines the real-time behavior of the custom device on the
 target. The RT Driver VI runs on the target regardless of the target's operating
 system.

You can have more than one RT Driver VI depending on the needs of your
 custom device. For example, if your custom device must support multiple real-time
 operating systems, you can add additional RT Driver VIs for each additional
 operating system the custom device must support.

| VI name | Description |
| --- | --- |
| RT Driver VI | Runs after the operator deploys the system definition file. You can add code to this VI to handle any run-time requirements of the custom device. Use this code to configure initialization, steady-state, and shutdown behavior for the custom device engine. This VI handles timing information and the exchange of data between the custom device and the rest of the VeriStand system. |

Parent topic:

Custom Device Framework

Related concepts:

- Custom Device API Library

Related tasks:

- Automating Responses to User Actions with Action VIs
- Adding Custom Glyphs, Shortcut Menus, and Toolbar Buttons

<!--NI_TOPIC bundle=veristand path=custom-device-pages.html language=enus -->
## TOPIC 00156: Custom Device Pages

- bundle_id: `veristand`
- source_path: `custom-device-pages.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-pages.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In a custom device, pages are the configuration pages that appear when you select the custom device or various sub-items of the device in System Explorer. The configuration page that an operator sees is simply the front panel of a page VI. Every custom device must include a Main Page VI that runs wh

### Custom Device Pages

In a custom device, *pages* are the configuration pages that appear when you
 select the custom device or various sub-items of the device in System
 Explorer.

The configuration page that an operator sees is simply the front panel of a page VI.
 Every custom device must include a Main Page VI that runs when the operator selects the
 top-level custom device item in the configuration tree. Sub-items of the custom device,
 such as sections and channels, appear with simple default configuration pages that allow
 a user to set descriptions for the associated items.

#### Extra Pages

You can create additional
 pages with extended functionality and use those pages in place of the default pages.

Plan an extra page for each item in a custom device that you want to
 customize differently. For example, if you want to use the same custom configuration
 page for all channels in a custom device, you only need to create one extra
 page.

The following table displays the items VeriStand requires to override a
 default page with an extra page in the custom device.

| Required item | Description | How to create |
| --- | --- | --- |
| Page VI | Defines the functions and appearance of the extra page. The front panel of the page VI serves as the configuration page in System Explorer. | Use the page template in the Custom Device API library. |
| Globally Unique Identifier (GUID) | Links to the extra page using an ID. When you associate an extra page with a channel or section, you override the default page by referencing the GUID of the extra page. | Use the GUID Generator VI in the labview\\vi.lib\\NI Veristand\\Custom Device Tools\\Custom Device Template Tool directory. You can set the GUID of an extra page by using the GUID terminal of either the Add Custom Device Section VI or Add Custom Device Channel VI. For more information on how to use the GUID Generator VI, refer to the topic on adding extra pages after creating the custom device project. |
| XML Declaration | Associates the GUID with the page VI in the custom device XML. | Edit the custom device XML to declare the extra page and its GUID. For more information, refer to the topic on adding extra pages after creating the custom device project. |
| Build Specification | Specifies the extra page and any of its dynamically called dependencies. | Edit the Configuration build specification to include the extra page and any of its dynamically called dependencies in the initialization library. For more information, refer to the topic on adding extra pages after creating the custom device project. |

Parent topic:

Planning a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-plan.html language=enus -->
## TOPIC 00157: Planning a Custom Device

- bundle_id: `veristand`
- source_path: `custom-device-plan.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-plan.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: It is important to plan the major components of a custom device before writing any LabVIEW code. Before you begin planning, you should understand the custom device framework. Understand the following components of a custom device. If the custom device must interact with unsupported or third-party ha

### Planning a Custom Device

It is important to plan the major components of a custom device before writing any
 LabVIEW code.

Before you begin planning, you should understand the custom device
 framework.

Understand the following components of a custom device.

Note

| Component | Description |
| --- | --- |
| Channels and waveforms | The inputs and outputs of the custom device. |
| Properties | Configuration data for the custom device. |
| Hierarchy | The organization and appearance of the custom device in System Explorer. |
| Pages | The configuration pages that appear in System Explorer. |
| Device Type | The execution mode of the custom device in terms of interaction with the rest of VeriStand. |

After planning your custom device, you can implement the custom
 device.

Parent topic:

Creating Custom Devices

Related concepts:

- Custom Device Framework
- Custom Device Channels and Waveforms
- Custom Device Item Properties
- Custom Device Hierarchy
- Custom Device Pages
- Custom Device Types

Related tasks:

- Implementing a Custom Device

<!--NI_TOPIC bundle=veristand path=custom-device-read-write-waveform-considerations.html language=enus -->
## TOPIC 00158: Other Considerations for Reading and Writing Waveforms in a Custom Device Engine

- bundle_id: `veristand`
- source_path: `custom-device-read-write-waveform-considerations.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-read-write-waveform-considerations.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When reading and writing waveforms in a custom device, you should try to avoid data loss, identify the value source when reading from multiple waveforms, and calculate the start time of a read operation. Avoiding Data Loss When Reading and Writing DataVeriStand uses queues to transfer data between c

### Other Considerations for Reading and Writing
 Waveforms in a Custom Device Engine

When reading and writing waveforms in a custom device, you should try to avoid data loss,
 identify the value source when reading from multiple waveforms, and calculate the start time of
 a read operation.

#### Avoiding Data Loss When Reading and Writing Data

- Write sessions—The queue size is three elements, so the custom device can write three
 times without the WPL reading from the queue before data loss occurs.
- Read sessions—The queue size is three times the number of waveforms being read. For
 example, if you read from ten waveforms, the queue size is 30.

If you notice data loss, you can specify a larger, custom queue size for the
 VeriStand Engine to use. When you open a read or write session with the Open Waveform
 Session VI, use the elements of the Communication Properties input cluster to define a
 custom queue size. If the CPU cannot read or write as quickly as the custom device requires,
 changing the queue size will not resolve data loss, only delay it.

For read sessions,
 you can monitor the WPL Overflow Count system channel to determine if a queue overflows. For
 write sessions, use the timed out? output of the Write Waveform(s) VI to indicate when data
 loss occurs.

#### Identifying the Source of Values When You Read from Multiple
 Waveforms

If you open a read session for multiple waveforms, the Read Waveform(s)
 VI executes whenever any waveform returns data, and the VI returns data from only that
 waveform. You can identify which waveform the data came from during a particular execution
 using the Data reference element that the VI returns in a cluster output called Properties.
 Compare the Data reference to the data references you generated before you opened the
 waveform session.

#### Calculating the Start Time of a Read Operation

When you read from a
 waveform with the Read Waveform(s) VI, the VI returns a cluster that includes a t0 at start
 element. t0 at start is the start time of the first sample in the waveform, not the start
 time of the first sample in the current array of read values. You can calculate the start
 time of the first sample read during a particular read operation using the following
 equation:

```text
current t0 = t0 at start + (dt * offset from start (samples))
  where  t0 at start is the start time of the first sample in the waveform, 
         dt is the time between samples, and 
         offset from start (samples) is the number of samples by which the first sample in the array of read values is offset from the first sample in the waveform. 
```

Note

Parent topic:

Reading and Writing Waveforms in the Custom Device Engine

<!--NI_TOPIC bundle=veristand path=custom-device-read-write-waveform.html language=enus -->
## TOPIC 00159: Reading and Writing Waveforms in the Custom Device Engine

- bundle_id: `veristand`
- source_path: `custom-device-read-write-waveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-read-write-waveform.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use waveforms in custom devices to publish waveform data or read waveform data from other sources in the VeriStand Engine. Before you begin, add a waveform to your custom device. Open your waveform custom device in LabVIEW. Use the VIs on the Waveform Data palette to open a write session to the wave

### Reading and Writing Waveforms in the Custom
 Device Engine

Use waveforms in custom devices to publish waveform data or
 read waveform data from other sources in the VeriStand Engine.

Before you begin, add a
 waveform to your custom device.

1. Open your waveform custom device in LabVIEW.
2. Use the VIs on the Waveform Data palette to open a write
 session to the waveform in the RT Driver VI of your custom
 device. 
 VI
DescriptionGet Waveform Data Reference
Generates a data reference to a specific
 waveform. If you want to write multiple waveforms,
 call this VI once per waveform and build an array
 of data references.
Open Waveform Session
Opens a write session for one or multiple
 waveforms. You should specify the delta t (dt), or
 time interval in seconds between any two points in
 the signal. For example, the dt of a 10 kHz
 waveform is 0.0001 seconds.
Start Waveform(s)
Provides a start time (t0) that defines
 when the first sample is written. Readers of the
 waveform in the VeriStand Engine and on the host
 computer will receive this value. If you want to
 read data from another waveform or from the DAQmx
 API, the t0 is provided. However, if you want to
 read waveform data from an FPGA, you must
 calculate the t0 yourself.
Write Waveform(s)
Writes an array of waveform samples. Call
 this VI repeatedly as you generate data for the
 waveform. You can write as much or as little data
 at a time as you want. If you opened a write
 session for multiple waveforms, this VI writes to
 each waveform simultaneously.
Close Waveform Session
Closes the write session.
3. Use the VIs on the Waveform Data palette to implement a read
 session from the waveform in the RT Driver VI of your custom
 device. 
 VI
DescriptionGet Waveform Data Reference
Generates a data reference to a specific
 waveform. If you want to read multiple waveforms,
 call this VI once per waveform and build an array
 of data references.
Open Waveform Session
Opens a read streaming session for one or
 multiple waveforms.
Read Waveform(s)
Returns an array of values from the waveform
 whenever any waveform source publishes data. Call
 this VI repeatedly to read data as it is
 published.
Close Waveform Session
Closes the waveform streaming session.

labview\examples\NI
 Veristand\Custom Devices\Waveform Analysis and Generation

Waveform Analysis and Generation Custom Device
 Project.lvproj

After you have set up your custom device, review
 the other considerations for reading and writing waveforms in a
 custom device engine.

Parent topic:

Implementing a Custom Device

Related concepts:

- Other Considerations for Reading and Writing Waveforms in a Custom Device Engine

Related tasks:

- Adding Custom Device Channels and Waveforms

<!--NI_TOPIC bundle=veristand path=custom-device-sync-asynchronous.html language=enus -->
## TOPIC 00160: Synchronizing an Asynchronous Custom Device with the Primary Control Loop

- bundle_id: `veristand`
- source_path: `custom-device-sync-asynchronous.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-sync-asynchronous.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure an asynchronous custom device to run synchronously with VeriStand by configuring the custom device to use the same timing source as the Primary Control Loop (PCL). Before you begin, you should understand asynchronous custom devices and the VeriStand Engine. VeriStand can use a DAQ device a

### Synchronizing an Asynchronous Custom Device
 with the Primary Control Loop

Configure an asynchronous custom device to run synchronously with
 VeriStand by configuring the custom device to use the same timing source as the Primary
 Control Loop (PCL).

Before you begin, you should understand asynchronous custom devices and the VeriStand Engine.

VeriStand can use a DAQ device as the timing source for the PCL. You can
 configure the RT Driver VI of your asynchronous custom device to use
 the same timing source.

When you synchronize your custom device to the PCL, your custom device
 will not delay PCL if it finishes late.

1. Set up an asynchronous custom
 device.
2. Modify the following code to add and configure the Set Loop
 Type VI in the Initialization VI. 
 You can add and configure the Set Loop Type VI in any VI
 for configuring the custom device, such as a page
 VI. For example, if you want a user to be able to
 specify whether or not to synchronize the custom
 device to the PCL, you could add and configure the
 Set Loop Type VI in the Main Page VI of the custom
 device.
 
[IMAGE alt='image' src='GUID-C03FBE23-58B8-4FF2-8131-FD1DE6ACB7FF-a5.gif'] 

1
Loop type—Specifies that
 the custom device will use a Timed Loop.
2
Set Loop Type VI—When Use
 Device Clock (Timed Loops only) input is True,
 VeriStand passes the timing source from the PCL to
 the Device Clock control in the RT Driver
 VI.
3. Modify the following code to configure the RT Driver VI to use
 the PCL Timing Source. 
 Before configuring your asynchronous RT Driver VI you must
 change the device's Data Loop from the default While Loop to
 a Timed Loop. You can do this by right-clicking the While
 Loop and selecting Replace with Timed
 Loop. 
 [IMAGE alt='image' src='GUID-FD589D04-69A9-430E-9583-29C89A29F7B2-a5.gif'] 

1
Device Clock—Specifies the
 name of a timing source that is ticked for every
 iteration of the PCL after the Custom Device FIFOs
 have been updated. VeriStand passes this timing
 source to the custom device. By wiring Device
 Clock to Source Name, the Timed Loop will run
 according to the same timing source as the PCL.
2
Get Custom Device Decimation
 VI—Returns the decimation factor of the custom
 device, or how many iterations of the PCL occur
 between calls to the custom device. This
 decimation factor serves as the Period of the Data
 Loop Timed Loop. The default value, 1, specifies
 no decimation, meaning the PCL will call the
 custom device on every iteration.
This configuration allows you to use the Set
 Custom Device Decimation VI in one of the VIs for
 configuring your custom device, such as
 Initialization VI or a page VI, to specify a
 decimation. Note For
 asynchronous custom devices, the decimation only
 affects when the Primary Control Loop reads and
 writes the FIFOs it uses to communicate with the
 custom device.
3
Get Asynchronous Driver VI Timed Loop
 Name VI—Returns the System
 Explorer path to the custom device as a
 string. This string serves as the unique Structure
 Name of the Data Loop Timed Loop, ensuring the
 VeriStand Engine synchronizes the start of this
 Timed Loop with the start of the PCL.
4
Get Timed Loop Priority
 VI—Outputs the priority of the Timed Loop. The
 priority can be low, medium, or high.
5
Convert Timed Loop Priority
 VI—Converts this enumeration value to a numeric
 value that the Priority terminal of the Timed Loop
 input node accepts.

Parent topic:

Implementing a Custom Device

Related concepts:

- Asynchronous Custom Devices
- VeriStand Engine

Related tasks:

- Using the Asynchronous Custom Device Driver Template

<!--NI_TOPIC bundle=veristand path=custom-device-timing-sync.html language=enus -->
## TOPIC 00161: Timing and Sync Custom Devices

- bundle_id: `veristand`
- source_path: `custom-device-timing-sync.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-timing-sync.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A timing and sync custom device is any device that has the capability to drive the RTSI 0 line to serve as the chassis master hardware synchronization device for a system. The RTSI 0 line is a digital line that sends a clock signal to synchronize all hardware I/O devices in the system. You can plan

### Timing and Sync Custom Devices

A *timing and sync* custom device is any device that has the capability to
 drive the RTSI 0 line to serve as the chassis master hardware synchronization device for a
 system.

The *RTSI 0 line* is a digital line that sends a clock signal to synchronize
 all hardware I/O devices in the system. You can plan and build a timing and sync custom
 device from a LabVIEW project. You must modify the VIs of the project to conform to the
 custom device
 framework and build the device for distribution to VeriStand.

When you distribute the device, operators can add the device to VeriStand by copying the
 contents of the Build directory you create into the
 <Common Data>\Timing and Sync directory on their host
 computer. VeriStand parses this directory for timing and sync devices when it launches.

After an operator has added the custom timing and sync device to the directory, they can
 add the device
 to the system definition file and configure the device as the chassis master
 hardware synchronization device. Timing and sync devices appear in System
 Explorer under Hardware»Chassis»Timing and Sync.

Parent topic:

Custom Device Types

Related concepts:

- Custom Device Framework

Related tasks:

- Adding and Configuring Timing and Sync Devices

<!--NI_TOPIC bundle=veristand path=custom-device-types.html language=enus -->
## TOPIC 00162: Custom Device Types

- bundle_id: `veristand`
- source_path: `custom-device-types.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-types.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The type of a custom device refers to its execution mode, which defines how the device interacts with the VeriStand Engine. Depending on your requirements, you can create custom devices that run inline or in parallel with the Primary Control Loop (PCL). You also can create timing and sync devices. T

### Custom Device Types

The type of a custom device refers to its execution mode, which defines how the device
 interacts with the VeriStand Engine.

Depending on your requirements, you can create custom devices that run inline or in
 parallel with the Primary Control Loop (PCL). You also can create timing and sync devices.

Note

System Explorer

Hardware

»

Chassis

»

Timing and Sync

The following table displays the pre-defined custom device types that are included in
 VeriStand.

| Device type | Basic architecture | Data interface | Timing | Benefits | Caveats | Use cases |
| --- | --- | --- | --- | --- | --- | --- |
| Asynchronous | Two loops, one for receiving commands and one for data transfer | FIFOs | Variable | Unlikely to affect timing of the rest of the VeriStand system, can run faster or slower than the PCL | 1-cycle latency due to FIFOs | Shared resources, background processes, non-deterministic hardware/protocols, system health monitoring, logging, offline analysis |
| Inline Hardware Interface | State machine with two-phase execution | Channel references | Inline | Sends data to engine before other components execute, receives data from engine after other components execute | Can adversely affect PCL timing | Most hardware, deterministic operation, two-phase operations (for example, stimulus-response) |
| Inline Model Interface | State machine with one-phase execution | Channel references | Inline | Sends data to engine with low latency | Can adversely affect PCL timing | Low latency calculations, such as PID, interpolation, and so on |
| Inline Timing and Sync | State machine with two-phase execution | Channel references | Inline | Same as Inline Hardware Interface, can function as hardware synchronization master device to drive RTSI 0 line | Can adversely affect PCL timing | Inline hardware synchronization master device |
| Asynchronous Timing and Sync | Single loop | FIFOs | Variable | Same as Asynchronous, but can function as hardware synchronization master device to drive RTSI 0 line | 1-cycle latency due to FIFOs | Asynchronous hardware synchronization master device |

Note

#### Custom Device Type Selection

Choose the
 type of custom device that most closely resembles the functionality you want to
 configure. For example, if you want to read and write data to and from a hardware
 device at the same rate as the PCL, select an inline hardware interface custom
 device type. However, if you have a serial hardware device, you should select an
 asynchronous custom device, as serial devices are slow and could affect the PCL
 timing. Understanding the execution steps of the PCL also can help you select the
 appropriate custom device type.

Note

#### Custom Device Type Configuration

You
 configure the custom device type by selecting the appropriate template VI from the
 Custom
 Device API library. The type of custom device you select will determine
 the architecture of the RT Driver VI, but the VIs for configuring the custom device
 remain the same across all types.

A custom device is not limited to a single
 device type, and you can alter the code in the template VIs to fit your needs. For
 example, you can create both inline and asynchronous engines for the same custom
 device, and use the Set Custom Device Drivers VI to switch between them. However,
 you must maintain the connector pane, controls, and indicators that the tool and
 templates include to ensure correct interaction with VeriStand.

Parent topic:

Planning a Custom Device

Related concepts:

- Primary Control Loop Execution Steps
- Asynchronous Custom Devices
- Inline Hardware Interface Custom Devices
- Inline Model Interface Custom Devices
- Timing and Sync Custom Devices
- Inline Custom Devices with Asynchronous Loops
- Custom Device API Library

<!--NI_TOPIC bundle=veristand path=custom-device-xml-element-types.html language=enus -->
## TOPIC 00163: Custom Device Non-Standard XML Element Types

- bundle_id: `veristand`
- source_path: `custom-device-xml-element-types.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-xml-element-types.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Non-standard element types are defined in the Custom Device.xsd schema. DependencyThe Dependency element type describes a dependency of the custom device, such as a DLL or VI, that the custom device requires and that you want to deploy to the target with the custom device. Element Required? Element

### Custom Device Non-Standard XML Element
 Types

Non-standard element types are defined in the Custom Device.xsd
 schema.

#### Dependency

The *Dependency*
 element type describes a dependency of the custom device, such as a DLL or VI, that
 the custom device requires and that you want to deploy to the target with the custom
 device.

| Element | Required? | Element type | Min/Max Occurrences | Description |
| --- | --- | --- | --- | --- |
| <Type> | Yes | xs:string | 1/1 | Specifies if the path you specify is relative or absolute. Valid values are Absolute, To Base, To Common Doc Dir, or To Application Data Dir. |
| <Path> | Yes | xs:string | 1/1 | Specifies the path to the dependency on the host computer. |
| <Behavior> | No | xs:string | 0/1 | Specifies whether the path is Static or Dynamic. |

#### LocString

The *LocString*
 element type specifies English and localized strings to display in menu items.

| Element | Required? | Element type | Min/Max Occurrences | Description |
| --- | --- | --- | --- | --- |
| <eng> | Yes | xs:string | 1/1 | VeriStand does not currently use this string. The <loc> string appears in the shortcut menu. |
| <loc> | Yes | xs:string | 1/1 | Specifies a string for a custom shortcut menu. You can use two colons (::) to separate elements and create nested menu items. |

#### Path

The *Path* element type
 describes a path to a file and whether the path is relative or absolute.

| Element | Required? | Element type | Min/Max Occurrences | Description |
| --- | --- | --- | --- | --- |
| <Type> | Yes | xs:string | 1/1 | Specifies whether the path you specify is relative or absolute. Valid values are Absolute, To Base, To Common Doc Dir, or To Application Data Dir. |
| <Path> | Yes | xs:string | 1/1 | Specifies the path to the file. |

#### Target

The Target
 element type describes the target to which you want to deploy the custom
 device.

| Element type | Enumerations |
| --- | --- |
| xs:string | All Windows Linux_x64 |

#### VersionType

The *VersionType*
 element type specifies version information.

| Attribute | Required? | Attribute type |
| --- | --- | --- |
| Major | Yes | xs:unsignedInt |
| Minor | Yes | xs:unsignedInt |
| Fix | Yes | xs:unsignedInt |
| Build | Yes | xs:unsignedInt |

Parent topic:

Custom Device XML File

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=custom-device-xml-tags.html language=enus -->
## TOPIC 00164: Custom Device XML Tags

- bundle_id: `veristand`
- source_path: `custom-device-xml-tags.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-xml-tags.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: XML tags define settings for a custom device. These elements, and non-standard element types, are defined in the Custom Device.xsd schema located in the <Common Data>\Custom Devices directory. You can open the file in an XML or text editor to read the schema and view the hierarchy. For an example of

### Custom Device XML Tags

XML tags define settings for a custom device.

Custom Device.xsd

\Custom Devices

Caution

The following table
 displays the XML tags you can use in a custom device XML file.

| Element | Required? | Element type | Min/Max occurrences | Description |
| --- | --- | --- | --- | --- |
| <CustomDevice> | Yes | complex | 1/1 | Opening tag for a custom device definition. |
| <XSDVersion> | No | VersionType | 0/1 | Specifies the version of the Custom Device.xsd file the XML is using. The version must match the version of VeriStand you are using. |
| >> <AddMenu> | Yes | LocString | 1/1 | Specifies the device name to display in the shortcut menu when an operator right-clicks the Custom Devices node in System Explorer. |
| >> <Dependency> | No | Dependency | 0/1 | Specifies the path to a dependency file, such as a DLL or VI, that the custom device requires and that you want to deploy to the target along with the custom device. |
| >> <Version> | Yes | xs:string | 1/1 | Specifies version information for the custom device. |
| >> <Type> | Yes | xs:string | 1/1 | Specifies the device type or execution mode of the custom device: Asynchronous Inline HW Interface Inline Model Interface Inline Timing and Sync Asynchronous Timing and Sync |
| >> <MaxOccurrence> | Yes | xs:int | 1/1 | Specifies the maximum number of instances of the custom device to allow in a system definition file. |
| >> <MainPageGUID> | Yes | xs:string | 1/1 | Specifies the GUID of the configuration page to associate with the top-level custom device item. |
| >> <TimingSource> | No | complex | 0/1 | Configures a custom timing source for the Primary Control Loop. |
| >>> <HasTimingSourceCapability> | Yes* | xs:boolean | 1/1 | Enables or disables the use of the timing source VI you specify as the timing source for the Primary Control Loop. |
| >>> <Paths> | No | complex | 1/1 | These elements are obsolete. Use <SourceDistribution> instead. |
| >>>> <Source> | Yes* | Path | 1/1 |  |
| >>>> <RealTimeSystemDestination> | Yes* | xs:string | 1/1 |  |
| >>> <SourceDistribution> | No | complex | 0/1 | Contains information about the source distribution for the timing source VI. |
| >>>> <Source> | Yes* | complex | 1/unbounded | Contains information about the files in the source distribution. |
| >>>>> <SupportedTarget> | Yes* | Target | 1/unbounded | Specifies the target operating system(s) on which the custom device runs. |
| >>>>> <Location> | Yes* | Path | 1/1 | Specifies the location of the timing source VI on the host computer. |
| >>>>> <RealTimeSystemDestination> | Yes* | xs:string | 1/1 | Specifies the destination path for the timing source VI on the target. |
| >>>>> <Version> | No | xs:string | 0/1 | Specifies version information for the source distribution. |
| >> <InitializationVI> | Yes | complex | 1/1 | Contains information about the Initialization VI that runs when you add the custom device to the system definition file. |
| >>> <Type> | Yes | xs:string | 1/1 | Specifies how the VI runs: Action—Specifies that the VI runs silently in the background. VI—Specifies that the VI runs in an interactive mode with the front panel visible. |
| >>> <Execution> | No | xs:string | 1/1 | Specifies additional information about the execution of the VI: Silent—Specifies that the VI runs silently in the background. Modal—Specifies that the VI runs in a modal window. Floating—Specifies that the VI runs in a floating window. Default—Specifies that the VI runs in the default mode for the <Type> you specify. |
| >>> <Position> | No | xs:string | 1/1 | Specifies where to position the front panel window, if displayed, on VI launch: Centered—Specifies to center the window on the default monitor. Mouse pointer—Specifies to position the origin of the window on the mouse pointer. |
| >>> <Item2Launch> | Yes | Path | 1/1 | Specifies the VI to launch as the Initialization VI. |
| >> <CustomDeviceVI> | Yes | complex | 1/1 | Contains information about the RT Driver VI that runs on the target. |
| >>> <Source> | No | Path | 0/1 | These elements are obsolete. Use <SourceDistribution> instead. |
| >>> <RealTimeSystemDestination> | No | xs:string | 0/1 |  |
| >>> <SourceDistribution> | No | complex | 0/1 | Contains information about the source distribution for the RT driver VI. |
| >>>> <Source> | Yes* | complex | 1/unbounded | Contains information about the files in the source distribution. |
| >>>>> <SupportedTarget> | Yes* | Target | 1/unbounded | Specifies the target operating system(s) on which the custom device runs. |
| >>>>> <Source> | Yes* | Path | 1/1 | Specifies the location of the RT driver VI on the host computer. |
| >>>>> <RealTimeSystemDestination> | Yes* | xs:string | 1/1 | Specifies the destination path for the RT driver VI on the target. |
| >> <Dependencies> | Yes | complex | 1/1 | Contains information about dependencies of the custom device. |
| >>> <Dependency> | No | complex | 0/unbounded | Contains information about a specific dependency. |
| >>>> <SupportedTarget> | No | Target | 0/1 | Specifies the target operating system(s) on which the custom device runs. |
| >>>> <Source> | Yes* | Path | 1/1 | Specifies the location of the dependency on the host computer. |
| >>>> <RealTimeSystemDestination> | Yes* | xs:string | 1/1 | Specifies the destination path for the dependency on the target. |
| >>>> <ForceDownload> | No | xs:boolean | 0/1 | Specifies whether to force the download of the dependency. |
| >>>> <Version> | No | xs:string | 0/1 | Specifies version information for the dependency. |
| >> <Pages> | Yes | complex | 1/1 | Contains information about System Explorer configuration pages associated with the custom device. |
| >>> <Page> | Yes | complex | 1/unbounded | Contains information about a specific page. |
| >>>> <Name> | Yes | LocString | 1/1 | Specifies the name of the page. |
| >>>> <DisallowRenaming> | No | xs:boolean | 0/1 | Disallows renaming of the item with which the page is associated. |
| >>>> <DeleteProtection> | No | xs:boolean | 0/1 | Disallows deleting the item with which the page is associated. |
| >>>> <AllowMultiSelection> | No | xs:boolean | 0/1 | Allows an operator to select the item with which the page is associated during a multi-select operation. |
| >>>> <ExcludeFromAlphabeticalOrder> | No | xs:boolean | 0/1 | Excludes a page's children from any alphabetical sorting operations. |
| >>>> <Copy> | No | xs:string | 0/1 | Configures copying of the item: Copy—Enables copying. Disabled—Disables copying. |
| >>>> <Paste> | No | xs:string | 0/1 | Configures pasting of the item: Create—Pastes by creating a new instance of the item. CreateIfNotExists_GUID—Pastes only if an item with the same GUID does not already exist. CreateIfNotExists_Name—Pastes only if an item with the same name does not already exist. Replace—Pastes by replacing an item. Dialog—Prompts the operator with a dialog before pasting. |
| >>>> <ParentGUIDs> | No | complex | 0/1 | Contains information about the GUIDs of possible parent items. When <Paste> is CreateIfNotExists_GUID, VeriStand checks any GUIDs listed here in addition to the page GUID. |
| >>>>> <ParentGUID> | No | xs:string | 0/unbounded | Specifies the GUID of a parent item. |
| >>>> <GUID> | Yes | xs:string | 1/1 | Specifies the page GUID. |
| >>>> <Glyph> | Yes | Path | 1/1 | Specifies the default icon that appears next to the item in System Explorer. |
| >>>> <InactiveGlyph> | No | Path | 0/1 | Specifies the icon that appears next to the item in System Explorer when the item is inactive. |
| >>>> <BrokenGlyph> | No | Path | 0/1 | Specifies the icon that appears next to the item in System Explorer when the item is broken. |
| >>>> <Item2Launch> | Yes | Path | 1/1 | Specifies the VI to launch as the page. |
| >>>> <RunTimeMenu> | No | complex | 0/1 | Contains information about the shortcut menu an operator can access by right-clicking the item at run time. |
| >>>>> <MenuItem> | Yes* | complex | 1/unbounded | Contains information about a specific shortcut menu item. |
| >>>>>> <GUID> | Yes* | xs:string | 1/1 | Specifies the GUID for the menu item. |
| >>>>>> <Type> | Yes* | xs:string | 1/1 | Specifies the type of the menu item: Action—Specifies that the item launches a VI that runs silently in the background. VI—Specifies that the item launches a VI and displays the front panel so the operator can interact with the VI. Separator—Specifies that the item is a menu separator. Custom—Specifies that the menu item has a custom type. |
| >>>>>> <Execution> | No | xs:string | 0/1 | Specifies additional information about the execution of the VI associated with the menu item. Silent—Specifies that the VI runs silently in the background. Modal—Specifies that the VI runs in a modal window. Floating—Specifies that the VI runs in a floating window. Default—Specifies that the VI runs in the default mode for the <Type> you specify. |
| >>>>>> <Position> | No | xs:string | 0/1 | Specifies where to position the front panel window, if displayed, on VI launch. Centered—Specifies to center the window on the default monitor. Mouse pointer—Specifies to position the origin of the window on the mouse pointer. |
| >>>>>> <Behavior> | No | xs:string | 0/1 | Specifies whether the menu item does nothing (None) or launches a VI (OpenFrontPanel). |
| >>>>>> <MinNrOfChilds> | No | xs:int | 0/1 | Specifies a minimum number of children for the menu item. |
| >>>>>> <Name> | Yes* | LocString | 1/1 | Specifies the name of the menu item. |
| >>>>>> <Item2Launch> | Yes* | Path | 1/1 | Specifies the VI to launch when an operator selects the menu item. |
| >>>>>> <Dependency> | No | Dependency | 0/1 | Specifies the path to a dependency file. |
| >>>>>> <CustomPopulation> | No | Path | 0/1 | Specifies a file to associate with the menu item if <Type> is Custom. |
| >>>> <ButtonList> | No | complex | 0/1 | Contains information about buttons that appear in the System Explorer when an operator displays the page. |
| >>>>> <Button> | Yes* | complex | 1/unbounded | Contains information about a specific button. |
| >>>>>> <ID> | Yes* | xs:string | 1/1 | Specifies a unique ID to associate with the button. |
| >>>>>> <Glyph> | Yes* | Path | 1/1 | Specifies the icon that appears on the button. |
| >>>>>> <Type> | No | xs:string | 0/1 | Specifies the type of the button: Action—Specifies that the item launches a VI that runs silently in the background. Dialog—Specifies that the button displays a dialog with which the operator can interact. Page—Specifies that the button displays a new configuration page. Notification—Specifies that the button sends a notification to the currently loaded configuration page. This option passes the button ID to the page. Separator—Specifies that the button is actually a separator on the button toolbar. |
| >>>>>> <ReferencedGUID> | Yes | xs:string | 0/1 | Specifies a GUID to reference when an operator clicks the button. |
| >>>>>> <ButtonText> | No | LocString | 0/1 | Specifies text to display on the button. |
| >>>>>> <Caption> | Yes* | LocString | 1/1 | Specifies a caption for the button. Captions appear in Context Help. |
| >>>>>> <TipStrip> | Yes* | LocString | 1/1 | Specifies a tip to display when an operator hovers over the button. |
| >>>>>> <Documentation> | Yes* | LocString | 1/1 | Specifies the description that appears in Context Help. |
| >>>>>> <Dependency> | No | Dependency | 0/1 | Specifies the path to a dependency file. |
| >>>> <ActionVIOnDelete> | No | Path | 0/1 | Specifies a VI to run when an operator deletes the item associated with the page from System Explorer. |
| >>>> <ActionVIOnLoad> | No | Path | 0/1 | Specifies a VI to run when VeriStand loads the item associated with the page. |
| >>>> <ActionVIOnSystemShutdown> | No | Path | 0/1 | Specifies a VI to run when VeriStand shuts down. |
| >>>> <ActionVIOnSave> | No | Path | 0/1 | Specifies a VI to run when an operator saves the system definition file. |
| >>>> <ActionVIOnDownload> | No | Path | 0/1 | Specifies a VI to run when an operator downloads the custom device to the target. |
| >>>> <ActionVIOnPaste> | No | Path | 0/1 | Specifies a VI to run when an operator pastes the item associated with the page. |
| >>>> <ActionVIOnTargetTypeChange> | No | Path | 0/1 | Specifies a VI to run when an operator changes the type of target on which the custom device runs. |
| >>>> <ActionVIOnDeleteRequest> | No | Path | 0/1 | Specifies a VI to run when a delete request is received for the item associated with the page. |
| >>>> <ActionVIOnCompile> | No | Path | 0/1 | Specifies a VI to run when the item associated with the page is compiled. |
| >>>> <Help> | No | complex | 0/1 | Contains information about help content for the item associated with the page. |
| >>>>> <Item2Launch> | Yes* | Path | 1/1 | Specifies the file to launch when an operator selects the Help option for the item. |
| >>>>> <FileType> | Yes* | xs:string | 1/1 | Specifies the help file type. Valid values are chm or other. |
| >>>>> <Section> | No | xs:string | 0/1 | Specifies a section of the help file to display when an operator selects the Help option. |
| >>>> <AdditionalInformation> | No | xs:string | 0/1 | Specifies additional information to store with the item. |
| >> <CustomXML> | No | xs:string | 0/1 | Contains custom XML that you add to the file. Code you enter between <CustomXML> tags is not validated against the Custom Device.xsd file. |
| *Required sub-tags of optional parent tags are only required if you use the parent tag. |  |  |  |  |

Parent topic:

Custom Device XML File

Related concepts:

- Custom Device Types

Related reference:

- Custom Device Non-Standard XML Element Types
- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=custom-device-xml.html language=enus -->
## TOPIC 00165: Custom Device XML File

- bundle_id: `veristand`
- source_path: `custom-device-xml.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-device-xml.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Custom Device XML file enables you to define parts of the custom device in System Explorer, specify which VIs to call, and select the dependencies to deploy to an RT target. When VeriStand launches, it uses the Custom Device XML file in the <Common Data>\Custom Devices directory to determine how

### Custom Device XML File

The *Custom Device XML file* enables you to define parts of the
 custom device in System Explorer, specify which VIs to call, and
 select the dependencies to deploy to an RT target.

When VeriStand launches, it uses the Custom Device XML file in the <Common
 Data>\Custom Devices directory to determine how to
 load, configure, display, and run custom devices. This XML file provides basic
 information about a custom device, including the type of custom device, paths to its VIs
 and dependencies, and pages, glyphs, buttons, and menu
 items associated with the custom device.

- Custom Device <Device Name>.xml
- SLSC Module <Device Name>.xml
- Timing and Sync <Device Name>.xml

Note

<Common Data>\Custom Devices

Caution

Parent topic:

Custom Device Framework

Related concepts:

- Custom Device Types

Related tasks:

- Adding Custom Glyphs, Shortcut Menus, and Toolbar Buttons

Related reference:

- VeriStand Directories and Aliases
- Custom Device XML Tags

<!--NI_TOPIC bundle=veristand path=custom-devices-asynchronous.html language=enus -->
## TOPIC 00166: Asynchronous Custom Devices

- bundle_id: `veristand`
- source_path: `custom-devices-asynchronous.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-devices-asynchronous.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An asynchronous custom device executes in a parallel loop with the VeriStand Engine's Primary Control Loop (PCL) and uses RT FIFOs to exchange channel data with the rest of VeriStand. You can create a standard asynchronous custom device from a template in the Custom Device API library. This also app

### Asynchronous Custom Devices

An *asynchronous* custom device executes in a parallel loop with the VeriStand
 Engine's Primary Control Loop (PCL) and uses RT FIFOs to exchange channel data with the rest
 of VeriStand.

You can create a
 standard asynchronous custom device from a template in the
 Custom Device API library. This also applies to the
 Asynchronous Timing and Sync device type, which is an asynchronous device
 that you add to the system definition file as a timing and sync device.

#### Timing of an Asynchronous Custom
 Device

The rate at which an asynchronous custom device
 executes depends on how you configure it. By default, the
 asynchronous custom device RT Driver VI template uses a While Loop,
 meaning your asynchronous custom device will execute as fast as
 possible. You can change the default While Loop to a Timed Loop, and
 then configure the Timed Loop to use a specific timing source, such
 as the timing source for a hardware device.

You can
 synchronize an asynchronous custom device with the Primary Control
 Loop by using the Device Clock control as the timing source of your
 Timed Loop. *Device Clock* is a timing sourced ticked for
 every iteration of the Primary Control Loop after custom device
 FIFOs have been updated. If you synchronize your device with the
 PCL, the dt of your Timed Loop will be in ticks of the PCL. So if
 you set the dt as 3, your Timed Loop will execute every 3 ticks of
 the PCL.

#### Decimation of an Asynchronous Custom
 Device

You can use Set Custom Device Decimation VI in the initialization
 code of your asynchronous custom device to change the decimation rate of your
 device. In an asynchronous custom device, the decimation affects when the Primary
 Control Loop reads and writes the FIFOs it uses to communicate with the custom
 device. For example, if you set the Decimation parameter of Set Custom Device
 Decimation VI to 4, the Primary Control Loop reads and writes the FIFOs on every
 fourth iteration.

#### Latency Due to FIFOs in Asynchronous Custom
 Device

Because asynchronous devices run in parallel with the PCL and pass
 channel data via RT FIFOs, there is a minimum of one cycle delay from when data
 leaves the PCL and when it enters the custom device, and vice versa. Additionally,
 asynchronous devices might not always execute at the same time with respect to the
 other components of the VeriStand. For example, the first iteration might execute
 before the PCL processes alarms, the second and third iterations after, and so
 on.

Parent topic:

Custom Device Types

<!--NI_TOPIC bundle=veristand path=custom-fpga-vi.html language=enus -->
## TOPIC 00167: Customizing an FPGA VI

- bundle_id: `veristand`
- source_path: `custom-fpga-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/custom-fpga-vi.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify an FPGA VI to match your hardware device. Before you begin, copy a sample FPGA VI and project and learn about FPGA customization guidelines and defaults. Open the FPGA VI in LabVIEW. Add or remove FPGA I/O items depending on the device and the needs of the project. By default, the sample FPGA

### Customizing an FPGA VI

Modify an FPGA VI to match your hardware device.

Before you begin, copy a sample FPGA VI and project
 and learn about FPGA
 customization guidelines and defaults.

1. Open the FPGA VI in LabVIEW.
2. Add or remove FPGA I/O items depending on the device and the needs of the
 project. 
 By default, the sample FPGA VI only uses the first 40 lines on connectors 1 and 2. You
 can add more FPGA I/O items to this project if you want to expose addition I/O lines on
 your target. Note For FPGA targets with
 no analog inputs or outputs, you can remove the analog I/O items from the project and
 the corresponding FPGA I/O Nodes from the FPGA VI.
Similarly, the default sample FPGA VI defines the digital lines on connector 0 as 8 PWM
 inputs and 8 PWM outputs. You may need more or fewer PWM channels. You can add other
 custom I/O not defined in the sample FPGA VI.
3. Optional: 
 If the FPGA VI displays broken wires to FPGA I/O nodes, update the corresponding I/O
 nodes with the correct pins available on the target.
4. Optional: 
 If the number of packets in either the DMA_READ or DMA_WRITE FIFO is greater than 15,
 update the FIFO size.
  1. In Project Explorer window, right-click a FIFO I/O item and
 select Properties.
  2. In the FPGA FIFO Properties dialog box under General, change
 the Number of Elements, and click
 OK.
5. Save the FPGA VI.

After customizing the FPGA VI, compile the VI into a
 bitfile.

Parent topic:

Customizing an FPGA Target

Related concepts:

- FPGA VI Customization Guidelines and Defaults

Related tasks:

- Copying the Sample FPGA VI and Project
- Compiling a Custom FPGA VI into a Bitfile

<!--NI_TOPIC bundle=veristand path=cutomize-test-results.html language=enus -->
## TOPIC 00168: Customizing ATML Test Result Appearance

- bundle_id: `veristand`
- source_path: `cutomize-test-results.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/cutomize-test-results.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Switch and edit style sheets to change the ATML report's fonts, colors, tables, and more when it appears in a web browser or external viewer application. When VeriStand finishes executing a real-time sequence, it generates an XML report that conforms to the approved version of the Test Results and S

### Customizing ATML Test Result
 Appearance

Switch and edit style sheets to change the ATML report's fonts, colors, tables, and more
 when it appears in a web browser or external viewer application.

<Application
 Data>VeriStand\Data Storage\ATML

- TRML.xsl —Displays reports in a vertical, tabular, indented
 format with data for each step in multiple rows. This is the default style
 sheet.
- TR_Horizontal.xsl —Displays reports in a concise tabular
 format with expand and collapse sections.

To switch between these style sheets, use the following
 steps.

1. In the <Application Data>\NI VeriStand\Data Storage\ATML
 directory, copy the TR_Horizontal.xsl and paste it in the same
 directory as the XML report.
2. Open the XML report in a text editor.
3. At the top of the XML report, change the code that reads
 <?xml-stylesheet type="text/xsl" href="TRML.xsl"?> to
 <?xml-stylesheet type="text/xsl"
 href="TR_Horizontal.xsl"?>.
4. Save the XML report.

Open the XML report in a web browser to view the changes.

You can edit the style sheet in a
 text editor to further modify the report's appearance.

Parent topic:

Viewing Stimulus Profile Test Results

<!--NI_TOPIC bundle=veristand path=daq-device-channel-properties.html language=enus -->
## TOPIC 00169: Adding and Configuring DAQ Device Channels

- bundle_id: `veristand`
- source_path: `daq-device-channel-properties.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/daq-device-channel-properties.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Define how VeriStand performs measurements using DAQ channels. Before you begin, add a DAQ device. Each measurement type has configurable properties. For example, counter input channels that count up have a count edge property that sets whether the channel counts rising edges or falling edges. Some

### Adding and Configuring DAQ Device
 Channels

Define how VeriStand performs measurements using DAQ channels.

Before you begin, add a DAQ device.

Note

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
4. Right-click a DAQ device and click Add Channels.
5. Determine the channel type you want based on the measurement type. 
 Measurement type
Channel typeAccelerometer
Bridge
Current
Force
Pressure
Resistance Temperature Detector (RTD)
Strain
Thermistor Iex
Thermistor Vex
Thermocouple
Torque
Voltage
Analog Input (AI)
Current
Voltage
Analog Output (AO)
Digital
 Input
Digital Input (DI)
Digital
 Output
Digital Output (DO)
Count Up/Down
Frequency
Position
Pulse Measurement
Time Period
Counter Input (CI)
Pulse
 Generation
Counter Output (CO)
6. In the Add DAQ Channels dialog box, use the
 Select channel type to add pull-down to select the
 channel type.
7. Use the Select measurement type pull-down to select the
 measurement type.
8. Click Next.
9. Select the channel(s) you want to add and click Finish. 
 Note If the DAQ device does not
 contain channels of the type you specified, no channels are available to
 select.
10. Save the system definition file.

Parent topic:

Adding and Configuring a DAQ Device

Related tasks:

- Adding and Configuring a DAQ Device

Related reference:

- Accelerometer Channel Properties (AI)
- Bridge Channel Properties (AI)
- Current Channel Properties (AI)
- Force Channel Properties (AI)
- Pressure Channel Properties (AI)
- RTD Channel Properties (AI)
- Strain Channel Properties (AI)
- Thermistor Iex Channel Properties (AI)
- Thermistor Vex Channel Properties (AI)
- Thermocouple Channel Properties (AI)
- Torque Channel Properties (AI)
- Voltage Channel Properties (AI)
- Current Channel Properties (AO)
- Voltage Channel Properties (AO)
- Digital Input Channel Properties (DI)
- Digital Output Channel Properties (DO)
- Count Up/Count Down Channel Properties (CI)
- Frequency Channel Properties (CI)
- Position Channel Properties (CI)
- Pulse Measurement Channel Properties (CI)
- Time Period Channel Properties (CI)
- Pulse Generation Channel Properties (CO)

<!--NI_TOPIC bundle=veristand path=data-logging-options.html language=enus -->
## TOPIC 00170: Data Logging Options

- bundle_id: `veristand`
- source_path: `data-logging-options.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/data-logging-options.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Log data with tools such as the Embedded Data Logger, Stimulus Profile Editor, and DAQ devices. Use the following table to determine the best data logging option for your needs.If you need to log data from varying sources, use DIAdem to combine and time correlate all of your data logs. For more info

### Data Logging Options

Log data with tools such as the Embedded Data Logger, Stimulus
 Profile Editor, and DAQ devices.

Note

Viewing Time Correlated NI VeriStand Data
 Logs

| Option | Location | Rate | Strengths | Weaknesses | Use cases |
| --- | --- | --- | --- | --- | --- |
| Embedded Data Logger | Target | Medium | Adds structured metadata to your log files and allows you to organize logged channels in groups. Configures dynamic start and stop trigger conditions. By using the Embedded Data Logger via a channel in the system definition, you can trigger logging through mappings to outputs from models, real-time sequences, procedures, etc. Retains logging data if you lose connection to the target. | Limits logging rate to the rate of the PCL. Requires configuration of the Embedded Data Logger before deploying. You cannot change configuration at run time. | Log more data than the bandwidth of the connection between a host and target allows. Disconnect the host from the target after deploying a system definition and continue to log data. |
| NI-XNET Raw Frame Data Logging | Target | Logs as data arrives | Logs potentially at rates faster than the PCL. Allows you to specify whether to log all frames or specific frames by ID. Retains logging data if you lose connection to the target. Configures dynamic start and stop trigger conditions. As you can control when to start and stop NI-XNET raw frame data logging via a channel in the system definition, you can trigger logging through mappings to outputs from models, real-time sequences, procedures, etc. | Logs data in a low-level format, so you must perform post-processing of the data to covert it to readable units. Cannot change configuration at run time. | Log frame data during an NI-XNET session. |
| Logging waveform acquisition from a DAQ device | Target | High, potentially up to the rate the DAQ board can run. | Produces smaller log files. Log potentially at rates faster than the PCL. You will not lose logging data if you lose connection to the target. | Logs via waveforms, and you cannot scale or calibrate waveforms as you might channels. Limited start and stop trigger functionality. Cannot change configuration at run time. | Log waveform acquisitions from a DAQ device. |
| Logging with the Stimulus Profile Editor | Host | Medium | Allows advanced triggering functionality. Capture responses of your unit under test (UUT) to a real-time test. | Limited to logging results from tests you execute in the Stimulus Profile Editor. The host must be connected to the target to log. Logging bandwidth limited to the bandwidth of the connection between the host and the target. | Save the responses of a UUT to specific scenarios. |
| VeriStand Editor logging specification file | Host | Medium | Reconfigure your logging settings and add new specification files at run time. Provides dynamic configuration options. Automates post-processing of your log data. | Logging bandwidth limited to the bandwidth of the connection between the host and the target. The host must be connected to the target to log. | Configure and execute host-side data logging from the VeriStand Editor. Automate post-processing actions. |
| Data Logging workspace control | Host | Medium | Reconfigure logging settings at run time. Provides dynamic configuration options. Automates post-processing of your log data. | Logging bandwidth limited to the bandwidth of the connection between the host and the target. The host must be connected to the target to log. | Perform dynamic logging on a host. Record behaviors during a test without undeploying a system definition. |

Parent topic:

Running Tests

Related tasks:

- Logging Target Data with the Embedded Data Logger
- Logging Incoming NI-XNET Frames
- Setting Up Timing and Logging Properties for Waveform Acquisitions
- Logging Real-Time Test Data with the Stimulus Profile Editor
- Logging Data with the VeriStand Editor
- Configuring and Executing Host-Side Logging

Related information:

- Viewing Time Correlated NI VeriStand Data Logs

<!--NI_TOPIC bundle=veristand path=debug-system.html language=enus -->
## TOPIC 00171: Debugging the System

- bundle_id: `veristand`
- source_path: `debug-system.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/debug-system.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Remedy system-related issues. After receiving errors in VeriStand, you must resolve them to continue running the system.For more help debugging the system, refer to NI KnowledgeBase for help resolving the error.

### Debugging the System

Remedy system-related issues.

Note

NI KnowledgeBase

1. VeriStand Error Codes VeriStand returns an error code when it encounters a problem while executing.
2. Viewing Real-Time Target Logs Display and monitor logs from a real-time target.
3. Related Documentation Use the following documents for more help with VeriStand.
4. Maximizing System Performance Increase the efficiency of VeriStand by following best practices for your system definition, controllers, hardware, models, and reflective memory.

Related information:

- NI KnowledgeBase

<!--NI_TOPIC bundle=veristand path=declare-temporary-variables-model-parameter.html language=enus -->
## TOPIC 00172: Declaring Temporary Variables in a Model Parameter File

- bundle_id: `veristand`
- source_path: `declare-temporary-variables-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/declare-temporary-variables-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Declare temporary variables in a model parameter .txt file for reuse in parameter values and expressions in VeriStand. Before you begin, learn about the supported syntax for .txt files. Open a formatted .txt file. Create a new line for the temporary variable. Enter the temporary variable name in the

### Declaring Temporary Variables in a Model
 Parameter File

Declare temporary variables in a model parameter .txt file
 for reuse in parameter values and expressions in VeriStand.

.txt

1. Open a formatted .txt file.
2. Create a new line for the temporary variable.
3. Enter the temporary variable name in the parameter column and the variable value in the
 value column. 
 Note The variable name must start with a letter and contain only alphanumeric characters
 or underscores.
4. Save the text file.
5. Configure VeriStand to allow temporary variables based on where you call the text
 file. 
 Location
How to configureStimulus Profile Editor
Open a stimulus profile.
On the Edit tab, select Update Model
 Parameters from File.
Set the Allow Temporary Variables property to
 true.
Initializing parameters
Use System Explorer to apply initial values for
 model parameters from a .txt file.
On the Simulation Models page, click Allow
 temporary variables.
Model Parameter Manager tab
Use the VeriStand Editor to import model
 parameters.
In the Configure Parameter Import dialog box, click
 Allow local variables.
Model Parameter Manager Workspace tool
Use the Workspace to import model
 parameters.
In the Select Model Calibration Filedialog box,
 click Allow temporary variables.
Note Allowing temporary variables causes
 VeriStand to assume that any parameter column entries that do not exactly match model
 parameter names are temporary variables. For example, if Allow Temporary Variables is
 TRUE and you enter a model parameter name incorrectly, VeriStand creates a temporary
 variable with the new name and uses that variable instead of the model parameter. You do
 not receive an error notification about the name mismatch.

ParameterUpdate2.txt

tempConversionFactor

environment temperature (C)

Note

```text
tempConversionFactor     0.5
{environment temperature (C)}     50 * tempConversionFactor
```

This
 file is part of the Update Model Parameters example, available in the <Common
 Data>\Examples\Stimulus Profile\Engine Demo\Stimulus Profiles\
 directory.

Parent topic:

Setting Model Parameters

Related concepts:

- Supported Syntax in Model Parameter Files

Related tasks:

- Changing the Initial Value of Model Parameters
- Importing and Managing Batches of Model Parameters with the VeriStand Editor
- Importing and Managing Batches of Model Parameters in the Workspace

<!--NI_TOPIC bundle=veristand path=declare-variable-real-time-sequence.html language=enus -->
## TOPIC 00173: Declaring Variables in a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `declare-variable-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/declare-variable-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Declare and define the variables a real-time sequence can access and act on. Before you begin, create a real-time sequence. Real-time sequences can contain four different sections of variables that appear in the Variables pane. Section Description Return Variable The value the real-time sequence ret

### Declaring Variables in a Real-Time Sequence

Declare and define the variables a real-time sequence can access and act on.

Before you begin, create a real-time
 sequence.

Variables

| Section | Description |
| --- | --- |
| Return Variable | The value the real-time sequence returns after it executes. |
| Parameters | The inputs and outputs that the sequence accepts when called and can pass out to other sequences or the stimulus profile. |
| Local Variables | Variables you want to access from statements within the current sequence. |
| Channel References | References that allow you to read/write system definition channels directly from a real-time sequence. Note Channel references bind to specific system definition channels when added to a real-time sequence. The sequence that contains them is bound to that system definition file. If you want to write a sequence that you can reuse across multiple system definition files, use Parameters. |

1. Open a real-time sequence.
2. Declare a Return Variable.
  1. Determine the data type you want the sequence to return: 
 Boolean—Returns a true/false value that
 indicates if the sequence passes.
Void Return Value—If you do not need to
 perform a pass/fail evaluation on the sequence.
  2. In the Primitives palette, drag a data type from
 the Variables folder to the Return
 Variable section of the Variables
 pane.
  3. In the Variables pane, select the variable and
 use the Property Browser to configure its name and,
 for a Boolean, default value.
3. Declare a Parameter.
  1. To conserve memory, select the smallest possible data type that can
 hold the value you want to pass into or out of the sequence. 
 Note Use Double or Boolean primitives to create parameters to map to
 system definition channels. All channels in VeriStand are 64-bit
 floating point numbers (doubles), but many can also accept Boolean
 values.
  2. In the Primitives palette, drag a data type from
 the Variables folder to the
 Parameters section of the
 Variables pane.
  3. In the Variables pane, select a variable and use
 the Property Browser to configure its
 Default Assignment, or the channel it maps
 to.
4. Declare a Local Variable.
  1. To conserve memory, select the smallest possible data type that can
 hold the value you want to pass into or out of the sequence.
  2. In the Primitives palette, drag a data type from
 the Variables folder to the Local
 Variables section of the Variables
 pane.
  3. In the Variables pane, select a variable and use
 the Property Browser to configure its
 Default Value.
5. Declare a Channel Reference.
  1. In the Variables pane, right-click the
 Channel References section and click
 Insert Channels.
  2. Use the configuration tree to select the channels you want to add as
 Channel References and click
 OK.

Expression

Property Browser

Parent topic:

Creating Real-Time Sequences

Related tasks:

- Creating Real-Time Sequences

Related reference:

- Boolean Variable
- Void Return Value

<!--NI_TOPIC bundle=veristand path=deploying-system-defintion-rt-target.html language=enus -->
## TOPIC 00174: Deploying the System Definition File to a Real-Time Target

- bundle_id: `veristand`
- source_path: `deploying-system-defintion-rt-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/deploying-system-defintion-rt-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Deploy the system definition file to the real-time (RT) target to run a project. Before you begin, install the VeriStand engine to the RT target using MAX. Open your project in the VeriStand Editor. You can deploy the system definition without launching the VeriStand Editor. In the Project Files pan

### Deploying the System Definition File to a
 Real-Time Target

Deploy the system definition file to the real-time (RT) target to run a
 project.

Before you begin, install the VeriStand engine to the
 RT target using MAX.

1. Open your project in the VeriStand Editor. 
 Note You can deploy the system
 definition without launching the VeriStand Editor.
2. In the Project Files pane, double-click a system
 definition file (.nivssdf) to open the Mapping
 Diagram.
3. In the Configuration pane, click
 Document.
4. Set the target's operating system to Linux_x64.
5. Enter the IP Address of the RT target.
6. Save the system definition file.
7. Click Operate»Deploy.

- If the system definition file on the host computer is the same as the system
 definition deployed to the target, the host connects to the target and launches
 the VeriStand Editor without deploying the system
 definition file.
- If the system definition file on the host computer is different from the system
 definition deployed to the target, clicking Operate»Deploy stops the system definition on the target and deploys the system
 definition on the host.

You can also manage individual targets at run
 time and configure a watchdog timer for VeriStand to execute during
 deployment.

Parent topic:

Running Tests

Related concepts:

- Individual Target Management

Related tasks:

- Downloading Support Files in MAX
- Running the VeriStand Gateway Silently
- Configuring the Watchdog Timer when Deploying to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=deployment-target.html language=enus -->
## TOPIC 00175: Deployment Target

- bundle_id: `veristand`
- source_path: `deployment-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/deployment-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The deployment target in an VeriStand system is a desktop PC or RT target on which you run the system definition file and VeriStand Engine. Internal Feature The following is a feature that you cannot directly modify. VeriStand Engine—The non-visible execution mechanism that controls the timing of th

### Deployment Target

The deployment target in an VeriStand system is a desktop PC or RT target on which you run the system definition file and VeriStand Engine.

#### Internal Feature

The following is a feature that you cannot directly modify.

- VeriStand Engine—The non-visible execution mechanism that controls the timing of the entire system and the communication between the target and the host computer. The VeriStand Engine consists of multiple timed loops that use RT FIFOs to transfer data between the loops. 
 Note To deploy a system definition file to an RT target, you must first download support files for VeriStand to the target.

#### Interactive Features

- System Definition File—The 
 .nivssdf file you configure in the System Explorer window. A system definition file contains the configuration settings of the VeriStand Engine, including:
  - The rate at which the system runs.
  - DAQ devices, NI-XNET devices, FPGA targets, or reflective memory devices and the task and channel configurations for each.
  - Simulation models to execute, and the rate at which they execute.
  - The list of active alarms. You can use alarms to
 trigger actions on the target, such as procedures, or to display
 dialog boxes that alert the user of an event.
  - The list of procedures that can execute on the target. A procedure is a script of commands that define a set of actions in the VeriStand Engine.
  - The system mappings that determine how channels are connected.
  - The list of channels for data objects in the system. The following table displays common channel types. 
 Channel Type 
 ExamplesHardware I/O channels 
 DAQ, FPGA, etc. 
 Model channels 
 Inputs, outputs, parameters, and signals 
 User channels 
 Used to store or map user-defined values in the system 
 Calculated channels 
 Channels that represent the result of a user-defined calculation of other channels in the system
- Model—A mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs, called inports and outports, that communicate with other parts of the control system. Build models using several different modeling environments, and then integrate the model into a system definition file.

Parent topic:

Components of a VeriStand Project

<!--NI_TOPIC bundle=veristand path=dev-computer.html language=enus -->
## TOPIC 00176: Development Computer

- bundle_id: `veristand`
- source_path: `dev-computer.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/dev-computer.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The development computer is the computer that contains the VeriStand software. The computer on which you develop a NI VeriStand project might be different from the host computer in the system. To extend the functionality of VeriStand, you might also use the following NI products on the development c

### Development Computer

The development computer is the computer that contains the VeriStand software.

- LabVIEW Development System—If you want to create custom devices, workspace controls/indicators, timing devices, and/or Tools menu utilities, you need the LabVIEW Development System.
- LabVIEW Real-Time Module—You need this module to use RT functions in custom device VIs.
- LabVIEW FPGA Module—If you add a National Instruments FPGA target to a project, it must have an associated FPGA bitfile. VeriStand provides FPGA bitfiles for certain FPGA devices. If you want to customize these FPGA bitfiles or create a custom FPGA bitfile for another FPGA target, you need the FPGA Module.

Parent topic:

Host Computer

<!--NI_TOPIC bundle=veristand path=di-digital-input.html language=enus -->
## TOPIC 00177: Digital Input Channel Properties (DI)

- bundle_id: `veristand`
- source_path: `di-digital-input.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/di-digital-input.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure DI channel properties to measure digital signals. For more information on measuring digital signals, refer to the NI-DAQmx Manual. Property/Section Description Invert Lines Specifies whether to reverse digital line polarity: False—Do not invert lines. True—Invert lines. Same as port—Use th

### Digital Input Channel Properties (DI)

Configure DI channel properties to measure digital signals.

For more information on measuring digital signals, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Invert Lines | Specifies whether to reverse digital line polarity: False—Do not invert lines. True—Invert lines. Same as port—Use the same option as the port that contains the channel. To set this option, on the Port Configuration page, click Invert digital lines. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=differences-workspace-editor.html language=enus -->
## TOPIC 00178: Differences between Workspace and VeriStand Editor

- bundle_id: `veristand`
- source_path: `differences-workspace-editor.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/differences-workspace-editor.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Workspace and VeriStand Editor contain features that are unique to their respective screen files. The screen files for each application are not compatible with each other. You cannot convert files from one application to the other. Use the following table to determine the screen application to u

### Differences between Workspace and VeriStand
 Editor

The Workspace and VeriStand Editor contain
 features that are unique to their respective screen files.

The screen files for each application are not compatible with each other. You cannot convert
 files from one application to the other.

Use the following table to determine the screen application to use based on the task you
 want to accomplish.

| Task | Supported Application |
| --- | --- |
| Natively design a user interface at run-time. Access scripting capabilities. Operators can launch the application without opening VeriStand. View screens across multiple monitors. Use core controls such as rings and tabs. View the project configuration tree within the application. | VeriStand Editor |
| Access the Channel Calibration tool. Access macro recording and playback capabilities. Access custom objects. Access API to automate the application. Use services to launch application tools upon connecting to a target. Sync services with the launch of the application window. Access add-ons. Map a vector channel to controls or indicators. Access model controls.1 Access a built-in TDMS file viewer.2 Use the application for benchmarking CPU and debugging the Console Viewer that ships with the Workspace.3 Access a built-in tool to launch the NI-XNET Bus Monitor.4 Access a tools menu that you can edit from Project Explorer.5 | Workspace |
| 1 You can map execution channels to regular controls to achieve the same functionality as a model control within the VeriStand Editor. 2 If you double-click a TDMS file in the VeriStand Editor, the file launches in your default viewer. 3 You can use the browser-based console viewer in the VeriStand Editor. 4 You can use an action button to launch the bus monitor application in the VeriStand Editor. 5 You can use action buttons to launch custom tools from the VeriStand Editor. |  |

Parent topic:

Running the VeriStand Workspace

Related reference:

- VeriStand Environment

<!--NI_TOPIC bundle=veristand path=disconnect-individual-target.html language=enus -->
## TOPIC 00179: Disconnecting Individual Targets

- bundle_id: `veristand`
- source_path: `disconnect-individual-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/disconnect-individual-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Disconnect a VeriStand target in the Manage Targets tool to support maintenance after errors or physical faults. In the VeriStand Editor, click Tool Launcher Manage Targets . In the Tool window's Manage Targets tab, select the target or targets that you want to disconnect. Click Disconnect. In the M

### Disconnecting Individual Targets

Disconnect a VeriStand target in the Manage Targets tool to support maintenance after
 errors or physical faults.

1. In the VeriStand Editor, click Tool Launcher»Manage Targets.
2. In the Tool window's Manage Targets
 tab, select the target or targets that you want to disconnect.
3. Click Disconnect.

Manage Targets

State

Parent topic:

Individual Target Management

<!--NI_TOPIC bundle=veristand path=display-waveform-data.html language=enus -->
## TOPIC 00180: Displaying Waveform Data in a Graph

- bundle_id: `veristand`
- source_path: `display-waveform-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/display-waveform-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Display double-precision waveform acquisition data in a waveform graph control to monitor and verify acquired data. Before you begin, set up timing and logging properties for waveform acquisitions. You can only graph waveforms with a double-precision floating-point data type. Open the Workspace. Sel

### Displaying Waveform Data in a Graph

Display double-precision waveform acquisition data in a waveform graph control to
 monitor and verify acquired data.

Before you begin, set up timing and
 logging properties for waveform acquisitions.

You can only graph waveforms with a double-precision
 floating-point data type.

1. Open the Workspace.
2. Select Screen»Edit Mode to display the Workspace Controls palette
 and alignment grid.
3. Click the Workspace Controls palette.
4. Select Graph»Waveformand drag the waveform graph onto the alignment grid.
5. In the Waveform Graph Settings dialog box, select the
 waveforms to display in the graph and the conditions that you want to stream
 data.

Ignore Time
 Stamps

Note

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Setting Up Timing and Logging Properties for Waveform Acquisitions

<!--NI_TOPIC bundle=veristand path=division-expression-functions-operators.html language=enus -->
## TOPIC 00181: Performing Division with Expression Functions and Operators

- bundle_id: `veristand`
- source_path: `division-expression-functions-operators.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/division-expression-functions-operators.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the division operator or quotient function to divide expression functions and operators. The division operator (/) method divides all numbers as doubles and results in a double quotient, regardless of the data type of the dividend or divisor. If the dividend, divisor, and result are all of type

### Performing Division with Expression Functions
 and Operators

Use the division operator or quotient function to divide expression functions and
 operators.

division operator (/)

Note

The *quotient function* method rounds the result of the division towards
 minus infinity.

Depending on your goal, use a division method with your expression function or
 operator.

| Goal | Method |
| --- | --- |
| Perform an integer division and want the result as a double | Division Operator (/) |
| Perform an integer division and want the result as an integer rounded towards minus infinity | Quotient Function |
| Divide U64 integers |  |

If the result is passed to
 another data type, VeriStand performs an implicit cast. An implicit cast converts
 one data type to another. For example, if a double is converted to an integer, the
 resulting number is rounded toward zero. This may lead to unexpected values.

| Function/Operator | Double | Integer (I32, I64, U32, U64) |
| --- | --- | --- |
| mod(x,y) | Nan | The sequence is aborted with error -8 |
| quotient(x,y) | -Inf/Nan/Inf |  |
| rem(x,y) | Nan |  |
| / | -Inf/Nan/Inf |  |
| % | Nan |  |

Parent topic:

Adding and Editing Expressions in a Real-Time Sequence

<!--NI_TOPIC bundle=veristand path=dma-scale-offset.html language=enus -->
## TOPIC 00182: DMA Scale and Offset

- bundle_id: `veristand`
- source_path: `dma-scale-offset.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/dma-scale-offset.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scale and offset are useful for converting the DMA FIFO value (DFV) to a usable value that corresponds to a real-world measurement. The following table displays equations that show how scale and offset convert DFV to voltage value (VV) for read channels of different data types, and VV to DFV for wri

### DMA Scale and Offset

Scale and offset are useful for converting the DMA FIFO value (DFV) to a usable value
 that corresponds to a real-world measurement.

The following table displays equations that show how scale and offset convert DFV to voltage
 value (VV) for read channels of different data types, and VV to DFV for write channels of
 different data types.

| Data type | Read or Write | Equation |
| --- | --- | --- |
| I8, U8, I16, U16, I32, U32, I64, U64, Boolean | Read | V V = [ D F V × ( scale ÷ P ) + offset ] |
| I8, U8, I16, U16, I32, U32, I64, U64, Boolean | Write | D F V = ( V V − offset ) × ( P ÷ scale ) |
| FXPI32, FXPU32,FXPI64, FXPU64 | Read | V V = ( F X P V × scale ) + offset |
| FXPI32, FXPU32,FXPI64, FXPU64 | Write | F X P V = ( V V − offset ) ÷ scale |
| PWM | Read | V V = [ H T ÷ ( L T + H T ) ] × ( scale + offset ) |
| PWM | Write | H T = [ ( V V − offset ) ÷ scale ] × P W M period L T = P W M period − H T |
| V V —Represents voltage value. D F V —Represents DMA FIFO value. P —Represents the positive range of the data type. F X P V —Represents the converted fixed-point value. H T —Represents high time. L T —Represents low time. |  |  |

Parent topic:

Creating a Custom FPGA Configuration File

<!--NI_TOPIC bundle=veristand path=do-digital-output.html language=enus -->
## TOPIC 00183: Digital Output Channel Properties (DO)

- bundle_id: `veristand`
- source_path: `do-digital-output.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/do-digital-output.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure DO channel properties to generate digital signals. For more information on generating digital signals, refer to the NI-DAQmx Manual. Property/Section Description Invert Lines Specifies whether to reverse digital line polarity: False—Do not invert lines. True—Invert lines. Same as port—Use

### Digital Output Channel Properties
 (DO)

Configure DO channel properties to generate digital signals.

For more information on generating digital signals, refer to the NI-DAQmx Manual.

| Property/Section | Description |
| --- | --- |
| Invert Lines | Specifies whether to reverse digital line polarity: False—Do not invert lines. True—Invert lines. Same as port—Use the same option as the port that contains the channel. To set this option, on the Port Configuration page, click Invert digital lines. |

Parent topic:

Adding and Configuring DAQ Device Channels

Related information:

- NI-DAQmx Common Applications

<!--NI_TOPIC bundle=veristand path=double-array-variable.html language=enus -->
## TOPIC 00184: Double Array Variable

- bundle_id: `veristand`
- source_path: `double-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/double-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of double-precision, floating point numbers. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriat

### Double Array Variable

An array of double-precision, floating point numbers.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=double-variable.html language=enus -->
## TOPIC 00185: Double Variable

- bundle_id: `veristand`
- source_path: `double-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/double-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A double-precision, floating point number. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most

### Double Variable

A double-precision, floating point number.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=dowhile-loop.html language=enus -->
## TOPIC 00186: DoWhile Loop

- bundle_id: `veristand`
- source_path: `dowhile-loop.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/dowhile-loop.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of statements that execute once and then continue executing for as long as the Repeat While expression evaluates to TRUE. Configure the code that executes in the loop by dragging expressions and other primitives to the loop and configuring them as you would any other section of sequence

### DoWhile Loop

A collection of statements that execute once and then continue executing for as long
 as the Repeat While expression evaluates to TRUE.

Configure the code that executes in the loop by dragging expressions
 and other primitives to the loop and configuring them as you would any other section
 of sequence code.

| Property/Section | Description |
| --- | --- |
| Repeat While | Specifies the expression to evaluate to determine if the loop continues to execute. The loop executes as long as this expression evaluates to TRUE. |
| Auto Yield | If TRUE, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Loops

<!--NI_TOPIC bundle=veristand path=download-support-MAX.html language=enus -->
## TOPIC 00187: Downloading Support Files in MAX

- bundle_id: `veristand`
- source_path: `download-support-MAX.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/download-support-MAX.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you can deploy VIs or a system definition file to a real-time target, use NI Measurement & Automation Explorer (MAX) to download support files. Launch MAX. In the configuration tree, click Remote Systems. Select the real-time target you want to deploy to and click Software. If the real-time t

### Downloading Support Files in MAX

Before you can deploy VIs or a system definition file to a real-time target, use NI
 Measurement & Automation Explorer (MAX) to download support files.

1. Launch MAX.
2. In the configuration tree, click Remote Systems.
3. Select the real-time target you want to deploy to and click
 Software. 
 Note If the real-time target does not have
 a Software category, then it does not support the required
 software.
4. On the toolbar, click Add/Remove Software to launch the LabVIEW
 Real-Time Software Wizard. 
 Note You will be prompted to enter the
 real-time system's administrator name and password if it has one. For more information,
 refer to the Logging into your System topic in the Measurement &
 Automation Explorer Help.
5. Optional: 
 Select Custom software installation (currently installed) and
 click Next to install recommended software if prompted.
6. Click the icon next to VeriStand RT Engine.
7. Select Install the feature and click
 Next.
8. Confirm that you want to install VeriStand support and click
 Next.

MAX displays the progress of the installation and reboots the target so it is ready for
 a system definition file.

Parent topic:

Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=ecu-preparing-system-definition-file.html language=enus -->
## TOPIC 00188: Preparing a System Definition File for Virtual ECUs

- bundle_id: `veristand`
- source_path: `ecu-preparing-system-definition-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ecu-preparing-system-definition-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the VeriStand Virtual ECU Toolkit to configure your system definition file to integrate virtual ECUs you created using third-party software from a supported vendor. Before you begin, download and install the VeriStand Virtual ECU Toolkit and set up the real-time target.

### Preparing a System Definition File for Virtual
 ECUs

Use the VeriStand Virtual ECU Toolkit to configure your system definition file to
 integrate virtual ECUs you created using third-party software from a supported
 vendor.

Before you begin, download
 and install the VeriStand Virtual ECU Toolkit and set up the real-time
 target.

1. Adding and Configuring Virtual ECUs Incorporate a virtual ECU with the system definition file.
2. Creating and Configuring an ECU Network Cluster Create an ECU network cluster to connect your virtual ECUs and ECUs.

Parent topic:

Configuring a System Definition File

Related tasks:

- Setting Up a Real-Time Target for Virtual ECUs

<!--NI_TOPIC bundle=veristand path=edit-xnet-databases.html language=enus -->
## TOPIC 00189: Editing NI-XNET Databases

- bundle_id: `veristand`
- source_path: `edit-xnet-databases.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/edit-xnet-databases.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the NI-XNET Database Editor to update embedded network databases, including frames, signals, and ECU assignments. Understand editor limits for LIN description files and FIBEX databases with LIN content. Before you begin, add an NI-XNET database. The NI-XNET Database Editor creates and maintains

### Editing NI-XNET Databases

Use the NI-XNET Database Editor to update embedded network databases, including
 frames, signals, and ECU assignments. Understand editor limits for LIN description
 files and FIBEX databases with LIN content.

Before you begin, add an NI-XNET
 database.

NI-XNET Database
 Editor

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»XNET Databases in the configuration tree.
4. Select the database you want to edit and click Launch XNET Database
 Editor
[IMAGE alt='image' src='GUID-56299BBE-F088-4C9C-9782-9BF85C8B601B-a5.gif']. 
 Note The editor cannot open LIN
 description files (.ldf) or FIBEX databases with LIN content.
5. Use the editor to make changes to the database.
6. Select File»Save to save the database file and close the editor.
7. Select the database again and click Refresh Databases
[IMAGE alt='image' src='GUID-0CA6E774-B2D1-44B2-8144-EDD0E23B14FF-a5.gif']. 
 Note VeriStand will ask you to delete any
 signals removed from the database or multiplexed signals that changed in the database.
 Import the changed multiplexed signals again for VeriStand to read them
 correctly.
8. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Adding NI-XNET Databases

<!--NI_TOPIC bundle=veristand path=editor-tools.html language=enus -->
## TOPIC 00190: VeriStand Editor Tools

- bundle_id: `veristand`
- source_path: `editor-tools.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/editor-tools.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand Editor provides tools that allow you to manipulate a project without having to open the system definition. Goal Task Log data Create logging specification (.nivslspec) files with Log Management to configure and execute host-side data logging. View model values Check signal values with

### VeriStand Editor Tools

The VeriStand Editor provides tools that allow you to manipulate a
 project without having to open the system definition.

| Goal | Task |
| --- | --- |
| Log data | Create logging specification (.nivslspec) files with Log Management to configure and execute host-side data logging. |
| View model values | Check signal values with the Model Signal Viewer without importing the signal as a channel or editing the system definition file. |
| Fault a channel to a specific value | Fault a channel with the Channel Fault Manager to test the behavior of a system when a channel reaches a specific value. |
| Import and manage batches of model parameters | Import model parameters with the Model Parameter Manager to apply values defined in an external .txt file to a model. |
| View channel values at run time | Monitor channels with the Channel Data Viewer to view the current values of several channels together. |

Parent topic:

Visualizing System State

Related tasks:

- Logging Data with the VeriStand Editor
- Viewing Model Values in the VeriStand Editor
- Faulting a Channel to a Specific Value
- Importing and Managing Batches of Model Parameters with the VeriStand Editor
- Viewing Channel Values at Run Time

<!--NI_TOPIC bundle=veristand path=enhance-workspace-tools.html language=enus -->
## TOPIC 00191: Enhancing Your Workspace to View Data

- bundle_id: `veristand`
- source_path: `enhance-workspace-tools.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/enhance-workspace-tools.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Workspace tools such as Alarm Monitor, Channel Data Viewer, TDMS File Viewer, and XNET Bus Monitor to view data. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard or Custom Tools Menu Item. In the Workspace, select Tools. Depe

### Enhancing Your Workspace to View Data

Use Workspace tools such as Alarm Monitor, Channel Data Viewer, TDMS
 File Viewer, and XNET Bus Monitor to view data.

Workspace

Tools

1. In the Workspace, select
 Tools.
2. Depending on your goal, use any of the following tools. 
 Goal
ToolManage alarms high limit, low limit,
 corresponding procedure name, delay duration, trip value,
 priority, state, and mode information.
Alarm Monitor
View the current values for several
 channels at a time.
Channel Data Viewer
View the contents of a
 .tdms file.
TDMS File Viewer
View and log messages sent by an NI-XNET
 device.
XNET Bus Monitor
Perform custom tasks specified by a
 LabVIEW VI.
Custom VI Tool

Parent topic:

Running the VeriStand Workspace

Related concepts:

- NI-XNET Bus Monitor

<!--NI_TOPIC bundle=veristand path=environment.html language=enus -->
## TOPIC 00192: VeriStand Environment

- bundle_id: `veristand`
- source_path: `environment.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/environment.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VeriStand environment is configuration-based, consisting of several dialog boxes and windows that allow you to modify various components of a project. The following table describes the windows that make up the VeriStand environment. Window Common Tasks How to Access VeriStand Editor Accessing th

### VeriStand Environment

The VeriStand environment is configuration-based, consisting of several dialog boxes
 and windows that allow you to modify various components of a project.

| Window | Common Tasks | How to Access |
| --- | --- | --- |
| VeriStand Editor | Accessing the system definition file Creating screens that serve as the user interface Monitoring system data displaying in user interface indicators Manipulating variables, such as model parameters, through user interface controls Creating mappings to connect channels Interacting with various tools designed for monitoring alarms, viewing channel data, or running stimulus profiles Testing system behavior using channel faulting and error monitoring tools Controlling the execution of your system Launching System Explorer and the Workspace Configuring and running stimulus profiles Configuring services Configuring alarm responses | Open a VeriStand project. |
| System Explorer | Creating and modifying system definition files by: Representing the hardware and software components in the system Creating alarms and procedures that execute on the target Creating mappings to connect channels Configuring settings of the VeriStand Engine, such as the rate at which the system runs | Double-click the system definition file (.nivssdf) in the Project Files pane of the VeriStand Editor. Launch a system definition file from Project Files and click Configure. |
| Workspace | Creating screens that serve as the user interface with which an operator interacts Monitoring system data displaying in user interface indicators Manipulating variables, such as model parameters, through user interface controls Interacting with various tools designed for monitoring alarms, viewing channel data, scaling and calibrating channels, or running stimulus profiles | Double-click Workspace in the Project Files pane of the VeriStand Editor. |

<!--NI_TOPIC bundle=veristand path=example-accessing-a-large-number-of-variables.html language=enus -->
## TOPIC 00193: Example: Accessing Many Variables

- bundle_id: `veristand`
- source_path: `example-accessing-a-large-number-of-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/example-accessing-a-large-number-of-variables.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In test scenarios like negative testing, you may need to access and reinitialize all variables. In such cases, you can use a combination of a control loop and the NI VeriStand - Send Message to Custom Device API. In the Custom Device Example, the CD.Command.SetHWValues and CD.Command.GetHWValues com

### Example: Accessing Many Variables

In test scenarios like negative testing, you may need to access and reinitialize all
 variables. In such cases, you can use a combination of a control loop and the NI VeriStand -
 Send Message to Custom Device API.

In the *Custom Device Example*, the CD.Command.SetHWValues and
 CD.Command.GetHWValues commands use JSON format to send and receive data.

The CD.Command.SetHWValues command carries a map of SignalIDs and the corresponding
 values to set. Upon receiving the message, the command deserializes the double values
 and maps them to their respective SignalIDs before pushing the values into the RT
 FIFO.

Figure 34.

[IMAGE alt='Block diagram showing the CD.Command.SetHWValues command process.' src='GUID-BC9A0C18-4EDA-4582-B0F0-A849D1A5CD98-a5.png']

The Write Data to HW state of the RT driver applies the new values to the driver.

Figure 35.

[IMAGE alt='Block diagram showing the Write Data to HW state processing Set Variables requests.' src='GUID-7843F7CD-1C79-4769-A73B-331691010DCF-a5.png']

The CD.Command.GetHWValues command includes a list of SignalIDs for which you are
 requesting current values. The command deserializes the list and pushes it into the RT
 FIFO.

Figure 36.

[IMAGE alt='Block diagram of the CD.Command.GetHWValues command showing signal processing and queue handling.' src='GUID-A29BD065-276A-4FE5-BC5C-6839D0313C06-a5.png']

The Read Data from HW state of the RT driver retrieves the corresponding value from the
 driver array.

Figure 37.

[IMAGE alt='Block diagram showing the Read Data from HW state with Get HW Val Ref and Read operations.' src='GUID-E963B6F3-D77F-4471-A114-F2E0FD366B43-a5.png']

#### Example: Set Values with a Custom
 Command

```text
                        int start = 100;
                        int count = 100;
                        
                        int[] signalIDs = new int[count];
                        double[] values = new double[count];
                        
                        for (int  index = 0; index <  count; index++)
                        {
                        signalIDs[index] = start + index;
                        values[index] = (double)(start + index);
                        }
                        
                        var data = new { SignalIDs = signalIDs, Values = values };
                        string json = JsonConvert.SerializeObject(data);
                        
                        Factory FacRef = new Factory();
                        var cdQuery = FacRef.GetICustomDevice("localhost", "Targets/Controller/Custom Devices/Runtime Configuration Support Demo");
                        cdQuery.SendMessage("CD.Command.SetHWValues", json, 5000, out string response);
                        Console.WriteLine(response);
                    
```

#### Example: Get Values with a Custom
 Command

```text
                        int start = 100;
                        int count = 100;
                        
                        int[] SignalIDsIn = new int[count];
                        int[] SignalIDsOut = new int[count];
                        
                        for (int  index = 0; index <  count; index++)
                        {
                        SignalIDsIn[index] = start + index;
                        SignalIDsOut[index] = start + index;
                        }
                        
                        var data = new { SignalIDsIn = signalIDsIn, SignalIDsOut = signalIDsOut };
                        string json = JsonConvert.SerializeObject(data);
                        
                        Factory FacRef = new Factory();
                        var cdQuery = FacRef.GetICustomDevice("localhost", "Targets/Controller/Custom Devices/Runtime Configuration Support Demo");
                        
                        cdQuery.SendMessage("CD.Command.GetHWValues", json, 5000, out string response);
                        Console.WriteLine("Response from Get HW Values Command:");
                        Console.WriteLine(response);
                    
```

Parent topic:

Overview of Runtime Configurability

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=example-fpga-configuration-file.html language=enus -->
## TOPIC 00194: Example FPGA Configuration File Structure

- bundle_id: `veristand`
- source_path: `example-fpga-configuration-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/example-fpga-configuration-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An FPGA configuration file needs to be structured correctly in XML to function properly. The following code displays an example of how to implement the FPGA configuration file XML tags.<?xml version='1.0'> <?xml-stylesheet type="text/xsl" href='NI VeriStand FPGA DMA.xsl'?> <FPGADMAChannelData xmlns:

### Example FPGA Configuration File
 Structure

An FPGA configuration file needs to be structured correctly in XML to function
 properly.

```text
<?xml version='1.0'> 
<?xml-stylesheet type="text/xsl" href='NI VeriStand FPGA DMA.xsl'?>
<FPGADMAChannelData xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation = "NI VeriStand FPGA DMA.xsd">
      <Version>2.0</Version>
      <Bitfile>FPGADMABitfile.lvbitx</Bitfile>

      <Categories>
          <Category>
              <Name>TopLevel1</Name>
              <Description>Description</Description>
              <Symbol>Default</Symbol>
              <Category>
                  <Name>NestedCategory1</Name>
                  <Description>Category with AI Symbol contained in TopLevel1</Description>
                  <Symbol>AI</Symbol>
              </Category>
              <Category>
                  <Name>NestedCategory2</Name>
                  <Description>Category with DI Symbol contained in TopLevel1</Description>
                  <Symbol>DI</Symbol>
              </Category>
          </Category>
      </Categories>

      <DMA_Read>
          <Packets>5</Packets>
          <Packet/>
          <Packet>
              <I8>
                  <Name>Signed8Channel</Name>
                  <Description>Description of channel</Description>
                  <Category>TopLevel1\NestedCategory1</Category>
                  <InitialValue>25</InitialValue>
                  <Scale>128</Scale>
                  <Offset>5</Offset>
                  <Unit>Volts</Unit>
                  <Symbol>AI</Symbol>
              </I8>
              <U8>
                  <Name>Unsigned8Channel</Name>
                  <Description>Description of channel</Description>
                  <Category>TopLevel1\NestedCategory2</Category>
                  <InitialValue>25</InitialValue>
                  <Scale>128</Scale>
                  <Offset>5</Offset>
                  <Unit>Volts</Unit>
                  <Symbol>AI</Symbol>
              </U8>
              <I16>
                  <Name>Signed16Channel</Name>
              </I16>
              <Boolean>
                  <Name>BooleanChannel</Name>
              </Boolean>
              <Void>
                  <Size>7</Size>
              </Void>
          </Packet>
          <Packet>
              <FXPI32>
                  <Name>Fixed Point Channel 1</Name>
                  <Scale>2</Scale>
                  <Offset>5</Offset>
                  <Unit>Volts</Unit>
                  <Symbol>AI</Symbol>
                  <FXPWL>20</FXPWL>
                  <FXPIWL>5</FXPIWL>
              </FXPI32>
          </Packet>
          <Packet>
              <PWM>
                  <Name>PWM In 0</Name>
                  <Description>PWM input</Description>
                  <Category>Input\PWM</Category>
                  <Scale>100</Scale>
                  <Unit>%</Unit>
                  <Symbol>PWM In</Symbol>
                  <PWMPeriod>40000</PWMPeriod>
              </PWM>
          </Packet>
          <Packet>
              <U8>
                  <Name>Channel with one parameter</Name>
                  <Parameters>
                      <I16>
                        <Name>UI Parameter name</Name>
                        <ControlName>Name of Control</ControlName>
                        <InitialValue>25</InitialValue>
                        <Scale>100</Scale>
                        <Offset>0</Offset>
                      </I16>
                  </Parameters>
              </U8>
          </Packet>
      </DMA_Read>

      <DMA_Write>
          <Packets>4</Packets>
          <Packet>
              <U8>
                  <Name>Unsigned8Out</Name>
                  <Category>TopLevel2</Category>
                  <Symbol>DO</Symbol>
              </U8>
          </Packet>
      </DMA_Write>
</FPGADMAChannelData>
```

Parent topic:

Creating a Custom FPGA Configuration File

Related reference:

- FPGA Configuration File XML Tags

<!--NI_TOPIC bundle=veristand path=examples.html language=enus -->
## TOPIC 00195: VeriStand Examples

- bundle_id: `veristand`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/examples.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI installs example code with your software or driver that demonstrates the functionality of VeriStand. Use these examples to learn about the product or accelerate your own application development. Most NI products install examples that you can access directly or from within NI software. The example

### VeriStand Examples

NI installs example code with your software or driver that demonstrates the functionality of VeriStand. Use these examples to learn about the product or accelerate your own application development.

Most NI products install examples that you can access directly or from within NI
 software. The example experience can differ slightly across products and
 versions.

| Application Area | Location | Description |
| --- | --- | --- |
| VeriStand Project | <Public Documents>\\National Instruments\\NI VeriStand <version>\\Examples\\Sinewave Delay | An example VeriStand project, including related items such as a system definition, a Workspace screen file, and compiled models. |
| Stimulus Profile Editor | <Public Documents>\\National Instruments\\NI VeriStand <version>\\Examples\\Stimulus Profile | VeriStand Stimulus Profile Editor examples. |
| ASAM XIL Sample Configurations | <Public Documents>\\National Instruments\\NI VeriStand <version>\\Examples\\DotNet4.6.2\\ASAM XIL | Configuration examples for ASAM XIL. |
| LabVIEW API | <Program Files>\\National Instruments\\LabVIEW <version>\\examples\\NI VeriStand <Program Files>\\National Instruments\\LabVIEW <version>\\examples\\NI VeriStand Custom Devices | LabVIEW examples that use the VeriStand API. |

<!--NI_TOPIC bundle=veristand path=execution-order-models.html language=enus -->
## TOPIC 00196: Configuring the Execution Order of Models

- bundle_id: `veristand`
- source_path: `execution-order-models.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/execution-order-models.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Set the execution order for simulation models in the Primary Control Loop to control parallel or series data flow. Use the following table to determine the order that your models execute. The PCL execution mode does not affect the execution order for multiple models. Model execution Description Diag

### Configuring the Execution Order of
 Models

Set the execution order for simulation models in the Primary Control Loop to control
 parallel or series data flow.

1. Use the following table to determine the order that your models execute. 
 Note The PCL
 execution mode does not affect the execution order for multiple
 models.
Model execution
Description
DiagramIn parallel (default)
Models read data from the previous PCL iteration and
 execute in parallel.
If you map one model to another, the second, dependent,
 model always receives data the first model generated
 during the previous iteration of the Model Execution
 Loop. It does not receive data the first model generates
 during the current iteration.
[IMAGE alt='image' src='GUID-43780F42-0A29-4719-92A7-645CEB64F5B8-a5.gif']
In series
Models execute relative to each other.
If you map one model to another, defining an execution
 order allows you to ensure that the second, dependent
 model receives data the first model generates during the
 same iteration.
[IMAGE alt='image' src='GUID-A7763DBB-B038-45C0-9F29-BD990D0E55ED-a5.gif']
2. Launch your project in the VeriStand Editor.
3. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
4. Click Targets»Controller»Simulation Models»Execution Order in the configuration tree.
5. On the Execution Order Configuration page, drag the red
 cells representing the Models from one group to another
 to arrange them in the order that you want the models to execute. 
 Note Models in the same
 execution groups execute in parallel.
6. Click Refresh to reorder the
 Models and Execution order
 lists based on the changes you have made.
7. Save the system definition file.

Parent topic:

Adding and Configuring a Model

Related concepts:

- Primary Control Loop Step Execution in Models

<!--NI_TOPIC bundle=veristand path=export-parameter-value.html language=enus -->
## TOPIC 00197: Exporting Parameter Values

- bundle_id: `veristand`
- source_path: `export-parameter-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/export-parameter-value.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Model Parameter Manager tool to export parameter values to reproduce certain behaviors in your model. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard or Custom Tools Menu Item. Deploy the system definition with models to

### Exporting Parameter Values

Use the Model Parameter Manager tool to export parameter
 values to reproduce certain behaviors in your model.

Workspace

Tools

1. Deploy the
 system definition with models to the target. 
 Note You can only apply new
 values to deployed systems.
2. In the Workspace, select Tools»Model Parameter Manager to launch the tool. 
 Note The name of this menu item might differ
 depending on how you named it in the Tools Properties
 dialog box.
3. Click Save Values to save the current system values to a
 new or existing model parameter file.

VeriStand exports values in the format that corresponds to
 the file extension you choose.

Parent topic:

Importing and Managing Batches of Model Parameters in the Workspace

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=expression-operator-precedence.html language=enus -->
## TOPIC 00198: Expression Operator Precedence

- bundle_id: `veristand`
- source_path: `expression-operator-precedence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/expression-operator-precedence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Operators in real-time sequence expressions have an order to when they execute. The following table lists the order of precedence for operators from highest to lowest. Operators on the same line have the same precedence. Operator Description ** Exponentiation -, !, ~, ++, and –– Unary negation, logi

### Expression Operator Precedence

Operators in real-time sequence expressions have an order to when they
 execute.

The following table lists the order of precedence for operators from highest to lowest. Operators
 on the same line have the same precedence.

| Operator | Description |
| --- | --- |
| ** | Exponentiation |
| -, !, ~, ++, and –– | Unary negation, logical not, bit complement, pre- and post-increment, pre- and post-decrement |
| *, /, % | Multiplication, division, modulus (remainder) |
| + and – | Addition and subtraction |
| >> and << | Arithmetic shift right and shift left |
| >, <, >=, and <= | Greater, less, greater or equal, and less or equal |
| != and == | Inequality and equality |
| & | Bit and |
| ^ | Bit exclusive or |
| \| | Bit or |
| && | Logical and |
| \|\| | Logical or |
| ? : | Conditional evaluation |
| = op= | Assignment, shortcut operate and assignop can be +, –, *, /, >>, <<, &, ^, \|, %, or **. |

The assignment operator = is right associative (groups right to left), as is the
 exponentiation operator **. All other binary operators are left associative.

```text
<lexpr> ? <texpr>: <fexpr>
```

<texpr>

<lexpr>

<fexpr>

Parent topic:

Adding and Editing Expressions in a Real-Time Sequence

<!--NI_TOPIC bundle=veristand path=expression-syntax.html language=enus -->
## TOPIC 00199: Expression Syntax

- bundle_id: `veristand`
- source_path: `expression-syntax.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/expression-syntax.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use expression syntax similarly to the syntax used in text-based programming languages. Your expression syntax must conform to the allowed functions and operator precedence in the Expression component of the Property Browser. The expression syntax is summarized below using Backus-Naur Form (BNF nota

### Expression Syntax

Use expression syntax similarly to the syntax used in text-based programming languages.

Your expression syntax must conform to the allowed functions and
 operator
 precedence in the Expression component of the
 Property Browser.

Note

- expression
- left-hand-side assignment-operator assignment

- expression binary-operator expression
- unary-operator expression
- expression unary-operator
- expression ? expression : expression
- ( expression )
- identifier
- constant
- function-name ( argument-list )

- identifier
- identifier array-subscription

- [ assignment ]

- = 
 += 
 –= 
 *= 
 /= 
 >>= 
 <<= 
 &= 
 ^= 
 |= 
 %= 
 **=

- + 
 – 
 * 
 / 
 ^ 
 != 
 == 
 > 
 < 
 >= 
 <= 
 >> 
 << 
 && 
 || 
 & 
 | 
 % 
 **

- – 
 ! 
 ++ 
 –– 
 ~

- expression
- expression , argument-list

- pi
- true
- false
- number

- _ 
 a~z 
 A~Z

- 0 
 1 
 2 
 3 
 4 
 5 
 6 
 7 
 8 
 9

- 1 
 2 
 3 
 4 
 5 
 6 
 7 
 8 
 9

- 0 
 1

- 0 
 1 
 2 
 3 
 4 
 5 
 6 
 7 
 8 
 9 
 a 
 b 
 c 
 d 
 e 
 f 
 A 
 B 
 C 
 D 
 E 
 F

- non-digit [non-first-character]

- non-digit [non-first-character]
- digit [non-first-character]

- integer-constant
- float-constant

- decimal-constant
- binary-constant
- hex-constant

- nonzero-digit #digit

- 0b #binary-digit
- 0B #binary-digit

- 0x #hex-digit
- 0X #hex-digit

- fraction exponent-part
- decimal-constant exponent-part

- #digit . digit #digit

- e [sign] #digit
- E [sign] #digit

- + 
 -

Parent topic:

Adding and Editing Expressions in a Real-Time Sequence

Related concepts:

- Expression Operator Precedence

Related reference:

- Expression Functions

<!--NI_TOPIC bundle=veristand path=expression.html language=enus -->
## TOPIC 00200: Expression Syntax

- bundle_id: `veristand`
- source_path: `expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/expression.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A statement that can operate on variables in a real-time sequence. For example, VarName * 2 is an expression that multiplies the value of a variable, VarName, by 2. Expressions are the building blocks of real-time sequence code, and must follow the expected syntax. Property/Section Description Expre

### Expression Syntax

A statement that can operate on variables in a real-time sequence.

For example, VarName * 2 is an expression that multiplies the value of a
 variable, VarName, by 2. Expressions are the building blocks of
 real-time sequence code, and must follow the expected syntax.

| Property/Section | Description |
| --- | --- |
| Expression | Specifies the expression to evaluate. You can include real-time sequence variables, supported functions, and operators in an expression. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Expressions Primitives

<!--NI_TOPIC bundle=veristand path=expressions-functions.html language=enus -->
## TOPIC 00201: Expression Functions

- bundle_id: `veristand`
- source_path: `expressions-functions.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/expressions-functions.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use functions when editing expressions in the Property Browser. All function names must be lowercase. Function Description Return type abs(x) Returns the absolute value of x. Returns a value of the same type as the input. abstime( ) Returns the current date and time in seconds relative to 12:00 a.m.

### Expression Functions

Use functions when editing expressions in the Property
 Browser.

Note

| Function | Description | Return type |
| --- | --- | --- |
| abs(x) | Returns the absolute value of x. | Returns a value of the same type as the input. |
| abstime( ) | Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. | Double |
| acos(x) | Returns the inverse cosine of x in radians. | Double |
| acosh(x) | Returns the inverse hyperbolic cosine of x. | Double |
| acot(x) | Returns the inverse cotangent of x in radians. | Double |
| acoth(x) | Returns the inverse hyperbolic cotangent of x. | Double |
| acsc(x) | Returns the inverse cosecant of x in radians. | Double |
| acsch(x) | Returns the inverse hyperbolic cosecant of x. | Double |
| arraysize(x) | Returns the number of elements in x, where x is an array. | Int64 |
| asec(x) | Returns the inverse secant of x in radians. | Double |
| asech(x) | Returns the inverse hyperbolic secant of x. | Double |
| asin(x) | Returns the inverse sine of x in radians. | Double |
| asinh(x) | Returns the inverse hyperbolic sine of x. | Double |
| atan(x) | Returns the inverse tangent of x in radians. | Double |
| atan2(y,x) | Returns the arctangent of y/x in radians. | Double |
| atanh(x) | Returns the inverse hyperbolic tangent of x. | Double |
| ceil(x) | Rounds x to the next higher integer (smallest integer ≥ x) and returns the rounded value. | Double |
| clearfault(x) | Clears any fault set on x. x must be a reference to a channel and should not be a reference to a local variable. If x references a local variable, clearfault performs no operation. | Void |
| clearlasterror(x) | Clears the last error set by the Generate Error primitive so the error does not appear in the test results file. | Void |
| cos(x) | Returns the cosine of x, where x is in radians. | Double |
| cosh(x) | Returns the hyperbolic cosine of x. | Double |
| cot(x) | Returns the cotangent of x (1/tan(x)), where x is in radians. | Double |
| coth(x) | Returns the hyperbolic cotangent of x (1/tanh(x)). | Double |
| csc(x) | Returns the cosecant of x (1/sin(x)), where x is in radians. | Double |
| csch(x) | Returns the hyperbolic cosecant of x (1/sinh(x)). | Double |
| deltat( ) | Returns the duration of the current system timestep in seconds. To perform equality or comparison operations, use deltatus instead. | Double |
| deltatus( ) | Returns the duration of the current system timestep in microseconds. | Int64 |
| exp(x) | Returns the value of e raised to the x power. | Double |
| expm1(x) | Returns one less than the value of e raised to the x power ((e^x) – 1). | Double |
| fault(x,c) | Faults x with a value of c. x must be a reference to a channel and should not be a reference to a local variable. If x references a local variable, fault performs no operation. | Boolean |
| fix(x) | Rounds x to the nearest integer between x and zero and returns the rounded value. | Double |
| floor(x) | Truncates x to the next lower integer (largest integer ≤ x) and returns the truncated value. | Double |
| getlasterror( ) | Returns the numeric error code of the last error set by the Generate Error primitive. | Int32 |
| hypot(x,y) | Returns sqrt((x * x) + (y * y)) without overflowing if x and y are large values. | Double |
| isnan(x) | Determines whether x is NaN. Returns true if x is NaN. Otherwise, returns false. | Boolean |
| iteration( ) | Returns the number of iterations since the virtual machine started. | Int64 |
| ln(x) | Returns the natural logarithm of x (to the base of e). | Double |
| lnp1(x) | Returns the natural logarithm of (x + 1). | Double |
| log(x) | Returns the logarithm of x to the base of 10. | Double |
| log10(x) | Returns the logarithm of x to the base of 10. | Double |
| log2(x) | Returns the logarithm of x to the base of 2. | Double |
| max(x,y) | Compares x and y and returns the larger value. | Returns a value of the same type as the input with the largest data type. |
| min(x,y) | Compares x and y and returns the smaller value. | Returns a value of the same type as the input with the largest data type. |
| mod(x,y) | Returns the remainder of x/y, when the quotient is rounded toward –Infinity. | Returns a value of the same type as the input with the largest data type. |
| pow(x,y) | Returns x raised to the y power. | Double |
| pow10(x) | Returns 10 raised to the x power. | Double |
| pow2(x) | Returns 2 raised to the x power. | Double |
| quotient(x,y) | Returns floor(x/y), the number of times y evenly divides into x. | Returns a value of the same type as the input with the largest data type. |
| rand(max) | Returns a floating-point number between 0 and the maximum value. | Double |
| recip(x) | Returns 1/x. | Double |
| rem(x,y) | Returns the remainder of x/y, when the quotient is rounded toward zero. | Returns a value of the same type as the input with the largest data type. |
| round(x) | Rounds x to the nearest integer and returns the rounded value. | Double |
| sec(x) | Returns the secant of x (1/cos(x)), where x is in radians. | Double |
| sech(x) | Returns the hyperbolic secant of x (1/cosh(x)). | Double |
| seqtime( ) | Returns the number of elapsed seconds since the virtual machine started. To perform equality or comparison operations, use seqtimeus instead. | Double |
| seqtimeus( ) | Returns the number of elapsed microseconds since the virtual machine started. | Int64 |
| sign(x) | Returns 1 if x is greater than 0, returns 0 if x is equal to 0, and returns –1 if x is less than 0. | Returns a value of the same type as the input. |
| sin(x) | Returns the sine of x, where x is in radians. | Double |
| sinh(x) | Returns the hyperbolic sine of x. | Double |
| sqrt(x) | Returns the square root of x. | Double |
| tan(x) | Returns the tangent of x, where x is in radians. | Double |
| tanh(x) | Returns the hyperbolic tangent of x. | Double |
| tickcountms( ) | Returns the current value of the millisecond counter. | Int64 |
| tickcountus( ) | Returns the current value of the microsecond counter. | Int64 |
| ythroot(x,y) | Returns x^(1/y), the yth root of x. | Double |

Parent topic:

Adding and Editing Expressions in a Real-Time Sequence

Related reference:

- Generate Error

<!--NI_TOPIC bundle=veristand path=expressions-primitives.html language=enus -->
## TOPIC 00202: Expressions Primitives

- bundle_id: `veristand`
- source_path: `expressions-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/expressions-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assign values to and perform operations on variables in a real-time sequence. Palette object Description Assignment A simple expression statement that assigns a value to a variable. Expression A statement that can operate on variables in a real-time sequence.

### Expressions Primitives

Assign values to and perform operations on variables in a real-time
 sequence.

| Palette object | Description |
| --- | --- |
| Assignment | A simple expression statement that assigns a value to a variable. |
| Expression | A statement that can operate on variables in a real-time sequence. |

Parent topic:

Real-Time Sequence Primitives

Related reference:

- Assignment Primitive
- Expression Syntax

<!--NI_TOPIC bundle=veristand path=extended-support-changes.html language=enus -->
## TOPIC 00203: Updates and Changes for VeriStand Extended Support Versions

- bundle_id: `veristand`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/extended-support-changes.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in VeriStand versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible change

### Updates and Changes for VeriStand Extended Support Versions

Browse updates and changes made in VeriStand versions
 on extended support.

Note

Release Notes

#### VeriStand 2021 R3 New Features

Explore the new features in VeriStand 2021 R3, including
 Windows 11 support, an external mode for Simulink models, and FPGA hardware
 integration.

##### Windows 11 Support

VeriStand now supports Microsoft Windows 11. For more
 information about NI support for Windows 11, refer to NI Product Compatibility
 for Microsoft Windows 11.

##### External
 Mode for Simulink Models

Enable *external mode* when building a
 model in MathWorks MATLAB Simulink<sup>®</sup> to monitor signals in Simulink. To
 access external mode and relevant documentation, download the VeriStand Model
 Generation Support add-on and refer to *External Mode Simulations for Parameter
 Tuning, Signal Monitoring, and Code Execution Profiling*.

For more
 information on VeriStand and Simulink models, refer to .

##### HDL Coder Support Package for NI FPGA
 Hardware

*HDL Coder Support Package for NI FPGA Hardware*
 enables access to NI FPGA hardware from HDL Coder. Use this package to remain within
 HDL Coder while generating a bitfile from a Simulink model. That bitfile can then be
 imported into VeriStand with the FPGA Addon custom device. To access this
 package, visit GitHub.

##### IP
 to FPGA Conversion Utility

*IP to FPGA Conversion Utility*
 supports the conversion of Simulink models into NI FPGA bitfiles. This utility uses
 a command line interface to convert models without opening LabVIEW. For more
 information on the utility, refer to the supplemental documentation.

##### AIM MIL-STD-1553 Custom
 Device

Use the *AIM MIL-STD-1553* custom device to interact
 with AIM MIL-STD-1553 PXIe modules in VeriStand. To access this custom device, visit
 the *AIM MIL-STD-1553 Custom Device* repository on GitHub.

Related concepts:

- How VeriStand Imports Models from the Model Generation Support MATLAB Add-on

Related information:

- NI Product Compatibility for Microsoft Windows 11
- External Mode Simulations for Parameter Tuning, Signal Monitoring,
 and Code Execution Profiling
- VeriStand Model Generation Support
- FPGA Add-on Custom Device
- HDL Coder Support Package for NI FPGA Hardware
- HDL Coder Support Package for NI FPGA Hardware
- VeriStand AIM MIL-STD-1553 Custom Device

#### VeriStand 2021 R2 New Features

Explore the new features in VeriStand 2021 R2, including
 Deployment Command Center, Simulink Model Bus Support, and custom device
 enhancements.

##### Deployment Command Center

Use the *Deployment Command Center*
 to execute HIL system validation tests by performing the following actions:

- Deploy and undeploy a system configuration.
- Connect and disconnect from local or remote gateways.
- Update gateway communication settings.
- Troubleshoot project and connection errors.

Access the Deployment Command Center from the
 VeriStand Editor by clicking the tab to the right of the
 home icon ([IMAGE alt='image' src='GUID-06D9F36B-1BE7-4810-A4AE-8905219DBD01-a5.png']).

##### Simulink
 Model Bus Support

Use virtual and non-virtual buses to organize Mathworks
 Simulink<sup>®</sup> software models.

*Virtual buses* are user
 interface aids that do not generate code. *Non-virtual buses* group
 elements in memory and can generate code.

.vsmodel

- Scalar
- Vector
- Numerical two-dimensional matrix
- Boolean two-dimensional matrix
- Scalar non-virtual bus

To access this support, generate models with version 1.1 of the
 *VeriStand Model Generation Support* add-on.

##### Custom Device LLB to PPL
 Conversion

- Improve deployment time by creating a smaller disk footprint.
- Avoid load-time conflicts by granting each packaged custom device a copy of
 shared VI dependencies.
- Avoid internal naming conflicts by preserving the file hierarchy.

Use inline and inline-async templates to convert your custom devices to
 PPL and use LabVIEW advanced packaging features. You can access these templates and
 relevant documentation from the *VeriStand Custom Device Wizard*
 repository on GitHub.

For more information, refer to the *Custom Device
 Developer Handbook*.

##### AIM ARINC
 429 Custom Device

Use the AIM ARINC 429 custom device to interact with
 ARINC 429 PXIe modules in VeriStand using the AIM API. You can access this custom
 device from *VeriStand Open Source Add-Ons* on GitHub.

Related information:

- VeriStand Model Generation Support
- VeriStand Custom Device Wizard
- VeriStand Custom Device Handbook
- VeriStand Open Source Add-Ons

#### VeriStand 2021 New Features

Explore the new features in VeriStand 2021, including
 enhanced editor capabilities, updated supported environments, and improved custom device
 resources.

##### VeriStand Editor

- Add,
 delete, and configure alarms.
- Use the
 Target Log Viewer to troubleshoot unexpected engine and custom device
 behavior.
- View and adjust the target rate of a timing source from the VeriStand
 Editor configuration pane by clicking
 Document .

##### Supported Environments

- LabVIEW 64-bit
- LabVIEW RT 2021

Note

- PharLap
- Linux ARM Targets

##### Custom Devices

Build better custom devices with the following
 resources.

- Use the Custom Device Handbook to extend the VeriStand environment with LabVIEW.
 The handbook provides background, design decisions, and technical information
 required to develop custom devices.
- Use templates to convert your custom devices to PPL and use LabVIEW advanced packaging features.
 You can access these templates and relevant documentation from the Custom
 Device Wizard GitHub repository.

##### VeriStand Model Generation
 Support

Use *VeriStand Model Generation Support* MATLAB add-on
 to create VeriStand compatible models within the MathWorks Simulink<sup>®</sup>
 environment. Access this support natively from Simulink.

Related concepts:

- How VeriStand Imports Models from the Model Generation Support MATLAB Add-on

Related tasks:

- Adding and Configuring Alarms
- Viewing Real-Time Target Logs

Related information:

- Custom Device Handbook
- Custom Device Wizard
- VeriStand Model Generation Support

#### VeriStand 2020 R6 New Features

Explore the new features in VeriStand 2020 R6, including
 updates to the VeriStand Editor, FPGA Addon Custom Device, and NI-SWITCH Custom
 Device.

##### VeriStand Editor

Set the default appearance of channels on the screen.
 Click File»Preferences and select Screen to set the channel label
 location and cluster arrangement.

##### FPGA Addon
 Custom Device

FPGA Add-on Custom Devices now support all FXP datatypes
 that are also supported by LabVIEW. You can access this custom device from the
 *VeriStand FPGA Add-on Custom Device* repository on
 GitHub.

##### NI-SWITCH
 Custom Device

Use the G scripting API to modify a NI-SWITCH Custom
 Device. For more information, refer to Scripting
 Examples.lvproj in <Application Data>\LabVIEW
 20xx\examples\NI VeriStand Custom Devices\Routing and Faulting. You
 can access this custom device from the *VeriStand Routing and Faulting Custom
 Device* repository on GitHub.

Related information:

- FPGA Add-on Custom Device
- Routing and Faulting Custom Device

#### VeriStand 2020 R5 New Features

Explore the new features in VeriStand 2020 R5, including
 new editing capabilities, customizable keyboard shortcuts, and advanced FPGA and telemetry
 tools.

##### VeriStand Editor

- Modify non-active mapping diagrams while a system definition is deployed.
 Editing in other tabs will not disturb the deployed system.
- Create
 duplicates of a system definition file. Use copies of a system
 definition to easily deploy and test modifications without losing the original
 file.
- Monitor
 array-type channels while the project is running.
- Use C# to customize and extend the VeriStand Editor . You can access
 examples of implemented C# code from the VeriStand Editor Plug-in
 Examples repository on GitHub.

##### Control Keyboard Shortcut Behavior from the Command Line

Use the
 noDeployKeys command to prevent the use of the deploy and
 undeploy keyboard shortcuts during a session. You can still deploy and
 undeploy from the Operate menu.

##### FPGA Add-on
 Custom Device

- Use the Scripting API to turn FPGA bitfiles into flexible and reusable system
 definition files.
- Load and reload bitfiles without losing a previous configuration. Scalars and
 waveforms from a former bitfile remain imported while those that no longer exist
 are removed from the new bitfile.

You can access this custom device from the *VeriStand FPGA Add-on Custom
 Device* repository on GitHub.

##### Collect
 Memory Usage Data with the Telemetry Custom Device

Use the Telemetry
 Custom Device to understand the CPU and RAM usage of your system. You can access
 this custom device from the *VeriStand Telemerty Custom Device*
 repository on GitHub.

Related tasks:

- Versioning a System Definition File
- Running VeriStand Operations Using the Command Line

Related information:

- VeriStand Editor Plug-in Examples
- VeriStand FPGA Add-on Custom Device
- VeriStand Telemerty Custom Device

#### VeriStand 2020 R4 New Features

Explore the new features in VeriStand 2020 R4, including
 silent deployment, custom device API enhancements, ASAM XIL steps, alarm status monitoring,
 and real-time sequence management.

##### Launching VeriStand Silently

Deploy a system definition without launching
 the VeriStand Editor or System Explorer using the Windows
 Run command or from a language of your choice.

##### Instrument
 Add-on Custom Device

Use the Instrument Add-on custom device API to create
 a new instrument from a previously exported configuration. You can also use the API
 to add messages and to configure the command and response functionality. For more
 information, refer to the *VeriStand Instrument Add-on Custom Device*
 repository on GitHub.

##### ASAM
 XIL Steps for TestStand

Use the
 <UndeployVeriStandProjectOnDisconnect> tag in the port
 configuration XML file to specify if VeriStand is undeployed when the
 Framework is cleaned up.

##### Alarm Status Channel

Monitor the state of one or more alarms in the
 VeriStand engine with an alarm status channel.
 You can use these channels in custom devices and real-time sequences to determine
 what actions to take when an alarm state changes.

##### Stopping Groups of Real-Time
 Sequences with Procedures

Create a procedure to
 stop a specified group of real-time sequences and skip to their clean-up sections.
 You can use the procedure to shut down sequences related to a specific device under
 test (DUT) in a multi-DUT scenario. Use the Stimulus Profile
 Editor to assign a group to a real-time sequence call
 step.

Related tasks:

- Running the VeriStand Gateway Silently
- Adding an Alarm
- Adding and Configuring a Procedure

Related reference:

- ASAM XIL Port Configuration Tag Reference
- Real-Time Sequence Call Step

Related information:

- VeriStand Instrument Add-on Custom Device

#### VeriStand 2020 R3 New Features

Explore the new features in VeriStand 2020 R3, including
 enhancements to the VeriStand Editor, XNET status channels, FMU fixed parameters, and custom
 devices for FPGA.

##### VeriStand Editor

- On the Mapping Diagram , use the Focus command
 ( <Ctrl+,> ) to emphasize all mappings and nodes
 connected to a selected item. Using Focus will highlight all directly connected
 components while fading the rest of the system. Note You can interact with faded
 items while using Focus.
- In the System Definition pane, right-click an item and
 select Locate in System Explorer to navigate to the place
 in System Explorer where that item is configured.

##### XNET
 Status Channels

Monitor the XNET bus statuses for CAN, LIN, and FlexRay
 from VeriStand. In System Explorer, right-click an XNET port
 and select Add Port Specific Channels to add status channels
 to the system definition.

##### FMU
 Fixed Parameters

Set initial values for Functional Mockup Unit (FMU)
 initialization parameters during deployment through a text
 file. You can also set fixed parameter values before running a deployed
 model.

##### FPGA Add-on
 Custom Device

Use the FPGA Add-on custom device to run an FPGA bitfile
 without implementing the normal VeriStand FPGA template. The add-on allows the
 transfer of basic scalar data types inline with VeriStand's primary control loop
 (PCL) and supports reading and writing waveforms with FPGA DMA channels. You can
 access this custom device from the *VeriStand FPGA Add-on Custom Device*
 repository on GitHub.

##### Instrument
 Add-on Custom Device

Use the Instrument Add-on custom device to
 communicate with instrumentation, such as power supplies, environmental chambers,
 and emissions equipment, over various protocols. The device supports serial, GPIB
 (using NI VISA), ethernet (TCP, UDP, and NI VISA), AK serial, and AK TCP. You can
 access this custom device from the *VeriStand Instrument Add-on Custom
 Device* repository on GitHub.

Related concepts:

- Supported Syntax in Model Parameter Files

Related information:

- FPGA Add-on Custom Device
- VeriStand Instrument Add-on Custom Device

#### VeriStand 2020 R2 New Features

Explore the new features in VeriStand 2020 R2, including
 enhancements to the VeriStand Editor, FlexRay, and CAN functionalities.

##### VeriStand Editor

- Manage aliases and user channels without using System
 Explorer .
- Use the Model Signal Viewer to check signal values while a project is
 running.
- Receive warnings when a disk model is out of sync with the loaded system
 definition model.

##### FlexRay

Enable the FlexRay Allow Passive
 to Active property to permit the transition from the normal-passive to
 the normal-active state.

##### CAN

Create channels to view timing information for individual CAN
 multiplexer modes independent of the overall frame.

Related tasks:

- Creating an Alias
- Adding a User Channel
- Viewing Model Values in the VeriStand Editor

#### VeriStand 2020 New Features

Explore the new features in VeriStand 2020, including
 Mapping Diagram enhancements, open-source custom devices, and expanded DAQmx
 support.

##### Mapping Diagram

The following tasks can be completed on the Mapping
 Diagram.

- Manage Calculated
 Channels⁠ — You can now create, modify, and delete calculated
 channels from the Mapping Diagram.
- View unmapped channels and mappings — Use the Mapping Diagram Table View to see unmapped
 channels and mappings in the system definition. You can filter the table by
 selecting a node or wire.

##### Embedded Data Logger Custom Device
 Available on GitHub

The Embedded Data Logger is now an open-source custom device that installs separately
 from VeriStand. You can access this custom device from the *VeriStand Embedded
 Data Logger Custom Device* repository on GitHub. The 20.0 version includes
 the ability to automatically split and archive log files.

##### Scripting Routing and Faulting Custom
 Device Elements

Use the LabVIEW API to script Routing and Faulting Custom
 Device elements and automate fault insertion in VeriStand. The API is supported in
 LabVIEW 2017 and newer. For more information, refer to the *VeriStand Routing
 and Faulting Custom Device* repository on GitHub.

##### Support for DAQmx Waveform
 Logging

VeriStand now supports DAQmx Waveform Tasks on CompactRIO with
 DAQmx Controllers. This enables per-slot support with DAQmx, FPGA, XNET, and Scan
 Engine on supported controllers.

##### CAN
 FD Scripting

The VeriStand .NET API now supports scripting CAN ports with
 CAN FD baud rates and custom bitfields.

Related tasks:

- Adding a Calculated Channel

Related information:

- VeriStand Embedded Data Logger Custom Device
- VeriStand Routing and Faulting Custom Device

#### VeriStand 2019 R3 New Features

Explore the new features in VeriStand 2019 R3, including
 Mapping Diagram enhancements, Simulink model support, DIAdem integration, and Routing and
 Faulting Custom Device updates.

##### Mapping Diagram

The following tasks can be completed on the Mapping
 Diagram.

- Add and configure simulation models on the diagram from the palette.
- Evaluate items, such as channels and mappings, that have been added or removed
 on the Mapping Diagram. These items are highlighted after completing actions
 such as swapping a model or altering the system definition.

##### MathWorks Simulink<sup>®</sup> Software Model Toolchain Support

VeriStand
 now supports
 models from Simulink software versions R2019a and R2019b for Windows and
 Linux only. VeriStand also supports compiling Simulink models for Windows using a
 MinGW-w64 compiler.

##### TDMS
 File Viewer Support for DIAdem

VeriStand now integrates DIAdem as its
 default TDMS
 file viewer.

##### Routing and
 Faulting Custom Device

Use the Routing and Faulting Custom Device's
 switching and fault insertion modules to inject faults. For more information, refer
 to the *VeriStand Routing and Faulting Custom Device* repository on
 GitHub.

The Routing and Faulting Custom Device also supports SLSC Switch
 hardware and additional hardware. The SLSC Switch Custom Device is a VeriStand
 add-on that supports SLSC routing modules. The following modules are supported:

- SLSC-12251
- SLSC-12252
- SET-2010

SLSC Switch routing modules can be found in System Explorer
 under Targets»Controller»Hardware»SLSC»SLSC Chassis»Modules»Slot (n).

Related tasks:

- Using Models from Simulink
- Enhancing Your Workspace to View Data

Related information:

- VeriStand Routing and Faulting Custom Device
- SLSC-12251
- SLSC-12252
- SET-2010

#### VeriStand 2019 R2 New Features

Explore the new features in VeriStand 2019 R2, including
 channel mapping, target specification, and terminal customization.

The following tasks can be completed on the Mapping
 Diagram.

- Map
 channels and aliases — Use wires to connect and disconnect
 mappings.
- Specify a
 target — Select a target and use the Document 
 pane to designate the name, operating system, and IP address.
- Remove a model or calculated channel — Click and delete a model or calculated
 channel to remove it from the system definition.
- Customize terminal placement — Right-click a node and hover over
 Terminal Placement to choose the side of the node
 that inputs and outputs appear.
- Change a channel's name — Right-click a channel and select Rename
 Channel .
- Reorder channels — Click, hold, and drag the left corner of a channel to
 rearrange the list. You can also click a channel and use the
 Search dialog box to select another channel to switch
 them.

Related tasks:

- Mapping Channels and Aliases
- Specifying a Target

#### VeriStand 2019 New Features

Explore the new features in VeriStand 2019, including
 VeriStand Editor enhancements, the Mapping Diagram, PXI NI Linux RT support, and custom
 device support.

##### VeriStand Editor

You can now use the VeriStand Editor to control aspects of
 your project. The UI Manager and Project Explorer windows from previous releases of
 VeriStand have been combined into one editor. Many of the features of the Project
 Explorer window can now be accessed through Project Files in
 the Navigation pane of the VeriStand Editor. The VeriStand
 Editor also contains the Mapping Diagram to help visualize channel mappings.

Note

x86\NI\VeriStand 2019

##### Mapping Diagram

You can now visualize software mappable points within a VeriStand project with the
 Mapping Diagram. This graphical diagram allows you to see all VeriStand channels and
 the mappings between them.

Groups of mappings between two nodes are
 automatically bundled into a single wire by default to reduce clutter. If a wire
 represents multiple mappings, you can select the bundle to see more information in
 the Configuration pane.

Other features of the Mapping
 Diagram include the ability to:

- Display aliases and user channels
- Validate and debug mappings

##### PXI NI Linux RT Support

You can now deploy System Definition Files to PXI NI Linux RT targets similarly to
 previously supported targets. Benefits of supporting the NI Linux RTOS include:

- Support for newer compilation tools and
 advance C++ features.
- Support for Linux and other libraries.
- Improvement of memory handling and
 computational power.

##### Custom Device Support

VeriStand 2019 officially supports the following custom devices.

- Engine Simulation Toolkit — Provides a configuration-based experience for
 validating engine control units (ECUs).
- Scan Engine and EtherCAT — Supports easily read scanned I/O from C series
 modules in a CompactRIO or NI 914x EtherCAT chassis. This custom device also
 supports custom FPGA personalities to be used with a 914x chassis.
- SLSC 12201 DIO Module Custom — Integrates the SLSC-12201 33 V Digital I/O
 Conditioning Module into VeriStand.
- SLSC EDS Custom Device — Allows any generic SLSC Capabilities file to be used in
 VeriStand.
- Synchronization Custom Device — Synchronizes RT system time and PXI chassis
 clocks.

These custom devices can be downloaded with VeriStand 2019 using NI Package
 Manager. Check NI GitHub for updates and other custom devices.

##### CAN FD Support

VeriStand 2019 supports XNET implementation for the Controller Area Network Flexible
 Data-Rate (CAN FD) protocol. With a XNET implementation, you can now use databases
 that support CAN FD and CAN FD with Baud Rate Switching I/O modes. This
 implementation also allows calculating and using custom baud rates for a CAN
 interface. For more information on CAN FD, see Understanding CAN with Flexible
 Data-Rate (CAN FD).

##### FMI Support

VeriStand now has limited support for the Functional Mockup Interface (FMI) API
 standard on Windows and PXI LinuxRT. Use the FMI standard to create tool agnostic,
 portable solutions between modeling and simulation environments. VeriStand enables
 the configuration and execution of FMI 2.0 CoSimulation models on host and National
 Instruments Real-Time Linux64 systems.

Note

<!--NI_TOPIC bundle=veristand path=faq-models.html language=enus -->
## TOPIC 00204: Models FAQs

- bundle_id: `veristand`
- source_path: `faq-models.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/faq-models.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers to common questions on models in VeriStand. Which Simulink addon should I use to compile my model?Use VeriStand Model Generation Support. What versions of MathWorks software and the LabVIEW Development System are compatible with my version of VeriStand?Refer to VeriStand Version Compatibilit

### Models FAQs

Answers to common questions on models in VeriStand.

#### Which
 Simulink addon should I use to compile my model?

#### What
 versions of MathWorks software and the LabVIEW Development System
 are compatible with my version of VeriStand?

Refer to *VeriStand Version
 Compatibility* for a list of software you can use with
 each VeriStand distribution.

#### What
 determines the rate a model runs?

The rate at which a
 model runs is a function of the system rate and a model-specific
 decimation of the system rate, where actual model rate =
 Primary Control Loop rate / decimation. You can use
 VeriStand to set the model timing.

#### How
 do I control the latency of models and the rest of my
 system?

The Primary Control Loop (PCL) of the VeriStand
 Engine provides two execution modes. The
 default mode, *Parallel*, applies a one-cycle delay
 between when a model executes and when the data it produces is
 available to the system. Alternatively,*Low Latency*
 mode ensures data from models is available to the rest of the system
 on the same iteration of the PCL as it is generated.

#### How
 do I make my models execute in a particular
 order?

Multiple models in a system execute in parallel
 unless you define an execution order. If you want
 one model to wait until a second model finishes executing before the
 first model runs, you must define an execution order. Execution
 orders ensure data can transfer between models during the same
 iteration of the PCL.

#### How can I improve the performance of my system as
 it relates to models?

Avoid importing parameters and signals that the
 system does not use. The presence of many parameters and signals can have a negative
 impact on the performance of the system even if the model is not
 running.

Parent topic:

Integrating and Executing Models

Related concepts:

- Primary Control Loop Step Execution in Models

Related tasks:

- Setting Model Timing
- Configuring the Execution Order of Models

Related information:

- VeriStand Model Generation Support
- VeriStand Version Compatibility

<!--NI_TOPIC bundle=veristand path=faq-raw-frame-data-logging.html language=enus -->
## TOPIC 00205: Raw Frame Data Logging FAQs

- bundle_id: `veristand`
- source_path: `faq-raw-frame-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/faq-raw-frame-data-logging.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Answers to common questions on using raw frame data logging in VeriStand. When should I use raw frame data logging for NI-XNET CAN interfaces?Raw frame logging for CAN interfaces is useful when you need the exact timestamps of when messages are sent and received from the hardware. You can use a prog

### Raw Frame Data Logging FAQs

Answers to common questions on using raw frame data logging in VeriStand.

#### When should I use raw frame data logging for
 NI-XNET CAN interfaces?

Raw frame logging for CAN interfaces is useful
 when you need the exact timestamps of when messages are sent and received from the
 hardware. You can use a program such as DIAdem for post-processing of the data.
 Additionally, you can use the log files you create to replay the
 frames.

#### How does raw frame logging affect processor
 load?

The processor load added by raw frame logging depends on the bus and
 the controller. However, raw frame logging is a background process. It should not
 interrupt higher priority items, such as the Primary Control Loop (PCL) or
 models.

#### Are timestamps added to the log files?

| Log file format | Type of timestamp |
| --- | --- |
| NI-XNET (.ncl) | Contains timestamps from the NI-XNET hardware. |
| TDMS (.tdms) | Contains timestamps from the NI-XNET hardware and from the VeriStand System Time channel. |

#### How can I view the raw frame data in real
 time?

You can use the NI-XNET Bus Monitor to display CAN, FlexRay, or LIN
 network data.

#### How can I log outgoing CAN frames?

To log outgoing CAN frames, you must enable the Echo Transmit? interface option to echo the outgoing frames to the input session.

Parent topic:

Logging Incoming NI-XNET Frames

<!--NI_TOPIC bundle=veristand path=fault-channels-real-time-sequence.html language=enus -->
## TOPIC 00206: Faulting Channels in a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `fault-channels-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fault-channels-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a software fault insertion by using the fault(x,c) and clearfault(x) functions. A software fault insertion allows you to test the behavior of a system when a channel reaches a certain value. Use the following functions to perform a software fault insertion. The fault(x,c) function faults the cha

### Faulting Channels in a Real-Time
 Sequence

Use a software fault insertion by using the fault(x,c) and clearfault(x)
 functions.

software fault insertion

- The fault(x,c) function faults the channel referenced by the
 specified parameter (x) to the specified value (c). Note While the fault is
 active, it overrides any attempts to set the value of the faulted
 channel, whether from mappings or from the VeriStand
 Editor or Workspace.
- The clearfault(x) function clears any faults from the specified
 channel (x). Once cleared, any mappings resume.

1. Create a
 real-time sequence.
2. Add
 expressions that call the fault(x,c) and clearfault(x)
 functions.

In the following real-time sequence, the parameter ao0 is mapped to the system
 definition channel PXI FPGA AO0. The real-time sequence faults the value of PXI FPGA
 AO0 to -10.0, waits five seconds, and then clears the fault.

[IMAGE alt='image' src='GUID-6598C068-A6B8-431B-A6C8-D245AE3C146D-a5.gif']

Parent topic:

Creating Real-Time Sequences

Related tasks:

- Creating Real-Time Sequences
- Adding and Editing Expressions in a Real-Time Sequence

Related reference:

- Expression Functions

<!--NI_TOPIC bundle=veristand path=fmi-limitations.html language=enus -->
## TOPIC 00207: FMI Support Limitations

- bundle_id: `veristand`
- source_path: `fmi-limitations.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fmi-limitations.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Early Access FMI support has several limitations. Data with more than two dimensions is not supported. All FMI numeric data types are supported but cast to doubles internally. Arrays of numeric types in FMI 3.0 are supported but cast to doubles internally. Clock, String, Binary, and Char variables a

### FMI Support Limitations

Early Access FMI support has several limitations.

- Data with more than two dimensions is not supported.
- All FMI numeric data types are supported but
 cast to doubles internally.
- Arrays of numeric types in FMI 3.0 are supported but cast to doubles internally.
- Clock, String, Binary, and Char variables are
 not supported.
- A DefaultExperiment 
 section with a non-zero stepSize is mandatory. Models without the
 DefaultExperiment section will fail to run. Note An example of a
 working stepSize is <DefaultExperiment
 stepSize="0.01"/>.
- Changing stepSize in
 VeriStand is not supported. The only way to change stepSize is by
 modifying the modelDescription.xml file inside the FMU.
- Only Co-Simulation interface type is supported.
- Early Return and Event Mode capabilities in FMI 3.0 are not supported.
- Terminal Grouping and Icons in FMI 3.0 are not supported.

#### Configuring Stack Size for FMU Models on Linux Real-Time Targets

When running an FMU model in VeriStand on Linux Real-Time (NILRT) targets, a segmentation fault may occur if the default stack size (256 KB) is exceeded, typically due to a stack overflow.

Workaround:

For VeriStand 2023 and later, you can prevent this issue by increasing the stack size. To do this, edit the lvrt.conf file located at /etc/natinst/share and add or modify the following line:

PosixThreadStackSizeLimit = 2048

This sets the stack size to 2048 KB, helping to avoid overflow during FMU execution.

Parent topic:

FMI Support

<!--NI_TOPIC bundle=veristand path=fmi.html language=enus -->
## TOPIC 00208: FMI Support

- bundle_id: `veristand`
- source_path: `fmi.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fmi.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Functional Mock-up Interface (FMI) is an API standardization for exchanging dynamic system models. You can use FMI to decouple modeling environments from model consumers. This decoupling helps create tool-agnostic, portable solutions between modeling and simulation environments. For more informa

### FMI Support

The Functional Mock-up Interface (FMI) is an API standardization for exchanging dynamic
 system models.

You can use FMI to decouple modeling environments from model consumers. This decoupling helps
 create tool-agnostic, portable solutions between modeling and simulation environments. For
 more information, refer to the FMI website.

1. Model Exchange—The package
 contains the mathematical representation of the model and the
 simulation environment solves the equations of the model
2. Co-Simulation—The model
 contains the solver for the model and can directly provide outputs
 based on inputs and time slice.
3. Scheduled Execution [Supported only in FMI 3.0] —The model contains
 partitions that can be activated concurrently by an external
 scheduler.

FMI also defines the distribution packaging of the model and decouples the interface description
 from the actual model binaries. You can have support for several platforms, like
 Windows 64-bit, Linux 64-bit, and source code in the same package. A model that
 implements this interface is called a Functional Mockup Unit (FMU).

Parent topic:

Integrating and Executing Models

Related information:

- FMI

<!--NI_TOPIC bundle=veristand path=for-loop.html language=enus -->
## TOPIC 00209: For Loop

- bundle_id: `veristand`
- source_path: `for-loop.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/for-loop.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of statements that execute continuously for a specified number of loop iterations. Configure the code that executes in the loop by dragging expressions and other primitives to the loop and configuring them as you would any other section of sequence code. Property/Section Description Ite

### For Loop

A collection of statements that execute continuously for a specified number of loop
 iterations.

Configure the code that executes in the loop by dragging expressions
 and other primitives to the loop and configuring them as you would any other section
 of sequence code.

| Property/Section | Description |
| --- | --- |
| Iteration Count | The number of iterations the loop executes. |
| Loop Variable | Specifies the identifier, or name, for the variable that holds the current iteration count for the loop. You can use this variable in other expressions within the real-time sequence. |
| Auto Yield | If TRUE, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Loops

<!--NI_TOPIC bundle=veristand path=foreach-loop.html language=enus -->
## TOPIC 00210: ForEach Loop

- bundle_id: `veristand`
- source_path: `foreach-loop.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/foreach-loop.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of statements that executes one time for each element in the array specified by the Array Expression. Configure the code that executes in the loop by dragging expressions and other primitives to the loop and configuring them as you would any other section of sequence code. Property/Sect

### ForEach Loop

A collection of statements that executes one time for each element in the array
 specified by the Array Expression.

Configure the code that executes in the loop by dragging expressions
 and other primitives to the loop and configuring them as you would any other section
 of sequence code.

| Property/Section | Description |
| --- | --- |
| Loop Variable | Specifies the identifier, or name, for the variable that holds the current iteration count for the loop. You can use this variable in other expressions within the real-time sequence. |
| Array Expression | Defines the array of items that the loop iterates over. |
| Auto Yield | If TRUE, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Loops

<!--NI_TOPIC bundle=veristand path=format-csv-stimulus-profiles.html language=enus -->
## TOPIC 00211: CSV File Formatting for Stimulus Profiles

- bundle_id: `veristand`
- source_path: `format-csv-stimulus-profiles.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/format-csv-stimulus-profiles.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Format your CSV file column headers to define inputs, values to assign to those inputs, and timestamps to update the input values. Based on your use case, use the following column headers in your CSV file. Use Case Column header Description All timestamp Specifies the relative time from the start of

### CSV File Formatting for Stimulus
 Profiles

Format your CSV file column headers to define inputs, values to assign to those inputs,
 and timestamps to update the input values.

Based on your use case, use the following column headers in your CSV file.

| Use Case | Column header | Description |
| --- | --- | --- |
| All | timestamp | Specifies the relative time from the start of the test, in milliseconds. This column specifies when to execute the action that a row defines, such as when to update a parameter value. |
| Stimulating | ParameterName | Specifies the name of an input parameter for the real-time sequence. This column contains the values to set for the parameter at the specified timestamp. ParameterName can be any string, but the name you specify effects how VeriStand creates the default channel assignment for the parameter. As with a standard real-time sequence file, you must assign channels in your system to each input parameter you specify. You can specify an unlimited number of parameters. |
| Faulting | #FLT_STATE#ParameterName | Specifies a fault state for ParameterName at the specified timestamp. Valid values are 0 (no fault) and 1 (fault). You must use this header together with #FLT_VALUE#ParameterName. |
| Faulting | #FLT_VALUE#ParameterName | Specifies the value to force ParameterName to when #FLT_STATE#ParameterName is 1. You must use this header together with #FLT_STATE#ParameterName. |
| Evaluating | #EXP(+tol;-tol;ms delay)#ParameterName | Specifies the expected pass/fail value for the ParameterName channel. VeriStand compares the actual values of ParameterName to the values in this column to determine whether to pass or fail the test. +tol and -tol are absolute values that specify the tolerance of the test, or the range above and below the expected value within which ParameterName must be to pass. ms delay is the delay in milliseconds to add to each timestamp value before updating the expected value of ParameterName. If you specify a delay on a value at a particular timestamp, VeriStand waits for timestamp + ms delay before updating the expected value from the one at the previous timestamp. |

Note

| Use Case | Column header |
| --- | --- |
| + | Plus |
| - | Minus |
| All other invalid characters | _ (underscore) |

For all headers that include a ParameterName, VeriStand creates a
 default channel assignment based on the format of ParameterName. If
 ParameterName is a fully qualified channel path or channel alias,
 VeriStand uses the full channel or alias as the default channel assignment. Otherwise,
 VeriStand treats ParameterName as a partially qualified alias and
 creates a fully qualified alias using ParameterName as the alias name.
 This new alias is the default channel assignment.

Parent topic:

Using CSV Files as Real-Time Sequences

Related tasks:

- Creating an Alias

<!--NI_TOPIC bundle=veristand path=fpga-target-custom.html language=enus -->
## TOPIC 00212: Customizing an FPGA Target

- bundle_id: `veristand`
- source_path: `fpga-target-custom.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fpga-target-custom.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: To run a project on an FPGA target, you need a bitfile (.lvbitx) and an FPGA configuration file (.fpgaconfig). VeriStand includes bitfiles and FPGA configuration files for many FPGA targets. The default bitfiles and configuration files are sufficient for many applications. If you want to use additio

### Customizing an FPGA Target

To run a project on an FPGA target, you need a bitfile (.lvbitx)
 and an FPGA configuration file (.fpgaconfig).

Note

1. Copy the
 sample FPGA VI and project—Create a template by making a copy of a sample FPGA VI and
 project.
2. Customize
 the FPGA VI—Modify an FPGA VI to match your hardware device.
3. Compile
 the FPGA VI into a bitfile—Prepare to use your FPGA VI in an FPGA target by compiling the VI into a
 bitfile.
4. Create an
 FPGA configuration file—Create an FPGA configuration file for the host computer.

Parent topic:

Adding Custom Software

Related tasks:

- Copying the Sample FPGA VI and Project
- Customizing an FPGA VI
- Compiling a Custom FPGA VI into a Bitfile
- Creating a Custom FPGA Configuration File

<!--NI_TOPIC bundle=veristand path=fpga-vi-customization-guidelines-defaults.html language=enus -->
## TOPIC 00213: FPGA VI Customization Guidelines and Defaults

- bundle_id: `veristand`
- source_path: `fpga-vi-customization-guidelines-defaults.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fpga-vi-customization-guidelines-defaults.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When modifying an FPGA VI, be aware of the guidelines and defaults. GuidelinesUse the following guidelines to avoid creating errors. Do not modify, remove, or rename block diagram objects in the gray areas of the sample FPGA VI. Do not modify the read or write code except to change the number of pac

### FPGA VI Customization Guidelines and
 Defaults

When modifying an FPGA VI, be aware of the guidelines and defaults.

#### Guidelines

- Do not modify, remove, or rename block diagram objects in the gray areas of
 the sample FPGA VI.
- Do not modify the read or write code except to change the number of packets
 or to change the size of the array constant for the DMA read operation of
 the DMA_WRITE FIFO.
- Ensure that the name of each control is unique within the VI.
- Do not use the following control/indicator names: Loop Rate (usec), Write to
 RTSI, Use External Timing, Reset, Start, or Generate IRQ.

Note

LabVIEW
 Help

Help

»

LabVIEW Help

#### Defaults

- analog input channels 0–7
- analog output channels 0–7
- digital lines 0–39 on connectors 1 and 2
- digital lines 0–15 on connector 0

DMA_READ FIFO

DMA_WRITE FIFO

Note

Join
 Numbers

Split Number

Parent topic:

Customizing an FPGA VI

Related tasks:

- Copying the Sample FPGA VI and Project

<!--NI_TOPIC bundle=veristand path=fpga-xml-tags.html language=enus -->
## TOPIC 00214: FPGA Configuration File XML Tags

- bundle_id: `veristand`
- source_path: `fpga-xml-tags.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/fpga-xml-tags.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use XML tags and structure to customize an FPGA configuration file. The first line of the FPGA configuration file includes the XML version. All other tags inside the file must be enclosed in <FPGADMAChannelData> tags.<?xml version="1.0"?> <FPGADMAChannelData> <!-- Insert tags here --> </FPGADMAChann

### FPGA Configuration File XML Tags

Use XML tags and structure to customize an FPGA configuration file.

<FPGADMAChannelData>

```text
<?xml version="1.0"?>
<FPGADMAChannelData>
<!-- Insert tags here -->
</FPGADMAChannelData>
```

*XML schema files* (.xsd) are definition files that
 constrain an XML file to a certain format. You can add a schema file to most XML
 editing tools when writing an XML file. Use the NI VeriStand FPGA
 DMA.xsd schema file in the <Common Data>\FPGA
 directory to minimize syntax and formatting errors when you create an FPGA
 configuration file.

| Tag | Required? | Parent tag | Number of child tags | Description |
| --- | --- | --- | --- | --- |
| FPGADMAChannelData | Yes | — | — | Contains all channel definitions. |
| Version | Yes | FPGADMAChannelData | 1 | Defines which version of the channel tags you used to create the FPGA configuration file. For example, if you used the tags defined in this table, you must set the Version tag to 2.0. |
| Bitfile | No | FPGADMAChannelData | 1 | Specifies the name of the corresponding bitfile (.lvbitx). The bitfile must be saved in the same directory as the FPGA configuration file. The default value is <name of FPGA configuration file>.lvbitx. |
| Categories | No | FPGADMAChannelData | 1 | Contains multiple category definitions and describes the hierarchy of the channels visible in System Explorer. You cannot nest <Categories>. |
| Category | Yes | Categories | 0 or more | Defines a single level of the configuration tree hierarchy in System Explorer. You can nest <Category>. If you do not specify <Category> elements, the configuration tree hierarchy is inferred based on the <Category> tags contained within individual channels. |
| Name | Yes | Category | 1 | Defines the name of <Category> in System Explorer configuration tree. <Name> must be unique within its set of siblings. |
| Description | No | Category | 1 | Specifies the description of <Category> in System Explorer. |
| Symbol | No | Category | 1 | Defines the symbol for <Category> in the System Explorer window configuration tree. You can select from the following values: Default AI AO DI DO PWM In PWM Out |
| DMA_Read | Yes | FPGADMAChannelData | 1 | Contains packet definitions. Specifies the content of the DMA_Read FIFO. |
| DMA_Write | Yes | FPGADMAChannelData | 1 | Contains packet definitions. Specifies the content of the DMA_Write FIFO. |
| Packets | Yes | DMA_XXX* | 1 | Defines the number of unsigned 64-bit packets contained in the DMA FIFO. If the number of <Packet> elements is less than the number specified in <Packets>, VeriStand ignores the last <Packet>. |
| Packet | No | DMA_XXX | 1 or more | Specifies the content of a single unsigned 64-bit channel in the DMA FIFO. You do not have to use all of the available bits in a packet. You also can specify an empty packet using the <Packet/> tag with no closing tag. An empty <Packet> element specifies a packet that is to be ignored. You might want to use an empty packet for the first DMA_Read packet because the first bit of the first DMA_Read packet contains a Late Status field by default. If you specify an empty packet for the first DMA_Read packet, this unusable Late Status bit does not appear in System Explorer. If you want the Late Status bit to be visible in System Explorer, specify it as a Boolean channel in the first DMA_Read packet. |
| I8 | No | Packet | 0 or more | Specifies a signed 8-bit channel in the DMA FIFO. |
| U8 | No | Packet | 0 or more | Specifies an unsigned 8-bit channel in the DMA FIFO. |
| I16 | No | Packet | 0 or more | Specifies a signed 16-bit channel in the DMA FIFO. |
| U16 | No | Packet | 0 or more | Specifies an unsigned 16-bit channel in the DMA FIFO. |
| I32 | No | Packet | 0 or more | Specifies a signed 32-bit channel in the DMA FIFO. |
| U32 | No | Packet | 0 or more | Specifies an unsigned 32-bit channel in the DMA FIFO. |
| I64 | No | Packet | 0 or more | Specifies a signed 64-bit channel in the DMA FIFO. |
| U64 | No | Packet | 0 or more | Specifies an unsigned 64-bit channel in the DMA FIFO. |
| Boolean | No | Packet | 0 or more | Specifies a Boolean channel in the DMA FIFO. |
| FXPI32 | No | Packet | 0 or more | Specifies a fixed-point signed 32-bit channel in the DMA FIFO. Use this data type if the word length you specify in <FXPWL> is less than or equal to 32 bits. The channel occupies the full 32 bits in the packet, but only use the bits corresponding to the word length. |
| FXPU32 | No | Packet | 0 or more | Specifies a fixed-point unsigned 32-bit channel in the DMA FIFO. Use this data type if the word length you specify in <FXPWL> is less than or equal to 32 bits. The channel still occupies the full 32 bits in the packet, but only the bits corresponding to the word length are used. |
| FXPI64 | No | Packet | 0 or more | Specifies a fixed-point signed 64-bit channel in the DMA FIFO. Use this data type if the word length you specify in <FXPWL> is greater than 32 bits. The channel still occupies the full 64 bits in the packet, but only the bits corresponding to the word length are used. |
| FXPU64 | No | Packet | 0 or more | Specifies a fixed-point unsigned 64-bit channel in the DMA FIFO. Use this data type if the word length you specify in <FXPWL> is greater than 32 bits. The channel still occupies the full 64 bits in the packet, but only the bits corresponding to the word length are used. |
| PWM | No | Packet | 0 or more | Specifies a pulse width modulation (PWM) channel in the DMA FIFO. Consists of two 32-bit numbers, totaling 64 bits. The lower 32 bits represent the low time of the PWM channel. The higher 32 bits represent the high time of the PWM channel. |
| Void | No | Packet | 0 or more | Specifies unused bits in the middle of a packet. |
| Size | Yes | Void | 1 | Specifies the number of bits to ignore in a packet. |
| Name | Yes | any data type | 1 | Defines the name of the channel in System Explorer. This tag must be unique within its category. |
| Description | No | any data type | 1 | Specifies the description of the channel in System Explorer. |
| Category | No | any data type | 1 | Specifies the full path of the category where the channel should appear. If you do not specify <Category>, the default is Input for channels in the DMA_Read FIFO and Output for channels in the DMA_Write FIFO. |
| InitialValue | No | any data type | 1 | Specifies the value of the channel until its value is set. The default value is 0. Use <InitialValue> for output channels. |
| Scale | No | any data type | 1 | Specifies the range of the scale in engineering units. For PWM and fixed-point data types, the default value is 1. For all other data types, the default value is the full positive range of the data type. For example, the full positive range of the signed 8-bit data type is 127, and the full positive range of the unsigned 8-bit data type is 255. |
| Offset | No | any data type | 1 | Specifies the offset of the scale in engineering units. The default value is 1. |
| Unit | No | any data type | 1 | Specifies the units of the channel. If you do not specify the units, the channel has no units. |
| Symbol | No | any data type | 1 | Defines the symbol of the channel in System Explorer. You can select from the following values: Default AI AO DI DO PWM In PWM Out |
| FXPWL | No | any fixed-point data type | 1 | Specifies the fixed-point word length. |
| FXPIWL | No | any fixed-point data type | 1 | Specifies the fixed-point integer word length. The default value is 0. |
| PWMPeriod | No | PWM | 1 | Specifies the pulse width modulation (PWM) period for output channels. The default value is 100000. |
| Parameters | No | any data type | 1 | Specifies the parameters associated with the parent channel. |
| any data type except for Void | Yes | Parameters | 1 or more | Defines a parameter associated with the parent channel and specifies the data type of that parameter. <Parameters> accepts the same data types as <Packet>. However, Void is not a valid data type for <Parameters>. If you use the Boolean data type, or the signed or unsigned 8-bit, 16-bit, 32-bit, or 64-bit data types, the associated FPGA VI control must be of the same data type. If you use the fixed-point or PWM data types, the data type of the associated FPGA VI control must correspond as follows: FXPI32 — I32 FXPI64 — I64 FXPU32 — U32 FXPU64 — U64 PWM — U64 |
| Name | Yes | any data type except for Void | 1 | Defines the name of the parameter on the channel configuration page in System Explorer. |
| ControlName | No | any data type except for Void | 1 | Specifies the name of the associated control in the corresponding FPGA VI. The default is the same as <Name>. The control referenced in the parameter must exist in the FPGA VI. |
| InitialValue | No | any data type except for Void | 1 | Specifies the parameter value when System Explorer loads the FPGA configuration file. The default value is 0. You can change parameter values in System Explorer. You cannot change parameter values at run time. |
| Scale | No | any data type except for Void | 1 | Specifies the range of the scale in engineering units. For PWM and fixed-point data types, the default value is 1. For all other data types, the default value is the full positive range of the data type. For example, the full positive range of the signed 8-bit data type is 127, and the full positive range of the unsigned 8-bit data type is 255. |
| Offset | No | any data type except for Void | 1 | Specifies the offset of the scale in engineering units. The default value is 1. |
| * DMA_XXX denotes both DMA_Read and DMA_Write. |  |  |  |  |

Parent topic:

Creating a Custom FPGA Configuration File

Related concepts:

- DMA Scale and Offset

Related reference:

- Example FPGA Configuration File Structure

<!--NI_TOPIC bundle=veristand path=framework-model-code-interaction.html language=enus -->
## TOPIC 00215: Model Framework and Model Code Interaction

- bundle_id: `veristand`
- source_path: `framework-model-code-interaction.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/framework-model-code-interaction.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you run your VeriStand or Model Interface Toolkit test application, the application executes functions that the VeriStand Model Framework files define. These functions call functions in your model code, which convert user-defined data types, initialize your model, and increment a time step in V

### Model Framework and Model Code
 Interaction

When you run your VeriStand or Model Interface Toolkit test application, the application
 executes functions that the VeriStand Model Framework files define.

These functions call functions in your model code, which convert user-defined data types,
 initialize your model, and increment a time step in VeriStand.

The following illustration shows how NI software, the Model Framework API, and code in
 your model interact.

[IMAGE alt='image' src='GUID-DD5F0215-6FED-4542-B5C5-A6A21646D55A-a5.png']

- Writing data to model inports
- Reading data from model outports
- Allowing you to adjust model parameter values
- Allowing you to probe model signals

Parent topic:

VeriStand Model Framework

<!--NI_TOPIC bundle=veristand path=ftp-download.html language=enus -->
## TOPIC 00216: FTP Download

- bundle_id: `veristand`
- source_path: `ftp-download.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ftp-download.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downloads files from an FTP server, such as a real-time target. . Some versions of Microsoft Windows block incoming FTP traffic by default. If prompted by the OS, allow VeriStand to use port 21 (FTP) to transfer data. Property/Section Description Description Specifies a description for the current i

### FTP Download

Downloads files from an FTP server, such as a real-time target..

Note

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| FTP Server | Includes the following properties that configure access to the FTP server: URL—The address of a file or directory on the FTP server.Note The address cannot contain any characters that define the protocol. For example, 10.0.72.66/samplefile.txt is a valid address, but ftp://10.0.72.66/samplefile.txt is not. Is Folder?—If TRUE, specifies that URL is a folder. If FALSE, specifies that URL is a specific file. Filter—If the path to the files to transfer is a folder, specifies a regular expression to use to filter the files in the folder by filename. Note This step only acts on the files that match the regular expression. The match is not case-sensitive. Username—Specifies the username to use to access the FTP server. Password—Specifies the password for Username. Timeout—Specifies the time in seconds to wait for a response from the FTP server before returning a timeout error. Passive Connection—If TRUE, specifies that this step initiates a connection on the FTP data port. If FALSE, specifies that this step listens for a connection on the FTP server. SSL—If TRUE, specifies that data transmission is encrypted using an SSL protocol. |
| FTP Transfer | Includes the following properties that configure details of the file transfer: Destination—The destination directory for downloaded files. If you do not specify a destination, this step downloads files to the directory that contains the stimulus profile. Binary—If TRUE, transmits data in binary form. If FALSE, transmits data as text. Behavior—Specifies the action to take if a file of the same name already exists in the Destination directory. Overwrite—Overwrites the existing file. This option does not change the creation date of the file, but it does change the most recent access date. Skip—Skips the file completely and does not include it in the download. Unique—Downloads the file and appends a number to the filename to create a unique name. Buffer Length—The size of the buffer, in bytes, to use for streaming data. The minimum is 2. |
| Proxy | Includes the following properties for configuring a proxy server: Enable Proxy—If TRUE, specifies to transmit data through a proxy server. Proxy URL—Specifies the URL of the proxy server. Proxy Username—Specifies the username for the proxy server. Proxy Password—Specifies the password for the Proxy Username. |
| Port | Includes the following property that configures which port the proxy server uses: Proxy Port—Specifies the port the FTP proxy uses. If Enable Proxy is FALSE, this value is ignored. |

Parent topic:

FTP Steps

<!--NI_TOPIC bundle=veristand path=ftp-steps.html language=enus -->
## TOPIC 00217: FTP Steps

- bundle_id: `veristand`
- source_path: `ftp-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ftp-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interact with files on an FTP server, such as a real-time target. Palette object Description FTP Download Downloads files from an FTP server, such as a real-time target. FTP Upload Uploads a file to an FTP server, such as a real-time target.

### FTP Steps

Interact with files on an FTP server, such as a real-time target.

| Palette object | Description |
| --- | --- |
| FTP Download | Downloads files from an FTP server, such as a real-time target. |
| FTP Upload | Uploads a file to an FTP server, such as a real-time target. |

Parent topic:

Other Steps

Related reference:

- FTP Download
- FTP Upload

<!--NI_TOPIC bundle=veristand path=ftp-upload.html language=enus -->
## TOPIC 00218: FTP Upload

- bundle_id: `veristand`
- source_path: `ftp-upload.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ftp-upload.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uploads a file to an FTP server, such as a real-time target. Some versions of Microsoft Windows block incoming FTP traffic by default. If prompted by the OS, allow VeriStand to use port 21 (FTP) to transfer data. Property/Section Description Description Specifies a description for the current item.

### FTP Upload

Uploads a file to an FTP server, such as a real-time target.

Note

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| FTP Server | Includes the following properties that configure access to the FTP server: URL—The address of a file or directory on the FTP server.Note The address cannot contain any characters that define the protocol. For example, 10.0.72.66/samplefile.txt is a valid address, but ftp://10.0.72.66/samplefile.txt is not. Username—Specifies the username to use to access the FTP server. Password—Specifies the password for Username. Timeout—Specifies the time in seconds to wait for a response from the FTP server before returning a timeout error. Passive Connection—If TRUE, specifies that this step initiates a connection on the FTP data port. If FALSE, specifies that this step listens for a connection on the FTP server. SSL—If TRUE, specifies that data transmission is encrypted using an SSL protocol. |
| FTP Transfer | Includes the following properties that configure details of the file transfer: Source—The path to the source file(s) to upload. This can be a file or a folder containing multiple files. Is Folder?—If TRUE, specifies that URL is a folder. If FALSE, specifies that URL is a specific file. Filter—If the path to the files to transfer is a folder, specifies a regular expression to use to filter the files in the folder by filename. Note This step only acts on the files that match the regular expression. The match is not case-sensitive. Binary—If TRUE, transmits data in binary form. If FALSE, transmits data as text. Behavior—Specifies the action to take if a file of the same name already exists in the Destination directory. Overwrite—Overwrites the existing file. This option does not change the creation date of the file, but it does change the most recent access date. Skip—Skips the file completely and does not include it in the download. Unique—Downloads the file and appends a number to the filename to create a unique name. Buffer Length—The size of the buffer, in bytes, to use for streaming data. The minimum is 2. |
| Proxy | Includes the following properties for configuring a proxy server: Enable Proxy—If TRUE, specifies to transmit data through a proxy server. Proxy URL—Specifies the URL of the proxy server. Proxy Username—Specifies the username for the proxy server. Proxy Password—Specifies the password for the Proxy Username. |
| Port | Includes the following property that configures which port the proxy server uses: Proxy Port—Specifies the port the FTP proxy uses. If Enable Proxy is FALSE, this value is ignored. |

Parent topic:

FTP Steps

<!--NI_TOPIC bundle=veristand path=generate-error.html language=enus -->
## TOPIC 00219: Generate Error

- bundle_id: `veristand`
- source_path: `generate-error.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/generate-error.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create and return a user-defined error code and message in the stimulus profile test results file. You can also configure this primitive to stop the sequence and skip to the clean-up tasks or to immediately abort the sequence without performing clean-up tasks. Only the most recent error appears in t

### Generate Error

Create and return a user-defined error code and message in the stimulus profile test
 results file.

You can also configure this primitive to stop the sequence and skip to the clean-up
 tasks or to immediately abort the sequence without performing clean-up tasks. Only
 the most recent error appears in the test results file because the most recent error
 overwrites any previous error that occurred.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Error Code | Specifies the numeric value to return. |
| Message | Specifies a string that you want to append to the Error Code in the test results file. |
| Action to Take | Specifies how to proceed through the remainder of the real-time sequence: ContinueSequenceExecution—Continues normal execution of the real-time sequence. StopSequence—Halts execution and runs the tasks under the Clean Up node. AbortSequence—Immediately halts execution without running tasks under the Clean Up node. |

```text
Outcome: Error: 55. Details: <append> ========================= NI VeriStand: Alert! The Engine Temperature is outside the critical range. Shutting down the engine.
```

Parent topic:

Miscellaneous Primitives

<!--NI_TOPIC bundle=veristand path=generate-errors-real-time-sequence.html language=enus -->
## TOPIC 00220: Generating Errors in a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `generate-errors-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/generate-errors-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a real-time sequence to return user-defined error codes and messages in the stimulus profile test results file. Create a real-time sequence. Add a Generate Errors primitive to the sequence code. This primitive also allows you to stop the sequence and skip to the clean-up tasks or to immedi

### Generating Errors in a Real-Time
 Sequence

Configure a real-time sequence to return user-defined error codes and messages in the
 stimulus profile test results file.

1. Create a
 real-time sequence.
2. Add a Generate Errors primitive to the sequence code. 
 Note This primitive also allows you to stop the sequence and skip to the
 clean-up tasks or to immediately abort the sequence without performing
 clean-up tasks.
3. If you need to clear or access an error later in the sequence, create an
 expression in the Property Browser that
 implements a function. 
 Goal
FunctionClear the last error so it does not appear in the test
 results file.
clearlasterror
Return the numeric error code of the last error.
getlasterror

Outcome: Error: 55. Details:
 <append>========================= VeriStand: Alert! The Engine Temperature is
 outside the critical range. Shutting down the engine.

Parent topic:

Creating Real-Time Sequences

Related tasks:

- Creating Real-Time Sequences
- Adding and Editing Expressions in a Real-Time Sequence
- Viewing Stimulus Profile Test Results

Related reference:

- Generate Error

<!--NI_TOPIC bundle=veristand path=generating-pdf-html-report-diadem.html language=enus -->
## TOPIC 00221: Generating a PDF or HTML Report with DIAdem

- bundle_id: `veristand`
- source_path: `generating-pdf-html-report-diadem.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/generating-pdf-html-report-diadem.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a pre-configured DIAdem report file (.TDR) to automatically generate a PDF or HTML report from log files. A DIAdem report file can display graphs, texts, and images based on the data from the loaded log files. Click Edit settings on the data logging control. Select Post-Processing. From the Repo

### Generating a PDF or HTML Report with
 DIAdem

Use a pre-configured DIAdem report file (.TDR) to automatically generate
 a PDF or HTML report from log files.

A DIAdem report file can display graphs,
 texts, and images based on the data from the loaded log files.

1. Click Edit settings on the data logging control.
2. Select Post-Processing.
3. From the Report generation options drop
 down menu, select Generate HTML
 report or Generate PDF
 report.
4. Specify the Report template path to the
 report template and the Report export
 path where you want to save the PDF or
 HTML report.

Parent topic:

Loading a File in DIAdem

<!--NI_TOPIC bundle=veristand path=group.html language=enus -->
## TOPIC 00222: Group

- bundle_id: `veristand`
- source_path: `group.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/group.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Groups steps with no impact on execution. You can use groups to organize your code. Because a Group is a single item, using groups makes it easy to move or duplicate a set of steps. Property/Section Description Group Name The name of the group. Description Specifies a description for the current ite

### Group

Groups steps with no impact on execution.

You can use groups to organize your code. Because a Group is a
 single item, using groups makes it easy to move or duplicate a set of steps.

| Property/Section | Description |
| --- | --- |
| Group Name | The name of the group. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Other Steps

<!--NI_TOPIC bundle=veristand path=hardware-synchronization-types.html language=enus -->
## TOPIC 00223: Hardware Synchronization Types

- bundle_id: `veristand`
- source_path: `hardware-synchronization-types.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/hardware-synchronization-types.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Time-Based and Signal-Based Synchronization to coordinate hardware device timing in a system. In Time-Based Synchronization, each piece of time-based hardware shares a common wall-clock time reference. For test and measurement hardware, there are many industry standards for time such as IEEE 158

### Hardware Synchronization Types

Use Time-Based and Signal-Based Synchronization to coordinate hardware device timing in a
 system.

In *Time-Based Synchronization*, each piece of time-based hardware shares a
 common wall-clock time reference. For test and measurement hardware, there are many
 industry standards for time such as IEEE 1588, GPS, network time protocol (NTP), pulse
 per second (PPS), and inter-range instrumentation group (IRIG) time codes.

With *Signal-Based Synchronization*, the system uses physical hardware pulses
 as a reference for events. Each piece of signal-based hardware in the system shares a
 hardware clock. The clock can be a shared Sample Clock or a high-frequency Reference
 Clock. Each signal-based device derives a Sample Clock and a shared start trigger from
 the shared clock. When multiple signal-based devices are synchronized, they update I/O
 simultaneously and also drift by the same number of samples over a time period.

The following table displays common use cases for each type of hardware
 synchronization.

| Synchronization Type | Use Case |
| --- | --- |
| Time-Based | Correlate data logged by time-based devices, such as XNET devices. Initiate I/O sampling across time-based devices. |
| Signal-Based | Simultaneously sample I/O across several different data acquisition devices. Update the PWM duty cycle of an FPGA device. Update analog outputs of data acquisition devices. |

Parent topic:

Synchronizing Hardware and Software

<!--NI_TOPIC bundle=veristand path=host-side-logging.html language=enus -->
## TOPIC 00224: Configuring and Executing Host-Side Logging

- bundle_id: `veristand`
- source_path: `host-side-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/host-side-logging.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the Data Logging control for host-side logging by setting channels, log triggers, session properties, and post-processing actions. Open the Workspace. Select Screen Edit Mode to display the Workspace Controls palette and alignment grid. Click the Workspace Controls palette. Select Logging

### Configuring and Executing Host-Side
 Logging

Configure the Data Logging control for host-side logging by setting channels, log
 triggers, session properties, and post-processing actions.

1. Open the Workspace.
2. Select Screen»Edit Mode to display the Workspace Controls palette and
 alignment grid.
3. Click the Workspace Controls palette.
4. Select Logging»Logging Control and drag the control onto the alignment grid.
5. Complete any of the following configuration goals in the Edit
 Settings dialog box. 
 Goal
Description
How to configureSpecify channels to log
Designate the channels to log data from.
Use the Channels page.
Start and stop a log session with triggers
Configure the Data Logging control to start and stop logging during a log
 session based on triggers. A trigger is a condition-based formula, such as
 EngineTemp>5000.
When you configure a start trigger, the Data Logging control waits after a
 log session begins for the start trigger to evaluate to TRUE
 before logging.
You can also configure a stop trigger. When you configure a stop trigger, the
 Data Logging control stops logging when the stop trigger evaluates to
 TRUE.
Use the Start Trigger and
 Stop Trigger pages.
Capture custom information about a log session
Capture specific information from an operator at the start of a log session
 using properties. Any captured properties are added as metadata to all log
 files generated during the log session.
For example, you can prompt an operator to enter information, such as the
 their name, the unit under test, and the test set point before running a log
 session.
Use the Properties page.
Automate post-processing of log data
Configure the Data Logging control to automatically run post-processing
 actions for log files produced by the control during a log session.
This allows you to automate post-processing actions, such as passing log
 files to Excel or generating a PDF report from the log files.
Use the Post-Processing
 page.See Running a Command Line Script and Loading a File
 in DIAdem.
Download log files produced by targets
Configure the Data Logging control to automatically download
 files produced by a target and to include these files in
 post-processing.
Use the Target Logs page.See
 Including
 Log Files Produced on a Target in Post-Processing.

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Running a Command Line Script
- Loading a File in DIAdem
- Including Log Files Produced on a Target in Post-Processing
- Logging and Documenting Sessions

<!--NI_TOPIC bundle=veristand path=host.html language=enus -->
## TOPIC 00225: Host Computer

- bundle_id: `veristand`
- source_path: `host.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/host.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A host computer hosts the screen files that serve as the user interface for operators and runs the VeriStand Gateway. The host computer must be a PC running a supported version of Windows. Internal Feature VeriStand Gateway—Creates a TCP/IP communication channel that facilitates communication with t

### Host Computer

A host computer hosts the screen files that serve as the user interface for operators
 and runs the VeriStand Gateway.

Note

#### Internal Feature

VeriStand Gateway—Creates a TCP/IP communication channel that facilitates
 communication with the VeriStand Engine over the network. The VeriStand Gateway
 receives channel values from the VeriStand Engine and stores them in a table. You
 can view these values using the Channel Data Viewer tab in VeriStand
 Editor or the Channel Data Viewer workspace tool. If you run a
 project on a desktop PC, the VeriStand Gateway initiates the VeriStand Engine.

If you run a project on an real-time target, the VeriStand Gateway
 synchronizes with the system definition file that is running on the RT target. If
 the system definition file currently running on the VeriStand Engine does not match
 the system definition that the VeriStand Gateway expects, then the VeriStand Gateway
 does not synchronize with the system definition file running on the RT target.

#### Interactive Features

- Project File—The .nivsprj file
 that defines high-level settings, such as:
  - The screen and system
 definition files to run
  - Available users and their
 permissions for the project
  - The list of tools you can
 launch from the Tools Launcher
  - Which services run when you
 deploy a project to the target
  - The IP address of the
 VeriStand Gateway
  - Stimulus profiles and
 real-time sequences
- Screen File—The .nivsscr or
 .nivsscreen files that define the configuration and
 settings for the screens and display items you view in the
 VeriStand Editor or Workspace ,
 respectively
- Stimulus profile—A test executive that can call real-time sequences, open and close VeriStand projects, and perform data-logging and pass/fail analysis. It also connects real-time sequences to system definition files to bind channel data within the system definition file to variables in the real-time sequence. Stimulus profiles execute on the host computer. You create and run a stimulus profile using the Stimulus Profile Editor.
- National Instruments Driver Software—You need the appropriate driver software to communicate with hardware installed on a target. For a list of the required driver software, see the VeriStand Readme located at 
 <Program Files>\National Instruments\NI VeriStand\readme\readme.html . If you installed VeriStand to a different location, locate the readme directory in the install location you specified.

Parent topic:

Components of a VeriStand Project

<!--NI_TOPIC bundle=veristand path=identify-local-global-parameter.html language=enus -->
## TOPIC 00226: Identifying Local and Global Parameters

- bundle_id: `veristand`
- source_path: `identify-local-global-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/identify-local-global-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use VeriStand to determine if your parameters are local or global. Before you begin, add a model and import parameters. Local parameters apply to a specific subsystem, or block, in the owning model. Local parameters allow you to independently adjust a common parameter for multiple instances of the s

### Identifying Local and Global
 Parameters

Use VeriStand to determine if your parameters are local or global.

Before you begin, add a model and import
 parameters.

*Local parameters* apply to a specific subsystem, or block, in the owning
 model. Local parameters allow you to independently adjust a common parameter for
 multiple instances of the same block.

*Global parameters*, by default, apply to the current model and to any
 global parameters with the same name in other models on the target. You can restrict
 global parameters in a model from applying to other models by configuring the scope of the
 global parameters. Global parameters are similar to workspace variables
 in MathWorks MATLAB<sup>®</sup> software.

A parameter *expression* contains the model name that appears in the
 System Explorer configuration tree. Every parameter also
 has an associated path that contains the name the model was compiled under. The
 expression of a global parameter also indicates whether its scope is at the
 target-level or the model-level.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Simulation Models»Models in the configuration tree.
4. Click a model.
5. Click Parameters and select a parameter.
6. On the Parameter Configuration page, review the parameter
 information.
7. Based on the model's expression and characteristics, determine the parameter
 type. 
 Example expression
Characteristic
Parameter typeSine Wave/Block1/Amplitude
The root of the Amplitude parameter is a
 block rather than a model.
Local
Sine Wave/Amplitude
The root of Amplitude is the owning
 model.
Global, model-level scope
Amplitude
The root of Amplitude is not a specific
 model.
Global, target-level scope
Note The name of the owning
 model in the system definition is Sine Wave.

Parent topic:

Scoping Global Parameters

Related tasks:

- Adding and Configuring a Model
- Scoping Global Parameters

<!--NI_TOPIC bundle=veristand path=if-else.html language=enus -->
## TOPIC 00227: If Else

- bundle_id: `veristand`
- source_path: `if-else.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/if-else.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A statement that defines an expression to evaluate to determine whether to execute one section of code or another. When you add an If Else statement to your real-time sequence code, the editor automatically generates Then and Else blocks under the statement. If the Test Expression evaluates to TRUE,

### If Else

A statement that defines an expression to evaluate to determine whether to execute
 one section of code or another.

When you add an If Else statement to your real-time sequence code,
 the editor automatically generates Then and
 Else blocks under the statement. If the Test
 Expression evaluates to TRUE, the statement executes the code under
 the Then block. If the expression evaluates to FALSE, the
 statement executes the code under the Else block.

To specify the code that each block executes, drag expressions and other primitives
 to the blocks and configure them as you would any other section of sequence code.

| Property/Section | Description |
| --- | --- |
| Test Expression | Specifies the expression to evaluate to determine the code to execute. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Conditional Statements

<!--NI_TOPIC bundle=veristand path=import-export-scale-mapping-text.html language=enus -->
## TOPIC 00228: Importing and Exporting Scale Mappings

- bundle_id: `veristand`
- source_path: `import-export-scale-mapping-text.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-export-scale-mapping-text.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Save and import the mappings of scales to channels using text files. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Right-click Scales and select Map Scales. In the Scale Mappings dialog

### Importing and Exporting Scale Mappings

Save and import the mappings of scales to channels using text files.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Right-click Scales and select Map
 Scales.
4. In the Scale Mappings dialog box, complete the following
 tasks. 
 Goal
 TaskImport a scale mapping.
 Click Import and select the file
 you want to import.Note The
 system definition file that you import scale mappings
 into must have matching scale and channel
 names.
 Export a scale mapping.
 Click Export and select a
 destination to save the text file.
5. Save the system definition file.

Parent topic:

Mapping Scales to Channels

<!--NI_TOPIC bundle=veristand path=import-manage-batch-model-parameters-workspace.html language=enus -->
## TOPIC 00229: Importing and Managing Batches of Model Parameters in the Workspace

- bundle_id: `veristand`
- source_path: `import-manage-batch-model-parameters-workspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-manage-batch-model-parameters-workspace.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Import model parameter values from external .m or .txt files, then review and apply them to a deployed system. Manage multiple parameter batches in the Workspace with the Model Parameter Manager. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Ad

### Importing and Managing Batches of Model
 Parameters in the Workspace

Import model parameter values from external .m or
 .txt files, then review and apply them to a deployed system. Manage
 multiple parameter batches in the Workspace with the Model Parameter Manager.

Workspace

Tools

In order to set the value of a parameter, you must import or calculate the new values and then apply the new values.

1. Deploy the
 system definition with models to the target. 
 Note You can only apply new
 values to deployed systems.
2. In the Workspace, select Tools»Model Parameter Manager to launch the tool. 
 Note The name of this menu item might differ
 depending on how you named it in the Tools Properties
 dialog box.
3. In the Model Parameter Manager tool, click
 Select Files.
4. In the Select Calibration Files to Load dialog box, click
 Add File.
5. Browse to the file(s) that contain parameter values, and click
 OK. 
 Note You can import parameter
 values from multiple model parameter files. However, only one file can
 define a specific parameter. Otherwise, VeriStand requires you to select the
 value to apply.
6. In the Select Calibration Files to Load dialog box, click
 OK to import the values from the files as new values.
7. In the Model Parameter Manager, review the New Value
 column for errors. 
 Note If an error glyph ([IMAGE alt='image' src='GUID-5E2F367B-58FE-4F60-8B5C-FDAA2C68C8FC-a5.gif']) appears next to a
 Parameter, ensure your files use supported
 syntax.
8. Double-click a file in the Selected Files column to edit
 the contents of the file.
9. Click Calc. New Values to read or calculate new
 parameters values from files you loaded. 
 Note This is useful for
 resetting parameters to their initial values.
10. Click Apply New.

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Deploying the System Definition File to a Real-Time Target
- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=import-models-model-generation-support.html language=enus -->
## TOPIC 00230: How VeriStand Imports Models from the Model Generation Support MATLAB Add-on

- bundle_id: `veristand`
- source_path: `import-models-model-generation-support.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-models-model-generation-support.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: VeriStand identifies inports, outports, parameters, and signals in models you created in Simulink software according to their configuration in Simulink. A simple model in Simulink might contain the following components. When you add this model to a system definition in VeriStand, its components appe

### How VeriStand Imports Models from the
 Model Generation Support MATLAB Add-on

VeriStand identifies inports, outports, parameters, and signals in models you
 created in Simulink software according to their configuration in
 Simulink.

A simple model in Simulink might contain the following components.

[IMAGE alt='image' src='GUID-6347F6AF-016E-431D-AD84-5972030E1435-a5.gif']

| Component in model | Type of component in VeriStand |
| --- | --- |
| Sine_Gain | Parameter |
| In1 | Inport |
| Out1 | Outport |

#### Signal
 Importing

To import signals, enable the signal for export
 before compiling the model. In Simulink, navigate to Code Generation»Interface to enable signal export and designate the required
 signals as test points.

Note

#### Simulink External
 Mode

To visualize signals and tune parameters, enable
 Simulink external mode before building an imported model. Refer to
 *External Mode Simulations for Parameter Tuning, Signal
 Monitoring, and Code Execution Profiling* for more
 information.

Note

After importing and deploying a model in
 VeriStand, connect to the model in Simulink by specifying the target
 IP address and port number. Determine the port number by referring
 to the ExternalMode/Port parameter. Once connected,
 use Simulink to visualize signals and tune parameters.

Note

#### Parameter
 Importing

- They are of a supported datatype.
- They are referenced by at least one Simulink block or
 Model Mask.

#### Inport and Outport
 Importing

Top-level Simulink inports and outports become VeriStand inports and outports. Inports and
 outports in subsystems are accessible when connected to the
 VeriStand Inport/Outport blocks.

#### Importing Models with
 Referenced Models and Model Masks

VeriStand supports
 importing models that use Referenced Models and models under Model
 Masks. Their Inports and Outports will not be available, but any
 variable referenced by those models will be available as a
 parameter.

Note

Parent topic:

Using Models from Simulink

Related information:

- External Mode Simulations for Parameter Tuning, Signal Monitoring,
 and Code Execution Profiling
- VeriStand Model Generation Support

<!--NI_TOPIC bundle=veristand path=import-models-simulink-framework.html language=enus -->
## TOPIC 00231: How VeriStand Imports Simulink Models using the Model Framework

- bundle_id: `veristand`
- source_path: `import-models-simulink-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-models-simulink-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: VeriStand identifies inports, outports, parameters, and signals in models you created in Simulink software according to their configuration in Simulink. A simple model in Simulink might contain the following components. When you add this model to a system definition in VeriStand, its components appe

### How VeriStand Imports Simulink Models using
 the Model Framework

VeriStand identifies inports, outports, parameters, and signals in models you created in
 Simulink software according to their configuration in Simulink.

A simple model in Simulink might contain the following components.

[IMAGE alt='image' src='GUID-6347F6AF-016E-431D-AD84-5972030E1435-a5.gif']

| Component in model | Type of component in VeriStand |
| --- | --- |
| Raw_Sine | Signal |
| Sine_Gain | Parameter |
| In1 | Inport |
| Out1 | Outport |

Note

#### Signal Importing

Note

#### Parameter
 Importing

- Global parameters , by default, applies to
 the current model and to any global parameters with
 the same name in other models on the target. This
 parameter is similar to a workspace variable in
 MathWorks MATLAB ® software. If you set
 inline parameters in the Simulink software,
 MathWorks Real-Time Workshop ® software
 converts MATLAB workspace variables to global
 parameters in the compiled model.
- Local parameters only apply to the specific
 model and block or subsystem that they belong to. If
 you do not set inline parameters in Real-Time
 Workshop, block parameters remain block parameters
 in the compiled model.

A Simulink model can contain only one type of parameter. However, a
 system definition can contain a model with global parameters and a
 model with block parameters.

VeriStand supports model references to submodels, but you cannot access
 parameters in submodels. Submodels execute in a VeriStand system,
 but their parameters are not available for mapping.

In Simulink, you can inline parameters. In VeriStand, inlined parameters
 are not available for configuration. However, even if you inline a
 parameter in Simulink, you still can allow users to influence the
 parameter by configuring a variable that affects the parameter to be
 tunable. For more information, refer to *Tune and Experiment
 with Block Parameter Values*.

- Contains a constant configured with an expression (x +
 3).
- Contains a sine wave block whose amplitude and frequency
 parameters are inlined, and therefore unavailable in
 VeriStand.
- Adds the result of the constant to the output from the
 sine wave block.

Although the parameters of the sine wave block are unavailable, you can
 influence the operation by specifying that the
 x variable is tunable in Simulink.
 After you add the model to VeriStand, when x
 is tunable, it will appear in the Parameters
 list in System Explorer. You can change the
 value of x as the model executes.

#### Inport and Outport Importing

Top-level Simulink inports and outports become VeriStand inports and outports. Submodel
 inports and outports in Simulink import only if you place VeriStand inport and outport
 blocks within the submodel in Simulink.

Parent topic:

Using Models from Simulink

Related information:

- Tune and Experiment with Block Parameter Values

<!--NI_TOPIC bundle=veristand path=import-scale-text.html language=enus -->
## TOPIC 00232: Importing Scale Values from a Text File

- bundle_id: `veristand`
- source_path: `import-scale-text.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-scale-text.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Import lookup table scale values or polynomial scale coefficients from a formatted text file. Before you import a text file, format that file. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explore

### Importing Scale Values from a Text
 File

Import lookup table scale values or polynomial scale coefficients from a
 formatted text file.

Before you import a text file, format that file.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Create a new lookup table scale or polynomial scale.
4. On the Lookup Table Configuration or
 Polynomial Scale Configuration
 page, click Import.
5. Select a text file that contains scale values and click
 OK.
6. In the Import Table Values or
 Import Polynomial Coefficients
 dialog box, import values from the text file, and click
 OK. 
 Note VeriStand imports polynomial coefficient values
 depending on the value in the Coefficients drop-down
 menu.
7. Save the system definition file.

Maintain the text file to allow reuse in
 multiple system definitions.

Parent topic:

Scaling a Channel on Hardware Devices

Related tasks:

- Defining Scale Values in a Text File
- Creating a Lookup Table Scale
- Creating a Polynomial Scale

<!--NI_TOPIC bundle=veristand path=import-scales-other.html language=enus -->
## TOPIC 00233: Importing Scales from Another Application

- bundle_id: `veristand`
- source_path: `import-scales-other.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-scales-other.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Import custom scales from another system definition file or from NI-DAQmx into a VeriStand system definition file. The scale names you import must not duplicate scale names already in the system definition file. You can import NI-DAQmx custom scales saved in MAX on the host computer. You can also im

### Importing Scales from Another
 Application

Import custom scales from another system definition file or from NI-DAQmx into a
 VeriStand system definition file.

The scale names you import must not duplicate scale
 names already in the system definition file.

You can import NI-DAQmx
 custom scales saved in MAX on the host computer. You can also import
 NI-DAQmx custom scales exported from MAX as an INI file. VeriStand does not
 support map range scales from MAX.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Right-click Scales and select
 Import Scales.
4. In the Import Scales dialog box, select
 the type of scale to import.
5. Save the system definition file.

Parent topic:

Scaling a Channel on Hardware Devices

<!--NI_TOPIC bundle=veristand path=import-xnet-frames.html language=enus -->
## TOPIC 00234: Importing NI-XNET Frames

- bundle_id: `veristand`
- source_path: `import-xnet-frames.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/import-xnet-frames.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Imports incoming or outgoing NI-XNET frames from an NI-XNET database into VeriStand for embedded network communication. Before you begin, add an NI-XNET database and port. Frames are the messages transmitted across an embedded network. These messages are sorted into clusters within an NI-XNET databa

### Importing NI-XNET Frames

Imports incoming or outgoing NI-XNET frames from an NI-XNET database into VeriStand
 for embedded network communication.

Before you begin, add an NI-XNET database and
 port.

Frames

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Hardware»Chassis»NI-XNET in the configuration tree.
4. Expand an NI-XNET LIN, FlexRay, or CAN port.
5. Expand Incoming or
 Outgoing.
6. Right click a frame type you want to import and select Import
 Frames.
7. In the Import NI-XNET Frames dialog box, click the XNET
 Frames tab, and select the frames you want to import. 
 You can also use the options on the Import Settings and
 General Options tabs to temporarily modify the
 default settings for importing frames. For example, you can import the
 frames in signal or raw data format, create information channels for the
 frames, or allow disable and trigger channels for frame transmission.
Note Configure default settings
 for importing frames on the XNET page of the Options dialog box.
8. Click OK.
9. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Adding NI-XNET Databases
- Adding an NI-XNET Port

<!--NI_TOPIC bundle=veristand path=imported-double-array-variable.html language=enus -->
## TOPIC 00235: Imported Double Array Variable

- bundle_id: `veristand`
- source_path: `imported-double-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/imported-double-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of Boolean values. To create this type of variable, right-click Local Variables in the Variables pane and select Import Double Array from File. In the file dialog box that displays, select a file whose data you want to import. The Import Double Array from File dialog box displays, which you

### Imported Double Array Variable

An array of Boolean values.

To create this type of variable, right-click Local Variables
 in the Variables pane and select Import Double
 Array from File. In the file dialog box that displays, select a file
 whose data you want to import. The Import Double Array from File dialog box
 displays, which you use to select which channels you want to import as local
 variables, specify how much data to import, and preview the channel data. When you
 click OK, the variable(s) appear in the list of local
 variables.

Note

Variables

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Properties | Includes the following properties that allow you to select an import file or that display information about the data that VeriStand will import from File Path: File Path—Specifies the path of the file from which to import values. You can change the import file after you create the variable; however, you cannot change other properties you set in the Import Double Array from File dialog box when you create the variable, such as the Number of Values Channel—Displays the name of the channel in the import file that contains data you want to import. Channel Group—Displays the name of the group in the import file that owns the Channel. Subset Start Value—Displays the index of the first value imported from the file. Number of Values—Displays the number of values imported from the file, starting at the Subset Start Value index. Offset—Displays the amount by which channel values are offset along the y-axis. Scale—Displays the multiplier by which channel values are scaled along the y-axis. |
| Units | Specifies the units to associate with the variable value. If the channel has associated units in the import file, VeriStand uses those units. You can change the Units after you import the local variable. |

Parent topic:

Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=improve-model-performance.html language=enus -->
## TOPIC 00236: Improving Model Performance

- bundle_id: `veristand`
- source_path: `improve-model-performance.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/improve-model-performance.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase model performance by consolidating small models and preallocating arrays for LabVIEW models. To optimize your model performance, complete any of the following tasks. Task Rationale Consolidate small models into one large model. Several small models use more memory than one large model. Prea

### Improving Model Performance

Increase model performance by consolidating small models and preallocating
 arrays for LabVIEW models.

To optimize your model performance, complete any of the following tasks.

| Task | Rationale |
| --- | --- |
| Consolidate small models into one large model. | Several small models use more memory than one large model. |
| Preallocate arrays for LabVIEW models instead of using Build Array functions. | Each Build Array function uses a shared resource. This may delay the model execution because both models cannot use the shared resource simultaneously. Preallocating arrays avoids potential delays. To preallocate an array, use a Case structure and the First Call? function. Replace the elements of the array at run time with the Replace Array Subset function. |

Parent topic:

Maximizing System Performance

<!--NI_TOPIC bundle=veristand path=including-log-files-post-processing.html language=enus -->
## TOPIC 00237: Including Log Files Produced on a Target in Post-Processing

- bundle_id: `veristand`
- source_path: `including-log-files-post-processing.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/including-log-files-post-processing.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Automatically download files produced by a target to include these files in post-processing. You must start and stop the logs on the targets from outside of the Data Logging control. Click Edit settings on the data logging control. Select Target Logs. Click Download target log files to host. Click A

### Including Log Files Produced on a Target
 in Post-Processing

Automatically download files produced by a target to include these files in
 post-processing.

Data Logging

1. Click Edit settings on the data logging control.
2. Select Target Logs.
3. Click Download target log files to host.
4. Click Add to add channels.
5. Select the targets from which you want to download files.
6. Specify the location to which to download the files in
 Destination and click OK.
7. Select Include downloaded target-log files in post
 processing.

When you stop logging, the log control downloads all files
 closed by the target during logging. If you choose to use DIAdem for post-process, the
 log files merge in DIAdem below the host-side log files.

Parent topic:

Loading a File in DIAdem

Related tasks:

- Logging and Documenting Sessions

<!--NI_TOPIC bundle=veristand path=installing-swproduct.html language=enus -->
## TOPIC 00238: Installing VeriStand

- bundle_id: `veristand`
- source_path: `installing-swproduct.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/installing-swproduct.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can install VeriStand with either NI Package Manager or the platform media. If Windows Update is enabled, the installation process might hang if Windows Update interferes with the installation of Microsoft Visual C++ 2015 Run-Time. To resolve this issue, visit the NI Support article NI Installer

### Installing VeriStand

You can install VeriStand with either NI Package Manager or the platform media.

Note

NI Installer Hangs While Installing Visual C++ 2015 Run-Time

Note

VeriStand

License Manager

#### Installing VeriStand Using Package Manager

Refer to *Package Manager* for information about installing, removing, and
 upgrading NI software using Package Manager.

#### Installing VeriStand Using the Platform Media

Note

To install VeriStand,
 modules, toolkits, and drivers, insert the VeriStand Platform media and follow the
 onscreen instructions. When prompted, log in to your NI User Account to activate
 your NI products. If you are managing your VeriStand license with a volume license
 server, you should receive your volume license file by email.

<!--NI_TOPIC bundle=veristand path=int32-array-variable.html language=enus -->
## TOPIC 00239: Int32 Array Variable

- bundle_id: `veristand`
- source_path: `int32-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/int32-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of 32-bit signed integers. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cas

### Int32 Array Variable

An array of 32-bit signed integers.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=int32-variable.html language=enus -->
## TOPIC 00240: Int32 Variable

- bundle_id: `veristand`
- source_path: `int32-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/int32-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A 32-bit signed integer. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where p

### Int32 Variable

A 32-bit signed integer.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=int64-array-variable.html language=enus -->
## TOPIC 00241: Int64 Array Variable

- bundle_id: `veristand`
- source_path: `int64-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/int64-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of 64-bit signed integers. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cas

### Int64 Array Variable

An array of 64-bit signed integers.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=int64-variable.html language=enus -->
## TOPIC 00242: Int64 Variable

- bundle_id: `veristand`
- source_path: `int64-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/int64-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A 64-bit signed integer. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where p

### Int64 Variable

A 64-bit signed integer.

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Evaluation Method | Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where parameters map to channels in a system definition, because calling by reference allows changes to the value of the channel to propagate across all sequences that use the parameter. ByReference—When another real-time sequence calls this real-time sequence as a subsequence, the calling sequence operates directly on the mapped variable value. If the subsequence updates the parameter value, the mapped variable in the calling sequence also is updated. If the calling sequence updates the mapped variable value while the subsequence executes from another task, the parameter value in the subsequence updates as well. ByReference parameters can only be called by variables of the same data type as the parameter. ByValue—When another real-time sequence calls this real-time sequence as a subsequence, the parameter maps a copy of the variable value. If the calling sequence updates the mapped variable value while the subsequence executes, the parameter value in the subsequence is not affected. If the subsequence modifies the parameter value while the subsequence executes, the value of the mapped variable in the calling sequence is not affected. ByValue parameters can be called by variables of any logical data type. Note This property only appears if you use the variable as a parameter. |
| Default Assignment | Specifies the default channel in the system definition to assign to this parameter. The real-time sequence uses the Default Assignment unless you override the parameter value when you call the real-time sequence from a stimulus profile. You can specify a channel by its alias or by the path to the channel in the system definition, for example: Targets/Controller/System Channels/Model Count This property only appears if you use the variable as a parameter. |
| Default Value | Specifies the default or initial value of the local variable. This property only appears if you use the variable as a local variable. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=integrate-execute-models.html language=enus -->
## TOPIC 00243: Integrating and Executing Models

- bundle_id: `veristand`
- source_path: `integrate-execute-models.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/integrate-execute-models.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use models to mathematically represent real-world systems in your VeriStand project. Simulate both the plant and controller to create a closed-loop control system within a software model. Use models for signal generation, signal analysis, and control. For more information on using models in VeriStan

### Integrating and Executing Models

Use models to mathematically represent real-world systems in
 your VeriStand project.

Simulate both the plant and controller to
 create a closed-loop control system within a software model. Use models for signal
 generation, signal analysis, and control. For more information on using models in
 VeriStand, refer to .

1. Prepare your model for use. 
 Use
 a model from C/C++—Create a model in C or C++ that NI software can load and execute through the
 VeriStand Model Framework.
Use
 a model from MathWorks Simulink<sup>®</sup> software—Use Simulink software to convert your model for use on real-time
 targets.Note VeriStand only supports 64-bit operating
 systems.
Use
 a model from LabVIEW VIs—Convert LabVIEW VIs into compiled .lvmodel or
 .lvmodelso files.
Use
 the Functional Mockup Interface (FMI)—Decouple modeling
 environments from model consumers.
2. Add and configure the model—Connect a model to other parts of the system and
 run the model on a hardware target.
3. Control
 and monitor model execution—Use model execution channels to interact with
 models.

Parent topic:

Configuring the System

Related concepts:

- Models FAQs
- FMI Support
- Common Issues with Models in VeriStand

Related tasks:

- Using Models from C and C++
- Using Models from Simulink
- Using Models from LabVIEW VIs
- Adding and Configuring a Model
- Controlling and Monitoring Model Execution

<!--NI_TOPIC bundle=veristand path=integrating-virtual-ecus.html language=enus -->
## TOPIC 00244: Integrating Virtual ECUs

- bundle_id: `veristand`
- source_path: `integrating-virtual-ecus.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/integrating-virtual-ecus.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the VeriStand Virtual ECU Toolkit to integrate and execute virtual electronic control units (ECUs) you created using third-party software from a supported vendor. An ECU is an embedded automotive system that controls other subsystems. When performing hardware-in-the loop (HIL) testing, you can u

### Integrating Virtual ECUs

Use the VeriStand Virtual ECU Toolkit to integrate and execute virtual electronic control
 units (ECUs) you created using third-party software from a supported
 vendor.

An *ECU* is an embedded automotive system that controls other
 subsystems. When performing hardware-in-the loop (HIL) testing, you
 can use a virtual ECU in the place of a real ECU in the following
 situations:

- Hardware is not available for testing.
- In place of rest bus models that represent ECUs in a
 network.

- [Setting Up a Real-Time Target for Virtual ECUs](setting-up-rt-target-virtual-ecus.html) Install the necessary software and configure a real-time target to use virtual ECUs.
- [Virtual ECU Vendor and Protocol Support](virtual-ecu-vendor-protocol-support.html) Virtual ECUs allow you to test devices quickly, with a more realistic rest bus simulation, and with less effort for creating the bus simulation.

Parent topic:

Configuring the System

Related tasks:

- Preparing a System Definition File for Virtual ECUs

<!--NI_TOPIC bundle=veristand path=keyboard-shortcuts.html language=enus -->
## TOPIC 00245: Keyboard Shortcuts

- bundle_id: `veristand`
- source_path: `keyboard-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/keyboard-shortcuts.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Navigate VeriStand using keyboard shortcuts. File Operations Action Shortcut Create a new screen document and add it to the existing project. <Ctrl-N> Open an existing project. <Ctrl-O> Close the current document. <Ctrl-W> Save the current file. <Ctrl-S> Save all open files. <Ctrl-Shift-S> Quit Veri

### Keyboard Shortcuts

Navigate VeriStand using keyboard shortcuts.

#### File
 Operations

| Action | Shortcut |
| --- | --- |
| Create a new screen document and add it to the existing project. | <Ctrl-N> |
| Open an existing project. | <Ctrl-O> |
| Close the current document. | <Ctrl-W> |
| Save the current file. | <Ctrl-S> |
| Save all open files. | <Ctrl-Shift-S> |
| Quit VeriStand. | <Alt-F4> |

#### Basic Editing

| Action | Shortcut |
| --- | --- |
| Cut. | <Ctrl-X> |
| <Shift-Delete> |  |
| Copy. | <Ctrl-C> |
| <Ctrl-Insert> |  |
| Paste. | <Ctrl-V> |
| <Shift-Insert> |  |
| Undo. | <Ctrl-Z> |
| <Alt-Backspace> |  |
| Redo. | <Ctrl-Y> |
| <Alt-Shift-Backspace> |  |

#### Editing Text

| Action | Shortcut |
| --- | --- |
| Select a single word in a string. | Double-click text |
| Select the entire string. | Triple-click text |
| Move the cursor within a string by one word in the direction of the arrow. | <Ctrl-Right arrow> |
| <Ctrl-Left arrow> |  |
| Move the cursor to the beginning of the current line. | <Home> |
| Move the cursor to the end of the current line. | <End> |
| Move the cursor to the beginning of the string. | <Ctrl-Home> |
| Move the cursor to the end of the string. | <Ctrl-End> |
| Cancel text entry. | <Esc> |
| Submit text entry. | <Ctrl-Enter> |
| Open shortcut menu for selected item. | <Shift-F10> |
| Add free label or comment to the project screen. | <Double-click open area> |
| Find and replace text or objects within a project. | <Ctrl-Shift-F> |
| Find and replace text or objects within a document. | <Ctrl-F> |

#### Selecting and Moving Objects

| Action | Shortcut |
| --- | --- |
| Select multiple objects. | <Shift-Click> |
| Add object to the current selection. |  |
| Select all objects. | <Ctrl-A> |
| Move selected objects in grid-sized increments. | <Arrow keys> |
| Move selected objects four grid units. | <Shift-Arrow key> |
| Copy and drag selected object. | <Ctrl-Drag> |
| Copy selected object and move it along one axis. | <Ctrl-Shift-Drag> |
| Resize selected object while maintaining aspect ratio. | <Shift-Resize> |
| Resize selected object while maintaining center point. | <Ctrl-Resize> |
| Resize selected object while maintaining both aspect ratio and center point. | <Shift-Ctrl-Resize> |
| Create additional blank space along the axis you drag the mouse. | <Ctrl-Drag open area> |

#### Navigating the Environment

| Action | Shortcut |
| --- | --- |
| Search document for next instance of text or an object. This command is only available when in Find mode. | <Enter> |
| <F3> |  |
| <Ctrl-G> |  |
| Search document for previous instance of text or an object. This command is only available when in Find mode. | <Shift-Enter> |
| <Shift-F3> |  |
| <Shift-Ctrl-G> |  |
| Cycle through document tabs in the order in which they appear onscreen. | <Ctrl-Tab> |
| Cycle through document tabs in the opposite order in which they appear onscreen. | <Ctrl-Shift-Tab> |

#### Navigating the Screen and Mapping Diagram

| Action | Shortcut |
| --- | --- |
| Highlight all mappings and nodes connected to a selected item. | <Ctrl+,> |
| Shift focus to the palette search bar. | <Ctrl-Spacebar> |
| <Ctrl-Alt-Spacebar> for Chinese keyboards |  |
| Scroll the document horizontally. | <Shift-Mouse Wheel> |
| Shift focus from one control to another in tabbing order while the code is running. | <Tab> |
| Shift focus from one control to another in reverse tabbing order while the code is running. | <Shift-Tab> |
| Pan across the project screen. | <Spacebar-Drag> |

#### Deployment Commands

| Action | Shortcut |
| --- | --- |
| Deploy the active system definition. | <F6> |
| Undeploy the active system definition. | <F7> |
| Connect to the system definition that is currently running on the VeriStand Gateway. | <F8> |
| Disconnect from the current running system definition. This leaves the VeriStand Gateway running for other clients. | <F9> |

#### Help Commands

| Action | Shortcut |
| --- | --- |
| Display the Context Help. | <Ctrl-H> |
| Access additional information on selected item. | <F1> |

#### Wiring

| Action | Shortcut |
| --- | --- |
| Delete all broken wires from the diagram. | <Ctrl-B> |
| Delete a wire you are in the process of creating. | <Esc> |
| <Ctrl-Z |  |
| Select one wire segment. | Single-click wire |
| Select a wire branch. | Double-click wire |
| Select the entire wire. | Triple-click wire |
| Create a new wire branch from an existing wire. | <Ctrl-Click> wire |
| Tack down the wire segment and start a new wire segment. | Single-click while wiring |
| End the wire without connecting it to a node. | Double-click while wiring |
| Switch the direction of a wire between horizontal and vertical. | <Tap spacebar> while wiring |
| Organize the diagram or the selected code to make it easier to understand. | <Ctrl-U> |

#### Navigating the Project Files
 Navigation Pane

| Action | Shortcut |
| --- | --- |
| Expand everything in the selected folder. | <*> on the numeric keypad |
| Expand the selected folder. | <+> on the numeric keypad |
| Collapse the selected folder. | <-> on the numeric keypad |
| Expand the selected folder if it is closed. Otherwise, this keyboard shortcut selects the first child. | <Right arrow> |
| Collapse the selected folder if it is open. Otherwise, this keyboard shortcut selects the parent. | <Left arrow> |
| Select the item beginning with the entered letter(s). | <Any printable key> |
| Open the selected document. | <Enter> |
| Rename the selected item. | <F2> |
| Move the selection to the first item in the tree. | <Home> |
| Moves the selection to the last item in the tree. | <End> |
| Move the selection to the first visible item in the tree. | <Page up> |
| Move the selection to the last visible item in the tree. | <Page down> |

#### Zooming

| Action | Shortcut |
| --- | --- |
| Zoom in and out. | <Ctrl-Mouse wheel> |
| Zoom in. | <Ctrl-+> |
| Zoom out. | <Ctrl--> |
| Zoom to fit. | <Ctrl-0> |
| Zoom to fit the selection. | <Ctrl-9> |

Parent topic:

VeriStand Environment

Related concepts:

- Host Computer

<!--NI_TOPIC bundle=veristand path=labview-examples.html language=enus -->
## TOPIC 00246: LabVIEW Examples

- bundle_id: `veristand`
- source_path: `labview-examples.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-examples.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example LabVIEW code helps you get started with NI software features and common programming workflows.

### LabVIEW Examples

Example LabVIEW code helps you get started with NI software features and common
 programming workflows.

- [Opening and Running a Project](labview-walkthrough-opening-and-running-a-pro.html) Use the NI VeriStand Execution .NET API in LabVIEW to connect to the VeriStand Gateway, deploy a system definition, and read channel values.
- [Programming with the System Definition API in LabVIEW](programming-with-the-system-definition-api-in.html) Use LabVIEW with the NI VeriStand System Definition .NET API to programmatically create, open, and change system definition files.

Parent topic:

VeriStand Examples

<!--NI_TOPIC bundle=veristand path=labview-vi-model-hardware-target.html language=enus -->
## TOPIC 00247: LabVIEW VI Model Hardware Target Support

- bundle_id: `veristand`
- source_path: `labview-vi-model-hardware-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-vi-model-hardware-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Verify your hardware target will support a LabVIEW VI compiled into a VeriStand model. Use the following table to determine if your hardware target supports a VeriStand model file type.For a list of real-time targets and the real-time operating systems (RTOS) that each runs, see Real-Time Controller

### LabVIEW VI Model Hardware Target
 Support

Verify your hardware target will support a LabVIEW VI compiled into a VeriStand
 model.

Note

Real-Time Controllers and Real-Time Operating
 System Compatibility

| Computer type | RTOS | Supported VeriStand model file type |
| --- | --- | --- |
| Windows | — | .lvmodel |
| Real-Time Target | NI Linux Real-Time | .lvmodelso |

On applicable real-time targets, .lvmodelso and
 .lvmodel files are supported if the source LabVIEW
 VI does not contain code with Windows function calls that are not supported
 by the RTOS.

Parent topic:

Using Models from LabVIEW VIs

Related information:

- Real-Time Controllers and Real-Time Operating System
 Compatibility

<!--NI_TOPIC bundle=veristand path=labview-vi-model-preparation.html language=enus -->
## TOPIC 00248: LabVIEW VI Model Conversion Preparation

- bundle_id: `veristand`
- source_path: `labview-vi-model-preparation.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-vi-model-preparation.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must assign front panel controls and indicators in LabVIEW VIs to the connector pane so VeriStand can identify them as inports, outports, and parameters when you add the compiled .lvmodel or .lvmodelso to a system definition. Use the following table to build the LabVIEW VI connector pane accordi

### LabVIEW VI Model Conversion
 Preparation

You must assign front panel controls and indicators in LabVIEW VIs to the connector pane
 so VeriStand can identify them as inports, outports, and parameters when you add the
 compiled .lvmodel or .lvmodelso to a system
 definition.

Use the following table to build the LabVIEW VI connector pane according to how you want each
 control or indicator to work in VeriStand.

| Desired VeriStand component | VI connector pane assignment | Is LabVIEW default value imported to VeriStand? |
| --- | --- | --- |
| Inport | Required input | No |
| Outport | Any output | No |
| Parameter | Optional or recommended input | Yes |

#### Supported LabVIEW Data Types

- Numerics
- Booleans
- 1D arrays of numerics
- 1D arrays of Booleans
- Clusters containing the previous data types

If you use an unsupported data type, LabVIEW returns an error when you
 try to convert the VI to a compiled model. Controls and indicators not assigned to
 the connector pane can have other data types.

#### Global and Local Parameters

A compiled
 model you add to a system definition can contain global parameters and block
 parameters.

If you want a LabVIEW VI front panel control to become a local
 parameter in VeriStand, place that control in a cluster shell before you compile. To
 make a LabVIEW VI front panel control a global parameter in VeriStand, do not place
 the control in a cluster.

#### Considerations for LabVIEW VIs with Array
 Terminals

If a LabVIEW VI contains an array control or indicator you want
 to include in the model, enter a value in the n<sup>th</sup> element of the array,
 where n is the desired number of elements. Right-click the
 array control and select Data Operations»Make Current Value Default. Otherwise, the array appears in VeriStand with a single
 element.

Parent topic:

Using Models from LabVIEW VIs

<!--NI_TOPIC bundle=veristand path=labview-walkthrough-modifying-a-daq-device-in.html language=enus -->
## TOPIC 00249: Modifying a DAQ Device in a System Definition File

- bundle_id: `veristand`
- source_path: `labview-walkthrough-modifying-a-daq-device-in.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-walkthrough-modifying-a-daq-device-in.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand System Definition .NET API in LabVIEW to programmatically configure DAQ devices in a system definition file. Creating and communicating with .NET objects in LabVIEW requires the .NET CLR 4.0 that installs with LabVIEW. You must use a .NET 2.0 configuration file if you want to

### Modifying a DAQ Device in a System Definition
 File

Use the NI VeriStand System Definition .NET API in LabVIEW to programmatically
 configure DAQ devices in a system definition file.

Note

The following sections provide an example of using the System Definition API to programmatically
 configure a DAQ device in a system definition.

As you follow the example, notice that the hierarchy of classes reflect the hierarchy of nodes that appear in the System Explorer window, shown as follows.

Figure 17.

[IMAGE alt='System Explorer tree showing a PXIe-6363 DAQ with analog, counter, and digital I/O channels.' src='GUID-1B22E3CF-2198-4012-A757-C2B727E80B56-a5.gif']

1. Part 1: Opening the System Definition File and Finding the First DAQ Device Opens an existing system definition file and locates the first DAQ device under the Chassis section.
2. Part 2: Adding Analog Input and Output Channels to a DAQ Device Modify a DAQ device in a VeriStand system definition by adding analog input and analog output channels. Create aliases for new channels and add channel mappings between analog inputs and outputs.
3. Part 3: Adding Digital Input and Output Channels to a DAQ Device Add digital input and digital output channels to a DAQ device in a VeriStand system definition, including alias links and channel mappings.
4. Part 4: Removing Broken Aliases and Channel Mappings Removes broken aliases and blank channel mappings in a VeriStand system definition file after DAQ channel changes.

Parent topic:

Programming with the System Definition API in LabVIEW

<!--NI_TOPIC bundle=veristand path=labview-walkthrough-modifying-a-system-defini.html language=enus -->
## TOPIC 00250: Modifying a System Definition File

- bundle_id: `veristand`
- source_path: `labview-walkthrough-modifying-a-system-defini.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-walkthrough-modifying-a-system-defini.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Programmatic modification of an NI VeriStand system definition file in LabVIEW using the System Definition .NET API. Includes opening a .nivssdf file, navigating the System Explorer hierarchy, and updating CAN ports.You can use LabVIEW to access the NI VeriStand System Definition .NET API and progra

### Modifying a System Definition File

Programmatic modification of an NI VeriStand system definition file in LabVIEW using
 the System Definition .NET API. Includes opening a .nivssdf file, navigating the System
 Explorer hierarchy, and updating CAN ports.

System Explorer

Note

- Remove a CAN port from a system definition file
- Add a new CAN port with an associated XNET database, CAN cluster, and incoming
 frame

System Explorer

Figure 8.

[IMAGE alt='System Explorer tree showing NI-XNET CAN1 with an incoming single-point frame.' src='GUID-946D779A-0B2B-41F0-869A-729C7CF6F13B-a5.gif']

Figure 9.

[IMAGE alt='LabVIEW block diagram that opens a system definition file and calls Root.GetTargets.' src='GUID-2E824BD9-81E5-48D4-B621-127D872E40CC-a5.gif']

Figure 10.

[IMAGE alt='LabVIEW block diagram that removes a CAN port node, adds a new CAN port, and saves the system definition.' src='GUID-25B2D55A-42C6-4EE4-BAFA-6E7E9736298C-a5.gif']

1. Open an existing .nivssdf file from disk by initializing a new
 instance of the SystemDefinition class. Note that the SystemDefinition
 constructor, used to open the existing system definition file is
 overloaded.
2. Find the first target in the system definition file by: 
 Tip Instead of
 using multiple cascading Property and Invoke Nodes, you can *use
 dottable properties*, a shorthand method for accessing some
 references. Table 2.Opening vs
 Creating a System Definition FileSystemDefinition(String)
 SystemDefinition(String, String, String, String,
 String, String, String)Opens an existing system definition file.
 Creates a new system definition file with specified
 configuration options.
 [IMAGE alt='image' src='GUID-B2D5B083-85E5-4C6A-84CC-AB548860880E-a5.gif']
 [IMAGE alt='image' src='GUID-358B0880-EF37-423E-BB57-D936AC3D6614-a5.gif']
  1. Obtaining the references to the following items in the system definition
 file, in descending order:
    1. The root-level item (via Root property)
    2. The Targets section (via GetTargets
 method)
    3. All targets under the Targets section
 (returned by GetTargetList method as an array of
 references)
  2. Indexing the first element from the array of target references.
3. Continue using Invoke Nodes to traverse the hierarchy of nodes under the
 Targets section until reaching the
 CAN section under the first chassis. Obtain an
 array of references to all CAN ports in that section. 
 Tip 
 Instead of traversing the hierarchy of System Definition API classes, you
 can *find and return a reference for a specific node*.
4. Remove the first CAN port from the CAN section.
5. Associate an existing XNET database with a new CAN port by initializing new
 instances of the Database and CANPort classes. Notice how the CANPort
 constructor contains a LinkedDatabase parameter that
 requires you to specify the XNET database associated with the port.
6. Traverse the hierarchy of sections that will appear under the new CAN port
 to get the Single-Point section. Add a new
 signal-based frame associated with the XNET database from step 5, to the
 Single-Point section.
7. Add the new CAN port to the CAN section of the system
 definition file.
8. Save the system definition file to disk.

Parent topic:

Programming with the System Definition API in LabVIEW

Related concepts:

- Programming with the System Definition API in LabVIEW
