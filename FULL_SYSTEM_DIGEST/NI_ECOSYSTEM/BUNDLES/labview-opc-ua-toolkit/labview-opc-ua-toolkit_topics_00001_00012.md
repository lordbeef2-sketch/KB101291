# NI DOCUMENT BUNDLE: labview-opc-ua-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-opc-ua-toolkit start=1 end=12 -->
<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=connections-between-an-opc-ua-server-and-an-o.html language=enus -->
## TOPIC 00001: Connections between an OPC UA Server and an OPC UA Client

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `connections-between-an-opc-ua-server-and-an-o.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/connections-between-an-opc-ua-server-and-an-o.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW OPC UA Toolkit supports both non-secure connections and secure connections between an OPC UA server and an OPC UA client. In a non-secure connection, the OPC UA server and OPC UA client do not need to trust each other. When the OPC UA server supports a non-secure connection, the OPC UA c

### Connections between an OPC UA Server and an OPC UA Client

The LabVIEW OPC UA Toolkit supports both non-secure connections and secure connections between an OPC UA server and an OPC UA client.

In a non-secure connection, the OPC UA server and OPC UA client do not need to trust each other. When the OPC UA server supports a non-secure connection, the OPC UA client can connect to the OPC UA server without security.

In a secure connection, the OPC UA server and OPC UA client must trust each other to protect the
 data exchange between each other. To establish a secure connection between an OPC UA
 server and an OPC UA client, you must complete the following tasks:

- Ensure that the OPC UA server supports a secure connection.
- Ensure that the OPC UA server trusts the certificate file that the OPC UA client uses.
- Ensure that the OPC UA client uses the secure message modes and corresponding security policies supported by the OPC UA server. 
 A message mode specifies the encryption mode when the OPC UA server and OPC UA client send
 messages to each other. The OPC UA Toolkit supports the following message mode
 options:None
 Sign
 Sign and EncryptA security policy specifies how the OPC UA server and OPC UA client sign
 and encrypt messages. The OPC UA Toolkit supports the following security policy
 options:Basic256Sha256
 Aes128Sha256RsaOaep
 Aes256Sha256RsaPss
- Ensure that the OPC UA client trusts the certificate file that the OPC UA server uses.

Parent topic:

OPC UA Toolkit

Related concepts:

- Protecting OPC UA Data Items

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=creating-an-opc-ua-server-and-an-opc-ua-clien.html language=enus -->
## TOPIC 00002: Creating an OPC UA Server and an OPC UA Client

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `creating-an-opc-ua-server-and-an-opc-ua-clien.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/creating-an-opc-ua-server-and-an-opc-ua-clien.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tutorial introduces you to the basics of creating an OPC UA server and an OPC UA client by using the OPC UA VIs. This tutorial consists of the following parts:

### Creating an OPC UA Server and an OPC UA Client

This tutorial introduces you to the basics of creating an OPC UA server and an OPC UA client by using the OPC UA VIs. This tutorial consists of the following parts:

1. Part 1: Creating an OPC UA Server
2. Part 2: Using an OPC UA Server
3. Part 3: Establishing Connections between an OPC UA Server and an OPC UA Client
4. Part 4: Using an OPC UA Client

Parent topic:

OPC UA Toolkit

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=extended-support-changes.html language=enus -->
## TOPIC 00003: Updates and Changes for LabVIEW OPC UA Toolkit Extended Support Versions

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/extended-support-changes.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in LabVIEW OPC UA Toolkit versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-v

### Updates and Changes for LabVIEW OPC UA Toolkit Extended Support Versions

Browse updates and changes made in LabVIEW OPC UA Toolkit versions
 on extended support.

Note

Release Notes

#### LabVIEW OPC UA Toolkit 2022 Q4
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit
 2022 Q4.

##### LabVIEW Support

- Added support for LabVIEW 2022 Q4.

##### VI Support

- Added reentrant support for OPC UA VIs

#### LabVIEW OPC UA Toolkit 2021 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit
 2021.

##### LabVIEW Support

- Added support for LabVIEW 2021.

#### LabVIEW OPC UA Toolkit 2020 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit
 2020.

##### LabVIEW Support

- Added support for LabVIEW 2020 (32-bit and 64-bit).

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00004: LabVIEW OPC UA Toolkit New Features and Changes

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW OPC UA Toolkit. Discover what is new in the latest releases of LabVIEW OPC UA Toolkit.If you cannot find new features and changes for your version, it might not include user-facing updates. Howeve

### LabVIEW OPC UA Toolkit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW OPC UA Toolkit.

LabVIEW OPC UA Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW OPC UA Toolkit
 2026 Q2 Changes

LabVIEW OPC UA Toolkit 2026 Q2 includes updates for creating secure
 OPC UA servers using LabVIEW.

