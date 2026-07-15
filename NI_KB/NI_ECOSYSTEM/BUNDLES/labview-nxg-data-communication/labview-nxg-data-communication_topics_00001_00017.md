# NI DOCUMENT BUNDLE: labview-nxg-data-communication

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-data-communication start=1 end=17 -->
<!--NI_TOPIC bundle=labview-nxg-data-communication path=alleviating-additional-latency.html language=enus -->
## TOPIC 00001: Alleviating Additional Latency

- bundle_id: `labview-nxg-data-communication`
- source_path: `alleviating-additional-latency.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/alleviating-additional-latency.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Network streams utilize network bandwidth as efficiently as possible while still maintaining reasonable latency. For example, when the write node writes data to the stream, the stream may hold onto the data for some time before transmitting it across the network. The stream holds the data to bundle

Alleviating Additional Latency

Network streams utilize network bandwidth as efficiently as possible while still maintaining reasonable latency.

For example, when the write node writes data to the stream, the stream may hold onto the data for some time before transmitting it across the network. The stream holds the data to bundle multiple writes in succession together and sends it as a single large TCP packet across the network rather than a series of smaller packets.

While this helps to minimize the amount of bandwidth wasted due to TCP packet overhead, it also increases the default latency for low-throughput data streams. If the stream is being used to communicate commands between the two applications, this additional latency may be undesirable. Follow the steps below to alleviate this additional latency.

1. Add the Flush Stream node to the diagram immediately after the write node and wire the two nodes together.
2. Right-click the timeout in ms input on the Flush Stream node to create a constant.
3. Give the timeout in ms input a timeout of 
 0.

[IMAGE alt='1378' src='GUID-ADE6085C-9983-428D-AF27-B15C007ACE13-a5.png']

The Flush Stream node forces the writer endpoint to immediately send all data to the reader endpoint without waiting for the data to be received or read from the reader endpoint. This programming technique provides the lowest latency possible for sending the data without blocking execution of the writer application. However, it also uses more memory. Use the element allocation mode of the Create Network Stream Writer Endpoint and Create Network Stream Reader Endpoint nodes to allocate initial buffer memory based on the data type input.

Note

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=components-that-commonly-affect-throughput.html language=enus -->
## TOPIC 00002: Components That Commonly Affect Throughput

- bundle_id: `labview-nxg-data-communication`
- source_path: `components-that-commonly-affect-throughput.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/components-that-commonly-affect-throughput.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: The components that most commonly limit the throughput of a network stream are shown and described below. The writer application contains the writer endpoint. It typically involves a loop, which will call the write node. The write node represents the cost of accepting data from the writer applicatio

Components That Commonly Affect Throughput

The components that most commonly limit the throughput of a network stream are shown and described below.

[IMAGE alt='1378' src='GUID-917FE9AF-2E70-4A01-B00D-3CDA5C113CFE-a5.svg']

|  | The writer application contains the writer endpoint. It typically involves a loop, which will call the write node. |
| --- | --- |
|  | The write node represents the cost of accepting data from the writer application and transferring it to the writer endpoint. |
|  | The network stream protocol asynchronously moves data from the writer endpoint to the reader endpoint and sends acknowledgment and flow control messages from the reader endpoint to the writer endpoint. |
|  | The read node represents the cost of removing data from the reader endpoint and transferring it to the reader application. |
|  | The reader application contains the reader endpoint. It typically involves a loop, which calls the read node. |

The writer application, network stream protocol, and reader application are all asynchronous processes that run in parallel to each other. The overall stream throughput is dictated by the slowest process. Here, the time to execute the write node is included as part of the writer application, and the time to execute the read node is included as part of the reader application.

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=data-types-highest-throughput.html language=enus -->
## TOPIC 00003: Data Types with the Highest Throughput

- bundle_id: `labview-nxg-data-communication`
- source_path: `data-types-highest-throughput.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/data-types-highest-throughput.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: The data type of the stream directly impacts its performance. For example, more complicated data types tend to have poorer throughput than simpler data types because the read and write nodes must flatten and unflatten the data communicated across the network. Therefore, streams with the highest thro

Data Types with the Highest Throughput

The data type of the stream directly impacts its performance. For example, more complicated data types tend to have poorer throughput than simpler data types because the read and write nodes must flatten and unflatten the data communicated across the network.

Therefore, streams with the highest throughput have the following data types:

- Numeric scalars
- Booleans
- 1D arrays of numeric scalars
- 1D arrays of Booleans

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=determining-endpoint-efficiency.html language=enus -->
## TOPIC 00004: Determining Endpoint Efficiency

- bundle_id: `labview-nxg-data-communication`
- source_path: `determining-endpoint-efficiency.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/determining-endpoint-efficiency.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Network Streams Properties node to display endpoint information. This node helps you determine how effectively data is delivered over the stream. Complete the following steps to determine the efficiency of an endpoint. Place a Network Stream Properties node inside the writer loop and wire it

