# NI DOCUMENT BUNDLE: xnet-db-editor

<!--NI_BUNDLE_CHUNK bundle=xnet-db-editor start=1 end=45 -->
<!--NI_TOPIC bundle=xnet-db-editor path=alias.html language=enus -->
## TOPIC 00001: Alias Names

- bundle_id: `xnet-db-editor`
- source_path: `alias.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/alias.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-XNET uses an alias name to identify a database file. The alias provides a shorter, easier-to-read name for use within your application. An alias isolates your application from changes to the specific file path. For example, if your application uses the alias MyDatabase and you change its file pat

Alias Names

NI-XNET uses an alias name to identify a database file. The alias provides a shorter,
 easier-to-read name for use within your application. An alias isolates your application
 from changes to the specific file path. For example, if your application uses the alias
 MyDatabase and you change its file path to
 x:\Embedded\Vehicle5\MyDatabase.dbc,
 your application continues to run without change.

Database aliases are required for FlexRay and LIN measurements, but are optional for CAN
 measurements.

After you create an alias, it exists until you explicitly delete it. If you uninstall
 NI-XNET, the aliases are deleted; however, if you reinstall or upgrade NI-XNET, the
 aliases from the previous installation remain. Deleting an alias does not delete the
 database file itself, only the association within NI-XNET.

A *local alias* defines a shortcut to a database file stored on your local
 host.

An *RT target alias* defines an alias for a database file stored on a remote
 system (i.e., LabVIEW Real-Time (RT) target).

Refer to *Managing Aliases* to learn how to use local aliases and add an alias for
 an RT target.

Parent topic:

NI-XNET Database Editor

Related reference:

- Managing Aliases

<!--NI_TOPIC bundle=xnet-db-editor path=bit-layout.html language=enus -->
## TOPIC 00002: Viewing Bit Layouts

- bundle_id: `xnet-db-editor`
- source_path: `bit-layout.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/bit-layout.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: A bit layout indicates the byte order of signals. The NI-XNET Database Editor displays bit layouts for relevant signals on the Signal, Frame, and PDU Properties pages. The Byte Order property defines how signal bytes are ordered in the frame payload when the frame is loaded in memory. The NI-XNET Da

Viewing Bit Layouts

A bit layout indicates the byte order of signals. The NI-XNET Database Editor displays bit layouts for relevant signals on the Signal, Frame, and PDU
 Properties pages.

The Byte Order property defines how signal bytes
 are ordered in the frame payload when the frame is loaded in memory.
 The NI-XNET Database Editor shows bit-level layouts of signals within a container so that you
 can determine more easily how signals are organized in their
 container and how they are multiplexed.

In the bit layout, individual signals are depicted as groups of one or
 more contiguous, like-colored boxes. The bit layout makes use of
 five colors to differentiate signals within the same container. Each
 colored box represents a bit, and each row in the bit layout is a
 byte of data.

Within a signal, numbered boxes indicate the order of bits. When you
 select a bit (one of the numbered boxes), all the bits in the group
 change to green, indicating the active signal.

1. In the left pane, select the appropriate PDU, frame, or signal
 name. 
 The editor displays the properties page in the content
 pane at the right. The Bit Layout
 panel is at the bottom of the page.
2. In the bit layout, click a numbered box in a group of one or
 more bits, indicated by color, to select a particular
 signal. 
 The following signal properties are displayed in the area at the right of the
 bit layout.Name—Signal name. Click the signal name to load Signal
 Properties in the content pane.
 Item Type—Signal, or type of item represented in the bit
 layout.
 Multiplexor Type—Type property: Static, Multiplexer, or
 Multiplexed.
 Byte Order—Order of bytes in the frame payload: Little Endian
 or Big Endian.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=can-ecu-properties.html language=enus -->
## TOPIC 00003: CAN ECU Properties

- bundle_id: `xnet-db-editor`
- source_path: `can-ecu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/can-ecu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the ECU Properties page if the database cluster is configured to use CAN protocol. Name ECU name. This must be unique within the cluster. TX Frames List of transmitted frames. RX Frames List of frames received. Comment Note or descriptive text related to thi

CAN ECU Properties

The following properties are available on the ECU Properties page if the database cluster
 is configured to use CAN protocol.

Name

TX Frames

RX Frames

Comment

Figure 1.

[IMAGE alt='1378' src='GUID-2FE91844-D9E5-431A-8DF5-8E56C96FC0AD-a5.png']

Parent topic:

ECU Properties

<!--NI_TOPIC bundle=xnet-db-editor path=cluster-properties-can.html language=enus -->
## TOPIC 00004: CAN Cluster Properties

- bundle_id: `xnet-db-editor`
- source_path: `cluster-properties-can.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/cluster-properties-can.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Cluster Properties page for CAN protocol. Name Cluster name. This must be unique within the database. Protocol Communication protocol of the cluster (CAN, FlexRay, or LIN). Application Protocol Higher level protocol run on the cluster. Choices are None o

CAN Cluster Properties

The following properties are available on the Cluster Properties page for CAN
 protocol.

Name

Protocol

Application Protocol

None

J1939

I/O Mode

CAN

0–8 bytes

CAN FD

64
 bytes

CAN FD + BRS

Preset Baud Rate

Unset

Custom

Baud Rate

Custom Baud Rate

Sample Point

Lock BRP

BRP

SJW

TSEG1

TSEG2

Comment

Parent topic:

Cluster Properties

<!--NI_TOPIC bundle=xnet-db-editor path=cluster-properties-flexray.html language=enus -->
## TOPIC 00005: FlexRay Cluster Properties

