# NI DOCUMENT BUNDLE: vision-builder-automated-inspection

<!--NI_BUNDLE_CHUNK bundle=vision-builder-automated-inspection start=1 end=59 -->
<!--NI_TOPIC bundle=vision-builder-automated-inspection path=acquire-an-image-from-a-windows-device.html language=enus -->
## TOPIC 00001: Acquire an Image from a Windows Device

- bundle_id: `vision-builder-automated-inspection`
- source_path: `acquire-an-image-from-a-windows-device.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/acquire-an-image-from-a-windows-device.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: With Vision Builder AI you can acquire an image through the following Windows devices: GigE Vision IEE 1394 USB camera Camera link Parallel digital camera Analog camera If you use a Windows Smart Camera, refer to Acquire an Image with the NI Smart Camera.

### Acquire an Image from a Windows Device

- GigE Vision
- IEE 1394
- USB camera
- Camera link
- Parallel digital camera
- Analog camera

Note

Acquire an Image with the NI Smart Camera

Parent topic:

Acquiring Images in Vision Builder AI

Related concepts:

- Acquire an Image with the NI Smart Camera

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=acquire-an-image-with-an-ni-compact-vision-sy.html language=enus -->
## TOPIC 00002: Acquire an Image with an NI Compact Vision System

- bundle_id: `vision-builder-automated-inspection`
- source_path: `acquire-an-image-with-an-ni-compact-vision-sy.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/acquire-an-image-with-an-ni-compact-vision-sy.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to acquire an image with a real-time NI Compact Vision System or Industrial Controller in Vision Builder AI:On Windows devices, select My Computer as the target to run Vision Builder AI. Refer to Acquire an Image from a Windows Device for instructions on acquiring an ima

### Acquire an Image with an NI Compact Vision
 System

Note

My Computer

Acquire an
 Image from a Windows Device

1. Launch Vision Builder AI.
2. Select the Compact Vision System or Industrial
 Controller from the list of available targets.
3. In the Configure Inspection section, select
 New Inspection from Template.
4. Select Acquire Image Template from the
 Compact Vision System tree.
5. Click the Run Inspection Once icon to acquire an image.

Parent topic:

Acquiring Images in Vision Builder AI

Related concepts:

- Troubleshooting the NI Compact Vision System or Industrial Controller
- Acquire an Image from a Windows Device

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=acquire-an-image-with-the-ni-smart-camera.html language=enus -->
## TOPIC 00003: Acquire an Image with the NI Smart Camera

- bundle_id: `vision-builder-automated-inspection`
- source_path: `acquire-an-image-with-the-ni-smart-camera.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/acquire-an-image-with-the-ni-smart-camera.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: On the Vision Builder AI welcome screen, select the NI Smart Camera in the list of targets.For Windows Smart Cameras, select My Computer. Click Acquire Image (Smart Camera) Example to open the image acquisition example in the Vision Builder AI Configuration Interface.For Windows Smart Cameras, click

### Acquire an Image with the NI Smart
 Camera

1. On the Vision Builder AI welcome screen, select the NI Smart Camera in
 the list of targets. Note For Windows Smart Cameras, select My Computer.
2. Click Acquire Image (Smart Camera) Example to open the image acquisition
 example in the Vision Builder AI Configuration
 Interface . Note For Windows Smart Cameras, click New
 Inspection, which opens the Vision Builder AI
 Configuration Interface. Select the
 Acquire Image (Smart Camera) step to configure the
 acquisition settings for the smart camera and to add the acquisition step to the
 inspection.
3. Click the Run State Once 
 ([IMAGE alt='image' src='GUID-9C73BD0A-1C97-4164-8CF6-4CF57273103E-a5.gif']) button to acquire a single
 image.
4. In the State Configuration window, double-click the Acquire
 Image (Smart Camera) step to open the property page.
5. Use the controls on the Main , Trigger , Lighting , and Advanced tabs
to configure any additional settings necessary for your application.
6. Click OK to save the step configuration.

To process acquired images, add additional steps to the inspection. Select Help»Show Context Help for information about the settings available for each step.

Parent topic:

Acquiring Images in Vision Builder AI

Related concepts:

- Troubleshooting the NI Smart Camera

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=adding-steps-to-inspections.html language=enus -->
## TOPIC 00004: Adding a Step to an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `adding-steps-to-inspections.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/adding-steps-to-inspections.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: In the Inspection Steps palette, click the step you want to add to the inspection. Configure the step according to the instructions in the Context Help window Configuration tab. Click OK to add the step to the inspection.

### Adding a Step to an Inspection

1. In the Inspection Steps palette, click the step you want
 to add to the inspection.
2. Configure the step according to the instructions in the Context
 Help window Configuration tab.
3. Click OK to add the step to the inspection.

Parent topic:

Manage Inspection Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=backup-execution-target-info.html language=enus -->
## TOPIC 00005: Backup Execution Target Information

- bundle_id: `vision-builder-automated-inspection`
- source_path: `backup-execution-target-info.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/backup-execution-target-info.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Vision Builder AI allows you to create a target image of a remote target for backup configuration. Target images contain all of the current configuration settings for a remote target and all of the inspections currently installed to the remote target. Target images are useful to backup configuration

### Backup Execution Target Information

Vision Builder AI allows you to create a target image of a remote target for backup
 configuration.

Target images contain all of the current configuration settings for a remote target
 and all of the inspections currently installed to the remote target. Target images
 are useful to backup configuration settings or to deploy the same configuration
 settings to multiple remote targets.

1. Complete one of the following actions: 
 OptionDescriptionIf you are currently connected to a remote target
 Select Target»Create Target Image to launch the Create Target
 Image dialog box.
 Enter information about the inspection and the location where
 you want to save the image.
 Click OKIf you are not currently connected to a remote target
 On the Vision Builder AI welcome screen, select
 Select Network Target from the
 Execution Target list.
 In the Select Remote Target dialog box,
 right-click the target for which you want to create an
 image.
 Enter information about the inspection and the location where
 you want to save the image.
 Click OK.
2. Restart the target.

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=benchmarking-inspection-performance.html language=enus -->
## TOPIC 00006: Benchmarking Inspection Performance

- bundle_id: `vision-builder-automated-inspection`
- source_path: `benchmarking-inspection-performance.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/benchmarking-inspection-performance.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the benchmark inspection tool to estimate how many milliseconds the image analysis steps of your inspection take to complete on the active image. The benchmark inspection tool does not account for events such as user input or waiting for an external signal or device. These processes may

### Benchmarking Inspection Performance

You can use the benchmark inspection tool to estimate how many milliseconds the image
 analysis steps of your inspection take to complete on the active image.

The benchmark inspection tool does not account for events such as user input or waiting for
 an external signal or device. These processes may be time intensive or dependant on external
 conditions. Therefore, these processes may significantly reduce the maximum rate at which
 you can run the inspection, and the speed of some steps may vary depending on the image you
 process.

Follow these instructions to benchmark the processing time of an inspection:

1. Open the inspection whose processing time you want to evaluate.
2. Select Operate»Benchmark Inspection to launch the Benchmark Inspection dialog box.
3. In the Number of runs control, specify the number of times to run the complete inspection for the benchmarking calculations. 
 Note The estimated completion time
 is accurate when connected to a target since the inspection is run on the target.
4. Click OK to close the dialog box.

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=camera-link-parallel-digital-or-analog-camera.html language=enus -->
## TOPIC 00007: Acquiring an Image with a Camera Link, Parallel Digital, or Analog Camera

- bundle_id: `vision-builder-automated-inspection`
- source_path: `camera-link-parallel-digital-or-analog-camera.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/camera-link-parallel-digital-or-analog-camera.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: On the Vision Builder AI welcome screen, select My Computer. Click Acquire Image (NI-IMAQ frame grabber) Example to open the image acquisition example in the Vision Builder AI Configuration Interface. Click the Run State Once () button to acquire a single image. In the State Configuration window, do

### Acquiring an Image with a Camera Link,
 Parallel Digital, or Analog Camera

1. On the Vision Builder AI welcome screen, select My
 Computer.
2. Click Acquire Image (NI-IMAQ frame grabber)
 Example to open the image acquisition
 example in the Vision Builder AI Configuration
 Interface.
3. Click the Run State Once
 ([IMAGE alt='image' src='GUID-9C73BD0A-1C97-4164-8CF6-4CF57273103E-a5.gif']) button to acquire a single image.
4. In the State Configuration window,
 double-click the Acquire Image step
 to open the property page.
5. Use the controls on the Main, Image
 Trigger, Line Trigger, and
 Calibration tabs to configure any additional settings
 necessary for your application.
6. Click OK to save the step configuration.

To process acquired images, add additional steps to the inspection. Select Help»Show Context Help for information about the settings available for each
 step.

Parent topic:

Acquire an Image from a Windows Device

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=configuration-interface.html language=enus -->
## TOPIC 00008: Elements of the Configuration Interface

- bundle_id: `vision-builder-automated-inspection`
- source_path: `configuration-interface.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/configuration-interface.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configuration Interface to configure and debug an inspection. 1 Vision Builder AI Configuration Interface Main window (1) Displays the image being processed, property pages for some inspection steps, or the state diagram for the inspection. Use the Main window to define regions of interest i