Determining Endpoint Efficiency

Use the Network Streams Properties node to display endpoint information. This node helps you determine how effectively data is delivered over the stream.

[IMAGE alt='1378' src='GUID-27B551A7-AC62-4066-90C6-364BF0FEB56E-a5.png']

1. Place a Network Stream Properties node inside the writer loop and wire it to the writer endpoint output.
2. Display the Buffer Size and the Available Elements for Writing properties on the Network Stream Properties node.
3. Add a Subtract node to the diagram.
4. Wire the Buffer Size output of the Network Stream Properties node to the x input of the Subtract node.
5. Wire the Available Elements for Writing output of the Network Stream Properties node to the y input of the Subtract node.
6. Add an indicator to the Subtract node to obtain the number of elements in the buffer of the writer endpoint.

The number of elements in the buffer indicates how efficiently an endpoint works. If the writer application is faster than the reader application, the write buffer will fill up. If the reader application is faster than the writer application, the read node will empty and then timeout as it waits for new data. To fix either scenario, change the endpoint buffer size to increase or decrease the number of elements.

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=fixed-cost-calling-read-write.html language=enus -->
## TOPIC 00005: The Fixed Cost of Calling Read and Write

- bundle_id: `labview-nxg-data-communication`
- source_path: `fixed-cost-calling-read-write.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/fixed-cost-calling-read-write.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: There is a fixed cost to calling the read or write node, regardless of how much data is transferred with each read or write call. Frequently calling read or write with relatively small data sets increases the fixed overhead overtime, which creates a bottleneck. Conversely, calling read or write with

The Fixed Cost of Calling Read and Write

There is a fixed cost to calling the read or write node, regardless of how much data is transferred with each read or write call.

- Processor utilization
- Numbers of elements read or written per call
- Endpoint buffer size

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=network-stream-endpoint-url-specifications.html language=enus -->
## TOPIC 00006: Network Stream Endpoint URL Specifications

- bundle_id: `labview-nxg-data-communication`
- source_path: `network-stream-endpoint-url-specifications.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/network-stream-endpoint-url-specifications.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Users must specify the URL for each endpoint in order for the endpoints to connect. When two endpoints connect, they create a network stream. The Network Stream Endpoint URL has the following syntax: ni.dex://host_name:context_name/endpoint_name URL Component Description ni.dex The protocol of the U

Network Stream Endpoint URL Specifications

Users must specify the URL for each endpoint in order for the endpoints to connect. When two endpoints connect, they create a network stream.

The Network Stream Endpoint URL has the following syntax:

ni.dex://host_name:context_name/endpoint_name

| URL Component | Description |
| --- | --- |
| ni.dex | The protocol of the URL. The dex protocol identifies the URL as an endpoint URL. |
| host_name | The DNS name or IP address of the computer where the endpoint resides. The default value for this component is localhost, which routes to the network location of the computer where the endpoint resides. |
| context_name | A string value that refers to the application where the endpoint resides. This component is an empty string unless you specify a URL that includes a context name with the writer name or the reader name inputs. Note Only one application on each computer can specify the default context. If you have multiple applications on a single computer using network streams, you must assign a URL instead of a name to each endpoint. |
| endpoint_name | The name that you assign to the endpoint with the writer name or the reader name inputs of the Create Network Stream Reader Endpoint and Create Network Stream Writer Endpoint nodes. |

Parent topic:

Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=network-stream-endpoints.html language=enus -->
## TOPIC 00007: Network Stream Endpoints

- bundle_id: `labview-nxg-data-communication`
- source_path: `network-stream-endpoints.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/network-stream-endpoints.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: When two endpoints connect, they create a network stream. Network streams must have a writer endpoint that writes data to a stream and a reader endpoint that reads data from the stream. Each endpoint is identified by a URL, which establishes a connection between two compatible endpoints. The order o

Network Stream Endpoints

When two endpoints connect, they create a network stream. Network streams must have a writer endpoint that writes data to a stream and a reader endpoint that reads data from the stream.

Each endpoint is identified by a URL, which establishes a connection between two compatible endpoints. The order of creating endpoints is not important.

When the network disconnects, and an endpoint becomes inactive, the other endpoint continuously tries to reestablish communication with the inactive endpoint in the background. This background process continues until the connection is repaired or until the inactive endpoint is destroyed.

Note

Network Streams Properties

[IMAGE alt='1378' src='GUID-7F5C6B8F-3271-4C6B-AFAF-3F335BD1548B-a5.png']

Parent topic:

Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=network-streams.html language=enus -->
## TOPIC 00008: Network Streams

- bundle_id: `labview-nxg-data-communication`
- source_path: `network-streams.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/network-streams.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: Network streams enable lossless, high-throughput data communication over Ethernet. Network streams also enable lossless, low-throughput communication, such as sending commands. Network streams use a one-way, point-to-point buffered communication model to transmit data between applications. This mean