- bundle_id: `xnet-db-editor`
- source_path: `cluster-properties-flexray.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/cluster-properties-flexray.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Cluster Properties page for FlexRay protocol. Name Cluster name. This must be unique within the database. Protocol Communication protocol of the cluster (CAN, FlexRay, or LIN). Channels FlexRay channels on which frames must be transmitted: A, B, A+B, or

FlexRay Cluster Properties

The following properties are available on the Cluster Properties page for FlexRay
 protocol.

Name

Protocol

Channels

Baud Rate

Bit Time

Baud Rate

Sample Clock Period

Baud Rate

0.0125 µs

0.025 µs

0.05 µs

TSS Transmitter

3–15 bits

CAS RX Low Max

67–99 gdBit

Cluster Drift Damping

0–5 MT

Cold Start Attempts

Max Sync Nodes

Cycle Time

Macrotick

1–6 µs

Macroticks Per Cycle

10–16000 MT.

Network Idle Time

2–805 MT.

Number of Static Slots

Static Slot

4–661 MT

Number of Minislots

Minislot

2–63
 MT.

Offset Correction Start

9–15999 MT

Symbol Window

0–142 MT

Max Payload Length

0–254 bytes

Minislot Action Point Offset

1–31 MT

Dynamic Slot Idle Phase

0–2 minislots

Wakeup Enabled

Wakeup Symbol RX Idle

14–59 gdBit

Wakeup Symbol RX Low

10–55 gdBit

Wakeup Symbol RX Window

76–301 gdBit

Wakeup Symbol TX Idle

45–180 gdBit

Wakeup Symbol TX Low

15–60 gdBit

Payload Length

0–254
 bytes

Action Point Offset

Max Without Clock Correction Passive

1–15 even/odd cycle
 pairs

Max Without Clock Correction Fatal

1–15 even/odd cycle pairs

Listen Noise

2–16

Network Management Vector Length

0–12 bytes

Comment

Parent topic:

Cluster Properties

<!--NI_TOPIC bundle=xnet-db-editor path=cluster-properties-lin.html language=enus -->
## TOPIC 00006: LIN Cluster Properties

- bundle_id: `xnet-db-editor`
- source_path: `cluster-properties-lin.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/cluster-properties-lin.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Cluster Properties page for LIN protocol. Name Cluster name. This must be unique within the database. Protocol Communication protocol of the cluster (CAN, FlexRay, or LIN). Timebase Tick Basic time unit of the LIN cluster (ms). Preset Baud Rate List of s

LIN Cluster Properties

The following properties are available on the Cluster Properties page for LIN
 protocol.

Name

Protocol

Timebase Tick

Preset Baud Rate

Custom

Baud Rate

Custom Baud Rate

Baud Rate

Preset Baud Rate

Custom

Custom Baud Rate

Preset Baud Rate

Custom

Comment

Parent topic:

Cluster Properties

<!--NI_TOPIC bundle=xnet-db-editor path=cluster-properties.html language=enus -->
## TOPIC 00007: Cluster Properties

- bundle_id: `xnet-db-editor`
- source_path: `cluster-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/cluster-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-XNET Database Editor enables you to configure a cluster by editing cluster properties. The specific properties available for a cluster vary by communication protocol (CAN, LIN, or FlexRay).

Cluster Properties

The NI-XNET Database Editor enables you to configure a cluster by editing
 cluster properties. The specific properties available for a cluster vary by communication
 protocol ([CAN](cluster-properties-can.html), [LIN](cluster-properties-lin.html), or [FlexRay](cluster-properties-flexray.html)).

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=cluster.html language=enus -->
## TOPIC 00008: Clusters

- bundle_id: `xnet-db-editor`
- source_path: `cluster.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/cluster.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: The basic entity of an automotive network database is a cluster. A cluster describes a single network (for example, a collection of nodes on a CAN or FlexRay bus). Each cluster has certain properties that must be configured; these properties vary by protocol (CAN, FlexRay, LIN). For a CAN cluster, t

Clusters

The basic entity of an automotive network database is a cluster. A cluster describes a single
 network (for example, a collection of nodes on a CAN or FlexRay bus). Each cluster has
 certain properties that must be configured; these properties vary by protocol (CAN,
 FlexRay, LIN).

For a CAN cluster, the only required property is baud rate. For FlexRay, you must
 configure approximately 30 global network parameters for a cluster. For FlexRay
 clusters, the NI-XNET Database Editor provides an easy edit mode that enables you to configure the most important
 properties, which the editor then uses to calculate the remaining parameters. The easy
 edit mode is usually the preferred choice. However, if you have an existing database,
 you can use the expert mode to configure the full set of parameters.

A typical database contains a single cluster. CANdb, NI-CAN, and LIN protocols support
 only one cluster (unnamed) per database.

FIBEX supports any number of clusters in a database; each cluster has a unique name. You
 could, for example, describe all the networks of a vehicle in a single database.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=configure-signal.html language=enus -->
## TOPIC 00009: Configuring Signals

- bundle_id: `xnet-db-editor`
- source_path: `configure-signal.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/configure-signal.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure a signal by specifying its signal type, data type, and byte order, and by modifying configuration parameters in Signal Properties. Complete the following steps to edit a signal in an open database. In the database tree, find and select the signal you want to configure. The content pane dis

Configuring Signals

Configure a signal by specifying its signal type, data type, and byte order, and by
 modifying configuration parameters in Signal
 Properties.

Complete the following steps to edit a
 signal in an open database.

1. In the database tree, find and select the signal you want to configure. 
 The content pane displays Signal Properties for the selected
 signal.
2. On the Signal Properties page, use the configuration controls to change property values
 as needed. 
 Refer to [Signal Properties](signal-properties.html) for details about particular signal properties.
3. Select File»Save As. 
 The Save Database As explorer window opens.
4. Select the database file or provide a file name, and click Save
 to save your changes to the database file.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=databases.html language=enus -->
## TOPIC 00010: Automotive Databases

- bundle_id: `xnet-db-editor`
- source_path: `databases.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/databases.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: An automotive database is typically a large file that contains descriptive information about a vehicle, parts of a vehicle, multiple vehicles, or software that runs parts of a vehicle. The database may contain information about networks, signals, streams, frames, protocol data units (PDUs), vehicle

Automotive Databases

An automotive database is typically a large file that contains descriptive information
 about a vehicle, parts of a vehicle, multiple vehicles, or software that runs parts of a
 vehicle. The database may contain information about networks, signals, streams, frames,
 protocol data units (PDUs), vehicle variants, and much more.

A database allows software programs and engineers to work efficiently with its content to
 design and build system models, run simulations, test components (such as ECUs), and so on.
 Users might use a database to view or edit details, communicate with a device under test
 (DUT), emulate part of a vehicle, or configure one or more objects in the database to match a
 test setup.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=ecu-properties.html language=enus -->
## TOPIC 00011: ECU Properties

- bundle_id: `xnet-db-editor`
- source_path: `ecu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/ecu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: All ECUs in a cluster are grouped under the ECU parent node. Properties available on the ECU Properties page vary depending on the communication protocol of the cluster.

ECU Properties

All ECUs in a cluster are grouped under the ECU parent node. Properties available on
 the ECU Properties page vary depending on the communication protocol of the
 cluster.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=ecu.html language=enus -->
## TOPIC 00012: ECUs

- bundle_id: `xnet-db-editor`
- source_path: `ecu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/ecu.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: An electronic control unit (ECU) controls one or more electrical systems or subsystems in a vehicle. A modern motor vehicle might contain 150 or more ECUs. An ECU transmits and receives frames (also called messages) on a closed Controller Area Network (CAN) bus. The NI-XNET Database Editor displays

