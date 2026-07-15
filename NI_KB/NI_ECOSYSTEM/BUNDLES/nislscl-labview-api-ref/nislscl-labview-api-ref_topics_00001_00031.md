# NI DOCUMENT BUNDLE: nislscl-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=nislscl-labview-api-ref start=1 end=31 -->
<!--NI_TOPIC bundle=nislscl-labview-api-ref path=menus/categories/measurement/slsc-switch-mnu.html language=enus -->
## TOPIC 00001: NI-SLSC Switch

- bundle_id: `nislscl-labview-api-ref`
- source_path: `menus/categories/measurement/slsc-switch-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc-switch-mnu.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on the NI-SLSC Switch palette to build the block diagram. icon

### NI-SLSC Switch

Use the VIs on the NI-SLSC Switch palette to build the block diagram.

[IMAGE alt='icon' src='slsc-switch-mnu.png']

- [Initialize with Topology VI](../../../vi-lib/slsc-switch/initialize-with-topology-vi.html) Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module.
- [Close VI](../../../vi-lib/slsc-switch/close-vi.html) Terminates the NI-SLSC Switch session and all of its attributes and deallocates any memory resources the driver uses.
- [Connect Channels VI](../../../vi-lib/slsc-switch/connect-channels-vi.html) Creates connections between channels.
- [Disconnect Channels VI](../../../vi-lib/slsc-switch/disconnect-channels-vi.html) Breaks connections between channels.
- [Set Path VI](../../../vi-lib/slsc-switch/set-path-vi.html) Connects two channels by specifying an explicit path in the path parameter. This VI is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use Connect Channels VI.
- [Can Connect Channels VI](../../../vi-lib/slsc-switch/can-connect-channels-vi.html) Verifies that a path between channel 1 and channel 2 can be created.
- [Disconnect All Channels VI](../../../vi-lib/slsc-switch/disconnect-all-channels-vi.html) Breaks all known existing paths.
- [Get Path VI](../../../vi-lib/slsc-switch/get-path-vi.html) Returns a string that identifies the explicit path created with Connect Channels VI. Pass this string to Set Path VI to establish the exact same path in future connections.
- [SLSC Switch Property Node VI](../../../vi-lib/slsc-switch/slsc-switch-property-node-vi.html) Gets (reads) and/or sets (writes) properties of a reference. Use the property node to get or set properties and methods on local or remote application instances, VIs, and objects. You also can use the Property Node to access the private data of a LabVIEW class.
- [Relay](../../../menus/categories/measurement/slsc-switch/relay-mnu.html) Use the SLSC Switch relay VIs to control and query individual relays of an NI SLSC switch.
- [Utility](../../../menus/categories/measurement/slsc-switch/utility-mnu.html) Use the SLSC Switch utility VIs to exercise additional features of a SLSC switch.

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=menus/categories/measurement/slsc-switch/relay-mnu.html language=enus -->
## TOPIC 00002: Relay

- bundle_id: `nislscl-labview-api-ref`
- source_path: `menus/categories/measurement/slsc-switch/relay-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc-switch/relay-mnu.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the SLSC Switch relay VIs to control and query individual relays of an NI SLSC switch. icon

### Relay

Use the SLSC Switch relay VIs to control and query individual relays of an NI SLSC switch.

[IMAGE alt='icon' src='relay-mnu.png']

- [Relay Control VI](../../../../vi-lib/slsc-switch/relay-control-vi.html) Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of source channels and configurations channels is void.
- [Get Relay Position VI](../../../../vi-lib/slsc-switch/get-relay-position-vi.html) Returns the relay position for the relay specified in relay name .

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=menus/categories/measurement/slsc-switch/utility-mnu.html language=enus -->
## TOPIC 00003: Utility

