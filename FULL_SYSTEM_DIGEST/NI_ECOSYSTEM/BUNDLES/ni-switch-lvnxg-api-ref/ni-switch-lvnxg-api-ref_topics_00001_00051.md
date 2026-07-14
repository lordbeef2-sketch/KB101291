# NI DOCUMENT BUNDLE: ni-switch-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-switch-lvnxg-api-ref start=1 end=51 -->
<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=action-nodes.html language=enus -->
## TOPIC 00001: Action Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `action-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/action-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Action nodes to perform Scan, Channel, and Relay actions.

Action Nodes

Use the Action nodes to perform Scan, Channel, and Relay actions.

NI-SWITCH Nodes

Use the nodes on the NI-SWITCH palette to build the block diagram.

Channel Nodes

Use the NI-SWITCH Channel nodes to configure channels for your device.

Disable

Places the switch module in a quiescent state where it has minimal or no impact on the system to which it is connected. This node disconnects all channels, and any scan in progress is aborted.

Relay Nodes

Use the NI-SWITCH relay nodes to control and query individual relays of an NI switch.

Scan Nodes

Use the NI-SWITCH scan nodes to configure a scan of an NI switch.

Parent topic:

NI-SWITCH Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=channel-nodes.html language=enus -->
## TOPIC 00002: Channel Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `channel-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/channel-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SWITCH Channel nodes to configure channels for your device.

Channel Nodes

Use the NI-SWITCH Channel nodes to configure channels for your device.

Action Nodes

Use the Action nodes to perform Scan, Channel, and Relay actions.

Can Connect Channels

Verifies that a path can be created between two channels.

Connect Channels

Creates connections between channels.

Disconnect Channels

Breaks connections between channels.

Disconnect All Channels

Breaks all existing paths.

Get Channel Name

channel string

Get Path

Returns a string that identifies the explicit path created with the niSwitch Connect Channels node. Pass this string to the niSwitch Set Path node to establish the exact same path in future connections.

Set Path

Connects two channels by specifying an explicit path.

Switch Is Debounced

Indicates whether all created paths have settled.

Wait For Debounce

Pauses until all created paths have settled.

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=configuration-nodes.html language=enus -->
## TOPIC 00003: Configuration Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `configuration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/configuration-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Configuration nodes to configure the device for scanning.

Configuration Nodes

Use the Configuration nodes to configure the device for scanning.

NI-SWITCH Nodes

Use the nodes on the NI-SWITCH palette to build the block diagram.

Configure Scan List

Configures the scan list and scan mode used for scanning.

Set Continuous Scan

Sets the switch to loop continuously through the scan list or to stop scanning after one pass through the scan list.

Trigger Nodes

Use the Trigger nodes to configure triggers for NI-SWITCH.

Parent topic:

NI-SWITCH Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=connect-channels.html language=enus -->
## TOPIC 00004: Connect Channels

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `connect-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/connect-channels.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates connections between channels.

Connect Channels

Creates connections between channels.

Channel Nodes

Use the NI-SWITCH Channel nodes to configure channels for your device.

Connect Channels (Single)

Creates a path between two channels. NI-SWITCH calculates and uses the shortest path between the two channels.

Connect Channels (Multiple)

Creates connections between multiple channels.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=disconnect-channels.html language=enus -->
## TOPIC 00005: Disconnect Channels

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `disconnect-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/disconnect-channels.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks connections between channels.

Disconnect Channels

Breaks connections between channels.

Channel Nodes

Use the NI-SWITCH Channel nodes to configure channels for your device.

Disconnect Channels (Single)

Breaks the path between two channels created with the niSwitch Connect Channels node or the niSwitch Set Path node. If no connection exists between the channels, NI-SWITCH returns an error.

Disconnect Channels (Multiple)

Breaks connections between channels.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=ivi-utilities-nodes.html language=enus -->
## TOPIC 00006: IVI Utilities Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `ivi-utilities-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/ivi-utilities-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SWITCH IVI Utilities nodes to exercise additional IVI functions of an NI switch.

IVI Utilities Nodes

Use the NI-SWITCH IVI Utilities nodes to exercise additional IVI functions of an NI switch.

Utility Nodes

Use the NI-SWITCH utility nodes to exercise additional features of an NI switch.

Get Next Coercion Record

Returns the coercion information associated with the IVI session, and clears the oldest instance in which NI-SWITCH coerced a value you specified.

Get Next Interchange Warning

Returns the interchangeability warnings associated with the IVI session. This node retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.

Clear Interchange Warnings

Clears the list of current interchange warnings.

Reset Interchange Check

Configures interchangeability checking algorithms to ignore all previous configuration operations.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-abort-scan.html language=enus -->
## TOPIC 00007: Abort Scan

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-abort-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-abort-scan.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the scan in progress. Use the niSwitch Initiate Scan node to initiate an aborted scan. If the switch module is not scanning, a No Scan In Progress error is returned. If you are using a legacy resource descriptor (SCXI:: or PXI::) and you abort a scan, the switch module returns to a disconnect

Abort Scan

Aborts the scan in progress. Use the niSwitch Initiate Scan node to initiate an aborted scan.

If the switch module is not scanning, a No Scan In Progress error is returned.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Understanding Errors