ECUs

An electronic control unit (ECU) controls one or more electrical systems or subsystems in a
 vehicle. A modern motor vehicle might contain 150 or more ECUs. An ECU transmits and receives
 frames (also called messages) on a closed Controller Area Network (CAN) bus.

The NI-XNET Database Editor displays ECUs only as transmitters and receivers of frames within clusters. The same ECU
 might appear as part of different clusters in the database; however, in an exported FIBEX
 file, the ECU appears as different entities.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=editing-clusters.html language=enus -->
## TOPIC 00013: Editing Clusters

- bundle_id: `xnet-db-editor`
- source_path: `editing-clusters.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-clusters.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or delete an existing cluster, or create a new database cluster. Editing a ClusterEdit an existing cluster by adding or deleting database objects, such as frames, PDUs, and signals, or by modifying cluster properties. Deleting a ClusterTo delete a cluster, select the cluster in the navigation t

Editing Clusters

Edit or delete an existing cluster, or create a new database cluster.

#### Editing a Cluster

Edit an existing
 [cluster](cluster.html) by
 adding or deleting database objects, such as frames, PDUs, and signals, or by modifying
 [cluster
 properties](cluster-properties.html).

#### Deleting a Cluster

To delete a cluster, select the cluster in the
 navigation tree, and then select Edit»Delete.

#### Creating
 a New Cluster

export clusters

1. Right-click the database in the navigation tree, select Create
 Cluster and a communication protocol: CAN,
 FlexRay, or LIN.
2. Provide a name for the cluster, and configure the available [cluster properties](cluster-properties.html), which vary
 by communication protocol.
3. Do one of the following:
  - For FIBEX XML database files, select File»Save to save your changes to the database.
  - For ARXML and NCD database files, select File»Save As , and save the modified database in FIBEX XML format.

Parent topic:

Editing a Database

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=editing-database.html language=enus -->
## TOPIC 00014: Editing a Database

- bundle_id: `xnet-db-editor`
- source_path: `editing-database.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-database.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create, edit, or delete database objects such as clusters, frames, PDUs, and signals.

Editing a Database

Create, edit, or delete database objects such as clusters, frames, PDUs, and
 signals.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=editing-frames.html language=enus -->
## TOPIC 00015: Editing Frames

- bundle_id: `xnet-db-editor`
- source_path: `editing-frames.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-frames.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or delete an existing frame, or create a new frame. Editing a FrameEdit an existing frame by adding or deleting signals, mapping a PDU to the frame, or by modifying frame properties. Deleting a FrameTo delete a frame, select the frame in the navigation tree, and then select Edit Delete . Creati

Editing Frames

Edit or delete an existing frame, or create a new frame.

#### Editing a Frame

Edit an existing [frame](frame.html) by
 adding or deleting signals, [mapping a PDU](mapping-pdus-to-frame.html) to the frame, or by modifying [frame
 properties](frame-properties.html).

#### Deleting a Frame

To delete a frame,
 select the frame in the navigation tree, and then select Edit»Delete.

#### Creating a Frame

New clusters can be created only in ARXML, NCD, and XML
 database files; you can export clusters from DBC and LDF database files.

1. Right-click the database cluster in the navigation tree, and select
 Create Frame.
2. Provide a name for the frame, and configure the available [frame
 properties](frame-properties.html), which vary by communication protocol.
3. Do one of the following:
  - For supported database files (i.e., DBC and XML), select File»Save to save your changes to the database.
  - For unsupported database file formats, select File»Save As , and save the modified database in FIBEX XML format.

Parent topic:

Editing a Database

<!--NI_TOPIC bundle=xnet-db-editor path=editing-lin-schedules.html language=enus -->
## TOPIC 00016: Editing LIN Schedules

- bundle_id: `xnet-db-editor`
- source_path: `editing-lin-schedules.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-lin-schedules.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or delete an existing schedule, or create a new LIN schedule. Editing a LIN ScheduleEdit an existing schedule by modifying available LIN schedule properties. Deleting a LIN ScheduleTo delete a LIN schedule, select the schedule in the navigation tree, and then select Edit Delete . Creating a LIN

Editing LIN Schedules

Edit or delete an existing schedule, or create a new LIN schedule.

#### Editing a LIN Schedule

Edit an existing
 [schedule](lin-schedules.html) by modifying available [LIN schedule
 properties](lin-schedule-properties.html).

#### Deleting a LIN Schedule

To delete a LIN schedule, select the schedule in the navigation tree, and then select Edit»Delete.

#### Creating a LIN Schedule

A schedule can be created only for LIN clusters. Required
 fields vary depending on the specified type of schedule entry.

1. Right-click a cluster in the navigation tree, and select Create LIN
 Schedule.
2. Provide a name for the schedule, and then click New
 Entry in the Configuration section and select the type of entry:
 Unconditional, Sporadic, or Event-triggered.
3. Configure the available [LIN schedule properties,](lin-schedule-properties.html) which vary by entry
 type.
4. Select File»Save to save your changes to the database.

Parent topic:

Editing a Database

<!--NI_TOPIC bundle=xnet-db-editor path=editing-LIN-schedules.html language=dede -->
## TOPIC 00017: Bearbeiten von LIN-Schedules

