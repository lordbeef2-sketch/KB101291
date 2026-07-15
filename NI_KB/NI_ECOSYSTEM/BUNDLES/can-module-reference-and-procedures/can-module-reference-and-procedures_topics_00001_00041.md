# NI DOCUMENT BUNDLE: can-module-reference-and-procedures

<!--NI_BUNDLE_CHUNK bundle=can-module-reference-and-procedures start=1 end=41 -->
<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_abort_transmit.html language=enus -->
## TOPIC 00001: Abort Transmit

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_abort_transmit.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_abort_transmit.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Abort Transmit

Abort a pending CAN frame transmission.

Since the determinism of CAN depends on the prioritization of frames based on ID, the SJA1000 CAN controller allows you to abort a pending transmit to replace it with a higher priority ID.

When implementing protocols that require abort, you must ensure that only one transmit is pending. Call **Wait on Transmit Complete** before (or after) each call to **CAN Output**. If more than one transmit is pending at the time **Abort Transmit** is called, the **Transmit Success** Boolean could refer to any one of those pending frames.

Refer to the [I/O Methods](985x_io_methods.html) introduction for step by step instructions to place this method in your LabVIEW diagram.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. |

|  | Timeout |
| --- | --- |
|  | Specifies the time to wait for the pending transmission to succeed or abort. The resolution is in milliseconds. Since this method must wait for the pending transmission to indicate abort or success, use a timeout greater than 0. Using a Timeout of 10000 (ten seconds) is sufficient for most CAN baud rates (longer than a frame time). The Timeout value of –1 (infinite wait) is not supported, but you can use the largest positive I32 value, which provides a maximum of approximately 25 days. |

#### Node Outputs

|  | Timed Out? |
| --- | --- |
|  | Indicates a timeout. When Timed Out? is TRUE, the error cluster indicates success (not a timeout error). Timed Out? will be TRUE only if you use a Timeout that is less than a frame-time for your specified CAN baud rate. |

|  | Transmit Success? |
| --- | --- |
|  | Indicates whether the pending transmit was successfully aborted, or transmitted on the network before it could be aborted. This value is valid only if Timed Out? is FALSE. If the pending transmit aborted successfully, this returns FALSE. If the pending frame transmitted successfully on the network prior to the Abort Transmit, this returns TRUE. |

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_add_targets_and_devices.html language=enus -->
## TOPIC 00002: Add Targets and Devices

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_add_targets_and_devices.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_add_targets_and_devices.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Add Targets and Devices

As with any other C Series module for CompactRIO, you must configure the CAN module prior to creating an FPGA VI. Refer to [Add Targets and Devices](/csh?topicname=lvdialog/add_targets_devices.html) dialog box for information on how to add the CAN module to your CompactRIO configuration.

Select the CAN module from the list of modules in the [New C Series Module](/csh?topicname=criodevicehelp/add%20module.html) dialog box. The module will then appear in the [Project Explorer](/csh?topicname=lvconcepts/using_labview_projects.html) window, ready for configuration.

In the Project Explorer window, right-click the NI 9852/NI 9853 module and select **Properties** from the shortcut menu to display the **Module Configuration** dialog box.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_arbitration.html language=enus -->
## TOPIC 00003: Arbitration

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_arbitration.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_arbitration.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Arbitration

Each CAN port uses dedicated resources in LabVIEW FPGA, as well as distinct communication paths between LabVIEW FPGA and the module. Therefore, when you access two different CAN ports in your FPGA VI, the nodes in the LabVIEW FPGA VI block diagram execute independently. For example, if you output a CAN frame to **CAN0** and simultaneously output a CAN frame to **CAN1**, the two CAN Output nodes execute independently. As another example, access to **CAN0** on a module in slot 1 occurs independently from access to **CAN0** on a module in slot 2.

When two or more nodes in the LabVIEW FPGA VI block diagram access the same CAN port at the same time, arbitration can occur to determine which node executes first. This arbitration may cause delays or jitter in your application. For example, if you want to transmit a specific CAN frame when a digital input trigger is detected in LabVIEW FPGA, arbitration between the CAN Output node and other CAN nodes can cause jitter from the digital input pulse to the start of the CAN frame.

#### Node Arbitration

For the same CAN port, CAN nodes of the same type must arbitrate. There are four types of CAN nodes:

- CAN Input
- CAN Output
- I/O Method Node
- I/O Property Node

CAN nodes of different type do not arbitrate at the node level.

For most applications, CAN node arbitration does not occur, and when it does the jitter introduced is small. For example, you would not normally use two CAN Input nodes simultaneously on the same CAN port, because neither node would return the correct sequence of CAN frames.

The most common situation in which CAN node arbitration occurs is use of a Wait I/O Method simultaneously with another I/O Method. For example, if you invoke Wait on Transmit Complete with a **Timeout** of 10 seconds, then invoke Abort Transmit soon after, node-level arbitration causes the Abort Transmit to execute after the Wait on Transmit Complete (possibly 10 seconds after invocation). When using multiple I/O Methods, you can avoid this behavior by polling for the event using **Timeout** of 0.

#### Output Path Arbitration

For each CAN port, two communication paths exist between LabVIEW FPGA and the CAN module. The output path transfers information from LabVIEW FPGA to the CAN port, and the input path transfers information from the CAN port to LabVIEW FPGA.

When two or more nodes in the LabVIEW FPGA VI block diagram access the same CAN port, arbitration can occur for the underlying output path. This arbitration is different than the usual node arbitration in LabVIEW FPGA, which is limited to multiple instances of a node. For example, if you write a frame to **CAN0**, and read a property on **CAN0** at the same time, arbitration occurs for the output path, because the CAN Output Node and the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) both send information from LabVIEW FPGA to the CAN port.

The following nodes use the output path to the CAN port:

- CAN Output
- I/O Method Node: Abort Transmit
- I/O Method Node: Reset
- I/O Method Node: Start
- I/O Method Node: Stop
- I/O Property Node: Read any property
- I/O Property Node: Write any property

When two or more of these nodes execute simultaneously for the same CAN port, arbitration occurs to force sequential execution, and some jitter may result. When arbitration occurs in the same FPGA clock cycle, CAN Output is prioritized first, then the [I/O Method Node](/csh?topicname=lvfpga/io_method_node.html), then the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html). When the nodes are the same, CAN [node arbitration](#nodearbitration) occurs.

The output path is implemented as a FIFO. This allows multiple frames to be sent to the CAN module for transmit, thus enabling tests that generate full bus load.

All nodes in the preceding list use the output FIFO with the exception of the Stop and Reset method. Since these methods stop CAN communication, they must execute regardless of pending transmit frames. Once the Stop or Reset method arbitrates successfully for the output path, it bypasses the FIFO and transfers the method to the CAN port for immediate execution.

When the output FIFO is full, a node in the preceding list (except Stop and Reset) must wait for an element to become available. This generally occurs when a frame from a previous CAN Output transmits successfully onto the network. The **Output Timeout (ms)** in the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html) dialog box specifies how long to wait for a new element to become available. Therefore, the **Output Timeout (ms)** applies to any CAN node in the preceding list, not just the CAN Output node.

If you specify **Output Timeout (ms)** of 0, the node simply checks to see if a new element is available (non-blocking). If an element exists, the node executes and error status of FALSE is returned (success). If no element exists, the node fails to execute, and error status of TRUE is returned (error). Therefore, in order to poll (such as writing frames without waiting), you must enable [Error Terminals](985x_errors.html) for the node. When an error is returned, you must attempt to execute the node again at a later time.

#### Input Path Arbitration

For the input path from the CAN port to LabVIEW FPGA, arbitration does not occur within LabVIEW FPGA. As soon as the CAN module has data for LabVIEW FPGA nodes, the data transfers immediately.

When the CAN port attempts to transfer information for two or more nodes back to LabVIEW FPGA, arbitration for the input path occurs within the CAN module. For example, if a CAN frame is received at the same time that a property is read, the CAN module must decide which node's data to transfer first. Although this input path arbitration can cause jitter, that jitter is minimal compared to the effects you can see from CAN node arbitration or CAN output path arbitration.

#### Module Configuration

The configuration information in Module Configuration is transferred from LabVIEW FPGA to the CAN module when the FPGA VI runs. Although this transfer occurs automatically as soon as the VI begins to run, all CAN nodes must wait for this one-time configuration to complete. The time required for configuration can be up to 1 second.

If your FPGA VI does not execute a CAN node before the configuration time elapses, you will not notice any delay. If a CAN node *is* executed before the configuration time elapses, the CAN node will wait for configuration to complete, then execute normally. If you execute CAN nodes in a manner that does not depend on timing, this behavior is not a concern. However, if you require the first CAN Input or CAN Output in your FPGA VI to execute without delay, you can do this by adding one of the following to the beginning of your VI (before the main loop):

