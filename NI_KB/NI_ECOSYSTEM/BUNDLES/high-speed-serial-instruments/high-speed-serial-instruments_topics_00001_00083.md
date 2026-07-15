# NI DOCUMENT BUNDLE: high-speed-serial-instruments

<!--NI_BUNDLE_CHUNK bundle=high-speed-serial-instruments start=1 end=83 -->
<!--NI_TOPIC bundle=high-speed-serial-instruments path=about-this-manual.html language=enus -->
## TOPIC 00001: About This Manual

- bundle_id: `high-speed-serial-instruments`
- source_path: `about-this-manual.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/about-this-manual.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI High-Speed Serial Instruments User Manual describes how to develop applications for use with the PXIe-6591R, PXIe-6592R, and PXIe-7902 high-speed serial FPGA targets. The PXIe-6591R, PXIe-6592R, and PXIe-7902 are designed for use in the following applications: Real-time data transmission, rec

### About This Manual

The *NI High-Speed Serial Instruments User Manual* describes how to develop applications for use with the PXIe-6591R, PXIe-6592R, and PXIe-7902 high-speed serial FPGA targets.

The PXIe-6591R, PXIe-6592R, and PXIe-7902 are designed for use in the following applications:

- Real-time data transmission, reception, and validation
- Functional test for semiconductor production
- Device interfacing
- High performance embedded systems This manual provides detailed information about the electrical and mechanical requirements of component-level IP (CLIP) and LabVIEW FPGA design. Chapters 2 and 3 contain information about the PXIe-6591R hardware architecture and functionality, respectively. Chapters 4 and 5 contain information about the PXIe-6592R hardware architecture and functionality, respectively. Chapters 6 and 7 contain information about the PXIe-7902 hardware architecture and functionality, respectively. Chapter 8 contains information about how to develop applications for all high-speed serial devices.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=accessing-the-xilinx-vivado-tools.html language=enus -->
## TOPIC 00002: Accessing the Xilinx Vivado Tools

- bundle_id: `high-speed-serial-instruments`
- source_path: `accessing-the-xilinx-vivado-tools.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/accessing-the-xilinx-vivado-tools.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to run Xilinx Vivado and generate a blank project for CLIP development. Ensure that your system meets the system requirements listed in the NI High-Speed Serial Instruments Readme, available from the Start menu and at ni.com/manuals. You can check the versions of the too

### Accessing the Xilinx Vivado Tools

Complete the following steps to run Xilinx Vivado and generate a blank project for CLIP development.

1. Ensure that your system meets the system requirements listed in the NI High-Speed Serial Instruments Readme, available from the Start menu and at ni.com/manuals. You can check the versions of the tool on your machine by selecting Start»Control Panel»Programs and Features. 
 Note If Vivado is installed by LabVIEW FPGA, it does not appear in Programs and Features.
2. Open the Xilinx Vivado Tool directory by navigating to C:\NIFPGA\programs\ VivadoXXXX_Y, where XXXX and Y refer to the Xilinx Vivado tool versions. For example, <VIVADO_DIR> version 2013.4 is located at C:\NIFPGA\programs\ Vivado2013_4.
3. Run the Xilinx Vivado batch file: <XilinxVivadoDir>\bin\vivado.bat. 
 You may receive the following warning when launching Vivado.Figure 17.EDK Environment Error Message[IMAGE alt='image' src='GUID-7BC1FBAA-AC2C-4B40-9916-C954FBEE4836-a5.png']
This error message is expected. You can ignore the error message if you are not using the Xilinx Embedded Development Kit (EDK). The EDK is not required for development with the high-speed serial device.
4. Click New Project and follow the instructions in the wizard. 
 You can also export an FPGA VI as a Vivado Design Suite project, as detailed in the [Exporting to Vivado](exporting-to-vivado.html) section.

Parent topic:

Socketed CLIP Development

<!--NI_TOPIC bundle=high-speed-serial-instruments path=adding-high-speed-serial-device-target-i-o.html language=enus -->
## TOPIC 00003: Adding High-Speed Serial Device Target I/O

- bundle_id: `high-speed-serial-instruments`
- source_path: `adding-high-speed-serial-device-target-i-o.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/adding-high-speed-serial-device-target-i-o.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to add target I/O for the high-speed serial device and to access signals from any instantiated CLIP on the block diagram: Place an FPGA I/O node on the FPGA target block diagram. The FPGA I/O node is located on the palette under Functions FPGA I/O FPGA I/O Node . Right-c

### Adding High-Speed Serial Device Target I/O

Complete the following steps to add target I/O for the high-speed serial device and to access signals from any instantiated CLIP on the block diagram:

1. Place an FPGA I/O node on the FPGA target block diagram. The FPGA I/O node is located on the palette under Functions»FPGA I/O»FPGA I/O Node.
2. Right-click the FPGA I/O node and select Add New FPGA I/O.
3. In the New FPGA I/O dialog box, select resources under Available Resources and add them to New FPGA I/O using the right arrow button.
4. To remove a resource, select the resource under New FPGA I/O and click the left arrow button.
5. Click OK.

Parent topic:

Developing with LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=before-you-begin.html language=enus -->
## TOPIC 00004: Before You Begin

- bundle_id: `high-speed-serial-instruments`
- source_path: `before-you-begin.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/before-you-begin.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information you need before developing applications using the high-speed serial devices. Development Requirements Successful system design with high-speed serial devices may require knowledge in the following areas, depending on your application. High-speed serial fundamentals

### Before You Begin

This section contains information you need before developing applications using the high-speed serial devices.

#### Development Requirements

Successful system design with high-speed serial devices may require knowledge in the
 following areas, depending on your application.

- High-speed serial fundamentals
- VHDL code design
- NI LabVIEW and LabVIEW FPGA programming

To learn about the fundamentals required to develop a system with high-speed serial
 devices, refer to the resources in the following table.

| Concept | Resources |
| --- | --- |
| High-speed serial fundamentals | High-Speed Serial I/O Made Simple: A Designers’ Guide, with FPGA Applications is available at xilinx.com. |
| VHDL code design | Some VHDL training or experience is required before working with the high-speed serial devices. Do not attempt to develop Component-Level IP (CLIP) without VHDL knowledge. For information about programming options, refer to An Introduction to PXI High-Speed Serial Instruments​. |
| NI LabVIEW and LabVIEW FPGA | For NI LabVIEW and LabVIEW FPGA training resources, refer to ni.com/training. For information about FPGA resources when using the LabVIEW FPGA Module and NI FPGA hardware, refer to The NI LabVIEW High-Performance FPGA Developer’s Guide. |

Related information:

- An Introduction to PXI High-Speed Serial Instruments
- The NI LabVIEW High-Performance FPGA Developer’s Guide

#### Installation Instructions

Refer to the getting started guide for your device (refer to the [Related Documentation](related-documentation.html) section of this document) for instructions about how to install LabVIEW, LabVIEW FPGA, the NI LabVIEW Instrument Design Libraries for High Speed Serial Instruments software, and your high-speed serial device.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=building-a-netlist-from-the-ip-core.html language=enus -->
## TOPIC 00005: Building a Netlist from the IP Core

- bundle_id: `high-speed-serial-instruments`
- source_path: `building-a-netlist-from-the-ip-core.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/building-a-netlist-from-the-ip-core.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: LabVIEW FPGA does not support Verilog source files in Component Level IP. However, you can generate EDIF netlists from any synthesized Verilog components in the IP you are using and instantiate the netlist in a VHDL wrapper.The following steps are an example of how to generate an EDIF netlist from t

### Building a Netlist from the IP Core

LabVIEW FPGA does not support Verilog source files in Component Level IP. However, you can generate EDIF netlists from any synthesized Verilog components in the IP you are using and instantiate the netlist in a VHDL wrapper.The following steps are an example of how to generate an EDIF netlist from the IP core:

1. Open the example project for your IP core in Vivado.
2. Set the appropriate top-level source file for which you plan to generate a netlist.
3. Run synthesis.
4. Open the Synthesized Design using one of the following methods. 
 Select Open Synthesized Design in the Synthesis Completed pop-up window.
Select the Design Run tab, then select Open Synthesized Design in the left hand pane.
5. In the Tcl Console, enter write_edif <name of entity>.edf to create the netlist that you use when you import the IP core into your LabVIEW project. The netlist location is indicated by the Tcl Console window.
6. The following figure shows the cells associated with the design in the Netlist window. 
 [IMAGE alt='image' src='GUID-CD3718B7-CEBC-417E-B05E-F4FEEAF43446-a5.png']
7. To build .edf files for an associated cell, enter the following command: write_edif -cell <name of cell> <file name>.edf For example, to create an .edf for clock_module_i, enter the following command: write_edif -cell clock_module_i aurora_64b66b_clock_module.edf 
 Note You may have to specify a longer path name depending on the location of the cell in your project. For example, clock_module_i may be located under  aurora_64b66b_0_block_i/clock_module_i.
8. Copy the netlist into your LabVIEW FPGA CLIP directory.
9. Include your netlist in the list of synthesis files when running the CLIP Wizard.

Parent topic:

Generating an IP Core from the Xilinx Vivado IP Catalog

<!--NI_TOPIC bundle=high-speed-serial-instruments path=clocking-architecture-6591.html language=enus -->
## TOPIC 00006: Clocking Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `clocking-architecture-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/clocking-architecture-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6591R module includes dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module. Refer to

### Clocking Architecture

The PXIe-6591R module includes dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module. Refer to the [Configuring the High-Speed Serial Device LabVIEW FPGA Targets](configuring-the-high-speed-serial-device-labv.html) section of Chapter[Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), [Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), for more detailed information about configuring clocking in your LabVIEW project.

Parent topic:

PXIe-6591R Module Overview

<!--NI_TOPIC bundle=high-speed-serial-instruments path=clocking-architecture-6592.html language=enus -->
## TOPIC 00007: Clocking Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `clocking-architecture-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/clocking-architecture-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6592R modules include dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module. 12 PXIe-6

### Clocking Architecture

The PXIe-6592R modules include dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module.

| Clock Name | Frequency Range | Available Sources |
| --- | --- | --- |
| MGT_RefClk0 | 60 MHz to 700 MHz | Backplane: PXIe_Clk100 and PXIe_DStarAFront panel: CLK IN/OUT |
| MGT_RefClk1 |  |  |

Refer to the [Configuring the High-Speed Serial Device LabVIEW FPGA Targets](configuring-the-high-speed-serial-device-labv.html) section of Chapter[Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), [Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), for more detailed information about configuring clocking in your LabVIEW project.

Parent topic:

PXIe-6592R Module Overview

<!--NI_TOPIC bundle=high-speed-serial-instruments path=clocking-architecture-7902.html language=enus -->
## TOPIC 00008: Clocking Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `clocking-architecture-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/clocking-architecture-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-7902 modules include dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module. Refer to t

### Clocking Architecture

The PXIe-7902 modules include dedicated clocking hardware to provide a flexible clocking solution for generating the high-speed serial transceiver reference clocks (MGT_RefClk). Use the Clocking and IO properties page in the LabVIEW project to configure the clock settings for your module. Refer to the [Configuring the High-Speed Serial Device LabVIEW FPGA Targets](configuring-the-high-speed-serial-device-labv.html) section of Chapter[Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), [Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), for more detailed information about configuring clocking in your LabVIEW project.

Parent topic:

PXIe-7902 Module Overview

<!--NI_TOPIC bundle=high-speed-serial-instruments path=compiling-labview-fpga-vis.html language=enus -->
## TOPIC 00009: Compiling LabVIEW FPGA VIs

- bundle_id: `high-speed-serial-instruments`
- source_path: `compiling-labview-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/compiling-labview-fpga-vis.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: You may need to purchase and install additional licenses to compile FPGA designs that incorporate licensed cores from Xilinx or third-party IP vendors. Refer to UG 973: Vivado Design Suite: Release Notes, Installation, and Licensing at xilinx.com for information about managing licenses. The high-spe

### Compiling LabVIEW FPGA VIs

You may need to purchase and install additional licenses to compile FPGA designs that incorporate licensed cores from Xilinx or third-party IP vendors. Refer to UG 973: Vivado Design Suite: Release Notes, Installation, and Licensing at xilinx.com for information about managing licenses.

The high-speed serial devices include large FPGA devices that require a 64-bit compile worker. Refer to the NI High-Speed Serial Readme for more information about what platforms to use to compile bitfiles.

If you are using LabVIEW FPGA 2014 or later, you cannot add additional licenses to remote compile workers in the NI LabVIWEW FPGA Compile Cloud Service. You cannot use NI LabVIEW FPGA Compile Cloud Service to compile designs that incorporate Xilinx or other third-party licensed cores.

Parent topic:

Developing with LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=configuring-the-high-speed-serial-device-labv.html language=enus -->
## TOPIC 00010: Configuring the High-Speed Serial Device LabVIEW FPGA Targets

- bundle_id: `high-speed-serial-instruments`
- source_path: `configuring-the-high-speed-serial-device-labv.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/configuring-the-high-speed-serial-device-labv.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure your high-speed serial device LabVIEW project: Create a new project by selecting File New Project , or open an existing project by selecting File Open . Right-click My Computer in the Project Explorer window and select New Targets and Devices from the shortc

### Configuring the High-Speed Serial Device LabVIEW FPGA Targets

Complete the following steps to configure your high-speed serial device LabVIEW project:

1. Create a new project by selecting File»New»Project, or open an existing project by selecting File»Open.
2. Right-click My Computer in the Project Explorer window and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box.
3. Select New target or device and select your device.
4. Add the protocol IP through your CLIP. Right-click the device name and select Properties»Component-Level IP. 
 Note If you are using example CLIP or pre-made CLIP, you can import the CLIP using the dialog box, or you can click on the Create File icon to create a new CLIP using the CLIP Wizard.Note You can modify a CLIP by selecting the preexisting CLIP Declaration Name and clicking Modify File.
