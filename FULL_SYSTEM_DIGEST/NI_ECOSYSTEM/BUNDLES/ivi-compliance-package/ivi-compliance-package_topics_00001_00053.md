# NI DOCUMENT BUNDLE: ivi-compliance-package

<!--NI_BUNDLE_CHUNK bundle=ivi-compliance-package start=1 end=53 -->
<!--NI_TOPIC bundle=ivi-compliance-package path=analyzing-your-program-with-ni-i-o-trace.html language=enus -->
## TOPIC 00001: Analyzing Your Program with NI I/O Trace

- bundle_id: `ivi-compliance-package`
- source_path: `analyzing-your-program-with-ni-i-o-trace.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/analyzing-your-program-with-ni-i-o-trace.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI I/O Trace is an application monitor for Windows applications using NI drivers. NI I/O Trace can monitor, record, and display calls made to IVI class drivers. You can use NI I/O Trace to quickly locate and analyze any erroneous calls that your application makes to the IVI class drivers. NI I/O Tr

### Analyzing Your Program with NI I/O Trace

NI I/O Trace is an application monitor for Windows applications using NI drivers. NI I/O
 Trace can *monitor, record, and display calls* made to IVI class drivers. You
 can use NI I/O Trace to quickly locate and analyze any erroneous calls that your
 application makes to the IVI class drivers.  NI I/O Trace captures all function calls
 made during a class driver session.

To monitor IVI class driver calls, the NI Spy attribute must be enabled on the class driver
 session. This attribute is enabled by default. You can programmatically disable the
 attribute by setting it to FALSE.

The following figure shows a sample trace from NI I/O Trace.

[IMAGE alt='image' src='GUID-276285E1-4806-4FF7-ADF0-64374D45D41A-a5.gif']

NI I/O Trace records all input parameters passed to a function and all output parameters that the
 function returns. NI I/O Trace also displays the return value of the function.

You can see detailed information for every call NI I/O Trace captures through property sheets.
 The following figure shows a sample property sheet.

[IMAGE alt='image' src='GUID-0266A56F-8AE9-4BE7-A72F-8326C212BD68-a5.gif']

The property sheets display detailed information such as:

- Information about the application that made each call and the time stamp of the call
- The input and output parameters to each call and the contents of buffer parameters
- Descriptive error information
- Interchangeability warnings
- Information regarding the coercion of attribute values

<!--NI_TOPIC bundle=ivi-compliance-package path=base-capabilities.html language=enus -->
## TOPIC 00002: Base Capabilities

- bundle_id: `ivi-compliance-package`
- source_path: `base-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/base-capabilities.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Base capabilities are the functions and attributes of an instrument class that are common to most of the instruments in that class. A class driver should cover 95% of the instruments in a particular class. For a specific driver to be compliant with a class, it must implement all the base capabilitie

### Base Capabilities

Base capabilities are the functions and attributes of an instrument class that are common to
 most of the instruments in that class. A class driver should cover 95% of the instruments in a
 particular class. For a specific driver to be compliant with a class, it must implement all
 the base capabilities.

For example, the base capabilities of the oscilloscope class have functions and attributes that
 configure an edge-triggered acquisition, initiate an acquisition, and return the acquired
 waveform. You can find more information about the Capability Groups in the *Related
 information*.

Parent topic:

Class Capability Groups

Related information:

- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=call-properties.html language=enus -->
## TOPIC 00003: Call Properties

- bundle_id: `ivi-compliance-package`
- source_path: `call-properties.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/call-properties.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI I/O Trace records detailed information about each call it captures. To see the detailed information for a specific call, use one of the following methods: Double-click the call in the capture window. Select the call and press <Enter>. Select the call and select View»Properties. Select the call an

### Call Properties

NI I/O Trace records detailed information about each call it captures. To see the detailed
 information for a specific call, use one of the following methods:

- Double-click the call in the capture window.
- Select the call and press <Enter> .
- Select the call and select View»Properties .
- Select the call and click Properties .

The Property Sheet dialog box contains additional information when it shows a call to an IVI
 class driver. Refer to *NI I/O Trace Help* for more information about the
 NI I/O Trace Property Sheet dialog box.

#### Input Tab

The following figure shows the
 Input tab of the Property Sheet dialog box.

[IMAGE alt='image' src='GUID-35DC6862-09F7-4A06-902A-B732FC3CB2C7-a5.gif']

The Input tab displays the input parameters value for a function call. When the
 class driver initialize function is called, it passes the logical name of the
 instrument you want to initialize. The initialize function returns an IVI session
 handle that identifies the instrument session. You pass the IVI session handle as
 the vi input parameter to all other class driver functions.
 For functions that have a vi input parameter that represents
 an IVI session handle, NI I/O Trace displays the value of the
 vi input parameter and the logical name that corresponds
 to the value. Thus, you can easily identify the particular instrument session that a
 call accesses.

#### Output Tab

The Output tab displays the
 output parameters and status information for the function call. For calls to an IVI
 class driver, NI I/O Trace displays additional error information. This information
 includes the primary error, the secondary error, and any error elaboration
 information.

The following figure shows the Output tab of the NI I/O Trace
 Property Sheet with information from a call to an IVI class driver.

[IMAGE alt='image' src='GUID-34EA975B-58FB-448D-9775-C6062975CF5B-a5.gif']

#### Interchange Warnings Tab

You can use NI
 I/O Trace to view interchangeability warnings. If you enable interchangeability
 checking and a class driver function encounters an interchangeability warning, an
 Interchange Warnings tab appears on the NI I/O Trace Property Sheet dialog box for
 the function call. The Interchange Warnings tab displays the interchangeability
 warnings that the function call produced. The following figure shows the Interchange
 Warnings tab.

[IMAGE alt='image' src='GUID-74BDD1B5-F3A3-4D8B-BC4F-98F3CBD3C0FD-a5.gif']

#### Coercions Tab

You can view how the
 specific driver coerces ViInt32 and ViReal64 values with NI I/O Trace. If you enable
 coercion recording and the specific driver coerces values that you pass to a class
 driver function, a Coercions tab appears on the NI I/O Trace Property Sheet dialog
 box for the function call. The following figure shows the Coercions tab.

[IMAGE alt='image' src='GUID-C5557C80-10BC-469D-BEBD-97315A5EDB3C-a5.gif']

The Coercions tab displays the name of the attribute that the specific driver
 coerced, the value that you specified in your program, and the value to which the
 specific driver coerced the attribute. If the attribute is channel based, the
 Coercions tab also displays the channel name.

Parent topic:

Analyzing Your Program with NI I/O Trace

Related information:

- NI I/O Trace Help

<!--NI_TOPIC bundle=ivi-compliance-package path=capturing-calls-to-ivi-class-drivers.html language=enus -->
## TOPIC 00004: Capturing Calls to IVI Class Drivers

- bundle_id: `ivi-compliance-package`
- source_path: `capturing-calls-to-ivi-class-drivers.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/capturing-calls-to-ivi-class-drivers.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: To view calls to IVI class drivers, you must enable capturing. When you launch NI IO Trace, capturing is disabled. To enable capturing, use one of the following methods: Select IO Trace»Start Capture. Click the blue arrow on the toolbar. Press <F8>. After you enable capturing, run your application t

### Capturing Calls to IVI Class Drivers

To view calls to IVI class drivers, you must enable capturing. When you launch NI IO Trace,
 capturing is disabled. To enable capturing, use one of the following methods:

- Select IO Trace»Start Capture .
- Click the blue arrow on the toolbar.
- Press <F8> .

After you enable capturing, run your application then return to NI IO Trace to view the captured
 calls. For a complete description of how to use NI I/O Trace, refer to the *NI IO
 Trace Help*. To view the NI IO Trace help, select Help»Help
 Topics. The following figure shows calls to the IviScope class driver
 that NI IO Trace captured.

[IMAGE alt='image' src='GUID-5795D1A0-652A-4496-818D-7085CE6421F7-a5.gif']

NI IO Trace displays the name of each class driver function call that it captures. For each
 function call, NI IO Trace displays the values of the input and output parameters. You
 can configure NI IO Trace to display the following details about the function call:

- Number
- Description
- Status
- Time
- Process ID
- Thread ID

If a function returns an error, NI IO Trace highlights the function call in red. If you enable
 interchangeability checking, NI IO Trace highlights the functions that report
 interchangeability warnings in blue.

Parent topic:

Analyzing Your Program with NI I/O Trace

Related information:

- NI I/O Trace Help

<!--NI_TOPIC bundle=ivi-compliance-package path=class-capability-groups.html language=enus -->
## TOPIC 00005: Class Capability Groups

- bundle_id: `ivi-compliance-package`
- source_path: `class-capability-groups.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/class-capability-groups.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because many instruments of a given class have additional, different functionality, no single programming interface can work with all instruments. For this reason, the IVI class drivers divide the instrument capabilities into categories shown in the Related concepts.

### Class Capability Groups

Because many instruments of a given class have additional, different functionality, no single
 programming interface can work with all instruments. For this reason, the IVI class
 drivers divide the instrument capabilities into categories shown in the*Related
 concepts*.

Parent topic:

IVI Driver Help Introduction

Related concepts:

- Inherent IVI Capabilities
- Base Capabilities
- Extension Groups
- Instrument Specific Capabilities

<!--NI_TOPIC bundle=ivi-compliance-package path=class-driver-apis.html language=enus -->
## TOPIC 00006: Class Driver APIs

- bundle_id: `ivi-compliance-package`
- source_path: `class-driver-apis.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/class-driver-apis.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI class APIs conform to the specifications of the IVI Foundation. Class Driver PrefixThe IVI class drivers work with a large set of specific drivers. Each class driver has a unique class prefix that gives the class driver unique and meaningful names and avoids conflicts with other instrument d

### Class Driver APIs

The IVI class APIs conform to the specifications of the IVI Foundation.

#### Class Driver Prefix

The IVI class drivers work with a large set of
 specific drivers. Each class driver has a unique class prefix that gives the class
 driver unique and meaningful names and avoids conflicts with other instrument driver
 functions, attributes, and files. Each function name and attribute ID in the class
 driver begins with the class prefix.

The names of all component files (.fp,
 .h, .dll, .llb, and so on) of the class driver begin with the class
 prefix.

| Digital Multimeter | IviDmm | IVIDMM_ | ividmm.* |
| --- | --- | --- | --- |
| Oscilloscope | IviScope | IVISCOPE_ | iviscope.* |
| Function Generator | IviFgen | IVIFGEN_ | ivifgen.* |
| DC Power Supply | IviDCPwr | IVIDCPWR_ | ividcpwr.* |
| AC Power Supply | IviACPwr | IVIDAPWR_ | iviacpwr.* |
| Switch | IviSwtch | IVISWTCH_ | iviswtch.* |
| Power Meter | IviPwrMeter | IVIPWRMETER_ | ivipwrmeter.* |
| RF Signal Generator | IviRFSigGen | IVIRFSIGGEN_ | ivirfsiggen.* |
| Spectrum Analyzer | IviSpecAn | IVISPECAN_ | ivispecan.* |
| Counter | IviCounter | IVICOUNTER_ | ivicounter.* |
| Digitizer | IviDigitizer | IVIDIGITIZER_ | ividigitizer.* |
| Downconverter | IviDownconverter | IVIDOWNCONVERTER_ | ividownconverter.* |
| Upconverter | IviUpconverter | IVIUPCONVERTER_ | iviupconverter.* |

Parent topic:

IVI Driver Help Introduction

<!--NI_TOPIC bundle=ivi-compliance-package path=class-driver-relationship-to-instrument-speci.html language=enus -->
## TOPIC 00007: Class Driver Relationship to Instrument Specific Drivers

