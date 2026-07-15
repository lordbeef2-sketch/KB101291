# NI DOCUMENT BUNDLE: labview-model-interface-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-model-interface-toolkit start=1 end=28 -->
<!--NI_TOPIC bundle=labview-model-interface-toolkit path=basic-architecture-for-executing-models-model.html language=enus -->
## TOPIC 00001: Basic Architecture for Executing Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `basic-architecture-for-executing-models-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/basic-architecture-for-executing-models-model.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Model Interface API allows for integration and execution of models in LabVIEW control systems, supporting reliable timing and synchronization for applications. The Model Interface API allows you to integrate and run models in LabVIEW control systems. In many applications, timing is an important

### Basic Architecture for Executing
 Models

The Model Interface API allows for integration and execution of models in LabVIEW
 control systems, supporting reliable timing and synchronization for
 applications.

The Model Interface API allows you to integrate and run models in LabVIEW control systems. In
 many applications, timing is an important factor in application design. Time steps must
 repeat based on specific timing characteristics or synchronize model execution with a
 hardware device clock. To ensure LabVIEW runs a model reliably, you can separate your
 code into at least two components:

A high-priority control loop

Lower priority/background code

Prior to the control loop of your code, you can perform initialization-related tasks, such as
 loading the model and initializing parameter values. After the control loop and
 background code stops, you can unload the model and close any references you opened.

#### Example:
 Simple Model Control Application

The following block diagram shows a
 simple VI:

Figure 3.

[IMAGE alt='image' src='GUID-B2728B93-0C4E-471A-A619-E2E1B45A9AE0-a5.gif']

The VI uses the Model Interface API to perform the following steps:

1. Loads the model from the disk.
2. Creates a model reference you pass to other VIs throughout the application to
 run and interact with the model. Note Avoid
 branching the model reference wire to ensure optimal performance. The Model
 Interface API is not designed to operate on a model in parallel
 locations.
3. Reads the compiled rate of the model in seconds.
4. Sets the period of the Timed Loop .. Each iteration of the
 Timed Loop must complete execution before the
 specified period. This example converts seconds to milliseconds. The
 Period input of the Timed Loop 
 requires values in the same units as the 1 kHz 
 clock timing source configured for the loop.
5. Performs the following tasks during each iteration of the high-priority control
 loop:
  1. Writes a value of 0 to the only model inport. Note This example applies the same inport value
 during every time step. This might be typical of applications in
 which you want to observe the model response to a particular
 stimulus. However, in hardware-in-the-loop applications, dynamic
 inport values might come from hardware I/O, such as channels on a
 DAQ device. In other applications, you might allow users to
 manipulate inport values via front-panel controls.
  2. Steps the model during each iteration of the Timed
 Loop . The Timed Loop iterates
 until an error occurs or the stop control is
 TRUE .
  3. Displays the value of the model outport in a waveform chart on the front
 panel.
6. The Model Interface API sets the value of a parameter when the control loop
 sleeps. This loop is typical of background-priority code.
7. The Model Interface API unloads the model and handles any errors that
 occurred.

In this example, the control loop transfers data between the model and front
 panel controls and indicators. A real-world application might contain the following
 features:

- A model with multiple inports, outports, parameters, and signals
- Hardware device driver VIs that read data from or write data to hardware
 I/O
- Multiple models

Note

labview\examples\Control and
 Simulation\Model Interface

Related concepts:

- Initializing Parameter Values
- Updating Parameters While the Model Runs
- Probing Signal Values

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=compiling-a-model-from-mathworks-simulink-sof.html language=enus -->
## TOPIC 00002: Compiling a Model from MathWorks Simulink

- bundle_id: `labview-model-interface-toolkit`
- source_path: `compiling-a-model-from-mathworks-simulink-sof.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/compiling-a-model-from-mathworks-simulink-sof.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Convert MathWorks Simulink models into compiled models compatible with the Model Interface API. Before you complete this procedure, ensure that you configure your models to interact with the Model Interface API the way you want. Verify that the VeriStand Model Framework is installed. The VeriStand M

### Compiling a Model from MathWorks
 Simulink

Convert MathWorks Simulink models into compiled models compatible with the Model
 Interface API.

Note

1. Verify that the VeriStand Model Framework is installed. The VeriStand Model Framework adds
 tools to Simulink that you can use later in this procedure.
2. Ensure you have the correct compiler.

Answer the following questions to determine which tools you must use to convert and compile
 Simulink models:

What Real-Time Operating System (RTOS) does my target run?

Real-Time
 Controllers and Real-Time Operating System Compatibility

ni.com

Given the operating system my target runs, what tools do I use to compile my
 model and what output do I create?

You can use the following compilers with various operating systems:

| Operating System | Required Tools | Required Output Type |
| --- | --- | --- |
| Microsoft Windows | Microsoft Visual C++ MathWorks Simulink Coder Note VeriStand 2015 also supports the older version of the Simulink Coder, called the Real-Time Workshop. | .dll |
| NI Linux Real-Time | C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition MathWorks Simulink Coder | .so |

Which versions of these tools are compatible with the version of the Model
 Interface Toolkit I am using?

LabVIEW Model Interface
 Toolkit

VeriStand
 Model Generation Support and MathWorks Simulink Compatibility

ni.com

Note

The LabVIEW Model Interface
 Toolkit shares several
 components with the VeriStand, such as tools for compiling models
 designed in third-party modeling environments.

For more
 information, see the following knowledge base articles at
 ni.com:

- Creating Simulation Models Using NI VeriStand Model
 Framework
- Generating Models from The MathWorks, Inc. Simulink Software
 for Deployment on NI Linux Real-Time Systems

#### Select the Correct Compiler in MATLAB

Windows

mex -setup

NI Linux Real-Time

#### Build the Compiled Model in
 Simulink

After you select and set up the correct compiler, complete the
 following steps to build the compiled model:

1. Launch Simulink.
2. Load the model you want to convert.
3. Select Simulation»Model Configuration Parameters to launch the Model Configuration
 Parameters dialog box.
4. Click the Solver tab.
5. Configure the following options:
  - Stop time : inf
  - Type : Fixed-step
6. Click the Code Generation tab.
7. Click the Browse button to launch the System
 Target File Browser dialog box.
8. Select the correct option for your target from the following list:
9. ETS, Windows — NIVeriStand.tlc—NI Real-Time Target
10. NI Linux Real-Time —
11. ARM-based targets — NIVeriStand_Linux_ARM_32.tlc — NI Real-Time Target
12. Intel x64-based targets — NIVeriStand_Linux_64.tlc — NI Real-Time Target
13. Click the OK button.
14. Click the Build button in the Category section
 to build the compiled model. The MATLAB command window displays the status of
 the build process. The following message in the MATLAB command window indicates
 that the Simulink Coder has completed building the compiled model:
 ### Successful completion of build procedure for model:
 ModelName.

#### Including
 External Source Code in the Compiled Model

If the model you are converting
 specifies any .c or .h files, you must
 specify the locations of the files to include them in the compiled model. To specify
 the source files and include directories in Simulink, go to the
 Configuration Parameters dialog box on the
 Code Generation tab.

Parent topic:

Using Models from MathWorks Simulink

Related concepts:

- Considerations for Integrating Models from MathWorks Simulink
- Compiling Models

Related information:

- Real-Time Controllers and Real-Time Operating System
 Compatibility
- VeriStand Model Generation Support and MathWorks Simulink
 Compatibility
- Creating Simulation Models Using NI VeriStand Model
 Framework
- Generating Models from The MathWorks, Inc. Simulink® Software for
 Deployment on NI Linux Real-Time Systems

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=compiling-models-overview-model-interface-too.html language=enus -->
## TOPIC 00003: Compiling Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `compiling-models-overview-model-interface-too.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/compiling-models-overview-model-interface-too.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compile models compatible with the LabVIEW Model Interface Toolkit. Use the Model Interface VIs of the LabVIEW Model Interface Toolkit to run and interact with models. However, this toolkit does not provide support for compiling models that are compatible with the toolkit. The following free compone

### Compiling Models

Compile models compatible with the LabVIEW Model Interface
 Toolkit.

Use the Model Interface VIs of the LabVIEW Model Interface
 Toolkit to run and interact with models. However, this
 toolkit does not provide support for compiling models that are compatible with the
 toolkit. The following free components are available from VeriStand. The components
 provide support for compiling compatible models:

VeriStand Model Generation Support Component

VeriStand Model Framework Component

LabVIEW Model Support Component

FMI Support Component

Note

LabVIEW Model Interface
 Toolkit

#### VeriStand Model Generation Support

The VeriStand Model Generation
 Support allows compiling models using Mathworks Simulink for running in LabVIEW Model Interface
 Toolkit. When you run your test application that
 you designed using the LabVIEW Model Interface
 Toolkit, the application
 executes functions that the .vsmodel binaries define. The
 .vsmodel binaries also execute your model
 code.

#### VeriStand Model Framework

