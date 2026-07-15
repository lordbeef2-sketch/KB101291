# NI DOCUMENT BUNDLE: labview-nxg-fpga-targets

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-fpga-targets start=1 end=48 -->
<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=accessing-stored-data-using-memory.html language=enus -->
## TOPIC 00001: Transferring Data Using a Memory Item

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `accessing-stored-data-using-memory.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/accessing-stored-data-using-memory.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a memory item to transfer data on an FPGA without respect to the sequence in which the data is written to memory. What to Use While Loops Create Memory Write Memory Read Memory What to Do Create the following diagram to transfer data between loops on an FPGA. Customize the gray sections for your

Transferring Data Using a Memory Item

Use a memory item to transfer data on an FPGA without respect to the sequence in which the data is written to memory.

#### What to Use

- While
 Loops
- Create Memory
- Write Memory
- Read Memory

#### What to Do

Create the following diagram to transfer data between loops on an FPGA.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-52C71248-4161-4E33-97B6-793870E9B864-a5.png']

|  | Define the data type, size, and latency of your locally scoped memory item using the Create Memory node. In this example, the Create Memory node defines the memory item properties to the following values: Memory type is Block RAMRead latency is 1 cycleRead-only is disabled |
| --- | --- |
|  | Specify the address within the memory item where you write data from this clock domain. The code in this diagram generates one address per loop iteration in the series {0,1,2} so that the Write Memory node can write a value for each of the three cases in the Case Structure in this While Loop. |
|  | Capture or generate the data you write to memory during each loop iteration. In this diagram, the Case Structure performs Square, Negate, and Increment operations on the value received from input value. |
|  | Use the memory reference from the Create Memory node to specify the memory item that the Write Memory node writes data samples to. For example, in this diagram, the Write Memory node writes the result of the square operation to address 0, writes the result of the negate operation to address 1, and writes the result of the increment operation to address 2. |
|  | Specify the address you read from this loop. The Case Selector, labeled operation, selects address 0 for Square, address 1 for Negate, and address 2 for Increment. |
|  | The Read Memory node waits until data from the specified address is read from the memory. |
|  | The Read Memory node returns an error if the specified address is greater than the size of the memory. Use the error out output to check if the output data is valid. Use the output data to perform subsequent operations. |

#### Troubleshooting

If the memory item returns unexpected data, verify that the input addresses for the
 Read Memory and Write Memory nodes are
 correct.

#### Examples

Search within the programming environment to access the following installed example:
 *Memory*.

Parent topic:

Data Transfer Using Memory Items

Related concepts:

- Data Transfer Using Memory Items
- Storing and Transferring Data

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=block-memory.html language=enus -->
## TOPIC 00002: Block RAM (BRAM) on an FPGA

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `block-memory.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/block-memory.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Block RAM (BRAM) is a type of random access memory embedded throughout an FPGA for data storage. You can use BRAM to accomplish the following tasks: Transfer data between multiple clock domains by using local FIFOs Transfer data between an FPGA target and a host processor by using a DMA FIFO Transfe

Block RAM (BRAM) on an FPGA

Block RAM (BRAM) is a type of random access memory embedded throughout an FPGA for data storage.

You can use BRAM to accomplish the following tasks:

- Transfer data between multiple clock domains by using local FIFOs
- Transfer data between an FPGA target and a host processor by using a DMA FIFO
- Transfer data between FPGA targets by using a peer-to-peer FIFO
- Store large data sets on an FPGA target more efficiently than RAM built from look-up tables

Parent topic:

Introduction to FPGA Resources

Related concepts:

- DRAM on an FPGA Target
- Configurable Logic Blocks (CLBs) on an FPGA
- Storing and Transferring Data
- Introduction to FPGA Resources

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=clocks-timing-on-fpga.html language=enus -->
## TOPIC 00003: Clocks and Timing on an FPGA

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `clocks-timing-on-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/clocks-timing-on-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW NXG implements FPGA code with a synchronous digital circuit that enforces the standard dataflow model. This synchronous digital circuit is driven by a clock, which is a periodic digital signal that determines the allowed propagation delay. Propagation delay is the time it takes a signal to t

Clocks and Timing on an FPGA

LabVIEW NXG implements FPGA code with a synchronous digital circuit that enforces the
 standard dataflow model. This synchronous digital circuit is driven by a
 *clock*, which is a periodic digital signal that determines the allowed
 propagation delay. *Propagation delay* is the time it takes a signal to travel
 along a combinatorial logic path from one register to the next. The *combinatorial
 path* is the collection of logic and wiring that a signal encounters between two
 registers.

Propagation delay consists of the following components:

Logic delay

Routing delay

Because registers update every clock cycle, the propagation delay must not exceed the clock
 period. By default, the LabVIEW NXG FPGA Module produces circuits that run at a clock rate of
 40 MHz outside the Clock-Driven Loop. A 40 MHz clock rate corresponds to a 25 nanoseconds
 clock period.

#### Automatically Inserting Registers to Reduce Propagation Delay

For paths that
 exceed the 25 ns constraint, LabVIEW NXG automatically inserts registers that break up the
 overall propagation delay into smaller delays to ensure that the propagation delay in the
 generated circuit is under the limit.

For example, the following figure includes a
 chain of nodes: A, B, C, and D. Each node has a certain amount of logic delay. The wires
 between the nodes have routing delay. The logic delay and the routing delay add up to a
 total delay of 29 ns, which is greater than the 25 ns timing constraint.

[IMAGE alt='1378' src='GUID-6A7E33D2-B7FE-4C4B-B7AF-B8CC3D8D5351-a5.svg']

To meet the delay propagation
 constraints, LabVIEW NXG automatically inserts registers along that path. In the following
 figure, the register breaks up the path into two paths, making both paths within the 25 ns
 timing constraint.

Note

[IMAGE alt='1378' src='GUID-B47DD8B3-EA83-423A-8A22-B0A6915384BD-a5.svg']

#### Automatic Loop Pipelining for Faster Execution

LabVIEW NXG executes loops with
 only algorithmic code in a pipelined fashion. In other words, a loop iteration may start
 before the previous iteration is complete as long as all the data dependencies for the
 iteration are satisfied, which makes the loop execution more efficient.

The following
 diagram illustrates loop pipelining with two loops and a Sequence
 Structure. The diagram includes five independent code units.

[IMAGE alt='1378' src='GUID-10D693AF-2C98-48F1-84F6-D97D564560E7-a5.png']

|  | The controls execute simultaneously at the startup of the VI because they do not have any data dependencies. |
| --- | --- |
|  | The For Loop is an independent code unit with data dependency on the x control. The For Loop executes in a pipelined fashion because it includes only algorithmic code. |
|  | The While Loop is an independent code unit with data dependency on the y control. The While Loop executes in a pipelined fashion because it includes only algorithmic code. |
|  | The Sequence Structure is an independent code unit with data dependencies on the z control and the output of the While Loop. |
|  | The element indicator is an independent code unit with data dependency on the Sequence Structure. |

The following figure illustrates the execution time of two consecutive calls to
 this VI, each big box representing one call to the VI. Each small box or group of small
 boxes represents the execution time of the corresponding code unit in the VI. With
 pipelining, loop iterations of the For Loop and While
 Loop have overlap in time, which results in faster loop execution.

For
 each call of the VI, the For Loop always iterates five times with a
 definite execution time because the Count input is set to 5. The
 While Loop iterates a variable number of times with an indefinite
 execution time because the number of loop iteration depends on the value of the
 y input, which can vary from call to call.

[IMAGE alt='1378' src='GUID-54E1E5DE-35F5-40F3-9FA0-66654286B8A3-a5.svg']

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=compiling-fpga-code.html language=enus -->
## TOPIC 00004: Compiling FPGA Code

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `compiling-fpga-code.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/compiling-fpga-code.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: To run code on an FPGA, you must compile the FPGA code into a bitfile that you then deploy to the FPGA. The bitfile contains binary data that describes how to configure the FPGA circuit so that it performs the same function as the code in the FPGA VI. Before you build a bitfile, ensure your FPGA app

Compiling FPGA Code

To run code on an FPGA, you must compile the FPGA code into a bitfile that you then deploy to the FPGA. The bitfile contains binary data that describes how to configure the FPGA circuit so that it performs the same function as the code in the FPGA VI.

Before you build a bitfile, ensure your FPGA application and all dependencies are targeted to an FPGA device in SystemDesigner.

Complete the following steps to compile your FPGA code into a bitfile:

Note

test and debug an FPGA VI

1. In the Application document, on the 
 Document tab, enter information about your application in the 
 Details section. Configure the build settings in the 
 Build section.
2. Click File»Save all.
3. Optional: 
 Click 
 FPGA preferences and [set up the FPGA compiler](/csh?topicname=configuring-the-fpga-compiler.html).
4. Click Build ([IMAGE alt='1378' src='GUID-532209E8-D52A-49BB-B0E4-A11675D091A5-a5.png']).
5. If a warning appears, click 
 Continue. 
 The bitfile begins compiling immediately and the 
 Build Queue tab shows the status of current and completed compilations. 
 org.dita.html5/xsl/topic.xsl 455Note Do not change any code in your FPGA application
 during the diagram analysis stage of compilation. Any changes you make to
 code during the diagram analysis stage may be reflected in the bitfile. If
 you want to continue working on code while you wait for the compilation to
 finish, do so after the diagram analysis stage.

[Monitor the compilation of your bitfile](/csh?topicname=monitoring-bitfile-compilation.html) to determine whether you need to make changes to your code.

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=configurable-logic-blocks.html language=enus -->
## TOPIC 00005: Configurable Logic Blocks (CLBs) on an FPGA

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `configurable-logic-blocks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/configurable-logic-blocks.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: A configurable logic block (CLB) is the basic repeating logic resource on an FPGA. When linked together by routing resources, the components in CLBs execute complex logic functions, implement memory functions, and synchronize code on the FPGA. CLBs contain smaller components, including flip-flops, l

Configurable Logic Blocks (CLBs) on an FPGA

A configurable logic block (CLB) is the basic repeating logic resource on an FPGA.
 When linked together by routing resources, the components in CLBs execute complex logic functions, implement memory functions, and synchronize code on the FPGA.

CLBs contain smaller components, including flip-flops, look-up tables (LUTs), and multiplexers.

Flip-Flop

Look-up Table (LUT)

Multiplexer

When you compile code to run on an FPGA target, LabVIEW implements much of the code using flip-flops, LUTs, and multiplexers.

Parent topic:

Introduction to FPGA Resources

Related concepts:

- Block RAM (BRAM) on an FPGA
- I/O Resources on an FPGA
- DRAM on an FPGA Target
- Storing and Transferring Data
- Introduction to FPGA Resources

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=configuring-the-fpga-compiler.html language=enus -->
## TOPIC 00006: Configuring the FPGA Compiler

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `configuring-the-fpga-compiler.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/configuring-the-fpga-compiler.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to set up the FPGA compiler: Select FilePreferences. On the FPGA tab, select an option in the Compiler section. The default is Local compile server. Option Description Local compile server Compile your FPGA code using the development computer. NI LabVIEW FPGA Compile Clo

Configuring the FPGA Compiler

Complete the following steps to set up the FPGA compiler:

1. Select 
 File»Preferences.
2. On the 
 FPGA tab, select an option in the 
 Compiler section. The default is 
 Local compile server. 
 OptionDescriptionLocal compile server
 Compile your FPGA code using the development computer.NI LabVIEW FPGA Compile Cloud Service
 Compile your FPGA code using high-performance cloud service that NI provides.Remote compile server
 Compile your FPGA code using an FPGA compile farm.
3. If you selected 
 NI LabVIEW FPGA Compile Cloud Service or 
 Remote compile server in the previous step, specify the required credentials as follows:
  - NI LabVIEW FPGA Compile Cloud Service —Specify the username and password of your NI LabVIEW FPGA Compile Cloud Service account .
  - Remote compile server —Specify the login information of the compile server, such as server name, port, username, and password. If the compile server allows admin users only, specify 
 admin as the username. If the compile server was not configured to use HTTPS, disable the 
 Secure connection checkbox. 
 org.dita.html5/xsl/topic.xsl 455 Note If you are not the administrator of the compile farm, ask the administrator for the credentials. If you are the administrator of a compile farm, refer to [Setting up an FPGA Compile Farm](/csh?topicname=setting-up-an-fpga-compile-farm.html) for more information about how to set up an FPGA compile farm.
4. Click 
 Test, if available, to verify the settings are valid. Resolve any errors.
5. Click 
 OK.

Parent topic:

Compiling FPGA Code

Related tasks:

- Compiling FPGA Code

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=control-execution-rate.html language=enus -->
## TOPIC 00007: Using Clock Domains to Control the Execution Rate of Clock-Driven Loops

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `control-execution-rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/control-execution-rate.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: FPGA targets support more than one clock. By configuring each Clock-Driven Loop to use a different clock, you can implement multiple clock domains in your Clock-Driven Logic code to execute your code at different rates to achieve separate timing objectives within one application. What to Use Clock-D

Using Clock Domains to Control the Execution Rate of Clock-Driven Loops

Clock-Driven Loop

#### What to Use

- Clock-Driven Loop
- Clock terminal of the Clock-Driven Loop

#### What to Do

Create the following diagram to implement clock domains that control the execution rates of code within Clock-Driven Loops.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-DB879121-9F35-4319-90FA-5670D928FA2E-a5.png']

|  | Divide your code into sections according to the separate timing objectives of your application. Place each section inside a Clock-Driven Loop. |
| --- | --- |
|  | When you wire a clock to the Clock-Driven Loop, all code placed within the loop attempts to execute within one clock cycle of the chosen clock. For each Clock-Driven Loop on your diagram, select a clock that allows you to execute code at a rate that meets your timing objective for that section of code. Note To execute more than one Clock-Driven Loop at the same clock rate, wire a single clock constant to multiple loops. Tip To create modular code for use with different clocks in different applications, wire a clock control to the Clock-Driven Loop instead of a clock constant. |

#### Troubleshooting

If your code fails to meet the timing objectives of your application using the clocks you choose:

- Create derived clocks to run code at a lower frequency.
- Use pipelining to reduce the length of the critical path. In the 
 Timing Violations tab, you can highlight the critical path on the diagram.

#### Examples

Search within the programming environment to access the following installed example:
 *Multiple Clock Domains*.

Parent topic:

Using Clock-Driven Loops to Run Code at Higher Rates with Lower Latency

Related concepts:

- Clocks and Timing on an FPGA

Related tasks:

- Customizing the Execution Rate of Clock-Driven Loops
- Resolving Timing Violations on the FPGA

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=create-eip-document-from-hdl-source.html language=enus -->
## TOPIC 00008: Creating an External FPGA IP Document from IP Source Files

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `create-eip-document-from-hdl-source.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/create-eip-document-from-hdl-source.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate IP into your FPGA application by creating an External FPGA IP document that declares IP files in a project for instantiation as component-level IP (CLIP) or an External FPGA IP Node. If you want to use an IP-XACT file to import IP descriptions into the External FPGA IP document, refer to C

