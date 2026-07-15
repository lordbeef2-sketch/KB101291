# NI DOCUMENT BUNDLE: ni-p2p-streaming

<!--NI_BUNDLE_CHUNK bundle=ni-p2p-streaming start=1 end=11 -->
<!--NI_TOPIC bundle=ni-p2p-streaming path=creating-and-monitoring-peer-to-peer-streams.html language=enus -->
## TOPIC 00001: Creating and Monitoring Peer-to-Peer Streams

- bundle_id: `ni-p2p-streaming`
- source_path: `creating-and-monitoring-peer-to-peer-streams.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/creating-and-monitoring-peer-to-peer-streams.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Peer To Peer Streaming VIs to create and monitor peer-to-peer streams.Creating a Peer-to-Peer StreamComplete the following steps to create a stream.Configure the writer and reader. Refer to the hardware API documentation for information about configuring a writer or reader.Obtain the referen

### Creating and Monitoring Peer-to-Peer Streams

Use the Peer To Peer Streaming VIs to create and monitor peer-to-peer streams.

#### Creating a Peer-to-Peer Stream

Complete the following steps to create a stream.

1. Configure the writer and reader. Refer to the hardware API documentation for information about configuring a writer or reader.
2. Obtain the references to the writer and reader using methods associated with the hardware API.
3. Wire the writer and reader references to the writer and
 reader inputs of the niP2P Create Peer to Peer
 Stream
 VI. This VI associates the writer and reader with the stream. After this VI
 runs, the stream is in a Disabled or Enabled state depending on the value of
 enable stream .
4. (Optional) Use the niP2P Enable Peer to Peer Stream VI to enable the stream. You do not need to use this VI if you wire a TRUE value to the enable stream input of the niP2P Create Peer to Peer Stream VI.
5. Stop the data transmission and disable the stream using the niP2P Disable Peer to Peer Stream VI or the niP2P Flush And Disable Peer to Peer Stream VI.
6. Use the niP2P Destroy Peer to Peer Stream VI to unlink and destroy the stream.

#### Monitoring the Status of a Peer-to-Peer Stream

In LabVIEW, you can monitor peer-to-peer stream events such as overflow, underflow, and stream state using an interrupt method or a polling method.

The interrupt method uses the niP2P Handle Events VI. The niP2P Handle Events VI automatically creates an Event structure and Register for Events node when you place the niP2P Handle Events VI on the block diagram. Wire the stream session output from the niP2P Create Peer to Peer Stream VI to the event source input of the Register for Events node to access stream events. Then implement code in each event case to handle the interrupt.

The polling method uses the Property Node configured for peer-to-peer streams to determine the state of the stream during run time. Place the Property Node in a While Loop to continuously monitor the stream and create code to handle changes in stream state.

Related concepts:

- Peer-to-Peer Stream State Model

<!--NI_TOPIC bundle=ni-p2p-streaming path=ni-peer-to-peer-streaming-help.html language=enus -->
## TOPIC 00002: NI Peer-to-Peer Streaming Help

- bundle_id: `ni-p2p-streaming`
- source_path: `ni-peer-to-peer-streaming-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/ni-peer-to-peer-streaming-help.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another. Using the peer-to-peer data streaming architecture, two or more devices

### NI Peer-to-Peer Streaming Help

The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another. Using the peer-to-peer data streaming architecture, two or more devices can transfer data directly to each other without first going through the host processor.

The peer-to-peer data streaming architecture defines the topology and data exchange policies of
 the data transfer. Therefore, you can use this architecture as a common communication
 protocol between multiple devices on different platforms. For example, you can transfer
 data from multiple, synchronized digitizers to a single FPGA device to perform
 correlated signal analysis across the acquired data streams.

The peer-to-peer data streaming architecture is also useful in applications with distributed
 processing requirements. These types of applications exchange data between multiple
 devices in the system to complete a particular analysis or control operation. In
 addition, the application might have throughput or processing needs that require a
 device running parallel to the host processor in the system to perform the analysis
 while the host performs other tasks. In these cases, you can use the peer-to-peer data
 streaming architecture to ease the burden on the communication bus of the system and
 minimize the impact on other devices on the same bus.