The VeriStand Model Framework provides tools
 for compiling models created in third-party modeling environments and for designing
 custom models in C/C++. When you run your test application, designed using the LabVIEW Model Interface
 Toolkit, the application executes functions
 defined in VeriStand Model Framework files. These functions then call functions in
 your model code to execute the model.

The VeriStand installer installs the
 VeriStand Model Framework files and documentation at
 RootDrive:\VeriStand\xxxx\ModelInterface\,
 where RootDrive is the drive where NI software installs and
 xxxx is the VeriStand version number. If you cannot locate
 the files at that location, run the VeriStand installer again and select the
 VeriStand Model Framework item from the list of features
 to install. You do not need to reinstall other NI software to install the VeriStand
 Model Framework.

Related concepts:

- Using Models from MathWorks Simulink
- Using C/C++ Models
- Using LabVIEW VIs as Models

Related information:

- Using FMU Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=components-of-an-application-model-interface.html language=enus -->
## TOPIC 00004: Components of an Application

- bundle_id: `labview-model-interface-toolkit`
- source_path: `components-of-an-application-model-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/components-of-an-application-model-interface.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Components of applications built with the LabVIEW Model Interface Toolkit, including targets, LabVIEW applications, and models. An application built with the LabVIEW Model Interface Toolkit typically consists of the following components: Target The system on which you run the application and the mod

### Components of an
 Application

Components of applications built with the LabVIEW Model Interface
 Toolkit,
 including targets, LabVIEW applications, and models.

An application built with the LabVIEW Model Interface
 Toolkit typically consists of the following components:

Target

LabView application

Model

When the target runs the LabVIEW application,
 the Model Interface API loads the model and iteratively executes the model. The API transfers
 data to and from the model and other parts of the system.

#### Additional Components in Applications that Include Hardware

If you
 intend to run your test application on an RT target or integrate I/O from hardware, you
 might need the following components:

LabVIEW Real-Time Module Component

LabVIEW FPGA Module Component

Driver Software Component

#### Components of a Model

Models can contain the following components
 through which tuning, data communication, and debugging occurs:

Inport and Outport Components

Parameter Components

Signal Components

Consider a system that contains a physical motor controller and a model that
 represents a DC motor. The model runs on a hardware target. Such a model might contain the
 following components:

- An inport that accepts the motor command from the motor controller.
- An outport that returns the motor speed from the model.
- Parameters that adjust the load on the motor. You might set parameter values once per
 test rather than updating them frequently during the test.
- A signal that returns internal data that aids in debugging.

#### Building and Preparing Models for Use in
 LabVIEW

You can build models using several different modeling environments. You
 must compile a model in the modeling environment before it can run in your application. The
 exact process for compiling a model to interact with the LabVIEW Model Interface
 Toolkit depends on the modeling environment you use to build
 it.

Note

For more information on preparing the model for use with the Model Interface API, see the
 *Compiling Models* section.

If you create the model in a modeling environment not covered in the *Compiling
 Models* section, refer to the documentation for that modeling environment.

#### Integrating Models into the LabVIEW
 Application

When you build your test application in LabVIEW, you connect parts of the model to sources
 of I/O in other parts of the application. For example, you might pass data from a hardware
 channel to a model inport so the model receives and operates on data from the hardware
 device. You must also configure timing and choose how to interact with parameters and
 signals in the model.

You can use the Model Interface Toolkit VIs for the following
 tasks:

- Control the execution of models
- Monitor status and timing
- Configure parameters
- Read signals as the models run

Related concepts:

- Using Models from MathWorks Simulink
- Using C/C++ Models
- Using LabVIEW VIs as Models
- Supported Model Types and Modeling Environments
- Basic Architecture for Executing Models
- Compiling Models

Related information:

- Software and Driver Downloads

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=configuring-model-timing-model-interface-tool.html language=enus -->
## TOPIC 00005: Configuring Model Timing

- bundle_id: `labview-model-interface-toolkit`
- source_path: `configuring-model-timing-model-interface-tool.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/configuring-model-timing-model-interface-tool.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure model timing by setting the execution rate using the Timed Loop. A model is set to run at a certain rate, or step size, as defined in the build options when the model is compiled. However, the rate at which the Model Interface API actually steps the model is determined by how often the Tak

### Configuring Model Timing

Configure model timing by setting the execution rate using the Timed
 Loop.

A model is set to run at a certain rate, or step size, as defined in the build options when the
 model is compiled. However, the rate at which the Model Interface API actually steps the
 model is determined by how often the Take Model Time Step VI runs in
 your application. You can use a Timed Loop to step the model at a
 specific rate to ensure this VI runs reliably and repeatedly.

In the following block diagram, each iteration of the Timed Loop must
 complete execution within the specified period. To calculate the period, the
 Get Model Period VI reads the compiled rate of the model in
 seconds. The Period input of the Timed
 Loop requires values in the same units as the 1 kHz clock timing source. This application converts seconds to milliseconds
 to match these units.

Figure 4.

[IMAGE alt='Block diagram showing a Timed Loop with model period calculation and simulation timing.' src='GUID-742629EC-FAEE-4761-96EE-1DAFB7F43D86-a5.gif']

Note

Timed Loop

Timed Loop

#### Methods for Setting and Monitoring
 Timing

The following table shows the features that allow you to control and monitor the
 timing of models in your application:

| Feature | Action |
| --- | --- |
| Period input on Timed Loop | Set the period of Timed Loop iterations/rate of model time steps. |
| Iteration Duration output on Timed Loop | View how long the current time step of the model has been running. |
| Finished Late? [i-1] output on Timed Loop | View whether the previous iteration of the Timed Loop ran longer than the specified period. |
| Get Simulation Time VI | View the time in the model. |

For an example code that demonstrates how to use the MIT Simple
 Load and Run Model VI, see the
 labview\examples\Control and Simulation\Model Interface
 directory.

#### Running Models Faster or Slower
 than Real Time

Depending on the rate at which you call the Take Model Time Step
 VI, the rate at which the model executes might differ from the compiled rate. For
 example, even if the model was compiled to run at 100
 Hz, you can set the Timed Loop period so that it
 runs at 1 kHz, or 10 times faster than real time.
 This means the model does not run in real time and is potentially unstable.

If
 both the controller and plant are simulated, such as in model-in-the-loop testing,
 running your model at a faster rate than the rate for which it was compiled can be
 desirable. Running faster than real time allows you to accomplish more simulation in
 a shorter amount of time. However, when you test with real hardware, as in
 hardware-in-the-loop testing, run your model at the rate for which it was compiled
 to accurately simulate the
 system.

Parent topic:

Basic Architecture for Executing Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=considerations-for-integrating-models-from-ma.html language=enus -->
## TOPIC 00006: Considerations for Integrating Models from MathWorks Simulink

- bundle_id: `labview-model-interface-toolkit`
- source_path: `considerations-for-integrating-models-from-ma.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/considerations-for-integrating-models-from-ma.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Model Interface API identifies and categorizes elements in MathWorks Simulink models. The Model Interface API identifies the following elements in models you created and compiled in MathWorks Simulink according to their configuration in the Simulink: Inports Outports Parameters Signals Case Stud

### Considerations for Integrating Models from
 MathWorks Simulink

The Model Interface API identifies and categorizes elements in MathWorks Simulink
 models.

The Model Interface API identifies the following elements in models you created and compiled in
 MathWorks Simulink according to their configuration in the Simulink:

- Inports
- Outports
- Parameters
- Signals

#### Case
 Study: Simple Models

Figure 1.

[IMAGE alt='A Simulink model showing a sine wave generator, gain block, summation block, and output.' src='GUID-9A630544-0538-4ECD-99F6-00E6F85BF208-a5.gif']

When you load this model in an application, the Model Interface API
 categorizes its components as described in the following table:

| Component in Model | Type of Component in LabVIEW |
| --- | --- |
| Raw_Sine | Signal |
| Sine_Gain | Parameter |
| In1 | Inport |
| Out1 | Outport |

#### Inports
 and Outports

Note

LabVIEW Model Interface
 Toolkit

#### Parameters

Compiled models contain one of two types of parameters:

Global parameter

Model
 Name

Parameter Name

Block parameters

Model Name

Block
 Name

Parameter Name

Tip

Get
 Paths

A Simulink model can contain only one type of parameter. However, an
 application can contain a model with global parameters and a model with block
 parameters.

#### Conditions Where Parameters Are
 Unavailable

The Model Interface API supports model references to submodels, but you cannot access
 parameters or signals in submodels. Submodels run in an application built with the
 Model Interface API, but their parameters and signals are not available for writing
 or reading.

In the Simulink, you can use inline parameters, but the Model
 Interface API cannot access inline parameters to get or set their values. If you use
 an inline parameter, you can still allow the Model Interface API to influence the
 parameter by configuring a variable that affects the parameter to be tuneable. For
 example, consider a model with the following characteristics:

- Contains a constant configured with the expression x + 3 .
- Contains a sine wave block whose amplitude and frequency parameters are inlined,
 and therefore unavailable in the Model Interface API.
- Adds the result of the x + 3 constant to the output from the
 sine wave block.

Although the parameters of the sine wave block are unavailable, you can
 influence the operation by specifying that the x variable is
 tunable in the Simulink. When x is tunable, it will appear in the
 list of parameters of the model, so you can change the value of x
 like a parameter as the model runs.

#### Signals

Model signals are usually excluded when you convert a model into
 a compiled model. To include model signals you must define the signals as test
 points in the software you use to compile the model.

#### Conditions Where Signals Are
 Unavailable

Certain optimizations you enable in the Simulink can make a signal unavailable to the
 Model Interface API. You can disable these options for the entire model to make all
 signals available for probing, but the memory footprint of the model increases as a
 result. Alternatively, you can mark individual signals as test points in the
 Simulink to maintain a reduced memory footprint while keeping the test-point signals
 available for probing.

Note

#### Bus
 Objects

In models compiled in Simulink R2010b or a later supported
 version, named components of bus objects, such as signals, are represented in the
 same hierarchy as in the uncompiled model. For models compiled in versions of the
 Simulink earlier than R2010b, bus objects are represented as a single vector of
 components.

Parent topic:

Using Models from MathWorks Simulink

Related concepts:

- Using Models from MathWorks Simulink

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=conversion-process-for-models-from-mathworks.html language=enus -->
## TOPIC 00007: Conversion Process for Models from MathWorks Simulink

- bundle_id: `labview-model-interface-toolkit`
- source_path: `conversion-process-for-models-from-mathworks.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/conversion-process-for-models-from-mathworks.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Convert MathWorks Simulink models into compiled models using MathWorks Real-Time Workshop and compatible tools for use with the Model Interface API. Before you can run a model you created in MathWorks Simulink with the Model Interface API, you must use Simulink to convert the model file to a compile