- 1 second delay
- CAN Property or Method node (for instance, a Start method node)

#### Summary

When an FPGA VI is limited to CAN Input and CAN Output for each CAN port, the jitter between node execution and CAN frame transfer is very small. This is due to the fact that each CAN port uses a distinct communication path for input data and output data.

When you mix methods or properties along with input/output, you may see increased jitter between node invocation and CAN frame transfer. This jitter is due to the arbitration. The jitter is typically only a few microseconds, so it will generally be well within the limits for your application.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_bit_timing.html language=enus -->
## TOPIC 00004: Bit Timing

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_bit_timing.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_bit_timing.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Bit Timing

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

Each CAN baud rate corresponds to multiple values for two Bit Timing Registers (BTR). The bit fields in these registers are consistent across almost all CAN controllers. This property specifies the baud rate as values for the Bit Timing Registers. The least significant byte is BTR0, and the most significant byte is BTR1.

The default value for this property comes from [Module Configuration](985x_module_config.html). The **Baud Rate** property is converted to commonly used BTR values, or you can specify BTR values directly in the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html) dialog.

For information on CAN Bit Timing Registers, refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_can_input.html language=enus -->
## TOPIC 00005: CAN Input

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_can_input.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_can_input.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### CAN Input

Wait for a CAN frame to be received, then return that frame.

Complete the following steps to read from a CAN port using CAN Input.

1. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My Computer in the Project Explorer window, selecting New»FPGA I/O , and then adding CAN»NI 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or CAN»NI 9852»CAN1 (or CAN»NI 9853»CAN1 ) to the FPGA I/O list. Refer to New FPGA I/O dialog box (FPGA Module) for more information about creating and adding FPGA I/O to your CompactRIO configuration.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI diagram.
4. Right-click the I/O Node and select Select FPGA I/O»CAN»NI 9852»CAN0 (or Select FPGA I/O»CAN»NI 9853»CAN0 ) or Select FPGA I/O»CAN»NI 9852»CAN1 (or Select FPGA I/O»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Node and select Change to Read to use the I/O node for CAN Input.
6. Right-click the I/O Node and choose Properties to select the Data Type .

Start communication on the CAN port prior to using CAN Input. Enable **Auto Start** in the [Module Configuration](985x_module_config.html), or invoke the [Start](985x_start.html) method to start communication.

The **Input Timeout (ms)** of the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html) dialog box specifies how long to wait for a new frame to be received. If you specify **Input Timeout (ms)** of 0, the CAN Input node will simply check to see if a new frame has arrived (non-blocking).

For information on how CAN Input arbitrates with other CAN nodes, refer to [Arbitration](985x_arbitration.html).

|  | Note You can add more than one CAN input port to the FPGA I/O node, and also add analog and digital inputs to the same FPGA I/O node by right-clicking the FPGA I/O node and selecting Add Element. Right-click the created I/O name and choose Select FPGA I/O to specify the I/O name. If you use more than one input per node, LabVIEW will execute them sequentially starting with the top input. If one input is blocked while waiting for the input, subsequent inputs will be delayed. For example, if you read CAN0 and CAN1 with the same CAN Input node, that node will wait for a frame to be received on CAN0, then it will wait for a frame to be received on CAN1. It is more efficient to access each CAN port using a distinct CAN Input node. |
| --- | --- |

#### Properties Dialog

The **Data Type** selects the type for the CAN frame returned by the CAN Input node. The available values are **Cluster** (default) and **Array of 6 U32**.

The benefits of using the **Cluster** data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front panel)

The benefits of the **Array of 6 U32** data type, and handshaking integers to the host VI one at a time, are:

- Faster for transfer to/from host VI
- Fewer FPGA gates

Refer to the *Using Clusters and Arrays in LabVIEW FPGA* Application Note for more information on the use of clusters and arrays. Refer to the CAN examples in [NI 9852/NI 9853 Related Documentation](985x_related_documentation.html) for examples using each data type.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. Unless you set the Input Timeout (ms) to –1 to wait indefinitely, you must use the error terminals to determine whether the CAN Input successfully received a CAN frame. |

|  | CANx |
| --- | --- |
|  | If the Data Type is defined as Cluster (default), the CAN frame is represented as a cluster with the following elements: |

|  | Timestamp High Timestamp Low Timestamp of when the frame was received. The timestamp is acquired at the end of the CAN frame. The high and low U32 represent a single U64 timestamp. The timestamp is large enough to avoid handling rollover. The timestamp is zero-based (relative). The time starts ticking at zero when CAN communication starts. The resolution is 100 ns. Identifier Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). This representation of the CAN identifier is the same as NI-CAN (see NI 9852/NI 9853 Related Documentation and Examples). Type Type of frame: Data Frame0 Remote Frame1 Bus Error6 Transceiver Fault7 InfoA Reserved for future use. InfoB Reserved for future use. Data Length For data frames, this indicates the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. Data For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. For remote frames, the values contained in Data are not valid and should be ignored. |  |
| --- | --- | --- |
|  | Timestamp High |  |
|  | Timestamp Low |  |
|  | Timestamp of when the frame was received. The timestamp is acquired at the end of the CAN frame. The high and low U32 represent a single U64 timestamp. The timestamp is large enough to avoid handling rollover. The timestamp is zero-based (relative). The time starts ticking at zero when CAN communication starts. The resolution is 100 ns. |  |
|  | Identifier |  |
|  | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). This representation of the CAN identifier is the same as NI-CAN (see NI 9852/NI 9853 Related Documentation and Examples). |  |
|  | Type |  |
|  | Type of frame: Data Frame0 Remote Frame1 Bus Error6 Transceiver Fault7 |  |
|  | Data Frame | 0 |
|  | Remote Frame | 1 |
|  | Bus Error | 6 |
|  | Transceiver Fault | 7 |
|  | InfoA |  |
|  | Reserved for future use. |  |
|  | InfoB |  |
|  | Reserved for future use. |  |
|  | Data Length |  |
|  | For data frames, this indicates the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. |  |
|  | Data |  |
|  | For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. For remote frames, the values contained in Data are not valid and should be ignored. |  |

|  |  |  |  |  |  | If the Data Type is defined as Array of 6 U32, the CAN frame is represented as the following array of 6 U32 values: |
| --- | --- | --- | --- | --- | --- | --- |

|  |  |  |  |  |  | Most significant byte ... ... Least significant byte Timestamp (upper U32) Timestamp (lower U32) Identifier Type InfoA InfoB DataLength Data[0] Data[1] Data[2] Data[3] Data[4] Data[5] Data[6] Data[7] |
| --- | --- | --- | --- | --- | --- | --- |
| Most significant byte | ... | ... | Least significant byte |  |  |  |
| Timestamp (upper U32) |  |  |  |  |  |  |
| Timestamp (lower U32) |  |  |  |  |  |  |
| Identifier |  |  |  |  |  |  |
| Type | InfoA | InfoB | DataLength |  |  |  |
| Data[0] | Data[1] | Data[2] | Data[3] |  |  |  |
| Data[4] | Data[5] | Data[6] | Data[7] |  |  |  |
|  |  |  |  |  |  | The meaning of each element is the same as the Cluster data type. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_can_module_reference_and_procedures.html language=enus -->
## TOPIC 00006: CAN Module Reference and Procedures

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_can_module_reference_and_procedures.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_can_module_reference_and_procedures.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### CAN Module Reference and Procedures

The NI 9852 and NI 9853 are the NI C Series modules for Controller Area Network (CAN). Use this help file as a reference for information on the FPGA Device I/O functions, methods, and properties of the NI 9852/NI 9853.

Within this help file, the term *CAN module* refers to the NI 9852 or NI 9853 C Series modules.
Within CompactRIO software, the NI 9852/NI 9853 are also designated by the names *cRIO-9852* and *cRIO-9853*.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2006–2023 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_can_modules.html language=enus -->
## TOPIC 00007: CAN Modules

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_can_modules.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_can_modules.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### CAN Modules

[NI 9852](crio-9852.html)

[NI 9853](crio-9853.html)

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_can_output.html language=enus -->
## TOPIC 00008: CAN Output

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_can_output.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_can_output.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### CAN Output

Write a CAN frame to be transmitted.

Complete the following steps to write to a CAN port using CAN Output.

1. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My Computer in the Project Explorer window, selecting New»FPGA I/O , and then adding CAN»NI 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or CAN»NI 9852»CAN1 (or CAN»NI 9853»CAN1 ) to the FPGA I/O list. Refer to New FPGA I/O dialog box (FPGA Module) for more information about creating and adding FPGA I/O to your CompactRIO configuration.
3. Place an I/O Node from the FPGA I/O palette onto your FPGA VI diagram.
4. Right-click the I/O Node and select Select FPGA I/O»CAN»NI 9852»CAN0 (or Select FPGA I/O»CAN»NI 9853»CAN0 ) or Select FPGA I/O»CAN»NI 9852»CAN1 (or Select FPGA I/O»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Node and select Change to Write to use the I/O node for CAN Output.
6. Right-click the I/O Node and choose Properties to select the Data Type .

Start communication on the CAN port prior to using CAN Output. Enable **Auto Start** in the [Module Configuration](985x_module_config.html), or invoking the [Start](985x_start.html) method to start communication.

The communication path from LabVIEW FPGA to the CAN port on the module is implemented as a FIFO. The CAN Output node waits for an available element in the FIFO, then writes the frame to the FIFO. If no other CAN frame exists in the FIFO, the CAN frame will begin to transmit immediately.

CAN Output does not wait for the requested transmit to complete on the network (acknowledgement). Call CAN Output followed by [Wait on Transmit Complete](985x_wait_on_transmit_complete.html) (I/O Method) if you want to transmit CAN frames one at a time.

Write multiple frames to the output FIFO if you want to transmit CAN frames as fast as possible. The CAN module will submit these frames to the SJA1000 controller as fast as possible, thus generating close to 100% busload.

When the output FIFO is full, the CAN Output node waits for an element to become available, then writes the frame to the FIFO. The **Output Timeout (ms)** of the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html) dialog box specifies how long to wait for a new element to become available, which occurs when a frame from a previous CAN Output transmits successfully onto the network. If you specify **Output Timeout (ms)** of 0, the CAN Output node returns an error status of TRUE (error) if a new element is not available (non-blocking). When an error is returned, you must attempt CAN Output of the same frame again at a later time.

In addition to the CAN Output node, the **Output Timeout (ms)** also applies to most methods and properties. For example, if **Output Timeout (ms)** is 0, the Abort Transmit method will return an error if the output FIFO is full. For more information on the output path from LabVIEW FPGA to the CAN port, refer to [Arbitration](985x_arbitration.html).

|  | Note You can add more than one CAN output port to the FPGA I/O node, and also add analog and digital outputs to the same FPGA I/O node by right-clicking the FPGA I/O node and selecting Add Element. Right-click the created I/O name and select Select FPGA I/O to specify the I/O name. If you use more than one output per node, LabVIEW will execute them sequentially starting with the top output. If one output is blocked while waiting for the output, subsequent outputs will be delayed. |
| --- | --- |

#### Properties Dialog

Selects the **Data Type** for the CAN frame written to the CAN Input node. The available values are **Cluster** (default) and **Array of 6 U32**.

The benefits of using the **Cluster** data type are:

- Simpler block diagram (easy to use)
- Fast and efficient, if you limit use to the block diagram only (not front panel)

The benefits of the **Array of 6 U32** data type, and handshaking integers to the host VI one at a time, are:

- Faster for transfer to/from host VI
- Fewer FPGA gates

Refer to the *Using Clusters and Arrays in LabVIEW FPGA* Application Note for more information on the use of clusters and arrays. Refer to the CAN examples in [NI 9852/NI 9853 Related Documentation and Examples](985x_related_documentation.html#examples) for examples using each data type.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. |

|  | CANx |
| --- | --- |
|  | If the Data Type is defined as Cluster (default), the CAN frame is represented as a cluster with the following elements: |

|  | Timestamp High Ignored. The transmit request always occurs as soon as possible (not timed). Timestamp Low Ignored. The transmit request always occurs as soon as possible (not timed). Identifier Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). This representation of the CAN identifier is the same as NI-CAN (see NI 9852/NI 9853 Related Documentation and Examples). Type Type of frame: Data Frame0 Remote Frame1 InfoA Reserved for future use. InfoB Reserved for future use. Data Length For data frames, this indicates the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. Data For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. |  |
| --- | --- | --- |
|  | Timestamp High |  |
|  | Ignored. The transmit request always occurs as soon as possible (not timed). |  |
|  | Timestamp Low |  |
|  | Ignored. The transmit request always occurs as soon as possible (not timed). |  |
|  | Identifier |  |
|  | Arbitration ID. If bit 29 (20000000 hexadecimal) is clear, this ID uses the standard format (11-bit). If bit 29 is set, this ID uses extended format (29-bit). This representation of the CAN identifier is the same as NI-CAN (see NI 9852/NI 9853 Related Documentation and Examples). |  |
|  | Type |  |
|  | Type of frame: Data Frame0 Remote Frame1 |  |
|  | Data Frame | 0 |
|  | Remote Frame | 1 |
|  | InfoA |  |
|  | Reserved for future use. |  |
|  | InfoB |  |
|  | Reserved for future use. |  |
|  | Data Length |  |
|  | For data frames, this indicates the number of bytes in Data (0–8). For remote frames, this indicates the number of bytes requested. |  |
|  | Data |  |
|  | For data frames, this provides the data bytes. The array uses a fixed size of 8 bytes. |  |

|  |  |  |  |  |  | If the Data Type is defined as Array of 6 U32, the CAN frame is represented as the following array of 6 U32 values: |
| --- | --- | --- | --- | --- | --- | --- |

|  |  |  |  |  |  | Most significant byte ... ... Least significant byte Timestamp (upper U32) Timestamp (lower U32) Identifier Type InfoA InfoB DataLength Data[0] Data[1] Data[2] Data[3] Data[4] Data[5] Data[6] Data[7] |
| --- | --- | --- | --- | --- | --- | --- |
| Most significant byte | ... | ... | Least significant byte |  |  |  |
| Timestamp (upper U32) |  |  |  |  |  |  |
| Timestamp (lower U32) |  |  |  |  |  |  |
| Identifier |  |  |  |  |  |  |
| Type | InfoA | InfoB | DataLength |  |  |  |
| Data[0] | Data[1] | Data[2] | Data[3] |  |  |  |
| Data[4] | Data[5] | Data[6] | Data[7] |  |  |  |
|  |  |  |  |  |  | The meaning of each element is the same as the Cluster data type. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. Right-click the node and select Error Terminals to enable. Unless you set the Output Timeout (ms) to -1 to wait indefinitely, you must use the error terminals to determine whether the CAN Output successfully submitted a CAN frame for transmit. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_comm_state.html language=enus -->
## TOPIC 00009: Comm State

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_comm_state.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_comm_state.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Comm State

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property describes the current communication state of the CAN controller.

The values are:

| 0 | Error Active |
| --- | --- |
| 1 | Error Passive |
| 2 | Bus Off |

Use the [Wait on Comm State Change](985x_wait_on_comm_state_change.html) method to detect changes in this property.

When you initially start communication, the CAN port will begin in the Error Active state as specified in the CAN standard (except when **Listen Only** is enabled). After bus errors cause a transition to Error Passive or Bus Off, that state will be retained even after you stop communication and restart. Use the [Reset](985x_reset.html) method if you need to reset back to the Error Active state.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_configuration.html language=enus -->
## TOPIC 00010: Configuration

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_configuration.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_configuration.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Configuration

[Add Targets and Devices](985x_add_targets_and_devices.html)

[Module Configuration](985x_module_config.html)

[CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html)

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_converting_frames_channels.html language=enus -->
## TOPIC 00011: Converting Frames To and From Channels (Signals)

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_converting_frames_channels.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_converting_frames_channels.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Converting Frames To and From Channels (Signals)

The CAN Input and CAN Output nodes in LabVIEW FPGA access CAN data as frames, the raw unit of transfer on the CAN bus. For some applications, it is useful to access CAN data as channels, also known as signals. A CAN channel represents a field in the data of a frame with specific CAN identifier. The field in the data is scaled to a floating-point value in physical units, such as Volts or Revolutions-per-minute. The specification for how CAN channels are converted to/from CAN frames is usually provided in a CAN database file, such as Vector CANdb files.

NI-CAN is the software for National Instruments PCI, PXI, and PCMCIA cards for CAN. The NI-CAN software provides features to enable conversion of CAN frames to/from channels. This frame to channel conversion can be used with the CompactRIO CAN module, even if you do not use an NI CAN PCI, PXI, or PCMCIA card. For information on how to download NI-CAN and learn more about frame to channel conversion, refer to [NI 9852/NI 9853 Related Documentation and Examples](985x_related_documentation.html).

The NI-CAN software can be used on Windows as well as LabVIEW RT controllers. Supported LabVIEW RT controllers include any PXI controller, and the cRIO-9002 and cRIO-9004 CompactRIO Real-Time Controllers. You install NI-CAN to a LabVIEW RT controller using the software installation tool under **Remote Systems** in MAX.