### Elements of the Configuration
 Interface

Use the Configuration Interface to configure and debug an
 inspection.

Figure 1.

[IMAGE alt='image' src='GUID-B1B74D0D-ED0D-4FF6-9380-DE8AC9CDA24D-a5.gif']

Main window

Main window

Overview window

Inspection Steps palette

State Configuration window

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=configuring-a-remote-target.html language=enus -->
## TOPIC 00009: Configuring a Remote Target

- bundle_id: `vision-builder-automated-inspection`
- source_path: `configuring-a-remote-target.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/configuring-a-remote-target.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: If prompted, click Configure Target. If the remote target is password-protected, Vision Builder AI prompts you to enter the administrator password. Enter a Name and Description for the remote target, and click Next. Device names are limited to 31 characters with no spaces or special characters, exce

### Configuring a Remote Target

1. If prompted, click Configure Target.
2. If the remote target is password-protected, Vision Builder AI prompts you to
 enter the administrator password.
3. Enter a Name and Description for the remote
 target, and click Next. 
 Device names are limited to 31 characters with no spaces or special
 characters, except hyphens. The first and last characters must be
 alphanumeric.
4. Select an IP address. 
 If your remote target is on a network that has a DHCP server, you may be able
 to automatically obtain an IP address from the DHCP server. A DHCP server
 allocates an IP address to the remote target each time the target is
 restarted. If you select the DHCP Server option, you do not
 need to specify other information, such as the Subnet Mask. If you do not
 know if the network has a DHCP server, check with a network administrator
 for assistance.
 To automatically obtain an IP address, select Obtain IP address
 from DHCP Server.
 To assign a static IP address to the remote target, select Edit
 the IP Settings and enter the following information:
 IP address
 Subnet Mask
 Gateway
 DNS serverNote Consult a network
 administrator before modifying these parameters.If you
 want to set the IP address without a DHCP server but are uncertain
 about the settings, click Suggest Values.
 Vision Builder AI attempts to detect the appropriate settings. Click
 Reset to Default to revert to the
 original settings.
5. Click Next.

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=create-new-remote-target-inspection.html language=enus -->
## TOPIC 00010: Create a New Remote Target Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `create-new-remote-target-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/create-new-remote-target-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a new inspection for a remote target, simulation mode allows you to specify values for controls that can be set without connecting to a remote target. For example, while simulating an IC-3173, the Acquire Image (1394, GigE, or USB) step allows you to specify a Step Name and an Acquis

### Create a New Remote Target Inspection

When you create a new inspection for a remote target, simulation mode allows you to
 specify values for controls that can be set without connecting to a remote target.

For example, while simulating an IC-3173, the Acquire Image (1394, GigE, or
 USB) step allows you to specify a Step Name and an
 Acquisition Mode, but the step does not allow you to specify camera
 attribute values because Vision Builder AI does not know which camera is connected to
 the target device where the inspection runs.

When you deploy a new inspection for the first time, Vision Builder AI prompts you to
 configure any hardware specific settings that were unavailable in simulation mode.

Parent topic:

Simulating Remote Targets

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=creating-inspections-from-templates.html language=enus -->
## TOPIC 00011: Creating an Inspection from a Template

- bundle_id: `vision-builder-automated-inspection`
- source_path: `creating-inspections-from-templates.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/creating-inspections-from-templates.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File New From Template to launch the Create New Inspection from Template dialog box. By default, only templates for the selected target are displayed. To view templates for all targets, select Show inspection templates for all targets. Select the template that you want to use to create a new

### Creating an Inspection from a Template

1. Select File»New From Template to launch the Create New Inspection from
 Template dialog box. 
 By default, only templates for the selected target are displayed. To view
 templates for all targets, select Show inspection templates for
 all targets.
2. Select the template that you want to use to create a new inspection. 
 By default, inspection templates are installed to c:\Program
 Files\National Instruments\<Vision Builder AI
 version>\Templates. Double-click Browse
 to load an inspection template from another location.
3. Click OK.

Vision Builder AI loads the selected inspection template as an untitled
 inspection.

Parent topic:

Manage Templates

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=creating-new-inspection-var.html language=enus -->
## TOPIC 00012: Creating a New Inspection Variable

- bundle_id: `vision-builder-automated-inspection`
- source_path: `creating-new-inspection-var.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/creating-new-inspection-var.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Inspection variables can only be used in the inspection they are created in. They cannot be accessed by other inspections. Click Inspection Variables tab. Click Add to launch the Add Inspection Variable dialog box. Enter a descriptive Name for the variable. Specify a Type for the variable. Numeric v

### Creating a New Inspection Variable

Inspection variables can only be used in the inspection
 they are created in. They cannot be accessed by other inspections.

1. Click Inspection Variables tab.
2. Click Add to launch the Add Inspection
 Variable dialog box.
3. Enter a descriptive Name for the variable.
4. Specify a Type for the variable. 
 Note Numeric
 variables are defined as double-precision floating point numbers. Point
 variables consist of two numeric values, one for the x-coordinate value and
 one for the y-coordinate value.
5. Specify an Initial Value for the variable.
6. Click OK to close the dialog box and create the
 variable.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=creating-new-inspection.html language=enus -->
## TOPIC 00013: Creating a New Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `creating-new-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/creating-new-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: To create a new inspection, select File New or click the New () button on the toolbar. If you have not saved the current inspection, Vision Builder AI will prompt you to save it before creating a new inspection.

### Creating a New Inspection

To create a new
 inspection, select File»New or click the New([IMAGE alt='image' src='GUID-A17C5AD1-5060-4A5B-9719-6D96ED9ADAF2-a5.gif'])
 button on the toolbar.

Note

Parent topic:

Manage Inspections

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=creating-new-network-variable.html language=enus -->
## TOPIC 00014: Creating a New Network Variable

- bundle_id: `vision-builder-automated-inspection`
- source_path: `creating-new-network-variable.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/creating-new-network-variable.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Network variables can be accessed by any device on the network that supports LabVIEW variables. Click the Network Variables tab. Click Add to launch the Add Network Variable dialog box. Enter a descriptive Name for the variable. Click the Select Source Item () button and select the source to use for

### Creating a New Network Variable

Network variables can be accessed by any device on the
 network that supports LabVIEW variables.

1. Click the Network Variables tab.
2. Click Add to launch the Add Network Variable
 dialog box.
3. Enter a descriptive Name for the variable.
4. Click the Select Source Item
 ([IMAGE alt='image' src='GUID-BCEDF3FF-C35D-4D36-AA84-4B88AEAAA955-a5.gif']) button and select the source to use for
 the value of the network variable.
5. Specify a Type for the variable. 
 Note Numeric
 variables are defined as double-precision floating point numbers. Point
 variables consist of two numeric values, one for the x-coordinate value and
 one for the y-coordinate value.
6. Specify the Access Type for the variable.
7. If necessary, enable the Use Buffering control to buffer the
 value of the variable.
8. Specify the Timeout to use when communicating with the
 variable.
9. Click OK to close the dialog box and create the
 variable.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=creating-new-system-var.html language=enus -->
## TOPIC 00015: Creating a New System Variable

- bundle_id: `vision-builder-automated-inspection`
- source_path: `creating-new-system-var.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/creating-new-system-var.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: System variables are limited to the device on which an inspection is deployed.Multiple inspections can access the same system variable if they are deployed on the same device. If the variable is published on a network, multiple instances across different devices can also access it.Use the Set Inspec

### Creating a New System Variable

System variables are limited to the device on which an
 inspection is deployed.

Multiple inspections can access the same system
 variable if they are deployed on the same device. If the variable is published on a
 network, multiple instances across different devices can also access it.

Note

Set Inspection Status

1. Click the System Variables tab.
2. Click Add to launch the Add System
 Variable dialog box.
3. Enter a descriptive Name for the variable.
4. Specify a Type for the variable. 
 Note Numeric
 variables are defined as double-precision floating point numbers.
5. Specify an Initial Value for the variable.
6. Enable the Publish on Network control if you want to access
 the variable from another device on the same network. Use the Use
 Buffering and Buffer Size controls to
 specify the buffer settings for system variables published on a network.
7. Click OK to close the dialog box and create the
 variable.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=edit-existing-inspection.html language=enus -->
## TOPIC 00016: Edit an Existing Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `edit-existing-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/edit-existing-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you open an existing inspection that has been configured for a remote target, simulation mode allows you to view and modify the inspection settings. When the inspection is redeployed to a remote target, the inspection uses the modified settings. When you are connected to a target in configurati