Creating an External FPGA IP Document from IP Source Files

Integrate IP into your FPGA application by creating an External FPGA IP document that declares IP files in a project for instantiation as component-level IP (CLIP) or an External FPGA IP Node.

Note

Creating an External FPGA IP Document from an IP-XACT File

Creating an External FPGA IP (EIP) document is a prerequisite step for integrating IP into your FPGA code. The EIP document catalogs port definitions from FPGA IP and then makes those port definitions available for use as palette items. After you create an EIP document, you can instantiate your IP resources in your FPGA code using the External FPGA IP Node or component-level IP (CLIP).
 The EIP document conforms to the IP-XACT standard (IEEE 1685).

Ensure that the IP for integration is any of the following supported file types:

| File Type | File Extension | Top-Level Synthesis | Additional Synthesis | Top-Level Simulation | Additional Simulation |
| --- | --- | --- | --- | --- | --- |
| VHSIC Hardware Description Language (VHDL) | .vhd | Yes | Yes | Yes | Yes |
| Xilinx Synthesis Technology (XST) Netlist Note XST Netlist files are supported only on Xilinx 7-series FPGA chips. | .ngc | Yes | Yes | No | No |
| Electronic Data Interchange Format (EDIF) Netlist | .edif, .edf, .edn | Yes | Yes | No | No |
| Design Checkpoint (DCP) | .dcp | Yes | Yes | No | No |
| Xilinx Core Instance (XCI) | .xci | Yes | Yes | No | Yes |
| Data | .data | No | Yes | No | No |
| Coefficient | .coe | No | Yes | No | No |
| Block RAM Memory Map (BMM) | .bmm | No | Yes | No | No |
| Xilinx Design Constraints (XDC) | .xdc | No | Yes | No | No |
| Memory Initialization File (MIF) | .mif | No | No | No | Yes |
| Configuration | .cfg | No | No | No | Yes |
| Verilog | .v | The FPGA compile server does not support Verilog files. Synthesize Verilog files to a Netlist before importing. |  |  |  |

1. Open the Application document for your FPGA target and click 
 New»External FPGA IP to create an External FPGA IP document. Double-click the new EIP document to open it.
2. In the 
 Main Synthesis Entity section, click the 
 Browse button to select the top-level source file for deployment on an FPGA.
3. In the 
 Main Simulation Entity section, click the 
 Browse button to select the top-level source file for simulation on a host computer. 
 If the 
 Main Synthesis Entity is a VHDL source file, the EIP document populates the 
 Main Simulation Entity text box with the same file you specify for 
 Main Synthesis Entity. The EIP document does not automatically populate files that are not VHDL. You can use different IP files for 
 Main Synthesis Entity and 
 Main Simulation Entity, but the IP files must share the same port and generic definitions. 
 org.dita.html5/xsl/topic.xsl 455Note CLIP does not support simulation. Your selection of a file for 
 Main Simulation Entity will apply only to External FPGA IP Node instances derived from this EIP document.
4. In the 
 Additional Resources section, click the 
 + button to add supplementary IP files as required by your application.
5. Click the 
 Parse and Verify button to populate the EIP document with the ports and signals defined in your IP.
6. Modify configuration of each port in the 
 Signal configuration, 
 Generics, and 
 Clock configuration tables. 
 The 
 Signal configuration, 
 Generics, and 
 Clock configuration tables in the EIP document display ports and generics defined in IP. When you click on a port, the 
 Item tab displays settings you can configure for each port.
  1. In the 
 Signal Configuration table, click the name of a signal to configure it on the 
 Item tab. 
 Refer to the following table for information regarding signal configuration options:
 Signal configuration option
 DescriptionLabVIEW name
 The 
 LabVIEW name for each signal must be unique. By default, the 
 LabVIEW name for a signal matches the name specified in the IP source file.
 Type
 The default is 
 Data. When the signal 
 Type is set to 
 Clock, the EIP document adds that signal to the 
 Clock configuration table for additional configuration. 
 org.dita.html5/xsl/topic.xsl 455Note If you change a signal 
 Type in the EIP document after creating an External FPGA IP Node instance, the change propagates to each External FPGA IP Node instance.
 Data type
 These data type definitions can be overridden within each External FPGA IP Node or CLIP instance. 
 org.dita.html5/xsl/topic.xsl 455Note If you change the 
 Data type of a signal in the EIP document after creating an External FPGA IP Node instance, the corresponding input/output of the External FPGA IP Node instance does not change.
 Active low/Active high
 This option is available only when the signal 
 Type is set to 
 reset. The default is 
 active high.
 Associated clock
 The 
 Associated Clock menu behaves differently depending on which 
 Type setting you select for a signal. 
 Data: the selected signal will work only in the clock domain selected in 
 Associated Clock.Clock: 
 When you place the External FPGA IP Node in Clock-Driven Logic, you must wire the clock input of the Clock-Driven Loop to the FPGA base clock you select for 
 Associated Clock.When you create a CLIP instance, you must map the CLIP clock to the same FPGA base clock that you select for 
 Associated Clock.When you select an input clock within the same EIP document from the 
 Associated Clock menu, the currently selected clock will be phase aligned to that input clock. You can set the ratio between these two clocks in the 
 Clock configuration table.Reset: this signal type is not affected by the 
 Associated Clock menu.Enable: the selected signal will only work in the clock domain selected in 
 Associated Clock.
  2. In the 
 Generics table, click on the name of a generic to configure it on the 
 Item tab. 
 The EIP document imports the 
 Default Value from the IP source file, but you can modify it by entering any string value that corresponds to the generic type specified in the source file. For example, enter a string of 
 True or 
 False for a boolean generic.
 org.dita.html5/xsl/topic.xsl 455Note If you change the 
 Default Value of a generic, you must click 
 Parse and Verify to apply your changes.
  3. In the 
 Clock configuration table, click on the name of a clock to configure it on the 
 Item tab.
  4. In the 
 MMCMs required and 
 BUFGs required text boxes, declare the number of mixed-mode clock managers and global buffers the IP will consume. 
 The application will compare your input for 
 MMCMs required and 
 BUFGs required with the maximum number of MMCMs and BUFGs allowed on your FPGA target. If your input exceeds the number of MMCMs and BUFGs allowed, the application will prevent you from compiling a bitfile.
 org.dita.html5/xsl/topic.xsl 455Note Consult the documentation for your FPGA target to determine how many MMCMs and BUFGs are available. The IP you catalog in the EIP document will consume physical resources on the FPGA, and you will need to configure these text boxes according to the specifications of your specific FPGA target.
7. Save the EIP document.

adding the External FPGA IP Node to your FPGA VI diagram

creating and adding a CLIP instance to your application

Parent topic:

Integrating External FPGA IP into an FPGA Application

Related concepts:

- Introduction to FPGA Resources
- I/O Resources on an FPGA
- Clocks and Timing on an FPGA

Related tasks:

- Creating an External FPGA IP Document from an IP-XACT File

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=create-eip-document-from-ip-xact.html language=enus -->
## TOPIC 00009: Creating an External FPGA IP Document from an IP-XACT File

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `create-eip-document-from-ip-xact.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/create-eip-document-from-ip-xact.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate IP into your FPGA application by importing IP descriptions from an IP-XACT XML file into an EIP document, declaring IP files in a project for use as component-level IP (CLIP) or the External FPGA IP Node. If you want to use IP source files to create an External FPGA IP document, refer to C

Creating an External FPGA IP Document from an IP-XACT File

Integrate IP into your FPGA application by importing IP descriptions from an IP-XACT XML file into an EIP document, declaring IP files in a project for use as component-level IP (CLIP) or the External FPGA IP Node.

Note

Creating an External FPGA IP Document from IP Source Files

Creating an External FPGA IP (EIP) document is a prerequisite step for integrating IP into your FPGA code. The EIP document catalogs port definitions from FPGA IP and then makes those port definitions available for use as palette items. After you create an EIP document, you can instantiate your IP resources in your FPGA code using the External FPGA IP Node or component-level IP (CLIP).

IP-XACT XML files, such as those created by Xilinx Vivado, describe IP blocks used in electronic system design. Import IP descriptions from an IP-XACT file in place of manually selecting IP files for inclusion into the EIP document. After importing IP descriptions into the EIP document editor, you can configure and edit component definitions from the IP source files and save them as an EIP file. The EIP document conforms to the IP-XACT standard (IEEE 1685). For more information about the IP-XACT XML schema, visit the IP-XACT Working Group page at accellera.org.

Ensure that the IP your IP-XACT file describes is any of the following supported file types:

| File Type | File Extension | Top-Level Synthesis | Additional Synthesis | Top-Level Simulation | Additional Simulation |
| --- | --- | --- | --- | --- | --- |
| VHSIC Hardware Description Language (VHDL) | .vhd | Yes | Yes | Yes | Yes |
| Xilinx Synthesis Technology (XST) Netlist Note XST Netlist files are supported only on Xilinx 7-series FPGA chips. | .ngc | Yes | Yes | No | No |
| Electronic Data Interchange Format (EDIF) Netlist | .edif, .edf, .edn | Yes | Yes | No | No |
| Design Checkpoint (DCP) | .dcp | Yes | Yes | No | No |
| Xilinx Core Instance (XCI) | .xci | Yes | Yes | No | Yes |
| Data | .data | No | Yes | No | No |
| Coefficient | .coe | No | Yes | No | No |
| Block RAM Memory Map (BMM) | .bmm | No | Yes | No | No |
| Xilinx Design Constraints (XDC) | .xdc | No | Yes | No | No |
| Memory Initialization File (MIF) | .mif | No | No | No | Yes |
| Configuration | .cfg | No | No | No | Yes |
| Verilog | .v | The FPGA compile server does not support Verilog files. Synthesize Verilog files to a Netlist before importing. |  |  |  |

Note

1. Open the Application document for your FPGA target and click 
 New»External FPGA IP to create an External FPGA IP document. Double-click the new EIP document to open it.
2. Click the 
 Import button and select an IP-XACT XML file.
3. Inspect the EIP document to verify that it imported the information from the IP-XACT file correctly. 
 org.dita.html5/xsl/topic.xsl 455Note By default, the EIP document sets the signal 
 Type to 
 Data for all signals imported from an IP-XACT file. You will need to perform additional configuration of the EIP document to make the import successful.
4. Configure signals, generics, and clocks.
  1. In the 
 Signal Configuration table, click the name of a signal to configure it on the 
 Item tab. 
 Refer to the following table for information regarding signal configuration options: 
 Signal configuration optionDescriptionLabVIEW nameThe 
 LabVIEW name for each signal must be unique. By default, the 
 LabVIEW name for a signal matches the name specified in the IP source file.TypeThe default is 
 Data. When the signal 
 Type is set to 
 Clock, the EIP document adds that signal to the 
 Clock configuration table for additional configuration. 
 org.dita.html5/xsl/topic.xsl 455Note If you change a signal 
 Type in the EIP document after creating an External FPGA IP Node instance, the change propagates to each External FPGA IP Node instance.Data typeThese data type definitions can be overridden within each External FPGA IP Node or CLIP instance. 
 org.dita.html5/xsl/topic.xsl 455Note If you change the 
 Data type of a signal in the EIP document after creating an External FPGA IP Node instance, the corresponding input/output of the External FPGA IP Node instance does not change.Active low/Active highThis option is available only when the signal 
 Type is set to 
 reset. The default is 
 active high.Associated clockThe 
 Associated Clock menu behaves differently depending on which 
 Type setting you select for a signal. 
 Data: the selected signal will work only in the clock domain selected in 
 Associated Clock.Clock: 
 When you place the External FPGA IP Node in Clock-Driven Logic, you must wire the clock input of the Clock-Driven Loop to the FPGA base clock you select for 
 Associated Clock.When you create a CLIP instance, you must map the CLIP clock to the same FPGA base clock that you select for 
 Associated Clock.When you select an input clock within the same EIP document from the 
 Associated Clock menu, the currently selected clock will be phase aligned to that input clock. You can set the ratio between these two clocks in the 
 Clock configuration table.Reset: this signal type is not affected by the 
 Associated Clock menu.Enable: the selected signal will only work in the clock domain selected in 
 Associated Clock.
  2. In the 
 Generics table, click on the name of a generic to configure it on the 
 Item tab. 
 The EIP document imports the 
 Default Value from the IP source file, but you can modify it by entering any string value that corresponds to the generic type specified in the source file. For example, enter a string of 
 True or 
 False for a boolean generic.
  3. In the 
 Clock configuration table, click on the name of a clock to configure it on the 
 Item tab.
  4. In the 
 MMCMs required and 
 BUFGs required text boxes, declare the number of mixed-mode clock managers and global buffers the IP will consume. 
 The application will compare your input for 
 MMCMs required and 
 BUFGs required with the maximum number of MMCMs and BUFGs allowed on your FPGA target. If your input exceeds the number of MMCMs and BUFGs allowed, the application will prevent you from compiling a bitfile.
 org.dita.html5/xsl/topic.xsl 455Note Consult the documentation for your FPGA target to determine how many MMCMs and BUFGs are available. The IP you catalog in the EIP document will consume physical resources on the FPGA, and you will need to configure these text boxes according to the specifications of your specific FPGA target.
5. Save the EIP document. 
 org.dita.html5/xsl/topic.xsl 455Note The EIP document does not overwrite the original IP-XACT file.

adding the External FPGA IP Node to your FPGA VI diagram

creating and adding a CLIP instance to your application

Parent topic:

Integrating External FPGA IP into an FPGA Application

Related concepts:

- Introduction to FPGA Resources
- I/O Resources on an FPGA
- Clocks and Timing on an FPGA

Related tasks:

- Creating an External FPGA IP Document from IP Source Files

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=custom-condition-symbol.html language=enus -->
## TOPIC 00010: Creating Custom Condition Symbols for an FPGA Target

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `custom-condition-symbol.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/custom-condition-symbol.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: You can create custom condition symbols targeted to an FPGA and use these symbols in any Disable Structure within your FPGA application. In SystemDesigner, select the FPGA target. On the Item tab, in the Compile symbols section, click the plus button to create a new symbol in the User-defined symbol

Creating Custom Condition Symbols for an FPGA Target

You can create custom condition symbols targeted to an FPGA and use these symbols in any Disable Structure within your FPGA application.

1. In SystemDesigner, select the FPGA target.
2. On the 
 Item tab, in the 
 Compile symbols section, click the plus button to create a new symbol in the 
 User-defined symbols table.
3. Enter a name and value for the symbol. Choose a name that indicates what the condition symbol is evaluating.

Disable Structure

Related information:

- Disable Structure (G Dataflow)

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=data-transfer-panel-controls-indicators.html language=enus -->
## TOPIC 00011: Data Transfer Using Panel Controls and Indicators

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `data-transfer-panel-controls-indicators.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/data-transfer-panel-controls-indicators.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Read Write FPGA Control node in a host VI to access the panel controls and indicators of the FPGA VI.Support for programmatic panel communication varies for each FPGA target. Refer to the hardware documentation for the FPGA target for more information.Use this method for small, frequent data

Data Transfer Using Panel Controls and
 Indicators

Read Write FPGA
 Control

Note

Use this method for
 small, frequent data transfers between the FPGA and the host because each call to
 the Read Write FPGA Control node initiates data transfer with
 minimal delay and low overhead. This method transfers only the most current data
 stored on the control or indicator of the FPGA VI.

Note

use
 FIFOs

#### What to Use

- Open FPGA
 Reference
- Read
 Write FPGA Control
- Close FPGA VI
 Reference

#### What to Do

Create the following diagram in a VI targeted to your host processor.

Customize the gray section for your unique programming goals.

[IMAGE alt='1378' src='GUID-5ECBC6FE-66AE-444D-88C3-4D3E8B3AFAC3-a5.png']

|  | Use the device name for your FPGA found in SystemDesigner to specify an FPGA target. To ensure your code runs on the FPGA, the device name input must match the FPGA device name. |
| --- | --- |
|  | Select the Open FPGA Reference node and select a mode of assigning an FPGA bitfile or application on the Item tab. To obtain a bitfile, you must compile FPGA code into a bitfile. |
|  | Select the controls or indicators in the FPGA VI that you want to read or write using the Read Write FPGA Control node. Resize the node to access more elements. To switch between read and write operations for an element, right-click the element and select Change to Read/Write. |
|  | Use the Close FPGA VI Reference node to close every reference the Open FPGA Reference node creates. |

Parent topic:

Storing and Transferring Data

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=data-transfer-using-fifos.html language=enus -->
## TOPIC 00012: Data Transfer Using FIFOs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `data-transfer-using-fifos.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/data-transfer-using-fifos.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: A FIFO is a data structure that holds elements in the order they are received and provides access to those elements using a first-in, first-out basis. The following illustration demonstrates the behavior of elements moving through a FIFO. The type of FIFO you create depends on the way you need to tr

Data Transfer Using FIFOs

A 
 *FIFO* is a data structure that holds elements in the order they are received and provides access to those elements using a first-in, first-out basis.

The following illustration demonstrates the behavior of elements moving through a FIFO.

[IMAGE alt='1378' src='GUID-146C7DC9-08EA-4B54-8E48-6A7197D175DF-a5.png']

The type of FIFO you create depends on the way you need to transfer data.

| Type of Data Transfer | Type of FIFO | Considerations |
| --- | --- | --- |
| Between Clock-Driven Loops | Local FIFO | You can access local FIFOs created through a resource collection (.grsc) across multiple documents in your project. To share the documents that reference that FIFO with another user, you must send the resource collection and documents. To create individual FPGA VIs within a single document that you can send to other users, use the Create FIFO node to create a local FIFO within the VI. |
| Between the host processor and the FPGA | Direct Memory Access (DMA) FIFO | Use DMA FIFOs to stream data between a host processor and the FPGA. A DMA FIFO allocates memory on both the host computer and the FPGA target yet acts as a single FIFO to take advantage of the resources of each device. |
| Between two FPGA targets or between an FPGA and non-FPGA target | Peer-to-Peer FIFO | Peer-to-peer FIFOs write data to a peer-to-peer writer FIFO on one target and read data from a peer-to-peer reader on another target. To define peer-to-peer FIFOs, use a resource collection. The writer and reader FIFOs are paired in the host VI but the actual data transfer happens directly from one target to another. |

Parent topic:

Storing and Transferring Data

Related concepts:

- Storing and Transferring Data
- Direct Memory Access (DMA) FIFOs
- DRAM on an FPGA Target

Related tasks:

- Transferring Data between a Target and Host Using FIFOs
- Transferring Data between Clock Domains Using FIFOs

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=dma-fifos.html language=enus -->
## TOPIC 00013: Direct Memory Access (DMA) FIFOs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `dma-fifos.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/dma-fifos.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Direct Memory Access (DMA) is a type of FIFO-based data transfer between an FPGA target and host processor. DMA communication consists of two DMA FIFOs: one FIFO on the host computer, and the other FIFO on the FPGA target. DMA communication provides the following benefits: Efficient separation of pr

Direct Memory Access (DMA) FIFOs

Direct Memory Access (DMA) is a type of FIFO-based data transfer between an FPGA target and host processor.

DMA communication consists of two DMA FIFOs: one FIFO on the host computer, and the other FIFO on the FPGA target.

DMA communication provides the following benefits:

- Efficient separation of processing tasks between the FPGA target and host processor, so the host processor remains free to perform operations during data transfer
- FPGA resource savings when transferring arrays of data
- FPGA resource savings by limiting the number of panel controls and indicators shared between a target and host
- Automatic synchronization for data transfers between the host and the FPGA target

You can use DMA communication for the following tasks:

- Transferring waveform data between the FPGA target and host
- Transferring large sets of data
- Data logging in systems where the target and host are continually connected, such as embedded systems
- Running algorithms, like digital signal processing, that the FPGA target processes more efficiently than the host computer

Parent topic:

Data Transfer Using FIFOs

Related concepts:

- Data Transfer Using FIFOs
- Storing and Transferring Data

Related tasks:

- Transferring Data between a Target and Host Using FIFOs

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=downloading-running-fpga-vi.html language=enus -->
## TOPIC 00014: Downloading and Running an FPGA VI

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `downloading-running-fpga-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/downloading-running-fpga-vi.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: To complete this task, you need a host VI and a compiled bitfile for the FPGA VI. Use the FPGA Host Interface nodes to download, run, and communicate with code on the FPGA. What to Use Open FPGA Reference Download FPGA VI Run FPGA VI Other FPGA Host Interface nodes Close FPGA VI Reference What to Do

Downloading and Running an FPGA VI

To complete this task, you need a host VI and a compiled bitfile for the FPGA VI.

FPGA Host Interface

#### What to Use

- Open FPGA Reference
- Download FPGA VI
- Run FPGA VI
- Other FPGA Host Interface nodes
- Close FPGA VI Reference

#### What to Do

Create the following diagram to download and run your FPGA VI to an FPGA target.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-2EEDE31D-AF88-4BF7-93C6-5C560A9BA336-a5.png']

|  | Use the device name for your FPGA found in SystemDesigner to specify an FPGA target. To ensure your code runs on the FPGA, the device name input must match the FPGA device name. To specify the FPGA bitfile you want to deploy to the target, complete the following steps: On the diagram, select the Open FPGA Reference node. On the Item tab, in the Mode section, select Run bitfile on hardware. In the File list, select a bitfile within your project or select Dynamic reference and wire the bitfile path to the bitfile path input of the Open FPGA Reference node. When you run this host VI, a reference to the FPGA application associated with the bitfile you selected opens and runs on the FPGA target you specify. |
| --- | --- |
|  | Download the FPGA VI specified in the bitfile to the FPGA target and run the VI. The Download FPGA VI and Run FPGA VI nodes replace the code on the FPGA each time you run the FPGA VI, ensuring that the FPGA VI properly resets before each execution. |
|  | Use the FPGA Host Interface nodes to interact with and send data to the FPGA. In this example, the host and the FPGA VI communicate in the following ways: Read/Write FPGA Control—The VIs write to and read from controls and indicators on their panels. DMA FIFO nodes—The VIs write to and read from a DMA FIFO on the FPGA. |
|  | Use the Close FPGA VI Reference node to close every reference the Open FPGA Reference node creates. If you don't close the reference, the FPGA VI runs until the host application stops running. |

#### Examples

Search within the programming environment to access the following installed example:
 *FPGA Host Interface*.

Related concepts:

- Host VIs
- FPGA VIs
- Execution of FPGA Code

Related tasks:

- Compiling FPGA Code
- Testing Communication between the Host VI and an FPGA VI

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=dynamic-ram.html language=enus -->
## TOPIC 00015: DRAM on an FPGA Target

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `dynamic-ram.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/dynamic-ram.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dynamic RAM (DRAM) is a type of random access memory used to store and access larger sets of data than block RAM (BRAM) or look-up tables (LUTs). DRAM is not available on all FPGA targets. Storing data in DRAM provides the following benefits: Additional space for large data sets that do not fit on t

DRAM on an FPGA Target

Dynamic RAM (DRAM) is a type of random access memory used to store and access larger sets of data than block RAM (BRAM) or look-up tables (LUTs).
 DRAM is not available on all FPGA targets.

Storing data in DRAM provides the following benefits:

- Additional space for large data sets that do not fit on the FPGA in BRAM or LUTs
- Lower latency access to memory than reading directly from the host
- Dedicated memory for data logging from embedded FPGAs that are not continuously connected to a host device

DRAM access has the following restrictions:

- Applications running on the FPGA cannot receive data from DRAM in a single clock cycle.
- Only one command can access DRAM memory at a time because DRAM requires sequential access.
- The sequential access required by DRAM prevents deterministic timing and may increase execution time.

Parent topic:

Introduction to FPGA Resources

Related concepts:

- Configurable Logic Blocks (CLBs) on an FPGA
- Block RAM (BRAM) on an FPGA
- I/O Resources on an FPGA
- Storing and Transferring Data
- Introduction to FPGA Resources

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=execution-of-fpga-code.html language=enus -->
## TOPIC 00016: Execution of FPGA Code

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `execution-of-fpga-code.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/execution-of-fpga-code.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can run FPGA code on the FPGA directly or you can run the code on the host computer to simulate running it on the FPGA. Execution on an FPGA To create code that executes on the FPGA target, you need to compile and download a bitfile (.lvbitx) to the FPGA. You create an Application document assoc

Execution of FPGA Code

You can run FPGA code on the FPGA directly or you can run the code on the host computer to simulate running it on the FPGA.

#### Execution on an FPGA

To create code that executes on the FPGA target, you need to compile and download a 
 *bitfile* (.lvbitx) to the FPGA.

You create an Application document associated with an FPGA VI to build a bitfile. The bitfile contains binary data that describes how to configure the FPGA circuit so that it performs the same function as the code in the FPGA VI. You then download this bitfile to the FPGA, and when the application runs, the bitfile reconfigures the FPGA circuit of the FPGA target. Use the FPGA Host Interface nodes to download, run, and communicate with the FPGA VI on the FPGA.

Compiling FPGA code into a bitfile can take a significant amount of time and varies depending on the size of the VI, the processor speed, and the amount of memory in the computer on which you are compiling.

#### Simulation on the Host Computer

FPGA code that executes on a host computer, in simulation, does not require compilation of the build and makes it easier and less time consuming to repeat tests until you're ready to compile and deploy to an FPGA.

Note

You can run an FPGA VI in simulation on the host to test and debug the code. When you click the 
 Run button from the panel or diagram of an FPGA VI, your code runs on the host computer rather than on the FPGA. Because the bitfile is not created and downloaded to the FPGA, you can test and debug the logic of your FPGA code more quickly. You also have access to debugging tools, such as breakpoints and probes, that you don't have access to when the code runs on an FPGA.

In addition to testing that the code in the FPGA VI works as you expect it to while you develop it, you also need to test how the FPGA code works in relation to the rest of your application. For example, you use a host VI to pass data to the FPGA VI to process. To make sure the host VI communicates as expected with the FPGA VI before you compile it, you can use the FPGA Host Interface nodes to run and communicate with the FPGA VI in simulation.

Related concepts:

- Host VIs
- FPGA VIs

Related tasks:

- Compiling FPGA Code

Related information:

- FPGA Host Interface Nodes

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=external-fpga-ip-instantiation.html language=enus -->
## TOPIC 00017: External FPGA IP Instantiation

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `external-fpga-ip-instantiation.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/external-fpga-ip-instantiation.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can instantiate external FPGA IP in your FPGA application using either component-level IP (CLIP) or the External FPGA IP Node. Component-Level IP Use component-level IP (CLIP) to import existing IP into FPGA hardware and communicate with it through the interface you create on the FPGA VI diagram

External FPGA IP Instantiation

You can instantiate external FPGA IP in your FPGA application using either component-level IP (CLIP) or the External FPGA IP Node.

Parent topic:

Integrating External FPGA IP into an FPGA Application

#### Component-Level IP

Use component-level IP (CLIP) to import existing IP into FPGA hardware and communicate with it through the interface you create on the FPGA VI diagram. Once imported, the IP runs independently and in parallel with FPGA VI execution. The IP can be in the form of either raw VHDL or intermediate files such as electronic design interchange format (EDIF) netlists.

- Run external FPGA IP in parallel with FPGA VI code.
- Execute external FPGA IP in multiple clock domains.
- Include constraints in the FPGA bitfile compilation.
- Create CLIP clocks.

Note

##### Constraints and Hierarchy

For constraints on specific ports within CLIP, you need to include macros that specify the location of the port within the overall VHDL hierarchy.

During bitfile compilation, the compiler applies the constraint by replacing the macro with its corresponding value. In addition, the compiler merges the content of the XDC constraint file you create into the top level XDC file it generates for all builds.

| Macro | Value |
| --- | --- |
| %ClipInstanceName% | The Label you specify for a CLIP instance when you create it in the Resource Collection. Note During compilation, the compiler may modify characters in the CLIP Label to ensure it adheres to VHDL syntax. |
| %ClipInstancePath% | The hierarchy from the target top-level VHDL to the CLIP top-level VHDL. |

The following XDC code is an example implementation of these macros in a constraint on a CLIP port. In this example, the port in the target top-level VHDL is a clock named clk.

```text
create_clock -period 10.000 -name %ClipInstanceName%Clk -waveform {0.000 5.000} -add [get_pins %ClipInstancePath%/clk]
```

#### External FPGA IP Node

Use the External FPGA IP Node to instantiate external FPGA IP on the diagram of an FPGA VI. The External FPGA IP Node executes within Clock-Driven Logic, which runs in a Clock-Driven Loop according to the dataflow of the VI. As part of the dataflow execution, the External FPGA IP Node gives you the ability to verify the overall application behavior and timing using the cycle-accurate simulation tools.

#### Choosing between CLIP or the External FPGA IP Node when Instantiating External FPGA IP

External FPGA IP Node

External FPGA IP Node

Use the following table to select the ideal approach for instantiating external FPGA IP.