If error in describes an error that had occurred before calling this node, the node still attempts to abort the scan. However, if the attempt fails, the node returns the error information that was passed in from the error in parameter.

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-can-connect-channels.html language=enus -->
## TOPIC 00008: Can Connect Channels

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-can-connect-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-can-connect-channels.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that a path can be created between two channels. If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned. session in Control that identifies a

Can Connect Channels

Verifies that a path can be created between two channels.

If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, an Implicit Connection Exists warning is returned.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 1

One of the channel names of the desired path. Pass the other channel name as channel 2.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 2

One of the channel names of the desired path. Pass the other channel name as channel 1.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### path capability

Value that indicates whether a path is valid.

| Path Available | The path is possible and available. |
| --- | --- |
| Path Exists | The path is possible, but already exists. |
| Path Unsupported | The path is not possible in the specified switch module and topology. |
| Resource In Use | The path is possible, but elements of the path are in use by another existing path. You must destroy the other path before creating this one. |
| Source Conflict | The path is possible, but connecting the channels will connect two sources. |
| Channel Not Available | The channel 1 and channel 2 inputs are configuration channels and are thus unavailable for external connections. |

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-clear-interchange-warnings.html language=enus -->
## TOPIC 00009: Clear Interchange Warnings

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-clear-interchange-warnings.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-clear-interchange-warnings.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that occur before this

Clear Interchange Warnings

Clears the list of current interchange warnings.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Details

When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so, ensure that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the instrument state depends on the configuration from a previously executed test module. Therefore, if you execute the test modules in a different order, the behavior of the instrument and therefore the entire test module is likely to change. This behavior change is generally instrument specific and represents an interchangeability problem.

You can use the niSwitch Reset Interchange Check node to test for such cases. After you call the niSwitch Reset Interchange Check node, the interchangeability checking algorithms in the specific driver ignore all previous configuration operations. By calling the niSwitch Reset Interchange Check node at the beginning of a test module, you can determine whether the test module has dependencies on the operation of previously executed test modules.

To guarantee that the niSwitch Get Next Interchange Warning node only returns those interchangeability warnings generated after calling the niSwitch Reset Interchange Check node, clear the list of interchangeability warnings by repeatedly calling the niSwitch Get Next Interchange Warning node until no interchangeability warnings are returned. If you are not interested in the content of those warnings, call the niSwitch Clear Interchange Warnings node.

Parent topic:

IVI Utilities Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-close.html language=enus -->
## TOPIC 00010: Close

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-close.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Terminates the NI-SWITCH session and all of its attributes and deallocates any memory resources the driver uses. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch I

Close

Terminates the NI-SWITCH session and all of its attributes and deallocates any memory resources the driver uses.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Re-initializing NI-SWITCH

niSwitch Initialize With Topology

niSwitch Initialize With Options

niSwitch Initialize

#### Closing with Errors

If error in describes an error that occurred before the call to niSwitch Close, this node still attempts to close the session. However, if the attempt fails, this node returns the error information that was passed in from error in.

Parent topic:

NI-SWITCH Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-commit.html language=enus -->
## TOPIC 00011: Commit

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-commit.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downloads the configured scan list and trigger settings to hardware. Calling this node is optional as it is implicitly called during the niSwitch Initiate Scan node. Use this node to arm triggers in a given order or to control when hardware operations are performed. session in Control that identifie

Commit

Downloads the configured scan list and trigger settings to hardware.

Calling this node is optional as it is implicitly called during the niSwitch Initiate Scan node. Use this node to arm triggers in a given order or to control when hardware operations are performed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-configure-scan-list.html language=enus -->
## TOPIC 00012: Configure Scan List

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-configure-scan-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-configure-scan-list.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scan list and scan mode used for scanning. The scan list is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer: com0>ch0; com0>ch1; com0>ch2; session in Control that identifies a

Configure Scan List

Configures the scan list and scan mode used for scanning.

The scan list is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer:

com0>ch0; com0>ch1; com0>ch2;

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scan list

Scan list to use.

Scan List

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### scan mode

Control that specifies how the switch module breaks existing connections when scanning.

Scan Mode

Default value: Break Before Make

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

To see the status of the scan, call either the niSwitch Switch Is Scanning node or the niSwitch Wait For Scan To Complete node. Use the niSwitch Configure Scan Trigger node to configure the scan trigger, and the niSwitch Initiate Scan node to start the scan.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-configure-scan-trigger.html language=enus -->
## TOPIC 00013: Configure Scan Trigger

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-configure-scan-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-configure-scan-trigger.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scan triggers for the scan list established with the niSwitch Configure Scan List node. This node sets the location where the switch expects to receive an input trigger to advance through the scan list. This node also sets the location where it generates a scan advanced signal after i

Configure Scan Trigger

Configures the scan triggers for the scan list established with the niSwitch Configure Scan List node.

This node sets the location where the switch expects to receive an input trigger to advance through the scan list. This node also sets the location where it generates a scan advanced signal after it completes an entry in the scan list.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scan delay

Minimum length of time the switch device waits after it creates a path until it asserts a trigger on the Scan Advanced Output channel.

Scan Delay

scan delay

Default value: 0.0 (seconds)

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger input

Trigger source used by the switch module during scanning. NI-SWITCH uses this value to set the Trigger Input property.

