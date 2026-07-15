# NI DOCUMENT BUNDLE: veristand

<!--NI_BUNDLE_CHUNK bundle=veristand start=251 end=426 -->
<!--NI_TOPIC bundle=veristand path=labview-walkthrough-modifying-models-in-a-sys.html language=enus -->
## TOPIC 00251: Modifying Models in a System Definition File

- bundle_id: `veristand`
- source_path: `labview-walkthrough-modifying-models-in-a-sys.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-walkthrough-modifying-models-in-a-sys.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use LabVIEW with the NI VeriStand System Definition .NET API to programmatically add, configure, and remove models in a system definition file. Creating and communicating with .NET objects in LabVIEW requires the .NET CLR 4.0 that installs with LabVIEW. You must use a .NET 2.0 configuration file i

### Modifying Models in a System Definition
 File

Use LabVIEW with the NI VeriStand System Definition .NET API to programmatically add,
 configure, and remove models in a system definition file.

Note

The following sections give an example of using the System Definition API to add a model,
 configure the inports and outports of the model, and remove a model. As you follow the
 example, notice that the hierarchy of classes reflect the hierarchy of nodes that appear
 in the System Explorer window, as shown in the following image.

Figure 11.

[IMAGE alt='System Explorer tree showing a model and its Inports, Outports, Parameters, and Signals.' src='GUID-17392366-11B6-47A1-A571-04167E66C9F0-a5.gif']

#### Part 1: Opening the System Definition File and Finding the Models
 Section

The first part of this example code programmatically opens an
 existing system definition file and navigates the nodes in the system definition to
 obtain the reference to the Models section.

Figure 12.

[IMAGE alt='LabVIEW block diagram showing nodes to open a system definition file and get the Models section.' src='GUID-2108B6B9-930E-4E57-BB4B-F74C6C38D204-a5.gif']

1. Open an existing system definition .nivssdf file from disk by initializing a new instance of the SystemDefinition class.
2. Find the Models section of the system definition file. To do so, obtain references to the following items, in descending order:
  1. The Targets section (obtained from the Root dottable property and GetTargets method)
  2. All targets under the Targets section (obtained from the GetTargetList method as an array of references)
  3. The first target in the system definition (obtained from the first reference in the array)
  4. The Simulation Models section (obtained from the GetSimulationModels method)
  5. The Models section (obtained from the GetModels method)

#### Part 2: Adding Models to the System Definition File

After obtaining the
 reference to the Models section, the example code adds three
 example models to the system definition file: sinewave, random, and delay.

Figure 13.

[IMAGE alt='LabVIEW block diagram showing a For Loop that adds models from an array to the Models section.' src='GUID-072142DB-2588-4428-B2BE-FEAA99E03EFE-a5.gif']

1. Create an array of clusters. In each cluster, define the parameters the Model
 constructor needs in following step. The array in the example code contains
 parameters for the sinewave, random, and delay example models.
2. Initialize a new instance of the Model class with the parameters you defined in
 the previous step.
3. Add the new model to the Models section of the system
 definition. The code repeats steps two and three for each set of parameters in
 the array.

#### Part 3: Creating Aliases for Model
 Outports

After adding the sinewave, random, and delay models to the system definition, the
 example code creates an alias for the first outport of each model.

Figure 14.

[IMAGE alt='LabVIEW diagram that creates an alias for the first outport (Outport0) of each model.' src='GUID-577D6974-304A-4924-9471-CB0D235F5DDF-a5.gif']

1. Obtain the reference to the Aliases section of the system
 definition file using the Root dottable property and GetAliases method.
2. Find the outports of each model by obtaining references to the following items,
 in descending order:
  1. The models added in the previous section (obtained from the GetModels
 method)
  2. The Outports section (obtained from the
 GetOutportsSection method)
  3. The outports under the Outports section (obtained
 from the GetOutports method)
3. Get the name of the model using a Property Node and append
 _Output0 to it. This string serves as the
 Name parameter of the alias.
4. Add a new alias using the AddNewAliasByReference method. The first outport,
 Out1 , serves as the
 LinkedChannelReference parameter.

#### Part 4: Removing a Model from the System Definition

Figure 15.

[IMAGE alt='LabVIEW block diagram showing a loop that gets model nodes and removes the matching model.' src='GUID-816E5A1C-F94C-48DB-A7A9-CC9F9E9A5480-a5.gif']

1. Obtain references to models in the Models section using
 the GetChildren method.
2. Find the reference to the delay model. To do so, get the
 Name property for each model. Compare the name of
 each model to the name of the desired model, delay , with
 the Equal? function.
3. Once found, remove delay from the system definition using
 the RemoveNode method.

#### Part 5: Removing Broken Aliases after Removing a Model

Figure 16.

[IMAGE alt='LabVIEW diagram loops through aliases and removes an alias with an empty string or path.' src='GUID-29234439-1A03-4688-9983-4097F37E90A7-a5.gif']

1. Find the aliases under the Aliases section by obtaining
 the following references, in descending order:
  1. The Aliases section of the system definition file
 (obtained from the Root dottable property and GetAliases method)
  2. The aliases under the Aliases section (obtained
 from the GetAliasesList method)
2. Find any aliases without a channel by:
  1. Getting the LinkedChannel parameter of each
 model.
  2. Getting the Name parameter of the linked
 channel.
  3. Evaluating whether a name exists for each linked channel with the Empty
 String/Path? function. If the Name parameter is
 empty, the alias is not linked to a channel.
3. Remove any aliases without a channel using the RemoveNode method.
4. Save the system definition file.

Parent topic:

Programming with the System Definition API in LabVIEW

Related concepts:

- Programming with the System Definition API in LabVIEW

<!--NI_TOPIC bundle=veristand path=labview-walkthrough-opening-and-running-a-pro.html language=enus -->
## TOPIC 00252: Opening and Running a Project

- bundle_id: `veristand`
- source_path: `labview-walkthrough-opening-and-running-a-pro.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/labview-walkthrough-opening-and-running-a-pro.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VeriStand Execution .NET API in LabVIEW to connect to the VeriStand Gateway, deploy a system definition, and read channel values.You can use LabVIEW to access the NI VeriStand Execution .NET API and automate the operation of an NI VeriStand application. Creating and communicating with .

### Opening and Running a Project

Use the NI VeriStand Execution .NET API in LabVIEW to connect to the VeriStand
 Gateway, deploy a system definition, and read channel values.

Note

- Deploy a system definition file to a target running the VeriStand Gateway
- Read values from channels
- Undeploy the system definition file

<Common Data>\Projects\Example

Figure 1.

[IMAGE alt='LabVIEW block diagram that deploys a system definition, reads channel values in a loop, then undeploys.' src='GUID-C661681C-DA4B-4A42-8CD6-71278871465E-a5.gif']

1. Initializes a new instance of the Factory class, which provides access to the NI
 VeriStand system and the various interfaces available in the Execution API. Any code
 you write using this API must include a Factory constructor to access NI
 VeriStand.
2. Gets the IWorkspace2 interface, which you can use to manage connections between the
 VeriStand Gateway and one or more targets, to start and stop basic Workspace
 operations, and to configure events for error and status notifications. Tip The GetIWorkspace2
 method is overloaded. The GetIWorkspace2() overload in the previous block
 diagram assumes the VeriStand Gateway is running on the localhost. A separate
 GetIWorkspace2(string) overload allows you to specify the IP address of the
 VeriStand Gateway.
3. Connects the VeriStand Gateway to one or more targets and deploys the system
 definition file. Note that if you set the
 deploy_system_definition parameter to false, the
 target(s) must already be running the system definition file before you call this
 method.
4. For fifty For Loop iterations, gets the values of the specified channels as the
 system definition file runs on the target. The remainder of the code in the For Loop
 creates and displays the channel values on the front panel in the format of
 Iteration 0: 0.925761, 4.791827, 1.957790. Tip Other members of the
 IWorkspace2 interface allow you to get the values of a single scalar channel or
 a vector channel, or to set the values of different types of channels.
5. Disconnects the VeriStand Gateway from all connected targets and undeploys the
 system definition file.

The following figure shows the Aliases section of the system definition file from this example, as displayed in the System Explorer configuration tree. Notice that alias paths in the previous block diagram reflect their names and location in the system definition file.

Figure 2.

[IMAGE alt='System Explorer tree showing Aliases under Sinewave Delay.' src='GUID-2355F1F6-2142-4CC3-BF53-870E895DB318-a5.gif']

Parent topic:

LabVIEW Examples

Related concepts:

- Programming with the System Definition API in LabVIEW

<!--NI_TOPIC bundle=veristand path=launch-veristand.html language=enus -->
## TOPIC 00253: Launch NI VeriStand Step

- bundle_id: `veristand`
- source_path: `launch-veristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/launch-veristand.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launches the VeriStand executable. The Stimulus Profile Editor runs as a separate executable from the main VeriStand application. Ensure VeriStand is running to execute tests. However, you can edit stimulus profiles and real-time sequences without running VeriStand. Property/Section Description Time

### Launch NI VeriStand Step

Launches the VeriStand executable.

The Stimulus Profile Editor runs as a separate executable from the main VeriStand application.
 Ensure VeriStand is running to execute tests. However, you can edit stimulus
 profiles and real-time sequences without running VeriStand.

| Property/Section | Description |
| --- | --- |
| Timeout | Specifies the time in seconds to wait for VeriStand to launch before returning a timeout error. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

VeriStand Control Steps

<!--NI_TOPIC bundle=veristand path=licensing-options.html language=enus -->
## TOPIC 00254: VeriStand Licensing Options

- bundle_id: `veristand`
- source_path: `licensing-options.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/licensing-options.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI offers a variety of licenses for the different ways you can use VeriStand in development and deployment applications. Licensing Options Use the following descriptions to determine the VeriStand licensing option that fits your needs. For more information on activating VeriStand licenses, refer to

### VeriStand Licensing Options

NI offers a variety of licenses for the different ways you can use VeriStand in
 development and deployment applications.

#### Licensing Options

Use the following descriptions to determine the VeriStand licensing option that fits
 your needs.

Note

ni.com/activate

ni.com/veristand

| License | Description |
| --- | --- |
| Evaluation Mode | Software runs as a Full Development system for 7 days. The evaluation period can be extended to 45 days. You can activate a VeriStand license at any point during or after the evaluation period. |
| Full Development | Enables full VeriStand functionality. |
| PC Development | Enables you to run simulations on a desktop PC. |
| Operator | Enables you to configure a project file by determining the preconfigured system definition file that runs on the target and defining the test environment that an operator interacts with. |

#### Comparing License Option
 Features

Note

| Feature | Full Development | PC Development | Operator |
| --- | --- | --- | --- |
| View system definition files as read-only | No | No | Yes |
| Create new system definition files | Yes | Yes | No |
| Configure supported NI hardware devices | Yes | Yes | No |
| Configure custom devices | Yes | Yes | No |
| Configure models | Yes | Yes | No |
| Add targets | Yes | Yes | No |
| Add user channels | Yes | Yes | No |
| Add calculated channels | Yes | Yes | No |
| Map channels | Yes | Yes | No |
| Add alarms | Yes | Yes | No |
| Add procedures | Yes | Yes | No |
| Deploy system definition file to a real-time target | Yes | No | Yes |
| Add standard and custom Tools menu utilities | Yes | Yes | Yes |
| Configure alarm responses | Yes | Yes | Yes |
| Add custom files to a project | Yes | Yes | Yes |
| Export channel resources | Yes | Yes | Yes |
| Create stimulus profiles | Yes | Yes | Yes |
| Run stimulus profiles | Yes | Yes | Yes |
| Log data | Yes | Yes | Yes |
| Run compiled models | Yes | Yes | Yes |

Note

®

#### Licensing
 Options for the VeriStand Virtual ECU Toolkit

In addition to a VeriStand
 license, you will need separate licensing to operate the VeriStand Virtual ECU
 Toolkit. The type of VeriStand license you have will determine what features you
 have access to in regard to using virtual electronic control units (ECUs).

| License Combination | Description |
| --- | --- |
| VeriStand Virtual ECU Toolkit VeriStand Operator | Deploy virtual ECUs. |
| VeriStand Virtual ECU Toolkit VeriStand Full Development | Create and deploy virtual ECUs. |

You will also need a license for the platform you used to create the virtual
 ECU, such as Synopsys<sup>®</sup> Silver. For more information, refer to
 *Integrating Virtual ECUs*.

Related tasks:

- Integrating Virtual ECUs

Related information:

- Installing, Updating, Repairing, and Removing NI
 Software
- Download VeriStand
- License Setup and Activation

<!--NI_TOPIC bundle=veristand path=loading-file-diadem.html language=enus -->
## TOPIC 00255: Loading a File in DIAdem

- bundle_id: `veristand`
- source_path: `loading-file-diadem.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/loading-file-diadem.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Load each data file generated during a log session in DIAdem to complete a variety of tasks such as generating graphs and tables. This feature requires NI DIAdem. For more information about NI DIAdem, visit ni.com/diadem. Click Edit settings on the data logging control. Select Post-Processing. From

### Loading a File in DIAdem

Load each data file generated during a log session in DIAdem to complete a variety of
 tasks such as generating graphs and tables.

ni.com/diadem

1. Click Edit settings on the data logging control.
2. Select Post-Processing.
3. From the Action to take at end of log session drop-down, select Load
 File in DIAdem.
4. Configure the options on this page to meet your needs.

Parent topic:

Configuring and Executing Host-Side Logging

Related tasks:

- Automating Post-Processing in DIAdem with a VBScript
- Generating a PDF or HTML Report with DIAdem
- Including Log Files Produced on a Target in Post-Processing

<!--NI_TOPIC bundle=veristand path=lock-model-parameters-run-time.html language=enus -->
## TOPIC 00256: Locking Model Parameters at Run Time

- bundle_id: `veristand`
- source_path: `lock-model-parameters-run-time.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/lock-model-parameters-run-time.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Lock model parameters at run time in the VeriStand Workspace to prevent expression-based updates after initial evaluation. Before you begin, you must deploy and connect to a system definition with models before you can lock model parameters. Locking a parameter is useful if you want an expression to

### Locking Model Parameters at Run Time

Lock model parameters at run time in the VeriStand Workspace to prevent
 expression-based updates after initial evaluation.

Before you begin, you must deploy and
 connect to a system definition with models before you can lock model parameters.

b = a *
 2

a

b

b

a

Note

VeriStand Editor

Workspace

Model Parameter
 Manager

VeriStand always unlocks parameters when you deploy a system
 definition. You cannot lock parameters when VeriStand initializes parameter values
 prior to running the model.

1. Open the Workspace.
2. Right-click a parameter.
3. On the Item Properties dialog box, enable
 Lock.
4. Click OK.

[IMAGE alt='image' src='GUID-22FEE575-08BA-44EB-8094-528949512B31-a5.gif']

Parent topic:

Setting Model Parameters

<!--NI_TOPIC bundle=veristand path=log-incoming-xnet-frames.html language=enus -->
## TOPIC 00257: Logging Incoming NI-XNET Frames

- bundle_id: `veristand`
- source_path: `log-incoming-xnet-frames.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/log-incoming-xnet-frames.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure NI VeriStand to log incoming NI-XNET raw frame data to TDMS or NCL log files. Specify buffering, filtering by frame ID, and trigger conditions for starting or stopping logging. When you deploy and run the project, VeriStand logs the frame data you specify to the log file when the trigger c

### Logging Incoming NI-XNET Frames

Configure NI VeriStand to log incoming NI-XNET raw frame data to TDMS or NCL log files.
 Specify buffering, filtering by frame ID, and trigger conditions for starting or stopping
 logging.

Note

NI-XNET Logfile
 Specification

NI-XNET\Documentation

.ncl

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET in the configuration tree.
4. Select an NI-XNET LIN, FlexRay, or CAN port.
5. Click Incoming»Raw Frame Data Logging.
6. Click New Raw Frame Data Logging
[IMAGE alt='image' src='GUID-72F956B1-80DE-4B36-82E4-04AF04BBB2D3-a5.gif'].
7. In the Add NI-XNET Logging File dialog box, configure the data
 logging file.
  1. Enter a XNET data logging file name.
  2. Select a file type from the drop-down.
  3. For TDMS files, enter a group name and channel name for storing the logged data.
  4. Select a destination for the log file. 
 Note You can choose a destination on
 either the host computer or real-time target.
8. Click OK. 
 The new file appears under Raw Frame Data Logging in the configuration tree.
9. On the XNET Data Logging Configuration page, enter a Buffer time
 [s] that is large enough to avoid a buffer overflow while reading data. 
 Note The larger the buffer, the more
 memory is required for data logging. To avoid additional dynamic memory allocation,
 determine the bus load for your session before starting a data logging operation.
10. Optional: 
 Select a filter from the drop-down to configure filtering of the frames to log. 
 Filtering uses frame IDs to include or exclude specific frames from the log
 file.
11. Click Trigger and File.
12. Configure when data logging starts, stops, and the operation that performs when logging
 restarts after a stop. 
 For example, on a trigger channel, you can specify to start logging when value becomes
 zero and to stop logging when it is not zero.
13. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

Related concepts:

- Raw Frame Data Logging FAQs

Related tasks:

- Replaying Logged NI-XNET CAN Frame Data
- Monitoring Incoming NI-XNET Frame Logging

<!--NI_TOPIC bundle=veristand path=log-real-time-test-data.html language=enus -->
## TOPIC 00258: Logging Real-Time Test Data with the Stimulus Profile Editor

- bundle_id: `veristand`
- source_path: `log-real-time-test-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/log-real-time-test-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use stimulus profiles to log real-time test data to the host computer while a test executes on a target. Before you begin, you should familiarize yourself with the Stimulus Profile Editor environment. Logging test data enables you to easily review and save the responses of a unit under test (UUT) to

### Logging Real-Time Test Data with the Stimulus
 Profile Editor

Use stimulus profiles to log real-time test data to the host computer
 while a test executes on a target.

Before you begin, you should familiarize yourself with the
 Stimulus Profile Editor environment.

Stimulus Profile Editor

1. Create a stimulus profile that
 calls a real-time sequence.
2. Add a Start Logging step to the
 stimulus profile, before the Real-Time Sequence
 Call step. 
 Note The step appears as Start Logging
 Configuration with a Channel Group substep.
3. Click Start Logging Configuration in the
 stimulus profile code and use the Property
 Browser to configure the following
 properties. 
 Property
DescriptionConfiguration Name
The name you want to use to
 start and stop logging.
File Path
The name and location for a
 resulting log file.
Timestamp Filename
Whether to append the start
 time of the logging operation to the name of the
 log file.
Replace Existing File
Whether to replace an
 existing file with the same filename. If you
 disable this property, the Stimulus
 Profile Editor appends any new log data
 to the existing file. This property performs a
 basic append, so you will need to use the channel
 data in the final file to determine where new data
 is appended. Note Consider adding a time channel
 to your log to easily identify breaks in data
 logging.
Log Rate [Hz]
The Stimulus Profile Editor
 logs data at the closest possible rate to this
 value without exceeding the rate at which the
 target produces data.
Triggered Logging
Configure trigger conditions
 to specify when data logging starts and stop. If
 you do not configure triggers, the
 Stimulus Profile Editor
 continuously logs all specified channel data
 beginning when the Start Logging step executes.
4. Click the Channel Group step and
 configure the following properties. 
 Property
DescriptionChannel Group Name
The name of the channel
 group used in the TDMS file.
Channels
Adds channels or aliases to
 the channel group.
5. If you want to log data in multiple channel groups, add
 additional Channel Group steps under Start
 Logging Configuration.
6. Add a Stop Logging step after the
 Real-Time Sequence Call step,
 and set the Configuration Name to the
 name you specified in the Start
 Logging step.
7. Save and run the stimulus profile.

Stimulus Profile Editor

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related tasks:

- Creating Stimulus Profiles
- Calling a Real-Time Sequence from a Stimulus Profile

Related reference:

- Start Logging Step
- Channel Group Step
- Stop Logging Step

<!--NI_TOPIC bundle=veristand path=log-sessions.html language=enus -->
## TOPIC 00259: Logging and Documenting Sessions

- bundle_id: `veristand`
- source_path: `log-sessions.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/log-sessions.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Control when a session log executes and document your observations about the session. You can also launch the File History dialog box from the control to view past log sessions and the files associated with them. Add and configure the Logging Control on the Workspace. Complete any of the following g

### Logging and Documenting Sessions

Control when a session log executes and document your observations about the
 session.

Note

File History

1. Add and
 configure the Logging Control on the
 Workspace.
2. Complete any of the following goals. 
 Goal
Description
How to OperateStart a log session
The log session starts when you click
 Start Logging or based on a start
 trigger.
Click Start
 Logging on the Data
 Logging control.
Stop a log session
The log session stops when you click
 Stop Logging, after a specified
 amount of time has elapsed, or based on a stop
 trigger.
Click Stop Logging
 on the Data Logging control.
Capture notes about a log session
Add notes to a log session to document observations, such
 as errors or peculiar behaviors, at the time they occur.
The note saves the information you enter and a timestamp
 of when you click Enter Note.
Click Enter Note
 on the Data Logging control while
 logging.
View the results of a log session
View information about past log sessions and any files
 generated during those log sessions with the
 File History dialog box.Note If
 you do not have a specified application for viewing
 TDMS files, you can view the file in the
 TDMS Filer Viewer workspace
 tool. To do so, right-click the file and select
 View File in TDMS File
 Viewer.
Each log session has a unique SessionGUID that appears as
 a root file property in the TDMS log files and user
 notes files generated during the log session. You can
 use the SessionGUID to link all files generated during
 the same log session when analyzing data.
Click History on
 the Data Logging control while
 logging.

Parent topic:

Configuring and Executing Host-Side Logging

Related tasks:

- Configuring and Executing Host-Side Logging

<!--NI_TOPIC bundle=veristand path=log-target-data-embedded-data-logger.html language=enus -->
## TOPIC 00260: Logging Target Data with the Embedded Data Logger

- bundle_id: `veristand`
- source_path: `log-target-data-embedded-data-logger.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/log-target-data-embedded-data-logger.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the VeriStand Embedded Data Logger custom device to log data on a target instead of the host. Before you begin, download the Embedded Data Logger from the VeriStand Embedded Data Logger Custom Device repository on GitHub. Use the Embedded Data Logger to log more data than the connection bandwidt

### Logging Target Data with the Embedded Data
 Logger

Use the VeriStand Embedded Data Logger custom device to log data on a target instead of
 the host.

VeriStand Embedded Data Logger Custom Device

Use the Embedded Data Logger to log more data than the connection bandwidth between
 the target(s) and the host allows. For example, to log data on several real-time
 targets, use the Embedded Data Logger instead of streaming the data from each target
 back to the host.

The Embedded Data Logger also allows you to log data after you disconnect the host
 machine. This is useful if you want to deploy your system definition to a real-time
 target, disconnect your host computer, and let the target run over several days.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller in the configuration tree.
4. Right-click Custom Devices and click National Instruments»Embedded Data Logger.
5. Add a log file.
  1. Right click Embedded Data Logger and select
 Add Log File.
  2. Edit the settings of the log file on its configuration page.
6. Specify the channels you want to log in each log file by group.
  1. Click Channel Groups.
  2. Click Add Channel Group.
  3. Click Add Channels.
  4. In the Select Channels window, specify the
 channels you want to log in the channel group.
  5. Click OK.
7. Save the system definition file.

Parent topic:

Adding Custom Software

Related concepts:

- Components of a VeriStand Project

Related information:

- VeriStand Embedded Data Logger Custom Device

<!--NI_TOPIC bundle=veristand path=log-tests-stimulus-profile.html language=enus -->
## TOPIC 00261: Logging Test Results with Stimulus Profiles

- bundle_id: `veristand`
- source_path: `log-tests-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/log-tests-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Stimulus Profile Editor to create and run stimulus profiles that log test results from real-time sequences on a target. If the Stimulus Profile Editor is not in the Tools menu, add it. You can start multiple concurrent stimulus profile executions. Each stimulus profile execution performs seq

### Logging Test Results with Stimulus
 Profiles

Use the Stimulus Profile Editor to create and run stimulus profiles that log test
 results from real-time sequences on a target.

Stimulus Profile Editor

Tools

You can start multiple concurrent stimulus
 profile executions. Each stimulus profile execution performs sequential execution of one or
 more real-time sequences.

1. In the Workspace, select Tools»Stimulus Profile Editor. 
 Note The
 name of this menu item might differ depending on how
 you named it in the Tools
 Properties dialog box. The
 Stimulus Project Editor
 launches as a separate application and may take a
 few minutes to open.
2. On the Start Page tab, select
 New Stimulus Profile.
3. Configure your stimulus profile.
  1. From the Steps palette,
 drag steps to the relevant step group
 folders.
  2. From the Sequences
 palette, drag real-time sequences to the relevant
 group folders.
4. On the Start Page tab, select
 New Real-Time Sequence.
5. Configure your real-time sequence file.
  1. From the Primitives
 palette, drag statements to the real-time
 sequence.
  2. From the Sequences
 palette, drag sequences to the real-time
 sequence.
6. Save the real-time sequence.
7. In the Stimulus Profile File window, add a
 step to call the real-time sequence you just created from
 the stimulus profile.
8. Save the stimulus profile.
9. Click Run.

Profile

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Adding a Standard or Custom Tools Menu Item

<!--NI_TOPIC bundle=veristand path=logging-steps.html language=enus -->
## TOPIC 00262: Logging Steps

- bundle_id: `veristand`
- source_path: `logging-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/logging-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Log data from channels in a system definition. Palette Object Description Channel Group Groups channels in a logging configuration. Start Logging Starts logging data from the system definition channels you specify to a TDMS file. Stop Logging Stops a currently running logging configuration.

### Logging Steps

Log data from channels in a system definition.

| Palette Object | Description |
| --- | --- |
| Channel Group | Groups channels in a logging configuration. |
| Start Logging | Starts logging data from the system definition channels you specify to a TDMS file. |
| Stop Logging | Stops a currently running logging configuration. |

Parent topic:

Stimulus Profile Steps

Related reference:

- Channel Group Step
- Start Logging Step
- Stop Logging Step

<!--NI_TOPIC bundle=veristand path=loops.html language=enus -->
## TOPIC 00263: Loops

- bundle_id: `veristand`
- source_path: `loops.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/loops.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Loops to add structures that repeat a section of real-time sequence code a specified number of times or while a specified condition is TRUE. Palette object Description DoWhile Loop A collection of statements that execute once and then continue executing for as long as the Repeat While expression

### Loops

Use Loops to add structures that repeat a section of real-time sequence code a
 specified number of times or while a specified condition is TRUE.

| Palette object | Description |
| --- | --- |
| DoWhile Loop | A collection of statements that execute once and then continue executing for as long as the Repeat While expression evaluates to TRUE. |
| For Loop | A collection of statements that execute continuously for a specified number of loop iterations. |
| ForEach Loop | A collection of statements that executes one time for each element in the array specified by the Array Expression. |
| While Loop | A collection of statements that execute continuously for as long as the Repeat While expression evaluates to TRUE. |

Parent topic:

Structures Primitives

Related reference:

- DoWhile Loop
- For Loop
- ForEach Loop
- While Loop

<!--NI_TOPIC bundle=veristand path=low-latency-mode-pcl-model-timing.html language=enus -->
## TOPIC 00264: Low Latency Primary Control Loop Timing in Models

- bundle_id: `veristand`
- source_path: `low-latency-mode-pcl-model-timing.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/low-latency-mode-pcl-model-timing.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Models in VeriStand that have a Primary Control Loop (PCL) set to low latency mode wait for the model to finish executing so other loops can access the data generated before executing again. As seen in the following illustration, the PCL will let models transfer data before executing the next step.

### Low Latency Primary Control Loop Timing in
 Models

Models in VeriStand that have a Primary Control Loop (PCL) set to low latency mode wait
 for the model to finish executing so other loops can access the data generated before
 executing again.

As seen in the following illustration, the PCL will let models transfer data before
 executing the next step.

[IMAGE alt='image' src='GUID-17729692-14EE-4CA1-BC7F-9CE8B8EB41B1-a5.gif']

#### Decimated Models

N

th

N

N

N

Note

#### Model Execution Deadlines

Note

Parent topic:

Primary Control Loop Step Execution in Models

Related concepts:

- Time Step Duration

<!--NI_TOPIC bundle=veristand path=macro-player.html language=enus -->
## TOPIC 00265: Macro Player Step

- bundle_id: `veristand`
- source_path: `macro-player.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/macro-player.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replays a previously recorded macro (.nivsmacro) file. Property/Section Description VeriStand Macro File The path to the macro file to play back. Playback Mode Specifies the speed at which to play back the macro file: Ignore Timing—(Default) Plays back the macro file as fast as possible. Use Timing—

### Macro Player Step

Replays a previously recorded macro (.nivsmacro) file.

| Property/Section | Description |
| --- | --- |
| VeriStand Macro File | The path to the macro file to play back. |
| Playback Mode | Specifies the speed at which to play back the macro file: Ignore Timing—(Default) Plays back the macro file as fast as possible. Use Timing—Plays back the macro file at the speed at which it was recorded. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Other Steps

<!--NI_TOPIC bundle=veristand path=manage-individual-targets.html language=enus -->
## TOPIC 00266: Individual Target Management

- bundle_id: `veristand`
- source_path: `manage-individual-targets.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/manage-individual-targets.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can manage individual targets at run time by connecting and disconnecting individual targets and undeploying a system definition. The following table displays the ways you can manage targets at run time. Management Action Description Connect Individual Targets Connect to a new target for the fir

### Individual Target Management

You can manage individual targets at run time by connecting and disconnecting individual
 targets and undeploying a system definition.

The following table displays the ways you can manage targets at run time.

| Management Action | Description |
| --- | --- |
| Connect Individual Targets | Connect to a new target for the first time or reconnect to an old target after maintenance. |
| Disconnect Individual Targets | Disconnect a target for maintenance if it returns an error or develops a physical fault. |
| Undeploy a System Definition | Undeploy the system definition from an old target. |

Parent topic:

Deploying the System Definition File to a Real-Time Target

Related tasks:

- Connecting Individual Targets
- Disconnecting Individual Targets
- Undeploying the System Definition from an Individual Target

<!--NI_TOPIC bundle=veristand path=manual-overview.html language=enus -->
## TOPIC 00267: VeriStand Overview

- bundle_id: `veristand`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/manual-overview.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: VeriStand accelerates product development by enabling hardware validation and embedded software testing for hardware-in-the-loop (HIL) applications. VeriStand is software that engineers use to validate hardware and perform embedded software tests for HIL applications. Use VeriStand to accelerate you

### VeriStand Overview

VeriStand accelerates product development by enabling hardware validation and
 embedded software testing for hardware-in-the-loop (HIL)
 applications.

VeriStand is software that engineers use to validate hardware and perform
 embedded software tests for HIL applications. Use VeriStand to
 accelerate your product development with model integration,
 real-time stimulus generation, and an extensible open software
 environment.

#### Key Features

The features that set VeriStand apart.

- Import simulation models and control algorithms
- Configure real-time I/O
- Configure stimulus generation and deploy real-time tests
- Enable test automation with .NET, TestStand, Python, ASAM XIL, and other
 software
- Create custom plugins with an extensible ecosystem
- Respond to events with configurable alarms
- Configure a user interface during execution
- Monitor application data, alarm states, and system execution metrics

<!--NI_TOPIC bundle=veristand path=map-channel-alias.html language=enus -->
## TOPIC 00268: Mapping Channels and Aliases

- bundle_id: `veristand`
- source_path: `map-channel-alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/map-channel-alias.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect channels or aliases to one another. Before you begin, add a channel or alias to the system definition. Launch your project in the VeriStand Editor. In the Project Files pane, double click the system definition file (.nivssdf) to open the Mapping Diagram. Click a channel or alias terminal and

### Mapping Channels and Aliases

Connect channels or aliases to one another.

Before you begin, add a channel or
 alias to
 the system definition.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, double click the system
 definition file (.nivssdf) to open the Mapping
 Diagram.
3. Click a channel or alias terminal and drag a wire to another channel or alias
 terminal to map them. 
 Note You can create mappings
 between terminals with matching names by right-clicking two nodes and
 selecting Automap. If the direction of the mapping
 cannot be automatically determined, use the Automap
 dialog box that appears to specify the source of the mappings.

You can remove a mapping by selecting and deleting the
 wire.

Parent topic:

Tailoring Channels

Related tasks:

- Adding a User Channel
- Creating an Alias

<!--NI_TOPIC bundle=veristand path=map-scales-to-channels.html language=enus -->
## TOPIC 00269: Mapping Scales to Channels

- bundle_id: `veristand`
- source_path: `map-scales-to-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/map-scales-to-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use VeriStand to apply a scale when you deploy and run the system definition. You can map a scale to multiple channels, but a channel can only have one scale applied. Scales can map to the following: FPGA channels Single-point DAQ channels XNET signals and raw data frames Custom device channels that

### Mapping Scales to Channels

Use VeriStand to apply a scale when you deploy and run the system definition.

- FPGA channels
- Single-point DAQ channels
- XNET signals and raw data frames
- Custom device channels that you flag as scalable

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Create a scale.
4. Right-click Scales and select
 Map Scales.
5. In the Scale Mappings dialog box, select
 one channel from Sources and one or
 more channels from Destinations.
6. Click Connect to map the scale to the
 channel(s). 
 Note 
 Connect is only enabled if it is valid to apply the
 selected scale to the selected channel(s).
7. Save the system definition file.

The mapped channels appear in Mappings.

Parent topic:

Scaling a Channel on Hardware Devices

Related tasks:

- Scaling a Channel on Hardware Devices
- Importing and Exporting Scale Mappings

<!--NI_TOPIC bundle=veristand path=maximize-system-performance.html language=enus -->
## TOPIC 00270: Maximizing System Performance

- bundle_id: `veristand`
- source_path: `maximize-system-performance.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/maximize-system-performance.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase the efficiency of VeriStand by following best practices for your system definition, controllers, hardware, models, and reflective memory.

### Maximizing System Performance

Increase the efficiency of VeriStand by following best practices for your system
 definition, controllers, hardware, models, and reflective memory.

- [Streamlining the System Definition](streamline-system-definition.html) Decrease the complexity of your system definition by removing unused hardware I/O channels, maximizing the Convert Clock rate for multiplex sampling DAQ devices, and using hardware timing.
- [Configuring the BIOS Settings of the Controller](configure-bios-real-time-controller.html) Increase the performance of your real-time controller by enabling turbo boost and reducing the number of enabled cores.
- [Configuring the Ethernet Settings of the Controller](configure-ethernet-controller.html) Increase the performance of your real-time controller by using line interrupt packet detection.
- [Optimizing Hardware Performance](select-hardware.html) Increase the performance of your VeriStand system by using hardware timing, simultaneous sampling, USB CAN devices, PXIe devices, and not using Real-Time Hypervisor.
- [Improving Model Performance](improve-model-performance.html) Increase model performance by consolidating small models and preallocating arrays for LabVIEW models.
- [Optimizing Reflective Memory](optimize-reflective-memory.html) Improve the use of your reflective memory usage by reducing the dynamic data size, creating channel mappings between targets, and using data channels selectively with non-VeriStand systems.

Parent topic:

Debugging the System

<!--NI_TOPIC bundle=veristand path=message-box.html language=enus -->
## TOPIC 00271: Message Box Step

- bundle_id: `veristand`
- source_path: `message-box.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/message-box.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a pop-up message to the stimulus profile operator. Property/Section Description Message The message that the pop-up displays to the operator. Dialog Title The text that appears in the title bar of the pop-up. Default Text The text that appears on the button the operator uses to close out of

### Message Box Step

Displays a pop-up message to the stimulus profile operator.

| Property/Section | Description |
| --- | --- |
| Message | The message that the pop-up displays to the operator. |
| Dialog Title | The text that appears in the title bar of the pop-up. |
| Default Text | The text that appears on the button the operator uses to close out of the pop-up. For example, OK. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Other Steps

<!--NI_TOPIC bundle=veristand path=miscellaneous-primitives.html language=enus -->
## TOPIC 00272: Miscellaneous Primitives

- bundle_id: `veristand`
- source_path: `miscellaneous-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/miscellaneous-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add cosmetic and informational elements to real-time sequence code. The primitives on this palette do not affect the execution of sequence code. Palette object Description Block Organize your real-time sequence code. Comment Document in your real-time sequence code. Generate Error Create and return

### Miscellaneous Primitives

Add cosmetic and informational elements to real-time sequence code.

The primitives on this palette do not affect the execution of sequence code.

| Palette object | Description |
| --- | --- |
| Block | Organize your real-time sequence code. |
| Comment | Document in your real-time sequence code. |
| Generate Error | Create and return a user-defined error code and message in the stimulus profile test results file. |

Parent topic:

Real-Time Sequence Primitives

Related reference:

- Block
- Comment
- Generate Error

<!--NI_TOPIC bundle=veristand path=model-code-components.html language=enus -->
## TOPIC 00273: Model Code Components

- bundle_id: `veristand`
- source_path: `model-code-components.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-code-components.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The files model.h and model.c are used to implement your models. Create the following two files to implement your C/C++ model:model.h—Contains the type definitions for your model parameters. You must name the file model.h and include all user-visible parameters in your model.model.c—Contains your mo

### Model Code Components

The files model.h and model.c are used to
 implement your models.

- model.h—Contains the type definitions for your model parameters. Note You must name the file
 model.h and include all user-visible parameters in
 your model.
- model.c—Contains your model code. Make a copy of template.c and modify the
 copy to ensure you maintain interdependent structures, such as headers, imported
 and exported symbols, and functions that NI software recognizes, between your
 model code and ni_modelframework.c . Note You can name this
 .c file anything.

Parent topic:

VeriStand Model Framework

Related tasks:

- Creating a Model Header File
- Adapting the C Template to Model Code

<!--NI_TOPIC bundle=veristand path=model-command.html language=enus -->
## TOPIC 00274: Model Command

- bundle_id: `veristand`
- source_path: `model-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-command.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Model Command channel to change the model execution state at run time. If you configured your model to be initially paused, you can use this channel to start it. If your model gets into a desirable state for testing purposes, you can pause the model, save that state to a file, and then resto

### Model Command

Use the Model Command channel to change the model execution state at run time.

If you configured your model to be initially paused, you can use this channel to start it. If
 your model gets into a desirable state for testing purposes, you can pause the model,
 save that state to a file, and then restore the state later.

| Value | Status |
| --- | --- |
| 0 | Start the model. Note If the model is paused, it starts from the current state. |
| 1 | Pause the model. |
| 2 | Reset the model. |
| 3 | Prompt to save the model state to file after setting the model to idle. Note The model must be running or paused when you set this command. Otherwise, VeriStand ignores the command. |
| 4 | Prompt to restore the model state from file after setting the model to idle. Note The model must be running or paused when you set this command. Otherwise, VeriStand ignores the command. |

Parent topic:

Controlling and Monitoring Model Execution

<!--NI_TOPIC bundle=veristand path=model-components.html language=enus -->
## TOPIC 00275: Components of a Model

- bundle_id: `veristand`
- source_path: `model-components.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-components.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Models run on hardware targets and contain inports, outports, parameters, and signals to respond to stimuli from other parts of the system by producing outputs in a way that simulates the modeled item. The following table displays common model components that connect to other parts of the system or

### Components of a Model

Models run on hardware targets and contain inports, outports, parameters, and signals to
 respond to stimuli from other parts of the system by producing outputs in a way that
 simulates the modeled item.

| Component | Description |
| --- | --- |
| Inports and Outports | Communicates with other parts of the control system. You can map inports and outports directly to hardware inputs and outputs, other models in the system, system channels, and more. Inports and outports are dynamic values the simulation updates each time the model executes. |
| Parameters | Acts like variables in the model. You can manipulate parameters to tune the behavior of the simulation. For example, an operator can set a parameter before the model starts executing or update its value between the execution of discrete tests. |
| Signals | Serves as probes, or test points, of a model as it executes. |

- An inport that accepts the motor command from the motor controller
- An outport that returns the motor speed from the model
- Parameters that adjust the load on the motor
- A signal that returns internal data that aids in debugging

Parent topic:

Adding and Configuring a Model

<!--NI_TOPIC bundle=veristand path=model-configuration-exe-support.html language=enus -->
## TOPIC 00276: Model Configuration and Execution Support

- bundle_id: `veristand`
- source_path: `model-configuration-exe-support.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-configuration-exe-support.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand enables configuration and execution of FMI 2.0 and FMI 3.0 CoSimulation models on Windows and NI Real-Time Linux 64-bit systems. This support requires FMUs to have the proper executable binaries available. Model Configuration You can use the same general model import and configuration step

### Model Configuration and Execution Support

VeriStand enables configuration and execution of FMI 2.0 and FMI 3.0 CoSimulation
 models on Windows and NI Real-Time Linux 64-bit systems. This support
 requires FMUs to have the proper executable binaries available.

#### Model Configuration

You can use the same general model import and configuration steps in System
 Explorer to import FMUs into VeriStand.

The following table displays how a variable appears based on its causality when a FMU
 is imported into VeriStand.

| FMU Variable Causality | VeriStand Node Type |
| --- | --- |
| input | inport |
| output | outport |
| parameter | parameter that can be imported as a channel or accessed through Model Parameter Manager |
| calculatedParameter | not visible |
| independent | not visible |
| local | signal |
| structural parameter | not visible |

The rate of the model is defined by the stepSize attribute in
 the DefaultExperiment. Decimation must be configured based on
 the rate at which the VeriStand Engine is running.

#### Model Execution

The following table displays the model execution target architectures that FMI supports on the
 NI platform.

| NI Target Architecture | Folder in .zip |  |
| --- | --- | --- |
| FMI 2.0 | FMI 3.0 |  |
| PXI Linux | linux64 | x86_64-linux |
| Linux64 cRIO | linux64 | x86_64-linux |
| Windows | win64 | x86_64-windows |

#### Configuring Log Level

To configure the log level of the FMU, create a file named fmu_log_level_override in the following directory:

Windows:C:\Program Files\National Instruments\VeriStand <Version>

Linux RT:/usr/local/natinst/lib

The file should contain a single digit specifying the desired log level index, ranging from 0 to 7.
 The default log level Fatal will be used if the fmu_log_level_override file is not available.

The log file will be created in the same directory as the FMU, named <modelName>.fmu.log.
 In case of Linux RT, the default path for the FMU and the log file is /c/ni-rt/NIVeriStand/Models/<modelName>.fmu.log.

The log levels are given below:

| Log Level | Description |
| --- | --- |
| 0 | Nothing |
| 1 | Fatal |
| 2 | Error |
| 3 | Warning |
| 4 | Info |
| 5 | Verbose |
| 6 | Debug |
| 7 | All |

Note

Parent topic:

FMI Support

<!--NI_TOPIC bundle=veristand path=model-framework-components.html language=enus -->
## TOPIC 00277: Model Framework Components

- bundle_id: `veristand`
- source_path: `model-framework-components.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-framework-components.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The model framework includes files that define properties, identify functions for export, implement an interface, and create interdependent structures. Use the following table to locate files in the Model Framework to help implement your model code. File Description Installed location ni_modelframew

### Model Framework Components

The model framework includes files that define properties, identify functions for export,
 implement an interface, and create interdependent structures.

Use the following table to locate files in the Model Framework to help implement your model
 code.

| File | Description | Installed location |
| --- | --- | --- |
| ni_modelframework.h | A header file that includes the following components:Type definitions to define properties—such as inports, outports, parameters, and signals—of your model's outward-facing components.Functions that the VeriStand Model Framework exports to your compiled model. | <RootDrive>\\VeriStand\\<xxxx>\\ModelInterface\\ |
| ni_modelframework.c | Implements the common interface between your test application and your model code. | <RootDrive>\\VeriStand\\<xxxx>\\ModelInterface\\custom\\src |
| template.c | A template for your model code. Use this file to create code that maintains interdependent structures between your model and ni_modelframework.c. | <RootDrive>\\VeriStand\\<xxxx>\\ModelInterface\\custom\\examples |

Note

<RootDrive>

<xxxx>

Parent topic:

VeriStand Model Framework

<!--NI_TOPIC bundle=veristand path=model-parameter-formatting.html language=enus -->
## TOPIC 00278: Supported Formatting for Model Parameter Files

- bundle_id: `veristand`
- source_path: `model-parameter-formatting.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-parameter-formatting.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: You need to format .txt and .m files correctly to use them in the Model Parameter Manager tool. The following table displays the file types and how they should be formatted. File Type Description Example Formatting Limitations .txt Support for simple text files that conform to the model parameter fi

### Supported Formatting for Model Parameter Files

You need to format 
 .txt and 
 .m files correctly to use them in the 
 Model Parameter Manager tool.

| File Type | Description | Example Formatting | Limitations |
| --- | --- | --- | --- |
| .txt | Support for simple text files that conform to the model parameter file format that several other VeriStand features support. Refer to for more information about this type of file. | a 10 b a * 2 | The Model Parameter Manager imports and sets the result of the expression rather than the expression itself. The Model Parameter Manager sets the value of b to 20, not a * 2. Changes to the value of a do not affect b because the original expression is no longer valid. |
| .m | Support for .m model parameter files that perform one or both of the following actions: Assigns constant values to parameters. Defines parameter values as the result of simple expressions that include other parameters or variables defined in the .m file. This feature only supports simple assignments and expressions, not the entire .m file syntax. | temp = 1; b = (temp * 3) / 2; | Expressions must depend on other parameters or variables. The names of parameters and variables used in expressions must start with a letter and contain only alphanumeric characters or underscores. Otherwise the Model Parameter Manager displays an error glyph (). |

Parent topic:

Importing and Managing Batches of Model Parameters in the Workspace

Related concepts:

- Supported Syntax in Model Parameter Files

<!--NI_TOPIC bundle=veristand path=model-parameter-manager-syntax.html language=enus -->
## TOPIC 00279: Supported Syntax for Model Parameter Manager

- bundle_id: `veristand`
- source_path: `model-parameter-manager-syntax.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-parameter-manager-syntax.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Model Parameter Manager supports simple text files ( .txt) as model parameter files. The Model Parameter Manager allows text files that conform to the model parameter file format that other VeriStand features support. One limitation of using model parameter text files is that the manager imports

### Supported Syntax for Model Parameter Manager

The Model Parameter Manager supports simple text files (
 .txt) as model parameter files.

The Model Parameter Manager allows text files that conform to
 the model parameter file format that other VeriStand
 features support.

One limitation of using model parameter text files is that the manager imports and
 sets the result of the expression rather than the expression itself. The following
 parameter definitions demonstrate this limitation.

```text
a 10
b a * 2
```

In this example, the Model Parameter Manager sets the value of
 b to 20, not a * 2. Changes
 to the value of a do not affect b because the
 original expression is no longer valid.

Parent topic:

Importing and Managing Batches of Model Parameters with the VeriStand Editor

Related concepts:

- Supported Syntax in Model Parameter Files

<!--NI_TOPIC bundle=veristand path=model-parameter-syntax.html language=enus -->
## TOPIC 00280: Supported Syntax in Model Parameter Files

- bundle_id: `veristand`
- source_path: `model-parameter-syntax.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-parameter-syntax.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Format text (.txt) files to the correct syntax before you apply them to a simulation model. The text files must be in the following format.parameter1 delimiter value1 parameter2 delimiter value2 ...Text files cannot contain any column headers. The following table describes valid entries for the elem

### Supported Syntax in Model Parameter
 Files

Format text (.txt) files to the correct syntax before you apply them to
 a simulation model.

```text
parameter1 delimiter value1
parameter2 delimiter value2
...
```

Note

Note

<Common Data>\Examples\Stimulus Profile\Engine Demo\Stimulus
 Profiles\Update Model Parameters

| Element Type | Processing Notes | Valid Entries |
| --- | --- | --- |
| parameter | Valid parameters begin with a letter and contain only alphanumeric characters or underscores. Enclose a parameter whose expression does not fit these conventions in curly braces ({ }). For example, represent a block parameter that includes the model and block names separated by slashes in the following way: {model1/sine/parameter1}. | An expression of a model parameter, as displayed on the Model Parameter configuration page in System Explorer. An alias to a model parameter path. The command subscript to call another model parameter file. The name of a temporary variable.Note You can use temporary variables elsewhere in the same parameter file, but they are local to that file. |
| delimiter | — | A Tab entry, by pressing Tab on your keyboard. An equals sign (=). A comma (,). |
| value | Regardless of localized setting, periods (.) in a value are processed as decimal separators and commas (,) are processed as a thousands separator. In the VeriStand Editor, the localization setting is considered when displaying values. This may lead to situations where values that contain a period in the file will be displayed with commas. | A numeric constant (double). A matrix in row-major form with the following element types. Numeric constants (doubles). Fractions of the form x/y, where x and y are doubles. A temporary variable that represents a scalar value. Note For example, if a and b are declared variables, then [1 -2/3; a b] is a valid 2 x 2 matrix. The constants Infinity and -Infinity. An expression that follows the VeriStand expression syntax. A path to another model parameter file.Note A path is only valid if the corresponding parameter entry is subscript. |

Parent topic:

Setting Model Parameters

Related tasks:

- Aliasing Parameter Names in a Model Parameter File
- Calling a Subscript from a Model Parameter File
- Declaring Temporary Variables in a Model Parameter File

<!--NI_TOPIC bundle=veristand path=model-status.html language=enus -->
## TOPIC 00281: Model Status

- bundle_id: `veristand`
- source_path: `model-status.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-status.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Model Status channel to monitor how the model is operating at run time. The Model Status channel returns the model's state, such as running, resetting, and stopped. Refer to the following table to determine what values VeriStand associates with each status. Value Status 0 Running 1 Paused 2

### Model Status

Use the Model Status channel to monitor how the model is operating at run time.

The Model Status channel returns the model's state, such as running, resetting, and stopped.

| Value | Status |
| --- | --- |
| 0 | Running |
| 1 | Paused |
| 2 | Resetting |
| 3 | Idle |
| 4 | Stopped |
| 5 | Restoring |
| 6 | Saving |

Parent topic:

Controlling and Monitoring Model Execution

<!--NI_TOPIC bundle=veristand path=model-time.html language=enus -->
## TOPIC 00282: Model Time

- bundle_id: `veristand`
- source_path: `model-time.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/model-time.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Model Time channel to verify that the model is running at the correct rate. You can compare the model time to the value of the System Time system channel to determine if the model is executing slower or faster than real time. The following equation describes how the VeriStand Engine determin

### Model Time

Use the Model Time channel to verify that the model is running at the correct rate.

You can compare the model time to the value of the System Time system channel to determine if the
 model is executing slower or faster than real time.

The following equation describes how the VeriStand Engine determines the rate to execute
 each model.

model rate = Primary Control Loop (PCL) rate / model decimation

If the rate for a model is incorrect, adjust its decimation and monitor the model time
 again.

Parent topic:

Controlling and Monitoring Model Execution

<!--NI_TOPIC bundle=veristand path=modify-control-mappings.html language=enus -->
## TOPIC 00283: Modifying Control Mappings at Run Time

- bundle_id: `veristand`
- source_path: `modify-control-mappings.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/modify-control-mappings.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Change the channel mapping for a control or indicator while the Workspace runs. Update the Control Label to match the new channel. Right-click a control or indicator. In the Item Properties dialog box, click Browse. In the Browse dialog box, select a channel in the configuration tree, and click OK.

### Modifying Control Mappings at Run Time

Change the channel mapping for a control or indicator while the Workspace runs.
 Update the Control Label to match the new channel.

1. Right-click a control or indicator.
2. In the Item Properties dialog box, click
 Browse.
3. In the Browse dialog box, select a channel in the
 configuration tree, and click OK.
4. In the Control Label field, rename the control or
 indicator, and click OK.

Parent topic:

Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=monitor-replay-status.html language=enus -->
## TOPIC 00284: Monitoring Replay Status

- bundle_id: `veristand`
- source_path: `monitor-replay-status.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/monitor-replay-status.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Check the status of your replaying logged NI-XNET CAN frame data using the Error, Pending Frames, and Status channels. Before you begin, you must add a data replay file. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select

### Monitoring Replay Status

Check the status of your replaying logged NI-XNET CAN frame data using the
 Error, Pending Frames, and
 Status channels.

Before you begin, you must add a data replay
 file.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET»CAN in the configuration tree.
4. Click a port.
5. Click Outgoing»Data Replay and click a log file.
6. Depending on your goal, click a channel. 
 Goal
ChannelReview the most recent replay
 error.
Error
Determine whether data is replaying as
 expected
Pending Frames
Find the current status of the replay
 process.
Status

You can monitor these channels from
 the Workspace or map them to other channels within the project.

Parent topic:

Replaying Logged NI-XNET CAN Frame Data

Related tasks:

- Replaying Logged NI-XNET CAN Frame Data
- Mapping Channels and Aliases

<!--NI_TOPIC bundle=veristand path=monitor-xnet-data-logging.html language=enus -->
## TOPIC 00285: Monitoring Incoming NI-XNET Frame Logging

- bundle_id: `veristand`
- source_path: `monitor-xnet-data-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/monitor-xnet-data-logging.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Check the status of your logging of incoming NI-XNET frames by using the Error, Finished Files, and Status channels. Before you begin, you must add a raw frame data logging file. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) an

### Monitoring Incoming NI-XNET Frame
 Logging

Check the status of your logging of incoming NI-XNET frames by using the Error, Finished
 Files, and Status channels.

Before you begin, you must add a raw frame data
 logging file.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET in the configuration tree.
4. Select an NI-XNET LIN, FlexRay, or CAN port.
5. Click Incoming»Raw Frame Data Logging and select a log file.
6. Depending on your goal, click a channel. 
 Goal
ChannelReview the most recent logging
 error.
Error
Determine what files are ready for use by
 other processes.
Finished Files
Find the current status of the data
 logging process.
Status 
 You can monitor these channels from the VeriStand Editor and Workspace,
 or map them
 to other channels within the project.

Parent topic:

Logging Incoming NI-XNET Frames

Related tasks:

- Logging Incoming NI-XNET Frames
- Mapping Channels and Aliases

<!--NI_TOPIC bundle=veristand path=multitask.html language=enus -->
## TOPIC 00286: MultiTask Structure

- bundle_id: `veristand`
- source_path: `multitask.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/multitask.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A structure that branches real-time sequence code execution into one or more child tasks. On each time step, the MultiTask structure iteratively executes code from each child task until the task either terminates or yields execution to the next time step. MultiTask structures have two child tasks by

### MultiTask Structure

A structure that branches real-time sequence code execution into one or more child
 tasks.

On each time step, the MultiTask structure iteratively executes code
 from each child task until the task either terminates or yields execution to the
 next time step. MultiTask structures have two child tasks by default, but you can
 add more Task primitives from the Multitasking palette.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Multitasking Primitives

<!--NI_TOPIC bundle=veristand path=multitasking-primitives.html language=enus -->
## TOPIC 00287: Multitasking Primitives

- bundle_id: `veristand`
- source_path: `multitasking-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/multitasking-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Multitasking primitives to divide real-time sequence code into multiple tasks that execute in parallel. Palette object Description MultiTask A structure that branches real-time sequence code execution into one or more child tasks. Stop Task Stops a Task in a MultiTask structure. Task A block

### Multitasking Primitives

Use the Multitasking primitives to divide real-time sequence code into multiple tasks
 that execute in parallel.

| Palette object | Description |
| --- | --- |
| MultiTask | A structure that branches real-time sequence code execution into one or more child tasks. |
| Stop Task | Stops a Task in a MultiTask structure. |
| Task | A block of code in a MultiTask structure. |

Parent topic:

Structures Primitives

Related reference:

- MultiTask Structure
- Stop Task
- Task

<!--NI_TOPIC bundle=veristand path=navigate-stimulus-profile-editor.html language=enus -->
## TOPIC 00288: Navigating the Stimulus Profile Editor Environment

- bundle_id: `veristand`
- source_path: `navigate-stimulus-profile-editor.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/navigate-stimulus-profile-editor.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Stimulus Profile Editor to create, modify, and execute stimulus profiles and real-time sequences. The Stimulus Profile Editor is a highly customizable environment consisting of various elements that you can show, hide, resize, or rearrange to suit your needs. The editor is a separate executa

### Navigating the Stimulus Profile Editor
 Environment

Use the Stimulus Profile Editor to create, modify, and execute stimulus profiles and
 real-time sequences.

Stimulus Profile Editor

The editor is a separate executable
 from System Explorer, VeriStand Editor, or
 Workspace. It allows you to develop your test profiles in
 parallel with the system definitions and user interfaces that they interact with.
 However, a stimulus profile must be associated with a deployed VeriStand system
 definition in order to execute.

In the Stimulus Profile
 Editor, you can start multiple concurrent stimulus profile
 executions. Each stimulus profile execution performs sequential execution of one or
 more real-time sequences.

To open the Stimulus Profile
 Editor, use the VeriStand Editor and click Tool Launcher»Stimulus Profile Editor.

Use the following sections of the Stimulus Profile Editor to modify your
 code.

[IMAGE alt='image' src='GUID-E0EB2183-C76B-40C0-8BD7-2A190C9F2805-a5.gif']

| 1 | Ribbon—Perform actions such as editing the environment and running profiles and sequences. |
| --- | --- |
| 2 | File menu—Perform actions such as creating, saving, and opening profiles and sequences. |
| 3 | Real-time sequence code. |
| 4 | Stimulus profile—Acts as the test executive that defines the stimuli to apply to a unit under test (UUT). |
| 5 | Real-time sequence—Defines specific tasks for a UUT. |
| 6 | Variables pane—displays all the variables the selected real-time sequence has access to at run time and uses in expressions. |
| 7 | Property Browser—Displays the editable properties of stimulus profile steps, real-time sequences, primitives, and references. Select an item in the code of a stimulus profile or real-time sequence to configure that item. |
| 8 | Context Help—Displays suggested help for an item that you hover over. |
| 9 | Status Bar—Displays the Project/System definition that you launched the editor from and the Gateway IP Address. By default, VeriStand associates stimulus profiles with the system definition file of the project that you create them. You can Browse to a different project or system definition from the editor. |
| 10 | References pane—Contains a list of all the real-time sequences that the selected real-time sequence references. |
| 11 | Warning and Errors list—Lists any errors, warnings, or messages in a stimulus profile or real-time sequence file. Click an error, warning, or message to display a description. |
| 12 | Sequences palette—Contains real-time sequences you add to a stimulus profile or real-time sequence. |
| 13 | Primitives palette—Contains programming building blocks, such as statements and variables, you can add to a real-time sequence. |

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related tasks:

- Creating a Stimulus Profile Editor Layout

<!--NI_TOPIC bundle=veristand path=new-features-and-changes.html language=enus -->
## TOPIC 00289: VeriStand New Features and Changes

- bundle_id: `veristand`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/new-features-and-changes.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of VeriStand. Discover what is new in the latest releases of VeriStand.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might incl

### VeriStand
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of VeriStand.

VeriStand

Note

Release Notes

#### VeriStand 2026 Q1 New Features

Explore the new features in VeriStand 2026 Q1,
 including engine performance improvements, GUI support for runtime configuration, and
 TestStand compatibility.

##### VeriStand Engine Performance
 Improvement

Removed redundant memory copies to improve Data Processing Loop execution time.

##### GUI support for Runtime
 Configuration Feature

Users can now configure runtime-configurable channels using the VeriStand Editor and
 use these channels which are added at runtime across VeriStand controls, charts, and
 other components of Veristand Editor.

##### Enhancements

Optimized Rx operations in Ballard ARINC 429 custom device.

##### VeriStand Steps for TestStand 2026 Q1

VeriStand Steps for TestStand 2026 Q1 release provides compatibility for TestStand
 2025 and TestStand 2026.

Related concepts:

- Overview of Runtime Configurability

#### VeriStand 2025 Q4 New Features

Explore the new features in VeriStand 2025 Q4,
 including runtime configuration, U64 data visualization, and performance
 optimizations.

##### Change the Configuration of
 Sections of a Deployed System Without Undeploying

ActionVIOnRecompile.vi

Runtime
 Configuration Support Example

Note

Note

##### U64 Data Value Visualization in
 VeriStand Screen

Added a control to VeriStand Screen which allows U64 data value visualization.

##### Parallel Execution Mode State Transition
 Optimizations

Optimized state transitions in the Primary Control Loop when
 using the Parallel execution mode to allocate more time for model
 execution.

##### .vsmodel I/O Performance
 Improvements

Improved I/O performance in .vsmodel, allowing faster
 execution when I/O ports are structured with contiguous variables of the same data
 type.

##### VeriStand UI Chart Display Rate
 Optimizations

Improved the responsiveness of the VeriStand UI by
 optimizing the chart display rate, which allows for better performance when working
 with a large number of charts.

##### IP to FPGA Conversion Utility
 Migrated to .NET 8

The IP to FPGA Conversion Utility has been migrated to .NET 8 from .NET
 Framework.

Related information:

- Runtime Configuration Support Example - NI GitHub
- IP to FPGA Conversion Utility

#### VeriStand 2025 Q3 New Features

Explore the new features in VeriStand 2025 Q3,
 including new import/export channels, model generation enhancements, and LIN frame
 processing support.

##### Import/Export Channels in Logging
 Specification

You now can import channels from and export channels to a text file in the logging
 specification in VeriStand.

##### VeriStand Model Generation Support
 for Signals with Protected Models

You now can use signals alongside protected reference models in VeriStand Model
 Generation support.

##### VeriStand Mode Generation Support
 Build Time Improvement

.vsmodels now build significantly faster when large numbers of parameters are present
 in a data dictionary.

##### Supporting Automatic Frame
 Processing for LIN Frames

For LIN frames, VeriStand XNET now supports adding a custom checksum and rolling
 counter in Automatic Frame Processing (AFP).

##### Configuring Lowpass Filters for Digital AI Filtering

VeriStand now supports configuring lowpass filters for the NI 4302, 4303, 4304, 4305, 4339, 4480, and 4481 modules.

#### VeriStand 2025 Q2 New Features

Explore the new features in VeriStand 2025 Q2,
 including FIPS support, LabVIEW 2025 64-bit compatibility, and error messages
 enhancements.

##### Running VeriStand on Windows Machine with FIPS

VeriStand
 can now run on a Windows machine with federal information processing
 standards (FIPS).

##### IP
 to FPGA Conversion Utility Supporting LabVIEW 2025
 64-Bit

IP to FPGA Conversion Utility 2025 Q2 now supports
 LabVIEW 2025 Q1 64-bit.

##### Configurable Time Axis for VeriStand Chart

VeriStand
 chart now allows you to configure any monotonically increasing
 channel as a time axis.

##### VeriStand Model Generation Support for Block
 Parameters

Use VeriStand Model Generation Support to
 access block parameters from Simulink models as model parameters in
 VeriStand. For more information, refer to *How VeriStand
 Imports Models from the Model Generation Support MATLAB
 Add-on* and the *VeriStand Model Generation
 Support* documentation.

##### Error Message Enhancement

Existing error messages now include more
 information to help you locate the source of the error.

Related concepts:

- How VeriStand Imports Models from the Model Generation Support MATLAB Add-on

Related information:

- VeriStand Model Generation Support

#### VeriStand 2025 Q1 New Features

Explore the new features in VeriStand 2025 Q1,
 including TestStand automation, LabVIEW 2025 Q1 support, model generation enhancements, and
 GCC compiler upgrades.

##### VeriStand Steps for TestStand

VeriStand Steps for TestStand are sets of
 custom steps that allow you to automate VeriStand and develop/reuse test sequences
 for hardware-in-the-loop (HIL) systems.

This product is available for download
 using NI Package Manager, or at *ni.com/downloads*. Follow the prompts in
 NI Package Manager to install VeriStand Steps for TestStand.

Please refer to
 the *VeriStand Steps for TestStand* for more information on how to use
 this application.

##### LabVIEW 2025 Q1
 Support

VeriStand is compatible with LabVIEW 2025 Q1 64-bit. All custom
 devices, LabVIEW models, and LabVIEW applications that contain the VeriStand API
 require this LabVIEW version. The VeriStand API will not install in previous
 versions of LabVIEW.

##### Enhanced VeriStand Model Generation Support for VeriStand IO
 Blocks

VeriStand Inport/Outport blocks now supports the enum data type,
 and can be connected to masked blocks and additional blocks like bus
 selector.

##### GCC
 Compiler Upgrade for VeriStand Model Generation Support

NI GCC
 Cross-Compiler for NI Linux Real-Time targets toolchain is upgraded to GNU C &
 C++ Compile Tools x64 2024Q4.

Related information:

- VeriStand Steps for TestStand

#### VeriStand
 2024 Q3 New Features

Explore the new features in VeriStand 2024 Q3, including
 FMI support for Enum data types, debug logging enhancements, and Simulink model
 integration.

##### FMI Support for Enum Data
 Type

Import FMUs with Inports/Outports/Parameters/Signals of type Enum as VeriStand
 channels.

##### Enhanced Debug Logging for
 Simulation Models in Target Log Viewer

Use the Target Log Viewer to understand debug information from FMUs, .vsmodels, and
 .lvmodels.

##### Simulink Model Enum Channels on
 VeriStand Screens

Scalar enum variables from .vsmodel and .fmu (3.0) are visible on VeriStand screens
 with their type definitions.

##### IP to FPGA Conversion Utility Supporting LV 2024 64-bit

IP to FPGA Conversion Utility 2024 Q3 now supports LabVIEW 2024 Q1 64-bit.

##### Support for Custom Reference Designs in HDL Coder Support Package for NI FPGA
 Hardware

The HDL Coder Support Package for NI FPGA hardware now includes support for custom
 reference designs, enabling the integration of Simulink models into existing LabVIEW
 FPGA projects.

#### VeriStand
 2024 Q2 New Features

Explore the new features in VeriStand 2024 Q2, including
 new model generation support, APIs for configuring ECU network clusters, and Synopsys Silver
 FMI 3.0 Virtual ECU support.

##### VeriStand Model Generation Support
 for Enum DataType

Use VeriStand Model Generation Support to import Inport/Outport/Signals/Parameter of
 type Enum from Simulink models as channels.

##### VeriStand Model Generation Support
 for VeriStand IO Blocks

Place VeriStand Inport/Outport blocks from VeriStand Model Generation Support anywhere in the
 subsystem hierarchy in your Simulink model to access them as model Inport/Outport
 channels.

##### APIs to Configure ECU Network Cluster

Configure Virtual ECU Clusters programmatically using APIs in the System Definition namespace.

##### Synopsys Silver FMI 3.0 Virtual ECU Support

Configure and execute Virtual ECUs from Synopsys Silver that follow the FMI 3.0
 standard.

Related concepts:

- How VeriStand Imports Models from the Model Generation Support MATLAB Add-on
- FMI Support

Related information:

- VeriStand Model Generation Support

#### VeriStand 2024 Q1 New Features

Explore the new features in VeriStand 2024 Q1,
 including LabVIEW 2024 Q1 support, the Virtual ECU Toolkit, and FMI 3.0 support.

##### LabVIEW 2024 Q1 Support

VeriStand is compatible with LabVIEW 2024 Q1 64-bit. All custom devices, LabVIEW
 models, and LabVIEW applications that contain the VeriStand API require this LabVIEW
 version. The VeriStand API will not install in previous versions of LabVIEW.

##### VeriStand Virtual ECU Toolkit

Use the VeriStand Virtual ECU Toolkit to integrate and execute virtual electronic
 control units (ECUs) for hardware-in-the loop (HIL) testing. Virtual ECUs allow you
 to test devices quickly, with a more realistic rest bus simulation, and with less
 effort for creating the bus simulation.

##### FMI 3.0 Support

VeriStand can configure and execute FMUs that follow the 3.0 standard. For more
 information on the support, refer to FMI Support.

Related tasks:

- Integrating Virtual ECUs

#### VeriStand 2023 Q4 New Features

Explore the new features in VeriStand 2023 Q4,
 including Alarm Monitor display enhancements, Launcher interface enhancements, and model
 generation support for simulation states.

##### Alarm Monitor Displays Trip
 Message and Value

The Alarm Monitor in the VeriStand Editor now actively showcases Trip Messages across
 all three tabs (Active, History, Rules). Furthermore, it actively presents Values
 within the Active and History tabs. Additionally, the Alarm Log actively records
 both the Trip Message and Value for comprehensive tracking.

##### Revamped Launcher
 Interface

The VeriStand Launcher has undergone a significant transformation, introducing
 separate tabs for Projects and Learning. To access a collection of preloaded
 VeriStand projects and educational resources, navigate to the Learning tab.
 Meanwhile, the Projects tab offers access to Default Projects and enables users to
 incorporate their custom template projects seamlessly.

##### VeriStand Model Generation Support
 for Simulation States

With VeriStand Model Generation Support, you can now preserve the state of a .vsmodel
 file during execution, allowing for later restoration of the model using the saved
 state through an XML file. To save and restore states, use the .NET IModel method or
 the Screen/Workspace.

Related information:

- IModel Methods

#### VeriStand 2023 Q3 New Features

Explore the new features in VeriStand 2023 Q3,
 including model generation support, Python API, more command line options, and FMU
 logging.

##### VeriStand Model Generation Support
 for Importing Non-Virtual Bus Signals

Use VeriStand Model Generation Support to import non-virtual bus signals from
 Simulink models as channels. For more information, refer to How VeriStand Imports
 Models from the Model Generation Support MATLAB Add-on and the VeriStand Model
 Generation Support add-on documentation.

##### Python System Definition API

Use niveristand to script system definition
 (.nivssdf) files for use in the VeriStand Editor and deploy
 them to the VeriStand Engine. For more information, you can refer to the Getting
 Started With VeriStand documentation. Note that this feature supports multiple
 VeriStand versions.

##### Expanded VeriStand.exe Command Line
 Options

Use the command line to execute processes in VeriStand, including the ability to now
 open and close specific files or documents in a project. For more information on
 specific commands and their functionalities, refer to VeriStand Command Line Options
 documenatation.

##### Support for FMU Logging in
 VeriStand

Set the logging level for FMUs by editing a configuration file to debug failures. For
 more information on configuring the log levels, refer to FMI Support
 documentation.

Related tasks:

- Running VeriStand Operations Using the Command Line

Related information:

- Getting Started With VeriStand

#### VeriStand 2023 Q2 New Features

Explore the new features in VeriStand 2023 Q2, including
 engine performance enhancements, model generation support, ESI file importing, screen
 cluster arrangement options, and IP to FPGA conversion utility updates.

##### VeriStand
 Engine Performance

In System Explorer, the new
 default for the PCL DAQ timing source is Signal From Task (Sample
 Complete). This default applies to new projects when the timing
 source is set to DAQ Timing or Automatic
 Timing and there is a NI-DAQ device with at least one analog input
 hardware-timed single point channel.

The Signal From Task (Sample Complete)
 default option sends a tick to the PCL each time the Master DAQ device finishes
 acquiring an AI channel sample. This setting is beneficial for multiplexed DAQ
 modules with many channels. The setting has no impact on simultaneous sampled module
 behavior.

Other VeriStand Engine improvements include loop processing
 reductions for systems with a high count of channels, mappings, and faultable
 channels. Large systems, such as those with more than 20,000 channels and 10,000
 mappings, can experience HP Loop duration reductions of more than 50
 microseconds.

##### VeriStand
 Model Generation Support for Importing Signals

Use VeriStand Model
 Generation Support to import signals from Simulink models as channels. For more
 information, refer to How VeriStand Imports Models from the Model Generation Support
 MATLAB Add-on and the VeriStand Model Generation Support add-on
 documentation.

##### ESI File Importing

Import an EtherCAT
 Slave Information (ESI) file into VeriStand using the Scan Engine and EtherCAT
 Custom Device without installing LabVIEW. To begin importing the ESI file, open
 System Explorer and navigate to the custom
 device.

##### Screen Cluster Arrangement Options

Use
 additional cluster arrangement options on VeriStand screens to compact the
 appearance of large cluster hierarchies. To access these options in the
 VeriStand Editor, navigate to File»Preferences and click Screen to select a cluster arrangement.

##### IP to FPGA Conversion Utility supporting LV 2023
 64-bit

IP to FPGA Conversion Utility 2023 Q2 now supports LabVIEW 2023 Q1
 64-bit.

#### VeriStand 2023 Q1 New Features

Explore the new features in VeriStand 2023 Q1, including
 LabVIEW 2023 Q1 support, XCP communication for Simulink models, DAQmx counter operations,
 and HDL Coder support for PXIe R-series Kintex-7 and Simscape models.

##### LabVIEW
 2023 Q1 Support

VeriStand is compatible with LabVIEW 2023 Q1 64-bit. All
 custom devices, LabVIEW models, and LabVIEW applications that contain the VeriStand
 API require this LabVIEW version. The VeriStand API will not install in previous
 versions of LabVIEW.

LabVIEW 2023 Q1 64-bit supports CompactRIO controllers
 and NI R Series modules. Custom devices and LabVIEW FPGA development can use LabVIEW
 64-bit.

Note

##### External Mode with XCP
 Communication

Enable external mode with XCP communication when building a
 MathWorks Simulink model to monitor signals and tune parameters from the Simulink
 environment. XCP provides additional capabilities such as viewing signals within
 referenced models. For more information, refer to the VeriStand Model Generation
 Support documentation on GitHub.

##### Terminal Specification for DAQmx Counter
 Operations

Use System Explorer or the System
 Definition .NET API to specify the following terminals for DAQmx counter
 tasks.

- Terminal for counter I/O tasks.
- A/B/Z terminal for position measurement tasks.

Specifying these terminals allows modules to use all counters through
 non-default PFI lines. For more information, refer to documentation for your
 module.

##### HDL Coder Support for PXIe R-series Kintex-7 and
 Simscape Models

HDL Coder Support Package for NI FPGA Hardware supports
 the following:

- PXIe R-series Kintex-7 modules ─ Use the support package to remain within HDL Coder while
 generating a bitfile from a Simulink model for compatible NI FPGA hardware.
- Simscape models.

Related information:

- VeriStand Model Generation Support

<!--NI_TOPIC bundle=veristand path=new-project.html language=enus -->
## TOPIC 00290: Creating a New Project

- bundle_id: `veristand`
- source_path: `new-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/new-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a new project in VeriStand to develop, prototype, and test control systems using hardware I/O and simulation models. Open VeriStand. Click Default Project. Enter a Project Name. Select a Location to save the project. Select a System Definition. If you do not have a system definition, leave th

### Creating a New Project

Create a new project in VeriStand to develop, prototype, and test
 control systems using hardware I/O and simulation models.

1. Open VeriStand.
2. Click Default Project.
3. Enter a Project Name.
4. Select a Location to save the project.
5. Select a System Definition. 
 Note If you do not have a system definition, leave this field as
 None chosen. VeriStand will create a new system
 definition file with the same name as the project.
6. Click Create.

Parent topic:

Configuring the System

<!--NI_TOPIC bundle=veristand path=new-system-definiton.html language=enus -->
## TOPIC 00291: Creating a New System Definition File

- bundle_id: `veristand`
- source_path: `new-system-definiton.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/new-system-definiton.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can create a new system definition file without creating a new project with System Explorer. Open VeriStand. Create or open a VeriStand project. Click Configure... to open System Explorer. Click File New to open the New System Definition dialog box. Enter a System Definition name. Click OK. Afte

### Creating a New System Definition File

You can create a new system definition file without creating a new project with
 System Explorer.

1. Open VeriStand.
2. Create or open a VeriStand project.
3. Click Configure... to open System
 Explorer.
4. Click File»New to open the New System Definition dialog
 box.
5. Enter a System Definition name.
6. Click OK.

After creating the system definition file, add it to the
 project.

Parent topic:

Configuring a System Definition File

Related tasks:

- Creating a New Project
- Adding and Activating a System Definition File

<!--NI_TOPIC bundle=veristand path=ni-hardware-support.html language=enus -->
## TOPIC 00292: NI Hardware Support

- bundle_id: `veristand`
- source_path: `ni-hardware-support.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/ni-hardware-support.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand supports NI-XNET devices, NI-DAQ devices, and NI FPGA targets. For the best performance, use NI-DAQ devices that support hardware-timed single point (HWTSP) I/O or on-demand sampling. Refer to DAQ Devices with Hardware-Timed Single Point Sampling Mode Support for a list of NI-DAQ devices t

### NI Hardware Support

VeriStand supports NI-XNET devices, NI-DAQ devices, and NI FPGA targets.

For the best performance, use NI-DAQ devices that support hardware-timed single point (HWTSP) I/O
 or on-demand sampling. Refer to *DAQ Devices with Hardware-Timed Single Point
 Sampling Mode Support* for a list of NI-DAQ devices that support HWTSP
 I/O. Refer to the custom device’s GitHub repository for a list of supported
 modules.

Note

Scan Engine and EtherCAT
 custom device GitHub repository

| Hardware Feature | NI-XNET Devices | NI-DAQ Devices | NI FPGA Targets |
| --- | --- | --- | --- |
| Custom FPGA VIs | No | No | Yes1 |
| Hardware timing | No | Yes | Yes |
| Analog I/O | No | Yes | Yes |
| Digital I/O | No | Yes | Yes |
| Pulse Width Modulation (PWM) I/O | No | Yes2 | Yes |
| Auto-discovery of installed devices and I/O modules | Yes | Yes | Yes |
| 1 Refer to the FPGA Targets with Built-in Support section for a list of NI FPGA targets for which VeriStand provides bitfiles and FPGA configuration files. 2 Device support for PWM I/O includes: Generating pulses—If HWTSP sample mode is enabled (default) for a counter output channel, only X Series PCI and PXI devices support generating pulses with that channel. However, if that property is disabled for a Counter Output (CO) channel, all DAQ devices support generating pulses. Measuring pulses—Only X Series PCI and PXI devices support measuring pulses with counter input channels. |  |  |  |

#### Supported
 Targets

- PXI/PCI—Any PXI controller with at least 256 MB of RAM.
- CompactRIO/Single-Board RIO—Any CompactRIO or Single-Board RIO device with at least 128 MB of
 RAM. Note The cRIO-906*x* series meets this requirement, but
 because it is an ARM-based controller, it is not supported in VeriStand
 2021 or later.
- Desktop PC—Any PC running Windows 7, Vista, XP Service Pack 3 or later,
 Server 2003 R2 (32-bit), or Server 2008 R2 (64-bit).

#### FPGA
 Targets with Built-in Support

- NI cRIO-9103 Note The files provided for the NI cRIO-9103 are configured for the NI 9215,
 NI 9263, NI 9411, and NI 9474 I/O modules.
- NI PXI/PCI-7811R
- NI PXI/PCI-7813R
- NI PXI/PCI-7831R
- NI PXI/PCI-7833R
- NI PXI/PCIe-7841R
- NI PXI/PCIe-7842R
- NI PXI/PCIe-7851R
- NI PXI/PCIe-7852R
- NI PXI-7853R
- NI PXI-7854R

All bitfiles use direct memory access (DMA) to transfer data.

You
 can use the LabVIEW FPGA Module to create custom FPGA bitfiles for these or other
 FPGA targets.

#### Supported SCXI Modules

- SCXI-1100
- SCXI-1102
- SCXI-1102B
- SCXI-1102C
- SCXI-1104
- SCXI-1104C
- SCXI-1112
- SCXI-1120
- SCXI-1120D
- SCXI-1121
- SCXI-1122
- SCXI-1124
- SCXI-1125
- SCXI-1126
- SCXI-1127
- SCXI-1128
- SCXI-1140
- SCXI-1141
- SCXI-1142
- SCXI-1143
- SCXI-1160
- SCXI-1161
- SCXI-1162
- SCXI-1162HV
- SCXI-1163
- SCXI-1163R
- SCXI-1190
- SCXI-1191
- SCXI-1192
- SCXI-1520
- SCXI-1530
- SCXI-1531
- SCXI-1540
- SCXI-1581

Related tasks:

- Adding and Configuring a Hardware Device

Related information:

- DAQ Devices with Hardware-Timed Single Point Sampling Mode
 Support
- Scan Engine and EtherCAT custom device GitHub
 repository
- Creating a Custom FPGA Bitfile

<!--NI_TOPIC bundle=veristand path=open-veristand-project.html language=enus -->
## TOPIC 00293: Open VeriStand Project Step

- bundle_id: `veristand`
- source_path: `open-veristand-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/open-veristand-project.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens the VeriStand project (.nivsprj) file you specify. A stimulus profile must be associated with an open and deployed project to execute real-time sequences. Use this step to open a project file directly from a stimulus profile. You can then use the Control Active VeriStand Project step to deploy

### Open VeriStand Project Step

Opens the VeriStand project (.nivsprj) file you specify.

| Property/Section | Description |
| --- | --- |
| Show Project | If TRUE, specifies to display the project in the VeriStand Editor. |
| Project Path | Specifies the path to the project file. This can be an absolute or relative path. Relative paths must be relative to the directory that contains the stimulus profile. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Security | Includes the following properties: Username—(Optional) Specifies the username to use to access the project. If the project has only one defined user, such as the Administrator, and that user has no password, you do not need to enter the username. Password—(Optional) Specifies the password associated with the Username. Not all usernames have associated passwords. If a username does have an associated password and you leave this property empty, VeriStand prompts you to enter the password when this step executes. |

Parent topic:

Project Steps

Related reference:

- Control Active VeriStand Project Step

<!--NI_TOPIC bundle=veristand path=open-workspace-tool-step.html language=enus -->
## TOPIC 00294: Open Workspace Tool Step

- bundle_id: `veristand`
- source_path: `open-workspace-tool-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/open-workspace-tool-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens the workspace tool specified by VI Path. Property/Section Description Initialization Time Specifies the time in milliseconds to allow for the workspace tool to initialize after it loads. The stimulus profile does not proceed to the next step until the initialization time elapses. VI Path Speci

### Open Workspace Tool Step

Opens the workspace tool specified by VI Path.

| Property/Section | Description |
| --- | --- |
| Initialization Time | Specifies the time in milliseconds to allow for the workspace tool to initialize after it loads. The stimulus profile does not proceed to the next step until the initialization time elapses. |
| VI Path | Specifies the path to the workspace tool VI. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Workspace Tools Steps

<!--NI_TOPIC bundle=veristand path=open-workspace.html language=enus -->
## TOPIC 00295: Open VeriStand Workspace

- bundle_id: `veristand`
- source_path: `open-workspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/open-workspace.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens the VeriStand Workspace and loads the screen (.nivsscreen) file associated with the currently active VeriStand project. Open the Workspace to see the affects of the test on channel values while the stimulus profile executes. Property/Section Description Description Specifies a description for

### Open VeriStand Workspace

Opens the VeriStand Workspace and loads the screen
 (.nivsscreen) file associated with the currently active VeriStand
 project.

Open the Workspace to see the affects of the test on channel
 values while the stimulus profile executes.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Workspace Steps

<!--NI_TOPIC bundle=veristand path=optimize-reflective-memory.html language=enus -->
## TOPIC 00296: Optimizing Reflective Memory

- bundle_id: `veristand`
- source_path: `optimize-reflective-memory.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/optimize-reflective-memory.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Improve the use of your reflective memory usage by reducing the dynamic data size, creating channel mappings between targets, and using data channels selectively with non-VeriStand systems. Before you begin, add a reflective memory network. Launch your project in the VeriStand Editor. In the Project

### Optimizing Reflective Memory

Improve the use of your reflective memory usage by reducing the
 dynamic data size, creating channel mappings between targets, and using data channels
 selectively with non-VeriStand systems.

Before you begin, add a reflective memory
 network.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. To optimize your reflective memory performance, complete any of the following
 tasks. 
 Goal
Tasks
RationaleReduce the dynamic data size of the data sharing network to 0.
Click Data Sharing Network.
On the Data Sharing Network configuration page, enter
 the Dynamic Data Size as 0.
Dynamic Data Size specifies the number of channels in reflective memory to
 reserve for dynamically mapping channel data at run time. Reflective memory
 can negatively impact performance. Reducing the number of channels to 0 avoids
 decreasing performance. Note This is only recommended for systems that do not
 execute stimulus profiles or perform data logging that references channels
 across multiple targets.
Create channel mappings between targets in the system definition
 file.
Create channel mappings between targets.
Prevent reflective memory used by VeriStand from overlapping with any
 non-VeriStand traffic on the bus.Click Configure Mappings
[IMAGE alt='image' src='GUID-2940293A-A793-4E2E-8EF1-4E79BA3EB54C-a5.png'].
In the System Configuration Mappings dialog box,
 click the Network drop-down and select
 Reflective Memory Network .
Click OK.
Click Data Sharing Network»Reflective Memory Network.
On the Reflective Memory Network Configuration
 page, enter a Start Memory Address and
 Maximum End Address Block to limit the range of
 addresses the systems can use.
Rather than using data channels to read and write data between targets in a
 system definition, create channel mappings between targets. When you configure
 channel mappings, VeriStand uses optimized reflective memory.
When sending data from a VeriStand system to a non-VeriStand system,
 manually select channels to add to reflective memory and read those channels
 from the non-VeriStand system.
Click Controller»Hardware»Chassis»Data Sharing»Reflective Memory.
Click Export Channels.
In the Export Channels to Reflective Memory dialog
 box, select channels to export and click OK.
Click Data Sharing Network»Reflective Memory Network.
On the Reflective Memory Network Configuration page,
 click Export memory table to file.
VeriStand adds the channels you export to the direct memory access (DMA)
 block write for the target. This reduces CPU usage.
After selecting the channels to export, you must configure the non-VeriStand
 systems to read the memory addresses of the exported channels. The Export
 memory table to file option creates a text file that contains the memory
 addresses when you deploy the system definition file.
When a VeriStand system must read data from a non-VeriStand system, add
 data channels to only the targets that require the data.
Click Controller»Hardware»Chassis»Data Sharing»Reflective Memory.
Click Add Data Channel.
Data channels allow you to specify the reflective memory addresses a
 VeriStand target reads. However, you should only add data channels you intend
 to use. VeriStand reads the memory addresses one at a time. The more addresses
 VeriStand reads, the slower the performance.
4. Save the system definition file.

Parent topic:

Maximizing System Performance

Related tasks:

- Adding Reflective Memory Networks
- Mapping Channels and Aliases

<!--NI_TOPIC bundle=veristand path=overview-of-runtime-configurability.html language=enus -->
## TOPIC 00297: Overview of Runtime Configurability

- bundle_id: `veristand`
- source_path: `overview-of-runtime-configurability.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/overview-of-runtime-configurability.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Runtime-configurable channels allow end users to dynamically add, change, or remove channels during system operation. This flexibility enables efficient testing and configuration without requiring system redeployment. End users can treat the reserved channels as a configurable subset of signals. For

### Overview of Runtime Configurability

Runtime-configurable channels allow end users to dynamically add, change, or
 remove channels during system operation. This flexibility enables efficient testing and
 configuration without requiring system redeployment.

End users can treat the reserved channels as a configurable subset of signals. For each
 test scenario, you can unload the current configuration and replace it with a new one,
 enabling flexible and efficient signal management without redeploying the system
 definition.

This functionality is beneficial for custom device developers working with systems that
 have many variables and don't use all channels or signals simultaneously. Depending on
 the test case or scenario, only a subset of the total signals is active at any given
 time.

#### Terms for Custom Device Developers

Figure 29.

[IMAGE alt='Diagram showing the runtime configuration process flow, including the Veristand Gateway and ActionVIOnRecompile.' src='GUID-AE27B0AD-9726-4224-8CD4-20F97BD50F14-a5.png']

Runtime Configurable Section

ActionVIOnRecompile

Note

Figure 30.

[IMAGE alt='LabVIEW block diagram showing CD.Command.ApplyConfig connected to Send Device Message and Byte Array.' src='GUID-7C9F6EBE-B656-44DA-9FAC-EBFE15D880E7-a5.png']

Command Loop

Figure 31.

[IMAGE alt='A LabVIEW block diagram showing a command loop handling runtime configuration changes.' src='GUID-558D68BD-640B-4654-B920-57988CD54D62-a5.png']

#### Terms for End Users

Runtime Configuration Manager Interface

Runtime Configuration File

Parent topic:

Creating Custom Devices

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=parallel-mode-pcl-model-timing.html language=enus -->
## TOPIC 00298: Parallel Mode Primary Control Loop Timing in Models

- bundle_id: `veristand`
- source_path: `parallel-mode-pcl-model-timing.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/parallel-mode-pcl-model-timing.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Models that have a Primary Control Loop (PCL) set to parallel mode have a one-cycle delay between when a model executes and when the data it produces is available to the system. As seen in the following illustration, the PCL will not wait for models to finish executing before it executes other steps

### Parallel Mode Primary Control Loop Timing in
 Models

Models that have a Primary Control Loop (PCL) set to parallel mode have a one-cycle delay
 between when a model executes and when the data it produces is available to the system.

As seen in the following illustration, the PCL will not wait for models to finish
 executing before it executes other steps.

[IMAGE alt='image' src='GUID-A4C58E1F-BA38-4019-B06A-B692E4789EB7-a5.gif']

#### Model Execution Deadlines

In parallel mode, because the PCL does not
 wait for the models to finish executing before it executes other steps, models can
 continue executing even after the PCL starts its next iteration. During the next
 iteration, the model must finish executing before the PCL can read data from models.
 The following illustration shows how the VeriStand engine imposes this deadline in
 parallel mode.

[IMAGE alt='image' src='GUID-D5A6E129-CF2E-4759-8501-6F3ECC6653F6-a5.gif']

Note

#### Deadlines When Model Rate Differs from Target Rate

If you configure a
 model to run at a decimation of the PCL rate, the VeriStand engine enforces a
 deadline when the decimation specifies it to finish executing. For example, if the
 target rate for the PCL is 100 Hz and the decimation for a model is 2 (therefore, it
 runs at 50 Hz), the VeriStand Engine does not impose a deadline after the first 100
 Hz PCL iteration because, according to the decimation, the model is not scheduled to
 finish executing.

However, after the second 100 Hz PCL iteration, when the
 model stops executing, the VeriStand Engine imposes a deadline. This happens on a
 per-model basis. A different model in the system with a decimation of 1 has a
 deadline imposed at every 100 Hz PCL iteration.

Parent topic:

Primary Control Loop Step Execution in Models

Related concepts:

- Time Step Duration

<!--NI_TOPIC bundle=veristand path=part-1-opening-the-system-definition-file-and.html language=enus -->
## TOPIC 00299: Part 1: Opening the System Definition File and Finding the First DAQ Device

- bundle_id: `veristand`
- source_path: `part-1-opening-the-system-definition-file-and.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/part-1-opening-the-system-definition-file-and.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Opens an existing system definition file and locates the first DAQ device under the Chassis section. 18 Locating a Device LabVIEW diagram opening a system definition file and finding the first DAQ device under Chassis. Open an existing system definition .nivssdf file from disk by initializing a new

### Part 1: Opening the System Definition File
 and Finding the First DAQ Device

Opens an existing system definition file and locates the first DAQ device under the
 Chassis section.

Figure 18.

[IMAGE alt='LabVIEW diagram opening a system definition file and finding the first DAQ device under Chassis.' src='GUID-F00BF774-F49C-4C5D-AB1C-3AB977E4D493-a5.gif']

1. Open an existing system definition .nivssdf file from disk by
 initializing a new instance of the SystemDefinition class.
2. Find the first DAQ device under the Chassis section of the
 system definition file by obtaining the references to the following items in the
 system definition file, in descending order:
  1. The Targets section (obtained from the Root dottable
 property and GetTargets method)
  2. The DAQ section Note To obtain this
 reference without traversing the system definition, the example code
 uses the FindNodeByPath method and specifies the node path. However, the
 FindNodeByPath method returns a BaseNode reference, which the
 ToMoreSpecificClass function then typecasts to the DAQ class.
  3. The DAQ devices under the DAQ section (obtained from
 the GetDeviceList method)
  4. The first DAQ device in the array of references

Parent topic:

Modifying a DAQ Device in a System Definition File

Related concepts:

- Programming with the System Definition API in LabVIEW
- Modifying a DAQ Device in a System Definition File
- Part 2: Adding Analog Input and Output Channels to a DAQ Device

<!--NI_TOPIC bundle=veristand path=part-2-adding-analog-input-and-output-channel.html language=enus -->
## TOPIC 00300: Part 2: Adding Analog Input and Output Channels to a DAQ Device

- bundle_id: `veristand`
- source_path: `part-2-adding-analog-input-and-output-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/part-2-adding-analog-input-and-output-channel.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modify a DAQ device in a VeriStand system definition by adding analog input and analog output channels. Create aliases for new channels and add channel mappings between analog inputs and outputs. 19 Adding an Analog Input Channel to a DAQ Device LabVIEW diagram adding a DAQ analog input channel and

### Part 2: Adding Analog Input and Output Channels to a DAQ Device

Modify a DAQ device in a VeriStand system definition by adding analog input and
 analog output channels. Create aliases for new channels and add channel mappings between
 analog inputs and outputs.

Figure 19.

[IMAGE alt='LabVIEW diagram adding a DAQ analog input channel and creating an alias in the system definition.' src='GUID-FBF2A6EB-701D-46A8-AFAB-D73004FD874D-a5.gif']

1. Obtain the reference to the existing Analog Input section
 under the DAQ device in the system definition using the GetAnalogInputSection
 method.
2. Remove the existing Analog Input section from the system
 definition file using the RemoveNode property. Removing any existing analog input
 channels prevents conflicts between existing channels and channels you add.
3. Create a new Analog Input section and add it to the DAQ
 device using the CreateAnalogInputs method.
4. Add a new analog input channel by initializing a new instance of the DAQAnalogInput
 class.
5. Add the new analog input channel to the Analog Input section
 using the AddAnalogInput method.
6. Create an alias and link it to the new channel by:
  1. Obtaining the reference to the Aliases section using
 the Root dottable property and GetAliases method.
  2. Creating a new alias and adding it to the Aliases 
 section using the AddNewaliasByReference method.

Figure 20.

[IMAGE alt='LabVIEW diagram that creates a DAQ analog output channel and adds an alias linked to it.' src='GUID-450C5B00-E7C5-4265-A785-EC106BDB9DB2-a5.gif']

1. Obtain the reference to the existing Analog Output 
 section under the DAQ device in the system definition using the
 GetAnalogInputSection method.
2. Remove the existing Analog Output section from the system
 definition using the RemoveNode method. Removing any existing analog output
 channels prevents conflicts between existing channels and channels you add.
3. Create a new Analog Output section and add it to the DAQ
 device using the CreateAnalogOutputs method.
4. Create a new analog output channel by initializing a new instance of the
 DAQAnalogOutput class.
5. Add the new analog output channel to the Analog Output 
 section using the AddAnalogOutput method.
6. Create an alias and link it to the new channel by:
  1. Obtaining the reference to the Aliases section
 using the Root dottable property and GetAliases method.
  2. Creating a new alias and adding it to the Aliases 
 section using the AddNewaliasByReference method.

Figure 21.

[IMAGE alt='LabVIEW diagram showing DAQAnalogOutput and DAQAnalogInput node paths wired to AddChannelMappings.' src='GUID-F00D8173-614C-4440-8F15-7F1C6F326F52-a5.gif']

1. Get the node path for the AO0 channel.
2. Get the node path for the AI0 channel.
3. Convert the node paths from strings to arrays using Build Array functions. Note Note that the
 parameters of the AddChannelMappings function in the next step require
 arrays. This allows you to create multiple mappings simultaneously. For this
 example, you only need to create one mapping, so each array will only
 contain one element.
4. Map AI0 to AO0 . Note that the
 source channel, AI0 , maps to the destination channel,
 AO0 , but the destination channel stores the mapping
 information.

Parent topic:

Modifying a DAQ Device in a System Definition File

Related concepts:

- Programming with the System Definition API in LabVIEW
- Part 1: Opening the System Definition File and Finding the First DAQ Device
- Modifying a DAQ Device in a System Definition File
- Part 3: Adding Digital Input and Output Channels to a DAQ Device

<!--NI_TOPIC bundle=veristand path=part-3-adding-digital-input-and-output-channe.html language=enus -->
## TOPIC 00301: Part 3: Adding Digital Input and Output Channels to a DAQ Device

- bundle_id: `veristand`
- source_path: `part-3-adding-digital-input-and-output-channe.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/part-3-adding-digital-input-and-output-channe.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Add digital input and digital output channels to a DAQ device in a VeriStand system definition, including alias links and channel mappings. 22 Adding a Digital Input Channel to a DAQ Device LabVIEW block diagram showing how to add a digital input channel and create an alias link in VeriStand. Obtain

### Part 3: Adding Digital Input and Output Channels to a DAQ Device

Add digital input and digital output channels to a DAQ device in a VeriStand system
 definition, including alias links and channel mappings.

Figure 22.

[IMAGE alt='LabVIEW block diagram showing how to add a digital input channel and create an alias link in VeriStand.' src='GUID-2A44E290-341B-4FC2-BB5D-478B9698788F-a5.gif']

1. Obtain the reference to the existing Digital Input section
 under the DAQ device in the system definition using the GetDigitalInputSection
 method.
2. Remove the existing Digital Input section using the
 RemoveNode method. Removing any existing digital input channels prevents conflicts
 between existing channels and channels you add.
3. Create a new Digital Input section and add it to the DAQ
 device using the CreateDigitalInputs method.
4. Create a new DAQ DIO port by initializing a new instance of the DAQDIOPort
 class.
5. Create a new digital input channel by initializing a new instance of the
 DAQDigitalInput class.
6. Add the new digital input channel to the DAQ DIO port using the AddDigitalInput
 method.
7. Add the DAQ DIO port with the digital input channel to the Digital
 Input section using the AddDIOPort method.
8. Create an alias and link it to the new channel by:
  1. Obtaining the reference to the Aliases section using
 the Root dottable property and GetAliases method.
  2. Creating a new alias and adding it to the Aliases 
 section using the AddNewaliasByReference method.

Figure 23.

[IMAGE alt='LabVIEW block diagram creating a DAQ digital output and alias, and adding it to a DIO port.' src='GUID-79F48C04-98FE-4CC6-AD74-46E963D4E051-a5.gif']

1. Obtain the reference to the existing Digital Output 
 section under the DAQ device in the system definition using the
 GetDigitalOutputSection method.
2. Remove the existing Digital Output section from the
 system definition using the RemoveNode method. Removing any existing digital
 output channels prevents conflicts between existing channels and channels you
 add.
3. Create a new Digital Output section and add it to the DAQ
 device.
4. Create a new DAQ DIO port by initializing a new instance of the DAQDIOPort
 class.
5. Create a new digital output channel by initializing a new instance of the
 DAQDigitalOutput class.
6. Add the new digital output channel to the new DAQ DIO port using the
 AddDigitalOutput method.
7. Add the DAQ DIO port with the digital output channel to the new
 Digital Output section using the AddDIOPort
 method.
8. Create an alias and link it to the new channel by:
  1. Getting the reference to the Aliases section
 using the Root dottable property and GetAliases method.
  2. Creating a new alias and adding it to the Aliases 
 section using the AddNewaliasByReference method.

Figure 24.

[IMAGE alt='LabVIEW block diagram adding DAQ digital I/O channel mappings and saving the system definition.' src='GUID-CBCE819A-D96A-477B-B928-8DD26B2C05DA-a5.gif']

1. Get the node path for the DO0 channel.
2. Get the node path for the DI0 channel.
3. Convert the node paths from strings to arrays using Build Array functions.
4. Map DI0 to DO0 using the Root
 dottable property and AddChannelMappings method.
5. Save the system definition file.

Parent topic:

Modifying a DAQ Device in a System Definition File

Related concepts:

- Programming with the System Definition API in LabVIEW
- Part 2: Adding Analog Input and Output Channels to a DAQ Device
- Modifying a DAQ Device in a System Definition File
- Part 4: Removing Broken Aliases and Channel Mappings

<!--NI_TOPIC bundle=veristand path=part-4-removing-broken-aliases-and-channel-ma.html language=enus -->
## TOPIC 00302: Part 4: Removing Broken Aliases and Channel Mappings

- bundle_id: `veristand`
- source_path: `part-4-removing-broken-aliases-and-channel-ma.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/part-4-removing-broken-aliases-and-channel-ma.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Removes broken aliases and blank channel mappings in a VeriStand system definition file after DAQ channel changes.Aliases and channel mappings can break when you remove channels that aliases or channel mappings link to. 25 Removing Unmapped Aliases LabVIEW diagram looping through aliases and removin

### Part 4: Removing Broken Aliases and Channel Mappings

Removes broken aliases and blank channel mappings in a VeriStand system definition
 file after DAQ channel changes.

Aliases and channel mappings can break when you remove channels that aliases or channel mappings
 link to.

Figure 25.

[IMAGE alt='LabVIEW diagram looping through aliases and removing aliases with an empty linked channel name.' src='GUID-66720B19-D5D9-4403-BF13-123DBDFFF414-a5.gif']

1. Find the aliases under the Aliases section of the system
 definition file. To do so, obtain references to the following items, in descending
 order:
  1. The Aliases section (obtained from the Root dottable
 property and GetAliases method)
  2. The aliases in the Aliases section (obtained from the
 GetAliasesList method)
2. Find any aliases without a channel by:
  1. Getting the LinkedChannel property of each
 alias.
  2. Getting the Name property of each linked
 channel.
  3. Evaluating whether or not a name exists for the channel using the Empty
 String/Path? Function. If the Name property does not
 exist for the linked channel, the alias is not linked to a channel.
3. Remove any aliases without a channel using the RemoveNode method.

Figure 26.

[IMAGE alt='LabVIEW diagram that gets channel mappings, deletes empty mappings, and saves the system definition.' src='GUID-0AB562D5-AE80-4F17-B99A-B9E22E7FD676-a5.gif']

1. Obtain references to all of the channel mappings in the system definition.
2. Create an array of any broken channel mappings by:
  1. Checking the channelPathSources array for empty
 strings with the Empty String/Path? function. If no source channel exists,
 the mapping is broken.
  2. Adding any broken channel mappings to the array.
3. Delete channel mappings added to the array in the previous step.
4. Save the system definition file.

Parent topic:

Modifying a DAQ Device in a System Definition File

Related concepts:

- Programming with the System Definition API in LabVIEW
- Part 3: Adding Digital Input and Output Channels to a DAQ Device
- Modifying a DAQ Device in a System Definition File

<!--NI_TOPIC bundle=veristand path=pcl-execution.html language=enus -->
## TOPIC 00303: Primary Control Loop Execution Steps

- bundle_id: `veristand`
- source_path: `pcl-execution.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/pcl-execution.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Primary Control Loop (PCL) controls the timing of the VeriStand Engine by performing several execution steps. The PCL can run in Parallel mode or Low Latency mode. The difference between the modes is the timing of model-related steps: In Parallel mode, the PCL initiates execution of models and c

### Primary Control Loop Execution Steps

The Primary Control Loop (PCL) controls the timing of the VeriStand Engine by performing several execution steps.

The PCL can run in 
 Parallel mode or 
 Low Latency mode. The difference between the modes is the timing of model-related steps:

- In Parallel mode, the PCL initiates
 execution of models and continues to its next iteration without waiting for models
 to finish executing. This causes a one-cycle delay between when a model executes and
 when the data it produces is available to the system
- In Low Latency mode, the PCL waits for
 the Model Execution Loop(s) to finish writing data to models before it reads and
 publishes model values to the system. This occurs during every iteration of the
 system. When the model completes execution, the PCL provides data from the model to
 other loops during the same iteration that the model generated the data. Note NI recommends you select Low
 Latency mode only if you need to minimize the latency between your inputs, model
 execution, and outputs. Waiting for Model Execution Loops to read, execute, and
 write on each iteration can significantly slow the execution speed of the
 system.

You can use System Explorer to set the execution
 mode of the PCL.

Note

| Step | Parallel mode | Low latency mode |
| --- | --- | --- |
| 1 | Gets inputs from hardware devices in the system definition. Note If the system includes an inline hardware interface custom device, the PCL reads DAQ digital lines and counters after the Read Data from HW case of the custom device executes in step 3. |  |
| 2 | Reads asynchronous custom device FIFOs from the previous iteration. |  |
| 3 | Runs the Read Data from HW case of inline hardware interface custom devices. If you configured hardware scaling, VeriStand applies the scaling after acquiring all hardware inputs. |  |
| 4 | Reads previous iteration data from models in the system definition. Note This step executes on the second and subsequent iterations. | — |
| 5 | Reads data from the previous iteration of the Data Processing Loop. |  |
| 6 | Processes system mappings. Note VeriStand components (including custom devices) cannot read data from a previous step until the PCL processes system mappings, even if the previous step acquired the data the component needs. |  |
| 7 | Runs the Execute Model case of inline model interface custom devices. |  |
| 8 | Executes steps of running real-time sequences. Note VeriStand executes real-time sequences after input operations but before output operations and continues to run every step of the real-time sequence until the sequence is complete, reaches a Yield step, or completes an iteration of a loop with Auto Yield set to TRUE. If a sequence takes longer than the given time for an iteration of the PCL, the PCL runs late. To avoid errors, break up the timing of the steps by placing Yield steps throughout the sequence and enabling the Auto Yield property for any loops in the sequence. |  |
| 9 | Processes system mappings. |  |
| 10 | Writes data to models. |  |
| 11 | Initiates asynchronous execution of models. | Initiates execution of models and waits for them to complete execution. |
| 12 | — | Reads data from models. |
| 13 | — | Processes system mappings. |
| 14 | Writes data to the Data Processing Loop. |  |
| 15 | Writes output data to hardware devices. |  |
| 16 | Runs the Write Data to HW case of inline hardware interface custom devices. |  |
| 17 | Writes data to asynchronous custom device FIFOs. |  |

Parent topic:

VeriStand Engine

Related concepts:

- VeriStand Engine

Related tasks:

- Configuring the VeriStand Engine

<!--NI_TOPIC bundle=veristand path=pcl-execution_2.html language=enus -->
## TOPIC 00304: Primary Control Loop Execution Steps

- bundle_id: `veristand`
- source_path: `pcl-execution_2.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/pcl-execution_2.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Primary Control Loop (PCL) controls the timing of the VeriStand Engine by performing several execution steps. The PCL can run in Parallel mode or Low Latency mode. The difference between the modes is the timing of model-related steps: In Parallel mode, the PCL initiates execution of models and c

### Primary Control Loop Execution Steps

The Primary Control Loop (PCL) controls the timing of the VeriStand Engine by performing several execution steps.

The PCL can run in 
 Parallel mode or 
 Low Latency mode. The difference between the modes is the timing of model-related steps:

- In Parallel mode, the PCL initiates
 execution of models and continues to its next iteration without waiting for models
 to finish executing. This causes a one-cycle delay between when a model executes and
 when the data it produces is available to the system
- In Low Latency mode, the PCL waits for
 the Model Execution Loop(s) to finish writing data to models before it reads and
 publishes model values to the system. This occurs during every iteration of the
 system. When the model completes execution, the PCL provides data from the model to
 other loops during the same iteration that the model generated the data. Note NI recommends you select Low
 Latency mode only if you need to minimize the latency between your inputs, model
 execution, and outputs. Waiting for Model Execution Loops to read, execute, and
 write on each iteration can significantly slow the execution speed of the
 system.

You can use System Explorer to set the execution
 mode of the PCL.

Note

| Step | Parallel mode | Low latency mode |
| --- | --- | --- |
| 1 | Gets inputs from hardware devices in the system definition. Note If the system includes an inline hardware interface custom device, the PCL reads DAQ digital lines and counters after the Read Data from HW case of the custom device executes in step 3. |  |
| 2 | Reads asynchronous custom device FIFOs from the previous iteration. |  |
| 3 | Runs the Read Data from HW case of inline hardware interface custom devices. If you configured hardware scaling, VeriStand applies the scaling after acquiring all hardware inputs. |  |
| 4 | Reads previous iteration data from models in the system definition. Note This step executes on the second and subsequent iterations. | — |
| 5 | Reads data from the previous iteration of the Data Processing Loop. |  |
| 6 | Processes system mappings. Note VeriStand components (including custom devices) cannot read data from a previous step until the PCL processes system mappings, even if the previous step acquired the data the component needs. |  |
| 7 | Runs the Execute Model case of inline model interface custom devices. |  |
| 8 | Executes steps of running real-time sequences. Note VeriStand executes real-time sequences after input operations but before output operations and continues to run every step of the real-time sequence until the sequence is complete, reaches a Yield step, or completes an iteration of a loop with Auto Yield set to TRUE. If a sequence takes longer than the given time for an iteration of the PCL, the PCL runs late. To avoid errors, break up the timing of the steps by placing Yield steps throughout the sequence and enabling the Auto Yield property for any loops in the sequence. |  |
| 9 | Processes system mappings. |  |
| 10 | Writes data to models. |  |
| 11 | Initiates asynchronous execution of models. | Initiates execution of models and waits for them to complete execution. |
| 12 | — | Reads data from models. |
| 13 | — | Processes system mappings. |
| 14 | Writes data to the Data Processing Loop. |  |
| 15 | Writes output data to hardware devices. |  |
| 16 | Runs the Write Data to HW case of inline hardware interface custom devices. |  |
| 17 | Writes data to asynchronous custom device FIFOs. |  |

Parent topic:

VeriStand Engine

<!--NI_TOPIC bundle=veristand path=pcl-model-latency.html language=enus -->
## TOPIC 00305: Primary Control Loop Step Execution in Models

- bundle_id: `veristand`
- source_path: `pcl-model-latency.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/pcl-model-latency.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Primary Control Loop (PCL) executes steps in models differently if it is in parallel mode or in low latency mode. Setting the PCL execution mode to parallel or low latency affects the steps that the VeriStand engine takes each iteration. The following table displays the main differences. PCL ite

### Primary Control Loop Step Execution in
 Models

The Primary Control Loop (PCL) executes steps in models differently if it is in
 parallel mode or in low latency mode.

Setting the PCL
 execution mode to parallel or low latency affects the steps that the
 VeriStand engine takes each iteration. The following table displays the main
 differences.

| PCL iteration | Parallel mode steps | Low latency mode steps |
| --- | --- | --- |
| First | Writes values to model. Initiates execution of model. | Writes values to model. Waits for model to finish executing. Reads values from model. |
| Second and after | Reads values from previous execution of model. Writes values to model. Initiates execution of model. |  |

In addition, the PCL timing differs in models depending on if it is running in parallel mode
 or low latency
 mode.

Parent topic:

Adding and Configuring a Model

Related concepts:

- Primary Control Loop Execution Steps
- Parallel Mode Primary Control Loop Timing in Models
- Low Latency Primary Control Loop Timing in Models

Related tasks:

- Configuring the VeriStand Engine

<!--NI_TOPIC bundle=veristand path=play-commands.html language=enus -->
## TOPIC 00306: Playing Back Commands Sent to the Target

- bundle_id: `veristand`
- source_path: `play-commands.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/play-commands.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Review the commands VeriStand sent to the target by playing back a recorded macro file in Macro Player. You can configure the play mode to control timing behavior during playback. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard

### Playing Back Commands Sent to the
 Target

Review the commands VeriStand sent to the target by playing back a recorded macro
 file in Macro Player. You can configure the play mode to control timing behavior during
 playback.

Workspace

Tools

Note

Macro Player

Macro
 Player

1. In the Workspace, select Tools»Macro Recorder to launch the tool. 
 Note The name of this menu item
 might differ depending on how you named it in the Tools
 Properties dialog box.
2. In the Macro Recorder tool, click File»Open and navigate to the macro file you want to play back.
3. Select a Play Mode. 
 Play Mode
 DescriptionIgnore Timing
 Plays back as fast as possible.
 Use Timing
 Plays back at the speed you recorded.
4. Click Play. 
 The Workspace Macro list highlights each command as it
 is played back.
5. Click Stop to stop playback.

Parent topic:

Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=preparing-a-custom-device-to-use-runtime-configurable-channels.html language=enus -->
## TOPIC 00307: Preparing a Custom Device to Use Runtime-Configurable Channels

- bundle_id: `veristand`
- source_path: `preparing-a-custom-device-to-use-runtime-configurable-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/preparing-a-custom-device-to-use-runtime-configurable-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Plan, implement, and change a custom device to support runtime-configurable channels in VeriStand. Plan your custom device. Decide which parts of the configuration hierarchy you need to set up at runtime. Avoid populating these sections or channels during the initial custom device configuration in S

### Preparing a Custom Device to Use
 Runtime-Configurable Channels

Plan, implement, and change a custom device to support runtime-configurable
 channels in VeriStand.

1. Plan your custom device.
  1. Decide which parts of the configuration hierarchy you need to set up at
 runtime.
  2. Avoid populating these sections or channels during the initial custom
 device configuration in System Explorer. Insert a
 RuntimeConfigurableSection at the appropriate location. This section
 acts as a placeholder, allowing you to add and compile content after
 system deployment.
2. Complete the option that best suits your use case. 
 OptionActionCreate a new custom device in the custom device wizard.
 Enable Support Runtime Configuration in
 the Custom Device Wizard while creating the custom device.Figure 32.Custom Device Wizard
 
 [IMAGE alt='The Custom Device Wizard with the Support Runtime Configuration option selected.' src='GUID-917C7069-9BA0-48F5-A210-9FDAA1F9C87C-a5.png']
 Verify that the following components are automatically added to
 the project.ActionVIOnRecompile.vi
 Command loop
 Code to launch the command loop during the RT driver
 initialization.Figure 33.Automatically Generated Components
 
 [IMAGE alt='Project Explorer showing Runtime Configuration Support Example with highlighted Command Loop and ActionVIOnRecompile.vi components.' src='GUID-B1F0978D-F526-48B1-973A-AC37EFFA6868-a5.png']Modify an existing custom device
 Add the ActionVIOnRecompile.vi. The VI template is available in
 the Custom Device API.
 Add a command loop and launch it asynchronously during RT driver
 initialization. Refer to the *Custom Device Example*
 for a reference implementation.
3. Develop the RT Driver VI and Action VI. 
 
 Refer to the *Custom Device Example* for a reference
 implementation.
  1. Implement the ActionVIOnRecompile and register it with VeriStand. 
 This callback VI compiles the sections or channels added at runtime
 after system deployment and passes the compiled data to the RT Driver
 VI.
  2. In the RT Driver VI, implement logic to receive and process the
 compiled data during runtime. 
 Use a command loop to handle incoming information and update later
 iterations.
  3. In the RT Driver VI, ensure that VeriStand channel values update when
 you apply a new configuration. 
 This ensures that in the next iteration, the VeriStand Primary
 Control Loop doesn't overwrite the values associated with the
 earlier configuration.

Note

Parent topic:

Overview of Runtime Configurability

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=programming-with-the-system-definition-api-c.html language=enus -->
## TOPIC 00308: Programming with the System Definition API in C#

- bundle_id: `veristand`
- source_path: `programming-with-the-system-definition-api-c.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/programming-with-the-system-definition-api-c.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use C# with the NI VeriStand System Definition .NET API to programmatically create, open, and change system definition files. You can use C# to access the NI VeriStand System Definition .NET API and programmatically control operation of the System Explorer window.

### Programming with the System Definition API in
 C#

Use C# with the NI VeriStand System Definition .NET API to programmatically create,
 open, and change system definition files.

You can use C# to access the NI VeriStand System Definition .NET API and programmatically
 control operation of the System Explorer window.

- [Modifying a System Definition File](c-modifying-a-system-definition-f.html) Use the NI VeriStand System Definition .NET API in C# to edit a system definition file from disk. The example updates XNET CAN ports, databases, clusters, and incoming frames through System Explorer node classes.
- [Modifying Models in a System Definition File](c-modifying-models-in-a-system-de.html) Use the NI VeriStand System Definition .NET API in C# to add, configure, and remove models in a system definition file.
- [Modifying a DAQ Device in a System Definition File](c-modifying-a-daq-device-in-a-sys.html) Use the NI VeriStand System Definition .NET API in C# to configure DAQ devices in a system definition file. This example uses the System Definition API to programmatically configure a DAQ device in a system definition.

Parent topic:

C# Examples

<!--NI_TOPIC bundle=veristand path=programming-with-the-system-definition-api-in.html language=enus -->
## TOPIC 00309: Programming with the System Definition API in LabVIEW

- bundle_id: `veristand`
- source_path: `programming-with-the-system-definition-api-in.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/programming-with-the-system-definition-api-in.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use LabVIEW with the NI VeriStand System Definition .NET API to programmatically create, open, and change system definition files. You can use LabVIEW to access the NI VeriStand System Definition .NET API and programmatically control operation of the System Explorer window. Creating and communicat

### Programming with the System Definition API in LabVIEW

Use LabVIEW with the NI VeriStand System Definition .NET API to programmatically
 create, open, and change system definition files.

System Explorer

Note

You interface with the System Definition API in LabVIEW through the following block diagram nodes:

- Constructor Node—Initializes a new instance of a specific class, such as the CANPort class.
- Property Node—Get and set properties, such as the reference to the root item of the system definition.
- Invoke Node—Invoke methods, such as the AddCANPort method that adds an instance of the CANPort class to the CAN section of a system definition file.

The following block diagram shows an example of using these three nodes to initialize a new
 system definition file and return references to components. These components appear in
 the System Explorer configuration tree.

Figure 3.

[IMAGE alt='LabVIEW block diagram using constructor, property, and invoke nodes to initialize a system definition file.' src='GUID-18145AB7-CAEB-4203-9770-13AE482F11E8-a5.gif']

#### Walkthrough: Accessing a Specific Class in the
 System Definition API

Select .NET Constructor

Figure 4.

[IMAGE alt='Select .NET Constructor dialog box with SystemDefinition selected in the object list.' src='GUID-82643806-1301-4AD0-96B6-1ABDFEDEE5AC-a5.gif']

The Constructors list in this dialog box shows
 an overloaded SystemDefinition constructor. The first overload, with many
 parameters, creates a new system definition file. The second overload,
 SystemDefinition(String), opens an existing system definition file whose path you
 specify. Note that the arguments after the class name correspond to initialization
 parameters. Constructor Nodes allow you to specify these initialization parameters,
 as the following block diagram shows.

Figure 5.

[IMAGE alt='LabVIEW block diagram using a SystemDefinition constructor node with initialization inputs.' src='GUID-18145AB7-CAEB-4203-9770-13AE482F11E8-a5.gif']

After you create a new class instance, wire the Constructor Node reference output
 to a Property Node. Use the Property Node to get or set properties for that class
 instance, such as the root-level item shown in the example block diagram. Wiring a
 class reference to an Invoke Node allows you to invoke a method in the class, such
 as the GetTargets method of the Root class in the example.

The hierarchy of
 classes in the System Definition API corresponds to the hierarchy of nodes that can
 appear in a system definition file displayed in the System
 Explorer window. Notice that the hierarchy of classes in the
 previous block diagram reflects the hierarchy of nodes in the System
 Explorer window. XNETAPIExample is the root
 item that contains the Targets section, which in turn
 contains the target named Controller.

Figure 6.

[IMAGE alt='System Explorer tree showing XNETAPIExample, Targets, and Controller.' src='GUID-9725DF27-4168-422E-BAAA-F1AEF93172A6-a5.gif']

#### Shorthand Programming with Dottable
 Properties

Some classes contain dottable properties that concatenate with
 other properties or methods. Dottable properties work the same as cascading multiple
 Property Nodes together. For example, compare the following code examples that both
 invoke the GetTargets method to return a reference to the
 Targets section of a system definition file.

| Cascading Property and Invoke Nodes |  |
| --- | --- |
| Dottable property |  |

#### Shorthand Programming by Finding Nodes by Name or Path

Instead of
 traversing the hierarchy of System Definition API classes until you reach a specific
 section, you can use the following methods, to directly find and access a node. Many
 of the System Definition API classes inherit these methods.

- BaseNode.FindFirstChildWithName
- BaseNode.FindNodeByPath

These methods are useful for decreasing the code required to access deeply
 nested nodes in system definition files. For example, the following block diagram
 shows the use of the FindNodeByPath method to access the CAN
 section under the first target in a system definition file.

Figure 7.

[IMAGE alt='LabVIEW block diagram using FindNodeByPath to access the CAN section under the first target.' src='GUID-68CD5CB5-50FA-4415-B52B-1593EF93EA70-a5.gif']

In the previous block diagram, the FindNodeByPath method returns a BaseNode
 reference, which represents generic nodes in a system definition file. You must use
 the To More Specific Class function to typecast the reference to the appropriate
 class, which is CAN in this case.

Parent topic:

LabVIEW Examples

Related concepts:

- Modifying a System Definition File

<!--NI_TOPIC bundle=veristand path=project-components.html language=enus -->
## TOPIC 00310: Components of a VeriStand Project

- bundle_id: `veristand`
- source_path: `project-components.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/project-components.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A VeriStand project contains at least one project file (.nivsprj), one system definition file (.nivssdf), and one screen file (.nivsscr or .nivsscreen). These files are used to configure, deploy, and interact with your system. The following figure illustrates the locations of these files and major c

### Components of a VeriStand Project

A VeriStand project contains at least one project file (.nivsprj),
 one system definition file (.nivssdf), and one screen file
 (.nivsscr or .nivsscreen). These files are used to
 configure, deploy, and interact with your system.

The following figure illustrates the locations of these files and major components of an VeriStand project.

[IMAGE alt='image' src='GUID-0B740E4B-F000-4795-9908-A6BD45916DAC-a5.gif']

Note

Related concepts:

- Host Computer
- Deployment Target
- Development Computer

<!--NI_TOPIC bundle=veristand path=project-steps.html language=enus -->
## TOPIC 00311: Project Steps

- bundle_id: `veristand`
- source_path: `project-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/project-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Open, communicate with, or close a VeriStand project (.nivsprj) file. Palette object Description Open VeriStand Project Opens the VeriStand project (.nivsprj) file you specify. Close Active VeriStand Project Closes the active VeriStand project (.nivsprj) file. Control Active VeriStand Project Sends

### Project Steps

Open, communicate with, or close a VeriStand project (.nivsprj)
 file.

| Palette object | Description |
| --- | --- |
| Open VeriStand Project | Opens the VeriStand project (.nivsprj) file you specify. |
| Close Active VeriStand Project | Closes the active VeriStand project (.nivsprj) file. |
| Control Active VeriStand Project | Sends a command to the active VeriStand project (.nivsprj) file. The project must be open for it to receive commands. |

Parent topic:

VeriStand Control Steps

Related reference:

- Open VeriStand Project Step
- Close Active VeriStand Project
- Control Active VeriStand Project Step

<!--NI_TOPIC bundle=veristand path=read-write-variable-real-time-sequence.html language=enus -->
## TOPIC 00312: Variables for Reading and Writing Channels in a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `read-write-variable-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/read-write-variable-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use parameter and channel reference variables to read or write system definition channels. There are key differences between how parameters and channel references access channels. Use the following table to determine the best variable type to read or write channels in your real-time sequence. Variab

### Variables for Reading and Writing Channels in
 a Real-Time Sequence

Use parameter and channel reference variables to read or write system definition
 channels.

| Variable | Use case | Limitations |
| --- | --- | --- |
| Parameter | Use parameters to create real-time sequences that you can use across multiple system definition files. | Parameters are difficult to manage if a stimulus profile contains nested real-time sequences or real-time sequences that access many channels. |
| Channel Reference | Use channel references if you do not need to use a real-time sequence with multiple system definition files. In general, channel references are easier to manage than parameters. | Channel references bind a real-time sequence to a specific system definition file. |

To illustrate how channel references are easier to manager than parameters, consider a
 real-time sequence, SeqA, that calls another sequence, SeqB. The stimulus profile,
 MyProfile, manages both sequences. You need to read a channel, named MyChannel, from
 SeqB.

| Parameters | Channel Reference |  |  |
| --- | --- | --- | --- |
|  | Add a parameter and assign MyChannel to it. Add the parameter to the real-time sequence code. |  | Add a channel reference for MyChannel. Add the channel reference to the real-time sequence code to read or write the system definition channel. Note You do not need to configure the channel reference in SeqA or MyProfile. |
|  | Add a parameter and assign it to MyChannel. Call SeqB and declare the MyChannel parameter in the real-time sequence call. |  |  |
|  | Configure the parameter assignments so that the appropriate SeqA parameter is assigned to MyChannel. |  |  |

Parent topic:

Creating Real-Time Sequences

<!--NI_TOPIC bundle=veristand path=real-time-call-step.html language=enus -->
## TOPIC 00313: Real-Time Sequence Call Step

- bundle_id: `veristand`
- source_path: `real-time-call-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/real-time-call-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calls a real-time sequence, executes the sequence on the specified Target, and returns information about whether the sequence execution passes or fails. You can call a real-time sequence from any section of a stimulus profile (Setup, Main, or Clean Up) or from within a Real-Time Sequence Group. Prop

### Real-Time Sequence Call Step

Calls a real-time sequence, executes the sequence on the specified Target, and
 returns information about whether the sequence execution passes or fails.

You can call a real-time sequence from any section of a stimulus profile
 (Setup, Main, or Clean
 Up) or from within a Real-Time Sequence Group.

| Property/Section | Description |
| --- | --- |
| File Path | Specifies the path to the real-time sequence to execute. You can specify a real-time sequence file (.nivsseq) or a properly formatted CSV file. |
| Target Name | Specifies the name of the target on which the sequence executes. The target must be defined in the system definition file associated with the stimulus profile. |
| Timeout [ms] | Specifies the amount of time in milliseconds within which the real-time sequence must complete each timestep. A zero or negative value indicates an infinite timeout. If the sequence does not complete a timestep within the specified amount of time, the VeriStand Engine aborts sequence execution and returns an error. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Pass/Fail Evaluation | Includes properties you can use to configure pass/fail evaluation for the sequence: Type—Specifies the type of pass/fail evaluation to perform. This step evaluates the return variable for the real-time sequence to determine whether the sequence passes or fails. You can select from the following options: AlwaysPass—(Default) The evaluation always passes, regardless of the value of the return variable. Boolean—Evaluates a Boolean value for pass/fail status. True is pass, unless you invert the evaluation. NumericBoundsCheck—Evaluates an integer value relative to specified high and low boundaries. Parameters—Defines parameters for the pass/fail evaluation. The options that appear depend on the Type of evaluation you specify. AlwaysPass evaluations have no parameters to define, because they always pass. You can set the following parameters: Invert—[Type: Boolean] If TRUE, inverts a Boolean evaluation so that FALSE is pass and TRUE is fail. Type—[Type: NumericBoundsCheck] Specifies the type of bounds check: Inbounds—The evaluation passes if the value is within the specified bounds. OutOfBounds—The evaluation passes if the value is outside the specified bounds. High—[Type: NumericBoundsCheck] Specifies the high limit of the bounds. A value is within bounds if it is less than or equal to this value and greater than or equal to the Low value. Low—[Type: NumericBoundsCheck] Specifies the low limit of the bounds. |
| Group Number | Defines the group associated with this real-time sequence. Valid group numbers include 0 to 27. A group number of -1 does not refer to any group. |
| Parameters | Contains properties that define the parameter assignments for the real-time sequence. When you specify the File Path to the real-time sequence, this section updates to display all the parameters defined in the sequence. Parameter Assignment—Specifies the value to assign to a real-time sequence parameter. You can specify a constant value or a channel in the system definition file. Update Parameters—Refreshes the Parameter Assignments for the sequence call based on the current contents of the specified sequence. This ensures parameter assignments exist for all parameters and that the data types of all parameter assignments match the data type of the corresponding sequence. This also deletes any parameter assignments that have no corresponding entry in the sequence.Use this option if you make any changes to the real-time sequence after you configure the Real-Time Sequence Call step. |

Parent topic:

Real-Time Sequences Steps

<!--NI_TOPIC bundle=veristand path=real-time-group-step.html language=enus -->
## TOPIC 00314: Real-Time Sequence Group Step

- bundle_id: `veristand`
- source_path: `real-time-group-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/real-time-group-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Groups Real-Time Sequence Call steps so that each sequence within the group executes in parallel. This step does not complete until each real-time sequence in the group executes. Property/Section Description Sequence Group Name Specifies the name of the sequence group. Description Specifies a descri

### Real-Time Sequence Group Step

Groups Real-Time Sequence Call steps so that each sequence within the group executes in
 parallel.

This step does not complete until each real-time sequence in the group executes.

| Property/Section | Description |
| --- | --- |
| Sequence Group Name | Specifies the name of the sequence group. |
| Description | Specifies a description for the current item. This text appears in the Context Help when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Real-Time Sequences Steps

<!--NI_TOPIC bundle=veristand path=real-time-sequence-primitives.html language=enus -->
## TOPIC 00315: Real-Time Sequence Primitives

- bundle_id: `veristand`
- source_path: `real-time-sequence-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/real-time-sequence-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use real-time sequence primitives to define variables, create expressions, and add structures such as loops and conditional statements to your real-time sequence code. A primitive is a programming element you can use in a real-time sequence. Subpalette Description Advanced Primitives Configure advan

### Real-Time Sequence Primitives

Use real-time sequence primitives to define variables, create expressions, and add
 structures such as loops and conditional statements to your real-time sequence
 code.

A *primitive* is a programming element you can use in a real-time
 sequence.

| Subpalette | Description |
| --- | --- |
| Advanced Primitives | Configure advanced operations in the real-time sequence code. |
| Expressions Primitives | Assign values to and perform operations on variables in a real-time sequence. |
| Miscellaneous Primitives | Add cosmetic and informational elements to real-time sequence code. |
| Structures Primitives | Add programming structures, such as loops and conditional statements, to the real-time sequence code. |
| Variables Primitives | Create and configure variables that a real-time sequence can access and act on. |

Parent topic:

Creating Real-Time Sequences

Related reference:

- Advanced Primitives
- Expressions Primitives
- Miscellaneous Primitives
- Structures Primitives
- Variables Primitives

<!--NI_TOPIC bundle=veristand path=real-time-sequence-steps.html language=enus -->
## TOPIC 00316: Real-Time Sequences Steps

- bundle_id: `veristand`
- source_path: `real-time-sequence-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/real-time-sequence-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call real-time sequences from a stimulus profile. Palette Object Description Real-Time Sequence Call Calls a real-time sequence, executes the sequence on the specified Target, and returns information about whether the sequence execution passes or fails. Real-Time Sequence Group Groups Real-Time Sequ

### Real-Time Sequences Steps

Call real-time sequences from a stimulus profile.

| Palette Object | Description |
| --- | --- |
| Real-Time Sequence Call | Calls a real-time sequence, executes the sequence on the specified Target, and returns information about whether the sequence execution passes or fails. |
| Real-Time Sequence Group | Groups Real-Time Sequence Call steps so that each sequence within the group executes in parallel. |

Parent topic:

Stimulus Profile Steps

Related reference:

- Real-Time Sequence Call Step
- Real-Time Sequence Group Step

<!--NI_TOPIC bundle=veristand path=reconfiguring-runtime-configurable-channels-after-deployment.html language=enus -->
## TOPIC 00317: Reconfiguring Runtime-Configurable Channels After Deployment

- bundle_id: `veristand`
- source_path: `reconfiguring-runtime-configurable-channels-after-deployment.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/reconfiguring-runtime-configurable-channels-after-deployment.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Dynamically add, change, or remove channels during system operation using .NET or the VeriStand Editor. .NET Dynamically add, change, or remove channels during system operation using .NET. Before you deploy the system, write the sections, channels, and their corresponding aliases required for your t

### Reconfiguring Runtime-Configurable Channels
 After Deployment

Dynamically add, change, or remove channels during system operation using .NET or the
 VeriStand Editor.

Parent topic:

Overview of Runtime Configurability

#### .NET

Dynamically add, change, or remove channels during system operation using
 .NET.

1. Before you deploy the system, write the sections, channels, and their
 corresponding aliases required for your test into a runtime configuration file.
 Refer to *Runtime Configuration File* to learn about available .NET
 APIs. 
 Note NI recommends that custom device developers
 provide APIs to help generate content for runtime configuration
 files.
2. Deploy your system.
3. Attach your configuration to the appropriate RuntimeConfigurableSection with
 the IRuntimeConfigurationManager API. For a .NET example of how to apply,
 reapply, or remove a runtime configuration, refer to *Runtime Configuration
 Manager*. 
 You can access channels defined in the configuration file through RT
 Sequences and Set and Get APIs of IWorkspace2. You can also fault these channels
 using the IChannelFault interface.
4. To switch to a new set of channels for a different test scenario, call the
 IRuntimeConfigurationManager API again with a new configuration file.

Related information:

- Custom Device Example
- Runtime Configuration File
- Runtime Configuration Manager

#### VeriStand Editor

Dynamically add, change, or remove channels during system operation using the VeriStand
 Editor.

1. Before you deploy the system, write the sections, channels, and their
 corresponding aliases required for your test into a runtime configuration
 file. 
 Note NI recommends that custom device developers
 provide APIs to help generate content for runtime configuration
 files.
2. Deploy your system.
3. In the VeriStand Editor, click View»Runtime Configuration Manager.
4. In the Runtime Configuration Manager pane, select a configuration from the
 table.
5. Enter a Timeout value.
6. To apply a new configuration or replace an existing configuration, click
 Apply Runtime Configuration and select the
 appropriate runtime configuration file.
7. To remove a configuration, select the configuration in the Runtime
 Configuration Manager pane and click Remove Runtime
 Configuration.

Related concepts:

- Overview of Runtime Configurability

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=recording-commands.html language=enus -->
## TOPIC 00318: Recording Commands VeriStand Sends to the Target

- bundle_id: `veristand`
- source_path: `recording-commands.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/recording-commands.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Record and save the commands that VeriStand sends to a target as a macro file (.nivsmacro) for later playback. Before you begin, verify that you have the tool in your Workspace Tools menu. If you do not, refer to Adding a Standard or Custom Tools Menu Item. You can also use the Macro Recorder VIs to

### Recording Commands VeriStand Sends to the
 Target

Record and save the commands that VeriStand sends to a target as a macro file
 (.nivsmacro) for later playback.

Workspace

Tools

Note

Macro Recorder

Macro
 Recorder

1. In the Workspace, select Tools»Macro Recorder to launch the tool. 
 Note The name of this menu item
 might differ depending on how you named it in the Tools
 Properties dialog box.
2. In the Macro Recorder tool, click
 Record to begin recording.
3. Use controls on the Workspace to send commands to the
 target. 
 The Workspace Macro list displays each command you
 send.
4. Click Pause to pause recording. 
 Note The Macro Recorder does not record any commands you send while it is
 paused. You can click Resume to continue appending
 commands to the same macro recording.
5. Click Stop to finish recording.
6. Click File»Save As to save the macro file.

Macro Player

Macro Recorder

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Adding a Standard or Custom Tools Menu Item
- Playing Back Commands Sent to the Target

<!--NI_TOPIC bundle=veristand path=related-docs.html language=enus -->
## TOPIC 00319: Related Documentation

- bundle_id: `veristand`
- source_path: `related-docs.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/related-docs.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following documents for more help with VeriStand. Refer to ni.com/manuals for updated documentation resources. Document Description VeriStand Release Notes Provides system requirements, installation instructions, and important information about the version of VeriStand that you are installin

### Related Documentation

Use the following documents for more help with VeriStand. 
 Refer to 
 ni.com/manuals for updated documentation resources.

| Document | Description |
| --- | --- |
| VeriStand Release Notes | Provides system requirements, installation instructions, and important information about the version of VeriStand that you are installing. Access this file from ni.com. |
| VeriStand .NET API Help | Documents several of the .NET APIs included with VeriStand. Use these APIs to programmatically control various software operations from any .NET-compatible programming language or environment, including LabVIEW and TestStand. Access this file from the Windows Start menu. |
| LabVIEW Help | Provides information about LabVIEW palettes, menus, tools, VIs, and functions. It also includes step-by-step instructions for using LabVIEW features, and documentation on LabVIEW Real-Time Module and LabVIEW FPGA Module when you install those modules. |
| LabWindows/CVI Help | Provides information about LabWindows and CVI windows, functions, tools, and menus. |
| NI-DAQmx Help | Provides information on using NI-DAQmx to program your National Instruments device. |
| NI-XNET Hardware and Software Help | Describes how to install and configure the NI-XNET hardware and software. It also includes the NI-XNET LabVIEW and C API reference and summarizes the CAN, FlexRay, and LIN standards. |
| Hardware Documentation | Provides support for any hardware devices you want to use with a project. |
| MathWorks Simulink® software documentation. | Provides support for Simulink tasks such as system-level design, simulation, automatic code generation, and continuous test and verification of embedded systems. |
| MathWorks MATLAB® software documentation. | Provides support for MATLAB tasks such as signal processing, event-based modeling, and application deployment. |
| MathWorks Simulink Coder® software documentation. | Provides support generates and executes C and C++ code from Simulink models and MATLAB functions. |

Parent topic:

Debugging the System

Related information:

- VeriStand Release Notes

<!--NI_TOPIC bundle=veristand path=replay-frame-data-can.html language=enus -->
## TOPIC 00320: Replaying Logged NI-XNET CAN Frame Data

- bundle_id: `veristand`
- source_path: `replay-frame-data-can.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/replay-frame-data-can.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Replay logged NI-XNET CAN frame data from TDMS or NCL files with original timing, plus optional frame ID filtering. Before you begin, add a CAN port. You can replay the frames within the file in the same order and timing as they were initially received. You can also filter specific frames from the f

### Replaying Logged NI-XNET CAN Frame
 Data

Replay logged NI-XNET CAN frame data from TDMS or NCL files with original timing,
 plus optional frame ID filtering.

Before you begin, add a CAN port.

Note

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»NI-XNET»CAN in the configuration tree.
4. Click a port.
5. Click Outgoing»Data Replay.
6. Click Add a Replay File
[IMAGE alt='image' src='GUID-9D8E079C-4AC2-4E18-A5FE-D2A76DC6BABB-a5.gif'] to display the Select an XNET Data File dialog box.
7. Click the Path folder to select a log file that contains CAN
 data and click OK.
8. Under Data Replay, select the log file to display the File Replay
 Configuration page.
9. Under File Replay Settings, specify a trigger channel for triggering the replay of the
 file. 
 Note Replay starts as soon as the value of the trigger channel is not zero. You can
 select a channel that triggers multiple replays of the file.
10. (TDMS only) Specify the group name and channel name for the TDMS channel that contains
 the data to replay.
11. Specify the cache # of frames and loop rate (Hz).
12. Under file replay IDs, specify the replay behavior. 
 The default behavior is to replay the entire file. You can configure this behavior to
 include or exclude specific frame IDs. Note If you select Include Frame
 IDs, you cannot specify IDs of single-point frames that already appear as
 outgoing frames under the port. If you select one of the other behavior options, you
 cannot have any outgoing, single-point frames specified under the port. Specifying a
 single-point frame as both an output and a frame to replay causes a run-time
 error.
13. Save the system definition file.

Note

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Adding a CAN, FlexRay, or LIN Port
- Logging Incoming NI-XNET Frames

<!--NI_TOPIC bundle=veristand path=run-operations-command-line-interface.html language=enus -->
## TOPIC 00321: Running VeriStand Operations Using the Command Line

- bundle_id: `veristand`
- source_path: `run-operations-command-line-interface.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/run-operations-command-line-interface.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the command line to execute processes in VeriStand, such as deploying or closing a project. Commands can be used while VeriStand is open or closed. Open a command prompt. Change directories to the location of the VeriStand executable. Execute one of the following commands using the following syn

### Running VeriStand Operations Using the Command
 Line

Use the command line to execute processes in VeriStand, such as
 deploying or closing a project.

Commands can be used while VeriStand is open or closed.

1. Open a command prompt.
2. Change directories to the location of the VeriStand executable.
3. Execute one of the following commands using the following syntax:
 VeriStand.exe /<command>. 
 Note You can use a slash
 (/), a dash (-), or two
 dashes (--) before each command. Commands are not
 case sensitive. For example, /deploy and
 --DePloY are equivalent commands.
Command
DescriptioncloseAllFiles
 Closes all open files prompting if there are any unsaved changes. 
 
 closeFile <relative path to project file>
 Closes individual project files if they are open prompting if there are any unsaved changes.
 This command can be repeated multiple times to open multiple files.
 For example: */closeFile "logging.nivslspec" /closeFile "screen.nivsscr"* will close both files.
 
 closeProject
 Closes the current project prompting if there are any unsaved changes.
 
connect
Connects to a deployed system on the gateway. This
 command executes after commands for creating the project,
 opening the project, and modifying the system definition.
 This command is ignored if deploy is also
 specified. An error returns if a system is not deployed but
 a project is open.
disconnect
Disconnects from a deployed system on the
 gateway.
deploy
Deploys the system to the gateway and connects to it.
 This command executes after commands for creating the
 project, opening the project, and modifying the system
 definition.
editScreen
Turns operate mode off to unlock the screen for editing.
 This can be used to reverse the
 operateScreen or
 operateOnly commands while VeriStand is
 running.
 
 forceCloseAllFiles
 Closes all open files and discards unsaved changes. 
 
 forceCloseFile <relative path to project file>
 Closes individual project files if they are open and discards unsaved changes.
 This command can be repeated multiple times to open multiple files.
 For example: */forcecloseFile "logging.nivslspec" /forcecloseFile "screen.nivsscr"* will close both files.
 
 
 forceCloseProject
 Closes the current project and discards unsaved changes.
 
gateway
<IP address or
 hostname>
Specifies the given IP address or hostname as the gateway.
help
Opens the VeriStand manual to *Running VeriStand
 Operations Using the Command Line*.
 
 nivsprj
 <file path to .nivsprj
 file>
 Opens the specified project. If the project
 does not exist, VeriStand creates it using the default
 project template. If VeriStand has a different project open,
 a dialog box will ask you to save and close it.
 
 
noDeployKeys
Disables the keyboard shortcuts for deploy
 (F6) and undeploy
 (F7). This command does not
 disable the Operate menu or the
 deploy and undeploy
 commands.
 
 openDocument <relative path to project file>
 Operates similar to openFile normally. However, a legacy .nivsproj VeriStand project path works like openLegacyProject for backward compatibility. 
 
 openFile <relative path to project file>
 Opens individual project files.
 This command can be repeated multiple times to open multiple files (with the last file getting focus).
 For example: */openFile "logging.nivslspec" /openFile "screen.nivsscr"* will open both files and leave screen.nivsscr with focus. 
 
 openLegacyProject <file path to legacy .nivsproj file>
 Converts a legacy .nivsproj VeriStand project into a .nivsprj file and opens it.
 
 openProject<file path to .nivsprj file>
 Opens the specified project. If the project
 does not exist, VeriStand creates it using the default
 project template. If VeriStand has a different project open,
 a dialog box will ask you to save and close it.
 
 operateOnly
 Turns operate mode on to lock the screen.
 When operate mode is on, you cannot resize, move, or edit
 the controls in the screen document. This command disables
 the screen document unlock button.
 
operateScreen
Turns operate mode on to lock the screen.
 When operate mode is on, you cannot resize, move, or edit
 the controls in the screen document. This command disables
 the screen document unlock button.

sysDef
<file path to .nivssdf system definition
 file>
Loads the system definition into an open or specified
 project. If you create a new project with the
 nivsprj or openProject
 commands, the specified system definition is used instead of
 the default template. This command does not work if the
 gateway is currently connected or connecting. This command
 executes before the connect
 command.
undeploy
Removes deployed system from the gateway. This command
 works on connected and disconnected systems.

Parent topic:

Running Tests

Related concepts:

- Host Computer

Related reference:

- Keyboard Shortcuts

<!--NI_TOPIC bundle=veristand path=run-silent-veristand.html language=enus -->
## TOPIC 00322: Running the VeriStand Gateway Silently

- bundle_id: `veristand`
- source_path: `run-silent-veristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/run-silent-veristand.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Deploy a system definition without launching a VeriStand user interface, such as VeriStand Editor or System Explorer. By silently running the VeriStand Gateway, you can deploy a system definition, close the user interface, and then reconnect to the still-deployed project upon re-opening the user int

### Running the VeriStand Gateway Silently

Deploy a system definition without launching a VeriStand user interface, such as
 VeriStand Editor or System
 Explorer.

By silently running the VeriStand Gateway, you
 can deploy a system definition, close the user interface, and then reconnect to the
 still-deployed project upon re-opening the user interface. This allows you to leave
 the system definition deployed while being able to connect and disconnect testing
 user interfaces as needed.

VeriStand Editor

Legacy Project
 Functionality Disabled

- Workspace
- Workspace Tools dialog box
- Console Viewer
- XNET Bus Monitor
- Channel Calibration
- System Explorer Options dialog box

While the Gateway is running silently, you can check on the Gateway's status and use
 programmatic APIs.

1. Open a command prompt. 
 Note You can also use the
 Windows Run command or a language of your choice.
2. Execute one of the following commands using the following syntax:
 "<Base>\veristand-server.exe"
 <command>. 
 Command
Descriptionhelp
Displays command options.
start
Starts the server if it is not already running.
stop
Stops the server if it is running.
status
Displays the status of the server.
deploy
Deploys a system definition to the server.
undeploy
Undeploys a system definition from the server if not
 password-locked.

Parent topic:

Deploying the System Definition File to a Real-Time Target

Related concepts:

- Components of a VeriStand Project
- APIs in VeriStand

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=run-tests.html language=enus -->
## TOPIC 00323: Running Tests

- bundle_id: `veristand`
- source_path: `run-tests.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/run-tests.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Execute and automate tests.

### Running Tests

Execute and automate tests.

- [Deploying the System Definition File to a Real-Time Target](deploying-system-defintion-rt-target.html) Deploy the system definition file to the real-time (RT) target to run a project.
- [Running VeriStand Operations Using the Command Line](run-operations-command-line-interface.html) Use the command line to execute processes in VeriStand, such as deploying or closing a project.
- [VeriStand .NET Reference](veristand-net-reference.html) Use .NET APIs to programmatically control software operations.
- [Data Logging Options](data-logging-options.html) Log data with tools such as the Embedded Data Logger, Stimulus Profile Editor, and DAQ devices.
- [Using NI-XNET Interfaces](using-xnet-interfaces.html) Use NI-XNET interfaces to communicate and interact with applications that require real-time, high-speed manipulation of hundreds of Controller Area Network (CAN), Local Interconnect Network (LIN), and FlexRay frames and signals.
- [ASAM XIL API - Generic Simulator Interface](asam-xil-interface.html) VeriStand includes a Generic Simulator Interface for the Framework, MAPort and EESPort based on the 2.1 version of the ASAM XIL Standard
- [Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences](create-test-scenarios.html) Use the VeriStand Stimulus Profile Editor to create specific test scenarios for use in your real-time test applications.

<!--NI_TOPIC bundle=veristand path=running-command-line-script.html language=enus -->
## TOPIC 00324: Running a Command Line Script

- bundle_id: `veristand`
- source_path: `running-command-line-script.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/running-command-line-script.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Execute a command line script for each file the control generates during a log session to complete tasks such as passing log files to a batch file or to an executable, like Excel, for additional post-processing. Click Edit settings on the data logging control. Select Post-Processing. From the Action

### Running a Command Line Script

Execute a command line script for each file the control generates during a log session to
 complete tasks such as passing log files to a batch file or to an executable, like
 Excel, for additional post-processing.

1. Click Edit settings on the data logging
 control.
2. Select Post-Processing.
3. From the Action to take at end of log session dull-down menu,
 select Run Command Line Script.
4. Enter the command line script you want to run.

Parent topic:

Configuring and Executing Host-Side Logging

<!--NI_TOPIC bundle=veristand path=runtime-configurable-channel-limitations-and-considerations.html language=enus -->
## TOPIC 00325: Runtime-Configurable Channel Limitations and Considerations

- bundle_id: `veristand`
- source_path: `runtime-configurable-channel-limitations-and-considerations.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/runtime-configurable-channel-limitations-and-considerations.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following section describes key considerations and behaviors when working with runtime-configurable channels. Area Considerations System Definition Tree The system definition tree refreshes when you add or remove a runtime configuration. VeriStand Screen Users can configure the VeriStand screen

### Runtime-Configurable Channel Limitations
 and Considerations

The following section describes key considerations and behaviors when working with
 runtime-configurable channels.

| Area | Considerations |
| --- | --- |
| System Definition Tree | The system definition tree refreshes when you add or remove a runtime configuration. |
| VeriStand Screen | Users can configure the VeriStand screen with channels that end users can add or configure at runtime. A control, indicator, or chart mapped to an inactive runtime configuration won't update values until you apply the corresponding runtime configuration. A control, indicator, or chart stops updating if the mapped runtime configuration becomes unavailable when you remove or change the respective configuration. |
| Faulting | Users can fault runtime-configurable faultable channels using the IChannelFault API or in the Channel Fault Manager pane.Note Always clear any faults on runtime-configurable channels before reapplying the configuration on the same node. Otherwise, the faults may apply to the new configuration. |
| Real-Time Sequences | You can use runtime-configurable channels in real-time (RT) sequences. To run an RT sequence that references a runtime-configured channel, you must apply the corresponding configuration. Stop any RT sequence that interacts with a runtime-configured channel manually before removing or reapplying the respective runtime configuration. |
| Host Logging | Users can configure the logging specification with channels added at runtime. If host-side logging begins before applying the corresponding configuration, and the channel isn't available, the final log ignores the unavailable channels. If you remove or change the configuration while host logging is active and a channel under the active logging group becomes unavailable, the logging session will stop. |
| Mapping | You can't map channels added at runtime. Use RT sequences instead. |
| Calibration and Scaling | Calibration and scaling aren't supported for channels added at runtime. |
| Host-Target Disconnection | If the host disconnects from the target, you will lose any runtime configuration applied earlier. You must reapply the configuration to continue using channels added at runtime. |
| APIs for Runtime-Configurable Channels | IWorkspace2 APIs–Access channels added or modified at runtime. IChannelMonitor APIs–Register for runtime-configurable channel value changes. Sends notifications when the corresponding channel is active. IUDPChannelStreamSession APIs–UDP channel streaming supports channels added at runtime. If the streaming session starts before applying the corresponding configuration and the channel isn't available, the session will stream only the available channels. If you remove or change the configuration while a streaming session is active and a channel under the active streaming group becomes unavailable, the streaming session will stop. |
| Remote Gateway | You can apply/remove/reapply runtime configuration using remote gateway.Note The runtime configuration file must exist on both the host and the remote host, and its absolute path must be identical on both systems. |

Parent topic:

Overview of Runtime Configurability

Related information:

- Custom Device Example

<!--NI_TOPIC bundle=veristand path=scale-value-define-text.html language=enus -->
## TOPIC 00326: Defining Scale Values in a Text File

- bundle_id: `veristand`
- source_path: `scale-value-define-text.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/scale-value-define-text.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Format scale values in a text file to import to VeriStand. VeriStand converts non-numeric characters in the import file to 0. Create a text file. Depending on the type of scale you want to import, use the format example in your text file. Scale Type Format Example Lookup Table Either column can serv

### Defining Scale Values in a Text File

Format scale values in a text file to import to VeriStand.

VeriStand converts non-numeric characters in the import
 file to 0.

1. Create a text file.
2. Depending on the type of scale you want to import, use the format example in
 your text file. 
 Scale Type
Format ExampleLookup Table
Either column can serve as the pre-scaled values or the
 scaled values.
Value1 delimiter Value1
Value2 delimiter Value2
The file can contain more than two columns of values
Value1 delimiter Value2 delimiter Value3
Polynomial Coefficients
Order0Coefficient
Order1Coefficient
.
.
.
Order9Coefficient

After creating and formatting the text file,
 you can import
 it to VeriStand.

Parent topic:

Importing Scale Values from a Text File

Related tasks:

- Importing Scale Values from a Text File

<!--NI_TOPIC bundle=veristand path=scaling-channel-hardware-device.html language=enus -->
## TOPIC 00327: Scaling a Channel on Hardware Devices

- bundle_id: `veristand`
- source_path: `scaling-channel-hardware-device.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/scaling-channel-hardware-device.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create scales to convert hardware channel unit measurements to transducer/actuator scaled units. Before you begin, you might need to scale a channel when using a sensor that requires scaling from its voltage or current output into engineering units. Use your sensor's documentation for more informati

### Scaling a Channel on Hardware Devices

Create scales to convert hardware channel unit measurements to transducer/actuator scaled
 units.

Before you begin, you might need to
 scale a channel when using a sensor that requires scaling from its voltage or current
 output into engineering units. Use your sensor's documentation for more information on
 creating a scale.

For input channels, scales convert read
 samples from the hardware channel to scaled units. Scales on output channels convert
 written samples to pre-scaled units of the channel.

1. Depending on your goal, complete one of the following tasks. 
 Goal
TaskCreate
 a lookup table scale.
Map an array of pre-scaled
 values to an array of corresponding scaled
 values.
Create
 a polynomial scale.
Convert values using a
 polynomial equation with up to ten
 coefficients.
Create
 a thermocouple scale.
Convert values to Kelvins
 or degrees Celsius, Fahrenheit, or Rankine.
Import
 scales from another application.
Import a scale
 created by another system definition file
 (.nivssdf) or
 NI-DAQmx.
Import
 scale values from a text file.
Import scale table
 values or coefficients from a text file.
2. Map the
 scale to the channel.

Parent topic:

Tailoring Channels

Related tasks:

- Creating a Lookup Table Scale
- Creating a Polynomial Scale
- Creating a Thermocouple Scale
- Importing Scales from Another Application
- Importing Scale Values from a Text File
- Mapping Scales to Channels
- Importing and Exporting Scale Mappings

<!--NI_TOPIC bundle=veristand path=scope-global-parameters.html language=enus -->
## TOPIC 00328: Scoping Global Parameters

- bundle_id: `veristand`
- source_path: `scope-global-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/scope-global-parameters.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Change the scope of global parameters in a VeriStand model to target-level or model-level. Before you begin, identify your parameter’s type and scope. In VeriStand, parameters have two scopes. Target-level scope—VeriStand applies updates to all global parameter values with the same name in other mod

### Scoping Global Parameters

Change the scope of global parameters in a VeriStand model to target-level or
 model-level.

Before you begin, identify your parameter’s
 type and scope.

- Target-level scope—VeriStand applies updates to all global parameter values
 with the same name in other models that run on the same target.
- Model-level scope—VeriStand restricts the scope of updates to just the
 parameter in the owning model.

All global parameters in a particular model share the same scope.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Simulation Models»Models in the configuration tree.
4. Click a model.
5. Click Parameters.
6. On the Parameters Configuration page, use the Scope for Global
 Parameters drop-down to select Target or
 Model.
7. Save the system definition file.

Parent topic:

Adding and Configuring a Model

Related tasks:

- Identifying Local and Global Parameters

<!--NI_TOPIC bundle=veristand path=screens.html language=enus -->
## TOPIC 00329: Viewing, Creating, and Interacting with Screens

- bundle_id: `veristand`
- source_path: `screens.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/screens.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create screens and projects in the VeriStand Editor to view, create, and interact with user interfaces. The following image highlights the parts of the editor you use to open, access, and interact with screens and projects. 1 Project Files—Use this tab to open, create, and organize all the files wit

### Viewing, Creating, and Interacting with Screens

Create screens and projects in the VeriStand Editor to view,
 create, and interact with user interfaces.

The following image highlights the parts of the editor you use to open, access, and interact
 with screens and projects.

[IMAGE alt='image' src='GUID-F2BE5BE3-0BA1-4F3E-8487-0C55E3264771-a5.png']

| 1 | Project Files—Use this tab to open, create, and organize all the files within a project. |
| --- | --- |
| 2 | Tools Launcher—Use this tab to launch various tools for interacting with your project while it runs. |
| 3 | Document—After you open one or more screens, click one of these tabs to access the contents of a single screen. |
| 4 | Configuration pane—Use this pane to edit various aspects of your current project. |
| 5 | Palette—Organized hierarchy of all the controls and indicators you can add to the screen. By adding controls and indicators to the screen, you can modify the user interface an operator uses to interact with a project. |
| 6 | Screen—Use this area to view and modify the contents of a screen. |
| 7 | Tools pane—Use this pane to access various tools for interacting with your project while it runs. You can also use this pane to view errors and warnings that occur in your project. |

Parent topic:

Visualizing System State

<!--NI_TOPIC bundle=veristand path=select-hardware.html language=enus -->
## TOPIC 00330: Optimizing Hardware Performance

- bundle_id: `veristand`
- source_path: `select-hardware.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/select-hardware.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Increase the performance of your VeriStand system by using hardware timing, simultaneous sampling, USB CAN devices, PXIe devices, and not using Real-Time Hypervisor. Add a hardware device. To optimize your hardware performance, complete any of the following tasks. Task Rationale Use controllers that

### Optimizing Hardware Performance

Increase the performance of your VeriStand system by using hardware
 timing, simultaneous sampling, USB CAN devices, PXIe devices, and not using Real-Time
 Hypervisor.

1. Add a hardware
 device.
2. To optimize your hardware performance, complete any of the following tasks. 
 Task
RationaleUse controllers that support hardware timing.
Software timing slows the system significantly and adds to
 CPU usage. Using controllers that support hardware timing allows for better
 system performance.
Choose DAQ devices that use simultaneous sampling.
Simultaneous sampling provides better performance than
 multiplexed sampling.
Use a USB CAN device instead of XNET ports or channels for bus monitoring
 only.
Using a USB CAN device on the host computer reduces the
 number of channels in the system. The fewer channels VeriStand reads, the better
 the performance.
Use PXIe devices and controllers.
PXIe devices generally contain newer technology and run at
 faster rates than other devices.
Do not use NI Real-Time Hypervisor for systems that require high
 performance.
Real-Time Hypervisor comes with dramatic real-time
 performance penalties. Switching to a real-time only PXI controller can
 potentially double the performance.

Parent topic:

Maximizing System Performance

Related tasks:

- Adding and Configuring a Hardware Device

<!--NI_TOPIC bundle=veristand path=send-workspace-tool-message.html language=enus -->
## TOPIC 00331: Send Workspace Tool Message

- bundle_id: `veristand`
- source_path: `send-workspace-tool-message.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/send-workspace-tool-message.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a workspace tool VI, as well as data required by the case in the tool that handles the command. The tool at the VI Path you specify must be capable of receiving messages. Property/Section Description VI Path Specifies the path to the workspace tool VI. Description Speci

### Send Workspace Tool Message

Sends a message or command to a workspace tool VI, as well as data required by the case
 in the tool that handles the command.

VI
 Path

| Property/Section | Description |
| --- | --- |
| VI Path | Specifies the path to the workspace tool VI. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Message Details | Includes the following properties: Command—Specifies the message or command to send to the workspace tool. The tool VI must include code to handle the command you send. This property expects a string. Data—Specifies data to send to the workspace tool. This can be any data that the code that handles the Command accepts, but must be a string with a format that the tool can process. Timeout [ms]—Specifies the amount of time in milliseconds to wait for a response from the workspace tool before timing out. |

Parent topic:

Workspace Tools Steps

<!--NI_TOPIC bundle=veristand path=set-alarm-group.html language=enus -->
## TOPIC 00332: Assigning an Alarm Group

- bundle_id: `veristand`
- source_path: `set-alarm-group.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-alarm-group.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Assign an alarm group to execute one alarm procedure at a time. Alarm groups are used to determine the execution order of re-arm procedures. You can assign alarms to different groups. If a system definition file contains multiple alarm groups, one procedure per alarm group executes simultaneously. L

### Assigning an Alarm Group

Assign an alarm group to execute one alarm procedure at a time.

Alarm groups

1. Launch your project in the VeriStand Editor.
2. Click View»System Definition.
3. Right-click an alarm and select Properties.
4. In the Properties dialog box, set the Re-arm
 behavior to Procedure.
5. Enter a Group number. 
 Note One alarm group is automatically created for each alarm that uses
 procedural re-arm behavior. All alarms default to group 0.
6. Optional: 
 Enter a Priority number. 
 Note Procedures execute
 differently in a group based on the priority
 you set for each procedure.
7. Click OK.
8. Save the system definition file.

Parent topic:

Adding and Configuring Alarms

<!--NI_TOPIC bundle=veristand path=set-alarm-priority.html language=enus -->
## TOPIC 00333: Setting an Alarm Priority

- bundle_id: `veristand`
- source_path: `set-alarm-priority.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-alarm-priority.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Set an alarm priority to ensure high severity alarms execute immediately, interrupting other alarms that may be executing when multiple alarms are monitoring the same system. Launch your project in the VeriStand Editor. Click  View System Definition . Right-click an alarm and select Properties. In t

### Setting an Alarm Priority

Set an alarm priority to ensure high severity alarms execute immediately, interrupting
 other alarms that may be executing when multiple alarms are monitoring the same
 system.

1. Launch your project in the VeriStand Editor.
2. Click View»System Definition.
3. Right-click an alarm and select
 Properties.
4. In the Properties dialog box, set the
 Re-arm behavior to
 Procedure.
5. Enter a Priority number. 
 Note Zero
 (0) is the highest priority number. For more
 information on priority execution, refer to .
6. Click OK.
7. Save the system definition file.

Parent topic:

Adding and Configuring Alarms

Related concepts:

- Alarm Group Execution

<!--NI_TOPIC bundle=veristand path=set-chasis-master-hardware-sync.html language=enus -->
## TOPIC 00334: Setting Chassis Master Hardware Synchronization Devices

- bundle_id: `veristand`
- source_path: `set-chasis-master-hardware-sync.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-chasis-master-hardware-sync.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a chassis master hardware synchronization device to control timing and synchronization for all hardware in a chassis. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure in System Explorer. Choose to ad

### Setting Chassis Master Hardware
 Synchronization Devices

Configure a chassis master hardware synchronization device to control timing and
 synchronization for all hardware in a chassis.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Choose to add and configure one of the following hardware
 devices to the system definition. 
 Device TypeDevice ConfigurationNI-DAQ
The NI-DAQ device must have at least one
 analog input or output channel.NI FPGA
Any NI FPGA device.Timing and Sync
The timing and sync device must have the
 capability to drive the 0 line. Note The RTSI 0
 line is a digital line that sends a clock signal
 that synchronizes all hardware I/O devices in the
 system.
4. Click Targets»Controller»Hardware»Chassis in the configuration tree to open the
 Chassis Configuration
 page.
5. Click Chassis master hardware synchronization
 device to select the hardware
 device.
6. Save the system definition file.

Parent topic:

Adding and Configuring a Hardware Device

Related tasks:

- Adding and Configuring a DAQ Device
- Adding NI FPGA Targets
- Adding and Configuring Timing and Sync Devices

Related information:

- Using Synchronization to Build Integration Test Systems with
 VeriStand

<!--NI_TOPIC bundle=veristand path=set-default-inport-values.html language=enus -->
## TOPIC 00335: Setting Default Values for Inports

- bundle_id: `veristand`
- source_path: `set-default-inport-values.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-default-inport-values.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Set the default value for a model inport to avoid invalid operations during initialization. The default value of all inports is 0. Change the default if your model divides by an inport to avoid an invalid operation.Verify if your system configuration will cause the initial default value to go unused

### Setting Default Values for Inports

Set the default value for a model inport to avoid invalid operations during
 initialization.

Note

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Simulation Models»Models in the configuration tree.
4. Click a model.
5. Click Inports and click an inport.
6. On the Inport Configuration page, set the Default
 Value.
7. Save the system definition file.

Parent topic:

Adding and Configuring a Model

Related concepts:

- Primary Control Loop Step Execution in Models

<!--NI_TOPIC bundle=veristand path=set-model-parameter-value-workspace.html language=enus -->
## TOPIC 00336: Setting Model Parameter Values in the Workspace

- bundle_id: `veristand`
- source_path: `set-model-parameter-value-workspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-model-parameter-value-workspace.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Model calibration controls in the Workspace let you view and modify model parameter values in the system definition. Open the Workspace. Select Screen Edit Mode to display the Workspace Controls palette and alignment grid. Click the Workspace Controls palette. Select Model Calibration Control. Choos

### Setting Model Parameter Values in the
 Workspace

Model calibration controls in the Workspace let you view and modify model
 parameter values in the system definition.

1. Open the Workspace.
2. Select Screen»Edit Mode to display the Workspace Controls palette
 and alignment grid.
3. Click the Workspace Controls palette.
4. Select Model Calibration Control.
5. Choose one of the following control types and drag it onto the alignment
 grid. 
 Note Glyphs appear next to
 parameters to indicate whether their status is unlocked ([IMAGE alt='image' src='GUID-FA469965-3F55-49FA-8C80-99A37EB05295-a5.gif']) or locked ([IMAGE alt='image' src='GUID-22FEE575-08BA-44EB-8094-528949512B31-a5.gif']). The [IMAGE alt='image' src='GUID-8871C392-EA89-430C-9AE5-DCE552754D09-a5.gif'] glyph appears on a control
 to indicate when you have made changes to a parameter but not applied them
 to the system.
Control Type
Description
ExampleMedium Control
Medium controls are the basic numeric controls for
 modifying a single model parameter value.
VeriStand applies value changes as soon as you enter them
 in a medium control
[IMAGE alt='image' src='GUID-F7D091F1-BD2B-48CB-8291-E664776C9380-a5.gif']
Array Control
Array controls help manage the elements of parameters in
 vector form.
Click Apply to commit the
 changes. Click Reset to replace
 any value changes you have not applied with the current
 system values.
[IMAGE alt='image' src='GUID-4662CC2E-1862-4A4C-84B1-0776C522E75A-a5.gif']
List Control
List controls provide access to multiple parameters.
 Select the parameters in the Item
 Properties dialog box for list controls.
VeriStand applies value changes as soon as you enter
 them.
[IMAGE alt='image' src='GUID-64F360BF-BFA4-4831-8E9B-CA1F0814B075-a5.gif']
6. Use the Item Properties dialog box to customize the
 control and click OK.

You can also lock the parameter
 value.

Parent topic:

Running the VeriStand Workspace

Related tasks:

- Locking Model Parameters at Run Time

<!--NI_TOPIC bundle=veristand path=set-model-parameter.html language=enus -->
## TOPIC 00337: Setting Model Parameters

- bundle_id: `veristand`
- source_path: `set-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the VeriStand Editor, Workspace, Model Parameter Manager, and Stimulus Profile Editor to set the values of model parameters. Depending on your goal, complete the following task to set model parameters. Goal Task Change the initial value of model parameters Configure VeriStand to apply initial va

### Setting Model Parameters

Use the VeriStand Editor, Workspace,
 Model Parameter Manager, and Stimulus Profile
 Editor to set the values of model parameters.

Depending on your goal, complete the following task to set model
 parameters.

| Goal | Task |
| --- | --- |
| Change the initial value of model parameters | Configure VeriStand to apply initial values for model parameters from a .txt file when a system definition file deploys. |
| Manually set individual parameters at run time. | Use model calibration controls in the Workspace to view and modify the values for any model parameters in the system definition. |
| Lock model parameters at run time | Lock a parameter in the Workspace to prevent its value from updating. |
| Declare temporary variables in a model parameter file | Declare temporary variables within a .txt file and use those temporary variables as new parameter values or as parts of expressions that define new parameter values. |
| Call a subscript from a model parameter file | Call additional parameter files from within a .txt file to encapsulate certain elements of a test in separate files. |
| Alias parameter names in a model parameter file | Use an alias file to define syntactically correct aliases for model parameter names. |
| Import and manage batches of model parameters in the VeriStand Editor | Import model parameters with the Model Parameter Manager to apply values defined in an external .txt file to a model. |
| Import and manage batches of model parameters in the Workspace |  |
| Update model parameters during a stimulus profile test | Use the Update Model Parameters from File step in a stimulus profile to apply model parameter values defined in a text file to a simulation model that is deployed and running on a target. |

Parent topic:

Adding and Configuring a Model

Related tasks:

- Changing the Initial Value of Model Parameters
- Setting Model Parameter Values in the Workspace
- Locking Model Parameters at Run Time
- Declaring Temporary Variables in a Model Parameter File
- Calling a Subscript from a Model Parameter File
- Aliasing Parameter Names in a Model Parameter File
- Importing and Managing Batches of Model Parameters with the VeriStand Editor
- Importing and Managing Batches of Model Parameters in the Workspace
- Updating Model Parameters During a Stimulus Profile Test

<!--NI_TOPIC bundle=veristand path=set-model-timing.html language=enus -->
## TOPIC 00338: Setting Model Timing

- bundle_id: `veristand`
- source_path: `set-model-timing.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/set-model-timing.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Control the actual model rate of the VeriStand Engine by setting the Primary Control Loop rate and the model decimation. Before you begin, learn about the VeriStand system. A model is set to run at a rate as defined in the build options when the model is compiled. Depending on configuration settings

### Setting Model Timing

Control the actual model rate of the VeriStand Engine by setting the Primary Control
 Loop rate and the model decimation.

Before you begin, learn about the
 VeriStand system.

The following equation describes how the VeriStand Engine
 executes models:

actual model rate = Primary Control Loop (PCL) rate / model
 decimation

Modify the system definition to alter this equation.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Set the PCL rate.
  1. Click Targets»Controller in the configuration tree.
  2. Under Timing Source Settings, set a Target
 Rate.
4. Set the model decimation.
  1. Click Targets»Controller»Simulation Models»Models in the configuration tree.
  2. Click a model.
  3. Under Model Settings, enter a Decimation.
5. Save the system definition file.

If both the controller and plant are simulated, such as during a model-in-the-loop
 test, you can run your model at a different rate than specified when it was
 compiled. For example, you can set the Primary Control Loop of a model compiled to
 run at 100 Hz to 1 kHz, or 10 times faster than real time (assuming model decimation
 is 1).

This results in more simulations and more data in a shorter amount of time. However,
 a model that does not run in real time is potentially unstable. When testing with
 hardware, such as hardware-in-the-loop testing, run your model at the rate it was
 compiled to accurately simulate the system.

Parent topic:

Adding and Configuring a Model

Related concepts:

- VeriStand Engine

<!--NI_TOPIC bundle=veristand path=setting-parameter-manually.html language=enus -->
## TOPIC 00339: Setting a Parameter Value Manually

- bundle_id: `veristand`
- source_path: `setting-parameter-manually.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/setting-parameter-manually.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Model Parameter Manager tool to set a parameter value manually. If the Model Parameter Manager tool is not in the Tools menu, add it. To set the value of a parameter manually, you must set and then apply new values. Deploy the system definition with models to the target. You can only apply n

### Setting a Parameter Value Manually

Use the Model Parameter Manager tool to set a parameter value
 manually.

Model Parameter Manager

Tools

To set the value of a parameter manually,
 you must set and then apply new values.

1. Deploy the
 system definition with models to the target. 
 Note You can only apply new
 values to deployed systems.
2. In the Workspace, select Tools»Model Parameter Manager to launch the tool. 
 Note The name of this menu item might differ
 depending on how you named it in the Tools Properties
 dialog box.
3. Double-click a parameter to launch the Edit Calibration
 Value dialog box.
4. Enter the new value you want to apply to the parameter in the New
 Value table.
5. Click OK.
6. Click Copy System Values to copy over any new values you
 have not applied.
7. Click Apply New.

Parent topic:

Importing and Managing Batches of Model Parameters in the Workspace

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=setting-up-rt-target-virtual-ecus.html language=enus -->
## TOPIC 00340: Setting Up a Real-Time Target for Virtual ECUs

- bundle_id: `veristand`
- source_path: `setting-up-rt-target-virtual-ecus.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/setting-up-rt-target-virtual-ecus.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the necessary software and configure a real-time target to use virtual ECUs. The VeriStand Virtual ECU Toolkit supports virtual ECUs created using Synopsys^® software. To deploy a virtual ECU to a real-time target, you must copy the Synopsis license file generated for your HIL system target

### Setting Up a Real-Time Target for Virtual
 ECUs

Install the necessary software and configure a real-time target to use virtual
 ECUs.

®

After setting up a real-time target, add
 your virtual ECUs to your VeriStand project.

Parent topic:

Integrating Virtual ECUs

Related tasks:

- Adding and Configuring Virtual ECUs

Related information:

- Contact Synopsys

<!--NI_TOPIC bundle=veristand path=single-point-versus-waveform.html language=enus -->
## TOPIC 00341: Single-Point Versus Waveform Acquisition

- bundle_id: `veristand`
- source_path: `single-point-versus-waveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/single-point-versus-waveform.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify if an Analog Input (AI) channel performs single-point or waveform acquisitions when you add the channel to a system definition. In single-point acquisitions, channels acquire a single point at a time and return the value directly to the system. A single-point acquisition is an immediate, non

### Single-Point Versus Waveform
 Acquisition

Specify if an Analog Input (AI) channel performs single-point or waveform
 acquisitions when you add the channel to a system definition.

In *single-point* acquisitions, channels acquire a single point at a time and
 return the value directly to the system. A single-point acquisition is an immediate,
 non-buffered operation that occurs at the rate at which the system runs.

In *waveform* acquisitions, channels acquire signals over a period of time as
 waveforms.

The following table displays the use case for each acquisition type.

| Acquisition Type | Use Case |
| --- | --- |
| Single-Point | Useful for implementing closed-loop control, as the system reads one value per iteration of the Primary Control Loop and can produce appropriate outputs during the same iteration. |
| Waveform | Useful for reading data at a rate faster than the rate a system runs. For example, when you need to monitor or log a value that changes quickly, such as the pressure in an engine cylinder, acquiring the signal as a waveform allows you to achieve the high sampling rate required to represent the signal adequately. When you configure AI channels to perform waveform acquisitions, you can achieve rates up to the maximum sampling rate for the DAQ device without being restricted by the system rate. |

Parent topic:

Setting Up Timing and Logging Properties for Waveform Acquisitions

Related tasks:

- Setting Up Timing and Logging Properties for Waveform Acquisitions

<!--NI_TOPIC bundle=veristand path=slsc-system-real-time-scheme.html language=enus -->
## TOPIC 00342: SLSC Systems in Real-Time Schemes

- bundle_id: `veristand`
- source_path: `slsc-system-real-time-scheme.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/slsc-system-real-time-scheme.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A SLSC system is composed of chassis and module devices. A SLSC chassis interfaces with the network and provides multiple slots for SLSC modules. A SLSC module contains circuitry for switching, loads, and signal conditioning. The device under test and the measurement device send signals to the SLSC

### SLSC Systems in Real-Time Schemes

A SLSC system is composed of chassis and module devices.

A *SLSC chassis* interfaces with the network and provides multiple slots for
 SLSC modules. A *SLSC module* contains circuitry for switching, loads, and
 signal conditioning.

The device under test and the measurement device send signals to the SLSC system for
 signal conditioning. The SLSC system passes the signals on to the next stage in the
 real-time scheme. Signals can pass back and forth through this process from either the
 measurement device or the device under test. The direction of the signals depends on the
 set up of the real-time scheme.

| Device | Name Format |
| --- | --- |
| Chassis | SLSC-<chassis_model>-<chassis_serial_number> |
| Module | <chassis_name>-Mod<slot_number> |

Parent topic:

Adding and Configuring an SLSC device

<!--NI_TOPIC bundle=veristand path=specify-target.html language=enus -->
## TOPIC 00343: Specifying a Target

- bundle_id: `veristand`
- source_path: `specify-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/specify-target.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Select a target and designate its name, operating system, and IP address. Update the target specification when reusing a system definition with a new real-time target. Launch your project in the VeriStand Editor. In the Project Files pane, double click the system definition file (.nivssdf) to open t

### Specifying a Target

Select a target and designate its name, operating system, and IP address.

Update the target specification when reusing
 a system definition with a new real-time target.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, double click the system
 definition file (.nivssdf) to open the Mapping
 Diagram.
3. In the Select Target drop-down, select a target. 
 Note The Select
 Target drop-down only appears when you have more than one
 target in your system definition.
4. In the Configuration pane, click
 Document.
5. Enter the target's Name.
6. In the Operating System drop-down, select the target's operating system.
7. Enter the target's IP Address. 
 Note VeriStand does not support
 remote Windows targets. The IP address will remain
 localhost.

Parent topic:

Configuring a System Definition File

<!--NI_TOPIC bundle=veristand path=start-logging-step.html language=enus -->
## TOPIC 00344: Start Logging Step

- bundle_id: `veristand`
- source_path: `start-logging-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/start-logging-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts logging data from the system definition channels you specify to a TDMS file. When you add this step to a stimulus profile, VeriStand automatically creates a Channel Group step to associate with the logging configuration. You can add multiple channel groups under a single logging configuration

### Start Logging Step

Starts logging data from the system definition channels you specify to a TDMS
 file.

When you add this step to a stimulus profile, VeriStand automatically creates a
 Channel Group step to associate with the logging
 configuration. You can add multiple channel groups under a single logging
 configuration.

| Property/Section | Description |
| --- | --- |
| Configuration Name | Specifies the name of a specific data logging operation. You use this name to identify and control the operation. For example, to start and stop data logging, both the Start Logging step and the Stop Logging step must use the same Configuration Name. |
| File Path | Specifies the name and location of the log file to save data to. The Stimulus Profile Editor creates log files in the TDMS file format. You can enter an absolute or relative path. VeriStand treats relative paths as relative to the directory that contains the ATML results file for the stimulus profile. |
| Timestamp Filename | If True, specifies to append a timestamp to the data log filename that indicates when the file is created. |
| Replace Existing File | If True, specifies to overwrite an existing file at the location specified by File Path. If False, specifies to append data to the existing log file.If you choose to append data to an existing TDMS file, VeriStand logs new data for existing channels under the existing channel and group names, and the file only shows the initial creation date in the file header. The TDMS file does not retain the timestamps of subsequent logging operations that append data to an existing file. |
| Log Rate [Hz] | Specifies the rate in hertz at which to log data. VeriStand logs at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default is 100. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Triggered Logging | Includes properties you can use to configure a trigger that starts logging: Trigger Condition—Specifies the condition under which to register start and stop triggers: none—(Default) No trigger is specified. Logging starts when this step executes and continues until a stop logging command is received or the stimulus profile stops executing. in_limits—Registers a start trigger when the Trigger Channel value enters the bounds specified by High Limit and Low Limit and a stop trigger when the channel value leaves the bounds. out_of_limits—Registers a start trigger when the Trigger Channel value leaves the bounds specified by High Limit and Low Limit and a stop trigger when the channel value re-enters the bounds. Trigger Channel—Path to the channel, as specified in the system definition file, to watch for the specified Trigger Condition. High Limit—High limit for trigger limit analysis. Low Limit—Low limit for trigger limit analysis. Pre-Trigger Duration—The number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log. Post-Trigger Duration—The duration in seconds to continue logging data after a stop trigger occurs. |
| File Segmenting | Includes properties you can use to control if and when a log file is split into separate files: Segment Options—Specifies whether and how the log file is segmented: DoNotSegment—Does not segment the log file, regardless of how large it gets. OnStartTrigger—Starts a new log file each time a start trigger occurs. SizeLimit—Starts a new log file when the current file reaches a specified size. Segment Size—[Segment Options: SizeLimit] Specifies the maximum size of a log file segment, in bytes. |

Parent topic:

Logging Steps

<!--NI_TOPIC bundle=veristand path=stimulus-other-steps.html language=enus -->
## TOPIC 00345: Other Steps

- bundle_id: `veristand`
- source_path: `stimulus-other-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/stimulus-other-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add functionality to a stimulus profile. Examples include displaying a message to the user, replaying a previously recorded macro (.nivsmacro) file, or grouping steps to better organize and reuse code. Palette object Description Command Shell Invokes the Windows Command Prompt, calls the application

### Other Steps

Add functionality to a stimulus profile.

Examples include displaying a message to the user, replaying a previously recorded
 macro (.nivsmacro) file, or grouping steps to better organize and
 reuse code.

| Palette object | Description |
| --- | --- |
| Command Shell | Invokes the Windows Command Prompt, calls the application specified by Filename, and passes that application the specified arguments. |
| Group | Groups steps with no impact on execution. |
| Macro Player | Replays a previously recorded macro (.nivsmacro) file. |
| Message Box | Displays a pop-up message to the stimulus profile operator. |

| Subpalette | Description |
| --- | --- |
| FTP Steps | Interact with files on an FTP server, such as a real-time target. |

Parent topic:

Stimulus Profile Steps

Related reference:

- Command Shell Step
- Group
- Macro Player Step
- Message Box Step
- FTP Steps

<!--NI_TOPIC bundle=veristand path=stimulus-profile-steps.html language=enus -->
## TOPIC 00346: Stimulus Profile Steps

- bundle_id: `veristand`
- source_path: `stimulus-profile-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/stimulus-profile-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use steps to call real-time sequences, configure data logging operations, and interact with other elements of VeriStand, such as the project or Workspace. A step is an element of a stimulus profile that performs a specific action. Subpalette Description Real-Time Sequences Steps Call real-time seque

### Stimulus Profile Steps

Use steps to call real-time sequences, configure data logging operations, and interact
 with other elements of VeriStand, such as the project or
 Workspace.

A *step* is an element of a stimulus profile that performs a specific
 action.

| Subpalette | Description |
| --- | --- |
| Real-Time Sequences Steps | Call real-time sequences from a stimulus profile. |
| Logging Steps | Log data from channels in a system definition. |
| VeriStand Control Steps | Interact with VeriStand, including the Workspace and the VeriStand project. |
| Other Steps | Add functionality to a stimulus profile. |

Parent topic:

Creating Stimulus Profiles

Related reference:

- Real-Time Sequences Steps
- Logging Steps
- VeriStand Control Steps
- Other Steps

<!--NI_TOPIC bundle=veristand path=stop-logging-step.html language=enus -->
## TOPIC 00347: Stop Logging Step

- bundle_id: `veristand`
- source_path: `stop-logging-step.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/stop-logging-step.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops a currently running logging configuration. To stop logging, the Configuration Name must match the name you specified in the Start Logging step. Property/Section Description Configuration Name Specifies the name of a specific data logging operation. You use this name to identify and control the

### Stop Logging Step

Stops a currently running logging configuration.

To stop logging, the Configuration Name must match the name you specified in the Start Logging
 step.

| Property/Section | Description |
| --- | --- |
| Configuration Name | Specifies the name of a specific data logging operation. You use this name to identify and control the operation. For example, to start and stop data logging, both the Start Logging step and the Stop Logging step must use the same Configuration Name. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Logging Steps

<!--NI_TOPIC bundle=veristand path=stop-task.html language=enus -->
## TOPIC 00348: Stop Task

- bundle_id: `veristand`
- source_path: `stop-task.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/stop-task.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops a Task in a MultiTask structure. When a task stops, any subsequences executing in that task immediately execute their Clean Up block and any sub-tasks stop. Property/Section Description Task Name Specify the task name. Description Specifies a description for the current item. This text appears

### Stop Task

Stops a Task in a MultiTask structure.

When a task stops, any subsequences executing in that task immediately
 execute their Clean Up block and any sub-tasks stop.

| Property/Section | Description |
| --- | --- |
| Task Name | Specify the task name. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Multitasking Primitives

<!--NI_TOPIC bundle=veristand path=streamline-system-definition.html language=enus -->
## TOPIC 00349: Streamlining the System Definition

- bundle_id: `veristand`
- source_path: `streamline-system-definition.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/streamline-system-definition.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Decrease the complexity of your system definition by removing unused hardware I/O channels, maximizing the Convert Clock rate for multiplex sampling DAQ devices, and using hardware timing. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.n

### Streamlining the System Definition

Decrease the complexity of your system definition by removing unused
 hardware I/O channels, maximizing the Convert Clock rate for multiplex sampling DAQ devices,
 and using hardware timing.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Depending on your goal, complete any of the following tasks. 
 Goal
 Tasks
 RationaleRemove all unused hardware I/O channels.
 Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
 Select a DAQ device and delete any unused hardware I/O channels.
 Unused hardware resources slow performance. VeriStand must
 read and write every I/O channel in the system definition regardless of whether
 or not the system uses the channel data.
 Maximize the rate of the Convert Clock on DAQ devices that use multiplexed
 sampling.
 Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
 Click a DAQ device and, in the Conversion rate drop-down, select
 Maximum.
 Multiplexing can cause delays if the Convert Clock does not run fast enough.
 Changing the rate of the Convert Clock to maximum minimizes the delay.
 Relevant DAQ devices include the M Series, E Series, and some X Series.Note Using the maximum possible
 Convert Clock rate also reduces the accuracy of measurements.
 Use hardware timing instead of software timing.
 Click Targets»Controller in the configuration tree.
 In the Primary Control Loop timing source drop-down, select
 Automatic.
 Click Hardware»Chassis in the configuration tree.
 In the Chassis master hardware synchronization device drop-down, select
 DAQ or FPGA.
 With hardware timing, a digital signal, such as a clock on your device,
 controls the rate at which signals are generated.
 With software timing, the software and operating system controls the rate
 instead of the measurement device. A hardware clock can run faster—and is more
 accurate—than a software loop.
4. Save the system definition file.

Parent topic:

Maximizing System Performance

Related tasks:

- Synchronizing Hardware and Software

<!--NI_TOPIC bundle=veristand path=structures-primitives.html language=enus -->
## TOPIC 00350: Structures Primitives

- bundle_id: `veristand`
- source_path: `structures-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/structures-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add programming structures, such as loops and conditional statements, to the real-time sequence code. Subpalette Description Conditional Statements Use the Conditional statements to execute different code under different, specified conditions. Loops Use Loops to add structures that repeat a section

### Structures Primitives

Add programming structures, such as loops and conditional statements, to the
 real-time sequence code.

| Subpalette | Description |
| --- | --- |
| Conditional Statements | Use the Conditional statements to execute different code under different, specified conditions. |
| Loops | Use Loops to add structures that repeat a section of real-time sequence code a specified number of times or while a specified condition is TRUE. |
| Multitasking Primitives | Use the Multitasking primitives to divide real-time sequence code into multiple tasks that execute in parallel. |

Parent topic:

Real-Time Sequence Primitives

Related reference:

- Conditional Statements
- Loops
- Multitasking Primitives

<!--NI_TOPIC bundle=veristand path=switch-statement-primitives.html language=enus -->
## TOPIC 00351: Switch Statement Primitives

- bundle_id: `veristand`
- source_path: `switch-statement-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/switch-statement-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Switch Statement primitives to create different cases of code to execute based on the value of a test expression. Palette object Description Case Statement A functional statement under which you add code that executes if a test condition is met. Switch A statement that defines an expression

### Switch Statement Primitives

Use the Switch Statement primitives to create different cases of code to execute
 based on the value of a test expression.

| Palette object | Description |
| --- | --- |
| Case Statement | A functional statement under which you add code that executes if a test condition is met. |
| Switch | A statement that defines an expression to evaluate to determine which section of code, or Case Statement, to execute. |

Parent topic:

Conditional Statements

Related reference:

- Case Statement
- Switch Primitive

<!--NI_TOPIC bundle=veristand path=switch.html language=enus -->
## TOPIC 00352: Switch Primitive

- bundle_id: `veristand`
- source_path: `switch.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/switch.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A statement that defines an expression to evaluate to determine which section of code, or Case Statement, to execute. The Switch statement executes the case with the Case Value that matches the value of the Test Expression. If no cases match the test value, a default case executes instead. When you

### Switch Primitive

A statement that defines an expression to evaluate to determine which section of code,
 or Case Statement, to execute.

The Switch statement executes the case with the Case
 Value that matches the value of the Test
 Expression. If no cases match the test value, a default case
 executes instead. When you add a Switch to your real-time sequence code, the editor
 automatically creates a Cases section for the test cases and a DefaultCase, which is
 another Case Statement.

Build your test code by adding additional cases to the Cases section. You can then
 add code to define the execution of each case, including the default.

| Property/Section | Description |
| --- | --- |
| Test Expression | Specifies the expression to evaluate to determine the code to execute. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Switch Statement Primitives

<!--NI_TOPIC bundle=veristand path=sychronize-hardware-sorftware.html language=enus -->
## TOPIC 00353: Synchronizing Hardware and Software

- bundle_id: `veristand`
- source_path: `sychronize-hardware-sorftware.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/sychronize-hardware-sorftware.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Synchronize NI VeriStand hardware and software timing to support consistent performance, accurate data analysis, and reliable time correlation across devices. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and select Configure i

### Synchronizing Hardware and Software

Synchronize NI VeriStand hardware and software timing to support consistent
 performance, accurate data analysis, and reliable time correlation across
 devices.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Depending on your goal, complete any of the following tasks. 
 Goal
 TasksConfigure timing of the system
 Click Targets»Controller.
 Under Timing Source Settings, in the Primary Control
 Loop timing source drop-down, select the device that
 will time the system by sending ticks to the Primary
 Control Loop of the VeriStand Engine to start loop
 iterations.
 Enter a Target Rate and a
 Timing Source Timeout.
 Synchronize hardware-timed single-point devices in a
 single chassis.
 Click Targets»Controller»Hardware»Chassis.
 In the Chassis master hardware synchronization
 device drop-down, select the device that will
 synchronize signal-based hardware devices in the
 chassis by distributing a Sample Clock to them.Note You
 must configure this for each chassis in your
 system definition. Additionally, you can only
 synchronize hardware in a PXI chassis, and all
 devices must be connected to the PXI backplane
 because the Sample Clock is routed from the
 chassis master using PXI_Trig0.
 Configure the device.
 Synchronize hardware-timed single-point devices in a
 multiple chassis.
 Share the chassis Reference Clocks between chassis
 with the 10 MHz REF IN and OUT BNC connectors on the
 backplanes of the PXI chassis.
 Click Targets»Controller»Hardware»Chassis
 Configure a chassis to export a start trigger. In the Chassis master hardware synchronization
 device drop-down, select the device that will
 synchronize signal-based hardware devices in the
 chassis by distributing a Sample Clock to
 them.
 In the Export start trigger on line drop-down,
 select which line the chassis will export a start
 trigger.
 Configure a chassis to import the start trigger. In the Chassis master hardware synchronization
 device drop-down, select the device that will
 synchronize signal-based hardware devices in the
 chassis by distributing a Sample Clock to
 them.
 In the Trigger line drop-down, select which
 line the chassis will import the start
 trigger.
 Synchronize complex systems
 Synchronizing more complex systems may require additional
 system and software configuration and additional
 hardware.
 For detailed help on synchronizing complex systems, see
 the white paper on Building Synchronized VeriStand
 Systems.
4. Save the system definition file.

Parent topic:

Adding and Configuring a Hardware Device

Related concepts:

- Hardware Synchronization Types

Related information:

- Building Synchronized VeriStand Systems

<!--NI_TOPIC bundle=veristand path=system-channels.html language=enus -->
## TOPIC 00354: System Channels

- bundle_id: `veristand`
- source_path: `system-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/system-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use system channels to monitor system parts, such as the host computer, the target, and the VeriStand Engine, while it is deployed and running. You can access the system channels in System Explorer by clicking Targets Controller System Channels . Use the following table for more information on each

### System Channels

Use system channels to monitor system parts, such as the host computer, the target, and
 the VeriStand Engine, while it is deployed and running.

You can access the system channels in System Explorer by
 clicking Targets»Controller»System Channels.

| Channel name | Units | Description |
| --- | --- | --- |
| Absolute Time | sec | The current date and time relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. VeriStand coerces this value from a 128-bit value to double precision. This change might impact resolution. |
| Actual Loop Rate | Hz | The execution rate of the Primary Control Loop. |
| Alarm Status | Enum | The alarm's current state. 0: Disabled 1: Enabled 2: Tripped 3: Delayed Trip 4: Indicate |
| Analysis State | N/A | The state of the analysis sub-system on the real-time target. |
| Command Rate | N/A | The decimation of the Data Processing Loop. |
| DAQ Error | N/A | The last reported error code from a DAQmx function call. The value zero indicates no error. |
| Delta T | sec | The period of the Primary Control Loop. |
| Detailed Tracing Flag | N/A | The Boolean value that specifies whether detailed execution tracing is enabled on the real-time target. |
| Failure Count | N/A | The failure count of current analysis settings. |
| Host IP | N/A | The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine. Note The channel value does not reset to zero when an unexpected disconnection occurs, such as a power loss or network outage. |
| HP Count | N/A | The number of times the Primary Control Loop reported being late. |
| HP Loop Duration | ns | The duration of the Primary Control Loop. |
| HP Loop Wakeup Status | Enum | The wakeup status of the Primary Control Loop. 0: Normal 1: Aborted 2: Asynchronous wakeup 3: Timing source error 4: Timed loop error 5: Timeout |
| HP-LP Overwrite | N/A | The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop. |
| HS TCP Overflow Count | N/A | The number of times the streaming data gets overwritten. |
| Iteration | N/A | The iteration count of the Primary Control Loop. |
| Last Late Iteration | N/A | The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1. |
| Log Status | N/A | The state of the logging sub-system on the real-time target. |
| LP Count | N/A | The number of times the Data Processing Loop reported being late. |
| LP Data Count | N/A | The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop. |
| LP Loop Duration | ns | The duration of the Data Processing Loop. |
| Max Streamed Channels | N/A | The maximum number of channels that the VeriStand Engine can stream to the host. |
| Model Count | N/A | The number of times the models have not completed their execution in time. |
| Real-Time (RT) Sequence Command | Enum | The command that specifies how to halt execution of real-time sequences: 0: None 1: Stop All—Stops real-time sequences and skips to their clean-up sections. 2: Abort All—Terminates sequence execution without performing any clean-up tasks. |
| RT Sequence Count | N/A | The number of real-time sequences currently running. |
| RT Engine Build | N/A | A value representing the build number of the VeriStand Engine. |
| Streamed Channel Count | N/A | The number of channels that the VeriStand Engine is currently streaming to the host. |
| Streamed Waveform Count | N/A | The number of waveforms that the VeriStand Engine is currently streaming to the host. |
| System Command | Enum | The command that internally directs the real-time system with the following numeric values: 0: None 1: Restart System—Restarts current system definition. 2: Reset System—Resets system and leaves RT target waiting for a system definition to be deployed. 3: Shut Down System—Stops VeriStand engine. 4: Reboot System—Reboots RT controller. |
| System Reserved X | N/A | These channels are reserved for use by VeriStand. |
| System Time | sec | The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop. |
| TCP Data Packet Loss | N/A | The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a workspace connects to the VeriStand Engine. |
| Thread Tracing Flag | N/A | The Boolean value that specifies whether thread execution tracing is enabled on the real-time Target. |
| Trace Buffer Size | N/A | The size in bytes of the execution trace buffer on the RT target. |
| Trace Enabled Flag | N/A | The Boolean value that specifies whether execution tracing is currently active on the real-time target. Set to 1 to start tracing. Set to 0 to stop tracing and write result to disk. Set to -1 to stop tracing and send the result to the host. If no host is present, it is logged to disk. |
| VI Tracing Flag | N/A | The Boolean value that specifies whether VI execution tracing is enabled on the real-time Target. |
| Watchdog Timer | ns | The amount of time since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz. |
| WPL Error Code | N/A | The last error code encountered by the Waveform Processing Loop. |
| WPL Error Count | N/A | The number of times the Waveform Processing Loop encountered an error. |
| WPL Overflow Count | N/A | The number of times the Waveform Processing Loop attempts to write to a waveform read session within the VeriStand Engine and times out. |
| WPL TCP Overflow Count | N/A | The number of times the Waveform Processing Loop attempts to write to the TCP loop for a host waveform-stream session and times out. |

Parent topic:

Tailoring Channels

<!--NI_TOPIC bundle=veristand path=tailor-channels.html language=enus -->
## TOPIC 00355: Tailoring Channels

- bundle_id: `veristand`
- source_path: `tailor-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tailor-channels.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Manage channels for scaling, faulting, and more.

### Tailoring Channels

Manage channels for scaling, faulting, and more.

- [System Channels](system-channels.html) Use system channels to monitor system parts, such as the host computer, the target, and the VeriStand Engine, while it is deployed and running.
- [Scaling a Channel on Hardware Devices](scaling-channel-hardware-device.html) Create scales to convert hardware channel unit measurements to transducer/actuator scaled units.
- [Faulting a Channel to a Specific Value](veristand-editor-channel-faulting.html) Fault a channel with the **Channel Fault Manager** to test the behavior of a system when a channel reaches a specific value.
- [Adding a User Channel](add-user-channel.html) Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations.
- [Creating an Alias](create-alias.html) Set an alternate name for channels in a system definition file.
- [Mapping Channels and Aliases](map-channel-alias.html) Connect channels or aliases to one another.
- [Adding a Calculated Channel](add-calculated-channel-mapping-diagram.html) Store a single value as a user channel to use as a variable in procedures, stimulus profiles, and other operations.

<!--NI_TOPIC bundle=veristand path=task.html language=enus -->
## TOPIC 00356: Task

- bundle_id: `veristand`
- source_path: `task.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/task.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A block of code in a MultiTask structure. On each time step, the MultiTask structure iteratively executes code from each child Task that it contains. A Task cannot exist outside of a MultiTask structure. Configure the code that executes as part of the task by dragging expressions and other primitive

### Task

A block of code in a MultiTask structure.

On each time step, the MultiTask structure iteratively executes code
 from each child Task that it contains. A Task cannot exist outside of a MultiTask
 structure. Configure the code that executes as part of the task by dragging
 expressions and other primitives to the task and configuring them as you would any
 other section of sequence code.

| Property/Section | Description |
| --- | --- |
| Task Name | Specify the task name. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Multitasking Primitives

<!--NI_TOPIC bundle=veristand path=time-log-waveform-daq.html language=enus -->
## TOPIC 00357: Setting Up Timing and Logging Properties for Waveform Acquisitions

- bundle_id: `veristand`
- source_path: `time-log-waveform-daq.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/time-log-waveform-daq.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use tasks to define properties for when a system starts and stops acquisitions and how to perform data logging. Before you begin, add a DAQ device to the system definition. Launch your project in the VeriStand Editor. In the Project Files pane, left-click a system definition file (.nivssdf) and sele

### Setting Up Timing and Logging Properties for
 Waveform Acquisitions

Use tasks to define properties for when a system starts and stops acquisitions and how to
 perform data logging.

Before you begin, add a DAQ
 device to the system definition.

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Click Targets»Controller»Hardware»Chassis»DAQ in the configuration tree.
4. Under a DAQ device, click Analog Input.
5. In the Sample Mode drop-down menu, select
 Waveform.
6. In the Analog Input Task drop-down menu, select Create
 new...
7. In the Create DAQ Task dialog box, name the task and set
 basic timing properties and click OK.
8. Click Waveform Tasks and select the task you created.
9. Depending on your goal, access one of the following areas to configure how
 VeriStand performs waveform acquisitions. 
 Goals
LocationPerform finite acquisitions and identify
 an external sample clock.
Click the task and use the Task
 Configuration page.
Allow logging and configure to save data
 in .tdms log files.
Click Logging and
 use the Logging Configuration
 page.
Control waveform acquisitions by DAQ
 devices.
Use waveform task channels.
Define triggers to for acquisitions to
 start and stop when a certain analog or digital value occurs
 or a software command is received.
Click Triggers and
 use the Triggers Configuration
 page.
10. Save the system definition file.

Parent topic:

Adding and Configuring a DAQ Device

Related concepts:

- Single-Point Versus Waveform Acquisition

Related tasks:

- Adding and Configuring a DAQ Device
- Adding Waveform Task Channels

Related information:

- TDMS File Format

<!--NI_TOPIC bundle=veristand path=time-step-duration.html language=enus -->
## TOPIC 00358: Time Step Duration

- bundle_id: `veristand`
- source_path: `time-step-duration.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/time-step-duration.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Time Step Duration channel to monitor how long a model takes to execute. If a model takes a long time to execute, the PCL might run slower than the target rate or the model might not run on schedule during the next PCL iteration. If a system contains multiple models and you need to determine

### Time Step Duration

Use the Time Step Duration channel to monitor how long a model takes to
 execute.

If a model takes a long time to execute, the PCL might run slower than the target rate or the
 model might not run on schedule during the next PCL iteration. If a system contains
 multiple models and you need to determine which one delayed the system, monitor the Time
 Step Duration execution channel for each model. During each PCL iteration, a model
 executes one time step, so this channel allows you to see if a model executes longer
 than the expected rate, given the following equation.

Note

Parent topic:

Controlling and Monitoring Model Execution

<!--NI_TOPIC bundle=veristand path=trigger-logging-stimulus-profile.html language=enus -->
## TOPIC 00359: Configuring Triggered Logging in Stimulus Profiles

- bundle_id: `veristand`
- source_path: `trigger-logging-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/trigger-logging-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use triggered logging in stimulus profiles if you want to see channel data under certain conditions, such as those that you might expect to cause the unit under test (UUT) to fail. When you use the Stimulus Profile Editor to log real-time test data, you can configure start and stop triggers for logg

### Configuring Triggered Logging in Stimulus
 Profiles

Use triggered logging in stimulus profiles if you want to see channel data under certain
 conditions, such as those that you might expect to cause the unit under test (UUT) to
 fail.

Stimulus Profile
 Editor

You can also configure pre-triggered and post-triggered data
 logging. This saves the channel data immediately before a start
 trigger and after a stop trigger. For example, if the start trigger
 represents a fault in the system, and the stop trigger represents a
 return to expected values, it can be useful to see the behavior of
 the system that lead to the fault and how well the system
 recovers.

1. Create a stimulus profile that logs real-time test data.
2. Select the Start Logging step for a
 logging configuration.
3. In the Property Browser, set the
 Trigger Channel to a channel
 you want to watch for logging conditions. 
 Note This can be any channel in the system definition
 associated with the stimulus profile.
4. Set the Trigger Condition and the
 corresponding High Limit and
 Low Limit values. 
 Note You can set the Trigger
 Condition to
 in_limits or
 out_of_limits to configure
 logging to start and stop when the value of
 Trigger Channel either
 enters or leaves the value range specified by the
 limits. For example, if you set Trigger
 Condition to
 in_limits, the stimulus
 profile registers a start trigger when the value of
 Trigger Channel is greater than or equal to the Low
 Limit and less than or equal to the High Limit. It
 registers a stop trigger, and stops logging, when
 the value of Trigger Channel
 leaves this window.
5. Depending on your desired result, configure the step to handle
 a situation where multiple start triggers occur. 
 Desired Result
ConfigurationOne file containing all logged
 data.
Disable Replace Existing
 File.
One file containing only data from the last
 occurrence of a start trigger.
Enable Replace Existing
 File.
Separate files for each set of logged
 data.
Enable Timestamp
 Filename.Note You must enable
 timestamps on segmented filenames to avoid
 filename conflicts.
Set Segment Options to
 OnStartTrigger
6. If you want to specify an amount of channel data to log
 immediately before a start trigger occurs, set a value for
 Pre-Trigger Duration. 
 Note When you execute the profile, the VeriStand Gateway
 maintains a buffer that always contains this amount
 of data.
7. If you want to specify an amount of channel data to log after a
 stop trigger occurs, set a value for Post-Trigger
 Duration.
8. Click Save.

Parent topic:

Logging Real-Time Test Data with the Stimulus Profile Editor

Related tasks:

- Logging Real-Time Test Data with the Stimulus Profile Editor

Related reference:

- Start Logging Step

<!--NI_TOPIC bundle=veristand path=tutorial-create-basic-stimulus-profile.html language=enus -->
## TOPIC 00360: Creating a Basic Stimulus Profile

- bundle_id: `veristand`
- source_path: `tutorial-create-basic-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-create-basic-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a stimulus profile to execute a real-time sequence. Before you begin, create a real-time sequence for the engine demo. In the Stimulus Profile Editor, click the Start Page tab. Click New Stimulus Profile. Save the stimulus profile as Engine Demo Basics tutorial.nivsstimprof in the <Common

### Creating a Basic Stimulus Profile

Configure a stimulus profile to execute a real-time
 sequence.

Before you begin, create a real-time sequence for the
 engine demo.

1. In the Stimulus Profile Editor, click the Start
 Page tab.
2. Click New Stimulus Profile.
3. Save the stimulus profile as Engine Demo Basics
 tutorial.nivsstimprof in the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus
 Profiles\Basic Engine Demo directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. In the Steps palette, expand Real-Time
 Sequences and drag Real-Time Sequence
 Call into Main. 
 The Real-Time Sequence Call calls the real-time sequence you specify in
 the Property Browser.
6. Select the Real-Time Sequence Call step in the stimulus
 profile code to specify the real-time sequence to call. 
 The Property Browser displays several properties you can use to
 configure the step. Each step in a stimulus profile contains properties. These
 properties are editable attributes that determine how the step executes.
7. In the Property Browser, browse the File
 Path to the real-time sequence you created. 
 The Parameters section of the Property
 Browser displays the parameters in the called real-time sequence
 as well the channels assigned to them. If you use the parameters to read or
 write system definition channels, you must assign those channels to the
 parameters in the stimulus profile. When you add a real-time sequence call, the
 stimulus profiles uses the default assignment for each parameter.
8. Click the Target Name pull-down and select
 Controller to execute the real-time sequence on the
 Controller target.
9. Click the Pass Fail pull-down and select
 AlwaysPass.
10. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-CDE09225-47E9-46FE-877B-43D9F976982B-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Setting up a Basic Stimulus Profile Editor Test

Related tasks:

- Creating a Basic Real-Time Sequence
- Communicating with the VeriStand Editor Using Stimulus Profile Arguments
- Running a Stimulus Profile

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-create-real-time-sequence.html language=enus -->
## TOPIC 00361: Creating a Basic Real-Time Sequence

- bundle_id: `veristand`
- source_path: `tutorial-create-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-create-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a real-time sequence that starts, stalls, and stops the engine demo. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Profile Editor, click New Real-Time Sequence. Save the sequence as Engine D

### Creating a Basic Real-Time Sequence

Create a real-time sequence that starts, stalls, and stops the engine
 demo.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click New
 Real-Time Sequence.
3. Save the sequence as Engine Demo Basics tutorial.nivsseq
 in the <Common Data>
\VeriStand Projects\Engine Demo\Stimulus Profiles\Basic Engine
 Demo directory.
4. Add blocks to organize your code.
  1. In the Primitives palette, expand
 Miscellaneous and drag a
 Block into the Setup section of the real-time
 sequence.
  2. In the Property Browser Name field, enter
 Turn on engine.
  3. Add a block to the Main section and name it
 Set engine speed to 2500 and wait.
  4. Add a block to the Clean Up section and name it
 Turn off engine.
5. Create variables. 
 Note For an example of how to
 use channel references to access channels, refer to .
  1. In the Primitives palette, expand
 Variables and drag a
 Boolean into the
 Parameters section of the
 Variables pane.
  2. In the Property Browser next to Default
 Assignment, click Browse to display the system
 definition channel tree.
  3. Click View aliases [IMAGE alt='image' src='GUID-0308531A-12AA-4B14-8695-E9EEC39F28A1-a5.gif'] to display the aliases defined
 in the system definition.
  4. Double-click EnginePower to assign this alias to
 the parameter.
  5. In Identifier, enter
 EnginePower.
  6. In Units, enter On/Off.
  7. Select Double from the
 Primitives palette and drag it to
 Parameters to add a double-precision numeric
 parameter after EnginePower.
  8. In the Property Browser, name the new parameter
 DesiredRPM, map the parameter to the
 corresponding alias, and enter the units as RPM.
6. Add variables to the sequence code and set their values.
  1. In the Variables pane, drag
 EnginePower into the Turn on
 engine block.
  2. In the Property Browser, edit the
 Expression to EnginePower =
 true. 
 This value will turn the engine on when the block executes.
  3. Drag DesiredRPM into the Set engine
 speed to 2500 and wait block.
  4. Set DesiredRPM to 2500.
  5. Press <Ctrl> and drag
 DesiredRPM from the Set engine
 speed to 2500 and wait block into the Turn
 off engine block.
  6. Set DesiredRPM to
 0.
  7. In the Variables pane, right-click EnginePower and
 select Copy.
  8. Right-click Turn off engine and select
 Paste. 
 Leave the value as false to turn the engine off when the block
 executes.
7. Set the expression to wait before it executes.
  1. In the Sequences palette, expand Real-Time Sequence Library»Standard»Timing and drag Wait into the
 Set engine speed to 2500 and wait block.
  2. In the Property Browser, edit the Expression to
 replace Duration with
 20. 
 This will hold the DesiredRPM value at
 2500 for 20 seconds when this step executes.
8. Set a return value.
  1. In the Primitives palette, expand
 Variables and drag Void Return
 Value into the Return Variable
 section of the Variables pane. 
 Note By default, the
 return value node is named Pass.
  2. In the Property Browser, enter the
 Identifier as Output
 to change the name of the return value node.
9. Save the real-time sequence.

[IMAGE alt='image' src='GUID-4E998F3A-4FB7-4441-B618-EFB4D0471B13-a5.png']

After creating this real-time sequence code,
 you must add it
 to a stimulus profile.

Parent topic:

Setting up a Basic Stimulus Profile Editor Test

Related tasks:

- Deploying the Engine Demo
- Reading and Writing Channels Directly from a Real-Time Sequence Tutorial
- Creating a Basic Stimulus Profile

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-deploy-engine-demo.html language=enus -->
## TOPIC 00362: Deploying the Engine Demo

- bundle_id: `veristand`
- source_path: `tutorial-deploy-engine-demo.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-deploy-engine-demo.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Deploy the engine demo's system definition before running a stimulus profile. Launch VeriStand and double-click Engine Demo. In the Engine Demo dialog box, click Create. Select Operate Deploy and wait for the system definition to deploy.

### Deploying the Engine Demo

Deploy the engine demo's system definition before running a stimulus
 profile.

1. Launch VeriStand and double-click Engine Demo.
2. In the Engine Demo dialog box, click
 Create.
3. Select Operate»Deploy and wait for the system definition to deploy.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

<!--NI_TOPIC bundle=veristand path=tutorial-log-data.html language=enus -->
## TOPIC 00363: Creating a Stimulus Profile to Log Data

- bundle_id: `veristand`
- source_path: `tutorial-log-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-log-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a stimulus profile that logs RPM and Temperature data as a TMDS file. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Profile Editor, click New Stimulus Profile. Save the stimulus profile as E

### Creating a Stimulus Profile to Log
 Data

Create a stimulus profile that logs RPM and Temperature data as a TMDS
 file.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click
 New Stimulus Profile.
3. Save the stimulus profile as Engine Demo Logging
 tutorial.nivsstimprof in the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Logging directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. In the Steps palette, expand Logging and
 drag Start Logging into Main. 
 A Channel
 Group step automatically appears under Start Logging. This step logs execution
 data for the channels you specify in each Channel Group that appears under this step.
6. From the Steps palette, drag another Channel
 Group into Start Logging so it contains two groups.
7. Click the Start Logging step and, in the Property Browser,
 configure it.
  1. Enter the Configuration Name as Logging
 Configuration Demo.
  2. Browse the File Path to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Logging, enter the File name as Log
 File, and click Save.
  3. Enable Replace Existing File.
  4. Enter the Log Rate [Hz] as 100.
  5. Click the Trigger Condition pull-down and select
 none.
  6. Click the Segment Options pull-down and select
 DoNotSegment.
8. Click the first Channel Group and, in the Property Browser,
 configure it.
  1. Enter the Channel Group Name as
 RPM.
  2. Browse the Channels, expand Aliases,
 and enable ActualRPM and
 DesiredRPM.
9. Click the second Channel Group and, in the Property Browser,
 configure it. 
 
 VeriStand logs data from the channels in the RPM and Temperature groups to
 Log File.tdms.
  1. Enter the Channel Group Name as
 Temperature.
  2. Browse the Channels, expand Aliases,
 and enable EngineTemp.
10. In the Steps palette, expand Real-Time
 Sequences and drag Real-Time Sequence Call into
 Main.
11. Configure the Real-Time Sequence Call.
  1. In the Property Browser, browse the File
 Path to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Logging\Engine Demo Logging.nivsseq.
  2. Click the Target Name pull-down and select
 Controller.
12. In the Steps palette, drag Stop Logging
 into Clean Up.
13. In the Property Browser of the step, enter the
 Configuration Name as Logging Configuration
 Demo.
14. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-DAA98310-C0B1-4AEA-904F-0EF68FCFA060-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Logging Data to a File using a Stimulus Profile

Related reference:

- VeriStand Directories and Aliases
- Channel Group Step

<!--NI_TOPIC bundle=veristand path=tutorial-multitask-real-time-sequence.html language=enus -->
## TOPIC 00364: Creating a Multitasking Real-Time Sequence

- bundle_id: `veristand`
- source_path: `tutorial-multitask-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-multitask-real-time-sequence.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a real-time sequence that will warm-up and monitor the demo engine in separate tasks. Before you begin, you need to deploy the Engine Demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Profile Editor, click New Real-Time Sequence.

### Creating a Multitasking Real-Time
 Sequence

Create a real-time sequence that will warm-up and monitor the demo
 engine in separate tasks.

Before you begin, you need to deploy the Engine Demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click New
 Real-Time Sequence.
3. Save the sequence as Engine Demo Advanced tutorial in the
 <Common Data>\VeriStand Projects\Engine
 Demo\Stimulus Profiles\Engine Demo Advanced directory.
4. Add blocks to organize your code.
  1. In the Primitives palette, expand
 Miscellaneous and drag a
 Block into the Setup section of the real-time
 sequence.
  2. In the Property Browser Name field, enter
 Turn on engine.
  3. Add a block to the Main section and name it
 Set engine speed to 2500 and wait.
  4. Add a block to the Clean Up section and name it
 Turn off engine.
5. Create variables. 
 
 The Variables pane will look like the following
 image. 
[IMAGE alt='image' src='GUID-FD097D12-01DC-42EE-9FBE-9FEA38D351E2-a5.gif']
  1. In the Primitives palette, expand
 Variables and drag a
 Boolean into the
 Parameters section of the
 Variables pane.
  2. In the Property Browser next to Default
 Assignment, click Browse to display the system
 definition channel tree.
  3. Click View aliases [IMAGE alt='image' src='GUID-0308531A-12AA-4B14-8695-E9EEC39F28A1-a5.gif'] to
 display the aliases defined in the system definition.
  4. Double-click EnginePower to assign this alias to
 the parameter.
  5. In Identifier, enter
 EnginePower.
  6. In Units, enter On/Off.
  7. Select Double from the
 Primitives palette and drag it to
 Parameters to add a double-precision numeric
 parameter after EnginePower.
  8. In the Property Browser, name the new parameter
 DesiredRPM, map the parameter to the
 corresponding alias, and enter the units as RPM.
  9. Add another Double primitive after DesiredRPM,
 name it ActualRPM, and map it to the
 corresponding alias.
  10. Add another Double primitive after ActualRPM,
 name it EngineTemp, and map it to the
 corresponding alias.
  11. Drag a Boolean primitive into the Local Variables
 section of the Variables pane and name it
 WarmUpComplete. 
 Note Local variables are
 variables you use within the real-time sequence as a way to hold
 values you get or set in statements.
  12. In the Primitives palette under Variables, drag
 Void Return Value into the Return
 Variable section of the Variables
 pane. 
 Note By default, the
 return value node is named Pass.
6. Add variables to the sequence code and set their values.
  1. In the Variables pane, drag
 EnginePower into the Turn on
 engine block.
  2. In the Property Browser, edit the
 Expression to EnginePower =
 true. 
 This value will turn the engine on when the block executes.
  3. Drag WarmUpComplete into
 Setup so that this variable is at the same
 level in the tree as Turn on engine. 
 Adding WarmUpComplete to Setup initializes the variable to a known
 value so that the real-time sequence can then write values to the
 variable during execution.
  4. Drag EnginePower into Turn off
 engine. 
 Leave the value as false to turn off the engine
 when the block executes.
  5. Drag DesiredRPM into Turn off
 engine. 
 Leave the value as 0 to decrease the RPM to 0
 when the block executes.
7. Enable Multitasking
  1. In the Primitives palette, expand Structures»Multitasking and drag MultiTask into
 Main.
  2. In the Property Browser, rename
 Task1 as EngineWarmUp
 and Task2 as
 MonitorEngineTemperature.
  3. Modify the EngineWarmUp task by adding the
 following code. 
 [IMAGE alt='image' src='GUID-CB432E20-56E9-405B-9B1B-C9EC3BD26C48-a5.gif'] 

Note In the
 Sequences palette, expand Real-Time Sequence Library»Standard»Timing to find
 WaitUntilSettled. 
 The EngineWarmUp task sets the engine speed (DesiredRPM) to 2500
 RPM, and then waits until the RPM (ActualRPM) settles into a range
 between 2450 and 9999999 RPM for 25 seconds. Then the task will raise
 the engine speed to 8000 RPM and wait until the RPM settles into a range
 between 7800 and 9999999 RPM for another 25 seconds. When the task
 successfully completes, the task sets the WarmUpComplete variable to
 true for the MonitorEngineTemperature task.
8. Modify the MonitorEngineTemperature task with the
 following code. 
 [IMAGE alt='image' src='GUID-B768E9EA-DC98-45C8-85E7-D5D2AFB1336C-a5.gif'] 

Note In the
 Primitives palette, expand Structures»Loops to find the DoWhile Loop and Structures»Conditional to find If Else. 
 As long as the WarmUpComplete variable is false, the
 MonitorEngineTemperature task monitors the engine temperature
 (EngineTemperature) to ensure it does not exceed 110 degrees. If the engine
 temperature exceeds 110 degrees, the engine shuts down and the sequence aborts.
 If the engine temperature remains below 110 degrees, the sequence completes its
 execution and turns off the engine.
9. Save the real-time sequence.

[IMAGE alt='image' src='GUID-F6C57201-E8E5-4417-ACAF-A61872627862-a5.png']

After creating this real-time
 sequence, add it to
 a stimulus profile.

Parent topic:

Executing Multiple Parallel Tasks Using the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Multitasking Stimulus Profile

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-multitask-stimulus-profile.html language=enus -->
## TOPIC 00365: Creating a Multitasking Stimulus Profile

- bundle_id: `veristand`
- source_path: `tutorial-multitask-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-multitask-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a stimulus profile to execute a multitasking real-time sequence. Before you begin, create a real-time sequence that performs multitasking. In the Stimulus Profile Editor, click the Start Page tab. Click New Stimulus Profile. Save the stimulus profile as Engine Demo Advanced tutorial in the

### Creating a Multitasking Stimulus
 Profile

Configure a stimulus profile to execute a multitasking
 real-time sequence.

Before you begin, create a real-time sequence
 that performs multitasking.

1. In the Stimulus Profile Editor, click the Start
 Page tab.
2. Click New Stimulus Profile.
3. Save the stimulus profile as Engine Demo Advanced tutorial in the
 <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Advanced directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. Create a step to call the sequence you created.
  1. In the Steps palette, expand Real-Time
 Sequences and drag Real-Time Sequence Call into
 Main.
  2. Select the Real-Time Sequence Call step in the stimulus
 profile code to specify the real-time sequence to call.
  3. In the Property Browser, browse the File
 Path to the real-time sequence you created.
  4. Click the Target Name pull-down and select
 Controller to execute the real-time sequence on the
 Controller target.
6. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-ED6D4263-A213-4CBD-8E62-6EF3368D6140-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Executing Multiple Parallel Tasks Using the Stimulus Profile Editor Tutorial

Related tasks:

- Creating a Multitasking Real-Time Sequence

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-real-time-sequence-pass-fail.html language=enus -->
## TOPIC 00366: Creating a Real-Time Sequence to Return a Pass/Fail Value

- bundle_id: `veristand`
- source_path: `tutorial-real-time-sequence-pass-fail.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-real-time-sequence-pass-fail.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Update an existing sequence to pass a Boolean return value. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . Click File Open , navigate to <Common Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo Ad

### Creating a Real-Time Sequence to Return a
 Pass/Fail Value

Update an existing sequence to pass a Boolean return
 value.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. Click File»Open, navigate to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus
 Profiles\Engine Demo Advanced, and double-click the Engine Demo
 Advanced sequence.
3. Save the sequence as Engine Demo Return Value tutorial in
 the <Common Data>\VeriStand Projects\Engine Demo\Stimulus
 Profiles\Engine Demo Return Value directory.
4. In the Primitives palette, expand
 Variables and drag Boolean to
 the Variables pane under Return
 Value to change the value from a Void Return Value.
5. In the Property Browser, change the
 Identifier to
 WarmUpSucceeded.
6. From the Variables pane, drag
 WarmUpSucceeded into the sequence code under
 MonitorEngineTemperature, inside
 Then. 
 If the Then section of the code executes, the return value will be
 false. This indicates that the warm-up task failed because the engine
 temperature exceeded 110 degrees.
7. Drag another WarmUpSucceeded into the sequence code
 under MonitorEngineTemperature, inside
 Else, and modify it in the Property
 Browser to be true. 
 If the Else section of the code executes, the return value will be true.
 This indicates that the warm-up task succeeded because the engine temperature
 remained below 110 degrees.
8. Save the real-time sequence.

[IMAGE alt='image' src='GUID-08133E0B-476B-4B85-9D55-015193B6AF1C-a5.gif']

After creating this real-time
 sequence, add it to
 a stimulus profile.

Parent topic:

Configuring Failure Notification Using the Stimulus Profile Editor Tutorial

Related tasks:

- Creating a Stimulus Profile with Execution Behavior after Step Failure

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-run-stimulus-profile.html language=enus -->
## TOPIC 00367: Running a Stimulus Profile

- bundle_id: `veristand`
- source_path: `tutorial-run-stimulus-profile.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-run-stimulus-profile.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Compile and run the stimulus profile to see the real-time sequence interact with the Engine Demo. On the stimulus profile, expand Execution Results. After each step executes, Execution Results displays the name of the step and the result of the step execution. Click Run to compile all the open and r

### Running a Stimulus Profile

Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

1. On the stimulus profile, expand Execution Results. 
 After each step executes, Execution Results displays the
 name of the step and the result of the step execution.
2. Click Run to compile all the open and referenced
 real-time sequence files and run the stimulus profile. 
 You can observe the user interface's graph to see the output change as the
 real-time sequence executes. Note The Warnings and Errors
 pane displays any errors, warnings, or messages that you must resolve before
 the stimulus profile can successfully execute. 
 The engine demo will run like in the following image. 
[IMAGE alt='image' src='GUID-12F52574-B6B8-4DEE-98F4-15D5C66DF2BF-a5.png']

When the stimulus profile completes its execution, the ATML Test
 Report opens. This report displays details about the stimulus profile
 execution. If you run the stimulus profile again, the previous results are overwritten.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related concepts:

- Automatic Test Markup Language (ATML) Standard

<!--NI_TOPIC bundle=veristand path=tutorial-sequence-channel-reference.html language=enus -->
## TOPIC 00368: Create a Real-Time Sequence with a Channel Reference

- bundle_id: `veristand`
- source_path: `tutorial-sequence-channel-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-sequence-channel-reference.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a real-time sequence that uses a channel reference to read/write a engine power channel and a parameter to specify the value to read/write. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Prof

### Create a Real-Time Sequence with a Channel
 Reference

Create a real-time sequence that uses a channel
 reference to read/write a engine power channel and a parameter to specify the value to
 read/write.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click New
 Real-Time Sequence.
3. Save the sequence as Set Engine Power tutorial in the
 <Common Data>\VeriStand Projects\Engine Demo\Stimulus
 Profiles\Engine Demo Channel References directory.
4. Create variables. 
 
 The Variables pane will look like the following
 image. 
[IMAGE alt='image' src='GUID-E50A200C-4545-4DE5-B01E-7F5ED558EBED-a5.jpg']
  1. In the Primitives palette, expand
 Variables and drag a
 Boolean into the
 Parameters section of the
 Variables pane.
  2. In the Property Browser, enter the
 Identifier, as
 OnOff.
  3. Click the Evaluation Method pull-down, select
 ByReference. 
 This parameter specifies whether to turn the engine on or off. You set
 the value when you call this sequence from the stimulus profile.
  4. In the Variables pane, right-click
 Channel References and click
 Insert Channels.
  5. In the Select channels dialog box, expand
 Aliases, enable
 EnginePower, and click
 OK. 
 This channel reference writes the value of the OnOff parameter to the
 EnginePower channel.
  6. In the Primitives palette under Variables, drag
 Void Return Value into the Return
 Variable section of the Variables
 pane. 
 This variable returns no value. Instead, you call this sequence from a
 stimulus profile to turn the engine on and off. Note By default, the
 return value node is named Pass.
5. Configure the real-time sequence to turn the engine on or off based on the
 value of the OnOff parameter.
  1. In the Variables pane, drag
 EnginePower into Main.
  2. In the Property Browser, enter the
 Expression as EnginePower =
 OnOff. 
 This allows you to toggle the engine on or off by calling this
 sequence from a stimulus profile.
6. Save the real-time sequence.

The real-time sequence code will look like the following image.

[IMAGE alt='image' src='GUID-6F34AE8F-58F5-4F52-A260-E0F2CCE36CB2-a5.png']

After creating this real-time sequence,
 create another
 real-time sequence.

Parent topic:

Reading and Writing Channels Directly from a Real-Time Sequence Tutorial

Related tasks:

- Create a Real-Time Sequence with Channel References and Local Variables

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-sequence-parameters-local-variables.html language=enus -->
## TOPIC 00369: Create a Real-Time Sequence with Channel References and Local Variables

- bundle_id: `veristand`
- source_path: `tutorial-sequence-parameters-local-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-sequence-parameters-local-variables.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a real-time sequence that uses channel references to measure how long the engine takes to settle at a specified RPM. Before you begin, create a real-time sequence with a channel reference. In the Stimulus Profile Editor, click the Start Page tab. Click New Real-Time Sequence. Save the sequenc

### Create a Real-Time Sequence with Channel
 References and Local Variables

Create a real-time sequence that uses channel references to
 measure how long the engine takes to settle at a specified RPM.

Before you begin, create a real-time sequence with a channel reference.

1. In the Stimulus Profile Editor, click the Start
 Page tab.
2. Click New Real-Time Sequence.
3. Save the sequence as Measure Set Preference tutorial in the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Channel References directory.
4. Create variables. 
 
 The Variables pane will look like the following
 image. 
[IMAGE alt='image' src='GUID-A242594A-8E84-4FB7-9305-E7340B942500-a5.jpg']
  1. In the Primitives palette, expand
 Variables, drag a Double into the
 Return Variable section of the Variables
 pane, and enter its Identifier as
 SettleTime
  2. Create and configure the following Double parameters and local variable. 
 Variable Type
Name
Evaluation Method
UnitsParameter
Setpoint
ByValue
rpm
Parameter
Tolerance
ByValue
rpm
Parameter
Timeout
ByValue
s
Local variable
StartTime
ByValue
s
  3. In the Variables pane, right-click Channel
 References and click Insert Channels.
  4. In the Select channels dialog box, expand
 Aliases, enable ActualRPM and
 DesiredRPM, and click OK.
5. Add a setup expression for the set point of the engine. 
 
 The Setup block of the sequence code uses the DesiredRPM channel reference to
 change the value of the DesiredRPM channel to the specified Setpoint. You specify the
 value of the Setpoint parameter when you call this sequence from the stimulus profile. By
 configuring the real-time sequence this way, you can call this sequence from the stimulus
 profile to measure the settle time of various set points.
  1. In the Primitives pane, expand
 Miscellaneous and drag Comment into
 Setup.
  2. In the Property Browser, enter the
 Comment as Set the desired set point for the
 engine.
  3. In the Variables pane, drag DesiredRPM
 into Setup.
  4. In the Property Browser, enter the
 Expression as DesiredRPM = Setpoint.
6. Add main expressions to measure how long it takes for the engine to settle at its RPM
 set point. 
 
 The Main block of the sequence stores the absolute time at which the sequence
 starts to the StartTime local variable. The code waits for the RPM, as read from the
 ActualRPM channel, to settle into a range between the DesiredRPM plus or minus the
 specified Tolerance for at least one second or until it reaches the specified Timeout.
 When the RPM either settles or times out, the code returns how long it took the engine to
 settle at the specified RPM.
  1. In the Primitives pane, drag Comment
 into Main.
  2. In the Property Browser, enter the
 Comment as Measure how long it takes for the
 engine to settle at its RPM set point.
  3. In the Variables pane, drag StartTime
 into Main.
  4. In the Property Browser, enter the
 Expression as StartTime = abstime().
  5. In the Sequences pane, expand Real-Tim Sequence Library»Standard»Timing and drag WaitUntilSettled into
 Main.
  6. In the Property Browser, enter the
 Expression as WaitUntilSettled(ActualRPM,
 DesiredRPM + Tolerance, DesiredRPM - Tolerance, 1.0, Timeout).
  7. In the Variables pane, drag SettleTime
 into Main.
  8. In the Property Browser, enter the
 Expression as SettleTime = abstime() -
 StartTime.
7. Save the real-time sequence.

The real-time sequence code will look like the following image.

[IMAGE alt='image' src='GUID-E9918507-C4D5-4BD6-8F16-F7ABE62338B1-a5.png']

After creating this real-time sequence,
 add it to a stimulus
 profile.

Parent topic:

Reading and Writing Channels Directly from a Real-Time Sequence Tutorial

Related tasks:

- Create a Real-Time Sequence with a Channel Reference
- Creating a Stimulus Profile that Calls a Channel Referencing Sequence

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-basic-test.html language=enus -->
## TOPIC 00370: Setting up a Basic Stimulus Profile Editor Test

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-basic-test.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-basic-test.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a real-time sequence that turns on a car engine, sets the engine speed to 2500 RPM, holds this speed for 20 seconds, and then turns the engine off. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus profile. Create a real-time sequence—Create a real-ti

### Setting up a Basic Stimulus Profile Editor
 Test

Create a real-time sequence that turns on a car engine, sets the
 engine speed to 2500 RPM, holds this speed for 20 seconds, and then turns the engine
 off.

1. Deploy the
 Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a
 real-time sequence—Create a real-time sequence that starts, stalls, and stops the engine
 demo.
3. Create a
 stimulus profile—Configure a stimulus profile to execute a real-time
 sequence.
4. Run the
 stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Basic Real-Time Sequence
- Creating a Basic Stimulus Profile
- Running a Stimulus Profile

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-call-csv-file.html language=enus -->
## TOPIC 00371: Calling a CSV File as a Real-Time Sequence

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-call-csv-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-call-csv-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Comma Separated Values (.csv) files within stimulus profiles to stimulate, fault, and evaluate channels. The stimulus profile you create in this tutorial executes a CSV file that turns on an engine and increases the RPM to 2500 within 10 seconds. After this CSV file completes its execution, the

### Calling a CSV File as a Real-Time
 Sequence

Use Comma Separated Values (.csv) files within stimulus
 profiles to stimulate, fault, and evaluate channels.

The stimulus profile you create in this tutorial executes a CSV file that
 turns on an engine and increases the RPM to 2500 within 10 seconds.
 After this CSV file completes its execution, the stimulus profile
 calls a sequence from the built-in library of sequences that causes
 the system to wait until the RPM parameters settle. Finally, the
 stimulus profile executes another CSV file that sets the engine RPM
 to various values over the course of 70 seconds.

To run in a stimulus profile, a CSV file must define inputs, values to
 assign to those inputs, and timestamps at which to update the input
 values. The CSV file must include this data under specific column
 headers that VeriStand expects.

1. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a stimulus profile to call the
 CSV file—Create a stimulus profile that calls two Comma Separated Values
 (.csv) files like a real-time sequence.
3. Run
 the stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-execute-parallel-tasks.html language=enus -->
## TOPIC 00372: Executing Multiple Parallel Tasks Using the Stimulus Profile Editor Tutorial

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-execute-parallel-tasks.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-execute-parallel-tasks.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a stimulus profile and a real-time sequence that incorporates multitasking, which executes multiple parallel tasks. This real-time test turns on a car engine, sets the engine speed to 2500 RPM, and holds this speed for 25 seconds. It then raises the engine speed to 8000 RPM and holds this spe

### Executing Multiple Parallel Tasks Using the
 Stimulus Profile Editor Tutorial

Create a stimulus profile and a real-time sequence that incorporates
 multitasking, which executes multiple parallel tasks.

This real-time test turns on a car
 engine, sets the engine speed to 2500 RPM, and holds this speed for 25 seconds. It then
 raises the engine speed to 8000 RPM and holds this speed for another 25 seconds. In
 addition to controlling the engine speed, the sequence monitors engine temperature. If
 the engine temperature exceeds 110 degrees, the engine shuts down and the sequence
 aborts.

1. Deploy the
 Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a
 multitasking real-time sequence—Create a real-time sequence that will warm-up and monitor the demo
 engine in separate tasks.
3. Create a
 stimulus profile—Configure a stimulus profile to execute a multitasking
 real-time sequence.
4. Run the
 stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Multitasking Real-Time Sequence
- Creating a Multitasking Stimulus Profile
- Running a Stimulus Profile

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-failure-notice.html language=enus -->
## TOPIC 00373: Configuring Failure Notification Using the Stimulus Profile Editor Tutorial

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-failure-notice.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-failure-notice.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify a real-time test by adding a return value that reflects the success or failure of a warm-up task. If the engine temperature does not exceed 110 degrees, the warm-up task completes and the sequence returns true, which indicates that the warm-up task succeeded. If the engine temperature exceeds

### Configuring Failure Notification Using the
 Stimulus Profile Editor Tutorial

Modify a real-time test by adding a return value that reflects the
 success or failure of a warm-up task.

If the engine temperature does not exceed
 110 degrees, the warm-up task completes and the sequence returns true, which indicates
 that the warm-up task succeeded. If the engine temperature exceeds 110 degrees, the
 engine shuts down and the return value is false, which indicates that the warm-up task
 failed.

1. Deploy the
 Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a
 real-time sequence to return a pass/fail value—Update an existing sequence to pass a Boolean return
 value.
3. Create a
 stimulus profile to execute after a step fails—Define the actions a stimulus profile performs to stop execution
 after a step fails.
4. Run the
 stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Stimulus Profile
 Editor

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Real-Time Sequence to Return a Pass/Fail Value
- Creating a Stimulus Profile with Execution Behavior after Step Failure
- Running a Stimulus Profile

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-log-data.html language=enus -->
## TOPIC 00374: Logging Data to a File using a Stimulus Profile

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-log-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-log-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Log channel data from a running stimulus test to a TDMS file. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus profile. Create a stimulus profile to log data—Create a stimulus profile that logs RPM and Temperature data as a TMDS file. Run the stimulus profi

### Logging Data to a File using a Stimulus
 Profile

Log channel data from a running stimulus test to a TDMS
 file.

1. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a stimulus profile to log
 data—Create a stimulus profile that logs RPM and Temperature data as a TMDS
 file.
3. Run
 the stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

VeriStand Editor

[IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']

»

TDMS File Viewer

Workspace

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Stimulus Profile to Log Data
- Running a Stimulus Profile
- Enhancing Your Workspace to View Data

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-play-macro-file.html language=enus -->
## TOPIC 00375: Creating a Stimulus Profile to Play a Macro File

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-play-macro-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-play-macro-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a stimulus profile to call a macro file that contains data from a previous engine test. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Profile Editor, click New Stimulus Profile. Save the sti

### Creating a Stimulus Profile to Play a Macro
 File

Create a stimulus profile to call a macro file that contains data from a
 previous engine test.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click
 New Stimulus Profile.
3. Save the stimulus profile as Engine Demo Macro Player
 tutorial.nivsstimprof in the <Common Data>\VeriStand
 Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Macro Player directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. In the Steps palette, expand
 Other and drag
 Macro Player to
 Main.
6. In the Property Browser next to VeriStand
 Macro File, click Browse and select
 <Common Data>\Examples\Stimulus
 Profile\Engine Demo\Stimulus Profiles\Engine Demo
 Macro Player\Engine Demo Macro.nivsmacro.
7. Click the Playback Mode pull-down and
 select UseTiming to play back the
 macro file using the timing information embedded in the
 file.
8. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-18F7F0FE-F812-45DF-B5E8-F7EAFE74D09F-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Playing Back Previously Recorded Test Data Using the Stimulus Profile Editor

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-playback-test-data.html language=enus -->
## TOPIC 00376: Playing Back Previously Recorded Test Data Using the Stimulus Profile Editor

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-playback-test-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-playback-test-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create and run a stimulus profile that plays back data from a previously recorded VeriStand macro file. A macro file is a recording of the commands sent to the target. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus profile. Create a stimulus profile—Creat

### Playing Back Previously Recorded Test Data
 Using the Stimulus Profile Editor

Create and run a stimulus profile that plays back data from a
 previously recorded VeriStand macro file.

macro file

1. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a stimulus profile—Create a stimulus profile to call a macro file that contains data from a
 previous engine test.
3. Run the stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Creating a Stimulus Profile to Play a Macro File
- Running a Stimulus Profile

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-profile-channel-reference.html language=enus -->
## TOPIC 00377: Creating a Stimulus Profile that Calls a Channel Referencing Sequence

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-profile-channel-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-profile-channel-reference.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a stimulus profile to turn on the engine and measure how long it takes the engine to settle at various RPMs. Before you begin, create a real-time sequence with channel references and local variables. In the Stimulus Profile Editor, click the Start Page tab. Click New Stimulus Profile. Save

### Creating a Stimulus Profile that Calls a
 Channel Referencing Sequence

Configure a stimulus profile to turn on the engine and
 measure how long it takes the engine to settle at various RPMs.

Before you begin, create a real-time sequence
 with channel references and local variables.

1. In the Stimulus Profile Editor, click the Start
 Page tab.
2. Click New Stimulus Profile.
3. Save the sequence as Test Engine Set Points tutorial in the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Channel References directory.
4. Add a setup step to call the sequence to turn on the engine.
  1. In the Steps palette, expand Real-Time
 Sequences and drag Real-Time Sequence Call into
 Setup.
  2. In the Property Browser, navigate to the Set Engine
 Power real-time sequence as the Filename.
  3. Under Parameters, click the OnOff
 pull-down and select True. 
 Note You do not need to configure any channel mappings from the stimulus profile. The
 real-time sequence uses a channel reference to change the value of the EnginePower
 channel to the value specified by the OnOff parameter.
5. Add main steps.
  1. Add a Real-Time Sequence Call into
 Main.
  2. In the Property Browser, navigate to the Measure Set
 Point Response real-time sequence as the Filename.
  3. Under Parameters, enter the Setpoint
 as 2500, Timeout as
 60, and Tolerance as
 100.
  4. Add another Real-Time Sequence Call to the Measure
 Set Point Response real-time sequence and enter the
 Setpoint as 6000,
 Timeout as 60, and
 Tolerance as 100.
  5. Add another Real-Time Sequence Call to the Measure
 Set Point Response real-time sequence and enter the
 Setpoint as 3000,
 Timeout as 60, and
 Tolerance as 100.
6. Add clean up steps.
  1. Add a Real-Time Sequence Call into Clean
 Up.
  2. In the Property Browser, navigate to the Set Engine
 Power real-time sequence as the Filename.
  3. Under Parameters, click the OnOff
 pull-down and select False.
7. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-39BD16C1-5560-4ACB-B6AA-0E6F0C375785-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Reading and Writing Channels Directly from a Real-Time Sequence Tutorial

Related tasks:

- Create a Real-Time Sequence with Channel References and Local Variables

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-profile-csv.html language=enus -->
## TOPIC 00378: Creating a Stimulus Profile to call CSV Files

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-profile-csv.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-profile-csv.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a stimulus profile that calls two Comma Separated Values (.csv) files like a real-time sequence. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . In the Stimulus Profile Editor, click New Stimulus Profile. Sav

### Creating a Stimulus Profile to call CSV
 Files

Create a stimulus profile that calls two Comma Separated Values
 (.csv) files like a real-time sequence.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. In the Stimulus Profile Editor, click
 New Stimulus Profile.
3. Save the stimulus profile as Engine Demo CSV File Replay
 tutorial.nivsstimprof in the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo CSV
 File Replay directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. Expand Real-Time Sequences and drag Real-Time
 Sequence Call step into Main.
6. In the Property Browser, next to File Path, click
 Browse and select <Common
 Data>\Examples\Stimulus Profile\Engine Demo\Stimulus Profiles\Engine
 Demo CSV File Replay\WarmUp Phase 1.csv.
7. Click the Target Name pull-down and select
 Controller to execute the CSV file on the Controller
 target.
8. In the Sequences palette, expand Real-Time Sequence Library»Standard»Timing and dragWaitUntilSettled into
 Main.
9. In the Property Browser, configure the WaitUntilSettled
 sequence.
  1. Click the Target Name pull-down and select
 Controller.
  2. Click the Type pull-down and select
 AlwaysPass
  3. Next to Signal, select Channel and click
 Browse to display the system definition channel tree.
  4. Click View aliases [IMAGE alt='image' src='GUID-0308531A-12AA-4B14-8695-E9EEC39F28A1-a5.gif'] to display the aliases defined
 in the system definition.
  5. Double-click ActualRPM to assign this alias to the
 parameter.
  6. Next to UpperLimit, select Constant and enter
 500000.
  7. Next to LowerLimit, select Constant and enter
 2400.
  8. Next to Timeout, select Constant and enter
 120.
10. Drag another Real-Time Sequence Call step into
 Main.
11. In the Property Browser, configure the step to call
 WarmUp Phase 2.csv, located in the same directory as
 WarmUp Phase 1.csv, and set the Target Name
 to Controller.
12. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-BB5B571F-DBA9-4BF0-AD58-94EE93A39E43-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Calling a CSV File as a Real-Time Sequence

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-profile-editorl.html language=enus -->
## TOPIC 00379: Getting Started with the Stimulus Profile Editor Tutorial

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-profile-editorl.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-profile-editorl.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use tutorial examples to become familiar with the Stimulus Profile Editor. Before you begin, learn how to navigate the stimulus profile editor. Set up a basic test—Create a real-time sequence that turns on a car engine, sets the engine speed to 2500 RPM, holds this speed for 20 seconds, and then tur

### Getting Started with the Stimulus Profile
 Editor Tutorial

Use tutorial examples to become familiar with the Stimulus Profile
 Editor.

Before you begin, learn how to navigate the stimulus profile editor.

1. Set
 up a basic test—Create a real-time sequence that turns on a car engine, sets the
 engine speed to 2500 RPM, holds this speed for 20 seconds, and then turns the engine
 off.
  1. Reading and writing channels directly from a
 real-time sequence—Use channel references, parameters, and variables to turn on a car
 engine, set the engine speed to three different RPM values, measure how long the engine takes
 to settle at each specified RPM, and turn the engine off.
2. Execute multiple parallel tasks—Create a stimulus profile and a real-time sequence that incorporates
 multitasking, which executes multiple parallel tasks.
3. Configure failure notification—Modify a real-time test by adding a return value that reflects the
 success or failure of a warm-up task.
4. Log
 data to a file—Log channel data from a running stimulus test to a TDMS
 file.
5. Call a CSV file as a real-time sequence—Use Comma Separated Values (.csv) files within stimulus
 profiles to stimulate, fault, and evaluate channels.
6. Play back previously recorded test data—Create and run a stimulus profile that plays back data from a
 previously recorded VeriStand macro file.
7. Update model parameter values during test
 execution—Call text files in a stimulus profile to update the values of engine
 model parameters while a test is running.

\Examples\Stimulus Profile\Engine
 Demo\Stimulus Profiles

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related tasks:

- Navigating the Stimulus Profile Editor Environment
- Setting up a Basic Stimulus Profile Editor Test
- Reading and Writing Channels Directly from a Real-Time Sequence Tutorial
- Executing Multiple Parallel Tasks Using the Stimulus Profile Editor Tutorial
- Configuring Failure Notification Using the Stimulus Profile Editor Tutorial
- Logging Data to a File using a Stimulus Profile
- Calling a CSV File as a Real-Time Sequence
- Playing Back Previously Recorded Test Data Using the Stimulus Profile Editor
- Updating Model Parameters During Test Execution Using the Stimulus Profile Editor Tutorial

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-profile-setp-failure.html language=enus -->
## TOPIC 00380: Creating a Stimulus Profile with Execution Behavior after Step Failure

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-profile-setp-failure.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-profile-setp-failure.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Define the actions a stimulus profile performs to stop execution after a step fails. Before you begin, create a real-time sequence that returns a pass/fail value. In the Stimulus Profile Editor, click the Start Page tab. Click New Stimulus Profile. Save the stimulus profile as Engine Demo Return Val

### Creating a Stimulus Profile with Execution
 Behavior after Step Failure

Define the actions a stimulus profile performs to stop execution
 after a step fails.

Before you begin, create a real-time sequence
 that returns a pass/fail value.

1. In the Stimulus Profile Editor, click the Start
 Page tab.
2. Click New Stimulus Profile.
3. Save the stimulus profile as Engine Demo Return Value tutorial in
 the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Return Value directory.
4. Add a step to launch the VeriStand Editor. 
 
 When the stimulus profile runs, this step opens the VeriStand
 Editor or Workspace so you can watch the
 stimulus profile execute.
  1. In the Steps palette, expand
 Other and drag Command
 Shell into Setup.
  2. In the Property Browser, specify the full path to
 VeriStand.exe as the
 Filename. 
 Note You can add arguments in the Property
 Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to
 connect to.
5. Create a step to call the sequence you created.
  1. In the Steps palette, expand Real-Time
 Sequences and drag Real-Time Sequence Call into
 Main.
  2. Select the Real-Time Sequence Call step in the stimulus
 profile code to specify the real-time sequence to call.
  3. In the Property Browser, browse the File
 Path to the real-time sequence you created.
  4. Click the Target Name pull-down and select
 Controller to execute the real-time sequence on the
 Controller target.
6. Create pop-up dialog box. 
 
 Because the Message Box step executes after the Real-Time Sequence Call step, you only
 see this message if the Real-Time Sequence Call step executes without failure, or if Stop
 Execution on Fail is disabled.
  1. In the Steps palette, expand the Other
 and drag Message Box into Main.
  2. In the Property Browser, enter the following into
 Message: 
 Because the Stop Execution on Fail checkbox is disabled, the Message Box
 step executes despite the failure of the previous step.
  3. Enter the following text into Dialog Title: 
 Checked/Unchecked - Stop Execution on Fail
  4. In Default Text, enter OK.
7. Click Engine Demo Return Value tutorial.nivsstimprof and in the
 Property Browser disable Stop Execution on
 Fail.
8. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-CF80D1F3-9C1C-4A0F-8E3E-960DD8DEEB27-a5.png']

After creating the stimulus profile, run
 it.

Parent topic:

Configuring Failure Notification Using the Stimulus Profile Editor Tutorial

Related tasks:

- Creating a Real-Time Sequence to Return a Pass/Fail Value

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-read-write-channel.html language=enus -->
## TOPIC 00381: Reading and Writing Channels Directly from a Real-Time Sequence Tutorial

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-read-write-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-read-write-channel.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use channel references, parameters, and variables to turn on a car engine, set the engine speed to three different RPM values, measure how long the engine takes to settle at each specified RPM, and turn the engine off. You can use channel references to read/write channels in a system definition dire

### Reading and Writing Channels Directly from a
 Real-Time Sequence Tutorial

Use channel references, parameters, and variables to turn on a car
 engine, set the engine speed to three different RPM values, measure how long the engine takes
 to settle at each specified RPM, and turn the engine off.

Note

1. Deploy the Engine
 Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Create a real-time
 sequence with a channel reference—Create a real-time sequence that uses a channel
 reference to read/write a engine power channel and a parameter to specify the value to
 read/write.
3. Create a real-time
 sequence with channel references and local variables—Create a real-time sequence that uses channel references to
 measure how long the engine takes to settle at a specified RPM.
4. Create a stimulus
 profile that calls a channel referencing sequence—Configure a stimulus profile to turn on the engine and
 measure how long it takes the engine to settle at various RPMs.
5. Run the stimulus
 profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Setting up a Basic Stimulus Profile Editor Test

Related tasks:

- Deploying the Engine Demo
- Create a Real-Time Sequence with a Channel Reference
- Create a Real-Time Sequence with Channel References and Local Variables
- Creating a Stimulus Profile that Calls a Channel Referencing Sequence
- Running a Stimulus Profile

<!--NI_TOPIC bundle=veristand path=tutorial-stimulus-update-model-parameter.html language=enus -->
## TOPIC 00382: Updating Model Parameters During Test Execution Using the Stimulus Profile Editor Tutorial

- bundle_id: `veristand`
- source_path: `tutorial-stimulus-update-model-parameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-stimulus-update-model-parameter.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Call text files in a stimulus profile to update the values of engine model parameters while a test is running. Use the Update Model Parameters from File step in a stimulus profile to call text files. This step has similar functionality to the VeriStand Editor Model Parameter Manager tab and the Mode

### Updating Model Parameters During Test
 Execution Using the Stimulus Profile Editor Tutorial

Call text files in a stimulus profile to update the values of engine
 model parameters while a test is running.

Use the Update Model Parameters from File step
 in a stimulus profile to call text files. This step has similar
 functionality to the VeriStand Editor Model Parameter Manager tab
 and the Model Parameter Manager Workspace tool. The step can update
 the parameters of a deployed and running model.

Using the step removes the manual process of launching the tool, updating
 values, and applying those values. Also, because Update Model
 Parameters from File is a step, it executes inline with the rest of
 your stimulus profile code. This ensures that you can update your
 model at known points within the execution of the stimulus
 profile.

1. Deploy the Engine Demo—Deploy the engine demo's system definition before running a stimulus
 profile.
2. Update the stimulus profile to use a
 text file—Configure an existing stimulus profile to use a text file to
 update model parameters without having to create and run multiple profiles.
3. Run
 the stimulus profile—Compile and run the stimulus profile to see the real-time sequence interact
 with the Engine Demo.

Parent topic:

Getting Started with the Stimulus Profile Editor Tutorial

Related tasks:

- Deploying the Engine Demo
- Updating a Stimulus Profile to Use a Text File for Model Parameters
- Running a Stimulus Profile

Related reference:

- Update Model Parameters from File Step

<!--NI_TOPIC bundle=veristand path=tutorial-text-file-model-parameters.html language=enus -->
## TOPIC 00383: Updating a Stimulus Profile to Use a Text File for Model Parameters

- bundle_id: `veristand`
- source_path: `tutorial-text-file-model-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/tutorial-text-file-model-parameters.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure an existing stimulus profile to use a text file to update model parameters without having to create and run multiple profiles. Before you begin, deploy the engine demo's system definition. In the VeriStand Editor, click Tool Launcher Stimulus Profile Editor . Click File Open , navigate to

### Updating a Stimulus Profile to Use a Text File
 for Model Parameters

Configure an existing stimulus profile to use a text file to
 update model parameters without having to create and run multiple profiles.

Before you begin, deploy the engine demo's system
 definition.

1. In the VeriStand Editor, click Tool Launcher [IMAGE alt='image' src='GUID-2D8EDC61-EC6A-471E-97FB-6F21BE69741E-a5.png']»Stimulus Profile Editor.
2. Click File»Open, navigate to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Engine Demo
 Return Value, and double-click the Engine Demo Return Value stimulus
 profile.
3. Save the stimulus profile as Update Model Parameters tutorial in
 the <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Update Model
 Parameters directory.
4. Optional: 
 If you want to run the stimulus profile in the VeriStand Editor,
 update the Setup step.
  1. Right-click Open VeriStand Workspace and select
 Delete.
  2. In the Steps palette, expand Other and
 drag Command Shell into the Setup.
  3. In the Property Browser, specify the full path to
 VeriStand.exe as the Filename. 
 Note You can add arguments in the
 Property Browser for this step to specify the VeriStand
 project, system definition file, and VeriStand gateway IP address to connect
 to.
5. In the Steps palette, expand VeriStand Control»Workspace and drag Update Model Parameters from File into
 Main, above the Real-Time Sequence Call.
6. In the Property Browser, set Source to
 <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Update Model
 Parameters\OriginalParameterValues.txt 
 If you open this file in a text editor, you can see that it resets the three key
 parameters for testing purposes back to their initial values.
 a [-7/9 0.5; -2/3 0]
{environment temperature (C)} 25
{idle speed (RPM)} 900In
 this code, a is the A matrix for the engine state-space model,
 {environment temperature (C)} is the temperature of the environment
 in which the engine operates, and {idle speed (RPM)} is the RPM the
 engine maintains while idle. Note VeriStand expects parameter names to start with a
 letter and contain only alphanumeric characters or underscores. If a parameter name
 does not fit this convention, you can enclose it in curly braces ( { } ) to indicate
 that the string is a model parameter.
7. Select the Prompt Operator step that appears after the Real-Time Sequence Call and
 change the Message to Model parameters set to default
 values and the Dialog Title to New
 Parameter Values.
8. Add a second Update Model Parameters from File after the Prompt Operator, and set the
 Source to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Update Model
 Parameters\ParameterUpdate1.txt. 
 This file changes the environment temperature and the idle speed of the engine to very
 high values:
 {environment temperature (C)} 75
{idle speed (RPM)} 2000
9. Right-click the Prompt Operator you configured and select Copy.
10. Right-click Main, and select Paste to add
 another operator prompt to the end of section. Update its message to
 Environment temperature set to 75 and Idle RPM set to 2000.
11. Copy the Real-Time Sequence Call and paste it after the prompt. 
 Because you are running the same test on each update of the model, you do not need to
 configure the sequence.
12. Add a third Update Model Parameters from File after the Prompt Operator, and set the
 Source to <Common
 Data>\VeriStand Projects\Engine Demo\Stimulus Profiles\Update Model
 Parameters\ParameterUpdate2.txt. 
 This file demonstrates some more advanced operations:
 tempConversionFactor 0.5
{environment temperature (C)} 50 * tempConversionFactor
subscript subfile.txtThe
 first line declares a temporary variable, tempConversionFactor. The second line uses
 this variable in a calculation. Temporary variables are local to the file in which you
 create them.The third line uses the subscript command to call another text file
 subfile.txt. This subscript sets a few more parameter values.
 When you call a file as a subscript, VeriStand inserts the contents of the subscript
 file into the calling file at the line that contains the subscript call.
13. Create another Prompt Operator with the Message Environment temperature
 reset to 25 C and the 'a' matrix (which controls RPM adjustments) changed to model a
 different engine.
14. Copy and paste another call to the real-time sequence.
15. Optional: 
 If you want to ensure you leave your system in a known state, add another Update Model
 Parameters from File that calls OriginalParameterValues.txt.
16. Click Update Model Parameters tutorial.nivsstimprof and in the
 Property Browser disable Stop Execution on
 Fail.
17. Save the stimulus profile.

The stimulus profile code will look like the following image.

[IMAGE alt='image' src='GUID-13AAC7C1-69E6-42AB-B818-8D0E75EE911D-a5.png']

Note

ParameterUpdate1.txt

Parent topic:

Updating Model Parameters During Test Execution Using the Stimulus Profile Editor Tutorial

Related tasks:

- Communicating with the VeriStand Editor Using Stimulus Profile Arguments
- Running a Stimulus Profile

Related reference:

- VeriStand Directories and Aliases

<!--NI_TOPIC bundle=veristand path=uint32-array-variable.html language=enus -->
## TOPIC 00384: UInt32 Array Variable

- bundle_id: `veristand`
- source_path: `uint32-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/uint32-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of 32-bit unsigned integers. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use c

### UInt32 Array Variable

An array of 32-bit unsigned integers.

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

<!--NI_TOPIC bundle=veristand path=uint32-variable.html language=enus -->
## TOPIC 00385: UInt32 Variable

- bundle_id: `veristand`
- source_path: `uint32-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/uint32-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A 32-bit unsigned integer. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where

### UInt32 Variable

A 32-bit unsigned integer.

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

<!--NI_TOPIC bundle=veristand path=uint64-array-variable.html language=enus -->
## TOPIC 00386: UInt64 Array Variable

- bundle_id: `veristand`
- source_path: `uint64-array-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/uint64-array-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: An array of 64-bit unsigned integers. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use c

### UInt64 Array Variable

An array of 64-bit unsigned integers.

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

<!--NI_TOPIC bundle=veristand path=uint64-variable.html language=enus -->
## TOPIC 00387: UInt64 Variable

- bundle_id: `veristand`
- source_path: `uint64-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/uint64-variable.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: A 64-bit unsigned integer. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the variable in expressions. Evaluation Method Specifies whether to evaluate the parameter by value or by reference. ByReference is appropriate for most use cases, where

### UInt64 Variable

A 64-bit unsigned integer.

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

<!--NI_TOPIC bundle=veristand path=undeploy-system-definition.html language=enus -->
## TOPIC 00388: Undeploying the System Definition from an Individual Target

- bundle_id: `veristand`
- source_path: `undeploy-system-definition.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/undeploy-system-definition.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Remove a system definition from an individual target in VeriStand to disconnect the target. Undeploying the system definition from a target also disconnects the target. In the VeriStand Editor, click Tool Launcher Manage Targets . In the Tool window's Manage Targets tab, select the target or targets

### Undeploying the System Definition from an
 Individual Target

Remove a system definition from an individual target in VeriStand to disconnect the
 target.

Undeploying the system definition from a
 target also disconnects the target.

1. In the VeriStand Editor, click Tool Launcher»Manage Targets.
2. In the Tool window's Manage Targets
 tab, select the target or targets from which you want to undeploy the system
 definition.
3. Click Undeploy.

Manage Targets

State

Parent topic:

Individual Target Management

<!--NI_TOPIC bundle=veristand path=update-model-parameters-stimulus.html language=enus -->
## TOPIC 00389: Updating Model Parameters During a Stimulus Profile Test

- bundle_id: `veristand`
- source_path: `update-model-parameters-stimulus.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/update-model-parameters-stimulus.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Apply model parameter values from a text file to a simulation model during stimulus profile execution on a deployed target. By using this step to automate model parameter value updates, you can update your model at known points within the execution of the stimulus profile. Create a stimulus profile

### Updating Model Parameters During a Stimulus
 Profile Test

Apply model parameter values from a text file to a simulation model during
 stimulus profile execution on a deployed target.

By using this step to automate model
 parameter value updates, you can update your model at known points within
 the execution of the stimulus profile.

1. Create a
 stimulus profile that is associated with the system definition file
 that contains the model you want to update.
2. In the Steps palette, click to VeriStand Control»Workspace and drag the Update Model Parameters from
 File step to the stimulus profile code.
3. In the Property Browser, configure the
 Update Model Parameters from
 File step. 
 Note The Update Model Parameters from
 File step also supports
 .m files generated by the Model Parameter Manager workspace
 tool.
  1. Enter a Source path to a
 text file (.txt) that conforms to
 the model parameter file
 format.
  2. Confirm that the Target
 property shows the target that the model is
 deployed to.
  3. Confirm that the
 Delimiter property is set
 to the delimiter that the
 Source file uses to
 separate parameter/value pairs.
  4. If you are using an alias file to define model
 parameters, enter the path to the file in the
 Alias File property.
  5. If you are using temporary variables within the
 Source file, enable
 Allow Temporary
 Variables
4. Deploy the system definition.
5. Compile and run the stimulus profile.

Update Model Parameters from File

Source

Parent topic:

Creating Stimulus Profiles

Related concepts:

- Supported Syntax in Model Parameter Files

Related tasks:

- Creating Stimulus Profiles
- Importing and Managing Batches of Model Parameters in the Workspace

Related reference:

- Update Model Parameters from File Step

<!--NI_TOPIC bundle=veristand path=update-models-parametes-file.html language=enus -->
## TOPIC 00390: Update Model Parameters from File Step

- bundle_id: `veristand`
- source_path: `update-models-parametes-file.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/update-models-parametes-file.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates parameter values for a simulation model to the values specified in a text (.txt) file. Use this step to synchronize parameter value updates with real-time sequences without stopping the execution of a stimulus profile. Property/Section Description Source Specifies the path to the text file t

### Update Model Parameters from File
 Step

Updates parameter values for a simulation model to the values specified in a text
 (.txt) file.

Use this step to synchronize parameter value updates with real-time sequences without
 stopping the execution of a stimulus profile.

| Property/Section | Description |
| --- | --- |
| Source | Specifies the path to the text file that contains the new model parameter values. The source file contains a set of key/value pairs that represent model parameter names and the corresponding values to assign each parameter. This file must be a .txt file, and must follow the expected model parameter file format. This step also provides limited support for .m files that follow the exact format generated by the Model Parameter Manager Workspace tool. |
| Target | Specifies the name of the target, as it appears in the system definition file, on which the model executes. This step can only update model parameters on one target at a time. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |
| Advanced | Includes the following properties: Alias File—Specifies the path to an alias file to define mappings for aliased parameter names in the source file. Alias files allow you to easily reuse the same source file for multiple models. For example, you can write a source file with parameter names a, b, and c, and then use an alias file to map a, b, and c to parameters in the current model.Alias files must be .txt files that use the same Delimiter as the source file. Delimiter—Specifies the delimiter used to separate model parameter names and values in the source file and, if used, parameter aliases and names in the alias file: Tab (Default) Equals Comma Allow Temporary Variables—If True, specifies to allow temporary variables in the source file. For example, the following snippet defines a temporary variable, tempX, and then uses tempX in an expression that defines a model parameter value: tempX 0.5 {parameter} 10 * tempXNote Model parameter names and alias names are case-sensitive. You will not receive error messages for variables that do not map to model parameters. Instead, the step discards the corresponding value when updating model parameters. This step assumes that keys in the source file that do not match a model parameter name or an alias defined in the alias file are temporary variables. |

Parent topic:

Workspace Steps

Related concepts:

- Supported Syntax in Model Parameter Files

Related tasks:

- Importing and Managing Batches of Model Parameters in the Workspace

<!--NI_TOPIC bundle=veristand path=use-model-framework.html language=enus -->
## TOPIC 00391: Using the VeriStand Model Framework for Simulink

- bundle_id: `veristand`
- source_path: `use-model-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/use-model-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Run Simulink models written in C/C++ with the VeriStand Model Framework. Before you begin, install the VeriStand Model Framework on the computer you are compiling the model. The framework adds tools you will use during the compile process. You should also install a supported version of Simulink. For

### Using the VeriStand Model Framework for
 Simulink

Run Simulink models written in C/C++ with the VeriStand Model
 Framework.

VeriStand Model Generation Support and MathWorks
 Simulink® Compatibility

Note

Simulink Coder

1. Launch Simulink and load the model you want to convert.
2. Configure the model parameters with the following settings. 
 Stop time: inf
Type: Fixed-step
3. Generate the model code.
4. Optional: 
 If the model specifies any .c or .h files,
 include the locations of the source files and directories.
5. Based on your target’s operating system, select the correct TLC file and
 compiler. 
 OS
TLC File
CompilerWindows
NIVeriStand.tlc
Microsoft Visual C++
Note NI recommends installing
 Microsoft Visual Studio 2017 with C++ Development option enabled.
NI Linux Real-Time Intel x64-based targets
NIVeriStand_Linux_64.tlc
C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition
6. Build the model.

The MATLAB software command window displays the status of the
 build process and indicates when the Simulink Coder software has completed compiling the
 model.

After compiling, add the model to the system
 definition.

Parent topic:

Using Models from Simulink

Related concepts:

- VeriStand Model Framework

Related tasks:

- Adding and Configuring a Model

Related information:

- VeriStand Model Generation Support and MathWorks Simulink®
 Compatibility
- Simulink Coder

<!--NI_TOPIC bundle=veristand path=use-models-c.html language=enus -->
## TOPIC 00392: Using Models from C and C++

- bundle_id: `veristand`
- source_path: `use-models-c.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/use-models-c.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a model in C or C++ that NI software can load and execute through the VeriStand Model Framework. Before you begin, install the VeriStand Model Framework on the computer you are compiling the model. The framework adds tools you will use during the compile process. Based on the operating system

### Using Models from C and C++

Create a model in C or C++ that NI software can load and execute through the
 VeriStand Model Framework.

Before you begin, install the VeriStand Model Framework on the
 computer you are compiling the model. The framework adds tools you will use
 during the compile process.

1. Based on the operating system (OS), choose a compiler. 
 OS
CompilerWindows
Microsoft Visual C++
NI Linux RT x64
C/C++ Development Tools for NI Linux Real-Time, Eclipse
 Edition
2. Create a model header file—Create a model.h header
 file that contains the type definitions for model properties and all
 user-visible parameters in your model.
3. Adapt the template to model code—Use the template.c
 file that the VeriStand Model Framework installs as a starting point for
 your model code.
4. Create a makefile to compile model code—Create a makefile for the compiler
 and operating system your model will use.

.c

model.h

<RootDrive>\VeriStand\<xxxx>\ModelInterface\custom\examples

Note

<RootDrive>

<xxxx>

After compiling the model,
 add it to a system
 definition.

For more information on simulating models in LabVIEW with the Model Interface
 Toolkit, open LabVIEW and select Help»LabVIEW Help. Click Contents and browse to Toolkits»Model Interface Toolkit.

Parent topic:

Integrating and Executing Models

Related concepts:

- VeriStand Model Framework

Related tasks:

- Creating a Model Header File
- Adapting the C Template to Model Code
- Creating a Makefile and Compiling Model Code
- Adding and Configuring a Model

<!--NI_TOPIC bundle=veristand path=use-models-simulink.html language=enus -->
## TOPIC 00393: Using Models from Simulink

- bundle_id: `veristand`
- source_path: `use-models-simulink.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/use-models-simulink.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Simulink software to convert your model for use on real-time targets. Depending on your version of MathWorks Simulink Software, use one of the following resources to compile your model. Simulink Version Resource R2017b to R2020b VeriStand Model Framework For more information on how the framework

### Using Models from Simulink

Use Simulink software to convert your model for use on real-time
 targets.

Depending on your version of MathWorks Simulink® Software, use one of the
 following resources to compile your model.

| Simulink Version | Resource |
| --- | --- |
| R2017b to R2020b | VeriStand Model Framework Note For more information on how the framework and Simulink interact, refer to How Veristand Imports Simulink Models using the Model Framework. |
| R2020a and newer | VeriStand Model Generation Support MATLAB AddonNote For more information on how the addon and Simulink interact, refer to How Veristand Imports Models from the Model Generation Support MATLAB Add-on. |

After compiling the model,
 add it to a system
 definition.

Parent topic:

Integrating and Executing Models

Related concepts:

- How VeriStand Imports Simulink Models using the Model Framework
- How VeriStand Imports Models from the Model Generation Support MATLAB Add-on

Related tasks:

- Using the VeriStand Model Framework for Simulink
- Adding and Configuring a Model

Related information:

- VeriStand Model Generation Support MATLAB Addon

<!--NI_TOPIC bundle=veristand path=user-manual-welcome.html language=enus -->
## TOPIC 00394: VeriStand User Manual

- bundle_id: `veristand`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/user-manual-welcome.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### VeriStand
 User Manual

The VeriStand User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Dimensional Drawings
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center
- Download VeriStand
- License Setup and Activation
- Installing, Updating, Repairing, and Removing NI
 Software
- VeriStand Release Notes
- VeriStand .NET API Help

<!--NI_TOPIC bundle=veristand path=using-models-labview.html language=enus -->
## TOPIC 00395: Using Models from LabVIEW VIs

- bundle_id: `veristand`
- source_path: `using-models-labview.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/using-models-labview.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Convert LabVIEW VIs into compiled .lvmodel or .lvmodelso files. Before you begin, verify VeriStand supports your hardware target and prepare your LabVIEW VIs for conversion.In order to generate compiled models from LabVIEW VIs, you need the following products:LabVIEW development system that is the s

### Using Models from LabVIEW VIs

Convert LabVIEW VIs into compiled .lvmodel or
 .lvmodelso files.

- LabVIEW development system that is the same year version as your VeriStand
 installation.
- LabVIEW Application Builder

You can convert LabVIEW VIs or simulation
 subsystems you create using the LabVIEW Control Design and Simulation Module. The
 converted files add system simulation, closed-loop control, and other functionality to
 VeriStand applications.

1. In LabVIEW, select Tools»NI VeriStand»Generate Model from VI.
2. On the Generate NI VeriStand Model from VI dialog box,
 enter the Source VI Path where you saved the source
 file.
3. Enter a Destination Folder where you want to save the
 generated model.
4. Optional: 
 If your source file is a simulation subsystem, click
 Next.
  1. Specify a model time step (sec) that indicates
 the interval between the times the ODE Solver evaluates the model and
 updates the model output. 
 Note For your compiled
 model to run in real-time, the model time step (sec) value must
 equal the controller period multiplied by the model Decimation, or
 the model Decimation divided by the Target Rate. These two methods
 are represented by the following equations. model time step (sec) = Controller Period *
 Decimation where Controller Period =
 1/Target Ratemodel time step (sec) = Decimation/Target
 RateIn System Explorer, use the
 Controller Configuration page to
 specify the Target Rate and the
 Model Configuration page to specify the
 Decimation.
  2. Specify the ODE Solver.
5. Click Build. 
 Note If you experience errors
 when converting a VI, refer to LabVIEW VI Model
 Conversion Preparation.

.lvmodel

.lvmodelso

.dll

- A .depvs file that LabVIEW creates to reference the
 dependencies.
- Any LabVIEW .dll located in a subdirectory named
 data in the destination folder where LabVIEW generates the
 compiled model.

Parent topic:

Integrating and Executing Models

Related concepts:

- LabVIEW VI Model Hardware Target Support
- LabVIEW VI Model Conversion Preparation

Related information:

- LabVIEW Application Builder

<!--NI_TOPIC bundle=veristand path=using-workspace.html language=enus -->
## TOPIC 00396: Running the VeriStand Workspace

- bundle_id: `veristand`
- source_path: `using-workspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/using-workspace.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Launch the Workspace to run a project, view and modify the user interface, and to perform operations such as monitoring alarms, viewing channel data, scaling and calibrating channels, and running stimulus profiles. Open a project in VeriStand. In the Project Files tab, double-click Workspace. Depend

### Running the VeriStand Workspace

Launch the Workspace to run a project, view and
 modify the user interface, and to perform operations such as monitoring alarms, viewing
 channel data, scaling and calibrating channels, and running stimulus
 profiles.

1. Open a project in VeriStand.
2. In the Project Files tab, double-click
 Workspace.
3. Depending on your goal, complete any of the following tasks in the
 Workspace. 
 Goal
TaskAdding
 and configuring controls and indicators
Use the
 Workspace Controls palette to
 add and configure controls and indicators to create a
 user interface.
Modifying control mappings at run time
Change the channel
 mapping of a control or indicator while the
 Workspace runs.
Calibrating a hardware channel at run
 time
Use the
 Channel Calibration tool to
 calibrate hardware channels by adjusting the values they
 return to known values while a system definition
 runs.
Using
 channel value forcing
Use the
 Channel Fault Manager tool to
 test the behavior of a system when a channel reaches a
 certain value.
Logging
 test results with stimulus profiles
Use the
 Stimulus Profile Editor to
 create and execute a stimulus profile on your host
 machine to log test data acquired from real-time
 sequences performed on a target.
Recording commands sent to the
 target
Use the Macro
 Recorder tool to record commands, such as
 the setting of channel or parameter values, model
 execution states, and fault or alarm values, that
 VeriStand sends to the target and save them to a macro
 (.nivsmacro) file.
Playing back commands sent to the
 target
Use the Macro
 Player tool to review the commands that
 VeriStand sent to the target using the macro
 (.nivsmacro) file you recorded
 with the Macro Recorder
 tool.
Setting model parameter values in the
 Workspace
Use model
 calibration controls in the
 Workspace to view and modify
 the values for any model parameters in the system
 definition.
Importing and managing batches of model
 parameters
Use the
 Model Parameter Manager tool to
 import and apply model parameter values defined in
 external .m or
 .txt files to a
 model.
Displaying waveform data in a graph
Use a waveform graph
 control to display data from one or more waveforms in
 the system definition file to monitor and verify
 acquired data.
Enhancing your Workspace to view data
Use other tools,
 such as the Alarm Monitor,
 TDMS File Viewer, and
 XNET Bus Monitor, to view data
 in the Workspace.
Configuring and Executing host-side
 logging
Use the
 Data Logging control to
 adjust log times, better format data files, select start
 and stop times, and more at run time.

Parent topic:

Visualizing System State

Related tasks:

- Adding and Configuring Controls and Indicators
- Modifying Control Mappings at Run Time
- Calibrating a Hardware Channel at Run Time
- Using Channel Value Forcing
- Logging Test Results with Stimulus Profiles
- Recording Commands VeriStand Sends to the Target
- Playing Back Commands Sent to the Target
- Setting Model Parameter Values in the Workspace
- Importing and Managing Batches of Model Parameters in the Workspace
- Displaying Waveform Data in a Graph
- Enhancing Your Workspace to View Data
- Configuring and Executing Host-Side Logging

<!--NI_TOPIC bundle=veristand path=using-xnet-frame-id.html language=enus -->
## TOPIC 00397: Using NI-XNET Frame IDs

- bundle_id: `veristand`
- source_path: `using-xnet-frame-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/using-xnet-frame-id.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: NI-XNET frame IDs uniquely identify frames on the network. Use frame IDs to prioritize event-triggered transmission, filter log files, and filter CAN replay data. The frames that transmit across the network are assigned unique identifiers. You can use these frame IDs for more than just identifying t

### Using NI-XNET Frame IDs

NI-XNET frame IDs uniquely identify frames on the network. Use frame IDs to prioritize
 event-triggered transmission, filter log files, and filter CAN replay data.

Note

NI-XNET
 Hardware and Software Help

1. Launch your project in the VeriStand Editor.
2. In the Project Files pane, left-click a system definition file
 (.nivssdf) and select Configure in System
 Explorer.
3. Depending on your goal, complete any of the following tasks. 
 Goal
TasksPrioritizing the order that event-triggered outgoing
 frames transmit.
Add a CAN, FlexRay, or LIN
 port.
Click the port you added.
On the port configuration page, click the
 Transmission Order tab.
Under Pending Transmit Order, click By
 Identifier.
Filtering specific frame IDs to include or exclude from
 the log file.
Set up logging for incoming NI-XNET
 frames.
Click the XNET logging file you added.
Use the XNET Data Logging
 Configuration page to configure
 filtering in the Data Logging Settings section.
Filtering CAN data replay file frames to specify frame
 IDs to include or exclude from replay.
Add a CAN data replay
 file.
Click the data replay file you added.
In the File Replay IDs section, use the
 File Replay Configuration
 page to configure filtering.
4. Save the system definition file.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Adding a CAN, FlexRay, or LIN Port
- Logging Incoming NI-XNET Frames
- Replaying Logged NI-XNET CAN Frame Data

<!--NI_TOPIC bundle=veristand path=using-xnet-interfaces.html language=enus -->
## TOPIC 00398: Using NI-XNET Interfaces

- bundle_id: `veristand`
- source_path: `using-xnet-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/using-xnet-interfaces.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Use NI-XNET interfaces to communicate and interact with applications that require real-time, high-speed manipulation of hundreds of Controller Area Network (CAN), Local Interconnect Network (LIN), and FlexRay frames and signals. Popular application types to use the NI-XNET platform include hardware-

### Using NI-XNET Interfaces

Use NI-XNET interfaces to communicate and interact with applications that require
 real-time, high-speed manipulation of hundreds of Controller Area Network (CAN), Local
 Interconnect Network (LIN), and FlexRay frames and signals.

Popular application types to use the NI-XNET platform include
 hardware-in-the-loop (HIL) simulation, rapid control prototyping, bus monitoring,
 and automation control.

The NI-XNET
 platform includes a series of high-performance CAN, LIN, and FlexRay
 communication protocol interfaces used by automotive and industrial networks.

Depending on your goal, complete any of the following tasks.

| Goal | Task |
| --- | --- |
| Add an NI-XNET database | Create a standardized file for embedded system communication in a FIBEX (.xml), CANdb (.dbc), NI-CAN (.ncd), or LDF (.ldf) format. |
| Edit an NI-XNET database | Use the NI-XNET Database Editor to configure a basic network, define frames and exchanged signals, and assign frames to Electronic Control Units (ECUs). |
| Import NI-XNET frames | Import incoming or outgoing frames from an NI-XNET database. |
| Use NI-XNET frame IDs | Use frame IDs to prioritize event-triggered frames, filter log file frames, and filter CAN data replay file frames. |
| Access timing and ID information for incoming NI-XNET frames | Create Frame Information channels to track timestamps and frame IDs. |
| Log incoming NI-XNET frames | Create TDMS (.tdms) or NI-XNET log (.ncl) files to record incoming frame data during an NI-XNET session. |
| Replay logged NI-XNET CAN frame data | Add and replay TDMS (.tdms) or NI-XNET log (.ncl) files on a CAN bus. |
| Configure cyclic NI-XNET CAN frame faulting | Configure outgoing cyclic frames of NI-XNET CAN interfaces by adding Skip Cyclic Frames and Transmit Time channels. |
| Configure cyclic redundancy checks (CRCs) and counters for outgoing NI-XNET CAN frames | Specify the bytes for outgoing frames of NI-XNET CAN interfaces to include in CRCs and add counters that increment each time the frame transmits across the bus. |

Parent topic:

Running Tests

Related concepts:

- NI-XNET Overview
- NI-XNET Bus Monitor
- How VeriStand Applies Scaling Factors to NI-XNET Signals

Related tasks:

- Adding NI-XNET Databases
- Editing NI-XNET Databases
- Importing NI-XNET Frames
- Using NI-XNET Frame IDs
- Accessing Timing and ID Information for Incoming NI-XNET Frames
- Logging Incoming NI-XNET Frames
- Replaying Logged NI-XNET CAN Frame Data
- Configuring NI-XNET CAN Cyclic Frame Faulting
- Configuring Cyclic Redundancy Checks (CRCs) and Counters for Outgoing NI-XNET CAN Frames

Related information:

- NI-XNET CAN, LIN, and FlexRay Platform Overview

<!--NI_TOPIC bundle=veristand path=variables-primitives.html language=enus -->
## TOPIC 00399: Variables Primitives

- bundle_id: `veristand`
- source_path: `variables-primitives.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/variables-primitives.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Variables primitives create and configure variables for real-time sequences, including Boolean and numeric types. Use array variables primitives to define arrays of a specific data type. Drag a variable to the Variables pane to configure its properties. You can drag most variables directly to the se

### Variables Primitives

Variables primitives create and configure variables for real-time sequences,
 including Boolean and numeric types. Use array variables primitives to define arrays of a
 specific data type.

Drag a variable to the Variables pane to configure its
 properties. You can drag most variables directly to the sequence code to create an
 expression that sets the value of a variable.

| Palette object | Description |
| --- | --- |
| Boolean | A Boolean value. |
| Double | A double-precision, floating point number. |
| Int32 | A 32-bit signed integer. |
| Int64 | A 64-bit signed integer. |
| UInt32 | A 32-bit unsigned integer. |
| UInt64 | A 64-bit unsigned integer. |
| Void Return Value | Returns void, or no value, when used as the return variable for a real-time sequence. |

| Subpalette | Description |
| --- | --- |
| Array Variables Primitives | Use the Array Variables primitives to create variables that are arrays of values of a certain data type. |

Parent topic:

Real-Time Sequence Primitives

Related reference:

- Boolean Variable
- Double Variable
- Int32 Variable
- Int64 Variable
- UInt32 Variable
- UInt64 Variable
- Void Return Value
- Array Variables Primitives

<!--NI_TOPIC bundle=veristand path=veristand-control-steps.html language=enus -->
## TOPIC 00400: VeriStand Control Steps

- bundle_id: `veristand`
- source_path: `veristand-control-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-control-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Explore the use of VeriStand Control steps to manage projects and interact with Workspace tools. For example, you can use Control steps to open and close the project, open and close the Workspace, and access Workspace tools. Palette object Description Launch NI VeriStand Launches the VeriStand execu

### VeriStand Control Steps

Explore the use of VeriStand Control steps to manage projects and interact with
 Workspace tools.

For example, you can use Control steps to open and close the project, open and close the
 Workspace, and access Workspace
 tools.

| Palette object | Description |
| --- | --- |
| Launch NI VeriStand | Launches the VeriStand executable. |

| Subpalette | Description |
| --- | --- |
| Project Steps | Open, communicate with, or close a VeriStand project (.nivsprj) file. |
| Workspace Steps | Interact with the Workspace and Workspace tools. |

Parent topic:

Stimulus Profile Steps

Related reference:

- Launch NI VeriStand Step
- Project Steps
- Workspace Steps

<!--NI_TOPIC bundle=veristand path=veristand-directories-aliases.html language=enus -->
## TOPIC 00401: VeriStand Directories and Aliases

- bundle_id: `veristand`
- source_path: `veristand-directories-aliases.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-directories-aliases.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand uses directories and aliases for project files, models, and custom devices. The following tables list paths to common VeriStand directories by operating system. The heading before each table indicates how NI documentation refers to the directory. For directories with aliases listed, the al

### VeriStand Directories and Aliases

VeriStand uses directories and aliases for project files, models, and custom
 devices.

Note

#### <Common
 Data>

Alias: To Common Doc Dir

| Operating system | Path |
| --- | --- |
| Windows | <Public Documents>\\National Instruments\\NI VeriStand <xxxx> |

Note

<xxxx>

#### <Application Data>

Alias: To Application Data
 Dir

For internal use only. Certain custom device development tools,
 including Custom Device XML and the Device Properties VIs, can reference this
 directory. However, NI recommends you avoid storing or modifying files in this
 directory.

| Operating system | Path |
| --- | --- |
| Windows | <Application Data>\\National Instruments\\VeriStand |

#### <Base>

Alias: To Base

| Operating system | Path |
| --- | --- |
| Windows | <Program Files>\\National Instruments\\VeriStand <xxxx> |

Note

<xxxx>

#### <Custom
 Device Engine Destination>

Alias: None

| Operating system | Path |
| --- | --- |
| Phar Lap/ETS | C:\\ni-rt\\NIVeristand\\custom devices\\<custom device name>\\ |

#### <Model
 Framework>

Alias: None

| Operating system | Path |
| --- | --- |
| Windows | C:\\VeriStand\\<xxxx>\\ModelInterface |

Note

<xxxx>

Parent topic:

VeriStand Environment

Related tasks:

- Creating an Alias

<!--NI_TOPIC bundle=veristand path=veristand-editor-channel-faulting.html language=enus -->
## TOPIC 00402: Faulting a Channel to a Specific Value

- bundle_id: `veristand`
- source_path: `veristand-editor-channel-faulting.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-editor-channel-faulting.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Fault a channel with the Channel Fault Manager to test the behavior of a system when a channel reaches a specific value. Before you begin, you must add and connect to a system definition file in order to use VeriStand Editor tools. In the VeriStand Editor, click View Channel Fault Manager . In the C

### Faulting a Channel to a Specific Value

Fault a channel with the Channel Fault Manager to
 test the behavior of a system when a channel reaches a specific value.

Before you begin, you must add and connect to a system definition file in order to use
 VeriStand Editor tools.

1. In the VeriStand Editor, click View»Channel Fault Manager.
2. In the Channel Fault Manager pane, click Add
 Fault, and select the channel you want to fault. 
 Note You can select multiple
 channels and fault all the selected channels to a single value.
3. In the 
 Value field, enter the value to which you want to force the channel, and then click 
 OK. 
 Channel Fault Manager saves the value as a pending value.
4. Verify the value and click 
 Apply Pending Changes to apply the value.

VeriStand forces the channel to the value you specified.

Pending
 Value

Apply
 Pending Changes

Parent topic:

Tailoring Channels

Related tasks:

- Adding and Activating a System Definition File

<!--NI_TOPIC bundle=veristand path=veristand-editor-logging-data.html language=enus -->
## TOPIC 00403: Logging Data with the VeriStand Editor

- bundle_id: `veristand`
- source_path: `veristand-editor-logging-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-editor-logging-data.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create logging specification (.nivslspec) files with Log Management to configure and execute host-side data logging. You can add and configure logging specifications after connecting to a deployed system definition. This enables you to adjust which channels to log, when to start and stop logging, an

### Logging Data with the VeriStand Editor

Create logging specification (.nivslspec)
 files with Log Management to configure and execute host-side data
 logging.

You can add and configure logging specifications after
 connecting to a deployed system definition. This enables you to adjust which channels to
 log, when to start and stop logging, and the format of log files produce by the control.
 You can also configure logging specifications to automate post-processing actions, such
 as merging log data or producing reports, for log files produced during a log session.

1. In the VeriStand Editor, click View»Tool Launcher»Log Management.
2. Use the following sections of the VeriStand Editor to add and configure a
 logging specification file. 
 [IMAGE alt='image' src='GUID-BF6E6776-08C6-4643-B2C7-C50DA35F5FB1-a5.png'] 

 1
 Logging Specification—The logging specification file
 appears in the Files pane under the current project.
 Select the logging specification file you want to configure.
 To create a new logging specification file, right-click the project file and
 select Add New»Logging Specification.
 2
 Logging specification file screen—When you open a logging
 specification file in VeriStand, the file is displayed in a screen. Use the
 screen to add channels to log.
 3
 Configuration—Contains various options for configuring
 the log session, such as when to start and stop logging, how to save the log
 files, and options for post processing of log files.
 4
 Log Management—Displays all of the logging
 specification files in your project. Use the Log
 Management tool to view the state of logging specifications and
 to manually start and stop logging sessions.
 To display this tab, click Log Management in the
 Tool Launcher.
 5
 Execution Control section—Contains
 Start and Stop options for the
 selected logging specification file.
 Click Start to begin a log session. If you specified
 to log immediately, logging begins after you click
 Start. If you created a start trigger, logging begins
 after the specified condition is triggered.
3. Save the logging specification file.

Parent topic:

VeriStand Editor Tools

<!--NI_TOPIC bundle=veristand path=veristand-editor-manage-model-parameters.html language=enus -->
## TOPIC 00404: Importing and Managing Batches of Model Parameters with the VeriStand Editor

- bundle_id: `veristand`
- source_path: `veristand-editor-manage-model-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-editor-manage-model-parameters.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Import and apply batches of model parameter values from external text files by using the VeriStand Editor Model Parameter Manager. Before you can work with model parameters, you must deploy and connect to a system definition and understand model parameter syntax. Maintaining model parameter values i

### Importing and Managing Batches of Model
 Parameters with the VeriStand Editor

Import and apply batches of model parameter values from external text files by using
 the VeriStand Editor Model Parameter Manager.

Before you can work with model parameters, you
 must deploy and connect to a system definition and understand model parameter syntax.

Maintaining model parameter values in external files allows you to quickly switch between
 batches of test parameters without manually entering the values. This tool is also
 useful for managing multiple parameters from a single interface.

Setting the value of a parameter is a two-step process: importing or calculating new values, and then applying the new values.

1. In the VeriStand Editor, click View»Model Parameter Manager.
2. In the Model Parameter Manager pane, click
 Import File.
3. In the Configure Parameter Import dialog box, select
 Parameter File Path and browse to the
 .txt file that contains parameter values.
  1. If aliases define the parameters in the file, select Alias
 File Path and browse to the alias file.
4. Click OK to import the values from the file as pending
 values.
5. Verify the values and click 
 Apply Pending Changes to apply the values.

Pending Value

Apply Pending Changes

Parent topic:

VeriStand Editor Tools

Related concepts:

- Supported Syntax in Model Parameter Files

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=veristand-editor-mapping-ctrls.html language=enus -->
## TOPIC 00405: Configuring Controls and Indicators to Send and Receive Data

- bundle_id: `veristand`
- source_path: `veristand-editor-mapping-ctrls.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-editor-mapping-ctrls.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a screen to send a receive data by mapping controls and indicators to a channel in the system definition. A screen contains various components that allow a user to send data to a system definition as well as receive data from it. These components are called controls and indicators. 1 Lock—

### Configuring Controls and Indicators to Send and Receive Data

Configure a screen to send a receive data by mapping controls and indicators to a
 channel in the system definition.

A screen contains various components that allow a user to send data to a system
 definition as well as receive data from it. These components are called
 *controls* and *indicators*.

[IMAGE alt='image' src='GUID-D70EBCE6-7042-47CF-8653-67EAD83CBEF2-a5.png']

| 1 | Lock—Locks the screen, making it easier to send and receive data with controls and indicators by preventing the controls from being edited while you operate them. Note You can also operate controls while locked. However, you have to select the control before you can operate it. |
| --- | --- |
| 2 | System definition tree—Displays the configuration tree of the current system definition. You can navigate the tree to select the channel you want to map with the control or indicator. |
| 3 | Data source—Displays the path of the channel currently mapped to the control or indicator. The channel path is only visible when you select a control or indicator on the screen. |

Parent topic:

Visualizing System State

<!--NI_TOPIC bundle=veristand path=veristand-editor-view-signal-values.html language=enus -->
## TOPIC 00406: Viewing Model Values in the VeriStand Editor

- bundle_id: `veristand`
- source_path: `veristand-editor-view-signal-values.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-editor-view-signal-values.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Check signal values with the Model Signal Viewer without importing the signal as a channel or editing the system definition file. In the VeriStand Editor, click View Tool Launcher Model Signal Viewer . In the Model Signal Viewer tab, click Select Signals. In the Select Signals dialog box, click the

### Viewing Model Values in the VeriStand
 Editor

Check signal values with the Model Signal
 Viewer without importing the signal as a channel or
 editing the system definition file.

1. In the VeriStand Editor, click View»Tool Launcher»Model Signal Viewer.
2. In the Model Signal Viewer tab, click
 Select Signals.
3. In the Select Signals dialog box, click
 the signals you want to view and click
 OK. 
 Note Only
 select signals that you need immediate information
 on. Adding too many signals will decrease the
 VeriStand Engine’s execution loop rate. For every
 500 signals displayed, there is an expected 1% drop
 in performance.

Path

Value

Model Signal Viewer

Parent topic:

VeriStand Editor Tools

<!--NI_TOPIC bundle=veristand path=veristand-error-codes.html language=enus -->
## TOPIC 00407: VeriStand Error Codes

- bundle_id: `veristand`
- source_path: `veristand-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-error-codes.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand returns an error code when it encounters a problem while executing. Use the following table to locate an error code message. For more information on correcting VeriStand errors, refer to the NI KnowledgeBase. Error code Message -307500 The FPGA configuration file (.fpgaconfig) is invalid o

### VeriStand Error Codes

VeriStand returns an error code when it encounters a problem while
 executing.

Use the following table to locate an error code message.

Note

NI KnowledgeBase

| Error code | Message |
| --- | --- |
| -307500 | The FPGA configuration file (.fpgaconfig) is invalid or contains an error. |
| -307501 | The specified operation is unable to acquire the memory necessary to execute. To correct this error, increase the amount of memory in the system or reduce the amount of memory that this operation requires. You can reduce the amount of memory required by the operation by uninstalling unneeded components from the real-time (RT) target or by reducing the number of devices, channels, and/or stimulus generators used. |
| -307502 | An FPGA argument or parameter is invalid. This might be a problem with the FPGA configuration file (.fpgaconfig) or FPGA bitfile. This problem also might be caused by an invalid FPGA target handle. |
| -307503 | An unknown exception occurred while running the NI FPGA device. Verify that NI-RIO and the VeriStand software are installed correctly on the real-time (RT) target. |
| -307504 | An FPGA argument or parameter is outside the expected range. Update the FPGA configuration file (.fpgaconfig). |
| -307505 | The FPGA bitfile has changed since the system definition file was last compiled. Open the system definition file in System Explorer and refresh the FPGA configuration file (.fpgaconfig). |
| -307510 | Framework with the given name already exists. |
| -307511 | EESPort with the given name already exists. |
| -307512 | An unexpected step error has occured. |
| -307525 | Cannot open selected file. The file was saved in a later version of VeriStand. |
| -307526 | The XML file provided is invalid. |
| -307548 | Legacy Stimulus Profile Editor is not supported anymore. |
| -307549 | Cannot find the wave file that an alarm response is configured to play when the alarm is triggered. Verify that wave files are located at their specified locations. |
| -307550 | You have provided an invalid username or password. |
| -307551 | Internal error. The buffered data system failed to find required information in the transaction's variant data. |
| -307552 | Internal error. An attempt was made to open a 2D waveform read session. |
| -307553 | Unexpected waveform data type. This VI requires the specified waveform nodes to be of a specific data type. |
| -307554 | The specified stream condition is not valid for the data type of the waveform. This error might occur if you try to set the streaming condition to be within a range of values for a waveform whose data type is a complex double (CDB). The in-range streaming condition supports only waveforms whose data type is double (DBL). |
| -307555 | Cannot open a waveform session using an empty array of waveform references. Use the Get Waveform Data Reference VI to generate valid data references with which you can open a waveform session. |
| -307556 | Cannot open waveform session because waveform data references are not valid. Use the Get Waveform Data Reference VI to generate valid data references with which you can open a waveform session. |
| -307557 | Custom device cannot perform requested operation because VeriStand Engine is shutting down. |
| -307559 | The size of an input array does not match the number of waveforms in the streaming session. When you write to a multiple-waveform session, the number of rows in the 2D Data array must match the number of waveforms in the session. When you start a multiple-waveform session, the size of the 1D t0s array must match the number of waveforms in the session. |
| -307561 | Cannot write to waveform. Another waveform write session is already open for this waveform reference, and only one writer can access the waveform reference at a time. |
| -307562 | The waveform session reference cannot be used if it is not open. Use the Open Waveform Session VI to open a waveform session reference. |
| -307600 | The specified VI is broken and cannot run. Open the VI in LabVIEW for more information. |
| -307601 | The XML file is invalid according to the XML schema document (XSD). |
| -307602 | The GUID could not be found. If the requested page is a custom device, contact the creator of the custom device. |
| -307603 | The requested custom device does not have a main page specified. Contact the creator of the custom device to correct this error. |
| -307604 | VeriStand cannot mutate the system definition file to the current version. |
| -307605 | The requested simulation model could not be found. Navigate to the Model Configuration page in System Explorer and choose a different model. |
| -307606 | The file does not contain a valid file format. |
| -307607 | VeriStand could not mutate the system definition file. The system definition file version is different from the official released version of VeriStand. |
| -307608 | The custom device does not provide a valid source distribution for the target specified. Specify a different target or contact the creator of the custom device for further support. |
| -307609 | The formula contains an unused variable declaration. |
| -307610 | The formula contains an invalid function or variable name. |
| -307611 | The associated NI-XNET database path cannot be found. Update either the alias or the database path. |
| -307612 | One or more chassis are unidentified. Open NI MAX and identify the type of the chassis for each controller that is configured in System Explorer. |
| -307613 | You cannot add channels of the type you selected. The DAQ device either contains no channels of this type, or all available channels of this type are already in the system definition. |
| -307614 | The DAQ support files are missing for the channel type selected. Try repairing your installation of VeriStand. |
| -307615 | This DAQ device does not support reference clock synchronization. In System Explorer on the DAQ Device Configuration page, click the PXI Backplane Reference Clock drop-down and select None or Automatic. |
| -307616 | The associated NI-XNET signal has been deleted from the XNET database or it changed so it no longer matches the system definition. If the database no longer contains the signal, delete the signal from the system definition. If the signal changed in the database, reimport the signal. |
| -307617 | The system definition contains aliases that are not linked to any channel. Click on the Error/Warning icon on System Explorer to get a list of aliases that are not linked and either link them to a channel or delete them. |
| -307621 | The request at the specified index does not have the same number of signals as the signal_num parameter. Call the GetNextCompletedRequest method to get a valid index and signal number of a completed request. |
| -307622 | The specified request was not completed. Call the GetNextCompletedRequest method to get a valid index to a completed request. |
| -307623 | The specified request index is not valid. Call the GetNextCompletedRequest method to get a valid index to a completed request |
| -307624 | No proper request was found. Call the GetNextCompletedRequest method after the model executes a step to get the index of a completed request. |
| -307625 | An error occurred while reading the signal values. |
| -307626 | One or more of the specified signals are not scalar. Only scalar signals can be viewed. |
| -307627 | One or more of the specified signal indexes are not valid. Use signal indexes that are in the model. |
| -307628 | There is not enough space on the target to read the signal values. Ensure you are not viewing signal values from paused models. |
| -307629 | A required input or output parameter for this method is null. Use allocated variables for parameters. |
| -307630 | The model refnum is not valid. Use the InitializeLibrary function to return a valid refnum. |
| -307650 | An unexpected error has occurred in the VeriStand API. |
| -307651 | The VeriStand API does not support this function. |
| -307652 | Failed to open a connection to VeriStand.exe. |
| -307653 | The input file parameter is invalid or does not exist. Ensure that this path is correct and that the file has not been removed. |
| -307654 | Cannot perform this request because VeriStand is not running a system definition file. Deploy a system definition file, and try again. |
| -307655 | Invalid request. VeriStand is missing an engine component that is required to process the request. |
| -307656 | Invalid request. VeriStand does not have a system definition file loaded. |
| -307657 | The specified password does not match the current deployed configuration password. |
| -307658 | VeriStand is unable to run the system definition file when a system definition file is already running. |
| -307659 | Invalid password input parameter. The password cannot be an empty string. |
| -307660 | Timeout occurred while deploying a new system definition file. |
| -307661 | VeriStand failed to deploy the system definition file. |
| -307662 | Node is not found in the system. |
| -307663 | Timeout occurred while processing request. |
| -307664 | Channel does not have read access. |
| -307665 | Channel does not have write access. |
| -307666 | The specified channel cannot be faulted. |
| -307667 | The requested operation on this item reference is invalid. |
| -307668 | The specified channel cannot be scaled. |
| -307669 | The license is unavailable, invalid, or VeriStand failed to initialize the licensing component. |
| -307670 | The VeriStand Gateway cannot process the requested operation. The VeriStand Gateway currently is busy performing another operation. |
| -307671 | The execution host is running a different system definition file than the file specified. You must deploy the system definition file in order to connect to the execution host. |
| -307672 | One or more targets failed to start within the specified timeout. Verify that any start trigger or clock signals are configured correctly. |
| -307673 | Another VeriStand Gateway already is connected to the execution host. Only one VeriStand Gateway can be connected to an execution host at a time. |
| -307674 | The Run Workspace function is no longer supported. Use the Connect to System function instead, which has a system definition file parameter instead of a workspace file. |
| -307675 | The VeriStand Gateway cannot complete the specified operation because the number of streamed channels for one or more targets exceeds the maximum size. Stop data logging configurations or graphs to reduce the number of streamed channels. You also can increase the maximum streamed channel count for the targets by editing the system definition file in System Explorer. |
| -307676 | VeriStand cannot open the specified project file because another project is already open. |
| -307677 | The reference to the project file is no longer valid. The referenced project is no longer open. |
| -307678 | The specified workspace tool VI is not open. |
| -307679 | The VeriStand Gateway is no longer connected to the targets. One of the targets stopped running the system definition file. |
| -307680 | An exception occurred when the model parameter file was being parsed. |
| -307681 | Failed to read the VeriStand service configuration file. Repair your VeriStand installation. |
| -307682 | Could not complete one or more requests because a target is offline. A target is no longer connected and is not running the system definition. Any future requests for this target will not be completed. |
| -307683 | Cannot deploy or connect to the system definition because all targets in the system are disabled. Enable one or more targets in the system definition, and then try to deploy again. |
| -307684 | Cannot start server because the port address is already in use by another process. To change the port address for the server, select Tools » Options, browse to the Port Settings page, and change the value of the corresponding control. |
| -307685 | Cannot initialize model parameter(s) defined in model parameter file because parameter was not found in system. 1) Ensure the expression of the parameter is spelled correctly in the file. 2) If the file defines a temporary variable, ensure the system definition allows temporary variables. 3) If the file contains aliases, ensure the path to an alias file is correct in the system definition. Verify the contents of the file and the settings on the Simulation Models configuration page in System Explorer, and try again. |
| -307686 | The specified target is not defined in the deployed system definition. |
| -307687 | The given number of channels and number of values do not match. |
| -307688 | Timeout occurred while reconnecting a target to the gateway. |
| -307689 | The specified target is disabled. Change the target settings in the system definition and redeploy if you wish to use this target. |
| -307690 | To reconnect to a target without deploying, the restart action for real-time (RT) targets must be set to Run System Definition. To enable the Run System Definition restart action, select the System Initialization node in the System Explorer and select Run System Definition. You must redeploy the system definition to make use of these changes. |
| -307691 | Import operation failed for the specified SLSC chassis. |
| -307692 | VeriStand encountered an unknown internal error while using WebDAV. Check your target's disk to determine if it is full. |
| -307700 | One or more Model Execution Loops failed to shut down properly. |
| -307701 | Timeout occurred while writing a parameter value to the VeriStand Engine. |
| -307702 | The size of the imported model data in the system definition file conflicts with the size in the specified model file. This error can occur if the model file contains a different number of inports, outports, signals, or parameters than when it was imported. This error also can occur if two or more models contain a global parameter with the same name but different dimensions. To correct this error, reload the model in the System Explorer and verify the dimensions of any global parameters that multiple models contain. Alternatively, on the Parameters page for a model in the Scope for Global Parameters drop-down, select Model to avoid conflicts caused when the model shares the global parameter with other models. |
| -307703 | The specified model is incompatible with VeriStand. If you want to deploy the model to an RT target, launch the Console Viewer tool to display the console output of the target, which includes information about the source of the error. |
| -307704 | The specified model is not compatible with the specified execution host. |
| -307705 | The specified model has an unsupported 32-bit architecture. |
| -307710 | The specified item is not an inline custom device. Pass in a valid reference to an inline custom device. |
| -307711 | A channel and the alias that references it both specify a data source mapping. A channel can only have one data source mapping. Remove the mapping for either the channel or its alias. |
| -307718 | Setting Scan Interface mode failed. Before using this mode, make sure NI RIO IO Scan is installed on the target. |
| -307719 | Unable to discover XNET interface(s) before timeout elapsed. Contact NI support at ni.com/support for more information about resolving this error. |
| -307720 | Failed to route PXI_Trig0 from bus segment of chassis master device to other bus segments. To address this issue, open MAX and select the chassis. On the Triggers pane for the chassis, clear any reservation for PXI_Trig0 on the appropriate bus, set routing for PXI_Trig0 to Dynamic, and try again. |
| -307721 | Cannot enable Slow Background Conversion Mode if hardware-timed single-point sample mode is disabled for analog input channels. If you want to enable Slow Background Conversion Mode for this device, you must first enable hardware-timed single-point support for its AI channels. |
| -307722 | A DAQ channel of an unexpected type was found. |
| -307723 | A property of a DAQ channel has an invalid value. Change the value the error message lists. If you used the System Definition API to change the units property of a channel, restore the units to the original value. |
| -307724 | A DAQ channel initialization VI encountered an unexpected property name. |
| -307725 | The value does not match the dimensions of the specified channel. |
| -307726 | A calculated channel failed to compile correctly and cannot be executed. |
| -307727 | The requested DAQ device, the master timing source for the timed loop, is unavailable. |
| -307728 | One or more channel mappings have incompatible dimensions. Matrix channels only can be mapped to matrix channels with the same dimension. |
| -307729 | The system definition file is missing. Deploy a valid system definition file. |
| -307730 | One or more asynchronous custom devices failed to shut down properly and the VeriStand Engine aborted them. |
| -307731 | The system definition file is not saved in the current version of VeriStand. VeriStand cannot mutate system definition files on a real-time target. Use System Explorer to open and save the file. |
| -307732 | The system has become unresponsive. The Primary Control Loop has been shut down. To correct this error, enable Filter Watchdog Errors on the Controller Configuration page of System Explorer. You can configure watchdog functionality by monitoring the Watchdog Timer system channel using alarms and procedures. |
| -307733 | The version of the calibration file (HardwareCalibrationData.nivscal) is too old to mutate to the current version. Delete the file and manually recreate the calibration settings. |
| -307734 | The scaling and calibration setting is invalid. The channel does not exist or is not scalable. |
| -307735 | A required resource is disabled in the current version of the VeriStand Engine. For example, a DAQ board is the master timing device, but the current VeriStand Engine has disabled NI-DAQ. Remove the device or resource from the system definition file. |
| -307736 | Unable to share data for the channel. Either the source or destination target does not have reflective memory support. |
| -307737 | Unable to create dynamic data sharing between targets. Either the source or destination target does not have a data sharing device. |
| -307738 | Unable to share data between two targets. There is not enough dynamic data sharing space. |
| -307739 | Data on reflective memory must have the correct byte alignment from memory address 0x0. |
| -307740 | Invalid data range. The reflective memory network requires a valid data range. |
| -307741 | VeriStand export data exceeds the allocated reflective memory address. |
| -307742 | The VeriStand Engine could not be loaded. Make sure that VeriStand and the required drivers, such as NI-DAQmx, are installed correctly. Refer to the VeriStand readme.html for a list of required software and drivers. |
| -307743 | The VeriStand Engine failed to start. A configured start trigger or external timing source did not occur within the specified timeout. |
| -307744 | An alarm failed to compile correctly and cannot be executed. |
| -307745 | You must specify a VISA device address for the reflective memory card. |
| -307746 | The maximum Windows target rate is 1 kHz. To achieve higher rates, use an NI-DAQ device or NI FPGA target. |
| -307747 | The system definition file contains two targets that are using the same IP address. Each target must have a unique IP address. Only one target can be a Windows target. |
| -307748 | The VeriStand Engine rebooted while running the system definition file. You must reconnect to the execution host and possibly redeploy the system definition file. |
| -307749 | A simulated DAQ device cannot be used as a Timed Loop timing source or as a chassis master hardware synchronization device. In System Explorer, navigate to the Chassis Configuration page and choose a different DAQ device from the Chassis master hardware synchronization device pull-down menu. On the Controller Configuration page, choose a different Primary Control Loop timing source. Or, if all DAQ devices are simulated, disable hardware-timed single-point support for all of them or disable the DAQ device. |
| -307750 | Deserialization error. Failed to load macro file. |
| -307751 | The specified operation is not permitted while playing a macro. |
| -307752 | The specified operation is not permitted until a macro is loaded. |
| -307753 | The specified operation is not permitted unless running a macro. |
| -307754 | Serialization error. Unable to save macro. |
| -307755 | The specified operation is not permitted while recording a macro. |
| -307756 | Internal error: The DAQmx waveform producer received a command which was not declared as a publicly available. |
| -307780 | The specified feature is supported only if the VeriStand Gateway is running on the localhost machine. |
| -307781 | The channel group cannot be found in the specified log file. |
| -307782 | The channel cannot be found in the specified log file. |
| -307783 | The data structure contains a dependencies cycle. |
| -307784 | The STI file is not valid. |
| -307785 | No error provider exists to handle the error signals. |
| -307800 | A procedure failed to compile correctly and cannot be executed. |
| -307824 | The specified item is not a waveform. |
| -307825 | The specified item is not a channel. |
| -307826 | The specified item is not an alias for a channel. |
| -307827 | The specified item is not an expected type inside the system storage hierarchy. |
| -307828 | This dependency does not refer to a valid item. The item may have been deleted. Select a different dependency or re-add the invalid item and click Update Dependencies. |
| -307829 | The specified node cannot be found. |
| -307830 | The channel dimension does not match the channel default value length. |
| -307831 | Unable to save file to the specified path. |
| -307832 | The depending file path is improperly formed or cannot be found. |
| -307850 | The target cannot be reached. Verify that the Ethernet cable is connected to the real-time (RT) target and that the RT target is enabled and running. |
| -307851 | One or more system definition file dependency files differ from the originally imported version. This might cause unexpected behavior or errors. Cancel the current operation and resolve any conflicts in System Explorer. |
| -307852 | The specified dependent file is contained within a LabVIEW library file (LLB), but the destination path on the target is not contained in an LLB. Individual files cannot be copied out of an LLB. The destination path on the target must have an LLB as the parent of the dependent file. |
| -307853 | The VeriStand Gateway was unable to establish a connection with the target. Confirm that the target is running and that the VeriStand Engine successfully started. If you still cannot connect to the target, use MAX to reinstall the VeriStand Run-Time Engine on the target. You may encounter this error if you attempt to connect to the target from a LabVIEW project, because a LabVIEW project can update the start-up application for the target. To deploy a system definition to a target, the VeriStand Run-Time Engine (VeriStand.rtexe) must be the start-up application. |
| -307860 | The specified trigger channel does not exist. |
| -307861 | The data logging configuration is invalid. One or more specified channels does not exist. |
| -307862 | The specified data logging configuration resulted in a buffer size that exceeds the maximum allowed size. Reduce the buffer size by reducing the pre-trigger time, the logging rate, or the number of logged channels in the data logging configuration. |
| -307863 | The specified property value is not a valid data type for a TDMS property. |
| -307864 | The specified log file path is not valid. It might include invalid tags. |
| -307865 | The specified data logging session does not exist. |
| -307866 | An error occurred while logging data. Refer to the error description for more information. |
| -307867 | The specified data logging session name is already in use. Specify a unique data logging session name. |
| -307868 | The specified trigger condition contains syntax errors. |
| -307869 | Data was lost during logging. The log files may not contain every sample. The start and stop triggers may have also missed data to evaluate. |
| -307870 | A compatible version of NI DIAdem is not installed. You must have NI DIAdem installed to load data in NI DIAdem. |
| -307871 | Cannot retrieve information for the specified log file. Ensure the session name and filename are correct. |
| -307872 | There was an error downloading one or more of the requested files. Please use the errors parameter for more detaield information. |
| -307881 | Cannot use legacy Channel Scaling and Calibration tool/API because this project contains calibration features from the new Channel Calibration tool/API introduced in VeriStand 2012. This error occurs because the project contains a channel calibration file (.nivscf). If you want to use the legacy Channel Scaling and Calibration tool, delete the .nivscf file under the Calibrations in Project Explorer and redeploy. Otherwise, use the Channel Calibration Tool/API instead of the legacy Channel Scaling and Calibration tool/API. |
| -307882 | Cannot use Channel Calibration tool/API because this project does not contain a channel calibration file (.nivscf). If you want to use the Channel Calibration tool/API, add a .nivscf file to the project under Calibrations in Project Explorer. Otherwise, you can use the legacy Channel Scaling and Calibration Tool/API instead of the Channel Calibration tool/API. |
| -307883 | Cannot deploy project because the system definition file contains scales but the project does not contain a channel calibration file (.nivscf). Delete the scales from the system definition file and redeploy. |
| -307887 | A polynomial scale mapped to a channel(s) does not have coefficients defined. Remove the mapping or update the scale to contain coefficients, and then try to deploy the system definition again. |
| -307889 | A lookup table scale mapped to a channel(s) is empty. Remove the mapping or update the scale to contain pairs of pre-scaled values and the corresponding values to which to scale them, and then try to deploy the system definition again. |
| -307891 | VeriStand only supports devices whose calibration password is the default value. Use NI MAX or the NI System Configuration API to reset the calibration password on the device to the default value. |
| -307900 | The number of generator mappings exceeds the maximum allowed. Reduce the number of mapped channels or increase the maximum number of mappings per generator using the Stimulus Configuration page. |
| -307901 | The number of compiled stimulus generator steps exceeds the maximum allowed. Reduce the number of steps in the stimulus generator or increase the maximum number of steps per generator using the Stimulus Configuration page. |
| -307902 | The specified stimulus profile is empty. It contains no compiled steps. |
| -307903 | The number of data points exceeds the maximum auxiliary buffer size. Reduce the number of data points in the stimulus profile or increase the maximum auxiliary buffer size in the Stimulus Configuration page of System Explorer. |
| -307904 | A stimulus profile failed to compile correctly. Verify that the stimulus profile links to valid channels. |
| -307905 | Timeout occurred while writing data to the auxiliary buffer. |
| -307906 | Timeout occurred while writing data to the analysis buffer. |
| -307907 | Multi-point data does not have the correct timing. The data must start at time 0 and increment at a multiple of Delta t value. |
| -307908 | The stimulus profile manager currently is reserved by a client. |
| -307909 | Unable to start stimulus profile generation. Stimulus profile file contains invalid profile steps or incorrect timing. |
| -307910 | Unable to start stimulus profile generation. CAN logging requires that the CAN Bus Monitor is running. |
| -307911 | Unable to start stimulus profile generation. One or more calibration files are not found. |
| -307912 | The number of data points exceeds the maximum analysis buffer size. Reduce the number of data points in the stimulus profile or increase the maximum analysis buffer size using the Stimulus Configuration page of System Explorer. |
| -307913 | The number of stimulus generators exceeds the maximum allowed. Reduce the number of stimulus generators in the stimulus profile or increase the maximum allowed using the Stimulus Configuration page of System Explorer. |
| -307914 | The specified CSV file does not contain a Timestamp column. The file you specify must have a Timestamp column that contains values in milliseconds. |
| -307915 | The operation could not be completed. A stimulus profile is running. |
| -307916 | A stimulus profile generator contains a Set Variable step that attempts to set a variable on another target. A Set Variable step only can set a variable on the same target as the generator containing the step. |
| -307917 | A stimulus profile generator contains channel mappings for channels on a different target than the target on which the generator will execute. A generator can only map to channels on the target on which it will execute. Confirm that the generator is not mapped to channels from different targets, or that the generator does not specify an execution target that is different than one of the channel mappings. |
| -307925 | The specified node is not compatible with this operation. |
| -307926 | This node already exists in the system. |
| -307927 | Invalid argument. The node reference is not a valid channel. |
| -307928 | Found an existing FPGA target with the same RIO address configuration. |
| -307929 | The mapping definition is invalid. The source channel must be readable, the destination channel must be writable, and both channels cannot be part of the stimulus generator. |
| -307930 | A node name cannot be an empty string. |
| -307931 | Model execution order group cannot be empty. |
| -307932 | The formula type must depend on variables. |
| -307933 | Attempted to write to a read-only property. |
| -307948 | Unable to establish a connection between the VeriStand Model Simulation Server and client. The VeriStand MDL client version is incompatible with the currently loaded VeriStand Model Simulation Server. |
| -307949 | The selected model (.mdl) is invalid. Verify that the model can be compiled and run properly, that you have added an NIVeriStandSignalProbe block to it, and that the stop time is set to inf. |
| -307950 | Unable to connect to the VeriStand Model Simulation Server. |
| -307951 | VeriStand requires that you compile a model (.mdl) before it can run on a real-time (RT) target. |
| -307970 | An inline custom device attempted to access invalid data in the VeriStand Engine. The inline custom device attempted to read or write data using an invalid reference or a reference that did not have the read or write access required for that operation. |
| -307971 | A channel cannot have child items. |
| -307972 | Error provider received an electrical error that contains a signal it cannot handle. Verify the error provider is implemented correctly and all errors contain the correct signals. |
| -307973 | Error provider received an electrical error with an unexpected number of signals. Verify the error provider is implemented correctly and all errors contain the correct number of signals. |
| -307974 | Error provider received an unexpected configuration. Verify the error provider is implemented correctly and the errors can be handled by the error provider. |
| -307980 | The specified stimulus profile session is locked. Unlock the stimulus profile session to control sequences in the session. |
| -307981 | The stimulus profile session does not contain a sequence with the specified name. |
| -307982 | The stimulus profile session is not deployed. |
| -307983 | The sequence containing the specified variable is currently running. You cannot probe a variable value while a sequence is running. |
| -307984 | The stimulus profile session is already deployed. |
| -307985 | The sequence did not complete the timestep within the specified timeout. This could be due to a sequence that contains too much processing or an infinite loop that does not yield. Evaluate the timing of your sequence or increase the timeout. |
| -307986 | The specified parameter assignment is not valid. The real-time sequence parameter does not exist. |
| -307987 | One or more real-time sequence parameters with a by-reference evaluation was not mapped to. Assign a value to all real-time sequence parameters that have a by-reference evaluation type. |
| -307988 | The compiler failed because the specified real-time sequence contains one or more errors. |
| -307989 | The specified parameter assignment is not valid. The channel mapped to the parameter could not be found in the system. |
| -307990 | A system definition channel has been mapped to two or more real-time sequence parameters that are not the same data type. A channel can only be mapped to multiple parameters if they share the same data type. |
| -307991 | A real-time sequence parameter assignment has an invalid data type. Match the data type of the value assigned to the parameter to the parameter's data type. |
| -307992 | The specified operation cannot be completed. There is no project file currently open. |
| -307993 | The parameter dimension does not match the parameter default value length. |
| -307994 | The specified parameter cannot be found. |
| -307995 | VeriStand engine failed to retrieve data from the SLSC chassis status loop within the specified timeout. The System Definition was undeployed. |
| -307996 | SLSC module not found in the specified slot. Check your SLSC hardware and make sure the custom device is inserted in the correct slot. |
| -307997 | There are SLSC chassis added to the system definition that are not supported. Remove the SLSC chassis from the system definition. |
| -307998 | The switch load signal conditioning (SLSC) chassis name or IP address/hostname is empty. Provide a SLSC chassis name or IP address/hostname. |

Parent topic:

Debugging the System

Related information:

- NI KnowledgeBase

<!--NI_TOPIC bundle=veristand path=veristand-file-extensions.html language=enus -->
## TOPIC 00408: VeriStand File Extensions

- bundle_id: `veristand`
- source_path: `veristand-file-extensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-file-extensions.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand projects use a variety of file types. Use the following table to find information on a file extension. File extension Description .bt1 A batch stimulus profile file created using VeriStand 2009, 2010, or NI Dynamic Testing Software 1.0. .cah Calibration History file. .csv Comma Separated V

### VeriStand File Extensions

VeriStand projects use a variety of file types.

Use the following table to find information on a file extension.

| File extension | Description |
| --- | --- |
| .bt1 | A batch stimulus profile file created using VeriStand 2009, 2010, or NI Dynamic Testing Software 1.0. |
| .cah | Calibration History file. |
| .csv | Comma Separated Values file. |
| .dbc | Database file that describes signals and associated messages for a collection of controller area network (CAN) nodes. |
| .depvs | Support file that lists any dependencies of a compiled model. This file ensures the dependencies deploy to real-time targets. |
| .dll | Shared library. VeriStand requires that models be compiled into a dynamic link library (DLL) before they can run on a Phar Lap RT target. |
| .et1 | A step-based stimulus profile file created using VeriStand 2009 or NI Dynamic Testing Software 1.0. |
| .et2 | A table-based stimulus profile file created using VeriStand 2009 or NI Dynamic Testing Software 1.0. |
| .fpgaconfig | FPGA Configuration file. XML-based file that specifies the content of direct memory access first-in-first-out memory buffers (DMA FIFOs). |
| .ini | Standard Windows configuration settings file. |
| .ldf | A local interconnect network (LIN) description file. |
| .llb | A LabVIEW VI library (LLB). Custom devices that run in VeriStand consist of LabVIEW VIs distributed in LLBs. |
| .lvbitx | LabVIEW-generated bitfile. Defines the available I/O on the FPGA. A bitfile is a compiled version of an FPGA VI. |
| .lvlib | LabVIEW project library. A collection of LabVIEW VIs, type definitions, shared variables, palette files, and other files, including other project libraries. For example, the VeriStand LabVIEW APIs are organized into project libraries. |
| .lvmodel | Compiled model that runs on Windows PCs. Generate models from a LabVIEW VI or simulation subsystem. |
| .lvmodelso | Compiled model that runs on Linux x64. Generate models from a LabVIEW VI or simulation subsystem. Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS. For more information about how to use LabVIEW models with Linux, visit the NI website. VeriStand is not supported on x64 Intel-based cDAQ controllers running NI Linux Real-Time. |
| .lvproj | LabVIEW project file. A LabVIEW file type you can use to build custom devices for VeriStand. |
| .m | Text-based m-script file that initializes variables and can provide other information needed by models. |
| .mdl | Model you developed in the MathWorks Simulink® simulation environment. |
| .ncd | NI-CAN database. Database file that describes signals and associated messages for a collection of CAN nodes. |
| .ncl | NI-XNET logfile. Binary file for the storage of CAN, FlexRay, and LIN data. |
| .nivscal | Calibration file deployed to targets. Binary file that VeriStand deploys, and then deletes when the project is undeployed. |
| .nivscf | Calibration file on host. XML-based file you can import a .nivscf file into other projects to reuse the calibrations. |
| .nivsmacro | Macro file. A recording of the commands sent to the target. |
| .nivsproj | Legacy VeriStand project file. |
| .nivsprj | VeriStand project file. |
| .nivsscreen | VeriStand screen file. |
| .nivssdf | VeriStand system definition file. |
| .nivsseq | Real-time sequence. |
| .nivsseqt | Real-time sequence template. |
| .nivsstimprof | Stimulus profile. |
| .nivsstimproft | Stimulus profile template. |
| .nivstest | A stimulus profile file created using VeriStand 2009, 2010, or NI Dynamic Testing Software 1.0. |
| .out | Shared library. |
| .tdms | Technical Data Management Streaming file. A binary measurement file that contains waveform data. Stores descriptive information at the file, group, and channel levels. When you run a stimulus profile file using the Stimulus Profile Editor, VeriStand logs data to a TDMS file. |
| .vi | LabVIEW Virtual Instrument. |
| .xml | Extensible Markup Language file. VeriStand requires a corresponding XML file for any custom device that you add to a project. An XML file might also refer to a Stimulus Profile Editor test results file or a FIBEX file, a database storage file for use with the XNET Database Editor. |
| .xsd | XML Schema Document file. This file determines the validity of that XML file. It contains a set of rules to which the corresponding XML document must adhere in order to be considered valid according to that schema. VeriStand ships with .xsd files that you can use to validate FPGA configuration files and custom device XML files. |

Parent topic:

VeriStand Environment

Related tasks:

- Using Models from LabVIEW VIs
- Viewing Stimulus Profile Test Results

<!--NI_TOPIC bundle=veristand path=veristand-glossary.html language=enus -->
## TOPIC 00409: Glossary

- bundle_id: `veristand`
- source_path: `veristand-glossary.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-glossary.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand uses unique terms for completing tasks while creating a project. Use the following table to learn more about a term used in VeriStand. Alphabetical order Term Description A Alarm A notification that the value of a particular channel has gone outside a specified range of values. An alarm tr

### Glossary

VeriStand uses unique terms for completing tasks while creating a project.

Use the following table to learn more about a term used in VeriStand.

| Alphabetical order | Term | Description |
| --- | --- | --- |
| A | Alarm | A notification that the value of a particular channel has gone outside a specified range of values. An alarm triggers the execution of a specified procedure. |
| Alias | An alternate name for a channel in a system definition file. |  |
| B | Bitfile | A LabVIEW-generated file that defines the available I/O on the FPGA. A bitfile is a compiled version of an FPGA VI. |
| Block diagram | A pictorial description or representation of a program or algorithm. In LabVIEW, the block diagram that consists of executable icons called nodes and wires that carry data between the nodes. The block diagram is the source code for the VI. The block diagram resides in the block diagram window of the VI. |  |
| C | Calculated channel | A channel that produces a new value based on calculations performed on other channels in the system. |
| Calibration | The process of determining the accuracy of an instrument. In a formal sense, calibration establishes the relationship of an instrument's measurement to the value provided by a standard. When that relationship is known, the instrument may then be adjusted (calibrated) for best accuracy. |  |
| CAN (Controller Area Network) | A serial bus finding increasing use as a device-level network for industrial automation. CAN was developed by Bosch to address the needs of in-vehicle automotive communications. |  |
| Chassis master hardware synchronization device | A hardware device that controls the synchronization of all hardware in a PXI chassis or across multiple PXI chassis. The chassis master hardware synchronization device must be an NI-DAQ device with at least one analog input or output channel, any NI FPGA, or a timing and sync device that has the capability to drive the RTSI 0 line. |  |
| Custom device | A virtual instrument that executes user-defined actions, such as third-party hardware control. |  |
| D | Differential measurement system | A way to configure a device to read signals, in which you do not need to connect either input to a fixed reference, such as the earth ground or a building ground. |
| DLL (Dynamic Link Library) | A compiled model. |  |
| DMA (Direct Memory Access) | A method by which data can be transferred to/from computer memory from/to a device or memory on the bus while the processor does something else. DMA is the fastest method of transferring data to/from computer memory. |  |
| Driver | Software that controls a specific hardware device. |  |
| F | FIBEX (FIeld Bus EXchange) | A vendor-independent exchange format for embedded network data. It is an XML-based text format. For NI-XNET, NI adopted the ASAM FIBEX standard as a database storage format. |
| FIFO (First-In-First-Out memory buffer) | The first data stored is the first data sent to the acceptor. |  |
| FIFO sink | The output of a FIFO. You can use the VeriStand Custom Device APIs to set the buffer size at the source and sink of the FIFOs that an asynchronous custom device uses to share data with the real-time engine. |  |
| FIFO source | The input of a FIFO. You can use the VeriStand Custom Device APIs to set the buffer size at the source and sink of the FIFOs that an asynchronous custom device uses to share data with the real-time engine. |  |
| FlexRay | A new, deterministic, fault-tolerant, and high-speed bus system developed in conjunction with automobile manufacturers and leading suppliers. |  |
| FPGA (Field-Programmable Gate Array) | A semi-conductor device that contains a large quantity of gates (logic devices), which are not interconnected, and whose function is determined by a wiring list, which is downloaded to the FPGA. The wiring list determines how the gates are interconnected, and this interconnection is performed dynamically by turning semiconductor switches on or off to enable the different connections. |  |
| FPGA configuration file | An XML-based file that specifies the content of DMA FIFOs. |  |
| FPGA VI | A configuration that is downloaded to the FPGA and that determines the functionality of the hardware. |  |
| Frames | Messages sent across an embedded network. Frames are sorted into clusters within an NI-XNET database. |  |
| H | HIL (Hardware-In-the-Loop) | A simulation configuration in which you test a controller implementation with a simulated system. |
| Host computer | The computer that runs the VeriStand Gateway and hosts the screen file. |  |
| I | Interface | The interface represents a single CAN, FlexRay, or LIN connector on an NI hardware device. Within NI-XNET, the interface is the software object used to communicate with external hardware described in the database. |
| L | LabVIEW | A graphical programming language. |
| LIN (Local Interconnect Network) | A standard for low-cost, low-end multiplexed communication in automotive networks. LIN provides cost-efficient communication in applications where the bandwidth and versatility of CAN are not required. |  |
| M | Mapping | A connection between two channels. |
| MAX (Measurement & Automation Explorer) | Provides a centralized location for configuration of NI hardware products. MAX also provides many useful tools for interaction with hardware. |  |
| MIO (Multifunction I/O) | A DAQ module that designates a family of data acquisition products that have multiple analog input channels, digital I/O channels, timing, and optionally, analog output channels. An MIO product can be considered a miniature mixed signal tester, due to its broad range of signal types and flexibility. Also known as multifunction DAQ. |  |
| N | NRSE (Non-Referenced Single-Ended mode) | All measurements are made with respect to a common (NRSE) measurement system reference, but the voltage at this reference can vary with respect to the measurement system ground. |
| O | Offline | A simulation configuration in which you use software to simulate the controller and the system you want to control. No hardware is involved in an offline simulation. |
| P | PCI (Peripheral Component Interconnect) | An industry-standard, high-speed databus. |
| Phar Lap ETS | A real-time operating system designed optimized for devices based on the Intel x86 architecture. |  |
| Port | In regard to NI-XNET, port refers to the connector on an NI hardware device. The physical connector includes the transceiver cable if applicable. |  |
| Port width | Refers to the number of lines in a port. For example, E Series devices have one port with eight lines; therefore, the port width is eight. |  |
| Procedure | A set of actions that the VeriStand Engine executes. |  |
| Project file | The .nivsprj file that defines high-level settings in an VeriStand project, such as the screen and system definition files to run, the IP address of the VeriStand Gateway, etc. |  |
| Q | Quadrature encoder | An encoding technique for a rotating device where two tracks of information are placed on the device, with the signals on the tracks offset by 90º from each other. This makes it possible to detect the direction of the motion. |
| R | RAM (Random-Access Memory) | The generic term for the read/write memory that is used in computers. RAM allows bits and bytes to be written to it as well as read from. |
| RCP (Rapid Control Prototype) | A simulation configuration in which you test plant hardware with a software model of the controller. |  |
| RT (Real-Time) | Pertaining to the performance of a computation during the actual time that the related physical process transpires so results of the computation can be used in guiding the physical process. |  |
| Real-time sequence | A program that can deploy to a target with a system definition file and read/write channels defined in the system definition file. Real-time sequences can feature a wide array of programming constructs, including while loops, for loops, variables, and conditional statements. Real-time sequences execute on the target. |  |
| Reflective memory network | A means of sharing data between two independent systems in a deterministic manner. Reflective memory devices are connected together using fiber optic cables. This reflective memory system forms a deterministic network that operates like a dual-ported memory system. |  |
| RSE (Referenced Single-Ended configuration) | All measurements are made with respect to a common reference measurement system or ground. Also called a grounded measurement system. |  |
| RTSI bus (Real-Time System Integration) | The NI timing bus that interconnects data acquisition devices directly by means of connectors on top of the devices for precise synchronization of functions. |  |
| S | Screen file | A .nivscreen or .nivsscr file that defines the configuration and settings for the screens and display items you view in the VeriStand Editor or Workspace. |
| SCXI (Signal Conditioning eXtensions for Instrumentation) | The NI product line for conditioning low-level signals within an external chassis near sensors so that only high-level signals are sent to DAQ devices in the noisy PC environment. |  |
| Service | A LabVIEW VI that runs on the host computer when VeriStand connects to a target. Services are typically Workspace tools that you want to launch as soon as you connect to a target, or that you want to synchronize with the launch of the Workspace window. |  |
| Single-point | Data acquisition in which the software reads a single point of data from one or more analog input channels and immediately returns the value. |  |
| Stimulus profile | A test executive that can call real-time sequences, open and close VeriStand projects, and perform data-logging and pass/fail analysis. It also connects real-time sequences to system definition files to bind channel data within the system definition file to variables in the real-time sequence. Stimulus profiles execute on the host computer. |  |
| Stimulus Profile Editor | A development environment you use to create, modify, and execute tests. |  |
| System channel | A channel that monitors the state and condition of various internal aspects of VeriStand. |  |
| System definition file | A .nivssdf file you configure primarily in System Explorer. A system definition file contains the configuration settings of the VeriStand Engine. |  |
| T | Target | The desktop PC or real-time target on which you run the system definition file and VeriStand Engine. |
| TestStand | NI test executive for sequencing and managing automatic test programs. |  |
| Timing and sync device | A virtual instrument that synchronizes more than one chassis. |  |
| U | User channel | A channel that stores a single value. |
| V | VeriStand Engine | The non-visible execution mechanism that controls the timing of the entire system as well as the communication between the target and the host computer. |
| VeriStand Gateway | The non-visible mechanism that creates a TCP/IP communication channel which facilitates communication with the VeriStand Engine over the network. The VeriStand Gateway receives channel values from the VeriStand Engine and stores these values in a table that can be viewed using the Channel Data Viewer. |  |
| VeriStand LabVIEW Model Generator | A tool that generates a compiled model from a LabVIEW VI or simulation subsystem. This tool is accessible from the Tools menu in LabVIEW 2010 or later and generates files of the type .lvmodel or .lvmodelso. Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS. |  |
| VI (Virtual Instrument) | A LabVIEW program. |  |
| X | XNET | A suite of products that provide connectivity to Controller Area Network (CAN), Local Interconnect Network (LIN), and FlexRay networks. |
| XNET database | A standardized file, such as CANdb (.dbc) or NI-CAN (.ncd) for CAN or FIBEX (.xml) for FlexRay that NI-XNET applications use to understand hardware communications in the embedded system. The database contains many object classes, each of which describes a distinct entity in the embedded system. |  |

<!--NI_TOPIC bundle=veristand path=veristand-model-framework.html language=enus -->
## TOPIC 00410: VeriStand Model Framework

- bundle_id: `veristand`
- source_path: `veristand-model-framework.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-model-framework.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand Model Framework is used to design and compile models created in third-party modeling environments and C/C++. VeriStand and the LabVIEW Model Interface Toolkit allow you to run simulation models written in C/C++. To enable your models to interact with this NI software, you must design t

### VeriStand Model Framework

The VeriStand Model Framework is used to design and compile models created in
 third-party modeling environments and C/C++.

VeriStand and the LabVIEW Model Interface Toolkit allow you to run simulation models written
 in C/C++. To enable your models to interact with this NI software, you must design them to
 work with the VeriStand Model Framework. The framework includes files that allow your model to
 interact with VeriStand and the Model Interface Toolkit.

When you run your VeriStand application, the application executes functions defined in VeriStand
 Model Framework files. These functions call your model code to execute the model.

Parent topic:

Using the VeriStand Model Framework for Simulink

Related concepts:

- Model Framework Components
- Model Code Components
- Model Framework and Model Code Interaction

<!--NI_TOPIC bundle=veristand path=veristand-net-reference.html language=enus -->
## TOPIC 00411: VeriStand .NET Reference

- bundle_id: `veristand`
- source_path: `veristand-net-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/veristand-net-reference.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use .NET APIs to programmatically control software operations. VeriStand includes the following .NET APIs. These APIs are documented in the VeriStand .NET Reference. API Assembly Description Execution API NationalInstruments.VeriStand.ClientAPI (in NationalInstruments.VeriStand.ClientAPI.dll) Automa

### VeriStand .NET Reference

Use .NET APIs to programmatically control software operations.

Note

VeriStand .NET Reference

| API | Assembly | Description |
| --- | --- | --- |
| Execution API | NationalInstruments.VeriStand.ClientAPI (in NationalInstruments.VeriStand.ClientAPI.dll) | Automates the operation of an VeriStand application on the target. For example, you can read and write channel data, control running models, configure alarm states and read data from alarms, and access Workspace tools. |
| System Definition API | NationalInstruments.VeriStand.SystemDefinitionAPI (in NationalInstruments.VeriStand.SystemDefinitionAPI.dll) | Automates the operation and configuration of a system definition file. This API performs the same operations as configuring the file in the System Explorer window. |
| Stimulus Profile Definition API | NationalInstruments.VeriStand.StimulusProfileDefinitionApi (in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll) | Automates the operation and configuration of stimulus profiles. This API performs the same operations as configuring stimulus profiles in the Stimulus Profile Editor. |
| Real-Time Sequence Definition API | NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi (in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll) | Automates the operation and configuration of real-time sequences. This API performs the same operations as configuring real-time sequences in the Stimulus Profile Editor. |
| Data Types API | NationalInstruments.VeriStand.Data (in NationalInstruments.VeriStand.DataTypes.dll) | Represents data types and resources used by VeriStand. |

You can access these assemblies from any .NET-compatible programming language or
 environment, including LabVIEW and NI TestStand.

Parent topic:

Running Tests

Related tasks:

- Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related information:

- VeriStand .NET Reference

<!--NI_TOPIC bundle=veristand path=version-system-definition.html language=enus -->
## TOPIC 00412: Versioning a System Definition File

- bundle_id: `veristand`
- source_path: `version-system-definition.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/version-system-definition.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create and test modifications to your system definition file by duplicating the file in the VeriStand Editor. Before you begin, create a VeriStand project. VeriStand supports the versioning of project documents, including the system definition. Copy an existing system definition to test changes. The

### Versioning a System Definition File

Create and test modifications to your system definition file by duplicating the file in
 the VeriStand Editor.

Before you begin, create a VeriStand
 project.

VeriStand supports the versioning of
 project documents, including the system definition. Copy an existing system definition to test
 changes. The original file serves as a restoration point whereas the copy can be modified.

1. Open a project in the VeriStand Editor.
2. In the Navigation pane, click Project
 Files.
3. Right-click the existing system definition file (.nivssdf) and
 select Duplicate. 
 Note If the system definition has unsaved
 changes, you will be prompted to save the file.
4. Optional: 
 Update the name of the new system definition.
  1. Right-click the file and select Rename.
  2. Enter a new name for the file.
5. Modify the new system definition file.
6. Right-click the modified system definition and select Make
 Active.
7. Select Operate»Deploy to deploy the modified system definition.
8. Optional: 
 Remove a system definition file by right-clicking the file and
 selecting Delete. 
 Note You cannot remove an active system definition. Right-click the system definition and
 select Make Inactive before deleting the file.

Parent topic:

Configuring a System Definition File

Related tasks:

- Creating a New Project

<!--NI_TOPIC bundle=veristand path=vi-source-distribution.html language=enus -->
## TOPIC 00413: Creating a VI Source Distribution

- bundle_id: `veristand`
- source_path: `vi-source-distribution.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/vi-source-distribution.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate custom VIs into VeriStand by building a LabVIEW project into a source distribution. Use the LabVIEW Application Builder to build a source distribution to call custom VIs in VeriStand. This creates a local copy of the VI dependencies. For more information, refer to Introduction to the LabVI

### Creating a VI Source Distribution

Integrate custom VIs into VeriStand by building a LabVIEW project into a source
 distribution.

Introduction to the LabVIEW Application Builder

1. Open the LabVIEW project containing the VI in Project
 Explorer.
2. Right-click Build Specifications and select New»Source Distribution.
3. In Source Distribution Properties, set where to build the
 output.
  1. Under the Category list, click
 Information.
  2. Enter a Build specification name.
  3. Select the Destination directory.
4. Include the VI source files.
  1. Under the Category list, click Source
 Files.
  2. Add the custom VI and any supporting sub-VIs to Always
 Included.
5. Specify the output type.
  1. Under the Category list,
 click Destinations.
  2. Click Add Destination to create a new destination.
  3. Enter a Destination label that matches the VI name.
  4. Set the Destination type as Directory.
6. Remove additional exclusions.
  1. Under the Category list, click Additional
 Exclusions.
  2. Disable Exclude file from vi.lib, Exclude files
 from instr.lib, and Exclude files from
 user.lib.
7. Click Build.

When the build finishes, LabVIEW creates the VI and all
 necessary dependencies in the destination path.

After building the custom VI, add it to the VeriStand
 project or to
 the Tools menu.

Parent topic:

Configuring a Project File

Related tasks:

- Adding Custom VIs
- Adding a Standard or Custom Tools Menu Item

Related information:

- Introduction to the LabVIEW Application Builder

<!--NI_TOPIC bundle=veristand path=view-test-results-atml.html language=enus -->
## TOPIC 00414: Viewing Stimulus Profile Test Results

- bundle_id: `veristand`
- source_path: `view-test-results-atml.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/view-test-results-atml.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable the Stimulus Profile Editor to automatically open stimulus profile test results. Each time you run a stimulus profile, VeriStand produces a test results file that adheres to the Automatic Test Markup Language (ATML) standard. In the VeriStand Editor, click Tool Launcher Stimulus Profile Edito

### Viewing Stimulus Profile Test Results

Enable the Stimulus Profile Editor to
 automatically open stimulus profile test results.

Each time you run a stimulus profile,
 VeriStand produces a test results file that adheres to the Automatic Test Markup
 Language (ATML) standard.

1. In the VeriStand Editor, click Tool Launcher»Stimulus Profile Editor.
2. Click the Execution tab and click Show Test
 Result File.

After a stimulus profile finishes
 running, the ATML Test Report will open in a web browser.

Alter the appearance of the test
 report by modifying
 its style sheet.

Parent topic:

Creating Real-Time Test Scenarios with Stimulus Profiles and Real-Time Test Sequences

Related concepts:

- Automatic Test Markup Language (ATML) Standard

Related tasks:

- Customizing ATML Test Result Appearance

<!--NI_TOPIC bundle=veristand path=viewing-target-logs.html language=enus -->
## TOPIC 00415: Viewing Real-Time Target Logs

- bundle_id: `veristand`
- source_path: `viewing-target-logs.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/viewing-target-logs.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Display and monitor logs from a real-time target. The Target Log Viewer collects system definition deployment information and debugging messages. Open your project in the VeriStand Editor. Deploy the system definition to a real-time target. Click Tool Launcher Target Log Viewer . In the Target Log V

### Viewing Real-Time Target Logs

Display and monitor logs from a real-time target.

Target Log Viewer

1. Open your project in the VeriStand
 Editor.
2. Deploy the system definition to a
 real-time target.
3. Click Tool Launcher»Target Log Viewer.
4. In the Target Log Viewer tab, click
 Start Listing. 
 An output log will begin to appear in the tab.
5. Click Stop Listening and scroll on the
 log to review information from the beginning of the
 deployment. 
 Note If you
 click Start Listening again,
 the log will update with information that was not
 recorded while stopped.

/c/ni-rt/NIVeriStand/Logs/

Parent topic:

Debugging the System

Related tasks:

- Deploying the System Definition File to a Real-Time Target

<!--NI_TOPIC bundle=veristand path=virtual-ecu-vendor-protocol-support.html language=enus -->
## TOPIC 00416: Virtual ECU Vendor and Protocol Support

- bundle_id: `veristand`
- source_path: `virtual-ecu-vendor-protocol-support.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/virtual-ecu-vendor-protocol-support.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Virtual ECUs allow you to test devices quickly, with a more realistic rest bus simulation, and with less effort for creating the bus simulation. Vendor SupportThe VeriStand Virtual ECU Toolkit supports virtual ECUs you created with Synopsys^® Silver in FMU format. Both FMI 2.0 and FMI 3.0 co-simulat

### Virtual ECU Vendor and Protocol
 Support

Virtual ECUs allow you to test devices quickly, with a more realistic rest bus
 simulation, and with less effort for creating the bus simulation.

#### Vendor Support

The VeriStand Virtual ECU Toolkit supports virtual ECUs you created with Synopsys<sup>®</sup>
 Silver in FMU format. Both FMI 2.0 and FMI 3.0 co-simulation models
 are supported. Contact Synopsys for more information about creating
 a virtual ECU.

#### Communication Protocol Support

- CAN
- LIN
- Ethernet

#### Limitations

- VeriStand supports only virtual ECUs built with
 Synopsys ® Silver virtual bus in Step
 Mode.
- VeriStand does not support running virtual ECUs and
 network clusters at different rates.
- VeriStand does not support virtual ECUs built with a
 non-default SVB Configuration file
 (SilverCanSvbConfigFile).

Parent topic:

Integrating Virtual ECUs

Related information:

- Contact Synopsys

<!--NI_TOPIC bundle=veristand path=visualize-system-state.html language=enus -->
## TOPIC 00417: Visualizing System State

- bundle_id: `veristand`
- source_path: `visualize-system-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/visualize-system-state.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `task`
- source_description: Create interfaces that an operator can use to interact with a VeriStand project. User interfaces, called screens, allow an operator to easily control and monitor specific channels within a system definition at run-time. Use the VeriStand Editor to modify and operate screens.For information on legacy

### Visualizing System State

Create interfaces that an operator can use to interact with a
 VeriStand project.

screens

VeriStand Editor

Note

- [Viewing, Creating, and Interacting with Screens](screens.html) Create screens and projects in the VeriStand Editor to view, create, and interact with user interfaces.
- [Adding and Configuring Components of a Screen](adding-ctrls.html) Add controls and indicators to a Screen to modify the user interface of a VeriStand project.
- [Configuring Controls and Indicators to Send and Receive Data](veristand-editor-mapping-ctrls.html) Configure a screen to send a receive data by mapping controls and indicators to a channel in the system definition.
- [VeriStand Editor Tools](editor-tools.html) The VeriStand Editor provides tools that allow you to manipulate a project without having to open the system definition.
- [Running the VeriStand Workspace](using-workspace.html) Launch the **Workspace** to run a project, view and modify the user interface, and to perform operations such as monitoring alarms, viewing channel data, scaling and calibrating channels, and running stimulus profiles.

Related tasks:

- Running the VeriStand Workspace

<!--NI_TOPIC bundle=veristand path=void-return-value.html language=enus -->
## TOPIC 00418: Void Return Value

- bundle_id: `veristand`
- source_path: `void-return-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/void-return-value.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Understand the use and limitations of the void return value variable in expressions and the Stimulus Profile Editor. You cannot use this variable for anything other than a return variable. Property/Section Description Identifier Specifies the name of the variable. Use this string to identify the var

### Void Return Value

Understand the use and limitations of the void return value variable in expressions
 and the Stimulus Profile Editor.

Note

| Property/Section | Description |
| --- | --- |
| Identifier | Specifies the name of the variable. Use this string to identify the variable in expressions. |
| Units | Specifies the units to associate with the variable value. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Variables Primitives

<!--NI_TOPIC bundle=veristand path=vs-engine.html language=enus -->
## TOPIC 00419: VeriStand Engine

- bundle_id: `veristand`
- source_path: `vs-engine.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/vs-engine.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand Engine is the execution mechanism that controls the timing of the entire system and the communication between the target and the host computer. The VeriStand Engine executes hardware I/O, runs models, procedures, alarms, and tests, and computes values in the channel table based on the

### VeriStand Engine

The VeriStand Engine is the execution mechanism that controls the timing of the
 entire system and the communication between the target and the host computer.

The VeriStand Engine executes
 hardware I/O, runs models, procedures, alarms, and tests, and computes values in the
 channel table based on the results of model execution and hardware I/O. This engine
 runs on either a desktop PC in simulation mode or as an embedded application on a RT
 system.

The VeriStand Engine consists of multiple timed loops that use
 real-time (RT) FIFOs to transfer data between the loops. Each loop performs
 designated tasks and has an assigned priority. Although you cannot change the
 priority or primary tasks of the engine loops, you can customize loop operations,
 such as the execution rate. The system definition file contains the configuration
 settings for the VeriStand Engine.

Note

The following figure illustrates the operation of the VeriStand
 Engine.

[IMAGE alt='image' src='GUID-E6E40161-67C2-4FAF-86B7-58523A9E53B4-a5.gif']

The following table displays the
 priority and default execution rate for the loops of the VeriStand Engine.

| VeriStand Engine loop | Description | Priority | Default execution rate |
| --- | --- | --- | --- |
| Primary Control Loop (PCL) | Controls the timing for the VeriStand Engine and maintains the most up-to-date table of channel values. Use System Explorer to set the execution mode of the PCL. Per iteration, the PCL executes the following tasks: Reads and writes high-speed FPGA I/O, analog and counter DAQ I/O, and Asynchronous Custom Device Loop data. Applies scaling to the data. Executes one step of the real-time sequence of a test that is currently running Sends data to the Data Processing Loop to synchronize the table of channel values. Sends data to the Model Execution Loop(s). Prompts the Data Processing Loop, Model Execution Loop(s), and Asynchronous Custom Device Loop(s) to execute. Performs software fault insertion. Creates mapping connections. Executes inline custom devices. Reads status information from the Waveform Processing Loop and DAQmx Waveform Producer Loop(s). Note For more information on the PCL, see Primary Control Loop Execution Steps | High | 100 Hz |
| Model Execution Loop(s) | Executes a corresponding compiled model. The number of models in the system definition determines the number of loops. Per iteration, each Model Execution Loop executes the following tasks: Reads the data sent by the PCL and maps this data to model inports. Executes one step of the model. Reads model outport values and sends this data to the PCL. Reads model inport signals and sends this data to the PCL. Note A Model Execution Loop handles high-speed, dynamic data associated with model inports and outports, while a Model Interface Loop reads and applies the lower-speed, asynchronous updates to model parameter values. | Medium | A decimation of the PCL rate |
| Asynchronous Custom Device Loop(s) | Executes and transmits custom device inport data values per iteration of the PCL. The VeriStand Engine is responsible for initiating the Asynchronous Custom Device Loop. | High Medium Low | User-defined |
| Waveform Processing Loop | Transfers waveform data through the system. Per iteration, the Waveform Processing Loop executes the following tasks: Reads waveform data from DAQmx Waveform Producer Loops. Sends waveform data to the VeriStand Gateway. Reads waveform data from custom devices. Sends waveform data to custom devices. | Low | Event driven |
| DAQmx Waveform Producer Loops | Acquires waveforms from DAQ devices. Each DAQmx Waveform Producer Loop corresponds to a waveform task in the system definition. Per iteration, Waveform Producer Loop executes the following tasks: Reads waveform data from analog input channels on DAQ devices. Sends waveform data to the Waveform Processing Loop. Logs acquired data to .tdms files. | Low | 10 Hz or user-defined |
| Data Processing Loop | Distributes the execution commands received by the Communication Receive Loop among the engine loops. Like the PCL, the Data Processing Loop maintains a complete copy of the channel values table. Per iteration, the Data Processing Loop executes the following tasks: Receives the table of channel values from the PCL. Executes procedures, alarms, and calculated channels. Transmits updated table of channel values to the PCL. Sends data values to the Communication Send Loop. | Medium | A decimation of the PCL rate |
| Communication Send Loop | Transmits channel values to the VeriStand Gateway. | Low | 15 Hz |
| Communication Receive Loop | Listens for execution commands that the VeriStand Gateway sends. | Low | Event driven |
| XNET Loop | Reads and writes XNET data. | Low | 100 Hz |
| DIO Loop | Reads and writes low-speed digital DAQ I/O data. | Low | A decimation of the PCL rate |
| Model Interface Loop | Reads and writes the lower-speed, asynchronous updates to model parameter values. | Low | Event driven |

Related concepts:

- Primary Control Loop Execution Steps

Related tasks:

- Configuring the VeriStand Engine

<!--NI_TOPIC bundle=veristand path=vs-engine_2.html language=enus -->
## TOPIC 00420: VeriStand Engine

- bundle_id: `veristand`
- source_path: `vs-engine_2.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/vs-engine_2.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VeriStand Engine is the execution mechanism that controls the timing of the entire system and the communication between the target and the host computer. The VeriStand Engine executes hardware I/O, runs models, procedures, alarms, and tests, and computes values in the channel table based on the

### VeriStand Engine

The VeriStand Engine is the execution mechanism that controls the timing of the
 entire system and the communication between the target and the host computer.

The VeriStand Engine executes
 hardware I/O, runs models, procedures, alarms, and tests, and computes values in the
 channel table based on the results of model execution and hardware I/O. This engine
 runs on either a desktop PC in simulation mode or as an embedded application on a RT
 system.

The VeriStand Engine consists of multiple timed loops that use
 real-time (RT) FIFOs to transfer data between the loops. Each loop performs
 designated tasks and has an assigned priority. Although you cannot change the
 priority or primary tasks of the engine loops, you can customize loop operations,
 such as the execution rate. The system definition file contains the configuration
 settings for the VeriStand Engine.

Note

The following figure illustrates the operation of the VeriStand
 Engine.

[IMAGE alt='image' src='GUID-E6E40161-67C2-4FAF-86B7-58523A9E53B4-a5.gif']

The following table displays the
 priority and default execution rate for the loops of the VeriStand Engine.

| VeriStand Engine loop | Description | Priority | Default execution rate |
| --- | --- | --- | --- |
| Primary Control Loop (PCL) | Controls the timing for the VeriStand Engine and maintains the most up-to-date table of channel values. Use System Explorer to set the execution mode of the PCL. Per iteration, the PCL executes the following tasks: Reads and writes high-speed FPGA I/O, analog and counter DAQ I/O, and Asynchronous Custom Device Loop data. Applies scaling to the data. Executes one step of the real-time sequence of a test that is currently running Sends data to the Data Processing Loop to synchronize the table of channel values. Sends data to the Model Execution Loop(s). Prompts the Data Processing Loop, Model Execution Loop(s), and Asynchronous Custom Device Loop(s) to execute. Performs software fault insertion. Creates mapping connections. Executes inline custom devices. Reads status information from the Waveform Processing Loop and DAQmx Waveform Producer Loop(s). Note For more information on the PCL, see Primary Control Loop Execution Steps | High | 100 Hz |
| Model Execution Loop(s) | Executes a corresponding compiled model. The number of models in the system definition determines the number of loops. Per iteration, each Model Execution Loop executes the following tasks: Reads the data sent by the PCL and maps this data to model inports. Executes one step of the model. Reads model outport values and sends this data to the PCL. Reads model inport signals and sends this data to the PCL. Note A Model Execution Loop handles high-speed, dynamic data associated with model inports and outports, while a Model Interface Loop reads and applies the lower-speed, asynchronous updates to model parameter values. | Medium | A decimation of the PCL rate |
| Asynchronous Custom Device Loop(s) | Executes and transmits custom device inport data values per iteration of the PCL. The VeriStand Engine is responsible for initiating the Asynchronous Custom Device Loop. | High Medium Low | User-defined |
| Waveform Processing Loop | Transfers waveform data through the system. Per iteration, the Waveform Processing Loop executes the following tasks: Reads waveform data from DAQmx Waveform Producer Loops. Sends waveform data to the VeriStand Gateway. Reads waveform data from custom devices. Sends waveform data to custom devices. | Low | Event driven |
| DAQmx Waveform Producer Loops | Acquires waveforms from DAQ devices. Each DAQmx Waveform Producer Loop corresponds to a waveform task in the system definition. Per iteration, Waveform Producer Loop executes the following tasks: Reads waveform data from analog input channels on DAQ devices. Sends waveform data to the Waveform Processing Loop. Logs acquired data to .tdms files. | Low | 10 Hz or user-defined |
| Data Processing Loop | Distributes the execution commands received by the Communication Receive Loop among the engine loops. Like the PCL, the Data Processing Loop maintains a complete copy of the channel values table. Per iteration, the Data Processing Loop executes the following tasks: Receives the table of channel values from the PCL. Executes procedures, alarms, and calculated channels. Transmits updated table of channel values to the PCL. Sends data values to the Communication Send Loop. | Medium | A decimation of the PCL rate |
| Communication Send Loop | Transmits channel values to the VeriStand Gateway. | Low | 15 Hz |
| Communication Receive Loop | Listens for execution commands that the VeriStand Gateway sends. | Low | Event driven |
| XNET Loop | Reads and writes XNET data. | Low | 100 Hz |
| DIO Loop | Reads and writes low-speed digital DAQ I/O data. | Low | A decimation of the PCL rate |
| Model Interface Loop | Reads and writes the lower-speed, asynchronous updates to model parameter values. | Low | Event driven |

<!--NI_TOPIC bundle=veristand path=while-loop.html language=enus -->
## TOPIC 00421: While Loop

- bundle_id: `veristand`
- source_path: `while-loop.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/while-loop.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Repeat a sequence of expressions while a Repeat While condition remains True. Use Auto Yield to release CPU time between iterations. Configure the code that executes in the loop by dragging expressions and other primitives to the loop and configuring them as you would any other section of sequence c

### While Loop

Repeat a sequence of expressions while a Repeat While condition remains True. Use
 Auto Yield to release CPU time between iterations.

Configure the code that executes in the loop by dragging expressions and other
 primitives to the loop and configuring them as you would any other section of
 sequence code.

| Property/Section | Description |
| --- | --- |
| Repeat While | Specifies the expression to evaluate to determine if the loop continues to execute. The loop executes as long as this expression evaluates to TRUE. |
| Auto Yield | If TRUE, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Loops

<!--NI_TOPIC bundle=veristand path=workspace-steps.html language=enus -->
## TOPIC 00422: Workspace Steps

- bundle_id: `veristand`
- source_path: `workspace-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/workspace-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reference information for the VeriStand Workspace steps used in stimulus profiles. Palette object Description Close VeriStand Workspace Closes the VeriStand workspace. Open VeriStand Workspace Opens the VeriStand Workspace and loads the screen (.nivsscreen) file associated with the currently active

### Workspace Steps

Reference information for the VeriStand Workspace steps used in stimulus
 profiles.

| Palette object | Description |
| --- | --- |
| Close VeriStand Workspace | Closes the VeriStand workspace. |
| Open VeriStand Workspace | Opens the VeriStand Workspace and loads the screen (.nivsscreen) file associated with the currently active VeriStand project. |
| Update Model Parameters from File | Updates parameter values for a simulation model to the values specified in a text (.txt) file. |

| Subpalette | Description |
| --- | --- |
| Workspace Tools Steps | Opens and communicates with Workspace tools directly from a stimulus profile. |

Parent topic:

VeriStand Control Steps

Related reference:

- Close VeriStand Workspace
- Update Model Parameters from File Step
- Workspace Tools Steps

<!--NI_TOPIC bundle=veristand path=workspace-tools-steps.html language=enus -->
## TOPIC 00423: Workspace Tools Steps

- bundle_id: `veristand`
- source_path: `workspace-tools-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/workspace-tools-steps.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reference information for Workspace Tools palette objects. Palette object Description Open Workspace Tool Opens the workspace tool specified by VI Path. Send Workspace Tool Message Sends a message or command to a workspace tool VI, as well as data required by the case in the tool that handles the co

### Workspace Tools Steps

Reference information for Workspace Tools palette objects.

| Palette object | Description |
| --- | --- |
| Open Workspace Tool | Opens the workspace tool specified by VI Path. |
| Send Workspace Tool Message | Sends a message or command to a workspace tool VI, as well as data required by the case in the tool that handles the command. |

Parent topic:

Workspace Steps

Related reference:

- Open Workspace Tool Step
- Send Workspace Tool Message

<!--NI_TOPIC bundle=veristand path=xnet-bus-monitor.html language=enus -->
## TOPIC 00424: NI-XNET Bus Monitor

- bundle_id: `veristand`
- source_path: `xnet-bus-monitor.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/xnet-bus-monitor.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-XNET Bus Monitor to display and log CAN, FlexRay, or LIN network data as either last recent data or historical data view. Use the Workspace to launch the NI-XNET Bus Monitor. To identify more detailed frame information, assign a network database to the NI-XNET Bus Monitor. You can display

### NI-XNET Bus Monitor

Use the NI-XNET Bus Monitor to display and log CAN, FlexRay, or LIN network data as
 either last recent data or historical data view.

Use the Workspace to launch the NI-XNET Bus Monitor.

To identify more detailed frame information, assign a network database to the NI-XNET Bus
 Monitor. You can display the message name and comment information in the
 Monitor view or ID Log view if you find a received frame in the database.

In addition to the network data, the NI-XNET Bus Monitor can provide statistical
 information. For offline data analysis, you can stream all received network data to disk
 in two log file formats.

You can launch the NI-XNET Bus Monitor from Measurement and Automation Explorer
 (MAX) or from the Windows Start menu.

For more information about the NI-XNET Bus Monitor, refer to the *NI-XNET
 Tools and Utilities Help*.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Enhancing Your Workspace to View Data

<!--NI_TOPIC bundle=veristand path=xnet-overview.html language=enus -->
## TOPIC 00425: NI-XNET Overview

- bundle_id: `veristand`
- source_path: `xnet-overview.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/xnet-overview.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use sessions, clusters, and frames to set up your NI-XNET interfaces. Refer to the NI-XNET Hardware and Software Help that installs with your hardware for more detailed documentation about NI-XNET interfaces. SessionsAn NI-XNET session represents a connection between your NI CAN, FlexRay, or LIN har

### NI-XNET Overview

Use sessions, clusters, and frames to set up your NI-XNET interfaces.

Note

NI-XNET Hardware and Software Help

#### Sessions

NI-XNET session

- Port —A port in NI-XNET refers to the physical connector on an
 NI hardware device.
- Interface —An interface represents the software CAN, FlexRay, or
 LIN connector on an NI hardware device. Use the interface name as an alias
 for your ports so you can avoiding changing your application if the physical
 hardware configuration changes.
- XNET Database —An XNET database is a standardized file that
 describes embedded communication. XNET database file formats include CANdb
 ( .dbc ) for CAN, FIBEX ( .xml ) for
 FlexRay, and LIN Description File ( .ldf ) for LIN. For the
 NI-XNET interface to communicate with hardware products on the external
 network, NI-XNET must understand the communication in the actual embedded
 system. You can edit NI-XNET databases directly from VeriStand by
 launching the NI-XNET Database
 Editor fromSystem Explorer.
- Session Mode —A session mode specifies the data type (signals or
 frames), direction (input or output), and how your application and network
 transfer data. VeriStand supports the following NI-XNET session modes: Note Refer to the
 *NI-XNET Hardware and Software Help* that installs with
 your hardware for more information about session modes.
  - Signal Input Single-Point
  - Signal Output Single-Point
  - Frame Input Single-Point
  - Frame Output Single-Point
  - Frame Input Stream

#### Clusters

A *cluster* is a description of a single network,
 such as a CAN bus, within an XNET database. For importing frames, each port in
 VeriStand is associated with a single cluster within an XNET database. A cluster can
 contain an arbitrary number of frames.

#### Frames

A *frame* is a message that transmits across an
 embedded network. In VeriStand, frames are either inputs (incoming frames) or
 outputs (outgoing frames), and are classified according to their transmission
 characteristics. For example, event-triggered frames transmit only when a specific
 event occurs. Frames also contain information such as ID numbers and timing data
 that you can access through Frame Information
 channels in VeriStand.

You can import frames into VeriStand in either signal
 or raw data format. Signal format frames contain *signals* and raw data
 format frames contain *channels*. These terms refer to the basic data
 exchange unit on the network.

The specific format and characteristics of
 frames vary based on the communication protocol you use. Refer to the *NI-XNET
 Hardware and Software Help* for detailed information about frame formats.

Parent topic:

Using NI-XNET Interfaces

Related tasks:

- Editing NI-XNET Databases
- Accessing Timing and ID Information for Incoming NI-XNET Frames

<!--NI_TOPIC bundle=veristand path=yield.html language=enus -->
## TOPIC 00426: Yield Primitive

- bundle_id: `veristand`
- source_path: `yield.html`
- source_url: https://docs-be.ni.com/bundle/veristand/raw/resource/enus/yield.html
- document_id: `veristand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses a real-time sequence while the Primary Control Loop iterates, then resumes sequence execution. In a multi-tasking real-time sequence, this statement causes the current task to complete the current step and yield control of the CPU to the next task, if one exists. Property/Section Description

### Yield Primitive

Pauses a real-time sequence while the Primary Control Loop iterates, then resumes
 sequence execution.

In a multi-tasking real-time sequence, this statement causes the current task to
 complete the current step and yield control of the CPU to the next task, if one
 exists.

| Property/Section | Description |
| --- | --- |
| Description | Specifies a description for the current item. This text appears when you hover over the item in the Stimulus Profile Editor. |

Parent topic:

Advanced Primitives