|  | Component-Level IP | External FPGA IP Node |
| --- | --- | --- |
| Supported synthesis file types | Top-level: VHDL (.vhd) Xilinx Synthesis Technology Netlist (.ngc) EDIF Netlist (.edif, .edf, .edn) Design Checkpoint (.dcp) Xilinx Core Instance (.xci) Note XST Netlist (.ngc) files are supported only on Xilinx 7-series FPGA chips. | Top-level: VHDL (.vhd) Xilinx Synthesis Technology Netlist (.ngc) EDIF Netlist (.edif, .edf, .edn) Design Checkpoint (.dcp) Xilinx Core Instance (.xci) Note XST Netlist (.ngc) files are supported only on Xilinx 7-series FPGA chips. |
| Additional: VHDL (.vhd) Xilinx Synthesis Technology Netlist (.ngc) EDIF Netlist (.edif, .edf, .edn) Design Checkpoint (.dcp) Xilinx Core Instance (.xci) Data (.data) Xilinx Distributed Arithmetic FIR Filter Coefficient (.coe) Block RAM Memory Map (.bmm) Xilinx Design Constraints (.xdc) | Additional: VHDL (.vhd) Xilinx Synthesis Technology Netlist (.ngc) EDIF Netlist (.edif, .edf, .edn) Design Checkpoint (.dcp) Xilinx Core Instance (.xci) Data (.data) Xilinx Distributed Arithmetic FIR Filter Coefficient (.coe) Block RAM Memory Map (.bmm) |  |
| Support for simulation | No | Yes |
| Supported simulation file types | N/A | Top-level: VHDL (.vhd) |
| Additional: VHDL (.vhd) Xilinx Distributed Arithmetic FIR Filter Coefficient (.coe) Memory Initialization File (.mif) Configuration (.cfg) Xilinx Core Instance (.xci) |  |  |
| Supported data types | Boolean Boolean array Integer Fixed-point Floating-point | Boolean Boolean array Integer Fixed-point Floating-point |
| Execution model | Executes parallel to, and independent of, the dataflow of an FPGA VI | Executes within Clock-Driven Logic, which runs in a Clock-Driven Loop according to the dataflow of an FPGA VI |
| Place of declaration | Declared in a project within an EIP document and instantiated within a Resource Collection | Declared in a project within an EIP document and instantiated when placed on the FPGA VI diagram as an IPIN |
| Languages that support instantiation | G Dataflow Clock-Driven Logic | Clock-Driven Logic |
| Support for multiple clock domains | Maximum number of clocks defined by FPGA | Maximum of two clocks: a Clock-Driven Loop clock and an FPGA-derived clock, where the derived clock executes at a rate that is an integer multiple of the Clock-Driven Loop clock |
| Support for using clocks from the IP as clocks that drive a Clock-Driven Loop | Yes | No |
| Support for VHDL generics | Yes | Yes |
| Support for constraints in the FPGA bitfile compilation | Yes | No |

Related concepts:

- Clocks and Timing on an FPGA

Related tasks:

- Instantiating External FPGA IP in an FPGA Application using CLIP
- Instantiating External FPGA IP in an FPGA Application using the External FPGA IP Node

Related information:

- nihelp://cdl-prog/clock-driven-logic/

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-data-storage-transfer.html language=enus -->
## TOPIC 00018: Storing and Transferring Data

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-data-storage-transfer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-data-storage-transfer.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Store and transfer data on an FPGA using resource items like FIFOs, memory items, FPGA registers, or handshake items. You can also transfer data on an FPGA using panel controls or indicators. Use the following table to determine the best type of data storage and transfer for your application. Type o

Storing and Transferring Data

Store and transfer data on an FPGA using resource items like FIFOs, memory items, FPGA
 registers, or handshake items. You can also transfer data on an FPGA using panel
 controls or indicators.

Use the following table to determine the best type of data storage and transfer for your application.

| Type of Data Storage or Transfer | Use Case |
| --- | --- |
| FIFO | Use a FIFO when you need to store multiple sequential data samples. FIFOs support lossless data transfer. |
| Memory Item | Use a memory item when you need to access data without respect to the sequence in which the data is written to memory. Unlike FIFOs, all units of data within a memory item are readable at any time. You can also store data in memory items prior to run time, called pre-initializing data, to use the memory as a read-only reference. Pre-initialized data can save logic resources and computation time. |
| FPGA Register | Use a register when you need to hold only one unit of the specified data size at one time. Data transfer using registers is often lossy, but registers consume fewer FPGA resources than FIFOs when storing equivalent sizes of data. Use registers for synchronization, and pipelining. |
| Handshake Item | Use a handshake item when you want lossless data transfer between multiple clock domains inside the FPGA. |
| Panel Controls and Indicators | Use panel controls and indicators to transfer the most current data between the FPGA and the host. This method is useful for small and frequent data transfers that require little overhead. |

Related concepts:

- Data Transfer Using FIFOs
- Data Transfer Using Memory Items
- Data Transfer Using FPGA Registers

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-io-blocks.html language=enus -->
## TOPIC 00019: I/O Resources on an FPGA

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-io-blocks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-io-blocks.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Input and output (I/O) resources on an FPGA target are physical structures that allow you to connect an FPGA target to other devices in your system. I/O resources translate analog or digital signals to or from a digital value so that you can process the signals using an FPGA target. The I/O resource

I/O Resources on an FPGA

Input and output (I/O) resources on an FPGA target are physical structures that allow you to connect an FPGA target to other devices in your system.
 I/O resources translate analog or digital signals to or from a digital value so that you can process the signals using an FPGA target.

The I/O resources available in an FPGA VI correspond to physical I/O resources available on the FPGA target. When an FPGA VI runs on an FPGA target, the VI processes I/O signals with the speed and determinism of the FPGA target.

In LabVIEW, FPGA I/O resources correspond both to system connectors, like the PXI backplane or Real-Time System Integration (RTSI) connectors, and to internal lines that provide I/O between configurable and non-configurable parts within the FPGA. For component-level IP (CLIP), I/O resources allow communication between the CLIP and LabVIEW code targeted to the FPGA.

Note

Parent topic:

Introduction to FPGA Resources

Related concepts:

- Configurable Logic Blocks (CLBs) on an FPGA
- Block RAM (BRAM) on an FPGA
- Introduction to FPGA Resources

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-memory-items.html language=enus -->
## TOPIC 00020: Data Transfer Using Memory Items

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-memory-items.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-memory-items.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: A memory item is a data storage container of a specified size, used to store and reference data samples on an FPGA. Unlike reading from a FIFO or register, you can read data from any location within a memory item, called an address, without respect to the order in which the data was written. You can

Data Transfer Using Memory Items

A 
 *memory item* is a data storage container of a specified size, used to store and reference data samples on an FPGA. 
 Unlike reading from a FIFO or register, you can read data from any location within a memory item, called an address, without respect to the order in which the data was written. You can create memory items in a resource collection or from within a document targeted to an FPGA.

You can read and write data to memory items on the FPGA at run time. You can also 
 *pre-initialize data* which stores data in memory items, as ROM or RAM, prior to run time. You must always pre-initialize ROM. Pre-initialized data can save logic resources and computation time.

You can implement memory items using look-up tables, block RAM, or dynamic RAM. The best memory item implementation for your system depends on the needs of your particular application.

| Memory Item Implementation | Advantages | Recommendations |
| --- | --- | --- |
| Look-up tables (LUTs) | Allow access to a memory item within a Clock-Driven Loop Provide an alternative implementation of memory when you have limited block RAM remaining | Implement memory in LUTs when you need to read data from a memory item during the same cycle as the one in which you invoke the memory item. Implementing memory in LUTs consumes logic resources and reduces the number of logic resources available for data processing. |
| Block RAM (BRAM) | Compiles at a high clock rate relative to other types of memory items Does not consume FPGA logic resources | Implement memory items in BRAM to write data in one clock domain and read the data from the same clock domain. Use memory items implemented in BRAM to conserve LUTs on your FPGA. |
| Dynamic RAM (DRAM) | Provides a larger storage capacity than memory items implemented in LUTs or BRAM Does not consume FPGA logic resources | Implement memory items in DRAM when you need to store large sets of data that are not immediately required by other parts of your system. DRAM is ideal for storing large data sets in embedded applications. |

Parent topic:

Storing and Transferring Data

Related concepts:

- Storing and Transferring Data
- Configurable Logic Blocks (CLBs) on an FPGA
- Block RAM (BRAM) on an FPGA
- DRAM on an FPGA Target

Related tasks:

- Transferring Data Using a Memory Item

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-registers.html language=enus -->
## TOPIC 00021: Data Transfer Using FPGA Registers

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-registers.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-registers.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: On an FPGA, registers synchronize sections of code that execute at different rates so that data can move between the sections. A register is a buffer that stores one data unit at a time. The number of bits stored in a register varies based on the data type specified for the register. For transferrin

Data Transfer Using FPGA Registers

On an FPGA, registers synchronize sections of code that execute at different rates so that data can move between the sections.

A 
 *register* is a buffer that stores one data unit at a time. The number of bits stored in a register varies based on the data type specified for the register. For transferring any given data type, registers use fewer resources than FIFOs implemented in LUTs, but registers do not guarantee lossless data transfer. Use registers when you need to store a single unit of data at a time and do not require lossless transfer.

Registers support the following processes:

- Holding state between iterations of a loop
- Synchronizing I/O
- Handshaking data between clock domains
- Pipelining
- Communicating with a host VI

Parent topic:

Storing and Transferring Data

Related concepts:

- Storing and Transferring Data

Related tasks:

- Transferring Data between Clock Domains Using Registers
- Transferring Data between Clock Domains Using FIFOs
- Transferring Data Using a Memory Item

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-supported-data-types.html language=enus -->
## TOPIC 00022: Supported Data Types

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-supported-data-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-supported-data-types.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA VIs support the following data types, which are a subset of the data types supported by LabVIEW NXG: 8-bit signed and unsigned integer numerics 16-bit signed and unsigned integer numerics 32-bit signed and unsigned integer numerics 64-bit signed and unsigned integer numerics Boolean Fixed-point

Supported Data Types

FPGA VIs support the following data types, which are a subset of the data types supported
 by LabVIEW NXG:

- 8-bit signed and unsigned integer numerics
- 16-bit signed and unsigned integer numerics
- 32-bit signed and unsigned integer numerics
- 64-bit signed and unsigned integer numerics
- Boolean
- Fixed-point
- Complex fixed-point
- Single-precision floating-point
- Double-precision floating-point
- Clusters of supported data types
- Up to three-dimensional arrays of supported data types

Related concepts:

- Using Arrays in FPGA Applications

Related information:

- Data Type Reference
- Introduction to Fixed-Point Numbers

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=fpga-vis.html language=enus -->
## TOPIC 00023: FPGA VIs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/fpga-vis.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: An FPGA VI is a VI that you target to an FPGA. Designate a top-level FPGA VI within an Application document (.gcomp) that represents a bitfile. The top-level FPGA VI serves as the container for your overall FPGA application. Place all of the code that makes up your FPGA application either directly o

FPGA VIs

An FPGA VI is a VI that you target to an FPGA.

Designate a top-level FPGA VI within an Application document (.gcomp) that represents a bitfile. The top-level FPGA VI serves as the container for your overall FPGA application. Place all of the code that makes up your FPGA application either directly on the diagram of the FPGA VI, or within subdocuments located on the diagram of the FPGA VI. This code can include Clock-Driven Logic. You compile the FPGA application to create a bitfile, so any code referenced within the top-level FPGA VI compiles as part of the FPGA application.

Because the resources available to a program running on an FPGA differ from those available on the host, an FPGA VI includes only palette objects and data types that are compatible with an FPGA. For example, the palette in an FPGA VI displays nodes and terminals that receive or generate FPGA resource references. The palette in an FPGA VI also includes the Clock-Driven Loop, which you place around the majority of the code on the diagram to control the execution speed of that code on the FPGA.

#### Examples

Search within the programming environment to access the following lessons:
 *Programming with Clock-Driven Logic*

Related concepts:

- Differences between Host and FPGA VIs

Related information:

- G Dataflow (G)
- Clock-Driven Loop
- Language Integration in LabVIEW

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=host-fpga-vis.html language=enus -->
## TOPIC 00024: Differences between Host and FPGA VIs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `host-fpga-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/host-fpga-vis.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: The resources on a host and an FPGA make each target better suited to different types of programming tasks. The programming objects available in a host VI and an FPGA VI vary to match to the purpose of the VI. This document-sensitive variation makes it easier and quicker for you to create code that

Differences between Host and FPGA VIs

The resources on a host and an FPGA make each target better suited to different types of programming tasks. 
 The programming objects available in a host VI and an FPGA VI vary to match to the purpose of the VI. 
 This document-sensitive variation makes it easier and quicker for you to create code that is compatible for the target you want a VI to run on.

The following table describes the differences between a host VI and an FPGA VI.

| Characteristic | Host VI | FPGA VI |
| --- | --- | --- |
| Purpose | Logging data Simulating, testing, and deploying FPGA code | Containing the code that makes up an FPGA application, including Clock-Driven Logic |
| Target | PC or controller | FPGA |
| Palette Objects | Extensive G palette | Limited G palette that includes: Clock-Driven Loop Nodes, terminals, and constants compatible with FPGAs Controls and indicators compatible with FPGAs |
| Supported Data Types | All | Numeric, Boolean, arrays, clusters, and FPGA resource references |

Related concepts:

- Host VIs
- FPGA VIs

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=host-vis.html language=enus -->
## TOPIC 00025: Host VIs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `host-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/host-vis.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: A host VI is a VI that you target to a processor, often a PC or a controller, within your hardware device. VIs that run on a host typically have access to larger amounts of memory. Thus, a host VI doesn't have the same resource constraints as a VI that runs on an FPGA. Because you can use host VIs t

Host VIs

A host VI is a VI that you target to a processor, often a PC or a controller, within your hardware device.

VIs that run on a host typically have access to larger amounts of memory. Thus, a host VI doesn't have the same resource constraints as a VI that runs on an FPGA. Because you can use host VIs to complete a wide array of resource-heavy programming tasks in an application, the palettes on a host VI provide a broad range of data types and nodes to support these programming tasks.

Tasks for which a host VI is well suited include:

- Processing, logging, and analyzing data on the host.
- Testing and simulating FPGA code in a host VI before implementing it on an FPGA.

Related concepts:

- Differences between Host and FPGA VIs

Related information:

- G Dataflow (G)
- Language Integration in LabVIEW

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=increasing-fpga-execution.html language=enus -->
## TOPIC 00026: Customizing the Execution Rate of Clock-Driven Loops

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `increasing-fpga-execution.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/increasing-fpga-execution.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: If none of the FPGA target base clocks meets the timing objectives of your Clock-Driven Loop or Clock-Driven Logic document, create a derived clock that scales the frequency of the base clocks to achieve faster or slower execution rates. Complete the following steps to create and use a derived clock

Customizing the Execution Rate of
 Clock-Driven Loops

If none of the FPGA target base clocks meets the timing objectives of your
 Clock-Driven Loop or Clock-Driven Logic document, create a derived clock that scales the
 frequency of the base clocks to achieve faster or slower execution rates.

Complete the following steps to create and use a derived clock.

1. In the Application document targeted to the FPGA target, open or create a resource collection.
2. In the Resource Collection document, create a new derived clock.
3. Optional: 
 Rename the clock to more easily differentiate between clocks on the diagram. 
 By default, the name is DerivedClock.
4. On the 
 Item tab, click 
 Change clock speed.
5. In the 
 Change Clock Speed dialog box, specify the new clock speed. 
 OptionDescriptionSet by frequency
 Use this option if you know the timing objective of your code according to the frequency, measured in MHz.Set by period
 Use this option if you know the timing objective of your code according to the length of one period, measured in ns. 
 If your entry falls outside the range of the slider, LabVIEW NXG automatically adjusts your entry to the closest acceptable number.
6. Click 
 OK.
7. Use the derived clock to drive a Clock-Driven Loop and control the timing of your code on the FPGA. 
 You can select a derived clock from a clock constant in an FPGA VI or Clock-Driven Logic document.

Parent topic:

Using Clock-Driven Loops to Run Code at Higher Rates with Lower Latency

Related concepts:

- Clocks and Timing on an FPGA

Related tasks:

- Using Clock Domains to Control the Execution Rate of Clock-Driven Loops

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=instantiate-ip-in-fpga-using-clip.html language=enus -->
## TOPIC 00027: Instantiating External FPGA IP in an FPGA Application using CLIP

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `instantiate-ip-in-fpga-using-clip.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/instantiate-ip-in-fpga-using-clip.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate external FPGA IP into your FPGA application by creating a component-level IP instance and transferring data between the component-level IP and your FPGA VI. Before you can add component-level IP (CLIP) to your FPGA application, you need to declare your IP by creating an External FPGA IP do