The switch module waits for a trigger at the specified location when it encounters a semicolon in the scan list. When the trigger occurs, the switch device advances to the next entry in the scan list and waits for a trigger from the location specified in trigger input.

Default value: 
 External

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### scan advanced output (External)

Output terminal for the Scan Advanced Output trigger signal. NI-SWITCH uses this value to set the Scan Advanced Output property.

After the switch processes each entry in the scan list, it waits the length of time specified in scan delay, then asserts a trigger on the line specified in scan advanced output.

| None | No Scan Advanced Output trigger is produced. |
| --- | --- |
| External | Sends the Scan Advanced Output trigger to the front connector of the switch module. Same as Front Connector. |
| TTLx | Sends the Scan Advanced Output trigger to PXI or SCXI trigger line x. |
| PXI Star | The switch waits until it receives a trigger on the PXI star trigger bus before processing the next entry in the scan list. |
| Rear Connector | Valid only for SCXI. Sends the Scan Advanced Output trigger to the rear connector of the switch module. |
| Front Connector | Sends the Scan Advanced Output trigger to the front connector of the switch module. Same as External. |
| Rear Connector <1..12> | Valid only for SCXI. Sends a Scan Advanced Output trigger to the rear connector of Slot <1..12>. Can be used as an alternative to calling the niSwitch Route Scan Advanced Output node. |
| Front Connector <1..12> | Valid only for SCXI. Sends a Scan Advanced Output trigger to the front connector of Slot <1..12>. Can be used as an alternative to calling the niSwitch Route Scan Advanced Output node. |

Default value: 
 External

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Synchronous Scanning

For synchronous scanning, set scan advanced output to None and define trigger input. For handshaking, trigger input and scan advanced output must be set.

Triggers generally originate from the SCXI or PXI trigger bus, the terminals on the front connector of the switch module, or the AUX connector on the rear of the switch module (referred to as the rear connector and supported by SCXI only).

When scanning a module that is not directly cabled to the trigger from its own front or rear connector, use the niSwitch Route Trigger Input node and/or the niSwitch Route Scan Advanced Output node to route the triggers on the cabled module to one of the backplane lines. When using these nodes to route triggers to the backplane, specify the backplane trigger location when calling the niSwitch Configure Scan Trigger node (even if it is the module cabled to the trigger source).

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-connect-channels-multiple.html language=enus -->
## TOPIC 00014: Connect Channels (Multiple)

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-connect-channels-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-connect-channels-multiple.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates connections between multiple channels. Specify connections with two endpoints only or the explicit path between two endpoints. NI-SWITCH calculates and uses the shortest path between the channels. In the event of an error, connecting stops at the point in the list where the error occurred. s

Connect Channels (Multiple)

Creates connections between multiple channels.

Specify connections with two endpoints only or the explicit path between two endpoints. NI-SWITCH calculates and uses the shortest path between the channels. In the event of an error, connecting stops at the point in the list where the error occurred.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### connection list

List of connections to make between channels.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Connect Channels

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-connect-channels-single.html language=enus -->
## TOPIC 00015: Connect Channels (Single)

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-connect-channels-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-connect-channels-single.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a path between two channels. NI-SWITCH calculates and uses the shortest path between the two channels. Paths are bidirectional. For example, if a path exists between CH1 and CH2, then the path also exists between CH2 and CH1. session in Control that identifies a particular NI-SWITCH session

Connect Channels (Single)

Creates a path between two channels. NI-SWITCH calculates and uses the shortest path between the two channels.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 1

One of the channel names of the desired path. Pass the other channel name as channel 2.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 2

One of the channel names of the desired path. Pass the other channel name as channel 1.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Errors

If a path is unavailable between the two channels, NI-SWITCH returns the following errors:

| Error | Description |
| --- | --- |
| Explicit Connection Exists | The channels have already been explicitly connected by calling either this node or the niSwitch Set Path node. |
| Is Configuration Channel | One of the channels is a configuration channel. Error elaboration contains information about the sources connected to channel 1 and channel 2. |
| Attempt to Connect Sources | Both channels are connected to a source. Error elaboration contains information about the sources connected to channel 1 and channel 2. |
| Cannot Connect to Itself | Channel 1 and channel 2 are identical. |
| Path Not Found | No paths between channel 1 and channel 2 are available. |
| Resource In Use | Channel 1 and/or channel 2 is in use. This error often occurs when one of the channels is set as a configuration channel and is in use or if one of the channels is a common multiplexer channel is in use. |

Parent topic:

Connect Channels

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-disable.html language=enus -->
## TOPIC 00016: Disable

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-disable.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Places the switch module in a quiescent state where it has minimal or no impact on the system to which it is connected. This node disconnects all channels, and any scan in progress is aborted. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize

Disable

Places the switch module in a quiescent state where it has minimal or no impact on the system to which it is connected. This node disconnects all channels, and any scan in progress is aborted.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Understanding Errors

If error in describes an error that had occurred before calling niSwitch Disable, this node still attempts to disable the switch. However, if the attempt fails, this node returns the error information that was passed in from error in.

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-disconn-channels-mult.html language=enus -->
## TOPIC 00017: Disconnect Channels (Multiple)

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-disconn-channels-mult.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-disconn-channels-mult.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks connections between channels. If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the node stops at the point in the list where the error occurred. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initi