Network Streams

Network streams enable lossless, high-throughput data communication over Ethernet. Network streams also enable lossless, low-throughput communication, such as sending commands.

Network streams use a one-way, point-to-point buffered communication model to transmit data between applications. This means that one of the endpoints is the writer of data and the other is the reader. When two endpoints connect, they create a network stream. Network streams feature connection management that automatically restores network connectivity if a disconnection occurs due to a network outage or other system failure. Network streams use a buffered, lossless communication strategy that ensures data written to the stream is not lost due to intermittent network connectivity.

Because network stream characteristics are comparable to those of TCP, they are ideal for high-throughput applications for which to avoid TCP complexity.

Parent topic:

Communicating over a Network

<!--NI_TOPIC bundle=labview-nxg-data-communication path=networkcomms.html language=enus -->
## TOPIC 00009: Communicating over a Network

- bundle_id: `labview-nxg-data-communication`
- source_path: `networkcomms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/networkcomms.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: There are multiple ways to communicate data over a network and each method offers different benefits. Use the following topics to determine which communication method best suits your application. TCP Network Communication UDP Network Communication Network Streams

Communicating over a Network

There are multiple ways to communicate data over a network and each method offers
 different benefits.

Use the following topics to determine which communication method best suits your application.

- TCP Network Communication
- UDP Network Communication
- Network
 Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=performance-considerations-network-streams.html language=enus -->
## TOPIC 00010: Performance Considerations for Network Streams

- bundle_id: `labview-nxg-data-communication`
- source_path: `performance-considerations-network-streams.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/performance-considerations-network-streams.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your network stream's performance requires careful consideration of its throughput and latency measurements. Throughput and latency depend on the specifications of the systems involved in the communication, the network interface used for the communication, and the overall congestion and reliability

Performance Considerations for Network Streams

Your network stream's performance requires careful consideration of its throughput and latency measurements.

Throughput and latency depend on the specifications of the systems involved in the communication, the network interface used for the communication, and the overall congestion and reliability of the network itself.

- Components That Commonly Affect Throughput —The
 following diagram breaks down the components of a network stream and how they
 affect its performance.
- Determining Endpoint Efficiency —Display endpoint information to
 see how effective a stream is performing.
- Tolerating Temporary Network Outages —Modify
 endpoint buffer sizes to tolerate network outages.
- The
 Fixed Cost of Calling Read and Write —The cost of calling read and
 write over time affects network stream performance.
- Data
 Types with the Highest Throughput —Choose a data type with the best
 throughput.
- Alleviating Additional Latency —Choose how quickly a stream
 flushes its data across the network.

Parent topic:

Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=sending-commands-network-stream.html language=enus -->
## TOPIC 00011: Sending Commands Using a Network Stream

