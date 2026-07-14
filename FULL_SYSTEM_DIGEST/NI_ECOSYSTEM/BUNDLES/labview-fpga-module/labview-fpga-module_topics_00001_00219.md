# NI DOCUMENT BUNDLE: labview-fpga-module

<!--NI_BUNDLE_CHUNK bundle=labview-fpga-module start=1 end=219 -->
<!--NI_TOPIC bundle=labview-fpga-module path=accessing-remote-fpga-targets-across-networks-fpga-interface.html language=enus -->
## TOPIC 00001: Accessing Remote FPGA Targets Across Networks

- bundle_id: `labview-fpga-module`
- source_path: `accessing-remote-fpga-targets-across-networks-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/accessing-remote-fpga-targets-across-networks-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to manage remote connections, understand the data flow, and use these steps to reliably configure and connect to FPGA targets over a network. How Remote Access WorksThe Open FPGA VI Reference function can connect to an FPGA target on a remote system when you provide a remote resource strin

### Accessing Remote FPGA Targets Across
 Networks

Learn how to manage remote connections, understand the data flow, and use these steps
 to reliably configure and connect to FPGA targets over a network.

#### How
 Remote Access Works

Open FPGA VI Reference

rio://<remote-host>/<fpga-resource>

- Enter the resource string in the FPGA Target
 Properties dialog box so the remote target appears in
 RIO Device controls and constants.
- Enter the resource string directly in a host VI using a RIO
 Device control or constant.

Note

Measurement & Automation Explorer (MAX)

Devices and Interfaces

#### Key Considerations

- The RIO server must be running where required for network access.
  - On NI Linux Real‑Time controllers (for example, CompactRIO), the
 service runs automatically.
  - On Windows or Linux desktop systems hosting local RIO hardware,
 start the service manually.
- Avoid branching a single FPGA VI reference when you need concurrent,
 independent operations. Create separate references instead.
- Plan throughput for network variability. Network transfers are not
 deterministic and are slower than local communication.

#### Troubleshooting at a Glance

- If discovery does not show the remote target, connect by IP with the
 resource string.
- If the reference fails to open, verify address/host name, reachability,
 firewall rules, and driver versions.

- [Specify a Remote FPGA Target in the FPGA Target Properties](specify-remote-fpga-target-properties.html) Learn how to add a remote FPGA target to a project so it appears in the RIO Device list on host VIs.
- [Specify a Remote FPGA Target in an FPGA Interface VI](specify-remote-fpga-target-interface-vi.html) Learn how to wire a remote resource string directly into the Open FPGA VI Reference function on a host VI.
- [Start and Verify the RIO Server for Network Access](start-verify-rio-server.html) Learn how to ensure the RIO server is running where it is required for network access to RIO devices.
- [Connect from a Linux Host to an Ethernet CompactRIO](connect-linux-to-ethernet-crio.html) Learn how to open a remote FPGA reference from a Linux desktop host to a CompactRIO controller.

Parent topic:

Communicating with FPGA VIs

Related tasks:

- Connect from a Linux Host to an Ethernet CompactRIO
- Specify a Remote FPGA Target in an FPGA Interface VI
- Specify a Remote FPGA Target in the FPGA Target Properties
- Start and Verify the RIO Server for Network Access

Related information:

- NI-RIO For Linux/x86 64-bit Architecture

<!--NI_TOPIC bundle=labview-fpga-module path=adding-an-fpga-base-clock-to-a-labview-project-fpga-module.html language=enus -->
## TOPIC 00002: Adding an FPGA Base Clock to a LabVIEW Project

- bundle_id: `labview-fpga-module`
- source_path: `adding-an-fpga-base-clock-to-a-labview-project-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-an-fpga-base-clock-to-a-labview-project-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA targets can support more than one base clock, although some targets add only a subset of supported base clocks to the Project Explorer window when you add the target. If the FPGA target you use does not include the FPGA base clock you need in the Project Explorer window when you add the target

### Adding an FPGA Base Clock to a LabVIEW Project

FPGA targets can support more than one base clock, although some targets add only a subset of supported base clocks


 to the Project Explorer window when you add the target. If the


 FPGA target you use does not include the FPGA base clock you need in the


 Project Explorer window when you add the target to a


 LabVIEW project, you can add a new base clock to the LabVIEW project.

Complete the following steps to add a new base clock to a LabVIEW project.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target and select New»FPGA Base


 Clock from the shortcut menu. The FPGA Base Clock Properties dialog box appears.
4. Select an available clock from the Resource pull-down


 menu.
5. Click the OK button. The new FPGA base clock appears in


 the Project Explorer window below the FPGA target.

You now can set the new base clock as the top-level clock in the project.

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Using FPGA Clocks and Timing
- Adding FPGA Targets to a LabVIEW Project
- Selecting a Top-Level Clock for an FPGA Target
- Configuring FPGA Base Clocks
- Creating FPGA-Derived Clocks
- Selecting an FPGA Clock as the Timing Source for SCTLs

<!--NI_TOPIC bundle=labview-fpga-module path=adding-component-level-ip-to-a-project-fpga-module.html language=enus -->
## TOPIC 00003: Adding Component-Level IP to a Project

- bundle_id: `labview-fpga-module`
- source_path: `adding-component-level-ip-to-a-project-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-component-level-ip-to-a-project-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You add a component-level IP (CLIP) item to the LabVIEW project to instantiate the CLIP inside the FPGA. If you want to instantiate the CLIP multiple times, each CLIP instance must have a unique name, and each name must follow VHDL naming conventions. Name each CLIP constant uniquely, and do not pre

### Adding Component-Level IP to a Project

You add a component-level IP (CLIP) item to the LabVIEW project to instantiate the


 CLIP inside the FPGA. If you want to instantiate the CLIP multiple times, each CLIP


 instance must have a unique name, and each name must follow VHDL naming conventions.


 Name each CLIP constant uniquely, and do not prefix CLIP constant names with


 k.

To add a CLIP item to the LabVIEW project you must associate a CLIP declaration file


 to the target and then add a CLIP item from the declaration file to the project. You


 associate a CLIP declaration file to the target using the Component-Level


 IP page of the FPGA


 Target Properties dialog box. You add the CLIP item to the project using


 the General page of the Component-Level


 IP Properties dialog box. Use the Clock


 Selections page of the Component-Level IP


 Properties dialog box to link clocks from the FPGA target to the


 inputs of the CLIP.

To pass data between CLIP and an FPGA VI, the CLIP declaration file must


 have a <InterfaceType>LabVIEW</InterfaceType> tag.


 Then, when you add the CLIP item to a LabVIEW project, the FPGA Module adds all of


 the I/O that is defined in the declaration XML file under the


 CLIP item in the LabVIEW project.

Tip

Refer to the CLIP Tutorial, Part 3: Adding CLIP to a Project for an example of adding


 CLIP to a Project.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- Passing Data between Component-Level IP and VIs
- Using the Configure Component-Level IP Wizard
- CLIP Tutorial, Part 3: Adding CLIP to a Project
- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- Using VHDL Code as Component-Level IP

<!--NI_TOPIC bundle=labview-fpga-module path=adding-fpga-targets-to-a-labview-project-fpga-module.html language=enus -->
## TOPIC 00004: Adding FPGA Targets to a LabVIEW Project

- bundle_id: `labview-fpga-module`
- source_path: `adding-fpga-targets-to-a-labview-project-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-fpga-targets-to-a-labview-project-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must create a LabVIEW project before you can create an application using an FPGA target. You then can add an FPGA target to the project and create FPGA VIs. Use one of the following procedures to add an FPGA target to a project: Adding an FPGA Target in the Local Development Computer Adding an F

### Adding FPGA Targets to a LabVIEW
 Project

You must create a LabVIEW project before you can create an application using an FPGA


 target. You then can add an FPGA target to the project and create FPGA VIs.

Use one of the following procedures to add an FPGA target to a project:

- Adding an FPGA Target in the Local Development Computer
- Adding an FPGA Target in a Real-Time System
- Adding an FPGA Target in a Remote Computer

After you create the project with an FPGA target, you can perform the following


 tasks:

- Create FPGA VIs
- Add FPGA I/O
- Add FPGA clocks
- Add FPGA register items
- Add FPGA memory items
- Add FPGA FIFOs

FPGA VI functionality varies depending upon the specific FPGA target. Refer to the


 specific FPGA target hardware


 documentation for more information on FPGA target functionality.

#### Adding an FPGA Target in the Local Development Computer

Complete the following steps to add an FPGA target that is installed in the local


 development computer to the Project


 Explorer window.

1. Create a new project or open an existing


 project.
2. Right-click My Computer in the Project


 Explorer window and select New»Targets and


 Devices from the shortcut menu to display the Add Targets and Devices dialog box.
3. Select Existing target or device to display the FPGA


 targets installed in the development computer. Tip If you do not


 have an FPGA target, you can select New target or


 device to display the types of FPGA targets for which


 support is installed on the development computer. You can add any of these


 targets to the project as a stand-in for an actual target.
4. Expand the FPGA Target folder. LabVIEW displays the FPGA


 targets that are installed in the local computer and for which support is


 installed on the local computer.
5. Select an FPGA target from the list of available targets.
6. Click the OK button. The FPGA target appears in the


 Project Explorer window under My


 Computer .

You now can add an FPGA VI under the FPGA target and develop the FPGA VI.

#### Adding an FPGA Target in a Real-Time System

Complete the following steps to add an FPGA target in an Real Time (RT) system to the


 Project Explorer window under an RT controller. Some FPGA


 targets cannot be used under an RT controller.

1. Create the project and RT target with the Real-Time New Project Wizard.
2. Right-click the RT target in the Project Explorer window


 and select New»Targets and Devices from the shortcut menu


 to display the Add Targets


 and Devices dialog box.
3. Select Existing target or device to display the FPGA


 targets installed in the RT system. Note You might need to set


 access permissions for the RT controller to display existing FPGA targets in


 the Add Targets and Devices dialog box.
4. Select an FPGA target from the list of available targets.
5. Click OK . The FPGA target appears in the


 Project Explorer window under the RT target.

You now can add an FPGA VI under the FPGA target and develop the FPGA VI.

#### Adding an FPGA Target in a Remote Computer

After the remote FPGA target appears in MAX and you set access


 permissions to the remote system in which it resides, you can add that target to the


 Project Explorer window in LabVIEW and develop VIs to run


 on the target. Complete the following steps to add a remote system and its FPGA


 target to the Project Explorer window in LabVIEW.

1. Right-click the project root in the Project Explorer 


 window and select New»Targets and Devices from the


 shortcut menu to display the Add Targets


 and Devices dialog box.
2. Select New target or device and select


 Networked Computer/Device from the list and click


 OK . The remote system appears in the


 Project Explorer window.
3. Right-click on Networked Computer/Device in the


 Project Explorer window and select


 Properties from the shortcut menu to display the


 Networked Computer/Device Properties dialog


 box.
4. Assign the remote computer you just added an IP address in the


 Address text box.
5. Click the OK button.
6. Right-click the remote system you just added and select New»Targets


 and Devices from the shortcut menu.
7. Select Existing target or device to display the FPGA


 targets installed in the development computer. [IMAGE alt='image' src='GUID-ED3A60E1-F7EE-431D-9D52-F9700753C21C-a5.png']Tip If you do


 not have an FPGA target, you can select New


 target or device to display the types of


 FPGA targets for which support is installed on the


 development computer. You can add any of these targets to


 the project as a stand-in for an actual target.
8. Click the OK button. The FPGA target appears in the


 Project Explorer window.

You now can add an FPGA VI under the FPGA target and develop the FPGA VI.

Parent topic:

Introduction to FPGA Applications and Projects

Related concepts:

- Adding an FPGA Base Clock to a LabVIEW Project
- Adding FPGA Targets to a LabVIEW Project
- Adding Items to an FPGA Target in the Project Explorer Window
- Creating FPGA I/O Items
- Creating FPGA-Derived Clocks
- Configuring FPGA Base Clocks
- Controlling the FPGA VI Execution Rate
- Downloading an FPGA VI to the Flash Memory of an FPGA Target
- Selecting a Top-Level Clock for an FPGA Target
- Selecting an FPGA Clock as the Timing Source for SCTLs
- Using CLIP Clocks
- Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=adding-indicators-to-monitor-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00005: Adding Indicators to Monitor FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `adding-indicators-to-monitor-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-indicators-to-monitor-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You cannot use probes and other traditional LabVIEW debugging techniques in FPGA VIs when you run them on FPGA targets. You instead can use indicators on the FPGA VI block diagram. Place indicators anywhere on the block diagram where you need to see data to verify the functionality of the VI. You ca

### Adding Indicators to Monitor FPGA VIs

You cannot use probes and other traditional


 LabVIEW debugging techniques in FPGA VIs when you run them on FPGA


 targets. You instead can use indicators on the FPGA VI block diagram. Place


 indicators anywhere on the block diagram where you need to see data to verify the


 functionality of the VI. You can use this procedure when the signals you want to


 observe change slowly relative to the speed with which the host computer


 communicates with the target.

Tip

Complete the following steps to use an indicator as you would a probe in an existing


 FPGA VI.

1. Create a new VI or open an existing VI under an FPGA target that


 also contains FPGA I/O items.
2. Right-click the wire you want to monitor and select


 Create»Indicator from the shortcut menu.
3. Repeat step 2 for each wire you want to monitor.
4. Compile the VI.

You now can run the FPGA VI using interactive front


 panel communication or programmatic FPGA


 interface communication to view and verify the data in the FPGA VI.

Parent topic:

Debugging FPGA VIs on an FPGA Target

Related concepts:

- Adding Items to an FPGA Target in the Project Explorer Window
- Compiling, Downloading, and Running FPGA VIs
- Debugging FPGA VIs on an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=adding-io-to-monitor-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00006: Adding I/O to Monitor FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `adding-io-to-monitor-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-io-to-monitor-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You cannot use probes and other traditional LabVIEW debugging techniques in FPGA VIs. If you have unused I/O resources on the FPGA target, you can add additional I/O terminals to the FPGA VI block diagram for debugging. You can monitor the additional I/O terminals using an external device, such as a

### Adding I/O to Monitor FPGA VIs

You cannot use probes and other traditional


 LabVIEW debugging techniques in FPGA VIs. If you have unused I/O


 resources on the FPGA target, you can add additional I/O terminals to the FPGA VI


 block diagram for debugging. You can monitor the additional I/O terminals using an


 external device, such as an oscilloscope, logic analyzer, and so on. Examples of


 using additional I/O terminals to monitor FPGA VIs include the following:

- Output the internal state of Boolean logic on a digital output terminal.
- Write a pattern to multiple digital output terminals to indicate when specific


 portions of the data flow execute.
- Pulse a digital output terminal to indicate when a trigger has been


 detected.
- Toggle a digital output terminal at each iteration of a loop to monitor the


 performance of the loop.

For example, complete the following steps to monitor the performance of a While Loop


 in an existing FPGA VI by toggling a digital output terminal at each iteration of


 the While Loop.

1. Create a new VI or open an existing VI under an FPGA target that


 also contains FPGA I/O items in the Project Explorer 


 window.
2. Create a new FPGA I/O item or select an unused FPGA I/O item that is


 under the FPGA target you are using in the Project


 Explorer window.
3. Right-click the While Loop and select Add Shift


 Register from the shortcut menu.
4. Add an FPGA I/O Node inside the While Loop.
5. Click the I/O Name section of the FPGA I/O Node and


 select the FPGA I/O item you previously added to the project.
6. If the FPGA I/O item is a digital input, right-click the FPGA I/O Node and


 select Change to Write .
7. Wire the left shift register to the input of the FPGA I/O Node.
8. Add a Not function to the While Loop.
9. Wire the x input of the Not function to the wire


 connecting the shift register and the FPGA I/O Node. Wire the .not.


 x? output of the Not function to the right shift register.
10. Select File»Save All in the Project


 Explorer window to save changes to the FPGA VI and the LEP


 file.
11. Recompile and run the FPGA VI on the FPGA target.
12. Monitor the state of the digital output terminal you selected using an


 oscilloscope or similar instrument.

Parent topic:

Debugging FPGA VIs on an FPGA Target

Related concepts:

- Adding Items to an FPGA Target in the Project Explorer Window
- Creating FPGA I/O Items
- Compiling, Downloading, and Running FPGA VIs
- Debugging FPGA VIs on an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=adding-items-to-an-fpga-target-in-the-project-explorer-window-fpga-module.html language=enus -->
## TOPIC 00007: Adding Items to an FPGA Target in the Project Explorer Window

- bundle_id: `labview-fpga-module`
- source_path: `adding-items-to-an-fpga-target-in-the-project-explorer-window-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-items-to-an-fpga-target-in-the-project-explorer-window-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add new or existing FPGA VIs, FPGA I/O items, FPGA FIFO, or FPGA clocks to an FPGA target in the Project Explorer window. You also can use folders to organize items under the FPGA target in the Project Explorer window. You might use the folder option for organizing items if you intend to use

### Adding Items to an FPGA Target in the Project
 Explorer Window

You can add new or existing FPGA VIs, FPGA I/O items, FPGA FIFO, or FPGA clocks to an FPGA target in the Project


 Explorer window. You also can use folders to organize items under the


 FPGA target in the Project Explorer window. You might use the


 folder option for organizing items if you intend to use multiple FPGA I/O items.

Complete the following steps to add an item to an FPGA target in the


 Project Explorer window.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target and select


 New»x from the shortcut menu to


 add a new item, where x is the type of


 item you want to add, such as a VI, FPGA I/O item, or folder. The item appears


 in the Project Explorer window under the FPGA


 target.
4. Double-click the new item in the Project Explorer window


 to edit or configure the item. If you added an FPGA base clock, right-click the


 FPGA base clock and select Properties from the shortcut


 menu to configure the clock.

Tip

Project Explorer

Parent topic:

Introduction to FPGA Applications and Projects

Related concepts:

- Adding FPGA Targets to a LabVIEW Project
- Adding Indicators to Monitor FPGA VIs
- Adding I/O to Monitor FPGA VIs
- Using FPGA Clocks and Timing
- Selecting an FPGA Clock as the Timing Source for SCTLs
- Setting and Retrieving Properties on FPGA I/O and FPGA Targets
- Using the FPGA I/O Node
- Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=adding-synthesis-files-fpga-module.html language=enus -->
## TOPIC 00008: Adding Synthesis Files

- bundle_id: `labview-fpga-module`
- source_path: `adding-synthesis-files-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adding-synthesis-files-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Synthesis files contain the HDL code you want to integrate into an FPGA VI. Complete the following steps to add synthesis files to the IP Integration Node. LabVIEW assumes the first file you add is the top-level file. Add the IP Integration Node to the block diagram. Double-click the node to configu

### Adding Synthesis Files

Synthesis files contain the HDL code you want to integrate into an FPGA VI. Complete


 the following steps to add synthesis files to the IP Integration


 Node.

Note

1. Add the IP Integration Node to the block diagram.
2. Double-click the node to configure it. The Name and


 Source page appears.
3. Click the Add Synthesis File button: [IMAGE alt='image' src='GUID-1ED78CD0-C780-4040-B2CA-44266C3C5FDF-a5.png'] LabVIEW prompts you for a synthesis file to


 add.
4. Choose the synthesis file to add and click the OK button.


 LabVIEW displays the synthesis file in the Synthesis File 


 column of the IP Source table.
5. (Optional) Set this file as the top-level file.
6. Notice the Simulation Behavior column of this table.


 LabVIEW assigns a simulation behavior based on the type of file you


 added. You now have the following options:
  - Accept the


 simulation behavior LabVIEW assigned.
  - Change


 this simulation behavior.
  - Exclude the file from simulation.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=adjusting-the-length-of-the-internal-combinatorial-path-of-a-dsp48e-or-dsp48e1-function-fpga-module.html language=enus -->
## TOPIC 00009: Adjusting the Length of the Internal Combinatorial Path of a DSP48E or DSP48E1 Function

- bundle_id: `labview-fpga-module`
- source_path: `adjusting-the-length-of-the-internal-combinatorial-path-of-a-dsp48e-or-dsp48e1-function-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/adjusting-the-length-of-the-internal-combinatorial-path-of-a-dsp48e-or-dsp48e1-function-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DSP48E or DSP48E1 schematic at the bottom of the configuration dialog box shows the internal combinatorial path of the function. If this combinatorial path is too long, the function cannot compile at the clock rate you specify, and LabVIEW returns errors when you attempt to compile the FPGA VI.

### Adjusting the Length of the Internal Combinatorial Path of a DSP48E or DSP48E1 Function

The DSP48E or DSP48E1 schematic at the bottom of the configuration dialog box shows


 the internal combinatorial path of the function. If this combinatorial path is too


 long, the function cannot compile at the clock rate you specify, and LabVIEW returns


 errors when you attempt to compile the FPGA VI.

You can avoid these errors by adding internal registers to the function. Adding


 registers increases the chances that a function can compile at a specified clock


 rate. However, adding registers also increases the latency of a DSP48E function and


 might unbalance the latencies of internal data paths relative to one another.


 Depending on how you are using the function, this imbalance might be acceptable, but


 you should be aware of the latencies of the internal data paths to ensure the


 function executes the way you want.

Use the Registers page of the configuration dialog box to add


 and configure internal registers in a DSP48E slice. Notice that as you add and


 configure registers, corresponding green boxes light up in the schematic at the


 bottom of the dialog box. The data paths also might change.

Note

Virtex-5
 FPGA XtremeDSP Design Considerations User Guide

www.xilinx.com

Virtex-6 FPGA
 DSP48E1 Slice User Guide

#### Enabling and Resetting Registers

Each register has a corresponding enable and reset terminal. By default, LabVIEW sets


 reset terminals to FALSE and enable terminals to TRUE while hiding all terminals


 from the block diagram. If these settings are acceptable, you do not need to change


 any settings.

For detailed control over enable and reset operations, use the


 Enable and Reset pages to specify


 which enable and reset terminals LabVIEW shows on the block diagram. At the top of


 each page is a pull-down menu of options you can choose from, as the following


 illustration shows:

[IMAGE alt='image' src='GUID-9783198A-5E2D-4D54-A8BF-38C7A078F7D3-a5.png']

These options have the following effects on registers you have added:

- Hide All Signals —Specifies that LabVIEW does not show any


 enable or reset terminals on the block diagram. In this situation, LabVIEW


 applies the default behavior as described above.
- Use a Single Terminal for All Registers —Specifies that


 LabVIEW displays either the enable or


 clear input terminal, depending on the page you are


 configuring. To enable/reset all registers in the slice simultaneously, wire a


 TRUE value to this terminal.
- Select Terminals to Show —Enables the checkboxes below


 this pull-down menu. To display the terminal for an individual register, place a


 checkmark in the appropriate checkbox. The name in parentheses is the VHDL name


 of the enable or reset signal. Note If you select this option but


 LabVIEW still dims some checkboxes, you have not added the corresponding


 register on the Registers page. Click the


 Registers tab, place a checkmark in the


 appropriate checkbox, and then return to the Enable


 or Reset page.

After you click the OK button and return to the block diagram,


 LabVIEW displays any Boolean input terminals you selected. You then can write code


 to set these terminals to TRUE or FALSE at the appropriate times.

#### VHDL Equivalent of LabVIEW Options

To view the VHDL equivalent of a configuration, click the VHDL
 Instantiation tab. Refer to Table 1-3 in either the *Virtex-5
 FPGA XtremeDSP Design Considerations User Guide* or the *Virtex-6
 FPGA DSP48E1 Slice User Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about specific attributes. The
 following table shows the attributes that correspond to each option in LabVIEW.

| LabVIEW Option | Attribute to Reference in Table 1-3 |
| --- | --- |
|  | AREG |
|  | BREG |
|  | ACASCREG |
|  | BCASCREG |
| alumode register | ALUMODEREG |
| c register | CREG |
| carryin register | CARRYINREG |
| carryinsel register | CARRYINSELREG |
| (DSP48E) m register | MREG |
| (DSP48E) multcarryin register | MULTCARRYINREG |
| (DSP48E1) m register and multcarryin register | MREG |
| opmode register | OPMODEREG |
| p registers | PREG |
| (DSP48E1) d register | DREG |
| (DSP48E1) ad register | ADREG |
| (DSP48E1) inmode register | INMODEREG |

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Viewing the Latencies of Data Paths in a DSP48E or DSP48E1 Function
- Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function
- Configuring DSP48E and DSP48E1 Functions

<!--NI_TOPIC bundle=labview-fpga-module path=avoiding-arbitration-to-optimize-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00010: Avoiding Arbitration to Optimize FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `avoiding-arbitration-to-optimize-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/avoiding-arbitration-to-optimize-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW uses arbitration to manage access to shared resources. When you select an arbitration option, select Never Arbitrate, if possible, to save space on the FPGA and increase speed. If you select the Never Arbitrate option for a resource interface, LabVIEW does not add arbitration components, whi

### Avoiding Arbitration to Optimize FPGA VIs

LabVIEW uses arbitration to manage access to shared resources. When you select an arbitration option, select Never


 Arbitrate, if possible, to save space on the FPGA and increase


 speed.

If you select the Never Arbitrate option for a resource interface, LabVIEW does not add arbitration components, which


 saves significant space on the FPGA. In addition to saving space, the


 Never Arbitrate option allows some of the FPGA I/O and FIFOfunctions


 to execute in a single clock cycle. To use the Never


 Arbitrate option, you must guarantee sequential access to the


 resource interface in the data flow of the FPGA VI, as shown in the following block


 diagram.

[IMAGE alt='image' src='GUID-8ADDFE7F-C17D-453E-9B80-7112DB311A9D-a5.png']

In the block diagram above, the Flat Sequence structure ensures that the two FIFO


 Method Nodes do not execute simultaneously, so resource contention does not occur.


 In such situations, Never Arbitrate is an appropriate option.


 However, if you select the Never Arbitrate option and make


 simultaneous requests, the FPGA VI corrupts data.

Note

Selecting the Never Arbitrate option when simulating an FPGA


 application that contains memory items with multiple accessors may result in


 incorrect behavior. For example, if your application includes multiple writers, each


 writer can update the memory address specified during simulation. Additionally, if


 your application includes multiple readers, each reader can assess the memory


 address specified during simulation.

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Understanding Arbitration Options
- Managing Shared Resources
- Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=avoiding-buffer-errors-in-dma-applications-fpga-module.html language=enus -->
## TOPIC 00011: Avoiding Buffer Errors in DMA Applications

- bundle_id: `labview-fpga-module`
- source_path: `avoiding-buffer-errors-in-dma-applications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/avoiding-buffer-errors-in-dma-applications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The number of elements a DMA buffer can hold, also known as the size or depth of the buffer, is a critical part of designing a robust application. The number of elements in a buffer has the following effects on an application: If the buffer is too small, the buffer fills up before data can be read a

### Avoiding Buffer Errors in DMA Applications

The number of elements a DMA buffer can hold, also known as the size or depth of the buffer, is a


 critical part of designing a robust application. The number of elements in a buffer


 has the following effects on an application:

- If the buffer is too small, the buffer fills up before data can be read and


 removed. In this situation, called an overflow, any data you write to the buffer


 is lost
- If the buffer is too large, it uses an unnecessary number of resources on the


 FPGA and/or host computer, which can reduce the performance of the


 application
- If you attempt to read more elements from a buffer than what is available, an


 underflow occurs and LabVIEW returns an error

To design a robust application, NI recommends that you:

- Set the sizes of each buffer appropriately
- Design the application to detect and avoid buffer overflows
- Design the application to detect and avoid buffer underflows
- Design the application to prevent stale data from accumulating in the


 buffers

The following sections provide more information about these strategies.

#### Setting Buffer Sizes Appropriately

The following table describes the two buffers that comprise a DMA channel, where to


 configure the size of each buffer, the recommended size of each buffer, and the


 maximum size of each buffer.

| Location of Buffer | Where to Configure | Default Buffer Size | Recommended Buffer Size | Maximum Buffer Size |
| --- | --- | --- | --- | --- |
| FPGA target | General page of the FIFO Properties dialog box | 1023 elements | 1023 elements. For most applications, you do not need to change the size of the FPGA buffer. | Depends on the amount of resources available on the FPGA and bytes allocated in memory on the host computer. If the FPGA does not have enough resources for the number of elements you specify, the FPGA VI fails to compile. Refer to the specific FPGA target hardware documentation for more information about DMA FIFO size limitations. |
| Host computer | FIFO.Configure method of Invoke Method function | 10,000 elements or twice the size of the FPGA FIFO buffer, whichever is greater | Five times the number of elements you specify to read or write | Depends on the amount of resources available on the FPGA and bytes allocated in memory on the host computer. If the FPGA does not have enough resources for the number of elements you specify, the FPGA VI fails to compile. Refer to the specific FPGA target hardware documentation for more information about DMA FIFO size limitations. |

#### Detecting and Avoiding Buffer Overflows

To detect when a buffer might overflow, use the Get Number of


 Elements to Write method of the FIFO Method


 Node. This method returns the number of empty elements in the buffer to


 which you can write data. If this value is zero, the buffer is full; data you write


 to the buffer might be lost.

Use the following techniques to prevent buffer overflow:

- Reduce the rate at which you write data to the buffer
- Increase the Requested Number of Elements to read on the


 host
- Increase the rate at which the host reads data
- Increase the size of the host buffer, the FPGA buffer, or both
- Reduce the load on the CPU on the host. The speed of the CPU and the presence of


 competing tasks reduce the transfer rate from the host buffer to application


 memory

#### Detecting and Avoiding Buffer Underflows

To detect when a buffer might underflow, use the Get Number of


 Elements to Read method of the FIFO Method


 Node. This method returns the number of elements in the buffer that are


 available to read. If this number is less than the number of elements you are


 reading from the buffer, reading from the buffer can cause the buffer to time


 out.

To detect when a buffer did underflow, check the FIFO.Read method for error –50400, as the following block diagram


 shows:

[IMAGE alt='image' src='GUID-CFC16604-C1AB-434F-8112-7CD3794EDAC9-a5.png']

You might want to take some action, such as stopping the application, if either


 problem occurs. You can use a Compound


 Arithmetic function configured as OR to stop


 execution of both the FPGA VI and the host VI when an overflow or underflow


 condition occurs.

Use the following techniques to avoid buffer underflow:

- Increase the Timeout of the FIFO.Read method
- Reduce the rate at which the host reads data
- Reduce the number of elements the VI reads from the buffer by reducing the value


 of the Number of Elements control you wire to the


 FIFO.Read function

#### Preventing Stale Data from Accumulating in a Buffer

When you execute a VI on an FPGA target and stop and restart the VI, buffers do not


 reset, which means data remains in the buffers the next time you run the FPGA


 VI.

Use the following techniques to clear any buffers:

- Reset the FPGA VI
- Flush the buffer to read the remaining elements of the FIFO

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Best Practices for DMA Applications
- Transferring Data Using Direct Memory Access

<!--NI_TOPIC bundle=labview-fpga-module path=avoiding-jitter-due-to-resource-contention-fpga-module.html language=enus -->
## TOPIC 00012: Avoiding Jitter Due to Resource Contention

- bundle_id: `labview-fpga-module`
- source_path: `avoiding-jitter-due-to-resource-contention-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/avoiding-jitter-due-to-resource-contention-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Jitter occurs if a requestor in a loop is delayed in becoming an accessor due to resource contention with one or more additional requestors, and the delay varies per loop iteration. For example, you might have an application performing a timed While Loop that samples analog input at a fixed rate. Ea

### Avoiding Jitter Due to Resource
 Contention

Jitter occurs if a requestor in a loop is delayed in becoming an accessor due to


 resource contention with one or more additional requestors, and the


 delay varies per loop iteration. For example, you might have an application


 performing a timed While Loop that samples analog input at a fixed rate.


 Each time the FPGA I/O Node executes, the node becomes an accessor as


 soon as it requests the analog input resource. If you add a second timed While Loop


 that samples the same analog input resource, the two FPGA I/O Nodes might


 simultaneously request the analog input resource. In this case, the arbiter delays


 one of the requestors while allowing the other requestor to become an accessor. This


 delay introduces jitter because resource access does not always occur immediately


 after the request was made.

To avoid jitter, design the FPGA VI block diagram to make sure a requestor does not


 access the shared resource when the shared resource is busy and to make sure two


 requests do not occur during the same clock cycle. Jitter occurs most often when you


 use a shared subVI in two independent parts of the VI, or when you access a resource


 interface from parallel loops, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-5049B101-2D0F-4028-8DED-B04C3DE28A27-a5.png']

The VI in the block diagram above contains parallel While Loops, both of which write


 to MemoryBlock1. Depending on how long it takes the rest of


 the code in each loop to execute, the two Memory Method Nodes might make


 simultaneous write requests to MemoryBlock1, resulting in


 both jitter and data uncertainty. In the example above, jitter occurs when


 Count1 and Count2 differ by 10 -


 15 ticks.

The possibility of jitter grows with the number of accessors to a single resource.


 However, if you avoid simultaneous requests, the delay through the arbiter is


 constant regardless of the number of potential accessors. To avoid multiple


 accessors in the above example, you could create a second memory item and write to


 it in the bottom While Loop, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-A72F2DCF-6DF5-4759-9F45-F689702952C2-a5.png']

Parent topic:

Managing Shared Resources

Related concepts:

- Managing Shared Resources
- Understanding Arbitration Options

<!--NI_TOPIC bundle=labview-fpga-module path=avoiding-large-vis-and-functions-in-fpga-vis-when-possible-fpga-module.html language=enus -->
## TOPIC 00013: Avoiding Large VIs and Functions in FPGA VIs When Possible

- bundle_id: `labview-fpga-module`
- source_path: `avoiding-large-vis-and-functions-in-fpga-vis-when-possible-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/avoiding-large-vis-and-functions-in-fpga-vis-when-possible-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to optimize an FPGA VI, be careful when using the following VIs and functions: Quotient & Remainder—This function consumes significant space on the FPGA. If you need to divide by a power of two, consider using the Scale By Power Of 2 function with a negative constant wired to the n input

### Avoiding Large VIs and Functions in FPGA VIs When Possible

If you want to optimize an FPGA VI, be careful when using the following VIs and


 functions:

- Quotient & Remainder—This function consumes significant space on the FPGA.


 If you need to divide by a power of two, consider using the Scale By Power Of 2 function with a negative


 constant wired to the n input.
- Divide and Reciprocal—These functions can consume significant space on the FPGA.


 However, you can save space if you set the rounding mode as Truncate or


 Round-Half-Up (Asymmetric) .
- Square Root—This function provides a default sqrt(x) 


 output that has a high precision. If the fractional word length of


 sqrt(x) is greater than half of that in


 x , you can decrease the fractional word length of


 sqrt(x) for a lower precision to save clock cycles


 and resources on the FPGA.
- Rotate 1D Array—If you wire a control to the input, this function takes time


 proportional to the number of positions to be rotated, plus two clock cycles of


 overhead to enter and leave the function. However, if you wire a constant to the


 input, this function takes negligible time to execute and consumes no space on


 the FPGA.
- Scale by Power of 2—If you wire a control to the input, this function can


 consume significant space on the FPGA. However, if you wire a constant to the


 input, the function consumes no space on the FPGA.

Note

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=avoiding-the-iteration-terminal-data-type-fpga-module.html language=enus -->
## TOPIC 00014: Avoiding the Iteration Terminal Data Type

- bundle_id: `labview-fpga-module`
- source_path: `avoiding-the-iteration-terminal-data-type-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/avoiding-the-iteration-terminal-data-type-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the smallest data type possible for non-constant values to decrease the size and increase the speed of an FPGA VI. If you use a While Loop, you can avoid using the 32-bit integer of the iteration terminal by using shift registers instead. The following illustrations show how to create While Loop

### Avoiding the Iteration Terminal Data Type

Use the smallest data type possible for non-constant values to decrease the size


 and increase the speed of an FPGA VI. If you use a While Loop, you can avoid using


 the 32-bit integer of the iteration terminal by using shift registers instead.

The following illustrations show how to create While Loops that run 2, 3, and 100


 iterations without using the iteration terminal.

[IMAGE alt='image' src='GUID-CF80CBFF-CB7C-4A28-BBA0-75CC23DE1467-a5.png']

[IMAGE alt='image' src='GUID-5715663C-1DA2-4241-861D-492FEF44A755-a5.png']

[IMAGE alt='image' src='GUID-A1637D60-F952-4116-A928-50D6D0A3FB8F-a5.png']

The constant initializing the shift register in the last illustration is an unsigned,


 8-bit integer data type.

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Using the Smallest Data Type to Optimize FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=best-practices-for-dma-applications-fpga-module.html language=enus -->
## TOPIC 00015: Best Practices for DMA Applications

- bundle_id: `labview-fpga-module`
- source_path: `best-practices-for-dma-applications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/best-practices-for-dma-applications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following best practices when working with DMA communication: Best Practice Details Refer to your FPGA target hardware documentation for information about how that target handles DMA transfers. DMA support and behavior varies by FPGA target. These differences have implications for how y

### Best Practices for DMA Applications

Consider the following best practices when working with DMA communication:

| Best Practice | Details |
| --- | --- |
| Refer to your FPGA target hardware documentation for information about how that target handles DMA transfers. | DMA support and behavior varies by FPGA target. These differences have implications for how you design an application. |
| Set buffer sizes appropriately and check for overflows and underflows. | The sizes of the DMA buffers have a large impact on the performance and robustness of your application. |
| Design your application to handle the following situations: The Timed Out? indicator of the FIFO Method Node returns TRUE on FPGA targets.The error out indicator of the FIFO Read Node returns code -50400 on RT targets. | These situations indicate an error occurred in reading or writing data to or from one of the buffers. If you design your application to handle these situations instead of failing, your application will be more robust. |
| When using the FIFO.Write method to transfer data from the host computer to an FPGA target, always read the value of the Empty Elements Remaining indicator before attempting to write data to the buffer. | The number of empty elements is guaranteed to be accurate for the next DMA operation. For most FPGA targets, this value is valid for subsequent operations also, decreasing by an amount equal to the size of each subsequent write. However, some FPGA targets recalculate this value after each write to the DMA channel. If you write to the channel in this situation, you risk LabVIEW discarding the data because the buffer might be full. The write operation also might time out. |
| When using the FIFO.Read method to read DMA data on the host computer, always read the value of the Elements Remaining indicator before attempting to read data from the buffer. | Use a polling programming architecture where you read the number of elements remaining in the buffer before attempting to read data from the buffer. |
| Stop a FIFO before configuring its number of elements programmatically. | If you configure the depth of a FIFO while the FIFO is running, the FIFO resets the next time it is started, which clears all data from the FIFO. |
| If you interleave multi-channel data, specify that the number of elements to write to the buffer is an integer multiple of the number of channels. | This design ensures you can read the same amount of data from each channel. For example, if you have eight I/O channels and specify 80 in the Requested Number of Elements control in the FIFO Properties dialog box, the buffer has space for 10 samples from each channel. |
| On the host, read or write large amounts of data at a time. | DMA communication incurs computational overhead; therefore, sending commands or small amounts of data wastes resources. |

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Avoiding Buffer Errors in DMA Applications
- Designing a Host VI to Read Data in DMA Applications
- Transferring Multi-Channel Data in DMA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=caveats-for-using-dsp48e-and-dsp48e1-functions-fpga-module.html language=enus -->
## TOPIC 00016: Caveats for Using DSP48E and DSP48E1 Functions

- bundle_id: `labview-fpga-module`
- source_path: `caveats-for-using-dsp48e-and-dsp48e1-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/caveats-for-using-dsp48e-and-dsp48e1-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes the differences between compiling a DSP48E or DSP48E1 function for an FPGA target and exporting the function for simulation: Execution on an FPGA Target Simulation Supported execution mode(s) Inside single-cycle Timed Loop Inside single-cycle Timed Loop Outside single-c

### Caveats for Using DSP48E and DSP48E1 Functions

The following table describes the differences between compiling a DSP48E or DSP48E1 function for an FPGA target and exporting the function for simulation:

|  | Execution on an FPGA Target | Simulation |
| --- | --- | --- |
| Supported execution mode(s) | Inside single-cycle Timed Loop | Inside single-cycle Timed Loop Outside single-cycle Timed Loop |
| Wiring restrictions for optional terminals: | You can wire the acout output of one function only to the acin input of another function. You can wire the bcout output of one function only to the bcin input of another function. You can wire the pcout output of one function only to the pcin input of another function. You can wire the multsignout output of one function only to the multsignin input of another function. You can wire the carrycascout output of one function only to the carrycascin input of another function. You cannot create branches for these wires, probe them, or create indicators for these output terminals. | You can create branches for these wires, probe them, and create indicators for the output terminals. |

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- Debugging FPGA VIs Using a Third-Party Simulator
- Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function
- Configuring DSP48E and DSP48E1 Functions

<!--NI_TOPIC bundle=labview-fpga-module path=changing-arbitration-options-fpga-module.html language=enus -->
## TOPIC 00017: Changing Arbitration Options

- bundle_id: `labview-fpga-module`
- source_path: `changing-arbitration-options-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/changing-arbitration-options-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, LabVIEW performs arbitration for all shared resources except for FPGA I/O. FPGA I/O default behavior is dependent upon the FPGA target and FPGA I/O resource. You can customize the arbitration options for FPGA I/O and FPGA FIFO items in the Project Explorer window if you need to optimize

### Changing Arbitration Options

By default, LabVIEW performs arbitration for


 all shared resources except for FPGA I/O. FPGA I/O default behavior is


 dependent upon the FPGA target and FPGA I/O resource. You can customize the


 arbitration options for FPGA I/O and FPGA


 FIFO items in the Project


 Explorer window if you need to optimize the FPGA VI. The default


 arbitration option varies according to the type of shared resource target and the


 I/O.

#### Changing Arbitration Options of an FPGA I/O Item

Complete the following steps to change the arbitration option of an FPGA I/O item in


 the Project Explorer window.

1. Right-click the FPGA I/O item in the Project Explorer 


 window and select Properties from the shortcut menu. The


 FPGA I/O Properties dialog box appears.
2. Select the Advanced Code Generation from the


 Category list.
3. Select the arbitration options you want from the pull-down menus.

#### Changing Arbitration Options of an FPGA FIFO Item

Complete the following steps to change the arbitration option of an FPGA FIFO item in


 the Project Explorer window.

1. Right-click the FIFO item in the Project Explorer window


 and select Properties from the shortcut menu. The FIFO Properties dialog box appears.
2. Select Interfaces from the Category 


 list.
3. Select the arbitration options you want from the pull-down menus.

Parent topic:

Managing Shared Resources

Related concepts:

- Creating FPGA I/O Items

<!--NI_TOPIC bundle=labview-fpga-module path=changing-simulation-behavior-fpga-module.html language=enus -->
## TOPIC 00018: Changing Simulation Behavior

- bundle_id: `labview-fpga-module`
- source_path: `changing-simulation-behavior-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/changing-simulation-behavior-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to change the simulation behavior that LabVIEW assigns to a synthesis file. Select one or more synthesis files in the IP Source table. Click the Set Simulation Behavior button: LabVIEW displays the Set Simulation Behavior dialog box. Select a new simulation behavior and

### Changing Simulation Behavior

Complete the following steps to change the simulation behavior


 that LabVIEW assigns to a synthesis file.

1. Select one or more synthesis files in the IP Source 


 table.
2. Click the Set Simulation Behavior button: [IMAGE alt='image' src='GUID-0D693026-8BFD-4943-B732-094A74B2FC44-a5.png'] LabVIEW displays the Set Simulation


 Behavior dialog box.
3. Select a new simulation behavior and configure as appropriate. If you want, you


 can exclude the file from simulation altogether. Note 
LabVIEW dims certain simulation behaviors depending on the types of


 synthesis files you select.NI recommends selecting the


 User-defined option for netlist synthesis


 files. This option requires one or more .vhd files


 that define the simulation model. If you do not have these


 .vhd files, you can select the


 Post-synthesis model option to have


 LabVIEW generate a .vhd file during simulation.


 However, selecting this option greatly increases the simulation run


 time due to sub-optimal VHDL generation.You cannot select


 the Same as synthesis option for netlist


 synthesis files.
4. Click the OK button to return to the configuration


 wizard.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=changing-the-top-level-fpga-target-clock-rate-fpga-module.html language=enus -->
## TOPIC 00019: Changing the Top-Level FPGA Target Clock Rate

- bundle_id: `labview-fpga-module`
- source_path: `changing-the-top-level-fpga-target-clock-rate-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/changing-the-top-level-fpga-target-clock-rate-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each FPGA target provides at least one clock to control the internal operations of the FPGA. FPGA target clocks determine the execution rate of the individual VIs and functions on the FPGA VI block diagram. You can compile FPGA VIs with faster clock rates for higher performance. However, not all FPG

### Changing the Top-Level FPGA Target Clock Rate

Each FPGA target provides at least one clock to control the internal operations of the FPGA.


 FPGA target clocks determine the execution rate of the individual VIs and functions


 on the FPGA VI block diagram. You can compile FPGA VIs with faster clock rates for


 higher performance. However, not all FPGA VIs can compile properly with faster clock


 rates. If you select a clock rate that is too fast for the FPGA VI, the Compilation Status window tells you the compilation


 failed because of a timing violation. You must fix the timing violation and try to compile again.

You can change the top-level FPGA target clock rate for an FPGA target by


 right-clicking the FPGA target in the Project


 Explorer window and selecting Properties from the


 shortcut menu. On the Top-Level Clock page of the FPGA


 Target Properties dialog box, you can set the top-level clock. You also


 can change the clock rate for a single-cycle Timed


 Loop within an FPGA VI by double-clicking the Input


 Node and selecting a clock rate in the Configure Timed


 Loop dialog box. You can select the FPGA target top-level clock or a


 clock you derive from the FPGA target base clock.

If you change the top-level FPGA target clock rate or the clock


 rate of a single-cycle Timed Loop in the FPGA VI, you must recompile the


 FPGA VI.

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Troubleshooting Timing Violations
- Executing Code in Single-Cycle Timed Loops
- Implementing Multiple Clock Domains

<!--NI_TOPIC bundle=labview-fpga-module path=check-dram-on-FPGA-target.html language=enus -->
## TOPIC 00020: Check DRAM Availability on an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `check-dram-on-FPGA-target.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/check-dram-on-FPGA-target.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to verify whether DRAM is available for an FPGA target in LabVIEW. Ensure you have the following: Access to Project Explorer. The FPGA target added to your LabVIEW project. If DRAM is available, you can configure memory partitions and arbitration settings on the DRAM Properties page.Carry

### Check DRAM Availability on an FPGA
 Target

Learn how to verify whether DRAM is available for an FPGA target in LabVIEW.

- Access to Project Explorer .
- The FPGA target added to your LabVIEW project.

Note

DRAM
 Properties

1. Open Project Explorer.
2. Right-click the FPGA target and select Properties.
3. Verify DRAM availability in the Category list on the
 left side of the dialog box.
  - If DRAM Properties appears, the target supports
 DRAM.
  - If DRAM Properties does not appear, DRAM is not
 available for this target.

Parent topic:

Using DRAM

Related concepts:

- Using DRAM

<!--NI_TOPIC bundle=labview-fpga-module path=choosing-between-the-fifo-implementation-options-fpga-module.html language=enus -->
## TOPIC 00021: Choosing between the FIFO Implementation Options

- bundle_id: `labview-fpga-module`
- source_path: `choosing-between-the-fifo-implementation-options-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/choosing-between-the-fifo-implementation-options-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Understanding the available FIFO implementation options can help you create more efficient FPGA designs. The FIFO implementation options specify how the FPGA represents target-scoped and VI-defined FIFOs in hardware. Use the FIFO Properties dialog box to select a FIFO implementation option. DMA and

### Choosing between the FIFO Implementation Options

Understanding the available FIFO implementation options can help you create more


 efficient FPGA designs. The FIFO implementation options specify how the FPGA


 represents target-scoped and VI-defined FIFOs in hardware. Use the FIFO


 Properties dialog box to select a FIFO implementation option.

Note

The following table helps you determine which FIFO implementation best suits your


 application.

| Implementation | What Does It Do? | What Considerations Should I Keep in Mind? |
| --- | --- | --- |
| Flip-Flops | Flip-flops are FPGA resources that you can use for data storage or other tasks, such as addition and subtraction. For this reason, flip-flops are often the least abundant FPGA resource for moving or storing data. | You cannot use FIFOs implemented using flip-flops across multiple clock domains. |
| Look-up Tables (LUTs) | Look-up tables, also known as distributed RAM, consist of logic gates hard-wired on the FPGA. Like flip-flops, LUTs can function as FPGA resources. | You cannot use FIFOs implemented using look-up tables across multiple clock domains. |
| Block Memory | Block memory, also known as block random access memory, block RAM or BRAM, is a dedicated FPGA resource for data storage. Refer to Implementing Block Memory FIFOs for more information about using built-in control logic with a block memory implementation. If you configure a target-scoped or VI-defined FIFO using block memory, you can configure the control logic. DMA and peer-to-peer FIFOs can use only block memory. | If you select the Block Memory option, you might not be able to read data in a target-scoped or VI-defined FIFO until up to six clock cycles after you write the data to the FIFO. If you select the timeout interface, wire the Timed Out? output of the FIFO Method Node configured with the Read method to determine whether the upstream data is ready. If you select the handshaking interface, wire the Output Valid output of the FIFO Method Node configured with the Read method to determine whether the upstream data is ready. |
| UltraRAM | UltraRAM, also known as URAM, is a flexible, high-density, and large-size memory building block available on most Xilinx UltraScale+ targets. UltraRAM has eight times the capacity of a block memory but is less flexible in data width and address space configuration than block memory. Use UltraRAM as a storage element for large local FIFOs. | You cannot use FIFOs implemented using UltraRAM across multiple clock domains. The Get Number of Elements to Read and Get Number of Elements to Write methods do not support FIFOs implemented using UltraRAM. |

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Implementing Multiple Clock Domains
- Implementing Block Memory FIFOs

<!--NI_TOPIC bundle=labview-fpga-module path=choosing-between-the-fifo-interface-options-fpga-module.html language=enus -->
## TOPIC 00022: Choosing between the FIFO Interface Options

- bundle_id: `labview-fpga-module`
- source_path: `choosing-between-the-fifo-interface-options-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/choosing-between-the-fifo-interface-options-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Understanding the available FIFO interface options can help you reduce the amount of code required to implement timeout and handshaking protocols for FIFOs. The FIFO interface options change the inputs and outputs available on certain FIFO methods. To select between the timeout and handshaking inter

### Choosing between the FIFO Interface Options

Understanding the available FIFO interface options can help you reduce the amount of


 code required to implement timeout and handshaking protocols for FIFOs. The FIFO


 interface options change the inputs and outputs available on certain FIFO methods.


 To select between the timeout and handshaking interfaces, right-click a FIFO Method


 Node that invokes a Read or Write method within a single-cycle Timed Loop and select


 Interface»Timeout or


 Interface»Handshaking from the shortcut menu.

The following table helps you determine which FIFO interface best suits your


 application.

| Interface | What Does It Do? | When Is It Available for Use? |
| --- | --- | --- |
| Timeout | Specifies a time, in number of clock ticks, that the method waits to complete an operation before it returns a timeout. The timeout interface helps you handle unresponsive devices or sections of code by enabling the following inputs and outputs: Timeout and Timed Out?. | This interface is the default interface available on all FIFOs that invoke the Read, Write, or Flush and Disable methods. |
| Handshaking | Facilitates communication between upstream and downstream nodes in high throughput applications. The handshaking interface reduces the amount of logic needed to implement a handshaking protocol by enabling the following inputs and outputs on the FIFO Method Node: Input Valid, Ready for Output, Output Valid, and Ready for Input. | This interface is available only within a single-cycle Timed Loop for FIFOs that invoke Read or Write methods. Additionally, some targets do not support the handshaking interface for peer-to-peer and DMA FIFOs. LabVIEW returns a compile time error for FIFOs that do not support the handshaking interface. |

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

<!--NI_TOPIC bundle=labview-fpga-module path=clearing-fpga-fifos-fpga-module.html language=enus -->
## TOPIC 00023: Clearing FPGA FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `clearing-fpga-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clearing-fpga-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you run the FPGA VI on a development computer with real I/O, LabVIEW clears FIFOs when the FPGA VI stops and then starts again. When you run the FPGA VI on an FPGA target using interactive front panel communication, LabVIEW does not clear FIFOs when the FPGA VI stops and then starts again. To c

### Clearing FPGA FIFOs

When you run the FPGA VI on a development computer with real I/O, LabVIEW clears


 FIFOs when the FPGA VI stops and then starts again. When you run the FPGA VI on an


 FPGA target using interactive front panel communication, LabVIEW does not


 clear FIFOs when the FPGA VI stops and then starts again. To clear target-scoped or


 VI-defined FIFOs on the FPGA, use the Clear method of the


 FIFO Method Node. You also can right-click the VI in the


 Project Explorer window and select


 Download from the shortcut menu to clear FIFOs.

When you control an FPGA VI using programmatic FPGA


 interface communication, use the Stop method of the Invoke Method function to clear individual DMA FIFOs from the host VI.


 You also can clear all FIFOs using the Reset method on the Invoke Method function or


 the Close FPGA VI Reference function with the


 Close and Reset if Last Reference shortcut menu option


 selected. In addition to clearing FIFOs, the Reset method and Close and


 Reset if Last Reference option complete other tasks.

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Debugging FPGA VIs Using Simulation Mode

<!--NI_TOPIC bundle=labview-fpga-module path=clip-tutorial-adding-component-level-ip-to-an-fpga-project-fpga-module.html language=enus -->
## TOPIC 00024: CLIP Tutorial: Adding Component-Level IP to an FPGA Project

- bundle_id: `labview-fpga-module`
- source_path: `clip-tutorial-adding-component-level-ip-to-an-fpga-project-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clip-tutorial-adding-component-level-ip-to-an-fpga-project-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use this tutorial to learn how to manually create and use CLIP in an FPGA project. However, NI recommends using the CLIP Wizard to import IP into an FPGA project as CLIP. To add CLIP to an FPGA project without using the CLIP Wizard, you must complete the following steps: Create or acquire th

### CLIP Tutorial: Adding Component-Level IP to an
 FPGA Project

You can use this tutorial to learn how to manually create and use CLIP in an FPGA


 project. However, NI recommends using the CLIP


 Wizard to import IP into an FPGA project as CLIP.

To add CLIP to an FPGA project without using the CLIP Wizard, you must complete the


 following steps:

1. Create or acquire the IP.
2. Define the interface to the IP using a declaration XML file.
3. Declare the CLIP in the properties of an FPGA target.
4. Add a CLIP item to a LabVIEW project.
5. Pass data between CLIP and an FPGA VI.

| Next: CLIP Tutorial, Part 1: Creating VHDL Code |
| --- |

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- Creating or Acquiring IP
- Defining the IP Interface
- Adding Component-Level IP to a Project
- Passing Data between Component-Level IP and VIs
- CLIP Tutorial, Part 1: Creating VHDL Code
- Using VHDL Code as Component-Level IP

<!--NI_TOPIC bundle=labview-fpga-module path=clip-tutorial-part-1-creating-vhdl-code-fpga-module.html language=enus -->
## TOPIC 00025: CLIP Tutorial, Part 1: Creating VHDL Code

- bundle_id: `labview-fpga-module`
- source_path: `clip-tutorial-part-1-creating-vhdl-code-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clip-tutorial-part-1-creating-vhdl-code-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To add component-level IP (CLIP) to an FPGA target, you must provide IP, in the form of VHDL code, to compile into the FPGA target. The tutorial uses a 16-bit adder with a flip-flop. The following VHDL code takes two I16 numeric values and returns their sum as an I16 numeric value. The VHDL code als

### CLIP Tutorial, Part 1: Creating VHDL Code

To add component-level IP (CLIP) to an FPGA target, you must provide IP, in the form
 of VHDL code, to compile into the FPGA target.

The tutorial uses a 16-bit adder with a flip-flop.

The following VHDL code takes two I16 numeric values and returns their sum as an I16
 numeric value. The VHDL code also requires a clock and a reset signal from the FPGA
 Module. If you want to use this example code, copy the code to a text file and save
 the file as DemoClipAdder.vhd.

Note

keep_hierarchy

```text
Library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity DemoClipAdder is
    port (
          clk : in std_logic;
          aReset : in std_logic;
          cPortA : in std_logic_vector(15 downto 0);
          cPortB : in std_logic_vector(15 downto 0);
          cAddOut : out std_logic_vector(15 downto 0) := (others => '0')
        );
end DemoClipAdder;

architecture rtl of DemoClipAdder is
    attribute keep_hierarchy : string;
    attribute keep_hierarchy of rtl : architecture is "yes";
begin
    process(aReset, clk) begin
      if(aReset = '1') then
        cAddOut <= (others => '0');
      elsif rising_edge(clk) then
        cAddOut <= std_logic_vector(signed(cPortA) + signed(cPortB));
      end if;
    end process;
end rtl; 
```

#### Adding Constraints to CLIP

The following UCF code constrains the clock rate of the sum output to be no less than
 100 MHz. If you want to use this example code, copy the code to a text file and save
 the file as (Xilinx ISE)DemoClipAdder.ucf or (Xilinx
 Vivado)DemoClipAdder.xdc. Add this constraints file along with
 the VHD file as synthesis files in the Configuring CLIP wizard to implement this
 constraint.

(Xilinx ISE)

```text
NET "%ClipInstancePath%/cAddOut*" TNM_NET = %ClipInstanceName%AddOut;
TIMESPEC TS_%ClipInstanceName%ThruAdder = TO "%ClipInstanceName%AddOut" 10 ns;
```

(Xilinx Vivado)

```text
create_clock -period 10.000 -name %ClipInstanceName%Clk -waveform {0.000 5.000} -add [get_pins %ClipInstancePath%/clk]
set_clock_latency -clock [get_clocks {%ClipInstanceName%Clk}] 10.0 [get_pins {%ClipInstancePath%/cAddOut[0]}]
```

| Previous: CLIP Tutorial: Adding Component-Level IP to an FPGA Project | Next: CLIP Tutorial, Part 2: Defining the Interface |
| --- | --- |

Parent topic:

CLIP Tutorial: Adding Component-Level IP to an FPGA Project

Related concepts:

- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- Using VHDL Code as Component-Level IP
- Creating or Acquiring IP
- Using the Configure Component-Level IP Wizard
- CLIP Tutorial, Part 2: Defining the Interface

<!--NI_TOPIC bundle=labview-fpga-module path=clip-tutorial-part-2-defining-the-interface-fpga-module.html language=enus -->
## TOPIC 00026: CLIP Tutorial, Part 2: Defining the Interface

- bundle_id: `labview-fpga-module`
- source_path: `clip-tutorial-part-2-defining-the-interface-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clip-tutorial-part-2-defining-the-interface-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To add IP as a component-level IP (CLIP) item in a LabVIEW project, the IP must have an accompanying declaration XML file to define the I/O for LabVIEW. You can use the Configure Component-Level IP wizard to create this file automatically from the example DemoClipAdder.vhd file. Complete the followi

### CLIP Tutorial, Part 2: Defining the Interface

To add IP as a component-level IP (CLIP) item in a LabVIEW project, the IP must have


 an accompanying declaration XML file to define the I/O for LabVIEW.

You can use the Configure Component-Level IP wizard to create this file automatically


 from the example DemoClipAdder.vhd file. Complete the following steps to create


 the declaration XML file using the CLIP wizard.

1. Right-click the FPGA target in the Project


 Explorer window and select Properties from the


 shortcut menu.
2. On the Component-Level IP page of the FPGA Target Properties dialog box, click the


 Create File button.
3. On the Name and Source page of the CLIP wizard, click the


 Add Synthesis File button.
4. Select DemoClipAdder.vhd and click the


 OK button to add the file.
5. (Optional) Select (Xilinx ISE) DemoClipAdder.ucf or (Xilinx


 Vivado) DemoClipAdder.xdc and click the


 OK button to add the file.
6. Click the Next button.
7. Follow the instructions in the rest of the CLIP wizard to finish creating the


 declaration XML file. Tip Click the Help


 button on each page of the wizard for more information about the available


 options.
8. Click the Finish button to complete the configuration and


 create the declaration XML file.

The CLIP wizard automatically adds the CLIP to the project.

| Previous: CLIP Tutorial, Part 1: Creating VHDL Code | Next: CLIP Tutorial, Part 3: Adding CLIP to a Project |
| --- | --- |

Parent topic:

CLIP Tutorial: Adding Component-Level IP to an FPGA Project

Related concepts:

- CLIP Tutorial, Part 1: Creating VHDL Code
- Defining the IP Interface
- Using the Configure Component-Level IP Wizard
- CLIP Tutorial, Part 3: Adding CLIP to a Project

<!--NI_TOPIC bundle=labview-fpga-module path=clip-tutorial-part-3-adding-clip-to-a-project-fpga-module.html language=enus -->
## TOPIC 00027: CLIP Tutorial, Part 3: Adding CLIP to a Project

- bundle_id: `labview-fpga-module`
- source_path: `clip-tutorial-part-3-adding-clip-to-a-project-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clip-tutorial-part-3-adding-clip-to-a-project-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You add a component-level IP (CLIP) item to the LabVIEW project to instantiate the CLIP inside the FPGA. Complete the following steps to add a CLIP item in a project: Create a new project and save the project as CLIP Demo.lvproj. Add an FPGA target that supports CLIP to the project. Right-click the

### CLIP Tutorial, Part 3: Adding CLIP to a Project

You add a component-level IP (CLIP) item to the LabVIEW project to


 instantiate the CLIP inside the FPGA.

Complete the following steps to add a CLIP item in a project:

1. Create a new project and save the project as


 CLIP Demo.lvproj .
2. Add an FPGA target that supports CLIP to the


 project.
3. Right-click the FPGA target and select Properties from


 the shortcut menu to display the FPGA


 Target Properties dialog box.
4. Select Component-Level IP from the


 Category list to display the Component-Level IP Properties page.
5. Click the Add button, select the


 DemoClipAdder.xml file, and click the


 OK button. Note The CLIP wizard automatically adds the declaration XML file to the


 project.
6. Click the OK button to close the FPGA


 Target Properties dialog box.
7. Right-click the FPGA target in the Project


 Explorer window and select New»Component-Level


 IP from the shortcut menu.
8. On the General page of the Component-Level IP Properties dialog box, enter Adder


 CLIP in the Name field and select


 DemoClipAdder from the Component-Level IP


 Declaration pull-down menu.
9. (Optional) On the Clock


 Selections page, select a clock. By default, the DemoClipAdder


 example uses the top-level FPGA clock, so you do not need to change the clock.
10. Click the OK button. Notice that the Project Explorer window now includes a CLIP item, as


 well as the I/O defined in the declaration XML file.

| Previous: CLIP Tutorial, Part 2: Defining the Interface | Next: CLIP Tutorial, Part 4: Passing Data between CLIP and VIs |
| --- | --- |

Parent topic:

CLIP Tutorial: Adding Component-Level IP to an FPGA Project

Related concepts:

- Adding Component-Level IP to a Project
- CLIP Tutorial, Part 2: Defining the Interface
- Using the Configure Component-Level IP Wizard
- CLIP Tutorial, Part 4: Passing Data between CLIP and VIs

<!--NI_TOPIC bundle=labview-fpga-module path=clip-tutorial-part-4-passing-data-between-clip-and-vis-fpga-module.html language=enus -->
## TOPIC 00028: CLIP Tutorial, Part 4: Passing Data between CLIP and VIs

- bundle_id: `labview-fpga-module`
- source_path: `clip-tutorial-part-4-passing-data-between-clip-and-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/clip-tutorial-part-4-passing-data-between-clip-and-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You pass data between component-level IP (CLIP) and VIs using an FPGA I/O Node in an FPGA VI. Complete the following steps to use an FPGA I/O Node to access CLIP I/O. In Demo CLIP.lvproj, right-click the FPGA target and select New»VI from the shortcut menu to create a new FPGA VI. Add a Flat Sequenc

### CLIP Tutorial, Part 4: Passing Data between CLIP and VIs

You pass data between component-level IP (CLIP) and VIs using an FPGA


 I/O Node in an FPGA VI.

Complete the following steps to use an FPGA I/O Node to access CLIP I/O.

1. In Demo CLIP.lvproj , right-click the FPGA target and select


 New»VI from the shortcut menu to create a new FPGA


 VI.
2. Add a Flat Sequence structure to the FPGA VI.
3. Drag the PortA I/O item from the project to inside the


 Flat Sequence structure.
4. Right-click the Adder CLIP/Port A input, select


 Create»Constant from the shortcut menu, enter a value


 of 5 for the constant, and label the constant


 Offset .
5. Right-click the Flat Sequence structure and select Add Frame


 After from the shortcut menu.
6. Drag the PortB I/O item from the project to inside empty


 frame of the Flat Sequence structure.
7. Right-click the Adder CLIP/Port B input on the FPGA I/O


 Node, select Create»Control from the shortcut menu, and


 label the control Position .
8. Expand the FPGA I/O Node to add AdderOut .
9. Right-click the Adder CLIP/AdderOut output, select


 Create»Indicator from the shortcut menu, and label


 the indicator Position + Offset .
10. Include the FPGA I/O Node within a While loop, as shown in the following block


 diagram:

[IMAGE alt='image' src='GUID-8BEF5E9D-FAD6-40F6-8D0D-77B8BBA3EB44-a5.png']

The block diagram writes a constant, which is an offset value, to the Port A input.


 In the While Loop, the FPGA I/O Node adds the offset to a position to create a new


 position.

| Previous: CLIP Tutorial, Part 3: Adding CLIP to a Project |
| --- |

Parent topic:

CLIP Tutorial: Adding Component-Level IP to an FPGA Project

Related concepts:

- CLIP Tutorial, Part 3: Adding CLIP to a Project
- Passing Data between Component-Level IP and VIs

<!--NI_TOPIC bundle=labview-fpga-module path=communicating-with-an-fpga-vi-executing-in-simulation-mode-fpga-interface.html language=enus -->
## TOPIC 00029: Communicating with an FPGA VI Executing in Simulation Mode

- bundle_id: `labview-fpga-module`
- source_path: `communicating-with-an-fpga-vi-executing-in-simulation-mode-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/communicating-with-an-fpga-vi-executing-in-simulation-mode-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following list describes behavior to consider when you use a host VI to communicate with an FPGA VI that is executing in simulation mode using simulated I/O: You must run the host VI on a development computer running a Windows operating system to communicate with the FPGA VI. You cannot execute

### Communicating with an FPGA VI Executing in Simulation Mode

The following list describes behavior to consider when you use a host VI to


 communicate with an FPGA VI that is executing in simulation mode using simulated


 I/O:

- You must run the host VI on a development computer running a Windows operating


 system to communicate with the FPGA VI. You cannot execute the host VI on an RT


 target when you want to use simulated I/O.
- To execute different code on the host VI based on where the FPGA VI executes,


 use the Invoke Method function configured for the Get FPGA VI Execution Mode


 method.
- The Up Cast function, the Dynamic FPGA Interface Cast function, and the Abort,


 Reset, and Download methods on the Invoke Method function do not support


 executing the FPGA VI in simulation mode. If you use these functions or methods,


 the host VI returns a run-time error.
- Direct Memory Access (DMA) FIFOs are valid while either the host VI or FPGA VI


 is executing. If both VIs stop executing, DMA FIFOs lose all data.
- Interrupts are valid only when the FPGA VI is executing. If the FPGA VI stops


 executing, all interrupt data is lost and any host interface waits return


 immediately.
- If you use the Invoke Method function to read DMA FIFOs, the function might


 timeout more frequently because the FPGA VI is not executing as fast in


 simulation mode as it would on an FPGA target.
- You must close the front panel window of the FPGA VI before executing the FPGA


 VI if you want to use the Close FPGA VI Reference function to close the


 reference, stop the FPGA VI, and reset the FPGA VI executing in simulation mode.


 You must open the front panel window of the FPGA VI before executing the FPGA VI


 if you want to use the Close FPGA VI Reference function to close the host


 reference without resetting the FPGA VI executing in simulation mode.

Parent topic:

Communicating with FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=communicating-with-fpga-targets-from-a-host-computer-fpga-module.html language=enus -->
## TOPIC 00030: Communicating with FPGA Targets from a Host Computer

- bundle_id: `labview-fpga-module`
- source_path: `communicating-with-fpga-targets-from-a-host-computer-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/communicating-with-fpga-targets-from-a-host-computer-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can communicate with the FPGA target in the following ways: Interactive front panel communication—Displays the front panel window of the FPGA VI on the host computer while the FPGA target executes the block diagram. Programmatic FPGA interface communication—Uses a separate VI running on an exter

### Communicating with FPGA Targets from a Host Computer

You can communicate with the FPGA target in the following ways:

- Interactive front panel communication—Displays the front panel


 window of the FPGA VI on the host computer while the FPGA target executes the


 block diagram.
- Programmatic FPGA interface communication—Uses a separate VI running


 on an external computer to control, monitor, and transfer data with the FPGA


 target. The VI you use to programmatically control and monitor the FPGA VI is


 called the host VI and the computer that runs the host VI is called the host


 computer.
- Peer-to-peer streaming—Transfers data between


 hardware devices.

The following table summarizes and compares these methods.

| Communication Method | Host OS | Control & Monitoring Mechanism | Common Use | Notes |
| --- | --- | --- | --- | --- |
| Interactive front panel communication | Windows | Front panel of FPGA VI | Simple logic verification Simple debugging | Not all targets support Does not require creating a VI to run on the host computer Does not support communication using DMA FIFOs or FPGA interrupts |
| Programmatic FPGA interface communication | Windows, RT | VI running on host | Data logging on the host Integration of FPGA, RT, and desktop components into one application Operations that cannot be performed on the FPGA Test benches Interacting with remote FPGA targets Applications that use DMA FIFOs or FPGA interrupts | Most common programming method Supports programmatic front panel communication |
| Peer-to-peer streaming | Windows, RT | VI running on host | Streaming data between two FPGA targets without going through the host processor Streaming data from multiple digitizers to an FPGA target Pipelining data from a digitizer to an FPGA target to a signal generator | Not all targets support Requires two targets as well as host computer |

NI recommends using programmatic FPGA interface communication and host VIs when


 possible. The advantage of using interactive front panel communication to


 communicate with an FPGA VI is that you do not need to program any additional VIs.


 However, using interactive front panel communication is not as powerful as using


 programmatic FPGA interface communication.

#### Using Interactive and Programmatic Communication Simultaneously

Although you can use both interactive front panel communication and programmatic FPGA


 interface communication simultaneously, NI recommends controlling and monitoring the


 FPGA VI with one communication option at a time. To debug the FPGA VI effectively


 using both communication options simultaneously, consider controlling the reading


 and writing of data from the host VI and monitoring the execution of the FPGA VI


 using interactive front panel communication.

Parent topic:

Storing and Transferring Data

Related concepts:

- Interactive Front Panel Communication
- Using a Host VI to Communicate with the FPGA Target
- Programming FPGAs Overview

<!--NI_TOPIC bundle=labview-fpga-module path=communicating-with-fpga-vis-fpga-interface.html language=enus -->
## TOPIC 00031: Communicating with FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `communicating-with-fpga-vis-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/communicating-with-fpga-vis-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The topics in this section provide functions and procedures that enable host VIs to communicate with FPGA VIs.

### Communicating with FPGA VIs

The topics in this section provide functions and procedures that enable host VIs to communicate
 with FPGA VIs.

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=labview-fpga-module path=compiling-an-fpga-vi-remotely-fpga-module.html language=enus -->
## TOPIC 00032: Compiling an FPGA VI Remotely

- bundle_id: `labview-fpga-module`
- source_path: `compiling-an-fpga-vi-remotely-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/compiling-an-fpga-vi-remotely-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can compile an FPGA VI on a computer other than the development computer. You might want to compile on another computer if the development computer is slow or does not have enough memory to compile the VI for the FPGA target. By default, LabVIEW uses the compile server and compile worker install

### Compiling an FPGA VI Remotely

You can compile an FPGA VI on a computer other than the development computer. You


 might want to compile on another computer if the development computer is slow or


 does not have enough memory to compile the VI for the FPGA target.

By default, LabVIEW uses the compile server and compile worker installed on the local


 computer. The compile server automatically installs with the FPGA Module on the


 local computer. However, you must install the FPGA Compile Farm Server on any remote


 computer you want to use as the compile server, and you must install the Xilinx


 compilation tools on any computer(s) you want to use as a compile worker.

Complete the following steps to configure LabVIEW to compile an FPGA VI on a remote


 computer.

1. Install the necessary Xilinx compilation tools on the remote computer.
2. Navigate to the FPGA\CompileWorker\ directory and run


 FPGACompileFarmConfiguration.exe .
3. Place a checkmark in the Allow users to connect remotely to this


 compile server checkbox and click


 OK .
4. Navigate to the FPGA\CompileWorker\ directory to launch the


 compile worker. Note You must launch the compile worker from the


 computer on which it is executing. You cannot launch the compile worker


 remotely.
5. Leave the compile worker running on the remote computer.
6. On the local computer, open the FPGA project that contains the FPGA VI you want


 to compile.
7. Select Tools»Options to display the


 Options dialog box.
8. Select FPGA Module from the


 Category list to display the FPGA Module


 Options dialog box.
9. Select Connect to a compile server in the


 Compile Server section.
10. Type the name or IP address of the remote computer running the compile server in


 the Host name text box.
11. (Optional) Type the user name and password necessary to log into the remote


 compile server. By default, the User name is


 admin and the Password text box is


 empty.
12. Click OK .
13. Compile the FPGA VI. If LabVIEW is unable to contact the compile server, LabVIEW


 displays an error in the Compilation Status window.


 Otherwise, LabVIEW compiles the FPGA VI on the remote computer every time you


 compile an FPGA VI.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Understanding the LabVIEW FPGA Compile System
- Getting Started with a Compile Farm

Related information:

- Installing the LabVIEW FPGA Compile Server on a Remote Computer
- NI LabVIEW FPGA Compilation Options

<!--NI_TOPIC bundle=labview-fpga-module path=compiling-downloading-and-running-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00033: Compiling, Downloading, and Running FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `compiling-downloading-and-running-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/compiling-downloading-and-running-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must compile an FPGA VI into a bitfile before you can download and run the FPGA VI on an FPGA target. The following sections outline the build process. Creating an FPGA VI Build Specification You must create a build specification to compile an FPGA VI into a bitfile for the FPGA. Build specifica

### Compiling, Downloading, and Running FPGA
 VIs

You must compile an FPGA VI into a bitfile before you can download and run the FPGA


 VI on an FPGA target. The following sections outline the build process.

#### Creating an FPGA VI Build Specification

You must create a build specification to compile an FPGA VI into a bitfile for the


 FPGA. Build specifications give the compiler instructions on how to create the


 bitfile.

Complete the following steps to create a build specification through the


 Project Explorer window.

1. Right-click Build Specifications in the Project
 Explorer window and select
 New»Compilation from the shortcut menu to display the
 Compilation Properties dialog box. You also can right-click an existing build
 specification in the Project Explorer window and select
 Properties from the shortcut menu to display this
 dialog box.
2. Specify the build specification name and other descriptive information on the


 Information page of the dialog box.
3. Display the Source Files page to specify the top-level VI. FPGA VIs can have


 only one top-level VI.
4. If available for your FPGA target, configure the Xilinx build options on the


 Xilinx Options page.
5. Click the OK button to close the dialog box or click the


 Build button to begin compiling the FPGA VI.

#### Compiling an FPGA VI

To compile an FPGA VI, you must set the execution mode of the FPGA target to execute


 FPGA VIs on the target. Right-click the target and select Select


 Execution Mode»FPGA Target from the shortcut menu.

You can compile FPGA VIs in the following ways:

- Click the Run button to compile the FPGA VI. If the FPGA


 target you use supports interactive front panel communication, LabVIEW


 automatically runs the FPGA VI on the FPGA target. Clicking the


 Run button compiles the VI only if the VI or project


 has changed since you last compiled the VI.
- Right-click an FPGA build specification in the Project


 Explorer window and select Build or


 Rebuild from the build specification shortcut


 menu.

The compilation process goes through several stages. Compiling FPGA VIs can take from


 a few minutes to a few hours. NI recommends testing and debugging an FPGA VI before


 you compile it.

#### Downloading a Compiled FPGA VI

After you compile the FPGA VI, you can download and run the FPGA VI on the FPGA


 target.

Note

You can download the compiled VI in the following ways.

- Right-click a compilation build specification in the Project


 Explorer window and select Download from


 the shortcut menu to download the FPGA VI.
- Programmatically force the FPGA VI to download using FPGA interface


 functions.
- If the target supports interactive front panel communication, click the


 Run button on an FPGA VI. If the FPGA VI is new or


 has changed, the FPGA VI will compile and download to the FPGA target


 automatically after the compilation completes. However, LabVIEW does not


 download the FPGA VI if the VI is already on the FPGA target.
- Store the FPGA VI in flash memory if the target supports flash memory.

If the Run when loaded to FPGA checkbox is enabled in the


 Information page of the Compilation


 Properties dialog box for your FPGA


 build specification, the FPGA VI automatically runs on the FPGA target


 after the download is complete. Otherwise, you must manually run the FPGA VI on the


 FPGA target after you download the FPGA VI.

#### Running a Compiled FPGA VI

You can run the FPGA VI in the following ways.

- Use the FPGA interface to run the FPGA VI. You can build host VIs to


 programmatically read and write to the front panel window of the FPGA VI using


 programmatic FPGA interface communication.
- If the target supports interactive front panel communication, click the


 Run button to run the VI. If you run an FPGA VI using


 interactive front panel communication, you cannot close the FPGA VI without


 stopping the VI running on the FPGA target.
- Run the FPGA VI automatically from the flash memory if the target has flash


 memory.

Related concepts:

- Adding Indicators to Monitor FPGA VIs
- Adding I/O to Monitor FPGA VIs
- Working with FPGA Build Specifications
- Interactive Front Panel Communication
- Understanding the LabVIEW FPGA Compile System
- Downloading an FPGA VI to an FPGA Target
- Downloading an FPGA VI to the Flash Memory of an FPGA Target
- Using a Host VI to Communicate with the FPGA Target
- Running FPGA VIs Automatically from Flash Memory
- Compiling an FPGA VI Remotely
- Estimating FPGA Resource Usage without Compiling
- Using CLIP Clocks
- Viewing the Bitfile Path
- Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-dsp48e-and-dsp48e1-functions-fpga-module.html language=enus -->
## TOPIC 00034: Configuring DSP48E and DSP48E1 Functions

- bundle_id: `labview-fpga-module`
- source_path: `configuring-dsp48e-and-dsp48e1-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-dsp48e-and-dsp48e1-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configuring a DSP48E or DSP48E1 function involves the following steps: Configuring the functionality of the slice, including the multiplier, pre-adder (DSP48E1 only), adder-subtractor or logic unit, and pattern detector Adjusting the length of the internal combinatorial path by adding or removing in

### Configuring DSP48E and DSP48E1 Functions

Configuring a DSP48E or DSP48E1 function involves the following steps:

1. Configuring the functionality of the slice, including the


 multiplier, pre-adder (DSP48E1 only), adder-subtractor or logic unit, and pattern detector
2. Adjusting the length of the internal combinatorial path by adding or


 removing internal registers
3. Deciding which block diagram terminals to show
4. Ensuring the precision of these terminals
5. Viewing the latencies of internal data paths

The following topics provide supplementary information:

- Caveats for using these functions
- Shrinking the functions' icons
- Determining the maximum number of DSP48E or DSP48E1


 functions you can use
- Replacing a DSP48E function with a DSP48E1 function


 and vice versa

#### Tutorials

Refer to the *DSP48E Example: Creating a Complex Multiplier* and *DSP48E Example:
 Creating an n-Tap FIR Filter* tutorials to
 familiarize yourself with these functions.

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- Configuring the Functionality of a DSP48E or DSP48E1 Slice
- Configuring Pattern Detection for a DSP48E or DSP48E1 Function
- Adjusting the Length of the Internal Combinatorial Path of a DSP48E or DSP48E1 Function
- Introduction to FPGA Hardware Concepts
- Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function
- Viewing the Latencies of Data Paths in a DSP48E or DSP48E1 Function
- Caveats for Using DSP48E and DSP48E1 Functions
- DSP48E Example: Creating a Complex Multiplier
- DSP48E Example: Creating an n-Tap FIR Filter
- Introduction to DSP48E and DSP48E1 Slices

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-fpga-base-clocks-fpga-module.html language=enus -->
## TOPIC 00035: Configuring FPGA Base Clocks

- bundle_id: `labview-fpga-module`
- source_path: `configuring-fpga-base-clocks-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-fpga-base-clocks-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the FPGA base clock that is associated with an FPGA target by specifying its name and certain properties. The properties available vary according to FPGA target and FPGA base clock selected. Complete the following steps to configure the FPGA base clock associated with an FPGA targe

### Configuring FPGA Base Clocks

You can configure the FPGA base clock that is associated with an FPGA target by specifying its name and


 certain properties. The properties available vary according to FPGA target and FPGA


 base clock selected. Complete the following steps to configure the FPGA base clock


 associated with an FPGA target.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. If the FPGA target you use does not automatically add an FPGA base clock to the


 Project Explorer window, add the FPGA base clock.
4. Right-click the FPGA base clock in the Project Explorer 


 window and select Properties from the shortcut menu. The


 FPGA Base Clock Properties dialog box appears.
5. Select the options you want to configure.
6. Click the OK button.

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Using FPGA Clocks and Timing
- Adding FPGA Targets to a LabVIEW Project
- Adding an FPGA Base Clock to a LabVIEW Project
- Controlling the FPGA VI Execution Rate

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-fpga-io-items-fpga-module.html language=enus -->
## TOPIC 00036: Configuring FPGA I/O Items

- bundle_id: `labview-fpga-module`
- source_path: `configuring-fpga-io-items-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-fpga-io-items-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the FPGA I/O item in the Project Explorer window or in the FPGA I/O Node on the block diagram. The configuration options you specify in the Project Explorer window apply to the FPGA I/O item on the FPGA target. The options you configure in the FPGA I/O Node only apply to the FPGA I

### Configuring FPGA I/O Items

You can configure the FPGA I/O item in the Project


 Explorer window or in the FPGA I/O Node on the block diagram. The


 configuration options you specify in the Project Explorer


 window apply to the FPGA I/O item on the FPGA target. The options you configure in


 the FPGA I/O Node only apply to the FPGA I/O item in the FPGA Node and not


 throughout the FPGA target.

#### Configuring FPGA I/O Items in the Project Explorer Window

Complete the following steps to configure FPGA I/O items in the Project


 Explorer window.

1. Right-click the FPGA I/O item in the Project Explorer 


 window and select Properties from the shortcut menu to


 display the FPGA I/O


 Properties dialog box.
2. Select General from the Category 


 list to assign a name to the FPGA I/O item.
3. Configure other options that appear under the Category 


 list. Note FPGA I/O configuration options vary according to


 I/O resources and the FPGA target. Some FPGA I/O items cannot be configured.


 Other FPGA I/O items have several configuration options. Select an option


 from the Category list and click the


 Help button, to learn about a configuration


 option available for the FPGA I/O item.

#### Configuring FPGA I/O Items in the FPGA I/O Node

Complete the following steps to configure FPGA I/O items in the FPGA I/O Node.

1. Right-click the FPGA I/O Node and select Properties from


 the shortcut menu to display the FPGA


 I/O Node Properties dialog box.
2. Configure options that appear under FPGA I/O item in the


 Category list. Note FPGA I/O


 configuration options vary according to I/O resources and the FPGA target.


 Some FPGA I/O items cannot be configured. Other FPGA I/O items have several


 configuration options. Select an option from the


 Category list and click the


 Help button, to learn about a configuration


 option available for the FPGA I/O item.

Parent topic:

Using FPGA I/O

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-fpga-targets-fpga-module.html language=enus -->
## TOPIC 00037: Configuring FPGA Targets

- bundle_id: `labview-fpga-module`
- source_path: `configuring-fpga-targets-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-fpga-targets-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure FPGA targets from the Project Explorer window. FPGA target functionality varies depending on the specific target. Refer to the specific FPGA target hardware documentation for information about configuration options available for the target. Create a new project or open an existing

### Configuring FPGA Targets

You can configure FPGA targets from the Project Explorer


 window. FPGA target functionality varies depending on the specific target. Refer to


 the specific FPGA target hardware documentation for information about configuration


 options available for the target.

1. Create a new project or open an existing project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target in the Project Explorer 


 window and select Properties from the shortcut menu. The


 FPGA Target Properties dialog box appears.
4. Select General from the Category 


 list.
5. Enter a Name for the FPGA target. The


 Name identifies the FPGA target in the


 Project Explorer window.
6. If you did not select an existing target when you added the FPGA target to the


 project, enter a Resource for the FPGA target. The


 Resource associates the FPGA target in the


 Project Explorer window with a specific FPGA target


 connected to the development computer, network computer, or RT target. Note You can find the Resource name in NI


 Measurement & Automation Explorer (MAX). For FPGA targets that appear in


 MAX as NI-DAQmx Devices, the Resource is the name of


 the device that you specify in MAX.
7. (Optional) Specify the execution mode you want to use to debug an FPGA VI on the


 Execution Mode page. Note LabVIEW


 displays only the options that the current FPGA target supports.
8. (Optional) Specify the top-level clock on the Top-Level


 Clock page.
9. (Optional) Add, create, or modify component-level IP declaration XML files on


 the Component-Level IP page.
10. (Optional) Configure target-scoped properties for DRAM on the DRAM


 Properties page.
11. (Optional) Configure conditional disable symbols on the Conditional


 Disable Symbols page.
12. Click OK .

Parent topic:

Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-input-and-output-terminals-of-the-high-throughput-math-functions-fpga-module.html language=enus -->
## TOPIC 00038: Configuring Input and Output Terminals of the High Throughput Math Functions

- bundle_id: `labview-fpga-module`
- source_path: `configuring-input-and-output-terminals-of-the-high-throughput-math-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-input-and-output-terminals-of-the-high-throughput-math-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The value ranges of High Throughput Math function input and output terminals depend on the encoding, word length, and integer word length of the terminal. If a terminal is signed, the value range is [–2^( iwl–1), 2^(iwl–1)–2^(–wl+iwl)], where: wl is the word length iwl is the integer word length If

### Configuring Input and Output Terminals of the
 High Throughput Math Functions

The value ranges of High Throughput Math function input and output terminals depend


 on the encoding, word length, and integer word length of the terminal. If a terminal


 is signed, the value range is [–2^( iwl–1),


 2^(iwl–1)–2^(–wl+iwl)],


 where:

- wl is the word length
- iwl is the integer word length

If a terminal is unsigned, the value range is: [0, 2^ iwl


 –2^(–wl + iwl )].

For example, if wl = 16, iwl = 1, and the


 terminal is signed, the value range is [–2^(1–1),


 2^(1–1)–2^(–16+1)], or [–1, 0.999969482421875]. If


 this terminal is unsigned, the value range is [0,


 1.999969482421875].

#### Unsupported Fixed-Point Configurations of Input Terminals

The fixed-point configuration of a terminal refers to the encoding, word length, and


 integer word length of that terminal. The input terminals of some functions, such as


 the High


 Throughput Add function, support all fixed-point configurations that


 LabVIEW supports. The input terminals of other functions, such as the High


 Throughput Exponential function, limit the supported fixed-point


 configurations. Refer to the help topic of a particular function for information


 about fixed-point configurations that the function supports. Access this topic by


 right-clicking a function and selecting Help from the


 shortcut menu.

Note

The following list shows the possible limitations an input terminal might have.

- Unsupported encoding—For example, the High Throughput


 Square Root function does not support a signed data type.
- Unsupported word length and/or integer word length—For example, if you wire data


 to the High Throughput Hyperbolic Sine & Cosine


 function and the encoding of that data type is signed, the function does not


 support an integer word length greater than 1 bit.
- Unsupported value range—For example, if you wire data to the High Throughput Natural Logarithm function, the function does not


 support a value outside the range [1/e, 1).

In some cases, if you wire an unsupported configuration to a terminal, LabVIEW alerts


 you by breaking the wire. You cannot run the function. In other cases, LabVIEW


 coerces the wire to a supported configuration. You can run the function, but this


 coercion might cause the function to behave unexpectedly. If the wire is not broken


 and does not have a coercion dot,


 the input terminal supports that fixed-point configuration.

#### Avoiding Unsupported Fixed-Point Configurations

You can avoid broken or coerced wires on input terminals by using the configuration


 dialog box to specify the fixed-point configuration for a particular input terminal.


 Complete the following steps to configure a terminal in this way.

1. Add the function to the block diagram.
2. Double-click the function. LabVIEW launches the configuration dialog box.
3. Use the Fixed-Point Configuration section to configure


 the data type of the terminal. Depending on the function, LabVIEW dims certain


 options and restricts the values you can enter in other text boxes. If you can


 specify a particular fixed-point configuration by using the configuration dialog


 box, the function supports that configuration.
4. Click the OK button to save changes and close the dialog


 box.

After you complete these steps, you can right-click the input terminal and select


 Create»Control or Create»Constant.


 The control or constant you create has a fixed-point configuration that the function


 supports.

#### Array Support

Some High Throughput Math and Basic Elements functions support arrays. The following


 table summarizes the High Throughput Math and Basic Elements functions with array


 support.

Note

| Function | Array of Integers | Array of Fixed-Point Numbers | Array of Clusters |
| --- | --- | --- | --- |
| High Throughput Add |  |  |  |
| High Throughput Subtract |  |  |  |
| High Throughput Multiply |  |  |  |
| Discrete Delay |  |  |  |
| Accumulator |  |  |  |
| AddSub |  |  |  |

The following considerations apply to the High Throughput Add, High Throughput


 Subtract, and High Throughput Multiply functions.

- If both data inputs are arrays, the two arrays are computed element by


 element.
- If one data input is an array and the other is a scalar, each element of the


 array is computed with the scalar.
- If both data inputs are arrays of different sizes, the terminal with the longer


 array adapts to the shorter array size. A coercion dot appears on the terminal


 with the longer array. For example, if x is an array of


 five elements and y is an array of three elements, the


 fourth and fifth elements of x are discarded. The output


 is an array of the same size.

#### Overflow and Rounding of Output Terminals

The theoretical computed value is the mathematic result regardless of the valid


 range of your output data terminal. If the range of an output terminal is not large


 enough to hold the theoretical computed value, overflow occurs. In this situation,


 the function behaves according to the option you specify in the Overflow


 mode pull-down list in the configuration dialog box. You also can


 specify whether the function displays a Boolean operation


 overflow output terminal on the block diagram. You can use the value


 of this terminal to control how a VI behaves if overflow occurs.

Note

In many situations, you can avoid overflow by placing a checkmark in the


 Adapt to source checkbox in the configuration dialog box


 of the function. If you place a checkmark in this checkbox, LabVIEW attempts to


 adjust the width and range of the output data type such that neither overflow nor


 rounding occurs. However, this adjustment is not possible in all situations. For


 example, if a function involves division, rounding always occurs. Also, some


 functions do not have this checkbox.

Parent topic:

Using the High Throughput Math Functions

Related concepts:

- Using the High Throughput Math Functions

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-labview-for-a-third-party-simulator-fpga-module.html language=enus -->
## TOPIC 00039: Configuring LabVIEW for a Third-Party Simulator

- bundle_id: `labview-fpga-module`
- source_path: `configuring-labview-for-a-third-party-simulator-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-labview-for-a-third-party-simulator-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you can export an FPGA VI for simulation, you must configure LabVIEW to work with an installed simulator. Complete the following steps to configure LabVIEW to work with an installed simulator. In LabVIEW, select Tools»Options to display the Options dialog box. Select FPGA Module from the Cate

### Configuring LabVIEW for a Third-Party Simulator

Before you can export an FPGA VI for simulation, you must configure LabVIEW to work


 with an installed simulator.

Complete the following steps to configure LabVIEW to work with an installed


 simulator.

1. In LabVIEW, select Tools»Options to display the


 Options dialog box.
2. Select FPGA Module from the


 Category list to display the FPGA Module


 Options dialog box.
3. Select a simulator from the Simulator pull-down


 menu.
4. Click OK to save the changes.

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-pattern-detection-for-a-dsp48e-or-dsp48e1-function-fpga-module.html language=enus -->
## TOPIC 00040: Configuring Pattern Detection for a DSP48E or DSP48E1 Function

- bundle_id: `labview-fpga-module`
- source_path: `configuring-pattern-detection-for-a-dsp48e-or-dsp48e1-function-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-pattern-detection-for-a-dsp48e-or-dsp48e1-function-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pattern Detect page to enable, disable, and configure pattern detection. Refer to the following sections of the Virtex-5 FPGA XtremeDSP Design Considerations User Guide or the Virtex-6 FPGA DSP48E1 Slice User Guide, available on the Xilinx Web site at www.xilinx.com, for information about pa

### Configuring Pattern Detection for a DSP48E or DSP48E1 Function

Use the Pattern Detect page to enable, disable, and configure pattern
 detection. Refer to the following sections of the *Virtex-5 FPGA XtremeDSP
 Design Considerations User Guide* or the *Virtex-6 FPGA DSP48E1 Slice
 User Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about pattern detection:

- "Pattern Detect Logic"
- "PATTERNDETECT and PATTERNBDETECT Port Logic"
- "Pattern Detect Applications" ( Virtex-5 FPGA XtremeDSP Design


 Considerations User Guide only) . This section also provides


 information about the VHDL generics and options in the table in the following


 section.

#### VHDL Equivalent of LabVIEW Options

To view the VHDL equivalent of a configuration, click the VHDL
 Instantiation tab. Refer to Table 1-3 in either the *Virtex-5
 FPGA XtremeDSP Design Considerations User Guide* or the *Virtex-6
 FPGA DSP48E1 Slice User Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about specific attributes. The
 following table shows the attributes that correspond to each option in LabVIEW.

| LabVIEW Option | Attribute to Reference in Table 1-3 |  |
| --- | --- | --- |
| DSP48E | DSP48E1 |  |
|  | USE_PATTERN_DETECT |  |
|  | SEL_PATTERN, PATTERN |  |
|  | SEL_ROUNDING_MASK, SEL_MASK, MASK | SEL_MASK, MASK |
|  | AUTORESET_PATTERN_DETECT, AUTORESET_PATTERN_DETECT_OPTINV | AUTORESET_PATDET |

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Configuring DSP48E and DSP48E1 Functions
- Configuring the Functionality of a DSP48E or DSP48E1 Slice
- Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-the-fpga-io-node-name-control-fpga-module.html language=enus -->
## TOPIC 00041: Configuring the FPGA I/O Node Name Control

- bundle_id: `labview-fpga-module`
- source_path: `configuring-the-fpga-io-node-name-control-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-the-fpga-io-node-name-control-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use FPGA I/O name controls to create reentrant subVIs with configurable I/O items. When you use an FPGA I/O control as an input on a subVI, the input accepts only I/O items that support a superset of the methods and properties you enable for the FPGA I/O control. All enabled methods must mat

### Configuring the FPGA I/O Node Name Control

You can use FPGA I/O name controls to create reentrant subVIs with configurable I/O


 items. When you use an FPGA I/O control as an input on a subVI, the input accepts


 only I/O items that support a superset of the methods and properties you enable for


 the FPGA I/O control. All enabled methods must match in name, and their parameters


 must match in name, order, and data type. All enabled properties must match in name


 and data type.

Complete the following steps to configure the FPGA I/O name control using the


 Configure FPGA I/O Name Control Type dialog box.

1. Right-click an FPGA I/O control or constant and select Configure I/O


 Type from the shortcut menu to display the Configure


 FPGA I/O Name Control Type dialog box.
2. Select an FPGA I/O item from the I/O Items list that


 supports all the methods and properties you plan to use with the FPGA I/O


 control. The methods and properties of the I/O item you select appear in the


 I/O Item Type list.
3. Click Replace All to copy all the methods and properties


 from the I/O Item Type list to the I/O Name


 Control Type list. You cannot move individual I/O item types to


 the I/O Name Control Type box.
4. Click Remove to remove methods and properties from the


 I/O Name Control Type list that you do not want to


 require of I/O items passed to the control. To make the control broadly


 reusable, remove any resource-specific methods and properties that you do not


 want to use with the FPGA I/O control. You can click an item in the


 I/O Name Control Type list and read about the item in


 the I/O Name Control Type Details section.
5. Click OK to close the dialog box.

Parent topic:

Using SubVIs in FPGA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-the-functionality-of-a-dsp48e-or-dsp48e1-slice-fpga-module.html language=enus -->
## TOPIC 00042: Configuring the Functionality of a DSP48E or DSP48E1 Slice

- bundle_id: `labview-fpga-module`
- source_path: `configuring-the-functionality-of-a-dsp48e-or-dsp48e1-slice-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-the-functionality-of-a-dsp48e-or-dsp48e1-slice-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you add a DSP48E or DSP48E1 function to a block diagram, double-click the function to launch its configuration dialog box. The first page is the Function page, which you use to configure the overall behavior of the function. Notice the schematic at the bottom of the configuration dialog box. T

### Configuring the Functionality of a DSP48E or DSP48E1 Slice

After you add a DSP48E or DSP48E1 function to a block diagram, double-click the


 function to launch its configuration dialog box. The first page is the


 Function page, which you use to configure the overall


 behavior of the function.

Note

The values of the opmode, alumode, and


 carryinsel inputs determine the functionality of DSP48E


 and DSP48E1 slices. The value of the inmode input affects the


 DSP48E1 slice. You can let LabVIEW configure these terminals by selecting either


 Configure for Arithmetic or Configure for


 Logic from the pull-down menu on the Function


 page. If you choose one of these options, LabVIEW sets these values appropriately


 after you configure the arithmetic or logical expression as the following sections


 describe.

Note

VHDL Instantiation

#### Configuring a DSP48E or DSP48E1 Function for Arithmetic Expressions

If you select Configure for Arithmetic, the function computes


 the following arithmetic expression:

p = (+/NOT z) +/–


 (x+y + carryin)

where:

- NOT z is equivalent to – z –


 1.
- z , x+y , and


 carryin are variables for which you select constant


 values, such as 0, or data sources, such as the value of a function terminal or


 computation. The values and/or sources you specify for these arguments determine


 the functionality of the slice. You can remove z or


 x+y from the equation by specifying the value as


 0 . Note 
The sources available for carryin depend on


 the values you specify for z and


 x+y. Therefore, NI recommends specifying


 z and x+y before


 specifying carryin.(DSP48E) Refer to Table 1-10 in the *Virtex-5 FPGA XtremeDSP Design Considerations User
 Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about the
 different sources of carryin. The manual
 lists this terminal as CARRYINSEL. (DSP48E1) Refer
 to Table 1-11 in the *Virtex-6 FPGA DSP48E1 Slice User
 Guide* for this information.
- p is the numerical result of this equation.

#### Configuring the Pre-Adder of a DSP48E1 Slice

To use the pre-adder of a DSP48E1 slice, set the value of x+y


 to m, where m =


 (d + a) *


 b. d, a and


 b can be either 0 or different stages in the


 d, a, and b


 input terminals' data paths. The following dialog box shows a sample configuration


 that uses the pre-adder:

[IMAGE alt='image' src='GUID-1B2FA402-CF7E-4C94-A546-545EBA3DE1AA-a5.png']

Refer to the following sections of the *Virtex-6 FPGA DSP48E1 Slice User


 Guide* for more information about the pre-adder:

- "Pre-adder"
- "Pre-Adder Block Applications"

#### Common DSP48E Arithmetic Configurations

The following dialog boxes show common arithmetic configurations of DSP48E


 functions:

#### Multiply

[IMAGE alt='image' src='GUID-6C6CB09D-D471-46E0-9587-E58374FF9B37-a5.png']

Note

Logic unit mode

One


 48-Bit

#### Multiply-accumulate

[IMAGE alt='image' src='GUID-7684D86D-F99C-4213-8EA8-58DC08A3CA02-a5.png']

#### Multiply-add

[IMAGE alt='image' src='GUID-9C648088-C433-4B1E-BD49-B0BDB7597798-a5.png']

#### Multiply-subtract

[IMAGE alt='image' src='GUID-628D1CF6-3E20-4974-966E-6AF2E9E4DC00-a5.png']

#### One-Step Counter

1. Function page: [IMAGE alt='image' src='GUID-BE385E2A-CB64-4482-AFD5-EF9381A8DAEF-a5.png']
2. Terminals page: [IMAGE alt='image' src='GUID-675007F5-F401-4989-B705-8C5B4897FE3E-a5.png']
3. On the block diagram, wire a TRUE constant to the carryin 


 terminal and 0 to the a and


 b input terminals: [IMAGE alt='image' src='GUID-5603672F-9E20-4FE0-A91D-4CF60131CF2A-a5.png']

#### n-Step Counter/Accumulator

1. Function page: [IMAGE alt='image' src='GUID-B0957485-55AD-4DFA-B3C4-000A6D81065E-a5.png']
2. On the block diagram, wire a control to the c input:


 [IMAGE alt='image' src='GUID-504E660E-AAEB-4502-AA32-D62EAD7E88C0-a5.png'] 
 c represents the number of steps for the counter. The


 function accumulates the value of c . Note 


 In this configuration, the carryin terminal is not


 displayed, which means LabVIEW sets it to a constant value of FALSE.

#### Common DSP48E1 Arithmetic Configurations

The following dialog boxes show common arithmetic configurations of DSP48E1


 functions:

#### Multiply

[IMAGE alt='image' src='GUID-C077DA4E-43CE-4CBD-A6BC-733D13148464-a5.png']

#### Multiply with Pre-Adder

[IMAGE alt='image' src='GUID-634D5A9E-8B51-42C7-B484-6952B7F12E1A-a5.png']

#### Multiply-accumulate

[IMAGE alt='image' src='GUID-666B7E4E-DE9F-47F2-8AB9-93D20FD98430-a5.png']

#### Multiply-add

[IMAGE alt='image' src='GUID-FFCDC533-194B-43E3-9E0D-0A42A3771B50-a5.png']

#### Multiply-subtract

[IMAGE alt='image' src='GUID-45D6B67D-9FB2-4C2F-A6B0-7CD563EE7700-a5.png']

#### Configuring a DSP48E or DSP48E1 Function for Logical Expressions

If you select Configure for Logic, the function compares


 Logic x to Logic z and returns the


 result as p. You must specify the sources of Logic


 x and Logic z along with the comparison


 operator, as the following illustration shows:

[IMAGE alt='image' src='GUID-1876EC74-314D-42A9-92F8-78687EEE3ACD-a5.png']

#### Configuring the Behavior of a DSP48E or DSP48E1 Function While a VI is


 Running

To change the behavior of a DSP48E or DSP48E1 slice while a VI is running, you first


 must select Custom Configuration in the configuration dialog


 box. After you select this option, LabVIEW shows the opmode,


 alumode, and carryinsel terminals


 on the block diagram. LabVIEW also shows the inmode terminal


 for DSP48E1 functions. You then must wire values to these terminals to obtain the


 configuration you want. Because this configuration is programmatic, you can change


 the behavior of a single DSP48E or DSP48E1 slice while the FPGA VI is running.

Note

Virtex-5 FPGA XtremeDSP Design Considerations User
 Guide

www.xilinx.com

- "ALUMODE Inputs"
- "Carry Input Logic"
- "Two-Input Logic Unit"
- "X, Y, and Z Multiplexer"

Virtex-6
 FPGA DSP48E1 Slice User Guide

#### VHDL Equivalent of LabVIEW Options

To view the VHDL equivalent of a configuration, click the VHDL
 Instantiation tab. Refer to Table 1-3 in either the *Virtex-5
 FPGA XtremeDSP Design Considerations User Guide* or the *Virtex-6
 FPGA DSP48E1 Slice User Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about specific attributes. The
 following table shows the attributes that correspond to each option in LabVIEW.

Note

- "Single Instruction, Multiple Data (SIMD)


 Mode"
- "Single Instruction Multiple Data (SIMD) Arithmetic"

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Configuring DSP48E and DSP48E1 Functions
- Configuring Pattern Detection for a DSP48E or DSP48E1 Function

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-the-matrix-size-and-interface-of-the-linear-algebra-matrix-multiply-function-fpga-module.html language=enus -->
## TOPIC 00043: Configuring the Matrix Size and Interface of the Linear Algebra Matrix Multiply Function

- bundle_id: `labview-fpga-module`
- source_path: `configuring-the-matrix-size-and-interface-of-the-linear-algebra-matrix-multiply-function-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-the-matrix-size-and-interface-of-the-linear-algebra-matrix-multiply-function-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For the Matrix Multiply function to operate on incoming data, you must configure the function using the Configure Linear Algebra Matrix Multiply dialog box. Complete the following steps to configure the matrix size and interface of a Linear Algebra Matrix Multiply function: Enter the values of M, L,

### Configuring the Matrix Size and Interface of the Linear Algebra Matrix Multiply Function

For the Matrix Multiply function to operate on incoming data, you must configure the


 function using the Configure Linear Algebra Matrix Multiply


 dialog box. Complete the following steps to configure the matrix size and interface


 of a Linear Algebra Matrix Multiply function:

1. Enter the values of M , L , and


 N in the Matrix Size section


 to set sizes of matrix A and matrix


 B .
2. Select the Input pattern of A and the Input


 pattern of B in the Interface 


 configuration section to specify that the function receives data element by


 element in the matrix, by vector, by row-wise, or by column-wise. Matrix


 A and matrix B must both use the same


 input pattern. For example, if the Input pattern of A is


 Row-Wise Element or Column-Wise


 Element , you can select only Row-Wise


 Element or Column-Wise Element as the


 Input pattern of B and LabVIEW dims the vector input


 pattern. Similarly, if the Input pattern of A is


 Row Vector or Column Vector ,


 you can select only Row Vector or Column


 Vector as the Input pattern of B and


 LabVIEW dims the element input pattern.
3. Use the Throughput option to specify the throughput rate


 you want the function to achieve. The throughput rate, in cycles/matrix, is the


 minimum number of FPGA clock cycles that must elapse before this function can


 receive the next pair of valid input matrices. This function requires several


 clock cycles to calculate the result of matrix A *matrix


 B . You may need to wait several cycles before you can


 input another pair of matrices to the next function. The


 Throughput options change based on matrix size as


 configured by M , L , and


 N . For example, if the size of matrix


 A is 3*4


 ( M * L ) with a Row


 Vector input pattern, and the size of matrix


 B is 4*5


 ( L * N ) with a Column


 Vector input pattern, the Throughput 


 possibilities are 3, 4, 5, 12, 15, or 20 cycles/matrix. However, because the


 input cycle of matrix A is 3 ( M ) and


 the input cycle of matrix B is 5 ( N ).


 The available Throughput should be greater than or equal


 to 5 cycles/matrix. Therefore, throughputs of 3 cycles/matrix or 4 cycles/matrix


 are invalid. LabVIEW displays the resulting available


 Throughput options: 5, 12, 15, and 20 cycles/matrix.


 Selecting a smaller number of cycles/matrix generally results in higher


 throughput rates but also consumes more FPGA resources. The following dialog box


 shows the correct configuration for this example: [IMAGE alt='image' src='GUID-01095D7D-684C-4C4E-98F7-FB2EDD3C8AC6-a5.png'] In the following example, if matrix


 A is configured with Row-Wise


 Element and matrix B is configured with


 Column-Wise Element , LabVIEW displays the resulting


 available Throughput options: 3, 4, 5, 12, 15, or 20


 cycles/matrix. The input cycle of matrix A is 12


 ( M * L ) and the input cycle of


 matrix B is 20


 ( L * N ). The available


 Throughput should be greater than or equal to the


 maximum input cycle of matrix A and matrix


 B , in this case 20 cycles/matrix. The resulting available


 Throughput option is 20 cycles/matrix. The following


 dialog box shows the correct configuration for this example: [IMAGE alt='image' src='GUID-510AEE7D-F102-4A91-BA1D-5A424E9227BD-a5.png']
4. Select the Output pattern for the function. The possible throughputs of
 the Linear Algebra Matrix Multiply function are M ,
 L , N ,
 M * L ,
 N * L , and
 M * N . Each throughput
 corresponds to a specific output pattern. Refer to the following table for the
 relationship between the throughput and Output pattern .
 Throughput in cycles/matrix
Output PatternM
Row Vector
L
Column Vector
N
Column Vector
M*L
Row Vector
L*N
Column Vector
M*N
Row-Wise Element In the following example, the size of matrix A is
 3*4 ( M * L ), the size of matrix
 B is 4*5
 ( L * N ), and the resulting
 Throughput is 20 cycles/matrix
 ( L * N ). The resulting
 Output pattern of
 A * B is Column
 Vector . The following dialog box shows the correct configuration
 for this example: [IMAGE alt='image' src='GUID-53173D47-4DF9-434C-A8AA-B10B51428677-a5.png']

Parent topic:

Using the Linear Algebra Functions

<!--NI_TOPIC bundle=labview-fpga-module path=configuring-the-mechanical-actions-of-boolean-controls-fpga-module.html language=enus -->
## TOPIC 00044: Configuring the Mechanical Actions of Boolean Controls

- bundle_id: `labview-fpga-module`
- source_path: `configuring-the-mechanical-actions-of-boolean-controls-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/configuring-the-mechanical-actions-of-boolean-controls-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the configurable mechanical action of a Boolean control to create front panels that resemble the behavior of physical instruments such as oscilloscopes and multimeters. Right-click a Boolean control and select the behavior from the options in the Mechanical Action menu. The mechanical ac

### Configuring the Mechanical Actions of Boolean Controls

You can use the configurable mechanical action of a Boolean control to create front


 panels that resemble the behavior of physical instruments such as oscilloscopes and


 multimeters. Right-click a Boolean control and select the behavior from the options


 in the Mechanical Action menu.

The mechanical actions of Boolean controls of an FPGA VI differ when the FPGA VI runs


 on hardware versus in simulation mode. In simulation mode, the mechanical actions of


 Boolean controls of the FPGA VI behave the same as in


 LabVIEW. On FPGA targets, use Switch When Pressed,


 Switch When Released, or Switch Until


 Released as a control that changes the current value once a new


 value is written from the host VI to the FPGA target, and retains the new value


 until another value is written from the host VI again. Use Latch When


 Pressed, Latch When Released, or


 Latch Until Released as a control that only changes the


 current value when a new value is written from the host VI to the FPGA target, and


 reverts to the previous value once the new value has been read by the FPGA


 target.

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=connect-linux-to-ethernet-crio.html language=enus -->
## TOPIC 00045: Connect from a Linux Host to an Ethernet CompactRIO

- bundle_id: `labview-fpga-module`
- source_path: `connect-linux-to-ethernet-crio.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/connect-linux-to-ethernet-crio.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to open a remote FPGA reference from a Linux desktop host to a CompactRIO controller. Ensure you have the following: NI‑RIO packages installed on the Linux host. IP address of the CompactRIO controller. Firewall rules that allow NI‑RIO discovery and data traffic. Basic network tools availa

### Connect from a Linux Host to an Ethernet
 CompactRIO

Learn how to open a remote FPGA reference from a Linux desktop host to a CompactRIO
 controller.

- NI‑RIO packages installed on the Linux host.
- IP address of the CompactRIO controller.
- Firewall rules that allow NI‑RIO discovery and data traffic.
- Basic network tools available (ping or equivalent).

Tip

- Use static IP addressing on the cRIO.
- Reserve a DHCP lease.

Tip

1. Install the required NI‑RIO packages on the Linux host.
2. Verify network connectivity to the controller by pinging the cRIO IP
 address.
3. Add Open FPGA VI Reference on the block diagram.
4. Perform one of the following actions: 
 Add RIO Device control on the front panel.
 Convert the terminal to a constant on the block diagram.
5. Enter the resource string:
 rio://<cRIO-IP>/<fpga-resource>. 
 Note cRIO-IP is the IP address of the CompactRIO
 controller.
 fpga-resource is the FPGA resource name on that
 system, such as RIO0.For example: rio://192.168.1.100/RIO0
6. Run the VI and confirm the reference opens successfully.
7. Verify end‑to‑end communication by performing read/write operations.

The expected result is that the Linux host opens a remote FPGA reference to the
 CompactRIO controller, which enables data exchange over Ethernet.

- Reference fails to open:
  - Check Linux firewall rules.
  - Ensure the cRIO is powered and reachable.
  - Verify driver versions.
- High latency or dropped transfers:
  - Reduce data rate.
  - Increase buffering.
  - Confirm network quality (switch ports, cables, VLANs).

Parent topic:

Accessing Remote FPGA Targets Across Networks

Related concepts:

- Accessing Remote FPGA Targets Across Networks

Related information:

- NI-RIO For Linux/x86 64-bit Architecture

<!--NI_TOPIC bundle=labview-fpga-module path=controlling-io-power-on-states-fpga-module.html language=enus -->
## TOPIC 00046: Controlling I/O Power-On States

- bundle_id: `labview-fpga-module`
- source_path: `controlling-io-power-on-states-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/controlling-io-power-on-states-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: An application might require that the I/O on the FPGA target be set to a known value when the system powers on. For example, if an FPGA target controls hydraulic valves with the digital outputs, the FPGA target must keep the valves turned off until the host VI is launched and starts to control the s

### Controlling I/O Power-On States

An application might require that the I/O on the FPGA target be set to a known value


 when the system powers on. For example, if an FPGA target controls hydraulic valves


 with the digital outputs, the FPGA target must keep the valves turned off until the


 host VI is launched and starts to control the system. You can create an FPGA VI and


 configure the FPGA target to set the power-on states of the FPGA target.

Note

You must program the FPGA VI so that the block diagram sets the output states without


 any dependencies on the host VI. For example, you can place the digital and analog


 output functions in the first frame of a sequence structure. You then place the rest


 of the LabVIEW code in the subsequent frames of the sequence structure, as shown in


 the following block diagram. Then configure the FPGA VI to start executing as soon


 as it is loaded in the FPGA. Compile and download the FPGA VI to the flash memory on


 the FPGA target and configure the FPGA target to automatically load the FPGA VI from the


 flash memory when the FPGA target powers on. When the FPGA target powers on, the


 FPGA VI loads into the FPGA from the flash memory, and the FPGA VI starts executing


 immediately. The output functions in the first frame of the sequence structure on


 the FPGA VI set the power-on output states.

[IMAGE alt='image' src='GUID-C6068862-1BF7-47F8-B438-AC2EE87D5CF7-a5.png']

You can create more than a static power-on state for the outputs of the FPGA target.


 You can create arbitrary power-on functionality that performs complex actions. For


 example, you can set outputs based on the state of the inputs, use serial


 communication with an external device, and so on. Refer to the specific FPGA target


 hardware documentation for information about default


 power-on states.

Note

Never Arbitrate

Parent topic:

Using FPGA I/O

Related concepts:

- Understanding Arbitration Options

<!--NI_TOPIC bundle=labview-fpga-module path=controlling-the-fpga-vi-execution-rate-fpga-module.html language=enus -->
## TOPIC 00047: Controlling the FPGA VI Execution Rate

- bundle_id: `labview-fpga-module`
- source_path: `controlling-the-fpga-vi-execution-rate-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/controlling-the-fpga-vi-execution-rate-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For some FPGA targets, you can configure the FPGA base clock and set it as the top-level clock in the project to control execution rates. You also can use a derived clock to circumvent base clock configuration restrictions. Different FPGA targets support different FPGA-derived clocks. For informatio

### Controlling the FPGA VI Execution Rate

For some FPGA targets, you can configure the FPGA base clock and set it as the top-level clock in the project to control execution rates.


 You also can use a derived clock to circumvent base clock configuration


 restrictions. Different FPGA targets support different FPGA-derived clocks. For


 information on allowed base clock configurations for different FPGA targets, refer


 to the specific FPGA target hardware


 documentation.

Complete the following steps to create an FPGA-derived clock to control the


 execution rate of items on the block diagram.

Note

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Create an FPGA-derived clock to run at the execution rate you


 want.
4. Set the FPGA-derived clock as the top level clock.

Note

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Configuring FPGA Base Clocks
- Selecting a Top-Level Clock for an FPGA Target
- Adding FPGA Targets to a LabVIEW Project
- Creating FPGA-Derived Clocks

<!--NI_TOPIC bundle=labview-fpga-module path=creating-a-custom-vi-to-simulate-io-fpga-module.html language=enus -->
## TOPIC 00048: Creating a Custom VI to Simulate I/O

- bundle_id: `labview-fpga-module`
- source_path: `creating-a-custom-vi-to-simulate-io-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-a-custom-vi-to-simulate-io-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A test bench is a custom VI that provides some stimulus to the unit under test and reads back the results to verify the design. In this case, the unit under test is the FPGA VI. The test bench passes or fails depending on the response. A simple test bench includes two parts: Stimulus—Data going into

### Creating a Custom VI to Simulate I/O

A test bench is a custom VI that provides some stimulus to the unit under test and


 reads back the results to verify the design. In this case, the unit under test is


 the FPGA VI. The test bench passes or fails depending on the response. A simple test


 bench includes two parts:

- Stimulus —Data going into the component being tested
- Response —Data passed back from the component being


 tested

You can create a custom VI to simulate I/O in LabVIEW for use as a test bench for


 your FPGA VI. You can use a custom VI as a test bench to create the data coming from


 a particular input or monitor an output. For example, if the expected input for a


 particular component is a noisy sine wave, you can use a custom VI to create the


 noisy sine wave. Every time an FPGA VI reads an input by calling an FPGA I/O Node,


 LabVIEW uses the custom VI you specify to provide the data. Using custom VIs for


 FPGA I/O creates a repeatable scenario for testing and makes it possible to change


 the data for a particular input. For example, if you need a square wave instead of a


 sine wave, you can modify the custom VI. You also can use custom VIs for FPGA I/O to


 monitor an output from FPGA I/O Nodes. For example, if the expected output of a


 component is a sine wave and the frequency of the sine wave is the important aspect


 of the output, you can create a custom VI to monitor the output of an FPGA I/O Node


 to verify that the frequency is correct.

Before debugging an FPGA VI using a test bench, you can test the logic of the VI


 without compiling it by executing the FPGA VI in simulation mode using simulated


 I/O. Executing an FPGA VI in simulation mode using simulated I/O saves compilation


 time, makes tests easier to repeat, and decreases the number of modifications


 necessary to create a test bench for additional debugging.

#### Creating a Custom VI Test Bench

Complete the following steps to create a custom VI test bench from a template.

1. In the Project Explorer window, right-click the FPGA


 target to display the FPGA Target Properties dialog box.
2. On the Execution Mode page, select


 Simulation .
3. From the pull-down menu, select Use Custom VI for FPGA


 I/O . LabVIEW displays the VI Path box


 below the menu.
4. Click the New VI from Template button.
5. Name the test bench and save it in the user.lib directory. The


 file path appears in the VI Path box.
6. Click the OK button to add the custom VI to the


 project.

Refer to the Tutorial: Creating Test Benches topic for an example of how to create


 and use a custom VI test bench.

Parent topic:

Debugging FPGA VIs Using Simulation Mode

Related concepts:

- Interactive Front Panel Communication
- Using a Host VI to Communicate with the FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=creating-a-peer-to-peer-streaming-session-fpga-module.html language=enus -->
## TOPIC 00049: Creating a Peer-to-Peer Streaming Session

- bundle_id: `labview-fpga-module`
- source_path: `creating-a-peer-to-peer-streaming-session-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-a-peer-to-peer-streaming-session-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a peer-to-peer streaming session. Place the niP2P Create Peer to Peer Stream VI on the block diagram. Wire the reference from the reader to the reader input terminal of the niP2P Create Peer to Peer Stream VI. Wire the reference from the writer to the writer in

### Creating a Peer-to-Peer Streaming Session

Complete the following steps to create a peer-to-peer streaming session.

1. Place the niP2P Create Peer to Peer Stream VI on the block


 diagram.
2. Wire the reference from the reader to the reader input


 terminal of the niP2P Create Peer to Peer Stream VI.
3. Wire the reference from the writer to the writer input


 terminal of the niP2P Create Peer to Peer Stream VI.
4. Wire the stream session output terminal of the niP2P


 Create Peer to Peer Stream VI to other Peer to Peer Streaming VIs in the host VI to control


 and monitor the streaming session.

Parent topic:

Using Peer-to-Peer Streaming with FPGA Targets

Related concepts:

- Using Peer-to-Peer Streaming with FPGA Targets
- Creating a Reference to a Peer-to-Peer Reader FIFO
- Creating a Reference to a Peer-to-Peer Writer FIFO

<!--NI_TOPIC bundle=labview-fpga-module path=creating-a-reference-to-a-peer-to-peer-reader-fifo-fpga-module.html language=enus -->
## TOPIC 00050: Creating a Reference to a Peer-to-Peer Reader FIFO

- bundle_id: `labview-fpga-module`
- source_path: `creating-a-reference-to-a-peer-to-peer-reader-fifo-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-a-reference-to-a-peer-to-peer-reader-fifo-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you can create a peer-to-peer streaming session, you must create a reference to the peer-to-peer reader FIFO. If the peer-to-peer reader FIFO is not on an FPGA target, refer to the specific FPGA target documentation for information about creating a reference. For FPGA targets, complete the fo

### Creating a Reference to a Peer-to-Peer Reader FIFO

Before you can create a peer-to-peer streaming session, you must create a reference to the


 peer-to-peer reader FIFO. If the peer-to-peer reader FIFO is not on an FPGA target,


 refer to the specific FPGA target documentation for information about creating a reference. For


 FPGA targets, complete the following steps to create a reference to a peer-to-peer


 reader FIFO.

1. Create a reader FIFO for an FPGA target.
2. On the block diagram of the host


 VI, place an Open


 FPGA VI Reference function.
3. Drag the FPGA VI for the reader from the Project Explorer 


 window to the Open FPGA VI Reference function.
4. Place an Invoke Method node on the block diagram.
5. Wire the FPGA VI Reference Out terminal of the Open FPGA


 VI Reference function to the FPGA VI Reference In 


 terminal of the Invoke Method node.
6. Click the Method terminal on the Invoke Method node and


 select FIFO»Get Peer to Peer Reader 


 from the shortcut menu, where FIFO is the name of the


 peer-to-peer FIFO under the FPGA target.
7. Use the output from the Reader terminal of the Invoke


 Method node to create a peer-to-peer streaming session from the host VI.

Parent topic:

Using Peer-to-Peer Streaming with FPGA Targets

Related concepts:

- Using Peer-to-Peer Streaming with FPGA Targets
- FPGA Target Hardware Documentation
- Creating Peer-to-Peer Reader FIFOs
- Creating a Peer-to-Peer Streaming Session

<!--NI_TOPIC bundle=labview-fpga-module path=creating-a-reference-to-a-peer-to-peer-writer-fifo-fpga-module.html language=enus -->
## TOPIC 00051: Creating a Reference to a Peer-to-Peer Writer FIFO

- bundle_id: `labview-fpga-module`
- source_path: `creating-a-reference-to-a-peer-to-peer-writer-fifo-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-a-reference-to-a-peer-to-peer-writer-fifo-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you can create a peer-to-peer streaming session, you must create a reference to the peer-to-peer writer FIFO. If the peer-to-peer writer FIFO is not on an FPGA target, refer to the specific FPGA target documentation for information about creating a reference. For FPGA targets, complete the fo

### Creating a Reference to a Peer-to-Peer Writer FIFO

Before you can create a peer-to-peer streaming session, you must create a reference to the


 peer-to-peer writer FIFO. If the peer-to-peer writer FIFO is not on an FPGA target,


 refer to the specific FPGA target documentation for information about creating a reference. For


 FPGA targets, complete the following steps to create a reference to a peer-to-peer


 writer FIFO.

1. Create a writer FIFO for an FPGA target.
2. On the block diagram of the host


 VI, place an Open


 FPGA VI Reference function.
3. Drag the FPGA VI for the writer from the Project Explorer 


 window to the Open FPGA VI Reference function.
4. Place an Invoke Method node on the block diagram.
5. Wire the FPGA VI Reference Out terminal of the Open FPGA


 VI Reference function to the FPGA VI Reference In 


 terminal of the Invoke Method node.
6. Click the Method terminal on the Invoke Method node and


 select FIFO»Get Peer to Peer Writer 


 from the shortcut menu, where FIFO is the name of the


 peer-to-peer FIFO under the FPGA target.
7. Use the output from the Writer terminal of the Invoke


 Method node to create a peer-to-peer streaming session.

Parent topic:

Using Peer-to-Peer Streaming with FPGA Targets

Related concepts:

- Using Peer-to-Peer Streaming with FPGA Targets
- FPGA Target Hardware Documentation
- Creating Peer-to-Peer Writer FIFOs
- Creating a Peer-to-Peer Streaming Session

<!--NI_TOPIC bundle=labview-fpga-module path=creating-fifos-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00052: Creating FIFOs in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `creating-fifos-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-fifos-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW provides different types of FIFOs that enable you to transfer data between different portions of an FPGA VI, between VIs in an FPGA target, or between devices. You can create FIFOs from the Project Explorer window or, in the case of target-scoped and VI-defined FIFOs, directly from the block

### Creating FIFOs in FPGA VIs

LabVIEW provides different types of FIFOs that enable you to transfer data between


 different portions of an FPGA VI, between VIs in an FPGA target, or between devices.


 You can create FIFOs from the Project Explorer window or, in


 the case of target-scoped and VI-defined FIFOs, directly from the block diagram.

#### Creating a Target-Scoped FIFO from the Project Explorer Window

Complete the following steps to create a target-scoped FIFO from the


 Project Explorer window.

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»FIFO to display the FIFO


 Properties dialog box.
3. On the General page, expand the pull-down menu under


 Implementation to display the available options.
4. Click OK to finish creating the FIFO.
5. Drag the FIFO from the Project Explorer window to the


 block diagram. LabVIEW adds a FIFO Method node configured for the FIFO.

#### Creating a FIFO from the Block Diagram

You can create either a target-scoped or a VI-defined FIFO from the block


 diagram.

Target-Scoped:

1. Display the block diagram.
2. From the Functions palette, add a FIFO Method


 Node to the block diagram.
3. Right-click the FIFO Method node and select Add New FIFO 


 from the shortcut menu to display the FIFO


 Properties dialog box. Tip You also can right-click the


 FIFO Method Node and select Select


 FIFO»x from


 the shortcut menu, where x is an


 existing FIFO.
4. On the General page, expand the


 Implementation pull-down menu to display the available options.
5. Click OK to finish creating the FIFO.

You also can wire a FIFO


 Constant, FIFO Method Node, or VI-Defined FIFO


 Configuration node to the FIFO In input to specify


 the FIFO. LabVIEW configures the FIFO Method Node with the default method. For FIFOs


 that support the Write method, the default method is Write. To select a different


 method after you specify the FIFO, right-click the FIFO Method Node and select


 Select Method»y


 from the shortcut menu, where y is the


 specific method.

VI-Defined:

1. Display the block diagram.
2. From the Functions palette, add a VI-Defined


 FIFO Configuration Node to the block diagram.
3. Right click the VI-Defined FIFO Configuration node and select


 Configure from the shortcut menu to display the FIFO Properties dialog box.
4. On the General page, expand the


 Implementation pull-down menu to display the available options.
5. Click OK to finish creating the FIFO.

#### Creating a DMA FIFO from the Project Explorer Window

First, complete the following steps to determine whether your target supports DMA


 FIFOs.

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select Properties from the shortcut menu to display the


 FPGA


 Target Properties dialog box.
3. Refer to the Target Information box on the General page to find DMA support information. If


 your target supports DMA, the Target Information box


 gives the number of DMA channels. If your target does not support DMA, the


 Target Information box indicates that DMA is not


 supported.

If your target supports DMA FIFOs, complete the following steps to create a DMA FIFO


 in an FPGA VI. Refer to Reading DMA


 FIFOs from Host VIs and Writing to


 DMA FIFOs from Host VIs for help configuring a host VI to read and write


 DMA FIFOs.

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»FIFO to display the FIFO


 Properties dialog box.
3. Use the Type pull-down menu to select either


 Host to Target—DMA or Target to


 Host—DMA , depending on which direction you want to stream the


 data.
4. Click OK to finish creating the FIFO.
5. Drag the FIFO from the Project Explorer window to the


 block diagram. LabVIEW adds a FIFO Method node configured for the FIFO.

#### Creating a Peer-to-Peer FIFO from the Project Explorer Window

Complete the following steps to create a peer-to-peer FIFO from the


 Project Explorer window or to determine whether a


 particular target supports peer-to-peer streaming.

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»FIFO to display the FIFO


 Properties dialog box.
3. On the General page, select Peer to Peer


 Writer or Peer to Peer Reader from the


 Type pull-down menu. If these options are not


 available in the pull-down menu, the target does not support peer-to-peer


 FIFOs.
4. Click OK to finish creating the FIFO.

Refer to the topics on using peer-to-peer


 streaming with FPGA targets for information about how to use peer-to-peer


 FIFOs.

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

<!--NI_TOPIC bundle=labview-fpga-module path=creating-fpga-derived-clocks-fpga-module.html language=enus -->
## TOPIC 00053: Creating FPGA-Derived Clocks

- bundle_id: `labview-fpga-module`
- source_path: `creating-fpga-derived-clocks-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-fpga-derived-clocks-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can derive additional clocks from FPGA base clocks in a LabVIEW project. Complete the following steps to derive an FPGA clock. Support of FPGA-derived clocks varies by FPGA target. Refer to the specific FPGA target hardware documentation for more information. Create a new project or open an ex

### Creating FPGA-Derived Clocks

You can derive additional clocks from FPGA base clocks in a LabVIEW project. Complete the following steps to derive


 an FPGA clock.

Note

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. If the FPGA target you use does not automatically add the FPGA base clock you


 want to the Project


 Explorer window, add the FPGA base clock.
4. Right-click an FPGA base clock in the Project Explorer 


 window and select New FPGA Derived Clock from the


 shortcut menu. The FPGA Derived Clock Properties dialog box


 appears. Note If the FPGA target does not support


 FPGA-derived clocks or the FPGA base clock you add, the New FPGA


 Derived Clock option is dimmed in the shortcut menu.
5. (Optional) Enter a name in the Name text box. By default,


 the name is the actual derived frequency.
6. Type the frequency at which you want the derived clock to run in the


 Desired Derived Frequency text box. LabVIEW finds the


 closest frequency that the underlying FPGA supports and displays it in the


 Derived Frequency text box in the Actual


 Derived Configuration section. If the FPGA supports the


 Derived Frequency , the Message 


 text box displays that the frequency is available. Otherwise, it displays the


 error between the derived frequency and the desired frequency.
7. Click the OK button to accept the derived frequency and


 close the dialog box. The FPGA-derived clock appears in the Project


 Explorer window with the derivation ratio in parentheses.

You now can set the new derived clock as the top-level clock in the project.

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Adding FPGA Targets to a LabVIEW Project
- Controlling the FPGA VI Execution Rate
- Using FPGA Clocks and Timing
- Adding an FPGA Base Clock to a LabVIEW Project
- Selecting a Top-Level Clock for an FPGA Target
- Selecting an FPGA Clock as the Timing Source for SCTLs

<!--NI_TOPIC bundle=labview-fpga-module path=creating-fpga-io-items-fpga-module.html language=enus -->
## TOPIC 00054: Creating FPGA I/O Items

- bundle_id: `labview-fpga-module`
- source_path: `creating-fpga-io-items-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-fpga-io-items-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to access an I/O resource on an FPGA target, you first must create an FPGA I/O item in the Project Explorer window. You then can use the FPGA I/O item in an FPGA I/O Node on the block diagram of an FPGA VI. You must create the FPGA I/O item under the FPGA target in the Project Explorer w

### Creating FPGA I/O Items

If you want to access an I/O resource on an FPGA target, you first must create an


 FPGA I/O item in the Project


 Explorer window. You then can use the FPGA I/O item in an FPGA I/O Node on the block diagram of an


 FPGA VI. You must create the FPGA I/O item under the FPGA target in the


 Project Explorer window.

Tip

If you add a C Series module to the Project Explorer window,


 LabVIEW automatically adds all FPGA I/O items to the project. If you add a component-level IP (CLIP) item to the Project


 Explorer window, LabVIEW automatically adds all I/O items associated


 with the CLIP to the project.

Complete the following steps to create a new FPGA I/O item.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target and select New»FPGA I/O from


 the shortcut menu. The New FPGA


 I/O dialog box appears.
4. Select the I/O resource you want to use in the Available


 Resources tree. Tip You can select multiple


 resources by pressing the <Ctrl> key and clicking additional


 resources. You also can select an entire group of I/O resources by clicking


 the top-level I/O type or folder, if available.
5. Click the Add button. The I/O resource appears in the


 Resource column of the New FPGA


 I/O table. The default name of the I/O resource appears in the


 Name column. You can enter a new name for the I/O


 resource by typing in the Name column.
6. Repeat steps 4 and 5 until all the I/O resources you want to use are listed in


 the New FPGA I/O table.
7. Click the OK button. The FPGA I/O items you created


 appear in the Project Explorer window under the FPGA


 target. If you do not remove the checkmark from the Place new I/O in


 folders checkbox in the New FPGA I/O 


 dialog box, the FPGA I/O items appear in folders organized according to the


 hierarchy in the Available Resources list.

You also can create FPGA I/O items from the FPGA I/O Node on


 the block diagram. Right-click the FPGA I/O Node and select Add New FPGA


 I/O from the shortcut menu to display the New FPGA


 I/O dialog box. Complete steps 4 through 7 above to add new FPGA I/O


 items to the FPGA target in the Project Explorer window.

Note

Project


 Explorer

Parent topic:

Using FPGA I/O

Related concepts:

- Adding FPGA Targets to a LabVIEW Project
- Adding I/O to Monitor FPGA VIs
- Changing Arbitration Options
- Using the FPGA I/O Node
- Performing Actions on FPGA I/O and FPGA Targets
- Setting and Retrieving Properties on FPGA I/O and FPGA Targets

<!--NI_TOPIC bundle=labview-fpga-module path=creating-fpga-memory-items-fpga-module.html language=enus -->
## TOPIC 00055: Creating FPGA Memory Items

- bundle_id: `labview-fpga-module`
- source_path: `creating-fpga-memory-items-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-fpga-memory-items-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The primary means of data storage in a single clock domain using an FPGA application is a memory item. Memory items can be created from the Project Explorer window or the block diagram. Creating a Memory Item from the Project Explorer Window Complete the following steps to create a target-scoped mem

### Creating FPGA Memory Items

The primary means of data storage in a single clock domain using an FPGA application


 is a memory item. Memory items can be created from the Project


 Explorer window or the block diagram.

#### Creating a Memory Item from the Project Explorer Window

Complete the following steps to create a target-scoped memory item from the


 Project Explorer window:

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»Memory to display the Memory


 Properties dialog box.
3. On the General page, expand the


 Implementation pull-down menu to display the


 available memory options.
4. Click OK to finish creating the memory item.
5. Drag the memory item from the Project Explorer window to


 the block diagram. LabVIEW adds a Memory Method Node configured for the memory


 item.

#### Creating a Memory Item from the Block Diagram

You can create either a target-scoped or a VI-defined memory item from the block


 diagram.

#### Target-Scoped

1. Display the block diagram of the FPGA VI.
2. From the Functions palette, add a Memory


 Method Node to the block diagram.
3. Right-click the Memory Method Node and select Add New


 Memory to display the Memory Properties 


 dialog box. Tip You also can right-click the Memory Method Node


 and select Select


 Memory»x, where


 x is an existing memory


 item.
4. On the General page, expand the


 Implementation pull-down menu to display the


 available memory options.
5. Click OK to finish creating the memory item.

You also can wire a reference to the Memory In input to


 specify an existing memory item. After you specify the memory, right-click the


 Memory Method Node and select Select


 Method»y, where


 y is the specific method.

#### VI-Defined

1. Display the block diagram of the FPGA VI.
2. From the Functions palette, add a VI-Defined


 Memory Configuration Node to the block diagram.
3. Right click the VI-Defined Memory Configuration Node and select


 Configure to display the Memory


 Properties dialog box.
4. Expand the Implementation pull-down menu to display the


 available memory options.
5. Click OK to finish creating the memory item.

When you configure a node on the block diagram to use a VI-defined memory item,


 LabVIEW prepends VI:: to the name of that memory item. For example, if


 you name your VI-defined memory item Coefficients, LabVIEW displays the


 name of that memory item as VI::Coefficients.

Parent topic:

FPGA Memory Items

<!--NI_TOPIC bundle=labview-fpga-module path=creating-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00056: Creating FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `creating-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Review the topics in this section and in LabVIEW documentation when creating FPGA VIs.

### Creating FPGA VIs

Review the topics in this section and in LabVIEW documentation when creating FPGA
 VIs.

Related concepts:

- Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=creating-or-acquiring-ip-fpga-module.html language=enus -->
## TOPIC 00057: Creating or Acquiring IP

- bundle_id: `labview-fpga-module`
- source_path: `creating-or-acquiring-ip-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-or-acquiring-ip-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to create or acquire component-level IP (CLIP) for FPGA targets and ensure compliance with LabVIEW FPGA design rules. To add component-level IP (CLIP) to an FPGA target, you must provide IP, in the form of VHDL code, to compile into the FPGA target. You can provide the VHDL code in the fol

### Creating or Acquiring IP

Learn how to create or acquire component-level IP (CLIP) for FPGA targets and ensure
 compliance with LabVIEW FPGA design rules.

To add component-level IP (CLIP) to an FPGA target, you must provide IP, in the form
 of VHDL code, to compile into the FPGA target. You can provide the VHDL code in the
 following ways:

- Create VHDL code manually.
- Generate IP cores through the Xilinx IP generator.
- Purchase IP from Xilinx or partners.

#### Supported IP File
 Types

- VHDL
- Verilog
- Xilinx IP generator

If you use Verilog, compile it into a netlist file and wrap the netlist
 in a VHDL file.

If you use the Xilinx IP generator, you can import a
 constraints file directly to a CLIP signal.

Notice

#### Additional Requirements for CLIP Files

- The top-level file for a CLIP must be a plain-text VHDL file.
- This file can instantiate netlists (for example, EDIF) and encrypted
 VHDL.
- If you use encrypted VHDL, perform encryption with a version of Vivado that
 is compatible with the LabVIEW FPGA version.

#### Custom User Libraries

- Create a netlist from the VHDL and integrate the netlist using CLIP.
- Reference the default reference library instead of a custom user
 library.

#### IP Design Rules

- Define supported I/O ports.
- Handle clocking and reset behavior correctly.

#### I/O Data Types

All I/O that interfaces with LabVIEW must use supported LabVIEW data types. [Table 2.Mapping FPGA Module Data Types
 to VHDL Data Types](creating-or-acquiring-ip-fpga-module.html#GUID-12D5C11C-85D9-4569-BF86-DEEC606A0E4A__TABLE_ZWT_LKZ_YHC) lists the FPGA Module data types and the corresponding VHDL data types.

| FPGA Module Data Type | VHDL Data Type |
| --- | --- |
| Boolean | std_logic |
| U8 and I8 | std_logic_vector(7 downto 0) |
| U16 and I16 | std_logic_vector(15 downto 0) |
| U32 and I32 | std_logic_vector(31 downto 0) |
| U64 and I64 | std_logic_vector(63 downto 0) |
| Fixed-point | std_logic_vector(x downto 0)Note x must be in the range [0,63]. |

For example, an IP input port of type std_logic_vector(31 downto
 0) is represented as a 32-bit unsigned integer (U32) in LabVIEW
 FPGA.

If the VHDL code requires an unsupported width (for example, std_logic_vector(65 downto 0)), create a
 wrapper VHDL file to adapt the port to a supported type.

Note

#### CLIP Clocking

Base and
 derived CLIP clocks run free and remain stable after Reset
 deasserts. Use stable external clocks; clocks that stop or glitch can interrupt CLIP
 behavior.

If CLIP and a VI access the same I/O in the same clock domain,
 synchronization registers add latency. You can disable synchronization to reduce
 latency.

- In FPGA I/O Properties .
- In FPGA I/O Node Properties .
- In the VHDL code of the CLIP.

#### Resetting VHDL Code

When
 you use the Reset method, include a single asynchronous reset input so the VHDL code
 resets with the FPGA VI.

If you do not include an asynchronous reset,
 implement an alternate reset mechanism to ensure the VHDL code functions properly
 before, during, and after the reset.

#### Constraints and
 Hierarchy

You can include CLIP-specific constraints using a constraints
 file, except for pin placement constraints. For example, constrain the period of a
 clock accessed through a global clock buffer.

To apply constraints regardless
 of component location in the VHDL hierarchy, use macros such as:

```text
NET "%ClipInstancePath%/myCLIPIO*" TNM_NET = %ClipInstanceName%myCLIPIO;
TIMESPEC TS_%ClipInstanceName%ThruMyCLIP = TO "%ClipInstanceName%myCLIPIO" 10 ns;
```

```text
create_clock -period 10.000 -name %ClipInstanceName%Clk -waveform {0.000 5.000} -add [get_pins %ClipInstancePath%/clk]
set_clock_latency -clock [get_clocks {%ClipInstanceName%Clk}] 10.0 [get_pins {%ClipInstancePath%/cAddOut[0]}]
```

Notice

Notice

#### Troubleshooting Constraints

- Remove the constraint.
- Use the signal in an FPGA VI.

1. Navigate to C:\NIFPGA .
2. Open the folder for your compilation.
3. Unzip output_files.zip and locate
 unapplied_constraints.xdc .
4. Search for the constraint in the file.

To check whether constraints were applied during compilation, see
 *Verify Unapplied Constraints in a CLIP Compilation*.

#### Best
 Practices

- Verify that CLIP I/O nodes are read and written in the same clock
 domain.
- Do not write constraints that rely on paths outside CLIP logic.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- CLIP Tutorial, Part 1: Creating VHDL Code
- Using VHDL Code as Component-Level IP
- Using the Configure Component-Level IP Wizard

Related tasks:

- Verify Unapplied Constraints in a CLIP Compilation

<!--NI_TOPIC bundle=labview-fpga-module path=creating-peer-to-peer-reader-fifos-fpga-module.html language=enus -->
## TOPIC 00058: Creating Peer-to-Peer Reader FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `creating-peer-to-peer-reader-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-peer-to-peer-reader-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a reader FIFO on an FPGA target for peer-to-peer streaming. For non-FPGA targets, refer to the specific FPGA target documentation for information about creating a peer-to-peer stream. Not all FPGA targets support peer-to-peer FIFOs. Refer to the Target Inform

### Creating Peer-to-Peer Reader FIFOs

Complete the following steps to create a reader FIFO on an FPGA target for peer-to-peer streaming. For non-FPGA targets, refer to the specific FPGA


 target documentation for information about creating a peer-to-peer


 stream.

Note

Target Information

1. Right-click an FPGA target in the Project Explorer window


 and select New»FIFO from the shortcut menu.
2. In the FIFO Properties dialog box, select Peer


 to Peer Reader from the Type pull-down


 menu. If Peer to Peer Reader is unavailable in the


 pull-down menu, the target is not capable of peer-to-peer FIFOs.
3. Enter a name in the Name text box. The FIFO name appears


 in FIFO Method Nodes, so consider naming the FIFO to


 make applications more readable on the block diagram. For example, you might


 want to use the name FIFO Reader .
4. Finish configuring the FIFO and click the OK button to


 close the dialog box.
5. Create an FPGA VI for the reader. The VI must be


 under the same FPGA target as the peer-to-peer FIFO.
6. Create a reference to the reader in the VI hosting the stream


 session.

Parent topic:

Using Peer-to-Peer Streaming with FPGA Targets

Related concepts:

- Creating a Reference to a Peer-to-Peer Reader FIFO
- Using Peer-to-Peer Streaming with FPGA Targets
- FPGA Target Hardware Documentation

<!--NI_TOPIC bundle=labview-fpga-module path=creating-peer-to-peer-writer-fifos-fpga-module.html language=enus -->
## TOPIC 00059: Creating Peer-to-Peer Writer FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `creating-peer-to-peer-writer-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-peer-to-peer-writer-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a writer FIFO on an FPGA target for peer-to-peer streaming. For non-FPGA targets, refer to the specific FPGA target documentation for information about creating a peer-to-peer stream. Not all FPGA targets support peer-to-peer FIFOs. Refer to the Target Inform

### Creating Peer-to-Peer Writer FIFOs

Complete the following steps to create a writer FIFO on an FPGA target for peer-to-peer streaming. For non-FPGA targets, refer to the specific FPGA


 target documentation for information about creating a peer-to-peer


 stream.

Note

Target Information

1. Right-click an FPGA target in the Project Explorer window


 and select New»FIFO from the shortcut menu.
2. In the FIFO Properties dialog box, select Peer


 to Peer Writer from the Type pull-down


 menu. If Peer to Peer Writer is unavailable in the


 pull-down menu, the target is not capable of peer-to-peer FIFOs.
3. Enter a name in the Name text box. The FIFO name appears


 in FIFO Method Nodes, so consider naming the FIFO to


 make applications more readable on the block diagram. For example, you might


 want to use the name FIFO Writer .
4. Finish configuring the FIFO and click the OK button to


 close the dialog box.
5. Create an FPGA VI for the writer. The VI must be


 under the same FPGA target as the peer-to-peer FIFO.
6. Create a reference to the writer in the VI hosting the stream


 session.

Parent topic:

Using Peer-to-Peer Streaming with FPGA Targets

Related concepts:

- Creating a Reference to a Peer-to-Peer Writer FIFO
- Using Peer-to-Peer Streaming with FPGA Targets
- FPGA Target Hardware Documentation

<!--NI_TOPIC bundle=labview-fpga-module path=creating-triggers-and-counters-fpga-module.html language=enus -->
## TOPIC 00060: Creating Triggers and Counters

- bundle_id: `labview-fpga-module`
- source_path: `creating-triggers-and-counters-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/creating-triggers-and-counters-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Module includes functions for performing basic I/O. However, you might have applications that require customized I/O functionality. Use the FPGA I/O Node as a building block to create customized I/O applications such as triggers and counters. Creating Triggers In many applications, you need

### Creating Triggers and Counters

The FPGA Module includes functions for performing basic I/O. However, you might have


 applications that require customized I/O functionality. Use the FPGA


 I/O Node as a building block to create customized I/O applications such


 as triggers and counters.

#### Creating Triggers

In many applications, you need to wait for a trigger before performing an action.


 You can wait for a trigger on a single digital input using the Wait on Rising Edge


 method with the FPGA I/O Method Node.

Note

The Wait on Rising Edge method waits until a condition you specify is met on the


 digital input before continuing. Place the FPGA I/O Method Node in the first frame


 of a sequence structure and place the LabVIEW code for the task in the next frame,


 as shown in the following block diagram.

[IMAGE alt='image' src='GUID-3CD0E92F-B82B-4B39-886F-5FC7D751A35B-a5.png']

You also can create more advanced triggering events from the FPGA I/O Node. For


 example, you might need an application that triggers only when multiple digital


 lines match a given condition, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-E98FE0C7-006B-4676-92F2-B7AED7430DBA-a5.png']

You can place an FPGA I/O Node configured with a digital input resource in a single-cycle Timed Loop and exit the single-cycle Timed Loop only when


 the digital inputs match the trigger pattern. Place the single-cycle Timed Loop in


 the first frame of a sequence structure, just as you do for the Wait on Rising Edge


 method in the previous example.

You can implement analog triggers using a While Loop in the


 same manner. Place an FPGA I/O Node configured with an analog input I/O resource and


 a Comparison function in a While Loop to trigger when the


 analog input value meets a programmable condition.

#### Creating Counters

Counters can range from simple event counters to complex signal measurements with


 multiple inputs and outputs. You can build a simple event counter with the FPGA I/O


 Method Node function in a While Loop. For example, you can use the Wait on Rising


 Edge method to wait for a rising edge to occur on a digital input terminal, as shown


 in the following block diagram.

[IMAGE alt='image' src='GUID-060C92F0-13AF-4BB2-9DC9-8BA157A862F7-a5.png']

When the FPGA I/O Method Node detects an edge, the block diagram increments the


 counter value and stores the counter value in a shift register on the While Loop.


 You can use a front panel indicator or local variable to view the counter value.

Note

You also can build more advanced counters from the FPGA I/O functions. For example,


 an application might require a counter with independent count up, count down, and


 gate inputs and an output, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-64AE0C01-E422-4CDA-8609-F548987E766B-a5.png']

In the block diagram above, the counter value increments when a rising edge occurs on


 Count Up, the counter value decrements when a rising edge


 occurs on Count Down, and Gate


 prevents count up and count down from changing the counter value when


 Gate is high. Count Up,


 Count Down, and Gate are the names


 of specific digital I/O resources on the FPGA target. The output asserts when the


 counter value is a multiple of four. You can make simple Boolean decisions in


 LabVIEW code to determine if the counter counts up, down, or stays the same. You


 also can make mathematical decisions in LabVIEW code to determine when the output


 asserts.

You can use the FPGA I/O Method Node to take measurements on input signals, as shown


 in the following block diagram. For example, you might need to measure the period of


 an input signal. You can place the FPGA I/O Method Node in the first frame of a


 sequence structure followed by the Tick Count


 Express VI in the second frame of the sequence structure. Then place the sequence


 structure in a While Loop. Wire the current value returned by the Tick Count VI to a


 shift register to serve as the input for the next iteration of the While Loop. Then


 subtract the previous time from the current time to determine the period of the


 input signal.

[IMAGE alt='image' src='GUID-1C097036-D8EE-4A90-AFCA-396640C04598-a5.png']

|  | Tip Use the single-cycle Timed Loop to increase execution speed and to decrease FPGA usage and jitter in counter applications. |
| --- | --- |

Parent topic:

Using FPGA I/O

<!--NI_TOPIC bundle=labview-fpga-module path=dataflow-and-the-enable-chain-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00061: Dataflow and the Enable Chain in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `dataflow-and-the-enable-chain-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/dataflow-and-the-enable-chain-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The enable chain is additional logic that LabVIEW adds to FPGA code to enforce dataflow on the FPGA. The enable chain consists of two parts: A series of registers that run in parallel with the actual flow of data on the block diagram. This part of the enable chain only exists outside single-cycle Ti

### Dataflow and the Enable Chain in FPGA VIs

The enable chain is additional logic that LabVIEW adds to FPGA code to enforce


 dataflow on the FPGA. The enable chain consists of two parts:

- A series of registers that run in parallel with the actual flow of data on the


 block diagram. This part of the enable chain only exists outside single-cycle


 Timed Loops.
- An implicit enable signal that enforces dataflow inside the single-cycle Timed


 Loop. This signal fans out to all nodes within the loop that contain


 state-holding elements.

#### Dataflow Outside a Single-Cycle Timed Loop

LabVIEW executes code in a dataflow manner. Nodes execute when data is present on all


 inputs that the node needs in order to run. When the node finishes execution, the


 outputs of the node pass data to the next node. The following illustration shows an


 example of the FPGA hardware required to implement a Boolean function outside a


 single-cycle Timed Loop.

[IMAGE alt='image' src='GUID-46F6E125-FF4B-4C41-830A-B742ECB77BB2-a5.png']

The enable chain guarantees that the FPGA logic executes in the same order as it


 appears on the LabVIEW block diagram. The illustration shows how the Boolean


 function is converted into FPGA logic when the function is outside a single-cycle


 Timed Loop. The function section of the illustration shows the Boolean logic


 corresponding to a Negate function on the block diagram. The enable chain section


 includes additional synchronization registers that only output on the rising edge of


 the clock.

The following illustration shows an example of FPGA hardware implementing an


 arithmetic operation.

[IMAGE alt='image' src='GUID-111A77CD-388F-4A5F-A05A-0B3A4281240E-a5.png']

Due to enable chain overhead, each function or VI takes a minimum of one clock cycle.


 Some functions, such as analog input operations, can take hundreds of clock cycles,


 depending upon the complexity of the operation and hardware limitations.

#### Dataflow Inside a Single-Cycle Timed Loop

Nodes that you place in a single-cycle Timed


 Loop do not include the register part of the enable chain. Eliminating


 the register overhead reduces the total space used on the FPGA because the


 flip-flops used for the enable chain are no longer required. Also, because the


 enable chain registers are not present, all operations in a single-cycle Timed Loop


 can complete in a single clock cycle. However, some nodes, such as the Memory Method


 Node or the FFT Express VI, take more than one clock cycle to


 execute, so the output of the node is not valid until the next iteration


 of the single-cycle Timed Loop. The number of clock-cycles required to obtain valid


 data is the latency of the node.

#### Understanding How the Implicit Enable Signal Affects Timing Performance

The implicit enable signal from the single-cycle Timed Loop fans out to all flops


 within the diagram. LabVIEW gates the clock associated with the single-cycle Timed


 Loop until the implicit enable signal is removed. The additional routing overhead of


 this fan-out can limit timing performance in large designs. If your design contains


 single-cycle Timed Loops that run independently of other nodes on the block diagram,


 consider removing the implicit enable signal from these loops to improve timing


 performance.

Note

The following represents a block diagram with code in a single-cycle Timed Loop.

[IMAGE alt='image' src='GUID-4DA34E6C-482C-4E69-A68D-784DC3C39CDB-a5.png']

The following illustration shows the VHDL representation of the above block diagram


 code.

[IMAGE alt='image' src='GUID-11B48875-C967-4456-8F39-1ACE6D03D3A1-a5.png']

Notice that by default, the implicit enable signal fans out to each node in the


 single-cycle Timed Loop that contains state-holding elements, such as flip-flops or


 block memory. This routing overhead limits timing performance for some


 applications.

The following illustration shows the same VHDL representation, this time with the


 implicit enable signal removed.

[IMAGE alt='image' src='GUID-F4AF5856-F10B-4097-B82D-BBC10BDEAE07-a5.png']

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Introduction to FPGA Hardware Concepts
- Executing Code in Single-Cycle Timed Loops
- Synchronizing I/O in Single-Cycle Timed Loops
- Viewing Signals Using the Waveform Viewer

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00062: Debugging FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `debugging-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW provides several ways to test and debug all or parts of an FPGA VI. Refer to the following table when deciding what execution mode you should use for verification and debugging. Execution Mode Verify Functional Performance Verify Timing Verify Integration of HDL IP Good for Unit Testing Good

### Debugging FPGA VIs

LabVIEW provides several ways to test and debug all or parts of an FPGA VI. Refer to


 the following table when deciding what execution mode you should use for


 verification and debugging.

| Execution Mode | Verify Functional Performance | Verify Timing | Verify Integration of HDL IP | Good for Unit Testing | Good for Component Testing | Good for System Testing |
| --- | --- | --- | --- | --- | --- | --- |
| Windows PC |  |  |  |  |  |  |
| Simulation Mode |  |  |  |  |  |  |
| FPGA Target |  |  |  |  |  |  |
| Third-Party Simulation |  |  |  |  |  |  |

Note

If you are able to debug and verify extensively at the unit and component levels, you


 will have less verification to do at the system level. Refer to the following


 sections for guidelines on identifying a unit, component, and system.

#### Unit

The unit is the most fundamental level of IP you can build. It maps to a specific


 processing function or algorithm and it does not make much sense to split and test


 it as a set of smaller functional units. Code that is considered a unit may have one


 or more of the following characteristics:

- It does not include any I/O, data communication, or target resources
- It does not have multiple loops running in parallel or at different rates
- You can provide some known inputs and test for expected outputs
- It does not rely on the explicit specific passing or control of time
- It can be called as a subVI that you may want to reuse in other part of your


 design

#### Component

Components are more complex pieces of logic that rely on the timing in the system.


 Components are modular and usually have a clear task or objective to accomplish. You


 can usually break an FPGA VI down into multiple components. The verification at this


 level makes sure that the components interact as expected when integrated into a


 system. You also may want to make sure that a subcomponent is interacting properly


 with the I/O or host VI without having to wait until the whole system is


 assembled.

#### System

The system level is the top-most component, represented by your top-level FPGA VI


 plus any additional HDL IP imported through CLIP. A system usually contains multiple


 While Loops or single-cycle Timed Loops. The system interface is exposed to the host


 application, so verification tests are either very similar in nature to running your


 host application or include your host application. Verification at the system level


 requires you to use the host interface API and to connect all real I/O signals to


 your system.

Related concepts:

- Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-fpga-vis-on-an-fpga-target-fpga-module.html language=enus -->
## TOPIC 00063: Debugging FPGA VIs on an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `debugging-fpga-vis-on-an-fpga-target-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-fpga-vis-on-an-fpga-target-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you get unexpected data from the application running on the FPGA, use the following techniques to identify and correct problems with the FPGA VI or the block diagram data flow: Add indicators to the FPGA VI block diagram to monitor the internal state of the FPGA VI. Use indicators instead of prob

### Debugging FPGA VIs on an FPGA Target

If you get unexpected data from the application running on the FPGA, use the


 following techniques to identify and correct problems with the FPGA VI or the block


 diagram data flow:

- Add indicators to the FPGA VI block diagram to monitor the internal


 state of the FPGA VI. Use indicators instead of probes. Place indicators anywhere on the block diagram where you need to


 see data to verify the functionality of the VI.
- Add I/O to the FPGA VI block diagram. If you have unused I/O


 resources on the FPGA target, you can use the unused resources to monitor the


 internal state of Boolean logic, triggers, and so on.

Tip

Parent topic:

Debugging FPGA VIs

Related concepts:

- Adding Indicators to Monitor FPGA VIs
- Adding I/O to Monitor FPGA VIs
- Debugging FPGA VIs Using Simulation Mode

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-fpga-vis-using-a-third-party-simulator-fpga-module.html language=enus -->
## TOPIC 00064: Debugging FPGA VIs Using a Third-Party Simulator

- bundle_id: `labview-fpga-module`
- source_path: `debugging-fpga-vis-using-a-third-party-simulator-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-fpga-vis-using-a-third-party-simulator-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: As FPGA designs get larger and more complicated, debugging designs on the FPGA chip becomes less efficient because of the time necessary for compiling and downloading to the target. Along with other debugging techniques, third-party simulation can help you test the timing behavior of FPGA VI compone

### Debugging FPGA VIs Using a Third-Party Simulator

As FPGA designs get larger and more complicated, debugging designs on the FPGA chip


 becomes less efficient because of the time necessary for compiling and downloading


 to the target. Along with other debugging techniques, third-party simulation can help you test the


 timing behavior of FPGA VI components. Cycle-accurate third-party simulation means


 that timing is precise but the simulation might not use the exact hardware model to


 implement it.

Note

#### Prerequisites

To use third-party simulation, you must be familiar with the Xilinx simulator and


 install the Xilinx compilation tools necessary for your hardware configuration.

Refer to the support document at


 ni.com for more information about NI hardware supported by each


 Xilinx compilation tool. Refer to the Xilinx Compilation


 Tools Readme for instructions on installing Xilinx compilation tools for


 LabVIEW.

#### Simulating FPGA VIs Using a Third-Party Simulator

You can use the Xilinx simulator to modify the VHDL test bench template that LabVIEW


 creates if you are familiar with VHDL. You must provide simulation models for any IP


 you include through the CLIP and IP Integration Nodes. You specify the models for


 CLIP simulation and the IP Integration Node simulation through their configuration


 wizards.

In the following illustration, the combined shaded areas indicate the parts that make


 up the test bench. LabVIEW generates the test bench template in VHDL. You then can


 edit the LabVIEW host VI to customize interactions with controls, indicators, and


 other LabVIEW objects. In addition, you can create stimulus and response models for


 the I/O within the VHDL test bench.

[IMAGE alt='image' src='GUID-7F872919-74FE-4747-AF3A-C1DCB1531443-a5.png']

Parent topic:

Debugging FPGA VIs

Related concepts:

- Caveats for Using DSP48E and DSP48E1 Functions
- Debugging FPGA VIs
- Implementing FIFOs Using Built-in Control Logic
- Using the Configure Component-Level IP Wizard

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-fpga-vis-using-a-xilinx-simulator-fpga-module.html language=enus -->
## TOPIC 00065: Debugging FPGA VIs Using a Xilinx Simulator

- bundle_id: `labview-fpga-module`
- source_path: `debugging-fpga-vis-using-a-xilinx-simulator-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-fpga-vis-using-a-xilinx-simulator-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following procedure describes how to debug an FPGA VI using a Xilinx simulator and a VHDL test bench template that you edit. Configure LabVIEW to work with a Xilinx simulator. Modify the FPGA VI if necessary. For example, you might want to reduce the simulation run time. Right-click the FPGA tar

### Debugging FPGA VIs Using a Xilinx Simulator

The following procedure describes how to debug an FPGA VI using a Xilinx simulator


 and a VHDL test bench template that you edit.

1. Configure LabVIEW to work with a Xilinx simulator.
2. Modify the FPGA VI if necessary. For example, you might want to reduce the


 simulation run time.
3. Right-click the FPGA target in the Project Explorer 


 window and select Select Execution Mode»Third-Party


 Simulation from the shortcut menu.
4. Create a simulation export build specification.
5. Click the Build button in the Simulation


 Export Properties dialog box to build the simulation export.


 LabVIEW creates the files necessary for simulation and places them in the


 simulation directory.
6. Provide the stimulus and response you want by modifying the VHDL code in the


 template.
7. In the Project Explorer window, right-click the


 simulation export and select Launch Simulator to open the


 simulator project.
8. Click the Run All button to run the simulation.
9. View the signals in the waveform viewer and troubleshoot the FPGA VI. Make


 changes to the FPGA VI if necessary.
10. Integrate the changes into the test bench if necessary.
11. Run RegenerateIsim.bat, located in the user directory, to regenerate the


 simulation executable.
12. Repeat steps 6 through 11 to continue troubleshooting the FPGA VI.

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-fpga-vis-using-simulation-mode-fpga-module.html language=enus -->
## TOPIC 00066: Debugging FPGA VIs Using Simulation Mode

- bundle_id: `labview-fpga-module`
- source_path: `debugging-fpga-vis-using-simulation-mode-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-fpga-vis-using-simulation-mode-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compiling an FPGA VI can take minutes to hours. However, you can test the logic of an FPGA VI before compiling it by executing the FPGA VI in simulation mode using simulated I/O. When you use this test method, LabVIEW generates random data for the inputs or uses a custom VI that you create to provid

### Debugging FPGA VIs Using Simulation Mode

Compiling an FPGA VI can take minutes to hours. However, you can test the logic of an


 FPGA VI before compiling it by executing the FPGA VI in simulation mode using


 simulated I/O. When you use this test method, LabVIEW generates random data for the


 inputs or uses a custom VI that you create to provide I/O. You also can use the FPGA


 Desktop Execution Node to communicate with FPGA resources that you select and to


 debug your FPGA design. For some FPGA targets, you also can execute the FPGA VI in


 simulation mode using real I/O.

When you run the FPGA VI in simulation on the development computer, you can use all


 traditional LabVIEW debugging techniques, such as probes, execution highlighting,


 breakpoints, and single-stepping, as well as debugging techniques that are specific


 to the FPGA host VI context.

Tip

To debug your FPGA design in simulation mode using simulated I/O, select from the


 following options:

- Sampling probes —Use this option to check intermediate


 values on a wire as a VI runs and to view changes in signal data over time.
- FPGA Desktop Execution Node —Use this option if you need


 to test individual design elements of your FPGA VI, or for system-level testing


 for designs that rely on supported features. Supported features include front


 panel controls and indicators, I/O resources, and resources that use simulated


 time. Refer to the "Understanding Simulated Time on the Host" section for a list


 of features that use simulated time.
- Custom VI test bench —Use this option if you need to


 create the data coming from a particular input or monitor an output.

#### Sampling Probes

Use Sampling probes in host VIs or FPGA VIs to check intermediate values on a wire as


 a VI runs and to view changes in signal data over time, such as when you need to


 debug signals from a single-cycle Timed Loop. When you use a Sampling probe in a


 host VI, you must first specify a sampling source for the probe.

You cannot use the Sampling Probe Watch Window to change data.


 The probe has no effect on the way a VI runs.

#### FPGA Desktop Execution Node

Before debugging an FPGA VI using a test bench, you can test the logic of the VI


 without compiling it by running the FPGA VI in simulation mode using simulated I/O.


 This test method saves compilation time, makes tests easier to repeat, and decreases


 the number of modifications necessary to create a test bench for additional


 debugging.

The FPGA Desktop Execution Node runs an FPGA VI in simulation mode using simulated


 I/O for a specified number of clock ticks. Use the FPGA Desktop Execution Node to


 test an individual loop containing IP you develop or an entire FPGA application with


 multiple loops running in parallel at different clock rates. Use this node to


 communicate with FPGA resources that you select and to debug your FPGA design.

Note

#### Custom VI Test Bench

You can create a custom VI to simulate I/O in LabVIEW for use as a test bench for


 your FPGA VI. You can use a custom VI as a test bench to create the data coming from


 a particular input or monitor an output. Every time an FPGA VI reads an input by


 calling an FPGA I/O Node, LabVIEW uses the custom VI you specify to provide the


 data. Using custom VIs for FPGA I/O creates a repeatable scenario for testing and


 makes it possible to change the data for a particular input. You also can use custom


 VIs for FPGA I/O to monitor an output from FPGA I/O Nodes.

(Statechart) You also can debug


 statecharts for an FPGA target on the development computer.

#### Understanding Simulated Time

If you use certain FPGA resources and you execute the FPGA VI in simulation mode


 using simulated I/O, the resource uses simulated time instead of real time.


 Simulated time might be faster than real time depending on the number of events that


 occur during the simulation. For example, if you add a Wait (Simulated Time) VI to


 the block diagram and set the delay to 1000 ms, LabVIEW does not attempt to delay


 one second of real time. Instead, LabVIEW delays as long as necessary before


 executing the next scheduled action in the simulation.

The following resources use simulated time on the host:

- While Loops
- Single-Cycle Timed Loops
- Wait (Simulated Time) VI
- Loop Timer Express VI
- Tick Count Express VI
- FIFOs, except DMA FIFOs
- Wait on Occurrence with Timeout in Ticks Function
- Interrupt VI, when Wait Until Cleared is TRUE

Parent topic:

Debugging FPGA VIs

Related concepts:

- Clearing FPGA FIFOs
- Debugging FPGA VIs on an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=debugging-with-the-fpga-desktop-execution-node-fpga-module.html language=enus -->
## TOPIC 00067: Debugging with the FPGA Desktop Execution Node

- bundle_id: `labview-fpga-module`
- source_path: `debugging-with-the-fpga-desktop-execution-node-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/debugging-with-the-fpga-desktop-execution-node-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FPGA Desktop Execution Node to test an individual loop containing IP you develop or an entire FPGA application with multiple loops running in parallel at different clock rates. Because the FPGA Desktop Execution Node executes an FPGA VI in simulation mode, you can develop tests for FPGA VIs

### Debugging with the FPGA Desktop Execution Node

Use the FPGA Desktop Execution Node to test an individual loop containing IP you


 develop or an entire FPGA application with multiple loops running in parallel at


 different clock rates. Because the FPGA Desktop Execution Node executes an FPGA VI


 in simulation mode, you can develop tests for FPGA VIs that contain target


 resources, such as I/O and memory items.

Note

Complete the following steps to debug an FPGA VI using the FPGA Desktop Execution


 Node:

1. In the Project Explorer window, right-click the FPGA target and select


 Properties to display the FPGA Target Properties


 dialog box. Note You also can right-click the FPGA target and


 select Select Execution Mode»Simulation (Simulated


 I/O).
2. On the Execution Mode page, select


 Simulation.
3. From the pull-down menu, select Use Simulated I/O .
4. From the host VI, add the FPGA Desktop Execution Node to the block diagram.
5. Configure the FPGA Desktop Execution Node. LabVIEW creates block diagram inputs


 or outputs for the FPGA resources you specify. Select the resources that you


 want to debug.
6. Click OK to finish configuring the FPGA Desktop Execution


 Node.
7. Run the host VI. You now can use standard LabVIEW debugging tools to analyze the


 simulated data the FPGA Desktop Execution Node returns.

Parent topic:

Debugging FPGA VIs Using Simulation Mode

<!--NI_TOPIC bundle=labview-fpga-module path=deciding-which-data-type-to-use-in-fpga-designs-fpga-module.html language=enus -->
## TOPIC 00068: Deciding Which Data Type to Use in FPGA Designs

- bundle_id: `labview-fpga-module`
- source_path: `deciding-which-data-type-to-use-in-fpga-designs-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/deciding-which-data-type-to-use-in-fpga-designs-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes the implications of using the integer, fixed-point, and single-precision floating-point data types for specific use cases. Use this table to help you decide which data type best suits your FPGA application. Use Case Data Type Data Precision FPGA Resource Use Latency You

### Deciding Which Data Type to Use in FPGA Designs

The following table describes the implications of using the integer, fixed-point,


 and single-precision floating-point data types for specific use cases. Use this


 table to help you decide which data type best suits your FPGA application.

| Use Case | Data Type | Data Precision | FPGA Resource Use | Latency |
| --- | --- | --- | --- | --- |
| You need to choose between calibrated fixed-point or uncalibrated integer I/O node outputs. | Integer | Proportional to word length. Higher dynamic range requires longer word lengths. | Proportional to word length. | Proportional to clock rate. |
| Your designs include data packing of multiple integers into a 32- or 64-bit word. |  |  |  |  |
| Your designs require bit manipulations, such as masking or inverting. |  |  |  |  |
| Your designs require resource-efficient arithmetic. | Fixed-point |  |  |  |
| You need to acquire analog I/O from a cRIO chassis. |  |  |  |  |
| You need to use High Throughput Math functions. |  |  |  |  |
| You need to represent very large and very small numbers in the same data path, such as with accumulators. | Single-precision floating-point | 24-bit precision is maintained even for high dynamic range data paths. | Significantly higher than fixed-point, especially for functions like Add, Subtract, and Multiply. | Requires more clock cycles to compute than operations using the fixed-point or integer data types. |
| You need to rapidly prototype. Use single-precision floating-point to get functional hardware designs quickly. Convert to fixed-point as necessary to optimize FPGA performance or resource usage. |  |  |  |  |

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=defining-the-ip-interface-fpga-module.html language=enus -->
## TOPIC 00069: Defining the IP Interface

- bundle_id: `labview-fpga-module`
- source_path: `defining-the-ip-interface-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/defining-the-ip-interface-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To add IP as a component-level IP (CLIP) item in a LabVIEW project, the IP must have an accompanying declaration XML file to define the I/O for the FPGA Module. The declaration XML file describes the elements of the IP. The FPGA Module uses this file to add the IP to a LabVIEW project. Refer to www.

### Defining the IP Interface

To add IP as a component-level IP (CLIP) item in a LabVIEW project, the IP must have an
 accompanying declaration XML file to define the I/O for the FPGA Module. The
 declaration XML file describes the elements of the IP. The FPGA Module uses this
 file to add the IP to a LabVIEW project.

Refer to www.w3.org/XML for information about using XML.

#### Creating a Declaration
 File

Note

Configure Component-Level IP

Configure
 Component-Level IP

The first line of the declaration file includes the XML version. All tags inside the
 file must be enclosed in <CLIPDeclaration> tags as shown
 below:

<?xml version="1.0"?>
 <CLIPDeclaration Name="My VHDL IP">
 <!-- Insert tags here -->
 </CLIPDeclaration>

| Tag | Required? | Parent Tag | Number of Tags with Parent Tag | Description |
| --- | --- | --- | --- | --- |
| CLIPDeclaration | Yes | — | — | All CLIP definitions must be contained within this tag. Name is a required attribute that defines the name of the CLIP that LabVIEW displays. |
| FormatVersion | Yes | CLIPDeclaration | 1 | Defines the version of the CLIP tags to use in this declaration XML file. Set FormatVersion to 4.3. |
| Description | No | CLIPDeclaration | 1 | Describes this CLIP and displays this description on the General page of the Component-Level IP Properties dialog box. |
| SupportedDeviceFamilies | No | CLIPDeclaration | 1 | Defines the supported device families using a comma-delimited list. LabVIEW recognizes the following devices: Spartan-3, Spartan-3E, Spartan-6, Virtex-II, Virtex-II Pro, Virtex-5, Virtex-6, Virtex-7, Zynq, Kintex-7. You also can specify Unlimited to support all families. |
| CompatibleCLIPSocketList | No | CLIPDeclaration | 1 | For socketed CLIP, specifies which sockets the CLIP supports. |
| Socket | Yes | CompatibleCLIPSocketList | 1 or more | For socketed CLIP, specifies the compatible socket names. |
| TopLevelEntityAndArchitecture | Yes | CLIPDeclaration | 1 | Specifies the entity and architecture for the top-level synthesis and simulation VHDL files. |
| SynthesisModel | Yes | TopLevelEntityAndArchitecture | 1 | Specifies the entity and architecture name for the top-level synthesis VHDL file. |
| Entity | Yes | SynthesisModel | 1 | Specifies the entity name for the top-level synthesis VHDL file. |
| Architecture | No | SynthesisModel | 1 | Specifies the architecture name for the top-level synthesis VHDL file. |
| SimulationModel | No | TopLevelEntityAndArchitecture | 1 | Specifies the entity and architecture name for the top-level simulation VHDL file. |
| Entity | Yes | SimulationModel | 1 | Specifies the entity name for the top-level simulation VHDL file. |
| Architecture | No | SimulationModel | 1 | Specifies the architecture name for the top-level simulation VHDL file. |
| InterfaceList | Yes | CLIPDeclaration | 1 | Contains one or more interface definitions. You cannot nest interface lists. You can define only one interface list. |
| Interface | Yes | InterfaceList | 1 or more | Defines all the I/O, clocks, and other signals available to or from the CLIP. You cannot nest interfaces. Name is a required attribute. |
| InterfaceType | Yes | Interface | 1 | Defines where the interface is connected in the FPGA. You can enter one of the following values: LabVIEW: Interface connects to the FPGA Module. All I/O and clocks are available as resources in the FPGA Module. Socket: Interface connects directly to a target-defined socket. The I/O and clocks are not available as resources in the FPGA Module. Fabric: Interface connects directly to the FPGA. The I/O and clocks are not available as resources in the FPGA. |
| SignalList | Yes | Interface | 1 | Contains one or more signal definitions. You cannot nest SignalList tags. |
| Signal | Yes | SignalList | 1 or more | Defines a signal that will be available to or from the CLIP. Must contain the Name attribute, which the FPGA Module uses for display purposes. The Name attribute must begin with a letter and must only contain English letters and numbers, periods, dashes, and underscores. The default is the HDLName you declare in the Signal tag. To organize signals into a CLIP IO hierarchy, use periods as delimiters in the name. For example, signals named A.Input and A.Output create a folder called A that contains signals Input and Output in the project. |
| Description | No | Signal | 1 | Specifies a description for the signal. |
| HDLName | No | Signal | 0 or 1 | Defines the name of the I/O entity in the VHDL file. The HDLName for the port must be the same as the name in the top-level synthesis file. |
| RequiredClockDomain | No | Signal | 0 or 1 | If you do not specify a required clock domain, you can use the I/O in any clock domain. The value of RequiredClockDomain must match a clock signal name defined in another location of the CLIP XML file. If you require a clock domain, any I/O Node on the block diagram that uses this CLIP I/O must be in the clock domain you specify. If the I/O Node is in the wrong clock domain, LabVIEW returns an error during compilation of the FPGA VI. |
| LeaveUndrivenIfNotUsedInLabVIEW | No | Signal | 0 or 1 | Specifies to not drive a signal in the top-level file when the VHDL has a default value. Otherwise, LabVIEW drives the signal with all zeros during code generation. |
| HDLType | Yes | Signal | 1 | Specifies the VHDL port type of a signal. Only std_logic and std_logic_vector are supported. Reset and clock signals can only be std_logic. |
| UseInLabVIEWSingleCycleTimedLoop | No | Signal | 0 or 1 | Valid values are: NotAllowed, Allowed, Required. The default value is Allowed. This tag specifies how you can use CLIP I/O in a single-cycle Timed Loop. In a single-cycle Timed Loop, you can ensure that data latches on every clock edge. If the IP in the CLIP expects to receive values on every clock edge, then setting this tag to Required makes LabVIEW enforce this requirement. |
| SpecificTargetClock | No | Signal | 0 or 1 | Specifies one of the available FPGA target base clocks as the required clock connection for the CLIP clock. The value of this tag is the name of the specific FPGA target base clock. The FPGA target base clock must exist in the project and must meet the required frequency range specified in the declaration XML file. |
| DataType | Yes | Signal | 1 | Defines the data type of the signal. If the signal is for a LabVIEW interface, the data type also defines how LabVIEW represents this signal. If the signal is for a socket interface, the data type must match the data type of the signal in the socket. Use one of the following child tags to define the data type: <Boolean /> <U8 /> <U16 /> <U32 /> <U64 /> <I8 /> <I16 /> <I32 /> <I64 /> <FXP>...</FXP> <Array>...</Array> |
| Boolean | No | DataType or Array | See parent tag | Specifies that the VHDL code uses std_logic. * |
| U8 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(7 downto 0). * |
| U16 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(15 downto 0). * |
| U32 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(31 downto 0). * |
| U64 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(63 downto 0). * |
| I8 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(7 downto 0). * |
| I16 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(15 downto 0). * |
| I32 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(31 downto 0). * |
| I64 | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(63 downto 0). * |
| FXP | No | DataType | See parent tag | Specifies that the VHDL code uses std_logic_vector(x downto 0), where x is in range [0,63]. * |
| WordLength | No | FXP | 0 or 1 | Specifies the word length of the FXP signal. The supported range is [1, 64]. |
| IntegerWordLength | No | FXP | 0 or 1 | Specifies the integer word length of the FXP signal. The supported range is [-2048, 2047]. |
| Unsigned | No | FXP | 0 or 1 | Add this tag if the FXP signal is unsigned. Do not add this tag if the FXP signal is signed. |
| Array | No | DataType | See parent tag | Creates an array of the Boolean data type. You must include the Boolean tag within the Array tag. You can use only the Array tag with socketed CLIP. |
| Size | Yes | Array | 1 | Specifies the size of the array. |
| Direction | No | Signal | 0 or 1 | Indicates if the CLIP receives or sends data on the signal. You can select from the following values: ToCLIP: Use for the CLIP to receive data on the signal. ToCLIP is the default value. FromCLIP: Use for the CLIP to send data on the signal. Bidirectional: Use for bidirectional lines. Support for Bidirectional is available only with socketed CLIP. |
| SignalType | No | Signal | 0 or 1 | Indicates the type of signal. You can select from the following values: data: Use if the signal is a standard I/O data signal. If you do not specify a value for the SignalType tag, the default is data. clock: Use if the signal is a clock. If you use clock, you must use the <Boolean/> tag within the DataType tag. reset: Use if the signal is a reset signal that connects to the global asynchronous reset signal of the FPGA VI; refer to the Resetting VHDL Code section in the Creating or Acquiring IP topic. The global asynchronous reset signal for FPGA VIs is active-high. You can use reset only if the InterfaceType tag is set to Fabric. A reset signal must be a ToCLIP signal. clock status: There are two types of clock status signals: SourceClockReady and DerivedClocksValid. Both signals are required for each FromCLIP clock with the SupportDerivedClocks tag. These signals together implement the handshaking interface with the LabVIEW FPGA clocking circuitry that produces derived clocks. |
| FreqInHertz | No | Signal | 1 | Defines the frequency range of the signal. The FreqInHertz tag is required if the SignalType is set to clock. |
| Max | Yes | FreqInHertz | 1 | Defines the maximum supported frequency in SI notation. The Max tag is required if you include a FreqInHertz tag. ** |
| Min | No | FreqInHertz | 0 or 1 | Defines the minimum supported frequency in SI notation. If you do not specify a value for Min, the Min value equals the Max value. ** |
| ImplementationList | Yes | CLIPDeclaration | 1 | Defines the CLIP files to include. The CLIP files do not need to be in the same directory. You can include only one ImplementationList tag. |
| Path | Yes | ImplementationList | 1 or more | Defines the path or directory that contains the implementation file(s) that are required for the IP to compile. The path to a directory does not include subdirectories, so you must define subdirectories in separate tags. The Path tag assumes either a path relative to the XML file or an absolute path. When defining a relative path to a subdirectory, use two periods in a row (..) to indicate the parent directory of the current working directory, a period (.) to indicate the current working directory, and a slash (/ or \\) to get to the next subdirectory. For example, use ../folderA/fileB.vhd to point to the fileB.vhd file that is inside of the folderA directory, which is at the same hierarchical level as the folder containing the XML file on disk. Use /folderA/fileB.vhd to point to the fileB.vhd file that is inside of the folderA directory, which is at the same hierarchical level as the XML file on disk. LabVIEW returns an error for invalid paths. LabVIEW does not return an error for a path to an empty directory unless no other file or directory tags exist in the XML file.Name is a required attribute of this tag and must be the same as the synthesis filename. |
| MD5 | No | Path | 1 | Detects whether a synthesis file has been modified. |
| TopLevel | No | Path | 0 or 1 | Indicates whether the current synthesis file is the top-level file. One and only one VHDL file can be a the top-level synthesis file. |
| SimulationFileList | No | Path | 1 | Defines the simulation file(s) for a specific synthesis file. You can include only one <SimulationFileList> tag for one synthesis file. This tag is required when <SimulationModel> is present. |
| Path | No | SimulationFileList | 1 or more | Defines the path or directory that contains the simulation file(s) that are required for the IP to compile. The path to a directory does not include subdirectories, so you must define subdirectories in separate tags. The Path tag assumes either a path relative to the XML file or an absolute path. When defining a relative path to a subdirectory, use two periods in a row (..) to indicate the parent directory of the current working directory, a period (.) to indicate the current working directory, and a slash (/ or \\) to get to the next subdirectory. For example, use ../folderA/fileB.vhd to point to the fileB.vhd file that is inside of the folderA directory, which is at the same hierarchical level as the folder containing the XML file on disk. Use /folderA/fileB.vhd to point to the fileB.vhd file that is inside of the folderA directory, which is at the same hierarchical level as the XML file on disk. LabVIEW returns an error for invalid paths. LabVIEW does not return an error for a path to an empty directory unless no other file or directory tags exist in the XML file. This tag is required under <SimulationModelType> when the <SimulationModelType> is User-defined. The simulation file name should be specified as the name attribute of this tag. Name is a required attribute. |
| SimulationModelType | Yes | SimulationFileList | 1 | Defines the simulation model type for a specific synthesis file. The options are: Same as synthesis, User-defined, and Exclude from simulation model. For non-netlist files, the default option is Same as synthesis. For netlist files, the default option is Exclude from simulation model, and Same as synthesis is not supported. |
| NumberOfDCMsNeeded | No | CLIPDeclaration | 0 or 1 | Reserves a certain number of digital clock managers (DCM) on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many DCMs. |
| NumberOfMMCMsNeeded | No | CLIPDeclaration | 0 or 1 | Reserves a certain number of mixed mode clock managers (MMCM) on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many MMCMs. |
| NumberOfBufGsNeeded | No | CLIPDeclaration | 0 or 1 | Reserves a certain number of BUFGs on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many global clock nets. |
| DutyCycleRange | No | Signal | 0 or 1 | Defines the maximum and minimum duty cycles that the clock supports. The default value is 50 percent. Include the % symbol after the value. |
| PercentInHighMax | No | DutyCycleRange | 0 or 1 | Defines the maximum time in percentage that the clock is held high. The default value is 50 percent. Include the % symbol after the value. ** |
| PercentInHighMin | No | DutyCycleRange | 0 or 1 | Defines the minimum time in percentage that the clock is held high. The default value is 50 percent. Include the % symbol after the value. ** |
| AccuracyInPPM | In ToCLIP: No In FromCLIP: Yes | Signal | 0 or 1 | Specifies the accuracy of the CLIP clock in parts per million. ** |
| JitterInPicoSeconds | In ToCLIP: No In FromCLIP: Yes | Signal | 0 or 1 | Specifies the jitter of the CLIP clock in picoseconds. ** |
| GenericList | No | CLIPDeclaration | 1 | Specifies information about the VHDL generic. |
| Generic | Yes | GenericList | 1 or more | Specifies the generic name as an attribute of this tag. |
| Description | No | Generic | 1 | Specifies a description for the generic. The description appears in the message box of the Generics and Syntax Check page of the Component-Level IP Properties dialog box. |
| GenericType | Yes | Generic | 1 | Specifies the generic type from the top-level synthesis file. |
| DefaultValue | Yes | Generic | 1 | Specifies the default value for the generic. This value is from the top-level synthesis file. You can specify another value to override the DefaultValue on the Generics and Syntax Check page of the Component-Level IP Properties dialog box or in the CLIP wizard. |
| SupportDerivedClocks | No | Signal | 1 | This tag is required for each FromCLIP clock that supports derived clocks. If this tag is present, the SourceClockReadyHDLName and DerivedClocksValidHDLName tags are also required. This tag is only valid for FromCLIP clock signals. |
| SourceClockReadyHDLName | No | Signal | 1 | This tag is required for each FromCLIP clock that has the SupportDerivedClocks tag. This is the HDL name of the clock status type signal in the FromCLIP direction. The presence of this HDL name indicates that the FromCLIP clock is valid and free-running. Once asserted, this signal should remain asserted until the DerivedClocksValid signal is asserted. De-asserting this signal indicates that the FromCLIP clock is about to be turned off. After de-asserting this signal, the FromCLIP clock should not be turned off until the DerivedClocksValidHDLName signal is de-asserted. |
| DerivedClocksValidHDLName | Yes | Signal | 1 | This tag is required for each FromCLIP clock that has the SupportDerivedClocks tag. This is the HDL name of the clock status type signal in the ToCLIP direction. The presence of this HDL name indicates that all derived clocks generated by the LabVIEW FPGA clock generation circuitry and sourced by this FromCLIP clock are valid and free-running. This signal serves two purposes: The de-assertion of this signal indicates to the CLIP that it is safe to disable the FromCLIP clock. This signal indicates to the CLIP when the generated derived clocks are valid. This tag is required for each external clock that supports derived clocks. |
| SupportsGating | ToCLIP: Yes In FromCLIP: No | Signal | 1 | This tag is required for each ToCLIP gated clock in order to support removing implicit enable signals from single-cycle Timed Loops. |
| CyclesRequiredBeforeAsynchronousResetClears | ToCLIP: Yes In FromCLIP: No | Signal | 1 | Defines the number of clock edges of this clock that must occur while asynchronous reset is asserted. This value must be 0 for this CLIP to be used when the build specification is configured to allow the removal of implicit enable signals because the asynchronous reset will assert and deassert before the clock starts running. This value must also be 0 if this clock is used with external clocks that may stop during reset. If a CLIP requires a running clock during asynchronous reset, such as for CLIP that use built-in FIFOs, and the design requires the removal of implicit enable signals, consider creating a local asynchronous reset, and prevent diagram access to or from the CLIP while this local reset is asserted. |
| ReadBeforePlace | No | Path | 1 | This tag can be applied to one or more XDC files. An XDC file contains constraints that are read by the Xilinx Vivado toolchain. An XDC file with ReadBeforePlace tag will be read by the Xilinx Vivado toolchain just before invoking the Place process, while an XDC file without ReadBeforePlace tag will be read by the Xilinx Vivado toolchain just before invoking the Synthesis process. This tag is available in LabVIEW FPGA 2022 and later, with CLIP FormatVersion 4.3 and later. This tag will not be set by the wizard and should be set manually. This tag is not available in the UCF file which contains constraints that are read by the Xilinx ISE toolchain. |

* This tag does not contain a value, so you can use a forward slash in the open tag
 or create empty open and close tags. For example, you can use <Boolean
 /> or <Boolean> </Boolean> to indicate
 a Boolean data type.

** You must use a period as the decimal separator when entering numeric values in
 CLIP parameters. If you use a comma as the decimal separator, LabVIEW returns an XML
 error.

#### Using a Schema to Reduce Errors

XML schema files are definition files that constrain an XML file to a certain format.
 You can add a schema file to most XML editing tools when writing an XML file. Use
 the CLIPDeclaration.xsd schema file in the
 labview\FPGA\CLIP\Schema directory to minimize syntax and
 formatting errors when you create a CLIP declaration file for user-defined CLIP.

Note

CLIPDeclaration.xsd

Note

Configure Component-Level IP

#### Handling Multiple Implementation Files in Different Directories

You can specify multiple files to implement CLIP code. In the following example, the


 CLIP you want to implement has five files saved in the directory structure show


 below:

foo/myCLIPDeclaration.xml

foo/myTop.vhd

foo/mySide.vhd

foo/components/myLeftSubComponent.vhd

foo/components/myMiddleSubComponent.vhd

foo/components/myRightSubComponent.vhd

In the myCLIPDeclaration.xml you can indicate all five VHDL files


 are necessary for the CLIP by using relative paths. Include the following code in


 the XML file to specify that the two VHDL files in the foo


 directory and all the files in the components are necessary.

<ImplementationList>

<Path Name="./myTop.vhd">

<TopLevel/></Path>

<Path Name="./mySide.vhd"></Path>

<Path Name="./components"></Path>

(

<Path


 Name="./components/myLeftSubComponent.vhd"></Path>

<Path


 Name="./components/myMiddleSubComponent.vhd"></Path>

<Path


 Name="./components/myRightSubComponent.vhd"></Path>

)

</ImplementationList>

Refer to the CLIP Tutorial, Part 2: Defining the Interface for an example of defining


 the CLIP interface.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- CLIP Tutorial, Part 2: Defining the Interface
- Using the Configure Component-Level IP Wizard

<!--NI_TOPIC bundle=labview-fpga-module path=defining-the-top-level-synthesis-file-fpga-module.html language=enus -->
## TOPIC 00070: Defining the Top-Level Synthesis File

- bundle_id: `labview-fpga-module`
- source_path: `defining-the-top-level-synthesis-file-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/defining-the-top-level-synthesis-file-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The top-level synthesis file defines the entity that the IP Integration Node synthesizes. If the top-level file is a .vhd file, this file also defines the architecture to use. In addition, the top-level synthesis file contains a list of ports that correspond to input and output terminals of the node

### Defining the Top-Level Synthesis File

The top-level synthesis file defines the entity that the IP Integration Node


 synthesizes. If the top-level file is a .vhd file, this file also


 defines the architecture to use. In addition, the top-level synthesis file contains


 a list of ports that correspond to input and output terminals of the node.

LabVIEW assumes the first .vhd file, Xilinx IP configuration file,


 or netlist file you add is the top-level file. Complete the following steps to


 specify another file as the top-level synthesis file.

1. Ensure the file meets the requirements for top-level synthesis files.
2. If you have not done so already, add the synthesis


 file to the list of synthesis files the IP Integration Node


 uses.
3. Select this file in the IP Source table.
4. Click the Set as Top Level button: [IMAGE alt='image' src='GUID-96521BE9-83CD-4057-B8FE-D24DEDEA336A-a5.png'] LabVIEW displays an icon to the left of the top-level file.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=designing-a-host-vi-to-read-data-in-dma-applications-fpga-module.html language=enus -->
## TOPIC 00071: Designing a Host VI to Read Data in DMA Applications

- bundle_id: `labview-fpga-module`
- source_path: `designing-a-host-vi-to-read-data-in-dma-applications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/designing-a-host-vi-to-read-data-in-dma-applications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Designing a host VI to read data from a DMA channel is an important part of implementing a DMA application. The designs discussed in this topic apply for applications that transfer data from an FPGA target to a host computer. Choosing a Design The following table summarizes some useful designs: Use

### Designing a Host VI to Read Data in DMA Applications

Designing a host VI to read data from a DMA channel is an important part of implementing a DMA application.

Note

#### Choosing a Design

The following table summarizes some useful designs:

| Use Case | Design | Advantages | Disadvantages |
| --- | --- | --- | --- |
| An application in which one or more of the following situations occur: The FPGA acquires data at an unknown rate. You do not know when data acquisition will start; for example, a hardware device triggers acquisition at an unknown or irregular interval. You must read all data from the buffer before executing any other tasks. | Blocking | Simplest programming design. Data throughput is higher than with either polling design. | The host VI can read either the entire Number of Elements or nothing. You wire this number to the FIFO.Read method of the Invoke Method function. For some targets, the host VI cannot execute any other tasks while waiting for the Number of Elements to become available. For these targets, if you are running the host VI on a real-time system, the real-time system may become temporarily inaccessible from the host desktop system. Refer to your target hardware documentation for more information about DMA restrictions. |
| A data logging application where the FPGA acquires data at a known rate but the host computer reads data at an unknown or irregular rate. | Polling a variable number of elements | The host VI can read any number of elements as soon as the data becomes available to read. | Compared with the blocking design: Reading data takes more time.Data throughput might be lower. |
| An application that requires a fixed, known amount of data to be read before continuing but must complete other tasks while waiting for data to become available. For example, consider an application that processes 1024 elements as a single frame of data but also must send commands to another target. The fixed-polling design reads data from the buffer when data is available but sends the necessary commands when it is not. This design also is useful if the FPGA acquires data at an unknown or irregular rate. | Polling a fixed number of elements | The host VI can execute other sequential tasks while waiting for data to become available. | The host VI can read either the entire Number of Elements or nothing. You wire this number to the FIFO.Read method of the Invoke Method function. Compared with the blocking design: Reading data takes more time.Data throughput might be lower. |

#### Programming the Host VI

Consider the following FPGA VI:

[IMAGE alt='image' src='GUID-1EAA3188-905D-4639-9686-1F111770A29E-a5.png']

This VI represents data acquisition by measuring the temperature of an FPGA device at



 a pre-determined rate and writing this temperature value to an FPGA DMA buffer. The



 following sections show example host VIs that read this data.

#### Blocking

[IMAGE alt='image' src='GUID-6BF9B35E-4343-4555-A2AA-6E529F629860-a5.png']

#### Polling a Variable Number of Elements

[IMAGE alt='image' src='GUID-BC921062-3C12-4526-8863-27F3146F0FAD-a5.png']

Notice how the Number of Elements this VI reads changes based



 on the number of Elements Remaining after the previous



 read.

#### Polling a Fixed Number of Elements

[IMAGE alt='image' src='GUID-2E2DF1DC-CA50-4DC8-9EFB-D557573609C7-a5.png']

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Best Practices for DMA Applications
- Synchronizing the FPGA and the Host
- Transferring Data Using Direct Memory Access

<!--NI_TOPIC bundle=labview-fpga-module path=determining-the-maximum-number-of-dsp48e-or-dsp48e1-functions-you-can-use-fpga-module.html language=enus -->
## TOPIC 00072: Determining the Maximum Number of DSP48E or DSP48E1 Functions You Can Use

- bundle_id: `labview-fpga-module`
- source_path: `determining-the-maximum-number-of-dsp48e-or-dsp48e1-functions-you-can-use-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/determining-the-maximum-number-of-dsp48e-or-dsp48e1-functions-you-can-use-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each DSP48E or DSP48E1 function you add to the block diagram represents one DSP48E or DSP48E1 slice, respectively. Each FPGA has a certain number of DSP48E or DSP48E1 slices available. Complete the following steps to determine the maximum number of functions you can use. You can use the DSP48E fun

### Determining the Maximum Number of DSP48E or
 DSP48E1 Functions You Can Use

Each DSP48E or DSP48E1 function you add to the block diagram represents one


 DSP48E or DSP48E1 slice, respectively. Each FPGA has a certain number of DSP48E or


 DSP48E1 slices available. Complete the following steps to determine the maximum


 number of functions you can use.

Note

1. Right-click the FPGA target in the Project Explorer 


 window and select Properties from the shortcut menu.


 LabVIEW displays the FPGA Target Properties dialog box.
2. Look in the Target Information text box for the
 Type of the FPGA. A Type of
 xc5v indicates the target is a Virtex-5 FPGA. A
 Type of xc6v indicates the
 target is a Virtex-6 FPGA. For example, the NI PCIe-7841R has a
 Type of xc5vlx30 , meaning it
 is a Virtex-5 FPGA and supports only DSP48E functions: [IMAGE alt='image' src='GUID-D1E851FE-399F-4ED5-8D9F-851A47E55E2F-a5.png']
3. DSP48E: Refer to Table 1-1 in the Virtex-5 FPGA XtremeDSP Design Considerations User Guide,
 available on the Xilinx Web site at www.xilinx.com. DSP48E1: Refer to Table 1-1
 in the Virtex-6 FPGA DSP48E1 Slice User Guide .
4. DSP48E: Find the Device DSP table cell that matches the
 Type of the FPGA. The subsequent columns show the
 maximum number of DSP48E slices on that type of FPGA. For example, the xc5vlx30
 type has 32 DSP48E slices. This number means that if you are programming an NI
 PCIe-7841R, you can add a maximum of 32 DSP48E functions to the block
 diagram.(DSP48E1) Find the Total DSP48E1 Slices per
 Device table cell that matches the Type 
 of the FPGA. This column shows the maximum number of DSP48E1 and DSP48E
 functions you can add to the block diagram.

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- DSP48E Example: Creating a Complex Multiplier

<!--NI_TOPIC bundle=labview-fpga-module path=determining-when-to-use-reentrant-or-non-reentrant-subvis-fpga-module.html language=enus -->
## TOPIC 00073: Determining When to Use Reentrant or Non-Reentrant SubVIs

- bundle_id: `labview-fpga-module`
- source_path: `determining-when-to-use-reentrant-or-non-reentrant-subvis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/determining-when-to-use-reentrant-or-non-reentrant-subvis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a subVI as reentrant or non-reentrant. By default, subVIs created under an FPGA target are reentrant. The following table provides recommendations for specific use cases. SubVI Type Design Reentrant Use when a subVI does not access shared resources, such as I/O. Non-reentrant Use w

### Determining When to Use Reentrant or Non-Reentrant SubVIs

You can configure a subVI as reentrant or non-reentrant. By default, subVIs created


 under an FPGA target are reentrant. The following table provides recommendations for


 specific use cases.

| SubVI Type | Design |
| --- | --- |
| Reentrant | Use when a subVI does not access shared resources, such as I/O. |
| Non-reentrant | Use when a subVI accesses shared resources. |
| Non-reentrant | Use when multiple instances of a subVI share data in a VI, such as functional global variables. |

For other design implementations, use the estimated device utilization and timing


 reports from the Reports pull-down menu of the Compilation Status window to verify which subVI


 configuration meets the needs of your FPGA application. The Compilation


 Status window appears after you compile an FPGA VI. You may need to


 iterate several times before finding the subVI type that works best for your


 application.

[IMAGE alt='image' src='GUID-5C55CC13-A469-4237-B4FB-9AD83447CC5F-a5.png']

Parent topic:

Using SubVIs in FPGA Applications

Related concepts:

- FPGA Memory Items
- Managing Shared Resources
- Optimizing FPGA VIs for Speed and Size
- Storing and Accessing Data From Different Parts of an FPGA Design
- Tutorial: Creating Test Benches

<!--NI_TOPIC bundle=labview-fpga-module path=determining-whether-an-fpga-target-supports-dma-fpga-module.html language=enus -->
## TOPIC 00074: Determining Whether an FPGA Target Supports DMA

- bundle_id: `labview-fpga-module`
- source_path: `determining-whether-an-fpga-target-supports-dma-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/determining-whether-an-fpga-target-supports-dma-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to determine whether an FPGA target supports DMA communication: Right-click the FPGA target in the Project Explorer window and select Properties. LabVIEW displays the FPGA Target Properties dialog box. Locate the Target Information section, which displays the Number of D

### Determining Whether an FPGA Target Supports DMA

Complete the following steps to determine whether an FPGA target supports DMA communication:

1. Right-click the FPGA target in the Project


 Explorer window and select Properties . LabVIEW


 displays the FPGA


 Target Properties dialog box.
2. Locate the Target Information section, which displays the Number of DMA


 Channels.

Note

- Refer to your FPGA target hardware documentation for information about how


 that target supports and handles DMA communication.
- The RIO Scan Interface and the NI Scan Engine require two DMA channels. You


 can use fewer channels by interleaving data over one channel.

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Transferring Multi-Channel Data in DMA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=disconnecting-from-the-fpga-compile-server-fpga-module.html language=enus -->
## TOPIC 00075: Disconnecting from the FPGA Compile Server

- bundle_id: `labview-fpga-module`
- source_path: `disconnecting-from-the-fpga-compile-server-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/disconnecting-from-the-fpga-compile-server-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can disconnect from the compile server if you want to close LabVIEW while a VI is compiling. You do not have to disconnect LabVIEW from the compile server to use LabVIEW while the FPGA VI compiles or to queue up multiple VIs to compile. Do not modify the FPGA VI you are compiling or any of the

### Disconnecting from the FPGA Compile
 Server

You can disconnect from the compile


 server if you want to close LabVIEW while a VI is compiling. You do not


 have to disconnect LabVIEW from the compile server to use LabVIEW while the FPGA VI


 compiles or to queue up multiple VIs to compile.

Note

- SubVIs in the hierarchy of the FPGA


 VI
- Any items under the FPGA target in the Project


 Explorer window
- Component-level IP (CLIP) instantiated under the FPGA


 target

Complete the following steps to disconnect LabVIEW from the compile server.

1. If the Compilation Status window is not displayed,


 right-click a build specification in the Project Explorer 


 window and select Display Compilation Results from the


 shortcut menu to display it.
2. Click the arrow next to the Close button in the


 Compilation Status window and select


 Disconnect All from the pull-down menu. The


 Compilation Status window disappears. You can


 continue to work in LabVIEW or close LabVIEW.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=downloading-an-fpga-vi-to-an-fpga-target-fpga-interface.html language=enus -->
## TOPIC 00076: Downloading an FPGA VI to an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `downloading-an-fpga-vi-to-an-fpga-target-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/downloading-an-fpga-vi-to-an-fpga-target-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW automatically downloads a compiled FPGA VI to the FPGA target when you invoke the Open FPGA VI Reference function. LabVIEW also automatically compiles, downloads, and runs an FPGA VI on the FPGA target when you click the Run button in an FPGA VI if the FPGA target supports interactive front

### Downloading an FPGA VI to an FPGA Target

LabVIEW automatically downloads a compiled FPGA VI to the FPGA target when you invoke


 the Open FPGA VI Reference function. LabVIEW also


 automatically compiles, downloads, and runs an FPGA VI on the FPGA target when you


 click the Run button in an FPGA VI if the FPGA target


 supports interactive front panel communication. LabVIEW does not


 download the FPGA VI if the VI is already on the FPGA target or if the FPGA is


 reserved for other purposes.

You can force LabVIEW to download an FPGA VI by right-clicking the FPGA VI in the


 Project Explorer window and selecting


 Download from the shortcut menu. Refer to the specific


 FPGA target hardware documentation for information about downloading


 options available for the target.

You also can have LabVIEW programmatically download an FPGA VI or bitfile to an FPGA


 target from a host VI.

Complete the following steps to programmatically download an FPGA VI or bitfile.

1. Open a reference to the FPGA VI or bitfile. Note The


 FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you


 want to open a reference to an FPGA VI. The host VI does not need to be in a


 project if you open a reference to a bitfile.
2. Add an Invoke Method function to the block diagram.
3. Wire the FPGA VI Reference Out parameter of the Open FPGA


 VI Reference function to the FPGA VI Reference In 


 parameter of the Invoke Method function.
4. Right-click the Invoke Method function and select


 Method»Download from the shortcut menu.

If you programmatically download the FPGA VI to the FPGA target with the Invoke


 Method function, you also must programmatically run the FPGA VI on the FPGA target


 with the Invoke Method function. Add another Invoke Method function to the block


 diagram and select Method»Run from the shortcut menu of the


 Invoke Method function to programmatically run an FPGA VI or bitfile.

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=downloading-an-fpga-vi-to-the-flash-memory-of-an-fpga-target-fpga-module.html language=enus -->
## TOPIC 00077: Downloading an FPGA VI to the Flash Memory of an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `downloading-an-fpga-vi-to-the-flash-memory-of-an-fpga-target-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/downloading-an-fpga-vi-to-the-flash-memory-of-an-fpga-target-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can store FPGA VIs on the flash memory of certain FPGA targets. Refer to the specific FPGA target hardware documentation for information about flash memory on the FPGA target. Complete the following steps to download a VI to flash memory on the FPGA target. Create a new project or open an existi

### Downloading an FPGA VI to the Flash Memory of
 an FPGA Target

You can store FPGA VIs on the flash memory of certain FPGA targets. Refer to the specific FPGA
 target hardware documentation for information about flash memory on the FPGA
 target.

Complete the following steps to download a VI to flash memory on the FPGA target.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target in the Project


 Explorer window and select RIO Device Setup 


 from the shortcut menu. The RIO Device Setup dialog box


 appears. Note You can click the Help


 button in the RIO Device Setup dialog box to display


 the RIO Device Setup Help.
4. Browse or type the path to the bitfile you want to download to flash memory in


 the Bitfile to Download path control.
5. Click the Download Bitfile button.
6. On the Device Settings tab, select Autoload VI


 on device power-up or Autoload VI on device


 reboot .
7. Click the Apply Settings button.
8. Click the Exit button.

Note

Run when loaded to FPGA

Run when loaded to FPGA

#### Alternative Ways to Download the VI to Flash Memory for CompactRIO


 Targets

You also can use the following methods to download an FPGA VI to the flash memory of


 CompactRIO targets.

- Complete the following steps to download the VI to flash memory without using


 the RIO Device Setup dialog box.
  1. Right-click the


 VI you want to download to flash memory and select Download


 VI to Flash Memory from the shortcut menu. The


 Confirm Downloading VI to Flash dialog box


 appears.
  2. Click the Yes button to download


 the VI to flash memory.
- Complete the following steps to download the VI to flash memory through the


 Start menu.
  1. Navigate to the NI-RIO\RIO


 Device Setup directory to display the RIO Device


 Setup dialog box.
  2. Select the FPGA target to


 which you want to download a bitfile from the


 Resource pull-down menu.
  3. Browse or


 type the path to the bitfile you want to download to the flash memory on


 the FPGA device in the Bitfile to Download path


 control.
  4. Click the Download Bitfile 


 button.
  5. On the Device Settings tab,


 select Autoload VI on device power-up or


 Autoload VI on device reboot .
  6. Click


 the Apply Settings button.
  7. Click the


 Exit button.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Adding FPGA Targets to a LabVIEW Project
- Running FPGA VIs Automatically from Flash Memory

<!--NI_TOPIC bundle=labview-fpga-module path=dsp48e-example-creating-a-complex-multiplier-fpga-module.html language=enus -->
## TOPIC 00078: DSP48E Example: Creating a Complex Multiplier

- bundle_id: `labview-fpga-module`
- source_path: `dsp48e-example-creating-a-complex-multiplier-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/dsp48e-example-creating-a-complex-multiplier-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use four DSP48E slices to implement a complex multiplier. The inputs to this multiplier are four fixed-point numbers (x1, x2, y1, and y2), each pair of which represents a complex number: x1 + j * y1 x2 + j * y2 The complex multiplier takes these inputs and produces two fixed-point numbers: x

### DSP48E Example: Creating a Complex Multiplier

You can use four DSP48E slices to implement a complex multiplier. The inputs to this


 multiplier are four fixed-point numbers (x1,


 x2, y1, and y2), each pair


 of which represents a complex number:

- x 1 + j * y 1
- x 2 + j * y 2

The complex multiplier takes these inputs and produces two fixed-point numbers:

- x 1 * x 2 – y 1 *


 y 2
- x 1 * y 2 + x 2 *


 y 1

You then can calculate (x1 * x2 –


 y1* y2) +


 j(x1 * y2 +


 x2 * y1).

Complete the following steps to create a complex multiplier.

1. Create a new, blank VI on a supported FPGA target.
2. Add a DSP48E function to the block diagram.
3. Double-click this function and configure it in the following ways:


 This function is now Function 0.
  1. Function page: [IMAGE alt='image' src='GUID-281CE2DD-E48E-4162-85B7-DD21A2F42874-a5.png']
  2. Terminals 


 page: [IMAGE alt='image' src='GUID-CF4D5C36-3584-4CC7-BB0C-AF6D6D5EFAA2-a5.png']
  3. Click the


 OK button to save changes and return to the


 block diagram.
4. Press the <Ctrl> key and drag the function below the current one. This


 action creates a copy of the DSP48E function, Function 1. The copy has the same


 configuration as the original. The block diagram now resembles the following


 figure: [IMAGE alt='image' src='GUID-343C8FFB-C840-41BB-A33F-85987CFE790C-a5.png']
5. Add another DSP48E function to the right of Function 0. This new function will


 be Function 2.
6. Double-click this function and configure it in the following ways:
  1. Function page: [IMAGE alt='image' src='GUID-71BEA9C1-D5BA-4A85-A16D-6C8DB79F97DA-a5.png']
  2. Terminals 


 page: [IMAGE alt='image' src='GUID-1A91A6B2-B37D-41AE-A5A6-A7B7B2849335-a5.png']
  3. Registers 


 page: [IMAGE alt='image' src='GUID-646D0019-3812-4979-8288-3B83808F3873-a5.png'] Adding an extra register to each data path ensures the latencies are balanced in this


 application.
  4. Click the OK button to save


 changes and return to the block diagram.
7. Press the <Ctrl> key and drag this function to the right of Function 1,


 below Function 2.
8. Double-click this new copy and configure the Function 


 page in the following way: [IMAGE alt='image' src='GUID-F321894B-2D54-4960-BB95-BF3ED6C32413-a5.png']
9. Click the OK button to save changes and return to the


 block diagram, which now resembles the following figure: [IMAGE alt='image' src='GUID-B9326099-BD43-410B-AF9C-37896C84D604-a5.png']
10. Create and wire the controls and indicators as shown in the following figure:


 [IMAGE alt='image' src='GUID-BA0284C9-7BB0-4C43-BD2C-DFE188CF7709-a5.png'] Note Depending on the sources of


 data for x1, x2,


 y1, and y2, you might need to configure the integer word lengths of the DSP48E input


 terminals.
11. Save the VI to a convenient location as DSP48E Complex


 Multiplier.vi .

You now can export this VI for simulation. To run this VI on an FPGA target, you must


 enclose the code in a single-cycle Timed


 Loop.

|  | Tip You can shrink the functions' icons to save space on the block diagram. |
| --- | --- |

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- Configuring DSP48E and DSP48E1 Functions
- Determining the Maximum Number of DSP48E or DSP48E1 Functions You Can Use
- Shrinking the DSP48E or DSP48E1 Function Icon

<!--NI_TOPIC bundle=labview-fpga-module path=dsp48e-example-creating-an-n-tap-fir-filter-fpga-module.html language=enus -->
## TOPIC 00079: DSP48E Example: Creating an n-Tap FIR Filter

- bundle_id: `labview-fpga-module`
- source_path: `dsp48e-example-creating-an-n-tap-fir-filter-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/dsp48e-example-creating-an-n-tap-fir-filter-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create an n-tap FIR filter by using n DSP48E functions. Each function processes one coefficient, or tap, of the FIR filter, where h[0..n–1] represents the n coefficients of the FIR filter. Complete the following steps to create a 3-tap FIR filter. Create a new, blank VI on a supported FPGA t

### DSP48E Example: Creating an n-Tap FIR Filter

You can create an n-tap FIR filter by using n


 DSP48E functions. Each function processes one coefficient, or tap, of the FIR


 filter, where h[0..n–1] represents the


 n coefficients of the FIR filter. Complete the following


 steps to create a 3-tap FIR filter.

1. Create a new, blank VI on a supported FPGA target.
2. Add a DSP48E function to the block diagram.
3. Double-click this function and configure it in the following ways:
  1. Function page: [IMAGE alt='image' src='GUID-281CE2DD-E48E-4162-85B7-DD21A2F42874-a5.png']
  2. Terminals 


 page: [IMAGE alt='image' src='GUID-CF4D5C36-3584-4CC7-BB0C-AF6D6D5EFAA2-a5.png']
  3. Click the


 OK button to save changes and return to the


 block diagram.
4. Add another DSP48E function to the block diagram. Configure this function in the


 following ways:
  1. Function page: [IMAGE alt='image' src='GUID-F321894B-2D54-4960-BB95-BF3ED6C32413-a5.png']
  2. Terminals 


 page: [IMAGE alt='image' src='GUID-F153C213-D870-4213-9D35-45EC019669F5-a5.png']
  3. Click the


 OK button to save changes and return to the


 block diagram.
5. Press the <Ctrl> key and drag this node to create a copy on the block


 diagram. Repeat this step until there are a total of n DSP48E


 functions on the block diagram. In this example for a three-tap filter, there


 are three DSP48E functions on the block diagram.
6. Double-click the n th function, click the


 Terminals tab, and remove the checkmark from the


 pcout checkbox.
7. Click the OK button to save changes and return to the


 block diagram. [IMAGE alt='image' src='GUID-70B558F2-F7BE-445A-A35B-8A701A2F0B68-a5.png']
8. Wire the functions and terminals together.
  1. Wire the data to filter to


 the a input of each DSP48E function. Depending on


 the source for this input, you might need to adjust the integer word length of the


 a input.
  2. Wire each individual filter


 coefficient to the b input of each successive


 DSP48E function. You might need to scale values you wire to these


 terminals.
  3. Wire each pcout output


 terminal to the pcin input terminal of the next


 DSP48E function.
  4. The p output terminal of


 the last DSP48E function returns the filtered data. Either create an


 indicator for this function or wire it to another


 function.
9. The block diagram now resembles the following figure: [IMAGE alt='image' src='GUID-B45A8411-B0C7-41EC-9C08-306860854CDE-a5.png']
10. Save the VI to a convenient location as DSP48E FIR


 Filter.vi .

In the previous figure, the a input of each function processes


 the data you want to filter. The b input processes the filter


 coefficients h[0] through


 h[n–1] for a total of n


 coefficients, one for each DSP48E function.

Tip

n

- Large arrays consume significant space on an


 FPGA. Therefore, NI recommends using other methods to store the


 coefficients, such as memory items. You also can use the Discrete


 Delay function to store multiple coefficients for a series of


 clock cycles.
- The block diagram will have a lot of DSP48E icons on the block diagram. You


 can shrink these icons to reduce the amount of space each icon uses.

You now can export this VI for simulation. To run this VI on an FPGA target, you must


 enclose the code in a single-cycle Timed


 Loop.

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- Configuring DSP48E and DSP48E1 Functions
- Shrinking the DSP48E or DSP48E1 Function Icon

<!--NI_TOPIC bundle=labview-fpga-module path=estimating-fpga-resource-usage-without-compiling-fpga-module.html language=enus -->
## TOPIC 00080: Estimating FPGA Resource Usage without Compiling

- bundle_id: `labview-fpga-module`
- source_path: `estimating-fpga-resource-usage-without-compiling-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/estimating-fpga-resource-usage-without-compiling-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For some FPGA target families, such as the Virtex-5, you can estimate how many resources your FPGA VI uses without compiling the FPGA VI. LabVIEW uses a Xilinx tool to estimate the number of slices, LUTs, and flip-flops that FPGA VI will use. Estimating resources before compiling allows you to decid

### Estimating FPGA Resource Usage without
 Compiling

For some FPGA target families, such as the Virtex-5, you can estimate how many


 resources your FPGA VI uses without compiling the FPGA VI. LabVIEW uses a Xilinx


 tool to estimate the number of slices, LUTs, and flip-flops that FPGA VI will use.


 Estimating resources before compiling allows you to decide if your FPGA design is


 close to fitting on the FPGA without waiting minutes to hours for the compilation to


 complete.

Note

Complete the following steps to estimate the FPGA resource usage for an FPGA


 application.

1. Right-click an FPGA build specification and select Estimate Resource


 Usage from the shortcut menu to begin the resource estimation


 process. If the Estimate Resource Usage menu item is not


 available, the target does not support this feature.
2. Follow the status of the process in the Compilation Status window.
3. When the report is ready, select Estimated device utilization


 (pre-synthesis) from the Reports 


 pull-down menu to display the report.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Reports Available from the Compilation Status Window
- Working with FPGA Build Specifications

<!--NI_TOPIC bundle=labview-fpga-module path=example-simulation-configurations-fpga-module.html language=enus -->
## TOPIC 00081: Example Simulation Configurations

- bundle_id: `labview-fpga-module`
- source_path: `example-simulation-configurations-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/example-simulation-configurations-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections provide examples of adding synthesis files and configuring simulation behavior. One .vhd Synthesis File You also Use for Simulation Complete the following steps to add a .vhd file and use that same file for simulation. Add an IP Integration Node to the block diagram. Double-cl

### Example Simulation Configurations

The following sections provide examples of adding synthesis


 files and configuring simulation


 behavior.

#### One .vhd Synthesis File You also Use for Simulation

Complete the following steps to add a .vhd file and use that same


 file for simulation.

1. Add an IP Integration Node to the block diagram.
2. Double-click the node to launch its configuration dialog box.
3. On the first page, click the Add Synthesis File 


 button.
4. Choose the .vhd file and click the OK 


 button. This file appears in the Synthesis File column of


 the table. Notice that the Simulation Behavior is


 Same as synthesis , which means LabVIEW uses the


 .vhd synthesis file for simulation also.

You now can continue configuring the IP Integration Node.

#### One Netlist Synthesis File with Several .vhd Files for Simulation

Complete the following steps to add a netlist file and then use multiple


 .vhd files for simulation.

1. Add an IP Integration Node to the block diagram.
2. Double-click the node to launch its configuration dialog box.
3. On the first page, click the Add Synthesis File 


 button.
4. Choose the netlist file and click the OK button. This


 file appears in the Synthesis File column of the


 table.
5. Click the Set Simulation Behavior button to launch the


 Set Simulation Behavior dialog box.
6. Select the User-defined option.
7. Use the buttons to the right of the file list to add .vhd files


 that define the simulation. Be sure to set the top-level simulation file as


 appropriate.

You now can continue configuring the IP Integration Node.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=example-vhdl-code-for-clip-clocks-fpga-module.html language=enus -->
## TOPIC 00082: Example VHDL Code for CLIP Clocks

- bundle_id: `labview-fpga-module`
- source_path: `example-vhdl-code-for-clip-clocks-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/example-vhdl-code-for-clip-clocks-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use component-level IP (CLIP) clocks in FPGA VIs. The following code is an example of how to derive clocks using Xilinx DCMs inside CLIP and use features such as phase shifting. The code also shows how to lock and reset a DCM and to use a BUFGCE for clocks that might stop. If you want to

### Example VHDL Code for CLIP Clocks

You can use component-level IP (CLIP) clocks in FPGA VIs. The following code is


 an example of how to derive clocks using Xilinx DCMs inside CLIP and use features


 such as phase shifting. The code also shows how to lock and reset a DCM and to use a


 BUFGCE for clocks that might stop.

Tip

ClipGenerateClks.vhd

ClipGenerateClks.vhd

```text
------------------------------------------------------------------------------- 
-- 
-- File: ClipGenerateClks.vhd 
-- Author: National Instruments Corporation 
-- Date: April 2009 
-- 
------------------------------------------------------------------------------- 
-- 
-- Purpose: 
-- 
-- This CLIP component generates clocks using a Xilinx DCM. A 40 Mhz clock is 
-- used to derive an 80 Mhz clock, and a phase shifted version of 80Mhz clock 
-- that is shifted by 180 degrees. 
-- 
-- This example illustrates to use other Xilinx DCM features 
-- such as phase shifting. 
-- 
-- Signal naming convention: 
-- 
-- All asynchronous signals are pre-fixed with a. 
-- All Clk40 synchronous signals are pre-fixed with c40. 
-- All Clk80FromDcm0 synchronous signals are pre-fixed with c80. 
-- All metastable signals are suffixed with _ms. 
-- 
-- Ports: 
-- 
-- aDiagramReset : This is the LabVIEW FPGA asynchronous diagram reset. 
-- 
-- Clk40 : This is the LabVIEW FPGA generated 40 Mhz clock. This 
-- clock is stable and free-running only when aDiagramReset 
-- is low. 
-- 
-- ClkOut80 : This is an 80 Mhz clock generated from Xilinx DCM. 
-- 
-- ClkOut80P180 : This is an 80 Mhz clock phase shifted by 180 degrees 
-- generated by Xilinx DCM. 
-- 
------------------------------------------------------------------------------- 

library ieee; 
  use ieee.std_logic_1164.all; 
  use ieee.numeric_std.all; 

entity ClipGenerateClks is 
  port ( 
    aDiagramReset : in std_logic; 
    Clk40 : in std_logic; 
    ClkOut80 : out std_logic; 
    ClkOut80P180 : out std_logic 
  ); 
end ClipGenerateClks; 

architecture rtl of ClipGenerateClks is 

  -- BUFG component declaration 
  component BUFG 
    port ( 
       I : in std_logic; 
       O : out std_logic); 
  end component; 

  -- BUFGCE component declaration 
  component BUFGCE 
    port ( 
       I : in std_logic; 
       CE : in std_logic; 
       O : out std_logic); 
  end component; 

  -- DCM component declaration 
  component DCM 
    generic ( 
       CLKIN_PERIOD : real; 
       CLK_FEEDBACK : string; 
       CLKDV_DIVIDE : real; 
       CLKFX_DIVIDE : integer; 
       CLKFX_MULTIPLY : integer; 
       CLKIN_DIVIDE_BY_2 : boolean; 
       CLKOUT_PHASE_SHIFT : string; 
       DESKEW_ADJUST : string; 
       DFS_FREQUENCY_MODE : string; 
       DLL_FREQUENCY_MODE : string; 
       DSS_MODE : string; 
       DUTY_CYCLE_CORRECTION : Boolean; 
       PHASE_SHIFT : integer; 
       STARTUP_WAIT : boolean 
    ); 
    port ( 
       CLKIN, CLKFB, RST, DSSEN, PSINCDEC, PSEN, PSCLK : in std_logic; 
       CLK0, CLK90, CLK180, CLK270, 
       CLK2X, CLK2X180, CLKDV, CLKFX, CLKFX180 : out std_logic; 
       LOCKED : out std_logic; 
       STATUS : out std_logic_vector(7 downto 0); 
       PSDONE : out std_logic 
    ); 
  end component; 

  constant kDcmResetDuration : positive := 3; 
  signal c40ResetToDcm0_ms : std_logic := '1'; 
  signal c40ResetToDcm0 : std_logic_vector(kDcmResetDuration downto 1) := (others => '1'); 
  signal Clk0FromDcm0, ClkFbToDcm0 : std_logic; 
  signal Clk80FromDcm0, Clk80P180FromDcm0, Clk80ThruBufg : std_logic; 
  signal aLockedFromDcm0 : std_logic; 
  signal c80Locked_ms, c80Locked : std_logic := '0'; 

begin 

  -- Dcm0RstShiftReg ---------------------------------------------------------- 
  -- This shift register makes sure that when the DCM reset asserts, it 
  -- remains asserted for at least three clock cycles of DCM CLKIN. This 
  -- is required for correct DCM locking sequence. Refer to the Xilinx FPGA 
  -- user guide for more information. 
  -- 
  -- The DCM should be reset when aDiagramReset asserts. This is important 
  -- because some LabVIEW FPGA generated clocks (base or derived clocks) may 
  -- not be valid when aDiagramReset is asserted. All LabVIEW FPGA clocks 
  -- (in this case Clk40) are guaranteed to be stable and free-running 
  -- immediately following the de-assertion of aDiagramReset. 
  -- However, if externally generated clocks are used to source the DCM, other 
  -- reset schemes would have to be used so that the DCM is kept in reset until 
  -- the external clock is stable and free-running. 
  ----------------------------------------------------------------------------- 
  Dcm0RstShiftReg : process (aDiagramReset, Clk40) 
  begin 
    if aDiagramReset = '1' then 
       c40ResetToDcm0_ms <= '1'; 
       c40ResetToDcm0 <= (others => '1'); 
    elsif rising_edge(Clk40) then 
       c40ResetToDcm0_ms <= '0'; 
       c40ResetToDcm0(1) <= c40ResetToDcm0_ms; 
       for i in 1 to kDcmResetDuration-1 loop 
           c40ResetToDcm0(i+1) <= c40ResetToDcm0(i); 
       end loop; 
    end if; 
  end process Dcm0RstShiftReg; 
  -- DCM0: -------------------------------------------------------------------- 
  -- This DCM generates a 80 Mhz and a phase shifted version of the 80 Mhz 
  -- clock shifted by 180 degrees. 
  ----------------------------------------------------------------------------- 
  DCM0: DCM 
    generic map( 
       CLKIN_PERIOD => 25.0, 
       CLK_FEEDBACK => "1X", 
       CLKDV_DIVIDE => 2.0, 
       CLKFX_DIVIDE => 1, 
       CLKFX_MULTIPLY => 4, 
       CLKIN_DIVIDE_BY_2 => FALSE, 
       CLKOUT_PHASE_SHIFT => "NONE", 
       DESKEW_ADJUST => "SYSTEM_SYNCHRONOUS", 
       DFS_FREQUENCY_MODE => "LOW", 
       DLL_FREQUENCY_MODE => "LOW", 
       DSS_MODE => "NONE", 
       DUTY_CYCLE_CORRECTION => TRUE, 
       PHASE_SHIFT => 0, 
       STARTUP_WAIT => FALSE 
    ) 
    port map ( 
       RST => c40ResetToDcm0(kDcmResetDuration), 
       CLKIN => Clk40, 
       CLKFB => ClkFbToDcm0, 
       CLK0 =>Clk0FromDcm0, 
       CLK180 =>OPEN, 
       CLK270 =>OPEN, 
       CLK2X =>Clk80FromDcm0, 
       CLK2X180 =>Clk80P180FromDcm0, 
       CLK90 =>OPEN, 
       CLKDV =>OPEN, 
       CLKFX =>OPEN, 
       CLKFX180 =>OPEN, 
       DSSEN =>'0', 
       PSCLK =>'0', 
       PSEN =>'0', 
       PSINCDEC =>'0', 
       LOCKED =>aLockedFromDcm0, 
       PSDONE =>OPEN, 
       STATUS =>OPEN); 
  -- BufgClkFbofDcm0: --------------------------------------------------------- 
  -- This BUFG is used to drive the feedback clock input of DCM0. 
  ----------------------------------------------------------------------------- 
  BufgClkFbofDcm0: BUFG 
    port map ( 
       I =>Clk0FromDcm0, 
       O =>ClkFbToDcm0); 
  -- BufgClk80: --------------------------------------------------------------- 
  -- This BUFG is used to drive the clock used by the synchronizer on locked 
  -- signal from DCM0. 
  ----------------------------------------------------------------------------- 
  BufgClk80: BUFG 
    port map ( 
       I => Clk80FromDcm0, 
       O => Clk80ThruBufg); 
  -- DblSyncLocked: ----------------------------------------------------------- 
  -- This double synchronizer synchronizes the asynchronous locked signal from 
  -- DCM0 to the Clk80FromDcm0 clock domain. This signal will be used to drive 
  -- the CE pin of the BUFGCE. This is because CE must not change during a short 
  -- setup window just prior to the rising clock edge on the BUFGCE input I. 
  -- Violating this setup time requirement can result in glitchy output pulse. 
  -- Refer to the Xilinx FPGA user guide for more information. 
  -- 
  -- However, when aDiagramReset asserts, c80Locked could violate the setup 
  -- time requirement of Clk80FromDcm0, and it could result in a glitchy output 
  -- pulse at output O of BUFGCE. This glitch is acceptable because the FPGA VI 
  -- will be in an asynchronous reset. However, if this clock is being used for 
  -- other circuitry not reset by aDiagramReset, that circuitry should be 
  -- disabled before this reset asserts. 
  ----------------------------------------------------------------------------- 
  DblSyncLocked : process (aDiagramReset, Clk80ThruBufg) 
  begin 
    if aDiagramReset = '1' then 
       c80Locked_ms <= '0'; 
       c80Locked <= '0'; 
    elsif rising_edge(Clk80ThruBufg) then 
       c80Locked_ms <= aLockedFromDcm0; 
       c80Locked <= c80Locked_ms; 
    end if; 
  end process DblSyncLocked; 

  -- BufgceClk80: ------------------------------------------------------------- 
  -- This BUFGCE remains disabled until DCM0 achieves lock. This ensures that 
  -- the global clock network is driven only when the 80 Mhz derived clock is 
  -- valid and glitch free. 
  -----------------------------------------------------------------------------
  BufgceClk80: BUFGCE 
    port map ( 
       I =>Clk80FromDcm0, 
       CE =>c80Locked, 
       O =>ClkOut80); 

  -- BufgceClk80P180: --------------------------------------------------------- 
  -- This BUFGCE remains disabled until DCM0 achieves lock. This ensures that 
  -- the global clock network is driven only when the phase shifted 80 Mhz 
  -- derived clock is valid and glitch free. 
  ----------------------------------------------------------------------------- 
  BufgceClk80P180: BUFGCE 
    port map ( 
       I =>Clk80P180FromDcm0, 
       CE =>c80Locked, 
       O =>ClkOut80P180); 

end rtl;
```

Parent topic:

Using CLIP Clocks

Related concepts:

- Using CLIP Clocks

<!--NI_TOPIC bundle=labview-fpga-module path=excluding-a-synthesis-file-from-simulation-fpga-module.html language=enus -->
## TOPIC 00083: Excluding a Synthesis File from Simulation

- bundle_id: `labview-fpga-module`
- source_path: `excluding-a-synthesis-file-from-simulation-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/excluding-a-synthesis-file-from-simulation-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you do not need to simulate a synthesis file, or if another simulation model already includes the simulation model of a synthesis file, you can exclude that file from simulation. Excluding a file reduces the chance of errors occurring during simulation. Even if you do not plan to export an FPGA

### Excluding a Synthesis File from
 Simulation

If you do not need to simulate a synthesis file, or if another simulation model


 already includes the simulation model of a synthesis file, you can exclude that file


 from simulation. Excluding a file reduces the chance of errors occurring during


 simulation.

Note

Complete the following steps to exclude a synthesis file from simulation.

1. Select one or more synthesis files in the IP Source 


 table.
2. Click the Set Simulation Behavior button: [IMAGE alt='image' src='GUID-0D693026-8BFD-4943-B732-094A74B2FC44-a5.png'] LabVIEW displays the Set Simulation


 Behavior dialog box.
3. Select the Exclude from simulation model option:


 [IMAGE alt='image' src='GUID-E0B73DED-6599-4433-8DB4-1D936539782A-a5.png']
4. Click the OK button to return to the configuration


 wizard.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=executing-code-in-single-cycle-timed-loops-fpga-module.html language=enus -->
## TOPIC 00084: Executing Code in Single-Cycle Timed Loops

- bundle_id: `labview-fpga-module`
- source_path: `executing-code-in-single-cycle-timed-loops-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/executing-code-in-single-cycle-timed-loops-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the single-cycle Timed Loop in FPGA VIs to optimize your code, implement multiple clock domains, and execute code in one clock cycle of the default FPGA target clock or at a rate you specify. When you place code inside a single-cycle Timed Loop, LabVIEW does not place enable chain regist

### Executing Code in Single-Cycle Timed Loops

You can use the single-cycle Timed Loop in FPGA VIs to optimize your code, implement multiple clock domains, and execute code in one clock cycle of


 the default FPGA target clock or at a rate you specify.

When you place code inside a single-cycle Timed Loop, LabVIEW does not place enable chain registers in the compiled function code. This increases the


 combinatorial path length of the code and may cause timing violation errors when you compile the FPGA VI.

Note

As the longest path through the logic inside the single-cycle Timed Loop increases,


 the maximum clock rate decreases. You can pipeline long combinatorial paths to keep the final maximum clock rate


 high. You also can separate sections of independent logic into different clock


 domains. You then can use long combinatorial paths in a slow clock domain and short


 combinatorial paths in a fast clock domain.

Parent topic:

Creating FPGA VIs

Related concepts:

- Using Single-Cycle Timed Loops to Optimize FPGA VIs
- Implementing Multiple Clock Domains
- Changing the Top-Level FPGA Target Clock Rate
- Dataflow and the Enable Chain in FPGA VIs
- Reducing Combinatorial Paths in FPGA VIs
- Optimizing FPGA VIs Using Pipelining

<!--NI_TOPIC bundle=labview-fpga-module path=executing-ip-faster-than-the-containing-single-cycle-timed-loop-fpga-module.html language=enus -->
## TOPIC 00085: Executing IP Faster than the Containing Single-Cycle Timed Loop

- bundle_id: `labview-fpga-module`
- source_path: `executing-ip-faster-than-the-containing-single-cycle-timed-loop-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/executing-ip-faster-than-the-containing-single-cycle-timed-loop-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the IP Integration Node to integrate IP that is designed to execute faster than the single-cycle Timed Loop that contains the node. In this situation, the IP must use an FPGA-derived clock that executes at a rate that is an integer multiple of the clock signal you wire to the single-cycl

### Executing IP Faster than the Containing
 Single-Cycle Timed Loop

You can use the IP Integration Node to integrate IP that is designed to



 execute faster than the single-cycle Timed



 Loop that contains the node. In this situation, the IP must use an FPGA-derived clock that executes at a rate that is an



 integer multiple of the clock signal you wire to the single-cycle Timed Loop. For



 example, if a single-cycle Timed Loop clock runs at 100 MHz, you can integrate IP



 that runs at 100 MHz, 200 MHz, 300 MHz, 400 MHz, and so on.

Complete the following steps to configure the IP Integration Node to execute faster



 than the containing single-cycle Timed Loop.

1. Ensure your IP synchronizes its output ports to the rising edge of the



 single-cycle Timed Loop clock.
2. Create the FPGA-derived clock and set it to the rate



 the IP requires. The FPGA-derived clock appears as an item in the Project Explorer window. Note The



 FPGA-derived clock must be phase-aligned to the single-cycle Timed Loop



 clock. The Message field in the FPGA Derived Clock Properties dialog box



 displays a warning if phase alignment is not possible. Phase alignment is



 not possible when the frequency of the single-cycle Timed Loop clock is



 outside the supported frequency range for phase alignment.
3. Double-click the IP Integration Node and navigate to the Clock and



 Enable Signals page.
4. In the Derived Multiple of Timed Loop Clock pull-down



 menu, specify the port in the IP that corresponds to the FPGA-derived



 clock.
5. Specify the Relative clock rate of the derived clock. For



 example, if the base clock executes at 100 MHz and the FPGA-derived clock



 executes at 400 MHz, enter 4x .
6. If the FPGA-derived clock has an enable signal, specify this signal in the



 IP Enable Signal(s) list.
7. Click the Next button and the



 Finish button until you return to the block



 diagram.
8. Add an FPGA clock constant to the block diagram and select



 the FPGA-derived clock you created.
9. Wire the output of this constant to the derived clock 



 input of the IP Integration Node.

The IP Integration Node now executes faster than the SCTL that contains the node.

Parent topic:

Using the IP Integration Node

<!--NI_TOPIC bundle=labview-fpga-module path=exporting-fpga-vis-as-vivado-design-suite-projects-fpga-module.html language=enus -->
## TOPIC 00086: Exporting FPGA VIs as Vivado Design Suite Projects

- bundle_id: `labview-fpga-module`
- source_path: `exporting-fpga-vis-as-vivado-design-suite-projects-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/exporting-fpga-vis-as-vivado-design-suite-projects-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module provides an option to export an FPGA VI as a Vivado Design Suite project. This option allows you to design the exported project and compile it into a bitfile in the Vivado Design Suite. You can then run the bitfile on an FPGA target, such as a Kintex-7 FlexRIO target or a Hig

### Exporting FPGA VIs as Vivado Design Suite Projects

The LabVIEW FPGA Module provides an option to export an FPGA VI as a Vivado Design


 Suite project. This option allows you to design the exported project and compile it


 into a bitfile in the Vivado Design Suite. You can then run the bitfile on an FPGA


 target, such as a Kintex-7 FlexRIO target or a High-Speed Serial Instrument, in the


 FPGA Module. This option takes advantage of the design features provided by the


 Vivado Design Suite while making full use of NI FPGA hardware resources. The


 following sections outline the exporting process.

Note

- Not all targets support Vivado Design Suite project export.


 Refer to the specific FPGA target hardware


 documentation for information about exporting options available


 for the target.
- You must install the necessary Xilinx compilation


 tool for Vivado on the local computer to export an FPGA VI as a Vivado


 Design Suite project or open the exported project. Visit


 ni.com/info and enter the Info Code XilinxCompileTools for more information about NI hardware


 and LabVIEW versions supported by each version of Xilinx compilation tool


 for Vivado. Refer to the Xilinx


 Compilation Tools Readme for instructions on installing the


 Xilinx compilation tool for Vivado.

#### Exporting an FPGA VI

You must export an FPGA VI as a Vivado Design Suite project before you can design the


 project and compile it into a bitfile that can be deployed to an FPGA target. To


 export an FPGA VI, you first must create a build specification.

Note

UserRTL_

UserRTL_FpgaTop.vhd

UserRTL_

Complete the following steps to export an FPGA VI through the Project


 Explorer window:

1. Right-click Build Specifications in the


 Project Explorer window and select


 New»Project Export for Vivado from the shortcut menu


 to display the Project Export for Vivado Design Suite Properties dialog box. You


 also can right-click an existing build specification for the Vivado Design Suite


 project export and select Properties from the shortcut


 menu to display this dialog box.
2. Specify the build specification name and other descriptive information on the


 Information page.
3. Display the Source Files page to specify the top-level VI. FPGA VIs can have


 only one top-level VI.
4. Click OK to close the dialog box or click


 Build to begin exporting the FPGA VI. After you click


 Build , LabVIEW creates the files necessary for the


 export and places the files in the export directory that you specified in step


 2. Note If you make further changes to the FPGA VI after


 exporting it as a Vivado Design Suite project, you can integrate your


 changes to the existing project by right-clicking the Vivado Design Suite


 project under Build Specifications and selecting


 Build or


 Rebuild.

#### Designing and Compiling an Exported Project

After you export the FPGA VI as a Vivado Design Suite project, you can continue to


 design and compile the exported project in the Vivado Design Suite. You can open the


 project in the following ways:

- In the Project Explorer window, right-click the project


 under Build Specifications and select Launch


 Vivado Design Suite .
- In the Project Explorer window, right-click the project


 under Build Specifications and select


 Explore to open the export directory. Open


 LaunchVivadoDesignSuite.bat in the export directory.
- Navigate to the export directory and open


 LaunchVivadoDesignSuite.bat .

Note

-flatten_hierarchy

-keep_equivalent_registers

Project Settings»Synthesis

tcl.post

Project


 Settings»Implementation»Write Bitstream (write_bitstream)

tcl.post

Refer to the Vivado Design Suite documentation for more details about designing the


 exported project and compiling it into a bitfile.

#### Running a Bitfile Generated from the Exported Project

After you generate a bitfile for your exported project in the Vivado Design Suite,


 you must create a host VI in the FPGA Module to programmatically download or run the


 bitfile using programmatic FPGA interface communication.

#### Where to Go from Here

Refer to the device-specific examples to learn more about exporting an FPGA VI as a


 Vivado Design Suite project. To access the device-specific examples, select


 Help»Find Examples from LabVIEW to launch the


 NI Example Finder. Click the


 Browse tab to locate device-specific examples or click


 the Search tab to search all installed examples by


 keyword.

Parent topic:

Debugging FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=filtering-fpga-io-using-multiple-input-channels-fpga-module.html language=enus -->
## TOPIC 00087: Filtering FPGA I/O Using Multiple Input Channels

- bundle_id: `labview-fpga-module`
- source_path: `filtering-fpga-io-using-multiple-input-channels-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/filtering-fpga-io-using-multiple-input-channels-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the filtering VIs on the FPGA Math & Analysis palette to filter FPGA I/O. By default, the FPGA filtering VIs accept a single input channel. However, you can use the Number of channels option in the configuration dialog box of the filtering VI to configure the VI for multiple input channels. The

### Filtering FPGA I/O Using Multiple Input
 Channels

Use the filtering VIs on the FPGA Math


 & Analysis palette to filter FPGA I/O. By default, the FPGA filtering


 VIs accept a single input channel. However, you can use the Number of


 channels option in the configuration dialog box of the filtering VI


 to configure the VI for multiple input channels. The following filtering VIs support


 multiple input channels:

- Butterworth Filter
- Notch Filter
- Rational Resampler

When you configure an FPGA filtering VI for multiple input channels, you must send


 each input channel to the filter VI in succession. You can bundle the input channels


 into an array and use a For Loop to ensure that the filter VI receives each input


 channel in succession, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-51C496ED-7C70-44C5-AEC1-AD2BABFCC15C-a5.png']

In the previous block diagram, four analog input signals pass through a Butterworth


 Filter and a Notch Filter. To maximize throughput, the VI uses Feedback Nodes to create a pipeline.

Note

Some filtering VIs that support multiple channels also support handshaking with multiple channels.

Parent topic:

Using FPGA I/O

Related concepts:

- Optimizing FPGA VIs Using Pipelining
- Scheduling Timing Using Handshaking Signals

<!--NI_TOPIC bundle=labview-fpga-module path=forcing-vi-execution-at-a-specific-time-interval-fpga-module.html language=enus -->
## TOPIC 00088: Forcing VI Execution at a Specific Time Interval

- bundle_id: `labview-fpga-module`
- source_path: `forcing-vi-execution-at-a-specific-time-interval-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/forcing-vi-execution-at-a-specific-time-interval-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to force a loop in an FPGA VI to execute at a specific time interval. Add a While Loop to the block diagram. Right-click the conditional terminal of the While Loop and select either Create Constant or Create Control from the shortcut menu depending on the needs of the ap

### Forcing VI Execution at a Specific Time Interval

Complete the following steps to force a loop in an FPGA VI to execute at a specific



 time interval.

1. Add a While Loop to the block diagram.
2. Right-click the conditional terminal of the While Loop and select either



 Create Constant or Create



 Control from the shortcut menu depending on the needs of the



 application.
3. Add a Flat Sequence structure inside the While Loop.
4. Add a Loop Timer Express VI inside the Flat Sequence



 structure.
5. Configure the Loop Timer in the Configure Loop



 Timer dialog box and click the OK button.
6. Right-click the Count input terminal of the Loop Timer



 Express VI and select Create»Constant . Enter the amount



 of time you want to elapse between iterations of the While Loop.
7. Right-click the Flat Sequence structure and select Add Frame



 After from the shortcut menu.
8. Add the code you want to execute on the FPGA to the new frame of the Flat



 Sequence structure. Note The code must be able to execute in less



 time than the amount of time you specified in step 6. If the code takes



 longer than the time specified, the execution time of the code determines



 the loop rate, and overrides the loop rate you specified in step



 6.

The following block diagram illustrates how to use a Flat Sequence Structure to



 specify the timing of an FPGA VI. [IMAGE alt='image' src='GUID-DFBC7CD9-E50B-420C-AC19-C083AA716F1D-a5.png']

Parent topic:

Controlling the FPGA VI Execution Rate

<!--NI_TOPIC bundle=labview-fpga-module path=fpga-interface.html language=enus -->
## TOPIC 00089: FPGA Interface

- bundle_id: `labview-fpga-module`
- source_path: `fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: June 2014, 371107L-01 The FPGA Interface provides programming features and functions to help you communicate with VIs or bitfiles that run on National Instruments FPGA targets, such as National Instruments Reconfigurable I/O (NI-RIO) devices. The VI that runs on the FPGA target is called the FPGA VI

### FPGA Interface

June 2014, 371107L-01

The FPGA Interface provides programming features and functions to help you communicate with VIs
 or bitfiles that run on National Instruments FPGA targets, such as National
 Instruments Reconfigurable I/O (NI-RIO) devices. The VI that runs on the FPGA target
 is called the FPGA VI. The VI you use to communicate with FPGA VIs or bitfiles is
 called the host VI. The host VI can run on PCs or RT targets.

The FPGA Interface is available with FPGA target driver software. You can use the


 FPGA Interface functions in a host VI if you have an


 FPGA target and the appropriate driver software. You do not need the LabVIEW FPGA


 Module to use the FPGA Interface functions. You need the FPGA Module if you want to


 develop FPGA VIs.

Parent topic:

Using a Host VI to Communicate with the FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=fpga-memory-items-fpga-module.html language=enus -->
## TOPIC 00090: FPGA Memory Items

- bundle_id: `labview-fpga-module`
- source_path: `fpga-memory-items-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/fpga-memory-items-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The primary means of data storage in a single clock domain using an FPGA application is a memory item. The LabVIEW FPGA Module has two types of memory items: VI-defined memory items: Use VI-defined memory items along with Memory name controls to create reentrant subVIs and avoid resource conflicts.

### FPGA Memory Items

The primary means of data storage in a single clock domain using an FPGA application


 is a memory item.

The LabVIEW FPGA Module has two types of memory items:

- VI-defined memory items : Use VI-defined memory items


 along with Memory name controls to create reentrant subVIs and avoid resource


 conflicts. If you configure a VI-defined memory item in a reentrant FPGA VI,


 LabVIEW creates a separate copy of the memory item for each instance of the VI.
- Target-scoped memory items : Use target-scoped memory


 items if you want the memory item to be visible and configurable from the


 Project Explorer window. Target-scoped memory items


 are statically bound by name to a corresponding item in the project, meaning


 that updates to the project item affect all instances of the memory on the block


 diagram. Target-scoped memory items are available within any FPGA VI under the


 same target in the Project Explorer window. If you use a


 target-scoped memory item and want to send the FPGA VI to another user, you must


 send the entire project. Otherwise, the FPGA VI is broken.

Note

The following block diagram shows how you can read from and write to a memory item


 using a Memory Method Node configured for a target-scoped memory item. This VI reads


 data from memory, increments the data, and then overwrites the same memory location


 with the new data.

Note

Data

2

x2

[IMAGE alt='image' src='GUID-6E0F4ADE-12AA-407B-860E-E87CFA5A8B17-a5.png']

#### Understanding the Memory Implementation Options

Use the Memory Properties dialog box to specify how LabVIEW


 implements a memory item. Expand the Implementation pull-down


 menu to display the available memory options, as shown in the following


 illustration.

[IMAGE alt='image' src='GUID-9E312B8F-4B82-45F5-8531-05DE8A3A1B32-a5.png']

Note

Memory Properties

#### Block Memory

Block memory, also known as block random access memory, block RAM, or BRAM, is an


 internal FPGA resource for data storage. Memory items using block memory compile at


 a high clock rate relative to other types of memory items. You can configure block


 memory for read-write access or dual-port read access. You also can use a memory


 item implemented using block memory to write data in one clock domain and read the


 data from a different clock domain. In this implementation, you can use only one


 writer node and one reader node for each memory item. Block memory does not consume


 FPGA resources. Use block memory first unless you need the advantages of a different


 type of memory.

|  | Caution When you use memory items implemented using block memory in multiple clock domains, it is possible to read from and write to the same address simultaneously. However, doing so can result in reading incorrect data. |
| --- | --- |

A higher number of cycles of read latency results in an increase in internal


 pipelining, which also can increase the maximum frequency of your compiled design.


 You can specify the number of cycles of read latency for memory items implemented


 using block memory on the General page of the


 Memory Properties dialog box. Refer to the following


 table to help you determine the number of cycles of read latency for your


 design.

| Cycles of read latency | Recommendations for Use | Impact on Maximum Frequency |
| --- | --- | --- |
| 0 | Available only when implementing memory using look-up tables | No change |
| 1 | Use this setting if you require valid data quickly, but lack the FPGA resources to use look-up tables | No change |
| 2 (default) | Recommended setting for maximum frequency of most designs | Increase |
| 3 | Use this setting if you need to store a large amount of data | Increase |
|  | Tip Use this setting if a Xilinx compilation report indicates that your design uses more than one block memory primitive. |  |

#### Look-up Tables (LUTs)

Look-up tables, also known as distributed RAM, consist of logic gates hard-wired on


 the FPGA. LUTs consume FPGA resources because they can function either as FPGA


 resources or as memory. Use look-up tables in the following situations:

- When you need to access this memory in a single-cycle Timed Loop and need to


 read data from the memory item during the same cycle as the one in which you


 invoke the node
- When you have limited remaining block memory

#### Dynamic RAM (DRAM)

DRAM is a form of external memory available on some FPGA targets. DRAM provides a


 large amount of storage space. However, because DRAM is external to the FPGA, the


 application cannot receive data from DRAM in a single clock cycle. DRAM also


 requires sequential access, meaning that only one command can access the memory at a


 time. Sequential access prevents deterministic timing and might increase execution


 time, depending on how many commands are waiting to access the DRAM.

Note

When DRAM is available, use it to store large amounts of data that do not fit


 elsewhere on the FPGA. If DRAM is not available for your target, the


 Memory Properties dialog box does not list DRAM as an


 option under the Implementation pull-down menu.

Parent topic:

Storing Data on an FPGA Target

Related concepts:

- Implementing Multiple Clock Domains
- Using I/O, Clocks, Register Items, Memory Items, FIFOs, and Handshake Items in SubVIs
- Determining When to Use Reentrant or Non-Reentrant SubVIs

<!--NI_TOPIC bundle=labview-fpga-module path=fpga-target-hardware-documentation-fpga-module.html language=enus -->
## TOPIC 00091: FPGA Target Hardware Documentation

- bundle_id: `labview-fpga-module`
- source_path: `fpga-target-hardware-documentation-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/fpga-target-hardware-documentation-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Documentation contains several references to the FPGA target hardware documentation for additional target-specific information. Each FPGA target comes with additional documentation that you might find useful as you develop FPGA VIs. LabVIEW Documentation includes topics for most FPGA target.

### FPGA Target Hardware Documentation

*LabVIEW Documentation* contains several references to the FPGA target hardware
 documentation for additional target-specific information. Each FPGA target comes
 with additional documentation that you might find useful as you develop FPGA VIs.
 *LabVIEW Documentation* includes topics for most FPGA target. In
 addition, some FPGA targets provide documentation in other locations. Refer to the
 related documentation topic for each target to locate additional documentation
 resources.

Sometimes features are specific to the FPGA device family, such as Virtex-II or


 Virtex-5. Refer to Xilinx documentation for


 information about the capabilities of the FPGA.

Related concepts:

- What is the FPGA Module?
- Creating a Reference to a Peer-to-Peer Reader FIFO
- Creating a Reference to a Peer-to-Peer Writer FIFO
- Creating Peer-to-Peer Reader FIFOs
- Creating Peer-to-Peer Writer FIFOs
- Using Peer-to-Peer Streaming with FPGA Targets

<!--NI_TOPIC bundle=labview-fpga-module path=functions-that-support-the-single-precision-floating-point-data-type-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00092: Functions that Support the Single-Precision Floating-Point Data Type in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `functions-that-support-the-single-precision-floating-point-data-type-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/functions-that-support-the-single-precision-floating-point-data-type-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following functions support the single-precision floating-point data type when used in an FPGA VI. Numeric Functions Absolute Value Add Compound Arithmetic Decrement Divide Increment Machine Epsilon Multiply Negate Negative Infinity Positive Infinity Reciprocal Scale by Power of 2 SGL Numeric Co

### Functions that Support the Single-Precision
 Floating-Point Data Type in FPGA VIs

The following functions support the single-precision floating-point data type when used in an FPGA VI.

#### Numeric Functions

- Absolute Value
- Add
- Compound Arithmetic
- Decrement
- Divide
- Increment
- Machine Epsilon
- Multiply
- Negate
- Negative Infinity
- Positive Infinity
- Reciprocal
- Scale by Power of 2
- SGL Numeric Constant
- Sign
- Square
- Square Root
- Subtract

#### Math & Scientific Constants

- Base 10 Logarithm of e
- Natural Logarithm Base
- Natural Logarithm of Pi
- Natural Logarithm of 2
- Natural Logarithm of 10
- Pi
- Pi Divided by 2
- Pi Multiplied by 2
- Reciprocal of e
- Reciprocal of Pi

#### Conversion Functions

- To Byte Integer
- To Fixed-Point
- To Long Integer
- To Quad Integer
- To Single Precision Float
- To Unsigned Byte Integer
- To Unsigned Long Integer
- To Unsigned Quad Integer
- To Unsigned Word Integer
- To Word Integer

#### Comparison Functions

- Equal?
- Equal to 0?
- Greater?
- Greater Than 0?
- Greater Or Equal?
- Greater Or Equal To 0?
- In Range and Coerce
- Less?
- Less Than 0?
- Less Or Equal?
- Less Or Equal To 0?
- Max


 & Min
- Not


 Equal?
- Not Equal To 0?
- Select
- Not A Number/Path/Refnum?

#### Channel Wire Endpoints

#### Stream

- Write
- Write With Abort
- Read
- Read With Abort

#### Tag

- Write
- Write With Abort
- Read
- Read With Abort

#### Accumulator Tag

- Write
- Write With Abort
- Read
- Read With Abort

#### Lossy Stream

- Write
- Write With Abort
- Read
- Read With Abort

#### One Element Stream

- Write
- Write With Abort
- Read
- Read With Abort

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=generating-interrupts-on-the-fpga-fpga-module.html language=enus -->
## TOPIC 00093: Generating Interrupts on the FPGA

- bundle_id: `labview-fpga-module`
- source_path: `generating-interrupts-on-the-fpga-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/generating-interrupts-on-the-fpga-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some FPGA targets allow you to generate interrupts from the FPGA VI to notify the host VI of events, such as data being ready, an error occurring, or a task finishing. To determine whether a target supports interrupts, access the FPGA Target Properties dialog box and locate the Target Information se

### Generating Interrupts on the FPGA

Some FPGA targets allow you to generate interrupts from the FPGA VI to notify the host VI of
 events, such as data being ready, an error occurring, or a task finishing. To
 determine whether a target supports interrupts, access the FPGA Target
 Properties dialog box and locate the Target
 Information section of the General page.

Note

Complete the following steps to generate interrupts in an FPGA VI.

1. Add the Interrupt VI to the block diagram of the FPGA VI in


 the data flow where you want the FPGA VI to generate the interrupt for the host


 VI.
2. Right-click the IRQ Number input of the Interrupt VI and


 select Create»Constant from the shortcut menu. You also


 can create a control or wire the output of another diagram node to the Interrupt


 VI input.
3. Enter the value of the logical interrupt you want to use in the IRQ


 Number input. The value of the logical interrupt allows the host


 computer to distinguish between multiple interrupts set in the FPGA VI. If you


 set only one interrupt in the FPGA VI, you can use any logical interrupt number.
4. Right-click the Wait Until Cleared input of the Interrupt


 VI and select Create»Constant from the shortcut


 menu.
5. Set the Wait Until Cleared Boolean constant to TRUE if


 you want the Interrupt VI to wait until the host VI acknowledges the interrupt. Set the Wait


 Until Cleared Boolean constant to FALSE if you do not need the


 Interrupt VI to wait until the host VI acknowledges the interrupt.

Refer to Synchronizing FPGA VIs and Host VIs Using Interrupts for information


 about using interrupts in the FPGA Interface.

Parent topic:

Synchronizing the FPGA and the Host

<!--NI_TOPIC bundle=labview-fpga-module path=generating-the-support-files-for-an-ip-integration-node-fpga-module.html language=enus -->
## TOPIC 00094: Generating the Support Files for an IP Integration Node

- bundle_id: `labview-fpga-module`
- source_path: `generating-the-support-files-for-an-ip-integration-node-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/generating-the-support-files-for-an-ip-integration-node-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Even if you do not plan to export the FPGA VI for simulation, you must generate support files before you can completely configure and use the IP Integration Node. Complete the following steps to generate support files. On the Name and Source page of the IP Integration Node configuration wizard, ensu

### Generating the Support Files for an IP
 Integration Node

Even if you do not plan to export the FPGA VI for simulation, you must generate


 support files before you can completely configure and use the IP Integration Node.


 Complete the following steps to generate support


 files.

1. On the Name and Source page of the IP Integration Node


 configuration wizard, ensure each synthesis file has the simulation


 behavior you want.
2. Navigate to the Generics


 and Support File Generation page.
3. (Optional) If the top-level


 synthesis file is a .vhd file that contains VHDL


 generics, set the values of these generics as appropriate. Use the


 Check Syntax button to ensure the syntax you enter is


 valid.
4. (Optional) To regenerate the entire simulation model, remove the checkmark from


 the Regenerate out-of-date support files only checkbox.


 Otherwise, LabVIEW generates only the synthesis components that have changed


 since the last time you generated the simulation model.
5. Click the Generate button to generate the support


 file.

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=getting-started-with-a-compile-farm-fpga-module.html language=enus -->
## TOPIC 00095: Getting Started with a Compile Farm

- bundle_id: `labview-fpga-module`
- source_path: `getting-started-with-a-compile-farm-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/getting-started-with-a-compile-farm-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic describes how to set up and configure a compile farm. A compile farm consists of an on-site compile server and one or more on-site compile workers that multiple developers can target. The following figure and description explain how the development computer, the compile server, and the co

### Getting Started with a Compile Farm

This topic describes how to set up and configure a compile farm. A compile farm


 consists of an on-site compile server and one or more on-site compile workers that


 multiple developers can target.

The following figure and description explain how the development computer, the


 compile server, and the compile workers operate together to deploy an FPGA VI to an


 FPGA target.

[IMAGE alt='image' src='GUID-EDFC1CF1-7367-4880-87B4-FC9B9EAAD14D-a5.png']

|  | You, or other developers, create an FPGA VI on a development computer and click the Run button in LabVIEW. |
| --- | --- |
|  | LabVIEW submits the compile job to the compile server. |
|  | The compile server sends the compile job to an available compile worker, which compiles the FPGA VI. |
|  | The compile worker submits the compiled VI back to the compile server. |
|  | The compile server submits the compiled VI back to the development computer. The FPGA VI is ready to deploy to the FPGA target. |

#### Hardware and Software Requirements
 and Recommendations

NI recommends a compile farm setup with at least two computers: a compile server and
 a compile worker. The following table describes these computers and the development
 computer.

Note

#### Setting up a Compile Farm

Before proceeding, identify the computer(s) that serve each role discussed in the


 table and ensure that you connect all computers across a network. Then, complete the


 following steps to set up the compile server, each compile worker, and the


 development computer(s).

#### Setting up the Compile Server

Complete the following tasks to set up the compile server.

1. Install the FPGA Compile Farm Server on the computer you want to designate as


 the compile server. Make note of the IP address or hostname of this


 computer.
2. Log in to the compile server.
  1. From a computer on the same network as the compile server, open a Web


 browser and navigate to


 http://<computername>:3580 ,


 where <computername> is the IP address or hostname of the compile


 server you recorded earlier. The compile server displays the NI


 Web-based Monitoring & Configuration service System


 Configuration page. Use this service to monitor and


 manage compile jobs in the queue.
  2. Click Login .
  3. Enter a user name and password that has administrative access to the NI


 Web-based Configuration & Monitoring service. By default, this user


 name is admin and the password is blank. Note NI recommends securing the compile server as soon as


 possible. Refer to the Securing a Target section


 of the FPGA Compile Farm Console Help, available by clicking


 Help on the Security


 Configuration page, for information about this


 task.If you access the compile server from the compile server


 itself, you do not need to log in.
3. Configure users who can use the compile farm to compile FPGA VIs.
  1. Click the Security Configuration button .
  2. Add user names and assign them passwords by using the


 + button at the bottom of the


 Users tab. Only users listed on this tab can


 use the compile farm. Refer to the Adding and Removing


 Users section of the console help, available by clicking


 Help , for more information adding users.
  3. Assign one or more users to the administrators 


 group. Users in this group can compile FPGA VIs by using the compile


 farm, but also can manage the compile job queue, cancel compile jobs,


 show and hide compile workers, and so on. Refer to the


 Assigning Users to a Group or Removing Users from a


 Group section of the console help, available by clicking


 Help , for information about assigning users


 to the administrators group.
  4. After you finish adding users and administrators, click


 Save and close the Web browser.

#### Setting up the Compile Workers

The next step is to make the compile server aware of each compile worker. For each


 compile worker, complete the following steps:

1. Install the Xilinx compilation tools on any computer that you want to designate


 as a compile worker.
2. Configure the compile worker.
  1. Start the compile worker by selecting Start»All


 Programs»National Instruments»FPGA»FPGA Compile Worker .


 Windows displays the LabVIEW FPGA Compile Worker 


 icon in the taskbar.
  2. Double-click this icon to display the status and capabilities of the


 compile worker.
  3. Click Configure to configure the compile


 worker.
  4. Select Connect to a compile server .
  5. Enter the following information:
    - Hostname :


 <computername>:3580 ,


 where <computername> is the IP address or hostname of the


 compile server.
    - Username : admin
    - Password : The password associated with


 the admin username. By default, this password is


 blank.
  6. Enter the Number of simultaneous jobs , which is


 the number of simultaneous compile jobs this worker can handle.


 Generally, one CPU core can handle one compile job. However, NI


 recommends leaving one core free for OS tasks. For example, if you have


 a quad-core CPU, NI recommends setting Number of simultaneous


 jobs to 3 .
  7. Click OK .
3. Verify that the compile server sees each compile worker.
  1. Log in to the compile server.
  2. Click the LabVIEW FPGA Compile Farm Console 


 button .
  3. Verify that the compile workers you added appear in


 Workers list. You might have to adjust the


 filters to see the compile worker.

#### Setting up the Development Computer(s)

Configure development computers to compile FPGA VIs using the compile farm. For each


 development computer, complete the following steps:

1. Install LabVIEW, the FPGA Module, and the NI-RIO driver software.
2. Launch LabVIEW and select Tools»Options to display the


 Options dialog box.
3. Select FPGA Module from the


 Category list.
4. Locate the Compile Server section and select


 Connect to a compile server .
5. In the dialog box that appears, click the + button to add


 a server.
6. Enter <computername>:3580 , where


 <computername> is the IP address or hostname of the compile server, in the


 Host name text box and click


 OK .
7. Enter a User name and Password 


 that you configured when you set up the compile server.
8. Click Test Connection to test the connection between the


 development computer and the compile server. Fix any errors that occur.
9. Click OK .

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling an FPGA VI Remotely

<!--NI_TOPIC bundle=labview-fpga-module path=how-dma-transfers-work-fpga-module.html language=enus -->
## TOPIC 00096: How DMA Transfers Work

- bundle_id: `labview-fpga-module`
- source_path: `how-dma-transfers-work-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/how-dma-transfers-work-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A DMA channel consists of two FIFO buffers: one on the host computer and one on the FPGA target. After creating a DMA FIFO, you write block diagram code to write data to, and read data from, the appropriate buffer. For example, if you are transferring data from the FPGA to the host, you write code o

### How DMA Transfers Work

A DMA channel consists of two FIFO buffers: one on the


 host computer and one on the FPGA target. After creating a DMA FIFO, you write block


 diagram code to write data to, and read data from, the appropriate buffer. For


 example, if you are transferring data from the FPGA to the host, you write code on


 the FPGA that writes data to the buffer. You also write code on the host that reads


 data from the buffer.

Note

Because DMA communication is based on FIFOs, data transfer occurs one element at a


 time. The first element in one buffer is the first element transferred to the other


 buffer. The following illustration shows an example of this data transfer.

[IMAGE alt='image' src='GUID-CC0F6B42-D697-47D5-B218-13A002CD8F6D-a5.png']

In the previous illustration, the FPGA VI acquires data and writes one element of


 data to the FPGA buffer of the DMA FIFO. The host VI reads four elements at a time


 from the host buffer.

Note

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Synchronizing the FPGA and the Host

<!--NI_TOPIC bundle=labview-fpga-module path=implementing-block-memory-fifos-fpga-module.html language=enus -->
## TOPIC 00097: Implementing Block Memory FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `implementing-block-memory-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/implementing-block-memory-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you implement block memory FIFOs, the actual number of elements the FIFO can hold depends on the factors outlined in this topic. Implementing FIFOs with Slice Fabric Control Logic If you implement a FIFO using block memory with the Slice Fabric control logic, the considerations in the following

### Implementing Block Memory FIFOs

When you implement block memory FIFOs, the actual number of elements the FIFO can


 hold depends on the factors outlined in this topic.

#### Implementing FIFOs with Slice Fabric Control Logic

If you implement a FIFO using block memory with the Slice


 Fabric control logic, the considerations in the following table


 apply to the actual number of elements the FIFO can hold:

| FIFO Type | Size to Specify | Considerations |
| --- | --- | --- |
| Target-scoped FIFOs | A power of two plus a small number of elements | The General page displays a size of 2^M+5, where M is the address width. LabVIEW coerces Requested Number of Elements to the closest larger value that is 2^M+5. For example, if Requested Number of Elements is 1,000, LabVIEW coerces this number to 1,029. If the FPGA does not have enough space for the coerced Requested Number of Elements, the FPGA VI fails to compile. |
| DMA FIFOs | One less than a power of two for Target to Host - DMA One less than a power of two plus six times the Number of Elements to Read for Host to Target - DMA | The General page displays a size of 2^M-1 or 2^M+(6*NumberofElementstoRead)-1, where M is the address width. LabVIEW coerces Requested Number of Elements to the closest larger valid value. If the FPGA does not have enough space for the coerced Requested Number of Elements, the FPGA VI fails to compile. You must implement DMA FIFOs using block memory with Slice Fabric control logic. Maximum DMA FIFO size varies by target. Refer to the specific FPGA target hardware documentation for more information about DMA FIFO size limitations. |
| Peer-to-peer FIFOs | One less than a power of two for writer FIFOs One less than a power of two plus six times the Number of Elements to Read for reader FIFOs | The General page displays a size of 2^M-1 or 2^M+(6*NumberofElementstoRead)-1, where M is the address width. LabVIEW coerces Requested Number of Elements to the closest larger valid value. If the FPGA does not have enough space for the coerced Requested Number of Elements, the FPGA VI fails to compile. You must implement peer-to-peer FIFOs using block memory with Slice Fabric control logic. |

#### Implementing FIFOs with Built-In Control Logic

If you implement a FIFO using block memory with the Built-In


 control logic, the following considerations apply to the actual number of elements


 the FIFO can hold:

- Enabling the handshaking interface on the Write method increases FIFO depth by


 one.
- Target-scoped FIFOs —LabVIEW coerces Requested


 Number of Elements to a depth that you can implement using the


 built-in FIFOs. The calculation for the coerced Requested Number of


 Elements varies depending on FPGA families. If the FPGA does not


 have enough space for the coerced Requested Number of


 Elements , the FPGA VI fails to compile.

Note

#### Implementing FIFOs with Target Optimal Control Logic

If you implement a FIFO using block memory with the Target


 Optimal control logic, all the considerations in this topic apply to


 the actual number of elements the FIFO can hold because target-optimal control logic


 is a combination of built-in and slice fabric control logic.

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Choosing between the FIFO Implementation Options

<!--NI_TOPIC bundle=labview-fpga-module path=implementing-fifos-using-built-in-control-logic-fpga-module.html language=enus -->
## TOPIC 00098: Implementing FIFOs Using Built-in Control Logic

- bundle_id: `labview-fpga-module`
- source_path: `implementing-fifos-using-built-in-control-logic-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/implementing-fifos-using-built-in-control-logic-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Built-in FIFO control logic, available in the block memory of some FPGA hardware targets, saves a significant amount of FPGA resources. In addition, these dedicated circuits can support higher clock rates than control logic you create using slice fabric. Refer to Xilinx documentation for information

### Implementing FIFOs Using Built-in Control Logic

Built-in FIFO control logic, available in the block memory of some FPGA hardware


 targets, saves a significant amount of FPGA resources. In addition, these dedicated


 circuits can support higher clock rates than control logic you create using slice


 fabric.

Note

#### Restrictions and Caveats for Using Built-In FIFO Control Logic

The following list outlines the restrictions and caveats for using built-in


 FIFOs.

- FPGAs must have a dedicated FIFO controller inside each block memory.
- The clock domains for built-in FIFOs must have stable and free-running clocks.
- (Xilinx Vivado) The following methods do not support FIFOs with the built-in


 control logic:
  - Get Number of Elements to Read
  - Get Number of Elements to Write
- Using the following methods increases resource usage and reduces the maximum


 frequencies of clock domains for reading and/or writing:
  - Get Number of Elements to Read
  - Get Number of Elements to Write
  - Clear
- Using the Clear method takes multiple clock cycles because it


 clears elements one by one instead of simultaneously.
- On some targets, built-in and target-optimal FIFO control logic are not


 supported in simulation exports. You can use Conditional Disable structures to implement slice-fabric FIFO


 control logic for simulation exports.
- Enabling the handshaking interface on the Write method increases FIFO depth by


 one.
- Once a built-in FIFO is completely full, you must wait until there are at least


 two empty elements before writing to the FIFO. The Get


 Number of Elements to Write method and the Write (FIFO


 Method) indicate that the FIFO is full until there are at least two


 empty elements.
- The calculation for the coerced Requested Number of


 Elements varies depending on FPGA families.

#### Optimizing FIFO Control Logic Using the Target Optimal Option

If you want to use built-in FIFOs but cannot guarantee that the application will meet


 all restrictions for using built-in FIFOs, you can configure the FIFO to use the


 optimal configuration for the situation. On the General


 page of the FIFO Properties dialog box, select Target Optimal


 from the Control Logic pull-down menu.

The Target Optimal option switches the FIFO configuration


 between Slice Fabric and Built-in


 logic depending upon the capabilities of the target and the application. The


 application uses built-in FIFOs when the target supports built-in FIFOs and the


 clock domain does not stop during reset. Otherwise, the application uses slice


 fabric to create the control logic.

Note

Target Optimal

Actual Number of


 Elements

Requested Number of Elements

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=implementing-multiple-clock-domains-fpga-module.html language=enus -->
## TOPIC 00099: Implementing Multiple Clock Domains

- bundle_id: `labview-fpga-module`
- source_path: `implementing-multiple-clock-domains-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/implementing-multiple-clock-domains-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Single-cycle Timed Loops can run under different clock domains. You can specify clock domains in FPGA VIs using the single-cycle Timed Loop. All available FPGA target clocks appear in the Project Explorer window as FPGA target base or derived clocks. You can select any FPGA target base or derived cl

### Implementing Multiple Clock Domains

Single-cycle Timed Loops can run under different clock domains. You can specify


 clock domains in FPGA VIs using the single-cycle Timed Loop. All available FPGA


 target clocks appear in the Project Explorer window as FPGA


 target base or derived clocks. You can select any FPGA target base or derived clock


 that the FPGA target supports as the timing source for a single-cycle Timed Loop.


 However, the combinatorial path length of the code you place in the single-cycle


 Timed Loop must be short enough to execute at the clock rate you specify.

#### Synchronizing I/O Under Different Clock Domains

You might need to transfer data between single-cycle Timed Loops set to run under


 different clock domains. Digital inputs on most FPGA targets are not synchronized to


 the top-level FPGA target clock and must be resynchronized. Some FPGA targets allow


 you to use external clocks or I/O resources specially synchronized to a specific


 clock. If input data is already synchronous to the top-level FPGA target clock, you


 can avoid the resynchronization overhead. Refer to the specific FPGA target hardware


 documentation for information about the synchronicity of available I/O


 resources.

#### Transferring Data between Clock Domains

To transfer data between clock domains, you can use single-cycle Timed Loop tunnels,


 register items, handshake items, local and global variables, or block memory FIFOs.


 The following table summarizes the characteristics of each method:

| Transfer Method | FPGA Resource | Lossy? | Between Parallel Loops? | Between Unlimited Domains? | Common Use |
| --- | --- | --- | --- | --- | --- |
| Single-Cycle Timed Loop Tunnels | Logic | No | No | No | Datalogging |
| Register Items and Local and Global Variables | Logic | Yes | Yes | Yes | Control, Simulation |
| Memory Items Implemented Using Block Memory | Memory | Yes | Yes | No | Datalogging |
| Block Memory FIFOs | Logic and Memory | No | Yes | No | Datalogging |
| Handshake Items | Logic | No | Yes | No | Control, Simulation |

#### Single-Cycle Timed Loop Tunnels

You can use the single-cycle Timed Loop tunnel to wire input and output signals on a


 single-cycle Timed Loop. LabVIEW handshakes input signals to the loop clock domain.


 After each iteration of the single-cycle Timed Loop terminates, LabVIEW handshakes


 any output signals to the top-level FPGA target clock. Single-cycle Timed Loop


 tunnels maintain the LabVIEW dataflow and therefore cannot be used to transfer data


 among parallel loops.

#### Register Items and Local and Global Variables

You can write to a register item or a local or global variable from only one clock


 domain. You then can read from the register item or local or global variable in as


 many clock domains as you need. LabVIEW transfers data from the writing domain to


 the reading domains and uses handshaking to avoid data corruption. You must wait


 several clock cycles of both the writing and reading domains to handshake a new


 value. Some values you write from one clock domain might not be read by the


 destination domain because of the handshaking overhead. To avoid cases where data is


 written faster than it can be read, you should program additional logic to ensure a


 two-way communication between the reader and writer, thus preventing data loss.

Note

#### Memory Items Implemented Using Block Memory

You can use a target-scoped or VI-defined memory item to store data and access it


 from a different clock domain only if you implement the memory item using block


 memory. To change the memory implementation, choose Block


 Memory as the Implementation of the memory


 item on the General page of the Memory


 Properties dialog box. In this implementation, you can use only one


 writer node and one reader node for each memory item.

|  | Caution When you use memory items implemented using block memory in multiple clock domains, it is possible to read from and write to the same address simultaneously. However, doing so can result in reading incorrect data. |
| --- | --- |

#### Block Memory FIFOs

You can use a target-scoped or VI-defined FIFO to transfer data between clock domains


 only if you implement the FIFO using block memory. To change the FIFO


 implementation, choose Block Memory as the


 Implementation of the memory item on the


 General page of the FIFO


 Properties dialog box. You can write data to a block memory FIFO


 from only one clock domain. You then can read the FIFO from only one other clock


 domain.

Note

#### Handshake Items

You can write to a handshake item from only one clock domain. You then can read from


 the handshake item in the same clock domain or a different clock domain. You can


 clear the handshake item from any clock domain. LabVIEW uses handshaking to achieve


 lossless transfer from the writing domain to the reading domain and to notify the


 writing domain when the reader receives the data. LabVIEW requires several clock


 cycles of both the writing and reading domains to handshake a new value across clock


 domains.

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Choosing between the FIFO Implementation Options
- Executing Code in Single-Cycle Timed Loops
- FPGA Memory Items
- Reducing Combinatorial Paths in FPGA VIs
- Changing the Top-Level FPGA Target Clock Rate
- Optimizing FPGA VIs Using Pipelining
- Storing and Accessing Data From Different Parts of an FPGA Design

<!--NI_TOPIC bundle=labview-fpga-module path=implementing-variable-sized-arrays-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00100: Implementing Variable-Sized Arrays in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `implementing-variable-sized-arrays-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/implementing-variable-sized-arrays-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create FPGA VIs with variable-sized arrays that resolve to a single size at compile time. When you compile an FPGA VI into a bitfile, multiple implementations of code cannot be called dynamically. This restriction means that LabVIEW must determine the size of an array input or output at comp

### Implementing Variable-Sized Arrays in FPGA VIs

You can create FPGA VIs with variable-sized arrays that resolve to a single size at


 compile time. When you compile an FPGA VI into a bitfile, multiple implementations


 of code cannot be called dynamically. This restriction means that LabVIEW must


 determine the size of an array input or output at compile time. The following table


 describes behaviors, caveats, and restrictions for implementing variable-sized


 arrays in FPGA applications.

| Array Operations | For each function that supports array inputs or outputs in the FPGA Module, LabVIEW determines the size of an array output by examining the inputs of a function. If a function includes only scalar or fixed-size array inputs, LabVIEW infers a fixed-size array output. LabVIEW returns an error if it cannot infer a fixed size. |
| --- | --- |
| Classes and Clusters | You can embed arrays that resolve to a single size at compile time in clusters and classes. |
| SubVIs | LabVIEW tracks inferred array sizes of subVIs in order to propagate them in and out of an FPGA VI. For non-reentrant subVIs, if an array size inferred through one call does not match the size of another call, LabVIEW returns an error for the front panel control along with all calls to that VI. |
| Shift Registers | Uninitialized shift registers default to an array size of zero. For initialized shift registers, LabVIEW infers the array size by examining the input terminals. If sizes of the initialized inputs do not match, LabVIEW returns an error. |
| Feedback Nodes | LabVIEW compares the array size on the input terminal of the Feedback Node to the size of the initializer terminal. If the sizes do not match, LabVIEW returns an error. For uninitialized Feedback Nodes, LabVIEW infers a size of zero for the initializer terminal. |
| Select Function | LabVIEW infers the output array size of a Select function only if both input array sizes statically resolve to the same fixed size at compile time. Otherwise, LabVIEW returns an error. |
| Case Structures | LabVIEW infers the array size of a Case structure output tunnel only if the input array sizes of all diagrams within the Case structure statically resolve to the same fixed size at compile time. Otherwise, LabVIEW returns an error. |
| For Loops | LabVIEW infers the array size of an auto-indexed output tunnel based on the number of times the For Loop executes. You must wire a constant value to the count terminal. LabVIEW returns an error if the size of the array output is not statically resolved. |
| Coercions | Wiring a variable-sized array to a fixed-size terminal where the array sizes do not match, as with subVI terminals and indicators, results in coerced data that is padded or truncated to the terminal size. When you wire a fixed-size array to a variable-sized terminal, the array size of the fixed type propagates forward. |
| Bounded Arrays | LabVIEW infers the size of bounded arrays at or below the bound. LabVIEW returns an error if the size of a bounded array cannot resolve to a single size at compile time. |
| Autopreallocate Arrays and Strings | If you select the Autopreallocate arrays and strings checkbox on the Execution page of the VI Properties dialog box, you can mix fixed-size and variable-sized arrays and LabVIEW coerces the data. |

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=improving-efficiency-when-accessing-dma-fifos-fpga-module.html language=enus -->
## TOPIC 00101: Improving Efficiency When Accessing DMA FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `improving-efficiency-when-accessing-dma-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/improving-efficiency-when-accessing-dma-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To implement traditional DMA FIFOs, LabVIEW uses multiple data copies to move data between LabVIEW and the device driver. These additional data copies consume CPU cycles and limit the size of applications that you can build using DMA FIFOs. For large, resource-intensive applications, consider using

### Improving Efficiency When Accessing DMA FIFOs

To implement traditional DMA FIFOs, LabVIEW uses multiple data copies to move data


 between LabVIEW and the device driver. These additional data copies consume CPU


 cycles and limit the size of applications that you can build using DMA FIFOs. For


 large, resource-intensive applications, consider using an external data value


 reference to avoid the data copy and reduce CPU overhead.

#### What to Use

Use the following block diagram objects to execute DMA transfers while incurring


 fewer data copies:

| Invoke Method Function |  | Case Structure |  | In Place Element Structure |  | Delete Data Value Reference |  | Merge Errors |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

#### What to Do

Create the following block diagram to execute DMA transfers while incurring fewer


 data copies. This block diagram uses the Invoke Method function configured with the


 Acquire Read Region method to acquire a region to read from the buffer, then passes


 the reference to the read region through an In Place Element structure. The subVI in


 the In Place Element structure executes application-specific code. After the subVI


 executes, the Delete Data Value Reference function releases the region on the


 buffer.

Customize the gray sections for your programming goals.

[IMAGE alt='image' src='GUID-C1DBAD3A-1BA8-417D-9E55-4A57628F4B51-a5.png']

The following list describes important details about the previous diagram:

|  | Configure an Invoke Method function. Select either the Acquire Write Region or the Acquire Read Region method, depending on the needs of your application. |
| --- | --- |
|  | Wire the reference to the read or write region to an In Place Element structure configured with Data Value Read/Write nodes. |
|  | Include code customized to meet your programming goals. |
|  | Delete the data value reference. You must delete the data value reference to make the reserved buffer region accessible again. |
|  | Ensure that the VI handles errors in the correct order using a Merge Errors function. You must handle incoming errors from the Invoke Method function before incoming errors from the In Place Element structure. |

#### Tips and Troubleshooting Information

When acquiring a region, Number of Elements and Elements in Region are not


 necessarily the same. For some targets, the number of bytes


 allocated in memory is coerced to a value that is valid for the specific target and


 is a multiple of 4096. For these targets, specify a Number of


 Elements that is a multiple of 4096 to avoid buffer wrapping. Refer


 to your target hardware documentation for more information about


 valid FIFO depths.

If the buffer is unable to acquire a region, the Invoke Method function


 returns error -61219. In most cases, this error


 results from failing to delete the data value reference that the Invoke Method


 function returns. If your application handles specific errors by code, ensure that


 you check for error -61219.

Parent topic:

Transferring Data Using Direct Memory Access

<!--NI_TOPIC bundle=labview-fpga-module path=improving-timing-performance-in-large-designs-fpga-module.html language=enus -->
## TOPIC 00102: Improving Timing Performance in Large Designs

- bundle_id: `labview-fpga-module`
- source_path: `improving-timing-performance-in-large-designs-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/improving-timing-performance-in-large-designs-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because they add an extra signal to the FPGA logic, implicit enable signals can create routing congestion and limit timing performance. For some applications, it may be appropriate to reduce routing congestion by allowing LabVIEW to remove the implicit enable signal from single-cycle Timed Loops tha

### Improving Timing Performance in Large Designs

Because they add an extra signal to the FPGA logic, implicit enable signals can create routing congestion and limit timing


 performance. For some applications, it may be appropriate to reduce routing


 congestion by allowing LabVIEW to remove the implicit enable signal from single-cycle Timed Loops that run independently of other nodes in the


 design.

#### Applications that Might Benefit from Removing Implicit Enable Signals

- High-throughput applications
- Applications with single-cycle Timed Loops that run under a fast clock and


 contain large amounts of code
- Applications that fail to compile after you add additional code, when you know


 that the additional code by itself would meet the necessary clock rate

Use the following flow chart to help determine whether your application is a


 candidate for removing implicit enable signals.

[IMAGE alt='image' src='GUID-5DFB56E2-2AEE-4A6A-8FB7-092AF62B2D90-a5.png']

#### Restricted Functionality

LabVIEW does not support the following methods and functionalities in projects in


 which implicit enable signals have been removed:

- Reset (Invoke Method)
- Close and reset
- Abort (Invoke Method)
- Re-running the VI without first re-downloading
- IP that undergoes an implicit synchronous reset before the VI begins


 execution
- IP that needs a running clock when reset is asserted
- Accessing controls, indicators, or DMA before the VI is running
- Only remove implicit enable signals when the block diagram does not contain


 logic that must execute before or after the affected loop

#### Removing Implicit Enable Signals from Qualified Loops

Complete the following steps to allow the compiler to remove the implicit enable


 signal from single-cycle Timed Loops that do not have data dependencies and are


 free-running.

1. On the Information page of the Compilation Properties dialog box, place a checkmark in the


 Allow removal of implicit enable signals inside single-cycle


 Timed Loops checkbox. Note If the


 Require removal of implicit enable signals


 checkbox does not appear, the VI is open under a target that does not


 support implicit enable removal.

#### Removing Implicit Enable Signals from All Loops

Complete the following steps to require the compiler to attempt to remove the


 implicit enable signal from single-cycle Timed Loops. Completing this procedure


 causes LabVIEW to return an error when the compiler cannot remove the implicit


 enable signal from a single-cycle Timed Loop.

1. Double-click the input node of a single-cycle Timed Loop to display the Configure Timed Loop dialog box.
2. Place a checkmark in the Require removal of implicit enable


 signals checkbox.

#### Enabling Implicit Enable Signal Removal for Individual CLIP Clocks

You must turn on the ability to remove implicit enable signals for each CLIP clock in


 your design by adding the necessary


 tags to ensure that the clock supports gating to the declaration XML


 file.

Parent topic:

Dataflow and the Enable Chain in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=install-fpga-module.html language=enus -->
## TOPIC 00103: Installing the LabVIEW FPGA Module

- bundle_id: `labview-fpga-module`
- source_path: `install-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/install-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can install the LabVIEW FPGA Module with either NI Package Manager or with the LabVIEW Platform media. Application Software Support The LabVIEW 2024 Q1 FPGA Module supports LabVIEW 2024 Q1. For information about the Application Software Support in earlier versions of the LabVIEW FPGA Module, ref

### Installing the LabVIEW FPGA Module

You can install the LabVIEW FPGA Module with either NI Package Manager or with the LabVIEW Platform
 media.

#### Application Software
 Support

The LabVIEW 2024 Q1 FPGA Module supports LabVIEW
 2024 Q1. For information about the Application Software Support in earlier versions
 of the LabVIEW FPGA Module, refer to the Readmes for those
 versions.

#### Installing the LabVIEW FPGA Module using Package
 Manager

Refer to *Package Manager* for information about installing, removing, and
 upgrading NI software using Package Manager.

#### Installing the LabVIEW FPGA Module using LabVIEW Platform Media

1. Log in as an administrator or as a user with administrative privileges.
2. Insert the LabVIEW Platform media. To request additional LabVIEW Platform media,
 refer to the NI website. If you purchased this product with an NI Software Suite
 or NI Product Bundle, use the installation media that shipped with your
 purchases to install this product.
3. Follow the instructions on the screen to install and activate the following
 software in this order: In addition to installing program files and documentation in the LabVIEW
 directory, the installer also puts files from Xilinx in the x:\NIFPGA directory,
 where x is the drive on which you installed LabVIEW. The FPGA Module uses these
 files to compile FPGA VIs into code that runs on an FPGA target.
  - LabVIEW
  - FPGA Module
  - (Optional) LabVIEW Real-Time Module—Use the LabVIEW Real-Time Module to
 program the real-time OS on NI PXI, NI PXI Express, NI CompactRIO, and
 NI Single-Board RIO devices. You have a temporary license for this
 product.
  - Xilinx Compilation Tools—Install these compilation tools on the
 development computer if you want to compile your LabVIEW FPGA VIs
 locally. You must install these tools on your development computer if
 you plan to use the Configure Component-Level IP wizard, configure the
 IP Integration Node, incorporate Xilinx IP, or use third-party
 simulation. Refer to your hardware documentation for information about
 the FPGA chip in your device and install the appropriate set of tools.
 Visit Using an Info Code and enter the Info Code
 XilinxCompileTools for more information about the
 NI hardware supported by each Xilinx compilation tool.
    - Xilinx Compilation Tools for Windows—Install these compilation
 tools if you will compile your FPGA VIs on a Windows computer.
 The recommended compilation tool for Windows is Vivado 2021.1.
 ISE Compilation tools are NOT supported on Windows 10. Note To
 configure the IP Integration Node, or use the Configure
 Component-Level IP wizard on Virtex-II devices, you also
 must install the Xilinx Compilation Tool for ISE 14.7.
 Xilinx IP and simulation exports are not supported on
 Virtex-II FPGA devices.
    - (Optional) FPGA Compile Farm Server—Use the FPGA Compile Farm
 Server to distribute FPGA VI compile jobs across multiple remote
 computers. Note Use the LabVIEW FPGA Compile Cloud Service
 to increase the development efficiency by offloading compile
 jobs to multiple computers in a cloud environment.
    - Device Driver—Device drivers contain driver software for most
 FPGA targets. Refer to your FPGA target hardware documentation
 for information about additional or different device drivers you
 need.

#### Setting Up a Remote Compile Farm Server or Compile Worker

Using an Info
 Code

XilinxCompileTools

- Windows—Visit Using an Info Code and enter the Info Code
 FPGAkb1rcs for information about setting up the FPGA
 compile farm server on a remote computer.
- Linux—Refer to the FPGA Module Xilinx Compilation Tools for Linux
 Readme for information about setting up a remote compile
 worker.

LabVIEW FPGA Compile Cloud Service

NI LabVIEW FPGA Compile Cloud Service

Related information:

- Package Manager
- Using an Info Code
- NI LabVIEW FPGA Compile Cloud Service
- FPGA Module Xilinx Compilation Tools for Linux Readme

<!--NI_TOPIC bundle=labview-fpga-module path=integrating-changes-to-the-vhdl-test-bench-fpga-module.html language=enus -->
## TOPIC 00104: Integrating Changes to the VHDL Test Bench

- bundle_id: `labview-fpga-module`
- source_path: `integrating-changes-to-the-vhdl-test-bench-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/integrating-changes-to-the-vhdl-test-bench-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: During third-party simulation, you might edit the FPGA VI and build the simulation export again. In some cases, you also must integrate corresponding changes into the VHDL test bench. When to Integrate Changes Into the Test Bench File You must integrate changes into the test bench file in the user d

### Integrating Changes to the VHDL Test Bench

During third-party simulation, you might edit the FPGA VI and build the simulation


 export again. In some cases, you also must integrate corresponding changes into the


 VHDL test bench.

#### When to Integrate Changes Into the Test Bench File

You must integrate changes into the test bench file in the user


 directory in the following cases:

- You edit properties of the FPGA target in the Project


 Explorer window.
- You change items in the Project Explorer window, such as adding, removing, or


 renaming FIFOs.
- You add or remove controls and/or indicators in the FPGA VI.

#### The File and Directory Structure for Simulation Exports

A simulation export is a collection of files necessary for simulation. You must


 access the simulation export directory to edit the test bench file. LabVIEW


 organizes the simulation export files in the following directory structure:

- Top-level destination directory—The directory you specify on the Information page of the Simulation Export Properties dialog box.
  - user —Contains the test bench file that you must edit.


 LabVIEW does not overwrite files in this directory. Note 


 If the installed third-party simulator is a Xilinx simulator, you


 must run RegenerateIsim.bat, located in the


 user directory, to regenerate the simulation


 executable after you make changes to the generated test


 bench.
  - niFpga —Contains the latest test bench template and


 other simulation files. Do not edit the files in this directory. Every


 time you build


 a simulation export, LabVIEW overwrites the files in this


 directory.
  - isim —(Xilinx Simulator) Contains the project file for a


 Xilinx Simulator. You can right-click the simulation export build


 specification in LabVIEW and select Launch


 Simulator from the shortcut menu to open the project


 file in a Xilinx Simulator.

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=integrating-third-party-ip-fpga-module.html language=enus -->
## TOPIC 00105: Integrating Third-Party IP

- bundle_id: `labview-fpga-module`
- source_path: `integrating-third-party-ip-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/integrating-third-party-ip-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to compare and choose between Component‑Level IP (CLIP) and the IP Integration Node (IPIN) for integrating third‑party IP into LabVIEW FPGA VIs, including supported formats, data types, and clocking considerations. You can integrate third-party IP into FPGA VIs using one of two methods: Co

### Integrating Third-Party IP

Learn how to compare and choose between Component‑Level IP (CLIP) and the IP
 Integration Node (IPIN) for integrating third‑party IP into LabVIEW FPGA VIs, including
 supported formats, data types, and clocking considerations.

- Component-Level IP (CLIP) interface
- IP Integration Node (IPIN)

Note

Compatibility Between Xilinx Compilation Tools and NI FPGA
 Hardware

#### Supported IP File Types

- VHDL
- Verilog
- Netlist files
- Xilinx IP configuration files:
  - Xilinx ISE ( .xco )
  - Xilinx Vivado ( .xci )

Note

#### Xilinx IP

- NI guarantees support only for Xilinx IP configuration files created with
 the current version of the Xilinx compilation tools for your FPGA
 target.
- Licensing details appear in Context Help for each IP.
 To import a license, place the .lic file into one of the
 following folders.
  - For Xilinx
 ISE: C:\NIFPGA\programs\<XilinxY_Z>\ISE\coregen\core_licenses
  - For Xilinx
 Vivado: C:\NIFPGA\programs\<VivadoA_B>\data\ip\core_licenses

For Xilinx ISE, coregen.exe installs with LabVIEW under
 C:\NIFPGA\programs\<XilinxY_Z>\ISE\bin\nt.

If
 you migrate Xilinx IP to another target or LabVIEW version, regenerate the IP for
 the new target.

Note

XilinxY_Z

VivadoA_B

#### CLIP Interface and IP Integration
 Node Details

Use [Table 1.CLIP Interface and IP
 Integration Node Comparison](integrating-third-party-ip-fpga-module.html#GUID-B195A91A-D6FA-4A89-8C69-2E48BCD24E58__TABLE_HXK_S5C_13C) to compare CLIP and IPIN at a glance. Capabilities can vary by
 FPGA target and tool version.

| Criteria | CLIP | IPIN |
| --- | --- | --- |
| Execution modes | Inside SCTL Outside SCTL | Inside SCTL |
| Simulation | Not supported | Supported |
| Third-party simulation | Supported | Supported |
| Supported LabVIEW data typesNote Top-level VHDL files support only the std_logic and std_logic_vector port types. | Boolean Boolean array Fixed-point Integer Note For Boolean array, target-dependent. Only supported by specific CLIP sockets. See target hardware documentation to determine CLIP socket support. | Boolean Boolean array Fixed-point Integer Single-precision floating-point |
| Synthesis file formats supported by Xilinx ISE | Constraints: .ucf HDL: .vhd, .v Netlists: .ngc, .edf, .edn, .ngd Xilinx IP config: .xco | Constraints: .ucf HDL: .vhd, .v Netlists: .ngc, .edf, .edn, .ngd Xilinx IP config: .xco |
| Synthesis file formats supported by Xilinx Vivado | Constraints: .xdc HDL: .vhd, .v Netlists: .dcp Xilinx IP config: .xci | Constraints: .xdc HDL: .vhd, .v Netlists: .dcp Xilinx IP config: .xci |
| Execution model | Executes parallel to, and independent of the VI dataflow | Executes as defined by the VI dataflow |
| Place of declaration | Acts as a global Declared in the LabVIEW project | Declared locally in an FPGA VI |
| Support for multiple clock domains | Maximum number of clocks defined by FPGA/target | Maximum of two clocks: Derived clock (integer multiple of SCTL) SCTL clock |
| Use IP clocks as SCTL clocks | Supported | Not supportedNote Uses the SCTL and the derived clocks of the node only. |
| VHDL generics | Supported | Supported |
| Support for constraints on IP | Target-dependent User constraints supported in CLIP ISE: .ucf Vivado: .xdc | Constraints typically encapsulated in imported core/wrapper Limited user constraints |
| Access to FPGA I/O | Supported (CLIP can expose I/O at the socket boundary) | Access via node interfaces External I/O not directly driven through IPIN |
| Best-fit scenarios | Additional clock domains Fixed-timing external interfaces Vendor HDL/netlists outside the VI diagram | Tight integration in SCTL and VI dataflow Xilinx IP cores (.xci/.xco) |

Note

std_logic

std_logic_vector

Related concepts:

- Using VHDL Code as Component-Level IP
- Using the IP Integration Node
- Integrating Xilinx IP into FPGA VIs
- Interfacing AXI IP in FPGA VIs

Related information:

- Compatibility Between Xilinx Compilation Tools and NI FPGA
 Hardware

<!--NI_TOPIC bundle=labview-fpga-module path=integrating-xilinx-ip-into-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00106: Integrating Xilinx IP into FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `integrating-xilinx-ip-into-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/integrating-xilinx-ip-into-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW uses the IP Integration Node to conveniently incorporate Xilinx IP into an FPGA VI. Complete the following steps to add Xilinx IP to an FPGA VI. Create a new, blank VI under a supported FPGA target and display the block diagram of the VI. Right-click the block diagram to select the Programmi

### Integrating Xilinx IP into FPGA VIs

LabVIEW uses the IP Integration Node to conveniently incorporate Xilinx


 IP into an FPGA VI. Complete the following steps to add Xilinx IP to an FPGA VI.

1. Create a new, blank VI under a supported FPGA target and display the block


 diagram of the VI.
2. Right-click the block diagram to select the Programming»Xilinx


 IP palette. Note This palette displays only IP


 that your FPGA device family supports. Not all FPGA device families support


 all IP. Refer to the data sheet of an IP for information about FPGA family


 support.
3. Find the IP you want and place it on the block diagram. LabVIEW creates a node


 to represent the IP.
4. Double-click the node to launch its configuration dialog box.
  1. Enter an IP Name . LabVIEW displays this name on


 the block diagram icon.
  2. Specify a Folder for Support Files . This folder


 is the location where the Xilinx IP generator places necessary files. If


 you move the FPGA VI to another computer, you must move this folder


 also.
  3. Click Configure Xilinx IP to launch the Xilinx IP


 generator.
  4. Configure the IP as necessary. Use the < Back 


 and Next > buttons to navigate through


 different options. You can click Datasheet or


 select the Documentation option, depending on


 your specific FPGA target, to view a PDF with detailed information about


 the IP.
  5. After you configure the IP, click Generate or


 OK , depending on your specific FPGA target.


 The Xilinx IP generator begins generating the VHDL code and returns you


 to LabVIEW. After the VHDL process finishes, the progress bar displays


 Generated IP successfully.
5. Click Next to proceed through the rest of the


 configuration pages. Click Finish to finish configuring


 the Xilinx IP.

Parent topic:

Integrating Third-Party IP

Related concepts:

- Integrating Third-Party IP

<!--NI_TOPIC bundle=labview-fpga-module path=interactive-front-panel-communication-fpga-module.html language=enus -->
## TOPIC 00107: Interactive Front Panel Communication

- bundle_id: `labview-fpga-module`
- source_path: `interactive-front-panel-communication-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/interactive-front-panel-communication-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use interactive front panel communication to communicate with an FPGA VI running on an FPGA target with no additional programming. With interactive front panel communication, the host computer displays the FPGA VI front panel window and the FPGA target executes the FPGA VI block diagram, as shown in

### Interactive Front Panel Communication

Use interactive front panel communication to communicate with an FPGA VI running on


 an FPGA target with no additional programming. With interactive front panel


 communication, the host computer displays the FPGA VI front panel window and the


 FPGA target executes the FPGA VI block diagram, as shown in the following


 illustration.

[IMAGE alt='image' src='GUID-E80A111A-3BA3-4237-AABC-80857EBAB35B-a5.png']

Note

The LabVIEW front panel window communicates with the FPGA target block diagram


 through the controls and indicators. You can communicate with an FPGA target


 connected directly to host computer or connected to a remote system over the


 network. As the FPGA target block diagram continues to run, the host computer


 updates values on the FPGA VI front panel window as often as possible. The execution


 rate of the FPGA VI is not affected by communication with the host computer.


 However, the front panel data you share during interactive front panel communication


 is not deterministic.

Use interactive front panel communication between the FPGA target and the host


 computer to control and test VIs running on the FPGA target. After downloading and


 running the FPGA VI, keep LabVIEW open on the host computer to display and interact


 with the front panel window of the FPGA VI.

During interactive front panel communication, you cannot use LabVIEW debugging tools,


 including probes, execution highlighting, breakpoints, and single-stepping. To


 identify errors before you compile, download, and run the FPGA VI on the FPGA


 target, consider using a test bench.

|  | Tip You cannot use interactive front panel communication while the FPGA is configured to execute on a third-party simulator. You can either use a host VI to execute the FPGA VI or change the execution mode of the FPGA target by right-clicking the FPGA target in the Project Explorer window and selecting Select Execution Mode. |
| --- | --- |

Parent topic:

Storing and Transferring Data

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Communicating with FPGA Targets from a Host Computer
- Creating a Custom VI to Simulate I/O

<!--NI_TOPIC bundle=labview-fpga-module path=interfacing-axi-ip-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00108: Interfacing AXI IP in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `interfacing-axi-ip-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/interfacing-axi-ip-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI exposes AXI, or Advanced eXtensible Interface, protocol for certain Xilinx IP on specific hardware targets. AXI protocol is an industry standard bus interface for interconnecting functional blocks of IP for high performance, high frequency applications. There are three types of AXI protocol: AXI4

### Interfacing AXI IP in FPGA VIs

NI exposes AXI, or Advanced eXtensible Interface, protocol for certain Xilinx IP on


 specific hardware targets. AXI protocol is an industry standard bus interface for


 interconnecting functional blocks of IP for high performance, high frequency


 applications. There are three types of AXI protocol: AXI4, AXI4-Lite, and


 AXI4-Stream.

Note

#### Interfacing AXI and Four-Wire IP in an FPGA VI

The AXI protocol is similar to the LabVIEW four-wire handshaking protocol in the


 signal connections. The main difference between the AXI protocol and the LabVIEW


 four-wire handshaking protocol is signal naming and placement of Feedback Nodes when


 interconnecting IP in the single-cycle Timed Loop.

AXI signals in Xilinx IP follow a general naming convention for their input and


 output terminals: m/s + protocol +


 signal name + tdata/tvalid/tready, where


 m represents the master block, or the node that produces the


 value, and s represents the slave block, or the node that


 consumes the value. For example, in the signal name


 m_axis_signal_tvalid, m represents the


 master, axis represents AXI Stream, signal


 represents the signal name, and tvalid represents valid.

AXI signals in IP created by NI follow a naming convention similar to that of Xilinx


 IP, but omit the axis term: m/s + signal name


 + tdata/tvalid/tready.

#### AXI to AXI Interconnect

The following diagram shows a conceptual configuration for the interconnection of two


 AXI4-Stream IP blocks.

[IMAGE alt='image' src='GUID-04F08314-80D7-4B15-8A02-703C2B31CE6D-a5.png']

The signals that flow downstream serve a similar purpose to those signals in the


 four-wire handshaking protocol. They inform downstream blocks of the validity of the


 data coming from the upstream block. For example, assuming two simple blocks with


 input signal x and output signal y,


 the m_y_tvalid output of IP Block 1 is


 TRUE whenever its m_y_tdata output contains valid


 y data.

The main difference between the LabVIEW four-wire handshaking protocol and the AXI


 Stream protocol lies in the meaning of the feedback signals, represented by the


 wires that flow upstream of the processing chain. An AXI signal informs upstream


 blocks of current cycle readiness and the four-wire signal informs upstream blocks


 of next cycle readiness. In AXI interfaces, a block deasserts its


 tready signal to indicate to its upstream counterpart


 that it is unable to receive data during the current clock cycle. The following


 timing diagram shows this scenario in the first few cycles. Notice that the value of


 tdata is held until the tready


 signal is reasserted.

[IMAGE alt='image' src='GUID-5E1785D1-2FEF-4B67-95A6-B8E5829ADC7B-a5.png']

The timing diagram above also shows how the master can halt the transfer by


 deasserting the tvalid signal in later cycles.

When interconnecting AXI IP in the single-cycle Timed Loop in LabVIEW, the output


 signals of IP Block 1 (AXI) connect to downstream IP


 Block 2 (AXI) through a Feedback Node, which acts as a register in the


 forward path. The Feedback Node temporarily stores any data in flight at the time


 the s_x_tready signal is deasserted until the slave block is


 ready to accept new data.

In AXI4-Stream, master blocks are not allowed to wait until the slave block is ready


 before producing valid data. When implementing blocks that conform to the AXI


 protocol, the block must repeatedly produce the same output, if valid, for as long


 as the associated tready signal remains deasserted.


 Additionally, an OR gate is needed to prime the handshaking process, as shown in the


 following diagram.

[IMAGE alt='image' src='GUID-BFC4B2C3-71E5-4226-B855-255508FA1512-a5.png']

#### Four-Wire to AXI Interconnect

The four-wire to AXI interconnect is similar to the AXI to AXI interconnect in its


 use of registers. The following diagram shows how to connect a single signal of a


 four-wire IP block to an AXI IP block.

[IMAGE alt='image' src='GUID-9D19CDF4-20EA-4581-B810-BABA636C24CE-a5.png']

#### AXI to Four-Wire Interconnect

The AXI to four-wire interconnect is similar to the four-wire to four-wire


 interconnect in its use of registers, but requires an AND gate to conform to the


 four-wire protocol requirement of providing valid data only when the downstream


 block is ready for input, as shown in the following diagram.

[IMAGE alt='image' src='GUID-47DF4FDD-C11A-499D-896D-6B0B111B5151-a5.png']

Parent topic:

Integrating Xilinx IP into FPGA VIs

Related concepts:

- Integrating Third-Party IP
- List of Xilinx IP
- Scheduling Timing Using Handshaking Signals
- Storing Data between Loop Iterations

<!--NI_TOPIC bundle=labview-fpga-module path=introduction-to-dsp48e-and-dsp48e1-slices-fpga-module.html language=enus -->
## TOPIC 00109: Introduction to DSP48E and DSP48E1 Slices

- bundle_id: `labview-fpga-module`
- source_path: `introduction-to-dsp48e-and-dsp48e1-slices-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/introduction-to-dsp48e-and-dsp48e1-slices-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file is not intended to be a comprehensive discussion of DSP48E or DSP48E1 slices. Before using these functions, We recommend that you become familiar with the Virtex-5 FPGA XtremeDSP Design Considerations User Guide for DSP48E functions or the Virtex-6 FPGA DSP48E1 Slice User Guide for DS

### Introduction to DSP48E and DSP48E1 Slices

Note

Virtex-5 FPGA
 XtremeDSP Design Considerations User Guide

Virtex-6 FPGA DSP48E1 Slice User Guide

www.xilinx.com

A DSP48E slice is a digital signal processing logic element


 included on certain FPGA device families, such as the Xilinx Virtex-5. You can use


 this slice to perform different kinds of arithmetic operations, including a


 multiply-accumulator, multiply-adder, and a one- or n-step


 counter. You also can use the slice to perform different kinds of logic operations,


 such as AND, OR, and XOR. You can cascade multiple DSP48E slices to implement more


 complex functions, including complex multipliers and n-tap finite impulse response


 (FIR) filters, without using any additional FPGA fabric resources.

A DSP48E1 slice is a digital signal processing element available only on certain


 Xilinx Virtex-6 and newer FPGA device families. The DSP48E1 slice includes a


 pre-adder before the multiplier and other features that extend the functionality of


 a DSP48E slice. This pre-adder is useful in implementing certain algorithms, such as


 symmetric FIR filters. Page 11 of the Virtex-6 FPGA DSP48E1 Slice User


 Guide contains a comprehensive listing of enhancements.

To access a DSP48E slice, add a DSP48E function to


 the block diagram and then configure the function.

Parent topic:

Creating FPGA VIs

Related concepts:

- Configuring DSP48E and DSP48E1 Functions

<!--NI_TOPIC bundle=labview-fpga-module path=introduction-to-fpga-applications-and-projects-fpga-module.html language=enus -->
## TOPIC 00110: Introduction to FPGA Applications and Projects

- bundle_id: `labview-fpga-module`
- source_path: `introduction-to-fpga-applications-and-projects-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/introduction-to-fpga-applications-and-projects-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA applications range from a local system with an FPGA target on a development computer running a single FPGA VI to a large embedded system that includes multiple FPGA targets, one or more RT targets, and LabVIEW running on a development computer. You must use LabVIEW project files (.lvproj) to cr

### Introduction to FPGA Applications and
 Projects

FPGA applications range from a local system with an FPGA target on a development


 computer running a single FPGA VI to a large embedded system that includes multiple


 FPGA targets, one or more RT targets, and LabVIEW running on a development computer.


 You must use LabVIEW project files (.lvproj) to create FPGA


 applications. Understanding your system architecture helps you use LabVIEW projects


 to build and manage your FPGA applications.

#### Understanding Local and Embedded Systems

The structure of your LabVIEW project depends on the components included in your FPGA


 application. Refer to the following figure to understand the physical layout of


 local and embedded systems containing an FPGA target.

[IMAGE alt='image' src='GUID-7D328D17-DFC9-4E09-9AC1-087B0D7DEFDD-a5.png']

#### Understanding the Components of an FPGA Project

Use the Project Explorer window to manage your FPGA project.


 Each FPGA project varies based on the components of the system architecture. The


 following figure shows the components of a local system, Local


 System.lvproj, versus an embedded system, Embedded


 System.lvproj.

[IMAGE alt='image' src='GUID-A9E2E8E5-33AB-4F6F-8A77-0530A456A0ED-a5.png']

The following table describes the components of an FPGA application and their


 location in LabVIEW FPGA projects.

|  | Component | Description |
| --- | --- | --- |
|  | LabVIEW Project | LabVIEW projects allow you to manage VIs and targets as you develop an application on the development computer. A LabVIEW project file includes references to files in the project, configuration information, deployment information, build information, and so on. |
|  | My Computer | My Computer, also called the development computer, is the computer you use to develop your LabVIEW project. The development computer is a PC that runs a supported version of Windows with LabVIEW and the LabVIEW FPGA Module installed. |
|  | RIO Chassis | The RIO chassis houses and directly connects the I/O blocks of the FPGA target to the interchangeable I/O modules for high-performance timing, triggering, and synchronization. |
|  | Controller | The controller directly connects to the RIO chassis and communicates with the development computer either directly or over a network. The controller includes an embedded processor that runs either a real-time operating system (RTOS) or Windows. |
|  | FPGA Target | The FPGA target is a programmable chip composed of logic blocks, I/O blocks, and programmable interconnects that implement the digital circuit you design with the LabVIEW FPGA Module. |
|  | FPGA VI | The FPGA VI is the VI that you download and run on the FPGA target. The LabVIEW compilation tools translate the FPGA VI into a circuit schematic to reconfigure the blocks and interconnects on the FPGA target. |
|  | Host VI | The host VI runs on the controller and communicates programmatically with the FPGA VI. You use the host VI to log data, control the timing of data transfer, and create a system with the FPGA target as a component. |
|  | User Interface VI | The user interface VI runs on the development computer and communicates with the host VI. The user interface VI allows the user to programmatically interact with the controls and indicators of the host VI. In the absence of a controller, the user interface VI becomes the host VI and communicates with the FPGA VI directly. |
|  | I/O | I/O refers to the analog and digital inputs and outputs of your FPGA system, such as thermocouples, RTD, bridge sensors, counters, pulse generation, and so on. Refer to your specific hardware documentation for supported I/O. |
|  | Clock | The clock controls the execution rate of the FPGA VI by specifying the timing objectives of an FPGA system. Operations occur at the rate determined by the dataflow of the VI if you do not include additional code to control the timing. The default clock rate on most FPGA targets is 40 MHz. |
|  | Build Specification | The build specification for your FPGA target specifies which of the following options LabVIEW creates when you compile your FPGA VI:Simulation Export—Configures and exports project files for third-party simulation.Compilation—Configures and translates project files into a bitfile to download to the FPGA target.Source Distribution—Configures project files for distribution as a stand-alone application. You must create a build specification before you compile, download, and run the FPGA VI. If you do not create a build specification, LabVIEW automatically creates and specifies a default build specification. |

Related concepts:

- What is the FPGA Module?
- Programming FPGAs Overview
- Managing FPGA Applications in the Project Explorer Window
- Adding FPGA Targets to a LabVIEW Project
- Adding Items to an FPGA Target in the Project Explorer Window
- Creating FPGA VIs
- Compiling, Downloading, and Running FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=introduction-to-fpga-hardware-concepts-fpga-module.html language=enus -->
## TOPIC 00111: Introduction to FPGA Hardware Concepts

- bundle_id: `labview-fpga-module`
- source_path: `introduction-to-fpga-hardware-concepts-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/introduction-to-fpga-hardware-concepts-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every FPGA chip, or FPGA, is composed of a finite number of predefined resources with programmable interconnects. These interconnects implement the digital circuit you design with the LabVIEW FPGA Module. When you create an FPGA VI, you design a circuit schematic that describes how logic blocks are

### Introduction to FPGA Hardware Concepts

Every FPGA chip, or FPGA, is composed of a finite number of predefined resources


 with programmable interconnects. These interconnects implement the digital circuit


 you design with the LabVIEW FPGA Module. When you create an FPGA VI, you design a


 circuit schematic that describes how logic blocks are wired together on the FPGA.


 When you compile the VI, the compilation


 tools translate the FPGA VI into the FPGA circuit.

Note

The following illustration shows the relationship between logic blocks, I/O blocks,


 and programmable routing on an FPGA.

[IMAGE alt='image' src='GUID-99BBDC14-45A5-4875-815D-624A255BD923-a5.png']

The following FPGA specifications are important to consider when designing an FPGA


 application.

- Number of configurable logic blocks
- Number of fixed function logic blocks, such as multipliers
- Size of memory resources, such as embedded block RAM

Refer to the support document at


 ni.com for more information about the fundamental parts of the


 FPGA.

#### Flip-Flops, LUTs, and Slices

FPGA resources are resources on the FPGA that can perform logic functions. FPGA


 resources are grouped in slices to create configurable logic blocks. A slice


 contains a set number of LUTs, flip-flops and multiplexers. A LUT is a collection of


 logic gates hard-wired on the FPGA. LUTs store a predefined list of outputs for


 every combination of inputs and provide a fast way to retrieve the output of a logic


 operation. A flip-flop is a circuit capable of two stable states and represents a


 single bit. A multiplexer, also known as a mux, is a circuit that selects between


 two or more inputs and outputs the selected input.

Different FPGA families implement slices and LUTs differently. For example, a slice


 on a Virtex-II FPGA has two LUTs and two flip-flops but a slice on a Virtex-5 FPGA


 has four LUTs and four flip-flops. In addition, the number of inputs to a LUT,


 commonly two to six, depend on the FPGA family.

#### Registers

A register is a group of flip-flops that stores a bit pattern. A register on the


 FPGA has a clock, input data, output data, and enable signal port. Every clock


 cycle, the input data is latched, stored internally, and the output data is updated


 to match the internally stored data. FPGA VIs use registers to perform the following


 functions:

- Holding state between iterations of a loop
- I/O synchronization
- Handshaking data between clock domains
- Pipelining
- Communicating with a host VI

Registers are a key concept in understanding timing considerations for FPGA VIs.

#### Block RAM

Block RAM, or block memory, is RAM that is embedded throughout the FPGA for storing


 data. In general, LabVIEW uses block RAM when synthesizing Memory &


 FIFO functions. You can specify how LabVIEW implements FIFOs and memory


 items in the FIFO Properties and Memory


 Properties dialog boxes, respectively.

#### DSP48E and DSP48E1

A DSP48E slice is a digital signal processing logic element


 included on certain FPGA device families, such as the Xilinx Virtex-5. You can use


 this slice to perform different kinds of arithmetic operations, including a


 multiply-accumulator, multiply-adder, and a one- or n-step


 counter. You also can use the slice to perform different kinds of logic operations,


 such as AND, OR, and XOR. You can cascade multiple DSP48E slices to implement more


 complex functions, including complex multipliers and n-tap finite impulse response


 (FIR) filters, without using any additional FPGA fabric resources.

A DSP48E1 slice is a digital signal processing element available only on certain


 Xilinx Virtex-6 and newer FPGA device families. The DSP48E1 slice includes a


 pre-adder before the multiplier and other features that extend the functionality of


 a DSP48E slice. This pre-adder is useful in implementing certain algorithms, such as


 symmetric FIR filters.

#### UltraRAM

UltraRAM, or URAM, is a flexible, high-density, and large-size memory building block


 available on most Xilinx UltraScale+ targets. UltraRAM has eight times the capacity


 of a block memory but is less flexible in data width and address space configuration


 than block memory. Use UltraRAM as a storage element for large local FIFOs. You can


 specify how LabVIEW implements FIFOs in the FIFO Properties


 dialog box.

Parent topic:

Programming FPGAs Overview

Related concepts:

- What is the FPGA Module?
- Configuring DSP48E and DSP48E1 Functions
- Dataflow and the Enable Chain in FPGA VIs
- Optimizing FPGA VIs Using Pipelining
- Understanding Timing Considerations for FPGA VIs
- Limiting the Number of Top-Level Front Panel Objects in FPGA VIs
- Managing FPGA Applications in the Project Explorer Window
- Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=limiting-the-number-of-top-level-front-panel-objects-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00112: Limiting the Number of Top-Level Front Panel Objects in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `limiting-the-number-of-top-level-front-panel-objects-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/limiting-the-number-of-top-level-front-panel-objects-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To decrease the amount of space the FPGA VI uses, reduce the number of front panel controls and indicators on the top-level FPGA VI. Each front panel object in a top-level FPGA VI consumes a significant amount of space on the FPGA because LabVIEW includes additional logic to communicate between the

### Limiting the Number of Top-Level Front Panel Objects in FPGA VIs

To decrease the amount of space the FPGA VI uses, reduce the number of front panel


 controls and indicators on the top-level FPGA VI. Each front panel object in a


 top-level FPGA VI consumes a significant amount of space on the FPGA because LabVIEW


 includes additional logic to communicate between the top-level FPGA VI and the host


 VI. Registers that store front panel control and indicator data require more


 flip-flops than internal registers.

Front panel objects in subVIs do not communicate directly with the host VI and


 therefore do not consume additional space on the FPGA. SubVI controls and indicators


 that must hold state information from one call to another use registers to store


 data. SubVI controls and indicators that only pass data into and out of a subVI


 consume no FPGA resources.

#### Limiting Arrays

Arrays appearing as top-level front panel objects consume significant space on the


 FPGA because each bit in the array uses a flip-flop on the FPGA. Consider replacing


 arrays with FIFOs or memory


 items to transfer data.

When you wire an array as an input to a function, the FPGA compiler creates the


 equivalent of a For loop to process each element of the array in sequence. If you


 wire a cluster as an input to an FPGA VI or function, the FPGA compiler creates


 parallel logic for each element of the cluster. The relationship between arrays and


 clusters is recursive such that if you wire a cluster of arrays as an input, the


 arrays are processed in parallel and the array elements are processed


 sequentially.

Note

#### Using Global Variables

If you do not need to access front panel controls and indicators from a host VI,


 consider replacing the controls and indicators with global


 variables to pass data within an FPGA VI. If you do not need to pass


 data, consider replacing controls with constants to decrease the amount of space the


 FPGA VI uses.

#### Using Feedback Nodes

To reduce resources, use Feedback Nodes


 instead of controls to store data in subVIs.

#### Bitpacking Data Types

To reduce the number of front panel objects, you might be able to combine objects, as


 shown in the following illustration.

[IMAGE alt='image' src='GUID-43FCB039-0701-497F-B906-A0AAE840CEFD-a5.png']

In the illustration above, each Boolean control on the top-level FPGA VI contains


 extra logic that consumes space on the FPGA. However, if you use a single 8-bit


 numeric control to represent the data, only one control contains extra logic. You


 can use the Number To Boolean Array and Index Array


 functions to access elements of the numeric control.

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Introduction to FPGA Hardware Concepts
- Optimizing FPGA VIs for Speed and Size
- Transferring Data Using Direct Memory Access
- Transferring Data Using Front Panel Controls and Indicators

<!--NI_TOPIC bundle=labview-fpga-module path=list-of-xilinx-ip-fpga-module.html language=enus -->
## TOPIC 00113: List of Xilinx IP

- bundle_id: `labview-fpga-module`
- source_path: `list-of-xilinx-ip-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/list-of-xilinx-ip-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Xilinx IP Functions to implement Xilinx IP in an FPGA VI. Refer to the Xilinx IP palette for a list of Xilinx IP functions available in the FPGA Module. The Xilinx IP names come from Xilinx IP data sheets, available on the Xilinx website at www.xilinx.com. Refer to the Xilinx IP data sheets

### List of Xilinx IP

Use the Xilinx IP Functions to implement Xilinx IP in an FPGA


 VI. Refer to the Xilinx IP palette for a list of Xilinx IP functions available in


 the FPGA Module. The Xilinx IP names come from Xilinx IP data sheets, available on


 the Xilinx website at www.xilinx.com. Refer to


 the Xilinx IP data sheets for detailed information about the Xilinx IP.

Note

ni.com/info

Parent topic:

Integrating Xilinx IP into FPGA VIs

Related concepts:

- Interfacing AXI IP in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=making-subvis-non-reentrant-fpga-module.html language=enus -->
## TOPIC 00114: Making SubVIs Non-Reentrant

- bundle_id: `labview-fpga-module`
- source_path: `making-subvis-non-reentrant-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/making-subvis-non-reentrant-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To make a subVI non-reentrant, complete the following steps. Press <Ctrl-I> to display the VI Properties dialog box. Select Execution from the Category pull-down menu. Select Non-reentrant execution in the Reentrancy section. Click OK.

### Making SubVIs Non-Reentrant

To make a subVI non-reentrant, complete the following steps.

1. Press <Ctrl-I> to display the VI Properties dialog


 box.
2. Select Execution from the Category 


 pull-down menu.
3. Select Non-reentrant execution in the


 Reentrancy section.
4. Click OK .

[IMAGE alt='image' src='GUID-3E11F72E-AC41-4B74-80BB-ECBD48ADCFA4-a5.png']

Parent topic:

Using SubVIs in FPGA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=manage-execution-rates-with-fpga-timing-functions-fpga-module.html language=enus -->
## TOPIC 00115: Manage Execution Rates with FPGA Timing Functions

- bundle_id: `labview-fpga-module`
- source_path: `manage-execution-rates-with-fpga-timing-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/manage-execution-rates-with-fpga-timing-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating Timed I/O Applications Applications often require the I/O to execute at a specific frequency. For example, the algorithms used in control loops typically require the inputs to be sampled at a known rate. Use the Loop Timer Express VI in a While Loop to control the execution rate of the I/O,

### Manage Execution Rates with FPGA Timing Functions

#### Creating Timed I/O Applications

Applications often require the I/O to execute at a specific frequency. For example,


 the algorithms used in control loops typically require the inputs to be sampled at a


 known rate. Use the Loop Timer Express VI in a While Loop to control the


 execution rate of the I/O, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-8CF85961-5F9C-401C-A9E0-9AD740BFD1F0-a5.png']

To use the Loop Timer Express VI to control the execution rate of the I/O, place a


 Sequence structure inside a While Loop. Place the Loop Timer Express VI in the first


 frame of the sequence structure. Configure the Counter Units


 and Size of Internal Counter in the Configure Loop


 Timer dialog box that appears. Place the LabVIEW code for the I/O in


 subsequent frames of the sequence structure.

Tip

Size of Internal Counter

The first call of the Loop Timer Express VI does not result in any wait or delay


 because this call establishes a reference time stamp for subsequent calls. After the


 first call of the Loop Timer Express VI, subsequent calls of the Loop Timer Express


 VI do not return until the time specified by the Count


 parameter has elapsed since the previous call. If the time specified by the


 Count parameter is less than the time it takes the FPGA


 target to execute the code in the While Loop, the Loop Timer Express VI does not


 affect the timing of the While Loop.

#### Creating Delays between Events

Use the Wait Express VI to create a delay between events in an FPGA VI. For


 example, you might want to create a delay between a trigger and a subsequent output.


 You can place the LabVIEW code for the trigger in the first frame of a sequence


 structure. Then place the Wait Express VI in the following frame. Finally, place the


 LabVIEW code for the output in the last frame of the sequence structure. You also


 can create a series of delays using multiple Wait VIs in a sequence structure, as


 shown in the following block diagram.

[IMAGE alt='image' src='GUID-A8262CCA-8A23-49DA-A1F1-51A722D411B5-a5.png']

#### Measuring Time between Events

Use the Tick Count Express VI to measure the time between events


 such as edges on a digital signal. You can use this Express VI when you need to


 determine the period, pulse-width, or frequency of an input signal or if you want to


 determine the execution time of a section of LabVIEW code.

For example, to determine the amount of time it takes a function or a section of


 LabVIEW code to execute, use a Sequence structure with two Tick Count Express VIs,


 as shown in the following block diagram.

[IMAGE alt='image' src='GUID-BF8FB693-124D-45EF-BEE2-E1686ECE053B-a5.png']

Place one Tick Count Express VI in the first frame of the Sequence structure. Then


 place the LabVIEW code you want to measure in the second frame of the Sequence


 structure. Finally, place the other Tick Count Express VI in the last frame of the


 sequence structure. You then can calculate the difference between the results of the


 two Tick Count Express VIs to determine the execution time. Subtract one from the


 result of the calculation to compensate for the execution time of the Tick Count


 Express VI.

The Tick Count Express VI has an internal counter to track time. The internal counter


 for each Tick Count Express VI you place on the same block diagram shares the same


 start time. Therefore, every Tick Count Express VI that uses the same values for the


 Counter Units and Size of Internal


 Counter options tracks the same time. For example, if you call two


 Tick Count Express VIs that use the same Configure Tick Count


 options at the same time, they return the same Tick Count


 value.

The Tick Count Express VI returns an integer value in Counter


 Units. The Tick Count value cannot represent


 any fractional time periods that might occur when Counter


 Units is configured for uSec or


 mSec. Configuring Counter Units


 for uSec or mSec can result in timing


 measurements that have an accuracy of ±1 Counter Unit value.


 For example, you can configure the Tick Count Express VIs in the block diagram above


 to measure time in milliseconds. If the first Tick Count Express VI executes at 47.9


 milliseconds, Tick Count returns a value of 47. If the second


 Tick Count Express VI executes at 53.2 milliseconds, Tick


 Count returns a value of 53. Although this example has a 5.3


 millisecond delay, the difference between the returned values is 6 milliseconds.

Parent topic:

Controlling the FPGA VI Execution Rate

Related concepts:

- Using the Integer Data Type

<!--NI_TOPIC bundle=labview-fpga-module path=managing-fpga-applications-in-the-project-explorer-window-fpga-module.html language=enus -->
## TOPIC 00116: Managing FPGA Applications in the Project Explorer Window

- bundle_id: `labview-fpga-module`
- source_path: `managing-fpga-applications-in-the-project-explorer-window-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/managing-fpga-applications-in-the-project-explorer-window-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to manage the components of an FPGA application, including the FPGA VI and host VI, the FPGA target, and target-specific options, such as FPGA I/O, FPGA FIFOs, and FPGA target clocks. The illustration below shows the Project Explorer window with an FPGA target, an FPG

### Managing FPGA Applications in the Project
 Explorer Window

Use the Project Explorer window to manage the components of an


 FPGA application, including the FPGA VI and host VI, the FPGA target, and


 target-specific options, such as FPGA I/O, FPGA FIFOs, and FPGA target clocks. The illustration below shows the


 Project Explorer window with an FPGA target, an FPGA base


 clock and derived clock, an FPGA VI, an FPGA I/O item, a FIFO, and a host VI.

[IMAGE alt='image' src='GUID-0C61E74A-228D-4C58-BB47-D6BA990DC7C1-a5.png']

You must create projects for FPGA VIs and host VIs. You can create a project using


 the FPGA Project wizard. You also can create a project by


 clicking the Empty Project link in the Getting Started window or by selecting


 File»New in LabVIEW and Project»Empty


 Project in the New dialog


 box. You now can add FPGA


 targets, FPGA target


 clocks, FPGA I/O,


 and FPGA FIFOs to the project. You can select an FPGA target


 you previously configured in the NI Measurement & Automation Explorer (MAX) or


 you can add a new FPGA target. You can add, configure, and manage VIs, folders, and


 FPGA project items below FPGA targets in the Project


 Explorer window.

To add items to an FPGA target, right-click the target in the Project


 Explorer window and select


 New»x from the shortcut menu, where


 x is the type of item you want to add, such as a VI, FPGA I/O


 item, or FIFO. The item appears in the Project Explorer window under the FPGA


 target.

#### Using Target-Specific Functionality

You create FPGA VIs in the same way you create VIs that run on Windows. However,


 programming an FPGA effectively requires some knowledge of the target capabilities


 and basic FPGA hardware concepts.

Each item below an FPGA target in the Project


 Explorer window contains FPGA target-specific information and


 functionality. When you select an item below an FPGA target in the


 Project Explorer window, LabVIEW displays only the


 options that the FPGA target supports. For example, if you select an FPGA VI below


 an FPGA target in the Project Explorer window and view the


 block diagram, LabVIEW displays only the subpalettes, VIs, and functions on the


 Functions palette that the FPGA target supports.

Note

[IMAGE alt='image' src='GUID-19E027DD-C614-4228-A6D1-DFAC88832828-a5.png']

#### Managing Multiple FPGA Targets

You can reuse items among different FPGA targets in a Project


 Explorer window. However, the new FPGA target might not support the same


 functionality as the previous FPGA target, so you must update the item properties to


 match the functionality and resources of the new FPGA target. For example, if you


 copy an FPGA I/O item between two different FPGA targets, you must verify the FPGA


 target to which you copied the FPGA I/O item supports the same I/O resource to which


 the FPGA I/O item was assigned in the first FPGA target.

Parent topic:

Introduction to FPGA Applications and Projects

Related concepts:

- Introduction to FPGA Hardware Concepts
- Reusing FPGA Objects
- Introduction to FPGA Applications and Projects

<!--NI_TOPIC bundle=labview-fpga-module path=managing-shared-resources-fpga-module.html language=enus -->
## TOPIC 00117: Managing Shared Resources

- bundle_id: `labview-fpga-module`
- source_path: `managing-shared-resources-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/managing-shared-resources-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some LabVIEW FPGA Module applications contain shared resources that multiple objects, such as functions or subVIs, access in an FPGA VI. The following are possible shared resources: Digital output lines Analog lines Register items Memory items FIFOs Handshake items The interrupt line Local and globa

### Managing Shared Resources

Some LabVIEW FPGA Module applications contain shared resources that multiple


 objects, such as functions or subVIs, access in an FPGA VI. The following are


 possible shared resources:

- Digital output lines
- Analog lines
- Register items
- Memory items
- FIFOs
- Handshake items
- The interrupt line
- Local and global variables
- Non-reentrant subVIs

Each shared resource contains one or more resource interfaces. A resource interface


 communicates between objects and shared resources, as shown in the following


 figure.

[IMAGE alt='image' src='GUID-2A5BBBD5-D4D2-4AE7-AD0B-817CF92A856B-a5.png']

Resource contention occurs when you include two or more objects on the FPGA VI block


 diagram that simultaneously request access to the same shared resource through the


 same resource interface. In the previous figure, resource contention does not occur


 because the objects request access to the shared resource through two different


 resource interfaces.

However, in the following figure, the two Memory Method Nodes request access to the


 same shared resource (My Memory Item) through the same resource interface. If the


 two Memory Method Nodes request access to the shared resource at the same time,


 resource contention occurs.

[IMAGE alt='image' src='GUID-7C0294BB-26A7-441B-B816-91404ED22B86-a5.png']

#### Using Arbitration to Avoid Resource Contention

To help you avoid resource contention, the FPGA Module offers arbitration options to


 determine which object can access the resource if multiple objects request access at


 the same time. The arbitration option you select determines if LabVIEW uses an arbiter. The


 arbitration options from which you can select vary by resource.

Note

Objects that request access to a resource through a resource interface are called


 requestors. A requestor becomes an accessor when the arbiter grants access to the


 resource, as shown in the following figure.

[IMAGE alt='image' src='GUID-0F54F36B-682F-40A0-B363-23BB5BD09BEE-a5.png']

Most objects interact with a single resource interface. However, in some situations,


 some objects interact with multiple interfaces. For example, if you use the FPGA I/O


 Node for a bidirectional digital line, the FPGA I/O Node interacts with the output


 data and output enable interfaces on the corresponding resource, as shown in the


 following figure.

[IMAGE alt='image' src='GUID-1F0E9BBC-ADB7-48EF-8A7C-253919FB5B91-a5.png']

The previous figure approximately maps to a circuit as shown in the following


 schematic diagram.

[IMAGE alt='image' src='GUID-426F63EB-0862-4A8D-878D-6CD8042C7EF8-a5.png']

In the previous figure, the circuit controls Output Enable and


 Output Data separately, so the LabVIEW FPGA Module


 represents Output Enable and Output


 Data as separate resource interfaces.

You can configure the arbitration options for each resource interface of FPGA I/O, FIFO, and


 memory items if you need to optimize the FPGA VI. If the FPGA VI design fits on the FPGA, meets the


 performance expectations, and compiles without errors, keep the default arbitration


 option. The default arbitration option for I/O depends on the FPGA target and the


 I/O resource. The default arbitration option for FIFOs and memory items is


 Arbitrate if Multiple Requestors Only. Other resources


 that include arbitration, such as controls and global variables, include fixed


 arbitration settings. You cannot change the arbitration option for such resources,


 so in some situations, you might need to modify the code on the block diagram to


 avoid resource contention.

Note

Parent topic:

Creating FPGA VIs

Related concepts:

- Avoiding Arbitration to Optimize FPGA VIs
- Avoiding Jitter Due to Resource Contention
- Using FPGA I/O
- Determining When to Use Reentrant or Non-Reentrant SubVIs
- Understanding Arbitration Options
- Optimizing FPGA VIs for Speed and Size
- Synchronizing the FPGA and the Host
- Using DRAM
- Using Parallel Operations

<!--NI_TOPIC bundle=labview-fpga-module path=measuring-while-loop-execution-rate-fpga-module.html language=enus -->
## TOPIC 00118: Measuring While Loop Execution Rate

- bundle_id: `labview-fpga-module`
- source_path: `measuring-while-loop-execution-rate-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/measuring-while-loop-execution-rate-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to measure the execution time of a While Loop in an FPGA VI. Add a While Loop to the block diagram. Right-click the conditional terminal of the While Loop and select either Create Constant or Create Control from the shortcut menu, depending on the needs of the applicatio

### Measuring While Loop Execution Rate

Complete the following steps to measure the execution time of a While Loop in an FPGA


 VI.

1. Add a While Loop to the block diagram.
2. Right-click the conditional terminal of the While Loop and select either


 Create Constant or Create


 Control from the shortcut menu, depending on the needs of the


 application.
3. Add the code you want to execute to the While Loop.
4. Add a Tick Count Express VI to the While Loop and click


 the OK button in the Configure Tick


 Count dialog box.
5. Right-click the While Loop and select Add Shift Register 


 from the shortcut menu.
6. Add a Subtract function to the While Loop.
7. Wire the Tick Count terminal of the Tick Count Express VI


 to the right shift register on the While Loop and to the


 x terminal of the Subtract function.
8. Wire the left shift register to the y terminal of the


 Subtract function.
9. Right-click the x–y terminal of the Subtract function and


 select Create»Indicator .
10. Run the VI. The value shown in the x–y indicator is the


 While Loop execution rate.

Parent topic:

Controlling the FPGA VI Execution Rate

<!--NI_TOPIC bundle=labview-fpga-module path=moving-ip-integration-nodes-to-another-computer-fpga-module.html language=enus -->
## TOPIC 00119: Moving IP Integration Nodes to Another Computer

- bundle_id: `labview-fpga-module`
- source_path: `moving-ip-integration-nodes-to-another-computer-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/moving-ip-integration-nodes-to-another-computer-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: As you configure and use the IP Integration Node, LabVIEW generates several support files to disk. You must keep these files with the VI that contains the IP Integration Node. If you move the VI that contains this Node to another folder on disk or another computer, or you check the VI into source co

### Moving IP Integration Nodes to Another
 Computer

As you configure and use the IP Integration Node, LabVIEW generates several support


 files to disk. You must keep these files with the VI that contains the IP


 Integration Node.

If you move the VI that contains this Node to another folder on disk or another


 computer, or you check the VI into source


 control, move these files along with the VI. Otherwise, you will need to


 regenerate the support files on the new computer.

Note

When moving VIs to another computer, keep the following files with the VI:

- The synthesis files you specify on the Name and


 Source page, including the following generated files:
  - (If the


 IP includes Xilinx IP configuration files) Any files in the (Xilinx ISE)


 xco_filename \XcoGeneratedFiles 


 directory or the (Xilinx Vivado)


 xci_filename \XciGeneratedFiles 


 directory. The (Xilinx ISE)


 xco_filename \XcoGeneratedFiles 


 directory is located in the same directory as the .xco 


 file itself or the (Xilinx Vivado)


 xci_filename \XciGeneratedFiles 


 directory is located in the same directory as the .xci 


 file itself.
  - (If the IP includes .ngc files)


 Any files in the


 ngc_filename \NgcGeneratedFiles\(Vivado/ISE) 


 directory. The


 ngc_filename \NgcGeneratedFiles\(Vivado/ISE) 


 directory is located in the same directory as the .ngc 


 file itself.
  - (If the IP includes .edif files)


 Any files in the


 edif_filename \EdifGeneratedFiles\(Vivado/ISE) 


 directory. The


 edif_filename \EdifGeneratedFiles\(Vivado/ISE) 


 directory is located in the same directory as the .edif 


 file itself.
- Any simulation files you specify in the Set Simulation


 Behavior dialog box.
- All generated simulation files, which are located in the


 IP_name \ SimFiles 


 directory. The IP_name directory is located


 in the same directory as the top-level


 synthesis file. You define the IP Name by using the IP


 Name text box on the Name and


 Source page of the configuration dialog box. Note Do


 not use the same IP Name for more than one IP


 Integration Node. If you do use the same name for more than one IP


 Integration Node and generate a


 simulation model, LabVIEW displays a warning to prevent you from


 overwriting the simulation files of another node.

Parent topic:

Using the IP Integration Node

<!--NI_TOPIC bundle=labview-fpga-module path=new-features-and-changes.html language=enus -->
## TOPIC 00120: LabVIEW FPGA Module New Features and Changes

- bundle_id: `labview-fpga-module`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW FPGA Module. Discover what is new in the latest releases of LabVIEW FPGA Module.If you cannot find new features and changes for your version, it might not include user-facing updates. However, you

### LabVIEW FPGA Module
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW FPGA Module.

LabVIEW FPGA Module

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW FPGA Module 2022 Q3 Changes

- New I/O Module Properties node added. Use this node with the
 Module constant to view properties for CompactRIO devices.

#### LabVIEW FPGA Module 2020 Changes

- Support for C Series FPGA targets.
- The Open FPGA VI Reference node has the following changes:
  - The Convert to Fixed-Point tab is deprecated. This option
 provided tools to convert floating-point data types to fixed-point.
  - The RIO address input is renamed device
 name .
  - The Deploy from file run mode is no longer available.
- The Run FPGA Simulation node is renamed Run GCDL
 Simulation .
- The Set Output Enable (Clock-Driven Logic) node has the following
 changes:
  - Terminals added for error in and error
 out .
  - The enable input is renamed enable? .

#### LabVIEW FPGA Module 2019 Changes

- Access memory items outside a clock-driven loop.
- Non-functional terminals removed from I/O channel nodes.
- The LabVIEW FPGA Module is no longer required to perform the following tasks:
  - Access FPGA targets in the Design view palette of SystemDesigner.
  - View or edit FPGA code.
  - Deploy bitfiles (.lvbitx) to FPGA targets.
  - Migrate LabVIEW FPGA functions to LabVIEW.
- The LabVIEW FPGA Module and relevant drivers are required to perform the following
 tasks:
  - Use driver-specific features in your FPGA code.
  - Run or compile FPGA code.
  - Migrate LabVIEW FPGA code that relies on specific drivers to LabVIEW..
- Compile FPGA code locally without manually setting up the FPGA compiler
 environment.
- Configure an FPGA resource constant to display the namespace in the resource name.

<!--NI_TOPIC bundle=labview-fpga-module path=opening-a-reference-to-an-fpga-vi-build-specification-or-bitfile-fpga-interface.html language=enus -->
## TOPIC 00121: Opening a Reference to an FPGA VI, Build Specification, or Bitfile

- bundle_id: `labview-fpga-module`
- source_path: `opening-a-reference-to-an-fpga-vi-build-specification-or-bitfile-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/opening-a-reference-to-an-fpga-vi-build-specification-or-bitfile-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can communicate with FPGA VIs or bitfiles running on FPGA targets using host VIs. Host VIs can run on PCs or RT targets. Each host VI must open a reference to the FPGA VI, build specification, or bitfile that runs on the FPGA target. You can open a reference to any FPGA VI or build specification

### Opening a Reference to an FPGA VI, Build
 Specification, or Bitfile

You can communicate with FPGA VIs or bitfiles running on FPGA targets using host VIs.



 Host VIs can run on PCs or RT targets. Each host VI must open a reference to the



 FPGA VI, build specification, or bitfile that runs on the FPGA target. You can open a



 reference to any FPGA VI or build specification that is part of the same LabVIEW



 project as the host VI. You can open a reference to any bitfile inside or outside



 the project.

The FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you want



 to open a reference to an FPGA VI. The host VI does not need to be in a project if



 you open a reference to a bitfile.

Note

#### Opening a Reference to an FPGA VI or Build Specification

Complete the following steps to open a reference to an FPGA VI or build specification



 in a host VI. You can open a reference if the host VI, FPGA target, FPGA VI, and



 build specification are in the same project. You cannot open a reference to an FPGA



 VI or build specification if you do not have the LabVIEW FPGA Module installed.

1. Create a new project or open an existing



 project.
2. Add an FPGA target to the project or verify the FPGA



 target appears in the Project



 Explorer window.
3. Create a new FPGA VI or verify the FPGA VI to which you want to open



 a reference appears in the Project Explorer window under



 the FPGA target.
4. Create a new host VI or open an existing host VI in the project. The host VI



 must be under My Computer or an RT target in the



 Project Explorer window.
5. Add an Open



 FPGA VI Reference function to the block diagram.
6. (Optional) Drag the FPGA VI you want to open a reference to from the



 Project Explorer window to the Open FPGA VI Reference



 function. The FPGA VI icon appears in the Open FPGA VI Reference function. If



 the FPGA target in the project is associated with a physical target, the target



 name and resource appears under the Open FPGA VI Reference function.
7. (Optional) Right-click the Open FPGA VI Reference function and select



 Configure Open FPGA VI Reference from the shortcut



 menu to display the Configure



 Open FPGA VI Reference dialog box, which you can use to select a



 build specification and other options for opening the reference.
8. (Optional) Wire a control or constant to the resource



 name input on the Open FPGA VI Reference function to specify an



 FPGA target on which to run the FPGA VI.

Note

#### Opening a Reference to a Bitfile

Complete the following steps to open a reference to a bitfile in a host VI. The host



 VI does not need to be in a project. If your application requires a reference to a



 bitfile at run time, wire an Open



 Dynamic Bitfile Reference function in place of the Open FPGA VI Reference function.

1. Create a new host VI or open an existing host VI. If the host VI is in a



 project, the host VI must be under My Computer or an RT



 target in the Project Explorer window.
2. Add an Open



 FPGA VI Reference function to the block diagram.
3. Right-click the Open FPGA VI Reference function and select Configure



 Open FPGA VI Reference from the shortcut menu.
4. Select the Bitfile option in the Configure



 Open FPGA VI Reference dialog box.
5. Navigate to the bitfile you want to open on an FPGA target.
6. (Optional) Use the Configure Open FPGA VI Reference 



 dialog box to select additional options for opening the reference.
7. Click the OK button. The FPGA VI icon appears in the Open



 FPGA VI Reference function. A folder icon appears in the upper left corner of



 the Open FPGA VI Reference function to denote the bitfile.
8. Wire a control or constant to the resource name input on



 the Open FPGA VI Reference function to specify an FPGA target on which to run



 the FPGA VI.

Note

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Downloading an FPGA VI to an FPGA Target
- Using Multiple FPGA VI References for the Same Target
- Reading DMA FIFOs from Host VIs
- Reading FPGA VI Indicators
- Synchronizing FPGA VIs and Host VIs Using Interrupts
- Using LabVIEW FPGA Interface without the FPGA Module
- Writing to DMA FIFOs from Host VIs
- Writing to FPGA VI Controls

<!--NI_TOPIC bundle=labview-fpga-module path=optimizing-fpga-vis-for-speed-and-size-fpga-module.html language=enus -->
## TOPIC 00122: Optimizing FPGA VIs for Speed and Size

- bundle_id: `labview-fpga-module`
- source_path: `optimizing-fpga-vis-for-speed-and-size-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/optimizing-fpga-vis-for-speed-and-size-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to optimize the performance of an FPGA VI, you might be able to modify the FPGA VI to increase speed, decrease the FPGA logic utilization, or both. The following table includes techniques you can use to optimize an FPGA VI. To understand the techniques in this table, you must be familiar

### Optimizing FPGA VIs for Speed and Size

If you want to optimize the performance of an FPGA VI, you might be able to modify


 the FPGA VI to increase speed, decrease the FPGA logic utilization, or both.

The following table includes techniques you can use to optimize an FPGA VI.

Note

| Optimization Technique | FPGA Speed | FPGA Size |
| --- | --- | --- |
| Reduce combinatorial paths. |  |  |
| Use pipelining when appropriate. |  |  |
| Use single-cycle Timed Loops. |  |  |
| Use parallel operations. |  |  |
| Select Never Arbitrate as an arbitration option. |  |  |
| Use non-reentrant subVIs. |  |  |
| Use reentrant subVIs. |  |  |
| Limit the number of front panel objects, such as arrays. |  |  |
| Use the smallest data type possible. |  |  |
| Limit the size of custom data types. |  |  |
| Avoid large VIs and functions, if possible. |  |  |
| Schedule timing using handshaking signals. |  |  |
| Use an external data value reference when accessing DMA FIFOs. |  |  |
| Reduce block memory resource usage by configuring dual port read access if possible. |  |  |
| Choose a block memory implementation for array constants unless you need the advantages of a different type of memory. Block memory does not consume FPGA resources and tends to compile at a high clock rate relative to other types of memory. |  |  |
| Remove the implicit enable signal from single-cycle Timed Loops that run independently of other nodes on the block diagram. This strategy is most useful for very large designs. |  |  |

Related concepts:

- Managing Shared Resources
- Introduction to FPGA Hardware Concepts
- Reducing Combinatorial Paths in FPGA VIs
- Optimizing FPGA VIs Using Pipelining
- Using Single-Cycle Timed Loops to Optimize FPGA VIs
- Using Parallel Operations
- Avoiding Arbitration to Optimize FPGA VIs
- Determining When to Use Reentrant or Non-Reentrant SubVIs
- Limiting the Number of Top-Level Front Panel Objects in FPGA VIs
- Using the Smallest Data Type to Optimize FPGA VIs
- Using Custom Data Types with Register Items, Memory Items, FIFOs, and Handshake Items
- Avoiding Large VIs and Functions in FPGA VIs When Possible
- Scheduling Timing Using Handshaking Signals
- Reducing Memory Resource Usage with Dual-Port Read Access

<!--NI_TOPIC bundle=labview-fpga-module path=optimizing-fpga-vis-using-pipelining-fpga-module.html language=enus -->
## TOPIC 00123: Optimizing FPGA VIs Using Pipelining

- bundle_id: `labview-fpga-module`
- source_path: `optimizing-fpga-vis-using-pipelining-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/optimizing-fpga-vis-using-pipelining-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pipelining is a technique you can use to increase the clock rate and throughput of an FPGA VI. Pipelined designs take advantage of the parallel processing capabilities of the FPGA to increase the efficiency of sequential code. To implement a pipeline, divide code into discrete steps and wire the inp

### Optimizing FPGA VIs Using Pipelining

Pipelining is a technique you can use to increase the clock rate and throughput of


 an FPGA VI. Pipelined designs take advantage of the parallel processing capabilities


 of the FPGA to increase the efficiency of sequential code. To implement a pipeline,


 divide code into discrete steps and wire the inputs and outputs of each step to


 Feedback Nodes or shift registers in a loop.

The following sections demonstrate FPGA VIs with standard execution versus pipelined


 execution in a single-cycle Timed Loop.

#### Standard Execution in a Single-Cycle Timed Loop

In the following block diagram, subVIs A,


 B, and C execute in sequence


 within a single-cycle Timed Loop. As a result, you set the clock rate of the


 single-cycle Timed Loop to accommodate the sum of the running times of all three


 running subVIs.

[IMAGE alt='image' src='GUID-EF863C0E-FDC7-4FBD-808F-17F99CD68200-a5.png']

#### Pipelined Execution in a Single-Cycle Timed Loop Using Feedback Nodes

In the following block diagram, LabVIEW pipelines the subVIs because the inputs and


 outputs of the subVIs are wired to Feedback Nodes. In this FPGA VI, the subVIs


 execute in parallel, all within a single cycle, and the maximum clock rate is


 limited only by the subVI with the longest combinatorial path.

[IMAGE alt='image' src='GUID-0AF259A0-0C08-4AB6-BF9F-3E6DE32999F7-a5.png']

#### Pipelined Execution in a Single-Cycle Timed Loop Using Shift Registers

You also can use shift registers to implement pipelined code, as shown in the


 following block diagram.

[IMAGE alt='image' src='GUID-E571971B-0D26-487A-8935-C640E0D0676B-a5.png']

#### Implementing Pipelined Code

Consider the following behaviors when implementing pipelined code:

- The output of the final step lags behind the input by the number of steps in the


 pipeline.
- The output is invalid for each clock cycle until the pipeline fills.
- The number of steps in a pipeline is called the pipeline depth.
- The latency of a pipeline, measured in clock cycles, corresponds to its depth.


 For a pipeline of depth N , the result is invalid until the


 N th clock cycle, and the output of each valid


 clock cycle lags behind the input by N -1 clock cycles.

Consider the following example.

[IMAGE alt='image' src='GUID-8476E5D9-93D6-441B-B9A0-5308DD6CCDBE-a5.png']

In this example, there are three separate execution steps in executing subVIs


 A, B, and


 C, resulting in a pipeline depth of three. Because this code


 requires three execution steps, the output is not valid until Clock Cycle


 3. The output of each valid clock cycle C always corresponds to the


 input from clock cycle C – (N – 1).

| Clock Cycle | Description |
| --- | --- |
| Clock Cycle 1 | In Clock Cycle 1, subVI A processes the first measurement (Meas1), while subVI B and subVI C both process the default value of the shift register (Default), yielding an invalid output. |
| Clock Cycle 2 | During Clock Cycle 2, subVI A processes the second measurement (Meas2), subVI B processes the output of subVI A from Clock Cycle 1, and subVI C processes an invalid input from subVI B, yielding an invalid output. |
| Clock Cycle 3 | During Clock Cycle 3, the pipeline finally fills, as all inputs are valid, and the output from subVI C is valid for the first time. subVI A processes the third measurement (Meas3), subVI B processes the output of subVI A from Clock Cycle 2, and subVI C processes the output of subVI B from Clock Cycle 2, yielding the output that corresponds to the first measurement (Meas1). After the pipeline is full, all subsequent clock cycles yield valid output, with a constant lag of two clock cycles. |

Tip

N

#### Pipelining to Increase Throughput

You can use pipelining to increase throughput by compiling a single-cycle Timed Loop


 in a faster clock domain.

[IMAGE alt='image' src='GUID-460C1B51-8D8E-46E1-A74D-CA7564E0CA16-a5.png']

#### Non-Pipelined (40 MHz)

The top section of the illustration shows the execution timing of a non-pipelined


 loop. This code consists of three subVIs, each of which requires a propagation delay


 of 12.5 ns. The total propagation delay from subVI A to


 subVI C is 37.5 ns, which is too long to compile at 40


 MHz.

#### Pipelined (40 MHz)

The middle section of the illustration shows how pipelining the code reduces the


 propagation delay to 12.5 ns, allowing the loop to compile at 40 MHz.

#### Pipelined (80 MHz)

The bottom section of the illustration shows that the loop compiles at a clock rate


 as high as 80 MHz because the propagation delay of the pipelined loop is only 12.5


 ns.

Note

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Executing Code in Single-Cycle Timed Loops
- Filtering FPGA I/O Using Multiple Input Channels
- Introduction to FPGA Hardware Concepts
- Optimizing FPGA VIs for Speed and Size
- Implementing Multiple Clock Domains
- Understanding Timing Considerations for FPGA VIs
- Reducing Combinatorial Paths in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=optimizing-memory-usage-of-array-constants-fpga-module.html language=enus -->
## TOPIC 00124: Optimizing Memory Usage of Array Constants

- bundle_id: `labview-fpga-module`
- source_path: `optimizing-memory-usage-of-array-constants-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/optimizing-memory-usage-of-array-constants-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can optimize your FPGA application by specifying how LabVIEW implements array constants in memory. The default implementation for new array constants is Auto, which means that the compiler decides whether to implement an array constant in block memory, look-up tables, or flip-flops based on spec

### Optimizing Memory Usage of Array Constants

You can optimize your FPGA application by specifying how LabVIEW implements array constants in memory. The default


 implementation for new array constants is Auto, which means


 that the compiler decides whether to implement an array constant in block memory,


 look-up tables, or flip-flops based on specific coding patterns.

If you have difficulty compiling FPGA VIs with the Auto


 setting, instead choose a Block Memory or Look-Up


 Tables implementation for array constants. Consider choosing a block


 memory implementation for array constants unless you need the advantages of a


 different type of memory. Block memory does not consume FPGA resources and tends to


 compile at a high clock rate relative to other types of memory.

An array constant created in another context, such as on the development computer, is


 automatically set to Auto when opened in an FPGA VI. An array


 constant created in an FPGA VI maintains the selected memory implementation when


 moved into another context.

#### Restrictions for Implementing Array Constants in Block Memory or Look-Up


 Tables

To ensure you can implement an array constant in either block memory or look-up


 tables, you must meet the following criteria:

- You cannot wire an array constant to a top-level indicator. However you can


 separate the Replace Array


 Subset function from the Index Array


 function in a separate subVI.
- If you place an array constant in a single-cycle Timed Loop, you can include in


 the loop only one Replace Array Subset function and only one Index Array


 function. For each of these functions, you can access only a single index


 address in one loop iteration and you cannot resize the function or include


 multiple value writes/reads.
- For block memory implementations in a single-cycle Timed Loop, you must meet the


 following additional criteria:
  - You must pass an array constant through a


 Feedback Node that you configure to globally initialize when the VI compiles or


 loads and to ignore initialization if the FPGA VI resets. To globally initialize a Feedback Node, right-click


 the initializer terminal and select Globally


 Initialize»Initialize On Compile Or Load . To configure


 the Feedback Node to ignore initialization, place a checkmark in the


 Ignore FPGA reset method checkbox on the


 FPGA Implementation page of the Feedback Node


 Properties dialog box.
  - You must


 place Feedback Nodes after read and write operations.
- For look-up table implementations within a single-cycle Timed Loop, you must


 also wire an array constant to a shift register or a Feedback Node.

Note

#### Coding Patterns for Array Constant Memory Implementations

Use the following FPGA VI patterns to help you ensure that an array constant uses the


 memory type that you selected. Conversely, if an FPGA VI does not compile, use the


 patterns below to help you determine why it failed.

Note

#### Coding Examples of Array Constants in Single-Cycle Timed


 Loops

#### Block Memory Implementations

You can implement an array constant in block memory if your coding patterns resemble


 the following examples.

#### RAM Pattern

In the following coding pattern, notice that a Feedback Node appears after the read


 performed by Index Array and after the write performed by Replace Array Subset. This


 pattern compiles because it satisfies the requirement of only one read and one write


 with the required Feedback Nodes.

[IMAGE alt='image' src='GUID-BB7BA640-9DA9-4C5C-BCEE-FE7043362917-a5.png']

#### ROM Pattern

In the following coding pattern, notice that a Feedback Node is required after the


 read performed by Index Array.

[IMAGE alt='image' src='GUID-C5276C0F-EA91-4480-9E69-3ACCB0FD1043-a5.png']

#### Look-Up Table Implementations

You can implement an array constant in look-up tables if your coding patterns


 resemble the following examples.

#### RAM Pattern

In the following coding pattern, notice that a Feedback Node is not required after


 the read performed by Index Array when placed in a single-cycle Timed Loop. Also


 notice that the required Feedback Node is wired to the array constant.

[IMAGE alt='image' src='GUID-89427A13-5B1C-4BA6-A6E9-90C0FAE7C6DB-a5.png']

#### ROM Pattern

In the following coding pattern, notice that a Feedback Node is not required after


 the read performed by Index Array.

[IMAGE alt='image' src='GUID-FD012DE7-7B9C-4E30-BCF1-F9F5CED4E73A-a5.png']

#### Coding Examples of Array Constants outside of Single-Cycle Timed Loops

If your code resembles the following patterns, you can implement an array constant in


 either block memory or look-up tables.

#### RAM Pattern

The following coding pattern allows only one write performed by Replace Array Subset,


 followed by one read performed by Index Array.

[IMAGE alt='image' src='GUID-9BAB6A30-186E-4DF9-95DD-5CA88793B1EB-a5.png']

#### ROM Pattern

The following coding pattern allows unlimited reads performed by Index Array and


 requires no Feedback Node.

[IMAGE alt='image' src='GUID-9F8E2CC9-33EB-41DA-B6B6-877BACF00103-a5.png']

Parent topic:

Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=passing-data-between-component-level-ip-and-vis-fpga-module.html language=enus -->
## TOPIC 00125: Passing Data between Component-Level IP and VIs

- bundle_id: `labview-fpga-module`
- source_path: `passing-data-between-component-level-ip-and-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/passing-data-between-component-level-ip-and-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you add CLIP to a LabVIEW project, the FPGA Module adds the CLIP I/O to the LabVIEW project. You can read from or write to the I/O using an FPGA I/O Node in an FPGA VI. By default, CLIP signals use synchronization registers. Each synchronization register adds a delay of a clock cycle before the

### Passing Data between Component-Level IP and
 VIs

When you add CLIP to a LabVIEW project, the FPGA Module adds the CLIP I/O to the


 LabVIEW project. You can read from or write to the I/O using an FPGA


 I/O Node in an FPGA VI.

By default, CLIP signals use synchronization registers. Each synchronization register


 adds a delay of a clock cycle before the VHDL code receives the value from the FPGA


 I/O Node. If the CLIP already includes flip-flops on the signals that go to or from


 the FPGA VI, you can configure the CLIP signals in LabVIEW to not use


 synchronization registers. In the Advanced


 Code Generation page of the FPGA I/O


 Properties dialog box, set the Number of Synchronizing


 Registers for Output Data and Number of Synchronizing


 Registers for Output Enable parameters to 0. If the CLIP runs in the


 same clock domain as the FPGA VI, you do not need to include flip-flops in the CLIP


 or synchronization registers in LabVIEW.

When you run the FPGA VI, the FPGA Module compiles the FPGA VI and all instantiated


 CLIP into the FPGA bitstream.

Refer to the CLIP Tutorial, Part 4: Passing Data between CLIP and VIs for an example


 of passing data between CLIP and VIs.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- Adding Component-Level IP to a Project
- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- CLIP Tutorial, Part 4: Passing Data between CLIP and VIs
- Using VHDL Code as Component-Level IP

<!--NI_TOPIC bundle=labview-fpga-module path=performing-actions-on-fpga-io-and-fpga-targets-fpga-module.html language=enus -->
## TOPIC 00126: Performing Actions on FPGA I/O and FPGA Targets

- bundle_id: `labview-fpga-module`
- source_path: `performing-actions-on-fpga-io-and-fpga-targets-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/performing-actions-on-fpga-io-and-fpga-targets-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use FPGA I/O Method Nodes to invoke methods, or actions, on the FPGA I/O items and C Series modules present. In some cases, you also can invoke methods on the FPGA target itself. The available methods depend on the FPGA target and the FPGA I/O item or C Series module you select. Complete the

### Performing Actions on FPGA I/O and FPGA
 Targets

You can use FPGA I/O Method Nodes to invoke methods, or actions, on the FPGA I/O items and C Series modules present. In some cases, you also can


 invoke methods on the FPGA target itself. The available methods depend on the FPGA


 target and the FPGA I/O item or C Series module you select.

Complete the following steps to create and configure an FPGA I/O Method Node.

1. Add an FPGA I/O Method Node to the block diagram.
2. Right-click the FPGA I/O Method Node and select Select


 Item from the shortcut menu. The Select


 Item menu displays the FPGA target as well as the FPGA I/O items


 and C Series modules present in the Project Explorer 


 window under the FPGA target. Select the item you want to use. Tip Alternatively, you can write reusable code by wiring an FPGA I/O control to the FPGA I/O


 In input of the FPGA I/O Method Node.
3. Right-click the FPGA I/O Method Node and select Select


 Method from the shortcut menu to select a method to which you


 want the FPGA I/O item assigned. LabVIEW displays the methods available for the


 FPGA target in the Select Method menu. LabVIEW displays


 No Methods Available in the shortcut menu if the FPGA


 target does not support methods for the item you select. Refer to the specific


 target hardware documentation for information about the


 methods the FPGA target supports. Tip You also can click the FPGA


 I/O Method Node and use the shortcut menu to select methods available for


 the FPGA target.
4. After you select a method from the shortcut menu, LabVIEW displays the method


 and the terminals for that method in the FPGA I/O Method Node. Wire the


 terminals that you need.

Tip

Parent topic:

Using FPGA I/O

Related concepts:

- Creating FPGA I/O Items

<!--NI_TOPIC bundle=labview-fpga-module path=performing-io-using-case-structures-in-sctls-fpga-module.html language=enus -->
## TOPIC 00127: Performing I/O Using Case Structures in SCTLs

- bundle_id: `labview-fpga-module`
- source_path: `performing-io-using-case-structures-in-sctls-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/performing-io-using-case-structures-in-sctls-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a Case structure inside a single-cycle Timed Loop (SCTL) to perform I/O for different cases or states of the application. This state machine architecture runs at the rate of the single-cycle Timed Loop, and the state transitions occur at a frequency that is less than the frequency of the

### Performing I/O Using Case Structures in SCTLs

You can use a Case structure inside a single-cycle Timed


 Loop (SCTL) to perform I/O for different cases or states of the


 application. This state machine architecture runs at the rate of the single-cycle


 Timed Loop, and the state transitions occur at a frequency that is less than the


 frequency of the loop.

When you use a Case structure inside a single-cycle Timed Loop, the combinatorial


 logic delay required to evaluate the case selector is proportional to the width of


 the selector input data type and the number of cases. The combinatorial logic delay


 introduced by output tunnels is proportional to the number of cases.

LabVIEW executes all cases in the Case structure every clock cycle, and then uses a


 multiplexing protocol to determine the output. To avoid unexpected behavior when


 using Case structures with digital I/O inside single-cycle Timed Loops, you need to


 understand the way LabVIEW synchronizes I/O in a single-cycle Timed Loop.

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Synchronizing I/O in Single-Cycle Timed Loops

<!--NI_TOPIC bundle=labview-fpga-module path=placing-the-high-throughput-math-functions-in-a-single-cycle-timed-loop-fpga-module.html language=enus -->
## TOPIC 00128: Placing the High Throughput Math Functions in a Single-Cycle Timed Loop

- bundle_id: `labview-fpga-module`
- source_path: `placing-the-high-throughput-math-functions-in-a-single-cycle-timed-loop-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/placing-the-high-throughput-math-functions-in-a-single-cycle-timed-loop-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can place all High Throughput Math functions inside a single-cycle Timed Loop. However, be aware of the following caveats in this situation: Most High Throughput Math functions are multi-cycle, which means these functions take more than one cycle to return a valid result. If you place a multi-cy

### Placing the High Throughput Math Functions in
 a Single-Cycle Timed Loop

You can place all High Throughput Math functions inside a single-cycle Timed



 Loop. However, be aware of the following caveats in this situation:

- Most High Throughput Math functions are multi-cycle, which means these functions take more than one cycle to



 return a valid result. If you place a multi-cycle High Throughput Math function



 inside a single-cycle Timed Loop, this function does not return a valid value



 during every clock cycle. The throughput rate of the function and



 the values of the handshaking terminals determine the clock cycles during which this



 function produces a valid value.
- If you place several High Throughput Math functions inside a single-cycle Timed



 Loop, the combinatorial path might become too long and cause timing violations



 when you compile the FPGA VI. For this reason, the High Throughput Math



 functions provide ways to reduce the length of the



 combinatorial path.

#### Single-Cycle versus Multi-Cycle Functions

The High Throughput Add, Subtract, and To



 Fixed-Point functions are single-cycle functions. These functions execute



 in a single FPGA clock cycle. All other High Throughput



 Math functions are multi-cycle functions. These functions need more than



 one clock cycle to execute. If you place several multi-cycle functions in a



 single-cycle Timed Loop, the combinatorial path might become too long to execute in a single clock cycle.

#### Achieving a High Throughput Rate

For a multi-cycle High Throughput



 Math function in a single-cycle Timed Loop, you use the



 Throughput control, located in the configuration dialog



 box of that function, to specify the throughput rate you want the function to



 achieve. The throughput rate, in cycles/sample, is the minimum number of FPGA clock



 cycles that must elapse before this function can receive valid input data.



 Therefore, smaller values of the Throughput control mean the



 function can execute faster, because fewer clock cycles must elapse before the



 function is ready to receive valid input data.

Note

Throughput

1 cycle / sample

To demonstrate the importance of the Throughput control,



 consider three multi-cycle High Throughput Math functions connected by handshaking terminals. Within this series of three



 connected functions, the slowest throughput rate in that series (that is, the



 Throughput control with the highest value) is the fastest



 throughput rate that all connected functions can achieve. This limitation is true



 for each independent series of connected functions in a single-cycle Timed Loop.

Note

Throughput

Throughput

>1 call / sample

#### Handshaking

Although multi-cycle High Throughput



 Math functions execute during every clock cycle of a single-cycle Timed Loop, these



 functions do not return valid values during every cycle. You can configure these



 functions to display four handshaking



 terminals on the function icon. You use these terminals to determine when



 the following actions occur:

- The function discards data from upstream functions.
- The function accepts data from upstream functions.
- Downstream functions discard data from the function.
- Downstream functions accept data from the function.

Note

Inside single-cycle



 Timed Loop

Register



 outputs

#### Reducing the Length of the Combinatorial Path

If you place several High Throughput Math functions inside a single-cycle Timed



 Loop, the length of the combinatorial path can prevent the FPGA VI from compiling at the



 necessary clock rate. In this situation, the Compilation



 Status window returns an error when you compile the FPGA VI. You can



 avoid these errors by increasing the



 number of pipelining stages or by adding input and/or output registers to



 the function.

#### Increasing the Number of Pipelining Stages

You can reduce the length of the combinatorial path by placing the High Throughput Complex Multiply function or the High Throughput



 Multiply function inside a single-cycle Timed Loop and specify a large



 Number of pipelining stages. When you specify a large



 Number of pipelining stages, LabVIEW increases the chance



 that the function can compile at the necessary clock rate.

#### Adding Input and Output Registers

You also can reduce the length of the combinatorial path by adding registers for the inputs and/or outputs of a function.



 Adding registers can prevent compilation errors. However, each set of registers also



 increases the latency of the function by one cycle, which means you must wait an



 extra cycle to receive a valid output value.

Note

The following figure shows how data flows through a function that contains these



 internal registers.

[IMAGE alt='image' src='GUID-2B9A173A-C646-43E7-A7D0-F37B5914E71C-a5.png']

Use the Registers section of a configuration dialog box to add



 input and/or output registers.

Note

Parent topic:

Using the High Throughput Math Functions

Related concepts:

- Reducing Combinatorial Paths in FPGA VIs
- Using the High Throughput Math Functions

<!--NI_TOPIC bundle=labview-fpga-module path=preparing-ip-for-use-with-the-ip-integration-node-fpga-module.html language=enus -->
## TOPIC 00129: Preparing IP for Use with the IP Integration Node

- bundle_id: `labview-fpga-module`
- source_path: `preparing-ip-for-use-with-the-ip-integration-node-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/preparing-ip-for-use-with-the-ip-integration-node-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following tables describe recommendations and requirements for using IP with the IP Integration Node. Recommendations for All IP The following recommendations apply to all IP you use with the IP Integration Node. Recommendation Details Use VHDL. The IP Integration Node is designed to work best w

### Preparing IP for Use with the IP Integration
 Node

The following tables describe recommendations and requirements for using IP with the



 IP



 Integration Node.

#### Recommendations for All IP

The following recommendations apply to all IP you use with the IP Integration



 Node.

|  | Recommendation | Details |
| --- | --- | --- |
|  | Use VHDL. | The IP Integration Node is designed to work best with VHDL. Using Verilog limits the available simulation options. To integrate Verilog code, first compile the code into a netlist file. You then can use this file with the IP Integration Node. |
|  | Validate the IP outside of LabVIEW. | The IP Integration Node is not a debugging or testing environment. Before integrating the IP into the IP Integration Node, NI recommends validating IP by synthesizing it using the Xilinx compilation tools first. You also can create a test bench in a third-party simulation tool to ensure the IP is robust. |
|  | Synchronize IP output ports to the rising edge of the single-cycle Timed Loop clock. | Synchronizing output ports to the rising edge of the single-cycle Timed Loop clock ensures that simulating the FPGA VI produces the same results as executing the VI on an FPGA target. |

#### Requirements for All IP

The following requirements apply to all IP you use with the IP Integration Node.

Note

#### Recommendations for IP that Contains Sequential Logic

Sequential logic is logic that uses one or more FPGA logic elements, such as



 flip-flops, to store its state from one clock cycle to the next. Examine the IP to



 determine whether it contains any sequential logic. If it does, the following



 recommendations apply to the IP. If the IP does not contain any sequential logic,



 the IP is combinatorial.

Note

#### Recommendation for IP that Contains Only Combinatorial Logic

Combinatorial logic is logic that does not store its state, that is, logic that is



 not sequential. If the IP does not



 contain any sequential logic, the IP is combinatorial. Complete the following steps



 if the IP contains only combinatorial logic:

1. Double-click the IP Integration Node and navigate to the Clock and



 Enable Signals page. Note If the node is configured



 already, you can right-click the node and select Configure»Clock



 and Enable Signals from the shortcut menu.
2. In the Clock signal name pull-down list, select



 No clock signal .
3. Click the OK button to save changes and return to the



 block diagram.

The IP Integration Node now treats the IP as combinatorial.

Parent topic:

Using the IP Integration Node

<!--NI_TOPIC bundle=labview-fpga-module path=programming-fpgas-overview-fpga-module.html language=enus -->
## TOPIC 00130: Programming FPGAs Overview

- bundle_id: `labview-fpga-module`
- source_path: `programming-fpgas-overview-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/programming-fpgas-overview-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module is ideal for programming applications that require functionality such as the following: Custom I/O—You can modify digital and analog lines with custom counters, encoders, and pulse width modulators (PWMs). Onboard decision making—You can make control, digital filtering, and B

### Programming FPGAs Overview

The LabVIEW FPGA Module is ideal for programming applications that require


 functionality such as the following:

- Custom I/O —You can modify digital and analog lines with


 custom counters, encoders, and pulse width modulators (PWMs).
- Onboard decision making —You can make control, digital


 filtering, and Boolean decisions on the target.
- Resource synchronization —Applications run with the


 precise timing of FPGA target resources, such as analog input (AI), analog


 output (AO), digital input and output (DIO), counters, and PWMs. You also can


 synchronize applications among multiple FPGA targets.
- Parallel execution —Independent portions of the block


 diagram can execute in parallel on the FPGA. For example, multiple independent


 While Loops on a block diagram each run simultaneously on


 independent portions of the FPGA. Adding additional independent loops does not


 affect the performance of existing loops.
- Independent and deterministic execution —FPGA VIs continue


 to run even if the computer that controls and monitors the FPGA target


 crashes.

#### Programming FPGAs with LabVIEW

The following outline provides an overview of steps involved for programming your FPGA target.
 The list is not a complete set of instructions. The *LabVIEW
 Documentation* includes topics to help you with the specifics of
 developing FPGA applications.

1. Understand the hardware capabilities of your target —Refer


 to the specific FPGA target or chassis hardware


 documentation for information about the capabilities and


 functionality of your FPGA and target.
2. Create an FPGA project for your application —You must


 create a LabVIEW project with an FPGA target before you can begin developing FPGA applications.
3. Create the FPGA VI —You can create FPGA VIs from scratch or get started with an example VI. Use


 the NI Example Finder to find example VIs for your target.
4. (Optional) Create a host VI —Host VIs run on an RT target


 or a PC and control and monitor FPGA VIs.
5. Compile and download the FPGA VI to the target —You must


 compile the FPGA VI before you can download and run it on an FPGA


 target.

Related concepts:

- What is the FPGA Module?
- Introduction to FPGA Applications and Projects
- Communicating with FPGA Targets from a Host Computer

<!--NI_TOPIC bundle=labview-fpga-module path=reading-dma-fifos-from-host-vis-fpga-interface.html language=enus -->
## TOPIC 00131: Reading DMA FIFOs from Host VIs

- bundle_id: `labview-fpga-module`
- source_path: `reading-dma-fifos-from-host-vis-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reading-dma-fifos-from-host-vis-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to read a DMA FIFO from a host VI. Open a reference to an FPGA VI or bitfile. The FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you want to open a reference to an FPGA VI. The host VI does not need to be in a project if you open a reference to

### Reading DMA FIFOs from Host VIs

Complete the following steps to read a DMA FIFO from a host VI.

1. Open a reference to an FPGA VI or bitfile. Note The



 FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you



 want to open a reference to an FPGA VI. The host VI does not need to be in a



 project if you open a reference to a bitfile. If you open a reference to an



 FPGA VI, the project must include a DMA FIFO item under the FPGA target and



 the FPGA VI must include a FIFO Method Node configured with the Write method on the block diagram that writes to the DMA FIFO



 item.
2. Add an Invoke Method function to the block diagram of the



 host VI in the data flow where you want the host VI to read the DMA FIFO. Make



 sure the host VI runs the FPGA VI before you read the DMA FIFO. Wire the



 FPGA VI Reference In input.
3. Click the Invoke Method function and select



 FIFO»Read from the shortcut menu,



 where FIFO is the name of the FIFO



 item in the project. Wire the inputs and outputs as needed.
4. Add the Close FPGA VI Reference function to the block



 diagram.
5. Wire the FPGA VI Reference Out output on the Invoke Node



 to the FPGA VI Reference In input on the Close FPGA VI



 Reference function.

Note

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=reading-fpga-vi-indicators-fpga-interface.html language=enus -->
## TOPIC 00132: Reading FPGA VI Indicators

- bundle_id: `labview-fpga-module`
- source_path: `reading-fpga-vi-indicators-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reading-fpga-vi-indicators-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to read an indicator in an FPGA VI from a host VI. Open a reference to the FPGA VI or bitfile. The FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you want to open a reference to an FPGA VI. The host VI does not need to be in a project if you op

### Reading FPGA VI Indicators

Complete the following steps to read an indicator in an FPGA VI from a host VI.

1. Open a reference to the FPGA VI or bitfile. Note The


 FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you


 want to open a reference to an FPGA VI. The host VI does not need to be in a


 project if you open a reference to a bitfile.
2. Add the Read/Write Control function to the block diagram.


 Notice that the Read/Write Control function contains one


 Unselected input.
3. Wire the FPGA VI Reference Out parameter of the Open FPGA VI Reference function or the


 Bitfile reference out parameter of the Open Dynamic Bitfile Reference function to the


 FPGA VI Reference In parameter of the Read/Write


 Control function.
4. Click the Unselected input. The shortcut menu lists all


 front panel controls and indicators in the FPGA VI in the


 Controls submenu. Note If the FPGA VI


 is not saved, or does not have any controls or indicators, this list is


 empty.
5. Select an indicator available in the FPGA VI from the shortcut menu. Notice that


 the Unselected input changes to an output and reflects


 the name of the indicator in the FPGA VI.

To read more indicators in the FPGA VI, right-click the Read/Write Control function


 and select Add Element from the shortcut menu and then


 customize the output as described in the previous step. You also can click the


 bottom line of the Read/Write Control function with the Positioning tool and drag


 the line down to add more controls and indicators. The read and write operations


 execute sequentially from top to bottom. Also, if the FPGA VI has subVIs and you


 want to access controls and indicators on the subVI, you must wire the subVI


 controls and indicators to the controls and indicators of the FPGA VI that is used


 in the Open FPGA VI Reference function.

Note

Change to


 Read

Parent topic:

Transferring Data Using Front Panel Controls and Indicators

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=reducing-combinatorial-paths-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00133: Reducing Combinatorial Paths in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `reducing-combinatorial-paths-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reducing-combinatorial-paths-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Long combinatorial paths take more time to execute and limit the maximum clock rate of the clock domain. Long combinatorial paths are typically a problem in single-cycle Timed Loops because the logic between the input register and the output register must execute within one period of the clock rate

### Reducing Combinatorial Paths in FPGA VIs

Long combinatorial paths take more time to execute and limit the maximum


 clock rate of the clock domain.

Long combinatorial paths are typically a problem in single-cycle Timed


 Loops because the logic between the input register and the output


 register must execute within one period of the clock rate you specify. In the


 single-cycle Timed Loop, LabVIEW removes registers within and between components,


 which increases the length of the combinatorial path between registers. If the code


 in a combinatorial path cannot execute within a clock cycle, LabVIEW returns a


 timing violation in the Compilation


 Status window.

Note

To reduce the length of a combinatorial path, first simplify the logic as much as


 possible. Once you have reduced the logic to its simplest form, you can further


 reduce the length of a combinatorial path by dividing the logic into discrete steps


 and pipelining your design.

Note

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Executing Code in Single-Cycle Timed Loops
- Implementing Multiple Clock Domains
- Optimizing FPGA VIs for Speed and Size
- Understanding Timing Considerations for FPGA VIs
- Optimizing FPGA VIs Using Pipelining
- Placing the High Throughput Math Functions in a Single-Cycle Timed Loop

<!--NI_TOPIC bundle=labview-fpga-module path=reducing-memory-resource-usage-with-dual-port-read-access-fpga-module.html language=enus -->
## TOPIC 00134: Reducing Memory Resource Usage with Dual-Port Read Access

- bundle_id: `labview-fpga-module`
- source_path: `reducing-memory-resource-usage-with-dual-port-read-access-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reducing-memory-resource-usage-with-dual-port-read-access-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For some applications, you may be able to reduce the usage of block memory resources and/or improve execution time by configuring the memory for dual-port read access on the Interfaces page of the Memory Properties dialog box. The main advantage of dual-port read memory is that with two read ports,

### Reducing Memory Resource Usage with Dual-Port Read Access

For some applications, you may be able to reduce the usage of block memory resources


 and/or improve execution time by configuring the memory for dual-port read access on


 the Interfaces page of the Memory


 Properties dialog box.

The main advantage of dual-port read memory is that with two read ports, you can


 access data simultaneously from two different addresses. For example, if


 coefficients relate to the same sine or cosine function, you can save the function


 once in a memory block and use two addresses to read the different phases. The two


 Memory Method Nodes reading this memory can be within


 one structure, such as a single-cycle Timed Loop, or in different places in the FPGA


 VI.

Parent topic:

FPGA Memory Items

Related concepts:

- Optimizing FPGA VIs for Speed and Size
- Storing Data on an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=reducing-memory-resource-usage-with-dual-port-read-access-fpga-module_2.html language=enus -->
## TOPIC 00135: Reducing Memory Resource Usage with Dual-Port Read Access

- bundle_id: `labview-fpga-module`
- source_path: `reducing-memory-resource-usage-with-dual-port-read-access-fpga-module_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reducing-memory-resource-usage-with-dual-port-read-access-fpga-module_2.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For some applications, you may be able to reduce the usage of block memory resources and/or improve execution time by configuring the memory for dual-port read access on the Interfaces page of the Memory Properties dialog box. The main advantage of dual-port read memory is that with two read ports,

### Reducing Memory Resource Usage with Dual-Port Read Access

For some applications, you may be able to reduce the usage of block memory resources


 and/or improve execution time by configuring the memory for dual-port read access on


 the Interfaces page of the Memory


 Properties dialog box.

The main advantage of dual-port read memory is that with two read ports, you can


 access data simultaneously from two different addresses. For example, if


 coefficients relate to the same sine or cosine function, you can save the function


 once in a memory block and use two addresses to read the different phases. The two


 Memory Method Nodes reading this memory can be within


 one structure, such as a single-cycle Timed Loop, or in different places in the FPGA


 VI.

Parent topic:

Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=reducing-simulation-run-time-fpga-module.html language=enus -->
## TOPIC 00136: Reducing Simulation Run Time

- bundle_id: `labview-fpga-module`
- source_path: `reducing-simulation-run-time-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reducing-simulation-run-time-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all FPGA VIs are practical to simulate because the simulation software runs more slowly than FPGA hardware. Consider limiting the parts of the FPGA VI that you simulate to reduce simulation run time. You can try the following strategies to reduce simulation run time: Reduce the user-defined dela

### Reducing Simulation Run Time

Not all FPGA VIs are practical to simulate because the simulation software runs more


 slowly than FPGA hardware. Consider limiting the parts of the FPGA VI that you


 simulate to reduce simulation run time.

You can try the following strategies to reduce simulation run time:

- Reduce the user-defined delays in nodes such as the Discrete


 Delay Express VI and Zero-Order


 Hold VI.
- Reduce the execution rates of FPGA timing functions.

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

<!--NI_TOPIC bundle=labview-fpga-module path=removing-synthesis-files-fpga-module.html language=enus -->
## TOPIC 00137: Removing Synthesis Files

- bundle_id: `labview-fpga-module`
- source_path: `removing-synthesis-files-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/removing-synthesis-files-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to remove a synthesis file from the IP Source table. Select the file in the IP Source list. Click the Remove button:

### Removing Synthesis Files

Complete the following steps to remove a synthesis file from the IP


 Source table.

1. Select the file in the IP Source list.
2. Click the Remove button: [IMAGE alt='image' src='GUID-12C7619D-466F-4A42-91A6-8827B42FECDB-a5.png']

Parent topic:

Synthesis Files and Simulation

<!--NI_TOPIC bundle=labview-fpga-module path=reports-available-from-the-compilation-status-window-fpga-module.html language=enus -->
## TOPIC 00138: Reports Available from the Compilation Status Window

- bundle_id: `labview-fpga-module`
- source_path: `reports-available-from-the-compilation-status-window-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reports-available-from-the-compilation-status-window-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can read each report in the Compilation Status window after the report becomes available during the compilation of the FPGA VI. Use the information in the reports to determine whether the FPGA VI fits on the FPGA and meets timing constraints. The reports available in the Compilation Status windo

### Reports Available from the Compilation Status
 Window

You can read each report in the Compilation Status window after the report becomes
 available during the compilation of the FPGA VI. Use the information in the reports
 to determine whether the FPGA VI fits on the FPGA and meets timing constraints. The
 reports available in the Compilation Status window vary
 depending on your specific FPGA target.

Note

Throughput
 Conventions in FPGA-Based Systems

#### Summary Report Details

This report contains a summary of the generated bitfile and is available only when


 the compilation is complete. If the report contains timing errors, you can


 investigate the errors by clicking the Timing


 Violation Analysis button.

#### Configuration Report Details

This report displays project information and the Xilinx compiler configuration you


 specified in the Xilinx


 Options page of the build specification.

#### Estimated Device Utilization (Pre-Synthesis) Report Details

This report is available after LabVIEW estimates FPGA resource usage using the Xilinx tools. The availability


 of this report depends on your specific FPGA target. This report includes the


 following information:

- Device Utilization —Indicates the FPGA element, such as


 slices, flip-flops, LUTs, and blocks of RAM.
- Used —Indicates how many of the FPGA element the compiled


 FPGA VI uses.
- Total —Indicates the total number of FPGA elements in the


 FPGA.
- Percent —Indicates the percentage of the FPGA elements


 that the FPGA application uses. If Percent is greater


 than 100, a warning message alerts you that the estimated device utilization


 exceeds 100 percent. Depending on the FPGA VI and hardware, Xilinx still may be


 able to fit everything on the FPGA. However, you may want to optimize the FPGA VI.

#### Estimated Device Utilization Report Details

This report is available after the compile server completes the synthesizing step of


 the compilation process. This report contains a summary of


 the FPGA utilization as estimated during the synthesis of the FPGA VI. This report


 includes the following information:

- Device Utilization —Indicates the FPGA element, such as


 slices, flip-flops, LUTs, and blocks of RAM.
- Used —Indicates how many of the FPGA element the compiled


 FPGA VI uses.
- Total —Indicates the total number of FPGA elements in the


 FPGA.
- Percent —Indicates the percentage of the FPGA elements


 that the FPGA application uses. If Percent is greater


 than 100, a warning message alerts you that the estimated device utilization


 exceeds 100 percent. Depending on the FPGA VI and hardware, Xilinx still may be


 able to fit everything on the FPGA. However, you may want to stop the


 compilation and optimize the FPGA VI.

#### Final Device Utilization Report Details

This report is available after the compile server completes the mapping or placement


 step of the compilation process. This report contains a summary of


 the FPGA utilization, including the following information:

- Device Utilization —Indicates the FPGA element, such as


 slices, flip-flops, LUTs, and blocks of RAM.
- Used —Indicates how many of the FPGA element the compiled


 FPGA VI uses.
- Total —Indicates the total number of FPGA elements in the


 FPGA.
- Percent —Indicates the percentage of the FPGA elements


 that the FPGA application uses. If Percent is greater


 than 100, the compilation failed. You must optimize the FPGA VI for size.

#### Estimated Timing Report Details

This report is available after the compile server completes the mapping or placement


 step of the compilation process. This report contains a summary of


 the FPGA clocks, as estimated during the mapping or placement of the FPGA VI. This


 report includes the following information:

- Clocks —Indicates the FPGA clocks.
- Requested (MHz) —Indicates the clock rate, in megahertz,


 at which the FPGA VI or FPGA VI component must be able to run. Some FPGA VI


 components, such as Timed Loops, are visible on the block diagram, while others,


 such as CLIP, are not. If Requested (MHz) is greater than


 Maximum (MHz) , a warning message alerts you that the


 VI does not meet timing constraints. Depending on the FPGA VI and hardware,


 Xilinx may still be able to compile the FPGA VI such that it meets timing


 constraints. However, you may want to stop the compilation and optimize the FPGA VI.
- Maximum (MHz) —Indicates the theoretical maximum


 compilation rate, in megahertz, for the FPGA VI or FPGA VI component.

#### Final Timing Report Details

This report is available after the compile server completes the routing step of the


 compilation process. This report contains a summary of


 the FPGA clocks, including the following information:

- Clocks —Indicates the FPGA clocks.
- Requested (MHz) —Indicates the clock rate, in megahertz,


 at which the FPGA VI or FPGA VI component must be able to run. Some FPGA VI


 components, such as Timed Loops, are visible on the block diagram, while others,


 such as CLIP, are not. If Requested (MHz) is greater than


 Maximum (MHz) , the compilation fails. Click the


 Investigate Timing Violation button to analyze the


 timing violations.
- Maximum (MHz) —Indicates the theoretical maximum


 compilation rate, in megahertz, for the FPGA VI or FPGA VI component. For


 specific FPGA targets, the Xilinx compiler does not attempt to optimize if a


 design meets timing requirements.

#### Xilinx Log Report Details

This log file is available only after the compilation is complete. If you are


 familiar with Xilinx tools, you might be able to use this file to troubleshoot


 compilation failures. Click the Save button to save this


 information to a file.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Estimating FPGA Resource Usage without Compiling
- Throughput Conventions in FPGA-Based Systems

<!--NI_TOPIC bundle=labview-fpga-module path=retaining-the-precision-of-dsp48e-and-dsp48e1-function-terminals-fpga-module.html language=enus -->
## TOPIC 00139: Retaining the Precision of DSP48E and DSP48E1 Function Terminals

- bundle_id: `labview-fpga-module`
- source_path: `retaining-the-precision-of-dsp48e-and-dsp48e1-function-terminals-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/retaining-the-precision-of-dsp48e-and-dsp48e1-function-terminals-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To retain numerical precision in a DSP48E or DSP48E1 application, use the Fixed-Point Configuration page of the configuration dialog box to set the integer word lengths of the input and output terminals appropriately. LabVIEW keeps the word lengths of these terminals constant, which means the intege

### Retaining the Precision of DSP48E and DSP48E1 Function Terminals

To retain numerical precision in a DSP48E or DSP48E1 application, use the


 Fixed-Point Configuration page of the configuration


 dialog box to set the integer word lengths of the input and output terminals


 appropriately. LabVIEW keeps the word lengths of these terminals constant, which


 means the integer word lengths are the variables you can control.

LabVIEW groups certain function terminals together. These groups must maintain


 identical fixed point data types. The following table shows the terminals and word


 length in each group.

| Terminal(s) in Group | Word Length of Terminals |
| --- | --- |
| a, acin | When Configure for Arithmetic is selected on the Function page and a multiplier is used, the word length is 25 in direct mode and 30 in cascade mode. Otherwise, the word length is 30 with the following exceptions:On UltraScale targets, only the lower 27 bits feed into the multiplier.On non-UltraScale targets, only the lower 25 bits feed into the multiplier. |
| acout | 30 |
| b, bcin, bcout | 18 |
| c | 48 |
| p, pcin, pcout | 48 |
| (DSP48E1) d | 25 |

Note

www.xilinx.com

#### Retaining Precision for the a and b Terminals

NI recommends setting the integer word length of the a and


 b terminals to meet the following criteria:

- The fractional word length of these terminals, which is the word length minus


 the integer word length, is greater than or equal to the fractional word length


 of the data type wired to the terminal.
- The integer word length of the terminal is greater than or equal to the integer


 word length of the source.

For example, if you wire a <+/–,16,1> data type to the b


 terminal, that data type has a fractional word length of 15 bits. Because the word


 length of b is fixed at 18 bits, set the integer word length


 of b to 3, 2, or 1 bits. These settings satisfy the above


 criteria: the fractional word length is 15, 16, or 17 bits, and the integer word


 length of b is greater than or equal to the integer word


 length of the source.

If the integer word length is less than 1 bit or more than 3 bits, LabVIEW coerces


 the value to the b terminal, resulting in a loss of


 precision. A coercion dot appears on the input terminal to alert you


 to this situation.

#### Retaining Precision for Multipliers

To retain full precision in a DSP48E or DSP48E1 function configured as a multiplier


 p = a * b,


 set the fractional word length of p to the sum of the


 fractional word lengths of the a and b


 terminals.

Consider the following example:

- The data type of the source to a is <+/–,16,1>. The


 fractional word length is 15 bits.
- The data type of the source to b is <+/–,16,2>. The


 fractional word length is 14 bits.

The sum of the fractional word lengths is 29 bits. In this situation, NI recommends


 completing the following steps:

1. Set a to <+/–,30,15>. This setting matches the


 15-bit fractional word length of the source wired to this terminal.
2. Set b to <+/–,18,4>. This setting matches the


 14-bit fractional word length of the source wired to this terminal.
3. Set p to <+/–,48,19>. This setting matches the


 29-bit fractional word length of the a and


 b terminals combined.

#### Retaining Precision for Accumulators

To retain full precision in a DSP48E or DSP48E1 function configured as an accumulator


 p = p + c,


 set the fractional word length of p equal to the fractional


 word length of c. For example, if the data type of the source


 to c is <+/–,16,3>, the fractional word length of


 c is 13 bits. Set p to


 <+/–,48,35>.

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Viewing the Latencies of Data Paths in a DSP48E or DSP48E1 Function
- Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function

<!--NI_TOPIC bundle=labview-fpga-module path=returning-compile-time-resolvable-arrays-from-array-functions-fpga-module.html language=enus -->
## TOPIC 00140: Returning Compile Time Resolvable Arrays from Array Functions

- bundle_id: `labview-fpga-module`
- source_path: `returning-compile-time-resolvable-arrays-from-array-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/returning-compile-time-resolvable-arrays-from-array-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In FPGA VIs, you can only use array functions that return arrays that resolve to a single size at compile time. This might mean that certain properties of the array, such as its length or the indexes of the elements you read/write, must be constant values. You can either wire constant values directl

### Returning Compile Time Resolvable Arrays from Array Functions

In FPGA VIs, you can only use array functions that return arrays that resolve to a


 single size at compile time. This might mean that certain properties of the array,


 such as its length or the indexes of the elements you read/write, must be constant


 values. You can either wire constant values directly to array functions, or rely on


 value propagation through constant


 folding.

Note

The following Array functions can return arrays that resolve to a


 single size at compile time.

| Function | Required Constants |
| --- | --- |
| Array Subset | The index and length inputs must be constant. You also can make all inputs constant. |
| Build Array | You can use constant or non-constant inputs. |
| Cluster To Array | You can use constant or non-constant inputs. |
| Decimate 1D Array | You can use constant or non-constant inputs. |
| Delete From Array | The length and index inputs must be constant. You also can make all inputs constant. |
| Initialize Array | The element input can be non-constant. The dimension size input must be constant. You also can make all inputs constant. |
| Insert Into Array | The index input must be constant. You also can make all inputs constant. |
| Interleave 1D Arrays | You can use constant or non-constant inputs. |
| Replace Array Subset | You can use constant or non-constant inputs. |
| Reshape Array | The dimension size input must be constant. |
| Reverse 1D Array | You can use constant or non-constant inputs. |
| Rotate 1D Array | You can use constant or non-constant inputs. |
| Split 1D Array | The index input must be constant. You also can make all inputs constant. |

Parent topic:

Implementing Variable-Sized Arrays in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=reusing-fpga-objects-fpga-module.html language=enus -->
## TOPIC 00141: Reusing FPGA Objects

- bundle_id: `labview-fpga-module`
- source_path: `reusing-fpga-objects-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/reusing-fpga-objects-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can copy, cut, or paste an FPGA VI among multiple FPGA targets to create additional target-specific application instances of the FPGA VI. You also can copy, cut, and paste FPGA I/O items, FPGA clocks, register items, memory items, FIFOs, and handshake items among multiple FPGA targets in the Pro

### Reusing FPGA Objects

You can copy, cut, or paste an FPGA VI among multiple FPGA targets to create



 additional target-specific application instances of the FPGA VI. You also can copy,



 cut, and paste FPGA I/O items, FPGA clocks, register items, memory items, FIFOs, and



 handshake items among multiple FPGA targets in the Project



 Explorer window. A copy of the item appears in the Project



 Explorer window under the FPGA target you select. Support of FPGA



 items varies by FPGA target.

Tip

You also can create additional instances of FPGA VIs and copy FPGA items across LabVIEW



 projects. Open the projects you want to copy among and copy or drag the



 FPGA item from one project to another project.

#### Reusing FPGA VIs

You can use the same FPGA VI under multiple FPGA targets of the same or different



 classes, as long as the FPGA target supports all FPGA I/O items, FPGA clocks, or



 FPGA FIFOs used in the FPGA VI. Because FPGA VI features vary by FPGA target, you



 can compile and run the FPGA VI instance on some FPGA targets but not on others. If



 you copy an FPGA VI that uses FPGA I/O items, clocks, or FIFOs to an FPGA target,



 copy the additional items with the FPGA VI. Otherwise, the



 Run button of the FPGA VI appears broken and you cannot



 compile and run the VI.

Note

Synchronize with Other



 Application Instances

Save As

#### Reusing FPGA I/O Items

You can copy FPGA I/O items among multiple FPGA targets. If the new FPGA target does



 not support the I/O resource for which you configure the FPGA I/O item or if the I/O



 resource already is in use, the item appears with a white ! in a red circle in the



 Project Explorer window. Also, if you have an FPGA VI



 under the new FPGA target that includes an FPGA I/O Node on the block diagram using



 the unsupported FPGA I/O item, the Run button appears broken



 and you cannot compile or run the VI. If the FPGA I/O item is broken, right-click



 the FPGA I/O item in the Project Explorer window and select



 Select Resource from the shortcut menu to display the



 Select Resource dialog box. Select an I/O resource that



 the FPGA target supports from the Select Resource dialog box



 and click the OK button. You also can right-click the FPGA



 I/O item in the Project Explorer window and select



 Remove from the shortcut menu to remove the item from the



 project. You then must reconfigure the FPGA I/O Node.

#### Reusing FPGA Clocks

You can copy FPGA clocks among multiple FPGA targets. If the new FPGA



 target does not support the clock resource for which you configure the FPGA clock or



 if the clock resource already is in use, the FPGA clock appears with a white ! in a



 red circle in the Project



 Explorer window. Also, if you have an FPGA VI under the new FPGA target



 that includes a single-cycle Timed Loop on the block diagram using the unsupported



 FPGA clock, the Code



 Generation Errors window appears and displays an error if you attempt to



 compile and run the VI. If the FPGA clock is broken, right-click the FPGA clock in



 the Project Explorer window and select



 Properties from the shortcut menu to display the FPGA Base Clock Properties dialog box or the FPGA Derived Clock Properties dialog box. If you copy an



 FPGA base clock, you can select a clock resource that the FPGA target supports from



 the Resource pull-down menu in the FPGA Base Clock



 Properties dialog box. If you copy an FPGA-derived clock, you can



 select a clock configuration that the FPGA targets supports by configuring the



 FPGA-derived clock. You also can right-click the FPGA clock in the



 Project Explorer window and select



 Remove from the shortcut menu to remove the FPGA clock



 from the project. You then must reconfigure the single-cycle Timed Loop using the



 new FPGA clock.

#### Reusing Register Items

You can copy register items among multiple FPGA targets.

#### Reusing FPGA Memory Items

You can copy memory items among multiple FPGA targets. If the new FPGA target does



 not support the memory item you copy, the Code



 Generation Errors window reports that the compilation failed when you



 compile the FPGA VI. You can right-click the memory item in the Project Explorer window and select



 Properties from the shortcut menu to display the Memory Properties dialog box. You then can configure the



 memory item and compile the FPGA VI again. You also can right-click the memory item



 in the Project Explorer window and select Remove



 from Project from the shortcut menu to remove the memory item from



 the project.

#### Reusing FPGA FIFOs

You can copy FPGA FIFOs among multiple FPGA targets. If the new FPGA target does not



 support the FPGA FIFO you copy, the Code



 Generation Errors or the Compilation



 Status window returns a report that the compilation failed when you



 compile the FPGA VI. You can right-click the FPGA FIFO in the Project Explorer window and select



 Properties from the shortcut menu to display the FIFO



 Properties dialog box. You then can configure the FPGA FIFO and compile



 the FPGA VI again. You also can right-click the FPGA FIFO in the Project



 Explorer window and select Remove from



 Project from the shortcut menu to remove the FPGA FIFO from the



 project.

#### Reusing Handshake Items

You can copy handshake items among multiple FPGA targets:

- VI-defined handshake items : Use VI-defined handshake



 items to create reentrant subVIs and avoid resource conflicts. If you configure



 a VI-defined handshake item in a reentrant FPGA VI, LabVIEW creates a separate



 copy of the handshake item for each instance of the VI.
- Target-scoped handshake items : Use target-scoped



 handshake items if you want the handshake item to be visible and configurable



 from the Project Explorer window. Target-scoped handshake



 items are available within any FPGA VI under the same target in the



 Project Explorer window.

#### Reusing CLIP Items

You can use the same CLIP between different FPGA targets. However, you cannot drag



 CLIP items between targets in the Project



 Explorer window. You must add the CLIP to the new target. If applicable,



 you also need to configure any I/O items associated with the CLIP in the same way



 you associated the I/O items in the original target.

Parent topic:

Creating FPGA VIs

Related concepts:

- Managing FPGA Applications in the Project Explorer Window

<!--NI_TOPIC bundle=labview-fpga-module path=running-fpga-vis-automatically-from-flash-memory-fpga-module.html language=enus -->
## TOPIC 00142: Running FPGA VIs Automatically from Flash Memory

- bundle_id: `labview-fpga-module`
- source_path: `running-fpga-vis-automatically-from-flash-memory-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/running-fpga-vis-automatically-from-flash-memory-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some FPGA targets have flash memory that can store FPGA VIs. Refer to the specific FPGA target hardware documentation for information about flash memory. Complete the following steps to automatically run an FPGA VI that is loaded from flash memory when you power on an FPGA target. Right-click and th

### Running FPGA VIs Automatically from Flash
 Memory

Some FPGA targets have flash memory that can store FPGA VIs. Refer to the specific FPGA target hardware documentation for information about flash memory.

Complete the following steps to automatically run an FPGA VI that is loaded from flash memory when you power on an FPGA target.

1. Right-click and the FPGA build specification you want to run in the Project


 Explorer window and select Properties 


 from the shortcut menu. The Compilation Properties dialog box appears.
2. On the Information page, place a checkmark in the Run when


 loaded to FPGA checkbox.
3. Click the OK button.
4. Configure the FPGA target to load the VI automatically when powered on.

Note

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Downloading an FPGA VI to the Flash Memory of an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=running-fpga-vis-on-the-host-fpga-module.html language=enus -->
## TOPIC 00143: Running FPGA VIs on the Host

- bundle_id: `labview-fpga-module`
- source_path: `running-fpga-vis-on-the-host-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/running-fpga-vis-on-the-host-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to run an FPGA VI on the host computer. Create a new project or open an existing project. Add an FPGA target to the project. Create a new VI or open an existing VI under the FPGA target. If an FPGA VI uses I/O variables, you cannot execute that FPGA VI on the host compu

### Running FPGA VIs on the Host

Complete the following steps to run an FPGA VI on the host computer.

1. Create a new project or open an existing project.
2. Add an FPGA target to the project.
3. Create a new VI or open an existing VI under the FPGA target. Note If an FPGA VI uses I/O variables, you cannot execute that FPGA VI on the


 host computer. If you place an I/O Variable node on the block diagram of an


 FPGA VI on the host computer, LabVIEW breaks the Run


 button.
4. Right-click the FPGA target in the Project Explorer 


 window and select Properties from the shortcut menu. The


 FPGA Target Properties dialog box appears.
5. Select Execution Mode from the


 Category list to display the Execution


 Mode page.
6. Select one of the following options:
  - Simulation —If you select this option, select


 Use Simulated I/O or Use Custom VI


 for FPGA I/O from the pull-down menu. Note Selecting Use Simulated I/O is not


 compatible with CLIP.
  - Simulation with Real I/O —Some FPGA targets do not


 support this option.
7. If you select Use Custom VI for FPGA I/O in the previous


 step, specify the path to the custom VI or create a New VI from


 Template using the VI Path control.


 LabVIEW calls the VI you specify whenever FPGA I/O Nodes, FPGA I/O Property


 Nodes, or FPGA I/O Method Nodes execute on the block diagram on the FPGA


 VI.
8. Click the OK button.
9. Click the Run button on the FPGA VI.

|  | Tip You also can change where the FPGA VI executes by right-clicking the FPGA target in the Project Explorer window and selecting an option from the Select Execution Mode shortcut menu. |
| --- | --- |

#### Considerations for Running FPGA VIs on the Host Computer

You can use a host VI to communicate with an FPGA VI executing in simulation mode


 using simulated I/O. However, you must be aware of special considerations when using


 the host VI.

If you include a digital I/O resource in a single-cycle Timed Loop, each


 synchronization register introduces a delay corresponding to one iteration of the


 single-cycle Timed Loop. In some cases, delays outside the FPGA may be significant


 for the system. If accurate modeling of the delays between the LabVIEW diagram and


 the FPGA is important for testing the logic of the application by executing the FPGA


 VI on the host computer, delay simulation data for the I/O by the number of calls to


 the I/O node, equivalent to the number of synchronization registers.

#### Verifying the FPGA VI Compiles for the FPGA

When you debug an FPGA VI using test benches, you execute the FPGA VI on the host


 computer multiple times. However, FPGA VIs are subject to special considerations


 when compiled for an FPGA target. In addition to testing the logic of the FPGA VI,


 you must consider whether the FPGA VI compiles with all of the constraints enforced


 by the FPGA design. Design considerations include whether the application utilizes


 more FPGA resources than available and whether the logic meets timing constraints


 set by the FPGA clocks.

NI recommends that you compile the FPGA VI periodically to make sure the FPGA VI


 satisfies all of these requirements. In addition, you can generate intermediate


 files and estimate FPGA resource utilization using commands in the build


 specification shortcut menu. The generation of intermediate files is a relatively


 short step in the process, and it often reports a large percentage of errors.

Parent topic:

Debugging FPGA VIs Using Simulation Mode

<!--NI_TOPIC bundle=labview-fpga-module path=scheduling-timing-using-handshaking-signals-fpga-module.html language=enus -->
## TOPIC 00144: Scheduling Timing Using Handshaking Signals

- bundle_id: `labview-fpga-module`
- source_path: `scheduling-timing-using-handshaking-signals-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/scheduling-timing-using-handshaking-signals-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Handshaking refers to communication between two nodes that establishes the parameters for continued communication. For a given block diagram node F in a single-cycle Timed Loop, handshaking determines when the following actions occur: F discards data from upstream nodes. An upstream node is any node

### Scheduling Timing Using Handshaking Signals

Handshaking

F

- F discards data from upstream nodes. An upstream
 node is any node that sends data to F .
- F accepts data from upstream nodes.
- Downstream nodes discard data from F . A
 downstream node is any node that receives data from
 F .
- Downstream nodes accept data from F .

In a single-cycle Timed Loop, handshaking is necessary because multi-cycle nodes need
 more than one cycle to compute valid data, but the single-cycle Timed Loop forces
 these nodes to return data every clock cycle. Therefore, multi-cycle nodes do not
 return valid data every clock cycle. To ensure the numerical accuracy of an
 algorithm, nodes that depend on this data must know whether the data is invalid or
 valid.

Note

Throughput Conventions in FPGA-Based Systems

#### Latency and Throughput
 Definitions

L

f

5 cycles

5 cycles

TRUE

T

f

T

f

T

f

- Nodes with high latency require careful alignment of readiness signals.
- Nodes with high throughput values can become bottlenecks in a chain of
 connected nodes.

#### Handshaking Protocol
 Terminals

input valid

TRUE

output valid

output valid

FALSE

ready for output

TRUE

ready for output

ready for input

TRUE

ready for output

FALSE

output valid

FALSE

ready for input

FALSE

For step‑by‑step wiring instructions with a worked diagram, see *Wiring
 Single‑Input Nodes Using Handshaking*.

Notice

- Setting input valid to TRUE when
 ready for input is FALSE
- Ignoring ready for output

#### Ensuring that Multi-Input Nodes
 Use Valid Data

Some nodes (for example, High Throughput Add) have multiple data inputs, such as
 x and y. In a single‑cycle Timed Loop,
 you must ensure that all required inputs are valid on the same clock cycle. If one
 input is valid and another input is invalid, the node processes the data with mixed
 validity. This action can lead to incorrect results.

- Sum the latencies of all nodes that feed data forward to
 x .
- Sum the latencies of all nodes that feed data forward to
 y .
- Make the two totals equal by inserting Feedback Nodes (or additional
 pipelining) on the shorter path.

- x valid
- ready for x
- y valid
- ready for y

Note

labview\examples\<target_type>\FPGA Fundamentals\FPGA Math and
 Analysis\High-Throughput Math\Vector Normalization\Vector
 Normalization.lvproj

Note

<target_type>

Note

input valid

input valid

TRUE

#### Nodes that Support Handshaking
 Terminals

- FFT Express VI
- Handshake Method Node
- High Throughput Math functions, except for the Basic Elements functions
- Linear Algebra functions
- Memory Method Node when configured for DRAM
- FIFO Method Node with the handshaking interface enabled
- Rational Resampler Express VI
- Scaled Window Express VI
- User-Controlled I/O Sampling functions

#### Nodes that Support Multi-channel
 Handshaking

- Rational Resampler Express VI

- The first valid data point goes to channel
 0 .
- The second valid data point goes to channel
 1 .
- The pattern continues for subsequent channels.

input valid

FALSE

Figure 1.

[IMAGE alt='Timing diagram showing clock, input valid, and output data signals.' src='GUID-BC891D50-2FD1-4CA3-B5F4-BD385BAC4E04-a5.png']

Figure 1.

clock

input valid

output data

d0

d1

d2

input valid

FALSE

TRUE

#### Determining the Fastest Allowable
 Throughput Rate

For a series of connected nodes within a single-cycle Timed Loop, the minimum number
 of clock cycles required determines the fastest throughput rate. This is the point
 at which you can send more data to the series. The fastest throughput rate is equal
 to the throughput rate of the slowest node (that is, the node with the highest value
 of its Throughput control) in the series. This node is the
 bottleneck for all nodes in the series. If the system sends data to this series at a
 rate that is faster than this fastest rate (that is, the system waits fewer than the
 fewest number of allowable clock cycles before sending data to the series), LabVIEW
 discards data points.

1. Check the throughput rate of each node individually.
2. Look at the Throughput control for each node to
 determine its rate.

Context Help

Throughput

For example, consider a series of nodes. The slowest node has a throughput rate of
 32 cycles/sample. The clock rate of the FPGA
 target is 40 MHz. The input sample rate is 2 MS/s. The the system calculates the system
 throughput rate by dividing the clock rate by the input sample rate. In this case,
 the calculation is 40,000,000 cycles/2,000,000
 samples. This results in a throughput rate of 20
 cycles/sample. In this situation, the system sends data to the series every
 20 cycles, which is faster than the fastest
 throughput rate of 32 cycles. This difference causes
 LabVIEW to discard data points.

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Filtering FPGA I/O Using Multiple Input Channels
- Optimizing FPGA VIs for Speed and Size
- Understanding Timing Considerations for FPGA VIs
- Using DRAM
- Interfacing AXI IP in FPGA VIs
- Throughput Conventions in FPGA-Based Systems

Related tasks:

- Wiring Single-Input Nodes Using Handshaking

<!--NI_TOPIC bundle=labview-fpga-module path=selecting-a-top-level-clock-for-an-fpga-target-fpga-module.html language=enus -->
## TOPIC 00145: Selecting a Top-Level Clock for an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `selecting-a-top-level-clock-for-an-fpga-target-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/selecting-a-top-level-clock-for-an-fpga-target-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define a top-level clock for an FPGA target in the Project Explorer window. The top-level clock is the global clock that the FPGA VI uses outside a single-cycle Timed Loop. The FPGA target uses one of the FPGA base clocks by default. Complete the following steps to select a top-level clock f

### Selecting a Top-Level Clock for an FPGA Target

You can define a top-level clock for an FPGA target in the Project


 Explorer window. The top-level clock is the global clock that the FPGA VI


 uses outside a single-cycle Timed Loop. The FPGA target uses one of the


 FPGA base clocks by default. Complete the following steps to select a top-level


 clock for an FPGA target.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. If the FPGA target you use does not automatically add an FPGA base clock to the


 Project Explorer window, add the FPGA base clock. If you want to use the FPGA base clock as


 the timing source for the top-level clock, skip the following step.
4. (Optional) Create an FPGA-derived clock.
5. Right-click the FPGA target in the Project Explorer 


 window and select Properties from the shortcut menu. The


 FPGA


 Target Properties dialog box appears.
6. Select Top-Level Clock in the


 Category list.
7. Select Default if you want to use the default FPGA target


 clock. Select Select Configured Clock and a configured


 clock from the Configured Clock list if you want to use a


 clock you configured.
8. Click the OK button.

Note

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Adding an FPGA Base Clock to a LabVIEW Project
- Controlling the FPGA VI Execution Rate
- Creating FPGA-Derived Clocks
- Adding FPGA Targets to a LabVIEW Project
- Selecting an FPGA Clock as the Timing Source for SCTLs

<!--NI_TOPIC bundle=labview-fpga-module path=selecting-an-fpga-clock-as-the-timing-source-for-sctls-fpga-module.html language=enus -->
## TOPIC 00146: Selecting an FPGA Clock as the Timing Source for SCTLs

- bundle_id: `labview-fpga-module`
- source_path: `selecting-an-fpga-clock-as-the-timing-source-for-sctls-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/selecting-an-fpga-clock-as-the-timing-source-for-sctls-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to select an FPGA base clock or derived clock as the timing source for a single-cycle Timed Loop (SCTL) in an FPGA VI. The SCTL uses the top-level clock of the FPGA target by default. Support of the single-cycle Timed Loop varies by FPGA target. Refer to the specific F

### Selecting an FPGA Clock as the Timing Source for SCTLs

Complete the following steps to select an FPGA base clock or derived clock as the timing source for a single-cycle Timed Loop (SCTL) in an FPGA VI. The SCTL uses the top-level clock of the FPGA target by default.

Note

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. If the FPGA target you use does not automatically add the FPGA base clock you


 want to the Project


 Explorer window, add the FPGA base clock. If you want to use the FPGA base clock as


 the timing source for the single-cycle Timed Loop, skip the following step.
4. (Optional) Create an FPGA-derived clock.
5. Create a new VI or open an existing VI under an FPGA target in the


 Project Explorer window.
6. Add a Timed Loop to the block diagram.
7. Select a clock by double-clicking the Input Node of the


 Timed Loop to display the Configure


 Timed Loop dialog box and selecting one of the following


 options: Alternatively, you can


 write reusable code by wiring an FPGA


 clock control to the Source Name input of the


 Timed Loop.
  - Top-Level Timing


 Source —Select this option if you want the Timed Loop to


 inherit the top-level timing source of the project it is in. You might


 use this option if you intend to reuse an FPGA VI on multiple FPGA


 targets.
  - Select Timing Source —Select this


 option if you want to use a timing source in the project other than the


 top-level clock. Then select a timing source from the


 Available Timing Source list. To use a clock


 that is not in the list, create a new base clock or create a new derived clock.

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Using FPGA Clocks and Timing
- Selecting a Top-Level Clock for an FPGA Target
- Adding FPGA Targets to a LabVIEW Project
- Adding an FPGA Base Clock to a LabVIEW Project
- Creating FPGA-Derived Clocks
- Adding Items to an FPGA Target in the Project Explorer Window

<!--NI_TOPIC bundle=labview-fpga-module path=setting-and-retrieving-properties-on-fpga-io-and-fpga-targets-fpga-module.html language=enus -->
## TOPIC 00147: Setting and Retrieving Properties on FPGA I/O and FPGA Targets

- bundle_id: `labview-fpga-module`
- source_path: `setting-and-retrieving-properties-on-fpga-io-and-fpga-targets-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/setting-and-retrieving-properties-on-fpga-io-and-fpga-targets-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use FPGA I/O Property Nodes to programmatically set and retrieve properties on FPGA I/O items and C Series modules in a LabVIEW project. In some cases, you also can set and retrieve properties on the FPGA target itself. The properties you can select are specific to the FPGA target and the I/

### Setting and Retrieving Properties on FPGA I/O
 and FPGA Targets

You can use FPGA I/O Property Nodes to programmatically set and retrieve properties


 on FPGA I/O items and C Series modules in a LabVIEW project. In some cases,


 you also can set and retrieve properties on the FPGA target itself. The properties


 you can select are specific to the FPGA target and the I/O resource that the FPGA


 I/O item is associated with in the Project


 Explorer window.

Complete the following steps to create and configure FPGA I/O Property Nodes.

1. Create a new VI or open an existing VI that is under an FPGA


 target.
2. (Optional) Add FPGA I/O items to the project.
3. Add an FPGA I/O Property Node to the block diagram.
4. Right-click the FPGA I/O Property Node and select Select


 Item from the shortcut menu. The Select


 Item menu displays the FPGA target as well as the FPGA I/O items


 and C Series modules present in the Project Explorer 


 window under the FPGA target. Select the item you want to use. Tip Alternatively, you can write reusable code by wiring an FPGA I/O control to the FPGA I/O


 In input of the FPGA I/O Property Node.
5. Right-click the Property terminal in the FPGA I/O


 Property Node and select Select Property from the


 shortcut menu to select a property you want to assign to the item. LabVIEW


 displays the properties available for the FPGA target in the Select


 Property menu. LabVIEW displays No Properties


 Available in the shortcut menu if the FPGA target does not


 support properties for the item you select. Refer to the specific FPGA target


 hardware documentation for information about the


 properties the FPGA target supports. Tip You also can click the


 FPGA I/O Property Node and use the shortcut menu to select properties


 available for the FPGA target.
6. (Optional) Add additional Property terminals in the FPGA


 I/O Property Node by right-clicking the node and selecting Add


 Element from the shortcut menu. You also can expand the FPGA I/O


 Property Node by clicking on the upper or lower edge of the node with the


 Positioning tool and dragging the edge up or down.

Tip

Parent topic:

Using FPGA I/O

Related concepts:

- Creating FPGA I/O Items
- Adding Items to an FPGA Target in the Project Explorer Window

<!--NI_TOPIC bundle=labview-fpga-module path=showing-and-hiding-the-terminals-of-a-dsp48e-or-dsp48e1-function-fpga-module.html language=enus -->
## TOPIC 00148: Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function

- bundle_id: `labview-fpga-module`
- source_path: `showing-and-hiding-the-terminals-of-a-dsp48e-or-dsp48e1-function-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/showing-and-hiding-the-terminals-of-a-dsp48e-or-dsp48e1-function-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you add a DSP48E or DSP48E1 function to the block diagram, LabVIEW shows only the a, b, c, and p terminals, where p is the output of the function and the other terminals are inputs. However, you can choose to show other terminals. Use the Terminals page of the configuration dialog box to speci

### Showing and Hiding the Terminals of a DSP48E or DSP48E1 Function

After you add a DSP48E or DSP48E1 function to the block diagram, LabVIEW shows only


 the a, b, c,


 and p terminals, where p is the output


 of the function and the other terminals are inputs. However, you can choose to show


 other terminals.

Use the Terminals page of the configuration dialog box to


 specify which block diagram terminals LabVIEW shows. The following illustrations


 show the names and data types of all terminals for both functions.

|  |  |
| --- | --- |

All numeric terminals are fixed-point. The previous illustration shows the encodings,


 word lengths, and integer word lengths of these terminals. If you hide these


 terminals, LabVIEW sets them to 0. These terminals do not adapt to source: if you


 wire a fixed-point control or indicator with a different data type to a terminal,


 LabVIEW coerces the value, which reduces precision. To retain precision, either wire


 a value with the same data type as the terminal or adjust the integer word length of the terminal.

Note

The other terminals are Booleans. If you hide these terminals, LabVIEW sets them to


 FALSE. You can show the patterndetect and


 patternbdetect terminals only if you enable pattern detection. You can show the


 overflow and underflow terminals


 only if you also enable registers for p.

If you show an input terminal, such as c, the corresponding


 VHDL is C => C. If you use this VHDL code elsewhere, you must


 replace the C on the right side of the port association with the


 name of the signal that drives the c input. If you hide the


 terminal, both LabVIEW and the VHDL set the value of c to a


 constant 0.

If you show an output terminal, such as overflow, the


 corresponding VHDL code is OVERFLOW => OVERFLOW. If you use this


 VHDL code elsewhere, you must replace the signal name on the right side of the port


 association to the name of the signal OVERFLOW drives. If you hide


 the terminal, the VHDL code is OVERFLOW => OPEN.

Note

Virtex-5 FPGA XtremeDSP Design Considerations
 User Guide

www.xilinx.com

Virtex-6 FPGA DSP48E1 Slice
 User Guide

#### Cascading or Hiding the a and b Input Terminals

Use the Terminals to Show section of the


 Terminals page to cascade or hide the


 a and/or b input terminals. The


 following illustration shows this section:

[IMAGE alt='image' src='GUID-4A2ECE5B-0040-49EC-9254-6665637435C7-a5.png']

Use this section to complete the following tasks:

- To set a terminal to cascade mode, select the acin or


 bcin option, respectively. The function then displays


 acin or bcin terminals instead


 of a or b . You must wire


 acin and bcin to the


 acout or bcout output


 terminals from another DSP48E or DSP48E1 function. Note The


 acin input terminal has the same data type as the


 a input terminal. The bcin


 terminal has the same data type as the b input


 terminal. The word lengths of these terminals are fixed, but you can adjust the integer word lengths to retain precision.
- To set a terminal to direct mode, select the a or


 b option, respectively.
- If you are not using a terminal, hide it by selecting its Hide


 both option.

Refer to the *Virtex-5 FPGA XtremeDSP Design Considerations User Guide* and the
 *Virtex-6 FPGA DSP48E1 Slice User Guide*, available on the Xilinx Web
 site at www.xilinx.com, for information about cascading and its
 implications for DSP48E and DSP48E1 slices.

#### VHDL Equivalent of LabVIEW Options

To view the VHDL equivalent of a configuration, click the VHDL
 Instantiation tab. Refer to Table 1-3 in either the *Virtex-5
 FPGA XtremeDSP Design Considerations User Guide* or the *Virtex-6
 FPGA DSP48E1 Slice User Guide*, available on the Xilinx Web site at
 www.xilinx.com, for information about specific attributes. The
 following table shows the attributes that correspond to each option in LabVIEW.

| LabVIEW Option | Attribute to Reference in Table 1-3 |
| --- | --- |
|  | A_INPUT |
|  | B_INPUT |

Note

b

bcin

B_INPUT

B

BCIN

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Adjusting the Length of the Internal Combinatorial Path of a DSP48E or DSP48E1 Function
- Caveats for Using DSP48E and DSP48E1 Functions
- Configuring DSP48E and DSP48E1 Functions
- Configuring Pattern Detection for a DSP48E or DSP48E1 Function
- Retaining the Precision of DSP48E and DSP48E1 Function Terminals

<!--NI_TOPIC bundle=labview-fpga-module path=shrinking-the-dsp48e-or-dsp48e1-function-icon-fpga-module.html language=enus -->
## TOPIC 00149: Shrinking the DSP48E or DSP48E1 Function Icon

- bundle_id: `labview-fpga-module`
- source_path: `shrinking-the-dsp48e-or-dsp48e1-function-icon-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/shrinking-the-dsp48e-or-dsp48e1-function-icon-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To reduce the amount of space a DSP48E or DSP48E1 function icon takes up on the block diagram, right-click the function and select Contracted View. The following figure shows the difference between the two views:

### Shrinking the DSP48E or DSP48E1 Function Icon

To reduce the amount of space a DSP48E or DSP48E1


 function icon takes up on the block diagram, right-click the function and select


 Contracted View. The following figure shows the


 difference between the two views:

[IMAGE alt='image' src='GUID-732557DA-EC71-4B5A-AF79-66425868BA6E-a5.png']

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

Related concepts:

- DSP48E Example: Creating a Complex Multiplier
- DSP48E Example: Creating an n-Tap FIR Filter

<!--NI_TOPIC bundle=labview-fpga-module path=specify-remote-fpga-target-interface-vi.html language=enus -->
## TOPIC 00150: Specify a Remote FPGA Target in an FPGA Interface VI

- bundle_id: `labview-fpga-module`
- source_path: `specify-remote-fpga-target-interface-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/specify-remote-fpga-target-interface-vi.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to wire a remote resource string directly into the Open FPGA VI Reference function on a host VI. Ensure you have the following: A host VI where you can place the Open FPGA VI Reference function. Host name or IP address of the remote system. FPGA resource name on the remote target. Required

### Specify a Remote FPGA Target in an FPGA
 Interface VI

Learn how to wire a remote resource string directly into the Open FPGA VI Reference
 function on a host VI.

- A host VI where you can place the Open FPGA VI
 Reference function.
- Host name or IP address of the remote system.
- FPGA resource name on the remote target.
- Required NI‑RIO drivers installed on the host.

Tip

Open FPGA VI Reference

Tip

1. Place Open FPGA VI Reference on the block diagram.
2. Perform one of the following actions: 
 Add a RIO Device control from the I/O palette on
 the front panel.
 Convert the terminal to a constant on the block diagram.
3. Perform one of the following actions: 
 Select the remote target from the dropdown menu if it was configured in
 the FPGA Target Properties.
 Enter the resource string directly in the control/constant:
 rio://<remote-host>/<fpga-resource> 
 Note <remote-host> is the host name or IP
 address of the system that runs the FPGA target you want to
 access.
 <fpga-resource> is the name of the FPGA
 resource on that system, such as RIO0.For example: rio://192.168.1.100/RIO0Tip See [Figure 5.Remote Target Specified by
 a RIO Device Constant](specify-remote-fpga-target-interface-vi.html#GUID-832608FE-367D-46A5-A3E9-A7041CEE2513__FIG_PRV_DYX_YHC) for a wiring reference.
4. Wire Open FPGA VI Reference to subsequent nodes. 
 For example: read/write methods.
5. Run the VI to open the remote reference and verify connectivity.

- Error on open:
  - Confirm the resource string.
  - Verify network connectivity.
  - Ensure the remote target is powered and reachable.
- Intermittent failures: check firewall rules, VLAN routing, and DNS
 resolution stability.

#### Wiring a Remote Resource into Open
 FPGA VI Reference

resource name

RIO
 Device

rio://<remote-host>/<fpga-resource>

Figure 5.

[IMAGE alt='Diagram showing Open FPGA VI Reference with a remote resource string wired to access a target over the network.' src='GUID-56CEC3D5-F3BA-4E69-91AE-AC9C3314DD84-a5.png']

Parent topic:

Accessing Remote FPGA Targets Across Networks

Related concepts:

- Accessing Remote FPGA Targets Across Networks

<!--NI_TOPIC bundle=labview-fpga-module path=specify-remote-fpga-target-properties.html language=enus -->
## TOPIC 00151: Specify a Remote FPGA Target in the FPGA Target Properties

- bundle_id: `labview-fpga-module`
- source_path: `specify-remote-fpga-target-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/specify-remote-fpga-target-properties.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to add a remote FPGA target to a project so it appears in the RIO Device list on host VIs. Ensure you have the following: Access to Project Explorer. Host name or IP address of the remote system. FPGA resource name on the remote target (for example, RIO0). Network connectivity between host

### Specify a Remote FPGA Target in the FPGA
 Target Properties

Learn how to add a remote FPGA target to a project so it appears in the RIO Device list
 on host VIs.

- Access to Project Explorer .
- Host name or IP address of the remote system.
- FPGA resource name on the remote target (for example, RIO0).
- Network connectivity between host and remote system.

Tip

Browse

Tip

Tip

1. Right‑click the FPGA target and select Properties in the
 Project Explorer window.
2. Enter the resource string:
 rio://<remote-host>/<fpga-resource> on the
 General page. 
 Note <remote-host> is the host name or IP
 address of the system that runs the FPGA target you want to
 access.
 <fpga-resource> is the name of the FPGA
 resource on that system, such as RIO0.For example: rio://192.168.1.100/RIO0Tip See [Figure 4.Remote Target Specified by
 a RIO Device Constant](specify-remote-fpga-target-properties.html#GUID-135602B5-0A39-4051-B707-7DC9F21C688A__FIG_VQH_MBY_YHC) for a wiring reference.
3. Click OK to save the property.
4. Add a RIO Device control or constant on the host
 VI.
5. Open the control/constant dropdown menu and select the newly added remote
 target.

The expected result is that the remote FPGA target becomes selectable from the RIO
 Device control/constant dropdown menu in host VIs.

- The remote target does not appear in the dropdown:
  - Verify IP/host name.
  - Confirm network reachability.
  - Check that discovery is allowed through firewalls.
- The resource string is rejected: ensure the syntax is
 rio://host/resource without trailing spaces or hidden
 characters.

#### Wiring a Remote Resource into Open FPGA VI Reference

resource name

RIO
 Device

FPGA Target Properties

Figure 4.

[IMAGE alt='Diagram showing Open FPGA VI Reference with a remote resource string wired to access a target over the network.' src='GUID-56CEC3D5-F3BA-4E69-91AE-AC9C3314DD84-a5.png']

Parent topic:

Accessing Remote FPGA Targets Across Networks

Related concepts:

- Accessing Remote FPGA Targets Across Networks

<!--NI_TOPIC bundle=labview-fpga-module path=start-verify-rio-server.html language=enus -->
## TOPIC 00152: Start and Verify the RIO Server for Network Access

- bundle_id: `labview-fpga-module`
- source_path: `start-verify-rio-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/start-verify-rio-server.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to ensure the RIO server is running where it is required for network access to RIO devices. Ensure you have the following: Administrative access on the system hosting local RIO hardware (for example, a PXI controller). Platform documentation or service management tools available. Network c

### Start and Verify the RIO Server for Network
 Access

Learn how to ensure the RIO server is running where it is required for network access to
 RIO devices.

- Administrative access on the system hosting local RIO
 hardware (for example, a PXI controller).
- Platform documentation or service management tools
 available.
- Network connectivity between host and target
 systems.

Note

- On NI Linux Real‑Time systems (for example,
 CompactRIO controllers), the RIO server runs
 automatically.
- On Windows or Linux desktop systems that host
 local RIO hardware, start the RIO server
 manually.

Tip

Tip

1. Open the service or configuration utility of the operating
 system.
2. Locate the RIO Server service. 
 Note The name of the RIO
 Server service may vary by
 platform.
3. Start the service if it is stopped. Set the startup type to
 automatic if required.
4. Verify the service is running and listening on the expected
 interfaces.
5. Confirm connectivity by attempting to open a remote FPGA
 reference from the host VI.

The expected result is that the RIO server begins running where needed,
 which enables network access to RIO devices.

- Service is running but remote access fails:
  - Verify firewall rules.
  - Confirm correct interface binding.
  - Check for port conflicts.
- Service will not start:
  - Confirm driver installation.
  - Check system logs.
  - Ensure dependencies are present.

Parent topic:

Accessing Remote FPGA Targets Across Networks

Related concepts:

- Accessing Remote FPGA Targets Across Networks

Related information:

- NI-RIO For Linux/x86 64-bit Architecture

<!--NI_TOPIC bundle=labview-fpga-module path=stopping-aborting-and-resetting-fpga-vis-fpga-interface.html language=enus -->
## TOPIC 00153: Stopping, Aborting, and Resetting FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `stopping-aborting-and-resetting-fpga-vis-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/stopping-aborting-and-resetting-fpga-vis-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you create an FPGA VI that you want to stop and run again from a host VI, National Instruments recommends that you design the FPGA VI so that you can stop its execution by setting a control on the FPGA VI to a certain value. This design practice allows you to control how the FPGA VI is stopped an

### Stopping, Aborting, and Resetting FPGA VIs

If you create an FPGA VI that you want to stop and run again from a host VI, National



 Instruments recommends that you design the FPGA VI so that you can stop its



 execution by setting a control on the FPGA VI to a certain value. This design



 practice allows you to control how the FPGA VI is stopped and the values on the



 outputs on the FPGA target when the FPGA VI stops. You can stop the FPGA VI from the



 host VI by writing the relevant FPGA VI control. You then can run the FPGA VI by



 using the Invoke Method function with the Run



 method. If you do not need control of the FPGA target outputs, you can



 use the Invoke Method function with the Reset



 method to abort and restore the FPGA VI to the default state.

If stopping is not designed as part of the FPGA VI, you can reset and/or abort the



 FPGA VI from the host VI using the Reset



 method or Abort



 method. The Abort method does not reset the FPGA VI to the default state



 which might affect how the FPGA VI reacts to future executions of the Run method



 from the host VI.

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Writing to FPGA VI Controls

<!--NI_TOPIC bundle=labview-fpga-module path=storing-and-accessing-data-from-different-parts-of-an-fpga-design-fpga-module.html language=enus -->
## TOPIC 00154: Storing and Accessing Data From Different Parts of an FPGA Design

- bundle_id: `labview-fpga-module`
- source_path: `storing-and-accessing-data-from-different-parts-of-an-fpga-design-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/storing-and-accessing-data-from-different-parts-of-an-fpga-design-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To store data using an FPGA application when you need to access that data from multiple clock domains, select from the following options: Method Use case Register items You need to store a single data point The data transfer can be lossy You need to post a status every clock cycle Memory items imple

### Storing and Accessing Data From Different Parts of an FPGA Design

To store data using an FPGA application when you need to access that data from


 multiple clock domains, select from the following options:

| Method | Use case |
| --- | --- |
| Register items | You need to store a single data point The data transfer can be lossy You need to post a status every clock cycle |
| Memory items implemented using block memory | You need to store multiple data points The data transfer can be lossy |
| Handshake items | The reader and writer nodes are synchronized The data transfer must be lossless |

#### Register Items

Use register items to store data when you need to access that data from multiple


 clock domains or from different parts of your design and you need to write reusable


 code. Register items consume fewer FPGA resources than FIFOs, and they do not


 consume block memory, which is a limited type of FPGA resource.

Note

The LabVIEW FPGA Module has two types of register items:

- VI-defined register items : Use VI-defined register items


 to create reentrant subVIs and avoid resource conflicts. If you configure a


 VI-defined register item in a reentrant FPGA VI, LabVIEW creates a separate copy


 of the register item for each instance of the VI.
- Target-scoped register items : Use target-scoped register


 items if you want the register item to be visible and configurable from the


 Project Explorer window. Target-scoped register items


 are available within any FPGA VI under the same target in the Project


 Explorer window.

The following block diagram shows how you can read from and write to a register item


 using a Register Method Node configured for a target-scoped register item. This VI


 adds the value of two controls, X and


 Y, writes the sum to a register item, reads the stored


 value, increments the stored value, and prints the result to an indicator. Note that


 the Write and Read methods are in two different clock domains.

[IMAGE alt='image' src='GUID-37A317BF-7532-45AF-BA15-2B7970335A1C-a5.png']

#### Creating a Target-Scoped Register Item from the Project Explorer Window

Complete the following steps to create a target-scoped register item from the


 Project Explorer window.

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»Register to display the FPGA


 Register Properties dialog box.
3. Click OK to finish creating the register item.
4. Drag the register item from the Project Explorer window


 to the block diagram. LabVIEW adds a Register Method Node configured for the


 register item.

Note

#### Creating a Register Item from the Block Diagram

You can create either a target-scoped or a VI-defined register item from the block


 diagram.

Target-Scoped:

1. Display the block diagram of the FPGA VI.
2. From the Functions palette, add a Register Method Node to


 the block diagram.
3. Right-click the Register Method Node and select Add New


 Register to display the FPGA Register


 Properties dialog box. [IMAGE alt='image' src='GUID-ED3A60E1-F7EE-431D-9D52-F9700753C21C-a5.png']Tip You also can


 right-click the Register Method Node and select


 Select


 Register»x,


 where x is an


 existing register


 item.
4. Click OK to finish creating the register item.

You also can wire a reference to the Register In input to


 specify an existing register item. LabVIEW configures the Register Method Node with


 the default method, Write. After you specify the register item, right-click the


 Register Method Node and selectSelect


 Method»y, where


 y is the specific method.

VI-Defined:

1. Display the block diagram of the FPGA VI.
2. From the Functions palette, add a VI-Defined Register


 Configuration Node to the block diagram.
3. Right click the VI-Defined Register Configuration Node and select


 Configure to display the FPGA Register


 Properties dialog box.
4. Click OK to finish creating the register item.

#### Handshake Items

Handshake items behave like single-element FIFOs. Use handshake items to transfer one


 data element between a writer node in one clock domain and a reader node in the same


 or a different clock domain. Use handshake items to achieve lossless transfer from a


 writing domain to a reading domain and notify the writing domain when the reader


 receives the data. Handshake items consume fewer FPGA resources than FIFOs, and they


 do not consume block memory, which is a limited type of FPGA resource.

The LabVIEW FPGA Module has two types of handshake items:

- VI-defined handshake items : Use VI-defined handshake


 items to create reentrant subVIs and avoid resource conflicts. If you configure


 a VI-defined handshake item in a reentrant FPGA VI, LabVIEW creates a separate


 copy of the handshake item for each instance of the VI.
- Target-scoped handshake items : Use target-scoped


 handshake items if you want the handshake item to be visible and configurable


 from the Project Explorer window. Target-scoped handshake


 items are available within any FPGA VI under the same target in the


 Project Explorer window.

#### Reading Data Using a Handshake Method Node

There are two ways to read data using a Handshake Method Node:

| Method | Use case |
| --- | --- |
| Read method | You only need to read the data element one time. The Read method automatically acknowledges the data, meaning that it removes the data to prepare for the next transfer. |
| Acknowledge and Read Without Acknowledge methods | You need control over when the node acknowledges the data transfer. The reader node can read the same data element multiple times until the acknowledge executes. |

The following block diagram shows how you can read from and write to a handshake item


 using a Handshake Method Node configured for a target-scoped handshake item. This VI


 increments a value by one, writes the data to a handshake item, reads the stored


 value, and automatically acknowledges the read. Input Valid


 is TRUE when Ready for Input is TRUE. The VI then writes the


 stored value to an indicator when Output Valid is TRUE. Note


 that the Write method and the Read method are in two different clock domains,


 indicated by two red boxes. This design ensures lossless data transfer by writing


 all data points to the faster clock domain.

Note

Clear

[IMAGE alt='image' src='GUID-FCA87339-805A-43B1-A687-5A21F7116594-a5.png']

#### Creating a Target-Scoped Handshake Item from the Project Explorer Window

Complete the following steps to create a target-scoped handshake item from the


 Project Explorer window:

1. In the Project Explorer window, right-click the FPGA


 target.
2. Select New»Handshake to display the FPGA


 Handshake Properties dialog box. Use the options in this dialog


 box to configure the handshake item.
3. Click OK to finish creating the handshake item.
4. Drag the handshake item from the Project Explorer window


 to the block diagram. LabVIEW adds a Handshake Method Node configured for the


 handshake item.

Note

#### Creating a Handshake Item from the Block Diagram

You can create either a target-scoped or a VI-defined handshake item from the block


 diagram.

Target-Scoped:

1. Display the block diagram of the FPGA VI.
2. Add a Handshake Method Node to the block diagram.
3. Right-click the Handshake Method Node and select Add New


 Handshake to display the FPGA Handshake


 Properties dialog box. [IMAGE alt='image' src='GUID-ED3A60E1-F7EE-431D-9D52-F9700753C21C-a5.png']Tip You also can


 right-click the Handshake Method Node and select


 Select


 Handshake»x,


 where x is an


 existing handshake


 item.
4. Click OK to finish creating the handshake item.

You also can wire a reference to the Handshake In input to


 specify the handshake item. LabVIEW configures the Handshake Method Node with the


 default method, Write. After you specify the handshake item, right-click the


 Handshake Method Node and selectSelect


 Method»y, where


 y is the specific method.

VI-Defined:

1. Display the block diagram of the FPGA VI.
2. Add a Handshake Method Node to the block diagram.
3. Double-click the VI-Defined Handshake Configuration Node to display the


 FPGA Handshake Properties dialog box.
4. Click OK to finish creating the handshake item.

Parent topic:

Storing Data on an FPGA Target

Related concepts:

- Implementing Multiple Clock Domains
- Using I/O, Clocks, Register Items, Memory Items, FIFOs, and Handshake Items in SubVIs
- Determining When to Use Reentrant or Non-Reentrant SubVIs

<!--NI_TOPIC bundle=labview-fpga-module path=storing-and-transferring-data-fpga-module.html language=enus -->
## TOPIC 00155: Storing and Transferring Data

- bundle_id: `labview-fpga-module`
- source_path: `storing-and-transferring-data-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/storing-and-transferring-data-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you design an FPGA application to store or transfer data, you specify the amount and type of FPGA resources the application uses to handle the data. Applications that require more FPGA resources than are available on the device will not compile. To create a viable FPGA design, select the approp

### Storing and Transferring Data

When you design an FPGA application to store or transfer data, you specify the


 amount and type of FPGA resources the application uses to handle the data.


 Applications that require more FPGA resources than are available on the device will


 not compile.

To create a viable FPGA design, select the appropriate type and quantity of FPGA


 resources to execute the tasks you require.

The following topics provide information about selecting the best design components


 for your application.

- Storing Data on an FPGA Target
- Transferring Data between Structures or Devices
- Using Peer-to-Peer Streaming with FPGA Targets

Parent topic:

Creating FPGA VIs

Related concepts:

- Storing Data on an FPGA Target
- Transferring Data between Devices or Structures Using FIFOs

<!--NI_TOPIC bundle=labview-fpga-module path=storing-data-between-loop-iterations-fpga-module.html language=enus -->
## TOPIC 00156: Storing Data between Loop Iterations

- bundle_id: `labview-fpga-module`
- source_path: `storing-data-between-loop-iterations-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/storing-data-between-loop-iterations-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Feedback Nodes Feedback Nodes use FPGA resources to store data. Use a Feedback Node to store data, such as state information, from one VI execution or loop iteration to the next. When a Feedback Node receives a new value, the node stores the value until the node passes that value to the next input t

### Storing Data between Loop Iterations

#### Feedback Nodes

Feedback Nodes use FPGA resources to store data. Use a Feedback Node to



 store data, such as state information, from one VI execution or loop iteration to



 the next. When a Feedback Node receives a new value, the node stores the value until



 the node passes that value to the next input terminal. To store samples of data for



 multiple subsequent iterations, increase the value of Delay



 on the Configuration page of the Properties



 dialog box to delay the output of the Feedback Node.

Note

The following example VI uses a Feedback Node. This VI runs a For Loop for



 n iterations. The VI then multiplies a constant value of



 3 by the value stored in the Feedback Node and returns the



 product. The Feedback Node has a value of 1 on the first call of



 the VI. Given n iterations, Product is



 3<sup>n</sup>.

[IMAGE alt='image' src='GUID-02F82EF5-4268-4F2D-9918-E43D7C6CBB46-a5.png']

Complete the following steps to create a Feedback Node.

1. Display the block diagram of the FPGA VI.
2. From the Functions palette, select



 Programming»Structures»Feedback Node and add it to



 the block diagram.

Alternately, the Feedback Node automatically appears when you wire the output of a



 subVI, function, or group of subVIs or functions to the input of that same VI,



 function, or group.

Configure Feedback Nodes using the Properties



 dialog box, accessible when you right-click a Feedback Node and select



 Properties from the shortcut menu. If you place a



 checkmark in the Ignore FPGA reset method checkbox on the



 Configuration page of this dialog box, the LabVIEW FPGA



 Module removes the reset from the underlying register instantiations. This removal



 gives the compiler the option to implement the delays using shift register look-up



 tables (SRLs) instead of flip-flops. SRLs combine many delays into a single look-up



 table (LUT), which can reduce FPGA resource use significantly.

In loops, you can right-click a Feedback Node and select Replace with



 Shift Register from the shortcut menu to replace the Feedback Node



 with shift registers. You also can replace shift registers



 with a Feedback Node. However, you cannot implement shift registers using SRLs.

Parent topic:

Storing Data on an FPGA Target

Related concepts:

- Interfacing AXI IP in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=storing-data-on-an-fpga-target-fpga-module.html language=enus -->
## TOPIC 00157: Storing Data on an FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `storing-data-on-an-fpga-target-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/storing-data-on-an-fpga-target-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Register items Memory items Feedback Nodes or shift registers Global and local variables Discrete Delay functions Arrays You can use the Target Information component on the General page of the FPGA Target Properties dialog box to get the number of block memory resources that an FPGA target supports.

### Storing Data on an FPGA Target

- Register items
- Memory items
- Feedback Nodes or shift registers
- Global and local variables
- Discrete Delay functions
- Arrays

[IMAGE alt='image' src='GUID-B08B1C80-138C-412C-BC73-417835DC8B7C-a5.png']

Note

Target Information

Parent topic:

Storing and Transferring Data

Related concepts:

- Storing and Transferring Data
- Reducing Memory Resource Usage with Dual-Port Read Access

<!--NI_TOPIC bundle=labview-fpga-module path=supported-data-types-fpga-module.html language=enus -->
## TOPIC 00158: Supported Data Types

- bundle_id: `labview-fpga-module`
- source_path: `supported-data-types-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/supported-data-types-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA VIs support the following data types: 8-bit signed and unsigned integer numerics 16-bit signed and unsigned integer numerics 32-bit signed and unsigned integer numerics 64-bit signed and unsigned integer numerics Boolean Fixed-point Single-precision floating-point for certain functions Clusters

### Supported Data Types

FPGA VIs support the following data types:

- 8-bit signed and unsigned integer numerics
- 16-bit signed and unsigned integer numerics
- 32-bit signed and unsigned integer numerics
- 64-bit signed and unsigned integer numerics
- Boolean
- Fixed-point
- Single-precision floating-point for certain functions
- Clusters of supported data types
- Arrays of supported data types that resolve to a single size at compile time

Parent topic:

Creating FPGA VIs

Related concepts:

- Using Custom Data Types with Register Items, Memory Items, FIFOs, and Handshake Items

<!--NI_TOPIC bundle=labview-fpga-module path=switching-between-dsp48e-and-dsp48e1-functions-fpga-module.html language=enus -->
## TOPIC 00159: Switching Between DSP48E and DSP48E1 Functions

- bundle_id: `labview-fpga-module`
- source_path: `switching-between-dsp48e-and-dsp48e1-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/switching-between-dsp48e-and-dsp48e1-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can replace a DSP48E function with a DSP48E1 function or vice versa by right-clicking the function and selecting Replace with DSP48E1 or Replace with DSP48E, respectively. For example, if you move a VI from a Virtex-5 FPGA target to a Virtex-6 FPGA target, you might want to replace a DSP48E func

### Switching Between DSP48E and DSP48E1 Functions

You can replace a DSP48E function with a DSP48E1 function or vice versa by


 right-clicking the function and selecting Replace with


 DSP48E1 or Replace with DSP48E, respectively.


 For example, if you move a VI from a Virtex-5 FPGA target to a Virtex-6 FPGA target,


 you might want to replace a DSP48E function with a DSP48E1 function.

Parent topic:

Introduction to DSP48E and DSP48E1 Slices

<!--NI_TOPIC bundle=labview-fpga-module path=synchronizing-fpga-vis-and-host-vis-using-interrupts-fpga-interface.html language=enus -->
## TOPIC 00160: Synchronizing FPGA VIs and Host VIs Using Interrupts

- bundle_id: `labview-fpga-module`
- source_path: `synchronizing-fpga-vis-and-host-vis-using-interrupts-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/synchronizing-fpga-vis-and-host-vis-using-interrupts-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some FPGA targets allow you to generate interrupts from the FPGA VI to notify the host VI of events, such as data being ready, an error occurring, or a task finishing. To determine whether a target supports interrupts, access the FPGA Target Properties dialog box and locate the Target Information se

### Synchronizing FPGA VIs and Host VIs Using Interrupts

Some FPGA targets allow you to generate interrupts from the FPGA VI to notify the host VI of events,


 such as data being ready, an error occurring, or a task finishing. To determine


 whether a target supports interrupts, access the FPGA Target


 Properties dialog box and locate the Target


 Information section of the General page.

#### Waiting for and Acknowledging a Single Interrupt

Complete the following steps to wait for and acknowledge a single interrupt in a host


 VI.

1. Open a reference to the FPGA VI or bitfile that generates


 interrupts.
2. Add the Invoke Method function to the block diagram of the


 host VI in the data flow where you want the host VI to wait for interrupts from


 the FPGA VI. Be sure to wire the FPGA VI Reference In 


 input.
3. Right-click the Invoke Method function and select Method»Wait on


 IRQ from the shortcut menu.
4. Right-click the IRQ Number(s) input on the Invoke Method


 function and select Create»Constant from the shortcut


 menu. You also can create a control.
5. Enter the value of the logical interrupt you selected in the FPGA VI.
6. Wire the Timeout input if you want to specify the maximum


 time the host VI waits for the interrupt before continuing the data flow. By


 default, the host VI does not wait for an interrupt to occur and returns only


 interrupts already set by the FPGA VI. You also can wire a constant with a value


 of –1 to wait indefinitely for an interrupt. If you use the


 Timeout input, you can use the Timed


 Out output to determine whether the host VI continued data flow


 due to the timeout occurring or to the receipt of an interrupt. If a timeout


 occurs, the Timed Out output returns TRUE.
7. Right-click the IRQ(s) Asserted output on the Invoke


 Method function and select Create»Indicator from the


 shortcut menu. LabVIEW creates a numeric indicator. A value of –1 indicates that


 the interrupt was not received.
8. Add the Invoke Method function to the block diagram of the host VI in the data


 flow where you want the host VI to acknowledge the interrupt from the FPGA VI.


 Add the Invoke Method function to a Case


 Structure if you want the function to execute only when the host VI


 receives an interrupt. If you wire a Boolean constant of TRUE to the


 Wait Until Cleared input of the Interrupt VI, add the


 Invoke Method function to the data flow where you want to tell the Interrupt VI


 to stop waiting. Be sure to wire the FPGA VI Reference In 


 input of the Invoke Method function.
9. Right-click the Invoke Method function and select Method»Acknowledge


 IRQ from the shortcut menu. Use the Acknowledge IRQ method to


 acknowledge the logical interrupt returned by the Wait on IRQ method.
10. Wire the IRQ(s) Asserted output of the Wait on IRQ method


 directly to the IRQ Number(s) input of the Acknowledge


 IRQ method.

#### Waiting for and Acknowledging Multiple Interrupts

Complete the following steps to wait for and acknowledge multiple interrupts in a


 host VI.

1. Open a reference to the FPGA VI or bitfile that generates


 interrupts.
2. Add the Invoke Method function to the block diagram of the


 host VI in the data flow where you want the host VI to wait for interrupts from


 the FPGA VI. Be sure to wire the FPGA VI Reference In 


 input.
3. Right-click the Invoke Method function and select Method»Wait on


 IRQ from the shortcut menu.
4. Add an Array Constant to the block diagram. An array


 includes an index display on the left, an element display on the right, and an


 optional label.
5. Add a Numeric Constant to the array.
6. Using the Positioning tool, expand the array constant to the number of


 interrupts needed.
7. Enter the values of the logical interrupts.
8. Wire the array constant to the IRQ Number(s) input.
9. Wire the Timeout input if you want to specify the maximum


 time the host VI waits for the interrupt before continuing the data flow. By


 default, the host VI does not wait for an interrupt to occur and returns only


 interrupts already set by the FPGA VI. You also can wire a constant with a value


 of –1 to wait indefinitely for an interrupt. If you use the


 Timeout input, you can use the Timed


 Out output to determine whether the host VI continued data flow


 due to the timeout occurring or to the receipt of an interrupt. If a timeout


 occurs, the Timed Out output returns TRUE.
10. Right-click the IRQ(s) Asserted output on the Invoke


 Method function and select Create»Indicator from the


 shortcut menu. LabVIEW creates an array indicator. The IRQ(s)


 Asserted front panel indicator displays the number(s) of the


 interrupts the FPGA target asserts. An empty array indicates that no interrupts


 were received.
11. Add the Invoke Method function to the block diagram of the host VI in the data


 flow where you want the host VI to acknowledge the interrupts from the FPGA VI.


 Add the Invoke Method function to a Case


 Structure if you want the function to execute only when the host VI


 receives an interrupt. If you wire a Boolean constant of TRUE to the


 Wait Until Cleared input of the Interrupt VI, add the


 Invoke Method function to the data flow where you want to tell the Interrupt VI


 to stop waiting. Be sure to wire the FPGA VI Reference In 


 input of the Invoke Method function.
12. Right-click the Invoke Method function and select Method»Acknowledge


 IRQ from the shortcut menu. Use the Acknowledge IRQ method to


 acknowledge the logical interrupts returned by the Wait on IRQ method.
13. Wire the IRQ(s) Asserted output of the Wait on IRQ method


 directly to the IRQ Number(s) input of the Acknowledge


 IRQ method.

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=synchronizing-io-in-single-cycle-timed-loops-fpga-module.html language=enus -->
## TOPIC 00161: Synchronizing I/O in Single-Cycle Timed Loops

- bundle_id: `labview-fpga-module`
- source_path: `synchronizing-io-in-single-cycle-timed-loops-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/synchronizing-io-in-single-cycle-timed-loops-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW places synchronization registers between the FPGA hardware I/O and the FPGA I/O Node as implemented on the target FPGA. You can specify the number of synchronization registers for input data as 0, 1, or 2, and you can specify the number of synchronization registers for output data as 0 or 1.

### Synchronizing I/O in Single-Cycle Timed Loops

LabVIEW places synchronization registers between the FPGA hardware I/O and the FPGA



 I/O Node as implemented on the target FPGA. You can specify the number of synchronization registers for input data as 0, 1, or 2,



 and you can specify the number of synchronization registers for output data as 0 or 1. When the input is



 set to Auto (default), the number of synchronization



 registers is 2 for input data and 1 for output data.

Note

|  | Caution If you specify 0 synchronization registers for digital output resources in a Case structure nested in a single-cycle Timed Loop, LabVIEW is unable to hold the previous state of the digital output resource when the enable chain deasserts, which may result in unexpected output. NI recommends that you avoid specifying 0 synchronization registers unless you add the necessary logic to hold the previous state. |
| --- | --- |

#### Example Code Using the Default Number of Synchronization Registers

Consider an FPGA VI with digital I/O operation running in a single-cycle Timed Loop



 as shown in the illustration below.

[IMAGE alt='image' src='GUID-44AA3FAA-4F81-4BF8-A951-763C039E5884-a5.png']

The digital input signal Digital Input 1 connects to a digital output signal Digital



 Output 1. The Trigger control wired to the selector terminal specifies when the



 application reads from the Digital Input 1 and writes to Digital Output 1 using a



 Case structure.

When the number of input synchronization registers is set to default of



 Auto, the circuit on the FPGA created as shown in the



 illustration below.

[IMAGE alt='image' src='GUID-7A3111D0-BF5F-4D7B-889A-A62E85E0A797-a5.png']

In this example, Digital Input 1 is a physical DIO pin on the FPGA that is connected



 to two synchronization registers. The first synchronization register handles the



 meta-stable state. The output of the second synchronization register is wired



 directly to a corresponding synchronization register for the Digital Output 1, which



 is connected to the output DIO pin on the FPGA. The Trigger control register output



 is connected to the enable chain input on the output synchronization register to determine



 when to output the signal.

#### Example Code: Setting the Number of Synchronization Registers to Zero

Consider the same block diagram as illustrated above, but now assume the number of



 synchronization registers is set to 0 for both the digital input and output. The



 equivalent circuit on the FPGA is shown below.

[IMAGE alt='image' src='GUID-7DF4ED6F-C39C-47C1-AF93-D599D3ED4257-a5.png']

Here, the digital input signal Digital Input 1 has a direct hardwire connection to



 the digital output signal Digital Output 1 on the FPGA. The compilation process does



 not include any control logic to determine when to read Digital Input 1 and write



 Digital Output 1. In this case, the digital I/O lines are connected to each other as



 soon as the bitfile is downloaded to the FPGA.

#### Example Code: Using Zero Synchronization Registers and a Logic Function

If you must set the number of I/O synchronization registers to 0 inside a



 single-cycle Timed Loop and you are not satisfied with the behavior described in



 Example Code: Setting the Number of



 Synchronization Registers to Zero, you must make sure that the



 application contains logic between the input and the output. By adding logic between



 the I/O input and output, you avoid creating a direct wire connection that runs



 independently of the controlling logic. The following block diagram illustrates one



 option for implementing code with no synchronization registers.

[IMAGE alt='image' src='GUID-671CDB7D-16A8-40C3-86E0-E19877B2950A-a5.png']

The block diagram above uses an And function instead of a Case structure to control



 whether the signal reaches Digital Output 1. The Digital Input 1 node and the



 Trigger control are the input to the And function and the output of the And function



 connects to the Digital Output 1 node. The equivalent circuit on the FPGA is shown



 below.

[IMAGE alt='image' src='GUID-F99FDA92-AEEF-446C-A1EF-E40F5CBD0A79-a5.png']

The circuit above is similar to the circuit in the Example Code: Using the Default Number of



 Synchronization Registers in that the connection between Digital Input 1



 and Digital Output 1 is made only when the Trigger control is set to TRUE. However,



 the circuit is different in that there are no synchronization registers on the



 signal path between Digital Input 1 and Digital Output 1. Digital Output 1 may be



 changing independently of the clock controlling the single-cycle Timed Loop.

Note

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Performing I/O Using Case Structures in SCTLs
- Dataflow and the Enable Chain in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=synchronizing-the-fpga-and-the-host-fpga-module.html language=enus -->
## TOPIC 00162: Synchronizing the FPGA and the Host

- bundle_id: `labview-fpga-module`
- source_path: `synchronizing-the-fpga-and-the-host-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/synchronizing-the-fpga-and-the-host-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA VI and the host VI are inherently asynchronous. If you need to synchronize execution or data transfer between the FPGA VI and the host VI, you can use interrupt-based or polling-based methods. Use interrupt-based synchronization when you need to minimize usage of the host processor and poll

### Synchronizing the FPGA and the Host

The FPGA VI and the host VI are inherently asynchronous. If you need to synchronize


 execution or data transfer between the FPGA VI and the host VI, you can use


 interrupt-based or polling-based methods. Use interrupt-based synchronization when


 you need to minimize usage of the host processor and polling-based synchronization


 when you need lower latency. DMA FIFOs are a special kind of polling-based


 synchronization that you can use to transfer data between the FPGA and the host. The


 following table summarizes the characteristics of these synchronization methods.

| Synchronization Method | Latency | Host CPU Usage | Common Use |
| --- | --- | --- | --- |
| Interrupt-Based | Higher | Lower | Datalogging |
| Polling-Based | Lower | Higher | Control, Simulation |
| DMA FIFOs | Lower | Lower | Datalogging |

#### Interrupt-Based Synchronization

An interrupt is a physical hardware line to the host that the FPGA target asserts.


 You can use interrupts to notify the host VI of events, such as data becoming


 available, an error occurring, or a task finishing.

An advantage of using interrupt-based communication instead of polling-based


 communication is that the host VI can perform other operations while waiting for the


 interrupt. However, the overhead required to process the interrupt increases latency


 relative to polling-based synchronization.

Use the Interrupt VI to generate any of the 32 logical interrupts available on


 the FPGA target. Each logical interrupt specifies the reason for causing the


 interrupt and allows you to handle it differently in software. You can set the


 Interrupt VI to wait until the host VI acknowledges the interrupt on the FPGA target


 by wiring the Wait Until Cleared input. In this case, the


 Interrupt VI waits until the host VI controlling the device acknowledges the


 interrupt.

Use caution when you include simultaneous interrupt calls on the FPGA target. The


 interrupt line becomes a shared resource if you use more than one, which can induce jitter.

#### Polling-Based Synchronization

Polling-based synchronization involves using a loop to continually check the status


 of the FPGA VI and performing an action when a certain condition becomes true. You


 can use the timing VIs to determine the frequency of the polling loop. You can


 decrease the synchronization latency by increasing the frequency of the polling


 loop. You can decrease the host CPU usage by decreasing the frequency of the polling


 loop.

#### Direct Memory Access (DMA) and Synchronization

DMA FIFOs are inherently synchronous. The DMA engine automatically polls the status of the DMA FIFO and initiates


 data transfer when the DMA FIFO contains the number of data values you specify.


 However, you can specify the manner in which a device retrieves data from a DMA


 FIFO. Specifically, you can use polling-based methods to retrieve data from a DMA FIFO.

Parent topic:

Creating FPGA VIs

Related concepts:

- Managing Shared Resources
- How DMA Transfers Work
- Designing a Host VI to Read Data in DMA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=synthesis-files-and-simulation-fpga-module.html language=enus -->
## TOPIC 00163: Synthesis Files and Simulation

- bundle_id: `labview-fpga-module`
- source_path: `synthesis-files-and-simulation-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/synthesis-files-and-simulation-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you add a synthesis file to the IP Integration Node, LabVIEW assigns a simulation behavior to that file. You can accept this behavior, change it, or exclude the file from simulation. The following table describes the available synthesis file types, the simulation behaviors LabVIEW automaticall

### Synthesis Files and Simulation

After you add a synthesis file to the IP Integration Node, LabVIEW


 assigns a simulation behavior to that file. You can accept this behavior, change it, or exclude the file


 from simulation. The following table describes the available synthesis


 file types, the simulation behaviors LabVIEW automatically assigns to each type, and


 caveats when exporting certain types of files for simulation for Virtex-II


 FPGAs.

Note

| Synthesis File Type | Simulation Behavior that LabVIEW Assigns | Notes | Simulation Caveats for Virtex-II FPGAs |
| --- | --- | --- | --- |
| Netlist files | User-defined | LabVIEW uses a simulation model that you define. You must click the Set Simulation Behavior button to launch the Set Simulation Behavior dialog box. In this dialog box, use the Add File, Remove File, and Set as Top buttons to add .vhd files to the simulation model. You can obtain these files from the same source that provided the netlist file. Ensure that the netlist file name is the same as the netlist component name. The Generics and Support File Generation page of the IP Integration Node Properties wizard displays a Xilinx error and configuration of the IP Integration Node fails if these names differ. | If the IP contains components that are specific to Virtex-II FPGAs, such as the BSCAN component, you cannot export the IP for simulation. |
| Xilinx IP configuration files | Same as synthesis | LabVIEW uses the .vhd simulation model generated by the Xilinx IP generator. | You cannot export Xilinx IP configuration files for simulation with Virtex-II FPGAs. |
| .coe | Same as synthesis | N/A. | N/A. |
| .vhd and other files | Same as synthesis | LabVIEW uses the .vhd synthesis file for simulation also. | .vhd files only: If the IP instantiates components for primitives that are specific to Virtex-II FPGAs, NI does not guarantee the accuracy of the simulation. |

Parent topic:

Using the IP Integration Node

<!--NI_TOPIC bundle=labview-fpga-module path=throughput-conventions.html language=enus -->
## TOPIC 00164: Throughput Conventions in FPGA-Based Systems

- bundle_id: `labview-fpga-module`
- source_path: `throughput-conventions.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/throughput-conventions.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to interpret throughput metrics across FPGA‑based systems by using consistent units, conversions, and multi‑channel scaling rules. Throughput in FPGA‑based systems can appear in different unit conventions depending on the data‑path design. The following sections describe how to interpret t

### Throughput Conventions in FPGA-Based
 Systems

Learn how to interpret throughput metrics across FPGA‑based
 systems by using consistent units, conversions, and multi‑channel scaling
 rules.

Throughput in FPGA‑based systems can appear in
 different unit conventions depending on the data‑path design. The following sections
 describe how to interpret these units consistently and how to relate them to
 multi‑channel behavior and clock‑rate constraints.

#### Unified Throughput Relationships

- System Throughput =Channel Throughput ÷ Number of
 Channels
- Channel Throughput =System Throughput × Number of
 Channels

Note

Wiring Single‑Input Nodes Using Handshaking

#### Throughput Unit Conventions

cycles/sample

cRIO‑class devices

FPGA clock cycles

samples/cycle

RF
 systems

#### Unit Conversions

- System Throughput (samples/cycle) =1 ÷ System Throughput
 (cycles/sample)

- System Throughput (cycles/sample) =Clock Rate (cycles/second) ÷ Sample
 Rate (samples/second)
- System Throughput (samples/cycle) =Sample Rate (samples/second) ÷ Clock
 Rate (cycles/second)

#### Interpreting Throughput as a Spacing Constraint

In single‑cycle Timed Loop handshaking, throughput is a key concept. Throughput, denoted as
 T<sub>f</sub>, represents the
 minimum number of clock cycles required. This value is the time that must elapse
 before a node can accept a new valid input after starting computation.

This definition naturally expresses in cycles/sample, because T<sub>f</sub> represents minimum
 spacing between accepted samples in clock cycles. A smaller T<sub>f</sub> supports more
 frequent acceptance of new samples.

Note

Scheduling Timing Using Handshaking Signals

#### Multi-Channel Designs: Interpretation and Interleaving

channel 0

- Channel 0 receives the first valid data
 point.
- Channel 1 receives the second valid data
 point.
- This pattern continues for subsequent channels.

Interleaving changes interpretation of per‑channel rates because scheduling
 distributes a single stream of valid samples across channels. Apply the system and
 the channel throughput relationships to interpret per‑channel rates in interleaved
 designs.

Note

Scheduling Timing Using Handshaking Signals

#### Timing Report Clock Metrics and Throughput Metrics

Requested (MHz)

- Requested (MHz) indicates the clock rate at
 which an FPGA VI or an FPGA VI component must operate.
- Maximum (MHz) indicates the theoretical
 maximum compilation rate for an FPGA VI or an
 FPGA VI component .

If the Requested (MHz) is greater than the Maximum (MHz), the design does not meet timing
 constraints. As a result, compilation can fail in the final timing stage.

- Select cycles/sample to evaluate how
 frequently a design can accept samples.
- Select samples/cycle to evaluate how
 frequently a design can process samples.
- Select one of these throughput unit to evaluate how frequently a design
 can produce samples.

Note

Requested (MHz)

Maximum (MHz)

Reports Available from the Compilation Status
 Window

#### Guidance for Use

1. Select a primary throughput convention that matches the operating model of
 the data path.
  - For multi‑cycle scheduling, select cycles/sample .
  - For streaming pipelines, select samples/cycle .
2. Calculate system throughput from clock rate and sample rate when a design
 starts with MHz and MS/s requirements.
3. Scale between system throughput and channel throughput using the channel
 count.
4. Compare system throughput against T<sub>f</sub> values
 of nodes in a processing chain to identify acceptance‑rate limits.
5. Validate timing feasibility using Requested
 (MHz) and Maximum (MHz) in
 compilation reports. Timing feasibility constrains usable clock rate.

#### Examples

Use these examples to relate throughput units, clock rate calculations, and
 channel-scaling rules.

- Converting cycles/sample and samples/cycle: A clock rate of 40 MHz and a sample rate of 2 MS/s yields 20
 cycles per sample. This value corresponds to 0.05 samples per cycle.40,000,000 ÷ 2,000,000 =20 cycles/sample
 2,000,000 ÷ 40,000,000 =0.05 samples/cycle
- Scaling throughput across channels (cycles/sample): A system throughput of 200 cycles/sample across 4 channels yields
 800 cycles/sample for channel
 throughput.Channel Throughput =200 × 4 = 800
 cycles/sample
- Scaling throughput across channels (samples/cycle) A system throughput of 0.5
 samples/cycle across 8 channels yields 0.0625 samples/cycle per
 channel.Channel Throughput =0.5 ÷ 8 = 0.0625
 samples/cycleper
 channel

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Reports Available from the Compilation Status Window
- Scheduling Timing Using Handshaking Signals

Related tasks:

- Wiring Single-Input Nodes Using Handshaking

<!--NI_TOPIC bundle=labview-fpga-module path=timing-fpga-vis-with-arbitration-enabled-fpga-module.html language=enus -->
## TOPIC 00165: Timing FPGA VIs with Arbitration Enabled

- bundle_id: `labview-fpga-module`
- source_path: `timing-fpga-vis-with-arbitration-enabled-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/timing-fpga-vis-with-arbitration-enabled-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all arbitration options take the same amount of time to execute. If you want accesses to multiple resources of the same type to occur simultaneously, you must choose arbitration options for each resource that take the same amount of time to execute. The following block diagram illustrates an FPG

### Timing FPGA VIs with Arbitration
 Enabled

Not all arbitration options take the same amount of time to execute. If you want


 accesses to multiple resources of the same type to occur simultaneously, you must


 choose arbitration options for each resource that take the same amount of time to


 execute. The following block diagram illustrates an FPGA VI that might have a timing


 problem depending on the arbitration options selected.

[IMAGE alt='image' src='GUID-DB783E5D-1A7A-456C-9A1C-4AC59853062D-a5.png']

The FPGA I/O Nodes shown in the block diagram above have three arbitration


 options. If you choose the Always Arbitrate arbitration


 option, LabVIEW implements an equivalent arbiter for both DIO0 and DIO1. Both


 arbiters take the same amount of time to execute, so DIO0 and DIO1 output


 simultaneously in the first frame of the Flat Sequence


 structure, as long as another object elsewhere on the block diagram does not


 simultaneously request access to either DIO0 or DIO1.

If you choose the Arbitrate if Multiple Requestors Only


 arbitration option, LabVIEW implements an arbiter for DIO0 but does not implement an


 arbiter for DIO1. DIO0 uses an arbiter because DIO0 is accessed from two different


 places on the block diagram. DIO1 uses no arbiter because DIO1 is accessed only


 once. DIO0 takes longer to execute than DIO1, so DIO0 and DIO1 do not output


 simultaneously in the first frame of the Flat Sequence


 structure.

If you choose the Never Arbitrate arbitration option for both


 FPGA I/O Nodes, LabVIEW does not implement an arbiter for either DIO0 or DIO1.


 Therefore, DIO0 and DIO1 produce output simultaneously. This is safe because the


 Sequence structure ensures sequential access to DIO0 unless another object on the


 block diagram requests simultaneous access to DIO0.

Parent topic:

Managing Shared Resources

Related concepts:

- Understanding Arbitration Options

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-between-devices-or-structures-using-fifos-fpga-module.html language=enus -->
## TOPIC 00166: Transferring Data between Devices or Structures Using FIFOs

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-between-devices-or-structures-using-fifos-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-between-devices-or-structures-using-fifos-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To transfer data between different portions of an FPGA VI, between VIs on an FPGA target, or between devices, use a FIFO. A FIFO is a data structure that holds elements in the order they are received and provides access to those elements using a first-in, first-out access policy. The following illus

### Transferring Data between Devices or Structures Using FIFOs

To transfer data between different portions of an FPGA VI, between VIs on an FPGA


 target, or between devices, use a FIFO. A FIFO is a data structure that holds


 elements in the order they are received and provides access to those elements using


 a first-in, first-out access policy.

The following illustration demonstrates the behavior of elements moving through a


 FIFO.

[IMAGE alt='image' src='GUID-720ECCA5-337D-40A0-AC06-BFE464D977C0-a5.png']

Use FIFOs to transfer data in the following ways:

- Between parallel loops within one clock domain
- Across clock domains
- Between peer-to-peer targets
- Between the host computer and the FPGA

Use the FIFO Properties dialog box to create and configure FIFOs.

All FIFOs except VI-defined FIFOs have a corresponding item in the project.


 Therefore, if you use a FIFO other than a VI-defined FIFO and send the FPGA VI to


 another user, you must send the entire project. Otherwise, you cannot run the FPGA


 VI.

Use the following flow chart to determine the FIFO configuration that best fits your


 application needs.

[IMAGE alt='image' src='GUID-8F899F34-D7C5-48A4-86C1-E0D965110840-a5.png']

Note

Target Information

The following figure shows an example of a target-scoped FIFO used to transfer data


 between two single-cycle Timed Loops in the same FPGA VI. The single-cycle Timed


 Loops are in two different clock domains. The top loop uses an 80 MHz clock and the


 bottom loop uses a 40 MHz clock. In this example, an FPGA I/O Node in the 80 MHz


 clock domain acquires temperature readings from a device. A FIFO Method node writes


 the data to a FIFO. If the empty elements in the FIFO are not available for writing


 immediately, the node times out, stops the loop, and sets the Write Timed


 Out? indicator to TRUE. A FIFO Method node in the 40 MHz clock


 domain reads the data, then passes the data to a Less Than 0? function. If the


 temperature is less than zero, the function sets the Device


 Frozen? indicator to TRUE. If the data is not available to read


 immediately, the FIFO Method node times out, stops the loop, and sets the


 Read Timed Out? indicator to TRUE.

[IMAGE alt='image' src='GUID-98D6F342-CA28-480F-A8B8-E89EC553BEE8-a5.png']

Note

Timeout

#### Data Transfer Tasks

You can transfer data in the following ways:

- Within one FPGA target —Use these types of FIFOs to


 transfer data between VIs, to and from loops in a single VI, or between clock


 domains.
  - Target-scoped FIFOs —Use target-scoped


 FIFOs if you want the FIFO to be visible and configurable from the


 Project Explorer window. Target-scoped FIFOs


 have a corresponding item in the project. Updates to the project item


 affect all instances of the FIFO. Target-scoped FIFOs are accessible


 within any VI under the same FPGA target in the Project


 Explorer window. If you use a target-scoped FIFO and


 want to send the FPGA VI to another user, you have to send the entire


 project. Otherwise, the FPGA VI is broken.
  - VI-defined


 FIFOs — Use VI–defined FIFOs along with FIFO name


 controls to create reentrant subVIs and avoid resource conflicts. If you


 configure a VI-defined FIFO in a reentrant FPGA VI, LabVIEW creates a


 separate copy of the FIFO for each instance of the VI.
- Between the host and the FPGA —Use direct memory access


 (DMA) FIFOs to transfer large amounts of data between the host and the FPGA.


 This type of FIFO directly accesses memory to transfer data from FPGA target VIs


 to host VIs and vice versa. A DMA FIFO allocates memory on both the host


 computer and the FPGA target, yet acts as a single FIFO. DMA FIFOs provide


 performance advantages over using front panel controls and indicators to


 communicate between the host and the FPGA.
- Between two peer-to-peer targets —Use peer-to-peer FIFOs


 to transfer data between peer-to-peer targets without sending the data through


 the host. You can use peer-to-peer streaming to send data between FPGA and


 non-FPGA targets, but the targets must be capable of using the peer-to-peer


 stream architecture. Peer-to-peer FIFOs have a corresponding item in the


 project.

Note

Parent topic:

Creating FPGA VIs

Related concepts:

- Storing and Transferring Data
- Transferring Data Using Direct Memory Access

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-between-the-fpga-and-host-fpga-module.html language=enus -->
## TOPIC 00167: Transferring Data between the FPGA and Host

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-between-the-fpga-and-host-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-between-the-fpga-and-host-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To transfer data between an FPGA VI and a host VI programmatically, you can use one of the following methods: Programmatic Front Panel Communication Direct Memory Access (DMA) User-defined I/O variables The following table summarizes and compares these methods. Data Transfer Method Host OS Throughpu

### Transferring Data between the FPGA and Host

To transfer data between an FPGA VI and a host VI programmatically, you can use one


 of the following methods:

- Programmatic Front Panel Communication
- Direct Memory Access (DMA)
- User-defined I/O variables

The following table summarizes and compares these methods.

| Data Transfer Method | Host OS | Throughput Rate | Call Overhead | Host CPU Usage | Timing Model | Synchronization |
| --- | --- | --- | --- | --- | --- | --- |
| Programmatic front panel communication | Windows, RT | Lower | Lower | Higher | User-Defined | User-Defined |
| Direct memory access | Windows, RT | Higher | Higher | Lower | User-Defined | Automatic |
| User-Defined I/O Variables | RT with NI Scan Engine capability | Lower | Lower | Lower | NI Scan Engine | Automatic |

In general, use programmatic front panel communication for small, frequent data


 transfers and DMA for streaming large amounts of data at a time. Use user-defined


 I/O variables for transferring coherent sets of FPGA I/O data to and from an RT host


 VI. The following table compares the common reasons to use each of the transfer


 methods.

| Data Transfer Method | Common Use |
| --- | --- |
| Programmatic Front Panel Communication | Sending configuration parameters or data from the host to the FPGA Reporting status from the FPGA to the host Sending commands between the host and the FPGA Transferring single-point data between the host and the FPGA Creating a test bench for an FPGA VI |
| Direct Memory Access | Transferring large sets of data between the host and the FPGA Transferring waveform data between the host and the FPGA |
| User-Defined I/O Variables | Performing the same functions as with front panel communication but with the timing and synchronization of the NI Scan Engine Transferring coherent sets of data |

Parent topic:

Creating FPGA VIs

Related concepts:

- Transferring Data Using Front Panel Controls and Indicators
- Transferring Data Using Direct Memory Access
- Transferring Data Using the NI Scan Engine and Variables

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-using-direct-memory-access-fpga-module.html language=enus -->
## TOPIC 00168: Transferring Data Using Direct Memory Access

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-using-direct-memory-access-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-using-direct-memory-access-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct memory access (DMA) is a FIFO-based method of transferring data between an FPGA target and the host computer. DMA does not involve the host processor; therefore, it is the fastest available method for transferring large amounts of data between the FPGA target and the host. DMA Communication B

### Transferring Data Using Direct Memory Access

Direct memory access (DMA) is a FIFO-based method of transferring data between an FPGA target and the



 host computer. DMA does not involve the host processor; therefore, it is the fastest



 available method for transferring large amounts of data between the FPGA target and



 the host.

#### DMA Communication Benefits

The following list highlights the benefits of using DMA communication to transfer



 data between an FPGA target and a host computer:

- Frees the host processor to perform other calculations during data transfer
- Limits the use of front panel controls and indicators
- Saves FPGA resources when transferring arrays of data
- Automatically synchronizes data transfers between the host and the FPGA



 target

Consider using DMA if your application performs any of the following tasks:

- Transferring waveform data between the FPGA target and the host
- Transferring large sets of data
- Data logging
- Running algorithms that the FPGA target can process more efficiently than the



 host computer; for example, averaging or summing values from multiple input



 channels

#### Implementing DMA Communication in an Application

At a high level, implementing DMA communication in an FPGA application involves the



 following steps:

1. Determine whether your FPGA target supports DMA



 communication
2. Decide whether DMA is the best choice for your application. Weigh the benefits of DMA as well as other options for transferring data between an FPGA



 target and host computer.
3. Understand how DMA works.
4. Design and program the application while paying attention to the best practices:
  - Evaluate multi-channel needs.
  - Design the host VI.
  - Avoid buffer errors.

Parent topic:

Transferring Data between the FPGA and Host

Related concepts:

- Transferring Data between the FPGA and Host
- Transferring Data between Devices or Structures Using FIFOs
- Limiting the Number of Top-Level Front Panel Objects in FPGA VIs
- Transferring Multi-Channel Data in DMA Applications
- Designing a Host VI to Read Data in DMA Applications
- Avoiding Buffer Errors in DMA Applications

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-using-front-panel-controls-and-indicators-fpga-module.html language=enus -->
## TOPIC 00169: Transferring Data Using Front Panel Controls and Indicators

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-using-front-panel-controls-and-indicators-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-using-front-panel-controls-and-indicators-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Read/Write Control function in a host VI to access the front panel controls and indicators of the FPGA VI, as shown in the following block diagram. Support for programmatic front panel communication varies by FPGA target. Refer to the specific FPGA target hardware documentation for more info

### Transferring Data Using Front Panel Controls and Indicators

Use the Read/Write Control function in a host VI to access the


 front panel controls and indicators of the FPGA VI, as shown in the following block


 diagram.

[IMAGE alt='image' src='GUID-2DD32DB9-A037-41E2-83AE-AFCC4170A297-a5.png']

Note

An advantage of programmatic front panel communication relative to other methods of


 transferring data between the FPGA and the host is its low overhead. Although you


 cannot attain high throughput with programmatic front panel communication, each call


 to the Read/Write Control function initiates data transfer with minimal delay.


 Therefore, programmatic front panel communication is ideal for small, frequent data


 transfers.

A disadvantage of programmatic front panel communication is that this method


 transfers only the most current data stored on the control or indicator of the FPGA


 VI. For example, data could be lost if the FPGA VI writes data to an indicator


 faster than the host VI can read the data. Also, each control or indicator on the


 FPGA VI uses resources on the FPGA. Best practices in FPGA programming recommend


 limiting the number of front panel objects in FPGA VIs. Finally,


 transferring data between the FPGA VI and the host VI using front panel controls and


 indicators requires the use of the host processor. As a result, the speed of data


 transfer is highly dependent upon the speed and availability of the host processor.


 A slower processor or lack of processor availability results in slower data transfer


 from the FPGA target to the host.

Parent topic:

Transferring Data between the FPGA and Host

Related concepts:

- Transferring Data between the FPGA and Host
- Limiting the Number of Top-Level Front Panel Objects in FPGA VIs
- Using a Host VI to Communicate with the FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-using-the-ni-scan-engine-and-variables-fpga-module.html language=enus -->
## TOPIC 00170: Transferring Data Using the NI Scan Engine and Variables

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-using-the-ni-scan-engine-and-variables-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-using-the-ni-scan-engine-and-variables-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you use programmatic front panel communication to transfer coherent sets of FPGA I/O data to an RT host VI, you must create block diagram code that synchronizes the FPGA VI with the host VI. If the FPGA target supports the NI Scan Engine, you can use the NI Scan Engine to synchronize this data tr

### Transferring Data Using the NI Scan Engine and Variables

If you use programmatic front panel communication to transfer coherent sets of FPGA


 I/O data to an RT host VI, you must create block diagram code that synchronizes the


 FPGA VI with the host VI. If the FPGA target supports the NI Scan Engine, you can


 use the NI Scan Engine to synchronize this data transfer. You then can use


 user-defined I/O variables to transfer data between the FPGA VI and the RT host VI.

Note

Using the NI Scan Engine reduces the amount of code you have to create to access and


 transfer coherent sets of data between FPGA I/O channels and the RT host VI. With


 user-defined I/O variables, you can process data on the FPGA target before sending


 that data to the RT host VI and after sending that data back to the FPGA VI. For


 example, you can create an application that executes the following steps:

1. Acquires analog I/O data and performs an FFT on the data in an FPGA VI
2. Transfers the processed data to a control loop in an RT VI
3. Transfers output data from the RT control loop back to the FPGA for output to


 the physical I/O channel

Steps 2 and 3 involve user-defined I/O variables to transfer data between the FPGA VI


 and RT VI.

(CompactRIO) Refer to the User-Defined IO Variable - Basic.lvproj in


 the labview\examples\CompactRIO\NI Scan Engine\Getting Started\User-Defined


 IO Variable - Basic\ directory for an example of using user-defined I/O


 variables.

#### Creating User-Defined I/O Variables

Right-click the chassis item in the Project Explorer window


 and select New»User-Defined Variable from the shortcut menu


 to create a new I/O variable. Because all I/O variables are unidirectional, you must


 configure the direction of each user-defined I/O variable as either FPGA


 to Host or Host to FPGA.

I/O variables that you create this way appear in a container labeled


 User-defined Variables.

Note

#### Caveats of User-Defined I/O Variables

Be aware of the following caveats when creating and using user-defined I/O


 variables:

- You must open a reference to an FPGA VI before using user-defined I/O


 variables.
- You can use user-defined I/O variables only on FPGA targets that support the NI


 Scan Engine. Refer to the target hardware documentation for information about


 support for the NI Scan Engine.
- User-defined I/O variables support scanned access only. You cannot use direct


 access for user-defined I/O variables.
- If you add a user-defined I/O variable node to the block diagram of an FPGA VI,


 you must set the execution mode of that FPGA VI to FPGA target. To change the


 execution mode of an FPGA VI, right-click the chassis item that contains that VI


 and select Select Execution Mode»FPGA Target . If you


 select Simulation (Simulated I/O) or


 Simulation (Real I/O) and that FPGA VI contains a


 user-defined I/O variable, the Run button appears broken


 and the FPGA VI cannot run.
- You can use user-defined I/O variables to communicate between only FPGA VIs and


 RT VIs running on the same chassis. However, if network publishing is enabled on


 a user-defined I/O variable, you can use the variable in any RT VI or


 Windows-based VI within the same LabVIEW project. For example, you can use


 network-published I/O variables to create a user interface VI that runs on


 Windows.

#### Accessing Timing Information from the NI Scan Engine

User-defined I/O variables rely on timing information from the NI Scan Engine. You


 can access this timing information by adding the Scan Clock I/O item to the block


 diagram of the FPGA VI. This I/O item transmits timing information, such as the


 number of FPGA clock cycles during which the signal is high, from the Scan Engine to


 the FPGA VI. Use this timing information to design an application that guarantees


 coherency of the data sets you transfer between the FPGA VI and the RT host VI.

Not all chassis support the Scan Clock I/O item. If you are using a chassis that does


 support this item, the item is located in the Project


 Explorer window under the Chassis I/O item


 for the FPGA Target. The following figure shows the location


 of this item.

[IMAGE alt='image' src='GUID-D80BB52B-5B72-4EFD-BC45-40B49370C689-a5.png']

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Transferring Data between the FPGA and Host

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-data-using-the-ni-scan-engine-and-variables-fpga-module_2.html language=enus -->
## TOPIC 00171: Transferring Data Using the NI Scan Engine and Variables

- bundle_id: `labview-fpga-module`
- source_path: `transferring-data-using-the-ni-scan-engine-and-variables-fpga-module_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-data-using-the-ni-scan-engine-and-variables-fpga-module_2.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you use programmatic front panel communication to transfer coherent sets of FPGA I/O data to an RT host VI, you must create block diagram code that synchronizes the FPGA VI with the host VI. If the FPGA target supports the NI Scan Engine, you can use the NI Scan Engine to synchronize this data tr

### Transferring Data Using the NI Scan Engine and Variables

If you use programmatic front panel communication to transfer coherent sets of FPGA


 I/O data to an RT host VI, you must create block diagram code that synchronizes the


 FPGA VI with the host VI. If the FPGA target supports the NI Scan Engine, you can


 use the NI Scan Engine to synchronize this data transfer. You then can use


 user-defined I/O variables to transfer data between the FPGA VI and the RT host VI.

Note

Using the NI Scan Engine reduces the amount of code you have to create to access and


 transfer coherent sets of data between FPGA I/O channels and the RT host VI. With


 user-defined I/O variables, you can process data on the FPGA target before sending


 that data to the RT host VI and after sending that data back to the FPGA VI. For


 example, you can create an application that executes the following steps:

1. Acquires analog I/O data and performs an FFT on the data in an FPGA VI
2. Transfers the processed data to a control loop in an RT VI
3. Transfers output data from the RT control loop back to the FPGA for output to


 the physical I/O channel

Steps 2 and 3 involve user-defined I/O variables to transfer data between the FPGA VI


 and RT VI.

(CompactRIO) Refer to the User-Defined IO Variable - Basic.lvproj in


 the labview\examples\CompactRIO\NI Scan Engine\Getting Started\User-Defined


 IO Variable - Basic\ directory for an example of using user-defined I/O


 variables.

#### Creating User-Defined I/O Variables

Right-click the chassis item in the Project Explorer window


 and select New»User-Defined Variable from the shortcut menu


 to create a new I/O variable. Because all I/O variables are unidirectional, you must


 configure the direction of each user-defined I/O variable as either FPGA


 to Host or Host to FPGA.

I/O variables that you create this way appear in a container labeled


 User-defined Variables.

Note

#### Caveats of User-Defined I/O Variables

Be aware of the following caveats when creating and using user-defined I/O


 variables:

- You must open a reference to an FPGA VI before using user-defined I/O


 variables.
- You can use user-defined I/O variables only on FPGA targets that support the NI


 Scan Engine. Refer to the target hardware documentation for information about


 support for the NI Scan Engine.
- User-defined I/O variables support scanned access only. You cannot use direct


 access for user-defined I/O variables.
- If you add a user-defined I/O variable node to the block diagram of an FPGA VI,


 you must set the execution mode of that FPGA VI to FPGA target. To change the


 execution mode of an FPGA VI, right-click the chassis item that contains that VI


 and select Select Execution Mode»FPGA Target . If you


 select Simulation (Simulated I/O) or


 Simulation (Real I/O) and that FPGA VI contains a


 user-defined I/O variable, the Run button appears broken


 and the FPGA VI cannot run.
- You can use user-defined I/O variables to communicate between only FPGA VIs and


 RT VIs running on the same chassis. However, if network publishing is enabled on


 a user-defined I/O variable, you can use the variable in any RT VI or


 Windows-based VI within the same LabVIEW project. For example, you can use


 network-published I/O variables to create a user interface VI that runs on


 Windows.

#### Accessing Timing Information from the NI Scan Engine

User-defined I/O variables rely on timing information from the NI Scan Engine. You


 can access this timing information by adding the Scan Clock I/O item to the block


 diagram of the FPGA VI. This I/O item transmits timing information, such as the


 number of FPGA clock cycles during which the signal is high, from the Scan Engine to


 the FPGA VI. Use this timing information to design an application that guarantees


 coherency of the data sets you transfer between the FPGA VI and the RT host VI.

Not all chassis support the Scan Clock I/O item. If you are using a chassis that does


 support this item, the item is located in the Project


 Explorer window under the Chassis I/O item


 for the FPGA Target. The following figure shows the location


 of this item.

[IMAGE alt='image' src='GUID-D80BB52B-5B72-4EFD-BC45-40B49370C689-a5.png']

Parent topic:

Transferring Data between the FPGA and Host

<!--NI_TOPIC bundle=labview-fpga-module path=transferring-multi-channel-data-in-dma-applications-fpga-module.html language=enus -->
## TOPIC 00172: Transferring Multi-Channel Data in DMA Applications

- bundle_id: `labview-fpga-module`
- source_path: `transferring-multi-channel-data-in-dma-applications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/transferring-multi-channel-data-in-dma-applications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you need to use DMA to transfer data from multiple I/O channels from an FPGA target to a host computer, NI recommends combining the data from each channel into a single array before writing the data to the DMA buffer. Combining data in this way is known as interleaving. Interleaving multi-channel

### Transferring Multi-Channel Data in DMA Applications

If you need to use DMA to transfer data from multiple I/O channels from an FPGA target to a


 host computer, NI recommends combining the data from each channel into a single


 array before writing the data to the DMA buffer. Combining data in this way is known


 as interleaving. Interleaving multi-channel data is useful because transferring the


 interleaved array requires only a single DMA channel, freeing up other DMA channels


 for other tasks. After you read the interleaved data from the DMA buffer, decimate


 the array to retrieve the data for each separate channel.

Note

#### Interleaving Data on the FPGA Target

The following figure shows an FPGA VI that acquires and interleaves data.

[IMAGE alt='image' src='GUID-8D97078C-0762-4577-A3E9-A31D4EDB8EDC-a5.png']

The VI in the previous figure acquires data from three input channels: AI0, AI1, and


 AI2. The VI uses the Build Array function to interleave data from these


 channels into a single array. Finally, the FIFO Method Node writes this single array


 to the DMA channel. The DMA channel transfers this array one element at a time from


 the FPGA target to the host computer.

Due to interleaving, the array contains the following elements:

| Array Element | Data |
| --- | --- |
| 0 | Sample 1 from AI0 |
| 1 | Sample 1 from AI1 |
| 2 | Sample 1 from AI2 |
| 3 | Sample 2 from AI0 |
| 4 | Sample 2 from AI1 |
| 5 | Sample 2 from AI2 |

Note

#### Decimating Data on the Host Computer

The following figure shows the VI that reads the data on the host computer.

[IMAGE alt='image' src='GUID-3EB75F0C-B652-4360-8D33-46470C67B32C-a5.png']

Note the following actions in the previous figure:

- When reading from a DMA channel, you must specify the Number of


 Elements to read. To calculate this number in this example,


 multiply the number of times you sampled each channel by the number of channels.


 In this example, the number of channels is three.
- The Decimate 1D Array function has been resized to contain three output terminals;


 therefore, this function splits the interleaved array into three separate


 arrays. The first array contains the measurements from AI0, the second array


 contains the measurements from AI1, and the third array contains the data from


 AI2. Note If you had a fourth channel of data, you would resize


 the Decimate 1D Array function to include a fourth output terminal.
- The purpose of the Build Array, Transpose 2D


 Array, and To Double


 Precision Float functions is to prepare the data for display on a


 waveform chart. You can replace these functions with ones that process the


 decimated data in the way that best fits your application.

Parent topic:

Transferring Data Using Direct Memory Access

Related concepts:

- Best Practices for DMA Applications
- Determining Whether an FPGA Target Supports DMA
- Transferring Data Using Direct Memory Access

<!--NI_TOPIC bundle=labview-fpga-module path=troubleshooting-timing-violations-fpga-module.html language=enus -->
## TOPIC 00173: Troubleshooting Timing Violations

- bundle_id: `labview-fpga-module`
- source_path: `troubleshooting-timing-violations-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/troubleshooting-timing-violations-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following strategies to troubleshoot a timing violation that appears in the Timing Violation Analysis window. If the target supports the Xilinx Options page, change some of the compilation options. Reduce long combinatorial paths. Use pipelining. Reduce the number of nested Case Stru

### Troubleshooting Timing Violations

You can use the following strategies to troubleshoot a timing violation that appears


 in the Timing Violation Analysis window.

- If the target supports the Xilinx Options page, change some of the compilation options.
- Reduce long combinatorial paths.
- Use pipelining.
- Reduce the number of nested Case


 Structures.
- Use smaller data types.
- Recompile the FPGA VI. Because the compilation process non-deterministically


 maps the FPGA VI to the FPGA, the process does not produce the same results each


 time you compile an FPGA VI. Therefore, if the FPGA VI missed the required clock


 rate by only a few nanoseconds, recompiling the FPGA VI might fix the timing


 violation.
- Reduce the clock rate of the application.
- Remove the implicit enable signal from single-cycle


 Timed Loops that run independently of other nodes on the block diagram. This


 strategy is most useful for very large designs.

Parent topic:

Debugging FPGA VIs

Related concepts:

- Changing the Top-Level FPGA Target Clock Rate

<!--NI_TOPIC bundle=labview-fpga-module path=tutorial-creating-test-benches-fpga-module.html language=enus -->
## TOPIC 00174: Tutorial: Creating Test Benches

- bundle_id: `labview-fpga-module`
- source_path: `tutorial-creating-test-benches-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/tutorial-creating-test-benches-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The tutorial in this topic covers the steps to complete to create a test bench for a simple FPGA VI that inverts values. Although the logic in the test bench will differ based on the logic in the FPGA VI you are testing, this tutorial outlines the common steps. The tutorial assumes knowledge of crea

### Tutorial: Creating Test Benches

The tutorial in this topic covers the steps to complete to create a test bench for a


 simple FPGA VI that inverts values. Although the logic in the test bench will differ


 based on the logic in the FPGA VI you are testing, this tutorial outlines the common


 steps. The tutorial assumes knowledge of creating VIs.

#### Creating an FPGA VI to Test

Complete the following steps to create an FPGA VI to test in this tutorial.

1. Create a LabVIEW project and save the project as


 inverter.lvproj .
2. Add an FPGA target to the project.
3. Right-click the FPGA target and select New»VI from the


 shortcut menu to create a new FPGA VI.
4. Save the FPGA VI as Inverter.vi .
5. Create two digital FPGA I/O items called input and


 output , respectively.
6. Drag the FPGA I/O items from the Project Explorer window


 to the block diagram of the Inverter VI to create corresponding FPGA I/O


 Nodes.
7. Right-click output on the FPGA I/O Node and select


 Change to Write from the shortcut menu.
8. Place the FPGA I/O Nodes within a While loop and wire the nodes together, as


 shown in the following block diagram: [IMAGE alt='image' src='GUID-6E73DC91-6AD2-4173-ACDB-31EB0F631747-a5.png']

The purpose of the Inverter VI is to read a digital line, invert the value, and write


 the inverted value to another digital line. Notice that the block diagram contains


 an error. The block diagram is missing a Not function between the two


 FPGA I/O Nodes.

#### Testing the FPGA VI on the Development Computer with Random Data

Complete the following steps to test the logic of the FPGA VI using random data for


 the input.

1. Right-click the FPGA target and select Properties from


 the shortcut menu.
2. In the FPGA Target Properties dialog box, select


 Execution Mode from the


 Category list to display the Execution


 Mode page.
3. In the Simulation pull-down menu, select Use


 Simulated I/O .
4. Click the OK button.
5. On the block diagram of the FPGA VI, right-click the wire connecting the two


 FPGA I/O Nodes and select Probe from the shortcut menu to


 create a probe.
6. Run the FPGA VI. Notice that the probe indicates values of TRUE and FALSE


 randomly.
7. Stop the FPGA VI.

#### Testing the FPGA VI on the Development Computer with a Custom VI

Complete the following steps to test the FPGA VI using a custom VI test bench.

1. On the Execution Mode page of the FPGA Target


 Properties dialog box, select Use Custom VI for FPGA


 I/O from the Simulation pull-down


 menu.
2. Click the New VI from Template button and save the custom


 VI as Simulated IO for Inverter.vi .
3. Click the Add button in the dialog that asks if you want


 to add the VI to the current project. Notice that LabVIEW adds the custom VI


 under My Computer in the project.
4. Open the block diagram of the Simulated IO for Inverter VI, read the comments in


 the VI, and delete the comments to reduce clutter on the block diagram. The


 block diagram of the Simulated IO for Inverter VI appears as shown in the


 following illustration: [IMAGE alt='image' src='GUID-F3262265-1B47-416A-83FA-F7668A43FADB-a5.png']
5. Right-click the I/O Item Name Case structure and select


 Duplicate Case from the shortcut menu.
6. Enter input in the selector label. The


 input case executes when the FPGA VI calls the FPGA


 I/O Node for the input I/O item. Note If


 you are using CLIP to pass data to the FPGA VI, you must place an extra


 backslash in the selector label for name of the CLIP I/O. For example, if


 the CLIP I/O item is CLIP\Port A, you must enter


 CLIP\\Port A in the selector label. The first backslash


 acts as an escape character for the second backslash in the name.
7. Right-click the Node or Element Type Case structure and


 select Duplicate Case from the shortcut menu. Notice that


 the Read I/O case is selected. This case executes for the


 FPGA I/O Node configured to read the input I/O item.
8. Delete the Report Support Error VI from the case and wire sim I/O


 info in and error out through the Case


 structure.
9. Replace the empty array with a True constant, To Variant function, and Build


 Array function as shown in the following block diagram: [IMAGE alt='image' src='GUID-A612096B-E54A-4A70-86D9-37DAA8EEAEB7-a5.png']
10. Run the Inverter VI. Notice that the probe on the wire between the two FPGA I/O


 Nodes indicates a value of TRUE because you included a True constant in the


 Simulated IO for Inverter VI. LabVIEW also returns an error message indicating


 that you did not specify behavior for the FPGA I/O Node configured for the


 output I/O item.

#### Testing the Output I/O Item

1. In the Project Explorer window, select My


 Computer and then select File»New to


 display the New dialog box.
2. Select Global Variable from the Other


 Files folder to create a new global VI.
3. Save the global VI as Test Bookkeeping .
4. Add a Boolean indicator called failed to the front panel


 of the Test Bookkeeping VI. The failed indicator is a


 global variable.
5. On the block diagram of the Simulated IO for Inverter VI, right-click the


 input case of the IO Item Name 


 Case structure and select Duplicate Case from the


 shortcut menu. Name the case as output .
6. In the Node or Element Type Case structure, select the


 Read I/O case, double-click the selector, and enter


 Write I/O . This case executes for the FPGA I/O Node for the


 output I/O item.
7. Delete the code that goes to the array of variants tunnel and add the Index


 Array function, Variant To Data function, and a Case structure with the


 failed global variable, as shown in the following


 block diagram. Because you specified TRUE as the value for the


 input I/O item, the value the Inverter VI writes to


 the output I/O item should be FALSE, if the code in the


 Inverter VI is correct. So, the test fails if the Inverter VI ever writes TRUE


 to the output I/O item. [IMAGE alt='image' src='GUID-5DC22B1C-084D-49B2-A194-DB0A1D68A89C-a5.png']
8. Run the Inverter VI and monitor the Test Bookkeeping VI. Notice that the


 failed indicator is TRUE, indicating that the test


 failed.
9. Stop the Inverter VI.
10. To fix the problem in the Inverter VI, add a Not function as shown in the


 following block diagram: [IMAGE alt='image' src='GUID-0488F0E0-8A4F-41E1-8D16-F4D255FCABEA-a5.png']
11. In the Test Bookkeeping VI, right-click the failed 


 indicator and select Data Operations»Reinitialize to Default


 Value from the shortcut menu. Now, when you run the Inverter VI,


 notice that the failed indicator remains FALSE,


 indicating that the test is not failing.

#### Testing the FPGA VI with a More Complex Custom VI

Complete the following steps to test that the Inverter VI behaves correctly for 10


 selected input values supplied sequentially.

1. In the Project Explorer window, right-click My


 Computer and select New»VI from the


 shortcut menu.
2. Save the VI as Test Stimulus.vi .
3. Update the Test Stimulus VI as shown in the following block diagram: [IMAGE alt='image' src='GUID-A0DEFA2C-CDDE-48CF-952A-5FFA12D3071F-a5.png']
4. Build the connector pane of the Test Stimulus VI so that you can use the VI as a


 subVI later in this tutorial.
5. In the Test Bookkeeping VI, add a stimulus index control


 that is a 32-bit signed integer. Also, add a test


 complete Boolean indicator, as shown in the following front


 panel: [IMAGE alt='image' src='GUID-803805E3-DAF7-45BF-8F65-896B96D0F3C2-a5.png']
6. In the Simulated IO for Inverter VI, update the


 Initializing case of the Execution


 Stage Case structure to initialize the values from the Test


 Bookkeeping VI as shown in the following block diagram. LabVIEW creates a clone


 of the custom VI for each case in the Execution Stage 


 Case structure. If you want to share data between different cases, you can use


 globals, as shown in the following block diagram, or some other mechanism that


 accounts for the cloned cases, such as non-reentrant subVIs. [IMAGE alt='image' src='GUID-7E0C70C2-8D12-48DC-8E3F-0F3BFB9F0D3B-a5.png']
7. Select the Running case from the Execution


 Stage Case structure, the input case from


 the I/O Item Name Case structure, and the Read


 I/O case from the Node or Element Type 


 Case structure.
8. Update the code for the Read I/O case of the


 Node or Element Type Case structure as shown in the


 following block diagram: [IMAGE alt='image' src='GUID-EF8619DE-4855-4535-9E64-9FD452E43ED7-a5.png']
9. Select the output case from the I/O Item


 Name Case structure and the Write I/O 


 case from the Node or Element Type Case structure.
10. Update the code for the Write I/O case of the


 Node or Element Type Case structure as shown in the


 following block diagram. The block diagram below gets the same stimulus as the


 read for the input, inverts the stimulus, compares the stimulus to the value the


 FPGA I/O Node receives, and declares test failure if the values are different.


 The block diagram also increments stimulus index until


 the index reaches 9, at which point the block diagram sets the test


 complete global variable to TRUE. [IMAGE alt='image' src='GUID-C4111C16-0FB6-42E7-8606-FD6DDF789C90-a5.png']
11. Run the Inverter VI and monitor the global variables in the Test Bookkeeping VI.


 Notice that stimulus index increases to 9,


 failed remains FALSE, and test


 complete remains FALSE until stimulus


 index reaches 9.
12. Stop the Inverter VI.

#### Using a Host VI to Automate Execution of the Test Bench

The test bench you created above requires some manual work to run an interpret


 results. To simplify repetition of the test, complete the following steps to create


 a host VI to automate execution of the test bench.

1. In the Project Explorer window, right-click My


 Computer and select New»VI from the


 shortcut menu.
2. Save the VI as Test Controller.vi and update the VI as shown in


 the following block diagram: [IMAGE alt='image' src='GUID-38091AF5-855B-464B-95EC-CB0216509E09-a5.png']

The Test Controller VI opens a reference to the Inverter VI and monitors the


 execution of the Inverter VI through global variables. After the test is complete or


 an error occurs, writing TRUE to the stop control stops the


 Test Controller VI. The Invoke Method configured for the Get FPGA VI Execution Mode


 method does not impact the execution, but the Invoke Method does provide access to


 any errors that might occur during execution of the FPGA VI on the development


 computer.

Parent topic:

Debugging FPGA VIs Using Simulation Mode

Related concepts:

- Determining When to Use Reentrant or Non-Reentrant SubVIs

<!--NI_TOPIC bundle=labview-fpga-module path=understanding-arbitration-options-fpga-module.html language=enus -->
## TOPIC 00175: Understanding Arbitration Options

- bundle_id: `labview-fpga-module`
- source_path: `understanding-arbitration-options-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/understanding-arbitration-options-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following arbitration options are available with the FPGA Module: Always Arbitrate Arbitrate if Multiple Requestors Only Never Arbitrate An arbiter performs the following general steps during arbitration. Waits for one or more requestors. If multiple requestors request access, the arbiter determ

### Understanding Arbitration Options

The following arbitration options are available with the FPGA Module:

- Always Arbitrate
- Arbitrate if Multiple



 Requestors Only
- Never Arbitrate

An arbiter performs the following general steps during arbitration.

1. Waits for one or more requestors. If multiple requestors request access, the



 arbiter determines which requestor becomes the accessor. Note The



 order in which an arbiter grants access to multiple requestors is



 non-deterministic.
2. Passes data from the accessor to the resource interface.
3. Begins resource execution.
4. Waits for the resource to complete execution.
5. Passes data back to the accessor.
6. Prepares the resource for another execution.
7. Waits for the next requestor.

Arbitration requires significant space on the FPGA. If you can decrease the number of



 requestors of a resource interface to one in the entire FPGA VI hierarchy, use the



 Arbitrate if Multiple Requestors Only or Never



 Arbitrate arbitration options. The single requestor requires no



 arbitration.

#### Always Arbitrate

A resource interface with the Always Arbitrate option always



 uses an arbiter, even if only one requestor requests access. The Always



 Arbitrate arbiter is a fair round robin arbiter that ensures



 sequential access to a shared resource. The arbiter does not allow a requestor to



 become an accessor again until all other waiting requestors have become accessors.



 Consequently, jitter occurs if you have more than one simultaneous requestor.

Use the Always Arbitrate option if you need single requestor



 channels synchronized with multiple requestor channels. Refer to Timing FPGA VIs with Arbitration Enabled for information about



 synchronized channels.

#### Arbitrate if Multiple Requestors Only

A resource interface with the Arbitrate if Multiple Requestors



 Only option does not use an arbiter if the FPGA VI contains only one



 requestor. If the resource interface has multiple requestors, LabVIEW generates



 arbitration circuits even if the requests are not simultaneous. You can save time



 and space in FPGA VIs if you use the Arbitrate if Multiple Requestors



 Only arbitration option if the shared resource contains only one



 requestor in the entire FPGA VI hierarchy.

Use the Arbitrate if Multiple Requestors Only option in the



 following situations:

- You have a large FPGA VI and need to save space.
- You have only one accessor for a resource interface in the entire FPGA VI



 hierarchy.
- You do not need single requestor channels synchronized with multiple requestor



 channels. Refer to Timing FPGA VIs with Arbitration Enabled for information about



 synchronized channels.
- You use a FIFO Method Node configured with the Read or Write method in a single-cycle Timed



 Loop.
- You use a Memory Method Node configured with the Read or Write method



 in a single-cycle Timed Loop.
- You have digital outputs in a single-cycle Timed Loop.

#### Never Arbitrate

If you select the Never Arbitrate option for a resource interface, LabVIEW does not add arbitration components, which



 saves significant space on the FPGA. In addition to saving space, the



 Never Arbitrate option allows some of the FPGA I/O and FIFO



 functions to execute in a single clock cycle. However, in cases where there are



 multiple accessors, multiple signals will be combined into one signal, resulting in



 additional logic. To use the Never Arbitrate option, you must



 guarantee sequential access to the resource interface in the data flow of the FPGA



 VI, as shown in the following block diagram.

Note

[IMAGE alt='image' src='GUID-8ADDFE7F-C17D-453E-9B80-7112DB311A9D-a5.png']

In the block diagram above, the Flat Sequence structure ensures that the two FIFO



 Method Nodes do not execute simultaneously, so resource contention does not occur.



 In such situations, Never Arbitrate is an appropriate option.



 However, if you select the Never Arbitrate option and make



 simultaneous requests, the behavior of the FPGA VI is undefined and data corruption



 is possible.

Note

Selecting the Never Arbitrate option when simulating an FPGA



 application that contains memory items with multiple accessors may result in



 incorrect behavior. For example, if your application includes multiple writers, each



 writer can update the memory address specified during simulation. Additionally, if



 your application includes multiple readers, each reader can assess the memory



 address specified during simulation.

Parent topic:

Managing Shared Resources

Related concepts:

- Avoiding Arbitration to Optimize FPGA VIs
- Controlling I/O Power-On States
- Managing Shared Resources
- Avoiding Jitter Due to Resource Contention
- Timing FPGA VIs with Arbitration Enabled

<!--NI_TOPIC bundle=labview-fpga-module path=understanding-the-labview-fpga-compile-system-fpga-module.html language=enus -->
## TOPIC 00176: Understanding the LabVIEW FPGA Compile System

- bundle_id: `labview-fpga-module`
- source_path: `understanding-the-labview-fpga-compile-system-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/understanding-the-labview-fpga-compile-system-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA compile system consists of three major components: LabVIEW, the compile server, and the compile worker. These three components have the following roles in compiling FPGA VIs into bitfiles to download to the FPGA chip on the target: LabVIEW—Sends compile job requests to the compile s

### Understanding the LabVIEW FPGA Compile
 System

The LabVIEW FPGA compile system consists of three major components: LabVIEW, the


 compile server, and the compile worker. These three components have the following


 roles in compiling FPGA VIs into bitfiles to download to the FPGA chip on the


 target:

- LabVIEW —Sends compile job requests to the compile


 server.
- Compile server —Receives requests from LabVIEW and sends


 compile jobs to an available compile worker.
- Compile worker —Takes job requests from the compile server


 and compiles the FPGA VI.

If you installed the LabVIEW FPGA Module and the Xilinx compilation tools on the same


 computer, this three-component architecture does not require any special


 configuration. By default, LabVIEW and the compile worker use the compile server


 installed on the local computer, called localhost. If you install


 the Xilinx compilation tools on a remote computer, you can compile the FPGA VI


 remotely using one or more remote compile workers.

#### How the Compilation Process Works

The compilation time depends on the size of the VI, the processor speed, and the


 amount of memory in the computer on which you are compiling. If the computer does


 not have sufficient memory, smaller block diagrams might compile quickly, but larger


 block diagrams might use large amounts of virtual memory, which can cause


 compilations to fail or take over 10 times longer to complete.

The following steps outline the process of compiling FPGA VIs. LabVIEW displays


 compilation status in the Compilation Status window. You can


 view the different compilation reports if you are connected to the compile


 server.

1. Generation of intermediate files —LabVIEW converts the


 FPGA VI into intermediate files (HDL code) to send to the compile server.
2. Queuing —The compile server queues jobs and send the


 intermediate files to the compile worker for compiling.
3. HDL compilation, analysis, and synthesis —The compile


 worker transforms intermediate files (HDL code) into digital logic


 elements.
4. Mapping —The compile worker divides the application logic


 between the physical building blocks on the FPGA.
5. Placing and routing —The compile worker assigns the logic


 to physical building blocks on the FPGA and routes the connections between the


 logic blocks to meet the space or timing constraints of the compilation.
6. Generating programming file —The compile worker creates


 binary data that LabVIEW saves inside a bitfile.
7. Creating bitfile —LabVIEW saves the bitfile in a


 subdirectory of the project directory and can download and/or run the


 application on the FPGA VI.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Compiling an FPGA VI Remotely
- Viewing the Bitfile Path

<!--NI_TOPIC bundle=labview-fpga-module path=understanding-the-simulation-vhdl-framework-fpga-module.html language=enus -->
## TOPIC 00177: Understanding the Simulation VHDL Framework

- bundle_id: `labview-fpga-module`
- source_path: `understanding-the-simulation-vhdl-framework-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/understanding-the-simulation-vhdl-framework-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use third-party simulation, understanding the simulation export VHDL framework can help you successfully debug the FPGA VI. The test bench framework, tb_NiFpgaSimulationModel, contains a hierarchy of models necessary for simulation, as shown in the following illustration. The following list

### Understanding the Simulation VHDL Framework

When you use third-party simulation, understanding the simulation export VHDL


 framework can help you successfully debug the FPGA VI.

The test bench framework, tb_NiFpgaSimulationModel, contains a


 hierarchy of models necessary for simulation, as shown in the following


 illustration.

[IMAGE alt='image' src='GUID-CE11DE4E-010D-4366-A88C-CD39A33CAF77-a5.png']

The following list describes the components of the simulation test bench in more


 detail.

tb_NiFpgaSimulationModel—The default name of the overarching
 test bench framework. The name always begins with tb_and ends with
 the name you specify in the Top-level simulation model name
 text box on the Information page of the Simulation Export Properties dialog box.

- Main stimulus process —Add code here to set controls, read
 indicators, and perform other stimulus for the FPGA VI. Enter the code you want
 between the NiFPGA_Run and NiFpga_Close 
 lines.
- NiFpgaSimulationModel —The simulation model.
  - NiFpgaSimInterface —The bus interface, or the VHDL
 that LabVIEW provides to communicate with the target-specific code. The
 name always begins with NiFpgaSim and includes
 interface . Other parts of this name depend on the
 target.
  - Toplevel 
 Framework —Target-specific code. The exact name of
 this model grouping varies by target.
    - TheWindow —The code that you want to
 interact with. TheWindow groups CLIP code and
 FPGA VI code.
      - Clip —The CLIP simulation code for
 the CLIP instances you specify in the LabVIEW project.
 You specify the simulation behavior for the CLIP on the
 Name and Source page of the Configure Component-Level IP
 wizard. Any code under this model grouping is
 user-defined.
      - TheVI —The code that LabVIEW
 generates for the FPGA VI. LabVIEW derives the name of
 TheVI from the name of the
 top-level VI you specify on the Source Files page of the
 Simulation Export Properties dialog box.
        - Controls and
 indicators —Code for the controls and
 indicators in the FPGA VI. This part of the model
 also contains code to handle resetting the FPGA
 VI.
        - VI logic —This part of the
 model contains code to run the VI logic from the
 block diagram of the FPGA VI. The code hierarchy
 in this part of the model reflects the hierarchy
 of the block diagram. For example, entities in the
 model such as single-cycle Timed Loops, Flat
 Sequence structures, and Case structures contain
 VHDL code to represent the nodes found in these
 structures on the block diagram.
      - (Optional) I/O Stimulus/Response—This part of the model
 contains code that you add to simulate FPGA target
 I/O.

#### Details for VI Logic Found under TheVI

Structures with multiple subdiagrams, such as Case structures and Flat Sequence


 structures, have a separate VHDL entity for each case or frame. These VHDL entities


 have names ending with _diag to indicate that they represent a


 subdiagram.

Reentrant subVIs appear in the VHDL code in the same manner as structures appear.


 Reentrant subVIs have multiple instances in the VHDL code hierarchy. These instances


 correspond to calls to the subVIs from the block diagram.

Non-reentrant subVIs include special VHDL logic to manage the data flow to and from


 reentrant subVIs.

The VHDL code also contains entities representing LabVIEW VIs and functions. Most of


 these elements are encrypted, but you can see incoming and outgoing values on their


 port maps.

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

Related concepts:

- Using the Configure Component-Level IP Wizard

<!--NI_TOPIC bundle=labview-fpga-module path=understanding-timing-considerations-for-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00178: Understanding Timing Considerations for FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `understanding-timing-considerations-for-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/understanding-timing-considerations-for-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To execute code using a dataflow model, LabVIEW synchronizes logic on the FPGA. By default, LabVIEW FPGA places a register between logic functions on the block diagram to maximize the propagation time available for each operation to execute. Propagation delay is the time it takes a signal to travel

### Understanding Timing Considerations for FPGA VIs

To execute code using a dataflow


 model, LabVIEW synchronizes logic on the FPGA. By default, LabVIEW FPGA


 places a register between logic functions on the block diagram to maximize the


 propagation time available for each operation to execute.

Propagation delay is the time it takes a signal to travel from one register to the


 next. The combinatorial path is the collection of logic and wiring that a signal


 encounters from one register to the next.

Because registers update every clock cycle, the propagation delay must not exceed


 the clock cycle. Propagation delay consists of two components, logic delay and


 routing delay. Logic delay, which is a function of the number and type of logic


 gates the signal traverses, often represents the most significant component of


 propagation delay. Routing delay, which is a function of the length of the wire path


 the signal traverses, is generally small, because the FPGA compiler attempts to


 cluster the components of a combinatorial path as tightly as possible on the FPGA.


 However, as the FPGA VI approaches the size limits of the FPGA, the physical


 separation between functions increases, and routing delay can become a significant


 component of the total propagation delay between two registers. The FPGA compiler


 returns a timing error if the propagation delay between any two registers exceeds


 the FPGA clock rate. This timing error is known also as a time constraint or period


 constraint violation.

Note

The LabVIEW FPGA Module is designed to produce circuits that can run at a clock rate


 of at least 40 MHz outside the single-cycle Timed Loop. A 40 MHz clock rate


 corresponds to a 25 nanoseconds clock cycle. To prevent the propagation delay


 between two registers from exceeding 25 ns, most LabVIEW functions include an output


 register and thus require a full clock cycle to execute. If the propagation delay


 between two registers exceeds 25 ns, the FPGA VI cannot compile at the 40 MHz


 default clock rate.

For example, suppose function A requires a 6 ns logic delay and function B requires a


 14 ns logic delay. If you wire functions A and B in sequence without a register


 between them, the total logic delay is 20 ns, which leaves 5 ns for routing delay if


 you want the functions to compile at the 40 MHz default clock rate. Depending on how


 the FPGA compiler routes the wires between the functions, the routing delay might or


 might not exceed 5 ns, as shown in Scenarios 1 and 2 below.

[IMAGE alt='image' src='GUID-929E9A6A-61C6-45B1-B9CE-1A17A60B3699-a5.png']

In Scenario 1, the design meets the timing constraints of a 40 MHz clock. In Scenario


 2 the design does not meet the timing constraints of a 40 MHz clock and produces a


 timing violation error when you try to compile the FPGA VI. In contrast, Scenario 3,


 below, illustrates a register between the two functions. This register placement


 results in two separate propagation delays. Each of these separate propagation


 delays can compile at 40 MHz, even if the routing delay is long.

[IMAGE alt='image' src='GUID-CDF827A2-25E9-4475-AA94-E90BF311218C-a5.png']

When a function is not in a single-cycle Timed Loop, the FPGA compiler places


 registers at regular intervals between the logic levels in a function to break up


 the logic into portions that can execute at the default FPGA clock rate. When a


 function that includes internal registers, such as the Memory Method


 Node, runs on the FPGA, the function takes as many clock cycles to


 execute as the number of registers in the function.

When you need logic to execute with lower latency at the same clock rate, you can use


 the single-cycle Timed Loop. When you place a function inside a single-cycle


 Timed Loop, the compiler does not include an output register for the function, so


 the single-cycle Timed Loop can execute within one clock cycle. Some functions, such


 as the Scaled Window or FFT Express VI, take


 multiple clock cycles even when these functions are located in single-cycle Timed


 Loops. Use handshaking to schedule the timing of data for these functions.

If the propagation delay within a single-cycle Timed Loop exceeds the clock cycle,


 the Timing Violation Analysis window tells you which


 single-cycle Timed Loop failed to meet timing requirements. In some cases, you can


 reduce the length of a combinatorial path by using Feedback Nodes or


 shift registers to implement a pipelined design.

Note

#### Resource Considerations for Large FPGA Applications

Every FPGA target contains a limited number of flip-flops. Because registers use


 flip-flops, the number and type of registers used by an FPGA VI can determine


 whether the FPGA VI fits on the FPGA target. In general, the number of flip-flops


 used by a register corresponds to the width of the data type. For example, a Boolean


 register needs only one flip-flop to store data while an I64 register requires 64


 flip-flops to store data.

For most users, the limited number of flip-flops on an FPGA is not a problem.


 However, if you run into space limitations on the FPGA, you must optimize the FPGA VI for size.

Parent topic:

Using FPGA Clocks and Timing

Related concepts:

- Introduction to FPGA Hardware Concepts
- Optimizing FPGA VIs Using Pipelining
- Reducing Combinatorial Paths in FPGA VIs
- Using Single-Cycle Timed Loops to Optimize FPGA VIs
- Scheduling Timing Using Handshaking Signals

<!--NI_TOPIC bundle=labview-fpga-module path=unsupported-labview-features-fpga-module.html language=enus -->
## TOPIC 00179: Unsupported LabVIEW Features

- bundle_id: `labview-fpga-module`
- source_path: `unsupported-labview-features-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/unsupported-labview-features-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Restricted and Unavailable LabVIEW Features ActiveX Conditional loop tunnels Dialog boxes File I/O Double-precision or extended-precision floating-point operations For Loop iteration parallelism Math and Signal Processing VIs not specific to the FPGA Module Printing Programmatic menus Shared variabl

### Unsupported LabVIEW Features

#### Restricted and Unavailable LabVIEW Features

- ActiveX
- Conditional loop tunnels
- Dialog boxes
- File I/O
- Double-precision or extended-precision floating-point operations
- For Loop iteration parallelism
- Math and Signal Processing VIs not specific to the FPGA Module
- Printing
- Programmatic menus
- Shared variables (except some targets that



 support the NI Scan Engine)
- Arrays that do not resolve to a single size at compile time
- Multidimensional arrays
- VI Server
- VI Server properties and methods

Support for other LabVIEW features varies by target.

#### Multidimensional Arrays or Arrays Unresolvable to a Single Size at Compile



 Time

You can use only one-dimensional arrays in FPGA VIs. LabVIEW must statically determine the size of an array at compile



 time. If necessary, you can make any array constant, control, or



 indicator fixed-size by right-clicking the array index and selecting Set



 Size from the shortcut menu. This option is only available in FPGA



 VIs.

LabVIEW must resolve arrays to a single size at compile time. This might mean that



 certain properties of the array, such as its length or the indexes of the elements



 you read/write, must be constant values. For example, if you use the Array



 Subset function, the index and



 length inputs must be constant so that LabVIEW can



 determine a set size for the output subarray. You can either



 wire constant values directly to array functions, or rely on value propagation



 through constant folding.

Tip

#### Shared Variables and the NI Scan Engine

Support for shared variables varies by FPGA target and RT controller. Not all



 CompactRIO RT controllers support the NI Scan



 Engine. Refer to the specific FPGA target or RT controller hardware documentation for more information about FPGA target and RT



 controller functionality.

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=user-manual-welcome.html language=enus -->
## TOPIC 00180: LabVIEW FPGA Module User Manual

- bundle_id: `labview-fpga-module`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### LabVIEW FPGA Module
 User Manual

The LabVIEW FPGA Module User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- LabVIEW User Manual
- LabVIEW FPGA Module Programming Reference Manual
- LabVIEW High-Performance FPGA Developer's Guide
- LabVIEW for CompactRIO Developer's Guide
- NI Learning Center
- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums

<!--NI_TOPIC bundle=labview-fpga-module path=using-a-host-vi-to-communicate-with-the-fpga-target-fpga-module.html language=enus -->
## TOPIC 00181: Using a Host VI to Communicate with the FPGA Target

- bundle_id: `labview-fpga-module`
- source_path: `using-a-host-vi-to-communicate-with-the-fpga-target-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-a-host-vi-to-communicate-with-the-fpga-target-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can programmatically interact with an FPGA VI using a separate VI running on the host computer. This programmatic FPGA interface communication differs from interactive front panel communication because it requires you to create a host VI as well as an FPGA VI. When you use programmatic FPGA inte

### Using a Host VI to Communicate with the FPGA Target

You can programmatically interact with an FPGA VI using a separate VI running on the


 host computer. This programmatic FPGA interface communication differs from


 interactive front panel communication because it requires you to create a host VI as


 well as an FPGA VI.

When you use programmatic FPGA interface communication, the FPGA VI runs on the FPGA


 target, and the host VI runs on the host computer, as shown in the following


 illustration.

[IMAGE alt='image' src='GUID-CB4839D0-82C0-464B-9DE3-E5C3BA47FDE6-a5.png']

You use a host VI to send information between the host computer and the FPGA target


 for the following reasons:

- You want to do more data processing than you can fit on the FPGA.
- You need to perform operations not available on the FPGA target, such as


 double-precision or extended-precision floating-point arithmetic.
- You want to create a multi-tiered application with the FPGA target as a


 component of a larger system.
- You want to log data.
- You want to control the timing and sequencing of data transfer.
- You want to create a test bench for an FPGA VI.

The host computer can be a Windows-based computer or an RT target. Both the Windows


 OS and RT OS support the FPGA


 Interface functions. In addition, you can use the FPGA Interface


 functions on the RT target to communicate with the FPGA target and then use a


 Windows-based computer to communicate with the RT target.

Note

The following steps outline the general programming sequence for the host VI:

1. Open a reference to an FPGA VI, build specification or bitfile.
2. Send or receive data using the FPGA Interface functions, such as the Read/Write Control and Invoke


 Method functions.
3. Close the FPGA reference with the Close FPGA


 VI Reference function.

The following block diagram shows a simple host VI that demonstrates this


 architecture. In this host VI, the application writes a value to the Boolean


 control, DIO1, on the FPGA and reads a value from the Boolean


 indicator, DIO0, on the FPGA.

[IMAGE alt='image' src='GUID-6215FFC1-239D-411A-A796-FEE3F2CA4E58-a5.png']

The code in the While loop changes depending on your application and the way you


 transfer data between the FPGA and the host.

Parent topic:

Creating FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Communicating with FPGA Targets from a Host Computer
- Creating a Custom VI to Simulate I/O
- Transferring Data Using Front Panel Controls and Indicators

<!--NI_TOPIC bundle=labview-fpga-module path=using-clip-clocks-fpga-module.html language=enus -->
## TOPIC 00182: Using CLIP Clocks

- bundle_id: `labview-fpga-module`
- source_path: `using-clip-clocks-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-clip-clocks-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can instantiate clock circuitry in component-level IP (CLIP) and use CLIP clocks in thesame way you use other clocks that the target provides. You also can route external clocks supplied by socketed CLIP to LabVIEW. CLIP clocks cannot be top-level clocks. Any clocks in the CLIP declaration file

### Using CLIP Clocks

You can instantiate clock circuitry in component-level IP (CLIP) and use CLIP clocks


 in thesame way you use other clocks that the target provides. You also can route external clocks


 supplied by socketed CLIP to LabVIEW. CLIP clocks cannot be top-level clocks. Any


 clocks in the CLIP declaration file appear automatically under the


 CLIP item in the Project


 Explorer window.

You cannot use the Start Enabling FPGA Clock and Start Disabling FPGA


 Clock VIs with CLIP clocks to protect circuitry when the clock might not


 be available.

#### Including Clocks in the VHDL File

To ensure the CLIP clock uses a low-skew global clock net, you must use a global


 clock buffer (BUFG). NI recommends using a global clock buffer with gated input


 (BUFGCE) to ensure that the clock is disabled whenever the clock has glitches or


 violates the period constraint for the clock. Refer to the Xilinx documentation for information about creating a clock in


 VHDL.

Refer to the example of VHDL code for a CLIP clock for a demonstration of creating a clock in


 VHDL code.

#### Including Clocks in the CLIP Declaration File

You define a clock in the CLIP declaration file using the same syntax as defining


 I/O. The order that clock and I/O appear in the declaration file dictates the order


 in which they appear in the LabVIEW project. For the CLIP clock, you must define the following tags.

- JitterInPicoSeconds
- AccuracyInPPM
- DutyCyclePercentInMin/Max

Use the Configure Component-Level IP wizard (CLIP wizard) to define the IP


 interface without editing the declaration XML file by hand.

Note

| CLIP Declaration Tag | Type of Xilinx Document | Suggested Search Terms to Find Information |
| --- | --- | --- |
| JitterInPicoSeconds | DC and Switching Characteristics | Output Clock Jitter |
| AccuracyInPPM | DC and Switching Characteristics | Output Clock Phase Alignment |
| DutyCyclePercentInMin/Max | User Guide | DCM attributes |

#### Adding CLIP Clocks to a LabVIEW Project

Complete the following steps to add a CLIP clock to a LabVIEW project.

1. Create a new project or open an existing


 project.
2. Add an FPGA target to the project.
3. Add a CLIP item to the project..
4. (Optional) Right-click the CLIP clock under the CLIP item in the


 Project Explorer window and select


 Properties from the shortcut menu to display the


 FPGA


 CLIP Clock Properties dialog box.
5. (Optional) Rename the clock in the Name text box. All


 other components in the dialog box are dimmed but show the values of the CLIP


 clock. You cannot configure the CLIP clock from LabVIEW. You must update the


 CLIP clock in the CLIP declaration file to change the clock configuration.
6. Click the OK button.

#### Deriving Clocks from CLIP Clocks

You can derive clocks from CLIP clocks. You must configure the CLIP clock to compile


 at a single frequency to enable the option to create a new derived clock.

Complete the following steps to derive a clock from an external clock:

1. Follow the instructions above to add a CLIP clock to the LabVIEW project.
2. Right-click the CLIP clock in the Project Explorer window. From the shortcut


 menu, select New FPGA Derived Clock to display the FPGA Derived Clock Properties dialog box.
3. Configure the clock.
4. Define the following tags in the CLIP


 declaration XML file file:
  - SupportDerivedClocks
  - SourceClockReadyHDLName
  - DerivedClocksValidHDLName

#### Using CLIP Clocks in SubVIs

You can use the clock constant or clock


 control to reference a CLIP clock in a subVI.

The name of the clock in the control or constant must match the name of the clock in


 the Project Explorer window exactly. If the names do not


 match, you receive an error message when you compile the FPGA VI. Use the pull-down menu of the FPGA clock constant


 or control to ensure the clock name you specify matches the name of the clock in the


 project.

#### Accessing CLIP I/O Using a Different Clock than the CLIP Clock

You must consider clock domains when using CLIP I/O in a single-cycle Timed


 Loop using a different clock than the CLIP clock. If the CLIP executes in


 one clock domain and the FPGA VI accesses the corresponding CLIP I/O using a


 different clock domain, the signals can transfer between clock domains incorrectly.


 If this happens, the Timing


 Violation Analysis window displays a timing violation.

To avoid transferring data between clock domains incorrectly, use one of the


 following strategies.

- Change the FPGA VI so that the CLIP and the single-cycle Timed Loop use the same


 clock.
- Redesign the FPGA using other methods of implementing multiple clock domains.
- Change the CLIP


 declaration XML file so that the CLIP I/O uses the same clock domain


 as the CLIP clock.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- Example VHDL Code for CLIP Clocks
- Using FPGA Clocks and Timing
- Adding FPGA Targets to a LabVIEW Project
- Compiling, Downloading, and Running FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-custom-data-types-with-register-items-memory-items-fifos-and-handshake-items-fpga-module.html language=enus -->
## TOPIC 00183: Using Custom Data Types with Register Items, Memory Items, FIFOs, and Handshake Items

- bundle_id: `labview-fpga-module`
- source_path: `using-custom-data-types-with-register-items-memory-items-fifos-and-handshake-items-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-custom-data-types-with-register-items-memory-items-fifos-and-handshake-items-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom controls of supported data types and select these controls as data types for FPGA register items, memory items, FIFOs, and handshake items. The custom control you select as a data type in the Register Properties, Memory Properties, FIFO Properties, or Handshake Properties dialo

### Using Custom Data Types with Register Items, Memory Items, FIFOs, and Handshake Items

You can create custom controls of supported data types and select these controls as


 data types for FPGA register items, memory items, FIFOs, and handshake items. The


 custom control you select as a data type in the Register


 Properties, Memory


 Properties, FIFO


 Properties, or Handshake


 Properties dialog boxes can be any control, type definition (typedef), or


 strict typedef created with supported data types. If the custom control is a typedef


 or strict typedef, LabVIEW disconnects the control from the typedef.

Using custom data types has the following advantages:

- Simplifies block diagrams and can increase application throughput.
- For some FPGA targets, breaks the 64-bit barrier by joining two small supported


 types into one larger data type. Refer to the specific FPGA target hardware documentation for more information about


 supported data types.
- Keeps resources separate for each value in the FIFO or memory.

Note

#### Combining Smaller Data Types While Keeping Resource Identities Separate

In the following example, the FIFO can transfer both address and data information in


 a single cluster element. Using a custom control, these values remain distinct so


 that you can split the values after reading the element from the FIFO.

[IMAGE alt='image' src='GUID-319A83F7-74E5-436A-87D7-823DBB20D5B3-a5.png']

#### Caveat when Using Custom Controls

Using large custom controls can affect the performance of an FPGA VI or waste FPGA


 resources.

Parent topic:

Storing and Transferring Data

Related concepts:

- Optimizing FPGA VIs for Speed and Size
- Supported Data Types

<!--NI_TOPIC bundle=labview-fpga-module path=using-dram-fpga-module.html language=enus -->
## TOPIC 00184: Using DRAM

- bundle_id: `labview-fpga-module`
- source_path: `using-dram-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-dram-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to access and configure DRAM on FPGA targets using LabVIEW FPGA memory items. Some FPGA targets contain onboard dynamic random access memory (DRAM) that you can access directly from the FPGA VI. LabVIEW supports DRAM access through FPGA memory items, which provide usability and VHDL optimi

### Using DRAM

Learn how to access and configure DRAM on FPGA targets using LabVIEW FPGA memory
 items.

Some FPGA targets contain onboard dynamic random access memory (DRAM) that you can
 access directly from the FPGA VI. LabVIEW supports DRAM access through FPGA memory
 items, which provide usability and VHDL optimization similar to block memory and
 LUT.

#### Accessing DRAM

Use the FPGA memory item interface in the project to access DRAM. DRAM memory items
 appear in the Project Explorer under the FPGA target.

You cannot use VI-defined memory items to configure DRAM.

#### Partitioning DRAM into Multiple
 Memory Items

You can partition physical DRAM banks into multiple memory items using the Memory
 Properties dialog. For example, if a target has two physical DRAM banks, you could
 partition one bank into three memories and the other into five. LabVIEW treats each
 memory independently.

Note

Check DRAM Availability on an FPGA
 Target

Figure 3.

[IMAGE alt='Diagram showing DRAM Bank 0 with three partitions and DRAM Bank 1 with five partitions.' src='GUID-EBB91868-DF7B-44BC-8212-9F64BF865F81-a5.png']

After creating partitions, configure arbitration between partitions in the same DRAM
 bank using the DRAM Properties page of the FPGA Target Properties dialog.

#### Arbitrating Access to the DRAM
 Bank

If you partition the DRAM into multiple memory items, you can configure the amount of
 time LabVIEW grants to each partition. By default, LabVIEW grants equal time to all
 partitions. This DRAM arbiter is not the same arbiter that arbitrates between
 different requestors of the same shared resource.

Specify the time to grant each partition under FPGA Target Properties»DRAM Properties. LabVIEW grants time to each partition using
 round robin scheduling.

#### Understanding Latency and
 DRAM

- Use the Request Data and Retrieve Data methods to read data from DRAM.
- Queue multiple requests for data using Request Data and retrieve requested
 data using Retrieve Data.
- DRAM returns requested data when you indicate readiness using handshaking
 signals.

To optimize performance, send requests for data or write data in bursts, such as on
 each clock cycle.

Parent topic:

FPGA Memory Items

Related concepts:

- Managing Shared Resources
- Scheduling Timing Using Handshaking Signals

Related tasks:

- Check DRAM Availability on an FPGA Target

<!--NI_TOPIC bundle=labview-fpga-module path=using-dynamic-fpga-interface-references-fpga-interface.html language=enus -->
## TOPIC 00185: Using Dynamic FPGA Interface References

- bundle_id: `labview-fpga-module`
- source_path: `using-dynamic-fpga-interface-references-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-dynamic-fpga-interface-references-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create subVIs that work with interfaces from different FPGA VIs or bitfiles as long as the relevant portions of the communication hardware interface to the host are compatible. The communication hardware interface includes the following: Names and types of controls and indicators Names, data

### Using Dynamic FPGA Interface References

You can create subVIs that work with interfaces from different FPGA VIs or bitfiles as


 long as the relevant portions of the communication hardware interface to the host


 are compatible. The communication hardware interface includes the following:

- Names and types of controls and indicators
- Names, data types, and types of DMA or peer-to-peer FIFOs
- Names, directions, and types of target-specific methods

These subVIs can work with any FPGA reference that implements the specified


 interface, even if the reference is to VIs or bitfiles on different target types.


 For example, you can use the same subVI for both a PCI and a PXI target.

To make an FPGA reference dynamic, place a checkmark in the Dynamic


 mode checkbox of the Configure


 Open FPGA VI Reference dialog box. You also can use the FPGA Interface Dynamic Refnum constant and Dynamic FPGA Interface Cast function to specify an FPGA


 interface. To create a subVI, change the constant to a control or indicator by


 right-clicking the constant and selecting Change to Control


 or Change to Indicator from the shortcut menu.

#### Edit-Time and Run-Time Errors

LabVIEW returns edit-time and run-time errors when using the dynamic mode of FPGA


 interfaces. The following examples describe situations when edit-time or run-time


 errors may occur:

- Edit-time error—Occurs if you use an Invoke


 Method function to configure a FIFO and then remove the FIFO from the


 project. The Invoke Method function causes a broken Run 


 button.
- Run-time error—Occurs if you cast a reference using the Dynamic FPGA Interface Cast function and use a Read/Write Control function to access an indicator,


 foo , on a reference that does not contain


 foo .

#### Ensuring that Dynamic Mode References Do Not Break Downstream Nodes

If you configure the FPGA VI reference with the dynamic mode option and it contains


 more elements than a subVI interface requires, you can encounter coercion problems


 that may break downstream nodes. To ensure that the dynamic FPGA interface reference


 that exits the subVI contains the same elements as the FPGA interface reference that


 entered the subVI, you have the following options:

- Branch the input wire to the reference from the calling VI.
- Wire the input reference of the subVI directly to the output reference.

Parent topic:

Communicating with FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-fixed-size-arrays-in-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00186: Using Fixed-Size Arrays in FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-fixed-size-arrays-in-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-fixed-size-arrays-in-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Module supports one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size of an array, consider using a fixed-size array in your FPGA VI. Creating Fixed-Size Array Controls Complete the following steps to create a fixed-size array control: A

### Using Fixed-Size Arrays in FPGA VIs

The FPGA Module supports one-dimensional arrays that resolve to a single size at


 compile time. If LabVIEW cannot infer a single size of an array, consider using a


 fixed-size array in your FPGA VI.

#### Creating Fixed-Size Array Controls

Complete the following steps to create a fixed-size array control:

1. Add an array to the front panel window. An array includes an index display


 on the left, an element display on the right, and an optional label.
2. If the Controls palette is not already visible,


 right-click the element display or the front panel window to display the


 Controls palette.
3. Drag a control or indicator into the array. For example, drag a numeric control


 into the array.
4. Right-click the index of the array control and select Set


 Size from the shortcut menu.
5. In the Size page of the Properties


 dialog box, select Fixed .
6. Enter the number of elements in the array.
7. Click the OK button.

#### Creating Fixed-Size Array Constants

Complete the following steps to create a fixed-size array constant:

1. Add an array constant to the block diagram. An array


 constant appears with an index display on the left, an empty element display on


 the right, and an optional label.
2. Add a constant to the array.
3. Right-click the index of the array constant and select Set


 Size from the shortcut menu.
4. In the Size page of the Properties


 dialog box, select Fixed .
5. Enter the number of elements in the array.
6. Click the OK button.

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-fpga-clocks-and-timing-fpga-module.html language=enus -->
## TOPIC 00187: Using FPGA Clocks and Timing

- bundle_id: `labview-fpga-module`
- source_path: `using-fpga-clocks-and-timing-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-fpga-clocks-and-timing-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following clocks in an FPGA application: Base clock—A digital signal existing in the target hardware that you can use as a clock for an FPGA application. Derived clock—A clock you create from a base clock that you can use as a clock for an FPGA application. You can scale the frequenc

### Using FPGA Clocks and Timing

You can use the following clocks in an FPGA application:

- Base clock —A digital signal existing in the target


 hardware that you can use as a clock for an FPGA application.
- Derived clock —A clock you create from a base clock that


 you can use as a clock for an FPGA application. You can scale the frequency of


 an FPGA target base, external, or CLIP clock by using a derived clock.
- Top-level clock —The global clock that the FPGA VI uses


 outside a single-cycle Timed Loop.

LabVIEW uses the base clock properties when setting timing constraints on circuits


 generated from the FPGA VI during compilation.

Every VI or function you place in an FPGA VI takes a certain amount of time, known as


 logic delay, to execute. The top-level clock on an FPGA target determines the


 execution time of the individual functions and VIs on the FPGA VI block diagram. If


 you change the frequency of the top-level clock, you also change the execution speed


 of functions on the block diagram and the execution rate of the FPGA VI.

By controlling the execution rate of the FPGA VI, you specify the timing objectives


 of an FPGA application. Operations occur at the rate determined by the dataflow of


 the VI if you do not include additional programming. To control or measure the


 execution timing, use the Timing VIs. You also can use the Timing VIs to create


 custom I/O applications, such as counters and triggers.

Parent topic:

Creating FPGA VIs

Related concepts:

- Adding an FPGA Base Clock to a LabVIEW Project
- Adding Items to an FPGA Target in the Project Explorer Window
- Configuring FPGA Base Clocks
- Creating FPGA-Derived Clocks
- Selecting an FPGA Clock as the Timing Source for SCTLs
- Using CLIP Clocks

<!--NI_TOPIC bundle=labview-fpga-module path=using-fpga-io-fpga-module.html language=enus -->
## TOPIC 00188: Using FPGA I/O

- bundle_id: `labview-fpga-module`
- source_path: `using-fpga-io-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-fpga-io-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Inputs and outputs (I/O) on FPGA targets allow you to connect the FPGA target to other devices. FPGA I/O resources are fixed elements of the FPGA targets that you use to transfer data among the different parts of the system. On some FPGA targets, FPGA I/O resources correspond to lines on front panel

### Using FPGA I/O

Inputs and outputs (I/O) on FPGA targets allow you to connect the FPGA target to



 other devices. FPGA I/O resources are fixed elements of the FPGA targets that you



 use to transfer data among the different parts of the system. On some FPGA targets,



 FPGA I/O resources correspond to lines on front panel connectors, PXI backplanes, or



 RTSI connectors. On other FPGA targets, FPGA I/O resources are nodes inside FPGAs



 that connect the part of the FPGA designed by NI with the part of the FPGA you



 design through FPGA VIs. For component-level IP (CLIP), I/O resources are nodes inside FPGAs that



 connect CLIP with the FPGA VI. Each FPGA I/O resource has a specific type, such as



 digital or analog. An FPGA target might have multiple I/O



 resources of the same or different types. You can create FPGA



 I/O items, determine the I/O resources on the FPGA target that you want to use, and



 then assign unique names to the I/O resources you use.

Note

Resources translate physical quantities to or from a digital value that you



 manipulate in FPGA Module software. An I/O resource has one or more terminals for



 receiving or generating a physical quantity. Many I/O resources on FPGA targets have



 physical terminals to which you can directly connect elements of the system.

When the FPGA VI runs on the FPGA target, it performs I/O operations in hardware. For



 example, if you configure an FPGA I/O Node to



 read a digital line, the FPGA I/O Node reads the line and returns the result to the



 FPGA VI. Because FPGA VIs run on the FPGA, the VI can react to the input with the



 speed and determinism available in the FPGA target hardware.

You can put analog and digital inputs and outputs together in the same node on the



 block diagram. You can use target-specific properties and methods on the FPGA I/O



 items with the FPGA I/O Property Node and the FPGA I/O Method



 Node, respectively.

#### Digital I/O

FPGA targets might organize digital I/O resources as individual lines or as groups of



 lines called ports. Some FPGA targets provide access to digital I/O resources



 exclusively as lines or ports. Other FPGA targets allow you to access the same



 physical lines both as individual lines and as ports. There are three types of



 digital I/O resources: those that read input, those that write output, and those



 that can perform both functions. Refer to the FPGA target hardware



 documentation for information about digital I/O support.

#### Digital Input Resources

You can read digital input FPGA resources with the FPGA I/O Node. Use digital input



 resources to monitor circuitry outside the FPGA target.

#### Digital Output Resources

You can write digital output FPGA resources with the FPGA I/O Node. Use digital



 output resources to control circuitry outside the FPGA target.

#### Digital Input and Output Resources

Some FPGA targets contain bidirectional, or tristate, digital I/O resources. In



 LabVIEW FPGA, tristate digital I/O resources are called digital input and output



 resources. You can read and write digital input and output resources with the FPGA



 I/O Node. You can use digital input and output resources to monitor and control



 circuitry outside the FPGA target. Tristate resources allow you to configure the I/O



 resource and control the direction of dataflow. Use the FPGA I/O Method



 Node configured with the Set Output Enable method to change the direction



 of dataflow. Wire a TRUE value to the Enable input to



 configure the tristate I/O resource as an output resource. Wire a FALSE value to the



 Enable input to configure the tristate I/O resource as an



 input resource.

Note

As shown in the following illustration, an Output Enable signal controls whether the



 line is configured for input or output.

[IMAGE alt='image' src='GUID-A87D5561-791D-4FEA-A637-4894F03B328F-a5.png']

The tristate resource acts like a switch that the Output Enable signal controls, as



 shown in the following illustration.

[IMAGE alt='image' src='GUID-C779C389-BD1C-48C7-B3FF-74E462572DE7-a5.png']

When the Output Enable signal is TRUE or equal to 1, the digital line is configured



 as an output, and the value stored in Output Data will be driven on the digital



 line. When the Output Enable signal is FALSE or equal to 0, the digital line is



 configured as a high-impedance input allowing the line to be driven by an external



 device, as shown in the following illustration.

[IMAGE alt='image' src='GUID-EE3BEF1D-3F04-4824-A87B-EBF86E47D6D8-a5.png']

Regardless of the state of the Output Enable signal, you can use Input Data to



 monitor the current state of the digital line.

If you use an FPGA I/O Node to read a digital input and output resource, the FPGA I/O



 Node does not change the direction of the resource. If you use a digital input and



 output resource to write output, you must disable the output before you can use the



 same resource to read input. As shown in the following illustration, the FPGA I/O



 Method Node with the Set Output Enable method disables the output line before the



 FPGA I/O Node configured with a digital input and output resource reads the state of



 an external signal. Otherwise, the FPGA I/O Node simply reads back the last value



 written by the FPGA VI.

[IMAGE alt='image' src='GUID-C9F12029-C8B9-439B-AB88-0214BC8A1865-a5.png']

If you use the FPGA I/O Node to write a digital input and output resource, the FPGA



 I/O Node both writes the data and enables the terminal for output. You also can use



 the FPGA I/O Method Node with the Set Output Data method to write data without



 enabling the output. Use the FPGA I/O Method Node with the Set Output Enable method



 to enable the digital terminal, which allows the data to be driven out. Use the Set



 Output Data method before the Set Output Enable method to specify the state of the



 digital input and output resource when you enable the output. For example, you might



 have one portion of the block diagram continuously generating an internal signal.



 Use the FPGA I/O Method Node with the Set Output Enable method in another portion of



 the block diagram to independently control when the internal signal is actually



 driven out to an external device.

If you include a digital I/O resource in a single-cycle Timed Loop, each



 synchronization register introduces a delay corresponding to one iteration of the



 single-cycle Timed Loop. In some cases, delays outside the FPGA may be significant



 for the system. If accurate modeling of the delays between the LabVIEW diagram and



 the FPGA is important for testing the logic of the application by executing the FPGA VI on a development computer, delay



 simulation data for the I/O by the number of calls to the I/O node, equivalent to



 the number of synchronization registers.

#### Analog I/O

#### Analog Input

If the FPGA target you use includes analog input resources, you can configure an FPGA



 I/O Node to read an analog input value. If you configure the FPGA I/O Node to read



 an analog input, the FPGA I/O Node might initiate a conversion, wait for the result,



 then return the binary representation of the voltage as a signed integer or



 fixed-point number. The analog input process and the resulting data type varies by



 FPGA target. For many FPGA targets, you create the FPGA VI to use the data returned



 by the analog input FPGA I/O Node for operations within the FPGA VI. You also can



 pass the data back to the host VI and, if applicable, convert the data to a voltage



 or other physical quantity if you have a transducer attached to the FPGA target



 analog input.

The equation you use to convert the binary representation to a physical quantity



 depends on the FPGA target and transducer. For example, with an NI PXI-7831R device,



 use the following equation to convert the binary representation to voltage: Input



 Voltage = (Binary Code / 32768) x 10.0V. Refer to the specific FPGA target hardware documentation for more information.

#### Analog Output

If the FPGA target you use includes analog output resources, you can configure an



 FPGA I/O Node to write an analog output value. If you configure the FPGA I/O Node to



 write an analog output, the FPGA I/O Node writes the binary representation of the



 voltage to the digital-to-analog converter (DAC), which sets the analog output



 voltage. The data type varies by FPGA target. You can generate voltage information



 from two sources—the host VI or the FPGA VI. Typically the host VI converts the



 voltage to an appropriate binary representation before writing the value to the FPGA



 VI. If the FPGA VI determines the voltage, typically the FPGA VI performs the



 calculations using the appropriate binary representations. In both cases, the DAC



 produces a voltage that corresponds to the binary representation.

The equation you use to convert a voltage to a binary representation depends on the



 specific FPGA target. For example, with an NI PXI-7831R device, use the following



 equation to convert the voltage to the binary representation: Binary Code = (Output



 Voltage x 32768) / 10.0V. Refer to the specific FPGA target hardware



 documentation for more information.

Parent topic:

Creating FPGA VIs

Related concepts:

- Managing Shared Resources
- Using Parallel Operations

<!--NI_TOPIC bundle=labview-fpga-module path=using-io-clocks-register-items-memory-items-fifos-and-handshake-items-in-subvis-fpga-module.html language=enus -->
## TOPIC 00189: Using I/O, Clocks, Register Items, Memory Items, FIFOs, and Handshake Items in SubVIs

- bundle_id: `labview-fpga-module`
- source_path: `using-io-clocks-register-items-memory-items-fifos-and-handshake-items-in-subvis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-io-clocks-register-items-memory-items-fifos-and-handshake-items-in-subvis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use name controls to create subVIs that can be reused with different I/O, clock, register, memory, FIFO, or handshake resources. You can use name controls only in reentrant FPGA subVIs. FPGA name controls are located on the Name Controls palette. The FPGA Module also includes block diagram constants

### Using I/O, Clocks, Register Items, Memory Items, FIFOs, and Handshake Items in SubVIs

Use name controls to create subVIs that can be reused with different I/O, clock,


 register, memory, FIFO, or handshake resources. You can use name controls only in


 reentrant FPGA subVIs.

Note

Name


 Controls

Complete the following steps to enable a subVI to accept an FPGA I/O, clock,


 register, memory, or FIFO resource.

1. Place an FPGA I/O Node, Register Method Node, Memory Method Node, FIFO Method


 Node, or Handshake Method Node on the block diagram of your subVI. To select an


 FPGA clock, place a single-cycle Timed Loop on the block diagram of your


 subVI.
2. Right-click the FPGA I/O In , Register


 In , Memory In , FIFO


 In , Handshake In , or Source


 Name input terminal and select


 Create»Control .
3. Assign the I/O, register, memory, FIFO, handshake, or clock control to a


 connector pane terminal of the subVI.

#### Passing I/O, Clocks, Register Items, Memory Items, FIFOs, or Handshake Items to a


 SubVI

The following block diagram shows MemoryControl.vi with the memory control,


 Memory In, wired to a Memory Method Node.

[IMAGE alt='image' src='GUID-BAE430D7-D006-424B-BCC1-2F41E8C3E380-a5.png']

The following block diagram shows MemoryControl.vi as the referenced subVI. Notice


 that the VI-Defined Memory Configuration node specifies the memory item to use in


 the calling VI below. This design means that if you want to execute MemoryControl.vi


 with a different memory item, you only have to change the item to which


 Memory In refers using the VI-Defined Memory


 Configuration node.

[IMAGE alt='image' src='GUID-DA0C7BAB-C86E-494F-A778-EF639D8284D2-a5.png']

#### Restrictions on FPGA Name Controls

The following restrictions apply to FPGA I/O, cRIO I/O, memory, FIFO, handshake, and


 clock controls:

- You can change the value of FPGA name controls only when programming the FPGA


 VI. You cannot change the values while an FPGA VI runs on a development computer


 or when using interactive front panel communication.
- FPGA name controls are available only when programming VIs under an FPGA target.


 FPGA name controls are not available when programming host VIs.
- You can bundle FPGA name controls into clusters with other FPGA name controls,


 with occurrence refnums, and with other data types. However, you cannot have


 such a cluster on the front panel of the top-level FPGA VI. LabVIEW returns an


 error when you attempt to compile the FPGA VI.

Parent topic:

Using SubVIs in FPGA Applications

Related concepts:

- FPGA Memory Items
- Storing and Accessing Data From Different Parts of an FPGA Design

<!--NI_TOPIC bundle=labview-fpga-module path=using-labview-classes-when-creating-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00190: Using LabVIEW Classes When Creating FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-labview-classes-when-creating-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-labview-classes-when-creating-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use certain aspects of LabVIEW object-oriented programming techniques when creating FPGA VIs. Supported LabVIEW Class Features Class constants, controls, and indicators Class methods Use of all FPGA supported data types within classes Classes contained in the private data of other classes Yo

### Using LabVIEW Classes When Creating FPGA VIs

You can use certain aspects of LabVIEW object-oriented


 programming techniques when creating FPGA VIs.

#### Supported LabVIEW Class Features

- Class constants, controls, and indicators
- Class methods
- Use of all FPGA supported data types within classes
- Classes contained in the private data of other classes

Note

#### Guidelines for Inheritance and Compile-Time Resolution of Classes

In LabVIEW object-oriented programming, the type of the object at run time can be the


 same or a descendant of the type of the wire. When you compile an FPGA VI into a


 bitfile, data routing is fixed, meaning that the compiler cannot dynamically call


 multiple implementations of code. This restriction means that the compiler must be


 able to statically determine which type is actually on the wire at run time. Use the


 following type guidelines as you create FPGA VIs:

- You can wire a child class terminal to a parent class terminal.
- Compared to any other subVI call, there is no additional overhead with dynamic


 dispatching in an FPGA VI because the override to invoke is determined at


 compile time.
- If an FPGA VI has a LabVIEW class input and is not reentrant, you can call that


 VI in multiple places in your VI hierarchy and wire it with different wire types


 at various locations. However, when the compiler analyzes your VI hierarchy, the


 wire type must resolve to the same class at all locations. This applies to both


 static dispatch and dynamic dispatch VIs.
- When you have local variables of the class type, ensure that all writes match in


 class type, as described in the following list:
  - If you have a LabVIEW


 class control and associated write locals, ensure that all wires


 connected to the write locals are of the same class type. If the control


 is on the connector pane, you must ensure that the wire connected to the


 terminal, which corresponds to the control, is of the same class type as


 well.
  - If you have a LabVIEW class indicator and associated write


 locals, ensure that all wires connected to the write locals and the


 indicator are of the same class type.
- When you have local variables of a class type and some of them are readers,


 ensure that all writes match the default class type, as described in the


 following list:
  - If you have read locals associated with a control or


 local variables associated with a wired control, you must ensure that


 all wires connected to the write locals, if any, are of the default


 type, unless the control is on the connector pane and you wire the


 terminal corresponding to the control.
  - If you have read locals


 associated with an indicator, you must ensure that all wires connected


 to the indicator and the write locals, if any, are of the default


 type.
- All objects in an array must resolve to the same class.
- Case structure tunnels in all frames must resolve to the same class.
- The compiler resolves the class for shift registers and Feedback Nodes at the


 initialization terminal and then uses that type for the rest of the loop.


 Uninitialized shift registers and Feedback Nodes resolve to the class of the


 wire. If you introduce a child class within the loop, the compile fails. In the


 following figure, the FPGA VI compiles only if DynDisp.vi 


 always returns the same type at its output that appears at its input. [IMAGE alt='image' src='GUID-57CB5630-779E-4717-82AD-A93451817BB8-a5.png']

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-labview-fpga-interface-without-the-fpga-module-fpga-interface.html language=enus -->
## TOPIC 00191: Using LabVIEW FPGA Interface without the FPGA Module

- bundle_id: `labview-fpga-module`
- source_path: `using-labview-fpga-interface-without-the-fpga-module-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-labview-fpga-interface-without-the-fpga-module-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have an FPGA target, you can use the FPGA Interface VIs and functions to interface with an FPGA bitfile even if you do not have the LabVIEW FPGA Module installed. Use the Open FPGA VI Reference function or the Open Dynamic Bitfile Reference function to open a reference to the FPGA bitfile. Yo

### Using LabVIEW FPGA Interface without the FPGA Module

If you have an FPGA target, you can use the FPGA Interface VIs and functions to


 interface with an FPGA bitfile even if you do not have the LabVIEW FPGA Module


 installed. Use the Open FPGA VI Reference function or the Open Dynamic Bitfile


 Reference function to open a reference to the FPGA bitfile. You then can use other


 FPGA Interface functions, such as Read/Write Control, Invoke Method, and Close FPGA


 VI Reference, to interface with the FPGA bitfile.

Note

Parent topic:

FPGA Interface

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=using-multiple-fpga-vi-references-for-the-same-target-fpga-interface.html language=enus -->
## TOPIC 00192: Using Multiple FPGA VI References for the Same Target

- bundle_id: `labview-fpga-module`
- source_path: `using-multiple-fpga-vi-references-for-the-same-target-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-multiple-fpga-vi-references-for-the-same-target-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to open references to different FPGA VIs or bitfiles on one target, open only one reference at a time, and close the reference before opening another. You can have more than one FPGA VI reference simultaneously open on a target, as long as all the references correspond to the same FPGA V

### Using Multiple FPGA VI References for the Same Target

If you want to open references to different FPGA VIs or bitfiles on one target, open


 only one reference at a time, and close the reference before opening another.

You can have more than one FPGA VI reference simultaneously open on a target, as long


 as all the references correspond to the same FPGA VI or bitfile on the same target.


 By opening more than one FPGA VI reference in a host VI, you can structure the host


 VI so that different parts of the host VI communicate with different parts of the


 FPGA VI. For example, the host VI can access controls and indicators, logical


 interrupts, and DMA channels. Therefore, you could partition the host VI to access


 these items using different instances of the Open FPGA


 VI Reference function. The only type of access that you can always make


 safely using multiple FPGA VI references is reading controls and indicators.

Note

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=using-parallel-operations-fpga-module.html language=enus -->
## TOPIC 00193: Using Parallel Operations

- bundle_id: `labview-fpga-module`
- source_path: `using-parallel-operations-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-parallel-operations-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Parallel operations on the FPGA typically increase execution rate and reduce jitter when compared to processor-based targets. Each parallel operation executes on its own dedicated section of FPGA hardware to achieve truly simultaneous execution. As a result, the total execution time of parallel FPGA

### Using Parallel Operations

Parallel operations on the FPGA typically increase execution rate and reduce jitter


 when compared to processor-based targets. Each parallel operation executes on its


 own dedicated section of FPGA hardware to achieve truly simultaneous execution. As a


 result, the total execution time of parallel FPGA operations equals the execution


 time of the slowest operation, whereas the total execution time of the same


 operations on a single processor equals the sum of all the execution times.

To create parallel operations, use multiple independent While Loops on a single block


 diagram. For example, you can implement multiple data acquisition engines, each with


 an independent sampling rate, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-34FB0191-54C8-44B6-81E9-9F66A43B820B-a5.png']

You can use independent sampling rates to efficiently acquire data in systems that


 contain both high frequency and low frequency signals. Configure one data


 acquisition engine with a high sampling rate to measure a high frequency signal.


 Configure the other data acquisition engine with a lower sampling rate to measure a


 low frequency signal.

If you use shared resources among parallel operations, you risk disabling parallel


 execution, as each operation must wait for the shared resource to become available


 before executing. Possible shared resources include digital I/O resources, analog I/O resources, memory


 items, register items, the interrupt line, local and


 global variables, and non-reentrant subVIs.

Tip

Using wires to transfer data between loops introduces a dataflow dependency that


 prevents the loops from running in parallel.

- Memory items
- Register items
- Local or global variables
- FIFOs

Parent topic:

Creating FPGA VIs

Related concepts:

- Optimizing FPGA VIs for Speed and Size
- Managing Shared Resources
- Using FPGA I/O

<!--NI_TOPIC bundle=labview-fpga-module path=using-peer-to-peer-streaming-with-fpga-targets-fpga-module.html language=enus -->
## TOPIC 00194: Using Peer-to-Peer Streaming with FPGA Targets

- bundle_id: `labview-fpga-module`
- source_path: `using-peer-to-peer-streaming-with-fpga-targets-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-peer-to-peer-streaming-with-fpga-targets-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Peer-to-peer streaming allows you to transfer data from an FPGA target directly to another target without sending the data through the host processor. You can use peer-to-peer streaming to send data between FPGA and non-FPGA targets, but the targets must be capable of using the peer-to-peer stream a

### Using Peer-to-Peer Streaming with FPGA Targets

Peer-to-peer streaming allows you to transfer data from


 an FPGA target directly to another target without sending the data through the host


 processor. You can use peer-to-peer streaming to send data between FPGA and non-FPGA


 targets, but the targets must be capable of using the peer-to-peer stream


 architecture. Refer to the specific FPGA target documentation for information about the peer-to-peer streaming


 capabilities of the target.

Complete the following tasks to set up a peer-to-peer streaming session between two


 targets.

1. Create a peer-to-peer writer FIFO
2. Create a peer-to-peer reader FIFO
3. Create a reference to a peer-to-peer writer FIFO
4. Create a reference to a peer-to-peer reader FIFO
5. Create a peer-to-peer streaming session

Parent topic:

Transferring Data between Devices or Structures Using FIFOs

Related concepts:

- Creating a Peer-to-Peer Streaming Session
- Creating a Reference to a Peer-to-Peer Reader FIFO
- Creating a Reference to a Peer-to-Peer Writer FIFO
- Creating Peer-to-Peer Reader FIFOs
- Creating Peer-to-Peer Writer FIFOs
- FPGA Target Hardware Documentation

<!--NI_TOPIC bundle=labview-fpga-module path=using-sampling-probes-fpga-module.html language=enus -->
## TOPIC 00195: Using Sampling Probes

- bundle_id: `labview-fpga-module`
- source_path: `using-sampling-probes-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-sampling-probes-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Sampling probes in host VIs or FPGA VIs to check intermediate values on a wire as a VI runs and to view changes in signal data over time. For example, you can use Sampling probes to debug VIs in a single-cycle Timed Loop or in code that is intended for a single-cycle Timed Loop. With Sampling pr

### Using Sampling Probes

Use Sampling probes in host VIs or FPGA VIs to check intermediate values on a wire as


 a VI runs and to view changes in signal data over time. For example, you can use


 Sampling probes to debug VIs in a single-cycle Timed Loop or in code that is


 intended for a single-cycle Timed Loop. With Sampling probes, you can visualize


 multiple signals on a waveform graph and compare how the value of each signal


 changes cycle by cycle.

Note

To view data from Sampling probes, use the Sampling Probe Watch


 Window. You cannot use the Sampling Probe Watch


 Window to change data. Sampling probes have no effect on the way a


 VI runs.

#### Understanding Sampling Sources

A sampling source determines when LabVIEW reads or samples data from associated


 probes. The sampling source ensures that Sampling probes update at the correct times


 relative to other Sampling probes associated with that source. There is no limit on


 the number of sampling sources you can specify. All probes associated with a given


 sampling source display on the same waveform graph in the Sampling Probe


 Watch Window.

The following table indicates some of the differences between sampling sources in the


 host VI and the FPGA VI:

Note

Note

Sampling Probe Watch Window

#### Specifying a Sampling Source in a Host VI

Complete the following steps to designate a loop as a sampling source on the block


 diagram of a host VI:

1. Add either of the following loops to the block diagram. For LoopWhile Loop
2. Right-click the loop border and select Mark as Probe Sampling Source to
 create the sampling source and display the Sampling Probe Watch
 Window . LabVIEW automatically lists and numbers the sampling
 source in the Sampling Probe Watch Window and displays
 the same number in a glyph in the top left corner of the loop.

#### Specifying a Sampling Source in an FPGA VI

LabVIEW automatically creates the FPGA sampling source using


 FPGA simulated time when you create the first Sampling probe. This sampling source


 is not tied to any individual structure on the block diagram, but you must use it


 within a single-cycle Timed Loop.

#### Creating a Sampling Probe on the Block Diagram

Complete the following steps to add a Sampling probe to the block diagram:

1. Right-click a wire and select Sampling Probe»x , where
 x is the name of the sampling source. LabVIEW automatically lists and numbers the probe in the
 Sampling Probe Watch Window and displays the same
 number in a glyph on the wire you clicked.
  - FPGA VI: The Sampling Probe Watch Window 
 appears.
  - Host VI: The Sampling Probe Watch Window is
 already open.
2. (Optional) Place more probes on other wires and objects in the VI where you


 expect the data to change. Move the Sampling Probe Watch


 Window out of the way if necessary.
3. Run the VI. The waveform graph on the right side of the Sampling


 Probe Watch Window displays data passed along the wire.
4. (Optional) To locate the probed wire in the Sampling Probe Watch


 Window , right-click the wire associated with the probe and


 select Find Probe from the shortcut menu. The view in the


 Sampling Probe Watch Window snaps to the selected


 probe.
5. Compare the data that appears in the Sampling Probe Watch


 Window to what you expect.
6. To remove a sampling probe, select the sampling probe in the Sampling Probe Watch
 Window and click Remove Selected Probe on
 the Sampling Probe Watch Window toolbar. Click
 Remove all to remove the currently displayed sampling
 source and all associated probes. All probes close automatically when you close
 the Sampling Probe Watch Window or the block
 diagram.

Parent topic:

Debugging FPGA VIs Using Simulation Mode

<!--NI_TOPIC bundle=labview-fpga-module path=using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00196: Using Single-Cycle Timed Loops to Optimize FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW automatically optimizes code inside a single-cycle Timed Loop (SCTL) to execute more quickly and consume less space on the FPGA target, compared to the same code inside a While Loop. When you use a While Loop with an FPGA target, the While Loop takes multiple clock cycles to execute each ite

### Using Single-Cycle Timed Loops to Optimize FPGA VIs

LabVIEW automatically optimizes code inside a single-cycle Timed Loop (SCTL) to


 execute more quickly and consume less space on the FPGA target, compared to the same


 code inside a While Loop. When you use a While Loop with an FPGA target, the While


 Loop takes multiple clock cycles to execute each iteration because the While Loop


 includes the enable chain registers. The number of clock cycles that the While Loop


 takes for each iteration is dependent on the code inside the loop. When you use an


 SCTL with an FPGA target, the SCTL executes all functions inside the loop within a


 single clock cycle. Using the SCTL on FPGA targets reduces execution cycles and


 saves resources, mainly because the SCTL does not include the enable chain


 registers. If the SCTL contains initialized shift registers, it takes one clock


 cycle before the first iteration to initialize shift register values. The SCTL is


 similar to a clocked process in HDL.

The following block diagram illustrates the difference between the While Loop and


 SCTL in terms of executing the same code.

[IMAGE alt='image' src='GUID-2078F2B9-4998-4CEA-88A2-A473B1CB1299-a5.png']

The following list describes important details about the previous diagram.

|  | The code within the While Loop takes four clock cycles to execute, excluding the overhead of the While Loop, which takes two additional clock cycles to execute. |
| --- | --- |
|  | The red vertical lines indicate where each clock cycle ends inside the While Loop. |
|  | The same code in a SCTL executes within one clock cycle, if the clock period is long enough for the logic. |

You can also include logic in a SCTL to optimize code by reducing execution cycles in


 an FPGA VI, as demonstrated in the following block diagram.

[IMAGE alt='image' src='GUID-239832F6-BA52-4145-8725-F2B496D4B155-a5.png']

If you use a SCTL within a While Loop, as demonstrated in the previous diagram, wire


 a TRUE constant to the condition terminal so that the code within the Timed Loop


 executes only once per iteration of the While Loop.

Parent topic:

Executing Code in Single-Cycle Timed Loops

Related concepts:

- Executing Code in Single-Cycle Timed Loops
- Optimizing FPGA VIs for Speed and Size
- Understanding Timing Considerations for FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module_2.html language=enus -->
## TOPIC 00197: Using Single-Cycle Timed Loops to Optimize FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-single-cycle-timed-loops-to-optimize-fpga-vis-fpga-module_2.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW automatically optimizes code inside a single-cycle Timed Loop (SCTL) to execute more quickly and consume less space on the FPGA target, compared to the same code inside a While Loop. When you use a While Loop with an FPGA target, the While Loop takes multiple clock cycles to execute each ite

### Using Single-Cycle Timed Loops to Optimize FPGA VIs

LabVIEW automatically optimizes code inside a single-cycle Timed Loop (SCTL) to


 execute more quickly and consume less space on the FPGA target, compared to the same


 code inside a While Loop. When you use a While Loop with an FPGA target, the While


 Loop takes multiple clock cycles to execute each iteration because the While Loop


 includes the enable chain registers. The number of clock cycles that the While Loop


 takes for each iteration is dependent on the code inside the loop. When you use an


 SCTL with an FPGA target, the SCTL executes all functions inside the loop within a


 single clock cycle. Using the SCTL on FPGA targets reduces execution cycles and


 saves resources, mainly because the SCTL does not include the enable chain


 registers. If the SCTL contains initialized shift registers, it takes one clock


 cycle before the first iteration to initialize shift register values. The SCTL is


 similar to a clocked process in HDL.

The following block diagram illustrates the difference between the While Loop and


 SCTL in terms of executing the same code.

[IMAGE alt='image' src='GUID-2078F2B9-4998-4CEA-88A2-A473B1CB1299-a5.png']

The following list describes important details about the previous diagram.

|  | The code within the While Loop takes four clock cycles to execute, excluding the overhead of the While Loop, which takes two additional clock cycles to execute. |
| --- | --- |
|  | The red vertical lines indicate where each clock cycle ends inside the While Loop. |
|  | The same code in a SCTL executes within one clock cycle, if the clock period is long enough for the logic. |

You can also include logic in a SCTL to optimize code by reducing execution cycles in


 an FPGA VI, as demonstrated in the following block diagram.

[IMAGE alt='image' src='GUID-239832F6-BA52-4145-8725-F2B496D4B155-a5.png']

If you use a SCTL within a While Loop, as demonstrated in the previous diagram, wire


 a TRUE constant to the condition terminal so that the code within the Timed Loop


 executes only once per iteration of the While Loop.

Parent topic:

Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=using-subvis-in-fpga-applications-fpga-module.html language=enus -->
## TOPIC 00198: Using SubVIs in FPGA Applications

- bundle_id: `labview-fpga-module`
- source_path: `using-subvis-in-fpga-applications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-subvis-in-fpga-applications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW allows you to group common sections of code for reuse as subVIs on the block diagram. Use subVIs when developing FPGA applications for any of the following reasons: Use multiple FPGA VIs—LabVIEW can run only one top-level FPGA VI, but you can implement multiple FPGA VIs by calling them as su

### Using SubVIs in FPGA Applications

LabVIEW allows you to group common sections of code for reuse as subVIs on the block


 diagram. Use subVIs when developing FPGA applications for any of the following


 reasons:

- Use multiple FPGA VIs —LabVIEW can run only one top-level


 FPGA VI, but you can implement multiple FPGA VIs by calling them as subVIs from


 the top-level FPGA VI.
- Conserve FPGA resources —Front panel objects in subVIs do


 not communicate directly with the host VI and therefore do not consume


 additional FPGA resources.
- Reuse code across multiple projects —Creating reusable,


 modular code helps you efficiently organize, manage, test, and debug your


 application by allowing for easier code review and updates and by avoiding code


 duplication.

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-subvis-in-host-vis-fpga-interface.html language=enus -->
## TOPIC 00199: Using SubVIs in Host VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-subvis-in-host-vis-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-subvis-in-host-vis-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use subVIs in host VIs that communicate with FPGA VIs or bitfiles on FPGA targets. To reference an FPGA VI or bitfile in a subVI, use the Open FPGA VI Reference function. You can configure the Open FPGA VI Reference function to be dynamic, so that these subVIs can work with any FPGA referenc

### Using SubVIs in Host VIs

You can use subVIs in host VIs that communicate with FPGA VIs or bitfiles on FPGA


 targets. To reference an FPGA VI or bitfile in a subVI, use the Open FPGA VI Reference function. You can configure the


 Open FPGA VI Reference function to be


 dynamic, so that these subVIs can work with any FPGA reference that


 implements the specified interface, even if the reference is on different target


 types. For example, you can use the same subVI for both a PCI and a PXI target.

Complete the following steps to create a dynamic FPGA interface reference for subVIs.

1. Right-click the Open FPGA VI Reference function on the


 host VI block diagram and select Configure Open FPGA VI


 Reference from the shortcut menu. The Configure


 Open FPGA VI Reference dialog box appears.
2. Select a build specification, VI, or bitfile in the Open 


 section.
3. Place a checkmark in the Dynamic mode checkbox.
4. Click the OK button to close the Configure


 Open FPGA VI Reference dialog box.

Parent topic:

Communicating with FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-configure-component-level-ip-wizard-fpga-module.html language=enus -->
## TOPIC 00200: Using the Configure Component-Level IP Wizard

- bundle_id: `labview-fpga-module`
- source_path: `using-the-configure-component-level-ip-wizard-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-configure-component-level-ip-wizard-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure Component-Level IP wizard (CLIP wizard) to define the IP interface without editing the declaration XML file by hand. You can use this wizard to create or modify a declaration XML file. The CLIP wizard also can check the syntax of the VHDL you are using in the CLIP. Depending on the

### Using the Configure Component-Level IP
 Wizard

Use the Configure Component-Level IP wizard (CLIP wizard) to define the IP interface without editing the declaration XML file by


 hand. You can use this wizard to create or modify a declaration XML file. The CLIP


 wizard also can check the syntax of the VHDL you are using in the CLIP. Depending on


 the action you want to perform, launch the CLIP wizard from the Component-Level IP page of the FPGA


 Target Properties dialog box in either of the following ways:

- To generate a new CLIP


 interface, click the Create File button.
- To modify an existing CLIP


 interface, select the declaration file and click the


 Modify File button.

Note

ni.com

The CLIP wizard contains the following pages:

1. Name and Source
2. Entity, Architecture, FPGA Family and IP Type
3. Generics
4. Basic Signal Settings
5. Additional Clock Signal Settings
6. Additional Clock Status Signal Settings
7. Additional Data Signal Settings
8. XML Export

#### Configuring a CLIP to Use with Simulation

With the wizard you can specify simulation models for CLIP so that you can export


 FPGA VIs containing CLIP for third-party simulation. If you are going to create simulation exports of


 FPGA VIs containing CLIP, you must define the simulation behavior for the CLIP


 synthesis files in the Name and


 Source page of the wizard.

Parent topic:

Using VHDL Code as Component-Level IP

Related concepts:

- Adding Component-Level IP to a Project
- CLIP Tutorial, Part 1: Creating VHDL Code
- CLIP Tutorial, Part 2: Defining the Interface
- CLIP Tutorial, Part 3: Adding CLIP to a Project
- Creating or Acquiring IP
- Defining the IP Interface
- Understanding the Simulation VHDL Framework
- Debugging FPGA VIs Using a Third-Party Simulator
- Using VHDL Code as Component-Level IP

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-fixed-point-data-type-fpga-module.html language=enus -->
## TOPIC 00201: Using the Fixed-Point Data Type

- bundle_id: `labview-fpga-module`
- source_path: `using-the-fixed-point-data-type-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-fixed-point-data-type-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The fixed-point data type provides some of the flexibility of the floating-point data type, but maintains the size and speed advantages of integer arithmetic. Refer to ni.com for more information about the fixed-point data type and working with this data type. Not all FPGA Module VIs and functions s

### Using the Fixed-Point Data Type

The fixed-point data type provides some of the flexibility



 of the floating-point data type, but maintains the size and speed advantages of



 integer arithmetic. Refer to ni.com for more information about the



 fixed-point data type and working with this data type.

Note

|  | Caution If you wire a fixed-point number to an integer terminal, you might lose fractional bits. |
| --- | --- |

#### Fixed-Point Configuration Effects on FPGA Resources

When using fixed-point numbers in an FPGA VI, it is important to select the proper



 overflow and rounding modes for a particular function. The High Throughput



 Math functions and some Numeric



 functions have configuration dialog boxes you use to select these modes. If overflow



 or rounding can occur, these modes affect the amount of FPGA resources an FPGA VI



 needs. If overflow or rounding cannot occur, the operation does not require



 additional FPGA resources.

In many situations, you can avoid overflow by placing a checkmark in the



 Adapt to source checkbox in the configuration dialog box



 of the function. If you place a checkmark in this checkbox, LabVIEW attempts to



 adjust the width and range of the output data type such that neither overflow nor



 rounding occurs. However, this adjustment is not possible in all situations. For



 example, if a function involves division, rounding always occurs. Also, some



 functions do not have this checkbox.

#### Effects of Overflow Modes

In general, the overflow modes affect FPGA resource usage in the following ways:

- Saturate —Requires FPGA resources to determine whether the



 input value is within the range of the output type and to choose whether to



 return the original or saturated value.
- Wrap —Requires fewer FPGA resources than the



 Saturate mode.

#### Effects of Rounding Modes

In general, the rounding modes affect FPGA resource usage in the following ways:

- Truncate —Removes bits and therefore does not require any



 FPGA resources. However, this mode produces the largest mean error for most data



 streams. This mode is the default for integer operations.
- Round-Half-Up (Asymmetric) —Adds to the least significant



 bit of the output data type. This option requires an adder that is the width of



 the output data type.
- Round-Half-Even —Requires the most FPGA resources and



 results in the longest combinatorial path of the three rounding modes. However, this mode



 returns the most statistically correct results for most data streams and is



 therefore the default rounding mode for the fixed-point data type.

Note

x

s

t

s

x

t

x

s

x

x

x

t

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-fpga-io-node-fpga-module.html language=enus -->
## TOPIC 00202: Using the FPGA I/O Node

- bundle_id: `labview-fpga-module`
- source_path: `using-the-fpga-io-node-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-fpga-io-node-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you create FPGA I/O items in the Project Explorer window, you can use the FPGA I/O items in FPGA I/O Nodes on the block diagram. You can click an FPGA I/O item in the Project Explorer window and drag it onto the block diagram to create a new FPGA I/O Node that is configured for that FPGA I/O i

### Using the FPGA I/O Node

After you create FPGA I/O items in the Project


 Explorer window, you can use the FPGA I/O items in FPGA


 I/O Nodes on the block diagram. You can click an FPGA I/O item in the


 Project Explorer window and drag it onto the block


 diagram to create a new FPGA I/O Node that is configured for that FPGA I/O item. You


 also can complete the following steps to add an FPGA I/O Node to the block diagram


 and configure terminals for specific FPGA I/O items.

1. Create a new VI or open an existing VI under an FPGA target that


 also contains FPGA I/O items.
2. Add an FPGA I/O Node to the block diagram.
3. Click the element section of the FPGA I/O Node to add a new FPGA I/O item or


 select an FPGA I/O item you previously added to the project. You can select any


 FPGA I/O item you want to use, regardless of the type of I/O resource. The new


 FPGA I/O item appears in the FPGA I/O Node. Alternatively, you can write


 reusable code by wiring an FPGA


 I/O control to the FPGA I/O In input of the


 FPGA I/O Node.

You can expand the FPGA I/O Node to add additional FPGA I/O items. Right-click an


 FPGA I/O item in the FPGA I/O Node and select Add Element


 from the shortcut menu. A new I/O Item terminal appears in


 the FPGA I/O Node. You then can repeat step 3 above to configure the new


 I/O Item terminal.

Tip

Project Explorer

Project


 Explorer

Project Explorer

Parent topic:

Using FPGA I/O

Related concepts:

- Creating FPGA I/O Items
- Adding Items to an FPGA Target in the Project Explorer Window

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-high-throughput-math-functions-fpga-module.html language=enus -->
## TOPIC 00203: Using the High Throughput Math Functions

- bundle_id: `labview-fpga-module`
- source_path: `using-the-high-throughput-math-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-high-throughput-math-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the High Throughput Math functions to perform high throughput math and analysis with fixed-point numbers on FPGA targets. These functions are similar to the Numeric functions but support higher throughput rates, handshaking terminals inside a single-cycle Timed Loop, input/output registers, and

### Using the High Throughput Math Functions

Use the High Throughput Math functions to perform high



 throughput math and analysis with fixed-point numbers on FPGA targets. These



 functions are similar to the Numeric



 functions but support higher throughput rates, handshaking terminals inside a



 single-cycle Timed Loop, input/output registers, and automatic pipelining.

#### Differences between the High Throughput Math Functions and the Numeric



 Functions

The High Throughput Math functions are different from the LabVIEW Numeric functions



 in the following ways:

- Additional functions —The High Throughput Math functions



 include trigonometric, logarithmic, and rectangular/polar coordinate conversion



 functions that support the fixed-point data type.
- Limited data type support— The High Throughput Math and



 Basic Elements functions support fewer data types than the Numeric functions do.



 Refer to the individual High Throughput



 Math or Basic



 Elements topics for supported data types.
- Universal single-cycle Timed Loop support —You cannot



 place some Numeric functions inside a single-cycle Timed



 Loop. However, you can place all High Throughput Math functions



 inside a single-cycle Timed Loop regardless of how many cycles that function



 takes to execute. Inside a single-cycle Timed Loop, these functions might



 display handshaking terminals. You use these terminals to ensure algorithms



 operate with only valid data. The High Throughput Math functions also feature



 ways to control the length of the combinatorial path to improve the clock



 rate at which the functions can compile.
- Higher throughput support —If you need to pipeline Numeric functions inside a single-cycle



 Timed Loop, you must pipeline these functions manually. However, most High



 Throughput Math functions have a Throughput control.



 LabVIEW pipelines the function automatically to achieve the throughput rate you



 specify.
- Labeled terminals —You can configure the High Throughput



 Math functions to display the encoding, word length, and integer word length of numeric



 terminals. You also can use the Context



 Help window to see configuration information about a function or



 wire.

NI recommends that you use the LabVIEW Numeric functions unless you need the benefits



 that the High Throughput Math functions provide. The Numeric functions are easier to



 use when creating a VI and can execute on more platforms than the High Throughput



 Math functions can. For example, the High Throughput Math functions do not support



 NI real-time targets.

#### Configuring a Function

To configure a High Throughput Math function, either double-click the function or



 right-click the function and select Configure from the



 shortcut menu. LabVIEW displays a configuration dialog box for the function. You use



 this dialog box to configure many aspects of the function that affect how it



 executes and the results it returns. By using the configuration dialog box to set



 the encodings, word lengths, and integer word lengths of



 input terminals, you can avoid problems with unsupported fixed-point configurations.

#### Configuring Function Appearance

You can display each High Throughput Math function in either expanded or contracted



 form. The expanded view displays the encoding, word length, and integer word length



 of each terminal. The contracted view saves space on the block diagram. To configure



 the appearance of a function, right-click that function and select



 Expanded View or Contracted



 View.

Parent topic:

Creating FPGA VIs

Related concepts:

- Placing the High Throughput Math Functions in a Single-Cycle Timed Loop
- Using the High Throughput Math Functions
- Configuring Input and Output Terminals of the High Throughput Math Functions

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-integer-data-type-fpga-module.html language=enus -->
## TOPIC 00204: Using the Integer Data Type

- bundle_id: `labview-fpga-module`
- source_path: `using-the-integer-data-type-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-integer-data-type-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can perform integer math on the FPGA by using the Numeric functions. When you perform integer math, the results can overflow. Integer overflow occurs when the result of a mathematical operation exceeds the range of the output data type. For example, the range of a U8 integer is 0 to 255. Adding

### Using the Integer Data Type

You can perform integer math on the FPGA by using the Numeric


 functions.

When you perform integer math, the results can overflow. Integer overflow occurs when


 the result of a mathematical operation exceeds the range of the output data type.


 For example, the range of a U8 integer is 0 to 255. Adding two U8 integers together


 that have a result greater than 255 results in overflow, such as 200 + 70. When


 overflow occurs, the result rolls over, or wraps, at the limit of the range and the


 result modulo 256 is returned. For example, a result of 270 for a U8 integer wraps


 at 256 and returns 14.

You can take advantage of the rollover behavior that occurs with overflow in some


 applications. For example, the execution time measurement example relies on the rollover behavior of


 overflow for proper operation. The example configures the Tick Count


 Express VIs with an 8-bit Size of Internal Counter and


 milliseconds for Counter Units. When the internal counter of


 the Tick Count Express VI reaches 255 ms, it rolls over to 0. If the first Tick


 Count Express VI returns a Tick Count of 132 ms and the


 execution time of the LabVIEW code to be measured takes 140 ms, the internal counter


 has rolled over and the second Tick Count Express VI returns a Tick


 Count value of 16 ms. When the block diagram subtracts 132 from 16,


 overflow occurs and results in the value of 140.

Note

Counter Units

Ticks

mSec

Use the following techniques to avoid integer overflow:

- Evaluate your usage of numeric


 data types.
- Use a larger output data type. If you use a larger output data type, you take up


 more space on the FPGA target but you can program the FPGA VI more quickly and


 easily and receive more accurate data.
- Use the Scale By Power Of 2 function to reduce the magnitude


 of integer of fixed-point inputs. If you use the Scale By Power Of 2 function


 with a constant n input, you do not use any FPGA


 resources for the scaling. However, you lose precision and you also must program


 the FPGA VI to be sure you scale all inputs and outputs correctly.
- Convert integers to the single-precision floating-point data type using the To Single Precision Float function.

Parent topic:

Creating FPGA VIs

Related concepts:

- Manage Execution Rates with FPGA Timing Functions

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-ip-integration-node-fpga-module.html language=enus -->
## TOPIC 00205: Using the IP Integration Node

- bundle_id: `labview-fpga-module`
- source_path: `using-the-ip-integration-node-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-ip-integration-node-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the IP Integration Node to integrate third-party IP into the block diagram of an FPGA VI. Using this node involves the following tasks. Install the necessary Xilinx compilation tools on the computer you plan to use to configure the IP Integration Node. Create or acquire IP synthesis files, such

### Using the IP Integration Node

Use the IP Integration Node to integrate third-party IP into the block diagram


 of an FPGA VI. Using this node involves the following tasks.

1. Install the necessary Xilinx compilation


 tools on the computer you plan to use to configure the IP Integration


 Node.
2. Create or acquire IP


 synthesis files, such as .vhd files, Xilinx IP


 configuration files, or netlist files. Ensure the IP meets the requirements of the node.
3. If you plan to export the IP for simulation, create or acquire the files that


 define a simulation model.
4. Add the IP Integration Node to the block diagram.
5. Double-click the node to configure it. LabVIEW displays a configuration wizard


 you use to complete the following tasks.
  1. Define the name of the IP and


 the synthesis files that compose the IP, including the top-level


 synthesis file.
  2. Set the simulation behavior of each synthesis


 file. The combined behavior results in a simulation model for the


 node.
  3. If the top-level synthesis file is a .vhd 


 file, define the top-level entity and architecture.
  4. Specify the


 FPGA families on which the IP can run.
  5. If the top-level


 synthesis file is a .vhd file, set the value of any


 generics and ensure their syntax is valid.
  6. Generate the


 simulation model.
  7. Specify any IP ports that correspond to clock


 enable signals.
  8. Specify any IP ports that correspond to


 synchronous or asynchronous reset signals.
  9. Specify when and how


 the IP resets.
  10. Define the block diagram terminals that appear


 and set the data types of these terminals.

After you complete these steps, LabVIEW generates the code to integrate the IP into


 the FPGA VI.

#### IP Integration Node Properties Wizard

Use the IP Integration Node Properties wizard to configure the IP Integration Node.

The IP Integration Node Properties wizard contains the following pages:

1. Name and Source
2. Entity, Architecture, and Targets
3. Generics and Support File Generation
4. Clock and Enable Signals
5. Reset Signals and Behavior
6. IP Terminals

Parent topic:

Integrating Third-Party IP

Related concepts:

- Integrating Third-Party IP

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-linear-algebra-functions-fpga-module.html language=enus -->
## TOPIC 00206: Using the Linear Algebra Functions

- bundle_id: `labview-fpga-module`
- source_path: `using-the-linear-algebra-functions-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-linear-algebra-functions-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Linear Algebra functions to perform vector and matrix calculations in high speed and high throughput FPGA applications, such as RF applications. You can configure the Linear Algebra functions to fit different throughput rates, matrix or vector sizes, and data types to meet timing and resourc

### Using the Linear Algebra Functions

Use the Linear Algebra functions to perform vector and matrix calculations in high



 speed and high throughput FPGA applications, such as RF applications. You can



 configure the Linear Algebra functions to fit different throughput rates, matrix or



 vector sizes, and data types to meet timing and resource requirements.

#### Linear Algebra Behaviors

Consider the following behaviors when developing FPGA applications with the Linear



 Algebra functions:

- Target support —All FPGA targets support the Linear



 Algebra functions.
- Single-cycle Timed Loop support —LabVIEW supports the



 Linear Algebra functions only inside the single-cycle Timed Loop.
- Four-wire handshaking protocol support —The Linear Algebra



 functions support handshaking signals.
- Simulation support —The Linear Algebra functions support



 both desktop and full diagram simulation. However, they do not guarantee



 cycle-accurate behavior for desktop simulation when output



 valid is FALSE, as the function has not computed a result that



 downstream nodes can use. When output valid is FALSE, the



 function may return different results on an FPGA target than on a host computer.



 Data returned during the deassertion of output valid 



 might be invalid and should be discarded.
- Limited data type support —The Linear Algebra functions



 support only scalar and vector values of the fixed-point data type. Each



 function includes separate connector pane terminals for real and imaginary



 numbers.
- Labeled input and output terminals —You can view encoding,



 word length, and integer word length of numeric terminals for each function in



 the Context Help window.

#### Configuring the Linear Algebra Functions

To configure a Linear Algebra function, either double-click the function or



 right-click the function and select Configure. LabVIEW



 displays a configuration dialog box for the function. Use this dialog box to



 configure how the function executes and the results the function returns. To avoid



 unsupported fixed-point configurations that result in broken wires, such as



 unsupported word lengths or integer word lengths, use the configuration dialog box



 to set the encodings, word lengths, and integer word lengths of input terminals.

#### Configuring Function Appearance

You can display each Linear Algebra function in either expanded or contracted form.



 The expanded view displays the encoding, word length, and integer word length of



 each terminal. The contracted view saves space on the block diagram. To configure



 the appearance of a function, right-click that function and select



 Expanded View or Contracted



 View.

#### Caveats and Restrictions for Input and Output Terminals

The following list describes input and output terminal behavior of the Linear Algebra



 functions:

- The Linear Algebra functions support only scalar and vector inputs of the



 fixed-point data type. Each function includes separate terminals for real and



 imaginary numbers.
- The input terminals of the Linear Algebra Dot Product, Linear Algebra Matrix



 Transpose, and Linear Algebra Norm Square functions adapt to the data types as



 well as the input pattern you wire to the function. The input terminals of the



 Linear Algebra Matrix Multiply function adapt to the data types but not the



 input pattern wired to the function. Configure the input pattern of the Linear



 Algebra Matrix Multiply function using the Configure Linear Matrix



 Multiply dialog box.
- The real and imaginary inputs of a Linear Algebra function must be of the same



 data type and input pattern, otherwise the data type or array size of the real



 data portion of the input terminal takes precedent.

#### Unsupported Configurations of Input Terminals

If you wire an unsupported fixed-point configuration to a terminal, LabVIEW breaks



 the wire and you cannot run the function. LabVIEW also might coerce the data type to



 a supported configuration. You can run the function, but this coercion might cause



 the function to behave unexpectedly. If the wire is not broken and does not have a



 coercion dot, the input terminal supports this fixed-point configuration.

#### Avoiding Unsupported Input Configurations

You can avoid broken wires or coerced data types on input terminals by using the



 configuration dialog box to specify the fixed-point configuration for a particular



 input terminal. Complete the following steps to configure a terminal in this



 way:

1. Add the function to the block diagram.
2. Double-click the function to launch the configuration dialog box.
3. Configure the encoding, word length, and integer word length of the input



 terminal(s) using the input section of the configuration dialog box. Depending



 on the function, LabVIEW dims certain options and restricts the values you can



 enter in other text boxes.
4. Click the OK button.

Right-click the input terminal and select Create»Control or



 Create»Constant to create an input with a fixed-point



 configuration that the function supports.

#### Overflow and Rounding of Output Terminals

The theoretical computed value is the mathematic result regardless of the valid



 range of your output data type. For the Linear Algebra functions that include an



 Overflow mode configuration, overflow occurs if the range



 of an output terminal is not large enough to hold the theoretical computed value. In



 this situation, the function either wraps or saturates, as specified in the



 Overflow mode pull-down in the configuration dialog



 box.

In many situations, you can avoid overflow by placing a checkmark in the



 Adapt to source checkbox in the configuration dialog box



 of the function. If you enable this option, LabVIEW attempts to adjust the width and



 range of the output data type such that neither overflow nor rounding occurs.



 However, this adjustment is not possible in all situations. LabVIEW supports a



 maximum word length of 64 bits and a maximum integer word length of 1023 bits. If



 you place a checkmark in this checkbox and the output data type requires a word



 length that exceeds these maximum values, overflow and/or rounding errors might



 occur.

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-single-precision-floating-point-data-type.html language=enus -->
## TOPIC 00207: Using the Single-Precision Floating-Point Data Type

- bundle_id: `labview-fpga-module`
- source_path: `using-the-single-precision-floating-point-data-type.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-single-precision-floating-point-data-type.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The single-precision floating-point (SGL) data type provides more accuracy than a 24-bit fixed-point data type but reduces overall performance due to the increased latency of functions and the large number of FPGA resources that it uses. Evaluate your usage of numeric data types to determine which d

### Using the Single-Precision Floating-Point Data Type

The single-precision floating-point (SGL) data type provides more accuracy than a


 24-bit fixed-point data type but reduces overall performance due to the increased


 latency of functions and the large number of FPGA resources that it uses. Evaluate


 your usage of numeric data types to determine which data type best suits your


 design.

The following list describes behavior to consider when developing FPGA applications


 with the single-precision floating-point data type:

- The FPGA Module does not support the double-precision or extended-precision


 floating-point data types.
- All FPGA targets support the SGL data type.
- Only certain functions support the SGL data type.
- The High Throughput Math functions do not support the SGL data type.
- Most functions cannot perform single-precision floating-point operations inside


 the single-cycle Timed Loop because these functions require more than one clock


 cycle to execute but do not have handshaking signals.
- Data type coercions in FPGA VIs can consume a significant amount of FPGA


 resources, especially when a terminal is coerced to the SGL data type.
- The FPGA Module does not support coercion to the SGL data type in the


 single-cycle Timed Loop.
- In the FPGA Module, the SGL data type is compliant with IEEE Std 754-2008, with


 the exception that it does not support subnormal numbers. For example, if you


 use the Equal? function to compare bit accuracy between the host and target, the


 function returns a FALSE result when the operation encounters a very small


 number. Such errors also may propagate in a feedback loop and reduce data


 precision.
- The bit pattern of NaN outputs on the FPGA may differ from


 NaN outputs on the development computer.
- The results of single-precision floating-point calculations performed on the


 FPGA may differ from the results of single-precision floating-point calculations


 performed in simulation.

#### Single-Precision Floating-Point Operations inside the Single-Cycle Timed


 Loop

Most functions cannot perform single-precision floating-point operations inside the


 single-cycle Timed Loop because these functions require more than one clock cycle to


 execute but do not have handshaking signals. The following features are supported


 inside the single-cycle Timed Loop with single-precision floating-point data:

- IP Integration Node
- Xilinx IP
- Memory items
- FIFOs
- Registers
- Local and global variables
- Not A Number/Path/Refnum? Function
- Select Function

Refer to the FPGA VI below for an example of how to pass single-precision


 floating-point data to a single-cycle Timed Loop using FIFOs.

[IMAGE alt='image' src='GUID-B52D9CDD-2F8C-428A-8EBD-24BF2B1F6414-a5.png']

The top loop shows data passing through the Square and Add functions outside the


 single-cycle Timed Loop. The intermediate result is then passed into the


 single-cycle Timed Loop through a FIFO Method Node to calculate the square root of


 the data. Finally a DMA FIFO passes the result back to the host computer.

#### Designing FPGA Applications with the Single-Precision Floating-Point Data


 Type

Consider the following uses when designing FPGA applications using single-precision


 floating-point operations.

#### Free the Host Processor to Perform Other Operations and Use Single-Precision


 Floating-Point Conversions with I/O

Performing I/O conversion to the FPGA frees processing on the host computer,


 especially in real-time systems. If you have FPGA resources available, perform


 fixed-point I/O to single-precision floating-point data conversions on the FPGA to


 free the host processor to perform other operations, such as meeting real-time


 requirements.

#### Operate on Data from Multiple Inputs or Outputs

Convert heterogeneous data paths into the SGL data type in order to handle them with


 common code. This conversion is useful in situations where you want to operate on


 data from multiple inputs that return different fixed-point data types.

The following FPGA VI shows an NI cRIO-9104 as it acquires data from two modules,


 converts to the SGL data type, and writes the data to a DMA FIFO.

[IMAGE alt='image' src='GUID-C7176402-BC91-4FCA-AB80-79099E247323-a5.png']

Parent topic:

Creating FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=using-the-smallest-data-type-to-optimize-fpga-vis-fpga-module.html language=enus -->
## TOPIC 00208: Using the Smallest Data Type to Optimize FPGA VIs

- bundle_id: `labview-fpga-module`
- source_path: `using-the-smallest-data-type-to-optimize-fpga-vis-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-the-smallest-data-type-to-optimize-fpga-vis-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the smallest data type possible for non-constant values to decrease the size and increase the speed of an FPGA VI. Consider the following guidelines when creating an FPGA VI. Numeric functions—Numeric functions coerce all inputs to a largest data type. For example, if you wire a 16-bit and a 32-

### Using the Smallest Data Type to Optimize FPGA VIs

Use the smallest data type possible for non-constant values to decrease the size and


 increase the speed of an FPGA VI. Consider the following guidelines when creating an


 FPGA VI.

- Numeric functions—Numeric functions coerce all


 inputs to a largest data type. For example, if you wire a 16-bit and a 32-bit


 integer to the inputs of the Multiply function,


 the function coerces the 16-bit integer into a 32-bit integer. If you want to


 avoid coercion to a larger data type, use the To


 Fixed-Point function to convert the integer inputs into equivalent


 fixed-point data types and configure the Multiply function output for the desired fixed-point


 representation.
- Loop Timer, Tick Count,


 and Wait VIs—You can use the smallest Size of Internal


 Counter possible for the FPGA VI.
- While Loop—You can convert the 32-bit iteration terminal output to


 the smallest data type that still supports the maximum number of iterations the


 loop executes. You also can avoid using the iteration terminal by using shift registers instead.
- Index Array function—The Index Array function uses a 32-bit integer


 as the default for the index input. If the array you wire


 to the array input contains less than 256 elements, you


 can change the representation of the input from a 32-bit integer to an 8-bit


 integer.

You also can save FPGA resources by choosing the smallest data type possible for the


 following block diagram objects:

- Comparison functions
- Wires to Case structures case selectors
- Controls and indicators

Parent topic:

Optimizing FPGA VIs for Speed and Size

Related concepts:

- Avoiding the Iteration Terminal Data Type
- Optimizing FPGA VIs for Speed and Size

<!--NI_TOPIC bundle=labview-fpga-module path=using-variables-to-store-data-fpga-module.html language=enus -->
## TOPIC 00209: Using Variables to Store Data

- bundle_id: `labview-fpga-module`
- source_path: `using-variables-to-store-data-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-variables-to-store-data-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use local or global variables to store data in an FPGA application. A variable stores only the latest value you write to it. If you write to a variable N times before reading from that variable, the N-1 values preceding the latest value are lost. If you do not need to use every data value yo

### Using Variables to Store Data

You can use local or global


 variables to store data in an FPGA application. A variable stores only the latest


 value you write to it. If you write to a variable N times before


 reading from that variable, the N-1 values preceding the latest


 value are lost. If you do not need to use every data value you acquire, variables


 are a good choice because you do not need to write extra code to discard unnecessary


 values.

Global variables appear under the FPGA target in the Project


 Explorer window, and you can access them from any VI running on the FPGA


 target. Use global variables to store data that you need to access from multiple


 VIs. Use local variables for data that you only need to access from a single VI, or


 data that you need to maintain separately for separate instances of a reentrant


 subVI. You can access a local variable only from a single VI. However, when you


 include a local variable in a reentrant subVI, each instance of the subVI contains a


 new instance of the local variable.

Note

Parent topic:

Storing and Transferring Data

<!--NI_TOPIC bundle=labview-fpga-module path=using-vhdl-code-as-component-level-ip-fpga-module.html language=enus -->
## TOPIC 00210: Using VHDL Code as Component-Level IP

- bundle_id: `labview-fpga-module`
- source_path: `using-vhdl-code-as-component-level-ip-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/using-vhdl-code-as-component-level-ip-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use component-level IP (CLIP) to instantiate VHDL code with a defined interface that occupies a portion of an FPGA. You can use CLIP to perform the following tasks: Run VHDL code in parallel with LabVIEW code. Execute VHDL code in multiple clock domains. Include constraints in the compilation. Creat

### Using VHDL Code as Component-Level IP

Use component-level IP (CLIP) to instantiate VHDL code with a defined interface that


 occupies a portion of an FPGA. You can use CLIP to perform the following tasks:

- Run VHDL code in parallel with LabVIEW code.
- Execute VHDL code in multiple clock domains.
- Include constraints in the compilation.
- Create CLIP


 clocks.
- Access hardware I/O. (This is only available for some targets. Refer to the


 hardware documentation for information about I/O


 support in CLIP.)

Note

#### Using CLIP in an FPGA Application

The following steps outline the procedure for using CLIP in an FPGA application:

- Create or acquire the IP.
- Use the Configure Component-Level IP wizard to define the IP interface and


 create a declaration XML file.
- Add the declaration file to the project using the FPGA Target


 Properties dialog box.
- Add CLIP items to the project.
- Use the CLIP items in an FPGA VI.

|  | Tip If you create or modify a declaration XML file using the Configure Component-Level IP wizard, LabVIEW automatically adds the file to the project. |
| --- | --- |

#### Types of CLIP

Support for CLIP varies by FPGA target. Refer to the target hardware


 documentation for information about CLIP support. Some FPGA targets


 support one or both of the following types of CLIP:

- User-defined CLIP —Enables VHDL code to communicate


 directly with an FPGA VI.
- Socketed CLIP —Enables VHDL code to communicate directly


 with an FPGA VI and to access FPGA pins that you cannot access with other


 LabVIEW VIs and functions. Some FPGA targets define a fixed CLIP socket in the


 FPGA where you can insert socketed CLIP.

The following illustration shows the relationship between an FPGA VI and CLIP.

[IMAGE alt='image' src='GUID-E7300344-7A6D-42DB-89B7-2AA6C88CB3BC-a5.png']

Refer to the CLIP Tutorial: Adding Component-Level IP to an FPGA Project for an


 example of using VHDL code as CLIP.

Parent topic:

Integrating Third-Party IP

Related concepts:

- CLIP Tutorial, Part 1: Creating VHDL Code
- Creating or Acquiring IP
- Using the Configure Component-Level IP Wizard
- Adding Component-Level IP to a Project
- Passing Data between Component-Level IP and VIs
- CLIP Tutorial: Adding Component-Level IP to an FPGA Project
- Integrating Third-Party IP

<!--NI_TOPIC bundle=labview-fpga-module path=verify-constraints-clip-comp.html language=enus -->
## TOPIC 00211: Verify Unapplied Constraints in a CLIP Compilation

- bundle_id: `labview-fpga-module`
- source_path: `verify-constraints-clip-comp.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/verify-constraints-clip-comp.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to check whether constraints were applied during FPGA compilation. Ensure you have the following: Access to the compilation output directory. A tool to unzip files. To verify unapplied constraints in a CLIP compilation, complete the following steps. Navigate to C:\NIFPGA. Open the folder f

### Verify Unapplied Constraints in a CLIP
 Compilation

Learn how to check whether constraints were applied during FPGA compilation.

- Access to the compilation output directory.
- A tool to unzip files.

To verify unapplied constraints in a CLIP compilation, complete the following
 steps.

1. Navigate to C:\NIFPGA.
2. Open the folder for your compilation.
3. Unzip output_files.zip and locate
 unapplied_constraints.xdc.
4. Open the file and search for the constraint.

The expected result is that the file lists all unapplied
 constraints for the compilation.

Parent topic:

Creating or Acquiring IP

Related concepts:

- Creating or Acquiring IP

<!--NI_TOPIC bundle=labview-fpga-module path=viewing-signals-using-the-waveform-viewer-fpga-module.html language=enus -->
## TOPIC 00212: Viewing Signals Using the Waveform Viewer

- bundle_id: `labview-fpga-module`
- source_path: `viewing-signals-using-the-waveform-viewer-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/viewing-signals-using-the-waveform-viewer-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a simulation export, you can specify the types of signals you are investigating so that they show up in the waveform viewer in LabVIEW-specific groupings. These groupings help you determine which signal corresponds to a component on the LabVIEW block diagram. You must be familiar wit

### Viewing Signals Using the Waveform Viewer

When you create a simulation export, you can specify the types of


 signals you are investigating so that they show up in the waveform viewer in


 LabVIEW-specific groupings. These groupings help you determine which signal


 corresponds to a component on the LabVIEW block diagram.

Note

The main groups of signals to appear in the waveform viewer are the following:

- Top-level controls and indicators
- I/O
- CLIP top-level port signals
- IP Integration Node top-level port signals

Within the main groups, the waveform viewer also shows implicit signals, such as


 clocks, the enable chain, register update logic, registers, and block diagram


 wires. The enable chain enforces the LabVIEW dataflow paradigm, so it is useful as a


 starting point for determining how a signal fits into the overall execution order of


 the FPGA VI. You can see only resources that are related directly to block diagram


 signals.

|  | Tip Use the VHDL names for block diagram objects to correspond these objects with signals in the waveform viewer. VHDL names appear at the bottom of the Context Help window. |
| --- | --- |

Parent topic:

Debugging FPGA VIs Using a Third-Party Simulator

Related concepts:

- Dataflow and the Enable Chain in FPGA VIs

<!--NI_TOPIC bundle=labview-fpga-module path=viewing-the-bitfile-path-fpga-module.html language=enus -->
## TOPIC 00213: Viewing the Bitfile Path

- bundle_id: `labview-fpga-module`
- source_path: `viewing-the-bitfile-path-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/viewing-the-bitfile-path-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The bitfile contains all the configuration information from the block diagram defining the internal logic and digital circuit of the FPGA and device-specific information from other files associated with the FPGA target. When the FPGA application executes, the bitfile loads on the FPGA chip and recon

### Viewing the Bitfile Path

The bitfile contains all the configuration information from the block diagram


 defining the internal logic and digital circuit of the FPGA and device-specific


 information from other files associated with the FPGA target. When the FPGA


 application executes, the bitfile loads on the FPGA chip and reconfigures the gate


 array logic. If you want to share or reference a bitfile that you create in the


 LabVIEW FPGA Module, you need the bitfile path, which is available only in the FPGA


 build specification.

Complete the following steps to view the bitfile path corresponding to a compiled


 FPGA VI:

1. Compile the FPGA VI.
2. Right-click the FPGA build specification in the Project


 Explorer window and select


 Properties .
3. You can view the bitfile path of the VI on the


 Information page of the Compilation


 Properties dialog box.
4. Click OK .

Parent topic:

Introduction to FPGA Applications and Projects

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Understanding the LabVIEW FPGA Compile System

<!--NI_TOPIC bundle=labview-fpga-module path=viewing-the-latencies-of-data-paths-in-a-dsp48e-or-dsp48e1-function-fpga-module.html language=enus -->
## TOPIC 00214: Viewing the Latencies of Data Paths in a DSP48E or DSP48E1 Function

- bundle_id: `labview-fpga-module`
- source_path: `viewing-the-latencies-of-data-paths-in-a-dsp48e-or-dsp48e1-function-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/viewing-the-latencies-of-data-paths-in-a-dsp48e-or-dsp48e1-function-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the schematic at the bottom of the configuration dialog box to view the latencies of data paths within a DSP48E or DSP48E1 function. These latencies are the number of clock cycles data needs to flow from an input terminal to an output terminal. For example, a to p is one data path. b to p is ano

### Viewing the Latencies of Data Paths in a DSP48E or DSP48E1 Function

Use the schematic at the bottom of the configuration dialog box to view the


 latencies of data paths within a DSP48E or DSP48E1


 function. These latencies are the number of clock cycles data needs to flow from an


 input terminal to an output terminal. For example, a to


 p is one data path. b to


 p is another. Each register you add in a data path increases the latency of that data path


 by one clock cycle but does not affect the latency of other data paths. Therefore,


 the latencies of data paths can become unbalanced as you configure a function.

Whether this imbalance is acceptable depends on how you are using the function. Some


 applications do not require data paths with balanced latencies. For example, if you


 are wiring one function to another, imbalances within each function can be cancelled


 out by equal-but-opposite imbalances in other functions. However, some applications


 require data paths with balanced latencies. The following example shows a situation


 where balanced data paths are necessary.

Consider a function that is configured as a multiplier, p =


 a
<sup>2</sup>. That is, you wire the same value to both the a


 and b input terminals of the function. This value starts at 0


 and increases by 1 every clock cycle. This DSP48E function contains the following


 data paths:

[IMAGE alt='image' src='GUID-F685CC66-7BD2-4FCE-850C-5F2D11D6C639-a5.png']

In this schematic, the a–>p data


 path contains the following three registers:

- a register 2
- m register
- p

Because this data path contains three registers, the data path has a latency of three


 clock cycles. However, the b–>p


 data path contains only two registers and therefore has a latency of two clock


 cycles. This latency imbalance means that:

- For the a –> p data path, the


 n 
 th clock cycle uses the value of a from the


 ( n – 3) th clock cycle
- For the b –> p data path, the


 n 
 th clock cycle uses the value of a from the


 ( n – 2) th clock cycle

This imbalance makes it impossible to accomplish the goal of calculating


 p = a
<sup>2</sup>. The following table shows the inputs and output of this function


 during its first eight clock cycles:

| Clock cycle | Value of a | Value of p | Explanation |
| --- | --- | --- | --- |
| 1 | 0 | N/A | Neither data path produces a value during this clock cycle. |
| 2 | 1 | N/A |  |
| 3 | 2 | 0 | The function multiplies the initialized value of the second register and 0 (value of a from the first clock cycle). |
| 4 | 3 | 0 | The function multiplies 0 (value of a from the first clock cycle) and 1 (value of a from the second clock cycle). |
| 5 | 4 | 2 | The function multiplies 1 (value of a from the second clock cycle) and 2 (value of a from the third clock cycle). |
| 6 | 5 | 6 | The function multiplies 2 (value of a from the third clock cycle) and 3 (value of a from the fourth clock cycle). |
| 7 | 6 | 12 | The function multiplies 3 (value of a from the fourth clock cycle) and 4 (value of a from the fifth clock cycle). |
| 8 | 7 | 20 | The function multiplies 4 (value of a from the fifth clock cycle) and 5 (value of a from the sixth clock cycle). |

In this application, the imbalance of latencies causes incorrect calculations. In


 this situation, use the Registers page to add another


 register to the b–>p data path. If


 you do this, the schematic resembles the following illustration:

[IMAGE alt='image' src='GUID-955D0BC4-163F-4B94-85C2-42955D9A5527-a5.png']

In the previous illustration, notice that both data paths have three registers, which


 means that for both data paths, the n
<sup>th</sup> clock cycle uses the value of a from the


 (n – 3)<sup>th</sup> clock cycle.

The following table shows the inputs and output of this function during its first


 eight clock cycles:

| Clock cycle | Value of a | Value of p | Explanation |
| --- | --- | --- | --- |
| 1 | 0 | N/A | Neither data path produces a value during this clock cycle. |
| 2 | 1 | N/A |  |
| 3 | 2 | N/A |  |
| 4 | 3 | 0 | The function multiplies 0 and 0 (value of a during the first clock cycle). |
| 5 | 4 | 1 | The function multiplies 1 and 1 (value of a during the second clock cycle). |
| 6 | 5 | 4 | The function multiplies 2 and 2 (value of a during the third clock cycle). |
| 7 | 6 | 9 | The function multiplies 3 and 3 (value of a during the fourth clock cycle). |
| 8 | 7 | 16 | The function multiplies 4 and 4 (value of a during the fifth clock cycle). |

Now that the latencies of the data paths are balanced, this DSP48E function


 calculates p = a
<sup>2</sup> correctly.

Parent topic:

Configuring DSP48E and DSP48E1 Functions

Related concepts:

- Adjusting the Length of the Internal Combinatorial Path of a DSP48E or DSP48E1 Function
- Configuring DSP48E and DSP48E1 Functions
- Retaining the Precision of DSP48E and DSP48E1 Function Terminals

<!--NI_TOPIC bundle=labview-fpga-module path=what-is-fpga-module.html language=enus -->
## TOPIC 00215: What is the FPGA Module?

- bundle_id: `labview-fpga-module`
- source_path: `what-is-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/what-is-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Module is a software add-on for LabVIEW that you can use to more efficiently and effectively design FPGA-based systems through a highly integrated development environment, IP libraries, a high-fidelity simulator, and debugging features.Use the FPGA Module and LabVIEW to create VIs that run

### What is the FPGA Module?

The *FPGA Module* is a software add-on for LabVIEW that you can
 use to more efficiently and effectively design FPGA-based systems through a highly
 integrated development environment, IP libraries, a high-fidelity simulator, and
 debugging features.Use the FPGA Module and LabVIEW to create VIs that run on
 NI FPGA targets, such as Reconfigurable I/O (RIO) devices. FPGA targets contain a
 reconfigurable FPGA (Field-Programmable Gate Array) surrounded by fixed I/O resources.
 Depending on the specific FPGA target, fixed I/O resources can include analog and digital
 resources, such as analog-to-digital converters (ADCs) and digital-to-analog converters
 (DACs), that you can control from the FPGA.

With the FPGA Module, you configure the behavior of the reconfigurable FPGA to match the
 requirements of a specific measurement and control system. The VI you create to run on
 an FPGA target is called the *FPGA VI*. Use the FPGA Module to write FPGA
 VIs. When you download the FPGA VI to the FPGA, you are programming the functionality of
 the FPGA target. Each new FPGA VI you create and download is a custom timing,
 triggering, and I/O solution.

Browse Related Concepts for topics to help you get started with building a LabVIEW FPGA
 application.

Related concepts:

- Introduction to FPGA Applications and Projects
- Programming FPGAs Overview
- Introduction to FPGA Hardware Concepts
- FPGA Target Hardware Documentation

#### Establishing a Design Flow

Depending on the complexity of your FPGA application, you may want to write and compile a
 program quickly, or you may want to leverage the built-in simulator to debug, test, and
 verify your code without having to compile every time you make a change. The following
 graphic outlines one recommended FPGA design flow that begins with evaluating your system
 requirements and ends with deploying your system.

[IMAGE alt='image' src='GUID-0860ECC3-EED9-406D-9D7B-AAFADEFDC0BC-a5.png']

<!--NI_TOPIC bundle=labview-fpga-module path=wiring-si-nodes-using-handshaking.html language=enus -->
## TOPIC 00216: Wiring Single-Input Nodes Using Handshaking

- bundle_id: `labview-fpga-module`
- source_path: `wiring-si-nodes-using-handshaking.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/wiring-si-nodes-using-handshaking.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to connect handshaking terminals between single-input nodes in a Single-Cycle Timed Loop. This process ensures data validity and maintains timing accuracy. Ensure you have the following: Familiarity with single-cycle Timed Loops (SCTLs) in LabVIEW FPGA. Understanding of handshaking termina

### Wiring Single-Input Nodes Using
 Handshaking

Learn how to connect handshaking terminals between single-input nodes in a Single-Cycle
 Timed Loop. This process ensures data validity and maintains timing accuracy.

- Familiarity with single-cycle Timed Loops (SCTLs) in LabVIEW FPGA.
- Understanding of handshaking terminals:
  - input valid
  - output valid
  - ready for input
  - ready for output
- Access to a block diagram with three nodes (upstream, function, downstream).

- U (upstream)
- F (function)
- D (downstream)

Note

- Setting input valid to TRUE when
 ready for input is FALSE
- Ignoring ready for output

Note

Throughput
 Conventions in FPGA-Based Systems

Tip

Throughput

F

- When F receives a valid input, it starts computing a result.
 You must wait at least T f clock
 cycles before F can accept another valid input.
- The Throughput control determines
 T f .
- A smaller value allows F to accept the next valid input more
 quickly.
- A larger value delays the reception of the next valid input.
- A smaller value also means the ready for input terminal of
 F can return TRUE earlier.

Carry out the following steps to wire single-input nodes using handshaking.

1. Wire the output valid terminal of U to the
 input valid terminal of F. 
 This connection signals F when U has
 produced a valid output value.
2. Verify that F receives input valid =
 TRUE. 
 F begins computing.
3. Keep the output valid terminal of F set to
 FALSE while F is computing.
4. Wait until at least L<sub>f</sub> clock
 cycles have elapsed since F began computing.
5. Verify that the ready for output terminal for
 F is TRUE. Then, set the output
 valid terminal of F to TRUE. 
 If downstream is not ready, F buffers the result and keeps the
 value of the output valid terminal FALSE.
6. Wire the output valid terminal of F to the
 input valid terminal of D. 
 This signals D when F presents a valid
 output value.
7. Wire the ready for input terminal of D to the
 ready for output terminal of F through a
 Feedback Node. 
 This action propagates downstream readiness with a one-cycle delay.
8. Wire the ready for input terminal of F to the
 ready for output terminal of U through a
 Feedback Node. 
 This action propagates the upstream readiness with a one-cycle delay.

#### Signal Connections and Timing Alignment in a Single-Cycle Timed Loop

Figure 2.

[IMAGE alt='Diagram showing a Timed Loop with FIFO and feedback nodes for data processing.' src='GUID-6372CF61-B303-4C5D-9AC2-5E17496508C9-a5.png']

Figure 2.

U

F

D

- input valid
- output valid
- ready for input
- ready for output

- Verify that output valid becomes TRUE for one
 cycle only when the system receives valid input and the downstream is ready.
- Confirm that readiness signals propagate correctly through Feedback Nodes.

Parent topic:

Scheduling Timing Using Handshaking Signals

Related concepts:

- Scheduling Timing Using Handshaking Signals
- Throughput Conventions in FPGA-Based Systems

<!--NI_TOPIC bundle=labview-fpga-module path=working-with-fpga-build-specifications-fpga-module.html language=enus -->
## TOPIC 00217: Working with FPGA Build Specifications

- bundle_id: `labview-fpga-module`
- source_path: `working-with-fpga-build-specifications-fpga-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/working-with-fpga-build-specifications-fpga-module.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must create a build specification before you can compile the FPGA VI into an FPGA application. LabVIEW uses the build options you set to generate the HDL and bitfile from the block diagram. Right-click a build specification under an FPGA target in the Project Explorer window and select from the

### Working with FPGA Build Specifications

You must create a build specification before you can compile the FPGA VI into an


 FPGA application. LabVIEW uses the build options you set to generate the HDL and


 bitfile from the block diagram.

Right-click a build specification under an FPGA target in the Project


 Explorer window and select from the following options. The options


 available for a build specification vary depending on your specific FPGA target.

- Build —Generates intermediate files only if the FPGA VI or


 build specification changed since the last time you compiled the VI. Then this


 command compiles the VI.
- Rebuild —Generates intermediate files regardless of


 whether the FPGA VI or build specification changed, and then compiles the


 VI.
- Estimate Resource Usage —Uses Xilinx tools to estimate FPGA resource usages without compiling. If the generated


 code signature is not current, this command first generates intermediate files


 and then estimates resource usage. The availability of this option depends on


 your specific FPGA target.
- Check Signature —Determines whether the bitfile is


 current. If the bitfile does not exist, the command checks the generated code


 signature.
- Generate Intermediate Files —Generates intermediate files


 without compiling the VI. Generating intermediate files catches certain code


 generations errors.
- Display Compilation Results —Displays the Compilation Status window. You must build the build


 specification once to display the Compilation Status window.

Note

Project Explorer

Build

#### Specifying a Default Build Specification

The default build specification is the build specification that the


 Run button uses to compile and run an FPGA application.


 If you click the Run button without first making a build


 specification, LabVIEW automatically creates and specifies a default build


 specification for the corresponding VI.

To specify the default build specification, place a checkmark in the Set


 as default build specification checkbox on the Source Files page of the Compilation


 Properties dialog box.

Parent topic:

Compiling, Downloading, and Running FPGA VIs

Related concepts:

- Compiling, Downloading, and Running FPGA VIs
- Estimating FPGA Resource Usage without Compiling

<!--NI_TOPIC bundle=labview-fpga-module path=writing-to-dma-fifos-from-host-vis-fpga-interface.html language=enus -->
## TOPIC 00218: Writing to DMA FIFOs from Host VIs

- bundle_id: `labview-fpga-module`
- source_path: `writing-to-dma-fifos-from-host-vis-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/writing-to-dma-fifos-from-host-vis-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to write to a DMA FIFO from a host VI. Open a reference to an FPGA VI or bitfile. The FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you want to open a reference to an FPGA VI. The host VI does not need to be in a project if you open a referenc

### Writing to DMA FIFOs from Host VIs

Complete the following steps to write to a DMA FIFO from a host VI.

1. Open a reference to an FPGA VI or bitfile. Note The



 FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you



 want to open a reference to an FPGA VI. The host VI does not need to be in a



 project if you open a reference to a bitfile. If you open a reference to an



 FPGA VI, the project must include a DMA FIFO item under the FPGA target and



 the FPGA VI must include a FIFO Method Node configured with the Read method



 on the block diagram that reads the DMA FIFO item.
2. Add an Invoke Method function to the block diagram of the



 host VI in the data flow where you want the host VI to write to the DMA FIFO.



 Wire the FPGA VI Reference In input.
3. Click the Invoke Method function and select



 FIFO»Write from the shortcut menu,



 where FIFO is the name of the FIFO



 item in the project. Wire the inputs and outputs as needed. The Write method



 returns Empty Elements Remaining when the data is written



 or when the Timeout period ends.
4. Add the Close FPGA VI Reference function to the block



 diagram.
5. Wire the FPGA VI Reference Out output on the Invoke Node



 to the FPGA VI Reference In input on the Close FPGA VI



 Reference function.

Note

Parent topic:

Communicating with FPGA VIs

Related concepts:

- Opening a Reference to an FPGA VI, Build Specification, or Bitfile

<!--NI_TOPIC bundle=labview-fpga-module path=writing-to-fpga-vi-controls-fpga-interface.html language=enus -->
## TOPIC 00219: Writing to FPGA VI Controls

- bundle_id: `labview-fpga-module`
- source_path: `writing-to-fpga-vi-controls-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-fpga-module/raw/resource/enus/writing-to-fpga-vi-controls-fpga-interface.html
- document_id: `labview-fpga-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to write to a control in an FPGA VI from a host VI. Open a reference to the FPGA VI or bitfile. The FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you want to open a reference to an FPGA VI. The host VI does not need to be in a project if you o

### Writing to FPGA VI Controls

Complete the following steps to write to a control in an FPGA VI from a host VI.

1. Open a reference to the FPGA VI or bitfile. Note The


 FPGA target, FPGA VI, and host VI must be in the same LabVIEW project if you


 want to open a reference to an FPGA VI. The host VI does not need to be in a


 project if you open a reference to a bitfile.
2. Add the Read/Write Control function to the block diagram.


 Notice that the Read/Write Control function contains one


 Unselected input.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function or the


 Bitfile reference out output of the Open Dynamic Bitfile Reference function to the


 FPGA VI Reference In input of the Read/Write Control


 function.
4. Click the Unselected input. The shortcut menu lists all


 front panel controls and indicators in the FPGA VI. Note If the


 FPGA VI is not saved, or does not have any controls or indicators, this list


 is empty.
5. Select a control available in the FPGA VI from the shortcut menu. Notice that


 the Unselected input changes to reflect the name of the


 control in the FPGA VI.

To write to more controls in the FPGA VI, right-click the Read/Write Control function


 and select Add Element from the shortcut menu and then


 customize the input as described in the previous step. You also can click the bottom


 line of the Read/Write Control function with the Positioning tool and drag the line


 down to add more controls and indicators. The read and write operations execute


 sequentially from top to bottom. Also, if the FPGA VI has subVIs and you want to


 access controls and indicators on the subVI, you must wire the subVI controls and


 indicators to the controls and indicators of the FPGA VI that is used in the Open


 FPGA VI Reference function.

Note

Change to Write

Parent topic:

Transferring Data Using Front Panel Controls and Indicators

Related concepts:

- Stopping, Aborting, and Resetting FPGA VIs
- Opening a Reference to an FPGA VI, Build Specification, or Bitfile
