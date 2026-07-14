# NI DOCUMENT BUNDLE: develop-flexrio-high-speed-serial-protocols

<!--NI_BUNDLE_CHUNK bundle=develop-flexrio-high-speed-serial-protocols start=1 end=7 -->
<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=adding-target-io.html language=enus -->
## TOPIC 00001: Adding High-Speed Serial Instrument Target I/O and Accessing Instantiated CLIP Signals on the Block Diagram

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `adding-target-io.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/adding-target-io.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `task`
- source_description: Place an FPGA I/O node on the FPGA target block diagram. The FPGA I/O node is located on the palette under Functions»FPGA I/O»FPGA I/O Node. Right-click the FPGA I/O node and select Add New FPGA I/O. In the New FPGA I/O dialog box, select resources under Available Resources and add them to New FPGA

Adding High-Speed Serial Instrument Target I/O
 and Accessing Instantiated CLIP Signals on the Block Diagram

1. Place an FPGA I/O node on the FPGA target block diagram. The FPGA I/O node is located on the palette under Functions»FPGA I/O»FPGA I/O Node.
2. Right-click the FPGA I/O node and select Add New FPGA I/O.
3. In theNew FPGA I/O dialog box, select resources under Available Resources and add them to New FPGA I/O using the right arrow button.
4. To remove a resource, select the resource under New FPGA I/O and click the left arrow button.
5. Click OK.

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=apply-constraints.html language=enus -->
## TOPIC 00002: Applying Constraints Using %ClipInstanceName% and %ClipInstancePath%

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `apply-constraints.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/apply-constraints.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `task`
- source_description: You can include all CLIP-specific user constraints, except pin placement constraints, in the constraints file (.xdc) you will add to your LabVIEW project.Complete the following steps to apply constraints on specific components within your CLIP without specifying the location of the component in the

Applying Constraints Using %ClipInstanceName%
 and %ClipInstancePath%

Complete the following steps to apply constraints on
 specific components within your CLIP without specifying the location of the
 component in the VHDL hierarchy.

1. In a text file, preface your constraints with the following macros: 
 create_clock -period 10.000 -name %ClipInstanceName%Clk -waveform {0.000 5.000} -add [get_pins %ClipInstancePath%/clk]
 set_clock_latency -clock [get_clocks {%ClipInstanceName%CLK}] 10.0 [get_pins {%ClipInstancePath%/cAddOut[0]}]
2. Save the file as DemoClipAdder.xdc.
3. Add the DemoClipAdder.xdc constraints file and the VHD
 file as synthesis files in the Configure CLIP wizard. 
 org.dita.html5/xsl/topic.xsl 455Note When using these macros, you do not need to include a separate constraints
 file for each CLIP instance because the LabVIEW FPGA Module will create a
 unique name for each instance.
 org.dita.html5/xsl/topic.xsl 455Note The Xilinx compilation tools may remove an unused CLIP signal from the
 bitstream. If you get an NGBuild error during compilation, remove the
 constraint or use the signal in an FPGA VI.

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=export-to-vivado.html language=enus -->
## TOPIC 00003: Customizing High-Speed Serial IP by Exporting to Vivado

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `export-to-vivado.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/export-to-vivado.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, you must install the necessary Xilinx compilations tool for Vivado on the local computer to export an FPGA VI as a Vivado Design Suite project or open the exported project. If you choose to implement an Aurora Streaming project without customization, you will not need to export to

Customizing High-Speed Serial IP by Exporting
 to Vivado

Note

The Aurora Streaming example projects provide the Stream
 Controller VI that can be used as an entry point for customizing
 Aurora IP in Vivado. Complete the following steps to export the Stream
 Controller VI to Vivado.

Note

NI6593 Template

NI6594 Template

1. From the FlexRIO Integrated I/O Project Creator, open the
 Aurora Streaming example project for your model and FPGA size.
2. In the LabVIEW Project Explorer window, expand your FPGA
 target item tree, right-click the Build Specifications
 item and select New»Project Export for Vivado from the shortcut menu.
3. On the Information page, specify the destination directory
 where you want to export the files.
4. On the Source Files page, specify
 NI6593 or NI6594 Stream Controller
 (FPGA).vi as the top-level VI.
5. Click Build. 
 LabVIEW creates the exported project inside
 a ProjectExportForVivado folder in the destination directory you specified in
 step 3. The exported project contains encrypted LabVIEW FPGA files, the
 unencrypted design files with the UserRTL_ prefix, and the Vivado project.
6. Navigate to the destination directory you specified in step 3 and open the
 Vivado project using the LaunchVivadoDesignSuite.bat file.
7. Once Vivado launches, the source hierarchy loads.
8. Navigate to the UserRTL_ files in the hierarchy.
9. Use the unencrypted design files (UserRTL_) as an entry point to develop IP in
 Vivado. When your design is complete, follow the instructions in the Configuring
 LabVIEW FPGA Targets topic to instantiate your CLIP in the I/O socket. You can
 also compile the design from Vivado to generate a LabVIEW bitfile (.lvbitx) that
 can be loaded onto the FPGA target.

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=flexrio-high-speed-serial-examples.html language=enus -->
## TOPIC 00004: FlexRIO High-Speed Serial Example Projects

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `flexrio-high-speed-serial-examples.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/flexrio-high-speed-serial-examples.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI FlexRIO High-Speed Serial Instruments require you to develop an FPGA VI, design a socketed CLIP (Component Level IP), and compile a LabVIEW bitfile that implements a custom high-speed serial protocol. The FlexRIO driver includes two example projects to serve as templates for this process: An

