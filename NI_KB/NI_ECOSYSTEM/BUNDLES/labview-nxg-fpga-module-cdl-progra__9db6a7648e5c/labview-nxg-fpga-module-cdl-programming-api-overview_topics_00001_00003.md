# NI DOCUMENT BUNDLE: labview-nxg-fpga-module-cdl-programming-api-overview

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-fpga-module-cdl-programming-api-overview start=1 end=3 -->
<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-programming-api-overview path=clock-driven-logic.html language=enus -->
## TOPIC 00001: Clock-Driven Logic

- bundle_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- source_path: `clock-driven-logic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-programming-api-overview/raw/resource/enus/clock-driven-logic.html
- document_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Clock-Driven Logic allows you to create code that executes in one clock cycle at the rate you specify for the Clock-Driven Loop. Because the code maps directly to resources on the FPGA when you compile and depends on the timing of the Clock-Driven Loop, Clock-Driven Logic code can only run within a

Clock-Driven Logic

Clock-Driven Logic allows you to create code that executes in one clock cycle at the rate you specify for the Clock-Driven Loop.
 Because the code maps directly to resources on the FPGA when you compile and depends on the timing of the Clock-Driven Loop, Clock-Driven Logic code can only run within a Clock-Driven Loop on the diagram of a VI targeted to an FPGA.

You program using Clock-Driven Logic in two places.

[IMAGE alt='1378' src='GUID-1880A442-D673-429F-803B-16AE842670C3-a5.png']

1. Within the Clock-Driven Loop directly.
2. Within a Clock-Driven Logic document (.gcdl), or subCDL, placed within the Clock-Driven Loop.

Note

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-programming-api-overview path=handshaking-signals.html language=enus -->
## TOPIC 00002: Handshaking Signals in Clock-Driven Logic

- bundle_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- source_path: `handshaking-signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-programming-api-overview/raw/resource/enus/handshaking-signals.html
- document_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Handshaking refers to communication between two nodes that establishes the parameters for continued communication. For a given function, handshaking does the following: Indicates when upstream nodes send valid data to the function. An upstream node is any node that sends data to the function. Determ

Handshaking Signals in Clock-Driven Logic

Handshaking refers to communication between two nodes that establishes the parameters for continued communication.

For a given function, handshaking does the following:

[IMAGE alt='1378' src='GUID-06C42A42-2816-41FA-BCF0-A19513D514D2-a5.png']

1. Indicates when upstream nodes send valid data to the function. An upstream node is any node that sends data to the function.
2. Determines when the function discards or accepts data from upstream nodes.
3. Determines when downstream nodes discard or accept data from the function.
4. Indicates when the function sends valid data to downstream nodes. A downstream node is any node that receives data from the function.

In a Clock-Driven Loop, handshaking is necessary because some nodes need more than one cycle to compute valid data, but the Clock-Driven Loop requires all nodes to return data every clock cycle. To ensure the numeric accuracy of an algorithm, nodes that depend on this data must know whether the data is invalid or valid. National Instruments has established a handshaking protocol you can use with certain nodes inside a Clock-Driven Loop. This protocol involves the following terminals:

[IMAGE alt='1378' src='GUID-7DA5AF5B-B4D0-4819-AA3A-560478A7C568-a5.png']

1. input valid—The next data point has arrived for processing.
2. ready for output—The downstream node can accept a new data point.
3. output valid—The current data point produced by the node is valid and ready to be used by downstream nodes.
4. ready for input—The node can accept a new data point during the next clock cycle.

Parent topic:

Clock-Driven Logic

Related tasks:

- Using Handshaking to Ensure Valid Data in a Clock-Driven Loop

<!--NI_TOPIC bundle=labview-nxg-fpga-module-cdl-programming-api-overview path=handshaking-valid-data-cdl.html language=enus -->
## TOPIC 00003: Using Handshaking to Ensure Valid Data in a Clock-Driven Loop

