# NI DOCUMENT BUNDLE: labview-control-design-and-simulation-module

<!--NI_BUNDLE_CHUNK bundle=labview-control-design-and-simulation-module start=1 end=123 -->
<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_iconstyles.html language=enus -->
## TOPIC 00001: Changing Function Icon Styles (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_iconstyles.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_iconstyles.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Changing Function Icon Styles (Control Design and Simulation Module)

You can change the icon style of a [Simulation](../lvsim/simulation.html) function on the simulation diagram. Right-click a Simulation function and select **Icon Style** from the shortcut menu to display the following options:

- Static —Displays the Simulation function as a standard VI.
- Dynamic —Displays the Simulation function as an object that you can resize. Dynamic icons also display a preview of their contents. For example, a Sine Signal function with a dynamic icon displays a sine wave with the frequency, amplitude, and phase that you configure.
- Text Only —Displays the Simulation function as a list of parameter values.
- Express —Displays the Simulation function with a list of parameters below the icon. You can resize the parameter list to display more inputs and outputs. This icon style also shows parameter values directly on the simulation diagram.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_initvalmesh.html language=enus -->
## TOPIC 00002: Defining Initial Parameter Values and a Mesh (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_initvalmesh.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_initvalmesh.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Defining Initial Parameter Values and a Mesh (Control Design and Simulation Module)

After you define the parameter space using the [minimum and maximum values](sim_c_parmbounds.html) of each parameter, you must specify the initial values of each parameter. These initial parameter values determine where the [Sequential Quadratic Programming](/csh?topicname=lvanlsconcepts/nonlinear_programming.html) (SQP) algorithm begins the search for optimal values. However, if you choose only a single initial set of initial values, the SQP algorithm might return [local optimal values](/csh?topicname=lvanlsconcepts/lvac_local_gloal_minima.html). Local optimal values are values that minimize the cost function within only a subset of parameter space. Local optimal values are not the true solution to the SQP algorithm because the true optimal values might exist outside the parameter space the algorithm searched.

To mitigate this problem, you can execute the SQP algorithm several times, using a different set of initial parameter values each time. If you use a large enough range of initial parameter values within the given parameter space, you can be relatively confident that the SQP algorithm finds the [global optimal values](/csh?topicname=lvanlsconcepts/lvac_local_gloal_minima.html).

You can implement this strategy by defining an initial parameters mesh. The initial parameters mesh defines the distribution pattern of these sets of initial values and the total number of initial value sets to generate. You can choose from four patterns depending on the needs of the problem: **Uniform grid**, **Uniform random**, **Quasirandom**, and **Random walk**.

Each pattern has unique characteristics and strengths. For example, the simplest possible option is the uniform grid, which generates a specified number of equally-spaced locations in the parameter space. However, the uniform random and quasirandom options often provide better coverage of the parameter space while using a fewer number of points than the uniform grid option. The random walk option biases the search to explore close to the initial values but eventually explores a larger region of parameter space. This option is useful if you think a particular parameter space contains the optimal values and you want to focus on a certain region of that space, such as the center.

Use the **Initial Parameters** input of the [SIM Optimal Design](../lvsim/sim_optimal_design_vi.html) VI to specify initial parameter values. Use the **Initial Parameters Mesh** input of this VI to define an initial parameters mesh.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_intro.html language=enus -->
## TOPIC 00003: Control Design and Simulation Module

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_intro.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Control Design and Simulation Module

March 2018, 371894J-01

Simulation is a process that involves using software to recreate and analyze the behavior of dynamic systems. You use the simulation process to lower product development costs by accelerating product development. You also use the simulation process to provide insight into the behavior of dynamic systems you cannot replicate conveniently in the laboratory. For example, simulating a jet engine saves time, labor, and money compared to building, testing, and rebuilding an actual jet engine. You can use the LabVIEW Control Design and Simulation Module to simulate a dynamic system or a component of a dynamic system. For example, you can simulate only the plant while using hardware for the controller, actuators, and sensors.

If you are new to the Control Design and Simulation Module, consider completing the [Getting Started with Simulation](../lvsimhowto/sim_h_gs.html) tutorial.

In addition to the topics contained in this help file, the LabVIEW Control Design User Manual contains information about using LabVIEW to design, analyze, and deploy controllers for dynamic systems.

The following table describes the tasks you can perform with the Control Design and Simulation Module and the components you use for these tasks.

| Task | Component |
| --- | --- |
| Design, analyze, and deploy controllers for dynamic system models | Control Design VIs and functions. |
| Configure simulation parameters, including the ordinary differential equation (ODE) solver, and define the simulation as part of a LabVIEW block diagram | Control & Simulation Loop |
| Build, simulate, and deploy dynamic system models, including models developed with the LabVIEW Advanced Signal Processing Toolkit or the Control Design and Simulation Module. Execute offline, Rapid Control Prototype (RCP), and Hardware-in-the-Loop (HIL) configurations Generate and combine input and feedback signals Collect and display simulation data | Simulation functions |
| Trim and linearize a nonlinear dynamic system model | Trim & Linearize VIs; Linearize Subsystem dialog box |
| Determine the optimal parameters for a dynamic system model, given a set of constraints | Optimal Design VIs |
| Convert your model you developed in The MathWorks, Inc. Simulink® application software into LabVIEW block diagram code | Simulation Model Converter |
| (Windows) Identify large, multivariable models of high-order systems from large amounts of data acquire and preprocess data from a system estimate models analyze, validate, and convert models | (Windows) System Identification VIs |

© 2002–2018 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_ode.html language=enus -->
## TOPIC 00004: Recommendations for Choosing a Solver (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_ode.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_ode.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Recommendations for Choosing a Solver (Control Design and Simulation Module)

Because many [dynamic system models](sim_c_models.html) consist of differential equations, you must [solve these differential equations](/csh?topicname=lvanlsconcepts/solving_odes.html) to observe the behavior of the simulated system. Most simulations you create in the LabVIEW Control Design and Simulation Module use [ordinary differential equation](/csh?topicname=lvanlsconcepts/solving_odes.html) (ODE) solvers. However, you also can choose to implement [differential algebraic equations](/csh?topicname=lvanlsconcepts/solving_daes.html) (DAE) solvers that enable you solve equations that contain an unknown function.

Before you simulate a dynamic system model, you must [specify and configure the solver](../lvsimhowto/sim_h_ode.html) for that simulation. ODE and DAE solvers use methods to approximate the solution to a differential equation. The solvers implement these methods in a variety of ways, each with various strengths and weaknesses. Defining characteristics of a solver include the following qualities:

- Accuracy or order
- Stability
- Computational speed
- Use of a fixed-time step size versus a variable-time step size
- Use of a single step versus multiple steps
- Suitability for stiff problems

#### Recommendations for Choosing an Appropriate Solver

Use the recommendations in the following sections to choose an appropriate solver for a simulation.

##### Models with Unknown Characteristics

If you do not know the expected behavior of a model, choose one of the following [variable step-size](/csh?topicname=lvanlsconcepts/vble_vs_fixed_step_size_ode.html), variable [order](/csh?topicname=lvanlsconcepts/ode_solver_accuracy_and_order.html) solvers:

- BDF
- Adams-Moulton
- Radau [Variable Order]
- Gear's Method

##### Deterministic Execution on a Real-Time Target

Choose a [fixed step-size](/csh?topicname=lvanlsconcepts/vble_vs_fixed_step_size_ode.html) ODE solver for use with a simulation that must [run deterministically in real time](sim_c_deter.html). Fixed step-size solvers run deterministically on RT targets, whereas variable step-size ODE solvers might not because the computational overhead of taking a time step varies over the course of an application.

The [Control & Simulation Loop](../lvsim/sim_simulation_loop.html) provides the following fixed step-size ODE solvers:

- Runge-Kutta 1 (Euler)
- Runge-Kutta 2
- Runge-Kutta 3
- Runge-Kutta 4
- Discrete States Only

##### Models with Discontinuities

If a model encounters many discontinuities—in the form of logic that causes a discontinuity in the ODE states or their derivatives—choose a lower [order](/csh?topicname=lvanlsconcepts/ode_solver_accuracy_and_order.html) solver, such as a solver of first, second, or third order. The following features introduce this type of discontinuity and might make a lower order solver appropriate.

|  | Note This recommendation does not apply to discontinuities introduced by sample data systems in the model. |
| --- | --- |

- Detect Zero Crossing function
- Friction function
- Integrator function, when you use the reset or limit features
- Lookup Table 1D , Lookup Table 2D , or Lookup Table 3D functions whose interpolation method you set as Nearest , Below, or Above
- Quantizer function
- Relay function
- Switch function
- Logic involving integers
- Other logic that causes a discontinuity in the ODE states or their derivatives

If the model does not encounter any discontinuities, choose a higher order solver, such as a solver of fourth order or greater.

##### Solutions That Require Resets

A [single-step ODE solver](/csh?topicname=lvanlsconcepts/single_vs_multi_step_ode.html) might be most efficient for applications that reset the solver often. Initializing a solver requires a certain amount of computation. This computation takes place each time the calculation resets a VI or encounters a discontinuity. Thus, a multi-step ODE solver that requires initialization at each step might be less efficient than a single-step solver.

The [Control & Simulation Loop](../lvsim/sim_simulation_loop.html) provides the following single-step ODE solvers:

- Runge-Kutta 1 (Euler)
- Runge-Kutta 2
- Runge-Kutta 3
- Runge-Kutta 4
- Runge-Kutta 23
- Runge-Kutta 45
- Rosenbrock

##### Stiff Problems

If a model varies in [stiffness](/csh?topicname=lvanlsconcepts/stiff_problems.html) over time, choose an implicit solver. Consider a system that has a broad spectrum of time constants and whose solution contains a component that is high in frequency but quickly dies out relative to the amplitude of the lower frequency waveform. An appropriate solver integrates the system when the high frequency solution is present, and then changes its strategy for the lower frequency solution.

The following implicit solvers start the solution at a low order and gradually move to a higher order when the solution is not stiff or does not experience discontinuities:

- BDF
- Rosenbrock
- SDKIRK 4
- Radau 5
- Radau 9
- Radau 13
- Radau [Variable Order]
- Gear's Method

When a model varies in stiffness, the solver might need to make certain steps with a very small step size. When you [configure the solver](../lvsimhowto/sim_h_ode.html), if you set the **Minimum Step Size (s)** parameter too large, the step might become unstable or, for implicit solvers, the step might lose convergence. If you experience these conditions, try reducing the **Minimum Step Size (s)**. This same logic applies to the **Initial Step Size (s)** parameter.

Variable step-size solvers make as large a step as seems stable for the ODE. If the collected output does not contain the details you want, you can limit the step size with the **Maximum Step Size (s)** parameter.

##### Differential Algebraic Equations

When you use the [Algebraic Variable](../lvsim/cd_alg_var.html), [Implicit State](../lvsim/cd_implicit_state.html), or [Implicit Variable](../lvsim/cd_implicit_variable.html) functions to solve differential algebraic equations, use one of the following solvers for implicit systems:

- BDF
- Radau 5
- Radau 9
- Radau 13
- Radau [Variable Order]
- Gear's Method

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_simloop.html language=enus -->
## TOPIC 00005: Configuring Simulation Parameters (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_simloop.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_simloop.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Configuring Simulation Parameters (Control Design and Simulation Module)

The [Control & Simulation Loop](../lvsim/sim_simulation_loop.html), shown in the following block diagram, contains the parameters that define the behavior of the simulation.

[IMAGE alt='image' src='simulation_loop.gif']

You can configure these simulation parameters by using the following two methods:

- Using the Configure Simulation Parameters dialog box
- Wiring values to the Input Node. Expand the Input Node to display the same parameters you can configure from the Configure Simulation Parameters dialog box.

You also can use a combination of these two methods in the same simulation diagram. However, values that you programmatically configure override any equivalent settings that you make in the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box.

|  | Tip Use the Output Node to view any errors that occur during the execution of the Control & Simulation Loop. Use the Simulation Parameters function to display the parameters you configure for the simulation. |
| --- | --- |

The Control & Simulation Loop is a version of the [Timed Loop](/csh?topicname=glang/timed_loop.html). Both loops can iterate deterministically according to a period and priority you define. However, the Control & Simulation Loop also executes the simulation diagram according to the [ordinary differential equation (ODE) solver](../lvsimconcepts/sim_c_ode.html) you choose. The inside of the Control & Simulation Loop also has a pale yellow background to distinguish the simulation diagram from the LabVIEW block diagram. Similar to other loops and structures, you can use tunnels to pass data in and out of the Control & Simulation Loop.

#### Configuring Simulation Parameters Programmatically

The following block diagram shows how you configure a simulation diagram programmatically.

[IMAGE alt='image' src='loc_bd_programmatic_loop_configure.gif']

The previous block diagram shows how the gray boxes on the Input Node display any values that you configure in the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box. Values that you configure programmatically do not have gray boxes.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_subsys.html language=enus -->
## TOPIC 00006: Types of Simulation Subsystems (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_subsys.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_subsys.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Types of Simulation Subsystems (Control Design and Simulation Module)

Simulation subsystems provide a way to modularize simulation diagram code. By combining several functions into a subsystem, you reduce the amount of space needed on the simulation diagram, making the simulation easier to navigate visually. Simulation subsystems also are useful for validating, distributing, and reusing portions of the simulation diagram.

You can use many [Simulation](../lvsim/simulation.html) VIs and functions only on a simulation diagram, such as within a [Control & Simulation Loop](../lvsim/sim_simulation_loop.html). Because simulation subsystems modularize simulation diagram code, you can use the Simulation VIs and functions in simulation subsystems as well. The entire block diagram of a simulation subsystem is pale yellow like the inside of a Control & Simulation Loop. When you use Simulation VIs and functions in a simulation subsystem, you place the VIs and functions directly on the subsystem block diagram rather than within a Control & Simulation Loop.

|  | Note You cannot use local variables in a simulation subsystem. |
| --- | --- |