Instantiating External FPGA IP in an FPGA Application using CLIP

Integrate external FPGA IP into your FPGA application by creating a component-level IP instance and transferring data between the component-level IP and your FPGA VI.

Creating an External FPGA IP Document from IP Source Files

Creating an External FPGA IP Document from an IP-XACT File

The EIP document declares external FPGA IP for integration into your FPGA application. When you create a CLIP instance, you map it to an EIP file. As a result, the ports defined by the IP files declared in the EIP document become clock and I/O constants in the FPGA VI palette. Add these I/O constants to your FPGA VI diagram to create the interface that interacts with the CLIP when running on the FPGA target. You can create and configure multiple CLIP instances derived from the same EIP file without affecting other CLIP instances.

1. In the Application document for your FPGA target, open or add a Resource Collection.
2. In the Resource Collection, expand the 
 Component-level IP section, and click 
 Create New to create a component-level IP instance.
3. Click the empty 
 Component-level IP instance to display its settings on the 
 Item tab.
4. Under 
 Component-Level IP declaration, select an EIP file. 
 The name of the 
 Component-level IP instance changes to reflect the configuration of the EIP file you select.
5. Click on the 
 Component-level IP instance again to display its settings on the 
 Item tab. 
 The 
 Item tab displays port configurations imported from the EIP file. The menus and signals available for configuration reflect the configuration of your EIP file. You can override any configurations from the EIP file without overwriting it.
6. If your IP has generics, configure them for each CLIP instance.
  1. In the 
 Item tab for a CLIP instance, locate and expand the 
 Generics section.
  2. Edit the value for a generic by entering any string value in the text box. 
 The string value must correspond to the generic type. For example, enter a string of 
 True or 
 False for a boolean generic.
7. Configure 
 Clip clock mapping. 
 The 
 Item tab for the selected CLIP instance displays input clocks under the CLIP clock mapping section. You can configure each input clock as one of the following: 
 OptionDescriptionDefer to target
 Select this option to map the CLIP clock to a base clock on the FPGA target. You can select the base clock in SystemDesigner: 
 Click on the Application document for your FPGA target to display configuration settings on the 
 Item tab.Under 
 Resource Association, click on the pull-down menu next to the CLIP clock you want to configure and select a base clock on your FPGA target.Derived clock
 Select any derived clock that you have created in the Resource Collection.
8. Configure 
 IO data type and synchronization registers. 
 This section displays the ports configured as 
 Data and 
 Enable in the EIP file.
  1. Configure each data signal as required for your application. You can override the settings derived from the EIP file without overwriting the EIP file.
  2. Configure 
 Synchronization registers. 
 Each synchronization register adds a delay of a clock cycle before the FPGA IP code receives the value from Read I/O or Write I/O.
 If you place the CLIP I/O constant on the diagram of the FPGA VI, configure 
 Synchronization registers in relation to the top-level clock of your FPGA VI.
 If you place the CLIP I/O constant in Clock-Driven Logic, configure 
 Synchronization registers in relation to the Clock-Driven Loop clock.
9. Create the interface between the CLIP and an FPGA VI.
  1. Open the FPGA VI or a Clock-Driven Logic document and display the diagram.
  2. Navigate to 
 Project Items»Software»Application»Resource Collection»Component-level IP»CLIP instance to locate the clocks and I/O for your CLIP instance.
  3. Select a clock or I/O and add it to the FPGA VI diagram. 
 You can place CLIP I/O constants inside or outside Clock-Driven Logic, but you must pay attention to whether the CLIP crosses clock domains. Use synchronization registers to add a delay of a clock cycle before the FPGA IP receives the value from Read I/O or Write I/O.
  4. Wire the output of a CLIP I/O constant to Read I/O, Write I/O, or Read/Write I/O. 
 For example, you can wire an output to Read/Write I/O as shown in the image below.
 
[IMAGE alt='1378' src='GUID-B1229C91-4D0A-4EA7-BCD5-8D01255B0E77-a5.png'] 

 org.dita.html5/xsl/topic.xsl 455Note Because the inputs and outputs of CLIP reflect the port configurations you make in the EIP document, your results may not match the image above.

Parent topic:

Integrating External FPGA IP into an FPGA Application

Related concepts:

- External FPGA IP Instantiation
- Clocks and Timing on an FPGA
- Storing and Transferring Data

Related tasks:

- Customizing the Execution Rate of Clock-Driven Loops
- Using Clock Domains to Control the Execution Rate of Clock-Driven Loops

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=instantiate-ip-in-fpga-using-eip-node.html language=enus -->
## TOPIC 00028: Instantiating External FPGA IP in an FPGA Application using the External FPGA IP Node

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `instantiate-ip-in-fpga-using-eip-node.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/instantiate-ip-in-fpga-using-eip-node.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate external FPGA IP into your FPGA application by placing the External FPGA IP Node into Clock-Driven Logic within your FPGA VI. Before you can add the External FPGA IP Node to your FPGA application, you need to declare your IP by creating an External FPGA IP document. Refer to Creating an Ex

Instantiating External FPGA IP in an FPGA Application using the External FPGA IP Node

Integrate external FPGA IP into your FPGA application by placing the External FPGA IP Node into Clock-Driven Logic within your FPGA VI.

External FPGA IP Node

Creating an External FPGA IP Document from IP Source Files

Creating an External FPGA IP Document from an IP-XACT File

1. Locate the EIP file in the 
 Project Files tab and drag it to the diagram. 
 The EIP file becomes the External FPGA IP Node when you place it on the diagram.
2. Wire the External FPGA IP Node according to the requirements of your application. 
 Note the following behaviors of the External FPGA IP Node: 
 The inputs and outputs of the External FPGA IP Node correspond to signals defined in the External FPGA IP document with the following exceptions: 
 The External FPGA IP Node does not display reset signals.The External FPGA IP Node does not display clock signals unless you configure one clock signal as the 
 Associated clock for another. For example, if you select 
 ClkA as the 
 Associated clock for 
 ClkB, the External FPGA IP Node will display 
 ClkB as an input. You can wire a derived clock to that input.The data type of each input and output is the data type you specify for it in the parent EIP document.
3. (Optional) Select the External FPGA IP Node. On the 
 Item tab, configure inputs and outputs according to the requirements of your application. 
 You can change the configuration of an External FPGA IP Node instance without affecting the EIP document or any other External FPGA IP Node or CLIP instance built from the same EIP document.

The following image shows an example of the External FPGA IP Node wired inside a Clock-Driven Loop.

[IMAGE alt='1378' src='GUID-D4BE4DD0-6D51-42ED-A616-85E00E10229C-a5.png']

Note

External FPGA IP Node

Parent topic:

Integrating External FPGA IP into an FPGA Application

Related concepts:

- External FPGA IP Instantiation

Related tasks:

- Using Clock Domains to Control the Execution Rate of Clock-Driven Loops

Related information:

- nihelp://cdl-prog/clock-driven-logic/

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=integrate-external-ip-into-fpga.html language=enus -->
## TOPIC 00029: Integrating External FPGA IP into an FPGA Application

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `integrate-external-ip-into-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/integrate-external-ip-into-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: By integrating external FPGA IP into an FPGA application, you can reuse existing FPGA code to implement a wide range of algorithms that are optimized for FPGAs. The Xilinx CORE Generator IP palette contains a library of IP blocks that you can incorporate into the dataflow of your FPGA VI without the

Integrating External FPGA IP into an FPGA Application

By integrating external FPGA IP into an FPGA application, you can reuse existing FPGA code to implement a wide range of algorithms that are optimized for FPGAs.

Note