Some examples of CompactRIO applications that use NI-CAN frame to channel conversion:

- Logging : The rugged enclosure and real-time capabilities of CompactRIO make it an ideal product for data logging in the field, such as drive testing of an automobile. For logging applications, the LabVIEW application on CompactRIO is simple: read CAN frames and store them in a file. When the CAN log file is later transferred from CompactRIO to a lab computer (usually running Windows), the application on the lab computer can read frames from the log file, and use NI-CAN to display the frames as CAN channel waveforms. In addition, if the LabVIEW application on CompactRIO stores a second log file with analog/digital samples, that data can be displayed on the lab computer as waveforms synchronized with the CAN channels.
- Triggering/Filtering : In a logging or other test application, you may need to evaluate CAN data to trigger some other task. For example, you may want to log a 5 second window of CAN/analog data when the "rpm" channel in CAN ID 5 first exceeds 4000 RPM. Although you could evaluate the raw data in CAN ID 5 to trigger the log, in some cases it is easier to simply evaluate the channel named "rpm" as defined in a CAN database. By installing NI-CAN on a CompactRIO Real-Time Controller such as the cRIO-9004, you can transfer CAN frames to NI-CAN, then read the "rpm" channel to detect when the value is greater than 4000.00.
- Prototyping/Simulation : For applications in which you must execute a control model within the CompactRIO Real-Time Controller, you typically wire CAN channels as inputs and outputs to the control model. In order to implement this, you can install NI-CAN on the CompactRIO Real-Time Controller. Your LabVIEW FPGA VI reads and writes CAN frames, and transfers those CAN frames to/from LabVIEW RT as you would any other I/O. Your LabVIEW RT VI uses NI-CAN to convert the CAN frames to/from CAN channels, which are then wired into the control model.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_crio_can_advanced_port_configuration_dialog_box.html language=enus -->
## TOPIC 00012: CAN Advanced Port Configuration

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_crio_can_advanced_port_configuration_dialog_box.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_crio_can_advanced_port_configuration_dialog_box.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### CAN Advanced Port Configuration

This dialog configures advanced properties for the CAN port. You can display this dialog from the [Module Configuration](985x_module_config.html).

#### Timeouts

The **Input Timeout (ms)** and **Output Timeout (ms)** specify timeout values to use with CAN nodes in the FPGA VI block diagram.

Each timeout is a signed 32-bit integer with a resolution of milliseconds, thus allowing a maximum value of approximately 25 days. Special values of 0 (do not wait) and –1 (wait indefinitely) are supported.

The CAN Input function waits for a new CAN frame to be received, then returns that frame. The **Input Timeout (ms)** specifies how long to wait for a new frame to be received.

If you specify **Input Timeout (ms)** of 0, the CAN Input node will simply check to see if a new frame has arrived (non-blocking). If a new frame exists, CAN Input returns the frame with an error status of FALSE (success). If no new frame exists, CAN Input returns an error status of TRUE (error). Therefore, in order to poll for new frames using an input timeout of 0, you must enable [Error Terminals](985x_errors.html) for the CAN Input node. When an error is returned, you must invoke CAN Input again at a later time to ensure no data is lost.

The communication path from LabVIEW FPGA to the CAN port is implemented as a FIFO. This allows multiple frames to be sent to the CAN module for transmit, thus enabling VIs that generate full bus load.

When the output FIFO is full, the CAN Output node waits for an element to become available, then writes the frame to the FIFO. **Output Timeout (ms)** specifies how long to wait for a new element to become available, which occurs when a frame from a previous CAN Output transmits successfully onto the network. If you specify **Output Timeout (ms)** of 0, the CAN Output node returns an error status of TRUE (error) if a new element is not available in the FIFO (non-blocking). When an error is returned, you must attempt CAN Output of the same frame again at a later time.

In addition to the CAN Output node, **Output Timeout (ms)** also applies to most methods and properties. For example, if **Output Timeout (ms)** is 0, the Abort Transmit method returns an error if the output FIFO is full. Refer to the [Arbitration](985x_arbitration.html) topic for more information on the output path from LabVIEW FPGA to the CAN port.

#### Bit Timing

When **Specify Baud Rate as Bit Timing Registers** is FALSE (unchecked), the baud rate for the CAN port is selected using the **Baud Rate** in the [Module Configuration](985x_module_config.html) dialog box. The SJA1000 bit timing registers for the corresponding baud rate are grayed out.

When **Specify Baud Rate as Bit Timing Registers** is TRUE (checked), the **Baud Rate** in the [Module Configuration](985x_module_config.html) dialog box is ignored, and two integer controls BTR0 and BTR1 set the baud rate for the CAN port. The values for **BTR0** and **BTR1** are specified as hexadecimal. For information on CAN bit timing registers, refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

#### Input Filter

This selection controls the acceptance filter registers of the SJA1000 CAN controller. The acceptance filter enables the SJA1000 to filter out certain CAN frames so that your FPGA VI can work with reduced overall traffic. The acceptance filter applies only to received frames, not transmitted frames.

The **Input Filter** selection determines how you specify the filter values in the dialog box:

**Receive All**

Receive all frames (all identifiers). This value is the default.

Register values corresponding to reception of all identifiers are shown in **SJA1000 Filter Mode**, **SJA1000 Mask**, and **SJA1000 Code** (grayed).

**Receive Selected**

Receive frames with selected identifiers. Based on a list of identifiers that you enter, the dialog will calculate values for the SJA1000 filter registers. The calculation attempts to filter out as many unwanted IDs as possible.

You select the list of identifiers using the following controls:

**ID Format**

Selects whether your CAN network uses **Standard** identifiers (11-bit) or **Extended** identifiers (29-bit).

**ID Display**

Selects whether to use **Decimal** or **Hexadecimal** for the identifiers in the **Add** control and **Selected IDs** list.

**Add From Database**

Opens a file dialog from which you can select a CANdb file (.DBC) or an NI-CAN database file (.NCD). When you click the OK button in the file dialog, the identifiers for all messages in the database are added to the **Selected IDs**.

The **Add From Database** button requires features of NI-CAN 2.3 or higher in order to import identifiers. If you do not have NI-CAN 2.3 or higher installed on your Windows system, the **Add From Database** button is grayed out.

**Add**

Enter a single identifier using the control to the right, then click this button to add the identifier to the **Selected IDs**.

**Delete**

Select a single identifier within the **Selected IDs** list, then click this button to delete that identifier from the list.

**Delete All**

Deletes all identifiers in **Selected IDs**.

**Selected IDs**

List of identifiers that you have selected using controls to the left. The dialog calculates the SJA1000 filters from this list, and the resulting register values are shown in **SJA1000 Filter Mode**, **SJA1000 Mask**, and **SJA1000 Code** (grayed).

If you change the **Input Filter** from **Receive Selected** to **SJA1000 Format**, the register values in **SJA1000 Filter Mode**, **SJA1000 Mask**, and **SJA1000 Code** retain their calculated values. This allows you to use **Receive Selected** to calculate filters for the identifiers, then change the registers directly for advanced filtering, such as checks for patterns in the data bytes.

**Number of Unwanted IDs**

Given the current filter calculation, this displays the number of identifiers that your FPGA VI will receive which are not listed in **Selected IDs**. Since the SJA1000 registers filter using bitwise masking, the filter efficiency is rarely 100%. If you use **ID Format** of **Extended**, this number can be large due to the 29 total bits used for identifiers.

**SJA1000 Format**

With this selection, you use controls to set the SJA1000 registers directly. For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

**SJA1000 Filter Mode**

Controls the Acceptance Filter Mode bit of the SJA1000 Mode register. Dual (0) specifies use of two filters, and Single (1) specifies use of a single filter.

**SJA1000 Mask**

Controls the SJA1000 Acceptance Mask 0–3 registers. The value is specified as hexadecimal. The least significant byte of the value is stored in register offset 3 (AMR3), the next least significant in offset 2 (AMR2), and so on.

**SJA1000 Code**

Controls the SJA1000 Acceptance Code 0–3 registers. The value is specified as hexadecimal. The least significant byte of the value is stored in register offset 3 (ACR3), the next least significant in offset 2 (ACR2), and so on.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_errors.html language=enus -->
## TOPIC 00013: Error Terminals

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_errors.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_errors.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Error Terminals

To detect errors, right-click the CAN node in the diagram and select **Error Terminals**. The resulting **Error In** and **Error Out** terminals provide the standard LabVIEW error cluster for error handling.