- bundle_id: `nislscl-labview-api-ref`
- source_path: `menus/categories/measurement/slsc-switch/utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc-switch/utility-mnu.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the SLSC Switch utility VIs to exercise additional features of a SLSC switch. icon

### Utility

Use the SLSC Switch utility VIs to exercise additional features of a SLSC switch.

[IMAGE alt='icon' src='utility-mnu.png']

- [Reset VI](../../../../vi-lib/slsc-switch/reset-vi.html) Disconnects all created paths and returns the switch module to the state at initialization.
- [Get Relay Names VI](../../../../vi-lib/slsc-switch/get-relay-names-vi.html) Returns a string array of valid relay names for the NI-SLSC Switch module.
- [Get Channel Names VI](../../../../vi-lib/slsc-switch/get-channel-names-vi.html) Returns a string array of valid channel names for the NI-SLSC Switch module.
- [Get Topologies VI](../../../../vi-lib/slsc-switch/get-topologies-vi.html) Enumerates the possible SLSC Switch topologies.

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/can-connect-channels-vi.html language=enus -->
## TOPIC 00004: Can Connect Channels VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/can-connect-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/can-connect-channels-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that a path between channel 1 and channel 2 can be created. If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned. Related Topic Get Path ico

### Can Connect Channels VI

Verifies that a path between **channel 1** and **channel 2** can be created.

If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned.

**Related Topic**

- Get Path

[IMAGE alt='icon' src='can-connect-channels-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. channel 1 — channel 1 specifies one of the channel names of the desired path. Pass the other channel name as channel 2 . channel 2 — channel 2 specifies one of the channel names of the desired path. Pass the other channel name as channel 1 . error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. path capability — path capability indicates whether a path is valid. Path Available (1) The path is possible and available. Path Exists (2) The path is possible, but already exists. Path Unsupported (3) The path is not possible in the specified switch module and topology. Resource In Use (4) The path is possible, but elements of the path are in use by another existing path. You must destroy the other path before creating this one. Source Conflict (5) The path is possible, but connecting the channels will connect two sources. Channel Not Available (6) Channel 1 and channel 2 are configuration channels and are thus unavailable for external connections. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Path Available (1) | The path is possible and available. |
| Path Exists (2) | The path is possible, but already exists. |
| Path Unsupported (3) | The path is not possible in the specified switch module and topology. |
| Resource In Use (4) | The path is possible, but elements of the path are in use by another existing path. You must destroy the other path before creating this one. |
| Source Conflict (5) | The path is possible, but connecting the channels will connect two sources. |
| Channel Not Available (6) | Channel 1 and channel 2 are configuration channels and are thus unavailable for external connections. |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/close-vi.html language=enus -->
## TOPIC 00005: Close VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/close-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/close-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Terminates the NI-SLSC Switch session and all of its attributes and deallocates any memory resources the driver uses. If error in describes an error that occurred before the call to NI-SLSC Switch Close, this VI still attempts to close the session. However, if the attempt fails, this VI returns the

### Close VI

Terminates the NI-SLSC Switch session and all of its attributes and deallocates any memory
 resources the driver uses.

If **error in** describes an error that occurred before the call to NI-SLSC Switch Close, this VI still attempts to close the session. However, if the attempt fails, this VI
 returns the error information that was passed in from **error in**.

Note

SLSC Switch.lvlib:Initialize with Topology

[IMAGE alt='icon' src='close-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/configchannels.html language=enus -->
## TOPIC 00006: Setting Source and Configuration Channels

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/configchannels.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/configchannels.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use NI-SLSC Switch to set the channel type. Set a channel as a source channel to provide additional software protection against unintentional damage to your system. Set a channel as a configuration channel to complete connections supported by the architecture of the switch, but unsupported i

### Setting Source and Configuration Channels

You can use NI-SLSC Switch to set the channel type. Set a channel as a source channel to provide additional software protection against unintentional damage to your system. Set a channel as a configuration channel to complete connections supported by the architecture of the switch, but unsupported in software.

Note

SLSC Switch Relay Control

To edit a channel type, use the SLSC Switch property node.

#### Source Channels

Set a source channel to indicate to the driver that a signal source is connected to the channel. NI-SLSC Switch does not allow two user-defined source channels to be directly or indirectly connected.

#### Configuration Channels

Set a configuration channel to allow NI-SLSC Switch to use the channel for internal path creation. Creating a column-to-column connection will fail in a matrix if a row channel is not set as a configuration channel.

Note

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/connect-channels-multiple-vi.html language=enus -->
## TOPIC 00007: Connect Channels (Multiple) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/connect-channels-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/connect-channels-multiple-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the connections between channels specified in connection list. Specify connections with two endpoints only or the explicit path between two endpoints. NI-SLSC Switch calculates and uses the shortest path between the channels. Refer to Setting Source and Configuration Channels for information

### Connect Channels (Multiple) VI

Creates the connections between channels specified in **connection list**. Specify connections with two endpoints only or the explicit path between two endpoints. NI-SLSC Switch calculates and uses the shortest path between the channels. Refer to [Setting Source and Configuration Channels](/csh?context=nislscsl_slscswitchviref_configchannels) for information about channel usage types. In the event of an error, connecting stops at the point in the list where the error occurred.

[IMAGE alt='icon' src='connect-channels-multiple-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. connection list — connection list specifies a list of connections between channels to make. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Connect Channels VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/connect-channels-single-vi.html language=enus -->
## TOPIC 00008: Connect Channels (Single) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/connect-channels-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/connect-channels-single-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a path between channel 1 and channel 2. NI-SLSC Switch calculates and uses the shortest path between the two channels. Refer to Setting Source and Configuration Channels for information about channel usage types. icon Inputs/Outputs cgenclassrn.png session in session in identifies a particul

### Connect Channels (Single) VI

Creates a path between **channel 1** and **channel 2**. NI-SLSC Switch calculates and uses the
 shortest path between the two channels. Refer to [Setting Source and
 Configuration Channels](/csh?context=nislscsl_slscswitchviref_configchannels) for information about channel usage types.

[IMAGE alt='icon' src='connect-channels-single-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. channel 1 — channel 1 specifies one of the channel names of the desired path. Pass the other channel name as channel 2 . channel 2 — channel 2 specifies one of the channel names of the desired path. Pass the other channel name as channel 1 . error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Note

If a path is unavailable between the two channels, SLSC Switch returns the following
 errors:

| Error | Description |
| --- | --- |
| Explicit Connection Exists | The channels have already been explicitly connected by calling either this VI or the SLSC Switch.lvlib:Set Path. |
| Is Configuration Channel | One of the channels is a configuration channel. Error elaboration contains information about which of the two channels is a configuration channel. |
| Attempt To Connect Sources | Both channels are connected to a source. Error elaboration contains information about the sources connected to channel 1 and channel 2. |
| Cannot Connect To Itself | Channel 1 and channel 2 are identical. |
| Path Not Found | No paths between channel 1 and channel 2 are available. |
| Resource In Use | Channel 1 and/or channel 2 is in use. This error often occurs when one of the channels is set as a configuration channel and is in use or if one of the channels is a common multiplexer channel in use. |

Parent topic:

Connect Channels VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/connect-channels-vi.html language=enus -->
## TOPIC 00009: Connect Channels VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/connect-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/connect-channels-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates connections between channels. Related Topics Connection and Disconnection List Syntax Disconnect Channels icon

### Connect Channels VI

Creates connections between channels.

**Related Topics**

- Connection and Disconnection List Syntax
- Disconnect Channels

[IMAGE alt='icon' src='connect-channels-vi.png']

- [Connect Channels (Single) VI](../../vi-lib/slsc-switch/connect-channels-single-vi.html) Creates a path between channel 1 and channel 2 . NI-SLSC Switch calculates and uses the shortest path between the two channels. Refer to Setting Source and Configuration Channels for information about channel usage types.
- [Connect Channels (Multiple) VI](../../vi-lib/slsc-switch/connect-channels-multiple-vi.html) Creates the connections between channels specified in connection list . Specify connections with two endpoints only or the explicit path between two endpoints. NI-SLSC Switch calculates and uses the shortest path between the channels. Refer to Setting Source and Configuration Channels for information about channel usage types. In the event of an error, connecting stops at the point in the list where the error occurred.

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/connection-disconnection-list.html language=enus -->
## TOPIC 00010: Connection and Disconnection List Syntax

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/connection-disconnection-list.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/connection-disconnection-list.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use connection lists and disconnection lists with Connect Channels (Multiple) and Disconnect Channels (Multiple) to create strings of one or more switching operation. For lists with multiple operations, commas separate each operation. NI-SLSC Switch validates the connection and disconnection

### Connection and Disconnection List Syntax

You can use connection lists and disconnection lists with [Connect Channels (Multiple)](connect-channels-multiple-vi.html) and [Disconnect Channels (Multiple)](disconnect-channels-multiple-vi.html) to create strings of one or more switching operation. For lists with multiple operations, commas separate each operation. NI-SLSC Switch validates the connection and disconnection lists, and aborts execution of the list if errors are returned.

Set a channel as a configuration channel to allow NI-SLSC Switch to use the channel for internal path creation. If a path between two channels includes one or more channels, the intermediate channels should be set as a configuration channel. If multiple intermediate channels exist, and the channel type is set as a configuration channel, NI-SLSC Switch selects the intermediate channel to use.

Note

Switching operations can connect and disconnect channels in one of two ways. Refer to the following table to determine the switching operation.

| Switching Operations | Syntax | Description |
| --- | --- | --- |
| Specify Endpoints | channel1 -> channel2 | NI-SLSC Switch searches for an available path between endpoints to connect or disconnect. The two specified channels must be on the same device, and an available path must exist between them. |
| Specify Explicit Path | [channel1 -> channel2 -> channel3] | You define the endpoints and any intermediate channels of the path.* |
| *The order of operations does not guarantee order of execution. To ensure a specific order, use multiple connection and disconnection lists. |  |  |

Tip

#### Connection and Disconnection List Examples

#### Example 1

If you want to create a connection or disconnection list with switching operations that specify endpoints and explicit paths, separate the switching operations with commas.

Syntax: Operation1, Operation2, Operation3

Example: c0 -> r0, [c1 -> r2 -> c5], r0 -> c4

#### Example 2

If a path exists between channel0, com0, and AB0, you can connect channel0 to AB0 by setting the channel type of com0 as a configuration channel.

Syntax: channel1 -> channel2

Example: channel0 -> AB0

#### Example 3

If you want to connect column 1 and column 5 of a matrix, and use row 2 to complete the connection, you must set the channel type of row 2 to a configuration channel before the connection is made.

Syntax: [channel1 -> channel2 -> channel3]

Example: [c1 -> r2 -> c5]

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/disconnect-all-channels-vi.html language=enus -->
## TOPIC 00011: Disconnect All Channels VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/disconnect-all-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/disconnect-all-channels-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks all known existing paths. If the switch module cannot break all paths, a warning is returned. Relays closed with SLSC Switch.lvlib:Relay Control are also disconnected. Related Topics Disconnect Channels icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Swi

### Disconnect All Channels VI

Breaks all known existing paths.

If the switch module cannot break all paths, a warning is returned.

Relays closed with [SLSC Switch.lvlib:Relay Control](relay-control-vi.html) are also disconnected.

**Related Topics**

- Disconnect Channels

[IMAGE alt='icon' src='disconnect-all-channels-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/disconnect-channels-multiple-vi.html language=enus -->
## TOPIC 00012: Disconnect Channels (Multiple) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/disconnect-channels-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/disconnect-channels-multiple-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks the connections between channels specified in disconnection list. If no connections exist between channels, NI-SLSC Switch returns an error. In the event of an error, the VI stops at the point in the list where the error occurred. icon Inputs/Outputs cgenclassrn.png session in session in iden

### Disconnect Channels (Multiple) VI

Breaks the connections between channels specified in **disconnection list**. If no connections exist between channels, NI-SLSC Switch returns an error. In the event of an error, the VI stops at the point in the list where the error occurred.

[IMAGE alt='icon' src='disconnect-channels-multiple-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. disconnection list — disconnection list specifies a list of connections between channels to break. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Disconnect Channels VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/disconnect-channels-single-vi.html language=enus -->
## TOPIC 00013: Disconnect Channels (Single) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/disconnect-channels-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/disconnect-channels-single-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks the path between two channels created with the Connect Channels VI or the Set Path VI. If no connection exists between the channels, NI-SLSC Switch returns an error. icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Switch session established with SLSC Swi

### Disconnect Channels (Single) VI

Breaks the path between two channels created with the Connect Channels VI or the Set Path VI. If no connection exists between the channels, NI-SLSC Switch returns an error.

[IMAGE alt='icon' src='disconnect-channels-single-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. channel 1 — channel 1 specifies one of the channel names of the path to break. Pass the other channel names for the switch module. channel 2 — channel 2 specifies one of the channel names of the path to break. Pass the other channel name as channel 1 . error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Disconnect Channels VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/disconnect-channels-vi.html language=enus -->
## TOPIC 00014: Disconnect Channels VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/disconnect-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/disconnect-channels-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks connections between channels. Related Topics Connection and Disconnection List Syntax Connect Channels icon

### Disconnect Channels VI

Breaks connections between channels.

**Related Topics**

- Connection and Disconnection List Syntax
- Connect Channels

[IMAGE alt='icon' src='disconnect-channels-vi.png']

- [Disconnect Channels (Single) VI](../../vi-lib/slsc-switch/disconnect-channels-single-vi.html) Breaks the path between two channels created with the Connect Channels VI or the Set Path VI. If no connection exists between the channels, NI-SLSC Switch returns an error.
- [Disconnect Channels (Multiple) VI](../../vi-lib/slsc-switch/disconnect-channels-multiple-vi.html) Breaks the connections between channels specified in disconnection list . If no connections exist between channels, NI-SLSC Switch returns an error. In the event of an error, the VI stops at the point in the list where the error occurred.

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-channel-names-vi.html language=enus -->
## TOPIC 00015: Get Channel Names VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-channel-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-channel-names-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string array of valid channel names for the NI-SLSC Switch module. Related Topics Get Relay Names icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Swit

### Get Channel Names VI

Returns a string array of valid channel names for the NI-SLSC Switch module.

**Related Topics**

- Get Relay Names

[IMAGE alt='icon' src='get-channel-names-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. channel names — channel names specifies the names of the channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-path-vi.html language=enus -->
## TOPIC 00016: Get Path VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-path-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that identifies the explicit path created with Connect Channels VI. Pass this string to Set Path VI to establish the exact same path in future connections. In some cases, multiple paths are available between two channels. When you call SLSC Switch.lvlib:Connect Channels, SLSC Switch

### Get Path VI

Returns a string that identifies the explicit path created with Connect Channels VI. Pass this string to Set Path VI to establish the exact same path in future connections.

In some cases, multiple paths are available between two channels. When you call [SLSC Switch.lvlib:Connect Channels](connect-channels-vi.html), SLSC Switch selects an available path; however, the driver may not always select the same path through the switch module.

This VI only returns those paths explicitly created by [SLSC Switch.lvlib:Connect Channels](connect-channels-vi.html) or [SLSC Switch.lvlib:Set Path](set-path-vi.html). For example, if you connect channels CH1 and CH3,and then channels CH2 and CH3, an explicit path between channels CH1 and CH2 does not exist, and an error is returned.

**Related Topic**

- Set Path

[IMAGE alt='icon' src='get-path-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. channel 1 — channel 1 specifies one of the channel names of the desired path. Pass the other channel name as channel 2 . channel 2 — channel 2 specifies one of the channel names of the desired path. Pass the other channel name as channel 1 . error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. path — path is a string composed of comma-separated paths between channel 1 and channel 2 . The first and last names in the path are the path endpoints. All other channels in the path are configuration channels . Examples of returned paths: ch0->com0, com0->ab0. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-relay-names-vi.html language=enus -->
## TOPIC 00017: Get Relay Names VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-relay-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-relay-names-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string array of valid relay names for the NI-SLSC Switch module. Related Topics Get Channel Names icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Swit

### Get Relay Names VI

Returns a string array of valid relay names for the NI-SLSC Switch module.

**Related Topics**

- Get Channel Names

[IMAGE alt='icon' src='get-relay-names-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. relay names — relay names specifies the names of the relays. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-relay-position-vi.html language=enus -->
## TOPIC 00018: Get Relay Position VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-relay-position-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-relay-position-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relay position for the relay specified in relay name. Related Topics Relay Control icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. cstr

### Get Relay Position VI

Returns the relay position for the relay specified in **relay name**.

**Related Topics**

- Relay Control

[IMAGE alt='icon' src='get-relay-position-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. relay name — relay name is the name of the relay to control. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. position — position indicates the position of the relay. Open (10) Indicates that the relay is open. Closed (11) Indicates that the relay is closed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Open (10) | Indicates that the relay is open. |
| Closed (11) | Indicates that the relay is closed. |

Parent topic:

Relay

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-topologies-device-vi.html language=enus -->
## TOPIC 00019: Get Topologies (Device) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-topologies-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-topologies-device-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumerates the possible SLSC Switch topologies. This is useful when paired with Initialize with Topology (Device). icon Inputs/Outputs cgenclassrntag.png device device specifies the name of the device to access. cerrcodeclst.png error in (no error) error in describes error conditions that occur befo

### Get Topologies (Device) VI

Enumerates the possible SLSC Switch topologies.

This is useful when paired with [Initialize with Topology (Device)](/csh?context=nislscsl_slscswitchviref_slsc_switch_initialize_with_topology_device).

[IMAGE alt='icon' src='get-topologies-device-vi.png']

#### Inputs/Outputs

| device — device specifies the name of the device to access. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. topologies — topologies specifies the topology to use for the switch module specified in device . Refer to your device's documentation for a list of valid topologies. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topologies VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-topologies-simulate-vi.html language=enus -->
## TOPIC 00020: Get Topologies (Simulate) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-topologies-simulate-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-topologies-simulate-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumerates the possible SLSC Switch topologies in the switches json string. This is useful when paired with Initialize with Topology (Override Switches) or Initialize with Topology (Simulate). icon Inputs/Outputs cstr.png switches json switches json specifies the json string used to define the relay

### Get Topologies (Simulate) VI

Enumerates the possible SLSC Switch topologies in the **switches json** string.

This is useful when paired with [Initialize with Topology (Override Switches)](/csh?context=nislscsl_slscswitchviref_slsc_switch_initialize_with_topology_override_switches) or [Initialize with Topology (Simulate)](/csh?context=nislscsl_slscswitchviref_slsc_switch_initialize_with_topology_simulate).

[IMAGE alt='icon' src='get-topologies-simulate-vi.png']

#### Inputs/Outputs

| switches json — switches json specifies the json string used to define the relays and topologies. This is used when a device is offline or does not have the information stored on the module. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. topologies — topologies specifies the topology to use for the switch module specified in device . Refer to your device's documentation for a list of valid topologies. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topologies VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/get-topologies-vi.html language=enus -->
## TOPIC 00021: Get Topologies VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/get-topologies-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/get-topologies-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enumerates the possible SLSC Switch topologies. icon

### Get Topologies VI

Enumerates the possible SLSC Switch topologies.

[IMAGE alt='icon' src='get-topologies-vi.png']

- [Get Topologies (Device) VI](../../vi-lib/slsc-switch/get-topologies-device-vi.html) Enumerates the possible SLSC Switch topologies.
- [Get Topologies (Simulate) VI](../../vi-lib/slsc-switch/get-topologies-simulate-vi.html) Enumerates the possible SLSC Switch topologies in the switches json string.

Parent topic:

Utility

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/initialize-with-topology-device-vi.html language=enus -->
## TOPIC 00022: Initialize with Topology (Device) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/initialize-with-topology-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/initialize-with-topology-device-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module. icon Inputs/Outputs cgenclassrntag.png device device specifies the name of the device to access. cstr.png topology topology specifies the topology to use for th

### Initialize with Topology (Device) VI

Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module.

[IMAGE alt='icon' src='initialize-with-topology-device-vi.png']

#### Inputs/Outputs

| device — device specifies the name of the device to access. topology — topology specifies the topology to use for the switch module specified in device . Refer to your device's documentation for a list of valid topologies. reset device — reset device specifies whether to reset the switch module during initialization. The default value is TRUE (1). TRUE (1) The device will reset. FALSE (0) The device will not reset. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE (1) | The device will reset. |
| FALSE (0) | The device will not reset. |

Parent topic:

Initialize with Topology VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/initialize-with-topology-override-switches-vi.html language=enus -->
## TOPIC 00023: Initialize with Topology (Override Switches) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/initialize-with-topology-override-switches-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/initialize-with-topology-override-switches-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module. This VI allows you to override the topology and relay definitions. The SLSC Switch driver will use the switches json parameter instead of reading the topol

### Initialize with Topology (Override Switches) VI

Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module.

This VI allows you to override the topology and relay definitions. The SLSC Switch driver will use the **switches json** parameter instead of reading the topology and relay definitions stored in the module's NVMEM.

[IMAGE alt='icon' src='initialize-with-topology-override-switches-vi.png']

#### Inputs/Outputs

| switches json — switches json specifies the json string used to define the relays and topologies. This is used when a device is offline or does not have the information stored on the module. device — device specifies the name of the device to access. topology — topology specifies the topology to use for the switch module specified in device . Refer to your device's documentation for a list of valid topologies. reset device — reset device specifies whether to reset the switch module during initialization. The default value is TRUE (1). TRUE (1) The device will reset. FALSE (0) The device will not reset. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE (1) | The device will reset. |
| FALSE (0) | The device will not reset. |

Parent topic:

Initialize with Topology VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/initialize-with-topology-simulate-vi.html language=enus -->
## TOPIC 00024: Initialize with Topology (Simulate) VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/initialize-with-topology-simulate-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/initialize-with-topology-simulate-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module. The switches json parameter specifies the topology and relay definitions to use with the simulated module. You can use this VI to query module properties w

### Initialize with Topology (Simulate) VI

Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module.

The **switches json** parameter specifies the topology and relay definitions to use with the simulated module.

You can use this VI to query module properties without hardware, such as calling [Get Channel Names](/csh?context=nislscsl_slscswitchviref_slsc_switch_get_channel_names) and [Can Connect Channels](/csh?context=nislscsl_slscswitchviref_slsc_switch_can_connect_channels).

[IMAGE alt='icon' src='initialize-with-topology-simulate-vi.png']

#### Inputs/Outputs

| switches json — switches json specifies the json string used to define the relays and topologies. This is used when a device is offline or does not have the information stored on the module. topology — topology specifies the topology to use for the switch module specified in device . Refer to your device's documentation for a list of valid topologies. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Initialize with Topology VI

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/initialize-with-topology-vi.html language=enus -->
## TOPIC 00025: Initialize with Topology VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/initialize-with-topology-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/initialize-with-topology-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module. icon

### Initialize with Topology VI

Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module.

[IMAGE alt='icon' src='initialize-with-topology-vi.png']

- [Initialize with Topology (Device) VI](../../vi-lib/slsc-switch/initialize-with-topology-device-vi.html) Returns a session handle used to identify the SLSC Switch module in all subsequent driver calls and sets the topology of the switch module.
- [Initialize with Topology (Simulate) VI](../../vi-lib/slsc-switch/initialize-with-topology-simulate-vi.html) Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module.
- [Initialize with Topology (Override Switches) VI](../../vi-lib/slsc-switch/initialize-with-topology-override-switches-vi.html) Returns a session handle used to identify the SLSC module in all subsequent SLSC Switch driver calls and sets the topology of the switch module.

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/relay-control-vi.html language=enus -->
## TOPIC 00026: Relay Control VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/relay-control-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/relay-control-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of source channels and configurations channels is void. Refer to Devices to determine if the switch module supports individual relay control. Related Topics Get Relay Posi

### Relay Control VI

Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of [source channels](/csh?context=nislscsl_slscswitchviref_configchannels) and [configurations channels](/csh?context=nislscsl_slscswitchviref_configchannels) is void.

Refer to Devices to determine if the switch module supports individual relay control.

**Related Topics**

- Get Relay Position

[IMAGE alt='icon' src='relay-control-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. relay names — relay names is the name of the relay or set of relays to control. You can supply a single relay name or comma-delimited list of relay names to control these relays. relay action (Close Relay) — relay action specifies whether to open or close the relay. The default value is Close Relay (21). Open Relay (20) Opens the relay. Close Relay (21) Closes the relay. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Open Relay (20) | Opens the relay. |
| Close Relay (21) | Closes the relay. |

Parent topic:

Relay

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/reset-vi.html language=enus -->
## TOPIC 00027: Reset VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/reset-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects all created paths and returns the switch module to the state at initialization. Related Topics Disconnect All Channels icon Inputs/Outputs cgenclassrn.png session in session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and use

### Reset VI

Disconnects all created paths and returns the switch module to the state at initialization.

**Related Topics**

- Disconnect All Channels

[IMAGE alt='icon' src='reset-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/set-path-vi.html language=enus -->
## TOPIC 00028: Set Path VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/set-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/set-path-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects two channels by specifying an explicit path in the path parameter. This VI is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use Connect Channels VI. To obtain the exact path for a given connection, use Get Path VI.

### Set Path VI

Connects two channels by specifying an explicit path in the **path** parameter. This VI is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use Connect Channels VI.

To obtain the exact path for a given connection, use Get Path VI.

**Related Topics**

- Get Path

[IMAGE alt='icon' src='set-path-vi.png']

#### Inputs/Outputs

| session in — session in identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. path — path is a string composed of comma-separated paths between channel 1 and channel 2 . The first and last names in the path are the path endpoints. All other channels in the path are configuration channels . Example of a valid path list string: ch0->com0, com0->ab0. In this example, com0 is a configuration channel. Obtain the path list for a previously created path with the SLSC Switch.lvlib:Get Path . error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out identifies a particular SLSC Switch session established with SLSC Switch.lvlib:Initialize with Topology and used for this NI-SLSC Switch call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/slsc-switch-property-node-vi.html language=enus -->
## TOPIC 00029: SLSC Switch Property Node VI

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/slsc-switch-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/slsc-switch-property-node-vi.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) and/or sets (writes) properties of a reference. Use the property node to get or set properties and methods on local or remote application instances, VIs, and objects. You also can use the Property Node to access the private data of a LabVIEW class. icon Inputs/Outputs cgenclassrn.png re

### SLSC Switch Property Node VI

Gets (reads) and/or sets (writes) properties of a reference. Use the property node to get or set properties and methods on local or remote application instances, VIs, and objects. You also can use the Property Node to access the private data of a LabVIEW class.

[IMAGE alt='icon' src='slsc-switch-property-node-vi.png']

#### Inputs/Outputs

| reference — reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node. You also can wire a LabVIEW class to the reference input to access the private data of the LabVIEW class. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reference out — reference out returns reference unchanged. error out — error out contains error information. This output provides standard error out functionality. Property — property 1..n are examples of properties you want to get (read). |
| --- |

Parent topic:

NI-SLSC Switch

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00030: Using the Standard Functionality for error in Parameters

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/standard-functionality-for-error-in-parameters.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=nislscl-labview-api-ref path=vi-lib/slsc-switch/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00031: Using the Standard Functionality for error out Parameters

- bundle_id: `nislscl-labview-api-ref`
- source_path: `vi-lib/slsc-switch/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/nislscl-labview-api-ref/raw/resource/enus/vi-lib/slsc-switch/standard-functionality-for-error-out-parameters.html
- document_id: `nislscl-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