Disconnect Channels (Multiple)

Breaks connections between channels.

If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the node stops at the point in the list where the error occurred.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### disconnection list

List of connections between channels to break.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Disconnect Channels

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-disconnect-all-channels.html language=enus -->
## TOPIC 00018: Disconnect All Channels

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-disconnect-all-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-disconnect-all-channels.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks all existing paths. If the switch module cannot break all paths, a warning is returned. If an error in parameter describes an error that occurred before the call to this node, NI-SWITCH still attempts to break all connections and returns the error information that was passed in from error in.

Disconnect All Channels

Breaks all existing paths.

If the switch module cannot break all paths, a warning is returned. If an error in parameter describes an error that occurred before the call to this node, NI-SWITCH still attempts to break all connections and returns the error information that was passed in from error in.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Closing Relays

Relays closed with the niSwitch Relay Control node are also disconnected.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-disconnect-channels-single.html language=enus -->
## TOPIC 00019: Disconnect Channels (Single)

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-disconnect-channels-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-disconnect-channels-single.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks the path between two channels created with the niSwitch Connect Channels node or the niSwitch Set Path node. If no connection exists between the channels, NI-SWITCH returns an error. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize Wit

Disconnect Channels (Single)

Breaks the path between two channels created with the niSwitch Connect Channels node or the niSwitch Set Path node. If no connection exists between the channels, NI-SWITCH returns an error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 1

One of the channel names of the path to break. Pass the other channel names for the switch module.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 2

One of the channel names of the path to break. Pass the other channel name as channel 1.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Disconnect Channels

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-error-message.html language=enus -->
## TOPIC 00020: Error Message

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-error-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-error-message.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an error code returned by NI-SWITCH into a user-readable string. Generally this information is supplied in error out of any NI-SWITCH node. Use this node for a static lookup of an error code description. session in Control that identifies a particular NI-SWITCH session established with the

Error Message

Converts an error code returned by NI-SWITCH into a user-readable string.
 Generally this information is supplied in error out of any NI-SWITCH node. Use this node for a static lookup of an error code description.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### error code

Status code returned by any NI-SWITCH node.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

Error information formatted into a string.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-channel-name.html language=enus -->
## TOPIC 00021: Get Channel Name

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-channel-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-channel-name.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the channel string that is in the channel table at the specified index. Use this node in a For Loop to get a complete list of valid channel names for the switch module. Use the Channel Count property to determine the number of channels. session in Control that identifies a particular NI-SWIT

Get Channel Name

Returns the channel string that is in the channel table at the specified index.

Use this node in a For Loop to get a complete list of valid channel names for the switch module. Use the Channel Count property to determine the number of channels.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Input that adds a 1-based index into the channel table.

Channel Count

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### channel string

Channel string that is in the channel table at index.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-next-coercion-record.html language=enus -->
## TOPIC 00022: Get Next Coercion Record

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-next-coercion-record.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-next-coercion-record.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the coercion information associated with the IVI session, and clears the oldest instance in which NI-SWITCH coerced a value you specified. If you set the Record Value Coercions property to TRUE, NI-SWITCH keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to instru

Get Next Coercion Record

Returns the coercion information associated with the IVI session, and clears the oldest instance in which NI-SWITCH coerced a value you specified.

If you set the Record Value Coercions property to TRUE, NI-SWITCH keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to instrument driver nodes. Use this node to retrieve information from that list.

The node returns an empty string if no coercion records remain for the session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### coercion record

Next coercion record for the IVI session.

If there are no coercion records remaining for the session, the node returns an empty string.

Parent topic:

IVI Utilities Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-next-interchange-warning.html language=enus -->
## TOPIC 00023: Get Next Interchange Warning

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-next-interchange-warning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-next-interchange-warning.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the interchangeability warnings associated with the IVI session. This node retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause diffe

Get Next Interchange Warning

Returns the interchangeability warnings associated with the IVI session. This node retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### interchange warning

Next interchange warning for the IVI session.

If there are no interchangeability warnings remaining for the session, this output returns an empty string.

#### Programming Patterns

To guarantee that this node only returns those interchangeability warnings generated after calling the niSwitch Reset Interchange Check node, clear the list of interchangeability warnings by repeatedly calling this node until no interchangeability warnings are returned. If you are not interested in the content of those warnings, call the niSwitch Clear Interchange Warnings node.

#### Interchangeability Checking

NI-SWITCH performs interchangeability checking when the Interchange Check property is set to TRUE.

The node returns an empty string for interchange warning if no interchangeability warnings remain for the session.

In general, NI-SWITCH generates interchangeability warnings when a property that affects the behavior of the switch is in a state that you did not specify.

Parent topic:

IVI Utilities Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-path.html language=enus -->
## TOPIC 00024: Get Path

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-path.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-path.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that identifies the explicit path created with the niSwitch Connect Channels node. Pass this string to the niSwitch Set Path node to establish the exact same path in future connections. In some cases, multiple paths are available between two channels. When you call the niSwitch Conn

Get Path

Returns a string that identifies the explicit path created with the niSwitch Connect Channels node. Pass this string to the niSwitch Set Path node to establish the exact same path in future connections.