- bundle_id: `xnet-db-editor`
- source_path: `editing-LIN-schedules.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/dede/editing-LIN-schedules.html
- source_language: `dede`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Bearbeiten oder Löschen eines vorhandenen Zeitplans oder Erstellen eines neuen LIN-Schedules. Bearbeiten eines LIN-Schedules Das Bearbeiten eines vorhandenen Schedules erfolgt durch Ändern der verfügbaren LIN-Schedule-Eigenschaften. Löschen eines LIN-Schedules Um ein LIN-Schedule zu löschen, wählen

### Bearbeiten von LIN-Schedules

Bearbeiten oder Löschen eines vorhandenen Zeitplans oder Erstellen eines neuen LIN-Schedules.

#### Bearbeiten eines LIN-Schedules

Das Bearbeiten eines vorhandenen [Schedules](lin-schedules.html) erfolgt durch Ändern der verfügbaren [LIN-Schedule-Eigenschaften](lin-schedule-properties.html).

#### Löschen eines LIN-Schedules

Um ein LIN-Schedule zu löschen, wählen Sie das Schedule in der Baumstruktur aus und wählen Sie dann Bearbeiten»Löschen.

#### Erstellen eines LIN-Schedules

Ein Schedule kann nur für LIN-Cluster erstellt werden. Die erforderlichen Felder variieren je nach dem angegebenen Typ des Schedule-Eintrags.

1. Klicken Sie mit der rechten Maustaste auf einen Cluster in der Baumstruktur und wählen Sie LIN-Schedule erstellen.
2. Geben Sie einen Namen für den Schedule ein und klicken Sie dann auf Neuer Eintrag im Abschnitt "Konfiguration" und wählen Sie die Art des Eintrags: "Unconditional", "Sporadic" oder "Event-triggered".
3. Konfigurieren Sie die verfügbaren [LIN-Schedule-Eigenschaften,](lin-schedule-properties.html) die je nach Eintragsart variieren.
4. Zum Speichern der Änderungen an der Datenbank wählen Sie Datei»Speichern.

Übergeordnetes Thema:

Bearbeiten einer Datenbank

<!--NI_TOPIC bundle=xnet-db-editor path=editing-pdus.html language=enus -->
## TOPIC 00018: Editing PDUs

- bundle_id: `xnet-db-editor`
- source_path: `editing-pdus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-pdus.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or delete an existing PDU, or create a new PDU. Editing a PDUEdit an existing PDU by modifying its PDU properties. Deleting a PDUTo delete a PDU, select the PDU in the navigation tree, and then select Edit Delete . Creating a New PDU Right-click a cluster in the navigation tree, and select Crea

Editing PDUs

Edit or delete an existing PDU, or create a new PDU.

#### Editing a PDU

Edit an existing [PDU](pdu.html) by
 modifying its [PDU properties](pdu-properties.html).

#### Deleting a PDU

To delete a PDU, select
 the PDU in the navigation tree, and then select Edit»Delete.

#### Creating a New PDU

1. Right-click a cluster in the navigation tree, and select Create
 PDU.
2. Provide a name for the PDU, and specify Payload Length
 in the [PDU
 properties](pdu-properties.html). 
 For information about adding signals to a PDU, refer to *Creating a
 Signal* in [Editing Signals](editing-signals.html).
3. Do one of the following:
  - For supported database files (i.e., DBC and XML), select File»Save to save your changes to the database.
  - For unsupported database file formats, select File»Save As , and save the modified database in FIBEX XML format.

Parent topic:

Editing a Database

<!--NI_TOPIC bundle=xnet-db-editor path=editing-signals.html language=enus -->
## TOPIC 00019: Editing Signals

- bundle_id: `xnet-db-editor`
- source_path: `editing-signals.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/editing-signals.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Edit or delete an existing signal, or create a new signal. Editing a SignalEdit an existing signal by modifying its signal properties. Deleting a SignalTo delete a signal, select the signal in the navigation tree, and then select Edit Delete . Creating a Signal In the navigation tree, right-click a

Editing Signals

Edit or delete an existing signal, or create a new signal.

#### Editing a Signal

Edit an existing [signal](signal.html) by
 modifying its [signal properties](signal-properties.html).

#### Deleting a Signal

To delete a signal,
 select the signal in the navigation tree, and then select Edit»Delete.

#### Creating a Signal

1. In the navigation tree, right-click a frame, or a PDU if defined, and select
 Create Signal.
2. Provide a name for the [signal](signal.html), and configure [signal
 properties](signal-properties.html).
3. Do one of the following:
  - For supported database files (i.e., DBC and XML), select File»Save to save your changes to the database.
  - For unsupported database file formats, select File»Save As , and save the modified database in FIBEX XML format.

Parent topic:

Editing a Database

<!--NI_TOPIC bundle=xnet-db-editor path=exporting-cluster.html language=enus -->
## TOPIC 00020: Exporting a Cluster

- bundle_id: `xnet-db-editor`
- source_path: `exporting-cluster.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/exporting-cluster.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Export a CAN cluster or LIN cluster as a DBC or LDF file, respectively. The database that contains the cluster you want to export must first be loaded in the NI-XNET Database Editor. When you export a database cluster, only features that XNET sessions use to communicate on the network are saved to t

Exporting a Cluster

Export a CAN cluster or LIN cluster as a DBC or LDF file, respectively.

NI-XNET Database
 Editor

When you export a database cluster,
 only features that XNET sessions use to communicate on the network are saved to the
 file. If the original database was created using software other than NI-XNET, the target
 file may be missing details from the original.

1. In the current database, right-click the CAN or LIN cluster that you want to
 export.
2. Select Export cluster. 
 The Export Cluster dialog opens.
3. Provide a file name and use the dialog to browse to the location on your system
 where you want to save the cluster.
4. Click OK.

Parent topic:

Saving and Exporting

<!--NI_TOPIC bundle=xnet-db-editor path=exporting-database.html language=enus -->
## TOPIC 00021: Exporting a Database

- bundle_id: `xnet-db-editor`
- source_path: `exporting-database.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/exporting-database.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Export a DBC or LDF database as a FIBEX database file. The database you want to export must first be loaded in the NI-XNET Database Editor. When you export a database, only features that XNET sessions use to communicate on the network are saved to the file. If the original file was created using sof

Exporting a Database

Export a DBC or LDF database as a FIBEX database file.

NI-XNET Database Editor

When you export a database, only
 features that XNET sessions use to communicate on the network are saved to the file. If the
 original file was created using software other than NI-XNET, the target file may be missing
 details from the original file.

1. Select File»Export as FIBEX. 
 The Export to FIBEX file dialog opens.
2. Provide a file name and use the dialog to browse to the location on your system where
 you want to save the database file.
3. Click Save.

Parent topic:

Saving and Exporting

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=flexray-ecu-properties.html language=enus -->
## TOPIC 00022: FlexRay ECU Properties

- bundle_id: `xnet-db-editor`
- source_path: `flexray-ecu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/flexray-ecu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the ECU Properties page if the database cluster is configured to use the FlexRay protocol. Name ECU name. This must be unique within the cluster. Cold Start Indicates whether the ECU transmits a startup frame. Connected Channels Indicates to which of the two

FlexRay ECU Properties

The following properties are available on the ECU Properties page if the database cluster
 is configured to use the FlexRay protocol.

Name

Cold Start

Connected Channels

Wakeup Channels

Wakeup Pattern

TX Frames

RX Frames

Comment

Figure 3.

[IMAGE alt='1378' src='GUID-5DC9A834-5346-4888-BD3C-386B81FD95BA-a5.png']

Parent topic:

ECU Properties

<!--NI_TOPIC bundle=xnet-db-editor path=format.html language=enus -->
## TOPIC 00023: Database Formats