##### New
 Features

This version of the LabVIEW OPC UA Toolkit adds the
 following feature:

- Support for server-side username and password authentication for NI OPC.

#### LabVIEW OPC UA Toolkit
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit 2025 Q4.

##### New
 Features

This version of the LabVIEW OPC UA Toolkit provides
 support for the following features:

- Added support for the following security policies for OPC UA Client and OPC UA Server:
  - Basic256Sha256
  - Aes128Sha256RsaOaep
  - Aes256Sha256RsaPss
- Ended support for the following security policies:
  - Basic128Rsa15
  - Basic256

#### LabVIEW OPC UA Toolkit
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit 2025 Q3.

##### New Software
 Support

This version of the LabVIEW OPC UA Toolkit provides
 support for the following software applications:

- Added support for OpenSSL 3.0.13.
- Added support for OPC UA on Linux Real-Time (RT) with LabVIEW 2025.
- Extended OPC UA support to all runtime engines.
- Installed latest security updates.

#### LabVIEW OPC UA Toolkit 2025 Q2
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW OPC UA Toolkit
 2025 Q2.

##### LabVIEW Support

- Added support for LabVIEW 2025 Q2.

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=opc-ua-toolkit.html language=enus -->
## TOPIC 00005: OPC UA Toolkit

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `opc-ua-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/opc-ua-toolkit.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW OPC UA Toolkit includes VIs for exchanging data between OPC UA servers and clients. OPC Unified Architecture (UA) is an OPC Foundation specification for device connectivity. Unlike the classic OPC specification, which uses Microsoft DCOM/COM-based technology, OPC UA is platform-independe

### OPC UA Toolkit

The LabVIEW OPC UA Toolkit includes VIs for exchanging data between OPC UA servers and clients.

OPC Unified Architecture (UA) is an OPC Foundation specification for device connectivity. Unlike the classic OPC specification, which uses Microsoft DCOM/COM-based technology, OPC UA is platform-independent and able to connect servers and clients over various types of networks that have access to a common address space. OPC UA servers and clients use unique certificates to provide authentication and encryption capabilities to protect data when servers and clients communicate with each other.

Visit ni.com/info and enter the Info Code exxt3g to understand the importance of OPC UA and for a comparison between OPC UA and classic OPC. Refer to the OPC Foundation website at www.opcfoundation.org for more information about OPC UA specifications.

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=part-1-creating-an-opc-ua-server.html language=enus -->
## TOPIC 00006: Part 1: Creating an OPC UA Server

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `part-1-creating-an-opc-ua-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/part-1-creating-an-opc-ua-server.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the OPC UA Server VIs to create an OPC UA server application that communicates with any OPC UA client. In Part 1 of this tutorial, you complete the following tasks: Creating an OPC UA server that supports only non-secure connections Creating an OPC UA server that supports only secure con

### Part 1: Creating an OPC UA Server

You can use the OPC UA Server VIs to create an OPC UA server application that communicates with any OPC UA client. In Part 1 of this tutorial, you complete the following tasks:

- Creating an OPC UA server that supports only non-secure connections
- Creating an OPC UA server that supports only secure connections
- Creating an OPC UA server that supports both non-secure and secure connections

#### Creating an OPC UA Server That Supports Only Non-Secure Connections

#### What to Use

Use the following objects to create an OPC UA server that supports only non-secure connections:

| Create VI | Start VI | Stop VI | Close VI |
| --- | --- | --- | --- |
|  |  |  |  |

#### What to Do

Create the following block diagram to add an OPC UA server that supports only
 non-secure connections.

Figure 1.

[IMAGE alt='image' src='GUID-82A34D61-807C-48B0-ADEF-EA5902F7EE92-a5.gif']

The following list describes important details about the previous diagram:

1. The server endpoint URL output of the
 Create VI returns
 the unique identifier of the OPC UA server.
2. (Recommended) The While
 Loop enables the VI
 to run continuously. Because an OPC UA server does not have any background
 services, LabVIEW destroys the OPC UA server when the VI stops. Therefore, you
 can create a structure, such as a While Loop, Event
 structure,
 or Time Delay, to
 enable the example VI to run continuously and avoid destroying the OPC UA
 server.
3. Use the Stop VI to stop
 the OPC UA server before you use the
 Close VI to close and
 destroy the OPC UA server.

#### Creating an OPC UA Server That Supports Only Secure Connections

#### What to Use

Use the following objects to create an OPC UA server that supports only secure connections:

| Create VI | Clear All Trusted Clients VI | Add Trusted Clients VI | Start VI | Stop VI | Close VI |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

#### What to Do

Create the following block diagram to add an OPC UA server that supports only secure
 connections.

Figure 2.

