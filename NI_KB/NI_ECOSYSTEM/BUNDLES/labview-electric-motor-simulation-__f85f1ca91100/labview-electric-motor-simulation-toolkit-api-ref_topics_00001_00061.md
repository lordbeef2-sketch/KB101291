# NI DOCUMENT BUNDLE: labview-electric-motor-simulation-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-electric-motor-simulation-toolkit-api-ref start=1 end=61 -->
<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_hil.html language=enus -->
## TOPIC 00001: Composing a Real HIL System with I/O Modules (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_hil.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_hil.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Composing a Real HIL System with I/O Modules (Electric Motor Simulation Toolkit)

In real hardware-in-the-loop (HIL) systems, the controller and simulator are usually on separate hardware. The I/O modules between the hardware connect the controller and simulator in a closed-loop.

In this step, you run the LabVIEW sample project wizard to create an Electric Motor Simulation sample project, in which you configure the I/O modules as well. Refer to the sample project documentation for information about connecting the controller, simulator, and I/O modules. You also can replace the control algorithm with your own code, run the solution, and verify the control algorithm.

#### Simulating on FPGA Targets

The following illustration describes a real HIL system where the simulator is on an FPGA target.

[IMAGE alt='image' src='loc_eps_hil_fpga.gif']

In a real HIL system, the simulator runs on an FPGA target and the controller runs on a real-time (RT) CompactRIO target. The host computer can be a desktop PC or a PXI target. If the host computer is a desktop PC, the FPGA target must run on a separate RT target. If the host computer is a PXI target, the FPGA target can either run on the host computer or a separate RT PXI target.

The following steps describe the workflow of an HIL system.

1. On the host computer, you run a main VI which provides a user interface for you to specify the motor parameters, change the velocity setpoint, and monitor the motor state.
2. The host computer sends commands, such as velocity setpoint changes, to the RT CompactRIO target through network stream.
3. The controller reads motor status from the simulator and writes the control commands back to the simulator through I/O modules.
4. The host computer reads the latest motor status directly from the simulator.

#### Simulating on Real-Time Targets

The following illustration describes a real HIL system where the simulator is on a real-time target.

[IMAGE alt='image' src='loc_eps_hil_rt.gif']

In this HIL system, the simulator runs on an RT PXI target while the controller runs on an RT CompactRIO target. The following steps describe the workflow of electric motor simulation on RT targets.

1. On the host computer, you run a main VI which provides a user interface for you to specify the motor parameters, change the velocity setpoint, and monitor the motor state.
2. The host computer sends commands of velocity setpoint changes to the RT CompactRIO through network stream.
3. The host computer sends commands of load torque changes to the RT PXI target through network stream.
4. The controller reads motor status from the simulator and writes control commands back to the simulator through I/O modules.
5. The host computer reads the latest motor status from the RT PXI target by using the shared variables.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_model.html language=enus -->
## TOPIC 00002: Choosing a Simulation Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Choosing a Simulation Model (Electric Motor Simulation Toolkit)

When you simulate an electric motor, you have multiple choices of the motor model functions. This topic gives a brief introduction to the built-in models of this toolkit and provides a comparison among different models to help you decide which one to choose.

The Electric Motor Simulation Toolkit allows you to simulate an AC Induction Motor (ACIM) using the constant parameter model.

To simulate a permanent magnet synchronous motor (PMSM), you can use either of the following models.

- Constant parameter model
- Variable parameter model
- Finite element analysis (FEA) model

For a switched reluctance motor (SRM), you can simulate the motor using either of the following models.

- Linear model
- FEA model

#### Comparing the Models

|  | Constant parameter model / Linear model | Variable parameter model | FEA model |
| --- | --- | --- | --- |
| Requirements | Requires various parameters of the motor. | Requires RTT files, ANSYS motor model files, or external models that contain motor parameters information. | Requires RTT files which describe the FEA model. |
| Resources | Involves relatively smaller amount of calculations and thus requires less resources. | Involves medium amount of calculations. Requires more resources than the constant parameter model and less resources than the FEA model. | Involves heavy calculations and a more complex algorithm. Requires more resources when you compile the code on FPGA targets. |
| Fidelity | Lowest. | Medium. | Highest. The simulation is very close to the real-world situation. |

##### Related Information

[Constant Parameter Model](../lvemsimshared/cons_para_model.html)

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[Linear Model](../lvemsimshared/line_model.html)