### Conversion Process for Models from MathWorks
 Simulink

Convert MathWorks Simulink models into compiled models using MathWorks Real-Time
 Workshop and compatible tools for use with the Model Interface API.

Before you can run a model you created in MathWorks Simulink with the Model Interface API, you
 must use Simulink to convert the model file to a compiled model. Simulink performs the
 following process:

1. When you build the compiled model, MathWorks Real-Time Workshop converts your model and any
 submodels into a C/C++ code version of the same model. The resulting C/C++ code
 version of your model is the same Simulink block diagram model, just in a different
 form.
2. A compiler, such as Microsoft Visual C++, compiles the C/C++ code model into the appropriate
 file type. For example, the Microsoft Visual C++ compiler creates the following
 files: Where ModelName is the name of the
 model. Note Shared
 libraries used by LabVIEW VIs must exist in either the
 ni-rt/ or the ni-rt/system/
 directory. LabVIEW ignores paths that are specified in the Call Library
 Node.
  - ModelName .dll
  - ModelName .out
  - ModelName .so
3. The MathWorks Real-Time Workshop places the compiled model file in one of the following
 directories located in the current working directory: Note Real-Time
 Workshop also generates the
 <ModelName>_portsReadme.txt
 text file, which specifies the lengths and positions of all model inport and
 outport array data.
  - (NI Linux Real-Time)
 < ModelName > _NIVeriStand_Linux_ARM_32_rtw
  - ModelName > _NIVeriStand_Linux_64_rtw

The following figure shows this conversion process:

Figure 2.

[IMAGE alt='A flowchart showing the conversion process from a model to a compiled model using Real-Time Workshop.' src='GUID-25FDE079-A92E-4925-8B1B-B216B46C07A6-a5.gif']

The tools you use to convert a Simulink model, such as Microsoft Visual C++ and the GNU
 Toolchain, differ according to the type of target that runs the model. However, the
 previous conversion process is generally the same across targets. For more information
 on the versions of the LabVIEW, Windows, model compiler, and MathWorks you can use with
 the LabVIEW Model Interface
 Toolkit, see the *VeriStand Model Generation
 Support and MathWorks Simulink Compatibility* knowledge base article at
 *ni.com*.

To compile a Simulink model, the VeriStand Model Framework must be installed on the computer
 with Simulink. The VeriStand Model Framework adds tools to Simulink that allow you to
 compile models that work with the Model Interface API.

Parent topic:

Using Models from MathWorks Simulink

Related concepts:

- Compiling a Model from MathWorks Simulink
- Compiling Models

Related information:

- VeriStand Model Generation Support and MathWorks Simulink
 Compatibility

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=executing-multiple-instances-of-a-model-simul.html language=enus -->
## TOPIC 00008: Executing Multiple Instances of a Model Simultaneously

- bundle_id: `labview-model-interface-toolkit`
- source_path: `executing-multiple-instances-of-a-model-simul.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/executing-multiple-instances-of-a-model-simul.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Run multiple instances of a model with different conditions by copying model files and managing file names or locations. To execute the same model under different conditions, such as with different inport mappings or parameter values, complete the following steps: Loading more than one instance of t

### Executing Multiple Instances of a Model
 Simultaneously

Run multiple instances of a model with different conditions by copying model files
 and managing file names or locations.

Note

1. Make a copy of the model files on disk for each instance you want to run.
2. Complete one of the following steps, depending on the real-time operating system of your
 target:
3. Windows —Rename the copied model files so that each has a unique name.
4. NI Linux Real-Time —Ensure all copied models have the same name as the original. Then copy
 each model file to a different location on the Linux Real-Time target
 using WebDAV. Note For information on
 how to transfer files using WebDAV, see *ni.com/info* and
 enter the code WebDAVTransfer.
5. Load the copies of the models separately with the Load Model VI. You can
 step the models within the same Timed Loop if you want them
 to run at the same rate.

For an example code that demonstrates executing multiple instances, see MIT Multiple
 Models VI in the labview\examples\Control and Simulation\Model
 Interface directory.

Parent topic:

Basic Architecture for Executing Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=finding-the-components-of-a-model-model-inter.html language=enus -->
## TOPIC 00009: Finding the Components of a Model

- bundle_id: `labview-model-interface-toolkit`
- source_path: `finding-the-components-of-a-model-model-inter.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/finding-the-components-of-a-model-model-inter.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Identify the inports, outports, parameters, and signals of a model by using VIs. If you receive a model you did not create, you might need to identify its inports, outports, parameters, and signals before you can work with the model. Complete the following steps to create a simple VI that returns in

### Finding the Components of a Model

Identify the inports, outports, parameters, and signals of a model by using
 VIs.

If you receive a model you did not create, you might need to identify its inports,
 outports, parameters, and signals before you can work with the model. Complete the
 following steps to create a simple VI that returns information about the components of a
 model:

1. Load the model using the Load Model VI.
2. Call the Get Paths VI to return the paths of components within
 the model.
3. Call the Get Information by Path VI to return the following
 information about the component at the path you specify:
  - Name
  - Dimension
  - Default value

Parent topic:

Components of an Application

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=frequently-asked-questions-faq-model-interfac.html language=enus -->
## TOPIC 00010: Troubleshooting the LabVIEW Model Interface Toolkit

- bundle_id: `labview-model-interface-toolkit`
- source_path: `frequently-asked-questions-faq-model-interfac.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/frequently-asked-questions-faq-model-interfac.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Guidance on troubleshooting the LabVIEW Model Interface Toolkit, including compatibility, performance, and model execution considerations. Modeling Environment Compatibility with the LabVIEW Model Interface ToolkitThe LabVIEW Model Interface Toolkit runs models from several environments, including M

### Troubleshooting the LabVIEW Model
 Interface Toolkit

Guidance on troubleshooting the LabVIEW Model Interface
 Toolkit, including
 compatibility, performance, and model execution considerations.

#### Modeling Environment Compatibility with the LabVIEW Model Interface
 Toolkit

LabVIEW Model Interface
 Toolkit

Note

LabVIEW Model Interface
 Toolkit

Support for
 Model Types and Modeling Environments

#### MathWork Compatibility with the LabVIEW Model Interface
 Toolkit

LabVIEW Model Interface
 Toolkit

VeriStand Model Generation
 Support and MathWorks Simulink Compatibility

ni.com

#### Hardware Target Compatibility with Operating
 Systems

The Model Interface API supports targets that run the following
 operating systems:

- NI Linux Real-Time
- Microsoft Windows

#### Model Run Rates

The rate at which a model
 runs depends on how often the Take Model Time Step VI executes to
 step your model. To ensure this VI runs at a specific rate, execute the
 Take Model Time Step VI in a Timed Loop.

#### System Performance

If you suspect that
 models are causing your application to run slower than you desire, consider the
 following solutions:

- Only set parameter values in the control loop if you must update the values
 during every time step. Instead, initialize the parameter values prior to
 running the control loop or set them in lower priority, background code.
- Probe only signals whose values you require. Probing many signals can negatively
 impact performance.
- Avoid changing the list of signals to probe frequently with the Set
 Signals to Probe VI.

#### Upgrading Applications and Models Created for the
 LabVIEW Simulation Interface Toolkit to Use the LabVIEW Model Interface
 Toolkit API

For more information on
 upgrading applications and models, see the *Migrating Simulation Interface
 Toolkit (SIT) Applications to the Model Interface Toolkit* knowledge base
 article at *ni.com*.

Related concepts:

- Supported Model Types and Modeling Environments

Related information:

- VeriStand Model Generation Support and MathWorks Simulink
 Compatibility
- Migrating Simulation Interface Toolkit (SIT) Applications to the
 Model Interface Toolkit

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=generating-compiled-models-from-vis-model-int.html language=enus -->
## TOPIC 00011: Generating Compiled Models from VIs

- bundle_id: `labview-model-interface-toolkit`
- source_path: `generating-compiled-models-from-vis-model-int.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/generating-compiled-models-from-vis-model-int.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Convert LabVIEW VIs or simulation subsystems into compiled models for use with the Model Interface API and Linux Real-Time OS targets. Prerequisite SoftwareTo compile models in LabVIEW, you must install the following software components: The LabVIEW Model Support feature The LabVIEW Application Buil