[IMAGE alt='image' src='GUID-B62134DC-2A9A-4DF2-89A7-D1D6C45CD7EB-a5.gif']

The following list describes important details about the previous diagram:

1. The supported security policies constant of the Create VI
 specifies the message mode and security policies that the OPC UA
 server supports. To prevent the OPC UA client from establishing a non-secure
 connection to the OPC UA server, you must set None to
 FALSE. To establish secure connections between the OPC UA client and the OPC UA
 server, you must select one or multiple message modes and security
 policies.
2. The server certificate file control of the Create VI
 specifies the path or name of the public key. Note If the OPC UA server does
 not trust the certificate file that the OPC UA client uses, LabVIEW returns
 an error. Ensure that you add trusted OPC UA client certificates to an OPC
 UA server when you create an OPC UA server that supports only secure
 connections.
3. (Optional) The Clear All Trusted
 Clients
 VI clears the OPC UA client certificates that the OPC UA server trusts. After
 you start the OPC UA server, you cannot clear the trusted client certificates
 until the OPC UA server stops.
4. The Add Trusted
 Clients
 VI adds trusted OPC UA client certificates to the OPC UA server. After you start
 the OPC UA server, you cannot add trusted client certificates until the OPC UA
 server stops. The trusted client certificates control of
 the Add Trusted Clients VI specifies the file paths of the certificates that the
 OPC UA server trusts. You must manually copy the trusted client certificates
 from the OPC UA client machine to the OPC UA server machine, and then enter the
 path in trusted client certificates .

#### Creating an OPC UA Server That Supports Both Non-Secure and Secure Connections

#### What to Use

Use the following objects to create an OPC UA server that supports both non-secure and secure connections:

| Create VI | Clear All Trusted Clients VI | Add Trusted Clients VI | Start VI | Stop VI | Close VI |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

#### What to Do

Create the following block diagram to add an OPC UA server that supports both
 non-secure and secure connections.

Figure 3.

[IMAGE alt='image' src='GUID-6DFB595B-C016-4F34-B145-37332DC44D10-a5.gif']

The following list describes important details about the previous diagram:

1. The supported security policies constant of the Create VI
 specifies the message mode and security policies that the OPC UA server
 supports. To establish a non-secure connection between the OPC UA client and the
 OPC UA server, you must set None to TRUE. To establish
 secure connections between the OPC UA client and the OPC UA server, you must
 select one or multiple message modes and security policies.
2. The server certificate file control of the Create VI
 specifies the path or name of the public key. Note To establish a non-secure
 connection with a client, make sure that the domain names include the
 machine name of the server application.
3. (Optional) The Clear All Trusted
 Clients
 VI clears the OPC UA client certificates that the OPC UA server trusts. After
 you start the OPC UA server, you cannot clear the trusted client certificates
 until the OPC UA server stops.
4. The Add Trusted
 Clients
 VI adds trusted OPC UA client certificates to the OPC UA server. After you start
 the OPC UA server, you cannot add trusted client certificates until the OPC UA
 server stops. The trusted client certificates control of
 the Add Trusted Clients VI specifies the file paths of the certificates that the
 OPC UA server trusts. You must manually copy the trusted client certificates
 from the OPC UA client machine to the OPC UA server machine, and then enter the
 path in trusted client certificates .

Parent topic:

Creating an OPC UA Server and an OPC UA Client

Related concepts:

- Connections between an OPC UA Server and an OPC UA Client
- Creating an OPC UA Server and an OPC UA Client

Related information:

- OPC UA Toolkit API Reference

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=part-2-using-an-opc-ua-server.html language=enus -->
## TOPIC 00007: Part 2: Using an OPC UA Server

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `part-2-using-an-opc-ua-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/part-2-using-an-opc-ua-server.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In part 2 of this tutorial, you complete the following tasks: Constructing an address space Reading and writing the value of a node Registering and unregistering an OPC UA server with the UA Local Discovery Server (LDS) Reading, updating, and deleting the history data of a node Reading the history e

### Part 2: Using an OPC UA Server

In part 2 of this tutorial, you complete the following tasks:

- Constructing an address space
- Reading and writing the value of a node
- Registering and unregistering an OPC UA server with the UA Local Discovery Server (LDS)
- Reading, updating, and deleting the history data of a node
- Reading the history events of a condition
- Updating and deleting the history events of a condition

#### Constructing an Address Space

- Folders
- Items
- Properties
- Notifiers
- Conditions

Constructing an address space includes the following tasks:

- Creating a folder in an address space
- Adding a notifier as a child to the folder
- Adding a source node to a notifier
- Adding a condition node to the notifier
- Adding an item as a child to the folder
- Adding a property to an item

#### What to Use

To create a folder in an address space, use the following objects:

| Add Folder VI | Add Notifier VI | Add Item VI | Add Condition VI | Add Property VI |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

#### What to Do

To construct an address space for an OPC UA server, create the following block
 diagram:

[IMAGE alt='image' src='GUID-05E32D3E-7E2D-4ECF-804A-D0B2A42B0E47-a5.gif']

The following list describes important details about the previous diagram:

1. The Add
 Folder 
 VI creates a folder named Folder1 .
2. The Add
 Notifier 
 VI adds a notifier named Dialog Notifier . The Add
 Item 
 VI adds an item named Source Node to Dialog
 Notifier .
3. The Add
 Condition 
 VI adds a dialog condition node to the address space.
4. The Add Item VI creates an item named
 Item at the top level of the address space. The
 Add
 Property 
 VI adds a property named Property to
 Item .
5. (Optional) The Delete
 Node 
 VI deletes the following nodes: Before you delete the node, you can use the
 Stop 
 VI to stop the OPC UA server. After the OPC UA server stops, you can do the
 following actions: After you delete the node, you can use the
 Start 
 VI to restart the OPC UA server.
  - The Dialog Notifier node.
  - Source Node , which is the child source node of the
 Dialog Notifier node.
  - Dialog Condition , which is the child condition node of
 the Dialog Notifier node.
  - Add nodes to the UPC UA server
  - Change the locations of nodes

#### Reading and Writing the Value of a
 Node

- Read the value of a node.
- Write a value to a node.

#### What to Use

To read and to write the value of a node on an OPC UA server, use the following
 objects:

| Add Folder VI | Add Item VI | Add Property VI | Read VI | Write VI |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

#### What to Do

- Read the value of a node.
- Read the timestamp of a node.
- Read the status of a node.
- Write a value to the node.

[IMAGE alt='image' src='GUID-C043B86F-CF69-472C-AB96-A89B72F147C2-a5.gif']

The following list describes important details about the previous diagram:

1. The
 Read 
 VI reads the value, timestamp, and status of Item1 .
2. The
 Write 
 VI writes the 1234 value and the Good status
 to the item that the Add Item VI created.

#### Registering and Unregistering an OPC
 UA Server with the LDS

You can use the OPC UA server VIs to register an OPC UA server with the LDS. You can
 also unregister the OPC UA server with the LDS.

#### What to Use

To register or unregister an OPC UA server with the LDS, use the following
 objects:

| Register Server VI | Unregister Server VI |
| --- | --- |
|  |  |

#### What to Do

To register or unregister the OPC UA server with the LDS, create the following block
 diagram:

[IMAGE alt='image' src='GUID-2798DF7A-B569-4DE2-A896-088738AEF399-a5.gif']

The following list describes important details about the previous diagram:

1. The server only trusts a valid LDS certificate file. local discovery
 server certificate file specifies the file path of the
 certificate file that the LDS
 uses.
 You must ensure that the OPC UA server and LDS trust each other. Place the
 server certificate file in a folder that the LDS public key infrastructure
 trusts.
2. The Register
 Server 
 VI registers the OPC UA server with the LDS. You must use this VI before the
 server starts. This VI registers the server to LDS after the server starts.
3. The Unregister
 Server 
 VI unregisters the OPC UA server with the LDS. This VI sends the offline
 registration to the LDS after the server stops. To register the server with the
 LDS after the server starts again, you must use the Register
 Server VI.

#### Reading, Updating, and Deleting
 History Data

Historical
 Access

- Device data
- Calculated data
- Status information
- Dynamically changing system data
- Diagnostic data

#### What to Use

To read, update, and delete history data, use the following objects:

| Add Folder VI | Add Item VI | Write VI | History Data Read VI | History Data Update VI | History Data Delete VI |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

#### What to Do

To read, update, and delete history data, create the following block diagram:

[IMAGE alt='image' src='GUID-E7D15FA9-16D7-4369-8F29-498A45059D0F-a5.gif']

The following list describes important details about the previous diagram:

1. The History Data
 Read 
 VI reads the history data of Item1 within a time range.
2. The History Data
 Update 
 VI updates the history data of Item1 at a specific
 timestamp.
3. The History Data
 Delete 
 VI deletes the history data of Item1 .

#### Reading History Events

Historical
 Access

- Notifications
- System alarms
- Operator action events
- System triggers

#### What to Use

To read history events, use the following objects:

| Add Notifier VI | Add Item VI | Write VI | Add Condition VI | History Event Read VI |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

#### What to Do

To read history events, create the following block diagram:

[IMAGE alt='image' src='GUID-D3876F7B-8CAA-46AC-B0A5-DCB59178938E-a5.gif']

The following list describes important details about the previous diagram:

1. The Add
 Notifier 
 VI adds a notifier to the OPC UA server. To establish an event hierarchy, you
 can add a condition node and a source node as child nodes to a notifier.
2. The Write VI writes a FALSE value to the
 Source Node . This action triggers an off-normal alarm,
 because the updated value of the Source Node does not match the
 value of the Normal State Node .
3. The History Event
 Read 
 VI reads history events from the notifier.

#### Updating and Deleting History
 Events

Historical
 Access

- Notifications
- System alarms
- Operator action events
- System triggers

#### What to Use

To update and to delete history events, use the following objects:

| Add Notifier VI | Add Item VI | Write VI | Add Condition VI | History Event Update VI | History Event Delete VI |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

#### What to Do

To update and to delete history events, create the following block diagram:

[IMAGE alt='image' src='GUID-8ECD9814-4A63-42F3-ADCC-71FA6E503E07-a5.gif']

The following list describes important details about the previous diagram:

1. The History Event
 Update 
 VI updates history events from the notifier.
2. The History Event
 Delete 
 VI deletes history events from the notifier.

Parent topic:

Creating an OPC UA Server and an OPC UA Client

Related information:

- OPC UA Toolkit API Reference

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=part-3-establishing-connections-between-an-op.html language=enus -->
## TOPIC 00008: Part 3: Establishing Connections between an OPC UA Server and an OPC UA Client

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `part-3-establishing-connections-between-an-op.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/part-3-establishing-connections-between-an-op.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the OPC UA Client VIs to create an OPC UA client application that communicates with any OPC UA server. In Part 3 of this tutorial, you establish a non-secure connection and secure connection between an OPC UA server and an OPC UA client. Establishing a Non-Secure Connection between an OP