[FEA Model](../lvemsimshared/fea_model.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_overview.html language=enus -->
## TOPIC 00003: Getting Started with Electric Motor Simulation (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_overview.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Getting Started with Electric Motor Simulation (Electric Motor Simulation Toolkit)

The Electric Motor Simulation Toolkit provides built-in models for the simulation. You can simulate an AC induction motor (ACIM), a permanent magnet synchronous motor (PMSM), or a switched reluctance motor (SRM) using this toolkit. The following sections describe the process you use to simulate an ACIM, a PMSM, or an SRM in LabVIEW.

#### Simulating an ACIM

You can simulate an ACIM by using the constant parameter model function. Use the following flowchart to learn the process of simulating an ACIM. Click on a shape for more information about each concept or simulation process.

[IMAGE alt='image' src='loc_eps_acim_process.gif']

#### Simulating a PMSM

You can simulate a PMSM using the constant parameter model function, the variable parameter model function, or the finite element analysis (FEA) model function. Use the following flowchart to learn the process of identifying a model and simulating a PMSM. Click on a shape for more information about each concept or simulation process.

[IMAGE alt='image' src='loc_eps_pmsm_process.gif']

#### Simulating an SRM

You can simulate an SRM using either the linear model function or the FEA Model function. Use the following flowchart to learn the process of identifying a model and simulating an SRM. Click on a shape for more information about each concept or simulation process.

[IMAGE alt='image' src='loc_eps_srm_process.gif']

Read through the following topics to simulate an electric motor using the Electric Motor Simulation Toolkit.

- Choosing a Simulation Model
- Preparing the Motor Model
- Controlling an Electric Motor
- Simulating an Electric Motor on FPGA or Real-Time Targets
- Composing a Real HIL System with I/O Modules

##### Related Information

[Supported Motor Types](../lvemsimshared/motor_type.html)

[Constant Parameter Model](../lvemsimshared/cons_para_model.html)

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[FEA model](../lvemsimshared/fea_model.html)

[Linear model](../lvemsimshared/line_model.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_related_doc.html language=enus -->
## TOPIC 00004: Related Documentation (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_related_doc.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Electric Motor Simulation Toolkit)

The following documents contain information that you might find helpful as you use the Electric Motor Simulation Toolkit.

- Electric Motor Simulation Toolkit Readme —Use this file to obtain introductory information about the Electric Motor Simulation Toolkit, such as a product overview, system requirements, installation instructions, activation instructions, help resources, and known issues. You can access this readme by navigating to the labview\readme directory and opening readme_EMSim.html .
- Electric Motor Simulation Toolkit Example VIs—Refer to the labview\examples\Electric Motor Simulation directory for example VIs that demonstrate how to perform common tasks using the Electric Motor Simulation Toolkit. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and navigating to the Toolkits and Modules»Electric Motor Simulation Toolkit folder in the NI Example Finder window.
- Electric Motor Simulation Toolkit Sample Project Documentation—Refer to the sample project documentation to understand the purpose of each sample project and to use the sample project to get started with LabVIEW and the Electric Motor Simulation Toolkit. Find the sample project documentation under the Project Documentation folder in the Project Explorer window of the sample project that you create.
- Additional LabVIEW documentation .

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_rtt.html language=enus -->
## TOPIC 00005: Preparing the Motor Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_rtt.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_rtt.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Preparing the Motor Model (Electric Motor Simulation Toolkit)

To simulate an electric motor, you must prepare the parameters and data pertaining to the motor model that you want to use. Different models require different resources at the preparation stage. This topic introduces you to the basis of obtaining the motor parameters and raw data.

#### Reading the Constant Parameters

To use the constant parameter model or linear model, you must know the parameters of the electric motor that you want to simulate. The simulator VI reads the motor parameters and imitates the behavior of a real motor.

The following figure is an example showing how the simulator VI reads the motor parameters. In this example, the simulator VI is PMSM Constant Parameter Model.vi. You must specify the motor parameters, such as the number of poles, resistance, inductance, and flux linkage, to the simulator VI.

[IMAGE alt='image' src='loc_bd_cons_para.gif']

##### Related Information

[Constant Parameter Model](../lvemsimshared/cons_para_model.html)

[Linear Model](../lvemsimshared/line_model.html)

[PMSM Constant Parameter Model VI](../lvemsimvi/pmsm_cons_para_model.html)

#### Reading an RTT File Using LabVIEW VIs

To use the finite element analysis (FEA) model or the variable parameter model, you can read the motor parameters and raw data from an RTT file.

With the Electric Motor Simulation Toolkit, you can read an RTT file to get a LabVIEW class reference of the model. The LabVIEW class reference contains the motor parameters in the LabVIEW format (lvclass), which is useful for the simulator VIs to obtain characteristics of the electric motor.

The following figure is an example showing how to read the RTT file and use the LabVIEW class reference with the simulator VI.

[IMAGE alt='image' src='loc_bd_read_rtt.gif']

The illustration shows the following sequence of steps:

1. The Create PMSM FEA Model.vi reads the RTT file to get the motor parameters and data.
2. The simulator VI uses the motor parameters and data that the previous part of this program reads to simulate the behavior of a motor. In this case, the simulator VI is the PMSM FEA Model.vi.

|  | Note If you are simulating a PMSM with the variable parameter model, use the Create PMSM Variable Parameter Model.vi to read the RTT file. If you are simulating an SRM with the FEA model, use the Read SRM RTT File.vi to read the RTT file. |
| --- | --- |

##### Related Information

[FEA Model](../lvemsimshared/fea_model.html)

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[Create PMSM FEA Model VI](../lvemsimvi/create_pmsm_fea_model.html)

[PMSM FEA Model VI](../lvemsimvi/pmsm_fea_model.html)

[Read SRM RTT File VI](../lvemsimvi/read_srm_rtt_file.html)

#### Reading an ANSYS Motor Model File Using LabVIEW VIs

To use the variable parameter model for simulating permanent magnet synchronous motors (PMSM), you can read the motor parameters and raw data from an ANSYS motor model file.

With the Electric Motor Simulation Toolkit, you can read an ANSYS motor model file to get a LabVIEW class reference of the PMSM variable parameter model. The LabVIEW class reference contains the motor parameters in the LabVIEW format (lvclass). The format is useful for the simulator VIs to obtain characteristics of the electric motor.

The following figure is an example showing how to read an ANSYS motor model file and use the LabVIEW class reference with the simulator VI.

[IMAGE alt='image' src='loc_bd_vari_ansys.gif']

The illustration shows the following sequence of steps:

1. The Create PMSM Variable Parameter Model.vi reads the ANSYS motor model file to get the motor parameters and data.
2. The simulator VI uses the motor parameters and data that the previous part of this program reads to simulate the behavior of a motor. In this case, the simulator VI is the PMSM Variable Parameter Model.vi.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[Create PMSM Variable Parameter Model VI](../lvemsimvi/create_pmsm_variable_parameter_model.html)

[PMSM Variable Parameter Model VI](../lvemsimvi/pmsm_vari_para_model.html)

#### Importing an External Model

To use the variable parameter model, you can get the motor parameters and raw data by importing an external model.

With the Electric Motor Simulation Toolkit, you can import an external model to generate a LabVIEW class reference of the variable parameter model. The LabVIEW class reference contains the motor parameters in the LabVIEW format (lvclass). The format is useful for the simulator VIs to obtain characteristics of the electric motor.

The following figure is an example showing how to import an external model and use the LabVIEW class reference with the simulator VI.

[IMAGE alt='image' src='loc_bd_vari_ext.gif']

The illustration shows the following sequence of steps:

1. The Create PMSM Variable Parameter Model.vi imports the external model to get the motor parameters and data.
2. The simulator VI uses the motor parameters and data that the previous part of this program reads to simulate the behavior of a motor. In this case, the simulator VI is the PMSM Variable Parameter Model.vi.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[Create PMSM Variable Parameter Model VI](../lvemsimvi/create_pmsm_variable_parameter_model.html)

[PMSM Variable Parameter Model VI](../lvemsimvi/pmsm_vari_para_model.html)

#### Related Examples

Refer to the following open-loop examples that you install along with this toolkit to get familiar with preparing the motor models.

- ACIM Open Loop Simulation VI in the labview\examples\Electric Motor Simulation\ACIM\ACIM Open Loop Simulation directory: 
 Open example 
 Find related examples
- PMSM Open Loop Simulation VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation directory: 
 Open example 
 Find related examples
- SRM Open Loop Simulation VI in the labview\examples\Electric Motor Simulation\SRM\SRM Open Loop Simulation directory: 
 Open example 
 Find related examples

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_sim_desktop.html language=enus -->
## TOPIC 00006: Controlling an Electric Motor (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_sim_desktop.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_sim_desktop.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Controlling an Electric Motor (Electric Motor Simulation Toolkit)

After choosing a simulation model and obtaining the necessary motor parameters, you can add a control terminal to the simulator. The control terminal, or the controller, contains control algorithms which manipulate all the calculations related to the simulator.

For hardware-in-the-loop (HIL) simulation, the controller and simulator work in a closed-loop system.

#### Closed-Loop Control System

Closed-loop control systems are systems with feedback. Feedback is a process in which the output signal of a dynamic system is passed, or fed back, to the input to regulate the next output. In a closed-loop control system, the controller gets speed feedback from the electric motor and keeps the motor running at a velocity approximately equal to the velocity setpoint.

The following figure shows a closed-loop system that consists of a controller and an electric motor.

[IMAGE alt='image' src='loc_eps_close_loop.gif']

In the electric motor simulation, the motor is usually not a real electric motor, but a simulated motor. If you use the Electric Motor Simulation Toolkit, replace the simulated motor with a simulator VI. The toolkit provides the following VIs for simulating electric motors.

- ACIM Constant Parameter Model VI
- PMSM Constant Parameter Model VI
- PMSM Variable Parameter Model VI
- PMSM FEA Model VI
- SRM Linear Model VI
- SRM FEA Model VI

The following process describes how a controller controls the motor velocity in a closed-loop system.

1. The controller sends a control message through the inverter to the motor.
2. The motor speeds up or down based on the control message.
3. The motor returns the motor state to a device which estimates the velocity on the basis of the motor state. If you simulate on a host computer, use the Motor Speed and Rotor Position VI to estimate the rotor velocity.
4. The device returns the velocity back to the velocity setpoint.
5. If the rotor velocity does not reach the velocity setpoint, the controller sends a new message to update the motor velocity.

The speed control algorithm ensures that the rotor velocity approaches the velocity setpoint. In other words, the electric motor is eventually running at the velocity that is approximately equal to the velocity setpoint.

#### Related Examples

This toolkit provides the following closed-loop examples for controlling a simulated motor on the host computer.

- ACIM Constant Parameter Model Closed Loop VI in the labview\examples\Electric Motor Simulation\ACIM\ACIM Constant Parameter Model Closed Loop directory: 
 Open example 
 Find related examples
- PMSM FEA Model Closed Loop VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Closed Loop directory: 
 Open example 
 Find related examples
- PMSM Variable Parameter Model Closed Loop VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM Variable Parameter Model Closed Loop directory: 
 Open example 
 Find related examples
- PMSM Constant Parameter Model Closed Loop VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM Constant Parameter Model Closed Loop directory: 
 Open example 
 Find related examples
- SRM FEA Model Closed Loop Control VI in the labview\examples\Electric Motor Simulation\SRM\SRM FEA Model Closed Loop Control directory: 
 Open example 
 Find related examples
- SRM Linear Model Closed Loop Control VI in the labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Closed Loop Control directory: 
 Open example 
 Find related examples

##### Related Information

[Motor Speed and Rotor Position VI](../lvemsimvi/motor_speed_rotor_position.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_sim_fpga.html language=enus -->
## TOPIC 00007: Simulating an Electric Motor on FPGA or Real-Time Targets (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_sim_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_sim_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulating an Electric Motor on FPGA or Real-Time Targets (Electric Motor Simulation Toolkit)

In real electric motor simulation, the simulated motor is usually on an FPGA target or a real-time target. Instead of happening on host computers, the simulation happens on FPGA or real-time targets because the electric motor simulation requires a very high speed of processing data, which is unable to achieve on host computers. Therefore, after testing the control algorithms on host computers, you can move the simulated motor to FPGA or real-time targets.

Compared with real-time targets, simulation on FPGA targets yields better performance, efficiency, and determinism. However, due to the complexity of simulation on FPGA targets, you need to test the control algorithms with a simpler solution without getting your solution equipped with real I/O modules.

#### Testing Simulation on FPGA Targets

Use the control algorithms that you verified in the previous step of *Controlling an Electric Motor* to control a simulated motor on an FPGA target. In this step, you must compile the simulator VIs on the host computer into a bitfile. Download the bitfile to an FPGA target and run the simulator VIs on the FPGA target. In this way, you can verify if the FPGA simulator VIs are correct.

Correct FPGA code must be able to control the speed of the simulated motor. The simulated motor must run at a velocity that is approximately equal to the velocity setpoint.

##### Related Examples

The Electric Motor Simulation Toolkit provides the following examples for comparing the simulation outputs on a host computer and on an FPGA target.

- ACIM FPGA Verification.lvproj in the labview\examples\Electric Motor Simulation\ACIM\ACIM FPGA Verification directory: 
 Open example 
 Find related examples
- PMSM FPGA Verification.lvproj in the labview\examples\Electric Motor Simulation\PMSM\PMSM FPGA Verification directory: 
 Open example 
 Find related examples

The Electric Motor Simulation Toolkit provides the following examples for simulating electric motors in closed-loop control on FPGA targets.

- ACIM Constant Parameter Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\ACIM\ACIM Constant Parameter Model Control Simulation directory: 
 Open example 
 Find related examples
- PMSM Constant Parameter Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\PMSM\PMSM Constant Parameter Model Control Simulation directory: 
 Open example 
 Find related examples
- PMSM FEA Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Control Simulation directory: 
 Open example 
 Find related examples
- PMSM Variable Parameter Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\PMSM\PMSM Variable Parameter Model Control Simulation directory: 
 Open example 
 Find related examples
- SRM Linear Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Control Simulation directory: 
 Open example 
 Find related examples
- 3-Phase SRM Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\SRM\3-phase SRM Control Simulation directory: 
 Open example 
 Find related examples
- 4-Phase SRM Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\SRM\4-phase SRM Control Simulation directory: 
 Open example 
 Find related examples
- 5-Phase SRM Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\SRM\5-phase SRM Control Simulation directory: 
 Open example 
 Find related examples

#### Simulating on Real-Time Targets

While simulating on the real-time targets, you download the simulator VIs to a real-time target similar to simulating on the FPGA targets. The solution is relatively simpler. You do not need to test the simulation without I/O modules. Use the Electric Motor Simulation sample project to simulate a motor and compose a hardware-in-the-loop system with I/O modules.

To create a sample project for simulation on real-time targets, select **Simulate motor on RT** as the hardware setting on the **Configure your new project** page. Refer to the sample project documentation for details about connecting the hardware by I/O modules, adapting the sample project to hardware, and running the simulation. Find an illustration about the simulation system in the *Composing a Real HIL System with I/O Modules* topic.

##### Related Information

[Controlling an Electric Motor](../lvemsim/emsim_sim_desktop.html)

[Real-Time Target](/csh?topicname=lvrthelp/rt_computing_devices.html)

[Composing a Real HIL System with I/O Modules](../lvemsim/emsim_hil.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial.html language=enus -->
## TOPIC 00008: Electric Motor Simulation Tutorials (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Electric Motor Simulation Tutorials (Electric Motor Simulation Toolkit)

Use the following two tutorials to learn the basis of simulating electric motors by using the Electric Motor Simulation Toolkit. These tutorials assume that you have fundamental knowledge about the hardware-in-the-loop (HIL) testing and using the LabVIEW FPGA Module.

- Simulating an SRM with the Linear Model
- Simulating a PMSM with the FEA Model

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_pmsm.html language=enus -->
## TOPIC 00009: Simulating a PMSM with the FEA Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_pmsm.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_pmsm.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulating a PMSM with the FEA Model (Electric Motor Simulation Toolkit)

In this tutorial, you design an application to simulate a permanent magnet synchronous motor (PMSM) and compose an HIL system with I/O modules. Use the finite element analysis (FEA) model function to simulate the PMSM. You can use the built-in examples and sample project that this toolkit provides to simulate the motor in an HIL system. After completing this tutorial, you can replace the control algorithms with your new electric control unit (ECU) control algorithms according to your application requirements.

This tutorial consists of the following parts:

1. Testing the FEA Model
2. Testing the Control Algorithms
3. Simulating a PMSM on an FPGA Target
4. Composing a Real HIL System

##### Related Information

[FEA Model](../lvemsimshared/fea_model.html)

[Getting Started with Electric Motor Simulation](../lvemsim/emsim_overview.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_pmsm_1.html language=enus -->
## TOPIC 00010: Part 1: Testing the FEA Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_pmsm_1.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_pmsm_1.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 1: Testing the FEA Model (Electric Motor Simulation Toolkit)

To get prepared with the FEA model simulation, you need to test the model function by reading an RTT file with LabVIEW. You can either download RTT files at www.jmag-international.com or create an RTT file by using the JMAG-RT software.

Complete the following steps to read the RTT file and test the FEA model function.

1. Open the PMSM Open Loop Simulation VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation directory. 
 Open example 
 Find related examples
2. On the block diagram, specify an RTT file to the input of the Read PMSM RTT File VI. For this example, use the 1k_S_D_IV.rtt file in the labview\examples\Electric Motor Simulation\PMSM\_RTT Files directory.
3. Run the PMSM Open Loop Simulation VI.
4. On the front panel, observe the results returned from the Voltage [V] indicator. You can see that the input voltage is three-phase alternating voltage.
5. On the front panel, the output of three-phase current for the three model functions displays in different colors. Select the FEA Ia , FEA Ib , and FEA Ic channels to see the simulated current output with the FEA model.
6. Observe the results returned from the Torque [Nm] indicator. Choose the FEA channel to see the simulated torque output with the FEA model.

When you run this example, the output voltage, current, and torque appear as shown in the following screenshot.

[IMAGE alt='image' src='loc_fp_openloop.gif']

##### Related Information

[FEA Model](../lvemsimshared/fea_model.html)

[Create PMSM FEA Model VI](../lvemsimvi/create_pmsm_fea_model.html)

[PMSM FEA Model VI](../lvemsimvi/pmsm_fea_model.html)

| Part 2: Testing the Control Algorithms |
| --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_pmsm_2.html language=enus -->
## TOPIC 00011: Part 2: Testing the Control Algorithms (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_pmsm_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_pmsm_2.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 2: Testing the Control Algorithms (Electric Motor Simulation Toolkit)

Before simulating an electric motor, you must test your control algorithms on a host computer without connecting to any targets. Testing the control algorithms on host computers saves the workload of simulation on FPGA targets.

This toolkit provides built-in examples to help you get familiar with testing the control algorithms. In this example, your control algorithms are written in a closed-loop control system with the LabVIEW VIs and functions. With the help of this example, you can learn how the control algorithms work with the simulator VI.

Complete the following steps to test the control algorithms in the closed-loop example.

1. Open the PMSM FEA Model Closed Loop VI in the labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Closed Loop directory. 
 Open example 
 Find related examples
2. Run the example VI.
3. Observe the results returned from the Rotor Velocity [RPM] indicator. The blue wave is the velocity setpoint that you specified, while the red wave is the velocity of the motor. You can see that the motor speed is gradually getting closer to the velocity setpoint.
4. On the Motor tab, change the Velocity Setpoint [RPM] to 1500 .
5. Observe the changes of Rotor Velocity [RPM] . The velocity setpoint is 1,500 and the motor speed is very close to 1,500.
6. Change the Velocity Setpoint [RPM] to a negative value and observe the changes of the motor speed.
7. Change the Load Torque [Nm] . The motor adjusts the speed to keep approaching the velocity setpoint.
8. Click the Inverter tab. Set the Inverter Type to Advanced . Choose a Fault Type . Observe the results returned from the indicators.
9. Click the Temperature tab. Change the Coil Temperature [K] and the Magnet Temperature [K] .
10. Click Stop to stop the example.

Open the block diagram of the PMSM FEA Model Closed Loop VI to view how the control algorithms work with the simulator VI. You can modify the control algorithms in this example to meet your application requirements. You also can replace the control algorithm with your new electric control unit (ECU) control algorithms and test if the control algorithms work with the simulator.

| Part 1: Testing the FEA Model | Part 3: Simulating a PMSM on an FPGA Target |
| --- | --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_pmsm_3.html language=enus -->
## TOPIC 00012: Part 3: Simulating a PMSM on an FPGA Target (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_pmsm_3.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_pmsm_3.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 3: Simulating a PMSM on an FPGA Target (Electric Motor Simulation Toolkit)

In this part, you can verify whether the algorithm can perform correctly with the hardware-in-the-loop (HIL) solution. Before getting your solution equipped with the real I/O modules, you need to test your algorithm with a simpler solution on an FPGA target.

Complete the following steps to simulate a permanent magnet synchronous motor (PMSM) on an FPGA target.

1. Open PMSM FEA Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Control Simulation directory: 
 Open example 
 Find related examples
2. In the Project Explorer window, right-click the RT PXI Target and select Properties from the shortcut menu to open the Real-Time PXI Properties dialog box.
3. In the IP Address/DNS Name field, enter the IP address for the real-time target.
4. In the Project Explorer window, right-click the FPGA Target and select Properties from the shortcut menu to open the FPGA Target Properties dialog box.
5. In the Resource field, specify the FPGA target hardware.
6. In the Project Explorer window, navigate to RT PXI Target»FPGA Target»Build Specifications»PMSM FEA Model Simulator . Right-click the build specification and select Build from the shortcut menu.
7. Compile the FPGA code.
8. In the Project Explorer window, right-click the PMSM FEA Model Controller VI and select Deploy from the shortcut menu to deploy the VI to the real-time target.
9. Open the PMSM FEA Model Controller Simulation VI.
10. On the front panel, enter the name of the real-time target in Machine Alias .
11. Run the PMSM FEA Model Control Simulation VI.
12. On the front panel of the PMSM FEA Model Controller VI, click Enable Control . The real-time controller supplies control signals to the simulated motor and the motor starts running at a fixed velocity.
13. Adjust the Velocity Setpoint [RPM] and Load Torque [Nm] on the Motor tab. Verify if the output of motor speed is still approaching the value of the velocity setpoint.
14. Click the Inverter tab. Set the Inverter Type to Advanced . Choose a Fault Type . Observe the results returned from the indicators.
15. Click the Temperature tab. Change the Coil Temperature [K] and the Magnet Temperature [K] .
16. Click Stop to stop the control.

##### Related Information

[Using the Project Explorer Window](/csh?topicname=lvconcepts/using_labview_projects.html)

[FPGA Target Properties Dialog Box](/csh?topicname=lvfpgadialog/fpga_target_properties.html)

| Part 2: Testing the Control Algorithms | Part 4: Composing a Real HIL System |
| --- | --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_pmsm_4.html language=enus -->
## TOPIC 00013: Part 4: Composing a Real HIL System (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_pmsm_4.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_pmsm_4.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 4: Composing a Real HIL System (Electric Motor Simulation Toolkit)

After verifying that the controller monitors the simulated motor, you can place the controller and simulator on separate hardware and compose a real hardware-in-the-loop (HIL) system. In the HIL system, you connect the controller and simulator with I/O modules.

With the Electric Motor Simulation Toolkit, you can run the LabVIEW sample project wizard to create an Electric Motor Simulation sample project, in which I/O modules are configured properly.

#### Creating a Sample Project

Complete the following steps to create a sample project for simulating a permanent magnet synchronous motor (PMSM) with the finite element analysis (FEA) model.

1. Select File»Create Project to launch the Create Project dialog box.
2. On the Choose a starting point for the project page, select Motor Simulation from the Sample Projects category list.
3. Select Electric Motor Simulation from the project list. Click Next .
4. On the Configure your new project page, specify the project name and path. For this tutorial, enter PMSM_FEA as the Project Name . Save the project to the C:\Users\Administrator\Documents\LabVIEW Data\PMSM_FEA directory.
5. In the Motor Settings section, select Permanent Magnet Synchronous Motor as the Type and FEA Model as the Model .
6. In the Hardware Settings section, select Simulate motor on FPGA .
7. Click Finish to create the sample project, as shown in the following figure. [IMAGE alt='image' src='loc_env_fea_sp.gif']

Find the sample project documentation in the **Project Documentation** folder of the project. Refer to the document for details about connecting the hardware by I/O modules, adapting the sample project to hardware, and running the simulation. You also can replace the control algorithm with your own code, run the solution, and verify the control algorithm.

##### Related Information

[Create Project Dialog Box](/csh?topicname=lvdialog/create_project_db.html)

[Supported Motor Types](../lvemsimshared/motor_type.html)

[FEA Model](../lvemsimshared/fea_model.html)

| Part 3: Simulating a PMSM on an FPGA Target |
| --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_srm.html language=enus -->
## TOPIC 00014: Simulating an SRM with the Linear Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_srm.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_srm.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulating an SRM with the Linear Model (Electric Motor Simulation Toolkit)

In this tutorial, you design an application to simulate a switched reluctance motor (SRM) and compose a hardware-in-the-loop (HIL) system with I/O modules. Suppose that you want to simulate a three-phase SRM using the linear model function. You can use the built-in examples and sample project that this toolkit provides to simulate the motor in an HIL system. After completing this tutorial, you can replace the control algorithms with your new electric control unit (ECU) control algorithms according to your application requirements.

This tutorial consists of the following parts:

1. Testing the Control Algorithms
2. Simulating an SRM on an FPGA Target
3. Composing a Real HIL System

##### Related Information

[Linear Model](../lvemsimshared/line_model.html)

[Getting Started with Electric Motor Simulation](../lvemsim/emsim_overview.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_srm_1.html language=enus -->
## TOPIC 00015: Part 1: Testing the Control Algorithms (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_srm_1.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_srm_1.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 1: Testing the Control Algorithms (Electric Motor Simulation Toolkit)

Before simulating an electric motor, you must test your control algorithms on a host computer without connecting to any targets. Modify the control algorithms until the controller can monitor the simulator satisfactorily. Testing the control algorithms on host computers saves the workload of simulation on FPGA targets.

This toolkit provides built-in examples to help you get familiar with testing the control algorithms. In this example, your control algorithms are written in a closed-loop control system using LabVIEW VIs and functions. With the help of this example, you can learn how the control algorithms work with the simulator VI.

Complete the following steps to test the control algorithms in the closed-loop example.

1. Open the SRM Linear Model Closed Loop Control VI in the labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Closed Loop Control directory. 
 Open example 
 Find related examples
2. Run the SRM Linear Model Closed Loop Control VI.
3. Observe the results returned from the Rotor Velocity [RPM] indicator. You can see that the motor speed is gradually getting closer to the velocity setpoint.
4. Change the Velocity Setpoint [RPM] to 1000 .
5. Observe the changes of Rotor Velocity [RPM] . The velocity setpoint is 1000 and the motor speed is very close to 1000.
6. Change the Velocity Setpoint [RPM] to a negative value and observe the changes of the motor speed.
7. Change the Load Torque [Nm] . The motor adjusts the speed to keep approaching the velocity setpoint.
8. Click Stop to stop this example.

Open the block diagram of the SRM Linear Model Closed Loop Control VI to view how the control algorithms work with the simulator VI. You can modify the control algorithms in this example to meet your application requirements. You also can replace the control algorithm with your new electric control unit (ECU) control algorithms and test if the control algorithms work with the simulator.

| Part 2: Simulating an SRM on an FPGA Target |
| --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_srm_2.html language=enus -->
## TOPIC 00016: Part 2: Simulating an SRM on an FPGA Target (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_srm_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_srm_2.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 2: Simulating an SRM on an FPGA Target (Electric Motor Simulation Toolkit)

In this part, you can verify whether the algorithm can perform correctly with the hardware-in-the-loop (HIL) solution. Before getting your solution equipped with the real I/O modules, you need to test your algorithm with a simpler solution on an FPGA target.

Complete the following steps to simulate a switched reluctance motor (SRM) on an FPGA target.

1. Open SRM Linear Model Control Simulation.lvproj in the labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Control Simulation directory: 
 Open example 
 Find related examples
2. In the Project Explorer window, right-click the RT Target and select Properties from the shortcut menu to open the Real-Time PXI Properties dialog box.
3. In the IP Address/DNS Name field, enter the IP address for the real-time target.
4. In the Project Explorer window, right-click the FPGA Target and select Properties from the shortcut menu to open the FPGA Target Properties dialog box.
5. In the Resource field, specify the FPGA target hardware.
6. In the Project Explorer window, navigate to RT Target»FPGA Target»Build Specifications»SRM Linear Model Simulator . Right-click the build specification and select Build from the shortcut menu.
7. Compile the FPGA code.
8. Open and run the SRM Linear Model Control Simulation VI.
9. On the front panel of the SRM Linear Model Control Simulation VI, enter the name of the FPGA target in Resource Name and choose the SRM Type .
10. Click Start . The real-time controller supplies control signals to the simulated motor and the motor starts running at a fixed velocity.
11. Adjust the Velocity Setpoint [RPM] and Load Torque [Nm] . Verify if the output of motor speed is still approaching the value of the velocity setpoint.
12. Click Stop to stop the control.

##### Related Information

[Using the Project Explorer Window](/csh?topicname=lvconcepts/using_labview_projects.html)

[FPGA Target Properties Dialog Box](/csh?topicname=lvfpgadialog/fpga_target_properties.html)

| Part 1: Testing the Control Algorithms | Part 3: Composing a Real HIL System |
| --- | --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/emsim_tutorial_srm_3.html language=enus -->
## TOPIC 00017: Part 3: Composing a Real HIL System (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/emsim_tutorial_srm_3.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/emsim_tutorial_srm_3.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Part 3: Composing a Real HIL System (Electric Motor Simulation Toolkit)

After verifying that the controller monitors the simulated motor, you can place the controller and simulator on separate hardware and compose a real hardware-in-the-loop (HIL) system. In the HIL system, you connect the controller and simulator with I/O modules.

With the Electric Motor Simulation Toolkit, you can run the LabVIEW sample project wizard to create an Electric Motor Simulation sample project, in which I/O modules are configured properly.

#### Creating an SRM Linear Model Sample Project

Complete the following steps to create a sample project for the switched reluctance motor (SRM) linear model.

1. Select File»Create Project to launch the Create Project dialog box.
2. On the Choose a starting point for the project page, select Motor Simulation from the Sample Projects category list.
3. Select Electric Motor Simulation from the project list. Click Next .
4. On the Configure your new project page, specify the project name and path. For this tutorial, enter SRM_Linear as the Project Name . Save the project to the C:\Users\Administrator\Documents\LabVIEW Data\SRM_Linear directory.
5. In the Motor Settings section, select Switched Reluctance Motor as the Type . Select Linear Model as the Model . Select 3-Phase as the Phase .
6. In the Hardware Settings section, select Simulate motor on FPGA .
7. Click Finish to create the sample project, as shown in the following figure. [IMAGE alt='image' src='loc_env_srm_line.gif']

Find the sample project documentation in the **Project Documentation** folder of the project. Refer to the document for details about connecting the hardware by I/O modules, adapting the sample project to hardware, and running the simulation.

##### Related Information

[Create Project Dialog Box](/csh?topicname=lvdialog/create_project_db.html)

[Linear Model](../lvemsimshared/line_model.html)

[Supported Motor Types](../lvemsimshared/motor_type.html)

| Part 2: Simulating an SRM on an FPGA Target |
| --- |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsim/lvemsim.html language=enus -->
## TOPIC 00018: NI Electric Motor Simulation Toolkit

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsim/lvemsim.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsim/lvemsim.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### NI Electric Motor Simulation Toolkit

October 2015, 373998C-01

The NI Electric Motor Simulation Toolkit is an add-on for both the LabVIEW platform and NI VeriStand. On the LabVIEW platform, this toolkit allows you to control and simulate an electric motor. This toolkit uses field-programmable gate array (FPGA) technology and integrates the [finite element analysis (FEA)](../lvemsimshared/fea_model.html) method to provide high-speed and high-fidelity electric motor simulation.

This toolkit also combines NI real-time testing software technology with third-party software. You can use this toolkit with JSOL JMAG-RT, part of the FEA tool suite from JSOL Corporation. You also can use this toolkit with ANSYS simulation software.

The Electric Motor Simulation Toolkit provides the following components:

- Electric Motor Simulation VIs —The Electric Motor Simulation VIs provide functionality that you use to simulate an electric motor. To access the Electric Motor Simulation VIs, select View»Functions Palette from the block diagram in LabVIEW and navigate to the Control Design and Simulation»Electric Motor Simulation palette.
- Sample projects —The sample projects demonstrate useful design patterns and serve as starting points for your applications. You can customize the sample projects according to the needs of your application. Select File»Create Project to display the Create Project dialog box, which lists the Electric Motor Simulation sample projects in the Motor Simulation category.
- Examples —Example VIs demonstrate common applications that you can create by using the Electric Motor Simulation Toolkit. You can modify an example VI to fit an application, or you can copy and paste from one or more example VIs into a VI that you create. Refer to the labview\examples\Electric Motor Simulation directory for example VIs installed with this toolkit. You also can access these examples by selecting Help»Find Examples and then selecting Toolkits and Modules»Electric Motor Simulation in the NI Example Finder.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

JSOL JMAG is a registered trademark of JSOL Corporation. ANSYS is a registered trademark of ANSYS Incorporated.

© 2013–2015 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/ansys_file.html language=enus -->
## TOPIC 00019: ANSYS Motor Model File (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/ansys_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/ansys_file.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### ANSYS Motor Model File (Electric Motor Simulation Toolkit)

ANSYS is a company that provides engineering simulation solutions. The ANSYS motor model file is the motor model file that the ANSYS simulation software generates. The ANSYS motor model file is in the TXT file format. The TXT file contains basic motor characteristics, such as the three-phase resistances and the number of poles. The TXT file also contains detailed motor parameters information, which are the analysis results of the ANSYS simulation software.

You can use the Electric Motor Simulation Toolkit to read an ANSYS motor model file if you use the variable parameter model for permanent magnet synchronous motors (PMSM). Refer to the ANSYS Incorporated website at www.ansys.com for more information about the ANSYS simulation software and the ANSYS motor model files.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[PMSM](../lvemsimshared/motor_type.html#pmsm)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/base_value.html language=enus -->
## TOPIC 00020: Base Value (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/base_value.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/base_value.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Base Value (Electric Motor Simulation Toolkit)

Apart from the engineering units, electrical engineers also use per-unit to measure quantities in physics. A per-unit system expresses system quantities as fractions of a defined base unit quantity. The per-unit system scales the actual value of a physical quantity, such as current, voltage, and speed, with a selected constant of the same measuring unit. The ratio of the actual value to the constant is the per-unit value of the physical quantity. The selected constant, also known as base value, has the same measuring unit as the actual value.

The following equation explains the relationship between a per-unit value and a base value.

[IMAGE alt='image' src='eq_per_unit.gif']

For example, suppose you have two voltages, *U<sub>1</sub>*=99 KV and *U<sub>2</sub>*=110 KV. When selecting 110 KV as the base value of voltages, you can express the per-unit value of *U<sub>1</sub>* and *U<sub>2</sub>* as follows.

[IMAGE alt='image' src='eq_per_unit_example1.gif']

[IMAGE alt='image' src='eq_per_unit_example2.gif']

The results show that the real value of *U<sub>1</sub>* is 0.9 times of the base value, while the real value of *U<sub>2</sub>* is the same as the base value. In other words, the per-unit value of *U<sub>1</sub>* is 0.9 and the per-unit value of *U<sub>2</sub>* is 1.

The per-unit system is ideal for fixed-point implementation. Per-unit helps to make the fixed-point model usable for various motors. All quantities are multiples of the base value that you select.

#### Troubleshooting Improper Base Value Error

When you use the Electric Motor Simulation VIs to generate FPGA data for electric motor simulation, an error occurs if improper **base values** lead to overflow. Complete the following steps to resolve the error.

1. Keep the value of speed base as default.
2. Gradually increase the value of current base . Keep the per-unit value of the maximum current within the range from 0.1 to 10. For example, suppose the maximum current of an electric motor is 300 A, you can select a value in the range from 30 A to 3000 A as the current base.
3. Gradually increase the value of voltage base . Keep the per-unit value of the maximum voltage within the range from 0.1 to 10.
4. Repeat steps 2 and 3 until the error stops occurring.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/cons_para_model.html language=enus -->
## TOPIC 00021: Constant Parameter Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/cons_para_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/cons_para_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Constant Parameter Model (Electric Motor Simulation Toolkit)

Use the constant parameter model function to simulate an AC induction motor (ACIM) or a permanent magnet synchronous motor (PMSM).

#### Constant Parameter Model for ACIM Simulation

The constant parameter model simulates the electromagnetic behavior of an ACIM by using the (α,β) orthogonal coordinate system.

In an (α,β) orthogonal coordinate system, the α axis usually coincides with the direction of the A current of the three-phase current in the stator. The β axis is the axis at an angle of 90 degrees from the α axis.

The following figure illustrates the relationship between the (α,β) orthogonal coordinate system and the three-phase current.

[IMAGE alt='image' src='noloc_eps_alpha_beta.gif']

Because of the three-phase current in the stator windings, the magnetizing currents of the stator produce a magnetic field. The magnetic field generates a current in the rotor. The voltage equations for ACIM simulation with the constant parameter model are as follows.

[IMAGE alt='image' src='eq_acim_vs1.gif']

[IMAGE alt='image' src='eq_acim_vs2.gif']

[IMAGE alt='image' src='eq_acim_vr1.gif']

[IMAGE alt='image' src='eq_acim_vr2.gif']

| where | Vsα is the stator voltage along the α axis |
| --- | --- |
|  | Vsβ is the stator voltage along the β axis |
|  | Rs is the stator resistance |
|  | Isα is the stator current along the α axis |
|  | Isβ is the stator current along the β axis |
|  | λsα is the stator flux linkage along the α axis |
|  | λsβ is the stator flux linkage along the β axis |
|  | Vrα is the rotor voltage along the α axis |
|  | Vrβ is the rotor voltage along the β axis |
|  | Rr is the rotor resistance |
|  | Irα is the rotor current along the α axis |
|  | Irβ is the rotor current along the β axis |
|  | λrα is the rotor flux linkage along the α axis |
|  | λrβ is the rotor flux linkage along the β axis |
|  | ωr is the electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |

The flux linkage equations are as follows.

[IMAGE alt='image' src='eq_acim_fluxs1.gif']

[IMAGE alt='image' src='eq_acim_fluxs2.gif']

[IMAGE alt='image' src='eq_acim_fluxr1.gif']

[IMAGE alt='image' src='eq_acim_fluxr2.gif']

| where | Lls is the stator leakage inductance |
| --- | --- |
|  | Llr is the rotor leakage inductance |
|  | Lm is the magnetizing inductance |

The voltage equations calculate the derivatives of stator flux linkage and rotor flux linkage.

[IMAGE alt='image' src='eq_acim_flux_de1.gif']

[IMAGE alt='image' src='eq_acim_flux_de2.gif']

[IMAGE alt='image' src='eq_acim_flux_de3.gif']

[IMAGE alt='image' src='eq_acim_flux_de4.gif']

where *k* and *k-1* are the simulation steps. For example, *λ<sub>sα</sub>*(*k*) is the stator flux linkage along the α axis at the *k* step, while *λ<sub>sα</sub>*(*k-1*) is the stator flux linkage along the α axis at the *k-1* step.

The flux linkage equations calculate the current by defining *λ<sub>mα</sub>*, *λ<sub>mβ</sub>*, and *L<sub>M</sub>*.

[IMAGE alt='image' src='eq_acim_cur_de1.gif']

[IMAGE alt='image' src='eq_acim_cur_de2.gif']

[IMAGE alt='image' src='eq_acim_cur_de3.gif']

The following equations can be derived to obtain the current in the (α,β) orthogonal coordinate system.

[IMAGE alt='image' src='eq_acim_cur1.gif']

[IMAGE alt='image' src='eq_acim_cur2.gif']

[IMAGE alt='image' src='eq_acim_cur3.gif']

[IMAGE alt='image' src='eq_acim_cur4.gif']

The constant parameter model calculates the electric torque of an ACIM by using the following equation.

[IMAGE alt='image' src='eq_acim_torque.gif']

where *p* is the number of poles.

#### Constant Parameter Model for PMSM Simulation

The constant parameter model simulates the electromagnetic behavior of a PMSM by using the d-q axes mathematical method.

The d-q axes are the axes in a (d,q) coordinate system. The d axis, or the direct axis, usually coincides with the axis of the rotor magnet pole. The q axis, or the quad axis, is the axis at an angle of 90 degrees from the d axis. When the rotor is stationary, the (d,q) coordinate system is a stationary reference frame. When the rotor starts rotating, the system is a rotor reference frame where the (d,q) coordinate system rotates at the rotor speed.

The following figure illustrates a (d,q) coordinate system.

[IMAGE alt='image' src='loc_eps_dqaxes.gif']

While the rotor is rotating, electromagnetic current is generated inside the electric motor. The voltage equations of the (d,q) rotor reference frame are as follows.

[IMAGE alt='image' src='eq_pmsm_vd.gif']

[IMAGE alt='image' src='eq_pmsm_vq.gif']

The flux linkage equations are as follows.

*λ<sub>d</sub>=L<sub>d</sub>I<sub>d</sub>+λ<sub>f</sub>*

*λ<sub>q</sub>=L<sub>q</sub>I<sub>q</sub>*

| where | ωr is electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |
| --- | --- |
|  | Id is the current along the d axis |
|  | Iq is the current along the q axis |
|  | λd is the flux linkage along the d axis |
|  | λq is the flux linkage along the q axis |
|  | λf is the flux linkage in the rotor magnet |
|  | Ld is the inductance along the d axis |
|  | Lq is the inductance along the q axis |

The following equation calculates the electric torque of the (d,q) rotor reference frame.

[IMAGE alt='image' src='eq_pmsm_torque.gif']

where *p* is the number of poles.

The following discrete equations calculate the current for PMSM simulation with the constant parameter model.

[IMAGE alt='image' src='eq_pmsm_cons_dis1.gif']

[IMAGE alt='image' src='eq_pmsm_cons_dis2.gif']

where *k* and *k-1* are the simulation steps. For example, *I<sub>d</sub>*(*k*) is the current along the d axis at the *k* step, while *I<sub>d</sub>*(*k-1*) is the current along the d axis at the *k-1* step.

##### Related Information

[Supported Motor Types](../lvemsimshared/motor_type.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/fea_model.html language=enus -->
## TOPIC 00022: FEA Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/fea_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/fea_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FEA Model (Electric Motor Simulation Toolkit)

The finite element analysis (FEA) model function implements high-fidelity model simulation of an electric motor. The FEA model takes real motor characteristics into account and uses the FEA method to describe the motor behaviors.

In mathematics, the FEA method is a numerical technique to find approximate solutions to boundary value problems. This method connects many simple element equations over many small subdomains, named finite elements, to approximate a more complex equation over a larger domain. In mechanics and computer science, the FEA method is also a method of mechanical computer simulation and a computational tool to perform engineering analysis. The FEA model uses software programs based on finite element method algorithms to divide a complex problem into smaller elements.

The FEA model function obtains real motor characteristics from the RTT files. Among the characteristics, motor parameters are analyzed using the FEA method. As part of the simulation process, the FEA model function looks up the motor parameters and characteristics in these files.

The FEA model uses the following voltage equation to calculate the current for a PMSM.

[IMAGE alt='image' src='eq_fea_pmsm.gif']

| where | Va, Vb, and Vc are the three-phase voltages |
| --- | --- |
|  | R is the phase resistance |
|  | Ia, Ib, and Ic are the three-phase currents |
|  | L'aa, L'bb, and L'cc are the differential self-inductances |
|  | L'ab, L'ac, L'ba, L'bc, L'ca, and L'cb are the differential mutual inductances |
|  | λa, λb, and λc are the magnetic fluxes generated by the permanent magnet |

The FEA model uses the following voltage equation to calculate the current for a three-phase SRM.

[IMAGE alt='image' src='eq_fea_srm.gif']

| where | Laa, Lbb, and Lcc are the self-inductances |
| --- | --- |
|  | Lab, Lac, Lba, Lbc, Lca, and Lcb are the mutual inductances |

##### Related Information

[RTT File](../lvemsimshared/rtt_file.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/inverter.html language=enus -->
## TOPIC 00023: Three-Phase Inverter (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/inverter.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/inverter.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Three-Phase Inverter (Electric Motor Simulation Toolkit)

An inverter is an electrical device that converts direct current (DC) to alternating current (AC). A three-phase inverter is a commonly-used inverter for powering a variable-speed motor like the permanent magnet synchronous motor (PMSM). The three-phase inverter consists of three single-phase branches which connect to three load terminals. Each single-phase branch contains two power switches. The following figure illustrates the circuit diagram of a three-phase inverter. In this circuit, the three resistances represent the load. In real applications, the load can be an electric motor.

[IMAGE alt='image' src='noloc_eps_inverter_model.gif']

The following symbols apply to the circuit diagram:

- S<sub>au</sub> is the phase A upper switch.
- S<sub>al</sub> is the phase A lower switch.
- S<sub>bu</sub> is the phase B upper switch.
- S<sub>bl</sub> is the phase B lower switch.
- S<sub>cu</sub> is the phase C upper switch.
- S<sub>cl</sub> is the phase C lower switch.
- V<sub>ab</sub> , V<sub>bc</sub> , and V<sub>ca</sub> are the line-to-line voltages.
- V<sub>a</sub> , V<sub>b</sub> , and V<sub>c</sub> are the phase voltages.

The Electric Motor Simulation Toolkit allows you to simulate an ideal three-phase inverter or an advanced three-phase inverter. In the ideal three-phase inverter model, the switches are simple on-off switches. When the switch is on, no voltage drop happens on the switch. When the switch is off, no current flows through the switch. In the advanced three-phase inverter model, the switches are insulated gate bipolar transistors (IGBT) with diodes. The advanced three-phase inverter model simulates the transient behavior of the inverter. By using the advanced three-phase inverter model, you can specify the forward voltage drops of the switches and insert fault to the inverter at run time.

#### Ideal Three-Phase Inverter Model

The ideal three-phase inverter model assumes that the switch state changes between on and off instantaneously. The two switches in the same single-phase branch are complementary. The following table lists the phase voltages and line-to-line voltages of the ideal three-phase inverter model. *V<sub>DC</sub>* is the DC voltage that connects to the inverter. In the **Switch State** column, *1* indicates that the switch is on, while *0* indicates that the switch is off.

| Switch State | Phase Voltage (V) | Line-to-Line Voltage (V) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sau | Sbu | Scu | Va | Vb | Vc | Vab | Vbc | Vca |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 2VDC/3 | -VDC/3 | -VDC/3 | VDC | 0 | -VDC |
| 1 | 1 | 0 | VDC/3 | VDC/3 | -2VDC/3 | 0 | VDC | -VDC |
| 0 | 1 | 0 | -VDC/3 | 2VDC/3 | -VDC/3 | -VDC | VDC | 0 |
| 0 | 1 | 1 | -2VDC/3 | VDC/3 | VDC/3 | -VDC | 0 | VDC |
| 0 | 0 | 1 | -VDC/3 | -VDC/3 | 2VDC/3 | 0 | -VDC | VDC |
| 1 | 0 | 1 | VDC/3 | -2VDC/3 | VDC/3 | VDC | -VDC | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

The Electric Motor Simulation Toolkit only calculates the phase voltages. The following equations demonstrate the relationship between the line-to-line voltages and the phase voltages.

[IMAGE alt='image' src='eq_l2l_ab.gif']

[IMAGE alt='image' src='eq_l2l_bc.gif']

[IMAGE alt='image' src='eq_l2l_ca.gif']

#### Advanced Three-Phase Inverter Model

The advanced three-phase inverter model regards the IGBT-with-diode switch as a small inductance (*L*) when the switch is on. When the switch is off, the model regards the switch as a small capacitance (*C*). A conductance (*G*) in parallel with a dependent current source (*J*) represents a switch. The following figure illustrates how the advanced three-phase inverter model simulates the switch.

[IMAGE alt='image' src='loc_eps_inverter_switch.gif']

The advanced three-phase inverter model regards the conductance as a constant to simplify the calculation process. The following equations show the relationship between the conductance and the simulation time interval (*dt*).

[IMAGE alt='image' src='eq_inverter_conduc1.gif']

[IMAGE alt='image' src='eq_inverter_conduc2.gif']

[IMAGE alt='image' src='eq_inverter_conduc3.gif']

The following equation determines the current source. The subscript *k* and *k-1* denote the simulation steps.

[IMAGE alt='image' src='eq_inverter_current.gif']

| where | Ik-1 is the current on the switch at the k-1 step |
| --- | --- |
|  | Vk-1 is the voltage on the switch at the k-1 step |
|  | sk=1 denotes that the switch is on at the k step |
|  | sk=0 denotes that the switch is off at the k step |

The following equation determines the state of the IGBT-with-diode switch.

[IMAGE alt='image' src='eq_inverter_switch.gif']

where [IMAGE alt='image' src='eq_inverter_s.gif'] denotes the complement of *s*. *g* is the gate signal for the switch. *g*=1 denotes that the gate signal commands the switch to be on, while *g*=0 denotes that the gate signal commands the switch to be off.

##### Inserting Fault to the Inverter

The advanced three-phase inverter model allows you to simulate the behavior of an inverter when the switch has faults. The model provides four types of faults and only supports one fault at a time. The four fault types are as follows.

- IGBT open fault —This fault occurs if any IGBT is interrupted. No current flows through the IGBT with fault. It is equivalent to replacing the switch with a diode.
- Diode open fault —This fault occurs if any diode is interrupted. No current flows through the diode with fault. It is equivalent to replacing the switch with an IGBT.
- IGBT and diode open fault —This fault occurs if any IGBT-with-diode switch is interrupted. No current flows through the IGBT-with-diode switch with fault. It is equivalent to removing the switch from the circuit.
- IGBT or diode short fault —This fault occurs if any IGBT or diode is bypassed. It is equivalent to replacing the switch with a wire. In this case, the protection circuit turns off the other switch in the same single-phase branch as the switch with fault. As a result, short circuit does not happen to the voltage source.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/line_model.html language=enus -->
## TOPIC 00024: Linear Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/line_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/line_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Linear Model (Electric Motor Simulation Toolkit)

The [switched reluctance motor (SRM)](../lvemsimshared/motor_type.html) shows strong nonlinearity because the flux of a stator winding depends on both the phase current and the rotor position. Therefore, the linear model utilizes the piece-wise linear method to describe the flux of an SRM.

In an SRM, the non-linear characteristics of the magnet affect the operation of the SRM. High levels of saturation occur cyclically as the rotor continuously moves from an unaligned position to an aligned position, with reference to the poles on the stator. The following figure depicts different rotor positions.

[IMAGE alt='image' src='loc_fp_linearaligned.gif']

The positions are specific to one of the phases. The aligned position means that the pole of the rotor and the pole of the stator are in the same line. The unaligned position means that the rotor of the specific phase is completely detached from the stator. The middle position is when the pole of the rotor has intersection with the pole of the stator. The flux linkage of the motor phase varies at different positions.

The SRM linear model function complies with the following equations.

Phase voltage equation:

[IMAGE alt='image' src='eq_srm_vol.gif']

Instant torque equation:

[IMAGE alt='image' src='eq_srm_torque.gif']

| where | λ is the flux linkage |
| --- | --- |
|  | θ is the rotor position |
|  | R is the resistance |
|  | I is the current |
|  | V is the voltage |
|  | T is the torque |

The following figure shows an analytical expression for the flux linkage of a linear model. The aligned and unaligned curves represent the flux changes at the aligned position and unaligned position. The two curves in the middle represent the flux changes at the middle positions.

[IMAGE alt='image' src='loc_eps_flux.gif']

In the following figure, the curves with dots show the flux linkage of a real motor at different rotor position. The curves without dots represent the linear model approximation.

[IMAGE alt='image' src='noloc_fp_linear.gif']

The slope of the straight line in the figure approximates the flux curve for the unaligned position, as shown in the following equation.

[IMAGE alt='image' src='eq_srm_flux1.gif']

where *L<sub>u</sub>* is a constant that represents the equivalent inductance of the coil for the unaligned position. The *u* subscript means unaligned.

For aligned positions, when *I* is no greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_flux2_1.gif']

where *λ<sub>a</sub>* is the flux of *I<sub>s</sub>* at the aligned position. The *a* subscript means aligned and the *s* subscript means saturated.

When *I* is greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_flux2_2.gif']

The dependency of *λ* on the rotor position *θ* is approximated by a sine wave oscillating between the maximum value *λ<sub>a</sub>(I)* and the minimum value *λ<sub>u</sub>(I)*, as illustrated in the following equation.

[IMAGE alt='image' src='eq_srm_flux3.gif']

where *p* is the number of poles in pairs.

From the previous equations, a linear model function solves the current and torque in the SRM.

When *I* is no greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_current1.gif']

where the *k* subscript indicates the variable calculated at the *k* step, while the *k-1* subscript indicates the variable calculated at the *k-1* step. For example, *I<sub>k</sub>* is the phase current at the *k* step, while *I<sub>k-1</sub>* is the phase current at the *k-1* step.

[IMAGE alt='image' src='eq_srm_torque1.gif']

When *I* is greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_current2.gif']

[IMAGE alt='image' src='eq_srm_torque2.gif']

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/lvemsimshared.html language=enus -->
## TOPIC 00025: Electric Motor Simulation Concepts (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/lvemsimshared.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/lvemsimshared.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Electric Motor Simulation Concepts (Electric Motor Simulation Toolkit)

October 2015, 374207C-01

Electric motor simulation is the process of imitating the control and operation of a real-world electric motor over time. The simulated electric motor is typically a part of the hardware-in-the-loop (HIL) simulation, which is widely used in the development and test of complex real-time embedded systems. Simulating an electric motor that runs in the HIL system allows you to design and debug the application without depending on the physical electric motor. When you simulate an electric motor, you can validate the mechanical parameters of the motor, test algorithms for controlling the motor behaviors, and verify if the simulated motor works with the controller and I/O modules in the HIL system before you deploy and run the application on real hardware. The technique of electric motor simulation is becoming increasingly popular in industrial development because of its efficiency, safety, duration, and advantage of saving the cost of all tools and effort.

With the Electric Motor Simulation Toolkit, you use the palette VIs, examples, and sample projects to design an HIL system and model the motion of real electric motors in a real-world system. You configure the motor parameters and test the control algorithms with efficiency in a simulated system. When you can ensure that the control algorithms work satisfactorily, replace the simulated motor with a real electric motor. You can further replace the control algorithms with a real controller, such as an electronic control unit (ECU).

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2013–2015 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/motor_type.html language=enus -->
## TOPIC 00026: Supported Motor Types (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/motor_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/motor_type.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported Motor Types (Electric Motor Simulation Toolkit)

The Electric Motor Simulation Toolkit allows you to simulate the following types of electric motors.

- AC induction motors (ACIM)
- Permanent magnet synchronous motors (PMSM)
- Switched reluctance motors (SRM)

#### ACIM

An ACIM is a type of electric motor that has a stationary stator outside and a rotor which spins inside. By supplying alternating current to the stator, the ACIM uses the electromagnet of the stator to generate current in the rotor and produce torque. The stator is a hollow metal cylinder with slots for coils of wires. The rotor consists of metal bars which have end rings at both ends to form short circuits. The following figure illustrates a typical ACIM.

[IMAGE alt='image' src='noloc_eps_acim.gif']

#### PMSM

A PMSM is a type of electric motor that utilizes permanent magnets in the rotor. The poles of a PMSM indicates how many even numbers of magnet poles that the rotor has. The following figure is an example of a typical PMSM. This motor has four permanent magnets on the rotor, as shown in the figure.

[IMAGE alt='image' src='noloc_eps_pmsm.gif']

#### SRM

An SRM is a type of electric motor that produces torque from a slight misalignment of poles on the rotor with poles on the stator. The rotor tends to align itself with the stator to maximize the inductance of the stator, while the stator is consequently energized to force the rotor to rotate. The phase of the SRM indicates the number of pole pairs in the stator. For example, the following figure illustrates a three-phase SRM. The stator of this motor has three pairs of poles.

[IMAGE alt='image' src='noloc_eps_srm.gif']

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/rtt_file.html language=enus -->
## TOPIC 00027: RTT File (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/rtt_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/rtt_file.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### RTT File (Electric Motor Simulation Toolkit)

An RTT file, or the JMAG-RT motor model, is a third-party product provided by the JSOL company. The file, with an extension of .rtt, contains basic motor characteristics, such as the motor type, connection type, and number of poles. The RTT file also contains detailed motor parameters information, which are the analysis results of the JMAG-RT software.

You can use the Electric Motor Simulation Toolkit to read an RTT file for the FEA model or the variable parameter model. You can either download RTT files from the JSOL website at www.jmag-international.com or create an RTT file by using the JMAG-RT software.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[FEA Model](../lvemsimshared/fea_model.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/temp_correction.html language=enus -->
## TOPIC 00028: Temperature Correction (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/temp_correction.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/temp_correction.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Temperature Correction (Electric Motor Simulation Toolkit)

Temperature correction is a functionality that simulates the changes of resistance, magnet flux, or torque in an electric motor according to temperature variations. In a permanent magnet synchronous motor (PMSM), when the magnet temperature and the coil temperature change, the resistance and the magnet flux change accordingly. Magnet temperature variations also affect the electromagnetic torque. In an AC induction motor (ACIM), when the rotor temperature and the stator temperature change, the rotor resistance and the stator resistance change accordingly. The Electric Motor Simulation Toolkit provides the temperature correction functionality for ACIM simulation with the constant parameter model and PMSM simulation with the FEA and the variable parameter models.

To perform the temperature correction functionality, you must obtain motor parameters for temperature correction. By using the Electric Motor Simulation VIs, you can either manually specify the temperature correction parameters, or obtain the temperature correction parameters from an RTT file.

The following equation calculates the PMSM coil resistance, the ACIM stator resistance, and the ACIM rotor resistance after temperature correction:

[IMAGE alt='image' src='eq_temp_correction1.gif']

| where | R' is the resistance after temperature correction |
| --- | --- |
|  | R is the resistance under the base temperature before temperature correction |
|  | k is the temperature correction coefficient |
|  | T is the real-time temperature |
|  | Tbase is the base temperature |

The following equation calculates the PMSM magnet flux after temperature correction:

[IMAGE alt='image' src='eq_temp_correction2.gif']

| where | F' is the magnet flux after temperature correction |
| --- | --- |
|  | F is the magnet flux under the magnet base temperature before temperature correction |
|  | km is the magnet temperature correction coefficient |
|  | Tm is the real-time magnet temperature |
|  | Tm-base is the magnet base temperature |

##### Related Information

[Constant Parameter Model](../lvemsimshared/cons_para_model.html)

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[FEA Model](../lvemsimshared/fea_model.html)

[RTT File](../lvemsimshared/rtt_file.html)

[Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/vari_para_model.html language=enus -->
## TOPIC 00029: Variable Parameter Model (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/vari_para_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/vari_para_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Variable Parameter Model (Electric Motor Simulation Toolkit)

Use the variable parameter model function to implement medium-fidelity model simulation of a permanent magnet synchronous motor (PMSM). Like the constant parameter model, the variable parameter model uses the voltage equations, flux linkage equations, and torque equation of the (d,q) rotor reference frame. Unlike the constant parameter model, the motor inductance in the variable parameter model is a variable due to magnet saturation. The variable parameter model can obtain real motor characteristics from an RTT file, an ANSYS motor model file, or an external model.

The variable parameter model uses the following discrete equations to calculate the current for a PMSM.

[IMAGE alt='image' src='eq_pmsm_vari_dis1.gif']

[IMAGE alt='image' src='eq_pmsm_vari_dis2.gif']

| where | ωr is electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |
| --- | --- |
|  | R is the resistance |
|  | Vd is the voltage along the d axis |
|  | Vq is the voltage along the q axis |
|  | λd is the flux linkage along the d axis |
|  | λq is the flux linkage along the q axis |
|  | λf is the flux linkage in the rotor magnet |
|  | Ld is the inductance along the d axis |
|  | Lq is the inductance along the q axis |
|  | k, k-1, and k-2 are the simulation steps |

For example, *I<sub>d</sub>*(*k*) is the current along the d axis at the *k* step. *I<sub>d</sub>*(*k-1*) is the current along the d axis at the *k-1* step. *L<sub>q</sub>*(*k-2*) is the inductance along the q axis at the *k-2* step.

#### External Model

An external model is a model function you create by using the Electric Motor Simulation Toolkit. You can import the external model to get motor characteristics for simulating a PMSM with the variable parameter model. Motor characteristics include number of poles, resistance, temperature correction parameters, direct inductance table, quad inductance table, flux table, and so on.

##### Related Information

[Supported Motor Types](../lvemsimshared/motor_type.html)

[Constant Parameter Model for PMSM Simulation](../lvemsimshared/cons_para_model.html#cons_pmsm)

[RTT File](../lvemsimshared/rtt_file.html)

[ANSYS Motor Model File](../lvemsimshared/ansys_file.html)

[Temperature Correction](../lvemsimshared/temp_correction.html)

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/3-phase_inverter_model.html language=enus -->
## TOPIC 00030: 3-Phase Inverter Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/3-phase_inverter_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/3-phase_inverter_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### 3-Phase Inverter Model VI

**Owning Palette:** [Inverter VIs](../lvemsimvi/emsim_inverter.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates a [three-phase inverter](../lvemsimshared/inverter.html). You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

#### 3-Phase Inverter Model (Ideal)

Simulates an ideal three-phase inverter.

[IMAGE alt='image' src='3-phase_inverter_model_ideal.gif']

|  | current specifies the three-phase current, in amperes, of the motor in the last simulation cycle. The current represents the three-phase current in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the current. |
| --- | --- |
|  | gate signal specifies the control signal from the controller and PWM modulation. The gate signal represents control command for the six switches within the inverter. Therefore, this array must have six elements. |
|  | DC voltage specifies the DC voltage, in volts, on the inverter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | voltage returns the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3-Phase Inverter Model (Advanced)

Simulates an advanced three-phase inverter.

[IMAGE alt='image' src='3-phase_inverter_model_advanced.gif']

|  | current specifies the three-phase current, in amperes, of the motor in the last simulation cycle. The current represents the three-phase current in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the current. |
| --- | --- |
|  | gate signal specifies the control signal from the controller and PWM modulation. The gate signal represents control command for the six switches within the inverter. Therefore, this array must have six elements. |
|  | DC voltage specifies the DC voltage, in volts, on the inverter. |
|  | inverter parameters specifies the characteristics of the inverter. IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
|  | IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | inverter fault specifies the fault of the inverter. fault type specifies the type of the fault. 0No Fault (default)—No fault occurs.1IGBT Open Fault—Any IGBT is interrupted.2Diode Open Fault—Any diode is interrupted.3IGBT and Diode Open Fault—Any IGBT with diode is interrupted.4IGBT or Diode Short Fault—Any IGBT or diode is bypassed. fault switch index specifies the index of the switch which is in fault state. 0Phase A Upper Switch (default)1Phase A Lower Switch2Phase B Upper Switch3Phase B Lower Switch4Phase C Upper Switch5Phase C Lower Switch |
|  | fault type specifies the type of the fault. 0No Fault (default)—No fault occurs.1IGBT Open Fault—Any IGBT is interrupted.2Diode Open Fault—Any diode is interrupted.3IGBT and Diode Open Fault—Any IGBT with diode is interrupted.4IGBT or Diode Short Fault—Any IGBT or diode is bypassed. |
| 0 | No Fault (default)—No fault occurs. |
| 1 | IGBT Open Fault—Any IGBT is interrupted. |
| 2 | Diode Open Fault—Any diode is interrupted. |
| 3 | IGBT and Diode Open Fault—Any IGBT with diode is interrupted. |
| 4 | IGBT or Diode Short Fault—Any IGBT or diode is bypassed. |
|  | fault switch index specifies the index of the switch which is in fault state. 0Phase A Upper Switch (default)1Phase A Lower Switch2Phase B Upper Switch3Phase B Lower Switch4Phase C Upper Switch5Phase C Lower Switch |
| 0 | Phase A Upper Switch (default) |
| 1 | Phase A Lower Switch |
| 2 | Phase B Upper Switch |
| 3 | Phase B Lower Switch |
| 4 | Phase C Upper Switch |
| 5 | Phase C Lower Switch |
|  | voltage returns the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/abc_dq_transform.html language=enus -->
## TOPIC 00031: ABC to DQ Transform VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/abc_dq_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/abc_dq_transform.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### ABC to DQ Transform VI

**Owning Palette:** [Transforms VIs](../lvemsimvi/emsim_transforms.html)

**Requires:** Electric Motor Simulation Toolkit

Transforms the three-phase current or voltage to direct and quad currents or voltages.

The three-phase current or voltage is the AC current or voltage of a three-phase circuit, while the d, q currents or voltages are the direct and quad current or voltage in the flux, torque (d, q) rotating reference frame.

[Details](#details)

[IMAGE alt='image' src='abc_to_dq_transform.gif']

|  | a specifies the a current or voltage, in amperes or volts, of the three-phase current or voltage. |
| --- | --- |
|  | b specifies the b current or voltage, in amperes or volts, of the three-phase current or voltage. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | d returns the direct current or voltage, in amperes or volts, from the Clarke and Park transform. |
|  | q returns the quad current or voltage, in amperes or volts, from the Clarke and Park transform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### ABC to DQ Transform Details

The equations for transforming current and voltage are similar. This section takes the current equations for an example.

This VI assumes that *I<sub>a</sub>+I<sub>b</sub>+I<sub>c</sub>*=0, where *I<sub>a</sub>* is the value of the a current, *I<sub>b</sub>* is the value of the b current, and *I<sub>c</sub>* is the value of the c current of the three-phase current.

The following equations convert three-phase current to direct and quad current:

[IMAGE alt='image' src='eq_dcurrent.gif']

[IMAGE alt='image' src='eq_qcurrent.gif']

| where | Id is the d or direct current |
| --- | --- |
|  | Iq is the q or quad current |
|  | θ is the mechanical rotor position in radians |

The values of I<sub>d</sub> and I<sub>q</sub> are also derived from the following equations:

[IMAGE alt='image' src='eq_dcurrent_1.gif']

[IMAGE alt='image' src='eq_qcurrent_1.gif']

where

[IMAGE alt='image' src='eq_abc_alpha.gif']

[IMAGE alt='image' src='eq_abc_beta.gif']

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/acim_cons_para_model.html language=enus -->
## TOPIC 00032: ACIM Constant Parameter Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/acim_cons_para_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/acim_cons_para_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### ACIM Constant Parameter Model VI

**Owning Palette:** [AC Induction Motor VIs](../lvemsimvi/emsim_acim.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates the AC Induction Motor (ACIM) by using the [constant parameter model](../lvemsimshared/cons_para_model.html) function.

[Example](#examples)

[IMAGE alt='image' src='acim_constant_parameter_model.gif']

|  | temperature specifies the stator temperature and the rotor temperature of the electric motor. If the value of stator temperature or rotor temperature is greater than 0, this VI performs the temperature correction functionality for the stator resistance and the rotor resistance. stator temperature specifies the temperature, in kelvins, of the motor stator. The default value is 0. rotor temperature specifies the temperature, in kelvins, of the motor rotor. The default value is 0. |
| --- | --- |
|  | stator temperature specifies the temperature, in kelvins, of the motor stator. The default value is 0. |
|  | rotor temperature specifies the temperature, in kelvins, of the motor rotor. The default value is 0. |
|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
|  | ACIM constant parameters specifies the parameters describing the characteristics of an ACIM. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. stator leakage inductance specifies the leakage inductance, in henries, of the stator windings. The value of stator leakage inductance must be greater than 0. rotor leakage inductance specifies the leakage inductance, in henries, of the rotor windings. The value of rotor leakage inductance must be greater than 0. magnetizing inductance specifies the magnetizing inductance, in henries, of the motor. The value of magnetizing inductance must be greater than 0. stator resistance specifies the resistance, in ohms, of the stator windings. The value of stator resistance must be greater than 0. rotor resistance specifies the resistance, in ohms, of the rotor windings. The value of rotor resistance must be greater than 0. base temperature specifies the base temperature, in kelvins, for the stator resistance and the rotor resistance. The value of base temperature must be equal to or greater than 0. stator temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the stator resistance. rotor temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the rotor resistance. |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | stator leakage inductance specifies the leakage inductance, in henries, of the stator windings. The value of stator leakage inductance must be greater than 0. |
|  | rotor leakage inductance specifies the leakage inductance, in henries, of the rotor windings. The value of rotor leakage inductance must be greater than 0. |
|  | magnetizing inductance specifies the magnetizing inductance, in henries, of the motor. The value of magnetizing inductance must be greater than 0. |
|  | stator resistance specifies the resistance, in ohms, of the stator windings. The value of stator resistance must be greater than 0. |
|  | rotor resistance specifies the resistance, in ohms, of the rotor windings. The value of rotor resistance must be greater than 0. |
|  | base temperature specifies the base temperature, in kelvins, for the stator resistance and the rotor resistance. The value of base temperature must be equal to or greater than 0. |
|  | stator temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the stator resistance. |
|  | rotor temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the rotor resistance. |
|  | voltage specifies the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | speed specifies the rotor speed, in revolutions per minute, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | abc current returns the three-phase current, in amperes, in the electric motor. This output is a three-element array, each element representing one phase of the three-phase current. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the ACIM Constant Parameter Model Closed Loop VI in the labview\examples\Electric Motor Simulation\ACIM\ACIM Constant Parameter Model Closed Loop directory for an example of using the ACIM Constant Parameter Model VI.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/clarke_transform.html language=enus -->
## TOPIC 00033: Clarke Transform VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/clarke_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/clarke_transform.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clarke Transform VI

**Owning Palette:** [Transforms VIs](../lvemsimvi/emsim_transforms.html)

**Requires:** Electric Motor Simulation Toolkit

Transforms the three-phase current or voltage to alpha and beta currents or voltages.

The three-phase current or voltage is the AC current or voltage of a three-phase circuit, while the alpha, beta currents or voltages are currents or voltages in the (α,β) orthogonal coordinate system.

[Details](#details)

[IMAGE alt='image' src='clarke_transform.gif']

|  | a specifies the a current or voltage, in amperes or volts, of the three-phase current or voltage. |
| --- | --- |
|  | b specifies the b current or voltage, in amperes or volts, of the three-phase current or voltage. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha returns the alpha current or voltage, in amperes or volts, from the Clarke transform. |
|  | beta returns the beta current or voltage, in amperes or volts, from the Clarke transform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Clarke Transform Details

The equations for transforming the current and the voltage are similar. This section takes the current equations for an example.

This VI assumes that *I<sub>a</sub>+I<sub>b</sub>+I<sub>c</sub>*=0, where *I<sub>a</sub>* is the value of the a current, *I<sub>b</sub>* is the value of the b current, and *I<sub>c</sub>* is the value of the c current of the three-phase current.

The following equations convert three-phase current to alpha and beta current:

[IMAGE alt='image' src='eq_abc_alpha.gif']

[IMAGE alt='image' src='eq_abc_beta.gif']

| where | Iα is the alpha current |
| --- | --- |
|  | Iβ is the beta current |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/create_pmsm_fea_model.html language=enus -->
## TOPIC 00034: Create PMSM FEA Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/create_pmsm_fea_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/create_pmsm_fea_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create PMSM FEA Model VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Reads the [RTT file](../lvemsimshared/rtt_file.html) to get a LabVIEW class reference of permanent magnet synchronous motor (PMSM) FEA model.

[Examples](#examples)

[IMAGE alt='image' src='create_pmsm_fea_model.gif']

|  | RTT file specifies the path to an RTT file. The RTT file contains motor parameters and data that the JMAG-RT software generates. |
| --- | --- |
|  | temperature correction parameters specifies the characteristics of the electric motor for temperature correction. If the value of any temperature correction parameter is not a number (NaN), this VI reads the temperature correction parameter from the RTT file. coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. |
|  | coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. |
|  | magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. |
|  | magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PMSM FEA model returns and saves the parameters and data of the PMSM in a LabVIEW class. You can use this LabVIEW class object as input to the PMSM FEA Model VI and the Generate PMSM FEA Model FPGA Data VI. |
|  | PMSM type returns the connection type and the number of poles of the electric motor. connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. If the RTT file uses delta connection, LabVIEW returns error code -376401. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. number of poles returns the number of poles in the electric motor. |
|  | connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. If the RTT file uses delta connection, LabVIEW returns error code -376401. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
| 0 | Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages. |
| 1 | Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
|  | number of poles returns the number of poles in the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Create PMSM FEA Model VI:

- PMSM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation
- labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Control Simulation\PMSM FEA Model Control Simulation.lvproj

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/create_pmsm_variable_parameter_model.html language=enus -->
## TOPIC 00035: Create PMSM Variable Parameter Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/create_pmsm_variable_parameter_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/create_pmsm_variable_parameter_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create PMSM Variable Parameter Model VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Reads the [RTT file](../lvemsimshared/rtt_file.html), the [ANSYS motor model file](../lvemsimshared/ansys_file.html), or imports an [external model](../lvemsimshared/vari_para_model.html) to get a LabVIEW class reference of permanent magnet synchronous motor (PMSM) variable parameter model. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)  [Examples](#examples)

#### Create PMSM Variable Parameter Model (RTT File)

Reads the RTT file to get a LabVIEW class reference of PMSM variable parameter model.

[IMAGE alt='image' src='create_pmsm_variable_parameter_model_rtt_file.gif']

|  | RTT file specifies the path to an RTT file. The RTT file contains motor parameters and data that the JMAG-RT software generates. |
| --- | --- |
|  | table size specifies the number of rows and columns in a two-dimensional table. By default, the table has the same number of rows and columns. The value of table size must be greater than 0. |
|  | temperature correction parameters specifies the characteristics of the electric motor for temperature correction. If the value of any temperature correction parameter is not a number (NaN), this VI reads the temperature correction parameter from the RTT file. coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. |
|  | coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. |
|  | magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. |
|  | magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PMSM variable parameter model returns and saves the parameters and data of the PMSM in a LabVIEW class. You can use this LabVIEW class object as the input to the PMSM Variable Parameter VI and the Generate PMSM Variable Parameter Model FPGA Data VI. |
|  | PMSM type returns the connection type and the number of poles of the electric motor. connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. If the RTT file uses delta connection, LabVIEW returns error code -376401. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. number of poles returns the number of poles in the electric motor. |
|  | connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. If the RTT file uses delta connection, LabVIEW returns error code -376401. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
| 0 | Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages. |
| 1 | Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
|  | number of poles returns the number of poles in the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create PMSM Variable Parameter Model (ANSYS File)

Reads the ANSYS motor model file to get a LabVIEW class reference of PMSM variable parameter model.

[IMAGE alt='image' src='create_pmsm_variable_parameter_model_ansys_file.gif']

|  | ANSYS file specifies the path to an ANSYS motor model file. The ANSYS motor model file contains motor parameters and data that the ANSYS simulation software generates. |
| --- | --- |
|  | temperature correction parameters specifies the characteristics of the electric motor for temperature correction. If the value of any temperature correction parameter is not a number (NaN), this VI reads the temperature correction parameter from the ANSYS motor model file. coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default is NaN. |
|  | coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default is NaN. |
|  | magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default is NaN. |
|  | magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default is NaN. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PMSM variable parameter model returns and saves the parameters and data of the PMSM in a LabVIEW class. You can use this LabVIEW class object as the input to the PMSM Variable Parameter VI and the Generate PMSM Variable Parameter Model FPGA Data VI. |
|  | PMSM type returns the connection type and the number of poles of the electric motor. connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. number of poles returns the number of poles in the electric motor. |
|  | connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
| 0 | Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages. |
| 1 | Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
|  | number of poles returns the number of poles in the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create PMSM Variable Parameter Model (External Model)

Imports an external model to get a LabVIEW class reference of PMSM variable parameter model.

[IMAGE alt='image' src='create_pmsm_variable_parameter_model_external_model.gif']

|  | inductance tables specifies two tables which list the direct inductance and quad inductance. The two tables share the same axes. d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. d current specifies the current, in amperes, along the d or direct axis. The length of this array must be equal to the number of columns in the d inductance table and the q inductance table. The values of d current must be in ascending order. q current specifies the current, in amperes, along the q or quad axis. The length of this array must be equal to the number of rows in the d inductance table and the q inductance table. The values of q current must be in ascending order. |
| --- | --- |
|  | d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. |
|  | q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. |
|  | d current specifies the current, in amperes, along the d or direct axis. The length of this array must be equal to the number of columns in the d inductance table and the q inductance table. The values of d current must be in ascending order. |
|  | q current specifies the current, in amperes, along the q or quad axis. The length of this array must be equal to the number of rows in the d inductance table and the q inductance table. The values of q current must be in ascending order. |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | resistance specifies the resistance, in ohms, of the electric motor. The value of resistance must be greater than 0. |
|  | temperature correction parameters specifies the characteristics of the electric motor for temperature correction. coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default value is 0. coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default value is 0. magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default value is 0. magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default value is 0. |
|  | coil base temperature specifies the base temperature, in kelvins, of the motor coil. The value of coil base temperature must be equal to or greater than 0. The default value is 0. |
|  | coil temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the motor resistance. The material of the coil determines the value of coil temperature coefficient. The default value is 0. |
|  | magnet base temperature specifies the base temperature, in kelvins, of the motor magnet. The value of magnet base temperature must be equal to or greater than 0. The default value is 0. |
|  | magnet temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the magnet flux. The material of the magnet determines the value of magnet temperature coefficient. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | flux table specifies a two-dimensional table of magnet flux. flux specifies a two-dimensional table of magnet flux in webers. The value of flux must be greater than 0. d current specifies the current, in amperes, along the d or direct axis. The length of this array must be equal to the number of columns in the flux table. The values of d current must be in ascending order. q current specifies the current, in amperes, along the q or quad axis. The length of this array must be equal to the number of rows in the flux table. The values of q current must be in ascending order. |
|  | flux specifies a two-dimensional table of magnet flux in webers. The value of flux must be greater than 0. |
|  | d current specifies the current, in amperes, along the d or direct axis. The length of this array must be equal to the number of columns in the flux table. The values of d current must be in ascending order. |
|  | q current specifies the current, in amperes, along the q or quad axis. The length of this array must be equal to the number of rows in the flux table. The values of q current must be in ascending order. |
|  | PMSM variable parameter model returns and saves the parameters and data of the PMSM in a LabVIEW class. You can use this LabVIEW class object as the input to the PMSM Variable Parameter VI and the Generate PMSM Variable Parameter Model FPGA Data VI. |
|  | PMSM type returns the connection type and the number of poles of the electric motor. connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. number of poles returns the number of poles in the electric motor. |
|  | connection type returns how the permanent magnet synchronous motor is connected to the circuit. Currently, the Electric Motor Simulation Toolkit only supports the star connection. 0Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages.1Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
| 0 | Star—Returns the connection type as star connection. High voltage transmission systems typically use star connections. Star connections offer the advantage of providing multiple voltages. |
| 1 | Delta—Returns the connection type as delta connection. Low voltage distribution systems typically use delta connections. Delta connections offer the advantage of high reliability. |
|  | number of poles returns the number of poles in the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create PMSM Variable Parameter Model Details

The following figure shows the structure of the **inductance tables** and the **flux table**. The column axis is **d current**. The row axis is **q current**.

[IMAGE alt='image' src='noloc_eps_induc_table.gif']

In the d inductance table, the value of **d inductance** can be shown as *L*<sub>d</sub> (*I*<sub>q</sub>, *I*<sub>d</sub>). In the q inductance table, the value of **q inductance** can be shown as *L*<sub>q</sub> (*I*<sub>q</sub>, *I*<sub>d</sub>). In the flux table, the value of **flux** can be shown as *F* (*I*<sub>q</sub>, *I*<sub>d</sub>).

| where | Ld is the d inductance table |
| --- | --- |
|  | Lq is the q inductance table |
|  | Id is d current |
|  | Iq is q current |
|  | F is the flux table |

#### Examples

Refer to the following VIs for examples of using the Create PMSM Variable Parameter Model VI:

- PMSM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation
- labview\examples\Electric Motor Simulation\PMSM\PMSM Variable Parameter Model Control Simulation\PMSM Variable Parameter Model Control Simulation.lvproj

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/dq_abc_transform.html language=enus -->
## TOPIC 00036: DQ to ABC Transform VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/dq_abc_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/dq_abc_transform.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DQ to ABC Transform VI

**Owning Palette:** [Transforms VIs](../lvemsimvi/emsim_transforms.html)

**Requires:** Electric Motor Simulation Toolkit

Transforms the direct and quad currents or voltages to three-phase current or voltage.

The three-phase current or voltage is the AC current or voltage of the three-phase circuit, while the d, q currents or voltages are the direct and quad current or voltage in the flux, torque (d, q) rotating reference frame.

[Details](#details)

[IMAGE alt='image' src='dq_to_abc_transform.gif']

|  | d specifies the direct current or voltage, in amperes or volts, from the Clarke and Park transform. |
| --- | --- |
|  | q specifies the quad current or voltage, in amperes or volts, from the Clarke and Park transform. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | a returns the a current or voltage, in amperes or volts, calculated by the inverse Park and Clarke transform. |
|  | b returns the b current or voltage, in amperes or volts, calculated by the inverse Park and Clarke transform. |
|  | c returns the c current or voltage, in amperes or volts, calculated by the inverse Park and Clarke transform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DQ to ABC Transform Details

The equations for transforming current and voltage are similar. This section takes the current equations for an example.

This VI converts the direct and quad currents to three-phase current using the following equations:

[IMAGE alt='image' src='eq_acurrent.gif']

[IMAGE alt='image' src='eq_bcurrent.gif']

[IMAGE alt='image' src='eq_ccurrent.gif']

| where | Ia is the a current of the three-phase current |
| --- | --- |
|  | Ib is the b current of the three-phase current |
|  | Ic is the c current of the three-phase current |
|  | Id is the d or direct current |
|  | Iq is the q or quad current |
|  | θ is the mechanical rotor position in radians |

The values of I<sub>a</sub>, I<sub>b</sub>, and I<sub>c</sub> also come out of the following equations:

[IMAGE alt='image' src='eq_acurrent_1.gif']

[IMAGE alt='image' src='eq_bcurrent_1.gif']

[IMAGE alt='image' src='eq_ccurrent_1.gif']

where

[IMAGE alt='image' src='eq_dq_alpha.gif']

[IMAGE alt='image' src='eq_dq_beta.gif']

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_acim.html language=enus -->
## TOPIC 00037: AC Induction Motor VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_acim.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_acim.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AC Induction Motor VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the AC Induction Motor VIs to simulate an AC induction motor (ACIM).

| Palette Object | Description |
| --- | --- |
| ACIM Constant Parameter Model | Simulates the AC Induction Motor (ACIM) by using the constant parameter model function. |
| Generate ACIM Constant Parameter Model FPGA Data | Generates data for simulating an AC Induction Motor (ACIM) on FPGA targets by using the constant parameter model function. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_error_codes.html language=enus -->
## TOPIC 00038: Error Codes (Electric Motor Simulation Toolkit)

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_error_codes.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Electric Motor Simulation Toolkit)

The [Electric Motor Simulation](../lvemsimvi/emsim_vis.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −376442 | Temperature correction failed and led to negative or zero resistance or flux. Possible reasons: the temperature correction parameters are invalid; the temperature is invalid; the resistance or the flux before temperature correction is invalid. Contact NI for technical support. |
| −376441 | The keyword in the CSV file is invalid. Possible reasons: the keyword is not in the keyword list; the keyword is not located in the first column; the keyword is duplicated. Contact NI for technical support. |
| −376440 | Table in the CSV file contains blanks. |
| −376439 | In the CSV file, a keyword does not have content or the content is not a pure number. |
| −376438 | The RIO device for the custom device is not local to the controller target. |
| −376437 | The ACIM constant parameters are invalid. Refer to the help of the ACIM constant parameters input for how to specify valid parameters. |
| −376436 | The inverter parameters are invalid. Refer to the help of the inverter parameters input for how to specify valid parameters. |
| −376435 | The DC voltage must be greater than 0. |
| −376434 | The model file is invalid. Refer to the Electric Motor Simulation Toolkit help for valid model files. |
| −376433 | The values of current in the external model must be in ascending order. |
| −376432 | Some of the temperature correction parameters are NaN. Refer to the help of the temperature correction parameters input for how to specify valid parameters. |
| −376431 | The number of phases in the RTT file must match the number of phases that you specified. Change the number of phases in the RTT file. |
| −376429 | Overflow occurred during FPGA data generation. Adjust the base values and try again. Refer to the Electric Motor Simulation Toolkit concepts for how to specify a proper base value. |
| −376428 | The size of the look-up table in the RTT file or the external model is too large to fit the FPGA target. |
| −376427 | The segmentation of the table axis in the RTT file is not supported. |
| −376426 | The resistance is invalid. Refer to the help of the resistance input for how to specify a valid value for the resistance. |
| −376425 | The PMSM constant parameters are invalid. Refer to the help of the PMSM constant parameters input for how to specify valid parameters. |
| −376424 | The mechanical parameters are invalid. Refer to the help of the mechanical parameters input for how to specify valid parameters. |
| −376423 | The input array size does not match the number of phases. For example, if the number of phases is 3, the input array of voltage must contain three elements. |
| −376422 | The number of poles must be an even number. |
| −376421 | The number of phases is invalid. For switched reluctance motors, the number of phases must be 3, 4, or 5. |
| −376420 | The FPGA bitfile and the RTT file do not match. Ensure the motor type and model function of the bitfile both match those of the RTT file. |
| −376404 | Failed to read the RTT file of the PMSM variable parameter model. Contact NI for technical support. |
| −376403 | Failed to read the RTT file of the PMSM FEA model. Contact NI for technical support. |
| −376402 | Failed to read the RTT file of the SRM FEA model. Contact NI for technical support. |
| −376401 | Failed to read the RTT file. Possible reasons: the RTT file is neither for a permanent magnet synchronous motor or switched reluctance motor; the RTT file is invalid. Contact NI for technical support. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_inverter.html language=enus -->
## TOPIC 00039: Inverter VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_inverter.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_inverter.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverter VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Inverter VIs to simulate an inverter.

| Palette Object | Description |
| --- | --- |
| 3-Phase Inverter Model | Simulates a three-phase inverter. You must manually select the polymorphic instance you want to use. |
| Generate 3-Phase Inverter Model FPGA Data | Generates data for simulating a three-phase inverter on FPGA targets. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_measure.html language=enus -->
## TOPIC 00040: Measurement VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_measure.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_measure.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Measurement VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Measurement VIs to calculate the motor speed and the mechanical rotor position and to simulate a Hall effect sensor or resolver.

| Palette Object | Description |
| --- | --- |
| Hall Effect Sensor Model | Simulates a Hall effect sensor that detects the mechanical position of the motor rotor. |
| Motor Speed and Rotor Position | Calculates the motor speed and mechanical rotor position at the next time step. A time step is the interval between the time at which the electric motor evaluates the running speed and updates the rotor position. |
| Resolver Model | Simulates a resolver that detects the position of the motor rotor. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_pmsm.html language=enus -->
## TOPIC 00041: Permanent Magnet Synchronous Motor VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_pmsm.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_pmsm.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Permanent Magnet Synchronous Motor VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Permanent Magnet Synchronous Motor VIs to simulate a permanent magnet synchronous motor (PMSM).

| Palette Object | Description |
| --- | --- |
| Create PMSM FEA Model | Reads the RTT file to get a LabVIEW class reference of permanent magnet synchronous motor (PMSM) FEA model. |
| Create PMSM Variable Parameter Model | Reads the RTT file, the ANSYS motor model file, or imports an external model to get a LabVIEW class reference of permanent magnet synchronous motor (PMSM) variable parameter model. You must manually select the polymorphic instance you want to use. |
| Generate PMSM Constant Parameter Model FPGA Data | Generates data for simulating a permanent magnet synchronous motor (PMSM) on FPGA targets by using the constant parameter model function. |
| Generate PMSM FEA Model FPGA Data | Generates data for simulating a permanent magnet synchronous motor (PMSM) on FPGA targets by using the JMAG finite element analysis (FEA) model function. Wire data to the resistance input to determine the polymorphic instance to use or manually select the instance. |
| Generate PMSM Variable Parameter Model FPGA Data | Generates data for simulating a permanent magnet synchronous (PMSM) on FPGA targets by using the variable parameter model function. |
| PMSM Constant Parameter Model | Simulates the permanent magnet synchronous motor (PMSM) by using the constant parameter model function. |
| PMSM FEA Model | Simulates the permanent magnet synchronous motor (PMSM) by using the JMAG finite element analysis (FEA) model function. Wire data to the resistance input to determine the polymorphic instance to use or manually select the instance. |
| PMSM Variable Parameter Model | Simulates the permanent magnet synchronous motor (PMSM) by using the variable parameter model function. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_srm.html language=enus -->
## TOPIC 00042: Switched Reluctance Motor VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_srm.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_srm.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Switched Reluctance Motor VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Switched Reluctance Motor VIs to simulate a switched reluctance motor (SRM).

| Palette Object | Description |
| --- | --- |
| Generate SRM FEA Model FPGA Data | Generates data for simulating a switched reluctance motor (SRM) on FPGA targets using the JMAG finite element analysis (FEA) model function. |
| Generate SRM Linear Model FPGA Data | Generates data and parameters for simulating a switched reluctance motor (SRM) on FPGA targets using the linear model function. |
| Read SRM RTT File | Reads the RTT file to get a LabVIEW class reference of switched reluctance motor (SRM) FEA model. |
| SRM FEA Model | Simulates a switched reluctance motor (SRM) using the JMAG finite element analysis (FEA) model function. |
| SRM Linear Model | Simulates a switched reluctance motor (SRM) using the linear model function. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_transforms.html language=enus -->
## TOPIC 00043: Transforms VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_transforms.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_transforms.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Transforms VIs

**Owning Palette:** [Electric Motor Simulation VIs](../lvemsimvi/emsim_vis.html)

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Transforms VIs to perform the Clarke transform and the inverse Clarke transform. You can also use the Transforms VIs to transform three-phase currents or voltages to direct and quad currents or voltages.

| Palette Object | Description |
| --- | --- |
| ABC to DQ Transform | Transforms the three-phase current or voltage to direct and quad currents or voltages. |
| Clarke Transform | Transforms the three-phase current or voltage to alpha and beta currents or voltages. |
| DQ to ABC Transform | Transforms the direct and quad currents or voltages to three-phase current or voltage. |
| Inverse Clarke Transform | Transforms the alpha and beta currents or voltages to three-phase current or voltage. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/emsim_vis.html language=enus -->
## TOPIC 00044: Electric Motor Simulation VIs

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/emsim_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/emsim_vis.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Electric Motor Simulation VIs

October 2015, 373999C-01

**Requires:** Electric Motor Simulation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Electric Motor Simulation VIs to control and simulate electric motors.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Electric Motor Simulation error codes](../lvemsimvi/emsim_error_codes.html).

| Subpalette | Description |
| --- | --- |
| AC Induction Motor VIs | Use the AC Induction Motor VIs to simulate an AC induction motor (ACIM). |
| Inverter VIs | Use the Inverter VIs to simulate an inverter. |
| Measurement VIs | Use the Measurement VIs to calculate the motor speed and the mechanical rotor position and to simulate a Hall effect sensor or resolver. |
| Permanent Magnet Synchronous Motor VIs | Use the Permanent Magnet Synchronous Motor VIs to simulate a permanent magnet synchronous motor (PMSM). |
| Switched Reluctance Motor VIs | Use the Switched Reluctance Motor VIs to simulate a switched reluctance motor (SRM). |
| Transforms VIs | Use the Transforms VIs to perform the Clarke transform and the inverse Clarke transform. You can also use the Transforms VIs to transform three-phase currents or voltages to direct and quad currents or voltages. |

© 2013–2015 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_acim_cons_para_fpga.html language=enus -->
## TOPIC 00045: Generate ACIM Constant Parameter Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_acim_cons_para_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_acim_cons_para_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate ACIM Constant Parameter Model FPGA Data VI

**Owning Palette:** [AC Induction Motor VIs](../lvemsimvi/emsim_acim.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating an AC Induction Motor (ACIM) on FPGA targets by using the [constant parameter model](../lvemsimshared/cons_para_model.html) function.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on the FPGA targets.

[IMAGE alt='image' src='generate_acim_constant_parameter_model_fpga_data.gif']

|  | ACIM constant parameters specifies the parameters describing the characteristics of an ACIM. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. stator leakage inductance specifies the leakage inductance, in henries, of the stator windings. The value of stator leakage inductance must be greater than 0. rotor leakage inductance specifies the leakage inductance, in henries, of the rotor windings. The value of rotor leakage inductance must be greater than 0. magnetizing inductance specifies the magnetizing inductance, in henries, of the motor. The value of magnetizing inductance must be greater than 0. stator resistance specifies the resistance, in ohms, of the stator windings. The value of stator resistance must be greater than 0. rotor resistance specifies the resistance, in ohms, of the rotor windings. The value of rotor resistance must be greater than 0. base temperature specifies the base temperature, in kelvins, for the stator resistance and the rotor resistance. The value of base temperature must be equal to or greater than 0. stator temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the stator resistance. rotor temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the rotor resistance. |
| --- | --- |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | stator leakage inductance specifies the leakage inductance, in henries, of the stator windings. The value of stator leakage inductance must be greater than 0. |
|  | rotor leakage inductance specifies the leakage inductance, in henries, of the rotor windings. The value of rotor leakage inductance must be greater than 0. |
|  | magnetizing inductance specifies the magnetizing inductance, in henries, of the motor. The value of magnetizing inductance must be greater than 0. |
|  | stator resistance specifies the resistance, in ohms, of the stator windings. The value of stator resistance must be greater than 0. |
|  | rotor resistance specifies the resistance, in ohms, of the rotor windings. The value of rotor resistance must be greater than 0. |
|  | base temperature specifies the base temperature, in kelvins, for the stator resistance and the rotor resistance. The value of base temperature must be equal to or greater than 0. |
|  | stator temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the stator resistance. |
|  | rotor temperature coefficient specifies the coefficient, in K^-1, for temperature correction of the rotor resistance. |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | ACIM constant parameters on FPGA returns the motor parameters, such as numbers of poles and resistance, which you can use to simulate an electric motor on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_pmsm_cons_para_fpga.html language=enus -->
## TOPIC 00046: Generate PMSM Constant Parameter Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_pmsm_cons_para_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_pmsm_cons_para_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate PMSM Constant Parameter Model FPGA Data VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating a permanent magnet synchronous motor (PMSM) on FPGA targets by using the [constant parameter model](../lvemsimshared/cons_para_model.html) function.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on the FPGA targets.

[IMAGE alt='image' src='generate_pmsm_constant_parameter_model_fpga_data.gif']

|  | PMSM constant parameters specifies the parameters describing the characteristics of a PMSM. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. resistance specifies the resistance, in ohms, in the electric motor. The value of resistance must be greater than 0. d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. flux linkage specifies the flux linkage, in webers, between the rotor and the stator. The value of flux linkage must be greater than 0. |
| --- | --- |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | resistance specifies the resistance, in ohms, in the electric motor. The value of resistance must be greater than 0. |
|  | d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. |
|  | q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. |
|  | flux linkage specifies the flux linkage, in webers, between the rotor and the stator. The value of flux linkage must be greater than 0. |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | PMSM constant parameters on FPGA returns the motor parameters, such as numbers of poles and resistance, which you can use to simulate an electric motor on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_pmsm_fea_fpga.html language=enus -->
## TOPIC 00047: Generate PMSM FEA Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_pmsm_fea_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_pmsm_fea_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate PMSM FEA Model FPGA Data VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating a permanent magnet synchronous motor (PMSM) on FPGA targets by using the [JMAG finite element analysis (FEA) model](../lvemsimshared/fea_model.html) function. Wire data to the **resistance** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on FPGA targets. You can transfer the FPGA data and motor parameters to an FPGA target where you simulate a motor. You can either use the [direct memory access (DMA)](/csh?topicname=lvfpgaconcepts/fpga_dma_communication.html) or the [front panel controls in an FPGA VI](/csh?topicname=lvfpgaconcepts/pfi_data_transfer.html) to transfer data and parameters from the host computer to an FPGA target.

#### Generate FPGA Data (Uniform Resistance)

[IMAGE alt='image' src='generate_fpga_data_uniform_resistance.gif']

|  | PMSM FEA model specifies a reference to the PMSM FEA model. Use the Create PMSM FEA Model VI to generate this reference. |
| --- | --- |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | base values specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation. voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. |
|  | current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. |
|  | speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding with a positive number. If the value of resistance is equal to or less than 0, this VI uses the resistance in the PMSM FEA model reference for calculation. The default value is -1. |
|  | FPGA data returns the data of the PMSM FEA model as an array of integer numbers. The FPGA data contains results, such as the inductance and torque of the motor, from the finite element analysis as the current in the motor varies. Use the direct memory access (DMA) to transfer the FPGA data from the host computer to an FPGA target. |
|  | PMSM FEA model parameters on FPGA returns the motor parameters, such as number of poles and resistance, for use by the electric motor simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | base values advanced returns the base values of the resistance, flux, inductance, and torque. This VI calculates base values advanced from the voltage, current, and speed base in the base values input. voltage base returns the base value of the voltage in volts. current base returns the base value of the current in amperes. speed base returns the base value of the motor speed in revolutions per minute. resistance base returns the base value of the resistance in ohms. flux base returns the base value of the flux linkage in webers. inductance base returns the base value of the inductance in henries. torque base returns the base value of the torque in newton meters. |
|  | voltage base returns the base value of the voltage in volts. |
|  | current base returns the base value of the current in amperes. |
|  | speed base returns the base value of the motor speed in revolutions per minute. |
|  | resistance base returns the base value of the resistance in ohms. |
|  | flux base returns the base value of the flux linkage in webers. |
|  | inductance base returns the base value of the inductance in henries. |
|  | torque base returns the base value of the torque in newton meters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generate FPGA Data (Phase Resistance)

[IMAGE alt='image' src='generate_fpga_data_phase_resistance.gif']

|  | PMSM FEA model specifies a reference to the PMSM FEA model. Use the Create PMSM FEA Model VI to generate this reference. |
| --- | --- |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | base values specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation. voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. |
|  | current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. |
|  | speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding under each phase of the three phases. Therefore, this array must have three elements, and each array element must specify the resistance under one phase. If this array is empty, this VI uses the resistance in the PMSM FEA model reference for calculation. |
|  | FPGA data returns the data of the PMSM FEA model as an array of integer numbers. The FPGA data contains results, such as the inductance and torque of the motor, from the finite element analysis as the current in the motor varies. Use the direct memory access (DMA) to transfer the FPGA data from the host computer to an FPGA target. |
|  | PMSM FEA model parameters on FPGA returns the motor parameters, such as number of poles and resistance, for use by the electric motor simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | base values advanced returns the base values of the resistance, flux, inductance, and torque. This VI calculates base values advanced from the voltage, current, and speed base in the base values input. voltage base returns the base value of the voltage in volts. current base returns the base value of the current in amperes. speed base returns the base value of the motor speed in revolutions per minute. resistance base returns the base value of the resistance in ohms. flux base returns the base value of the flux linkage in webers. inductance base returns the base value of the inductance in henries. torque base returns the base value of the torque in newton meters. |
|  | voltage base returns the base value of the voltage in volts. |
|  | current base returns the base value of the current in amperes. |
|  | speed base returns the base value of the motor speed in revolutions per minute. |
|  | resistance base returns the base value of the resistance in ohms. |
|  | flux base returns the base value of the flux linkage in webers. |
|  | inductance base returns the base value of the inductance in henries. |
|  | torque base returns the base value of the torque in newton meters. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_pmsm_vari_para_fpga.html language=enus -->
## TOPIC 00048: Generate PMSM Variable Parameter Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_pmsm_vari_para_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_pmsm_vari_para_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate PMSM Variable Parameter Model FPGA Data VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating a permanent magnet synchronous (PMSM) on FPGA targets by using the [variable parameter model](../lvemsimshared/vari_para_model.html) function.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on FPGA targets. You can transfer the FPGA data and motor parameters to an FPGA target where you simulate a motor. You can either use the [direct memory access (DMA)](/csh?topicname=lvfpgaconcepts/fpga_dma_communication.html) or the [front panel controls in an FPGA VI](/csh?topicname=lvfpgaconcepts/pfi_data_transfer.html) to transfer data and parameters from the host computer to an FPGA target.

[IMAGE alt='image' src='generate_pmsm_variable_parameter_model_fpga_data.gif']

|  | PMSM variable parameter model specifies a reference to the PMSM variable parameter model. Use the Create PMSM Variable Parameter Model VI to generate this reference. |
| --- | --- |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding with a positive number. If the value of resistance is equal to or less than 0, this VI uses the resistance in the PMSM variable parameter model reference for calculation. The default value is -1. |
|  | FPGA data returns the data of the PMSM variable parameter model as an array of integer numbers. The FPGA data contains results, such as the inductance and flux of the motor, as the current in the motor varies. Use the DMA to transfer the FPGA data from the host computer to an FPGA target. |
|  | PMSM variable parameters on FPGA returns the motor parameters, such as number of poles and resistance, for use by the electric motor simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_srm_fea_fpga.html language=enus -->
## TOPIC 00049: Generate SRM FEA Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_srm_fea_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_srm_fea_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate SRM FEA Model FPGA Data VI

**Owning Palette:** [Switched Reluctance Motor VIs](../lvemsimvi/emsim_srm.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating a switched reluctance motor (SRM) on FPGA targets using the [JMAG finite element analysis (FEA) model](../lvemsimshared/fea_model.html) function.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on FPGA targets. You can transfer the FPGA data and motor parameters to an FPGA target where you simulate a motor. You can either use the [direct memory access (DMA)](/csh?topicname=lvfpgaconcepts/fpga_dma_communication.html) or the [front panel controls in an FPGA VI](/csh?topicname=lvfpgaconcepts/pfi_data_transfer.html) to transfer data and parameters from the host computer to an FPGA target.

[IMAGE alt='image' src='generate_srm_fea_model_fpga_data.gif']

|  | SRM FEA model specifies a reference to the SRM FEA model. Use the Read SRM RTT File VI to generate this reference. |
| --- | --- |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | base values specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation. voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. |
|  | current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. |
|  | speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | initial state specifies the initial state of the motor when the motor starts. initial rotor position specifies the mechanical rotor position, in degrees, when the motor starts. The default value is 0. initial current specifies the current, in amperes, in each phase when the motor starts. The default value is 0. |
|  | initial rotor position specifies the mechanical rotor position, in degrees, when the motor starts. The default value is 0. |
|  | initial current specifies the current, in amperes, in each phase when the motor starts. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance in ohms. If the value of resistance is equal to or less than zero, this VI uses the data in the SRM FEA model reference for calculation. The default value is -1. |
|  | FPGA data returns the data of the SRM FEA model as an array of integer numbers. The FPGA data contains results of the finite element analysis, such as the inductance and torque of the motor, as the current in the motor varies. Use the direct memory access (DMA) to transfer the FPGA data from the host computer to an FPGA target. |
|  | SRM model information returns the motor parameters, such as number of poles and resistance, for use by the electric motor simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | SRM initial state and scaling factors returns the motor state at the starting point and the scaling factors on FPGA targets. initial rotor position returns the mechanical rotor position, in degrees, when the motor starts. initial electric angle returns the electric angle of each phase, in degrees, when the motor starts. initial inductance returns the inductance, in henries, of the motor when the motor starts. current factor returns the factor to scale the current of the simulated motor on FPGA targets. inductance factor returns the factor to scale the inductance of the simulated motor on FPGA targets. torque factor returns the factor to scale the torque of the simulated motor on FPGA targets. voltage factor returns the factor to scale the voltage of the simulated motor on FPGA targets. scaled R*dt returns the scaled value calculated by the following formula: y=(R * dt) / x, where R is the resistance and x is the inductance factor. |
|  | initial rotor position returns the mechanical rotor position, in degrees, when the motor starts. |
|  | initial electric angle returns the electric angle of each phase, in degrees, when the motor starts. |
|  | initial inductance returns the inductance, in henries, of the motor when the motor starts. |
|  | current factor returns the factor to scale the current of the simulated motor on FPGA targets. |
|  | inductance factor returns the factor to scale the inductance of the simulated motor on FPGA targets. |
|  | torque factor returns the factor to scale the torque of the simulated motor on FPGA targets. |
|  | voltage factor returns the factor to scale the voltage of the simulated motor on FPGA targets. |
|  | scaled R*dt returns the scaled value calculated by the following formula: y=(R * dt) / x, where R is the resistance and x is the inductance factor. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/gen_srm_linear_fpga.html language=enus -->
## TOPIC 00050: Generate SRM Linear Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/gen_srm_linear_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/gen_srm_linear_fpga.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate SRM Linear Model FPGA Data VI

**Owning Palette:** [Switched Reluctance Motor VIs](../lvemsimvi/emsim_srm.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data and parameters for simulating a switched reluctance motor (SRM) on FPGA targets using the [linear model](../lvemsimshared/line_model.html) function.

This VI prepares the FPGA data on the desktop, and thus reduces the workload of calculations on FPGA targets.

[Example](#examples)

[IMAGE alt='image' src='generate_srm_linear_model_fpga_data.gif']

|  | SRM linear model parameters specifies the parameters describing the linear model of an SRM. unaligned inductance specifies the equivalent inductance, in henries, of the coil at the unaligned position. saturated position current specifies the current, in amperes, of the coil at the saturated position. aligned flux specifies the flux, in webers, of the saturated position current at the aligned position. max current specifies the maximum current in amperes. rotor position offset specifies the angle, in degrees, between the rotor salient pole and the stator salient pole when the rotor position is 0. |
| --- | --- |
|  | unaligned inductance specifies the equivalent inductance, in henries, of the coil at the unaligned position. |
|  | saturated position current specifies the current, in amperes, of the coil at the saturated position. |
|  | aligned flux specifies the flux, in webers, of the saturated position current at the aligned position. |
|  | max current specifies the maximum current in amperes. |
|  | rotor position offset specifies the angle, in degrees, between the rotor salient pole and the stator salient pole when the rotor position is 0. |
|  | SRM type specifies the number of poles and phases in the electric motor. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. number of phases specifies the number of phases in an electric motor. The number of phases can only be 3, 4, or 5. |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | number of phases specifies the number of phases in an electric motor. The number of phases can only be 3, 4, or 5. |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | initial rotor position specifies the mechanical rotor position, in degrees, when the motor starts. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies the resistance, in ohms, of the electric motor. The value of resistance must be greater than 0. |
|  | SRM linear model parameters on FPGA returns a reference to the SRM linear model, which you can use to simulate an electric motor on an FPGA target. Use the front panel controls in an FPGA VI to transfer the motor parameters from the host computer to an FPGA target. |
|  | model initial state returns information about the SRM linear model at the starting time. Use the information of initial state for calculations on FPGA targets later. rotor speed returns the rotor speed, in radian per second, when the motor starts. rotor position returns the mechanical rotor position, in radian, when the motor starts. delta theta returns the increment in the rotor position at the starting time. The unit is radian. theta returns an array that contains the electric angles of all SRM phases. sin (# of poles * theta) returns an array of numbers calculated by the following formula: sin ( # of poles * theta), where # of poles is the number of poles, and theta is the electric angle. cos (# of poles * theta) returns an array of numbers calculated by the following formula: cos ( # of poles * theta), where # of poles is the number of poles, and theta is the electric angle. |
|  | rotor speed returns the rotor speed, in radian per second, when the motor starts. |
|  | rotor position returns the mechanical rotor position, in radian, when the motor starts. |
|  | delta theta returns the increment in the rotor position at the starting time. The unit is radian. |
|  | theta returns an array that contains the electric angles of all SRM phases. |
|  | sin (# of poles * theta) returns an array of numbers calculated by the following formula: sin ( # of poles * theta), where # of poles is the number of poles, and theta is the electric angle. |
|  | cos (# of poles * theta) returns an array of numbers calculated by the following formula: cos ( # of poles * theta), where # of poles is the number of poles, and theta is the electric angle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the SRM Linear Model Configuration VI in the labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Configuration directory for an example of using the Generate SRM Linear Model FPGA Data VI.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/generate_inverter_model_fpga_data.html language=enus -->
## TOPIC 00051: Generate 3-Phase Inverter Model FPGA Data VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/generate_inverter_model_fpga_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/generate_inverter_model_fpga_data.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generate 3-Phase Inverter Model FPGA Data VI

**Owning Palette:** [Inverter VIs](../lvemsimvi/emsim_inverter.html)

**Requires:** Electric Motor Simulation Toolkit

Generates data for simulating a [three-phase inverter](../lvemsimshared/inverter.html) on FPGA targets. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

This VI prepares the FPGA data on the host computer, and thus reduces the workload of calculations on FPGA targets. You can transfer the FPGA data to an FPGA target where you simulate an inverter. You can use the [front panel controls in an FPGA VI](/csh?topicname=lvfpgaconcepts/pfi_data_transfer.html) to transfer data from the host computer to an FPGA target.

#### Generate 3-Phase Inverter Model FPGA Data (FXP)

Generates fixed-point data for simulating a three-phase inverter on FPGA targets.

[IMAGE alt='image' src='generate_3-phase_inverter_model_fpga_data_fxp.gif']

|  | inverter parameters specifies the characteristics of the inverter. IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
| --- | --- |
|  | IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
|  | DC voltage specifies the DC voltage, in volts, on the inverter. |
|  | base values specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation. voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | voltage base specifies the base value of the voltage, in volts, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 volt. |
|  | current base specifies the base value of the current, in amperes, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 ampere. |
|  | speed base specifies the base value of the speed, in revolutions per minute, that you can use to convert an engineering unit to a per-unit, and vice versa. The default is 1 revolution per minute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | inverter parameters on FPGA returns the inverter parameters, such as DC voltage, IGBT forward voltage drop, diode forward voltage drop, and conductance, for use by the inverter simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the inverter parameters from the host computer to an FPGA target. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generate 3-Phase Inverter Model FPGA Data (SGL)

Generates single-precision floating point data for simulating a three-phase inverter on FPGA targets.

[IMAGE alt='image' src='generate_3-phase_inverter_model_fpga_data_sgl.gif']

|  | inverter parameters specifies the characteristics of the inverter. IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
| --- | --- |
|  | IGBT forward voltage drop specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | diode forward voltage drop specifies the forward voltage drop, in volts, of the diode in the inverter. The value of diode forward voltage drop must be equal to or greater than 0. The default is 0. |
|  | conductance specifies the conductance, in siemens, of the switches in the inverter. The value of conductance must be greater than 0. The default is 1. |
|  | DC voltage specifies the DC voltage, in volts, on the inverter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | inverter parameters on FPGA returns the inverter parameters, such as DC voltage, IGBT forward voltage drop, diode forward voltage drop, and conductance, for use by the inverter simulation on an FPGA target. Use the front panel controls in an FPGA VI to transfer the inverter parameters from the host computer to an FPGA target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/hall_effect_sensor_model.html language=enus -->
## TOPIC 00052: Hall Effect Sensor Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/hall_effect_sensor_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/hall_effect_sensor_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Hall Effect Sensor Model VI

**Owning Palette:** [Measurement VIs](../lvemsimvi/emsim_measure.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates a Hall effect sensor that detects the mechanical position of the motor rotor.

The Hall effect sensor represents one type of position sensor that many electric motor applications use. This VI simulates a typical application where three Hall effect sensors locates on the arc of a circle with the same central angle from each other.

[Details](#details)

[IMAGE alt='image' src='hall_effect_sensor_model.gif']

|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
| --- | --- |
|  | Hall configuration specifies the angles that the three Hall effect sensors locate. angle A specifies the angle, in degrees, that the Hall effect sensor A locates. The default value is -60 degrees. angle B specifies the angle, in degrees, that the Hall effect sensor B locates. The default value is 60 degrees. angle C specifies the angle, in degrees, that the Hall effect sensor C locates. The default value is 180 degrees. |
|  | angle A specifies the angle, in degrees, that the Hall effect sensor A locates. The default value is -60 degrees. |
|  | angle B specifies the angle, in degrees, that the Hall effect sensor B locates. The default value is 60 degrees. |
|  | angle C specifies the angle, in degrees, that the Hall effect sensor C locates. The default value is 180 degrees. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Hall A returns the state of Hall effect sensor A, where TRUE is active, and FALSE is inactive. |
|  | Hall B returns the state of Hall effect sensor B, where TRUE is active, and FALSE is inactive. |
|  | Hall C returns the state of Hall effect sensor C, where TRUE is active, and FALSE is inactive. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Hall Effect Sensor Model Details

The following table shows the relationship between sensor states and rotor position. The **Hall configuration** uses the default settings where **angle A** is -60 degrees, **angle B** is 60 degrees, and **angle C** is 180 degrees.

| Sensor | State | Rotor Position |
| --- | --- | --- |
| Hall A | 1 | 0° ≤ θ ≤ 120° or 300° ≤ θ ≤ 360° |
| Hall A | 0 | Others |
| Hall B | 1 | 60° ≤ θ ≤ 240° |
| Hall B | 0 | Others |
| Hall C | 1 | 180° ≤ θ ≤ 360° |
| Hall C | 0 | Others |

The following figure illustrates the relationship between Hall effect sensor states and rotor position.

[IMAGE alt='image' src='loc_fp_hallstate.gif']

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/inverse_clarke_transform.html language=enus -->
## TOPIC 00053: Inverse Clarke Transform VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/inverse_clarke_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/inverse_clarke_transform.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse Clarke Transform VI

**Owning Palette:** [Transforms VIs](../lvemsimvi/emsim_transforms.html)

**Requires:** Electric Motor Simulation Toolkit

Transforms the alpha and beta currents or voltages to three-phase current or voltage.

The three-phase current or voltage is the AC current or voltage of the three-phase circuit, while the alpha, beta currents or voltages are the currents or voltages in the (α,β) orthogonal coordinate system.

[Details](#details)

[IMAGE alt='image' src='inverse_clarke_transform.gif']

|  | alpha specifies the alpha current or voltage, in amperes or volts, from the Clarke transform. |
| --- | --- |
|  | beta specifies the beta current or voltage, in amperes or volts, from the Clarke transform. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | a returns the a current or voltage, in amperes or volts, calculated by the inverse Clarke transform. |
|  | b returns the b current or voltage, in amperes or volts, calculated by the inverse Clarke transform. |
|  | c returns the c current or voltage, in amperes or volts, calculated by the inverse Clarke transform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Clarke Transform Details

The equations for transforming the current and the voltage are similar. This section takes the current equations for an example.

This VI converts the alpha and beta currents to three-phase current using the following equations:

[IMAGE alt='image' src='eq_acurrent_1.gif']

[IMAGE alt='image' src='eq_bcurrent_1.gif']

[IMAGE alt='image' src='eq_ccurrent_1.gif']

| where | Ia is the a current of the three-phase current |
| --- | --- |
|  | Ib is the b current of the three-phase current |
|  | Ic is the c current of the three-phase current |
|  | Iα is the alpha current |
|  | Iβ is the beta current |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/motor_speed_rotor_position.html language=enus -->
## TOPIC 00054: Motor Speed and Rotor Position VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/motor_speed_rotor_position.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/motor_speed_rotor_position.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Motor Speed and Rotor Position VI

**Owning Palette:** [Measurement VIs](../lvemsimvi/emsim_measure.html)

**Requires:** Electric Motor Simulation Toolkit

Calculates the motor speed and mechanical rotor position at the next time step. A time step is the interval between the time at which the electric motor evaluates the running speed and updates the rotor position.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='motor_speed_and_rotor_position.gif']

|  | dt specifies the time step, in seconds, between speed in and speed out, or between rotor position in and rotor position out. The value of dt must be greater than 0. |
| --- | --- |
|  | speed in specifies the current speed, in revolutions per minute, of the electric motor. |
|  | rotor position in specifies the current position, in degrees, of the motor rotor. |
|  | electromagnetic torque specifies the current electromagnetic torque, in newton meters, that the electric motor generates inside the motor while the motor is running. |
|  | load torque specifies the current load torque, in newton meters, that you externally apply to the motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | mechanical parameters specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor. inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | inertia specifies the moment of inertia, in kgm^2, of the electric motor. The value of inertia must be equal to or greater than 0. |
|  | friction coefficient specifies the friction coefficient of the electric motor. The value of friction coefficient must be equal to or greater than 0. |
|  | speed out returns the speed of the motor at the next time step. |
|  | rotor position out returns the position of the rotor at the next time step. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Motor Speed and Rotor Position Details

This VI calculates the motor speed and rotor position at the next time step using the following equations:

[IMAGE alt='image' src='eq_motorspeed_1.gif']

[IMAGE alt='image' src='eq_motorspeed_2.gif']

[IMAGE alt='image' src='eq_motorspeed_3.gif']

| where | J is the moment of inertia of the motor |
| --- | --- |
|  | B is the friction coefficient of the motor |
|  | Te is the electromagnetic torque |
|  | Tl is the load torque |
|  | ωin is speed in |
|  | ωout is speed out |
|  | θin is rotor position in |
|  | θout is rotor position out |

#### Examples

Refer to the following VIs for examples of using the Motor Speed and Rotor Position VI:

- PMSM Constant Parameter Model Closed Loop VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Constant Parameter Model Closed Loop
- PMSM FEA Model Closed Loop VI: labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Closed Loop
- SRM Linear Model Closed Loop Control VI: labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Closed Loop Control
- SRM FEA Model Closed Loop Control VI: labview\examples\Electric Motor Simulation\SRM\SRM FEA Model Closed Loop Control

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/pmsm_cons_para_model.html language=enus -->
## TOPIC 00055: PMSM Constant Parameter Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/pmsm_cons_para_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/pmsm_cons_para_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM Constant Parameter Model VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates the permanent magnet synchronous motor (PMSM) by using the [constant parameter model](../lvemsimshared/cons_para_model.html) function.

[Examples](#examples)

[IMAGE alt='image' src='pmsm_constant_parameter_model.gif']

|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
| --- | --- |
|  | PMSM constant parameters specifies the parameters describing the characteristics of a PMSM. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. resistance specifies the resistance, in ohms, in the electric motor. The value of resistance must be greater than 0. d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. flux linkage specifies the flux linkage, in webers, between the rotor and the stator. The value of flux linkage must be greater than 0. |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | resistance specifies the resistance, in ohms, in the electric motor. The value of resistance must be greater than 0. |
|  | d inductance specifies the inductance, in henries, along the d or direct axis. The value of d inductance must be greater than 0. |
|  | q inductance specifies the inductance, in henries, along the q or quad axis. The value of q inductance must be greater than 0. |
|  | flux linkage specifies the flux linkage, in webers, between the rotor and the stator. The value of flux linkage must be greater than 0. |
|  | voltage specifies the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | speed specifies the rotor speed, in revolutions per minute, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | abc current returns the three-phase current, in amperes, in the electric motor. This output is a three-element array, each element representing one phase of the three-phase current. |
|  | dq current returns the direct current and the quad current in amperes. The value of dq current corresponds to the value of abc current in the flux, torque (d, q) rotating reference frame. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the PMSM Constant Parameter Model VI:

- PMSM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation
- PMSM Constant Parameter Model Closed Loop VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Constant Parameter Model Closed Loop

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/pmsm_fea_model.html language=enus -->
## TOPIC 00056: PMSM FEA Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/pmsm_fea_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/pmsm_fea_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM FEA Model VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates the permanent magnet synchronous motor (PMSM) by using the [JMAG finite element analysis (FEA) model](../lvemsimshared/fea_model.html) function. Wire data to the **resistance** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### PMSM FEA Model (Uniform Resistance)

[IMAGE alt='image' src='pmsm_fea_model_uniform_resistance.gif']

|  | temperature specifies the coil temperature and the magnet temperature of the electric motor. If the value of coil temperature or magnet temperature is greater than 0, this VI performs the temperature correction functionality for the resistance and the magnet flux. coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
| --- | --- |
|  | coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. |
|  | magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
|  | PMSM FEA model specifies a reference to the PMSM FEA model. Use the Create PMSM FEA Model VI to generate this reference. |
|  | voltage specifies the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding with a positive number. If the value of resistance is equal to or less than 0, this VI uses the resistance in the PMSM FEA model reference for calculation. The default value is -1. |
|  | current returns the three-phase current in the electric motor, in amperes. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PMSM FEA Model (Phase Resistance)

[IMAGE alt='image' src='pmsm_fea_model_phase_resistance.gif']

|  | temperature specifies the coil temperature and the magnet temperature of the electric motor. If the value of coil temperature or magnet temperature is greater than 0, this VI performs the temperature correction functionality for the resistance and the magnet flux. coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
| --- | --- |
|  | coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. |
|  | magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
|  | PMSM FEA model specifies a reference to the PMSM FEA model. Use the Create PMSM FEA Model VI to generate this reference. |
|  | voltage specifies the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding under each phase of the three phases. Therefore, this array must have three elements, and each array element must specify the resistance under one phase. If this array is empty, this VI uses the resistance in the PMSM FEA model reference for calculation. |
|  | current returns the three-phase current in the electric motor, in amperes. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the PMSM FEA Model VI:

- PMSM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation
- PMSM FEA Model Closed Loop VI: labview\examples\Electric Motor Simulation\PMSM\PMSM FEA Model Closed Loop

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/pmsm_vari_para_model.html language=enus -->
## TOPIC 00057: PMSM Variable Parameter Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/pmsm_vari_para_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/pmsm_vari_para_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM Variable Parameter Model VI

**Owning Palette:** [Permanent Magnet Synchronous Motor VIs](../lvemsimvi/emsim_pmsm.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates the permanent magnet synchronous motor (PMSM) by using the [variable parameter model](../lvemsimshared/vari_para_model.html) function.

[Examples](#examples)

[IMAGE alt='image' src='pmsm_variable_parameter_model.gif']

|  | temperature specifies the coil temperature and the magnet temperature of the electric motor. If the value of coil temperature or magnet temperature is greater than 0, this VI performs the temperature correction functionality for the resistance and the magnet flux. coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
| --- | --- |
|  | coil temperature specifies the temperature, in kelvins, of the motor coil. The default value is 0. |
|  | magnet temperature specifies the temperature, in kelvins, of the motor magnet. The default value is 0. |
|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
|  | PMSM variable parameter model specifies a reference to the PMSM variable parameter model. Use the Create PMSM Variable Parameter Model VI to generate this reference. |
|  | voltage specifies the three-phase voltage, in volts, of the electric motor. The voltage represents the three-phase voltage in a three-phase electric power system. Therefore, this array must have three elements, and each array element must specify one phase of the voltage. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | speed specifies the rotor speed, in revolutions per minute, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance, in ohms, of the stator winding with a positive number. If the value of resistance is equal to or less than 0, this VI uses the resistance in the PMSM variable parameter model reference for calculation. The default value is -1. |
|  | abc current returns the three-phase current, in amperes, in the electric motor. This output is a three-element array, each element representing one phase of the three-phase current. |
|  | dq current returns the direct current and the quad current in amperes. The value of dq current corresponds to the value of abc current in the flux, torque (d, q) rotating reference frame. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the PMSM Variable Parameter Model VI:

- PMSM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Open Loop Simulation
- PMSM Variable Parameter Model Closed Loop VI: labview\examples\Electric Motor Simulation\PMSM\PMSM Variable Parameter Model Closed Loop

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/read_srm_rtt_file.html language=enus -->
## TOPIC 00058: Read SRM RTT File VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/read_srm_rtt_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/read_srm_rtt_file.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read SRM RTT File VI

**Owning Palette:** [Switched Reluctance Motor VIs](../lvemsimvi/emsim_srm.html)

**Requires:** Electric Motor Simulation Toolkit

Reads the [RTT file](../lvemsimshared/rtt_file.html) to get a LabVIEW class reference of switched reluctance motor (SRM) FEA model.

[Examples](#examples)

[IMAGE alt='image' src='read_srm_rtt_file.gif']

|  | RTT file specifies the path to an RTT file. The RTT file contains motor parameters and data that the JMAG-RT software generates. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SRM FEA model returns and saves the motor's parameters in a LabVIEW class. You can use this LabVIEW class object as input to the SRM FEA Model VI and the Generate SRM FEA Model FPGA Data VI. |
|  | SRM type returns information about the number of poles and phases. number of poles returns the number of poles in the electric motor. number of phases returns the number of phases of the motor. |
|  | number of poles returns the number of poles in the electric motor. |
|  | number of phases returns the number of phases of the motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Read SRM RTT File VI:

- SRM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\SRM\SRM Open Loop Simulation
- labview\examples\Electric Motor Simulation\SRM\3-phase SRM Control Simulation\3-Phase SRM Control Simulation.lvproj
- labview\examples\Electric Motor Simulation\SRM\4-phase SRM Control Simulation\4-Phase SRM Control Simulation.lvproj
- labview\examples\Electric Motor Simulation\SRM\5-phase SRM Control Simulation\5-Phase SRM Control Simulation.lvproj

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/resolver_model.html language=enus -->
## TOPIC 00059: Resolver Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/resolver_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/resolver_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Resolver Model VI

**Owning Palette:** [Measurement VIs](../lvemsimvi/emsim_measure.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates a resolver that detects the position of the motor rotor.

[IMAGE alt='image' src='resolver_model.gif']

|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
| --- | --- |
|  | reference specifies the reference signals that are applied to the resolver. Typically the reference signal is a sine wave. |
|  | transformation ratio specifies the scaling ratio of the output signals. sin ratio specifies the scaling ratio of the output signal by sine of the reference. The default is 1. cos ratio specifies the scaling ratio of the output signal by cosine of the reference. The default is 1. |
|  | sin ratio specifies the scaling ratio of the output signal by sine of the reference. The default is 1. |
|  | cos ratio specifies the scaling ratio of the output signal by cosine of the reference. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sin returns the modulated signal by sine of the reference, calculated by the following formula: sin=sin (rotor position)*reference*sin ratio. |
|  | cos returns the modulated signal by cosine of the reference, calculated by the following formula: cos=cos (rotor position)*reference*cos ratio. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/srm_fea_model.html language=enus -->
## TOPIC 00060: SRM FEA Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/srm_fea_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/srm_fea_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SRM FEA Model VI

**Owning Palette:** [Switched Reluctance Motor VIs](../lvemsimvi/emsim_srm.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates a switched reluctance motor (SRM) using the [JMAG finite element analysis (FEA) model](../lvemsimshared/fea_model.html) function.

[Example](#examples)

[IMAGE alt='image' src='srm_fea_model.gif']

|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
| --- | --- |
|  | SRM FEA model specifies a reference to the SRM FEA model. Use the Read SRM RTT File VI to generate this reference. |
|  | voltage specifies the voltage of each phase of the electric motor in an array. The size of the voltage array must be the same as the number of phase. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies resistance in ohms. If the value of resistance is equal to or less than zero, this VI uses the data in the SRM FEA model reference for calculation. The default value is -1. |
|  | current returns the phase current of the electric motor in an array. The size of the current array must match the number of phases. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the SRM FEA Model Closed Loop Control VI in the labview\examples\Electric Motor Simulation\SRM\SRM FEA Model Closed Loop Control directory for an example of using the SRM FEA Model VI.

<!--NI_TOPIC bundle=labview-electric-motor-simulation-toolkit-api-ref path=lvemsimvi/srm_linear_model.html language=enus -->
## TOPIC 00061: SRM Linear Model VI

- bundle_id: `labview-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimvi/srm_linear_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimvi/srm_linear_model.html
- document_id: `labview-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SRM Linear Model VI

**Owning Palette:** [Switched Reluctance Motor VIs](../lvemsimvi/emsim_srm.html)

**Requires:** Electric Motor Simulation Toolkit

Simulates a switched reluctance motor (SRM) using the [linear model](../lvemsimshared/line_model.html) function.

[Examples](#examples)

[IMAGE alt='image' src='srm_linear_model.gif']

|  | SRM linear model parameters specifies the parameters describing the linear model of an SRM. unaligned inductance specifies the equivalent inductance, in henries, of the coil at the unaligned position. saturated position current specifies the current, in amperes, of the coil at the saturated position. aligned flux specifies the flux, in webers, of the saturated position current at the aligned position. max current specifies the maximum current in amperes. rotor position offset specifies the angle, in degrees, between the rotor salient pole and the stator salient pole when the rotor position is 0. |
| --- | --- |
|  | unaligned inductance specifies the equivalent inductance, in henries, of the coil at the unaligned position. |
|  | saturated position current specifies the current, in amperes, of the coil at the saturated position. |
|  | aligned flux specifies the flux, in webers, of the saturated position current at the aligned position. |
|  | max current specifies the maximum current in amperes. |
|  | rotor position offset specifies the angle, in degrees, between the rotor salient pole and the stator salient pole when the rotor position is 0. |
|  | initialize? specifies whether to initialize the internal state of the electric motor. This VI performs calculations that are dependent on all previous data since the VI last ran or since you set initialize? to TRUE. If you set initialize? to TRUE, this VI resets the internal state of the motor to 0 and restarts the electric motor simulation. The default value is FALSE. |
|  | SRM type specifies the number of poles and phases in the electric motor. number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. number of phases specifies the number of phases in an electric motor. The number of phases can only be 3, 4, or 5. |
|  | number of poles specifies the number of poles in the electric motor. The number of poles must be an even number. |
|  | number of phases specifies the number of phases in an electric motor. The number of phases can only be 3, 4, or 5. |
|  | voltage specifies the voltage of each phase of the electric motor in an array. The size of the voltage array must be the same as the number of phase. |
|  | rotor position specifies the mechanical rotor position, in degrees, of the electric motor. |
|  | speed specifies the rotor speed, in revolutions per minute, of the electric motor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dt specifies the time interval, in seconds, at which LabVIEW simulates the electric motor. The value of dt must be greater than 0. |
|  | resistance specifies the resistance, in ohms, of the electric motor. The value of resistance must be greater than 0. |
|  | current returns the phase current of the electric motor in an array. The size of the current array must match the number of phases. |
|  | torque returns the electromagnetic torque, in newton meters, of the electric motor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the SRM Linear Model VI:

- SRM Open Loop Simulation VI: labview\examples\Electric Motor Simulation\SRM\SRM Open Loop Simulation
- SRM Linear Model Closed Loop Control VI: labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Closed Loop Control
- SRM Linear Model Configuration VI: labview\examples\Electric Motor Simulation\SRM\SRM Linear Model Configuration