- bundle_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- source_path: `handshaking-valid-data-cdl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-cdl-programming-api-overview/raw/resource/enus/handshaking-valid-data-cdl.html
- document_id: `labview-nxg-fpga-module-cdl-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Clock-Driven Loops force nodes to return data every clock cycle. However, some nodes, called multi-cycle nodes, need more than one cycle to compute a valid result. Therefore, nodes that depend on data from multi-cycle nodes must know whether that data is valid. Use a handshaking protocol so that nod

Using Handshaking to Ensure Valid Data in a Clock-Driven Loop

Clock-Driven Loops force nodes to return data every clock cycle. However, some nodes, called 
 *multi-cycle* nodes, need more than one cycle to compute a valid result. Therefore, nodes that depend on data from multi-cycle nodes must know whether that data is valid. Use a handshaking protocol so that nodes in a Clock-Driven Loop communicate with one another to verify that transferred data is valid every clock cycle.

#### What to Use

- Clock-Driven Loop in a G VI document targeted to an FPGA
- Feedback Node (Reverse)
- Nodes that support a handshaking protocol 
 org.dita.html5/xsl/topic.xsl 455 Note Nodes that support a handshaking protocol include one or more of the following handshaking inputs or outputs: input valid, output valid, ready for input, and ready for output.

#### What to Do

Create the following diagram to ensure that nodes within a Clock-Driven Loop send and receive only valid data through each loop iteration.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-7131A32A-B0A7-4438-8A6E-FDA84FB32B10-a5.png']

|  | Use a Data Exchange node or a terminal to connect the code in the Clock-Driven Loop to the rest of the system. Read FIFO in this diagram receives an array of data from a host VI and sends each sample sequentially to the downstream nodes in this code. |
| --- | --- |
|  | Use nodes from the Clock-Driven Logic palette to process the input data. All multi-cycle nodes from the Clock-Driven Logic palette have one or more of the following handshaking inputs or outputs: input valid, output valid, ready for input, and ready for output. For all multi-cycle nodes, wire output valid of the upstream node to input valid of the downstream node, and wire ready for output of the downstream node through a Feedback Node to ready for input of the upstream node. |
|  | Use a Data Exchange node or a terminal to connect the code in the Clock-Driven Loop to the rest of the system. Write FIFO in this diagram transfers the data that is processed by the Clock-Driven Loop back to the Host VI in the order that the data is received. |
|  | Connect output valid of the upstream node with input valid of the downstream node to prevent the downstream node from accepting a new input until the upstream node produces a new valid result. When output valid is False, any data output from the node is undefined. The undefined value generated by a node may differ between simulation and hardware. |
|  | Use a Feedback Node to enable downstream nodes to communicate their readiness to receive a new input with upstream nodes. The Feedback Node sends the result from ready for input back to ready for output of an upstream node. To avoid consuming an invalid input, each downstream node rejects new input data until both its ready for input produces a True value and its input valid receives a True value. Also, the upstream node sends new data only after the downstream node is ready for a new input, so the downstream node does not skip valid data. |

#### Troubleshooting

- If you receive unexpected or invalid output data, the handshaking signals may be wired incorrectly. For each upstream node, verify that output valid is wired to input valid of its adjacent downstream node. Also verify that, for each upstream node, ready for output is wired through a Feedback Node to ready for input of its adjacent downstream node.
- If you are using FIFOs to communicate between the host VI and the target and receive unexpected data in the host VI, verify that the FIFO references in the FPGA VI match the FIFO references in the host VI. For more information about using FIFOs to transfer data between a host and target, see Transferring Data between a Host and Target Using FIFOs .

#### Examples

Search within the programming environment to access the following installed examples:

- FPGA Host Interface
- FIFO
- Multiple Clock Domains

Search within the programming environment to access the following lessons:

- Handshaking in Clock-Driven Logic
- Programming with Clock-Driven Logic

Parent topic:

Handshaking Signals in Clock-Driven Logic

Related concepts:

- Handshaking Signals in Clock-Driven Logic
