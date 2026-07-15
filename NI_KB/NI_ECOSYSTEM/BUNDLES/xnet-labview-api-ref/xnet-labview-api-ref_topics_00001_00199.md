# NI DOCUMENT BUNDLE: xnet-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=xnet-labview-api-ref start=1 end=199 -->
<!--NI_TOPIC bundle=xnet-labview-api-ref path=menus/categories/measurement/xnet-mnu.html language=enus -->
## TOPIC 00001: XNET

- bundle_id: `xnet-labview-api-ref`
- source_path: `menus/categories/measurement/xnet-mnu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/menus/categories/measurement/xnet-mnu.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI-XNET is the National Instruments software for embedded network protocols, such as Controller Area Network (CAN) and FlexRay. Embedded network protocols are used in systems of distributed electronics, such as the powertrain control system within an automobile. National Instruments XNET hardware pr

### XNET

NI-XNET is the National Instruments software for embedded network protocols, such as Controller Area Network (CAN) and FlexRay. Embedded network protocols are used in systems of distributed electronics, such as the powertrain control system within an automobile. National Instruments XNET hardware products connect LabVIEW to these systems in order to test or control the electronics.

This palette provides VIs, property nodes, and I/O name constants for NI-XNET.

[IMAGE alt='icon' src='xnet-mnu.png']

- [XNET Session](../../../vi-lib/xnet/xnet-llb/xnet-session-vi.html) This constant provides the constant form of the XNET Session I/O name. You drag a constant to the block diagram of your VI, then select a session. You can change constants only during configuration, prior to running the VI.
- [XNET Create Session VI](../../../vi-lib/xnet/xnet-llb/xnet-create-session-vi.html) Creates an XNET session to read/write data on the CAN or FlexRay network. The instances of this polymorphic VI specify the session mode.
- [XNET Session Property Node](../../../vi-lib/xnet/xnet-llb/xnet-session-property-node-vi.html) Property node used to read/write properties for an XNET Session I/O name.
- [XNET Read VI](../../../vi-lib/xnet/xnet-llb/xnet-read-vi.html) Reads data from the network using an XNET session.
- [XNET Write VI](../../../vi-lib/xnet/xnet-llb/xnet-write-vi.html) Writes data to the network using an XNET session.
- [Database](../../../menus/categories/measurement/xnet/xnet-db-mnu.html) This subpalette includes functions for accessing databases that specify the embedded network configuration, including frame and signal data that is transferred. You can use these functions to retrieve information from database files, create new database objects in LabVIEW, and edit and save new database files.
- [Notify](../../../menus/categories/measurement/xnet/xnet-notify-mnu.html) This subpalette includes functions for waiting on events from XNET hardware, including creation of a LabVIEW timing source.
- [Advanced](../../../menus/categories/measurement/xnet/xnet-adv-mnu.html) This subpalette includes advanced functions for controlling the state of NI-XNET sessions, connecting hardware terminals, and retrieving information about the XNET hardware in your system.
- [IP Stack](../../../menus/categories/measurement/xnet/xnet-internal-ipstack-mnu.html) This subpalette includes functions for creating and configuring a network socket for TCP and UDP communication.
- [XNET Controls](../../../vi-lib/userdefined/high-color/xnet/dir-mnu.html) NI-XNET is the National Instruments software for embedded network protocols, such as Controller Area Network (CAN) and FlexRay. Embedded network protocols are used in systems of distributed electronics, such as the powertrain control system within an automobile. National Instruments XNET hardware products connect LabVIEW to these systems in order to test or control the electronics. This palette provides NI-XNET I/O name controls for your front panel.

<!--NI_TOPIC bundle=xnet-labview-api-ref path=menus/categories/measurement/xnet/xnet-internal-ipstack-mnu.html language=enus -->
## TOPIC 00002: IP Stack

- bundle_id: `xnet-labview-api-ref`
- source_path: `menus/categories/measurement/xnet/xnet-internal-ipstack-mnu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/menus/categories/measurement/xnet/xnet-internal-ipstack-mnu.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This subpalette includes functions for creating and configuring a network socket for TCP and UDP communication. icon

### IP Stack

This subpalette includes functions for creating and configuring a network socket for TCP and UDP communication.

[IMAGE alt='icon' src='xnet-internal-ipstack-mnu.png']

- [XNET IP Stack Create VI](../../../../vi-lib/xnet/xnet-llb/xnet-ip-stack-create-vi.html) Creates an XNET IP stack to use for TCP and/or UDP communication.
- [TCP](../../../../menus/categories/measurement/xnet/xnet-internal-ipstack-tcp-mnu.html) The VIs in this subpalette use the XNET TCP Socket for TCP communication. The NI-XNET Socket API for TCP is analogous to LabVIEW's built-in TCP palette for the OS stack.
- [UDP](../../../../menus/categories/measurement/xnet/xnet-internal-ipstack-udp-mnu.html) The VIs in this subpalette use the XNET UDP Socket for UDP communication. The NI-XNET Socket API for UDP is analogous to LabVIEW's built-in UDP palette for the OS stack.
- [XNET IP Stack Clear VI](../../../../vi-lib/xnet/xnet-llb/xnet-ip-stack-clear-vi.html) Clears (closes) the XNET IP Stack.
- [XNET IP Stack Wait VI](../../../../vi-lib/xnet/xnet-llb/xnet-ip-stack-wait-vi.html) Waits for interface(s) in the XNET IP Stack to be ready for communication.
- [XNET IP Stack Get Info VI](../../../../vi-lib/xnet/xnet-llb/xnet-ip-stack-get-info-vi.html) Gets runtime information for an XNET IP Stack.

Parent topic:

XNET

<!--NI_TOPIC bundle=xnet-labview-api-ref path=menus/categories/measurement/xnet/xnet-internal-ipstack-tcp-mnu.html language=enus -->
## TOPIC 00003: TCP

- bundle_id: `xnet-labview-api-ref`
- source_path: `menus/categories/measurement/xnet/xnet-internal-ipstack-tcp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/menus/categories/measurement/xnet/xnet-internal-ipstack-tcp-mnu.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VIs in this subpalette use the XNET TCP Socket for TCP communication. The NI-XNET Socket API for TCP is analogous to LabVIEW's built-in TCP palette for the OS stack. icon

### TCP

The VIs in this subpalette use the XNET TCP Socket for TCP communication. The NI-XNET Socket API for TCP is analogous to LabVIEW's built-in TCP palette for the OS stack.

[IMAGE alt='icon' src='xnet-internal-ipstack-tcp-mnu.png']

- [XNET TCP Socket Open VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-open-vi.html) Opens a TCP network connection using a specified address and port.
- [XNET TCP Socket Write VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-write-vi.html) Writes data to a TCP network connection.
- [XNET TCP Socket Read VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-read-vi.html) Reads a number of bytes from a TCP network connection.
- [XNET TCP Socket Close VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-close-vi.html) Closes a TCP network connection.
- [XNET TCP Socket Create Listener VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-create-listener-vi.html) Use this node with XNET TCP Socket Wait on Listener to create and listen for connections on the server.
- [XNET TCP Socket Wait on Listener VI](../../../../vi-lib/xnet/xnet-llb/xnet-tcp-socket-wait-on-listener-vi.html) Waits for an accepted TCP network connection.
- [XNET TCP Socket Property Node](../../../../vi-lib/xnet/xnet-llb/property-node-xnet-tcp-socket-vi.html) Provides properties that can be used with the XNET TCP Socket VIs.

Parent topic:

IP Stack

<!--NI_TOPIC bundle=xnet-labview-api-ref path=menus/categories/measurement/xnet/xnet-internal-ipstack-udp-mnu.html language=enus -->
## TOPIC 00004: UDP

- bundle_id: `xnet-labview-api-ref`
- source_path: `menus/categories/measurement/xnet/xnet-internal-ipstack-udp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/menus/categories/measurement/xnet/xnet-internal-ipstack-udp-mnu.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VIs in this subpalette use the XNET UDP Socket for UDP communication. The NI-XNET Socket API for UDP is analogous to LabVIEW's built-in UDP palette for the OS stack. icon

### UDP

The VIs in this subpalette use the XNET UDP Socket for UDP communication. The NI-XNET Socket API for UDP is analogous to LabVIEW's built-in UDP palette for the OS stack.

[IMAGE alt='icon' src='xnet-internal-ipstack-udp-mnu.png']

- [XNET UDP Socket Open VI](../../../../vi-lib/xnet/xnet-llb/xnet-udp-socket-open-vi.html) Opens a UDP socket to send a datagram to a single receiver on the port you specify. If you want to send a single datagram to multiple receivers in parallel, use the XNET UDP Multicast Open node.
- [XNET UDP Socket Write VI](../../../../vi-lib/xnet/xnet-llb/xnet-udp-socket-write-vi.html) Writes a datagram to a remote UDP port. To send multicast datagrams, specify the multicast group address in the remote address input.
- [XNET UDP Socket Read VI](../../../../vi-lib/xnet/xnet-llb/xnet-udp-socket-read-vi.html) Reads a datagram from a UDP socket.
- [XNET UDP Socket Close VI](../../../../vi-lib/xnet/xnet-llb/xnet-udp-socket-close-vi.html) Closes a UDP socket and frees system resources.
- [XNET UDP Socket Multicast Open VI](../../../../vi-lib/xnet/xnet-llb/xnet-udp-socket-multicast-open-vi.html) Opens a UDP multicast socket to send a single datagram to multiple receivers in parallel on the port you specify.
- [XNET UDP Socket Property Node](../../../../vi-lib/xnet/xnet-llb/property-node-xnet-udp-socket-vi.html) Provides properties that can be used with the XNET UDP Socket VIs.
- [XNET UDP Socket Invoke Node](../../../../vi-lib/xnet/xnet-llb/invoke-node-xnet-udp-socket-vi.html) Methods in this node can be used with the XNET UDP Socket VIs.

Parent topic:

IP Stack

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc.html language=enus -->
## TOPIC 00005: XNET Refnum

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### XNET Refnum

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertycluster64bitbaudrate.html language=enus -->
## TOPIC 00006: 64bit Baud Rate

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertycluster64bitbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertycluster64bitbaudrate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Baud rate used by all ECUs in the cluster. Remarks The following table lists the characteristics of this property. Short Name BaudRate64 Data type cu64.png Permissions Read/Write

### 64bit Baud Rate

Baud rate used by all ECUs in the cluster.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | BaudRate64 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterapplicationprotocol.html language=enus -->
## TOPIC 00007: Application Protocol

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterapplicationprotocol.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterapplicationprotocol.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Higher-level application protocol of the cluster. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name ApplProtocol Data type cu32.png Permissions Read/Write None 0 J1939 1

### Application Protocol

Higher-level application protocol of the cluster. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ApplProtocol |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| None | 0 |  |
| --- | --- | --- |
| J1939 | 1 |  |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclustercan64bitfdbaudrate.html language=enus -->
## TOPIC 00008: CAN:64bit FD Baud Rate

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclustercan64bitfdbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclustercan64bitfdbaudrate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fast baud rate used by all ECUs in this cluster for CAN FD with Baud Rate Switch. Remarks The following table lists the characteristics of this property. Short Name CAN.FdBaudRate64 Data type cu64.png Permissions Read/Write

### CAN:64bit FD Baud Rate

Fast baud rate used by all ECUs in this cluster for CAN FD with Baud Rate Switch.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CAN.FdBaudRate64 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclustercanfdisomode.html language=enus -->
## TOPIC 00009: CAN:FD ISO Mode

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclustercanfdisomode.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclustercanfdisomode.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates to use the pre-ISO definition of the CAN FD specification. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name CAN.FdIsoMode Data type cu32.png Permissions Read Only ISO 0 Non ISO 1 ISO Legacy 2

### CAN:FD ISO Mode

Indicates to use the pre-ISO definition of the CAN FD specification. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CAN.FdIsoMode |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| ISO | 0 |  |
| --- | --- | --- |
| Non ISO | 1 |  |
| ISO Legacy | 2 |  |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclustercomment.html language=enus -->
## TOPIC 00010: Comment

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclustercomment.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclustercomment.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Comment describing the cluster (string). Remarks The following table lists the characteristics of this property. Short Name Comment Data type cstr.png Permissions Read/Write

### Comment

Comment describing the cluster (string).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Comment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterconfigstatus.html language=enus -->
## TOPIC 00011: Configuration Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterconfigstatus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterconfigstatus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuration status of the cluster. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true. Remarks The following table lists the characteristics of this property. Short Name ConfigStatus Data type ci32.png Permissions Read Only

### Configuration Status

Configuration status of the cluster. This property is used only if you change the Database property **Show Invalid From Open?** from false (default) to true.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConfigStatus |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterdatabase.html language=enus -->
## TOPIC 00012: Database

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterdatabase.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterdatabase.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database that contains this cluster (XNET Database I/O Name). Remarks The following table lists the characteristics of this property. Short Name Database Data type cgenclassrntag.png Permissions Read Only

### Database