### Generating Compiled Models from VIs

Convert LabVIEW VIs or simulation subsystems into compiled models for use with the Model
 Interface API and Linux Real-Time OS targets.

#### Prerequisite Software

To compile models in LabVIEW, you must install the
 following software components:

- The LabVIEW Model Support feature
- The LabVIEW Application Builder, which is included with the LabVIEW Professional
 Development System. If you use the LabVIEW Base Development System or Full
 Development System, you can purchase the Application Builder separately.

Note

#### Generating a Compiled Model

.lvmodel

.lvmodelso

Note

.lvmodelso

1. Create a VI or simulation subsystem that performs the actions you want from your
 simulation model.
2. Configure the connector pane for your VI or subsystem.
3. Save the VI or subsystem.
4. In LabVIEW, select Tools»VeriStand»Generate Model from VI to display the Generate Model from VI 
 dialog box. Note The
 LabVIEW Model Interface
 Toolkit shares several components with
 the VeriStand, such as tools for compiling models.
5. In the Source VI Path field, enter the path where you
 saved the source file.
6. In the Destination Folder field, enter the path where you
 want to save the generated model.
7. If your source file is a simulation subsystem, click the
 Next button and complete the following steps:
  1. Specify a value for the model time step (sec) , which is the
 interval between the times the ODE Solver evaluates the model and
 updates the model output, in seconds. For your compiled model to run in
 real-time, the model time step (sec) value must
 equal the controller period multiplied by the
 Decimation model, or the
 Decimation model divided by the Target Rate: Model time step (sec) = Controller Period x
 Decimation 
 or Model time
 step (sec) = Decimation/Target Rate Where Controller
 Period = 1/Target Rate
  2. Specify the Target Rate on the
 Controller Configuration tab of the
 System Explorer window.
  3. Specify the Decimation on the Model
 Configuration tab of the System
 Explorer window. Note The equation only
 applies to compiled models you generate from simulation subsystems,
 because there is no simulated time in a standard VI.
  4. Specify the ODE Solver.
8. Click the Build button. The Generate Model from
 VI dialog box displays the progress of the model
 generation. Note If you experience errors when
 converting a VI or if the model does not contain the inports, outports, and
 parameters you expect, see the *Preparing VIs to Be Converted to a
 Compiled Model* section.

#### Moving the
 Model and Support Files

If you deploy the compiled
 .lvmodel or .lvmodelso to an RT
 target, LabVIEW copies required .dlls to the target
 automatically. However, if you manually copy the .lvmodel or
 .lvmodelso file to a new location, such as a different host
 system, you must also move any LabVIEW .dlls, such as
 NILVSim.dll for a simulation subsystem. The files are
 stored in a subdirectory named data in the destination folder
 where LabVIEW generates the compiled model.

Parent topic:

Using LabVIEW VIs as Models

Related concepts:

- Compiling Models
- Using LabVIEW VIs as Models

Related information:

- Software and Driver Downloads

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=initializing-inport-values-model-interface-to.html language=enus -->
## TOPIC 00012: Initializing Inport Values

- bundle_id: `labview-model-interface-toolkit`
- source_path: `initializing-inport-values-model-interface-to.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/initializing-inport-values-model-interface-to.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create and modify an array of inport values outside the control loop to optimize memory usage and prevent invalid model operations. The Take Model Time Step VI requires you to pass an array of inport values to the VI. By creating this array outside the control loop that contains the Take Model Time

### Initializing Inport Values

Create and modify an array of inport values outside the control loop to optimize
 memory usage and prevent invalid model operations.

The Take Model Time Step VI requires you to pass an array of inport values
 to the VI. By creating this array outside the control loop that contains the
 Take Model Time Step VI, you preallocate the memory and avoid
 incurring data copies in the control loop. This eliminates jitter while the model
 executes.

After you create an array of initial inport values, you can manipulate the array so it includes
 the values you want to apply to the model inports. Updating the initial inport values
 can allow you to prevent your models from ever using invalid values. For example, if the
 model divides by an inport value, you can change the default value from 0 to avoid an
 invalid operation.

The following block diagram shows how to use the Model Interface API to create and modify the
 inports array outside the control loop:

Figure 5.

[IMAGE alt='Block diagram showing the use of the Model Interface API to modify the inports array outside the control loop.' src='GUID-5683FC24-5179-4753-8864-F9714316D93B-a5.gif']

The Model Interface API performs the following steps:

1. Creates an array of the appropriate size for the model inport values. The value of
 each element is 0.
2. Replaces the first element in the array of initialized values with the value from
 the Offset front panel control. Note This example applies the same inport value during every
 time step. This might be typical of applications in which you want to observe
 the response to a particular stimulus. However, in hardware-in-the-loop
 applications, you might want to apply dynamic values from hardware I/O, such as
 channels on a DAQ device. In this scenario, you can manipulate the inport array
 inside the control loop.
3. Passes the inport array into the model and steps the model. Note Wires that connect terminals of the Take Model
 Time Step VI within a loop to terminals of objects outside of the
 loop must pass through a shift register rather than a tunnel for VeriStand to
 process the model correctly. Unlike shift registers, tunnels do not allow data
 from one iteration to carry over to the next causing the output value of the
 model to remain at zero.

For an example code that demonstrates how to use the MIT Inport and Output
 VI, see the labview\examples\Control and Simulation\Model Interface
 directory.

Parent topic:

Basic Architecture for Executing Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=initializing-parameter-values-model-interface.html language=enus -->
## TOPIC 00013: Initializing Parameter Values

- bundle_id: `labview-model-interface-toolkit`
- source_path: `initializing-parameter-values-model-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/initializing-parameter-values-model-interface.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set and initialize parameter values in models using the Model Interface API or modeling environment software. Many models have parameters, which act as variables in the model. The default values of parameters are compiled into the model. However, you can perform the following tasks to set new initia

### Initializing Parameter Values

Set and initialize parameter values in models using the Model Interface API or
 modeling environment software.

Many models have parameters, which act as variables in the model. The default values of
 parameters are compiled into the model. However, you can perform the following tasks to
 set new initial values:

- In the appropriate modeling environment software, manually change the parameter
 values in the model, and then recompile the model.
- In your LabVIEW code, use the Model Interface API to programmatically change parameter values
 at run time. After your code loads a model, you can set an initial value for a
 parameter.

To initialize a parameter value with the Model Interface API, complete the following steps:

1. Set the new values.
2. Commit the new values.

The following block diagram shows how to initialize a parameter in the initialization
 portion of your code:

Figure 6.

[IMAGE alt='A LabView block diagram showing steps to initialize a parameter using the Model Interface API.' src='GUID-50C581E8-2AEC-415A-9EA4-890EE868336C-a5.gif']

The initialization portion of the code performs the following steps:

- Loads the model from disk.
- Creates a model reference. Pass the model reference to set parameters for other VIs
 in the application and to run the model in a control loop.
- Creates a Parameter Interface reference. Pass the reference to
 get and set parameters for other VIs.
- Sets the value of the scalar parameter whose index is 1 among all the model
 parameters. Tip 
 You can use the Set Parameter VI to update one
 element of a vector parameter or an entire vector parameter.
 You can use the Get Information by Path VI to
 programmatically return the index of a specific parameter rather than
 hard-coding it on the block diagram. However, hard-coding values
 provides better performance than using this VI.

After the initialization portion of your code runs, your model will use the new parameter value
 when the control loop of your application steps the model for the first time.

For an example code that demonstrates the initialization process, see the MIT
 Multiple Models VI in the labview\examples\Control and
 Simulation\Model Interface directory.

Parent topic:

Basic Architecture for Executing Models

Related concepts:

- Updating Parameters While the Model Runs

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=installing-support-on-an-rt-target-model-inte.html language=enus -->
## TOPIC 00014: Installing Support on an RT Target