FlexRIO High-Speed Serial Example
 Projects

The PXI FlexRIO High-Speed Serial Instruments require you to develop an FPGA VI, design a
 socketed CLIP (Component Level IP), and compile a LabVIEW bitfile that implements a
 custom high-speed serial protocol.

The FlexRIO driver includes two example projects to serve as templates for this process:

- An Aurora Streaming project based on Xilinx Aurora Core IP that allows for
 implementation of a high-speed serial protocol between your module and another
 device that implements Aurora. Use this example out-of-the-box or use it as a
 template for developing an Aurora-based custom application. org.dita.html5/xsl/topic.xsl 455 Note You can also use the Aurora
 Streaming project to test your FlexRIO High-Speed Serial module by connecting a
 QSFP cable from PORT 0 to PORT 1 and following the instructions inside the
 Continuous Stream Writer (Host) or Finite Stream Reader (Host) VIs.
- A CLIP Template project that includes a VHD file to be used as a template for
 creating a custom I/O module socketed CLIP.

Access either project through the FlexRIO Integrated IO Project Creator Tool in the
 LabVIEW Example Finder, located at LabVIEW»Help»Find Examples»Hardware Input and Output»FlexRIO»Integrated
 IO»Getting Started»Getting Started FlexRIO Integrated IO.vi.

#### Determining How to Develop Your FlexRIO
 High-Speed Serial Application

Use the flow chart below to determine which approach to the FlexRIO High-Speed Serial development
 process best fits your application.

[IMAGE alt='1378' src='GUID-531F6313-1B7F-4276-880A-CDC3355741CA-a5.png']

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=generate-netlist.html language=enus -->
## TOPIC 00005: Generating a Netlist for Verilog Source Files Not Supported in CLIP

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `generate-netlist.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/generate-netlist.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `task`
- source_description: LabVIEW FPGA does not support Verilog source files in CLIP. But, you can generate EDIF netlists from any synthesized Verilog components in the IP you are using and instantiate the netlist in a VHDL wrapper that you can then add to the CLIP. The following steps provide an example of how to generate a

Generating a Netlist for Verilog Source Files
 Not Supported in CLIP

The following steps provide an example of how to
 generate an EDIF netlist from a Xilinx IP core:

1. Open the example project for your IP core in Vivado.
2. Set the appropriate top-level source file for which you plan to generate a
 netlist.
3. Run synthesis.
4. Open the Synthesized Design using one of the following methods:
  - Select Open Synthesized Design in the
 Synthesis Completed pop-up window.
  - Select the Design Run tab, then select
 Open Synthesized Design in the left hand
 pane.
5. In the Tcl Console , enter write_edif <name of
 entity>.edf to create the netlist you will use when you
 import the IP core into your LabVIEW project. The netlist location is indicated
 by the Tcl Console window.
6. To build .edf files for an associated cell, enter the following command: write_edif -cell <name of cell> <file name>.edf For example, to create an .edf for clock_module_i, enter the following
 command: write_edif -cell clock_module_i aurora_64b66b_clock_module.edf
7. Copy the netlist into your LabVIEW FPGA CLIP directory.
8. Include your netlist in the list of synthesis files when running the LabVIEW
 Configure Component-Level IP wizard.

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=onfigure-labview-fpga-target.html language=enus -->
## TOPIC 00006: Configuring the LabVIEW FPGA Target

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `onfigure-labview-fpga-target.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/onfigure-labview-fpga-target.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a new project by selecting File»New»Project, or open an existing project by selecting File»Open. Right-click My Computer in the Project Explorer window and select New»Targets and Devices. In the Add Targets and Devices dialog box, choose New target or device and select your device. Right-clic

Configuring the LabVIEW FPGA Target