### Part 3: Establishing Connections between an OPC UA Server and an OPC UA Client

You can use the OPC UA Client VIs to create an OPC UA client application that communicates with any OPC UA server. In Part 3 of this tutorial, you establish a *non-secure connection* and *secure connection* between an OPC UA server and an OPC UA client.

#### Establishing a Non-Secure Connection between an OPC UA Server and an OPC UA Client

#### What to Use

Use the following objects to establish a non-secure connection between an OPC UA server and an OPC UA client.

| Connect VI | Disconnect VI |
| --- | --- |
|  |  |

#### What to Do

Create the following block diagram to establish a non-secure connection between an
 OPC UA server and an OPC UA client.

Figure 4.

[IMAGE alt='image' src='GUID-448E881E-1E6F-49D9-8C1A-9B621661FA12-a5.gif']

The following list describes important details about the previous diagram:

1. The server endpoint URL control of the
 Connect VI
 specifies the endpoint URL to which the OPC UA client connects.
2. The security policy constant of the Connect VI specifies
 the message mode and security policy to use. To connect an OPC UA
 client to an OPC UA server in non-security mode, you must set message
 mode to None . An OPC UA client has to
 trust the OPC UA server certificate even for an insecure connection.
3. The
 Disconnect
 VI disconnects the OPC UA client from the OPC UA server.

#### Establishing a Secure Connection between an OPC UA Server and an OPC UA Client

#### What to Use

Use the following objects to establish a secure connection between an OPC UA server and an OPC UA client.

| Connect VI | Disconnect VI |
| --- | --- |
|  |  |

#### What to Do

Create the following block diagram to establish a secure connection between an OPC UA
 server and an OPC UA client.

Figure 5.

[IMAGE alt='image' src='GUID-FAEBC4C0-68F4-4C37-9332-7433FBAD50FC-a5.gif']

The following list describes important details about the previous diagram:

1. The security policy constant of the Connect VI specifies
 the message mode and security policy to use. To establish secure connections
 between an OPC UA server and an OPC UA client, you must set message
 mode to either Sign or Sign
 and Encrypt depending on the message mode that the OPC UA server
 supports. You must also specify a security policy that the OPC UA server
 supports.
2. The client certificate file control of the Connect VI
 specifies the path or name of the public key. If you do not specify the
 client certificate file , the Connect VI generates and
 uses the default certificate file .
3. The trusted server certificates control of the Connect VI
 specifies the file paths of the certificates that the OPC UA client trusts. You
 must manually copy the trusted server certificates from the OPC UA server
 machine to the OPC UA client machine, and then enter the path in
 trusted server certificates .

Note

Parent topic:

Creating an OPC UA Server and an OPC UA Client

Related concepts:

- Connections between an OPC UA Server and an OPC UA Client
- Protecting OPC UA Data Items

Related information:

- OPC UA Toolkit API Reference

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=part-4-using-an-opc-ua-client.html language=enus -->
## TOPIC 00009: Part 4: Using an OPC UA Client

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `part-4-using-an-opc-ua-client.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/part-4-using-an-opc-ua-client.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In part 4 of this tutorial, you learn to use an OPC UA client to complete the following tasks: Browsing a node Getting the attributes of a node Reading and writing the value of a node Reading history data and events Creating a data subscription Creating an event subscription Responding to an acknowl

### Part 4: Using an OPC UA Client

In part 4 of this tutorial, you learn to use an OPC UA client to complete the following
 tasks:

- Browsing a node
- Getting the attributes of a node
- Reading and writing the value of a node
- Reading history data and events
- Creating a data subscription
- Creating an event subscription
- Responding to an acknowledgeable condition
- Shelving and unshelving an alarm

#### Browsing a Node

- Folders
- Items
- Properties
- Notifiers
- Conditions

A node ID describes the ID of a node in the address space of the OPC UA
 server. You can use the OPC UA
 client VIs to
 browse a node. Browsing a node allows you to get the ID, name, and type of all the
 child nodes of this node.

#### What to Use

To browse a node, use the following object:

| Forward Browse VI |
| --- |
|  |

#### What to Do

- Reference type
- ID
- Name
- Class
- Type of all its child nodes

To browse a node of an address space, create the following block
 diagram:

[IMAGE alt='image' src='GUID-6C48A8EC-A815-4DE4-807A-B773C5D8C3A4-a5.gif']

The following list describes important details about the previous diagram:

1. The Forward
 Browse 
 VI browses a node with the ns=2;s=Folder1 ID.
2. The browse result output of the Forward Browse
 VI returns the following information:
  - Reference type
  - ID
  - Name
  - Class
  - Type of all its child nodes

#### Getting the Attributes of a
 Node

- Name
- Type
- Data type
- Access level
- Description

#### What to Use

To get the attributes of a node, use the following object:

| Get Node Attribute VI |
| --- |
|  |

#### What to Do

To get the attributes of a node, create the following block diagram:

[IMAGE alt='image' src='GUID-951DA373-178F-422C-951A-84F889B3E020-a5.gif']

The following list describes important details about the previous diagram:

1. The Get Node
 Attribute 
 VI gets the attributes of a node with the ns=2;s=Folder1 
 ID.
2. The node attribute output of the Get Node
 Attribute VI returns the attributes of the node with the
 ns=2;s=Folder1 ID. The attributes contain the following
 information on the node:
  - Name
  - Type
  - Data type
  - Access level
  - Description

#### Reading and Writing the Value of a
 Node

- Read the value of a node.
- Write a value to a node.

#### What to Use

To read and to write the value of a node, use the following objects:

| Multiple Read VI | Multiple Write VI |
| --- | --- |
|  |  |

#### What to Do

- Read the value of a node.
- Read the timestamp of a node.
- Read the status of a node.
- Write a value to the node.

To read and to write the value of a node, create the following block
 diagram:

[IMAGE alt='image' src='GUID-D3E35906-89E0-4B87-B012-4CA7F88E850B-a5.gif']

The following list describes important details about the previous diagram:

1. The Multiple
 Read 
 VI reads the value, timestamp, and status of the node with the
 ns=2;s=Folder1.Item1.Property ID.
2. The Multiple
 Write 
 VI writes the 1234 value and the Good status
 to the node with the ns=2;s=Folder1.Item1.Property ID.

#### Reading History Data and History
 Events

Historical
 Access

- Device data
- Calculated data
- Status information
- Dynamically changing system data
- Diagnostic data

- Notifications
- System alarms
- Operator action events
- System triggers

#### What to Use

To read history data and history events, use the following objects:

| History Data Multiple Read VI | History Event Multiple Read VI |
| --- | --- |
|  |  |

#### What to Do

To read history data and history events, create the following block diagram:

[IMAGE alt='image' src='GUID-9E29FDD1-0D7C-4A82-B706-38F19039E67A-a5.gif']

The following list describes important details about the previous diagram:

1. The History Data Multiple
 Read 
 VI reads the history data. num values per nodes specifies
 the maximum number of values to return over the time range.
2. The History Event Multiple
 Read 
 VI reads the history events.

#### Creating a Data Subscription

You can use the OPC UA client VIs to create a data subscription to the nodes of an
 OPC UA server. The OPC UA server collects data changes that happen on a node that
 the OPC UA client subscribes to. The OPC UA server also sends a notification message
 about the changes to the OPC UA client.

#### What to Use

To create a data subscription, use the following objects:

| Create Subscription VI | Add Monitored Data Nodes VI | Delete Monitored Nodes VI | Delete Subscriptions VI |
| --- | --- | --- | --- |
|  |  |  |  |

#### What to Do

To create a data subscription to the nodes of an OPC UA server, create the following
 block diagram:

[IMAGE alt='image' src='GUID-787A84BA-B0F5-4F67-9D00-12F3D4164EE2-a5.gif']

The following list describes important details about the previous diagram:

1. To create a data subscription to the nodes of the OPC UA server and add nodes to
 the subscription, do the following:
  - Wire the subscription ID out output of the
 Create
 Subscription 
 VI to the subscription ID in input of the
 Add Monitored Data
 Nodes 
 VI.
2. The node IDs control of the Add Monitored Data
 Nodes VI specifies an array of node IDs that this VI adds to a
 subscription.
3. The Event
 Structure 
 handles the data change event. You can wire the OPC UA data change
 event output of the Create
 Subscription 
 VI to the event source input of the Register
 For Events function. You can also wire the event
 registration refnum output of the Register For
 Events function to the Event Dynamic
 Registration terminal of the Event
 Structure to handle the data change event. Within the
 While Loop , the Event
 Structure continuously gets the data change event.
4. The Data Change output returns updates of the data on the
 OPC UA server.
5. (Optional) The Delete Monitored
 Nodes 
 VI deletes monitored nodes from a subscription. To delete monitored nodes, wire
 the subscription ID out output of the Create
 Subscription VI to the subscription ID in 
 input of the Delete Monitored Nodes VI. The
 node IDs control of the Delete Monitored
 Nodes VI specifies an array of node IDs that this VI deletes
 from a subscription.
6. (Optional) The Delete
 Subscriptions 
 VI deletes one or more subscriptions. By deleting a subscription, you delete all
 the monitored nodes from the subscription.

#### Creating an Event
 Subscription

You can use the OPC UA client VIs to create an event subscription to the notifier of
 an OPC UA server. When the notifier that an OPC UA client subscribes to receives
 event notifications, the OPC UA server collects these events. The the OPC UA server
 sends a notification message to the OPC UA client.

#### What to Use

To create an event subscription, use the following objects:

| Create Event Subscription VI | Add Monitored Event Nodes VI | Delete Monitored Nodes VI | Delete Subscriptions VI |
| --- | --- | --- | --- |
|  |  |  |  |

#### What to Do

To create an event subscription to the notifier of an OPC UA server, create the
 following block diagram:

[IMAGE alt='image' src='GUID-C5127DE3-6DD2-4CD2-B77E-31FF689CCBA8-a5.gif']

The following list describes important details about the previous diagram:

1. To create an event subscription to monitor the notifier of the OPC UA server, do
 the following:
  - Wire the subscription ID out output of the
 Create Event
 Subscription 
 VI to the subscription ID in input of the
 Add Monitored Event
 Nodes 
 VI.
2. The node IDs control of the Add Monitored
 Events Nodes VI specifies an array of node IDs. This array of
 node IDs corresponds to the notifiers that this VI adds to an event
 subscription.
3. The Event
 Structure 
 handles the data change event. You can wire the OPC UA condition
 event output of the Create Event
 Subscription 
 VI to the event source input of the Register
 For Events function. You can also wire the event
 registration refnum output of the Register For
 Events function to the Event Dynamic
 Registration terminal of the Event
 Structure to handle the data change event. Within the
 While Loop , the Event
 Structure continuously gets the condition event.
4. The condition events output returns event notifications
 from the OPC UA server.
5. (Optional) The Delete Monitored
 Nodes
 VI deletes monitored nodes from a subscription. To delete monitored nodes, wire
 the subscription ID out output of the Create
 Subscription VI to the subscription ID in 
 input of the Delete Monitored Nodes VI. The
 node IDs control of the Delete Monitored
 Nodes VI specifies an array of node IDs that this VI deletes
 from a subscription.
6. (Optional) The Delete
 Subscriptions 
 VI deletes one or more subscriptions. By deleting a subscription, you delete all
 the monitored notifiers from the event subscription.

#### Responding to an Acknowledgeable
 Condition

You can use the Alarms and
 Conditions
 VIs of the OPC UA client VIs to respond to an acknowledgeable condition.

#### What to Use

To respond to an acknowledgeable condition, use the following objects:

| Create Event Subscription VI | Add Monitored Event Nodes VI | Respond Acknowledgeable Condition VI |
| --- | --- | --- |
|  |  |  |

#### What to Do

To change the states of conditions and alarms, create the following block
 diagram:

[IMAGE alt='image' src='GUID-745C8E48-FB19-4F33-BBA9-287165D2E7E1-a5.gif']

The following list describes important details about the previous diagram:

1. The Respond Acknowledgeable
 Condition 
 VI acknowledges an acknowledgeable condition.
2. The Respond Acknowledgeable
 Condition 
 VI confirms an acknowledgeable condition. A condition must be acknowledged
 before it is confirmed.

#### Shelving and Unshelving an
 Alarm

You can use the Alarms and
 Conditions
 VIs of the OPC UA client VIs to shelve and unshelve an alarm.

#### What to Use

To shelve and unshelve an alarm, use the following objects:

| Create Event Subscription VI | Add Monitored Event Nodes VI | Shelve Alarm Condition VI |
| --- | --- | --- |
|  |  |  |

#### What to Do

To shelve and unshelve an alarm, create the following block diagram:

[IMAGE alt='image' src='GUID-AAE27C47-5925-4485-A884-CB7BF300D602-a5.gif']

The following list describes important details about the previous diagram:

1. The Timed Shelve instance of the Shelve Alarm
 Condition 
 VI shelves an alarm for a definite time period. When the shelving
 time value is set to 0 , the Shelve
 Alarm Condition VI shelves an alarm for the maximum amount of
 time. The OPC UA client cannot receive events when the alarm is in shelved
 state, unless the alarm is changed to unshelved or inactive state.
2. The unshelve instance of Shelve Alarm Condition VI
 unshelves an alarm.

Parent topic:

Creating an OPC UA Server and an OPC UA Client

Related concepts:

- Creating an OPC UA Server and an OPC UA Client

Related information:

- OPC UA Toolkit API Reference

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=protecting-opc-ua-data-items.html language=enus -->
## TOPIC 00010: Protecting OPC UA Data Items

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `protecting-opc-ua-data-items.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/protecting-opc-ua-data-items.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Compared with classic OPC, OPC Unified Architecture (UA) offers expanded security across servers and clients by utilizing private keys and public keys. A certificate file contains a pair of keys: a public key and a private key. You can use the Add Trusted Clients VI to add a public key that an OPC U