### Edit an Existing Inspection

When you open an existing inspection that has been configured for a remote target,
 simulation mode allows you to view and modify the inspection settings. When the
 inspection is redeployed to a remote target, the inspection uses the modified
 settings.

When you are connected to a target in configuration mode, and select Target»Add/Retrieve Inspections... from the menu, you can copy inspections to or from the target. Any
 cameras, or communication devices used by the target inspection will be saved as part of
 the inspection when copied to Windows. When simulation mode is used to open this
 inspection on Windows, it will have access to all same cameras and communication devices
 the inspection was using on the target. Any changes made to the communication devices in
 simulation mode will update the settings in the inspection. When the inspection is
 copied back to the target, any changes may require reconciling when the inspection is
 opened on the target.

Parent topic:

Simulating Remote Targets

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=editing-existing-var.html language=enus -->
## TOPIC 00017: Editing an Existing Variable

- bundle_id: `vision-builder-automated-inspection`
- source_path: `editing-existing-var.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/editing-existing-var.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Variable Manager to modify the settings of an existing variable. Click Reset to Initial to reset the variables in the selected tab to their initial values. You can also use the View Measurements tool to change the current value of variables, or even results of steps. Select the variable you

### Editing an Existing Variable

Use the Variable Manager to modify the settings of an
 existing variable.

Note

Reset
 to Initial

View Measurements

1. Select the variable you want to edit from the Variable
 Manager.
2. Click Edit to launch the Edit
 Variable dialog box.
3. Modify the variable control settings.
4. Click OK to close the dialog box and update the variable
 settings. 
 Note Changing the
 initial value of a variable doesn't modify the current value. Click
 Reset to Initial Value to reset all variables on
 the selected tab to their initial values. You can also change individual
 variable values from the Tools»View Measurements window by double clicking on the variables value and editing
 the value.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=exporting-variables.html language=enus -->
## TOPIC 00018: Exporting Variables

- bundle_id: `vision-builder-automated-inspection`
- source_path: `exporting-variables.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/exporting-variables.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Export button to export variables to a tab-delimited .txt file. Click the Export button. Specify a location to save the tab-delimited file.

### Exporting Variables

Export

.txt

1. Click the Export button.
2. Specify a location to save the tab-delimited file.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=file-format-of-import-export-var.html language=enus -->
## TOPIC 00019: File Format of Import/Export Variables

- bundle_id: `vision-builder-automated-inspection`
- source_path: `file-format-of-import-export-var.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/file-format-of-import-export-var.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Import and Export buttons create or expect a tab delimited .txt file. Each line of the file describes a variable, and is formatted as follows: Variable Name <tab> Inspection <tab> Data Type <tab> <Initial Value (0 “” False)> Variable Name <tab> System <tab> Data Type <tab> <Initial Value (0 “” F

### File Format of Import/Export Variables

The Import and Export buttons
 create or expect a tab delimited .txt file.

Each line of the file describes a variable, and is formatted as follows:

Variable Name <tab> Inspection <tab> Data Type <tab>
 <Initial Value (0 “” False)>

Variable Name <tab> System <tab> Data Type <tab>
 <Initial Value (0 “” False)> <tab> <Shared
 (False)> <tab> <Use Buffering (False)> <tab>
 <Buffer Size (1)>

Variable Name <tab> Network <tab> Data Type <tab>
 Network Path <tab> <Access Type (Read/Write)>
 <tab> <Use Buffering (False)> <tab> <Timeout
 (1000 ms)>

The # Uses column indicates the number of times this variable is used in
 the inspection. Click the Where Used button to see
 the locations in the inspection where the variable is used.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=file-system-on-real-time-targets.html language=enus -->
## TOPIC 00020: Using the File System on Real-Time Targets

- bundle_id: `vision-builder-automated-inspection`
- source_path: `file-system-on-real-time-targets.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/file-system-on-real-time-targets.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: While other LabVIEW RT targets follow Microsoft Windows-style conventions, the file system of Linux Real-Time targets follows conventions established for UNIX-style operating systems. You must use WebDAV to transfer files to and from a real-time target. The following table provides Vision Builder AI

### Using the File System on Real-Time
 Targets

While other LabVIEW RT targets follow Microsoft Windows-style conventions, the file
 system of Linux Real-Time targets follows conventions established for UNIX-style
 operating systems.

Note

The following table provides Vision Builder AI file path references on Real-Time
 targets:

|  | CVS-1458/1459, IC-312x, IC-317x |
| --- | --- |
| User VIs | /home/lvuser/natinst/vbai/User VIs |
| User Images | /home/lvuser/natinst/vbai/User Images |

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=getting-started-config-interface.html language=enus -->
## TOPIC 00021: Getting Started with the Configuration Interface

- bundle_id: `vision-builder-automated-inspection`
- source_path: `getting-started-config-interface.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/getting-started-config-interface.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Run an inspection from the Configuration Interface during development to test and debug inspections.

### Getting Started with the Configuration
 Interface

Run an inspection from the Configuration Interface during
 development to test and debug inspections.

- [Elements of the Configuration Interface](configuration-interface.html)
- [Switching Between the Configuration and Inspection Interfaces](switching-between-the-configuration-and-inspe.html)
- [Manage Images](manage-images.html)
- [Manage Inspections](manage-inspections.html)
- [Manage Templates](manage-templates.html)
- [Benchmarking Inspection Performance](benchmarking-inspection-performance.html)
- [Acquiring Images in Vision Builder AI](help-me-acquire-my-first-image-in-vision-buil.html)

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=gige-vision-iee1394-or-usb-camera.html language=enus -->
## TOPIC 00022: Acquiring an Image with a GigE Vision, IEEE 1394, or USB Camera

- bundle_id: `vision-builder-automated-inspection`
- source_path: `gige-vision-iee1394-or-usb-camera.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/gige-vision-iee1394-or-usb-camera.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: On the Vision Builder AI welcome screen, select My Computer. Click Acquire Image from IEEE 1394 GigE Vision or USB Camera Example to open the image acquisition example in the Vision Builder AI Configuration Interface. Click the Run State Once () button to acquire a single image. In the State Configu

### Acquiring an Image with a GigE Vision, IEEE
 1394, or USB Camera

1. On the Vision Builder AI welcome screen, select My
 Computer.
2. Click Acquire Image from IEEE 1394 GigE Vision or
 USB Camera Example to open the image
 acquisition example in the Vision Builder AI
 Configuration
 Interface.
3. Click the Run State Once
 ([IMAGE alt='image' src='GUID-9C73BD0A-1C97-4164-8CF6-4CF57273103E-a5.gif'])
 button to acquire a single image.
4. In the State Configuration window,
 double-click the Acquire Image (1394, GigE, or
 USB) step to open the property
 page.
5. Use the controls on the Main,
 Attributes, and Calibration
 tabs to configure any additional settings necessary for your application.
6. Click OK to save the step configuration.

To process acquired images, add additional steps to the inspection. Select Help»Show Context Help for information about the settings available for each
 step.

Parent topic:

Acquire an Image from a Windows Device

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=GUID-930FF1B1-0285-4462-BA95-B8F09357ABFB.html language=enus -->
## TOPIC 00023: Importing Variables

- bundle_id: `vision-builder-automated-inspection`
- source_path: `GUID-930FF1B1-0285-4462-BA95-B8F09357ABFB.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/GUID-930FF1B1-0285-4462-BA95-B8F09357ABFB.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Import button to import variables from a tab-delimited .txt file.Vision Builder AI displays a summary of the number of variables imported, and any warning and error messages that occurred during import. Warnings occur if the imported file contains syntax errors or type mismatches between the

### Importing Variables

Use the Import button to import variables from a tab-delimited
 .txt file.

Vision Builder AI displays a summary of
 the number of variables imported, and any warning and error messages that occurred
 during import. Warnings occur if the imported file contains syntax errors or type
 mismatches between the variable type and the value specified. Errors occur if there
 are spelling errors in the scope or type of variables, or a variable is already
 defined.

Note

1. Click the Import button. 
 Tip Export variables
 to see the format of the tab-delimited file.
2. Select the tab-delimited file source to import variables from. 
 Tip Select
 Copy to Clipboard to copy the import summary data
 as a tab-delimited file.

Parent topic:

Variable Manager

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=help-me-acquire-my-first-image-in-vision-buil.html language=enus -->
## TOPIC 00024: Acquiring Images in Vision Builder AI

- bundle_id: `vision-builder-automated-inspection`
- source_path: `help-me-acquire-my-first-image-in-vision-buil.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/help-me-acquire-my-first-image-in-vision-buil.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: With Vision Builder AI you can inspect images by uploading them from a variety of cameras, including the NI Smart Camera and any cameras connected to Windows devices, Real-Time Compact Vision Systems, or industrial controllers.The following topics provide information on how to acquire images with di

### Acquiring Images in Vision Builder AI