For example, a high-throughput PXI Express-based digitizer can transfer data to an FPGA device to perform spectral analysis if the host processor is not sufficient to perform the analysis. To preserve bandwidth use on the PXI Express bus, you can use the peer-to-peer data streaming architecture to send data from the digitizer directly to the FPGA device.

Related concepts:

- Understanding the Peer-to-Peer Data Streaming Architecture
- Peer-to-Peer Data Streaming - Multiple Digitizers, Single FPGA Device Topology

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-data-streaming-digitizer-to-fpga.html language=enus -->
## TOPIC 00003: Peer-to-Peer Data Streaming - Digitizer to FPGA Device to Signal Generator Topology

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-data-streaming-digitizer-to-fpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-data-streaming-digitizer-to-fpga.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows peer-to-peer pipelining topology using multiple peer-to-peer streams with an NI digitizer, an FPGA device (such as an NI FlexRIO device), and a signal generator. The digitizer contains a writer to a stream, the FPGA device contains a reader for the digitizer stream and a w

### Peer-to-Peer Data Streaming - Digitizer to FPGA Device to Signal Generator Topology

The following figure shows peer-to-peer pipelining topology using multiple peer-to-peer streams
 with an NI digitizer, an FPGA device (such as an NI FlexRIO device), and a signal
 generator. The digitizer contains a writer to a stream, the FPGA device contains a
 reader for the digitizer stream and a writer to the signal generator stream, and the a
 signal generator contains a reader for the FPGA device stream. The writer and reader on
 the FPGA device use two different device resources on the FPGA device.

You can use this type of topology in instrument control applications.

Figure 6.

[IMAGE alt='image' src='GUID-9C7752C1-9F2A-4953-BDB4-DD4C2096FB9B-a5.gif']

Parent topic:

Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-data-streaming-multiple-digitize.html language=enus -->
## TOPIC 00004: Peer-to-Peer Data Streaming - Multiple Digitizers, Single FPGA Device Topology

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-data-streaming-multiple-digitize.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-data-streaming-multiple-digitize.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows peer-to-peer topology using multiple NI digitizers and an FPGA device (such as an NI FlexRIO device). The digitizers each contain a writer to a stream, and the FPGA device contains a separate reader for each of two streams. You can use this type of topology to offload inte

### Peer-to-Peer Data Streaming - Multiple Digitizers, Single FPGA Device Topology

The following figure shows peer-to-peer topology using multiple NI digitizers and an FPGA device
 (such as an NI FlexRIO device). The digitizers each contain a writer to a stream, and
 the FPGA device contains a separate reader for each of two streams.

You can use this type of topology to offload intensive data processing from the digitizers to the FPGA on the NI FlexRIO device without using resources on the host processor.

Figure 5.

[IMAGE alt='image' src='GUID-0AA6FCBC-52B4-4CB6-96E3-029DA8088C2A-a5.gif']

Parent topic:

Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-data-streaming-multiple-fpga-dev.html language=enus -->
## TOPIC 00005: Peer-to-Peer Data Streaming - Multiple FPGA Devices, Single Stream Topology

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-data-streaming-multiple-fpga-dev.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-data-streaming-multiple-fpga-dev.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows peer-to-peer topology using two FPGA devices (such as NI FlexRIO devices) and a single peer-to-peer stream. One device contains a writer to the stream, and the other contains a reader. You can use this type of topology to streamline data processing on FPGA devices without

### Peer-to-Peer Data Streaming - Multiple
 FPGA Devices, Single Stream Topology

The following figure shows peer-to-peer topology using two FPGA devices (such as
 NI FlexRIO devices) and a single peer-to-peer stream. One device contains a writer to
 the stream, and the other contains a reader.

You can use this type of topology to streamline data processing on FPGA devices without
 using resources on the host processor.

Figure 2.

[IMAGE alt='image' src='GUID-A56B5DF4-CFF4-406C-8093-7E383B13831E-a5.gif']

