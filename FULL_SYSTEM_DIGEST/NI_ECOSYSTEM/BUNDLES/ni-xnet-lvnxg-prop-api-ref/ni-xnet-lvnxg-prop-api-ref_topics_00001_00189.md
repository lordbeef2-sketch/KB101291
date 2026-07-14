# NI DOCUMENT BUNDLE: ni-xnet-lvnxg-prop-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-xnet-lvnxg-prop-api-ref start=1 end=189 -->
<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=ni-xnet-properties.html language=enus -->
## TOPIC 00001: NI-XNET Properties

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `ni-xnet-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/ni-xnet-properties.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Topics in this section describe the properties available in NI-XNET property nodes.

NI-XNET Properties

Topics in this section describe the properties available in NI-XNET property
 nodes.

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-applprotocol-10073.html language=enus -->
## TOPIC 00002: ApplProtocol

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-applprotocol-10073.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-applprotocol-10073.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the application protocol that the session uses. The database used with the XNET Create Session node determines the application protocol. Enumeration Value Description None 0 The default application protocol. J1939 1 Indicates J1939 clusters. This value enables the following features: Sendi

ApplProtocol

Specifies the application protocol that the session uses. The database used with the
 XNET Create Session node determines the application protocol.

| Enumeration | Value | Description |
| --- | --- | --- |
| None | 0 | The default application protocol. |
| J1939 | 1 | Indicates J1939 clusters. This value enables the following features: Sending/receiving long frames as the SAE J1939 specification specifies, using the J1939 transport protocol. Using a special notation for J1939 identifiers. Using J1939 address claiming. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-baudrate64-9010001.html language=enus -->
## TOPIC 00003: BaudRate64

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-baudrate64-9010001.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-baudrate64-9010001.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Sets the baud rate that all cluster nodes use. This baud rate represents the rate from the database, so it is read-only from the session. Use a session interface property (for example, Interface:64bit Baud Rate) to override the database baud rate with an application-specific baud rate. CAN For CAN,

BaudRate64

Sets the baud rate that all cluster nodes use.

This baud rate represents the rate from the database, so it is read-only from the session. Use
 a session interface property (for example, Interface:64bit Baud Rate)
 to override the database baud rate with an application-specific baud rate.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read/Write

#### CAN

For CAN, this rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000,
 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some
 transceivers may only support a subset of these values.

If you need values other than these, use the custom settings as described in the Interface:64bit Baud Rate property.

#### FlexRay

For FlexRay, this baud rate can be 2500000, 5000000, or 10000000.

#### LIN

For LIN, this baud rate can be 2400–20000, inclusive.

If you need values other than these, use the custom settings as described in the Interface:64bit Baud Rate property.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-can-iomode-10010.html language=enus -->
## TOPIC 00004: CAN.IoMode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-can-iomode-10010.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-can-iomode-10010.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: CAN I/O mode used by the cluster. This property is a ring (enumerated list) of three values. Enumeration Value Description CAN 0 Default CAN 2.0 A/B standard I/O mode as defined in ISO 11898-1:2003. A fixed baud rate is used for transfer, and the payload length is limited to 8 bytes. CAN FD 1 CAN FD

CAN.IoMode

CAN I/O mode used by the cluster. This property is a ring (enumerated list) of three
 values.

| Enumeration | Value | Description |
| --- | --- | --- |
| CAN | 0 | Default CAN 2.0 A/B standard I/O mode as defined in ISO 11898-1:2003. A fixed baud rate is used for transfer, and the payload length is limited to 8 bytes. |
| CAN FD | 1 | CAN FD mode as specified in the CAN with Flexible Data-Rate specification, version 1.0. Payload lengths up to 64 bytes are allowed, but they are transmitted at a single fixed baud rate defined by the XNET Cluster 64bit Baud Rate or XNET Session Interface:64bit Baud Rate properties. |
| CAN FD+BRS | 2 | CAN FD with optional Baud Rate Switching enabled. Payload lengths up to 64 bytes are allowed; the data portion of the CAN frame is transferred at a different (higher) baud rate, defined by the CAN:64bit FD Baud Rate or XNET Session Interface:CAN:64bit FD Baud Rate properties. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-cluster-configuration-status-10009.html language=enus -->
## TOPIC 00005: ConfigStatus

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-cluster-configuration-status-10009.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-cluster-configuration-status-10009.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configuration status of the cluster. This property is used only if the Database ShowInvalidFromOpen? property is changed from default value to True. Configuration Status returns an NI-XNET error code. You can pass the value to the error code input of the Simple Error Handler node to convert it to a

ConfigStatus

Configuration status of the cluster.

This property is used only if the Database ShowInvalidFromOpen?
 property is changed from default value to True.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read

Configuration Status returns an NI-XNET error code. You can pass the value to the
 error code input of the Simple Error Handler node
 to convert it to a text description (on message output) of the configuration
 problem.

By default, incorrectly configured clusters in the database are not returned from the XNET
 Database Clusters property because they cannot be used in the bus
 communication. You can change this behavior by setting the XNET Database ShowInvalidFromOpen? property to True. When the configuration status
 of a cluster becomes invalid after the database has been opened, the cluster
 still is returned from the XNET Database Clusters property, even if
 ShowInvalidFromOpen? is False.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-cluster-database-5010002.html language=enus -->
## TOPIC 00006: Database

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-cluster-database-5010002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-cluster-database-5010002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Database (XNET Database I/O Name) that contains this cluster. The parent database is defined when the cluster is created; you cannot change it afterward.

Database

Database (XNET Database I/O Name) that contains this cluster.

The parent database is defined when the cluster is created; you cannot change it afterward.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-ecus-6010003.html language=enus -->
## TOPIC 00007: ECUs

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-ecus-6010003.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-ecus-6010003.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Array of ECUs (array of XNET ECU I/O names) contained in the cluster. An ECU is assigned to a cluster when the ECU object is created. You cannot change this assignment afterward. To add an ECU to a cluster, use the XNET Database Create (ECU) node. To remove an ECU from the cluster, use the XNET Data

ECUs

Array of ECUs (array of XNET ECU I/O names) contained in the cluster.

An ECU is assigned to a cluster when the ECU object is created. You cannot change this
 assignment afterward.

To add an ECU to a cluster, use the [XNET Database Create
 (ECU)](/csh?topicname=xnet-database-create-ecu.html) node. To remove an ECU from the cluster, use the [XNET Database Delete
 (ECU)](/csh?topicname=xnet-database-delete-ecu.html) node.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-lin-tick-1010071.html language=enus -->
## TOPIC 00008: LIN.Tick

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-lin-tick-1010071.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-lin-tick-1010071.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Relative time between LIN ticks (f64, relative time in seconds). The XNET LIN Schedule Entry:Delay property must be a multiple of this tick. This tick is referred to as the "timebase" in the LIN specification. The XNET ECU LIN:Master? property defines the LIN:Tick property in this cluster. You canno

LIN.Tick

Relative time between LIN ticks (f64, relative time in seconds).

The XNET LIN Schedule Entry:Delay property must be a
 multiple of this tick. This tick is referred to as the "timebase" in the LIN
 specification.

The XNET ECU
 LIN:Master? property defines the LIN:Tick property in
 this cluster. You cannot use the LIN:Tick property when there is
 no LIN:Master? property defined in this cluster.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster-pdus-required-201000a.html language=enus -->
## TOPIC 00009: PDUsReqd?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster-pdus-required-201000a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster-pdus-required-201000a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines whether this cluster requires using PDUs in the database API. If this property is False, you can ignore the PDU concept for this cluster and it is safe to use signals as child objects of a frame without PDUs. If this property returns True, the cluster contains a PDU configuration, which r

PDUsReqd?

Determines whether this cluster requires using PDUs in the database
 API.

If this property is False, you can ignore the PDU concept for this cluster and it is safe
 to use signals as child objects of a frame without PDUs.

If this property returns True, the cluster contains a PDU configuration, which requires
 reading PDUs as child objects of a frame and signals as child objects of a PDU.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Cluster](xnet-cluster.html)

**Permissions:** Read

Internally, the database always uses PDUs, but it shows signal objects as
 children of both frame and PDU.

The following conditions must be fulfilled for all frames in the cluster to
 return False from the PDUs Required? property:

- Only one PDU is mapped to the frame.
- This PDU is not mapped to other frames.
- The PDU Start Bit in the frame is 0.
- The PDU Update Bit is not used.

If the conditions are not fulfilled for a given frame, signals from the frame are
 still returned, but reading the property returns a warning.

The NI-XNET session only supports frames that require a PDU for FlexRay. On a CAN or LIN
 cluster, frames that require a PDU cause the XNET Frame Configuration Status
 property and the [XNET Create
 Session](/csh?topicname=xnet-create-session.html) node to return an error.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Cluster

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-cluster.html language=enus -->
## TOPIC 00010: XNET Cluster Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-cluster.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET Cluster I/O name. Use the XNET Cluster property node to change the properties for an XNET cluster I/O name..

XNET Cluster

Reads and writes properties for an XNET Cluster I/O name.

Use the XNET Cluster property node to change the properties for an XNET cluster I/O
 name..

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-database-clsts-6000002.html language=enus -->
## TOPIC 00011: Clusters

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-database-clsts-6000002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-database-clsts-6000002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of XNET Cluster I/O names in this database. A cluster is assigned to a database when the cluster object is created; you cannot change this assignment afterward. You can use an array element to read or write the cluster properties (for example, cluster protocol or cluster frames). Re

Clusters

Returns an array of XNET Cluster I/O names in this database.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Database](xnet-database.html)

**Permissions:** Read

A cluster is assigned to a database when the cluster object is created; you
 cannot change this assignment afterward.

You can use an array element to read or write the cluster properties (for
 example, cluster protocol or cluster frames). Refer to XNET Cluster I/O Name for
 information about using XNET I/O names.

FIBEX and AUTOSAR files can contain any number of clusters, and each cluster uses
 a unique name. For CANdb (.dbc), LDF (.ldf), or NI-CAN (.ncd) files, the file
 contains only one cluster, and no cluster name is stored in the file. For these
 database formats, NI-XNET uses the name Cluster for the single cluster.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Database

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-database.html language=enus -->
## TOPIC 00012: XNET Database Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-database.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-database.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET Database I/O name. Use the XNET Database property node to set or modify an XNET Database I/O name.

XNET Database

Reads and writes properties for an XNET Database I/O name.

Use the XNET Database property node to set or modify an XNET Database I/O name.

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-cluster-5050001.html language=enus -->
## TOPIC 00013: Cluster

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-cluster-5050001.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-cluster-5050001.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the I/O name of the parent cluster to which the ECU is connected. The parent cluster is determined when the ECU object is created. You cannot change it afterward.

Cluster

Provides the I/O name of the parent cluster to which the ECU is
 connected.

The parent cluster is determined when the ECU object is created. You cannot change it
 afterward.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-comment-3050005.html language=enus -->
## TOPIC 00014: Comment

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-comment-3050005.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-comment-3050005.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Comment describing the ECU object. A comment is a string containing up to 65535 characters.

Comment

Comment describing the ECU object. A comment is a string containing up to 65535
 characters.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-flexray-coldstart-2050010.html language=enus -->
## TOPIC 00015: FlexRay.Coldstart?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-flexray-coldstart-2050010.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-flexray-coldstart-2050010.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates that the ECU transmits a startup frame. This property is valid only for ECUs connected to a FlexRay bus. It returns True when one of the frames in this ECU's Frames Transmitted property has the XNET Frame FlexRay:Startup? property set to True. You can determine the frame transmitting the s

FlexRay.Coldstart?

Indicates that the ECU transmits a startup frame.

This property is valid only for ECUs connected to a FlexRay bus. It returns True when one
 of the frames in this ECU's Frames Transmitted property has the XNET Frame
 FlexRay:Startup? property set to True.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read

You can determine the frame transmitting the startup using the FlexRay:Startup
 Frame property. An ECU can send only one startup frame on the FlexRay bus.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-frames-received-6050003.html language=enus -->
## TOPIC 00016: FrmsRx

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-frames-received-6050003.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-frames-received-6050003.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of I/O names of frames the ECU receives. This property defines all frames the ECU receives. All frames an ECU receives in a given cluster must be defined in the same cluster.

FrmsRx

Returns an array of I/O names of frames the ECU receives.

This property defines all frames the ECU receives. All frames an ECU receives in a given
 cluster must be defined in the same cluster.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-frames-transmitted-6050004.html language=enus -->
## TOPIC 00017: FrmsTx

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-frames-transmitted-6050004.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-frames-transmitted-6050004.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of I/O names of frames the ECU transmits. This property defines all frames the ECU transmits. All frames an ECU transmits in a given cluster must be defined in the same cluster.

FrmsTx

Returns an array of I/O names of frames the ECU transmits.

This property defines all frames the ECU transmits. All frames an ECU transmits in a
 given cluster must be defined in the same cluster.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-j1939-node-name-9050029.html language=enus -->
## TOPIC 00018: J1939.NodeName

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-j1939-node-name-9050029.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-j1939-node-name-9050029.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the SAE J1939 node name to be used when simulating this ECU. This property is a 64-bit, unique identifier for this ECU. If you assign this ECU to an XNET session (SAE J1939:ECU property), XNET will start address claiming for this address using this node name and the property.

J1939.NodeName

Specifies the SAE J1939 node name to be used when simulating this ECU.

This property is a 64-bit, unique identifier for this ECU. If you assign this ECU to an
 XNET session (SAE
 J1939:ECU property), XNET will start address claiming for this address using
 this node name and the property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-j1939-preferred-address-50028.html language=enus -->
## TOPIC 00019: J1939.PreferredAddress

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-j1939-preferred-address-50028.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-j1939-preferred-address-50028.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the preferred SAE J1939 node address to be used when simulating this ECU. If you assign this ECU to an XNET session (SAE J1939:ECU property), XNET will start address claiming for this address using the ECU:Node Name property and use the address for the session when the address is granted.

J1939.PreferredAddress

Specifies the preferred SAE J1939 node address to be used when simulating this
 ECU.

If you assign this ECU to an XNET session (SAE J1939:ECU
 property), XNET will start address claiming for this address using the
 ECU:Node Name property and use the address for the session
 when the address is granted.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-lin-configured-nad-50023.html language=enus -->
## TOPIC 00020: LIN.ConfigNAD

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-lin-configured-nad-50023.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-lin-configured-nad-50023.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configured node address (NAD) of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services. Initial NAD is replaced by Configured NAD with node configuration services. This property must be defined before reading, either by writing to the property or by importing from a

LIN.ConfigNAD

Configured node address (NAD) of a LIN slave node.

NAD is the address of a slave node and is used in diagnostic services. Initial
 NAD is replaced byConfigured NAD with node
 configuration services. This property must be defined before reading, either by writing
 to the property or by importing from an LDF.

Caution

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-lin-dfunction-id-50025.html language=enus -->
## TOPIC 00021: LIN.FunctionID

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-lin-dfunction-id-50025.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-lin-dfunction-id-50025.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: A 16-bit value identifying the function of the LIN node (ECU). This property must be defined before reading, either by writing to the property or by importing from an LDF. This property is not saved in the FIBEX database. You can import it only from an LDF file.

LIN.FunctionID

A 16-bit value identifying the function of the LIN node (ECU).

This property must be defined before reading, either by writing to the property or by
 importing from an LDF.

Caution

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-lin-initial-nad-50022.html language=enus -->
## TOPIC 00022: LIN.InitialNAD

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-lin-initial-nad-50022.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-lin-initial-nad-50022.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Initial node address (NAD) of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services. Initial NAD is replaced by Configured NAD with node configuration services. This property must be defined before reading, either by writing to the property or by importing from an L

LIN.InitialNAD

Initial node address (NAD) of a LIN slave node.

NAD is the address of a slave node and is used in diagnostic services. Initial
 NAD is replaced by Configured NAD with node
 configuration services. This property must be defined before reading, either by writing
 to the property or by importing from an LDF.

Caution

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-lin-master-2050020.html language=enus -->
## TOPIC 00023: LIN.Master?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-lin-master-2050020.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-lin-master-2050020.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines whether the ECU is a LIN master (True) or slave (False). The default value is False.

LIN.Master?

Determines whether the ECU is a LIN master (True) or slave (False).

The default value is False.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu-lin-stmin-1050027.html language=enus -->
## TOPIC 00024: LIN.STmin

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu-lin-stmin-1050027.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu-lin-stmin-1050027.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Minimum time in seconds the node requires to prepare for the next frame of the diagnostic service. This property must be defined before reading, either by writing to the property or by importing from an LDF. This property is not saved in the FIBEX database. You can import it only from an LDF file.

LIN.STmin

Minimum time in seconds the node requires to prepare for the next frame of the
 diagnostic service.

This property must be defined before reading, either by writing to the property or by
 importing from an LDF.

Caution

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET ECU](xnet-ecu.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET ECU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-ecu.html language=enus -->
## TOPIC 00025: XNET ECU Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-ecu.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET ECU I/O name. Use the XNET ECU property node to change the configuration of an electronic control unit (ECU).

XNET ECU

Reads and writes properties for an XNET ECU I/O name.

Use the XNET ECU property node to change the configuration of an electronic control unit
 (ECU).

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-cluster-5060005.html language=enus -->
## TOPIC 00026: Cluster

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-cluster-5060005.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-cluster-5060005.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the I/O name to the parent cluster in which the schedule has been created. You cannot change the parent cluster after creating the schedule object.

Cluster

Returns the I/O name to the parent cluster in which the schedule has been created.
 You cannot change the parent cluster after creating the schedule object.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule](xnet-lin-schedule.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-comment-3060006.html language=enus -->
## TOPIC 00027: Comment

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-comment-3060006.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-comment-3060006.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Comment describing the schedule object. A comment is a string containing up to 65535 characters.

Comment

Comment describing the schedule object. A comment is a string containing up to 65535
 characters.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule](xnet-lin-schedule.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entries-6060001.html language=enus -->
## TOPIC 00028: Entries

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entries-6060001.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entries-6060001.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Array of entries for this LIN schedule. Each entry's position in this array specifies the position in the schedule. The database file and/or the order that you create entries at runtime determine the position.

Entries

Array of entries for this LIN schedule.

Each entry's position in this array specifies the position in the schedule. The database
 file and/or the order that you create entries at runtime determine the position.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule](xnet-lin-schedule.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entry-delay-1070002.html language=enus -->
## TOPIC 00029: Delay

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entry-delay-1070002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entry-delay-1070002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Time from the start of this entry (slot) to the start of the next entry. This property uses a double value in seconds, with the fractional part used for milliseconds or microseconds.

Delay

Time from the start of this entry (slot) to the start of the next entry.

This property uses a double value in seconds, with the fractional part used for
 milliseconds or microseconds.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule Entry](xnet-lin-schedule-entry.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule Entry

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entry-name-3070006.html language=enus -->
## TOPIC 00030: NameShort

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entry-name-3070006.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entry-name-3070006.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Short name (string) identifying the LIN schedule entry. The I/O name (long name) contains qualifiers, such as database name, to ensure that it is unique. If you write this property, it changes both short and long name. The short name is limited to 128 characters. A schedule entry name must be unique

NameShort

Short name (string) identifying the LIN schedule entry.

The I/O name (long name) contains qualifiers, such as database name, to ensure that it is
 unique. If you write this property, it changes both short and long name.

The short name is limited to 128 characters. A schedule entry name must be unique for all
 entries in the same schedule.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule Entry](xnet-lin-schedule-entry.html)

**Permissions:** Read/Write

Lowercase letters (a–z), uppercase letters (A–Z), numbers, and the underscore (_)
 are valid characters for the short name. The space ( ), period (.), and other
 special characters are not supported within the name. The short name must begin
 with a letter (uppercase or lowercase) or underscore, and not a number.

You can write this property to change the schedule entry’s short name. When you
 do this and then use the original XNET LIN schedule entry that contains the old
 name, errors can result because the old name cannot be found. Follow these steps
 to avoid this problem:

1. Get the old Name (Short) property using the property
 node.
2. Set the new Name (Short) property for the object.
3. Wire the XNET LIN schedule entry as the input string to the LabVIEW
 Search and Replace String VI with the old
 Name as the search string and the new Name as the replace string. This
 replaces the short name in the XNET LIN schedule entry, while retaining the
 other text that ensures a unique name.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule Entry

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entry-node-config-data-bytes-a070009.html language=enus -->
## TOPIC 00031: NodeConfFFDataBytes

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entry-node-config-data-bytes-a070009.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entry-node-config-data-bytes-a070009.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Array of 8 bytes containing raw data for LIN node configuration. The node configuration service is executed only if the schedule entry Type is set to Node configuration. This property is not saved to the FIBEX file. If you write this property, save the database, and reopen it, the node configuration

NodeConfFFDataBytes

Array of 8 bytes containing raw data for LIN node configuration.

The node configuration service is executed only if the schedule entry Type is set to
 Node configuration.

Caution

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule Entry](xnet-lin-schedule-entry.html)

**Permissions:** Read/Write

Node configuration defines a set of services used to configure slave nodes in the
 cluster.

Each service has a specific set of parameters coded in this byte array. In the
 LDF file, those parameters are stored, for example, in the node (ECU) or the
 frame object. NI-XNET LDF reader composes those parameters to the byte values
 like they are sent on the bus.

The LIN specification document describes node configuration services and the
 mapping of parameters to raw format bytes.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule Entry

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entry-schedule-5070007.html language=enus -->
## TOPIC 00032: Schedule

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entry-schedule-5070007.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entry-schedule-5070007.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: LIN schedule that uses this entry. The LIN schedule is considered the parent of this entry. You define the parent schedule when you create the entry object. You cannot change it afterward.

Schedule

LIN schedule that uses this entry.

The LIN schedule is considered the parent of this entry. You define the parent schedule
 when you create the entry object. You cannot change it afterward.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule Entry](xnet-lin-schedule-entry.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule Entry

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-entry.html language=enus -->
## TOPIC 00033: XNET LIN Schedule Entry Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-entry.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-entry.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET LIN Schedule Entry I/O name. Use the XNET LIN Schedule Entry property node to set or modify properties for an XNET LIN Schedule Entry I/O name.

XNET LIN Schedule Entry

Reads and writes properties for an XNET LIN Schedule Entry I/O name.

Use the XNET LIN Schedule Entry property node to set or modify properties for an XNET LIN
 Schedule Entry I/O name.

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-name-3060002.html language=enus -->
## TOPIC 00034: NameShort

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-name-3060002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-name-3060002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Short name (string) identifying the XNET LIN schedule object. The short name is limited to 128 characters. A schedule name must be unique for all schedules in a cluster. Lowercase letters (a–z), uppercase letters (A–Z), numbers, and the underscore (_) are valid characters for the short name. The spa

NameShort

Short name (string) identifying the XNET LIN schedule object.

The short name is limited to 128 characters. A schedule name must be unique for all
 schedules in a cluster.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule](xnet-lin-schedule.html)

**Permissions:** Read/Write

Lowercase letters (a–z), uppercase letters (A–Z), numbers, and the underscore (_)
 are valid characters for the short name. The space ( ), period (.), and other
 special characters are not supported within the name. The short name must begin
 with a letter (uppercase or lowercase) or underscore, and not a number.

You can write this property to change the schedule’s short name. When you do this
 and then use the original XNET LIN schedule that contains the old name, errors
 can result because the old name cannot be found. Follow these steps to avoid
 this problem:

1. Get the old Name (Short) property using the property node.
2. Set the new Name (Short) property for the object.
3. Wire the XNET LIN schedule as the input string to the LabVIEW Search and
 Replace String VI with the old Name as the search string
 and the new Name as the replace string. This replaces the short name in the
 XNET LIN schedule, while retaining the other text that ensures a unique
 name.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-run-mode-60004.html language=enus -->
## TOPIC 00035: RunMode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-run-mode-60004.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-run-mode-60004.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies how the master runs this schedule: Continuous (0), Once (1), or Null (2). Usually, the default value for the run mode is Continuous. If the schedule is configured to be a collision resolving table for an event-triggered entry, the default is Once. This property is a ring (enumerated list)

RunMode

Specifies how the master runs this schedule: Continuous (0),
 Once (1), or Null (2).

Usually, the default value for the run mode is Continuous. If the
 schedule is configured to be a collision resolving table for an event-triggered entry,
 the default is Once.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule](xnet-lin-schedule.html)

**Permissions:** Read/Write

This property is a ring (enumerated list) with the following values:

| String | Value | Description |
| --- | --- | --- |
| Continuous | 0 | The master runs the schedule continuously. When the last entry executes, the schedule starts again with the first entry. |
| Once | 1 | The master runs the schedule once (all entries), then returns to the previously running continuous schedule (or null). If requests are submitted for multiple run-once schedules, each run-once executes in succession based on its Priority, then the master returns to the continuous schedule (or null). |
| Null | 2 | All communication stops immediately. A schedule with this run mode is called a null schedule. |

This property is not read from the database, but is handled like a database
 property. After opening the database, the default value is returned, and you can
 change the property. But similar to database properties, you cannot change it
 after a session is created.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-lin-schedule-type-70005.html language=enus -->
## TOPIC 00036: Type

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-lin-schedule-type-70005.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-lin-schedule-type-70005.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines the mechanism used to transfer frames in this schedule entry (slot). The default value is Unconditional (0). The values (enumeration) for this property are: Enumeration Value Description Unconditional 0 A single frame transfers in this entry (slot). Sporadic 1 The master transmits in this

Type

Determines the mechanism used to transfer frames in this schedule entry
 (slot).

The default value is Unconditional (0).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET LIN Schedule Entry](xnet-lin-schedule-entry.html)

**Permissions:** Read/Write

The values (enumeration) for this property are:

| Enumeration | Value | Description |
| --- | --- | --- |
| Unconditional | 0 | A single frame transfers in this entry (slot). |
| Sporadic | 1 | The master transmits in this slot. The master selects among multiple frames to transmit. Only updated frames are transmitted. When multiple frames have been updated, the master decides by priority; the other updated frames remain pending and can be sent when this schedule entry executes again. Order of frames in the Frames property determines frame priority. |
| Event-triggered | 2 | Multiple slaves can transmit a frame in this slot. When a collision occurs, this is detected and resolved using a schedule specified in the Collision Resolving Schedule property. |
| Node configuration | 3 | Schedule entry contains a node configuration service. The node configuration service is defined as raw data bytes in the Node Configuration:Free Format:Data Bytes property. |

A LIN frame can exist in multiple schedules and multiple schedule entries. For
 example, if a frame exists in an Event-triggered entry in schedule A, it also
 exists in an Unconditional entry of a different schedule B, so that
 Event-triggered collisions in schedule A can be resolved by switching to
 schedule B.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET LIN Schedule Entry

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-pdu-cluster-5080004.html language=enus -->
## TOPIC 00037: Cluster

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-pdu-cluster-5080004.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-pdu-cluster-5080004.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Cluster that contains the PDU (XNET Cluster I/O Name). You cannot change the parent cluster after creating the PDU object.

Cluster

Cluster that contains the PDU (XNET Cluster I/O Name).

You cannot change the parent cluster after creating the PDU object.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET PDU](xnet-pdu.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET PDU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-pdu-data-multiplexed-2080008.html language=enus -->
## TOPIC 00038: Mux.IsMuxed?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-pdu-data-multiplexed-2080008.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-pdu-data-multiplexed-2080008.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates (True/False) whether this PDU is data multiplexed. The default value is False. This property returns True if the PDU contains a multiplexer signal. PDUs containing a multiplexer contain subframes that allow using bits of the payload for different information (signals), depending on the Mul

Mux.IsMuxed?

Indicates (True/False) whether this PDU is data multiplexed.

The default value is False. This property returns True if the PDU contains a multiplexer
 signal.

PDUs containing a multiplexer contain subframes that allow using bits of the payload for
 different information (signals), depending on the Multiplexer
 Value.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET PDU](xnet-pdu.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET PDU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-pdu-mux-static-signals-608000a.html language=enus -->
## TOPIC 00039: Mux.StatSigs

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-pdu-mux-static-signals-608000a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-pdu-mux-static-signals-608000a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of static signals contained in the multiplexed PDU (array of XNET Signal I/O Name). Static signals are contained in every PDU transmitted, as opposed to dynamic signals, which are transmitted depending on the multiplexer value. You can create static signals by specifying the PDU as

Mux.StatSigs

Returns an array of static signals contained in the multiplexed PDU (array of XNET
 Signal I/O Name).

Static signals are contained in every PDU transmitted, as opposed to *dynamic
 signals*, which are transmitted depending on the multiplexer value.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET PDU](xnet-pdu.html)

**Permissions:** Read

You can create static signals by specifying the PDU as the parent object. You can
 create dynamic signals by specifying a subframe as the parent.

If the PDU is not multiplexed, this property returns the same array as the XNET
 PDU Signals property

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET PDU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-pdu-payload-length-80003.html language=enus -->
## TOPIC 00040: PayldLen

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-pdu-payload-length-80003.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-pdu-payload-length-80003.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of bytes of data in the PDU's payload. This number can be less than the payload length of mapped frames. This property is required. If the property does not contain a valid value, and you create an XNET session that uses this PDU, the session returns an error. To ensure that the property cont

PayldLen

Number of bytes of data in the PDU's payload.

This number can be less than the payload length of mapped frames.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET PDU](xnet-pdu.html)

**Permissions:** Read/Write

This property is required. If the property does not contain a valid value, and
 you create an XNET session that uses this PDU, the session returns an error. To
 ensure that the property contains a valid value, you can do one of the
 following:

- Use a database file (or alias) to create the session. The file formats
 require a valid value in the text for this property.
- Set a value in LabVIEW using the property node. This is required when you
 create your own in-memory database (:memory:) rather than using a file. The
 property does not contain a default in this case, so you must set a valid
 value prior to creating a session.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET PDU

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-pdu.html language=enus -->
## TOPIC 00041: XNET PDU Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-pdu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-pdu.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET PDU I/O name. Use the XNET PDU property node to change the configuration of the protocol data unit (PDU).

XNET PDU

Reads and writes properties for an XNET PDU I/O name.

Use the XNET PDU property node to change the configuration of the protocol data unit
 (PDU).

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-applprotocol-100091.html language=enus -->
## TOPIC 00042: Application Protocol

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-applprotocol-100091.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-applprotocol-100091.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the application protocol that the session uses. The database used with the XNET Create Session VI determines the application protocol. 0 None 1 J1939

Application
 Protocol

Returns the application protocol that the session uses.

The database used with the XNET Create Session VI determines the application protocol.

| 0 | None |
| --- | --- |
| 1 | J1939 |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-cluster-310000a.html language=enus -->
## TOPIC 00043: Cluster

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-cluster-310000a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-cluster-310000a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the cluster (network) used with XNET Create Session. Use this property on the block diagram as follows: As a refnum wired to a property node to access information for the cluster and its objects (frames, signals, and so on). As a string containing the cluster name. This name typically is the

Cluster

Returns the cluster (network) used with XNET Create Session.

Use this property on the block diagram as follows:

- As a refnum wired to a property node to access information for the cluster and its
 objects (frames, signals, and so on).
- As a string containing the cluster name. This name typically is the database alias
 followed by the cluster name.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-database-3100002.html language=enus -->
## TOPIC 00044: Database

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-database-3100002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-database-3100002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: This property returns the database used with the XNET Create Session. Use this property on the block diagram as follows: As a refnum wired to a property node to access information for the database and its objects (frames, signals, and so on). As a string containing the database name. This is the nam

Database

This property returns the database used with the XNET Create Session.

Use this property on the block diagram as follows:

- As a refnum wired to a property node to access information for the database and its
 objects (frames, signals, and so on).
- As a string containing the database name. This is the name of the database alias or
 in-memory database. If the database was opened using a file path that does not
 correlate to an assigned alias, a unique identifier based on file name and content
 is returned.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-ethernet-filtering-frame-filter.html language=enus -->
## TOPIC 00045: Frame Filter

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-ethernet-filtering-frame-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-ethernet-filtering-frame-filter.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Pcap Filter: Sets the filter string to be applied on packets received on this stream. The format uses industry-standard packet filter syntax.

Frame Filter

Pcap Filter: Sets the filter string to be applied on packets received on this stream.
 The format uses industry-standard packet filter syntax.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-ethernet-logging-mode-1000b9.html language=enus -->
## TOPIC 00046: Ethernet:Logging:Mode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-ethernet-logging-mode-1000b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-ethernet-logging-mode-1000b9.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables or disables logging. The value is Off by default; to enable logging, you must write this property to the log. The Ethernet:Logging:Mode property uses a ring (enumerated list) with the following values: String Value Description Off 0 Disable logging for the session. Log 1 Enable logging for t

Ethernet:Logging:Mode

Enables or disables logging.

The value is Off by default; to enable logging, you must write this property to the log.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

The **Ethernet:Logging:Mode** property uses a ring
 (enumerated list) with the following values:

| String | Value | Description |
| --- | --- | --- |
| Off | 0 | Disable logging for the session. |
| Log | 1 | Enable logging for the session. You cannot read data using XNET Read when using this mode. If you require access to the data, read from the log file. |

When logging is enabled, you must use the Filepath
 property to specify a valid path for the log file.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-ethernet-logging-op-1000bb.html language=enus -->
## TOPIC 00047: Ethernet:Logging:Operation

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-ethernet-logging-op-1000bb.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-ethernet-logging-op-1000bb.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the operation used to create the log file. This property uses a ring (enumerated list) with the following values: Enumeration Value Description Create or Replace 0 Create a new log file, or replace an existing log file. Create 1 Create a new log file. If the file already exists, XNET retur

Ethernet:Logging:Operation

Specifies the operation used to create the log file.

This property uses a ring (enumerated list) with the following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| Create or Replace | 0 | Create a new log file, or replace an existing log file. |
| Create | 1 | Create a new log file. If the file already exists, XNET returns an error. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-active-0x0310ffff.html language=enus -->
## TOPIC 00048: Frame:Active

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-active-0x0310ffff.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-active-0x0310ffff.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides access to properties for a specific frame running within the session. Writing this property sets the active frame for subsequent properties in the Frame category. The Active Frame property only applies to other properties in the same property node. The string syntax supports the following o

Frame:Active

Provides access to properties for a specific frame running within the session.
 Writing this property sets the active frame for subsequent properties in the Frame
 category.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

The string syntax supports the following options:

- Decimal number: This is interpreted as the index of the signal or frame in
 the session's list. If the session is signal I/O, subsequent frame
 properties change the signal's parent frame.
- XNET Frame: If the session is frame I/O, you can wire a frame name from the
 session's List of Frames property.
- XNET Signal: If the session is signal I/O, you can wire a signal name from
 the session's List of Signals property. Subsequent frame properties change
 the signal's parent frame.

If the session is Frame Stream Input or Frame Stream Output, this property has no
 effect, because stream I/O sessions do not use specific frames.

The default value of this property is 0, the first frame or signal in the
 session's list. If the empty string is wired to this property, this is converted
 to 0 internally.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-can-transmit-time-1100082.html language=enus -->
## TOPIC 00049: Frame:CAN:Transmit Time

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-can-transmit-time-1100082.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-can-transmit-time-1100082.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the amount of time that must elapse between subsequent transmissions of a cyclic frame. The default value of this property comes from the database (the XNET Frame CAN:Transmit Time property). If you set this property while a frame object is currently started, the frame object is stopped, t

Frame:CAN:Transmit
 Time

Specifies the amount of time that must elapse between subsequent transmissions of a
 cyclic frame.

The default value of this property comes from the database (the XNET Frame CAN:Transmit
 Time property).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

If you set this property while a frame object is currently started, the frame
 object is stopped, the cyclic rate updated, and then the frame object is
 restarted. Because of the stopping and starting, the frame's start time offset
 is re-evaluated.

Note

Frame:Active

Note

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-lin-transmit-n-corrupted-checksums-100085.html language=enus -->
## TOPIC 00050: Frame:LIN:Transmit N Corrupted Checksums

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-lin-transmit-n-corrupted-checksums-100085.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-lin-transmit-n-corrupted-checksums-100085.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: When set to a nonzero value, this property causes the next N number of checksums to be corrupted. The checksum is corrupted by negating the value calculated per the database; (EnhancedValue * -1) or (ClassicValue * -1). This property is valid only for output sessions. If the frame is transmitted in

Frame:LIN:Transmit N Corrupted
 Checksums

When set to a nonzero value, this property causes the next N number of checksums to
 be corrupted.

The checksum is corrupted by negating the value calculated per the database;
 (EnhancedValue * -1) or(ClassicValue * -1). This
 property is valid only for output sessions. If the frame is transmitted in an
 unconditional or sporadic schedule slot, N is always decremented for each frame
 transmission. If the frame is transmitted in an event-triggered slot and a collision
 occurs, N is not decremented. In that case, N is decremented only when the collision
 resolving schedule is executed and the frame is successfully transmitted. If the frame
 is the only one to transmit in the event-triggered slot (no collision), N is decremented
 at event-triggered slot time.

This property is useful for testing ECU behavior when a corrupted checksum is
 transmitted.

Note

Frame:Active

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-output-queue-update-frequency-100084.html language=enus -->
## TOPIC 00051: Frame:Output Queue Update Frequency

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-output-queue-update-frequency-100084.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-output-queue-update-frequency-100084.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines how often the NI-XNET firmware notifies the driver of frames being consumed from the output queue. Note that this property should usually not be changed; it is provided for advanced users. The value is given in 6-byte packets. The maximum value is 0xFFFF bytes, which results in 10922 6-by

Frame:Output Queue Update
 Frequency

Determines how often the NI-XNET firmware notifies the driver of frames being
 consumed from the output queue.

Note that this property should usually not be changed; it is provided for advanced
 users.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

The value is given in 6-byte packets. The maximum value is 0xFFFF bytes, which
 results in 10922 6-byte packets. Setting the property to 0 will use the
 internally defined update frequency.

The default value is 0, which means the update frequency is an internally
 selected rate that depends on the queue size. Very large queues can cause
 updates to be delayed. This property can be used to make the updates more
 frequently.

Note

Frame:Active

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-sae-j1939-address-filter-3100086.html language=enus -->
## TOPIC 00052: Frame:SAE J1939:Address Filter

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-sae-j1939-address-filter-3100086.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-sae-j1939-address-filter-3100086.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Defines a filter for the source address of the PGN transmitting node. You can use this property when multiple nodes with different addresses are transmitting the same PGN. This property can be used only in input sessions. If the filter is active, the session accepts only frames transmitted by a node

Frame:SAE J1939:Address
 Filter

Defines a filter for the source address of the PGN transmitting node. You can use
 this property when multiple nodes with different addresses are transmitting the same
 PGN. This property can be used only in input sessions.

If the filter is active, the session accepts only frames transmitted by a node with the
 defined address. All other frames with the same PGN but transmitted by other nodes are
 ignored.

The value is a string representing the decimal value of the address. Use the
 Number to Decimal String node if your address is given as
 a number. To reset the filter, set the value to empty string (default).

Note

Frame:Active

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-frame-skipncyclic-100083.html language=enus -->
## TOPIC 00053: Frm.SkipNCyclic

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-frame-skipncyclic-100083.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-frame-skipncyclic-100083.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: When set to a nonzero value N, this property causes the next N cyclic frames to be skipped. Note that only CAN interfaces currently support this property. When the frame's transmission time arrives and the skip count is nonzero, a frame value is dequeued (if this is not a single-point session), and

Frm.SkipNCyclic

When set to a nonzero value N, this property causes the next N cyclic frames to be
 skipped.

Note that only CAN interfaces currently support this property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

When the frame's transmission time arrives and the skip count is nonzero, a frame
 value is dequeued (if this is not a single-point session), and the skip count is
 decremented, but the frame actually is not transmitted across the bus. When the
 skip count decrements to 0, subsequent cyclic transmissions resume. This
 property is valid only for output sessions and frames with cyclic timing (that
 is, not event-based frames).

This property is useful for testing of ECU behavior when a cyclic frame is
 expected, but is missing for N cycles.

Note

Frame:Active

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-baudrate-9100016.html language=enus -->
## TOPIC 00054: Intf.BaudRate64

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-baudrate-9100016.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-baudrate-9100016.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Sets the CAN, FlexRay, or LIN interface baud rate. The default value for this interface property is the same as the cluster's baud rate in the database. You can modify this property only when the interface is stopped. Your application can set this interface baud rate to override the value in the dat

Intf.BaudRate64

Sets the CAN, FlexRay, or LIN interface baud rate. The default value for this
 interface property is the same as the cluster's baud rate in the database.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Your application can set this interface baud rate to override the value in the
 database, or when no database is used.

Note

#### CAN

When the upper nibble (0xF0000000) is clear, this is a numeric baud rate (for
 example, 500000).

NI-XNET CAN hardware currently accepts the following numeric baud rates: 33333,
 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000,
 400000, 500000, 800000, and 1000000.

Note

Note

When the upper nibble of the lower 32 bit is set to 0xA (that is, 0xA0000000),
 the remaining bits provide fields for more custom CAN communication baud rate
 programming. The fields are shown in the following tables:

|  | 63..32 | 31..28 | 27..0 |
| --- | --- | --- | --- |
| Normal | Res | b0000 | Baud Rate (33.3 k–1 M) |

|  | 63..46 | 45..32 | 31..28 | 27..23 | 22..16 | 15..8 | 7 | 6..0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom 64-bit | Res | Tq | b1010 | Res | NSJW | NTSEG1 | Res | NTSEG2 |

*Time quantum (Tq)* is used to program the baud rate prescaler. Valid
 values are 25–12800, in increments of 0x19 (25 decimal). Time quantum is defined
 in *ISO 11898-1, 12.4.1 Bit Encoding/Decoding*.

*Nominal (Re-)Synchronization Jump Width (NSJW)*. Valid values are
 0–127. The actual hardware interpretation of this value is one more than the
 programmed value.

*Nominal Time Segment 1 (NTSEG1)* is the time segment before the
 sample point. Valid values are 1–0xFF (1–255 decimal). The actual hardware
 interpretation of this value is one more than the programmed value. NTSEG1 is
 described in Bosch's *M_CAN Controller Area Network User’s Manual*,
 Revision 3.2.1.

*Nominal Time Segment 2 (NTSEG2)* is the time segment after the sample
 point. The actual hardware interpretation of this value is one more than the
 programmed value. NTSEG2 is described in Bosch's *M_CAN Controller Area
 Network User’s Manual*, Revision 3.2.1.

#### 32-bit baud rate property

The following information is valid for the former 32-bit Baud
 Rate property that was replaced by the 64bit property. You still
 can use the baud rate values used with the 32-bit property.

When the upper nibble is set to 0x8 (that is, 0x80000000), the remaining bits
 provide fields for more custom CAN communication baud rate programming.
 Additionally, if the upper nibble is set to 0xC (that is, 0xC0000000), the
 remaining bits provide fields for higher-precision custom CAN communication baud
 rate programming. The higher-precision bit timings facilitate connectivity to a
 CAN FD cluster.

|  | 31..28 | 27..26 | 25..24 | 23 | 22..20 | 19..16 | 15..14 | 13..12 | 11..8 | 7..4 | 3..0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom | b1000 | Res | SJW (0–3) | TSEG2 (0–7) | TSEG1 (1–15) | Res | Tq (125–0x3200) |  |  |  |  |
| High Precision | b1100 | SJW (0–15) | TSEG2 (0–15) | TSEG1 (1–63) | Tq (25–0x3200) |  |  |  |  |  |  |

*(Re-)Synchronization Jump Width (SJW)*. Valid programmed values are
 0–3 in normal custom mode and 0–15 in high-precision custom mode. The actual
 hardware interpretation of this value is one more than the programmed value.

*Time Segment 2 (TSEG2)* is the time segment after the sample point.
 Valid programmed values are 0–7 in normal custom mode and 0–15 in high-precision
 custom mode. TSEG2 is the Phase_Seg2 time described in *ISO 11898-1, 12.4.1
 Bit Encoding/Decoding*. The actual hardware interpretation of this
 value is one more than the programmed value.

*Time Segment 1 (TSEG1)* is the time segment before the sample point.
 Valid programmed values are 1–0xF (1–15 decimal) in normal custom mode and
 1–0x3F (1–63 decimal) in high-precision custom mode. TSEG1 is the combination of
 the Prop_Seg and Phase_Seg1 time described in ISO 11898-1, 12.4.1 Bit
 Encoding/Decoding. The actual hardware interpretation of this value is one more
 than the programmed value.

*Time quantum (Tq)* is used to program the baud rate prescaler. Valid
 programmed values are 125–12800, in increments of 0x7D (125 decimal) ns for
 normal custom mode and 25–12800, in increments of 0x19 (25 decimal) ns for
 high-precision custom mode. Time quantum is defined in *ISO 11898-1, 12.4.1
 Bit Encoding/Decoding*.

An advanced baud rate example is 0x8014007D. This example breaks down into the
 following values:

- SJW = 0x0 (0x01 in hardware, due to the + 1)
- TSEG2 = 0x1 (0x02 in hardware, due to the + 1)
- TSEG1 = 0x4 (0x05 in hardware, due to the + 1)
- Tq = 0x7D (125 ns in hardware)

Each time quanta is 125 ns. From IS0 11898–1, 12.4.1.2 Programming of Bit Time,
 the nominal time segments length is Sync_Seg (Fixed at 1) + (Prop_Seg +
 Phase_Seg1)(B) + Phase_Seg2(C) = 1 + 2 + 5 = 8. So, the total time for a bit in
 this example is 8 * 125 ns = 1000 ns = 1 µs. A 1 µs bit time is equivalent to a
 1 MHz baud rate.

#### Formulas

Baud rate = (Total Ticks per Sec / Ticks for 1 bit ) = (Oscillator
 Frequency[Hz] * Tq[Ticks]) / 25) /
 (Sync_Seg[Ticks] + TSEG1[Ticks] +
 TSEG2[Ticks])

Note

Sample Point = (TSEG1 + Sync_Seg) /
 (TSEG1 + Sync_Seg +
 TSEG2)

#### LIN

When the upper nibble (0xF0000000) is clear, you can set only baud rates within
 the LIN-specified range (2400 to 20000) for the interface.

When the upper nibble is set to 0x8 (0x80000000), no check for baud rate within
 LIN-specified range is performed, and the lowest 16 bits of the value may
 contain the custom baud rate.

Any custom value higher than 65535 is masked to a 16-bit value. As with the
 non-custom values, the interface internally calculates the appropriate divisor
 values to program into its UART. Because the interface uses the Atmel ATA6620
 LIN transceiver, which is guaranteed to operate within the LIN 2.0 specification
 limits, there are some special considerations when programming custom baud rates
 for LIN:

- The ATA6620 transceiver incorporates a TX-dominant timeout function to
 prevent a faulty device that it is built into from holding the LIN dominant
 indefinitely. If the TX line into the transceiver is held in the dominant
 state for too long, the transceiver switches its driver to the recessive
 state. This places a limit on the length of the LIN header break field that
 the interface transmits, therefore limiting the lowest baud rate you can
 set. At the point the baud rate or break length is set for the interface, it
 uses the baud rate bit time and break length settings internally to
 calculate the resulting break duration and returns an error if that duration
 is long enough to trigger the TX dominant timeout.
- At the other end of the baud range, the ATA6620 is specified to work up to
 20000 baud. While you can use the custom bit to program rates higher than
 20000 baud, transceiver behavior when operating above that rate is not
 guaranteed.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-bus-error-to-input-stream-2100015.html language=enus -->
## TOPIC 00055: Intf.BusErrToInStrm?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-bus-error-to-input-stream-2100015.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-bus-error-to-input-stream-2100015.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the hardware to place a CAN or LIN bus error frame into the Stream Input queue after it is generated. A bus error frame is generated when the hardware detects a bus error. Only CAN and LIN interfaces currently support this property.

Intf.BusErrToInStrm?

Configures the hardware to place a CAN or LIN bus error frame into the Stream Input
 queue after it is generated.

A bus error frame is generated when the hardware detects a bus error.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-disable-protocol-exception-handling-21000a4.html language=enus -->
## TOPIC 00056: Intf.CAN.DisProtExcHdlng

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-disable-protocol-exception-handling-21000a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-disable-protocol-exception-handling-21000a4.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether default protocol exception handling is disabled and the CAN hardware transmits an error frame instead. A protocol exception occurs when CAN hardware detects an invalid combination of bits on the CAN bus reserved for a future protocol expansion. NI-XNET allows you to define how the

Intf.CAN.DisProtExcHdlng

Indicates whether default protocol exception handling is disabled and the CAN
 hardware transmits an error frame instead.

A protocol exception occurs when CAN hardware detects an invalid combination of bits on
 the CAN bus reserved for a future protocol expansion. NI-XNET allows you to define how
 the hardware should behave in case of a protocol exception.

| Value | Meaning | Description |
| --- | --- | --- |
| False | Property is enabled | CAN hardware stops receiving frames and starts a bus integration. |
| True | Property is disabled | CAN hardware transmits an error frame when it detects a protocol exception condition. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-enable-edge-filter-21000a2.html language=enus -->
## TOPIC 00057: Intf.CAN.EdgeFilter

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-enable-edge-filter-21000a2.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-enable-edge-filter-21000a2.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: When this property is enabled, the CAN hardware requires two consecutive dominant time quanta (tq) to detect an edge for hard synchronization.The default value for this property is False.

Intf.CAN.EdgeFilter

When this property is enabled, the CAN hardware requires two consecutive
 dominant time quanta (tq) to detect an edge for hard synchronization.The
 default value for this property is False.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-external-transceiver-config.html language=enus -->
## TOPIC 00058: Intf.CAN.ExtTcvrCfg

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-external-transceiver-config.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-external-transceiver-config.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables you to configure XS series CAN hardware to communicate properly with your external transceiver. The connector on your XS series CAN hardware has five lines for communicating with your transceiver. Line Direction Purpose Ext_RX In Data received from the CAN bus. Ext_TX Out Data to transmit on

Intf.CAN.ExtTcvrCfg

Enables you to configure XS series CAN hardware to communicate properly with your
 external transceiver.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

The connector on your XS series CAN hardware has five lines for communicating
 with your transceiver.

| Line | Direction | Purpose |
| --- | --- | --- |
| Ext_RX | In | Data received from the CAN bus. |
| Ext_TX | Out | Data to transmit on the CAN bus. |
| Output0 | Out | Generic output used to configure the transceiver mode. |
| Output1 | Out | Generic output used to configure the transceiver mode. |
| NERR | In | Input to connect to the nERR pin of your transceiver to route status back from the transceiver to the hardware. |

#### Transceiver Communication

Ext_RX and Ext_TX lines provide for the transfer of CAN data to and from the
 transceiver. The remaining three lines are for configuring the transceiver and
 retrieving status from the transceivers. Not all transceivers use all pins.
 Typically, a transceiver has one or two lines that can configure the transceiver
 mode. The NI-XNET driver natively supports five transceiver modes:

- Normal
- Sleep
- Single Wire Wakeup
- Single Wire High Speed
- Power-On

This property configures how the NI-XNET driver sets the outputs of your external
 transceiver for each mode. The configuration is in the form of a U32 written as
 a bitmask. The U32 bitmask is defined as follows.

| 31 | 30..15 | 14..12 | 11..9 | 8..6 | 5..3 | 2..0 |
| --- | --- | --- | --- | --- | --- | --- |
| nERR Connected | Reserved | PowerOn Configuration | SWHighSpeed Configuration | SWWakeup Configuration | Sleep Configuration | Normal Configuration |

Where each configuration is a 3-bit value defined as:

| 2 | 1 | 0 |
| --- | --- | --- |
| State Supported | Output1 Value | Output0 Value |

The Interface:CAN:Transceiver State property changes the transceiver state. Based
 on the transceiver configuration, if the state is supported, the configuration
 determines how the two pins are set. If the state is not supported, an error is
 returned, because you tried to set an invalid configuration. Note that all
 transceivers must support a Normal state, so the State Supported bit for that
 configuration is ignored.

Other internal state changes may occur. For example, if you put the transceiver
 to sleep and a remote wakeup occurs, the transceiver automatically is changed to
 the normal state.

If nERR Connected is set, the nERR pin into the connector determines a
 transceiver error. It is active low, meaning a value of 0 on this pin indicates
 an error. A value of 1 indicates no error. If this line is connected, the
 NI-XNET driver monitors this line and reports its status via the
 **transceiver error?** field of [NI-XNET Read
 (State CAN Comm)](/csh?topicname=xnet-read-state-can-comm.html).

#### Examples

*TJA1041 (HS)*: To connect to the TJA1041 transceiver, connect Output0
 to the nSTB pin and Output1 to the EN pin. The TJA1041 does have an nERR pin, so
 that should be connected to the nERR input. The TJA1041 supports a power-on
 state, a sleep state, and a normal state. As this is not a single wire
 transceiver, it does not support any single wire state. For normal operation,
 the TJA1041 uses a 1 for both nSTB and EN. For sleep, the TJA1041 uses the
 standby mode, which uses a 0 for both nSTB and EN. For power-on, the TJA1041
 uses a 1 for nSTB and a 0 for EN. The final configuration is 0x80005027.

*TJA1054 (LS)*: You can connect and configure the TJA1054 identically
 to the TJA1041.

*AU5790 (SW)*: To connect to the AU5790 transceiver, connect Output0
 to the nSTB pin and Output1 to the EN pin. The AU5790 does not support any
 transceiver status, so you do not need to connect the nERR pin. The AU5790
 supports all states. For normal operation, the AU5790 uses a 1 for both nSTB and
 EN. For sleep, the AU5790 uses a 0 for both nSTB and EN. For Single Wire Wakeup,
 the AU5790 requires nSTB to be a 0 and EN to be a 1. For Single Wire High-Speed,
 the AU5790 requires nSTB to be a 1, and EN to be a 0. For power-on, the sleep
 state is used so there is less interference on the bus. The final configuration
 is 0x00004DA7.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-fd-iso-mode-10003e.html language=enus -->
## TOPIC 00059: Intf.CAN.FdIsoMode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-fd-iso-mode-10003e.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-fd-iso-mode-10003e.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether the interface is working in the ISO CAN FD standard or non-ISO CAN FD standard. The default value for this property is ISO. This property is valid only when the interface is in CAN FD(+BRS) mode. It specifies whether the interface is working in the ISO CAN FD standard (ISO standard

Intf.CAN.FdIsoMode

Indicates whether the interface is working in the ISO CAN FD standard or non-ISO CAN
 FD standard.

The default value for this property is ISO.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

This property is valid only when the interface is in CAN FD(+BRS) mode. It
 specifies whether the interface is working in the ISO CAN FD standard (ISO
 standard 11898-1:2015) or non-ISO CAN FD standard (Bosch CAN FD 1.0
 specification).

Two ports using different standards (ISO CAN FD vs. non-ISO CAN FD) cannot
 communicate with each other.

When you use a CAN FD database (DBC or FIBEX file created with NI-XNET), you can
 specify the ISO CAN FD mode when creating an alias name for the database.

An alias is created automatically when you open a new database in the NI-XNET
 Database Editor. The specified ISO CAN FD mode is used as default, which you can
 change in the session using this property.

Note

Interface:CAN:Transmit I/O Mode

Note

Note

Interface:CAN:Transmit I/O Mode

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-fdbaudrate64-9100027.html language=enus -->
## TOPIC 00060: Intf.CAN.FdBaudRate64

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-fdbaudrate64-9100027.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-fdbaudrate64-9100027.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Sets the fast data baud rate for CAN FD+BRS CAN:I/O Mode. The default value for this interface property is the same as the cluster's FD baud rate in the database. You can modify this property only when the interface is stopped. Your application can set this property to override the value in the data

Intf.CAN.FdBaudRate64

Sets the fast data baud rate for CAN FD+BRS CAN:I/O Mode. The default value for this
 interface property is the same as the cluster's FD baud rate in the
 database.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Your application can set this property to override the value in the database.

Note

When the upper nibble (0xF0000000) is clear, this is a numeric baud rate (for
 example, 500000).

NI-XNET CAN hardware currently accepts the following numeric baud rates: 200000,
 250000, 400000, 500000, 800000, 1000000, 1250000, 1600000, 2000000, 2500000,
 4000000, 5000000, and 8000000.

Note

When the upper nibble of the lower 32 bit is set to 0xA (that is, 0xA0000000),
 the remaining bits provide fields for more custom CAN communication baud rate
 programming. The fields are shown in the following tables:

|  | 63..32 | 31..28 | 27..0 |
| --- | --- | --- | --- |
| Normal | Res | b0000 | Baud Rate (200 k–8 M) |

|  | 63..56 | 55 | 54..47 | 46..40 | 39 | 38..32 | 31..28 | 27 | 26..13 | 12..8 | 7..4 | 3..0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom 64-bit | Res | TDC | Res | TDCO | Res | TDCF | b1010 | Res | Tq | DTSEG1 | DTSEG2 | DSJW |

*Transmitter Delay Compensation (TDC)* enables or disables the TDC
 feature.

- 0: TDC is disabled.
- 1: TDC is enabled.

*Transmitter Delay Compensation Offset (TDCO)* defines the distance
 between the delay from transmit to receive point and secondary sample point.
 Valid values are 0–127.

*Transmitter Delay Compensation Filter Window Length (TDCF)* defines
 the minimum value for the secondary sample point position. It is enabled when
 TDCF is greater than TDCO. Valid values are 0–127.

*Time quantum (Tq)* is used to program the baud rate prescaler. Valid
 values are 25–800, in increments of 25 ns.

*Data Time Segment 1 (DTSEG1)* is the data time segment before the
 sample point. Valid values are 1–31. DTSEG1 is described in the Bosch
 *M_CAN Controller Area Network User’s Manual*, Revision 3.2.1.
 The actual hardware interpretation of this value is one more than the programmed
 value.

*Data Time Segment 2 (DTSEG2)* is the data time segment after the
 sample point. NTSEG2 is described in the Bosch *M_CAN Controller Area
 Network User’s Manual*, Revision 3.2.1. The actual hardware
 interpretation of this value is one more than the programmed value.

*Data (Re-)Synchronization Jump Width (DSJW)*. Valid programmed values
 are 0–15. The actual hardware interpretation of this value is one more than the
 programmed value.

#### 32-bit baud rate
 property

The following information is valid for the former 32-bit Baud
 Rate property that was replaced by the 64bit property. You still
 can use the baud rate values used with the 32-bit property.

When the upper nibble is set to 0x8 (that is, 0x80000000), the remaining bits
 provide fields for more custom CAN communication baud rate programming.

|  | 31..28 | 27..26 | 25..24 | 23..20 | 19..16 | 15..10 | 9..8 | 7..0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom | b1000 | Res | SJW (0–3) | TSEG2 (0–7) | TSEG1 (1–15) | Res | Tq (25–800) |  |

*(Re-)Synchronization Jump Width (SJW)*. Valid programmed values are
 0–3. The actual hardware interpretation of this value is one more than the
 programmed value.

*Time Segment 2 (TSEG2)* is the time segment after the sample point.
 Valid programmed values are 0–7. TSEG2 is the Phase_Seg2(D) described in Bosch's
 *CAN with Flexible Data-Rate Specification, Version 1.0*. The
 actual hardware interpretation of this value is one more than the programmed
 value.

*Time Segment 1 (TSEG1)* is the time segment before the sample point.
 Valid programmed values are 1–0xF (1–15 decimal). TSEG1 is the combination of
 the Prop_Seg(D) and Phase_Seg1(D) described in the Bosch *CAN with Flexible
 Data-Rate Specification, Version 1.0*. The actual hardware
 interpretation of this value is one more than the programmed value.

*Time quantum (Tq)* is used to program the baud rate prescaler. Valid
 programmed values are 25–800, in increments of 25 ns.

#### Formulas

Baud rate = (Total Ticks per Sec / Ticks for 1 bit ) = (Oscillator
 Frequency[Hz] * Tq[Ticks]) / 25) /
 (Sync_Seg[Ticks] + TSEG1[Ticks] +
 TSEG2[Ticks])

Note

Sample Point = (TSEG1 + Sync_Seg) /
 (TSEG1 + Sync_Seg +
 TSEG2)

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-iomode-100026.html language=enus -->
## TOPIC 00061: Intf.CAN.IoMode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-iomode-100026.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-iomode-100026.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the I/O Mode the interface is using: CAN (0), CAN FD (1), or CAN FD + BRS (2). The value is initialized from the database cluster when the session is created and cannot be changed later. However, you can transmit standard CAN frames on a CAN FD network. Refer to the Interface:CAN:Transmit

Intf.CAN.IoMode

Indicates the I/O Mode the interface is using: CAN (0), CAN FD (1), or CAN FD + BRS
 (2).

The value is initialized from the database cluster when the session is created and cannot be
 changed later. However, you can transmit standard CAN frames on a CAN FD network. Refer
 to the Interface:CAN:Transmit I/O Mode property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-listen-only-2100022.html language=enus -->
## TOPIC 00062: Intf.CAN.LstnOnly?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-listen-only-2100022.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-listen-only-2100022.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines whether the CAN interface transmits any information to the CAN bus. You can modify this property only when the interface is stopped. When this property is FALSE, the interface can transmit CAN frames and acknowledge received CAN frames. When this property is TRUE, the interface can neithe

Intf.CAN.LstnOnly?

Determines whether the CAN interface transmits any information to the CAN
 bus.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

When this property is FALSE, the interface can transmit CAN frames and
 acknowledge received CAN frames.

When this property is TRUE, the interface can neither transmit CAN frames nor
 acknowledge a received CAN frame. The TRUE value enables passive monitoring of
 network traffic, which can be useful for debugging scenarios when you do not
 want to interfere with a communicating network cluster.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-pending-tx-order-100020.html language=enus -->
## TOPIC 00063: Intf.CAN.PendTxOrder

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-pending-tx-order-100020.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-pending-tx-order-100020.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures how the CAN interface manages the internal queue of frames: As Submitted (0) or By Identifier (1). As Submitted transmits frames in the order that they were submitted into the queue. By Identifier transmits frames with the highest priority identifier (lower CAN ID value) first. You can mo

Intf.CAN.PendTxOrder

Configures how the CAN interface manages the internal queue of frames: As
 Submitted (0) or By Identifier (1).

*As Submitted* transmits frames in the order that they were submitted into the
 queue. *By Identifier* transmits frames with the highest priority identifier
 (lower CAN ID value) first.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Note

NI-XNET stores frames in an internal queue and transmits them onto the CAN bus
 when the bus is idle. This property modifies how NI-XNET handles this queue of
 frames.

When you configure this property to be As Submitted, frames are transmitted in
 the order that they were submitted into the queue. There is no reordering of any
 frames, and a higher priority frame may be delayed due to the transmission or
 retransmission of a previously submitted frame. However, this mode has the
 highest performance.

When you configure this property to be By Identifier, frames with the highest
 priority identifier (lower CAN ID value) transmit first. The frames are stored
 in a priority queue sorted by ID. If a frame currently being transmitted
 requires retransmission (for example, it lost arbitration or failed with a bus
 error), and a higher priority frame is queued in the meantime, the lower
 priority frame is not immediately retried, but the higher priority frame is
 transmitted instead. In this mode, you can emulate multiple ECUs and still see a
 behavior similar to a real bus in that the highest priority message is
 transmitted on the bus. This mode may be slower in performance (possible delays
 between transmissions as the queue is re-evaluated), and lower priority messages
 may be delayed indefinitely due to frequent high-priority messages.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-termination-100025.html language=enus -->
## TOPIC 00064: Intf.CAN.Term

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-termination-100025.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-termination-100025.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the onboard termination of the NI-XNET interface CAN connector (port) to be Off or On. CAN hardware can have different termination requirements;, and the Off and On values have different meanings. You can modify this property only when the interface is stopped. This property does not take

Intf.CAN.Term

Configures the onboard termination of the NI-XNET interface CAN connector (port) to
 be Off or On. CAN hardware can have different termination requirements;, and the Off and
 On values have different meanings.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

#### High-Speed CAN

High-Speed CAN networks are typically terminated on the bus itself instead of
 within a node. However, NI-XNET allows you to configure termination within the
 node to simplify testing. If your bus already has the correct amount of
 termination, leave this property in the default state of Off. However, if you
 require termination, set this property to On.

| Value | Meaning | Description |
| --- | --- | --- |
| Off | Disabled | Termination is disabled |
| On | Enabled | Termination (120 kΩ) is enabled |

#### Low-Speed/Fault-Tolerant CAN

Every node on a low-speed CAN network requires termination for each CAN data line
 (CAN_H and CAN_L). This configuration allows the Low-Speed/Fault-Tolerant CAN
 port to provide fault detection and recovery.

In general, if the existing network has an overall network termination of 125 Ω
 or less, select the default 4.99 kΩ option. Otherwise, you should turn on
 termination to enable the 1.11 kΩ option.

| Value | Meaning | Description |
| --- | --- | --- |
| Off | 4.99 kΩ | Termination is set to 4.99 kΩ |
| On | 1.11 kΩ | Termination is set to 1.11 kΩ |

#### Single Wire CAN

The ISO standard requires single wire transceivers to have a 9.09 kΩ resistor,
 and no additional configuration is supported.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-transceiver-state-100028.html language=enus -->
## TOPIC 00065: Intf.CAN.TcvrState

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-transceiver-state-100028.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-transceiver-state-100028.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the CAN transceiver and CAN controller states, such as such as whether the transceiver is asleep or communicating. The transceiver state controls whether the transceiver is asleep or communicating, as well as configuring other special modes. The following table lists the accepted values.

Intf.CAN.TcvrState

Configures the CAN transceiver and CAN controller states, such as such as whether the
 transceiver is asleep or communicating.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

The transceiver state controls whether the transceiver is asleep or
 communicating, as well as configuring other special modes. The following table
 lists the accepted values.

| Enumeration | Value |
| --- | --- |
| Normal | 0 |
| Sleep | 1 |
| Single Wire Wakeup | 2 |
| Single Wire High-Speed | 3 |

#### Normal

*Normal* state sets the transceiver to normal communication mode. If
 the transceiver is in the Sleep mode, this performs a local wakeup of the
 transceiver and CAN controller chip.

#### Sleep

*Sleep* state sets the transceiver and CAN controller chip to Sleep (or standby)
 mode. You can set the interface to Sleep mode only while the interface is
 communicating. If the interface has not been started, setting the transceiver to
 Sleep mode returns an error.

Before going to sleep, all pending transmissions are transmitted onto the CAN
 bus. Once all pending frames have been transmitted, the interface and
 transceiver go into Sleep (or standby) mode. Once the interface enters Sleep
 mode, further communication is not possible until a wakeup occurs.

The transceiver and CAN controller wake from Sleep mode when either a local
 wakeup or remote wakeup occurs. A *local wakeup* occurs when the
 application sets the transceiver state to either Normal or Single Wire Wakeup.
 A*remote wakeup* occurs when a remote node transmits a CAN frame
 (referred to as the wakeup frame). The wakeup frame wakes up the NI-XNET
 interface transceiver and CAN controller chip. The CAN controller chip does not
 receive or acknowledge the wakeup frame.

After detecting the wakeup frame and idle bus, the CAN interface enters Normal
 mode. When the local or remote wakeup occurs, frame transmissions resume from
 the point at which the original Sleep mode was set.

You can use [XNET Read (State CAN Comm)](/csh?topicname=xnet-read-state-can-comm.html) to detect when a wakeup occurs. To
 suspend the application while waiting for the remote wakeup, use [XNET Wait
 (CAN Remote Wakeup)](/csh?topicname=xnet-wait-can-remote-wakeup.html).

#### Single Wire Wakeup

For a remote wakeup to occur for Single Wire transceivers, the node that transmits the wakeup
 frame first must place the network into the Single Wire Wakeup Transmission mode
 by asserting a higher voltage.

This state sets a Single Wire transceiver into the Single Wire Wakeup
 Transmission mode, which forces the Single Wire transceiver to drive a higher
 voltage level on the network to wake up all sleeping nodes. Other than this
 higher voltage, this mode is similar to Normal mode. CAN frames can be received
 and transmitted normally.

If you are not using a Single Wire transceiver, setting this state returns an
 error. If your current mode is Single Wire High-Speed, setting this mode returns
 an error because you are not allowed to wake up the bus in high-speed mode.

The application controls the timing of how long the wakeup voltage is driven. The
 application typically changes to Single Wire Wakeup mode, transmits a single
 wakeup frame, and then returns to Normal mode.

#### Single Wire High-Speed

This state sets a Single Wire transceiver into Single Wire High-Speed Communication mode. If
 you are not using a Single Wire transceiver, setting this state returns an
 error.

Single Wire High-Speed Communication mode disables the transceiver's internal
 waveshaping function, allowing the SAE J2411 High Speed baud rate of 83.333
 kbytes/s to be used. The disadvantage versus Single Wire Normal Communication
 mode, which only allows the SAE J2411 baud rate of 33.333 kbytes/s, is degraded
 EMC performance. Other than the disabled waveshaping, this mode is similar to
 Normal mode. CAN frames can be received and transmitted normally.

This mode has no relationship to High-Speed transceivers. It is merely a higher
 speed mode of the Single Wire transceiver, typically used to download data when
 the onboard network is attached to an offboard tester ECU.

The Single Wire transceiver does not support use of this mode in conjunction with
 Sleep mode. For example, a remote wakeup cannot transition from sleep to this
 Single Wire High-Speed mode. Therefore, setting the mode to Sleep from Single
 Wire High-Speed mode returns an error.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-transceiver-type-100029.html language=enus -->
## TOPIC 00066: Intf.CAN.TcvrType

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-transceiver-type-100029.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-transceiver-type-100029.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables you to set the transceiver type for XNET hardware that provides a software-selectable transceiver type. You can modify this property only when the interface is stopped. Use the XNET Interface CAN:Transceiver Capability property to determine whether your hardware supports a software-selectabl

Intf.CAN.TcvrType

Enables you to set the transceiver type for XNET hardware that provides a
 software-selectable transceiver type.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Use the XNET Interface CAN:Transceiver Capability property
 to determine whether your hardware supports a software-selectable transceiver.

You can use the Transceiver Type property to determine
 the currently configured transceiver type. The following table lists accepted
 values:

| Enumeration | Value |
| --- | --- |
| High-Speed (HS) | 0 |
| Low-Speed (LS) | 1 |
| Single Wire (SW) | 2 |
| External (Ext) | 3 |
| Disconnect (Disc) | 4 |

The default value for this property depends on the hardware you are using. If you
 have fixed-personality hardware, the default value is the hardware value. If you
 have hardware that supports software-selectable transceivers, the default is
 High-Speed.

#### Transceiver Configuration

*High-Speed (HS)* enables the high-speed transceiver, which supports
 baud rates of 40 kbaud to 1 Mbaud. When using a high-speed transceiver, you can
 also communicate with a CAN FD bus. Refer to Interface:CAN:64bit FD Baud Rate for more information about
 supported CAN FD baud rates.

*Low-Speed/Fault-Tolerant (LS/FT)* enables the
 low-speed/fault-tolerant transceiver. This transceiver supports baud rates of
 40–125 kbaud.

*Single Wire (SW)* enables the single wire transceiver. A single wire
 transceiver supports baud rates of 33.333 kbaud and 83.333 kbaud.

*External (Ext)* allows you to use an external transceiver to connect
 to your CAN bus. Refer to Interface:CAN:External Transceiver Config for more
 information.

*Disconnect (Disc)* allows you to disconnect the CAN controller chip
 from the connector. You can use this value when you physically change the
 external transceiver.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-transmit-iomode-100039.html language=enus -->
## TOPIC 00067: Intf.CAN.TxIoMode

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-transmit-iomode-100039.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-transmit-iomode-100039.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the I/O Mode the interface uses when transmitting a CAN frame. By default, this property matches the XNET Cluster CAN:I/O Mode property. However, even if the interface is in CAN FD+BRS mode, you can force it to transmit frames in the standard CAN format. For this purpose, set this property

Intf.CAN.TxIoMode

Specifies the I/O Mode the interface uses when transmitting a CAN
 frame.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

By default, this property matches the XNET Cluster CAN:I/O Mode property.
 However, even if the interface is in CAN FD+BRS mode, you can force it to
 transmit frames in the standard CAN format. For this purpose, set this property
 to CAN.

The Transmit I/O mode may not exceed the mode set by the XNET Cluster CAN:I/O
 Mode property.

Note

Note

CAN:I/O Mode

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-can-transmit-pause-21000a3.html language=enus -->
## TOPIC 00068: Intf.CAN.TxPause

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-can-transmit-pause-21000a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-can-transmit-pause-21000a3.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether the CAN hardware pauses before transmitting the next frame. When this property is enabled, the CAN hardware waits for two full bit times after successful transmission before transmitting the next frame. This allows other CAN nodes to transmit lower priority CAN messages while this

Intf.CAN.TxPause

Indicates whether the CAN hardware pauses before transmitting the next
 frame.

When this property is enabled, the CAN hardware waits for two full bit times after
 successful transmission before transmitting the next frame. This allows other CAN nodes
 to transmit lower priority CAN messages while this CAN node is transmitting
 high-priority CAN messages with high speed. Default value is False.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-echo-tx-2100010.html language=enus -->
## TOPIC 00069: Intf.EchoTx?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-echo-tx-2100010.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-echo-tx-2100010.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines whether Frame Input or Signal Input sessions contain frames that the interface transmits. When this property is true, and a frame transmit is complete for an Output session, the frame is echoed to the Input session. Frame Input sessions can use the Flags field to differentiate frames rece

Intf.EchoTx?

Determines whether Frame Input or Signal Input sessions contain frames that the
 interface transmits.

When this property is true, and a frame transmit is complete for an Output session, the
 frame is echoed to the Input session. Frame Input sessions can use the Flags field to
 differentiate frames received from the bus and frames the interface transmits.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

When using [XNET Read (Frame CAN)](/csh?topicname=xnet-read-frame-can.html), XNET Read
 (Frame FlexRay), or [XNET Read
 (Frame LIN)](/csh?topicname=xnet-read-frame-lin.html), the Flags field is parsed into an
 **echo?** Boolean in the frame cluster. When using
 [XNET
 Read (Frame Raw)](/csh?topicname=xnet-read-frame-raw.html), you can parse the Flags field manually by reviewing
 the Raw Frame Format section. Signal Input sessions cannot differentiate the
 origin of the incoming data.

Note

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-endpoint-receive-filter-c1000bc.html language=enus -->
## TOPIC 00070: Intf.Enet.Ept.RxFilter

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-endpoint-receive-filter-c1000bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-endpoint-receive-filter-c1000bc.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Each frame that is received by the interface is forwarded to either the XNET endpoint or the OS stack (not both). This property configures zero, one, or two identification elements (filters) for this forwarding decision. The following C language pseudo-code describes how XNET forwards each received

Intf.Enet.Ept.RxFilter

Each frame that is received by the interface is forwarded to either the XNET endpoint
 or the OS stack (not both). This property configures zero, one, or two identification
 elements (filters) for this forwarding decision.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

The following C language pseudo-code describes how XNET forwards each received
 frame to either the XNET endpoint or the OS stack:

```text
// TRUE forwards to XNET endpoint, FALSE forwards to OS stack
Boolean forwardFrameToEndpoint = FALSE;
for (int i = 0; i < 2; i++)
{
	boolean endpointMatch =
	( RxFilter[i].useVID || RxFilter[i].usePriority || RxFilter[i].useDestinationMAC );

	if ( RxFilter[i].useVID && (RxFilter[i].VID != frameVID)
	endpointMatch = FALSE;

	if ( RxFilter[i].usePriority && (RxFilter[i].Priority != framePriority) )
	endpointMatch = FALSE;

	if ( RxFilter[i].useDestinationMAC && (RxFilter[i].DestinationMAC != frameDestinationMAC) )
	endpointMatch = FALSE;

	// Only one element must match in order to forward to XNET endpoint.
	forwardFrameToEndpoint = forwardFrameToEndpoint || endpointMatch;
}
```

The default value is:

RxFilter[0].UseVID = TRUE, RxFilter[0].VID = 2, 
RxFilter[0].UsePriority = TRUE, RxFilter[0].Priority = 3, 
RxFilter[0].UseDestinationMAC = FALSE, 
RxFilter[1].UseVID = TRUE, RxFilter[1].VID = 2, 
RxFilter[1]UsePriority = TRUE, RxFilter[1].Priority = 2, 
RxFilter[1].UseDestinationMAC = FALSE

This default value corresponds to AVB traffic (SR class A and B) using the
 defaults specified for the credit-based shaper in IEEE Std 802.1Q.

If an XNET input session is not started for the interface's endpoint (e.g., Frame
 Input Stream session on "ENET1"), all frames are forwarded to the OS stack. An
 XNET input session for the interface's monitor (e.g., Frame Input Stream session
 on "ENET1/monitor") receives all frames regardless of the value of this
 property.

If you write this property with fewer than two elements, the missing element is
 configured with all three "use" flags set to false. For example, if you write
 zero elements (an empty array), all traffic is forwarded to the OS stack.

IEEE Std 802.1Q specifies that VLAN ID (VID) and destination MAC address can be
 used for forwarding decisions. The VID is typically used for a type of traffic,
 and destination MAC address is used for a specific stream (flow). The Priority
 Code Point (PCP) determines how the frame travels through transmit queues in the
 network. The PCP is commonly known as priority.

The data type for VID is U16. Each VID value ranges from 1 to 4094. The VID in
 this property applies only to a tagged frame. The tagged frame must use a Tag
 Protocol Identification (TPID) of hex 8100, which is the Customer VLAN Tag
 (C-TAG) format commonly known as a VLAN tag. This property's VID value is
 compared to the VID value in the Tag Control Info of the frame. An untagged
 frame has an implicit VID of 1, but if this property's UseVID is true and VID is
 1, the untagged frame forwards to the OS stack.

The data type for priority is U8. Each priority value ranges from 0 to 7. The
 priority in this property applies only to a tagged frame. The tagged frame must
 use a Tag Protocol Identification (TPID) of hex 8100, which is the Customer VLAN
 Tag (C-TAG) format commonly known as a VLAN tag. This property's priority value
 is compared to the Priority Code Point (PCP) value in the Tag Control Info of
 the frame. An untagged frame has an implicit priority of 0, but if this
 property's UsePriority is true and Priority is 0, the untagged frame forwards to
 the OS stack.

The destination MAC address is a string of six octets. Each octet consists of two
 hexadecimal (0-9, A-F) digits. The octets are separated by colon. For example:
 00:80:2F:AB:CD:EF.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-endpoint-transmit-bandwidth-91000bf.html language=enus -->
## TOPIC 00071: Intf.Enet.Ept.TxBandw

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-endpoint-transmit-bandwidth-91000bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-endpoint-transmit-bandwidth-91000bf.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the maximum bandwidth for the credit-based shaper algorithm specified in IEEE Std 802.1Q, which is used for all transmissions from the endpoint. The value for this property is in units of bits per second. The Transmit Bandwidth property applies when you call XNET Write (Frame Ethernet) to

Intf.Enet.Ept.TxBandw

Configures the maximum bandwidth for the credit-based shaper algorithm specified in
 IEEE Std 802.1Q, which is used for all transmissions from the endpoint.

The value for this property is in units of bits per second.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

The Transmit Bandwidth property applies when you call
 [XNET
 Write (Frame Ethernet)](/csh?topicname=xnet-read-frame-ethernet.html) to transmit frames using an endpoint session.
 The endpoint is the highest importance for transmit, and the OS stack is lower
 importance. This property corresponds to the
 **adminIdleSlope** parameter as described in IEEE Std
 802.1Q. The default value corresponds to 75% of a 100 Mb/s link.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-ipv4-address-31000eb.html language=enus -->
## TOPIC 00072: Intf.Enet.IpV4Addr

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-ipv4-address-31000eb.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-ipv4-address-31000eb.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the IPv4 address that is configured on the XNET interface in the network by the OS stack. The IPv4 address is returned as a string in dotted-decimal notation. For example, 192.0.2.1.

Intf.Enet.IpV4Addr

Indicates the IPv4 address that is configured on the XNET interface in the network
 by the OS stack.

The IPv4 address is returned as a string in dotted-decimal notation. For example,
 192.0.2.1.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-jumbo-frames.html language=enus -->
## TOPIC 00073: Intf.Enet.JumboFrames

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-jumbo-frames.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-jumbo-frames.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the jumbo frame setting for the interface. You can configure this property using NI-MAX or the System Configuration Jumbo Frames property in LabVIEW. The Jumbo Frames property is a ring (enumerated list) with the following values: Enumeration Value Description Disabled 0 Monitor and OS sta

Intf.Enet.JumboFrames

Indicates the jumbo frame setting for the interface. You can configure this
 property using NI-MAX or the System Configuration Jumbo Frames
 property in LabVIEW.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

The Jumbo Frames property is a ring (enumerated list) with
 the following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Monitor and OS stack paths will not receive jumbo frames. |
| 9018 Bytes | 1 | Jumbo frames up to 9018 bytes can be received on the monitor and OS stack paths. |

Note

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-link-speed.html language=enus -->
## TOPIC 00074: Intf.Enet.LinkSpeed

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-link-speed.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-link-speed.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the current link speed on the interface or shows if the link is down. The LinkSpeed property is a ring (enumerated list) with the following values: Enumeration Value Description 0 Link Down The link for the Ethernet interface is down. 1 100 Mb/s The Ethernet interface is operating at 100 M

Intf.Enet.LinkSpeed

Indicates the current link speed on the interface or shows if the link is
 down.

The LinkSpeed property is a ring (enumerated list) with the
 following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| 0 | Link Down | The link for the Ethernet interface is down. |
| 1 | 100 Mb/s | The Ethernet interface is operating at 100 Mb/s (Fast Ethernet) capability. |
| 2 | 1000 Mb/s | The Ethernet interface is operating at 1000 Mb/s (Gigabit) capability. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-operational-status-1000aa.html language=enus -->
## TOPIC 00075: Intf.Enet.OpStat

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-operational-status-1000aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-operational-status-1000aa.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the operational status of the interface (that is, communicating or not). String Value Description Down 0 The interface cannot transmit or receive frames (packets). Up 1 The interface is ready to transmit and receive frames (packets). This property corresponds to interface operational statu

Intf.Enet.OpStat

Indicates the operational status of the interface (that is, communicating or
 not).

| String | Value | Description |
| --- | --- | --- |
| Down | 0 | The interface cannot transmit or receive frames (packets). |
| Up | 1 | The interface is ready to transmit and receive frames (packets). |

This property corresponds to interface operational status as specified in IETF management
 standards such as RFC 2863 and RFC 8343.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

#### Interface state

The XNET interface Communicating state behaves differently for Ethernet compared
 to other XNET protocols, such as CAN. The OS stack provides a network interface,
 and the operating system brings its network interface to communicating state
 ("link up") at power on. The operating system keeps the interface in
 communicating state until it is powered off. Therefore, the Ethernet interface
 is communicating at its physical layer (PHY) before and after the existence of
 any XNET session.

XNET interface states have a limited context; they control the transfer of frames
 to/from the XNET endpoint and monitor paths, but they do not control the actual
 communicating state ("link up" or "link down") of the interface. The Operational
 Status property returns the actual communicating state of the interface.

As a consequence of this state behavior, it is possible to enable the time sync
 protocol prior to starting the XNET interface because the time sync protocol
 operates independently from the endpoint and monitor paths (like the OS stack).

#### Read behavior

Although the link is up prior to XNET interface start, if a frame is received
 prior to the initial XNET start and would normally be received by endpoint or
 monitor, XNET Read will not return the frame.

[XNET
 Start](/csh?topicname=xnet-start.html) discards all unread frames from the receive queue. [XNET
 Stop](/csh?topicname=xnet-stop.html) has no effect on the receive queue, and link down/up events have
 no effect on the receive queue. If frames are received but not read, and your
 application stops the interface without restarting, XNET Read will return the
 previously received frames.

All unread frames are discarded from the receive queue when the XNET session is
 cleared.

#### Write behavior

When [XNET
 Stop](/csh?topicname=xnet-stop.html) is invoked, or when the link goes down, pending frames in the
 XNET transmit queues are discarded.

[XNET
 Write](/csh?topicname=xnet-write.html) ignores the operational status of the link when the XNET
 interface is not running. If you invoke XNET Write prior to starting the XNET
 interface, the frame is queued regardless of the operational status. If the link
 is up when [XNET Start](/csh?topicname=xnet-start.html) is invoked, those queued frames are transmitted. If the
 link is down when XNET Start is invoked, those queued frames are discarded.

If you invoke XNET Write on a started XNET interface and the link is down, the
 frame is not queued and an error is returned. After the link comes back up, when
 you invoke XNET Write again, frames are queued for transmission (with no need to
 restart the XNET interface).

You can use [XNET Wait (Transmit Complete)](/csh?topicname=xnet-wait-transmit-complete.html) to ensure that frames are transmitted
 before you clear the XNET session.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-os-network-adapter-desc-31000ed.html language=enus -->
## TOPIC 00076: Intf.Enet.OsAdapterDesc

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-os-network-adapter-desc-31000ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-os-network-adapter-desc-31000ed.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the description of this XNET session's Ethernet interface as represented in the OS. On XNET Ethernet products, each port can be accessed as an XNET interface or by using an operating system API for Ethernet. In NI MAX, this name is shown on the Network Settings tab for the system, listed und

Intf.Enet.OsAdapterDesc

Returns the description of this XNET session's Ethernet interface as represented in
 the OS. On XNET Ethernet products, each port can be accessed as an XNET interface or by
 using an operating system API for Ethernet.

In NI MAX, this name is shown on the Network Settings tab for the
 system, listed under Network Adapters.

On Windows, this is the network adapter description in network properties.

On Linux, this is the network interface name and is the same as the OS Network Adapter
 Name property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-os-network-adapter-name-31000ec.html language=enus -->
## TOPIC 00077: Intf.Enet.OsAdapterName

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-os-network-adapter-name-31000ec.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-os-network-adapter-name-31000ec.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the name of this XNET session's Ethernet interface as represented in the OS. On XNET Ethernet products, each port can be accessed as an XNET interface or by using an operating system API for Ethernet. On Windows, this is the network adapter name. On Linux, this is the network interface name

Intf.Enet.OsAdapterName

Returns the name of this XNET session's Ethernet interface as represented in
 the OS. On XNET Ethernet products, each port can be accessed as an XNET interface or by
 using an operating system API for Ethernet.

On Windows, this is the network adapter name.

On Linux, this is the network interface name and is the same as the Network Adapter
 Description property

This name is used in applications such as Wireshark.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-stats-rxbad-frames-91000b6.html language=enus -->
## TOPIC 00078: Intf.Enet.St.RxBad

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-stats-rxbad-frames-91000b6.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-stats-rxbad-frames-91000b6.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Count of frames received with an error detected by the Ethernet MAC and/or PHY. This statistic is analogous to the ifInErrors parameter as described in RFC 2863.

Intf.Enet.St.RxBad

Count of frames received with an error detected by the Ethernet MAC and/or
 PHY.

This statistic is analogous to the **ifInErrors** parameter as
 described in RFC 2863.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-stats-rxgood-frames-91000af.html language=enus -->
## TOPIC 00079: Intf.Enet.St.RxGood

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-stats-rxgood-frames-91000af.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-stats-rxgood-frames-91000af.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Count of error-free frames received. This count is equal to (Rx Good Unicast + Rx Good Multicast + Rx Good Broadcast).

Intf.Enet.St.RxGood

Count of error-free frames received.

This count is equal to (*Rx Good Unicast* + *Rx Good
 Multicast* + *Rx Good Broadcast*).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-stats-txbytes-91000b7.html language=enus -->
## TOPIC 00080: Intf.Enet.St.TxBytes

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-stats-txbytes-91000b7.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-stats-txbytes-91000b7.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Count of the number of bytes (octets) transmitted. The count for each frame is its frame length. Reading this counter twice can be used to obtain an estimate of transmitted bandwidth over the time between the two reads.

Intf.Enet.St.TxBytes

Count of the number of bytes (octets) transmitted. The count for each frame is its
 frame length.

Reading this counter twice can be used to obtain an estimate of transmitted bandwidth
 over the time between the two reads.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-stats-txgood-frames-91000b8.html language=enus -->
## TOPIC 00081: Intf.Enet.St.TxGood

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-stats-txgood-frames-91000b8.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-stats-txgood-frames-91000b8.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Count of error-free frames transmitted. This count is equal to (Tx Good Unicast + Tx Good Multicast + Tx Good Broadcast).

Intf.Enet.St.TxGood

Count of error-free frames transmitted.

This count is equal to (*Tx Good Unicast* + *Tx Good
 Multicast* + *Tx Good Broadcast*).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-accuracy-1000c6.html language=enus -->
## TOPIC 00082: Intf.Enet.Time.ClkAccy

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-accuracy-1000c6.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-accuracy-1000c6.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the accuracy of the hardware clock (e.g., oscillator) distributed by the clock when it is the grandmaster. The best master clock algorithm (BMCA) uses this property in its comparison of clock quality. This property uses a ring (enumerated list) with the following values: Enumeration Value

Intf.Enet.Time.ClkAccy

Indicates the accuracy of the hardware clock (e.g., oscillator) distributed by the
 clock when it is the grandmaster.

The best master clock algorithm (BMCA) uses this property in its comparison of clock
 quality.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

This property uses a ring (enumerated list) with the following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| Within25nsec | 32 | Time is accurate to within 25 ns |
| Within100nsec | 33 | Time is accurate to within 100 ns |
| Within250nsec | 34 | Time is accurate to within 250 ns |
| Within1usec | 35 | Time is accurate to within 1 µs |
| Within2500nsec | 36 | Time is accurate to within 2500 ns |
| Within10usec | 37 | Time is accurate to within 10 µs |
| Within25usec | 38 | Time is accurate to within 25 µs |
| Within100usec | 39 | Time is accurate to within 100 µs |
| Within250usec | 40 | Time is accurate to within 250 µs |
| Within1msec | 41 | Time is accurate to within 1 ms |
| Within2500usec | 42 | Time is accurate to within 2500 µs |
| Within10msec | 43 | Time is accurate to within 10 ms |
| Within25msec | 44 | Time is accurate to within 25 ms |
| Within100msec | 45 | Time is accurate to within 100 ms |
| Within250msec | 46 | Time is accurate to within 250 ms |
| Within1sec | 47 | Time is accurate to within 1 s |
| Within10sec | 48 | Time is accurate to within 10 s |
| GreaterThan10sec | 49 | Time accuracy is greater than 10 s |
| Unknown | 254 | Clock is not synchronized |

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 clockAccuracy parameter as described in 14.2.4 of IEEE Std 802.1AS-2011, which
 in turn references 7.6.2.5 of IEEE Std 1588-2008, which describes clock accuracy
 values.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-adjust-net-time-91000d1.html language=enus -->
## TOPIC 00083: Intf.Enet.Time.Adjust

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-adjust-net-time-91000d1.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-adjust-net-time-91000d1.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: When this clock is the grandmaster (that is, the Grandmaster Clock ID equals the Clock ID), a write of this property applies a positive or negative adjustment to the time distributed to the network. This can be used to align network time with another timescale. When this clock is a slave (not the gr

Intf.Enet.Time.Adjust

When this clock is the grandmaster (that is, the Grandmaster Clock
 ID equals the Clock ID), a write of this property
 applies a positive or negative adjustment to the time distributed to the network. This
 can be used to align network time with another timescale.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

When this clock is a slave (not the grandmaster), a write of this property has no
 effect (error returned); the adjustment will be overridden when time is received
 from the grandmaster.

This property corresponds to the **lastGmPhaseChange**
 parameter of the ClockSourceTime.invoke function,
 specified in the IEEE Std 802.1AS-2011.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-bmca-21000c2.html language=enus -->
## TOPIC 00084: Intf.Enet.Time.BMCA?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-bmca-21000c2.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-bmca-21000c2.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables (runs) the Best Master Clock Algorithm (BMCA) of the time synchronization Protocol. The BMCA dynamically exchanges messages over the network to select the best grandmaster in the network, and to change all port states in order to transfer timing messages from the selected grandmaster to slav

Intf.Enet.Time.BMCA?

Enables (runs) the Best Master Clock Algorithm (BMCA) of the time synchronization
 Protocol.

The BMCA dynamically exchanges messages over the network to select the best grandmaster
 in the network, and to change all port states in order to transfer timing messages from
 the selected grandmaster to slaves.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

When this property is True, Protocol runs the BMCA. The Port
 State property is determined from operation of the BMCA. The XNET
 interface is capable of acting as a grandmaster. Therefore, the BMCA can set the
 Port State property to Slave (i.e., XNET interface
 receives time) or Master (XNET interface sends time). The Port State
 Configured property is not used while the BMCA is enabled. The BMCA
 uses the following properties in order for its selection of grandmaster (with
 exceptions for topology):

- Priority1
- Clock Class
- Clock Accuracy
- Clock Offset Scaled Log Variance
- Priority2
- Clock ID

When this property is False, the BMCA is not operational. The False value is
 useful for in-vehicle applications in which the topology for time
 synchronization is considered to be part of the vehicle's static design. The
 Port State Configured property must be written in
 order to specify the Master or Slave state for the port. The read-only
 Port State property reflects Port State
 Configured. When an XNET session is started on a port that is
 set to Tap mode, this property becomes read only and its value cannot be
 modified.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-clockclass-1000c5.html language=enus -->
## TOPIC 00085: Intf.Enet.Time.ClkCls

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-clockclass-1000c5.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-clockclass-1000c5.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the traceability of time or frequency distributed by the clock when it is the grandmaster. The value for this property is an integer. The best master clock algorithm (BMCA) uses this property in its comparison of clock quality. Clock Class Specification Integer Description 6 The clock is sy

Intf.Enet.Time.ClkCls

Provides the traceability of time or frequency distributed by the clock when it is
 the grandmaster. The value for this property is an integer.

The best master clock algorithm (BMCA) uses this property in its comparison of clock
 quality.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

#### Clock Class Specification

| Integer | Description |
| --- | --- |
| 6 | The clock is synchronized to a primary time reference. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 7 | The clock has previously been designated as Clock Class 6, but has lost the ability to synchronize to a primary time reference. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 13 | The clock is synchronized to an application-specific time source. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 14 | The clock has previously been designated as Clock Class 13, but has lost the ability to synchronize to an application-specific time source. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 52 | The clock is degradation alternative A for a Clock Class 7 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 58 | The clock is degradation alternative A for a Clock Class 14 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 68–122 | The clock uses an alternate PTP profile. |
| 133–170 | The clock uses an alternate PTP profile. |
| 187 | The clock is degradation alternative B for a Clock Class 7 clock that is not within holdover specification. A clock in this class can be a slave to another clock in the domain. |
| 193 | The clock is degradation alternative B for a Clock Class 14 clock that is not within holdover specification. A clock of this class can be a slave to another clock in the domain. |
| 216–232 | The clock uses an alternate PTP profile. |
| 248 | The default Clock Class. This class is used if none of the other class definitions apply. |
| 255 | The clock is a slave-only clock. |

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **clockClass** parameter as described in 14.2.3 of IEEE
 Std 802.1AS-2011, which in turn references 7.6.2.4 of IEEE Std 1588-2008, which
 describes the clock class specification.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-clockid-31000c4.html language=enus -->
## TOPIC 00086: Intf.Enet.Time.ClkID

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-clockid-31000c4.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-clockid-31000c4.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: This property uniquely identifies the clock in the network. The Clock ID is formed by taking the MAC address assigned to the clock and mapping it to an array of eight bytes, according to rules in the IEEE Std 802 EUI-48 standard. The best master clock algorithm (BMCA) uses this property as a tie-bre

Intf.Enet.Time.ClkID

This property uniquely identifies the clock in the network.

The Clock ID is formed by taking the MAC address assigned to the clock and mapping it to
 an array of eight bytes, according to rules in the IEEE Std 802 EUI-48 standard. The
 best master clock algorithm (BMCA) uses this property as a tie-breaker among clocks that
 would otherwise be equal.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

The Clock ID is returned as a string of eight octets. Each octet consists of two
 hexadecimal (0-9, A-F) digits. The octets are separated by colon. For example,
 00:80:2F:AB:CD:EF:00:01

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 clockIdentity parameter as described in 14.2.1 of IEEE Std 802.1AS-2011.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-gmaccuracy-1000cd.html language=enus -->
## TOPIC 00087: Intf.Enet.Time.GMClkAccy

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-gmaccuracy-1000cd.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-gmaccuracy-1000cd.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the Clock Accuracy of the currently selected grandmaster for this clock. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the grandmasterClockAccuracy attribute, specified in 14.4.5 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.GMClkAccy

Provides the Clock Accuracy of the currently selected grandmaster for this clock.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 grandmasterClockAccuracy attribute, specified in 14.4.5 of IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-gmclockid-31000cb.html language=enus -->
## TOPIC 00088: Intf.Enet.Time.GMClkID

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-gmclockid-31000cb.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-gmclockid-31000cb.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: This property provides the Clock ID of the currently selected grandmaster for this clock. The Grandmaster Clock ID is returned as a string of eight octets. Each octet consists of two hexadecimal (0-9, A-F) digits. The octets are separated by colon. For example, 00:80:2F:AB:CD:EF:00:01 For the Protoc

Intf.Enet.Time.GMClkID

This property provides the Clock ID of the currently selected grandmaster for this
 clock.

The Grandmaster Clock ID is returned as a string of eight octets. Each octet consists of
 two hexadecimal (0-9, A-F) digits. The octets are separated by colon. For example,
 00:80:2F:AB:CD:EF:00:01

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **grandmasterIdentity** attribute, specified in 14.4.3
 of IEEE Std 802.1AS-2011. This property also uses the
 **gmPresent** Boolean specified in 10.2.3.13 of IEEE
 Std 802.1AS-2011. If **gmPresent** is True, this property
 returns the Clock ID of the grandmaster. If **gmPresent**
 is False, this property returns the Clock ID of the XNET Interface. If
 grandmaster information has not been received (e.g., Protocol Enabled is False,
 or BMCA is disabled and the slave does not receive announce messages), this
 property returns the invalid value of all zeroes.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-gmclockoffvar-1000ce.html language=enus -->
## TOPIC 00089: Intf.Enet.Time.GMClkOffVar

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-gmclockoffvar-1000ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-gmclockoffvar-1000ce.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the Clock Offset Scaled Log Variance of the currently selected grandmaster for this clock. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the grandmasterOffsetScaledLogVariance attribute, specified in 14.4.6 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.GMClkOffVar

Provides the Clock Offset Scaled Log Variance of the currently selected grandmaster
 for this clock.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **grandmasterOffsetScaledLogVariance** attribute, specified in
 14.4.6 of IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-offset-91000c3.html language=enus -->
## TOPIC 00090: Intf.Enet.Time.OffMaster

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-offset-91000c3.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-offset-91000c3.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the positive or negative offset in time between this clock and the grandmaster. Offset From Master can be used to determine when this XNET interface is sufficiently synchronized to the grandmaster in order to continue. The time synchronization protocol specifies that this offset is received

Intf.Enet.Time.OffMaster

Provides the positive or negative offset in time between this clock and the
 grandmaster.

Offset From Master can be used to determine when this XNET
 interface is sufficiently synchronized to the grandmaster in order to continue.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

When Port State is Master, this XNET interface acts as grandmaster, and
 therefore this property returns 0.0.

For the Protocol of IEEE Std
 802.1AS-2011, this property corresponds to the offsetFromMaster parameter as
 described in 14.3.2 of IEEE Std 802.1AS-2011.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-ann-receipt-timeout-1000e0.html language=enus -->
## TOPIC 00091: Intf.Enet.Time.Port.AnnTmout

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-ann-receipt-timeout-1000e0.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-ann-receipt-timeout-1000e0.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: If Port State is Slave, this property configures the number of announce intervals to wait without receiving an announce message before assuming that the neighboring Master is no longer available and that the best master clock algorithm (BMCA) needs to run, if enabled. For the Protocol of IEEE Std 80

Intf.Enet.Time.Port.AnnTmout

If **Port State** is Slave, this property configures the number
 of announce intervals to wait without receiving an announce message before assuming that
 the neighboring Master is no longer available and that the best master clock algorithm
 (BMCA) needs to run, if enabled.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **announceReceiptTimeout** parameter as described in 14.6.13 of
 IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-annintvl-1000de.html language=enus -->
## TOPIC 00092: Intf.Enet.Time.Port.AnnIntvl

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-annintvl-1000de.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-annintvl-1000de.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: If Announce Transmit Enabled? is True, this property provides the current interval used for successive transmissions of the announce message by this port. According to the standards, a message transmission interval is a signed integer in the range -128 to 127, represented as the logarithm to the bas

Intf.Enet.Time.Port.AnnIntvl

If Announce Transmit Enabled? is True, this property provides
 the current interval used for successive transmissions of the announce message by this
 port.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

According to the standards, a message transmission interval is a signed integer
 in the range -128 to 127, represented as the logarithm to the base 2 of the time
 interval measured in seconds. For example, value 0 is 1 second, and value -3 is
 125 milliseconds. In LabVIEW, the interval is provided as a ring (enumerated
 list) for usability.

| Enumeration | Value | Description |
| --- | --- | --- |
| 125 milliseconds | -3 | Message transmission interval of 125 milliseconds. |
| 250 milliseconds | -2 | Message transmission interval of 250 milliseconds. |
| 500 milliseconds | -1 | Message transmission interval of 500 milliseconds. This value is supported on all NI products. |
| 1 second | 0 | Message transmission interval of 1 second. This value is supported on all NI products. |
| 2 seconds | 1 | Message transmission interval of 2 second. This value is supported on all NI products. |

The LabVIEW ring is limited to values that are practical in implementation, but
 not all values are supported for all NI products. All NI products support the
 values listed as such in the table.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **currentLogAnnounceInterval** parameter as described in
 14.6.12 of IEEE Std 802.1AS-2011. If the optional Signaling message is used in
 the network, the **currentLogAnnounceInterval** parameter can
 be different from its initial value (see Log Announce Interval Configured).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-log-pdlyintvlconf-1000d8.html language=enus -->
## TOPIC 00093: Intf.Enet.Time.Port.PdlyIntvlConf

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-log-pdlyintvlconf-1000d8.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-log-pdlyintvlconf-1000d8.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: If the Pdelay Enabled? property is True, this property configures the interval between successive transmissions of the Pdelay_Req message by this port. According to the standards, a message transmission interval is a signed integer in the range -128 to 127, represented as the logarithm to the base 2

Intf.Enet.Time.Port.PdlyIntvlConf

If the Pdelay Enabled? property is True, this property
 configures the interval between successive transmissions of the Pdelay_Req message by
 this port.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

According to the standards, a message transmission interval is a signed integer
 in the range -128 to 127, represented as the logarithm to the base 2 of the time
 interval measured in seconds. For example, value 0 is 1 second, and value -3 is
 125 milliseconds. In LabVIEW, the interval is provided as a ring (enumerated
 list) for usability.

| Enumeration | Value | Description |
| --- | --- | --- |
| 125 milliseconds | -3 | Message transmission interval of 125 milliseconds. |
| 250 milliseconds | -2 | Message transmission interval of 250 milliseconds. |
| 500 milliseconds | -1 | Message transmission interval of 500 milliseconds. This value is supported on all NI products. |
| 1 second | 0 | Message transmission interval of 1 second. This value is supported on all NI products. |
| 2 seconds | 1 | Message transmission interval of 2 second. This value is supported on all NI products. |

The LabVIEW ring is limited to values that are practical in implementation, but
 not all values are supported for all NI products. All NI products support the
 values listed as such in the table.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **initialLogPdelayReqInterval** parameter as described
 in 14.6.18 of IEEE Std 802.1AS-2011. The
 **initialLogPdelayReqInterval** parameter is used for
 the initial transmit interval of Pdelay_Req, but
 afterward the interval can only be changed by receiving a special Signaling
 message from the neighboring clock (see 10.5.4.3 of IEEE Std 802.1AS-2011). The
 Signaling message is optional, and if not used in the network, this property
 configures the interval exclusively.

When an XNET session is started on a port that is set to Tap mode, this property
 becomes read only and its value cannot be modified.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-log-syncintvlconf-1000da.html language=enus -->
## TOPIC 00094: Intf.Enet.Time.Port.SyncIntvlConf

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-log-syncintvlconf-1000da.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-log-syncintvlconf-1000da.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: If Port State is Master, this property configures the interval between successive transmissions of the sync message by this port. According to the standards, a message transmission interval is a signed integer in the range -128 to 127, represented as the logarithm to the base 2 of the time interval

Intf.Enet.Time.Port.SyncIntvlConf

If Port State is Master, this property configures the interval
 between successive transmissions of the sync message by this port.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

According to the standards, a message transmission interval is a signed integer
 in the range -128 to 127, represented as the logarithm to the base 2 of the time
 interval measured in seconds. For example, value 0 is 1 second, and value -3 is
 125 milliseconds. In LabVIEW, the interval is provided as a ring (enumerated
 list) for usability.

| Enumeration | Value | Description |
| --- | --- | --- |
| 125 milliseconds | -3 | Message transmission interval of 125 milliseconds. |
| 250 milliseconds | -2 | Message transmission interval of 250 milliseconds. |
| 500 milliseconds | -1 | Message transmission interval of 500 milliseconds. This value is supported on all NI products. |
| 1 second | 0 | Message transmission interval of 1 second. This value is supported on all NI products. |
| 2 seconds | 1 | Message transmission interval of 2 second. This value is supported on all NI products. |

The LabVIEW ring is limited to values that are practical in implementation, but
 not all values are supported for all NI products. All NI products support the
 values listed as such in the table.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **initialLogSyncInterval** parameter as described in
 14.6.14 of IEEE Std 802.1AS-2011. The
 **initialLogSyncInterval** parameter is used for the
 initial transmit interval of Synch, but afterward the interval can only be
 changed by receiving a special Signaling message from the neighboring clock (see
 10.5.4.3 of IEEE Std 802.1AS-2011). The Signaling message is optional, and if
 not used in the network, this property configures the interval exclusively.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-log-synctmout-1000dc.html language=enus -->
## TOPIC 00095: Intf.Enet.Time.Port.SyncTmout

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-log-synctmout-1000dc.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-log-synctmout-1000dc.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: If Port State is Slave, this property configures the number of sync intervals to wait without receiving a sync message before assuming that the neighboring Master is no longer available and that the best master clock algorithm (BMCA) needs to run, if enabled. For the Protocol of IEEE Std 802.1AS-201

Intf.Enet.Time.Port.SyncTmout

If Port State is Slave, this property configures the number of
 sync intervals to wait without receiving a sync message before assuming that the
 neighboring Master is no longer available and that the best master clock algorithm
 (BMCA) needs to run, if enabled.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **syncReceiptTimeout** parameter as described in 14.6.16 of IEEE
 Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-pdelay-enabled-21000d7.html language=enus -->
## TOPIC 00096: Intf.Enet.Time.Port.Pdly?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-pdelay-enabled-21000d7.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-pdelay-enabled-21000d7.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables the exchange of Pdelay (peer-to-peer delay) messages, as a means of measuring Propagation Delay. When Pdelay Enabled? is True, the port transmits Pdelay request messages (Pdelay_Req) to the neighboring clock and processes received Pdelay response messages (Pdelay_Resp). The port also process

Intf.Enet.Time.Port.Pdly?

Enables the exchange of Pdelay (peer-to-peer delay) messages, as a means of measuring
 Propagation Delay.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

When Pdelay Enabled? is True, the port transmits Pdelay
 request messages (Pdelay_Req) to the neighboring clock and processes received
 Pdelay response messages (Pdelay_Resp). The port also processes received Pdelay
 request messages and transmits Pdelay response messages. The Propagation Delay
 is measured using this message exchange. The Propagation
 Delay Configured property is not used while Pdelay is enabled.

When this property is False, Pdelay messages are not transmitted, and received
 Pdelay messages are ignored. The false value is useful for in-vehicle
 applications in which the topology for time synchronization is considered to be
 part of the vehicle's static design. The Propagation Delay Configured property
 must be used in order to specify the propagation delay for the port. The
 read-only Propagation Delay property reflects Propagation Delay Configured.

For the Protocol of IEEE Std 802.1AS-2011, a property value of true corresponds
 to propagation delay measurement as described in 11.1.2 of IEEE Std
 802.1AS-2011. A property value of false is not specified in IEEE Std
 802.1AS-2011. Behavior analogous to a property value of false is specified for
 802.1AS as part of the AUTOSAR Specification of Time Synchronization over
 Ethernet, and the Avnu Automotive Ethernet AVB Functional and Interoperability
 Specification.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-propdelay-11000d4.html language=enus -->
## TOPIC 00097: Intf.Enet.Time.Port.PropDly

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-propdelay-11000d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-propdelay-11000d4.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the propagation delay for the Ethernet cable between this clock and its neighboring clock. Propagation delay is the time it takes for a single bit to travel along the wire (i.e., PHY to PHY). Propagation delay is a fundamental measurement that is required for time synchronization. This prop

Intf.Enet.Time.Port.PropDly

Provides the propagation delay for the Ethernet cable between this clock and its
 neighboring clock.

Propagation delay is the time it takes for a single bit to travel along the wire (i.e.,
 PHY to PHY). Propagation delay is a fundamental measurement that is required for time
 synchronization.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

This property uses a double-precision floating-point, and the value is provided
 in seconds, which is typically used in LabVIEW for relative times. To convert
 the value to nanoseconds, multiply this property value by 1,000,000,000.

The propagation speed for copper wires is close to 2 * 10^8 meters/second (5
 nanoseconds/meter). Therefore, multiplying this property value by 200,000,000
 provides a close approximation of the cable length in meters. For example, 800
 nanoseconds of propagation delay occurs with approximately 160 meters of copper
 cable.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **neighborPropDelay** attribute, specified in 14.6.7 of
 IEEE Std 802.1AS-2011.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-propdelayconf-11000d5.html language=enus -->
## TOPIC 00098: Intf.Enet.Time.Port.PropDlyConf

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-propdelayconf-11000d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-propdelayconf-11000d5.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the Propagation Delay when Pdelay Enabled? is False. If Pdelay Enabled? is True, the value in this property is ignored.

Intf.Enet.Time.Port.PropDlyConf

Configures the Propagation Delay when Pdelay
 Enabled? is False. If Pdelay Enabled? is True,
 the value in this property is ignored.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-propdelayth-11000d6.html language=enus -->
## TOPIC 00099: Intf.Enet.Time.Port.PropDlyTh

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-propdelayth-11000d6.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-propdelayth-11000d6.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Sets the threshold for the Propagation Delay property. For IEEE Std 802.1AS, if the Propagation Delay exceeds the threshold in this property, the protocol assumes that a switch or router that is not 802.1AS-capable exists between this clock and the neighboring 802.1AS-capable clock. The resulting as

Intf.Enet.Time.Port.PropDlyTh

Sets the threshold for the Propagation Delay
 property.

For IEEE Std 802.1AS, if the Propagation Delay exceeds the threshold in this property,
 the protocol assumes that a switch or router that is not 802.1AS-capable exists between
 this clock and the neighboring 802.1AS-capable clock. The resulting asymmetries would
 have an adverse effect on time synchronization accuracy, so this port sets AS Capable? to
 False. If Pdelay
 Enabled? is False, this property is ignored.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Propagation Delay Threshold uses a double-precision
 floating-point, and the value is provided in seconds, which is typically used in
 LabVIEW for relative times. To convert the value to nanoseconds, multiply this
 property value by 1000000000 (for read).

The propagation speed for copper wires is close to 2 * 10^8 meters/second (5
 nanoseconds/meter). Therefore, multiplying this property value by 200000000
 provides a close approximation of the cable length in meters. For example, 800
 nanoseconds of propagation delay occurs with approximately 160 meters of copper
 cable.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **neighborPropDelayThresh** parameter, specified in
 14.6.8 of IEEE Std 802.1AS-2011. The default value is specified in IEEE Std
 802.1AS-2011/Cor1-2013. When an XNET session is started on a port that is set to
 Tap mode, this property becomes read only and its value cannot be modified.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-state-1000d3.html language=enus -->
## TOPIC 00100: Intf.Enet.Time.Port.PortSt

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-state-1000d3.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-state-1000d3.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the current state of the port. This property uses a ring (enumerated list) with the following values: Enumeration Value Description Disabled 3 The protocol is disabled on the port. No protocol messages are transmitted in this state. The port discards received messages for the protocol. The

Intf.Enet.Time.Port.PortSt

Provides the current state of the port.

This property uses a ring (enumerated list) with the following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| Disabled | 3 | The protocol is disabled on the port. No protocol messages are transmitted in this state. The port discards received messages for the protocol. The port is in this state when Protocol Enabled? is False. |
| Master | 6 | Port is sending time. If the clock has only one port, the port is acting as grandmaster. |
| Passive | 7 | Port is exchanging messages to measure Propagation Delay but is not sending time (Master) or receiving time (Slave). |
| Slave | 9 | Port is receiving time. In IEEE Std 802.1AS, the port is not necessarily synchronized (calibrated). In IEEE Std 1588, the port is assumed to be synchronized. |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **portRole** parameter, specified in 14.6.3 of IEEE Std
 802.1AS-2011, which in turn references 8.2.5.3.1 of IEEE Std 1588-2008. The only
 valid values for IEEE Std 802.1AS-2011 are Disabled,
 Master, Slave, and
 Passive.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-state-config-1000d2.html language=enus -->
## TOPIC 00101: Intf.Enet.Time.Port.PortStConf

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-state-config-1000d2.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-state-config-1000d2.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the Port State when BMCA Enabled? is False. Valid values are Master and Slave. If BMCA Enabled? is True, the value in this property is ignored. When an XNET session is started on a port that is set to Tap mode, this property becomes read only and its value cannot be modified.

Intf.Enet.Time.Port.PortStConf

Configures the Port State when BMCA
 Enabled? is False. Valid values are Master and
 Slave.

If **BMCA Enabled?** is True, the value in this property is ignored.

When an XNET session is started on a port that is set to Tap mode, this property becomes
 read only and its value cannot be modified.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-stats-ctrnames-41000e3.html language=enus -->
## TOPIC 00102: Intf.Enet.Time.Port.St.CtrNames

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-stats-ctrnames-41000e3.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-stats-ctrnames-41000e3.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the name of each Ethernet statistics property supported by XNET. The name uses uppercase for the first letter of each word, with space as a separator between words. The name at a specific index corresponds to the counter at the same index in Counter Values. The array of strings for this prop

Intf.Enet.Time.Port.St.CtrNames

Returns the name of each Ethernet statistics property supported by
 XNET.

The name uses uppercase for the first letter of each word, with space as a separator
 between words.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

The name at a specific index corresponds to the counter at the same index in
 Counter Values. The array of strings for this property is the same size as the
 Counter
 Values array of strings.

The Counter Names and Counter
 Values properties are intended to be used together to display
 all statistics on the front panel. These properties do not require knowledge of
 specific property names. For example, if a new version of NI-XNET adds a
 statistic property (to the end of the arrays), the new property will display
 without change to your LabVIEW application. Statistics are grouped as receive
 (rx) and transmit (tx).

When the Port Mode of the session's interface is set to Direct, receive and
 transmit are relative to that interface.

When the Port Mode is set to Tap, receive statistics refer to this session's
 interface, and all transmit statistics are zero. If you want to get statistics
 for frames received by the Tap partner, use a session with the Tap partner's
 interface.

All statistics reset to zero when the system powers up or the device is reset.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-stats-rxann-91000e6.html language=enus -->
## TOPIC 00103: Intf.Enet.Time.Port.St.RxAnn

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-stats-rxann-91000e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-stats-rxann-91000e6.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: A count of the number of announce messages received. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the rxAnnounceCount parameter as described in 14.7.7 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.Port.St.RxAnn

A count of the number of announce messages received.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **rxAnnounceCount** parameter as described in 14.7.7 of IEEE Std
 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-stats-rxpdreq-91000e7.html language=enus -->
## TOPIC 00104: Intf.Enet.Time.Port.St.RxPDReq

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-stats-rxpdreq-91000e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-stats-rxpdreq-91000e7.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: A count of the number of Pdelay_Req messages received. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the rxPdelayRequestCount parameter as described in 14.7.4 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.Port.St.RxPDReq

A count of the number of Pdelay_Req messages received.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **rxPdelayRequestCount** parameter as described in 14.7.4 of IEEE
 Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-stats-rxsync-91000e5.html language=enus -->
## TOPIC 00105: Intf.Enet.Time.Port.St.RxSync

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-stats-rxsync-91000e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-stats-rxsync-91000e5.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: A count of the number of Sync messages received. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the rxSyncCount parameter as described in 14.7.2 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.Port.St.RxSync

A count of the number of Sync messages received.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **rxSyncCount** parameter as described in 14.7.2 of IEEE Std
 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-stats-txpdreq-91000ea.html language=enus -->
## TOPIC 00106: Intf.Enet.Time.Port.St.TxPDReq

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-stats-txpdreq-91000ea.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-stats-txpdreq-91000ea.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: A count of the number of Pdelay_Req messages transmitted. For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the txPdelayRequestCount parameter as described in 14.7.14 of IEEE Std 802.1AS-2011.

Intf.Enet.Time.Port.St.TxPDReq

A count of the number of Pdelay_Req messages transmitted.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the
 **txPdelayRequestCount** parameter as described in 14.7.14 of
 IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-synced-21000e2.html language=enus -->
## TOPIC 00107: Intf.Enet.Time.Port.Sync?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-synced-21000e2.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-synced-21000e2.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether the clock using the time synchronization protocol is successfully synchronized to other clocks in the network. Time synchronization occurs independently from start of the interface. For example, you can read and write Ethernet frames when time sync is not enabled, or when the time

Intf.Enet.Time.Port.Sync?

Indicates whether the clock using the time synchronization protocol is successfully
 synchronized to other clocks in the network.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

For the Protocol of IEEE Std 802.1AS-2011, this property is True when AS
 Capable is True and the following conditions apply:

- If Port
 State is Slave, XNET clock adjustment algorithm (servo) is in its
 final stage (calibrated). Sufficient messages have been exchanged such that
 synchronization quality (e.g., Offset From Master) is unlikely to improve
 significantly, but no fixed metric is applied as a threshold.
- If Port State is Master and best master clock algorithm (BMCA) is
 enabled, at least two announce intervals have elapsed. Master state means
 that the XNET port is acting as grandmaster (the source of time in the
 network), so Synced? would normally be true
 immediately. When using the BMCA, the XNET port initializes assuming that it
 is a potential grandmaster (Master), but when it receives an announce
 message from a better grandmaster, the Port State changes to Slave. By
 waiting up to two announce intervals, the XNET port avoids reporting a
 false-positive from Synced? (i.e., true because it
 was Master upon initialization, then false when a better grandmaster is
 detected, and then true again after slave calibration).
- If Port State is Master and BMCA is disabled,
 Synced? is true immediately. As BMCA is disabled,
 this XNET port will act as the Master (grandmaster) indefinitely.

In the IEEE 1588-2008 standard (on which IEEE Std 802.1AS-2011 is based), this
 Synced? flag is analogous to transition out of the
 UNCALIBRATED state. For 802.1AS, behavior similar to this property is specified
 as the AVB_Sync state of the Avnu Automotive Ethernet AVB Functional and
 Interoperability Specification.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-port-syncstatus-1000f0.html language=enus -->
## TOPIC 00108: Intf.Enet.Time.Port.SyncStat

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-port-syncstatus-1000f0.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-port-syncstatus-1000f0.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the current synchronization status of the time synchronization protocol. This property uses a ring (enumerated list) with the following values. Enumeration Value Description Synced 0 The clock using the time synchronization protocol is successfully synchronized with other clocks in the netw

Intf.Enet.Time.Port.SyncStat

Provides the current synchronization status of the time synchronization
 protocol.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

This property uses a ring (enumerated list) with the following values.

| Enumeration | Value | Description |
| --- | --- | --- |
| Synced | 0 | The clock using the time synchronization protocol is successfully synchronized with other clocks in the network. This value is returned when the time synchronization protocol's Synced property is True. |
| EnetLinkDown | 1 | The interface cannot transmit or receive frames (packets). |
| ProtocolDisabled | 2 | Time synchronization protocol is disabled. |
| MeasuringPropDelay | 3 | The port is exchanging messages to measure Propagation Delay, but the port is not sending time (master) or receiving time (slave). |
| MasterPendingAnnounce | 4 | The Port State is master with the BMCA enabled and is waiting until at least two Announce Intervals have elapsed before declaring the port synchronized. This avoids reporting a false-positive when the best master clock algorithm (BMCA) has not finished electing the best master. |
| WaitingForMaster | 5 | The Port State is slave and a sync message has not been received from the master. |
| SyncingToMaster | 6 | The Port State is slave and the XNET clock adjustment algorithm (servo) has not reached its final state (calibrated). A sufficient number of messages need to be exchanged so that synchronization quality (e.g., Offset From Master) is unlikely to improve significantly, but no fixed metric is applied as a threshold. |
| PeerNotProtoCapable | 7 | The time synchronization protocol is not detecting a neighbor that is running the protocol according to the requirements in the standard. |
| PropDelayExceedsTreshold | 8 | For IEEE Std 802.1AS, the measured propagation delay exceeds the value specified by the property Propagation Delay Threshold. As a result, the time synchronization protocol sets the AS Capable? property to False. |
| SyncReceiptTimeout | 9 | The Port State is slave and the time synchronization protocol has not received a sync message from the Master in at least the number of sync intervals specified by the Sync Receipt Timeout property. |
| FrequencyOutOfRange | 10 | The Port State is slave and the grandmaster clock has exceeded the frequency range of the XNET clock (±100 ppm). |
| SyncIntervalOutOfRange | 11 | The Port State is slave and the master is sending sync messages outside of the supported sync interval range. |
| MultipleMastersDetected | 12 | The Port State is configured as master with the BMCA disabled and another master has been detected by the time synchronization protocol. |

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-priority1-1000c8.html language=enus -->
## TOPIC 00109: Intf.Enet.Time.Pri1

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-priority1-1000c8.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-priority1-1000c8.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: The best master clock algorithm (BMCA) uses this property as the first comparison to determine the grandmaster. Lower values take precedence. Valid values range from 0 to 255. The value 255 specifies that the clock is not grandmaster-capable (slave only). For example, if you write this property to z

Intf.Enet.Time.Pri1

The best master clock algorithm (BMCA) uses this property as the first comparison to
 determine the grandmaster. Lower values take precedence.

Valid values range from 0 to 255. The value 255 specifies that the clock is not
 grandmaster-capable (slave only). For example, if you write this property to zero, and
 all other clocks in the network have a Priority1 greater than zero, this clock is likely
 to be selected as grandmaster.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the priority1
 attribute, specified in 14.2.6 of IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-priority2-1000c9.html language=enus -->
## TOPIC 00110: Intf.Enet.Time.Pri2

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-priority2-1000c9.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-priority2-1000c9.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: The best master clock algorithm (BMCA) uses this property as a secondary comparison, after comparing the properties for clock quality, and before using Clock ID as a tie-breaker. Lower values take precedence. Valid values range from 0 to 255. For the Protocol of IEEE Std 802.1AS-2011, this property

Intf.Enet.Time.Pri2

The best master clock algorithm (BMCA) uses this property as a secondary comparison,
 after comparing the properties for clock quality, and before using Clock
 ID as a tie-breaker. Lower values take precedence.

Valid values range from 0 to 255.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the priority1
 attribute, specified in 14.2.6 of IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-proten-21000c1.html language=enus -->
## TOPIC 00111: Intf.Enet.Time.ProtEn?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-proten-21000c1.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-proten-21000c1.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Enables (runs) or disables the time synchronization protocol. When this property is True, the protocol transmits and receives messages in order to synchronize time with its neighboring ports. When this property is False, the protocol does not transmit messages, and messages received for the protocol

Intf.Enet.Time.ProtEn?

Enables (runs) or disables the time synchronization protocol.

When this property is True, the protocol transmits and receives messages
 in order to synchronize time with its neighboring ports.

When this property is False, the protocol does not transmit messages,
 and messages received for the protocol are ignored.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

This property must be written to false prior to changing the value of the Protocol property. All other writable Time Sync properties can be
 changed while this property is True.

The Protocol Enabled? property is created only when at
 least one XNET Session exists on the Ethernet interface; therefore, this
 property is effectively False when no XNET Session is created. The time
 synchronization protocol does not run outside the context of XNET sessions.

This property is not associated with the state of input/output on the session
 (refer to State Models). It is possible to enable the time synchronization
 protocol prior to starting the session (e.g., to wait for Synced? to equal True prior to timestamping received frames). It is
 also possible to start the session with the time synchronization protocol
 disabled, in which case frames from [Read (Frame
 Ethernet)](/csh?topicname=xnet-read-frame-ethernet.html) contain a **network synced?** flag of
 False.

For the Protocol of IEEE Std 802.1AS-2011, a property value of True
 corresponds to running the clock's protocol, as described in 7.4 of IEEE Std
 802.1AS-2011. A property value of True does not necessarily indicate that time
 is synchronized with the neighboring port. The AS
 Capable property is used to determine if the neighboring port is
 running 802.1AS.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-protocol-1000c0.html language=enus -->
## TOPIC 00112: Intf.Enet.Time.Prot

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-protocol-1000c0.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-protocol-1000c0.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the time synchronization protocol that the clock is using. This protocol is indicated in all time sync messages that are transmitted by the session's interface (port). The Protocol property uses a ring (enumerated list) with the following values: Enumeration Value Description IEEE Std 802.

Intf.Enet.Time.Prot

Specifies the time synchronization protocol that the clock is using.

This protocol is indicated in all time sync messages that are transmitted by the
 session's interface (port). The Protocol property uses a ring
 (enumerated list) with the following values:

| Enumeration | Value | Description |
| --- | --- | --- |
| IEEE Std 802.1AS-2011 | 0 | IEEE Standard 802.1AS-2011: Timing and Synchronization for Time-Sensitive Applications in Bridged Local Area Networks. |

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-ethernet-timesync-stepsgm-1000ca.html language=enus -->
## TOPIC 00113: Intf.Enet.Time.StepsGM

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-ethernet-timesync-stepsgm-1000ca.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-ethernet-timesync-stepsgm-1000ca.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates the number of steps that this clock is removed from the grandmaster. For example, if there is a single Ethernet cable that connects this clock to the grandmaster, this property returns the value 1. The best master clock algorithm (BMCA) uses this property for topology analysis. If two pote

Intf.Enet.Time.StepsGM

Indicates the number of steps that this clock is removed from the grandmaster. For
 example, if there is a single Ethernet cable that connects this clock to the
 grandmaster, this property returns the value 1.

The best master clock algorithm (BMCA) uses this property for topology analysis. If two
 potentially equal grandmasters provide the same timescale, the BMCA can select the one
 that is closer, with the rationale that each step has an adverse effect on accuracy.

For the Protocol of IEEE Std 802.1AS-2011, this property corresponds to the stepsRemoved
 attribute, specified in 14.3.1 of IEEE Std 802.1AS-2011.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-accepted-startup-range-100030.html language=enus -->
## TOPIC 00114: Intf.FlexRay.AccStartRng

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-accepted-startup-range-100030.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-accepted-startup-range-100030.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Range of clock deviation allowed for startup frames during node integration. Expressed in microticks (0–1875). This property corresponds to the pdAcceptedStartupRange node parameter in the FlexRay Protocol Specification. You can overwrite the default value by writing a value within the specified ran

Intf.FlexRay.AccStartRng

Range of clock deviation allowed for startup frames during node integration.
 Expressed in microticks (0–1875).

This property corresponds to the **pdAcceptedStartupRange** node parameter in the *FlexRay
 Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-allow-halt-due-to-clock-2100031.html language=enus -->
## TOPIC 00115: Intf.FlexRay.AlwHltClk?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-allow-halt-due-to-clock-2100031.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-allow-halt-due-to-clock-2100031.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Controls the transition of the interface to the POC:halt-state due to a clock synchronization errors (boolean). If set to true, the node can transition to the POC: halt state. If set to false, the node does not transition to the POC: halt state and remains in the POC: normal passive state, allowing

Intf.FlexRay.AlwHltClk?

Controls the transition of the interface to the POC:halt-state due to a clock
 synchronization errors (boolean).

If set to true, the node can transition to the POC: halt state. If set to false, the node
 does not transition to the POC: halt state and remains in the POC: normal passive state,
 allowing for self recovery.

This property corresponds to the **pAllowHaltDueToClock** node parameter
 in the *FlexRay Protocol Specification*.

The property is a Boolean flag. The default value of this property is false.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface. Refer to [XNET Read (State FlexRay Comm)](/csh?topicname=xnet-read-state-flexray-comm.html) for more information about the POC: halt and POC: normal passive states.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-allow-passive-to-active-100032.html language=enus -->
## TOPIC 00116: Intf.FlexRay.AlwPassAct

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-allow-passive-to-active-100032.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-allow-passive-to-active-100032.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of consecutive even/odd cycle pairs that must have valid clock correction terms before the FlexRay node can transition from the POC: normal-passive to the POC: normal-active state. The property is expressed as the number of even/odd cycle pairs, with values of 0–31. If set to zero, the node c

Intf.FlexRay.AlwPassAct

Number of consecutive even/odd cycle pairs that must have valid clock correction
 terms before the FlexRay node can transition from the POC: normal-passive to the POC:
 normal-active state. The property is expressed as the number of even/odd cycle pairs,
 with values of 0–31.

If set to zero, the node cannot transition from POC: normal-passive to POC:
 normal-active.

This property corresponds to the **pAllowPassiveToActive** node parameter
 in the *FlexRay Protocol Specification*.

The default value of this property is zero.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

Refer to [XNET Read (State FlexRay Comm)](/csh?topicname=xnet-read-state-flexray-comm.html) for more information about the POC:
 normal-active and POC: normal-passive states.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-auto-asleep-when-stopped-210003a.html language=enus -->
## TOPIC 00117: Intf.Flexray.AutoAslpWhnStp?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-auto-asleep-when-stopped-210003a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-auto-asleep-when-stopped-210003a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies whether the FlexRay interface (node) automatically places the FlexRay transceiver and controller into sleep when the interface is stopped. The default value of this property is False, and you must handle the wakeup/sleep processing manually using the XNET Session Interface:FlexRay:Sleep pr

Intf.Flexray.AutoAslpWhnStp?

Specifies whether the FlexRay interface (node) automatically places the FlexRay
 transceiver and controller into sleep when the interface is stopped.

The default value of this property is False, and you must handle the wakeup/sleep processing
 manually using the XNET Session Interface:FlexRay:Sleep
 property.

When this property is called with the value True while the interface is asleep, the
 interface is put to sleep immediately. When this property is called with the value
 False, the interface is set to a local awake state immediately.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

If the interface is asleep when [XNET
 Start](/csh?topicname=xnet-start.html) is called, the FlexRay interface waits for a wakeup pattern
 on the bus before transitioning out of the POC:READY state. To initiate a bus
 wakeup, you can set the XNET Session Interface:FlexRay:Sleep property with a value of Remote Wake.

After [XNET
 Stop](/csh?topicname=xnet-stop.html) is called, if this property is True, the FlexRay interface
 automatically goes back to sleep to be ready to handle the wakeup on subsequent
 XNET Start calls. When this property is False when XNET Stop is called, the
 FlexRay interface remains in the sleep state it was in prior to the XNET Stop
 call.

You can overwrite the default value by writing this property prior to starting
 the FlexRay interface.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-cluster-drift-damping-100033.html language=enus -->
## TOPIC 00118: Intf.FlexRay.ClstDriftDmp

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-cluster-drift-damping-100033.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-cluster-drift-damping-100033.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Local cluster drift damping factor used for rate correction. The range for the property is 0–20 MT. This property corresponds to the pAllowPassiveToActive node parameter in the FlexRay Protocol Specification. The cluster drift damping property should be configured in such a way that the damping valu

Intf.FlexRay.ClstDriftDmp

Local cluster drift damping factor used for rate correction. The range for the
 property is 0–20 MT.

This property corresponds to the **pAllowPassiveToActive** node parameter
 in the *FlexRay Protocol Specification*.

The cluster drift damping property should be configured in such a way that the damping
 values in all nodes within the same cluster have approximately the same duration.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-coldstart-2100034.html language=enus -->
## TOPIC 00119: Intf.FlexRay.Coldstart?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-coldstart-2100034.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-coldstart-2100034.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether the FlexRay interface operates as a coldstart node on the cluster (boolean). This property is read-only, and is calculated from the Key Slot Identifier property. If the KeySlot Identifier is 0 (invalid slot identifier), the XNET FlexRay interface does not act as a coldstart node, a

Intf.FlexRay.Coldstart?

Indicates whether the FlexRay interface operates as a coldstart node on the cluster
 (boolean).

This property is read-only, and is calculated from the Key Slot
 Identifier property.

If the KeySlot Identifier is 0 (invalid slot identifier), the XNET FlexRay interface does not act as a coldstart node, and this property is false. If the KeySlot Identifier is 1 or more, the XNET FlexRay interface transmits a startup frame from that slot, and the Interface:FlexRay:Coldstart? property is true.

This property returns a Boolean flag (true/false). The default value of this property is false.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-connected-channels-10003c.html language=enus -->
## TOPIC 00120: Intf.FlexRay.ConnectedChs

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-connected-channels-10003c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-connected-channels-10003c.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: This property specifies the channel(s) that the FlexRay interface (node) is physically connected to. The default value of this property is all channels available on the cluster. However, if you are using a node connected to only one channel of a multichannel cluster that uses wakeup, you must set th

Intf.FlexRay.ConnectedChs

This property specifies the channel(s) that the FlexRay interface (node) is physically connected to. The default value of this property is all channels available on the cluster.

However, if you are using a node connected to only one channel of a multichannel cluster
 that uses wakeup, you must set the value properly. If you do not, your node may not wake
 up, as the wakeup pattern cannot be received on a channel not physically connected.

This property corresponds to the **pChannels** node parameter in the
 *FlexRay Protocol Specification*.

The values supported for this property (enumeration) are A = 1, B = 2, and A and B =
 3.

You can overwrite the default value by writing this property prior to starting the
 FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-decoding-correction-100035.html language=enus -->
## TOPIC 00121: Intf.FlexRay.DecCorr

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-decoding-correction-100035.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-decoding-correction-100035.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the value used to calculate the difference between primary time reference point and secondary time reference point (for clock synchronization). Expressed in microticks (14-143). The clock synchronization algorithm uses the primary time reference and the sync frame's expected arrival time t

Intf.FlexRay.DecCorr

Specifies the value used to calculate the difference between primary time reference point and secondary time reference point (for clock synchronization). Expressed in microticks (14-143).

The clock synchronization algorithm uses the primary time reference and the sync frame's
 expected arrival time to calculate and compensate for the node's local clock
 deviation.

This property corresponds to the **pDecodingCorrection** node parameter in
 the *FlexRay Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-delay-compensation-cha-100036.html language=enus -->
## TOPIC 00122: Intf.FlexRay.DelayCompA

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-delay-compensation-cha-100036.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-delay-compensation-cha-100036.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the value that the XNET FlexRay interface (node) uses to compensate for reception delays on channel A. This takes into account the assumed propagation delay up to the maximum allowed propagation delay (cPropagationDelayMax) for microticks in the 0.0125–0.05 range. In practice, you should a

Intf.FlexRay.DelayCompA

Specifies the value that the XNET FlexRay interface (node) uses to compensate for reception delays on channel A.

This takes into account the assumed propagation delay up to the maximum allowed propagation
 delay (cPropagationDelayMax) for microticks in the
 0.0125–0.05 range. In practice, you should apply the minimum of the propagation delays
 of all sync nodes.

This property corresponds to the**pDelayCompensation[A]** node parameter
 in the *FlexRay Protocol Specification*.

The property range is 0–200 MT.

You can overwrite the default value by writing a value within the specified range to this property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-delay-compensation-chb-100037.html language=enus -->
## TOPIC 00123: Intf.FlexRay.DelayCompB

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-delay-compensation-chb-100037.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-delay-compensation-chb-100037.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the value that the XNET FlexRay interface (node) uses to compensate for reception delays on channel B. This takes into account the assumed propagation delay up to the maximum allowed propagation delay (Propagation Delay Max) for microticks in the 0.0125–0.05 range. In practice, you should

Intf.FlexRay.DelayCompB

Specifies the value that the XNET FlexRay interface (node) uses to compensate for reception delays on channel B.

This takes into account the assumed propagation delay up to the maximum allowed propagation
 delay (**Propagation Delay Max**) for microticks in the 0.0125–0.05
 range. In practice, you should apply the minimum of the propagation delays of all sync
 nodes.

This property corresponds to the **pDelayCompensation[B]** node parameter
 in the *FlexRay Protocol Specification*.

The property range is 0–200 MT.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-key-slot-identifier-100038.html language=enus -->
## TOPIC 00124: Intf.FlexRay.KeySlotID

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-key-slot-identifier-100038.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-key-slot-identifier-100038.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the FlexRay slot number from which the NI-XNET FlexRay interface transmits a startup frame, during the process of integration with other cluster nodes. The default value of this property is 0 (no startup frame). For a network (cluster) of FlexRay nodes to start up for communication, at lea

Intf.FlexRay.KeySlotID

Specifies the FlexRay slot number from which the NI-XNET FlexRay interface transmits a startup frame, during the process of integration with other cluster nodes. The default value of this property is 0 (no startup frame).

For a network (cluster) of FlexRay nodes to start up for communication, at least two nodes must transmit startup frames. If your application is designed to test only one external ECU, you must configure the XNET FlexRay interface to transmit a startup frame. If the one external ECU does not transmit a startup frame itself, you must use two XNET FlexRay interfaces for the test, each of which must transmit a startup frame.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

There are two methods for configuring the XNET FlexRay interface as a coldstart node (transmit startup frame).

#### Output Session with Startup Frame

Create an output session that contains a startup frame (or one of its signals). The XNET Frame FlexRay:Startup? property is true for a startup frame. If you use this method, this Key Slot Identifier property contains the identifier property of that startup frame. You do not write this property.

#### Write this Key Slot Identifier Property

This interface uses the identifier (slot) you write to transmit a startup frame using that slot.

Note

You can overwrite the default value by writing an identifier that corresponds to the identifier of a startup frame prior to starting the FlexRay interface.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-latest-tx-100041.html language=enus -->
## TOPIC 00125: Intf.FlexRay.LatestTx

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-latest-tx-100041.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-latest-tx-100041.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of the last minislot in which a frame transmission can start in the dynamic segment (0-7981). This property is read-only, because it is calculated using the frames in the dynamic segment that you specify for transmit. This property corresponds to the pLatestTx node parameter in the FlexRay Pr

Intf.FlexRay.LatestTx

Number of the last minislot in which a frame transmission can start in the dynamic segment (0-7981). This property is read-only, because it is calculated using the frames in the dynamic segment that you specify for transmit.

This property corresponds to the **pLatestTx** node parameter in the
 *FlexRay Protocol Specification*.

This property can be read any time prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-listen-timeout-100042.html language=enus -->
## TOPIC 00126: Intf.FlexRay.ListTimo

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-listen-timeout-100042.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-listen-timeout-100042.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the upper limit for the startup listen timeout and wakeup listen timeout. Expressed in microticks (1284–1283846). Refer to Summary of the FlexRay Standard for more information about startup and wakeup procedures within the FlexRay protocol. This property corresponds to the pdListenTimeout

Intf.FlexRay.ListTimo

Specifies the upper limit for the startup listen timeout and wakeup listen timeout.
 Expressed in microticks (1284–1283846).

Refer to Summary of the FlexRay Standard for more information about startup and wakeup
 procedures within the FlexRay protocol.

This property corresponds to the **pdListenTimeout** node parameter in the
 *FlexRay Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-macro-initial-offset-cha-100043.html language=enus -->
## TOPIC 00127: Intf.FlexRay.MacInitOffA

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-macro-initial-offset-cha-100043.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-macro-initial-offset-cha-100043.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the number of macroticks between the static slot boundary and the following macrotick boundary of the secondary time reference point based on the nominal macrotick duration. Applies to channel A only. Expressed in macroticks (2-72). This property corresponds to the pMacroInitialOffset[A] n

Intf.FlexRay.MacInitOffA

Specifies the number of macroticks between the static slot boundary and the following macrotick boundary of the secondary time reference point based on the nominal macrotick duration. Applies to channel A only. Expressed in macroticks (2-72).

This property corresponds to the **pMacroInitialOffset[A]** node parameter
 in the *FlexRay Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-macro-initial-offset-chb-100044.html language=enus -->
## TOPIC 00128: Intf.FlexRay.MacInitOffB

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-macro-initial-offset-chb-100044.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-macro-initial-offset-chb-100044.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of macroticks between the static slot boundary and the following macrotick boundary of the secondary time reference point based on the nominal macrotick duration. Applies to channel B only. Expressed in macroticks (2-72). This property corresponds to the pMacroInitialOffset[B] node parameter

Intf.FlexRay.MacInitOffB

Number of macroticks between the static slot boundary and the following macrotick boundary of the secondary time reference point based on the nominal macrotick duration. Applies to channel B only. Expressed in macroticks (2-72).

This property corresponds to the **pMacroInitialOffset[B]** node parameter
 in the *FlexRay Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-max-drift-100047.html language=enus -->
## TOPIC 00129: Intf.FlexRay.MaxDrift

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-max-drift-100047.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-max-drift-100047.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the maximum drift offset between two nodes that operate with unsynchronized clocks over one communication cycle. Expressed in microticks (2-1923). This property corresponds to the pdMaxDrift node parameter in the FlexRay Protocol Specification. The range of values for this property is 2–19

Intf.FlexRay.MaxDrift

Specifies the maximum drift offset between two nodes that operate with unsynchronized
 clocks over one communication cycle. Expressed in microticks (2-1923).

This property corresponds to the **pdMaxDrift** node parameter in the
 *FlexRay Protocol Specification*.

The range of values for this property is 2–1923 MT.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-micro-initial-offset-cha-100045.html language=enus -->
## TOPIC 00130: Intf.FlexRay.MicInitOffA

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-micro-initial-offset-cha-100045.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-micro-initial-offset-cha-100045.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the number of microticks between the closest macrotick boundary described by the Macro Initial Offset Ch A Interface property and the secondary time reference point. Applies to channel A only. Expressed in microticks (0-240). This parameter depends on the Interface:FlexRay:Delay Compensati

Intf.FlexRay.MicInitOffA

Specifies the number of microticks between the closest macrotick boundary described
 by the Macro Initial Offset Ch A Interface property and the
 secondary time reference point. Applies to channel A only. Expressed in microticks
 (0-240).

This parameter depends on the Interface:FlexRay:Delay Compensation
 property for Channel A, and therefore you must set it independently for each
 channel.

This property corresponds to the **pMicroInitialOffset[A]** node
 parameter in the *FlexRay Protocol Specification.*

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-micro-initial-offset-chb-100046.html language=enus -->
## TOPIC 00131: Intf.FlexRay.MicInitOffB

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-micro-initial-offset-chb-100046.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-micro-initial-offset-chb-100046.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of microticks between the closest macrotick boundary described by the Macro Initial Offset Ch B Interface property and the secondary time reference point. Applies to channel B only. Expressed in microticks (0-240). This parameter depends on the Interface:FlexRay:Delay Compensation property fo

Intf.FlexRay.MicInitOffB

Number of microticks between the closest macrotick boundary described by the Macro Initial Offset Ch B Interface property and the secondary time reference point. Applies to channel B only. Expressed in microticks (0-240).

This parameter depends on the Interface:FlexRay:Delay Compensation
 property for Channel B, and therefore you must set it independently for each
 channel.

This property corresponds to the **pMicroInitialOffset[B]** node
 parameter in the *FlexRay Protocol Specification.*

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-microtick-100048.html language=enus -->
## TOPIC 00132: Intf.FlexRay.Microtick

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-microtick-100048.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-microtick-100048.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Duration of a microtick, expressed in microseconds. This property is read-only, because it is calculated as a function of the Cluster property Baud Rate and the Interface property Samples Per Microtick. This property corresponds to the pdMicrotick node parameter in the FlexRay Protocol Specification

Intf.FlexRay.Microtick

Duration of a microtick, expressed in microseconds.

This property is read-only, because it is calculated as a function of the Cluster propertyBaud Rate and the Interface property Samples Per Microtick.

This property corresponds to the pdMicrotick node parameter in the *FlexRay Protocol Specification*.

This property can be read any time prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-null-frames-to-input-stream-2100049.html language=enus -->
## TOPIC 00133: Intf.FlexRay.NullToInStrm?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-null-frames-to-input-stream-2100049.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-null-frames-to-input-stream-2100049.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Indicates whether the Frame Input Stream session should return FlexRay null frames from XNET Read>. When this property uses the default value of false, FlexRay null frames are not returned for a Frame Input Stream session. This behavior is consistent with the other two frame input modes (Frame Input

Intf.FlexRay.NullToInStrm?

Indicates whether the Frame Input Stream session should return FlexRay null frames from XNET Read>.

When this property uses the default value of false, FlexRay null frames are not returned for a
 Frame Input Stream session. This behavior is consistent with the other two frame input
 modes (Frame Input Single-Point and Frame Input
 Queued), which never return FlexRay null frames from [XNET Read](/csh?topicname=xnet-read.html).

When you set this property to true for a Frame Input Stream session, [XNET Read](/csh?topicname=xnet-read.html)
 returns all FlexRay null frames that are received by the interface. This feature is used
 to monitor all frames that occur on the network, regardless of whether new payload is
 available or not. When you use the [Frame FlexRay](/csh?topicname=xnet-read-frame-flexray.html)
 instance of [XNET Read](/csh?topicname=xnet-read.html), each frame's type field indicates a null frame.

You can overwrite the default value prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-offset-correction-100058.html language=enus -->
## TOPIC 00134: Intf.FlexRay.OffCorr

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-offset-correction-100058.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-offset-correction-100058.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the maximum permissible offset correction value, expressed in microticks. The offset correction synchronizes the cycle start time. The value indicates the number of microticks added or subtracted to the offset correction portion of the network idle time, to synchronize the interface to the

Intf.FlexRay.OffCorr

Provides the maximum permissible offset correction value, expressed in microticks. The offset correction synchronizes the cycle start time.

The value indicates the number of microticks added or subtracted to the offset correction
 portion of the network idle time, to synchronize the interface to the FlexRay network.
 The value is returned as a signed 32–bit integer (I32). The offset correction value
 calculation takes place every cycle, but the correction is applied only at the end of
 odd cycles. This is a read-only property.

This property can be read anytime prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-offset-correction-out-100050.html language=enus -->
## TOPIC 00135: Intf.FlexRay.OffCorrOut

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-offset-correction-out-100050.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-offset-correction-out-100050.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the magnitude of the maximum permissible offset correction value. Expressed in microticks (5-15266). This node parameter is based on the value of the maximum offset correction for the specific cluster. This property corresponds to the pOffsetCorrectionOut node parameter in the FlexRay Prot

Intf.FlexRay.OffCorrOut

Specifies the magnitude of the maximum permissible offset correction value. Expressed in microticks (5-15266).

This node parameter is based on the value of the maximum offset correction for the
 specific cluster.

This property corresponds to the **pOffsetCorrectionOut** node
 parameter in the *FlexRay Protocol Specification*.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-rate-correction-100059.html language=enus -->
## TOPIC 00136: Intf.FlexRay.RateCorr

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-rate-correction-100059.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-rate-correction-100059.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the rate correction value. Expressed in microticks. The rate correction synchronizes frequency. This property is read-only. The value indicates the number of microticks added to or subtracted from the configured number of microticks in a cycle, to synchronize the interface to the FlexRay ne

Intf.FlexRay.RateCorr

Provides the rate correction value. Expressed in microticks. The rate correction synchronizes frequency. This property is read-only.

The value indicates the number of microticks added to or subtracted from the configured
 number of microticks in a cycle, to synchronize the interface to the FlexRay
 network.

The value is returned as a signed 32-bit integer (I32). The rate correction value
 calculation takes place in the static segment of an odd cycle, based on values measured
 in an even-odd double cycle.

This property can be read prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-rate-correction-out-100052.html language=enus -->
## TOPIC 00137: Intf.FlexRay.RateCorrOut

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-rate-correction-out-100052.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-rate-correction-out-100052.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the magnitude of the maximum permissible rate correction value. Expressed in microticks (2-1923). This node parameter is based on the value of the maximum rate correction for the specific cluster. This property corresponds to the pRateCorrectionOut node parameter in the FlexRay Protocol Sp

Intf.FlexRay.RateCorrOut

Specifies the magnitude of the maximum permissible rate correction value. Expressed in microticks (2-1923).

This node parameter is based on the value of the maximum rate correction for the specific
 cluster.

This property corresponds to the **pRateCorrectionOut** node parameter
 in the *FlexRay Protocol Specification*.

This property is calculated from the microticks per cycle and clock accuracy.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-samples-per-microtick-100053.html language=enus -->
## TOPIC 00138: Intf.FlexRay.SampPerMicro

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-samples-per-microtick-100053.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-samples-per-microtick-100053.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the number of samples per microtick. There is a defined relationship between the "ticks" of the microtick timebase and the sample ticks of bit sampling. Specifically, a microtick consists of an integral number of samples. As a result, there is a fixed phase relationship between the microti

Intf.FlexRay.SampPerMicro

Specifies the number of samples per microtick.

There is a defined relationship between the "ticks" of the microtick timebase and the
 sample ticks of bit sampling. Specifically, a microtick consists of an integral number
 of samples.

As a result, there is a fixed phase relationship between the microtick timebase and the
 sample clock ticks.

This property corresponds to the **pSamplesPerMicrotick** node
 parameter in the *FlexRay Protocol Specification*.

The supported values for this property are 1, 2, and 4 samples.

You can overwrite the default value by writing a value within the specified range to this
 property prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-single-slot-enabled-2100054.html language=enus -->
## TOPIC 00139: Intf.FlexRay.SingSlotEn?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-single-slot-enabled-2100054.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-single-slot-enabled-2100054.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures whether the FlexRay interface (node) should enter single slot mode following startup (boolean). This Boolean property supports a strategy to limit frame transmissions following startup to a single frame (designated by the XNET Session Interface:FlexRay:Key Slot Identifier property). If yo

Intf.FlexRay.SingSlotEn?

Configures whether the FlexRay interface (node) should enter single slot mode following startup (boolean).

This Boolean property supports a strategy to limit frame transmissions following startup
 to a single frame (designated by the XNET Session Interface:FlexRay:Key Slot Identifier property). If you leave this property
 false prior to start (default), all configured output frames transmit. If you set this
 property to true prior to start, only the key slot transmits. After the interface is
 communicating (integrated), you can set this property to false at runtime to enable the
 remaining transmissions (the protocol's ALL_SLOTS command). After the interface is
 communicating, you cannot set this property from false to true.

This property corresponds to the **pSingleSlotEnabled** node parameter
 in the *FlexRay Protocol Specification*.

You can overwrite the default value prior to starting the FlexRay
 interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-sleep-10003b.html language=enus -->
## TOPIC 00140: Intf.FlexRay.Sleep

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-sleep-10003b.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-sleep-10003b.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Use the Sleep property to change the NI-XNET FlexRay interface sleep/awake state and optionally to initiate a wakeup on the FlexRay cluster. The property is a ring (enumerated list) with the following values: String Value Description Local Sleep 0 Set interface and transceiver(s) to sleep Local Wake

Intf.FlexRay.Sleep

Use the Sleep property to change the NI-XNET FlexRay interface sleep/awake state and optionally to initiate a wakeup on the FlexRay cluster.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

The property is a ring (enumerated list) with the following values:

| String | Value | Description |
| --- | --- | --- |
| Local Sleep | 0 | Set interface and transceiver(s) to sleep |
| Local Wake | 1 | Set interface and transceiver(s) to awake |
| Remote Wake | 2 | Set interface and transceivers to awake and attempt to wake up the FlexRay bus by sending the wakeup pattern on the configured wakeup channel |

This property is write only. Setting a new value is effectively a request, and
 the property node returns before the request is complete. To detect the current
 interface sleep/wake state, use [XNET Read (State FlexRay
 Comm)](/csh?topicname=xnet-read-state-flexray-comm.html).

The FlexRay interface maintains a state machine to determine the action to
 perform when this property is set (request). The following table specifies the
 sleep/wake action on the FlexRay interface.

| Request | Current Local State |  |
| --- | --- | --- |
| Sleep | Awake |  |
| Local Sleep | No action | Change local state |
| Local Wake | Attempt to integrate with the bus (move from POC:READY to POC:NORMAL) | No action |
| Remote Wake | Attempt to wake up the bus followed by an attempt to integrate with the bus (move from POC:READY to POC:NORMAL ACTIVE). If the interface is not yet started, setting Remote Wake schedules a remote wake to be generated once the interface has started. | No action |

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-statistics-enabled-210005a.html language=enus -->
## TOPIC 00141: Intf.FlexRay.StatisticsEn?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-statistics-enabled-210005a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-statistics-enabled-210005a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures whether to enable reporting of FlexRay error statistics. When this Boolean property is false (default), calls to XNET Read (State FlexRay Statistics) always return zero for each statistic. To enable FlexRay statistics, set this property to true in your application. You can overwrite the d

Intf.FlexRay.StatisticsEn?

Configures whether to enable reporting of FlexRay error statistics.

When this Boolean property is false (default), calls to [XNET
 Read (State FlexRay Statistics)](/csh?topicname=xnet-read-state-flexray-statistics.html) always return zero for each statistic. To
 enable FlexRay statistics, set this property to true in your application.

You can overwrite the default value prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-symbol-frames-to-input-stream-210003d.html language=enus -->
## TOPIC 00142: Intf.FlexRay.SymToInStrm?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-symbol-frames-to-input-stream-210003d.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-symbol-frames-to-input-stream-210003d.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: This property indicates whether the Frame Input Stream Mode session should return FlexRay symbols from XNET Read. When this property uses the default value of False, FlexRay symbols are not returned for a Frame Input Stream Mode session. This behavior is consistent with the other two frame input mod

Intf.FlexRay.SymToInStrm?

This property indicates whether the Frame Input Stream Mode session should return FlexRay symbols from **XNET Read**.

When this property uses the default value of False, FlexRay symbols are not returned for
 a Frame Input Stream Mode session. This behavior is consistent with the other two frame
 input modes (Frame Input Single-Point Mode and Frame Input Queued Mode), which never
 return FlexRay symbols from [XNET Read](/csh?topicname=xnet-read.html).

When you set this property to true for a Frame Input Stream Mode session, [XNET Read](/csh?topicname=xnet-read.html) returns
 all FlexRay symbols the interface receives. This feature detects wakeup symbols and
 Media Access Test Symbols (MTS). When you use the the [XNET Read (Frame
 FlexRay)](/csh?topicname=xnet-read-frame-flexray.html) instance of [XNET Read](/csh?topicname=xnet-read.html), each frame type field indicates a symbol.

When the frame type is FlexRay Symbol, the first payload byte (offset 0) specifies the
 type of symbol: 0 for MTS or 1 for wakeup. The frame payload length is 1 or higher, with
 bytes beyond the first reserved for future use. The frame timestamp specifies when the
 symbol window occurred. The cycle count, channel A indicator, and channel B indicator
 are encoded the same as FlexRay data frames. All other fields in the frame are unused
 (0).

You can overwrite the default value prior to starting the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-sync-frames-channel-a-odd-810005c.html language=enus -->
## TOPIC 00143: Intf.FlexRay.SyncChAOdd

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-sync-frames-channel-a-odd-810005c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-sync-frames-channel-a-odd-810005c.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of sync frames (slot IDs) transmitted or received on channel A during the last odd cycle. This read-only property returns an array in which each element holds the slot ID of a sync frame. If the interface is not started, this returns an empty array. If you start the interface, but i

Intf.FlexRay.SyncChAOdd

Returns an array of sync frames (slot IDs) transmitted or received on channel A during the last odd cycle.

This read-only property returns an array in which each element holds the slot ID of a
 sync frame. If the interface is not started, this returns an empty array. If you start
 the interface, but it fails to communicate (integrate), this property may be helpful in
 diagnosing the problem.

This property can be read any time prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-sync-frames-channel-b-even-810005d.html language=enus -->
## TOPIC 00144: Intf.FlexRay.SyncChBEven

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-sync-frames-channel-b-even-810005d.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-sync-frames-channel-b-even-810005d.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns an array of sync frames (slot IDs) transmitted or received on channel B during the last even cycle. This read-only property returns an array in which each element holds the slot ID of a sync frame. If the interface is not started, this returns an empty array. If you start the interface, but

Intf.FlexRay.SyncChBEven

Returns an array of sync frames (slot IDs) transmitted or received on channel B during the last even cycle.

This read-only property returns an array in which each element holds the slot ID of a
 sync frame. If the interface is not started, this returns an empty array. If you start
 the interface, but it fails to communicate (integrate), this property may be helpful in
 diagnosing the problem.

This property can be read any time prior to closing the FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-termination-100057.html language=enus -->
## TOPIC 00145: Intf.FlexRay.Term

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-termination-100057.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-termination-100057.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Controls termination at the NI-XNET interface (enumeration) connector (port). This applies to both channels (A and B) on each FlexRay interface. False means the interface is not terminated (default). True means the interface is terminated. You can overwrite the default value by writing this property

Intf.FlexRay.Term

Controls termination at the NI-XNET interface (enumeration) connector
 (port).

This applies to both channels (A and B) on each FlexRay interface. False means the interface
 is not terminated (default). True means the interface is terminated.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

You can overwrite the default value by writing this property prior to starting the FlexRay
 interface. You can start the
 FlexRay interface by calling [XNET
 Start](/csh?topicname=xnet-start.html) with scope set to either
 Normal or Interface Onlyon
 the session.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-flexray-wakeup-channel-100055.html language=enus -->
## TOPIC 00146: Intf.FlexRay.WakeupCh

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-flexray-wakeup-channel-100055.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-flexray-wakeup-channel-100055.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the channel the FlexRay interface (node) uses to send a wakeup pattern. This property is used only when the XNET Session Interface:FlexRay:Sleep property is set to Remote Wake. This property corresponds to the pWakeupChannel node parameter in the FlexRay Protocol Specification. The values

Intf.FlexRay.WakeupCh

Specifies the channel the FlexRay interface (node) uses to send a wakeup pattern.

This property is used only when the XNET Session Interface:FlexRay:Sleep property is set to Remote Wake.

This property corresponds to the **pWakeupChannel** node parameter in
 the *FlexRay Protocol Specification*.

The values supported for this property (enumeration) are A = 0 and B = 1.

You can overwrite the default value by writing this property prior to starting the
 FlexRay interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-io-name-3100013.html language=enus -->
## TOPIC 00147: Intf.IOName

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-io-name-3100013.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-io-name-3100013.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns a reference to the interface used to create the session. You can pass this I/O into an XNET Interface property node to retrieve hardware information for the interface, such as the name and serial number. The I/O Name is the same reference available from the XNET System property node, which i

Intf.IOName

Returns a reference to the interface used to create the session.

You can pass this I/O into an XNET Interface property node to retrieve hardware
 information for the interface, such as the name and serial number. The I/O Name is the
 same reference available from the XNET System property node, which is used to read
 information for all XNET hardware in the system.

You can use this property on the diagram to:

- Display a string that contains the name of the interface as shown in Measurement and
 Automation Explorer (MAX).
- Provide a refnum you can wire to a property node to read information for the
 interface.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-break-length-100070.html language=enus -->
## TOPIC 00148: Intf.LIN.BreakLen

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-break-length-100070.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-break-length-100070.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Determines the length of the serial break used at the start of a frame header (schedule entry). The value is specified in bit-times. This property is applicable only when the interface is the master. The valid range is 10–36 (inclusive). The default value is 13, which is the value the LIN standard s

Intf.LIN.BreakLen

Determines the length of the serial break used at the start of a frame header
 (schedule entry). The value is specified in bit-times.

This property is applicable only when the interface is the master.

The valid range is 10–36 (inclusive). The default value is 13, which is the value the LIN
 standard specifies. At baud rates below 9600, the upper limit may be lower than 36 to
 avoid violating hold times for the bus. For example, at 2400 baud, the valid range is
 10–14.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-diagnostics-p2min-1100077.html language=enus -->
## TOPIC 00149: Intf.LIN.DiagP2min

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-diagnostics-p2min-1100077.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-diagnostics-p2min-1100077.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: The minimum time (in seconds) between reception of the last frame of the diagnostic request message and transmission of the response for the first frame in the diagnostic response message by the slave. This property applies only to the interface as slave. An attempt to write the property for interfa

Intf.LIN.DiagP2min

The minimum time (in seconds) between reception of the last frame of the diagnostic
 request message and transmission of the response for the first frame in the diagnostic
 response message by the slave.

This property applies only to the interface as slave. An attempt to write the property
 for interface as master results in error nxErrInvalidPropertyValue being reported.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-master-2100072.html language=enus -->
## TOPIC 00150: Intf.LIN.Master?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-master-2100072.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-master-2100072.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the role of the NI-XNET LIN interface the network: master (True) or slave (False). The default value is False. You can set this property only when the interface is stopped. In a LIN network (cluster), there always is a single ECU in the system called the master. The master transmits a sche

Intf.LIN.Master?

Specifies the role of the NI-XNET LIN interface the network: master (True) or slave
 (False). The default value is False.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

In a LIN network (cluster), there always is a single ECU in the system called the
 master. The master transmits a schedule of frame headers. Each frame header is a
 remote request for a specific frame ID. For each header, typically a single ECU
 in the network (slave) responds by transmitting the requested ID payload. The
 master ECU can respond to a specific header as well, and thus the master can
 transmit payload data for the slave ECUs to receive.

The default value for this property is False (slave). This means that by default,
 the interface does not transmit frame headers onto the network. When you use
 input sessions, you read frames that other ECUs transmit. When you use output
 sessions, the NI-XNET interface waits for the remote master to send a header for
 a frame in the output sessions, then the interface responds with data for the
 requested frame.

If you call [XNET Write (State LIN Schedule Change)](/csh?topicname=xnet-write-state-lin-schedule-change.html) to request
 execution of a schedule, that implicitly sets this property to True (master).
 You also can set this property to True using a property node, but no schedule is
 active by default, so you still must call XNET Write (State LIN Schedule Change)
 at some point to request a specific schedule.

Regardless of this property's value, you use can input and output sessions. This
 property specifies which hardware transmits the scheduled frame headers: NI-XNET
 (True) or a remote master ECU (False).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-no-response-input-2100080.html language=enus -->
## TOPIC 00151: Intf.LIN.NoRespToInStrm?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-no-response-input-2100080.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-no-response-input-2100080.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the hardware to place a LIN No Response frame in the Stream Input queue after it is generated. A No Response frame is generated when the hardware detects a header with no response. To enable hardware to log this frame, you must enable this property. No Response frame fields Element Descri

Intf.LIN.NoRespToInStrm?

Configures the hardware to place a LIN No Response frame in the Stream Input
 queue after it is generated.

A No Response frame is generated when the hardware detects a header with no response. To
 enable hardware to log this frame, you must enable this property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

#### No Response frame fields

| Element | Description |
| --- | --- |
| identifier | Unprotected version of header ID |
| event slot? | False |
| event ID | 0 |
| echo? | False |
| type | LIN No Response |
| timestamp | Time when the end of header (ID) was detected |
| payload length | 0 |
| payload | N/A |

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-output-stream-slave-list-nad-8100079.html language=enus -->
## TOPIC 00152: Intf.LIN.OutStrmSlvRspListByNAD

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-output-stream-slave-list-nad-8100079.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-output-stream-slave-list-nad-8100079.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides a list of NADs for use with the replay feature (Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive). For LIN, the array of frames to replay might contain multiple slave response frames, each with the same slave response identifier, but each having been trans

Intf.LIN.OutStrmSlvRspListByNAD

Provides a list of NADs for use with the replay feature (Interface:Output
 Stream Timing property set to Replay Exclusive or Replay
 Inclusive).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

For LIN, the array of frames to replay might contain multiple slave response
 frames, each with the same slave response identifier, but each having been
 transmitted by a different slave (per the NAD value in the data payload). This
 means that processing slave response frames for replay requires two levels of
 filtering.

First, you can include or exclude the slave response frame or ID for replay using
 Interface:Output Stream List or Interface:Output Stream List By ID. If you do not include the slave
 response frame or ID for replay, no slave responses are transmitted. If you do
 include the slave response frame or ID for replay, you can use the Output Stream
 Slave Response List by NAD property to filter which slave responses (per the NAD
 values in the array) are transmitted. This property is always inclusive,
 regardless of the replay mode (inclusive or exclusive).

If the NAD is in the list and the response frame or ID has been enabled for
 replay, any slave response for that NAD is transmitted. If the NAD is not in the
 list, no slave response for that NAD is transmitted. The property's data type is
 an array of unsigned 32-bit integer (u32). Currently, only byte 0 is required to
 hold the NAD value. The remaining bits are reserved for future use.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-schedules-4100075.html language=enus -->
## TOPIC 00153: Intf.LIN.Schedules

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-schedules-4100075.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-schedules-4100075.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides the list of schedules for use when the NI-XNET LIN interface acts as a master (Interface:LIN:Master? is True). When the interface is master, you can wire one of these schedules to XNET Write (State LIN Schedule Change) to request a schedule change. When the interface does not act as a maste

Intf.LIN.Schedules

Provides the list of schedules for use when the NI-XNET LIN interface acts as a
 master (Interface:LIN:Master? is True).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

When the interface is master, you can wire one of these schedules to [XNET
 Write (State LIN Schedule Change)](/csh?topicname=xnet-write-state-lin-schedule-change.html) to request a schedule change.

When the interface does not act as a master, you cannot control the schedule, and XNET Write
 (State LIN Schedule Change) returns an error if it cannot set the interface into
 master mode (for example, if the interface already is started).

This array of XNET LIN Schedule I/O names is the same list as the [XNET
 Cluster:LIN:Schedules](/csh?topicname=xnet-cluster-lin-schedules-6010070.html) property used to configure the session.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-lin-start-allowed-nopower-2100078.html language=enus -->
## TOPIC 00154: Intf.LIN.StrtWoPwr?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-lin-start-allowed-nopower-2100078.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-lin-start-allowed-nopower-2100078.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures whether a LIN session is allowed to start without bus power applied to the interface. The default value is False. When set to True, there is no check for bus power present at start, and no error is reported if the interface is started without bus power. When set to False (default), the LI

Intf.LIN.StrtWoPwr?

Configures whether a LIN session is allowed to start without bus power applied to the
 interface. The default value is False.

When set to True, there is no check for bus power present at start, and no error is
 reported if the interface is started without bus power.

When set to False (default), the LIN interface checks for bus power present at start, and
 an error is reported (nxErrMissingBusPower) if the interface is started without bus
 power.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-out-stream-list-6100011.html language=enus -->
## TOPIC 00155: Intf.OutStrmList

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-out-stream-list-6100011.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-out-stream-list-6100011.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides a list of frames for use with the replay feature (Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive). In Replay Exclusive mode, the hardware transmits only frames that do not appear in the list. In Replay Inclusive mode, the hardware transmits only frames t

Intf.OutStrmList

Provides a list of frames for use with the replay feature (Interface:Output Stream
 Timing property set to Replay Exclusive or Replay Inclusive).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

In Replay Exclusive mode, the hardware transmits only frames that do not appear
 in the list. In Replay Inclusive mode, the hardware transmits only frames that
 appear in the list. For a LIN interface, the header of each frame written to
 stream output is transmitted, and the Exclusive or Inclusive mode controls the
 response transmission. Using these modes, you can either emulate an ECU (Replay
 Inclusive, where the list contains the frames the ECU transmits) or test an ECU
 (Replay Exclusive, where the list contains the frames the ECU transmits), or
 some other combination.

This property's data type is an array of XNET Frame from a database. When you are
 using a database file such as CANdb FIBEX or AUTOSAR, each XNET frame uses the
 string name. If you are not using a database file or prefer to specify the
 frames using CAN arbitration IDs or LIN unprotected IDs, you can use
 Interface:Output Stream List By ID instead of this property.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-out-stream-list-id-8100021.html language=enus -->
## TOPIC 00156: Intf.OutStrmListById

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-out-stream-list-id-8100021.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-out-stream-list-id-8100021.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Provides a list of frames for use with the replay feature. The replay feature is available when the Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive. This property serves the same purpose as Interface:Output Stream List, in that it provides a list of frames for rep

Intf.OutStrmListById

Provides a list of frames for use with the replay feature.

The replay feature is available when the Interface:Output Stream Timing property set to
 Replay Exclusive or Replay Inclusive.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

This property serves the same purpose as Interface:Output Stream List, in that it provides a list of frames
 for replay filtering. This property provides an alternate format for you to
 specify the frames by their CAN arbitration ID or LIN unprotected ID. The
 property's data type is an array of unsigned 32-bit integer (U32). Each integer
 represents a CAN or LIN frame's identifier, using the same encoding as the Raw
 Frame Format.

Within each CAN frame ID value, bit 29 (hex 20000000) indicates the CAN
 identifier format (set for extended, clear for standard). If bit 29 is clear,
 the lower 11 bits (0–10) contain the CAN frame identifier. If bit 29 is set, the
 lower 29 bits (0–28) contain the CAN frame identifier. LIN frame ID values may
 be within the range of possible LIN IDs (0-63).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-out-stream-timing-100012.html language=enus -->
## TOPIC 00157: Intf.OutStrmTimng

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-out-stream-timing-100012.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-out-stream-timing-100012.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: The Output Stream Timing property configures how the hardware transmits frames queued using a Frame Output Stream session. The following table lists the accepted values: Enumeration Value Immediate 0 Replay Exclusive 1 Replay Inclusive 2 When you configure this property to be Immediate, frames are d

Intf.OutStrmTimng

The Output Stream Timing property configures how the hardware transmits frames queued
 using a Frame Output Stream session.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

The following table lists the accepted values:

| Enumeration | Value |
| --- | --- |
| Immediate | 0 |
| Replay Exclusive | 1 |
| Replay Inclusive | 2 |

When you configure this property to be Immediate, frames are dequeued from the
 queue and transmitted immediately to the bus. The hardware transmits all frames
 in the queue as fast as possible.

When you configure this property as Replay Exclusive or Replay Inclusive, the
 hardware is placed into a Replay mode. In this mode, the hardware evaluates the
 frame timestamps and attempts to maintain the original transmission times as the
 timestamp stored in the frame indicates. The actual transmission time is based
 on the relative time difference between the first dequeued frame and the time
 contained in the dequeued frame.

When in one of the replay modes, you can use the Interface:Output Stream List property to supply a list. In Replay
 Exclusive mode, the hardware transmits only frames that do not appear in the
 list. In Replay Inclusive mode, the hardware transmits only frames that appear
 in the list. Using these modes, you can either emulate an ECU (Replay Inclusive,
 where the list contains the frames the ECU transmits) or test an ECU (Replay
 Exclusive, where the list contains the frames the ECU transmits), or some other
 combination. You can replay all frames by using Replay Exclusive mode without
 setting any list.

#### Runtime Behavior

When the hardware is in a replay mode, the first frame received from the
 application is considered the start time, and all subsequent frames are
 transmitted at the appropriate delta from the start time. For example, if the
 first frame has a timestamp of 12:01.123, and the second frame has a timestamp
 of 12:01.456, the second frame is transmitted 333 ms after the first frame.

If a frame's time is identical or goes backwards relative to the first timestamp,
 this is treated as a new start time, and the frame is transmitted immediately on
 the bus. Subsequent frames are compared to this new start time to determine the
 transmission time. For example, assume that the application sends the hardware
 four frames with the following timestamps: 12:01.123, 12:01.456, 12:01.100, and
 12:02.100. In this scenario, the first frame transmits immediately, the second
 frame transmits 333 ms after the first, the third transmits immediately after
 the second, and the fourth transmits one second after the third. Using this
 behavior, you can replay a logfile of frames repeatedly, and each new replay of
 the file begins with new timing.

A frame whose timestamp goes backwards relative to the previous timestamp, but
 still is forward relative to the start time, is transmitted immediately. For
 example, assume that the application sends the hardware four frames with the
 following timestamps: 12:01.123, 12:01.456, 12:01.400, and 12:02.100. In this
 scenario, the first frame transmits immediately, the second frame transmits 333
 ms after the first, the third transmits immediately after the second, and the
 fourth transmits 544 ms after the third.

When a frame with a Delay Frame frame type is received, the hardware delays for
 the requested time. The next frame to be dequeued is treated as a new first
 frame and transmitted immediately. You can use a Delay Frame with a time of 0 to
 restart time quickly. If you replay a logfile of frames repeatedly, you can
 insert a Delay Frame at the start of each replay to insert a delay between each
 iteration through the file.

When a frame with a Start Trigger frame type is received, the hardware treats
 this frame as a new first frame and uses the absolute time associated with this
 frame as the new start time. Subsequent frames are compared to this new start
 time to determine the transmission time. Using a Start Trigger is especially
 useful when synchronizing with data acquisition products, so that you can replay
 the first frame at the correct time relative to the start trigger for accurate
 synchronized replay.

#### Special Considerations for
 LIN

Only LIN interface as Master supports stream output. You do not need to set the
 interface explicitly to Master if you want to use stream output. Just create a
 stream output session, and the driver automatically sets the interface to Master
 at interface start.

You can use immediate mode to transmit a header or full frame. You can transmit
 only the header for a frame by writing the frame to stream output with the
 desired ID and an empty data payload. You can transmit a full frame by writing
 the frame to stream output with the desired ID and data payload. If you write a
 full frame for ID n to stream output, and you have created a frame output
 session for frame with ID n, the stream output data takes priority (the stream
 output frame data is transmitted and not the frame output data). If you write a
 full frame to stream output, but the frame has not been defined in the database,
 the frame transmits with Enhanced checksum. To control the checksum type
 transmitted for a frame, you first must create the frame in the database and
 assign it to an ECU using the LIN specification you desire (the specification
 number determines the checksum type). You then must create a frame output object
 to transmit the response for the frame, and use stream output to transmit the
 header. Similarly, to transmit n corrupted checksums for a frame, you first must
 create a frame object in the database, create a frame output session for it, set
 the transmit n corrupted checksums property, and then use stream output to
 transmit the header.

Regarding event-triggered frame handling for immediate mode, if the hardware can
 determine that an ID is for an event-triggered frame, which means an
 event-triggered frame has been defined for the ID in the database, the frame is
 processed as if it were in an event-triggered slot in a schedule. If you write a
 full frame with event-triggered ID, the full frame is transmitted. If there is
 no collision, the next stream output frame is processed. If there is a
 collision, the hardware executes the collision-resolving schedule. The hardware
 retransmits the frame response at the corresponding slot time in the collision
 resolving schedule. If you write a header frame with an event-triggered ID and
 there is no collision, the next stream output frame is processed. If there is a
 collision, the hardware executes the collision-resolving schedule.

You can mix use of the hardware scheduler and stream output immediate mode.
 Basically, the hardware treats each stream output frame as a separate run-once
 schedule containing a single slot for the frame. Transmission of a stream output
 frame may interrupt a run-continuous schedule, but may not interrupt a run-once
 schedule. Transmission of stream output frames is interleaved with
 run-continuous schedule slot executions, depending on the application timing of
 writes to stream output. Stream output is prioritized to the equivalent of the
 lowest priority level for a run-once schedule. If you write one or more run-once
 schedules with higher-than-lowest priority and write frames to stream output,
 all the run-once schedules are executed before stream output transmits anything.
 If you write one or more run-once schedules with the lowest priority and write
 frames to stream output, the run-once schedules execute in the order you wrote
 them, and are interleaved with stream output frames, depending on the
 application timing of writes to stream output and writes of run-once schedule
 changes.

In contrast to the immediate mode, neither replay mode allows for the concurrent
 use of the hardware scheduler, and an error is reported if you attempt to do so.
 Event-triggered frame handling is different for the replay modes. If the
 hardware can determine that an ID is for an event-triggered frame, which means
 an event-triggered frame has been defined for the ID in the database, the frame
 is transmitted as if it were being transmitted during the collision-resolving
 schedule for the event triggered frame. The full frame is transmitted with the
 Data[0] value (the underlying unconditional frame ID), copied into the header
 ID. If a frame cannot be found in the database, it is transmitted with Enhanced
 checksum. Otherwise, it is transmitted with the checksum type defined in the
 database.

The reply modes provide an easy means to replay headers only, full frames only,
 or some mix of the two. For either replay mode, the header for each frame is
 always transmitted and the slot delay is preserved. For replay inclusive, if you
 want only to replay headers, leave the Interface:Output Stream List property empty. To replay some of the
 responses, add their frames to Interface:Output Stream List. For frames that are
 not in Interface:Output Stream List, you are free to create frame output objects
 for them, for which you can change the checksum type or transmit corrupted
 checksums.

There is another consideration for the replay of diagnostic slave response
 frames. Because the master always transmits only the diagnostic slave response
 header, and a slave transmits the response if its NAD matches the one
 transmitted in the preceding master request frame, an array of frames for replay
 might include multiple slave response frames (each having the same slave
 response header ID) transmitted by different slaves (each having a different NAD
 value in the data payload). If you are using inclusive mode, you can choose not
 to replay any slave response frames by not including the slave response frame in
 Interface:Output Stream List. You can choose to replay some or all of the slave
 response frames by first including the slave response frame in Interface:Output
 Stream List, then including the NAD values for the slave responses you want to
 play back, in Interface:LIN:Output Stream Slave Response List By NAD. In this
 way, you have complete control over which slave responses are replayed (which
 diagnostic slaves you emulate). Replay of a diagnostic master request frame is
 handled like replay of any other frame; the header is always transmitted. Using
 the inclusive mode as an example, the response may or may not be transmitted
 depending on whether or not the master request frame is in Interface:Output
 Stream List.

#### Restrictions on Other
 Sessions

When you use Immediate mode, there are no restrictions on frames that you use in
 other sessions.

When you use Replay Inclusive mode, you can create output sessions that use
 frames that do not appear in the Interface:Output Stream List property. Attempting to create an
 output session that uses a frame from the Interface:Output Stream List property
 results in an error. Input sessions have no restrictions.

When you use Replay Exclusive mode, you cannot create any other output sessions.
 Attempting to create an output session returns an error. Input sessions have no
 restrictions.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-source-terminal-star-trigger-3100090.html language=enus -->
## TOPIC 00158: Intf.SrcTerm.StartTrigger

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-source-terminal-star-trigger-3100090.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-source-terminal-star-trigger-3100090.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Specifies the name of the internal terminal to use as the interface Start Trigger. The data type is NI Terminal (DAQmx terminal). Use this property to connect the interface Start Trigger to triggers in other modules and/or interfaces. When you read this property, you specify the interface Start Trig

Intf.SrcTerm.StartTrigger

Specifies the name of the internal terminal to use as the interface Start
 Trigger. The data type is NI Terminal (DAQmx terminal).

Use this property to connect the interface Start Trigger to triggers in other modules
 and/or interfaces. When you read this property, you specify the interface Start Trigger
 as the source of a connection. When you write this property, you specify the interface
 Start Trigger as the destination of a connection, and the value you write represents the
 source.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

For examples that demonstrate use of this property to synchronize NI-XNET and
 NI-DAQmx hardware, refer to the Synchronization category within the NI-XNET
 examples.

The connection this property creates is disconnected when you clear (close) all
 sessions that use the interface.

This property is supported for C Series modules in a CompactDAQ chassis. It is
 not supported for CompactRIO, PXI, or PCI (refer to the XNET Connect Terminals
 VI for those platforms).

The digital trigger signal at this terminal is for the Start Interface
 transition, to begin communication for all sessions that use the interface. This
 property routes the start trigger, but not the timebase (used for timestamp of
 received frames and cyclic transmit of frames). Timebase routing is not required
 for CompactDAQ, because all modules in the chassis automatically use a shared
 timebase.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-start-trigger-frames-to-input-stream-2100014.html language=enus -->
## TOPIC 00159: Intf.StartTrigToInStrm?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-start-trigger-frames-to-input-stream-2100014.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-start-trigger-frames-to-input-stream-2100014.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures the hardware to place a start trigger frame into the Stream Input queue after it is generated. A Start Trigger frame is generated when the interface is started. The start trigger frame is especially useful if you plan to log and replay CAN data.

Intf.StartTrigToInStrm?

Configures the hardware to place a start trigger frame into the Stream Input queue
 after it is generated.

A Start Trigger frame is generated when the interface is started. The start trigger frame is
 especially useful if you plan to log and replay CAN data.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-interface-stats-rxbytes-count-91000ae.html language=enus -->
## TOPIC 00160: Intf.Enet.St.RxBytes

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-interface-stats-rxbytes-count-91000ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-interface-stats-rxbytes-count-91000ae.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Count of the number of bytes (octets) received. The count for each frame is its frame length. Bad frames are counted in addition to good frames. Reading this counter twice can be used to obtain an estimate of received bandwidth over the time between the two reads. This statistic is analogous to the

Intf.Enet.St.RxBytes

Count of the number of bytes (octets) received. The count for each frame is its frame
 length. Bad frames are counted in addition to good frames.

Reading this counter twice can be used to obtain an estimate of received bandwidth over
 the time between the two reads.

This statistic is analogous to the **etherStatsOctets** parameter as
 described in RFC 2819.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-ecu-5100093.html language=enus -->
## TOPIC 00161: J1939.ECU

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-ecu-5100093.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-ecu-5100093.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Assigns a database ECU to this session. Setting this property changes the node address and J1939 64-bit ECU name of the session to the values stored in the database ECU object. Changing the node address starts an address claiming procedure, as described in the SAE J1939:Node Address property. This p

J1939.ECU

Assigns a database ECU to this session.

Setting this property changes the node address and J1939 64-bit ECU name of the session
 to the values stored in the database ECU object. Changing the node address starts an
 address claiming procedure, as described in the SAE J1939:Node
 Address property.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Write

Changing the node address causes NI-XNET to start the interface; you must set any
 properties that are to be set before the interface starts before changing the
 node address. Also, note that setting the node address does not start the
 session. J1939 traffic is not retained by an input session until [XNET
 Start](/csh?topicname=xnet-start.html) or [XNET Read](/csh?topicname=xnet-read.html) are explicitly called.

You can assign the same ECU to multiple sessions running on the same CAN
 interface (for example, CAN1). All sessions with the same assigned ECU represent
 one J1939 node.

If multiple sessions have been assigned the same ECU, setting the SAE
 J1939:Node Address property in one session changes the address
 in all sessions with the same assigned ECU running on the same CAN interface.

For more information, refer to the SAE J1939:Node Address
 property.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-include-destination-address-in-pgn-21000a5.html language=enus -->
## TOPIC 00162: J1939.IncludeDestAddrInPGN

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-include-destination-address-in-pgn-21000a5.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-include-destination-address-in-pgn-21000a5.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Include the J1939 destination address (PDU1 PS field) when matching received frames to database frames. When set to True, this property instructs NI-XNET to include the destination address when extracting the parameter group number (PGN) from the frame. This allows the same PGN sent to different des

J1939.IncludeDestAddrInPGN

Include the J1939 destination address (PDU1 PS field) when matching received frames
 to database frames.

When set to True, this property instructs NI-XNET to include the destination address when
 extracting the parameter group number (PGN) from the frame. This allows the same PGN
 sent to different destination addresses to be handled by separate input sessions.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

Incoming J1939 frames are matched to an XNET database by the PGN of the frame.
 When receiving PDU1 frames, the destination address of the frame (J1939 PS
 field) is ignored when calculating the PGN, in accordance to the J1939
 specification. This causes an XNET session to receive all frames that share the
 same PGN, making it difficult to distinguish destinations for traffic.

When set to True, this property instructs NI-XNET to include the destination
 address when extracting the PGN from the frame. This allows the same PGN sent to
 different destination addresses to be handled by separate input sessions.

This property may be set at any time. When set after session start, it will not
 affect frames already received.

The SAE J1939:Include Destination Address in PGN property
 is valid only for input sessions. It is not valid for stream sessions. This
 property affects all frames in a session.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-max-repeats-cts-10009e.html language=enus -->
## TOPIC 00163: J1939.MaxReptCTS

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-max-repeats-cts-10009e.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-max-repeats-cts-10009e.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Maximum number of CTS repetitions for the J1939 Transport Protocol. This property applies to only the CAN J1939 application protocol.

J1939.MaxReptCTS

Maximum number of CTS repetitions for the J1939 Transport Protocol.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-number-of-packets-received-10009c.html language=enus -->
## TOPIC 00164: J1939.NumPktsRecv

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-number-of-packets-received-10009c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-number-of-packets-received-10009c.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Maximum number of data packets that can be received in one block at the responder node for the J1939 Transport Protocol. This property applies to only the CAN J1939 application protocol.

J1939.NumPktsRecv

Maximum number of data packets that can be received in one block at the responder
 node for the J1939 Transport Protocol.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-number-of-packets-response-10009d.html language=enus -->
## TOPIC 00165: J1939.NumPktsResp

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-number-of-packets-response-10009d.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-number-of-packets-response-10009d.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Maximum number of packets transmitted in a block for the J1939 Transport Protocol. This property allows the originator node to limit the number of packets in the TP.CM_CTS message. When the responder complies with this limit, it ensures the sender always can retransmit packets that the responder may

J1939.NumPktsResp

Maximum number of packets transmitted in a block for the J1939 Transport
 Protocol.

This property allows the originator node to limit the number of packets in the TP.CM_CTS
 message. When the responder complies with this limit, it ensures the sender always can
 retransmit packets that the responder may not have received.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-resp-time-trgd-1100099a.html language=enus -->
## TOPIC 00166: J1939.RespTimeTrGD

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-resp-time-trgd-1100099a.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-resp-time-trgd-1100099a.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the Device Response Time value for global destination messages (TP.CM_BAM messages). The value is the minimum delay between sending two TP.CM_BAM messages, in seconds. The recommended range is 0.05 s to 0.200 s. This property is related to handling the transport protocol. Default value is 0

J1939.RespTimeTrGD

Modifies the Device Response Time value for global destination messages (TP.CM_BAM
 messages).

The value is the minimum delay between sending two TP.CM_BAM messages, in seconds. The
 recommended range is 0.05 s to 0.200 s. This property is related to handling the
 transport protocol.

Default value is 0.05 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-resp-time-trsd-1100099.html language=enus -->
## TOPIC 00167: J1939.RespTimeTrSD

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-resp-time-trsd-1100099.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-resp-time-trsd-1100099.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the Device Response Time value for specific destination messages (TP.CM_RTS/CTS messages). The value specifies the minimum delay between receipt of a message and sending a response. This value also specifies a minimum time delay between packets of a multipacket message directed to a specifi

J1939.RespTimeTrSD

Modifies the Device Response Time value for specific destination messages
 (TP.CM_RTS/CTS messages).

The value specifies the minimum delay between receipt of a message and sending a
 response. This value also specifies a minimum time delay between packets of a
 multipacket message directed to a specific destination.

According to the J1939 specification, the time between packets of a multipacket message
 directed to a specific destination may be 0 ms to 200 ms. Increasing the response time
 can adversely affect performance in handling multipacket messages.

Default value is 0 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-timeoutt1-1100095.html language=enus -->
## TOPIC 00168: J1939.TimeoutT1

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-timeoutt1-1100095.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-timeoutt1-1100095.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the timeout T1 value for the responder node. The value is the maximum gap between two received TP.DT messages, in seconds. This property is related to handling the transport protocol. Default value is 0.75 s. This property applies to only the CAN J1939 application protocol.

J1939.TimeoutT1

Modifies the timeout T1 value for the responder node.

The value is the maximum gap between two received TP.DT messages, in seconds. This
 property is related to handling the transport protocol. Default value is 0.75 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-timeoutt2-1100096.html language=enus -->
## TOPIC 00169: J1939.TimeoutT2

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-timeoutt2-1100096.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-timeoutt2-1100096.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the timeout T2 value at the responder node. This value is the maximum gap between sending out the TP.CM_CTS message and receiving the next TP.DT message, in seconds. This property is related to handling the transport protocol. Default value is 1.25 s. This property applies to only the CAN J

J1939.TimeoutT2

Modifies the timeout T2 value at the responder node.

This value is the maximum gap between sending out the TP.CM_CTS message and receiving the next
 TP.DT message, in seconds. This property is related to handling the transport protocol.
 Default value is 1.25 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-timeoutt3-1100097.html language=enus -->
## TOPIC 00170: J1939.TimeoutT3

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-timeoutt3-1100097.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-timeoutt3-1100097.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the timeout T3 value at the originator node. The value is the maximum gap between sending out a TP.CM_RTS message or the last TP.DT message and receiving the TP.CM_CTS response, in seconds. This property is related to handling the transport protocol. Default value is 1.25 s. This property a

J1939.TimeoutT3

Modifies the timeout T3 value at the originator node.

The value is the maximum gap between sending out a TP.CM_RTS message or the last TP.DT message
 and receiving the TP.CM_CTS response, in seconds. This property is related to handling
 the transport protocol. Default value is 1.25 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-j1939-timeoutt4-1100098.html language=enus -->
## TOPIC 00171: J1939.TimeoutT4

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-j1939-timeoutt4-1100098.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-j1939-timeoutt4-1100098.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Modifies the timeout T4 value at the originator node. This value is the maximum gap between the TP.CM_CTS hold message and the next TP.CM_CTS message, in seconds. This property is related to handling the transport protocol. Default value is 1.05 s. This property applies to only the CAN J1939 applica

J1939.TimeoutT4

Modifies the timeout T4 value at the originator node.

This value is the maximum gap between the TP.CM_CTS hold message and the next TP.CM_CTS
 message, in seconds. This property is related to handling the transport protocol.
 Default value is 1.05 s.

Note

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-listfrms-410ffff.html language=enus -->
## TOPIC 00172: ListFrms

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-listfrms-410ffff.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-listfrms-410ffff.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the list of frames in the session. This property is valid only for sessions of Frame Input or Frame Output mode. For a Signal Input/Output session, use the List of Signals property. Use each array element on the block diagram as follows: As a refnum wired to a property node to access informa

ListFrms

Returns the list of frames in the session.

This property is valid only for sessions of Frame Input or Frame Output mode. For a
 Signal Input/Output session, use the List of Signals property.

Use each array element on the block diagram as follows:

- As a refnum wired to a property node to access information for the frame.
- As a string containing the frame name. The name is the one used to create the
 session.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-numinlist-100005.html language=enus -->
## TOPIC 00173: NumInList

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-numinlist-100005.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-numinlist-100005.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the number of frames or signals in the session's list. This is a quick way to get the size of the List of Frames or List of Signals property.

NumInList

Returns the number of frames or signals in the session's list. This is a quick way to
 get the size of the List of Frames or List of
 Signals property.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-numpend-100006.html language=enus -->
## TOPIC 00174: NumPend

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-numpend-100006.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-numpend-100006.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the number of values (frames or signals) pending for the session. For input sessions, this is the number of frame/signal values available to XNET Read. If you call the XNET Read node with number to read of this number and timeout of 0.0, XNET Read should return this number of values successf

NumPend

Returns the number of values (frames or signals) pending for the
 session.

For input sessions, this is the number of frame/signal values available to [XNET Read](/csh?topicname=xnet-read.html). If
 you call the XNET Read node with **number to read** of this number
 and **timeout** of 0.0, XNET Read should return this number of
 values successfully.

For output sessions, this is the number of frames/signal values provided to [XNET Write](/csh?topicname=xnet-write.html) but
 not yet transmitted onto the network.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

Stream frame sessions using FlexRay or CAN FD protocol may use a variable size of
 frames. In these cases, this property assumes the largest possible frame size.
 If you use smaller frames, the real number of pending values might be
 higher.

The largest possible frames sizes are:

- CAN FD: 64 byte payload.
- FlexRay: The higher value of the frame size in the static segment and the
 maximum frame size in the dynamic segment. The XNET Cluster
 FlexRay:Payload Length Maximum property provides
 this value.

The execution time to read this property is sufficient for use in a high-priority
 loop on LabVIEW Real-Time (RT).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-numunused-10000b.html language=enus -->
## TOPIC 00175: NumUnused

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-numunused-10000b.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-numunused-10000b.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the number of values (frames or signals) unused for the session. If you get this property prior to starting the session, it provides the size of the underlying queue(s). Contrary to the Queue Size property, this value is in number of frames for Frame I/O, not number of bytes; for Signal I/O,

NumUnused

Returns the number of values (frames or signals) unused for the session. If you get
 this property prior to starting the session, it provides the size of the underlying
 queue(s).

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

Contrary to the Queue Size property, this value is in number of frames
 for Frame I/O, not number of bytes; for Signal I/O, it is the number of signal
 values in both cases. After start, this property returns the queue size minus
 the Number
 of Values Pending property.

For input sessions, this is the number of frame/signal values unused in the
 underlying queue(s).

For output sessions, this is the number of frame/signal values you can provide to
 a subsequent Write. If you call [XNET
 Write](/csh?topicname=xnet-write.html) with this number of values and timeout of 0.0, XNET Write
 should return success.

Stream frame sessions using the FlexRay, CAN FD, or Ethernet protocol may use
 frames that vary in size. In these cases, this property assumes the largest
 possible frame size. If you use smaller frames, the real number of pending
 values might be higher.

The largest possible frames sizes are:

- CAN FD: 64 byte payload.
- FlexRay: The higher value of the frame size in the static segment and the
 maximum frame size in the dynamic segment. The XNET Cluster
 FlexRay:Payload Length Maximum property provides this
 value.
- Ethernet: The Payload Length Maximum property provides this
 value.

The execution time to read this property is sufficient for use in a high-priority
 loop on LabVIEW Real-Time (RT).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-payldmax-100009.html language=enus -->
## TOPIC 00176: PayldLenMax

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-payldmax-100009.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-payldmax-100009.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Maximum payload length of all frames in this session, expressed as bytes (0-254). This property applies only to Frame sessions. For CAN Stream (Input and Output), this property depends on the XNET Cluster CAN:I/O Mode property. If the I/O mode is CAN, this property is 8 bytes. If the I/O mode is CAN

PayldLenMax

Maximum payload length of all frames in this session, expressed as bytes (0-254).
 This property applies only to Frame sessions.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

For CAN Stream (Input and Output), this property depends on the XNET
 Cluster CAN:I/O Mode property. If the I/O mode is CAN, this
 property is 8 bytes. If the I/O mode is CAN FD or CAN FD+BRS, this property is
 64 bytes.

For LIN Stream (Input and Output), this property always is 8 bytes. For FlexRay
 Stream (Input and Output), this property is the same as the XNET
 Cluster FlexRay:Payload Length Maximum property value. For
 Queued and Single-Point (Input and Output), this is the maximum payload of all
 frames specified in the List of Frames property.

For Ethernet Stream (Input and Output), this property is the maximum length of
 the *frame data* in each frame, which includes the Ethernet header in
 addition to the Ethernet payload (MSDU).

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-protocol-100008.html language=enus -->
## TOPIC 00177: Protocol

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-protocol-100008.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-protocol-100008.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Returns the protocol that the interface in the session uses. 0 CAN 1 FlexRay 2 LIN 3 Ethernet

Protocol

Returns the protocol that the interface in the session uses.

| 0 | CAN |
| --- | --- |
| 1 | FlexRay |
| 2 | LIN |
| 3 | Ethernet |

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session-queuesize-10000c.html language=enus -->
## TOPIC 00178: QueueSize

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session-queuesize-10000c.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session-queuesize-10000c.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: For output sessions, queues store data passed to XNET Write and not yet transmitted onto the network. For input sessions, queues store data received from the network and not yet obtained using XNET Read. For most applications, the default queue sizes are sufficient. You can write to this property to

QueueSize

For output sessions, queues store data passed to XNET Write and not yet
 transmitted onto the network. For input sessions, queues store data received from the
 network and not yet obtained using XNET Read. For most applications, the default queue
 sizes are sufficient. You can write to this property to override the default.

When you write (set) this property, you must do so prior to the first session start. You cannot
 set this property again after calling [XNET Stop](/csh?topicname=xnet-stop.html).

For signal I/O sessions, this property is the number of signal values stored. This is analogous
 to the number of values you use with [XNET Read](/csh?topicname=xnet-read.html) or [XNET Write](/csh?topicname=xnet-write.html).

For frame I/O sessions, Queue Size is
 the number of bytes of frame data stored.

For standard CAN and LIN frame I/O
 sessions, each frame uses exactly 24 bytes. You can use this
 number to convert the Queue Size (in bytes) to/from the number of frame
 values.

For CAN FD and FlexRay frame I/O sessions, each frame value size can vary
 depending on the payload length. For more information, refer to Raw Frame Format.

For Signal I/O XY sessions, you can use signals from more than one frame. Within the
 implementation, each frame uses a dedicated queue. According to the formulas below, the
 default queue sizes can be different for each frame. If you read the default Queue Size
 property for a Signal Input XY session, the largest queue size is returned, so that a
 call to XNET Read of that size can empty all queues. If you read the default
 Queue Size property for a Signal Output XY session, the
 smallest queue size is returned, so that a call to XNET Write of that size can succeed
 when all queues are empty. If you write the Queue Size property
 for a Signal I/O XY session, that size is used for all frames, so you must ensure that
 it is sufficient for the frame with the fastest transmit time.

For Signal I/O Waveform sessions, you can use signals from more than one
 frame. Within the implementation, each frame uses a dedicated queue. The
 Queue Size property does not represent the memory in these
 queues, but rather the amount of time stored. The default queue allocations store
 Application Time worth of resampled signal values. If you read the default
 Queue Size property for a Signal I/O Waveform session, it
 returns Application Time multiplied by the time Resample Rate. If you write the Queue
 Size property for a Signal I/O Waveform session, that value is translated from a number
 of samples to a time, and that time is used to allocate memory for each queue.

For Single-Point sessions (signal or frame), this property is ignored. Single-Point sessions
 always use a value of 1 as the effective queue size.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Session](xnet-session.html)

**Permissions:** Read/Write

#### Default Value

You calculate the default queue size based on the following assumptions:

- Application Time: The time between calls to the XNET Read
 VI/XNET Write VI in your application.
- Frame Time: The time between frames on the network for this
 session.

The following pseudo code describes the default queue size formula:

```text
if (session is Signal I/O Waveform)
             Queue_Size = (Application_Time * Resample_Rate);
          else
             Queue_Size = (Application_Time / Frame_Time);
          if (Queue_Size < 64)
             Queue_Size = 64;
          if (session mode is Frame I/O)
             Queue_Size = Queue_Size * Frame_Size;
```

For Signal I/O Waveform sessions, the initial formula calculates the number of
 resampled values that occur within the Application Time. This is done by
 multiplying Application Time by the XNET Session Resample Rate property.

For all other session modes, the initial formula divides Application Time by
 Frame Time.

The minimum for this formula is 64. This minimum ensures that you can read or
 write at least 64 elements. If you need to read or write more elements for a
 slow frame, you can set the Queue Size property to a larger number than the
 default. If you set a large Queue Size, this may limit the maximum number of
 frames you can use in all sessions.

For Frame I/O sessions, this formula result is multiplied by each frame value
 size to obtain a queue size in bytes.

For Signal I/O sessions, this formula result is used directly for the queue size
 property to provide the number of signal values for the XNET Read VI or XNET
 Write VI. Within the Signal I/O session, the memory allocated for the queue
 incorporates frame sizes, because the signal values are mapped to/from frame
 values internally.

#### Application Time

The LabVIEW target in which your application runs determines the Application
 Time:

- Windows: 400 ms (0.4 s)
- LabVIEW Real-Time (RT): 100 ms (0.1 s)

This works under the assumption that for Windows, more memory is available for
 input queues, and you have limited control over the application timing. LabVIEW
 RT targets typically have less available memory, but your application has better
 control over application timing.

#### Frame Time

Frame Time is calculated differently for Frame I/O Stream sessions compared to
 other modes. For Frame I/O Stream, you access all frames in the network
 (cluster), so the Frame Time is related to the average bus load on your network.
 For other modes, you access specific frames only, so the Frame Time is obtained
 from database properties for those frames.

The Frame Time used for the default varies by session mode and protocol, as
 described below.

CAN, Frame I/O Stream:

- Frame Time is 100 µs (0.0001 s). This time assumes a baud rate of 1 Mbps,
 with frames back to back (100 percent busload).
- For CAN sessions created for a standard CAN bus, the Frame Size is 24 bytes.
 For CAN sessions created for a CAN FD Bus (the cluster I/O mode is CAN FD or
 CAN FD+BRS), the frame size can vary up to 64 bytes. However, the default
 queue size is based on the 24-byte frame time. When connecting to a CAN FD
 bus, you may need to adjust this size as necessary.
- When you create an application to stress test NI-XNET performance, it is
 possible to generate CAN frames faster than 100 µs. For this application,
 you must set the queue size to larger than the default.

FlexRay, Frame I/O Stream:

- Frame Time is 20 µs (0.00002 s). This time assumes a baud rate of 10 Mbps,
 with a cycle containing static slots only (no minislots or NIT), and frames
 on channel A only.
- Small frames at a fast rate require a larger queue size than large frames at
 a slow rate. Therefore, this default assumes static slots with 4 bytes, for
 a Frame Size of 24 bytes.
- When you create an application to stress test NI-XNET performance, it is
 possible to generate FlexRay frames faster than 20 µs. For this application,
 you must set the queue size to larger than the default.

LIN, Frame I/O Stream:

- Frame Time is 2 ms (0.002 s). This time assumes a baud rate of 20 kbps, with
 1 byte frames back to back (100 percent busload).
- For all LIN sessions, Frame Size is 24 bytes.

CAN, Other Modes:

- For Frame I/O Queued, Signal I/O XY, and Signal I/O Waveform, the Frame Time
 is different for each frame in the session (or frame within which signals
 are contained).
- For CAN frames, Frame Time is the frame property CAN Transmit Time, which
 specifies the time between successive frames (in floating-point seconds).
- If the frame's CAN Transmit Time is 0, this implies the possibility of
 back-to-back frames on the network. Nevertheless, this back-to-back traffic
 typically occurs in bursts, and the average rate over a long period of time
 is relatively slow. To keep the default queue size to a reasonable value,
 when CAN Transmit Time is 0, the formula uses a Frame Time of 50 ms (0.05
 s).
- For CAN sessions using a standard CAN cluster, the frame size is 24 bytes.
 For CAN sessions using a CAN FD cluster, the frame size may differ for each
 frame in the session. Each frame size is obtained from its XNET Frame
 Payload Length property in the database.

FlexRay, Other Modes:

- For Frame I/O Queued, Signal I/O XY, and Signal I/O Waveform, the Frame Time
 is different for each frame in the session (or frame within which signals
 are contained).
- For FlexRay frames, Frame Time is the time between successive frames (in
 floating-point seconds), calculated from cluster and frame properties. For
 example, if a cluster Cycle (cycle duration) is 10000 µs, and the frame Base
 Cycle is 0 and Cycle Repetition is 1, the frame's Transmit Time is 0.01 (10
 ms).
- For these session modes, the Frame Size is different for each frame in the
 session. Each Frame Size is obtained from its XNET Frame Payload Length
 property in the database.

LIN, Other Modes:

- For LIN frames, Frame Time is a property of the schedule running in the LIN
 master node. It is assumed that the Frame Time for a single frame always is
 larger than 8 ms, so that the default queue size is set to 64 frames
 throughout.
- For all LIN sessions, Frame Size is 24 bytes.

#### Examples

The following table lists example session configurations and the resulting
 default queue sizes.

| Session Configuration | Default Queue Size | Formula |
| --- | --- | --- |
| Frame Input Stream, CAN, Windows | 96000 | (0.4 / 0.0001) = 4000; 4000 x 24 bytes |
| Frame Output Stream, CAN, Windows | 96000 | (0.4 / 0.0001) = 4000; 4000 x 24 bytes; output is always same as input |
| Frame Input Stream, FlexRay, Windows | 480000 | (0.4 / 0.00002) = 20000; 20000 x 24 bytes |
| Frame Input Stream, CAN, LabVIEW RT | 24000 | (0.1 / 0.0001) = 1000; 1000 x 24 bytes |
| Frame Input Stream, FlexRay, LabVIEW RT | 120000 | (0.1 / 0.00002) = 5000; 5000 x 24 bytes |
| Frame Input Queued, CAN, Transmit Time 0.0, Windows | 1536[1] | (0.4 / 0.05) = 8; Transmit Time 0 uses Frame Time 50 ms; use minimum of 64 frames (64 x 24) |
| Frame Input Queued, CAN, Transmit Time 0.0005, Windows | 19200[1] | (0.4 / 0.0005) = 800; 800 x 24 bytes |
| Frame Input Queued, CAN, Transmit Time 1.0 (1 s), Windows | 1536[1] | (0.4 / 1.0) = 0.4; use minimum of 64 frames (64 x 24) |
| Frame Input Queued, FlexRay, every 2 ms cycle, payload length 4, Windows | 4800 | (0.4 / 0.002) = 200; 200 x 24 bytes |
| Frame Input Queued, FlexRay, every 2 ms cycle, payload length 16, LabVIEW RT | 2048 | (0.1 / 0.002) = 50, use minimum of 64; payload length 16 requires 32 bytes; 64 x 32 bytes |
| Signal Input XY, two CAN frames, Transmit Time 0.0 and 0.0005, Windows | 64[1] and 800[1] (read as 800) | (0.4 / 0.05) = 8, use minimum of 64; (0.4 / 0.0005) = 800; expressed as signal values |
| Signal Output XY, two CAN frames, Transmit Time 0.0 and 0.0005, Windows | 64[1] and 800[1] (read as 64) | (0.4 / 0.05) = 8, use minimum of 64; (0.4 / 0.0005) = 800; expressed as signal values |
| Signal Output Waveform, two CAN frames, 1 ms and 400 ms, resample rate 1000 Hz, Windows | 400[1] | Memory allocation is 400 and 64 frames to provide 0.4 sec of storage, queue size represents number of samples, or (0.4 x 1000.0) |
|  |  |  |

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Session

<sup>1</sup> For a CAN FD cluster, the default queue size
 is based on the frame's database payload length, which may be larger
 than 24 bytes (up to 64 bytes).

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-session.html language=enus -->
## TOPIC 00179: XNET Session Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-session.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET Session I/O name. Use the XNET Session property node to change the session configuration.

XNET Session

Reads and writes properties for an XNET Session I/O name.

Use the XNET Session property node to change the session configuration.

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-byteordr-30001.html language=enus -->
## TOPIC 00180: ByteOrdr

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-byteordr-30001.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-byteordr-30001.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Byte order in the frame payload (ring).This property defines how signal bytes are ordered in the frame payload when the frame is loaded in memory. Little endian (Intel): Higher significant signal bits are placed on higher byte addresses. Big endian (Motorola): Higher significant signal bits are plac

ByteOrdr

Byte order in the frame payload (ring).

This property
 defines how signal bytes are ordered in the frame payload when the frame is loaded in
 memory.

- Little endian (Intel): Higher significant signal bits are placed on
 higher byte addresses.
- Big endian (Motorola): Higher significant signal bits are placed on
 lower byte addresses.

If the Byte Order property does not contain a valid value,
 and you create an XNET session that uses this signal, the session returns an error. To
 ensure that the property contains a valid value, you can do one of the following:

- Use a database file (or alias) to create the session. The file formats require a
 valid value in the text for this property.
- Set a value in LabVIEW using the property node. This is needed when you create your
 own in-memory database (:memory:) rather than use a file. The property does not
 contain a default value in this case, so you must set a valid value prior to
 creating a session.

Figure 1.

[IMAGE alt='Little Endian Signal with Start Bit 12' src='GUID-3A570A5B-3D6B-4DF1-9904-B51E68070A69']

Figure 2.

skipping image GUID-9DB47DF1-ACF7-4621-BE28-5B00A4055A18

skipping image GUID-9DB47DF1-ACF7-4621-BE28-5B00A4055A18

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-comment-3030002.html language=enus -->
## TOPIC 00181: Comment

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-comment-3030002.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-comment-3030002.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Comment describing the signal object. The comment string is limited to a maximum of 65535 characters.

Comment

Comment describing the signal object.

The comment string is limited to a maximum of 65535 characters.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-default-1030004.html language=enus -->
## TOPIC 00182: Default

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-default-1030004.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-default-1030004.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Default value of the signal, specified as scaled floating point units.

Default

Default value of the signal, specified as scaled floating point units.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-frame-5030005.html language=enus -->
## TOPIC 00183: Frame

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-frame-5030005.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-frame-5030005.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Frame that contains the signal .

Frame

Frame that contains the signal .

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-mux-data-multiplexer-2030030.html language=enus -->
## TOPIC 00184: Mux.Muxer?

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-mux-data-multiplexer-2030030.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-mux-data-multiplexer-2030030.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Configures whether this signal is a data multiplexer (boolean)? When the parent frame is data multiplexed (also known as mode dependent), it contains a special signal called the multiplexer. The value of the multiplexer signal determines which subframe is used.

Mux.Muxer?

Configures whether this signal is a data multiplexer (boolean)? When the parent frame
 is data multiplexed (also known as mode dependent), it contains a special signal called
 the multiplexer. The value of the multiplexer signal determines which subframe is
 used.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-mux-subframe-5030033.html language=enus -->
## TOPIC 00185: Mux.Subfrm

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-mux-subframe-5030033.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-mux-subframe-5030033.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Subframe that contains the signal. This property is valid only when the Mux:Dynamic? property is True.

Mux.Subfrm

Subframe that contains the signal. This property is valid only when the Mux:Dynamic?
 property is True.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-numbits-30012.html language=enus -->
## TOPIC 00186: NumBits

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-numbits-30012.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-numbits-30012.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Number of bits in the frame payload (1-64). This property is required.

NumBits

Number of bits in the frame payload (1-64). This property is required.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal-start-bit-30015.html language=enus -->
## TOPIC 00187: StartBit

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal-start-bit-30015.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal-start-bit-30015.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Starting position in the frame payload. The range is 0 (lowest bit in the first byte) to 63 (highest bit in the last byte) for CAN. The range is 0 to 2031 for FlexRay. This property is required.

StartBit

Starting position in the frame payload. The range is 0 (lowest bit in the first byte)
 to 63 (highest bit in the last byte) for CAN. The range is 0 to 2031 for FlexRay. This
 property is required.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

- Characteristics
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signal.html language=enus -->
## TOPIC 00188: XNET Signal Class

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signal.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvClass`
- source_description: Reads and writes properties for an XNET Signal I/O name. Use the XNET Signal property node to configure properties for an XNET Signal I/O name.

XNET Signal

Reads and writes properties for an XNET Signal I/O name.

Use the XNET Signal property node to configure properties for an XNET Signal I/O name.

Parent topic:

NI-XNET Properties

<!--NI_TOPIC bundle=ni-xnet-lvnxg-prop-api-ref path=xnet-signalr-name-short-3030008.html language=enus -->
## TOPIC 00189: NameShort

- bundle_id: `ni-xnet-lvnxg-prop-api-ref`
- source_path: `xnet-signalr-name-short-3030008.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-prop-api-ref/raw/resource/enus/xnet-signalr-name-short-3030008.html
- document_id: `ni-xnet-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `lvProperty`
- source_description: Short name of the string. A signal name must be unique for all signals in a frame. Valid characters are lowercase letters (a–z), uppercase letters (A–Z), numbers, and underscore (_). Other special characters such as space ( ) and period (.) are not supported within the name. The short name must begi

NameShort

Short name of the string. A signal name must be unique for all signals in a
 frame.

Valid characters are lowercase letters (a–z), uppercase letters (A–Z), numbers, and underscore
 (_). Other special characters such as space ( ) and period (.) are not supported within
 the name. The short name must begin with a letter (uppercase or lowercase) or
 underscore, and not a number. The short name is limited to 128 characters.

If you write this property, it changes both short and long name.

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

- Characteristics
- Details
- Compatibility

**Long Name:**

**Class:**[XNET Signal](xnet-signal.html)

**Permissions:** Read/Write

Unlike the I/O name (long name), the short name does not include qualifiers such
 as the database, cluster, or frame name to ensure that it is unique. The short
 name is used for display purposes. The fully qualified name is available by
 using the XNET Signal I/O name as a string.

If you write this property to change the signal's short name and then use the
 original XNET Signal that contains the old name, errors can result because the
 old name cannot be found. Use the following steps to avoid this problem:

1. Get the old Name (Short) property using the property
 node.
2. Set the new Name (Short) property for the
 object.
3. Close the object using the XNET Database
 Close node. Wire the close all? 
 input as False to close only the renamed object.
4. Wire the XNET Signal as the input string to the Search and Replace
 String node with the old Name (Short) 
 value as the search string and the new Name (Short) 
 value as the replacement string. This replaces the short name in the XNET
 Signal, while retaining the other text that ensures a unique name.

**Where This Property Is Available:**

Desktop OS: Windows

Web Server:

Parent topic:

XNET Signal