5. If you are generating new CLIP, follow the instructions in the CLIP Wizard to interface your CLIP with LabVIEW FPGA. You do not need to use the CLIP Wizard if you are reusing an existing CLIP. Refer to the [FPGA Module Help](http://zone.ni.com/reference/en-XX/help/371599K-01/) for more detailed information about the CLIP Wizard. The CLIP Wizard guides you through the following tasks. 
 Adding VHDL source, XDC constraints, and EDF/EDN/EDIF netlists
Configuring device types
Configuring generics
Performing syntax checks
Specifying how to use the signals in your CLIPNote In Step 2 of the CLIP Wizard, select the appropriate Component Level IP Type for your target.Note After you create the CLIP and add the files, you do not need to modify the CLIP for any changes to take place if you do not change the source paths. If you change the source paths or modify the CLIP source files, you must use the CLIP Wizard.
6. Instantiate the CLIP in the I/O socket. When you add a new target to the project, LabVIEW automatically creates a compatible I/O socket in the project. Right-click the socket and select Properties, then select General under Category.
7. Select a declaration from the drop-down menu under Socketed Component Level IP Declaration.
8. Click OK. The user-defined signals in your CLIP appear under the socket item.
9. Right-click the IO socket and select Properties»Clocking and IO to configure the Clocking and IO Configuration properties for your device. 
 Note Clocking and routing information is compile-time static and cannot be reconfigured at runtime.Note If you are using an example project or a Sample Project, the Clocking and IO Configuration tabs are already configured. If you create a new project, default values are configured, but you must review the settings and ensure that they are correct. If you insert a CLIP into the socket but do not configure the Clocking and IO page, an error is returned.Note The high-speed serial devices support empty sockets.
10. Select the Clocking tab.
11. Under Input Clock Configuration, select your input clock and its frequency in MHz. The input clock is sourced from one of the following locations: 
 Device backplane (PXIe_Clk100)
CLK IN connector on the front panel
10 MHz Onboard Clock (PXIe-6592R only)
12. Under Output Clock Configuration, select any output reference clocks you want to use and specify their frequencies in MHz. The output clocks that you select here are routed to your CLIP for use with your application. 
 Note (PXIe-6591R only) When CLK IN/OUT is enabled as an output reference clock, it routes the specified frequency to the SMA connector.Note (PXIe-6592R only) When PFI 0/CLK OUT, PFI 1, PFI 2, and PFI 3 are enabled as output reference clocks, they route the specified frequency to the corresponding SMB connector.Note If you specify an invalid combination of input clock frequencies and output clock frequencies, an error message appears and the OK button is dimmed until you reconfigure the clocks to a valid frequency combination.
13. Select the IO Configuration tab.
14. Under Active Serial Lanes, select the checkbox for any serial lanes that you want configured for Transmit (TX) or Receive (RX). Select the All/None checkbox to select/deselect all serial lanes. 
 Note Selecting the active serial lanes adds additional placement constraints to your project based on the lanes you select, so ensure that you select all lanes used in your project.
15. Under GPIO Configuration, use the Voltage Family selector box to specify the voltage level used by the GPIO (Digital Data and Control on the PXIe-6591R, and PFI 0, PFI 1, PFI 2, and PFI 3 on the PXIe-6592R). 
 Refer to Table 1 for a list of clocking and routing dependencies for the PXIe-6591R and PXIe-7902. Refer to Table 2 for a list of clocking and routing dependencies for the PXIe-6592R.
16. Click OK. 
 Table 24.PXIe-6591R and PXIe-7902 Clocking and Routing DependenciesConnector
Valid ConfigurationsCLK IN/OUT
Input clock or output clockTable 25.PXIe-6592R Clocking and Routing DependenciesConnector/Clock
Valid Configurations
NotesPFI 0/CLK IN
Input clock or output clock
When enabled as output clocks, PFI 0/CLK IN/OUT, PFI 1/ CLK OUT, PFI 2/CLK OUT, and PFI 3/CLK OUT must share the same frequency.The output of any enabled PFI*x* line is 10 MHz when Enable CPRI Output Clock Configuration is enabled.If PFI 0/CLK IN/OUT is not configured as the input clock or enabled as an output clock, you can configure PFI 0/CLK IN/OUT for GPIO.
PFI 1
Output clock
When enabled as output clocks, PFI 0/CLK IN/OUT, PFI 1/ CLK OUT, PFI 2/CLK OUT, and PFI 3/CLK OUT must share the same frequency.The output of any enabled PFI*x* line is 10 MHz when Enable CPRI Output Clock Configuration is enabled.If PFI 1/CLK OUT, PFI 2/ CLK OUT, and PFI 3/CLK OUT are not configured as output clocks, you can use them individually for GPIO.
PFI 2
Output clock
PFI 3
Output clock
MGT_RefClk0 and MGT_RefClk1
—
When Enable CPRI Output Clock Configuration is enabled, the internal reference clock is set to 153.6 MHz. This imposes frequency restrictions on MGT_RefClk0 and MGTRefClk1. The output of any PFI lines is 10 MHz, phase-aligned with the 153.6 MHz clock.
MGT_RefClk2
—
This clock’s frequency is always 156.25 MHz.The following steps show an example of how to configure the PXIe-6592R for 140 MHz output on MGT_RefClk0 from a 100 MHz input clock on PFI0/CLK IN.
17. Right-click the IO socket and select Properties»Clocking and IO.
18. Under Input Clock Configuration, select PFI0/CLK IN and enter 100.
19. Under Output Clock Configuration, select the checkbox next to MGT_RefClk0 to enable it.
20. Enter 140 in the text box to the right of MGT_RefClk0.
21. Click OK. 
 Note By selecting an input clock and an output clock in this example, the MGT_RefClk0 is phase loop-locked to the incoming 100 MHz clock. Refer to Chapter[PXIe-6591R Hardware Architecture](pxie-6591r-hardware-architecture.html), [PXIe-6591R Hardware Architecture](pxie-6591r-hardware-architecture.html), for more information about PXIe-6591R clocking capabilities. Refer to Chapter[PXIe-6592R Hardware Architecture](pxie-6592r-hardware-architecture.html), [PXIe-6592R Hardware Architecture](pxie-6592r-hardware-architecture.html), for more information about PXIe-6592R clocking capabilities. Refer to Chapter[PXIe-7902 Hardware Architecture](pxie-7902-hardware-architecture.html), [PXIe-7902 Hardware Architecture](pxie-7902-hardware-architecture.html), for more information about PXIe-7902 clocking capabilities.

Parent topic:

Developing with LabVIEW FPGA

Related concepts:

- PXIe-6592R Clocking

<!--NI_TOPIC bundle=high-speed-serial-instruments path=configuring-trigger-pulses.html language=enus -->
## TOPIC 00011: Configuring Trigger Pulses

- bundle_id: `high-speed-serial-instruments`
- source_path: `configuring-trigger-pulses.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/configuring-trigger-pulses.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: To ensure compatibility with other devices, configure trigger pulses on the high-speed serial device to last for at least two clock cycles of the clock on the receiving device. For example, if the clock on the receiving device is 80 MHz, which corresponds to a clock period of 12.5 nanoseconds, the t

### Configuring Trigger Pulses

To ensure compatibility with other devices, configure trigger pulses on the high-speed serial device to last for at least two clock cycles of the clock on the receiving device. For example, if the clock on the receiving device is 80 MHz, which corresponds to a clock period of 12.5 nanoseconds, the trigger line must be constant for at least 25 ns, which is two cycles of an 80 MHz clock.

Note

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=connecting-and-interfacing-with-the-pxie-6591.html language=enus -->
## TOPIC 00012: Connecting and Interfacing with the PXIe-6591R

- bundle_id: `high-speed-serial-instruments`
- source_path: `connecting-and-interfacing-with-the-pxie-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/connecting-and-interfacing-with-the-pxie-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This chapter contains information about the PXIe-6591R module and its functionality, including front panel diagrams, connectors, and pinouts.

### Connecting and Interfacing with the PXIe-6591R

This chapter contains information about the PXIe-6591R module and its functionality, including front panel diagrams, connectors, and pinouts.

- [Front Panel](front-panel-6591.html) The following figure shows the pinouts for the PXIe-6591R front panel connectors.
- [Recommended Mating Cables and Connectors](recommended-mating-cables-and-connectors-6591.html)
- [Transceiver Lane and Quad Mapping](transceiver-lane-and-quad-mapping-6591.html)
- [Signal Routing](signal-routing-6591.html) The PXIe-6591R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0 and PORT 1 connector pins using a 100 nF AC-coupling capacitor, as shown in the following figure.
- [Socketed CLIP Interface](socketed-clip-interface-6591.html#GUID-B33A437E-EE05-48E3-AFD5-45190EA73637) Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=connecting-and-interfacing-with-the-pxie-6592.html language=enus -->
## TOPIC 00013: Connecting and Interfacing with the PXIe-6592R

- bundle_id: `high-speed-serial-instruments`
- source_path: `connecting-and-interfacing-with-the-pxie-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/connecting-and-interfacing-with-the-pxie-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This chapter contains information about the PXIe-6592R module and its functionality, including front panel diagrams, connectors, and pinouts.

### Connecting and Interfacing with the PXIe-6592R

This chapter contains information about the PXIe-6592R module and its functionality, including front panel diagrams, connectors, and pinouts.

- [Front Panel](front-panel-6592.html) The following figure shows the pinouts for the PXIe-6592R front panel connectors.
- [Recommended Mating Cables and Connectors](recommended-mating-cables-and-connectors-6592.html)
- [Transceiver Lane and Quad Mapping](transceiver-lane-and-quad-mapping-6592.html)
- [Signal Routing](signal-routing-6592.html) The PXIe-6592R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, and PORT 3 connector pins, as shown in the following figure.
- [Socketed CLIP Interface](socketed-clip-interface-6592.html#GUID-E4FA57E5-3C4F-4A75-8751-A0286FFEEAF0) Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=connecting-and-interfacing-with-the-pxie-7902.html language=enus -->
## TOPIC 00014: Connecting and Interfacing with the PXIe-7902

- bundle_id: `high-speed-serial-instruments`
- source_path: `connecting-and-interfacing-with-the-pxie-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/connecting-and-interfacing-with-the-pxie-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This chapter contains information about the PXIe-7902 module and its functionality, including front panel diagrams, connectors, and pinouts.

### Connecting and Interfacing with the PXIe-7902

This chapter contains information about the PXIe-7902 module and its functionality, including front panel diagrams, connectors, and pinouts.

- [Front Panel](front-panel-7902.html) The following figure shows the pinouts for the PXIe-7902 front panel connectors.
- [Recommended Mating Cables and Connectors](recommended-mating-cables-and-connectors-7902.html)
- [Transceiver Lane and Quad Mapping](transceiver-lane-and-quad-mapping-7902.html)
- [Signal Routing](signal-routing-7902.html) The PXIe-7902 high-speed serial differential signals are routed directly from the Virtex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, PORT 3, PORT 4, and PORT 5 connector pins, as shown in the following figure. This signal routing is replicated for every lane across every port.
- [Socketed CLIP Interface](socketed-clip-interface-7902.html#GUID-1581B6DE-537D-47C3-8CFE-14A321E6D7CD) Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=connecting-axi4-lite-and-axi4-stream-interfac.html language=enus -->
## TOPIC 00015: Connecting AXI4-Lite and AXI4-Stream Interfaces to the Host

- bundle_id: `high-speed-serial-instruments`
- source_path: `connecting-axi4-lite-and-axi4-stream-interfac.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/connecting-axi4-lite-and-axi4-stream-interfac.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: In LabVIEW FPGA, the AXI4-Lite and AXI4-Stream wrappers are located on the <Target Name>\CLIP Adapters palette. These wrappers adapt a collection of CLIP I/O that implements AXI4-Lite protocol and signaling into a simple reader or writer endpoints that present 4-wire handshaking to the diagram. This

### Connecting AXI4-Lite and AXI4-Stream Interfaces to the Host

In LabVIEW FPGA, the AXI4-Lite and AXI4-Stream wrappers are located on the <Target Name>\CLIP Adapters palette.

These wrappers adapt a collection of CLIP I/O that implements AXI4-Lite protocol and signaling into a simple reader or writer endpoints that present 4-wire handshaking to the diagram. This handshaking allows easier transition to many FPGA features without the need to implement the state logic on your own.

NI provides the following wrappers:

- AXI4-Lite FXP32x1
- AXI4-Stream Writer FXP32 (1 sample/cycle)
- AXI4-Stream Writer FXP64 (1 sample/cycle, 2 samples/cycle, and 4 samples/cycle)
- AXI4-Stream Reader FXP32 (1 sample/cycle)
- AXI4-Stream Reader FXP64 (1 sample/cycle, 2 samples/cycle, and 4 samples/cycle) Refer to the Aurora sample projects for information about how to use the AXI4-Stream wrappers in an application. The Aurora Simple Streaming sample project uses Create AXI4-Stream Resources.vi to register the CLIP Resources in the form of an AXI4-Stream endpoint. The following figure shows a snippet of the Create AXI-4 Stream Resources.vi block diagram. Figure 19.Create AXI4 Resources VI Block Diagram [IMAGE alt='image' src='GUID-69B64EA8-1C22-49BE-A5F2-0451E60B1BF3-a5.png'] The resulting AXI4-Stream Writer and AXI4-Stream Reader can then be used to transfer data by calling Write.vi and Read.vi, respectively. Refer to the NI High-Speed Serial Instruments Help for more information about how to use high-speed serial VIs. Refer to the Aurora sample projects for information about how to use the AXI4-Stream wrappers in an application.

Parent topic:

Developing with LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=connecting-signals-to-enable-eye-scan.html language=enus -->
## TOPIC 00016: Connecting Signals to Enable Eye Scan

- bundle_id: `high-speed-serial-instruments`
- source_path: `connecting-signals-to-enable-eye-scan.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/connecting-signals-to-enable-eye-scan.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must connect the GTX2_CHANNEL primitive’s registers to the Instruction Framework in order to use Eye Scan. Connect these registers using the FXP32-Address, FXP32-Data version of AXI4-Lite. For information about how to use the AXI4-Lite interface to configure Eye Scan, refer to the Connecting AXI

### Connecting Signals to Enable Eye Scan

You must connect the GTX2_CHANNEL primitive’s registers to the Instruction Framework in order to use Eye Scan. Connect these registers using the FXP32-Address, FXP32-Data version of AXI4-Lite. For information about how to use the AXI4-Lite interface to configure Eye Scan, refer to the [Connecting AXI4-Lite and AXI4-Stream Interfaces to the Host](connecting-axi4-lite-and-axi4-stream-interfac.html) section of this chapter.

Note

[IMAGE alt='image' src='GUID-D0F35F88-F6FE-4080-9B9E-425C896F93C5-a5.png']

[IMAGE alt='image' src='GUID-345C201D-0CB0-4962-9870-4E4C5F9912E3-a5.png']

Parent topic:

Developing with LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=constraints-and-hierarchy.html language=enus -->
## TOPIC 00017: Constraints and Hierarchy

- bundle_id: `high-speed-serial-instruments`
- source_path: `constraints-and-hierarchy.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/constraints-and-hierarchy.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can include CLIP-specific user constraints in the compilation using a constraints file, depending on your specific FPGA target. You can use this mechanism for all constraints except pin placement constraints. For example, you can access a clock directly from a global clock input pin through a gl

### Constraints and Hierarchy

You can include CLIP-specific user constraints in the compilation using a constraints file, depending on your specific FPGA target. You can use this mechanism for all constraints except pin placement constraints. For example, you can access a clock directly from a global clock input pin through a global clock buffer for socketed CLIP. You must constrain the period of this clock.

For constraints on specific components within CLIP, you might need to specify the location of the component within the overall VHDL hierarchy. In such cases, consider prefacing the constraints with the following macros. Prefacing allows the constraints to be applied regardless of the component location in the VHDL hierarchy. If you want to use this example code, copy the code to a text file and save the file as DemoClipAdder.xdc. Add this constraints file along with the VHD file as synthesis files in the Configuring CLIP wizard to implement this constraint.

Parent topic:

Writing a VHDL Wrapper Around the Protocol IP Core

#### Xilinx Vivado

create_clock -period 10.000 -name %ClipInstanceName%Clk -waveform {0.000 5.000} -add [get_pins %ClipInstancePath%/clk]  set_clock_latency -clock [get_clocks {%ClipInstanceName%CLK}] 10.0 [get_pins {%ClipInstancePath%/cAddOut[0]}]

To instantiate the CLIP multiple times, each CLIP instance must have a unique name, and the name must follow VHDL naming conventions. When you include these macros, you do not need to include a separate constraints file for each instance because the FPGA Module creates a unique instance name.

If a CLIP signal is not used, the Xilinx compilation tools might remove the signal from the bitstream. In such cases, you might get an NGBuild error during compilation. To resolve this issue, remove the constraint or use the signal in an FPGA VI.

Caution

6OB8E8FM

<!--NI_TOPIC bundle=high-speed-serial-instruments path=debugging-clocks-using-frequency-counters.html language=enus -->
## TOPIC 00018: Debugging Clocks Using Frequency Counters

- bundle_id: `high-speed-serial-instruments`
- source_path: `debugging-clocks-using-frequency-counters.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/debugging-clocks-using-frequency-counters.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: The Frequency Counter is a module inside the FPGA that provides a built-in method for debugging clock signals during CLIP development. To use the Frequency Counter, complete the following steps: Attach clocks to one of the four DebugClk(3..0) signals in the CLIP. On the host, use the method provided

### Debugging Clocks Using Frequency Counters

The Frequency Counter is a module inside the FPGA that provides a built-in method for debugging clock signals during CLIP development. To use the Frequency Counter, complete the following steps:

1. Attach clocks to one of the four DebugClk(3..0) signals in the CLIP.
2. On the host, use the method provided on all high-speed serial device FPGA reference wires. 
 [IMAGE alt='image' src='GUID-D163B749-7E94-4785-95DF-745D56153AF6-a5.png']The Read FPGA Frequency Counter method initiates a Frequency Counter measurement for 1 ms and reports the frequency of the selected clock. If the Frequency Counter cannot detect a clock signal, it returns Valid? as false. Valid frequencies are reliable between 2 kHz and 333.33 MHz.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=debugging-link-connections-using-eye-scan.html language=enus -->
## TOPIC 00019: Debugging Link Connections Using Eye Scan

- bundle_id: `high-speed-serial-instruments`
- source_path: `debugging-link-connections-using-eye-scan.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/debugging-link-connections-using-eye-scan.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The MGTs on the Xilinx Kintex-7 provide a debugging capability called Eye Scan. The Eye Scan API VIs are located on the LabVIEW VI palette at FPGA Interface Software-Designed Instruments NI High-Speed Serial NI Eye Scan . You must connect the GTX2_CHANNEL register(s) on the FPGA to use Eye Scan. Ref

### Debugging Link Connections Using Eye Scan

The MGTs on the Xilinx Kintex-7 provide a debugging capability called Eye Scan. The Eye Scan API VIs are located on the LabVIEW VI palette at FPGA Interface»Software-Designed Instruments»NI High-Speed Serial»NI Eye Scan.

You must connect the GTX2_CHANNEL register(s) on the FPGA to use Eye Scan. Refer to the [Wiring the Instruction Targets](wiring-the-instruction-targets.html) section for information about connecting the GTX2_CHANNEL register. Refer to the Aurora sample project to learn how to use the Eye Scan API in an application.

National Instruments offers two versions of Eye Scan: Rectangular Eye Scan and N Point Eye Scan. Use Rectangular Eye Scan to obtain a traditional eye that sweeps the unit interval and nominal voltage. Use N Point Eye Scan to measure the Bit Error Ratio at arbitrary unit interval and nominal voltage offsets. For information about the Rectangular Eye Scan VIs and N Point Eye Scan VIs, refer to the NI  High-Speed Serial Instruments Help.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=developing-applications-for-the-high-speed-se.html language=enus -->
## TOPIC 00020: Developing Applications for the High-Speed Serial Device

- bundle_id: `high-speed-serial-instruments`
- source_path: `developing-applications-for-the-high-speed-se.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/developing-applications-for-the-high-speed-se.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This chapter provides information about how to develop applications for the high-speed serial device, including information about creating socketed CLIP and using LabVIEW.

### Developing Applications for the High-Speed Serial Device

This chapter provides information about how to develop applications for the high-speed serial device, including information about creating socketed CLIP and using LabVIEW.

- [Development Flow](development-flow.html) Refer to the following diagram for an overview of the high-speed serial development process.
- [Socketed CLIP Development](socketed-clip-development.html) This section provides steps for creating socketed CLIP for use with your application. Socketed CLIP provides the following functionality:
- [Developing with LabVIEW FPGA](developing-with-labview-fpga.html) After configuring the CLIP in VHDL, you can use LabVIEW FPGA to continue the development process. LabVIEW FPGA provides FPGA target support, configuration for clocking and routing, and interfacing with LabVIEW on your host computer for a fully integrated development experience.
- [LabVIEW and System Integration](labview-and-system-integration.html) The following sections contain information about how to integrate your high-speed serial system in the LabVIEW application development environment.

<!--NI_TOPIC bundle=high-speed-serial-instruments path=developing-with-labview-fpga.html language=enus -->
## TOPIC 00021: Developing with LabVIEW FPGA

- bundle_id: `high-speed-serial-instruments`
- source_path: `developing-with-labview-fpga.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/developing-with-labview-fpga.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: After configuring the CLIP in VHDL, you can use LabVIEW FPGA to continue the development process. LabVIEW FPGA provides FPGA target support, configuration for clocking and routing, and interfacing with LabVIEW on your host computer for a fully integrated development experience. Refer to the Related

### Developing with LabVIEW FPGA

After configuring the CLIP in VHDL, you can use LabVIEW FPGA to continue the development process. LabVIEW FPGA provides FPGA target support, configuration for clocking and routing, and interfacing with LabVIEW on your host computer for a fully integrated development experience.

Refer to the [Related Documentation](related-documentation.html) section of [About This Manual](about-this-manual.html) for a list of LabVIEW FPGA documentation that you may find helpful as you develop your application.

Parent topic:

Developing Applications for the High-Speed Serial Device

<!--NI_TOPIC bundle=high-speed-serial-instruments path=development-flow.html language=enus -->
## TOPIC 00022: Development Flow

- bundle_id: `high-speed-serial-instruments`
- source_path: `development-flow.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/development-flow.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following diagram for an overview of the high-speed serial development process. 16 High-Speed Serial Development Process If the sample project code is sufficient for your application, you do not have to modify the IP core, update the VHDL CLIP wrapper, or refresh the CLIP.

### Development Flow

Refer to the following diagram for an overview of the high-speed serial development process.

Figure 16.

[IMAGE alt='image' src='GUID-2057AEF1-D745-4E55-8D13-60A7CFAC7BA0-a5.svg']

If the sample project code is sufficient for your application, you do not have to modify the IP core, update the VHDL CLIP wrapper, or refresh the CLIP.

Parent topic:

Developing Applications for the High-Speed Serial Device

<!--NI_TOPIC bundle=high-speed-serial-instruments path=dma-streaming.html language=enus -->
## TOPIC 00023: DMA Streaming

- bundle_id: `high-speed-serial-instruments`
- source_path: `dma-streaming.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/dma-streaming.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The high-speed serial devices support both host-to-target streaming and target-to-host streaming through DMA channels that connect the host to your target. Use DMA streaming to allow the maximum throughput of data from your host application to be streamed to the target at high rates of speed. The hi

### DMA Streaming

The high-speed serial devices support both host-to-target streaming and target-to-host streaming through DMA channels that connect the host to your target. Use DMA streaming to allow the maximum throughput of data from your host application to be streamed to the target at high rates of speed.

The high-speed serial devices provide up to 32 DMA channels that can be accessed by your Host. These channels can be used in a variety of ways to meet your application’s needs. The total overall bandwidth of the module limits your DMA use, whether you use 1 DMA channel or 32.

The maximum width of a DMA channel is 256 bits. To use the full width of the DMA channel to achieve maximum throughput, you can write an array of U64 elements into the DMA FIFO and configure the FIFO for multi-element read/write (four elements per read/write) to satisfy the 256 bit width. You can also write up to 1024 bits at a time from LabVIEW FPGA, and the Ready for Input connection throttles the connection to the FIFO to prevent overflow.

Theoretically, DMA throughput is maximized and is most consistent when the DMA FIFO buffer is sized as large as possible to absorb variations in the readiness of the host memory. However, sizing the FIFO larger consumes block RAM resources on the FPGA and increases the timing pressure on the FIFO. NI recommends making the FIFO as large as you can successfully compile with, in order to sustain throughput through the PCIe bus to and from host memory. You can change the size of the FIFO by configuring the Requested Number of Elements for the FIFO in the project properties. You can validate the DMA sizing through benchmarking, and you can use VIs in the Streaming Design Library to monitor the health of a FIFO.

For more detailed information about using DMA, DMA best practices, and how to make design decisions on how to implement DMA in your application, refer to the Transferring Data Using Direct Memory Access topic of the LabVIEW FPGA Help.

Total throughput depends on the SCTL rate from the FPGA that is reading or writing the DMA channels. The data throughput is calculated by the following equation:

(*Data Width*× *Samples per Cycle*) ×*Number of DMA FIFOs* × *SCTL Clock Rate*= *Data Throughput*

Note

Note

Note

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=documenting-your-ip.html language=enus -->
## TOPIC 00024: Documenting Your IP

- bundle_id: `high-speed-serial-instruments`
- source_path: `documenting-your-ip.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/documenting-your-ip.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends documenting the behavior of your CLIP. Refer to the following guidelines for information about how to document your CLIP and how documenting your CLIP can affect the rest of your design: Document the endianness of your CLIP in order to properly interface your CLIP to the LabVIEW FPGA d

### Documenting Your IP

NI recommends documenting the behavior of your CLIP. Refer to the following guidelines for information about how to document your CLIP and how documenting your CLIP can affect the rest of your design:

- Document the endianness of your CLIP in order to properly interface your CLIP to the LabVIEW FPGA diagram. Refer to the Writing a VHDL Wrapper Around the Protocol IP Core section of this chapter for more information about how CLIP endianess affects the design process.
- Clearly define the portion of your entity interface that is facing the diagram, and which portion of your entity is facing the front panel.
- Clearly define your LED behavior.
- Document the connector signals by describing which signals are used, which signals are unused, and the manner in which the signal is used. Signal use can affect which ports are active with your IP and the behavior of cables upon insetion and removal.
- Use the DebugClks signal to determine the health of the internal clocks being sent to the IP. Define which bits of the 4-bit vector correspond to the clock being monitored.
- Document how you integrate AXI4-Lite signals with LabVIEW data types. Some AXI4-Lite signals do not integrate easily with LabVIEW data types; for example, address ports can have widths of 11, but LabVIEW only provides addresses with widths of 8, 16, 32, and 64. Additionally, the AXI4-Lite and AXI4-Stream adapters are configured for use with fixed-point I/O.
- Document how clocks are used and how they are routed in your CLIP for use with the IP. You must route clocks to the diagram for use with the single-cycle timed loop (SCTL) in LabVIEW FPGA.
- Document the address map of individual components within any AXI4-Lite interfaces.

Parent topic:

Writing a VHDL Wrapper Around the Protocol IP Core

<!--NI_TOPIC bundle=high-speed-serial-instruments path=download-reset-and-run-side-effects-in-the-la.html language=enus -->
## TOPIC 00025: Download, Reset, and Run Side Effects in the LabVIEW FPGA Host Interface

- bundle_id: `high-speed-serial-instruments`
- source_path: `download-reset-and-run-side-effects-in-the-la.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/download-reset-and-run-side-effects-in-the-la.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the high-speed serial device FPGA loads, it performs a power-on self-configuration sequence that configures various on-board hardware. This configuration occurs at the following times: At device power-up after the bitfile loads. At the first time Run is called after a new bitfile is downloaded

### Download, Reset, and Run Side Effects in the LabVIEW FPGA Host Interface

When the high-speed serial device FPGA loads, it performs a power-on self-configuration sequence that configures various on-board hardware. This configuration occurs at the following times:

- At device power-up after the bitfile loads.
- At the first time Run is called after a new bitfile is downloaded and the bitfile is not set to Run on Load.
- When Run is called after Reset. For more information about Run, Reset, and other Invoke methods, refer to the [LabVIEW FPGA Module Help](http://zone.ni.com/reference/en-XX/help/371599J-01/lvfpgahost/invoke_method/#details). Note When self-configuration executes, the clocking configuration enters an indeterminate state. When the clocking configuration is in an indeterminate state, you cannot rely on clocking stability from the clocking and routing hardware on the high-speed serial device.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=exporting-to-vivado.html language=enus -->
## TOPIC 00026: Exporting to Vivado

- bundle_id: `high-speed-serial-instruments`
- source_path: `exporting-to-vivado.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/exporting-to-vivado.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Exporting a LabVIEW FPGA VI as a Vivado project allows you to design the exported project in LabVIEW, then compile it into a bitfile in the Vivado Design Suite. You can then run the bitfile on an FPGA target in the FPGA Module. This option takes advantage of the design features provided by the Vivad

### Exporting to Vivado

Exporting a LabVIEW FPGA VI as a Vivado project allows you to design the exported project in LabVIEW, then compile it into a bitfile in the Vivado Design Suite. You can then run the bitfile on an FPGA target in the FPGA Module. This option takes advantage of the design features provided by the Vivado Design Suite while making full use of LabVIEW FPGA hardware resources. Refer to the Exporting FPGA VIs as Vivado Design Suite Projects (FPGA Module) topic in the *LabVIEW Help* for more information about this feature.

The PXIe-6591R, PXIe-6592R, and PXIe-7902 devices support exporting to Vivado. The Aurora sample projects for the PXIe-6591R, PXIe-6592R, and PXIe-7902R provide out-of-the-box support that demonstrates how to use hardware design files as an entry point when exporting to Vivado.

Complete the following steps to export a LabVIEW FPGA VI as a Vivado Design Suite project.

1. Open the Aurora Simple Streaming sample project for your hardware device. The following image shows the PXIe-6592R Aurora Simple Streaming sample project as an example. The files with the UserRTL_ prefix are used as the entry point when the top-level FPGA VI is exported to Vivado. 
 [IMAGE alt='image' src='GUID-395C53F5-4FC3-4354-AC85-6B8C53643607-a5.png']
2. In the LabVIEW project, select the Stream Controller [device name] build specification under the Build Specifications item. 
 [IMAGE alt='image' src='GUID-2041EFB6-4D9C-4B83-9AB2-3075A5CA4030-a5.png']
3. Navigate to the LabVIEW project root directory. The exported project is located inside the ProjectExportForVivado folder. The exported project contains encrypted LabVIEW FPGA files, the unencrypted design files with the UserRTL_ prefix, and the Vivado project files. 
 [IMAGE alt='image' src='GUID-361964DD-5540-4FAE-99AD-ABF01435639A-a5.png']
4. Open the Vivado project using the LaunchVivadoDesignSuite.bat file. 
 [IMAGE alt='image' src='GUID-FA93B558-67AA-4642-A051-3B5A74CA01DA-a5.png']
5. The source hierarchy loads once Vivado launches. 
 Note The hierarchy source is encrypted, except for the design files prefixed with UserRTL_ and added to the FPGA target as a socketed CLIP.
6. Navigate to the UserRTL_ files in the hierarchy. 
 [IMAGE alt='image' src='GUID-BF6452C8-0F2C-4A68-8DE8-EF18F258249B-a5.png']
7. Use the unencrypted design files as an entry point for IP you are developing in Vivado. You can compile the design from Vivado to generate a LabVIEW bitfile (.lvbitx) that can be loaded on the respective NI targets.

Parent topic:

Socketed CLIP Development

<!--NI_TOPIC bundle=high-speed-serial-instruments path=eye-scan-state-model.html language=enus -->
## TOPIC 00027: Eye Scan State Model

- bundle_id: `high-speed-serial-instruments`
- source_path: `eye-scan-state-model.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/eye-scan-state-model.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: The Eye Scan API abstracts the Eye Scan algorithm provided by Xilinx into a simple API with few states. The general programming flow is as follows: Open Session Configure Properties Start Measure Close Session. You can loop measurements for frequent updates. The following figure illustrates the Eye

### Eye Scan State Model

The Eye Scan API abstracts the Eye Scan algorithm provided by Xilinx into a simple API with few states. The general programming flow is as follows:

Open Session»Configure Properties»Start»Measure»Close Session.

Note

[IMAGE alt='image' src='GUID-9CA6DA18-DFF0-4E50-9908-FD4518C4D0D6-a5.svg']

1. Open a session with Open Session (Poly).vi.
2. Configure the properties using the Property Node, located on the NI Eye Scan VI palette (FPGA Interface»Software-Designed Instruments»NI High-Speed Serial»NI Eye Scan). Some properties have default values, but you must configure the following properties before starting the scan: 
 RX Internal Data WidthValid values are 16 bits, 20 bits, 32 bits, and 40 bits.Note The RX Internal Data Width property must be set to the Internal Data Width of the RX interface datapath. Refer to the FPGA RX Interface section of the Xilinx *7 Series FPGAs GTX/GTH Transceivers User Guide* for information about the FPGA RX interface datapath configuration.
RX Output Divider
Equalization ModeValid modes are LPM (low-power mode) and DFE (decision-feedback equalization). Refer to the Xilinx 7 Series FPGAs GTX/GTH Transceivers User Guide for more information about these modes.
3. Call Start.vi to begin measuring on the first point.
4. NI recommends calling Measure (Poly).vi with a relatively small timeout value in a loop. This allows you to receive updates to the progress of Eye Scan while measurements are still being taken, and provides updates without using a large amount of computational resources. Once Eye Scan finishes measuring the active point, it automatically reconfigures for the next point and begins measuring that point. This process continues until one of the following occurs: 
 *Number of New Points Requested*completes
*Timeout*is reached
Every requested point is scanned
5. Once the last point has been measured, Eye Scan moves to the Finished state. In the Finished state, you can call the Measure VI to retrieve all previously acquired data since the last Start call. You can also reconfigure and call Start again in order to begin a new Eye Scan. 
 Note When you call Start, all previously acquired data is discarded. To stop Eye Scan before measurement is complete, call Stop.vi. Calling this VI moves Eye Scan to the Stopped state and discards the data from the point currently being measured. Previously acquired points may no longer be obtained by calling Measure (Poly).vi. Once Eye Scan is stopped, you can reconfigure properties and call Start.vi to restart measurement.

Parent topic:

Debugging Link Connections Using Eye Scan

<!--NI_TOPIC bundle=high-speed-serial-instruments path=front-panel-6591.html language=enus -->
## TOPIC 00028: Front Panel

- bundle_id: `high-speed-serial-instruments`
- source_path: `front-panel-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/front-panel-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the pinouts for the PXIe-6591R front panel connectors. 3 PXIe-6591R Front Panel Connectors and Pinouts Refer to the following table for a list of the PXIe-6591R front panel connectors and their descriptions. 7 PXIe-6591R Front Panel Connectors Connector Type Description CL

### Front Panel

The following figure shows the pinouts for the PXIe-6591R front panel connectors.

Figure 3.

[IMAGE alt='image' src='GUID-089362C5-C4E2-4A0E-8A14-486D5FA38E64-a5.svg']

Refer to the following table for a list of the PXIe-6591R front panel connectors and their descriptions.

| Connector | Type | Description |
| --- | --- | --- |
| CLK IN/OUT | SMA | Reference Clock input and exported clock output |
| Digital Data & Control (DDC) | VHDCI | General purpose I/O |
| Port 0 | Mini-SAS HD External | High-speed serial interfacing ports |
| Port 1 |  |  |

Parent topic:

Connecting and Interfacing with the PXIe-6591R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=front-panel-6592.html language=enus -->
## TOPIC 00029: Front Panel

- bundle_id: `high-speed-serial-instruments`
- source_path: `front-panel-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/front-panel-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the pinouts for the PXIe-6592R front panel connectors. 8 PXIe-6592R Front Panel Connectors and Pinout Refer to the following table for a list of the PXIe-6592R front panel connectors and their descriptions. 14 PXIe-6592R Front Panel Connectors Connector Type Description PF

### Front Panel

The following figure shows the pinouts for the PXIe-6592R front panel connectors.

Figure 8.

[IMAGE alt='image' src='GUID-B3D11866-A8D3-441F-93ED-A6554CF3E453-a5.svg']

Refer to the following table for a list of the PXIe-6592R front panel connectors and their descriptions.

| Connector | Type | Description |
| --- | --- | --- |
| PFI 0/CLK IN/OUT | SMB | Reference Clock input, exported clock output, and general-purpose I/O. |
| PFI 1/CLK OUT |  |  |
| PFI 2/CLK OUT |  |  |
| PFI 3/CLK OUT |  |  |
| Port 0 | SFP+ | High-speed serial interfacing ports |
| Port 1 |  |  |
| Port 2 |  |  |
| Port 3 |  |  |

Parent topic:

Connecting and Interfacing with the PXIe-6592R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=front-panel-7902.html language=enus -->
## TOPIC 00030: Front Panel

- bundle_id: `high-speed-serial-instruments`
- source_path: `front-panel-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/front-panel-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the pinouts for the PXIe-7902 front panel connectors. 13 PXIe-7902 Front Panel Connectors and Pinout Refer to the following table for a list of the PXIe-7902 front panel connectors and their descriptions. 20 PXIe-7902 Front Panel Connectors Connector Type Description CLK I

### Front Panel

The following figure shows the pinouts for the PXIe-7902 front panel connectors.

Figure 13.

[IMAGE alt='image' src='GUID-C7E19126-FB0C-40D3-9D6C-C083D5595B65-a5.svg']

Refer to the following table for a list of the PXIe-7902 front panel connectors and their descriptions.

| Connector | Type | Description |
| --- | --- | --- |
| CLK IN | SMB | Reference Clock input and general-purpose I/O |
| Port 0 | Mini-SAS HD x4 | High-speed serial interfacing ports |
| Port 1 |  |  |
| Port 2 |  |  |
| Port 3 |  |  |
| Port 4 |  |  |
| Port 5 |  |  |

Parent topic:

Connecting and Interfacing with the PXIe-7902

<!--NI_TOPIC bundle=high-speed-serial-instruments path=generating-an-ip-core-from-the-xilinx-vivado.html language=enus -->
## TOPIC 00031: Generating an IP Core from the Xilinx Vivado IP Catalog

- bundle_id: `high-speed-serial-instruments`
- source_path: `generating-an-ip-core-from-the-xilinx-vivado.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/generating-an-ip-core-from-the-xilinx-vivado.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: You may need to purchase and install additional licenses to generate some protocol IP core from Xilinx or third-party IP vendors. Refer to UG 973: Vivado Design Suite: Release Notes, Installation, and Licensing at xilinx.com for information about managing licenses.Complete the following steps to cre

### Generating an IP Core from the Xilinx Vivado IP Catalog

You may need to purchase and install additional licenses to generate some protocol IP core from Xilinx or third-party IP vendors. Refer to UG 973: Vivado Design Suite: Release Notes, Installation, and Licensing at xilinx.com for information about managing licenses.

Complete the following steps to create a Xilinx Vivado project:

1. Refer to the section of Chapter[Before You Begin](before-you-begin.html#GUID-B2312619-280D-48CB-B892-41035D0D1FCB), [Before You Begin](before-you-begin.html#GUID-B2312619-280D-48CB-B892-41035D0D1FCB), for information about licensing before creating a Xilinx Vivado project.
2. Launch the Xilinx Vivado IP catalog.
  1. Select Manage IP on the Vivado start screen.
  2. Locate the appropriate IP core to launch the configuration dialog. For example, the Aurora 64B66B IP core is located in Communication and Networking»Serial Interfaces»Aurora 64B66B.
3. Select the IP core settings. NI recommends that you select AXI4-Stream for high-speed data streams when possible. 
 Note NI does not recommend selecting AXI4-Lite for DRP accesses in the Xilinx IP cores because compatibility with LabVIEW FPGA AXI4-Lite adapters cannot be guaranteed. Refer to the Aurora sample projects for an example of how to use the LabVIEW FPGA AXI4-Lite adapters to connect to DRP within the CLIP.

Parent topic:

Socketed CLIP Development

<!--NI_TOPIC bundle=high-speed-serial-instruments path=improving-performance-in-larger-designs-throu.html language=enus -->
## TOPIC 00032: Improving Performance in Larger Designs through Enable Chain Removal

- bundle_id: `high-speed-serial-instruments`
- source_path: `improving-performance-in-larger-designs-throu.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/improving-performance-in-larger-designs-throu.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, LabVIEW adds code to the FPGA code to enforce data flow. This code addition is referred to as the enable chain. In larger applications, the enable chain can create routing congestion and limit performance. You can remove the enable chain under certain circumstances. Refer to Improving Ti

### Improving Performance in Larger Designs through Enable Chain Removal

By default, LabVIEW adds code to the FPGA code to enforce data flow. This code addition is referred to as the enable chain. In larger applications, the enable chain can create routing congestion and limit performance. You can remove the enable chain under certain circumstances. Refer to Improving Timing Performance in Large Designs (FPGA Module) in the [LabVIEW FPGA Module Help](http://zone.ni.com/reference/en-XX/help/371599K-01/lvfpgaconcepts/fpga_routing_congestion/) for more information about how to remove enable chains and when to do so.

Parent topic:

Socketed CLIP Development

<!--NI_TOPIC bundle=high-speed-serial-instruments path=labview-and-system-integration.html language=enus -->
## TOPIC 00033: LabVIEW and System Integration

- bundle_id: `high-speed-serial-instruments`
- source_path: `labview-and-system-integration.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/labview-and-system-integration.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections contain information about how to integrate your high-speed serial system in the LabVIEW application development environment.

### LabVIEW and System Integration

The following sections contain information about how to integrate your high-speed serial system in the LabVIEW application development environment.

Parent topic:

Developing Applications for the High-Speed Serial Device

<!--NI_TOPIC bundle=high-speed-serial-instruments path=maximizing-peer-to-peer-streaming-throughput.html language=enus -->
## TOPIC 00034: Maximizing Peer-to-Peer Streaming Throughput

- bundle_id: `high-speed-serial-instruments`
- source_path: `maximizing-peer-to-peer-streaming-throughput.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/maximizing-peer-to-peer-streaming-throughput.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Maximum throughput is dependent on the streaming modules, chassis, and, if the configuration warrants it, the controller. Generally, the lowest of these rates is the maximum possible P2P bandwidth. High-speed serial devices are PXI Express x8 Gen 2 capable, meaning they allow theoretical 3.4 GB/s un

### Maximizing Peer-to-Peer Streaming Throughput

Maximum throughput is dependent on the streaming modules, chassis, and, if the configuration warrants it, the controller. Generally, the lowest of these rates is the maximum possible P2P bandwidth. High-speed serial devices are PXI Express x8 Gen 2 capable, meaning they allow theoretical 3.4 GB/s unidirectional streaming and theoretical 2.4 GB/s bidirectional streaming. The recommended hardware setup for getting maximum P2P streaming between NI high-speed serial instruments is to use an NI PXIe-1085 chassis with a device in slot 4 and a device in slot 6.

For example, a P2P steam that is four U64 samples wide running on the 100 MHz PXI clock can theoretically transfer data at 3.2 GB/s. When transferring data at this speed, use the handshaking interface on the P2P FIFO to implement flow control.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=modifying-third-party-ip-core-logic.html language=enus -->
## TOPIC 00035: Modifying Third-Party IP Core Logic

- bundle_id: `high-speed-serial-instruments`
- source_path: `modifying-third-party-ip-core-logic.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/modifying-third-party-ip-core-logic.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you modify a third-party IP core for your high-speed serial protocol, consult the Xilinx Product Guide for the IP you are using before attempting to make any modifications. Adhere to the following guidelines when modifying third-party IP core logic: Ensure all clocks are connected. Ensure AXI4-Li

### Modifying Third-Party IP Core Logic

If you modify a third-party IP core for your high-speed serial protocol, consult the Xilinx Product Guide for the IP you are using before attempting to make any modifications.

Adhere to the following guidelines when modifying third-party IP core logic:

- Ensure all clocks are connected.
- Ensure AXI4-Lite management signals are connected correctly to the Xilinx DRP signals on the GTXE2_CHANNEL and GTXE2_COMMON primitives.
- Select Include Shared Logic in example design in the IP wizard to access various resources outside of the IP core logic, such as MGT_RefClk input buffers and QPLL wrappers. The following examples explain the differences in how the IBUFDS_GTE2 resource is exposed with and without the Include Shared Logic in example design option.
- Option 1: Include the IBUFDS_GTE2 input buffer primitive inside the core by selecting Include Shared Logic in core in the IP wizard. The image on the left in Figure modifying-third-party-ip-core-logic.html#GUID-BB837D7C-0A41-433B-9689-4AE01DCC53BF__ID-00000A3E shows this option.
- Option 2: Instantiate a single IBUFDS_GTE2 input buffer in your top level CLIP VHDL, connect its output signal to both cores, and select Include Shared Logic in example design in the IP wizard. The image on the right in Figure modifying-third-party-ip-core-logic.html#GUID-BB837D7C-0A41-433B-9689-4AE01DCC53BF__ID-00000A3E shows this option. Note Do not modify the IP core unless you understand the required reference clock(s) and clocking resources. The following figure shows the difference between the top-level CLIP VHDL with shared logic in the core (left) and without shared logic (right). Top-Level CLIP VHDL and Shared Logic [IMAGE alt='image' src='GUID-F9B25254-F27C-41C5-B0E5-FF22C34ECE6F-a5.svg']

Parent topic:

Generating an IP Core from the Xilinx Vivado IP Catalog

<!--NI_TOPIC bundle=high-speed-serial-instruments path=monitoring-power-and-temperature.html language=enus -->
## TOPIC 00036: Monitoring Power and Temperature

- bundle_id: `high-speed-serial-instruments`
- source_path: `monitoring-power-and-temperature.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/monitoring-power-and-temperature.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Due to the degree of customization possible with the high-speed serial device FPGAs, some applications may draw too much power or dissipate too much heat. Monitor the device state carefully, especially if your device pushes the power or heat limits. Use the Read Module Temperature and Read Module Po

### Monitoring Power and Temperature

Due to the degree of customization possible with the high-speed serial device FPGAs, some applications may draw too much power or dissipate too much heat. Monitor the device state carefully, especially if your device pushes the power or heat limits. Use the Read Module Temperature and Read Module Power method nodes to monitor device temperature and heat, respectively.

Read Module Temperature allows you to read two onboard sensors: one sensor is embedded directly in the FPGA, and one reads the device temperature.

Figure 20.

[IMAGE alt='image' src='GUID-39EC870B-CA80-40AD-BA30-7D618BD69936-a5.png']

Read Module Power provides information about how much power the device is drawing from the chassis 3.3V and 12V power rails.

Figure 21.

[IMAGE alt='image' src='GUID-E0AE1E9E-16B4-4816-93CE-66D20C2A934A-a5.png']

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=n-point-eye-scan.html language=enus -->
## TOPIC 00037: N Point Eye Scan

- bundle_id: `high-speed-serial-instruments`
- source_path: `n-point-eye-scan.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/n-point-eye-scan.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following portion of code shows a typical use case for N Point Eye Scan. This code scans 4 points with a Bit Error Ratio floor of 2.33E-10 and produces a 4-point eye, which is useful for measuring pass/fail conditions. To obtain a 6-point eye, add two extra points to the array using the Array of

### N Point Eye Scan

The following portion of code shows a typical use case for N Point Eye Scan. This code scans 4 points with a Bit Error Ratio floor of 2.33E-10 and produces a 4-point eye, which is useful for measuring pass/fail conditions. To obtain a 6-point eye, add two extra points to the array using the Array of Points to Measure property.

Figure 23.

[IMAGE alt='image' src='GUID-98EF2391-B331-4CA7-BA1D-C293C0521BE8-a5.png']

The Array of Points to Measure property contains the horizontal and vertical offsets for each point that you wish to perform a Bit Error Ratio measurement on.

Parent topic:

Debugging Link Connections Using Eye Scan

<!--NI_TOPIC bundle=high-speed-serial-instruments path=peer-to-peer-streaming.html language=enus -->
## TOPIC 00038: Peer-to-Peer Streaming

- bundle_id: `high-speed-serial-instruments`
- source_path: `peer-to-peer-streaming.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/peer-to-peer-streaming.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another. Using the peer-to-peer data streaming architecture, two or more devices

### Peer-to-Peer Streaming

The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another. Using the peer-to-peer data streaming architecture, two or more devices can transfer data directly to each other without first going through the host processor.

The high-speed serial devices can stream Peer-to-Peer (P2P) data to or from any other NI-P2P capable device. For example, you can implement the writer on a digitizer using the NI-SCOPE instrument driver and implement the reader on an NI high-speed serial software-designed instrument device using LabVIEW with the LabVIEW FPGA Module.

For an overview of the P2P architecture, refer to An Introduction to Peer-to-Peer Streaming at ni.com. If you need more details on Peer-to-Peer and the P2P API, refer to the NI Peer-to-Peer Streaming Help, available at ni.com/manuals and as part of the NI High-Speed Serial Instruments Help.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=power-thermal-protection-and-shutdown.html language=enus -->
## TOPIC 00039: Power/Thermal Protection and Shutdown

- bundle_id: `high-speed-serial-instruments`
- source_path: `power-thermal-protection-and-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/power-thermal-protection-and-shutdown.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The high-speed serial devices have a fail-safe power and thermal shutdown to prevent damage to the module or other hardware in your chassis. Device shutdown can cause your host to reboot or display an error screen. In order to avoid this issue, monitor temperature and power consumption closely when

### Power/Thermal Protection and Shutdown

The high-speed serial devices have a fail-safe power and thermal shutdown to prevent damage to the module or other hardware in your chassis. Device shutdown can cause your host to reboot or display an error screen. In order to avoid this issue, monitor temperature and power consumption closely when developing custom FPGA images.

If a power and thermal shutdown occurs, power cycle the system and contact NI customer support at ni.[com/support](https://www.ni.com/support).

Parent topic:

Monitoring Power and Temperature

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxi-triggers.html language=enus -->
## TOPIC 00040: PXI Triggers

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxi-triggers.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxi-triggers.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the FPGA I/O Node to access the trigger lines on PXI devices. The following sections explain how to configure trigger pulses, reserve trigger lines, and release trigger lines.

### PXI Triggers

You can use the FPGA I/O Node to access the trigger lines on PXI devices. The following sections explain how to configure trigger pulses, reserve trigger lines, and release trigger lines.

Parent topic:

LabVIEW and System Integration

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6591r-clocking.html language=enus -->
## TOPIC 00041: PXIe-6591R Clocking

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6591r-clocking.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6591r-clocking.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6591R clocking architecture includes the following MGT Reference Clocks: MGT_RefClk0 MGT_RefClk1MGT_RefClk0 and MGT_RefClk1 are separate clocks, but are derived though simple integer division of a common, higher frequency PLL clock. Refer to the following table for information about the clo

### PXIe-6591R Clocking

The PXIe-6591R clocking architecture includes the following MGT Reference Clocks:

- MGT_RefClk0
- MGT_RefClk1 MGT_RefClk0 and MGT_RefClk1 are separate clocks, but are derived though simple integer division of a common, higher frequency PLL clock. Refer to the following table for information about the clocks’ supported frequency ranges and available sources. Table 6.PXIe-6591R Reference ClocksClock Name
Frequency Range
Available SourcesMGT_RefClk0
60 MHz to 700 MHz
Backplane: PXIe_Clk100 and PXIe_DStarAFront panel: CLK IN/OUT
MGT_RefClk1 Refer to the [Configuring the High-Speed Serial Device LabVIEW FPGA Targets](configuring-the-high-speed-serial-device-labv.html) section of Chapter[Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), [Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), for more information about how to configure Reference Clocks for your device. The following figure illustrates the clocking circuitry on the PXIe-6591R. Figure 2.PXIe-6591R Clocking Diagram [IMAGE alt='image' src='GUID-4BD580EA-85C0-42F1-8883-A3EEED571D72-a5.svg']

Parent topic:

PXIe-6591R Module Overview

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6591r-hardware-architecture.html language=enus -->
## TOPIC 00042: PXIe-6591R Hardware Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6591r-hardware-architecture.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6591r-hardware-architecture.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following chapter contains information about the PXIe-6591R clocking architecture. The PXIe-6591R is a high-speed serial interfacing module. The PXIe-6591R hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GT

### PXIe-6591R Hardware Architecture

The following chapter contains information about the PXIe-6591R clocking architecture.

The PXIe-6591R is a high-speed serial interfacing module. The PXIe-6591R hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GTX transceiver technology; you can reuse existing protocol IP that works with Xilinx GTX transceivers, or you can develop your own protocol IP. If you develop your own protocol IP, the IP must be developed for a Xilinx Kintex-7 GTX transceiver.

Note

- PXIe-6591R front panel connectors for data, clocking, and triggering external to the module
- Socketed CLIP for HDL IP and interface definition from the FPGA VI to the PXIe-6591R front panel
- Xilinx Kintex-7 FPGA
- Dynamic random access memory (DRAM)
- NI-defined bus interface from the FPGA to the host PC The following figure illustrates the key components of the PXIe-6591R architecture. Figure 1.PXIe-6591R System Architecture Elements [IMAGE alt='image' src='GUID-BB2A8E7A-0B88-4850-8934-AE057B38C592-a5.svg']

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6591r-module-overview.html language=enus -->
## TOPIC 00043: PXIe-6591R Module Overview

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6591r-module-overview.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6591r-module-overview.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6591R module includes the following key features. Refer to the PXIe-6591R Specifications for more details. 5 PXIe-6591R Key Features Line rate 500 Mb/s to 8 Gb/s and 9.8 Gb/s to 12.5 Gb/s Multi-gigabit transceiver lanes 8 (4 per port) Front Panel Connectors Two Mini-SAS HD connectors (Port

### PXIe-6591R Module Overview

The PXIe-6591R module includes the following key features. Refer to the PXIe-6591R Specifications for more details.

| Line rate | 500 Mb/s to 8 Gb/s and 9.8 Gb/s to 12.5 Gb/s |
| --- | --- |
| Multi-gigabit transceiver lanes | 8 (4 per port) |
| Front Panel Connectors | Two Mini-SAS HD connectors (Port 0 and Port 1) for high-speed serial I/OOne SMA (CLK IN/OUT) connector for external clock routingOne VHDCI (Digital Data & Control) for 20 general-purpose input/output lines |
| FPGA | Kintex-7 410T FFG900 package |
| FPGA speed grade | -3 (XC7K410T-3FFG900) |
| DRAM | 2 GB onboard DRAM166 MHz clock frequencyBit-width: 512-bit |
| Backplane connection | Gen 2x8 PXI Express, PCIe 2.0 compliant |

Parent topic:

PXIe-6591R Hardware Architecture

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6592r-clocking.html language=enus -->
## TOPIC 00044: PXIe-6592R Clocking

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6592r-clocking.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6592r-clocking.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how the PXIe‑6592R generates, distributes, and exports MGT reference clocks. Overview The PXIe-6592R clocking architecture provides three MGT reference clocks. MGT_RefClk0 Generated by dividing a higher‑frequency PLL clock. MGT_RefClk1 Generated by dividing the same PLL clock through a separat

### PXIe-6592R Clocking

Learn how the PXIe‑6592R generates, distributes, and exports MGT reference
 clocks.

#### Overview

The PXIe-6592R clocking architecture provides three
 MGT reference clocks.

MGT_RefClk0

PLL

MGT_RefClk1

PLL

MGT_RefClk2

156.25 MHz

For information about the supported frequency ranges and available sources for each
 clock, see [Table 13.PXIe-6592R Reference Clocks](pxie-6592r-clocking.html#GUID-B00B7F37-487E-490F-9D9A-473696BE456E__TABLE_YBH_RYX_F3C).

#### Reference Clock Sources

| Clock Name | Frequency Range | Backplane Sources | Front Panel Sources | Other Sources |
| --- | --- | --- | --- | --- |
| MGT_RefClk0 | 60 MHz to 670 MHz | PXIe_Clk100 PXIe_DStarA | PFI 0 CLK IN/OUT | 10 MHz Onboard Clock |
| MGT_RefClk1 | 60 MHz to 670 MHz | PXIe_Clk100 PXIe_DStarA | PFI 0 CLK IN/OUT | 10 MHz Onboard Clock |
| MGT_RefClk2 | 156.25 MHz | None | None | None |

#### Configuring Reference
 Clocks

For guidance about configuring reference clocks, see *Configuring High‑Speed
 Serial Device LabVIEW FPGA Targets*.

#### Exporting Clocks on PFI
 Connectors

- PFI 0
- PFI 1
- PFI 2
- PFI 3

When the PFI connectors export a clock, all connectors must use the same
 frequency.

For a visual representation of the clocking circuitry on the PXIe‑6592R, see [Figure 7.PXIe-6592R Clocking
 Architecture](pxie-6592r-clocking.html#GUID-B00B7F37-487E-490F-9D9A-473696BE456E__FIG_WTG_JDY_F3C).

#### Clocking Architecture
 Diagram

Figure 7.

[IMAGE alt='Diagram showing the PXIe‑6592R clocking architecture. The image illustrates PFI\u202f0–3 as front panel inputs feeding clock multiplexers, a Clock Synthesis and Routing block connected to PXIe_Clk100, PXIe_DStarA, and a 10\u202fMHz onboard clock, and the FPGA receiving MGT_RefClk0, MGT_RefClk1, and the independent 156.25\u202fMHz MGT_RefClk2.' src='GUID-95ABAF9B-99FA-42C0-906C-9E5304FADAD4-a5.svg']

Parent topic:

PXIe-6592R Module Overview

Related tasks:

- Configuring the High-Speed Serial Device LabVIEW FPGA Targets

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6592r-hardware-architecture.html language=enus -->
## TOPIC 00045: PXIe-6592R Hardware Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6592r-hardware-architecture.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6592r-hardware-architecture.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following chapter contains information about the PXIe-6592R clocking architecture. The PXIe-6592R is a high-speed serial interfacing module. The PXIe-6592R hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GT

### PXIe-6592R Hardware Architecture

The following chapter contains information about the PXIe-6592R clocking architecture.

The PXIe-6592R is a high-speed serial interfacing module. The PXIe-6592R hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GTX transceiver technology; you can reuse existing protocol IP that works with Xilinx GTX transceivers, or you can develop your own protocol IP. If you develop your own protocol IP, the IP must be developed for a Xilinx Kintex-7 GTX transceiver.

Note

- PXIe-6592R front panel connectors for data, clocking, and triggering external to the module
- Socketed CLIP for HDL IP and interface definition from the FPGA VI to the PXIe-6592R front panel
- Xilinx Kintex-7 FPGA
- Dynamic random access memory (DRAM)
- NI-defined bus interface from the FPGA to the host PC The following figure illustrates the key components of the PXIe-6592R architecture. Figure 6.PXIe-6592R System Architecture Elements [IMAGE alt='image' src='GUID-BB2A8E7A-0B88-4850-8934-AE057B38C592-a5.svg']

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-6592r-module-overview.html language=enus -->
## TOPIC 00046: PXIe-6592R Module Overview

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-6592r-module-overview.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-6592r-module-overview.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6592R modules include the following key features. Refer to the PXIe-6592R Specifications for more details. 11 PXIe-6592R Key Features Line rate 500 Mb/s to 8 Gb/s and 9.8 Gb/s to 10.3125 Gb/s serial Multi-gigabit transceiver lanes 4 (1 per port) Front Panel Connectors Four SFP+ connectors (

### PXIe-6592R Module Overview

The PXIe-6592R modules include the following key features. Refer to the PXIe-6592R Specifications for more details.

| Line rate | 500 Mb/s to 8 Gb/s and 9.8 Gb/s to 10.3125 Gb/s serial |
| --- | --- |
| Multi-gigabit transceiver lanes | 4 (1 per port) |
| Front Panel Connectors | Four SFP+ connectors (Port 0, Port 1, Port 2, and Port 3) for high-speed serialFour SMB connectors (PFI 0/CLK IN/OUT, PFI 1/CLK OUT, PFI 2/CLK OUT, and PFI 3/CLK OUT) for external triggering and clock input/output |
| FPGA | Kintex-7 410T FFG900 package |
| FPGA speed grade | -2 (XC7K410T-2FFG900) |
| DRAM | 2 GB onboard DRAM166 MHz clock frequencyBit-width: 512-bit |
| Backplane connection | Gen 2x8 PXI Express, PCIe 2.0 compliant |

Parent topic:

PXIe-6592R Hardware Architecture

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-7902-clocking.html language=enus -->
## TOPIC 00047: PXIe-7902 Clocking

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-7902-clocking.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-7902-clocking.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-7902 clocking architecture includes the following MGT Reference Clocks: MGT_RefClk0 MGT_RefClk1 MGT_RefClk2MGT_RefClk0, MGT_RefClk1, and MGT_RefClk2 are separate clocks, but are derived though simple integer division of a common, higher frequency PLL clock. Refer to the following table for

### PXIe-7902 Clocking

The PXIe-7902 clocking architecture includes the following MGT Reference Clocks:

- MGT_RefClk0
- MGT_RefClk1
- MGT_RefClk2 MGT_RefClk0, MGT_RefClk1, and MGT_RefClk2 are separate clocks, but are derived though simple integer division of a common, higher frequency PLL clock. Refer to the following table for information about the clocks’ supported frequency ranges and available sources. Table 19.PXIe-7902 Reference ClocksClock Name
Frequency Range
Available SourcesMGT_RefClk0MGT_RefClk1MGT_RefClk2
60 MHz to 670 MHz156.25 MHz
Backplane: PXIe_Clk100 and PXIe_DStarAFront panel: CLK INOther: 10 MHz Onboard Clock— Refer to the [Configuring the High-Speed Serial Device LabVIEW FPGA Targets](configuring-the-high-speed-serial-device-labv.html) section of Chapter[Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), [Developing Applications for the High-Speed Serial Device](developing-applications-for-the-high-speed-se.html), for more information about how to configure Reference Clocks for your device. The following figure illustrates the clocking circuitry on the PXIe-7902. Figure 12.PXIe-7902 Clocking Diagram [IMAGE alt='image' src='GUID-5890F70F-A0EA-4AFE-A562-7FC0E5A262FA-a5.svg']

Parent topic:

PXIe-7902 Module Overview

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-7902-hardware-architecture.html language=enus -->
## TOPIC 00048: PXIe-7902 Hardware Architecture

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-7902-hardware-architecture.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-7902-hardware-architecture.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following chapter contains information about the PXIe-7902 clocking architecture. The PXIe-7902 is a high-speed serial interfacing module. The PXIe-7902 hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GTX t

### PXIe-7902 Hardware Architecture

The following chapter contains information about the PXIe-7902 clocking architecture.

The PXIe-7902 is a high-speed serial interfacing module. The PXIe-7902 hardware architecture allows you to fully customize your serial digital protocol application. The high-speed serial interface uses Xilinx GTX transceiver technology; you can reuse existing protocol IP that works with Xilinx GTX transceivers, or you can develop your own protocol IP. If you develop your own protocol IP, the IP must be developed for a Xilinx Virtex-7 GTX transceiver.

Note

- PXIe-7902 front panel connectors for data, clocking, and triggering external to the module
- Socketed CLIP for HDL IP and interface definition from the FPGA VI to the PXIe-7902 front panel
- Xilinx Virtex-7 FPGA
- Dynamic random access memory (DRAM)
- NI-defined bus interface from the FPGA to the host PC The following figure illustrates the key components of the PXIe-7902 architecture. Figure 11.PXIe-7902 System Architecture Elements [IMAGE alt='image' src='GUID-59B0CB3C-BFC0-4C42-B999-81EA1DDD560D-a5.svg']

<!--NI_TOPIC bundle=high-speed-serial-instruments path=pxie-7902-module-overview.html language=enus -->
## TOPIC 00049: PXIe-7902 Module Overview

- bundle_id: `high-speed-serial-instruments`
- source_path: `pxie-7902-module-overview.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/pxie-7902-module-overview.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-7902 modules include the following key features. Refer to the PXIe-7902 Specifications for more details. 18 PXIe-7902 Key Features Line rate 500 Mb/s to 8 Gb/s, and 9.8 Gb/s to 12.5 Gb/s serial Multi-gigabit transceiver lanes 24 (4 per port) Front Panel Connectors Six mini-SAS x4 connectors

### PXIe-7902 Module Overview

The PXIe-7902 modules include the following key features. Refer to the PXIe-7902 Specifications for more details.

| Line rate | 500 Mb/s to 8 Gb/s, and 9.8 Gb/s to 12.5 Gb/s serial |
| --- | --- |
| Multi-gigabit transceiver lanes | 24 (4 per port) |
| Front Panel Connectors | Six mini-SAS x4 connectors (Port 0, Port 1, Port 2, Port 3, Port 4, and Port 5) for high-speed serialOne SMB connector (CLK IN) for clock input |
| FPGA | Xilinx Virtex-7 485T FFG1158 package |
| FPGA speed grade | -3 (XC7VX485T-3FFG1158E) |
| DRAM | 2 GB onboard DRAM166 MHz clock frequencyBit-width: 512-bit |
| Backplane connection | Gen 2x8 PXI Express, PCIe 2.0 compliant |

Parent topic:

PXIe-7902 Hardware Architecture

<!--NI_TOPIC bundle=high-speed-serial-instruments path=recommended-mating-cables-and-connectors-6591.html language=enus -->
## TOPIC 00050: Recommended Mating Cables and Connectors

- bundle_id: `high-speed-serial-instruments`
- source_path: `recommended-mating-cables-and-connectors-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/recommended-mating-cables-and-connectors-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the PXIe-6591R product listing page for a list of mating cables to use with your PXIe-6591R.

### Recommended Mating Cables and Connectors

Refer to the PXIe-6591R [product listing page](http://sine.ni.com/nips/cds/view/p/lang/en/nid/212694) for a list of mating cables to use with your PXIe-6591R.

Parent topic:

Connecting and Interfacing with the PXIe-6591R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=recommended-mating-cables-and-connectors-6592.html language=enus -->
## TOPIC 00051: Recommended Mating Cables and Connectors

- bundle_id: `high-speed-serial-instruments`
- source_path: `recommended-mating-cables-and-connectors-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/recommended-mating-cables-and-connectors-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the PXIe-6592R product listing page for a list of mating cables to use with your PXIe-6592R.

### Recommended Mating Cables and Connectors

Refer to the PXIe-6592R [product listing page](http://sine.ni.com/nips/cds/view/p/lang/en/nid/212696) for a list of mating cables to use with your PXIe-6592R.

Parent topic:

Connecting and Interfacing with the PXIe-6592R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=recommended-mating-cables-and-connectors-7902.html language=enus -->
## TOPIC 00052: Recommended Mating Cables and Connectors

- bundle_id: `high-speed-serial-instruments`
- source_path: `recommended-mating-cables-and-connectors-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/recommended-mating-cables-and-connectors-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the PXIe-7902 product listing page for a list of mating cables to use with your PXIe-7902.

### Recommended Mating Cables and Connectors

Refer to the PXIe-7902 [product listing page](http://www.ni.com/en-us/support/model.pxie-7902.html) for a list of mating cables to use with your PXIe-7902.

Parent topic:

Connecting and Interfacing with the PXIe-7902

<!--NI_TOPIC bundle=high-speed-serial-instruments path=rectangular-eye-scan.html language=enus -->
## TOPIC 00053: Rectangular Eye Scan

- bundle_id: `high-speed-serial-instruments`
- source_path: `rectangular-eye-scan.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/rectangular-eye-scan.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following portion of code shows a typical use case for Rectangular Eye Scan. This code measures a single channel and updates the Bit Error Ratio graph once per 100 milliseconds. 22 Rectangular Eye Scan Use the Horizontal Step Size and Vertical Step Size properties to control the density of your

### Rectangular Eye Scan

The following portion of code shows a typical use case for Rectangular Eye Scan. This code measures a single channel and updates the Bit Error Ratio graph once per 100 milliseconds.

Figure 22.

[IMAGE alt='image' src='GUID-D6DDF34A-7F56-4DE7-99BC-C6076FA3831C-a5.png']

Use the Horizontal Step Size and Vertical Step Size properties to control the density of your Eye Scan plot. The points to be measured are computed based on step size starting from 0, up to the largest absolute value closest to, but not exceeding, the maximum value.

Parent topic:

Debugging Link Connections Using Eye Scan

<!--NI_TOPIC bundle=high-speed-serial-instruments path=related-documentation.html language=enus -->
## TOPIC 00054: Related Documentation

- bundle_id: `high-speed-serial-instruments`
- source_path: `related-documentation.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/related-documentation.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following documents contain information that you may find helpful as you read this manual. 1 Documentation Locations and Descriptions Document Location Description NI PXIe-6591R Specifications Available from the Start menu and at ni.com/ manuals. Contains specifications for your PXIe-6591R modul

### Related Documentation

The following documents contain information that you may find helpful as you read this manual.

| Document | Location | Description |  |
| --- | --- | --- | --- |
| NI PXIe-6591R Specifications | Available from the Start menu and at ni.com/ manuals. | Contains specifications for your PXIe-6591R module. |  |
| NI PXIe-6592R Specifications | Available from the Start menu and at ni.com/ manuals. | Contains specifications for your PXIe-6592R module. |  |
| PXIe-7902 Specifications | Available from the Start menu and at ni.com/ manuals. | Contains specifications for your PXIe-7902 module. |  |
| PXIe-6591R Getting Started Guide | Available from the Start menu and at ni.com/ manuals. | Contains installation instructions for your system. |  |
| PXIe-6592R Getting Started Guide | Available from the Start menu and at ni.com/ manuals. | Contains installation instructions for your system. |  |
| PXIe-7902 Getting Started Guide | Available from the Start menu and at ni.com/ manuals. | Contains installation instructions for your system. |  |
| NI High-Speed Serial Instruments Help | Available from the Start menu and at ni.com/ manuals. | Contains information about how to add FPGA I/O to your project, and how to configure your high-speed serial device with VIs. |  |
| LabVIEW FPGA documentation | NI LabVIEW High- Performance FPGA Developer’s Guide | Available at ni.com/ tutorial. | Summarizes the most effective techniques for optimizing throughput, latency, and FPGA resources when using the LabVIEW FPGA Module and the NI RIO hardware platform. |
| FPGA Module Help | This document is a book within the LabVIEW Help. Access this document by navigating to Start » All Programs » National Instruments » LabVIEW » LabVIEW Help, or by searching for FPGA Module Help at ni.com/manuals. Browse to the FPGA Module book in the Contents tab for information about using the LabVIEW FPGA Module. | With the LabVIEW FPGA Module and LabVIEW, you can create VIs that run on National Instruments FPGA targets.The Getting Started with the LabVIEW FPGA book provides links to the top resources that you can use to get started with LabVIEW FPGA.The Integrating Third-Party IP (FPGA Module) book contains information about adding custom HDL code to your LabVIEW project. |  |
| LabVIEW FPGA Module Release and Upgrade Notes | Available at ni.com/ manuals. You can also view this document by selecting Start » All Programs » National Instruments » LabVIEW » LabVIEW Manuals. | Contains information about installing the LabVIEW FPGA Module, describes new features, and provides upgrade information. |  |

#### Xilinx Documentation

Xilinx FPGA
 documentation provides information required for the successful development of your
 high-speed serial device. The following table provides a list of specific Xilinx
 documentation resources.

Xilinx documentation is available at www.[xilinx.com](https://www.xilinx.com).

| Document | Document Part Number | Description |
| --- | --- | --- |
| 7 Series FPGAs Overview | DS180 | Outlines the features and product selection of the Xilinx 7 series FPGAs: Artix-7, Kintex-7, and Virtex-7 devices. |
| Kintex-7 FPGAs Data Sheet: DC and AC Switching Characteristics | DS182 | Contains the DC and AC switching characteristic specifications for the Kintex-7 FPGAs. |
| Vivado Design Suite: Release Notes, Installation, and Licensing | UG973 | Provides an overview of the new release of the Vivado Design Suite, including information on new and changed features, installation requirements for the software, and licensing information. |
| High-Speed Serial I/O Made Simple: A Designer’s Guide, with FPGA Applications | — | Recommended for users new to high-speed serial. |
| 7 Series FPGAs GTX/GTH Transceivers User Guide | UG476 | Technical reference describing the 7 series FPGAs GTX/GTH transceivers. |
| Vivado Design Suite User Guide: Using Constraints | UG903 | Describes using Xilinx Design Constraints (XDC) in Vivado tools. |

#### Additional Resources

The
 software-designed instruments webpage, located at ni.[com/ software-designed-instruments](https://www.ni.com/software-designed-instruments), contains product information, white
 papers, and videos to help you develop applications.

Parent topic:

About This Manual

<!--NI_TOPIC bundle=high-speed-serial-instruments path=releasing-trigger-lines.html language=enus -->
## TOPIC 00055: Releasing Trigger Lines

- bundle_id: `high-speed-serial-instruments`
- source_path: `releasing-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/releasing-trigger-lines.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to release a trigger line for your device. LabVIEW automatically releases the trigger reservation when you close the FPGA VI Reference, but you can use an invoke node if you want to unreserve the trigger without closing the FPGA VI Reference. Place the Open FPGA VI Refer

### Releasing Trigger Lines

Complete the following steps to release a trigger line for your device.

Note

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Unreserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant. An enum constant is created to help you select the trigger. 
 To release multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to release, wiring the FPGA VI Reference Out output of the existing Invoke Method function to the FPGA VI Reference In input of the Invoke Method node that follows it.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=reserving-pxi-triggers.html language=enus -->
## TOPIC 00056: Reserving PXI Triggers

- bundle_id: `high-speed-serial-instruments`
- source_path: `reserving-pxi-triggers.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/reserving-pxi-triggers.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments recommends that you reserve the trigger lines used by PXI devices, including the high-speed serial device. If two PXI devices try to drive the same trigger line in different applications, or if the PXI devices are not programmed to work together, the application does not work, a

### Reserving PXI Triggers

National Instruments recommends that you reserve the trigger lines used by PXI devices, including the high-speed serial device. If two PXI devices try to drive the same trigger line in different applications, or if the PXI devices are not programmed to work together, the application does not work, and in some cases, third-party PXI devices can be damaged. You can use Measurement & Automation Explorer (MAX) or the LabVIEW FPGA Host VI to reserve trigger lines.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=reserving-trigger-lines-in-max.html language=enus -->
## TOPIC 00057: Reserving Trigger Lines in MAX

- bundle_id: `high-speed-serial-instruments`
- source_path: `reserving-trigger-lines-in-max.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/reserving-trigger-lines-in-max.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you download and run the FPGA VI interactively, configure the PXI triggers in MAX. MAX maintains the trigger reservation for the device even after you cycle power to the PXI chassis.

### Reserving Trigger Lines in MAX

If you download and run the FPGA VI interactively, configure the PXI triggers in MAX. MAX maintains the trigger reservation for the device even after you cycle power to the PXI chassis.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=reserving-trigger-lines-in-the-labview-fpga-h.html language=enus -->
## TOPIC 00058: Reserving Trigger Lines in the LabVIEW FPGA Host VI

- bundle_id: `high-speed-serial-instruments`
- source_path: `reserving-trigger-lines-in-the-labview-fpga-h.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/reserving-trigger-lines-in-the-labview-fpga-h.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you download and run the FPGA VI programmatically, reserve the trigger lines in the host VI. Use the Invoke Method function to reserve the trigger and to release the trigger reservation. LabVIEW releases the trigger reservation for the device automatically when you close the FPGA VI reference. Yo

### Reserving Trigger Lines in the LabVIEW FPGA Host VI

If you download and run the FPGA VI programmatically, reserve the trigger lines in the host VI. Use the Invoke Method function to reserve the trigger and to release the trigger reservation. LabVIEW releases the trigger reservation for the device automatically when you close the FPGA VI reference. You must run the host VI again to reserve the trigger.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=reserving-trigger-lines.html language=enus -->
## TOPIC 00059: Reserving Trigger Lines

- bundle_id: `high-speed-serial-instruments`
- source_path: `reserving-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/reserving-trigger-lines.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to reserve a trigger line for a PXI device. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI. Place the Invoke Method function on the block diagram. Wire the FPGA VI Reference Out output of the Open FPGA VI R

### Reserving Trigger Lines

Complete the following steps to reserve a trigger line for a PXI device.

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Reserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant. An enum constant is created to help you select the trigger. 
 To reserve multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to reserve, wiring the FPGA VI Reference Out output of the existing Invoke Method function to the FPGA VI Reference In input of the Invoke Method node that follows it.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=high-speed-serial-instruments path=signal-routing-6591.html language=enus -->
## TOPIC 00060: Signal Routing

- bundle_id: `high-speed-serial-instruments`
- source_path: `signal-routing-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/signal-routing-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6591R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0 and PORT 1 connector pins using a 100 nF AC-coupling capacitor, as shown in the following figure. 4 PXIe-6591R Signal Routing

### Signal Routing

The PXIe-6591R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0 and PORT 1 connector pins using a 100 nF AC-coupling capacitor, as shown in the following figure.

Figure 4.

[IMAGE alt='image' src='GUID-C9CE551E-DB07-47C8-9DD5-A2ABC343F866-a5.svg']

Parent topic:

Connecting and Interfacing with the PXIe-6591R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=signal-routing-6592.html language=enus -->
## TOPIC 00061: Signal Routing

- bundle_id: `high-speed-serial-instruments`
- source_path: `signal-routing-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/signal-routing-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-6592R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, and PORT 3 connector pins, as shown in the following figure. 9 PXIe-6592R Signal Routing

### Signal Routing

The PXIe-6592R high-speed serial differential signals are routed directly from the Kintex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, and PORT 3 connector pins, as shown in the following figure.

Figure 9.

[IMAGE alt='image' src='GUID-19B8EA49-EA35-4DE8-AAD7-8C3C1DBAD070-a5.svg']

Parent topic:

Connecting and Interfacing with the PXIe-6592R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=signal-routing-7902.html language=enus -->
## TOPIC 00062: Signal Routing

- bundle_id: `high-speed-serial-instruments`
- source_path: `signal-routing-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/signal-routing-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXIe-7902 high-speed serial differential signals are routed directly from the Virtex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, PORT 3, PORT 4, and PORT 5 connector pins, as shown in the following figure. This signal routing is replicated for every lane across every port. 14 PXIe-7902 Signal Rou

### Signal Routing

The PXIe-7902 high-speed serial differential signals are routed directly from the Virtex-7 FPGA pins to the PORT 0, PORT 1, PORT 2, PORT 3, PORT 4, and PORT 5 connector pins, as shown in the following figure. This signal routing is replicated for every lane across every port.

Figure 14.

[IMAGE alt='image' src='GUID-F4FF6D11-2AF4-4CA3-9F7B-B2017BB7E343-a5.svg']

Parent topic:

Connecting and Interfacing with the PXIe-7902

<!--NI_TOPIC bundle=high-speed-serial-instruments path=socketed-clip-development.html language=enus -->
## TOPIC 00063: Socketed CLIP Development

- bundle_id: `high-speed-serial-instruments`
- source_path: `socketed-clip-development.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/socketed-clip-development.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides steps for creating socketed CLIP for use with your application. Socketed CLIP provides the following functionality: Allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Allows the CLIP to communicate directly with circuitr

### Socketed CLIP Development

This section provides steps for creating socketed CLIP for use with your application. Socketed CLIP provides the following functionality:

- Allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI.
- Allows the CLIP to communicate directly with circuitry external to the FPGA.
- Allows your IP to communicate directly with both the FPGA VI and the external FPGA module connector interface. You can develop socketed CLIP either by using the Xilinx Vivado tools, or by exporting a LabVIEW FPGA VI as a Vivado Design Suite project.
- The Xilinx Vivado tools create a blank project, from which you can develop socketed CLIP. For more information about using the Xilinx Vivado tools to develop socketed CLIP, refer to the Accessing the Xilinx Vivado Tools section.
- You can also design your project in LabVIEW, then export the project to the Vivado Design Suite. For more information about exporting a LabVIEW FPGA VI as a Vivado Design Suite project, refer to the Exporting to Vivado section.

Parent topic:

Developing Applications for the High-Speed Serial Device

<!--NI_TOPIC bundle=high-speed-serial-instruments path=socketed-clip-interface-6591.html language=enus -->
## TOPIC 00064: Socketed CLIP Interface

- bundle_id: `high-speed-serial-instruments`
- source_path: `socketed-clip-interface-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/socketed-clip-interface-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA. The following sections provide information about how to configure your device for

### Socketed CLIP Interface

Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

The following sections provide information about how to configure your device for use with socketed CLIP.

Parent topic:

Connecting and Interfacing with the PXIe-6591R

#### PXIe-6591R Socketed CLIP

Refer to the following diagram for an overview of the PXIe-6591R socketed CLIP interface.

Figure 5.

[IMAGE alt='image' src='GUID-402AE916-BDAB-4A4B-BE2A-E4B0A7BE2F04-a5.svg']

Refer to the following table for a list of the PXIe-6591R socketed CLIP signals.

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| MGT_RefClk0_p | In (pad) | N/A | Differential input clock that you must connect to an IBUFDS_GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk0_n | In (pad) | N/A |  |
| MGT_RefClk1_p | In (pad) | N/A |  |
| MGT_RefClk1_n | In (pad) | N/A |  |
| MGT_RefClks_ ExtPllLocked | In | Async | Indicates the state of the PLL within the clocking logic that provides the Reference Clock to the FPGA MGTs (MGT_ RefClkx signals).Use this signal with MGT_ RefClks_Valid to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals. |
| MGT_RefClks_Valid | In | Async | Indicates if the selected clock input to the clocking logic is valid and the PLL within the clocking logic has locked.Use this signal to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals.On the rising edge of MGT_ RefClks_Valid, you may need to reset or relock state machines and/or internal PLLs sensitive to MGT_RefClkx signals. |
| DebugClks(3:0) | Out | Clock | Debug ports to aid in debugging the clocking connections in the CLIP. These ports connect to frequency counters that can monitor the frequency of any clock that you connect to these ports.Refer to the Debugging Clocks Using Frequency Counters section of ChapterDeveloping Applications for the High-Speed Serial Device, Developing Applications for the High-Speed Serial Device, for details about how to use these signals. |
| ExportedUser ReferenceClk | Out | Clock | Reserved for future use. |
| LED_ActiveRed | Out | Async | The front panel Active indicator’s red LED turns on when this signal is driven high.The CLIP’s access to this LED may be temporarily overridden to show error conditions, temperature faults, and power faults.This signal is conditioned with the pulse stretcher to guarantee a minimum assertion time of 100 ms to comply with PXI guidelines and to facilitate visual perception. You can drive this signal asynchronously if you provide a 50 ns minimum assertion time. You can also drive this signal synchronously for a minimum 1 cycle of SocketClk40. |
| LED_ActiveGreen | Out | Async | The front panel Active indicator’s green LED turns on when this signal is driven high.The CLIP’s access to this LED may be temporarily overridden to show error conditions, temperature faults, and power faults.This signal is conditioned with the pulse stretcher to guarantee a minimum assertion time of 100 ms to comply with PXI guidelines and to facilitate visual perception. You can drive this signal asynchronously if you provide a 50 ns minimum assertion time. You can also drive this signal synchronously for a minimum 1 cycle of SocketClk40. |
| SocketClk40 | In | Clock | A 40 MHz clock that runs continuously regardless of connectivity. This signal is connected to the 40 MHz Onboard Clock signal, which is the default top-level clock for the LabVIEW FPGA VI. |
| sFrontEndConfiguration Done | In | SocketClk40 | Asserts high and stays high when the power-on self-configuration (POSC) state machine is finished with configuration.After the aResetSl signal transitions from high to low, indicating that the CLIP logic should come out of reset, a POSC reconfiguration occurs unconditionally.The required clocking signals are not valid until after this signal asserts high. |
| sFrontEndConfiguration Prepare | In | SocketClk40 | Reserved for future use. NI recommends assigning this signal to sFrontEnd ConfigurationReady. |
| sFrontEndConfiguration Ready | Out | SocketClk40 | Reserved for future use. NI recommends assigning sFrontEndConfiguration Prepare to this signal. |
| aResetSl | In | Async | This signal is not required.This signal is an asynchronous reset signal from the LabVIEW FPGA environment. If you create an input signal to your CLIP and assign it as Reset in the CLIP wizard, that signal is driven as an asynchronous reset signal. Reset all CLIP state machines and logic whenever this signal is logic high.This signal is driven high when you call the LabVIEW FPGA Reset invoke method. Call Run on the FPGA VI to deassert this signal.Do not use CLIP inputs from the LabVIEW FPGA VI in the CLIP until aResetSl is deasserted. |
| Port<0..1>_RX_p(3:0) | In (pad) | N/A | Dedicated MGT receive signals for Port <0..1>. |
| Port<0..1>_RX_n(3:0) | In (pad) | N/A |  |
| Port<0..1>_TX_p(3:0) | Out (pad) | N/A | Dedicated MGT transmit signals for Port <0..1>. |
| Port<0..1>_TX_n(3:0) | Out (pad) | N/A |  |
| Port<0..1>_SCL | In/Out | Async | Bidirectional serial clock signal for the two-wire communication interface on the Port <0..1> connector.Valid values: 0 and Z (open drain).This signal is also called MODDEF1.This signal has a 5 kΩ pull up to +3.3V. |
| Port<0..1>_SDA | In/Out | Async | Bidirectional serial data signal for the two-wire communication interface on the Port <0..1> connector.Valid values: 0 and Z (open drain).This signal is also called MODDEF2.This signal has a 5 kΩ pull up to +3.3V. |
| Port<0..1>_GPIO_In | In | Async | Active low presence detect signal from pin B2 on the cable connector. You must tie GPIO_OutEnable_n to “1” in order to allow this functionality. This input is driven low by the high-speed connector while it is inserted into the module. |
| Port<0..1>_GPIO_Out | Out | Async | This signal is unused. |
| Port<0..1>_GPIO_ OutEnable_n | Out | Async | You must tie this signal to “1” to disable output and allow the B2 pin to function as a presence detect signal. |
| sPort<0..1>_ EnablePower | Out | SocketClk40 | Enables or disables the power supply to the cable on Port <0..1>.This signal is active high. |
| sPort<0..1>_Power Good | In | SocketClk40 | Indicates that the power supply to the cable for Port <0..1> is enabled.This signal may deassert if an over-power condition is detected. |
| DDC_GPIO_In(19:0) | In | Async | These signals are GPIO inputs within the DDC VHDCI connector.These signals, along with DDC_GPIO_Out(19:0) and DDC_GPIO_OutEnable_ n(19:0), allow control and monitoring of the DIO(19:0) connections on the DDC_ VHDCI connector. |
| DDC_GPIO_Out(19:0) | Out | Async | These signals are GPIO outputs within the DDC VHDCI connector.These signals, along with DDC_GPIO_In(19:0) and DDC_GPIO_OutEnable_ n(19:0), allow control and monitoring of the DIO(19:0) connections on the DDC_ VHDCI connector. |
| DDC_GPIO_OutEnable_ n(19:0) | Out | Async | These signals enable GPIO_Out within the DDC VHDCI connector.Drive these signals low to enable output.These signals, along with DDC_GPIO_In(19:0) and DDC_GPIO_Out(19:0), allow control and monitoring of the DIO(19:0) connections on the DDC_VHDCI connector. |

<!--NI_TOPIC bundle=high-speed-serial-instruments path=socketed-clip-interface-6592.html language=enus -->
## TOPIC 00065: Socketed CLIP Interface

- bundle_id: `high-speed-serial-instruments`
- source_path: `socketed-clip-interface-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/socketed-clip-interface-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA. The following sections provide information about how to configure your device for

### Socketed CLIP Interface

Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

The following sections provide information about how to configure your device for use with socketed CLIP.

Parent topic:

Connecting and Interfacing with the PXIe-6592R

#### PXIe-6592R Socketed CLIP

Refer to the following diagram for an overview of the PXIe-6592R socketed CLIP interface.

Figure 10.

[IMAGE alt='image' src='GUID-53A79A0C-6BDF-47CF-9331-A8EC0A075547-a5.svg']

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| MGT_RefClk0_p | In (pad) | N/A | Differential input clock that you must connect to an IBUFDS_GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk0_n | In (pad) | N/A |  |
| MGT_RefClk1_p | In (pad) | N/A |  |
| MGT_RefClk1_n | In (pad) | N/A |  |
| MGT_RefClk2_p | In (pad) | N/A | Fixed 156.25 MHz Reference Clock for the transceivers that you must connect to an IBUFDS_GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk2_n | In (pad) | N/A |  |
| MGT_RefClks_ ExtPllLocked | In | Async | Indicates the state of the PLL within the clocking logic and provides the Reference Clock to the FPGA MGTs (MGT_ RefClkx signals).Use this signal with MGT_ RefClks_Valid to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals. |
| MGT_RefClks_ Valid | In | Async | Indicates if the selected clock input to the clocking logic is valid and the PLL within the clocking logic has locked.Use this signal to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals.On the rising edge of MGT_ RefClks_Valid, you may need to reset or relock state machines and/or internal PLLs sensitive to MGT_RefClkx signals. |
| DebugClks(3:0) | Out | Clock | Debug ports to aid in debugging the clocking connections in the CLIP. These ports connect to frequency counters that can monitor the frequency of any clock that you connect to these ports.Refer to the Debugging Clocks Using Frequency Counters section of ChapterDeveloping Applications for the High-Speed Serial Device, Developing Applications for the High-Speed Serial Device, for details about how to use these signals. |
| ExportedUser ReferenceClk | Out | Clock | Reserved for future use. |
| LED_ActiveRed | Out | Async | The front panel Active indicator’s red LED turns on when this signal is driven high.The CLIP’s access to this LED may be temporarily overridden to show error conditions, temperature faults, and power faults.This signal is conditioned with the pulse stretcher to guarantee a minimum assertion time of 100 ms to comply with PXI guidelines and to facilitate visual perception. You can drive this signal asynchronously if you provide a 50 ns minimum assertion time. You can also drive this signal synchronously for a minimum 1 cycle of SocketClk40. |
| LED_ActiveGreen | Out | Async | The front panel Active indicator’s green LED turns on when this signal is driven high.The CLIP’s access to this LED may be temporarily overridden to show error conditions, temperature faults, and power faults.This signal is conditioned with the pulse stretcher to guarantee a minimum assertion time of 100 ms to comply with PXI guidelines and to facilitate visual perception. You can drive this signal asynchronously if you provide a 50 ns minimum assertion time. You can also drive this signal synchronously for a minimum 1 cycle of SocketClk40. |
| SocketClk40 | In | Clock | A 40 MHz clock that runs continuously regardless of connectivity. This signal is connected to the 40 MHz Onboard Clock signal, which is the default top-level clock for the LabVIEW FPGA VI. |
| sFrontEnd ConfigurationDone | In | SocketClk40 | Asserts high and stays high when the power-on self-configuration (POSC) state machine is finished with configuration.After the aResetSl signal transitions from high to low, indicating that the CLIP logic should come out of reset, a POSC reconfiguration occurs unconditionally.The required clocking signals are not valid until after this signal asserts high. |
| sFrontEnd ConfigurationPrepare | In | SocketClk40 | Reserved for future use. NI recommends assigning this signal to sFront EndConfigurationReady. |
| sFrontEnd ConfigurationReady | Out | SocketClk40 | Reserved for future use. NI recommends assigning this signal to sFront EndConfigurationPrepare. |
| aResetSl | In | Async | This signal is not required.This signal is an asynchronous reset signal from the LabVIEW FPGA environment. If you create an input signal to your CLIP and assign it as Reset in the CLIP wizard, that signal is driven as an asynchronous reset signal. Reset all CLIP state machines and logic whenever this signal is logic high.This signal is driven high when you call the LabVIEW FPGA Reset invoke method. Call Run on the FPGA VI to deassert this signal.Do not use CLIP inputs from the LabVIEW FPGA VI in the CLIP until aResetSl is deasserted. |
| Port<0..3>_RX_p | In (pad) | N/A | Dedicated MGT receive signals for Port <0..3>. |
| Port<0..3>_RX_n | In (pad) | N/A |  |
| Port<0..3>_TX_p | Out (pad) | N/A | Dedicated MGT transmit signals for Port <0..3>. |
| Port<0..3>_TX_n | Out (pad) | N/A |  |
| Port<0..3>_Mod_ ABS | In | Async | This signal is asserted when the module for Port <0..3> is absent.This signal is also called MODDEF0.This signal is grounded when a module is connected to indicate that the module is present.This signal is pulled asserted when no module is present. |
| Port<0..3>_RS0 | Out | Async | Drives the Port <0..3> SFP+ module’s RX rate select signal.If this signal’s RX rate is more than 4.25 Gbps, drive this signal high. If this signal’s RX rate is 4.25 Gbps or less, drive this signal low. |
| Port<0..3>_RS1 | Out | Async | Drives the Port <0..3> SFP+ module’s TX rate select signal.If this signal’s TX rate is more than 4.25 Gbps, drive this signal high. If this signal’s TX rate is 4.25 Gbps or less, drive this signal low. |
| Port<0..3>_Rx_LOS | In | Async | This signal is driven by the Port <0..3> SFP+ module to indicate that the SFP+ module cannot detect an RX signal. |
| Port<0..3>_Tx_Disable | Out | Async | Drives the Port <0..3> SFP+ module’s Tx_Disable signal.Driving this signal high disables the transmitter for the respective port. |
| Port<0..3>_Tx_Fault | In | Async | This signal is driven by the Port <0..3> SFP+ module to indicate a TX fault.This signal indicates that the module laser is operating incorrectly. |
| Port<0..3>_SCL | In/Out | Async | Bidirectional serial clock signal for the two wire communication interface on the Port<0..3> connector.Valid values are 0 and Z (open drain).This signal is also called MODDEF1.This signal has a 10 kΩ pull up to +3.3V.You must assert sPort<0..3>_ EnablePower to enable the Port<0..3>_SCL and Port<0..3>_SDA interface. |
| Port<0..3>_SDA | In/Out | Async | Bidirectional serial data signal for the two wire communication interface on the Port<0..3> connector.Valid values are 0 and Z (open drain).This signal is also called MODDEF2.This signal has a 10 kΩ pull up to +3.3V.You must assert sPort<0..3>_ EnablePower to enable the Port<0..3>_SCL and Port<0..3>_SDA interface. |
| sPort<0..3>_Enable Power | Out | SocketClk40 | Enables or disables the optical power supply on Port <0..3>.Assert this signal to enable the optical supply for its corresponding port. |
| sPort<0..3>_Power Good | In | SocketClk40 | Indicates that the optical power supply for Port <0..3> is enabled.This signal may deassert if an over-power condition occurs. |
| PFI<0..3>_GPIO_In | In | Async | Acquires GPIO input from the PFI<0..3> connectors. |
| PFI<0..3>_GPIO_Out | Out | Async | Drives the GPIO output data to the PFI<0..3> connectors. |
| PFI<0..3>_GPIO_ OutEnable_n | Out | Async | Enables or disables the GPIO output driver on PFI<0..3>.This signal is active low. |

<!--NI_TOPIC bundle=high-speed-serial-instruments path=socketed-clip-interface-7902.html language=enus -->
## TOPIC 00066: Socketed CLIP Interface

- bundle_id: `high-speed-serial-instruments`
- source_path: `socketed-clip-interface-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/socketed-clip-interface-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA. The following sections provide information about how to configure your device for

### Socketed CLIP Interface

Socketed CLIP allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI. Socketed CLIP also allows the CLIP to communicate directly with circuitry external to the FPGA.

The following sections provide information about how to configure your device for use with socketed CLIP.

Parent topic:

Connecting and Interfacing with the PXIe-7902

#### PXIe-7902 Socketed CLIP

Refer to the following diagram for an overview of the PXIe-7902 socketed CLIP interface.

Figure 15.

[IMAGE alt='image' src='GUID-43FD5A38-C206-4FAE-BB05-B97402605B84-a5.svg']

The following signals are provided through the PXIe-7902 CLIP socket. You can use these signals to develop your own custom CLIP. For more information about how to configure the PXIe-7902 CLIP, refer to the *NI High-Speed Serial Instruments Help*.

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| MGT_RefClk2_p | In (pad) | N/A | Differential input clock that you must connect to an IBUFDS_ GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk2_n | In (pad) | N/A |  |
| MGT_RefClk3_p | In (pad) | N/A | Differential input clock that you must connect to an IBUFDS_ GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk3_n | In (pad) | N/A |  |
| MGT_RefClk4_p | In (pad) | N/A | Differential input clock that you must connect to an IBUFDS_ GTE2 input buffer primitive when this input clock is used in your design. |
| MGT_RefClk4_n | In (pad) | N/A |  |
| Port<0..5>_RX_p | In (pad) | N/A | Dedicated MGT receive signals for Port <0..5>. |
| Port<0..5>_RX_n | In (pad) | N/A |  |
| Port<0..5>_TX_p | Out (pad) | N/A | Dedicated MGT transmit signals for Port <0..5>. |
| Port<0..5>_TX_n | Out (pad) | N/A |  |
| GtxRxPolarity_in | In (pad) |  | 24-bit signal that indicates the polarity of the receive signal.Some MGT signals have inverted polarity external to the FPGA; use this signal to determine which channels, if any, are inverted. |
| GtxTxPolarity_in | In (pad) |  | 24-bit signal that indicates the polarity of the transmit signal.Some MGT signals have inverted polarity external to the FPGA; use this signal to determine which channels, if any, are inverted. |
| SocketClk40 | In | Clock | A 40 MHz clock that runs continuously regardless of connectivity. This signal is connected to the 40 MHz Onboard Clock signal, which is the default top-level clock for the LabVIEW FPGA VI. |
| Port<0..5>_SCL | In/Out | Async | Bidirectional serial clock signal for the two wire communication interface on the Port<0..5> connector.Valid values are 0 and Z (open drain).This signal is also called MODDEF1.This signal has a 10 kOhm pull up to +3.3V.You must assert aPort<_EnablePower to enable the Port<0..5>_SCL and Port<0..5>_SDA interface. |
| Port<0..5>_SDA | In/Out | Async | Bidirectional serial data signal for the two wire communication interface on the Port<0..3> connector.Valid values are 0 and Z (open drain).This signal is also called MODDEF2.This signal has a 10 kOhm pull up to +3.3V.You must assert aPort_EnablePower to enable the Port<0..5>_SCL and Port<0..5>_SDA interface. |
| Port<0..5>_ModPrs_n | In (pad) |  | Indicates the presence of a device on the other end of the cable for each port. |
| MGT_RefClks_ ExtPllLocked | In | Async | Indicates the state of the PLL within the clocking logic and provides the Reference Clock to the FPGA MGTs (MGT_ RefClkx signals).Use this signal with MGT_ RefClks_Valid to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals. |
| MGT_RefClks_ Valid | In | Async | Indicates if the selected clock input to the clocking logic is valid and the PLL within the clocking logic has locked.Use this signal to gate and/or reset the clocking signals into any CLIP that depends on the MGT_RefClkx signals.On the rising edge of MGT_ RefClks_Valid, you may need to reset or relock state machines and/or internal PLLs sensitive to MGT_RefClkx signals. |
| DebugClks(5:0) | Out | Clock | Debug ports to aid in debugging the clocking connections in the CLIP. These ports connect to frequency counters that can monitor the frequency of any clock that you connect to these ports.Refer to the Debugging Link Connections Using Eye Scan section of ChapterDeveloping Applications for the High-Speed Serial Device, Developing Applications for the High-Speed Serial Device, for details about how to use these signals. |
| ExportedUser ReferenceClk | Out | Clock | Reserved for future use. |
| sFrontEnd ConfigurationDone | In | SocketClk40 | Asserts high and stays high when the power-on self-configuration (POSC) state machine is finished with configuration.After the aResetSl signal transitions from high to low, indicating that the CLIP logic should come out of reset, a POSC reconfiguration occurs unconditionally.The required clocking signals are not valid until after this signal asserts high. |
| sFrontEnd ConfigurationPrepare | In | SocketClk40 | Reserved for future use. NI recommends assigning this signal to sFront EndConfigurationReady. |
| sFrontEnd ConfigurationReady | Out | SocketClk40 | Reserved for future use. NI recommends assigning this signal to sFront EndConfigurationPrepare. |
| aPort_Enable Power | Out | SocketClk40 | Enables or disables the power supply on Port <0..5>.Assert this signal to enable the power supply for its corresponding port.You can leave this signal disabled when using copper cables. This signal is required when using optical cables. |
| aPort_Power Good | In | SocketClk40 | Indicates that the power supply for Port <0..5> is enabled.This signal may deassert if an over-power condition occurs. |
| aOptical_Enable Power | Out | SocketClk40 | Enables or disables the optical power supply on Port <0..5>.Assert this signal to enable the optical supply for its corresponding port. |
| aOptical_Power Good | In | SocketClk40 | Indicates that the optical power supply for Port <0..5> is enabled.This signal may deassert if an over-power condition occurs. |

<!--NI_TOPIC bundle=high-speed-serial-instruments path=soft-shutdown.html language=enus -->
## TOPIC 00067: Soft Shutdown

- bundle_id: `high-speed-serial-instruments`
- source_path: `soft-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/soft-shutdown.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Exceeding the soft thermal and power threshold puts your device in a safe state and provides a warning. The errors -63170 or -63171 indicate that the device has gone into a soft shutdown. To recover from this error, power cycle the board. In order to avoid seeing this error again, improve the airflo

### Soft Shutdown

Exceeding the soft thermal and power threshold puts your device in a safe state and provides a warning. The errors -63170 or -63171 indicate that the device has gone into a soft shutdown. To recover from this error, power cycle the board. In order to avoid seeing this error again, improve the airflow to your chassis or consider reduced FPGA logic.

Parent topic:

Monitoring Power and Temperature

<!--NI_TOPIC bundle=high-speed-serial-instruments path=transceiver-lane-and-quad-mapping-6591.html language=enus -->
## TOPIC 00068: Transceiver Lane and Quad Mapping

- bundle_id: `high-speed-serial-instruments`
- source_path: `transceiver-lane-and-quad-mapping-6591.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/transceiver-lane-and-quad-mapping-6591.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your application requires multiple lanes, refer to Table 1 and Table 2 for information about transceiver and RefClk selection when using the Xilinx tools to generate protocol IP. 8 Transceiver Lane and Quad Mapping Connector Lane Quad Location Physical Resource PORT 0 0 Quad 3 (Q3) GTX_X0Y13 1 GT

### Transceiver Lane and Quad Mapping

If your application requires multiple lanes, refer to Table 1 and Table 2 for information about transceiver and RefClk selection when using the Xilinx tools to generate protocol IP.

| Connector | Lane | Quad Location | Physical Resource |
| --- | --- | --- | --- |
| PORT 0 | 0 | Quad 3 (Q3) | GTX_X0Y13 |
| 1 | GTX_X0Y15 |  |  |
| 2 | GTX_X0Y14 |  |  |
| 3 | GTX_X0Y12 |  |  |
| PORT 1 | 0 | Quad 2 (Q2) | GTX_X0Y10 |
| 1 | GTX_X0Y11 |  |  |
| 2 | GTX_X0Y9 |  |  |
| 3 | GTX_X0Y8 |  |  |

| Clock Signal | Quad Location | Physical Resource |
| --- | --- | --- |
| MGT_RefClk0 | Quad 3 (Q3) | REFCLK1_Q3 |
| MGT_RefClk1 | Quad 2 (Q2) | REFCLK0_Q2 |

For more information about lane and channel bonding caveats, refer to the 7 Series FPGAs GTX/GTH Transceivers User Guide (UG476) at xilinx.com.

Note

Parent topic:

Connecting and Interfacing with the PXIe-6591R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=transceiver-lane-and-quad-mapping-6592.html language=enus -->
## TOPIC 00069: Transceiver Lane and Quad Mapping

- bundle_id: `high-speed-serial-instruments`
- source_path: `transceiver-lane-and-quad-mapping-6592.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/transceiver-lane-and-quad-mapping-6592.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your application requires multiple lanes, refer to Table 1 and Table 2 for information about transceiver and RefClk selection when using the Xilinx tools to generate protocol IP. 15 Transceiver Lane and Quad Mapping Connector Lane Quad Location Physical Resource PORT 0 0 Quad 3 (Q3) GTX_X0Y15 POR

### Transceiver Lane and Quad Mapping

If your application requires multiple lanes, refer to Table 1 and Table 2 for information about transceiver and RefClk selection when using the Xilinx tools to generate protocol IP.

| Connector | Lane | Quad Location | Physical Resource |
| --- | --- | --- | --- |
| PORT 0 | 0 | Quad 3 (Q3) | GTX_X0Y15 |
| PORT 1 | 0 | GTX_X0Y13 |  |
| PORT 2 | 0 | Quad 2 (Q2) | GTX_X0Y10 |
| PORT 3 | 0 | GTX_X0Y8 |  |

| Clock Signal | Quad Location | Physical Resource |
| --- | --- | --- |
| MGT_RefClk0 | Quad 3 (Q3) | REFCLK1_Q3 |
| MGT_RefClk1 | Quad 2 (Q2) | REFCLK0_Q2 |
| MGT_RefClk2 | Quad 3 (Q3) | REFCLK0_Q3 |

For more information about lane and channel bonding caveats, including cases where you need to use single or multiple reference clocks for single or multiple transceivers, refer to 7 Series FPGAs GTX/GTH Transceivers User Guide (UG476) at xilinx.com.

Parent topic:

Connecting and Interfacing with the PXIe-6592R

<!--NI_TOPIC bundle=high-speed-serial-instruments path=transceiver-lane-and-quad-mapping-7902.html language=enus -->
## TOPIC 00070: Transceiver Lane and Quad Mapping

- bundle_id: `high-speed-serial-instruments`
- source_path: `transceiver-lane-and-quad-mapping-7902.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/transceiver-lane-and-quad-mapping-7902.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your application requires multiple lanes, refer to the following tables for information about transceiver and RefClk selection when using the Xilinx tools to generate protocol IP. 21 Transceiver Lane and Quad Mapping Connector Lane Quad Location Physical Resource PORT 0 0 Quad 0 (Q0) GTX_X0Y5 1 G

### Transceiver Lane and Quad Mapping

If your application requires multiple lanes, refer to the following tables for information about
 transceiver and RefClk selection when using the Xilinx tools to generate protocol
 IP.

| Connector | Lane | Quad Location | Physical Resource |
| --- | --- | --- | --- |
| PORT 0 | 0 | Quad 0 (Q0) | GTX_X0Y5 |
| 1 | GTX_X0Y4 |  |  |
| 2 | GTX_X0Y6 |  |  |
| 3 | GTX_X0Y7 |  |  |
| PORT 1 | 0 | Quad 1 (Q1) | GTX_X0Y9 |
| 1 | GTX_X0Y8 |  |  |
| 2 | GTX_X0Y10 |  |  |
| 3 | GTX_X0Y11 |  |  |
| PORT 2 | 0 | Quad 2 (Q2) | GTX_X0Y13 |
| 1 | GTX_X0Y12 |  |  |
| 2 | GTX_X0Y14 |  |  |
| 3 | GTX_X0Y15 |  |  |
| PORT 3 | 0 | Quad 3 (Q3) | GTX_X0Y17 |
| 1 | GTX_X0Y16 |  |  |
| 2 | GTX_X0Y18 |  |  |
| 3 | GTX_X0Y19 |  |  |
| PORT 4 | 0 | Quad 4 (Q4) | GTX_X0Y21 |
| 1 | GTX_X0Y20 |  |  |
| 2 | GTX_X0Y22 |  |  |
| 3 | GTX_X0Y23 |  |  |
| PORT 5 | 0 | Quad 5 (Q5) | GTX_X0Y25 |
| 1 | GTX_X0Y24 |  |  |
| 2 | GTX_X0Y26 |  |  |
| 3 | GTX_X0Y27 |  |  |

| Clock Signal | Quad Location | Physical Resource |
| --- | --- | --- |
| MGT_RefClk2 | Quad 1 (Q1) | REFCLK1_Q1 |
| MGT_RefClk3 | Quad 3 (Q3) | REFCLK1_Q3 |
| MGT_RefClk4 | Quad 5 (Q5) | REFCLK1_Q5 |

For more information about lane and channel bonding caveats, including cases where you need to
 use single or multiple reference clocks for single or multiple transceivers, refer to
 *7 Series FPGAs GTX/GTH Transceivers User Guide (UG476)* at
 xilinx.com.

Parent topic:

Connecting and Interfacing with the PXIe-7902

<!--NI_TOPIC bundle=high-speed-serial-instruments path=troubleshooting.html language=enus -->
## TOPIC 00071: Troubleshooting

- bundle_id: `high-speed-serial-instruments`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/troubleshooting.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: To learn how to generate and integrate Aurora IP into your LabVIEW project, see Generating and Integrating Aurora IP into Your LabVIEW Project.

### Troubleshooting

To learn how to generate and integrate Aurora IP into your LabVIEW project, see [Generating and Integrating Aurora IP into Your
 LabVIEW Project](http://digital.ni.com/public.nsf/allkb/723FE910AF2D01A686257D89007702C4).

<!--NI_TOPIC bundle=high-speed-serial-instruments path=user-manual-welcome.html language=enus -->
## TOPIC 00072: NI High-Speed Serial Instruments User Manual

- bundle_id: `high-speed-serial-instruments`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/user-manual-welcome.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI High-Speed Serial Instruments User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Info

### NI High-Speed Serial
 Instruments
 User Manual

The NI High-Speed Serial
 Instruments User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- PXIe-6591 Specifications
- PXIe-6591 Getting Started
- PXIe-6592 Specifications
- PXIe-6592 Getting Started
- PXIe-7902 Specifications
- PXIe-7902 Getting Started
- An Introduction to PXI High-Speed Serial Instruments
- The NI LabVIEW High-Performance FPGA Developer’s Guide
- Software and Driver Downloads
- Release Notes
- License Setup and Activation
- Dimensional Drawings
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-existing-vhdl-ip-inside-clip-or-ipin.html language=enus -->
## TOPIC 00073: Using Existing VHDL IP Inside CLIP or IPIN

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-existing-vhdl-ip-inside-clip-or-ipin.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-existing-vhdl-ip-inside-clip-or-ipin.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use existing IP in your project, refer to Importing External IP Into LabVIEW FPGA in the Related Information section. CLIP does not support custom user libraries in the VHDL. If your VHDL uses custom user libraries, use one of the following workarounds: Create a netlist from the VHDL and integrat

### Using Existing VHDL IP Inside CLIP or
 IPIN

To use existing IP in your project, refer to *Importing External IP Into LabVIEW FPGA*
 in the *Related Information* section.

CLIP does not support custom user libraries in the VHDL. If your VHDL uses custom user libraries, use one of the following workarounds:

- Create a netlist from the VHDL and integrate the netlist using CLIP.
- Reference the default reference library instead of a custom user library. Refer to the Creating or Acquiring IP (FPGA Module) topic in the LabVIEW FPGA Module Help for more information about using existing VHDL IP inside CLIP or IPIN.

Parent topic:

Developing with LabVIEW FPGA

Related information:

- Importing External IP Into LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-basic-elements.html language=enus -->
## TOPIC 00074: Using niInstr Basic Elements

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-basic-elements.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-basic-elements.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Basic Elements Instrument Design Library contains VIs that perform common FPGA functions, such as detecting rising and falling edges, storing Boolean values, and data handshaking. Using this library can be beneficial when developing new FPGA logic for your instrument.

### Using niInstr Basic Elements

The Basic Elements Instrument Design Library contains VIs that perform common FPGA functions, such as detecting rising and falling edges, storing Boolean values, and data handshaking. Using this library can be beneficial when developing new FPGA logic for your instrument.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-clip-adapters.html language=enus -->
## TOPIC 00075: Using niInstr CLIP Adapters

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-clip-adapters.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-clip-adapters.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. Refer to the Connecting AXI4-Lite and AXI4-Stream Interfaces to the Host section of this chapter for more information about how to use the CLIP Adapters instrument design library.

### Using niInstr CLIP Adapters

The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. Refer to the [Connecting AXI4-Lite and AXI4-Stream Interfaces to the Host](connecting-axi4-lite-and-axi4-stream-interfac.html) section of this chapter for more information about how to use the CLIP Adapters instrument design library.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-data-trigger.html language=enus -->
## TOPIC 00076: Using niInstr Data Trigger

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-data-trigger.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-data-trigger.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Data Trigger Instrument Design Library VIs to generate a trigger when the input data sample is more than or less than the configured value. This library supports multiple trigger types. For more information on supported triggers and their use, refer to the LabVIEW context help for the Data T

### Using niInstr Data Trigger

Use the Data Trigger Instrument Design Library VIs to generate a trigger when the input data sample is more than or less than the configured value.

This library supports multiple trigger types. For more information on supported triggers and their use, refer to the LabVIEW context help for the Data Trigger VIs.

This library supports various data types and samples per cycle.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-eye-scan.html language=enus -->
## TOPIC 00077: Using niInstr Eye Scan

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-eye-scan.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-eye-scan.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the Connecting Signals to Enable Eye Scan and Debugging Link Connections Using Eye Scan sections of this chapter for information about using the Eye Scan instrument design library.

### Using niInstr Eye Scan

Refer to the [Connecting Signals to Enable Eye Scan](connecting-signals-to-enable-eye-scan.html) and [Debugging Link Connections Using Eye Scan](debugging-link-connections-using-eye-scan.html) sections of this chapter for information about using the Eye Scan instrument design library.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-instruction-framework.html language=enus -->
## TOPIC 00078: Using niInstr Instruction Framework

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-instruction-framework.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-instruction-framework.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When t

### Using niInstr Instruction Framework

Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When the destination Address Space completes an instruction, it provides a response which is routed back to the Instruction Producer that issued the instruction, as shown in the following diagram.

Figure 18.

[IMAGE alt='image' src='GUID-0E287778-F877-418F-9A18-D5ED87A8EB56-a5.svg']

The Instruction Framework instrument design library includes some host VIs to help with communication between host libraries and FPGA address spaces. The Subsystem Map class provides a way to look up the location of an Address Space on the host, using the Address Space’s unique identifier (UID). A context object is returned from this lookup function, which can be used to specify the destination for a read or write operation.

Use the Instruction Target class as an abstract interface for the mechanism used to communicate with the Instruction Framework FPGA Network. The FIFO Register Bus instrument design library provides an Instruction Target implementation on the host, which is coupled to an Instruction Producer implementation on the FPGA. This allows a host controller to send instructions to Address Spaces on the FPGA, and read the resulting responses. The instructions are sent to the FPGA using a uniquely named DMA FIFO, and the responses are received using a uniquely named indicator.

Some instrument design libraries use the Instruction Framework as a configuration mechanism. These libraries require a Subsystem Map object to look-up the location of corresponding Address Spaces on the FPGA. These libraries will also require an Instruction Target to provide the communication mechanism from the host controller to an Instruction Producer on the Instruction Framework FPGA Network. The corresponding Address Spaces must be added to the Instruction Framework FPGA Network in order for the host library to communicate properly with the FPGA library. This Address Space implementation provides register access through an Instruction Producer, such as the FIFO Register Bus library, instead of using controls and indicators on the top level of the FPGA diagram.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-niinstr-streaming.html language=enus -->
## TOPIC 00079: Using niInstr Streaming

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-niinstr-streaming.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-niinstr-streaming.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA. Refer to the Aurora Simple Streaming sample project for an example of how to use t

### Using niInstr Streaming

The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA.

Refer to the Aurora Simple Streaming sample project for an example of how to use the Streaming Instrument Design Library.

Parent topic:

Using the NI Common Instrument Design Libraries

<!--NI_TOPIC bundle=high-speed-serial-instruments path=using-the-ni-common-instrument-design-librari.html language=enus -->
## TOPIC 00080: Using the NI Common Instrument Design Libraries

- bundle_id: `high-speed-serial-instruments`
- source_path: `using-the-ni-common-instrument-design-librari.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/using-the-ni-common-instrument-design-librari.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Instrument design libraries can speed up your application development. The instrument design libraries are located at <LVDir>\instr.lib\_niInstr. In LabVIEW, the common instrument design libraries are located on the niHighSpeedSerial Host palette at FPGA Interface Software-Defined Instruments HSS Ho

### Using the NI Common Instrument Design Libraries

Instrument design libraries can speed up your application development. The instrument design libraries are located at <LVDir>\instr.lib\_niInstr.

In LabVIEW, the common instrument design libraries are located on the niHighSpeedSerial Host palette at FPGA Interface»Software-Defined Instruments»HSS Host.

In LabVIEW FPGA, the common instrument design libraries are located on the <Target Name> palette.

The following sections provide an overview of the instrument design libraries. For more information about the instrument design libraries, refer to the NI High-Speed Serial Instruments Help.

Parent topic:

Developing with LabVIEW FPGA

<!--NI_TOPIC bundle=high-speed-serial-instruments path=wiring-the-instruction-targets.html language=enus -->
## TOPIC 00081: Wiring the Instruction Targets

- bundle_id: `high-speed-serial-instruments`
- source_path: `wiring-the-instruction-targets.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/wiring-the-instruction-targets.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to wire the instruction targets shown in Figures22 Rectangular Eye Scan and23 N Point Eye Scan. Eye Scan uses the GTX2_CHANNEL UID with UID 1206 as a child context of the top-level UID. In the high-speed serial sample projects, the GTX2_CHANNEL UID is nested under the to

### Wiring the Instruction Targets

Complete the following steps to wire the instruction targets shown in Figures[Figure 22.Rectangular Eye Scan](rectangular-eye-scan.html#GUID-8C9D42D4-0F2D-48FC-BAC7-85D8DC392F20__ID-FIG-00000030) and[Figure 23.N Point Eye Scan](n-point-eye-scan.html#GUID-8350C719-966B-48D9-BB5F-227F62A0CDF3__ID-FIG-00000032).

Note

1. Create a FIFO Register Bus.
  1. Place niInstr FIFO Register Bus v1 Host.lvclass:Open Session.vi on the block diagram.
  2. Wire the fpga ref input parameter to the FPGA Reference obtained from Open FPGA VI Reference.
2. Retrieve the list of subsystems by connecting the session out parameter from niInstr FIFO Register Bus v1 Host.lvclass:Open Session.vi to the input of niInstr Subsystem Map v1 Host.lvclass:Read Subsystem Map.vi. This retrieves information related to all subsystems, address spaces, and the routing context for each address space.
3. Connect the subsystem map output to niInstr Subsystem Map v1 Host.lvclass: Subsystem Lookup.vi. Specify the UID (Unique Identifier) for the top-level UID that has GTX2_CHANNEL as a child UID. By default, this is the same UID as that of the NI-provided CLIP. If you registered Eye Scan to a different top-level UID, use that UID instead.
4. Connect the instruction target from niInstr Subsystem Map v1 Host.lvclass:Read Subsystem Map.vi to the instruction target input terminal of niHighSpeedSerialEyeScan v1 Host.lvclass:Open Session.vi, and the context from niInstr Subsystem Map v1 Host.lvclass:Subsystem Lookup.vi to the parent context terminal of niHighSpeedSerialEyeScan v1 Host.lvclass:Open Session.vi.

Parent topic:

N Point Eye Scan

<!--NI_TOPIC bundle=high-speed-serial-instruments path=writing-a-vhdl-wrapper-around-the-protocol-ip.html language=enus -->
## TOPIC 00082: Writing a VHDL Wrapper Around the Protocol IP Core

- bundle_id: `high-speed-serial-instruments`
- source_path: `writing-a-vhdl-wrapper-around-the-protocol-ip.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/writing-a-vhdl-wrapper-around-the-protocol-ip.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: A VHDL wrapper is generally necessary to adapt the protocol signals to the dataflow semantics used within the LabVIEW FPGA diagram. NI recommends that you adhere to the following guidelines when writing a VHDL wrapper around the protocol IP core: Keep the interface between the CLIP and the LabVIEW F

### Writing a VHDL Wrapper Around the Protocol IP Core

A VHDL wrapper is generally necessary to adapt the protocol signals to the dataflow semantics used within the LabVIEW FPGA diagram. NI recommends that you adhere to the following guidelines when writing a VHDL wrapper around the protocol IP core:

- Keep the interface between the CLIP and the LabVIEW FPGA diagram as simple as possible. Note LabVIEW stores values in big-endian format, and your IP may accept only little-endian format. NI recommends performing any conversions in the CLIP and keeping endian conversions off the LabVIEW diagram for ease of use.
- Do not pass asynchronous signals to the LabVIEW FPGA diagram. Register the signals in a clock domain in the VHDL logic before passing them to the LabVIEW FPGA diagram.
- Use AXI4-Stream and AXI4-Lite interfaces for streaming data and register accesses. NI provides AXI4-Stream and AXI4-Lite wrappers to use on the LabVIEW FPGA diagram. Refer to the Generating an IP Core from the Xilinx Vivado IP Catalog section of this chapter for more information about IP core logic.
- If you expose an AXI4-Lite endpoint, use Xilinx AXI4 interconnect IP to expose only one AXI4-Lite endpoint to the LabVIEW FPGA diagram.
- Document the frequency of clocks coming from CLIP. Consider supporting enable chain removal. Refer to the Improving Performance in Larger Designs through Enable Chain Removal section of this chapter for more information about how to enable chain removal.
- Implement a state machine that allows asynchronous resets. If you declare an input signal as a reset signal in the CLIP wizard, then that signal is asserted when the LabVIEW FPGA VI is not running.
- Implement a state machine that resets the protocol cores when the PORT# module is absent if your state machine does not already account for this.
- Connect various clocks from your CLIP to the DebugClks std_logic_vector in order to use host-side frequency counter debugging utilities.
- Provide timing constraints in XDC for your CLIP. Include timing constraints for clocks within your CLIP, but do not include pin/location constraints on MGTs transceiver lanes and RefClks. Refer to UG 903: Vivado Design Suite User Guide: Using Constraints at xilinx.com for more information about timing constraints in XDC for your CLIP.
- Use the TXOUTCLK and/or RXOUTCLK clock constraints for your high-speed serial CLIP if your protocol uses it directly.
- The following is an example syntax for the constraint: create_clock -period <period in ns> [get_pins %ClipInstancePath%/<path to your clock pin relative to the top level CLIP VHDL>].
- If you generate an asynchronous reset within your CLIP VHDL, create a false path constraint from the register that generates the reset signal. Include a “don’t touch” attribute for any false path constraints.
- The following is an example syntax for the “don’t touch” attribute: attribute dont_touch : string; attribute dont_touch of <signal name> : signal is "true";
- The following is an example syntax for the false path constraint: set_false_path -from [get_cells %ClipInstancePath%/<path to your register>]
- When writing constraints, you may need to refer to the CLIP’s instance name or the absolute path to the CLIP instance in the VHDL hierarchy. Refer to the Constraints and Hierarchy section of this chapter for more information about using the search-and-replace keywords %ClipInstanceName% and %ClipInstancePath%.

Parent topic:

Socketed CLIP Development

<!--NI_TOPIC bundle=high-speed-serial-instruments path=xilinx-documentation-references.html language=enus -->
## TOPIC 00083: Xilinx Documentation References

- bundle_id: `high-speed-serial-instruments`
- source_path: `xilinx-documentation-references.html`
- source_url: https://docs-be.ni.com/bundle/high-speed-serial-instruments/raw/resource/enus/xilinx-documentation-references.html
- document_id: `high-speed-serial-instruments`
- page_type: `leaf`
- content_type: `concept`
- source_description: Xilinx FPGA documentation provides information required for the successful development of your high-speed serial device. The following table provides a list of specific Xilinx documentation resources. All Xilinx documentation can be found at www.xilinx.com. 3 Xilinx 7-Series FPGA Documentation Docum

### Xilinx Documentation References

Xilinx FPGA documentation provides information required for the successful development of your high-speed serial device. The following table provides a list of specific Xilinx documentation resources.

All Xilinx documentation can be found at www.xilinx.com.

| Document | Document Part Number | Description |
| --- | --- | --- |
| 7 Series FPGAs Overview | DS180 | Outlines the features and product selection of the Xilinx 7 series FPGAs, including Kintex-7 devices. |
| Kintex-7 FPGAs Data Sheet: DC and AC Switching Characteristics | DS182 | Contains the DC and AC switching characteristic specifications for the Kintex-7 FPGAs. |
| Vivado Design Suite: Release Notes, Installation, and Licensing | UG973 | Provides an overview of the new release of the Vivado Design Suite, including information on new and changed features, installation requirements for the software, and licensing information. |
| High-Speed Serial I/O Made Simple: A Designer’s Guide, with FPGA Applications | — | Recommended for users new to high-speed serial. |
| 7 Series FPGAs GTX/GTH Transceivers User Guide | UG476 | Technical reference describing the 7 series FPGAs GTX/GTH transceivers. |
| Vivado Design Suite User Guide: Using Constraints | UG903 | Describes using Xilinx Design Constraints (XDC) in Vivado tools. |

Parent topic:

About This Manual