Use of **Error Terminals** for CAN development is recommended. For some CAN nodes, the error terminals are essential. For example, you need to evaluate **Error Out** from a CAN Input node to determine if a CAN frame was received within the specified **Input Timeout (ms)**. The only cost of using error terminals is slight FPGA gate usage, not performance.

When an error occurs, you can use the LabVIEW **Explain Error Help** dialog box for a description of the error code. Right-click an error cluster and select **Explain Error** from the shortcut menu for more information about the error. You also can select **Explain Error** and enter the returned error code into the dialog box.

The error descriptions in the **Explain Error** dialog box are generic to all CompactRIO (C Series) modules. The following sections provide information specific to the CAN module.

#### Module Communication Error

##### Error Code: 65536

This error will occur anytime there is a catastrophic error with communication to the CAN module. Some possible causes are:

- Unplugging the CAN module.
- Invoking a CAN node while the CompactRIO Sleep line is asserted. This error does not occur for the Sleep feature of the CAN transceiver ( Transceiver Mode property).
- Invoking a CAN node before the CAN module has reconfigured itself after the CompactRIO Sleep line deasserts (approximately 1 second).
- Invalid data transfer between LabVIEW FPGA and the CAN module.

#### Incorrect Module Error

##### Error Code: 65537

This error will occur if the user plugs in another CompactRIO module into a slot configured for a CAN module.

#### Timeout Error

##### Error Code: 65538

This error occurs when:

- CAN Input does not receive a valid CAN frame within the specified Input Timeout (ms) .
- CAN Output does not detect an available element in the output FIFO within the specified Output Timeout (ms) .
- An I/O Method or I/O Property node does not detect an available element in the output FIFO within the specified Output Timeout (ms) . Refer to Arbitration for more information.

This error is not returned when a Wait or Abort Transmit method times out. Those methods indicate a timeout in the **Timed Out?** terminal.

#### Data Overflow Error

##### Error Code 65539

This error can only occur from the CAN Input node. This indicates that you did not invoke CAN Input fast enough, and one or more CAN frames were lost. Since LabVIEW FPGA executes at a much faster rate than CAN frames are received, this can only happen when you introduce artificial delays in your FPGA VI. By invoking CAN Input at least once every 50 microseconds, this error will not occur.

#### Not Run Mode Error

##### Error Code: 65540

This error occurs when communication is stopped and you use a CAN feature that requires communication to be started first. Refer to the preceding documentation to determine which features require running communication.

Prior to using the feature ([CAN Output](985x_can_output.html), [I/O Method](/csh?topicname=lvfpga/io_method_node.html), or [I/O Property](/csh?topicname=lvfpga/io_property_node.html) node), make sure that you start communication on the CAN port. You can start communication by enabling **Auto Start** in the [Module Configuration](985x_module_config.html) or by invoking the [Start](985x_start.html) method.

#### Run Mode Error

##### Error Code 65541

This error occurs when communication is started and you use a CAN feature that requires communication to be stopped. Refer to the preceding documentation to determine which feature cannot be used while communication is running.

Prior to using the feature (usually writing a property), make sure that you stop communication on the CAN port. To set initial properties, disable **Auto Start** in the [Module Configuration](985x_module_config.html), then set the desired properties, invoke the [Start](985x_start.html) method, and proceed with your remaining application. To set properties in your main application loop, invoke the [Stop](985x_stop.html) method, set the relevant properties, then invoke the [Start](985x_start.html) method.

#### Feature Not Supported Error

##### Error Code 65546

This error is returned by the CAN Property node when a property selected for reading or writing is not supported on the specified module.

#### Too Many Error Frames Warning

##### Error Code 65547

This warning occurs when a serious fault is detected on the node, resulting in a burst of error frames. This warning indicates that one or more error frames may not be reported to LabVIEW FPGA. However, all valid CAN data frames will be reported.

Verify that cabling, baudrate, and termination of all nodes on the network are correct, and that proper bus power is supplied.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_io_methods.html language=enus -->
## TOPIC 00014: I/O Methods

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_io_methods.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_io_methods.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### I/O Methods

Complete the following steps to use an [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) for CAN:

1. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My Computer in the Project Explorer window, selecting New»FPGA I/O , and then adding CAN»NI 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or CAN»NI 9852»CAN1 (or CAN»NI 9853»CAN1 ) to the FPGA I/O list. Refer to New FPGA I/O dialog box (FPGA Module) for more information about creating and adding FPGA I/O to your CompactRIO configuration.
3. Place an I/O Method Node from the FPGA I/O palette onto your FPGA VI diagram.
4. Right-click the I/O Method Node, and select Select Item»CAN»NI 9852»CAN0 (or Select Item»CAN»NI 9853»CAN0 ) or Select Item»CAN»NI 9852»CAN1 (or Select Item»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Method Node and choose Select Method to specify the desired method from the list of CAN methods.

For information on how the I/O Method Node arbitrates with other CAN nodes, refer to [Arbitration](985x_arbitration.html).

|  | Note There are no module-specific methods for NI 9852 or NI 9853, so adding CAN»NI 9852 or CAN»NI 9853 to the FPGA I/O node and choosing Select Method will not display any methods. |
| --- | --- |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_io_properties.html language=enus -->
## TOPIC 00015: I/O Properties

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_io_properties.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_io_properties.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### I/O Properties

Complete the following steps to use an [FPGA I/O Property node](/csh?topicname=lvfpga/io_property_node.html) for CAN:

1. Use the Add Targets and Devices dialog box to add the CAN module to your CompactRIO configuration. Right-click the CAN module in the Project Explorer window and select Properties to specify the configuration properties for the module.
2. Create an FPGA I/O item for CAN by right-clicking the FPGA target under My Computer in the Project Explorer window, selecting New»FPGA I/O , and then adding CAN»NI 9852»CAN0 (or CAN»NI 9853»CAN0 ) and/or CAN»NI 9852»CAN1 (or CAN»NI 9853»CAN1 ) to the FPGA I/O list. Refer to New FPGA I/O dialog box (FPGA Module) for more information about creating and adding FPGA I/O to your CompactRIO configuration.
3. Place an I/O Property Node from the FPGA I/O palette onto your FPGA VI diagram.
4. Right-click the I/O Property Node and select Select Item»CAN»NI 9852»CAN0 (or Select Item»CAN»NI 9853»CAN0 ) or Select Item»CAN»NI 9852»CAN1 (or Select Item»CAN»NI 9853»CAN1 ).
5. Right-click the I/O Property Node and choose Select Property to specify the appropriate property from the list of available CAN properties.

For information on how the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) arbitrates with other CAN nodes, refer to [Arbitration](985x_arbitration.html).

The description of each property includes the following table.

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
| <value> | <value> | <value> | <value> |

**Data type**: Shows the icon for the LabVIEW data type used for this property.

**Permissions**: Read, Write, or Read/Write. If the property is Read/Write, you can right-click the property in the node and select **Change To Read** or **Change To Write** to select the direction. Otherwise, only one direction is supported.

**Write while stopped?**: Yes or No to indicate whether you can write the property while CAN communication is stopped. You can always read a property with Read permissions.

**Write while running?**: Yes or No to indicate whether you can write the property while CAN communication is running. You can always read a property with Read permissions.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_listen_only.html language=enus -->
## TOPIC 00016: Listen Only

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_listen_only.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_listen_only.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Listen Only

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls **Listen Only** mode for passive monitoring/logging.

The default value for this property comes from [Module Configuration](985x_module_config.html).

FALSE disables **Listen Only** mode. Received frames are acknowledged, and frames can be transmitted using **CAN Output**.

TRUE enables **Listen Only** mode. The CAN port can only receive frames. The port does not transmit on the network. No acknowledgement is transmitted when a frame is received. When listen-only is enabled, the [Comm State](985x_comm_state.html) property begins in the Error Passive state.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_log_bus_errors.html language=enus -->
## TOPIC 00017: Log Bus Errors

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_log_bus_errors.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_log_bus_errors.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Log Bus Errors

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property enables the logging of bus errors as frames that can be read using the [CAN Input](985x_can_input.html) node.

The bus error frame is logged when the Philips SJA1000 CAN controller detects a bus error and the Bus Error Interrupt occurs.

FALSE indicates that the bus errors will not be logged and cannot be read using the [CAN Input](985x_can_input.html) node (default).
TRUE indicates that the bus errors will be logged as frames and can be read using the [CAN Input](985x_can_input.html) node.

The bus error frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 4 |
| Type | 6 |
| Data | Bytes 0—Comm State (see below) 1—Transmit Error Counter 2—Receive Error Counter 3—ECC Register 4—X 5—X 6—X 7—X |

|  | Note X means Reserved or Don't Care. |
| --- | --- |