1. Create a new project by selecting File»New»Project, or open an existing project by selecting File»Open.
2. Right-click My Computer in the Project Explorer window and select New»Targets and Devices.
3. In the Add Targets and Devices dialog box, choose New target or device and select your device.
4. Right-click the device name and choose Properties from the menu.
5. In the FPGA Target Properties dialog box, choose Component-Level IP from the Category listbox.
6. To the right of the Component-Level IP listbox, click
 the Add file icon to import your CLIP declaration file
 (.xml). 
 org.dita.html5/xsl/topic.xsl 455Note Use the xml file in the CLIP Template example project as a reference when creating a CLIP
 declaration xml file for your custom IP. Access the example xml file by
 opening your example project root folder and selecting Socketed CLIPs»Template.
7. Click OK. LabVIEW automatically creates a compatible I/O socket in the project.
8. To instantiate the CLIP in the I/O socket, expand the FPGA target tree item, right-click IO Socket and select Properties from the menu.
9. In the IO Socket Properties dialog box, choose General from the Category listbox, then select a CLIP from the Component Level IP listbox.
10. Click OK. The user-defined signals in your CLIP appear under the IO Socket item.

Enter the tasks the user should do
 after finishing this task (optional).

<!--NI_TOPIC bundle=develop-flexrio-high-speed-serial-protocols path=optimize-third-party-ip.html language=enus -->
## TOPIC 00007: Optimizing Third-Party IP for LabVIEW Integration

- bundle_id: `develop-flexrio-high-speed-serial-protocols`
- source_path: `optimize-third-party-ip.html`
- source_url: https://docs-be.ni.com/bundle/develop-flexrio-high-speed-serial-protocols/raw/resource/enus/optimize-third-party-ip.html
- document_id: `develop-flexrio-high-speed-serial-protocols`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your application will not use Aurora Core IP, you can choose to purchase or license third-party IP. Follow the guidelines below to optimize your third-party IP for LabVIEW integration. When Generating an IP Core from the Xilinx Vivado IP Catalog Refer to Generating and Integrating Aurora IP into

Optimizing Third-Party IP for LabVIEW
 Integration

If your application will not use Aurora Core IP, you can choose to purchase or license
 third-party IP. Follow the guidelines below to optimize your third-party IP
 for LabVIEW integration.

#### When Generating an IP Core from the Xilinx
 Vivado IP Catalog

- Refer to Generating and Integrating Aurora IP into Your LabVIEW Project ,
 available by search at ni.com, for a step-by-step procedure you can use as
 guidance for generating any IP core from the Xilinx Vivado IP Catalog.
- Ensure you have purchased and installed all necessary licenses. For more
 information about managing licenses, search for UG 973: Vivado Design Suite:
 Release Notes, Installation, and Licensing at www.xilinx.com.
- In the IP core settings, select AXI4-Stream for high-speed data streams.
- NI does not guarantee compatibility between AXI4-Lite for DRP accesses in the
 Xilinx IP cores and LabVIEW FPGA AXI4-Lite adapters. Refer to the Aurora
 Streaming example projects in the FlexRIO Integrated I/O Project Creator for an
 example of how to use the LabVIEW FPGA AXI4-Lite adapters to connect to DRP
 within the CLIP.

#### When Using Existing VHDL IP inside CLIP or
 IPIN

- For instructions on importing existing IP into your project, refer to
 Importing External IP Into LabVIEW FPGA available by search at
 ni.com.
- CLIP does not support custom user libraries in the VHDL. If your VHDL uses
 custom user libraries, you can either reference the default reference library
 instead of a custom user library, or create a netlist from the VHDL and
 integrate the netlist using CLIP.
- Refer to the Creating or Acquiring IP topic in the LabVIEW FPGA Module
 Help for more information about using existing VHDL IP inside CLIP or
 IPIN.

#### When Modifying Third-Party IP Core
 Logic

- If you purchase or license an IP core from Xilinx, refer the Xilinx Product
 Guide for the IP before attempting to make any modifications.
- Ensure all clocks are connected.
- Ensure AXI4-Lite management signals are connected correctly to the DRP signals
 on the MGT primitives corresponding to your FPGA type.
- When designing in Vivado, you can access resources outside of the IP core logic,
 such as MGT_RefClk input buffers and QPLL wrappers, by selecting
 Include Shared Logic in example design in the IP
 wizard.

##### How to Use Vivado's Including Shared
 Logic Options

The IP wizard inside Vivado provides options for including shared logic in the VHDL.

The following diagrams compare how the IBUFDS_GTE3/4 resource is exposed in the top-level
 CLIP VHDL when selecting Including Shared Logic in example
 design or Including Shared Logic in
 core.

To access resources outside the IP core logic,
 select the Include Shared Logic in example design
 option.

###### Including Shared Logic in core Option

[IMAGE alt='1378' src='GUID-23812B03-6522-4A3D-A9A7-88CA7191D107-a5.png']

###### Including Shared Logic in example design
 Option

[IMAGE alt='1378' src='GUID-6B0719B4-F940-492E-8E56-2BF5FE3B7033-a5.png']

#### When Compiling LabVIEW FPGA VIs that
 Incorporate Third-Party IP