Parent topic:

Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-data-streaming-multiple-fpga.html language=enus -->
## TOPIC 00006: Peer-to-Peer Data Streaming - Multiple FPGA Devices, Multiple Streams Topology

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-data-streaming-multiple-fpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-data-streaming-multiple-fpga.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows peer-to-peer topology and pipelining using multiple FPGA devices (such as NI FlexRIO devices) and multiple peer-to-peer streams. One FPGA device contains a writer to a stream, another FPGA device contains a reader for one stream and a writer to the other stream, and the th

### Peer-to-Peer Data Streaming - Multiple FPGA Devices, Multiple Streams Topology

The following figure shows peer-to-peer topology and pipelining using multiple FPGA devices (such
 as NI FlexRIO devices) and multiple peer-to-peer streams. One FPGA device contains a
 writer to a stream, another FPGA device contains a reader for one stream and a writer to
 the other stream, and the third FPGA device contains a reader for the second stream. The
 FPGA device with both a writer and reader uses a different device resource for the
 writer than for the reader.

You can use this type of topology to increase the processing speed of data in an application.

Figure 3.

[IMAGE alt='image' src='GUID-FCB3355E-70CC-4652-AD67-8D214D1A8002-a5.gif']

Parent topic:

Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-data-streaming-single-digitizer.html language=enus -->
## TOPIC 00007: Peer-to-Peer Data Streaming - Single Digitizer, Single FPGA Device Topology

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-data-streaming-single-digitizer.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-data-streaming-single-digitizer.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows peer-to-peer topology using an NI digitizer and an FPGA device (such as an NI FlexRIO device) in a single peer-to-peer stream. The digitizer contains a writer to the stream, and the FPGA device contains a reader.You can use this type of topology to offload intensive data p

### Peer-to-Peer Data Streaming - Single Digitizer, Single FPGA Device Topology

The following figure shows peer-to-peer topology using an NI digitizer and an FPGA device (such
 as an NI FlexRIO device) in a single peer-to-peer stream. The digitizer contains a
 writer to the stream, and the FPGA device contains a reader.

You can use this type of topology to offload intensive data processing from the digitizer to the FPGA on the NI FlexRIO device without using resources on the host processor.

Figure 4.

[IMAGE alt='image' src='GUID-16D04325-F1BF-492F-B6F8-2D6A74692EA5-a5.gif']

Parent topic:

Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=peer-to-peer-stream-state-model.html language=enus -->
## TOPIC 00008: Peer-to-Peer Stream State Model