- bundle_id: `labview-model-interface-toolkit`
- source_path: `installing-support-on-an-rt-target-model-inte.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/installing-support-on-an-rt-target-model-inte.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Install support files for the LabVIEW Model Interface Toolkit on a Real-Time (RT) target to enable deployment of VIs using the Model Interface API. To deploy VIs that contain the Model Interface API to an RT target, you must first download support files for the LabVIEW Model Interface Toolkit to the

### Installing Support on an RT Target

Install support files for the LabVIEW Model Interface
 Toolkit on a Real-Time
 (RT) target to enable deployment of VIs using the Model Interface API.

LabVIEW Model Interface
 Toolkit

Note

LabVIEW Real-Time Target Configuration

Measurement & Automation Explorer Help

Help

»

MAX Help

Complete the following steps in MAX on a host system with the LabVIEW Model Interface
 Toolkit installed to download the support files:

1. Launch MAX from the Start menu or from NI Launcher.
2. Complete the following steps to launch the LabVIEW Real-Time Software Wizard: Note If a login
 password has been set, you might be prompted to enter the administrator name and
 password of the RT system. For more information, see the *Logging into your
 System* section in the *Measurement & Automation Explorer
 Help*.
  1. Expand Remote Systems in the configuration tree.
  2. Expand your RT target.
  3. Select Software .
  4. Click the Add/Remove Software icon on the toolbar to
 launch the LabVIEW Real-Time Software Wizard. Note If
 your target does not have a Software category,
 then it does not support the required software.
3. If prompted to install a recommended software set, select Custom software
 installation (currently installed) and click
 Next . Otherwise, proceed to the next step.
4. Click the icon next to the Model Interface Toolkit item.
5. Select Install the feature , and then click
 Next .
6. Confirm that you want to install LabVIEW Model Interface
 Toolkit support, and then
 click Next .

MAX displays the progress of the installation, and then reboots the target.

Parent topic:

Components of an Application

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=LMIToverview.html language=enus -->
## TOPIC 00015: LabVIEW Model Interface Toolkit Overview

- bundle_id: `labview-model-interface-toolkit`
- source_path: `LMIToverview.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/LMIToverview.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Model Interface Toolkit allows you to integrate models from a variety of simulation environments and programming languages into your development, prototyping, and testing of control systems. The toolkit provides the Model Interface API, a palette of VIs you use to run and interact with m

### LabVIEW Model Interface
 Toolkit
 Overview

The LabVIEW Model Interface
 Toolkit allows you to integrate models from a
 variety of simulation environments and programming languages into your development,
 prototyping, and testing of control systems.

The toolkit provides the Model Interface API, a palette of VIs you use to run and
 interact with models. You can use other LabVIEW features in conjunction with the Model
 Interface API, such as LabVIEW projects and hardware driver VIs.

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=manipulating-model-components-in-flattened-fo.html language=enus -->
## TOPIC 00016: Manipulating Model Components in Flattened Format

- bundle_id: `labview-model-interface-toolkit`
- source_path: `manipulating-model-components-in-flattened-fo.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/manipulating-model-components-in-flattened-fo.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Format data as flattened 1D arrays in column-major order for inports, outports, signals, and vector parameters. When you use the LabVIEW Model Interface Toolkit VIs to transfer data to model components, such as inports and parameters, in several cases you must format the data as flattened 1D arrays

### Manipulating Model Components in Flattened
 Format

Format data as flattened 1D arrays in column-major order for inports, outports,
 signals, and vector parameters.

When you use the LabVIEW Model Interface
 Toolkit VIs to transfer data to model
 components, such as inports and parameters, in several cases you must format the data as
 flattened 1D arrays of values in column-major order.

#### Format of
 Inport, Outport, and Signal Values

You must format the data as flattened
 arrays when you perform the following tasks with the LabVIEW Model Interface
 Toolkit VIs:

Setting inport values

Getting outport values

Getting signal values

In the following table each row represents a separate component of the same
 type, such as an inport, outport, or signal:

| Index in model | Value |
| --- | --- |
| 0 | 1 |
| 1 | [-0.777778, 0.5;-0.666667, 0] |
| 2 | 3 |

The Model Interface API represents these components with the following
 flattened 1D array in column-major order: [1, -0.777778, -0.666667, 0.5, 0,
 3].

#### Format of Vector Parameters

To set or get the value of a particular element within a 2D vector parameter, you
 must identify the offset of that specific element within the flattened 1D array that
 represents the vector. Consider the following 2 × 2 vector
 parameter:

[-0.777778, 0.5;

-0.666667,
 0]

The following table lists the offset values you use to
 identify each element in the parameter:

| Value | Column number | Row number | Offset within parameter |
| --- | --- | --- | --- |
| -0.777778 | 0 | 0 | 0 |
| 0.5 | 1 | 0 | 2 |
| -0.666667 | 0 | 1 | 1 |
| 0 | 1 | 1 | 3 |

Parent topic:

Basic Architecture for Executing Models

Related concepts:

- Probing Signal Values
- Initializing Parameter Values
- Updating Parameters While the Model Runs

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=probing-signal-values-model-interface-toolkit.html language=enus -->
## TOPIC 00017: Probing Signal Values

- bundle_id: `labview-model-interface-toolkit`
- source_path: `probing-signal-values-model-interface-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/probing-signal-values-model-interface-toolkit.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Probe signal values in a model using the Model Interface API, including signal buffering, formatting, and accessing values during execution. Signals in a model serve as probes, or test points, of a model as it runs. An outport connects to other parts of the application and must return data during ev

### Probing Signal Values

Probe signal values in a model using the Model Interface API, including signal
 buffering, formatting, and accessing values during execution.

Signals in a model serve as probes, or test points, of a model as it runs. An outport connects
 to other parts of the application and must return data during every time step.
 Applications do not need to read signal values at such a high priority. The Model
 Interface API provides VIs for accessing signal values in the background portion of your
 code.

The following block diagram shows the use of a Timed Loop that steps the
 model at a constant rate and a While Loop that reads signal
 values and displays them on the front panel:

Figure 9.

[IMAGE alt='Block diagram showing a Timed Loop for model stepping and a While Loop for reading and displaying signal values.' src='GUID-8E3DA453-465C-4E3F-A764-38F2F8EEC0EF-a5.gif']

Both loops run until an error occurs or the stop front panel control is
 TRUE.

The code performs the following steps:

1. Loads the model from disk.
2. Reads the compiled rate of the model in seconds, which is used to calculate the
 Timed Loop period.
3. Performs the following tasks to prepare the VI to read signal values:
  1. Returns an array of paths for all the signals in the model.
  2. Creates a Signal Interface reference that you pass to
 other VIs to define which signals to probe and to get values from the probed
 signals.
4. Defines the list of signals to probe in the Signal Paths 
 array. The Maximum Probed Data History input also configures
 the Model Interface API to store signal values from up to 100 model time steps in a
 buffer. Tip To improve performance in your
 application, only probe signals whose values you need. Avoid frequently changing
 the signals to probe. Probing many signals and frequently changing the signal
 list can both decrease performance.
5. Steps the model during each iteration of the Timed Loop . Reads and
 writes inports and outports. The Timed Loop iterates until an
 error occurs or the stop control is
 TRUE .
6. Returns the signal values from a specific model time step. The format of this output
 is a flattened 1D array that contains the values of each signal. Tip This VI contains a Simulation Time
 output. This output returns the elapsed time in the model, in seconds, when the
 model produced the current signal values. This value is useful for allowing you
 to correlate events within the model with the time they occurred.
7. When LabVIEW returns probed signal values before the timeout, the False case of the
 Case structure converts the array of signal values to a cluster and
 plots them in a waveform chart on the front panel.
8. Closes the reference to the signal-probe session. Unloads the model from memory, and
 handles any errors.

For an example code that demonstrates probing signal values, see the MIT Signal
 Probes VI in the labview\examples\Control and Simulation\Model
 Interface directory.

The Get Probed Signal Values VI returns signal values in the following
 formats, depending on which instance of the polymorphic VI you use:

Raw

Tip

Format Raw Signal
 Values

Formatted

Figure 10.

[IMAGE alt='A user interface showing signal paths and their corresponding probed data values.' src='GUID-B413F76D-16DE-4F6C-9521-2C796C91EDE1-a5.gif']

To change the signals that the Model Interface API is probing while the control loop steps the
 model, call the Set Signals to Probe VI again with the new list of
 signals. If any signal values from the previous signal list are still in the signal
 buffer, meaning the Get Probed Signal Values VI has not returned
 those values, the Model Interface API discards those values and immediately starts
 buffering values for the new signal list.

#### Storing
 Signal Values from Multiple Time Steps

Get Probed
 Signal Values

Get Probed Signal Values

Tip

Get Probed Signal Values

Maximum Probed Data History

Set
 Signals to Probe

Parent topic:

Basic Architecture for Executing Models

Related concepts:

- Manipulating Model Components in Flattened Format

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=relationship-to-veristand.html language=enus -->
## TOPIC 00018: Relationship to VeriStand

- bundle_id: `labview-model-interface-toolkit`
- source_path: `relationship-to-veristand.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/relationship-to-veristand.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the shared components of VeriStand and the LabVIEW Model Interface Toolkit for model compilation. The VeriStand real-time testing software and the LabVIEW Model Interface Toolkit share components that provide support for compiling models. VeriStand is a software environment for efficiently creat

### Relationship to VeriStand

Use the shared components of VeriStand and the LabVIEW Model Interface
 Toolkit
 for model compilation.

The VeriStand real-time testing software and the LabVIEW Model Interface
 Toolkit
 share components that provide support for compiling models.

VeriStand is a software environment for efficiently creating real-time testing
 applications. VeriStand helps you to configure a multicore-ready real-time engine to
 execute tasks such as real-time stimulus generation and data acquisition for high-speed
 and conditioned measurements.

Related concepts:

- Components of an Application
- Supported Model Types and Modeling Environments
- Troubleshooting the LabVIEW Model Interface Toolkit
- Basic Architecture for Executing Models
- Configuring Model Timing
- Initializing Parameter Values
- Updating Parameters While the Model Runs
- Probing Signal Values
- Troubleshooting Issues in Models
- Compiling Models
- Using Models from MathWorks Simulink
- Using C/C++ Models
- Using LabVIEW VIs as Models
- Where to Go Next

Related information:

- What is NI VeriStand?

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=supported-model-types-and-modeling-environmen.html language=enus -->
## TOPIC 00019: Supported Model Types and Modeling Environments

- bundle_id: `labview-model-interface-toolkit`
- source_path: `supported-model-types-and-modeling-environmen.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/supported-model-types-and-modeling-environmen.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Supported model types, compatibility considerations, and modeling environments for the LabVIEW Model Interface Toolkit. The following table describes LabVIEW Model Interface Toolkit support for common model types: 1 Supported Model Types Model Type Support Support Considerations MathWorks Simulink m

### Supported Model Types and Modeling
 Environments

Supported model types, compatibility considerations, and modeling environments for the
 LabVIEW Model Interface
 Toolkit.

The following table describes LabVIEW Model Interface
 Toolkit support for common
 model types:

| Model Type | Support | Support Considerations |
| --- | --- | --- |
| MathWorks Simulink model compiled using Simulink Coder and VeriStand Model Generation Support | Supported | Runs on the following target types in the specified compiled formats: Windows PC — .vsmodel NI Linux Real-Time targets — .vsmodel |
| Legacy MathWorks Simulink model compiled using Model Framework | Supported | Runs on the following target types in the specified compiled formats: Windows PC — .dll NI Linux Real-Time targets — .so |
| Uncompiled model from MathWorks Simulink software | Not supported | You must compile these models before you can use them with the Model Interface API. |
| C/C++ | Supported | For information on how to create and compile C/C++ models that are compatible with the VeriStand Model Framework, see VeriStand Model Framework Introduction section. You can find the section in the NI_VStand_Model_Framework_Guide.pdf file, in the C:\\VeriStand\\xxxx\\ModelInterface\\custom folder, where xxxx is the VeriStand version number. |
| FMU3For more information on FMI support and limitations, see FMI Support in the VeriStand User Manual. | Supported | You can load models conforming to FMI standard in LabVIEW Model Interface Toolkit. Runs on the following target types in the specified compiled formats: Windows PC — .fmu NI Linux Real-Time targets — .fmu |
| LabView VI compiled as a .lvmodel For more information on the versions of the LabVIEW, Windows, model compiler, and MathWorks software you can use with the LabVIEW Model Interface Toolkit, see the VeriStand Model Generation Support and MathWorks Simulink Compatibility knowledge base article at ni.com. | Supported | Runs on Windows PCs. |
| LabVIEW VI compiled as a .lvmodelso For more information on the versions of the LabVIEQ, Windows, model compiler, and MathWorks you can use with the LabVIEW Model Interface Toolkit, see the VeriStand Model Generation Support and MathWorks Simulink Compatibility knowledge base article at ni.com. | Supported | Runs on Linux x64. Note You must install additional software to enable LabView models for targets running a Linux Real-Time OS. x64 Intel-based cDAQ controllers running NI Linux Real-Time do not support the LabVIEW Model Interface Toolkit. |
| Compiled models from other environments | Supported | Several modeling environments can build compiled models that work with the VeriStand Model Framework. |
| Models compiled for use with the LabVIEW Simulation Interface Toolkit | Not supported | You must recompile these models before you can use them with the Model Interface API. |

#### Simulink
 Model Compatibility

In Simulink, you can convert models that use only a
 fixed step-size Ordinary Differential Equation (ODE) solver into compiled models.
 Additionally, you must turn off data logging in the Simulink.

Note

#### Troubleshooting Missing Options in Modeling Environments

If features for
 compiling models, such as the NIVeriStand.tlc—NI Real-Time
 Target system target file in Simulink, are missing, ensure all
 required NI components are installed. The LabVIEW Model Interface
 Toolkit
 does not install features for compiling models. However, the components that install
 this support are available from VeriStand.

Related concepts:

- Compiling a Model from MathWorks Simulink
- Generating Compiled Models from VIs
- Compiling Models

Related information:

- VeriStand Model Generation Support and MathWorks Simulink
 Compatibility
- FMI Support

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=troubleshooting-issues-in-models-model-interf.html language=enus -->
## TOPIC 00020: Troubleshooting Issues in Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `troubleshooting-issues-in-models-model-interf.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/troubleshooting-issues-in-models-model-interf.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Identify and resolve issues in models. If your model crashes or does not execute as you expect, try to isolate the issue and determine if its source is within the model or due to your LabVIEW code. Isolating the IssueTo identify the source of an issue, load and execute a simple model. If the simple

### Troubleshooting Issues in Models

Identify and resolve issues in models.

If your model crashes or does not execute as you expect, try to isolate the issue and
 determine if its source is within the model or due to your LabVIEW code.

#### Isolating the Issue

To identify the source of an issue, load and execute
 a simple model. If the simple model executes as expected, the source of the issue is
 likely within your model. However, if the simple model also experiences issues, the
 source of the issue might be due to the LabView code.

The following issues can
 occur when you run a model:

- The model crashes.
- The model does not run at expected rate.
- The performance decreases.

#### Problem: Model Crashes

Models often crash
 when an inport receives a value of 0 and the model attempts to divide by the inport
 value. Depending on your system, the following solutions might address this
 issue:

- Change the default value for the inport prior to stepping the model.
- Rewrite the model to remove the possibility of dividing by 0.

#### Problem: Model Runs Too Fast or Too
 Slow

If your model is unstable because it runs too fast or too slow,
 ensure the actual model rate matches the rate at which the model was compiled to
 run. If the rates do not match, adjust the period of the control loop that steps
 your model.

#### Problem: Decreased
 Performance

If you suspect that models cause your application to run
 slower than you desire, consider the following solutions that might improve
 performance:

- Only set parameter values in the control loop if you must update them during
 every time step. Instead, initialize the parameter values prior to running the
 control loop or set them in lower priority, background code.
- Probe only signals whose values you need. Probing many signals can have a
 negative impact on performance.
- Avoid changing the list of signals to probe frequently with the Set
 Signals to Probe VI.

Parent topic:

Troubleshooting the LabVIEW Model Interface Toolkit

Related concepts:

- Initializing Inport Values
- Configuring Model Timing

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=updating-parameters-while-the-model-runs-mode.html language=enus -->
## TOPIC 00021: Updating Parameters While the Model Runs