With Vision Builder AI you can inspect images by uploading them from a variety of
 cameras, including the NI Smart Camera and any cameras connected to Windows devices,
 Real-Time Compact Vision Systems, or industrial controllers.

The following topics provide information on how to acquire images with different types of
 hardware:

- [Acquire an Image with the NI Smart Camera](acquire-an-image-with-the-ni-smart-camera.html)
- [Acquire an Image from a Windows Device](acquire-an-image-from-a-windows-device.html)
- [Acquire an Image with an NI Compact Vision System](acquire-an-image-with-an-ni-compact-vision-sy.html)

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=how-to-use-the-color-palette-editor.html language=enus -->
## TOPIC 00025: How to Use the Color Palette Editor

- bundle_id: `vision-builder-automated-inspection`
- source_path: `how-to-use-the-color-palette-editor.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/how-to-use-the-color-palette-editor.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: The Color Palette Editor enables you to apply a specified color palette to monochrome images which is useful for 16-bit grayscale images for medical, scientific, or temperature monitoring applications.Once you configure a color palette, all steps in the Vision Builder AI inspection use the same pale

### How to Use the Color Palette Editor

The Color Palette Editor enables you to apply a specified color palette to monochrome images
 which is useful for 16-bit grayscale images for medical, scientific, or temperature
 monitoring applications.

Once you configure a color palette, all steps in the Vision Builder AI inspection use the same
 palette. Take the following steps to configure a color palette:

1. In the Image Acquisition step, click [IMAGE alt='image' src='GUID-8D69157C-6484-49B7-9522-EEE0DB1CB3DE-a5.gif'] or
 [IMAGE alt='image' src='GUID-635658C6-4F4F-43E4-97C3-B9FE5FD3159E-a5.gif']
 in the toolbar above the main display window to open the Color
 Palette Editor. 
 To create a new palette, click [IMAGE alt='image' src='GUID-8D69157C-6484-49B7-9522-EEE0DB1CB3DE-a5.gif'].
 To edit an existing palette, use the pull-down menu next to the
 New Palette button to select a palette, and
 then click [IMAGE alt='image' src='GUID-635658C6-4F4F-43E4-97C3-B9FE5FD3159E-a5.gif'].
2. Enter a unique name for the palette in Color Palette Name.
3. Select a default palette to apply to the image using the Start from Palette drop-down menu. Click Apply to apply the palette to the Color Palette Samples table.
4. Use the Interpolation Method pull-down menu to specify the interpolation technique used to color the image. When you select a new Interpolation Method, the Grayscale to Color Mapping Graphs change.
5. Select a sample in the Color Palette Samples table to assign a specific color to a grayscale value. You can also drag the vertical lines in the Grayscale to Color Mapping Graphs to configure grayscale values. Use the Add, Delete, and Sort buttons below the table to add, delete, or reorder samples.
6. Click Preview to view a preview of the configured settings in the main display window.
7. Close the Color Palette Editor by clicking
 OK or Cancel.
8. To delete a palette, select the pull-down menu next to the New
 Palette button, and click [IMAGE alt='image' src='GUID-E19BCD13-4B37-4EF2-A3D1-0ACD32D288A5-a5.gif']. 
 Custom palettes are saved in the <Program Data>\National
 Instruments\Vision Builder AI\Palettes folder.

Parent topic:

Using Vision Builder AI Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=installing-software-to-remote-target.html language=enus -->
## TOPIC 00026: Installing Software to a Remote Target

- bundle_id: `vision-builder-automated-inspection`
- source_path: `installing-software-to-remote-target.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/installing-software-to-remote-target.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: If prompted, click Install Software. Enable the Update Target Software checkbox. Vision Builder AI automatically selects the appropriate software image for the selected remote target. If you want to select a different software image, click the Browse () button and navigate to the software image that

### Installing Software to a Remote Target

1. If prompted, click Install Software.
2. Enable the Update Target Software checkbox. 
 Note Vision
 Builder AI automatically selects the appropriate software image for the
 selected remote target. If you want to select a different software image,
 click the Browse
 ([IMAGE alt='image' src='GUID-4E8EFA93-5D13-42D9-9D22-77FD7227F0B8-a5.gif']) button and navigate to the software
 image that you want to use.
3. To remove any existing software, inspections, images, and log files currently
 on the remote target before installing the new software, enable the
 Format Target Before Installing Software
 control. 
 Caution Formatting
 removes all data stored on the remote target. Backup any important data from
 the remote target before enabling the Format Target Before
 Installing Software control.
4. Click OK to install the software on the remote
 target.

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=manage-images.html language=enus -->
## TOPIC 00027: Manage Images

- bundle_id: `vision-builder-automated-inspection`
- source_path: `manage-images.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/manage-images.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about image handling in Vision Builder AI:

### Manage Images

The following sections contain information about image handling in Vision Builder AI:

- [Opening an Image](opening-an-image.html)
- [Saving an Image](saving-an-image.html)
- [Printing an Image](printing-an-image.html)
- [Viewing Options](viewiing-options.html)

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=manage-inspection-steps.html language=enus -->
## TOPIC 00028: Manage Inspection Steps

- bundle_id: `vision-builder-automated-inspection`
- source_path: `manage-inspection-steps.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/manage-inspection-steps.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each state in an inspection is intended to contain a separate set of inspection steps. To manage these steps, read the following sections:

### Manage Inspection Steps

Each state in an inspection is intended to contain a separate set of inspection steps. To
 manage these steps, read the following sections:

- [Adding a Step to an Inspection](adding-steps-to-inspections.html)
- [Removing a Step from an Inspection](removing-steps-from-inspections.html)
- [Modifying a Step in an Inspection](modifying-steps-in-inspections.html)

Parent topic:

Using Vision Builder AI Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=manage-inspections.html language=enus -->
## TOPIC 00029: Manage Inspections

- bundle_id: `vision-builder-automated-inspection`
- source_path: `manage-inspections.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/manage-inspections.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about options for running an inspection in Vision Builder AI:

### Manage Inspections

The following sections contain information about options for running an inspection in Vision
 Builder AI:

- [Creating a New Inspection](creating-new-inspection.html)
- [Opening an Inspection](opening-an-inspection.html)
- [Saving an Inspection](saving-an-inspection.html)
- [Printing an Inspection](printing-an-inspection.html)
- [Modifying Inspection Properties](modifying-inspection-prop.html)

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=manage-templates.html language=enus -->
## TOPIC 00030: Manage Templates

- bundle_id: `vision-builder-automated-inspection`
- source_path: `manage-templates.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/manage-templates.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Vision Buidler AI, templates are patterns that you are trying to match in an image. A template can be a region selected from an image or it can be an entire image. The following sections contain information about the basics of using templates in Vision Builder AI:

### Manage Templates

In Vision Buidler AI, templates are patterns that you are trying to match in an image. A
 template can be a region selected from an image or it can be an entire image.

The following sections contain information about the basics of using templates in
 Vision Builder AI:

- [Creating an Inspection from a Template](creating-inspections-from-templates.html)
- [Saving an Inspection as a Template](saving-inspections-as-templates.html)

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=managing-inspections-between-the-host-and-rem.html language=enus -->
## TOPIC 00031: Managing Inspections Between the Host and Remote Target

- bundle_id: `vision-builder-automated-inspection`
- source_path: `managing-inspections-between-the-host-and-rem.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/managing-inspections-between-the-host-and-rem.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click Target Add/Retrieve Inspections to launch the Inspection Manager dialog box. This menu item is available only when you are connected to a remote target.The Inspection Manager dialog box contains a list of inspections on the host computer, a list of inspections on the remote target, and details

### Managing Inspections Between the Host and
 Remote Target

1. Click Target»Add/Retrieve Inspections to launch the Inspection Manager dialog box.
 Note This menu item
 is available only when you are connected to a remote target. The
 Inspection Manager dialog box contains a list of
 inspections on the host computer, a list of inspections on the remote target, and
 details about the selected inspection.
2. Select the inspection you want to copy or delete in the This Computer list or the Remote Device list.
3. Click Copy or Delete .
4. Click Done to close the Inspection Manager dialog
 box.

Parent topic:

Working with Remote Targets

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=migrating-an-inspection-to-labview.html language=enus -->
## TOPIC 00032: Migrating an Inspection to LabVIEW

- bundle_id: `vision-builder-automated-inspection`
- source_path: `migrating-an-inspection-to-labview.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/migrating-an-inspection-to-labview.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure LabVIEW and Vision Builder AI to migrate inspections between them.You can migrate an inspection from Vision Builder AI to LabVIEW under the following conditions: You have installed the required version of LabVIEW and the Vision Development Module as listed in the Vision Builder for Automat

### Migrating an Inspection to LabVIEW

Configure LabVIEW and Vision Builder AI to migrate inspections between them.

You can migrate an inspection from Vision Builder AI to LabVIEW under the following
 conditions:

- You have installed the required version of LabVIEW and the Vision Development Module as listed
 in the Vision Builder for Automated Inspection Readme .
- You launched LabVIEW at least once.
- If your Vision Builder AI inspection uses a step that requires a driver, you must download and install a version of the driver that supports the LabVIEW version that you are migrating to.

Follow these steps for the migration:

1. Select Tools»Migrate Inspection to LabVIEW . Vision Builder AI opens the LabVIEW VI
 Creation dialog box.
2. Select which versions of LabVIEW and Vision to use to create the VI.
3. Select a folder to save the VI.
4. Click OK to migrate the inspection to LabVIEW.

Note

Match
 Pattern

Detect Defects

Configuration Files

Refer to the *Vision Builder for Automated Inspection Readme* for a list of steps that
 require additional software to migrate to LabVIEW.

Note

NI-IMAQ

NI-IMAQdx

NI-IMAQ I/O

#### FAQs

Q: To which version of LabVIEW can I migrate my Vision Builder AI
 inspection?

Refer to the *Vision Builder for Automated Inspection
 Readme* for the latest LabVIEW version that Vision Builder AI migrates
 to.

If your Vision Builder AI inspection uses a step that requires a driver,
 you must download and install a version of the driver that supports the LabVIEW
 version that you are migrating to.

Q: Can I migrate Vision Builder AI
 inspections to the current version of LabVIEW?

No. You must migrate Vision
 Builder AI inspections to a LabVIEW version from the previous year. For example, a
 Vision Builder AI 2013 inspection migrates to LabVIEW 2012, and a Vision Builder AI
 2012 Inspection migrates to LabVIEW 2011.

Q: Why did I lose LabVIEW support
 when I upgraded my inspection to a new version of Vision Builder AI?

If your
 Vision Builder AI inspection uses a Read/Write I/O (NI-DAQmx)
 step, you must download and install a version of NI-DAQmx that
 supports the required version of LabVIEW.

Q: How do I migrate an OPC UA step
 to LabVIEW if the OPC UA server requires a password?

1. Copy the OPC UA certificates folder from the
 Vision Builder AI folder to the destination
 folder.
2. Specify the correct password in the System Config.ini in
 the Configuration Files folder in the destination
 folder.

Q: Why is the generated code broken when migrating to LabVIEW on a Windows
 Industrial Smart Camera?

The generated code is expecting a conditional disable
 symbol to be set, but it is not set by default on Windows.

Parent topic:

Vision Builder AI Tools

Related information:

- Vision Builder for Automated Inspection Readme

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=modifying-inspection-prop.html language=enus -->
## TOPIC 00033: Modifying Inspection Properties

- bundle_id: `vision-builder-automated-inspection`
- source_path: `modifying-inspection-prop.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/modifying-inspection-prop.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Inspection Documentation window to modify the properties of your inspection such as the inspection name, creation date, last modification date, or the description of the inspection. To access the Inspection Properties dialog box, select File Inspection Properties . Use the Inspection Propert

### Modifying Inspection Properties

Use the Inspection Documentation window to modify the properties
 of your inspection such as the inspection name, creation date, last modification date,
 or the description of the inspection.

To access the Inspection Properties dialog box, select File»Inspection Properties.

Use the Inspection Properties dialog box to view a description
 of the inspection or open the Inspection Documentation window to
 modify it.

Parent topic:

Manage Inspections

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=modifying-steps-in-inspections.html language=enus -->
## TOPIC 00034: Modifying a Step in an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `modifying-steps-in-inspections.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/modifying-steps-in-inspections.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Follow one of these instructions to open the property page of a step to modify its controls: Right-click the step, and select Edit. Click the step, and select Edit Edit Step . Click the step, and click the Edit Step () button. Double-click the step.

### Modifying a Step in an Inspection

- Right-click the step, and select Edit .
- Click the step, and select Edit»Edit Step .
- Click the step, and click the Edit Step 
 ([IMAGE alt='image' src='GUID-812C8EDC-1E42-4D38-B720-3B6CC511273A-a5.gif']) button.
- Double-click the step.

Parent topic:

Manage Inspection Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=ni-vision-builder-ai-remote-target-configurat.html language=enus -->
## TOPIC 00035: Vision Builder AI Remote Target Configuration

- bundle_id: `vision-builder-automated-inspection`
- source_path: `ni-vision-builder-ai-remote-target-configurat.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/ni-vision-builder-ai-remote-target-configurat.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Builder AI remote targets are field programmable devices that you add to a subnet and run remotely.You configure a remote target from a host machine on the same subnet, defining settings such as the target name and description, network settings, and software revisions. Click Start All Program

### Vision Builder AI Remote Target
 Configuration

Vision Builder AI remote targets are field programmable devices that you add to a subnet
 and run remotely.

You configure a remote target from a host machine on the same subnet, defining settings such as
 the target name and description, network settings, and software revisions.

1. Click Start»All Programs»National Instruments»Vision Builder AI .
2. On the Vision Builder AI welcome screen, select the remote target that you want to configure
 from the list of targets. Tip If the remote target that you
 want to configure is on a different subnet than the development computer, it may
 not appear in the list of available targets. Click Add
 Target, enter the IP address of the remote target you want to
 configure, and click OK to add the target to the
 table.
3. Vision Builder AI automatically checks the state of the target and displays configuration
 options, if necessary. Tip If you want to configure a remote
 target but are not prompted, right-click the target and select
 Configure.

Parent topic:

Working with Remote Targets

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=opening-an-image.html language=enus -->
## TOPIC 00036: Opening an Image

- bundle_id: `vision-builder-automated-inspection`
- source_path: `opening-an-image.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/opening-an-image.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Open an image file in Vision Builder AI by configuring a Read Image File step and adding it to your inspection.

### Opening an Image

Read Image File

Parent topic:

Manage Images

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=opening-an-inspection.html language=enus -->
## TOPIC 00037: Opening an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `opening-an-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/opening-an-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File Open or click the Open () button on the toolbar. Navigate to the location of the inspection you want to open and select the inspection. Click OK to open the selected inspection.

### Opening an Inspection

1. Select File»Open or click the Open([IMAGE alt='image' src='GUID-4FD2657A-59A8-4290-8F76-9C75BB40F5D5-a5.gif']) button on the
 toolbar.
2. Navigate to the location of the inspection you want to open and select the
 inspection.
3. Click OK to open the selected inspection.

Parent topic:

Manage Inspections

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=overview.html language=enus -->
## TOPIC 00038: Vision Builder Automated Inspection Overview

- bundle_id: `vision-builder-automated-inspection`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/overview.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Vision Builder for Automated Inspection is application software that helps you rapidly develop and deploy machine vision inspection systems. Using menu-driven development tools, you can configure cameras, customize image processing from hundreds of algorithms and inspection steps, interface with aut

### Vision Builder Automated Inspection
 Overview

Vision Builder for Automated Inspection is application software that helps you rapidly
 develop and deploy machine vision inspection systems. Using menu-driven development
 tools, you can configure cameras, customize image processing from hundreds of algorithms
 and inspection steps, interface with automation hardware, and generate inspection
 results.

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=printing-an-image.html language=enus -->
## TOPIC 00039: Printing an Image

- bundle_id: `vision-builder-automated-inspection`
- source_path: `printing-an-image.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/printing-an-image.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File Print Image to launch the Print Image Comment dialog box. Enter a descriptive title for the image. This title appears above the image on the printout. Enter a comment about the image. Enable the Print Results Overlaid on the Image control if you want to add the overlay information to the

### Printing an Image

1. Select File»Print Image to launch the Print Image Comment dialog
 box.
2. Enter a descriptive title for the image. This title appears above the image on
 the printout.
3. Enter a comment about the image.
4. Enable the Print Results Overlaid on the Image control
 if you want to add the overlay information to the printed image.
5. Click OK to print the image.

Parent topic:

Manage Images

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=printing-an-inspection.html language=enus -->
## TOPIC 00040: Printing an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `printing-an-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/printing-an-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File Print Inspection to launch the Print Inspection dialog box. Enable the Print Inspection State Diagram control to print the state diagram from the inspection. Enable the Print State and Transition Details to print details about the states and transitions in the inspection. The inspection

### Printing an Inspection

1. Select File»Print Inspection to launch the Print Inspection dialog
 box.
2. Enable the Print Inspection State Diagram control to
 print the state diagram from the inspection.
3. Enable the Print State and Transition Details to print
 details about the states and transitions in the inspection. The inspection
 details contain information about the steps in each state and transition
 conditions.
4. Click OK to print the inspection.

Parent topic:

Manage Inspections

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=removing-steps-from-inspections.html language=enus -->
## TOPIC 00041: Removing a Step from an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `removing-steps-from-inspections.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/removing-steps-from-inspections.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Follow one of these instructions to remove an inspection step from the State Configuration window: Right-click the step and select Delete. Click the step and select Edit Delete . Click the step and click the Delete () button.