- bundle_id: `ivi-compliance-package`
- source_path: `class-driver-relationship-to-instrument-speci.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/class-driver-relationship-to-instrument-speci.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows an example of the relationship between the capability groups of a class driver and a specific driver. In this figure, the class driver implements the inherent IVI capabilities, the base instrument capabilities, and two extension capability groups. The specific driver imple

### Class Driver Relationship to Instrument Specific Drivers

The following figure shows an example of the relationship between the capability groups of a
 class driver and a specific driver. In this figure, the class driver implements the
 inherent IVI capabilities, the base instrument capabilities, and two extension
 capability groups. The specific driver implements the inherent IVI capabilities, the
 base instrument capabilities, one of the extension capability groups, and instrument
 specific capabilities.

[IMAGE alt='image' src='GUID-CE836FDC-CFBD-4534-8D2B-E972951A1D49-a5.gif']

The class driver dynamically loads the specific driver. The IVI class drivers require that the
 specific driver be in a .dll, .c, or .obj file. The specific drivers normally come in
 .dll and .c file formats. If you use the class drivers outside of the LabWindows/CVI
 environment, you must use the .dll file.

In general, when a test program calls functions and attributes of a capability group in the class
 driver, the class driver maps these calls to the corresponding capability group in the
 specific driver. If the test program attempts to call extension group functions that the
 specific driver does not implement, the class driver returns an error.

The class driver does not implement instrument specific capabilities. Instead, the test program
 accesses the instrument specific capabilities by invoking functions and attributes of
 the specific driver directly.

Note

In the figure above, a dashed line connects the inherent IVI capabilities of the class driver and
 specific driver because some inherent IVI functions and attributes are accessible only
 through the class driver. If you initialize an instrument driver session by calling the
 initialize function in the specific driver, you cannot access the class–only functions
 and attributes.

Note

class prefixes

| Description | Function Name |
| --- | --- |
| Specific Driver Module Pathname | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_LOCATOR |
| Class Revision | CLASSPREFIX_ATTR_CLASS_DRIVER_REVISION |
| Class Specification Major Version | CLASSPREFIX_ATTR_CLASS_DRIVER_SPEC_MAJOR_VERSION |
| Class Specification Minor Version | CLASSPREFIX_ATTR_CLASS_DRIVER_SPEC_MINOR_VERSION |
| Class Driver Vendor | CLASSPREFIX_ATTR_CLASS_DRIVER_VENDOR |
| Class Driver Description | CLASSPREFIX_ATTR_CLASS_DRIVER_DESCRIPTION |
| Spy | CLASSPREFIX_ATTR_SPY |
| Use Specific Simulation | CLASSPREFIX_ATTR_USE_SPECIFIC_SIMULATION |
| Function Capabilities | CLASSPREFIX_ATTR_FUNCTION_CAPABILITIES |

Parent topic:

Class Capability Groups

Related concepts:

- Class Driver APIs

<!--NI_TOPIC bundle=ivi-compliance-package path=class-driver-simulation.html language=enus -->
## TOPIC 00008: Class Driver Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `class-driver-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/class-driver-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI class drivers provide simulation tools. You can use these tools to create simulated output data. The class drivers provide simulation by using a simulation driver. Simulation drivers are components that plug into a class driver. The class driver uses the simulation driver to generate data.IC

### Class Driver Simulation

The IVI class drivers provide simulation tools. You can use these tools to create simulated
 output data. The class drivers provide simulation by using a simulation driver. Simulation
 drivers are components that plug into a class driver. The class driver uses the simulation
 driver to generate data.

ICP installs a simulation driver for each IVI class driver. Each simulation driver communicates
 with the corresponding class driver to perform more flexible data generation than in
 instrument specific drivers. The following diagram illustrates how a class driver uses a class
 simulation driver.

[IMAGE alt='image' src='GUID-1B0DAEB8-DB16-477C-B876-C0371F160433-a5.gif']

#### Class Simulation Driver

When your program calls a class driver, the
 class driver calls the corresponding function in the specific driver. When you enable
 simulation, the class driver opens an additional session that is assigned to its class
 simulation driver. Whenever you invoke a function in the class driver, the class driver
 first calls the corresponding function in the specific driver and then calls the same
 function in the class simulation driver. The specific driver performs range checking and
 coercion on all input parameters, and the class simulation driver generates the simulated
 output data and status codes.

Simulation drivers have two modes: interactive and
 non-interactive. You specify whether to use interactive or non-interactive simulation with
 MAX. In interactive mode, simulation drivers have pop-up user interface panels that allow
 you to configure the parameters for generating the simulated output data.

For example,
 when you initialize the IviDmm class driver in simulation mode, the simulation driver
 displays the panel shown in the following figure.

[IMAGE alt='image' src='GUID-C74DE595-4D25-47F0-8500-5EC279DFB2C6-a5.gif']

From the panel, you can select a base measurement value and an offset. For example, in
 the previous figure, the panel settings specify a value of 10.0 with a range of ±1.0. You
 can configure the driver to display the panel each time the program calls a function that
 returns measurement data, or you can configure the driver to generate the data automatically
 within the range you specify. In non-interactive mode, the simulation driver returns data to
 the program without requiring further user interaction.

In addition to generating
 simulated measurement data, you can use the class simulation features to generate simulated
 results for the Self-Test, Error Query, and Revision Query functions that all IVI drivers
 export. You can also use the class simulation tools to generate simulated completion codes
 for the instrument driver functions. Use this feature to verify that your program correctly
 handles error conditions that the instrument driver might return.

To configure all the
 features of the simulation driver, use attributes in the simulation driver. When you use
 non-interactive simulation, you configure the attributes of the simulation driver with MAX
 without modifying your test program code.

ICP includes C source code for the class
 simulation drivers. You can develop robust simulated data generation algorithms for your
 test systems and incorporate them into the simulation drivers. Whenever you swap to a
 different instrument, you can reuse your developed simulation code because the simulation
 drivers work with the class drivers.

Parent topic:

IVI Driver Help Introduction

Related concepts:

- IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=completely-specifying-the-state-of-the-instru.html language=enus -->
## TOPIC 00009: Completely Specifying the State of the Instrument

- bundle_id: `ivi-compliance-package`
- source_path: `completely-specifying-the-state-of-the-instru.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/completely-specifying-the-state-of-the-instru.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: To maximize interchangeability, you must completely specify the state of the attributes that affect the behavior of the instrument. If you do not, the behavior of your program depends on instrument specific settings that can result from any of the following conditions: The power-on settings of the d

### Completely Specifying the State of the Instrument

To maximize interchangeability, you must completely specify the state of the attributes that
 affect the behavior of the instrument. If you do not, the behavior of your program
 depends on instrument specific settings that can result from any of the following
 conditions:

- The power-on settings of the device.
- The state that the instrument configures for an attribute as a result of your program configuring other attributes.
- The state that a previous program configured for the instrument.

If you do not specify the state of the instrument completely, you considerably increase the chance that your program will not behave the same way when you swap instruments or you run your programs in a different order.

capability group

base capabilities

extension capability group

Note

IVIDMM_ATTR_SAMPLE_COUNT

IVIDMM_ATTR_SAMPLE_TRIGGER

IVIDMM_ATTR_SAMPLE_INTERVAL

SAMPLE_TRIGGER

IVIDMM_VAL_INTERVAL

IVIDMM_ATTR_SAMPLE_INTERVAL

Parent topic:

Developing an Instrument Independent Application

Related concepts:

- Class Capability Groups
- Base Capabilities
- Extension Groups

<!--NI_TOPIC bundle=ivi-compliance-package path=configuring-ni-i-o-trace.html language=enus -->
## TOPIC 00010: Configuring NI I/O Trace

- bundle_id: `ivi-compliance-package`
- source_path: `configuring-ni-i-o-trace.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/configuring-ni-i-o-trace.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: To monitor a particular driver session, you must enable monitoring for that driver session and for the IVI class driver. Refer to Measurement & Automation Explorer Help for IVI for more information about how to use MAX to enable monitoring for a particular driver session.To enable monitoring for an

### Configuring NI I/O Trace

To monitor a particular driver session, you must enable monitoring for that driver session and
 for the IVI class driver. Refer to *Measurement & Automation Explorer Help for
 IVI* for more information about how to use MAX to enable monitoring for a
 particular driver session.

To enable monitoring for an IVI class driver within NI I/O Trace, launch NI I/O Trace by clicking
 Start»Programs»National Instruments»NI I/O Trace. To enable
 monitoring for a particular class driver, select I/O
 Trace»Options. The class drivers appear in the NI I/O Trace Options
 dialog box for you to select. By default, all class drivers are selected for monitoring.
 The following figure shows the NI I/O Trace Options dialog box where you enable this
 setting.

[IMAGE alt='image' src='GUID-808779C5-8534-45D8-AC6A-BF10BB415C3C-a5.gif']

Parent topic:

Analyzing Your Program with NI I/O Trace

Related information:

- Measurement & Automation Explorer Help
 for IVI

<!--NI_TOPIC bundle=ivi-compliance-package path=configuring-the-simulation-driver-session.html language=enus -->
## TOPIC 00011: Configuring the Simulation Driver Session

- bundle_id: `ivi-compliance-package`
- source_path: `configuring-the-simulation-driver-session.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/configuring-the-simulation-driver-session.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to NI IVI Driver Help»Configuring Your System for more information about configuring the simulation driver session in MAX.

### Configuring the Simulation Driver Session

Refer to 
NI IVI Driver Help»Configuring Your System for more information about configuring the simulation driver session in MAX.

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=developing-a-reference-program.html language=enus -->
## TOPIC 00012: Developing a Reference Program

- bundle_id: `ivi-compliance-package`
- source_path: `developing-a-reference-program.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/developing-a-reference-program.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: One technique for verifying instrument replacement candidates is to create a reference program. You can create the reference program when you specify the requirements of your test program or when you develop your test program. The reference program uses an IVI class driver to programmatically descri

### Developing a Reference Program

One technique for verifying instrument replacement candidates is to create a reference program.
 You can create the reference program when you specify the requirements of your test
 program or when you develop your test program. The reference program uses an IVI class
 driver to programmatically describe all the instrument configurations and operations
 that you require.

To verify whether a new instrument can work with your program, execute the reference program
 using the specific driver for the new instrument. You can run the reference program with
 the physical instrument or with *simulation enabled*. If you can execute the
 reference program without errors using the new instrument, then you can probably use the
 new instrument with your existing application. Depending on how many errors and the
 types of errors the reference program generates, you can gauge the degree to which you
 must modify your program to make it work with the new instrument.

Parent topic:

Verifying Instrument Replacement Candidates

Related information:

- Enabling Instrument Simulation

<!--NI_TOPIC bundle=ivi-compliance-package path=developing-an-instrument-independent-applicat.html language=enus -->
## TOPIC 00013: Developing an Instrument Independent Application

- bundle_id: `ivi-compliance-package`
- source_path: `developing-an-instrument-independent-applicat.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/developing-an-instrument-independent-applicat.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following links describe items to consider when you use IVI class drivers to develop an instrument-independent test program. Follow the guidelines contained in the following links to maximize the potential for your application to work with other instruments.

### Developing an Instrument Independent Application

The following links describe items to consider when you use IVI class drivers to develop an
 instrument-independent test program. Follow the guidelines contained in the following
 links to maximize the potential for your application to work with other instruments.

<!--NI_TOPIC bundle=ivi-compliance-package path=disabling-unused-extensions.html language=enus -->
## TOPIC 00014: Disabling Unused Extensions

- bundle_id: `ivi-compliance-package`
- source_path: `disabling-unused-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/disabling-unused-extensions.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you use an instrument that has extended capabilities but your application does not configure the settings for the extended capabilities, the settings are in an unknown state. The unknown state could affect the behavior of the instrument capabilities that the program does use. Furthermore, the unk

### Disabling Unused Extensions

If you use an instrument that has extended capabilities but your application does not configure
 the settings for the extended capabilities, the settings are in an unknown state. The
 unknown state could affect the behavior of the instrument capabilities that the program
 does use. Furthermore, the unknown state is likely to vary from one instrument to
 another. The settings are likely to be the power-on settings for the instrument. The
 power-on settings vary from instrument to instrument.

To avoid having different behavior when used with different instruments, each instrument
 specific driver disables unused extensions by setting the extensions to an
 interchangeable state. This interchangeable state renders the extension group unable to
 affect the behavior of the instrument. Normally, an extension remains disabled until
 your program explicitly uses it. At which point the instrument driver does not have to
 take any other action. Therefore, if your program sets any values of the extension
 group, the specific driver does not enable the extension group.

