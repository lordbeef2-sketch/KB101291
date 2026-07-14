# NI DOCUMENT BUNDLE: ni-switch-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-switch-labview-api-ref start=1 end=53 -->
<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/dir-mnu.html language=enus -->
## TOPIC 00001: NI-SWITCH

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/dir-mnu.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on the NI-SWITCH palette to build the block diagram. icon

### NI-SWITCH

Use the VIs on the NI-SWITCH palette to build the block diagram.

[IMAGE alt='icon' src='dir-mnu.png']

- [niSwitch Initialize With Topology VI](../../instr-lib/niswitch/niswitch-llb/niswitch-initialize-with-topology-vi.html) Returns a session handle used to identify the switch module in all subsequent instrument driver calls and sets the topology of the switch module.
- [niSwitch Close VI](../../instr-lib/niswitch/niswitch-llb/niswitch-close-vi.html) Terminates the NI-SWITCH session and all of its attributes and deallocates any memory resources the driver uses.
- [niSwitch Connect Channels VI](../../instr-lib/niswitch/niswitch-llb/niswitch-connect-channels-vi.html) Creates connections between channels.
- [niSwitch Disconnect Channels VI](../../instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-vi.html) Breaks connections between channels.
- [niSwitch Wait For Debounce VI](../../instr-lib/niswitch/niswitch-llb/niswitch-wait-for-debounce-vi.html) Pauses until all created paths have settled. Call this VI before the niSwitch Get Relay Count VI to ensure an accurate relay count.
- [niSwitch Set Path VI](../../instr-lib/niswitch/niswitch-llb/niswitch-set-path-vi.html) Connects two channels by specifying an explicit path in the path list parameter. This VI is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use the niSwitch Connect Channels VI .
- [niSwitch Can Connect Channels VI](../../instr-lib/niswitch/niswitch-llb/niswitch-can-connect-channels-vi.html) Verifies that a path between channel 1 and channel 2 can be created.
- [niSwitch Disconnect All Channels VI](../../instr-lib/niswitch/niswitch-llb/niswitch-disconnect-all-channels-vi.html) Breaks all existing paths.
- [niSwitch Switch Is Debounced VI](../../instr-lib/niswitch/niswitch-llb/niswitch-switch-is-debounced-vi.html) Indicates whether all created paths have settled by returning the value of the Is Debounced property.
- [niSwitch Get Path VI](../../instr-lib/niswitch/niswitch-llb/niswitch-get-path-vi.html) Returns a string that identifies the explicit path created with the niSwitch Connect Channels VI . Pass this string to the niSwitch Set Path VI to establish the exact same path in future connections.
- [niSwitch Property Node VI](../../instr-lib/niswitch/niswitch-llb/niswitch-property-node-vi.html) Gets (reads) and/or sets (writes) properties of the NI-SWITCH driver. For a complete list of NI-SWITCH properties, refer to NI-SWITCH Properties .
- [Scan](../../instr-lib/niswitch/scan-mnu.html) Use the NI-SWITCH scan VIs to configure a scan of an NI switch.
- [Relay](../../instr-lib/niswitch/relay-mnu.html) Use the NI-SWITCH relay VIs to control and query individual relays of an NI switch.
- [Utility](../../instr-lib/niswitch/utility-mnu.html) Use the NI-SWITCH utility VIs to exercise additional features of an NI switch.

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-abort-scan-vi.html language=enus -->
## TOPIC 00002: niSwitch Abort Scan VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-abort-scan-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-abort-scan-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the scan in progress. The switch module returns to the state it was in before the scan was initiated. Use the niSwitch Initiate Scan VI to initiate an aborted scan. If the switch module is not scanning, a No Scan In Progress error is returned. If error in describes an error that had occurred

### niSwitch Abort Scan VI

Aborts the scan in progress. The switch module returns to the state it was in before the scan was initiated. Use the [niSwitch Initiate Scan VI](/csh?topicname=niswitch-initiate-scan-vi.html) to initiate an aborted scan.

If the switch module is not scanning, a No Scan In Progress error is returned.

If **error in** describes an error that had occurred before calling this VI, the VI still attempts to abort the scan. However, if the attempt fails, the VI returns the error information that was passed in from the **error in** parameter.

**Related Topics**

- niSwitch Properties
- Scanning
- Writing a Software Trigger Scanning Program

