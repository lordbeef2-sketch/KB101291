# NI DOCUMENT BUNDLE: labview-nxg-p2p-streaming

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-p2p-streaming start=1 end=12 -->
<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=blocking-non-blocking-state-transitions.html language=enus -->
## TOPIC 00001: Blocking and Non-Blocking State Transitions

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `blocking-non-blocking-state-transitions.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/blocking-non-blocking-state-transitions.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Transitions between two states can be non-blocking or blocking. Non-blocking transitions, such as the transition from Enabled to Flushing, occur immediately. Blocking transitions, such as from Unlinked to Disabled, halt the application until the reader or writer completes the necessary tasks. For ex

Blocking and Non-Blocking State Transitions

Transitions between two states can be non-blocking or blocking. Non-blocking transitions, such as the transition from Enabled to Flushing, occur immediately. Blocking transitions, such as from Unlinked to Disabled, halt the application until the reader or writer completes the necessary tasks.

For example, when a stream transitions from Unlinked to Disabled, it must wait on the writer or reader to initialize. Non-blocking transitions for the writer and reader occur before the next clock cycle. Blocking transitions might not finish for several clock cycles.

The following table lists the types of transitions, the blocking characteristics of the transition, and the host application nodes that can perform the transition.

| Transition | Type | Node |
| --- | --- | --- |
| Unlinked to Disabled | Blocking | Create Stream |
| Disabled to Enabled | Blocking | Enable Stream |
| Enabled to Flushing | Non-Blocking | Flush and Disable Stream |
| Flushing to Disabled | Blocking | Flush and Disable Stream |
| Enabled to Disabled | Blocking | Disable Stream |

Parent topic:

Peer-to-Peer Stream State Model

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=digitizer-to-fpga-device-to-signal-generator-topology.html language=enus -->
## TOPIC 00002: Digitizer to FPGA Device to Signal Generator Topology

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `digitizer-to-fpga-device-to-signal-generator-topology.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/digitizer-to-fpga-device-to-signal-generator-topology.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this type of topology in instrument control applications. The following figure shows peer-to-peer pipelining topology using multiple peer-to-peer streams with an NI digitizer, an FPGA device, and a signal generator. The digitizer contains a writer to a stream, the FPGA device contains a reader f

Digitizer to FPGA Device to Signal Generator Topology

Use this type of topology in instrument control applications.

The following figure shows peer-to-peer pipelining topology using multiple peer-to-peer streams with an NI digitizer, an FPGA device, and a signal generator. The digitizer contains a writer to a stream, the FPGA device contains a reader for the digitizer stream and a writer to the signal generator stream, and the signal generator contains a reader for the FPGA device stream. The writer and reader on the FPGA device use two different device resources on the FPGA device.

[IMAGE alt='1378' src='GUID-287ECE54-C8BC-4952-B73E-A9D80DC2C903-a5.svg']

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=multiple-digitizers-single-fpga-device-topology.html language=enus -->
## TOPIC 00003: Multiple Digitizers, Single FPGA Device Topology

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `multiple-digitizers-single-fpga-device-topology.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/multiple-digitizers-single-fpga-device-topology.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this type of topology to offload intensive data processing from the digitizers to the FPGA on the device without using resources on the host processor. The following figure shows peer-to-peer topology using multiple NI digitizers and an FPGA device. The digitizers each contain a writer to a stre

Multiple Digitizers, Single FPGA Device Topology

Use this type of topology to offload intensive data processing from the digitizers to the FPGA on the device without using resources on the host processor.

The following figure shows peer-to-peer topology using multiple NI digitizers and an FPGA device. The digitizers each contain a writer to a stream, and the FPGA device contains a separate reader for each of two streams.

[IMAGE alt='1378' src='GUID-20BB85D7-820C-4E06-95A9-805A98502207-a5.svg']

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=multiple-fpga-devices-multiple-streams-topology.html language=enus -->
## TOPIC 00004: Multiple FPGA Devices, Multiple Streams Topology

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `multiple-fpga-devices-multiple-streams-topology.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/multiple-fpga-devices-multiple-streams-topology.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this type of topology to increase the processing speed of data in an application. The following figure shows peer-to-peer topology and pipelining using multiple FPGA devices and multiple peer-to-peer streams. One FPGA device contains a writer to a stream, another FPGA device contains a reader fo

Multiple FPGA Devices, Multiple Streams Topology

Use this type of topology to increase the processing speed of data in an application.

The following figure shows peer-to-peer topology and pipelining using multiple FPGA devices and multiple peer-to-peer streams. One FPGA device contains a writer to a stream, another FPGA device contains a reader for one stream and a writer to the other stream, and the third FPGA device contains a reader for the second stream. The FPGA device with both a writer and reader uses a different device resource for the writer than for the reader.