For example, the IviDmm base capabilities control DMMs that take a single measurement. The
 IviDmm class defines a multipoint extension group that controls DMMs that can acquire
 multiple samples from multiple triggers. If you develop a program that sues only the
 IviDmm base capabilities with an instrument that implements the multipoint extension
 group, the IviDmm-compliant specific driver sets the multipoint extension group
 attributes to an interchangeable state when you call either Initiate or Read functions
 for IviDmm. In addition to these functions, the driver also disables all extensions in
 the Initialize and Reset With Defaults functions.

To disable the multipoint extension group to the interchangeable state, the IviDmm-compliant
 specific driver sets the trigger count attribute to 1 and the sample count attribute to
 1. In this configuration, the multipoint extension group does not affect the behavior of
 the instrument. Therefore, you can run the program with instruments that implement only
 the IviDmm base capabilities as well as with instruments that implement the multipoint
 extension group.

For more information about the interchangeable state that the class drivers apply for disabling
 unused extensions, check the *Related concepts*.

Parent topic:

Class Driver Simulation

Related concepts:

- Interchangeability Checking

<!--NI_TOPIC bundle=ivi-compliance-package path=enabling-simulation-after-initializing.html language=enus -->
## TOPIC 00015: Enabling Simulation after Initializing

- bundle_id: `ivi-compliance-package`
- source_path: `enabling-simulation-after-initializing.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/enabling-simulation-after-initializing.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have disabled simulation when you initialize the instrument driver, some instrument drivers allow you to enable simulation at a later time. When you disable simulation at the time of initialization, the IVI Engine sets the driver to perform instrument I/O; therefore, the instrument must be pr

### Enabling Simulation after Initializing

If you have disabled simulation when you initialize the instrument driver, some instrument
 drivers allow you to enable simulation at a later time. When you disable simulation at
 the time of initialization, the IVI Engine sets the driver to perform instrument I/O;
 therefore, the instrument must be present in your system. You can then enable or disable
 simulation at any time by setting the PREFIX_ATTR_SIMULATE attribute. If you configure
 the simulation driver for interactive simulation, the simulation driver displays the
 Simulator Setup dialog box the first time you enable simulation. When you enable
 simulation, the simulation driver behaves as this topic describes. This approach is
 useful if you want to simulate the instrument only during specific times that you run
 your application.

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=extension-groups.html language=enus -->
## TOPIC 00016: Extension Groups

- bundle_id: `ivi-compliance-package`
- source_path: `extension-groups.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/extension-groups.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Extension groups contain specialized groups of functions and attributes that are common to many instruments in that class, but not all. The IVI specifications do not require specific instrument drivers to implement extension groups. With extension groups, the IVI class drivers create standard progra

### Extension Groups

Extension groups contain specialized groups of functions and attributes that are common to many instruments in that class, but not all. The IVI specifications do not require specific instrument drivers to implement extension groups. With extension groups, the IVI class drivers create standard programming interfaces for features and capabilities that are not common to every instrument of that class.

For example, although all oscilloscopes have similar base capabilities for vertical and horizontal settings, they have a wide variety of trigger modes. The IviScope class driver includes extensions for different trigger modes, such as TV trigger, runt trigger, width trigger, and so on. Every oscilloscope that has TV triggering can comply with the TV trigger extension group functions and attributes of the IviScope class. However, an oscilloscope that does not support the TV trigger extension group can still comply with the IviScope class because the oscilloscope can support the base capabilities of the IviScope class.

If you use an extension group in your program, any instrument you use with the program must support the extension group. The LabWindows/CVI function panels, LabVIEW VIs, and help file for the class drivers mark functions and attributes that are a part of an extension group with a special symbol. For example, the IviScope class driver help file marks the functions and attributes that control the TV trigger extension group with the symbol [TV].

You can find more information about the extension groups of a particular class in the
 *Related information*.

Parent topic:

Class Capability Groups

Related information:

- NI IVI Driver Help
- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=following-the-class-behavior-model.html language=enus -->
## TOPIC 00017: Following the Class Behavior Model

- bundle_id: `ivi-compliance-package`
- source_path: `following-the-class-behavior-model.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/following-the-class-behavior-model.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each IVI class driver defines a behavior model. The behavior model describes the relationships between the functions and attributes of the driver and the behavior of the instrument. The behavior model also describes the order of operations for configuring an instrument and controlling instrument ope

### Following the Class Behavior Model

Each IVI class driver defines a behavior model. The behavior model describes the relationships
 between the functions and attributes of the driver and the behavior of the instrument.
 The behavior model also describes the order of operations for configuring an instrument
 and controlling instrument operations. Follow the behavior model for each class to
 maximize the possibility of using your program with other instruments.

For example, the IviScope behavior model recommends that you fetch a waveform from the instrument
 after you have acquired it and before you reconfigure the instrument for the next
 acquisition. Some oscilloscopes destroy an acquired waveform each time you reconfigure
 them, so fetching prior to reconfiguration ensures that the acquired waveform is
 available. Other types of oscilloscopes do not destroy the acquired waveform each time
 you reconfigure them; however, you should follow the fetching recommendation of the
 behavior model so that your program can fetch acquired waveforms successfully from
 either type of oscilloscope.

| LabVIEW Behavior Model | LabWindows/CVI Behavior Model |
| --- | --- |
| IviACPwr | IviACPwr |
| IviDCPwr | IviDCPwr |
| IviDmm | IviDmm |
| IviFgen | IviFgen |
| IviScope | IviScope |
| IviSwtch | IviSwtch |
| IviPwrMeter | IviPwrMeter |
| IviRFSigGen | IviRFSigGen |
| IviSpecAn | IviSpecAn |
| IviCounter | IviCounter |
| IviDigitizer | IviDigitizer |
| IviDownconverter | IviDownconverter |
| IviUpconverter | IviUpconverter |

Parent topic:

Developing an Instrument Independent Application

Related information:

- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=inherent-ivi-capabilities.html language=enus -->
## TOPIC 00018: Inherent IVI Capabilities

- bundle_id: `ivi-compliance-package`
- source_path: `inherent-ivi-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/inherent-ivi-capabilities.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Inherent IVI Capabilities are the functions and attributes that all IVI class drivers implement.To complete the function names in the following table for any one of the IVI class drivers, replace ClassPrefix with one of the class prefixes. For example, for the digital multimeter DMM class ClassPrefi

### Inherent IVI Capabilities

Note

ClassPrefix_init

IviDMM_init

| Prefix Type | LabVIEW Inherent VI | LabWindows/CVI Inherent Function |
| --- | --- | --- |
| Initialize/Close— Contains VIs and functions that initialize and close instrument driver sessions. | ClassPrefix Initialize | ClassPrefix_init |
| ClassPrefix Initialize With Options | ClassPrefix_InitWithOptions |  |
| ClassPrefix Close | ClassPrefix_close |  |
| Set, Get, and Check Attribute/Property— Contains VIs and functions that set, get, and check the values of attributes. Type-safe functions exist for each attribute data type. The possible data types are ViInt32, ViReal64, ViString, ViBoolean, and ViSession. You insert one of these values in place of the place holder, <type>. | Use Property Node VI to get and set attributes. You can not check attributes in LabVIEW. ClassPrefix Invalidate All Attributes | ClassPrefix_SetAttribute<type> |
| ClassPrefix_GetAttribute<type> |  |  |
| ClassPrefix_CheckAttribute<type> |  |  |
| ClassPrefix_InvalidateAllAttributes |  |  |
| Utility— VIs and functions that control common instrument operations. These functions include many of the functions that VXIplug&play requires, such as reset, self-test, revision query, error query, and error message. This class also contains functions that access IVI error information, access interchangeability warnings, access coercion records, and lock the instrument driver session. | ClassPrefix Reset | ClassPrefix_reset |
| ClassPrefix Self-Test | ClassPrefix_self_test |  |
| ClassPrefix Revision Query | ClassPrefix_revision_query |  |
| ClassPrefix Error-Query | ClassPrefix_error_query |  |
| ClassPrefix Error Message | ClassPrefix_error_message |  |
| ClassPrefix Reset With Defaults | ClassPrefix_ResetWithDefaults |  |
| ClassPrefix Disable | ClassPrefix_Disable |  |
|  | ClassPrefix_GetSpecificDriverCHandle |  |
| Error Info Subcategory | Use the General Error Handler VI to view errors, which is the standard LabVIEW approach. | ClassPrefix_GetError |
| ClassPrefix_ClearError |  |  |
| Interchangeability Info Subcategory | ClassPrefix Get Next Interchange Warning | ClassPrefix_GetNextInterchangeWarning |
| ClassPrefix Reset Interchange Check | ClassPrefix_ResetInterchangeCheck |  |
| ClassPrefix Clear Interchange Warnings | ClassPrefix_ClearInterchangeWarnings |  |
| Coercion Info Subcategory | ClassPrefix | ClassPrefix_GetNextCoercionRecord |
| Get Next Coercion Record |  |  |
| Locking Subcategory | You cannot lock IVI sessions in LabVIEW. | ClassPrefix_LockSession |
| ClassPrefix_UnlockSession |  |  |

Note

The following table shows the inherent IVI properties/attributes.

| Prefix Type | LabVIEW Property | LabWindows/CVI Attribute |
| --- | --- | --- |
| User Options — Attributes that you can set to affect the behavior of class drivers and specific drivers. | Range Check | CLASSPREFIX_ATTR_RANGE_CHECK |
| Query Instrument Status | CLASSPREFIX_ATTR_QUERY_INSTRUMENT_STATUS |  |
| Cache | CLASSPREFIX_ATTR_CACHE |  |
| Simulate | CLASSPREFIX_ATTR_SIMULATE |  |
| Use Specific Simulation | CLASSPREFIX_ATTR_USE_SPECIFIC_SIMULATION |  |
| Record Value Coercions | CLASSPREFIX_ATTR_RECORD_COERCIONS |  |
| Interchange Check | CLASSPREFIX_ATTR_INTERCHANGE_CHECK |  |
| SPY | CLASSPREFIX_ATTR_SPY |  |
| Class Driver Identification— Attributes that describe the version, supplier, and prefix of the class driver. | Class Driver Description | CLASSPREFIX_ATTR_CLASS_DRIVER_DESCRIPTION |
| Class Driver Prefix | CLASSPREFIX_ATTR_CLASS_DRIVER_PREFIX |  |
| Class Driver Vendor | CLASSPREFIX_ATTR_CLASS_DRIVER_VENDOR |  |
| Class Driver Revision | CLASSPREFIX_ATTR_CLASS_DRIVER_REVISION |  |
| Class Driver Class Specification Major Version | CLASSPREFIX_ATTR_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION |  |
| Class Driver Class Specification Minor Version | CLASSPREFIX_ATTR_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION |  |
| Specific Driver Identification— Attributes that describe the version, supplier, location, and prefix of the specific driver. | Specific Driver Description | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| Specific Driver Prefix | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_PREFIX |  |
| Specific Driver Locator | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_LOCATOR |  |
| Specific Driver Vendor | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_VENDOR |  |
| Specific Driver Revision | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_REVISION |  |
| Specific Driver Class Specification Major Version | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION |  |
| Specific Driver Class Specification Minor Version | CLASSPREFIX_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION |  |
| Specific Driver Capabilities Category— Attributes that describe various capabilities of the instrument controlled by the instrument driver. | Supported Instrument Models | CLASSPREFIX_ATTR_SUPPORTED_INSTRUMENT_MODELS |
| Group Capabilities | CLASSPREFIX_ATTR_GROUP_CAPABILITIES |  |
| Function Capabilities | CLASSPREFIX_ATTR_FUNCTION_CAPABILITIES |  |
| Channel Count | CLASSPREFIX_ATTR_CHANNEL_COUNT |  |
| Instrument Identification— Attributes that provide model and firmware information about the instrument controlled by the instrument driver. | Manufacturer | CLASSPREFIX_ATTR_INSTRUMENT_MANUFACTURER |
| Model | CLASSPREFIX_ATTR_INSTRUMENT_MODEL |  |
| Firmware Revision | CLASSPREFIX_ATTR_INSTRUMENT_FIRMWARE_REVISION |  |
| Advanced Session Information— Attributes that provide resource and I/O session information regarding the class and specific driver. | Logical Name | CLASSPREFIX_ATTR_LOGICAL_NAME |
| Resource Descriptor | CLASSPREFIX_ATTR_IO_RESOURCE_DESCRIPTOR |  |
| Driver Setup | CLASSPREFIX_ATTR_DRIVER_SETUP |  |

