# NI DOCUMENT BUNDLE: labview-model-interface-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-model-interface-toolkit-api-ref start=1 end=54 -->
<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_basic_design.html language=enus -->
## TOPIC 00001: Basic Architecture for Executing Models (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_basic_design.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_basic_design.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Basic Architecture for Executing Models (Model Interface Toolkit)

The Model Interface API allows you to integrate and run models in LabVIEW control systems. In many applications, timing is an important consideration in application design because you want time steps to repeat according to specific timing characteristics or to synchronize model execution with the clock of a hardware device. To ensure LabVIEW runs a model reliably, you can separate your code into at least two components:

- A high-priority control loop —Executes one time step, first writing to model inports, and then reading from outports.
- Lower priority/background code —Executes when the control loop sleeps after completing execution. This code might get and set parameter values or read values from signals in the model.

Prior to the control loop of your code, you can perform initialization-related tasks, such as loading the model and initializing parameter values. After the control loop and background code stop executing, you unload the model and close any references you opened.

#### Example: Simple Model Control Application

The following block diagram shows a simple VI that uses the Model Interface API to load the model, execute the model indefinitely in a control loop, set a parameter value in background-priority code, and unload the model.

[IMAGE alt='image' src='loc_bd_load_run_mit.gif']

|  | Loads the model from disk and creates a model reference you pass to other VIs throughout the application to run and interact with the model. Note Avoid branching the model reference wire to ensure optimal performance. The Model Interface API is not designed to operate on a model in parallel locations. |
| --- | --- |
|  | Note Avoid branching the model reference wire to ensure optimal performance. The Model Interface API is not designed to operate on a model in parallel locations. |
|  | Reads the compiled rate of the model in seconds and sets the period of the Timed Loop. Each iteration of the Timed Loop must complete execution before the specified period. This example converts seconds to milliseconds because the Period input of the Timed Loop expects values in the same units as the 1 kHz clock timing source the loop is configured to use. |
|  | Performs the following tasks during each iteration of the high-priority control loop: Writes a value of 0 to the only model inport. Note This example applies the same inport value during every time step. This might be typical of applications in which you want to observe the model response to a particular stimulus. However, in hardware-in-the-loop applications, dynamic inport values might come from hardware I/O, such as channels on a DAQ device. In other applications, you might allow users to manipulate inport values via front-panel controls. Steps the model during each iteration of the Timed Loop. The Timed Loop iterates until an error occurs or the stop control is TRUE. Displays the value of the model outport in a waveform chart on the front panel. |
|  | Note This example applies the same inport value during every time step. This might be typical of applications in which you want to observe the model response to a particular stimulus. However, in hardware-in-the-loop applications, dynamic inport values might come from hardware I/O, such as channels on a DAQ device. In other applications, you might allow users to manipulate inport values via front-panel controls. |
|  | Sets the value of a parameter when the control loop sleeps. This loop is typical of background-priority code. |
|  | Unloads the model and handles any errors that occurred. |

In this example, the control loop transfers data between the model and front panel controls and indicators. A real-world application might contain features such as:

- A model with multiple inports, outports, parameters, and signals
- Hardware device driver VIs that read data from or write data to hardware I/O
- Multiple models

Refer to the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates various uses of the Model Interface API.

##### Related Links

[Selecting a Timing Source for a Timed Structure](/csh?topicname=lvconcepts/con_select_timed_struct_timing.html)

[Initializing Parameter Values](mit_model_params_init.html)

[Updating Parameters While the Model Runs](mit_model_params_run.html)

[Probing Signal Values](mit_model_signals.html)

#### Choosing the Right Type of Control Loop

When you design the control-loop portion of your application, choose between using a Timed Loop or a While Loop to repeatedly step the model:

- Use a Timed Loop when:
  - You want your code to repeat according to specific timing characteristics, such as at a guaranteed rate. Timed Loops provide features that help you ensure that the model executes deterministically, with each time step finishing on time, every time.
  - You want the model execution code to run at a higher priority than other code whose timing characteristics are less critical.
  - You want to synchronize the control loop with the clock of a hardware device. For example, if you want to pass data from a DAQ device into a model, a Timed Loop can use an external signal on the DAQ device to control its timing.
- Use a While Loop when you do not need precise timing abilities or deterministic execution. While Loops might be appropriate if you want to run your application on a general-purpose operating system, such as Windows, that does not guarantee real-time performance.

##### Related Links

[Timed Loop](/csh?topicname=glang/timed_loop.html)

[While Loop](/csh?topicname=glang/while_loop.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_convert_model_to_dll.html language=enus -->
## TOPIC 00002: Compiling a Model from MathWorks Simulink® Software (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_convert_model_to_dll.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_convert_model_to_dll.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Compiling a Model from MathWorks Simulink® Software (Model Interface Toolkit)

Complete the following steps to convert your model you created in MathWorks Simulink[®](/csh?topicname=lvhelp/trademarks.html) software into a compiled model that the Model Interface API can run.

|  | Note Before you complete this procedure, ensure your models are configured to interact with the Model Interface API the way you want. |
| --- | --- |

#### 1. Verify That the VeriStand Model Framework Is Installed

The VeriStand Model Framework must be installed on the computer with the Simulink software. The VeriStand Model Framework adds tools to the Simulink software that you use later in this procedure. [More information](mit_shared_components.html).

#### 2. Ensure You Have the Correct Compiler

Answer the following questions to determine which tools you must use to convert and compile Simulink models:

1. What real-time operating system (RTOS) does my target run? Refer to the following KnowledgeBase at ni.com for a list of RT targets and the RTOS that each runs, then continue to step 2: What Operating System is my Real-Time Controller Running and Why? (Windows) If you want to create a compiled model that runs on Windows, just continue to step 2.
2. Given the OS my target runs, what tools do I use to compile my model and what output do I create? 
 OS
Required Tools
Required Output Type
Windows
Microsoft Visual C++
MathWorks Simulink ® Coder ™ software
[IMAGE alt='image' src='note.gif']
**Note** VeriStand 2015 also supports the older version of the Simulink Coder, called the Real-Time Workshop ®.
DLL
Phar Lap ETS
NI Linux Real-Time
C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition
MathWorks Simulink Coder software
.so
3. Which versions of these tools are compatible with the version of the Model Interface Toolkit I am using? Refer to the following KnowledgeBase document at ni.com for a list of the versions of the LabVIEW, Windows, model compiler, and MathWorks software you can use with the Model Interface Toolkit: VeriStand Version Compatibility.

##### Related Links

- KnowledgeBase at ni.com : Setting up MathWorks MATLAB® Software to Create a VeriStand Compatible DLL
- KnowledgeBase at ni.com : Generating Models from MathWorks Simulink® Simulation Software for Deployment on NI Linux Real-Time Systems

|  | Note The Model Interface Toolkit shares several components with the VeriStand software, such as tools for compiling models designed in third-party modeling environments. |
| --- | --- |

#### 3. Select the Correct Compiler in MATLAB

- (Phar Lap ETS, Windows) Run mex -setup in the MATLAB software and select the option number for a compatible version of Microsoft Visual C++.
- (NI Linux Real-Time) Go to the next section. You do not need to select a compiler for NI Linux Real-Time when you install C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition.

#### 4. Build the Compiled Model in Simulink

After you have the correct compiler set up and selected, complete the following steps to build the compiled model:

1. Launch the Simulink software and load your model you want to convert.
2. Select Simulation»Model Configuration Parameters to launch the Model Configuration Parameters dialog box.
3. Click the Solver tab and configure the following options:
  - Stop time : inf
  - Type : Fixed-step
4. Click the Code Generation tab.
5. Click the Browse button to launch the System Target File Browser dialog box.
6. Select the correct option for your target from the list:
 
 [IMAGE alt='image' src='note.gif']
**Note** If the appropriate .tlc is not visible, the MATLAB software files might be read-only, and the Model Interface Toolkit installer is not able to provide this option. To display the option, add the following lines to the matlabrc.m file, a file that is installed by the MATLAB software:
 addpath('*X*:\VeriStand'); 
 NIVeriStandAddPaths;
 
 
where *X* is the drive letter on which you installed the VeriStand Model Framework.
 
 
The Model Interface Toolkit shares several components with the VeriStand software, such as tools for compiling models designed in third-party modeling environments.
  - (ETS, Windows) NIVeriStand.tlc—NI Real-Time Target
  - (NI Linux Real-Time)
    - (ARM-based targets) NIVeriStand_Linux_ARM_32.tlc—NI Real-Time Target
    - (Intel x64-based targets) NIVeriStand_Linux_64.tlc—NI Real-Time Target 
 [IMAGE alt='image' src='note.gif']
**Note** The Model Interface Toolkit is not supported on x64 Intel-based cDAQ controllers running NI Linux Real-Time.
7. Click the OK button.
8. Click the Build button in the Category section to begin building the compiled model. The MATLAB software command window displays the status of the build process. The following message in the MATLAB command window indicates that the Simulink Coder software has completed building the compiled model. ### Successful completion of build procedure for model: *ModelName*

#### Including External Source Code in the Compiled Model

If your model you are converting specifies any .c or .h files, you must specify the locations of these files so they are included in the compiled model. Specify the source files and include directories in the Simulink software, on the **Code Generation** tab of the **Configuration Parameters** dialog box.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_error_codes.html language=enus -->
## TOPIC 00003: Error Codes (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_error_codes.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Model Interface Toolkit)

The LabVIEW Model Interface Toolkit can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in the Model Interface Toolkit.

| Code | Description |
| --- | --- |
| -383251 | Support for multirate models requires the NI VeriStand 2013 Model Framework requires version 2013.0.1.0 or later. Recompile your model using the appropriate version of the NI VeriStand Model Framework. |
| −383700 | Operation on a parameter is incompatible with the Update Parameters In Line? property. 1) Cannot set a parameter in line when this property is FALSE. 2) Cannot get/set a parameter in background-priority code when this property is TRUE. Correct the value of this property to match the type of parameter operation you want to perform. |
| −383250 | In multirate models, total number of subsystems with different rates exceeds maximum number allowed. Edit the model(s) to reduce the number of subsystems with different rates, and then rebuild the model(s). |
| −383204 | Index is out of bounds. |
| −383203 | Cannot start the model because the model has already been started. |
| −383202 | Model error. |
| −383201 | The reference to the model is invalid. Ensure you pass a valid model reference to this VI. |
| −383200 | Cannot load model. Ensure the Model Library Path is valid and the model conforms to the NI VeriStand Model Framework header file (NIVERISTAND_API.h). |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_finding_comps.html language=enus -->
## TOPIC 00004: Finding the Components of a Model (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_finding_comps.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_finding_comps.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Finding the Components of a Model (Model Interface Toolkit)

If you receive a model you did not create, you might need to identify its inports, outports, parameters, and signals before you can work with the model. Complete the following steps to create a simple VI that returns information about the components of a model:

1. Load the model using the Load Model VI.
2. Call the Get Paths VI to return the paths of components within the model you loaded.
3. Call the Get Information by Path VI to return more information about the component at the path you specify, such as its name, dimension, and default value.

##### Related Links

[Get Paths VI](../vsmitref/get_paths.html)