- bundle_id: `labview-nxg-data-communication`
- source_path: `sending-commands-network-stream.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/sending-commands-network-stream.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Network streams enable high-throughput, but you can use network streams for lossless, low-throughput communication to send and receive commands. To send commands using network streams, you must develop code to write and read data on the host and target applications. What to Use Create Network Stream

Sending Commands Using a Network Stream

Network streams enable high-throughput, but you can use network streams for lossless, low-throughput communication to send and receive commands.

To send commands using network streams, you must develop code to write and read data on the host and target applications.

#### What to Use

- Create Network Stream Writer Endpoint
- Create Network Stream Reader Endpoint
- Write Single Element to Stream
- Read Single Element from Stream
- Flush Stream
- Destroy Stream Endpoint
- While Loop
- Event Structure
- Case Structure

#### What to Do

1. Create the controls to send commands on the panel of the host application. The controls you use are entirely dependent on the goals and requirements of your application.
2. Create the following diagram in a VI for the host application. This diagram illustrates the network stream code on the host application. 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The Create Network Stream Writer Endpoint node creates the writer
 endpoint in host application.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 The writer endpoint establishes a connection with the reader endpoint using the reader URL.
 Refer to the 
 *Details* tab of the [Create Network Stream Writer Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-WRITER-ENDPOINT.html) or the [Create Network Stream Reader Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-READER-ENDPOINT.html) nodes for help specifying endpoint URLs.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 The Event Structure has one or more subdiagrams, or event cases. Only one event case executes when the structure executes to handle an event. You must place the Event Structure in a While Loop to handle multiple events. Configure the Event Structure to send commands to the target application. The code you write is entirely dependent on the goals and requirements of your application.
 org.dita.html5/xsl/topic.xsl 455Note To configure event cases and events,
 refer to [Executing Code Based on an
 Event](/csh?topicname=EXECUTE-CODE-BASED-ON-EVENT.html) for more information.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 The Write Single Element to Stream node will write the command to the buffer, depending on the event case the user selects, which the reader endpoint on the target application reads from.
 org.dita.html5/xsl/topic.xsl 455Note 
 You can use the Write Multiple Elements to the Stream node to add more than one data point at a time.
 [IMAGE alt='1378' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 If you want to minimize latency and ensure that commands propagate over the network immediately, place the Flush Stream node directly after the Write Single Element to Stream node. If low-latency is not a goal or requirement for your application, you can place the Flush Stream node outside of the While Loop.
 org.dita.html5/xsl/topic.xsl 455Note Use this node before using the Destroy Stream Endpoint node to ensure that the writer endpoint buffer is empty before you destroy it. This prevents data loss.
 [IMAGE alt='1378' src='GUID-F2CDD9BB-5D12-4E8D-8D71-2A02539C495D-a5.svg']
 If you want to shut down the network stream, call the Destroy Stream Endpoint to destroy the writer endpoint. To destroy a stream completely, however, you must destroy both the reader and writer endpoints.
3. Create the following diagram in a VI for the target application. This diagram illustrates the entire network stream code on the target application. 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The Create Network Stream Reader Endpoint node creates the reader endpoint on the target application. Once the reader endpoint exists, the writer endpoint will attempt to connect with it.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 The Read Single Element from Stream node continuously consumes commands from the buffer originally sent from the writer loop.
 org.dita.html5/xsl/topic.xsl 455Note 
 The Read Multiple Elements from Stream node consumes batches of data from the buffer. You can use this node even if you used the Write Single Element to Stream node in the writer loop.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 A Case Structure contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes. Case Structures behave similarly to 
 switch statements or 
 if-then-else statements in other programming languages. The data type of the value you wire to the selector terminal defines various cases that are available in the Case Structure. Use the case selector label to define the various cases in which different code executes. Place the code you want to execute in each case on the corresponding subdiagram of the Case Structure.
 org.dita.html5/xsl/topic.xsl 455Note In this example, the first Case Structure handles the data out and error out outputs of the Read Single Element from Stream node. The second Case Structure parses the commands.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 If you want to shut down the network stream, call the Destroy Stream Endpoint to destroy the writer endpoint. To destroy a stream completely, however, you must destroy both the reader and writer endpoints.

After you configure your target VI to meet your application's needs, you can use a network stream to send and receive commands. After you finish developing your host and target applications, your applications can send and receive commands. Be sure to run the target application first to ensure that the writer endpoint can locate the reader endpoint.

#### Troubleshooting

- If you have trouble establishing a connection, try the following troubleshooting strategies:
  - Make sure you are using the recommended firewall settings .
  - (Windows 7) Make sure your Ethernet adapters are set to a "Home" or "Work" setting. If your network is set to Private, you may receive an error.
  - Make sure your endpoint URL is specified properly. Refer to the 
 *Details* tab of the [Create Network Stream Writer Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-WRITER-ENDPOINT.html) or the [Create Network Stream Reader Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-READER-ENDPOINT.html) nodes for help specifying endpoint URLs.
  - Make sure you are not reusing endpoint names. If a name collision occurs, your intended endpoints will not connect and will error out. To avoid name collisions, consider using globally unique identifiers (GUID).
  - Make sure the endpoints you want to use are not connected to other endpoints. An endpoint can only connect to one other endpoint at a time.
  - Make sure you are specifying an endpoint that exists.
  - Make sure you are using compatible endpoints.
    - You cannot connect two reader endpoints to each other nor two writer endpoints to each other. You must use a writer endpoint and a reader endpoint.
    - The endpoints must have the same data type.
- If you have trouble streaming data after establishing a connection, try the following troubleshooting strategies:
  - Make sure the nodes are compatible with one another. You cannot wire a Read Multiple Elements from Stream node or a Read Single Element from Stream node to a Create Network Stream Writer Endpoint node. You also cannot wire a Write Multiple Elements to Stream node, a Write Single Element to Stream node, or a Flush Stream node to a Create Network Stream Reader Endpoint node.
  - Make sure you are not reading or writing a number of elements larger than the endpoint buffer size .

#### Examples

Search within the programming environment to access the following installed example:

- Simple Network Streams

Parent topic:

Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=streaming-data-using-network-stream.html language=enus -->
## TOPIC 00012: Streaming Data Using a Network Stream

- bundle_id: `labview-nxg-data-communication`
- source_path: `streaming-data-using-network-stream.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/streaming-data-using-network-stream.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Use network streams to stream data between two or more applications. To transmit data using network streams, you must develop the code to write and read data on both the host and target applications. What to Use Create Network Stream Writer Endpoint Create Network Stream Reader Endpoint Destroy Stre

Streaming Data Using a Network Stream

Use network streams to stream data between two or more applications.

To transmit data using network streams, you must develop the code to write and read data on both the host and target applications.