Parent topic:

Class Capability Groups

Related concepts:

- Class Driver APIs

<!--NI_TOPIC bundle=ivi-compliance-package path=instrument-specific-capabilities.html language=enus -->
## TOPIC 00019: Instrument Specific Capabilities

- bundle_id: `ivi-compliance-package`
- source_path: `instrument-specific-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/instrument-specific-capabilities.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to inherent IVI capabilities, base instrument capabilities, and extension groups, IVI specific drivers may export instrument specific functions and attributes. These features are usually device-specific functions that are not interchangeable with other devices. Only the specific driver i

### Instrument Specific Capabilities

In addition to *inherent IVI capabilities*, *base instrument capabilities*,
 and *extension groups*, IVI specific drivers may export instrument specific
 functions and attributes. These features are usually device-specific functions that are
 not interchangeable with other devices.

Only the specific driver implements the instrument specific capabilities. Therefore, if you want
 to use instrument specific capabilities in your test program, you must access the
 specific driver directly, instead of using a class driver. For information about the
 instrument specific features of a driver, refer to *IVI Instrument Specific
 Drivers*.

Your test program can access both the class driver and the specific driver during execution. In LabVIEW, the current instructions work. In LabWindows/CVI, you must use the GetSpecificDriver C Handle to get the specific driver session, then use the new handle to access the specific driver directly.

When you initialize an instrument through a class driver, you can specify default values for instrument specific attributes. MAX allows you to set the initial values of the instrument specific attributes to protect interchangeability.

Parent topic:

Class Capability Groups

Related concepts:

- Inherent IVI Capabilities
- Base Capabilities
- Extension Groups
- IVI Instrument Specific Drivers Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=interactive-simulation.html language=enus -->
## TOPIC 00020: Interactive Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `interactive-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/interactive-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: In all class drivers, the VXI plug&play-compliant VIs and functions have output parameters that return values or strings from the instrument. VXIplug&play-compliant VIs VXIplug&play-compliant Functions ClassPrefix Self-Test CLASSPREFIX_self-test ClassPrefix Revision Query CLASSPREFIX_revision_query

### Interactive Simulation

In all class drivers, the VXI plug&play-compliant VIs and functions have output parameters
 that return values or strings from the instrument.

| VXIplug&play-compliant VIs | VXIplug&play-compliant Functions |
| --- | --- |
| ClassPrefix Self-Test | CLASSPREFIX_self-test |
| ClassPrefix Revision Query | CLASSPREFIX_revision_query |
| ClassPrefix Error-Query | CLASSPREFIX_error_query |

During simulation, the simulation driver can create simulated data for the output parameters of
 these functions. This panel allows you to configure the simulation data to return from these
 functions.

You can access this view in the IviACPwr, IviCounter, IviDigitizer, IviDCPwr, IviDmm,
 IviPwrMeter, IviScope,or the IviSpecAn Simulator Setup dialog
 boxes. In this case, you see the Simulator Setup dialog box for IviScope. Scroll down to see a
 description of each control.

[IMAGE alt='image' src='GUID-79E1E84C-9EFA-4D81-A118-2C54A7036FA4-a5.gif']

#### IviScope Simulator Setup Dialog Box

The
 Simulator Setup dialog boxes for the different class drivers have common features. Each
 Simulator Setup dialog box has a View ring control in the upper left-hand corner. Use the View
 ring control to select a feature of the simulation driver to configure. All the dialog boxes
 have views to configure the simulation of the VXIplug&play functions and
 the simulation of function status codes. For classes that take measurements, such as IviDmm,
 IviScope, and IviDCPwr, the Simulator Setup dialog box also contains a Measurement Data
 Simulation view.

Because you can fully configure the simulation driver in the Simulator
 Setup dialog box at run time, you do not have to use MAX to specify attribute values in the
 Initial Settings tab of the Simulation Driver Sessions folder. If you do specify initial
 settings, however, the values that you specify appear as the initial values in the Simulator
 Setup dialog box each time you call ClassPrefix_init.

#### Self-Test

Use the Result Code and Message
 controls to specify the values you want the ClassPrefix Self-Test VI or
 ClassPrefix_self_test function of the driver to return in its output
 parameters.

#### Error-Query

Use the Error Code and Message
 controls to specify the values you want the ClassPrefix Error-Query VI or
 ClassPrefix_error_query function of the driver to return in its output
 parameters.

#### Revision Query

Use the Instrument Driver
 Revision and Firmware Revision controls to specify the values you want the ClassPrefix Revision
 Query VI orClassPrefix_revision_query function of the driver to return in its
 output parameters.

Parent topic:

IVI Class Driver Simulation Overview

Related information:

- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=interchangeability-checking-rules.html language=enus -->
## TOPIC 00021: Interchangeability Checking Rules

- bundle_id: `ivi-compliance-package`
- source_path: `interchangeability-checking-rules.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/interchangeability-checking-rules.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although interchangeability checking can be performed through the specific driver interface, interchangeability and thus interchangeability checking is only relevant when called through the class driver interface. The following rules govern interchangeability checking in IVI. An interchangeability c

### Interchangeability Checking Rules

Note

The following rules govern interchangeability checking in IVI.

1. An interchangeability check occurs when you invoke a driver operation that depends on the
 current state of the instrument. For example, IviDmm compliant drivers perform
 interchangeability checking when your program calls any of the functions shown in
 the following table. Name in LabWindows/CVI
 Name in LabVIEW
 Prefix_Initiate
 Prefix Initiate
 Prefix_Read
 Prefix Read
 Prefix_ReadMultiPoint
 Prefix Read MultiPoint
2. The driver performs interchangeability checking on a capability group basis. When you enable interchangeability checking, the driver always performs interchangeability checking on the base capabilities group.
3. The driver performs interchangeability checking on all extension groups for which you have set any of the attributes. If your program has never set any attributes of an extension group, the driver does not perform interchangeability checking on that group.

In general, a driver generates an interchangeability warning when it encounters one of the
 following conditions:

- Unspecified State An attribute that is in a state that you did not specify. An attribute ends up in an unspecified state if the attribute is not configured by your program or if your program configures the attribute but the value becomes invalid as a result of your program configuring a different attribute.

If an attribute is in a state that you did not specify, then the value of the attribute is unknown. The value of the attribute, and therefore the behavior of the instrument, is likely to be different when you run the program with a different instrument.
- Instrument Specific Value You set a classdefined attribute to an instrument specific value. Many class attribute values represent a set of discrete settings. For these attributes, the class specifications defines the possible values that you can assign to the attribute. Specific drivers can define additional, instrument specific values for the attribute. When your program sets an attribute to an instrument specific value, your program is likely to behave differently when you run it with different instruments.

For example, the attribute that configures the measurement function can have both class values and instrument specific values. The class defines values for common measurement functions such as AC volts, DC volts, AC current, DC current, and others. Specific drivers can define instrument specific values for the attribute. The constant values that one specific driver uses can overlap with the constant values other specific drivers use. One specific driver might define an instrument specific measurement function and another specific driver might use the same value to define an entirely different measurement function. Therefore, using an instrument specific value in your program can result in different measurement results depending on which instrument you use.
- ReadOnly Attribute You configure the value of an attribute that the class defines as readonly. In a few cases, the class defines read-only attributes that specific drivers might implement as read/write.

The attributes that return the aperture time in the IviDmm class are examples of this interchangeability issue. With some DMMs, you can set the aperture time as well as read it. The specific drivers for these DMMs might implement the attributes for the aperture time as read/write. Most other class-compliant drivers implement the attribute as readonly. Therefore, if your program sets an attribute that a class defines as readonly, your program may not work with other instruments.
- Value Not Configured The driver encounters an error when it tries to
 apply a value to an extension attribute that your program never configures.
 Disabling Unused Extensions describes how the driver sets the
 attributes of extension groups that do not have specified valuesit sets the
 attributes to an interchangeable state. The driver does this to make your program
 behave the same regardless of whether the instruments you use implement the
 extension group. Other instruments that implement the extension group might not
 support the value to which the driver attempts to set the attribute. In this case,
 the driver queues an interchangeability warning instead of returning an error from
 the function. An example of this behavior is the attribute that configures the
 interpolation method in the IviScope class. If your program does not set the value
 of this attribute and the specific driver implements the attribute, the driver
 attempts to set the interpolation method to Sin(x)/x. However, some oscilloscopes
 always interpolate data points. For these cases, the driver generates an
 interchangeability warning to indicate that the attribute that controls the
 interpolation method is not in an interchangeable state. Each IVI specific driver
 defines exceptions to the interchangeability checking rules and defines which
 functions perform interchangeability checking. Refer to *IVI Class Driver
 Help* for more information regarding the interchangeability checking
 rules for a particular class.

Parent topic:

Class Driver Simulation

Related concepts:

- Disabling Unused Extensions

Related information:

- IVI Class Driver Help

<!--NI_TOPIC bundle=ivi-compliance-package path=interchangeability-checking.html language=enus -->
## TOPIC 00022: Interchangeability Checking

- bundle_id: `ivi-compliance-package`
- source_path: `interchangeability-checking.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/interchangeability-checking.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: IVI drivers have a feature called interchangeability checking. Interchangeablility checking verifies that your program produces the same behavior when used with a different instrument. Enable interchangeability checking by completing one of the following procedures: Refer to Configuring Your System

### Interchangeability Checking

IVI drivers have a feature called interchangeability checking. Interchangeablility checking
 verifies that your program produces the same behavior when used with a different
 instrument.

Enable interchangeability checking by completing one of the following procedures:

- Refer to Configuring Your System In MAX to enable interchangeability checking in
 MAX.
- For information on configuring your system in MAX, open MAX and navigate to
 Help » Help Topics
- Set the value of the interchangeability checking attribute to VI_TRUE in your
 program.
- Set the interchangeability checking attribute to VI_TRUE in the option string
 parameter of the InitWithOptions function or Initialize With Options VI.

When interchangeability checking is enabled, the driver queues interchangeability warnings when
 it encounters instrument configurations that might not produce the same behavior when you use
 a different instrument. Use *Analyzing Your Program with NI I/O Trace* to view
 these warnings or call the Get Next Interchange Warning function.

Parent topic:

Class Driver Simulation

Related concepts:

- Analyzing Your Program with NI I/O Trace

<!--NI_TOPIC bundle=ivi-compliance-package path=interchangeability.html language=enus -->
## TOPIC 00023: Interchangeability

