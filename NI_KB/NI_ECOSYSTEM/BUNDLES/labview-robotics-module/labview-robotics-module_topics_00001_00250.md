# NI DOCUMENT BUNDLE: labview-robotics-module

<!--NI_BUNDLE_CHUNK bundle=labview-robotics-module start=1 end=250 -->
<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_comm_overview.html language=enus -->
## TOPIC 00001: Communicating between Processes in a Robotics Application (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_comm_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_comm_overview.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Communicating between Processes in a Robotics Application (Robotics Module)

Robotics applications often consist of processes on different targets that must work together. Therefore, communication architecture is an important component of robotics applications. The following figure shows an example of a robotics application with many processes that must transfer data locally and over a network.

[IMAGE alt='image' src='loc_eps_comm_overview.gif']

LabVIEW offers many different features for communicating between processes in applications similar to the previous one. Use the following flowchart to determine an appropriate communication feature for your robotics application. Click a bubble to learn more about the communication concept or feature it describes.

[IMAGE alt='image' src='loc_eps_comm_flowchart.gif']

#### Lossless Communication

Lossless communication describes network transmission that guarantees the delivery of every data point.

#### Fixed Protocol

A fixed protocol is a predefined message format that you cannot change. For example, a fixed protocol might require a three-byte header at the beginning of each data point or a two-byte checksum at the end of each data point.

#### Buffering

Buffering is the transmission of data to a memory space, or buffer, which stores that data until the recipient reads it. If a buffer becomes full, newer values sometimes overwrite older values in the buffer. Buffering prevents data loss when a process writes data faster than other processes can read it. However, if your processes need only the latest values in a data set rather than most or all of the values, buffering is not always useful. Refer to the [National Instruments Web site](javascript: WWW(WWW_PRODUCERCONSUMER)) at ni.com for more information about buffering.

#### Broadcasting

Broadcasting is a model of communication in which processes send data to a network port so that any computers listening on that port can receive that data. Multicasting is a related model in which a process sends data to a group of computers on a network. Unicasting is another related model in which a process sends messages to a single network destination identified by a unique address.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_comm_queues.html language=enus -->
## TOPIC 00002: Transferring Data on a Single Target (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_comm_queues.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_comm_queues.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Transferring Data on a Single Target (Robotics Module)

Use the [Queue Operations](/csh?topicname=glang/queue_vis.html) functions to [communicate between processes in a robotics application](../lvrobogsm/robo_comm_overview.html) when transferring data on a single target. Processes that communicate using Queue Operations functions can run in parallel while also running at different rates.

|  | Note Use the RT FIFO functions instead of queues to transfer data on a single target in RT and FPGA applications that must maintain determinism. Use user events instead of queues to broadcast data to multiple processes on a single target. |
| --- | --- |

The following figure shows an example of a robotics application that uses queues.

[IMAGE alt='image' src='loc_eps_comm_queueexample.gif']

The following events occur in the previous figure.

|  | The obstacle detection process acquires data at a rate of 200 times per second and stores those data points in a queue. |
| --- | --- |
|  | Because the path planning process is computationally intensive, it runs approximately two times per second and waits until the queue obtains 100 data points. |
|  | When the queue contains 100 data points, the path planning process calculates a path for the robot. Note Because these processes run in parallel, they do not block each other. The obstacle detection process can continue to add data points to the queue even as the path planning process calculates a path. |
|  | Note Because these processes run in parallel, they do not block each other. The obstacle detection process can continue to add data points to the queue even as the path planning process calculates a path. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_controls_props.html language=enus -->
## TOPIC 00003: Customizing Robotics Indicators (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_controls_props.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_controls_props.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Customizing Robotics Indicators (Robotics Module)

You can customize the appearance and some behaviors of the [compass, attitude, and rangefinder indicators](robo_controls_concepts.html).

#### Changing Units from Degrees to Radians

To change the units in which a compass, attitude, or rangefinder indicator expresses angles, right-click the indicator and select **Angles in Radians** or **Angles in Degrees** from the shortcut menu.

#### Changing the Appearance of Indicators

To change the visual appearance of a compass, attitude, or rangefinder indicator, right-click the indicator and select **Compass Properties**, **Attitude Properties**, or **Rangefinder Properties**, respectively, from the shortcut menu. In the **Indicator** properties dialog box that displays, use the configuration options to choose which components display on the indicator and the colors of the components.

|  | Tip The right side of the properties dialog box displays a preview of the current configuration so you can see how changes look before you apply them to the indicator. |
| --- | --- |

You can [customize additional properties of rangefinder indicators](../lvrobogsm/robo_controls_rangef_props.html).

For compass and attitude indicators, you also can [create properties to programmatically read and write](/csh?topicname=lvhowto/creating_property_nodes.html) many of the options available in the properties dialog boxes.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_controls_rangef_props.html language=enus -->
## TOPIC 00004: Customizing Rangefinder Indicators (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_controls_rangef_props.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_controls_rangef_props.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Customizing Rangefinder Indicators (Robotics Module)

You can [customize some properties](robo_controls_props.html) that compass, attitude, and rangefinder indicators have in common. You also can modify additional properties of [rangefinder indicators](robo_controls_concepts.html#2drange), as described in the following sections.

#### Changing the Plot Range and Scale

To change the range of distances for which a rangefinder indicator displays data, right-click the indicator and select **Rangefinder Properties** from the shortcut menu to display the **Rangefinder Indicator** dialog box.

- To set a static maximum distance, remove the checkmark from the AutoScale checkbox, if necessary, and enter the value in the Fit to Radius control. You can use any unit of measurement to specify distance values. However, always use consistent units when you specify these values.
- To configure the indicator to automatically include the largest distance at which an obstacle exists, place a checkmark in the AutoScale checkbox. When the AutoScale checkbox contains a checkmark, LabVIEW disables the Fit to Radius control and ignores its value.

|  | Tip The right side of the Rangefinder Indicator dialog box displays a preview of the current configuration so you can see how changes look before you apply them to the indicator. |
| --- | --- |

#### Customizing the Appearance of Obstacles Detected at the Same Angle

The rangefinder indicator can display obstacles that exist at the same angle but at different distances. You might want to customize the appearance of obstacles that appear at different distances within the sensor field of view so you can differentiate between them. The following front panel shows a simple example of customizing the appearance of two rows of obstacles.

[IMAGE alt='image' src='loc_fp_rangefinder2.gif']

Complete the following steps to customize the appearances of rows of obstacles:

1. Right-click the indicator and select Rangefinder Properties from the shortcut menu to display the Rangefinder Indicator dialog box.
2. At the bottom of the dialog box, set the number of the obstacle row you want to customize in the Data Row control. The 0 Data Row includes the first obstacle at each angle, the 1 Data Row includes the second obstacle at each angle, and so on.
3. Use the other controls in this section of the dialog box to customize the appearance of obstacles in each row.

#### Drawing Lines That Connect Obstacles

By default, the rangefinder indicator displays obstacles as single points. You can configure a rangefinder indicator to draw lines that connect obstacles in the same row, as shown in the front panel in the previous section.

Complete the following steps to configure the indicator to draw lines between obstacles in the same row:

1. Right-click the indicator and select Rangefinder Properties from the shortcut menu to display the Rangefinder Indicator dialog box.
2. At the bottom of the dialog box, set the number of the obstacle row you want to customize in the Data Row control. The 0 Data Row includes the first obstacle at each angle, the 1 Data Row includes the second obstacle at each angle, and so on.
3. Place a checkmark in the Draw Lines checkbox.
4. (Optional) In the Max Line Distance control, enter the distance between obstacles at which you want to stop drawing connecting lines. LabVIEW draws lines between any points closer than the Max Line Distance . Inf means LabVIEW draws lines between all obstacles in the same row, no matter the distance.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_deploying_vis.html language=enus -->
## TOPIC 00005: Deploying, Downloading, and Running VIs and Applications (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_deploying_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_deploying_vis.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Deploying, Downloading, and Running VIs and Applications (Robotics Module)

Before you run VIs on an RT or FPGA target, you must deploy RT VIs and any dependencies to the RT target and download files on the FPGA target.

This topic includes links to topics you might find useful at each of these levels.

- Building and Distributing Applications
- Deploying and Running VIs on an RT Target
- Building and Deploying a Stand-Alone Real-Time Application
- Compiling, Downloading, and Running FPGA VIs
- Configuring FPGA VIs to Run Automatically
- Downloading an FPGA VI to the Flash Memory of an FPGA Target

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_design_robot.html language=enus -->
## TOPIC 00006: Designing a Simulated Robot (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_design_robot.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_design_robot.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Designing a Simulated Robot (Robotics Module)

Designing and configuring a robot model allows you to [simulate robots](../lvrobogsm/robo_sim_overview.html) in a [simulation scene](../lvrobogsm/robo_sim_creating.html) without depending on the physical robot. A robot model is a software representation of a robot for use in a simulated environment. A robot model consists of component models and joints, which connect the component models. Component models include wheels, tracks, arms, conveyors, and simple objects that you can use to assemble a robot model. When you design a robot model, you can add component models and sensors as robot parts, add joints to connect the robot parts, add motors to control the movement of joints, and configure the posture and properties of the robot parts.

Use the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html) to design a robot model. You can design robots by using the predefined models or using the robot parts that you created. You also can import a computer-aided design (CAD) robot model in the builder. A CAD robot model is a 3D description file for visualization of a robot, which typically includes the geometry, texture, and material information of the robot. Compared with a typical CAD model which is for visualization only, a robot model that you design in LabVIEW includes both the visual and physical models that describe the simulated robot. The visual model describes the visual appearance of the simulated robot and does not affect the behavior of the robot in the simulation scene. The physical model contains the kinematics and dynamics information of the physical robot and its components in the simulation scene.

The following steps describes the process you use to design a robot model in LabVIEW.

1. Create robot parts for a simulated robot using one of the following methods.
  1. Import a CAD model and add physical models to the CAD model .
  2. Add predefined models to the robot model.
2. Specify the position and orientation of robot parts to assemble a robot model.
3. Connect robot parts with different types of joints.
4. Add motors to control the movement of the joints.
5. Save or export the robot model that you design.

You can [view and adjust the posture of the models](../lvrobogsm/robo_position_models.html) in the 3D environment.

Use the robot model that you design to simulate the behavior of real robots in a simulated environment that you set up with the [Robotics Environment Simulation Wizard](../lvrobodialog/robo_sim_wizard.html).

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_docinfo.html language=enus -->
## TOPIC 00007: Robotics Module

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_docinfo.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_docinfo.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Robotics Module

June 2014, 372983F-01

The LabVIEW Robotics Module is a software package that allows you to develop and deploy a robotics application using LabVIEW, other National Instruments software, and device drivers.

The Robotics Module provides the following components:

- VIs and device drivers —Robotics Module VIs provide algorithms for navigation, steering, and so on. The Robotics Module also provides sensor and actuator drivers that allow you to control certain devices commonly used in robotics systems. To access the Robotics VIs and most device drivers, select View»Functions Palette from the block diagram in LabVIEW and navigate to the Robotics palette.
 [IMAGE alt='image' src='note.gif']
**Note** The Robotics Module also includes drivers that provide connectivity to sensors on FPGA targets. To browse or search for these drivers, use the NI Example Finder, available by selecting **Help»Find Examples** in LabVIEW. The **Robotics»Sensor Drivers** category contains these drivers.
- Setup wizards —The Robotics Module provides the following wizards:
  - Hardware Setup Wizard —This wizard configures the basic settings of NI RIO hardware targets and installs software on the targets. Select View»Getting Started Window , click the Welcome link on the Getting Started window, and click the Hardware Setup Wizard link to launch this wizard.
  - Robotics Project Wizard —This wizard allows you to create a new LabVIEW project configured with your hardware or a simulation project. Select File»New from the Getting Started window to open the New dialog box. Expand the Project»Project from Wizard node and select Robotics Project . Then, click the OK button to launch the Robotics Project Wizard .
- Simulator —A built-in robotics simulator renders 3D simulation scenes and models the motion of real robots in a real-world environment.
- Examples —Examples VIs demonstrate robotics concepts, such as path planning, kinematics, and acquiring data from sensors. You can modify an example VI to fit an application, or you can copy and paste from one or more example VIs into a VI that you create. Use the NI Example Finder, available by selecting Help»Find Examples from LabVIEW, to browse or search for example VIs.
 [IMAGE alt='image' src='note.gif']
**Note** Some robotics examples require additional software. In the NI Example Finder, select an example and refer to the **Information** section for a list of software you must install to run the example. 
 You also can access robotics-specific example VIs from the labview\examples\robotics directory. Access examples for certain sensor and actuator drivers in the labview\instr.lib\*device* directory, where device is the name of a device for which you have drivers installed.
- Templates —Templates demonstrate useful design patterns and serve as starting points for your applications. You can customize the templates according to the needs of your application. Select File»Create Project to display the Create Project dialog box, which lists templates. The Robotics Module provides the robotics application architectures template.

[Use the LabVIEW Robotics environment](../lvrobogsm/robo_environment.html) to easily access these features.

#### Code Downloads on ni.com

Use the following links to find resources and download code that might be helpful as you use the Robotics Module.

- FPGA IPNet—Find FPGA IP and examples gathered from internal National Instruments developers and the LabVIEW FPGA community.
- Instrument Driver Network (IDNet)—Find, download, and customize a driver to communicate with third-party instruments.

#### Case Studies

See how others use the NI development platform in applications for autonomous vehicles, research and teaching, and robotic arms at ni.com/robotics.

© 2009–2014 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_environment.html language=enus -->
## TOPIC 00008: Accessing the LabVIEW Robotics Environment (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_environment.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_environment.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Accessing the LabVIEW Robotics Environment (Robotics Module)

The Robotics Module provides a different environment than the LabVIEW Development System to allow you to easily access robotics-specific features and focus on developing robotics applications. To access the LabVIEW Robotics environment, select **Start»All Programs»National Instruments»LabVIEW Robotics»LabVIEW Robotics *x***, where *x* is the version of the Robotics Module. (Windows 8) Click **NI Launcher** and select **LabVIEW Robotics** in the window that appears.

If LabVIEW is already open, select **Tools»Choose Environment** to display the [Choose Environment Settings](/csh?topicname=lvdialog/chooseenvironment_dialog.html) dialog box, which you can use to change environments.

In the LabVIEW Robotics environment, you can access Robotics specific tutorials and the Hardware Setup Wizard by clicking the **Welcome** link on the Robotics [Getting Started](../lvrobodialog/robo_gsw.html) window.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_error_codes.html language=enus -->
## TOPIC 00009: Error Codes (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_error_codes.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Error Codes (Robotics Module)

The [Robotics](../lvrobovi/robotics_pal.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| –310272 | You cannot run the robotics simulator on a real-time target. Remove any code that initializes a simulated KUKA youBot before you deploy this VI to the RT target. |
| –310271 | The EtherCAT module command failed. |
| –310253 | You cannot run the robotics simulator on a real-time target. Remove any code that initializes a simulated Starter Kit robot before you deploy this VI to the RT target. |
| –310252 | The robot sensor or actuator is invalid. Make sure you use the appropriate initialization VI from the Starter Kit palette to begin communicating with the robot. |
| –310251 | The interface with the Starter Kit FPGA is invalid. Make sure you use the appropriate initialization VI from the Starter Kit palette to begin communicating with the robot. |
| –310232 | The manifest file was modified by an application. Open the Simulator Assistant, verify the settings in the configuration dialog box, and click OK to regenerate the Simulator Assistant. |
| –310231 | You can have only one Simulator Assistant running at the same time on the same machine. You must remove additional instances of the Simulator Assistant. |
| –310230 | The manifest file does not exist at the path you specified. You must reconfigure and specify a valid path to a manifest file in the Simulator Assistant. |
| –310227 | This VI only supports hinge, slider, or fixed joints in the serial arm. |
| –310226 | The arm you specified is not a serial robotic arm. |
| –310225 | The link ID you specified does not correspond to any links in the robot. Make sure the robot ID, base ID, and end effector ID are correct and match with the serial arm properties. |
| –310216 | Unable to delete the resource folder of the robot model. The resource folder may contain files that do not belong to the robot model or you may not have permission to modify the resource folder. |
| –310215 | Unable to delete the robot model files. Make sure you have the permission to modify the manifest file. |
| –310214 | Unable to create a temporary folder. Make sure you have permission to modify the temporary directory. You can change the location of LabVIEW temporary directory by selecting Tools»Options in LabVIEW and change the directory on the Paths page. |
| –310212 | You do not have permission to modify this folder. |
| –310211 | Unable to load the robot model because the manifest file is not a National Instruments robot simulation model file or the manifest file is broken. |
| –310208 | The Robotics Environment Simulator Wizard or Robot Simulation Model Builder cannot load a non-3D physical object to a 3D physics global variable. |
| –310207 | The converter VI cannot export the output file correctly. |
| –310206 | This VI supports exporting to *.lvsg and *.ive file formats only. |
| –310205 | The Input Path control is empty. You must specify the path to the file you want to load and convert. |
| –310204 | The converter VI cannot load the file at the Input Path correctly. Make sure the file is not corrupt and try to load it again. |
| –310203 | This VI supports input files of only *.dae, *.lvsg, and *.ive file formats. |
| –310202 | The Input Path control is empty. You must specify the path to the file you want to load and convert. |
| –310201 | The simulation step size must be greater than 0. National Instruments recommends step sizes of 5 to 20 ms. |
| –310200 | The manifest file does not exist at the path you specified. Make sure you specify a valid path to a manifest file. |
| –310199 | The simulator cannot find an .stl file that the manifest file references. To correct this error, use the Offline Configuration VIs to read and modify the path to the .stl file in the manifest file. |
| –310198 | The component ID you specified does not correspond to any components in the manifest file for this simulation instance. |
| –310197 | The obstacle ID you specified does not correspond to any obstacles in the manifest file for this simulation instance. |
| –310196 | The robot ID you specified does not correspond to any robots in the manifest file for this simulation instance. |
| –310195 | The input manifest file is not valid. Use the Robotics Environment Simulator Wizard or the VIs on the Offline Configuration palette to generate valid manifest files. |
| –310194 | The actuator ID you specified does not correspond to any actuators associated with the robot ID in the manifest file for this simulation instance. |
| –310193 | The sensor ID you specified does not correspond to any sensors associated with the robot ID in the manifest file for this simulation instance. |
| –310192 | The robotics simulator is already running another simulation program. You can run only one simulation program at a time. |
| –310191 | The robotics simulator is not correctly initialized. Make sure the Start Simulator Service VI runs before any initialization driver VIs for simulated sensors or actuators. |
| –310190 | The joint parameter in the manifest file is not valid. |
| –310189 | You can only add geometries to a component. |
| –310188 | The robot joint ID does not correspond to any joints associated with the robot ID in the manifest file for this simulation instance. |
| –310174 | The input parameter is not valid. |
| –310173 | The joint type you use does not support the current operation. |
| –310172 | The number of rows and number of columns in the friction coefficient table must be the same. |
| –310169 | The ODE physical engine returned an error. Verify that the physical properties of the robot model are valid. You also can change the value of the step size input to the Start Simulator Service VI to avoid this error. |
| −310132 | The type of the input sentence does not match the Parse GPS Sentence VI polymorphic instance you selected. Make sure you select the correct polymorphic instance for the type of the sentence you want to parse. |
| −310131 | The input sentence contains formatting that makes the sentence invalid. For example, an NMEA sentence must begin with $, contain an * followed by a valid checksum, and be less than 83 characters in length. |
| −310130 | The input text contains none of the GPS data points the Get GPS Data VI returns. |
| −310120 | No available headings for travel exist because obstacles within the distance threshold of the vehicle block all possible headings. |
| −310085 | The wheel radius is invalid. The radius must be a positive, non-zero value. |
| −310084 | You cannot replace wheels in a built-in steering frame, such as a differential steering frame, because different wheel types are inconsistent with the definition of that steering frame type. |
| −310083 | The motor communication session is invalid. Use the Initialize Motor Communication VI to generate a valid LabVIEW class object. |
| −310082 | The steering frame is invalid. Steering frames must contain at least one wheel. |
| −310081 | You cannot remove wheels from the built-in steering frame, such as a differential steering frame, because fewer wheels are inconsistent with the definition of that steering frame type. |
| −310080 | You cannot add wheels to a built-in steering frame, such as a differential steering frame, because additional wheels are inconsistent with the definition of that steering frame type. |
| −310048 | The length and offset arrays for the SCARA arm each must contain four elements. |
| −310047 | The kinematic parameters and dynamic parameters arrays for the arm each must be of equal size. |
| −310046 | No valid solutions exist. Ensure the desired position is within the achievable workspace. |
| −310045 | The kinematic parameters specified do not match the parameters this VI requires. Refer to the help topic for this VI for the required parameters. |
| −310044 | The transform is formatted incorrectly. A valid transform is a 4-by-4 matrix with a last row in the form of [0 0 0 1]. |
| −310043 | The dynamic parameters you specified are not within the range of valid values. For example, the mass of a link cannot be a negative value. Make sure the values you specify are valid. |
| −310042 | The kinematic parameters you specified are not within the range of valid values. Make sure the values you specify are valid. |
| −310041 | The number of elements in the joint position, joint velocity, or joint acceleration array is not equal to the number of links in the serial arm. Make sure the number of elements in the array matches the number of links in the arm. |
| −310040 | LabVIEW cannot converge to a solution in the number of steps you specified. Make sure that the serial arm can achieve the transform you desire. |
| −310021 | The map contains nodes that are not compatible with the AD* VIs. Use the A* VI instead or update the map to use supported nodes. |
| −310020 | No valid paths exist between the start reference and the goal reference. |
| −310004 | The cell costs in the occupancy grid must all be greater than or equal to 0. Make sure all values in the occupancy grid array input are greater than or equal to 0. |
| −310003 | You cannot set a cell or edge cost to be less than 0. Set the cost to a value greater than or equal to 0. |
| −310002 | The x- and y-coordinates you specified refer to a cell outside of the occupancy grid map. Make sure you specify coordinates for a cell within the map. |
| −310001 | The reference to the map node you specified is null or does not refer to a valid node. |
| −310000 | The coordinate sizes of the two nodes do not match. Make sure you specify node coordinates with the same number of dimensions. |
| 310000 | LabVIEW ignored the request because the start node and end node specified for the edge are the same node. |
| 310001 | You set a cell or edge cost to 0, which might yield unexpected results in path planning applications. Set costs to values greater than 0 to help prevent unexpected results. |
| 310002 | One or more cell costs in the occupancy grid is 0, which might yield unexpected results in path planning applications. Set costs to values greater than 0 to help prevent unexpected results. |
| 310080 | LabVIEW coerced the steering angle of the wheel to meet the kinematic constraints of the wheel. |
| 310081 | The type of wheel used for this operation does not match the expected type. LabVIEW might return incomplete or unexpected values if the wheel does not contain expected data. |
| 310130 | The input text contained some but not all of the GPS data points the Get GPS Data VI returns. |
| 310131 | The input sentence contains an unexpected value. For example, the GGA polymorphic instance of the Parse GPS Sentence VI expects readings of height above mean sea level to be specified in meters. |
| 310132 | The sentence index of the input sentence is greater than the number of sentences the input sentence specifies is possible. |
| 310170 | The Take Simulation Steps VI only can work in a synchronized simulation mode. Make sure you set the timing mode of the Start Simulator Service VI as synchronized. |
| 310171 | The object that you imported does not exist in the Model Tree. |
| 310210 | Unable to load the robot model because some files are missing in the resource folder. |
| 310250 | You cannot write to a digital I/O line on a simulated robot. |
| 310251 | You cannot read the state of a digital I/O line on a simulated robot. |
| 310252 | You cannot write to a pulse width modulation (PWM) line on a simulated robot. |
| 310253 | You cannot write to an analog output line on a simulated robot. |
| 310254 | You cannot read the state of an analog input line on a simulated robot. |
| 310270 | The EtherCAT module communication is busy. |
| 310272 | Unable to find the KUKA youBot arm. Ensure that the KUKA youBot arm is mounted and open. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_glossary.html language=enus -->
## TOPIC 00010: Glossary (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_glossary.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_glossary.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Glossary (Robotics Module)

[LabVIEW Glossary](/csh?topicname=lvconcepts/glossary.html)

| A |  |
| --- | --- |
| A* | A path planner algorithm of computer science to find a least-cost path through a static Occupancy Grid map. |
| accelerometer | A device that measures the proper acceleration of the device. This is not necessarily the same as the coordinate acceleration (change of velocity of the device in space), but is rather the type of acceleration associated with the phenomenon of weight experienced by a test mass that resides in the frame of reference of the accelerometer device. |
| actuator | A physical device that applies the control action to the plant. |
| AD* | A dynamic path planner algorithm that plans a path from the initial location through a map to the goal you specify. |
| C |  |
| CAD model | A 3D description file for visualization of a robot, which typically includes the geometry, texture, and material information of the robot. The LabVIEW Robotics Module supports CAD model files with the extensions .ive, .dae, and .wrl. |
| component model | A wheel model, track model, arm model, conveyor model, or a simple object that you can use to assemble a robot model. |
| D |  |
| directed graph | A graphic structure where each edge is directed. A edge is the link that connect some pairs of vertices. |
| E |  |
| end effector | An end effector is the end of the last link in a serial arm. |
| G |  |
| gyroscope | A device that measures the orientation. |
| I |  |
| IMU | Inertial measurement unit. A sensor that contains gyroscopes and accelerometers. |
| J |  |
| Jacobian matrix | A matrix where each element is the first-order partial derivative of a certain variable of a function with respect to another variable of a vector. |
| L |  |
| link | A link is the basic component of a serial arm, which is connected with joints. |
| O |  |
| occupancy grid | An evenly spaced grid map to represent the map of the robotic environment. Each cell of the grid has a cost value representing the possibility or presence of an obstacle at that location in the environment. |
| P |  |
| posture | The posture of a robot contains the position and orientation of the robot. |
| Q |  |
| quaternion | A four-dimensional number system to represent the homogenous transformation in the Euclidean space. |
| R |  |
| robot model | A software representation of a robot for use in a simulated environment. A robot model consists of component models and joints, which connect the component models. |
| rotation matrix | A homogenous matrix to perform rotation transform in the Euclidean space. |
| S |  |
| serial arm | A serial arm consists of a base, a link or series of links connected at joints, and an end effector. The base is the first link in a serial arm, and the end effector is at the end of the last link in an arm. |
| steering frame | A structure that contains the distribution and dimension information of the wheels that you use for steering control. |
| V |  |
| vector field | A map in which each vector represents a point to indicate location, orientation, and magnitude of the point in the Euclidean space. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_mb_export.html language=enus -->
## TOPIC 00011: Importing and Exporting a Robot Model (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_mb_export.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_mb_export.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Importing and Exporting a Robot Model (Robotics Module)

In the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html), you can import robot models or import component models to assemble a simulated robot. You also can export the robots that you design for use in a [simulation program](../lvrobogsm/robo_sim_overview.html).

To import existing models, click the **Import** button and navigate to a robot model. The robot model files that LabVIEW Robotics Module supports are .xml files. The robot model that you import appears in the **Model View**. You can position, modify, and configure the robot model as you [design the robot model](../lvrobogsm/robo_design_robot.html).

Exporting the robot model enables you to save the robot model. Click the **Export** button to save the robot model as a .xml file. If you save the robot model to the default directory of LabVIEW Data\Robotics\Simulator\Model\Config\, the robot model appears in the **User Model Library** of the **Model Library** in the builder. Save the robot models in the Robot folder and save the component models in the Customized Parts folder. Robot and component models you save in these folders also appear in the [Robotics Environment Simulation Wizard](../lvrobodialog/robo_sim_wizard.html) as a component you can add when [creating a simulation scene](../lvrobogsm/robo_sim_creating.html).

|  | Note If you save the robot model to a directory other than the default directory, the model does not appear in the Model Library so you cannot add the model from the Model Library. You need to use the Import button to import the model. |
| --- | --- |

When you export the robot model, LabVIEW automatically creates a folder in the same directory that you save the [manifest file](../lvrobogsm/robo_sim_overview.html#framework). This folder stores the resource files of the robot model, such as the CAD files and texture. The name of the folder uses the format of *model_name*RSC. For example, if you create a robot model with the name *my_robot*, the resource folder for this robot model is my_robotRSC. Do not delete, rename, or modify any content in this folder.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_mb_properties.html language=enus -->
## TOPIC 00012: Configuring the Properties of Robot Parts (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_mb_properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_mb_properties.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Configuring the Properties of Robot Parts (Robotics Module)

Robots and robot parts have properties that you can use to configure a robot model. You can view and configure the properties of a robot and robot parts in the **Properties** table of the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html). The properties of a robot part include the part ID, visual information, and physical information. Edit values in the **Properties** table to configure the properties of the robot model.

Use the following methods to configure the properties of a robot part:

- Robot Simulation Model Builder —When you select a robot part in the builder, the properties of this part display in the Properties table. Click one of the properties to change the value. In the Model View , the visual and physical models of the robot part change as you modify the properties.
- CAD Model Importer —If you want to edit the properties of a component or edit the visual and physical model properties of a component, launch the CAD Model Importer and edit the properties of the component. In the importer, you can change the physical model of the component or edit the properties of the component in the Properties table.
- Component Model Dialog Boxes —When you add or edit complex parts, such as SD6 tracks , Omni and Mecanum wheels , and DH arms , you can use the Configure Track , Configure Wheel , and DH Arm Generator dialog boxes for editing properties.

The following table contains descriptions of the properties that you use to configure a robot part.