### Removing a Step from an Inspection

State Configuration

- Right-click the step and select Delete .
- Click the step and select Edit»Delete .
- Click the step and click the Delete 
 ([IMAGE alt='image' src='GUID-177512B1-1875-44A0-8D1B-6AC69C05643E-a5.gif']) button.

Parent topic:

Manage Inspection Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=review-execution-target-info.html language=enus -->
## TOPIC 00042: Review Execution Target Information

- bundle_id: `vision-builder-automated-inspection`
- source_path: `review-execution-target-info.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/review-execution-target-info.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: To verify the properties of an execution target and ensure it is the correct remote target you want to connect to, or to check if it is configured properly, click Properties. Review the identification information, network settings, and installed software for the remote target.

### Review Execution Target Information

To verify the properties of an execution target and ensure it is the correct remote
 target you want to connect to, or to check if it is configured properly, click
 Properties. Review the identification information, network
 settings, and installed software for the remote target.

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=saving-a-vi-for-distribution.html language=enus -->
## TOPIC 00043: Saving a VI for Distribution

- bundle_id: `vision-builder-automated-inspection`
- source_path: `saving-a-vi-for-distribution.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/saving-a-vi-for-distribution.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Launch LabVIEW 2018 or later. To use a VI created in a version of LabVIEW later than 2018, save the VI for a previous version. Refer to the LabVIEW Help for more information about saving for a previous version. A VI that requires a licensed development toolkit cannot be saved for a previous version

### Saving a VI for Distribution

1. Launch LabVIEW 2018 or later. Note To use a VI created in a version of LabVIEW later than 2018, save the VI for a
 previous version. Refer to the *LabVIEW Help* for more information
 about saving for a previous version. A VI that requires a licensed development
 toolkit cannot be saved for a previous version of LabVIEW. Note When working with
 real-time targets, add the target to the project in LabVIEW Real-Time Mode and
 complete the following steps within the context of the target listed in the
 project.
2. Open the VI. If the VI is already open, save the VI.
3. Select File»New Project .
4. Add the VI and any dependencies to the project.
5. If a .dll file is listed under Dependencies, but is not located in the
 Windows directory, move the file to the same level as the included VIs. Note The VI will not save
 for distribution correctly if you fail to perform steps 4 and 5.
6. Save the project by selecting File»Save Project .
7. Right-click Build Specifications underneath the VI you added to the
 project and select New»Source Distribution from the shortcut menu to display the Source Distribution
 Properties dialog box.
8. Enter a Build Specification Name and a Destination Directory.
9. Select the Source Files category.
10. In the Project Files list, select any .dll files.
 Add the files to the Always Excluded list. Note System .dll
 files are not included in the compiled LLB.
11. In the Project Files list, select the top level VIs used in the Vision
 Builder AI Run LabVIEW VI steps and add the files to the
 Always Included list. Note Placing all VIs and subVIs used
 by the inspection in a single LabVIEW project allows the VIs to share common
 dependencies, which may reduce the load time and memory requirements for your
 inspection. Creating a single LLB also simplifies the process of copying the
 inspection to another computer.
12. Select the Destinations category.
13. In the Destination type control, select LLB .
14. Select the Source Files Settings category.
15. In the Project Files list, click Dependencies .
16. Enable the Apply prefix to all contained items checkbox and enter a
 prefix.
17. Select the Additional Exclusions category and enable the following
 checkboxes: Note If you are
 using a version of LabVIEW earlier than LabVIEW 2018, disable the Modify
 project library file after removing unused members checkbox.
  - Disconnect type definitions
  - Remove unused polymorphic VI instances
  - Remove unused members of project libraries
  - Modify project library file after removing unused
 members
  - Exclude dependent packed libraries
  - Exclude dependent shared libraries
18. Disable the following checkboxes:
  - Exclude files from VI.lib
  - Exclude files from instr.lib
  - Exclude files from user.lib
19. Select the Preview category. Click Generate
 Preview to review the generated file hierarchy for the source
 distribution. To ensure the preview is accurate, save changes to VIs in memory
 before you create or edit a build specification.
20. Click Build . You can find the resulting source distribution in the
 directory specified in the Destination directory control in
 the Information category of the build specification.

Tip

Parent topic:

Using Vision Builder AI Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=saving-an-image.html language=enus -->
## TOPIC 00044: Saving an Image

- bundle_id: `vision-builder-automated-inspection`
- source_path: `saving-an-image.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/saving-an-image.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File Save Image to launch the Save Image dialog box. Select the file path to which you want to save the image. Click OK to display the Save Image dialog box. Select the file format. JPEG, JPEG2000, and PNG are compressed file formats. If you select one of these formats, use the Image Quality

### Saving an Image

1. Select File»Save Image to launch the Save Image dialog box.
2. Select the file path to which you want to save the image.
3. Click OK to display the Save
 Image dialog box.
4. Select the file format. JPEG, JPEG2000, and PNG are compressed file formats. If
 you select one of these formats, use the Image Quality or
 Compression Ratio controls to specify image
 compression values. 
 Valid values for Image Quality range from
 0 to 1000, where 0 equals
 maximum compression and 1000 equals no compression. Valid
 values for Compression Ratio range from 1
 to 1000, where 1 is no compression and
 1000 would result in a file size about
 1000 times smaller.Note PNG format always performs a
 lossless compression. JPEG2000 performs a lossless compression if the
 Lossless control is enabled.
5. Optional: 
 Enable the Merge Image Overlay control if you want to
 add the overlay information to the saved image. 
 Note This option is
 only available when the image has an overlay. Merging the overlay modifies
 the content of the image and causes Vision Builder AI to save the image as a
 color image.
6. Optional: 
 Enable the Save Color Palette control if you want to
 include the color palette as part of the saved image file. 
 This does not change the pixel values of the image, but the color palette will
 be applied to the image for display purposes.Note This option is only
 available when the image is using a color palette.
7. Click Save to save the image.

Parent topic:

Manage Images

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=saving-an-inspection.html language=enus -->
## TOPIC 00045: Saving an Inspection

- bundle_id: `vision-builder-automated-inspection`
- source_path: `saving-an-inspection.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/saving-an-inspection.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: To save an inspection for the first time or to make a copy of an existing inspection, complete the following steps: Select File Save As or click the Save () button on the toolbar. Navigate to the location where you want to save the file and enter a File name for the inspection file. Click Save to sa

### Saving an Inspection

1. Select File»Save As or click the Save ([IMAGE alt='image' src='GUID-68B98823-2BB3-4FE8-B3AE-AB40CAE5FCEB-a5.gif']) button on the
 toolbar.
2. Navigate to the location where you want to save the file and enter a
 File name for the inspection file.
3. Click Save to save the inspection.

Parent topic:

Manage Inspections

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=saving-inspections-as-templates.html language=enus -->
## TOPIC 00046: Saving an Inspection as a Template

- bundle_id: `vision-builder-automated-inspection`
- source_path: `saving-inspections-as-templates.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/saving-inspections-as-templates.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Select File Inspection Properties to open the Inspection Properties dialog box. Enter a description of the template and click OK. Select File Save as Template . By default, inspection templates are installed to c:\Program Files\National Instruments\<Vision Builder AI version>\Templates.

### Saving an Inspection as a Template

1. Select File»Inspection Properties to open the Inspection Properties dialog
 box.
2. Enter a description of the template and click OK.
3. Select File»Save as Template.

By default, inspection templates are installed to c:\Program Files\National
 Instruments\<Vision Builder AI version>\Templates.

Parent topic:

Manage Templates

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=setting-password-on-remote-target.html language=enus -->
## TOPIC 00047: Setting a Password on a Remote Target

- bundle_id: `vision-builder-automated-inspection`
- source_path: `setting-password-on-remote-target.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/setting-password-on-remote-target.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `task`
- source_description: Protect a remote target by adding a password to it. Open a Web browser and enter http://<Target IP Address> in the Web browser address bar to open the Web Configuration window for your target. Click the Security Configuration () icon on the left. The Security Configuration window appears. Click Logi

### Setting a Password on a Remote Target

Protect a remote target by adding a password to
 it.

1. Open a Web browser and enter http://<Target IP Address>
 in the Web browser address bar to open the Web
 Configuration window for your target.
2. Click the Security Configuration
 ([IMAGE alt='image' src='GUID-C192E034-9ED7-4650-AAEE-6ABA81A54319-a5.gif']) icon on the left. The Security
 Configuration window appears.
3. Click Login at the top right.
4. Enter admin as the User Name, leave the
 Password field blank, and click
 OK.
5. Click Change Password.
6. Enter and re-enter the new password, click OK, then
 click Save. A message appears warning that the password
 is changing and you must login again. Click OK.

Parent topic:

Vision Builder AI Remote Target Configuration

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=simulating-remote-targets.html language=enus -->
## TOPIC 00048: Simulating Remote Targets