[Get Information by Path VI](../vsmitref/get_information_by_path.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_flattened_arrays.html language=enus -->
## TOPIC 00005: Manipulating Model Components in Flattened Format (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_flattened_arrays.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_flattened_arrays.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Manipulating Model Components in Flattened Format (Model Interface Toolkit)

When you use the Model Interface VIs to transfer data to model components, such as inports and parameters, in several cases you must format the data as flattened 1D arrays of values in column-major order.

#### Format of Inport, Outport, and Signal Values

When you perform the following tasks with the Model Interface VIs, you must format the data as flattened arrays:

- Setting inport values —You specify all inport values in a flattened array.
- Getting outport values —LabVIEW returns all outport values in a flattened array.
- Getting signal values —LabVIEW returns all signal values from a particular time step in a flattened array.

Consider the following table, where each row represents a separate component of the same type, such as an inport, outport, or signal.

| Index in model | Value |
| --- | --- |
| 0 | 1 |
| 1 | [-0.777778, 0.5;-0.666667, 0] |
| 2 | 3 |

The Model Interface API represents these components with the following flattened 1D array in column-major order:

[1, -0.777778, -0.666667, 0.5, 0, 3]

##### Related Links

[Probing Signal Values](mit_model_signals.html)

#### Format of Vector Parameters

To set or get the value of a particular element within a 2D vector parameter, you must identify the offset of that specific element within the flattened 1D array that represents the vector. Consider the following 2 × 2 vector parameter:

[-0.777778, 0.5;

-0.666667, 0]

The following table lists the offset values you use to identify each element in the parameter.

| Value | Column number | Row number | Offset within parameter |
| --- | --- | --- | --- |
| -0.777778 | 0 | 0 | 0 |
| 0.5 | 1 | 0 | 2 |
| -0.666667 | 0 | 1 | 1 |
| 0 | 1 | 1 | 3 |

##### Related Links

[Initializing Parameter Values](mit_model_params_init.html)

[Updating Parameters While the Model Runs](mit_model_params_run.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_gen_vs_model.html language=enus -->
## TOPIC 00006: Generating Compiled Models from VIs (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_gen_vs_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_gen_vs_model.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Compiled Models from VIs (Model Interface Toolkit)

You can convert LabVIEW VIs into compiled models you can run with the Model Interface API. If you have the Control Design and Simulation Module installed, you also can convert simulation subsystems.

#### Prerequisite Software

Before you can compile models in LabVIEW, you must install the following software components:

- The LabVIEW Model Support feature, available on the VeriStand DVD you receive with your purchase. More information .
- The LabVIEW Application Builder, which is included with the LabVIEW Professional Development System. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder separately.

#### Generating a Compiled Model

Complete the following steps to generate a compiled .lvmodel or .lvmodelso you can use with the Model Interface API:

|  | Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS (.lvmodelso files). For more information about how to use LabVIEW models with Linux, visit the NI website. |
| --- | --- |

1. Create a VI or simulation subsystem that performs the actions you require from your simulation model.
2. Configure the connector pane for your VI or subsystem using guidelines for preparing VIs to be converted to a compiled model.
3. Save the VI or subsystem.
4. In LabVIEW, select Tools»VeriStand»Generate Model from VI to display the Generate Model from VI dialog box.
 [IMAGE alt='image' src='note.gif']
**Note** The Model Interface Toolkit shares several components with the VeriStand software, such as tools for compiling models.
5. In the Source VI Path field, enter the path where you saved the source file.
6. In the Destination Folder field, enter the path where you want to save the generated model.
7. (Control Design and Simulation Module) If your source file is a simulation subsystem, click the Next button and complete the following steps.
  1. Specify a value for the model time step (sec) , which is the interval between the times the ODE Solver evaluates the model and updates the model output, in seconds. For your compiled model to run in real-time, the model time step (sec) value must equal the controller period multiplied by the model Decimation , or the model Decimation divided by the Target Rate :
 model time step (sec) = Controller Period * Decimation 
 or
 model time step (sec) = Decimation / Target Rate 
 where Controller Period = 1 / Target Rate . You specify the Target Rate on the Controller Configuration page of the System Explorer window. You specify the Decimation on the Model Configuration page of the System Explorer window.
 [IMAGE alt='image' src='note.gif']
**Note** Because there is no simulated time in a standard VI, the previous equation applies only to compiled models you generate from simulation subsystems.
  2. Specify the ODE Solver .
8. Click the Build button. The Generate Model from VI dialog box displays the progress of the model generation.
 [IMAGE alt='image' src='note.gif']
**Note** If you experience errors when converting a VI or if the model does not contain the inports, outports, and parameters you expect, refer to the guidelines for [preparing VIs to be converted to a compiled model](mit_model_from_lv.html#prep).

#### Moving the Model and Support Files

If you deploy the compiled .lvmodel or .lvmodelso to an RT target, LabVIEW copies required DLLs to the target automatically. However, if you manually copy the .lvmodel or .lvmodelso file to a new location, such as a different host computer, you also must move any LabVIEW DLLs, such as NILVSim.dll for a simulation subsystem, located in a subdirectory named data in the destination folder where LabVIEW generates the compiled model.

##### Related Information

[Using LabVIEW VIs as Models](mit_model_from_lv.html)

ni.com: Purchase the Application Builder

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_install_sw_rt.html language=enus -->
## TOPIC 00007: Installing Support on an RT Target (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_install_sw_rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_install_sw_rt.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Installing Support on an RT Target (Model Interface Toolkit)

To deploy VIs that contain the Model Interface API to an RT target, you must first download support files for the Model Interface Toolkit to the target.

|  | Note This topic assumes the RT target has network settings configured and has the LabVIEW Real-Time Module and any driver software, such as NI-RIO and NI-DAQmx, installed. If you need to perform these tasks, refer to the LabVIEW Real-Time Target Configuration topic in the Measurement & Automation Explorer Help, available by selecting Help»MAX Help from NI MAX. |
| --- | --- |

On a host computer with the Model Interface Toolkit installed, complete the following steps in NI MAX to download the support files:

1. Launch NI MAX from the Start menu or (Windows 8) from NI Launcher.
2. Complete the following steps to launch the LabVIEW Real-Time Software Wizard:
 
 [IMAGE alt='image' src='note.gif']
**Note** If a login password has been set, you might be prompted to enter the RT system's administrator name and password. For more information, refer to the *Logging into your System* topic in the *Measurement & Automation Explorer Help*.
  1. Expand Remote Systems in the configuration tree and then expand your RT target.
  2. Select Software .
  3. Click the Add/Remove Software icon on the toolbar to launch the LabVIEW Real-Time Software Wizard. If your target does not have a Software category, then it does not support the required software.
3. If prompted to install a recommended software set, select Custom software installation (currently installed) and click Next . Otherwise, proceed to the next step.
4. Click the icon next to the Model Interface Toolkit item, select Install the feature , and then click Next .
5. Confirm that you want to install Model Interface Toolkit support, and then click Next .

MAX displays the progress of the installation, and then reboots the target so it is ready for you to deploy files.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_compiling.html language=enus -->
## TOPIC 00008: Conversion Process for Models from MathWorks Simulink® Software (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_compiling.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_compiling.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Conversion Process for Models from MathWorks Simulink® Software (Model Interface Toolkit)

Before you can run a model you created in MathWorks Simulink[®](/csh?topicname=lvhelp/trademarks.html) software with the Model Interface API, you must use the Simulink software to convert the model file to a compiled model. The Simulink software performs the following process:

1. When you build the compiled model, MathWorks Real-Time Workshop® software converts your model and any submodels into a C/C++ code version of the same model. The resulting C/C++ code version of your model is the same Simulink block diagram model, just in a different form.
2. A compiler, such as Microsoft Visual C++, compiles the C/C++ code model into the appropriate file type. For example, the Microsoft Visual C++ compiler creates a file named *ModelName* .dll , *ModelName* .out , or *ModelName* .so , where *ModelName* is the name of the model.
 [IMAGE alt='image' src='note.gif']
**Note** Shared libraries used by LabVIEW VIs must exist in either the ni-rt/ or the ni-rt/system/ directory. LabVIEW ignores paths specified in the Call Library Node.
3. The Real-Time Workshop software places the compiled model file in one of the following directories located in the current working directory:
 
 [IMAGE alt='image' src='note.gif']
**Note** A text file, <*ModelName*>_portsReadme.txt, is also generated, which specifies the lengths and positions of all model inport and outport array data.
  - (Phar Lap ETS) < *ModelName* > _NIVeriStand_rtw
  - (NI Linux Real-Time) < *ModelName* > _NIVeriStand_Linux_ARM_32_rtw or *ModelName* > _NIVeriStand_Linux_64_rtw

The following figure shows this conversion process.

[IMAGE alt='image' src='loc_eps_converttocompiledmodel.gif']

The tools you use to convert a Simulink model, such as Microsoft Visual C++ and the GNU Toolchain, differ according to the type of target that will run the model. However, the previous conversion process is generally the same across targets. Refer to the following KnowledgeBase document at ni.com for a list of the versions of the LabVIEW, Windows, model compiler, and MathWorks software you can use with the Model Interface Toolkit: VeriStand Version Compatibility.

#### Prerequisites for Compilation

To compile a Simulink model, the VeriStand Model Framework must be installed on the computer with the Simulink software. The VeriStand Model Framework adds tools to the Simulink software that allow you to compile models that work with the Model Interface API.

##### Related Links

[Compiling a Model from MathWorks Simulink Software](mit_convert_model_to_dll.html)

[VeriStand Model Framework](mit_shared_components.html#model_framework)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_debugging.html language=enus -->
## TOPIC 00009: Troubleshooting Issues in Models (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_debugging.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_debugging.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Troubleshooting Issues in Models (Model Interface Toolkit)

If your model crashes or does not execute as you expect, try to isolate the issue and determine if its source is within the model or due to your LabVIEW code.

#### Isolating the Issue

To identify the source of an issue, load and execute a simple model. If the simple model executes as expected, the source of the issue is likely within your model. However, if the simple model also experiences issues, the source of the issue might be due to the LabVIEW code.

The following issues can occur when you run a model:

- Model crashes. Details.
- Model does not run at expected rate. Details.
- Decreased performance. Details.

#### Problem: Models are Crashing

Models often crash when an inport receives a value of 0 and the model attempts to divide by the inport value. This issue might occur upon run if the default value for an inport is 0. Depending on your system, the following solutions might address this issue:

- Change the default value for the inport prior to stepping the model.
- Rewrite the model to remove the possibility of dividing by 0.

##### Related Links

[Initializing Inport Values](mit_model_inports.html)

#### Problem: Model Runs Too Fast or Too Slow

If your model is unstable because it runs too fast or too slow, ensure the actual model rate matches the rate at which the model was compiled to run. If the rates do not match, adjust the period of the control loop that steps your model.

##### Related Links

[Configuring Model Timing](mit_model_timing.html)

#### Problem: Decreased Performance

If you suspect that models are causing your application to run slower than you desire, consider the following solutions that might improve performance:

- Only set parameter values in the control loop if you must update them during every time step. Instead, initialize the parameter values prior to running the control loop or set them in lower priority, background code.
- Probe only signals whose values you require. Probing many signals can have a negative impact on performance.
- Avoid changing the list of signals to probe frequently with the Set Signals to Probe VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_faq.html language=enus -->
## TOPIC 00010: Frequently Asked Questions (FAQ) (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_faq.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_faq.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Frequently Asked Questions (FAQ) (Model Interface Toolkit)

| Hardware and Software Support |  |
| --- | --- |
| Q: | Which modeling environments produce models that are compatible with the Model Interface Toolkit? |
| A: | The Model Interface Toolkit can run models from several environments, including MathWorks Simulink® software, after the models are compiled to work with the VeriStand Model Framework. Refer to the following help topic for more details about the types of models the Model Interface Toolkit supports: Support for Model Types and Modeling Environments |
| Q: | What versions of MathWorks software are compatible with my version of the Model Interface Toolkit? |
| A: | Refer to the following KnowledgeBase document at ni.com for a list of the versions of the LabVIEW, Windows, model compiler, and MathWorks software you can use with the Model Interface Toolkit: VeriStand Version Compatibility. |
| Q: | What types of hardware targets can run applications that call the Model Interface API? |
| A: | The Model Interface API supports targets that run the following operating systems: NI Linux Real-Time, Phar Lap ETS, and Windows. Refer to the KnowledgeBase at ni.com for a list of NI RT targets and the real-time operating system that each runs. |
| Timing and Performance |  |
| Q: | What determines the rate at which a model runs? |
| A: | The rate at which a model runs depends on how often the Take Model Time Step VI executes to step your model. To ensure this VI runs at a specific rate, execute the Take Model Time Step VI in a Timed Loop. |
| Q: | How can I improve the performance of my system as it relates to models? |
| A: | If you suspect that models are causing your application to run slower than you desire, consider the following solutions that might improve performance: Only set parameter values in the control loop if you must update them during every time step. Instead, initialize the parameter values prior to running the control loop or set them in lower priority, background code. Probe only signals whose values you require. Probing many signals can negatively impact performance. Avoid changing the list of signals to probe frequently with the Set Signals to Probe VI. |
| Migrating from the Simulation Interface Toolkit |  |
| Q: | How do I upgrade an application and models created for the LabVIEW Simulation Interface Toolkit to use the Model Interface Toolkit API? |
| A: | Refer to the following KnowledgeBase document for this information: Migrating Simulation Interface Toolkit Applications to Use the Model Interface Toolkit |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_from_c.html language=enus -->
## TOPIC 00011: Using C/C++ Models (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_from_c.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_from_c.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using C/C++ Models (Model Interface Toolkit)

The Model Interface API can run models you create in C/C++ and compile into a DLL, .out, or .so file. The models must be designed and compiled to work with the VeriStand Model Framework.

Refer to the *VeriStand Model Framework Introduction* guide (NI_VStand_Model_Framework_Guide.pdf in the *RootDrive*:\VeriStand\*xxxx*\ModelInterface\custom directory, where *RootDrive* is the drive where NI software installs and *xxxx* is the VeriStand version number) for information about creating and compiling C/C++ models that are compatible with the VeriStand Model Framework. This guide describes the components of the VeriStand Model Framework, the process for creating model code that is compatible with the framework, and requirements for compiling your model with the framework.

#### Related Links

[VeriStand Model Framework](mit_shared_components.html#model_framework)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_from_lv.html language=enus -->
## TOPIC 00012: Using LabVIEW VIs as Models (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_from_lv.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_from_lv.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using LabVIEW VIs as Models (Model Interface Toolkit)

You can convert other LabVIEW VIs into compiled .lvmodel or .lvmodelso files that the Model Interface API can run. This might be useful if you want to distribute the .lvmodel or .lvmodelso to other users to work with in the Model Interface Toolkit or VeriStand systems. You can convert LabVIEW VIs, or convert simulation subsystems you create using the LabVIEW Control Design and Simulation Module. The following sections describe how the Model Interface API supports these models.

|  | Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS (.lvmodelso files). For more information about how to use LabVIEW models with Linux, visit the NI website. |
| --- | --- |

#### Verifying That LabVIEW Model Support is installed

Before you can compile models in LabVIEW, you must install the LabVIEW Model Support feature, available on the VeriStand DVD you receive with your purchase. [More information](mit_shared_components.html).

#### Verifying Support for Your Hardware Target

Before you convert a LabVIEW VI into a compiled .lvmodel or .lvmodelso, answer the following questions to determine whether your target supports these models:

1. Do you want to run the model on a Windows computer or an RT target?
  - (Windows) —Windows targets support .lvmodel files. You can skip the remaining questions.
  - (RT) —Support depends on the real-time operating system (RTOS) the target runs. Continue to the next question.
2. What RTOS does my RT target run? Refer to the KnowledgeBase at ni.com for a list of RT targets and the RTOS that each runs, and then continue to the next question.
3. Given the RTOS my target runs, are .lvmodel or .lvmodelso files supported?
  - (Phar Lap ETS) — .lvmodel files are supported as long as the source VI does not contain code with certain Windows function calls that are not supported by the RTOS.
  - (NI Linux Real-Time) — .lvmodelso files are supported as long as the source VI does not contain code with certain Windows function calls that are not supported by the RTOS.

#### Preparing VIs to be Converted to Models

In the source VI to be compiled, you must assign front panel controls and indicators in VIs to the connector pane so the Model Interface API can identify them as inports, outports, and parameters when it loads the compiled .lvmodel or .lvmodelso. Build the VI connector pane according to how you want each control or indicator to work VeriStand, as the following table describes.

| Desired component in test application | VI connector pane assignment | Is default value maintained? |
| --- | --- | --- |
| Inport | Required input | No |
| Outport | Any output | No |
| Parameter | Optional or Recommended input | Yes |

##### Supported Data Types

Ensure that front panel controls or indicators assigned to the VI connector pane have only the following data types:

- Numerics
- Booleans
- 1D arrays of numerics
- 1D arrays of Booleans
- Clusters containing the previous data types

If you use an unsupported data type, LabVIEW returns an error when you try to convert the VI to a compiled .lvmodel or .lvmodelso. Note controls and indicators *not* assigned to the connector pane can have other data types because these objects are not part of the compiled model.

##### Related Links

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Setting Required, Recommended, and Optional Inputs and Outputs](/csh?topicname=lvhowto/specifying_required_recomm.html)

##### Configuring Global and Local Parameters

A compiled .lvmodel or .lvmodelso can contain two types of parameters, global parameters and block parameters:

- Local, or block, parameters apply only to the specific model to which they belong. If you want a front panel control in the source VI to become a local parameter, place that control in a cluster shell before you compile the VI into a .lvmodel or .lvmodelso . You can identify local parameters as those whose paths are in the form of Model Name / Cluster Name / Parameter Name .
- A global parameter applies to any model in the system that contains a parameter with the same name. To ensure a front panel control in the source VI becomes a global parameter in VeriStand, do not place that control in a cluster. You can identify global parameters as those whose paths are in the form of Model Name / Parameter Name .

|  | Tip To determine whether a parameter is global or block based on its path, use the Get Paths VI to return the paths of model parameters in a model. |
| --- | --- |

A .lvmodel or .lvmodelso can contain both local and global parameters.

##### Considerations for VIs with Array Terminals

If a VI contains an array control or indicator you want to include in the .lvmodel or .lvmodelso, enter a value in the *n*<sup>th</sup> element of the array, where *n* is the desired number of elements. Then, right-click the array control and select **Data Operations»Make Current Value Default**. Otherwise, the array becomes a single scalar value when the Model Interface API loads the model.

##### Related Links

[Generating Compiled Models from VIs](mit_gen_vs_model.html)

[Compiling Models Overview](mit_shared_components.html)

ni.com: Purchase the Control Design and Simulation Module

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_from_mdl.html language=enus -->
## TOPIC 00013: Using Models from MathWorks Simulink® Software (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_from_mdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_from_mdl.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Models from MathWorks Simulink® Software (Model Interface Toolkit)

You can use your model you created in MathWorks Simulink[®](/csh?topicname=lvhelp/trademarks.html) software with the Model Interface API. However, first you must compile the model into a DLL, .out, or .so file.

#### Overview of Compiling Simulink Models

The following illustration shows the typical workflow for compiling and integrating a Simulink model in a Model Interface Toolkit application. Green boxes ([IMAGE alt='image' src='noloc_env_mdl_flow_green.gif']) mean you complete the step in MathWorks application software. Blue boxes ([IMAGE alt='image' src='noloc_env_mdl_flow_blue.gif']) mean you complete the step in LabVIEW.

Click a box for detailed instructions for each step.

[IMAGE alt='image' src='loc_eps_mdl_mit_flow.gif']

##### Related Links

[Support for Model Types and Modeling Environments](../vsmithelp/mit_model_support.html)

[Considerations for Integrating Models from MathWorks Simulink Software](mit_models_mdl.html)

[Compiling a Model from MathWorks Simulink Software](mit_convert_model_to_dll.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_inports.html language=enus -->
## TOPIC 00014: Initializing Inport Values (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_inports.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_inports.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initializing Inport Values (Model Interface Toolkit)

The Take Model Time Step VI requires you to pass an array of inport values to the VI. By creating this array outside the control loop that contains the Take Model Time Step VI, you preallocate the memory and avoid incurring data copies in the control loop, which can cause jitter while the model executes.

After you create an array of initial inport values, you can manipulate the array so it includes the values you want to apply to the model inports. Updating the initial inport values can allow you to prevent your models from ever using invalid values. For example, if the model divides by an inport value, you can change the default value from 0 to avoid an invalid operation.

The following block diagram shows how to use the Model Interface API to create and modify the inports array outside the control loop.

[IMAGE alt='image' src='loc_bd_inport_array.gif']

|  | Creates an array of the appropriate size for the model inport values. The value of each element is 0. |
| --- | --- |
|  | Replaces the first element in the array of initialized values with the value from the Offset front panel control. Note This example applies the same inport value during every time step. This might be typical of applications in which you want to observe the response to a particular stimulus. However, in hardware-in-the-loop applications, you might want to apply dynamic values from hardware I/O, such as channels on a DAQ device. In this scenario, you can manipulate the inport array inside the control loop. |
|  | Note This example applies the same inport value during every time step. This might be typical of applications in which you want to observe the response to a particular stimulus. However, in hardware-in-the-loop applications, you might want to apply dynamic values from hardware I/O, such as channels on a DAQ device. In this scenario, you can manipulate the inport array inside the control loop. |
|  | Passes the inport array into the model and steps the model. Note Wires that connect terminals of the Take Model Time Step VI within a loop to terminals of objects outside of the loop must pass through a shift register rather than a tunnel for VeriStand to process the model correctly. Unlike shift registers, tunnels do not allow data from one iteration to carry over to the next causing the output value of the model to remain at zero. |
|  | Note Wires that connect terminals of the Take Model Time Step VI within a loop to terminals of objects outside of the loop must pass through a shift register rather than a tunnel for VeriStand to process the model correctly. Unlike shift registers, tunnels do not allow data from one iteration to carry over to the next causing the output value of the model to remain at zero. |

Refer to the MIT Inport and Output VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

##### Related Links

[Create Inports Array VI](../vsmitref/create_inports_array.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_params_init.html language=enus -->
## TOPIC 00015: Initializing Parameter Values (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_params_init.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_params_init.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initializing Parameter Values (Model Interface Toolkit)

Many models have parameters, which act as variables in the model. The default values of parameters are compiled into the model. However, you can perform the following tasks to set new initial values:

- In the appropriate modeling environment software, manually change the parameter values in the model, and then recompile the model.
- In your LabVIEW code, use the Model Interface API to programmatically change parameter values at run time. After your code loads a model, you can set an initial value for a parameter, as shown below.

In the latter case, initializing a parameter value with the Model Interface API is a two-step process: setting the new values, and then committing the new values. The following block diagram shows how to initialize a specific parameter in the initialization portion of your code:

[IMAGE alt='image' src='loc_bd_init_mit_params.gif']

|  | Loads the model from disk and creates a model reference that you pass to other VIs throughout the application to set its parameters, and later, to run the model in a control loop. |
| --- | --- |
|  | Creates a Parameter Interface reference that you pass to other VIs to get and set model parameters. |
|  | Sets the value of the scalar parameter whose index is 1 among all the model parameters. Tip You also can use the Set Parameter VI to update one element of a vector parameter or an entire vector parameter. You can use the Get Information by Path VI to programmatically return the index of a specific parameter rather than hard-coding it on the block diagram. However, note that hard-coding values provides better performance than using this VI. |
|  | Tip You also can use the Set Parameter VI to update one element of a vector parameter or an entire vector parameter. You can use the Get Information by Path VI to programmatically return the index of a specific parameter rather than hard-coding it on the block diagram. However, note that hard-coding values provides better performance than using this VI. |
|  | Commits the new value to the model. The Model Interface API only applies values you set after the Commit Parameters VI runs. |

After this initialization portion of your code runs, your model will use the new parameter value when the control loop of your application steps the model for the first time.

Refer to the MIT Multiple Models VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

#### Related Links

[Parameters VIs](../vsmitref/mit_param_pal.html)

[Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_params_run.html language=enus -->
## TOPIC 00016: Updating Parameters While the Model Runs (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_params_run.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_params_run.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Updating Parameters While the Model Runs (Model Interface Toolkit)

Many models have parameters, which act as variables in the model. The default values of parameters are compiled into the model. However, while a model runs in your application, you might want to adjust parameter values to test the system response. In your application, use the Model Interface API to programmatically change parameter values at run time.

#### Methods of Updating Parameters

Updates to parameters are often lower priority than transferring data between model inports/outports and other parts of the application, so updates do not need to occur during every time step. For example, it is more critical for a model to receive the motor command from a motor controller via inport than to adjust parameters that affect the load on the motor.

Choose between two methods for implementing code that sets parameters:

- With a lower priority than updates to inport and outports. More information.
- With the same high priority as updating inports and outports. More information.

The following sections describe the use case for each method and typical code for implementing them.

##### Low-Priority Updates to Parameters

You can use the Model Interface API to set parameter values in a lower priority, background part of your application, such as a loop that runs when the high priority control loop finishes executing and sleeps. This design is useful because updating parameters in the control loop that steps your model can decrease performance of the application.

Setting the value of a parameter outside the control loop is a two-step process: setting the new values, and then committing the new values. This process is similar to the process for initializing parameters.

The following block diagram shows the use of a Timed Loop that steps the model at a constant rate and a While Loop that updates parameter values. Both loops run until an error occurs or the **stop** front panel control is TRUE.

[IMAGE alt='image' src='loc_bd_params_bg.gif']

|  | Loads the model from disk and reads the compiled rate of the model in seconds, which is used to calculate the Timed Loop period. |
| --- | --- |
|  | Creates a Parameter Interface reference that you pass to other VIs to get and set model parameters. |
|  | Steps the model during each iteration of the Timed Loop and reads/writes inports and outports. The Timed Loop iterates until an error occurs or the stop control is TRUE. |
|  | Runs when the Timed Loop sleeps to set the value of a scalar parameter whose index is 0 among all the model parameters. Tip You also can use the Set Parameter VI to set one element of a vector parameter or an entire vector parameter. |
|  | Tip You also can use the Set Parameter VI to set one element of a vector parameter or an entire vector parameter. |
|  | Applies the new value to the model when the Apply Changes Boolean control is TRUE. Until the Commit Parameters VI runs, any values you set in step 4 are not applied. Therefore, you can set multiple new values and only set the latest value with the Commit Parameters VI. |
|  | Closes the reference to the parameter-update session, unloads the model from memory, and handles any errors. |

Refer to the MIT Parameter Management VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

##### High-Priority Updates to Scalar Parameters

To ensure that the model receives updates to parameter values during the same time step that you set them, you can update parameter values in the same control loop that steps your model. However, be aware that frequently calling this VI can decrease the performance of the control loop.

[IMAGE alt='image' src='loc_bd_params_inline.gif']

|  | Loads the model from disk and reads the compiled rate of the model in seconds, which is used to calculate the Timed Loop period. |
| --- | --- |
|  | Sets the Update Parameters In Line? property to TRUE so that you can access parameters in the same loop that steps the model. If this property is FALSE (default), meaning you can update parameters only outside the control loop, LabVIEW returns error code -383700 when the Set Parameter Inline VI runs. Note Within an application, you can either set parameters in line with time steps or set them in code outside the control loop. You cannot use both methods simultaneously. More information. |
|  | Note Within an application, you can either set parameters in line with time steps or set them in code outside the control loop. You cannot use both methods simultaneously. More information. |
|  | Sets the value of a scalar parameter whose index is 0 among all the model parameters. Note For illustration purposes, the Set Parameter Inline VI runs during every iteration of the Timed Loop. In a real-world application, you might want to implement this code so that the VI runs only when you want to set a new parameter value. The Set Parameter Inline VI allows you to set new parameter values only for scalar parameters or for a single element of a vector parameter. You cannot set an entire vector parameter or get any parameter values in line. |
|  | Note For illustration purposes, the Set Parameter Inline VI runs during every iteration of the Timed Loop. In a real-world application, you might want to implement this code so that the VI runs only when you want to set a new parameter value. The Set Parameter Inline VI allows you to set new parameter values only for scalar parameters or for a single element of a vector parameter. You cannot set an entire vector parameter or get any parameter values in line. |
|  | Steps the model and reads/writes inports and outports. The Timed Loop iterates until an error occurs or the stop control is TRUE. |
|  | Unloads the model from memory and handles any errors. |

Note that unlike initializing parameters or setting them from a background loop, you do *not* need to commit parameters when you update them in line.

##### Making Background and Inline Updates to Parameters

If you want to make background updates to parameter values in one part of your code *and* also make inline updates in the control loop, you can switch the value of the [Update Parameters In Line?](../vsmitref/mit_props.html) property. For example, you might want to initialize parameter values prior to stepping your model, and then change the values as the model executes.

##### Getting and Setting Elements in Vector Parameters

In addition to getting and setting scalar parameters, the Get Parameter, Set Parameter, and Set Parameter Inline VIs allow you to update a single element of a vector parameter. To identify the specific element of the vector to update, specify the position of the element within the parameter via the **Offset within parameter** input of these VIs. Use the following guidelines to determine the correct value for this input:

- If the vector has one dimension, the offset of an elements is zero-based.
- If the vector has two dimensions, the Model Interface API treats the parameter as a flattened 1D array in column-major order. You can use the Calculate Parameter Offset VI to return the offset of a particular element within the flattened array.

#### Related Links

[Format of Vector Parameters](mit_flattened_arrays.html#params)

[Calculate Parameter Offset VI](../vsmitref/calculate_parameter_off.html)

[Initializing Parameter Values](mit_model_params_init.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_signals.html language=enus -->
## TOPIC 00017: Probing Signal Values (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_signals.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Probing Signal Values (Model Interface Toolkit)

Signals in a model serve as probes, or test points, of a model as it executes. Whereas an outport typically connects to other parts of the application and must return data during every time step, applications typically do not need to read signal values at such a high priority. The Model Interface API provides VIs for accessing signal values in the background portion of your code.

The following block diagram shows the use of a Timed Loop that steps the model at a constant rate and a While Loop that reads signal values and displays them on the front panel. Both loops run until an error occurs or the **stop** front panel control is TRUE.

[IMAGE alt='image' src='loc_bd_probe_signals.gif']

|  | Loads the model from disk and reads the compiled rate of the model in seconds, which is used to calculate the Timed Loop period. |
| --- | --- |
|  | Performs the following tasks to prepare the VI to read signal values: Returns an array of paths for all the signals in the model. Creates a Signal Interface reference that you pass to other VIs to define which signals to probe and to get values from the probed signals. |
|  | Defines the list of signals to probe as the signals in the Signal Paths array. The Maximum Probed Data History input also configures the Model Interface API to store signal values from up to 100 model time steps in a buffer. More information. Tip To improve performance in your application, only probe signals whose values you need and avoid frequently changing the signals to probe. Probing many signals and frequently changing the signal list can both decrease performance. |
|  | Tip To improve performance in your application, only probe signals whose values you need and avoid frequently changing the signals to probe. Probing many signals and frequently changing the signal list can both decrease performance. |
|  | Steps the model during each iteration of the Timed Loop and reads/writes inports and outports. The Timed Loop iterates until an error occurs or the stop control is TRUE. |
|  | Returns the values of signals from a specific model time step. The format of this output is a flattened 1D array that contains the values of each signal. Tip This VI contains a Simulation Time output, which returns the elapsed time in the model, in seconds, when the model produced the current signal values. This value is useful for allowing you to correlate events within the model with the time they occurred. |
|  | Tip This VI contains a Simulation Time output, which returns the elapsed time in the model, in seconds, when the model produced the current signal values. This value is useful for allowing you to correlate events within the model with the time they occurred. |
|  | When LabVIEW returns probed signal values before the timeout, the False case of the Case structure converts the array of signal values to a cluster and plots them in a waveform chart on the front panel. |
|  | Closes the reference to the signal-probe session, unloads the model from memory, and handles any errors. |

Refer to the MIT Signal Probes VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

#### Returning Probed Data in Different Formats

The Get Probed Signal Values VI returns signal values in two formats, depending on which instance of the polymorphic VI you use:

- Raw —Returns signal values in a flattened 1D array in column-major order . This polymorphic instance allows your code to run with higher performance.
 [IMAGE alt='image' src='tip.gif']
**Tip** If you read probed signal values in raw format, you can format them offline using the Format Raw Signal Values VI.
- Formatted —Returns signal values in a formatted array in which the value for each signal is a separate element, shown as follows:

[IMAGE alt='image' src='loc_fp_probed_data.gif']

#### Changing Signals to Probe

To change the signals that the Model Interface API is probing while the control loop steps the model, call the Set Signals to Probe VI again with the new list of signals. Note that if any signal values from the previous signal list are still in the signal buffer, meaning the Get Probed Signal Values VI has not returned those values, the Model Interface API discards those values and immediately starts buffering values for the new signal list.

#### Storing Signal Values from Multiple Time Steps

Each time the Get Probed Signal Values VIs executes, it returns signal values from the earliest time step for which LabVIEW stores signal data. Storing signal values from multiple time steps is useful because code that probes signals typically runs at a lower priority than the control loop that steps your model. Therefore, the model might execute multiple times, producing multiple values for each signal, between subsequent calls to the Get Probed Signal Values VI.

|  | Tip If you find the Get Probed Signal Values VI loses signal values because it does not execute before the buffer overflows, you can increase the value of the Maximum Probed Data History input of the Set Signals to Probe VI. |
| --- | --- |

#### Related Links

[Get Probed Signal Values VI](../vsmitref/get_probed_signal_values.html)

[Set Signals to Probe VI](../vsmitref/set_signals_to_probe.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_support.html language=enus -->
## TOPIC 00018: Supported Model Types and Modeling Environments (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_support.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported Model Types and Modeling Environments (Model Interface Toolkit)

The following table describes Model Interface Toolkit support for common types of models. The Model Interface Toolkit uses the VeriStand Model Framework to execute functions in your models, so supported models are those that are compatible with the framework.

| Supported? | Model Type | Support Considerations |
| --- | --- | --- |
|  | MathWorks Simulink® model compiled using MathWorks Real-Time Workshop®1 | Runs on the following target types in the specified compiled formats: Windows PC—DLL Phar Lap ETS RT targets—DLL NI Linux Real-Time targets—.so |
|  | Uncompiled model from MathWorks Simulink software | You must compile these models before you can use them with the Model Interface API. |
|  | C/C++ | Refer to the VeriStand Model Framework Introduction guide2 for information about creating and compiling C/C++ models that are compatible with the VeriStand Model Framework. |
|  | LabVIEW VI compiled as a .lvmodel1 | Runs on Windows PCs. Also runs on Phar Lap ETS RT targets as long as the VI does not contain code with certain Windows function calls that the ETS real-time operating system does not support. |
|  | LabVIEW VI compiled as a .lvmodelso1 | Runs on Linux x64 and Linux ARM. Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS. For more information about how to use LabVIEW models with Linux, visit the NI website. The Model Interface Toolkit is not supported on x64 Intel-based cDAQ controllers running NI Linux Real-Time. |
|  | Note You must install additional software to enable LabVIEW models for targets running a Linux Real-Time OS. For more information about how to use LabVIEW models with Linux, visit the NI website. The Model Interface Toolkit is not supported on x64 Intel-based cDAQ controllers running NI Linux Real-Time. |  |
|  | Compiled models from other environments | Several modeling environments can build compiled models that work with the VeriStand Model Framework. |
|  | Models compiled for use with the LabVIEW Simulation Interface Toolkit | You must recompile these models before you can use them with the Model Interface API. |
| 1 Refer to the following KnowledgeBase document at ni.com for a list of the versions of the LabVIEW, Windows, model compiler, and MathWorks software you can use with the Model Interface Toolkit: VeriStand Version Compatibility.2 NI_VStand_Model_Framework_Guide.pdf in the RootDrive:\\VeriStand\\xxxx\\ModelInterface\\custom directory, where RootDrive is the drive where NI software installs and xxxx is the VeriStand version number. |  |  |

##### Related Links

[Compiling a Model from MathWorks Simulink Software](mit_convert_model_to_dll.html)

[Generating Compiled Models from VIs](mit_gen_vs_model.html)

Developer Zone: List of supported modeling environments

#### Simulink Model Compatibility

In the Simulink software, you can convert models that use only a fixed step-size ordinary differential equation (ODE) solver into compiled models. Additionally, you must turn off data logging in the Simulink application software. Refer to the Simulink documentation for information about using the Simulink application software to change the ODE solver of a model and turn off data logging.

#### Troubleshooting Missing Options in Modeling Environments

If features for compiling models, such as the **NIVeriStand.tlc—NI Real-Time Target** system target file in the Simulink software, are missing, ensure all required NI components are installed. The Model Interface Toolkit does not install features for compiling models. However, the components that install this support are available for installation from the same VeriStand DVD that contains the Model Interface Toolkit. [More information](mit_shared_components.html).

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_model_timing.html language=enus -->
## TOPIC 00019: Configuring Model Timing (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_model_timing.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_model_timing.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring Model Timing (Model Interface Toolkit)

A model is set to run at a certain rate, or step size, as defined in the build options when the model is compiled. However, the rate at which the Model Interface API actually steps the model is determined by how often the Take Model Time Step VI executes in your application. As mentioned previously, you can use a Timed Loop to step the model at a specific rate to ensure this VI runs reliably and repeatedly.

In the following block diagram, each iteration of the Timed Loop must complete execution within the period specified. To calculate the period, the Get Model Period VI reads the compiled rate of the model in seconds. However, the **Period** input of the Timed Loop expects values in the same units as the 1 kHz clock timing source, so this application converts seconds to milliseconds.

[IMAGE alt='image' src='loc_bd_timing_mit.gif']

|  | Note If the subdiagram of the Timed Loop completes execution within the period of the loop, the Timed Loop sleeps and allows any other code or structures to execute on the block diagram. |
| --- | --- |

##### Methods for Setting and Monitoring Timing

The previous block diagram shows Timed Loop and Model Interface API features that allow you to control and monitor the timing of models in your application.

| Action | Feature |  |
| --- | --- | --- |
|  | Set the period of Timed Loop iterations/rate of model time steps. | Period input on Timed Loop |
|  | View how long the current time step of the model has been running. | Iteration Duration output on Timed Loop |
| View whether the previous iteration of the Timed Loop ran longer than the specified period. | Finished Late? [i-1] output on Timed Loop |  |
|  | View the time in the model. | Get Simulation Time VI |

Refer to the MIT Simple Load and Run Model VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

##### Related Links

[Timed Loop](/csh?topicname=glang/timed_loop.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

##### Running Models Faster or Slower than Real Time

Depending on the rate at which you call the Take Model Time Step VI, the rate at which the model actually executes might differ from the compiled rate. For example, even if the model was compiled to run at 100 Hz, you can set the Timed Loop period so that it runs at 1 kHz, or 10 times faster than real time. This means the model does not run in real time and is potentially unstable.

If both the controller and plant are simulated, such as in model-in-the-loop testing, running your model at a faster rate than the rate for which it was compiled can be desirable. Running faster than real time allows you to accomplish more simulation in a shorter amount of time. However, when you test with real hardware, as in hardware-in-the-loop testing, run your model at the rate for which it was compiled to accurately simulate the system.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_models_mdl.html language=enus -->
## TOPIC 00020: Considerations for Integrating Models from MathWorks Simulink® Software (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_models_mdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_models_mdl.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Considerations for Integrating Models from MathWorks Simulink® Software (Model Interface Toolkit)

The Model Interface API identifies inports, outports, parameters, and signals in models you created and compiled in MathWorks Simulink[®](/csh?topicname=lvhelp/trademarks.html) application software according to their configuration in the Simulink software.

#### Case Study: Simple Models

Consider the following model from the Simulink software environment.

[IMAGE alt='image' src='vs_simulinkmodel.gif']

When you load this model in an application, the Model Interface API categorizes its components as described in the following table.

| Component in model | Type of component in LabVIEW |
| --- | --- |
| Raw_Sine | Signal |
| Sine_Gain | Parameter |
| In1 | Inport |
| Out1 | Outport |

#### Inports and Outports

Simulink inports and outports located on the top-level of the simulation hierarchy in the Simulink software are available as inports and outports. However, inports and outports in submodels are available only if you place VeriStand inport and outport blocks in the submodel.

|  | Note The Model Interface Toolkit shares several components with the VeriStand software, such as its inport and outport blocks. |
| --- | --- |

#### Parameters

Compiled models contain one of two types of parameters: global parameters or block parameters:

- A global parameter, similar to a workspace variable in MathWorks MATLAB® software, applies to any model in the application that contains a parameter with the same name. Even if you open a parameter interface to update parameters for a specific model, the Model Interface API applies updates to all models that contain the same global parameter.
 
 If you specify to inline parameters in the Simulink software, MathWorks Real-Time Workshop® software converts MATLAB workspace variables to global parameters in the compiled model. You can identify global parameters as those whose paths are in the form of Model Name / Parameter Name .
- Block parameters are not global and apply only to the specific model to which they belong. If you do not specify to inline parameters in the Real-Time Workshop software, block parameters remain block parameters in the compiled model. You can identify block parameters as those whose paths are in the form of Model Name / Block Name / Parameter Name .

|  | Tip To determine whether a parameter is global or block based on its path, use the Get Paths VI to return the paths of model parameters in a model. |
| --- | --- |

A Simulink model can contain only one type of parameter. However, an application can contain a model with global parameters and a model with block parameters.

##### Conditions Where Parameters Are Unavailable

The Model Interface API supports model references to submodels, but you cannot access parameters or signals in submodels. In other words, submodels execute in an application built with the Model Interface API, but their parameters and signals are not available for writing or reading.

In the Simulink software, you can inline parameters, but the Model Interface API cannot access inlined parameters to get or set their values. If you inline a parameter, you still can allow the Model Interface API to influence the parameter by configuring a variable that affects the parameter to be tuneable. For example, consider a model with the following characteristics:

- Contains a constant configured with the expression x + 3 .
- Contains a sine wave block whose amplitude and frequency parameters are inlined, and therefore unavailable in the Model Interface API.
- Adds the result of the x + 3 constant to the output from the sine wave block.

Although the parameters of the sine wave block are unavailable, you can influence the operation by specifying that the *x* variable is tunable in the Simulink software. When *x* is tunable, it will appear in the list of parameters the model contains, so you can change the value of *x* like a parameter as the model executes.

#### Signals

Model signals are usually excluded when you convert a model into a compiled model unless you define a signal as a test point in the software you use to compile the model.

##### Conditions Where Signals Are Unavailable

The Model Interface API supports model references to submodels, but you cannot access parameters or signals in submodels. In other words, submodels execute in an application built with the Model Interface API, but their parameters and signals are not available for writing or reading.

Certain optimizations you enable in the Simulink software can make a signal unavailable to the Model Interface API. You can disable these options for the entire model to make all signals available for probing, but the memory footprint of the model increases as a result. Alternatively, you can mark individual signals as test points in the Simulink software to maintain a reduced memory footprint while keeping the test-point signals available for probing.

|  | Note If you previously converted your model to a compiled model, you must convert the model again after marking signals as test points. |
| --- | --- |

#### Bus Objects

In models compiled in the Simulink R2010b software or a later supported version, named components of bus objects, such as signals, are represented in the same hierarchy as in the uncompiled model. For models compiled in versions of the Simulink software earlier than R2010b, bus objects are represented as a single vector of components.

#### Related Links

[Using Models from MathWorks Simulink Software](mit_model_from_mdl.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_models_recommendations.html language=enus -->
## TOPIC 00021: Using Model Interface VIs in the Control Loop

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_models_recommendations.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_models_recommendations.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Model Interface VIs in the Control Loop

When you design your application, certain Model Interface Toolkit VIs are suitable for use in the control loop that steps your model, while some are not suitable due to their effect on jitter and determinism. The following VIs are suitable for use in a time-critical VI or timed structure that runs on an RT target:

- Take Model Time Step
- Get Simulation Time
- Set Parameter Inline

Avoid using the following VIs in the model control loop if determinism is an important consideration in your application:

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

##### Related Links

[Model Interface Toolkit VIs](../vsmitref/vsmitref.html)

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_multiple_models.html language=enus -->
## TOPIC 00022: Executing Multiple Instances of a Model Simultaneously (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_multiple_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_multiple_models.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Multiple Instances of a Model Simultaneously (Model Interface Toolkit)

To execute the same model under different conditions, such as with different inport mappings or parameter values, complete the following steps:

|  | Note Loading more than one instance of the same compiled model can cause errors if the model accesses a shared resource, such as a dependant file. Contact your model provider for information about whether the model accesses such resources. |
| --- | --- |

1. Make a copy of the model files on disk for each instance you need to execute.
2. Complete one of the following steps, depending on the real-time operating system of your target:
  - (Phar Lap ETS, Windows) Rename the copied model files so that each has a unique name.
  - (NI Linux Real-Time) Ensure all copied models have the same name as the original. Then copy each model file to a different location on the NI Linux Real-Time target using WebDAV.
 [IMAGE alt='image' src='note.gif']
**Note** For information about how to transfer files using WebDAV, visit ni.com/info and enter the code WebDAVTransfer.
3. Load the copies of the models separately with the Load Model VI. You can step the models within the same Timed Loop if you want them to run at the same rate.

Refer to the MIT Multiple Models VI in the labview\examples\Control and Simulation\Model Interface directory for example code that demonstrates these concepts.

##### Related Links

[Basic Architecture for Executing Models](mit_basic_design.html)

[Load Model VI](../vsmitref/load_model.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_overview.html language=enus -->
## TOPIC 00023: Components of an Application (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_overview.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Components of an Application (Model Interface Toolkit)

An application built with the Model Interface Toolkit typically consists of the following components:

- Target —The computer on which you run the application and model. You can run a model either on a Windows target or on a supported National Instruments real-time (RT) target.
- LabVIEW application —The LabVIEW code that uses the Model Interface API to run and interact with a model. The block diagram of the VI contains the code that steps the model, transfers data to and from the model, and so on.
- Model —A model is a mathematical representation of a real-world system, such as the plant and controller, in a closed-loop control system. Models run on hardware targets and are typically used to respond to stimuli from other parts of the system by producing outputs in a way that simulates the modeled item. Models also can serve the functions of signal generation, signal analysis, and control.

When the target runs the LabVIEW application, the Model Interface API loads the model and iteratively executes the model, transferring data to and from the model and other parts of the system.

#### Additional Components in Applications that Include Hardware

If you intend to run your test application on an RT target or integrate I/O from hardware, you might need the following components:

- LabVIEW Real-Time Module —You need this module to run a deterministic RT simulation.
- LabVIEW FPGA Module —To interact with FPGA I/O, you need the FPGA Module.
- National Instruments Driver Software —You need the appropriate National Instruments driver software, such as NI-DAQmx, NI-RIO, or NI-XNET, to communicate with hardware installed in a target.

The remainder of this topic describes tasks you typically perform to create and integrate a model into a LabVIEW application using the Model Interface API.

#### Components of a Model

Models can contain the following components through which tuning, data communication, and debugging occurs:

- Inports and Outports —To communicate with other parts of the control system, models contain inputs and outputs, called inports and outports. You can transfer data between an inport or outport and hardware inputs and outputs, other models in the system, and so on. Inports and outports are dynamic values the Model Interface API updates each time step the model executes.
- Parameters —Parameters act like variables in the model. Unlike inports, whose values come from elsewhere in the system and change frequently, users typically manipulate parameters infrequently to tune the behavior of the simulation. For example, an operator might set a parameter before the model starts executing or update its value between the execution of discrete tests.
- Signals —Signals serve as probes, or test points, of a model as it executes. For example, you might want to monitor the value a function produces for the model to use internally if the value will not be available through an outport.

Consider a system that contains a physical motor controller and a model that represents a DC motor. The model runs on a hardware target. Such a model might contain the following components:

- An inport that accepts the motor command from the motor controller.
- An outport that returns the motor speed from the model.
- Parameters that adjust the load on the motor. You might set parameter values once per test rather than updating them frequently during the test.
- A signal that returns internal data that aids in debugging.

#### Building and Preparing Models for Use in LabVIEW

You can build models using several different modeling environments. You must compile a model in the modeling environment before it can run in your application. The exact process for compiling a model to interact with the Model Interface Toolkit depends on the modeling environment you use to build it. Refer to the appropriate resource for your specific modeling environment for information about preparing the model for use with the Model Interface API:

- Using Models from MathWorks Simulink® Software
- Using C/C++ Models
- Using LabVIEW VIs as Models

If you build the model in some other modeling environment, refer to the modeling environment documentation for information on how to compile your model to be compatible with the Model Interface API.

##### Related Links

[Support for Model Types and Modeling Environments](mit_model_support.html)

#### Integrating Models into the LabVIEW Application

When you build your test application in LabVIEW, you connect parts of the model to sources of I/O in other parts of the application. For example, you might pass data from a hardware channel to a model inport so the model receives and operates on data from the hardware device. You also must configure timing and choose how to interact with parameters and signals in the model.

Use Model Interface Toolkit VIs to control the execution of models, monitor their status and timing, configure their parameters, and read from their signals as the models run.

##### Related Links

[Basic Architecture for Executing Models](mit_basic_design.html)

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_shared_components.html language=enus -->
## TOPIC 00024: Compiling Models Overview (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_shared_components.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_shared_components.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Compiling Models Overview (Model Interface Toolkit)

The Model Interface Toolkit provides the Model Interface VIs, which you use to run and interact with models. However, this toolkit does not provide support for compiling models that are compatible with the toolkit. The following free components, available on the same VeriStand DVD from which you install the Model Interface Toolkit, install support for compiling compatible models:

- VeriStand Model Framework —Provides tools for compiling models designed in C/C++ or third-party modeling environments, such as MathWorks Simulink ® software.
- LabVIEW Model Support —Provides a tool for generating models from LabVIEW VIs.

|  | Note If you install only the Model Interface Toolkit and not these components, environments like LabVIEW and the Simulink software do not support compiling compatible models. |
| --- | --- |

#### Related Links

- Using Models from MathWorks Simulink® Software
- Using C/C++ Models
- Using LabVIEW VIs as Models

#### VeriStand Model Framework

The VeriStand The Model Framework provides tools for compiling models created in third-party modeling environments and for designing custom models in C/C++. When you run your test application, designed using the Model Interface Toolkit, the application executes functions defined in VeriStand Model Framework files. These functions then call functions in your model code to execute the model.

##### Finding the Model Framework Files and Documentation

The VeriStand installer installs the Model Framework files and documentation at *RootDrive*:\VeriStand\*xxxx*\ModelInterface\, where *RootDrive* is the drive where NI software installs and *xxxx* is the VeriStand version number. If you cannot locate the files at that location, run the VeriStand installer again and select the **VeriStand Model Framework** item from the list of features to install. You do not need to reinstall other NI software to install the Model Framework.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_vsmithelp_boilerplate.html language=enus -->
## TOPIC 00025: Model Interface Toolkit

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_vsmithelp_boilerplate.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_vsmithelp_boilerplate.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model Interface Toolkit

May 2020, 374160D-01

The LabVIEW Model Interface Toolkit allows you to integrate models from a variety of simulation environments and programming languages into your development, prototyping, and testing of control systems.

This toolkit provides the Model Interface API, a palette of VIs you use to run and interact with models. You can use other LabVIEW features in conjunction with the Model Interface API, such as LabVIEW projects and hardware driver VIs.

Use the following help topics to get started with the Model Interface Toolkit.

| Getting Started Components of an Application Support for Model Types and Modeling Environments Frequently Asked Questions (FAQ) Developing an Application Basic Architecture for Executing Models Configuring Model Timing Initializing Parameter Values Updating Parameters While the Model Runs Probing Signal Values Troubleshooting Issues in Models | Compiling and Integrating Models Compiling Models Overview Using Models from MathWorks Simulink® Software Using C/C++ Models Using LabVIEW VIs as Models Where to Go Next Integrating Hardware, Distributing Code, and More |
| --- | --- |

|  | To view all related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

#### Relationship to VeriStand

The VeriStand real-time testing software and the Model Interface Toolkit share [components that provide support for compiling models](mit_shared_components.html).

VeriStand is a software environment for efficiently creating real-time testing applications. VeriStand helps you configure a multicore-ready real-time engine to execute tasks such as real-time stimulus generation and data acquisition for high-speed and conditioned measurements. For more information about VeriStand, refer to ni.com/veristand.

© 2013-2020 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmithelp/mit_wheretogo.html language=enus -->
## TOPIC 00026: Where to Go Next (Model Interface Toolkit)

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmithelp/mit_wheretogo.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmithelp/mit_wheretogo.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Where to Go Next (Model Interface Toolkit)

Refer to the following resources as you continue building your application in LabVIEW.

#### Finding Example Code

To browse example code that demonstrates various uses of the Model Interface API, select **Help»Find Examples** from LabVIEW to launch the NI Example Finder. Navigate to the **Toolkits and Modules** folder. To find the examples on disk, you also can browse to the labview\examples\Control and Simulation\Model Interface directory. You can modify an example VI to fit an application, or you can copy and paste from one or more examples into a VI that you create.

#### Integrating Device I/O

To read data from a hardware device and write it to a model inport or write data from a model inport to a hardware device, use driver VIs written for the device. For example, you can use the NI-DAQmx VIs to communicate with an NI DAQ device in your test application. After you install a LabVIEW add-on such as a module, toolkit, or driver, the documentation for that add-on appears in a separate help system you can access by selecting **Help»*Add-On Help***, where *Add-On Help* is the name of the separate help system for the add-on.

#### Optimizing an Application to Run on an RT Target

If your application includes a VI that runs on an RT target and VIs that run on the host computer, choose from available remote-communication methods: [Exploring Remote Communication Methods](/csh?topicname=lvrtconcepts/exploring_communication_methods.html).

Developing complex LabVIEW Real-Time applications requires an understanding of how LabVIEW maps to the real-time computing model. Some LabVIEW programming strategies that work well when developing for a general-purpose operating system do not translate to the headless, priority-driven execution model of a real-time operating system (RTOS). For best practices for designing, developing, and deploying applications with the LabVIEW Real-Time Module, refer to the [RT Best Practices Portal](/csh?topicname=lvrtbestpractices/rt_portal.html).

The LabVIEW Real-Time Module and other LabVIEW add-ons add functionality to the LabVIEW development system and must be purchased separately. Refer to the specific module documentation for more information about that product.

#### Distributing an Application

You must use a LabVIEW project to build stand-alone applications that you can distribute, as well as to deploy or download files to RT targets. You also must use a project to work with a Windows Embedded Standard, RT, FPGA, or Touch Panel target.

- Building and Deploying a Stand-Alone Real-Time Application

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/calculate_parameter_off.html language=enus -->
## TOPIC 00027: Calculate Parameter Offset VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/calculate_parameter_off.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/calculate_parameter_off.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Calculate Parameter Offset VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Calculates the position of an element within a flattened vector parameter. This offset position is required to update a single element of 2D vector parameters with the [Set Parameter](../vsmitref/set_parameter.html) or [Set Parameter Inline](../vsmitref/set_parameter_inline.html) VIs.

**Related link:** [Manipulating Model Components in Flattened Format](../vsmithelp/mit_flattened_arrays.html)

[IMAGE alt='image' src='calculate_parameter_offset.gif']

|  | Parameter Information contains the following elements that describe a parameter. You can generate this cluster with the Get Information by Path VI. Name is the symbolic path of the parameter within the model in the format: Model Name (as specified in the model)/Block Name (if the parameter is a block parameter)/Parameter Name. Index specifies the index of the parameter among all the parameters in the model. Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
| --- | --- |
|  | Name is the symbolic path of the parameter within the model in the format: Model Name (as specified in the model)/Block Name (if the parameter is a block parameter)/Parameter Name. |
|  | Index specifies the index of the parameter among all the parameters in the model. |
|  | Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
| 0 | Double—Double-precision, floating-point numeric |
|  | Row number specifies the index of the row in which the element appears within the original 2D vector parameter. Row indexes are zero-based. |
|  | Column number specifies the index of the column in which the element appears within the original 2D vector parameter. Column indexes are zero-based. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Offset within Parameter returns the offset of the element within the flattened vector. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/call_model_start_routine.html language=enus -->
## TOPIC 00028: Call Model Start Routine VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/call_model_start_routine.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/call_model_start_routine.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Call Model Start Routine VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Executes initialization code defined in the model-start function of a model.

|  | Note This VI calls MDLStart, a function in The MathWorks, Inc. Simulink® software, or USER_ModelStart(), a user-defined function in models compiled using the NI VeriStand 2013 Model Framework or later. |
| --- | --- |

Use this VI to explicitly call the model-start function if you need to perform tasks after this VI executes the function and before the first time step. However, if you do *not* need to perform any tasks after the model-start function but before the first time step, you can avoid using this VI because LabVIEW automatically executes the function when the [Take Model Time Step](../vsmitref/take_model_time_step.html) VI runs for the first time.

[IMAGE alt='image' src='call_model_start_routine.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/close_parameter_interface.html language=enus -->
## TOPIC 00029: Close Parameter Interface VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/close_parameter_interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/close_parameter_interface.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Close Parameter Interface VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Closes a reference to model parameters that you opened with the [Create Parameter Interface](../vsmitref/create_parameter_inter.html) VI.

[Examples](#examples)

[IMAGE alt='image' src='close_parameter_interface.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Close Parameter Interface VI:

- MIT Multiple models VI: labview\examples\Control and Simulation\Model Interface
- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/close_signal_interface.html language=enus -->
## TOPIC 00030: Close Signal Interface VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/close_signal_interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/close_signal_interface.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Close Signal Interface VI

**Owning Palette:** [Signals VIs](../vsmitref/mit_signals_pal.html)

**Requires:** Model Interface Toolkit

Closes a reference to model signals that you opened with the [Create Signal Interface](../vsmitref/create_signal_interface.html) VI.

[Example](#examples)

[IMAGE alt='image' src='close_signal_interface.gif']

|  | Signal Interface in is a reference that allows you to access the signals in a model. To create this reference, you must create a signal interface. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Signal Probes VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Close Signal Interface VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/commit_parameters.html language=enus -->
## TOPIC 00031: Commit Parameters VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/commit_parameters.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/commit_parameters.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Commit Parameters VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Applies the value of any model parameters you previously set with the [Set Parameter](../vsmitref/set_parameter.html) VI.

Until this VI runs, LabVIEW does not apply any parameter values you set in code outside of the control loop. Therefore, you can set multiple new parameters with the Set Parameter VI, and then apply them simultaneously with this VI.

**Programming Patterns:** [Initializing Parameter Values Before the Model Runs](../vsmithelp/mit_model_params_init.html), [Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='commit_parameters.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Parameter Interface out returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Commit Parameters Details

Because you must use this VI outside the control loop that steps the model, you typically cannot control the exact time within the model that LabVIEW updates the parameters.

#### Examples

Refer to the following VIs for examples of using the Commit Parameters VI:

- MIT Multiple models VI: labview\examples\Control and Simulation\Model Interface
- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/create_inports_array.html language=enus -->
## TOPIC 00032: Create Inports Array VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/create_inports_array.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/create_inports_array.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Inports Array VI

**Owning Palette:** [Inports & Outports VIs](../vsmitref/mit_io_pal.html)

**Requires:** Model Interface Toolkit

Creates an array with the number of elements needed to represent the model inports. Every array element is initialized to 0. You can manipulate this array to set initial inport values prior to running the model.

By creating the inport array outside the control loop, you preallocate the memory and avoid incurring data copies in the control loop, which can cause jitter.

**Programming Patterns:** [Initializing Inport Values](../vsmithelp/mit_model_inports.html)

[Example](#examples)

[IMAGE alt='image' src='create_inports_array.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Inports Array out returns an array that contains the number of elements needed to represent the model inports. The value of each element is 0. The format of this input is a flattened 1D array in column-major order. |
|  | Inports Array size returns the number of elements in the flattened array of inport values. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Inport and Output VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Create Inports Array VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/create_parameter_inter.html language=enus -->
## TOPIC 00033: Create Parameter Interface VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/create_parameter_inter.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/create_parameter_inter.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Parameter Interface VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Creates a reference through which you manipulate the parameters of a model. Use the reference this VI creates to initialize parameters or update them from background-priority code as the model executes.

**Programming Patterns:** [Initializing Parameter Values Before the Model Runs](../vsmithelp/mit_model_params_init.html), [Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

[Examples](#examples)

[IMAGE alt='image' src='create_parameter_interface.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Parameter Interface returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Create Parameter Interface VI:

- MIT Multiple models VI: labview\examples\Control and Simulation\Model Interface
- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/create_signal_interface.html language=enus -->
## TOPIC 00034: Create Signal Interface VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/create_signal_interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/create_signal_interface.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Signal Interface VI

**Owning Palette:** [Signals VIs](../vsmitref/mit_signals_pal.html)

**Requires:** Model Interface Toolkit

Creates a reference through which you read from the signals in a model. Use the reference this VI creates to set a list of signals to read, then read their values from background-priority code as the model executes.

**Programming Patterns:** [Probing Signal Values at Run Time](../vsmithelp/mit_model_signals.html)

[Example](#examples)

[IMAGE alt='image' src='create_signal_interface.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Signal Interface returns a reference that allows you to access the signals in a model. Wire this output to other VIs from the Signals palette to interact with the signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Signal Probes VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Create Signal Interface VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/format_raw_signal_values.html language=enus -->
## TOPIC 00035: Format Raw Signal Values VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/format_raw_signal_values.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/format_raw_signal_values.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Format Raw Signal Values VI

**Owning Palette:** [Signals VIs](../vsmitref/mit_signals_pal.html)

**Requires:** Model Interface Toolkit

Returns an unflattened version of the model signal values in the flattened **Data Array in**. This VI is useful if you want to read raw signal values quickly while the model executes and later reformat them offline for visualization.

Use the Raw instance of the polymorphic [Get Probed Signal Values](../vsmitref/get_probed_signal_values.html) VI returns signal values in this format.

[IMAGE alt='image' src='format_raw_signal_values.gif']

|  | Data Array in specifies the array of raw signal values to format. |
| --- | --- |
|  | Probed Signals Information is an array of clusters in which each cluster describes a signal whose values are part of the Data Array in. You can generate these clusters with the Get Information by Path VI. Index specifies the index of the signal among all the signals in the model. Block Name is the symbolic path of the block from the signal originates. This string is in the format: Model Name (as specified in the model)/Block Name. Port Number is the port number of the signal. Signal Name is the user-defined name of the signal. Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
|  | Index specifies the index of the signal among all the signals in the model. |
|  | Block Name is the symbolic path of the block from the signal originates. This string is in the format: Model Name (as specified in the model)/Block Name. |
|  | Port Number is the port number of the signal. |
|  | Signal Name is the user-defined name of the signal. |
|  | Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
| 0 | Double—Double-precision, floating-point numeric |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Structured Data returns the signal values formatted as a 1D array of clusters, where each cluster element is a 2D array of signal values for a specific signal from a specific time step. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_information_by_path.html language=enus -->
## TOPIC 00036: Get Information by Path VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_information_by_path.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_information_by_path.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Information by Path VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Returns properties of a specific component of a model, such as an inport or parameter, that you can pass to other VIs to interact with the component.

[Details](#details)  [Example](#examples)

#### Get Inport Information by Path

Returns properties for a model inport.

[IMAGE alt='image' src='get_inport_information_by_path.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | Inport Path specifies the path of an inport within the model. You can use the Get Paths VI to return the paths of model components. If the model does not contain a component with the path you specify, Found? is FALSE and the Inport Information cluster elements contain default data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Inport Information returns the following elements that describe the inport. Path is the path of the component within the model. Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. offset returns the position of the inport within the flattened 1D array of inport values the Model Interface API uses to store inport values. Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
|  | Path is the path of the component within the model. |
|  | Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | offset returns the position of the inport within the flattened 1D array of inport values the Model Interface API uses to store inport values. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
| 0 | Double—Double-precision, floating-point numeric. |
|  | Found? is TRUE if the component whose path you specify exists in the model. Otherwise, LabVIEW returns FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Outport Information by Path

Returns properties for a model outport.

[IMAGE alt='image' src='get_outport_information_by_path.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | Outport Path specifies the path of an outport within the model. You can use the Get Paths VI to return the paths of model components.If the model does not contain a component with the path you specify, Found? is FALSE and the Outport Information cluster elements contain default data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Outport Information returns the following elements that describe the outport. Path is the path of the component within the model. Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. offset returns the position of the outport within the flattened 1D array of outport values the Model Interface API uses to store outport values. Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
|  | Path is the path of the component within the model. |
|  | Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | offset returns the position of the outport within the flattened 1D array of outport values the Model Interface API uses to store outport values. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
| 0 | Double—Double-precision, floating-point numeric. |
|  | Found? is TRUE if the component whose path you specify exists in the model. Otherwise, LabVIEW returns FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Parameter Information by Path

Returns properties for a model parameter.

[IMAGE alt='image' src='get_parameter_information_by_path.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | Parameter Path is the path of a parameter within the model. You can use the Get Paths VI to return the paths of model components.If the model does not contain a component with the path you specify, Found? is FALSE and the Index element of the Parameter Information output cluster is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Parameter Information returns the following elements that describe the parameter. Name is the symbolic path of the parameter within the model in the format: Model Name (as specified in the model)/Block Name (if the parameter is a block parameter)/Parameter Name. Index specifies the index of the parameter among all the parameters in the model. Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
|  | Name is the symbolic path of the parameter within the model in the format: Model Name (as specified in the model)/Block Name (if the parameter is a block parameter)/Parameter Name. |
|  | Index specifies the index of the parameter among all the parameters in the model. |
|  | Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
| 0 | Double—Double-precision, floating-point numeric. |
|  | Found? is TRUE if the component whose path you specify exists in the model. Otherwise, LabVIEW returns FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Signal Information by Path

Returns properties for a model signal.

[IMAGE alt='image' src='get_signal_information_by_path.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | Signal Path specifies the path of a signal within the model. You can use the Get Paths VI to return the paths of model components.If the model does not contain a component with the path you specify, Found? is FALSE and the Index element of the Signal Information output cluster is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Signal Information returns the following elements that describe the signal. Index is the index of the signal among all the signals in the model. Block Name is the path of the block from which the signal originates. This string is in the format of Model Name (as specified in the model)/Block Name. Port Number returns the port number of the signal. Signal Name returns the user-defined name of the signal. Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
|  | Index is the index of the signal among all the signals in the model. |
|  | Block Name is the path of the block from which the signal originates. This string is in the format of Model Name (as specified in the model)/Block Name. |
|  | Port Number returns the port number of the signal. |
|  | Signal Name returns the user-defined name of the signal. |
|  | Dimensions is an array whose elements are the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric. |
| 0 | Double—Double-precision, floating-point numeric. |
|  | Found? is TRUE if the component whose path you specify exists in the model. Otherwise, LabVIEW returns FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Information by Path Details

Related link: [Finding the Components of a Model](../vsmithelp/mit_finding_comps.html)

#### Example

Refer to the MIT Get Model Information VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Get Information by Path VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_model_period.html language=enus -->
## TOPIC 00037: Get Model Period VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_model_period.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_model_period.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Model Period VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Returns the rate, in seconds, at which the model was compiled to run.

A model is set to run at a certain rate, or step size, as defined in the build options when the model is compiled. However, the rate at which the Model Interface API actually steps the model is determined by how often the [Take Model Time Step](../vsmitref/take_model_time_step.html) VI executes in your application.

**Programming Patterns:** [Configuring Model Timing](../vsmithelp/mit_model_timing.html)

[Example](#examples)

[IMAGE alt='image' src='get_model_period.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Model Period (s) returns the base rate, in seconds, at which the model was compiled to run. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Simple Load and Run Model VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Get Model Period VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_outport.html language=enus -->
## TOPIC 00038: Get Outport VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_outport.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_outport.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Outport VI

**Owning Palette:** [Inports & Outports VIs](../vsmitref/mit_io_pal.html)

**Requires:** Model Interface Toolkit

Returns the value of the model outport specified by **Outport Information**.

[IMAGE alt='image' src='get_outport.gif']

|  | Outports Array in contains the values of all outports in the model. The format of this output is a flattened 1D array in column-major order. |
| --- | --- |
|  | Outport Information contains the following elements that describe the outport whose value you want to get. You can generate this cluster with the Get Information by Path VI. Path is the path of the component within the model. Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. offset is the position of the component within the flattened array of values the Model Interface API uses to return inport and outport values from the model. Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
|  | Path is the path of the component within the model. |
|  | Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | offset is the position of the component within the flattened array of values the Model Interface API uses to return inport and outport values from the model. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
| 0 | Double—Double-precision, floating-point numeric |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Outports Array out returns the values of all outports in the model. The format of this output is a flattened 1D array in column-major order. |
|  | Outport Value returns the value of the specified outport. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Outports Array out returns the values of all outports in the model. The format of this output is a flattened 1D array in column-major order. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_parameter.html language=enus -->
## TOPIC 00039: Get Parameter VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_parameter.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_parameter.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Parameter VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Returns the value of a specific model parameter.

This VI is intended for use in background-priority code, rather than in line with model time steps in the control loop. Therefore, the [Update Parameters In Line?](../vsmitref/mit_props.html) property must be FALSE when this VI runs. Otherwise, LabVIEW returns error -383700.

[Details](#details)  [Examples](#examples)

#### Get Parameter (Vector)

Gets the value of a vector parameter.

[IMAGE alt='image' src='get_parameter__vector.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | Parameter index specifies the index of the parameter among all the parameters in the model. Use the Get Information by Path VI to return the index of a parameter within a model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Parameter Interface out returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | Parameter value returns the value of the specified parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Parameter (Scalar)

Gets the value of a scalar parameter or a single element within a vector parameter.

[IMAGE alt='image' src='get_parameter__scalar.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | Parameter index specifies the index of the parameter among all the parameters in the model. Use the Get Information by Path VI to return the index of a parameter within a model. |
|  | Offset within parameter specifies the offset of an element you want to update within a vector parameter. The format of vector parameters is a flattened 1D array in column-major order. The default is 0. If the parameter you want to update is scalar, leave this value set to 0.You can use the Calculate Parameter Offset VI to calculate this value. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Parameter Interface out returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | Parameter value returns the value of the specified parameter or parameter element. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Parameter Details

This VI returns only parameter values you have committed with the [Commit Parameters](../vsmitref/commit_parameters.html) VI.

#### Examples

Refer to the following VIs for examples of using the Get Parameter VI:

- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface
- MIT Multiple Parameter VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_paths.html language=enus -->
## TOPIC 00040: Get Paths VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_paths.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_paths.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Paths VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Returns the paths of a specific type of component within the model.

You can use the path of a model component to [return properties](../vsmitref/get_information_by_path.html) of a component that other Model Interface VIs require.

[Details](#details)  [Examples](#examples)

#### Get Inport Paths

Returns the paths of all model inports.

[IMAGE alt='image' src='get_inport_paths.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Inport Paths returns an array whose elements are the paths of inports within the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Outport Paths

Returns the paths of all model outports.

[IMAGE alt='image' src='get_outport_paths.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Outport Paths returns an array whose elements are the paths of outports within the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Parameter Paths

Returns the paths of all model parameters.

[IMAGE alt='image' src='get_parameter_paths.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Parameter Paths returns an array whose elements are the paths of parameters within the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Signal Paths

Returns the paths of all model signals.

[IMAGE alt='image' src='get_signal_paths.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Signal Paths returns an array whose elements are the paths of signals within the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Paths Details

Related link: [Finding the Components of a Model](../vsmithelp/mit_finding_comps.html)

#### Examples

Refer to the following VIs for examples of using the Get Paths VI:

- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface
- MIT Signal Probes VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_probed_signal_values.html language=enus -->
## TOPIC 00041: Get Probed Signal Values VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_probed_signal_values.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_probed_signal_values.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Probed Signal Values VI

**Owning Palette:** [Signals VIs](../vsmitref/mit_signals_pal.html)

**Requires:** Model Interface Toolkit

Returns the values of signals in a model that you previously chose to probe. Each time this VI executes, it returns signal values from a particular time step, unless the VI times out.

Call the [Set Signals to Probe](../vsmitref/set_signals_to_probe.html) VI before this VI to configure the list of signals to probe.

|  | Note To improve performance in your application, only probe signals whose values you need. Probing many signals can decrease performance. |
| --- | --- |

**Programming Patterns:** [Probing Signal Values at Run Time](../vsmithelp/mit_model_signals.html)

[Details](#details)  [Example](#examples)

#### Get Probed Signal Values (Formatted)

Returns signal values in a formatted array of clusters in which the value for each signal is formatted as a separate 2D array.

[IMAGE alt='image' src='get_probed_signal_values__formatted.gif']

|  | Signal Interface in is a reference that allows you to access the signals in a model. To create this reference, you must create a signal interface. |
| --- | --- |
|  | Timeout (ms) specifies the maximum amount of time to wait for LabVIEW to return signal values from the model. If a timeout occurs, Timed out? is TRUE and Probed Data is empty. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Time (s) returns the elapsed time in the model, in seconds, when the model produced the signal values returned in Probed Data. This value is useful for allowing you to correlate events within the model with the time they occurred. |
|  | Signal Interface out returns a reference that allows you to access the signals in a model. Wire this output to other VIs from the Signals palette to interact with the signals. |
|  | Probed Data returns the value of each signal during a time step. The format of this output is a 1D array of clusters, where each cluster element is a 2D signal value for a specific signal from a specific time step. The Simulation Time (s) output indicates the time within the model at which the signal values occurred. |
|  | Timed out? is TRUE if LabVIEW does not return signal values within the Timeout (ms) you specify. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Packet Index returns the zero-based index of packets received for the signal probe session. |

#### Get Probed Signal Values (Raw)

Returns signal values in a [flattened 1D array in column-major order](../vsmithelp/mit_flattened_arrays.html). Use this instance when your application requires high performance.

[IMAGE alt='image' src='get_probed_signal_values__raw.gif']

|  | Signal Interface in is a reference that allows you to access the signals in a model. To create this reference, you must create a signal interface. |
| --- | --- |
|  | Timeout (ms) specifies the maximum amount of time to wait for LabVIEW to return signal values from the model. If a timeout occurs, Timed out? is TRUE and Probed Data is empty. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Time (s) returns the elapsed time in the model, in seconds, when the model produced the signal values returned in Probed Data. This value is useful for allowing you to correlate events within the model with the time they occurred. |
|  | Signal Interface out returns a reference that allows you to access the signals in a model. Wire this output to other VIs from the Signals palette to interact with the signals. |
|  | Probed Data returns values probed from each signal you set to probe during a particular time step. The format of this output is a flattened 1D array in column-major order. |
|  | Timed out? is TRUE if LabVIEW does not return signal values within the Timeout (ms) you specify. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Packet Index returns the zero-based index of packets received for the signal probe session. |

#### Get Probed Signal Values Details

Each time this VI executes, it returns signal values probed during the earliest time step for which LabVIEW stores signal data. You configure the maximum number of time steps for which LabVIEW stores signal values via the **Maximum Probed Data History** input of the [Set Signals to Probe](../vsmitref/set_signals_to_probe.html) VI.

#### Example

Refer to the MIT Signal Probes VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Get Probed Signal Values VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/get_simulation_time.html language=enus -->
## TOPIC 00042: Get Simulation Time VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/get_simulation_time.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/get_simulation_time.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Simulation Time VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Returns the elapsed time within the model, which can be different than real time. This VI allows you to correlate events within the model, such as specific outport values returned by the [Take Model Time Step](../vsmitref/take_model_time_step.html) VI, with the time they occurred.

[Example](#examples)

[IMAGE alt='image' src='get_simulation_time.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Simulation Time (s) returns the elapsed time, in seconds, within the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Parameter Sweep with F-16 Engine VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Get Simulation Time VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/load_model.html language=enus -->
## TOPIC 00043: Load Model VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/load_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/load_model.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Load Model VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Loads a model into memory and prepares it for execution. You must call this VI to load a model before you can execute the model in a control loop.

**Programming Patterns:** [Basic Architecture for Executing Models](../vsmithelp/mit_basic_design.html)

[Example](#examples)

[IMAGE alt='image' src='load_model.gif']

|  | Model Path specifies the path to the model you want to prepare for execution. Models must conform to the NI VeriStand Model Framework header file (NIVERISTAND_API.h). Otherwise, LabVIEW returns error code -383200. |
| --- | --- |
|  | Multirate Options contains the following elements for configuring how subsystems in a multirate model execute. If the model is single-rate, LabVIEW ignores these options. Processor identifies the processor you want to handle execution. Enter a number between 0 and 255, where 0 (default) represents the first processor. If you enter a number that exceeds the number of available processors, LabVIEW generates a run-time error. Priority specifies the priority of the execution of subsystems in the multirate model. The priority specifies when the subsystems execute relative to other objects on the block diagram. This value must be a positive integer between 1 and 65,535. |
|  | Processor identifies the processor you want to handle execution. Enter a number between 0 and 255, where 0 (default) represents the first processor. If you enter a number that exceeds the number of available processors, LabVIEW generates a run-time error. |
|  | Priority specifies the priority of the execution of subsystems in the multirate model. The priority specifies when the subsystems execute relative to other objects on the block diagram. This value must be a positive integer between 1 and 65,535. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Simple Load and Run Model VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Load Model VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/mit_io_pal.html language=enus -->
## TOPIC 00044: Inports & Outports VIs

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/mit_io_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/mit_io_pal.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inports & Outports VIs

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Inports & Outports VIs to initialize or get and set the values of inport and outports in a model.

| Palette Object | Description |
| --- | --- |
| Create Inports Array | Creates an array with the number of elements needed to represent the model inports. Every array element is initialized to 0. You can manipulate this array to set initial inport values prior to running the model. |
| Get Outport | Returns the value of the model outport specified by Outport Information. |
| Set Inport | Sets the value of the model inport specified by Inport Information. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/mit_param_pal.html language=enus -->
## TOPIC 00045: Parameters VIs

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/mit_param_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/mit_param_pal.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Parameters VIs

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Parameters VIs to set parameters in a model as the model executes. Choose the VIs you use to manage parameters according two factors: the time at which you want to change parameters (before or during execution) and the priority of the value changes.

**Programming Patterns:** [Initializing Parameter Values Before the Model Runs](../vsmithelp/mit_model_params_init.html), [Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

| Palette Object | Description |
| --- | --- |
| Calculate Parameter Offset | Calculates the position of an element within a flattened vector parameter. This offset position is required to update a single element of 2D vector parameters with the Set Parameter or Set Parameter Inline VIs. |
| Close Parameter Interface | Closes a reference to model parameters that you opened with the Create Parameter Interface VI. |
| Commit Parameters | Applies the value of any model parameters you previously set with the Set Parameter VI. |
| Create Parameter Interface | Creates a reference through which you manipulate the parameters of a model. Use the reference this VI creates to initialize parameters or update them from background-priority code as the model executes. |
| Get Parameter | Returns the value of a specific model parameter. |
| Set Parameter | Sets the value of a model parameter. First set new values with this VI, and then commit the new values with the Commit Parameters VI. |
| Set Parameter Inline | Updates a scalar parameter or a single element of a vector parameter. This VI is intended to be placed in line with the Take Model Time Step VI in the control loop to ensure that the model receives updates to parameter values during the same time step you set them. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/mit_props.html language=enus -->
## TOPIC 00046: Model Interface Toolkit Properties

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/mit_props.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/mit_props.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model Interface Toolkit Properties

The Model Interface Toolkit provides a class with properties you can use to get and set properties of a model reference. Use a Property Node to access the properties via the model reference wire that the Load Model VI generates and other Model Interface VIs use.

The following table describes the properties in the NI VeriStand Model Interface Toolkit class.

| Property | Permissions | Description |
| --- | --- | --- |
| Inport Paths | Read | Gets an array of inport paths. |
| Model Framework Version | Read | Gets the version number of the NI VeriStand Model Framework in which the model was compiled. |
| Model Period | Read | Gets the base rate of the model. |
| Multirate Timed Out? | Read | TRUE if a multirate model times out while waiting for its subsystems to complete execution. |
| Multirate Timeout (ms) | Read/write | Gets/sets the timeout duration for a multirate model in milliseconds. |
| Outport Paths | Read | Gets an array of outport paths. |
| Parameter Paths | Read | Gets an array of parameter paths. |
| Signal Paths | Read | Gets an array of signal paths. |
| Simulation Time | Read | Gets the simulation time of the model. |
| Update Parameters In Line? | Read/write | If TRUE, the Set Parameters Inline VI can set parameter values in the same control loop that steps the model. To set parameters from background-priority code with the Set Parameter VI, set this property to FALSE. Otherwise, LabVIEW returns an error. |

#### Example Code

The following block diagram shows a Property Node that sets and gets a few properties of a model reference.

[IMAGE alt='image' src='loc_bd_mit_props.gif']

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/mit_signals_pal.html language=enus -->
## TOPIC 00047: Signals VIs

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/mit_signals_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/mit_signals_pal.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Signals VIs

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Signals VIs to read values from signals in a model as the model executes.

**Programming Patterns:** [Probing Signal Values at Run Time](../vsmithelp/mit_model_signals.html)

| Palette Object | Description |
| --- | --- |
| Close Signal Interface | Closes a reference to model signals that you opened with the Create Signal Interface VI. |
| Create Signal Interface | Creates a reference through which you read from the signals in a model. Use the reference this VI creates to set a list of signals to read, then read their values from background-priority code as the model executes. |
| Format Raw Signal Values | Returns an unflattened version of the model signal values in the flattened Data Array in. This VI is useful if you want to read raw signal values quickly while the model executes and later reformat them offline for visualization. |
| Get Probed Signal Values | Returns the values of signals in a model that you previously chose to probe. Each time this VI executes, it returns signal values from a particular time step, unless the VI times out. Call the Set Signals to Probe VI before this VI to configure the list of signals to probe. |
| Set Signals to Probe | Sets which signals in a model you want to probe. After you set the signal list, the Get Probed Signal Values VI returns values for those signals as the model executes. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/set_inport.html language=enus -->
## TOPIC 00048: Set Inport VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/set_inport.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/set_inport.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Inport VI

**Owning Palette:** [Inports & Outports VIs](../vsmitref/mit_io_pal.html)

**Requires:** Model Interface Toolkit

Sets the value of the model inport specified by **Inport Information**.

[IMAGE alt='image' src='set_inport.gif']

|  | Inports Array in is the array that contains values for each inport in the model. The format of this input is a flattened 1D array in column-major order. |
| --- | --- |
|  | Inport Information contains the following elements that describe the inport whose value you want to set. You can generate this cluster with the Get Information by Path VI. Path is the path of the component within the model. Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. offset is the position of the component within the flattened array of values the Model Interface API uses to return inport and outport values from the model. Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
|  | Path is the path of the component within the model. |
|  | Dimensions is an array that contains the dimensions of the component. The first element is the number of columns, and the second element is the number of rows. |
|  | offset is the position of the component within the flattened array of values the Model Interface API uses to return inport and outport values from the model. |
|  | Type is the data type of the component. 0Double—Double-precision, floating-point numeric |
| 0 | Double—Double-precision, floating-point numeric |
|  | Inport Value specifies the value to apply to the inport. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Inports Array out returns the inports array with the new Inport Value inserted. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/set_parameter.html language=enus -->
## TOPIC 00049: Set Parameter VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/set_parameter.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/set_parameter.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Parameter VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Sets the value of a model parameter. First set new values with this VI, and then commit the new values with the [Commit Parameters](../vsmitref/commit_parameters.html) VI.

This VI is intended for use in background-priority code, rather than in line with model time steps in the control loop. Therefore, the [Update Parameters In Line?](../vsmitref/mit_props.html) property must be FALSE when this VI runs. Otherwise, LabVIEW returns error -383700.

**Programming Patterns:** [Initializing Parameter Values Before the Model Runs](../vsmithelp/mit_model_params_init.html), [Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

[Examples](#examples)

#### Set Parameter (Vector)

Sets the value of a vector parameter.

[IMAGE alt='image' src='set_parameter__vector.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | Parameter index specifies the index of the parameter among all the parameters in the model. Use the Get Information by Path VI to return the index of a parameter within a model. |
|  | Parameter value specifies the value to set for the parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Parameter Interface out returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Parameter (Scalar)

Sets the value of a scalar parameter or a single element within a vector parameter.

[IMAGE alt='image' src='set_parameter__scalar.gif']

|  | Parameter Interface in is a reference that allows you to access the parameters in a model. To create this reference, you must create a parameter interface. |
| --- | --- |
|  | Parameter index specifies the index of the parameter among all the parameters in the model. Use the Get Information by Path VI to return the index of a parameter within a model. |
|  | Parameter value specifies the value to set for the parameter or parameter element. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Offset within parameter specifies the offset of an element you want to update within a vector parameter. The format of vector parameters is a flattened 1D array in column-major order. The default is 0. If the parameter you want to update is scalar, leave this value set to 0.You can use the Calculate Parameter Offset VI to calculate this value. |
|  | Parameter Interface out returns a reference that allows you to access the parameters in a model. Wire this output to other VIs from the Parameters palette to interact with the parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Set Parameter VI:

- MIT Multiple models VI: labview\examples\Control and Simulation\Model Interface
- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/set_parameter_inline.html language=enus -->
## TOPIC 00050: Set Parameter Inline VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/set_parameter_inline.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/set_parameter_inline.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Parameter Inline VI

**Owning Palette:** [Parameters VIs](../vsmitref/mit_param_pal.html)

**Requires:** Model Interface Toolkit

Updates a scalar parameter or a single element of a vector parameter. This VI is intended to be placed in line with the [Take Model Time Step](../vsmitref/take_model_time_step.html) VI in the control loop to ensure that the model receives updates to parameter values during the same time step you set them.

|  | Note Using this VI with models compiled to work with the NI VeriStand 2012 Model Framework or earlier negatively impacts performance of the application. National Instruments recommends that you recompile models to work with the latest version of the NI VeriStand Model Framework.Calling this VI frequently can decrease the performance of the control loop.The Update Parameters In Line? property must be TRUE when this VI runs. Otherwise, LabVIEW returns error code -383700. |
| --- | --- |

**Programming Patterns:** [Updating Parameters While a Model Runs](../vsmithelp/mit_model_params_run.html)

[IMAGE alt='image' src='set_parameter_inline.gif']

|  | Model In specifies the model from which you want to subtract information. |
| --- | --- |
|  | Parameter index specifies the index of the parameter among all the parameters in the model. Use the Get Information by Path VI to return the index of a parameter within a model. |
|  | Parameter value specifies the value to set for the parameter or parameter element. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Offset within parameter specifies the offset of an element you want to update within a vector parameter. The format of vector parameters is a flattened 1D array in column-major order. The default is 0. If the parameter you want to update is scalar, leave this value set to 0.You can use the Calculate Parameter Offset VI to calculate this value. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/set_signals_to_probe.html language=enus -->
## TOPIC 00051: Set Signals to Probe VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/set_signals_to_probe.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/set_signals_to_probe.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Signals to Probe VI

**Owning Palette:** [Signals VIs](../vsmitref/mit_signals_pal.html)

**Requires:** Model Interface Toolkit

Sets which signals in a model you want to probe. After you set the signal list, the [Get Probed Signal Values](../vsmitref/get_probed_signal_values.html) VI returns values for those signals as the model executes.

To change the signals for which the [Get Probed Signal Values](../vsmitref/get_probed_signal_values.html) VI returns values, call this VI again with a new list of **Signal Paths**.

**Programming Patterns:** [Probing Signal Values at Run Time](../vsmithelp/mit_model_signals.html)

[Example](#examples)

[IMAGE alt='image' src='set_signals_to_probe.gif']

|  | Maximum Probed Data History specifies the maximum number of model time steps from which you want to store signal values in a buffer. The default is 10. If you find the Get Probed Signal Values VI loses signal values because it does not execute before the buffer overflows, you can increase this value. |
| --- | --- |
|  | Signal Interface in is a reference that allows you to access the signals in a model. To create this reference, you must create a signal interface. |
|  | Signal Paths is an array of paths for the signals you want to probe. You can use the Get Paths VI to return signal paths from the model. |
|  | Timeout (ms) specifies the maximum amount of time to wait for LabVIEW to configure the list of signals to probe. If a timeout occurs, Timed out? is TRUE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Decimation (1) specifies the decimation factor for the probes. You can set a decimation to probe signals at a slower rate than the model is running. For example, if you set the decimation to 10, LabVIEW probes the signals for 1 out of every 10 model time steps. |
|  | Signal Interface out returns a reference that allows you to access the signals in a model. Wire this output to other VIs from the Signals palette to interact with the signals. |
|  | Timed out? is TRUE if LabVIEW does not set the list of signals to probe within the Timeout (ms) you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Signal Probes VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Set Signals to Probe VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/take_model_time_step.html language=enus -->
## TOPIC 00052: Take Model Time Step VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/take_model_time_step.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/take_model_time_step.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Take Model Time Step VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Writes to model inports, runs the model for one time step, and returns values from outports.

|  | Tip You can call the Get Simulation Time VI after this VI executes to track the internal time within the model. |
| --- | --- |

**Programming Patterns:** [Basic Architecture for Executing Models](../vsmithelp/mit_basic_design.html)

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='take_model_time_step.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | Inport Array specifies the values to write to the inports in the model. The format of this input is a flattened 1D array in column-major order. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model out is a reference to a specific model in memory. Wire this output to other Model Interface VIs to interact with the model. |
|  | Outports Array out returns the values of all outports in the model. The format of this output is a flattened 1D array in column-major order. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Take Model Time Step Details

Wires that connect terminals of the Take Model Time Step VI within a loop to terminals of objects outside of the loop must pass through a shift register rather than a tunnel for VeriStand to process the model correctly. Unlike shift registers, tunnels do not allow data from one iteration to carry over to the next causing the output value of the model to remain at zero.

#### Examples

Refer to the following VIs for examples of using the Take Model Time Step VI:

- MIT Parameter Management VI: labview\examples\Control and Simulation\Model Interface
- MIT Multiple models VI: labview\examples\Control and Simulation\Model Interface

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/unload_model.html language=enus -->
## TOPIC 00053: Unload Model VI

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/unload_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/unload_model.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Unload Model VI

**Owning Palette:** [Model Interface VIs](../vsmitref/vsmitref.html)

**Requires:** Model Interface Toolkit

Unloads a model from memory that you previously loaded with the [Load Model](../vsmitref/load_model.html) VI.

**Programming Patterns:** [Basic Architecture for Executing Models](../vsmithelp/mit_basic_design.html)

[Example](#examples)

[IMAGE alt='image' src='unload_model.gif']

|  | Model in is a reference to a model in memory. You must load a model to create this reference. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the MIT Simple Load and Run Model VI in the labview\examples\Control and Simulation\Model Interface directory for an example of using the Unload Model VI.

<!--NI_TOPIC bundle=labview-model-interface-toolkit-api-ref path=vsmitref/vsmitref.html language=enus -->
## TOPIC 00054: Model Interface VIs

- bundle_id: `labview-model-interface-toolkit-api-ref`
- source_path: `vsmitref/vsmitref.html`
- source_url: https://docs-be.ni.com/bundle/labview-model-interface-toolkit-api-ref/raw/resource/enus/vsmitref/vsmitref.html
- document_id: `labview-model-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model Interface VIs

August 2014, 374167B-01

**Requires:** Model Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Model Interface VIs to run and interact with models from a variety of simulation environments and programming languages in your development, prototyping, and testing of control systems.

**Programming Patterns:** [Basic Architecture for Executing Models](../vsmithelp/mit_basic_design.html)

| Palette Object | Description |
| --- | --- |
| Call Model Start Routine | Executes initialization code defined in the model-start function of a model. |
| Get Information by Path | Returns properties of a specific component of a model, such as an inport or parameter, that you can pass to other VIs to interact with the component. |
| Get Model Period | Returns the rate, in seconds, at which the model was compiled to run. |
| Get Paths | Returns the paths of a specific type of component within the model. |
| Get Simulation Time | Returns the elapsed time within the model, which can be different than real time. This VI allows you to correlate events within the model, such as specific outport values returned by the Take Model Time Step VI, with the time they occurred. |
| Load Model | Loads a model into memory and prepares it for execution. You must call this VI to load a model before you can execute the model in a control loop. |
| Take Model Time Step | Writes to model inports, runs the model for one time step, and returns values from outports. |
| Unload Model | Unloads a model from memory that you previously loaded with the Load Model VI. |

| Subpalette | Description |
| --- | --- |
| Inports & Outports VIs | Use the Inports & Outports VIs to initialize or get and set the values of inport and outports in a model. |
| Parameters VIs | Use the Parameters VIs to set parameters in a model as the model executes. Choose the VIs you use to manage parameters according two factors: the time at which you want to change parameters (before or during execution) and the priority of the value changes. |
| Signals VIs | Use the Signals VIs to read values from signals in a model as the model executes. |

© 2013-2014 National Instruments. All rights reserved.