[IMAGE alt='icon' src='niswitch-abort-scan-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scan

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-can-connect-channels-vi.html language=enus -->
## TOPIC 00003: niSwitch Can Connect Channels VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-can-connect-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-can-connect-channels-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that a path between channel 1 and channel 2 can be created. If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned. Related Topic niSwitch Get

### niSwitch Can Connect Channels VI

Verifies that a path between **channel 1** and **channel 2** can be created.

If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned.

**Related Topic**

- niSwitch Get Path

[IMAGE alt='icon' src='niswitch-can-connect-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. channel 1 — channel 1 specifies one of the channel names of the desired path. Pass the other channel name as channel 2. Refer to Devices for valid channel names for the switch module. Examples of valid channel names are ch0, com0, ab0, r1, c2, and cjtemp. channel 2 — channel 2 specifies one of the channel names of the desired path. Pass the other channel name as channel 1. Refer to Devices for valid channel names for the switch module. Examples of valid channel names are ch0, com0, ab0, r1, c2, and cjtemp error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. path capability — path capability indicates whether a path is valid. Path Available (1) The path is possible and available. Path Exists (2) The path is possible, but already exists. Path Unsupported (3) The path is not possible in the specified switch module and topology. Resource In Use (4) The path is possible, but elements of the path are in use by another existing path. You must destroy the other path before creating this one. Source Conflict (5) The path is possible, but connecting the channels will connect two sources. Channel Not Available (6) Channel 1 and channel 2 are configuration channels and are thus unavailable for external connections. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Path Available (1) | The path is possible and available. |
| Path Exists (2) | The path is possible, but already exists. |
| Path Unsupported (3) | The path is not possible in the specified switch module and topology. |
| Resource In Use (4) | The path is possible, but elements of the path are in use by another existing path. You must destroy the other path before creating this one. |
| Source Conflict (5) | The path is possible, but connecting the channels will connect two sources. |
| Channel Not Available (6) | Channel 1 and channel 2 are configuration channels and are thus unavailable for external connections. |

Parent topic:

NI-SWITCH

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-clear-interchange-warnings-vi.html language=enus -->
## TOPIC 00004: niSwitch Clear Interchange Warnings VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-clear-interchange-warnings-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-clear-interchange-warnings-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. Related Topics niSwitch Get Next Interchange Warning niSwitch Reset Interchange Check icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI

### niSwitch Clear Interchange Warnings VI

Clears the list of current interchange warnings.

**Related Topics**

- niSwitch Get Next Interchange Warning
- niSwitch Reset Interchange Check

[IMAGE alt='icon' src='niswitch-clear-interchange-warnings-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so, ensure that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the instrument state depends on the configuration from a previously executed test module. Therefore, if you execute the test modules in a different order, the behavior of the instrument and therefore the entire test module is likely to change. This behavior change is generally instrument specific and represents an interchangeability problem.

You can use the [niSwitch Reset Interchange Check VI](niswitch-reset-interchange-check-vi.html) to test for such cases. After you call the [niSwitch Reset Interchange Check VI](niswitch-reset-interchange-check-vi.html), the interchangeability checking algorithms in the specific driver ignore all previous configuration operations. By calling the [niSwitch Reset Interchange Check VI](niswitch-reset-interchange-check-vi.html) at the beginning of a test module, you can determine whether the test module has dependencies on the operation of previously executed test modules.

To guarantee that the [niSwitch Get Next Interchange Warning VI](niswitch-get-next-interchange-warning-vi.html) only returns those interchangeability warnings generated after calling the [niSwitch Reset Interchange Check VI](niswitch-reset-interchange-check-vi.html), clear the list of interchangeability warnings by repeatedly calling the [niSwitch Get Next Interchange Warning VI](niswitch-get-next-interchange-warning-vi.html) until no interchangeability warnings are returned. If you are not interested in the content of those warnings, call the [niSwitch Clear Interchange Warnings VI](niswitch-clear-interchange-warnings-vi.html).

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-convert-thermocouple-reading-vi.html language=enus -->
## TOPIC 00005: niSwitch Convert Thermocouple Reading VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-convert-thermocouple-reading-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-convert-thermocouple-reading-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a voltage reading from a thermocouple into a temperature value. Related Topics niSwitch Temperature to Volts niSwitch Volts to Temperature icon Inputs/Outputs cu16.png Temperature Units (C) Temperature Units is the units of temperature the VI outputs. c1dsgl.png Thermocouple Voltage Thermoc

### niSwitch Convert Thermocouple Reading VI

Converts a voltage reading from a thermocouple into a temperature value.

**Related Topics**

- niSwitch Temperature to Volts
- niSwitch Volts to Temperature

[IMAGE alt='icon' src='niswitch-convert-thermocouple-reading-vi.png']

#### Inputs/Outputs

| Temperature Units (C) — Temperature Units is the units of temperature the VI outputs. Thermocouple Voltage — Thermocouple Voltage is the voltage read from the thermocouple. CJC Voltage — CJC Voltage is the cold-junction compensation reference voltage. ThermocoupleType — ThermocoupleType can be B, E, J, K, R, S, T, or N. Temperature — Temperature is the return temperature value in the units specified in Temperature Units. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-disable-vi.html language=enus -->
## TOPIC 00006: niSwitch Disable VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-disable-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-disable-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Places the switch module in a quiescent state where it has minimal or no impact on the system to which it is connected. This VI disconnects all channels, and any scan in progress is aborted. If error in describes an error that had occurred before calling niSwitch Disable, this VI still attempts to d

### niSwitch Disable VI

Places the switch module in a quiescent state where it has minimal or no impact on the system to which it is connected. This VI disconnects all channels, and any scan in progress is aborted.

If **error in** describes an error that had occurred before calling niSwitch Disable, this VI still attempts to disable the switch. However, if the attempt fails, this VI returns the error information that was passed in from **error in**.

**Related Topics**

- niSwitch Close
- niSwitch Disconnect All Channels

[IMAGE alt='icon' src='niswitch-disable-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-disconnect-all-channels-vi.html language=enus -->
## TOPIC 00007: niSwitch Disconnect All Channels VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-disconnect-all-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-disconnect-all-channels-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks all existing paths. If the switch module cannot break all paths, a warning is returned. If an error in parameter describes an error that occurred before the call to this VI, NI-SWITCH still attempts to break all connections and returns the error information that was passed in from error in. R

### niSwitch Disconnect All Channels VI

Breaks all existing paths.

If the switch module cannot break all paths, a warning is returned. If an **error in** parameter describes an error that occurred before the call to this VI, NI-SWITCH still attempts to break all connections and returns the error information that was passed in from **error in**.

Relays closed with the [niSwitch Relay Control VI](niswitch-relay-control-vi.html) are also disconnected.

**Related Topics**

- Immediate Operations
- niSwitch Disconnect Channels

[IMAGE alt='icon' src='niswitch-disconnect-all-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SWITCH

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-multiple-vi.html language=enus -->
## TOPIC 00008: niSwitch Disconnect Channels (Multiple) VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-multiple-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks the connections between channels specified in disconnection list. If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the VI stops at the point in the list where the error occurred. icon Inputs/Outputs civrn.png instrument handle instrument handle i

### niSwitch Disconnect Channels (Multiple) VI

Breaks the connections between channels specified in **disconnection list**. If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the VI stops at the point in the list where the error occurred.

[IMAGE alt='icon' src='niswitch-disconnect-channels-multiple-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. disconnection list — disconnection list specifies a list of connections between channels to break. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niSwitch Disconnect Channels VI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-single-vi.html language=enus -->
## TOPIC 00009: niSwitch Disconnect Channels (Single) VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-single-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks the path between two channels created with the niSwitch Connect Channels VI or the niSwitch Set Path VI. If no connection exists between the channels, NI-SWITCH returns an error. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular NI-SWITCH session establ

### niSwitch Disconnect Channels (Single) VI

Breaks the path between two channels created with the [niSwitch Connect Channels VI](/csh?topicname=niswitch-connect-channels-vi.html) or the [niSwitch Set Path VI](/csh?topicname=niswitch-set-path-vi.html). If no connection exists between the channels, NI-SWITCH returns an error.

[IMAGE alt='icon' src='niswitch-disconnect-channels-single-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. channel 1 — channel 1 specifies one of the channel names of the path to break. Pass the other channel names for the switch module. Examples of valid channel names are ch0, com0, ab0, r1, c2, and cjtemp channel 2 — channel 2 specifies one of the channel names of the path to break. Pass the other channel name as channel 1. Refer to Devices for valid channel names for the switch module. Examples of valid channel names are ch0, com0, ab0, r1, c2, and cjtemp error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niSwitch Disconnect Channels VI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-vi.html language=enus -->
## TOPIC 00010: niSwitch Disconnect Channels VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks connections between channels. Related Topics Connection and Disconnection List Syntax niSwitch Connect Channels Immediate Operations icon

### niSwitch Disconnect Channels VI

Breaks connections between channels.

**Related Topics**

- Connection and Disconnection List Syntax
- niSwitch Connect Channels
- Immediate Operations

[IMAGE alt='icon' src='niswitch-disconnect-channels-vi.png']

- [niSwitch Disconnect Channels (Single) VI](../../../instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-single-vi.html) Breaks the path between two channels created with the niSwitch Connect Channels VI or the niSwitch Set Path VI . If no connection exists between the channels, NI-SWITCH returns an error.
- [niSwitch Disconnect Channels (Multiple) VI](../../../instr-lib/niswitch/niswitch-llb/niswitch-disconnect-channels-multiple-vi.html) Breaks the connections between channels specified in disconnection list . If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the VI stops at the point in the list where the error occurred.

Parent topic:

NI-SWITCH

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-error-message-vi.html language=enus -->
## TOPIC 00011: niSwitch Error Message VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-error-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-error-message-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an error code returned by NI-SWITCH into a user-readable string. Generally this information is supplied in error out of any NI-SWITCH VI. Use this VI for a static lookup of an error code description. Related Topics Error and Status Codes icon Inputs/Outputs civrn.png instrument handle instr

### niSwitch Error Message VI

Converts an error code returned by NI-SWITCH into a user-readable string. Generally this information is supplied in **error out** of any NI-SWITCH VI. Use this VI for a static lookup of an error code description.

**Related Topics**

- Error and Status Codes

[IMAGE alt='icon' src='niswitch-error-message-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error code (0) — error code is the status code returned by any NI-SWITCH VI. Default value: 0 error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error message — error message is the error information formatted into a string. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-get-channel-name-vi.html language=enus -->
## TOPIC 00012: niSwitch Get Channel Name VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-get-channel-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-get-channel-name-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the channel string that is in the channel table at the specified index. Use this VI in a For Loop to get a complete list of valid channel names for the switch module. Use the Channel Count property to determine the number of channels. Related Topics niSwitch Get Relay Name icon Inputs/Output

### niSwitch Get Channel Name VI

Returns the **channel string** that is in the channel table at the specified index.

Use this VI in a For Loop to get a complete list of valid channel names for the switch module. Use the [Channel Count](/csh?context=niswitch_switchpropref_pniswitch_channelcount) property to determine the number of channels.

**Related Topics**

- niSwitch Get Relay Name

[IMAGE alt='icon' src='niswitch-get-channel-name-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. index (1) — index is a 1-based index into the channel table. The default value is 1. The maximum value is equal to the value of the Channel Count property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. channel string — channel string returns the channel string that is in the channel table at index. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-get-next-coercion-record-vi.html language=enus -->
## TOPIC 00013: niSwitch Get Next Coercion Record VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-get-next-coercion-record-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-get-next-coercion-record-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the coercion information associated with the IVI session, and clears the oldest instance in which NI-SWITCH coerced a value you specified. If you set the Record Value Coercions property to TRUE, NI-SWITCH keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to instru

### niSwitch Get Next Coercion Record VI

Returns the coercion information associated with the IVI session, and clears the oldest instance in which NI-SWITCH coerced a value you specified.

If you set the [Record Value Coercions](/csh?context=niswitch_switchpropref_pniswitch_recordvaluecoercions) property to TRUE, NI-SWITCH keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to instrument driver VIs. You use this VI to retrieve information from that list.

The VI returns an empty string if no coercion records remain for the session.

**Related Topics**

- Record Value Coercions

[IMAGE alt='icon' src='niswitch-get-next-coercion-record-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. coercion record — coercion record returns the next coercion record for the IVI session. If there are no coercion records remaining for the session, the VI returns an empty string. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-get-next-interchange-warning-vi.html language=enus -->
## TOPIC 00014: niSwitch Get Next Interchange Warning VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-get-next-interchange-warning-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-get-next-interchange-warning-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the interchangeability warnings associated with the IVI session. This VI retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause differe

### niSwitch Get Next Interchange Warning VI

Returns the interchangeability warnings associated with the IVI session. This VI retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.

NI-SWITCH performs interchangeability checking when the [Interchange Check](/csh?context=niswitch_switchpropref_pniswitch_interchangecheck) property is set to TRUE.

The VI returns an empty string for interchange warning if no interchangeability warnings remain for the session.

In general, NI-SWITCH generates interchangeability warnings when a property that affects the behavior of the switch is in a state that you did not specify.

**Related Topics**

- niSwitch Clear Interchange Warnings
- niSwitch Reset Interchange Check

[IMAGE alt='icon' src='niswitch-get-next-interchange-warning-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. interchange warning — interchange warning is the next interchange warning for the IVI session. If there are no interchangeability warnings remaining for the session, interchange warning is an empty string. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-get-relay-count-vi.html language=enus -->
## TOPIC 00015: niSwitch Get Relay Count VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-get-relay-count-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-get-relay-count-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of times the relay has changed from Closed to Open. Relay count is useful for tracking relay life and use. Call the niSwitch Wait For Debounce VI before this VI to ensure an accurate count. Refer to Relay Count to determine if the switch module supports relay counting. Related Top

### niSwitch Get Relay Count VI

Returns the number of times the relay has changed from Closed to Open. Relay count is useful for tracking relay life and use. Call the [niSwitch Wait For Debounce VI](/csh?topicname=niswitch-wait-for-debounce-vi.html) before this VI to ensure an accurate count.

Refer to [Relay Count](/csh?context=ni-switch_switch_relay_count) to determine if the switch module supports relay counting.

**Related Topic**

- niSwitch Get Relay Name

[IMAGE alt='icon' src='niswitch-get-relay-count-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. relay name — relay name specifies the name of the relay. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. count — count is the number of relay cycles. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Relay

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-get-relay-position-vi.html language=enus -->
## TOPIC 00016: niSwitch Get Relay Position VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-get-relay-position-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-get-relay-position-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relay position for the relay specified in relay name. Refer to Devices to determine if the switch module supports individual relay control. Related Topics niSwitch Relay Control Relay Forms icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular NI-SWITC

### niSwitch Get Relay Position VI

Returns the relay position for the relay specified in **relay name**.

Refer to [Devices](/csh?context=ni-switch_switch_devices) to determine if the switch module supports [individual relay control](/csh?context=ni-switch_switch_immediate).

**Related Topics**

- niSwitch Relay Control
- Relay Forms

[IMAGE alt='icon' src='niswitch-get-relay-position-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. relay name — relay name specifies the name of the relay. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. position — position indicates the position of the relay. Open (10) Indicates that the relay is open. Closed (11) Indicates that the relay is closed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Open (10) | Indicates that the relay is open. |
| Closed (11) | Indicates that the relay is closed. |

Parent topic:

Relay

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-route-scan-advanced-output-vi.html language=enus -->
## TOPIC 00017: niSwitch Route Scan Advanced Output VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-route-scan-advanced-output-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-route-scan-advanced-output-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes the scan advanced output trigger from a trigger bus line (TTLx) to the front or rear connector. Use this VI when handshaking with a switch module that is not directly cabled to the controller. In this module's session, set the scan advanced output bus line to a trigger bus line. In the cabled

### niSwitch Route Scan Advanced Output VI

Routes the scan advanced output trigger from a trigger bus line (TTL*x*) to the front or rear connector.

Use this VI when [handshaking](/csh?context=ni-switch_switch_handshakingg) with a switch module that is not directly cabled to the controller. In this module's session, set the **scan advanced output** bus line to a trigger bus line. In the cabled module's session, use this VI to route from the trigger bus line to the front or rear connector of the cabled module.

If this VI is used to route scan advanced from a TTL line, specify the TTL line as the **scan advanced output** destination in the [niSwitch Configure Scan Trigger VI](niswitch-configure-scan-trigger-vi.html).

**Related Topics**

- Scanning

[IMAGE alt='icon' src='niswitch-route-scan-advanced-output-vi.png']

#### Inputs/Outputs

| invert (False) — invert inverts the input trigger signal from rising to falling and falling to rising. The default value is FALSE (0). TRUE (1) Inverts the input trigger signal from falling to rising. FALSE (0) Inverts the input trigger signal from rising to falling. instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. scan advanced output connector — scan advanced output connector is the Scan Advanced Output destination. Valid locations are the front and rear connectors. scan advanced output bus line — scan advanced output bus line is the trigger line to route the scan advanced output trigger from the front or rear connector. Select None (default) to break an existing route. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE (1) | Inverts the input trigger signal from falling to rising. |
| FALSE (0) | Inverts the input trigger signal from rising to falling. |

Parent topic:

Scan

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-route-trigger-input-vi.html language=enus -->
## TOPIC 00018: niSwitch Route Trigger Input VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-route-trigger-input-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-route-trigger-input-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes the input trigger from the front or rear connector to a trigger bus line (TTLx). To disconnect the route, call this VI again and select None for the trigger input bus line parameter. This VI should be used when scanning a module in a different NI-SWITCH session that is not directly cabled to

### niSwitch Route Trigger Input VI

Routes the input trigger from the front or rear connector to a trigger bus line (TTL*x*). To disconnect the route, call this VI again and select **None** for the **trigger input bus line** parameter.

This VI should be used when scanning a module in a different NI-SWITCH session that is not directly cabled to the trigger source ([multimodule scanning](/csh?context=ni-switch_switch_scanning_multiple_mod) operations).

If this VI is used to route a trigger to a TTL line, specify the TTL line as the **trigger input** in the [niSwitch Configure Scan Trigger VI](niswitch-configure-scan-trigger-vi.html).

**Related Topics**

- niSwitch Configure Scan Trigger
- Scanning

[IMAGE alt='icon' src='niswitch-route-trigger-input-vi.png']

#### Inputs/Outputs

| invert (False) — invert inverts the input trigger signal from rising to falling and falling to rising. The default value is FALSE (0). TRUE (1) Inverts the input trigger signal from falling to rising. FALSE (0) Inverts the input trigger signal from rising to falling. instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. trigger input connector — trigger input connector specifies the location of the input trigger source on the switch module. Valid locations are the front and rear connectors. The default Value is Front Connector. trigger input bus line — trigger input bus line specifies the trigger line to route the input trigger. Select None to break an existing route. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE (1) | Inverts the input trigger signal from falling to rising. |
| FALSE (0) | Inverts the input trigger signal from rising to falling. |

Parent topic:

Scan

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-self-test-vi.html language=enus -->
## TOPIC 00019: niSwitch Self-Test VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-self-test-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that NI-SWITCH can communicate with the switch module. Related Topics Debugging with the Switch Soft Front Panel icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitc

### niSwitch Self-Test VI

Verifies that NI-SWITCH can communicate with the switch module.

**Related Topics**

- Debugging with the Switch Soft Front Panel

[IMAGE alt='icon' src='niswitch-self-test-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. self-test result — self-test result returns a value from the switch self-test. 0 equals success and 1 equals failure. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. error out — error out contains error information. This output provides standard error out functionality. self-test message — self-test message returns a response string from the switch self-test. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-llb/niswitch-switch-is-scanning-vi.html language=enus -->
## TOPIC 00020: niSwitch Switch Is Scanning VI

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-llb/niswitch-switch-is-scanning-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-llb/niswitch-switch-is-scanning-vi.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the status of the scan. Related Topic Scanning icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. cerr

### niSwitch Switch Is Scanning VI

Indicates the status of the scan.

**Related Topic**

- Scanning

[IMAGE alt='icon' src='niswitch-switch-is-scanning-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology VI, the niSwitch Initialize With Options VI, or the niSwitch Initialize VI and used for all subsequent NI-SWITCH calls. is scanning — is scanning indicates whether the switch module is scanning. The driver returns the value of the Is Scanning property. The default value is FALSE (0). TRUE (1) The switch module is scanning. FALSE (0) The switch module is idle. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE (1) | The switch module is scanning. |
| FALSE (0) | The switch module is idle. |

Parent topic:

Scan

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-bandwidth.html language=enus -->
## TOPIC 00021: Module Characteristics:Bandwidth

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-bandwidth.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth for the channel in hertz. Related topics Bandwidth and Insertion Loss niSwitch Properties RF Switching Considerations Remarks The following table lists the characteristics of this property. Short Name Bandwidth Data type cdbl.png Permissions Read Only Channel-based Yes Resettab

### Module Characteristics:Bandwidth

Returns the bandwidth for the channel in hertz.

**Related topics**

- Bandwidth and Insertion Loss
- niSwitch Properties
- RF Switching Considerations

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-cabledmoduletriggerbus.html language=enus -->
## TOPIC 00022: Obsolete Attributes:Cabled Module Trigger Bus

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-cabledmoduletriggerbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-cabledmoduletriggerbus.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead. Remarks The following table lists the characteristics of this property. Short Name Cabled Module Trigger Bus Data type ci32.png Permissions Read/Write Channel-b

### Obsolete Attributes:Cabled Module Trigger Bus

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the [niSwitch Route Trigger Input](/csh?context=niswitch_switchviref_niswitch_route_trigger_input) VI instead.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cabled Module Trigger Bus |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-continuousscan.html language=enus -->
## TOPIC 00023: Scanning Configuration:Continuous Scan

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-continuousscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-continuousscan.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to continuously scan through a scan list. Set the property to FALSE to stop scanning after one pass through the scan list. Set this property to TRUE to loop continuously through the scan list. If you set the property to TRUE, the niSwitch Wait For Scan To Complete VI times out, and

### Scanning Configuration:Continuous Scan

Specifies whether to continuously scan through a scan list. Set the property to FALSE to stop scanning after one pass through the scan list. Set this property to TRUE to loop continuously through the scan list.

If you set the property to TRUE, the [niSwitch Wait For Scan To Complete](/csh?context=niswitch_switchviref_niswitch_wait_for_scan_to_complete) VI times out, and you must call the [niSwitch Abort Scan](/csh?context=niswitch_switchviref_niswitch_abort_scan) VI to stop the scan.

**Related topics**

- niSwitch Properties
- Scanning

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Continuous Scan |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-description.html language=enus -->
## TOPIC 00024: Inherent IVI Attributes:Driver Identification:Description

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-description.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a brief description of the instrument driver. Related topics niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Description

Contains a brief description of the instrument driver.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Description |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driverprefix.html language=enus -->
## TOPIC 00025: Inherent IVI Attributes:Driver Identification:Driver Prefix

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driverprefix.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the prefix for all of the instrument driver VIs. Related topics niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Driver Prefix Data type cstr.png Permissions Read Only Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Driver Prefix

Contains the prefix for all of the instrument driver VIs.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Prefix |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driversetup.html language=enus -->
## TOPIC 00026: Inherent IVI Attributes:Advanced Session Information:Driver Setup

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-driversetup.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the Driver Setup string that you specified when initializing the instrument driver. In some cases, you must specify instrument driver options at initialization time—for example, when specifying a particular instrument model from among a family of instruments that the instrument driver suppo

### Inherent IVI Attributes:Advanced Session Information:Driver Setup

Contains the Driver Setup string that you specified when initializing the instrument driver.

In some cases, you must specify instrument driver options at initialization time—for example, when specifying a particular instrument model from among a family of instruments that the instrument driver supports. This is useful when using simulation.

You can specify instrument driver-specific options through the DriverSetup keyword in the **option string** parameter of the [niSwitch Initialize With Options](/csh?context=niswitch_switchviref_niswitch_initialize_with_options) VI, or through the IVI Configuration Utility. If you did not specify a Driver Setup string, this property returns an empty string.

**Related topics**

- niSwitch Initialize With Options
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Setup |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-drivervendor.html language=enus -->
## TOPIC 00027: Inherent IVI Attributes:Driver Identification:Driver Vendor

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-drivervendor.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the name of the vendor that supplies the instrument driver. Related topics niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Driver Vendor Data type cstr.png Permissions Read Only Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Driver Vendor

Contains the name of the vendor that supplies the instrument driver.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Vendor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-firmwarerevision.html language=enus -->
## TOPIC 00028: Inherent IVI Attributes:Instrument Identification:Firmware Revision

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-firmwarerevision.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the firmware revision information for the instrument currently in use. Related topics niSwitch Properties niSwitch Revision Query Remarks The following table lists the characteristics of this property. Short Name Firmware Revision Data type cstr.png Permissions Read Only Channel-based No Re

### Inherent IVI Attributes:Instrument Identification:Firmware Revision

Contains the firmware revision information for the instrument currently in use.

**Related topics**

- niSwitch Properties
- niSwitch Revision Query

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Firmware Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-handshakinginitiation.html language=enus -->
## TOPIC 00029: Scanning Configuration:Handshaking Initiation

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-handshakinginitiation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-handshakinginitiation.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to start handshaking with a measurement device. Related topics Handshaking niSwitch Properties Scanning Remarks The following table lists the characteristics of this property. Short Name Handshaking Initiation Data type ci32.png Permissions Read/Write Channel-based No Resettable No Swi

### Scanning Configuration:Handshaking Initiation

Specifies how to start handshaking with a measurement device.

**Related topics**

- Handshaking
- niSwitch Properties
- Scanning

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Handshaking Initiation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

| Switch_Initiated | 1 | The niSwitch Initiate Scan VI returns immediately after beginning scan list execution. It is assumed that the measurement device has already been configured and is waiting for the scanner advanced signal. The measurement should be configured to first wait for a trigger, then take a measurement. Thus, the first scanner advanced output signal of the switch module initiates handshaking. |
| --- | --- | --- |
| Measurement_Device_Initiated | 0 | The niSwitch Initiate Scan VI does not return until the switch hardware is waiting for a trigger input. This ensures that if you initiate the measurement device after calling the niSwitch Initiate Scan VI , the switch is sure to receive the first measurement complete (MC) signal sent by the measurement device. The measurement device should be configured to first take a measurement, send MC, then wait for scanner advanced output signal. Thus, the first MC of the measurement device initiates handshaking. |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-interchangecheck.html language=enus -->
## TOPIC 00030: Inherent IVI Attributes:User Options:Interchange Check

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-interchangecheck.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and retrieve interchangeability warnings when you call the niSwitch Connect Channels, niSwitch Set Path and niSwitch Initiate Scan VIs. The default value is FALSE. Interchangeability checking examines the properties in a capability group only

### Inherent IVI Attributes:User Options:Interchange Check

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings when you call the [niSwitch Connect Channels](/csh?context=niswitch_switchviref_niswitch_connect_channels), [niSwitch Set Path](/csh?context=niswitch_switchviref_niswitch_set_path) and [niSwitch Initiate Scan](/csh?context=niswitch_switchviref_niswitch_initiate_scan) VIs. The default value is FALSE.

Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property that you have not set or that has been invalidated affects the behavior of the instrument.

Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Call [niSwitch Get Next Interchange Warning](/csh?context=niswitch_switchviref_niswitch_get_next_interchange_warning) VI to extract interchange warnings. Call the [niSwitch Clear Interchange Warnings](/csh?context=niswitch_switchviref_niswitch_clear_interchange_warnings) VI to clear the list of interchangeability warnings without reading them.

**Related topics**

- niSwitch Get Next Interchange Warning
- niSwitch Properties
- niSwitch Reset Interchange Check

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interchange Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-ioresourcedescriptor.html language=enus -->
## TOPIC 00031: Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-ioresourcedescriptor.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the resource descriptor the instrument driver uses to identify the physical device. If you initialize the instrument driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration Utility. If you initialize the instrument dr

### Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor

Contains the resource descriptor the instrument driver uses to identify the physical device.

If you initialize the instrument driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration Utility. If you initialize the instrument driver with the resource descriptor, this property contains that value.

**Related topics**

- Initialization
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IO Resource Descriptor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isconfigurationchannel.html language=enus -->
## TOPIC 00032: Channel Configuration:Is Configuration Channel

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isconfigurationchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isconfigurationchannel.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. The instrument driver uses configuration channels to create paths between the channels you specify in the niSwitch Connect Channels VI. Set this property to TRUE to designate the chan

### Channel Configuration:Is Configuration Channel

Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. The instrument driver uses configuration channels to create paths between the channels you specify in the [niSwitch Connect Channels](/csh?context=niswitch_switchviref_niswitch_connect_channels) VI.

Set this property to TRUE to designate the channel as a configuration channel. Set this property to FALSE to designate the channel as available for external connections.
 Because you cannot use a configuration channel for external connections, the [niSwitch Connect Channels](/csh?context=niswitch_switchviref_niswitch_connect_channels) VI returns the Is Configuration Channel error when you attempt to establish a connection between a configuration channel and any other channel.

**Related topics**

- niSwitch Properties
- Setting Source and Configuration Channels

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Configuration Channel |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isdebounced.html language=enus -->
## TOPIC 00033: Module Characteristics:Is Debounced

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isdebounced.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isdebounced.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid. Related topics Electromechanical Relays niSwitch Properties Settling Time Remarks The following table lists the characteristi

### Module Characteristics:Is Debounced

Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid.

**Related topics**

- Electromechanical Relays
- niSwitch Properties
- Settling Time

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Debounced |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isscanning.html language=enus -->
## TOPIC 00034: Scanning Configuration:Is Scanning

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isscanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-isscanning.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the switch module has completed the scan operation. TRUE indicates that the scan has completed. Related topics niSwitch Properties Scanning Remarks The following table lists the characteristics of this property. Short Name Is Scanning Data type cbool.png Permissions Read Only Chann

### Scanning Configuration:Is Scanning

Indicates whether the switch module has completed the scan operation. TRUE indicates that the scan has completed.

**Related topics**

- niSwitch Properties
- Scanning

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Scanning |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-issourcechannel.html language=enus -->
## TOPIC 00035: Channel Configuration:Is Source Channel

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-issourcechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-issourcechannel.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to designate the channel as a source channel. Set this property to TRUE when you connect the channel to a power supply, a function generator, or an active measurement point on the unit under test, and you do not want to connect the channel to another source. The instrument driver p

### Channel Configuration:Is Source Channel

Specifies whether to designate the channel as a source channel.

Set this property to TRUE when you connect the channel to a power supply, a function generator, or an active measurement point on the unit under test, and you do not want to connect the channel to another source. The instrument driver prevents source channels from connecting to each other: when you attempt to connect two source channels, the [niSwitch Connect Channels](/csh?context=niswitch_switchviref_niswitch_connect_channels) VI returns the Attempt To Connect Sources error.

**Related topics**

- niSwitch Properties
- Setting Source and Configuration Channels

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Source Channel |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-iswaitingfortrigger.html language=enus -->
## TOPIC 00036: Scanning Configuration:Is Waiting for Trigger?

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-iswaitingfortrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-iswaitingfortrigger.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates with a semi-colon (;) that at that point in the scan list, the scan engine should pause until a trigger is received from the trigger input. If you generate that trigger through either a hardware pulse or the niSwitch Send Software Trigger VI, you must know when the scan engine has reached

### Scanning Configuration:Is Waiting for Trigger?

Indicates with a semi-colon (;) that at that point in the scan list, the scan engine should pause until a trigger is received from the trigger input. If you generate that trigger through either a hardware pulse or the [niSwitch Send Software Trigger](/csh?context=niswitch_switchviref_niswitch_send_software_trigger) VI, you must know when the scan engine has reached such a state.

**Related topics**

- niSwitch Configure Scan Trigger
- niSwitch Properties
- Scanning

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Waiting for Trigger? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-logicalname.html language=enus -->
## TOPIC 00037: Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-logicalname.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the logical name you specified when opening the current IVI session. You can wire a logical name to the niSwitch Initialize or the niSwitch Initialize With Options VIs. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a virtual instr

### Inherent IVI Attributes:Advanced Session Information:Logical Name

Contains the logical name you specified when opening the current IVI session.

You can wire a logical name to the [niSwitch Initialize](/csh?context=niswitch_switchviref_niswitch_initialize) or the [niSwitch Initialize With Options](/csh?context=niswitch_switchviref_niswitch_initialize_with_options) VIs. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section, which specifies a physical device and initial user options, in the IVI Configuration file.

**Related topics**

- Initialization
- niSwitch Properties
- Using NI Switches in IVI

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-manufacturer.html language=enus -->
## TOPIC 00038: Inherent IVI Attributes:Instrument Identification:Manufacturer

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-manufacturer.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the name of the manufacturer of the instrument currently in use. Related topics niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Manufacturer Data type cstr.png Permissions Read Only Channel-based No Resettable No

### Inherent IVI Attributes:Instrument Identification:Manufacturer

Contains the name of the manufacturer of the instrument currently in use.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Manufacturer |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavescanadvancedbus.html language=enus -->
## TOPIC 00039: Obsolete Attributes:Master Slave Scan Advanced Bus

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavescanadvancedbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavescanadvancedbus.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property has been deprecated and might be removed from a future release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI instead. Remarks The following table lists the characteristics of this property. Short Name Master Slave Scan Advanced Bus Data type ci32.png Permissions Read/Write C

### Obsolete Attributes:Master Slave Scan Advanced Bus

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use [niSwitch Route Scan Advanced Output](/csh?context=niswitch_switchviref_niswitch_route_scan_advanced_output) VI instead.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Master Slave Scan Advanced Bus |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavetriggerbus.html language=enus -->
## TOPIC 00040: Obsolete Attributes:Master Slave Trigger Bus

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavetriggerbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-masterslavetriggerbus.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead. Remarks The following table lists the characteristics of this property. Short Name Master Slave Trigger Bus Data type ci32.png Permissions Read/Write Channel-ba

### Obsolete Attributes:Master Slave Trigger Bus

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the [niSwitch Route Trigger Input](/csh?context=niswitch_switchviref_niswitch_route_trigger_input) VI instead.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Master Slave Trigger Bus |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumacvoltage.html language=enus -->
## TOPIC 00041: Module Characteristics:Maximum AC Voltage

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumacvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumacvoltage.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum AC voltage the channel can switch in volts RMS. Related topics General Switching Considerations niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Maximum AC Voltage Data type cdbl.png Permissions Read Only Channel-based Yes Res

### Module Characteristics:Maximum AC Voltage

Returns the maximum AC voltage the channel can switch in volts RMS.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum AC Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryaccurrent.html language=enus -->
## TOPIC 00042: Module Characteristics:Maximum Carry AC Current

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryaccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryaccurrent.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum AC current the channel can carry in amperes RMS. Related topics General Switching Considerations niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Maximum Carry AC Current Data type cdbl.png Permissions Read Only Channel-based

### Module Characteristics:Maximum Carry AC Current

Returns the maximum AC current the channel can carry in amperes RMS.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Carry AC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryacpower.html language=enus -->
## TOPIC 00043: Module Characteristics:Maximum Carry AC Power

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryacpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarryacpower.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum AC power the channel can carry in volt-amperes. Related topics General Switching Considerations niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Maximum Carry AC Power Data type cdbl.png Permissions Read Only Channel-based Yes

### Module Characteristics:Maximum Carry AC Power

Returns the maximum AC power the channel can carry in volt-amperes.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Carry AC Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydccurrent.html language=enus -->
## TOPIC 00044: Module Characteristics:Maximum Carry DC Current

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydccurrent.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum DC current the channel can carry in amperes. Related topics General Switching Considerations niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Maximum Carry DC Current Data type cdbl.png Permissions Read Only Channel-based Yes

### Module Characteristics:Maximum Carry DC Current

Returns the maximum DC current the channel can carry in amperes.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Carry DC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydcpower.html language=enus -->
## TOPIC 00045: Module Characteristics:Maximum Carry DC Power

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumcarrydcpower.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum DC power the channel can carry in watts. Related topics General Switching Considerations niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Maximum Carry DC Power Data type cdbl.png Permissions Read Only Channel-based Yes Resett

### Module Characteristics:Maximum Carry DC Power

Returns the maximum DC power the channel can carry in watts.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Carry DC Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingaccurrent.html language=enus -->
## TOPIC 00046: Module Characteristics:Maximum Switching AC Current

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingaccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingaccurrent.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum AC current the channel can switch in amperes RMS. Related topics niSwitch Properties Switching Current Remarks The following table lists the characteristics of this property. Short Name Maximum Switching AC Current Data type cdbl.png Permissions Read Only Channel-based Yes Resett

### Module Characteristics:Maximum Switching AC Current

Returns the maximum AC current the channel can switch in amperes RMS.

**Related topics**

- niSwitch Properties
- Switching Current

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Switching AC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdccurrent.html language=enus -->
## TOPIC 00047: Module Characteristics:Maximum Switching DC Current

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdccurrent.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum DC current the channel can switch in amperes. Related topics niSwitch Properties Switching Current Remarks The following table lists the characteristics of this property. Short Name Maximum Switching DC Current Data type cdbl.png Permissions Read Only Channel-based Yes Resettable

### Module Characteristics:Maximum Switching DC Current

Returns the maximum DC current the channel can switch in amperes.

**Related topics**

- niSwitch Properties
- Switching Current

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Switching DC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdcpower.html language=enus -->
## TOPIC 00048: Module Characteristics:Maximum Switching DC Power

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-maximumswitchingdcpower.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum DC power the channel can switch in watts. Related topics niSwitch Properties Switching Power Remarks The following table lists the characteristics of this property. Short Name Maximum Switching DC Power Data type cdbl.png Permissions Read Only Channel-based Yes Resettable No

### Module Characteristics:Maximum Switching DC Power

Returns the maximum DC power the channel can switch in watts.

**Related topics**

- niSwitch Properties
- Switching Power

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Switching DC Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-model.html language=enus -->
## TOPIC 00049: Inherent IVI Attributes:Instrument Identification:Model

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-model.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the model number or name of the instrument currently in use. Related topics niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Model Data type cstr.png Permissions Read Only Channel-based No Resettable No

### Inherent IVI Attributes:Instrument Identification:Model

Contains the model number or name of the instrument currently in use.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofcolumns.html language=enus -->
## TOPIC 00050: Matrix Configuration:Number of Columns

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofcolumns.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofcolumns.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of channels on the column of a matrix or scanner. If the switch module is a scanner, this property returns the number of input channels. The Wire mode property affects the number of available columns. For example, if your switch module has eight input lines and you use the 4-wire

### Matrix Configuration:Number of Columns

Returns the number of channels on the column of a matrix or scanner. If the switch module is a scanner, this property returns the number of input channels.

The [Wire mode](pniswitch-wiremode.html) property affects the number of available columns. For example, if your switch module has eight input lines and you use the 4-wire mode, then the number of columns available is two.

**Related topics**

- Matrix
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Columns |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrelays.html language=enus -->
## TOPIC 00051: Module Characteristics:Number of Relays

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrelays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrelays.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of relays that the instrument driver supports. Related topics niSwitch Get Relay Name niSwitch Properties Remarks The following table lists the characteristics of this property. Short Name Number of Relays Data type ci32.png Permissions Read Only Channel-based No Resettable No

### Module Characteristics:Number of Relays

Returns the number of relays that the instrument driver supports.

**Related topics**

- niSwitch Get Relay Name
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Relays |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrows.html language=enus -->
## TOPIC 00052: Matrix Configuration:Number of Rows

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrows.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-numberofrows.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of channels on the row of a matrix or scanner. If the switch module is a scanner, this property returns the number of output channels. The Wire mode property affects the number of available rows. For example, if your switch module has eight input lines and you use the 2-wire mode,

### Matrix Configuration:Number of Rows

Returns the number of channels on the row of a matrix or scanner. If the switch module is a scanner, this property returns the number of output channels.

The [Wire mode](pniswitch-wiremode.html) property affects the number of available rows. For example, if your switch module has eight input lines and you use the 2-wire mode, then the number of columns you have available is four.

**Related topics**

- Matrix
- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Rows |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-labview-api-ref path=instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-queryinstrumentstatus.html language=enus -->
## TOPIC 00053: Inherent IVI Attributes:User Options:Query Instrument Status

- bundle_id: `ni-switch-labview-api-ref`
- source_path: `instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-labview-api-ref/raw/resource/enus/instr-lib/niswitch/niswitch-rc/niswitch/pniswitch-queryinstrumentstatus.html
- document_id: `ni-switch-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the instrument driver queries the instrument status after each operation. The default value is TRUE. Use the niSwitch Initialize With Options VI to override the default value. Querying the instrument status is useful for debugging. After you validate your program, set this property

### Inherent IVI Attributes:User Options:Query Instrument Status

Specifies whether the instrument driver queries the instrument status after each operation. The default value is TRUE. Use the [niSwitch Initialize With Options](/csh?context=niswitch_switchviref_niswitch_initialize_with_options) VI to override the default value.

Querying the instrument status is useful for debugging. After you validate your program, set this property to FALSE to disable status checking and maximize performance.
 The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Query Instrument Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

Parent topic:

niSwitch Properties