- bundle_id: `vision-builder-automated-inspection`
- source_path: `simulating-remote-targets.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/simulating-remote-targets.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Simulating remote targets allows you to develop and edit Vision Builder AI inspections for a remote target using a desktop computer.In addition to the standard Vision Builder AI inspection steps, the following target-specific steps are available in simulation mode: Acquire Image (1394, GigE, or USB)

### Simulating Remote Targets

Simulating remote targets allows you to develop and edit Vision Builder AI inspections
 for a remote target using a desktop computer.

In addition to the standard Vision Builder AI inspection steps, the following target-specific
 steps are available in simulation mode:

- Acquire Image (1394, GigE, or USB)
- Read/Write Camera Attributes
- Acquire Image (Smart Camera)
- Read/Write I/O
- Generate Pulse
- Read/Write I/O (Vision RIO)
- Generate Pulse (Vision RIO)

To use Vision Builder AI with a simulated remote target, complete the following steps:

1. On the Vision Builder AI welcome screen click Add Simulated Target 
 ([IMAGE alt='image' src='GUID-C79E7F92-2F1B-43D9-B20B-1AC0C07F4EE7-a5.gif']) .
2. Select a remote target class to simulate and click OK . If you want to
 create a simulated Smart Camera, click Next and choose a
 camera model to simulate, then click OK .
3. On the Vision Builder AI welcome screen, select the simulated remote target in the list of
 targets.
4. Click New Inspection .
5. Add and configure steps from the Inspection Steps palette to create your
 application.

Parent topic:

Working with Remote Targets

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=switching-between-the-configuration-and-inspe.html language=enus -->
## TOPIC 00049: Switching Between the Configuration and Inspection Interfaces

- bundle_id: `vision-builder-automated-inspection`
- source_path: `switching-between-the-configuration-and-inspe.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/switching-between-the-configuration-and-inspe.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are in the Configuration Interface and want to switch to the Inspection Interface, select File Switch to Inspection Interface .If you have not already saved your current inspection, Vision Builder AI prompts you to save your current inspection before switching to the Inspection Interface.

### Switching Between the Configuration and Inspection Interfaces

If you are in the Configuration Interface and want to switch to
 the Inspection Interface, select File»Switch to Inspection Interface.

If you have not already saved your current inspection, Vision Builder AI prompts you to save your
 current inspection before switching to the Inspection
 Interface.

Parent topic:

Getting Started with the Configuration Interface

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=troubleshoot-ni-hardware-in-vision-builder-ai.html language=enus -->
## TOPIC 00050: Troubleshoot NI Hardware in Vision Builder AI

- bundle_id: `vision-builder-automated-inspection`
- source_path: `troubleshoot-ni-hardware-in-vision-builder-ai.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/troubleshoot-ni-hardware-in-vision-builder-ai.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the type of hardware you are using:

### Troubleshoot NI Hardware in Vision Builder
 AI

Select the type of hardware you are using:

- [Troubleshooting the NI Smart Camera](troubleshooting-the-ni-smart-camera.html)
- [Troubleshooting the NI Compact Vision System or Industrial Controller](troubleshooting-the-ni-compact-vision-system.html)

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=troubleshooting-the-ni-compact-vision-system.html language=enus -->
## TOPIC 00051: Troubleshooting the NI Compact Vision System or Industrial Controller

- bundle_id: `vision-builder-automated-inspection`
- source_path: `troubleshooting-the-ni-compact-vision-system.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/troubleshooting-the-ni-compact-vision-system.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Compact Vision System or Industrial Controller Does Not Appear in the List of Execution Targets On Windows devices, select My Computer as the target to run Vision Builder AI. Refer to Acquire an Image from a Windows Device for instructions on acquiring an image on a Windows device. Verify that t

### Troubleshooting the NI Compact Vision System
 or Industrial Controller

#### The Compact Vision System or
 Industrial Controller Does Not Appear in the List of Execution Targets

Note

My Computer

Acquire an Image from a Windows Device

#### Verify that the Target Device Has
 Power

The PWR/FAULT LED is solid green.

#### Verify that the Device is Communicating with the
 Development Computer

The ACTIVITY/LINK LED on the primary network port
 flashes green when you refresh the device list in Vision Builder AI.

#### Verify the Network Port Used

You must use
 the primary Ethernet connector on the device. The following figure illustrates the
 primary Ethernet port on a Compact Vision System or IC-312x:

[IMAGE alt='image' src='GUID-30DFE2DC-A129-44CD-854C-02994263AB70-a5.gif']

If you are using a different device, refer to the device documentation for the
 location of the primary Ethernet port.

#### Verify the Network Settings

- The target may have been configured on another network and then moved to the
 current network. Reconfigure the target device for the current network. Note Connect a
 monitor and keyboard to the Compact Vision System and press
 Enter to view the current configuration
 settings of the device.
- Another device on the network is using the IP address assigned to the
 target. Note This can happen when you assign the same
 static IP to two devices, you assign a static IP that is in the range of
 the IP address available for DHCP use on your network, or the DHCP
 server assigns the same IP address to another device. Either
 remove or reconfigure the other device, or reconfigure to use a different
 IP address. Put the Compact Vision System into the IP RESET state and
 restart it into the normal state.
- The target is configured to acquire an IP address from a DHCP server, but no
 DHCP server is available. By default, the target automatically attempts to
 connect to the network using DHCP. If the target is unable to initiate a
 DHCP connection, the target connects to the network with a link-local IP
 address ( 169.254.x.x ).

#### Verify that the Ethernet Cable Is Appropriate for
 Your Network

The cable you are using may be inappropriate for the speed of
 your network, causing network communication dropout. While 1,000 Mbps communication
 over short cable lengths can be achieved with the CAT5 cable commonly used for 10
 and 100 Mbps, CAT5e and CAT6 cables are more reliable and recommended for 1,000 Mbps
 links. The target has the ability to perform auto-crossover, allowing the use of
 straight or crossover Ethernet cables, independent of the connection
 configuration.

#### Verify Firewall Settings

If you are having difficulty detecting the system and setting up the target on your
 network, you must configure the firewall to open the TCP/UDP ports used by the
 target and the host machine. Refer to the following table for more information about
 TCP/UDP ports:

| Port | Type | Details |
| --- | --- | --- |
| 3580 | TCP/UDP | Reserved as nati-svrloc (NAT-ServiceLocator). Used by Measurement & Automation Explorer (MAX) to locate remote targets. |
| 7749 | TCP | Used for remote image display (not reserved). |
| 7750 | TCP | Used for NI-IMAQdx remote configuration (not reserved). |
| 3363 | TCP/UDP | Reserved as nati-vi-server (NATI VI Server). Used by Vision Builder for Automated Inspection to configure a remote target. |

Note

#### Related Information