- bundle_id: `ni-p2p-streaming`
- source_path: `peer-to-peer-stream-state-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/peer-to-peer-stream-state-model.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state model for peer-to-peer streams defines the conditions under which the stream can move from one state to another and coordinates the writer, reader, and host. The peer-to-peer stream has the following states: Unlinked—The writer and reader have no connection to the stream, the host, or each

### Peer-to-Peer Stream State Model

The state model for peer-to-peer streams defines the conditions under which the stream can move
 from one state to another and coordinates the writer, reader, and host.

The peer-to-peer stream has the following states:

- Unlinked —The writer and reader have no connection to the stream, the host, or each other. You must use an application on the host to transition the stream out of the Unlinked state.
- Disabled —The writer has the hardware address of the reader and vice versa, but the stream is not prepared to accept data. When the stream is in the Disabled state, no data can flow through the stream.
- Enabled —The stream is capable of transmitting data from the writer to the reader. While the stream is in the Enabled state, data can flow from the writer to the reader. The host, reader, and writer can enable the stream when the stream is in a Disabled state.
- Flushing —The writer stops accepting new data and sends all existing data to the reader.

Use the Property Node configured for niP2P Stream to determine the state of the stream during run time.

#### Blocking and Non-Blocking State Transitions

Transitions between two states can be non-blocking or blocking. 
Non-blocking transitions, such as the transition from Enabled to Flushing, occur immediately. Blocking transitions, such as from Unlinked to Disabled, halt the application until the reader or writer completes the necessary tasks. For example, when a stream transitions from Unlinked to Disabled, it must wait on the writer or reader to initialize. Non-blocking transitions for the writer and reader occur before the next clock cycle. Blocking transitions might not finish for several clock cycles.

The following table lists the types of transitions, the blocking characteristics of the transition, and the host application VIs that can perform the transition.

| Transition | Type | VI |
| --- | --- | --- |
| Unlinked to Disabled | Blocking | niP2P Create Peer to Peer Stream |
| Disabled to Enabled | Blocking | niP2P Enable Peer to Peer Stream |
| Enabled to Flushing | Non-Blocking | niP2P Flush And Disable Peer to Peer Stream |
| Flushing to Disabled | Blocking | niP2P Flush And Disable Peer to Peer Stream |
| Enabled to Disabled | Blocking | niP2P Disable Peer to Peer Stream |
| Disabled to Unlinked | Non-Blocking | niP2P Unlink Peer to Peer Stream |

#### States of the Host

The state of the host matches the state of the stream. The host application can monitor all states of the stream and control the transitions between the stream states. When the host application begins, the stream is in an Unlinked state. The host application then transitions the stream into other states using the Peer To Peer Streaming VIs. The following illustration shows the stream states and the transitions that the host can control.

Figure 7.

[IMAGE alt='image' src='GUID-66C9477A-A6A0-4066-8341-1A3B3C36034C-a5.gif']

#### States of the Writer

The state of the writer matches the state of the stream, but the writer cannot control all the transitions between the stream states. When the host links the writer and reader, the writer transitions from the Unlinked state to the Disabled state. When the host disables the stream, the writer transitions to the Disabled state immediately. When the writer or host initiates a flush and disable command, the writer transitions to the Flushing state and then to the Disabled state when the transfer of data in the queue is complete or the command times out, whichever happens first.

You can use the following VIs to disable the stream from the host application:

- niP2P Flush And Disable Peer to Peer Stream VI—The writer remains in the Flushing state until the writer transfers all data packets in the queue or until the flush timeout expires, whichever happens first.
- niP2P Disable Peer to Peer Stream VI—The writer immediately transitions to the Disabled state and no more data transfers to the reader.

The following illustration shows the possible states of the writer and the transitions that the writer can control.

Figure 8.

[IMAGE alt='image' src='GUID-6D440EBB-44A6-4756-AE63-A829B232C5D0-a5.gif']

#### States of the Reader

The state of the reader matches the state of the stream, except for the Flushing state. Also, the reader cannot control all the transitions between the stream states. When the host links the writer and reader, the reader transitions from the Unlinked state to the Disabled state. The following illustration shows the possible states of the reader and the transitions that the reader can control.

Figure 9.

[IMAGE alt='image' src='GUID-6CEA4036-359D-4660-B70B-E1B8FB86FA35-a5.gif']

Related concepts:

- Understanding the Peer-to-Peer Data Streaming Architecture

<!--NI_TOPIC bundle=ni-p2p-streaming path=standard-error-behavior.html language=enus -->
## TOPIC 00009: Standard Error Parameter Behavior

- bundle_id: `ni-p2p-streaming`
- source_path: `standard-error-behavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/standard-error-behavior.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes contain error in or error out parameters that you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard

### Standard Error Parameter Behavior

Many LabVIEW nodes contain error in or error out parameters that you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard behavior forerror in and error out is described in the following table.

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurs before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurs before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |
|  | error out contains error information. If error in indicates that an error occurs before this node runs, error out contains the same error information. Otherwise, it describes the error status that this node produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

error in cluster contains the following cluster elements:

|  | status is TRUE if an error occurs before this node runs or FALSE to indicate a warning or that an error did not occur before the node runs. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning, and in most cases is the name of the node that produces the error or warning. The default is an empty string. |

error out contains the following cluster elements:

|  | status is TRUE if an error occurs before or while this node runs, or FALSE to indicate a warning or that no error occurred before or while this node runs. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning, and in most cases is the name of the node that produces the error or warning. |

<!--NI_TOPIC bundle=ni-p2p-streaming path=understanding-the-peer-to-peer-data-streaming.html language=enus -->
## TOPIC 00010: Understanding the Peer-to-Peer Data Streaming Architecture

