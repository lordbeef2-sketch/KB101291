# NI DOCUMENT BUNDLE: flexlogger-plug-in-development-kit

<!--NI_BUNDLE_CHUNK bundle=flexlogger-plug-in-development-kit start=1 end=37 -->
<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=accessing-the-flexlogger-palette-in-labview.html language=enus -->
## TOPIC 00001: Accessing the FlexLogger Palette in LabVIEW

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `accessing-the-flexlogger-palette-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/accessing-the-flexlogger-palette-in-labview.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the FlexLogger palette in LabVIEW to develop and customize plug-ins. The FlexLogger Plug-In Development Kit installer adds the FlexLogger palette to LabVIEW. The palette provides the plug-in and channel methods needed to interact with FlexLogger. In LabVIEW, navigate to View Functions Palette .

### Accessing the FlexLogger Palette in
 LabVIEW

Use the FlexLogger palette in LabVIEW to develop and customize plug-ins.

FlexLogger Plug-In Development Kit

1. In LabVIEW, navigate to View»Functions Palette. 
[IMAGE alt='image' src='GUID-C3436C53-96CD-4FF5-83B8-3E677CAF880B-a5.png']
2. In the Functions window, select the
 FlexLogger palette. 
[IMAGE alt='image' src='GUID-96D7025E-8024-4271-931D-45CC9904E4FC-a5.png']

FlexLogger Plug-In LabVIEW Classes

Parent topic:

FlexLogger Plug-In Development

Related concepts:

- FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=additional-classes.html language=enus -->
## TOPIC 00002: Additional Classes

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `additional-classes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/additional-classes.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following classes belong to PluginSDK.lvlibp and are outside the scope of FlexLogger plug-in development. These classes should not be used in your plug-ins. 9 Additional Classes Not Used in Plug-in Development Class Name Summary Addon Interface.lvclass Defines the communication between plug-ins

### Additional Classes

The following classes belong to PluginSDK.lvlibp and are outside the
 scope of FlexLogger plug-in development. These classes should not be used in your
 plug-ins.

| Class Name | Summary |
| --- | --- |
| Addon Interface.lvclass | Defines the communication between plug-ins and FlexLogger |
| Message Completion Handler.lvclass | Messaging functionality for classes that do not inherit from Plugin.lvclass |
| Parameters.lvclass | Provides the parameter functionality for the Channel and Plug-in classes |

Parent topic:

FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=channel-class.html language=enus -->
## TOPIC 00003: Channel Class

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `channel-class.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/channel-class.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Channel class, Channel.lvclass, allows plug-ins to send data to FlexLogger and read setpoint data from FlexLogger. The Plug-in class uses the Channel class to organize channels and ensure consistency between the plug-in and FlexLogger.

### Channel Class

The Channel class, Channel.lvclass, allows plug-ins to send data to
 FlexLogger and read setpoint data from FlexLogger. The Plug-in class uses the Channel class to
 organize channels and ensure consistency between the plug-in and FlexLogger.

Parent topic:

FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=channel-data-types.html language=enus -->
## TOPIC 00004: Channel Data Types

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `channel-data-types.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/channel-data-types.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Channel class supports analog (Wfm (DBL)), digital (Wfm (Digital)), and string data types for all channels. Analog waveform is the default data type. To specify a data type, connect it to the Create Channel VI. You can also set the data type using Write Data Type VI and connecting it to the Crea

### Channel Data Types

The Channel class supports analog (Wfm (DBL)), digital (Wfm (Digital)), and string data types
 for all channels. Analog waveform is the default data type.

To specify a data type, connect it to the Create Channel VI.

[IMAGE alt='Screenshot of the Create Channel VI with a Wfm (DBL) data type connected.' src='GUID-19FE14FC-8C63-4D0C-8C51-5125CF35D8AE-a5.png']

Write Data Type VI

Create Channel VI

Write Data Type VI

[IMAGE alt='Screenshot of the Write Data Type VI connected to the Create Channel VI.' src='GUID-F4AAC835-3F4D-4425-819C-848B3EDD9168-a5.png']

Note

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=channel-specific-parameters.html language=enus -->
## TOPIC 00005: Channel Specific Parameters

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `channel-specific-parameters.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/channel-specific-parameters.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Channel class supports double-precision floating point numbers, strings, enums, Booleans, and integers as channel-level parameters. Channel-specific parameters can be created by using the Channel class’s Write Parameter VI, as shown in the following example:

### Channel Specific Parameters

Write Parameter VI,

[IMAGE alt='image' src='GUID-B88E783F-F385-46FB-9FD8-5B3BEA65056C-a5.png']

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=commands.html language=enus -->
## TOPIC 00006: Commands

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `commands.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/commands.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug-ins have a special parameter type called Command. When you select this parameter, the plug-in will create a button in FlexLogger. Pressing the button in FlexLogger sends a notification to the plug-in. For example, use a Command parameter to create a Tare button for a scale plug-in. When you pre

### Commands

Plug-ins have a special parameter type called Command. When you select
 this parameter, the plug-in will create a button in FlexLogger. Pressing the button in
 FlexLogger sends a notification to the plug-in. For example, use a Command parameter to create
 a Tare button for a scale plug-in.

[IMAGE alt='image' src='GUID-49A9AC59-FE8D-4058-98C5-8C4DEF7A8BB9-a5.png']

When you press the Tare button in FlexLogger, the plug-in tares the
 scale.

[IMAGE alt='image' src='GUID-FAB1E794-3EAF-46A8-ADB6-5FE7ECF183AD-a5.png']

In order to create a user-defined command in a plug-in, you must override the Handle
 Notification VI. Create an overriding VI by right-clicking the
 .lvclass file in the project and selecting New»VI for Override.

- Notification Type - a string input to match the name given to your
 plug-in command parameter
- Payload - a string input that is empty when the notification comes
 from a command button, except for the built-in commands, Test Start and Test Stop. The
 Test Start and Test Stop commands return the time (in seconds) for the start or stop of a
 test. Use Notification Payload to Timestamp VI to decode the
 payload.

[IMAGE alt='image' src='GUID-66339DC4-A6C3-49E2-9DD5-24088990050F-a5.png']

To create a special case for Test Start or Test Stop notifications, add these notification
 type names to the case structure and use Notification Payload to Timestamp
 VI
 (<vi.lib>\FlexLogger\SDK\PluginSDK.lvlibp\PEFClasses\SDK\Plugin\)
 to convert the payload to a timestamp.

Note that Handle Notification VI runs in a separate loop. If you want to
 share data with other VIs in the Plug-in class, use a Data Value Reference instead of directly
 changing the private class member variables.

Parent topic:

Plug-in Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=create-channel-vi.html language=enus -->
## TOPIC 00007: Create Channel VI

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `create-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/create-channel-vi.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Create Channel VI allows you to create three types of channels, Produced by Plug-in, Produced by Plugin (Resampler timing), and Setpoint consumed by Plugin. Creating channels involves the following information: 8 Plug-in Channel Components Name LabVIEW Data Type Description Unique Channel Identi

### Create Channel VI

Create Channel VI

Produced by Plug-in

Produced by Plugin (Resampler timing)

Setpoint consumed
 by Plugin

| Name | LabVIEW Data Type | Description |
| --- | --- | --- |
| Unique Channel Identifier | string | Channel identifier that is unique in the plug-in context. Displayed in the far-left Channel Specification column (for example, ai0 for a DAQ channel). Strings with five or fewer characters display best in FlexLogger. |
| Default Channel Name | string | Channel name in FlexLogger. |
| Display Group | string | Name used in Channel Specification header and channel selector. |
| Unit | string | Channel units (for example, Hz). |
| Can Delete? | Boolean | Allow users to disable this channel. False by default. When setting Can Disable? to True, plug-in developers should monitor which channels are disabled by using Get Valid Channels. When a channel is disabled, do not write data back to FlexLogger for the disabled channel. |
| Default Value | double | Setpoint consumed by Plugin channels allow plug-in developers to set the default value that appears in FlexLogger when the plug-in is added. |
| dt(sec) | double | If Produced by Plugin channels use the 1D Wfm (DBL) or 1D Wfm (Digital) option provided by Write VI, this parameter tells the FlexLogger application what dt to expect. |

FlexLogger allows users to change a channel’s Default Channel Name
 from both the channel configuration dialog and directly in the Channel Specification table.
 Additionally, FlexLogger requires all channels in the Channel Specification to have unique
 names—and will automatically change a plug-in channel name if that rule is violated (for
 example, myChannel becomes myChannel_1). Regardless of the
 change toDefault Channel Name, the Unique Channel
 Identifier parameter remains unchanged.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=creating-a-plug-in-from-a-template.html language=enus -->
## TOPIC 00008: Creating a FlexLogger Plug-In from a Template

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `creating-a-plug-in-from-a-template.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/creating-a-plug-in-from-a-template.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the FlexLogger Plug-in Wizard and plug-in templates to create plug-ins that you can use in FlexLogger. Launch LabVIEW. In LabVIEW, select FileCreate Project. From the Create Project window, select FlexLogger IO Plug-in and click Finish. In the Create FlexLogger IO Plug-in window, update the IO P