The first data byte (Comm State) indicates the current communication state of the CAN controller. The states are:

0—Error Active

1—Error Passive

2—Bus Off

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_log_transceiver_faults.html language=enus -->
## TOPIC 00018: Log Transceiver Faults

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_log_transceiver_faults.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_log_transceiver_faults.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Log Transceiver Faults

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property enables the logging of transceiver faults as frames that can be read using the [CAN Input](985x_can_input.html) node.

FALSE indicates that the transceiver faults will not be logged as frames (default).
TRUE indicates that logging is enabled and the transceiver faults will be logged as frames which can be monitored using the [CAN Input](985x_can_input.html) node.

|  | Note The TJA1041 transceivers on the NI 9853 high-speed module only detect faults during transmission. |
| --- | --- |

The transceiver fault frame has the following format:

| Arbitration ID | 0 |
| --- | --- |
| Data Length | 1 |
| Type | 7 |
| Data | Bytes 0—Transceiver fault (0=fault cleared, 1=fault present) 1—X 2—X 3—X 4—X 5—X 6—X 7—X |

|  | Note X means Reserved or Don't Care. |
| --- | --- |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_ls_ft_termination.html language=enus -->
## TOPIC 00019: LS/FT Termination

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_ls_ft_termination.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_ls_ft_termination.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### LS/FT Termination

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property enables the setting of the low-speed/fault-tolerant transceiver termination on the NI 9852 module to either 1 kiloohm (1.11 kΩ) or 5 kiloohm (4.99 kΩ).

This termination affects both R<sub>RTH</sub> and R<sub>RTL</sub>. For more information on determining the required termination for your LS/FT node, refer to the ISO 11898-3 specification (CAN fault-tolerant transmission), or refer to the *Connectors and Cables* section of the *NI-CAN Hardware and Software Manual*.

**1 kiloohm** indicates that the termination for the LS/FT CAN port will be 1 kΩ (default).

**5 kiloohm** indicates that the termination for the LS/FT CAN port will be 5 kΩ.

|  | Note This property applies only to the ports on the NI 9852 low-speed/fault-tolerant module. |
| --- | --- |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_module_config.html language=enus -->
## TOPIC 00020: Module Configuration

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_module_config.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_module_config.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Module Configuration

Separate configuration properties are provided for each CAN port on the module, labeled as tabs **CAN0** and **CAN1**. The tab labeled **Module** provides configuration properties that apply to all CAN ports on the module.

The configuration properties are downloaded to the CAN module each time your FPGA VI runs. The configuration properties are saved as part of the LabVIEW project file as well as the FPGA VI image.

This module configuration often makes it possible for you to avoid setting properties in the VI, and focus on CAN Input/Output within the FPGA VI diagram.

#### CAN Port Properties

The **CAN0** and **CAN1** tabs provide configuration properties for their respective CAN port.

##### Baud Rate

This specifies the baud rate (bit rate) to use for CAN communication. Typical CAN baud rates are listed as kilobits per second (kbps).

The default baud rate for the NI 9852 module is **125.0 kbps**, which is the typical baud rate used for low-speed transceivers. The default baud rate for the NI 9853 module is **500.0 kbps**, which is the typical baud rate used for high-speed transceivers.
If you prefer to specify the baud rate as bit timing register values, refer to [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html).

##### Auto Start

This Boolean property indicates whether to invoke the **Start** method automatically when the FPGA VI runs. The default is TRUE (enabled).

When **Auto Start** is TRUE (enabled), the **Start** method is invoked automatically when the FPGA VI runs, and the **Stop** method is invoked automatically when the FPGA VI stops running. This enables your FPGA VI diagram to begin using CAN Input and CAN Output nodes without first using an explicit **Start** method.

When **Auto Start** is FALSE (disabled), the **Start** method is *not* invoked automatically. You must use the [Start](985x_start.html) method in your FPGA VI diagram in order to start communication. The behavior for **Stop** is the same as when **Auto Start** is TRUE, in that the Stop method is invoked automatically when the FPGA VI stops running.

##### Listen Only

This Boolean control indicates whether to enable the **Listen Only** feature for passive monitoring of the network. The default is FALSE (disabled).

When **Listen Only** is FALSE (disabled), you can transmit CAN messages normally using CAN Output. When CAN messages are received, those messages are acknowledged.

When **Listen Only** is TRUE (enabled), you *cannot* transmit CAN messages. When CAN messages are received, those messages are *not* acknowledged. The Philips SJA1000 CAN controller enters error passive state when **Listen Only** is enabled. Checking **Listen Only** enables passive monitoring of network traffic, which can be useful for debugging scenarios in which only one device exists on the network.

##### LS/FT Termination

This control is applicable only for the NI 9852 low-speed/fault-tolerant modules. This control enables the setting of the LS/FT port termination to either **1 kiloohm** or **5 kiloohm**.

##### Advanced

This button displays a dialog to configure advanced properties for the CAN port. Refer to [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html) for more information.

#### Module Properties

The **Module** tab provides configuration properties that apply to all CAN ports on the module.

##### Module Clock

Performance of the I/O, methods, and properties is determined by the speed of communication between LabVIEW FPGA and the module. This speed is limited to 20MHz on the CompactRIO Reconfigurable Embedded System, and 10MHz on CompactRIO R Series Expansion system. In order to write CAN applications with consistent performance regardless of LabVIEW FPGA target, the **Module Clock** property allows you to select 10MHz for the CompactRIO Reconfigurable Embedded System.

For the CompactRIO Reconfigurable Embedded System, the default **Module Clock** is 20MHz, but you can select 10MHz for compatibility with the CompactRIO R Series Expansion system.

For the CompactRIO R Series Expansion system, the only selection for **Module Clock** is 10MHz.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_module_id.html language=enus -->
## TOPIC 00021: Module ID

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_module_id.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_module_id.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Module ID

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property returns the module identifier of the module, which is hexadecimal 71F3 for the NI 9852 CAN module and hexadecimal 714F for the NI 9853 CAN module.

This property applies to the entire module. To select a module property, right-click the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) and select **FPGA I/O»NI 9852** or **FPGA I/O»NI 9853**.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_module_properties.html language=enus -->
## TOPIC 00022: Module Properties

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_module_properties.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_module_properties.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Module Properties

These properties apply to the entire module. To select a module property, right-click the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) and select **FPGA I/O»NI 9852** or **FPGA I/O»NI 9853**.

[Module ID](985x_module_id.html)

[Serial Number](985x_serial_number.html)

[Vendor ID](985x_vendor_id.html)

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_receive_error_counter.html language=enus -->
## TOPIC 00023: Receive Error Counter

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_receive_error_counter.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_receive_error_counter.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Receive Error Counter

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property provides access to the CAN controller Receive Error Counter defined by the CAN standard.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_related_documentation.html language=enus -->
## TOPIC 00024: NI 9852/NI 9853 Related Documentation and Examples

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_related_documentation.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### NI 9852/NI 9853 Related Documentation and Examples

The following documents contain information that you might find helpful as you use LabVIEW with CompactRIO. You must have Adobe Acrobat Reader with Search and Accessibility 5.0.5 or later installed to view the PDFs. Refer to the Adobe Systems Incorporated Web site to download Acrobat Reader. Refer to the National Instruments Product Manuals Library for updated documentation resources.

- NI 9852 Operating Instructions —Refer to this document for information about using the NI 9852 module. This document is included in your hardware shipping kit. You also can access the NI 9852 Operating Instructions by selecting Start»All Programs»National Instruments»CompactRIO»CAN»NI 9852 Operating Instructions .
- NI 9853 Operating Instructions —Refer to this document for information about using the NI 9853 module. This document is included in your hardware shipping kit. You also can access the NI 9853 Operating Instructions by selecting Start»All Programs»National Instruments»CompactRIO»CAN»NI 9853 Operating Instructions .
- CompactRIO Related Documentation —Refer to this list for information about CompactRIO manuals and help resources.
- LabVIEW Help —Use the LabVIEW Help for information on how to use the LabVIEW FPGA Module, and other C Series modules.
- NI-CAN Hardware and Software User Manual —NI-CAN is the software for National Instruments PCI, PXI, and PCMCIA cards for CAN. You can download NI-CAN from ni.com/downloads . You also can access the NI-CAN manual by selecting Start»All Programs»National Instruments»NI-CAN»NI-CAN Hardware and Software Manual . The NI-CAN Hardware and Software Manual contains a general overview of CAN, plus information on frame to channel conversion. Frame to channel conversion is a software feature that you can use with the CompactRIO CAN module, even if you do not use an NI CAN PCI, PXI, or PCMCIA card. You can find information about frame to channel conversion in the Frame To Channel Conversion section of the chapter titled Using the Channel API .