You can run simulation subsystems as [stand-alone VIs](#running_a_subsystem_as_a_stand-alone_vi), [within a Control & Simulation Loop or another simulation subsystem](#running_a_subsystem_in_a_simulation_loop), or [on a block diagram outside a Control & Simulation Loop](#running_a_subsystem_outside_a_simulation_loop).

#### Running a Subsystem as a Stand-Alone VI

When you run a simulation subsystem as a stand-alone VI, you configure the simulation parameters by selecting **Operate»Configure Simulation Parameters** to launch the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box. You also can configure the execution and appearance of the subsystem by selecting **File»VI Properties**.

When running a simulation subsystem as a stand-alone VI, you can use standard LabVIEW [debugging](/csh?topicname=lvconcepts/debug_techniques.html) techniques, such as [execution highlighting](/csh?topicname=lvhowto/execution_highlighting.html), [breakpoints](/csh?topicname=lvhowto/breakpoints.html), [probes](/csh?topicname=lvhowto/using_the_probe_tool.html), and [single-stepping](/csh?topicname=lvhowto/single_step_mode.html). You cannot use these techniques on a subsystem that is within another Control & Simulation Loop. You also cannot step into the subsystem. However, you can set a breakpoint on the entire subsystem by right-clicking the subsystem and selecting **Breakpoint»Set Breakpoint** from the shortcut menu. You also can use a probe or a custom probe to monitor the subsystem output.

The following image shows the simulation diagram of a simulation subsystem Newton.vi, which obtains the position of a mass by using Newton's Second Law of Motion.

[IMAGE alt='image' src='loc_bd_newton.gif']

In the previous simulation diagram, this subsystem has front panel controls and indicators, so you can run this subsystem by clicking the **Run** button. Because Newton.vi does not have a Control & Simulation Loop, you configure the parameters of this subsystem by selecting **Operate»Configure Simulation Parameters**.

#### Running a Subsystem in a Control & Simulation Loop

If you run a simulation subsystem inside a Control & Simulation Loop, the simulation subsystem inherits the parameters from the Control & Simulation Loop.

The following image shows Newton.vi included within the Control & Simulation Loop of another simulation diagram.

[IMAGE alt='image' src='loc_bd_spring_mass_damper.gif']

In the previous image, the parameters of the Control & Simulation Loop override any parameters you configured specifically for Newton.vi.

|  | Note You create this subsystem and this VI in the Getting Started with Simulation tutorial. |
| --- | --- |

#### Running a Subsystem Outside a Control & Simulation Loop

If you run a simulation subsystem on a block diagram outside a Control & Simulation Loop, the simulation subsystem executes one step of the [ordinary differential equation](sim_c_ode.html) (ODE) solver each time the simulation subsystem is called. For example, if you place the simulation subsystem in a [Timed Loop](/csh?topicname=glang/timed_loop.html), one step of the ODE solver executes at each iteration of the loop. You can use only fixed step-size ODE solvers for a simulation subsystem outside a Control & Simulation Loop. Specify the time step using the **Step Size (s)** configuration option of the subsystem.

|  | Tip If you create an application with a simulation subsystem inside a Timed Loop and then deploy the application to a real-time target, set the Step Size (s) of the subsystem equal to the period of the Timed Loop. |
| --- | --- |

When you place a simulation subsystem on a block diagram outside a Control & Simulation Loop, the icon of the simulation subsystem appears in the **Express** [style](sim_c_iconstyles.html) by default. You can wire values to the parameters of the simulation subsystem to configure the simulation subsystem programmatically.

|  | Note The Static and Dynamic icon styles are disabled for subsystems outside a Control & Simulation Loop. |
| --- | --- |

You also can configure the parameters of the simulation subsystem interactively. Double-click the simulation subsystem to launch the configuration dialog box of that simulation subsystem. In this configuration dialog box, you can configure the specific parameters of the simulation subsystem as well as the following general simulation parameters:

- Initial Time (s) —Specifies the time at which to start the ODE solver.
- ODE Solver —Specifies the type of ODE solver the simulation uses.
- Nan/Inf Check —Specifies that you want the Control Design and Simulation Module to check the simulation values for not a number (NaN) and infinite (Inf) values. The Control Design and Simulation Module returns an error if it encounters a NaN or Inf value.
- Step Size (s) —Specifies the interval, in seconds, between the times at which the ODE solver evaluates the model and updates the model output.
- Discrete Step Size (s) —Specifies the base time step size, in seconds, for the simulation.
- Auto Discrete Time —Automatically calculates the Discrete Step Size (s) .

These parameters are identical to parameters you can configure in the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box of a Control & Simulation Loop. In the configuration dialog box of a simulation subsystem, these parameters appear as sub-items of the **Simulation Parameters** item in the **Parameters** tree. If the simulation subsystem already contains a parameter with the same name as one of the general simulation parameters listed above, LabVIEW appends the general simulation parameter name with an underscore.

The following image shows Newton.vi on a block diagram outside a Control & Simulation Loop.

[IMAGE alt='image' src='loc_bd_newton_outside_loop.gif']

In the previous image, the Timed Loop determines when Newton.vi executes the next step of the ODE solver. Because Newton.vi is outside a Control & Simulation Loop, you can configure the simulation parameters, including the ODE solver to use, by double-clicking the simulation subsystem.

If you run a simulation subsystem outside a Control & Simulation Loop, you can reinitialize the simulation subsystem by setting the **Initialize** input of the simulation subsystem to TRUE. This input restarts the ODE solver from the specified **Initial Time (s)**. The **Initialize** input is available for a simulation subsystem only when the subsystem is not inside a Control & Simulation Loop or another simulation subsystem.

#### Enabled and Triggered Subsystems

Enabled and triggered subsystems execute only when certain conditions are met. An enabled subsystem executes when a Boolean input to the subsystem receives a TRUE value. This input enables the subsystem. A triggered subsystem executes when an input signal to the subsystem crosses 0 or an offset from 0 that you specify. You can configure the subsystem to wait for the trigger signal to cross 0 on a rising slope, a falling slope, or either. The same subsystem can be both enabled and triggered.

You also can configure the behavior of specific outputs of an enabled or triggered subsystem by specifying the values those outputs return when the subsystem does not execute. This prevents a disabled subsystem from breaking the execution of the rest of the simulation diagram or VI.

To configure enabling or triggering for a subsystem, double-click the subsystem to display the [Subsystem Configuration](../lvsim/subsys_config_db.html) dialog box. Select **Execution Control** from the **Parameters** list and use the options under **Parameter Information** to configure the basic execution behavior of the subsystem. Select individual outputs from the **Parameters** list to configure the behavior of those outputs when the subsystem does not execute.

#### Polymorphic Subsystems

If you create one or more subsystems that perform the same operation on different data types, you can package those subsystems together to create a polymorphic subsystem. A polymorphic subsystem is a [single VI](/csh?topicname=lvconcepts/polymorphic_vis.html) that points to one or more subsystems, called instances. Each instance accepts a different data type for a single input or output terminal. LabVIEW automatically selects the correct instance based on the input data type.

For example, one subsystem could operate on a double-precision floating point number, while another subsystem performs the same operation on a 16-bit integer. Instead of placing both subsystems on the simulation diagram, you can [create a polymorphic subsystem](../lvsimhowto/sim_h_subsyssa.html#poly) that automatically chooses the correct instance.

For a polymorphic subsystem to work, each instance of the polymorphic subsystem must be a simulation subsystem. You cannot create a polymorphic subsystem with both VIs and subsystems as instances. Also, each subsystem must have an identical [connector pane pattern](/csh?topicname=lvhowto/selecting_a_connector_pane.html). Additionally, the names of corresponding input parameters for each instance must be identical.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_subsystop.html language=enus -->
## TOPIC 00007: Modularizing the Simulation Diagram (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_subsystop.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_subsystop.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Modularizing the Simulation Diagram (Control Design and Simulation Module)

The LabVIEW Control Design and Simulation Module supports [simulation subsystems](sim_c_subsys.html), which you use to modularize and encapsulate portions of the simulation diagram. You [create simulation subsystems](../lvsimhowto/sim_h_subsyssa.html) similarly to creating subVIs.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_translator.html language=enus -->
## TOPIC 00008: Using the Simulation Model Converter (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_translator.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_translator.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Using the Simulation Model Converter (Control Design and Simulation Module)

You can use the Simulation Model Converter to convert your model (.mdl or .slx) file, developed in The MathWorks, Inc. Simulink[®](sim_trademarks.html) simulation environment, into a LabVIEW VI that consists of a simulation diagram containing LabVIEW functions, wires, and simulation subsystems corresponding to the contents of your model file. As part of the conversion process, the Simulation Model Converter uses The MathWorks, Inc. MATLAB[®](sim_trademarks.html) application software and the Simulink application software to compile your model file and execute any of your .m files that you specify in the dialog box. If the MATLAB software or the Simulink software is not installed on the same computer as the LabVIEW Control Design and Simulation Module, the results of the conversion might be less accurate.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_transwarn.html language=enus -->
## TOPIC 00009: Caveats and Recommendations when using the Simulation Model Converter (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_transwarn.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_transwarn.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Caveats and Recommendations when using the Simulation Model Converter (Control Design and Simulation Module)

If the Simulation Model Converter cannot find a value for a parameter in your model (.mdl or .slx) file it is converting, LabVIEW displays a warning. In these cases, the Simulation Model Converter uses the default value of the parameter in the corresponding LabVIEW function.

|  | Note In some cases, the Simulation Model Converter cannot find a value for a parameter because the parameter contains an expression instead of a constant value. If you have a licensed copy of The MathWorks, Inc. MATLAB® software version 5.0 or later installed on your computer, the Simulation Model Converter attempts to evaluate the MATLAB software expressions in your model file prior to converting the file. If the Simulation Model Converter successfully evaluates the expression, the Simulation Model Converter uses the result of that evaluation as the parameter value and does not produce a warning. |
| --- | --- |

The Simulation Model Converter cannot fully convert all functions of every model to LabVIEW block diagram code. If the Simulation Model Converter encounters a [block it cannot convert](../lvsimconcepts/sim_c_ublocks.html), you receive a warning. In these cases, the Simulation Model Converter creates a placeholder [simulation subsystem](../lvsimconcepts/sim_c_subsys.html) in LabVIEW. You must [create a simulation subsystem](../lvsimhowto/sim_h_subsyssa.html) using a LabVIEW VI to accomplish the same functionality as the block to replace this placeholder simulation subsystem in LabVIEW.

Because LabVIEW is strict about data types, the converted simulation subsystem might have broken wires. In this case, add block diagram code to convert between converted data types.

#### Converting Stateflow[®](sim_trademarks.html) Diagrams with the Simulation Model Converter

You can use the [Simulation Model Converter](../lvsim/sim_simtrans.html) to convert statecharts developed with The MathWorks, Inc. Stateflow[®](sim_trademarks.html) application software into statecharts usable within the LabVIEW Statechart Module. This topic describes the differences between the Stateflow[®](sim_trademarks.html) statechart code and the converted code in the LabVIEW Statechart Module.

|  | Note To convert statecharts developed with The MathWorks, Inc. Stateflow® application software to statecharts usable within the LabVIEW Statechart Module, you must install the LabVIEW Statechart Module. You can visit the NI website for more information about the LabVIEW Statechart Module. |
| --- | --- |

##### Unsupported Stateflow[®](sim_trademarks.html) Features

The following Stateflow[®](sim_trademarks.html) features are unsupported in the LabVIEW Statechart Module.

- Super-step semantics
- Initial transitions to a junction
- Temporal logic
- Output events
- Bus signals
- Guards on a default transition

The Simulation Model Converter converts any Stateflow[®](sim_trademarks.html) diagram regardless of whether or not it contains unsupported features. If your model includes any of these features, the Simulation Model Converter displays a warning after completing the conversion. You can edit the converted code using the LabVIEW Statechart Module.

##### Graphical Differences

The following graphical differences exist between the Stateflow[®](sim_trademarks.html) diagram code and the converted code in the LabVIEW Statechart Module.

###### Regions

In a Stateflow[®](sim_trademarks.html) diagram, [states](/csh?topicname=lvsc/sc_state.html) can exist within other states. In the LabVIEW Statechart Module, states only can exist within a [region](/csh?topicname=lvsc/sc_region.html) to create hierarchical states. The following image shows using a region within a state to create hierarchical states.

[IMAGE alt='image' src='region.gif']

###### Transition Nodes

A Stateflow[®](sim_trademarks.html) diagram represents transitions between states as splines with labels containing code that defines the behavior of the transition. The LabVIEW Statechart Module represents transitions as wires with [transition nodes](/csh?topicname=lvscconcepts/sc_c_trans.html) that contain the same information as the Stateflow[®](sim_trademarks.html) label. You use these transition nodes to [define the trigger(s), guard, and action of the transition](/csh?topicname=lvschowto/sc_h_configt.html).

[IMAGE alt='image' src='transitions.gif']

###### State Names

In a Stateflow[®](sim_trademarks.html) diagram, states have labels that contain information about the behavior of the state. When you convert a Stateflow[®](sim_trademarks.html) diagram using the Simulation Model Converter, LabVIEW converts the information from the label in Stateflow[®](sim_trademarks.html) into [guards](/csh?topicname=lvscconcepts/sc_c_tga.html) and [actions](/csh?topicname=lvscconcepts/sc_c_tga.html).

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_trimlin.html language=enus -->
## TOPIC 00010: Trimming and Linearizing Nonlinear Models (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_trimlin.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_trimlin.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Trimming and Linearizing Nonlinear Models (Control Design and Simulation Module)

Many real-world [dynamic system models](sim_c_models.html) are [nonlinear](../lvsimconcepts/sim_c_models.html#linear_versus_nonlinear_models). If you want to design a controller for a nonlinear model, you must first linearize that model. Linearizing a nonlinear model involves approximating the behavior of that model around an operating point. The operating point is the set of the inputs and states of the model. When you linearize a model, the result is a [linear](../lvsimconcepts/sim_c_models.html#linear_versus_nonlinear_models) [time-invariant](../lvsimconcepts/sim_c_models.html#time-variant_versus_time-invariant_models) (LTI) [state-space](../lvsimconcepts/sim_c_models.html#linear_model_forms) model.

|  | Note You can design a controller for LTI models using the Control Design VIs and functions. |
| --- | --- |

Trimming a model involves searching for values of model inputs and states that satisfy any conditions you specify. For example, you can specify that the model outputs or state derivatives must have a certain value. Trimming the model using these conditions returns the values of the inputs and states that, when given to the model, produce the outputs and state derivatives you specified. You also can trim a model to determine an operating point about which you linearize the model.

The LabVIEW Control Design and Simulation Module provides several methods for trimming and linearizing models. You can [interactively trim and linearize a model](../lvsimhowto/sim_h_itl.html). You also can [programmatically trim](../lvsimhowto/sim_h_trimprog.html) and [programmatically linearize](../lvsimhowto/sim_h_linprog.html) a model.

|  | Note The above methods operate on continuous simulation subsystems. Therefore, you must create a simulation subsystem that represents the model before trimming or linearizing that model. |
| --- | --- |

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_c_ublocks.html language=enus -->
## TOPIC 00011: Unsupported Blocks (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_c_ublocks.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_c_ublocks.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Unsupported Blocks (Control Design and Simulation Module)

The [Simulation Model Converter](../lvsim/sim_simtrans.html) dialog box cannot convert the following blocks used in The MathWorks, Inc. Simulink[®](sim_trademarks.html) application software. In these cases, the Simulation Model Converter creates a placeholder [simulation subsystem](../lvsimconcepts/sim_c_subsys.html) in LabVIEW. You must [create a simulation subsystem](../lvsimhowto/sim_h_subsyssa.html) using a LabVIEW VI to accomplish the same functionality as the block to replace this placeholder simulation subsystem in LabVIEW. In the **Simulation Model Converter** dialog box, place a checkmark in the **Show Errors** checkbox to display information about any warnings or errors the Simulation Model Converter encountered during the conversion.

|  | Note With the exception of the list below and all blocks in the Additional Math and Discrete Library, the Simulation Model Converter supports all blocks in the Simulink® application software Base package. |
| --- | --- |

- Action Port
- Assertion
- Band-Limited White Noise
- Block Support Table
- Bus Assignment
- Bus to Vector
- Check Discrete Gradient
- Check Dynamic Gap
- Check Dynamic Lower Bound
- Check Dynamic Range
- Check Dynamic Upper Bound
- Check Input Resolution
- Check Static Gap
- Check Static Lower Bound
- Check Static Range
- Check Static Upper Bound
- Configurable Subsystem
- Data Type Conversion Inherited
- Data Type Duplicate
- Data Type Propagation
- Data Type Scaling Strip
- DocBlock
- Embedded MATLAB Function
- Environment Controller
- Extract Bits
- For Iterator Subsystem
- From Workspace
- Function-Call Generator
- Function-Call Subsystem
- If
- If Action Subsystem
- Interval Test
- Interval Test Dynamic
- Level-2 M-File S-Function
- Lookup Table (n-D)
- Merge
- Model
- Model Info
- Permute Dimensions
- Rate Transition
- S-Function
- S-Function Builder
- Shift Arithmetic
- Signal Builder
- Signal Conversion
- Squeeze
- Switch Case
- Switch Case Action Subsystem
- Time-Based Linearization
- To Workspace
- Trigger-Based Linearization
- Variable Time Delay
- Weighted Moving Average
- While Iterator Subsystem

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_emi_order.html language=enus -->
## TOPIC 00012: Execution Order of Callbacks Functions (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_emi_order.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_emi_order.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Execution Order of Callbacks Functions (Control Design and Simulation Module)

The shared library corresponding to an [external, or third-party, model](../lvsimconcepts/sim_using_emi.html) must export [Callbacks](../lvsimemi/emi_callbacks.html) functions as appropriate for the structure of the model. The LabVIEW Control Design and Simulation Module executes the Callbacks functions in the following order:

[IMAGE alt='image' src='loc_eps_emi_adv_callback_flow.gif']

* The Control Design and Simulation Module executes the [EMI_CB_CalculateDiscreteStates](../lvsimemi/emi_emi_cb_calculatediscretestates.html) function only on discrete time steps. Use the [EMI_SetDiscretePeriod](../lvsimemi/emi_emi_setdiscreteperiod.html) and the [EMI_SetDiscreteSkew](../lvsimemi/emi_emi_setdiscreteskew.html) functions to determine the discrete time steps.

In the previous illustration, the functions shaded in gray are functions you might export if you want to detect [zero crossings](../lvsimconcepts/sim_zero_crossings.html). Export the [EMI_CB_CalculateZeroCrossingSignals](../lvsimemi/emi_emi_cb_calculatezerocrossingsignals.html) and the [EMI_CB_CalculateResetStates](../lvsimemi/emi_emi_cb_calculateresetstates.html) functions if you use the internal zero-crossing detection system of the Control Design and Simulation Module. Export the [EMI_CB_CheckStepAcceptance](../lvsimemi/emi_emi_cb_checkstepacceptance.html) and the EMI_CB_CalculateResetStates functions if you implement a custom algorithm for detecting zero crossings.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_esi_solvers.html language=enus -->
## TOPIC 00013: Execution Order of Callback API Functions (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_esi_solvers.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_esi_solvers.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Execution Order of Callback API Functions (Control Design and Simulation Module)

In many other software applications, when you create an ordinary differential equation (ODE) solver, you define the right-hand-sides function of the ODE and then pass a pointer to that function through to the solver. The solver contains an internal loop that calls the right-hand-sides function as many times as necessary to advance the simulation.

In the LabVIEW Control Design and Simulation Module, you [create an external ODE solver](../lvsimhowto/sim_esi_create.html) in C/C++, and the solver provides a set of [Callback API](../lvsimesi/esi_callback_api.html) functions to LabVIEW. The solver must export all [Callback API](../lvsimesi/esi_callback_api.html) functions. The Control Design and Simulation Module calls these functions in a predefined sequence. When necessary, the Control Design and Simulation Module evaluates the right-hand-sides function of the ODE.

The order in which the Control Design and Simulation Module executes the Callback API functions depends on whether the solver has a variable or fixed step size.

#### Variable Step-Size Solvers

A variable step-size solver evaluates whether each major step satisfies the relative tolerance and absolute tolerance values and proposes the next step size after each major step.

The following flowchart illustrates the execution order of a variable step-size ODE solver.

[IMAGE alt='image' src='loc_eps_variable_stepsize_execution.gif']

The n-vector function *f(x,u,t)* is the right-hand-sides function of the ODE. *x* is the states and is an n-dimensional vector, *u* is the input to the model and is m-dimensional, and *t* is time. The ellipses represent evaluations of the right-hand-sides function, the rectangles represent Callback API functions in the ODE solver, and the diamond represents a decision point within the execution order.

The Control Design and Simulation Module first sets the states of the solver to the initial values you specify and evaluates the right-hand-sides function of the ODE at the initial time, initial state values, and initial input values. The Control Design and Simulation Module mandates the step size, and the solver can request the step size any time from initialization onward. The Control Design and Simulation Module then calls the [Initialize](../lvsimesi/esi_initialize.html) function to perform any tasks required before the simulation starts.

After the Control Design and Simulation Module calls the Initialize function of the external solver, the [UpdateStates](../lvsimesi/esi_updatestates.html) function provides the first state update for the state values of the model. The UpdateStates function specifies the state and time values at which the Control Design and Simulation Module evaluates the right-hand-sides function of the ODE. The [SetIsMajorStep](../lvsimesi/esi_sim_solversetismajorstep.html) function within the UpdateStates function specifies whether the next step is a minor or a major step.

The Control Design and Simulation Module must consider several competing factors when it calculates the time for the next simulation step. The simulation might contain [Discrete Linear Systems](../lvsim/discrete_systems.html) functions that require a step at a particular fixed rate. The simulation also might contain a [Detect Zero Crossing](../lvsim/sim_zerocrossdetect.html) function that requires a step just before and just after a signal crosses a particular threshold. The simulation might contain other functions, such as [Signal Generation](../lvsim/signal_generation.html) functions, that require a step just before and just after a particular time. Each of these competing factors and the ODE solver nominate a step size. The Control Design and Simulation Module then takes the smallest nominated step size.

After a major step, the Control Design and Simulation Module evaluates the state derivatives at the current state and time values and then calls the [EvaluateError](../lvsimesi/esi_evaluateerror.html) function. The [EvaluateError](../lvsimesi/esi_evaluateerror.html) function evaluates whether the current major step satisfies the relative and absolute error tolerance values for the ODE solver.

If the step satisfies the tolerance values and a discontinuity in a continuous signal occurs, the Control Design and Simulation Module calls the [Restart](../lvsimesi/esi_restart.html) function. This function restarts the ODE solver after the discontinuity.

When the Control Design and Simulation Module determines that the simulation has reached the final time, the Control Design and Simulation Module calls the [Finalize](../lvsimesi/esi_finalize.html) function. During the execution of this function, the solver can perform any finalization tasks such as releasing any memory allocated with the [Initialize](../lvsimesi/esi_initialize.html) function.

|  | Note The Information function specifies a name for the solver. The Control Design and Simulation Module calls this function only when you launch the Configure Simulation Parameters dialog box. |
| --- | --- |

#### Fixed Step-Size Solvers

Fixed step-size solvers proceed as a series of frames. Each frame consists of a fixed number of minor steps followed by a major step. The following flowchart illustrates the execution order of each step for a fixed step-size solver.

[IMAGE alt='image' src='loc_eps_fixed_stepsize_execution.gif']

The n-vector function *f(x,u,t)* is the right-hand-sides function of the ODE. *x* is the states and is an n-dimensional vector, *u* is the input to the model and is m-dimensional, and *t* is time. The ellipses represent evaluations of the right-hand-sides function, the rectangles represent Callback API functions in the ODE solver, and the diamond represents a decision point within the execution order.

After the Control Design and Simulation Module calls the Initialize function of the external solver, the [UpdateStates](../lvsimesi/esi_updatestates.html) function provides the first state update for the state values of the model. The UpdateStates function specifies the state and time values at which the Control Design and Simulation Module evaluates the right-hand-sides function of the ODE. The [SetIsMajorStep](../lvsimesi/esi_sim_solversetismajorstep.html) function within the UpdateStates function specifies whether the next step is a minor or a major step.

When the Control Design and Simulation Module determines that the simulation has reached the final time, the Control Design and Simulation Module calls the [Finalize](../lvsimesi/esi_finalize.html) function. During the execution of this function, the solver can perform any finalization tasks such as releasing any memory allocated with the [Initialize](../lvsimesi/esi_initialize.html) function.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_glossary.html language=enus -->
## TOPIC 00014: Glossary (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_glossary.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_glossary.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Glossary (Control Design and Simulation Module)

ABCDEFHILMNOPRST

[LabVIEW Glossary](/csh?topicname=lvconcepts/glossary.html)

| A |  |
| --- | --- |
| Ackermann | A technique for placing poles in a system model. Use the CD Ackermann VI to implement this technique. |
| actuator | A physical device that applies the control action to the plant. |
| auto-covariance | A measure of how closely a value of a stochastic process, such as noise, varies with the subsequent value of that process. |
| B |  |
| balanced system model | A system model with identical controllability and observability diagonal Grammians. Use the CD Balance State-Space Model (Diagonal) VI and the CD Balance State-Space Model (Grammians) VI to balance a state-space system model. |
| Bode plot | A plot that shows the gain and phase margins of a system model for a common frequency range. Bode plots show how close a system model is to instability. Use the CD Bode VI to create a Bode plot for a system model. |
| C |  |
| CGD | Common Graph Description. The format the Simulation Model Converter uses to store each system, subsystem, block, and line from your model you developed in The MathWorks, Inc. Simulink® simulation environment. |
| constraints | See inequality constraints. |
| continuous model | A dynamic system model that represents real-world signals, which vary continuously with time. You characterize a continuous model by differential equations. See also discrete model. |
| Control & Simulation Loop | The structure that executes the simulation diagram over multiple time steps. |
| controller | A device that regulates the operation of a dynamic system. |
| cost | The scalar value that results from solving a cost function. |
| cost function | A performance measure you want to minimize when designing optimal parameters. A cost function is a functional equation that maps a set of points in a time series to a single scalar value. |
| D |  |
| design | See optimal design. |
| direct feedthrough | A relationship between a function input and a function output in which the function uses the input at the current step to calculate the output at the current step. See also indirect feedthrough. |
| discrete model | A dynamic system model that represents signals that are sampled at discontinuous intervals in time. You characterize a discrete model by difference equations. See also continuous model. |
| distributed parameter model | A physical model that you can describe with partial differential equations. See also lumped parameter model. |
| dynamic system | A system whose behavior varies with time. |
| dynamic system model | A differential or difference equation that represents the behavior of all or part of a dynamic system. |
| E |  |
| empirical modeling | A modeling technique in which you use experimental data to define a dynamic system model. See also physical modeling. |
| F |  |
| feedback cycle | A cycle in which data flow originates from an output of a function or subsystem and terminates as an input of the same function or subsystem. See also indirect feedthrough. |
| H |  |
| HIL | Hardware-in-the-loop. A simulation configuration in which you test a controller implementation with a simulated system. See also RCP. |
| I |  |
| indirect feedthrough | A relationship between a function input and a function output in which the function does not use the input at the current step to compute the output at the current step. See also direct feedthrough. |
| inequality constraints | Any restrictions you place on how the optimal design process determines optimal parameter values. You can define inequality constraints for the control action, the output, the rate of change of the control action, and the rate of change of the output. |
| Input Node | A collection of input terminals attached to the Control & Simulation Loop. Use the Input Node to configure simulation parameters programmatically. See also Output Node. |
| L |  |
| linear model | A dynamic system model that obeys the principles of superposition and homogeneity. See also nonlinear model. |
| linearize | A procedure that approximates the behavior of a nonlinear model. See also trim. |
| lumped parameter model | A physical model you can describe with an ordinary differential equation. See also distributed parameter model. |
| M |  |
| model | See dynamic system model. |
| N |  |
| nonlinear model | A dynamic system model that does not obey the principles of superposition or homogeneity. See also linear model. |
| O |  |
| offline | A simulation configuration in which you use software to simulate the controller and the system you want to control. No hardware is involved in an offline simulation. |
| optimal design | The process of selecting parameter values that maximize a measure of performance. |
| Output Node | An output terminal on the Control & Simulation Loop. Use the Output Node to view any errors the simulation diagram generates. See also Input Node. |
| P |  |
| parameter bounds | Any restrictions you place on possible parameter values during the optimal design process. The optimal design process does not consider any parameter values outside the bounds you define. |
| parameter design | See optimal design. |
| parameter mesh | A set of points that defines the distribution patterns of sets of parameter values and the number of sets to generate. |
| period | The amount of time in which a discrete linear Simulation function must complete. |
| physical modeling | A modeling technique in which you use the laws of physics to define a dynamic system model. See also empirical modeling. |
| plant | A dynamic system whose behavior you want to observe, replicate, or manipulate. |
| R |  |
| RCP | Rapid control prototype. A simulation configuration in which you test plant hardware with a software model of the controller. See also HIL. |
| S |  |
| simulation diagram | A LabVIEW diagram that allows you to use Simulation functions within a Control & Simulation Loop or simulation subsystem. A simulation diagram, like other LabVIEW diagrams, has the following semantic properties: The order of operations is not completely specified by the user. The order of operations is implied by data interdependencies. A function can execute only after all necessary inputs have become available. Outputs are generated after a function completes execution. |
| skew | The amount of time by which you want to delay the execution of a discrete linear Simulation function. |
| SQP | Sequential Quadratic Programming. A general-purpose numerical optimization algorithm. |
| subsystem | A section of a simulation diagram you represent with a single icon instead of multiple Simulation functions and wires. |
| T |  |
| time-invariant model | A dynamic system model whose parameters do not change with time. |
| time-variant model | A dynamic system model whose parameters change with time. |
| trim | A procedure that searches for the values of states and inputs that produce output and/or state derivative conditions you specify. See also linearize. |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_howto.html language=enus -->
## TOPIC 00015: How-To

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_howto.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_howto.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### How-To

This book contains step-by-step instructions and other information that might be useful as you use the LabVIEW Control Design and Simulation Module. Refer to the [Concepts](sim_concepts.html) book to learn about related concepts.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_imptinfo.html language=enus -->
## TOPIC 00016: Additional Important Information (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_imptinfo.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_imptinfo.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Additional Important Information (Control Design and Simulation Module)

[Trademarks](sim_trademarks.html)

[Patents](sim_patents.html)

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_partial_support.html language=enus -->
## TOPIC 00017: Partially Supported Blocks (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_partial_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_partial_support.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Partially Supported Blocks (Control Design and Simulation Module)

The [Simulation Model Converter](../lvsimconcepts/sim_c_translator.html) provides limited support for the following blocks used in The MathWorks, Inc. Simulink[®](sim_trademarks.html) application software. If the Simulation Model Converter does not convert a block properly, you must [create a simulation subsystem](../lvsimhowto/sim_h_subsyssa.html) in LabVIEW to accomplish the same functionality as the block to replace the placeholder simulation subsystem that the Simulation Model Converter creates. In the [Simulation Model Converter](../lvsim/sim_simtrans.html) dialog box, place a checkmark in the **Show Errors** checkbox to display information about any warnings or errors the Simulation Model Converter encountered during the conversion.

| Simulink Block | Limitation |
| --- | --- |
| Data Type Conversion | When you use the Simulation Model Converter to convert a Data Type Conversion block that converts negative numbers to numeric values with an unsigned data type, the results vary from those that the Simulink application software returns. The Control Design and Simulation Module saturates the numeric values by clipping the negative values to zero. The Simulink application software wraps the numeric value by reinterpreting the negative number as an unsigned number, which creates a large positive number. |
| Direct Lookup Table (n-D) | The Simulation Model Converter can convert a Direct Lookup Table (n-D) block only for tables of up to 10 dimensions.. |
| Discrete Derivative | The Simulation Model Converter cannot convert this block if the block has gains or initial conditions. |
| Discrete FIR Filter | The Simulation Model Converter can convert a Discrete FIR Filter block only if it uses scalar quantities. |
| Floating Scope | The Simulation Model Converter treats floating scopes as regular scopes when converting this block. You must wire floating scopes manually in the Control Design and Simulation Module. |
| From | When you use the converted subsystem corresponding to this block, race conditions might occur. |
| Gain | The Simulation Model Converter cannot convert this block if this block performs matrix multiplication. |
| Goto | When you use the converted subsystem corresponding to this block, race conditions might occur. |
| Integer Delay | The Simulation Model Converter cannot convert Integer Delay blocks that use initial conditions. |
| Matrix Concatenate | The Simulation Model Converter can convert this block when the block concatenates 2D matrices along rows, columns, or a third dimension. |
| Probe | LabVIEW does not support framed signals. The framed signal output of the converted subsystem corresponding to this block is always zero. |
| Pulse Generator | The Simulation Model Converter cannot convert this block if it uses sample-based or external clock settings. |
| Reshape | The Simulation Model Converter cannot convert Reshape blocks that have signals with more than two dimensions. |
| Transfer Fcn First Order | The Simulation Model Converter cannot convert Transfer Fcn First Order blocks that use initial conditions, rounding, or saturation. |
| Transfer Fcn Lead or Lag | The Simulation Model Converter cannot convert Transfer Fcn Lead or Lag blocks that use initial conditions, rounding, or saturation. |
| Transfer Fcn Real Zero | The Simulation Model Converter cannot convert Transfer Fcn Real Zero blocks that use initial conditions, rounding, or saturation. |
| Scope | When you use the Simulation Model Converter to convert a Scope block with multiple inputs, the results vary from those that the Simulink application software returns. The Control Design and Simulation Module plots multiple inputs on one graph. The Simulink application software plots multiple inputs on separate graphs. |
| Sine Wave | The Simulation Model Converter cannot convert Sine Wave blocks that have sample-based or external clock settings. |
| Step | The Simulation Model Converter cannot convert Step blocks that use a user-specified sample time. |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_patents.html language=enus -->
## TOPIC 00018: Patents

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_patents.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_patents.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Patents

For patents covering the NI products/technology, refer to the appropriate location: **Help»Patents** in your software, the patents.txt file on your media, or the National Instruments Patent Notice at ni.com/patents.

You are only permitted to use this product in accordance with the accompanying license agreement. All rights not expressly granted to you in the license agreement accompanying the product are reserved to NI. Further, and without limiting the forgoing, no license or any right of any kind (whether by express license, implied license, the doctrine of exhaustion or otherwise) is granted under any NI patents.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_related_documentation.html language=enus -->
## TOPIC 00019: Related Documentation (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_related_documentation.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Control Design and Simulation Module)

You must have Adobe Reader installed to view PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to ni.com/manuals for updated documentation resources.

The following resources contain information that you might find helpful as you use the LabVIEW Control Design and Simulation Module.

- ni.com/gettingstarted—This website provides information about getting started with LabVIEW.
- LabVIEW Control Design User Manual—This manual contains information about using LabVIEW to design, analyze, and deploy controllers for dynamic systems.
- Getting Started with the LabVIEW Real-Time Module—This manual introduces the concepts necessary to create real-time simulations .
- Real-Time Execution Trace Toolkit documentation.
- NI-CAN Hardware and Software Manual
- NI-DAQmx Help
- LabVIEW Control Design and Simulation Module Readme —Use this file to learn important last-minute information, including installation and upgrade issues, compatibility issues, changes from the previous version, and known issues with the Control Design and Simulation Module. Open this readme by selecting Start»All Programs»National Instruments»LabVIEW»Readme and opening readme_ControlandSim.html or by navigating to the labview\readme directory and opening readme_ControlandSim.html .
- LabVIEW Control Design and Simulation Module example VIs—Refer to the labview\examples\Control and Simulation directory for example VIs that demonstrate common tasks using the Control Design and Simulation Module. You also can access these VIs by selecting Help»Find Examples and selecting Toolkits and Modules»Control and Simulation in the NI Example Finder window.
- (Windows) System Identification example VIs—Refer to the labview\examples\System Identification directory for example VIs that demonstrate common tasks using the System Identification VIs. You also can access these VIs by selecting Help»Find Examples and selecting Toolkits and Modules»System Identification in the NI Example Finder window.
- (Windows) LabVIEW System Identification VIs Algorithm References—Use this manual to learn about the algorithms and function references that the System Identification VIs use.
- Additional LabVIEW documentation .

|  | Note The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by NI. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the Control Design and Simulation Module or any other NI product. |
| --- | --- |

- Åström, K., and T. Hagglund. 1995. PID controllers: theory, design, and tuning. 2d ed. ISA.
- Balbis, Luisella. 2006. Predictive control tool kit. UKACC control, 2006. Mini symposia : 87–96.
- Bertsekas, Dimitri P. 1999. Nonlinear programming . 2d ed. Belmont, MA: Athena Scientific.
- Datta, A., M. T. Ho, and S. P. Bhattacharyya. 2000. Structure and synthesis of PID controllers. London: Springer-Verlag.
- Dorf, R. C., and R. H. Bishop. 2010. Modern control systems. 12th ed. Upper Saddle River, NJ: Prentice Hall.
- Franklin, G. F., J. D. Powell, and A. Emami-Naeini. 2009. Feedback control of dynamic systems. 6th ed. Upper Saddle River, NJ: Prentice Hall.
- Franklin, G. F., J. D. Powell, and M. L. Workman. 1997. Digital control of dynamic systems. 3d ed. Menlo Park, CA: Addison Wesley.
- Ho, Ming-Tzu, G. J. Silva, A. Datta, and S. P. Bhattacharyya. 2004. Real and complex stabilization: stability and performance. Proc. Of the 2004 American Control Conference 5:4126–38.
- Keel, L. H., J. I. Rego, and S. P. Bhattacharyya. 2003. A new approach to digital PID controller design. IEEE Transactions on Automatic Control 48, no. 4.
- Keel, L.H., and S.P. Bhattacharyya. 2002. Root counting, phase unwrapping, stability and stabilization of discrete time systems. Linear algebra and its applications 351–2:501–518.
- Kuo, Benjamin C. 1995. Digital control systems. 2d ed. New York: Oxford University Press.
- Loan, C.F.V. 1978. Computing integrals involving the matrix exponential, IEEE Transactions on Automatic Control , vol. 23, no. 3, pp. 395–404.
- Nise, Norman S. 2010. Control systems engineering. 6th ed. New York: John Wiley & Sons, Inc.
- Ogata, Katsuhiko. 1995. Discrete-time control systems. 2d ed. Englewood Cliffs, N.J.: Prentice Hall.
- Ogata, Katsuhiko. 2009. Modern control engineering. 5th ed. Upper Saddle River, NJ: Prentice Hall.
- Zhou, Kemin, and John C. Doyle. 1998. Essentials of robust control. Upper Saddle River, NJ: Prentice Hall.

#### Related Documentation for ODE and DAE Solvers

The following resources contain information about [ordinary differential equation (ODE) solvers](../lvsimconcepts/sim_c_ode_solvers.html) the Control Design and Simulation Module provides.

- Ascher, U. M., and L. R. Petzold. 1998. Computer methods for ordinary differential equations and differential-algebraic equations . Philadelphia: Society for Industrial and Applied Mathematics.
- Bogacki, P., and L. F. Shampine. 1989. A 3(2) Pair of Runge-Kutta formulas. Applied Mathematics Letters , vol. 2, no. 4, pp. 321-325.
- Brown, Roy Leonard, and Charles William Gear. 1973. Documentation for DFASUB - A Program for the Solution of Simultaneous Implicit Differential and Nonlinear Equations . Urbana, Illinois: Department of Computer Science, University of Illinois at Urbana-Champaign.
- Gear, C. W. 1970. The Simultaneous Numerical Solution of Differential-Algebraic Equations . Stanford, California: Stanford Linear Accelerator Center and Computer Science Department, Stanford University.
- Gear, C. William. 1971. Numerical Initial Value Problems in Ordinary Differential Equations . New Jersey: Prentice-Hall.
- Hairer, E. and G. Wanner. 1991. Solving Ordinary Differential Equations II, Stiff and Differential-Algebraic Problems (Springer Series in Computational Mathematics) . Berlin: Springer-Verlag.
- Hairer, Ernst, and Gerhard Wanner. Stiff differential equations solved by Radau methods. Journal of Computational and Applied Mathematics , vol. 111, no. 1-2, pp. 93-111.
- Hairer, E., S. P. Nørsett, G. Wanner. 1993. Solving Ordinary Differential Equations I, Nonstiff Problems, (Springer Series in Computational Mathematics) . 2nd ed. Berlin: Springer-Verlag.
- Ralston, A. 1978. A First Course in Numerical Analysis . 2nd ed. New York: McGraw-Hill Inc.
- Shampine, Lawrence F. 1994. Numerical solution of ordinary differential equations. New York: Chapman & Hall, Inc.
- Shampine, Lawrence F., and M. K. Gordon. 1975. Computer Solution of Ordinary Differential Equations: The Initial Value Problem . New York: W. H. Freeman and Company.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_trademarks.html language=enus -->
## TOPIC 00020: Trademarks

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_trademarks.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_trademarks.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Trademarks

LabVIEW, National Instruments, NI, ni.com, the National Instruments corporate logo, and the Eagle logo are trademarks of National Instruments Corporation. Refer to the *Trademark Information* at ni.com/trademarks for other National Instruments trademarks.

MATLAB®, Stateflow®, and Simulink® are registered trademarks of The MathWorks, Inc.

FireWire® is the registered trademark of Apple Inc.

Handle Graphics®, MATLAB®, Real-Time Workshop®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and TargetBox™ and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix® and Tek are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

Other product and company names mentioned herein are trademarks or trade names of their respective companies.

Members of the National Instruments Alliance Partner Program are business entities independent from National Instruments and have no agency, partnership, or joint-venture relationship with National Instruments.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_using_emi.html language=enus -->
## TOPIC 00021: Using the External Model Interface (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_using_emi.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_using_emi.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Using the External Model Interface (Control Design and Simulation Module)

Third parties can use the External Model Interface (EMI) to [create](#create) an external, or third-party, model in C/C++. LabVIEW users can use EMI to [simulate](#simulate) the external model in the LabVIEW Control Design and Simulation Module.

The following illustration shows the relationship between the components of the EMI.

[IMAGE alt='image' src='loc_eps_emi_relationships.gif']

#### Creating an External Model

First create a C/C++ project that uses the [External Model Interface](../lvsimemi/emi_lvsimemi.html) functions to define the dynamic equations for the model. Refer to the [Example 1: Creating an External Model](../lvsimhowto/sim_emi_example1.html) topic for an example of a C/C++ project that defines an external model.

|  | Note In many cases, LabVIEW users do not need to create external models. Instead, use the External Model function in LabVIEW to simulate models you receive from a third party. |
| --- | --- |

Before defining the dynamic equations for the external model, you must include the SIM_EMI_API.h header file, located in the labview\CCodeGen\Simulation directory. This header file includes definitions and declarations for all functions and data types that the EMI supports.

After you enter the include line for the header file, use the External Model Interface functions to define the following dynamic equations for the external model:

| Model Part | Equation |
| --- | --- |
| Indirect Outputs | yindirect = f1(t, p, xc, xd) |
| Direct Outputs | ydirect = f2(t, p, xc, xd, u) |
| Derivatives of Continuous States | xc' = f3(t, p, xc, xd, u) |
| Discrete States | xd, next = f4(t, p, xc, xd, u) |

| where | y is the outputs of the model |
| --- | --- |
|  | t is the time |
|  | p is the parameters of the model |
|  | xc is the continuous states |
|  | xd is the discrete states |
|  | u is the inputs to the model |
|  | xc' is the derivatives of xc |

|  | Note The total number of inputs (u), outputs (y), and parameters (p) of the model cannot exceed 25. |
| --- | --- |

You also can define equations for calculating the [zero crossings](../lvsimconcepts/sim_zero_crossings.html) or reset states of the external model.

You must export the [EMI_CB_ModelInterface](../lvsimemi/emi_emi_cb_modelinterface.html) function for each model you create. You also must export [Callbacks](../lvsimemi/emi_callbacks.html) functions as appropriate for the structure of the model. For example, if the model contains indirect outputs, you must export the [EMI_CB_CalculateIndirectOutputs](../lvsimemi/emi_emi_cb_calculateindirectoutputs.html) function to calculate the indirect outputs. If you do not export the appropriate Callbacks functions, LabVIEW returns an error when you attempt to simulate the model.

Build the C/C++ project into a (Windows) .dll, (macOS) .framework or .dylib, or (Linux) .so shared library file and distribute the shared library to end users.

#### Simulating an External Model

Use the [External Model](../lvsim/sim_external_model.html) function to represent an external model that you want to simulate, such as a model you receive from a third party. Refer to the [Example 2: Simulating an External Model](../lvsimhowto/sim_emi_example2.html) topic for an example of simulating an external model.

When you add an External Model function to a [simulation diagram](../lvsimconcepts/sim_c_buildsim.html), the [Select an External Model Library](../lvsim/sim_select_emlib_db.html) dialog box appears. In this dialog box, specify the shared library you want to reference from the External Model function. The External Model function updates to reflect the structure of the model corresponding to the shared library. For example, if the model has one input, two parameters, and one output, the External Model function has one block diagram input, two parameters in the [configuration dialog box](../lvsimconcepts/sim_c_func.html), and one block diagram output.

When you run the simulation, the Control Design and Simulation Module uses an [ordinary differential equation](/csh?topicname=lvanlsconcepts/solving_odes.html) (ODE) solver to compute the behavior of the dynamic system model that the External Model function represents. The Control Design and Simulation Module calls the External Model Interface functions that the corresponding shared library exports.

|  | Note The Control Design and Simulation Module executes the Callbacks functions in a specific order. |
| --- | --- |

If the shared library you reference from an External Model function changes, right-click the External Model function and select **Relink to External Model Library** from the shortcut menu to reference the modified shared library. If you want to reference a different shared library from the External Model function, right-click the External Model function and select **Select External Model Library** from the shortcut menu to display the [Select an External Model Library](../lvsim/sim_select_emlib_db.html) dialog box. Then select the new shared library you want to reference.

You can [configure](../lvsimconcepts/sim_c_func.html) the External Model function as you do other Simulation functions.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimconcepts/sim_zero_crossings.html language=enus -->
## TOPIC 00022: Detecting Zero Crossings (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimconcepts/sim_zero_crossings.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimconcepts/sim_zero_crossings.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Detecting Zero Crossings (Control Design and Simulation Module)

Use the [Detect Zero Crossing](../lvsim/sim_zerocrossdetect.html) function to detect a zero crossing in a simulation. Use the [Zero Crossings](../lvsimemi/emi_zero_crossings.html) functions to detect zero crossings for an [external model](#external_model_zcs).

A zero crossing occurs if the following equation is true:

sgn(*u*(*t<sub>i</sub>*<sub>–1</sub>)–**offset**(*t<sub>i</sub>*<sub>–1</sub>)) ≠ sgn(*u*(*t<sub>i</sub>*)–**offset**(*t<sub>i</sub>*))

| where | u(t) is the value of the signal at time t |
| --- | --- |
|  | ti is the time of the current step |
|  | ti–1 is the time of the previous step |

The internal zero-crossing detection system of the LabVIEW Control Design and Simulation Module uses linear interpolation. For example, the Control Design and Simulation Module checks whether a zero crossing occurred at the current time step. If a zero crossing occurred between the previous time step and the current time step, the Control Design and Simulation Module rejects the current time step, if possible. The Control Design and Simulation Module then performs linear interpolation between the value of the signal at the previous time step and the value of the signal at the current time step, proposes a new step size corresponding to the time at which the interpolated line crosses the offset, and checks again for a zero crossing. The Control Design and Simulation Module continues rejecting and proposing new step sizes either until it identifies the time step corresponding to the zero crossing or until it can no longer reject any steps.

The Control Design and Simulation Module resets the [ordinary differential equation (ODE) solver](../lvsimconcepts/sim_c_ode.html) when a zero crossing occurs.

#### Detecting Zero Crossings in an External Model

Third parties can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to create an external, or third-party model in C/C++. If you are a third-party user of EMI, use the following guidelines to detect zero crossings for a model you create.

- If you need to configure the zero crossing triggers and offsets only once, such as before a simulation runs, set the triggers and offsets in the EMI_CB_InitializeModel function. Otherwise, write code that updates the triggers and offsets as necessary during the simulation.
- Define and export the EMI_CB_CalculateZeroCrossingSignals function to calculate the signals you want to monitor for zero crossings.
- Write code to respond to zero crossings. For example, you can use the EMI_GetZeroCrossingResults function to determine the type of zero crossing that occurred. The Control Design and Simulation Module also automatically calls the EMI_CB_CalculateResetStates function when a zero crossing occurs.

You also can implement a custom algorithm for checking an external model for zero crossings, for example if you want to use polynomial interpolation instead of linear interpolation. Within the [EMI_CB_CheckStepAcceptance](../lvsimemi/emi_emi_cb_checkstepacceptance.html) function, first check whether a zero crossing occurred at the current time step. If a zero crossing occurred between the previous time step and the current time step, use the [EMI_CanRejectStep](../lvsimemi/emi_emi_canrejectstep.html) function to determine whether you can reject the current time step. If you can reject the current time step, use the [EMI_RejectStep](../lvsimemi/emi_emi_rejectstep.html) function to reject the time step and propose a new step size. If you cannot reject the current time step, you might want to use the [EMI_RequestCallbackToResetStates](../lvsimemi/emi_emi_requestcallbacktoresetstates.html) function to request a call to the EMI_CB_CalculateResetStates function after the current time step.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/cdsim_shortcut.html language=enus -->
## TOPIC 00023: Keyboard Shortcuts (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/cdsim_shortcut.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/cdsim_shortcut.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Keyboard Shortcuts (Control Design and Simulation Module)

The following table lists keyboard shortcuts you can use in the Control Design and Simulation Module.

|  | Note The <Ctrl> key in these shortcuts corresponds to the (macOS) <Command> key. |
| --- | --- |

| Keyboard Shortcut | Description |
| --- | --- |
| Simulation Functions |  |
| Double-click | Displays the configuration dialog box for the function. |
| Simulation Subsystems |  |
| Double-click | Displays the Subsystem Configuration dialog box. |
| Ctrl-double-click | Displays the block diagram of the subsystem. |
| Shift-double-click | Displays the front panel of the subsystem. |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_create_emi.html language=enus -->
## TOPIC 00024: Creating External Models (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_create_emi.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_create_emi.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Creating External Models (Control Design and Simulation Module)

Third parties can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to create an external, or third-party, model in C/C++. Refer to the [Example 1: Creating an External Model](../lvsimhowto/sim_emi_example1.html) topic for an example of a C/C++ project that defines an external model.

Complete the following steps to create an external model.

1. Create a C/C++ project that uses the External Model Interface functions to define the dynamic equations for the external model you want to simulate. Use the following guidelines when creating the C/C++ project:
  - Use C-style calling conventions when defining the Callbacks functions.
  - Use the EMI_GetCurrentVersion function in the Simulation shared library NILVSim.dll , (macOS) NILVSim.framework or (Linux) NILVSim.so , located in the labview/vi.lib/Simulation/Implementation/Shared/ directory, to determine which version of the External Model Interface is installed. Generate C/C++ code that is compatible with the installed version of the External Model Interface.
  - Include the SIM_EMI_API.h header file, located in the labview\CCodeGen\Simulation directory. This header file includes definitions and declarations for all functions and data types that the EMI supports.
  - Export the EMI_CB_ModelInterface function. You must export the EMI_CB_ModelInterface function for each model you create.
  - Export Callbacks functions as appropriate for the structure of the model. For example, if the model contains indirect outputs, you must export the EMI_CB_CalculateIndirectOutputs function to calculate the indirect outputs. If you do not export the appropriate Callbacks functions, LabVIEW returns an error when you attempt to simulate the model.
  - Ensure the model has no more than 25 total inputs, outputs, and parameters.
2. Build the C/C++ project into a (Windows) .dll , (macOS) .framework or .dylib , or (Linux) .so shared library file.
3. Distribute the shared library to end users.

LabVIEW users can use EMI to [simulate](../lvsimhowto/sim_simulate_emi.html) the external model in the LabVIEW Control Design and Simulation Module.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_create_sim_emi.html language=enus -->
## TOPIC 00025: Creating and Simulating External Models (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_create_sim_emi.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_create_sim_emi.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Creating and Simulating External Models (Control Design and Simulation Module)

Third parties can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to [create](../lvsimhowto/sim_create_emi.html) an external, or third-party, model in C/C++. LabVIEW users can use EMI to [simulate](../lvsimhowto/sim_simulate_emi.html) the external model in the LabVIEW Control Design and Simulation Module.

|  | (Windows) To view topics related to the Control Design and Simulation Module, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_emi_example1.html language=enus -->
## TOPIC 00026: Example 1: Creating an External Model (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_emi_example1.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_emi_example1.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Example 1: Creating an External Model (Control Design and Simulation Module)

Third parties can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to create an external, or third-party, model in C/C++.

The following code illustrates an example of a C/C++ project that uses the [External Model Interface](../lvsimemi/emi_lvsimemi.html) functions to define the dynamic equations for a simple integrator. This code is similar to the EMI_Integrator example, accessible by navigating to the labview\examples\Control and Simulation\Simulation\External Model Interface\EMI_Integrator\Source directory and opening EMI_Integrator.c.

|  | Note In many cases, LabVIEW users do not need to create external models. Instead, use the External Model function in LabVIEW to simulate models you receive from a third party. Refer to Example 2 for an example of simulating an external model. |
| --- | --- |

#include "SIM_EMI_API.h"

void EMI_CB_ModelInterface(emiRef model){

EMI_SetModelName(model, "My Integrator");

EMI_AddScalarInput(model, "Input");

EMI_AddScalarParam(model, "Initial Value", EMI_ParamSource_ConfigPage, 0.0);

EMI_AddScalarOutput(model, "Output", EMI_Feedthrough_Indirect);

}

void EMI_CB_SizeInformation(emiRef model){

EMI_SetNumberOfContinuousStates(model, 1);

}

void EMI_CB_InitializeModel(emiRef model){

double* xc = EMI_GetInitialContinuousStates(model);

const double* p = EMI_GetParam(model, 0);

xc[0] = p[0];

}

void EMI_CB_CalculateDerivatives(emiRef model){

double* d = EMI_GetDerivatives(model);

const double* u = EMI_GetInput(model, 0);

d[0] = u[0];

}

void EMI_CB_CalculateIndirectOutputs(emiRef model){

double* y = EMI_GetOutput(model, 0);

const double* xc = EMI_GetContinuousStates(model);

y[0] = xc[0];

}

Notice that this file first includes the SIM_EMI_API.h header file. This header file is located in the labview\CCodeGen\Simulation directory.

The [EMI_CB_ModelInterface](../lvsimemi/emi_emi_cb_modelinterface.html) function specifies information about the model, such as the number and names of the inputs and outputs. In this example, the EMI_CB_ModelInterface function specifies that the model has the following characteristics:

- model name of My Integrator
- one input named Input
- one parameter named Initial Value whose default source is the configuration dialog box of the External Model function and whose default value is 0.0
- one output named Output with indirect feedthrough behavior

The [EMI_CB_SizeInformation](../lvsimemi/emi_emi_cb_sizeinformation.html) function specifies information about the states and zero crossing signals of the model. In this example, the EMI_CB_SizeInformation function specifies that the model has one continuous state.

The [EMI_CB_InitializeModel](../lvsimemi/emi_emi_cb_initializemodel.html) function initializes the continuous state to the value of the first element of the parameter. The [EMI_CB_CalculateDerivatives](../lvsimemi/emi_emi_cb_calculatederivatives.html) and [EMI_CB_CalculateIndirectOutputs](../lvsimemi/emi_emi_cb_calculateindirectoutputs.html) functions calculate the derivatives of the continuous states and the indirect outputs of the model, respectively.

The C/C++ project you create must export the EMI_CB_ModelInterface function and any other [Callbacks](../lvsimemi/emi_callbacks.html) functions as appropriate for the structure of the model. In this example, you must export all five defined Callbacks functions.

After you create the model, build the C/C++ project into a (Windows) .dll, (macOS) .framework or .dylib, or (Linux) .so shared library file and distribute the shared library to end users.

LabVIEW users can reference this shared library from the [External Model](../lvsim/sim_external_model.html) function and use the External Model function to represent and simulate the model in the Control Design and Simulation Module.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_emi_example2.html language=enus -->
## TOPIC 00027: Example 2: Simulating an External Model (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_emi_example2.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_emi_example2.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Example 2: Simulating an External Model (Control Design and Simulation Module)

LabVIEW users can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to simulate an external, or third-party, model in the LabVIEW Control Design and Simulation Module. Use the [External Model](../lvsim/sim_external_model.html) function to represent and simulate the model.

Complete the following steps to simulate the My Integrator model created in [Example 1](../lvsimhowto/sim_emi_example1.html).

1. In a blank VI, add a Control & Simulation Loop to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
2. Add an External Model function to the block diagram inside the Control & Simulation Loop.
 [IMAGE alt='image' src='add.gif'] Add
3. In the Select an External Model Library dialog box that appears, browse to the shared library corresponding to the My Integrator model. You also can browse to the EMI_Integrator.dll file located in the labview\examples\Control and Simulation\Simulation\External Model Interface\EMI_Integrator directory. This .dll file corresponds to the EMI_Integrator.c example code.
4. Click the OK button to close the Select an External Model Library dialog box.
5. If the Context Help window is not displayed, select Help»Show Context Help to display the window.
6. Hover over the External Model function on the block diagram. Notice that the function now has a name of My Integrator , one block diagram input named Input , and one block diagram output named Output .
7. Double-click the External Model function to display the configuration dialog box. Notice that the configuration dialog box has an Initial Value parameter with a default value of 0.
8. Click the OK button to close the configuration dialog box for the External Model function.
9. Add a Sine Signal function to the block diagram inside the Control & Simulation Loop and to the left of the External Model function.
 [IMAGE alt='image' src='add.gif'] Add
10. Wire the output output of the Sine Signal function to the Input input of the External Model function.
11. Add a SimTime Waveform function to the block diagram inside the Control & Simulation Loop and to the right of the External Model function. When you place this function on a simulation diagram, LabVIEW automatically wires a waveform chart indicator to the function.
 [IMAGE alt='image' src='add.gif'] Add
12. Wire the Output output of the External Model function to the Value input of the SimTime Waveform function.
13. Press the <Ctrl-E> keys to display the front panel window of the VI.
14. Run the VI and observe that the Waveform Chart indicator displays the integral of a sine wave.
15. Stop the VI.

Refer to the EMI_Integrator VI in the labview\examples\Control and Simulation\Simulation\External Model Interface\EMI_Integrator directory for an example of using the External Model function.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_esi_create.html language=enus -->
## TOPIC 00028: Creating an External Solver (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_esi_create.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_esi_create.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Creating an External Solver (Control Design and Simulation Module)

You can use the [External Solver Interface](../lvsimhowto/sim_using_esi.html) to create and [use](../lvsimhowto/sim_using_esi.html) external [ordinary differential equation](/csh?topicname=lvanlsconcepts/solving_odes.html) (ODE) solvers in the LabVIEW Control Design and Simulation Module. When you create an external solver, you can use the solver for any [simulation subsystem](../lvsimhowto/sim_h_subsyssa.html).

Complete the following steps to create an external solver.

1. Create a C/C++ project that uses the External Solver Interface functions to define the external ODE solver. Use the following guidelines when creating the C/C++ project:
  - Use C-style calling conventions when defining the External Solver Interface functions.
  - Include the SIM_Solver.h header file, located in the labview\CCodeGen\Simulation directory. This header file includes definitions and declarations for all functions and data types that the ESI supports.
  - Use the Information function to specify the name of the solver that appears in the ODE Solver pull-down menu in the Configure Simulation Parameters dialog box.
  - Define the solver such that it exports all Callback API functions.
2. Build the C/C++ project into a (Windows) .dll , (macOS) .framework or .dylib , or (Linux) .so shared library file.
3. Copy the shared library file into the labview\vi.lib\Simulation\ContinuousLinear\Implementation\Shared\Solvers\Plugins directory for each installation of LabVIEW where you want to use the external ODE solver.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_esi_howto.html language=enus -->
## TOPIC 00029: Creating and Using External Solvers (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_esi_howto.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_esi_howto.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Creating and Using External Solvers (Control Design and Simulation Module)

Use the [External Solver Interface](../lvsimhowto/sim_using_esi.html) (ESI) to [create](../lvsimhowto/sim_esi_create.html) and [use](../lvsimhowto/sim_using_esi.html) external ordinary differential equation (ODE) solvers in the LabVIEW Control Design and Simulation Module.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_addinput.html language=enus -->
## TOPIC 00030: Displaying Additional Inputs and Outputs on the Control & Simulation Loop (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_addinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_addinput.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Displaying Additional Inputs and Outputs on the Control & Simulation Loop (Control Design and Simulation Module)

You can use three methods to display additional inputs on the Input Node. The first method you can use is resizing the Input Node. To resize a node, first move the cursor over the Input Node to display resizing handles. Then, move the cursor over a resizing handle. Click and drag the handle down to add terminals to the node.

The second method you can use is adding individual inputs. To add the next available input, right-click the Input Node and select **Add Input** from the shortcut menu.

The third method you can use is displaying all the available inputs. To display all the available inputs, right-click the Input Node and select **Show All Inputs** from the shortcut menu.

#### Displaying Additional Outputs

To display outputs on the Output Node that [store and return the value of a signal over the duration of the simulation](../lvsimconcepts/sim_c_utils.html#storing), double-click the Output Node to display the [Access Model Hierarchy Configuration](../lvsim/sim_access_hrchy_db.html) dialog box. In this dialog box, create an accessor for the signal you want to store. After you create and configure an accessor in this dialog box and click the **OK** button, an output terminal displays on the Output Node.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_calcdisc.html language=enus -->
## TOPIC 00031: Automatically Calculating the Discrete Step Size of a Simulation (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_calcdisc.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_calcdisc.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Automatically Calculating the Discrete Step Size of a Simulation (Control Design and Simulation Module)

Instead of manually entering a discrete step size for the simulation, you can use the LabVIEW Control Design and Simulation Module to automatically calculate the discrete step size of the simulation based on the **sample period (s)** parameter and **sample skew (s)** parameter of each [Discrete Linear Systems](../lvsim/discrete_systems.html) function on the simulation diagram. The step size of a [fixed step-size](/csh?topicname=lvanlsconcepts/vble_vs_fixed_step_size_ode.html) [ordinary differential equation (ODE) solver](../lvsimconcepts/sim_c_ode.html) also affects the discrete step size of the simulation. The step sizes of variable step-size ODE solvers do not affect this discrete step size.

The Control Design and Simulation Module calculates the floating-point greatest common divisor (GCD) of two numbers, *x*<sub>1</sub> and *x*<sub>2</sub>, by finding the largest value of *z* such that the following equation is true:

abs((*x*<sub>i</sub>/*z*) – round(*x*<sub>i</sub>/*z*)) > ε

where *i* = 1, 2, ... *n*

In this equation, *n*is the total number of discrete Simulation functions on the simulation diagram.*x*<sub>1</sub> is the **sample period (s)** parameter and the **sample skew (s)** parameter of a single discrete function on the simulation diagram. *x*<sub>2</sub> represents these parameters for a second discrete function on the simulation diagram. *z* is the discrete time step of the simulation, and ε is a small number. The Control Design and Simulation Module uses an extension of this equation to calculate the floating-point GCD of a set of discrete functions on the simulation diagram with sample periods *x*<sub>1</sub>, *x*<sub>2</sub>, ... *x<sub>n</sub>*, where *x<sub>n</sub>* > 0.

Complete the following steps to automatically configure the discrete time step of a simulation.

1. Display the Configure Simulation Parameters dialog box.
2. Place a checkmark in the Auto Discrete Time checkbox.
3. Click the OK button to save changes and return to the simulation diagram.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_convmdl.html language=enus -->
## TOPIC 00032: Converting Your Models into LabVIEW Code (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_convmdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_convmdl.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Converting Your Models into LabVIEW Code (Control Design and Simulation Module)

Select **Tools»Control Design and Simulation»Simulation Model Converter** to display the [Simulation Model Converter](../lvsim/sim_simtrans.html) dialog box.

The Simulation Model Converter executes the following steps:

1. Uses The MathWorks, Inc. MATLAB ® application software and The MathWorks, Inc. Simulink ® application software to compile your model ( .mdl or .slx ) file and execute any of your .m files that you specify in the dialog box. The MATLAB software obtains the values of any parameters and equations that your .m file contains. The Simulation Model Converter then passes these values from the MATLAB software to LabVIEW. If the MATLAB software is not installed on the same computer as the LabVIEW Control Design and Simulation Module, the results of the conversion might be less accurate.
2. Parses your model file for model information such as timing and ordinary differential equation (ODE) solver settings.
3. Stores each system, subsystem, block, and line in an XML-based Common Graph Description (CGD) format.
4. Generates a LabVIEW simulation subsystem corresponding to each model subsystem, in order. Converting in order ensures that the Simulation Model Converter generates every LabVIEW subsystem that has a parent simulation diagram before generating the parent simulation diagram. The Simulation Model Converter converts all blocks into one or more LabVIEW functions or simulation subsystems. The Simulation Model Converter also converts lines into wires that connect terminals on the LabVIEW functions and simulation subsystems.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs.html language=enus -->
## TOPIC 00033: Tutorial: Getting Started with Simulation (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Tutorial: Getting Started with Simulation (Control Design and Simulation Module)

This tutorial shows you how to construct a simulation diagram that represents the behavior of a dynamic system. This dynamic system consists of a spring with one end fixed and the other end attached to a mass. Because a damper inhibits the movement of the mass, this dynamic system is called a spring-mass damper system.

If you are new to LabVIEW, consider visiting ni.com/gettingstarted for more information about getting started with LabVIEW before proceeding with this tutorial.

|  | You can complete this tutorial in approximately 30 minutes. |
| --- | --- |

|  | Note You can print this tutorial by right-clicking this page and selecting Print from the shortcut menu. |
| --- | --- |

#### Background Information

A [dynamic system model](../lvsimconcepts/sim_c_models.html) is a differential or difference equation that describes the behavior of the dynamic system. In this tutorial, the following differential equation describes the dynamic system.

*F*(*t*) − *cx*'(*t*) − *kx*(*t*) = *mx*''(*t*)

where *t* is the simulation time, *F*(*t*) is an external force applied to the system, *c* is the damping constant of the spring, *k* is the stiffness of the spring, *m* is a mass, and *x*(*t*) is the position of the mass. *x*' is the first derivative of the position, which equals the velocity of the mass. *x*'' is the second derivative of the position, which equals the acceleration of the mass.

The following illustration shows this dynamic system.

[IMAGE alt='image' src='loc_eps_smdamper.gif']

The goal of this tutorial is to use the LabVIEW Control Design and Simulation Module to view the position *x*(*t*) of the mass *m* with respect to time *t*. You can calculate the position by integrating the velocity of the mass. You can calculate the velocity by integrating the acceleration of the mass. If you know the force and mass, you can calculate this acceleration by using Newton's Second Law of Motion, given by the following equation:

Force = Mass / Acceleration

Therefore,

Acceleration = Force / Mass

Substituting terms from the differential equation above yields the following equation:

*x*''(*t*) = (*F*(*t*) − *cx*'(*t*) − *kx*(*t*))/*m*

In this tutorial you will construct a simulation diagram that iterates the following steps over a period of time.

1. Divides a known force by a known mass to calculate the acceleration of the mass.
2. Integrates acceleration to calculate the velocity of the mass.
3. Integrates velocity to calculate the position of the mass.

Performing these integrations over a period of time requires an [ordinary differential equation](../lvsimconcepts/sim_c_ode.html) (ODE) solver. LabVIEW includes several ODE solvers you can use in a simulation. Each ODE solver has properties that make it suitable for different tasks. For example, some ODE solvers have [variable step sizes](/csh?topicname=lvanlsconcepts/vble_vs_fixed_step_size_ode.html). During a simulation, these ODE solvers can adjust the points in time at which the Control Design and Simulation Module evaluates the simulation diagram. Conversely, ODE solvers with fixed step sizes cannot make this change.

Complete the steps in the following sections to build a simulation diagram that simulates the spring-mass damper dynamic system model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_bs.html language=enus -->
## TOPIC 00034: 3. Building the Simulation (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_bs.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_bs.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 3. Building the Simulation (Control Design and Simulation Module)

The next step is to build the simulation by placing Simulation functions on the simulation diagram and wiring these functions together. Note that you can place most Simulation functions only on the simulation diagram, that is, you cannot place Simulation functions on a LabVIEW block diagram. Complete the following steps to build the simulation of this dynamic system.

#### Placing Functions on the Simulation Diagram

1. Navigate to the Simulation palette.
2. Select the Signal Arithmetic palette and place a Multiplication function on the simulation diagram. You will use this function to divide the force by the mass to calculate the acceleration.
3. Double-click the Multiplication function to display the configuration dialog box for the function. You can double-click most Simulation functions to view and change the parameters of that function.
4. The function currently displays two × symbols on the left side of the dialog box. This setting specifies that both incoming signals are multiplied together. Click the bottom × symbol to change it to a × symbol. This Multiplication function now divides the top signal by the bottom signal.
 [IMAGE alt='image' src='tip.gif']
 **Tip** To view detailed information about the Multiplication function, click the **Help** button in this dialog box.
5. Click the OK button to save changes and return to the simulation diagram.
6. Right-click the Multiplication function and select Visible Items»Label from the shortcut menu. Double-click the Multiplication label and enter Calculate Acceleration as the new label.
7. Return to the Simulation palette and select the Continuous Linear Systems palette.
8. Place an Integrator function on the simulation diagram. You will use this function to calculate velocity by integrating acceleration.
 [IMAGE alt='image' src='note.gif']
 **Note** If you move the Integrator function close enough to the Multiplication function, LabVIEW might [automatically create a wire](/csh?topicname=lvhowto/automatic_wiring.html) between the two functions. In this situation, place the Integrator on the simulation diagram and then delete the wire LabVIEW creates by right-clicking the wire and selecting **Delete Wire Branch** from the shortcut menu.
9. Label this Integrator function Calculate Velocity .
 [IMAGE alt='image' src='tip.gif']
 **Tip** To view detailed information about the Integrator function, right-click this function and select **Help** from the shortcut menu.
10. Press the <Ctrl> key and click and drag the Integrator function to another location on the simulation diagram. This action creates a copy of the Integrator function, which you will use to calculate position by integrating velocity. Label this new Integrator function Calculate Position .
11. Select the Graph Utilities palette and place two SimTime Waveform functions on the simulation diagram. You will use these functions to view the results of the simulation over time.
12. Each SimTime Waveform function has an associated Waveform Chart. Label the first waveform chart Velocity and the second waveform chart Position .
13. Arrange the functions to look like the following simulation diagram.
 [IMAGE alt='image' src='loc_bd_tut_loop.gif'] 
 [IMAGE alt='image' src='note.gif']
 **Note** If the **Velocity** and **Position** indicators do not resemble the previous block diagram, you can right-click each indicator and remove the checkmark from the [View as Icon](/csh?topicname=lvhowto/display_terms_as_fp_icons.html) option on the shortcut menu.
14. Select File»Save and save this VI to a convenient location as Spring-Mass Damper Example.vi .

#### Wiring the Simulation Functions Together

The next step is [wiring](/csh?topicname=lvconcepts/using_wires.html) the functions together to represent the flow of data from one function to another.

|  | Note Wires on the simulation diagram include arrows that show the direction of the dataflow, whereas wires on a LabVIEW block diagram do not show these arrows. |
| --- | --- |

Complete the following steps to wire these functions together.

|  | Tip If you have trouble viewing the input and output terminals the following steps mention, display the Context Help window by pressing <Ctrl-H>. This window displays all input and output terminals when you move the cursor over a function. |
| --- | --- |

1. Right-click the Operand1 input of the Calculate Acceleration function and select Create»Control from the shortcut menu to add a numeric control to the front panel window.
2. Label this control Force .
3. Double-click this control on the simulation diagram. LabVIEW displays the front panel and highlights the Force control.
4. Display the block diagram and create a control for the Operand2 input of the Calculate Acceleration function. Label this new control Mass .
5. Wire the Result output of the Calculate Acceleration function to the input input of the Calculate Velocity function.
6. Wire the output output of the Calculate Velocity function to the input input of the Calculate Position function.
7. Right-click the wire you just created and select Create Wire Branch from the shortcut menu. Wire this branch to the Value input of the SimTime Waveform function that has the Velocity waveform chart.
8. Wire the output output of the Calculate Position function to the Value input of the SimTime Waveform function that has the Position waveform chart. The simulation diagram now resembles the following image.
 [IMAGE alt='image' src='loc_bd_tut_loop_wired.gif'] 
 [IMAGE alt='image' src='note.gif']
 **Note** If the **Force** and **Mass** controls do not resemble the previous block diagram, you can right-click each control and remove the checkmark from the **View as Icon** option in the shortcut menu.

In the previous simulation diagram, notice how the arrows on each wire indicate data flow. For example, the values you will provide for **Force** and **Mass** controls flow into the Calculate Acceleration function, the result of this function flows into the Calculate Velocity function, and so on.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_csd.html language=enus -->
## TOPIC 00035: 1. Creating the Simulation Diagram (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_csd.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_csd.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 1. Creating the Simulation Diagram (Control Design and Simulation Module)

You create a simulation diagram by placing a [Control & Simulation Loop](../lvsim/sim_simulation_loop.html) on the LabVIEW block diagram. The Control & Simulation Loop contains parameters that affect the simulation, such as which ODE solver to use and how long to run the simulation. Complete the following steps to create the simulation diagram.

1. Launch LabVIEW and select File»New VI to create a new, blank VI.
2. Select Window»Show Block Diagram to view the block diagram. You also can press the <Ctrl-E> keys to view the block diagram.
3. If you are not already viewing the Functions palette, select View»Functions Palette to display this palette.
4. Select Control Design & Simulation»Simulation to view the Simulation palette.
5. Click the Control & Simulation Loop icon:
 [IMAGE alt='image' src='loopicon.gif']
6. Move the cursor over the block diagram. Click to place the top left corner of the loop, drag the cursor diagonally to establish the size of the loop, and click again to place the loop on the block diagram.
 The simulation diagram is the area enclosed by the Control & Simulation Loop. Notice the simulation diagram has a pale yellow background to distinguish it from the rest of the block diagram. You can resize the Control & Simulation Loop by dragging its borders.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_csfp.html language=enus -->
## TOPIC 00036: 7. Configuring Simulation Functions Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_csfp.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_csfp.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 7. Configuring Simulation Functions Programmatically (Control Design and Simulation Module)

The previous section provided information about configuring Simulation functions using the configuration dialog box. Instead of using the configuration dialog box, you can improve the interactivity of a simulation by creating front panel controls that configure a Simulation function programmatically. Complete the following steps to configure the Stiffness function programmatically.

1. If you are not already viewing the Context Help window, press <Ctrl-H> to display this window.
2. Display the block diagram and move the cursor over the Stiffness function. Notice this function has only one input terminal.
3. Display the configuration dialog box for the Stiffness function.
4. Select Terminal from the Parameter source pull-down menu. This action disables the gain numeric control.
5. Click the OK button to save changes and return to the block diagram.
6. Move the cursor over the Stiffness function. Notice the Context Help window displays the Gain function with the new gain input terminal.
7. Create a control for this input, and label the control Stiffness .
8. View the front panel. Notice the new control Stiffness . Enter a value of 100 for this control and run the simulation. Notice the behavior is exactly the same as when you used the configuration dialog box to configure the Stiffness function.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_csp.html language=enus -->
## TOPIC 00037: 2. Configuring Simulation Parameters (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_csp.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_csp.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 2. Configuring Simulation Parameters (Control Design and Simulation Module)

The Control & Simulation Loop contains the parameters that define how the simulation executes. Complete the following steps to view and configure these simulation parameters.

1. Double-click the Input Node, attached to the left side of the Control & Simulation Loop, to display the Configure Simulation Parameters dialog box. You also can right-click the loop border and select Configure Simulation Parameters from the shortcut menu.
2. Ensure the value of the Final Time (s) numeric control is 10 , which specifies that this tutorial simulates ten seconds of time.
3. Click the ODE Solver pull-down menu to view the list of ODE solvers the Control Design and Simulation Module includes. If the term (variable) appears next to an ODE solver, that solver has a variable step size. The other ODE solvers have a fixed step size. Ensure a checkmark is beside the default ODE solver Runge-Kutta 23 (variable) .
4. Because this ODE solver is a variable step-size solver, you can specify the Minimum Step Size (s) and Maximum Step Size (s) this ODE solver can take. Enter 0.01 in the Maximum Step Size (s) numeric control to limit the size of the time step this ODE solver can take.
5. Click the Timing Parameters tab to access parameters that control how often the simulation executes .
6. Ensure the Synchronize Loop to Timing Source checkbox does not contain a checkmark. This option specifies that the simulation executes without any timing restrictions.
 [IMAGE alt='image' src='note.gif']
 **Note** Use this option when you want the simulation to run as fast as possible. If you are running this simulation on a real-time (RT) target, you can place a checkmark in this checkbox and configure how often the simulation executes.
7. Click the OK button to save changes and return to the simulation diagram.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_cspp.html language=enus -->
## TOPIC 00038: 10. Configuring Simulation Parameters Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_cspp.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_cspp.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 10. Configuring Simulation Parameters Programmatically (Control Design and Simulation Module)

Earlier in this example, you used the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box to configure the parameters of Spring-Mass Damper Example.vi. You also can configure simulation parameters programmatically by using the Input Node of the Control & Simulation Loop. Complete the following steps to configure simulation parameters programmatically.

1. View the simulation diagram of Spring-Mass Damper Example.vi .
2. Move the cursor over the Input Node to display resizing handles.
3. Drag the bottom handle down to display all available Node inputs. You use these inputs to configure the simulation parameters without displaying the Configure Simulation Parameters dialog box.
 [IMAGE alt='image' src='tip.gif']
 **Tip** You also can right-click the Input Node and select **Show All Inputs** from the shortcut menu. 
 Notice the gray boxes next to each input. These boxes display values you configure in the Configure Simulation Parameters dialog box. For example, the third gray box from the top displays 10.0000 , which is the value of the Final Time numeric control that you configured. The fifth gray box from the top displays RK 23 . This box specifies the current ODE solver, which you configured as Runge-Kutta 23 (variable) .
 [IMAGE alt='image' src='tip.gif']
 **Tip** Move the cursor over the left edge of each Node input to display the label of that input.
4. Right-click the input terminal of the ODE Solver input and select Create»Constant from the shortcut menu. A block diagram constant appears outside the Control & Simulation Loop. The value of this constant is Runge-Kutta 1 (Euler) , which is different than what you configured in the Configure Simulation Parameters dialog box. However, the gray box disappears from the Input Node, indicating that the value of this parameter does not come from the Configure Simulation Parameters dialog box. Values that you programmatically configure override any settings you made in the Configure Simulation Parameters dialog box. The Input Node now resembles the following image. [IMAGE alt='image' src='loc_bd_tut_loop_pconfig.gif'] 
 [IMAGE alt='image' src='tip.gif']
 **Tip** You also can use this method to create a front panel control instead of a block diagram constant.
5. Right-click the constant you created and select Delete from the shortcut menu.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_css.html language=enus -->
## TOPIC 00039: 6. Configuring the Stiffness of the Spring (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_css.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_css.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 6. Configuring the Stiffness of the Spring (Control Design and Simulation Module)

Before you run the simulation again, you must configure the stiffness of the simulated spring. Complete the following steps to configure this Simulation function.

1. Double-click the Stiffness function to display the configuration dialog box.
2. Enter 100 in the gain numeric control. This value represents a stiffness of 100 Newtons per meter.
3. Click OK to return to the simulation diagram. Notice that the Stiffness function displays 100 .
4. Display the front panel and ensure the Force control is set to -9.8 and the Mass control is set to 1 .
5. Run the simulation. The Velocity and Position charts display the behavior of the mass as the spring oscillates. The front panel now resembles the following image. 
 [IMAGE alt='image' src='loc_fp_tut_loop_run_f.gif'] 
 
 Notice the new behavior compared to the last time you ran the simulation. This time, the velocity and position do not constantly decrease. Both values oscillate, which is how a spring behaves in the real world.
6. Change the value of the Mass control to 10 and run the simulation again. Notice the different behavior in the Velocity and Position charts. The 10 kg mass forces the spring to oscillate less frequently and within a smaller velocity/position range.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_ess.html language=enus -->
## TOPIC 00040: 9. Editing the Simulation Subsystem (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_ess.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_ess.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 9. Editing the Simulation Subsystem (Control Design and Simulation Module)

Edit the simulation subsystem Newton.vi by right-clicking this subsystem and selecting **Open Subsystem** from the shortcut menu. View the simulation diagram. Notice this simulation subsystem does not contain a Control & Simulation Loop, but the entire background is pale yellow to indicate a simulation diagram. If you place this simulation subsystem [in a Control & Simulation Loop](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_in_a_simulation_loop), the simulation subsystem inherits all simulation parameters from the Control & Simulation Loop. If you run this subsystem [as a stand-alone VI](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_as_a_stand-alone_vi), you can configure the simulation parameters by selecting **Operate»Configure Simulation Parameters**. Any parameters you configure using this method do not take effect when the subsystem is within another Control & Simulation Loop. If you place this simulation subsystem on a block diagram [outside a Control & Simulation Loop](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_outside_a_simulation_loop), you can configure the simulation parameters by double-clicking the simulation subsystem to display the configuration dialog box of that simulation subsystem.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_ls.html language=enus -->
## TOPIC 00041: 11. Linearizing a Subsystem (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_ls.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_ls.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 11. Linearizing a Subsystem (Control Design and Simulation Module)

To perform analysis on a simulation model, you first must create a linearized subsystem. Linearizing a nonlinear simulation subsystem involves approximating the behavior of that subsystem around an operating point. Complete the following steps to linearize a subsystem using the [Linearize Subsystem](../lvsim/linearizesubsystem.html) dialog box and perform analysis on the linearized subsystem.

1. Click and drag a selection rectangle around the portion of the simulation diagram selected in the following simulation diagram. [IMAGE alt='image' src='gs_linearizebd.gif']
2. Select Edit»Create Simulation Subsystem .
3. Save the VI. When LabVIEW prompts you to save, click the Yes button to save the new, unsaved subsystem. Name the subsystem Spring Mass Subsystem.vi .
4. Right-click the subsystem and select Trim/Linearize Subsystem from the shortcut menu. The Linearize Subsystem dialog box appears.
5. In the Static column of the Initial Inputs tab, place checkmarks in the checkboxes next to Stiffness and Mass . During the linearization process, these become constants instead of variables.
6. In the Value column of the Initial Inputs tab, enter a value of 100 for Stiffness , a value of 10 for Mass , and a value of -9.8 for Force .
7. Click the Linearize button to open the SIM Linearizer Results dialog box and display an equation representing the transfer function of the model.
8. Click the Save Model button and name the file Linearized Spring-Mass Damper Example.lti .
9. Close all open dialog boxes.
10. Save the VI.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_msdc.html language=enus -->
## TOPIC 00042: 8. Modularizing Simulation Diagram Code (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_msdc.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_msdc.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 8. Modularizing Simulation Diagram Code (Control Design and Simulation Module)

You can create [simulation subsystems](../lvsimconcepts/sim_c_subsys.html) to divide simulation diagrams into components that are modular, reusable, and independently verifiable. Complete the following steps to create a simulation subsystem from this simulation diagram.

1. View the simulation diagram.
2. Select the Calculate Acceleration, Calculate Velocity, and Calculate Position functions by pressing the <Shift> key and clicking each function.
3. Select Edit»Create Simulation Subsystem . LabVIEW replaces these three functions with a single function that represents the simulation subsystem, which is circled in the following image.
 [IMAGE alt='image' src='loc_bd_tut_loop_subsys.gif'] 
 The inputs and outputs of the simulation subsystem include the inputs and outputs of all the functions you selected. Also, notice the amount of blank space on the simulation diagram. Because you combined three functions into a subsystem, you can resize the Control & Simulation Loop and reposition the functions to make the simulation diagram easier to view.
4. Press <Ctrl-S> to save the simulation diagram. LabVIEW prompts you to save the simulation subsystem you just created. Click the Yes button and save this simulation subsystem as Newton.vi . You now have a simulation subsystem that obtains the position of a mass by using Newton's Second Law of Motion.

|  | Note You can resize the simulation subsystem to better display its simulation diagram. You also can double-click the simulation subsystem to display the configuration dialog box of that simulation subsystem. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_pals.html language=enus -->
## TOPIC 00043: 12. Performing Analysis on a Linearized Subsystem (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_pals.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_pals.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 12. Performing Analysis on a Linearized Subsystem (Control Design and Simulation Module)

After you linearize a subsystem, you might want to perform analysis on that subsystem by applying an impulse response and testing the reaction of the system. This procedure explains how to use LabVIEW Control Design and Simulation VIs to determine the damping ratio and the natural frequency of the newly linearized subsystem, view the mathematical representation of the transfer function equation, and display a pole-zero map of the results. You can use these results to determine how the linearized system performs under different impulse response conditions.

1. Create a new blank VI.
2. If you are not already viewing the Functions palette, select View»Functions Palette to display this palette.
3. Select Control Design & Simulation»Control Design»Model Construction to display the Model Construction palette.
4. Add the CD Read Model from File VI to the block diagram.
5. Right-click the File Path input of the CD Read Model from File VI and select Create»Control from the shortcut menu. Enter the path to the Linearized Spring-Mass Damper Example.lti model in the File Path control.
6. Add the CD Draw Transfer Function Equation VI to the block diagram. Wire the First State-Space Model in Record output of the CD Read Model From File VI to the Transfer-Function Model input of the CD Draw Transfer Function Equation VI.
 [IMAGE alt='image' src='note.gif']
 **Note** Because the CD Draw Transfer Function Equation VI is a polymorphic VI, the **Transfer-Function Model** input changes to a **State-Space Model** input when you wire these functions together.
7. Right-click the Equation output of the CD Draw Transfer Function VI and select Create»Indicator from the shortcut menu.
8. View the front panel and run the VI. Note that the Equation indicator displays the mathematical representation of the transfer function of the model you created.
9. Use the palette search to add a CD Pole-Zero Map VI, a CD Damping Ratio and Natural Frequency VI, and a CD Impulse Response VI to the block diagram.
 [IMAGE alt='image' src='note.gif']
 **Note** You also can perform step impulse analysis on a linearized subsystem using the [CD Step Response](../lvctrldsgn/step_response.html) VI.
10. Wire the First State-Space Model in Record output of the CD Read Model from File VI to the State-Space Model input of each VI.
11. Create indicators for the Pole-Zero Map output of the CD Pole-Zero Map VI, the Damping Ratio and Natural Frequencies outputs of the CD Damping Ratio and Natural Frequency VI, and the Impulse Response Graph output of the CD Impulse Response VI. The block diagram now resembles the following diagram.
 [IMAGE alt='image' src='gs_polezeromapbd.gif']
12. Switch to the front panel and run the VI. The front panel now resembles the following front panel.
 [IMAGE alt='image' src='gs_trimlinearizefp.gif']

Note that the **Impulse Response Graph** displays a waveform identical to the waveform in the Spring-Mass Damper Example.vi. The **Impulse Response Graph** simulates the original model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_rds.html language=enus -->
## TOPIC 00044: 5. Representing Damping and Stiffness (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_rds.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_rds.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 5. Representing Damping and Stiffness (Control Design and Simulation Module)

Representing damping and stiffness involves feeding back the velocity and position, each multiplied by a different constant, to the input of the Calculate Acceleration function. Recall the following differential equation this VI simulates.

*F*(*t*) − *cx*'(*t*) − *kx*(*t*) = *mx*''(*t*)

In the previous equation, notice you multiply the damping constant *c* by the velocity of the mass *x*'(*t*). You multiply the stiffness constant *k* by the mass position *x*(*t*). You then subtract these quantities from the external force applied to the mass.

Complete the following steps to represent damping and stiffness in this dynamic system model.

1. View the simulation diagram.
2. Select the Signal Arithmetic palette and place a Summation function on the simulation diagram. Move this function to the left of the Force and Mass controls.
3. Double-click the Summation function to configure its operation. By default, the Summation function displays the following three input terminals: a ∅ symbol, a + symbol, and a - symbol. This configuration subtracts one input signal from another.
 [IMAGE alt='image' src='note.gif']
 **Note** The **∅** terminal configures the visual layout of the function and does not provide a terminal for an input signal.
4. Click the ∅ symbol twice to change this terminal to the - symbol. This Summation function now subtracts the top and bottom input signals from the left input signal.
5. Click the OK button to save changes and return to the simulation diagram.
6. Select the Signal Arithmetic palette and place a Gain function on the simulation diagram. Move this function above the existing simulation diagram code but still within the Control & Simulation Loop.
7. The input of the Gain function is on the left side of the function, and the output is on the right side. You can reverse the direction of these terminals to indicate feedback better. Right-click the Gain function and select Reverse Terminals from the shortcut menu. The Gain function now points toward the left side of the simulation diagram.
8. Label this Gain function Damping .
9. Press the <Ctrl> key and drag the Gain function to create a separate copy. Move this copy below the existing simulation diagram code but still within the Control & Simulation Loop. Label this function Stiffness .
10. Right-click the wire connecting the Force control to the Calculate Acceleration function and select Delete Wire Branch from the shortcut menu. Move the Force control to the left of the Summation function, and wire this control to the Operand2 input of the Summation function.
11. Create wires 1-5 as indicated in the following image. 
 
 The simulation diagram now fully represents the equation that defines the behavior of the dynamic system.
12. Press <Ctrl-S> to save the VI.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_rs.html language=enus -->
## TOPIC 00045: 4. Running the Simulation (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_rs.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_rs.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### 4. Running the Simulation (Control Design and Simulation Module)

You now can run this simulation to test that the data is flowing properly through the Simulation functions. Complete the following steps to run this simulation.

1. Select Window»Show Front Panel , or press <Ctrl-E>, to view the front panel of this simulation. The front panel displays the following objects: a control labeled Force , a control labeled Mass , a waveform chart labeled Velocity , and a waveform chart labeled Position .
2. If necessary, rearrange these controls and indicators so that all objects are visible.
3. Enter -9.8 in the Force numeric control. This value represents the force of gravity, 9.8 meters per second squared, acting on the dynamic system.
4. Enter 1 in the Mass numeric control. This value represents a mass of one kilogram.
5. Click the Run button or press the <Ctrl-R> keys to run the VI.

The front panel now resembles the following image.

[IMAGE alt='image' src='loc_fp_tut_loop_run.gif']

In the previous front panel, notice that the force of gravity causes the mass position and velocity to constantly decrease. However, in the real world, a mass attached to a spring oscillates up and down. This simulated spring does not oscillate because the simulation diagram does not represent damping or stiffness. You must represent these factors to have a complete simulation of the dynamic system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_gs_sum.html language=enus -->
## TOPIC 00046: Summary (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_gs_sum.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_gs_sum.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Summary (Control Design and Simulation Module)

This tutorial introduced you to the following concepts:

- The simulation diagram reflects the dynamic system model you want to simulate. This dynamic system model is a differential or difference equation that represents a dynamic system.
- The Control & Simulation Loop contains the parameters that define the behavior of the simulation. The Control & Simulation Loop also defines the visual boundary of the simulation diagram. Double-click the Input Node of the Control & Simulation Loop to access configurable parameters . You also can expand the Input Node to access these parameters.
- The Simulation palette contains the VIs and functions you use to build a simulation. You can double-click most Simulation functions to display a dialog box that configures that function. You also can create input terminals for function inputs.
- You can create simulation subsystems to modularize, encapsulate, validate, and re-use portions of the simulation diagram.

#### Where to Go from Here

Refer to the following documentation for more information about the Control Design and Simulation Module and LabVIEW.

##### Additional Control Design and Simulation Module Resources

|  | (Windows) To view topics related to the Control Design and Simulation Module, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

The Control Design and Simulation Module ships with many example VIs that demonstrate the capabilities of the product. Select **Help»Find Examples** to display the [NI Example Finder](/csh?topicname=lvhowto/finding_example_vis.html) and browse these examples.

##### Additional LabVIEW Resources

- Refer to ni.com/gettingstarted for more information about getting started with LabVIEW.
- The Fundamentals book of the LabVIEW Help provides information about LabVIEW programming concepts, techniques, features, VIs, and functions you can use to create many types of applications.

Refer to the NI website for additional developer resources, training, technical support, and so on.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_itl.html language=enus -->
## TOPIC 00047: Trimming and Linearizing a Subsystem Interactively (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_itl.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_itl.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Trimming and Linearizing a Subsystem Interactively (Control Design and Simulation Module)

Use the [Linearize Subsystem](../lvsim/linearizesubsystem.html) dialog box to [trim and/or linearize](../lvsimconcepts/sim_c_trimlin.html) a nonlinear simulation subsystem.

Complete the following steps to use this dialog box:

1. Select Tools»Control Design and Simulation»Linearize Subsystem to display this dialog box.
2. Use the Subsystem page to select a simulation subsystem from memory or disk.
3. Choose the inputs and outputs you want in the linearized model. The linearize algorithm excludes inputs and outputs you mark as Static .
4. Use the tabs to specify any constraints on subsystem inputs, outputs, states, and/or state derivatives. The trim algorithm determines the input and state values that satisfy these constraints.
5. Click the Trim button to trim the subsystem. After you click this button, the optimal state, input, output, and state derivative values appear in the Trimmed Operating Point section.
6. Click the Import trimmed values button. Clicking this button transfers the values from the Trimmed Operating Point section to the Initial Inputs , Initial Outputs , and Initial States sections. The linearize algorithm uses values from these three sections as the operating point around which the nonlinear model is converted to an LTI state-space model.
7. Click the Linearize button to linearize the subsystem around the Trimmed Operating Point .

|  | Note You also can use the Trim & Linearize VIs to trim and linearize a nonlinear simulation subsystem. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_linmodint.html language=enus -->
## TOPIC 00048: Defining Linear Models Interactively (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_linmodint.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_linmodint.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Defining Linear Models Interactively (Control Design and Simulation Module)

You use the [Continuous Linear Systems](../lvsim/linear_systems.html) functions and the [Discrete Linear Systems](../lvsim/discrete_systems.html) functions to define continuous and discrete linear system models interactively or [programmatically](sim_h_linmodprog.html). The LabVIEW Control Design and Simulation Module supports transfer function, zero-pole-gain, and state-space model forms. Complete the following steps to configure a linear model interactively.

1. Place a continuous or discrete Transfer Function, Zero-Pole-Gain, or State-Space function on the simulation diagram.
2. Double-click the function to display the configuration dialog box.
3. Use the Polymorphic instance pull-down menu to specify whether the model is single-input single-output (SISO) or multiple-input multiple-output (MIMO).
4. Select the model parameter from the Parameters listbox. For example, if you are configuring a state-space function, select the State-Space parameter. After you select the parameter, the Parameter Information section shows the configuration options for the model.
5. If the model is MIMO, define the size of the model by using the Inputs and Outputs numeric controls in the Model Dimensions section. The Model Dimensions section is dimmed if you configure a SISO model because SISO models have only one input and one output. If the model is in state-space form, you also define the number of states using the States numeric control. 
 The following illustration shows a sample configuration dialog box for a MIMO transfer function model. 
 [IMAGE alt='image' src='loc_bd_tf_config_db.gif'] 
 
 The example in the previous illustration shows a model with two inputs and two outputs. The Inputs and Outputs numeric controls define these dimensions. The Numerator and Denominator vectors define the coefficients of the equation at the current input-output location. The Current Input and Current Output text boxes define the current input-output location. The Input-Output Model matrix also shows this location graphically with a black square.
6. Specify another input-output location by clicking an element in the Input-Output Model matrix. You also can adjust the values of the Current Input and Current Output text boxes. For example, to define the bottom-left equation of the MIMO model in the previous illustration, decrement the value of the Current Input text box by one. You also can click the bottom-left element of the Input-Output Model matrix.
7. Define the model by entering coefficients in the Numerator and Denominator vectors.
8. Click the OK button to save changes and return to the simulation diagram.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_linmodprog.html language=enus -->
## TOPIC 00049: Defining Linear Models Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_linmodprog.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_linmodprog.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Defining Linear Models Programmatically (Control Design and Simulation Module)

You can define models programmatically using the following methods:

- Wire a constant to the input of the function.
- Wire a model you constructed with the Model Construction VIs to the input of the function.

The following sections provide information about these methods.

#### Defining Linear Models Using a Constant

Complete the following steps to create a constant that represents the model.

1. Define the model interactively .
2. Click the Copy to Clipboard button in the configuration dialog box.
3. Select Terminal from the Parameter source pull-down menu.
4. Click the OK button to close the configuration dialog box and return to the block diagram.
5. Select Edit»Paste to paste a constant on the block diagram. This constant contains the terms you defined in step 1.
6. Wire the output of the constant to the appropriate input of the linear model function.

The following illustration shows a transfer function model as a block diagram constant.

[IMAGE alt='image' src='loc_bd_tf_constant.gif']

#### Defining Linear Models Using the Control Design VIs

If you already have created a model using the Model Construction VIs, you can place that model on the block diagram and wire the output of the model to the input of the corresponding Simulation function. The **Parameter source** pull-down menu in the configuration dialog box of this function must be set to **Terminal**. The following block diagram shows how you can use the [CD Construct Transfer Function Model](../lvctrldsgn/const_trans_func_model.html) VI to define a transfer function model.

[IMAGE alt='image' src='loc_bd_tf_cd_config.gif']

You can use the [Model Conversion](../lvctrldsgn/conversions_vis.html) VIs to convert model forms and representations on the simulation diagram. For example, you can wire a continuous controller model to the input of the [CD Convert Continuous to Discrete](../lvctrldsgn/convert_cont_to_discrete.html) VI. Then, wire the output of this VI to the input of a discrete Simulation function.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_linprog.html language=enus -->
## TOPIC 00050: Linearizing a Subsystem Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_linprog.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_linprog.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Linearizing a Subsystem Programmatically (Control Design and Simulation Module)

You can linearize a subsystem using the [SIM Linearize](../lvsim/sim_linearize_vi.html) VI. By default, this VI includes all subsystem states, inputs, and outputs in the linear time-invariant (LTI) model. You can exclude inputs and outputs from the LTI model using the [SIM Query Subsystem](../lvsim/sim_querysys.html) VI and the [SIM Set Parameter Value](../lvsim/sim_set_param_value.html) VI. You also use these VIs to change the value of an input or state.

First, wire a path or reference to a subsystem to the **Path** input of the SIM Query Subsystem VI. This VI returns the **States**, **Inputs**, and **Outputs** of the subsystem. Second, wire the **States**, **Inputs**, or **Outputs** parameter to the **Parameters In** input of the SIM Set Parameter Value VI. You must use one SIM Set Parameter Value VI for each parameter on which you want to operate. Use the this VI to change the LTI model in the following ways:

- Exclude an input or output from the LTI model —Set the Parameter Type of that input or output to Static . Because you cannot exclude a state from the LTI model, changing the Parameter Type of a state to Static does not change the LTI model.
- Include an input or output in the LTI model —Set the Parameter Type of that input or output to Variable .
- Change the value of an input or state that is included in the LTI model —Change the Value of that input or state. Because subsystem inputs and states influence the output, directly changing the Value of an output does not change the LTI model.

|  | Note The default Parameter Type of each state, input, and output is Variable. |
| --- | --- |

Finally, wire the modified **States**, **Inputs**, or **Outputs** parameter to the appropriate input of the SIM Linearize VI. You also must wire a path or reference to the subsystem to this VI. The resulting **State-Space Model** includes all the subsystem states and any inputs and outputs you set to Variable. The **State-Space Model** does not include any inputs and outputs you set to Static.

For example, consider a subsystem that is a nonlinear model of a car, car.vi. If you want to approximate the behavior of this model when the engine speed of the car is 50 miles per hour, linearize the model using a value of 50 mph for the engine speed parameter. Also consider any parameters you want exclude from the LTI model. For example, you generally do not need to account for gravitational acceleration in an LTI model because gravitational acceleration is a constant. The following block diagram linearizes a car model using these specifications.

[IMAGE alt='image' src='loc_bd_linearize.gif']

The example in the previous block diagram executes the following steps:

1. Obtains the value of the Inputs parameter of the car model using the SIM Query Subsystem VI. The Inputs parameter contains subsystem inputs such as engine speed and gravitational acceleration .
2. Wires the Inputs parameter to the Parameters In input of the SIM Set Parameter Value VI. This VI sets the Value of engine speed to 50 and sets the Parameter Type to Variable .
3. Wires the modified Inputs parameter to the Parameters In input of another SIM Set Parameter Value VI. This VI sets the Parameter Type of gravitational acceleration to Static . Because this example does not specify a Value for gravitational acceleration , the SIM Set Parameter Value VI does not change the value of gravitational acceleration . Therefore, the LTI model uses the default value of gravitational acceleration that the SIM Query Subsystem VI returned.
4. Wires the modified Inputs parameter to the Inputs input of the SIM Linearize VI. This VI returns an LTI model, State-Space Model , that approximates the behavior of the car model when the engine speed is 50 mph.

|  | Note You can specify the subsystem to linearize using a Path or Reference to the subsystem. Using a path to a subsystem causes the subsystem to load into memory every time a VI accesses the subsystem. Using a reference to a subsystem ensures that the subsystem loads into memory only once. |
| --- | --- |

To obtain the parameter names or parameter values for a subsystem, use the [SIM Get Parameter Names](../lvsim/sim_getpnames.html) VI or the [SIM Get Parameter Value](../lvsim/sim_get_param_value.html) VI, respectively.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_looptiming.html language=enus -->
## TOPIC 00051: Configuring the Timing of the Control & Simulation Loop (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_looptiming.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_looptiming.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Configuring the Timing of the Control & Simulation Loop (Control Design and Simulation Module)

The [Control & Simulation Loop](../lvsim/sim_simulation_loop.html) contains parameters that affect how often the simulation executes. You configure these parameters when you are running a simulation that has real-world timing needs. For example, if you are simulating a controller that must return a value every millisecond, you can configure the simulation to execute only once every millisecond. This example places a strict upper-bound on the execution of the Control & Simulation Loop; therefore, the simulation is deterministic. NI provides special real-time (RT) hardware targets you can use to ensure determinism in a simulation. In addition to an RT target, you also must install the LabVIEW Real-Time Module to execute a simulation deterministically. Refer to the NI website for information about these RT hardware targets and the Real-Time Module.

|  | Note Deterministic simulations require fixed step-size ordinary differential equation (ODE) solvers. |
| --- | --- |

You use the **Timing Parameters** page of the [Configure Simulation Parameters](../lvsim/sim_configparams.html) dialog box to configure the timing of the Control & Simulation Loop. You can use this dialog box to configure the following timing scenarios:

#### No Timing

To run a simulation without any timing restrictions, ensure the **Synchronize Loop to Timing Source** checkbox does not contain a checkmark. In this situation, the simulation runs as fast as possible. This option is appropriate for running [offline simulations](../lvsimconcepts/sim_c_config.html).

#### 1 kHz Timing on a Computer Running Windows

If you do not have an RT target available, you can simulate 1 kHz timing using a computer running Windows. To make this change, place a checkmark in the **Synchronize Loop to Timing Source** checkbox and select **1 kHz Clock** from the **Source type** list.

If you have a supported NI RT target, you also can select the **1 MHz Clock** option. If you select this option for a simulation that is running on an unsupported target, the LabVIEW Control Design and Simulation Module switches to 1 kHz timing when you run the simulation.

|  | Note You are not restricted to the 1 kHz or 1 MHz loop rates. You can use the Period control to adjust the period of the simulation as necessary. |
| --- | --- |

#### Hardware-Controlled Timing Defined by External Timing Source

To specify a rate other than 1 kHz, you can use an external timing source, such as an NI DAQ device, to control the Control & Simulation Loop. To make this change, place a checkmark in the **Synchronize Loop to Timing Source** checkbox and select **Other <defined by source name or terminal>** from the **Source type** list. Then, wire the **timing source out** output of the DAQmx Create Task VI to the **Source name** input of the Control & Simulation Loop.

|  | Note You must install NI-DAQmx™, available on the National Instruments Device Driver DVD, to use the DAQmx VIs. |
| --- | --- |

#### Hardware-Controlled Timing Defined by VIs

Instead of using an external timing source, you can use the RT hardware I/O VIs to control the timing of the Control & Simulation Loop. In this situation, you ensure the **Synchronize Loop to Timing Source** checkbox does not contain a checkmark. Then, you use a VI, such as the DAQmx Read VI, to control the timing of the Control & Simulation Loop.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_modelparamsbd.html language=enus -->
## TOPIC 00052: Tutorial: Configuring Simulation Functions and Accessing Signals in a Simulation Hierarchy (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_modelparamsbd.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_modelparamsbd.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Tutorial: Configuring Simulation Functions and Accessing Signals in a Simulation Hierarchy (Control Design and Simulation Module)

This tutorial guides you through [configuring parameters of Simulation functions](../lvsimconcepts/sim_c_modelparamsbd.html) elsewhere in a hierarchy of [Simulation](../lvsim/simulation.html) functions and subsystems. In these exercises, you configure the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function to initialize parameters of a Simulation function in a VI before the simulation runs.

#### Exercise 1: Preparing the Block Diagram

Complete the following steps to create a VI with simulation functions and a VI that edits model parameters in the simulation VI:

1. Open the SimEx Sine VI in the labview\examples\Control and Simulation\Simulation\Signal Generation directory. This example VI contains a simulation diagram with a function you can configure.
 Open example
2. Save a copy of this VI in a convenient directory that is readable and writable. Name the file SimEx Sine Test.vi .
3. Open the block diagram. In the Control & Simulation Loop , delete the frequency control and the wire that connects it to the Sine Signal function. Instead of setting the frequency of the signal through a wired terminal, you will configure the value from another VI.
4. Select File»New VI to create a blank VI. This VI will set the frequency parameter in SimEx Sine Test.vi .
5. Save the blank VI in the same directory as SimEx Sine Test.vi .
6. Add the Access Model Hierarchy function to the block diagram of the blank VI.
 [IMAGE alt='image' src='add.gif'] Add

#### Exercise 2: Identifying Which Model Parameters to Update

Complete the following steps to configure the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function to access a particular model parameter in the simulation VI:

1. Double-click the Access Model Hierarchy function to open its configuration dialog box.
2. In the VI with Simulation text box, enter the location on disk of SimEx Sine Test.vi . 
 [IMAGE alt='image' src='tip.gif']
**Tip** If the VI is still open, click the **Select VI in memory** button to select that VI as the **VI with Simulation**.
3. In the Accessors list, click accessor 1 to make its name editable and enter the name freq_accessor . This list corresponds to terminals on the Access Model Hierarchy function.
4. In the bottom half of the dialog box, select Sine Signal in the Select a function or subsystem list.
5. In the Select a parameter or signal list, select the frequency item. The Source column for this item reads Unwired Terminal to indicate the frequency parameter does not have another source. The Access Model Hierarchy function can write only to parameters that are unwired or configured.
6. Note that the path to the frequency parameter you selected automatically appears in the Path to model parameter or signal text box. Also, note that the Get/Set option is configured to set the value of the frequency parameter rather than to read its value.
7. (Optional) In the Parameter Value section, change the value of the frequency control. You also can set the value of model parameters from a block diagram terminal.

The following dialog box for the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function shows the configuration from this exercise.

[IMAGE alt='image' src='loc_bd_tut_config1.gif']

#### Exercise 3: Identifying Which Signals to Collect

Complete the following steps to configure the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function to return signal values from the simulation VI:

1. Beside the Accessors list, click the add button to create a new accessor through which the Access Model Hierarchy function will return the signal value.
2. Click the new accessor to make its name editable and enter the name sine_sig_accessor .
3. In the bottom half of the dialog box, select Sine Signal in the Select a function or subsystem list.
4. In the Select a parameter or signal list, select the output item. The Source column for this item reads Signal to indicate the item corresponds to a wire in the simulation diagram in which it resides. The Access Model Hierarchy function can return only signals on wires.
5. Note that the path to the output parameter you selected automatically appears in the Path to model parameter or signal text box.
6. Click OK , which displays a popup dialog about configuring a collection period. You will complete this task in Exercise 4 so LabVIEW can collect signal values.

On the block diagram, the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function, shown as follows, is configured to perform the following tasks:

- Write to the frequency model parameter of the Sine Signal function in SimEx Sine Test.vi .
- Read and return signal values from the output terminal of the same function.

[IMAGE alt='image' src='loc_bd_tut_getset1.gif']

#### Exercise 4: Updating the Model Parameter and Collecting Signal Values at Run Time

Complete the following steps to set the frequency parameter of the [Sine Signal](../lvsim/sim_sinewave.html) function and collect the signal it generates as the simulation runs:

1. On the block diagram that contains the Access Model Hierarchy function, right-click the value input for the Sine Signal.frequency accessor and select Create»Control from the shortcut menu.
2. Enter a value of 3 in the Sine Signal.frequency control from step 1.
 This concludes the preparation for setting the frequency parameter.
3. Right-click the value output for the Sine Signal.output accessor and select Create»Indicator .
4. Return to the block diagram of SimEx Sine Test.vi . Though you identified signal to collect with the Sine Signal.output accessor, you still must specify how often to collect signal values .
5. Double-click the Input Node of the Control & Simulation Loop to display the Configure Simulation Parameters dialog box.
6. In the Signal Collection section, set the Decimation control to 1, which means LabVIEW collects a value at every time step. By default, the decimation period is 0, which means LabVIEW does not collect any values.
7. Click OK to return to the block diagram.
 This concludes the preparation for collecting signal values.
8. Run SimEx Sine Test.vi and observe the simulated signal in the waveform chart.
9. Run the VI that contains the Access Model Hierarchy function and observe the change to the signal frequency in the waveform chart of SimEx Sine Test.vi . Note the signal value collected and displayed in the Sine Signal.output indicator.

You can [use this function in other types of applications](../lvsimconcepts/sim_c_modelparamsbd.html), such as to access parameters and signals in the same VI as the [Access Model Hierarchy](../lvsim/sim_readwriteparams.html) function and to access these items in a simulation that runs on an RT target.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_modtransfer.html language=enus -->
## TOPIC 00053: Transferring Linear Model Definitions between Functions (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_modtransfer.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_modtransfer.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Transferring Linear Model Definitions between Functions (Control Design and Simulation Module)

If you [define a model interactively](../lvsimhowto/sim_h_linmodint.html), you can transfer that model definition to another linear model function using the following two methods:

- Use the Copy to Clipboard and Paste from Clipboard buttons in the configuration dialog box. After defining a model, click the Copy to Clipboard button to copy that definition to the clipboard. Then, place another linear model function on the simulation diagram, display the configuration dialog box for that function, and click the Paste from Clipboard button.
- Use the Save Model and Load Model buttons in the configuration dialog box. After defining a model, click the Save Model button to save that definition to a data file. Then, place another linear model function on the simulation diagram, display the configuration dialog box for that function, and click the Load Model button to specify the data file you saved. Use this method to transfer a model definition to another computer.

The following rules apply when transferring model definitions between functions.

- If you transfer a single-input single-output (SISO) model definition to a multiple-input multiple-output (MIMO) Simulation function or vice versa, the LabVIEW Control Design and Simulation Module populates only the first input-output pair of the target Simulation function.
- You cannot transfer model definitions to another model form. For example, if you save a transfer function model definition to a data file, you cannot load that data file into a State-Space function.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_ode.html language=enus -->
## TOPIC 00054: Specifying and Configuring a Solver (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_ode.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_ode.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Specifying and Configuring a Solver (Control Design and Simulation Module)

For a given simulation, you must specify and configure the [ordinary differential equation](/csh?topicname=lvanlsconcepts/solving_odes.html) (ODE) or [differential algebraic equation](/csh?topicname=lvanlsconcepts/solving_daes.html) (DAE) solver.

Complete the following steps to specify and configure the solver for a simulation:

1. Double-click the Input Node of the Control & Simulation Loop to launch the Configure Simulation Parameters dialog box.
2. In the ODE Solver pull-down menu, select the ODE or DAE solver for the simulation.
 [IMAGE alt='image' src='note.gif']
**Note** Solvers have various strengths and weaknesses. [Choose a solver that is appropriate](../lvsimconcepts/sim_c_ode.html) for the model and application.
3. (Optional) Configure the options available for the solver. If you specify a fixed step-size solver, you can configure only the Step Size (s) option. If you specify a variable step size solver, indicated by the term (variable) next to the solver name, you can configure options that define the step sizes, tolerance, and so on.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_optcasestudy.html language=enus -->
## TOPIC 00055: Case Study: Designing a PID Controller for a Second-Order System (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_optcasestudy.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_optcasestudy.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Case Study: Designing a PID Controller for a Second-Order System (Control Design and Simulation Module)

This section examines the PID Design for Second Order Continuous System VI, which determines the optimal gain values *K*<sub>P</sub>, *K*<sub>I</sub>, and *K*<sub>D</sub> for a proportional-integral-derivative (PID) controller in a second-order continuous dynamic system. This VI is located in the labview\examples\Control and Simulation\Simulation\Optimal Control Design directory.

The following illustration shows the block diagram of this VI.

[IMAGE alt='image' src='bd_opt_pid.gif']

This VI [constructs a dynamic system model](../lvsimconcepts/sim_c_constrmdl.html) using the [SIM Construct Default System](../lvsim/sim_constrsys.html) VI. In this example, the dynamic system has only three components: a controller C, a plant G1, and a reference input signal ***r***. The [SIM Optimal Design](../lvsim/sim_optimal_design_vi.html) VI excites the dynamic system with the reference input signal to determine the optimal settings for the controller.

The following transfer function equation defines the plant G1.

[IMAGE alt='image' src='eq_system.gif']

The following illustration shows the **System Matrices** control that represents this equation.

[IMAGE alt='image' src='fp_opt_pid_g1.gif']

The **Signal Parameters Array** parameter of the SIM Construct Default System VI specifies the reference input signal ***r*** that excites this system. This example excites the dynamic system with a step input signal. The following illustration shows this parameter.

[IMAGE alt='image' src='fp_opt_pid_rt.gif']

|  | Note Notice in the previous illustration that r is the third element, or index number 2, of the Signal Parameters Array. ru and ry correspond to the first and second elements of this array, respectively. If you define a custom dynamic system, you also can define custom reference signals beginning with the third element of this array. |
| --- | --- |

The following illustration shows the **Problem Specification** parameter of the SIM Optimal Design VI.

[IMAGE alt='image' src='fp_opt_pid_spec.gif']

The **System response type** parameter in the previous illustration shows this example optimizes parameters for the controller C. The **Inequality constraints type** parameter shows this example uses the default calculations for the inequality constraint envelopes. The **Cost type** parameter shows this example minimizes the linear quadratic (LQ) cost function. The following equation shows this [cost function](../lvsim/sim_optimal_design_vi.html#functypes) *J<sub>LQ</sub>*.

[IMAGE alt='image' src='eq_jlq.gif']

The **Weights for cost function** parameter in the previous illustration shows this example uses the following weight matrix ***W***:

[IMAGE alt='image' src='eq_w.gif']

This weight matrix penalizes the control action *u*(*t*) but emphasizes that this example minimizes the position error *e*(*t*). ***W*** also reflects the difference in scale between the control action range and the output range.

The following illustration shows the **Inequality Constraints** parameter that defines the inequality constraints envelopes.

[IMAGE alt='image' src='fp_opt_pid_constr.gif']

The upper constraint envelope on the output is a line with points (0, 1.25) and (10, 1.05). The lower constraint envelope on the output has points (0, 0), (1.5, 0), and (10, 0.95). The following illustration shows these envelopes.

[IMAGE alt='image' src='loc_fp_output_constr.gif']

The following illustration shows the constraints on the control action. The upper constraint envelope is a line with points (0, 75) and (10, 20). The lower constraint envelope is a line with points (0, –75) and (10, –25).

[IMAGE alt='image' src='loc_fp_ctrl_constr.gif']

This example does not place inequality constraints on either the rate of control action or the rate of output.

The following illustration shows the parameter bounds this example uses for each gain parameter of the PID controller.

[IMAGE alt='image' src='fp_opt_pid_bounds.gif']

These bounds form the parameter space in which this example searches for optimal values.

The following illustration shows the initial parameter values this example uses. Each element of this array corresponds to the same element of the **Parameter Bounds** array.

[IMAGE alt='image' src='fp_opt_pid_init.gif']

This example uses an initial parameters mesh to generate two additional search locations quasi-randomly. The following illustration shows this **Initial Parameters Mesh**.

[IMAGE alt='image' src='fp_opt_pid_mesh.gif']

When you run this VI, the SQP algorithm executes once using the values from the **Initial Parameters** parameter. The algorithm then executes two more times, using the **Initial Parameters Mesh** parameter to generate two sets of initial parameter values.

The following illustration shows all three sets of initial parameter values.

[IMAGE alt='image' src='fp_opt_pid_initsqp.gif']

The first row of the following illustration is the same as the values shown in the **Initial Parameters** parameter. The second and third rows contain quasirandomly-generated locations within the **Parameter Bounds** of each parameter.

|  | Note The Array of Initial Parameters parameter is on the Debug Information page of the SIM Optimal Design VI. |
| --- | --- |

After the SQP algorithm executes, this VI returns all possible optimal parameter values, as shown in the following illustration.

[IMAGE alt='image' src='fp_opt_pid_optparams.gif']

Of the parameter value sets shown in the previous illustration, one set minimizes the LQ cost function. The SIM Optimal Design VI returns this optimal set of parameter values in the **Design parameters** array. The following illustration shows this array and the corresponding value of the cost function.

[IMAGE alt='image' src='fp_opt_pid_desparams.gif']

Therefore, the optimal gain values for *K*<sub>P</sub>, *K*<sub>I</sub>, and *K*<sub>D</sub>are 14.7257, 11.2553, and 0.203472, respectively.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_reinput.html language=enus -->
## TOPIC 00056: Removing and Rearranging Control & Simulation Loop Inputs (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_reinput.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_reinput.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Removing and Rearranging Control & Simulation Loop Inputs (Control Design and Simulation Module)

You can use two methods to remove unwired inputs from the Input Node. The first method you can use is resizing the node. Click and drag the resize handle at the bottom of the node up to remove unwired inputs from the node.

The second method you can use is removing individual unwired inputs. To remove the last unwired input on the Input Node, right-click the node and select **Remove Input** from the shortcut menu.

You also can rearrange the order of unwired inputs on the Input Node. Right-click an input and select **Select Input** from the shortcut menu to view a list of inputs. The top half of this list contains the inputs currently displayed on the Input Node. The input on which you right-clicked has a checkmark by it. Select an input from the top half of the list to switch the positions of the inputs. The bottom half of this list contains the inputs not currently displayed on the Input Node. Select an input from the bottom half of the list to replace the selected input with the input you select.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_reversing.html language=enus -->
## TOPIC 00057: Reversing Function Icons (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_reversing.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_reversing.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Reversing Function Icons (Control Design and Simulation Module)

You can reverse [Simulation](../lvsim/simulation.html) functions to better display the data flow of an entire feedback system, as shown in the following block diagram:

[IMAGE alt='image' src='loc_bd_reverse_icons.gif']

To reverse a Simulation function, right-click the icon and select **Reverse Terminals** from the shortcut menu.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_stopprog.html language=enus -->
## TOPIC 00058: Stopping a Simulation Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_stopprog.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_stopprog.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Stopping a Simulation Programmatically (Control Design and Simulation Module)

Use the [Halt Simulation](../lvsim/sim_haltsimulation.html) function to stop a simulation programmatically. Place this function on the simulation diagram and wire a Boolean control to the **Halt?** input. If the **Halt?** Boolean control is TRUE, the function stops the simulation after the current time step. You also can place a Halt Simulation function in a simulation subsystem to stop the execution of the parent simulation diagram. The Halt Simulation function operates like the conditional terminal on a [While Loop](/csh?topicname=glang/while_loop.html). However, you can place more than one Halt Simulation function on the simulation diagram. With multiple Halt Simulation functions, you can stop the simulation from various points in a simulation diagram or subsystem.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_subsysft.html language=enus -->
## TOPIC 00059: Defining the Feedthrough Behavior of Subsystems (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_subsysft.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_subsysft.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Defining the Feedthrough Behavior of Subsystems (Control Design and Simulation Module)

LabVIEW flattens the hierarchy of a [simulation subsystem](../lvsimconcepts/sim_c_subsys.html) when you run that subsystem. This flattened hierarchy means Simulation functions inside a simulation subsystem can execute when that function receives all the inputs that function uses, even if the subsystem did not receive all the inputs the subsystem uses. A simulation subsystem saves a feedthrough mapping from all inputs to all outputs. If a subsystem input does not depend on the subsystem output at the current time step, you can use the subsystem as an indirect feedthrough function in a [feedback cycle](../lvsimconcepts/sim_c_feedthrough.html).

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_subsyssa.html language=enus -->
## TOPIC 00060: Creating a Simulation Subsystem (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_subsyssa.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_subsyssa.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Creating a Simulation Subsystem (Control Design and Simulation Module)

You can create a [simulation subsystem](../lvsimconcepts/sim_c_subsys.html) from a selection of the simulation diagram. In this situation, LabVIEW automatically [creates a connector pane](/csh?topicname=lvconcepts/building_connector_pane.html) for the subsystem inputs and outputs. A connector pane is required if you want to connect that simulation subsystem to inputs and outputs [within another Control & Simulation Loop](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_in_a_simulation_loop) or on a block diagram [outside a Control & Simulation Loop](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_outside_a_simulation_loop). However, you can run a simulation subsystem [as a stand-alone VI](../lvsimconcepts/sim_c_subsys.html#running_a_subsystem_as_a_stand-alone_vi) without creating a connector pane.

You also can create a new simulation subsystem to run as a stand-alone VI. If you want, you can create a connector pane for this subsystem later.

|  | Note You cannot use local variables in a simulation subsystem. |
| --- | --- |

#### Creating a Simulation Subsystem from a Selection on the Simulation Diagram

Complete the following steps to create a simulation subsystem and connector pane simultaneously.

1. Launch LabVIEW and create a new, blank VI.
2. Place a Control & Simulation Loop on the block diagram. [IMAGE alt='image' src='add.gif'] Add
3. Create the simulation diagram code and configure simulation parameters using the Configure Simulation Parameters dialog box.
4. Select a portion of the simulation diagram code and select Edit»Create Simulation Subsystem . LabVIEW replaces the code you selected with a single function that represents the simulation subsystem. The function shows the block diagram of the simulation subsystem.
5. Run the subsystem by running the VI that contains the subsystem.

When you create a subsystem using the above method, the LabVIEW Control Design and Simulation Module automatically creates a connector pane and configuration dialog box for the simulation subsystem. To display this configuration dialog box, double-click the subsystem on the block diagram. To edit the front panel window or block diagram window of the subsystem, right-click the subsystem and select **Open Subsystem** from the shortcut menu.

#### Creating a New Simulation Subsystem

Complete the following steps to create a simulation subsystem without a connector pane.

1. Launch LabVIEW.
2. Select File»New .
3. Select Other Files»Simulation Subsystem from the Create New tree.
4. Click the OK button. LabVIEW creates a new, blank VI with a pale yellow block diagram, which is the simulation diagram.
5. Create the simulation diagram code and configure simulation parameters. Because this new subsystem has no Control & Simulation Loop, you configure simulation parameters, such as the ordinary differential equation(ODE) solver , by selecting Operate»Configure Simulation Parameters .
 You also can configure properties that affect how this subsystem appears and runs. To configure these properties for a stand-alone subsystem, select File»VI Properties to display the VI Properties dialog box.
6. Save the simulation subsystem.

|  | Note You also can create a new simulation subsystem by displaying the Project Explorer window, right-clicking a target, and selecting New»Simulation Subsystem from the shortcut menu. |
| --- | --- |

You now can run this simulation subsystem as a stand-alone VI. You also can [place this subsystem](/csh?topicname=lvhowto/adding_subvis_to_block_dia.html) within the Control & Simulation Loop of another VI or on the block diagram outside a Control & Simulation Loop. However, before doing so, you must [build a connector pane](/csh?topicname=lvconcepts/building_connector_pane.html) for the subsystem. The connector pane defines the relationships between block diagram terminals and subsystem inputs and outputs. After you define a connector pane for a subsystem, the Control Design and Simulation Module creates a configuration dialog box for that subsystem.

As you create the connector pane, consider the parameter requirements and the initial value of each parameter. The default source for a subsystem parameter depends on whether you specify that parameter as required, recommended, or optional. The initial value for the parameter is the default value of the parameter control.

The following list describes the availability and default sources of parameters.

- If the connection is required, the parameter is available only as a terminal on the simulation diagram. The parameter is not visible in the configuration dialog box.
- If the connection is recommended, the default source of the parameter is the terminal. You also have the option to configure the parameter using the configuration dialog box.
- If the connection is optional, the default source of the parameter is the configuration dialog box. You also have the option to configure the parameter using a terminal on the simulation diagram.

#### Creating Enabled and Triggered Subsystems

Enabled and triggered subsystems execute only when certain conditions are met. You can configure subsystems to be enabled, triggered, or both. Complete the following steps to create a subsystem that is both enabled and triggered.

1. Double-click the subsystem to display the Subsystem Configuration dialog box.
2. From the Parameters list, select Execution Control . The Parameter Information section displays options for configuring the execution of the subsystem.
3. From the Execution Control pull-down menu, select Enable And Trigger .
4. Select a Trigger Type . This option specifies the direction in which the input signal to the subsystem must cross 0 to trigger the subsystem.
5. (Optional) Specify a Trigger Offset value to specify a value other than 0 that the input signal must cross to trigger the subsystem.
6. Select an output of the subsystem from the Parameters list to display configuration options for the output.
7. Select a Disabled Behavior . If you select Hold , the output returns its last known value, which on first execution is the initial value of the subsystem. If you select Reset , the output resets to its initial value or a default value you specify, depending on whether you enable the Use Configured Default Value option.
8. (Optional) Place a checkmark in the Use Configured Default Value checkbox to enable the **output name** field and enter a default value for the output to return if the subsystem does not execute.
9. Repeat steps 6–8 for all the outputs of the subsystem.
10. Click the OK button to close the Subsystem Configuration dialog box and apply the execution control settings. Notice that the subsystem now includes Enable and Trigger inputs. The values you wire to these inputs determine whether the subsystem executes.

#### Creating Polymorphic Subsystems

To create a [polymorphic subsystem](../lvsimconcepts/sim_c_subsys.html#poly), you must have two or more subsystems with identical [connector pane patterns](/csh?topicname=lvhowto/selecting_a_connector_pane.html). Each subsystem should handle a different data type. You then create a [single polymorphic VI](/csh?topicname=lvconcepts/polymorphic_vis.html) that points to these subsystems.

|  | Note Consider naming these VIs on disk to make choosing subsystems easier. LabVIEW convention is to have the data type, or other useful polymorphic information, in parentheses after the VI name. For example, if you have two subsystems, one that operates on a double-precision floating point number and one that operates on a 16-bit integer, you could rename the subsystems to Perform Operation (Double) and Perform Operation (Integer), respectively. LabVIEW uses the contents of these parentheses if you do not explicitly specify an instance name when creating a polymorphic subsystem. |
| --- | --- |

After you create these subsystems, complete the following steps to create a polymorphic subsystem.

1. Select File»New to display the New dialog box.
2. Select VI»Polymorphic VI from the Create New tree. The Polymorphic VI window appears.
3. Click the Add button and select a simulation subsystem to add to the polymorphic VI. Repeat this step for as many simulation subsystems as you want to add. Each subsystem must have an identical connector pane pattern. 
 [IMAGE alt='image' src='note.gif']
**Note** The polymorphic VI breaks if you add a VI that is not a simulation subsystem, a simulation subsystem with a different connector pane pattern, or a simulation subsystem that is broken.
4. Remove, rename, and rearrange the instances as needed.
5. Select File»Save to save the polymorphic VI. You now can place this subsystem within the Control & Simulation Loop of another VI or on the block diagram outside a Control & Simulation Loop.

After you place the polymorphic subsystem on the simulation diagram or block diagram, you can perform the following actions:

- Display the Polymorphic VI window —Right-click the polymorphic subsystem and select Open Polymorphic VI from the shortcut menu.
- Display the configuration dialog box of the currently displayed subsystem —Double-click the polymorphic subsystem. Notice the Polymorphic instance pull-down menu contains the names you specified for each instance.
- Edit the currently displayed subsystem —Right-click the polymorphic subsystem and select Open Subsystem from the shortcut menu.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_h_trimprog.html language=enus -->
## TOPIC 00061: Trimming a Subsystem Programmatically (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_h_trimprog.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_h_trimprog.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Trimming a Subsystem Programmatically (Control Design and Simulation Module)

Use the [SIM Trim](../lvsim/sim_trim_vi.html) VI to trim a continuous simulation subsystem. By default, this VI trims a subsystem to a steady state in which all state derivatives are zero. By default, this VI does not specify any conditions and includes all inputs and states in the search. You can use the [SIM Query Subsystem](../lvsim/sim_querysys.html) VI and the [SIM Set Parameter Value](../lvsim/sim_set_param_value.html) VI to change the behavior of SIM Trim VI in the following ways:

- Trim a subsystem to a transient state —Specify a non-zero Value for one or more state derivatives. You also must set the Parameter Type of these state derivatives to Fixed .
- Specify one or more state, input, and/or output conditions —Specify a Value for one or more states, inputs, and/or outputs. You also must set the Parameter Type of these states, inputs, and/or outputs to Fixed .
- Change the initial search location —Specify a Value for one or more states, inputs, and/or outputs. The values of these parameters form the location at which the SIM Trim VI begins the search. You also must set the Parameter Type of these states, inputs, and/or outputs to Variable .
- Exclude a state and/or input from the search —Specify a Value for each input and/or state that you want to exclude. You also must set the Parameter Type of these states and/or inputs to Static .

For example, consider a car model car.vi that contains car position as a state. The car model has a cruise-control system that must set the position of the accelerator to maintain forward movement at a specified velocity. You can specify the velocity of the car using the derivative of car position. The following block diagram trims the car model using a specified velocity of 60 miles per hour.

[IMAGE alt='image' src='loc_bd_trim.gif']

The example in the previous block diagram executes the following steps:

1. Obtains the value of the State Derivatives parameter of the car model using the SIM Query Subsystem VI. The State Derivatives parameter contains car position , which is equivalent to the velocity of the car.
2. Wires the State Derivatives parameter to the Parameters In input of the SIM Set Parameter Value VI. This VI sets the Value of car position to 60 . The Parameter Type of car position is Fixed , which indicates this parameter is a condition that the SIM Trim VI must satisfy. This VI must return values of states and inputs that keep the velocity of the car at 60 mph.
3. Wires the modified State Derivatives parameter to the State Derivatives input of the SIM Trim VI. This VI returns the Trimmed Inputs and Trimmed States parameters that the cruise-control system must use to maintain a velocity of 60 mph. This VI also returns the Trimmed Outputs and Trimmed State Derivatives parameters that the car model returns when the cruise-control system uses the values of the Trimmed States and Trimmed Inputs parameters.

|  | Note If the SIM Trim VI cannot satisfy all specified conditions, this VI returns the closest values to the specified conditions. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_simulate_emi.html language=enus -->
## TOPIC 00062: Simulating External Models (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_simulate_emi.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_simulate_emi.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Simulating External Models (Control Design and Simulation Module)

LabVIEW users can use the [External Model Interface](../lvsimconcepts/sim_using_emi.html) (EMI) to simulate an external, or third-party, model in the LabVIEW Control Design and Simulation Module. Use the [External Model](../lvsim/sim_external_model.html) function to represent and simulate the model. Refer to the [Example 2: Simulating an External Model](../lvsimhowto/sim_emi_example2.html) topic for an example of simulating an external model.

Complete the following steps to simulate an external model.

1. Create a new VI.
2. Add a Control & Simulation Loop to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
3. Add an External Model function to the block diagram inside the Control & Simulation Loop.
 [IMAGE alt='image' src='add.gif'] Add
4. In the Select an External Model Library dialog box that appears, browse to the shared library corresponding to the model you want to simulate.
 [IMAGE alt='image' src='note.gif']
**Note** If you reference an invalid shared library, the [Select an External Model Library](../lvsim/sim_select_emlib_db.html) dialog box returns an error.
5. If the model requires model configuration parameters, enter the parameters in the Configuration parameters text box. Refer to the documentation for the external model, if available, for more information about required model configuration parameters.
6. Click the OK button to close the Select an External Model Library dialog box. The External Model function now represents the model corresponding to the shared library you selected. You can configure the External Model function as you do other Simulation functions.

If the shared library you reference from an External Model function changes, right-click the External Model function and select **Relink to External Model Library** from the shortcut menu to reference the modified shared library. If you want to reference a different shared library from the External Model function, right-click the External Model function and select **Select External Model Library** from the shortcut menu to display the [Select an External Model Library](../lvsim/sim_select_emlib_db.html) dialog box. Then select the new shared library you want to reference.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsimhowto/sim_using_esi.html language=enus -->
## TOPIC 00063: Using an External Solver (Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsimhowto/sim_using_esi.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsimhowto/sim_using_esi.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Using an External Solver (Control Design and Simulation Module)

You can use the [External Solver Interface](../lvsimhowto/sim_using_esi.html) to [create](../lvsimhowto/sim_esi_create.html) and use external solvers in the LabVIEW Control Design and Simulation Module. When you create an external solver, you can use the solver for any [simulation subsystem](../lvsimhowto/sim_h_subsyssa.html).

Complete the following steps to use an external ODE solver in the Control Design and Simulation Module.

1. Create a new VI.
2. Add a Control & Simulation Loop to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
3. Double-click the Input Node of the Control & Simulation Loop to launch the Configure Simulation Parameters dialog box.
4. In the Solver Method section, select the external solver from the ODE Solver pull-down menu. [IMAGE alt='image' src='note.gif']
**Note** When you create the external ODE solver, use the [Information](../lvsimesi/esi_information.html) function to specify the name of the solver that appears in the **ODE Solver** pull-down menu.
5. (Optional) Set the Simulation Time and the Continuous Time Step and Tolerance or Discrete Time Step settings.
6. Click the OK button to select the external solver for the simulation subsystem. [IMAGE alt='image' src='note.gif']
**Note** If you configure a VI to use an external solver and then run the VI on a computer without the external solver installed, errors might occur. Ensure the shared library file for the external solver is in the labview\vi.lib\Simulation\ContinuousLinear\Implementation\Shared\Solvers\Plugins directory.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/acquiring_data.html language=enus -->
## TOPIC 00064: Acquiring Data from a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/acquiring_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/acquiring_data.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Acquiring Data from a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The first step in identifying an unknown system is acquiring data. You can acquire dynamic system data by using NI DAQ hardware and software or you can use data from a file on disk. You can acquire data in the time domain and/or the frequency domain. You must acquire the input and output data of the system synchronously and save synchronous input and output data with constant time steps. If the input data and the output data are not synchronous, you cannot use the data to identify an unknown system.

For verification and validation reasons, you must acquire two sets of input-output data samples or split the data into two sets. You use one set of samples to estimate the mathematical model of the system. You use the second set of samples to [validate](validating_models.html) the resulting model. If the resulting model does not meet the predefined specifications, such as the mean square error (MSE), modify the settings and re-verify the resulting model with the data sets.

Identifying a system involves a number of choices with regard to the system output signals you want to measure and the input signals you want to manipulate. The choices you make about how to manipulate system inputs, types of signal conditioning, signal ranges, and sampling behavior affect the validity of the model you obtain. You can use different modeling techniques on the same experimental data set. However, if the data set does not reflect the behavior of interest, you must acquire a more descriptive data set.

Because the system identification process is often an experimental process, the entire process often is time consuming and possibly costly. Therefore, you must think about the design of process prior to experimenting with various identification techniques.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/analyzing_models.html language=enus -->
## TOPIC 00065: Analyzing Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/analyzing_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/analyzing_models.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Analyzing Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can use model analysis to observe some characteristics, such as [frequency response](si_frequency_response.html), stability, and order, of dynamic system models. Use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to analyze the dynamic system models and present the results in [Bode plot](#bode_plot), the [Nyquist plot](#nyquist_plot), and the [pole-zero plot](#pole-zero_plot) graphs.

Refer to the Model Presentation VI in the labview\examples\System Identification\Getting Started\General.llb for an example that demonstrates how to use the [SI Bode Plot](../lvsysid/bode_plot.html), [SI Nyquist Plot](../lvsysid/nyquist_plot.html), and [SI Pole-Zero Plot](../lvsysid/zeros_poles_plot.html) VIs to compute the Bode, Nyquist, and pole-zero plots, respectively, of an system model.

#### Bode Plot

A Bode plot contains a Bode magnitude plot and a Bode phase plot. These two plots together describe the frequency response of the dynamic system model you estimate. A Bode magnitude plot describes magnitude versus frequency. A Bode phase plot describes phase versus frequency. The following figure shows an example of a Bode plot.

[IMAGE alt='image' src='bode_plot_with_sample_data.gif']

The SI Bode Plot VI calculates the upper and lower limits according to the confidence level you set. You can obtain information, such as the gain of the system and the cutoff frequency, by evaluating the Bode plot. You can display the Bode magnitude and phase using the [SI Bode Plot Indicator](../lvsysid/si_bode_indicator.html).

#### Nyquist Plot

A Nyquist plot describes the gain and phase of a frequency response in polar coordinates by plotting the imaginary part of the complex frequency response versus the real part. In polar coordinates, a Nyquist plot shows the phase as the angle and the magnitude as the distance from the origin. You can use the Nyquist plot to predict the stability of a system. The following figure shows an example of a Nyquist plot.

[IMAGE alt='image' src='nyquist_plot_with_sample_data.gif']

The SI Nyquist Plot VI calculates the upper and lower limits according to the confidence level you set. You can use the SI Nyquist Plot VI to generate the Nyquist plot and display this plot by using the [SI Nyquist Plot Indicator](../lvsysid/si_nyquist_indicator.html).

#### Pole-Zero Plot

The pole-zero plot displays the poles and zeros of a system. By observing the locations of the poles and zeros, you can conclude whether the system is stable. In a stable system, all poles are within the unit circle. The following figure shows a pole-zero plot of a stable model.

[IMAGE alt='image' src='pole_zero_plot_with_sample_data.gif']

You can use the SI Pole-Zero Plot VI to generate a pole-zero plot and display the plot by using the [SI Pole-Zero Plot Indicator](../lvsysid/si_pole_zero_indicator.html).

You also can use the pole-zero plot to determine if you can reduce model orders. By observing the pole-zero placements, you can determine if any pole-zero pairs have overlapping confidence intervals. A confidence interval is a region the SI Pole-Zero Plot VI calculates from the confidence level you set. The existence of overlapping confidence intervals implies that pole-zero cancellations exist and that the model order might be unnecessarily high. The pole-zero plot shown in the previous figure is an optimal model with the appropriate order because the pole-zero pairs do not have overlapping confidence intervals.

If the model order is too high, you can try reducing the model order. You then can use the F-test criterion to assess if the reduction in model order leads to a significant increase in the prediction error. If the reduction in model order leads to a significant increase in the prediction error, do not reduce the model order.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/anlz_valid_conv.html language=enus -->
## TOPIC 00066: Analyzing, Validating, and Converting Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/anlz_valid_conv.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/anlz_valid_conv.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Analyzing, Validating, and Converting Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After estimating a model of a dynamic system, you can observe model characteristics by [analyzing the model](analyzing_models.html). You also can verify that the model represents the dynamic system by [validating the model](validating_models.html). Use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to analyze and validate models.

According to linear system theory, you can represent a linear system with different models. Each [model representation](model_types_and_reps.html#model_reps) has benefits and drawbacks for characterizing a dynamic system. Certain model representations are more suitable for certain analysis techniques. You can use the System Identification VIs to [convert models](converting_models.html) from one representation to another to identify the best-fit model for the system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/anti-aliasing_filter.html language=enus -->
## TOPIC 00067: Applying an Anti-Aliasing Filter (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/anti-aliasing_filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/anti-aliasing_filter.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Applying an Anti-Aliasing Filter (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

According to the Nyquist sampling theorem, the sampling rate must be greater than twice the maximum frequency component of the signal of interest. In other words, the maximum frequency of the input signal must be smaller than half the sampling rate. For example, if the maximum frequency component of a signal is 1K Hz, the sampling rate must be greater than 2K Hz. In real-world applications, you can set the sampling rate between 3K and 5K Hz.

This criterion, in practice, is often difficult to ensure. Even if you are sure that the measured signal has an upper limit on its frequency, external factors, such as signals from the powerline interference or radio stations, can contain frequencies higher than the Nyquist frequency. These frequencies might then alias into the frequency range of interest and give you inaccurate results.

To ensure that you limit the frequency content of the input signal, you can add a lowpass filter before the sampler and the analog to digital converter (ADC). A lowpass filter passes low frequencies and attenuates high frequencies. This filter is an anti-aliasing filter because by attenuating the frequencies greater than the Nyquist frequency, the filter prevents the sampling of aliased components. When you use a filter before the sampler and ADC, the anti-aliasing filter is an analog filter with a proper cut-off frequency. The cut-off frequency equals the maximum frequency component of the signal of interest. Using the anti-aliasing filter satisfies the Nyquist sampling theorem. You must have data acquisition hardware that supports anti-aliasing filters to use this filter.

Similarly, you can use a digital filter to remove frequency content above the system bandwidth and then [downsample](filt_downsampling.html) the data to the desired sampling rate.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/case_study_estimating.html language=enus -->
## TOPIC 00068: Estimating an ARX Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/case_study_estimating.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/case_study_estimating.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Estimating an ARX Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

One of the biggest challenges in model estimation is selecting the correct model and the order of the model. The [System Identification](../lvsysid/lv_sysid_pal.html) VIs support three different criteria to aid in the estimation of the order of a model.

- Final Prediction Error (FPE) Criterion
- Akaike's Information Criterion (AIC)
- Minimum Description Length (MDL) Criterion

Sometimes the results you obtain with these three criteria might be inconsistent. You can use a [pole-zero plot](analyzing_models.html#pole-zero_plot) for further investigation and to verify the results of the order estimation.

The following figure shows a prediction error plot generated by the [SI Estimate Orders of System Model](../lvsysid/est__orders_system_model.html) VI for an [ARX](modeldefinitionsarx.html) model. The y-axis is the prediction error and the x-axis is the model dimension. The three different color bars on the chart represent the FPE, AIC, and MDL criteria.

[IMAGE alt='image' src='order_est_fp.gif']

You can use the AIC, MDL, and a [user-defined criterion](#user-defined_criterion) to determine the A and B orders of the ARX model.

#### Akaike's Information Criterion

The following block diagram uses the SI Estimate Orders of System Model VI for order estimation. To estimate the orders of a model, the SI Estimate Orders of System Model VI requires two data sets—one for estimation and one for validation. You do not need to acquire two data sets from a system, rather, you can partition one data set into two using the [SI Split Signals](../lvsysid/si_split_signal.html) VI. The SI Split Signals VI divides the preprocessed data samples into a portion for model estimation and a portion for model validation.

In the following figure, the **1st portion (%)** is 66, which means the SI Estimate Orders of System Model VI will use 66% of the data samples for estimation and the remainder of the data samples for validation.

[IMAGE alt='image' src='order_est_bd.gif']

The SI Estimate Orders of System Model VI generates the **prediction error** plot for the ARX model and the optimal A order and B order based on the AIC criterion. By using the AIC criterion, the lowest prediction error corresponds to a model dimension of 19, as shown in the **prediction error** plot. For an ARX model, the model dimension is equal to the sum of the A order, B order, and delay values. The SI Estimate Orders of System Model VI returns the following optimal orders:

- A order = 9
- B order = 10
- delay = 0

#### Verifying the Results

After determining the orders of the model, you want to verify the results to ensure the model accurately describes the system. One method is to plot a pole-zero map and [visually inspect](visual_inspection.html) the plot to determine whether there is any redundancy in the data. If a pole and a zero overlap, the pole and zero cancel out each other, which indicates the estimated optimal order is too high.

The **pole-zero plot** graph in the following figure shows a pole-zero plot with three overlapping pole-zero pairs. Due to numerical error, it is unlikely that a zero and a pole perfectly overlap. You can use the confidence region to justify whether the pole and the zero cancel out each other.

[IMAGE alt='image' src='pole-zero_plot_fp.gif']

Because there are three pole-zero pairs, you can conclude that the AIC criterion does not produce the most optimal orders.

#### Minimum Description Length Criterion

Because the AIC criterion produced a model with non-optimal orders, you can try estimating the model orders with the MDL criterion. By using the MDL criterion, the lowest prediction error corresponds to a model dimension of 12, as shown in the **prediction error** plot. The SI Estimate Orders of System Model VI returns the following optimal orders:

- A order = 6
- B order = 6
- delay = 0

The following figure shows a pole-zero plot of a model with a model dimension of 12.

[IMAGE alt='image' src='pole-zero_mdl_fp.gif']

Compare the previous figure, which uses the MDL criterion, and the figure that uses the AIC criterion. Because there are no overlapping pole-zero pairs in the previous figure, you can conclude that the MDL criterion fits better than the AIC criterion in this particular example.

In addition to examining redundancy, you also can use the pole-zero plot for other purposes. For example, both the previous two figures show poles outside the unit circle. Having poles outside the unit circle implies that this model is not optimal because the ARX system based on the AIC or MDL criteria is unstable. One way to stabilize the system is to change the order.

In addition to the FPE, AIC, and MDL criteria, you can set user-defined orders in the SI Estimate Orders of System Model VI.

#### User-Defined Criterion

If you know nothing about the system, you might have to rely on trial and error to determine the optimal orders of the model. However, if you have some knowledge about a system, you can customize the estimation to find a model that fits a certain model dimension. For this model, assume you know that the system is stable; therefore, no poles exist outside the unit circle. Because both the AIC and MDL criterion did not produce stable models, the model orders do not describe the system accurately.

On the following block diagram, you can customize the **method** parameter. Instead of **AIC** or **MDL**, you can select **<Other>** and enter the desired model dimension in the text box. Assume you know that the model dimension is nine.

[IMAGE alt='image' src='noloc_bd_pole_zero_valid.gif']

The following figure shows the corresponding **pole-zero
plot** graph with a model dimension of nine, which corresponds to the following optimal orders:

- A order = 4
- B order = 5
- delay = 0

[IMAGE alt='image' src='pole-zero_user_fp.gif']

Compare the pole-zero plot in the previous figure with the previous two figures which uses the MDL criterion and the AIC criterion. The figure which uses the user-defined criterion has no overlapping pole-zero pairs and all the poles are within the unit circle. By visually inspecting the pole-zero plot, you can see that this model is stable and not redundant. Using these model orders, you now can estimate and verify the system model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/case_study_preprocessing.html language=enus -->
## TOPIC 00069: Preprocessing the Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/case_study_preprocessing.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/case_study_preprocessing.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Preprocessing the Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After you gather data, the next step in the system identification process is to [preprocess](preprocessing_data.html) the data. The input to the system in this case study is the reaction torque of the structure on the ground. This input is a swept sine wave with 200 frequency points equally spaced over the frequency band from 0.122 Hz to 24.4 Hz.

The output of this system is the acceleration of the flexible arm. The acceleration contains information about the flexible resonances and anti-resonances.

The data set contains 4096 samples at a sampling rate of 500 Hz or sampling time of 0.002 seconds. Thus the total time of the response is 8.192 seconds.

You can preprocess the raw data by examining the time and frequency responses of the system. Based on those analyses, you can [filter](#applying_a_filter_to_the_raw_data) and [downsample](#downsampling_the_raw_data) the data set to reduce the amount of data in the raw data set for simpler identification.

#### Examining the Time Response Data

Using the data in the [SI Data Samples](../lvsysid/si_data_samples.html) VI for the flexible robotic arm, you can view the input and output data, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_flexible_arm.gif']

The **stimulus signal – torque** output corresponds to the input data, or the torque, and the **response signal – acceleration** output corresponds to the output data, or the acceleration.

The following figure shows the input and output data on graphs during the length of the response. By looking at the graphs, you can inspect the data for outliers, clipped saturation, or quantization effects that you can remove because they are not representative of the system behavior.

[IMAGE alt='image' src='flexarm_fp.gif']

The previous figure shows no obvious nominal, trend, or outlier values in the input or output time waveforms.

#### Examining the Frequency Response Data

In addition to examining the time response data, you also want to examine the [frequency response](si_frequency_response.html) data. You can use the [SI Estimate Frequency Response](../lvsysid/estimate_freq_response.html) VI to view the frequency response of the measured output signal, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_freq_estimation.gif']

The input data is periodic over 4096 samples, which is the signal length. Notice that in the previous figure the **window length**, 4096, is the same as the signal length so as to obtain a smaller bias in the frequency response estimation.

The following figure shows the magnitude and phase responses of the measured output signal. The **magnitude response** graph shows three resonances and two anti-resonances in the frequency domain. Resonances are vibrations of large amplitude in a system caused by exciting the system at its natural frequency.

[IMAGE alt='image' src='est_freq_resp_fp.gif']

Notice the resonance at approximately 42 Hz. You can deduce that this resonance is caused by noise or nonlinear system behavior because the 42 Hz falls outside the frequency range of the input data, 0.122–24.4 Hz. At 42 Hz, there is no input energy, thus implying that the response at 42 Hz is not a result of the input.

By examining the frequency response data, you see that [filtering](filt_downsampling.html) is necessary to remove this resonance peak at 42 Hz. You can use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to [apply a filter](#applying_a_filter_to_the_raw_data) to the flexible arm data.

#### Applying a Filter to the Raw Data

To eliminate the resonance peak at 42 Hz, you can apply a filter to the raw data. By first applying a lowpass filter with a cutoff frequency of 25 Hz, you eliminate the high-frequency noise from the raw data set. The following figure shows how to use [SI Lowpass Filter](../lvsysid/si_lowpass_filter.html) to apply a lowpass filter to the raw data set.

[IMAGE alt='image' src='noloc_bd_lowpass_filter.gif']

You can see the effects of the lowpass filter by comparing the frequency response of the filtered data set in the following figure to the frequency response of the non-filtered data set. By using a lowpass filter, you can see that the resonance at approximately 42 Hz is no longer part of the data set you will use to estimate the model.

[IMAGE alt='image' src='lowpassfilter_fp.gif']

#### Downsampling the Raw Data

Sampling theory, in conjunction with the Nyquist criterion, enables you to reduce the sampling rate from 500 Hz to 50 Hz. Applying a [filter and downsampling](filt_downsampling.html) the data set reduces the number of samples in and the computational complexity of the data set. The goal is to use as few samples as possible to evaluate the behavior of the system.

Sampling theory enables you to downsample, or decimate, the data set. Downsampling reduces the sampling rate, 500 Hz, by a factor of 10. Thus downsampling enables you to acquire the data at a sampling rate of 50 Hz. The Nyquist criterion states that you must sample the signal at a minimum of twice the highest frequency in the system.

Recall that the input data is equally spaced over the frequency band 0.122–24.4 Hz. Therefore, according to the Nyquist criterion, you must sample at a minimum of 50 Hz to avoid any antialiasing. The benefit of sampling at 50 Hz is that you still acquire all the data in the frequency band, yet you eliminate the resonance peak at 42 Hz.

Therefore, in the following figure, the SI Lowpass Filter VI sets the **cutoff frequency** to 25. In addition to applying a lowpass filter to the data, you must downsample the reduced data set. The [SI Down Sampling](../lvsysid/down_sample.html) VI in the following figure uses a **decimation factor** of 10.

[IMAGE alt='image' src='noloc_bd_downsample.gif']

The SI Lowpass Filter VI applies a lowpass filter before downsampling the data set to avoid aliasing at the 42 Hz resonance. Together, the lowpass filter and downsampling remove the high frequency disturbance and make the process faster and more efficient.

Notice that the **window length** parameter of the SI Estimate Frequency Response VI in the previous figure is around 400 instead of 4096, as shown in the previous figure. You can reduce the window length by a factor of 10 because the number of samples in the reduced data set is one tenth of the number of samples in the raw data set.

The following figure shows the frequency response after applying a filter to and downsampling the raw data set.

[IMAGE alt='image' src='downsample_fp.gif']

Filtering and downsampling are beneficial because they eliminate the nonrealistic parts of the frequency response and reduce the amount of work required in the model estimation process.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/case_study_ssest.html language=enus -->
## TOPIC 00070: Estimating and Validating a State-Space Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/case_study_ssest.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/case_study_ssest.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Estimating and Validating a State-Space Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

For a [state-space](modeldefinitionsss.html) model, order estimation is equivalent to estimating the number of significant singular values, which correspond to the number of states in the model. After identifying a state-space model that represents the system, you can use the same validation and verification technique used in the [Simulation and Prediction](case_study_validating.html#simulation_and_prediction) section and the [Residual Analysis](case_study_validating.html#residual_analysis) section.

The examples in this topic use the same flexible robotic arm data and the same preprocessing techniques.

#### Finding the Singular Values

The following block diagram shows how to use the [SI Estimate Orders of System Model](../lvsysid/est__orders_system_model.html) VI to find the optimal order and the number of significant singular values.

[IMAGE alt='image' src='svplot_ss_bd.gif']

The **Singular Values** graph in the following figure shows a singular value plot with four leading singular values.

[IMAGE alt='image' src='svplot_ss_fp.gif']

By looking both at the **Singular Values** graph and the **optimal order**, you can see that there are four states in this state-space model.

#### Validating the Estimated State-Space Model

You can [validate](validating_models.html) the state-space model in the same way that you validated the ARX model. You use the [SI Model Simulation](../lvsysid/model_simulation.html) VI and the [SI Model Prediction](../lvsysid/model_prediction.html) VI to determine the accuracy of the state-space model.

The following figure shows the complete process, from estimating the state-space model to simulating and predicting the response of the model.

[IMAGE alt='image' src='noloc_bd_ss_sim_predict.gif']

The **simulation** and **1-step ahead prediction** graphs in the previous figure show simulation and prediction plots for a state-space model.

[IMAGE alt='image' src='simpredict_ss_fp.gif']

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/case_study_validating.html language=enus -->
## TOPIC 00071: Validating the ARX Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/case_study_validating.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/case_study_validating.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Validating the ARX Model (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The goal of [model validation](validating_models.html) is to determine whether or not the estimated model accurately reflects the actual system. Using the model orders found in the [User-Defined Criterion](case_study_estimating.html#user-defined_criterion) section, you can [simulate and predict](#simulation_and_prediction) the response of the system. You can compare these responses to the actual response and determine the accuracy of the estimated model. You also can [analyze the residuals](#residual_analysis) to determine the accuracy of the estimated model.

#### Simulation and Prediction

You can use the [SI Model Simulation](../lvsysid/model_simulation.html) VI and [SI Model Prediction](../lvsysid/model_prediction.html) VI to determine the accuracy of the estimated model. The SI Model Simulation VI simulates the system model and the SI Model Prediction VI performs a prediction of the system model. The results of the SI Model Prediction VI might differ from the SI Model Simulation VI because the SI Model Prediction VI periodically makes corrections to the estimated response based on the actual response of the system.

The following figure shows how you use these VIs to verify the [ARX model](modeldefinitionsarx.html) created in the [User-Defined Criterion](case_study_estimating.html#user-defined_criterion) section.

[IMAGE alt='image' src='noloc_bd_arx_simple_predict.gif']

The **simulation** and **1-step ahead prediction** graphs enable you to visually determine how accurate the model is. The following figure shows the results of the simulation and prediction as well as the actual response of the system.

[IMAGE alt='image' src='simpredict_arx_fp.gif']

Notice how the actual response, or the **measured
response**, is different from the **simulated
response** in the **simulation** graph. The SI Model Simulation VI simulates the response of the system without considering the actual response of and the noise dynamics in the system.

#### Residual Analysis

In addition to simulation and prediction, you can perform a [residual analysis](validating_models.html#model_residual_analysis) to validate the system model. Residual analysis tests whether the [prediction error](parameters_for_pe.html) correlates to the stimulus signal. Prediction errors are usually uncorrelated with all stimulus signals in an open-loop system.

The following block diagram shows how you can use the [SI Model Residual Analysis](../lvsysid/model_resid_analysis.html) VI with the ARX model identified in the [User-Defined Criterion](case_study_estimating.html#user-defined_criterion) section to analyze the residuals.

[IMAGE alt='image' src='noloc_bd_arx450_residual.gif']

The following figure shows an example of ideal results where both [autocorrelation](validating_models.html#autocorrelation) and [cross correlation](validating_models.html#cross_correlation) are inside the confidence region except those in the vicinity of τ = 0. This result indicates that the estimated model accurately describes the system.

[IMAGE alt='image' src='arx450_residual_fp.gif']

When you verify and validate the identified model, you must use multiple analysis techniques to determine if the estimated model accurately represents the system. Some analysis techniques can be misleading. For example, if you performed a residual analysis on the model identified in the [Minimum Description Length Criterion](case_study_estimating.html#minimum_description_length_criterion) section, you might conclude that this model is an accurate representation of the system. The following figure shows the autocorrelation and cross-correlation residual analysis for the model in the [Minimum Description Length Criterion](case_study_estimating.html#minimum_description_length_criterion) section. Recall that this model has the following orders:

- A order = 6
- B order = 6
- delay = 0

[IMAGE alt='image' src='arx660_residual_fp.gif']

The previous figure shows that both the autocorrelation and cross correlation are inside the confidence region. Therefore, without performing any other analyses, you might conclude that this model is an accurate representation of the system. However, the pole-zero analysis in the [Minimum Description Length Criterion](case_study_estimating.html#minimum_description_length_criterion) section showed poles outside of the unit circle. So you already determined that this model is unstable. Thus, despite acceptable autocorrelation and cross-correlation values, concluding that this model is accurate is incorrect.

Thus, if you only performed a residual analysis, you might not discover that this model is actually unstable. When validating a model, perform multiple analyses to ensure the accuracy of the model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/chirp_waveform.html language=enus -->
## TOPIC 00072: Chirp Waveform (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/chirp_waveform.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/chirp_waveform.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Chirp Waveform (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The chirp waveform, also known as a swept sine wave, is a sinusoid waveform with a frequency that varies continuously over a certain range of values ω
 <sub>1</sub>
 ≤
 ω
 ≤
 ω
 <sub>2</sub> for a specific period of time 0 ≤
 *t*
 ≤
 *T*. The resulting signal has a [crest factor](choosing_stimulus_signal.html)
 *C*
 <sub>f</sub> of [IMAGE alt='image' src='eq_sqrt2.gif']. You can modify the signal to excite specific signal spectra.

In comparison to other stimulus signals, such as white noise, a chirp waveform is easier to generate and control. You can use the [Chirp Pattern](/csh?topicname=lvanls/chirp_pattern.html) VI to generate a chirp pattern. You then can use the [Build Waveform (Analog Waveform)](/csh?topicname=lvwave/build_waveform.html) function to convert this chirp pattern to a chirp waveform.

The following figure shows an example of a chirp waveform.

[IMAGE alt='image' src='chirp.gif']

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/choosing_stimulus_signal.html language=enus -->
## TOPIC 00073: Choosing a Stimulus Signal (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/choosing_stimulus_signal.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/choosing_stimulus_signal.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Choosing a Stimulus Signal (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The choice of stimulus signals has an important role in the system behavior and the accuracy of the estimated model. These signals determine the operating points of the system. While the system under test often limits the choice of signals, you must choose stimulus signals to produce a response of the system under test. The response provides the information you need for developing an accurate model. The response is dependent on the physics of the system you want to study. Some systems tend to respond faster than others. Other systems have large time constants and delays. For these reasons, defining a stimulus signal that provides enough excitation to the system is important. You must choose the stimulus signal types according to the system under test to ensure the response contains the important features of the system dynamics. Use the following guidelines to choose input signal types.

- You want to test the system under conditions similar to the actual operating conditions. When you complete experiments in these conditions, you identify the system in the same conditions under which you will implement the resulting model. This criterion is extremely important for nonlinear systems.
- You want the inputs to the system under test to excite the system. Whether the system is excited is dependent on the spectrum of the input signal. Specifically, you must excite the system with an input frequency similar to the frequency at which such inputs change during normal operations.
- You want the amplitude of the step input to cover a wide range of variations. Therefore, in the data you use for model estimation, you must cover the normal operation range of system inputs, especially when you use the calculated model for model-based control. To cover the normal operation range, you can combine the positive and negative step changes of different magnitudes in the system inputs.
- You want the input signal to deliver as much input power to the system as possible. However, in the real-world, you must ensure that this input power stays within the limits of the physical system. The crest factor C f , defined by the following equation, describes this property.
 [IMAGE alt='image' src='eq_crest_factor.gif'] 
 The smaller the crest factor, the better the signal excitation. A better signal excitation results in larger total energy delivery and enhanced signal-to-noise ratio. The theoretical lower bound for the crest factor is 1.

You can use the following types of stimulus signals for exciting the system under test.

- Filtered Gaussian white noise
- Random binary signal
- Pseudo-random binary sequence
- Chirp waveform
- Step signals and step responses

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/closed-loop_est.html language=enus -->
## TOPIC 00074: Closed-Loop Systems Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/closed-loop_est.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/closed-loop_est.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Closed-Loop Systems Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Systems in many real-world applications contain feedback. Feedback is a process in which the output signal of a dynamic system is passed, or fed back, to the input to regulate the next output. Systems without feedback are open-loop systems. Systems with feedback are closed-loop systems.

In an open-loop system, the stimulus signal and the output noise do not correlate with each other. In a closed-loop system, the stimulus signal correlates to the output noise. Though you can apply many open-loop model estimation methods to closed-loop data, not all open-loop model estimation methods handle the correlation between the stimulus signal and output noise well.

#### Feedback in Systems

Feedback is common in control systems. Feedback regulates the system outputs on the basis of a reference input. Feedback also reduces the effect of input disturbances. One example of a closed-loop system is a system that regulates room temperature, as shown in the following figure. In this example, the reference input is the temperature *T*
 <sub>set</sub> at which you want the room to stay. The thermostat senses the actual temperature, *T*
 <sub>actual</sub>, of the room. Based on the difference between *T*
 <sub>actual</sub> and *T*
 <sub>set</sub>, the thermostat activates the heater or the air conditioner. The thermostat returns *T*
 <sub>actual</sub> as the feedback to compare again with *T*
 <sub>set</sub>. Then the thermostat uses the difference between *T*
 <sub>actual</sub>and 
 *T*
 <sub>set</sub> to regulate the temperature at the next moment.

[IMAGE alt='image' src='noloc_eps_closed-loop_thermostat.gif']

You must verify if feedback exists before choosing a model estimation method because not all open-loop model estimation methods work correctly with closed-loop data.

|  | Note You must know whether the data you collect is from an open-loop system or a closed-loop system according to the real-world system configuration. If you do not have such information, you can determine if feedback exists by using the SI Detect Feedback VI or by obtaining the impulse responses of a dynamic system. You can use the Least Squares instances of the SI Estimate Impulse Response VI to estimate the impulse response of a dynamic system. |
| --- | --- |

The following figure shows a comparison of the impulse responses of the dynamic system in a closed-loop system and an open-loop system.

[IMAGE alt='image' src='feedback_detection.gif']

The values outside the **upper limit** and **lower limit** range at the negative lag, which appears between –10 and 0 on the x-axis, are considered significant values. Significant values in the impulse response at negative lags imply feedback in data. As shown in the following figure, significant values exist in the **Closed-loop data** plot. Therefore, feedback exists in the closed-loop system. No significant impulse response values exist in the **Open-loop data** plot. Thus, feedback does not exist in the open-loop system.

#### Understanding Closed-Loop Model Estimation Methods

Closed-loop model estimation methods use data from a closed-loop system to build a model for a dynamic system that a controller regulates. The following figure shows a system that consists of a dynamic system and a controller. In this system, *G*
 <sub>0</sub> is the dynamic system, *F*
 <sub>y</sub> is the controller, *H* is the stochastic part of the dynamic system, *u* is the stimulus signal, *y* is the response signal, *r* is the reference signal that is an external signal, and *e* is the output noise. In control engineering, this system is known as a feedback-path closed-loop system, which is a typical closed-loop system.

[IMAGE alt='image' src='noloc_eps_typical_closed-loop_system.gif']

In some cases, the controller comes before the dynamic system in a closed-loop system. This system is known as a feedforward-path closed-loop system, as shown in the following figure.

[IMAGE alt='image' src='noloc_eps_feedforward_closed-loop_system.gif']

Depending on the amount of prior knowledge you have about the feedback, the controller, and the reference signal of a system, you can categorize closed-loop model estimation approaches into the following three groups:

- Direct identification —Uses the stimulus and response signals to identify the dynamic system model as if the dynamic system is in an open-loop system. You can apply the direct identification approach to compute all types of models except state-space models.
- Indirect identification —Identifies a closed-loop system by using the reference signal and the response signal and then determines the dynamic system model based on the known controller of the closed-loop system. You can apply the indirect identification approach to compute transfer function models.
- Joint input-output identification —Considers the stimulus signal and the response signal as outputs of a cascaded system. The reference signal and the noise jointly perturb the system, and the dynamic system model is identified from this joint input-output system. You can apply the joint input-output identification approach to compute transfer function models.

You can choose a suitable model identification approach according to the information you have about the closed-loop system. The following table summarizes the information you must have to use each identification approach.

|  | Stimulus Signal | Response Signal | Reference Signal | Controller Information |
| --- | --- | --- | --- | --- |
| Direct | Yes | Yes | — | — |
| Indirect | — | Yes | Yes | Yes |
| Joint Input-Output | Yes | Yes | Yes | — |

With the [System Identification](../lvsysid/lv_sysid_pal.html) VIs, you can choose to use the direct, indirect, or joint input-output identification approaches for different types of closed-loop systems. The direct identification approach supports single-input single-output (SISO), multiple-input single-output (MISO), and multiple-input multiple-output (MIMO) systems. The indirect and joint input-output identification approaches support SISO systems only.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/constraints_with_guess.html language=enus -->
## TOPIC 00075: Setting Parameter Constraints with an Initial Guess (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/constraints_with_guess.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/constraints_with_guess.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Setting Parameter Constraints with an Initial Guess (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you have information about a certain parameter and can estimate a value for that parameter, you can refine estimation by using that value as an initial guess.

The [SI Estimate Partially Known State-Space Model](../lvsysid/est_pk_ss_model.html) VI and the [SI Estimate Partially Known Continuous Transfer Function Model](../lvsysid/est_pk_continuous_tf_model.html) VI perform optimization using the initial guess you provide. These two VIs then use the upper and lower limit settings you specify as boundary constraints during the optimization process.

The initial guess you provide greatly affects the performance of any optimization technique. Whether an optimization process reaches a global optimum depends on the initial guess. With some initial guesses, optimization processes might locate only a local optimum, which is the smallest difference between the estimated output and the real output within a certain smaller range rather than in the whole range of interest. Therefore, to decrease the risk of locating a local optimum instead of the global optimum, try different initial guesses. The following figure shows an example of different estimations resulting from different initial guesses and illustrates the importance of setting different initial guesses to find the global optimum.

[IMAGE alt='image' src='estimating_local_optimum_and_global_optimum.gif']

As the previous figure shows, if you set *C* to an initial guess of 0.1, you obtain an optimized value of 0.02. You can see the **Estimated response (global)** plot and the **Measured response** plot match in the **Response graph**. This response from the estimated model is close to the real-world response. However, if you set the initial guess of *C* to 1.5, you get an optimized value of 1.41. The **Estimated response (local)** plot does not match the **Measured response** plot in the **Response graph**. Thus, with this initial guess, the estimated model response does not represent the real-world response accurately.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/constraints_with_range.html language=enus -->
## TOPIC 00076: Setting Parameter Constraints with a Range (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/constraints_with_range.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/constraints_with_range.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Setting Parameter Constraints with a Range (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you have prior knowledge of a parameter, you can set constraints by providing upper and lower limits for the parameter. With the limit range, the [SI Estimate Partially Known State-Space Model](../lvsysid/est_pk_ss_model.html) VI randomly selects a value within the range as an initial guess of the parameter. From this initial value, the VI then performs optimization to minimize the difference between the estimated output and the measured real output. The goal of constraint optimization is to find a global optimum, or the smallest difference between the estimated output and the real output, with parameters of physical meaning. Successfully finding the global optimum depends on the limit range you set and the random initial value the SI Estimate Partially Known State-Space Model VI selects.

To increase the possibility of finding the global optimum, complete the following steps:

1. Use prior knowledge to set the range as narrow as possible.
2. Perform multiple estimates with the range you set. You might get different optimization results because the SI Estimate Partially Known State-Space Model VI randomly selects an initial value within the range each time you run the VI. If you repeatedly obtain the same result, this result might be the optimum you want to find. If you obtain inconsistent results, either choose the result that best meets the system requirements, or continue with step 3 to adjust the limit range.
3. Select one of the previous results you got in step 2 according to the prior knowledge you have of the system. Narrow the range in which the result falls. Run the SI Estimate Partially Known State-Space Model VI multiple times. A consistent result you get might be the optimum you want to find. Otherwise, repeat this step until you find a consistent result.

You set limits in the [SI Estimate Partially Known Continuous Transfer Function Model](../lvsysid/est_pk_continuous_tf_model.html) VI the same way you do in the SI Estimate Partially Known State-Space Model VI.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/converting_models.html language=enus -->
## TOPIC 00077: Converting Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/converting_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/converting_models.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Converting Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can use the [Model Conversion](../lvsysid/model_conversion_pal.html) VIs to convert system models from one representation to another, from continuous to discrete models, and from discrete to continuous models. You can convert models you created in this toolkit to models you can use in another toolkit. You also can convert a model after you estimate the model or after you [analyze](analyzing_models.html) or [validate](validating_models.html) the model.

You can use the Model Conversion VIs to switch between different [model types and representations](model_types_and_reps.html). For example, when estimating a digital system, you can convert an existing continuous model to a discrete model to approximate the real-time behavior of the system. You do not need to create a new discrete model for the digital system. Using the Model Conversion VIs, you also can convert models you create with the [System Identification](../lvsysid/lv_sysid_pal.html) VIs into [transfer function](modeldefinitionstf.html), [zero-pole-gain](modeldefinitionszpg.html), or [state-space](modeldefinitionsss.html) models that you then can use with the LabVIEW Control Design and Simulation Module. This model conversion process enables you to identify a model for an unknown system with the System Identification VIs and then design a controller for this system using the Control Design and Simulation Module.

Refer to the National Instruments Web site for more information about the Control Design and Simulation Module.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/data_scaling.html language=enus -->
## TOPIC 00078: Data Scaling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/data_scaling.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/data_scaling.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Data Scaling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Multiple-input multiple-output (MIMO) systems commonly have inputs and outputs of different amplitude ranges. This diversity can result in an ill-conditioned model estimation, which reduces the accuracy of the model. To resolve this issue, you can scale the data ranges of different inputs and outputs. For example, consider the valves A and B in the following figure.

[IMAGE alt='image' src='noloc_eps_onetank.gif']

Valves *A* and *B* operate between 0–100% and 50–60%, respectively. The pressure in the respective stream lines are *P*<sub>A</sub> and *P*<sub>B</sub>. If you assume that *P*<sub>B</sub> can be much larger than *P*<sub>A</sub>, you might need to normalize the range of operation of valve *B* for numerical robustness. You can use the following relationship to normalize the range of operation.

[IMAGE alt='image' src='eq_normalize_example.gif']

The [SI Normalize](../lvsysid/si_normalize.html) VI ensures that all stimulus and response signals have a zero mean and unit variance over the sample data range used for model estimation. This process standardizes the range of the equation for all signals considered for model estimation. This data preprocessing step considers all inputs and outputs equally important from the numerical calculation viewpoint.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/define_est_pk.html language=enus -->
## TOPIC 00079: Defining and Estimating Partially Known Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/define_est_pk.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/define_est_pk.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Defining and Estimating Partially Known Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Before estimating partially known models, you first must define those models. Using prior knowledge, you choose a model for the dynamic system and set parameter constraints for the model. You then can estimate the model to represent the dynamic system. Use the [SI Create Partially Known State-Space Model](../lvsysid/create_pk_ss_model.html) VI and the [SI Create Partially Known Continuous Transfer Function Model](../lvsysid/create_pk_continuous_tf_model.html) VI to define partially known models.

Use the SI Create Partially Known State-Space Model VI to define partially known continuous or discrete [state-space](modeldefinitionsss.html) models.

You can use the SI Create Partially Known State-Space Model VI, for example, to define a state-space model that represents an RLC circuit consisting of a resistor *R*, an inductor *L*, and a capacitor *C*. Using prior knowledge, you describe the relationship of *R*, *L*, and *C* with the following equations:

[IMAGE alt='image' src='eq_rlc_a.gif']

[IMAGE alt='image' src='eq_rlc_b.gif']

[IMAGE alt='image' src='eq_rlc_c.gif']

*D* = 0

You also can use prior knowledge to define the initial guesses and upper and lower limits of *R*, *L*, and *C*. The SI Create Partially Known State-Space Model VI uses variables rather than numerical values to construct a symbolic model. As the following figure shows, you use variable names, such as *R*, *L*, and *C*, in the **symbolic A**, **symbolic B**, **symbolic C**, and **symbolic D** inputs to define the RLC circuit. Then you specify values for *R*, *L*, and *C* in the **variables** input.

[IMAGE alt='image' src='using_variables.gif']

Use the SI Create Partially Known Continuous Transfer Function Model VI to define partially known continuous transfer function models. The following equation represents a continuous [transfer function](modeldefinitionstf.html) model.

[IMAGE alt='image' src='eq_continuoustf_model.gif']

| where | Kp is the transfer function gain |
| --- | --- |
|  | Td is the delay |
|  | Tp is the first-order time constant |
|  | w is the natural frequency |
|  | r is the damping ratio |
|  | s represents the time |

You can apply the prior knowledge you have about the parameters *K*, *T*<sub>d</sub>, *T*<sub>p</sub>, *w*, and *r* to the **static gain**, **delay(s)**, **T**<sub>p</sub>**(s)**, **natural freq (rad/s)**, and **damping ratio** inputs, respectively, of the SI Create Partially Known Continuous Transfer Function Model VI by defining the initial guesses and upper and lower limits.

With the System Identification VIs and a partially known model, you can set constraints on each parameter of a state-space or continuous transfer function model in two ways—with an upper and lower limit or with an initial guess.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/direct_id.html language=enus -->
## TOPIC 00080: Direct Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/direct_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/direct_id.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Direct Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If the stimulus and response signals of a closed-loop system are available but you do not have any other information about the system, you can use only the techniques developed for open-loop models to estimate the closed-loop system. However, you cannot apply all open-loop identification methods to estimate the model of a dynamic system in a closed-loop system. Some open-loop model identification methods assume zero correlation between the stimulus signal and output noise. In closed-loop systems, this correlation is nonzero. Thus, if you use certain open-loop model estimation methods, such as the instrument variable (IV) method and the [correlation analysis](ir_correlation_analysis.html) methods, with closed-loop data, you might estimate a model incorrectly. You can use the prediction error method to identify the dynamic system in a closed-loop system.

The direct identification approach is used commonly in real-world applications. This approach is convenient because you do not need to have additional information about a closed-loop system, such as the reference signal or the controller. However, the estimation might not be accurate if the model type you select for a dynamic system does not describe the output noise of the system accurately. For example, if the output noise of a dynamic system is color noise and you select an [output-error (OE)](modeldefinitionsoe.html) model, which assumes the output noise is white noise, the estimation for the OE model might be biased when you use direct identification. The bias might be small, though, if the signal-to-noise ratio (SNR) of the system is high.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/est_frf.html language=enus -->
## TOPIC 00081: Estimating the Frequency Response Function (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/est_frf.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/est_frf.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Estimating the Frequency Response Function (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The frequency response function (FRF) represents the frequency-domain relationship between the inputs and outputs of a dynamic system. The FRF contains the magnitude, phase, and frequency information of the dynamic system data. You estimate the FRF when you have time-domain data, but you want to identify a system model in the frequency domain. If you [acquire](acquiring_data.html) frequency-domain data, this data already contains the FRF.

When you estimate the FRF, the following factors can affect the FRF negatively.

- Noise
- Spectral leakage
- Nonlinear distortion

Use the [SI Estimate FRF](../lvsysid/si_est_frf.html) VI to estimate the FRF and to minimize the effects of these factors. This VI supports [windowing](/csh?topicname=lvanlsconcepts/windowing_fa.html), which helps to minimize spectral leakage. This VI also supports [averaging](/csh?topicname=lvanlsconcepts/average_improve_measure_freq.html), which helps to minimize noise and nonlinear distortion.

#### Minimizing Spectral Leakage

To minimize the effects of spectral leakage, you can apply a window to the time-domain data. The SI Estimate FRF VI supports several types of windows for different types of signals. The [type of window you choose](/csh?topicname=lvanlsconcepts/choosing_smoothing_window.html) depends on the characteristics of the signal. For example, use a [Hanning](/csh?topicname=lvanlsconcepts/lvac_hanning.html) window for random excitation signals. For impact excitation signals, use an [Exponential](/csh?topicname=lvanlsconcepts/lvac_exponential.html) window.

#### Minimizing Noise and Nonlinear Distortion

You can average multiple FRF measurements to minimize the effects of nonlinear distortion and reduce the effects of noise in the data measurements. Averaging the data smooths the frequency response by reducing fluctuations that exist in the data.

The SI Estimate FRF VI supports both [RMS averaging](/csh?topicname=lvanlsconcepts/lvac_rms_averaging.html) and [vector averaging](/csh?topicname=lvanlsconcepts/lvac_vector_averaging.html) to average dynamic system data.

|  | Note The multiple-input multiple-output (MIMO) instances of the SI Estimate FRF VI support the RMS averaging mode only. |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/estimating_models.html language=enus -->
## TOPIC 00082: Estimating Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/estimating_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/estimating_models.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Estimating Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After [acquiring](acquiring_data.html) and [preprocessing](preprocessing_data.html) the data from a linear time-invariant system, the next step in the system identification process is estimating the model. You can use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to estimate models by using any of the following methods:

- Nonparametric
- Parametric
- Partially Known
- Closed-Loop Systems
- Recursive
- Frequency-Domain

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/filt_downsampling.html language=enus -->
## TOPIC 00083: Filtering and Downsampling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/filt_downsampling.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/filt_downsampling.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Filtering and Downsampling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You might be interested in only a specific frequency range of the frequency response for a model. You can filter and enhance the data in the frequency range to improve the fit in the regions of interest. If the sampling frequency is much higher than the bandwidth of the system, the sampling frequency might substantially increase the computation burden for complicated identification algorithms. You can decrease the sampling frequency by taking every *n*
 <sup>th</sup> sample to construct a new downsampled data set. Applying an anti-alias filter on the data before downsampling prevents corruption of the downsampled data set.

You can use the [SI Lowpass Filter](../lvsysid/si_lowpass_filter.html) VI or the [SI Bandpass Filter](../lvsysid/si_bandpass_filter.html) VI to apply a lowpass or bandpass filter, respectively, to the data from the system. You then can use the [SI Down Sampling](../lvsysid/down_sample.html) VI to reduce the number of samples in the data set.

Refer to the Down Sampling VI in the labview\examples\System Identification\Getting Started\General.llb for an example that demonstrates how to use the SI Down Sampling VI to reduce the sampling rate of a signal.

After preprocessing the data you acquired from a dynamic system, the result is a data set that you can use to estimate a model that reflects the system dynamics.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/filt_gauss_white_noise.html language=enus -->
## TOPIC 00084: Filtered Gaussian White Noise (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/filt_gauss_white_noise.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/filt_gauss_white_noise.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Filtered Gaussian White Noise (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Filtered Gaussian white noise is a simple signal that can generate virtually any signal spectra in conjunction with the proper linear filtering. The theoretical [crest factor](choosing_stimulus_signal.html) *C*<sub>f</sub> for a Gaussian is infinite, but clipping the Gaussian amplitude to the input signal limit reduces the crest factor. Clipping the Gaussian amplitude minimally affects the generated spectrum. You can use the [Gaussian White Noise](/csh?topicname=lvanls/gaussian_white_noise.html) VI to generate Gaussian white noise. You then can use the [Filters](/csh?topicname=lvanls/filter_vis.html) VIs to generate Filtered Gaussian white noise from Gaussian white noise.

The following figure shows an example of Filtered Gaussian white noise.

[IMAGE alt='image' src='filtered_gaussian.gif']

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/flexarm_case_study.html language=enus -->
## TOPIC 00085: Flexible Arm Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/flexarm_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/flexarm_case_study.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Flexible Arm Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study guides you through the system identification process by using the sample data in the [SI Data Samples](../lvsysid/si_data_samples.html) VI. The SI Data Samples VI includes data sets for a DC motor, a flexible robot arm, a ball and beam apparatus, an RC circuit, and so on. This case study uses the flexible arm data to demonstrate the system identification process and to compare different estimation methods.

The flexible arm is a nonlinear dynamic system. The [System Identification](../lvsysid/lv_sysid_pal.html) VIs enable you to build models for linear systems. This case study guides you through obtaining a linear representation of a nonlinear system.

Refer to the labview\examples\system identification\SICaseStudy1.llb to access the VIs in this case study.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/fr_lag_window.html language=enus -->
## TOPIC 00086: Applying a Lag Window (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/fr_lag_window.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/fr_lag_window.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Applying a Lag Window (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When computing *Φ*<sub>*uu*</sub>(*e*<sup>*jω*</sup>) and *Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) to obtain the frequency response *G*(*e*<sup>*jω*</sup>), you can apply a lag window *ω*(*τ*) to the autocorrelation function *R*<sub>*uu*</sub> and the cross-correlation function *R*<sub>*uy*</sub> before performing the FFT operation. Applying a lag window improves the accuracy of the frequency response estimation, according to the following equations.

[IMAGE alt='image' src='eq_auto-spectral_density.gif']

[IMAGE alt='image' src='eq_cross-spectral_density.gif']

The lag window approaches zero when the lag *τ* is large. The window weighs out the points of *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> with large lag *τ*, thereby improving the accuracy of the frequency response estimation. The [SI Estimate Frequency Response](../lvsysid/estimate_freq_response.html) VI uses a Hanning window as the lag window.

The [frequency response](si_frequency_response.html) with the lag window, *G*'(*e*<sup>*jω*</sup>), is equivalent to the moving average version of the frequency response without the lag window, *G*(*e*<sup>*jω*</sup>). The average smooths the frequency response, but the smooth frequency response also can deviate from the true frequency response. Adjusting the length of the lag window can balance the trade-off between variance and bias of the frequency response estimation. The larger the length of the lag window, the fewer points of *G*(*e*<sup>*jω*</sup>) the SI Estimate Frequency Response VI averages to compute *G*'(*e*<sup>*jω*</sup>), and hence the larger the variance and the smaller the bias of the frequency estimation.

The following example demonstrates how the length of the lag window affects the frequency response estimation. The following figure shows the front panel of a VI that simulates a system defined by the following equation.

*y*(*k*) – 1.46*y*(*k*– 1) + 2.5*y*(*k* – 2) – 1.46*y*(*k* – 3) + *yk* – 4 = *u*(*k*) + 0.45*u*(*k* – 1) + *u*(*k* – 2)

[IMAGE alt='image' src='lagwindow_fp.gif']

The following figure shows the block diagram of this VI.

[IMAGE alt='image' src='noloc_bd_lag_window.gif']

In this example VI, the input signal *u*(*k*) is a swept sine wave whose normalized frequency is from 0 to 0.5 Hz. The number of data points in the input signal is 4096. The length of the lag window therefore must be less than or equal to 4096. The following figures show the resulting frequency responses when the window length is 4096 and 64, respectively.

[IMAGE alt='image' src='lagwindowlarge.gif']

[IMAGE alt='image' src='lagwindowsmall.gif']

The frequency response curve is smoother and the variance is smaller when the length of the lag window is small. However, when the length of the lag window is too small, you cannot distinguish between the two close peaks in the frequency response, as shown in the previous figure with window length equal to 64. When the length of the lag window is large, the SI Estimate Frequency Response VI accurately estimates the peaks, as shown in the previous figure with window length equal to 4096. The bias is small with a large lag window, but the variance of the estimated frequency response is large.

Setting the length of the lag window to 5–10% of the number of data points when estimating the frequency response often results in a good trade-off between the bias and variance. The length also depends on the signals, the properties of the system, and the purpose of application. For example, to identify the passband of a system, use a smaller lag window. To identify the dynamic properties of a system, such as its natural frequency, use a larger lag window.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/fr_spectral_analysis.html language=enus -->
## TOPIC 00087: Spectral Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/fr_spectral_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/fr_spectral_analysis.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Spectral Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can use the spectral analysis method with any input signal. However, the frequency bandwidth of the input signal must cover the range of interest.

Because the [frequency response](si_frequency_response.html) is the [Fourier transform](/csh?topicname=lvanlsconcepts/fourier_transform.html) of the impulse response, applying the Fourier transform to both sides of the cross-correlation function yields the following equation.

*Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) = *Φ*<sub>*uu*</sub>(*e*<sup>*jω*</sup>)*G*(*e*<sup>*jω*</sup>)

| where | G(ejω) is the frequency response of the system |
| --- | --- |
|  | Φuu(ejω) is the auto-spectral density of the stimulus signal |
|  | Φuy(ejω) is the cross-spectral density between the stimulus signal u(k) and the response signal y(k) |

You then can use the following equation to compute the frequency response *G*(*e*<sup>*jω*</sup>).

[IMAGE alt='image' src='eq_frequency_response.gif']

You can compute *Φ*<sub>uu</sub>(*e*<sup>*jω*</sup>) and *Φ*<sub>*uy*</sub>(*e*<sup>*jω*</sup>) by applying a fast Fourier transform (FFT) to the autocorrelation function *R*<sub>*uu*</sub> and the cross-correlation function *R*<sub>*uy*</sub>, respectively. The number of data points you need to compute *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> decreases as the lag *τ* increases. Therefore, *R*<sub>*uu*</sub> and *R*<sub>*uy*</sub> become inaccurate for a large lag *τ*. In this situation, you can apply a [lag window](fr_lag_window.html) to counter the effects of a large lag *τ* and improve the accuracy of the frequency response estimation.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/freq_sysid.html language=enus -->
## TOPIC 00088: Frequency-Domain Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/freq_sysid.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/freq_sysid.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Frequency-Domain Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Frequency-domain model estimation involves identifying a model of a dynamic system by using the frequency-domain representation of the dynamic system data. You acquire frequency-domain data by using a frequency analyzer. If you acquire time-domain data, you also can convert this time-domain data to frequency-domain data by [estimating the frequency response function](est_frf.html) (FRF) of a dynamic system. The FRF represents the frequency-domain relationship between the inputs and outputs of a dynamic system.

Use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to obtain the FRF and estimate two categories of [parametric](parametric_est.html) models—[transfer function](modeldefinitionstf.html) and [state-space](modeldefinitionsss.html). Use the [SI Estimate Transfer Function Model from FRF](../lvsysid/est_tf_from_frf.html) VI to estimate [continuous and discrete](model_types_and_reps.html) single-input single-output (SISO) transfer function models. Use the [SI Estimate State-Space Model from FRF](../lvsysid/est_ss_from_frf.html) VI to estimate discrete SISO and multiple-input multiple-output (MIMO) state-space models.

#### Advantages of Frequency-Domain System Identification

Compared to time-domain model estimation methods, frequency-domain model estimation methods have the following advantages:

- You can reduce a large number of time-domain data samples to a finite number of frequency-domain data samples.
- You can reduce the effects of noise by averaging the FRF from multiple time-domain data measurements.
- You can focus on frequency bands of interest by directly weighting the frequency-domain data.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/freqsysid_case_study.html language=enus -->
## TOPIC 00089: Frequency-Domain Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/freqsysid_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/freqsysid_case_study.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Frequency-Domain Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study demonstrates how to use frequency-domain data from a flexible robotic arm to estimate and validate a [transfer function](modeldefinitionstf.html) model and [state-space](modeldefinitionsss.html) model of the robotic arm. This case study estimates the models directly from frequency-domain data.

|  | Note If the system you want to estimate contains time-domain data, you first must estimate the FRF by using the SI Estimate FRF VI. |
| --- | --- |

Refer to the Flexible Arm (Frequency Domain) VI in the labview\examples\System Identification\Industry Applications\Mechanical Systems.llb to access the VI in this case study.

In this case study, the input is voltage and the outputs are strain and position. Strain is proportional to the acceleration of the flexible arm. Position is the radial position of the arm.

Because this system contains one input and two outputs, two single-input single-output (SISO) FRFs or one multiple-input multiple-output (MIMO) FRF define this system. One FRF defines the relationship between the voltage input and the strain output. The other FRF defines the relationship between the voltage input and the position output. Each FRF contains information about the magnitude and phase of the frequency response and the scale of the frequency data. This information is specific to each input-output pair. To measure the FRFs in this case study, sine waves at different frequencies excite the flexible arm. This data set has a sampling time of 0.02 seconds, which is equivalent to a sampling rate of 50 Hz.

#### Estimating and Validating a Transfer Function Model

Use the [SI Estimate Transfer Function Model from FRF](../lvsysid/est_tf_from_frf.html) VI to estimate a transfer function model from a SISO FRF. Because this case study involves one input and two outputs, this VI must estimate and validate each SISO transfer function model separately. The following figure shows the block diagram for estimating a transfer function model and validating the resulting transfer function model against the original FRF data. This block diagram uses the FRF describing the relationship between the voltage input and the position output to estimate the transfer function model.

[IMAGE alt='image' src='bd_tf_position.gif']

The **FRF magnitude** and the **FRF phase** inputs of the SI Estimate Transfer Function Model from FRF VI require that the data input is in polar form.

|  | Note If the data input is in complex form, you can use the Re/Im To Polar Function to convert the complex data into polar form to separate the magnitude, phase, and frequency components of the complex representation. After converting the complex data into polar form, bundle the magnitude and frequency components into one cluster and bundle the phase and frequency components into another cluster. Each cluster then contains the data you wire to the FRF magnitude and the FRF phase inputs of the SI Estimate Transfer Function Model from FRF VI. |
| --- | --- |

In this case study, the **FRF magnitude** and the **FRF phase** inputs contain data in polar form. Therefore, the **FRF magnitude** and the **FRF phase** inputs wire directly into the SI Estimate Transfer Function Model from FRF VI.

|  | Note The FRF format input of this VI specifies whether the original FRF magnitude is in decibels or in a linear scale and whether the original FRF phase is wrapped and in radians or in degrees. In this case study, the original FRF data uses the default values of FRF format. The original FRF magnitude is not in decibels. The original FRF phase is wrapped and in radians. |
| --- | --- |

Because a transfer function model is a type of [parametric](parametric_est.html) model representation, you must specify the model parameters before estimating the model. For a transfer function model, you must specify the orders of the numerator and denominator polynomial functions. If you do not have prior knowledge about the system, you must use trial and error to determine the optimal orders of the model.

One way to identify the optimal orders is to observe the peaks in the magnitude response of the original FRF. The optimal order is at least twice the number of peaks. You can plot and observe the magnitude by using the [SI Bode Plot](../lvsysid/bode_plot.html) VI. You can increase the accuracy of the model by modifying the initial guess after analyzing the model. In the previous block diagram, 2 is the initial guess for both the numerator order and the denominator order.

You can [validate](validating_models.html) the resulting model by comparing the original FRF and the FRF that the model generates. Compare the two FRFs on an XY graph by using the SI Bode Plot VI. By default, the SI Bode Plot VI unwraps the phase information and converts the units of the resulting phase to degrees. To compare the original FRF and the FRF that the SI Bode Plot VI displays more accurately, use the [Unwrap Phase](/csh?topicname=lvanls/unwrap_phase.html) VI to unwrap the phase in the original FRF. This case study also uses the [Mathematics](/csh?topicname=lvwave/waveform_measurement_vis.html) VIs to convert the original FRF from radians to degrees.

The following figure shows the [Bode plot](analyzing_models.html#bode_plot) of a 2nd-order transfer function model.

[IMAGE alt='image' src='noloc_eps_fp_tf_position_order3.gif']

Visually inspect the alignment of the **Model-generated FRF** and the **Original FRF** to determine whether the estimated transfer function model accurately describes the dynamic system. Notice that the **Original FRF** and the **Model-generated FRF** do not align. Therefore, 2 is not the most appropriate order value for the transfer function model.

You can increase the accuracy of the model by specifying different values for the **Orders of TF** control. The following figure shows the Bode plots of a 6th-order transfer function model.

[IMAGE alt='image' src='noloc_eps_fp_tf_position.gif']

In this case study, setting the value of the **Orders of TF** to 6 provides a closer alignment of the **Model-generated FRF** and the **Original FRF**. Therefore, a 6th-order transfer function model describes the voltage-position FRF of the dynamic system more accurately than a 2nd-order model.

Identify a second transfer function model by using the FRF of the voltage input and strain output. You must apply the same method when optimizing the model order.

#### Estimating and Validating a State-Space Model

In this case study, a single MIMO FRF also can represent the frequency-domain relationship of the input and outputs of the flexible arm system. You can use this MIMO FRF to estimate state-space models of a dynamic system. The [SI Estimate State-Space Model from FRF](../lvsysid/est_ss_from_frf.html) VI estimates a state-space model for SISO and MIMO systems. This VI requires you to specify the **number of states** of the system you want to estimate. This value comes from prior knowledge about the system.

You also can provide an initial guess if you do not have prior knowledge. A guideline for identifying the number of states of a system is the same as the guideline for identifying the orders of a transfer function model. The number of states is at least twice the number of peaks in the magnitude of the FRF. Because a MIMO FRF is composed of more than one SISO FRF, you must observe the magnitude of the SISO FRF with the maximum number of peaks.

In this case study, the SISO FRFs that comprise the MIMO FRF both have one peak. Therefore, the initial guess at the number of states is 2. By increasing the number of states and plotting the model-generated MIMO FRF along with the original MIMO FRF on a Bode plot, you can observe that entering eight states produces an acceptable estimation for the system.

The following figure shows the Bode Plots of the original MIMO FRF and the MIMO FRF that the state-space model generates.

[IMAGE alt='image' src='fp_ss.gif']

Compare the **FRF Position** graphs in the previous figure with the 6th-order transfer function **FRF Position** graphs. Both model-generated FRFs are close to the original FRF in the **FRF Position** graphs. The proximity of these FRFs indicates that the 6th-order transfer function model and the state-space model with eight states are close approximations for estimating system models in this case study.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/indirect_id.html language=enus -->
## TOPIC 00090: Indirect Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/indirect_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/indirect_id.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Indirect Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The indirect identification approach, which estimates the [transfer function](modeldefinitionstf.html) model of a dynamic system in a closed-loop system, first identifies the transfer function model of the closed-loop system based on the reference signal and the response signal. This approach then retrieves the transfer function model of the dynamic system from the identified closed-loop system. The indirect identification approach can identify the transfer function of the dynamic system accurately even when the signal-to-noise ratio (SNR) of the system is low and no matter whether the output noise is white noise or color noise. However, this approach requires prior knowledge about the controller of the system and the reference signal also must be available. In addition, any inaccuracy or nonlinearity of the controller in the system might affect estimating the model of the dynamic system.

With indirect identification, you can use the following two equations to describe the [feedback-path closed-loop system](closed-loop_est.html).

*y*(*k*) = *G*<sub>0</sub>(*z*)*u*(*k*) + *e*(*k*)

*u*(*k*) = *r*(*k*) – *F*
 <sub>y</sub>(*z*)*y*(*k*)

| where | G0(z) is the open-loop transfer function of the dynamic system |
| --- | --- |
|  | Fy(z) is the transfer function of a linear, time-invariant (LTI) controller |
|  | u(k) is the stimulus signal of the system |
|  | y(k) is the response signal of the system |
|  | r(k) is the reference signal of the system |
|  | e(k) is the output noise of the system |

By combining the previous two equations, you can represent the closed-loop relationship with the following equation:

[IMAGE alt='image' src='eq_closed-loop1.gif']

If you define *G*<sub>cl</sub> as the closed-loop transfer function between the reference signal and the response signal, and let *G*<sub>cl</sub> satisfy the following equation:

[IMAGE alt='image' src='eq_closed-loop2.gif']

you can estimate *G*<sub>cl</sub> with *r*(*k*) as the input and *y*(*k*) as the output using an open loop method, because *r*(*k*) and *e*(*k*) are uncorrelated. You then can calculate *G*<sub>0</sub>after you calculate *G*<sub>cl</sub>, as the following equation shows:

[IMAGE alt='image' src='eq_closed-loop3.gif']

For [feedforward-path closed-loop systems](closed-loop_est.html), you use the following two equations to describe the systems.

*y*(*k*) = *G*<sub>0</sub>(*z*)*u*(*k*) + *e*(*k*)

*u*(*k*) = [*r*(*k*) – *y*(*k*)]*F*<sub>y</sub>(*z*)

By combining the previous two equations, you can represent the feedforward-path closed-loop relationship with the following equation:

[IMAGE alt='image' src='eq_closed-loop4.gif']

If you define *G*<sub>cl</sub> as the feedforward-path closed-loop transfer function and let *G*<sub>cl</sub> satisfy the following equation:

[IMAGE alt='image' src='eq_closed-loop5.gif']

you can estimate *G*<sub>cl</sub> with *r*(*k*) as the input and *y*(*k*) as the output using an open loop method, because *r*(*k*) and *e*(*k*) are uncorrelated. You then can calculate *G*<sub>0</sub>after you calculate *G*<sub>cl</sub>, as the following equation shows:

[IMAGE alt='image' src='eq_closed-loop6.gif']

With indirect identification, you calculate *G*<sub>cl</sub>by performing polynomial operations on *G*<sub>o</sub> and *F*<sub>y</sub>. Because of the limitations of polynomial operations, the orders of the numerator and denominator might change after manipulation. Thus, the [SI Estimate Transfer Function Model](../lvsysid/est_transfer_function_model.html) VI or the [SI Transfer Function Estimation](../lvsysid/est_tf_model_express.html) Express VI, which you can use with the indirect identification approach, might return an error regarding the mismatch between the order you set and the order of the estimated model. In this case, you must adjust the tolerance setting of these two VIs so that the numerator and denominator orders match the orders you set. A larger tolerance facilitates zero-pole cancellations, which reduce the numerator and denominator polynomial orders.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/influencing_factors.html language=enus -->
## TOPIC 00091: Accounting for Factors that Influence a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/influencing_factors.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/influencing_factors.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Accounting for Factors that Influence a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The key to the system identification process is having some knowledge of the system for which you want to identify a model. This knowledge provides the basis for determining which signals are outputs, which in turn determines sensor placement, and which signals are inputs that you can use to excite the system. Simple tests might be necessary to determine influences, coupling, time delays, and time constants to aid in the modeling effort.

You also must consider signals that are not directly capable of being manipulated but still affect the system. You must include those signals as inputs to the system model. For example, consider the effect of wind gusts on the pitch dynamics of an airplane. The airplane responds in pitch to the elevator angle as a direct input. A wind gust affects the pitch of an airplane, which in turn influences the dynamics of the airplane, but the wind gust is not directly adjustable. To create an accurate model of the airplane, you might want to include wind gusts as an input variable.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/ir_correlation_analysis.html language=enus -->
## TOPIC 00092: Correlation Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/ir_correlation_analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/ir_correlation_analysis.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Correlation Analysis Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The correlation analysis method uses the cross correlation between the input and output signals as an estimation of the impulse response, as shown by the following equation:

[IMAGE alt='image' src='eq_correlation_analysis1.gif']

The input signal must be zero-mean white noise with a spectral density that is equally distributed across the whole frequency range. The [SI Estimate Impulse Response](../lvsysid/estimate_impulse_response.html) VI can prewhiten input signals that are not white noise.

Assuming the input *u*(*k*) of the system is a stationary, stochastic process and statistically independent of the disturbance *e*(*k*), the following equation is true.

[IMAGE alt='image' src='eq_correlation_analysis2.gif']

*R*<sub>uy</sub>represents the cross-correlation function between the stimulus signal *u*(*k*) and the response signal *y*(*k*), as defined by the following equation.

[IMAGE alt='image' src='eq_correlation_analysis3.gif']

*R*<sub>uu</sub> represents the autocorrelation of the stimulus signal *u*(*k*), as defined by the following equation.

[IMAGE alt='image' src='eq_correlation_analysis4.gif']

*N* is the number of data points. If the stimulus signal is a zero-mean white noise signal, the autocorrelation function reduces to the following equation.

[IMAGE alt='image' src='eq_correlation_analysis5.gif']

where *σ*<sub>u</sub> is the standard deviation of the stimulus white noise and *δ*(*τ*) is the Dirac function. Substituting *R*<sub>uu</sub>(*τ*) into the cross-correlation function between the stimulus signal *u*(*k*) and the response signal *y*(*k*) yields the following equation.

[IMAGE alt='image' src='eq_correlation_analysis6.gif']

You can rearrange the terms of this equation to obtain the following equation defining the impulse response *h*(*k*).

[IMAGE alt='image' src='eq_correlation_analysis7.gif']

#### Prewhitening

The correlation analysis method that estimates the impulse response is useful only when the input signal *u*(*k*) is a zero-mean white noise signal. However, the input signal is not white noise in most real-world applications. Therefore, you must precondition the input *u*(*k*) and output *y*(*k*) signals before you apply the correlation analysis method.

Prewhitening is a preconditioning technique for the correlation analysis method. Prewhitening involves applying a filter to the input signal *u*(*k*) and the output signal *y*(*k*) to obtain a prewhitened input signal *u'*(*k*) and a prewhitened output signal *y'*(*k*). If the filter is well designed such that *u'*(*k*) is white noise, you can perform a correlation analysis on *u'*(*k*) and *y'*(*k*) to estimate the impulse response. The impulse response that you estimate with *u'*(*k*) and *y'*(*k*) is equivalent to the impulse response that you estimate with *u*(*k*) and *y*(*k*) because the following equation remains true.

[IMAGE alt='image' src='eq_prewhitening.gif']

You now must design the prewhitening filter so that *u*'(*k*) is white noise. The SI Estimate Impulse Response VI uses an [AR](modeldefinitionsar.html) model for this purpose.

#### Accuracy of the Impulse Response

The accuracy of the impulse response estimation using the correlation analysis method depends on the performance of the prewhitening filter, specifically whether the filter produces a white noise result *u'*(*k*) for *u*(*k*). The performance of the filter depends on the signal and the AR order of the filter. The rule of thumb for selecting the AR order is trial-and-error. If *u'*(*k*) is not white enough, the result from the correlation method is not reliable. You can increase the AR order to improve the accuracy of the impulse response.

The SI Estimate Impulse Response VI provides the outputs **whiteness test** and **rejected?** to indicate whether you have properly set the AR order and consequently whether the impulse response estimation is reliable. The following example shows how the whiteness property of the input signal affects the correlation analysis method and how to use the outputs **whiteness test** and **rejected?** to justify the impulse response estimation.

The following figure shows the front panel of a VI that simulates a system defined by the following equation.

*y*(*k*) = 0.2*u*(*k*) + 0.8*u*(*k* – 1) + 0.3*u*(*k* – 2)

[IMAGE alt='image' src='prewhitening_fp.gif']

The following figure shows the block diagram of this VI. This example VI demonstrates the accuracy of the impulse response estimation in the following circumstances:

- Zero-mean, pseudo-white noise input signal without prewhitening
- Zero-mean, pseudo-white noise input signal with prewhitening
- Nonzero-mean, white noise input signal without prewhitening
- Nonzero-mean white noise input signal with prewhitening

[IMAGE alt='image' src='prewhitening_bd.gif']

In this example VI, the **is white noise?** checkbox determines whether the SI Estimate Impulse Response VI generates zero-mean white noise as an input to the system. When you place a checkmark in the **is white noise?** checkbox and run the VI, the generated input signal is zero-mean white noise, and the estimated impulse response closely approximates the true impulse response. When you do not place a checkmark in the **is white noise?** checkbox, the generated input signal is not zero-mean white noise. As a result, the estimated impulse response is different from the true impulse response. These results indicate that the correlation analysis method is accurate and reliable when the input signal is zero-mean white noise.

The **AR order** box determines the level of prewhitening. When **AR order** equals 0, the SI Estimate Impulse Response VI does not apply prewhitening to the system. When **AR order** is small and you do not place a checkmark in the **is white noise?** checkbox, the variance of the impulse response is large because the input signal is not always white noise. The greater the value of **AR order**, the better the VI whitens the signal, but the more computation time and memory the VI requires.

The **whiteness test** indicator of this VI shows whether the input is zero-mean white noise. This indicator displays the autocorrelation of the stimulus signal after whitening. If most of the autocorrelation is within the confidence region, the input signal is well prewhitened, and the estimation of the impulse response is reliable. If the autocorrelation is outside of the confidence region, the estimation is unreliable. When the estimation is unreliable, **rejected?** is TRUE and indicates a 5% risk of rejecting an impulse response estimation that might be reliable.

If you apply proper prewhitening, the correlation analysis method is accurate and reliable for any input signal. To obtain the best prewhitening settings, start with a small **AR order** value, such as 2, and observe the **whiteness test** and **rejected?** outputs of the SI Estimate Impulse Response VI. If necessary, increase the value of **AR order**. Generally, the smaller the bandwidth of the input signal, the larger the **AR order** you need. A large **AR order** slows the estimation performance. The default **AR order** value is 50.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/ir_least_squares.html language=enus -->
## TOPIC 00093: Least Squares Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/ir_least_squares.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/ir_least_squares.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Least Squares Method (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If both the input signal *u*(*k*) and output signal *y*(*k*) of a system are available, you can obtain the value of the impulse response *h*(*k*). This method does not require a [Dirac delta function](si_impulse_response.html) as the input signal of the system. Instead, you can use a [common stimulus signal](choosing_stimulus_signal.html) and the corresponding response signal from the system to compute the impulse response mathematically. You can obtain the impulse response for both positive and negative lags.

The Least Squares instance of the [SI Estimate Impulse Response](../lvsysid/estimate_impulse_response.html) VI implements the least squares method to obtain the value of *h*(*k*). Refer to the LabVIEW System Identification VIs Algorithm References manual for more information about the least squares method.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/joint_io_id.html language=enus -->
## TOPIC 00094: Joint Input-Output Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/joint_io_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/joint_io_id.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Joint Input-Output Identification (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you do not have any knowledge about the controller structure but the stimulus, response, and reference signals are all available, you can use the joint input-output identification approach to estimate the [transfer function](modeldefinitionstf.html) model of a dynamic system in a closed-loop system. This approach uses the transfer functions from different input-output signal pairs to estimate a closed-loop system. The [System Identification](../lvsysid/lv_sysid_pal.html) VIs implement the following two-stage method for the joint input-output approach.

1. Let T 0 ( z ) satisfy the following equation: [IMAGE alt='image' src='eq_joint_io1.gif']

By manipulating two equations describing the [feedback-path closed-loop system](closed-loop_est.html), you can rewrite *u*(*k*) as follows:

*u*(*k*) = *T*<sub>0</sub>(*z*)*r*(*k*) – *F*<sub>y</sub>(*z*)*T*<sub>0</sub>(*z*)*e*(*k*)

Any open-loop model estimation method then can estimate *T*<sub>0</sub>(*z*) because *r*(*k*) and *e*(*k*) are uncorrelated signals. After you obtain the value of *T*<sub>0</sub>(*z*), you can compute *û*(*k*) = *T*<sub>0</sub>(*z*)*r*(*k*). You then can represent *u*(*k*) as follows:

[IMAGE alt='image' src='eq_joint_io2.gif']

Using the previous equation, you obtain an input signal *û*(*k*), which is constructed from *r*(*k*) and is uncorrelated with the measurement noise.

1. By manipulating the equation y ( k ) = G 0 ( z ) u ( k ) + e ( k ), you can rewrite y ( k ) as follows: [IMAGE alt='image' src='eq_joint_io3.gif']

Because *û*(*k*) is uncorrelated with *e*(*k*), the original closed-loop model estimation problem between *u*(*k*) and *y*(*k*) becomes an open-loop problem between *û*(*k*) and *y*(*k*).

You use the same methodology to compute *y*(*k*) for a [feedforward-path closed-loop system](closed-loop_est.html), where

[IMAGE alt='image' src='eq_joint_io4.gif']

You rewrite *y*(*k*) as follows:

[IMAGE alt='image' src='eq_joint_io5.gif']

The two-stage method does not require you to know anything about the feedback or the controller structure and controller parameters. Also, you treat the closed-loop model estimation as an open-loop model estimation within each of the two steps. Therefore, you can use any method that works with open-loop models. Whether the real-world output noise is white noise or color noise, the two-stage method provides reliable estimations.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/kalman_filter.html language=enus -->
## TOPIC 00095: Kalman Filter (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/kalman_filter.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/kalman_filter.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Kalman Filter (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The Kalman filter is a linear optimum filter that minimizes the mean of the squared error recursively. The convergence rate of the Kalman filter is relatively fast, but the implementation is more complex than that of LMS-based algorithms.

Recall that the equation *J*(*k*) = *E*[*e*
 <sup>2</sup>(*k*)] defines the cost function. The following procedure lists the steps of the Kalman filter algorithm.

1. Initialize the parametric vector using a small positive number ε. 
 
 [IMAGE alt='image' src='eq_least_mean_sq3.gif']
2. Initialize the data vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq5.gif']
3. Initialize the k × k matrix P (0). 
 
 [IMAGE alt='image' src='eq_matrix_p1.gif']
4. For k = 1, update the data vector based on and the current input data u ( k ) and output data y ( k ).
5. Compute the predicted response by solving the following equation. 
 
 [IMAGE alt='image' src='eq_predicted_response3.gif']
6. Compute the error e ( k ) by solving the following equation. 
 
 [IMAGE alt='image' src='eq_system_error.gif']
7. Update the Kalman gain vector defined by the following equation. 
 
 [IMAGE alt='image' src='eq_gain_vector2.gif'] 
 
 
 Q 
 *M* is the measurement noise and P ( k ) is a k × k matrix whose initial value is defined by P (0) in step 3.
8. Update the parametric vector . 
 
 [IMAGE alt='image' src='eq_parametric_vector2.gif']
9. Update the P ( k ) matrix. 
 
 [IMAGE alt='image' src='eq_matrix_p3.gif'] 
 
 
 Q 
 *P* is the correlation matrix of the process noise.
10. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–10.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/least_mean_squares.html language=enus -->
## TOPIC 00096: Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/least_mean_squares.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/least_mean_squares.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The least mean squares (LMS) method uses the following equations to define the cost function *J*(*k*) = *E*[*e*
 <sup>2</sup>(*k*)].

The parametric vector [IMAGE alt='image' src='eq_predicted_response2.gif'] updates according to the following equation.

[IMAGE alt='image' src='eq_least_mean_sq1.gif']

*k* is the number of iterations, μ is step-size, which is a positive constant, and [IMAGE alt='image' src='eq_data_vector1.gif'] is the data vector from the past input data *u*(*k*) and output data *y*(*k*). [IMAGE alt='image' src='eq_data_vector1.gif'] is defined by the following equation.

[IMAGE alt='image' src='eq_least_mean_sq2.gif']

The following procedure describes how to implement the LMS algorithm.

1. Initialize the step-size μ.
2. Initialize the parametric vector using a small positive number ε. 
 
 [IMAGE alt='image' src='eq_least_mean_sq3.gif']
3. Initialize the data vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq5.gif']
4. For k = 1, update the data vector based on and the current input data u ( k ) and output data y ( k ).
5. Compute the predicted response using the following equation. 
 
 [IMAGE alt='image' src='eq_least_mean_sq6.gif']
6. Compute the error e ( k ) by solving the following equation. 
 
 [IMAGE alt='image' src='eq_system_error.gif']
7. Update the parameter vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq7.gif']
8. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–8.

The LMS algorithm is one of the most widely used and understood adaptive algorithms. Selecting the step-size μ is important with the LMS algorithm, because the selection of the step-size μ directly affects the rate of convergence and the stability of the algorithm. The convergence rate of the LMS algorithm is usually proportional to the step-size μ. The larger the step-size μ, the faster the convergence rate. However, a large step-size μ can cause the LMS algorithm to become unstable. The following equation describes the range of the step-size μ.

0 < μ < μ
 <sub>max</sub>

μ
 <sub>max</sub> is the maximum step-size that maintains stability in the LMS algorithm. μ
 <sub>max</sub> is related to the statistical property of the stimulus signal. A uniformly optimized step-size μ that achieves a fast convergence speed while maintaining the stability in the system does not exist, regardless of the statistical property of the stimulus signal. For better performance, use a self-adjustable step-size μ and the [normalized least mean squares (NLMS)](normalized_lms.html) algorithm.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/model-based_cd.html language=enus -->
## TOPIC 00097: Model-Based Control Design Process (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/model-based_cd.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/model-based_cd.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Model-Based Control Design Process (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The model-based control design process involves building a model of a plant, analyzing and synthesizing a controller for the plant, simulating the plant and controller, and deploying the controller. National Instruments provides a complete solution for identifying and validating a plant model, designing a controller for the model, analyzing the controller, and prototyping and deploying the control system. The following figure shows this process, which is based on LabVIEW and National Instruments Real-Time (RT) Series hardware.

[IMAGE alt='image' src='noloc_eps_ni_tool_chain.gif']

#### Analyzing Data and Creating a Plant Model

In the initial phase of the design process, you must obtain a mathematical model of the plant you want to control. One way to obtain a model is by using a numerical process known as system identification. This process involves acquiring data from a plant and then numerically analyzing stimulus and response data to estimate the parameters of the plant.

National Instruments provides DAQ and modular instrumentation software and hardware that you can use to stimulate and measure the response of the plant. You then can use the [System Identification](../lvsysid/lv_sysid_pal.html) VIs to estimate and create accurate mathematical models of the plant.

System identification is a process that includes [acquiring](acquiring_data.html) and [preprocessing](preprocessing_data.html) raw data from a dynamic system and [identifying mathematical models](estimating_models.html) based on the raw data. You then [validate](validating_models.html) that the resulting model accurately describes the observed system behavior. If the results are unsatisfactory, you revise the parameters and iterate through the process. The following flowchart shows a typical system identification process.

[IMAGE alt='image' src='noloc_eps_system_id_app_flowchart.gif']

A real-world system seldom has one model that perfectly describes all the observed behaviors of the system. Because system identification involves many variables—such as sampling frequency, type of mathematical model, model order, and so on—you usually have a number of models you can use. Each model describes the behavior of the system to some extent or in a particular mode of operation.

Furthermore, multiple applicable algorithms might be available for the same model. The algorithms you select depend on the model structure, stochastic assumptions, and numerical properties of the algorithm. The System Identification VIs include different adaptive techniques for [recursive system identification](recursive_est.html) and different algorithms for model estimation.

#### Designing a Controller

In the second phase of the design process, you synthesize and analyze a controller. The LabVIEW Control Design and Simulation Module provides a set of VIs for classical and modern linear control analysis and design techniques. With these VIs you can design, implement, and deploy linear time-invariant (LTI) system models.

You can use the Control Design and Simulation Module to analyze the plant model you identified with the System Identification VIs. The Control Design and Simulation VIs help you determine an appropriate controller structure. You then can synthesize a controller to achieve the desired performance criteria of the system based on the dynamic behavior of the plant and/or control system. Finally, you can analyze the overall system by combining the controller with the identified plant model.

#### Simulating the Plant

In the third phase of the design process, you simulate the plant. You can simulate plants in LabVIEW by using the Control Design and Simulation Module. You can use this software to perform offline simulations of a linear or nonlinear plant model. You can use this simulation to investigate the time and frequency responses of the plant due to complex, time-varying inputs. If you install the LabVIEW Real-Time Module, you also can perform rapid control prototyping (RCP), and hardware-in-the-loop (HIL) simulations by using NI RT Series hardware.

#### Deploying the Controller

The last stage of the design process is to deploy the controller to an RT target, such as a PXI or CompactRIO controller. LabVIEW, the Control Design and Simulation Module, the Real-Time Module, and NI RT Series hardware provide a common platform that you can use to design, prototype, and deploy the embedded control system. You also can use the Control Design and Simulation Module and the Real-Time Module as the platform for implementing the control system.

National Instruments also provides products for I/O and signal conditioning, such as NI DAQ and SCXI devices, that you can use to gather and process data. Using these tools, which are built on the LabVIEW platform, you can experiment with different approaches at each stage in the design process and quickly identify the optimal design solution for an embedded control system.

Refer to the National Instruments website for more information about these National Instruments products.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/model_types_and_reps.html language=enus -->
## TOPIC 00098: Model Types and Representations (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/model_types_and_reps.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/model_types_and_reps.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Model Types and Representations (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can represent a dynamic system using several types of dynamic system models.

#### Model Types

You base the type of a dynamic system model on the properties of the dynamic system that the model represents.

##### Linear versus Nonlinear Models

Dynamic system models are either linear or nonlinear. A linear model obeys the principles of superposition and homogeneity. The following equations are true for linear models.

*y*<sub>1</sub> = *f*(*u*<sub>1</sub>)

*y*<sub>2</sub> = *f*(*u*<sub>2</sub>)

*f*(*u*<sub>1</sub> + *u*<sub>2</sub>) = *f*(*u*<sub>1</sub>) + *f*(*u*<sub>2</sub>) = *y*<sub>1</sub> + *y*<sub>2</sub>

*f*(*a**u*<sub>1</sub>) = *a**f*(*u*<sub>1</sub>) = *a**y*<sub>1</sub>

where *u*<sub>1</sub> and *u*<sub>2</sub> are the system inputs, *y*<sub>1</sub> and *y*<sub>2</sub> are the system outputs, and *a* is a constant.

Conversely, nonlinear models do not obey the principles of superposition or homogeneity. Nonlinear effects in real-world systems include saturation, dead-zone, friction, backlash, and quantization effects; relays; switches; and rate limiters. Many real-world systems are nonlinear, but you can simulate most real-world systems with linear models to simplify a design or analysis procedure.

##### Time-Variant versus Time-Invariant Models

Dynamic system models are either time-variant or time-invariant. The parameters of a time-variant model change with time. For example, you can use a time-variant model to describe an automobile. As fuel burns, the mass of the vehicle changes with time.

Conversely, the parameters of a time-invariant model do not change with time. For an example of a time-invariant model, consider a simple robot. Generally, the dynamic characteristics of robots do not change over short periods of time.

##### Continuous versus Discrete Models

Dynamic system models are either continuous or discrete. Both continuous and discrete system models can be linear or nonlinear and time-invariant or time-variant. Continuous models describe how the behavior of a system varies continuously with time, which means you can obtain the properties of a system at any certain moment from the continuous model. Discrete models describe the behavior of a system at separate time instants, which means you cannot obtain the behavior of the system between every two sampling points.

Continuous system models are analog. You derive continuous models of a physical system from differential equations of the system. The coefficients of continuous models have clear physical meanings. For example, you can derive the continuous transfer function of an RC circuit if you know the details of the circuit. The coefficients of the continuous transfer function are the functions of *R* and *C* in the circuit. You use continuous models if you need to match the coefficients of a model to some physical components in the system.

Discrete system models are digital. You derive discrete models of a physical system from difference equations or by converting continuous models to discrete models. In computer-based applications, signals and operations are digital. Thus, you can use discrete models to implement a digital controller or to simulate the behavior of a physical system at discrete instants. You also can use discrete models in the accurate model-based design of a discrete controller for a dynamic system.

##### SISO, SIMO, MISO, and MIMO Models

Dynamic system models contain different numbers of inputs and outputs. You can classify dynamic system models into the following types by the input and output numbers of the dynamic system that the model represents.

- Single-Input Single-Output (SISO) Models
- Single-Input Multiple-Output (SIMO) Models
- Multiple-Input Single-Output (MISO) Models
- Multiple-Input Single-Output (MIMO) Models

The [System Identification](../lvsysid/lv_sysid_pal.html) VIs include VIs with different polymorphic instances of VIs for these types of models. Use the corresponding polymorphic instances of VIs to estimate these types of models. You can use the MIMO instances of System Identification VIs to estimate MISO, SIMO, and SISO models by adding an empty dimension to the input signals, output signals, or both signals of the dynamic system.

#### Model Representations

You can use the System Identification VIs to represent each model [type](#model_types) in any of the following representations:

- Transfer function models
- Zero-pole-gain models
- State-space models

If the model is discrete, you also can use a [general-linear polynomial](modeldefinitionsgl.html) model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsar.html language=enus -->
## TOPIC 00099: AR Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsar.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsar.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### AR Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The autoregressive (AR) model does not include the dynamics between the system input and output. Therefore, the AR model is more suitable for representing signals rather than a system because a system generally has an input and an output. Time series analysis methods, such as power spectrum envelope estimation, prewhitening, and linear prediction coding, commonly use the AR model. Refer to the *Time Series Analysis Tools User Manual* at ni.com/manuals for more information about time series analysis methods.

Use the [SI Estimate AR Model](../lvsysid/estimate_ar_model.html) VI to estimate AR system models. The following equation shows the form of the AR model.

*A*(*z*)*y*(*k*) = *e*(*k*)

| where | y(k) is the system outputs |
| --- | --- |
|  | e(k) is the system disturbance |

*A*(*z*) is polynomial with respect to the backward shift operator *z*
 <sup>–1</sup> and defined by the following equation.

[IMAGE alt='image' src='a_q_poly_equation.gif']

| where | ka is the model order |
| --- | --- |

The following figure depicts the signal flow of an AR system model.

[IMAGE alt='image' src='noloc_eps_estimate_armodel_details2.gif']

| where | e is the system disturbance |
| --- | --- |
|  | y is the system outputs |
|  | A is A(z) |

If you consider *A*(*z*) to be a filter, *A*(*z*)*y*(*k*) is the filtering of *A*(*z*) on the signal *y*(*k*). The result of the filtering is white noise *e*(*k*), as shown in the AR model equation. Hence, the filter *A*(*z*) also is known as the [prewhitening](ir_correlation_analysis.html#prewhitening) filter. From the frequency-domain standpoint, the prewhitening filter *A*(*z*) suppresses the spectrum at frequencies where the magnitude of the spectrum is large. Suppressing the high-magnitude frequencies results in a flat spectrum.

As shown in the AR model equation, if you know the AR coefficients *A*(*z*) and the noise *e*(*k*), you can reconstruct the signal *y*(*k*). *A*(*z*) and *e*(*k*) completely characterize a signal. *A*(*z*) normally has a small number of coefficients. *e*(*k*) has a small dynamic range and requires a smaller number of bits for encoding. Therefore, you can use the AR model for compression purposes in a process known as linear prediction coding (LPC). Speech and vibration signal processing methods, such as compression and pattern recognition, commonly use LPC. You also can use *A*(*z*) and *e*(*k*) to estimate the power spectrum of the signal *y*(*k*).

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsarmax.html language=enus -->
## TOPIC 00100: ARMAX Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsarmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsarmax.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### ARMAX Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When *D*(*z*) and *F*(*z*) equal 1, the [general-linear polynomial model](modeldefinitionsgl.html) reduces to an autoregressive-moving average with exogenous terms (ARMAX) model. Unlike the [autoregressive with exogenous terms](modeldefinitionsarx.html) (ARX) model, the system structure of an ARMAX model includes the stochastic dynamics. ARMAX models are useful when you have dominating disturbances that enter early in the process, such as at the input. For example, a wind gust affecting an aircraft is a dominating disturbance early in the process. The ARMAX model has more flexibility than the ARX model in handling models that contain disturbances.

Use the [SI Estimate ARMAX Model](../lvsysid/estimate_armax_model.html) VI to estimate ARMAX models. This VI uses the Gauss-Newton method to optimize the mean square value of the prediction error when searching for the optimal ARMAX model. This searching process is iterative and might converge to a local minimum rather than a global minimum. Therefore, you must [validate](validating_models.html) the estimated model. If the estimated model passes the validation test, you can use this model even if the SI Estimate ARMAX Model VI might locate only a local minimum.

The following equation shows the form of the ARMAX model.

*A*(*z*)*y*(*k*) = *B*(*z*)*u*(*k* - *n*) + *C*(*z*)*e*(*k*)

| where | y(k) is the system outputs |
| --- | --- |
|  | u(k) is the system inputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |

*A*(*z*), *B*(*z*), and *C*(*z*) are polynomial with respect to the backward shift operator *z*
 <sup>–1</sup> and defined by the following equations.

[IMAGE alt='image' src='a_q_poly_equation.gif']

[IMAGE alt='image' src='b_q_poly_equation.gif']

[IMAGE alt='image' src='c_q_poly_equation.gif']

The following figure depicts the signal flow of an ARMAX model.

[IMAGE alt='image' src='noloc_eps_est_armax_model_details2.gif']

| where | u is the system inputs |
| --- | --- |
|  | e is the system disturbance |
|  | y is the system outputs |
|  | A is A(z) |
|  | B is B(z) |
|  | C is C(z) |

#### SISO

The following is the time domain equation for the ARMAX SISO model.

[IMAGE alt='image' src='armaxsisomodeleqn.gif']

| where | ka is the A order |
| --- | --- |
|  | kb is the B order |
|  | kc is the C order |
|  | n is the system delay |
|  | e(k) is the system disturbance |

Refer to the Estimate Polynomial Models VI in the labview\examples\System Identification\Getting Started\Parametric Estimation.llb for an example that demonstrates how to estimate ARMAX models for an unknown system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsarx.html language=enus -->
## TOPIC 00101: ARX Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsarx.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsarx.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### ARX Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When *C*(*z*), *D*(*z*), and *F*(*z*) equal 1, the [general-linear polynomial model](modeldefinitionsgl.html) reduces to an autoregressive with exogenous terms (ARX) model. This model is the simplest model that incorporates the stimulus signal. However, the ARX model captures some of the stochastic dynamics as part of the system dynamics. In this model, the transfer function of the deterministic part *G*(*z*
 <sup>–1</sup>, θ) of the system and the transfer function of the stochastic part *H*(*z*
 <sup>–1</sup>, θ) of the system have the same set of poles. This coupling can be unrealistic. The system dynamics and stochastic dynamics of a system do not share the same set of poles all the time. You can reduce this disadvantage if the signal-to-noise ratio is high.

When the disturbance *e*(*k*) of a system is not white noise, the coupling between the deterministic and stochastic dynamics can bias the estimation of the ARX model. You can set the model order higher than the actual model order to minimize the estimation error, especially when the signal-to-noise ratio is low. However, increasing the model order can change some dynamic characteristics of the model, such as the stability of the model.

Use the [SI Estimate ARX Model](../lvsysid/estimate_arx_model.html) VI to estimate ARX models. The identification method for the ARX model is the [least squares method](ir_least_squares.html), which is a special case of the [prediction error method](parameters_for_pe.html). The least squares method is the most efficient polynomial estimation method because this method solves linear regression equations in analytic form. Moreover, the solution is unique. Refer to the LabVIEW System Identification VIs Algorithm References manual for more information about the least squares and prediction error methods.

The following equation shows the form of the ARX model.

*A*(*z*)*y*(*k*) = *B*(*z*)*u*(*k* - *n*) + *e*(*k*)

| where | u(k) is the system inputs |
| --- | --- |
|  | y(k) is the system outputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |

*A*(*z*) and *B*(*z*) are polynomial with respect to the backward shift operator *z*
 <sup>–1</sup> and defined by the following equations.

[IMAGE alt='image' src='a_q_poly_equation.gif']

[IMAGE alt='image' src='b_q_poly_equation.gif']

|  | Note The backward shift operator makes z –n u(k) = u(k - n). |
| --- | --- |

The following figure depicts the signal flow of an ARX model.

[IMAGE alt='image' src='noloc_eps_est_arx_model_details2.gif']

| where | u is the system inputs |
| --- | --- |
|  | e is the system disturbance |
|  | y is the system outputs |
|  | A is A(z) |
|  | B is B(z) |

#### SISO

The following is the time domain equation for the ARX SISO model.

[IMAGE alt='image' src='arxsisomodeleqn.gif']

| where | ka is the A order |
| --- | --- |
|  | kb is the B order |
|  | n is the system delay |
|  | e(k) is the system disturbance |

Refer to the Estimate Polynomial Models VI in the labview\examples\System Identification\Getting Started\Parametric Estimation.llb for an example that demonstrates how to estimate ARX models for an unknown system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsbj.html language=enus -->
## TOPIC 00102: Box-Jenkins Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsbj.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsbj.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Box-Jenkins Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When *A*(*z*) equals 1, the [general-linear polynomial model](modeldefinitionsgl.html) reduces to the Box-Jenkins model. This model provides a complete model of a system because this model represents disturbance properties separately from system dynamics. This model is useful when you have disturbances that enter late in the process, such as measurement noise on the output.

Use the [SI Estimate BJ Model](../lvsysid/estimate_bj_model.html) VI to estimate Box-Jenkins models. The identification method of the Box-Jenkins model is the [prediction error method](parameters_for_pe.html), which is the same as that of the [ARMAX model](modeldefinitionsarmax.html).

The following equation shows the form of the Box-Jenkins model.

[IMAGE alt='image' src='est_bj_model_details1.gif']

| where | y(k) is the system outputs |
| --- | --- |
|  | u(k) is the system inputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |

*B*(*z*), *C*(*z*), *D*(*z*), and *F*(*z*) are polynomial with respect to the backward shift operator *z*
 <sup>-1</sup> and defined by the following equations.

[IMAGE alt='image' src='b_q_poly_equation.gif']

[IMAGE alt='image' src='c_q_poly_equation.gif']

[IMAGE alt='image' src='d_q_poly_equation.gif']

[IMAGE alt='image' src='f_q_poly_equation.gif']

The following figure depicts the signal flow of a Box-Jenkins model.

[IMAGE alt='image' src='noloc_eps_est_bj_model_details2.gif']

| where | u is the system inputs |
| --- | --- |
|  | e is the system disturbance |
|  | y is the system outputs |
|  | v and ω are the auxiliary variables |

#### SISO

The following are the time domain equations for the Box-Jenkins SISO model.

[IMAGE alt='image' src='oesisomodeleqn1.gif']

[IMAGE alt='image' src='bjsisomodeleqn2.gif']

[IMAGE alt='image' src='bjsisomodeleqn3.gif']

| where | kf is the F order |
| --- | --- |
|  | kb is the B order |
|  | kc is the C order |
|  | kd is the D order |
|  | u(k) is the system input |
|  | n is the system delay |
|  | e(k) is the system disturbance |
|  | w is the auxiliary variable |

Refer to the Estimate Polynomial Models VI in the labview\examples\System Identification\Getting Started\Parametric Estimation.llb for an example that demonstrates how to estimate Box-Jenkins models for an unknown system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsgl.html language=enus -->
## TOPIC 00103: General-Linear Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsgl.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsgl.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### General-Linear Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Generally, you can describe a [discrete system](model_types_and_reps.html#model_types) by using the general-linear polynomial model. This model provides flexibility for both system dynamics and stochastic dynamics.

Use the [SI Estimate General Linear Model](../lvsysid/est_general_linear_model.html) VI to estimate general-linear polynomial models. The following equation describes this model.

*y*(*k*) = *z*
 <sup>–n</sup>
 *G*(*z*
 <sup>–1</sup>, θ)*u*(*k*) + *H*(*z*
 <sup>–1</sup>, θ)*e*(*k*)

| where | u(k) and y(k) are the input and output of the system, respectively |
| --- | --- |
|  | e(k) is the disturbance of the system which usually is zero-mean white noise |
|  | G(z–1, θ) is the transfer function of the deterministic part of the system |
|  | H(z–1, θ) is the transfer function of the stochastic part of the system |

The deterministic transfer function specifies the relationship between the output and the input signal. The stochastic transfer function specifies how the random disturbance affects the output signal. Often the deterministic and stochastic parts of a system are referred to as system dynamics and stochastic dynamics, respectively.

The term *z*
 <sup>–1</sup> is the backward shift operator, which is defined by the following equations:

*z*
 <sup>–1</sup>
 *x*(*k*) = *x*(*k* - 1)

*z*
 <sup>–2</sup>
 *x*(*k*) = *x*(*k* - 2)

...

*z*
 <sup>*–n*</sup>
 *x*(*k*) = *x*(*k* - *n*)

*z*
 <sup>*–n*</sup> defines the number of delay samples between the input and the output.

*G*(*z*
 <sup>–1</sup>, θ)*u*(*k*) and *H*(*z*
 <sup>–1</sup>, θ)*e*(*k*) are rational polynomials as defined by the following equations:

[IMAGE alt='image' src='eq_g_polynomial.gif']

[IMAGE alt='image' src='eq_h_polynomial.gif']

The vector θ is the set of model parameters. The following equations do not display θ to make the equations easier to read.

The following equation shows the form of the general-linear model.

[IMAGE alt='image' src='est_gen_lin_details1.gif']

| where | y(k) is the system outputs |
| --- | --- |
|  | u(k) is the system inputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |

*A*(*z*), *B*(*z*), *C*(*z*), *D*(*z*), and *F*(*z*) are polynomial with respect to the backward shift operator *z*
 <sup>-1</sup> and defined by the following equations.

[IMAGE alt='image' src='a_q_poly_equation.gif']

[IMAGE alt='image' src='b_q_poly_equation.gif']

[IMAGE alt='image' src='c_q_poly_equation.gif']

[IMAGE alt='image' src='d_q_poly_equation.gif']

[IMAGE alt='image' src='f_q_poly_equation.gif']

The following figure depicts the signal flow of a general-linear model.

[IMAGE alt='image' src='noloc_eps_est_gen_lin_details2.gif']

| where | u is the system inputs |
| --- | --- |
|  | e is the system disturbance |
|  | y is the system outputs |
|  | v and ω are the auxiliary variables |

Setting one or more of *A*(*z*), *C*(*z*), *D*(*z*), and *F*(*z*) to 1 can create simpler models such as autoregressive with exogenous terms ([ARX](modeldefinitionsarx.html)), autoregressive-moving average with exogenous terms ([ARMAX](modeldefinitionsarmax.html)), [output-error](modeldefinitionsoe.html), and [Box-Jenkins](modeldefinitionsbj.html) models, which you commonly use in real-world applications.

#### SISO

The following are the time domain equations for the general-linear SISO model.

[IMAGE alt='image' src='oesisomodeleqn1.gif']

[IMAGE alt='image' src='bjsisomodeleqn2.gif']

[IMAGE alt='image' src='glsisomodeleqn3.gif']

| where | kf is the F order |
| --- | --- |
|  | kb is the B order |
|  | kc is the C order |
|  | kd is the D order |
|  | ka is the A order |
|  | u(k) is the system inputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |
|  | w is the auxiliary variable |

Refer to the Estimate Polynomial Models VI in the labview\examples\System Identification\Getting Started\Parametric Estimation.llb for an example that demonstrates how to estimate general-linear polynomial models for an unknown system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsoe.html language=enus -->
## TOPIC 00104: Output-Error Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsoe.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsoe.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Output-Error Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

When *A*(*z*), *C*(*z*), and *D*(*z*) equal 1, the [general-linear polynomial](modeldefinitionsgl.html) model reduces to the output-error model. This model describes the system dynamics separately from the stochastic dynamics. The output-error model does not use any parameters for simulating the disturbance characteristics.

Use the [SI Estimate OE Model](../lvsysid/estimate_oe_model.html) VI to estimate output-error models. The identification method of the output-error model is the [prediction error method](parameters_for_pe.html), which is the same as that of the [ARMAX](modeldefinitionsarmax.html) model. If the disturbance *e*(*k*) is white noise, all minima are global. However, a local minimum can exist if the disturbance is not white noise.

The following equation shows the form of the output-error model.

[IMAGE alt='image' src='est_oe_model_details1.gif']

| where | y(k) is the system outputs |
| --- | --- |
|  | u(k) is the system inputs |
|  | n is the system delay |
|  | e(k) is the system disturbance |

*B*(*z*) and *F*(*z*) are polynomials with respect to the backward shift operator *z*
 <sup>–1</sup> and defined by the following equations.

[IMAGE alt='image' src='b_q_poly_equation.gif']

[IMAGE alt='image' src='f_q_poly_equation.gif']

The following figure depicts the signal flow of an output-error model.

[IMAGE alt='image' src='est_oe_model_details2.gif']

| where | u is the system inputs |
| --- | --- |
|  | e is the system disturbance |
|  | y is the system outputs |
|  | ω is the auxiliary variable |

#### SISO

The following are the time domain equations for the output-error SISO model.

[IMAGE alt='image' src='oesisomodeleqn1.gif']

[IMAGE alt='image' src='oesisomodeleqn2.gif']

| where | kf is the F order |
| --- | --- |
|  | kb is the B order |
|  | n is the system delay |
|  | e(k) is the system disturbance |
|  | w is the auxiliary variable. |

Refer to the Estimate Polynomial Models VI in the labview\examples\System Identification\Getting Started\Parametric Estimation.llb for an example that demonstrates how to estimate Output-Error models for an unknown system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsss.html language=enus -->
## TOPIC 00105: State-Space Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsss.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsss.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### State-Space Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The state-space model is the most convenient model for describing multiple-input multiple-output (MIMO) systems. State-space models often are preferable to polynomial models, especially in modern control applications that focus on multivariable systems. You can estimate both [continuous and discrete](model_types_and_reps.html) state-space models.

#### Continuous

Use [partially known model estimation methods](partially_known_est.html) to estimate continuous state-space models. You must provide an initial guess for each parameter before conducting estimation. The following equations show the form of the continuous state-space model.

[IMAGE alt='image' src='canssreal_eq1.gif']

| where | A is an n × n state matrix of the given system |
| --- | --- |
|  | B is an n × m input matrix of the given system |
|  | C is an r × n output matrix of the given system |
|  | D is an r × m direct transmission matrix of the given system |
|  | K is the Kalman gain matrix |
|  | e is the system disturbance |

#### Discrete

Use the [SI Estimate State-Space Model](../lvsysid/est_state_space_model.html) and [SI Estimate State-Space Model from FRF](../lvsysid/est_ss_from_frf.html) VIs to estimate [discrete](model_types_and_reps.html) state-space models. The SI Estimate State-Space Model VI supports the following two estimation methods:

- Deterministic-stochastic subspace method —This method uses principal component analysis to estimate parameters. This method uses both stimulus and response signals to estimate state-space models. This method includes the stochastic parts of the system in the model structure.
- Realization method —This method uses the impulse response to estimate only the deterministic state-space model. This method does not include stochastic parts of the system in the model structure.

Refer to the LabVIEW System Identification VIs Algorithm References manual for more information about the deterministic-stochastic subspace method and the realization method.

The following equations show the form of the discrete state-space model.

*x*(*k* + 1) = *A**x*(*k*) + *B**u*(*k*) + *K**e*(*k*)

*y*(*k*) = *C**x*(*k*) + *D**u*(*k*) + *e*(*k*)

|  | Note The equations for the discrete state-space model based on frequency-domain data do not contain Ke(k) and e(k). |
| --- | --- |

| where | k is the model sampling time multiplied by the discrete time step, where the discrete time step equals 0, 1, 2, … |
| --- | --- |
|  | n is the number of model states |
|  | m is the number of model inputs |
|  | r is the number of model outputs |
|  | x is the model state vector |
|  | u is the model input vector |
|  | y is the model output vector |
|  | e(k) is the system disturbance |

The state-space transfer matrices *A*, *B*, *C*, and *D* often reflect physical characteristics of a system. The dimension of the state vector *x* is the only setting you must provide for the state-space model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionstf.html language=enus -->
## TOPIC 00106: Transfer Function Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionstf.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionstf.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Transfer Function Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can use a transfer function to define either a [continuous system or a discrete](model_types_and_reps.html) system. The following equations describe a continuous system and a discrete system, respectively, from which the transfer function is derived.

*y*(*t*) = *G*(*s*)*u*(*t*) + *e*(*t*)

*y*(*k*) = *G*(*z*)*u*(*k*) + *e*(*k*)

| where | y(t) and y(k) are the system outputs |
| --- | --- |
|  | G(s) and G(z) is the transfer function between the stimulus and the response |
|  | u(t) and u(k) are the system inputs |
|  | e(t) and e(k) are the system disturbance |

|  | Note Continuous models use the s variable to define time whereas discrete models use the z variable. |
| --- | --- |

#### SISO

The following is the equation for the continuous transfer function SISO model.

[IMAGE alt='image' src='continuoustransferfunction.gif']

| where | s is the Laplace variable and continuous time |
| --- | --- |
|  | m is the order of the numerator polynomial function |
|  | n is the order of the denominator polynomial function |
|  | bm are the coefficients of the numerator polynomial function |
|  | an are the coefficients of the numerator polynomial function |
|  | Td is the system delay |

|  | Note For transfer function SISO models based on frequency-domain data, Td equals zero. |
| --- | --- |

The following is the equation for the discrete-time transfer function SISO model.

[IMAGE alt='image' src='discretetransferfunctioneq.gif']

| where | z is discrete time |
| --- | --- |
|  | m is the order of the numerator polynomial function |
|  | n is the order of the denominator polynomial function |
|  | bm are the coefficients of the numerator polynomial function |
|  | an are the coefficients of the numerator polynomial function |

#### MISO

The following is the equation for the continuous transfer function MISO model.

[IMAGE alt='image' src='continuouszpk_mimo.gif']

| where | Gij are the transfer functions between the stimulus and the response |
| --- | --- |
|  | i is the input number of the system |
|  | j is the output number of the system |

The following is the equation for the discrete-time transfer function MISO model.

[IMAGE alt='image' src='discretezpk_mimo.gif']

You can use the [SI Estimate Transfer Function Model](../lvsysid/est_transfer_function_model.html) VI to estimate both continuous and discrete models. For discrete models, this VI implements the [prediction error method](parameters_for_pe.html). For continuous models, this VI internally performs the following three consecutive steps to estimate the model:

1. Calculates a discrete model with the prediction error method.
2. Applies the Zero-Order-Hold method to convert the discrete model to a continuous model.
3. Uses the Gauss-Newton method to optimize the continuous model this VI converted in step 2.

You can [use](freqsysid_case_study.html) the [SI Estimate Transfer Function Model from FRF](../lvsysid/est_tf_from_frf.html) VI to estimate both continuous and discrete SISO models in the frequency domain.

Transfer function models describe only the deterministic part of the system. For stochastic control, [general-linear polynomial models](modeldefinitionsgl.html) commonly are used because these models separately describe the deterministic and stochastic parts of a system. However, in classical control engineering, the deterministic part of the system is more important than the stochastic part. Therefore, you can take advantage of the relationship between input and output signals of the transfer function model to describe the deterministic part of the system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionsud.html language=enus -->
## TOPIC 00107: User Defined Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionsud.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionsud.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### User Defined Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If a [general-linear polynomial](modeldefinitionsgl.html), [transfer function](modeldefinitionstf.html), [zero-pole-gain](modeldefinitionszpg.html), or [state-space](modeldefinitionsss.html) model cannot represent the model you want to estimate, you can define a model by revising a template VI. You can find template VIs in the \vi.lib\addons\System Identification\User-Defined Model Templates.llb. You then can estimate the model you define by using the [SI Estimate User-Defined Model](../lvsysid/est_user-defined_model.html) VI. This VI enables you to estimate some other model representations in addition to the general-linear, transfer function, zero-pole-gain, and state-space models that the [System Identification](../lvsysid/lv_sysid_pal.html) VIs directly support. For example, you can use this VI to estimate nonlinear models. With this VI, you also can estimate linear models that you define early.

Refer to the following VIs for examples that demonstrate how to use the SI Estimate User-Defined Model VI.

Estimate Hammerstein Model VI in the labview\examples\System Identification\Getting Started\User Defined Model.llb

Estimate Hammerstein-Weiner Model VI in the labview\examples\System Identification\Getting Started\User Defined Model.llb

Estimate Weiner Model VI in the labview\examples\System Identification\Getting Started\User Defined Model.llb

Parameterize Nonlinear Differential Equation Model VI in the labview\examples\System Identification\Getting Started\User Defined Model.llb

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/modeldefinitionszpg.html language=enus -->
## TOPIC 00108: Zero-Pole-Gain Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/modeldefinitionszpg.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/modeldefinitionszpg.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Zero-Pole-Gain Model Definitions (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you rewrite the equations for the [transfer function](modeldefinitionstf.html) model to show the locations of the zeros and poles of the dynamic system, you obtain the zero-pole-gain model.

#### SISO

The following is the equation for the continuous zero-pole-gain SISO model.

[IMAGE alt='image' src='continuouszpk_siso.gif']

| where | s is the Laplace variable and continuous time |
| --- | --- |
|  | k is the transfer function gain |
|  | Zi are the zeros |
|  | Pj are the poles |

The following is the equation for the discrete-time zero-pole-gain SISO model.

[IMAGE alt='image' src='discretezpkeq.gif']

| where | z is discrete time |
| --- | --- |

When *s* or *z* equals 0, you can calculate the static gain from the two equations.

[IMAGE alt='image' src='zpk_model_definition_s0.gif']

#### MISO

The following is the equation for the continuous zero-pole-gain MISO model.

[IMAGE alt='image' src='continuouszpk_mimo.gif']

| where | Gij are the transfer functions between the stimulus and the response |
| --- | --- |
|  | i is the input number of the system |
|  | j is the output number of the system |

The following is the equation for the discrete-time zero-pole-gain MISO model.

[IMAGE alt='image' src='discretezpk_mimo.gif']

The [System Identification](../lvsysid/lv_sysid_pal.html) VIs do not include a VI to estimate zero-pole-gain models directly because you can use the [SI Model Conversion](../lvsysid/model_conversion_vi.html) VI to [convert another model representation](converting_models.html) to a zero-pole-gain model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/normalized_lms.html language=enus -->
## TOPIC 00109: Normalized Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/normalized_lms.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/normalized_lms.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Normalized Least Mean Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The following equation defines a popular self-adjustable step-size μ(*k*) that you use in the normalized least mean squares (NLMS) algorithm.

[IMAGE alt='image' src='eq_normalized_lmsq1.gif']

[IMAGE alt='image' src='eq_data_vector1.gif'] represents the data vector. ε is a very small positive number that prevents the denominator from equaling zero when [IMAGE alt='image' src='eq_normalized_lmsq2.gif'] approaches zero.

The step-size μ(*k*) is time-varying because the step-size changes with the time index *k*.

Substituting μ(*k*) into the parametric vector [IMAGE alt='image' src='eq_parametric_vector1.gif'] equation yields the following equation.

[IMAGE alt='image' src='eq_normalized_lmsq3.gif']

Compared to the [least mean squares (LMS)](least_mean_squares.html) algorithm, the NLMS algorithm is always stable if the step-size μ(*k*) is between zero and two, regardless of the statistical property of the stimulus signal *u*(*k*).

The procedure of the NLMS algorithm is the same as the LMS algorithm except for the estimation of the time-varying step-size μ(*k*).

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/partially_known_est.html language=enus -->
## TOPIC 00110: Partially Known Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/partially_known_est.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/partially_known_est.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Partially Known Model Estimation Methods (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The [nonparametric](nonparametric_est.html) and [parametric](parametric_est.html) model estimation methods, also known as black-box estimation methods, assume that systems are unknown. Because these estimation methods do not take prior system knowledge into account, you must use either an algorithm or trial-and-error to vary model parameters until the behavior of the model matches the measured input-output data. Although you can use the estimated parameters to reproduce the response of the system accurately, these parameters might not have any physical meanings.

However, in practice, many systems are partially known because you have information about the underlying dynamics or some of the physical parameters. You can use [partially known](define_est_pk.html) model estimation methods, also known as grey-box estimation methods, to estimate models when you have this information.

Black-box methods also assume that all model parameters are adjustable. However, in many real-world applications, you cannot adjust all the parameters arbitrarily, because the parameters might have constraints. For example, in some chemical processes, water must flow only in one direction. When estimating the flow rate of water, you know that the flow rate cannot be negative. Thus, the constraint is that the flow rate must be a positive value. You must consider this constraint and any other constraints when you estimate the flow rate of water in this process. Such constraints usually follow one of the following guidelines:

- A parameter must be as close to a value as possible.
- A parameter must be between two values.
- Two or more parameters must correlate to each other.

These constraints reflect the knowledge you have of the physical system. This knowledge can result in a more realistic parameter estimation. Parameter constraints increase the possibility of the [System Identification](../lvsysid/lv_sysid_pal.html) VIs locating the optimal parameters that describe the dynamic system model. Parameter constraints also improve the accuracy of locating these optimal parameters.

You can set parameter constraints when using grey-box estimation methods, whereas you cannot set parameter constraints when using black-box estimation methods. When using these methods, you can set only the model order that specifies the number of parameters to calculate.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/pk_case_study.html language=enus -->
## TOPIC 00111: Partially Known Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/pk_case_study.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/pk_case_study.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Partially Known Model Estimation Case Study (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

This case study gives an example that uses the prior knowledge you have about a system to define and estimate [state-space](modeldefinitionsss.html) models. You use the same procedure when estimating continuous [transfer function](modeldefinitionstf.html) models. However, you apply different methods to define continuous transfer function models.

The following figure shows an RLC circuit, where *u* is the input voltage, *y* is the output voltage, *i*<sub>L</sub> is the current, and *u*<sub>C</sub> is the capacitor voltage. In this example, *y* equals the capacitor voltage *u*<sub>C</sub>.

[IMAGE alt='image' src='noloc_eps_rlc_circuit.gif']

Suppose *R* is 1.5 Ω and *L* and *C* are unknown. You can complete the following steps to identify the values of *L* and *C*.

1. Apply a wide-band voltage to u and measure the output y simultaneously. The Continuous State-Space Model of an RLC Circuit example VI uses a chirp signal from 0.5 Hz to 6 Hz as the stimulus signal. The response to the chirp signal is the response signal. This example VI then preprocesses the stimulus and response signals to remove the offset level in these signals.
2. Define a model for this circuit. Because you have information about the approximate values of L and C , you can build a partially known state-space model or a partially known transfer function model.
3. Estimate the model you defined in step 2 and then estimate L and C .

The Continuous State-Space Model of an RLC Circuit example VI guides you through defining and estimating a state-space model for the RLC circuit.

Refer to the Continuous State-Space Model of an RLC Circuit VI in the labview\examples\System Identification\Getting Started\Grey-Box Model.llb to access the VI in this case study.

Refer to the Continuous Transfer Function Model of a DC Motor with Known Gain VI in the labview\examples\System Identification\Getting Started\Grey-Box Model.llb for an example that demonstrates how to use a partially known transfer function model to estimate the RLC circuit.

You can use the following first-order differential equation to represent the relationship between the capacitor voltage and the current of this RLC circuit.

[IMAGE alt='image' src='eq_capacitor_volt_rlc.gif']

You can use the following first-order differential equation to represent the voltage relationship in this RLC circuit.

[IMAGE alt='image' src='eq_volt_rlc.gif']

By manipulating the previous two equations, you can deduce the continuous state-space model for this RLC circuit using the following two equations:

[IMAGE alt='image' src='eq_continuousss_model_rlc1.gif']

[IMAGE alt='image' src='eq_continuousss_model_rlc2.gif']

Use the [SI Create Partially Known State-Space Model](../lvsysid/create_pk_ss_model.html) VI to build the symbolic state-space model for this circuit, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_defining_partially_known_state_space_model.gif']

You specify the symbolic state-space model using formula strings, such as 1/C, -1/L, and -1.5/L, with *L* and *C* as variables. Then you define *L* and *C* with the **variables** input, as shown in the following figure. Using prior knowledge, you know that *L* is a positive value around the initial value of 0.1 H, and *C* is a value between 0 F and 0.3 F.

[IMAGE alt='image' src='model_parameters_of_rlc_circuit.gif']

Next, you can estimate the state-space model with the [SI Estimate Partially Known State-Space Model](../lvsysid/est_pk_ss_model.html) VI, as shown in the following figure.

[IMAGE alt='image' src='noloc_bd_estimate_partially_known_state_space_model.gif']

The SI Estimate Partially Known State-Space Model VI estimates each parameter of the model. You obtain the estimated model and optimized variables of the model after this VI performs an optimization. In this example, you obtain the values 0.20 H for *L* and 0.02 F for *C*, as shown in the following figure.

[IMAGE alt='image' src='optimized_variables.gif']

The Continuous State-Space Model of an RLC Circuit example VI uses the [SI Draw Model](../lvsysid/draw_model.html) VI and the values of *L* and *C* you obtain to display the estimated model in a 2D picture control, as shown in the following figure.

[IMAGE alt='image' src='estimated_model.gif']

You then can determine how accurately this model simulates the dynamic system by [validating the model](validating_models.html). Refer to the [System Identification Case Study](sysid_case_study.html) book for an example of validating a model.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/poly_vs_ss_model.html language=enus -->
## TOPIC 00112: Comparing Polynomial and State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/poly_vs_ss_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/poly_vs_ss_model.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Comparing Polynomial and State-Space Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Selecting the correct model type and model order is crucial for successfully estimating a parametric model. In general, [state-space](modeldefinitionsss.html) models provide a more complete representation of the system, especially for multiple-input multiple-output (MIMO) systems, than polynomial models because state-space models are similar to first principle models that can provide more degree of freedom in describing MIMO systems.

The identification procedure for state-space models does not involve nonlinear optimization so the estimation reaches a solution regardless of the initial guess. Moreover, the parameter settings for the state-space model are simpler. You need to select only the order, or the number of states, of the model. The order can come from prior knowledge of the system. You also can [determine the order](case_study_ssest.html) by analyzing the singular values of the information matrix. However, the states that the state-space identification procedure identifies might not reflect the physical characteristics of a system accurately. Using a similarity transformation, you can identify equivalent models with states that better represent the system. Similarity transformations enable you to transform the states without misrepresenting the input-output behavior of the system.

When model order is high, state-space models are preferable to polynomial models. Polynomial models with high order might encounter numerical problems in computation.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/preprocessing_data.html language=enus -->
## TOPIC 00113: Preprocessing Data from a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/preprocessing_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/preprocessing_data.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Preprocessing Data from a System (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After acquiring the data, you must preprocess the raw data samples. Preprocessing involves steps such as removing trends, filtering noise, and so on. You can use the [Data Preprocessing](../lvsysid/data_preprocess_pal.html) VIs to analyze the raw data and determine whether that data accurately reflects the response of the system you want to identify. To identify a system model in the frequency domain by using time-domain data, you must preprocess the time-domain data by [estimating the frequency response function (FRF)](est_frf.html). You can use the [SI Estimate FRF](../lvsysid/si_est_frf.html) VI to estimate the FRF from time-domain data.

You can use a number of preprocessing techniques to ensure that the incoming data samples are free from external noise, scaling problems, outliers, and other corruptions. These preprocessing techniques include the following methods:

- Visually inspecting data
- Removing offsets and trends
- Filtering and downsampling
- Data Scaling

|  | Note To identify a system model in the frequency domain by using time-domain data, you must preprocess the time-domain data by estimating the frequency response function (FRF). |
| --- | --- |

[Validating](validating_models.html) the quality of the data at each step in the preprocessing procedure is important in ensuring that you accurately identify a model in the later steps of the system identification process.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/pseudo-random_bin_seq.html language=enus -->
## TOPIC 00114: Pseudo-Random Binary Sequence (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/pseudo-random_bin_seq.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/pseudo-random_bin_seq.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Pseudo-Random Binary Sequence (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

A Pseudo-Random Binary Sequence, also known as Maximal Length Sequence (MLS), is a periodic, deterministic signal with properties similar to white noise. You often generate a pseudo-random binary sequence using an *n*-bit shift register with feedback through an [exclusive or](/csh?topicname=glang/exclusive_or.html) (XOR) function. While appearing random, the sequence actually repeats every 2*n*–1 values.

When using a whole period, the pseudo-random binary sequence has special mathematical advantages that make it attractive as a stimulus signal. In particular, you can attribute variations in response signals between two periods of the stimulus to noise due to the periodic nature of the signal. Also, like the white random binary noise, the pseudo-random binary sequence has a low [crest factor](choosing_stimulus_signal.html) *C*<sub>f</sub>. You can use the [SI Generate Pseudo-Random Binary Sequence](../lvsysid/generate_prbs.html) VI to generate a Pseudo-Random Binary Sequence.

The following figure shows an example of a pseudo-random binary sequence.

[IMAGE alt='image' src='pseudorandom_binary.gif']

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/recursive_ls.html language=enus -->
## TOPIC 00115: Recursive Least Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/recursive_ls.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/recursive_ls.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Recursive Least Squares (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

The recursive least squares (RLS) algorithm and [Kalman filter](kalman_filter.html) algorithm use the following equations to modify the cost function *J*(*k*) = *E*[*e*
 <sup>2</sup>(*k*)].

[IMAGE alt='image' src='eq_modified_cost.gif']

Compare this modified cost function, which uses the previous *N* error terms, to the cost function, *J*(*k*) =  *E*[*e*
 <sup>2</sup>(*k*)], which uses only the current error information *e*(*k*). The modified cost function *J*(*k*) is more robust. The corresponding convergence rate in the RLS algorithm is faster, but the implementation is more complex than that of LMS-based algorithms.

The following procedure describes how to implement the RLS algorithm.

1. Initialize the parametric vector using a small positive number ε. 
 
 [IMAGE alt='image' src='eq_least_mean_sq3.gif']
2. Initialize the data vector . 
 
 [IMAGE alt='image' src='eq_least_mean_sq5.gif']
3. Initialize the k × k matrix P (0). 
 
 [IMAGE alt='image' src='eq_matrix_p1.gif']
4. For k = 1, update the data vector based on and the current input data u ( k ) and output data y ( k ).
5. Compute the predicted response by using the following equation. 
 
 [IMAGE alt='image' src='eq_predicted_response3.gif']
6. Compute the error e ( k ) by solving the following equation. 
 
 [IMAGE alt='image' src='eq_system_error.gif']
7. Update the gain vector defined by the following equation. 
 
 [IMAGE alt='image' src='eq_gain_vector1.gif'] 
 
 The properties of a system might vary with time, so you must ensure that the algorithm tracks the variations. You can use the forgetting factor λ, which is an adjustable parameter, to track these variations. The smaller the forgetting factor λ, the less previous information this algorithm uses. When you use small forgetting factors, the adaptive filter is able to track time-varying systems that vary rapidly. The range of the forgetting factor λ is between zero and one, typically 0.98 < λ < 1.
 
 
 P ( k ) is a k × k matrix whose initial value is defined by P (0) in step 3.
8. Update the parametric vector . 
 
 [IMAGE alt='image' src='eq_parametric_vector2.gif']
9. Update the P ( k ) matrix. 
 
 [IMAGE alt='image' src='eq_matrix_p2.gif']
10. Stop if the error is small enough, else set k = k + 1 and repeat steps 4–10.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/removing_offsets_trends.html language=enus -->
## TOPIC 00116: Removing Offsets and Trends (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/removing_offsets_trends.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/removing_offsets_trends.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Removing Offsets and Trends (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

You can remove [offsets](#removing_offsets) and [trends](#removing_trends) from raw data sets by using the [SI Remove Trend](../lvsysid/remove_trend.html) VI. You can specify whether to remove offsets or trends by using the **trend type** input of this VI.

Refer to the Remove Trend VI in the labview\examples\System Identification\Getting Started\General.llb for an example that demonstrates how to remove the offset or trend from a signal.

#### Removing Offsets

An estimated system model is a linearized version of the dynamic system around the operating point. You must subtract the operating points from the raw data samples because linearization is done with respect to the signal values relative to the operating point, which is the offset level of the signal.

The following figure shows an example of removing the offset level of a signal. The goal of the water tank is to keep the water level at six meters. The **Water level record** graph shows that the water level changes in the vicinity of the operating point of six meters. If you use the water level record for system identification, you must remove the six meter operating point value.

[IMAGE alt='image' src='watertank.gif']

The SI Remove Trend VI enables you to remove the offset from the raw data set. You must set the **trend type**to **mean** to use this preprocessing technique.

#### Removing Trends

External influences might add some low frequency or periodic components to the data. These additional components are not relevant to the specific modeling problem. Examples of external influences include variations due to the 24-hour day cycle in power plants, seasonal influences in biological and economical systems, thermal expansion in rolling mills, 50 or 60 Hz interference in power lines, and so on. The amplitude of these trends can be large and can corrupt the results of signal analysis and [parametric](parametric_est.html) identification algorithms.

The SI Remove Trend VI provides a way for you to remove these external influences, or trends, from the raw data set. You must set the **trend type**to **linear** to use this preprocessing technique.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/selecting_ir_length.html language=enus -->
## TOPIC 00117: Selecting an Impulse Response Length (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/selecting_ir_length.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/selecting_ir_length.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Selecting an Impulse Response Length (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Theoretically, the length of the impulse response might be infinite. For some systems, the impulse response quickly reaches zero, and the number of nonzero points is finite. For other systems, the impulse response never reaches zero. Realistically, you can obtain only the first *N* points of the impulse response due to limited signal length and limited memory size. Therefore, the [SI Estimate Impulse Response](../lvsysid/estimate_impulse_response.html) VI has inputs to specify how many points of the impulse response to observe. With the [least squares](ir_least_squares.html) method, you must ensure the sum of **num of points (t<0)** and **num of points (t>=0)** is no larger than the signal length. With the [correlation analysis](ir_correlation_analysis.html) method, you can set **num of points** to be as large as the signal length.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/si_frequency_response.html language=enus -->
## TOPIC 00118: Frequency Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/si_frequency_response.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/si_frequency_response.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Frequency Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Theoretically, the results from [impulse response](si_impulse_response.html) estimation and the results from frequency response estimation are equivalent. For example, the Fourier transform of the impulse response *h*(*n*), which you can compute using impulse response estimation, equals the frequency response *G*(*e*<sup>*jω*</sup>). However, this equivalence does not hold in most real-world applications because of different preprocessing schemes in impulse response estimation and frequency response estimation.

The frequency response provides the complete frequency-domain characteristics of the system, including the passband and the natural frequency of the system. A sinusoidal input signal has the following general form:

*u*(*t*) = sin(*ω*<sub>0</sub>*t*)

The response of a linear time-invariant system to a sinusoidal input also is a sinusoidal signal. However, the response to the sinusoidal input might have a different magnitude and phase than the sinusoidal signal, as shown in the following equation.

*y*(*t*) = *b*sin(*ω*<sub>0</sub>*t* + *θ*)

where *b* and *θ* are the magnitude and phase, respectively, of the frequency response of the system to an input sinusoidal frequency *ω*<sub>0</sub>. If you apply input signals with a number of sinusoids at different frequencies, you can obtain an estimate of the frequency response *G*(*ω*) of the system at those frequencies. The frequency response is a complex-valued sequence. The magnitude of *G*(*ω*) is the magnitude response of the system and the phase of *G*(*ω*) is the phase response of the system. This method of obtaining the frequency response is straightforward but takes a long time to complete and is sensitive to noise. For these reasons, the [SI Estimate Frequency Response](../lvsysid/estimate_freq_response.html) VI uses the [spectral analysis method](fr_spectral_analysis.html) to estimate the frequency response function (FRF).

|  | Note You can use the SI Estimate FRF VI to estimate the FRF if you have only time-domain data available. |
| --- | --- |

#### Applications of the Frequency Response

The frequency response gives the characteristics of the system in the [frequency domain](/csh?topicname=lvanlsconcepts/freq_time_domain_diffs.html). You can use the frequency response to obtain useful information before applying [parametric estimation](parametric_est.html). For example, you can use the frequency response to determine whether you must pre-filter the signals or what the model order of the system is. You also can use nonparametric frequency response to verify parametric model estimation results by comparing the frequency response of the parametric model with the nonparametric frequency response.

One example of a real-world application of the frequency response is with the flexible arm, as shown in the following figure. The input of this system is the reaction torque of the structure on the ground. This input is a multi-sine wave with 200 frequency points equally spaced over the frequency band from 0.122 Hz to 24.4 Hz. The output of this system is the acceleration of the flexible arm. The frequency response of this system is not significant outside of the range of interest, which is the frequency band of the input signal, or 0.122 Hz to 24.4 Hz. However, notice that the **magnitude response** has a peak around 42 Hz. The peak around 42 Hz may be the result of noise, or nonlinearity, or another input source. You can use lowpass filtering to remove the 42 Hz peak before applying parametric estimation.

[IMAGE alt='image' src='est_freq_resp_fp.gif']

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/si_impulse_response.html language=enus -->
## TOPIC 00119: Impulse Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/si_impulse_response.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/si_impulse_response.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Impulse Response (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

An impulse input to a dynamic system is defined differently depending on whether the system is discrete or continuous. For a continuous dynamic system, an impulse input, also known as the Dirac delta function, is a unit-area signal with an infinite amplitude and infinitely small duration occurring at a specified time. At all other times, the input signal value is zero. For a discrete system, an impulse is a physical pulse that has unit amplitude at the first sample period and zero amplitude for all other times.

The following figure shows an impulse input.

[IMAGE alt='image' src='noloc_eps_unit_impulse.gif']

| where | t is time |
| --- | --- |
|  | u(t) is the input signal |

Because the impulse signal excites all frequencies and the duration of this signal is infinitely small, you can see the natural response of the system.

The following figure shows that the impulse response of a linear time-invariant system is equal to the output *y*(*k*) of the system when you apply an impulse signal to the input *u*(*k*) of the system. The impulse response provides the complete characteristic information of a system.

[IMAGE alt='image' src='noloc_eps_impulse_response_definition.gif']

If you know the impulse response *h*(*n*) and the input signal *u*(*k*) of a system, then you can compute the output *y*(*k*) of the system by using the following equation.

[IMAGE alt='image' src='eq_ir_output.gif']

where*e*(*k*) is the disturbance of the system.

According to impulse response theory, when you apply a Dirac delta function to a system, the output of the system is the impulse response. You can think of the Dirac delta function *δ*(*x*) as a function that has the value of infinity for *x* = 0, the value zero elsewhere, and a total integral of one. However, generating an ideal Dirac delta function is unrealistic.

If you apply an approximate impulse with a small duration to the input of a system, the output of the system is the approximation of the impulse response of the system. The smaller the duration of the impulse, the closer the output of the system is to the true impulse response. However, an impulse carries little energy and might not excite the system, and noise might corrupt the output of the system. An impulse with a large amplitude and duration can improve the signal-to-noise ratio of the output signal. However, a large amplitude impulse can damage the hardware of the system, and a long-duration impulse leads to inaccuracy. For these reasons, you can use the [least squares](ir_least_squares.html) and [correlation analysis](ir_correlation_analysis.html) methods to estimate the impulse response.

#### Applications of the Impulse Response

The impulse response not only indicates the stability and causality of the system if [feedback](closed-loop_est.html#feedback_in_systems) exists in the system, but also provides information on properties such as the damping, dominating time constant, and time delay. Some of this information, such as the time delay, is useful for [parametric model estimation](parametric_est.html). Therefore, you can use nonparametric impulse response estimation before parametric model estimation to help estimate the parameters. You can use the [SI Estimate Impulse Response](../lvsysid/estimate_impulse_response.html) VI to estimate the impulse response and determine the time delay of a system by using the correlation analysis method.

The following figure shows the block diagram of a VI that simulates a system defined by the following equation.

*y*(*k*) = 0.2*u*(*k* – 2) + 0.8*u*(*k* – 3) + 0.3*u*(*k* – 4)

[IMAGE alt='image' src='timedelay_bd.gif']

In the previous figure, the two initial values of the **estimated impulse response** are smaller than the **confidence level**. You can have 99.0% confidence that values less than the **confidence level** are insignificant, and you can consider those values to be equal to 0. Therefore, you can conclude that the time delay of the system is 2 because the beginning of the first two values of the impulse response are zero.

Another common application of the impulse response is to detect feedback in systems by using the least squares method. If feedback exists in a system, the impulse response of the system becomes significantly large at negative lags and the correlation between the input signal and disturbance *e*(*k*) is nonzero. The correlation analysis method assumes the input signal and the disturbance *e*(*k*) are independent from each other. Thus, this method cannot estimate accurately the impulse response of the system that contains feedback. Only the least squares method can provide reliable results. You can use the [SI Detect Feedback](../lvsysid/detect_feedback.html) VI to estimate the impulse response of a system and determine whether feedback exists in the system.

Refer to the Feedback Detection VI in the labview\examples\System Identification\Getting Started\General.llb for an example that demonstrates how to use the SI Detect Feedback VI to detect feedback in a system.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/si_step_response.html language=enus -->
## TOPIC 00120: Step Signals and Step Responses (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/si_step_response.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/si_step_response.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Step Signals and Step Responses (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

A step signal is a signal that switches from an initial value *a* to another value *b* in a very short time. You can generate this signal by creating an array that begins with a series of *a* and then shifts to a series of *b*. For example, if you use zero as *a* and one as *b*, you can create an array that begins with a series of zeros and then shifts to a series of ones, such as "0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1". Use the [Build Waveform (Analog Waveform)](/csh?topicname=lvwave/build_waveform.html) function to convert this array to a waveform signal.

Use step signals as stimulus signals to estimate dynamic systems from step responses. The following figure shows an example of a step stimulus signal and the corresponding step response.

[IMAGE alt='image' src='noloc_eps_si_step_signal.gif']

A step stimulus signal and the corresponding step response contain the following phases:

- Initial Condition —A time period when both the step stimulus signal and the step response equal zero.
- t **0** —The time point when the step stimulus signal starts to change.
- Delay —A time period when the step stimulus signal equals one and the step response equals zero.
- Steady State —A time period when the step stimulus signal equals one and the gradient of the step response equals zero.

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/sigs_acq_data.html language=enus -->
## TOPIC 00121: Part 2: Exciting the System and Acquiring Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/sigs_acq_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/sigs_acq_data.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Part 2: Exciting the System and Acquiring Data (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

After you [choose a proper dynamic system model](sigs_phys_model.html), you must acquire the input and output data from the direct current (DC) servomotor. You then [preprocess](preprocessing_data.html) and use the data to estimate unknown coefficients of the dynamic system model. You can use an encoder or a DC tachometer to measure the shaft speed of the DC servomotor.

Set up the following experimental circuit to excite the DC servomotor and acquire response signals with an encoder.

[IMAGE alt='image' src='noloc_eps_sigs_motor_exp_encoder.gif']

Set up the following experimental circuit to excite the DC servomotor and acquire response signals with a DC tachometer.

[IMAGE alt='image' src='noloc_eps_sigs_motor_exp_tacho.gif']

Both circuits use an NI data acquisition (DAQ) card to generate digital stimulus signals. You also can use a reconfigurable I/O (RIO), CompactRIO, or Single-Board RIO device to generate the stimulus signals and acquire data. In these two circuits, a D/A output channel of the NI-DAQ card converts the stimulus signals to analog voltage signals and sends these signals to an amplifier. An A/D input on the NI-DAQ card acquires the original analog signals, converts the signals to digital signals, and records these digital signals for identification. The amplifier sends the enhanced analog signals to drive the DC servomotor. If you use an encoder to measure the shaft speed of the DC servomotor, the encoder generates pulses when the DC servomotor rotates. The encoder sends the pulses to a digital input channel of the NI-DAQ card. A counter in the NI-DAQ card counts the number of pulses and computes the rotational speed of the DC servomotor. If you use a DC tachometer to measure the shaft speed of the DC servomotor, the DC tachometer generates back-EMF voltage signals when the DC servomotor rotates. The DC tachometer sends the voltage signals to another A/D channel of the NI-DAQ card. The NI-DAQ card calculates the rotational speed by using the voltage signals.

|  | Note Ensure the NI-DAQ card acquires stimulus voltage signals and rotational speed synchronously. Ensure you acquire and save synchronous stimulus signals and response signals with constant time steps. |
| --- | --- |

You can use the following [types of stimulus signals](choosing_stimulus_signal.html):

- Step signals —Use step stimulus signals for the low frequency band of a linear dynamic system. This type of signal is easy to generate but has a low signal-to-noise ratio (SNR) in the high frequency bands. To generate a step signal, create an array that begins with a series of zeros and then shifts to a series of ones, such as "0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1". An element in this array represents a sampling point. Ensure the array contains enough elements according to the sampling rate of the device you use. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.
- Swept sine signals —Use swept sine stimulus signals for the full frequency bands of a linear dynamic system. This type of stimulus signal has a high SNR in the full frequency bands of a linear dynamic system. However, if the response signals contain non-linear distortion, this type of stimulus signal cannot eliminate the distortion and leads to an inaccurate dynamic system model. Use the Chirp Pattern VI to generate an array containing a swept sine pattern. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.
- Random signals —Use random stimulus signals for the full frequency band of dynamic systems. This type of stimulus signal has a high SNR in the full frequency band. You must repeat exciting the dynamic system and acquiring data for multiple times to cover the full range of the dynamic system and eliminate any non-linear distortion in the response signals. Use the Periodic Random Noise VI to generate an array of periodic random noise. You then use the Build Waveform (Analog Waveform) function to convert this array to a waveform signal.

In this example, you can use any of these three types of stimulus signals to excite the DC servomotor.

Refer to the following VIs for examples of generating stimulus signals and acquiring data from a dynamic system. You must have the required hardware, such as an NI-DAQ card, to use these examples.

- Stimulus Signal Generation (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples
- Stimulus and Response Data (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples
- Stimulus and Response Data with Encoder (DAQmx) VI: labview\examples\System Identification\Getting Started\General.llb 
 Open example 
 Find related examples

Alternately, if you do not have the required hardware or a DC servomotor, use the [SI Data Samples](../lvsysid/si_data_samples.html) VI to generate the input and output data. This tutorial uses the SI Data Samples VI to complete the following parts. If you also use this VI to complete the following parts, you can get identical results as the results in this tutorial.

Complete the following steps to generate the input and output data by using the SI Data Samples VI.

1. Create a blank VI in LabVIEW.
2. Add the SI Data Samples VI to the block diagram of the VI you created. This VI generates single-input single-output waveform signals by default.
 [IMAGE alt='image' src='add.gif'] Add
3. Right-click the data input of this VI and select Create»Constant from the shortcut menu to create a constant for this input.
4. Ensure the value of this constant is Motor .

You can save this VI and use this VI to complete the following parts of this tutorial.

| Previous: Choosing a Proper System Model by Using Physical Modeling | Next: Identifying Dynamic System Models |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/sigs_mod_convert.html language=enus -->
## TOPIC 00122: Part 5: Converting Dynamic System Models to Control Design Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/sigs_mod_convert.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/sigs_mod_convert.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Part 5: Converting Dynamic System Models to Control Design Models (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

If you want to design controllers for a dynamic system, you must convert the dynamic system model you [identified](sigs_model_id.html) to a system model that you can use in the LabVIEW Control Design and Simulation Module. For example, you can use the Control Design and Simulation Module to design controllers for this DC servomotor to control the behaviors of this DC servomotor.

You also can use the Control Design and Simulation Module to complete the following tasks:

- Construct plants and control models
- Analyze dynamic system performance
- Simulate dynamic systems with a wide option of solvers
- Deploy dynamic systems to real-time hardware

Complete the following steps to convert a dynamic system model to a control design model.

1. Add the SI Convert to Models of CDT VI to the block diagram of the VI you created .
 [IMAGE alt='image' src='add.gif'] Add
2. Select a proper instance of this polymorphic VI.
  - MIMO TF —Select this instance to convert a transfer function dynamic system model.
  - MIMO SS —Select this instance to convert a state-space dynamic system model.
3. Create a constant for the realization type input of the SI Convert to Models of CDT VI.
4. Set the realization type constant to full .
5. Wire the system model out output of the following VIs or Express VIs to the system model input of the SI Convert to Models of CDT VI.
  - SI Estimate State-Space Model VI
  - SI Estimate Transfer Function Model VI
  - SI Model Estimation Express VI
  - SI Transfer Function Estimation Express VI
6. Create an indicator for the transfer function model or state-space model output of the SI Convert to Models of CDT VI. The following figure shows the block diagram. 
 [IMAGE alt='image' src='noloc_eps_sigs_cdt_model_conv.gif']
7. Wire all error in and error out terminals on the block diagram.
8. Run this VI to convert the dynamic system model.
9. Save the resulting model.

The following figure shows the resulting dynamic system model.

[IMAGE alt='image' src='sigs_cdt_model_result.gif']

|  | Note If you have the Control Design and Simulation Module installed, you can wire the resulting model to the Control Design VIs and Functions or the Simulation VIs and Functions. |
| --- | --- |

| Previous: Validating and Analyzing Dynamic System Models |  |
| --- | --- |

<!--NI_TOPIC bundle=labview-control-design-and-simulation-module path=lvsysidconcepts/sigs_phys_model.html language=enus -->
## TOPIC 00123: Part 1: Choosing a Proper Dynamic System Model by Using Physical Modeling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

- bundle_id: `labview-control-design-and-simulation-module`
- source_path: `lvsysidconcepts/sigs_phys_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-control-design-and-simulation-module/raw/resource/enus/lvsysidconcepts/sigs_phys_model.html
- document_id: `labview-control-design-and-simulation-module`
- page_type: `leaf`
- content_type: ``

### Part 1: Choosing a Proper Dynamic System Model by Using Physical Modeling (Advanced Signal Processing Toolkit or Control Design and Simulation Module)

Before you estimate a dynamic system, create a mathematical model that contains unknown coefficients. You then use system identification to estimate these coefficients.

Physical modeling is a common method for sketching a mathematical model that represents a real dynamic system. Physical modeling determines the nature of the model, such as the model order and the number of I/O channels. Use physical modeling to define proper models for dynamic systems.

The following figure shows an electrical circuit model of a brushed direct current (DC) servomotor.

[IMAGE alt='image' src='noloc_eps_sigs_dcmotor_graph.gif']

| where | V is the source voltage of the DC power supply. |
| --- | --- |
|  | R is the resistance of the DC servomotor armature circuit. |
|  | L is the inductance of the DC servomotor armature circuit. |
|  | i is the circuit armature current. |
|  | ω is the shaft speed of the DC servomotor. |
|  | T is the torque of the DC servomotor. |

In this dynamic system, the source voltage, *V*, is the input and the DC servomotor shaft speed, *ω*, is the output.

According to Faraday's Law of electromagnetic induction, the circuit armature current *i*, motor torque *T*, motor shaft velocity *ω*, and motor back-EMF voltage *e*, have the following relationship:

[IMAGE alt='image' src='eq_sigs_motor_te.gif']

| where | Kt is an electromotive force constant. |
| --- | --- |
|  | Ke is a motor back-EMF constant. |

You can obtain the following equations by using Newton's Law and Kirchhoff's Law.

[IMAGE alt='image' src='eq_sigs_n_k_model.gif']

| where | J is the moment of inertia of the rotor. |
| --- | --- |
|  | b is the damping ratio of the mechanical part of the DC servomotor. |

Perform further transforms on these equations to obtain a mathematic model of the dynamic system. You can choose one of the four common dynamic system models on the basis of your needs.

- Use the continuous-time transfer function model to create a model that you can use with an analog proportional-integral-derivative (PID) controller.
- Use the continuous-time state-space model to create a model that you can use with an analog state feedback controller.
- Use the discrete-time transfer function model to create a model that you can use with a digital PID controller.
- Use the discrete-time state-space model to create a model that you can use with a digital state feedback controller.

|  | Note If you perform system identification with an improper or incorrect physical model, the resulting dynamic system model may not correctly describe the behaviors of the dynamic system. |
| --- | --- |

|  | Next: Exciting the System and Acquiring Data |
| --- | --- |