[IMAGE alt='1378' src='GUID-D71CE11C-6806-456C-808C-0FE8A0400F23-a5.svg']

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=multiple-fpga-devices-single-stream-topology.html language=enus -->
## TOPIC 00005: Multiple FPGA Devices, Single Stream Topology

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `multiple-fpga-devices-single-stream-topology.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/multiple-fpga-devices-single-stream-topology.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this type of topology to streamline data processing on FPGA devices without using resources on the host processor. The following figure shows peer-to-peer topology using two FPGA devices and a single peer-to-peer stream. One device contains a writer to the stream, and the other contains a reader

Multiple FPGA Devices, Single Stream Topology

Use this type of topology to streamline data processing on FPGA devices without using resources on the host processor.

The following figure shows peer-to-peer topology using two FPGA devices and a single peer-to-peer stream. One device contains a writer to the stream, and the other contains a reader.

[IMAGE alt='1378' src='GUID-87DA6CB8-F1D4-4628-899C-7383CBF9A102-a5.svg']

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=peer-to-peer-stream-state-model.html language=enus -->
## TOPIC 00006: Peer-to-Peer Stream State Model

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `peer-to-peer-stream-state-model.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/peer-to-peer-stream-state-model.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state model for peer-to-peer streams defines the conditions under which the stream can move from one state to another and coordinates the writer, reader, and host. The peer-to-peer stream has the following states: Unlinked The writer and reader have no connection to the stream, the host, or each

Peer-to-Peer Stream State Model

The state model for peer-to-peer streams defines the conditions under which the stream can move from one state to another and coordinates the writer, reader, and host.

The peer-to-peer stream has the following states:

Unlinked

Disabled

Enabled

Flushing

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=peer-to-peer-streaming.html language=enus -->
## TOPIC 00007: NI Peer-to-Peer Streaming

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `peer-to-peer-streaming.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/peer-to-peer-streaming.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another. Using the peer-to-peer data streaming architecture, two or more devices

NI Peer-to-Peer Streaming

The peer-to-peer data streaming architecture is a method of transferring data between hardware devices. A peer-to-peer stream acts like a single, unidirectional pipe from which data can flow directly from one device to another.

Using the peer-to-peer data streaming architecture, two or more devices can transfer data directly to each other without first going through the host processor. The peer-to-peer data streaming architecture defines the topology and data exchange policies of the data transfer. Therefore, you can use this architecture as a common communication protocol between multiple devices on different platforms. For example, you can transfer data from multiple, synchronized digitizers to a single FPGA device to perform correlated signal analysis across the acquired data streams.

The peer-to-peer data streaming architecture is also useful in applications with distributed processing requirements. These types of applications exchange data between multiple devices in the system to complete a particular analysis or control operation. In addition, the application might have throughput or processing needs that require a device running parallel to the host processor in the system to perform the analysis while the host performs other tasks. In these cases, you can use the peer-to-peer data streaming architecture to ease the burden on the communication bus of the system and minimize the impact on other devices on the same bus.

For example, a high-throughput PXI Express-based digitizer can transfer data to an FPGA device to perform spectral analysis if the host processor is not sufficient to perform the analysis. To preserve bandwidth use on the PXI Express bus, you can use the peer-to-peer data streaming architecture to send data from the digitizer directly to the FPGA device.

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=single-digitizer-single-fpga-device-topology.html language=enus -->
## TOPIC 00008: Single Digitizer, Single FPGA Device Topology

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `single-digitizer-single-fpga-device-topology.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/single-digitizer-single-fpga-device-topology.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this type of topology to offload intensive data processing from the digitizer to the FPGA on the device without using resources on the host processor. The following figure shows peer-to-peer topology using an NI digitizer and an FPGA device in a single peer-to-peer stream. The digitizer contains

Single Digitizer, Single FPGA Device Topology

Use this type of topology to offload intensive data processing from the digitizer to the FPGA on the device without using resources on the host processor.

The following figure shows peer-to-peer topology using an NI digitizer and an FPGA device in a single peer-to-peer stream. The digitizer contains a writer to the stream, and the FPGA device contains a reader.

[IMAGE alt='1378' src='GUID-ED1C5D8A-F784-4791-B92F-80AA3A04ECA7-a5.svg']

Parent topic:

NI Peer-to-Peer Streaming

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=states-of-host.html language=enus -->
## TOPIC 00009: States of the Host

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `states-of-host.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/states-of-host.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state of the host matches the state of the stream. The host application can monitor all states of the stream and control the transitions between the stream states. When the host application begins, the stream is in an Unlinked state. The host application then transitions the stream into other st

States of the Host

The state of the host matches the state of the stream. The host application can monitor all states of the stream and control the transitions between the stream states.

When the host application begins, the stream is in an Unlinked state. The host application then transitions the stream into other states using the niP2P nodes. The following illustration shows the stream states and the transitions that the host can control.

[IMAGE alt='1378' src='GUID-5B8B5613-2E59-437B-856C-765246D4831F-a5.svg']

Parent topic:

Peer-to-Peer Stream State Model

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=states-of-reader.html language=enus -->
## TOPIC 00010: States of the Reader

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `states-of-reader.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/states-of-reader.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state of the reader matches the state of the stream, except for the Flushing state. The reader cannot control all the transitions between the stream states. When the host links the writer and reader, the reader transitions from the Unlinked state to the Disabled state. The following illustration

States of the Reader

The state of the reader matches the state of the stream, except for the Flushing state. The reader cannot control all the transitions between the stream states.

When the host links the writer and reader, the reader transitions from the Unlinked state to the Disabled state. The following illustration shows the possible states of the reader and the transitions that the reader can control.

[IMAGE alt='1378' src='GUID-C56CF157-8A72-4FC4-AD6D-736060620F17-a5.svg']

Parent topic:

Peer-to-Peer Stream State Model

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=states-of-writer.html language=enus -->
## TOPIC 00011: States of the Writer

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `states-of-writer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/states-of-writer.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: The state of the writer matches the state of the stream, but the writer cannot control all the transitions between the stream states. When the host links the writer and reader, the writer transitions from the Unlinked state to the Disabled state. When the host disables the stream, the writer transit

States of the Writer

The state of the writer matches the state of the stream, but the writer cannot control all the transitions between the stream states.

When the host links the writer and reader, the writer transitions from the Unlinked state to the Disabled state. When the host disables the stream, the writer transitions to the Disabled state immediately. When the writer or host initiates a flush and disable command, the writer transitions to the Flushing state and then to the Disabled state when the transfer of data in the queue is complete or the command times out, whichever happens first.

Use the Flush and Disable Stream and Disable Stream nodes to disable the stream from the host application.

The following illustration shows the possible states of the writer and the transitions that the writer can control.

[IMAGE alt='1378' src='GUID-425F97A7-2BAB-4986-9CB1-5EA901535285-a5.svg']

Parent topic:

Peer-to-Peer Stream State Model

<!--NI_TOPIC bundle=labview-nxg-p2p-streaming path=understanding-p2p-data-streaming-architecture.html language=enus -->
## TOPIC 00012: Understanding the Peer-to-Peer Data Streaming Architecture

- bundle_id: `labview-nxg-p2p-streaming`
- source_path: `understanding-p2p-data-streaming-architecture.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-p2p-streaming/raw/resource/enus/understanding-p2p-data-streaming-architecture.html
- document_id: `labview-nxg-p2p-streaming`
- page_type: `leaf`
- content_type: `concept`
- source_description: From a system-level perspective, three components work together to ensure proper operation of a peer-to-peer data stream: the writer, the reader, and the host. Although the previous figure shows a host application creating a single stream, a host application can manage multiple streams. Hosts and Ho

Understanding the Peer-to-Peer Data Streaming Architecture

From a system-level perspective, three components work together to ensure proper operation of a peer-to-peer data stream: the writer, the reader, and the host.

[IMAGE alt='1378' src='GUID-311E67EE-6D42-4965-BBC3-7E47C29754AA-a5.svg']

Note

Parent topic:

NI Peer-to-Peer Streaming

#### Hosts and Host Applications

A peer-to-peer data stream cannot exist without the presence of a host computer, such as a PXI system, running a host application. The host links the writer and reader together and maintains the stream.

The host must continue to run the host application to maintain the stream, but the host processor does not participate in the actual transfer of data between the writer and reader. In addition, the host does not have access to data in the stream, the writer, or the reader. The host provides the following services:

- Provides a unified software API for stream status and control between different types of devices.
- Programmatically creates streams at run time.
- Manipulates stream connectivity during run time.
- Increases system-level robustness and fault tolerance.

You can write host applications to handle errors or faults that occur in the writer or reader. For example, the host application can manipulate the state of the reader while the stream is actively transmitting data to prevent the reader from receiving stream data if the writer encounters a problem. In this situation, the host application can shut down the stream attached to the reader in a safe and controlled way.

#### Writers and Readers

The writer and reader are the origin and terminus of the unidirectional data stream, respectively. The writer is the device resource that writes data to the stream. The reader is the device resource that reads data from the stream.

Hardware devices that are capable of peer-to-peer data streaming can participate in multiple streams by using different resources as the writer and reader. Because the peer-to-peer data streaming architecture is unidirectional, each device resource can either write data to a stream or read data from the stream, but the same device resource cannot be both a writer and reader. Only hardware resource availability limits the number of streams that a device resource can support.