- bundle_id: `labview-model-interface-toolkit`
- source_path: `updating-parameters-while-the-model-runs-mode.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/updating-parameters-while-the-model-runs-mode.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Model Interface API to update model parameters programmatically during runtime. Many models have parameters, which act as variables in the model. The default values of parameters are compiled into the model. However, while a model runs in your application, you might want to adjust parameter

### Updating Parameters While the Model
 Runs

Use the Model Interface API to update model parameters programmatically during
 runtime.

Many models have parameters, which act as variables in the model. The default values of
 parameters are compiled into the model. However, while a model runs in your application,
 you might want to adjust parameter values to test the system response. In your
 application, use the Model Interface API to programmatically change parameter values at
 run time.

#### Methods of
 Updating Parameters

Updates to parameters are often lower priority than
 transferring data between model inports and outports and other parts of the
 application. Updates do not need to occur during every time step. For example, it is
 more critical for a model to receive the motor command from a controller by inport
 than to adjust parameters that affect the load on the motor.

Choose between
 the following methods for implementing code that sets parameters:

- With a lower priority than updates to inport and outports.
- With the same high priority as updating inports and outports.

#### Low-Priority Updates to
 Parameters

You can use the Model Interface API to set parameter values in a lower priority,
 background part of your application, such as a loop that runs when the high priority
 control loop finishes executing and sleeps. This design is useful because updating
 parameters in the control loop that steps your model can decrease performance of the
 application.

To set the value of a parameter outside the control loop,
 complete the following steps:

1. Set the new values.
2. Commit the new values.

This process is similar to the process for initializing parameters.

The
 following block diagram shows the use of a Timed Loop that
 steps the model at a constant rate and a While Loop that
 updates parameter values:

Figure 7.

[IMAGE alt='Block diagram showing a Timed Loop for stepping the model and a While Loop for updating parameters.' src='GUID-DE72FDF7-CE8D-43BE-AEDA-CCB4D81A9CC6-a5.gif']

Both loops run until an error occurs or the stop front
 panel control is TRUE.

The code performs the following
 steps:

1. Loads the model from disk.
2. Reads the compiled rate of the model in seconds, which is used to calculate the
 Timed Loop period.
3. Creates a Parameter Interface reference. Pass the reference
 to other VIs to get and set model parameters.
4. Steps the model during each iteration of the Timed Loop .
 Reads and writes inports and outports. The Timed Loop 
 iterates until an error occurs or the stop control is
 TRUE .
5. Runs when the Timed Loop sleeps to
 set the value of a scalar parameter whose index is 0 among all the model
 parameters. Tip You also can use the
 Set Parameter VI to set one element of a vector
 parameter or an entire vector parameter.
6. Applies the new value to the model when the Apply Changes
 Boolean control is TRUE . Until the
 Commit Parameters VI runs, any values you set in step 5 are not applied. Therefore, you can set multiple
 new values and only set the latest value with the Commit
 Parameters VI.
7. Closes the reference to the parameter-update session. Unloads the model from
 memory and handles any errors.

For an example code that demonstrates updating parameter values, see
 MIT Parameter Management VI in the
 labview\examples\Control and Simulation\Model
 Interface.

#### High-Priority Updates to Scalar
 Parameters

To ensure that the model receives updates to parameter values during the same time
 step that you set them, you can update parameter values in the same control loop
 that steps your model. However, be aware that frequently calling this VI can
 decrease the performance of the control loop.

Figure 8.

[IMAGE alt='A LabView block diagram showing a timed loop for updating scalar parameters in a control loop.' src='GUID-E80C4092-A4CC-4EAC-BDE9-0BBD9AE656B8-a5.gif']

The code performs the following steps:

1. Loads the model from disk.
2. Reads the compiled rate of the model in seconds, which is used to calculate the
 Timed Loop period.
3. Sets the Update Parameters Inline property to TRUE so
 that you can access parameters in the same loop that steps the model. If this
 property is FALSE (default), meaning you can update parameters
 only outside the control loop, LabVIEW returns error code -383700 when the
 Set Parameter Inline VI runs. Note Within an application, you can either set parameters
 inline with time steps or set them in code outside the control loop. You
 cannot use both methods simultaneously.
4. Sets the value of a scalar parameter whose index is 0 among all the model
 parameters. Note For illustration
 purposes, the Set Parameter Inline VI runs during
 every iteration of the Timed Loop. In a
 real-world application, you might want to implement this code so that
 the VI runs only when you want to set a new parameter value.The
 Set Parameter Inline VI allows you to set new
 parameter values only for scalar parameters or for a single element of a
 vector parameter. You cannot set an entire vector parameter or get any
 parameter values inline.
5. Steps the model and reads and writes inports and outports. The Timed
 Loop iterates until an error occurs or the
 stop control is TRUE .
6. Unloads the model from memory and handles any errors.

Note

#### Making Background and Inline
 Updates to Parameters

If you want to make background updates to parameter values in one part of your code
 and also make inline updates in the control loop, you can switch the value of the
 Update Parameters Inline property. For example, you might
 want to initialize parameter values prior to stepping your model, and then change
 the values as the model executes.

#### Getting and Setting Elements in
 Vector Parameters

In addition to getting and setting scalar parameters, the following VIs allow you to
 update a single element of a vector parameter:

- Get Parameter
- Set Parameter
- Set Parameter Inline

To identify the specific element of the vector to update, specify the position
 of the element within the parameter by the Offset within
 parameter input of these VIs. Consider the following guidelines to
 determine the correct value for this input:

- If the vector has one dimension, the offset of an element is zero-based.
- If the vector has two dimensions, the Model Interface API treats the parameter
 as a flattened 1D array in column-major order. You can use the
 Calculate Parameter Offset VI to return the offset of a
 particular element within the flattened array.

Parent topic:

Basic Architecture for Executing Models

Related concepts:

- Manipulating Model Components in Flattened Format
- Initializing Parameter Values

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00022: LabVIEW Model Interface Toolkit User Manual

- bundle_id: `labview-model-interface-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Model Interface Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Infor

### LabVIEW Model Interface
 Toolkit
 User Manual

The LabVIEW Model Interface
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=using-c-c-models-model-interface-toolkit.html language=enus -->
## TOPIC 00023: Using C/C++ Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `using-c-c-models-model-interface-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/using-c-c-models-model-interface-toolkit.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Model Interface API supports running C/C++ models compiled into .dll, .out, or .so formats with the VeriStand Model Framework. The Model Interface API can run models you create in C/C++ and compile into one of the following formats: .dll .out .so The models must be designed and compiled to work

### Using C/C++ Models

The Model Interface API supports running C/C++ models compiled into
 .dll, .out, or .so
 formats with the VeriStand Model Framework.

The Model Interface API can run models you create in C/C++ and compile into one of the
 following formats:

- .dll
- .out
- .so

The models must be designed and compiled to work with the VeriStand Model Framework.

For more information on creating and compiling C/C++ models that are compatible with the
 VeriStand Model Framework, see the
 NI_VStand_Model_Framework_Guide.pdf guide. You can find the
 guide in the
 RootDrive:\VeriStand\xxxx\ModelInterface\custom
 directory, where RootDrive is the drive where the software installs.
 xxxx is the VeriStand version number. The guide describes the
 following topics:

- Components of the VeriStand Model Framework
- Process for creating model code that is compatible with the framework
- Requirements for compiling your model with the framework

Parent topic:

Compiling Models

Related concepts:

- Compiling Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=using-fmu-models.html language=enus -->
## TOPIC 00024: Using FMU Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `using-fmu-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/using-fmu-models.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The section explains the Functional Mock-up Interface (FMI) standard, its model interaction patterns, and platform support for Functional Mockup Units (FMUs). The Functional Mock-up Interface (FMI) is an API standardization for exchanging dynamic system models. You can use FMI to decouple modeling e

### Using FMU Models

The section explains the Functional Mock-up Interface (FMI) standard, its model
 interaction patterns, and platform support for Functional Mockup Units (FMUs).

The Functional Mock-up Interface (FMI) is an API standardization for exchanging dynamic
 system models. You can use FMI to decouple modeling environments from model consumers.
 This decoupling helps create tool-agnostic, portable solutions between the modeling and
 the simulation environments. For more information, refer to the FMI website.

The LabVIEW Model Interface Toolkit allows for configuration and execution of FMI 2.0 and
 FMI 3.0 CoSimulation models on Microsoft Windows and Real-Time Linux 64-bit systems.

The FMI standard defines the following model interaction patterns:

Model Exchange

Co-Simulation

Scheduled Execution

FMI also defines the distribution packaging of the model. FMI decouples the interface
 description from the actual model binaries. A model that implements this interface is
 called a Functional Mockup Unit (FMU). For example, you can have support for the
 following platforms:

- Windows 64-bit
- Linux 64-bit
- The source code in the same package

Parent topic:

Compiling Models

Related information:

- FMI Support
- FMI Website

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=using-labview-vis-as-models-model-interface-t.html language=enus -->
## TOPIC 00025: Using LabVIEW VIs as Models