- bundle_id: `xnet-db-editor`
- source_path: `format.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/format.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-XNET supports most common automotive database formats, including CAN database (DBC), NI-CAN database (NCD), FIBEX XML, and LIN description file (LDF). The NI-XNET Database Editor enables you to export databases as FIBEX databases file in XML format.

Database Formats

NI-XNET supports most common automotive database formats, including CAN database (DBC),
 NI-CAN database (NCD), FIBEX XML, and LIN description file (LDF).

The NI-XNET Database Editor enables you to export databases as FIBEX databases file in XML format.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=frame-properties-can.html language=enus -->
## TOPIC 00024: CAN Frame Properties

- bundle_id: `xnet-db-editor`
- source_path: `frame-properties-can.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/frame-properties-can.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Frame Properties page if the database cluster is configured to use the CAN protocol. Name Name of the frame. This must be unique within the cluster. Arbitration ID CAN frame identifier. This ID is used to determine priority during arbitration. In the sta

CAN Frame Properties

The following properties are available on the Frame Properties page if the database cluster
 is configured to use the CAN protocol.

Name

Arbitration ID

11 bits

11
 bits

18 bits

29-Bit ID

29-Bit ID

Arbitration ID

Payload Length

0–8 bytes

Timing Type

CAN: Timing Type

Cyclic and Event Timing

I/O Mode

CAN

0–8
 bytes

CAN FD

64 bytes

CAN FD + BRS

Transmit Time

Mapped PDUs

Bit Layout

Show as PDUs

Comment

The following properties are available in the J1939 Configuration
 panel of the Frame Properties page if the database cluster is configured to use the SAE
 J1939 application protocol with CAN.

J1939 PGN

Reserved (EDP)

Data
 Page

PDU Format

Data Page

Reserved
 (EDP)

PDU Format

PDU Format

PDU Specific

PDU Format

PDU Specific

PDU Format

PDU Specific

Priority

Source Address

Parent topic:

Frame Properties

<!--NI_TOPIC bundle=xnet-db-editor path=frame-properties-flexray.html language=enus -->
## TOPIC 00025: FlexRay Frame Properties

- bundle_id: `xnet-db-editor`
- source_path: `frame-properties-flexray.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/frame-properties-flexray.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Frame Properties page if the database cluster is configured to use the FlexRay protocol. Name Name of the frame. This must be unique within the cluster. Payload Length Number of data bytes that can be transmitted in the frame's payload. The payload lengt

FlexRay Frame Properties

The following properties are available on the Frame Properties page if the database
 cluster is configured to use the FlexRay protocol.

Name

Payload Length

0 to 254 bytes

Cycle Repetitions

In-Cycle Repetitions

Slot ID

Channel
 Assignment

Slot ID

Channel Assignment

Sync

Startup

Preamble

n

n

Network Management Vector Length

Mapped PDUs

Bit Layout

Show as PDUs

Comment

Parent topic:

Frame Properties

<!--NI_TOPIC bundle=xnet-db-editor path=frame-properties-lin.html language=enus -->
## TOPIC 00026: LIN Frame Properties

- bundle_id: `xnet-db-editor`
- source_path: `frame-properties-lin.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/frame-properties-lin.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the Frame Properties page if the database cluster is configured to use the LIN protocol. Name Name of the frame. This must be unique within the cluster. Unprotected ID LIN frame identifier, which is a number 0 to 63. This number identifies the content of the

LIN Frame Properties

The following properties are available on the Frame Properties page if the database
 cluster is configured to use the LIN protocol.

Name

Unprotected ID

Payload Length

0–8 bytes

LIN Checksum

Mapped PDUs

Bit Layout

Show as PDUs

Comment

Parent topic:

Frame Properties

<!--NI_TOPIC bundle=xnet-db-editor path=frame-properties.html language=enus -->
## TOPIC 00027: Frame Properties

- bundle_id: `xnet-db-editor`
- source_path: `frame-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/frame-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frame properties vary depending on the communication protocol of the cluster. Use the NI-XNET Database Editor to edit frame properties.

Frame Properties

Frame properties vary depending on the communication protocol of the cluster. Use the
 NI-XNET Database Editor to edit frame properties.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=frame.html language=enus -->
## TOPIC 00028: Frames

- bundle_id: `xnet-db-editor`
- source_path: `frame.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/frame.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: A frame is a single message exchanged on a cluster. Each cluster can contain any number of frames. There are four types of frames on a CAN bus: Data frame – used to transmit data. Remote frame – used to request data. Error frame – transmitted by any node on the bus that detects an error. Overload fr

Frames

A frame is a single message exchanged on a cluster. Each cluster can contain any number of
 frames. There are four types of frames on a CAN bus:

- Data frame – used to transmit data.
- Remote frame – used to request data.
- Error frame – transmitted by any node on the bus that detects an error.
- Overload frame – transmitted by receiving devices to indicate they are not yet ready
 to receive data.

The data frame is the only frame used for actual data transmission, and it consists of
 three major segments: header, payload, and trailer. Frame formats differ according to
 communication protocol; refer to NI-XNET Hardware and Software Help for detailed information.

The most basic frame properties are the *identifier* (Arbitration ID for CAN,
 Slot ID for FlexRay) and the *payload length*, which can be 0–8 bytes for
 CAN, or 0–254 bytes (even values only) for FlexRay.

In addition to the basic properties, CAN, FlexRay, and LIN frames have several
 protocol-specific properties. Use the NI-XNET Database Editor to edit properties according to the protocol of the cluster.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=j1939-ecu-properties.html language=enus -->
## TOPIC 00029: J1939 ECU Properties

- bundle_id: `xnet-db-editor`
- source_path: `j1939-ecu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/j1939-ecu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the ECU Properties page if the database cluster is configured to use CAN I/O mode with the SAE J1939 application protocol. Name ECU name. This must be unique within the cluster. Preferred Address Specifies the preferred J1939 node address to be used when sim

J1939 ECU Properties

The following properties are available on the ECU Properties page if the database cluster
 is configured to use CAN I/O mode with the SAE J1939 application protocol.

Name

Preferred Address

Node Name

Node Name

Preferred Address

Identity Number

Manufacturer Code

ECU Instance

Industry Group

Arbitrary Address Capable

Reserved

Function

Industry Group

Function Instance

Function

Vehicle System

Vehicle System

Industry Group

Vehicle System Instance

TX Frames

RX Frames

Comment

Figure 2.

[IMAGE alt='1378' src='GUID-07F33144-1876-4D25-B7D5-7008ABDFB9BF-a5.png']

Parent topic:

ECU Properties

<!--NI_TOPIC bundle=xnet-db-editor path=lin-ecu-properties.html language=enus -->
## TOPIC 00030: LIN ECU Properties

- bundle_id: `xnet-db-editor`
- source_path: `lin-ecu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/lin-ecu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are available on the ECU Properties page if the database cluster is configured to use the LIN protocol. Name ECU name. This must be unique within the cluster. LIN Master Indicates whether the ECU is a LIN Master or LIN Slave. Protocol Version LIN protocol version supported b