For
 complete instructions on setting up hardware, installing software, configuring an IP
 address, and device specifications, go to [https://www.ni.com/docs](https://www.ni.com/docs) and download the documentation for your Compact
 Vision System or Industrial Controller.

Parent topic:

Troubleshoot NI Hardware in Vision Builder AI

Related concepts:

- Acquire an Image from a Windows Device

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=troubleshooting-the-ni-smart-camera.html language=enus -->
## TOPIC 00052: Troubleshooting the NI Smart Camera

- bundle_id: `vision-builder-automated-inspection`
- source_path: `troubleshooting-the-ni-smart-camera.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/troubleshooting-the-ni-smart-camera.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Smart Camera Does Not Appear in the List of Execution Targets On Windows devices, select My Computer as the target to run Vision Builder AI. Refer to Acquire an Image with the NI Smart Camera for instructions on acquiring an image on a Windows device. Verify that the Smart Camera Has Power The P

### Troubleshooting the NI Smart Camera

#### The Smart Camera Does Not Appear in
 the List of Execution Targets

Note

My Computer

Acquire an Image with the NI Smart Camera

#### Verify that the Smart Camera Has
 Power

The Power and User LEDs are solid green.

#### Verify that the Smart Camera is
 Communicating with the Development Computer

The 100/1G LED flashes green while refreshing the list of devices in Vision Builder
 AI.

#### Verify that the Ethernet Cable Is Appropriate for Your Network

If you have a 1,000 Mbps link, verify that the M12 cable is X-coded and rated for 1,000 Mbps data transfer.

#### Verify the Network Settings

If the smart camera is configured to use a DHCP server and no DHCP server is present,
 the camera may not be visible on the network. If you are using a static IP address,
 another device on the network may be using the same address. This can happen when
 you assign the same static IP to two devices, you assign a static IP that is in the
 range of the IP address available for DHCP use on your network, or the DHCP server
 assigns the same IP address to another device.

Connect the smart camera to
 the same subnet as the development computer and reconfigure the smart camera network
 settings. Refresh the list of targets on the Vision Builder AI Welcome screen, then
 reconfigure the network settings for the device.

#### Verify Firewall Settings

- Windows Firewall may have blocked Vision Builder AI from communicating with the smart camera.
 Refer to Adding a Firewall Exception for more information.
- A firewall may be blocking communication with the smart camera. Refer to Configuring a
 Firewall for Remote Targets for more information.

#### Related Information

For complete instructions on setting up hardware, installing software, configuring an
 IP address, and device specifications, go to [https://www.ni.com/docs](https://www.ni.com/docs) and download the documentation for your Smart
 Camera.

Parent topic:

Troubleshoot NI Hardware in Vision Builder AI

Related concepts:

- Acquire an Image with the NI Smart Camera

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=user-manual-welcome.html language=enus -->
## TOPIC 00053: Vision Builder Automated Inspection User Manual

- bundle_id: `vision-builder-automated-inspection`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/user-manual-welcome.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Vision Builder Automated Inspection User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related I

### Vision Builder Automated Inspection
 User Manual

The Vision Builder Automated Inspection User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=using-flat-field-correction-to-correct-intens.html language=enus -->
## TOPIC 00054: Using Flat Field Correction to Correct Intensity Variation

- bundle_id: `vision-builder-automated-inspection`
- source_path: `using-flat-field-correction-to-correct-intens.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/using-flat-field-correction-to-correct-intens.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Flat field correction uses one bright field image and one optional dark field image to correct uneven background intensity. You can specify or create a single bright field image, or you can create a bright field image iteratively at each inspection.The following figure illustrates use cases for vari

### Using Flat Field Correction to Correct
 Intensity Variation

Flat field correction uses one bright field image and one optional dark field image to correct
 uneven background intensity.

You can specify or create a single bright field image, or you can create a bright field
 image iteratively at each inspection.

The following figure illustrates use cases for various types of flat field correction:

[IMAGE alt='image' src='GUID-F323A1C3-A8E1-4DDE-9ED6-37495D1771AD-a5.gif']

#### Using a Specified Bright Field Image
 for Flat Field Correction

Select Correction with specified bright field image to use one
 image as the bright field for flat field correction. Click [IMAGE alt='image' src='GUID-72791460-CEC0-4B5A-BB8B-2A2239EDD798-a5.gif'] to launch the Flat Field Creation
 Wizard to create a new bright field image.

Use this option if
 you can acquire an image of only the background.

You can use a single state in
 Vision Builder AI to correct new images from the acquisition step or the flat field
 step, as shown in the following diagram:

[IMAGE alt='image' src='GUID-4AC703B2-7B51-4AF2-B869-63DF8FB3BCE2-a5.gif']

#### Using Online Learning for Flat Field
 Correction

Select Online Correction Using Modeling for the inspection to
 relearn the bright field at each iteration. Use the Estimate
 Background controls to configure how the algorithm computes the
 bright field.

This option is recommended when background variations are
 inconsistent across images.

#### Using Online Learning with a Simple
 Flat Field

You can use branching or a different inspection to acquire and/or process a
 background image, then use the newly computed flat field image for future
 corrections. This setup creates a background image to compute the flat field image,
 then saves the flat field image to correct the image from the next
 iteration.

In this model, online learning is not done at each iteration. The
 following diagram shows online learning with a simple flat field:

[IMAGE alt='image' src='GUID-EB8F60D8-42FA-47B6-A366-962605708C52-a5.gif']

#### Using Iterative Online Learning with
 Modeling

You can create an inspection that acquires an image, learns the flat field model from
 that image, then corrects and processes the image in one state, as shown in the
 following diagram:

[IMAGE alt='image' src='GUID-EAA11EB2-B8E7-422B-8615-E7879DECF7F5-a5.gif']

This setup does not save the flat field image.

#### Using Online Learning with
 Modeling

You can create an inspection where the flat field is not learned at each iteration,
 but is applied to the acquired image, as shown in the following diagram:

[IMAGE alt='image' src='GUID-D5BD2DCD-520B-4959-BC0B-255E14E47553-a5.gif']

#### Using Different Inspections to
 Process and Save Flat Field Images

You can create two separate inspections to process flat field images, as shown in the
 following diagram:

[IMAGE alt='image' src='GUID-18EE662A-8CEA-4579-90CD-0AB4A82771F8-a5.gif']

Parent topic:

Using Vision Builder AI Steps

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=variable-manager.html language=enus -->
## TOPIC 00055: Variable Manager

- bundle_id: `vision-builder-automated-inspection`
- source_path: `variable-manager.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/variable-manager.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Variable Manager to create and manage Vision Builder AI inspection variables, system variables, and network variables. The primary difference between the variable types is the scope of the variable: Inspection variables are limited to the inspection for which they are created. System variabl

### Variable Manager

Use the Variable Manager to create and manage Vision Builder AI inspection variables, system
 variables, and network variables.

- Inspection variables are limited to the inspection for which they are
 created.
- System variables are limited to the device on which an inspection is deployed.
 Multiple inspections may access the same system variable as long as the
 inspections are deployed on the same device. Multiple instances on multiple
 devices may access the same system variable as long as the variable is published
 on a network.
- Network variables can be accessed by any device on the network that supports
 LabVIEW variables.

Note

Use the Set Variable step to update the value of any variable except
 built-in system variables. For example, use the Set Variable step
 to set the current image as the value of a system or network image variable.

Parent topic:

Vision Builder AI Tools

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=viewiing-options.html language=enus -->
## TOPIC 00056: Viewing Options

- bundle_id: `vision-builder-automated-inspection`
- source_path: `viewiing-options.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/viewiing-options.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the View menu options or the buttons on the Vision Builder AI toolbar to change the display in the Main window. The following options are available: View Option Toolbar Icon Description Zoom In Increases the magnification of the active image. You can also use the mouse wheel to zoom in or out of

### Viewing Options

Use the View menu options or the buttons on the Vision Builder
 AI toolbar to change the display in the Main window.

The following options are available:

| View Option | Toolbar Icon | Description |
| --- | --- | --- |
| Zoom In |  | Increases the magnification of the active image. You can also use the mouse wheel to zoom in or out of the image. |
| Zoom Out |  | Decreases the magnification of the active image. You can also use the mouse wheel to zoom in or out of the image |
| Zoom 1:1 |  | Displays the active image at its original size with no magnification. |
| Zoom to Fit |  | Scales the active image to fit in the Main window. |
| Toggle Main Window View |  | Switches the Main window view between the active image and the inspection state diagram. |
| View Inspection State Diagram | — | Displays the inspection state diagram in the Main window along with the Setup, Cleanup, and Select Inspection configuration states. |

Parent topic:

Manage Images

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=vision-builder-ai-steps.html language=enus -->
## TOPIC 00057: Using Vision Builder AI Steps

- bundle_id: `vision-builder-automated-inspection`
- source_path: `vision-builder-ai-steps.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/vision-builder-ai-steps.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about managing inspection steps, editing the color palette, flat field correction, and saving VIs.

### Using Vision Builder AI Steps

This section contains information about managing inspection steps, editing the color
 palette, flat field correction, and saving VIs.

- [Manage Inspection Steps](manage-inspection-steps.html)
- [How to Use the Color Palette Editor](how-to-use-the-color-palette-editor.html)
- [Using Flat Field Correction to Correct Intensity Variation](using-flat-field-correction-to-correct-intens.html)
- [Saving a VI for Distribution](saving-a-vi-for-distribution.html)

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=vision-builder-ai-tools.html language=enus -->
## TOPIC 00058: Vision Builder AI Tools

- bundle_id: `vision-builder-automated-inspection`
- source_path: `vision-builder-ai-tools.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/vision-builder-ai-tools.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about managing variables and migrating inspections between Vision Builder AI and LabVIEW.

### Vision Builder AI Tools

This section contains information about managing variables and migrating inspections between
 Vision Builder AI and LabVIEW.

- [Variable Manager](variable-manager.html)
- [Migrating an Inspection to LabVIEW](migrating-an-inspection-to-labview.html)

<!--NI_TOPIC bundle=vision-builder-automated-inspection path=work-with-remote-targets.html language=enus -->
## TOPIC 00059: Working with Remote Targets

- bundle_id: `vision-builder-automated-inspection`
- source_path: `work-with-remote-targets.html`
- source_url: https://docs-be.ni.com/bundle/vision-builder-automated-inspection/raw/resource/enus/work-with-remote-targets.html
- document_id: `vision-builder-automated-inspection`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about handling remote targets and troubleshooting hardware in Vision Builder AI.

### Working with Remote Targets

This section contains information about handling remote targets and troubleshooting hardware in
 Vision Builder AI.

- [Simulating Remote Targets](simulating-remote-targets.html)
- [Vision Builder AI Remote Target Configuration](ni-vision-builder-ai-remote-target-configurat.html)
- [Managing Inspections Between the Host and Remote Target](managing-inspections-between-the-host-and-rem.html)