- bundle_id: `labview-model-interface-toolkit`
- source_path: `using-labview-vis-as-models-model-interface-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/using-labview-vis-as-models-model-interface-t.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Convert LabVIEW VIs into compiled models for use with the LabVIEW Model Interface Toolkit or VeriStand systems. You can convert other LabVIEW VIs into compiled .lvmodel or .lvmodelso files that the Model Interface API can run. This might be useful if you want to distribute the .lvmodel or .lvmodelso

### Using LabVIEW VIs as Models

Convert LabVIEW VIs into compiled models for use with the LabVIEW Model Interface
 Toolkit or VeriStand systems.

You can convert other LabVIEW VIs into compiled .lvmodel or
 .lvmodelso files that the Model Interface API can run. This
 might be useful if you want to distribute the .lvmodel or
 .lvmodelso to other users to work with in the LabVIEW Model Interface
 Toolkit or VeriStand systems. You can convert LabVIEW
 VIs and simulation subsystems you create using the LabVIEW Control Design and Simulation
 Module. The following sections describe how the Model Interface API supports these
 models.

Note

.lvmodelso

#### Verifying That LabView Model Support is Installed

To compile models in
 LabVIEW, you must install the LabVIEW Model Support feature, available from
 VeriStand.

#### Verifying Support for Your Hardware Target

Before you convert a LabVIEW
 VI into a compiled .lvmodel or .lvmodelso,
 answer the following questions to determine whether your target supports these
 models:

Do you want to run the model on a Windows computer or an RT target?

Windows

.lvmodel

RT

What RTOS does my RT target run?

Real-Time Controllers and Real-Time Operating System
 Compatibility

ni.com

.lvmodel

.lvmodelso

.lvmodelso

#### Preparing VIs to be Converted to Models

In the source VI to be compiled,
 you must assign front panel controls and indicators in VIs to the connector pane.
 Then, the Model Interface API can identify panel controls when it loads the compiled
 .lvmodel or .lvmodelso files as the
 following elements:

- Inports
- Outports
- Parameters

The following table describes how to build the VI connector pane with custom
 controls and indicators to work with VeriStand:

| Desired Component in Test Application | VI Connector Pane Assignment | Is Default Value Maintained? |
| --- | --- | --- |
| Inport | Required input | No |
| Outport | Any output | No |
| Parameter | Optional or Recommended input | Yes |

#### Supported Data Types

Ensure that front panel controls or indicators assigned to the VI connector pane have
 only the following data types:

- Numerics
- Booleans
- 1D arrays of numerics
- 1D arrays of Booleans
- Clusters containing the previous data types

If you use an unsupported data type, LabVIEW returns an error when you try to convert
 the VI to a compiled .lvmodel or
 .lvmodelso file. Controls and indicators that are not
 assigned to the connector pane might have other data types because these objects are
 not part of the compiled model.

#### Configuring Global and Local
 Parameters

A compiled .lvmodel or .lvmodelso might
 contain two types of parameters:

Local, or block, parameters

.lvmodel

.lvmodelso

Model Name

Cluster
 Name

Parameter Name

Global parameters

Model Name

Parameter
 Name

Tip

Get Paths

A .lvmodel or .lvmodelso file can contain
 both local and global parameters.

#### Considerations for VIs with Array
 Terminals

If a VI contains an array control or indicator you want to include in the
 .lvmodel or .lvmodelso, enter a value
 in the n<sup>th</sup> element of the array, where
 n is the desired number of elements. Then, right-click the
 array control and select Data Operations»Make Current Value Default. Otherwise, the array becomes a single scalar value when the Model
 Interface API loads the model.

Parent topic:

Compiling Models

Related concepts:

- Compiling Models
- Generating Compiled Models from VIs

Related information:

- Real-Time Controllers and Real-Time Operating System
 Compatibility

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=using-model-interface-vis-in-the-control-loop.html language=enus -->
## TOPIC 00026: Using Model Interface VIs in the Control Loop

- bundle_id: `labview-model-interface-toolkit`
- source_path: `using-model-interface-vis-in-the-control-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/using-model-interface-vis-in-the-control-loop.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Identify LabVIEW Model Interface Toolkit VIs suitable for use in time-critical control loops and those that might affect determinism. When you design your application, certain LabVIEW Model Interface Toolkit VIs are suitable for use in the control loop that steps your model. Others are not suitable

### Using Model Interface VIs in the Control Loop

Identify LabVIEW Model Interface
 Toolkit VIs suitable for use in
 time-critical control loops and those that might affect determinism.

When you design your application, certain LabVIEW Model Interface
 Toolkit VIs
 are suitable for use in the control loop that steps your model. Others are not suitable
 due to their effect on jitter and determinism. The following VIs are suitable for use in
 a time-critical VI or timed structure that runs on an Real-Time (RT) target:

- Take Model Time Step
- Get Simulation Time
- Set Parameter Inline

Avoid using the following VIs in the model control loop if determinism is an important
 consideration in your application:

- Calculate Parameter Offset
- Commit Parameter
- Create Inport Array
- Create Parameter Interface
- Create Signal Interface
- Get Information by Path
- Get Probed Signal Values
- Get Parameters
- Set Parameter
- Set Signals to Probe

Parent topic:

Basic Architecture for Executing Models

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=using-models-from-mathworks-simulink-software.html language=enus -->
## TOPIC 00027: Using Models from MathWorks Simulink

- bundle_id: `labview-model-interface-toolkit`
- source_path: `using-models-from-mathworks-simulink-software.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/using-models-from-mathworks-simulink-software.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Integrate MathWorks Simulink models with the Model Interface API by compiling them into supported formats for real-time targets. You can use your model you created in MathWorks Simulink with the Model Interface API. However, first you must compile the model into one of the following formats: .dll .o

### Using Models from MathWorks
 Simulink

Integrate MathWorks Simulink models with the Model Interface API by compiling them
 into supported formats for real-time targets.

You can use your model you created in MathWorks Simulink with the Model Interface API.
 However, first you must compile the model into one of the following formats:

- .dll
- .out
- .so

#### Overview of Compiling Simulink Models

The following illustration shows
 the typical workflow for compiling and integrating a Simulink model in a LabVIEW Model Interface
 Toolkit application:

[IMAGE alt='image' src='GUID-4AFF1861-5A05-45C5-A7BF-0B141930E5C4-a5.gif']

Green boxes ([IMAGE alt='A green box representing a step in the Simulink model compilation workflow.' src='GUID-440574CB-0364-4690-90F3-75606A0F8282-a5.gif']) indicate that you must complete the step in the MathWorks. Blue
 boxes ([IMAGE alt='A blue box representing a step in the Simulink model compilation workflow.' src='GUID-553FCB52-A40E-473B-BE1A-DE0AF9D2F754-a5.gif']) indicate that you must complete the step in LabVIEW.

Use
 Simulink to convert your model for use on real-time targets.

Depending on your
 version of MathWorks Simulink, use one of the following resources to compile your
 model:

| Simulink Version | Resource |
| --- | --- |
| R2017b to R2020b | VeriStand Model Framework |
| R2020a and newer | VeriStand Model Generation Support MATLAB Addon |

Parent topic:

Compiling Models

Related concepts:

- Supported Model Types and Modeling Environments
- Considerations for Integrating Models from MathWorks Simulink
- Compiling a Model from MathWorks Simulink

<!--NI_TOPIC bundle=labview-model-interface-toolkit path=where-to-go-next-model-interface-toolkit.html language=enus -->
## TOPIC 00028: Where to Go Next

- bundle_id: `labview-model-interface-toolkit`
- source_path: `where-to-go-next-model-interface-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit/raw/resource/enus/where-to-go-next-model-interface-toolkit.html
- document_id: `labview-model-interface-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resources for building applications in LabVIEW. Refer to the following resources as you continue building your application in LabVIEW: To browse example code that demonstrates various uses of the Model Interface API, select Help Find Examples in LabVIEW to launch the Example Finder. Navigate to the

### Where to Go Next

Resources for building applications in LabVIEW.

Refer to the following resources as you continue building your application in
 LabVIEW:

To browse example code that demonstrates various uses of the Model Interface API, select Help»Find Examples in LabVIEW to launch the Example Finder. Navigate to the
 Toolkits and Modules folder. To find the examples on disk,
 you can browse to the labview\examples\Control and Simulation\Model
 Interface directory. You can modify an example VI to fit an application,
 or you can copy and paste from one or more examples into a VI that you create.

#### Integrating Device I/O

To read data from a hardware device and write it
 to a model inport or write data from a model inport to a hardware device, use driver
 VIs written for the device. For example, you can use the NI-DAQmx VIs to communicate
 with a DAQ device in your test application. After you install a LabVIEW add-on such
 as a module, toolkit, or driver, the documentation for that add-on appears in a
 separate help system you can access by selecting Help»Add-On Help, where Add-On Help is the name of the separate
 help system for the add-on.

#### Optimizing an Application to Run on an RT Target

If your application
 includes a VI that runs on an Real-Time (RT) target and VIs that run on the host
 system, choose from available remote-communication methods. For more information on
 communication methods, see *Exploring Remote Communication
 Methods*.

Developing complex LabVIEW Real-Time applications requires an
 understanding of how LabVIEW maps to the real-time computing model. Some LabVIEW
 programming strategies that work well when developing for a general-purpose
 operating system do not translate to the headless, priority-driven execution model
 of a Real-Time Operating System (RTOS). For best practices for designing,
 developing, and deploying applications with the LabVIEW Real-Time Module, see
 *Real-Time Module Best Practices*.

The LabVIEW Real-Time Module
 and other LabVIEW add-ons add functionality to the LabVIEW development system and
 must be purchased separately. For more information, see the specific module
 documentation on that product.

#### Distributing an Application

You must use a LabVIEW project to build
 stand-alone applications that you can distribute and deploy or download files to RT
 targets. You also must use a project to work with a Windows Embedded Standard, RT,
 FPGA, or Touch Panel target. For more information, see *Building and Deploying
 a Stand-Alone Real-Time Application*.

Related information:

- Exploring Remote Communication Methods
- Real-Time Module Best Practices
- Building and Deploying a Stand-Alone Real-Time
 Application