In some cases, multiple paths are available between two channels. When you call the niSwitch Connect Channels node, NI-SWITCH selects an available path; however, the driver may not always select the same path through the switch module.

This node returns only those paths explicitly created by the niSwitch Connect Channels node or the niSwitch Set Path node. For example, if you connect channels CH1 and CH3,and then channels CH2 and CH3, an explicit path between channels CH1 and CH2 does not exist, and an error is returned.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 1

One of the channel names of the desired path. Pass the other channel name as channel 2.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel 2

One of the channel names of the desired path. Pass the other channel name as channel 1.

Examples of valid channel names are 
 ch0, 
 com0, 
 ab0, 
 r1, 
 c2, and 
 cjtemp.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### path

String that is composed of comma-separated paths between channel 1 and channel 2.

The first and last names in the path are the path endpoints. All other channels in the path are configuration channels.

Examples of returned paths:

ch0>com0, com0>ab0.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-relay-count.html language=enus -->
## TOPIC 00025: Get Relay Count

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-relay-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-relay-count.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of times the relay has changed from Closed to Open. Relay count is useful for tracking relay life and use. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or t

Get Relay Count

Returns the number of times the relay has changed from Closed to Open.
 Relay count is useful for tracking relay life and use.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### relay name

Name of the relay or set of relays to control.

You can supply a single relay name or comma-delimited list of relay names to control these relays. Examples of valid relay names are ch0, ab0, 1wire, and hlselect.

Note

niSwitch Wait For Debounce

niSwitch Switch Is Debounced

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### count

Number of relay cycles.

#### Programming Patterns

Call the niSwitch Wait For Debounce node before this node to ensure an accurate count.

Parent topic:

Relay Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-relay-name.html language=enus -->
## TOPIC 00026: Get Relay Name

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-relay-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-relay-name.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relay name that is in the relay list at the specified index. Use this node in a For Loop to get a complete list of valid relay names for the switch module. Use the Number of Relays property to determine the number of relays. session in Control that identifies a particular NI-SWITCH sessi

Get Relay Name

Returns the 
relay name that is in the relay list at the specified index.

Use this node in a For Loop to get a complete list of valid relay names for the switch module. Use the Number of Relays property to determine the number of relays.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Input that adds a 1-based index into the channel table.

Channel Count

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### relay name

Name of the relay.

Examples of valid relay names are ch0, ab0, 1wire, and hlselect.

Parent topic:

Relay Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-get-relay-position.html language=enus -->
## TOPIC 00027: Get Relay Position

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-get-relay-position.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-get-relay-position.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relay position for the relay specified in relay name. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that

Get Relay Position

Returns the relay position for the relay specified in relay name.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### relay name

Name of the relay or set of relays to control.

You can supply a single relay name or comma-delimited list of relay names to control these relays. Examples of valid relay names are ch0, ab0, 1wire, and hlselect.

Note

niSwitch Wait For Debounce

niSwitch Switch Is Debounced

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### position

Relay postition.

| Open | Indicates that the relay is open. |
| --- | --- |
| Closed | Indicates that the relay is closed. |

Parent topic:

Relay Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-initialize-with-topology.html language=enus -->
## TOPIC 00028: Initialize With Topology

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-initialize-with-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-initialize-with-topology.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session handle used to identify the switch module in all subsequent instrument driver calls and sets the topology of the switch module. By default, the switch module is reset to a known state. simulate Boolean value that enables simulation of the switch module specified in resource name. T

Initialize With Topology

Returns a session handle used to identify the switch module in all subsequent instrument driver calls and sets the topology of the switch module.

By default, the switch module is reset to a known state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### simulate

Boolean value that enables simulation of the switch module specified in resource name.

| TRUE | Enables simulation of the switch module. |
| --- | --- |
| FALSE (Default) | Disables simulation of the switch module. |

Default value: False (0)

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the switch module to initialize.

IVI logical names are also valid resource names.

##### Syntax

Optional fields are shown in square brackets ([]). The default values for optional fields are as follows:

chassis ID = 1

bus number = 0

| Configured in MAX Under | Valid Syntax |
| --- | --- |
| Devices and Interfaces | DeviceName |
| PXI System | PXI[bus number]::device number |

##### Resource Name Examples

The following table lists example resource names.

| Resource Name | Description |
| --- | --- |
| SC1Mod3 | NI-DAQmx module in chassis SC1 Slot 3 |
| MySwitch | NI-DAQmx module renamed to MySwitch |
| PXI0:16 | PXI bus 0, device number 16 |
| PXI::16 | PXI bus 0, device number 16 |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### topology name

Topology to use for the switch module specified in resource name. Create a control for topology name to select from a list of topologies.

This topology overrides the topology specified in MAX.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset device

Boolean value that specifies whether to reset the switch module during initialization.

| TRUE (Default) | Specifies to reset the switch module during initialization. |
| --- | --- |
| FALSE | Specifies that the switch module is not reset during initialization. |

Note

niSwitch Initialize With Topology

Default value: TRUE (1)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-SWITCH Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-initiate-scan.html language=enus -->
## TOPIC 00029: Initiate Scan

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-initiate-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-initiate-scan.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits the configured scan list and trigger settings to hardware and initiates the scan. If the niSwitch Commit node was called earlier, niSwitch Initiate Scan only initiates the scan and returns immediately. session in Control that identifies a particular NI-SWITCH session established with the niS