1. Create or acquire IP for integration. 
 For IP source files that are not VHDL, National Instruments recommends that you integrate files created using the same version of Vivado shipped with your version of NXG software. Refer to the [support document](http://www.ni.com/r/7mn3ce) at ni.com for more information about the Vivado version shipped with each version of NXG software.
 You declare the IP in your project using the External FPGA IP document. The External FPGA IP document supports the following file types:
 File Type
 File Extension
 Top-Level Synthesis
 Additional Synthesis
 Top-Level Simulation
 Additional SimulationVHSIC Hardware Description Language (VHDL)
 .vhd
 Yes
 Yes
 Yes
 Yes
 Xilinx Synthesis Technology (XST) Netlist 
 org.dita.html5/xsl/topic.xsl 455Note XST Netlist files are supported only on Xilinx 7-series FPGA chips.
 .ngc
 Yes
 Yes
 No
 No
 Electronic Data Interchange Format (EDIF) Netlist
 .edif, 
 .edf, 
 .edn
 Yes
 Yes
 No
 No
 Design Checkpoint (DCP)
 .dcp
 Yes
 Yes
 No
 No
 Xilinx Core Instance (XCI)
 .xci
 Yes
 Yes
 No
 Yes
 Data
 .data
 No
 Yes
 No
 No
 Coefficient
 .coe
 No
 Yes
 No
 No
 Block RAM Memory Map (BMM)
 .bmm
 No
 Yes
 No
 No
 Xilinx Design Constraints (XDC)
 .xdc
 No
 Yes
 No
 No
 Memory Initialization File (MIF)
 .mif
 No
 No
 No
 Yes
 Configuration
 .cfg
 No
 No
 No
 Yes
 Verilog
 .v
 The FPGA compile server does not support Verilog files. Synthesize Verilog files to a Netlist before importing.
2. Declare the IP in your project using one of the following procedures: 
 
 org.dita.html5/xsl/topic.xsl 455Note The EIP document supports IP-XACT files exported from Xilinx Vivado, but you may have varying results when importing files from other vendors.
  - Create an External FPGA IP document from IP source files — Integrate IP into your FPGA application by creating an External FPGA IP document that declares IP files in a project for instantiation as component-level IP (CLIP) or an External FPGA IP Node.
  - Create an External FPGA IP document from an IP-XACT file — Integrate IP into your FPGA application by importing IP descriptions from an IP-XACT XML file into an EIP document, declaring IP files in a project for use as component-level IP (CLIP) or the External FPGA IP Node.
3. [Select an approach for instantiating external FPGA IP](/csh?topicname=external-fpga-ip-instantiation.html)—You can instantiate external FPGA IP in your FPGA application using either component-level IP (CLIP) or the External FPGA IP Node.
4. Instantiate the IP using one of the following procedures:
  - Instantiate external FPGA IP in an FPGA application using the External FPGA IP Node — Integrate external FPGA IP into your FPGA application by placing the External FPGA IP Node into Clock-Driven Logic within your FPGA VI.
  - Instantiate external FPGA IP in an FPGA application using CLIP — Integrate external FPGA IP into your FPGA application by creating a component-level IP instance and transferring data between the component-level IP and your FPGA VI.

After completing IP integration, you can run the FPGA VI in simulation or compile and deploy to an FPGA target.

Related concepts:

- Execution of FPGA Code

Related tasks:

- Compiling FPGA Code

Related information:

- nihelp://design/application-deployment/

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=intro-fpga-resources.html language=enus -->
## TOPIC 00030: Introduction to FPGA Resources

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `intro-fpga-resources.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/intro-fpga-resources.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every FPGA has a set number of programmable logic, routing, I/O, and memory resources. The compiler uses these resources to implement code on the FPGA. The programmable resources on an FPGA are located at regular intervals across the chip, which allows for short paths between the resources. Short pa

Introduction to FPGA Resources

Every FPGA has a set number of programmable logic, routing, I/O, and memory resources. The compiler uses these resources to implement code on the FPGA.

The programmable resources on an FPGA are located at regular intervals across the chip, which allows for short paths between the resources. Short paths between resources reduce the minimum execution time that code running on the FPGA target requires. Since there are multiple instances of each resource on an FPGA, multiple concurrent processes can run on the same device at the same time, while minimizing resource conflicts. The following illustration shows a simplified example of programmable resources on an FPGA.

[IMAGE alt='1378' src='GUID-E70776A9-4DA6-41D4-8892-4E98941005E2-a5.png']

1. Configurable logic blocks (CLBs)—Basic repeating units of logic on the FPGA.
2. Programmable routing—Interconnecting wires that join CLBs together to build complex logic. Programmable routing also joins I/O blocks to CLBs and joins CLBs to memory resources.
3. I/O resources—Analog and digital inputs and outputs that connect the FPGA to external signals.

An FPGA must receive configuration instructions before it can perform any computation. The compiler generates configuration instructions for the FPGA that implements your code. When you compile your application, the compiler arranges the programmable resources on the FPGA to create a circuit that performs the following actions as shown in the illustration above:

1. Receives inputs from the I/O blocks
2. Processes the inputs using CLBs
3. Passes the processed inputs back to the I/O blocks as outputs

The compiler uses different combinations of available FPGA resources to implement the same code depending on the performance directives you set in your code and the resources available on your FPGA.

Related concepts:

- Storing and Transferring Data
- Configurable Logic Blocks (CLBs) on an FPGA
- I/O Resources on an FPGA

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=monitoring-bitfile-compilation.html language=enus -->
## TOPIC 00031: Monitoring the Compilation of a Bitfile

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `monitoring-bitfile-compilation.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/monitoring-bitfile-compilation.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: An FPGA target contains a limited number of resources. If a bitfile requires more resources than the FPGA target has available, the compilation of the bitfile fails. Use the estimated and actual number of resources a bitfile uses to determine changes you need to make to code. Compilation can take a

Monitoring the Compilation of a Bitfile

An FPGA target contains a limited number of resources. If a bitfile requires more resources than the FPGA target has available, the compilation of the bitfile fails. 
 Use the estimated and actual number of resources a bitfile uses to determine changes you need to make to code.

Compilation can take a long time, during which you can monitor the process and cancel a compilation if you encounter severe errors. You do not have to wait for the entire process to finish.

After you begin the process of [compiling your FPGA code](/csh?topicname=compiling-fpga-code.html), complete the following steps to monitor the compilation status:

1. In the Build Queue tab, click the
 Open button ([IMAGE alt='1378' src='GUID-2A596B47-A78F-4862-97C7-A861DA24914F-a5.png']) to monitor the status of the
 bitfile during compilation. 
 If the bitfile is unavailable, the Open button is not enabled.org.dita.html5/xsl/topic.xsl 455Note Do not change any code in your FPGA application
 during the diagram analysis stage of compilation. Any changes you make to
 code during the diagram analysis stage may be reflected in the bitfile. If
 you want to continue working on code while you wait for the compilation to
 finish, do so after the diagram analysis stage.
2. After the synthesizing stage of compilation, click each resource listed under 
 Estimated resource usage to view the estimated FPGA resources that your bitfile requires. 
 If your bitfile is estimated to need more resources than the FPGA target contains, cancel the compilation and revise your code. After you cancel a compilation, you must begin a new compilation to compile your updated code.
3. Click the resources listed under 
 Actual resource usage to see the total number of each resource used on the FPGA target. 
 If your compilation fails, you can use the resource usage information to investigate errors or determine changes you need to make in your code. For example, if your bitfile uses all LUTs from the FPGA, but few block RAMs, you may need to change the way you implement memory or FIFOs in your code.

After the compilation is complete, proceed with one of the following tasks:

- If the 
 Timing Violations tab displays timing violations, fix the timing violations and recompile the bitfile. Refer to Resolving Timing Violations on the FPGA for tips to fix timing violations.
- If the 
 Timing Violations tab displays no timing violations, you can deploy the bitfile to an FPGA. Refer to [Downloading and Running an FPGA VI](/csh?topicname=downloading-running-fpga-vi.html) for help downloading and running the compiled bitfile on an FPGA. When you run the bitfile on an FPGA, the bitfile reconfigures the FPGA circuit of the FPGA by transferring all the code and performance requirements of your application to the FPGA.

Parent topic:

Compiling FPGA Code

Related tasks:

- Compiling FPGA Code

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=resolving-timing-violations-fpga.html language=enus -->
## TOPIC 00032: Resolving Timing Violations on the FPGA

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `resolving-timing-violations-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/resolving-timing-violations-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Timing violations occur when the execution time requested by sections of code is shorter than execution time the bitfile achieves after compiling. If the Timing Violations tab displays timing violations after you build a bitfile, you must resolve the timing violations and rebuild the bitfile before

Resolving Timing Violations on the FPGA

Timing violations occur when the execution time requested by sections of code is shorter than execution time the bitfile achieves after compiling.If the 
 Timing Violations tab displays timing violations after you build a bitfile, you must resolve the timing violations and rebuild the bitfile before deploying the bitfile to the FPGA.

Resolve timing violations using the following steps.

1. Double-click a bitfile in the 
 Build Queue tab.
2. In the 
 Build Errors section, click 
 Investigate to view timing violations in your bitfile. 
 The 
 Timing Violations tab displays a row for each section of your code that failed to meet the timing requirements specified by your bitfile. Each section of your code that contains timing errors is called a 
 *critical path*. When possible, the 
 Timing Violations tab reports timing violations for individual objects inside of a critical path. 
 The following image shows how the 
 Timing Violations tab displays timing violations. 
 
[IMAGE alt='1378' src='GUID-42292014-0B79-4CB0-89ED-C45F78DC1BF4-a5.png']
3. Double-click each critical path or object in the 
 Timing Violations tab to highlight the critical path or object on the diagram. Update paths with the longest timing delays first using the following strategies. 
 org.dita.html5/xsl/topic.xsl 455Note You can rebuild your bitfile after implementing each strategy to test the impact of your code revisions on the original timing violations.
  - Reduce long node paths inside each Clock-Driven Loop . 
 Each node takes a certain amount of time to execute, so use fewer nodes inside each Clock-Driven Loop by simplifying the logic of the code, if possible. Long node paths inside a Clock-Driven Loop result in timing delays when compiled on the FPGA. Also, avoid deeply nested Case Structures to reduce the length of paths inside a Clock-Driven Loop.
  - Use pipelining. 
 Pipelining is the process of restructuring one long section of code into several shorter sections that run in parallel. Pipelining takes advantage of the parallel processing capabilities of the FPGA to increase efficiency of sequential code. To implement pipelining, divide code into discrete steps and wire the inputs and outputs of each step to Feedback Nodes in the Clock-Driven Loop. The following image shows code organized into subCDLs and pipelined through Feedback Nodes. [IMAGE alt='1378' src='GUID-ACB6025D-39B2-4106-A03B-EFE7BDCB921B-a5.png']
  - Use smaller data types. 
 Use the smallest data type possible for terminals to decrease the size and increase the speed of an FPGA VI. For example, if a terminal uses a 32-bit integer data type by default, but you know the terminal will never contain a number above 255, change the data type of the terminal to an 8-bit integer to use fewer FPGA resources.
  - Reduce the clock rate of Clock-Driven Loops that contain critical paths. 
 If your application does not explicitly depend on completing each clock cycle at exactly the rate specified, reduce the frequency of the clock that drives the components that failed to meet timing requirements.
  - Rebuild the bitfile. 
 If your failed compilation misses the required throughput time by only a few nanoseconds, try rebuilding your bitfile. Each build of a bitfile does not always produce identical results on the FPGA, so rebuilding sometimes resolves minor timing violations. If your bitfile continues to return timing violations, repeat the previous strategies. If you cannot eliminate timing violations, consider moving parts of your application to the host processor.

Parent topic:

Compiling FPGA Code

#### Resolving Optimized or Non-Diagram Logic Timing Violations

The 
 Timing Violations tab reports errors under 
 Optimized or Non-Diagram Logic when the location of the timing violation in the compiled code cannot be determined. Timing violations for Clock-Driven Logic code and Optimized FPGA VI code often appear under 
 Optimized or Non-Diagram Logic in the 
 Timing Violations tab.

Choose the following strategy to resolve optimized or non-diagram logic timing violations, based on the type of code you compile in the bitfile.

- For Clock-Driven Logic code, use the strategies listed in 
 Resolving Timing Violations on the FPGA . 
 The compiler often implements common operations (i.e. Add, Multiply) in dedicated resource blocks to optimize the performance of the code. As a result, part of your critical path from a Clock-Driven Logic document or a Clock-Driven Loop often appears under 
 Optimized or Non-Diagram Logic.
- For Optimized FPGA VI code, revise the 
 FPGA Estimates configuration. 
 On the 
 Document tab, select 
 FPGA Estimates and increase the 
 Routing Margin and 
 Clock Rate to improve the timing in the code. If the 
 Optimized or Non-Diagram Logic object still shows a large delay after you revise the 
 FPGA Estimates configuration, try revising your Optimized FPGA VI algorithm. Verify that the clock rate you requested for your Optimized FPGA VI matches the clock rate of the Clock-Driven Loop or Clock-Driven Logic document that calls the Optimized FPGA VI.

Note

<your_compilation>

After you resolve all timing violations and rebuild the bitfile without errors, you can deploy the bitfile to an FPGA. Refer to [Downloading and Running an FPGA VI](/csh?topicname=downloading-running-fpga-vi.html) for help downloading and running the compiled bitfile on an FPGA. When you run the bitfile on an FPGA, the bitfile reconfigures the FPGA circuit of the FPGA by transferring all the code and performance requirements of your application to the FPGA.

Related tasks:

- Compiling FPGA Code

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=sampling-probes-cdl.html language=enus -->
## TOPIC 00033: Sampling Probes Tab

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `sampling-probes-cdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/sampling-probes-cdl.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `reference`
- source_description: In a Clock-Driven Loop on the diagram of an FPGA VI or in a Clock-Driven Logic (CDL) document, you can check intermediate values and view changes in signal data over time by right-clicking a wire and selecting Add sampling probe. Use the Sampling Probes tab to interact with the data collected from s

Sampling Probes Tab

In a Clock-Driven Loop on the diagram of an FPGA VI or in a Clock-Driven Logic (CDL)
 document, you can check intermediate values and view changes in signal data over time by
 right-clicking a wire and selecting Add sampling probe. Use
 the **Sampling Probes** tab to interact with the data collected from sampling
 probes.

[IMAGE alt='1378' src='GUID-D2AF43B1-6B6E-4C2F-A3D5-D1F778F62472-a5.png']

1. To view data from sampling probes, open the Sampling Probes tab using the Tool Launcher. Select the FPGA to which you targeted the application as the Sampling source. In the list on the left-hand side of the tab, you can click each sampling probe to rename it and double-click to highlight the probe on the diagram.
2. If you use more than one copy of a subCDL in the application that you target to the Sampling source, you can monitor the unique data for each instance of a sampling probe that you set in that subCDL. The sampling probe collects data for all instances that execute and divides the data into a separate list for each instance.
3. Use the graph on the right side of the tab to visualize data from sampling probes. The graph loads new data after the simulation stops executing for any reason and at each breakpoint that you set in the application. At each breakpoint, the graph appends new data to the data collected prior to that breakpoint for sampling probes in the same document as the breakpoint.
4. Use the cursor to compare exact sampling probe values for a certain value on the x-axis.
5. The unit of the x-axis on the graph changes based on execution method. The x-axis
 represents simulated time in seconds when you click the Run button to simulate an FPGA
 VI or CDL document on the development computer. The x-axis represents iterations of the
 CDL document when you use the Run GCDL Simulation node to test a CDL document in a host
 VI.

#### Example

Search within the programming environment to access the following installed example:

Sampling Probes

#### Tips and Tricks for Using Sampling Probes

Consider the following tips and tricks for using sampling probes:

- Closing the project deletes data from all sampling probes. If you want to save data that you acquire during testing and debugging, refer to 
 Testing a Clock-Driven Logic Document on the Host .
- An error glyph next to any plot on the graph indicates that you changed the data type of the wire after the sampling probe acquired any existing data. Run the simulation again to acquire data with the new data type.
- Monitor the value of a single sampling probe as the application executes using the 
 Debugging tab. The 
 Debugging tab updates that value as the application executes. 
 org.dita.html5/xsl/topic.xsl 455 Note Only one value for a sampling probe with more than one instance appears in the 
 Debugging tab. The value shown reflects the value for the instance that executed last.
- If you expect to see data for a sampling probe but it is not displayed in the graph, ensure that there is a checkmark in the checkbox next to the sampling probe in the 
 Sampling Probes tab. If the sampling probe is not listed, ensure that you selected the appropriate 
 Sampling source . You can also verify that at least one instance of the sampling probe acquired data in the 
 Debugging tab.
- Each sampling probe reports data at each rising edge of the clock that drives the Clock-Driven Loop containing the probe. Aligning the cursor with the edge of the clock signal allows you to view the data values as they change at an interval of one loop iteration. To compare sampling probe data to clock signals in the graph, include the following code on the subdiagram of one Clock-Driven Loop for the clock that drives the code you are testing. 
 Select the plot that represents your clock and use 
 Previous Transition and 
 Next Transition to align the cursor with the edges of the clock signal.

Related tasks:

- Testing a Clock-Driven Logic Document on the Host

Related information:

- Debugging Tools

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=setting-up-an-fpga-compile-farm.html language=enus -->
## TOPIC 00034: Setting up an FPGA Compile Farm

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `setting-up-an-fpga-compile-farm.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/setting-up-an-fpga-compile-farm.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: As the administrator of an FPGA compile farm, you must set up a web server on the compile server and connect one or more compile workers to the compile server. Before you begin the setup process, gain a basic understanding of the FPGA compile farm. Setting up a Web Server on the Compile Server Set u

Setting up an FPGA Compile Farm

As the administrator of an FPGA compile farm, you must set up a web server on the compile server and connect one or more compile workers to the compile server.

Before you begin the setup process, gain a basic understanding of the [FPGA compile farm](/csh?topicname=understanding-fpga-compile-farm.html).

Parent topic:

Configuring the FPGA Compiler

#### Setting up a Web Server on the Compile Server

Set up a web server on the compile server so that the compile worker and the development computer can connect to the compile server.

1. On the compile server, verify that the LabVIEW NXG FPGA Compile Farm Toolkit is installed by checking the 
 Installed tab in NI Package Manager. If the LabVIEW NXG FPGA Compile Farm Toolkit is not installed, install the toolkit in NI Package Manager.
2. Click 
 Start»All Programs»National Instruments»NI Web Server Configuration to launch the NI Web Server Configuration.
3. Follow the prompts in NI Web Server Configuration to set up the web server. 
 You will need the credentials you specify, such as port, password, and HTTPS connection status, when connecting a compile worker to the compile server. Users of the compile farm will also need the credential information when connecting to the compile server from their development computers.

#### Connecting a Compile Worker to the Compile Server

Connect a compile worker to the compile server so that the compile worker can receive compile job requests from the compile server.

Tip

Complete the following steps on each compile worker that you want to connect to the compile server:

1. If the compile worker is a different computer than the compile server, ensure the computer has the same development environment and is in the same network as the compile server.
2. Click 
 Start»All Programs»National Instruments»FPGA Compile Tools NXG»FPGA Compile Worker NXG and click 
 Configure to launch the 
 Configure Compile Worker dialog box.
3. Consider the following options before proceeding: 
 If...Next StepThe compile worker is the same computer as the compile server.
 Select 
 Use the local compile server and proceed to step 6.The compile worker is a different computer than the compile server.
 Select 
 Connect to a compile server and proceed to step 4.
4. Enter the login information of the compile server, such as server name, port, username, and password. 
 If the compile server was configured to allow admin users only, specify 
 admin as the username.
5. Enable the 
 Secure connection checkbox if you configured the compile server to use HTTPS. Otherwise, disable the checkbox.
6. Click 
 Test to verify the settings are valid. 
 Resolve any errors.
7. In the 
 Number of simultaneous jobs field, specify the maximum number of compile jobs that the compile worker can handle simultaneously. 
 org.dita.html5/xsl/topic.xsl 455Tip Generally, one CPU core can handle one compile job. However, NI recommends leaving one core free for operating system tasks. For example, if you have a quad-core CPU, NI recommends setting 
 Number of simultaneous jobs to 3.
8. Click 
 OK.

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=simulation-modes-fpga-application.html language=enus -->
## TOPIC 00035: Simulation Modes for Segments of an FPGA Application

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `simulation-modes-fpga-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/simulation-modes-fpga-application.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can execute units, components, or an entire system in simulation mode, which replicates the characteristics of an FPGA and generates behavior similar to what you can expect when you deploy to live hardware. Deploying an application you create onto an FPGA can be a time-consuming process. You sho

Simulation Modes for Segments of an FPGA Application

You can execute units, components, or an entire system in 
 *simulation mode*, which replicates the characteristics of an FPGA and generates behavior similar to what you can expect when you deploy to live hardware.

Deploying an application you create onto an FPGA can be a time-consuming process. You should begin deploying your application only after you are sure it does not contain any unintentional functionality or bugs. If you encounter a problem in your application after you deploy to live hardware, you have to identify the source of the issue, fix the issue, recompile the bitfile, and redeploy your code to the device.

Debugging your application using simulation mode and FPGA-specific debugging tools can significantly reduce the time you spend waiting for code to deploy and troubleshooting issues. Use the following tools to execute Clock-Driven Logic code in simulation mode:

Run in simulation mode

Run

Run in simulation mode

Run in simulation mode

Run GCDL Simulation node

Note

Project Files

Run GCDL Simulation

Host interface simulation

Open FPGA Reference

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=testbench-vi-information.html language=enus -->
## TOPIC 00036: Test Portions of Your FPGA Application with Testbench VIs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `testbench-vi-information.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/testbench-vi-information.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create a testbench VI on the host of the FPGA application to test code in your application using the full range of debugging tools in the development environment. A testbench VI generates a set of data that you can use to test the functionality and limits of a unit or component in your application.

Test Portions of Your FPGA Application with Testbench VIs

Create a testbench VI on the host of the FPGA application to test code in your application using the full range of debugging tools in the development environment.

A testbench VI generates a set of data that you can use to test the functionality and limits of a unit or component in your application. You create the code that generates the sample data, so you can focus on specific issues or limits of the code under test. You can also use a predefined set of data as the VI data source, depending on the requirements of your application.

Note

After the code under test finishes executing using the sample data, the testbench VI displays the results of the code. You can configure the panel of the testbench VI to display information you gather about the specific parts of the code under test that you are investigating.

#### Considerations when Creating Testbench VIs

When you create a testbench VI, determine the following aspects of the VI to ensure that it generates data similar to the data the deployed application will handle:

- Data type for the input samples
- Number of samples to send through the code under test
- Output format to display the results of the testbench VI execution

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=testing-cdl-document-on-host.html language=enus -->
## TOPIC 00037: Testing a Clock-Driven Logic Document on the Host

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `testing-cdl-document-on-host.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/testing-cdl-document-on-host.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Compiling code for the FPGA can take minutes to hours. To save time, you can test the logic of Clock-Driven Logic (CDL) documents using simulation in a host VI before compiling. Testing individual CDL documents on the host allows you to ensure that you thoroughly test the functionality of the CDL co

Testing a Clock-Driven Logic Document on the Host

Testing individual CDL documents on the host allows you to ensure that you thoroughly test the functionality of the CDL code.

#### What to Use

- Run GCDL
 Simulation
- For Loop
- While Loop

#### What to Do

Create the following diagram to simulate and test your CDL document in a host VI.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-5C615834-89B1-42BA-BB99-93410713D92C-a5.png']

|  | Select a CDL document to simulate with the Run GCDL Simulation node on the Item tab. The inputs and outputs that appear on the node correspond to the inputs and outputs of the CDL document you select. If there are sampling probes in the CDL document that you select, you can view data for each sampling probe when you simulate using Run GCDL Simulation. To view data, use the Tool Launcher to open the Sampling Probes tab and set Sampling source to the FPGA to which you targeted the CDL document. |
| --- | --- |
|  | The Run GCDL Simulation node simulates clock cycles on an FPGA. Because code on an FPGA often takes multiple clock cycles to produce valid data, you can use a While Loop around the Run GCDL Simulation node to ensure that the host VI runs until the CDL executes completely. |
|  | The For Loop repeats the code you want to test until all the test values you supply are consumed. The auto-indexing functionality of a For Loop allows the CDL document to access and process each individual element of an input array. You can then collect the result of each loop iteration with an auto-indexing output tunnel. |
|  | Provide test data that exercises all inputs and outputs of the CDL document and spans the range you expect the CDL document to receive from the application. The code in the diagram example above focuses on testing the data in input, a cluster, of the CDL document. Depending on your preference, you can test all inputs and outputs in a single host VI or you can test them across multiple VIs. |
|  | Provide results you expect the CDL document to produce for the test data provided. |
|  | Compare the results of the data processed by the CDL document to the results you expect to determine if logic or other code in the CDL document needs to change. |

#### Troubleshooting

- If your test results do not match your expected results, create sampling probes in the CDL document that you are testing. After the host VI executes, you can view the data that the sampling probes collect in the 
 Sampling Probes tab and use the data to debug your code.
- The complexity needed in the host VI varies depending upon the complexity of the CDL document you are testing. For example, if the CDL document uses handshaking or pipelining, you might need more complex code in the host VI to fully test the CDL document. If your test only uses code that is available on the FPGA, consider testing by simulating your CDL document in a Clock-Driven Loop on the diagram of an FPGA VI.

#### Examples

Search within the programming environment to access the following installed example:
 *Sampling Probes*

Search within the programming environment to access the following lesson:
 *Programming with Clock-Driven Logic*.

Related concepts:

- Strategies for Testing FPGA Applications
- Host VIs

Related reference:

- Sampling Probes Tab

Related information:

- Clock-Driven Logic

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=testing-communication-host-fpga.html language=enus -->
## TOPIC 00038: Testing Communication between the Host VI and an FPGA VI

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `testing-communication-host-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/testing-communication-host-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: To complete this task, you need the FPGA VI and the host VI you want to communicate between. You can run FPGA code on the host computer to test the logic of the code without investing the time to compile it. Testing the communication between the host VI and the FPGA VI, on the host computer, saves t

Testing Communication between the Host VI and an FPGA VI

To complete this task, you need the FPGA VI and the host VI you want to communicate between.

Testing the communication between the host VI and the FPGA VI, on
 the host computer, saves time and makes it easier to repeat tests until you are
 ready to deploy to the FPGA.

#### What to Use

- Open FPGA Reference
- Close FPGA VI Reference
- Other FPGA Host Interface nodes

#### What to Do

Create the following diagram to communicate with the FPGA VI from a host VI.

Customize the gray section for your unique programming goals.

[IMAGE alt='1378' src='GUID-7D879547-C629-499A-84EA-759047EBFB83-a5.png']

|  | To specify the FPGA bitfile you want to deploy to the target, complete the following steps: On the diagram, select the Open FPGA Reference node. On the Item tab, in the Mode section, select Run bitfile on hardware. In the File list, select a bitfile within your project or select Dynamic reference and wire the bitfile path to the bitfile path input. Wire the address of the FPGA target to device name. When you run this host VI, a reference to the FPGA application associated with the bitfile you selected opens and runs on the FPGA target you specify. |
| --- | --- |
|  | When testing communication between a host VI and the FPGA VI, use test code that mirrors the communication that you want to occur when you actually deploy the FPGA VI. Use the FPGA Host Interface nodes to communicate with code on an FPGA and in simulation on the host computer. In the diagram above, one of the ways the host VI and the FPGA VI communicates is through a DMA FIFO using the Write DMA FIFO and Read DMA FIFO nodes. When this host VI runs, the host VI and the FPGA VI write data to and read data from a block of memory on the host that simulates a FIFO on the FPGA. Note The host VI cannot simulate FPGA Host Interface nodes that perform hardware-specific functions, such as the Download FPGA VI node or the P2P Streaming nodes. |
|  | Use the Close FPGA VI Reference node to close every reference the Open FPGA Reference node creates. If you do not close the reference, the FPGA VI runs indefinitely until you click the Abort button in the FPGA VI. |

#### Examples

Search within the programming environment to access the following installed example:
 *FPGA Host Interface*.

Related concepts:

- Host VIs
- FPGA VIs
- Execution of FPGA Code

Related tasks:

- Compiling FPGA Code
- Downloading and Running an FPGA VI

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=testing-fpga-applications.html language=enus -->
## TOPIC 00039: Strategies for Testing FPGA Applications

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `testing-fpga-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/testing-fpga-applications.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: Testing an application, and the pieces of the application, allows you to ensure that the application functions as you expect and helps to prevent errors later in development. Test your application on three levels: unit, component, and system. Testing smaller portions of code as you create them saves

Strategies for Testing FPGA Applications

Testing an application, and the pieces of the application, allows you to ensure that the application functions as you expect and helps to prevent errors later in development.

Test your application on three levels: unit, component, and system. Testing smaller portions of code as you create them saves time by identifying and preventing errors and bugs as your program grows. If you test and debug the functionality of the code extensively at the unit and component levels, you reduce the potential for errors at the system level.

Refer to the following guidelines for help identifying units, components, and systems:

Unit

- Real-world I/O
- Interaction with target resources or data in a separate unit
- Multiple loops running in parallel or at different rates
- Reliance on the specific passing or control of real-world time, as opposed to simulated time

You can call units as subVIs or subCDLs that you can reuse throughout your application.

Component

System

Note

FPGA Host Interface

FPGA Host Interface

Create Testbench VIs to test individual units and components of your application as you complete them. A testbench is typically a VI that provides simulated input values to your code and displays the output of the code on the panel. When your system is complete, you can create a Testbench VI that runs your entire application, or you can simply run your host application.

The following list provides examples of tests you might perform on various FPGA-targeted documents:

- Clock-Driven Logic—To test CDL code, use a
 Run GCDL Simulation node to call the CDL document from a
 testbench VI on the host.
- Mixed languages in an FPGA VI—To test code that mixes languages in an FPGA VI, place the code in a top-level FPGA VI testbench. Use FPGA Host Interface nodes in a host VI to run the FPGA testbench in simulation on the host.
- Top-Level FPGA VI—To test your entire application, also known as the system, use FPGA Host Interface nodes in a host VI to run the top-level FPGA VI in simulation on the host.

Related tasks:

- Testing a Clock-Driven Logic Document on the Host
- Testing Communication between the Host VI and an FPGA VI

Related information:

- Language Integration in LabVIEW

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=tools-to-debug-clock-driven-logic.html language=enus -->
## TOPIC 00040: Tools for Debugging Clock-Driven Logic Code

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `tools-to-debug-clock-driven-logic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/tools-to-debug-clock-driven-logic.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use several Clock-Driven Logic troubleshooting tools that the development environment includes to debug Clock-Driven Logic code in your FPGA application. Testbench VI Generates sample data and compares the output of the code under test to an expected outcome to determine whether the code fun

Tools for Debugging Clock-Driven Logic Code

You can use several Clock-Driven Logic troubleshooting tools that the development environment includes to debug Clock-Driven Logic code in your FPGA application.

Testbench VI

Run GCDL Simulation Node

Note

Run GCDL Simulation

Sampling Probe

Sampling Probes

Sampling probes are only available in a Clock-Driven Logic document or a Clock-Driven Loop. When you add a sampling probe to a wire, it appears on both the 
 Debugging and 
 Sampling Probes tabs. The 
 Debugging tab displays the most recent value the probe recorded, while the 
 Sampling Probes tab displays each data point recorded during the most recent application execution.

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=transferring-data-clock-domains-fifo.html language=enus -->
## TOPIC 00041: Transferring Data between Clock Domains Using FIFOs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `transferring-data-clock-domains-fifo.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/transferring-data-clock-domains-fifo.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Before completing this task, verify that FIFOs are the best data storage and transfer option for your application. Use FIFOs to move data between Clock-Driven Loops to ensure that every data sample is valid and that every data sample written by one loop is read by the other loop. What to Use Clock-D

Transferring Data between Clock Domains Using FIFOs

Before completing this task, verify that FIFOs are the best data storage and transfer option for your application.

Use FIFOs to move data between Clock-Driven Loops to ensure that every data sample is valid and that every data sample written by one loop is read by the other loop.

#### What to Use

- Clock-Driven Loops
- Write FIFO
- Read FIFO
- Feedback Nodes

#### What to Do

Create the following diagram to transfer data between clock domains without data loss.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-32F3921D-9D6F-481E-84C2-AE65B8897675-a5.png']

|  | Use a reference to a local FIFO implemented in block RAM or look-up tables to ensure that the Write FIFO and Read FIFO nodes in separate Clock-Driven Loops access the same FIFO. To implement a FIFO in block RAM or look-up tables, select the FIFO in the resource collection. In the Behavior section of the Item tab, ensure Storage is set to Block RAM or Look-up table. |
| --- | --- |
|  | Use a Case Structure and Feedback Nodes to retain data samples for multiple clock cycles when the other Clock-Driven Loop is not ready for data. |
|  | Perform operations inside the Case Structure on the data you write to the FIFO shared between clock domains. Wire the data from the Case Structure to both Write FIFO and the sender data indicator. For the False case, wire the data from the previous clock cycle through the Case Structure. Also, add a False constant to the Case Structure and wire the False constant to input valid of Write FIFO to communicate that the data is not valid. |
|  | Use Read FIFO to read and remove the oldest element from the FPGA FIFO and determine whether the read operation is successful. Wire a True constant to ready for output of Read FIFO to communicate that the data from the other Clock-Driven Loop is ready to be read. Read FIFO reads every sample sent from the other Clock-Driven Loop. |
|  | Perform operations on the data from the other clock domain. To preserve the last processed data sample produced by this Clock-Driven Loop when no new valid samples are available, use a Case Structure and a Feedback Node to retain a data sample for multiple clock cycles. The following image shows the False case of the Case Structure in this section. |

#### Examples

Search within the programming environment to access the following installed example:
 *Multiple Clock Domains*.

Parent topic:

Data Transfer Using FIFOs

Related concepts:

- Data Transfer Using FIFOs
- Storing and Transferring Data

Related tasks:

- Transferring Data Using a Memory Item
- Transferring Data between Clock Domains Using Registers

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=transferring-data-clock-domians-registers.html language=enus -->
## TOPIC 00042: Transferring Data between Clock Domains Using Registers

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `transferring-data-clock-domians-registers.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/transferring-data-clock-domians-registers.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Before completing this task, verify that registers are the best data storage and transfer option for your application. When you need to store a single unit of data per clock cycle and do not require lossless transfer, use one or more local registers to transfer data between clock domains in a VI tar

Transferring Data between Clock Domains Using Registers

Before completing this task, verify that registers are the best data storage and transfer option for your application.

When you need to store a single unit of data per clock cycle and do not require lossless transfer, use one or more local registers to transfer data between clock domains in a VI targeted to an FPGA. Registers consume fewer FPGA resources than FIFOs and do not consume limited block RAM or dynamic RAM resources. However, if you require lossless data transfer, use FIFOs or handshake items instead of registers.

#### What to Use

- Clock-Driven Loops
- Create Register
- Read Register
- Write Register

#### What to Do

Create the following diagram to transfer data between clock domains using registers.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-80CDB397-940D-45C6-ACEE-88B53C97060A-a5.png']

|  | Use a locally scoped register item to share a register between two Clock-Driven Loops in the same FPGA VI. The constant you wire to initial value of Create Register determines the initial value and data type of the register item. However, in a lossy data transfer, the actual value is not important for the application. |
| --- | --- |
|  | Share the same register reference across Clock-Driven Loops so that Write Register and Read Register in separate clock domains access the same FPGA resource. |
|  | Process the data that you write to the FPGA register you reference in this clock domain. |
|  | Place Write Register in the faster of two clock domains to ensure that Read Register reads valid data. Write Register in a faster clock domain overwrites the data in the register many times for each time the slower clock domain reads a data point. |
|  | Place Read Register in the slower of two clock domains. Read Register in a slower clock domain will always read valid data but may miss, or drop, many units of data between one valid read and the next. If you need to read every unit of data, transfer data using FIFOs instead of registers. |
|  | Perform operations on the most recent unit of data read from the FPGA register you reference in this clock domain. |

#### Examples

Search within the programming environment to access the following installed examples:

- Register
- Multiple Clock Domains

Parent topic:

Data Transfer Using FPGA Registers

Related concepts:

- Data Transfer Using FPGA Registers
- Storing and Transferring Data

Related tasks:

- Transferring Data between Clock Domains Using FIFOs
- Transferring Data Using a Memory Item

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=transferring-data-target-host-fifo.html language=enus -->
## TOPIC 00043: Transferring Data between a Target and Host Using FIFOs

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `transferring-data-target-host-fifo.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/transferring-data-target-host-fifo.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `task`
- source_description: Use FIFOs to transfer data between an FPGA target and a host processor without data loss.To transfer only the most current data between the FPGA and the host with minimal delay and low overhead, use panel controls and indicators instead. What to Use Open FPGA Reference Run FPGA VI Write DMA FIFO Rea

Transferring Data between a Target and Host Using FIFOs

Note

use panel
 controls and indicators

#### What to Use

- Open FPGA Reference
- Run FPGA VI
- Write DMA FIFO
- Read DMA FIFO
- Close FPGA VI Reference
- Read FIFO
- Write FIFO

#### What to Do

1. Create the following diagram in a VI targeted to
 your FPGA. Customize the gray section for your unique programming goals. [IMAGE alt='1378' src='GUID-56FBC837-CABD-40FB-9E90-1CCF3BFE0A78-a5.svg'] [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']In a resource collection (.grsc) targeted to the
 FPGA, create a Host to Target FIFO. Use a FIFO
 constant to reference the Host to Target FIFO
 that you created. Wire this FIFO reference to the
 Read FIFO node.[IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']Process the data sent from the host. Use
 the timed out? output of the
 Read FIFO and Write
 FIFO nodes to determine if the read or write
 operation is successful.[IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']In a resource collection (.grsc) targeted to the
 FPGA, create a Target to Host FIFO. Use a FIFO
 constant to reference the Target to Host FIFO
 that you created. Wire this FIFO reference to the
 Write FIFO node.
2. Create the following diagram in a VI targeted to your host processor. Customize the gray sections for your unique programming goals. [IMAGE alt='1378' src='GUID-1B58603B-5FDD-4D4E-971C-3891DB226E08-a5.png'] [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']Use the device name for your FPGA found in SystemDesigner to specify an FPGA target. To ensure your code runs on the FPGA, the device name input must match the FPGA device name.[IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']Select the Open FPGA Reference node and select a mode of assigning an FPGA bitfile or application on the Item tab. You must assign a bitfile or application before you can select FIFO references for the Write DMA FIFO and Read DMA FIFO nodes. To obtain a bitfile, you must first compile FPGA code into a bitfile.[IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']Perform operations using the host processor before transferring data to the FPGA target. The data you write to the Write DMA FIFO node must use the same data type that you need in your FPGA VI. Convert data types from the host processor to the data type of the FIFO you specify for the Write DMA FIFO node.[IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']Select the Write DMA FIFO node and specify the reference to the Host to Target FIFO in the General section of the Item tab.[IMAGE alt='1378' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']Select the Read DMA FIFO node and specify the reference to the Target to Host FIFO in the General section of the Item tab.[IMAGE alt='1378' src='GUID-F2CDD9BB-5D12-4E8D-8D71-2A02539C495D-a5.svg']The data output from the Read DMA FIFO node contains data written to the DMA FIFO from the FPGA target. Use this output to display data from the FPGA target on the host, or use the host to further process the output data using the host processor.

#### Troubleshooting

If you receive unexpected or invalid data on your host from your target:

- Check that the device name for your hardware is correct. Verify the device name input you use in LabVIEW NXG matches the device name listed for your hardware device in SystemDesigner.
- Check that the FIFO references on the host match the FIFO references on the target. The FIFO you configure for the Write DMA FIFO node on the host must match the FIFO reference you send to the Read FIFO node on the FPGA target. The FIFO you configure for the Read DMA FIFO node on the host must match the FIFO reference you send to the Write FIFO node on the FPGA target.

#### Examples

Search within the programming environment to access the following installed examples:

- FIFO
- FPGA Host Interface

Parent topic:

Data Transfer Using FIFOs

Related concepts:

- Storing and Transferring Data
- Direct Memory Access (DMA) FIFOs
- Data Transfer Using FIFOs

Related information:

- Using Handshaking to Ensure Valid Data in a Clock-Driven Loop

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=understanding-fpga-compile-farm.html language=enus -->
## TOPIC 00044: Understanding FPGA Compile Farm

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `understanding-fpga-compile-farm.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/understanding-fpga-compile-farm.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: An FPGA compile farm consists of a compile server and one or more compile workers that are connected to the compile server. The following figure shows how the components work together to compile FPGA code into a bitfile. You create and edit FPGA code on the development computer. The development comp

Understanding FPGA Compile Farm

An FPGA compile farm consists of a compile server and one or more compile workers that are connected to the compile server. The following figure shows how the components work together to compile FPGA code into a bitfile.

[IMAGE alt='1378' src='GUID-46BEF049-A679-42DE-9555-487019C4A8B8-a5.svg']

1. You create and edit FPGA code on the development computer.
2. The development computer submits a compile job request to the compile server. The compile server can be the development computer or a remote computer.
3. The compile server sends the compile job to an available compile worker, which compiles the FPGA code into a bitfile. The compile worker can be the development computer or a remote computer.
4. The compile worker submits the bitfile back to the compile server.
5. The compile server sends the bitfile back to the development computer. You can then deploy the bitfile to the FPGA target.

Parent topic:

Configuring the FPGA Compiler

Related tasks:

- Setting up an FPGA Compile Farm

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=using-arrays-in-fpga.html language=enus -->
## TOPIC 00045: Using Arrays in FPGA Applications

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `using-arrays-in-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/using-arrays-in-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use up to three-dimensional arrays with a fixed size or a variable size that resolves to a fixed size at compile time in your FPGA application. To configure an array constant, control, or indicator to be fixed-sized, select the array object and select Fixed in the Compiled size option in the

Using Arrays in FPGA Applications

You can use up to three-dimensional arrays with a fixed size or a variable size that
 resolves to a fixed size at compile time in your FPGA application.

To configure an array constant, control, or indicator to be fixed-sized, select the array object
 and select Fixed in the Compiled size
 option in the Item tab.

To use a variable-sized array, make sure the array size can be determined at compile
 time. This might mean that certain properties of the array, such as the length or
 indexes of the elements you read or write, must be constant values. For example, if you
 use the Array Subset node, the index and
 length inputs must be constant so that the size for the
 output subarray can be determined.

The following table describes behaviors, caveats, and restrictions for using
 variable-sized arrays with some nodes or functionalities in FPGA applications.

| Nodes or Functionalities | Behavior, Caveats, and Restrictions |
| --- | --- |
| Array Operations | For each node that supports array inputs or outputs, LabVIEW NXG determines the size of an array output by examining the inputs of the node. If a node includes only scalar or fixed-size array inputs, LabVIEW NXG infers a fixed-size array output. LabVIEW NXG returns an error if it cannot infer a fixed size. The following Array nodes can return arrays that resolve to a fixed size at compile time, regardless of constant or non-constant inputs: Build Array Cluster to Array Decimate 1D Array Interleave 1D Arrays Replace Array Subset Reverse 1D Array Rotate 1D Array The following Array nodes can return arrays that resolve to a fixed size at compile time if one or more inputs are constants: Array Subset—The index and length inputs must be constant. Delete from Array—The length and index inputs must be constant. Initialize Array—The dimension size input must be constant. Insert into Array—The index input must be constant. Reshape Array—The dimension size input must be constant. Split 1D Array—The index input must be constant. |
| Classes and Clusters | You can embed arrays that resolve to a fixed size at compile time in clusters and classes. |
| SubVIs | LabVIEW NXG tracks inferred array sizes of subVIs in order to propagate them in and out of an FPGA VI. For subVIs with VI reentrancy set to None, if an array size inferred through one call does not match the size of another call, LabVIEW NXG returns an error for the panel control along with all calls to that VI. |
| Shift Registers | LabVIEW NXG infers the array size by examining the input terminals. If the array size of the initial value input does not match the size of the array passed from the right border, LabVIEW NXG returns an error. |
| Feedback Nodes | LabVIEW NXG compares the array size on the input terminal of the Feedback Node to the size of the initializer terminal. If the sizes do not match, LabVIEW NXG returns an error. |
| Select Node | LabVIEW NXG infers the output array size only if both input array sizes statically resolve to the same fixed size at compile time. Otherwise, LabVIEW NXG returns an error. |
| Case Structures | LabVIEW NXG infers the array size of a Case structure output tunnel only if the input array sizes of all diagrams within the Case structure statically resolve to the same fixed size at compile time. Otherwise, LabVIEW NXG returns an error. |
| For Loops | LabVIEW NXG infers the array size of an auto-indexed output tunnel based on the number of times the For Loop executes. You must wire a constant value to the count terminal. LabVIEW NXG returns an error if the size of the array output is not statically resolved. |
| Coercions | Wiring a variable-sized array to a fixed-size terminal where the array sizes do not match, as with subVI terminals and indicators, results in coerced data that is padded or truncated to the terminal size. When you wire a fixed-size array to a variable-sized terminal, the array size of the fixed type propagates forward. |

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=using-clock-driven-loops.html language=enus -->
## TOPIC 00046: Using Clock-Driven Loops to Run Code at Higher Rates with Lower Latency

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `using-clock-driven-loops.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/using-clock-driven-loops.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you need logic to execute with lower latency at the same clock rate, use the Clock-Driven Loop or create a Clock-Driven Logic document (.gcdl). The clock wired to a Clock-Driven Loop or the clock you define for a Clock-Driven Logic document determines the execution time of one iteration of the

Using Clock-Driven Loops to Run Code at Higher
 Rates with Lower Latency

When you need logic to execute with lower latency at the same clock rate, use the
 Clock-Driven Loop or create a Clock-Driven Logic
 document (.gcdl).

The clock wired to a Clock-Driven Loop or the clock you
 define for a Clock-Driven Logic document determines the execution time of
 one iteration of the logic within that loop or document. You can use the
 base clock(s) of the FPGA target or [create
 derived clocks](/csh?topicname=increasing-fpga-execution.html) that scale the frequency of the base clocks
 if none of the base clocks meets the timing objectives of your
 Clock-Driven Loop or Clock-Driven Logic
 document. You can [define
 different clock domains](/csh?topicname=control-execution-rate.html) for the Clock-Driven Loops or
 Clock-Driven documents in your FPGA application to execute sections of your
 code at different clock rates to achieve separate timing objectives.

When you place code inside a Clock-Driven Loop or a
 Clock-Driven Logic document, the compiler does not automatically insert
 registers on the data path. Some nodes, such as the FFT or other high
 throughput math nodes, take multiple clock cycles even when they are in
 Clock-Driven Loops. Use [handshaking](/csh?topicname=handshaking-signals.html)
 to schedule the timing of data for these nodes.

If the propagation delay within a Clock-Driven Loop or
 Clock-Driven Logic document exceeds the specified clock rate, LabVIEW NXG
 returns a timing violation when you attempt to compile your code. The
 Timing Violation Analysis window displays which
 Clock-Driven Loop or Clock-Driven Logic
 document failed to meet timing requirements. In some cases, you can reduce
 the length of a combinatorial path by manually inserting Feedback Nodes or
 shift registers to implement a pipelined design.

Parent topic:

Clocks and Timing on an FPGA

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=using-custom-data-types-with-resources.html language=enus -->
## TOPIC 00047: Using Custom Data Types with FPGA Resource Items

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `using-custom-data-types-with-resources.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/using-custom-data-types-with-resources.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom controls of supported data types and use these controls as data types for FIFOs, memory items, FPGA registers, or handshake items by configuring the resource data type in the Element section of the Item tab. If the custom control is a type definition, LabVIEW NXG disconnects th

Using Custom Data Types with FPGA Resource
 Items

You can create custom controls of supported data types and use these controls as data
 types for FIFOs, memory items, FPGA registers, or handshake items by configuring the
 resource data type in the Element section of the
 **Item** tab. If the custom control is a type definition,
 LabVIEW NXG disconnects the control from the type definition.

In the following example, the FIFO transfers address and data information in a
 single cluster element. Using a custom control, these values remain distinct
 so that you can split the values after reading the element from the
 FIFO.

[IMAGE alt='1378' src='GUID-FAF76284-5D6B-46E4-A143-D38953FC62B1-a5.png']

Using custom data types has the following advantages:

- Simplifies diagrams and increases application throughput.
- Breaks the 64-bit barrier by joining two small supported types into one
 larger data type for some FPGA targets. Refer to the hardware
 documentation for the FPGA target for more information.
- Keeps resources separate for each value in the FIFO or memory.

Note

Parent topic:

Storing and Transferring Data

Related concepts:

- Supported Data Types

Related information:

- Creating a Custom Data Type Using a G Type Document

<!--NI_TOPIC bundle=labview-nxg-fpga-targets path=using-subvis-in-fpga.html language=enus -->
## TOPIC 00048: Using SubVIs in FPGA Applications

- bundle_id: `labview-nxg-fpga-targets`
- source_path: `using-subvis-in-fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-targets/raw/resource/enus/using-subvis-in-fpga.html
- document_id: `labview-nxg-fpga-targets`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can group common sections of code for reuse as subVIs on the diagram. When developing FPGA applications, use subVIs for the following purposes: Use multiple FPGA VIs—You can create only one top-level FPGA VI, but you can implement multiple FPGA VIs by calling them as subVIs from the top-level FP

Using SubVIs in FPGA Applications

You can group common sections of code for reuse as subVIs on the diagram.

When developing FPGA applications, use subVIs for the following purposes:

- Use multiple FPGA VIs—You can create only one top-level FPGA VI, but you can
 implement multiple FPGA VIs by calling them as subVIs from the top-level FPGA
 VI.
- Conserve FPGA resources—Panel objects in subVIs do not communicate directly with the
 host VI and therefore do not consume additional FPGA resources.
- Reuse code across multiple projects—Creating reusable, modular code helps you
 efficiently organize, manage, test, and debug your application by allowing for
 easier code review and updates and by avoiding code duplication.

The [VI reentrancy](http://www.ni.com/documentation/en/labview/latest/create-first/choose-right-vi-reentrancy/) of subVIs on an FPGA
 target is set to Stateful by default. Use this option if a subVI
 accesses shared resources, such as I/O, or if multiple instances of the subVI share data
 in a VI, such as functional global variables. To verify if subVI configuration meets the
 resource and timing needs of your application, [compile the application](/csh?topicname=compiling-fpga-code.html)
 and check the Estimated resource usage report and
 Timing Violations tab when the compilation completes.

Note

Related information:

- SubVIs