Database that contains this cluster (XNET Database I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Database |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterecus.html language=enus -->
## TOPIC 00013: ECUs

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterecus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterecus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of ECUs contained in the cluster (array of XNET ECU I/O Name). Remarks The following table lists the characteristics of this property. Short Name ECUs Data type c1dgenclassrntag.png Permissions Read Only

### ECUs

Array of ECUs contained in the cluster (array of XNET ECU I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ECUs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayactionpointoffset.html language=enus -->
## TOPIC 00014: FlexRay:Action Point Offset

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayactionpointoffset.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayactionpointoffset.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of macroticks (MT) that the action point is offset from the beginning of a static slot or symbol window (0-63). Remarks The following table lists the characteristics of this property. Short Name FlexRay.ActPtOff Data type cu32.png Permissions Read/Write

### FlexRay:Action Point Offset

Number of macroticks (MT) that the action point is offset from the beginning of a static slot or symbol window (0-63).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.ActPtOff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraychannels.html language=enus -->
## TOPIC 00015: FlexRay:Channels

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraychannels.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraychannels.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Channels that are used by the cluster. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name FlexRay.Channels Data type cu32.png Permissions Read/Write A 1 B 2 A and B 3

### FlexRay:Channels

Channels that are used by the cluster. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.Channels |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| A | 1 |  |
| --- | --- | --- |
| B | 2 |  |
| A and B | 3 |  |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraycycle.html language=enus -->
## TOPIC 00016: FlexRay:Cycle

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraycycle.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraycycle.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Duration of the cycle, expressed in microseconds (10-16000). Remarks The following table lists the characteristics of this property. Short Name FlexRay.Cycle Data type cu32.png Permissions Read/Write

### FlexRay:Cycle

Duration of the cycle, expressed in microseconds (10-16000).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.Cycle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraydynamicslotidlephase.html language=enus -->
## TOPIC 00017: FlexRay:Dynamic Slot Idle Phase

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraydynamicslotidlephase.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraydynamicslotidlephase.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Duration of the idle phase within a dynamic slot (0-2 minislot) Remarks The following table lists the characteristics of this property. Short Name FlexRay.DynSlotIdlPh Data type cu32.png Permissions Read/Write

### FlexRay:Dynamic Slot Idle Phase

Duration of the idle phase within a dynamic slot (0-2 minislot)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.DynSlotIdlPh |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylatestusabledynamicslot.html language=enus -->
## TOPIC 00018: FlexRay:Latest Usable Dynamic Slot

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylatestusabledynamicslot.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylatestusabledynamicslot.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the highest slot ID in the dynamic segment that can still transmit a full-length frame, provided no other frames have been sent in the dynamic segment. Remarks The following table lists the characteristics of this property. Short Name FlexRay.LatestUsableDyn Data type cu32.png Permissions

### FlexRay:Latest Usable Dynamic Slot

Indicates the highest slot ID in the dynamic segment that can still transmit a full-length frame, provided no other frames have been sent in the dynamic segment.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.LatestUsableDyn |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylistennoise.html language=enus -->
## TOPIC 00019: FlexRay:Listen Noise

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylistennoise.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraylistennoise.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Upper limit for the startup and wakeup listen timeout in the presence of noise. Remarks The following table lists the characteristics of this property. Short Name FlexRay.LisNoise Data type cu32.png Permissions Read/Write

### FlexRay:Listen Noise

Upper limit for the startup and wakeup listen timeout in the presence of noise.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.LisNoise |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraymacropercycle.html language=enus -->
## TOPIC 00020: FlexRay:Macro Per Cycle

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraymacropercycle.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraymacropercycle.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of macroticks per cycle (10-16000). Remarks The following table lists the characteristics of this property. Short Name FlexRay.MacroPerCycle Data type cu32.png Permissions Read/Write

### FlexRay:Macro Per Cycle

Number of macroticks per cycle (10-16000).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.MacroPerCycle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayminislotactionpointoffset.html language=enus -->
## TOPIC 00021: FlexRay:Minislot Action Point Offset

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayminislotactionpointoffset.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayminislotactionpointoffset.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of macroticks (MT) the minislot action point is offset from the beginning of a minislot (0-31). Remarks The following table lists the characteristics of this property. Short Name FlexRay.MinislotActPt Data type cu32.png Permissions Read/Write

### FlexRay:Minislot Action Point Offset

Number of macroticks (MT) the minislot action point is offset from the beginning of a minislot (0-31).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.MinislotActPt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynetworkmanagementvectorlength.html language=enus -->
## TOPIC 00022: FlexRay:Network Management Vector Length

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynetworkmanagementvectorlength.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynetworkmanagementvectorlength.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Length of the Network Management vector in bytes (0-12) Remarks The following table lists the characteristics of this property. Short Name FlexRay.NMVecLen Data type cu32.png Permissions Read/Write

### FlexRay:Network Management Vector Length

Length of the Network Management vector in bytes (0-12)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.NMVecLen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberminislots.html language=enus -->
## TOPIC 00023: FlexRay:Number Of Minislots

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberminislots.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberminislots.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of minislots in the dynamic segment (0-7986). Remarks The following table lists the characteristics of this property. Short Name FlexRay.NumMinislt Data type cu32.png Permissions Read/Write

### FlexRay:Number Of Minislots

Number of minislots in the dynamic segment (0-7986).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.NumMinislt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberstaticslots.html language=enus -->
## TOPIC 00024: FlexRay:Number Of Static Slots

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberstaticslots.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraynumberstaticslots.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of static slots in the static segment (2-1023). Remarks The following table lists the characteristics of this property. Short Name FlexRay.NumStatSlt Data type cu32.png Permissions Read/Write

### FlexRay:Number Of Static Slots

Number of static slots in the static segment (2-1023).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.NumStatSlt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayoffsetcorrectionstart.html language=enus -->
## TOPIC 00025: FlexRay:Offset Correction Start

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayoffsetcorrectionstart.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayoffsetcorrectionstart.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start of the offset correction phase within the Network Idle Time (NIT), expressed as the number of macroticks from the start of cycle (9-15999). Remarks The following table lists the characteristics of this property. Short Name FlexRay.OffCorSt Data type cu32.png Permissions Read/Write

### FlexRay:Offset Correction Start

Start of the offset correction phase within the Network Idle Time (NIT), expressed as the number of macroticks from the start of cycle (9-15999).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.OffCorSt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthdynamicmax.html language=enus -->
## TOPIC 00026: FlexRay:Payload Length Dynamic Maximum

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthdynamicmax.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthdynamicmax.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum payload length of all dynamic frames in this cluster, expressed as bytes (0-254). Remarks The following table lists the characteristics of this property. Short Name FlexRay.PayldLenDynMax Data type cu32.png Permissions Read/Write

### FlexRay:Payload Length Dynamic Maximum

Maximum payload length of all dynamic frames in this cluster, expressed as bytes (0-254).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.PayldLenDynMax |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthstatic.html language=enus -->
## TOPIC 00027: FlexRay:Payload Length Static

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthstatic.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraypayloadlengthstatic.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Payload length of all static frames in this cluster, expressed as bytes (0-254). Remarks The following table lists the characteristics of this property. Short Name FlexRay.PayldLenSt Data type cu32.png Permissions Read/Write

### FlexRay:Payload Length Static

Payload length of all static frames in this cluster, expressed as bytes (0-254).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.PayldLenSt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraystaticslot.html language=enus -->
## TOPIC 00028: FlexRay:Static Slot

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraystaticslot.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraystaticslot.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Duration of a slot in the static segment, expressed in macroticks (4-659) Remarks The following table lists the characteristics of this property. Short Name FlexRay.StatSlot Data type cu32.png Permissions Read/Write

### FlexRay:Static Slot

Duration of a slot in the static segment, expressed in macroticks (4-659)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.StatSlot |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindow.html language=enus -->
## TOPIC 00029: FlexRay:Symbol Window

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindow.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindow.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Duration of the symbol window, expressed in macroticks (0-139) Remarks The following table lists the characteristics of this property. Short Name FlexRay.SymWin Data type cu32.png Permissions Read/Write

### FlexRay:Symbol Window

Duration of the symbol window, expressed in macroticks (0-139)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.SymWin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindowstart.html language=enus -->
## TOPIC 00030: FlexRay:Symbol Window Start

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindowstart.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysymbolwindowstart.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start of symbol window, expressed as the offset in macroticks (MT) from the start of cycle. Remarks The following table lists the characteristics of this property. Short Name FlexRay.SymWinStart Data type cu32.png Permissions Read Only

### FlexRay:Symbol Window Start

Start of symbol window, expressed as the offset in macroticks (MT) from the start of cycle.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.SymWinStart |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysyncnodemax.html language=enus -->
## TOPIC 00031: FlexRay:Sync Node Max

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysyncnodemax.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraysyncnodemax.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum number of nodes (ECUs) that may transmit sync frames (FlexRay:Sync? true). (2-15). Remarks The following table lists the characteristics of this property. Short Name FlexRay.SyncNodeMax Data type cu32.png Permissions Read/Write

### FlexRay:Sync Node Max

Maximum number of nodes (ECUs) that may transmit sync frames (**FlexRay:Sync?** true). (2-15).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.SyncNodeMax |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayusewakeup.html language=enus -->
## TOPIC 00032: FlexRay:Use Wakeup?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayusewakeup.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexrayusewakeup.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the FlexRay cluster supports wakeup. Remarks The following table lists the characteristics of this property. Short Name FlexRay.UseWakeup? Data type cbool.png Permissions Read/Write

### FlexRay:Use Wakeup?

Specifies whether the FlexRay cluster supports wakeup.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.UseWakeup? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymbolrxlow.html language=enus -->
## TOPIC 00033: FlexRay:Wakeup Symbol Rx Low

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymbolrxlow.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymbolrxlow.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of bit times used to test the low portion of a received wakeup symbol (10-55) Remarks The following table lists the characteristics of this property. Short Name FlexRay.WakeSymRxLow Data type cu32.png Permissions Read/Write

### FlexRay:Wakeup Symbol Rx Low

Number of bit times used to test the low portion of a received wakeup symbol (10-55)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.WakeSymRxLow |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxidle.html language=enus -->
## TOPIC 00034: FlexRay:Wakeup Symbol Tx Idle

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxidle.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxidle.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of bit times used to transmit the idle part of the wakeup symbol (45-180). Remarks The following table lists the characteristics of this property. Short Name FlexRay.WakeSymTxIdl Data type cu32.png Permissions Read/Write

### FlexRay:Wakeup Symbol Tx Idle

Number of bit times used to transmit the idle part of the wakeup symbol (45-180).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.WakeSymTxIdl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxlow.html language=enus -->
## TOPIC 00035: FlexRay:Wakeup Symbol Tx Low

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxlow.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterflexraywakeupsymboltxlow.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of bit times used to transmit the low part of the wakeup symbol (15-60). Remarks The following table lists the characteristics of this property. Short Name FlexRay.WakeSymTxLow Data type cu32.png Permissions Read/Write

### FlexRay:Wakeup Symbol Tx Low

Number of bit times used to transmit the low part of the wakeup symbol (15-60).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.WakeSymTxLow |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterframes.html language=enus -->
## TOPIC 00036: Frames

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterframes.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterframes.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of frames transmitted by an ECU in the cluster (array of XNET Frame I/O Name). Remarks The following table lists the characteristics of this property. Short Name Frms Data type c1dgenclassrntag.png Permissions Read Only

### Frames

Array of frames transmitted by an ECU in the cluster (array of XNET Frame I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frms |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlinschedules.html language=enus -->
## TOPIC 00037: LIN:Schedules

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlinschedules.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlinschedules.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of schedules for this LIN cluster (array of XNET LIN Schedule I/O Name). While the XNET interface is running, you can use the XNET Write (State LIN Schedule Change) VI to change the running schedule. No schedule runs by default, so you must write a schedule request at least once in your applic

### LIN:Schedules

Array of schedules for this LIN cluster (array of XNET LIN Schedule I/O Name).

While the XNET interface is running, you can use the **XNET Write (State LIN Schedule Change)** VI to change the running schedule. No schedule runs by default, so you must write a schedule request at least once in your application.

For the **XNET Write (State LIN Schedule Change)** VI, if you use an index to specify the schedule, that index is the position in this array (starting at 0). The database file and/or the order that you create schedules at run time determine the position.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.Schedules |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlintick.html language=enus -->
## TOPIC 00038: LIN:Tick

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlintick.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterlintick.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Relative time between LIN ticks (relative F64 in seconds). The Delay property of the XNET LIN Schedule Entry must be a multiple of this tick. This tick is referred to as the 'timebase' in LIN specification. Remarks The following table lists the characteristics of this property. Short Name LIN.Tick D

### LIN:Tick

Relative time between LIN ticks (relative F64 in seconds). The **Delay** property of the **XNET LIN Schedule Entry** must be a multiple of this tick.

This tick is referred to as the 'timebase' in LIN specification.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.Tick |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-cluster/propertyclusterpdus.html language=enus -->
## TOPIC 00039: PDUs

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-cluster/propertyclusterpdus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-cluster/propertyclusterpdus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of PDUs contained in the cluster (array of XNET PDU I/O Name). Remarks The following table lists the characteristics of this property. Short Name PDUs Data type c1dgenclassrntag.png Permissions Read Only

### PDUs

Array of PDUs contained in the cluster (array of XNET PDU I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDUs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Cluster Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-database/propertydatabaseclusters.html language=enus -->
## TOPIC 00040: Clusters

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-database/propertydatabaseclusters.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-database/propertydatabaseclusters.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of clusters (networks) contained in the database (array of XNET Cluster I/O Name). Remarks The following table lists the characteristics of this property. Short Name Clsts Data type c1dgenclassrntag.png Permissions Read Only

### Clusters

Array of clusters (networks) contained in the database (array of XNET Cluster I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Clsts |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Database Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device-p.html language=enus -->
## TOPIC 00041: XNET Device Properties

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device-p.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device-p.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### XNET Device Properties

- [Form Factor](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceformfactor.html) Physical form factor of the device, such as PXI, PCI, and so on. This property is a ring (enumerated list).
- [Interfaces](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfaces.html) Array of interfaces contained within this device (array of XNET Interface I/O Name).
- [Interfaces (All)](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfacesall.html) Array of interfaces (including those without a transceiver cable) contained within this device (array of XNET Interface I/O Name).
- [Number of Ports](../../../resource/objmgr/xnet-rc/xnet-device/propertydevicenumberofports.html) Number of physical ports (connectors) on the NI hardware device. For FlexRay, a port consists of both channel A and channel B. A physical port is assigned to a logical interface name using the Measurement and Automation Explorer (MAX).
- [Number of Ports (All)](../../../resource/objmgr/xnet-rc/xnet-device/propertydevicenumberofportsall.html) Number of physical ports (connectors) on the NI hardware device. This includes the ports without a transceiver cable. For FlexRay, a port consists of both channel A and channel B. A physical port is assigned to a logical interface name using the Measurement and Automation Explorer (MAX).
- [Product Name](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceproductname.html) Product name of the device (string).
- [Product Number](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceproductnumber.html) Numeric portion of the product name This number is 4 digits.
- [Serial Number](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceserialnumber.html) Serial number. This number is typically shown in hexadecimal within a label on the device.
- [Slot Number](../../../resource/objmgr/xnet-rc/xnet-device/propertydeviceslotnumber.html) Slot number. Physical slot in which the device (module) is located. For PXI and C Series, this is the slot number within the chassis.

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydeviceformfactor.html language=enus -->
## TOPIC 00042: Form Factor

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydeviceformfactor.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydeviceformfactor.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Physical form factor of the device, such as PXI, PCI, and so on. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name FormFac Data type cu32.png Permissions Read Only PXI 0 PXIe 3 PCI 1 PCIe 5 C Series 2 USB 4

### Form Factor

Physical form factor of the device, such as PXI, PCI, and so on. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FormFac |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| PXI | 0 |  |
| --- | --- | --- |
| PXIe | 3 |  |
| PCI | 1 |  |
| PCIe | 5 |  |
| C Series | 2 |  |
| USB | 4 |  |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfaces.html language=enus -->
## TOPIC 00043: Interfaces

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfaces.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfaces.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of interfaces contained within this device (array of XNET Interface I/O Name). Remarks The following table lists the characteristics of this property. Short Name Intfs Data type c1dgenclassrntag.png Permissions Read Only

### Interfaces

Array of interfaces contained within this device (array of XNET Interface I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intfs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfacesall.html language=enus -->
## TOPIC 00044: Interfaces (All)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfacesall.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydeviceinterfacesall.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of interfaces (including those without a transceiver cable) contained within this device (array of XNET Interface I/O Name). Remarks The following table lists the characteristics of this property. Short Name IntfsAll Data type c1dgenclassrntag.png Permissions Read Only

### Interfaces (All)

Array of interfaces (including those without a transceiver cable) contained within this device (array of XNET Interface I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IntfsAll |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydevicenumberofportsall.html language=enus -->
## TOPIC 00045: Number of Ports (All)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydevicenumberofportsall.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydevicenumberofportsall.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of physical ports (connectors) on the NI hardware device. This includes the ports without a transceiver cable. For FlexRay, a port consists of both channel A and channel B. A physical port is assigned to a logical interface name using the Measurement and Automation Explorer (MAX). Remarks The

### Number of Ports (All)

Number of physical ports (connectors) on the NI hardware device. This includes the ports without a transceiver cable. For FlexRay, a port consists of both channel A and channel B. A physical port is assigned to a logical interface name using the Measurement and Automation Explorer (MAX).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumPortsAll |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydeviceproductname.html language=enus -->
## TOPIC 00046: Product Name

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydeviceproductname.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydeviceproductname.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Product name of the device (string). Remarks The following table lists the characteristics of this property. Short Name ProductName Data type cstr.png Permissions Read Only

### Product Name

Product name of the device (string).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ProductName |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-device/propertydeviceserialnumber.html language=enus -->
## TOPIC 00047: Serial Number

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-device/propertydeviceserialnumber.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-device/propertydeviceserialnumber.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serial number. This number is typically shown in hexadecimal within a label on the device. Remarks The following table lists the characteristics of this property. Short Name SerNum Data type cu32.png Permissions Read Only

### Serial Number

Serial number. This number is typically shown in hexadecimal within a label on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SerNum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Device Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu-p.html language=enus -->
## TOPIC 00048: XNET ECU Properties

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu-p.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu-p.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### XNET ECU Properties

- [Cluster](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecucluster.html) Cluster that contains this ECU (XNET Cluster I/O Name).
- [Comment](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecucomment.html) Comment describing the ECU (string).
- [Configuration Status](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuconfigstatus.html) Configuration status of the ECU. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true.
- [FlexRay:Coldstart?](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecucoldstart.html) Indicates that the ECU transmits a startup frame. This property is true when one of the frames in the ECU's Frames Transmitted has the property Startup? true. This startup frame can be accessed from the FlexRay:Startup Frame property.
- [FlexRay:Connected Channels](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuflexrayconnectedchannels.html) Specifies the channel(s) that the FlexRay ECU (node) is physically connected to. The default value of this property is all channels available on the cluster.
- [FlexRay:Startup Frame](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecustartupframe.html) When FlexRay:Coldstart? is true, this indicates the startup frame that the ECU transmits (XNET Frame I/O Name). When FlexRay:Coldstart? is false, this I/O name is empty (invalid). You can use this frame to simulate the ECU, thereby making the National Instruments FlexRay interface operate as a coldstart node. To do this, use the Session property node to set Interface:FlexRay:Key Slot Identifier to the Identifier of the frame referenced by this property.
- [FlexRay:Wakeup Channels](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuflexraywakeupchannels.html) Specifies the channel(s) on which the FlexRay ECU (node) is allowed to generate the wake-up pattern. The default value of this property is not to be a wakeup node.
- [FlexRay:Wakeup Pattern](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuflexraywakeuppattern.html) Specifies the number of repetitions of the wakeup symbol that are combined to form a wakeup pattern when the FlexRay ECU (node) enters the POC:WAKEUP_SEND state.
- [Frames Received](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuframesreceived.html) Array of frames that the ECU receives (array of XNET Frame I/O Name).
- [Frames Transmitted](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuframestransmitted.html) Array of frames that the ECU transmits (array of XNET Frame I/O Name).
- [LIN:Configured NAD](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinconfigurednad.html) Configured NAD of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services.
- [LIN:Function ID](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinfunctionid.html) 16-bit value identifying the function of the LIN node (ECU).
- [LIN:Initial NAD](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculininitialnad.html) Initial NAD of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services.
- [LIN:Master?](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinmaster.html) Is this ECU the LIN master (true) or slave (false)? Default is false.
- [LIN:P2min](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinp2min.html) The minimum time in seconds between reception of the last frame of the diagnostic request and the response sent by the node.
- [LIN:Protocol Version](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinprotocolversion.html) Version of the LIN standard used by this ECU. This property is a ring (enumerated list). For an ECU created in-memory ( XNET Database Create (ECU).vi ), the default is the newest protocol version supported by NI-XNET.
- [LIN:STmin](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinstmin.html) The minimum time in seconds the node requires to prepare for the next frame of the diagnostic service.
- [LIN:Supplier ID](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyeculinsupplierid.html) 16-bit value identifying the supplier of the LIN node (ECU).
- [Name (Short)](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecuname.html) Short name of the ECU (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database and cluster name. If you write this property, it changes both short and long name (see Detailed help ).
- [SAE J1939:Node Name](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939nodename.html) SAE J1939 Node Name for this ECU. This is a 64bit quantity that uniquely identifies the ECU. NI-XNET starts Address Claiming with this node name when the ECU is assigned to the session.
- [SAE J1939:Preferred Address](../../../resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939preferredaddress.html) Preferred SAE J1939 Address for this ECU. NI-XNET starts Address Claiming with this address when the ECU is assigned to the session.

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecucoldstart.html language=enus -->
## TOPIC 00049: FlexRay:Coldstart?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecucoldstart.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecucoldstart.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the ECU transmits a startup frame. This property is true when one of the frames in the ECU's Frames Transmitted has the property Startup? true. This startup frame can be accessed from the FlexRay:Startup Frame property. Remarks The following table lists the characteristics of this pro

### FlexRay:Coldstart?

Indicates that the ECU transmits a startup frame. This property is true when one of the frames in the ECU's **Frames Transmitted** has the property **Startup?** true. This startup frame can be accessed from the **FlexRay:Startup Frame** property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.Coldstart? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecuconfigstatus.html language=enus -->
## TOPIC 00050: Configuration Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecuconfigstatus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecuconfigstatus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuration status of the ECU. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true. Remarks The following table lists the characteristics of this property. Short Name ConfigStatus Data type ci32.png Permissions Read Only

### Configuration Status

Configuration status of the ECU. This property is used only if you change the Database property **Show Invalid From Open?** from false (default) to true.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConfigStatus |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecuframestransmitted.html language=enus -->
## TOPIC 00051: Frames Transmitted

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecuframestransmitted.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecuframestransmitted.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of frames that the ECU transmits (array of XNET Frame I/O Name). Remarks The following table lists the characteristics of this property. Short Name FrmsTx Data type c1dgenclassrntag.png Permissions Read/Write

### Frames Transmitted

Array of frames that the ECU transmits (array of XNET Frame I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FrmsTx |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyeculinconfigurednad.html language=enus -->
## TOPIC 00052: LIN:Configured NAD

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyeculinconfigurednad.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyeculinconfigurednad.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configured NAD of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services. Remarks The following table lists the characteristics of this property. Short Name LIN.ConfigNAD Data type cu32.png Permissions Read/Write

### LIN:Configured NAD

Configured NAD of a LIN slave node. NAD is the address of a slave node and is used in diagnostic services.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.ConfigNAD |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyeculinfunctionid.html language=enus -->
## TOPIC 00053: LIN:Function ID

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyeculinfunctionid.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyeculinfunctionid.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: 16-bit value identifying the function of the LIN node (ECU). Remarks The following table lists the characteristics of this property. Short Name LIN.FunctionID Data type cu32.png Permissions Read/Write

### LIN:Function ID

16-bit value identifying the function of the LIN node (ECU).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.FunctionID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyeculinprotocolversion.html language=enus -->
## TOPIC 00054: LIN:Protocol Version

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyeculinprotocolversion.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyeculinprotocolversion.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the LIN standard used by this ECU. This property is a ring (enumerated list). For an ECU created in-memory (XNET Database Create (ECU).vi), the default is the newest protocol version supported by NI-XNET. Remarks The following table lists the characteristics of this property. Short Name L

### LIN:Protocol Version

Version of the LIN standard used by this ECU. This property is a ring (enumerated list).

For an ECU created in-memory (**XNET Database Create (ECU).vi**), the default is the newest protocol version supported by NI-XNET.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.ProtclVer |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| 1.2 | 2 |  |
| --- | --- | --- |
| 1.3 | 3 |  |
| 2.0 | 4 |  |
| 2.1 | 5 |  |
| 2.2 | 6 |  |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyeculinstmin.html language=enus -->
## TOPIC 00055: LIN:STmin

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyeculinstmin.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyeculinstmin.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The minimum time in seconds the node requires to prepare for the next frame of the diagnostic service. Remarks The following table lists the characteristics of this property. Short Name LIN.STmin Data type cdbl.png Permissions Read/Write

### LIN:STmin

The minimum time in seconds the node requires to prepare for the next frame of the diagnostic service.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.STmin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyeculinsupplierid.html language=enus -->
## TOPIC 00056: LIN:Supplier ID

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyeculinsupplierid.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyeculinsupplierid.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: 16-bit value identifying the supplier of the LIN node (ECU). Remarks The following table lists the characteristics of this property. Short Name LIN.SupplierID Data type cu32.png Permissions Read/Write

### LIN:Supplier ID

16-bit value identifying the supplier of the LIN node (ECU).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.SupplierID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939nodename.html language=enus -->
## TOPIC 00057: SAE J1939:Node Name

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939nodename.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939nodename.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SAE J1939 Node Name for this ECU. This is a 64bit quantity that uniquely identifies the ECU. NI-XNET starts Address Claiming with this node name when the ECU is assigned to the session. Remarks The following table lists the characteristics of this property. Short Name J1939.NodeName Data type cu64.p

### SAE J1939:Node Name

SAE J1939 Node Name for this ECU. This is a 64bit quantity that uniquely identifies the ECU. NI-XNET starts Address Claiming with this node name when the ECU is assigned to the session.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.NodeName |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939preferredaddress.html language=enus -->
## TOPIC 00058: SAE J1939:Preferred Address

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939preferredaddress.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecusaej1939preferredaddress.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Preferred SAE J1939 Address for this ECU. NI-XNET starts Address Claiming with this address when the ECU is assigned to the session. Remarks The following table lists the characteristics of this property. Short Name J1939.PreferredAddress Data type cu32.png Permissions Read/Write

### SAE J1939:Preferred Address

Preferred SAE J1939 Address for this ECU. NI-XNET starts Address Claiming with this address when the ECU is assigned to the session.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.PreferredAddress |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-ecu/propertyecustartupframe.html language=enus -->
## TOPIC 00059: FlexRay:Startup Frame

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-ecu/propertyecustartupframe.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-ecu/propertyecustartupframe.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When FlexRay:Coldstart? is true, this indicates the startup frame that the ECU transmits (XNET Frame I/O Name). When FlexRay:Coldstart? is false, this I/O name is empty (invalid). You can use this frame to simulate the ECU, thereby making the National Instruments FlexRay interface operate as a colds

### FlexRay:Startup Frame

When **FlexRay:Coldstart?** is true, this indicates the startup frame that the ECU transmits (XNET Frame I/O Name). When **FlexRay:Coldstart?** is false, this I/O name is empty (invalid).

You can use this frame to simulate the ECU, thereby making the National Instruments FlexRay interface operate as a coldstart node. To do this, use the Session property node to set **Interface:FlexRay:Key Slot Identifier** to the **Identifier** of the frame referenced by this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.StartupFrm |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET ECU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframecantimingtype.html language=enus -->
## TOPIC 00060: CAN:Timing Type

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframecantimingtype.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframecantimingtype.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the timing used for the CAN frame. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name CAN.TimingType Data type cu32.png Permissions Read/Write Cyclic Data 0 Event Data 1 Cyclic Remote 2 Event Remote 3 Cyclic/Event

### CAN:Timing Type

Configures the timing used for the CAN frame. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CAN.TimingType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Cyclic Data | 0 |  |
| --- | --- | --- |
| Event Data | 1 |  |
| Cyclic Remote | 2 |  |
| Event Remote | 3 |  |
| Cyclic/Event | 4 |  |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframecomment.html language=enus -->
## TOPIC 00061: Comment

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframecomment.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframecomment.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Comment describing the frame (string). Remarks The following table lists the characteristics of this property. Short Name Comment Data type cstr.png Permissions Read/Write

### Comment

Comment describing the frame (string).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Comment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframedefaultpayload.html language=enus -->
## TOPIC 00062: Default Payload

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframedefaultpayload.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframedefaultpayload.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default payload for the frame, specified as an array of bytes (array of U8). The number of bytes in the array must match the frame's Payload Length property. Remarks The following table lists the characteristics of this property. Short Name DefaultPayload Data type c1du8.png Permissions Read/Write

### Default Payload

Default payload for the frame, specified as an array of bytes (array of U8). The number of bytes in the array must match the frame's **Payload Length** property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DefaultPayload |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraychannelassignment.html language=enus -->
## TOPIC 00063: FlexRay:Channel Assignment

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraychannelassignment.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraychannelassignment.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the FlexRay channels used for frame transmit. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name FlexRay.ChAssign Data type cu32.png Permissions Read/Write A 1 B 2 A and B 3

### FlexRay:Channel Assignment

Configures the FlexRay channels used for frame transmit. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.ChAssign |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| A | 1 |  |
| --- | --- | --- |
| B | 2 |  |
| A and B | 3 |  |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraypreamble.html language=enus -->
## TOPIC 00064: FlexRay:Payload Preamble?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraypreamble.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraypreamble.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the Payload Preamble bit is used in the frame (boolean). Remarks The following table lists the characteristics of this property. Short Name FlexRay.Preamble? Data type cbool.png Permissions Read/Write

### FlexRay:Payload Preamble?

Configures whether the Payload Preamble bit is used in the frame (boolean).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.Preamble? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraysync.html language=enus -->
## TOPIC 00065: FlexRay:Sync?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraysync.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraysync.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the frame is a sync frame, used for cluster wide clock synchronization (boolean). Remarks The following table lists the characteristics of this property. Short Name FlexRay.Sync? Data type cbool.png Permissions Read/Write

### FlexRay:Sync?

Configures whether the frame is a sync frame, used for cluster wide clock synchronization (boolean).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.Sync? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraytimingtype.html language=enus -->
## TOPIC 00066: FlexRay:Timing Type

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraytimingtype.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeflexraytimingtype.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the timing used for the FlexRay frame. This property is a ring (enumerated list). This determines whether the frame transmits when no new data is available. Remarks The following table lists the characteristics of this property. Short Name FlexRay.TimingType Data type cu32.png Permissions

### FlexRay:Timing Type

Configures the timing used for the FlexRay frame. This property is a ring (enumerated list). This determines whether the frame transmits when no new data is available.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.TimingType |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Cyclic | 0 |  |
| --- | --- | --- |
| Event | 1 |  |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepchannels.html language=enus -->
## TOPIC 00067: FlexRay:In Cycle Repetitions:Channel Assignments

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepchannels.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepchannels.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Additional channel assignments for the frame when FlexRay in-cycle repetition is enabled (array of ring). Remarks The following table lists the characteristics of this property. Short Name FlexRay.InCycRep.ChAssigns Data type c1du32.png Permissions Read/Write

### FlexRay:In Cycle Repetitions:Channel Assignments

Additional channel assignments for the frame when FlexRay in-cycle repetition is enabled (array of ring).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.InCycRep.ChAssigns |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepenabled.html language=enus -->
## TOPIC 00068: FlexRay:In Cycle Repetitions:Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepenabled.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframeincyclerepenabled.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the frame is repeated 2 or 4 times each cycle (boolean). In-cycle repetition effectively transmits the frame at a rate faster than the FlexRay cycle. Remarks The following table lists the characteristics of this property. Short Name FlexRay.InCycRep.Enabled? Data type cbool.png Permis

### FlexRay:In Cycle Repetitions:Enabled?

Indicates that the frame is repeated 2 or 4 times each cycle (boolean). In-cycle repetition effectively transmits the frame at a rate faster than the FlexRay cycle.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FlexRay.InCycRep.Enabled? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframelinchecksum.html language=enus -->
## TOPIC 00069: LIN:Checksum

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframelinchecksum.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframelinchecksum.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the checksum within the transmitted LIN frame is classic or enhanced. This property is a ring (enumerated list) with the following values: - Classic: LIN 1.x checksum - Enhanced: LIN 2.x checksum This property is read-only. The checksum is determined from the LIN version of ECUs t

### LIN:Checksum

Determines whether the checksum within the transmitted LIN frame is classic or enhanced.

This property is a ring (enumerated list) with the following values:
- Classic: LIN 1.x checksum
- Enhanced: LIN 2.x checksum

This property is read-only. The checksum is determined from the LIN version of ECUs transmitting and receiving the frame. The lower version of both ECUs is significant. If the LIN version of both ECUs is 2.0 or higher, the checksum type is Enhanced; otherwise, the checksum type is Classic.

Diagnostic frames (with decimal identifier 60 or 61) always use Classic checksum, as specified by LIN 2.x.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LIN.Checksum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Classic | 0 |  |
| --- | --- | --- |
| Enhanced | 1 |  |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframemuxdatamultiplexersignal.html language=enus -->
## TOPIC 00070: Mux:Data Multiplexer Signal

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframemuxdatamultiplexersignal.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframemuxdatamultiplexersignal.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data multiplexer signal (XNET Signal I/O Name). If the Is Data Multiplexed? property is false, this name is empty. Remarks The following table lists the characteristics of this property. Short Name Mux.DataMuxSig Data type cgenclassrntag.png Permissions Read Only

### Mux:Data Multiplexer Signal

Data multiplexer signal (XNET Signal I/O Name). If the **Is Data Multiplexed?** property is false, this name is empty.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.DataMuxSig |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframemuxisdatamultiplexed.html language=enus -->
## TOPIC 00071: Mux:Is Data Multiplexed?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframemuxisdatamultiplexed.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframemuxisdatamultiplexed.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether this frame is data multiplexed (boolean)? When a frame is data multiplexed (also known as mode dependent), it contains a special signal called the multiplexer. Of the remaining signals, some are the same in all instances of the frame (static), and some depend on the value of the mu

### Mux:Is Data Multiplexed?

Indicates whether this frame is data multiplexed (boolean)? When a frame is data multiplexed (also known as mode dependent), it contains a special signal called the multiplexer. Of the remaining signals, some are the same in all instances of the frame (static), and some depend on the value of the multiplexer (dynamic).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.IsMuxed? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframemuxsubframes.html language=enus -->
## TOPIC 00072: Mux:Subframes

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframemuxsubframes.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframemuxsubframes.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of subframes contained in the multiplexed frame (array of XNET Subframe I/O Name). Each subframe defines a group of dynamic signals transmitted using the same multiplexer value. Only one subframe at a time is transmitted in the frame. Remarks The following table lists the characteristics of th

### Mux:Subframes

Array of subframes contained in the multiplexed frame (array of XNET Subframe I/O Name). Each subframe defines a group of dynamic signals transmitted using the same multiplexer value. Only one subframe at a time is transmitted in the frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.Subframes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframepdumapping.html language=enus -->
## TOPIC 00073: PDU_Mapping

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframepdumapping.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframepdumapping.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property maps PDUs to the frame. A mapped PDU is transmitted inside the frame's payload. For FlexRay, you can map one or more PDUs to a frame and one PDU to multiple frames. For CAN and LIN, the PDU is equivalent to the frame, because only one-to-one mapping is supported. Remarks The following

### PDU_Mapping

This property maps PDUs to the frame. A mapped PDU is transmitted inside the frame's payload. For FlexRay, you can map one or more PDUs to a frame and one PDU to multiple frames. For CAN and LIN, the PDU is equivalent to the frame, because only one-to-one mapping is supported.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDU_Mapping |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-frame/propertyframesignals.html language=enus -->
## TOPIC 00074: Signals

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-frame/propertyframesignals.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-frame/propertyframesignals.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of signals contained in the frame (array of XNET Signal I/O Name). Remarks The following table lists the characteristics of this property. Short Name Sigs Data type c1dgenclassrntag.png Permissions Read Only

### Signals

Array of signals contained in the frame (array of XNET Signal I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sigs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Frame Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface-p.html language=enus -->
## TOPIC 00075: XNET Interface Properties

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface-p.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface-p.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### XNET Interface Properties

- [CAN:Termination Capability](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecanterminationcapability.html) Indicates the CAN termination capability of the hardware. This property is a ring (enumerated list).
- [CAN:Transceiver Capability](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecantransceivercapability.html) Indicates the CAN transceiver capability of the hardware. This property is a ring (enumerated list).
- [Device](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedevice.html) Device that contains this interface (XNET Device I/O Name). Each device represents a hardware product such as PCI card or USB box.
- [Dongle Compatible Firmware Version](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblefirmwareversion.html) Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's firmware.
- [Dongle Compatible Revision](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblerevision.html) Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's hardware revision.
- [Dongle Firmware Version](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglefirmwareversion.html) Firmware revision number of the connected Transceiver Cable.
- [Dongle ID](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedongleid.html) Indicates the type of the connected Transceiver Cable. This property is a ring (enumerated list).
- [Dongle Revision](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglerevision.html) Hardware revision number of the connected Transceiver Cable.
- [Dongle State](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglestate.html) Indicates the state of the connected Transceiver Cable. This property is a ring (enumerated list).
- [Name](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacename.html) Name of the interface (string). This name is shown in the Measurement and Automation Explorer (MAX).
- [Number](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacenumber.html) Interface number. Each National Instruments XNET interface is assigned a unique number. The numbering sequence starts at 1, and is distinct for each Protocol .
- [Port Number](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceportnumber.html) Physical port number of the interface (1-2). This number is typically printed on the hardware device near the connector for the port.
- [Protocol](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceprotocol.html) Protocol supported by the National Instruments interface (ring)
- [Sessions in Project](../../../resource/objmgr/xnet-rc/xnet-interface/propertyinterfacesessionsinproject.html) Property not supported in 1.0. Invisible to avoid breaking property node created using 1.0 alpha.

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecanterminationcapability.html language=enus -->
## TOPIC 00076: CAN:Termination Capability

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecanterminationcapability.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecanterminationcapability.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the CAN termination capability of the hardware. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name CAN.TermCap Data type cu32.png Permissions Read Only No 0 Yes 1

### CAN:Termination Capability

Indicates the CAN termination capability of the hardware. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CAN.TermCap |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| No | 0 |  |
| --- | --- | --- |
| Yes | 1 |  |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecantransceivercapability.html language=enus -->
## TOPIC 00077: CAN:Transceiver Capability

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecantransceivercapability.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacecantransceivercapability.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the CAN transceiver capability of the hardware. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name CAN.TcvrCap Data type cu32.png Permissions Read Only HS 0 LS 1 XS 3 XS (HS/LS) 4

### CAN:Transceiver Capability

Indicates the CAN transceiver capability of the hardware. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CAN.TcvrCap |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| HS | 0 |  |
| --- | --- | --- |
| LS | 1 |  |
| XS | 3 |  |
| XS (HS/LS) | 4 |  |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedevice.html language=enus -->
## TOPIC 00078: Device

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedevice.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedevice.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Device that contains this interface (XNET Device I/O Name). Each device represents a hardware product such as PCI card or USB box. Remarks The following table lists the characteristics of this property. Short Name Device Data type cgenclassrntag.png Permissions Read Only

### Device

Device that contains this interface (XNET Device I/O Name). Each device represents a hardware product such as PCI card or USB box.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblefirmwareversion.html language=enus -->
## TOPIC 00079: Dongle Compatible Firmware Version

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblefirmwareversion.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblefirmwareversion.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's firmware. Remarks The following table lists the characteristics of this property. Short Name DnglCptFwVers Data type cu32.png Permissions Read Only

### Dongle Compatible Firmware Version

Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's firmware.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DnglCptFwVers |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblerevision.html language=enus -->
## TOPIC 00080: Dongle Compatible Revision

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblerevision.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglecompatiblerevision.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's hardware revision. Remarks The following table lists the characteristics of this property. Short Name DnglCptRev Data type cu32.png Permissions Read Only

### Dongle Compatible Revision

Returns a number representing the oldest driver version compatible with the connected Transceiver Cable's hardware revision.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DnglCptRev |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglefirmwareversion.html language=enus -->
## TOPIC 00081: Dongle Firmware Version

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglefirmwareversion.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglefirmwareversion.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Firmware revision number of the connected Transceiver Cable. Remarks The following table lists the characteristics of this property. Short Name DnglFwVers Data type cu32.png Permissions Read Only

### Dongle Firmware Version

Firmware revision number of the connected Transceiver Cable.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DnglFwVers |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglestate.html language=enus -->
## TOPIC 00082: Dongle State

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglestate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacedonglestate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the state of the connected Transceiver Cable. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name DnglState Data type cu32.png Permissions Read Only No dongle, no external power 1 No dongle, has external power 2 Has

### Dongle State

Indicates the state of the connected Transceiver Cable. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DnglState |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| No dongle, no external power | 1 |  |
| --- | --- | --- |
| No dongle, has external power | 2 |  |
| Has dongle, no external power | 3 |  |
| Ready | 4 |  |
| Busy | 5 |  |
| Comm Error | 13 |  |
| Overcurrent | 14 |  |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfacenumber.html language=enus -->
## TOPIC 00083: Number

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfacenumber.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfacenumber.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface number. Each National Instruments XNET interface is assigned a unique number. The numbering sequence starts at 1, and is distinct for each Protocol. Remarks The following table lists the characteristics of this property. Short Name Number Data type cu32.png Permissions Read Only

### Number

Interface number. Each National Instruments XNET interface is assigned a unique number. The numbering sequence starts at 1, and is distinct for each **Protocol**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceportnumber.html language=enus -->
## TOPIC 00084: Port Number

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceportnumber.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceportnumber.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Physical port number of the interface (1-2). This number is typically printed on the hardware device near the connector for the port. Remarks The following table lists the characteristics of this property. Short Name PortNum Data type cu32.png Permissions Read Only

### Port Number

Physical port number of the interface (1-2). This number is typically printed on the hardware device near the connector for the port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PortNum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceprotocol.html language=enus -->
## TOPIC 00085: Protocol

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceprotocol.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-interface/propertyinterfaceprotocol.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Protocol supported by the National Instruments interface (ring) Remarks The following table lists the characteristics of this property. Short Name Protocol Data type cu32.png Permissions Read Only CAN 0 FlexRay 1 LIN 2 Ethernet 3 Unknown 4294967294

### Protocol

Protocol supported by the National Instruments interface (ring)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Protocol |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| CAN | 0 |  |
| --- | --- | --- |
| FlexRay | 1 |  |
| LIN | 2 |  |
| Ethernet | 3 |  |
| Unknown | 4294967294 |  |

Parent topic:

XNET Interface Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule-entry-p.html language=enus -->
## TOPIC 00086: XNET LIN Schedule Entry Properties

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule-entry-p.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule-entry-p.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### XNET LIN Schedule Entry Properties

- [Collision Resolving Schedule](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrycollisionresolvingschedule.html) LIN schedule that resolves a collision for this event-triggered entry (XNET LIN Schedule I/O Name). This property applies only when the entry's Type property is Event-triggered . When a collision occurs for the event-triggered entry in this schedule, the master must switch to the collision resolving schedule to transfer the unconditional frames successfully. If the XNET interface is acting as the master on the LIN cluster, NI-XNET automatically writes a schedule request for this collision resolving schedule. The collision resolving schedule's Run Mode must be Once . When the entry's Type property is any value other than Event-triggered , this property returns an empty schedule (invalid).
- [Delay](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrydelay.html) Time from the start of this entry (slot) to the start of the next entry (DBL seconds, fractional part used for milliseconds and microseconds).
- [Event Identifier](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryeventidentifier.html) Identifier of the event-triggered entry. This identifier is unprotected (NI-XNET handles the protection). This property applies only when the entry's Type property is Event-triggered . This identifier is used for the event-triggered entry itself, and the 1st byte of the payload contains the protected identifier of the corresponding Unconditional frame. When the entry's Type property is any value other than Event-triggered , this property returns hexadecimal FFFFFFFF (invalid).
- [Frames](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryframes.html) Array of frames for this LIN schedule entry (array of XNET Frame I/O Name). If the Type of the entry is Unconditional , this array contains one element, which is the single Unconditional frame. If the Type of the entry is Sporadic , this array contains one or more Unconditional frames. When multiple frames are pending in the NI-XNET interface, the order to transmit is determined by the order in this array. If the Type of the entry is Event-triggered , this array contains one or more Unconditional frames. When multiple frames are pending in the NI-XNET interface, the order to transmit is determined by the order in this array. If frames are pending in multiple ECUs, a collision will typically occur (see Collision Resolving Schedule ).
- [Name (Short)](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrynameshort.html) Short name of the LIN schedule entry (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database name. If you write this property, it changes both short and long name (see Detailed help ).
- [Node Configuration:Free Format:Data Bytes](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrynodeconfigurationfreeformatdatabytes.html) An array of 8 bytes containing raw data for LIN node configuration.
- [Schedule](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryschedule.html) LIN schedule that uses this entry (XNET LIN Schedule I/O Name). This LIN schedule is considered the parent of this entry.
- [Type](../../../resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrytype.html) This property determines the mechanism used to transfer frames in this schedule entry (slot): - Unconditional: A single frame transfers in this slot. - Sporadic: Master transmits in this slot. The master can select among multiple frames to transmit. - Event-triggered: Multiple slaves can transmit. When a collision occurs, this is detected and resolved using a different schedule. - Node configuration: Schedule entry contains a node configuration service.

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrycollisionresolvingschedule.html language=enus -->
## TOPIC 00087: Collision Resolving Schedule

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrycollisionresolvingschedule.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrycollisionresolvingschedule.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: LIN schedule that resolves a collision for this event-triggered entry (XNET LIN Schedule I/O Name). This property applies only when the entry's Type property is Event-triggered. When a collision occurs for the event-triggered entry in this schedule, the master must switch to the collision resolving

### Collision Resolving Schedule

LIN schedule that resolves a collision for this event-triggered entry (XNET LIN Schedule I/O Name).

This property applies only when the entry's **Type** property is **Event-triggered**. When a collision occurs for the event-triggered entry in this schedule, the master must switch to the collision resolving schedule to transfer the unconditional frames successfully. If the XNET interface is acting as the master on the LIN cluster, NI-XNET automatically writes a schedule request for this collision resolving schedule. The collision resolving schedule's **Run Mode** must be **Once**.

When the entry's **Type** property is any value other than **Event-triggered**, this property returns an empty schedule (invalid).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CollResSched |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET LIN Schedule Entry Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrydelay.html language=enus -->
## TOPIC 00088: Delay

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrydelay.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentrydelay.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Time from the start of this entry (slot) to the start of the next entry (DBL seconds, fractional part used for milliseconds and microseconds). Remarks The following table lists the characteristics of this property. Short Name Delay Data type cdbl.png Permissions Read/Write

### Delay

Time from the start of this entry (slot) to the start of the next entry (DBL seconds, fractional part used for milliseconds and microseconds).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET LIN Schedule Entry Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryeventidentifier.html language=enus -->
## TOPIC 00089: Event Identifier

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryeventidentifier.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryeventidentifier.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Identifier of the event-triggered entry. This identifier is unprotected (NI-XNET handles the protection). This property applies only when the entry's Type property is Event-triggered. This identifier is used for the event-triggered entry itself, and the 1st byte of the payload contains the protected

### Event Identifier

Identifier of the event-triggered entry. This identifier is unprotected (NI-XNET handles the protection).

This property applies only when the entry's **Type** property is **Event-triggered**. This identifier is used for the event-triggered entry itself, and the 1st byte of the payload contains the protected identifier of the corresponding Unconditional frame.

When the entry's **Type** property is any value other than **Event-triggered**, this property returns hexadecimal FFFFFFFF (invalid).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EventID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET LIN Schedule Entry Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryschedule.html language=enus -->
## TOPIC 00090: Schedule

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryschedule.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule-entry/propertylinscheduleentryschedule.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: LIN schedule that uses this entry (XNET LIN Schedule I/O Name). This LIN schedule is considered the parent of this entry. Remarks The following table lists the characteristics of this property. Short Name Schedule Data type cgenclassrntag.png Permissions Read Only

### Schedule

LIN schedule that uses this entry (XNET LIN Schedule I/O Name). This LIN schedule is considered the parent of this entry.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Schedule |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET LIN Schedule Entry Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinscheduleconfigurationstatus.html language=enus -->
## TOPIC 00091: Configuration Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinscheduleconfigurationstatus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinscheduleconfigurationstatus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuration status of the LIN schedule. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true. Remarks The following table lists the characteristics of this property. Short Name ConfigStatus Data type ci32.png Permissions Read Only

### Configuration Status

Configuration status of the LIN schedule. This property is used only if you change the Database property **Show Invalid From Open?** from false (default) to true.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConfigStatus |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET LIN Schedule Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinschedulenameshort.html language=enus -->
## TOPIC 00092: Name (Short)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinschedulenameshort.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-lin-schedule/propertylinschedulenameshort.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short name of the LIN schedule (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database name. If you write this property, it changes both short and long name (see Detailed help). Remarks The following table lists the characteristics of this property. S

### Name (Short)

Short name of the LIN schedule (string).

The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database name. If you write this property, it changes both short and long name (see **Detailed help**).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NameShort |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET LIN Schedule Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypducluster.html language=enus -->
## TOPIC 00093: Cluster

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypducluster.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypducluster.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cluster that contains the PDU (XNET Cluster I/O Name). Remarks The following table lists the characteristics of this property. Short Name Cluster Data type cgenclassrntag.png Permissions Read Only

### Cluster

Cluster that contains the PDU (XNET Cluster I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cluster |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypduconfigurationstatus.html language=enus -->
## TOPIC 00094: Configuration Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypduconfigurationstatus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypduconfigurationstatus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuration status of the PDU. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true. Remarks The following table lists the characteristics of this property. Short Name ConfigStatus Data type ci32.png Permissions Read Only

### Configuration Status

Configuration status of the PDU. This property is used only if you change the Database property **Show Invalid From Open?** from false (default) to true.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConfigStatus |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypduframes.html language=enus -->
## TOPIC 00095: Frames

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypduframes.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypduframes.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of all frames to which the PDU is mapped (array of XNET Frame I/O Name). A PDU is transmitted within the frames to which it is mapped. To map a PDU to a frame, use the XNET Frame PDU Mapping property. You can map one PDU to multiple frames. Remarks The following table lists the characteristics

### Frames

Array of all frames to which the PDU is mapped (array of XNET Frame I/O Name). A PDU is transmitted within the frames to which it is mapped.

To map a PDU to a frame, use the XNET Frame **PDU Mapping** property. You can map one PDU to multiple frames.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frms |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxdatamultiplexersignal.html language=enus -->
## TOPIC 00096: Mux:Data Multiplexer Signal

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxdatamultiplexersignal.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxdatamultiplexersignal.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Data multiplexer signal (XNET Signal I/O Name). This property applies to CAN only, and it is the same as the PDU's parent frame. Remarks The following table lists the characteristics of this property. Short Name Mux.DataMuxSig Data type cgenclassrntag.png Permissions Read Only

### Mux:Data Multiplexer Signal

Data multiplexer signal (XNET Signal I/O Name). This property applies to CAN only, and it is the same as the PDU's parent frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.DataMuxSig |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxisdatamultiplexed.html language=enus -->
## TOPIC 00097: Mux:Is Data Multiplexed?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxisdatamultiplexed.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxisdatamultiplexed.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether this PDU is data multiplexed (boolean)? This property applies to CAN only, and it is the same as the PDU's parent frame. Remarks The following table lists the characteristics of this property. Short Name Mux.IsMuxed? Data type cbool.png Permissions Read Only

### Mux:Is Data Multiplexed?

Indicates whether this PDU is data multiplexed (boolean)? This property applies to CAN only, and it is the same as the PDU's parent frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.IsMuxed? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxstaticsignals.html language=enus -->
## TOPIC 00098: Mux:Static Signals

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxstaticsignals.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypdumuxstaticsignals.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of static signals contained in the multiplexed PDU (array of XNET Signal I/O Name). This property applies to CAN only, and it is the same as the PDU's parent frame. Remarks The following table lists the characteristics of this property. Short Name Mux.StatSigs Data type c1dgenclassrntag.png Pe

### Mux:Static Signals

Array of static signals contained in the multiplexed PDU (array of XNET Signal I/O Name). This property applies to CAN only, and it is the same as the PDU's parent frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.StatSigs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypduname.html language=enus -->
## TOPIC 00099: Name (Short)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypduname.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypduname.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short name of the PDU (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database and cluster name. If you write this property, it changes both short and long name (see Detailed help). Remarks The following table lists the characteristics of this property

### Name (Short)

Short name of the PDU (string).

The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database and cluster name. If you write this property, it changes both short and long name (see **Detailed help**).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NameShort |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-pdu/propertypdupayloadlength.html language=enus -->
## TOPIC 00100: Payload Length

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-pdu/propertypdupayloadlength.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-pdu/propertypdupayloadlength.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of bytes of data in the PDU's payload. This number can be less than the payload length of mapped frames. Remarks The following table lists the characteristics of this property. Short Name PayldLen Data type cu32.png Permissions Read/Write

### Payload Length

Number of bytes of data in the PDU's payload. This number can be less than the payload length of mapped frames.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PayldLen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET PDU Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertyinterfacestatisticsenabled.html language=enus -->
## TOPIC 00101: Interface:FlexRay:Statistics Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertyinterfacestatisticsenabled.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertyinterfacestatisticsenabled.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable reporting of FlexRay error statistics to XNET Read (State FlexRay Statistics). Remarks The following table lists the characteristics of this property. Short Name Intf.FlexRay.StatisticsEn? Data type cbool.png Permissions Read/Write

### Interface:FlexRay:Statistics Enabled?

Configures whether to enable reporting of FlexRay error statistics to **XNET Read (State FlexRay Statistics)**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.FlexRay.StatisticsEn? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaeven.html language=enus -->
## TOPIC 00102: Interface:FlexRay:Sync Frames Channel A Even

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaeven.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaeven.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of sync frames (slot IDs) transmitted or received on channel A during the last even cycle (array of u32). Remarks The following table lists the characteristics of this property. Short Name Intf.FlexRay.SyncChAEven Data type c1du32.png Permissions Read Only

### Interface:FlexRay:Sync Frames Channel A Even

Array of sync frames (slot IDs) transmitted or received on channel A during the last even cycle (array of u32).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.FlexRay.SyncChAEven |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaodd.html language=enus -->
## TOPIC 00103: Interface:FlexRay:Sync Frames Channel A Odd

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaodd.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelaodd.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of sync frames (slot IDs) transmitted or received on channel A during the last odd cycle (array of u32). Remarks The following table lists the characteristics of this property. Short Name Intf.FlexRay.SyncChAOdd Data type c1du32.png Permissions Read Only

### Interface:FlexRay:Sync Frames Channel A Odd

Array of sync frames (slot IDs) transmitted or received on channel A during the last odd cycle (array of u32).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.FlexRay.SyncChAOdd |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelbeven.html language=enus -->
## TOPIC 00104: Interface:FlexRay:Sync Frames Channel B Even

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelbeven.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertyinterfacesyncframeschannelbeven.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of sync frames (slot IDs) transmitted or received on channel B during the last even cycle (array of u32). Remarks The following table lists the characteristics of this property. Short Name Intf.FlexRay.SyncChBEven Data type c1du32.png Permissions Read Only

### Interface:FlexRay:Sync Frames Channel B Even

Array of sync frames (slot IDs) transmitted or received on channel B during the last even cycle (array of u32).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.FlexRay.SyncChBEven |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionapplicationprotocol.html language=enus -->
## TOPIC 00105: Application Protocol

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionapplicationprotocol.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionapplicationprotocol.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Higher-level application protocol of the interface used to create the session. This property is a ring (enumerated list). Remarks The following table lists the characteristics of this property. Short Name ApplProtocol Data type cu32.png Permissions Read Only None 0 J1939 1

### Application Protocol

Higher-level application protocol of the interface used to create the session. This property is a ring (enumerated list).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ApplProtocol |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| None | 0 |  |
| --- | --- | --- |
| J1939 | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionautostart.html language=enus -->
## TOPIC 00106: Auto Start?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionautostart.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionautostart.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to automatically start the output session. Input sessions always start automatically. Remarks The following table lists the characteristics of this property. Short Name AutoStart? Data type cbool.png Permissions Read/Write

### Auto Start?

Configures whether to automatically start the output session. Input sessions always start automatically.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AutoStart? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessiondatabase.html language=enus -->
## TOPIC 00107: Database

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessiondatabase.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessiondatabase.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database used to create the session (XNET Database I/O Name). Remarks The following table lists the characteristics of this property. Short Name Database Data type cgenclassrntag.png Permissions Read Only

### Database

Database used to create the session (XNET Database I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Database |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogerror.html language=enus -->
## TOPIC 00108: Ethernet:Logging:Error?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogerror.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogerror.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if an error has occurred in the logging thread. To see the error information, stop the session using XNET Stop; the error from the logging thread will be merged with the error of the XNET Stop VI. Remarks The following table lists the characteristics of this property. Short Name Enet.Log.E

### Ethernet:Logging:Error?

Indicates if an error has occurred in the logging thread. To see the error information, stop the session using XNET Stop; the error from the logging thread will be merged with the error of the XNET Stop VI.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enet.Log.Error? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogmffilesizethreshold.html language=enus -->
## TOPIC 00109: Ethernet:Logging:MultipleFiles:FileSizeThreshold

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogmffilesizethreshold.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionenetlogmffilesizethreshold.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Threshold, specified in bytes, above which a new log file will be created if the value of EnableMultipleFiles is true. FileSizeThreshold is ignored if EnableMultipleFiles is false. Remarks The following table lists the characteristics of this property. Short Name Enet.Log.Mf.FlSzTh Data type cu64.pn

### Ethernet:Logging:MultipleFiles:FileSizeThreshold

Threshold, specified in bytes, above which a new log file will be created if the value of EnableMultipleFiles is true. FileSizeThreshold is ignored if EnableMultipleFiles is false.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enet.Log.Mf.FlSzTh |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionenetnumframesreceived.html language=enus -->
## TOPIC 00110: Ethernet:Number of Frames Received

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionenetnumframesreceived.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionenetnumframesreceived.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is a count of frames received by the session. When logging is off, these frames can be obtained from XNET Read. When logging is on, these frames are stored in the log file. When an input session is used for the Ethernet endpoint, the Interface:Ethernet:Endpoint:Receive Filter property determine

### Ethernet:Number of Frames Received

This is a count of frames received by the session. When logging is off, these frames can be obtained from XNET Read. When logging is on, these frames are stored in the log file.

When an input session is used for the Ethernet endpoint, the **Interface:Ethernet:Endpoint:Receive Filter** property determines which frames are received by the session.

This count resets to zero when the session starts. The count is unchanged when the session stops.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enet.NumFramesReceived |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionframecanstarttimeoffset.html language=enus -->
## TOPIC 00111: Frame:CAN:Start Time Offset

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionframecanstarttimeoffset.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionframecanstarttimeoffset.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this property to configure the amount of time that must elapse between the session being started and the time that the first frame is transmitted across the bus. This is different than the cyclic rate, which determines the time between subsequent frame transmissions. Use this property to have mo

### Frame:CAN:Start Time Offset

Use this property to configure the amount of time that must elapse between the session being started and the time that the first frame is transmitted across the bus. This is different than the cyclic rate, which determines the time between subsequent frame transmissions.

Use this property to have more control over the schedule of frames on the bus, to offer more determinism by configuring cyclic frames to be spaced evenly.

If you do not set this property, NI-XNET chooses this start time offset based on the CAN arbitration identifier and periodic transmit time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frm.CAN.StartTimeOff |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionframeskipncyclicframes.html language=enus -->
## TOPIC 00112: Frame:Skip N Cyclic Frames

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionframeskipncyclicframes.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionframeskipncyclicframes.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When set to a nonzero value N, this property causes the next N cyclic frames to be skipped. When the frame's transmission time arrives and the skip count is nonzero, a frame value is dequeued (if this is not a single-point session), and the skip count is decremented, but the frame actually is not tr

### Frame:Skip N Cyclic Frames

When set to a nonzero value N, this property causes the next N cyclic frames to be skipped. When the frame's transmission time arrives and the skip count is nonzero, a frame value is dequeued (if this is not a single-point session), and the skip count is decremented, but the frame actually is not transmitted across the bus. When the skip count decrements to zero, subsequent cyclic transmissions resume. This property is valid only for output sessions and frames with cyclic timing (that is, not event-based frames).

This property is useful for testing of ECU behavior when a cyclic frame is expected, but is missing for N cycles.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frm.SkipNCyclic |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterface64bitbaudrate.html language=enus -->
## TOPIC 00113: Interface:64bit Baud Rate

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterface64bitbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterface64bitbaudrate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: CAN, FlexRay, or LIN interface baud rate. The default for this interface property is the same as the cluster's baud rate in the database. Remarks The following table lists the characteristics of this property. Short Name Intf.BaudRate64 Data type cu64.png Permissions Read/Write

### Interface:64bit Baud Rate

CAN, FlexRay, or LIN interface baud rate. The default for this interface property is the same as the cluster's baud rate in the database.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.BaudRate64 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecaniomode.html language=enus -->
## TOPIC 00114: Interface:CAN:I/O Mode

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecaniomode.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecaniomode.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: CAN I/O Mode. This property is a ring (enumerated list). The default for this interface property is the same as the cluster's CAN I/O Mode in the database. Remarks The following table lists the characteristics of this property. Short Name Intf.CAN.IoMode Data type cu32.png Permissions Read Only CAN

### Interface:CAN:I/O Mode

CAN I/O Mode. This property is a ring (enumerated list). The default for this interface property is the same as the cluster's CAN I/O Mode in the database.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.CAN.IoMode |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| CAN 2.0 | 0 |  |
| --- | --- | --- |
| CAN FD | 1 |  |
| CAN FD+BRS | 2 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecanpendingtransmitorder.html language=enus -->
## TOPIC 00115: Interface:CAN:Pending Transmit Order

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecanpendingtransmitorder.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecanpendingtransmitorder.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Pending Transmit Order property configures how the CAN interface manages the internal queue of frames. More than one frame may desire to transmit at the same time. NI-XNET stores the frames in an internal queue and transmits them onto the CAN bus when the bus is idle. This property modifies how

### Interface:CAN:Pending Transmit Order

The Pending Transmit Order property configures how the CAN interface manages the internal queue of frames. More than one frame may desire to transmit at the same time. NI-XNET stores the frames in an internal queue and transmits them onto the CAN bus when the bus is idle.

This property modifies how NI-XNET handles this queue of frames. The following table lists the accepted values:
- As Submitted
- By Identifier

When you configure this property to be As Submitted, frames are transmitted in the order that they were submitted into the queue. There is no reordering of any frames, and a higher priority frame may be delayed due to the transmission or retransmission of a previously submitted frame. However, this mode has the highest performance.

When you configure this property to be By Identifier, frames with the highest priority identifier (lower CAN ID value) transmit first.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.CAN.PendTxOrder |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

| As Submitted | 0 |  |
| --- | --- | --- |
| By Identifier | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecantransmitpause.html language=enus -->
## TOPIC 00116: Interface:CAN:Transmit Pause

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecantransmitpause.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacecantransmitpause.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the transmitter waits for two full bit times after successful transmission before transmitting the next frame. The default for this interface property is FALSE. Remarks The following table lists the characteristics of this property. Short Name Intf.CAN.TxPause Data type cbool.png Perm

### Interface:CAN:Transmit Pause

Indicates that the transmitter waits for two full bit times after successful transmission before transmitting the next frame. The default for this interface property is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.CAN.TxPause |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceechotransmit.html language=enus -->
## TOPIC 00117: Interface:Echo Transmit?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceechotransmit.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceechotransmit.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether input sessions will contain frames transmitted by the interface (boolean). Remarks The following table lists the characteristics of this property. Short Name Intf.EchoTx? Data type cbool.png Permissions Read/Write

### Interface:Echo Transmit?

Configures whether input sessions will contain frames transmitted by the interface (boolean).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.EchoTx? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetadjust.html language=enus -->
## TOPIC 00118: Interface:Adjust Local Time

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetadjust.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetadjust.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A write of this property applies a positive or negative phase adjustment, in nanoseconds, to the local time that is used for timestamping of frames. This adjustment can be used to align the local time with another timescale or device. Remarks The following table lists the characteristics of this pro

### Interface:Adjust Local Time

A write of this property applies a positive or negative phase adjustment, in nanoseconds, to the local time that is used for timestamping of frames. This adjustment can be used to align the local time with another timescale or device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.AdjustLocal |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointrxfilter.html language=enus -->
## TOPIC 00119: Interface:Ethernet:Endpoint:Receive Filter

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointrxfilter.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointrxfilter.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For each frame received by the interface, the frame is forwarded to either the XNET endpoint or the OS stack (not both). This property configures zero, one, or two identification elements (filters) for this forwarding decision. The following C language pseudo-code describes how XNET forwards each re

### Interface:Ethernet:Endpoint:Receive Filter

For each frame received by the interface, the frame is forwarded to either the XNET endpoint or the OS stack (not both). This property configures zero, one, or two identification elements (filters) for this forwarding decision.

The following C language pseudo-code describes how XNET forwards each received frame to either the XNET endpoint or the OS stack:

 // TRUE forwards to XNET endpoint, FALSE forwards to OS stack
boolean forwardFrameToEndpoint = FALSE;
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

Refer to detailed help for default values, and the type and range for each field.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Ept.RxFilter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointtxbandw.html language=enus -->
## TOPIC 00120: Interface:Ethernet:Endpoint:Transmit Bandwidth

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointtxbandw.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetendpointtxbandw.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property configures the maximum bandwidth for the credit-based shaper algorithm specified in IEEE Std 802.1Q, which is used for all transmit from the endpoint. The value is in units of bits per second. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.

### Interface:Ethernet:Endpoint:Transmit Bandwidth

This property configures the maximum bandwidth for the credit-based shaper algorithm specified in IEEE Std 802.1Q, which is used for all transmit from the endpoint. The value is in units of bits per second.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Ept.TxBandw |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetipv4addr.html language=enus -->
## TOPIC 00121: Interface:Ethernet:IPv4 Address

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetipv4addr.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetipv4addr.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the IPv4 address that is configured on the XNET interface in the network by the OS stack. The IPv4 address is returned as a string in dotted-decimal notation. For example: 192.0.2.1. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.IpV4Addr Data

### Interface:Ethernet:IPv4 Address

Indicates the IPv4 address that is configured on the XNET interface in the network by the OS stack. The IPv4 address is returned as a string in dotted-decimal notation. For example: 192.0.2.1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.IpV4Addr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeed.html language=enus -->
## TOPIC 00122: Interface:Ethernet:Link Speed

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeed.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeed.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current link speed on the interface or shows if the link is down. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.LinkSpeed Data type cu32.png Permissions Read Only Link_Down 0 100Mb/s 1 1000Mb/s 2

### Interface:Ethernet:Link Speed

Indicates the current link speed on the interface or shows if the link is down.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.LinkSpeed |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Link_Down | 0 |  |
| --- | --- | --- |
| 100Mb/s | 1 |  |
| 1000Mb/s | 2 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeedconfigured.html language=enus -->
## TOPIC 00123: Interface:Ethernet:Link Speed Configured

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeedconfigured.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetlinkspeedconfigured.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the link speed that is configured for the Ethernet PHY on the interface. This property is configured using MAX or the System Configuration property Link Speed Configured. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.LinkSpeedConf Data type cu

### Interface:Ethernet:Link Speed Configured

Indicates the link speed that is configured for the Ethernet PHY on the interface. This property is configured using MAX or the System Configuration property Link Speed Configured.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.LinkSpeedConf |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| 100Mb/s | 1 |  |
| --- | --- | --- |
| 1000Mb/s | 2 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetmacaddr.html language=enus -->
## TOPIC 00124: Interface:Ethernet:MAC Address

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetmacaddr.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetmacaddr.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the MAC address that uniquely identifies the XNET Interface in the network. This MAC address applies to the endpoint as well as the OS stack. The MAC address is an individual (unicast) EUI-48 MAC address that is assigned to the hardware according to the requirements of IEEE Std 802. The da

### Interface:Ethernet:MAC Address

Indicates the MAC address that uniquely identifies the XNET Interface in the network. This MAC address applies to the endpoint as well as the OS stack. The MAC address is an individual (unicast) EUI-48 MAC address that is assigned to the hardware according to the requirements of IEEE Std 802. The data type is an array of 6 bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.MacAddr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphypwrmode.html language=enus -->
## TOPIC 00125: Interface:Ethernet:PHY Power Mode

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphypwrmode.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphypwrmode.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current power mode of the PHY. If the XNET device supports the sleep/wake capability, the PHY Power Mode can be changed by calling the XNET Write (State Ethernet Sleep) and XNET Write (State Ethernet Wake) VIs. Remarks The following table lists the characteristics of this property. Sho

### Interface:Ethernet:PHY Power Mode

Indicates the current power mode of the PHY. If the XNET device supports the sleep/wake capability, the PHY Power Mode can be changed by calling the XNET Write (State Ethernet Sleep) and XNET Write (State Ethernet Wake) VIs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.PhyPwrMode |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Normal | 0 |  |
| --- | --- | --- |
| Sleep | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphystate.html language=enus -->
## TOPIC 00126: Interface:Ethernet:PHY State

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphystate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetphystate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the mode for which the interface is configured to use the Ethernet PHY: Master, Slave, or Autonegotiate. This property is configured using MAX or the System Configuration property PHY State Configured. Remarks The following table lists the characteristics of this property. Short Name Intf.

### Interface:Ethernet:PHY State

Indicates the mode for which the interface is configured to use the Ethernet PHY: Master, Slave, or Autonegotiate. This property is configured using MAX or the System Configuration property PHY State Configured.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.PhySt |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Slave | 0 |  |
| --- | --- | --- |
| Master | 1 |  |
| Auto | 2 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetportmode.html language=enus -->
## TOPIC 00127: Interface:Ethernet:Port Mode

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetportmode.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetportmode.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the hardware connectivity for the port. This property is configured using MAX or the System Configuration property PHY State Configured. It is a ring of values, as described in the following table: Direct: The port is directly connected, such that frames received and transmitted on the por

### Interface:Ethernet:Port Mode

Indicates the hardware connectivity for the port. This property is configured using MAX or the System Configuration property PHY State Configured. It is a ring of values, as described in the following table:

Direct: The port is directly connected, such that frames received and transmitted on the port have no relationship to any other port on the XNET device. Input and output sessions are supported in Direct mode.

Tap: This port is connected to another port on the XNET device using a Tap. The pair of connected ports are referred to as tap partners. A frame received on one Tap partner is immediately transmitted out the other tap partner, to mimic behavior of an Ethernet cable. Output sessions are not supported in Tap mode.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.PortMode |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Direct | 0 |  |
| --- | --- | --- |
| Tap | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetsleepcap.html language=enus -->
## TOPIC 00128: Interface:Ethernet:Sleep Capability

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetsleepcap.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetsleepcap.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the sleep capability is enabled or disabled/not available for the interface. This property is configured using NI MAX or the System Configuration property Sleep Capability Configured. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Sleep

### Interface:Ethernet:Sleep Capability

Indicates whether the sleep capability is enabled or disabled/not available for the interface. This property is configured using NI MAX or the System Configuration property Sleep Capability Configured.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.SleepCap |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Disabled / Not Available | 0 |  |
| --- | --- | --- |
| Enabled | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatctrnames.html language=enus -->
## TOPIC 00129: Interface:Ethernet:Statistics:MAC:Counter Names

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatctrnames.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatctrnames.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property returns the name of each Ethernet statistics property supported by XNET. The name uses uppercase for the first letter of each word, with space as a separator between words. The name at a specific index corresponds to the counter at the same index in Counter Values. The size of this pro

### Interface:Ethernet:Statistics:MAC:Counter Names

This property returns the name of each Ethernet statistics property supported by XNET. The name uses uppercase for the first letter of each word, with space as a separator between words.

The name at a specific index corresponds to the counter at the same index in **Counter Values**. The size of this property's array of strings is the same as the size of the **Counter Values** array of strings.

**Counter Names** and **Counter Values** are intended to be used together in order to display all statistics on the front panel. These properties do not require knowledge of specific property names. For example, if a new version of NI-XNET adds a statistic property (at the end of the arrays), the new property will display without change to your LabVIEW application.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.St.MAC.CtrNames |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatphyctrvalues.html language=enus -->
## TOPIC 00130: Interface:Ethernet:Statistics:PHY:Counter Values

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatphyctrvalues.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatphyctrvalues.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property returns the counter value of each Ethernet statistics PHY property supported by XNET. Each counter value is returned as a string for display, but the internal counter uses a 64-bit unsigned integer (U64) data type to avoid rollover. The counter resets to zero when the system powers up

### Interface:Ethernet:Statistics:PHY:Counter Values

This property returns the counter value of each Ethernet statistics PHY property supported by XNET. Each counter value is returned as a string for display, but the internal counter uses a 64-bit unsigned integer (U64) data type to avoid rollover. The counter resets to zero when the system powers up or the device is reset, and increments according to the description in Ethernet Statistics PHY Properties.

The counter value at a specific index corresponds to the name at the same index in Counter Names. The array of strings for this property is the same size as the Counter Names array of strings. Refer to Ethernet Statistics PHY Properties for a description of each counter value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.St.PHY.CtrValues |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxbad.html language=enus -->
## TOPIC 00131: Interface:Ethernet:Statistics:MAC:Rx Bad Frames Count

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxbad.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxbad.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is a count of frames received with an error detected by the Ethernet MAC and/or PHY. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.St.MAC.RxBad Data type cu64.png Permissions Read Only

### Interface:Ethernet:Statistics:MAC:Rx Bad Frames Count

This is a count of frames received with an error detected by the Ethernet MAC and/or PHY.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.St.MAC.RxBad |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxgood.html language=enus -->
## TOPIC 00132: Interface:Ethernet:Statistics:MAC:Rx Good Frames Count

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxgood.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenetstatrxgood.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is a count of error-free frames received. This count is equal to (Rx Good Unicast + Rx Good Multicast + Rx Good Broadcast). Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.St.MAC.RxGood Data type cu64.png Permissions Read Only

### Interface:Ethernet:Statistics:MAC:Rx Good Frames Count

This is a count of error-free frames received. This count is equal to (Rx Good Unicast + Rx Good Multicast + Rx Good Broadcast).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.St.MAC.RxGood |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeclkaccy.html language=enus -->
## TOPIC 00133: Interface:Ethernet:Time Sync:Clock Accuracy

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeclkaccy.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeclkaccy.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides the accuracy of the hardware clock (e.g. oscillator) distributed by the clock when it is the grandmaster. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.ClkAccy Data type cu32.png Permissions Read Only Within25ns 32 Within100n

### Interface:Ethernet:Time Sync:Clock Accuracy

This property provides the accuracy of the hardware clock (e.g. oscillator) distributed by the clock when it is the grandmaster.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.ClkAccy |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Within25ns | 32 |  |
| --- | --- | --- |
| Within100nsec | 33 |  |
| Within250ns | 34 |  |
| Within1usec | 35 |  |
| Within2500nsec | 36 |  |
| Within10usec | 37 |  |
| Within25usec | 38 |  |
| Within100usec | 39 |  |
| Within250usec | 40 |  |
| Within1msec | 41 |  |
| Within2500usec | 42 |  |
| Within10msec | 43 |  |
| Within25msec | 44 |  |
| Within100msec | 45 |  |
| Within250msec | 46 |  |
| Within1sec | 47 |  |
| Within10sec | 48 |  |
| GreaterThan10sec | 49 |  |
| Unknown | 254 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkid.html language=enus -->
## TOPIC 00134: Interface:Ethernet:Time Sync:Grandmaster Clock ID

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkid.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkid.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides the Clock ID of the currently selected grandmaster for this clock. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.GMClkID Data type cstr.png Permissions Read Only

### Interface:Ethernet:Time Sync:Grandmaster Clock ID

This property provides the Clock ID of the currently selected grandmaster for this clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.GMClkID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkoffvar.html language=enus -->
## TOPIC 00135: Interface:Ethernet:Time Sync:Grandmaster Clock Offset Scaled Log Variance

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkoffvar.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimegmclkoffvar.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides the Clock Offset Scaled Log Variance of the currently selected grandmaster for this clock. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.GMClkOffVar Data type cu32.png Permissions Read Only

### Interface:Ethernet:Time Sync:Grandmaster Clock Offset Scaled Log Variance

This property provides the Clock Offset Scaled Log Variance of the currently selected grandmaster for this clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.GMClkOffVar |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvl.html language=enus -->
## TOPIC 00136: Interface:Ethernet:Time Sync:Port:Log Announce Interval

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvl.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvl.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If Announce Transmit Enabled? is true, this property provides the current interval used for successive transmits of the Announce message by this port. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.AnnIntvl Data type ci32.png Permissions Read O

### Interface:Ethernet:Time Sync:Port:Log Announce Interval

If Announce Transmit Enabled? is true, this property provides the current interval used for successive transmits of the Announce message by this port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.AnnIntvl |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| 125 milliseconds | -3 |  |
| --- | --- | --- |
| 250 milliseconds | -2 |  |
| 500 milliseconds | -1 |  |
| 1 second | 0 |  |
| 2 seconds | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvlconf.html language=enus -->
## TOPIC 00137: Interface:Ethernet:Time Sync:Port:Log Announce Interval Configured

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvlconf.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportannintvlconf.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If Announce Transmit Enabled? is true, this property configures the interval between successive transmits of the Announce message by this port. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.AnnIntvlConf Data type ci32.png Permissions Read/Writ

### Interface:Ethernet:Time Sync:Port:Log Announce Interval Configured

If Announce Transmit Enabled? is true, this property configures the interval between successive transmits of the Announce message by this port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.AnnIntvlConf |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| 125 milliseconds | -3 |  |
| --- | --- | --- |
| 250 milliseconds | -2 |  |
| 500 milliseconds | -1 |  |
| 1 second | 0 |  |
| 2 seconds | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportanntx.html language=enus -->
## TOPIC 00138: Interface:Ethernet:Time Sync:Port:Announce Transmit Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportanntx.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportanntx.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the transmit of Announce messages, which provide properties of this port as a potential grandmaster. Since Announce messages are required for proper operation of the BMCA, this property is ignored when BMCA Enabled? is true. When this property is true, the port transmits Announce messages. T

### Interface:Ethernet:Time Sync:Port:Announce Transmit Enabled?

Enables the transmit of Announce messages, which provide properties of this port as a potential grandmaster. Since Announce messages are required for proper operation of the BMCA, this property is ignored when BMCA Enabled? is true.

When this property is true, the port transmits Announce messages. This value is the default behavior as specified in the protocol standard.

When this property is false, the port does not transmit Announce messages. When this property is false in the grandmaster, slave ports will not receive information about that grandmaster (e.g. properties like Grandmaster Clock Accuracy). Therefore, the false value is useful for in-vehicle applications in which each slave assumes properties for its grandmaster as part of the vehicle's static design.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.AnnTx? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportascap.html language=enus -->
## TOPIC 00139: Interface:Ethernet:Time Sync:Port:AS Capable?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportascap.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportascap.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property is specific to the IEEE Std 802.1AS Protocol. It returns true if the neighboring port is running the protocol according to the requirements in the standard (false otherwise). Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.AScap? D

### Interface:Ethernet:Time Sync:Port:AS Capable?

This property is specific to the IEEE Std 802.1AS Protocol. It returns true if the neighboring port is running the protocol according to the requirements in the standard (false otherwise).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.AScap? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdly.html language=enus -->
## TOPIC 00140: Interface:Ethernet:Time Sync:Port:Pdelay Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdly.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdly.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the exchange of Pdelay (peer-to-peer delay) messages, as a means of measuring Propagation Delay. When this property is true, the port transmits Pdelay request messages (Pdelay_Req) to the neighboring clock and processes received Pdelay response messages (Pdelay_Resp). The port also processes

### Interface:Ethernet:Time Sync:Port:Pdelay Enabled?

Enables the exchange of Pdelay (peer-to-peer delay) messages, as a means of measuring Propagation Delay.

When this property is true, the port transmits Pdelay request messages (Pdelay_Req) to the neighboring clock and processes received Pdelay response messages (Pdelay_Resp). The port also processes received Pdelay request messages and transmits Pdelay response messages. The Propagation Delay is measured using this message exchange. The Propagation Delay Configured property is not used while Pdelay is enabled.

When this property is false, Pdelay messages are not transmitted, and received Pdelay messages are ignored. The false value is useful for in-vehicle applications in which the topology for time synchronization is considered to be part of the vehicle's static design. The Propagation Delay Configured property must be used in order to specify the propagation delay for the port. The read-only Propagation Delay property reflects Propagation Delay Configured.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.Pdly? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdlyintvl.html language=enus -->
## TOPIC 00141: Interface:Ethernet:Time Sync:Port:Log Pdelay_Req Interval

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdlyintvl.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpdlyintvl.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If Pdelay Enabled? is true, this property provides the current interval used for successive transmits of the Pdelay_Req message by this port. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.PdlyIntvl Data type ci32.png Permissions Read Only 125

### Interface:Ethernet:Time Sync:Port:Log Pdelay_Req Interval

If Pdelay Enabled? is true, this property provides the current interval used for successive transmits of the Pdelay_Req message by this port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.PdlyIntvl |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| 125 milliseconds | -3 |  |
| --- | --- | --- |
| 250 milliseconds | -2 |  |
| 500 milliseconds | -1 |  |
| 1 second | 0 |  |
| 2 seconds | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportportstconf.html language=enus -->
## TOPIC 00142: Interface:Ethernet:Time Sync:Port:Port State Configured

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportportstconf.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportportstconf.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property configures the Port State when BMCA Enabled? is false. Valid values are Master and Slave. If BMCA Enabled? is true, the value in this property is ignored. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.PortStConf Data type cu32.pn

### Interface:Ethernet:Time Sync:Port:Port State Configured

This property configures the Port State when BMCA Enabled? is false. Valid values are Master and Slave. If BMCA Enabled? is true, the value in this property is ignored.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.PortStConf |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Master | 6 |  |
| --- | --- | --- |
| Slave | 9 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpropdlyth.html language=enus -->
## TOPIC 00143: Interface:Ethernet:Time Sync:Port:Propagation Delay Threshold

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpropdlyth.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportpropdlyth.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For IEEE Std 802.1AS, if the Propagation Delay exceeds the threshold in this property, the protocol assumes that a switch/router that is not 802.1AS-capable exists between this clock and the neighboring 802.1AS-capable clock. Since the resulting asymmetries have an adverse effect of time synchroniza

### Interface:Ethernet:Time Sync:Port:Propagation Delay Threshold

For IEEE Std 802.1AS, if the Propagation Delay exceeds the threshold in this property, the protocol assumes that a switch/router that is not 802.1AS-capable exists between this clock and the neighboring 802.1AS-capable clock. Since the resulting asymmetries have an adverse effect of time synchronization accuracy, this port sets AS Capable? to false.

The data type is DBL in seconds, which is typically used in LabVIEW for relative times. If nanoseconds are desired, multiply this value by 1000000000.

The propagation speed for copper wires is close to 2 * 10^8 meters/second. Therefore, multiplying this property value by 200000000 provides a close approximation of the cable length in meters.

If Pdelay Enabled? is false, this property is ignored.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.PropDlyTh |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrnames.html language=enus -->
## TOPIC 00144: Interface:Ethernet:Time Sync:Port:Statistics:Counter Names

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrnames.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrnames.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property returns the name of each Time Sync Port statistics property supported by XNET. The name uses uppercase for the first letter of each word, with space as a separator between words. The name at a specific index corresponds to the counter at the same index in Counter Values. The size of th

### Interface:Ethernet:Time Sync:Port:Statistics:Counter Names

This property returns the name of each Time Sync Port statistics property supported by XNET. The name uses uppercase for the first letter of each word, with space as a separator between words.

The name at a specific index corresponds to the counter at the same index in **Counter Values**. The size of this property's array of strings is the same as the size of the **Counter Values** array of strings.

**Counter Names** and **Counter Values** are intended to be used together in order to display all statistics on the front panel. These properties do not require knowledge of specific property names. For example, if a new version of NI-XNET adds a statistic property (at the end of the arrays), the new property will display without change to your LabVIEW application.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.St.CtrNames |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrvalues.html language=enus -->
## TOPIC 00145: Interface:Ethernet:Time Sync:Port:Statistics:Counter Values

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrvalues.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatctrvalues.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property returns the counter value of each Time Sync Port statistics property supported by XNET. Each counter value is returned as a string for display, but the internal counter uses type of U64 in order to avoid rollover. The counter resets to zero when the interface starts, and increments acc

### Interface:Ethernet:Time Sync:Port:Statistics:Counter Values

This property returns the counter value of each Time Sync Port statistics property supported by XNET. Each counter value is returned as a string for display, but the internal counter uses type of U64 in order to avoid rollover. The counter resets to zero when the interface starts, and increments according to the description in **Counter Names**.

The counter value at a specific index corresponds to the name at the same index in **Counter Names**. The size of this property's array of counters is the same as the size of the **Counter Names** array of strings.

Refer to **Counter Names** for a description of each counter value.

The array of counters are not provided as a single snapshot in time. For example, it is possible that a new frame is received as the values are returned, such that index 3 does not count the new frame, and index 4 does count the new frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.St.CtrValues |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatrxsync.html language=enus -->
## TOPIC 00146: Interface:Ethernet:Time Sync:Port:Statistics:Rx Sync Count

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatrxsync.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstatrxsync.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is a count of the number of Sync messages received. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.St.RxSync Data type cu64.png Permissions Read Only

### Interface:Ethernet:Time Sync:Port:Statistics:Rx Sync Count

This is a count of the number of Sync messages received.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.St.RxSync |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstattxpdreq.html language=enus -->
## TOPIC 00147: Interface:Ethernet:Time Sync:Port:Statistics:Tx Pdelay Request Count

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstattxpdreq.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportstattxpdreq.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is a count of the number of Pdelay_Req messages transmitted. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.St.TxPDReq Data type cu64.png Permissions Read Only

### Interface:Ethernet:Time Sync:Port:Statistics:Tx Pdelay Request Count

This is a count of the number of Pdelay_Req messages transmitted.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.St.TxPDReq |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsync.html language=enus -->
## TOPIC 00148: Interface:Ethernet:Time Sync:Port:Synced?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsync.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsync.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property indicates whether the time sync protocol's clock is successfully synchronized to other clocks in the network. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.Sync? Data type cbool.png Permissions Read Only

### Interface:Ethernet:Time Sync:Port:Synced?

This property indicates whether the time sync protocol's clock is successfully synchronized to other clocks in the network.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.Sync? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncintvlconf.html language=enus -->
## TOPIC 00149: Interface:Ethernet:Time Sync:Port:Log Sync Interval Configured

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncintvlconf.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncintvlconf.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If Port State is Master, this property configures the interval between successive transmits of the Sync message by this port. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.Time.Port.SyncIntvlConf Data type ci32.png Permissions Read/Write 125 millisecond

### Interface:Ethernet:Time Sync:Port:Log Sync Interval Configured

If Port State is Master, this property configures the interval between successive transmits of the Sync message by this port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.SyncIntvlConf |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| 125 milliseconds | -3 |  |
| --- | --- | --- |
| 250 milliseconds | -2 |  |
| 500 milliseconds | -1 |  |
| 1 second | 0 |  |
| 2 seconds | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncstat.html language=enus -->
## TOPIC 00150: Interface:Ethernet:Time Sync:Port:Sync Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncstat.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeportsyncstat.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides the current synchronization status of the time sync protocol. It is a ring as described in the following table: Synced: The time sync protocolâ€™s clock is successfully synchronized with other clocks in the network. This value is returned when the time synchronization protocol

### Interface:Ethernet:Time Sync:Port:Sync Status

This property provides the current synchronization status of the time sync protocol. It is a ring as described in the following table:

Synced: The time sync protocolâ€™s clock is successfully synchronized with other clocks in the network. This value is returned when the time synchronization protocol's Synced property is true.

EnetLinkDown: The interface can not transmit or receive frames (packets).

ProtocolDisabled: The time sync protocol is disabled.

MeasuringPropDelay: The port is exchanging messages to measure Propagation Delay, but the port is not sending time (Master) or receiving time (Slave).

MasterPendingAnnounce: The Port State is Master with the BMCA enabled and is waiting until at least two Announce Intervals have elapsed before declaring the port synchronized. This avoids reporting a false-positive when the BMCA has not finished electing the best master.

WaitingForMaster: The Port State is Slave and a Sync message has not been received from the master.

SyncingToMaster: The Port State is Slave and XNET's clock adjustment algorithm (servo) has not reached its final state (calibrated). A sufficient number of messages need to be exchanged such that synchronization quality (e.g. Offset From Master) is unlikely to improve significantly, but no fixed metric is applied as a threshold.

PeerNotProtoCapable: The time sync protocol is not detecting a neighbor that is running the protocol according to the requirements in the standard.

PropDelayExceedsTreshold: For IEEE Std 802.1AS, the measured propagation delay exceeds the value specified by the property Propagation Delay Threshold. As a result, the time sync protocol sets the property AS Capable false.

SyncReceiptTimeout: The Port State is Slave and the time sync protocol has not received a Sync message from the Master in at least the number of Sync intervals specified by the property Sync Receipt Timeout.

FrequencyOutOfRange: The Port State is Slave and the grandmasterâ€™s clock has exceeded the frequency range of XNET's clock (+/- 100 ppm).

SyncIntervalOutOfRange: The Port State is Slave and the master is sending Sync messages outside of the supported Sync interval range.

MultipleMastersDetected: The Port State is configured as Master with the BMCA disabled and another master has been detected by the time sync protocol.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Port.SyncStat |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Synced | 0 |  |
| --- | --- | --- |
| EnetLinkDown | 1 |  |
| ProtocolDisabled | 2 |  |
| MeasuringPropDelay | 3 |  |
| MasterPendingAnnounce | 4 |  |
| WaitingForMaster | 5 |  |
| SyncingToMaster | 6 |  |
| PeerNotProtoCapable | 7 |  |
| PropDelayExceedsTreshold | 8 |  |
| SyncReceiptTimeout | 9 |  |
| FrequencyOutOfRange | 10 |  |
| SyncIntervalOutOfRange | 11 |  |
| MultipleMastersDetected | 12 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri1.html language=enus -->
## TOPIC 00151: Interface:Ethernet:Time Sync:Priority1

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri1.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri1.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The BMCA uses this property as the first comparison to determine the grandmaster. Lower values take precedence. Valid values range from 0 to 255. The value 255 specifies that the clock is not grandmaster-capable (slave only). Remarks The following table lists the characteristics of this property. Sh

### Interface:Ethernet:Time Sync:Priority1

The BMCA uses this property as the first comparison to determine the grandmaster. Lower values take precedence. Valid values range from 0 to 255. The value 255 specifies that the clock is not grandmaster-capable (slave only).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Pri1 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri2.html language=enus -->
## TOPIC 00152: Interface:Ethernet:Time Sync:Priority2

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri2.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimepri2.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The BMCA uses this property as a secondary comparison, after comparing the properties for clock quality, and before using Clock ID as a tie-breaker. Lower values take precedence. Valid values range from 0 to 255. Remarks The following table lists the characteristics of this property. Short Name Intf

### Interface:Ethernet:Time Sync:Priority2

The BMCA uses this property as a secondary comparison, after comparing the properties for clock quality, and before using Clock ID as a tie-breaker. Lower values take precedence. Valid values range from 0 to 255.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.Pri2 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeproten.html language=enus -->
## TOPIC 00153: Interface:Ethernet:Time Sync:Protocol Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeproten.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimeproten.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (runs) the time synchronization Protocol. When this property is true, the Protocol transmits and receives messages in order to synchronize time with its neighboring ports. When this property is false, the Protocol does not transmit messages, and messages received for the protocol are ignored

### Interface:Ethernet:Time Sync:Protocol Enabled?

Enables (runs) the time synchronization Protocol.

When this property is true, the Protocol transmits and receives messages in order to synchronize time with its neighboring ports.

When this property is false, the Protocol does not transmit messages, and messages received for the protocol are ignored.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.ProtEn? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimestepsgm.html language=enus -->
## TOPIC 00154: Interface:Ethernet:Time Sync:Steps to Grandmaster

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimestepsgm.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettimestepsgm.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides the number of steps that this clock is removed from the grandmaster. For example, if there is a single Ethernet cable that connects this clock to the grandmaster, this property returns the value 1. Remarks The following table lists the characteristics of this property. Short N

### Interface:Ethernet:Time Sync:Steps to Grandmaster

This property provides the number of steps that this clock is removed from the grandmaster. For example, if there is a single Ethernet cable that connects this clock to the grandmaster, this property returns the value 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.StepsGM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettrigppssync.html language=enus -->
## TOPIC 00155: Interface:Ethernet:Trigger PPS Synced?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettrigppssync.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceenettrigppssync.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the configured PXI trigger that carries a pulse per second (PPS) has synchronized the network timekeeper on this interface. Remarks The following table lists the characteristics of this property. Short Name Intf.Enet.TrigPpsSync? Data type cbool.png Permissions Read Only

### Interface:Ethernet:Trigger PPS Synced?

Indicates if the configured PXI trigger that carries a pulse per second (PPS) has synchronized the network timekeeper on this interface.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.TrigPpsSync? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagenabled.html language=enus -->
## TOPIC 00156: Interface:Ethernet:Time Sync:VLAN Tag:Enabled?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagenabled.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagenabled.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the use of VLAN Tags with the time sync protocol. When this property is true, the protocol transmits messages with the user-provided VLAN Tag added. Received protocol messages which don't have a matching VLAN Tag are discarded. When this property is false, the time sync protocol does not add

### Interface:Ethernet:Time Sync:VLAN Tag:Enabled?

Enables the use of VLAN Tags with the time sync protocol.

When this property is true, the protocol transmits messages with the user-provided VLAN Tag added. Received protocol messages which don't have a matching VLAN Tag are discarded.

When this property is false, the time sync protocol does not add VLAN Tags to any transmitted messages, and received messages with a VLAN Tag are discarded.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.VlanTagEnabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagid.html language=enus -->
## TOPIC 00157: Interface:Ethernet:Time Sync:VLAN Tag:ID

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagid.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceethernettimesyncvlantagid.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When time sync protocol VLAN Tags are enabled, this property configures the VLAN ID for transmitted messages, and discards received messages that don't have a matching VLAN ID. The VLAN ID is a 12-bit field with values 0..4095, with 0 and 4095 being reserved. Remarks The following table lists the ch

### Interface:Ethernet:Time Sync:VLAN Tag:ID

When time sync protocol VLAN Tags are enabled, this property configures the VLAN ID for transmitted messages, and discards received messages that don't have a matching VLAN ID. The VLAN ID is a 12-bit field with values 0..4095, with 0 and 4095 being reserved.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.Enet.Time.VlanTagID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinbreaklength.html language=enus -->
## TOPIC 00158: Interface:LIN:Break Length

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinbreaklength.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinbreaklength.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property determines the length of the serial break used at the start of a frame header (schedule entry). The value is specified in bit-times. The valid range is 13â€“36 (inclusive). The default value is 13, which is the value the LIN standard specifies. Remarks The following table lists the cha

### Interface:LIN:Break Length

This property determines the length of the serial break used at the start of a frame header (schedule entry). The value is specified in bit-times.

The valid range is 13â€“36 (inclusive). The default value is 13, which is the value the LIN standard specifies.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.BreakLen |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinchecksumtoinputstream.html language=enus -->
## TOPIC 00159: Interface:LIN:Checksum to Input Stream?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinchecksumtoinputstream.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinchecksumtoinputstream.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property indicates whether checksums are reported in Input Stream session frames. The default of FALSE indicates that each frame Event ID equals 0. TRUE indicates that each frame Event ID contains the received checksum. Remarks The following table lists the characteristics of this property. Sho

### Interface:LIN:Checksum to Input Stream?

This property indicates whether checksums are reported in Input Stream session frames. The default of FALSE indicates that each frame Event ID equals 0. TRUE indicates that each frame Event ID contains the received checksum.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.ChecksumToInStrm? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagp2min.html language=enus -->
## TOPIC 00160: Interface:LIN:Diagnostics P2min

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagp2min.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagp2min.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When the interface is the slave, this is the minimum time in seconds between reception of the last frame of the diagnostic request message and transmission of the response for the first frame in the diagnostic response message by the slave. Remarks The following table lists the characteristics of th

### Interface:LIN:Diagnostics P2min

When the interface is the slave, this is the minimum time in seconds between reception of the last frame of the diagnostic request message and transmission of the response for the first frame in the diagnostic response message by the slave.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.DiagP2min |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagstmin.html language=enus -->
## TOPIC 00161: Interface:LIN:Diagnostics STmin

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagstmin.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelindiagstmin.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When the interface is the slave, this is the minimum time in seconds it places between the end of transmission of a frame in a diagnostic response message and the start of transmission of the response for the next frame in the diagnostic response message. Remarks The following table lists the charac

### Interface:LIN:Diagnostics STmin

When the interface is the slave, this is the minimum time in seconds it places between the end of transmission of a frame in a diagnostic response message and the start of transmission of the response for the next frame in the diagnostic response message.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.DiagSTmin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinmaster.html language=enus -->
## TOPIC 00162: Interface:LIN:Master?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinmaster.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinmaster.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This boolean property specifies the NI-XNET LIN interface role on the network: master (true) or slave (false). The default value for this property is false (slave). If you call the XNET Write (State LIN Schedule Change) VI to request execution of a schedule, that implicitly sets this property to tru

### Interface:LIN:Master?

This boolean property specifies the NI-XNET LIN interface role on the network: master (true) or slave (false).

The default value for this property is false (slave).

If you call the XNET Write (State LIN Schedule Change) VI to request execution of a schedule, that implicitly sets this property to true (master).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.Master? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinoutputstreamslaveresponselistbynad.html language=enus -->
## TOPIC 00163: Interface:LIN:Output Stream Slave Response List By NAD

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinoutputstreamslaveresponselistbynad.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinoutputstreamslaveresponselistbynad.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property provides a list of NADs for use with the replay feature (Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive). Besides filtering for the frame ID through the Interface:Interface:Output Stream List By ID property this property allows another level of filt

### Interface:LIN:Output Stream Slave Response List By NAD

This property provides a list of NADs for use with the replay feature (**Interface:Output Stream Timing** property set to Replay Exclusive or Replay Inclusive).

Besides filtering for the frame ID through the **Interface:Interface:Output Stream List By ID** property this property allows another level of filtering frames by the NAD of the sending device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.OutStrmSlvRspListByNAD |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinsleep.html language=enus -->
## TOPIC 00164: Interface:LIN:Sleep

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinsleep.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinsleep.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this property to change the NI-XNET LIN interface sleep/awake state and optionally to change remote node (ECU) sleep/awake states. The property is a ring (enumerated list) with the following values: - Remote Sleep: Set interface to sleep locally and transmit sleep requests to remote nodes - Remo

### Interface:LIN:Sleep

Use this property to change the NI-XNET LIN interface sleep/awake state and optionally to change remote node (ECU) sleep/awake states.

The property is a ring (enumerated list) with the following values:
- Remote Sleep: Set interface to sleep locally and transmit sleep requests to remote nodes
- Remote Wake: Set interface to awake locally and transmit wakeup requests to remote nodes
- Local Sleep: Set interface to sleep locally and not to interact with the network
- Local Wake: Set interface to awake locally and not to interact with the network

The property is write only. Setting a new value is effectively a request, and the property node returns before the request is complete. To detect the current interface sleep/wake state, use the **XNET Read (State LIN Comm)** VI.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.Sleep |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

| Remote Sleep | 0 |  |
| --- | --- | --- |
| Remote Wake | 1 |  |
| Local Sleep | 2 |  |
| Local Wake | 3 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinstartallowedwithoutbuspower.html language=enus -->
## TOPIC 00165: Interface:LIN:Start Allowed without Bus Power?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinstartallowedwithoutbuspower.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelinstartallowedwithoutbuspower.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property allows to start a LIN session without bus power being applied to the interface. If set to FALSE (default), this attempt causes an error condition. Remarks The following table lists the characteristics of this property. Short Name Intf.LIN.StrtWoPwr? Data type cbool.png Permissions Read

### Interface:LIN:Start Allowed without Bus Power?

This property allows to start a LIN session without bus power being applied to the interface. If set to FALSE (default), this attempt causes an error condition.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.StrtWoPwr? |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelintermination.html language=enus -->
## TOPIC 00166: Interface:LIN:Termination

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelintermination.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacelintermination.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Termination property configures the NI-XNET interface LIN connector (port) onboard termination. The enumeration is Off (disabled) and On (enabled). The default value is Off. Remarks The following table lists the characteristics of this property. Short Name Intf.LIN.Term Data type cu32.png Permis

### Interface:LIN:Termination

The Termination property configures the NI-XNET interface LIN connector (port) onboard termination. The enumeration is Off (disabled) and On (enabled). The default value is Off.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.LIN.Term |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Off | 0 |  |
| --- | --- | --- |
| On | 1 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamlistbyid.html language=enus -->
## TOPIC 00167: Interface:Output Stream List By ID

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamlistbyid.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamlistbyid.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Output Stream List By ID property provides a list of frames for use with the replay feature (Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive). This property serves the same purpose as Interface:Output Stream List, in that it provides a list of frames for repla

### Interface:Output Stream List By ID

The Output Stream List By ID property provides a list of frames for use with the replay feature (Interface:Output Stream Timing property set to Replay Exclusive or Replay Inclusive).

This property serves the same purpose as Interface:Output Stream List, in that it provides a list of frames for replay filtering. This property provides an alternate format for you to specify the frames by their CAN/LIN arbitration ID. The property's data type is an array of unsigned 32-bit integer (U32). Each integer represents a CAN/LIN frame's identifier, using the same encoding as the Raw Frame Format.

Within each CAN frame ID value, bit 29 (hex 20000000) indicates the CAN identifier format (set for extended, clear for standard). If bit 29 is clear, the lower 11 bits (0â€“10) contain the CAN frame identifier. If bit 29 is set, the lower 29 bits (0â€“28) contain the CAN frame identifier.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.OutStrmListById |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamtiming.html language=enus -->
## TOPIC 00168: Interface:Output Stream Timing

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamtiming.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfaceoutputstreamtiming.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Output Stream Timing property configures how the firmware transmits frames queued using a Frame Output Stream session. The following table lists the accepted values: - Immediate - Replay Exclusive - Replay Inclusive When you configure this property to be Immediate, frames are dequeued from the q

### Interface:Output Stream Timing

The Output Stream Timing property configures how the firmware transmits frames queued using a Frame Output Stream session. The following table lists the accepted values:
- Immediate
- Replay Exclusive
- Replay Inclusive

When you configure this property to be Immediate, frames are dequeued from the queue and transmitted immediately to the bus. The firmware transmits all frames in the queue as fast as possible. Immediate is the default value.

When you configure this property as Replay Exclusive or Replay Inclusive, the firmware is placed into a Replay mode. In this mode, the firmware evaluates the frame timestamps and attempts to maintain the original transmission times as the timestamp stored in the frame indicates. The actual transmission time is based on the relative time difference between the first dequeued frame and the time contained in the dequeued frame.

When in one of the replay modes, you can use the **Interface:Output Stream List** property to supply a list. In Replay Exclusive mode, the firmware transmits only frames that do not appear in the list. In Replay Inclusive mode, the firmware transmits only frames that appear in the list. Using these modes, you can either emulate an ECU (Replay Inclusive, where the list contains the frames the ECU transmits) or test an ECU (Replay Exclusive, where the list contains the frames the ECU transmits), or some other combination. You can replay all frames by using Replay Exclusive mode without setting any list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.OutStrmTimng |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Immediate | 0 |  |
| --- | --- | --- |
| ReplayExclusive | 1 |  |
| ReplayInclusive | 2 |  |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacesourceterminalstarttrigger.html language=enus -->
## TOPIC 00169: Interface:Source Terminal:Start Trigger

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacesourceterminalstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessioninterfacesourceterminalstarttrigger.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property specifies the name of a terminal where there is a digital signal to use as the Start Trigger source. The data type is NI Terminal (DAQmx terminal). This property is supported for C Series modules in a CompactDAQ chassis. It is not supported for CompactRIO, PXI, or PCI. Use this propert

### Interface:Source Terminal:Start Trigger

This property specifies the name of a terminal where there is a digital signal to use as the Start Trigger source. The data type is NI Terminal (DAQmx terminal).

This property is supported for C Series modules in a CompactDAQ chassis. It is not supported for CompactRIO, PXI, or PCI.

Use this property to connect the interface Start Trigger to triggers in other modules and/or interfaces. When you read this property, you specify the interface Start Trigger as the source of a connection. When you write this property, you specify the interface Start Trigger as the destination of a connection, and the value you write represents the source. For example, to connect the Start Trigger of analog input module for use as Start Trigger of a CAN interface, read the DAQmx Trigger Node property **Start:Digital Edge:Source**, and write the resulting value to this CAN interface property.

The connection that is created by this property is disconnected when you clear (close) all relevant sessions.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Intf.SrcTerm.StartTrigger |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionlistofframes.html language=enus -->
## TOPIC 00170: List of Frames

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionlistofframes.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionlistofframes.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: List of frames used to create the session (array of XNET Frame I/O Name). This property is valid only for sessions with a mode of Frame Input or Frame Output. For Signal Input/Output session, use the List of Signals property. Remarks The following table lists the characteristics of this property. Sh

### List of Frames

List of frames used to create the session (array of XNET Frame I/O Name).
This property is valid only for sessions with a **mode** of Frame Input or Frame Output. For Signal Input/Output session, use the **List of Signals** property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ListFrms |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionlistofsignals.html language=enus -->
## TOPIC 00171: List of Signals

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionlistofsignals.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionlistofsignals.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: List of signals used to create the session (array of XNET Signal I/O Name). This property is valid only for sessions with a mode of Signal Input or Signal Output. For Frame Input/Output session, use the List of Frames property. Remarks The following table lists the characteristics of this property.

### List of Signals

List of signals used to create the session (array of XNET Signal I/O Name).
This property is valid only for sessions with a **mode** of Signal Input or Signal Output. For Frame Input/Output session, use the **List of Frames** property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ListSigs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionnumberofvaluespending.html language=enus -->
## TOPIC 00172: Number of Values Pending

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionnumberofvaluespending.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionnumberofvaluespending.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of values pending for the session. Remarks The following table lists the characteristics of this property. Short Name NumPend Data type cu32.png Permissions Read Only

### Number of Values Pending

Number of values pending for the session.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumPend |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionpayloadlengthmaximum.html language=enus -->
## TOPIC 00173: Payload Length Maximum

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionpayloadlengthmaximum.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionpayloadlengthmaximum.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum payload length of all frames in this session, expressed as bytes. This property does not apply to Signal sessions (only Frame). Remarks The following table lists the characteristics of this property. Short Name PayldLenMax Data type cu32.png Permissions Read Only

### Payload Length Maximum

Maximum payload length of all frames in this session, expressed as bytes. This property does not apply to Signal sessions (only Frame).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PayldLenMax |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionqueuesize.html language=enus -->
## TOPIC 00174: Queue Size

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionqueuesize.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionqueuesize.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For output sessions, queues store data passed to the XNET Write VI and not yet transmitted onto the network. For input sessions, queues store data received from the network and not yet obtained using the XNET Read VI. For most applications, the default queue sizes are sufficient. You can write to th

### Queue Size

For output sessions, queues store data passed to the **XNET Write** VI and not yet transmitted onto the network. For input sessions, queues store data received from the network and not yet obtained using the **XNET Read** VI. For most applications, the default queue sizes are sufficient. You can write to this property to override the default.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QueueSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939ecubusy.html language=enus -->
## TOPIC 00175: SAE J1939:ECU Busy

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939ecubusy.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939ecubusy.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the J1939 session temporarily does not accept long messages. Remarks The following table lists the characteristics of this property. Short Name J1939.Busy Data type cbool.png Permissions Read/Write

### SAE J1939:ECU Busy

Indicates whether the J1939 session temporarily does not accept long messages.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.Busy |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939includedestaddrinpgn.html language=enus -->
## TOPIC 00176: SAE J1939:Include Destination Address in PGN

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939includedestaddrinpgn.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939includedestaddrinpgn.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Include the J1939 destination address (PDU1 PS field) when matching received frames to database frames. Remarks The following table lists the characteristics of this property. Short Name J1939.IncludeDestAddrInPGN Data type cbool.png Permissions Read/Write

### SAE J1939:Include Destination Address in PGN

Include the J1939 destination address (PDU1 PS field) when matching received frames to database frames.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.IncludeDestAddrInPGN |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939maximumrepeatcts.html language=enus -->
## TOPIC 00177: SAE J1939:Maximum Repeat CTS

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939maximumrepeatcts.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939maximumrepeatcts.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum number of CTS repetitions for the J1939 Transport Protocol. Remarks The following table lists the characteristics of this property. Short Name J1939.MaxReptCTS Data type cu32.png Permissions Read/Write

### SAE J1939:Maximum Repeat CTS

Maximum number of CTS repetitions for the J1939 Transport Protocol.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.MaxReptCTS |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939nodename.html language=enus -->
## TOPIC 00178: SAE J1939:Node Name

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939nodename.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939nodename.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The J1939 Node Name associated with this session. This is usually assigned as content of the J1939:ECU property, but can be read out or overridden manually. Remarks The following table lists the characteristics of this property. Short Name J1939.NodeName Data type cu64.png Permissions Read/Write

### SAE J1939:Node Name

The J1939 Node Name associated with this session. This is usually assigned as content of the **J1939:ECU** property, but can be read out or overridden manually.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.NodeName |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt2.html language=enus -->
## TOPIC 00179: SAE J1939:Timing:Timeout T2

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt2.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt2.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the timeout T2 value at the responder node. Value is the maximum gap between sending out a TP.CM_CTS message and receiving the next TP.DT message, in seconds. Remarks The following table lists the characteristics of this property. Short Name J1939.TimeoutT2 Data type cdbl.png Permissions Rea

### SAE J1939:Timing:Timeout T2

Changes the timeout T2 value at the responder node. Value is the maximum gap between sending out a TP.CM_CTS message and receiving the next TP.DT message, in seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.TimeoutT2 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt3.html language=enus -->
## TOPIC 00180: SAE J1939:Timing:Timeout T3

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt3.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-session/propertysessionsaej1939timeoutt3.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the timeout T3 value at the originator node. Value is the maximum gap between sending out a TP.CM_RTS message or the last TP.DT message and receiving the TP.CM_CTS response, in seconds. Remarks The following table lists the characteristics of this property. Short Name J1939.TimeoutT3 Data ty

### SAE J1939:Timing:Timeout T3

Changes the timeout T3 value at the originator node. Value is the maximum gap between sending out a TP.CM_RTS message or the last TP.DT message and receiving the TP.CM_CTS response, in seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | J1939.TimeoutT3 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Session Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalbyteorder.html language=enus -->
## TOPIC 00181: Byte Order

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalbyteorder.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalbyteorder.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Byte order in the frame payload. This property is a ring (enumerated list) and is required. Remarks The following table lists the characteristics of this property. Short Name ByteOrdr Data type cu32.png Permissions Read/Write Little Endian 0 Big Endian 1

### Byte Order

Byte order in the frame payload. This property is a ring (enumerated list) and is required.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ByteOrdr |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Little Endian | 0 |  |
| --- | --- | --- |
| Big Endian | 1 |  |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalconfigstatus.html language=enus -->
## TOPIC 00182: Configuration Status

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalconfigstatus.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalconfigstatus.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuration status of the signal. This property is used only if you change the Database property Show Invalid From Open? from false (default) to true. Remarks The following table lists the characteristics of this property. Short Name ConfigStatus Data type ci32.png Permissions Read Only

### Configuration Status

Configuration status of the signal. This property is used only if you change the Database property **Show Invalid From Open?** from false (default) to true.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConfigStatus |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignaldefaultvalue.html language=enus -->
## TOPIC 00183: Default Value

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignaldefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignaldefaultvalue.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default value of the signal, specified as scaled floating point units (DBL). Remarks The following table lists the characteristics of this property. Short Name Default Data type cdbl.png Permissions Read/Write

### Default Value

Default value of the signal, specified as scaled floating point units (DBL).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Default |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignaldynamic.html language=enus -->
## TOPIC 00184: Mux:Dynamic?

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignaldynamic.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignaldynamic.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether this signal is data multiplexed, also known as dynamic (boolean). Signals that depend on the multiplexer are considered dynamic (this property true), and are contained in a subframe. Signals that are common to all frame values are considered static (this property false). Remarks Th

### Mux:Dynamic?

Specifies whether this signal is data multiplexed, also known as dynamic (boolean). Signals that depend on the multiplexer are considered dynamic (this property true), and are contained in a subframe. Signals that are common to all frame values are considered static (this property false).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.Dynamic? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalmax.html language=enus -->
## TOPIC 00185: Maximum Value

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalmax.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalmax.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum value of the signal, specified as scaled floating point units (DBL). Remarks The following table lists the characteristics of this property. Short Name Max Data type cdbl.png Permissions Read/Write

### Maximum Value

Maximum value of the signal, specified as scaled floating point units (DBL).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalmultiplexervalue.html language=enus -->
## TOPIC 00186: Mux:Multiplexer Value

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalmultiplexervalue.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalmultiplexervalue.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When Mux:Dynamic? is true, this specifies the dynamic subframe in which the signal is contained. When the value of the data multiplexer signal matches this value, the dynamic signal exists in the frame. Remarks The following table lists the characteristics of this property. Short Name Mux.MuxValue D

### Mux:Multiplexer Value

When **Mux:Dynamic?** is true, this specifies the dynamic subframe in which the signal is contained. When the value of the data multiplexer signal matches this value, the dynamic signal exists in the frame.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mux.MuxValue |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalname.html language=enus -->
## TOPIC 00187: Name (Short)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalname.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalname.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short name of the signal (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database, cluster, and frame name. If you write this property, it changes both short and long name (see Detailed help). Remarks The following table lists the characteristics of th

### Name (Short)

Short name of the signal (string).

The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database, cluster, and frame name. If you write this property, it changes both short and long name (see **Detailed help**).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NameShort |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-signal/propertysignalscalingfactor.html language=enus -->
## TOPIC 00188: Scaling Factor

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-signal/propertysignalscalingfactor.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-signal/propertysignalscalingfactor.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Scaling factor used to convert bits in frame payload to/from scaled floating point units. The scaling factor is the A in the linear scaling formula AX+B, where X is the raw data, and B is the scaling offset. Remarks The following table lists the characteristics of this property. Short Name ScaleFac

### Scaling Factor

Scaling factor used to convert bits in frame payload to/from scaled floating point units. The scaling factor is the A in the linear scaling formula AX+B, where X is the raw data, and B is the scaling offset.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ScaleFac |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Signal Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-subframe/propertysubframename.html language=enus -->
## TOPIC 00189: Name (Short)

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-subframe/propertysubframename.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-subframe/propertysubframename.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Short name of the subframe (string). The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database, cluster, and frame name. If you write this property, it changes both short and long name (see Detailed help). Remarks The following table lists the characteristics of

### Name (Short)

Short name of the subframe (string).

The I/O name (long name) contains qualifiers to ensure that it is unique, such as the database, cluster, and frame name. If you write this property, it changes both short and long name (see **Detailed help**).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NameShort |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET Subframe Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-system/propertysystemdevices.html language=enus -->
## TOPIC 00190: Devices

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-system/propertysystemdevices.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-system/propertysystemdevices.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array of devices contained in the current system (array of XNET Device I/O Name). Remarks The following table lists the characteristics of this property. Short Name Devices Data type c1dgenclassrntag.png Permissions Read Only

### Devices

Array of devices contained in the current system (array of XNET Device I/O Name).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Devices |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET System Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-system/propertysystemversionbuild.html language=enus -->
## TOPIC 00191: Version:Build

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-system/propertysystemversionbuild.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-system/propertysystemversionbuild.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Build number for the driver (seldom used). Remarks The following table lists the characteristics of this property. Short Name Ver.Build Data type cu32.png Permissions Read Only

### Version:Build

Build number for the driver (seldom used).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ver.Build |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET System Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-system/propertysystemversionminor.html language=enus -->
## TOPIC 00192: Version:Minor

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-system/propertysystemversionminor.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-system/propertysystemversionminor.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Minor version number of the driver. The Minor version increments based on minor enhancements to features, support for new hardware or operating systems, and so on. Remarks The following table lists the characteristics of this property. Short Name Ver.Minor Data type cu32.png Permissions Read Only

### Version:Minor

Minor version number of the driver. The Minor version increments based on minor enhancements to features, support for new hardware or operating systems, and so on.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ver.Minor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET System Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-system/propertysystemversionupdate.html language=enus -->
## TOPIC 00193: Version:Update

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-system/propertysystemversionupdate.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-system/propertysystemversionupdate.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Update version number of the driver. The Update version increments based on changes that do not impact features, such as bug fixes. Remarks The following table lists the characteristics of this property. Short Name Ver.Update Data type cu32.png Permissions Read Only

### Version:Update

Update version number of the driver. The Update version increments based on changes that do not impact features, such as bug fixes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ver.Update |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET System Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-tcp-socket/propertyipstacktcprxdata.html language=enus -->
## TOPIC 00194: Receive Data Available

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-tcp-socket/propertyipstacktcprxdata.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-tcp-socket/propertyipstacktcprxdata.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of bytes available for Read, expressed as bytes. Remarks The following table lists the characteristics of this property. Short Name RxData Data type cu32.png Permissions Read Only

### Receive Data Available

Number of bytes available for Read, expressed as bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RxData |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

XNET TCP Socket Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=resource/objmgr/xnet-rc/xnet-udp-socket/propertyipstackudprxbuf.html language=enus -->
## TOPIC 00195: Receive Buffer Size

- bundle_id: `xnet-labview-api-ref`
- source_path: `resource/objmgr/xnet-rc/xnet-udp-socket/propertyipstackudprxbuf.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/resource/objmgr/xnet-rc/xnet-udp-socket/propertyipstackudprxbuf.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maximum size of receive buffer, expressed as bytes. Remarks The following table lists the characteristics of this property. Short Name RxBuf Data type cu32.png Permissions Read/Write

### Receive Buffer Size

Maximum size of receive buffer, expressed as bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RxBuf |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

XNET UDP Socket Properties

<!--NI_TOPIC bundle=xnet-labview-api-ref path=vi-lib/userdefined/high-color/xnet/database-mnu.html language=enus -->
## TOPIC 00196: Database Controls

- bundle_id: `xnet-labview-api-ref`
- source_path: `vi-lib/userdefined/high-color/xnet/database-mnu.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/vi-lib/userdefined/high-color/xnet/database-mnu.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: I/O names for access to databases that specify the configuration of the embedded network, including frame and signal data that is transferred. Each class of object in the database is represented by a distinct I/O name class. icon

### Database Controls

I/O names for access to databases that specify the configuration of the embedded network, including frame and signal data that is transferred. Each class of object in the database is represented by a distinct I/O name class.

[IMAGE alt='icon' src='database-mnu.png']

- [XNET Database](../../../../vi-lib/userdefined/xnetdatabase-ctl.html) To communicate with hardware products on the external CAN/FlexRay network, NI-XNET applications must understand how that hardware communicates in the actual embedded system, such as the vehicle. This embedded communication is described within a standardized file, such as CANdb (.dbc) or NI-CAN (.ncd) for CAN, or FIBEX (.xml) for FlexRay. Within NI-XNET, this file is referred to as a database. The database contains many object classes, each of which describes a distinct entity in the embedded system. Use the XNET Database I/O name to select a database, access properties, and invoke methods (for example, save).
- [XNET Cluster](../../../../vi-lib/userdefined/xnetcluster-ctl.html) Each database contains one or more clusters, where the cluster represents a collection of hardware products all connected over a shared cabling harness. In other words, each cluster represents a single CAN network or FlexRay network. For example, the database may describe a single vehicle, where the vehicle contains a Body CAN cluster, a Powertrain CAN cluster, and a Chassis FlexRay cluster. Use the XNET Cluster I/O name to select a cluster, access properties, and invoke methods.
- [XNET ECU](../../../../vi-lib/userdefined/xnetecu-ctl.html) Each Electronic Control Unit (ECU) represents a single hardware product in the embedded system. The cluster contains one or more ECUs, all connected by a CAN or FlexRay cable. Use the XNET ECU I/O name to select an ECU, access properties, and invoke methods.
- [XNET Frame](../../../../vi-lib/userdefined/xnetframe-ctl.html) Each frame represents a unique unit of data transfer over the cluster cable. The frame bits contain payload data and an identifier that specifies the data (signal) content. Only one ECU in the cluster transmits each frame, and one or more ECUs receive each frame. Use the XNET Frame I/O name to select a frame, access properties, and invoke methods.
- [XNET PDU](../../../../vi-lib/userdefined/xnetpdu-ctl.html) Many FlexRay networks use the concept of a Protocol Data Unit (PDU) to implement configurations similar to CAN. The PDU is a container of signals. You can use a single PDU within multiple frames for faster timing. A single frame can contain multiple PDUs, each updated independently. Use the XNET PDU I/O name to select a PDU, access properties, and invoke methods.
- [XNET Signal](../../../../vi-lib/userdefined/xnetsignal-ctl.html) Each frame contains zero or more values, each of which is called a signal. For example, the first two bytes of a frame payload may represent a temperature, and the third payload byte may represent a pressure. Within the database, each signal specifies its name, position, and length of the raw bits in the frame, and a scaling formula to convert raw bits to/from a physical unit. The physical unit uses a LabVIEW double-precision floating-point numeric type. The signal is the highest level of abstraction for embedded networks. When you use an XNET Session to read/write signal values as physical units, your application does not need to be concerned with protocol details and frame encoding. Use the XNET Signal I/O name to select a signal, access properties, and invoke methods.
- [XNET LIN Schedule](../../../../vi-lib/userdefined/xnetlinschedule-ctl.html) The LIN protocol is different than CAN or FlexRay, in that it supports multiple schedules that determine when frames transmit. You can change the current schedule at runtime. Within a database file, a cluster for LIN contains one or more LIN schedules. Each LIN schedule contains one or more LIN schedule entries. Use the XNET LIN Schedule I/O name to select a schedule, access properties, and invoke methods.

Parent topic:

XNET Controls

<!--NI_TOPIC bundle=xnet-labview-api-ref path=vi-lib/userdefined/xnetcluster-ctl.html language=enus -->
## TOPIC 00197: XNET Cluster

- bundle_id: `xnet-labview-api-ref`
- source_path: `vi-lib/userdefined/xnetcluster-ctl.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/vi-lib/userdefined/xnetcluster-ctl.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Each database contains one or more clusters, where the cluster represents a collection of hardware products all connected over a shared cabling harness. In other words, each cluster represents a single CAN network or FlexRay network. For example, the database may describe a single vehicle, where the

### XNET Cluster

Each database contains one or more clusters, where the cluster represents a collection of hardware products all connected over a shared cabling harness. In other words, each cluster represents a single CAN network or FlexRay network. For example, the database may describe a single vehicle, where the vehicle contains a Body CAN cluster, a Powertrain CAN cluster, and a Chassis FlexRay cluster.

Use the XNET Cluster I/O name to select a cluster, access properties, and invoke methods.

[IMAGE alt='icon' src='xnetcluster-ctl.png']

#### Data type

| XNET Cluster — This control provides the control form of the XNET Cluster I/O name. You drag a control to the front panel of your VI, so that the user of the VI can select a name. For a complete description, refer to XNET Cluster I/O Name. |
| --- |

Parent topic:

Database Controls

<!--NI_TOPIC bundle=xnet-labview-api-ref path=vi-lib/userdefined/xnetdatabase-ctl.html language=enus -->
## TOPIC 00198: XNET Database

- bundle_id: `xnet-labview-api-ref`
- source_path: `vi-lib/userdefined/xnetdatabase-ctl.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/vi-lib/userdefined/xnetdatabase-ctl.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: To communicate with hardware products on the external CAN/FlexRay network, NI-XNET applications must understand how that hardware communicates in the actual embedded system, such as the vehicle. This embedded communication is described within a standardized file, such as CANdb (.dbc) or NI-CAN (.ncd

### XNET Database

To communicate with hardware products on the external CAN/FlexRay network, NI-XNET applications must understand how that hardware communicates in the actual embedded system, such as the vehicle. This embedded communication is described within a standardized file, such as CANdb (.dbc) or NI-CAN (.ncd) for CAN, or FIBEX (.xml) for FlexRay. Within NI-XNET, this file is referred to as a database. The database contains many object classes, each of which describes a distinct entity in the embedded system.

Use the XNET Database I/O name to select a database, access properties, and invoke methods (for example, save).

[IMAGE alt='icon' src='xnetdatabase-ctl.png']

#### Data type

| XNET Database — This control provides the control form of the XNET Database I/O name. You drag a control to the front panel of your VI, so that the user of the VI can select a name. For a complete description, refer to XNET Database I/O Name.. |
| --- |

Parent topic:

Database Controls

<!--NI_TOPIC bundle=xnet-labview-api-ref path=vi-lib/userdefined/xnetinterface-ctl.html language=enus -->
## TOPIC 00199: XNET Interface

- bundle_id: `xnet-labview-api-ref`
- source_path: `vi-lib/userdefined/xnetinterface-ctl.html`
- source_url: https://docs-be.ni.com/bundle/xnet-labview-api-ref/raw/resource/enus/vi-lib/userdefined/xnetinterface-ctl.html
- document_id: `xnet-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The XNET interface represents a single CAN or FlexRay connector (port) on the device. Within NI-XNET, the interface is the object used to communicate with external hardware described in the database. When you create an NI-XNET session, you specify a physical and logical connection between the NI int

### XNET Interface

The XNET interface represents a single CAN or FlexRay connector (port) on the device. Within NI-XNET, the interface is the object used to communicate with external hardware described in the database. When you create an NI-XNET session, you specify a physical and logical connection between the NI interface and a cluster (network).

The XNET interface I/O name is used to select an interface to pass to the XNET Create Session VI, and to read hardware information properties.

[IMAGE alt='icon' src='xnetinterface-ctl.png']

#### Data type

| XNET Interface — This control provides the control form of the XNET Interface I/O name. You drag a control to the front panel of your VI, so that the user of the VI can select a name. For a complete description, refer to XNET Interface I/O Name. |
| --- |

Parent topic:

System Controls