### Creating a FlexLogger Plug-In from a
 Template

Use the FlexLogger Plug-in Wizard and
 plug-in templates to create plug-ins that you can use in FlexLogger.

1. Launch LabVIEW.
2. In LabVIEW, select File»Create Project.
3. From the Create Project window, select FlexLogger IO
 Plug-in and click Finish.
4. In the Create FlexLogger IO Plug-in window, update the
 IO Plug-in Name and select a Plug-in
 Template based on your goal. 
 Table 1.FlexLogger Plug-In
 TemplatesGoal
 Plug-In Template
 Data FlowCreate a plug-in that sends a setpoint value you enter in FlexLogger to a
 plug-in channel.Control a third-party instrument with FlexLogger. For more
 information, refer to *Read Setpoint Channels from
 FlexLogger*.
 Consume setpoint data
 User input → plug-in
 Create a plug-in that consumes one or more waveforms from FlexLogger
 channels, performs a custom calculation, and produces a waveform of resulting
 data that can be logged in FlexLogger.
 Perform calculation
 FlexLogger → plug-in
 and
 plug-in → FlexLogger
 Create a plug-in that generates waveform data and sends it to
 FlexLogger.
 Produce data for FlexLogger
 plug-in → FlexLogger
5. Optional: 
 Update the Description and Destination Directory
 (Source) for the plug-in. By default, the wizard saves new plug-ins in the
 My Documents\LabVIEW Projects\FlexLogger IO Plug-ins\
 directory.
6. Click Create. 
 The FlexLogger Plug-In Wizard creates a LabVIEW project with necessary
 dependencies, a new LabVIEW class, an XML file, and a packed library build
 specification.
7. Optional: 
 Customize your plug-in using the methods described in the *Plug-in
 Development* section.
8. To build your plug-in, select the Packed Library build specification and click
 Build Selected. 
[IMAGE alt='image' src='GUID-27F59AB3-3865-46C2-BA7B-18F2A28831C5-a5.png'] 
 FlexLogger Plug-in Wizard builds the packed library file and XML file for the
 plug-in and saves them in the default FlexLogger plug-in directory,
 %public%\Documents\National
 Instruments\FlexLogger\Plugins\IOPlugins.

After creating a plug-in, use it in your
 FlexLogger project.

Related concepts:

- Read Setpoint Channels from FlexLogger
- FlexLogger Plug-In Development

Related tasks:

- Using Plug-Ins in FlexLogger

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=debugging-plug-in-loading-errors.html language=enus -->
## TOPIC 00009: Debugging Plug-In Loading Errors

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `debugging-plug-in-loading-errors.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/debugging-plug-in-loading-errors.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If FlexLogger fails to parse a plug-in XML file, the plug-in is not available for you to add in the Channel Specification. If a parsing failure occurs, FlexLogger creates a Error.txt file in the plug-in folder. The file contains details about the problem.

### Debugging Plug-In Loading Errors

If FlexLogger fails to parse a plug-in XML file, the plug-in is not available for you to add
 in the Channel Specification. If a parsing failure occurs, FlexLogger creates a
 Error.txt file in the plug-in folder. The file contains details about
 the problem.

Parent topic:

FlexLogger Plug-In Debugging

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=dynamic-channel-number-with-individual-settings.html language=enus -->
## TOPIC 00010: Alternative Configuration - Dynamic Channel Number with Individual Settings

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `dynamic-channel-number-with-individual-settings.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/dynamic-channel-number-with-individual-settings.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure the settings in FlexLogger to support a dynamic number of channels with separate settings. In this configuration, each channel has its own offset and multiplier setting as well as user-selected waveforms that each channel applies unique scaling parameters to. Reconfigure the code f

### Alternative Configuration - Dynamic Channel
 Number with Individual Settings

Note

Disable

[IMAGE alt='image' src='GUID-237B6F97-46F9-45EC-85B5-05F7BBABBCE6-a5.svg']

1. Update the class private data control to track the number of channels. 
[IMAGE alt='image' src='GUID-9B575F66-8ADB-4856-87B7-41ABFDD30EC4-a5.png']
2. Modify Initialize VI to create the Number of Channels parameter for
 the plug-in and initialize the private data. 
[IMAGE alt='image' src='GUID-2FB97819-06AE-4971-80EF-149227D89563-a5.png']
3. In the Configure Session VI, read the current number of channels
 configured by the user and compare with the previous value stored in the private data. Add
 any new channels that need to be configured and remove any channels that are no longer
 needed. 
[IMAGE alt='image' src='GUID-0949A54F-AD37-42EE-A625-A07A0958EC87-a5.png'] 
 The Get Channel With Name VI
 (<vi.lib>\FlexLogger\SDK\PluginSDK.lvlibp\Plugin\) determines
 if the channel has already been created. Since you allow the user to disable channels,
 disabled channels are not returned by the Get Valid Channels VI. You
 determine which channels to add and remove to prevent any existing channels from being
 removed or overwritten. This ensures all the configured settings for any existing channels
 remain unchanged, including the disabled setting. Get Valid Channels VI
 is called whenever the user changes the Number of Channels parameter from the
 Plug-in Configuration dialog in FlexLogger.
4. Modify the Process VI to go through all enabled channels. Use
 Get Valid Producer Channels VI
 (<vi.lib>\FlexLogger\SDK\PluginSDK.lvlibp\Plugin\) to obtain
 only enabled channel producers for this plug-in. For each channel, get the waveforms,
 multiplier, and offset associated with the channel. 
[IMAGE alt='image' src='GUID-0C5B2104-65F5-4A68-B3C9-7412F6460C53-a5.png'] 
 Below is the resulting plug-in Configuration, Channel Configuration and channel table
 in FlexLogger:
 
[IMAGE alt='image' src='GUID-52EEA5CC-C227-4E3A-AEEE-EE5DE86B81A4-a5.png'] 

 
[IMAGE alt='image' src='GUID-B13D7448-1100-4145-B53A-971DAB7968C5-a5.png'] 

 
[IMAGE alt='image' src='GUID-27492ED2-897A-438D-B604-8432E4F28665-a5.png']

Parent topic:

Retrieve Data from Individual Channels

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=dynamic-channels.html language=enus -->
## TOPIC 00011: Dynamic Channels

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `dynamic-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/dynamic-channels.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To help developers work with dynamic channels—such as when names change or channels are disabled—plug-ins maintain an array of valid channels. Wiring a property node to a plug-in class wire provides direct access to the ValidProducerChannels, and ValidConsumerChannels arrays: Knowing what channels a

### Dynamic Channels

ValidProducerChannels

ValidConsumerChannels

[IMAGE alt='image' src='GUID-80BA1D62-7962-4004-8142-B7E99DEFE73C-a5.png']

Knowing what channels are valid allows developers to configure their plug-ins correctly and
 produce the right data for the available channels.

When channels assigned to a plug-in need to be changed, developers can use Replace
 Producer Channels VI and Replace Channel Group VI to replace
 multiple channels at once rather than individually. Replace Producer Channels VI replaces all
 existing producer channels with a specified list of channels, which can be useful in situation
 where the user configuration changes in a way that requires a completely new set of producer
 channels. Replace Channel Group VI replaces all channels in a particular group with a
 specified list of channels, which can be useful in situations where only a subset of the
 channels need to be replaced.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=extended-support-changes.html language=enus -->
## TOPIC 00012: Updates and Changes for FlexLogger Plug-In Development Kit Extended Support Versions

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/extended-support-changes.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in FlexLogger Plug-In Development Kit versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information

### Updates and Changes for FlexLogger Plug-In Development Kit Extended Support Versions

Browse updates and changes made in FlexLogger Plug-In Development Kit versions
 on extended support.

Note

Release Notes

#### FlexLogger Plug-In Development Kit
 1.6

- Send strings from third party devices to FlexLogger. Use the Produce Data for FlexLogger
 plug-in template and configure the Write Data VI to write string channel data.

Related concepts:

- Writing Channel Data from a Plug-In to FlexLogger

#### FlexLogger Plug-In Development Kit
 1.5

- Added support for LabVIEW 2022

#### FlexLogger Plug-In Development Kit
 1.4

- Added support for LabVIEW 2021

#### FlexLogger Plug-In Development Kit
 1.3

- Added support for LabVIEW 2020

#### FlexLogger Plug-In Development Kit
 1.2

- Support for digital input plug-in channels

#### FlexLogger Plug-In Development Kit
 1.1

- New Perform calculation plug-in template type
  - Send FlexLogger analog input channels
  - Publish calculation results back to FlexLogger with the same timing information as
 the mapped channels
- Custom plug-in commands offer users a new way to interact with plug-ins

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=flexlogger-plug-in-debugging.html language=enus -->
## TOPIC 00013: FlexLogger Plug-In Debugging

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `flexlogger-plug-in-debugging.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/flexlogger-plug-in-debugging.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Troubleshoot plug-in problems with the debugging resources available in LabVIEW and FlexLogger. Refer to the following debugging resources that align with your troubleshooting scenario. 10 Plug-In Debugging Resources Scenario Resource Why is my plug-in is not available to load in FlexLogger? Review

### FlexLogger Plug-In Debugging

Troubleshoot plug-in problems with the debugging resources available in LabVIEW and
 FlexLogger.

Refer to the following debugging resources that align with your troubleshooting scenario.

| Scenario | Resource |
| --- | --- |
| Why is my plug-in is not available to load in FlexLogger? | Review the error log created by FlexLogger. Refer to Debugging Plug-In Loading Errors for more information. |
| How do I view errors published by VIs used in my plug-in in FlexLogger? | Configure your VIs in LabVIEW, and view errors and warnings in FlexLogger. Refer to Viewing Errors in FlexLogger for more information. |
| How do I interactively test my plug-in before I use it in FlexLogger? | Use the Plug-in Environment Simulator in LabVIEW. Refer to Interactively Testing Plug-Ins for more information. |

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=flexlogger-plug-in-development-kit.html language=enus -->
## TOPIC 00014: FlexLogger Plug-In Development Kit Overview

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `flexlogger-plug-in-development-kit.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/flexlogger-plug-in-development-kit.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexLogger Plug-In Development Kit is a FlexLogger add-on that is designed for test engineers. Use the FlexLogger Plug-In Development Kit to create LabVIEW plug-ins that perform custom in-line calculations. The plug-ins can acquire data from NI hardware that is supported by FlexLogger and third-

### FlexLogger Plug-In Development Kit
 Overview

The FlexLogger Plug-In Development Kit is a FlexLogger add-on that is designed
 for test engineers. Use the FlexLogger Plug-In Development Kit to create LabVIEW
 plug-ins that perform custom in-line calculations. The plug-ins can acquire data from NI
 hardware that is supported by FlexLogger and third-party hardware.

#### Key Features

- Easy integration with FlexLogger
- Plug-in templates to:
  - communicate with NI hardware supported by FlexLogger and third-party
 hardware
  - perform custom in-line calculations
  - generate waveform data

#### Components of the FlexLogger Plug-In Development Kit

The FlexLogger Plug-In Development Kit is an optional add-on designed for use in a
 FlexLogger test system.

- FlexLogger
- LabVIEW
- LabVIEW Application Builder Module

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=flexlogger-plug-in-development.html language=enus -->
## TOPIC 00015: FlexLogger Plug-In Development

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `flexlogger-plug-in-development.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/flexlogger-plug-in-development.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the components of a plug-in so you can customize a plug-in you created from a template or develop a new plug-in. When you create a plug-in named MyFirstPlugin, for example, using the FlexLogger Plug-In Wizard in LabVIEW, the wizard creates a project with the hierarchy shown below. The VI

### FlexLogger Plug-In Development

Learn about the components of a plug-in so you can customize a plug-in you created from
 a template or develop a new plug-in.

When you create a plug-in named MyFirstPlugin, for example, using the
 FlexLogger Plug-In Wizard in LabVIEW, the wizard creates a project with the hierarchy shown
 below.

[IMAGE alt='image' src='GUID-18AC8D53-0D56-4AE3-BBDF-335F250B77FD-a5.png']

The VIs within MyFirstPlugin.lvclass are the starting point for code
 changes. These VIs perform different roles, such as defining parameters and exchanging data
 with FlexLogger. For details about how these VIs function, refer to *Processing Element
 Class*. State information—like a hardware reference—passes between the VIs using the
 private class data defined in MyFirstPlugin.ctl.

[IMAGE alt='image' src='GUID-8664539D-F2B1-40DE-8854-1542EC193F00-a5.png']

If you plan to develop a plug-in, first test your hardware and drivers using a LabVIEW VI
 that communicates with third-party instruments. NI recommends that you start with the
 LabVIEW-only VI provided in some of the examples, including Mouse Input. This LabVIEW-only VI
 demonstrates how to map functionality from a standalone VI to a FlexLogger plug-in class. For
 more information, refer to *FlexLogger Plug-In Development Kit Examples*.

FlexLogger Plug-In Development Kit

| Question | Where to Go |
| --- | --- |
| How many channels do I need? | Refer to Channel Class for details on how plug-in channels communicate with FlexLogger. |
| How many parameters will I need to edit while logging data? | Only setpoint channels can be edited while data logging is in progress. Refer to Read Setpoint Channels from FlexLogger for details on how to use setpoint channels. |
| How many plug-in parameters do I need? | Plug-in parameter values affect the entire plug-in—for example, the name of a hardware resource. Refer to Plug-in Class for more information. |
| How many channel-specific parameters do I need? | Channel-specific parameter values are unique to every channel and are defined when creating new plug-in channels. Refer to Channel Class for more information. |
| What data do I need to pass between plug-in VIs? | You must pass references to any resources you initialize or allocate. For example, if an instrument session is initialized in Configure Session VI, it needs to be passed to Process VI for use and then to Cleanup Session VI for disposal. Important plug-in information can be stored in the private class data of the plug-in (for example, MyFirstPlugin.ctl). |
| How do I know my plug-in works? | Use one of the following approaches to evaluate the functionality of your plug-in by executing the logic and investigating the effect of code changes. Load the plug-in into FlexLogger. Refer to Using Plug-Ins in FlexLogger for more information. Run the plug-in with the Plug-in Environment Simulator. Refer to Interactively Testing Plug-Ins for more information. |

Related concepts:

- Processing Element Class
- Channel Class
- Read Setpoint Channels from FlexLogger
- Plug-in Class
- Interactively Testing Plug-Ins

Related tasks:

- Using Plug-Ins in FlexLogger

Related reference:

- FlexLogger Plug-In Development Kit Examples

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=flexlogger-plug-in-examples.html language=enus -->
## TOPIC 00016: FlexLogger Plug-In Development Kit Examples

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `flexlogger-plug-in-examples.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/flexlogger-plug-in-examples.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about the various examples included in the FlexLogger Plug-In Development Kit. The examples are located in the %ProgramFiles%\National Instruments\LabVIEW <version>\examples\FlexLogger\IO Plugins directory. 2 FlexLogger Plug-In Development Kit Examples Example Type Description Cycle Counter Pe

### FlexLogger Plug-In Development Kit
 Examples

Learn about the various examples included in the FlexLogger Plug-In Development Kit. The examples are located in the %ProgramFiles%\National Instruments\LabVIEW
 <version>\examples\FlexLogger\IO Plugins
 directory.

| Example | Type | Description |
| --- | --- | --- |
| Cycle Counter | Perform calculation | Counts the number of times a specified channel rises above a threshold. |
| Digital Port Calculator | Perform calculation | Combines eight individual digital channels into a single analog value representing the port value. |
| IVI DC Power Supply | Consume setpoint data | Uses the IVI DC Power class driver to control a power supply instrument.To load this IVI example, first install the IVI Compliance Package from NI Package Manager and an IVI DC Power-compliant instrument driver to control the power supply. |
| IVI Meter – DC Voltage | Produce data for FlexLogger | Reads DC voltage values from an IVI DMM class driver-compliant instrument.To load this IVI example, first install the IVI Compliance Package from NI Package Manger and an IVI compliant instrument driver to read voltage values from an instrument. |
| Mouse Input | Produce data for FlexLogger | Reads data from the mouse connected to the computer. |
| Rosette | Perform calculation | Calculates a rosette measurement from multiple strain input channels. |

#### LabVIEW-only VIs

Some examples include a LabVIEW-only VI that demonstrates how to map functionality from a
 standalone VI to a FlexLogger plug-in class. For example, the LabVIEW project for the Mouse
 Input example contains Mouse Input - LabVIEW Only Example VI that describes
 how different parts of the block diagram correspond to the VIs in Mouse
 Input.lvclass.

[IMAGE alt='image' src='GUID-DAC61428-A827-456B-9DD6-4A5BDC84CAA2-a5.png']

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=flexlogger-plug-in-labview-classes.html language=enus -->
## TOPIC 00017: FlexLogger Plug-In LabVIEW Classes

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `flexlogger-plug-in-labview-classes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/flexlogger-plug-in-labview-classes.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the FlexLogger Plug-In Development Kit, PluginSDK.lvlibp contains the classes and VIs to use for plug-in development. The most common classes for plug-in development are the Plug-in and Channel classes. If you are unfamiliar with LabVIEW object-oriented programming, refer to LabVIEW Object-Orient

### FlexLogger Plug-In LabVIEW Classes

In the FlexLogger Plug-In Development Kit, PluginSDK.lvlibp
 contains the classes and VIs to use for plug-in development. The most common classes for plug-in
 development are the Plug-in and Channel classes.

Tip

LabVIEW Object-Oriented Programming

LabVIEW
 User Manual

Parent topic:

FlexLogger Plug-In Development

Related information:

- LabVIEW Object-Oriented Programming

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=installing-the-flexlogger-plug-in-development-kit.html language=enus -->
## TOPIC 00018: Installing the FlexLogger Plug-In Development Kit

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `installing-the-flexlogger-plug-in-development-kit.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/installing-the-flexlogger-plug-in-development-kit.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the FlexLogger Plug-In Development Kit using NI Package Manager. Before you begin, refer to FlexLogger Plug-In Development Kit Compatibility with FlexLogger and LabVIEW to verify software compatibility. Use NI Package Manager to download and install your NI software. For more information, re

### Installing the FlexLogger Plug-In Development Kit

Install the FlexLogger Plug-In Development Kit using NI Package
 Manager.

FlexLogger Plug-In Development
 Kit Compatibility with FlexLogger and LabVIEW

Installing, Updating, Repairing, and Removing
 NI Software

1. Install LabVIEW.
2. Install FlexLogger.
3. Install the FlexLogger Plug-In Development Kit.

Related information:

- Installing, Updating, Repairing, and Removing NI Software with Package
 Manager
- FlexLogger Plug-In Development Kit Compatibility with FlexLogger and
 LabVIEW

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=interactive-debugging-session-example.html language=enus -->
## TOPIC 00019: Interactive Debugging Session Example

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `interactive-debugging-session-example.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/interactive-debugging-session-example.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: The following scenario illustrates how the Simulator could be used to investigate an issue with a plug-in under development. After loading and configuring the DMM plug-in, the plug-in channel does not produce any data. The Error and Warning pane in FlexLogger, displays an error message that referenc

### Interactive Debugging Session Example

The following scenario illustrates how
 the Simulator could be used to investigate an issue with a plug-in under
 development.

1. After loading and configuring the DMM plug-in, the plug-in channel does not produce any
 data. The Error and Warning pane in FlexLogger, displays an error
 message that references a problem in the Configure Session VI.
2. To investigate further, open the LabVIEW project for the DMM plug-in
 %ProgramFiles%\National Instruments\LabVIEW
 <version>\examples\FlexLogger\IO Plugins\IVI Meter – DC
 Voltage\IVI Meter – DC Voltage.lvproj.
3. Open and run Plug-in Environment Simulator VI and then select the
 LabVIEW class of the DMM plug-in (IVI Meter – DC Voltage.lvclass).
4. After updating the plug-in parameter that defines the IVI Logical
 Name to test channel, the simulator stops running and the Runtime
 Information error terminal displays and error: 
[IMAGE alt='image' src='GUID-4459E6F0-0CC4-4141-A24C-1AB02A88A2C7-a5.png']
5. To investigate further, navigate to the plug-in LabVIEW project and open
 Configure Session VI. 
[IMAGE alt='image' src='GUID-4368AF08-5DCA-4970-81FD-30A852B5CFEE-a5.png']
6. With Configure Session VI open, add a breakpoint to see what part of
 the logic is generating the error: 
[IMAGE alt='image' src='GUID-601B54D1-1732-4EB2-870E-6E0D193EC1B5-a5.png']
7. With the breakpoint in place, run the simulator again and load the DMM plug-in. That
 action will hit the newly placed breakpoint. Using LabVIEW’s debugging tools, step through
 the block diagram to see exactly which VI is having problems: 
[IMAGE alt='image' src='GUID-A1CB1D77-67CA-4471-9ABE-2AC2678EACF6-a5.png']
8. After this debugging session, you will see that the plug-in has been using the wrong
 IVI Logical Name parameter, resulting in an error from the IVI
 driver VIs. The plug-in runs as expected when using the correct name.

Parent topic:

Interactively Testing Plug-Ins

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=interactively-testing-plug-ins.html language=enus -->
## TOPIC 00020: Interactively Testing Plug-Ins

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `interactively-testing-plug-ins.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/interactively-testing-plug-ins.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When plug-ins load and run in FlexLogger, the application’s compiled data engine and the compiled plug-ins prevent interactive debugging with LabVIEW. The Plug-in Environment Simulator provides a simplified, test-specific environment that allows developers to run and debug plug-ins from the source G

### Interactively Testing Plug-Ins

When plug-ins load and run in FlexLogger, the application’s compiled data engine and the
 compiled plug-ins prevent interactive debugging with LabVIEW. The Plug-in
 Environment Simulator provides a simplified, test-specific environment that
 allows developers to run and debug plug-ins from the source G code.

The Plug-in Environment Simulator installs to %ProgramFiles%\National
 Instruments\LabVIEW <version>\resource\FlexLogger\SDK\Plugin
 Environment Simulator.

Note

To enable interactive debugging of plug-in source code, the Simulator is provided as a VI as
 shown in the following figure.

Figure 2.

[IMAGE alt='image' src='GUID-853D95F7-71F5-4D52-B03A-4F251AF70484-a5.png']

To debug a plug-in, open and run the Plugin Environment Simulator VI. When
 the simulator starts running, it prompts you for the plug-in class to debug. The following
 figure displays the simulator running an unmodified Produce Data for FlexLogger plug-in.

Figure 3.

[IMAGE alt='image' src='GUID-17A1F516-C288-4F8F-AA93-A145DF1C7AF7-a5.png']

The Configure Plugin Parameters button allows you to update plug-in
 parameters.

Figure 4.

[IMAGE alt='image' src='GUID-D17D3049-025C-4D0F-8AB4-980CE4031FA3-a5.png']

Similarly, the Configure Channel Parameters allows developers to
 update channel parameters.

Figure 5.

[IMAGE alt='image' src='GUID-70FD020D-EF33-49C3-A909-8BF29EA751F0-a5.png']

Plug-ins following the consume setpoint data template do not write any data to FlexLogger, so
 the Channel Data chart shows the current setpoint values. The
 Update Setpoint Channels button provides the input information needed
 to write the correct values to an external system. The following figure shows setting the
 setpoint for an unmodified setpoint consumer plug-in example.

Figure 6.

[IMAGE alt='image' src='GUID-749A121F-48C7-46F9-AD12-9D5BA4FF8ECF-a5.png']

When using waveform channel inputs with the simulator, it is first necessary to pick
 channel(s) that are mapped to the parameters. This mimics the behavior when interacting with
 the application. In the simulator, any designated name receives a constant value waveform.
 Configure mapped channels through the Configure Device Parameters
 dialog as shown in the following figures.

Figure 7.

[IMAGE alt='image' src='GUID-35900A6A-0076-45FA-AB7A-B83278C7BA0E-a5.png']

Figure 8.

[IMAGE alt='image' src='GUID-C2AA44EC-BBF1-40AF-86C9-09E0FBB11B9C-a5.png']

You can change the constant value using the Change Setpoint
 option.

Figure 9.

[IMAGE alt='image' src='GUID-78462864-2303-4025-AF1E-15C0D6A31017-a5.png']

Parent topic:

FlexLogger Plug-In Debugging

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=loading-plug-ins-from-custom-locations.html language=enus -->
## TOPIC 00021: Loading FlexLogger Plug-ins from Custom Locations

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `loading-plug-ins-from-custom-locations.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/loading-plug-ins-from-custom-locations.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure FlexLogger to load plug-ins from locations outside of the default directory. By default, FlexLogger loads plug-ins from %public%\Documents\National Instruments\FlexLogger\Plugins\IOPlugins. Complete the following steps to load plug-ins from additional, custom locations. Using a text editor

### Loading FlexLogger Plug-ins from Custom
 Locations

Configure FlexLogger to load plug-ins from locations outside of the default
 directory.

%public%\Documents\National
 Instruments\FlexLogger\Plugins\IOPlugins