- bundle_id: `ni-p2p-streaming`
- source_path: `understanding-the-peer-to-peer-data-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/understanding-the-peer-to-peer-data-streaming.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: From a system-level perspective, three components work together to ensure proper operation of a peer-to-peer data stream: the writer, the reader, and the host. 1 Peer-to-Peer Data Streaming Architecture Although the previous figure shows a host application creating a single stream, a host applicati

### Understanding the Peer-to-Peer Data Streaming Architecture

From a system-level perspective, three components work together to ensure proper operation of a peer-to-peer data stream: the writer, the reader, and the host.

Figure 1.

[IMAGE alt='image' src='GUID-037BF0FE-8198-473E-9B86-6D1DC03EA298-a5.gif']

Note

#### Writers and Readers

The writer and reader are the origin and terminus of the unidirectional data stream, respectively. The writer is the device resource that writes data to the stream. The reader is the device resource that reads data from the stream. Hardware devices that are capable of peer-to-peer data streaming can participate in multiple streams by using different resources as the writer and reader. Because the peer-to-peer data streaming architecture is unidirectional, each device resource can either write data to a stream or read data from the stream, but the same device resource cannot be both a writer and reader. Only hardware resource availability limits the number of streams that a device resource can support.

#### Hosts and Host Applications

A peer-to-peer data stream cannot exist without the presence of a host computer, such as a PXI system, running a host application. The host links the writer and reader together and maintains the stream. The host must continue to run the host application to maintain the stream, but the host processor does not participate in the actual transfer of data between the writer and reader. In addition, the host does not have access to data in the stream, the writer, or the reader. The host provides the following services:

- Provides a unified software API for stream status and control between different types of devices
- Programmatically creates streams at run time
- Manipulates stream connectivity during run time
- Increases system-level robustness and fault tolerance

You can write host applications to handle errors or faults that occur in the writer or reader. For example, the host application can manipulate the state of the reader while the stream is actively transmitting data to prevent the reader from receiving stream data if the writer encounters a problem. In this situation, the host application can shut down the stream attached to the reader in a safe and controlled way.

#### Streaming Data between Different
 Platforms

The peer-to-peer data streaming architecture uses hardware resources to
 connect the writer directly to the reader. Therefore, you can implement the writer and
 reader on different platforms, even though different hardware platforms use different
 interfaces to send and receive data and driver software varies from device to device. For
 example, you can implement the writer on a digitizer using the NI-SCOPE instrument driver
 and implement the reader on an NI FlexRIO device using LabVIEW with the LabVIEW FPGA
 Module.

To create a peer-to-peer application you must use the platform-specific
 hardware API to configure the I/O and processing algorithms for the device.

Note

After you implement the writer and
 reader using the platform-specific API, you use the Peer To Peer
 Streaming
 VIs on the host to create and control the stream. Refer to *Creating and Monitoring
 Peer-to-Peer Streams* for more information.

The hardware API is usually
 similar between devices on the same platform. Refer to the hardware API documentation for
 information about writing or reading data using the peer-to-peer data streaming
 architecture.

#### Examples of Peer-to-Peer
 Topology

Refer to the related topics for high-level examples of data flow using
 the peer-to-peer data streaming architecture.

Related concepts:

- Creating and Monitoring Peer-to-Peer Streams
- Peer-to-Peer Data Streaming - Multiple FPGA Devices, Single Stream Topology
- Peer-to-Peer Data Streaming - Multiple FPGA Devices, Multiple Streams Topology
- Peer-to-Peer Data Streaming - Single Digitizer, Single FPGA Device Topology
- Peer-to-Peer Data Streaming - Multiple Digitizers, Single FPGA Device Topology
- Peer-to-Peer Data Streaming - Digitizer to FPGA Device to Signal Generator Topology

<!--NI_TOPIC bundle=ni-p2p-streaming path=user-manual-welcome.html language=enus -->
## TOPIC 00011: NI P2P Streaming User Manual

- bundle_id: `ni-p2p-streaming`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-streaming/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI P2P Streaming User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI P2P Streaming
 User Manual

The NI P2P Streaming User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Supported Devices
- Software and Driver Downloads
- Release Notes