### Protecting OPC UA Data Items

Compared with classic OPC, OPC Unified Architecture (UA) offers expanded security across servers and clients by utilizing private keys and public keys. A certificate file contains a pair of keys: a public key and a private key.

You can use the Add Trusted Clients VI to add a public key that an OPC UA client uses to an OPC UA server. You can use the Connect VI to specify the public key that an OPC UA server uses.

By default, the OPC UA server or client trusts the certificate file it uses. Ensure that the public key and private key have the same name and reside in the same folder. You can use an existing certificate file. If you do not specify a certificate file for the OPC UA server or client to use, LabVIEW creates a certificate file, Default OPC UA, to use when you create an OPC UA server or client at run time. You also can use the Create Certificate VI to create a certificate file.

The following table shows the location of the certificate file that LabVIEW creates at run time or when you use the Create Certificate VI.

| Operating System | File Path to the Certificate File | Note |
| --- | --- | --- |
| Windows | C:\\ProgramData\\National Instruments\\certstore\\opcua\\ | You can find public keys and private keys in the file path to the certificate file. |
| NI Linux Real-Time | /var/local/natinst/certstore/opcua/ | You can find public keys and private keys in the file path to the certificate file. |

Note

.der

.pem

Parent topic:

OPC UA Toolkit

Related information:

- OPC UA Toolkit API Reference

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=related-documentation.html language=enus -->
## TOPIC 00011: Related Documentation

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `related-documentation.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/related-documentation.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following documents contain information that might be helpful as you use the LabVIEW OPC UA Toolkit. LabVIEW OPC UA Release Notes—Use this page to view release notes, known issues, bug fixes, and behavior changes. LabVIEW OPC UA Toolkit Example VIs—Refer to the labview\examples\Data Communicatio

### Related Documentation

The following documents contain information that might be helpful as you use the LabVIEW OPC UA Toolkit.

- LabVIEW OPC UA Release Notes —Use this page to view release notes, known
 issues, bug fixes, and behavior changes.
- LabVIEW OPC UA Toolkit Example VIs—Refer to the labview\examples\Data Communication\OPCUA directory for example VIs that demonstrate common tasks using the OPC UA Toolkit. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and selecting Toolkits and Modules»OPC UA in the NI Example Finder window.
- Additional LabVIEW documentation.

The following resources were used as references to produce the OPC UA Toolkit and they offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by NI. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the OPC UA Toolkit or any other NI product.

- OPC Unified Architecture Specification
- List of Trade Facilitation Recommendations N° 20

Parent topic:

OPC UA Toolkit

Related information:

- OPC Unified Architecture Specification
- List of Trade Facilitation Recommendations N° 20
- Release Notes
- LabVIEW User Manual

<!--NI_TOPIC bundle=labview-opc-ua-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00012: LabVIEW OPC UA Toolkit User Manual

- bundle_id: `labview-opc-ua-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-opc-ua-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW OPC UA Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### LabVIEW OPC UA Toolkit
 User Manual

The LabVIEW OPC UA Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download LabVIEW OPC UA Toolkit
- LabVIEW OPC UA Toolkit Programming Reference Manual
- Download LabVIEW OPC UA Toolkit Release Notes
- Interactive Activation Guide
- NI Learning Center