| Property | Where to Configure Property | Description |
| --- | --- | --- |
| Movable | Robot Simulation Model Builder CAD Model Importer | If the value is True, the robot part is a stationary object which has infinite mass. |
| Mass | Robot Simulation Model Builder CAD Model Importer | Defines the mass of a robot part. Note If the robot part contains multiple components, this property displays the total mass of the robot part, including all the sub-components. If the inertia matrix of the robot part is all-zero, you cannot configure the total mass of the robot part in the Robot Simulation Model Builder. You can only edit the robot part in the CAD Model Importer and configure the mass for each component. |
|  | Note If the robot part contains multiple components, this property displays the total mass of the robot part, including all the sub-components. If the inertia matrix of the robot part is all-zero, you cannot configure the total mass of the robot part in the Robot Simulation Model Builder. You can only edit the robot part in the CAD Model Importer and configure the mass for each component. |  |
| Mass Center | Robot Simulation Model Builder CAD Model Importer | Defines the center of the mass or gravity. The center of mass is the point in the robot part where the entire mass is concentrated. |
| Inertia Matrix | Robot Simulation Model Builder CAD Model Importer | Inertia Matrix is a 3x3 matrix that describes the way to distribute mass of the body around the center of mass. The Mass Center and Inertia Matrix are only effective when the Inertia Matrix is not all-zero. |
| Material Type | Robot Simulation Model Builder CAD Model Importer | Defines the friction coefficient of a robot part at the contact point with other parts. Refer to the Kinetic Friction Coefficient Table VI in the labview\\vi.lib\\robotics\\Simulator\\Interface\\Utility directory to view a table of the default friction coefficients for each type of material. Note If you are configuring a robot part combined with multiple components and each component uses a different material type, you cannot configure the material type of the robot part in the Robot Simulation Model Builder. Edit the robot part in the CAD Model Importer and configure the material type for each component. |
|  | Note If you are configuring a robot part combined with multiple components and each component uses a different material type, you cannot configure the material type of the robot part in the Robot Simulation Model Builder. Edit the robot part in the CAD Model Importer and configure the material type for each component. |  |
| Subspace Name | Robot Simulation Model Builder CAD Model Importer | A subspace represents a collection of robot parts and joints that are located near each other. This property defines the name of the subspace. Robot parts in the same subspace cannot collide with each other. |
| Color | Robot Simulation Model Builder CAD Model Importer Configure Wheel Dialog Box Configure Track Dialog Box DH Arm Generator Dialog Box | Sets the color of a robot part. If the robot part has texture, this item changes the color of the physical model. If the robot part does not have texture, this item changes the color of the visual model. |
| Resolution (EU) | Robot Simulation Model Builder | Sensor resolution is the smallest change a sensor can detect in the quantity that the sensor is measuring. Engineering Unit (EU) is the unit defined by different sensors. |
| Sample Rate (Hz) | Robot Simulation Model Builder | Defines the rate at which sensors do sampling. |
| Feedback | Robot Simulation Model Builder | Feedback property appears in the Properties table only when you select a joint in the Parts Hierarchy. Feedback refers to the force a joint applies directly to the parts it connects. If the value of the feedback property is True, you can read force or torque feedback from the joint. Note The Robotics Module provides a force control method for you to apply a force to a motor when you simulate mobile robots. If a joint motor is under force control, you cannot read force or torque feedback from the joint. |
|  | Note The Robotics Module provides a force control method for you to apply a force to a motor when you simulate mobile robots. If a joint motor is under force control, you cannot read force or torque feedback from the joint. |  |
| Ground Level | CAD Model Importer | Defines the position of the ground plane along the z-axis. |
| Roller Number | Configure Wheel Dialog Box | The number of rollers on the wheel frame. |
| Radius Offset | Configure Wheel Dialog Box | The offset between the roller position and the radius of the wheel frame. |
| Row Number | Configure Wheel Dialog Box | The number of rows of rollers on an Omni wheel. |
| Height Offset | Configure Wheel Dialog Box | The position of rollers on the height axis of an Omni wheel frame. This property only works when the row number is larger than 1. |
| Roller Orientation | Configure Wheel Dialog Box | Defines the orientation of the rollers on a Mecanum wheel. |
| Twist Angle | DH Arm Generator Dialog Box | Defines the angle, in radians, between the rotation axis of the joint of this link and the rotation axis of the next joint with respect to the link. |
| Length | DH Arm Generator Dialog Box | Defines the length of the link between the joint of this link and the next joint. |
| Rotation Angle | DH Arm Generator Dialog Box | Defines the angle of rotation, in radians, between this link and the next link along the rotation axis of the joint that connects the links. |
| Offset Distance | DH Arm Generator Dialog Box | Defines the distance from this link to the next link along the axis of the joint that connects the links. |
| Joint Displacement | DH Arm Generator Dialog Box | Joint displacement is the displacement from the joint to the origin of the coordinate system of the Denavit-Hartenberg (DH) arm along the Z- axis of the coordinate system. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_motors.html language=enus -->
## TOPIC 00013: Attaching and Detaching Motors (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_motors.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_motors.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Attaching and Detaching Motors (Robotics Module)

Motors control the motion of robot models. You can attach motors to the joints in a robot model. To attach motors to a joint, right-click the joint, and select **Set Motors»New** from the shortcut menu. When you attach a motor to a joint, the motor ID and motor rate display in the **Properties** table of the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html).

|  | Note You cannot attach motors to spring joints, because spring joints move passively only when the two robot parts the joint connects move. |
| --- | --- |

You can [configure the rate of the motor in the Properties table](../lvrobogsm/robo_mb_properties.html) to control the linear or angular velocity of a joint. The motor rate is the ratio of the motor velocity to the joint velocity as defined by the following equation.

[IMAGE alt='image' src='loc_eq_mrate.gif']

where *v<sub>j</sub>* is the joint velocity, *r<sub>m</sub>* is the motor rate, and *v<sub>m</sub>* is the velocity of the motor that attaches to the joint.

If the joint type is hinge or revolute, the joint velocity is angular velocity. If the joint type is slider or prismatic, the joint velocity is linear velocity. The value of the motor rate can be negative or positive.

The [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html) automatically deletes motors that are not attached to any joints. To detach a motor from a joint, select the joint in the **Parts Hierarchy** list, right-click the joint, and select **Set Motors** from the shortcut menu. Click the motor that you want to detach.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_new_features.html language=enus -->
## TOPIC 00014: Version 2014 Features (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_new_features.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_new_features.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Version 2014 Features (Robotics Module)

This topic lists new features and changes in the LabVIEW 2014 Robotics Module. Refer to the [LabVIEW 2014 Features and Changes](/csh?topicname=lvupgrade/labview_features.html) topic for information about new features in LabVIEW 2014.

|  | Note Refer to the readme_Robotics.html file, located in the labview\\readme directory, for a complete list of new features and changes, information about upgrade and compatibility issues specific to different versions of the Robotics Module, and information about known issues with the LabVIEW 2014 Robotics Module. |
| --- | --- |

#### Conveyor Model

The [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html) contains a conveyor model in the in the **Built-in Model Library** folder of the **Model Library**. LabVIEW provides a linear conveyor model for you to create conveyors for a robot model. You can use the conveyor model to simulate an assembly line or a transporter line. Click and drag the linear conveyor from the **Model Library** to the **Model View** to add a linear conveyor. When you add a linear conveyor to a robot model, the **Configure Conveyor** dialog box opens. You can configure the properties of the conveyor in the **Configure Conveyor** dialog box. Click **OK** to add the conveyor to the robot model.

#### Piston Joint

The Robotics Module provides a new type of joint for connecting robot parts in the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html). You can use the piston joint to connect robot parts. The piston joint allows the two parts to move closer to and apart from each other. The two parts can also rotate around the translation axis. The Robotics Module provides one type of piston joints, the spring joint, which returns to the original length when the joint is free of external forces. To add a spring joint to a robot model, select a joint in the **Parts Hierarchy**, right-click the joint, and select **Joint Type»Piston»Spring** from the shortcut menu.

#### Reading Force Feedback from Joints

Force feedback from a joint refers to the force that the joint applies to the parts it connects. In the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html), you can configure the feedback property of joints. If the value of the feedback property is True, you can read force or torque feedback from the joint.

|  | Note The Robotics Module provides a force control method for you to apply a force to a motor when you simulate mobile robots. If you use the force control method to control a joint motor, you cannot read force or torque feedback. |
| --- | --- |

#### Behavior Changes

The LabVIEW 2014 Robotics Module introduces the following behavior changes.

##### VI Changes

The Robotics Module 2014 includes the following change to VIs:

The 5R Type 1 Serial Arm instance in the [Initialize Serial Arm](../lvrobovi/init_serial_arm.html) polymorphic VI on the [Serial Arm Definition](../lvrobovi/serial_arm_def_pal.html) palette has the new L4 parameter.

##### New Control Method

The Robotics Module 2014 includes the following new control method:

The force control method allows you to apply a force to a motor when you simulate mobile robots.

##### New Examples

The labview\examples\robotics directory includes the following new examples:

- Simulator\Gravity Compensation\Gravity Compensation.lvproj
- Simulator\Industrial Robot Arm\Industrial Robot Arm.lvproj
- Simulator\Springed Starter Kit\Springed Starter Kit.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_position_models.html language=enus -->
## TOPIC 00015: Viewing and Positioning Robot Models (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_position_models.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_position_models.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Viewing and Positioning Robot Models (Robotics Module)

The robot coordinate system represents the posture of a robot in a 3D environment. The posture of a robot contains the position and orientation of the robot. In the [Robot Simulation Model Builder](../lvrobodialog/robo_model_builder.html), the red, green, and blue rays represent the X-, Y-, Z- axes of the robot coordinate system. The intersection of the three rays is the origin of the robot coordinate system. The green grid is the XY plane of the system, which crosses the origin and the X- and Y- axes. The origin of the robot must coincide with the origin of the robot coordinate system. Use the 3D positioner, as shown in the following figure, to move a robot or component model along the X-, Y-, and Z- axes in the robot coordinate system.

[IMAGE alt='image' src='noloc_env_3dpositioner.gif']

If you add physical models in the [CAD Model Importer](../lvrobodialog/robo_model_importer.html), the red, green, and blue rays represent the X-, Y-, Z- axes of the world coordinate system. You can position the physical models to the CAD model along the X-, Y-, and Z- axes. The geometric center of the CAD model is the origin of the world coordinate system.

As you [design a robot model](../lvrobogsm/robo_design_robot.html) in the builder, you can view the robot model in the **Model View** preview window. The following table lists actions you can perform to customize your view of the robot model or objects in the **Model View**.

| Action | Shortcut/Movement |
| --- | --- |
| Move the camera around the scene. | Click and drag the environment. |
| Zoom in and out of the 3D scene. | Hold <Shift>, and then click and drag in the 3D scene. |
| Reposition the environment within the scene. | Hold <Ctrl>, and then click and drag the environment. |

You can specify the position and orientation of a robot model in the **Model View**. The following table lists actions you can perform to drag, rotate, or reposition the robot parts in the **Model View**.

| Action | Shortcut/Movement |
| --- | --- |
| Move a component along the axes. | Click and drag the component along the X-, Y-, and Z- axes. |
| Rotate a robot model or component around the axes of the robot model. | Click and drag the component along the XY-, YZ-, XZ- axes. |
| Move the component along the Z- plane surface. | Hold <Ctrl> and drag the component. |
| Undo the last action. | Press <Ctrl–Z>. |

If you need to change the posture of multiple components in the **Model View**, select the root component of multiple components in the **Parts Hierarchy** tree, right-click the root component, and select **Select Branch** from the shortcut menu to select all the components that belong to this root. You also can select multiple components by holding <Ctrl> and selecting multiple items in the **Parts List** or **Parts Hierarchy** tree.

To specify the exact position and orientation of a robot model, use the **Properties** table to [configure the properties of robot parts](../lvrobogsm/robo_mb_properties.html).

|  | Note If you select multiple components and use the Properties table to configure the position properties, the position of the first component you select changes accordingly. Other components also move to maintain their relative position to the first component you select. |
| --- | --- |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_project_overview.html language=enus -->
## TOPIC 00016: Creating Robotics Applications (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_project_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_project_overview.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Creating Robotics Applications (Robotics Module)

With the Robotics Module, you must use a [LabVIEW project](/csh?topicname=lvconcepts/using_labview_projects.html) (.lvproj) to build and configure robotics applications and to work with RT and FPGA targets. Use projects to group LabVIEW files and non-LabVIEW files, configure communication between hardware, create build specifications, and deploy files to targets.

[Use the Robotics Project Wizard](../lvrobogsm/robo_project_creating.html) to create a new project that includes hardware targets, sensors, VIs, and other application files.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_related_doc.html language=enus -->
## TOPIC 00017: Related Documentation (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_related_doc.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Robotics Module)

The following documents contain information that you might find helpful as you use the Robotics Module.

#### Tutorials

- Getting Started with NI LabVIEW Robotics—Visit ni.com for information and resources about using the LabVIEW environment, robotics-specific capabilities, NI reconfigurable I/O (RIO) hardware, and Robotics simulation examples.
- Getting Started with the LabVIEW Robotics Module—Use this manual to familiarize yourself with the LabVIEW Robotics software and concepts behind building a robotics application in LabVIEW. 
 The Getting Started with the LabVIEW Robotics Module manual is available in the labview\manuals directory. You must have Adobe Reader 6.0.1 or later installed to view or search the PDF versions of the manual. Refer to the Adobe Systems Incorporated Web site to download Adobe Reader. Refer to the National Instruments Product Manuals Library for updated documentation resources.

#### Product Documentation

- LabVIEW Robotics Module Readme —The readme_Robotics.html file contains information to help you install and configure components in the LabVIEW Robotics package and a list of new features. The file also provides information on known issues with the LabVIEW Robotics Module. Access this document by navigating to the labview\readme directory and opening readme_Robotics.html .
- Additional LabVIEW documentation for LabVIEW add-ons such as the Real-Time Module, FPGA Module, and so on.

#### External Source

- Open Dynamics Engine (ODE) Manual—Refer to the ODE Manual at www.ode-wiki.org/wiki for detailed information about ODE-specific concepts and terms.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_creating.html language=enus -->
## TOPIC 00018: Creating a Simulation Scene (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_creating.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_creating.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Creating a Simulation Scene (Robotics Module)

A simulation scene of a [simulation program](../lvrobogsm/robo_sim_overview.html) contains the components you want to simulate. Components in a Robotics Module simulation typically include the environment, or ground plus any attached features; robots, which might have sensors and actuators attached; and obstacles. Each component has associated properties that define its physical state. For example, gravity is a property of environments and mass is a property of robots.