#### NI 9852/NI 9853 Related Examples

The NI 9852/NI 9853 software installs several examples that provide an excellent starting point for your development. The description of each example describes the configuration required to run the example and an overview of the LabVIEW VIs.
You can find the examples for the NI 9852/NI 9853 by selecting **Help»Find Examples** in LabVIEW to launch the NI Example Finder. Select **Hardware Input and Output»CompactRIO»Module Specific»CAN** in the NI Example Finder window.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_reset.html language=enus -->
## TOPIC 00025: Reset

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_reset.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_reset.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Reset

Reset the CAN port to the same state as when the FPGA VI started running.

This method resets the SJA1000, and then restores all properties to their default values. If you enable **Auto Start** in the tool, this method will also re-start communication.

When a CAN controller enters the Bus Off state (see [Comm State](985x_comm_state.html) property), it no longer communicates. Like most CAN controllers, the SJA1000 does not allow recovery from Bus Off to Error Active using the CAN controller register set. This behavior is normal within an embedded system (vehicle), but many test setups intentionally generate Bus Off, and therefore require a mechanism to recover (i.e. to run the test again). By performing a complete reset of the SJA1000, this method recovers from the Bus Off state.

This method also clears the output FIFO as well as any pending CAN node (including all Wait methods). The reset affects only the specified CAN port, and has no effect on the other CAN port of the module.
For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_self_reception.html language=enus -->
## TOPIC 00026: Self Reception

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_self_reception.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_self_reception.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Self Reception

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property specifies whether to echo successfully transmitted CAN frames to be read using **CAN Input**. Each reception occurs just as if the frame were received from another CAN device. For self reception to operate properly, another CAN node must receive and acknowledge each transmit. If a transmitted frame is not successfully acknowledged, it is not echoed for input.

FALSE indicates transmits are not echoed (default), and TRUE indicates transmits are echoed.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_serial_number.html language=enus -->
## TOPIC 00027: Serial Number

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_serial_number.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_serial_number.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Serial Number

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property returns the serial number of the CAN module.

This property applies to the entire module. To select a module property, right-click the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) and select **FPGA I/O»NI 9852** or **FPGA I/O»NI 9853**.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_single_shot_transmit.html language=enus -->
## TOPIC 00028: Single Shot Transmit

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_single_shot_transmit.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_single_shot_transmit.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Single Shot Transmit

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | Yes |

This property specifies whether to retry failed CAN frame transmissions.

FALSE indicates standard CAN behavior, where failed CAN frame transmissions are automatically retried (default), and TRUE indicates single-shot. With single-shot enabled, if a CAN frame is not transmitted successfully, the CAN controller will not retry.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_sja1000_filter_code.html language=enus -->
## TOPIC 00029: SJA1000 Filter Code

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_sja1000_filter_code.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_sja1000_filter_code.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### SJA1000 Filter Code

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Code registers (ACR0 to ACR3). The least significant byte of the property is stored in register offset 3 (ACR3), the next least significant in offset 2 (ACR2), and so on.

The default value comes from the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html).

The mask for the SJA1000 filter is specified using the [SJA1000 Filter Mask](985x_sja1000_filter_mask.html) property, and the filter mode is specified using the [SJA1000 Filter Mode](985x_sja1000_filter_mode.html) property.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_sja1000_filter_mask.html language=enus -->
## TOPIC 00030: SJA1000 Filter Mask

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_sja1000_filter_mask.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_sja1000_filter_mask.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### SJA1000 Filter Mask

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Mask registers (AMR0 to AMR3). The least significant byte of the property is stored in register offset 3 (AMR3), the next least significant in offset 2 (AMR2), and so on.

The default value comes from the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html).

The code for the SJA1000 filter is specified using the [SJA1000 Filter Code](985x_sja1000_filter_code.html) property, and the filter mode is specified using the [SJA1000 Filter Mode](985x_sja1000_filter_mode.html) property.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_sja1000_filter_mode.html language=enus -->
## TOPIC 00031: SJA1000 Filter Mode

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_sja1000_filter_mode.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_sja1000_filter_mode.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### SJA1000 Filter Mode

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Mode register. Dual (0) specifies use of two filters, and Single (1) specifies use of a single filter.

The default value comes from the [CAN Advanced Port Configuration](985x_crio_can_advanced_port_configuration_dialog_box.html).

The code and mask for the SJA1000 filter are specified using the [SJA1000 Filter Code](985x_sja1000_filter_code.html) and the [SJA1000 Filter Mask](985x_sja1000_filter_mask.html) properties.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the datasheet of the Philips SJA1000 standalone CAN controller, available for download on www.nxp.com.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_start.html language=enus -->
## TOPIC 00032: Start

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_start.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_start.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Start

Start communication.

Cases for using this method, as opposed to enabling **Auto Start** in [Module Configuration](985x_module_config.html):

- Change configuration properties within the diagram (such as the Listen Only property)
- Auto-baud algorithms (must Stop/Start to set the baud rate for each attempt)
- Start CAN communication on a trigger (analog or digital input)

For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_stop.html language=enus -->
## TOPIC 00033: Stop

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_stop.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_stop.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Stop

Stop communication.

This method also clears the output FIFO as well as any pending CAN node (including all Wait methods).

For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_transceiver_mode.html language=enus -->
## TOPIC 00034: Transceiver Mode

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_transceiver_mode.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_transceiver_mode.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Transceiver Mode

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read/Write | No | Yes |

This property sets the mode for the CAN transceiver, as well as the associated mode in the SJA1000 CAN controller.

The values are:

| 0 | Normal |
| --- | --- |
| 1 | Sleep |

The Sleep mode places the SJA1000 and the CAN transceiver into a low-power state. This low-power state has no effect on LabVIEW FPGA hardware. The Sleep mode can be set only when the CAN controller is running (not when stopped).

A *local wakeup* occurs when you set **Transceiver Mode** from Sleep back to Normal.

A *remote wakeup* occurs when a remote node transmits a CAN frame (referred to as the wakeup frame). The wakeup frame wakes up the transceiver and CAN controller chip. The wakeup frame is not received or acknowledged by the SJA1000 CAN controller. When the wakeup frame ends, the CAN port enters Normal mode, and again receives and transmits CAN frames. If the node that transmitted the wakeup frame did not detect an acknowledgement (such as if other nodes were also waking), it will retry the transmission, and the retry will be received by the CAN port.

Once the transceiver is set into Sleep mode, you can invoke the [Wait on Transceiver Wakeup](985x_wait_on_tranceiver_wakeup.html) method to determine when a remote wakeup occurs.

After communication starts, the SJA1000 must detect a bus free condition (11 bit times) before you can change the **Transceiver Mode** to Sleep. If you set the mode to Sleep before bus free, the SJA1000 will automatically return to Normal mode. After you start communication (run FPGA with **Auto Start** enabled or invoke [Start](985x_start.html) method), you must wait at least 11 bit times before setting **Transceiver Mode** to Sleep.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_transmit_error_counter.html language=enus -->
## TOPIC 00035: Transmit Error Counter

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_transmit_error_counter.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_transmit_error_counter.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Transmit Error Counter

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property provides access to the CAN controller Transmit Error Counter defined by the CAN standard.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_vendor_id.html language=enus -->
## TOPIC 00036: Vendor ID

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_vendor_id.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_vendor_id.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Vendor ID

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read | N/A | N/A |

This property returns the vendor identifier of the module, which is hexadecimal 1093 for National Instruments.

This property applies to the entire module. To select a module property, right-click the [I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) and select **FPGA I/O»NI 9852** or **FPGA I/O»NI 9853**.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_wait_on_comm_state_change.html language=enus -->
## TOPIC 00037: Wait on Comm State Change

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_wait_on_comm_state_change.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_wait_on_comm_state_change.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Wait on Comm State Change

Wait for a change in the communication state of the CAN port ([Comm State](985x_comm_state.html) property). This enables you to handle CAN communication state changes in a separate loop from your main CAN Input/Output loop.

If the **Comm State** property changes before you call Wait (relative to the previous Wait), the current Wait returns immediately. The **Comm State** is not considered to be changed when you first Start, and it does not change after Stop.

This method returns an error if invoked while communication is stopped.

For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timeout |
| --- | --- |
|  | Specifies the time to wait for the communication state to change. The resolution is in milliseconds. The special Timeout of 0 is used to poll for the changed state. If Comm State has changed from the previous call to Wait, the Timed Out? Boolean is FALSE. If Comm State has not changed, the Timed Out? Boolean is TRUE. The Timeout value of –1 (infinite wait) is not supported, but you can use the largest positive I32 value, which provides a maximum of approximately 25 days. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timed Out? |
| --- | --- |
|  | Indicates a timeout. When Timed Out? is TRUE, the error cluster indicates success (not a timeout error). |