#### What to Use

- Create Network Stream Writer Endpoint
- Create Network Stream Reader Endpoint
- Destroy Stream Endpoint
- Flush Stream
- Read Single Element from Stream
- Write Single Element to Stream
- While Loop

#### What to Do

1. Create the following diagram in a VI for the target application. This diagram illustrates the entire network stream code on the target application. 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 TheCreate Network Stream Writer Endpoint node creates the writer endpoint in the target application.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 The writer endpoint establishes a connection with the reader endpoint using the reader URL.
 Refer to the 
 *Details* tab of the [Create Network Stream Writer Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-WRITER-ENDPOINT.html) or the [Create Network Stream Reader Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-READER-ENDPOINT.html) nodes for help specifying endpoint URLs.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 The Write Single Element to Stream node continuously adds one data point to the FIFO buffer, which the reader endpoint on the host application reads from.
 org.dita.html5/xsl/topic.xsl 455Note 
 You can use the Write Multiple Elements to the Stream node to add more than one data point at a time.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 To specify the amount of time to wait between loop iterations, wire the desired time duration to the input of the Wait node. The Wait node waits until the value of the operating system's counter increases by an amount equal to the input you specify.
 [IMAGE alt='1378' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 Data streams continuously until the user clicks the Stop button on the target application, which notifies the reader endpoint on the host application that the stream is no longer valid.
 org.dita.html5/xsl/topic.xsl 455Note You can also use the Stop button on the host application to stop streaming data.
 [IMAGE alt='1378' src='GUID-F2CDD9BB-5D12-4E8D-8D71-2A02539C495D-a5.svg']
 The Flush Stream node transfers all data to the reader endpoint before data flow resumes. It ensures that all data still residing in the writer endpoint buffer immediately transfer across the network. The Flush Stream node then waits until either the specified wait condition is met or the timeout expires.
 org.dita.html5/xsl/topic.xsl 455Note Use this node before the Destroy Stream Endpoint node to ensure the reader endpoint receives all data before destroying the writer endpoint. This prevents data loss.
 [IMAGE alt='1378' src='GUID-91842EB6-EE23-4D5B-977F-495F8F2BE07D-a5.svg']
 The Destroy Stream Endpoint node destroys the writer endpoint. To destroy a stream completely, however, you must destroy both the reader and writer endpoints.
2. Create the following diagram in a VI for the host application. This diagram illustrates the network stream code on the host application. 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The Create Network Stream Reader Endpoint node creates the reader endpoint on the host application. Once the reader endpoint exists, the writer endpoint will attempt to connect with it.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 The Read Single Element from Stream node continuously consumes data from the FIFO buffer originally sent from the writer loop.
 org.dita.html5/xsl/topic.xsl 455Note 
 The Read Multiple Elements from Stream node consumes batches of data from the buffer. You can use this node even if you used the Write Single Element to Stream node in the writer loop.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 When the Destroy Stream Endpoint node destroys the writer endpoint, the reader endpoint receives an error, which causes the data flow to exit the While Loop.
 org.dita.html5/xsl/topic.xsl 455Note When the network disconnects, an endpoint becomes inactive. The other endpoint continuously tries to reestablish communication with the inactive endpoint in the background. This background process continues until the connection is repaired or until the inactive endpoint is destroyed.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 The Destroy Stream Endpoint node destroys the reader endpoint, which destroys the stream.

After you finish developing your target and host applications, your target and host applications communicate using a network stream when you run the applications simultaneously. Be sure to run the target application first to ensure the writer endpoint can locate the reader endpoint.

#### Troubleshooting

- If you have trouble establishing a connection, try the following troubleshooting strategies:
  - Make sure you are using the recommended firewall settings .
  - (Windows 7) Make sure your Ethernet adapters are set to a "Home" or "Work" setting. If your network is set to Private, you may receive an error.
  - Make sure your endpoint URL is specified properly. Refer to the 
 *Details* tab of the [Create Network Stream Writer Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-WRITER-ENDPOINT.html) or the [Create Network Stream Reader Endpoint](/csh?topicname=CREATE-NETWORK-STREAM-READER-ENDPOINT.html) nodes for help specifying endpoint URLs.
  - Make sure you are not reusing endpoint names. If a name collision occurs, your intended endpoints will not connect and will error out. To avoid name collisions, consider using globally unique identifiers (GUID).
  - Make sure the endpoints you want to use are not connected to other endpoints. An endpoint can only connect to one other endpoint at a time.
  - Make sure you are specifying an endpoint that exists.
  - Make sure you are using compatible endpoints.
    - You cannot connect two reader endpoints to each other nor two writer endpoints to each other. You must use a writer endpoint and a reader endpoint.
    - The endpoints must have the same data type.
- If you have trouble streaming data after establishing a connection, try the following troubleshooting strategies:
  - Make sure the nodes are compatible with one another. You cannot wire a Read Multiple Elements from Stream node or a Read Single Element from Stream node to a Create Network Stream Writer Endpoint node. You also cannot wire a Write Multiple Elements to Stream node, a Write Single Element to Stream node, or a Flush Stream node to a Create Network Stream Reader Endpoint node.
  - Make sure you are not reading or writing a number of elements larger than the endpoint buffer size .

#### Examples

Search within the programming environment to access the following installed example:

- Simple Network Streams

Parent topic:

Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=tcp-network-communication.html language=enus -->
## TOPIC 00013: TCP Network Communication

- bundle_id: `labview-nxg-data-communication`
- source_path: `tcp-network-communication.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/tcp-network-communication.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: Transmission Control Protocol (TCP) is a connection-based protocol that ensures reliable transmission across networks, delivering data in sequence without errors, loss, or duplication. Use TCP for applications that require a reliable stream of data between programs running on different computers or

TCP Network Communication

Transmission Control Protocol (TCP) is a connection-based protocol that ensures reliable transmission across networks, delivering data in sequence without errors, loss, or duplication. 
 Use TCP for applications that require a reliable stream of data between programs running on different computers or different targets within a system. TCP permits multiple, simultaneous connections between computers and targets. You can use TCP to send byte streams between a client and a server.

TCP clients and servers must establish a connection before transferring data. Establishing a connection involves listening for a connection on the server and opening a connection on the client at the port where the server is listening. After establishing a connection, the client can reliably send commands to and receive responses from the server. Unlike in TCP network communication, UDP senders and receivers do not need to establish a connection before transferring data. If you don't need highly reliable network communication and want to transfer data with lower latency, you can use UDP network communication.

Parent topic:

Communicating over a Network

<!--NI_TOPIC bundle=labview-nxg-data-communication path=tolerating-temporary-network-outages.html language=enus -->
## TOPIC 00014: Tolerating Temporary Network Outages

- bundle_id: `labview-nxg-data-communication`
- source_path: `tolerating-temporary-network-outages.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/tolerating-temporary-network-outages.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Preventing data loss is one of the benefits of using network streams, especially since you can account for temporary network outages. To tolerate temporary network outages, consider the following: Determine the minimum average rate of data transfer your network stream performs. Determine how long of

Tolerating Temporary Network Outages

Preventing data loss is one of the benefits of using network streams, especially since you can account for temporary network outages.

To tolerate temporary network outages, consider the following:

1. Determine the minimum average rate of data transfer your network stream performs.
2. Determine how long of a network outage you want to account for.
3. Using those two figures, multiply them to determine your minimum endpoint buffer size.

For example, if you continuously acquire 100 kB/s of voltage data from a measurement device, you may find that you only need 10 kB endpoint buffers to sustain the data transfer under ideal conditions. However, if you want to tolerate outages of up to 10 seconds without losing data from your measurement device, you'll need a minimum writer endpoint buffer size of 1 MB.

Parent topic:

Performance Considerations for Network Streams

<!--NI_TOPIC bundle=labview-nxg-data-communication path=transferring-data-over-network-tcp.html language=enus -->
## TOPIC 00015: Transferring Data over a Network Using TCP

- bundle_id: `labview-nxg-data-communication`
- source_path: `transferring-data-over-network-tcp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/transferring-data-over-network-tcp.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Transmission Control Protocol (TCP) to reliably transfer data between a client and a server. To transmit data using TCP, you must develop the code to send and receive data on both the client and the server. What to Use TCP Open Connection TCP Listen TCP Read TCP Write TCP Close Connection What t

Transferring Data over a Network Using TCP

Use Transmission Control Protocol (TCP) to reliably transfer data between a client and a server.

To transmit data using TCP, you must develop the code to send and receive data on both the client and the server.

#### What to Use

- TCP Open Connection
- TCP Listen
- TCP Read
- TCP Write
- TCP Close Connection

#### What to Do

1. Create the following diagram in a VI targeted to the host processor. This diagram illustrates TCP code on the server side. 
 Customize the gray sections for your unique programming goals. 
 [IMAGE alt='1378' src='GUID-DC67E3F7-0E0F-4BDE-A57B-E6293852A58C-a5.png'] 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The TCP Listen node waits for an incoming connection on a specific port. The port you specify on the server must match the port you specify on the client.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 TCP Read nodes read data from the specified port and retrieve commands from the client. You must specify the number of bytes to read. Make sure to read commands in accordance with your message handling strategy. For example, if a size prefix precedes a command, read the length first and then read the amount of data the length indicates.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 TCP Write nodes write data to the specified port and send responses to the client. Make sure you send data in accordance with your message handling strategy. For example, if the client reads a response prefix to know how many bytes are in the response, make sure to prepend the length of the response to the response.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 If any unread data remains and the connection closes, you may be unable to access that data. Make sure to read all data the client sends before closing the connection.
2. Create the following diagram in a VI targeted to a processor, such as a real-time controller or a remote PC. This diagram illustrates TCP code on the client side. 
 Customize the gray sections for your unique programming goals. 
 [IMAGE alt='1378' src='GUID-BB175FC8-5E31-41F3-AA99-A08957959259-a5.png'] 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The TCP Open Connection node opens a connection to the server at the port and address you specify. The address must match the IP address of the server, and the port you specify on the client must match the port you specify on the server.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 TCP Write nodes write data to the specified port and send commands to the server. Make sure to format commands according to the messaging strategy for your application, as described in the next table row.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 TCP Read nodes read data from the specified port and retrieve responses from the client. You must specify the number of bytes to read. 
 Use one of the following strategies to handle messages of different sizes:Precede each command and response with a fixed-size prefix that indicates the size of the rest of the command or response you want to send. This allows the client to read the number of bytes in the command or response first and then specify the appropriate number of bytes to read for the rest of the command or response.Make each command and response a fixed size. When a command or response is smaller than the size you specify, you can pad it to the fixed size. This option is the most efficient but isn't as flexible as the previous option.Follow each command and response with a specific terminating character. Read data in small units until you reach the terminating character.You can display the response data from the server on the client UI or further process the response data locally.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 If any unread data remains and the connection closes, you may be unable to access that data. Make sure to read all data the server sends before closing the connection.

After you finish developing your server and client applications, your client and server applications will communicate using TCP when you run the applications simultaneously. Be sure to run the server application first to ensure that TCP Open Connection on the client is able to locate the listener.

#### Troubleshooting

- If you have trouble establishing a connection, try the following troubleshooting strategies:
  - Make sure the TCP Listen node on the server executes before the TCP Open Connection node executes on the client. If TCP Open Connection executes first, it will return an error because it cannot locate the listener.
  - Verify that the IP address you specify for TCP Open Connection on the client matches the IP address of the server. Note that different IP addresses that refer to the same computer are not compatible. For example, if you create a connection that listens to localhost and write to the numeric IP address of the local computer, such as 10.113.0.53, the client and server do not establish a connection.
  - Verify that the port you specify for TCP Open Connection on the client matches the port you specify for TCP Listen on the server.
  - Verify that the ports you have specified are valid, open ports. Valid TCP ports range from 0 to 65535. To dynamically locate an open port, use port 0 and provide a service name for any TCP Open Connection and TCP Listen nodes as illustrated by the images above.
- If you have trouble transferring data after establishing a connection, make sure the bytes to read input on each TCP Read node receives a value greater than zero. If you wire a value of zero or leave the input unwired, the node does not read anything and does not produce an error.

#### Examples

Search within the programming environment to access the following installed examples:

- Simple TCP
- TCP Named Service
- TCP Multiple Connections

Parent topic:

TCP Network Communication

<!--NI_TOPIC bundle=labview-nxg-data-communication path=transferring-data-over-network-udp.html language=enus -->
## TOPIC 00016: Transferring Data over a Network Using UDP

- bundle_id: `labview-nxg-data-communication`
- source_path: `transferring-data-over-network-udp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/transferring-data-over-network-udp.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the User Datagram Protocol (UDP) to transfer data to a single client, known as unicast communication, or between a number of processes or processors that have opted into a group or receivers, known as multicast communication, without establishing a connection between the sender and the receiver.

Transferring Data over a Network Using UDP

Use the User Datagram Protocol (UDP) to transfer data to a single client, known as 
 *unicast* communication, or between a number of processes or processors that have opted into a group or receivers, known as 
 *multicast* communication, without establishing a connection between the sender and the receiver.

To transmit data using UDP, you must develop the code to send or receive data on both the system you want to send data to and the system you want to receive data from.

Note

#### What to Use

- UDP Open or UDP Multicast Open
- UDP Read
- UDP Write
- UDP Close

#### What to Do

1. Create the following diagram in a VI targeted to the system that you want to receive data. 
 Customize the gray sections for your unique programming goals. 
 [IMAGE alt='1378' src='GUID-8FCB1D5A-5296-4662-B524-EB65B489C838-a5.png'] 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The UDP Open node opens a local UDP socket to send a datagram to a single receiver on the port or service name you specify. Make sure the port or service name you wire to UDP Open on the receiver matches the port or service name you write to from the sender.
 To send a single datagram to multiple receivers in parallel, known as multicast communication, use UDP Multicast Open instead of the standard UDP Open node, as shown in the following image.
 
[IMAGE alt='1378' src='GUID-A64DB17A-369A-49A9-BFFA-463680939E92-a5.png'] 

 UDP multicast communication lowers network traffic compared to unicast communication, which must iterate through the list of clients. To receive data sent by a multicast sender, the sender broadcasts a multicast IP address. All receivers must join a multicast group by specifying the same multicast IP address. Multicast addresses are in the 224.0.0.0 to 239.255.255.255 range.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 UDP Read nodes read from the socket. If the sender sends multiple datagrams to the receiver before the read operation occurs, UDP Read reads only the latest datagram.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 You can display the data you receive from the sender on the UI of the receiver or further process the data locally.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 After you close the UDP socket, you can no longer send or receive data on the specified port until you reopen the socket. Make sure you no longer want to send or receive data before you close the socket.
2. Create the following diagram in a VI targeted to the system that you want to send data. 
 Customize the gray sections for your unique programming goals. 
 [IMAGE alt='1378' src='GUID-13FA19AE-0E96-4A4D-8816-31A73886ECE5-a5.png'] 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 The UDP Open node opens a local UDP socket to send a datagram to a single receiver on the port or service name you specify.
 To send a single datagram to multiple receivers in parallel, known as multicast communication, use UDP Multicast Open instead of the standard UDP Open node.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 UDP Write nodes write to the specified receiver port and send data to the receiver. The address you specify must match the IP address of the receiver, and the port or service name you specify must match the port you specify on the receiver.
 To multicast data to multiple recipients, specify the same multicast IP address that the receivers read from, as shown in the following image.
 
[IMAGE alt='1378' src='GUID-9FFFF75A-0B33-45D7-BC38-55090BDA48D9-a5.png'] 

 Multicast addresses are in the 224.0.0.0 to 239.255.255.255 range.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 The maximum size limit for each datagram is 65,535 bytes. However, try to keep datagrams to a reasonable size, about 1,000 bytes or fewer, to minimize the chance that the protocol will need to split and reassemble the underlying data packet during transmission. When the data packet is greater than the Maximum Transmit Unit (MTU) of the network hardware being used, data fragmentation happens. For standard cabled Ethernet, which has an MTU of 1,500 bytes, about 1,000 bytes is a good rule of thumb to prevent any fragmentation from happening.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 After you close the UDP socket, you can no longer send or receive data on the specified port until you reopen the socket. Make sure you no longer want to send or receive data before you close the socket.

After you finish developing your sender and receiver applications, your sender and receiver applications communicate using UDP when you simultaneously run the applications.

#### Troubleshooting

- If a recipient consistently receives datagrams in the wrong order, consider sending shorter messages. The maximum size limit for each datagram is 65,535 bytes. However, try to keep datagrams to about 1,000 bytes or fewer to minimize the chance that the protocol will need to split and reassemble the underlying data packet during transmission.
- If you have trouble transferring data successfully, try the following troubleshooting strategies:
  - Verify that the port, service name, or address you specify for UDP Write on the sender matches the port or service name you specify for UDP Open or UDP Multicast Open on the receiver. Different IP addresses that refer to the same computer are not compatible. For example, if you open a UDP socket using the address 
 localhost and write to the numeric IP address of the local computer, such as 
 10.113.0.53 , the receiver does not receive data.
  - If you are broadcasting data, verify that the IP address you specify for UDP Write on the sender matches the IP address you specify for UDP Multicast Open on the receiver.
  - Verify that the recipient VI opens the UDP socket before the datagram arrives from the sender. If the datagram arrives before the recipient opens the appropriate UDP socket, the datagram is lost without any warning or notification.
  - Verify that the ports you have specified are valid, open ports. Valid UDP ports range from 0 to 65,535. To dynamically locate an open port, use port 0 and provide a service name for any UDP Open and UDP Write nodes, as illustrated by the images above. Because specifying port 0 causes the nodes to locate a random open port, use port 0 only if you intend to use service names.

#### Example

Search within the programming environment to access the following installed example:
 *Simple UDP*

Parent topic:

UDP Network Communication

<!--NI_TOPIC bundle=labview-nxg-data-communication path=udp-network-communication.html language=enus -->
## TOPIC 00017: UDP Network Communication

- bundle_id: `labview-nxg-data-communication`
- source_path: `udp-network-communication.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-data-communication/raw/resource/enus/udp-network-communication.html
- document_id: `labview-nxg-data-communication`
- page_type: `leaf`
- content_type: `concept`
- source_description: User Datagram Protocol (UDP) is a high-performance way to communicate short packets of data to one or more recipients. UDP transfers data faster, with higher throughput and lower latency, than TCP, because UDP does not require the overhead that TCP does. UDP does not guarantee successful and proper

UDP Network Communication

*User Datagram Protocol* (UDP) is a high-performance way to communicate short packets of data to one or more recipients.

Note

You use UDP to send datagrams between processes or processors without establishing a connection between the sender and the receiver. A 
 *datagram* is a basic data transfer packet that contains the data you want to transmit and a header that indicates the source and destination address.

Parent topic:

Communicating over a Network