- bundle_id: `ivi-compliance-package`
- source_path: `interchangeability.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/interchangeability.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Interchangeability of IVI class drivers depends on the fundamental interchangeability of the hardware that you are using. Your test system requirements still dictate your choice of particular instruments. For example, if your test system requires DMM measurements with 8½ digits of precision, you mus

### Interchangeability

Interchangeability of IVI class drivers depends on the fundamental interchangeability of the
 hardware that you are using. Your test system requirements still dictate your choice of
 particular instruments. For example, if your test system requires DMM measurements with
 8½ digits of precision, you must use a DMM with 8½ digits of precision. You cannot
 replace an 8½ digit DMM with a 5½ digit DMM in your test system, unless you require only
 5½ digits of precision, regardless of the software architecture. IVI class drivers
 implement a standard architecture for swapping instruments that are capable of taking
 the required measurements for your test system.

Parent topic:

IVI Driver Help Introduction

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-class-driver-simulation-overview.html language=enus -->
## TOPIC 00024: IVI Class Driver Simulation Overview

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-class-driver-simulation-overview.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-class-driver-simulation-overview.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI class drivers implement simulation features by using simulation drivers. ICP installs a simulation driver for each IVI class driver. Each simulation driver plugs in to the corresponding class driver and performs flexible output data simulation.The following table lists the simulation driver

### IVI Class Driver Simulation Overview

The IVI class drivers implement simulation features by using simulation drivers. ICP installs a
 simulation driver for each IVI class driver. Each simulation driver plugs in to the
 corresponding class driver and performs flexible output data simulation.

The following table lists the simulation driver files that ICP installs.

| IVI Class Simulation Drivers | Simulation Driver Files |
| --- | --- |
| IviScope | nisScope.dll, nisScope.c, nisScope.h, nisScopeu.uir, nisScopeu.h |
| IviDmm | nisDmm.dll, nisDmm.c, nisDmm.h, nisDmmu.uir, nisDmmu.h |
| IviFgen | nisFgen.dll, nisFgen.c, nisFgen.h |
| IviSwtch | nisSwtch.dll, nisSwtch.c, nisSwtch.h |
| IviACPwr | nisACPwr.dll, nisACPwr.c, nisACPwr.h, nisACPwru.uir, nisACPwrUir.c, nisACPwru.h |
| IviDCPwr | nisDCPwr.dll, nisDCPwr.c, nisDCPwr.h, nisDCPwru.uir, nisDCPwrUir.c, nisDCPwru.h |
| IviPwrMeter | nisPwrMeter.dll, nisPwrMeter.c, nisPwrMeter.h, nisPwrMeteru.uir, nisPwrMeteru.h |
| IviRFSigGen | nisRFSigGen.dll, nisRFSigGen.c, nisRFSigGen.h |
| IviSpecAn | nisSpecAn.dll, nisSpecAn.c, nisSpecAn.h, nisSpecAnu.uir, nisSpecAnu.h |
| IviCounter | nisCounter.dll, nisCounter.c, nisCounter.h, nisCounteru.uir, nisCounteru.h |
| IviDigitizer | nisDigitizer.dll, nisDigitizer.c, nisDigitizer.h, nisDigitizeru.uir, nisDigiziteru.h |
| IviDownconverter | nisDownconverter.dll, nisDownconverter.c, nisDownconverter.h |
| IviUpconverter | nisUpconverter.dll, nisUpconverter.c, nisUpconverter.h |
| Common Files | nisimu.uir, nisimu.h |

ICP distributes the simulation drivers as .dll files so that you can use them
 immediately. It also includes C source files for the simulation drivers, so you can
 modify the drivers to meet your specific simulation requirements. The ICP installation
 program places the simulation driver .dll files in the
 <IVI Standard Root Dir
 >\bin directory. The installation program places the
 .c, .h, and .uir files in the
 <All Users>\Documents\National
 Instruments\CVI\Samples\IVI\ClassSim directory.

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-class-drivers-overview.html language=enus -->
## TOPIC 00025: IVI Class Drivers Overview

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-class-drivers-overview.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-class-drivers-overview.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: IVI class drivers implement functions and attributes for controlling an instrument within a specified class, as defined by the IVI Foundation. Each IVI class driver consists of generic code that can call IVI instrument specific drivers. Through configuration you can switch between various specific d

### IVI Class Drivers Overview

IVI class drivers implement functions and attributes for controlling an instrument within a specified class, as defined by the IVI Foundation.

Each IVI class driver consists of generic code that can call IVI instrument specific drivers.
 Through configuration you can switch between various specific drivers, achieving
 interchangeability. By using IVI class drivers in your test program, you can change
 hardware without changing test code or recompiling your application.

The following figure shows how a class driver redirects function calls from a test program to the
 correct specific driver.

[IMAGE alt='image' src='GUID-72AE49AC-F95E-4193-BC47-C4477440C16C-a5.gif']

The IVI Foundation manages the definition of the instrument classes. The IVI Foundation’s charter
 is to define flexible programming interfaces for instrument classes that meet the needs
 of test system developers. The IVI Foundation has created specifications for common
 instrument classes. The IVI Foundation specifications define a standard Application
 Programming Interface (API) for each instrument class.

The NI IVI class drivers conform to the IVI Foundation specifications. For example, the
 oscilloscope class contains a collection of attributes that are common to all
 oscilloscopes, such as vertical range, offset, timebase, trigger mode, and so on. The
 class also contains functions that set these attributes or retrieve data from the
 instrument, such as ConfigureChannel, ConfigureAcquisitionRecord, ReadWaveform, and so
 on. IVI class specifications give a standard definition for each of these functions and
 attributes for an oscilloscope. Programmers use these specifications to write test
 programs that work with any oscilloscope.

Parent topic:

IVI Driver Help Introduction

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-class-drivers.html language=enus -->
## TOPIC 00026: IVI Class Drivers

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-class-drivers.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-class-drivers.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI Compliance Package supports several IVI driver classes. You can develop hardware independent test programs with these driver classes. The setup program installs the files you need to use the class drivers with LabWindows/CVI and LabVIEW. Refer to the following help files for more information

### IVI Class Drivers

Note

- LabWindows/CVI — IVI Class Driver Help for
 LabWindows/CVI
- LabVIEW — IVI Class Driver Help for
 LabVIEW

#### LabWindows/CVI

For LabWindows/CVI, an IVI class driver consists of the following files:

- The class driver program, which consists of a .dll file and import library (.lib) files for various compilers.

- The class driver includes file (.h), which contains the function declarations and constant definitions for the class.

- The class driver function panel file (.fp), which defines the function tree, the function panels, and the help text.

- The .sub file, which documents attributes and their possible values.

- A Windows HTML help file (.chm), which contains documentation for the LabWindows/CVI class driver.

#### LabVIEW

For LabVIEW, an IVI class driver consists of the following files:

- The class driver VIs, which are in a .llb file. The VIs link to a .dll
 file.

- The .rc file, which documents properties and their possible values.

- A set of .mnu files, which documents the hierarchy of VIs for the class
 driver.

- A Windows HTML help file (.chm), which contains documentation for the LabVIEW
 class driver.

Refer to *IVI Class Drivers Overview* for more information about class
 drivers.

Parent topic:

IVI Compliance Package Overview

Related information:

- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-driver-help-introduction.html language=enus -->
## TOPIC 00027: IVI Driver Help Introduction

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-driver-help-introduction.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-driver-help-introduction.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The topics in this book are intended for both LabWindows/CVI and LabVIEW users. These topics describe how to develop hardware independent test programs with IVI (Interchangeable Virtual Instruments) instrument drivers.These topics also give an overview of IVI instrument drivers and the IVI system ar

### IVI Driver Help Introduction

The topics in this book are intended for both LabWindows/CVI and LabVIEW users. These topics
 describe how to develop hardware independent test programs with
 IVI (Interchangeable Virtual Instruments) instrument
 drivers.

These topics also give an overview of IVI instrument drivers and the IVI system architecture, so
 that you can configure your system and develop test programs that are independent of
 your hardware. Follow the guidelines in these topics when you develop, debug and deploy
 test programs that use IVI instrument drivers.

- [IVI Instrument Specific Drivers Overview](ivi-instrument-specific-drivers-overview.html)
- [IVI Class Drivers Overview](ivi-class-drivers-overview.html)
- [Interchangeability](interchangeability.html)
- [Main Components of an IVI System](main-components-of-an-ivi-system.html)
- [Class Driver APIs](class-driver-apis.html)
- [Class Capability Groups](class-capability-groups.html)
- [Class Driver Simulation](class-driver-simulation.html)

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-instrument-specific-drivers-overview.html language=enus -->
## TOPIC 00028: IVI Instrument Specific Drivers Overview

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-instrument-specific-drivers-overview.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-instrument-specific-drivers-overview.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: IVI instrument specific drivers contain the information to control a particular instrument model, including the command strings, parsing code, and valid ranges of each setting for that particular instrument. IVI instrument drivers apply an attribute-based approach to instrument control to deliver be

### IVI Instrument Specific Drivers Overview

IVI instrument specific drivers contain the information to control a particular instrument model,
 including the command strings, parsing code, and valid ranges of each setting for that
 particular instrument. IVI instrument drivers apply an attribute-based approach to
 instrument control to deliver better run-time performance and more flexible instrument
 driver operation.

In the remainder of this help file the term specific driver refers to an IVI instrument specific
 driver A specific driver gives you the following benefits over a traditional instrument
 driver:

- State Caching State caching prevents the specific driver from sending 
redundant commands to the instrument. If you try to set an attribute to a value 
that is already configured, the specific driver skips sending the command. You 
can disable state caching.
- Range Checking Range checking verifies that a value you specify for an 
attribute is within the valid range for the instrument, without performing 
costly I/O or causing an instrument error. You can disable this feature for 
faster execution speed.
- Status Query The status query feature automatically checks the status of the instrument after each operation. You can disable this feature for faster execution speed.
- Simple Simulation You can develop application code for an instrument driver 
even when the instrument is not available. In simulation mode, the instrument 
driver generates simulated data for output parameters.
- Multithread Safety You can use the IVI instrument driver in multithreaded
 applications. Multiple execution threads can use the same IVI instrument session
 without interfering with each other.

Parent topic:

IVI Driver Help Introduction

<!--NI_TOPIC bundle=ivi-compliance-package path=ivi-shared-components.html language=enus -->
## TOPIC 00029: IVI Shared Components

- bundle_id: `ivi-compliance-package`
- source_path: `ivi-shared-components.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ivi-shared-components.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI Shared Components are owned and distributed by the IVI Foundation. These components make the underlying structure of an IVI-compliant system. Since IVI Compliance Package components are designed to work with the IVI Shared Components, the IVI Shared Components are installed as part of the IV

### IVI Shared Components

The IVI Shared Components are owned and distributed by the IVI Foundation. These components make
 the underlying structure of an IVI-compliant system. Since IVI Compliance Package
 components are designed to work with the IVI Shared Components, the IVI Shared
 Components are installed as part of the IVI Compliance Package.

The Configuration Server included in the IVI Shared Components provides an API for accessing
 instrument driver data. Various IVI products have been redesigned to work with the
 Configuration Server instead of the previous way of using the ivi.ini
 file.

Parent topic:

IVI Compliance Package Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=main-components-of-an-ivi-system.html language=enus -->
## TOPIC 00030: Main Components of an IVI System