|  | Comm State |
| --- | --- |
|  | Returns the new value of the Comm State property. |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_wait_on_tranceiver_wakeup.html language=enus -->
## TOPIC 00038: Wait on Transceiver Wakeup

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_wait_on_tranceiver_wakeup.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_wait_on_tranceiver_wakeup.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Wait on Transceiver Wakeup

Wait for the [Transceiver Mode](985x_transceiver_mode.html) property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. A local wakeup occurs if you use the [I/O Property node](/csh?topicname=lvfpga/io_property_node.html) to set **Transceiver Mode** property back to Normal.

If a wakeup occurs before you call Wait (relative to the previous Wait), the current Wait returns immediately. The wakeup is not considered to have occurred when you first Start, and it does not occur after Stop.

This method returns an error if invoked while communication is stopped.

For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timeout |
| --- | --- |
|  | Specifies the time to wait for the Transceiver Mode to change to Normal. The resolution is in milliseconds. The special Timeout of 0 is used to poll for the wakeup. If a wakeup has occurred since the previous call to Wait, the Timed Out? Boolean is FALSE. If Transceiver Mode is still Sleep, the Timed Out? Boolean is TRUE. The Timeout value of –1 (infinite wait) is not supported, but you can use the largest positive I32 value, which provides a maximum of approximately 25 days. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timed Out? |
| --- | --- |
|  | Indicates a timeout. When Timed Out? is TRUE, the error cluster indicates success (not a timeout error). |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/985x_wait_on_transmit_complete.html language=enus -->
## TOPIC 00039: Wait on Transmit Complete

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/985x_wait_on_transmit_complete.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/985x_wait_on_transmit_complete.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### Wait on Transmit Complete

Wait for *all* frames written to CAN Output to complete transmission. You typically use this to determine when all frames have been acknowledged.

If all transmits are complete before you call Wait (relative to the previous Wait), the current wait returns immediately. All transmits are considered complete after you first Start. This method returns an error if invoked while communication is stopped.

For step by step instructions to place this method in your LabVIEW FPGA VI block diagram, refer to the [I/O Methods](985x_io_methods.html) introduction.

#### Node Inputs

|  | Error In |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timeout |
| --- | --- |
|  | Specifies the time to wait for the Transceiver Mode to change to Normal. The resolution is in milliseconds. The special Timeout of 0 is used to poll for transmit complete status. If all transmits are complete, the Timed Out? Boolean is FALSE. If one or more transmissions are pending (not successful or aborted), the Timed Out? Boolean is TRUE. The Timeout value of –1 (infinite wait) is not supported, but you can use the largest positive I32 value, which provides a maximum of approximately 25 days. |

#### Node Outputs

|  | Error Out |
| --- | --- |
|  | Optional. Not shown by default. To enable, right-click the node and select Error Terminals. |

|  | Timed Out? |
| --- | --- |
|  | Indicates a timeout. When Timed Out? is TRUE, the error cluster indicates success (not a timeout error). |

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/crio-9852.html language=enus -->
## TOPIC 00040: NI 9852

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/crio-9852.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/crio-9852.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### NI 9852

2-Port, Low-Speed/Fault-Tolerant CAN Module

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html) for either [CAN Input](985x_can_input.html) or [CAN Output](985x_can_output.html).

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| CAN0 | CAN Port 0 |
| CAN1 | CAN Port 1 |

#### I/O Methods

This device supports the following [I/O methods](985x_io_methods.html).

| Method | Description |
| --- | --- |
| Abort Transmit | Abort a pending CAN frame transmission. |
| Reset | Reset the CAN port to the same state as when the FPGA VI started running. |
| Start | Start communication. |
| Stop | Stop communication. |
| Wait on Comm State Change | Wait for a change in the communication state of the CAN port (Comm State property). |
| Wait on Transceiver Wakeup | Wait for the Transceiver Mode property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. |
| Wait on Transmit Complete | Wait for all frames written to CAN Output to complete transmission. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following properties with this device.

| Property | Description |
| --- | --- |
| Bit Timing | Specifies the baud rate as values for the Bit Timing Registers (BTR0 and BTR1). |
| Comm State | Describes the current communication state of the CAN controller. |
| Listen Only | Controls listen-only mode for passive monitoring/logging. |
| Log Bus Errors | Enables the logging of bus errors as frames that can be read using the CAN Input node. |
| Log Transceiver Faults | Enables the logging of transceiver faults as frames that can be read using the CAN Input node. |
| LS/FT Termination | Enables the setting of the low-speed/fault-tolerant transceiver termination to either 1 kiloohm (1.11 kΩ) or 5 kiloohm (4.99 kΩ). |
| Receive Error Counter | Provides access to the CAN controller Receive Error Counter. |
| Self Reception | Specifies whether to echo successfully transmitted CAN frames to be read using CAN Input. |
| Single Shot Transmit | Specifies whether to retry failed CAN frame transmissions. |
| SJA1000 Filter Code | Controls the SJA1000 Acceptance Code registers (ACR0 to ACR3). |
| SJA1000 Filter Mask | Controls the SJA1000 Acceptance Mask registers (AMR0 to AMR3). |
| SJA1000 Filter Mode | Controls the SJA1000 Acceptance Mode register. |
| Transceiver Mode | Sets the mode for the CAN transceiver and the associated mode in the SJA1000 CAN controller. |
| Transmit Error Counter | Provides access to the CAN controller Transmit Error Counter. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following properties with this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. Refer to C Series Module IDs for a list of modules and the associated IDs. |
| Serial Number | Returns the unique serial number of the CAN module. |
| Vendor ID | Returns the National Instruments vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the Single-Cycle Timed Loop.

<!--NI_TOPIC bundle=can-module-reference-and-procedures path=lv985xhelp/crio-9853.html language=enus -->
## TOPIC 00041: NI 9853

- bundle_id: `can-module-reference-and-procedures`
- source_path: `lv985xhelp/crio-9853.html`
- source_url: https://docs-be.ni.com/bundle/can-module-reference-and-procedures/raw/resource/enus/lv985xhelp/crio-9853.html
- document_id: `can-module-reference-and-procedures`
- page_type: `leaf`
- content_type: ``

### NI 9853

2-Port, High Speed CAN Module

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html) for either [CAN Input](985x_can_input.html) or [CAN Output](985x_can_output.html).

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| CAN0 | CAN Port 0 |
| CAN1 | CAN Port 1 |

#### I/O Methods

This device supports the following [I/O methods](985x_io_methods.html).

| Method | Description |
| --- | --- |
| Abort Transmit | Abort a pending CAN frame transmission. |
| Reset | Reset the CAN port to the same state as when the FPGA VI started running. |
| Start | Start communication. |
| Stop | Stop communication. |
| Wait on Comm State Change | Wait for a change in the communication state of the CAN port (Comm State property). |
| Wait on Transceiver Wakeup | Wait for the Transceiver Mode property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. |
| Wait on Transmit Complete | Wait for all frames written to CAN Output to complete transmission. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following properties with this device.

| Property | Description |
| --- | --- |
| Bit Timing | Specifies the baud rate as values for the Bit Timing Registers (BTR0 and BTR1). |
| Comm State | Describes the current communication state of the CAN controller. |
| Listen Only | Controls listen-only mode for passive monitoring/logging. |
| Log Bus Errors | Enables the logging of bus errors as frames that can be read using the CAN Input node. |
| Log Transceiver Faults | Enables the logging of transceiver faults as frames that can be read using the CAN Input node. |
| Receive Error Counter | Provides access to the CAN controller Receive Error Counter. |
| Self Reception | Specifies whether to echo successfully transmitted CAN frames to be read using CAN Input. |
| Single Shot Transmit | Specifies whether to retry failed CAN frame transmissions. |
| SJA1000 Filter Code | Controls the SJA1000 Acceptance Code registers (ACR0 to ACR3). |
| SJA1000 Filter Mask | Controls the SJA1000 Acceptance Mask registers (AMR0 to AMR3). |
| SJA1000 Filter Mode | Controls the SJA1000 Acceptance Mode register. |
| Transceiver Mode | Sets the mode for the CAN transceiver and the associated mode in the SJA1000 CAN controller. |
| Transmit Error Counter | Provides access to the CAN controller Transmit Error Counter. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following properties with this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. Refer to C Series Module IDs for a list of modules and the associated IDs. |
| Serial Number | Returns the unique serial number of the CAN module. |
| Vendor ID | Returns the National Instruments vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the Single-Cycle Timed Loop.