- You may need to purchase and install additional licenses to compile FPGA
 designs that incorporate licensed cores from Xilinx or third-party IP
 vendors. Refer to UG 973: Vivado Design Suite: Release Notes,
 Installation, and Licensing at www.xilinx.com for information about
 managing licenses.
- FlexRIO high-speed serial instruments include large FPGA devices that require a
 64-bit compile worker.
- You cannot add additional licenses to remote compile workers in the NI LabVIEW FPGA
 Compile Cloud Service. You cannot use NI LabVIEW FPGA Compile Cloud Service to
 compile designs that incorporate Xilinx or other third-party licensed cores.

#### When Writing a VHDL Wrapper around the
 Protocol IP Core

- Keep the interface between the CLIP and the LabVIEW FPGA diagram as simple as
 possible. org.dita.html5/xsl/topic.xsl 455 Note LabVIEW stores
 values in big-endian format, and your IP may accept only little-endian
 format. For simplicity and ease of use, perform endian conversions in the
 CLIP and keep them off the LabVIEW diagram.
- Do not pass asynchronous signals to the LabVIEW FPGA diagram. Register the
 signals in a clock domain in the VHDL logic before passing them to the LabVIEW
 FPGA diagram.
- Run synthesis.
- Use AXI4-Stream and AXI4-Lite interfaces for streaming data and register
 accesses. NI provides AXI4-Stream and AXI4-Lite wrappers to use on the LabVIEW
 FPGA diagram.
- If you expose an AXI4-Lite endpoint, use Xilinx AXI4 interconnect IP to expose
 only one AXI4-Lite endpoint to the LabVIEW FPGA diagram.
- Document the frequency of clocks coming from CLIP. In larger applications, the
 default enable chain in LabVIEW can create routing congestion and limit
 performance. Consider supporting enable chain removal. Refer to Improving
 Timing Performance in Large Designs in the LabVIEW FPGA Module Help
 for more information about how and when to remove enable chains.
- Implement a state machine that allows asynchronous resets. If you declare an
 input signal as a reset signal in the Configure CLIP 
 wizard, then that signal is asserted when the LabVIEW FPGA VI is not running.
- Implement a state machine that resets the protocol cores when the PORT# module
 is absent.
- Connect various clocks from your CLIP to the DebugClks
 std_logic_vector in order to use host-side frequency counter
 debugging utilities.
- Provide timing constraints in the constraints file for your CLIP. Include timing
 constraints for clocks within your CLIP, but do not include pin or location
 constraints on MGTs transceiver lanes and RefClks.
- Use the TXOUTCLK and RXOUTCLK clock
 constraints for your high-speed serial CLIP if your protocol uses it directly.
 Refer to the following syntax example for a clock constraint:
 create_clock -period <period in ns> [get_pins %ClipInstancePath%/<path to your clock pin relative to the top level CLIP VHDL>]
- If you generate an asynchronous reset within your CLIP VHDL, create a false path
 constraint from the register that generates the reset signal and include a
 "don't touch" attribute. Refer to the following syntax example for a "don't
 touch" attribute:
 attribute dont_touch : string; attribute dont_touch of <signal name> : signal is "true"; Refer
 to the following syntax example for a false path
 constraint: set_false_path -from [get_cells %ClipInstancePath%/<path to your register>]
- When writing constraints, you may need to refer to the instance name of the CLIP
 or the absolute path to the CLIP instance in the VHDL hierarchy. Refer to
 Applying Constraints Using %ClipInstanceName% and
 %ClipInstancePath% for more information about using the
 search-and-replace keywords %ClipInstanceName% and %ClipInstancePath%.

#### When Documenting Your IP

- Note the endianness of the CLIP in order to properly interface the CLIP to the
 LabVIEW FPGA diagram.
- Clearly define which portion of the entity faces the diagram and which portion
 of the entity faces the front panel.
- Clearly define LED behavior.
- Describe how each signal is used and document unused signals. Signal use can
 affect which ports are active with the IP and affect the behavior of cables upon
 insertion and removal.
- Use the DebugClks signal to determine the health of the internal clocks being
 sent to the IP. Define which bits of the 4-bit vector correspond to the clock
 being monitored.
- Document how you integrate AXI4-Lite signals with LabVIEW data types. Some
 AXI4-Lite signals do not integrate easily with LabVIEW data types. For example,
 address ports can have widths of 11, but LabVIEW only provides addresses with
 widths of 8, 16, 32, and 64. Additionally, the AXI4-Lite and AXI4-Stream
 adapters are configured for use with fixed-point I/O.
- Document how the CLIP uses and routes clocks. You must route clocks to the
 diagram for use with the single-cycle timed loop (SCTL) in LabVIEW FPGA.
- Document the address map of individual components within any AXI4-Lite
 interfaces.