- bundle_id: `ivi-compliance-package`
- source_path: `main-components-of-an-ivi-system.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/main-components-of-an-ivi-system.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Main Components of an IVI SystemThe following figure shows the components of an IVI system. In general, to implement an automated test system, you develop a program that controls instruments. For each instrument model that you access, you use an IVI specific driver. The specific driver contains all

### Main Components of an IVI System

#### Main Components of an IVI System

The
 following figure shows the components of an IVI system. In general, to implement an
 automated test system, you develop a program that controls instruments. For each
 instrument model that you access, you use an IVI specific driver. The specific
 driver contains all the information to control a particular instrument model.

[IMAGE alt='image' src='GUID-369C86D6-1877-4D69-A831-F86D129C6AAD-a5.gif']

#### IVI System Architecture

Your test
 program communicates with the specific driver in one of two ways: directly or
 through an IVI class driver.

#### Directly

Your test program can call the specific driver directly, similar to the way you use traditional instrument drivers. With this approach, you gain most of the benefits of IVI instrument drivers, including state caching, range checking, status query checking, simple simulation, and multithread safety. All functions and attributes that the specific driver exports begin with a prefix that uniquely identifies the specific driver. Because the specific driver's prefix is unique, interchangeability is not available through direct communication, and you must modify and recompile your test program when you want to use a different specific driver.

#### Through an IVI Class Driver

Your test program can access a specific driver indirectly through an IVI class
 driver. With IVI class drivers, you can develop test programs that are independent
 of specific hardware and interchange instruments without modifying or recompiling
 your test program. In addition to interchangeability, IVI class drivers deliver
 other benefits such as class simulation, I/O tracing, and interchangeability
 checking. For information about a particular IVI class driver, refer to *IVI
 Class Driver Help*.

When you use an IVI class driver, you begin by calling its initialize function. This
 function uses the logical name parameter to initialize the instrument and driver
 software. The function then returns an instrument handle that you use with all other
 IVI class driver function calls. You create and configure logical names in MAX.

To change the instrument that your program uses, edit the logical name in MAX to
 identify the new specific driver and physical instrument. You do not have to change
 or recompile your program. Therefore, the class driver allows you to develop
 hardware-independent test programs that do not require modification when you use a
 different instrument. For a complete description of the IVI configuration features
 in MAX, refer to *Measurement & Automation Explorer Help for
 IVI*.

Parent topic:

IVI Driver Help Introduction

Related concepts:

- Using IVI Class Drivers

<!--NI_TOPIC bundle=ivi-compliance-package path=max.html language=enus -->
## TOPIC 00031: MAX

- bundle_id: `ivi-compliance-package`
- source_path: `max.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/max.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Measurement & Automation Explorer (MAX) configuration utility to configure your instrument-independent test system. With MAX, you create and configure IVI logical names. In your program, you pass logical names to one of the class driver initialize functions to identify the instruments (also know

### MAX

Note

ni.com/idnet

Parent topic:

IVI Compliance Package Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=measurement-data-simulation.html language=enus -->
## TOPIC 00032: Measurement Data Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `measurement-data-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/measurement-data-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The simulation drivers perform measurement data simulation. For example, when you use the IviScope class driver with simulation enabled, you can configure the waveform that the IviScope_ReadWaveform and IviScope_FetchWaveform functions return.The following figure shows the Measurement Data Simulatio

### Measurement Data Simulation

The simulation drivers perform measurement data simulation. For example, when you use the
 IviScope class driver with simulation enabled, you can configure the waveform that the
 IviScope_ReadWaveform and IviScope_FetchWaveform functions
 return.

The following figure shows the Measurement Data Simulation view for the IviScope simulation
 driver.

[IMAGE alt='image' src='GUID-0B45F00A-6C08-453A-B9EB-FE2A64D83288-a5.gif']

#### IviScope Measurement Data Simulation View

The Measurement Data Simulation view for each simulation driver has an Always Prompt for Output Data Simulation checkbox control. Use this control to specify whether you want the simulation driver to display the Measurement Data Simulation panel each time your program takes a measurement. If you enable the Always Prompt for Output Data Simulation control, you can configure the data separately that the simulation driver generates for each measurement. When you disable the control, you configure the output data simulation once for the instrument session when you call an initialization function.

You can configure the measurement data simulation in MAX on the Initial Settings 
tab of IVI Drivers»Advanced»Simulation Driver Sessions»nisIviClass 
or in the simulation interactive panels.

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=minimize-the-use-of-extension-capability-grou.html language=enus -->
## TOPIC 00033: Minimize the Use of Extension Capability Groups

- bundle_id: `ivi-compliance-package`
- source_path: `minimize-the-use-of-extension-capability-grou.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/minimize-the-use-of-extension-capability-grou.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use only the extension capability groups that your test program requires. Minimizing the number of extension capability groups you access for an IVI session maximizes the number of instruments that you can use with your application.The class drivers divide the capabilities of an instrument class int

### Minimize the Use of Extension Capability Groups

Use only the extension capability groups that your test program requires. Minimizing the number
 of extension capability groups you access for an IVI session maximizes the number of
 instruments that you can use with your application.

The class drivers divide the capabilities of an instrument class into *capability
 groups*. The capability groups contain functions and attributes that you use
 to access the features of that capability group. Each class driver defines a *base
 capability group*. A specific driver must implement the base capabilities
 group to be compliant with the class. Therefore, you can always use the base
 capabilities group in your program.

The other capability groups are *extension capability groups*. Extension capability
 groups represent the less common capabilities of the instrument class. Specific drivers
 are not required to implement the extension capability groups. Not all specific drivers
 implement the same set of extension capability groups. Each time you use a new extension
 capability group in your program, you limit the number of instruments that you can use
 in your application.

Parent topic:

Developing an Instrument Independent Application

Related concepts:

- Class Capability Groups
- Base Capabilities
- Extension Groups

<!--NI_TOPIC bundle=ivi-compliance-package path=modifying-the-simulation-driver.html language=enus -->
## TOPIC 00034: Modifying the Simulation Driver

- bundle_id: `ivi-compliance-package`
- source_path: `modifying-the-simulation-driver.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/modifying-the-simulation-driver.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI class simulation drivers provide general purpose simulation features. However, you might require more application-specific simulation capabilities. For that reason, the IVI Compliance Package includes C source code for the simulation drivers. You can customize the data simulation algorithms

### Modifying the Simulation Driver

The IVI class simulation drivers provide general purpose simulation features. However, you might
 require more application-specific simulation capabilities. For that reason, the IVI
 Compliance Package includes C source code for the simulation drivers. You can customize
 the data simulation algorithms for your specific requirements. Because simulation
 drivers work with the class drivers, you can reuse the simulation code you develop with
 different specific instruments.

Note

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=new-features-and-changes.html language=enus -->
## TOPIC 00035: IVI Compliance Package New Features and Changes

- bundle_id: `ivi-compliance-package`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/new-features-and-changes.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of IVI Compliance Package. Discover what is new in the latest releases of IVI Compliance Package.If you cannot find new features and changes for your version, it might not include user-facing updates. Howeve

### IVI Compliance Package
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of IVI Compliance Package.

IVI Compliance Package

Note

Release Notes

Related information:

- Software and Driver Downloads

#### IVI Compliance Package
 2026 Q2 Changes

IVI Compliance Package 2026 Q2 includes bug fixes.

##### New
 Features

This version of IVI Compliance Package adds support
 for the following features:

- Bug fixes and improvements.

<!--NI_TOPIC bundle=ivi-compliance-package path=ni-i-o-trace.html language=enus -->
## TOPIC 00036: NI I/O Trace

- bundle_id: `ivi-compliance-package`
- source_path: `ni-i-o-trace.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/ni-i-o-trace.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI I/O Trace monitors Windows applications that use NI drivers. NI I/O Trace can monitor, record, and display calls made to IVI class drivers. Use NI I/O Trace to quickly locate and analyze any erroneous calls that your application makes to the IVI class drivers.

### NI I/O Trace

NI I/O Trace monitors Windows applications that use NI drivers. NI I/O Trace can monitor, record,
 and display calls made to IVI class drivers. Use NI I/O Trace to quickly locate and analyze
 any erroneous calls that your application makes to the IVI class drivers.

Parent topic:

Class Driver Simulation

<!--NI_TOPIC bundle=ivi-compliance-package path=non-interactive-simulation.html language=enus -->
## TOPIC 00037: Non-Interactive Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `non-interactive-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/non-interactive-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you disable interactive simulation, you can configure simulation only in MAX. After you initialize your driver by calling an initialization function, you cannot alter the configuration of the simulation driver. Non-interactive simulation is useful when you want to prevent the interactive panels

### Non-Interactive Simulation

When you disable interactive simulation, you can configure simulation only in MAX. After you
 initialize your driver by calling an initialization function, you cannot alter the
 configuration of the simulation driver. Non-interactive simulation is useful when you
 want to prevent the interactive panels from interrupting your test program.

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=overview.html language=enus -->
## TOPIC 00038: IVI Compliance Package Overview

- bundle_id: `ivi-compliance-package`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/overview.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI IVI Compliance Package is a software package that contains IVI class drivers and the support libraries necessary for the development and use of applications that leverage IVI instrument interchangeability. The IVI Compliance Package is also based on and is compliant with the latest version of

### IVI Compliance Package
 Overview

The NI IVI Compliance Package is a software package that contains IVI class drivers and
 the support libraries necessary for the development and use of applications that
 leverage IVI instrument interchangeability.

The IVI Compliance Package is also based on and is compliant with the latest version of
 the instrument programming specifications defined by the IVI Foundation. The IVI class
 drivers in the ICP are used with IVI specific drivers. You can either download IVI
 specific drivers from ni.com/idnet or create them yourself.

- [What the Setup Program Installs](what-the-setup-program-installs.html)
- [IVI Class Drivers](ivi-class-drivers.html)
- [MAX](max.html)
- [IVI Shared Components](ivi-shared-components.html)

<!--NI_TOPIC bundle=ivi-compliance-package path=status-code-simulation.html language=enus -->
## TOPIC 00039: Status Code Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `status-code-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/status-code-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: You use the dialog box shown in the following figure to configure the status code for a simulation. You can access this view in the IviCounter, IviDigitizer, IviDCPwr, IviDmm, IviPwrMeter, IviScope, or IviSpecAn Simulator Setup dialog boxes. In this case, you see the Simulator Setup dialog box for I

### Status Code Simulation

You use the dialog box shown in the following figure to configure the status code for a
 simulation. You can access this view in the IviCounter, IviDigitizer, IviDCPwr,
 IviDmm, IviPwrMeter, IviScope, or IviSpecAn Simulator
 Setup dialog boxes. In this case, you see the Simulator Setup dialog box
 for IviScope.

To configure the status code simulation, select Status Code Simulation from the View ring control.

Scroll down to see a description of each control.

[IMAGE alt='image' src='GUID-D78B9CB3-C328-4171-9A59-FBAAD57E3118-a5.gif']

#### Status Code Simulation View

The Status
 Code Simulation view is the same for all simulation drivers. The Status Code
 Simulation view has the following controls:

- Simulate Status Codes This control lists all of the class
 driver functions that the selected instrument specific driver supports. The list
 also indicates each function's associated simulation status code in both macro
 name form and in hexadecimal value form. You use the Status Code
 Macro and Custom Status Code controls to
 modify simulation status codes. Setting this control has the same effect as
 configuring the PREFIX _ATTR_SIMULATE_STATUS_CODES attribute
 on the Initial Settings tab of IVI Drivers»Advanced»Simulation Driver
 Sessions»nisIviClass in MAX or in the simulation interactive
 panels.
- Status Code Macro This control allows you to change the
 simulation status code of the currently selected function. Setting this control
 to the custom status code option sets the value you placed in the
 Custom Status Code control as the function's
 simulated status code. If you select Custom Status Code, you can configure a
 custom status code in the Custom Status Code control.
- Custom Status Code This control lets you specify a custom
 status code to simulate for a particular function.
- Reset all to VI_SUCCESS This control resets all of the
 class driver functions' simulation status codes to VI_SUCCESS (0).

Configuring simulated status codes with this dialog box has the same effect as
 configuring the corresponding simulated status code attributes on the Initial
 Settings tab of IVI Drivers»Advanced»Simulation Driver
 Sessions»nisIviClass in MAX or in the simulation interactive
 panels.

Parent topic:

IVI Class Driver Simulation Overview

Related information:

- IVI Class Driver Help for
 LabWindows/CVI
- IVI Class Driver Help for
 LabVIEW

<!--NI_TOPIC bundle=ivi-compliance-package path=testing-the-new-driver-in-simulation-mode.html language=enus -->
## TOPIC 00040: Testing the New Driver in Simulation Mode

- bundle_id: `ivi-compliance-package`
- source_path: `testing-the-new-driver-in-simulation-mode.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/testing-the-new-driver-in-simulation-mode.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you do not have a reference program, you can verify a replacement candidate by trying to run your program with the new instrument. If you cannot make connections to the physical instrument, you can enable simulation. Often the analysis routines in your test program depend on the data that an inst

### Testing the New Driver in Simulation Mode

If you do not have a reference program, you can verify a replacement candidate by trying to run your program with the new instrument. If you cannot make connections to the physical instrument, you can *enable simulation*.

Often the analysis routines in your test program depend on the data that an instrument returns.
 If the instrument does not return valid data, the program returns an error and does not
 fully execute all the statements that control the instrument. If you enable simulation,
 you can use the class simulation drivers to create simulated data so that you can fully
 execute your test program.

If you can execute your program using the new instrument, then you can probably replace your
 existing instrument with the new one.

Parent topic:

Verifying Instrument Replacement Candidates

Related information:

- Enabling Instrument Simulation

<!--NI_TOPIC bundle=ivi-compliance-package path=use-max-to-configure-instrument-specific-attr.html language=enus -->
## TOPIC 00041: Use MAX to Configure Instrument Specific Attributes

- bundle_id: `ivi-compliance-package`
- source_path: `use-max-to-configure-instrument-specific-attr.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/use-max-to-configure-instrument-specific-attr.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to NI IVI Driver Help»Configuring Your System Using MAX for more information about using Initial Settings to configure instrument specific attributes.

### Use MAX to Configure Instrument Specific Attributes

Refer to NI IVI Driver Help»Configuring Your System Using MAX for more
 information about using Initial Settings to configure instrument specific
 attributes.

Parent topic:

Developing an Instrument Independent Application

<!--NI_TOPIC bundle=ivi-compliance-package path=user-interface-requirements.html language=enus -->
## TOPIC 00042: User-Interface Requirements

- bundle_id: `ivi-compliance-package`
- source_path: `user-interface-requirements.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/user-interface-requirements.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The interactive capabilities of simulation drivers place additional requirements on your system. The simulation driver .dll files require the LabWindows/CVI RunTime Engine. The IVI Compliance Package installation program installs the LabWindows/CVI RunTime Engine.If you want to deploy a simulation

### User-Interface Requirements

The interactive capabilities of simulation drivers place additional requirements on your system.
 The simulation driver .dll files require the LabWindows/CVI RunTime Engine. The IVI
 Compliance Package installation program installs the LabWindows/CVI RunTime Engine.

If you want to deploy a simulation driver on a system that does not have the LabWindows/CVI
 RunTime Engine, you must modify and recompile the simulation driver source code. This
 section describes the modifications you must make for LabWindows/CVI 5.0 or later.

LabWindows/CVI 5.0.xTo modify and recompile the
 simulation driver using the LabWindows/CVI 5.0.x compiler, complete
 the following steps:

1. Edit the .c file of the simulation driver. The .c file for each simulation driver contains the
 following statements: #ifndef ALLOW_INTERACTIVE_SIMULATION 
 #define ALLOW_INTERACTIVE_SIMULATION 
 To prevent your program from trying to invoke the LabWindows/CVI RunTime Engine,
 change the ALLOW_INTERACTIVE_SIMULATION macro definition from 1
 to 0 so that the compiler does not process any of the user interface
 code.
2. Enable the Instrument Driver Support Only command in the Build menu of the Project window. When you enable Instrument Driver Support Only, your project does not link to the LabWindows CVI RunTime Engine. To enable Instrument Driver Support Only, select Build»Instrument Driver Support Only .
3. Select Build»Create Dynamic Link Library in the Project window to compile the simulation driver .dll file. The Create Dynamic Link Library dialog box appears. Be sure to export the symbols from the .h file of the simulation driver as follows:
  1. Click Change to display the DLL Export Options dialog.
  2. Select Include File Symbols from the Export What control.
  3. Select the .h file for the simulation driver in the Which Project Include Files
 list control.
4. Click OK to create the DLL.

LabWindows/CVI 5.5To modify and recompile the simulation driver using the LabWindows/CVI 5.5 compiler, complete the following steps:

1. Edit the .c file of the simulation driver. The .c file for each simulation driver contains the
 following statements: #ifndef ALLOW_INTERACTIVE_SIMULATION 
 #define ALLOW_INTERACTIVE_SIMULATION 
 To prevent your program from trying to invoke the LabWindows/CVI RunTime Engine,
 change the ALLOW_INTERACTIVE_SIMULATION macro definition from 1
 to 0 so that the compiler does not process any of the user interface
 code.
2. Select Build»Target Settings in the Project window. The Target Settings dialog appears. Enable Instrument Driver Support Only if you do not want to link to the LabWindows/CVI Run-Time Engine. Be sure to export the symbols from the .h file of the simulation driver by completing the following steps:
  1. Click Change in the export section to display the DLL Export Options dialog box.
  2. Select Include File Symbols from the Export What control.
  3. Select the .h file for the simulation driver in the Which Project Include Files
 list control.
3. Select Build»Create Release Dynamic Link Library in the Project window to
 compile the simulation .dll file.

LabWindows/CVI 6.0 and 7.0To modify and recompile the simulation driver
 using the LabWindows/CVI 6.0 or 7.0 compiler, complete the following steps:

1. Edit the .c file of the simulation driver. The .c file for each simulation
 driver contains the following statements: #ifndef
 ALLOW_INTERACTIVE_SIMULATION 
 #define ALLOW_INTERACTIVE_SIMULATION 
 To prevent your program from trying to invoke the LabWindows/CVI RunTime Engine,
 change the ALLOW_INTERACTIVE_SIMULATION macro definition from 1 to 0 so that the
 compiler does not process any of the user interface code.
2. Select Build»Target Settings in the Project window. The Target Settings dialog appears. Select Instrument Driver Only from the Runtime Support control. Be sure to export the symbols from the .h file of the simulation driver by completing the following steps:
  1. Click Change in the export section to display the DLL Export Options dialog box.
  2. Select Include File Symbols from the Export What control.
  3. Select the .h file for the simulation driver in the Which Project Include Files list control.
3. Select Build»Create Release Dynamic Link Library in the Project window to compile the simulation .dll file.

After you compile the simulation driver, the resulting .dll does not require the LabWindows/CVI
 RunTime Engine, but you cannot use the interactive simulation panels. If you attempt to
 enable interactive simulation without the LabWindows/CVI RunTime Engine, the simulation
 driver returns an error.

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=user-manual-welcome.html language=enus -->
## TOPIC 00043: IVI Compliance Package User Manual

- bundle_id: `ivi-compliance-package`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/user-manual-welcome.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IVI Compliance Package User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### IVI Compliance Package
 User Manual

The IVI Compliance Package User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=ivi-compliance-package path=using-class-drivers-in-labview.html language=enus -->
## TOPIC 00044: Using Class Drivers in LabVIEW

- bundle_id: `ivi-compliance-package`
- source_path: `using-class-drivers-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-class-drivers-in-labview.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use IVI class drivers in LabVIEW the same way that you use other LabVIEW instrument drivers. The IVI class drivers are in the IVI Class Drivers palette. To access the IVI Class Drivers palette, select Functions»Instrument I/O»IVI Class Drivers, as shown in the following figure. Each IVI class driver

### Using Class Drivers in LabVIEW

Use IVI class drivers in LabVIEW the same way that you use other LabVIEW instrument drivers. The
 IVI class drivers are in the IVI Class Drivers palette. To access the IVI Class Drivers
 palette, select Functions»Instrument I/O»IVI Class Drivers, as
 shown in the following figure.

[IMAGE alt='image' src='GUID-829EDBB0-B460-407D-B682-8F7335183392-a5.gif']

Each IVI class driver has a subpalette that contains all the VIs for the corresponding class
 driver. The LabVIEW class drivers have VIs that perform the same operations as the
 LabWindows/CVI class drivers. To access a VI for a particular class driver, select the
 subpalette that corresponds to the class driver in the IVI Class Drivers palette.

The following figure shows a code example that uses the IviDmm class driver to configure a DMM
 and take a measurement.

[IMAGE alt='image' src='GUID-577FCC13-6F33-4BAB-BAD8-394D45567726-a5.gif']

The following figure shows how you can use the property node to access individual instrument
 driver attributes. After LabVIEW calls the IviDmm Initialize VI, it uses the Property
 Node to set values for the Function, Trigger Source, and Range. Expand the Visa
 Functions book in the LabVIEW Help or refer to the NI-VISA Programmer Reference Manual
 for more information on VISA properties and attributes. Refer to the LabVIEW Help for
 more information about how to use the property node.

[IMAGE alt='image' src='GUID-F3F15AD6-B2A4-47BF-A75B-491BD410D681-a5.gif']

Parent topic:

Using IVI Class Drivers

<!--NI_TOPIC bundle=ivi-compliance-package path=using-class-drivers-in-labwindows-cvi.html language=enus -->
## TOPIC 00045: Using Class Drivers in LabWindows/CVI

- bundle_id: `ivi-compliance-package`
- source_path: `using-class-drivers-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-class-drivers-in-labwindows-cvi.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: You use the IVI class drivers in the LabWindows/CVI the same way that you use other LabWindows/CVI instrument drivers. You can load and unload class drivers manually using the Instrument menu. To load a class driver, complete the following steps: Select Instrument»Load. In the Load Instrument dialog

### Using Class Drivers in LabWindows/CVI

You use the IVI class drivers in the LabWindows/CVI the same way that you use other
 LabWindows/CVI instrument drivers. You can load and unload class drivers manually using
 the Instrument menu. To load a class driver, complete the following steps:

1. Select Instrument»Load .
2. In the Load Instrument dialog box, select the function panel (.fp) file for the class driver you want to load.

The class driver function panel files are in the <IVI Standard Root
 Dir>\Drivers directory.

The following figure shows the Instrument menu after you load the class drivers.

[IMAGE alt='image' src='GUID-177A75CE-D5CA-4203-A5A8-293E239ADC35-a5.gif']

#### LabWindows/CVI Instrument
 Menu

You do not have to include the class drivers that you load through the Instrument
 menu in your project, and you can load and unload them at any time. Class drivers
 that are loaded through the Instrument menu are not automatically loaded to your
 project and can be unloaded at any time. However, you must reload the driver every
 time you launch LabWindows/CVI.

To add the IVI class drivers into your project, complete one of the following
 steps:

1. Open the Function Panel window.
2. Select File»Add to Project .

or

1. From the Workspace window, select Edit»Add to Project»Instrument
 (.fp) .
2. Choose the .fp file for the driver.

The .fp file represents the class driver in the project list. If the .fp file is in
 the project list, LabWindows/CVI automatically loads the class driver when you open
 the project and removes the class driver when you unload the project.

A class driver function panel contains a function panel window for each function that
 the class driver exports. With the function panel windows, you can interactively
 call class driver functions and automatically generate code for your
 application.

The class drivers have high-level and low-level functions. With the high-level
 functions, you can easily initialize and close the instrument, configure the
 instrument, control instrument operations, and retrieve measurements. High-level
 functions set multiple instrument attributes in a single operation.

For example, to set up and take a measurement using a DMM, you might use the
 following high-level statements in your program:

ViReal64
 reading;

ViSession
 dmmHandle;

IviDmm_Init ("DMM1", VI_TRUE, VI_TRUE,
 &dmmHandle);

IviDmm_ConfigureMeasurement (dmmHandle,
 IVIDMM_VAL_DC_VOLTS_RATIO, IVIDMM_VAL_AUTO_RANGE_ON,
 0.0006));

IviDmm_ConfigureTrigger (dmmHandle,
 IVIDMM_VAL_IMMEDIATE, 0.0));

IviDmm_Read (dmmHandle,
 5000, &reading));

IviDmm_close
 (dmmHandle);

With the low-level functions of the class drivers, you can access individual
 instrument driver attributes. For example, the following figure shows the Set
 Attribute function panel for the IviDmm class driver. Refer to the *IVI Class
 Driver Help for LabWindows/CVI* for more information on how to use
 function panels in LabWindows/CVI.

[IMAGE alt='image' src='GUID-9A10263C-8072-458B-8371-4FCAC038B653-a5.gif']

Parent topic:

Using IVI Class Drivers

Related information:

- IVI Class Driver Help for
 LabWindows/CVI

<!--NI_TOPIC bundle=ivi-compliance-package path=using-high-level-configuration-functions-rath.html language=enus -->
## TOPIC 00046: Using High-Level Configuration Functions Rather than Setting Individual Attributes

- bundle_id: `ivi-compliance-package`
- source_path: `using-high-level-configuration-functions-rath.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-high-level-configuration-functions-rath.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Rather than Setting Individual AttributesIVI class drivers have both high-level and low-level configuration functions. Using the high-level functions to configure an instrument is a good practice. The high-level functions group the setting of related attributes into a single operation. When you call

### Using High-Level Configuration Functions Rather than Setting Individual Attributes

#### Rather than Setting Individual
 Attributes

IVI class drivers have both high-level and low-level
 configuration functions. Using the high-level functions to configure an instrument
 is a good practice. The high-level functions group the setting of related attributes
 into a single operation. When you call a high-level function in a class driver, the
 class driver invokes the corresponding function in the specific driver. The specific
 driver is responsible for setting the attributes in the correct order for the
 instrument. Also, the specific driver can handle complex interactions between
 multiple attributes for the instrument. If you swap instruments, the new specific
 driver sets the attributes in the correct order and handles attribute interactions
 for the new instrument.

With the low-level functions, you set values for
 individual attributes. When you use the low-level functions to manipulate
 attributes, you must understand the relationships and interactions between the
 attributes for an instrument. When you replace the instrument, the attribute order
 dependencies are likely to change. Therefore, you have to change the order in which
 your program sets the attributes when you swap the instrument.

Parent topic:

Developing an Instrument Independent Application

<!--NI_TOPIC bundle=ivi-compliance-package path=using-ivi-class-drivers.html language=enus -->
## TOPIC 00047: Using IVI Class Drivers

- bundle_id: `ivi-compliance-package`
- source_path: `using-ivi-class-drivers.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-ivi-class-drivers.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you configure your system with MAX, you can develop an interchangeable application by making calls to the IVI class drivers. The class drivers isolate your program from the specific drivers that communicate with the instruments.

### Using IVI Class Drivers

After you configure your system with MAX, you can develop an interchangeable application by
 making calls to the IVI class drivers. The class drivers isolate your program from the
 specific drivers that communicate with the instruments.

Related concepts:

- Using Class Drivers in LabVIEW
- Using Class Drivers in LabWindows/CVI

<!--NI_TOPIC bundle=ivi-compliance-package path=using-logical-names.html language=enus -->
## TOPIC 00048: Using Logical Names

- bundle_id: `ivi-compliance-package`
- source_path: `using-logical-names.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-logical-names.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use logical names to identify a physical instrument and specific driver without including instrument specific information in your test program. In general, creating a logical name that fits the context of your application is best, no matter which specific instrument you use.For example, the logical

### Using Logical Names

Use logical names to identify a physical instrument and specific driver without including
 instrument specific information in your test program. In general, creating a logical
 name that fits the context of your application is best, no matter which specific
 instrument you use.

For example, the logical name DMM fits the context of an application in which you swap two or
 more digital multimeters such as a Fluke 45 and an HP 34401A. In contrast, the logical
 names FL45 and HP34401A do not fit the context because they are too specific.

When you create a logical name, consider if you want to use it in multiple applications. One
 approach is to create one logical name for all the applications in your system. Another
 approach is to create a unique logical name for each application.

If you create a global logical name, you can quickly reconfigure your entire system. When
 replacing an instrument, you reconfigure only one logical name in MAX. The disadvantage
 of this method is that any change to the configuration of the logical name in MAX
 affects all applications in your system that use that name. You are also limited by the
 requirements of all the applications that use the logical name. This approach also
 requires that you coordinate your applications to use the same set of logical names.

If you create a unique logical name for each application, you can customize the configuration of
 the instrument for each application. However, if you swap an instrument that many
 applications use, it may take you longer to reconfigure your system. Also, this approach
 requires that you coordinate the development of the applications that you run on your
 system so that they do not use the same logical names.

Parent topic:

Developing an Instrument Independent Application

<!--NI_TOPIC bundle=ivi-compliance-package path=using-the-development-mode-settings-for-inher.html language=enus -->
## TOPIC 00049: Using the Development Mode Settings for Inherent Attributes

- bundle_id: `ivi-compliance-package`
- source_path: `using-the-development-mode-settings-for-inher.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/using-the-development-mode-settings-for-inher.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: IVI class drivers have many features that help you to debug and analyze your program. You enable these features by setting the development mode settings for inherent attributes.After you complete the development of your application and verify that your program is working correctly, enable the produc

### Using the Development Mode Settings for Inherent Attributes

IVI class drivers have many features that help you to debug and analyze your program. You enable
 these features by setting the development mode settings for inherent attributes.

After you complete the development of your application and verify that your program is working
 correctly, enable the production mode settings for the inherent attributes to maximize
 performance.

The following table lists the development mode and production mode settings for the inherent
 attributes.

| LabVIEW Property | Inherent Attribute | Development Mode Setting | Production Mode Setting |
| --- | --- | --- | --- |
| ClassPrefix Spy | CLASSPREFIX_ATTR_SPY | VI_TRUE | VI_FALSE |
| ClassPrefix Range Check | CLASSPREFIX_ATTR_RANGE_CHECK | VI_TRUE | VI_FALSE |
| ClassPrefix Query Instrument Status | CLASSPREFIX_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_FALSE |
| ClassPrefix Interchange Check | CLASSPREFIX_ATTR_INTERCHANGE_CHECK | VI_TRUE | VI_FALSE |
| ClassPrefix Record Value Coercions | CLASSPREFIX_ATTR_RECORD_COERCIONS | VI_TRUE | VI_FALSE |

Refer to *Measurement & Automation Explorer Help for IVI* for information
 about how to use MAX to set the development mode and production mode settings for
 inherent attributes.

#### CLASSPREFIX_ATTR_RANGE_CHECK

Enables/disables range checking. If you enable range checking, the specific driver
 checks all parameters passed to the class driver and specific driver functions.

#### CLASSPREFIX_ATTR_QUERY_INSTRUMENT_STATUS

Enables/disables instrument
 status checking. If you enable instrument status checking, the specific driver
 checks the status of the instrument after most calls made to the class driver or
 specific driver.

#### CLASSPREFIX_ATTR_INTERCHANGE_CHECK

Enables/disables *interchangeability checking*. Interchangeability
 checking verifies that your program produces the same behavior when you use it with
 a different instrument. If you enable interchangeability checking, the driver queues
 warnings when it encounters instrument configurations that are not likely to produce
 the same behavior when you use a different instrument. The class driver obtains
 interchangeability warnings from the specific driver, so you can find additional
 documentation on the warnings provided in the specific driver's help file.

Note

Analyzing Your Program with NI I/O Trace

PREFIX_GetNextInterchangeWarning

#### CLASSPREFIX_ATTR_RECORD_COERCIONS

Enables/disables coercion recording. In many cases, specific drivers coerce the
 value that you specified for a function parameter or attribute to a value that the
 instrument can accept. Specific drivers may coerce a value only if the new value
 results in instrument behavior that is the same or better than what you requested.
 Coercion of values is essential for instrument interchangeability. If specific
 drivers did not coerce values, you would have to specify valid values for the
 specific instruments you use. If you attempted to use your program with new
 instruments, the valid values would probably be different.

For example, the
 IviDmm class defines an attribute called IVIDMM_ATTR_RANGE that you
 use to specify the measurement range. Typically, DMMs have a discrete set of ranges.
 One DMM might have discrete settings for the range attribute such as 1 V, 10 V, and
 100 V. Another DMM might have discrete settings such as 2 V, 20 V, and 200 V. If you
 use the first instrument, you might set the range attribute to 10.0. If you then
 attempt to run your program with the second instrument, 10.0 is no longer an
 acceptable value, so the specific driver for the second instrument therefore coerces
 the value to 20.0.

In other cases, specific drivers coerce the value you
 specified for an attribute to the value the instrument would coerce the value to.
 This coercion is necessary to implement the IVI state caching feature. For example,
 if a DMM has discrete settings for the range attribute of 1 V, 10 V, and 100 V, it
 coerces any value between 2 V and 9 V to 10 V. Thus, if you set the range to 2 V,
 then to 7 V, and then to 5 V, the actual range remains at 10 V. To prevent sending
 redundant commands to the instrument, the specific driver coerces the value
 internally, sends the coerced value to the instrument, and caches the coerced value.
 In this example, the specific driver coerces 2 V to 10 V, sends 10 V to the
 instrument, and caches 10 V. When you set the range to 5 V and 7 V, the driver
 coerces these values to 10 V, notices that 10 V is the current cache value, and does
 not send any commands to the instrument.

If you enable coercion recording, the
 driver keeps a record of each instance a ViInt32 or
 ViReal64 value is coerced. You can view the coercion records to
 understand how the specific driver coerces values that you specified in your
 program.

Note

PREFIX_GetNextCoercionRecord

Parent topic:

Developing an Instrument Independent Application

Related concepts:

- Interchangeability Checking
- Analyzing Your Program with NI I/O Trace

Related information:

- Measurement & Automation Explorer Help
 for IVI

<!--NI_TOPIC bundle=ivi-compliance-package path=verifying-instrument-replacement-candidates.html language=enus -->
## TOPIC 00050: Verifying Instrument Replacement Candidates

- bundle_id: `ivi-compliance-package`
- source_path: `verifying-instrument-replacement-candidates.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/verifying-instrument-replacement-candidates.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use to verify whether a new instrument can work with an existing application.

### Verifying Instrument Replacement
 Candidates

You can use to verify whether a new instrument can work with an existing application.

<!--NI_TOPIC bundle=ivi-compliance-package path=viewing-interchangeability-warnings.html language=enus -->
## TOPIC 00051: Viewing Interchangeability Warnings

- bundle_id: `ivi-compliance-package`
- source_path: `viewing-interchangeability-warnings.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/viewing-interchangeability-warnings.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Analyzing Your Program with NI I/O Trace to view interchangeability warnings. NI I/O Trace highlights functions in blue that have interchangeability warnings.Alternatively, you can use the Get Next Interchange Warning VI or function to retrieve interchangeability warnings programmaticall

### Viewing Interchangeability Warnings

You can use *Analyzing Your Program with NI I/O Trace* to view interchangeability
 warnings. NI I/O Trace highlights functions in blue that have interchangeability
 warnings.

Note

Parent topic:

Class Driver Simulation

Related concepts:

- Analyzing Your Program with NI I/O Trace

<!--NI_TOPIC bundle=ivi-compliance-package path=vxiplug-play-function-simulation.html language=enus -->
## TOPIC 00052: VXIplug&play Function Simulation

- bundle_id: `ivi-compliance-package`
- source_path: `vxiplug-play-function-simulation.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/vxiplug-play-function-simulation.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure the simulation of the VXIplug&play functions, select VXIplug&play Function Simulation from the View ring control of the Simulator Setup dialog box. The VXIplug&play Function Simulation view is the same for all simulation drivers.The following table describes the controls that appear in

### VXIplug&play Function Simulation

To configure the simulation of the VXIplug&play functions, select
 VXIplug&play Function Simulation from the View ring
 control of the Simulator Setup dialog box. The VXIplug&play
 Function Simulation view is the same for all simulation drivers.

The following table describes the controls that appear in the VXI plug&play Function
 Simulation view, including the names of the related attributes.

| Control Label | Description | Related Attribute in the Initial Settings Tab |
| --- | --- | --- |
| SelfTest Code | Value that the Prefix_self_test function returns in the self-test code parameter | PREFIX_ATTR_SELF_TEST_CODE |
| SelfTest Message | String that the Prefix_self_test function returns in the self-test message parameter | PREFIX_ATTR_SELF_TEST_MSG |
| Error Code | Value that the Prefix_error_query function returns in the error code parameter | PREFIX_ATTR_ERROR_QUERY_CODE |
| Error Message | String that the Prefix_error_query function returns in the error message parameter | PREFIX_ATTR_ERROR_QUERY_MSG |
| Instrument Driver Revision | String that the Prefix_revision_query function returns in the instrument revision parameter | PREFIX_ATTR_DRIVER_REV_QUERY |
| Firmware Revision | String that the Prefix_revision_query function returns in the instrument firmware revision parameter | PREFIX_ATTR_INSTR_REV_QUERY |

Parent topic:

IVI Class Driver Simulation Overview

<!--NI_TOPIC bundle=ivi-compliance-package path=what-the-setup-program-installs.html language=enus -->
## TOPIC 00053: What the Setup Program Installs

- bundle_id: `ivi-compliance-package`
- source_path: `what-the-setup-program-installs.html`
- source_url: https://docs-be.ni.com/bundle/ivi-compliance-package/raw/resource/enus/what-the-setup-program-installs.html
- document_id: `ivi-compliance-package`
- page_type: `leaf`
- content_type: `concept`
- source_description: The setup program for the IVI Compliance Package installs the components on your hard disk, which are described in the Related Concepts.

### What the Setup Program Installs

The setup program for the IVI Compliance Package installs the components on your hard disk, which
 are described in the Related Concepts.

Parent topic:

IVI Compliance Package Overview

Related concepts:

- IVI Class Drivers
- MAX
- IVI Shared Components