Initiate Scan

Commits the configured scan list and trigger settings to hardware and initiates the scan.
 If the niSwitch Commit node was called earlier, niSwitch Initiate Scan only initiates the scan and returns immediately.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

To stop the scanning operation, call the niSwitch Abort Scan node.

#### Actions Allowed While Scanning

Once the scanning operation begins, you cannot perform any operations other than those allowed by the niSwitch Abort Scan node or the niSwitch Send Software Trigger node, as well as retrieval of attributes. All other nodes return a Scan In Progress error.

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-nodes.html language=enus -->
## TOPIC 00030: NI-SWITCH Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the nodes on the NI-SWITCH palette to build the block diagram.

NI-SWITCH Nodes

Use the nodes on the NI-SWITCH palette to build the block diagram.

Action Nodes

Use the Action nodes to perform Scan, Channel, and Relay actions.

Close

Terminates the NI-SWITCH session and all of its attributes and deallocates any memory resources the driver uses.

Configuration Nodes

Use the Configuration nodes to configure the device for scanning.

Initialize With Topology

Returns a session handle used to identify the switch module in all subsequent instrument driver calls and sets the topology of the switch module.

niSwitch Properties

Gets (reads) and/or sets (writes) properties of the NI-SWITCH driver.

Utility Nodes

Use the NI-SWITCH utility nodes to exercise additional features of an NI switch.

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-prop-node.html language=enus -->
## TOPIC 00031: niSwitch Properties

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-prop-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-prop-node.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) and/or sets (writes) properties of the NI-SWITCH driver. niswitch in Control that specifies inputs to the property node. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default valu

niSwitch Properties

Gets (reads) and/or sets (writes) properties of the NI-SWITCH driver.