LIN ECU Properties

The following properties are available on the ECU Properties page if the database cluster
 is configured to use the LIN protocol.

Name

LIN Master

Protocol Version

Supplier ID

Function ID

Initial NAD

Configured NAD

P2min

STmin

TX Frames

RX Frames

Comment

Figure 4.

[IMAGE alt='LIN ECU Properties screen' src='GUID-002A0EC4-BCC0-4A1B-906C-8F447B0A8F9A-a5.png']

Parent topic:

ECU Properties

<!--NI_TOPIC bundle=xnet-db-editor path=lin-schedule-properties.html language=enus -->
## TOPIC 00031: LIN Schedule Properties

- bundle_id: `xnet-db-editor`
- source_path: `lin-schedule-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/lin-schedule-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: Name Schedule name; this name must be unique within the cluster. Type Specifies the type of schedule entry: Unconditional, Sporadic, or Event-triggered. Frames Specifies the frame to be transmitted. Delay Duration of time (in milliseconds) after the previous frame's transmission before this frame wi

LIN Schedule Properties

Name

Type

Frames

Delay

Event ID

Unprotected ID

LIN Frame Properties

Collision Resolving Schedule

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=lin-schedules.html language=enus -->
## TOPIC 00032: LIN Schedules

- bundle_id: `xnet-db-editor`
- source_path: `lin-schedules.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/lin-schedules.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: In LIN networks, a dedicated Master node is responsible for issuing frames on the bus. For this purpose, it executes a schedule that defines the sequence of frames to be transferred on the bus. Schedules can be periodic or run once, and more than one schedule can exist, which the Master node can swi

LIN Schedules

In LIN networks, a dedicated Master node is responsible for issuing frames on the bus.
 For this purpose, it executes a schedule that defines the sequence of frames to be
 transferred on the bus. Schedules can be periodic or run once, and more than one
 schedule can exist, which the Master node can switch between.

- Unconditional—Frame x is sent at a specified delay after the
 previous frame.
- Sporadic—Out of a collection of several frames, one with data available is sent.
 If more than one frame has data available, the Master node chooses a frame to
 send at its discretion. Only the Master node can send these frames.
- Event-triggered—Out of a collection of several frames, one with data available
 is sent. As this mode is not restricted to the Master node, more than one node
 can start sending. If such a collision occurs, the Master node detects it and
 executes a special collision-resolving schedule that allows each node to
 transmit its data.

For more details, refer to the *LIN Protocol Specification*.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=managing-aliases.html language=enus -->
## TOPIC 00033: Managing Aliases

- bundle_id: `xnet-db-editor`
- source_path: `managing-aliases.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/managing-aliases.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an alias to reference a specific database file. An alias provides a shorter, easier-to-read name for use within your application. FlexRay and LIN protocols require alias names to be assigned to databases, while the CAN protocol does not. Alias names are used in many NI-XNET features, including t

Managing Aliases

Use an alias to reference a specific database file. An alias provides a shorter,
 easier-to-read name for use within your application. FlexRay and LIN protocols require alias
 names to be assigned to databases, while the CAN protocol does not.

Alias names are used in many NI-XNET features, including the deployment of database files
 to LabVIEW Real-Time targets.

When you open a database file in the NI-XNET Database Editor, the database name
 and path are automatically added to the Alias Manager.

Select View»Alias Manager to open the Alias Manager.

The Path information for a local alias cannot be modified manually,
 but you can specify or change the Name either before or after the
 database is added to the Alias Manager.

To add a database manually to the Alias Manager, do the following:

1. In the Local Aliases section, click the cluster icon at the right of an empty row to
 open the Open Database window.
2. Use the Open Database explorer window to locate a database file you want to add.
3. Select the database file, and click Open .
4. In Local Aliases, click the add symbol (+) to add a new row to the bottom of the
 list.

Note

To display configurable properties for a database, click the gear icon at the right of the
 row to open the Alias Properties window.

To add an alias for an RT target, you must first provide the target hostname or IP address and
 valid connection credentials in the appropriate fields, and then click
 Connect. Once connected, click Deploy
 Alias to select a database to deploy.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=manual-overview.html language=enus -->
## TOPIC 00034: NI-XNET Database Editor

- bundle_id: `xnet-db-editor`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/manual-overview.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-XNET Database Editor Manual includes an overview of automotive database concepts, user instructions, and reference information for using the database editor. The NI-XNET Database Editor enables you to view and manage automotive databases for CAN, CAN/FD, FlexRay, and LIN networks. This utilit

NI-XNET Database Editor

The NI-XNET Database Editor Manual includes an overview of automotive database concepts, user instructions, and reference
 information for using the database editor.

The NI-XNET Database Editor enables you to view and manage automotive databases for CAN, CAN/FD, FlexRay, and LIN
 networks. This utility provides support for modern automotive industry standards such as
 AUTOSAR.

#### Top Tasks

| Opening a Database | Open and load a database file. |
| --- | --- |
| Searching the Database | Search for database objects, and filter by signal, frame, cluster ECU, or PDU. |
| Editing Clusters | Create or delete database objects such as clusters, frames, PDUs, and signals. |
| Configuring Signals | Configure a signal by specifying its signal type, data type, and byte order,and by modifying configuration parameters in Signal Properties. |
| Saving and Exporting | Save changes to the current database, save the current database to a new location, or export the database as a FIBEX database file. |

<!--NI_TOPIC bundle=xnet-db-editor path=mapping-pdus-to-frame.html language=enus -->
## TOPIC 00035: Mapping PDUs to a Frame

- bundle_id: `xnet-db-editor`
- source_path: `mapping-pdus-to-frame.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/mapping-pdus-to-frame.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Map PDUs to a frame, or unmap a PDU. One PDU can be mapped to multiple frames, and multiple PDUs can be mapped to a single frame. To unmap a PDU from a frame, click the X at the right of the PDU you want to remove. Expand the cluster and the Frames node, and select the frame to which you want to map

Mapping PDUs to a Frame