You save information about components in a [manifest file](../lvrobogsm/robo_sim_overview.html#framework). When you run a simulation program that [calls the manifest file](../lvrobogsm/robo_sim_programming.html#start_sim), the simulator reads from the file and displays the scene.

#### Designing a Simulation Scene with Predefined Components

Use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to design a robotics simulation scene that contains predefined components. After you design a scene, the wizard saves the simulation scene definition in a manifest file and generates [simulation-related files](robo_sim_overview.html#proj_parts) in a LabVIEW project.

As you design a simulation scene in the wizard, you can perform the following actions to customize the **Simulation Scene** preview window.

| Action | Shortcut/Movement |
| --- | --- |
| Move the camera around the scene. | Click and drag the environment. |
| Zoom in and out of the 3D scene. | Hold <Shift>, and then click and drag in the 3D scene. |
| Zoom out to an overhead view of the environment. | Double-click the 3D scene. |
| Zoom in and focus on an object. | Double-click the object. |
| Reposition the environment or an object within the scene. | Hold <Ctrl>, and then click and drag the environment or object. |
| Rotate an object around the axis you select in the Rotation Behavior pull-down menu. | Click and drag the object. |
| Remove an object from the simulator. | Select the object and press <Delete>. |

|  | Tip The Robotics Environment Simulator Wizard displays helpful messages in the lower left corner, depending on where you position the cursor and what actions you take. |
| --- | --- |

To modify the properties of a component, such as the mass of a robot, select the component in the simulation scene, and then click the property or value you want to modify in the **Properties** table at the bottom left of the wizard.

#### Designing a Simulation Scene with Custom Components

To design a simulation scene and components manually rather than with the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html), you can use the [Offline Configuration](../lvrobovi/simulator_config_pal.html) VIs to create a simulation scene on the block diagram and save it in a manifest file. One benefit of designing a simulation scene manually is the ability to [associate a custom environment with the simulation scene](robo_sim_environment.html).

|  | Note Using the Offline Configuration VIs to create a simulation scene is an advanced feature. To create a simulation scene that does not require custom components, use the Robotics Environment Simulator Wizard instead. |
| --- | --- |

When you design a simulation scene manually, you define components individually, and then save their definitions in a manifest file. The following block diagram shows a simple example of defining an environment and robot and saving their definitions in a manifest file.

[IMAGE alt='image' src='loc_bd_save_manifest.gif']

|  | Note Use SI units and SI-derived units when you define component properties. |
| --- | --- |

The previous block diagram uses the following components to construct the manifest file:

- New Simulation Object VIs specify the type of components to create.
- Property Nodes define the unique properties of the new Starter Kit 1.0 robot and associate the robot with the new simulation instance.
- The Save Simulation Instance VI saves a manifest file you can call in a simulation VI when you start the simulator.

|  | Tip To make a simulation scene accessible in the Robotics Environment Simulator Wizard, save the manifest file in the labview\\resource\\plugins\\NewDialogFiles\\ProjectWizards\\Robotics\\LV4R_SIM\\Config\\Template directory. |
| --- | --- |

Refer to the Create Manifest File VI in the labview\examples\robotics\Simulator\iRobot Create directory for an example of manually creating a simulation scene and manifest file.

When you use the [Offline Configuration](../lvrobovi/simulator_config_pal.html) VIs to create a simulation scene, you do not need to develop the simulation program in a LabVIEW project.

#### Reading and Modifying Properties of Components

After you create a robotics simulation scene and save the definition in a .xml manifest file, you can [read or modify the properties of components](robo_sim_reading.html) in the manifest file.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_deploying.html language=enus -->
## TOPIC 00019: Running a Simulation Program on a Real Robot (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_deploying.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_deploying.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Running a Simulation Program on a Real Robot (Robotics Module)

After you program and view a [robotics simulation program](../lvrobogsm/robo_sim_overview.html), you can make a few modifications to the VIs and then run them on a hardware target that controls a real robot. You must use a [LabVIEW project with simulation-related files](../lvrobogsm/robo_sim_overview.html#proj_parts) to organize and deploy the code to hardware. Complete the following steps to prepare a simulation program to run on real hardware and then deploy the program.

1. In the Project Explorer window, add the hardware target to which you want to deploy the application.
 [IMAGE alt='image' src='note.gif']
**Note** If you use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to create a simulation scene, you can use the same project the wizard generates.
2. Under the hardware target, add the master simulation VI and any subVIs you create as part of the program. Do not move the .xml manifest file under the target.
3. Open each VI and remove or reconfigure any LabVIEW code related to simulation. The following tasks describe common steps you must take:
  - Remove any VIs that control the simulator itself, such as the Start Simulator Service and Stop Simulator Service VIs.
  - Remove initialization driver VIs for simulated sensor and actuators . Replace the simulation initialization VIs with initialization VIs for real devices.
  - Remove the Get Simulator Reference VI and any Property Nodes and Invoke Nodes you use to manipulate simulated components.
  - Remove any Offline Configuration VIs.
4. Right-click the VI under the hardware target that served as the master simulation VI and select Deploy from the shortcut menu to deploy the VI and any support files for the VI to the target.

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of a project that contains both a simulation program and a hardware target with the program modified to run on the target.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_distributing.html language=enus -->
## TOPIC 00020: Distributing a Simulation Program (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_distributing.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_distributing.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Distributing a Simulation Program (Robotics Module)

After you [write a robotics simulation program](robo_sim_programming.html), you can build the code into a stand-alone application that you can distribute to other users. Applications are useful when you want users to run VIs without installing the LabVIEW development system.

Complete the following steps to create a stand-alone application from a simulation program.

1. Create a build specification for the stand-alone application, but do not build it yet. Perform the following actions on the Source Files page of the Application Properties dialog box:
  - Specify that you want the master simulation VI to serve as the startup VI that displays and runs when you launch the application.
  - Add the .xml manifest file the master VI calls to the Always Included list.
2. Build the stand-alone application as described in the instructions for creating a build specification .
3. Copy the following files to the support directory that you specify on the Destinations page of the Application Properties dialog box:
  - The resource folder ( xxxRSC ) in the project directory
  - (Optional) To customize the friction coefficient table, copy this file: labview\vi.lib\robotics\Simulator\Interface\Utility\Kinetic Friction Coefficient.txt

Complete the following steps to create an installer to distribute the stand-alone application you created from a simulation program.

1. Add the resource folder ( xxxRSC ) as a new folder in the LabVIEW project .
2. Create a build specification for the installer, but do not build it yet.
3. In the Source Files page of the Installer Properties dialog box, add the following files to the Destination View :
  - The stand-alone application you created from the simulation program
  - The resource folder ( xxxRSC ) in the project directory
 [IMAGE alt='image' src='note.gif']
**Note** The directory structure of the resource folder in the **Destination View** must match the directory structure in the project directory and LabVIEW project. If the **Destination View** does not have this directory structure, create the structure in the [Destinations](/csh?topicname=lvdialog/destinations_install_page.html) page of the [Installer Properties](/csh?topicname=lvdialog/installer_tab_windows.html) dialog box.
The resource folder must reside under the support directory you specify in the [Destinations](/csh?topicname=lvdialog/destination_settings_db.html) page of the [Application Properties](/csh?topicname=lvdialog/build_app_or_dll_db.html) dialog box. For example, if the resource folder resides under the support directory MyFolder, the **Destination View** in the [Source Files](/csh?topicname=lvdialog/files_install_page.html) page of the [Installer Properties](/csh?topicname=lvdialog/installer_tab_windows.html) dialog box must have the following directory structure: MyFolder\xxxRSC.
  - (Optional) The friction coefficient table located at: labview\vi.lib\robotics\Simulator\Interface\Utility\Kinetic Friction Coefficient.txt
4. In the Additional Installers page of the Installer Properties dialog box, place a checkmark next to the following items in the National Instruments Installers to Include list:
 
 [IMAGE alt='image' src='note.gif']
**Note** The version of the LabVIEW Run-Time Engine and the LabVIEW Robotics Runtime Engine must be the same.
  - LabVIEW Run-Time Engine
  - LabVIEW Robotics Module Runtime
5. Build the installer as described in the instructions for creating a build specification .

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_environment.html language=enus -->
## TOPIC 00021: Using CAD Files to Define a Simulated Environment (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_environment.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_environment.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Using CAD Files to Define a Simulated Environment (Robotics Module)

When you [simulate a mobile robot](../lvrobogsm/robo_sim_overview.html), parts of the [simulated environment](../lvrobogsm/robo_sim_overview.html#framework) are defined in .ive and .stl files. The robotics simulator uses these files, along with other data, to render the environment. You can export information about an environment that is saved in an existing CAD file to a .ive file. Use this .ive file with an existing .stl file that corresponds to the original CAD file to define an environment you can use in the robotics simulator.

Complete the following steps to use CAD files to define a simulated environment and save the definition to a file.

1. Open and run the CAD Model Converter VI located in the labview\vi.lib\robotics\Simulator\Interface\Utility\Converter directory.
2. Enter the path to the CAD file you want to convert in the Input Path control. This VI supports CAD files with the following file formats: .dae , .ive , and .lvsg .
3. In the Export Path control, enter the path to a .ive file to which you want to export information from the CAD file. Save the file in a subdirectory of the labview\resource\robotics\simulator\CADModels\environment directory.
 .ive files describe the visualization model of the environment.
4. Click the Export button export the CAD information to the .ive file.
5. Save an existing .stl file that corresponds to the original CAD file in a subdirectory of the labview\resource\robotics\simulator\CADModels\environment directory.
 .stl files are triangle mesh files that describe the physical model of the environment.
6. Use the Offline Configuration VIs to create a .xml file that defines an environment according to these .ive and .stl files. The following block diagram shows an example of designing a simulated environment manually and saving the environment in a .xml file you can load in the Robotics Environment Simulator Wizard .
 [IMAGE alt='image' src='loc_bd_import_environment.gif'] 
 In the previous block diagram, the Property Node associates the .ive and .stl files with the definition for a new simulated environment. The Flatten to XML function and the Save Manifest File String VI, which is located in labview\vi.lib\robotics\Simulator\Interface\Simulator Configuration directory, save the definition to disk.

To make a simulation scene whose environment is defined in .ive and .stl files accessible in the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html), save the .xml file in the labview\resource\plugins\NewDialogFiles\ProjectWizards\Robotics\LV4R_SIM\Config\Environment directory.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_overview.html language=enus -->
## TOPIC 00022: Simulating Mobile Robots (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_overview.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Simulating Mobile Robots (Robotics Module)

Simulating a mobile robot that runs an embedded application allows you to design and debug the application without depending on the physical robot. When you simulate a robot, you can validate the mechanical structure of the robot, test algorithms that control it, and visualize the robot in an environment before you deploy and run the application on real hardware. In the LabVIEW Robotics Module, use the built-in robotics simulator to render a 3D simulation scene and model the motion of real robots in a real-world environment. You create robotics applications to run in the simulator similarly to how you design LabVIEW applications that run on real robots.

The following steps describe the process you use to simulate robots in LabVIEW.

1. Design a simulated robot that you can use in a simulation scene.
2. Design the simulation scene with the environment and robots you want to simulate.
3. Write VIs to start the simulator and control simulated components.
4. Run a master simulation VI to display the simulation as it runs.
5. (Optional) Create an executable that displays the simulation so you can distribute it to other users.
6. (Optional) Deploy the same VIs to a real hardware target

#### Overview of Robotics Simulation in LabVIEW

Robotics simulation programs in LabVIEW include the following items:

- Robotics simulator —The simulator reads and displays simulation scenes you design, calculates realistic, physics-based properties of simulated components as they interact, and advances the time in the simulation. You start the simulator in a VI you write.
- Simulation program —You create programs to run in the simulator. These programs contain the following components:
  - Manifest file —When you design a simulation environment and components, you save their definitions in a .xml file, called a manifest file. The simulator reads from manifest files to render the components they define.
    - Simulation scene —Each manifest file defines one simulation scene, a combination of simulated components and their properties. You can render one simulation scene at a time in the simulator. Simulation scenes contain the following components:
      - Environment —Each simulation instance must have an environment that describes the ground and any attached features. The environment also has associated physical properties, such as the surface material and force of gravity.
      - Robots —Robots can contain simulated sensors and actuators . Because sensors and actuators are not synchronous to the simulation programs, robots containing sensors and actuators do not act deterministically. The same input may result in different outputs.
      - Obstacles —Environments can contain obstacles that are separate from the environment and have their own associated properties.
  - VIs —You write VIs to control the simulator and simulated components. The VIs contain the same code to control simulated robots that embedded applications running on real robots might contain.
  - ID List —When you create a simulation project using the Robotics Environment Simulator Wizard , the project includes an ID list file under the simulation target. The ID list file is a .txt file that contains ID names of the simulated robot, the components of the robot, and the obstacles in the environment.
- Display window —When you start the simulator, the simulation displays in a 3D picture control .

#### Overview of a Simulation Project

You might find it useful to organize simulation programs in [LabVIEW projects](/csh?topicname=lvconcepts/using_labview_projects.html). Projects group files and allow you to deploy them to hardware. Use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to automatically generate a project similar to the one in the following screenshot, or [create a similar project manually](robo_sim_creating.html#offlineconfig).

|  | Note You do not need to use a LabVIEW project to run the simulator and display a simulation scene. However, to use the Robotics Environment Simulator Wizard or create an executable you can distribute, you must use a project. |
| --- | --- |

[IMAGE alt='image' src='loc_env_sim_proj.gif']

The previous LabVIEW project shows the following items:

- Robotics Environment Simulator ( )—Organizes the files that define and control components in a particular simulation scene. LabVIEW adds this item to a project when you use the Robotics Environment Simulator Wizard to create a simulation scene. Right-click this item in the Project Explorer window and select Properties from the shortcut menu to launch the wizard and modify components in the current simulation scene .
- Robotics Environment Simulator ID List.txt —Contains the ID names of the components in the simulation scene you create. LabVIEW adds this item to a project when you use the Robotics Environment Simulator Wizard to create a simulation scene.
- Robotics Environment Simulator.vi —Starts and stops the simulator, serves as a user interface for the simulation, and calls LabVIEW code that manipulates components in the simulation .
- Robotics Environment Simulator.xml —Serves as the manifest file that contains definitions for components in the simulation scene you create. LabVIEW adds this item to a project when you use the Robotics Environment Simulator Wizard to create a simulation scene.
 [IMAGE alt='image' src='note.gif']
**Note** Do not directly edit the contents of this manifest file to change the simulation scene. Instead, use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) or the [Offline Configuration](../lvrobovi/simulator_config_pal.html) VIs to modify the scene.
- subVIs —Organizes subVIs and any additional files you include to control the simulation scene.
- Dependencies —Contains device driver VIs and other items that VIs in the project require. You cannot add items directly to Dependencies . Dependencies updates automatically when you add, remove, or save an item in the project.
- Build Specifications —Includes build configurations for stand-alone applications.

In the simulation project folder, LabVIEW creates a [resource (RSC) folder](../lvrobogsm/robo_mb_export.html) to store the resource files for simulation. When you rename the simulation target ([IMAGE alt='image' src='noloc_env_sim_glyph.gif']), the names of the manifest file and the ID list file automatically change to match the target name. However, you need to manually update the resource folder. To create a new resource folder for the updated simulation target, select the target in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, right-click the target, and select **Properties** from the shortcut menu to launch the wizard. Save the simulator from the wizard and LabVIEW creates a *NewName*RSC folder in the same directory that you save the manifest file.

#### Recommendations for Simulating Robots

The following list describes some of the caveats and recommendations to consider when you run the robotics simulator:

- Run only one simulation program at a time. If you start the simulator when another simulation program is running, LabVIEW returns error code –310192 .
- If you experience performance issues when you run a simulation on a single-core CPU, run the simulation on a multicore CPU to improve the performance.
- Use step sizes to balance the performance of the simulator with its accuracy. When you start the simulator , you must specify a step size, in milliseconds, that defines the amount of time that elapses in the environment between updates the simulator makes to physical properties. Large step sizes result in less accurate real-world behavior. Smaller step sizes result in a simulation that more accurately models real-world behavior, but they require more processor resources.
- Maintain a constant step size when you run a simulation.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_physics.html language=enus -->
## TOPIC 00023: Units of Measurement in the Robotics Simulator (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_physics.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_physics.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Units of Measurement in the Robotics Simulator (Robotics Module)

When you [design a simulation scene](robo_sim_creating.html) or [read and write properties of components](robo_sim_reading.html) in a simulation scene, express values in appropriate units of measurement. The [robotics simulator](robo_sim_overview.html) recognizes many of the same [SI units and SI-derived units that LabVIEW recognizes](/csh?topicname=lvhowto/available_units_in_labview.html), as described in the following table.

| Quantity Name | Unit | Abbreviation |
| --- | --- | --- |
| acceleration (gravity) | meters per second squared | m/s2 |
| frequency (sampling rate) | hertz | Hz |
| latitude, longitude | degree | deg |
| length (altitude, range, position of objects relative to origin) | meter | m |
| mass | kilogram | kg |
| plane angle (rotation) | radian | rad |

Resolution, a quantity associated with simulated sensors, expresses the minimum accuracy of the data being acquired.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_programming.html language=enus -->
## TOPIC 00024: Writing VIs to Control a Simulation (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_programming.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_programming.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Writing VIs to Control a Simulation (Robotics Module)

After you [create a simulation scene](robo_sim_creating.html), write VIs to control the components in the scene when you view it in the [robotics simulator](robo_sim_overview.html). You typically create a master simulation VI that performs the following tasks:

- Starts the simulator.
- Manipulates components, such as robots, in the simulation.
- Serves as a user interface for passing data into and out of the simulator.

Use the [Simulator Assistant](../lvrobovi/sim_asst.html) to interactively configure the robotics simulator and interaction with robot components in a simulation scene. Drop the Simulator Assistant inside a [loop](/csh?topicname=lvconcepts/loops_and_structures.html) and use the configuration dialog box that appears to specify the simulation instance, sensors, and actuators you want to control.

You can right-click the Simulator Assistant and select **Convert to SubVI** to convert the Simulator Assistant to a subVI. The subVI displays the VIs from the [Simulator](../lvrobovi/simulator_pal.html) palette and sensors and actuator drivers for the simulation program. You can use this subVI to extend the robotics simulator architecture.

|  | Caution You cannot revert the subVI you convert from the Simulator Assistant back to the Simulator Assistant. |
| --- | --- |

Refer to the InvertPendulum.lvproj in the labview\examples\robotics\Simulator\InvertPendulum directory for an example of programming simulation applications using the Simulator Assistant.

You might find it useful to organize simulation programs in [LabVIEW projects](robo_sim_overview.html#proj_parts). Projects group files and allow you to deploy them to hardware. If you use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to create a simulation scene, the wizard automatically generates a project that includes a master VI. You can add additional VIs and files to the same project. If you use the [Offline Configuration](../lvrobovi/simulator_config_pal.html) VIs to create the scene, you do not need to develop the simulation VIs in a LabVIEW project.

#### Examples of Typical Simulation VIs

The following block diagram shows a simple example of a master VI in a simulation program. In this example, the code between the [Start Simulator Service](../lvrobovi/sim_start_service.html) and [Stop Simulator Service](../lvrobovi/sim_stop_service.html) VIs directs a simulated robot to travel through the environment in a straight line at the velocity the **Desired Robot Velocity** control specifies.

[IMAGE alt='image' src='loc_eps_sim_ex1.gif']

|  | VIs from the Simulator palette start and stop the simulator. |
| --- | --- |
|  | VIs from the Device I/O with Simulation palette communicate with simulated actuators on the robot. |
|  | The Get Simulator Reference VI returns a reference to the robot body in the simulation scene, using the robot ID to identify the correct robot. |
|  | An LVODE property reads the angular velocity of the robot body referenced by the Get Simulator Reference VI. The Angular Velocity indicator displays the values on the front panel. |
|  | LabVIEW code sets the motor speeds at which to move the robot. |

|  | Note To simulate a Starter Kit robot, you also can use the Starter Kit VIs to control the robot. |
| --- | --- |

Refer to the Simulated iRobot.lvproj in the labview\examples\robotics\Simulator\iRobot Create directory for an example of programming simulation applications.

Refer to the Robot Balance.lvproj in the labview\examples\robotics\Simulator\Robot Balance directory for an example of programming simulation applications.

#### Starting the Simulator

To begin creating the master VI in a simulation program, add the [Start Simulator Service](../lvrobovi/sim_start_service.html) and [Stop Simulator Service](../lvrobovi/sim_stop_service.html) VIs to the block diagram. The Start Simulator Service VI starts the simulator and initializes the simulation scene defined in the manifest file you wire to the **manifest file** input of the VI.

##### Timing in the Simulator

When you start a simulation with the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI, you must specify a value for the **step size (ms)** input. The step size in a simulation defines the amount of time that elapses in the simulation environment between updates the simulator makes to physical properties in the simulation. Large step sizes result in less accurate real-world behavior. Smaller step sizes result in a simulation that more accurately models real-world behavior, but they require more processor resources. National Instruments recommends step sizes of 5 to 20 ms.

#### Controlling Specific Components in the Simulation

After you start the simulator with the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI, use structures, VIs, functions, and other LabVIEW nodes to control the simulation. An important part of the master VI is manipulating components in the simulation scene. The simulator pairs components you define in a [manifest file](robo_sim_overview.html#proj_parts) with LabVIEW code you write to manipulate those components.

The process you use to manipulate a component depends on the type of the component.

##### Manipulating Robots, the Environment, and Obstacles

In simulation VIs, you manipulate robots, the environment, and obstacles with [LVODE properties and methods](../lvroboprop/lvode_classes.html). The following list contains examples of how you can use these properties and methods to get and set attributes of components and perform actions on the components:

- Set the force that gravity applies in the environment.
- Read the velocity at which a robot travels.
- Change the position of an obstacle in the environment.

Complete the following steps to manipulate a component on the block diagram.

1. Use the Get Simulator Reference VI to obtain a reference to a component in the manifest file. If you use an instance of the Get Simulator Reference polymorphic VI that requires you to specify a component ID, find the ID and wire it to the VI.
2. Wire the output reference from the VI to the reference input on a Property Node or Invoke Node .
3. Select from the available LVODE properties and methods to specify how you want to manipulate the component.

The following block diagram shows an example of reading data from a component.

[IMAGE alt='image' src='loc_bd_sim_ex2.gif']

When you access components through [Property Nodes](/csh?topicname=glang/property_node.html) and [Invoke Nodes](/csh?topicname=glang/invoke_node.html), you can control the components programmatically at run time. For example, you can set the velocity at which a robot travels by passing values to a Property Node on the block diagram through a [user interface](#ui).

##### Communicating with Simulated Sensors

Use [Device I/O with Simulation](../lvrobovi/robo_simdrivers_pal.html) drivers in a simulation application to [communicate with simulated sensors and actuators](robo_prog_sensors.html#haiol). The drivers on the Device I/O with Simulation palette are organized like traditional LabVIEW drivers. However, these drivers allow you to communicate with both real and simulated devices.

When you initialize communication with a simulated sensor or actuator, you must [find and specify the component ID](robo_sim_reading.html) of the device with which you want to communicate.

#### Designing a User Interface

The front panel of the master simulation VI serves as the user interface if you want to manually control any parameters at run time or display values from the scene. [Add controls to the front panel](/csh?topicname=lvconcepts/fp_controls_indicators.html) to pass values into the simulation. Add indicators to display values from the simulation on the front panel. For example, you might add a numeric control to the front panel that allows you to adjust the speed at which you want a robot to travel while the simulation runs.

If you use the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to generate a simulation project, the master VI in the project contains a **ManifestFile** control that identifies the manifest file the wizard created. When you run the master VI, the manifest file must be located in the same directory as the .lvproj file.

##### Displaying the Simulation Scene on the Front Panel

When you run the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI, the simulation displays in a [3D picture control](/csh?topicname=lvconcepts/3d_pic_control.html) within a new window by default. Complete the following steps to display the simulation on the front panel of a VI rather than in a new window.

1. Add a 3D picture control to the front panel.
2. Right-click the 3D picture control and select Create»Reference from the shortcut menu to create a reference to the control on the block diagram.
3. Wire the 3D picture control reference to the 3D Picture Refnum input of the Start Simulator Service VI. If the 3D picture control is on the front panel of a subVI, you must pass the reference out of the subVI and onto the block diagram of the master VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_reading.html language=enus -->
## TOPIC 00025: Reading and Modifying Properties of Simulation Components (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_reading.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_reading.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Reading and Modifying Properties of Simulation Components (Robotics Module)

After you [create a robotics simulation scene](robo_sim_creating.html) in a [manifest file](robo_sim_overview.html#framework), you might want to read or modify the properties of a component in the scene for the following reasons:

- To find the unique ID for a component in order to interact with it on the block diagram .
- To modify properties of a component, such as the mass of a robot.

Use one of the following procedures to read from or modify properties of components.

- If you created the simulation scene in the Robotics Environment Simulator Wizard , right-click the simulation target ( ) in the Project Explorer window and select Properties from the shortcut menu to launch the wizard. Use the Properties table at the bottom left of the wizard to view IDs of components you select and modify their properties. 
 
 [IMAGE alt='image' src='tip.gif']
**Tip** You also can open the [ID list file](../lvrobogsm/robo_sim_overview.html#framework) to view the IDs of components in the simulation scene you create.
- If the manifest file for the simulation scene is not in a LabVIEW simulation project , you can manually read and modify properties of components defined in the manifest file. Use the Load Simulation Instance VI with the properties available in the Property Node (Simulator Engine) to read from the file, as shown in the following block diagram. 
 
 [IMAGE alt='image' src='loc_bd_read_manifest.gif'] 
 
 You also can read the contents of a manifest file, use a Property Node (Simulator Engine) to overwrite the properties of a component with new values, and then save the updated definition for the simulation scene in the manifest file. Right-click the property and select Change To Read or Change To Write from the shortcut menu to change the operation of the property.

|  | Note The robotics simulator returns component properties in SI units and SI-derived units. Use the same units when you define component properties. |
| --- | --- |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sim_viewing.html language=enus -->
## TOPIC 00026: Viewing a Robotics Simulation (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sim_viewing.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sim_viewing.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Viewing a Robotics Simulation (Robotics Module)

You can run a [simulation program](../lvrobogsm/robo_sim_programming.html) in the [robotics simulator](../lvrobogsm/robo_sim_overview.html) to render the simulation scene in a [3D picture control](/csh?topicname=lvconcepts/3d_pic_control.html) and view the interactions of components within the environment. Complete the following steps to run and view a simulation.

1. Open the master simulation VI that starts the simulator . If you used the Robotics Environment Simulator Wizard to create the simulation scene, the master VI is the top-level VI under the simulator item ( ) in the Project Explorer window.
2. On the block diagram, make sure the path to the manifest file whose contents you want to simulate is wired to the manifest file input of the Start Simulator Service VI.
3. Run the VI. The simulation displays and begins running in a new window.
 [IMAGE alt='image' src='note.gif']
**Note** If you did not [add code to control components in the simulator](../lvrobogsm/robo_sim_programming.html), the simulator shows the same static scene you designed.
4. Stop the simulation.

The following table lists actions you can perform to customize your view of the simulation within the 3D picture control.

| Action | Shortcut/Movement |
| --- | --- |
| Move the camera around the scene. | Click and drag the environment. |
| Zoom in and out of the 3D scene. | Hold <Shift>, and then click and drag in the 3D scene. |
| Reposition the environment within the scene. | Hold <Ctrl>, and then click and drag the environment. |

You also can [display the simulation scene on the front panel](../lvrobogsm/robo_sim_programming.html#display_sim_fp) of a VI.

To change the properties of a component in the simulation scene, such as the mass of a robot, [edit the definition of the component](../lvrobogsm/robo_sim_reading.html) in the manifest file.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_skit_advanced.html language=enus -->
## TOPIC 00027: Modifying Connections on the Starter Kit FPGA (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_skit_advanced.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_skit_advanced.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Modifying Connections on the Starter Kit FPGA (Robotics Module)

The Single-Board RIO in the [Robotics Starter Kit](robo_skit_overview.html) allows access to various analog and digital I/O on the FPGA. You can connect new devices to the FPGA to extend the functionality of the robot or change the default connections of the robot drive motors, distance sensor, and sensor servo. When you add or change connections on the FPGA, the [methods you can use to program the FPGA](robo_skit_programming.html) vary according to the changes you make.

|  | Note Refer to the user guide for the Single-Board RIO on your robot for dimensions, pinouts, and specifications. You can find the user guide and other resources in the National Instruments Product Manuals Library at ni.com/manuals. |
| --- | --- |

#### Connecting a New Device to the FPGA

If you connect a new device to the FPGA, you can use the [Direct Input and Output](../lvrobovi/skit_direct_io_pal.html) VIs to read from or write to certain analog and digital lines without directly programming the FPGA. However, if you want to connect the device to I/O the VIs do not support, you must [write an FPGA VI](/csh?topicname=lvfpgaconcepts/fpgaappdev.html) to access that device.

#### Changing Connections of Existing Devices

If you change the I/O to which the robot drive motors, distance sensor, or sensor servo connect by default, the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs cannot access them anymore because the expected I/O becomes invalid. Instead, you must [write an FPGA VI to communicate with the FPGA I/O and RT host VI, and you must compile and download a new FPGA bitfile](/csh?topicname=lvfpgaconcepts/fpgaappdev.html).

|  | Caution Incorrectly modifying connections on the FPGA can damage the device. Refer to the user guide for the Single-Board RIO on your robot for information about safely working with connections on the device. |
| --- | --- |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_skit_overview.html language=enus -->
## TOPIC 00028: LabVIEW Robotics Starter Kit (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_skit_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_skit_overview.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### LabVIEW Robotics Starter Kit (Robotics Module)

The NI LabVIEW Robotics Starter Kit includes a robot that runs LabVIEW Robotics software on NI reconfigurable I/O (RIO) hardware. You can use the robot and hardware to prototype and deploy autonomous applications. National Instruments has produced two versions of the Robotics Starter Kit robot, as shown in the following table.

|  |  |
| --- | --- |
| Starter Kit 1.0 with NI sbRIO-9631 | Starter Kit 2.0 with NI sbRIO-9632 |

On both robots, the Single-Board RIO (sbRIO) controller, mounted on top of the robot base, includes a real-time processor and Field-Programmable Gate Array (FPGA) on a single board. By default, the FPGA has a sensor and motors wired to digital I/O: a Parallax PING))) ultrasonic distance sensor, a servo motor on which the sensor is mounted, and two DC drive motors. You can expand the built-in analog and digital I/O using C Series modules.

Refer to the National Instruments Web site for more information about the LabVIEW Robotics Starter Kit.

#### Setting up the Starter Kit Robot

Refer to the printed *Quick Start Guide* included in the Robotics Starter Kit for information about setting up the Starter Kit robot for the first time. The *Quick Start Guide* provides instructions for wiring the robot, downloading software to the robot, testing the sensor and motors, and so on.

##### Required Software for Using the Starter Kit Robot

The Robotics Starter Kit includes a DVD with the LabVIEW Development System and the following LabVIEW add-ons. You must use the media that shipped with your purchase to install all the add-ons on the development computer before you can program a Starter Kit robot.

- LabVIEW Real-Time Module
- LabVIEW FPGA Module
- LabVIEW Robotics Module
- NI-RIO drivers

#### Programming the Starter Kit Robot

After the development computer, robot, and sbRIO are set up, [create a LabVIEW project that contains the Starter Kit hardware targets](../lvrobogsm/robo_project_creating.html). Refer to the [instructions for programming a Starter Kit robot](../lvrobogsm/robo_skit_programming.html) for more information about controlling the robot in LabVIEW.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_skit_programming.html language=enus -->
## TOPIC 00029: Programming a Starter Kit Robot (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_skit_programming.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_skit_programming.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Programming a Starter Kit Robot (Robotics Module)

When you [set up the Robotics Starter Kit robot](robo_skit_overview.html#setup), the printed *Quick Start Guide* in the kit instructs you to use the [Robotics Project Wizard](../lvrobodialog/robo_proj_wizard.html) to create and deploy a ready-to-run application to the robot. If you want to program the robot to behave differently, you can modify the VIs in the [LabVIEW project](../lvrobogsm/robo_project_overview.html) the wizard creates or [create a new project for the Starter Kit robot](../lvrobogsm/robo_project_creating.html).

|  | Note You must install all software on the LabVIEW Robotics Starter Kit DVD before you can use the Starter Kit VIs with a real Starter Kit robot. |
| --- | --- |

#### Ways to Program the Starter Kit Robot

An important part of programming the Starter Kit robot is communicating with the FPGA on the Single-Board RIO (sbRIO) to control the motors and distance sensor. When you want to program the FPGA on National Instruments RIO hardware targets, such as the sbRIO on the robot, you typically must develop a real-time application with [FPGA components](/csh?topicname=lvfpgaconcepts/fpgaappdev.html) that directly interface with FPGA I/O. With the Robotics Starter Kit, instead of writing an FPGA VI to directly control the FPGA, you can use the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to control the motors and sensor wired to the FPGA. The following table describes how the two methods for communicating with the FPGA on the robot differ.

| Programming method | Writing an FPGA VI | Using the Starter Kit VIs in a real-time host VI |
| --- | --- | --- |
| LabVIEW projectcomponents |  |  |
| API to use in RT host VI to communicate with FPGA | Open FPGA VI Reference function Read/Write Control functions Close FPGA VI Reference function | Starter Kit VIs |

|  | Note If you modify or expand the I/O on the FPGA, you might need to write an FPGA VI instead of using the Starter Kit VIs. |
| --- | --- |

#### Communicating with the FPGA

The [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs communicate with the FPGA on the robot similarly to how sensor drivers communicate with sensors. For example, as described in the following sections, typical Starter Kit applications start a communication session with the FPGA, read from and write to the FPGA, and then close the communication session.

|  | Note (Starter Kit 2.0) You must configure the sbRIO-9632 chassis to use the LabVIEW FPGA Interface programming mode or the Starter Kit VIs do not run on the sbRIO. To configure the programming mode, right-click the sbRIO chassis in the Project Explorer window and select Properties from the shortcut menu to display the Single-Board RIO Chassis Properties dialog box. Select LabVIEW FPGA Interface in the Programming Mode section. |
| --- | --- |

##### Initializing Communication

Use the initialization VI appropriate for your robot—the [Initialize Starter Kit 1.0 (sbRIO-9631)](../lvrobovi/skit_init_1.html) VI or the [Initialize Starter Kit 2.0 (sbRIO-9632)](../lvrobovi/skit_init_2.html) VI—to begin the communication session with the FPGA.

##### Reading from and Writing to the FPGA

The Starter Kit initialization VIs return a reference to the interface with the FPGA, which you use throughout the host VI to access I/O on the FPGA. For example, you can wire the reference to the [Write DC Motor Velocity Setpoints](../lvrobovi/skit_write_motor_setpts.html) VI to write the velocities at which you want the DC drive motors to move.

The Starter Kit robot is designed to move autonomously, without direct control by an operator. To program the robot to operate continuously, place code to control the robot inside a loop that runs and then repeats itself. For example, if you want the robot to continuously move forward until the distance finder detects an obstacle, place a loop that reads from the distance sensor and writes velocities to the drive motors based on the presence of obstacles. You also might want to program the sensor servo to pan back and forth so the distance finder scans a wider radius around the robot. In this example, you can use a loop to supply a new angle to the [Write Sensor Servo Angle](../lvrobovi/skit_write_servo_angle.html) VI on each new loop iteration to implement a panning motion. Use [shift registers](/csh?topicname=lvconcepts/shift_registers_concepts.html) to pass values and the FPGA interface reference between loop iterations.

|  | Tip Use a Timed Loop to implement precise control of timing in the loop, such as the period of loop iterations and the priority at which to run the code in the loop relative to other block diagram code. |
| --- | --- |

Refer to the Starter Kit 1.0.lvproj in the labview\examples\robotics\Starter Kit 1.0 directory for an example of using the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to control the Starter Kit 1.0 robot.

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to control the Starter Kit 2.0 robot.

##### Closing Communication

Use the [Close Starter Kit](../lvrobovi/skit_write_servo_angle.html) VI to end the communication session with the FPGA. When this VI ends the communication session, the drive motors, sensor, and sensor servo stop moving.

#### Calculating Values to Supply to the Starter Kit VIs

As mentioned previously, the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs are designed to communicate with the sensor and motors wired to the FPGA on the robot. However, an important part of controlling the robot is calculating values to write to those devices. The following sections describe methods for implementing code that does not directly relate to communication with the FPGA.

##### Implementing Steering for a Robot

In a Starter Kit application, you might want to control the speed of the robot by specifying one overall velocity value. However, because the left and right drive motors on the robot connect to separate lines on the FPGA, the [Write DC Motor Velocity Setpoints](../lvrobovi/skit_write_motor_setpts.html) VI requires you to write the desired velocity for each motor. You can use the [Steering](../lvrobovi/steering_pal.html) VIs to convert between an overall velocity value and individual motor velocities and perform other functions related to controlling the steering of the robot.

To integrate the [Steering](../lvrobovi/steering_pal.html) VIs with a Starter Kit application, use the [Create Starter Kit Steering Frame 1.0](../lvrobovi/skit_create_1_frame.html) VI or [Create Starter Kit Steering Frame 2.0](../lvrobovi/skit_create_2_frame.html) VI from the [Starter Kit](../lvrobovi/starter_kit_pal.html) palette to generate a steering frame object for the robot. The object contains information required to calculate velocity values, such as the types and locations of wheels on the robot. Use the object with the Steering VIs to calculate appropriate velocities for the motors. The following block diagram shows an example of integrating the Steering VIs with the Starter Kit VIs to drive a robot.

[IMAGE alt='image' src='loc_bd_skit_steering.gif']

##### Useful LabVIEW VIs and Functions

To complement the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs, use other LabVIEW VIs and functions to calculate values you want to write to the sensors and actuators on the robot. The [Angle](/csh?topicname=gmath/angle_vis.html) VIs and the [Scaling](/csh?topicname=lvinstio/scaling_palette.html) VIs allow you to convert between units commonly used in robotics applications. For example, you can use the [Degrees to Radians](/csh?topicname=lvinstio/degrees_to_radians.html) VI to convert angles expressed in degrees to angles expressed in radians.

The [Robotics](../lvrobovi/robotics_pal.html) palette provides other VIs for designing robotics-related algorithms.

#### Accessing Unused I/O on the FPGA

Although the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs abstract the interface between VIs and the FPGA, you still can access certain unused analog and digital I/O on the FPGA. Use the [Direct Input and Output](../lvrobovi/skit_direct_io_pal.html) VIs with the reference to the FPGA interface to read from or write to these analog and digital lines on the FPGA. Like the Starter Kit VIs, the Direct Input and Output VIs allow you to interact with the FPGA without writing an FPGA VI.

|  | Note To modify the default configuration of the FPGA or connect devices to I/O lines that the Direct Input and Output VIs do not support, you must write an FPGA VI to access the I/O instead of using the Starter Kit VIs. |
| --- | --- |

#### Simulating a Starter Kit Robot

You can use the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs in an application that [controls a simulated Starter Kit robot](robo_skit_sim.html). Then, you can use the same LabVIEW project and VIs to [deploy the application to the sbRIO](robo_sim_deploying.html) on a real Starter Kit robot.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_skit_sim.html language=enus -->
## TOPIC 00030: Simulating a Starter Kit Robot (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_skit_sim.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_skit_sim.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Simulating a Starter Kit Robot (Robotics Module)

You can [simulate](robo_sim_overview.html) a [Robotics Starter Kit robot](robo_skit_overview.html) without depending on an actual robot.

#### Creating a Starter Kit Simulation Project

A simulation application for a Starter Kit robot is organized in a LabVIEW project with the same types of [simulation-related files](robo_sim_overview.html#proj_parts) as other robotics simulation applications. Use the following methods to generate a LabVIEW project for simulating a Starter Kit robot:

- To simulate a robot running an application and deploy the application to a real robot, use the Robotics Project Wizard to create a new Robotics Starter Kit project. This wizard generates a project that contains both a simulator target and the Single-Board RIO target on the real robot. This wizard places the simulated robot in a predefined simulation scene, which you can modify later.
- To simulate a robot when you do not want to deploy the application to a real robot, use the Robotics Environment Simulator Wizard to create a new Robotics Environment Simulator project. This wizard allows you to design a simulation environment that includes the Starter Kit robot and any other components you want to simulate.

Both wizards save a manifest file, which defines the simulation scene and components in the scene, in the LabVIEW project under the simulator target ([IMAGE alt='image' src='noloc_env_sim_glyph.gif']). After you create the LabVIEW project, you can launch the [Robotics Environment Simulator Wizard](../lvrobodialog/robo_sim_wizard.html) to [modify components in the simulation scene](robo_sim_reading.html), such as the environment, and save the changes in the manifest file. The Robot Environment Simulator reads the manifest file to display the simulation scene.

#### Writing a Starter Kit Simulation Application

After you create a project with a simulator target, you can use the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to communicate with simulated versions of the Starter Kit robot similar to how you [interface with a real robot](../lvrobogsm/robo_skit_programming.html). To begin the application, use the appropriate initialization VI for your simulation application—the [Initialize Starter Kit 1.0](../lvrobovi/skit_init_sim_1.html) VI or the [Initialize Starter Kit 2.0](../lvrobovi/skit_init_sim_2.html) VI—with the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI.

After you start the simulator, [write a VI to control the simulation](robo_sim_programming.html). With the exception of the initialization VI, you can use all other [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs in applications for real or simulated robots. The ability to reuse these VIs is useful because you can design and test a simulated Starter Kit application and then use the same LabVIEW project to deploy the same application to a real robot.

When you finish simulating the robot application, you can [prepare the project and files to be deployed](../lvrobogsm/robo_sim_deploying.html) to a real robot.

Refer to the Starter Kit 1.0.lvproj in the labview\examples\robotics\Starter Kit 1.0 directory for an example of using the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to simulate the Starter Kit 1.0 robot.

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the [Starter Kit](../lvrobovi/starter_kit_pal.html) VIs to simulate the Starter Kit 2.0 robot.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_steering.html language=enus -->
## TOPIC 00031: Driving Wheeled Robots (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_steering.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_steering.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Driving Wheeled Robots (Robotics Module)

To drive a wheeled robot at a certain velocity and direction, you first must design a representation of the robot steering frame that defines properties of the frame and its wheels. After you design the steering frame representation on the block diagram, use that representation to implement motor control by calculating and converting between robot velocity and wheel velocities and connecting to motors that drive wheels.

The following sections describe how to manually and programmatically design a steering frame.

#### Manually Designing a Steering Frame

You can use the [Configure Steering Frame](../lvrobovi/config_steering_frame.html) Express VI to design a steering frame in an interactive dialog box. This Express VI returns the steering frame object, which you interact with on the block diagram using [Steering](../lvrobovi/steering_pal.html) VIs that allow you to control wheel and frame velocity.

Refer to the Configurable Steering.lvproj in the labview\examples\robotics\Steering\Configurable Steering directory for an example of manually designing and then steering a wheeled robot.

#### Programmatically Designing a Steering Frame

When you programmatically design a steering frame, you typically write code similar to the following block diagram.

[IMAGE alt='image' src='loc_bd_create_steering.gif']

The previous block diagram performs the following tasks to generate a steering frame object when the VI runs:

- Uses the Create Wheel VI to generate four wheel objects with the properties the wheel parameters cluster defines.
- Bundles the wheels together in the format the Create Steering Frame Express VI requires.
- Uses the Mecanum instance of the Create Steering Frame Express VI to generate a Mecanum steering frame object with the four wheels at the locations defined by the wheel separation width and wheel separation length inputs.

Refer to the Mecanum Steering.lvproj in the labview\examples\robotics\Steering\Mecanum Steering directory for an example of programmatically designing and steering a wheeled robot.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_sys_sensors.html language=enus -->
## TOPIC 00032: Connecting to USB Devices (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_sys_sensors.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_sys_sensors.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Connecting to USB Devices (Robotics Module)

Some RT targets have support for onboard [USB](/csh?topicname=lvmeasconcepts/usb_communication.html) hardware. You can connect an external USB Communications Device Class (CDC) ACM device to a USB port of an RT target and then access the device from VIs running on the RT target. To access the device, modify and use existing driver VIs that are configured for serial communication and use [NI-VISA](/csh?topicname=lvmeasconcepts/visa_in_labview.html) to communicate with the device.

Complete the following steps to modify a driver to communicate with a USB device.

1. Connect the external USB device to the USB port of the RT target.
2. Open the initialization driver VI for the device. If you do not have a driver installed for the device, use the NI Instrument Driver Finder to download and install a driver.
3. Right-click the VISA resource name control on the front panel of the initialization driver VI and select Select VISA Class»I/O Session»USB Raw from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** When you modify drivers that are configured for serial communication, you do not need to specify values for serial-specific properties.
4. Clean up the block diagram and save the VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobogsm/robo_vision.html language=enus -->
## TOPIC 00033: Acquiring and Processing Images from Cameras (Robotics Module)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobogsm/robo_vision.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobogsm/robo_vision.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Acquiring and Processing Images from Cameras (Robotics Module)

National Instruments offer various solutions for acquiring and processing images from a camera on a robot. The following list describes a few options you can explore to implement vision-related functionality in a typical LabVIEW robotics application:

- Use a desktop computer, industrial controller, or another target that runs a Windows operating system to perform one of the following tasks:
  - Communicate vision-related commands to a camera on a robot.
  - Acquire images from a camera on a robot wirelessly and process image data offline.
- Use an NI RIO target that connects to a camera, such as an Internet protocol (IP) camera, and perform image acquisition and processing on the target.
- Use an NI Smart Camera to acquire and process images.

After you decide on a hardware implementation, use NI software that integrates vision algorithms with other parts of robotics applications. The NI Vision Acquisition Software provides driver software for acquiring, displaying, logging, and monitoring images from cameras. The NI Vision Development Module includes hundreds of functions for acquiring and processing images from cameras.

Refer to the National Instruments Web site at ni.com/vision for more information about the NI Vision platform, including embedded vision systems, NI Smart Cameras, and vision software.

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_accelerometer_acceleration.html language=enus -->
## TOPIC 00034: Acceleration Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_accelerometer_acceleration.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_accelerometer_acceleration.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Acceleration Property

**Short Name:**Acceleration

**Requires:**Robotics Module

**Class:**
 [Accelerometer Properties](lvode_accelerometer_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the measured acceleration.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_accelerometer_p.html language=enus -->
## TOPIC 00035: Accelerometer Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_accelerometer_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_accelerometer_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Accelerometer Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Sensor](lvode_sensor_p.html) class. View the class [hierarchy](lvode_classes.html).

An accelerometer is a device that measures the proper acceleration of the device. This is not necessarily the same as the coordinate acceleration (change of velocity of the device in space), but is rather the type of acceleration associated with the phenomenon of weight experienced by a test mass that resides in the frame of reference of the accelerometer device.

[Acceleration](lvode_accelerometer_acceleration.html)

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_addtorques.html language=enus -->
## TOPIC 00036: AddTorques Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_addtorques.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_addtorques.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddTorques Method

**Short Name:**AMJAddTorques

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds the torques.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddTorques | noDirection | void |
| torque1 | noDirection | Single-precision, floating-point number |
| torque2 | noDirection | Single-precision, floating-point number |
| torque3 | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_bounce.html language=enus -->
## TOPIC 00037: Axis1:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_cfm.html language=enus -->
## TOPIC 00038: Axis1:CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:CFM Property

**Short Name:**CFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the constraint force mixing (CFM) of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_fmax.html language=enus -->
## TOPIC 00039: Axis1:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fmax of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_fudge_factor.html language=enus -->
## TOPIC 00040: Axis1:Fudge Factor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_fudge_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_fudge_factor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Fudge Factor Property

**Short Name:**FudgeFactor

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fudge factor of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_hi_stop.html language=enus -->
## TOPIC 00041: Axis1:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_lo_stop.html language=enus -->
## TOPIC 00042: Axis1:Lo Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_lo_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_lo_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Lo Stop Property

**Short Name:**LoStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the lo stop of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_stop_cfm.html language=enus -->
## TOPIC 00043: Axis1:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop constraint force mixing (CFM) of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_stop_erp.html language=enus -->
## TOPIC 00044: Axis1:Stop ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_stop_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_stop_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Stop ERP Property

**Short Name:**StopERP

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop error reduction parameter (ERP) of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis1_vel.html language=enus -->
## TOPIC 00045: Axis1:Vel Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis1_vel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis1_vel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Vel Property

**Short Name:**Vel

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the velocity of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_bounce.html language=enus -->
## TOPIC 00046: Axis2:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_cfm.html language=enus -->
## TOPIC 00047: Axis2:CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:CFM Property

**Short Name:**CFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the constraint force mixing (CFM) of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_fmax.html language=enus -->
## TOPIC 00048: Axis2:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fmax of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_fudge_factor.html language=enus -->
## TOPIC 00049: Axis2:Fudge Factor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_fudge_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_fudge_factor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Fudge Factor Property

**Short Name:**FudgeFactor

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fudge factor of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_hi_stop.html language=enus -->
## TOPIC 00050: Axis2:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_lo_stop.html language=enus -->
## TOPIC 00051: Axis2:Lo Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_lo_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_lo_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Lo Stop Property

**Short Name:**LoStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the lo stop of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_stop_cfm.html language=enus -->
## TOPIC 00052: Axis2:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop CFM of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_stop_erp.html language=enus -->
## TOPIC 00053: Axis2:Stop ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_stop_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_stop_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Stop ERP Property

**Short Name:**StopERP

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop error reduction parameter (ERP) of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis2_vel.html language=enus -->
## TOPIC 00054: Axis2:Vel Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis2_vel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis2_vel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Vel Property

**Short Name:**Vel

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the velocity of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_bounce.html language=enus -->
## TOPIC 00055: Axis3:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_cfm.html language=enus -->
## TOPIC 00056: Axis3:CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:CFM Property

**Short Name:**CFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the constraint force mixing (CFM) of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_fmax.html language=enus -->
## TOPIC 00057: Axis3:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fmax of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_fudge_factor.html language=enus -->
## TOPIC 00058: Axis3:Fudge Factor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_fudge_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_fudge_factor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Fudge Factor Property

**Short Name:**FudgeFactor

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fudge factor of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_hi_stop.html language=enus -->
## TOPIC 00059: Axis3:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_lo_stop.html language=enus -->
## TOPIC 00060: Axis3:Lo Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_lo_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_lo_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Lo Stop Property

**Short Name:**LoStop

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the lo stop of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_stop_cfm.html language=enus -->
## TOPIC 00061: Axis3:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop constraint force mixing (CFM) of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_stop_erp.html language=enus -->
## TOPIC 00062: Axis3:Stop ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_stop_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_stop_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Stop ERP Property

**Short Name:**StopERP

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop error reduction parameter (ERP) of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_axis3_vel.html language=enus -->
## TOPIC 00063: Axis3:Vel Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_axis3_vel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_axis3_vel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Vel Property

**Short Name:**Vel

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the velocity of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_getangle.html language=enus -->
## TOPIC 00064: GetAngle Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_getangle.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_getangle.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetAngle Method

**Short Name:**AMJGetAngle

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the angle.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetAngle | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| angle | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_getanglerate.html language=enus -->
## TOPIC 00065: GetAngleRate Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_getanglerate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_getanglerate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetAngleRate Method

**Short Name:**AMJGetAngleRate

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the angle rate.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetAngleRate | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| angleRate | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_getaxis.html language=enus -->
## TOPIC 00066: GetAxis Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_getaxis.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_getaxis.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetAxis Method

**Short Name:**AMJGetAxis

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the axis.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetAxis | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| axis | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_getaxisrel.html language=enus -->
## TOPIC 00067: GetAxisRel Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_getaxisrel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_getaxisrel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetAxisRel Method

**Short Name:**AMJGetAxisRel

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the axis rel.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetAxisRel | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| rel | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_m.html language=enus -->
## TOPIC 00068: AMotorJoint Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AMotorJoint Methods

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_m.html) class. View the class [hierarchy](lvode_classes.html).

- AddTorques
- GetAngle
- GetAngleRate
- GetAxis
- GetAxisRel
- SetAngle
- SetAxis

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_mode.html language=enus -->
## TOPIC 00069: Mode Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_mode.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_mode.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Mode Property

**Short Name:**Mode

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the angular motor mode.

The angular motor mode must be one of the following constants:

- dAMotorUser—The user controls the AMotor axes and joint angle settings. This is the default mode.
- dAMotorEuler—LabVIEW automatically computes the Euler angles and the axis a1. The user must set the AMotor axes correctly. When you initially set this mode, the current relative orientations of the bodies correspond to all Euler angles at zero.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

32-bit signed integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_number_of_axes.html language=enus -->
## TOPIC 00070: Number of Axes Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_number_of_axes.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_number_of_axes.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Number of Axes Property

**Short Name:**NumAxes

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Properties](lvode_amotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the number of angular axes the AMotor controls. This number can have a value between 0, which effectively deactivates the joint, and 3. dAMotorEuler [mode](lvode_amotorjoint_mode.html) automatically sets the value to 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

32-bit signed integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_p.html language=enus -->
## TOPIC 00071: AMotorJoint Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AMotorJoint Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_p.html) class. View the class [hierarchy](lvode_classes.html).

- Axis1:Bounce
- Axis1:CFM
- Axis1:FMax
- Axis1:Fudge Factor
- Axis1:Hi Stop
- Axis1:Lo Stop
- Axis1:Stop CFM
- Axis1:Stop ERP
- Axis1:Vel
- Axis2:Bounce
- Axis2:CFM
- Axis2:FMax
- Axis2:Fudge Factor
- Axis2:Hi Stop
- Axis2:Lo Stop
- Axis2:Stop CFM
- Axis2:Stop ERP
- Axis2:Vel
- Axis3:Bounce
- Axis3:CFM
- Axis3:FMax
- Axis3:Fudge Factor
- Axis3:Hi Stop
- Axis3:Lo Stop
- Axis3:Stop CFM
- Axis3:Stop ERP
- Axis3:Vel
- Mode
- Number of Axes

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_setangle.html language=enus -->
## TOPIC 00072: SetAngle Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_setangle.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_setangle.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### SetAngle Method

**Short Name:**AMJSetAngle

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Sets the angle.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| SetAngle | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| angle | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_amotorjoint_setaxis.html language=enus -->
## TOPIC 00073: SetAxis Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_amotorjoint_setaxis.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_amotorjoint_setaxis.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### SetAxis Method

**Short Name:**AMJSetAxis

**Requires:**Robotics Module

**Class:**
 [AMotorJoint Method](lvode_amotorjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Sets the axis.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| SetAxis | noDirection | void |
| anum | noDirection | Single-precision, floating-point number |
| rel | noDirection | Single-precision, floating-point number |
| axis | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_balljoint_anchor.html language=enus -->
## TOPIC 00074: Anchor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_balljoint_anchor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_balljoint_anchor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Anchor Property

**Short Name:**Anchor

**Requires:**Robotics Module

**Class:**
 [BallJoint Properties](lvode_balljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Sets the position of the joint anchor point. The joint tries to keep this point on each body together.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_balljoint_anchor2.html language=enus -->
## TOPIC 00075: Anchor2 Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_balljoint_anchor2.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_balljoint_anchor2.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Anchor2 Property

**Short Name:**Anchor2

**Requires:**Robotics Module

**Class:**
 [BallJoint Properties](lvode_balljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the position of the joint anchor point. The joint tries to keep this point on each body together.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_balljoint_cfm.html language=enus -->
## TOPIC 00076: CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_balljoint_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_balljoint_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### CFM Property

**Short Name:**CFM

**Requires:**Robotics Module

**Class:**
 [BallJoint Properties](lvode_balljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the constraint force mixing (CFM).

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_balljoint_erp.html language=enus -->
## TOPIC 00077: ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_balljoint_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_balljoint_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### ERP Property

**Short Name:**ERP

**Requires:**Robotics Module

**Class:**
 [BallJoint Properties](lvode_balljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the error reduction parameter (ERP).

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_balljoint_p.html language=enus -->
## TOPIC 00078: BallJoint Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_balljoint_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_balljoint_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### BallJoint Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_p.html) class. View the class [hierarchy](lvode_classes.html).

- Anchor2
- Anchor
- CFM
- ERP

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addforce.html language=enus -->
## TOPIC 00079: AddForce Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addforce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addforce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddForce Method

**Short Name:**BodyAddForce

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Add force to the body.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddForce | noDirection | void |
| force | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addforceatpos.html language=enus -->
## TOPIC 00080: AddForceAtPos Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addforceatpos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addforceatpos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddForceAtPos Method

**Short Name:**BodyAddForceAtPos

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds force to the body on the position.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddForceAtPos | noDirection | void |
| force | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addrelforce.html language=enus -->
## TOPIC 00081: AddRelForce Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addrelforce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addrelforce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddRelForce Method

**Short Name:**BodyAddRelForce

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds force to the body (relative to the body's own frame of reference).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddRelForce | noDirection | void |
| force | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addrelforceatpos.html language=enus -->
## TOPIC 00082: AddRelForceAtPos Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addrelforceatpos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addrelforceatpos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddRelForceAtPos Method

**Short Name:**BodyAddRelForceAtPos

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds force to the body on the position (relative to the body's own frame of reference).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddRelForceAtPos | noDirection | void |
| force | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addreltorque.html language=enus -->
## TOPIC 00083: AddRelTorque Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addreltorque.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addreltorque.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddRelTorque Method

**Short Name:**BodyAddRelTorque

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds torque to the body (relative to the body's own frame of reference).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddRelTorque | noDirection | void |
| torque | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addreltorqueatpos.html language=enus -->
## TOPIC 00084: AddRelTorqueAtPos Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addreltorqueatpos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addreltorqueatpos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddRelTorqueAtPos Method

**Short Name:**BodyAddRelTorqueAtPos

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds torque to the body on the position (relative to the body's own frame of reference).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddRelTorqueAtPos | noDirection | void |
| torque | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addtorque.html language=enus -->
## TOPIC 00085: AddTorque Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addtorque.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addtorque.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddTorque Method

**Short Name:**BodyAddTorque

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds torque to the body.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddTorque | noDirection | void |
| torque | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_addtorqueatpos.html language=enus -->
## TOPIC 00086: AddTorqueAtPos Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_addtorqueatpos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_addtorqueatpos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddTorqueAtPos Method

**Short Name:**BodyAddTorqueAtPos

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds torque to the body on the position.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddTorqueAtPos | noDirection | void |
| torque | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_angulardamping.html language=enus -->
## TOPIC 00087: AngularDamping Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_angulardamping.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_angulardamping.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AngularDamping Property

**Short Name:**AngularDamping

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the angular damping.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_autodisableangularthreshold.html language=enus -->
## TOPIC 00088: AutoDisableAngularThreshold Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_autodisableangularthreshold.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_autodisableangularthreshold.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AutoDisableAngularThreshold Property

**Short Name:**AutoDisableAngularThreshold

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the auto-disable angular threshold for the body.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_autodisableflag.html language=enus -->
## TOPIC 00089: AutoDisableFlag Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_autodisableflag.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_autodisableflag.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AutoDisableFlag Property

**Short Name:**AutoDisableFlag

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the auto-disable flag for the body.

#### Data Type

32-bit signed integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_disable.html language=enus -->
## TOPIC 00090: Disable Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_disable.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_disable.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Disable Method

**Short Name:**BodyDisable

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Disables a body.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Disable | noDirection | void |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_finite_rotation_axis.html language=enus -->
## TOPIC 00091: Finite Rotation Axis Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_finite_rotation_axis.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_finite_rotation_axis.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Finite Rotation Axis Property

**Short Name:**FiniteRotationAxis

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the current finite rotation axis of the body.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_getnumjoints.html language=enus -->
## TOPIC 00092: GetNumJoints Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_getnumjoints.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_getnumjoints.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetNumJoints Method

**Short Name:**BodyGetNumJoints

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the number of joints attached to the body.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetNumJoints | noDirection | void |
| result | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_getposrelpoint.html language=enus -->
## TOPIC 00093: GetPosRelPoint Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_getposrelpoint.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_getposrelpoint.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetPosRelPoint Method

**Short Name:**BodyGetPosRelPoint

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Takes a point in global coordinates and returns the point's position in body-relative coordinates.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetPosRelPoint | noDirection | void |
| point | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_getrelpointpos.html language=enus -->
## TOPIC 00094: GetRelPointPos Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_getrelpointpos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_getrelpointpos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetRelPointPos Method

**Short Name:**BodyGetRelPointPos

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Takes a point on a body in body relative coordinates and returns that point's position in global coordinates.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetRelPointPos | noDirection | void |
| point | In and out | 2D array of single-precision, floating-point numbers |
| position | In and out | 2D array of single-precision, floating-point numbers |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_id.html language=enus -->
## TOPIC 00095: ID Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_id.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### ID Property

**Short Name:**ID

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

LVODE ID.

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_iskinematic.html language=enus -->
## TOPIC 00096: IsKinematic Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_iskinematic.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_iskinematic.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### IsKinematic Method

**Short Name:**BodyIsKinematic

**Requires:**Robotics Module

**Class:**
 [Body Method](lvode_body_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Tests if a body is in the kinematic state.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| IsKinematic | noDirection | void |
| result | noDirection | Boolean |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_lineardamping.html language=enus -->
## TOPIC 00097: LinearDamping Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_lineardamping.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_lineardamping.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### LinearDamping Property

**Short Name:**LinearDamping

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the linear damping.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_m.html language=enus -->
## TOPIC 00098: Body Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Body Methods

**Requires:**Robotics Module

**Class:**
 [LVODE properties and methods](lvode_classes.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Bodies are the basic element of simulation in the robotics simulator, and every body belongs to a [world](lvode_world_p.html). A rigid body has various properties from the point of view of the simulation. Some properties, such as position, velocity, and orientation change over time, while some properties, such as mass and the inertia matrix, are usually constant over time.

Use these methods to construct different types of mass for a body.

- AddForce
- AddForceAtPos
- AddRelForce
- AddRelForceAtPos
- AddRelTorque
- AddRelTorqueAtPos
- AddTorque
- AddTorqueAtPos
- Disable
- Enable
- GetJoint
- GetNumJoints
- GetPointVel
- GetPosRelPoint
- GetRelPointPos
- GetRelPointVel
- IsConnectedTo
- IsEnabled
- IsKinematic
- SetDampingDefaults
- SetDynamic
- SetKinematic
- VectorFromWorld
- VectorToWorld

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_mass.html language=enus -->
## TOPIC 00099: Mass Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_mass.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_mass.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Mass Property

**Short Name:**Mass

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets body mass. Each body has a mass object property.

#### Data Type

Reference number (refnum)

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_position.html language=enus -->
## TOPIC 00100: Position Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_position.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_position.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Position Property

**Short Name:**Position

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the global position of the body.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_rotation.html language=enus -->
## TOPIC 00101: Rotation Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_rotation.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_rotation.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Property

**Short Name:**Rotation

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the rotation matrix of the body.

#### Data Type

2D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_body_torque.html language=enus -->
## TOPIC 00102: Torque Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_body_torque.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_body_torque.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Torque Property

**Short Name:**Torque

**Requires:**Robotics Module

**Class:**
 [Body Properties](lvode_body_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the current accumulated torque vector.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_bumper_result.html language=enus -->
## TOPIC 00103: result Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_bumper_result.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_bumper_result.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### result Property

**Short Name:**result

**Requires:**Robotics Module

**Class:**
 [Bumper Properties](lvode_bumper_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns a value of TRUE if the sensor collides with another object.

#### Data Type

Boolean

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_camera_p.html language=enus -->
## TOPIC 00104: Camera Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_camera_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_camera_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Camera Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Sensor](lvode_sensor_p.html) class. View the class [hierarchy](lvode_classes.html).

- Position
- Target
- UpDirection

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_camera_position.html language=enus -->
## TOPIC 00105: Position Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_camera_position.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_camera_position.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Position Property

**Short Name:**Position

**Requires:**Robotics Module

**Class:**
 [Camera Properties](lvode_camera_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the position of the camera.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_camera_updirection.html language=enus -->
## TOPIC 00106: UpDirection Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_camera_updirection.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_camera_updirection.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### UpDirection Property

**Short Name:**UpDirection

**Requires:**Robotics Module

**Class:**
 [Camera Properties](lvode_camera_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the up direction of the camera.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_distancesensor_distance.html language=enus -->
## TOPIC 00107: Distance Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_distancesensor_distance.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_distancesensor_distance.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Distance Property

**Short Name:**Distance

**Requires:**Robotics Module

**Class:**
 [DistanceSensor Properties](lvode_distancesensor_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the distance, in meters, to the nearest object at a particular scanning direction. This type of sensor shoots a ray on a direction and returns the distance to nearest object.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_distancesensor_low_range.html language=enus -->
## TOPIC 00108: Low Range Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_distancesensor_low_range.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_distancesensor_low_range.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Low Range Property

**Short Name:**LowRange

**Requires:**Robotics Module

**Class:**
 [DistanceSensor Properties](lvode_distancesensor_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the low range at which this sensor detects obstacles. You cannot modify this value after initializing communication with the sensor.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_fixedjoint_set.html language=enus -->
## TOPIC 00109: Set Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_fixedjoint_set.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_fixedjoint_set.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Set Method

**Short Name:**FJSet

**Requires:**Robotics Module

**Class:**
 [FixedJoint Method](lvode_fixedjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Call this method on the fixed joint after you attach the joint.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Set | noDirection | void |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_forcesensor_force.html language=enus -->
## TOPIC 00110: Force Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_forcesensor_force.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_forcesensor_force.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Force Property

**Short Name:**Force

**Requires:**Robotics Module

**Class:**
 [ForceSensor Properties](lvode_forcesensor_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the measured acceleration.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_category_bits.html language=enus -->
## TOPIC 00111: Category Bits Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_category_bits.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_category_bits.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Category Bits Property

**Short Name:**CategoryBits

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the category bits of a geometrical figure.

#### Data Type

32-bit unsigned integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_collide_bits.html language=enus -->
## TOPIC 00112: Collide Bits Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_collide_bits.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_collide_bits.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Collide Bits Property

**Short Name:**CollideBits

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the collide bits of a geometrical figure.

#### Data Type

32-bit unsigned integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_id.html language=enus -->
## TOPIC 00113: ID Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_id.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### ID Property

**Short Name:**ID

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the LVODE ID of a geometrical figure.

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_m.html language=enus -->
## TOPIC 00114: Geom Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Geom Methods

**Class:**
 [LVODE properties and methods](lvode_classes.html)

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Geometry objects, or geoms, are the basics objects in the collision system. A geom can represent a single rigid shape, such as a sphere or box, or a group of geoms, referred to as a space.
Geoms can be placeable or non-placeable. A placeable geom has a position vector and a 3 × 3 rotation matrix that you can change during the simulation. Non-placeable geoms might represent some static feature of the environment that you cannot move, so they do not have a position vector or rotation matrix associated with them. Spaces are non-placeable geoms because, although each contained geom can have its own position and orientation, it does not make sense for the space itself to have a position and orientation.

- Collide
- IsSpace

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_surface_motion2.html language=enus -->
## TOPIC 00115: surface:motion2 Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_surface_motion2.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_surface_motion2.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### surface:motion2 Property

**Short Name:**motion2

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets surface velocity in friction direction 2.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_surface_slip2.html language=enus -->
## TOPIC 00116: surface:slip2 Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_surface_slip2.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_surface_slip2.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### surface:slip2 Property

**Short Name:**slip2

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the coefficients of force-dependent-slip (FDS) for friction direction 2.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_surface_soft_cfm.html language=enus -->
## TOPIC 00117: surface:soft CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_surface_soft_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_surface_soft_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### surface:soft CFM Property

**Short Name:**softCFM

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the contact normal softness parameter.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_geom_type.html language=enus -->
## TOPIC 00118: Type Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_geom_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_geom_type.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Type Property

**Short Name:**Type

**Requires:**Robotics Module

**Class:**
 [Geom Properties](lvode_geom_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the type of geometrical figure.

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_gps_altitude.html language=enus -->
## TOPIC 00119: Altitude Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_gps_altitude.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_gps_altitude.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Altitude Property

**Short Name:**Altitude

**Requires:**Robotics Module

**Class:**
 [GPS Properties](lvode_gps_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the current z-axis position, in meters. This value represents the altitude above mean sea level (m).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_gps_ground_speed.html language=enus -->
## TOPIC 00120: Ground Speed Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_gps_ground_speed.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_gps_ground_speed.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Ground Speed Property

**Short Name:**GroundSpeed

**Requires:**Robotics Module

**Class:**
 [GPS Properties](lvode_gps_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the current moving speed, in knots, of the sensor.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_gps_latitude.html language=enus -->
## TOPIC 00121: Latitude Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_gps_latitude.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_gps_latitude.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Latitude Property

**Short Name:**Latitude

**Requires:**Robotics Module

**Class:**
 [GPS Properties](lvode_gps_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the current y-axis angle, in degrees. Convert this value to the standard latitude value.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_gps_longitude.html language=enus -->
## TOPIC 00122: Longitude Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_gps_longitude.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_gps_longitude.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Longitude Property

**Short Name:**Longitude

**Requires:**Robotics Module

**Class:**
 [GPS Properties](lvode_gps_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the current x-axis angle, in degrees. Convert this angle to the standard longitude value.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_anchor.html language=enus -->
## TOPIC 00123: Anchor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_anchor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_anchor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Anchor Property

**Short Name:**Anchor

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the position of the joint anchor point in the form of (x, y, z). The joint tries to keep this point on each body together.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_angle1.html language=enus -->
## TOPIC 00124: Angle1 Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_angle1.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_angle1.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle1 Property

**Short Name:**Angle

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns angle 1 that is measured between the two bodies, or between the body and the static environment. The angle is between -pi and pi.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_angle1_rate.html language=enus -->
## TOPIC 00125: Angle1 Rate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_angle1_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_angle1_rate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle1 Rate Property

**Short Name:**AngleRate

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the rotation rate of the joint of angle 1 in radians.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_angle2_rate.html language=enus -->
## TOPIC 00126: Angle2 Rate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_angle2_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_angle2_rate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle2 Rate Property

**Short Name:**Angle2Rate

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the rotation rate of the joint of angle 2 in radians.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_axis1_stop_cfm.html language=enus -->
## TOPIC 00127: Axis1:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_axis1_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_axis1_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Stops the constraint force mixing value of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_axis2_hi_stop.html language=enus -->
## TOPIC 00128: Axis2:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_axis2_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_axis2_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the Hi Stop of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_axis2_stop_cfm.html language=enus -->
## TOPIC 00129: Axis2:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_axis2_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_axis2_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [Hinge2Joint Properties](lvode_hinge2joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Stops the constraint force mixing value of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hinge2joint_p.html language=enus -->
## TOPIC 00130: Hinge2Joint Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hinge2joint_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hinge2joint_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Hinge2Joint Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_p.html) class. View the class [hierarchy](lvode_classes.html).

- Anchor
- Anchor2
- Angle1
- Angle1 Rate
- Angle2 Rate
- Axis1:Axis
- Axis1:Bounce
- Axis1:CFM
- Axis1:FMax
- Axis1:Fudge Factor
- Axis1:Hi Stop
- Axis1:Lo Stop
- Axis1:Stop CFM
- Axis1:Stop ERP
- Axis1:Vel
- Axis2:Axis
- Axis2:Bounce
- Axis2:CFM
- Axis2:FMax
- Axis2:Fudge Factor
- Axis2:Hi Stop
- Axis2:Lo Stop
- Axis2:Stop CFM
- Axis2:Stop ERP
- Axis2:Vel
- Suspension CFM
- Suspension ERP

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hingejoint_angle_rate.html language=enus -->
## TOPIC 00131: Angle Rate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hingejoint_angle_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hingejoint_angle_rate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle Rate Property

**Short Name:**AngleRate

**Requires:**Robotics Module

**Class:**
 [HingeJoint Properties](lvode_hingejoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the rotation rate of the joint, specified in rad/s.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hingejoint_axis_bounce.html language=enus -->
## TOPIC 00132: Axis:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hingejoint_axis_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hingejoint_axis_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [HingeJoint Properties](lvode_hingejoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of the axis.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_hingejoint_axis_hi_stop.html language=enus -->
## TOPIC 00133: Axis:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_hingejoint_axis_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_hingejoint_axis_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [HingeJoint Properties](lvode_hingejoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of the axis.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_imu_anglerates.html language=enus -->
## TOPIC 00134: Angle Rates Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_imu_anglerates.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_imu_anglerates.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle Rates Property

**Short Name:**AngleRates

**Requires:**Robotics Module

**Class:**
 [IMU Properties](lvode_imu_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the measured angle rates.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_imu_orientation.html language=enus -->
## TOPIC 00135: Orientation Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_imu_orientation.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_imu_orientation.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Orientation Property

**Short Name:**Orientation

**Requires:**Robotics Module

**Class:**
 [IMU Properties](lvode_imu_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the orientation of the sensor.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_imu_p.html language=enus -->
## TOPIC 00136: IMU Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_imu_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_imu_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### IMU Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Sensor](lvode_sensor_p.html) class. View the class [hierarchy](lvode_classes.html).

An inertial measurement unit (IMU) is a sensor that contains [gyroscopes](lvode_gyroscope_p.html) and [accelerometers](lvode_accelerometer_p.html).

- Velocity
- Orientation
- Acceleration
- Angle Rates

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_joint_getparam.html language=enus -->
## TOPIC 00137: GetParam Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_joint_getparam.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_joint_getparam.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### GetParam Method

**Short Name:**JTGetParam

**Requires:**Robotics Module

**Class:**
 [Joint Method](lvode_joint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the parameters of a joint.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| GetParam | noDirection | void |
| parameter | noDirection | 32-bit signed integer |
| value | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_joint_type.html language=enus -->
## TOPIC 00138: Type Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_joint_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_joint_type.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Type Property

**Short Name:**Type

**Requires:**Robotics Module

**Class:**
 [Joint Properties](lvode_joint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the joint type.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_jointgroup_id.html language=enus -->
## TOPIC 00139: ID Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_jointgroup_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_jointgroup_id.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### ID Property

**Short Name:**ID

**Requires:**Robotics Module

**Class:**
 [JointGroup Properties](lvode_jointgroup_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns LVODE ID.

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_jointgroup_m.html language=enus -->
## TOPIC 00140: JointGroup Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_jointgroup_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_jointgroup_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### JointGroup Methods

**Requires:**Robotics Module

**Class:**
 [LVODE properties and methods](lvode_classes.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

A jointgroup is a collection of joints in a world.

You can add joints to a jointgroup. You can quickly destroy the entire group of joints at once. However, you cannot destroy individual joints in a jointgroup before the entire jointgroup is emptied.

[Empty](lvode_jointgroup_empty.html)

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lidar_direction.html language=enus -->
## TOPIC 00141: Direction Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lidar_direction.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lidar_direction.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Direction Property

**Short Name:**Direction

**Requires:**Robotics Module

**Class:**
 [LIDAR Properties](lvode_lidar_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the scanning directions at which this sensor searches for obstacles.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lidar_high_range.html language=enus -->
## TOPIC 00142: High Range Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lidar_high_range.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lidar_high_range.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### High Range Property

**Short Name:**HighRange

**Requires:**Robotics Module

**Class:**
 [LIDAR Properties](lvode_lidar_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the high range at which this sensor detects obstacles. You cannot modify this value after initializing communication with the sensor.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lidar_low_range.html language=enus -->
## TOPIC 00143: Low Range Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lidar_low_range.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lidar_low_range.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Low Range Property

**Short Name:**LowRange

**Requires:**Robotics Module

**Class:**
 [LIDAR Properties](lvode_lidar_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the low range at which this sensor detects obstacles. You cannot modify this value after initializing communication with the sensor.

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lmotorjoint_axis1_lo_stop.html language=enus -->
## TOPIC 00144: Axis1:Lo Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lmotorjoint_axis1_lo_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lmotorjoint_axis1_lo_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Lo Stop Property

**Short Name:**LoStop

**Requires:**Robotics Module

**Class:**
 [LMotorJoint Properties](lvode_lmotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the lo stop of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lmotorjoint_axis1_stop_cfm.html language=enus -->
## TOPIC 00145: Axis1:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lmotorjoint_axis1_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lmotorjoint_axis1_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [LMotorJoint Properties](lvode_lmotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop constraint force mixing (CFM) of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lmotorjoint_axis3_stop_erp.html language=enus -->
## TOPIC 00146: Axis3:Stop ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lmotorjoint_axis3_stop_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lmotorjoint_axis3_stop_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis3:Stop ERP Property

**Short Name:**StopERP

**Requires:**Robotics Module

**Class:**
 [LMotorJoint Properties](lvode_lmotorjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop error reduction parameter (ERP) of axis 3.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_lmotorjoint_m.html language=enus -->
## TOPIC 00147: LMotorJoint Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_lmotorjoint_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_lmotorjoint_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### LMotorJoint Methods

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_m.html) class. View the class [hierarchy](lvode_classes.html).

- GetAxis
- SetAxis

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_add.html language=enus -->
## TOPIC 00148: Add Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_add.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_add.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Add Method

**Short Name:**MassAdd

**Requires:**Robotics Module

**Class:**
 [Mass Method](lvode_mass_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds the mass b to the mass a.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Add | noDirection | void |
| b | noDirection | Reference number (refnum) |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_center.html language=enus -->
## TOPIC 00149: Center Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_center.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_center.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Center Property

**Short Name:**center

**Requires:**Robotics Module

**Class:**
 [Mass Properties](lvode_mass_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the mass center.

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_id.html language=enus -->
## TOPIC 00150: ID Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_id.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_id.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### ID Property

**Short Name:**ID

**Requires:**Robotics Module

**Class:**
 [Mass Properties](lvode_mass_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets the LVODE ID of the mass.

#### Data Type

32-bit signed integer

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_m.html language=enus -->
## TOPIC 00151: Mass Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Mass Methods

**Requires:**Robotics Module

**Class:**
 [LVODE properties and methods](lvode_classes.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Bodies in the robotics simulator contain the mass information. Use the mass methods to define the mass values of a body.

- Add
- Adjust
- Rotate
- SetBox
- SetBoxTotal
- SetCapsule
- SetCapsuleTotal
- SetCylinder
- SetCylinderTotal
- SetParameters
- SetSphere
- SetSphereTotal
- SetTrimesh
- SetTrimeshTotal
- SetZero
- Translate

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_setcylindertotal.html language=enus -->
## TOPIC 00152: SetCylinderTotal Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_setcylindertotal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_setcylindertotal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### SetCylinderTotal Method

**Short Name:**MassSetCylinderTotal

**Requires:**Robotics Module

**Class:**
 [Mass Method](lvode_mass_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Creates a cylinder mass of the size and total mass you specify.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| SetCylinderTotal | noDirection | void |
| total mass | noDirection | Single-precision, floating-point number |
| direction | noDirection | Single-precision, floating-point number |
| radius | noDirection | Single-precision, floating-point number |
| length | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_mass_setspheretotal.html language=enus -->
## TOPIC 00153: SetSphereTotal Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_mass_setspheretotal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_mass_setspheretotal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### SetSphereTotal Method

**Short Name:**MassSetSphereTotal

**Requires:**Robotics Module

**Class:**
 [Mass Method](lvode_mass_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Creates a sphere of the size and total mass you specify.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| SetSphereTotal | noDirection | void |
| total mass | noDirection | Single-precision, floating-point number |
| radius | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_motorcontroller_kd.html language=enus -->
## TOPIC 00154: Kd Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_motorcontroller_kd.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_motorcontroller_kd.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Kd Property

**Short Name:**Kd

**Requires:**Robotics Module

**Class:**
 [Motor Controller Properties](lvode_motorcontroller_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the D control factor for PID control. The default value is 0.0.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_motorcontroller_kp.html language=enus -->
## TOPIC 00155: Kp Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_motorcontroller_kp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_motorcontroller_kp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Kp Property

**Short Name:**Kp

**Requires:**Robotics Module

**Class:**
 [Motor Controller Properties](lvode_motorcontroller_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the P control factor for PID control. The default value is 1.0.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_motorcontroller_positioncontrol.html language=enus -->
## TOPIC 00156: Position Control Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_motorcontroller_positioncontrol.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_motorcontroller_positioncontrol.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Position Control Method

**Short Name:**PositionControl

**Requires:**Robotics Module

**Class:**
 [Motor Controller Method](lvode_motorcontroller_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Sets the position of motor using PID control.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Position Control | noDirection | void |
| target position | noDirection | numeric single value |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pistonjoint_positionrate.html language=enus -->
## TOPIC 00157: PositionRate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pistonjoint_positionrate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pistonjoint_positionrate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### PositionRate Property

**Short Name:**PositionRate

**Requires:**Robotics Module

**Class:**
 [PistonJoint Properties](lvode_pistonjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the time derivative of the position.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pistonjoint_prismatic_joint_stop_erp.html language=enus -->
## TOPIC 00158: Prismatic Joint:Stop ERP Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pistonjoint_prismatic_joint_stop_erp.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pistonjoint_prismatic_joint_stop_erp.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Joint:Stop ERP Property

**Short Name:**StopERP

**Requires:**Robotics Module

**Class:**
 [PistonJoint Properties](lvode_pistonjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop error reduction parameter (ERP) of the prismatic part.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pistonjoint_rotoide_joint_fmax.html language=enus -->
## TOPIC 00159: Rotoide Joint:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pistonjoint_rotoide_joint_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pistonjoint_rotoide_joint_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotoide Joint:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [PistonJoint Properties](lvode_pistonjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the fmax of the rotoide part.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_prjoint_positionrate.html language=enus -->
## TOPIC 00160: PositionRate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_prjoint_positionrate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_prjoint_positionrate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### PositionRate Property

**Short Name:**PositionRate

**Requires:**Robotics Module

**Class:**
 [PRJoint Properties](lvode_prjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the position rate.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_prjoint_prismatic_articulation_bounce.html language=enus -->
## TOPIC 00161: Prismatic Articulation:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_prjoint_prismatic_articulation_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_prjoint_prismatic_articulation_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Articulation:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [PRJoint Properties](lvode_prjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of the prismatic articulation.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_prjoint_prismatic_articulation_fmax.html language=enus -->
## TOPIC 00162: Prismatic Articulation:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_prjoint_prismatic_articulation_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_prjoint_prismatic_articulation_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Articulation:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [PRJoint Properties](lvode_prjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the FMax of the prismatic articulation.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_prjoint_prismatic_articulation_stop_cfm.html language=enus -->
## TOPIC 00163: Prismatic Articulation:Stop CFM Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_prjoint_prismatic_articulation_stop_cfm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_prjoint_prismatic_articulation_stop_cfm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Articulation:Stop CFM Property

**Short Name:**StopCFM

**Requires:**Robotics Module

**Class:**
 [PRJoint Properties](lvode_prjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the stop constraint force mixing (CFM) of the prismatic articulation.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pujoint_axis1_hi_stop.html language=enus -->
## TOPIC 00164: Axis1:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pujoint_axis1_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pujoint_axis1_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [PUJoint Properties](lvode_pujoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pujoint_prismatic_articulation_fmax.html language=enus -->
## TOPIC 00165: Prismatic Articulation:FMax Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pujoint_prismatic_articulation_fmax.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pujoint_prismatic_articulation_fmax.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Articulation:FMax Property

**Short Name:**FMax

**Requires:**Robotics Module

**Class:**
 [PUJoint Properties](lvode_pujoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the FMax of the prismatic articulation.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_pujoint_prismatic_articulation_hi_stop.html language=enus -->
## TOPIC 00166: Prismatic Articulation:Hi Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_pujoint_prismatic_articulation_hi_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_pujoint_prismatic_articulation_hi_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Prismatic Articulation:Hi Stop Property

**Short Name:**HiStop

**Requires:**Robotics Module

**Class:**
 [PUJoint Properties](lvode_pujoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the hi stop of the prismatic articulation.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_ray_m.html language=enus -->
## TOPIC 00167: Ray Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_ray_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_ray_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Ray Methods

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Geom](lvode_geom_m.html) class. View the class [hierarchy](lvode_classes.html).

A ray is different from all the other Geom classes in that it does not represent a solid object. A ray is an infinitely thin line that starts from the position of the geom and extends in the direction of the local z-axis of the geom.

- Get
- Get
- Set
- SetParams

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_sensor_noise.html language=enus -->
## TOPIC 00168: Noise Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_sensor_noise.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_sensor_noise.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Noise Property

**Short Name:**Noise

**Requires:**Robotics Module

**Class:**
 [Sensor Properties](lvode_sensor_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the measurement noise of a sensor. Just as data from a real sensor might contain noise, data from a simulated sensor can contain simulated noise. The default is 0.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_sliderjoint_addforce.html language=enus -->
## TOPIC 00169: AddForce Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_sliderjoint_addforce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_sliderjoint_addforce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AddForce Method

**Short Name:**SJAddForce

**Requires:**Robotics Module

**Class:**
 [SliderJoint Method](lvode_sliderjoint_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Adds two forces.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| AddForce | noDirection | void |
| force | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_sliderjoint_m.html language=enus -->
## TOPIC 00170: SliderJoint Methods

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_sliderjoint_m.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_sliderjoint_m.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### SliderJoint Methods

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Joint](lvode_joint_m.html) class. View the class [hierarchy](lvode_classes.html).

[AddForce](lvode_sliderjoint_addforce.html)

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_sliderjoint_position_rate.html language=enus -->
## TOPIC 00171: Position Rate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_sliderjoint_position_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_sliderjoint_position_rate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Position Rate Property

**Short Name:**PositionRate

**Requires:**Robotics Module

**Class:**
 [SliderJoint Properties](lvode_sliderjoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the position rate of the joint.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_space_p.html language=enus -->
## TOPIC 00172: Space Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_space_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_space_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Space Properties

**Requires:**Robotics Module

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Inherits from the [Geom](lvode_geom_p.html) class. View the class [hierarchy](lvode_classes.html).

A space is a non-placeable geom that can contain other geoms. It is similar to the rigid body concept of the world except that it applies to collision instead of dynamics. Space objects improve the performance of collision detection. Without spaces, you might generate contacts in your simulation by calling the [Collide](../lvroboprop/lvode_geom_collide.html) method of the [Geom](../lvroboprop/lvode_geom_m.html) class to get contact points for every single pair of geoms. This is computationally expensive if your environment has many objects. A better approach is to insert the geoms into a space and call the [Collide](lvode_space_collide.html) of the Space class.

- Clean
- Number of Geoms

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_sphere_radius.html language=enus -->
## TOPIC 00173: Radius Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_sphere_radius.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_sphere_radius.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Radius Property

**Short Name:**Radius

**Requires:**Robotics Module

**Class:**
 [Sphere Properties](lvode_sphere_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the radius of a sphere.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_anchor.html language=enus -->
## TOPIC 00174: Anchor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_anchor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_anchor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Anchor Property

**Short Name:**Anchor

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the position of the joint anchor point in the form of (x, y, z). The joint tries to keep this point on each body together.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

1D array of single-precision, floating-point numbers

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_angle1_rate.html language=enus -->
## TOPIC 00175: Angle1 Rate Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_angle1_rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_angle1_rate.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Angle1 Rate Property

**Short Name:**AngleRate

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Returns the rotation rate of the joint of angle 1 in radians.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read only

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_axis1_bounce.html language=enus -->
## TOPIC 00176: Axis1:Bounce Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_axis1_bounce.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_axis1_bounce.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Bounce Property

**Short Name:**Bounce

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the bounce of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_axis1_fudge_factor.html language=enus -->
## TOPIC 00177: Axis1:Fudge Factor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_axis1_fudge_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_axis1_fudge_factor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Fudge Factor Property

**Short Name:**FudgeFactor

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the Fudge Factor of an axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_axis1_lo_stop.html language=enus -->
## TOPIC 00178: Axis1:Lo Stop Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_axis1_lo_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_axis1_lo_stop.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis1:Lo Stop Property

**Short Name:**LoStop

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the Lo Stop of axis 1.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_universaljoint_axis2_fudge_factor.html language=enus -->
## TOPIC 00179: Axis2:Fudge Factor Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_universaljoint_axis2_fudge_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_universaljoint_axis2_fudge_factor.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Axis2:Fudge Factor Property

**Short Name:**FudgeFactor

**Requires:**Robotics Module

**Class:**
 [UniversalJoint Properties](lvode_universaljoint_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the Fudge Factor of axis 2.

View an [illustration of the joint and its components](../lvroboprop/robo_joint_defs.html).

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_altitude.html language=enus -->
## TOPIC 00180: Altitude Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_altitude.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_altitude.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Altitude Property

**Short Name:**Altitude

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the altitude of the world origin point.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_lineardamping.html language=enus -->
## TOPIC 00181: LinearDamping Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_lineardamping.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_lineardamping.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### LinearDamping Property

**Short Name:**LinearDamping

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the world's default linear damping. Bodies will use the world's parameters by default.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_lineardampingthreshold.html language=enus -->
## TOPIC 00182: LinearDampingThreshold Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_lineardampingthreshold.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_lineardampingthreshold.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### LinearDampingThreshold Property

**Short Name:**LinearDampingThreshold

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the world's default linear damping threshold. Bodies will use the world's parameters by default.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_longitude.html language=enus -->
## TOPIC 00183: Longitude Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_longitude.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_longitude.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Longitude Property

**Short Name:**Longitude

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the longitude of the world origin point.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_p.html language=enus -->
## TOPIC 00184: World Properties

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_p.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_p.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### World Properties

**Requires:**Robotics Module

**Class:**
 [LVODE properties and methods](lvode_classes.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

The world object is a container for rigid bodies and joints. Step the world frequently to make it active.

Objects in different worlds cannot interact. For example, rigid bodies from two different worlds cannot collide. Most applications require only one world. However, all objects in a world exist at the same point in time, so you must use separate worlds is to simulate systems at different rates.

- Altitude
- AngularDamping
- AngularDampingThreshold
- AutoDisableAngularThreshold
- AutoDisableFlag
- AutoDisableLinearThreshold
- AutoDisableSteps
- AutoDisableTime
- AutoEnableDepthSF1
- Constraint Force Mixing
- ContactMaxCorrectingVel
- ContactSurfaceLayer
- Error Reduction Parameter
- Gravity
- ID
- Latitude
- LinearDamping
- LinearDampingThreshold
- Longitude
- MaxAngularSpeed
- QuickStepNumIterations
- QuickStepW
- Time

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_quickstep.html language=enus -->
## TOPIC 00185: QuickStep Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_quickstep.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_quickstep.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### QuickStep Method

**Short Name:**WorldQuickStep

**Requires:**Robotics Module

**Class:**
 [World Method](lvode_world_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Steps the world. For large systems this method performs better than the [Step](lvode_world_step.html) method, but this method is less accurate.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Quick Step | noDirection | void |
| stepsize | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_quickstepnumiterations.html language=enus -->
## TOPIC 00186: QuickStepNumIterations Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_quickstepnumiterations.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_quickstepnumiterations.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### QuickStepNumIterations Property

**Short Name:**QuickStepNumIterations

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the number of iterations that the [QuickStep](lvode_world_quickstep.html) method performs per step.

#### Data Type

32-bit signed integer

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_quickstepw.html language=enus -->
## TOPIC 00187: QuickStepW Property

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_quickstepw.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_quickstepw.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### QuickStepW Property

**Short Name:**QuickStepW

**Requires:**Robotics Module

**Class:**
 [World Properties](lvode_world_p.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Gets or sets the over-relaxation parameter for the SOR algorithm of the [QuickStep](lvode_world_quickstep.html) method.

#### Data Type

Single-precision, floating-point number

#### Permissions

read/write

<!--NI_TOPIC bundle=labview-robotics-module path=lvroboprop/lvode_world_step.html language=enus -->
## TOPIC 00188: Step Method

- bundle_id: `labview-robotics-module`
- source_path: `lvroboprop/lvode_world_step.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvroboprop/lvode_world_step.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Step Method

**Short Name:**WorldStep

**Requires:**Robotics Module

**Class:**
 [World](lvode_world_m.html)

**To Use:** [Create a property or method](../lvrobogsm/robo_sim_programming.html#lvode).

Steps the world. For large systems this method performs slower than the [QuickStep](lvode_world_quickstep.html) method, but this method is more accurate.

#### Parameters

| Name | Direction | Type |
| --- | --- | --- |
| Step | noDirection | void |
| stepsize | noDirection | Single-precision, floating-point number |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/ad_star_initialize.html language=enus -->
## TOPIC 00189: Initialize AD* VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/ad_star_initialize.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/ad_star_initialize.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Initialize AD* VI

**Owning Palette:** [Path Planning VIs](../lvrobovi/path_planning_pal.html)

**Requires:** Robotics Module

Initializes a path planning session with which the [AD*](../lvrobovi/ad_star_plan.html) VI operates.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='anytime_d_star_initialize.gif']

|  | map reference in is a reference to the map that represents the robot environment. You can use the Create Directed Graph Map VI or Create Occupancy Grid Map VI to generate this LabVIEW class object. |
| --- | --- |
|  | start reference specifies the current position of the robot within the map. If this VI operates on a directed graph map or occupancy grid map, you can use the Get Node Reference VI or Get Cell Reference VI, respectively, to generate this LabVIEW class object. |
|  | goal reference specifies the position to which the robot should navigate within the map. If this VI operates on a directed graph map or occupancy grid map, you can use the Get Node Reference VI or Get Cell Reference VI, respectively, to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | manual epsilon, if TRUE (default), requires you to specify a heuristic multiplier in the AD* VI that controls the optimality of the paths the VI plans. Otherwise, LabVIEW manages the multiplier automatically. Refer to the Details section for more information about the epsilon value. |
|  | Anytime D* is an object on which the AD* VI operates to plan a dynamic path. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize AD* Details

The AD* path planning algorithm can be time-intensive if you want a highly optimal path. When you specify TRUE for **manual epsilon** to control the optimality of the paths the AD* VI calculates, you can balance the time required to plan with the accuracy of the path calculated.

|  | Note When LabVIEW automatically manages the epsilon value, the paths are not necessarily optimal. Refer to the description of the epsilon input in the AD* VI topic for more information about how LabVIEW manages and uses this value. |
| --- | --- |

#### Example

Refer to the Anytime D Star on an Occupancy Grid.lvproj in the labview\examples\robotics\Path Planning\ADstar\ADstar on Occupancy Grid directory for an example of using the Initialize AD* VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/ad_star_plan.html language=enus -->
## TOPIC 00190: AD* VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/ad_star_plan.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/ad_star_plan.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### AD* VI

**Owning Palette:** [Path Planning VIs](../lvrobovi/path_planning_pal.html)

**Requires:** Robotics Module

Plans a dynamic path through a map to the goal you specify. The first time this VI runs, the VI returns an initial path to a goal node within the map you specify in the [Initialize AD*](../lvrobovi/ad_star_initialize.html) VI.

Use this VI in a [loop with shift registers](/csh?topicname=lvconcepts/shift_registers_concepts.html) to update the **path references** through the map in each iteration. This VI searches the map for updates and then updates the path accordingly the next time the VI runs.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='anytime_d_star_plan.gif']

|  | overhaul, when TRUE, ends the current planning session and begins a new session. Refer to the Details section for information on when to begin a new path planning session. |
| --- | --- |
|  | Anytime D* in is a reference to an AD* object from the Initialize AD* VI. |
|  | current reference specifies the current position of the robot within the map. If this VI operates on a directed graph map or occupancy grid map, you can use the Get Node Reference VI or Get Cell Reference VI, respectively, to generate this LabVIEW class object. |
|  | new goal reference specifies a new position to which the robot should navigate within the map. If this VI operates on a directed graph map or occupancy grid map, you can use the Get Node Reference VI or Get Cell Reference VI, respectively, to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | epsilon is a number greater than or equal to 1 that specifies the level of optimality for the path. If epsilon is 1, this VI plans an optimal, or least-cost path. If epsilon is greater than 1, this VI returns the path faster, but the path is optimal for the value of epsilon, where path cost ≤ epsilon * n and where n is the cost of the optimal path. In the Initialize AD* VI, you can choose to set epsilon manually. If you do not control the value manually, the AD* VI sets epsilon equal to 5 the first time the VI runs and decreases the value by 1 each time the VI runs until epsilon is 1 and the VI returns an optimal path. |
|  | Anytime D* out is the object this VI uses to update path references. |
|  | path references is an array of references to points on the map along the path this VI calculates. If no valid path exists is TRUE, LabVIEW returns a partial path. Otherwise, path references contains a complete path to the goal node.You can use a partial path to direct a mobile robot to a point in the map that is nearer to the goal than the current position of the robot. |
|  | no valid path exists is TRUE if the path references do not end at the goal node. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | path cost is the cost of traversing the path references. path cost returns Inf if no possible path exists or the map changes significantly. |

#### AD* Details

This VI uses an Anytime D* (AD*) algorithm to calculate a sub-optimal path quickly and then update the path in subsequent executions until the VI plans an optimal path. Also, this VI can run while the robot application processes input data from sensors so that this VI can reflect changes to the robot environment in subsequent paths to the goal node.

This VI uses information from previous iterations to calculate paths. Therefore, if you specify a **new goal reference** within the map, this VI automatically ends the current the path planning session and plans a new initial path. If the map changes significantly, use the **overhaul** input to reset the path planning session manually. Resetting the session is more efficient than allowing the VI to replan the path from previous calculations that are invalid after the map changes.

LabVIEW locks maps while this VI plans paths through them. While a map is locked, LabVIEW queues any updates to the map and applies them when this VI finishes planning a path.

|  | Note The following resource offers useful background information about the algorithm discussed in this documentation. This resource is provided for general informational purposes only and is not affiliated, sponsored, or endorsed by National Instruments. The content of this resource is not a representation of, may not correspond to, and does not imply current or future functionality in the Robotics Module or any other National Instruments product. |
| --- | --- |

Likhachev, Maxim, Dave Ferguson, Geoff Gordon, Anthony Stentz, and Sebastian Thrun. "Anytime Search in Dynamic Graphs," *Artificial Intelligence Journal (AIJ)* 172, no. 14 (September 2008): 1613–1643.

#### Example

Refer to the Anytime D Star on an Occupancy Grid.lvproj in the labview\examples\robotics\Path Planning\ADstar\ADstar on Occupancy Grid directory for an example of using the AD* VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/add_node.html language=enus -->
## TOPIC 00191: Add Node VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/add_node.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/add_node.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Add Node VI

**Owning Palette:** [Directed Graph Map VIs](../lvrobovi/directed_graph_pal.html)

**Requires:** Robotics Module

Adds a unique point, or node, to a map at the coordinates you specify.

If the map already contains a node with the same name as **name**, this VI does not add the node to the map.

[Example](#examples)

[IMAGE alt='image' src='add_node.gif']

|  | map reference in is a reference to the map that represents the robot environment. Use the Create Directed Graph Map VI to generate this LabVIEW class object. |
| --- | --- |
|  | name assigns a name to the map node. For this VI to operate on a specific node, the node must have a unique name. |
|  | coordinates specifies the position of the node within the directed graph map. The number of elements in coordinates corresponds to the number of dimensions in the robot environment you want to represent. For example, most ground robots can move to a point at given x- and y-coordinates, in which case coordinates contains two elements. As the number of dimensions you define within a map increases, so does the time required to calculate a path through the map. However, a path through a map with three dimensions might be more optimal than a path between the same points through a map with two dimensions because more movements are possible in the former map. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | map reference out is a reference to the map that represents the robot environment. You can wire this output to other Path Planning VIs. |
|  | already exists? returns TRUE if a node with the same name as the name you specify exists. If TRUE, this VI does not add the node to the map. LabVIEW does not return an error if already exists is TRUE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Astar on Voronoi.lvproj in the labview\examples\robotics\Path Planning\Astar\Astar on Voronoi Graph directory for an example of using the Add Node VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/add_quaternions.html language=enus -->
## TOPIC 00192: Add Quaternions VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/add_quaternions.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/add_quaternions.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Add Quaternions VI

**Owning Palette:** [Quaternions VIs](../lvrobovi/quaternion_pal.html)

**Requires:** Robotics Module

Returns the sum of two quaternions.

[IMAGE alt='image' src='add_quaternions.gif']

|  | quaternion 1 is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | quaternion 2 is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
|  | sum is the sum of quaternion 1 and quaternion 2. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/add_wheels_to_frame.html language=enus -->
## TOPIC 00193: Add Wheels to Steering Frame VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/add_wheels_to_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/add_wheels_to_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Add Wheels to Steering Frame VI

**Owning Palette:** [Advanced VIs](../lvrobovi/steering_advanced_pal.html)

**Requires:** Robotics Module

Adds the wheel or wheels you specify to **steering frame in**. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

[Details](#details)

#### Add Single Wheel to Steering Frame

[IMAGE alt='image' src='add_single_wheel_to_steering_frame.gif']

|  | x position specifies the x-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the left of the center, and a positive value represents a position to the right of the center. |
| --- | --- |
|  | y position specifies the y-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the rear of the center, and a positive value represents a position to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel is a reference to a steering frame wheel. Use the Create Wheel VI to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angle (rad) specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Add Multiple Wheels to Steering Frame

[IMAGE alt='image' src='add_multiple_wheels_to_steering_frame.gif']

|  | x positions specifies the x-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. |
| --- | --- |
|  | y positions specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheels contains an array of references to steering frame wheels. Use the Create Wheel VI to generate these LabVIEW class objects. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angles (rad) specifies the angles of the wheel frames, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Add Wheels to Steering Frame Details

When you use the Steering VIs to create and operate on a steering frame and wheels, always use a consistent unit of measurement when you specify values that represent distance.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/advanced_vfh.html language=enus -->
## TOPIC 00194: Advanced VFH VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/advanced_vfh.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/advanced_vfh.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Advanced VFH VI

**Owning Palette:** [Obstacle Avoidance VIs](../lvrobovi/obstacle_avoid_pal.html)

**Requires:** Robotics Module

Identifies obstacles and gaps, or open areas, in the robot environment and returns an open direction for travel that best leads to a goal position.

|  | Note This VI accepts and returns angle values in radians. You can use any unit of measurement to specify distance values. However, always use a consistent unit when you specify these values. |
| --- | --- |

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='advanced_vfh.gif']

|  | obstacle clearance distance specifies the minimum distance by which the center of the vehicle can approach an obstacle. The default is 0. Use this input to account for the space required for the vehicle body that extends out from the position of the sensor. |
| --- | --- |
|  | heading is a cluster that contains the following elements. current heading (rad) specifies the direction at which the vehicle points. target heading (rad) specifies the direction at which the goal position lies. |
|  | current heading (rad) specifies the direction at which the vehicle points. |
|  | target heading (rad) specifies the direction at which the goal position lies. |
|  | distances specifies the distances between the robot sensor and objects in the robot environment. |
|  | direction angles (rad) specifies the angles at which objects are located with respect to the center of the sensor. Elements in direction angles (rad) correspond to elements in distances. |
|  | thresholds specifies the range at which this VI identifies an obstacle as too close to clear. This VI measures threshold distances from the outside edge of the obstacle clearance distance around the vehicle to obstacles. inner threshold distance specifies the distance between the sensor and an obstacle at which this VI first considers the direction blocked. outer threshold distance specifies the distance between the sensor and an obstacle at which this VI no longer considers the direction blocked. When you run this VI repeatedly in a loop and a sensor detects an obstacle within inner threshold distance, this VI considers the direction blocked until a sensor returns a distance to the obstacle that exceeds outer threshold distance. |
|  | inner threshold distance specifies the distance between the sensor and an obstacle at which this VI first considers the direction blocked. |
|  | outer threshold distance specifies the distance between the sensor and an obstacle at which this VI no longer considers the direction blocked. When you run this VI repeatedly in a loop and a sensor detects an obstacle within inner threshold distance, this VI considers the direction blocked until a sensor returns a distance to the obstacle that exceeds outer threshold distance. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | # bins determines the number of headings this VI considers for travel. For higher performance, specify a smaller # bins than is possible. The default is 399. |
|  | maximum heading change (rad) specifies the greatest angle by which the vehicle can change direction when an obstacle blocks the current heading of the vehicle. You should limit maximum heading change (rad) to the range of headings for which the vehicle has sensor data. The default is 1.5708. |
|  | chosen heading (rad) contains the direction of travel this VI calculates in response to the goal position and obstacles in the vehicle environment. |
|  | histogram returns the histogram data that represents the distances to objects in range of the sensor, arranged by angle and direction. |
|  | mask contains Boolean values that specify whether a direction in the robot environment is blocked. A value of FALSE indicates an obstacle blocks the heading. # bins determines the number of elements in mask. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Advanced VFH Details

Use this VI to perform target tracking because when a robot vehicle encounters an obstacle within the **inner threshold distance**, this VI calculates a new heading, but the vehicle remains near the target. This VI considers a heading blocked when an obstacle is within an **inner threshold distance**. Then, to account for sensor noise, this VI finds that heading free only when sensors show the obstacle outside the **outer threshold distance**.

Use the Simple Vector Field Histogram to implement reactionary motion without a goal.

The following front panel represents a robot vehicle that encounters an obstacle within the **inner threshold distance** of the robot and shows the open and blocked headings that result. The histogram data represents the position at which the object becomes an obstacle given the **obstacle clearance distance** of the robot, and the LIDAR sensor data represents the obstacle itself.

[IMAGE alt='image' src='loc_fp_avfh_graph.gif']

#### Example

Refer to the Simulated Mecanum Robot.lvproj in the labview\examples\robotics\Simulated Mecanum Robot directory for an example of using the Advanced VFH VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/an_inverse_kinematics.html language=enus -->
## TOPIC 00195: Analytical Inverse Kinematics VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/an_inverse_kinematics.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/an_inverse_kinematics.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Analytical Inverse Kinematics VI

**Owning Palette:** [Kinematics VIs](../lvrobovi/kinematics_pal.html)

**Requires:** Robotics Module

Returns the joint angles of a [6R](../lvrobogsm/robo_arm_definition.html#6r), [5R](../lvrobogsm/robo_arm_definition.html#5r), or [SCARA arm](../lvrobogsm/robo_arm_definition.html#scara) given the posture of the end effector relative to the arm base. Wire data to the ***X*****_serial arm in** input, where ***X*** is the arm type, to determine the polymorphic instance to use or [manually select the instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html).

This VI uses an analytical solver to compute inverse kinematics, while the [Inverse Kinematics](../lvrobovi/inverse_kinematics.html) VI provides an analytical solver. [Choose an inverse kinematics solver](../lvrobogsm/robo_arm_concepts.html#kinematics) according to the arm type you generate.

[Examples](#examples)

#### SCARA

This instance accepts [SCARA serial arms](../lvrobogsm/robo_arm_definition.html#scara).

[IMAGE alt='image' src='scara_inverse_kinematics.gif']

|  | SCARA serial arm in is a reference to a SCARA serial robotic arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector position is a four-element array whose elements represent the position of the end effector relative to the arm base. The end effector position array is in the form of [x, y, z, theta], where x, y, z correspond to translation along the x-, y-, and z-axes and theta corresponds to rotation in radians about the z-axis. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SCARA serial arm out is a reference to a SCARA serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | joint positions returns two solutions for achieving the input end effector position. joint positions returns a 2 × 4 array in which the first row is the solution when 0<joint 2<180 degrees. The second row is the solution when 180<joint 2<360 degrees. Each column represents the position of a joint expressed in radians. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 6R Type 1

This instance accepts [6R type 1 serial arms](../lvrobogsm/robo_arm_definition.html#6r).

[IMAGE alt='image' src='analytical_inverse_kinematics_6r_type_1.gif']

|  | 6R type 1 serial arm in is a reference to a 6R type 1 serial robotic arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector transform specifies the homogenous transform that represents the position of the end effector relative to the arm base. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | 6R type 1 serial arm out is a reference to a 6R type 1 serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | joint positions returns solutions for achieving the input end effector transform. joint positions returns a 2D array in which each row is a solution and each column represents the position of a joint expressed in radians. NaN indicates a row is invalid. |
|  | number of valid solutions specifies the number of rows of joint values that are valid based on the arm parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 6R Type 2

This instance accepts [6R type 2 serial arms](../lvrobogsm/robo_arm_definition.html#6r).

[IMAGE alt='image' src='analytical_inverse_kinematics_6r_type_2.gif']

|  | 6R type 2 serial arm in is a reference to a 6R type 2 serial robotic arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector transform specifies the homogenous transform that represents the position of the end effector relative to the arm base. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | 6R type 2 serial arm out is a reference to a 6R type 2 serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | joint positions returns solutions for achieving the input end effector transform. joint positions returns a 2D array in which each row is a solution and each column represents the position of a joint expressed in radians. NaN indicates a row is invalid. |
|  | number of valid solutions specifies the number of rows of joint values that are valid based on the arm parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 6R Type 3

This instance accepts [6R type 3 serial arms](../lvrobogsm/robo_arm_definition.html#6r).

[IMAGE alt='image' src='analytical_inverse_kinematics_6r_type_3.gif']

|  | 6R type 3 serial arm in is a reference to a 6R type 3 serial robotic arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector transform specifies the homogenous transform that represents the position of the end effector relative to the arm base. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | 6R type 3 serial arm out is a reference to a 6R type 3 serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | joint positions returns solutions for achieving the input end effector transform. joint positions returns a 2D array in which each row is a solution and each column represents the position of a joint expressed in radians. NaN indicates a row is invalid. |
|  | number of valid solutions specifies the number of rows of joint values that are valid based on the arm parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 5R Type 1

This instance accepts [5R type 1 serial arms](../lvrobogsm/robo_arm_definition.html#5r).

[IMAGE alt='image' src='analytical_inverse_kinematics_5r_type_1.gif']

|  | 5R type 1 serial arm in is a reference to a 5R type 1 serial robotic arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector transform specifies the homogenous transform that represents the position of the end effector relative to the arm base. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | 5R type 1 serial arm out is a reference to a 5R type 1 serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | joint positions returns solutions for achieving the input end effector transform. joint positions returns a 2D array in which each row is a solution and each column represents the position of a joint expressed in radians. NaN indicates a row is invalid. |
|  | reachable returns whether the end effector can reach the position you specify in end effector transform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Analytical Inverse Kinematics VI:

- labview\examples\robotics\Simulator\SCARA Arm\SCARA Arm.lvproj
- labview\examples\robotics\Simulator\Puma560\Puma560 Simulator.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/cartesian_inertia.html language=enus -->
## TOPIC 00196: Cartesian Manipulator Inertia VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/cartesian_inertia.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/cartesian_inertia.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Cartesian Manipulator Inertia VI

**Owning Palette:** [Dynamics VIs](../lvrobovi/dynamics_pal.html)

**Requires:** Robotics Module

Calculates a matrix that represents the kinetic energy of the end effector of a robotic arm in Cartesian space. Wire data to the **joint positions** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

**.m file:** [cinertia](robotic_arm_pal.html#details)

#### Cartesian Manipulator Inertia (Point)

Use this instance to calculate values at a single point.

[IMAGE alt='image' src='cartesian_manipulator_inertia_point.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | joint positions specifies the joint angles that make up the robotic arm pose for which you want to calculate the solution. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | inertia matrix contains the torque that results from inertia at each joint in joint positions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cartesian Manipulator Inertia (Trajectory)

Use this instance to calculate values at points along a trajectory.

[IMAGE alt='image' src='cartesian_manipulator_inertia_trajectory.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | joint position trajectory specifies the joint angles of the robotic arm pose at points along a trajectory where each row represents a pose at a particular time and each column represents a particular joint. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | inertia matrix trajectory contains the torques that result from inertia at each joint in joint position trajectory. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/close_motor_comm.html language=enus -->
## TOPIC 00197: Close Motor Communication VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/close_motor_comm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/close_motor_comm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Close Motor Communication VI

**Owning Palette:** [Motor Communication VIs](../lvrobovi/motor_comm_pal.html)

**Requires:** Robotics Module

Terminates a communication session between a motor and the wheel the motor controls. Wire data to the **motor communication in** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Close Single Motor Communication

[IMAGE alt='image' src='close_motor_communication_scalar.gif']

|  | motor communication in is a reference to the communication session between a motor and the wheel the motor controls. Use the Initialize Motor Communication VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Close Multiple Motor Communication

[IMAGE alt='image' src='close_motor_communication_vector.gif']

|  | motor communication in is an array of references to communication sessions between motors and the wheels the motors control. Use the Initialize Motor Communication VI to generate these LabVIEW class objects. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/config_steering_frame.html language=enus -->
## TOPIC 00198: Configure Steering Frame Express VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/config_steering_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/config_steering_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Configure Steering Frame Express VI

**Owning Palette:** [Steering VIs](../lvrobovi/steering_pal.html)

**Requires:** Robotics Module

Generates a [wheeled steering frame](../lvrobogsm/robo_steering.html) that you design in an interactive dialog box. You can choose from pre-defined steering frame designs or create a custom frame design.

|  | Tip You can click and drag a wheel in the preview section of the dialog box to change the position of the wheel. If the steering frame is user-defined, you also can press the <Shift> key and then click and drag a wheel to change its angle relative to the steering frame. |
| --- | --- |

You also can [programmatically generate a steering frame](../lvrobogsm/robo_steering.html).

[Example](#examples)

| Dialog Box Options |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Steering Type | Sets the overall design of the steering frame you want to create. The design you choose determines which properties of the steering frame you can edit in this dialog box. Select from the following designs: User Defined—Frame is fully customizable, allowing you to set all properties of wheels, such as the number of wheels and their types and positions. Differential—Frame consists of two fixed wheels. The center of a differential steering frame is at the midpoint of the wheel separation. Ackermann—Frame consists of two steering front wheels and two fixed rear wheels. The center of the steering frame is at the midpoint of the width between the rear wheels. Mecanum—Frame consists of four Mecanum wheels. The center of the steering frame is at the midpoint of the rectangle formed by the four wheels. |
| Angle Units | Specifies whether to express the angles of wheels relative to the steering frame in degrees or radians. |
| Wheels | Lists wheels that are currently part of the steering frame design. If you select a Steering Type that is not User Defined, you cannot edit this list because pre-defined frames require specific configurations of wheels. Use the buttons below the Wheels list to add, remove, and copy wheels. |
| Wheel Type | Specifies the design for the wheel selected in the Wheels list. Select from the following options: Fixed—Fixed wheels travel forward and backward and cannot change steering angle. Steering—LabVIEW assumes that the steering angle of steering wheels can change instantaneously to satisfy nonslip and pure-rolling constraints. Caster—The steering angle of a caster wheel is the location of the wheel about the pivot attached to the steering frame. Caster wheels have a forward offset from the center point but no lateral offset. Mecanum—Mecanum wheels consist of a series of rollers around the circumference, oriented 45 degrees from the wheel axis. Omni—Omni wheels consist of a series of rollers around the circumference, oriented perpendicular to the wheel axis. Availability: When Steering Type is User Defined. |
| Wheel Name | Specifies the identifier assigned to the wheel. You can pass this name to VIs on the Advanced steering palette to programmatically act on a specific wheel. Availability: When Steering Type is User Defined. |
| X Position | Specifies the x-coordinate of the wheel with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. Availability: When Steering Type is User Defined. |
| Y Position | Specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. Availability: When Steering Type is User Defined. |
| Frame Angle | Specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. Express this value in radians or degrees according to the option you select in the Angle Units pull-down menu. Availability: When Steering Type is User Defined. |
| Wheel Radius | Specifies the radius of the wheel. You can use any unit of measurement to specify distance values. However, always use consistent units when you specify these values. |
| Gear Ratio | Specifies the ratio of motor velocity to wheel velocity in the forward direction. |
| Forward Rotation Direction | Specifies the direction in which the wheel turns when the wheel rotates forward, given an end-on view of the wheel axle. Choose from clockwise or counterclockwise. Availability: When Steering Type is User Defined. |
| Max Steering Angle | Specifies the largest possible counterclockwise angle formed between the wheel axle and the frame of reference of the steering frame. Availability: When Steering Type is User Defined and Wheel Type is Steering. |
| Min Steering Angle | Specifies the largest possible clockwise angle formed between the wheel axle and the frame of reference of the steering frame. Availability: When Steering Type is User Defined and Wheel Type is Steering. |
| Steering Gear Ratio | Specifies the ratio of motor angle to wheel angle in the direction of steering. Availability: When Steering Type is User Defined and Wheel Type is Steering. |
| Motor Angle Offset | Specifies the difference of the motor angle and the product of the steering gear ratio and the steering angle. Availability: When Steering Type is User Defined and Wheel Type is Steering. |
| Steering Range | Defines possible steering angles of the wheel. You can use either this control or the Max Steering Angle and Min Steering Angle options to set this range. This VI measures steering angles counterclockwise from the wheel frame angle as viewed from above, so angles to the left of the frame angle are positive values and angles to the right are negative values. Availability: When Steering Type is User Defined and Wheel Type is Steering. |
| Forward Offset | Specifies the distance between the center of the wheel and the center point attached to the steering frame. Availability: When Steering Type is User Defined and Wheel Type is Caster. |
| Caster Gear Ratio | Specifies the ratio of motor velocity to wheel velocity in the caster steering angle. This VI uses caster gear ratio only if you use the caster motor communication input to connect the wheel to a motor and then communicate wheel data to the motor. Availability: When Steering Type is User Defined and Wheel Type is Caster. |
| Roller Orientation | Specifies the direction in which the Mecanum wheel rollers angle. Left means the rollers meet the ground surface angle 45 degrees from the wheel shaft in the counterclockwise direction. Right means the rollers meet the ground surface angle 45 degrees from the wheel shaft in the clockwise direction. Availability: When Steering Type is User Defined and Wheel Type is Mecanum. |
| Wheel Separation | Specifies the distance between the two fixed wheels. Availability: When Steering Type is Differential. |
| Wheel Separation Width | Specifies the distance between the wheels on the left and right sides of the steering frame. Availability: When Steering Type is Ackermann or Mecanum. |
| Wheel Separation Length | Specifies the distance between the front and rear wheels of the steering frame. Availability: When Steering Type is Ackermann or Mecanum. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| error in | Describes error conditions that occur before this node runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| steering frame out | Returns a reference to the steering frame you designed in the interactive dialog box. You can wire this output to other Steering VIs. |
| error out | Contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Configurable Steering.lvproj in the labview\examples\robotics\Steering\Configurable Steering directory for an example of using the Configure Steering Frame.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/conjugate_quaternion.html language=enus -->
## TOPIC 00199: Conjugate Quaternion VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/conjugate_quaternion.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/conjugate_quaternion.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Conjugate Quaternion VI

**Owning Palette:** [Quaternions VIs](../lvrobovi/quaternion_pal.html)

**Requires:** Robotics Module

Returns the conjugate of a quaternion.

[Details](#details)

[IMAGE alt='image' src='conjugate_quaternion.gif']

|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | conjugate is the conjugate, or involution, of quaternion. |

#### Conjugate Quaternion Details

The conjugate of a quaternion in the form of *a* + *bi* + *cj* + *dk* is *a* – *bi* – *cj* – *dk*.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/coriolis_torque.html language=enus -->
## TOPIC 00200: Coriolis Torque VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/coriolis_torque.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/coriolis_torque.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Coriolis Torque VI

**Owning Palette:** [Dynamics VIs](../lvrobovi/dynamics_pal.html)

**Requires:** Robotics Module

Calculates the joint torques that result from the Coriolis and centripetal forces on the joints of a robotic arm. Wire data to the **joint positions** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

**.m file:** [coriolis](robotic_arm_pal.html#details)

#### Coriolis Torque (Point)

Use this instance to calculate values at a single point.

[IMAGE alt='image' src='coriolis_torque_point.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | joint positions specifies the joint angles that make up the robotic arm pose for which you want to calculate the solution. |
|  | joint velocities specifies the velocity of each joint in joint positions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | torques contains the torque vectors that result at each joint in joint positions. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Coriolis Torque (Trajectory)

Use this instance to calculate values at points along a trajectory.

[IMAGE alt='image' src='coriolis_torque_trajectory.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | joint position trajectory specifies the joint angles of the robotic arm pose at points along a trajectory where each row represents a pose at a particular time and each column represents a particular joint. |
|  | joint velocity trajectory specifies the velocity of each joint in joint position trajectory. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | torque trajectory contains the torque vectors at each element of joint position trajectory. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/create_directed_graph.html language=enus -->
## TOPIC 00201: Create Directed Graph Map VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/create_directed_graph.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/create_directed_graph.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Create Directed Graph Map VI

**Owning Palette:** [Directed Graph Map VIs](../lvrobovi/directed_graph_pal.html)

**Requires:** Robotics Module

Generates a map of the robot environment that consists of irregularly spaced points, or **nodes**.

[Example](#examples)

[IMAGE alt='image' src='create_directed_graph_map.gif']

|  | nodes defines points within the directed graph map. name assigns a name to the map node. For this VI to operate on a specific node, the node must have a unique name. coordinates specifies the position of the node within the directed graph map. The number of elements in coordinates corresponds to the number of dimensions in the robot environment you want to represent. For example, most ground robots can move to a point at given x- and y-coordinates, in which case coordinates contains two elements. As the number of dimensions you define within a map increases, so does the time required to calculate a path through the map. However, a path through a map with three dimensions might be more optimal than a path between the same points through a map with two dimensions because more movements are possible in the former map. |
| --- | --- |
|  | name assigns a name to the map node. For this VI to operate on a specific node, the node must have a unique name. |
|  | coordinates specifies the position of the node within the directed graph map. The number of elements in coordinates corresponds to the number of dimensions in the robot environment you want to represent. For example, most ground robots can move to a point at given x- and y-coordinates, in which case coordinates contains two elements. As the number of dimensions you define within a map increases, so does the time required to calculate a path through the map. However, a path through a map with three dimensions might be more optimal than a path between the same points through a map with two dimensions because more movements are possible in the former map. |
|  | heuristic function specifies the heuristic with which to calculate distances in the map. 0Euclidean Distance (default)—Defines the distance between two points as the square root of the sum of the squares of the differences between the corresponding coordinates of the points.1Manhattan Distance—Defines the distance between two points as the sum of the absolute differences of their coordinates. This option is useful when movement is possible only in the x and y directions. |
| 0 | Euclidean Distance (default)—Defines the distance between two points as the square root of the sum of the squares of the differences between the corresponding coordinates of the points. |
| 1 | Manhattan Distance—Defines the distance between two points as the sum of the absolute differences of their coordinates. This option is useful when movement is possible only in the x and y directions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | map reference out is a reference to the map that represents the robot environment. You can wire this output to other Path Planning VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Astar on Voronoi.lvproj in the labview\examples\robotics\Path Planning\Astar\Astar on Voronoi Graph directory for an example of using the Create Directed Graph Map VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/directed_graph_pal.html language=enus -->
## TOPIC 00202: Directed Graph Map VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/directed_graph_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/directed_graph_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Directed Graph Map VIs

**Owning Palette:** [Path Planning VIs](../lvrobovi/path_planning_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Directed Graph Map VIs to create and control a map, implemented as a directed graph, through which a mobile robot can navigate.

[Example](#examples)

Directed graph maps are useful for representing large robot environments that are not completely defined because you must define only known points, or nodes, in the map rather than the entire map.

|  | Note The VIs on this palette cannot execute at the same time. Enforce data dependency between these VIs to ensure they do not run simultaneously. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Add Node | Adds a unique point, or node, to a map at the coordinates you specify. |
| Close Directed Graph Map | Closes an open reference to a directed graph map object. |
| Create Directed Graph Map | Generates a map of the robot environment that consists of irregularly spaced points, or nodes. |
| Enqueue Change to Edge Cost | Requests that LabVIEW set the cost of traversing the area of the directed graph map between start node and end node to the value you specify. |
| Get All Nodes | Returns the names and coordinates of all nodes defined in a map. |
| Get Edge Cost | Returns the cost of traversing the edge, or area, of the directed graph map between start node and end node. |
| Get Node | Returns the coordinates of a map node in map reference in. You can use this VI to verify that a particular node exists or to return node coordinates you can plot. |
| Get Node Reference | Returns a reference to the map node you specify. |
| Get Nodes in Path | Returns the names and coordinates of the nodes along a path through a directed graph map. |

#### Example

Refer to the Astar on Voronoi.lvproj in the labview\examples\robotics\Path Planning\Astar\Astar on Voronoi Graph directory for an example of using the Directed Graph Map VIs.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/divide_quaternions.html language=enus -->
## TOPIC 00203: Divide Quaternions VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/divide_quaternions.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/divide_quaternions.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Divide Quaternions VI

**Owning Palette:** [Quaternions VIs](../lvrobovi/quaternion_pal.html)

**Requires:** Robotics Module

Computes the **quotient** of two quaternions or a quaternion and a scalar number. Wire data to the **y** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Divide Quaternion by Quaternion

[IMAGE alt='image' src='divide_quaternion_by_quaternion.gif']

|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | y is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
|  | quotient is the quotient of quaternion divided by y. |

#### Divide Quaternion by Scalar

[IMAGE alt='image' src='divide_quaternion_by_scalar.gif']

|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | y is a scalar number. |
|  | quotient is the quotient of quaternion divided by y. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/draw_steering_frame.html language=enus -->
## TOPIC 00204: Draw Steering Frame Picture VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/draw_steering_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/draw_steering_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Draw Steering Frame Picture VI

**Owning Palette:** [Steering VIs](../lvrobovi/steering_pal.html)

**Requires:** Robotics Module

Creates an image you can wire to a [2D picture control](/csh?topicname=lvconcepts/using_the_picture_indicator.html) to visualize a steering frame on the front panel. The picture can display data about the directions and velocities at which wheels move.

[Examples](#examples)

[IMAGE alt='image' src='draw_steering_frame_picture.gif']

|  | drawing options configures details of how the steering frame picture appears. draw wheel states? specifies whether to draw changes to the steering angle of wheels. LabVIEW ignores this input for wheels with fixed steering angles. highlight wheel index specifies the index number of a wheel you want to highlight in blue in the picture. The default is –1, which means this VI does not highlight a wheel. pixels per unit specifies the number of pixels to draw to represent one unit of measurement. For example, you might specify to draw the robot at a size of 400 pixels per inch. draw forward velocity? specifies whether to draw arrows that represent the direction and magnitude of the forward velocity of the robot. velocity scale specifies an amount by which to scale the arrows that represent forward velocity when draw forward velocity? is TRUE. This VI draws arrows of the length that corresponds to the pixels per unit you specify. The default is 1. |
| --- | --- |
|  | draw wheel states? specifies whether to draw changes to the steering angle of wheels. LabVIEW ignores this input for wheels with fixed steering angles. |
|  | highlight wheel index specifies the index number of a wheel you want to highlight in blue in the picture. The default is –1, which means this VI does not highlight a wheel. |
|  | pixels per unit specifies the number of pixels to draw to represent one unit of measurement. For example, you might specify to draw the robot at a size of 400 pixels per inch. |
|  | draw forward velocity? specifies whether to draw arrows that represent the direction and magnitude of the forward velocity of the robot. |
|  | velocity scale specifies an amount by which to scale the arrows that represent forward velocity when draw forward velocity? is TRUE. This VI draws arrows of the length that corresponds to the pixels per unit you specify. The default is 1. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | picture in is an existing picture control whose contents you want to display in picture out along with the steering frame picture this VI draws. |
|  | picture draw area size defines the size of the draw area in the picture control in terms of width and height in pixels. Use the Draw Area Size property to read these values from the picture control in which you want to display the steering frame picture and generate a cluster you can wire to this input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | steering frame position specifies the position of the steering frame drawing relative to the center of the picture control. x position specifies the x-coordinate of the center of the steering frame. A negative value represents a position to the left of the picture center, and a positive value represents a position to the right of the picture center. y position specifies the y-coordinate of the center of the steering frame. A negative value represents a position to the rear of the picture center, and a positive value represents a position to the front of the picture center. angle (rad) specifies the angle of the steering frame within the picture, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. An angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | x position specifies the x-coordinate of the center of the steering frame. A negative value represents a position to the left of the picture center, and a positive value represents a position to the right of the picture center. |
|  | y position specifies the y-coordinate of the center of the steering frame. A negative value represents a position to the rear of the picture center, and a positive value represents a position to the front of the picture center. |
|  | angle (rad) specifies the angle of the steering frame within the picture, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. An angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | picture out is the picture displaying the tree structure. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Draw Steering Frame Picture VI:

- labview\examples\robotics\Steering\Mecanum Steering\Mecanum Steering.lvproj
- labview\examples\robotics\Steering\Ackermann Steering\Ackermann Steering.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/extract_sentences.html language=enus -->
## TOPIC 00205: Extract Sentences VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/extract_sentences.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/extract_sentences.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Extract Sentences VI

**Owning Palette:** [NMEA Advanced VIs](../lvrobovi/nmea_advanced_pal.html)

**Requires:** Robotics Module

Returns complete NMEA sentences contained in **sensor data**.

[IMAGE alt='image' src='extract_sentences.gif']

|  | previous partial sentence contains characters to prepend to sensor data. |
| --- | --- |
|  | sensor data contains the data to parse for GPS data. This VI appends sensor data to previous partial sentence and then parses the data. Use a method of instrument control to acquire sensor data from a GPS receiver. For example, you can use VISA in LabVIEW to read NMEA sentences from a GPS receiver through a serial port and then parse the data with this VI. |
|  | filter for sentence type specifies the type of NMEA sentences this VI returns. This VI ignores sentences in previous partial sentence and sensor data of all other types. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | discarded data before first sentence contains all characters before the first sentence in sensor data. |
|  | remaining partial sentence contains all characters following the final sentence in complete sentences. To avoid losing this data, use this VI in a loop with shift registers to transfer remaining partial sentence to the previous partial sentence input on the next iteration of the loop. |
|  | complete sentences is an array of all valid NMEA sentences in sensor data. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | invalid sentences contains NMEA sentences with formatting errors, such as invalid checksums. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/get_grid_cells.html language=enus -->
## TOPIC 00206: Get All Occupancy Grid Cells VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/get_grid_cells.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/get_grid_cells.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get All Occupancy Grid Cells VI

**Owning Palette:** [Occupancy Grid Map VIs](../lvrobovi/occupancy_grid_pal.html)

**Requires:** Robotics Module

Returns an array of the cells in an occupancy grid map.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='get_all_occupancy_grid_cells.gif']

|  | map reference in is a reference to the map that represents the robot environment. Use the Create Occupancy Grid Map VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | map reference out is a reference to the map that represents the robot environment. You can wire this output to other Path Planning VIs. |
|  | occupancy grid contains the cost of entering each cell in the occupancy grid map from an adjacent cell. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get All Occupancy Grid Cells Details

|  | Note In the Occupancy Grid Map VIs, (x, y) coordinates that define the locations of cells are relative to the origin of the map, which is the cell at the bottom-left corner of the map. Refer to the Details section in the Create Occupancy Grid Map VI topic for more information about how (x, y) coordinate pairs map to cells in occupancy grid maps. |
| --- | --- |

#### Examples

Refer to the following VIs for examples of using the Get All Occupancy Grid Cells VI:

- labview\examples\robotics\Path Planning\ADstar\ADstar on Occupancy Grid\Anytime D Star on an Occupancy Grid.lvproj
- labview\examples\robotics\Path Planning\Astar\Astar on Occupancy Grid\Astar on Occupancy Grid.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/get_motor_setpoint.html language=enus -->
## TOPIC 00207: Get Motor Setpoint VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/get_motor_setpoint.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/get_motor_setpoint.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Motor Setpoint VI

**Owning Palette:** [Motor Communication VIs](../lvrobovi/motor_comm_pal.html)

**Requires:** Robotics Module

Returns the angles or angular velocity setpoints from the motor communication session. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

Use the [Update Motor State](../lvrobovi/update_motor_state.html) VI to apply the setpoints this VI returns to the motor or motors in the communication session.

#### Get Motor Angle Setpoint

[IMAGE alt='image' src='get_motor_angle_setpoint.gif']

|  | motor communication in is a reference to the communication session between a motor and the wheel the motor controls. Use the Initialize Motor Communication VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | motor communication out is a reference to the communication session between a motor and the wheel the motor controls. You can wire this output to other Motor Communication VIs. |
|  | angle returns the angle, in radians, of the motor shaft. |
|  | failed? is TRUE if this VI cannot calculate the motor setpoint, for example, because the value is undefined. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Motor Angle Setpoints

[IMAGE alt='image' src='get_motor_angle_setpoints.gif']

|  | motor communication in is an array of references to communication sessions between motors and the wheels the motors control. Use the Initialize Motor Communication VI to generate these LabVIEW class objects. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | motor communication out is an array of references to communication sessions between motors and the wheels the motors control. You can wire this output to other Motor Communication VIs. |
|  | angles returns the angles, in radians, of the motor shafts. |
|  | failed? is TRUE for a motor if this VI cannot calculate the motor setpoint, for example, because the value is undefined. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Motor Velocity Setpoint

[IMAGE alt='image' src='get_motor_velocity_setpoint.gif']

|  | motor communication in is a reference to the communication session between a motor and the wheel the motor controls. Use the Initialize Motor Communication VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | motor communication out is a reference to the communication session between a motor and the wheel the motor controls. You can wire this output to other Motor Communication VIs. |
|  | velocity returns the rate, in radians per second, at which the motor shaft rotates in the counterclockwise direction. |
|  | failed? is TRUE if this VI cannot calculate the motor setpoint, for example, because the value is undefined. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Motor Velocity Setpoints

[IMAGE alt='image' src='get_motor_velocity_setpoints.gif']

|  | motor communication in is an array of references to communication sessions between motors and the wheels the motors control. Use the Initialize Motor Communication VI to generate these LabVIEW class objects. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | motor communication out is an array of references to communication sessions between motors and the wheels the motors control. You can wire this output to other Motor Communication VIs. |
|  | velocities returns the rates, in radians per second, at which the motor shafts rotate in the counterclockwise direction. |
|  | failed? is TRUE for a motor if this VI cannot calculate the motor setpoint, for example, because the value is undefined. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/get_nmea_type.html language=enus -->
## TOPIC 00208: Get Sentence Type VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/get_nmea_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/get_nmea_type.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Sentence Type VI

**Owning Palette:** [NMEA Advanced VIs](../lvrobovi/nmea_advanced_pal.html)

**Requires:** Robotics Module

Returns the [type](../lvrobovi/nmea_advanced_pal.html#sentences) of an NMEA **sentence**. The first token following $ in an NMEA sentence is the **sentence type**. The type of a sentence defines the contents and interpretation of the sentence.

[IMAGE alt='image' src='get_sentence_type.gif']

|  | sentence is the sentence on which to operate. sentence must include valid NMEA formatting and end with a carriage return and line feed, or \\r\\n. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | sentence type returns the sentence type token in sentence. |
|  | valid sentence? returns TRUE if the NMEA sentence is formatted properly. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/get_node.html language=enus -->
## TOPIC 00209: Get Node VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/get_node.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/get_node.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Node VI

**Owning Palette:** [Directed Graph Map VIs](../lvrobovi/directed_graph_pal.html)

**Requires:** Robotics Module

Returns the coordinates of a map node in **map reference in**. You can use this VI to verify that a particular node exists or to return node **coordinates** you can plot.

[IMAGE alt='image' src='get_node.gif']

|  | map reference in is a reference to the map that represents the robot environment. Use the Create Directed Graph Map VI to generate this LabVIEW class object. |
| --- | --- |
|  | name specifies the name of the map node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | map reference out is a reference to the map that represents the robot environment. You can wire this output to other Path Planning VIs. |
|  | coordinates contains the position of the node within the directed graph map. |
|  | found? indicates whether the map defines the position of the node you specify. If the map does not define the node, LabVIEW does not return an error. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/get_node_reference.html language=enus -->
## TOPIC 00210: Get Node Reference VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/get_node_reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/get_node_reference.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Node Reference VI

**Owning Palette:** [Directed Graph Map VIs](../lvrobovi/directed_graph_pal.html)

**Requires:** Robotics Module

Returns a reference to the map node you specify.

You can wire the **node reference** this VI returns to the [Path Planning](../lvrobovi/path_planning_pal.html) VIs to specify the current or goal position of a robot navigating through a map.

[Example](#examples)

[IMAGE alt='image' src='get_node_reference.gif']

|  | map reference in is a reference to the map that represents the robot environment. Use the Create Directed Graph Map VI to generate this LabVIEW class object. |
| --- | --- |
|  | name specifies the name of the map node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | map reference out is a reference to the map that represents the robot environment. You can wire this output to other Path Planning VIs. |
|  | node reference contains a reference to the map node with the name you specify. You can wire this output to the Path Planning VIs. |
|  | found? indicates whether the map defines the position of the node you specify. If the map does not define the node, LabVIEW does not return an error. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Astar on Voronoi.lvproj in the labview\examples\robotics\Path Planning\Astar\Astar on Voronoi Graph directory for an example of using the Get Node Reference VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/kinematics_pal.html language=enus -->
## TOPIC 00211: Kinematics VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/kinematics_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/kinematics_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Kinematics VIs

**Owning Palette:** [Robotic Arm VIs](../lvrobovi/robotic_arm_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Kinematics VIs to calculate trajectories in joint or Cartesian space and to convert between the two.

| Palette Object | Description |
| --- | --- |
| Analytical Inverse Kinematics | Returns the joint angles of a 6R, 5R, or SCARA arm given the posture of the end effector relative to the arm base. Wire data to the X_serial arm in input, where X is the arm type, to determine the polymorphic instance to use or manually select the instance. |
| Forward Kinematics | Returns a homogenous transform or transforms that represents the position of a robotic arm end effector relative to the base of the arm. Wire data to the joint positions input to determine the polymorphic instance to use or manually select the instance. .m file: fkine |
| Generate Cartesian Trajectory | Generates a smooth trajectory of end effector positions between two points in Cartesian space. Wire data to the intermediate points input to determine the polymorphic instance to use or manually select the instance. .m file: ctraj |
| Generate Joint Trajectory | Generates joint angles, velocities, and accelerations along a smooth trajectory between two points in joint space. Wire data to the intermediate points input to determine the polymorphic instance to use or manually select the instance. .m file: jtraj |
| Inverse Kinematics | Computes the joint angles of a robotic arm given the location of the end effector relative to the arm base. Wire data to the end effector transform input to determine the polymorphic instance to use or manually select the instance. .m file: ikine |
| Manipulator Jacobian (End Effector Frame) | Generates a Jacobian matrix that transforms differential velocities in joint space to the Cartesian velocity of the end effector in the coordinate frame of the end effector. .m file: jacobn |
| Manipulator Jacobian (World Frame) | Generates a Jacobian matrix that transforms differential velocities in joint space to the Cartesian velocity of the end effector in the coordinate frame of the world. .m file: jacob0 |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/matrix_to_angle_vec.html language=enus -->
## TOPIC 00212: Rotation Matrix to Angle Vector VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/matrix_to_angle_vec.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/matrix_to_angle_vec.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Matrix to Angle Vector VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Converts a **rotation matrix** to the corresponding **angle** and **vector** by which the rotation occurs.

**.m file:** [tr2angvec](robotic_arm_pal.html#details)

[Example](#examples)

[IMAGE alt='image' src='rotation_matrix_to_angle_vector.gif']

|  | rotation matrix specifies a 3 × 3 matrix. |
| --- | --- |
|  | angle contains the angle, in radians, around vector by which the rotation occurs. |
|  | vector contains the x-, y-, and z-coordinates of the unit vector. |

#### Example

Refer to the Robot Arm Examples.lvproj in the labview\examples\robotics\Robotic Arm directory for an example of using the Rotation Matrix to Angle Vector VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/matrix_to_euler.html language=enus -->
## TOPIC 00213: Rotation Matrix to Euler Angles VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/matrix_to_euler.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/matrix_to_euler.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Matrix to Euler Angles VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Converts the **rotation matrix** you specify to Z, X, and Z Euler angles.

**.m file:** [tr2eul](robotic_arm_pal.html#details)

[IMAGE alt='image' src='rotation_matrix_to_euler_angles.gif']

|  | rotation matrix specifies a 3 × 3 matrix. |
| --- | --- |
|  | euler angles contains the Euler angles in radians. phi (Z) contains the first rotation angle about the z-axis in radians. theta (X) contains the rotation angle about the x-axis in radians. psi (Z) contains the second rotation angle about the z-axis in radians. |
|  | phi (Z) contains the first rotation angle about the z-axis in radians. |
|  | theta (X) contains the rotation angle about the x-axis in radians. |
|  | psi (Z) contains the second rotation angle about the z-axis in radians. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/matrix_to_quaternion.html language=enus -->
## TOPIC 00214: Rotation Matrix to Quaternion VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/matrix_to_quaternion.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/matrix_to_quaternion.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Matrix to Quaternion VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Converts a **rotation matrix** to the corresponding unit quaternion.

[IMAGE alt='image' src='rotation_matrix_to_quaternion.gif']

|  | rotation matrix specifies a 3 × 3 matrix. |
| --- | --- |
|  | quaternion contains a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/matrix_to_rpy_angles.html language=enus -->
## TOPIC 00215: Rotation Matrix to Roll Pitch Yaw VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/matrix_to_rpy_angles.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/matrix_to_rpy_angles.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Matrix to Roll Pitch Yaw VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Converts a **rotation matrix** to the corresponding **roll**, **pitch**, and **yaw** values.

**.m file:** [tr2rpy](robotic_arm_pal.html#details)

[IMAGE alt='image' src='rotation_matrix_to_roll_pitch_yaw.gif']

|  | rotation matrix specifies a 3 × 3 matrix. |
| --- | --- |
|  | angles returns the roll, pitch, and yaw values along those axes. roll contains the angle about the x-axis. pitch contains the angle about the y-axis. yaw contains the angle about the z-axis. |
|  | roll contains the angle about the x-axis. |
|  | pitch contains the angle about the y-axis. |
|  | yaw contains the angle about the z-axis. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/matrix_to_transform.html language=enus -->
## TOPIC 00216: Rotation Matrix to Transform VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/matrix_to_transform.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/matrix_to_transform.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotation Matrix to Transform VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Returns the transform that corresponds to the **rotation matrix** and **translation vector** you specify.

**.m file:** [r2t](robotic_arm_pal.html#details)

[IMAGE alt='image' src='rotation_matrix_to_transform.gif']

|  | rotation matrix specifies a 3 × 3 matrix. |
| --- | --- |
|  | translation vector defines the x, y, and z translation coordinates of transform. The default is [0, 0, 0]. |
|  | transform contains the 4 × 4 matrix homogenous transform that represents the values you specify. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/motor_comm_pal.html language=enus -->
## TOPIC 00217: Motor Communication VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/motor_comm_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/motor_comm_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Motor Communication VIs

**Owning Palette:** [Steering VIs](../lvrobovi/steering_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Motor Communication VIs to connect robot vehicle wheels to motors that control wheel angle and velocity. When you initiate a communication session between a wheel and the motor that controls the wheel, you can read and write motor data according to the position of the wheel as it moves.

| Palette Object | Description |
| --- | --- |
| Close Motor Communication | Terminates a communication session between a motor and the wheel the motor controls. Wire data to the motor communication in input to determine the polymorphic instance to use or manually select the instance. |
| Get Motor Setpoint | Returns the angles or angular velocity setpoints from the motor communication session. You must manually select the polymorphic instance to use. |
| Initialize Motor Communication | Begins a communication session for the motor that controls the wheel you specify. |
| Update Motor State | Writes angle or angular velocity values of the motor or motors to the motor communication session. You must manually select the polymorphic instance to use. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/move_wheels_in_frame.html language=enus -->
## TOPIC 00218: Reposition Wheels on Steering Frame VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/move_wheels_in_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/move_wheels_in_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Reposition Wheels on Steering Frame VI

**Owning Palette:** [Advanced VIs](../lvrobovi/steering_advanced_pal.html)

**Requires:** Robotics Module

Changes the location of the wheel or wheels to the position and angle you specify. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

#### Reposition Single Wheel in Steering Frame

[IMAGE alt='image' src='move_single_wheel_in_steering_frame.gif']

|  | x position specifies the x-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the left of the center, and a positive value represents a position to the right of the center. |
| --- | --- |
|  | y position specifies the y-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the rear of the center, and a positive value represents a position to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel index specifies the index of the wheel on which to operate, where 0 corresponds to the first wheel you added to the steering frame, 1 corresponds to the second wheel, and so on. The default is 0.If you specify an index value greater than the number of wheels steering frame in contains, LabVIEW returns FALSE in found? for the invalid index. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angle (rad) specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheel you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reposition Multiple Wheels in Steering Frame

[IMAGE alt='image' src='move_multiple_wheels_in_steering_frame.gif']

|  | x positions specifies the x-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. |
| --- | --- |
|  | y positions specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel indexes specifies the indexes of the wheels on which to operate, where 0 corresponds to the first wheel you added to the steering frame, 1 corresponds to the second wheel, and so on. If you do not specify wheel indexes, this VI returns all wheels on the steering frame.If you specify an index value greater than the number of wheels steering frame in contains, LabVIEW returns FALSE in found? for the invalid index. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angles (rad) specifies the angles of the wheel frames, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheels you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reposition Single Wheel in Steering Frame by Name

[IMAGE alt='image' src='move_single_wheel_in_steering_frame_by_name.gif']

|  | x position specifies the x-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the left of the center, and a positive value represents a position to the right of the center. |
| --- | --- |
|  | y position specifies the y-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the rear of the center, and a positive value represents a position to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel name specifies the identifier for the wheel. If you specify a name for a wheel that steering frame in does not contain, LabVIEW returns FALSE in found? for the invalid name. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angle (rad) specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheel you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reposition Multiple Wheels in Steering Frame by Name

[IMAGE alt='image' src='move_multiple_wheels_in_steering_frame_by_name.gif']

|  | x positions specifies the x-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. |
| --- | --- |
|  | y positions specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel names specifies the identifiers for the wheels. If you do not specify wheel names, this VI returns all wheels on the steering frame.If you specify a name for a wheel that steering frame in does not contain, LabVIEW returns FALSE in found? for the invalid name. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angles (rad) specifies the angles of the wheel frames, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheels you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/multiply_quaternions.html language=enus -->
## TOPIC 00219: Multiply Quaternions VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/multiply_quaternions.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/multiply_quaternions.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Multiply Quaternions VI

**Owning Palette:** [Quaternions VIs](../lvrobovi/quaternion_pal.html)

**Requires:** Robotics Module

Returns the **product** of two quaternions or a quaternion and a scalar number. Wire data to the **y** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Multiply Quaternion by Quaternion

[IMAGE alt='image' src='multiply_quaternion_by_quaternion.gif']

|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | y is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
|  | product is the product of quaternion multiplied by y. |

#### Multiply Quaternion by Scalar

[IMAGE alt='image' src='multiply_quaternion_by_scalar.gif']

|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
| --- | --- |
|  | y is a scalar number. |
|  | product is the product of quaternion multiplied by y. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/nmea_advanced_pal.html language=enus -->
## TOPIC 00220: NMEA Advanced VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/nmea_advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/nmea_advanced_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### NMEA Advanced VIs

**Owning Palette:** [NMEA Protocol VI](../lvrobovi/nmea_protocol_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the NMEA Advanced VIs to read data from GPS receivers and form and parse NMEA sentences.

| Palette Object | Description |
| --- | --- |
| Extract Sentences | Returns complete NMEA sentences contained in sensor data. |
| Form GPS Sentence | Creates an NMEA sentence using the data you specify for a particular sentence type. You must manually select the polymorphic instance to use. |
| Form Sentence | Creates an NMEA sentence formatted as the sentence type you specify and with the sentence data you specify. This VI also applies punctuation, a checksum, and termination characters to the sentence. |
| Get Sentence Parts | Returns an array of values contained in an NMEA sentence. |
| Get Sentence Type | Returns the type of an NMEA sentence. The first token following $ in an NMEA sentence is the sentence type. The type of a sentence defines the contents and interpretation of the sentence. |
| Parse GPS Sentence | Returns data contained in a particular type of NMEA sentence. The input sentence you specify must include valid NMEA formatting and end with a carriage return and line feed, or \\r\\n. You must manually select the polymorphic instance to use. |
| Validity Check | Specifies whether the formatting of an NMEA sentence is valid. |

#### Types of NMEA Sentences

The first token following $ in an NMEA sentence is the sentence type. The type of a sentence defines the contents and interpretation of the sentence. Sentence type tokens in GPS NMEA sentences are typically in the form of GPxxx, where xxx is the three-letter acronym of a type of GPS NMEA sentence.

Although many types of NMEA sentences exist, the Form GPS Sentence and Parse GPS Sentence VIs provide explicit support for creating and parsing a few common types of sentences. The following table describes the sentence types these VIs support.

| Sentence Type | Data Contained in Sentences |
| --- | --- |
| GGA | Time, position, and type of fix |
| GLL | Time, position, and status of fix |
| GSA | Type of fix, dilution of precision, and satellite data |
| GSV | Satellite data |
| RMC | Time, position, heading, and speed |
| VTG | Heading and speed relative to the ground |

Use the Form Sentence and Get Sentence Parts VIs to create and parse other types of sentences, respectively.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/nmea_protocol_pal.html language=enus -->
## TOPIC 00221: NMEA Protocol VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/nmea_protocol_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/nmea_protocol_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### NMEA Protocol VI

**Owning Palette:** [Protocols VIs](../lvrobovi/robo_protocols_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the NMEA Protocol VI to parse strings that contain GPS data for common GPS data points.

[Example](#examples)

This VI and the NMEA Advanced VIs generally can read and parse GPS data that is compatible with the National Marine Electronics Association (NMEA) standard. Many GPS receivers communicate data in the NMEA format, or NMEA sentences. National Instruments tested these VIs with common GPS receivers. However, National Instruments does not guarantee full support for any NMEA standard.

GPS NMEA sentences are formatted as shown in the following example:

$GPxxx,y<sub>0</sub>,y<sub>1</sub>,...,*zz\r\n, where xxx is the three-letter acronym of a [type](../lvrobovi/nmea_advanced_pal.html#sentences) of NMEA sentence, y<sub>0</sub>, y<sub>1</sub>, and so on are GPS data points, zz is a two-letter checksum, and \r\n are termination characters.

| Palette Object | Description |
| --- | --- |
| Get GPS Data | Parses sensor data in the NMEA format from GPS receivers and returns common GPS data, such as the latitude and longitude of a reading. |

| Subpalette | Description |
| --- | --- |
| NMEA Advanced VIs | Use the NMEA Advanced VIs to read data from GPS receivers and form and parse NMEA sentences. |

#### Example

Refer to the NMEA Get GPS Data From Record VI in the labview\examples\robotics\NMEA directory for an example of using the NMEA Protocol VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/obstacle_avoid_pal.html language=enus -->
## TOPIC 00222: Obstacle Avoidance VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/obstacle_avoid_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/obstacle_avoid_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Obstacle Avoidance VIs

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Obstacle Avoidance VIs to implement obstacle avoidance in mobile robot vehicles.

[Examples](#examples)

| Palette Object | Description |
| --- | --- |
| Advanced VFH | Identifies obstacles and gaps, or open areas, in the robot environment and returns an open direction for travel that best leads to a goal position. |
| Simple Vector Field Histogram | Identifies obstacles and gaps, or open areas, in the robot environment, which you can use to implement reactionary motion in a robot vehicle. |

#### Examples

Refer to the following VIs for examples of using the Obstacle Avoidance VIs:

- labview\examples\robotics\LIDAR Guided Robot\LIDAR Guided Robot.lvproj
- labview\examples\robotics\Simulated Mecanum Robot\Simulated Mecanum Robot.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/occupancy_grid_pal.html language=enus -->
## TOPIC 00223: Occupancy Grid Map VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/occupancy_grid_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/occupancy_grid_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Occupancy Grid Map VIs

**Owning Palette:** [Path Planning VIs](../lvrobovi/path_planning_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Occupancy Grid Map VIs to create and control an occupancy grid map through which a mobile robot can navigate. Occupancy grid maps are useful for representing robot environments in which you know the cost of traversing each point in the map.

[Examples](#examples)

Details

Create Occupancy Grid Map

|  | Note The VIs on this palette cannot execute at the same time. Enforce data dependency between these VIs to ensure they do not run simultaneously. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Close Occupancy Grid Map | Closes an open reference to an occupancy grid map object. |
| Create Occupancy Grid Map | Generates a map in the form of a grid of variables, or cells, that describe the robot environment. |
| Enqueue Change to Cell Cost | Requests that LabVIEW update the cost of entering the cell in the occupancy grid map at the x- and y-coordinates you specify. |
| Get All Occupancy Grid Cells | Returns an array of the cells in an occupancy grid map. |
| Get Cell Cost | Returns the cost of entering the cell in the occupancy grid map at the x- and y-coordinates you specify. |
| Get Cell Reference | Returns a reference to the cell in the occupancy grid map at the position you specify. |
| Get Cells in Path | Returns the cell coordinates of the points along a path through an occupancy grid map. |

#### Examples

Refer to the following VIs for examples of using the Occupancy Grid Map VIs:

- labview\examples\robotics\Path Planning\ADstar\ADstar on Occupancy Grid\Anytime D Star on an Occupancy Grid.lvproj
- labview\examples\robotics\Path Planning\Astar\Astar on Occupancy Grid\Astar on Occupancy Grid.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/parse_gps_sentence.html language=enus -->
## TOPIC 00224: Parse GPS Sentence VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/parse_gps_sentence.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/parse_gps_sentence.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Parse GPS Sentence VI

**Owning Palette:** [NMEA Advanced VIs](../lvrobovi/nmea_advanced_pal.html)

**Requires:** Robotics Module

Returns data contained in a particular [type of NMEA sentence](../lvrobovi/nmea_advanced_pal.html#sentences). The input sentence you specify must include [valid NMEA formatting](../lvrobovi/validity_check.html) and end with a carriage return and line feed, or \r\n. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

Use the [Get Sentence Parts](../lvrobovi/get_sentence_parts.html) VI to parse sentences of types this VI does not support.

#### Parse GGA Sentence

[IMAGE alt='image' src='parse_gga_sentence.gif']

|  | date override specifies a date on which the reading in the sentence occurs. By default, this VI assumes the reading occurs on the current date. |
| --- | --- |
|  | GGA sentence specifies the GGA NMEA sentence to parse into individual data points. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GGA data contains values from GGA sentence. time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. fix quality is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. quality defines the type and quality of the reading. 0Invalid1GPS Fix2DGPS Fix3PPS Fix4Real Time Kinematic5Float RTK6Estimated7Manual Input Mode8Simulation Mode number of satellites in view is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of satellites contains the total number of satellites from which you receive fixes. horizontal dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. altitude above mean sea level is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. altitude (m) contains the distance at which the reading occurs relative to the mean sea level. height of geoid above WGS84 is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. height of geoid (m) represents the distance of the mean ocean surface of the Earth above the ellipsoid, or reference surface, defined in the WGS 84 standard. time since last DGPS update is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (s) contains the elapsed time since the previous fix if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. DGPS station ID number is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. station ID number contains the identifier of the Differential Global Positioning System (DGPS) broadcast station from which the fix originates if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. |
|  | time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. |
|  | included? indicates whether the sentence contains this data point. |
|  | time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. |
|  | latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | included? indicates whether the sentence contains this data point. |
|  | latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | included? indicates whether the sentence contains this data point. |
|  | longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | fix quality is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. quality defines the type and quality of the reading. 0Invalid1GPS Fix2DGPS Fix3PPS Fix4Real Time Kinematic5Float RTK6Estimated7Manual Input Mode8Simulation Mode |
|  | included? indicates whether the sentence contains this data point. |
|  | quality defines the type and quality of the reading. 0Invalid1GPS Fix2DGPS Fix3PPS Fix4Real Time Kinematic5Float RTK6Estimated7Manual Input Mode8Simulation Mode |
| 0 | Invalid |
| 1 | GPS Fix |
| 2 | DGPS Fix |
| 3 | PPS Fix |
| 4 | Real Time Kinematic |
| 5 | Float RTK |
| 6 | Estimated |
| 7 | Manual Input Mode |
| 8 | Simulation Mode |
|  | number of satellites in view is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of satellites contains the total number of satellites from which you receive fixes. |
|  | included? indicates whether the sentence contains this data point. |
|  | number of satellites contains the total number of satellites from which you receive fixes. |
|  | horizontal dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | included? indicates whether the sentence contains this data point. |
|  | horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | altitude above mean sea level is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. altitude (m) contains the distance at which the reading occurs relative to the mean sea level. |
|  | included? indicates whether the sentence contains this data point. |
|  | altitude (m) contains the distance at which the reading occurs relative to the mean sea level. |
|  | height of geoid above WGS84 is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. height of geoid (m) represents the distance of the mean ocean surface of the Earth above the ellipsoid, or reference surface, defined in the WGS 84 standard. |
|  | included? indicates whether the sentence contains this data point. |
|  | height of geoid (m) represents the distance of the mean ocean surface of the Earth above the ellipsoid, or reference surface, defined in the WGS 84 standard. |
|  | time since last DGPS update is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (s) contains the elapsed time since the previous fix if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. |
|  | included? indicates whether the sentence contains this data point. |
|  | time (s) contains the elapsed time since the previous fix if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. |
|  | DGPS station ID number is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. station ID number contains the identifier of the Differential Global Positioning System (DGPS) broadcast station from which the fix originates if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. |
|  | included? indicates whether the sentence contains this data point. |
|  | station ID number contains the identifier of the Differential Global Positioning System (DGPS) broadcast station from which the fix originates if fix quality is DGPS Fix. If fix quality is not DGPS Fix, LabVIEW returns 0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parse GLL Sentence

[IMAGE alt='image' src='parse_gll_sentence.gif']

|  | date override specifies a date on which the reading in the sentence occurs. By default, this VI assumes the reading occurs on the current date. |
| --- | --- |
|  | GLL sentence specifies the GLL NMEA sentence to parse into individual data points. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GLL data contains values from GLL sentence. latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. status is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | included? indicates whether the sentence contains this data point. |
|  | latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | included? indicates whether the sentence contains this data point. |
|  | longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. |
|  | included? indicates whether the sentence contains this data point. |
|  | time (UTC) contains the UTC time at which the reading occurs. Unless you specify a value for date override, this VI assumes the reading occurs on the current date. |
|  | status is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. |
|  | included? indicates whether the sentence contains this data point. |
|  | value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. |
| 0 | Void—Specifies that the data is invalid. |
| 1 | Active—Specifies that the data is valid. |
|  | type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | included? indicates whether the sentence contains this data point. |
|  | mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
| 0 | Simulator |
| 1 | Not Valid |
| 2 | Estimated |
| 3 | Differential |
| 4 | Autonomous |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parse GSA Sentence

[IMAGE alt='image' src='parse_gsa_sentence.gif']

|  | GSA sentence specifies the GSA NMEA sentence to parse into individual data points. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GSA data contains values from GSA sentence. selection of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. selection of 2D or 3D fix describes the freedom of the receiver to move between modes. 0Automatic (default)—Allows the receiver to switch between operating in 2D and 3D mode.1Manual–Requires the receiver to operate in either 2D or 3D mode. type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode describes the mode in which the receiver obtains the fix. 1No Fix—Specifies that a satellite fix is unavailable.22D Fix—Specifies that data from three satellites defines the horizontal position of the receiver.33D Fix—Specifies that data from four or more satellites defines the absolute position of the receiver in space. satellite PRN numbers is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. PRN numbers contains the pseudo-random noise (PRN) numbers by which receivers identify the satellites. dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. DOP describes the overall quality of the reading. Factors that affect DOP include the distance between satellites and geographic obstructions between satellites and the receiver. Low DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. horizontal dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. vertical dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. vertical DOP describes the quality of the satellite reading with respect to values of altitude. Low vertical DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | selection of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. selection of 2D or 3D fix describes the freedom of the receiver to move between modes. 0Automatic (default)—Allows the receiver to switch between operating in 2D and 3D mode.1Manual–Requires the receiver to operate in either 2D or 3D mode. |
|  | included? indicates whether the sentence contains this data point. |
|  | selection of 2D or 3D fix describes the freedom of the receiver to move between modes. 0Automatic (default)—Allows the receiver to switch between operating in 2D and 3D mode.1Manual–Requires the receiver to operate in either 2D or 3D mode. |
| 0 | Automatic (default)—Allows the receiver to switch between operating in 2D and 3D mode. |
| 1 | Manual–Requires the receiver to operate in either 2D or 3D mode. |
|  | type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode describes the mode in which the receiver obtains the fix. 1No Fix—Specifies that a satellite fix is unavailable.22D Fix—Specifies that data from three satellites defines the horizontal position of the receiver.33D Fix—Specifies that data from four or more satellites defines the absolute position of the receiver in space. |
|  | included? indicates whether the sentence contains this data point. |
|  | mode describes the mode in which the receiver obtains the fix. 1No Fix—Specifies that a satellite fix is unavailable.22D Fix—Specifies that data from three satellites defines the horizontal position of the receiver.33D Fix—Specifies that data from four or more satellites defines the absolute position of the receiver in space. |
| 1 | No Fix—Specifies that a satellite fix is unavailable. |
| 2 | 2D Fix—Specifies that data from three satellites defines the horizontal position of the receiver. |
| 3 | 3D Fix—Specifies that data from four or more satellites defines the absolute position of the receiver in space. |
|  | satellite PRN numbers is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. PRN numbers contains the pseudo-random noise (PRN) numbers by which receivers identify the satellites. |
|  | included? indicates whether the sentence contains this data point. |
|  | PRN numbers contains the pseudo-random noise (PRN) numbers by which receivers identify the satellites. |
|  | dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. DOP describes the overall quality of the reading. Factors that affect DOP include the distance between satellites and geographic obstructions between satellites and the receiver. Low DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | included? indicates whether the sentence contains this data point. |
|  | DOP describes the overall quality of the reading. Factors that affect DOP include the distance between satellites and geographic obstructions between satellites and the receiver. Low DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | horizontal dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | included? indicates whether the sentence contains this data point. |
|  | horizontal DOP describes the quality of the reading with respect to values of latitude and longitude. Low horizontal DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | vertical dilution of precision is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. vertical DOP describes the quality of the satellite reading with respect to values of altitude. Low vertical DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | included? indicates whether the sentence contains this data point. |
|  | vertical DOP describes the quality of the satellite reading with respect to values of altitude. Low vertical DOP values indicate high precision, and a value of 1 indicates the precision of the reading is ideal. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parse GSV Sentence

[IMAGE alt='image' src='parse_gsv_sentence.gif']

|  | GSV sentence specifies the GSV NMEA sentence to parse into individual data points. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GSV data contains values from GSV sentence. number of sentences for full data is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of sentences contains the total number of sentences that define readings for all available satellites. A sentence can contain data for no more than four satellites. sentence index is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. index contains the number of the sentence to form. If index is greater than the number of sentences that is possible, LabVIEW returns a warning. number of satellites in view is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of satellites contains the total number of satellites from which you receive fixes. satellite data is a cluster that contains the following elements. included? displays whether the sentence contains this data point for each satellite. data is a cluster that contains the following elements. PRN number is the pseudo-random noise (PRN) number by which receivers identify the satellite. elevation (deg) contains the elevation of the satellite. azimuth (deg) contains the azimuth of the satellite. signal to noise ratio is a number between 0 and 99, specified in dB, that defines signal strength. |
|  | number of sentences for full data is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of sentences contains the total number of sentences that define readings for all available satellites. A sentence can contain data for no more than four satellites. |
|  | included? indicates whether the sentence contains this data point. |
|  | number of sentences contains the total number of sentences that define readings for all available satellites. A sentence can contain data for no more than four satellites. |
|  | sentence index is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. index contains the number of the sentence to form. If index is greater than the number of sentences that is possible, LabVIEW returns a warning. |
|  | included? indicates whether the sentence contains this data point. |
|  | index contains the number of the sentence to form. If index is greater than the number of sentences that is possible, LabVIEW returns a warning. |
|  | number of satellites in view is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. number of satellites contains the total number of satellites from which you receive fixes. |
|  | included? indicates whether the sentence contains this data point. |
|  | number of satellites contains the total number of satellites from which you receive fixes. |
|  | satellite data is a cluster that contains the following elements. included? displays whether the sentence contains this data point for each satellite. data is a cluster that contains the following elements. PRN number is the pseudo-random noise (PRN) number by which receivers identify the satellite. elevation (deg) contains the elevation of the satellite. azimuth (deg) contains the azimuth of the satellite. signal to noise ratio is a number between 0 and 99, specified in dB, that defines signal strength. |
|  | included? displays whether the sentence contains this data point for each satellite. |
|  | data is a cluster that contains the following elements. PRN number is the pseudo-random noise (PRN) number by which receivers identify the satellite. elevation (deg) contains the elevation of the satellite. azimuth (deg) contains the azimuth of the satellite. signal to noise ratio is a number between 0 and 99, specified in dB, that defines signal strength. |
|  | PRN number is the pseudo-random noise (PRN) number by which receivers identify the satellite. |
|  | elevation (deg) contains the elevation of the satellite. |
|  | azimuth (deg) contains the azimuth of the satellite. |
|  | signal to noise ratio is a number between 0 and 99, specified in dB, that defines signal strength. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parse RMC Sentence

[IMAGE alt='image' src='parse_rmc_sentence.gif']

|  | RMC sentence specifies the RMC NMEA sentence to parse into individual data points. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RMC data contains values from RMC sentence. time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. status is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. ground speed is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (knots) is the speed of the device at the time the reading occurred. true track angle is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. angle (deg) contains the direction of travel at the time the reading occurred with respect to true north. magnetic variation is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. variation (deg) contains the angle between the local magnetic field and true north. type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | time of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. time (UTC) contains the UTC time at which the reading occurs. |
|  | included? indicates whether the sentence contains this data point. |
|  | time (UTC) contains the UTC time at which the reading occurs. |
|  | status is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. |
|  | included? indicates whether the sentence contains this data point. |
|  | value describes whether the data is valid. 0Void—Specifies that the data is invalid.1Active—Specifies that the data is valid. |
| 0 | Void—Specifies that the data is invalid. |
| 1 | Active—Specifies that the data is valid. |
|  | latitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | included? indicates whether the sentence contains this data point. |
|  | latitude (deg) contains the location on Earth north or south of the equator at which the reading occurs. Positive values represent locations north of the equator, and negative values represent locations south of the equator. |
|  | longitude is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | included? indicates whether the sentence contains this data point. |
|  | longitude (deg) contains the location on Earth east or west of the prime meridian at which the reading occurs. Positive values represent locations east of the prime meridian, and negative values represent locations west of the prime meridian. |
|  | ground speed is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (knots) is the speed of the device at the time the reading occurred. |
|  | included? indicates whether the sentence contains this data point. |
|  | speed (knots) is the speed of the device at the time the reading occurred. |
|  | true track angle is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. angle (deg) contains the direction of travel at the time the reading occurred with respect to true north. |
|  | included? indicates whether the sentence contains this data point. |
|  | angle (deg) contains the direction of travel at the time the reading occurred with respect to true north. |
|  | magnetic variation is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. variation (deg) contains the angle between the local magnetic field and true north. |
|  | included? indicates whether the sentence contains this data point. |
|  | variation (deg) contains the angle between the local magnetic field and true north. |
|  | type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | included? indicates whether the sentence contains this data point. |
|  | mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
| 0 | Simulator |
| 1 | Not Valid |
| 2 | Estimated |
| 3 | Differential |
| 4 | Autonomous |
|  | error out contains error information. This output provides standard error out functionality. |

#### Parse VTG Sentence

[IMAGE alt='image' src='parse_vtg_sentence.gif']

|  | VTG sentence specifies the VTG NMEA sentence to parse into individual data points. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VTG data contains values from VTG sentence. true track made good is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. true track made good (deg) contains the direction of travel with respect to true north. magnetic track made good is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. magnetic track made good (deg) contains the direction of travel with respect to the local magnetic field. ground speed (knots) is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (knots) is the speed of the device at the time the reading occurred. ground speed (km/h) is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (km/h) is the speed of the device at the time the reading occurred. type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | true track made good is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. true track made good (deg) contains the direction of travel with respect to true north. |
|  | included? indicates whether the sentence contains this data point. |
|  | true track made good (deg) contains the direction of travel with respect to true north. |
|  | magnetic track made good is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. magnetic track made good (deg) contains the direction of travel with respect to the local magnetic field. |
|  | included? indicates whether the sentence contains this data point. |
|  | magnetic track made good (deg) contains the direction of travel with respect to the local magnetic field. |
|  | ground speed (knots) is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (knots) is the speed of the device at the time the reading occurred. |
|  | included? indicates whether the sentence contains this data point. |
|  | speed (knots) is the speed of the device at the time the reading occurred. |
|  | ground speed (km/h) is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. speed (km/h) is the speed of the device at the time the reading occurred. |
|  | included? indicates whether the sentence contains this data point. |
|  | speed (km/h) is the speed of the device at the time the reading occurred. |
|  | type of fix is a cluster that contains the following elements. included? indicates whether the sentence contains this data point. mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
|  | included? indicates whether the sentence contains this data point. |
|  | mode contains the mode in which the receiver obtains the fix and indicates signal integrity. For example, the Differential and Autonomous modes correspond to active, reliable readings. 0Simulator1Not Valid2Estimated3Differential4Autonomous |
| 0 | Simulator |
| 1 | Not Valid |
| 2 | Estimated |
| 3 | Differential |
| 4 | Autonomous |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/quaternion_pal.html language=enus -->
## TOPIC 00225: Quaternions VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/quaternion_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/quaternion_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Quaternions VIs

**Owning Palette:** [Robotic Arm VIs](../lvrobovi/robotic_arm_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Quaternions VIs to perform quaternion math for use in robotic kinematics.

**.m file:** [quaternion](robotic_arm_pal.html#details)

| Palette Object | Description |
| --- | --- |
| Add Quaternions | Returns the sum of two quaternions. |
| Conjugate Quaternion | Returns the conjugate of a quaternion. |
| Divide Quaternions | Computes the quotient of two quaternions or a quaternion and a scalar number. Wire data to the y input to determine the polymorphic instance to use or manually select the instance. |
| Generate Random Quaternion | Returns a quaternion whose elements are between –1 and 1. |
| Get Unit Quaternion | Computes the unit quaternion of a quaternion. .m file: unit |
| Interpolate Quaternions | Returns a quaternion that is a spherical linear interpolation between two quaternions. .m file: qinterp |
| Inverse Quaternion | Returns the inverse of a quaternion. .m file: inv |
| Multiply Quaternions | Returns the product of two quaternions or a quaternion and a scalar number. Wire data to the y input to determine the polymorphic instance to use or manually select the instance. |
| Normalize Quaternion | Returns the norm of the input quaternion. This VI uses the Vector Norm VI to compute the norm. .m file: norm |
| Rotate Vector by Quaternion | Rotates a vector. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/replace_wheels_frame.html language=enus -->
## TOPIC 00226: Replace Wheels in Steering Frame VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/replace_wheels_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/replace_wheels_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Replace Wheels in Steering Frame VI

**Owning Palette:** [Advanced VIs](../lvrobovi/steering_advanced_pal.html)

**Requires:** Robotics Module

Replaces wheels in **steering frame in** with the wheels you specify. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

[Details](#details)

#### Replace Single Wheel in Steering Frame

[IMAGE alt='image' src='replace_single_wheel_in_steering_frame.gif']

|  | x position specifies the x-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the left of the center, and a positive value represents a position to the right of the center. |
| --- | --- |
|  | y position specifies the y-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the rear of the center, and a positive value represents a position to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel index specifies the index of the wheel on which to operate, where 0 corresponds to the first wheel you added to the steering frame, 1 corresponds to the second wheel, and so on. If you specify an index value greater than the number of wheels steering frame in contains, LabVIEW returns FALSE in found? for the invalid index. |
|  | wheel is a reference to a steering frame wheel. Use the Create Wheel VI to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angle (rad) specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheel you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Replace Multiple Wheels in Steering Frame

[IMAGE alt='image' src='replace_multiple_wheels_in_steering_frame.gif']

|  | x positions specifies the x-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. |
| --- | --- |
|  | y positions specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel indexes specifies the indexes of the wheels on which to operate, where 0 corresponds to the first wheel you added to the steering frame, 1 corresponds to the second wheel, and so on. If you specify an index value greater than the number of wheels steering frame in contains, LabVIEW returns FALSE in found? for the invalid index. |
|  | wheels contains an array of references to steering frame wheels. Use the Create Wheel VI to generate these LabVIEW class objects. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angles (rad) specifies the angles of the wheel frames, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheels you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Replace Single Wheel in Steering Frame by Name

[IMAGE alt='image' src='replace_single_wheel_in_steering_frame_by_name.gif']

|  | x position specifies the x-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the left of the center, and a positive value represents a position to the right of the center. |
| --- | --- |
|  | y position specifies the y-coordinate of the wheel with respect to the center of the steering frame. A negative value represents a position to the rear of the center, and a positive value represents a position to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel name specifies the identifier for the wheel. If you specify a name for a wheel that steering frame in does not contain, LabVIEW returns FALSE in found? for the invalid name. |
|  | wheel is a reference to a steering frame wheel. Use the Create Wheel VI to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angle (rad) specifies the angle of the wheel frame, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheel you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Replace Multiple Wheels in Steering Frame by Name

[IMAGE alt='image' src='replace_multiple_wheels_in_steering_frame_by_name.gif']

|  | x positions specifies the x-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the left of the center, and positive values represent positions to the right of the center. |
| --- | --- |
|  | y positions specifies the y-coordinates of the wheels with respect to the center of the steering frame. Negative values represent positions to the rear of the center, and positive values represent positions to the front of the center. |
|  | steering frame in is a reference to the steering frame on which to operate. Use the Create Steering Frame VI to generate this LabVIEW class object. |
|  | wheel names specifies the identifiers for the wheels. If you specify a name for a wheel that steering frame in does not contain, LabVIEW returns FALSE in found? for the invalid name. |
|  | wheels contains an array of references to steering frame wheels. Use the Create Wheel VI to generate these LabVIEW class objects. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | frame angles (rad) specifies the angles of the wheel frames, measured counterclockwise from the direction of forward travel of the steering frame as viewed from above. A frame angle of 0 is parallel to the direction of forward travel of the steering frame. |
|  | steering frame out is a reference to the steering frame. You can wire this output to other Steering VIs. |
|  | found? indicates whether steering frame in contains the wheel you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Replace Wheels in Steering Frame Details

When use the Steering VIs to create and operate on a steering frame, always use a consistent unit of measurement when you specify values that represent distance.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_lidar_pal.html language=enus -->
## TOPIC 00227: Laser Range Finders Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_lidar_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_lidar_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Laser Range Finders Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Laser Range Finders drivers to [communicate](../lvrobogsm/robo_prog_sensors.html) with light detection and ranging (LIDAR) devices.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_receivers_pal.html language=enus -->
## TOPIC 00228: Infrared Receivers Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_receivers_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_receivers_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Infrared Receivers Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

communicate

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_rfid_pal.html language=enus -->
## TOPIC 00229: RFID Devices Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_rfid_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_rfid_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### RFID Devices Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the RFID Devices drivers to [communicate](../lvrobogsm/robo_prog_sensors.html) with radio-frequency identification (RFID) readers/writers.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_rotary_pos_pal.html language=enus -->
## TOPIC 00230: Absolute Rotary Position Sensors Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_rotary_pos_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_rotary_pos_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Absolute Rotary Position Sensors Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

communicate

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_simdrivers_pal.html language=enus -->
## TOPIC 00231: Device I/O with Simulation Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_simdrivers_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_simdrivers_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Device I/O with Simulation Drivers

**Owning Palette:** [Sensors and Actuators Drivers](../lvrobovi/sensing_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Device I/O with Simulation drivers to configure and [control real or simulated sensors and actuators](../lvrobogsm/robo_prog_sensors.html). Use the [initialization VI](../lvrobogsm/robo_prog_sensors.html#initialize) appropriate for your application to select the type of connection the driver implements.

Use the [Device I/O](../lvrobovi/robo_drivers_pal.html) drivers if you do not need to use a driver in a simulator application and you do not need the ability to switch the connection type.

| Subpalette | Description |
| --- | --- |
| Absolute Rotary Position Sensors Drivers | Use the Absolute Rotary Position Sensors drivers to communicate with devices that perform absolute rotary position detection. |
| Ambient Light Sensors Drivers | Use the Ambient Light Sensors drivers to communicate with devices that perform ambient light detection. |
| Electronic Compasses Drivers | Use the Electronic Compasses drivers to communicate with electronic compasses. |
| Encoders Drivers | Use the Encoders drivers to communicate with encoders. |
| Force Sensors Drivers | Use the Force Sensors drivers to communicate with devices that perform force detection. |
| GPS Receivers Drivers | Use the GPS Receivers drivers to communicate with GPS receivers. |
| Inertial Measurement Devices Drivers | Use the Inertial Measurement Devices drivers to communicate with devices that measure characteristics of motion and orientation. |
| Infrared Range Finders Drivers | Use the Infrared Range Finders drivers to communicate with devices that perform infrared range detection. |
| Infrared Receivers Drivers | Use the Infrared Receivers drivers to communicate with infrared receivers. |
| Laser Range Finders Drivers | Use the Laser Range Finders drivers to communicate with light detection and ranging (LIDAR) devices. |
| Motors Drivers | Use the Motors drivers to communicate with servos and motor controllers. |
| RFID Devices Drivers | Use the RFID Devices drivers to communicate with radio-frequency identification (RFID) readers/writers. |
| Sonar Range Finders Drivers | Use the Sonar Range Finders drivers to communicate with devices that perform sonar range detection. |
| Thermal Devices Drivers | Use the Thermal Devices drivers to communicate with devices that perform thermal detection. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_sonar_pal.html language=enus -->
## TOPIC 00232: Sonar Range Finders Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_sonar_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_sonar_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Sonar Range Finders Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Sonar Range Finders drivers to [communicate](../lvrobogsm/robo_prog_sensors.html) with devices that perform sonar range detection.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_thermal_pal.html language=enus -->
## TOPIC 00233: Thermal Devices Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_thermal_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_thermal_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Thermal Devices Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html), [Device I/O with Simulation Drivers](../lvrobovi/robo_simdrivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Thermal Devices drivers to [communicate](../lvrobogsm/robo_prog_sensors.html) with devices that perform thermal detection.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_tts_pal.html language=enus -->
## TOPIC 00234: Text to Speech Devices Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_tts_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_tts_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Text to Speech Devices Drivers

**Owning Palette:** [Device I/O Drivers](../lvrobovi/robo_drivers_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Text to Speech Devices drivers to [communicate](../lvrobogsm/robo_prog_sensors.html) with devices that convert text into spoken words.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robo_update_plot.html language=enus -->
## TOPIC 00235: Update Plot VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robo_update_plot.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robo_update_plot.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Update Plot VI

**Owning Palette:** [Plots VIs](../lvrobovi/robo_plots_pal.html)

**Requires:** Robotics Module

Returns a 3D scene with the 3D object that represents a robotic arm. You must use the [Initialize Plot](../lvrobovi/robo_init_plot.html) VI to initialize the 3D object before you call this VI for the first time.

You can use this VI in a [loop with shift registers](/csh?topicname=lvconcepts/shift_registers_feedback_node.html) to update the **joint positions** of the robotic arm in the 3D object and display the motion of the arm between poses.

[Examples](#examples)

[IMAGE alt='image' src='update_plot.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | joint positions contains the joint angles with which to update the 3D object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | serial arm scene returns a reference to the 3D scene object that contains the simulated robotic arm. Wire this output to the 3D picture control to add a 3D picture control to the front panel window and view the 3D scene. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Update Plot VI:

- labview\examples\robotics\Robotic Arm\Robot Arm Examples.lvproj
- labview\examples\robotics\Simulator\Puma560\Puma560 Simulator.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robotic_arm_pal.html language=enus -->
## TOPIC 00236: Robotic Arm VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robotic_arm_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robotic_arm_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Robotic Arm VIs

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Robotic Arm VIs to [design and control a serial robotic arm](../lvrobogsm/robo_arm_concepts.html). You can perform dynamic and [kinematic calculations](../lvrobogsm/robo_arm_concepts.html#kinematics) on an arm, simulate an arm, and so on to prototype the robotic arm.

|  | Note Always use consistent units of measurement when you wire values that represent distance, velocity, and acceleration to the inputs of these VIs. The Robotic Arm VIs can operate on any metric unit of measurement. |
| --- | --- |

| Subpalette | Description |
| --- | --- |
| Dynamics VIs | Use the Dynamics VIs to calculate the forces that act on a robotic arm or to calculate the forces required to move an arm according to the conditions you specify. |
| Homogenous Transforms VIs | Use the Homogenous Transforms VIs to convert between transforms, quaternions, and angle representations. |
| Kinematics VIs | Use the Kinematics VIs to calculate trajectories in joint or Cartesian space and to convert between the two. |
| Plots VIs | Use the Plots VIs to create and display a representation of a robotic arm. |
| Quaternions VIs | Use the Quaternions VIs to perform quaternion math for use in robotic kinematics. |
| Serial Arm Definition VIs | Use the Serial Arm Definition VIs to design and generate a serial robotic arm. To design an arm, you define the parameters of the links and joints that make up the arm. |

#### Robotic Arm VI Details

National Instruments developed the Robotic Arm VIs using, in part, code provided by Peter Corke and derived many of these VIs from his Robotics Toolbox. These VIs correspond to .m files in the Robotics Toolbox where noted. The Robotics Toolbox is made available at no charge at www.petercorke.com/robot by a party not affiliated with, or sponsored or endorsed by, NI. NI is not responsible for the content of the Web site or the Robotics Toolbox.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/robotics_pal.html language=enus -->
## TOPIC 00237: Robotics VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/robotics_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/robotics_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Robotics VIs

June 2014, 372985F-01

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Robotics VIs to design algorithms and applications that you can deploy to embedded robotic systems.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [Robotics error codes](../lvrobogsm/robo_error_codes.html).

|  | Note Refer to the KnowledgeBase at ni.com for information about the deterministic characteristics of the Robotics VIs. |
| --- | --- |

| Subpalette | Description |
| --- | --- |
| Connectivity VIs | Use the items on the Connectivity palette to access VIs that interface with other robotics software, including third-party products. |
| KUKA youBot VIs | Use the KUKA youBot VIs to design and control a KUKA youBot. |
| Obstacle Avoidance VIs | Use the Obstacle Avoidance VIs to implement obstacle avoidance in mobile robot vehicles. |
| Path Planning VIs | Use the Path Planning VIs to calculate a path to a goal point in a map that represents the robot environment. |
| Protocols VIs | Use the Protocols VIs to process data formatted in communication protocols, such as data sent by sensors, in LabVIEW. |
| Robotic Arm VIs | Use the Robotic Arm VIs to design and control a serial robotic arm. You can perform dynamic and kinematic calculations on an arm, simulate an arm, and so on to prototype the robotic arm. |
| Sensors and Actuators Drivers | Use the Sensors and Actuators drivers to configure and control sensors and actuators commonly used in robotics systems. Browse the Instrument I/O palette to find other drivers you can use. Use the NI Instrument Driver Finder to search for and install additional drivers. |
| Simulator VIs | Use the Simulator VIs to control the robotics simulator and interact with components in a robotics simulation. |
| Starter Kit VIs | Use the VIs on the subpalette that corresponds to your LabVIEW Robotics Starter Kit robot to control the robot without writing an FPGA VI. |
| Steering VIs | Use the Steering VIs to create a mobile robotics system that consists of a built-in or user-defined steering frame and wheels. You can calculate and convert between robot and wheel velocity and connect with motors that drive wheels to implement motor control. |

© 2009–2014 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/rotate_vector_quatn.html language=enus -->
## TOPIC 00238: Rotate Vector by Quaternion VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/rotate_vector_quatn.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/rotate_vector_quatn.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Rotate Vector by Quaternion VI

**Owning Palette:** [Quaternions VIs](../lvrobovi/quaternion_pal.html)

**Requires:** Robotics Module

Rotates a vector.

[IMAGE alt='image' src='rotate_vector_by_quaternion.gif']

|  | vector specifies the x-, y-, and z-coordinates of the point around which to rotate. |
| --- | --- |
|  | quaternion is a four-element array whose elements specify the scalar and three-element vector parts of a quaternion. |
|  | rotated vector contains vector rotated by quaternion. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/rpy_angle_to_matrix.html language=enus -->
## TOPIC 00239: Roll Pitch Yaw to Rotation Matrix VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/rpy_angle_to_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/rpy_angle_to_matrix.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Roll Pitch Yaw to Rotation Matrix VI

**Owning Palette:** [Homogenous Transforms VIs](../lvrobovi/transforms_pal.html)

**Requires:** Robotics Module

Converts **roll**, **pitch**, and **yaw** angles to the corresponding **rotation matrix**.

**.m file:** [rpy2r](robotic_arm_pal.html#details)

[IMAGE alt='image' src='roll_pitch_yaw_to_rotation_matrix.gif']

|  | angles specifies the roll, pitch, and yaw values along those axes. roll specifies the angle about the x-axis. pitch specifies the angle about the y-axis. yaw specifies the angle about the z-axis. |
| --- | --- |
|  | roll specifies the angle about the x-axis. |
|  | pitch specifies the angle about the y-axis. |
|  | yaw specifies the angle about the z-axis. |
|  | rotation matrix contains the 3 × 3 matrix that represents the rotation. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sensing_pal.html language=enus -->
## TOPIC 00240: Sensors and Actuators Drivers

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sensing_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sensing_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Sensors and Actuators Drivers

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Sensors and Actuators drivers to configure and control sensors and actuators commonly used in robotics systems. Browse the [Instrument I/O](/csh?topicname=lvinstio/inst_i_o_vi_and_func_descr.html) palette to find other drivers you can use. Use the [NI Instrument Driver Finder](/csh?topicname=lvdialog/id_finder.html) to search for and install additional drivers.

(Control Design and Simulation Module) You can use the [Estimation](/csh?topicname=lvsim/estimation_vis.html) functions to implement Kalman filters that perform sensor fusion of data.

| Subpalette | Description |
| --- | --- |
| Device I/O Drivers | Use the Device I/O drivers to configure and control sensors and actuators commonly used in robotics systems. You cannot use these drivers in a simulation application. |
| Device I/O with Simulation Drivers | Use the Device I/O with Simulation drivers to configure and control real or simulated sensors and actuators. Use the initialization VI appropriate for your application to select the type of connection the driver implements. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/set_base.html language=enus -->
## TOPIC 00241: Set Base Transform VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/set_base.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/set_base.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Set Base Transform VI

**Owning Palette:** [Serial Arm Definition VIs](../lvrobovi/serial_arm_def_pal.html)

**Requires:** Robotics Module

Sets the position of the base of a robotic arm.

[Example](#examples)

[IMAGE alt='image' src='set_base_transform.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | base transform specifies the homogenous transform that describes the base of the robotic arm. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Puma560 Simulator.lvproj in the labview\examples\robotics\Simulator\Puma560 directory for an example of using the Set Base Transform VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/set_tool.html language=enus -->
## TOPIC 00242: Set End Effector Transform VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/set_tool.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/set_tool.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Set End Effector Transform VI

**Owning Palette:** [Serial Arm Definition VIs](../lvrobovi/serial_arm_def_pal.html)

**Requires:** Robotics Module

Sets the position of the end effector of a robotic arm.

[Example](#examples)

[IMAGE alt='image' src='set_end_effector_transform.gif']

|  | serial arm in is a reference to a serial robotics arm. Use the Initialize Serial Arm VI to generate this LabVIEW class object. |
| --- | --- |
|  | end effector transform specifies the homogenous transform that represents the position of the end effector with respect to the adjacent link. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | serial arm out is a reference to a serial robotic arm. You can wire this output to other Robotic Arm VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Puma560 Simulator.lvproj in the labview\examples\robotics\Simulator\Puma560 directory for an example of using the Set End Effector Transform VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_load_instance.html language=enus -->
## TOPIC 00243: Load Simulation Instance VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_load_instance.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_load_instance.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Load Simulation Instance VI

**Owning Palette:** [Offline Configuration VIs](../lvrobovi/simulator_config_pal.html)

**Requires:** Robotics Module

Returns a reference to a simulation instance defined in a manifest file. Use the reference with Property Nodes to [access and edit components in the simulation instance](../lvrobogsm/robo_sim_creating.html#modify_instance).

[IMAGE alt='image' src='load_simulation_instance.gif']

|  | manifest file specifies the absolute path to the .xml manifest file that defines the simulation instance. If you specify an invalid path, LabVIEW returns error code –310200. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | simulation instance returns the simulation instance component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_new_object.html language=enus -->
## TOPIC 00244: New Simulation Object VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_new_object.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_new_object.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### New Simulation Object VI

**Owning Palette:** [Offline Configuration VIs](../lvrobovi/simulator_config_pal.html)

**Requires:** Robotics Module

[Creates a new component for use in a robotics simulation scene](../lvrobogsm/robo_sim_creating.html#offlineconfig) you can render in the robotics simulator. After you use this VI to create a component, wire the output to a [Property Node (Simulation Engine)](../lvrobovi/sim_prop_node.html) to access and define attributes of the component.

When you finish defining components, prepare to [save them in a manifest file](../lvrobogsm/robo_sim_creating.html#offlineconfig).

[Example](#examples)

#### New Simulation Instance

[IMAGE alt='image' src='new_simulation_instance.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | simulation instance returns the simulation instance component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Environment

[IMAGE alt='image' src='new_environment.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | environment returns the environment component. Wire this reference to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Box

[IMAGE alt='image' src='new_box.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | box returns the box component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Sphere

[IMAGE alt='image' src='new_sphere.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | sphere returns the sphere component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Cylinder

[IMAGE alt='image' src='new_cylinder.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | cylinder returns the cylinder component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New 1D Distance Sensor

[IMAGE alt='image' src='new_distance_sensor.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | distance sensor returns the distance sensor component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Hokuyo URG LIDAR

[IMAGE alt='image' src='new_lidar.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | Hokuyo URG LIDAR returns the Hokuyo LIDAR sensor component. Wire this component to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New IP Camera

[IMAGE alt='image' src='new_camera.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | camera returns the IP camera component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New GPS Sensor

[IMAGE alt='image' src='new_gps_sensor.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | GPS sensor returns the GPS sensor component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New FRC Robot

[IMAGE alt='image' src='new_frc_bot.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | FRC robot returns the FRC robot component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New iRobot Create

[IMAGE alt='image' src='new_irobot_create.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | iRobot Create returns the iRobot Create robot component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Starter Kit 1.0

[IMAGE alt='image' src='new_starter_kit_1.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | starter kit 1.0 returns the Starter kit 1.0 robot component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### New Starter Kit 2.0

[IMAGE alt='image' src='new_starter_kit_2.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | starter kit 2.0 returns the Starter kit 2.0 robot component. Wire this data to a Property Node (Simulator Engine). |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Stewart Robot VI in the labview\examples\robotics\Simulator\Stewart Robot directory for an example of using the New Simulation Object VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_pause_service.html language=enus -->
## TOPIC 00245: Pause Simulator Service VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_pause_service.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_pause_service.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Pause Simulator Service VI

**Owning Palette:** [Simulator VIs](../lvrobovi/simulator_pal.html)

**Requires:** Robotics Module

Pauses the simulation instance the [robotics simulator](../lvrobogsm/robo_sim_overview.html) is currently running. You can use this VI to temporarily halt the simulator in order to [define or change the environment or robots](../lvrobogsm/robo_sim_creating.html) in the simulation instance.

[Example](#examples)

[IMAGE alt='image' src='pause_simulator_service.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Robot Balance.lvproj in the labview\examples\robotics\Simulator\Robot Balance directory for an example of using the Pause Simulator Service VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_prop_node.html language=enus -->
## TOPIC 00246: Property Node (Simulator Engine)

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_prop_node.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_prop_node.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Property Node (Simulator Engine)

**Owning Palette:** [Offline Configuration VIs](../lvrobovi/simulator_config_pal.html)

**Requires:** Robotics Module

[Gets (reads) and/or sets (writes)](../lvrobogsm/robo_sim_creating.html#offlineconfig) properties of a simulated component. The node operates in the same way as a standard [Property Node](/csh?topicname=glang/property_node.html).

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='property_node_simulator_engine.gif']

|  | reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node.You also can wire a LabVIEW class to the reference input to access the private data of the LabVIEW class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | property 2..n are examples of properties you want to set (write). |
|  | reference out returns reference unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | property 1..n are examples of properties you want to get (read). |

#### Property Node (Simulator Engine) Details

To select the object on which to execute the property, wire a simulation object to the **reference** input. For example, to select the environment, wire the environment object to the **reference** input. The node adapts the available properties to the object automatically.

#### Example

Refer to the Stewart Robot VI in the labview\examples\robotics\Simulator\Stewart Robot directory for an example of using the Property Node (Simulator Engine) function.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_save_instance.html language=enus -->
## TOPIC 00247: Save Simulation Instance VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_save_instance.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_save_instance.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Save Simulation Instance VI

**Owning Palette:** [Offline Configuration VIs](../lvrobovi/simulator_config_pal.html)

**Requires:** Robotics Module

Writes [definitions for components in a simulation instance](../lvrobogsm/robo_sim_creating.html#offlineconfig) to a manifest file the [robotics simulator](../lvrobogsm/robo_sim_overview.html) can read.

[Example](#examples)

[IMAGE alt='image' src='save_simulation_instance.gif']

|  | manifest file specifies the absolute path to the .xml manifest file. If the file does not exist, this VI creates the file. |
| --- | --- |
|  | simulation instance contains the simulation instance you want to save in a manifest file. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Stewart Robot VI in the labview\examples\robotics\Simulator\Stewart Robot directory for an example of using the Save Simulation Instance VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/sim_start_service.html language=enus -->
## TOPIC 00248: Start Simulator Service VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/sim_start_service.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/sim_start_service.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Start Simulator Service VI

**Owning Palette:** [Simulator VIs](../lvrobovi/simulator_pal.html)

**Requires:** Robotics Module

Calls the [robotics simulator](../lvrobogsm/robo_sim_overview.html) and initializes the [simulation scene you define in a manifest file](../lvrobogsm/robo_sim_overview.html#framework).

|  | Note If you call this VI while another instance of the simulator is running, LabVIEW returns error code –310192. |
| --- | --- |

Use the [Stop Simulator Service](../lvrobovi/sim_stop_service.html) VI to end the communication session when you finish viewing the simulation.

[Examples](#examples)

[IMAGE alt='image' src='start_simulator_service.gif']

|  | step mode specifies how the simulator models real-world behavior at each simulation step. 0Performance—Specifies that the simulator models real-world behavior more efficiently. 1Accuracy—Specifies that the simulator models real-world behavior more accurately. |
| --- | --- |
| 0 | Performance—Specifies that the simulator models real-world behavior more efficiently. |
| 1 | Accuracy—Specifies that the simulator models real-world behavior more accurately. |
|  | timing mode specifies the timing behavior in the simulation environment. 0Software Real-Time—Specifies that the timing of the simulation environment matches the timing of the real-world. 1Free Running—Specifies that the simulator runs in the simulation environment as fast as the system allows regardless of the timing in the real-world. 2Synchronized—Specifies that you control the timing in the simulation environment. Use the Take Simulation Steps VI to control the steps to take forward in a synchronized mode. |
| 0 | Software Real-Time—Specifies that the timing of the simulation environment matches the timing of the real-world. |
| 1 | Free Running—Specifies that the simulator runs in the simulation environment as fast as the system allows regardless of the timing in the real-world. |
| 2 | Synchronized—Specifies that you control the timing in the simulation environment. Use the Take Simulation Steps VI to control the steps to take forward in a synchronized mode. |
|  | manifest file specifies the absolute path to the .xml manifest file that defines the simulation instance. If you specify an invalid path, LabVIEW returns error code –310200. |
|  | enable 3D visualization specifies whether LabVIEW generates a 3D scene of the simulated environment and components defined in the manifest file. The default is TRUE. |
|  | step size (ms) specifies the rate at which to advance the current time of the simulation and adjust the physical states of components. National Instruments recommends step sizes of 5 to 20 ms. Large step sizes result in less accurate real-world behavior. Smaller step sizes result in a simulation that more accurately models real-world behavior, but they require more processor resources. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | 3D picture refnum specifies a reference to a 3D picture control in which you want to display the simulation. You can wire a reference to a 3D picture control to this input to display the simulation scene on an existing front panel. By default, the simulator displays the simulation in a new window. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Start Simulator Service VI:

- labview\examples\robotics\Simulator\iRobot Create\Simulated iRobot.lvproj
- labview\examples\robotics\Simulator\Robot Balance\Robot Balance.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/simple_vfh.html language=enus -->
## TOPIC 00249: Simple Vector Field Histogram VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/simple_vfh.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/simple_vfh.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Simple Vector Field Histogram VI

**Owning Palette:** [Obstacle Avoidance VIs](../lvrobovi/obstacle_avoid_pal.html)

**Requires:** Robotics Module

Identifies obstacles and gaps, or open areas, in the robot environment, which you can use to implement reactionary motion in a robot vehicle.

Use the [Advanced VFH](../lvrobovi/advanced_vfh.html) VI rather than this VI for goal-directed obstacle avoidance.

|  | Note You can use any unit of measurement to specify distance and angle values. However, always use consistent units when you specify these values. |
| --- | --- |

[Example](#examples)

[IMAGE alt='image' src='simple_vector_field_histogram.gif']

|  | panic range defines the range at which this VI identifies an obstacle as an area of the environment to avoid. panic threshold distance specifies the maximum distance at which obstacle within panic range is TRUE. panic threshold angle specifies the maximum angle at which obstacle within panic range is TRUE. |
| --- | --- |
|  | panic threshold distance specifies the maximum distance at which obstacle within panic range is TRUE. |
|  | panic threshold angle specifies the maximum angle at which obstacle within panic range is TRUE. |
|  | distances specifies the distances between the robot sensor and objects in the robot environment. |
|  | direction angles specifies the angles at which objects are located with respect to the center of the sensor. Positive values represent locations to the right of the center of the sensor, and negative values represent positions to the left of the center of the sensor. Elements in direction angles correspond to elements in distances. |
|  | distance threshold specifies the distance at which this VI does not consider objects to be obstacles. This VI ignores any objects at distances greater than distance threshold. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | obstacle within panic range is TRUE if an object within panic threshold angle is nearer to the sensor than the panic threshold distance. |
|  | largest gap describes the largest open area in the robot environment. angle to gap contains the direction of the open area with respect to the robot sensor. size of gap contains the angular size, or visual diameter, of the open area, measured as an angle. |
|  | angle to gap contains the direction of the open area with respect to the robot sensor. |
|  | size of gap contains the angular size, or visual diameter, of the open area, measured as an angle. |
|  | nearest obstacle describes the object nearest to the sensor. angle to obstacle contains the direction of the obstacle with respect to the sensor. distance to obstacle contains the distance between the sensor and the obstacle. |
|  | angle to obstacle contains the direction of the obstacle with respect to the sensor. |
|  | distance to obstacle contains the distance between the sensor and the obstacle. |
|  | histogram returns the histogram data that represents the distances to objects in range of the sensor, arranged by angle and direction. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the LIDAR Guided Robot.lvproj in the labview\examples\robotics\LIDAR Guided Robot directory for an example of using the Simple Vector Field Histogram VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_create_2_frame.html language=enus -->
## TOPIC 00250: Create Starter Kit 2.0 Steering Frame VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_create_2_frame.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_create_2_frame.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Create Starter Kit 2.0 Steering Frame VI

**Owning Palette:** [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Generates a steering frame object for the Starter Kit 2.0 robot. You can use the steering frame object with the [Steering](../lvrobovi/steering_pal.html) VIs to [implement steering for the Starter Kit robot](../lvrobogsm/robo_skit_programming.html#skit_steering).

[Example](#examples)

[IMAGE alt='image' src='create_skit_2_frame.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | starter kit differential steering frame contains information about the robot steering frame, such as the types and locations of wheels. You can wire this output to Steering VIs to read or write velocity values. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the Create Starter Kit 2.0 Steering Frame VI.