[IMAGE alt='1378' src='PropertyNode.niSwitch.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### niswitch in

Control that specifies inputs to the property node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### niswitch out

Indicator that displays outputs from the property node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-SWITCH Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-relay-control.html language=enus -->
## TOPIC 00032: Relay Control

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-relay-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-relay-control.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of source channels and configurations channels is void. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Top

Relay Control

Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of source channels and configurations channels is void.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### relay names

Name of the relay or set of relays to control.

You can supply a single relay name or comma-delimited list of relay names to control these relays. Examples of valid relay names are ch0, ab0, 1wire, and hlselect.

Note

niSwitch Wait For Debounce

niSwitch Switch Is Debounced

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### relay action

Value that specifies whether to open or close the relay.

| Open Relay | Opens the relay. |
| --- | --- |
| Close Relay | Closes the relay. |

Default value: Close Relay (21)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Relay Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-reset-interchange-check.html language=enus -->
## TOPIC 00033: Reset Interchange Check

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-reset-interchange-check.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-reset-interchange-check.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures interchangeability checking algorithms to ignore all previous configuration operations. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node

Reset Interchange Check

Configures interchangeability checking algorithms to ignore all previous configuration operations.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Using Multiple Test Modules

When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so, ensure that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the instrument state depends on the configuration from a previously executed test module. Therefore, if you execute the test modules in a different order, the behavior of the instrument and therefore the entire test module is likely to change. This behavior change is generally instrument specific and represents an interchangeability problem.

You can use this node to test for such cases. After you call this node, the interchangeability checking algorithms in the specific driver ignore all previous configuration operations. By calling this node at the beginning of a test module, you can determine whether the test module has dependencies on the operation of previously executed test modules.

This node does not clear the interchangeability warnings from the list of previously recorded interchangeability warnings.

Parent topic:

IVI Utilities Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-reset-with-defaults.html language=enus -->
## TOPIC 00034: Reset With Defaults

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-reset-with-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-reset-with-defaults.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the switch module and applies initial user-specified settings from the logical name used to initialize the session. If the session was created without a logical name, this node is equivalent to the niSwitch Reset node. session in Control that identifies a particular NI-SWITCH session establis

Reset With Defaults

Resets the switch module and applies initial user-specified settings from the logical name used to initialize the session. If the session was created without a logical name, this node is equivalent to the niSwitch Reset node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Understanding Errors

If error in describes an error that had occurred before calling niSwitch Reset With Defaults, this node still attempts to reset the switch. However, if the attempt fails, this node returns the error information that was passed in from error in.

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-reset.html language=enus -->
## TOPIC 00035: Reset

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-reset.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects all created paths and returns the switch module to the state at initialization. Configuration channel and source channel settings remain unchanged. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch

Reset

Disconnects all created paths and returns the switch module to the state at initialization.
 Configuration channel and source channel settings remain unchanged.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Resetting with Errors

If error in describes an error that occurred before calling this node, this node still attempts to reset the switch. However, if the attempt fails, this node returns the error information that was passed in from the error in parameter.

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-revision-query.html language=enus -->
## TOPIC 00036: Revision Query

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-revision-query.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision of NI-SWITCH. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that occur before this node runs. Th

Revision Query

Returns the revision of NI-SWITCH.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

NI-SWITCH software revision numbers in the form of a string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Currently unsupported.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-route-scan-advanced-output.html language=enus -->
## TOPIC 00037: Route Scan Advanced Output

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-route-scan-advanced-output.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-route-scan-advanced-output.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes the scan advanced output trigger from a trigger bus line (TTLx) to the front or rear connector. Use this node when handshaking with a switch module that is not directly cabled to the controller. In this module's session, set the scan advanced output bus line to a trigger bus line. In the cabl

Route Scan Advanced Output

Routes the scan advanced output trigger from a trigger bus line (TTL*x*) to the front or rear connector.

Use this node when handshaking with a switch module that is not directly cabled to the controller. In this module's session, set the scan advanced output bus line to a trigger bus line. In the cabled module's session, use this node to route from the trigger bus line to the front or rear connector of the cabled module.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### invert

Boolean input that reverses the input trigger signal from rising to falling and falling to rising.

| TRUE | Reverses the input trigger signal. |
| --- | --- |
| FALSE | Does not reverse the input trigger signal. |

Default value: FALSE (0)

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### scan advanced output connector

Destination of the Scan Advanced Output.

Valid locations are the front and rear connectors.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### scan advanced output bus line

Trigger line that routes the scan advanced output trigger from the front or rear connector.

None

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

If this node is used to route scan advanced from a TTL line, specify the TTL line as the scan advanced output destination in the niSwitch Configure Scan Trigger node.

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-route-trigger-input.html language=enus -->
## TOPIC 00038: Route Trigger Input

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-route-trigger-input.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-route-trigger-input.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes the input trigger from the front or rear connector to a trigger bus line (TTLx). This node should be used when scanning a module in a different NI-SWITCH session that is not directly cabled to the trigger source (multimodule scanning operations). invert Boolean input that reverses the input t

Route Trigger Input

Routes the input trigger from the front or rear connector to a trigger bus line (TTL*x*).

This node should be used when scanning a module in a different NI-SWITCH session that is not directly cabled to the trigger source (multimodule scanning operations).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### invert

Boolean input that reverses the input trigger signal from rising to falling and falling to rising.

| TRUE | Reverses the input trigger signal. |
| --- | --- |
| FALSE | Does not reverse the input trigger signal. |

Default value: FALSE (0)

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger input connector

Location of the input trigger source on the switch module.

Valid locations are the front and rear connectors.

Default value: 
 Front Connector

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger input bus line

Trigger line that routes the input trigger.

None

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

If this node is used to route a trigger to a TTL line, specify the TTL line as the trigger input in the niSwitch Configure Scan Trigger node.

#### Disconnecting Routes

To disconnect the route, call this node again and select 
 None for the trigger input bus line parameter.

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-self-test.html language=enus -->
## TOPIC 00039: Self-Test

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-self-test.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies that NI-SWITCH can communicate with the switch module. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that oc

Self-Test

Verifies that NI-SWITCH can communicate with the switch module.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self-test result

Value from the switch self-test.

A value of 0 indicates success and 1 indicates failure.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self-test message

Response string from the switch self-test.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-send-software-trigger.html language=enus -->
## TOPIC 00040: Send Software Trigger

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-send-software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-send-software-trigger.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software trigger to the switch module specified in the NI-SWITCH session. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error

Send Software Trigger

Sends a software trigger to the switch module specified in the NI-SWITCH session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

When the trigger input parameter is set to Software Trigger Function using the niSwitch Configure Scan Trigger or the Trigger Input property, the scan does not proceed from a semicolon (wait for trigger) until this node is called.

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-set-continuous-scan.html language=enus -->
## TOPIC 00041: Set Continuous Scan

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-set-continuous-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-set-continuous-scan.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the switch to loop continuously through the scan list or to stop scanning after one pass through the scan list. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwit

Set Continuous Scan

Sets the switch to loop continuously through the scan list or to stop scanning after one pass through the scan list.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### continuous scan

Boolean value that specifies whether the scan list is run once or continuously during scanning.

| TRUE | Indicates that the scan list is run continuously during scanning. |
| --- | --- |
| FALSE | Indicates that the scan list is run once during scanning. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Call the niSwitch Abort Scan node to halt a continuous scan.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-set-path.html language=enus -->
## TOPIC 00042: Set Path

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-set-path.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-set-path.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects two channels by specifying an explicit path. This node is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use the niSwitch Connect Channels node. To obtain the exact path for a given connection, use the niSwitch Get P

Set Path

Connects two channels by specifying an explicit path.

This node is useful where path repeatability is important, such as in calibrated signal paths. If path repeatability is not necessary, use the niSwitch Connect Channels node.

To obtain the exact path for a given connection, use the niSwitch Get Path node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### path list

String that is composed of comma-separated paths between two channels. The first and last names in the path are the path endpoints. All other channels in the path are configuration channels.

Example of a valid path list string:

ch0>com0, com0>ab0.

In this example, com0 is a configuration channel.

Obtain the path list for a previously created path with the niSwitch Get Path node.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-switch-is-debounced.html language=enus -->
## TOPIC 00043: Switch Is Debounced

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-switch-is-debounced.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-switch-is-debounced.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether all created paths have settled. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that occur before thi

Switch Is Debounced

Indicates whether all created paths have settled.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is debounced

Boolean value that indicates whether all created paths have settled.

| TRUE | All created paths have settled. |
| --- | --- |
| FALSE | The created paths are not settled. |

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-switch-is-scanning.html language=enus -->
## TOPIC 00044: Switch Is Scanning

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-switch-is-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-switch-is-scanning.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the status of the scan. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that occur before this node runs. The

Switch Is Scanning

Indicates the status of the scan.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is scanning

Boolean value that indicates whether the switch module is scanning. The driver returns the value of the Is Scanning property.

| TRUE | The switch module is scanning. |
| --- | --- |
| FALSE | The switch module is not scanning. |

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-wait-for-debounce.html language=enus -->
## TOPIC 00045: Wait For Debounce

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-wait-for-debounce.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-wait-for-debounce.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses until all created paths have settled. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node. error in Error conditions that occur before this nod

Wait For Debounce

Pauses until all created paths have settled.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time

Maximum length of time to wait for all relays in the switch module to activate or deactivate.

If the specified time elapses before all relays activate or deactivate, a timeout error is returned.

Default value: 5,000 (milliseconds)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Call this node before the niSwitch Get Relay Count node to ensure an accurate relay count.

Parent topic:

Channel Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=niswitch-wait-for-scan-to-complete.html language=enus -->
## TOPIC 00046: Wait For Scan To Complete

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `niswitch-wait-for-scan-to-complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/niswitch-wait-for-scan-to-complete.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses until the switch module stops scanning or maximum time has elapsed and returns a timeout error. session in Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize

Wait For Scan To Complete

Pauses until the switch module stops scanning or maximum time has elapsed and returns a timeout error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Control that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time

Maximum length of time to wait for the switch module to stop scanning.

If the specified time elapses before the scan ends, a timeout error is returned.

Default value: 5,000 (milliseconds)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Indicator that identifies a particular NI-SWITCH session established with the niSwitch Initialize With Topology node, the niSwitch Initialize With Options node, or the niSwitch Initialize node and used for all subsequent NI-SWITCH calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scan Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=relay-nodes.html language=enus -->
## TOPIC 00047: Relay Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `relay-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/relay-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SWITCH relay nodes to control and query individual relays of an NI switch.

Relay Nodes

Use the NI-SWITCH relay nodes to control and query individual relays of an NI switch.

Action Nodes

Use the Action nodes to perform Scan, Channel, and Relay actions.

Relay Control

Controls individual relays of the switch module. When controlling individual relays, the protection offered by setting the usage of source channels and configurations channels is void.

Get Relay Position

relay name

Get Relay Count

Returns the number of times the relay has changed from Closed to Open.

Get Relay Name

relay name

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=reset-node.html language=enus -->
## TOPIC 00048: Reset

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `reset-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/reset-node.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the switch to a known state.

Reset

Resets the switch to a known state.

Utility Nodes

Use the NI-SWITCH utility nodes to exercise additional features of an NI switch.

Reset

Disconnects all created paths and returns the switch module to the state at initialization.

Reset With Defaults

Resets the switch module and applies initial user-specified settings from the logical name used to initialize the session. If the session was created without a logical name, this node is equivalent to the niSwitch Reset node.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=scan-nodes.html language=enus -->
## TOPIC 00049: Scan Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `scan-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/scan-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SWITCH scan nodes to configure a scan of an NI switch.

Scan Nodes

Use the NI-SWITCH scan nodes to configure a scan of an NI switch.

Action Nodes

Use the Action nodes to perform Scan, Channel, and Relay actions.

Abort Scan

Aborts the scan in progress. Use the niSwitch Initiate Scan node to initiate an aborted scan.

Commit

Downloads the configured scan list and trigger settings to hardware.

Initiate Scan

Commits the configured scan list and trigger settings to hardware and initiates the scan.

Send Software Trigger

Sends a software trigger to the switch module specified in the NI-SWITCH session.

Switch Is Scanning

Indicates the status of the scan.

Wait For Scan To Complete

maximum time

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=trigger.html language=enus -->
## TOPIC 00050: Trigger Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/trigger.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Trigger nodes to configure triggers for NI-SWITCH.

Trigger Nodes

Use the Trigger nodes to configure triggers for NI-SWITCH.

Configuration Nodes

Use the Configuration nodes to configure the device for scanning.

Configure Scan Trigger

Configures the scan triggers for the scan list established with the niSwitch Configure Scan List node.

Route Scan Advanced Output

x

Route Trigger Input

x

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-switch-lvnxg-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00051: Utility Nodes

- bundle_id: `ni-switch-lvnxg-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-lvnxg-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-switch-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SWITCH utility nodes to exercise additional features of an NI switch.

Utility Nodes

Use the NI-SWITCH utility nodes to exercise additional features of an NI switch.

NI-SWITCH Nodes

Use the nodes on the NI-SWITCH palette to build the block diagram.

Error Message

Converts an error code returned by NI-SWITCH into a user-readable string.

IVI Utilities Nodes

Use the NI-SWITCH IVI Utilities nodes to exercise additional IVI functions of an NI switch.

Reset

Resets the switch to a known state.

Revision Query

Returns the revision of NI-SWITCH.

Self-Test

Verifies that NI-SWITCH can communicate with the switch module.

Parent topic:

NI-SWITCH Nodes