Map [PDUs](pdu.html) to
 a frame, or unmap a PDU.

X

1. Expand the cluster and the Frames node, and select the frame to which you want
 to map the PDU.
2. In the Mapped PDUs panel on the Frame Properties page,
 click Select New PDU and select a PDU from the
 list.
3. Click the add symbol (+) at the right of the row to add the PDU. 
 The selected PDU is added to the list of PDUs mapped to the
 frame.

Parent topic:

Editing Frames

<!--NI_TOPIC bundle=xnet-db-editor path=multiplexed-signals.html language=enus -->
## TOPIC 00036: Creating Multiplexed Signals

- bundle_id: `xnet-db-editor`
- source_path: `multiplexed-signals.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/multiplexed-signals.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a multiplexed signal by changing its signal type to Multiplexed and assigning a mode value. The NI-XNET Database Editor handles subframe manipulation behind the scenes. Configure one signal to be a multiplexer signal. In Signal Properties, change the Signal Type for the selected signal to Mul

Creating Multiplexed Signals

Create a multiplexed signal by changing its signal type to Multiplexed and assigning a
 mode value. The NI-XNET Database Editor handles subframe manipulation behind the scenes.

1. Configure one signal to be a multiplexer signal. In Signal
 Properties, change the Signal Type
 for the selected signal to
 Multiplexer.
2. Select another signal, and configure it to be a multiplexed
 signal. In Signal Properties, change the Signal
 Type for the selected signal to
 Multiplexed.
3. Change the Mode Value for the
 multiplexed signal to match the mode value of the
 multiplexer signal.
4. Select File»Save As. 
 The Save Database As explorer window opens.
5. Select the database file or provide a file name, and click
 Save to save your changes to
 the database file.

For more information about multiplexed signals, refer to KB article [How Do Multiplexed Signals Work In NI-XNET
 Database Editor and in LabVIEW?](http://www.ni.com/r/xnetmux)

Parent topic:

Configuring Signals

<!--NI_TOPIC bundle=xnet-db-editor path=opening-database.html language=enus -->
## TOPIC 00037: Opening a Database

- bundle_id: `xnet-db-editor`
- source_path: `opening-database.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/opening-database.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Open and load a database file. Do one of the following: Select File Open File . Click Open Database on the Database Editor Start page. Click Open Database in the left pane. The Open Database window opens. Browse to the location of the database file. Select the file, and click Open. The database file

Opening a Database

Open and load a database file.

1. Do one of the following: 
 
 The Open Database window opens.
  - Select File»Open File .
  - Click Open Database on the Database Editor Start
 page.
  - Click Open Database in the left pane.
2. Browse to the location of the database file. Select the file, and click
 Open. 
 The database file is loaded in the editor, and the navigation pane
 shows a tree view of the open database.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=pdu-properties.html language=enus -->
## TOPIC 00038: PDU Properties

- bundle_id: `xnet-db-editor`
- source_path: `pdu-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/pdu-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: All PDUs in a cluster are grouped together under the PDUs parent node. When you select a PDU, the properties page for that PDU is displayed in the content pane. The PDU Properties page contains the following properties: Name PDU name. This must be unique within the cluster. Payload Length Length of

PDU Properties

All PDUs in a cluster are grouped together under the PDUs
 parent node. When you select a PDU, the properties page for that PDU is displayed in
 the content pane. The PDU Properties page contains the following properties:

Name

Payload Length

8 bytes

254 bytes

Bit Layout

Comment

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=pdu.html language=enus -->
## TOPIC 00039: PDUs

- bundle_id: `xnet-db-editor`
- source_path: `pdu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/pdu.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: A protocol data unit (PDU) is a data unit that is defined in a cluster and exchanged within a frame. PDUs encapsulate network data and provide a way to communicate information between independent protocols, such as in a CAN-FlexRay gateway. You can think of a PDU as a container of signals. A single

PDUs

A protocol data unit (PDU) is a data unit that is defined in a cluster and exchanged within a
 frame. PDUs encapsulate network data and provide a way to communicate information
 between independent protocols, such as in a CAN-FlexRay gateway. You can think of a PDU
 as a container of signals. A single container (PDU) can be transmitted in multiple
 frames, and a single frame can contain multiple PDUs.

#### PDUs and Frames

A frame can contain any number of non-overlapping PDUs. A frame can have multiple PDUs, and
 the same PDU can exist in different frames. The following figure shows the
 one-to-n (one PDU in n number of frames) and
 n-to-one (n number of PDUs in one frame)
 relationships.

[IMAGE alt='Diagram showing a single PDU in 3 different frames, and three different PDUs in a single frame' src='GUID-914852EC-EF0C-424A-888D-B2FDEFA75566-a5.svg']

Note

#### PDUs and Signals

Like a frame, a PDU contains an arbitrary number of signals. A PDU acts like a container
 for a logical group of signals. The following figure represents the relationship between
 frames, PDUs, and signals.

[IMAGE alt='Diagram depicting PDUs as containers for signals, and the PDUs withing frames' src='GUID-4F4AD2D0-0D66-417E-918C-0F19ACB4C1AA-a5.svg']

#### PDU Properties

PDU properties provide such information as the position of the PDU in a frame, size,
 signals within the PDU, and so on. Three such properties are Start
 Bit, Payload Length, and Update
 Bit.

The Start Bit of a PDU within the frame indicates where in the
 frame the particular PDU data starts.

Payload Length defines the size of the PDU in bytes.

The receiver uses the Update Bit to determine whether the
 frame sender has updated data in a particular PDU. Update bits allow for the
 decoupling of a signal update from a frame occurrence. Update But is an optional PDU
 property.

#### Timing

Because the same PDU can exist in multiple frames, PDUs can have flexible transmission
 schedules. For example, in the following diagram, the first PDU is transmitted in Frame 1
 (Timing 1) as well as in Frame 2 (Timing 2); the receiving node receives the PDU according
 to the different timings of the containing frames.

[IMAGE alt='Timing diagram showing frame timing with some PDUs in multiple frames' src='GUID-C975A438-8538-4106-B7FD-0467397BCB52-a5.svg']

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=saving-database.html language=enus -->
## TOPIC 00040: Saving the Database File