1. Using a text editor, create a file that specifies additional plug-in locations using
 the following JSON format. 
 {"AdditionalPluginPaths":["C:\\Users\\<username>\\Documents\\Flex
 LoggerProjects\\","<another absolute path>"]}
2. Save the file in the root directory of %public%\Documents\National
 Instruments\FlexLogger\Plugins\IOPlugins. FlexLogger does not have specific
 requirements for the file name.
3. Change the file extension from .txt to
 .config.
4. Re-launch FlexLogger.

Add channels

»

Plug-in

Channel Specification

Parent topic:

FlexLogger Plug-In File Structure

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=new-features-and-changes.html language=enus -->
## TOPIC 00022: FlexLogger Plug-In Development Kit New Features and Changes

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/new-features-and-changes.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of FlexLogger Plug-In Development Kit. Discover what is new in the latest releases of FlexLogger Plug-In Development Kit.If you cannot find new features and changes for your version, it might not include use

### FlexLogger Plug-In Development Kit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of FlexLogger Plug-In Development Kit.

FlexLogger Plug-In Development Kit

Note

Release Notes

#### FlexLogger Plug-In Development Kit 2025
 Q3

- Find detailed API reference documentation for the FlexLogger Plug-In Development Kit
 in-product or online at ni.com/docs . Refer to the FlexLogger Plug-In
 Development Kit API Reference for more information.

Related information:

- FlexLogger Plug-In Development Kit API Reference

#### FlexLogger Plug-In Development Kit 2025
 Q2

- Added support for LabVIEW 2025

#### FlexLogger Plug-In Development Kit 2024
 Q3

- Added support for LabVIEW 2024

#### FlexLogger Plug-In Development Kit
 1.7

- Added support for LabVIEW 2023 Q1

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=plug-in-and-channel-parameters.html language=enus -->
## TOPIC 00023: Plug-In and Channel Parameters

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `plug-in-and-channel-parameters.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/plug-in-and-channel-parameters.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the plug-in parameters and the channel parameters of a plug-in to support custom calculations and data acquisition from third-party hardware devices. Plug-in parameters, such as Device Name, apply to the whole plug-in. Channel parameters apply to a specific plug-in channel. The following f

### Plug-In and Channel Parameters

Configure the plug-in parameters and the channel parameters of a plug-in to support
 custom calculations and data acquisition from third-party hardware devices.

Plug-in parameters

Device Name

Channel parameters

[IMAGE alt='image' src='GUID-D2195898-5879-4DE5-89A7-C25758A90E3D-a5.svg']

1. FlexLogger dialog box for configuring channel parameters.
2. LabVIEW VIs for customizing channel parameters.
3. FlexLogger dialog box for configuring plug-in parameters.
4. LabVIEW VIs for customizing plug-in parameters.

Parent topic:

Using Plug-Ins in FlexLogger

Related tasks:

- Accessing the FlexLogger Palette in LabVIEW

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=plug-in-class.html language=enus -->
## TOPIC 00024: Plug-in Class

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `plug-in-class.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/plug-in-class.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Plug-in class, Plugin.lvclass, is the parent class for plug-ins created with the FlexLogger Plug-in Development Kit. It provides the state management functionality for the plug-in by inheriting from Processing Element.lvclass. The Plug-in class also provides methods to define and interact with p

### Plug-in Class

The Plug-in class, Plugin.lvclass, is the parent class for plug-ins
 created with the FlexLogger Plug-in Development Kit. It provides the state management
 functionality for the plug-in by inheriting from Processing
 Element.lvclass. The Plug-in class also provides methods to define and interact
 with plug-in channels and parameters. After initializing the channels, the Plug-in class
 maintains channel information that correctly reflects the state of the plug-in channels in
 FlexLogger.

Write Parameter VI

[IMAGE alt='image' src='GUID-7DEFB280-FD07-4264-B8B6-851453A97C70-a5.png']

Note

Do not call Add Channels multiple times from the same plug-in method
 as it causes parameter settings to not save correctly.

Parent topic:

FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=plug-in-file-structure.html language=enus -->
## TOPIC 00025: FlexLogger Plug-In File Structure

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `plug-in-file-structure.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/plug-in-file-structure.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn where FlexLogger looks for plug-ins so you can load the plug-ins that you created. The FlexLogger Plug-In Wizard saves the packed library file and the XML file for the plug-in that you built. You can find the files in the default FlexLogger plug-in directory, %public%\Documents\National Instru

### FlexLogger Plug-In File Structure

Learn where FlexLogger looks for plug-ins so you can load the plug-ins that you
 created.

The FlexLogger Plug-In Wizard saves the packed library file and the XML file for the plug-in
 that you built. You can find the files in the default FlexLogger plug-in directory,
 %public%\Documents\National Instruments\FlexLogger\Plugins\IOPlugins.
 FlexLogger loads plug-ins from the default directory.

You can configure FlexLogger to load plug-ins from custom locations. Refer to *Loading
 FlexLogger Plug-ins from Custom Locations* for more information.

MyFirstPlugin

| Folder | %public%\\Documents\\National Instruments\\FlexLogger\\Plugins\\IOPlugins\\MyFirstPlugin |
| --- | --- |
| Packed library file | %public%\\Documents\\National Instruments\\FlexLogger\\Plugins\\IOPlugins\\MyFirstPlugin\\MyFirstPlugin.lvlibp |
| XML file | %public%\\Documents\\National Instruments\\FlexLogger\\Plugins\\IOPlugins\\MyFirstPlugin\\MyFirstPlugin.xmlFlexLogger uses the XML file to register and to load the plug-in for use at run-time. The XML file contains the plug-in name, description, and version. If you update the plug-in or change the plug-in name, you must manually update the XML file. |

Note

- The folder, packed library file, and the XML file must have the same name.
- FlexLogger does not support multiple plug-ins with the same name.
- When you modify a plug-in, you must close and re-open your FlexLogger project to use
 the updated plug-in.

#### Versioning

When you create a plug-in, the FlexLogger Plug-In Wizard assigns a version number to the
 plug-in. The wizard defines the version number in the <Version> and
 <OldestCompatibleVersion> tags in the plug-in XML file. Update the
 <Version> and <OldestCompatibleVersion>
 values to track updates to a plug-in that you have already added to a FlexLogger
 project.

Related tasks:

- Loading FlexLogger Plug-ins from Custom Locations

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=plug-in-parameters.html language=enus -->
## TOPIC 00026: Alternative Configuration - Plug-in Parameters

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `plug-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/plug-in-parameters.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: If you do not need to change settings while logging data, you can make Enabled, Multiplier, and Offset parameters of the plug-in instead of setpoint channels. Reconfigure the code from the previous example as follows: Update the class control to contain private data that can be passed between the VI

### Alternative Configuration - Plug-in
 Parameters

If you do not need to change settings
 while logging data, you can make Enabled, Multiplier, and Offset parameters of the plug-in
 instead of setpoint channels. Reconfigure the code from the previous example as
 follows:

1. Update the class control to contain private data that can be passed between the
 VIs. 
[IMAGE alt='image' src='GUID-CDD7DD59-E310-4189-AE9C-CBF10098B938-a5.png']
2. Modify Initialize VI to create the parameters for the plug-in. 
[IMAGE alt='image' src='GUID-0C726578-9BFA-4276-8DB5-2B1E457A79DF-a5.png']
3. Read the parameter values in Configure Session VI and update the
 private data. This VI is called whenever the user changes the parameter values from the
 Plug-in Configuration dialog box in FlexLogger. 
[IMAGE alt='image' src='GUID-6C552217-CC6B-4446-93D8-D41E6DAEBE26-a5.png']
4. Modify Process VI to use the Enabled, Multiplier, and Offset private
 data instead of parsing it out of the waveform data. 
[IMAGE alt='image' src='GUID-87C73697-34DD-4BD2-A199-D0CAE1F22762-a5.png'] 
 Below is the resulting plug-in configuration and channel table in
 FlexLogger: 
[IMAGE alt='image' src='GUID-8AB5E082-606D-40C8-A217-C0B4F5C615A3-a5.png'] 
 
[IMAGE alt='image' src='GUID-78B7EEF9-877D-4684-875D-112A5AD2007C-a5.png']

Parent topic:

Retrieve Data from Individual Channels

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=process-state-timing.html language=enus -->
## TOPIC 00027: Process Method Timing

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `process-state-timing.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/process-state-timing.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Initialize method, plug-ins which produce data or consume only setpoint data set the Timing Parameters that control how the Process method executes. If a plug-in reads waveform data from other FlexLogger channels, you should instead set the Resampling Parameters, which determine how input dat

### Process Method Timing

In the *Initialize* method, plug-ins which produce data or consume only setpoint
 data set the Timing Parameters that control how the
 *Process* method executes. If a plug-in reads waveform data from other FlexLogger
 channels, you should instead set the Resampling Parameters, which
 determine how input data will be resampled. Plug-ins should typically only use either the
 Set Plugin Timing VI or the Set Plugin Resampling VI
 in Initialize VI, but not both. In situations where the plug-in timing is
 not driven by the timing of the input data, you may want to use the Set Plugin Timing
 VI in addition to Set Plug-in Resampling VI.

| Timing Parameter | Timing Period (ms) required? | Description |
| --- | --- | --- |
| Periodic | Yes | With a timing period of n, periodic timing ensures at least n milliseconds between runs of the Process method. |
| Immediate | No | Run Process without delay. This method is typically used when a blocking call inside the Process method controls timing. |
| On Data Ready | Optional | For use by plug-ins that read channel data from FlexLogger—such as the Consume setpoint data from FlexLogger template. On Data Ready blocks execution of Process until FlexLogger sends new channel data to the plug-in.This parameter uses a timing period of n milliseconds as a time-out. After passing the time-out period, the plug-in executes Process without receiving new channel data from FlexLogger. If the time-out period is ≤0 ms, On Data Ready blocks execution of Process until FlexLogger sends new channel data to the plug-in. |
| Triggered | No | Not applicable for IO Plug-in development. |

| Resampling Parameter | Description |
| --- | --- |
| Resampling Mode | Determines how resampling of input waveforms will be done. In Minimum and Maximum mode the resampling rate is determined by the input channels. In Maximum mode any slower channels will be resampled to the rate of the fastest channel. In Custom mode resampling is done at a fixed rate specified by the Resampling Rate parameter. In Original Rate mode no resampling will be done. This mode should only be used if there is a single input channel. |
| Resampling Rate (Hz) | The rate to resample the data at if using Custom mode. |
| Drift Tolerance (seconds) | The amount of history to store in the plug-in waiting for time aligned data from different sources. A high number here increases the memory usage of the plug-in, a low number potentially causes issues with plug-ins which are not synchronized. |
| Block Size (seconds) | The minimum amount of overlapping data that should be present before the Process method is called. |

Parent topic:

Processing Element Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=processing-element-class.html language=enus -->
## TOPIC 00028: Processing Element Class

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `processing-element-class.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/processing-element-class.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how execution states are managed by FlexLogger plug-ins. The Processing Element class, Processing Element.lvclass, defines the plug-in execution states. The FlexLogger data engine manages the transitions between these states with a set of methods. Refer to the following figure and table to lea

### Processing Element Class

Learn how execution states are managed by FlexLogger plug-ins.

The Processing Element class, Processing Element.lvclass, defines the
 plug-in execution states. The FlexLogger data engine manages the transitions between these
 states with a set of methods. Refer to the following figure and table to learn more about each
 method.

[IMAGE alt='image' src='GUID-5CF0C503-3F87-480C-855F-601F0A429079-a5.svg']

| Method | Description |
| --- | --- |
| Initialize | Runs only once—When you add a plug-in to the FlexLogger Channel Specification.Defines the timing method used by the Process method.Declare the plug-in parameters users interact with in FlexLogger.Declare the channels (and corresponding channel parameters) the plug-in will read data from or send data to. |
| Configure Session | Runs when you make a configuration change while FlexLogger is not running a test.Initialize and configure hardware/instrument sessions. Runs after the Initialize method.Read the latest channel parameters set in FlexLogger. Read the latest plug-in parameters set in FlexLogger.Set the timing information (dt, T0) for data written to FlexLogger in the Process method.Read what channels FlexLogger reports as valid (channels defined by the plug-in may be modified in FlexLogger). |
| Process | Read from and write to third-party hardware. Read channel data from FlexLogger.Write channel data to FlexLogger. |
| Cleanup Session | Runs when you make a configuration change.Cleans up the hardware sessions and resources initialized by the Configure Session method. |
| Finalize | Runs when you remove a plug-in from your FlexLogger project or close the project. Cleans up any resources initialized during the Initialize method. Commonly empty. |

Parent topic:

FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=read-and-write-waveform-channels.html language=enus -->
## TOPIC 00029: Read and Write Waveform Channels

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `read-and-write-waveform-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/read-and-write-waveform-channels.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug-ins created from the Perform calculation template read waveform data from FlexLogger and publish waveform or string data to FlexLogger. You can also create a plug-in which only reads waveform data and does not publish any data back to FlexLogger. To map FlexLogger channels to a plug-in use the

### Read and Write Waveform Channels

Plug-ins created from the Perform calculation template read waveform data from FlexLogger and
 publish waveform or string data to FlexLogger. You can also create a plug-in which only reads
 waveform data and does not publish any data back to FlexLogger.

[IMAGE alt='image' src='GUID-65C15F4B-9AE0-4ACA-B139-41F05279F4FC-a5.svg']

To map FlexLogger channels to a plug-in use the Plug-in class Write Parameter
 VI
 Single Channel or Multiple Channel modes. The Single
 Channel mode maps one named parameter to one channel while the Multiple
 Channel mode maps one named parameter to multiple FlexLogger channels.

[IMAGE alt='image' src='GUID-A34E79BF-6572-4246-8D5E-02F3B232B67D-a5.png']

Select the channels you want to map from the plug-in level Configure
 gear located to the right of the plug-in name.

Note

Write Parameter VI

[IMAGE alt='image' src='GUID-01EEF5B7-515C-47C1-B3EB-7A7885F19083-a5.png']

Select the channels you want to map from the channel-in level
 Configure gear that appears to the left of the channel name when you
 hover over the channel.

When using the minimum or maximum resampling mode of a plug-in, it is common that the rate of
 the waveform channels produced by the plug-in match the rate of the input. Since the rate can
 change dynamically based on your channel selection in these modes, a new type of channel,
 Produced by Plugin (Resampler Timing), is provided which automatically
 adapts to these changes in sample rate. NI recommends creating your producer channels with
 this option whenever the resampling mode is set to Minimum or
 Maximum.

[IMAGE alt='image' src='GUID-A4F68435-F81B-435C-B729-27652F2E0788-a5.png']

Note

When reading waveforms from other channels, the length of the waveform will be determined
 by how much data that channel wrote in one cycle of its Process VI. Since
 the waveforms are not combined, waiting for longer periods between reads does not result in
 more data in the waveform, but in more waveforms in the queue that can be read by
 Read 1D Wfm VI.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=read-setpoint-channels-from-flexlogger.html language=enus -->
## TOPIC 00030: Read Setpoint Channels from FlexLogger

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `read-setpoint-channels-from-flexlogger.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/read-setpoint-channels-from-flexlogger.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug-ins created from the Consume setpoint data template read values from user settable controls in FlexLogger and use those values to control third-party output devices. To create a channel that consumes setpoint channel information from FlexLogger, use the Setpoint consumed by Plugin option in Cre

### Read Setpoint Channels from FlexLogger

Plug-ins created from the Consume setpoint data template read values from user settable
 controls in FlexLogger and use those values to control third-party output devices.

[IMAGE alt='image' src='GUID-09FA1ACD-F54E-4240-8550-4E9A4282EEE7-a5.svg']

To create a channel that consumes setpoint channel information from FlexLogger, use the
 Setpoint consumed by Plugin option in Create Channel
 VI.

[IMAGE alt='image' src='GUID-0FB7634A-4813-43B5-B62A-0FDC65235E48-a5.png']

As demonstrated by the Process VI in the Consume setpoint data template,
 the Plug-in class Read Latest Setpoints VI extracts the most recent scalar
 value and provides a one-dimensional array of setpoints (one per channel).

[IMAGE alt='image' src='GUID-5DEE039B-E274-483A-AF88-CAFBCEF464A5-a5.png']

In the IVI DC Power Supply example, the setpoint value read from FlexLogger is used as the
 level input to set the Power Supply DC voltage level.

[IMAGE alt='image' src='GUID-59656881-80F5-4396-9347-29E7DDF459C8-a5.png']

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=requirements.html language=enus -->
## TOPIC 00031: FlexLogger Plug-In Development Kit Requirements

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `requirements.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/requirements.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FlexLogger Plug-In Development Kit works with LabVIEW and FlexLogger. Refer to the LabVIEW documentation and FlexLogger documentation to ensure your system meets the specified minimum requirements. Software Version Compatibility Refer to FlexLogger Plug-In Development Kit Compatibility with Flex

### FlexLogger Plug-In Development Kit
 Requirements

The FlexLogger Plug-In Development Kit works with LabVIEW and FlexLogger. Refer to the
 LabVIEW documentation and FlexLogger documentation to ensure your system meets the
 specified minimum requirements.

#### Software Version Compatibility

Refer to *FlexLogger Plug-In Development Kit Compatibility with FlexLogger and LabVIEW* for an updated list of compatible software versions.

Related information:

- FlexLogger Plug-In Development Kit Compatibility with FlexLogger
 and LabVIEW
- FlexLogger System Requirements
- LabVIEW System Requirements

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=retrieve-data-from-individual-channels.html language=enus -->
## TOPIC 00032: Retrieve Data from Individual Channels

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `retrieve-data-from-individual-channels.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/retrieve-data-from-individual-channels.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To read waveforms from other plug-ins or use a setpoint channel in the Process VI, use either the Read 1D Wfm VI or Read Latest Setpoints VI based on the types of channels that are configured. Use Read 1D Wfm VI to return an array of data for each waveform or setpoint channel. Use Read Latest Setpoi

### Retrieve Data from Individual Channels

To read waveforms from other plug-ins or use a setpoint channel in the Process
 VI, use either the Read 1D Wfm VI or Read Latest
 Setpoints VI based on the types of channels that are configured. Use Read
 1D Wfm VI to return an array of data for each waveform or setpoint channel. Use
 Read Latest Setpoints VI to return the latest value for each waveform and
 setpoint channel.

Note

Process VI

If you have a mix of analog and digital data to read, you can use one of these VIs to
 read the analog data and one of the corresponding digital VIs to read the digital data.

The following is an example plug-in that scales waveforms from other channels based on
 setpoint channels. These setpoint channels provide a multiplier, offset, and
 a digital setpoint to enable or disable the scaling.

The Initialize VI could look like the following to enable the user to
 select waveforms from other channels in FlexLogger and use setpoint channels to change
 parameters while logging data.

[IMAGE alt='image' src='GUID-85E1F9EF-5C08-40FA-89C4-0D800CB6457C-a5.png']

Based on the configuration of the previous Initialize VI, the
 Process VI might look like the following:

[IMAGE alt='image' src='GUID-1651F2CE-8F15-4303-B87C-7DB93D74E5FB-a5.png']

Read 1D Wfm VI gets all of the analog data and returns it as an array. The
 Offset and Mult parameters receive the setpoint
 channel data of the plug-in and Select Channels receives the waveform data. Select
 Channels is a plug-in parameter that references waveforms from other FlexLogger
 channels the user specified in the Plug-in Configuration dialog box. Once
 the data is read, the Get Data from Stream VI parses specific waveforms
 based on the unique names used when creating the channels.

Read Digital Setpoint VI gets all of the digital setpoint
 and waveform data and returns a single point of the most recent data for all
 channels.

Below is the resulting channel table in FlexLogger.

[IMAGE alt='image' src='GUID-8E69ABBF-C748-4020-A5FC-4AAC29046C5B-a5.png']

Parent topic:

Channel Class

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=system-interface-class.html language=enus -->
## TOPIC 00033: System Interface Class

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `system-interface-class.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/system-interface-class.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The System Interface class (System Interface.lvclass) defines the execution environment interacting with a FlexLogger plug-in. When FlexLogger loads and runs a built plug-in, the plug-in will communicate with FlexLogger’s underlying data engine. When debugging a plug-in in the Plug-in Environment Si

### System Interface Class

The System Interface class (System Interface.lvclass) defines the
 execution environment interacting with a FlexLogger plug-in. When FlexLogger loads and runs a
 built plug-in, the plug-in will communicate with FlexLogger’s underlying data engine. When
 debugging a plug-in in the Plug-in Environment Simulator, the plug-in will communicate with a
 simplified, test-specific environment.

Parent topic:

FlexLogger Plug-In LabVIEW Classes

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=user-manual-welcome.html language=enus -->
## TOPIC 00034: FlexLogger Plug-In Development Kit User Manual

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/user-manual-welcome.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexLogger Plug-In Development Kit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related In

### FlexLogger Plug-In Development Kit
 User Manual

The FlexLogger Plug-In Development Kit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- FlexLogger Plug-In Development Kit Compatibility with FlexLogger and
 LabVIEW
- Download the FlexLogger Plug-In Development Kit
- License Setup and Activation
- FlexLogger Plug-In Development Kit Release Notes
- FlexLogger User Manual
- FlexLogger Python API Overview
- FlexLogger Python API Reference
- FlexLogger Plug-In Development Kit API Reference

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=using-plug-ins-in-flexlogger.html language=enus -->
## TOPIC 00035: Using Plug-Ins in FlexLogger

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `using-plug-ins-in-flexlogger.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/using-plug-ins-in-flexlogger.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `task`
- source_description: Add and configure plug-in channels to your FlexLogger project so you can perform custom in-line calculations or collect data from third-party hardware devices. If you do not have a FlexLogger project already, create a FlexLogger project. For more information, refer to Creating a New Project. Launch

### Using Plug-Ins in FlexLogger

Add and configure plug-in channels to your FlexLogger project so you can perform custom
 in-line calculations or collect data from third-party hardware devices.

Creating a New
 Project

1. Launch FlexLogger and open your project.
2. Complete the following tasks for your desired goal. 
 Goal
 TasksAdd a plug-in to my project
 In the Channel Specification toolbar, select Add channels»Plug-in.
 Select the plug-in you want to add. Note If FlexLogger did not load
 any plug-ins on launch, the Plug-in option does not
 appear. For troubleshooting plug-in issues, refer to *FlexLogger
 Plug-In File Structure* and *FlexLogger Plug-In
 Debugging*.FlexLogger adds the plug-in you selected to the
 Channel Specification under the local system.
 Configure plug-in parameters
 Click Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] at the right
 edge of the plug-in header to open the plug-in configuration dialog box. Note When FlexLogger is running a
 test, you cannot modify plug-in parameters, and FlexLogger disables the
 plug-in Configure gear [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'].FlexLogger automatically generates the
 plug-in configuration dialog box with settings for the parameters you defined
 in the plug-in.
 Configure channel parameters
 Hover over an individual channel to see Configure
 [IMAGE alt='image' src='GUID-F0BE2D8A-8018-4B4E-A304-F42433AE741C-a5.png'] appear on the left side of the
 channel row.
 Click the gear to open the channel configuration dialog box.
 Note Channel-level parameters
 apply to only the selected channel.
 FlexLogger automatically generates the channel configuration dialog box with
 settings for parameters you defined in the plug-in.
 Stop logging a channel
 Hover over the channel and click Disable logging
 ([IMAGE alt='image' src='GUID-C90BC748-60E1-411C-B0B4-B7559C23CD7A-a5.png']).
 Delete a plug-in
 Click Delete
 [IMAGE alt='image' src='GUID-0286DF0A-B22C-47E6-95D6-EF0EB082D6E3-a5.png'] at the right edge of the plug-in
 header to remove a plug-in from your project.

Related concepts:

- FlexLogger Plug-In File Structure
- FlexLogger Plug-In Debugging

Related information:

- Creating a New Project — FlexLogger User Manual

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=viewing-errors-in-flexlogger.html language=enus -->
## TOPIC 00036: Viewing Errors in FlexLogger

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `viewing-errors-in-flexlogger.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/viewing-errors-in-flexlogger.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the plug-in class provides built-in error handling, it is important that developers wire their error wires to the provided error out terminals. For example, IVI class driver VIs publish errors on their error wires when the VIs are initialized incorrectly. Wiring the error terminals from the

### Viewing Errors in FlexLogger

Because the plug-in class provides built-in error handling, it is important that developers
 wire their error wires to the provided error out terminals. For example, IVI class driver VIs
 publish errors on their error wires when the VIs are initialized incorrectly. Wiring the error
 terminals from the driver VIs to the error out terminal ensures errors appear in FlexLogger as
 shown in the following figure.

Figure 1.

[IMAGE alt='image' src='GUID-656DE828-B2AA-4CDF-A159-14B833A54A86-a5.png']

In FlexLogger, three distinct error notifications appear.

- Detailed errors in the Errors and Warnings pane
- An error icon on the plug-in header
- The Error indicator next to the Stop Test button

Parent topic:

FlexLogger Plug-In Debugging

<!--NI_TOPIC bundle=flexlogger-plug-in-development-kit path=writing-channel-data-from-a-plug-in-to-flexlogger.html language=enus -->
## TOPIC 00037: Writing Channel Data from a Plug-In to FlexLogger

- bundle_id: `flexlogger-plug-in-development-kit`
- source_path: `writing-channel-data-from-a-plug-in-to-flexlogger.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-plug-in-development-kit/raw/resource/enus/writing-channel-data-from-a-plug-in-to-flexlogger.html
- document_id: `flexlogger-plug-in-development-kit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug-ins created from the Produce data for FlexLogger template send collected data to FlexLogger. Use the Produce data for FlexLogger template as a starting point for creating your own plug-ins that send channel data to FlexLogger. To create a channel that sends data to FlexLogger, select the Produc

### Writing Channel Data from a Plug-In to
 FlexLogger

Plug-ins created from the Produce data for FlexLogger template send collected data to
 FlexLogger. Use the Produce data for FlexLogger template as a starting point for creating your
 own plug-ins that send channel data to FlexLogger.

[IMAGE alt='Block diagram of the flow of data from a third party data aquisition device to the Produce Data for FlexLogger Plug-in to the FlexLogger Application.' src='GUID-A498875F-395D-49D8-9C82-AB685A551C95-a5.svg']

To create a channel that sends data to FlexLogger, select the Produced by
 Plugin mode in Create Channel VI. The Create Channel
 VI is in the Initialize method of the Produce data for FlexLogger template.

[IMAGE alt='Screenshot of the Create Channel VI with Produced by Plugin mode selected.' src='GUID-EB797458-A330-424A-AE0F-1F3EA038300A-a5.png']

You can write string data or waveform data to a FlexLogger channel. To write string data,
 specify 1D String (NChan 1 Sample) as the data type in the Write
 Data VI. The Write Data VI is in the Process method of the
 Produce data for FlexLogger template.

[IMAGE alt='Screenshot of the Write Data VI within the Produce data for FlexLogger plug-in template with 1D String (NCHan 1 Sampe) mode selected.' src='GUID-15DF3E53-18FD-40E8-A64D-1878C54E6193-a5.png']

When writing strings, you can optionally specify the time stamp at which the string is
 written. If you don't specify a time stamp, the VI will use the current time as the time stamp
 for when the string is written. The following image shows all of the inputs and outputs for
 the Write Data VI.

[IMAGE alt='Screenshot of the Write Data VI contextual help showing all the inputs and outputs.' src='GUID-7E07A78D-D65A-462E-B4BC-12668B56828D-a5.png']

To send waveform data, specify either a one or two-dimensional array of doubles.

[IMAGE alt='Screenshot of the Write Data VI with 1D DBL (NChan NSample) mode selected.' src='GUID-3A886BAD-B513-4C7D-8DD6-86D9687DBF23-a5.png']

[IMAGE alt='Screenshot of the Write Data VI with 2D DBL (NChan NSample) mode selected.' src='GUID-6F025977-02A5-4808-A57D-60BD7D32AD3E-a5.png']

Writing waveforms that overlap in time disrupts visualization and logging capabilities of
 FlexLogger. The Produce data for FlexLogger template uses the Set Stream Timing
 VI to send data to FlexLogger without overlap errors. The Set Stream
 Timing VI is in the Configure Session method and defines the waveform
 dt and Start Time timing parameters.

[IMAGE alt='Screenshot of the Set Stream Timing VI.' src='GUID-AE493D77-D8AB-4C92-BAAF-001E27D81A9C-a5.png']

Since the Configure Session method always executes before the Process method, the timing
 information for the output channel updates after every configuration change.

Parent topic:

Channel Class