- bundle_id: `xnet-db-editor`
- source_path: `saving-database.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/saving-database.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Save changes to the current database file or save the database to a new location. Saving ChangesTo save changes to a supported database file, select File Save or press Ctrl + S.Only features that XNET sessions use to communicate on the network are saved to the file. If the original file was created

Saving the Database File

Save changes to the current database file or save the database to a new
 location.

#### Saving Changes

To save changes to a supported database file, select File»Save or press Ctrl + S.

Note

#### Using Save As

Save As

1. Select File»Save As or press Ctrl + Shift + S. 
 The Save Database As dialog opens.
2. Provide a file name and use the dialog to browse to the location on your system
 where you want to save the database file. (Click New
 folder to create a folder, if needed.)
3. Click Save to save the database to the specified
 location.

Note

Parent topic:

Saving and Exporting

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=saving-exporting-databases.html language=enus -->
## TOPIC 00041: Saving and Exporting

- bundle_id: `xnet-db-editor`
- source_path: `saving-exporting-databases.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/saving-exporting-databases.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-XNET Database Editor enables you to save changes to the current database, save the current database to a new location, and export a database to FIBEX XML. You can also export CAN and LIN clusters. Only features that XNET sessions use to communicate on the network are saved to the file. If the

Saving and Exporting

The NI-XNET Database Editor enables you to [save changes](saving-database.html) to the current database,
 save the current database to a new location, and [export a database](exporting-database.html) to FIBEX XML. You
 can also export [CAN and LIN
 clusters](exporting-cluster.html).

Note

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=searching.html language=enus -->
## TOPIC 00042: Searching the Database

- bundle_id: `xnet-db-editor`
- source_path: `searching.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/searching.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `task`
- source_description: Search for database objects. You can filter the search by Signal, Frame, Cluster, ECU, and PDU. Search for database objects by name or by comments. you can filter your search by Signal, Frame, Cluster, ECU, and PDU. Click the search icon in the toolbar. The left pane displays a search field with a f

Searching the Database

Search for database objects. You can filter the search by Signal, Frame, Cluster, ECU,
 and PDU.

Search for database objects by name or by
 comments. you can filter your search by Signal, Frame, Cluster, ECU, and PDU.

1. Click the search icon in the toolbar. 
 The left pane displays a search field with a filter icon
 on the right side.
2. Enter a full or partial search string in the field.
3. Click the filter icon, and select or deselect criteria to
 filter your search.
4. Press Enter on the keyboard. 
 Search results are displayed in the left pane, below the
 search field.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=signal-properties.html language=enus -->
## TOPIC 00043: Signal Properties

- bundle_id: `xnet-db-editor`
- source_path: `signal-properties.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/signal-properties.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI-XNET describes each signal in the database using several parameters, or properties. The NI-XNET Database Editor enables you to configure signals by editing signal properties. Available properties are as follows. Required properties are indicated with an asterisk (*): Name Signal name. This must b

Signal Properties

NI-XNET describes each signal in the database using several parameters, or
 properties. The NI-XNET Database Editor enables you to configure signals by editing signal properties. Available
 properties are as follows. Required properties are indicated with an asterisk
 (*):

Name

Type

- Static–Signal that is contained in every frame transmitted.
- Multiplexer–Signal that carries an identifier for multiplexed signals.
- Multiplexed–Signal that is combined with other signals that share the same multiplexer
 identifier.

Mode Value

Start Bit*

Number of Bits*

Data Type*

Byte Order*

- Little Endian–Bits are counted from the least significant bit to the
 highest address.
- Big Endian–Bits are counted from the most significant bit to the lowest address.

Scaling Factor

Scaling Offset

Maximum

Minimum

Default Value

Unit

Bit Layout

Comment

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=signal.html language=enus -->
## TOPIC 00044: Signals

- bundle_id: `xnet-db-editor`
- source_path: `signal.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/signal.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signals are the basic data exchange units on a vehicle network, and are equivalent to CAN channels. Each frame contains an arbitrary number of signals. Individual signals that are transmitted (speed or temperature, for example) are often less than the maximum payload of a frame, therefore several si

Signals

Signals are the basic data exchange units on a vehicle network, and are equivalent to CAN
 *channels*.

Each frame contains an arbitrary number of signals. Individual signals that are
 transmitted (speed or temperature, for example) are often less than the maximum payload
 of a frame, therefore several signals are typically sent together in the same frame.

*Static signals* are contained in every frame transmitted, as opposed to
 dynamic signals, which are transmitted depending on the multiplexer value. A static
 signal can be used to create a dynamic signal. However, the dynamic signal cannot be
 changed to a static signal afterward.

A *dynamic signal* is transmitted in the frame when the multiplexer signal in
 the frame has a given value specified in the subframe. Dynamic signals may overlap other
 dynamic signals when they have a different multiplexer value.

A *multiplexer signal* carries an identifier for multiplexed signals.
 Multiplexer signals may not overlap other static or dynamic signals in the frame. A PDU
 can contain only one multiplexer signal.

*Multiplexed signals* are separate signals that occupy the same bit space in a
 frame. They are linked by a separate, multiplexer signal that determines which signal
 gets to occupy that bit space in that particular frame instance. Multiplexed signals are
 transmitted using the same multiplexer identifier.

Parent topic:

NI-XNET Database Editor

<!--NI_TOPIC bundle=xnet-db-editor path=troubleshooting.html language=enus -->
## TOPIC 00045: Troubleshooting

- bundle_id: `xnet-db-editor`
- source_path: `troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/xnet-db-editor/raw/resource/enus/troubleshooting.html
- source_language: `enus`
- document_id: `xnet-db-editor`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-XNET Database Editor error log enables you to view detailed information about errors that occurred while using the editor. By default, an error log is generated in the following path: C:\Users\[user]\AppData\Local\National Instruments\NI-XNET\log\niXntDatabaseEditor.log. To open the error log

Troubleshooting

The NI-XNET Database Editor error log enables you to view detailed information about errors that occurred
 while using the editor. By default, an error log is generated in the following path:
 C:\Users\[user]\AppData\Local\National
 Instruments\NI-XNET\log\niXntDatabaseEditor.log.

To open the error log from the NI-XNET Database Editor, select View»Open Error Log.

The error log provides for each event a time and date stamp, indication of whether
 the event was an error or warning, description of the event, and file path for the
 database active when the event occurred.

For further assistance, consider asking the NI community through the Automotive and
 Embedded Networks [discussion forum](http://www.ni.com/r/aenforum).

For detailed information about the XNET API or working with frames and signals in
 NI-XNET, refer to *NI-XNET Hardware and Software Help*.

Refer to [NI Product Manuals](https://search.ni.com/nisearch/app/main/p/bot/no/ap/tech/lang/en/pg/1/sn/catnav:pm/q/xnet%20database%20editor/) for updated documentation
 resources.

Parent topic:

NI-XNET Database Editor
