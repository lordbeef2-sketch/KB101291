# NI DOCUMENT BUNDLE: ni-xnet-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-xnet-lvnxg-api-ref start=1 end=125 -->
<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=ni-xnet-node-reference.html language=enus -->
## TOPIC 00001: NI-XNET Nodes

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `ni-xnet-node-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/ni-xnet-node-reference.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: These topics describe the NI-XNET nodes.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=ni-xnet-wait.html language=enus -->
## TOPIC 00002: XNET Wait

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `ni-xnet-wait.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/ni-xnet-wait.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for an event to occur.

XNET Wait

Waits for an event to occur.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Transmit Complete

Waits for previously written data to be transmitted on the cluster.

Interface Communicating

Waits for the interface to begin communication on the cluster.

CAN Remote Wakeup

Waits for the CAN interface to wake up due to activity by a remote ECU on the network.

Ethernet Synced

Waits for the Ethernet interface to synchronize time on the network.

LIN Remote Wakeup

Waits for the LIN interface to wake up due to activity by a remote ECU on the network.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-blink.html language=enus -->
## TOPIC 00003: XNET Blink

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-blink.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-blink.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Blinks LEDs for the XNET interface to identify its physical port in the system. interface in The XNET Interface I/O name. modifier An input that controls LED blinking. Disable (0) Disable blinking for identification. This option turns off both LEDs for the port. Enable (1) Enable blinking for identi

XNET Blink

Blinks LEDs for the XNET interface to identify its physical port in the system.

[IMAGE alt='1378' src='XNET_Blink.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface in

The XNET Interface I/O name.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### modifier

An input that controls LED blinking.

| Disable (0) | Disable blinking for identification. This option turns off both LEDs for the port. |
| --- | --- |
| Enable (1) | Enable blinking for identification. Both LEDs of the interface’s physical port turn on and off. The hardware blinks the LEDs automatically until you disable, so there is no need to call XNET Blink repetitively. |

Both LEDs blink green (not red). The blinking rate is approximately three times per second.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### interface out

An output that is the same as interface in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Each XNET device contains one or two physical ports. Each port is labeled on the hardware as 
 *Port 1* or 
 *Port 2*. The XNET device also provides two LEDs per port. For a two-port board, LEDs 1 and 2 are assigned to Port 1, and LEDs 3 and 4 are assigned to physical Port 2.

When your application uses multiple XNET devices, this node helps to identify each interface to associate its software behavior (LabVIEW code) to its hardware connection (port). Prior to running your XNET sessions, you can call this node to blink the interface LEDs.

For example, if you have a system with three PCI CAN cards, each with two ports, you can use this node to blink the LEDs for interface CAN4, to identify it among the six CAN ports.

The LEDs of each port support two states:

- Identification: Blink LEDs to identify the physical port assigned to the interface.
- In Use: LED behavior that XNET sessions control.

Identification LED State

You can use XNET Blink only in the Identification state. If you call this node while one or more XNET sessions for the interface are open (created), it returns an error, because the port's LEDs are in the In Use state.

In Use LED State

When you create an XNET session for the interface, the LEDs for that physical port transition to the In Use state. If you called XNET Blink previously to enable blinking for identification, that LED behavior no longer applies. The In Use LED state remains until all XNET sessions are cleared. This typically occurs when all LabVIEW nodes are no longer running. The patterns that appear on the LEDs while In Use are documented in LEDs.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-close.html language=enus -->
## TOPIC 00004: XNET Close

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-close.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears (closes) the XNET session. session in The session to clear. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error

XNET Close

Clears (closes) the XNET session.

[IMAGE alt='1378' src='XNET_Close.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to clear. This session is selected from the LabVIEW project or returned from XNET Create Session.

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

#### Description

This node stops communication for the session and releases all resources the session uses. XNET Close internally calls XNET Stop with normal scope, so if this is the last session using the interface, communication stops.

When your application is finished (the top-level node is idle), LabVIEW automatically clears all XNET sessions within that node and its leaf nodes. Therefore, XNET Close is rarely needed in your application.

You typically use XNET Close when you need to clear the existing session to create a new session that uses the same objects. For example, if you create a session for a frame named 
 *frameA* using Frame Output Single-Point mode, then you create a second session for 
 *frameA* using Frame Output Queued mode, the second call to XNET Create Session returns an error, because 
 *frameA* can be accessed using only one output mode. If you call XNET Clear before the second XNET Create Session call, you can close the previous use of 
 *frameA* to create the new session.

This node disconnects terminals that you connected using the XNET Connect Terminals node.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-connect-terminals.html language=enus -->
## TOPIC 00005: XNET Connect Terminals

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-connect-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-connect-terminals.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects terminals on the XNET interface. session in The session to use for the connection. This session is selected from the LabVIEW project or returned from XNET Create Session. source terminal The connection source. destination terminal The connection destination. error in Error conditions that o

XNET Connect Terminals

Connects terminals on the XNET interface.

[IMAGE alt='1378' src='XNET_Connect_Terminals.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for the connection. This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source terminal

The connection source.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### destination terminal

The connection destination.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A duplicate of session in, provided for simpler wiring.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node connects a source terminal to a destination terminal on the interface hardware. The XNET terminal represents an external or internal hardware connection point on a National Instruments XNET hardware product. External terminals include PXI_Trigger lines for a PXI card, RTSI terminals for a PCI card, or the single external terminal for a C Series module. Internal terminals include timebases (clocks) and logical entities such as a start trigger.

The terminal inputs use the XNET Terminal I/O name, so you can select from possible values using the drop-down list. Typically, one of the pair is an internal and the other an external.

Valid Combinations of Source/Destination

The following table lists all valid combinations of source terminal and destination terminal.

| Source | Destination |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| PXI_Trigx | FrontPanel0 FrontPanel1 | Start Trigger | MasterTimebase | Log Trigger |  |
| PXI_Trigx | X | X | ✓ | ✓ | ✓ |
| FrontPanel0 FrontPanel1 | X | X | ✓ | ✓ | ✓ |
| PXI_Star 1 | X | X | ✓ | X | X |
| PXI_Clk10 1 | X | X | X | ✓ | X |
| StartTrigger | ✓ | ✓ | X | X | X |
| CommTrigger | ✓ | ✓ | X | X | X |
| FlexRayStartCycle 2 | ✓ | ✓ | X | X | X |
| FlexRayMacrotick 2 | ✓ | ✓ | X | ✓ | X |
| 1MHzTimebase | ✓ | ✓ | X | X | X |
| 10MHzTimebase | ✓ | X | X | X | X |
| 1Valid only on PXI hardware. 2Valid only on FlexRay hardware. |  |  |  |  |  |

Source Terminals

The following table describes the valid source terminals.

| Source Terminal | Description |
| --- | --- |
| PXI_Trigx | Selects a general-purpose trigger line as the connection source (input), where x is a number from 0 to 7. For PCI cards, these are the RTSI lines. For PXI cards, these are the PXI Trigger lines. For C Series modules in a CompactDAQ chassis, all modules in the chassis automatically share a common timebase. For information about routing the StartTrigger for CompactDAQ, refer to the XNET Session Interface:Source Terminal:Start Trigger property. |
| FrontPanel0 FrontPanel1 | Selects a general-purpose Front Panel Trigger line as the connection source (input). |
| PXI_Star | Selects the PXI star trigger signal. Within a PXI chassis, some PXI products can source star trigger from Slot 2 to all higher-numbered slots. PXI_Star enables the PXI XNET hardware to receive the star trigger when it is in Slot 3 or higher. Note You cannot use this terminal with a PCI device. |
| PXI_Clk10 | Selects the PXI 10 MHz backplane clock. The only valid destination terminal for this source is MasterTimebase. This routes the 10 MHz PXI backplane clock for use as the XNET card timebase. When you use PXI_Clk10 as the XNET card timebase, you also must use PXI_Clk10 as the timebase for other PXI cards to perform synchronized input/output. Note You cannot use this terminal with a PCI device. |
| StartTrigger | Selects the start trigger, which is the event set when the Start Interface transition occurs. The start trigger is the same for all sessions using a given interface. You can route the start trigger of this XNET card to the start trigger of other XNET or DAQ cards to ensure that sampling begins at the same time on both cards. For example, you can synchronize two XNET cards by routing StartTrigger as the source terminal on one XNET card and then routing StartTrigger as the destination terminal on the other XNET card, with both cards using the same PXI Trigger line for the connections. |
| CommTrigger | Selects the communicating trigger, which is the event set when the Comm State Communicating transition occurs. The communicating trigger is the same for all sessions using a given interface. You can route the communicating trigger of this XNET card to the start trigger of other XNET or DAQ cards to ensure that sampling begins at the same time on both cards. The communicating trigger is similar to a start trigger, but is used if your clock source is the FlexRayMacrotick, which is not available until the interface is properly integrated into the bus. Because you cannot generate a start trigger to another interface until the synchronization clock is also available, you can use this trigger to allow for the clock under this special circumstance. |
| FlexRayStartCycle | Selects the FlexRay Start of Cycles as an advanced trigger source. This generates a repeating pulse that external hardware can use to synchronize a measurement or other action with each FlexRay cycle. Note You can use this terminal only with a FlexRay device. |
| FlexRayMacrotick | Selects the FlexRay Macrotick as a timing source. The FlexRay Macrotick is the basic unit of time in a FlexRay network. You can use this source terminal to synchronize other measurements to the actual time on the FlexRay bus. In this scenario, you would configure the FlexRayMacrotick as the source terminal and route it to a PXI Trigger or front panel terminal. After the interface is communicating to the FlexRay network, the Macrotick signal becomes available. You also can connect the FlexRayMacrotick to the MasterTimebase. This configures the counter that timestamps received frames to run synchronized to FlexRay time, and also allows you to read the FlexRay cycle macrotick to do additional synchronization with the FlexRay bus in your application. Note You can use this terminal only with a FlexRay device. |
| 1MHzTimebase | Selects the XNET card's local 1 MHz oscillator. The only valid destination terminals for this source are PXI_Trig0–PXI_Trig7. This source terminal routes the XNET card local 1 MHz clock so that other NI cards can use it as a timebase. For example, you can synchronize two XNET cards by connecting 1MHzTimebase to PXI_Trigx on one XNET card and then connecting PXI_Trigx to MasterTimebase on the other XNET card. |
| 10MHzTimebase | Selects the XNET card's local 10 MHz oscillator. This routes the XNET card local 10 MHz clock for use as a timebase by other NI cards. For example, you can synchronize two XNET cards by connecting 10MHzTimebase to PXI_Trigx on one XNET card and then connecting PXI_Trigx to MasterTimebase on the other XNET card. |

Destination Terminals

The following table describes the valid destination terminals.

| Destination Terminal | Description |
| --- | --- |
| PXI_Trigx | Selects a general-purpose trigger line as the connection destination (output), where x is a number from 0 to 7. For PCI cards, these are the RTSI lines. For PXI cards, these are the PXI Trigger lines. For C Series modules in a CompactDAQ chassis, all modules in the chassis automatically share a common timebase. For information about routing the StartTrigger for CompactDAQ, refer to the XNET Session Interface:Source Terminal:Start Trigger property. Caution NI-XNET does not automatically reserve PXI trigger lines. Driving the same line from two devices may cause hardware damage. Before configuring a PXI trigger line as a destination terminal, reserve it through the PXI chassis properties in NI Measurement & Automation Explorer. |
| FrontPanel0 FrontPanel1 | Selects a general-purpose Front Panel Trigger line as the connection destination (output). |
| StartTrigger | Selects the start trigger, which is the event that allows the interface to begin communication. The start trigger occurs on the first source terminal low-to-high transition. The start trigger is the same for all sessions using a given interface. This causes the Start Interface transition to occur. You can route the start trigger of another XNET or DAQ card to ensure that sampling begins at the same time on both cards. For example, you can synchronize with an M-Series DAQ MIO card by routing the AI start trigger of the MIO card to a RTSI line and then routing the same PXI Trigger line with StartTrigger as the destination terminal on the XNET card. The default (disconnected) state of this destination means the start trigger occurs when XNET Start is invoked with the scope set to either Normal or Interface Only. Alternately, if Auto Start? is enabled, reading or writing to a session may start the interface. |
| MasterTimebase | MasterTimebase instructs the XNET card to use the connection source terminal as the master timebase. The XNET card uses this master timebase for input sampling (including timestamps of received messages) as well as periodic output sampling. Your XNET hardware supports incoming frequencies of 1 MHz, 10 MHz, and 20 MHz, and automatically detects the frequency without any additional configuration. For example, you can synchronize a CAN and DAQ M Series MIO card by connecting the 10 MHz oscillator (board clock) of the DAQ card to a PXI_Trig line, and then connecting the same PXI_Trig line as the source terminal. For PXI and PXI Express form factor hardware, you also can use PXI_Clk10 as the source terminal. This receives the PXI 10 MHz backplane clock for use as the master timebase. MasterTimebase applies separately to each port of a multiport XNET card, meaning you could run each port off of a separate incoming (or onboard) timebase signal. If you are using a PCI board, the default connection to the MasterTimebase is the local oscillator. If you are using a PXI or PXI Express board, the default connection to the MasterTimebase is the PXI_Clk10 signal, if it is available. Some chassis allow PXI_Clk10 to be turned off. In this case, the hardware automatically uses the local oscillator as the default MasterTimebase. |
| Log Trigger | The Log Trigger terminal generates a frame when it detects a rising edge. When connected, this frame is transferred into the Frame Stream Input session's queue if the session is started. |

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-frame-can-to-signal.html language=enus -->
## TOPIC 00006: Frame CAN to Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-frame-can-to-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-frame-can-to-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET CAN frame data and signals. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. frame data An input that provides the array of LabVIEW clusters. Each array element corresponds to a frame value to convert. Ea

Frame CAN to Signal

Converts between NI-XNET CAN frame data and signals.

[IMAGE alt='1378' src='XNET_Convert_(Frame_CAN_to_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### frame data

An input that provides the array of LabVIEW clusters.

Each array element corresponds to a frame value to convert.

The data you write is converted to signal values in the order you provide them. Only the latest signal value is returned.

The elements of each cluster are specific to the CAN protocol.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### identifier

The CAN frame arbitration identifier.

extended?

extended?

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### extended?

A Boolean value that determines whether the identifier uses extended format (true) or standard format (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

An element not used for conversion. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### type

The frame type (decimal value in parentheses).

| CAN Data (0) | The CAN data frame contains payload data. This is the most commonly used frame type for CAN. |
| --- | --- |
| CAN Remote (1) | A CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using XNET Read. This value is not meaningful, as a remote frame does not contain any data to convert. |

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

An element that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for the CAN data frame.

For more information, refer to the section for each mode.

For a transmitted remote frame (CAN Remote type), the payload length in the frame value specifies the number of payload bytes requested. Your application provides this payload length by filling payload with the requested number of bytes. This enables your application to specify the frame payload length, but the actual values in the payload bytes are ignored (not contained in the transmitted frame).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### signal data

An output that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data returns the most recent converted value for each signal. If multiple frames for a signal are input, only signal data from the most recent frame is returned. Here, most recent is defined by the order of the frames in the frame data array, not the timestamp.

If no frame is input for the corresponding signals, the XNET Signal Default Value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-frame-flexray-to-signal.html language=enus -->
## TOPIC 00007: Frame FlexRay to Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-frame-flexray-to-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-frame-flexray-to-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET FlexRay frame data and signals. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. frame data Provides the array of LabVIEW clusters. Each array element corresponds to a frame value to convert. Each array e

Frame FlexRay to Signal

Converts between NI-XNET FlexRay frame data and signals.

[IMAGE alt='1378' src='XNET_Convert_(Frame_FlexRay_to_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### frame data

Provides the array of LabVIEW clusters.

Each array element corresponds to a frame value to convert.

The data you write is converted to signal values in the order you provide them. Only the latest signal value is returned.

The elements of each cluster are specific to the FlexRay protocol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### slot

A parameter that specifies the slot number within the FlexRay cycle.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### cycle count

A parameter that specifies the cycle number.

The FlexRay cycle count increments from 0 to 63, then rolls over back to 0.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### startup?

A Boolean value that specifies whether the frame is a startup frame (true) or not (false). This field is ignored for conversion.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### sync?

A Boolean value that specifies whether the frame is a sync frame (true) or not (false). This field is ignored for conversion.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### preamble?

A Boolean value that specifies the value of the payload preamble indicator in the frame header.

preamble?

If the frame is in the dynamic segment, preamble? being true indicates the presence of a message ID at the beginning of the payload. The message ID is always 2 bytes in length.

If preamble? is false, the payload does not contain a network management vector or a message ID.

This field is ignored for conversion.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### chA

A Boolean value that specifies whether the frame was received on channel A (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### chB

A Boolean value that specifies whether to transmit the frame on channel B (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

An element not used for conversion. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### type

The frame type.

type

FlexRay Data

FlexRay Data

The FlexRay Null type is not transmitted based on this type. As specified in the XNET Frame FlexRay:Timing Type property, the FlexRay null frame is transmitted when a cyclically timed frame does not have new data.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

An element that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for FlexRay frames of type FlexRay Data.

You can leave all other FlexRay frame cluster elements uninitialized. For more information, refer to the section for each mode.

The XNET Convert (Frame FlexRay to Signal) node uses the following fields to identify a FlexRay frame:

- slot
- cycle count
- chA/chB

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### signal data

An output that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data returns the most recent converted value for each signal. If multiple frames for a signal are input, only signal data from the most recent frame is returned. Here, most recent is defined by the order of the frames in the frame data array, not the timestamp.

If no frame is input for the corresponding signals, the XNET Signal Default Value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-frame-lin-to-signal.html language=enus -->
## TOPIC 00008: Frame LIN to Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-frame-lin-to-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-frame-lin-to-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET LIN frame data and signals. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. frame data An input that provides the array of LabVIEW clusters. Each array element corresponds to a frame value to convert. Ea

Frame LIN to Signal

Converts between NI-XNET LIN frame data and signals.

[IMAGE alt='1378' src='XNET_Convert_(Frame_LIN_to_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### frame data

An input that provides the array of LabVIEW clusters.

Each array element corresponds to a frame value to convert.

The data you write is converted to signal values in the order you provide them. Only the latest signal value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### identifier

An element not used for transmit. You must set this element to 0.

Each frame is identified based on the list of frames or signals provided for the session. The actual identifier to transmit is taken from the database (frame and schedule properties). Therefore, this identifier in the frame value is ignored.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### event slot?

An element not used for transmit. You must set this element to false.

The currently running schedule is used to map the specific frame to a corresponding schedule entry (slot). The schedule entry itself determines whether the slot is unconditional, sporadic, or event triggered.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### event ID

An element not used for transmit. You must set this element to 0.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

An element not used for conversion. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### type

The frame type.

| LIN Data (64) | The LIN data frame contains payload data. This is currently the only frame type for LIN. |
| --- | --- |

This value is ignored for conversion.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

An element that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for a LIN data frame.

For more information, refer to the section for each mode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### signal data

An output that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data returns the most recent converted value for each signal. If multiple frames for a signal are input, only signal data from the most recent frame is returned. Here, most recent is defined by the order of the frames in the frame data array, not the timestamp.

If no frame is input for the corresponding signals, the XNET Signal Default Value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-frame-raw-to-signal.html language=enus -->
## TOPIC 00009: Frame Raw to Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-frame-raw-to-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-frame-raw-to-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET raw frame data and signals. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. frame data An input that provides the array of bytes, representing frames to transmit. The raw bytes encode one or more frames

Frame Raw to Signal

Converts between NI-XNET raw frame data and signals.

[IMAGE alt='1378' src='XNET_Convert_(Frame_Raw_to_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### frame data

An input that provides the array of bytes, representing frames to transmit.

This frame format is the same for read and write of raw data and also is used for log file examples.

For information about which elements of the raw frame are applicable, refer to the XNET Convert instance for the protocol in use (XNET Convert (Frame CAN to Signal), XNET Convert (Frame FlexRay to Signal), or XNET Convert (Frame LIN to Signal)).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### signal data

An output that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data returns the most recent converted value for each signal. If multiple frames for a signal are input, only signal data from the most recent frame is returned. Here, most recent is defined by the order of the frames in the frame data array, not the timestamp.

If no frame is input for the corresponding signals, the XNET Signal Default Value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-signal-to-frame-can.html language=enus -->
## TOPIC 00010: CAN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-signal-to-frame-can.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-signal-to-frame-can.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET signals and CAN frame data. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. signal data An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

CAN

Converts between NI-XNET signals and CAN frame data.

[IMAGE alt='1378' src='XNET_Convert_(Signal_to_Frame_CAN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### signal data

An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data provides the value for the next conversion of each signal.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### frame data

An output that returns the array of LabVIEW clusters.

The elements of each cluster are specific to the CAN protocol.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### identifier

The CAN frame arbitration identifier.

extended?

If extended? is true, the identifier uses extended format, so 29 bits of this identifier are valid.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### extended?

A Boolean value that determines whether the identifier uses extended format (true) or standard format (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false). For conversion, it is always set to false.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type.

| CAN Data (0) | The CAN data frame contains payload data. This is the most commonly used frame type for CAN. When the session is in ISO CAN FD mode, the CAN type is more specific according to the CAN I/O mode of the frame in the database (one of the types listed below). |
| --- | --- |
| CAN 2.0 Data (8) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the CAN 2.0 standard. |
| CAN FD Data (16) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the CAN FD standard. |
| CAN FD+BRS Data (24) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the CAN FD+BRS standard. |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

An element that represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for the CAN data frame.

For a received remote frame (type of CAN Remote), the payload length in the frame value specifies the number of payload bytes requested. This payload length is provided to your application by filling payload with the requested number of bytes. Your application can use the payload array size, but you must ignore the actual values in the payload bytes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-signal-to-frame-flexray.html language=enus -->
## TOPIC 00011: FlexRay

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-signal-to-frame-flexray.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-signal-to-frame-flexray.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET signals and FlexRay frame data. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. signal data An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating po

FlexRay

Converts between NI-XNET signals and FlexRay frame data.

[IMAGE alt='1378' src='XNET_Convert_(Signal_to_Frame_FlexRay).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### signal data

An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data provides the value for the next conversion of each signal.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### frame data

Returns the array of LabVIEW clusters.

The elements of each cluster are specific to the FlexRay protocol.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### Slot

This element specifies the slot number within the FlexRay cycle.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### cycle count

An element that specifies the cycle number.

The FlexRay cycle count increments from 0 to 63, then rolls over back to 0.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### startup?

A Boolean value that specifies whether the frame is a startup frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sync?

A Boolean value that specifies whether the frame is a sync frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### preamble?

A Boolean value that specifies the value of the payload preamble indicator in the frame header.

preamble?

If the frame is in the dynamic segment, preamble? being true indicates the presence of a message ID at the beginning of the payload. The message ID is always 2 bytes in length.

If preamble? is false, the payload does not contain a network management vector or a message ID.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### chA

A Boolean value that specifies whether the frame was received on channel A (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### chB

A Boolean value that specifies whether the frame was received on channel B (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false).

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type.

| FlexRay Data (32) | FlexRay data frame. The frame contains payload data. This is the most commonly used frame type for FlexRay. All elements in the frame are applicable. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

An element that represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for FlexRay frames of type FlexRay Data or FlexRay Null.

According to the FlexRay protocol, this length range is 0-254.

XNET Convert (Signal to Frame FlexRay) writes the FlexRay frame identification to the following fields:

- slot
- cycle count
- chA/chB

In addition, the following fields are set to their database definition:

- startup?
- sync?
- preamble?

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-signal-to-frame-lin.html language=enus -->
## TOPIC 00012: LIN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-signal-to-frame-lin.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-signal-to-frame-lin.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET signals and LIN frame data. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. signal data An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

LIN

Converts between NI-XNET signals and LIN frame data.

[IMAGE alt='1378' src='XNET_Convert_(Signal_to_Frame_LIN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### signal data

An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data provides the value for the next conversion of each signal.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### frame data

Returns the array of LabVIEW clusters.

The elements of each cluster are specific to the LIN protocol.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### identifier

The identifier received within the frame's header.

If the schedule entry (slot) is unconditional or sporadic, this identifies the payload data (LIN frame). If the schedule entry is event triggered, this identifies the schedule entry itself, and the protected ID contained in the first payload byte identifies the payload.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### event slot?

This element is not used. This element is false.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### event ID

This element is not used. This element is 0.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false). For conversion, it is always set to false.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type.

| LIN Data (64) | The LIN data frame contains payload data. This is currently the only frame type for LIN. |
| --- | --- |

For conversion, this is always set to false.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

An element that represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for the LIN data frame.

According to the LIN protocol, this payload is 0-8 bytes in length.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert-signal-to-frame-raw.html language=enus -->
## TOPIC 00013: Raw

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert-signal-to-frame-raw.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert-signal-to-frame-raw.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET signals and raw frame data. session in The session to read. This session is returned from XNET Create Session. The session mode must be Conversion. signal data An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

Raw

Converts between NI-XNET signals and raw frame data.

[IMAGE alt='1378' src='XNET_Convert_(Signal_to_Frame_Raw).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read. This session is returned from XNET Create Session. The session mode must be Conversion.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### signal data

An input that returns a one-dimensional array of signal values. Each signal value is scaled, 64-bit floating point.

The data provides the value for the next conversion of each signal.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### frame data

An output that returns an array of bytes.

This frame format is the same for read and write of raw data, and it is also used for log file examples.

The data always returns complete frames.

For information about which elements of the raw frame are applicable, refer to the frame read for the protocol in use (XNET Convert (Signal to Frame CAN), XNET Convert (Signal to Frame FlexRay), or XNET Convert (Signal to Frame LIN)).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Convert

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-convert.html language=enus -->
## TOPIC 00014: XNET Convert

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-convert.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-convert.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts between NI-XNET signal data and frame data or vice versa.

XNET Convert

Converts between NI-XNET signal data and frame data or vice versa.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Frame CAN to Signal

Converts between NI-XNET CAN frame data and signals.

Frame FlexRay to Signal

Converts between NI-XNET FlexRay frame data and signals.

Frame LIN to Signal

Converts between NI-XNET LIN frame data and signals.

Frame Raw to Signal

Converts between NI-XNET raw frame data and signals.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-conversion.html language=enus -->
## TOPIC 00015: Conversion

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-conversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-conversion.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Conversion Mode. signal list The array of XNET signals to convert to or from frames. These signals are specified in your database and describe the values encoded in one or more frames. error in Error conditions that occur before this node runs. The node re

Conversion

Creates an XNET session at run time for the Conversion Mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Conversion).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET signals to convert to or from frames.

These signals are specified in your database and describe the values encoded in one or more frames.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-input-queued.html language=enus -->
## TOPIC 00016: Queued

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-input-queued.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-input-queued.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Input Queued mode. frame The XNET Frame to read. This mode supports only one frame per session. Your database specifies this frame. interface The XNET Interface to use for this session. error in Error conditions that occur before this node runs. The

Queued

Creates an XNET session at run time for the Frame Input Queued mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Input_Queued).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame

The XNET Frame to read.

This mode supports only one frame per session. Your database specifies this frame.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-input-single-point.html language=enus -->
## TOPIC 00017: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-input-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-input-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Input Single-Point mode. frame list The array of XNET Frames to read. Your database specifies these frames. interface The XNET Interface to use for this session. error in Error conditions that occur before this node runs. The node responds to this in

Single-Point

Creates an XNET session at run time for the Frame Input Single-Point mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Input_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### frame list

The array of XNET Frames to read.

Your database specifies these frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-input-stream.html language=enus -->
## TOPIC 00018: Stream

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-input-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-input-stream.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Input Stream mode. cluster The XNET Cluster I/O Name to use for interface configuration. The default value is :memory:, the in-memory database. There are six options: Empty in-memory database:cluster is unwired, and the in-memory database is empty (X

Stream

Creates an XNET session at run time for the Frame Input Stream mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Input_Stream).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster

The XNET Cluster I/O Name to use for interface configuration.

:memory:

There are six options:

- Empty in-memory database: cluster is unwired, and the in-memory database is empty (XNET Database Create Object is not used). This option is supported for CAN only (not FlexRay or LIN). After you create the session, you must set the XNET Session Interface:64bit Baud Rate property using a Session node. You must set the baud rate prior to starting the session.
- Pre-defined CAN FD in-memory database: Pass in special in-memory databases :can_fd: and :can_fd_brs:, as the cluster (XNET Database Create Object is not used). These databases are similar to the empty in-memory database (:memory:), but configure the cluster in either CAN FD or CAN FD+BRS mode, respectively. After you create the session, you must set the XNET Session Interface:64bit Baud Rate and Interface:CAN:64bit FD Baud Rate properties using a Session node. You must set these baud rates prior to starting the session.
- Pre-defined SAE J1939 Database: Pass in the special in-memory database :can_j1939:. This database is similar to the empty in-memory database (:memory:), but configures the cluster in CAN SAE J1939 application protocol mode. After you create the session, you must set the XNET Session Interface:64bit Baud Rate property using a Session node. You must set this baud rate prior to starting the session.
- Cluster within database file: cluster specifies a cluster within a database file. This is the most common option used with FlexRay. The cluster within the FIBEX database file contains all required properties to configure the interface. For CANdb files, although the file itself does not specify a CAN baud rate, you provide this when you add an alias to the file within NI-XNET. For LIN, the LDF file format already specifies the baud rate.
- Nonempty in-memory database: Call XNET Database Create Object to create a cluster within the in-memory database, use the XNET Cluster property node to set properties (such as baud rate), then wire from the Cluster node to this cluster.
- Subordinate: Wire in cluster of :subordinate: . A subordinate session uses the cluster and interface configuration from other sessions. For example, you may have a test application with which the end user specifies the database file, cluster, and signals to read/write. You also have a second application with which you want to log all received frames (input stream), but that application does not specify a database. You run this second application using a subordinate session, meaning it does not configure or start the interface, but depends on the primary test application. For a subordinate session, start and stop of the interface (using XNET Start) is ignored. The subordinate session reads frames only when another nonsubordinate session starts the interface.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-output-pdu-queued.html language=enus -->
## TOPIC 00019: Queued

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-output-pdu-queued.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-output-pdu-queued.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Output Queued mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Write for the session, and access the payload array only. PDU The XNET PDU to read. This mode supports only one PDU per session. Your

Queued

Creates an XNET session at run time for the Frame Output Queued mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Write for the session, and access the payload array only.

[IMAGE alt='1378' src='XNET_Create_Session_(PDU_Output_Queued).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU

The XNET PDU to read.

This mode supports only one PDU per session. Your database specifies this PDU.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-output-pdu-single-point.html language=enus -->
## TOPIC 00020: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-output-pdu-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-output-pdu-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Output Single-Point mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Write for the session, and access the payload array only. PDU list The array of XNET PDUs to read. Your database specifies thes

Single-Point

Creates an XNET session at run time for the Frame Output Single-Point mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Write for the session, and access the payload array only.

[IMAGE alt='1378' src='XNET_Create_Session_(PDU_Output_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### PDU list

The array of XNET PDUs to read.

Your database specifies these PDUs.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-output-queued.html language=enus -->
## TOPIC 00021: Queued

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-output-queued.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-output-queued.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Output Queued mode. frame The XNET Frame to write. This mode supports only one frame per session. Your database specifies this frame. interface The XNET Interface to use for this session. error in Error conditions that occur before this node runs. Th

Queued

Creates an XNET session at run time for the Frame Output Queued mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Output_Queued).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame

The XNET Frame to write.

This mode supports only one frame per session. Your database specifies this frame.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-output-single-point.html language=enus -->
## TOPIC 00022: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-output-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-output-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Output Single-Point mode. frame list The array of XNET Frames to write. Your database specifies these frames. interface The XNET Interface to use for this session. error in Error conditions that occur before this node runs. The node responds to this

Single-Point

Creates an XNET session at run time for the Frame Output Single-Point mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Output_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### frame list

The array of XNET Frames to write.

Your database specifies these frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-frame-output-stream.html language=enus -->
## TOPIC 00023: Stream

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-frame-output-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-frame-output-stream.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Output Stream mode. This instance is supported for CAN and LIN only (not FlexRay). cluster The XNET Cluster I/O Name to use for interface configuration. The default value is :memory:, the in-memory database. There are five options: Empty in-memory da

Stream

Creates an XNET session at run time for the Frame Output Stream mode. This instance is supported for CAN and LIN only (not FlexRay).

[IMAGE alt='1378' src='XNET_Create_Session_(Frame_Output_Stream).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster

The XNET Cluster I/O Name to use for interface configuration.

:memory:

There are five options:

- Empty in-memory database: cluster is unwired, and the in-memory database is empty (XNET Database Create Object is not used). After you create the session, you must set the XNET Session Interface:Baud Rate property using a Session node. You must set the CAN or LIN baud rate prior to starting the session.
- Pre-defined CAN FD in-memory database: Pass in special in-memory databases :can_fd: and :can_fd_brs:, as the cluster (XNET Database Create Object is not used). These databases are similar to the empty in-memory database (:memory:), but configure the cluster in either CAN FD or CAN FD+BRS mode, respectively. After you create the session, you must set the XNET Session Interface:64bit Baud Rate and Interface:CAN:64bit FD Baud Rate properties using a Session node. You must set these baud rates prior to starting the session.
- Pre-defined SAE J1939 Database: Pass in the special in-memory database :can_j1939:. This database is similar to the empty in-memory database (:memory:), but configures the cluster in CAN SAE J1939 application protocol mode. After you create the session, you must set the XNET Session Interface:64 bit Baud Rate property using a Session node. You must set this baud rate prior to starting the session.
- Cluster within database file: cluster specifies a cluster within a database file. For CANdb files, although the file itself does not specify a CAN baud rate, you provide this when you add an alias to the file within NI-XNET.
- Nonempty in-memory database: Call XNET Database Create Object to create a cluster within the in-memory database, use the Cluster node to set properties (such as baud rate), then wire from the Cluster node to this cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-generic.html language=enus -->
## TOPIC 00024: Generic

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-generic.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-generic.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time using strings instead of XNET I/O names. This node is for advanced applications, when you need to store the configuration as strings (such as within a text file). list Provides the list of signals or frames for the session. The list syntax depends on the mode: Mod

Generic

Creates an XNET session at run time using strings instead of XNET I/O names. This node is for advanced applications, when you need to store the configuration as strings (such as within a text file).

[IMAGE alt='1378' src='XNET_Create_Session_(Generic).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### list

Provides the list of signals or frames for the session.

| Mode | List Syntax |
| --- | --- |
| Signal Input Single-Point, Signal Output Single-Point | list contains one or more XNET Signal names. If more than one name is provided, a comma must separate each name. Each name must use the <signal> or <frame.signal> syntax as specified for the I/O name (new line and <dbSelection> not included). |
| Signal Input Waveform, Signal Output Waveform | list contains one or more XNET Signal names. If more than one name is provided, a comma must separate each name. Each name must use the <signal> or <frame.signal> syntax as specified for the I/O name (new line and <dbSelection> not included). |
| Signal Input XY, Signal Output XY | list contains one or more XNET Signal names. If more than one name is provided, a comma must separate each name. Each name must use the <signal> or <frame.signal> syntax as specified for the I/O name (new line and <dbSelection> not included). |
| Frame Input Stream, Frame Output Stream | list is empty (unwired). |
| Frame Input Queued, Frame Output Queued | list contains only one XNET Frame name. Only one name is supported. The frame name must use the <frame> syntax as specified for the I/O name (new line and <dbSelection> not included). |
| Frame Input Single-Point, Frame Output Single-Point | list contains one or more XNET Frame names. If more than one name is provided, a comma must separate each name. The frame name must use the <frame> syntax as specified for the I/O name (new line and <dbSelection> not included). |

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### mode

The session mode.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### database

The XNET Database to use for interface configuration.

<alias>

<filepath>

:memory:

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### cluster

The XNET Cluster to use for interface configuration.

<cluster>

<alias>.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-pdu-input-queued.html language=enus -->
## TOPIC 00025: Queued

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-pdu-input-queued.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-pdu-input-queued.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Input Queued mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Read for the session, and access the payload array only. PDU The XNET PDU to read. This mode supports only one PDU per session. Your d

Queued

Creates an XNET session at run time for the Frame Input Queued mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Read for the session, and access the payload array only.

[IMAGE alt='1378' src='XNET_Create_Session_(PDU_Input_Queued).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU

The XNET PDU to read.

This mode supports only one PDU per session. Your database specifies this PDU.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-pdu-input-single-point.html language=enus -->
## TOPIC 00026: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-pdu-input-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-pdu-input-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Frame Input Single-Point mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Read for the session, and access the payload array only. PDU list The array of XNET PDUs to read. Your database specifies these

Single-Point

Creates an XNET session at run time for the Frame Input Single-Point mode. This selection uses a PDU to specify the raw data, not a frame. Use the frame selections of XNET Read for the session, and access the payload array only.

[IMAGE alt='1378' src='XNET_Create_Session_(PDU_Input_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### PDU list

The array of XNET PDUs to read.

Your database specifies these PDUs.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-input-single-point.html language=enus -->
## TOPIC 00027: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-input-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-input-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Input Single-Point mode. signal list The array of XNET Signals to read. These signals are specified in your database and describe the values encoded in one or more frames, or they are trigger signals for frames. interface The XNET Interface to use f

Single-Point

Creates an XNET session at run time for the Signal Input Single-Point mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Input_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to read.

These signals are specified in your database and describe the values encoded in one or more frames, or they are trigger signals for frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-input-waveform.html language=enus -->
## TOPIC 00028: Waveform

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-input-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-input-waveform.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Input Waveform mode. signal list The array of XNET Signals to read. These signals are specified in your database and describe the values encoded in one or more frames. interface The XNET Interface to use for this session. error in Error conditions t

Waveform

Creates an XNET session at run time for the Signal Input Waveform mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Input_Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to read.

These signals are specified in your database and describe the values encoded in one or more frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-input-xy.html language=enus -->
## TOPIC 00029: XY

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-input-xy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-input-xy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Input XY mode. signal list The array of XNET Signals to read. These signals are specified in your database and describe the values encoded in one or more frames. interface The XNET Interface to use for this session. error in Error conditions that oc

XY

Creates an XNET session at run time for the Signal Input XY mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Input_XY).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to read.

These signals are specified in your database and describe the values encoded in one or more frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-output-single-point.html language=enus -->
## TOPIC 00030: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-output-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-output-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Output Single-Point mode. signal list The array of XNET Signals to write. These signals are specified in your database and describe the values encoded in one or more frames, or they are trigger signals for frames. interface The XNET Interface to use

Single-Point

Creates an XNET session at run time for the Signal Output Single-Point mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Output_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to write.

These signals are specified in your database and describe the values encoded in one or more frames, or they are trigger signals for frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-output-waveform.html language=enus -->
## TOPIC 00031: Waveform

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-output-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-output-waveform.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Output Waveform mode. signal list The array of XNET Signals to read. These signals are specified in your database and describe the values encoded in one or more frames. interface The XNET Interface to use for this session. error in Error conditions

Waveform

Creates an XNET session at run time for the Signal Output Waveform mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Output_Waveform).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to read.

These signals are specified in your database and describe the values encoded in one or more frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session-signal-output-xy.html language=enus -->
## TOPIC 00032: XY

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session-signal-output-xy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session-signal-output-xy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session at run time for the Signal Output XY mode. signal list The array of XNET Signals to write. These signals are specified in your database and describe the values encoded in one or more frames. interface The XNET Interface to use for this session. error in Error conditions that

XY

Creates an XNET session at run time for the Signal Output XY mode.

[IMAGE alt='1378' src='XNET_Create_Session_(Signal_Output_XY).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dio.png']

##### signal list

The array of XNET Signals to write.

These signals are specified in your database and describe the values encoded in one or more frames.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### interface

The XNET Interface to use for this session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The created session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Create Session

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-session.html language=enus -->
## TOPIC 00033: XNET Create Session

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-session.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an XNET session to read/write data on the network.

XNET Create Session

Creates an XNET session to read/write data on the network.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Conversion

Creates an XNET session at run time for the Conversion Mode.

Generic

Creates an XNET session at run time using strings instead of XNET I/O names. This node is for advanced applications, when you need to store the configuration as strings (such as within a text file).

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-create-timing-source-flexray-cycle.html language=enus -->
## TOPIC 00034: XNET Create Timing Source (FlexRay Cycle)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-create-timing-source-flexray-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-create-timing-source-flexray-cycle.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a timing source for a LabVIEW Timed Loop. The timing source is based on the FlexRay communication cycle. The timing source sends a tick to the Timed Loop at a specific offset in time within the FlexRay cycle. The offset within the cycle is specified in FlexRay macroticks. timing source name

XNET Create Timing Source (FlexRay Cycle)

Creates a timing source for a LabVIEW Timed Loop. The timing source is based on the FlexRay communication cycle. The timing source sends a tick to the Timed Loop at a specific offset in time within the FlexRay cycle. The offset within the cycle is specified in FlexRay macroticks.

[IMAGE alt='1378' src='XNET_Create_Timing_Source_(FlexRay_Cycle).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### timing source name

The timing source name, returned as timing source out if this node succeeds.

timing source name

timing source out

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for creating the timing source.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### macrotick offset

The offset within each FlexRay cycle that you want the timing source to tick.

For further recommendations about selecting a value, refer to 
 *Macrotick Offset* on the 
 Details tab.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### timing source out

The timing source name. You wire this name to the Source Name of the input node outside the Timed Loop.

Using the Timed Loop

Details

If this node returns an error (status true in error out), timing source out is empty, which indicates to the Timed Loop that no valid timing source exists.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Use this node to synchronize your LabVIEW Real-Time application to the deterministic FlexRay cycle. Because the FlexRay cycle repeats every few milliseconds, real-time execution is required, and therefore this node is not supported on Windows.

You can create only one FlexRay Cycle timing source for each FlexRay interface. You can wire a single timing source to multiple Timed Loops.

The following sections include more detailed information about using this node.

Using the Timed Loop

This section includes guidelines for using the LabVIEW Timed Loop with the NI-XNET FlexRay Cycle timing source. For complete information, refer to the LabVIEW help topics for the Timed Loop.

The Timed Loop contains the nodes described below.

[IMAGE alt='1378' src='GUID-8D277744-AE6B-4761-8896-8D2E0AF438D3-a5.png']

1. Input Node
2. Left Data Node
3. Right Data Node
4. Output Node

Input Node

Source Name: Wire the 
 timing source name output of this node to this terminal on the Timed Loop input node. This specifies the XNET timing source and overrides the default built-in timing source (1 kHz).

Period: For most applications, you wire the constant 1 to this terminal, which overrides the default of 1000. The 
 Period specifies the number of timing source ticks that must occur for the loop to iterate. A value of 1 iterates the Timed Loop on every FlexRay cycle. Higher values skip FlexRay cycles (for example, 2 iterates the loop every other FlexRay cycle).

Timeout: For most applications, you wire the constant 300 to this terminal, which overrides the default of -1. The 
 Timeout specifies the maximum number of milliseconds to wait for a tick. For this FlexRay cycle timing source, this timeout primarily applies to the first loop iteration. According to the FlexRay specification, the process of fully synchronizing the distributed network clocks can take as long as 200 ms. This network clock synchronization is required for the NI-XNET interface to detect the first FlexRay cycle and send a tick to the Timed Loop. If network communication problems occur (for example, noise on the cable), the first tick does not occur. Using a value of 300 for this terminal ensures that if problems occur on the FlexRay network, the Timed Loop can recover (refer to 
 *Wake-Up Reason* in 
 *Left Data Node*).

Error: Use this terminal to propagate errors through the Timed Loop. The Timed Loop does not execute if this terminal receives an error condition. You typically wire the error out from this XNET Create Timing Source (FlexRay Cycle) node to this terminal. This avoids the need for alternate error propagation techniques, such as a shift register.

Left Data Node

Error: Propagates errors through the structure. Wire this terminal to error in of the first node within the subdiagram.

Wake-Up Reason: If the first Timed Loop iteration encounters a Timeout due to problems on the FlexRay network, this terminal returns a value of 5 (Timeout). When the timeout occurs, the Timed Loop does not return an error condition from Error. The timeout causes the iteration to execute untimed, then try again on the next iteration. If the FlexRay tick occurs as expected, Wake-Up Reason returns a value of 0 (Normal).

Right Data Node

Error: Propagates errors from the subdiagram out of the Timed Loop. If Error receives an error condition, the Timed Loop finishes executing the current iteration untimed, exits the loop, and returns the error condition on the Output Node. If you want the Timed Loop to exit on error, wire error out from the last node in the subdiagram to this terminal.

Output Node

Error: Propagates errors the Timed Loop receives and returns errors from the subdiagram.

Session Start and Stop

When the Timed Loop input node executes, the XNET session for the timing source is started automatically. This auto-start is equivalent to calling XNET Start (Normal). This auto-start is performed even if the session's Auto Start? property is false. Because the Timed Loop uses an execution priority that typically is higher than the nodes that precede it, starting FlexRay communication within the Timed Loop ensures that you do not miss the first FlexRay cycle. Due to these factors, do not call XNET Start prior to the Timed Loop (use the Timed Loop auto-start instead).

After the initial session and interface auto-start, the Timed Loop Timeout is used to wait for communication to begin.

When the Timed Loop exits to its output node, the XNET session remains in its current state. The Timed Loop does not stop or clear the session, so you can continue to use the session in nodes that follow.

Macrotick Offset

To set the macrotick offset, it helps to understand some NI-XNET implementation aspects. When the FlexRay Communication Controller (CC) receives a frame, the NI-XNET hardware immediately transfers that frame to LabVIEW Real-Time (RT). This transfer is performed using DMA (Direct Memory Access) on the PXI backplane, so that it occurs quickly and with negligible jitter to your LabVIEW RT execution.

The following figure shows the effects of this implementation. In this example, the macrotick offset is set to occur at the end of slot 1. The subdiagram in the Timed Loop calls XNET Read to read the value received from slot 1.

For better visibility in these figures, the NI-XNET blocks (Read/Write, DMA I/O, an dCC I/O) are longer than actual performance. When using a PXI controller for LabVIEW Real-Time, your results typically will be faster. This is especially true if your application does not transfer data on the PXI backplane continuously (for example, streaming analog, vision, or TCP/IP data), as this sort of transfer can adversely impact the NI-XNET DMA latencies.

Figure 1.

[IMAGE alt='1378' src='GUID-9DCBC3D7-138F-42E4-9FDC-6D6D4929718D-a5.png']

The preceding figure shows that the DMA input transfer for slot 1 (IN1) occurs at the same time as XNET Read for slot 1 (R1). Depending on which one completes first, XNET Read may return a value from the current cycle (3) or the previous cycle (2).

To prevent this uncertainty, macrotick offset must be large enough to ensure that the frame DMA input is complete. Relative to the preceding figure, setting macrotick offset to the end of slot 2 would suffice.

When your LabVIEW RT application calls XNET Write, the frame values are transferred immediately using DMA. The frame values are transferred to the NI-XNET hardware onboard processor memory. For efficiency reasons, this onboard processor waits until the FlexRay cycle Network Idle Time (NIT) to transfer the frame values from its memory to the FlexRay Communication Controller (CC). The FlexRay Communication Controller transmits each frame value according to its slot configuration in the cycle.

The following figure shows the effects of this implementation. This example expands on the preceding figure by calling XNET Write with a value for slot 8. XNET Write (W8) is called well in advance of slot 8 in the cycle. The DMA output transfer for the value of slot 8 (D8) occurs immediately after XNET Write. Nevertheless, the value for slot 8 is not placed into the FlexRay Communication Controller until the NIT time, shown as C8. This means that although XNET Write was called before slot 8's occurrence in the current cycle 3, that value does not transmit until the subsequent cycle 4.

This implementation for output means that it is not necessarily urgent to call XNET Write before the relevant slot. You merely need to provide time for XNET Write and the related DMA output to complete prior to the NIT.

Figure 2.

[IMAGE alt='1378' src='GUID-251A3CB7-1920-4A1A-8C5F-8CBA929B00CB-a5.png']

Taking these implementation considerations into account, the typical macrotick offset goal is a value that executes the Timed Loop after the last cycle input DMA and prior to the NIT. Ideally, the macrotick offset provides sufficient time for input DMA, XNET Read, LabVIEW code within the Timed Loop (for example, a simulation model), XNET Write, and DMA output.

To find a value for macrotick offset, you can use the XNET Cluster property node. The FlexRay:NIT Start property provides the macrotick offset for the start of NIT, which is your upper limit. To determine the lower limit, the FlexRay:Static Slot property provides the number of macroticks for each static slot. Static slot numbers begin at 1. Assuming static slot X is the last slot that you read, the lower limit for macrotick offset is (X x FlexRay:Static Slot).

The following example demonstrates a technique for calculating macrotick offset. The example uses a simple FlexRay cluster configured as follows:

- Baud Rate —5000000 bps (5 Mbps)
- Macrotick —1 (1 µs duration)
- Macro Per Cycle —1000 (1 ms)
- Number of Static Slots —10
- Number of Minislots —80
- Static Slot —58 MT (16 byte payload)
- NIT Start —900 MT offset
- NIT —100 MT (duration)

Within the Timed Loop, the example does the following:

- Reads a Signal Input Single-Point session for frames in static slots 2, 3, and 4.
- Executes a simulation model (passes in inputs and obtains outputs).
- Writes a Signal Output Single-Point session for frames in static slots 8, 9, and 10.

Assume that you test the simulation model performance and determine that it takes 100 µs (including jitter). Using the cluster configuration and the time required for the simulation model, select a macrotick offset that locates the simulation model at the midpoint between the end of slot 4 (the last input frame) and the start of NIT. This provides the maximum time possible for XNET Read/XNET Write, DMA input/output, and CC input/output.

| EndOfSlot4 | = (4 x Static_Slot) = (4 x 58) = 232 |
| --- | --- |
| Midpoint | = EndOfSlot4 + ((NIT_Start - EndOfSlot4) / 2) = 232 + ((900 - 232) / 2) = 232 + 334 = 566 |
| macrotick offset | = (Midpoint - (SimModelTime / 2)) = (566 - (100 / 2)) = 516 |

The following figure shows the Timed Loop timing diagram. Notice that the simulation model is synchronized deterministically with the FlexRay cycle. The Timed Loop code reads inputs from the current cycle, calculates outputs, and then writes the output for the next cycle.

Figure 3.

[IMAGE alt='1378' src='GUID-9940FE93-2474-4E56-B13E-6BF4066CDAD2-a5.png']

Reading from the FlexRay Communication Controller (and performing the corresponding DMA) for frames 2, 3, and 4 is shown as blocks IN2, IN3, and IN4. XNET Read for frames 2, 3, and 4 is shown as block R2,3,4. The simulation model execution is shown as block SIM. The start of SIM is halfway between the end of slot 4 and the start of NIT. XNET Write for frames 8, 9, and 10 is shown as block W8,9,10. The corresponding DMA output for these frames is shown as block D8,9,10. The FlexRay Communication Controller update during the NIT is shown as block C8,9,10.

As with any performance-sensitive configuration, you should measure using your own hardware and application to calculate the best macrotick offset value. To determine the current cycle and macrotick within the Timed Loop for measurement purposes, use XNET Read (State FlexRay Cycle Macrotick).

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-add-alias.html language=enus -->
## TOPIC 00035: XNET Database Add Alias

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-add-alias.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-add-alias.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new alias to a database file. CAN FD ISO mode An input that sets the way the API processes ISO FD frames. 0 ISO 1 Non-ISO 2 ISO Legacy default FD baud rate An input that sets the default FD baud rate for a CAN database that does not internally specify the FD baud rate. default baud rate An in

XNET Database Add Alias

Adds a new alias to a database file.

[IMAGE alt='1378' src='XNET_Database_Add_Alias.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### CAN FD ISO mode

An input that sets the way the API processes ISO FD frames.

| 0 | ISO |
| --- | --- |
| 1 | Non-ISO |
| 2 | ISO Legacy |

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### default FD baud rate

An input that sets the default FD baud rate for a CAN database that does not internally specify the FD baud rate.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### default baud rate

An input that provides the default baud rate, used when filepath refers to a CANdb database (.dbc) or an NI-CAN database (.ncd).

filepath

.xml

default baud rate

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### ignore application protocol?

An input that is applicable only to a database with a J1939 application protocol, and sets whether the API should ignore the application protocol and process J1939 frames as raw CAN frames (True), or process them as J1939 frames (False).

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### alias

An input that provides the desired alias name.

Unlike the name of other XNET database objects, the alias name can use special characters such as space and dash. Commas are not allowed in the alias name, because XNET Database Get List parses the alias list as a comma-separated list of strings. If the alias name already exists, this node changes the previous filepath to the specified filepath.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### filepath

An input that provides the path to the CANdb, FIBEX, or LDF file. Commas are not allowed in the alias name, because XNET Database Get List parses the alias list as a comma-separated list of strings.

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

#### Description

NI-XNET uses alias names for database files. The alias names provide a shorter name for display and allow for changes to the file system without changing the application.

This node is supported on Windows only.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-cluster.html language=enus -->
## TOPIC 00036: Cluster

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-cluster.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a cluster from a database, or all database objects. cluster in The cluster to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to

Cluster

Closes a cluster from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(Cluster).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a cluster object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-database.html language=enus -->
## TOPIC 00037: Database

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-database.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-database.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an XNET database, or all database objects. database in The database to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to standar

Database

Closes an XNET database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(Database).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### database in

The database to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes an XNET database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Note

close all?

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-ecu.html language=enus -->
## TOPIC 00038: ECU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-ecu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an ECU from a database, or all database objects. ECU in The ECU to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

ECU

Closes an ECU from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(ECU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### ECU in

The ECU to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes an ECU object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-frame.html language=enus -->
## TOPIC 00039: Frame

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-frame.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a frame from a database, or all database objects. frame in The frame to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to standa

Frame

Closes a frame from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(Frame).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame in

The frame to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a frame object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-lin-schedule-entry.html language=enus -->
## TOPIC 00040: Schedule Entry

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-lin-schedule-entry.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-lin-schedule-entry.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a LIN schedule entry from a database, or all database objects. LIN schedule entry in The schedule entry to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node respond

Schedule Entry

Closes a LIN schedule entry from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(LIN_Schedule_Entry).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### LIN schedule entry in

The schedule entry to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a LIN schedule entry object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-lin-schedule.html language=enus -->
## TOPIC 00041: Schedule

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-lin-schedule.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-lin-schedule.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a LIN schedule object from a database, or all database objects. LIN schedule in The schedule to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this i

Schedule

Closes a LIN schedule object from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(LIN_Schedule).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### LIN schedule in

The schedule to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a LIN schedule object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-pdu.html language=enus -->
## TOPIC 00042: PDU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-pdu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-pdu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a PDU from a database, or all database objects. PDU in The PDU to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to standard err

PDU

Closes a PDU from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(PDU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU in

The PDU to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a PDU object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-signal.html language=enus -->
## TOPIC 00043: Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a signal from a database, or all database objects. signal in The signal to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according to sta

Signal

Closes a signal from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### signal in

The signal to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a signal object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close-subframe.html language=enus -->
## TOPIC 00044: Subframe

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close-subframe.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close-subframe.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a subframe from a database, or all database objects. subframe in The subframe to close. close all? An input that indicates that all open database objects will be closed. This is the default. error in Error conditions that occur before this node runs. The node responds to this input according

Subframe

Closes a subframe from a database, or all database objects.

[IMAGE alt='1378' src='XNET_Database_Close_(Subframe).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### subframe in

The subframe to close.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### close all?

An input that indicates that all open database objects will be closed. This is the default.

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

#### Description

This node closes a subframe object from a database (or all database objects). It is an instance of XNET Database Close.

To simplify the task of closing all database objects you opened, you can use the close all? parameter set to true (default); otherwise, only the single database object wired in is closed.

Database objects are closed automatically when the top-level node terminates, so using this node is optional. However, you may want to close database objects to free their memory prior to starting a session. You can use this node to do this.

Parent topic:

XNET Database Close

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-close.html language=enus -->
## TOPIC 00045: XNET Database Close

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-close.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an object from a database, or all database objects.

XNET Database Close

Closes an object from a database, or all database objects.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Cluster

Closes a cluster from a database, or all database objects.

Database

Closes an XNET database, or all database objects.

ECU

Closes an ECU from a database, or all database objects.

Frame

Closes a frame from a database, or all database objects.

PDU

Closes a PDU from a database, or all database objects.

Signal

Closes a signal from a database, or all database objects.

Subframe

Closes a subframe from a database, or all database objects.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-cluster.html language=enus -->
## TOPIC 00046: Cluster

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-cluster.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET cluster. database in The parent database object. database in can be an existing file. You can create a new database in memory by specifying :memory: for database in and create an entire hierarchy of objects in memory, without using a file on the disk. cluster name The name of the

Cluster

Creates a new XNET cluster.

[IMAGE alt='1378' src='XNET_Database_Create_(Cluster).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### database in

The parent database object.

database in

:memory:

database in

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### cluster name

The name of the cluster to create.

Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### database out

A copy of the database in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

The I/O name of the newly created cluster object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET cluster object. It is an instance of XNET Database Create Object.

The cluster name input becomes the Name (Short) property of the created object. This is distinct from the string contained within cluster out, which uses the syntax described in XNET Cluster I/O Name.

The cluster object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-dynamic-signal.html language=enus -->
## TOPIC 00047: Dynamic Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-dynamic-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-dynamic-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET dynamic signal. subframe in The subframe parent object. signal name The name of the signal to create. The name must be unique for all signals in a frame in which the subframe parent was defined, including the static signals and the multiplexer signal. Lowercase letters, uppercase

Dynamic Signal

Creates a new XNET dynamic signal.

[IMAGE alt='1378' src='XNET_Database_Create_(Dynamic_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### subframe in

The subframe parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal name

The name of the signal to create.

The name must be unique for all signals in a frame in which the subframe parent was defined, including the static signals and the multiplexer signal. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### subframe out

A copy of the subframe in parameter. You can use this parameter to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### signal out

The I/O name of the newly created signal object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET dynamic signal object. It is an instance of XNET Database Create Object.

The signal name input becomes the Name (Short) property of the created object. This is distinct from the string contained within signal out, which uses the syntax described in XNET Signal I/O Name.

The signal object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Dynamic Signal is transmitted in the frame when the multiplexer signal contains the multiplexer value defined in the subframe.

In NI-CAN, dynamic signals were called mode-dependent channels.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-ecu.html language=enus -->
## TOPIC 00048: ECU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-ecu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET ECU. cluster in The cluster parent object. ECU name The name of the ECU to create. The name must be unique for all ECUs in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other speci

ECU

Creates a new XNET ECU.

[IMAGE alt='1378' src='XNET_Database_Create_(ECU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### ECU name

The name of the ECU to create.

The name must be unique for all ECUs in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### ECU out

The I/O name of the newly created ECU object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET ECU object. It is an instance of XNET Database Create Object.

The ECU name input becomes the Name (Short) property of the created object. This is distinct from the string contained within ECU out, which uses the syntax described in XNET ECU I/O Name.

The ECU object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-frame.html language=enus -->
## TOPIC 00049: Frame

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-frame.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET frame. cluster in The cluster parent object. frame name The name of the frame to create. The name must be unique for all frames in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and oth

Frame

Creates a new XNET frame.

[IMAGE alt='1378' src='XNET_Database_Create_(Frame).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### frame name

The name of the frame to create.

The name must be unique for all frames in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### frame out

The I/O name of the newly created frame object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET frame object. It is an instance of XNET Database Create Object.

The frame name input becomes the Name (Short) property of the created object. This is distinct from the string contained within frame out, which uses the syntax described in XNET Frame I/O Name.

The frame object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-lin-schedule-entry.html language=enus -->
## TOPIC 00050: Schedule Entry

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-lin-schedule-entry.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-lin-schedule-entry.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET LIN schedule entry object. LIN schedule in The schedule parent object. LIN schedule entry name The name of the schedule entry to create. The name must be unique for all entries in a schedule. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid character

Schedule Entry

Creates a new XNET LIN schedule entry object.

[IMAGE alt='1378' src='XNET_Database_Create_(LIN_Schedule_Entry).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### LIN schedule in

The schedule parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### LIN schedule entry name

The name of the schedule entry to create.

The name must be unique for all entries in a schedule. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### LIN schedule out

A copy of the LIN schedule in parameter. You can use this parameter to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### LIN schedule entry out

The I/O name of the newly created LIN schedule entry object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET schedule entry object. It is an instance of XNET Database Create Object.

Schedule entries is an ordered array in a schedule. The schedule is being processed in the order of this array. A newly created entry always is added to the last position of the array.

The LIN schedule entry name input becomes the Name (Short) property of the created object. This is distinct from the string contained in LIN schedule entry out, which uses the syntax described in XNET LIN Schedule Entry I/O Name.

The schedule entry object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-lin-schedule.html language=enus -->
## TOPIC 00051: Schedule

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-lin-schedule.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-lin-schedule.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET LIN schedule. cluster in The cluster parent object. LIN schedule name The name of the schedule to create. The name must be unique for all schedules in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ),

Schedule

Creates a new XNET LIN schedule.

[IMAGE alt='1378' src='XNET_Database_Create_(LIN_Schedule).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### LIN schedule name

The name of the schedule to create.

The name must be unique for all schedules in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### LIN schedule out

The I/O name of the newly created LIN schedule object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET LIN schedule object. It is an instance of XNET Database Create Object.

The LIN schedule name input becomes the Name (Short) property of the created object. This is distinct from the string contained within LIN schedule out, which uses the syntax described in XNET LIN Schedule I/O Name.

The schedule object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-object.html language=enus -->
## TOPIC 00052: XNET Database Create Object

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-object.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new database object.

XNET Database Create Object

Creates a new database object.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Cluster

Creates a new XNET cluster.

Dynamic Signal

Creates a new XNET dynamic signal.

ECU

Creates a new XNET ECU.

Frame

Creates a new XNET frame.

PDU

Creates a new XNET PDU.

Signal

Creates a new XNET signal.

Subframe

Creates a new XNET subframe.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-pdu-signal.html language=enus -->
## TOPIC 00053: Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-pdu-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-pdu-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a new dynamic signal (signal within a multiplexed PDU). This node selection is the same as XNET Database Create (Dynamic Signal), except that it uses a PDU as the signal's parent, not a frame. PDU in The PDU parent object. signal name The name of the signal to create. Lowercase letters, upper

Signal

Create a new dynamic signal (signal within a multiplexed PDU). This node selection is the same as XNET Database Create (Dynamic Signal), except that it uses a PDU as the signal's parent, not a frame.

[IMAGE alt='1378' src='XNET_Database_Create_(PDU_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU in

The PDU parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal name

The name of the signal to create.

Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### PDU out

The reference to the newly created PDU object.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### signal out

The I/O name of the newly created signal object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET signal object. It is an instance of XNET Database Create Object.

The signal name input becomes the Name (Short) property of the created object. This is distinct from the string contained within signal out, which uses the syntax described in XNET Signal I/O Name.

The signal object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-pdu-subframe.html language=enus -->
## TOPIC 00054: Subframe

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-pdu-subframe.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-pdu-subframe.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a new subframe. This node selection is the same as XNET Database Create (Subframe), except that it uses a PDU as the subframe's parent, not a frame. PDU in The PDU parent object. subframe name The name of the subframe to create. The name must be unique for all subframes in a frame. Lowercase

Subframe

Create a new subframe. This node selection is the same as XNET Database Create (Subframe), except that it uses a PDU as the subframe's parent, not a frame.

[IMAGE alt='1378' src='XNET_Database_Create_(PDU_Subframe).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU in

The PDU parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### subframe name

The name of the subframe to create.

The name must be unique for all subframes in a frame. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### PDU out

A copy of the PDU in parameter. You can use this parameter to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### subframe out

The I/O name of the newly created subframe object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET subframe object. It is an instance of XNET Database Create Object.

The subframe name input becomes the Name (Short) property of the created object.

The subframe object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

A subframe defines the multiplexer value for all dynamic signals in this subframe. Dynamic signals within a subframe inherit the multiplexer value from the subframe parent.

In NI-CAN, a subframe was called a mode.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-pdu.html language=enus -->
## TOPIC 00055: PDU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-pdu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-pdu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET PDU. cluster in The cluster parent object. PDU name The name of the PDU to create. The name must be unique for all PDUs in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other speci

PDU

Creates a new XNET PDU.

[IMAGE alt='1378' src='XNET_Database_Create_(PDU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### PDU name

The name of the PDU to create.

The name must be unique for all PDUs in a cluster. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### PDU out

The reference to the newly created PDU object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET PDU object. It is an instance of XNET Database Create Object.

The PDU name input becomes the Name (Short) property of the created object. This is distinct from the string contained within PDU out, which uses the syntax described in XNET PDU I/O Name.

The PDU object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the new created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-signal.html language=enus -->
## TOPIC 00056: Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET signal. frame in The frame parent object. signal name The name of the signal to create. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the nam

Signal

Creates a new XNET signal.

[IMAGE alt='1378' src='XNET_Database_Create_(Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame in

The frame parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal name

The name of the signal to create.

Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### frame out

A copy of the frame in parameter. You can use this parameter to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### signal out

The I/O name of the newly created signal object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET signal object. It is an instance of XNET Database Create Object.

The signal name input becomes the Name (Short) property of the created object. This is distinct from the string contained within signal out, which uses the syntax described in XNET Signal I/O Name.

The signal object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-create-subframe.html language=enus -->
## TOPIC 00057: Subframe

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-create-subframe.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-create-subframe.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new XNET subframe. frame in The frame parent object. subframe name The name of the subframe to create. The name must be unique for all subframes in a frame. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), a

Subframe

Creates a new XNET subframe.

[IMAGE alt='1378' src='XNET_Database_Create_(Subframe).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame in

The frame parent object.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### subframe name

The name of the subframe to create.

The name must be unique for all subframes in a frame. Lowercase letters, uppercase letters, numbers, and the underscore (_) are valid characters for the name. The space ( ), period (.), and other special characters are not supported within the name. The name must begin with a letter (uppercase or lowercase) or underscore, and not a number. The name is limited to 128 characters.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### frame out

A copy of the frame in parameter. You can use this parameter to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### subframe out

The I/O name of the newly created subframe object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node creates an XNET subframe object. It is an instance of XNET Database Create Object.

The subframe name input becomes the Name (Short) property of the created object.

The subframe object is created and remains in memory until the database is closed. This node does not change the open database file on disk. To save the newly created object to the file, use XNET Database Save.

A subframe defines the multiplexer value for all dynamic signals in this subframe. Dynamic signals within a subframe inherit the multiplexer value from the subframe parent.

In NI-CAN, a subframe was called a mode.

Parent topic:

XNET Database Create Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-cluster.html language=enus -->
## TOPIC 00058: Cluster

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-cluster.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET cluster and all child objects in this cluster. cluster in The I/O name of the cluster to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out

Cluster

Deletes an XNET cluster and all child objects in this cluster.

[IMAGE alt='1378' src='XNET_Database_Delete_(Cluster).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The I/O name of the cluster to delete.

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

#### Description

This node deletes an XNET cluster object with all frames, PDUs, signals, subframes, and ECUs in this cluster. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O names of all deleted objects are closed and no longer can be used.

The objects are deleted from a database in memory. The change is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-ecu.html language=enus -->
## TOPIC 00059: ECU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-ecu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET ECU. ECU in The I/O name of the ECU to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces this output

ECU

Deletes an XNET ECU.

[IMAGE alt='1378' src='XNET_Database_Delete_(ECU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### ECU in

The I/O name of the ECU to delete.

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

#### Description

This node deletes an XNET ECU object. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O name of the ECU is closed and no longer can be used.

The ECU object is deleted from a database in memory and is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-frame.html language=enus -->
## TOPIC 00060: Frame

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-frame.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET frame and all child objects in the frame. frame in The I/O name of the frame to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error in

Frame

Deletes an XNET frame and all child objects in the frame.

[IMAGE alt='1378' src='XNET_Database_Delete_(Frame).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame in

The I/O name of the frame to delete.

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

#### Description

This node deletes an XNET frame object with all mapped PDUs, including signals and subframes in those PDUs. It is an instance of XNET Database Delete Object. To avoid deleting PDUs with the frame, unmap the PDUs from the frame before deleting the frame (set the XNET Frame PDU_Mapping property to an empty array).

Upon deletion, the I/O names of all deleted objects are closed and no longer can be used.

The objects are deleted from a database in memory. The change is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-lin-schedule-entry.html language=enus -->
## TOPIC 00061: Schedule Entry

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-lin-schedule-entry.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-lin-schedule-entry.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET schedule entry object. LIN schedule entry in The I/O name of the LIN schedule entry to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out E

Schedule Entry

Deletes an XNET schedule entry object.

[IMAGE alt='1378' src='XNET_Database_Delete_(LIN_Schedule_Entry).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### LIN schedule entry in

The I/O name of the LIN schedule entry to delete.

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

#### Description

This node deletes an XNET LIN schedule entry object. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O name of the deleted object is closed, and you no longer can use it.

The objects are deleted from a database in memory. The change is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-lin-schedule.html language=enus -->
## TOPIC 00062: Schedule

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-lin-schedule.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-lin-schedule.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET LIN schedule and all LIN schedule entry objects in this schedule. LIN schedule in The I/O name of the LIN schedule to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defa

Schedule

Deletes an XNET LIN schedule and all LIN schedule entry objects in this schedule.

[IMAGE alt='1378' src='XNET_Database_Delete_(LIN_Schedule).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### LIN schedule in

The I/O name of the LIN schedule to delete.

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

#### Description

This node deletes an XNET LIN schedule object and the entries it contains. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O names of all deleted objects are closed, and you no longer can use them.

The LIN schedule object is deleted from a database in memory and is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-object.html language=enus -->
## TOPIC 00063: XNET Database Delete Object

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-object.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a database object.

XNET Database Delete Object

Deletes a database object.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Cluster

Deletes an XNET cluster and all child objects in this cluster.

ECU

Deletes an XNET ECU.

Frame

Deletes an XNET frame and all child objects in the frame.

PDU

Deletes an XNET PDU and all child objects in this PDU.

Signal

Deletes an XNET signal.

Subframe

Deletes an XNET subframe and all dynamic signals in the subframe.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-pdu.html language=enus -->
## TOPIC 00064: PDU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-pdu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-pdu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET PDU and all child objects in this PDU. PDU in An input that references the PDU to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error

PDU

Deletes an XNET PDU and all child objects in this PDU.

[IMAGE alt='1378' src='XNET_Database_Delete_(PDU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### PDU in

An input that references the PDU to delete.

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

#### Description

This node deletes an XNET PDU object with all signals and subframes in this PDU. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O names to all deleted objects are closed and no longer can be used.

The objects are deleted from a database in memory. The change is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-signal.html language=enus -->
## TOPIC 00065: Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET signal. signal in The I/O name of the signal to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces thi

Signal

Deletes an XNET signal.

[IMAGE alt='1378' src='XNET_Database_Delete_(Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### signal in

The I/O name of the signal to delete.

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

#### Description

This node deletes an XNET signal object. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O name of the signal is closed and no longer can be used.

The signal object is deleted from a database in memory and is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-delete-subframe.html language=enus -->
## TOPIC 00066: Subframe

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-delete-subframe.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-delete-subframe.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an XNET subframe and all dynamic signals in the subframe. subframe in The I/O name of the subframe to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error erro

Subframe

Deletes an XNET subframe and all dynamic signals in the subframe.

[IMAGE alt='1378' src='XNET_Database_Delete_(Subframe).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### subframe in

The I/O name of the subframe to delete.

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

#### Description

This node deletes an XNET subframe object and all dynamic signals in this subframe. It is an instance of XNET Database Delete Object.

Upon deletion, the I/O names of the subframe and related dynamic signals are closed and no longer can be used.

The objects are deleted from a database in memory. The change is in force until the database is closed. This node does not change the open database file on disk. To save the changed database to the file, use XNET Database Save.

Parent topic:

XNET Database Delete Object

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-deploy.html language=enus -->
## TOPIC 00067: XNET Database Deploy

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-deploy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-deploy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys a database to a remote LabVIEW Real-Time (RT) target. IP address The target IP address. alias An input that provides the database alias name. To deploy a database text file, first add an alias using XNET Database Add Alias. wait for complete? An input that determines whether the node returns

XNET Database Deploy

Deploys a database to a remote LabVIEW Real-Time (RT) target.

[IMAGE alt='1378' src='XNET_Database_Deploy.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### IP address

The target IP address.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### alias

An input that provides the database alias name. To deploy a database text file, first add an alias using XNET Database Add Alias.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input that determines whether the node returns directly or waits until the entire transmission is completed.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output that indicates the deployment progress.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node transfers an optimized binary image of the database to the LabVIEW RT target. After deploying the database, you can use the alias name in any node for the Windows host and the LabVIEW RT target.

This node is supported on Windows only. LabVIEW RT database deployments are managed remotely from Windows.

This node must access the remote LabVIEW RT target from Windows, so IP address must specify a valid IP address for the LabVIEW RT target. You can find this IP address using MAX or nodes in the LabVIEW Real-Time palettes.

If the LabVIEW RT target access is password protected, use the following syntax for the IP address to deploy an alias: 
 *[user:password@]IPaddress*.

Remote file transfer can take a few seconds, especially when the RT target is far away.

If wait for complete? is true, this node waits for the entire transfer to complete, then returns. error out reflects the deployment status, and percent complete is 100.

If wait for complete? is false, this node transfers a portion of the database and returns before it is complete. For an incomplete transfer, error out returns success, and percent complete is less than 100. You can use percent complete to display transfer progress on your front panel. You must call XNET Database Deploy in a loop until percent complete is returned as 100, at which time error out reflects the entire deployment status.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-export.html language=enus -->
## TOPIC 00068: XNET Database Export

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-export.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-export.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a cluster from the open database to a file in a specific format. cluster in The I/O name of the cluster. filepath An input that contains the pathname to the file to be created. error in Error conditions that occur before this node runs. The node responds to this input according to standard e

XNET Database Export

Exports a cluster from the open database to a file in a specific format.

[IMAGE alt='1378' src='XNET_Database_Export.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The I/O name of the cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### filepath

An input that contains the pathname to the file to be created.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node exports a cluster from an XNET database to a specific file format. A CAN cluster is exported as CANdb++ database (.dbc). A LIN cluster is exported as a LIN database file (.ldf). A FlexRay cluster cannot be exported and returns an error. If the target file exists, it is overwritten. The filepath parameter is required; you cannot accidentally overwrite the original file by specifying an empty filepath.

XNET saves to the file only features that XNET sessions use to communicate on the network. If the original file was created using non-XNET software, the target file may be missing details from the original file. For example, NI-XNET supports only linear scaling. If the original FIBEX file used a rational equation that cannot be expressed as a linear scaling, XNET converts this to a linear scaling with factor 1.0 and offset 0.0.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-dbc-attribute-cluster.html language=enus -->
## TOPIC 00069: Cluster

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-dbc-attribute-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-dbc-attribute-cluster.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file. mode The mode specification of this node. Depending on this value, the node returns the following data: Mode 0: Get Attribute Value: For a given object (for example, a signal), the node retur

Cluster

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

[IMAGE alt='1378' src='XNET_Database_Get_DBC_Attribute_(Cluster).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### mode

The mode specification of this node.

- Mode 0: Get Attribute Value: For a given object (for example, a signal), the node returns the attribute value assigned to the object. The attribute values always are returned as text in attribute text . The DBC specification also allows defining other data types, such as integer or float. If necessary, you can convert the data to a number by using, for example, the Scan From String node in the String palette. If the attribute is defined as an enumeration of text strings, the attribute value returned here is the index to the enumeration list, which you can retrieve using Mode 1 of the node.
- Mode 1: Get Enumeration: For a given attribute name, the node returns the enumeration text table as a comma-separated string in attribute text . Because for a given attribute name, the enumeration is the same for all objects of the same type, object in can point to any object with the given class ( object in specifies the class). If no enumeration is defined for an attribute, the node returns an empty string.
- Mode 2: Get Attribute Name List: Returns all attribute names defined for the given object type as a comma-separated string. object in can point to any object in the database of the given class ( object in specifies the object class). attribute name is ignored (it should be set to empty string).
- Mode 3: Get Signal Value Table: This is valid only when object in points to a signal. attribute name is ignored (it should be set to empty string). If the given signal contains a value table, the function returns a comma-separated list in the form [value,string]{,<value>,<string>}. The list contains any number of corresponding value,string pairs. If no value table is defined for the signal, the result is an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### cluster in

The cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### attribute name

The attribute name.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### cluster out

A copy of the cluster in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### attribute text

The attribute value.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is default?

An output that indicates that a default value is used instead of a specific value for this object.

is default?

mode

mode

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Depending on the mode parameter, this node reads an attribute value, attribute enumeration, list of existing attributes, or value table of a signal from a DBC file. Refer to the mode input description for details.

Attributes are supported for the following object types:

- Cluster (DBC file: network attribute)
- Frame (DBC file: message attribute)
- Signal (DBC file: signal attribute)
- ECU (DBC file: node attribute)

Databases other than DBC do not support attributes. Attributes are not saved to a FIBEX file when you open and save a DBC file.

Parent topic:

XNET Database Get DBC Attribute

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-dbc-attribute-ecu.html language=enus -->
## TOPIC 00070: ECU

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-dbc-attribute-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-dbc-attribute-ecu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file. mode The mode specification of this node. Depending on this value, the node returns the following data: Mode 0: Get Attribute Value: For a given object (for example, a signal), the node retur

ECU

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

[IMAGE alt='1378' src='XNET_Database_Get_DBC_Attribute_(ECU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### mode

The mode specification of this node.

- Mode 0: Get Attribute Value: For a given object (for example, a signal), the node returns the attribute value assigned to the object. The attribute values always are returned as text in attribute text . The DBC specification also allows defining other data types, such as integer or float. If necessary, you can convert the data to a number by using, for example, the Scan From String node in the String palette. If the attribute is defined as an enumeration of text strings, the attribute value returned here is the index to the enumeration list, which you can retrieve using Mode 1 of the node.
- Mode 1: Get Enumeration: For a given attribute name, the node returns the enumeration text table as a comma-separated string in attribute text . Because for a given attribute name, the enumeration is the same for all objects of the same type, object in can point to any object with the given class ( object in specifies the class). If no enumeration is defined for an attribute, the node returns an empty string.
- Mode 2: Get Attribute Name List: Returns all attribute names defined for the given object type as a comma-separated string. object in can point to any object in the database of the given class ( object in specifies the object class). attribute name is ignored (it should be set to empty string).
- Mode 3: Get Signal Value Table: This is valid only when object in points to a signal. attribute name is ignored (it should be set to empty string). If the given signal contains a value table, the function returns a comma-separated list in the form [value,string]{,<value>,<string>}. The list contains any number of corresponding value,string pairs. If no value table is defined for the signal, the result is an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### ECU in

The ECU.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### attribute name

The attribute name.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### ecu out

A copy of the ecu in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### attribute text

The attribute value.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is default?

An output that indicates that a default value is used instead of a specific value for this object.

is default?

mode

mode

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Depending on the mode parameter, this node reads an attribute value, attribute enumeration, list of existing attributes, or value table of a signal from a DBC file. Refer to the mode input description for details.

Attributes are supported for the following object types:

- Cluster (DBC file: network attribute)
- Frame (DBC file: message attribute)
- Signal (DBC file: signal attribute)
- ECU (DBC file: node attribute)

Databases other than DBC do not support attributes. Attributes are not saved to a FIBEX file when you open and save a DBC file.

Parent topic:

XNET Database Get DBC Attribute

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-dbc-attribute-frame.html language=enus -->
## TOPIC 00071: Frame

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-dbc-attribute-frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-dbc-attribute-frame.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file. mode The mode specification of this node. Depending on this value, the node returns the following data: Mode 0: Get Attribute Value: For a given object (for example, a signal), the node retur

Frame

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

[IMAGE alt='1378' src='XNET_Database_Get_DBC_Attribute_(Frame).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### mode

The mode specification of this node.

- Mode 0: Get Attribute Value: For a given object (for example, a signal), the node returns the attribute value assigned to the object. The attribute values always are returned as text in attribute text . The DBC specification also allows defining other data types, such as integer or float. If necessary, you can convert the data to a number by using, for example, the Scan From String node in the String palette. If the attribute is defined as an enumeration of text strings, the attribute value returned here is the index to the enumeration list, which you can retrieve using Mode 1 of the node.
- Mode 1: Get Enumeration: For a given attribute name, the node returns the enumeration text table as a comma-separated string in attribute text . Because for a given attribute name, the enumeration is the same for all objects of the same type, object in can point to any object with the given class ( object in specifies the class). If no enumeration is defined for an attribute, the node returns an empty string.
- Mode 2: Get Attribute Name List: Returns all attribute names defined for the given object type as a comma-separated string. object in can point to any object in the database of the given class ( object in specifies the object class). attribute name is ignored (it should be set to empty string).
- Mode 3: Get Signal Value Table: This is valid only when object in points to a signal. attribute name is ignored (it should be set to empty string). If the given signal contains a value table, the function returns a comma-separated list in the form [value,string]{,<value>,<string>}. The list contains any number of corresponding value,string pairs. If no value table is defined for the signal, the result is an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### frame in

The frame.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### attribute name

The attribute name.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### frame out

A copy of the frame in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### attribute text

The attribute value.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is default?

An output that indicates that a default value is used instead of a specific value for this object.

is default?

mode

mode

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Depending on the mode parameter, this node reads an attribute value, attribute enumeration, list of existing attributes, or value table of a signal from a DBC file. Refer to the mode input description for details.

Attributes are supported for the following object types:

- Cluster (DBC file: network attribute)
- Frame (DBC file: message attribute)
- Signal (DBC file: signal attribute)
- ECU (DBC file: node attribute)

Databases other than DBC do not support attributes. Attributes are not saved to a FIBEX file when you open and save a DBC file.

Parent topic:

XNET Database Get DBC Attribute

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-dbc-attribute-signal.html language=enus -->
## TOPIC 00072: Signal

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-dbc-attribute-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-dbc-attribute-signal.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file. mode The mode specification of this node. Depending on this value, the node returns the following data: Mode 0: Get Attribute Value: For a given object (for example, a signal), the node retur

Signal

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

[IMAGE alt='1378' src='XNET_Database_Get_DBC_Attribute_(Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### mode

The mode specification of this node.

- Mode 0: Get Attribute Value: For a given object (for example, a signal), the node returns the attribute value assigned to the object. The attribute values always are returned as text in attribute text . The DBC specification also allows defining other data types, such as integer or float. If necessary, you can convert the data to a number by using, for example, the Scan From String node in the String palette. If the attribute is defined as an enumeration of text strings, the attribute value returned here is the index to the enumeration list, which you can retrieve using Mode 1 of the node.
- Mode 1: Get Enumeration: For a given attribute name, the node returns the enumeration text table as a comma-separated string in attribute text . Because for a given attribute name, the enumeration is the same for all objects of the same type, object in can point to any object with the given class ( object in specifies the class). If no enumeration is defined for an attribute, the node returns an empty string.
- Mode 2: Get Attribute Name List: Returns all attribute names defined for the given object type as a comma-separated string. object in can point to any object in the database of the given class ( object in specifies the object class). attribute name is ignored (it should be set to empty string).
- Mode 3: Get Signal Value Table: This is valid only when object in points to a signal. attribute name is ignored (it should be set to empty string). If the given signal contains a value table, the function returns a comma-separated list in the form [value,string]{,<value>,<string>}. The list contains any number of corresponding value,string pairs. If no value table is defined for the signal, the result is an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### signal in

The signal.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### attribute name

The attribute name.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### signal out

A copy of the signal in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### attribute text

The attribute value.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is default?

An output that indicates that a default value is used instead of a specific value for this object.

is default?

mode

mode

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Depending on the mode parameter, this node reads an attribute value, attribute enumeration, list of existing attributes, or value table of a signal from a DBC file. Refer to the mode input description for details.

Attributes are supported for the following object types:

- Cluster (DBC file: network attribute)
- Frame (DBC file: message attribute)
- Signal (DBC file: signal attribute)
- ECU (DBC file: node attribute)

Databases other than DBC do not support attributes. Attributes are not saved to a FIBEX file when you open and save a DBC file.

Parent topic:

XNET Database Get DBC Attribute

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-dbc-attribute.html language=enus -->
## TOPIC 00073: XNET Database Get DBC Attribute

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-dbc-attribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-dbc-attribute.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

XNET Database Get DBC Attribute

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Cluster

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

Frame

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

Signal

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

ECU

Reads the attribute value, attribute enumeration, defined attributes, or signal value table from a DBC file.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-get-list.html language=enus -->
## TOPIC 00074: XNET Database Get List

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-get-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-get-list.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current list of databases on a system. IP address The target IP address. If IP address is unwired (empty), this node retrieves aliases and file paths for the local Windows system. error in Error conditions that occur before this node runs. The node responds to this input according to standa

XNET Database Get List

Gets the current list of databases on a system.

[IMAGE alt='1378' src='XNET_Database_Get_List.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### IP address

The target IP address.

IP address

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### array of alias

An output that returns an array of strings, one for every alias registered in the system. If no aliases are registered, the array is empty.

[IMAGE alt='datatype_icon' src='/assets/img/i1dpath.png']

##### array of filepath

An output that returns an array of strings that contain the file paths and filenames of the databases assigned to the aliases, one for every alias registered in the system.

If no aliases are registered, the array is empty. This parameter applies to Windows targets only 
.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

For a local Windows call (IP address empty), array of filepath returns an array of file paths. The size of this array is the same as array of alias. It provides the Windows file path for each corresponding alias.

This call checks for the existence of the database file and removes any aliases that are no longer valid.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge-cluster.html language=enus -->
## TOPIC 00075: XNET Database Merge (Cluster)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge-cluster.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges all objects of the source cluster into the target cluster. wait for complete? An input used to split the merging process into parts (for example, to display a progress bar). target cluster in The I/O name of the cluster where the source cluster is merged. source cluster The I/O name of the cl

XNET Database Merge (Cluster)

Merges all objects of the source cluster into the target cluster.

[IMAGE alt='1378' src='XNET_Database_Merge_(Cluster).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input used to split the merging process into parts (for example, to display a progress bar).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### target cluster in

The I/O name of the cluster where the source cluster is merged.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source cluster

The I/O name of the cluster to be merged into the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### copy mode

An input that defines the merging behavior if the target cluster already contains elements with the same name.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### prefix

An input added to the source cluster name if an element with the same name exists in the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output used when wait for complete? is false.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### target cluster out

A copy of target cluster in. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node merges all objects contained in the source cluster into the target cluster.

The following nodes merge the objects with dependent-child objects:

- XNET Database Merge (Frame)
- XNET Database Merge (PDU)
- XNET Database Merge (ECU)
- XNET Database Merge (LIN Schedule)

Copy mode and prefix are passed to the appropriate node for the merging process.

If the copy mode is set to Copy using source or Merge using source, all cluster properties including the name are copied from the source to the target cluster.

Depending on the number of contained objects in the source and destination clusters, the execution can take longer. If wait for complete? is true, this node waits until the merging process gets completed. If the execution completes without errors, percent complete returns 100. If wait for complete? is false, the function returns quickly and percent complete returns values less than 100. You must call XNET Database Merge repeatedly until percent complete returns 100. You can use the time between calls to update a progress bar.

Parent topic:

XNET Database Merge

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge-ecu.html language=enus -->
## TOPIC 00076: XNET Database Merge (ECU)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge-ecu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge-ecu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges an ECU object with Tx/Rx frames into the destination cluster. wait for complete? An input used to split the merging process into parts (for example, to display a progress bar). target cluster in The I/O name of the cluster where the source cluster is merged. source ECU The I/O name of the ECU

XNET Database Merge (ECU)

Merges an ECU object with Tx/Rx frames into the destination cluster.

[IMAGE alt='1378' src='XNET_Database_Merge_(ECU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input used to split the merging process into parts (for example, to display a progress bar).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### target cluster in

The I/O name of the cluster where the source cluster is merged.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source ECU

The I/O name of the ECU to be merged into the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### copy mode

An input that defines the merging behavior if the target cluster already contains elements with the same name.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### prefix

An input added to the source cluster name if an element with the same name exists in the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output used when wait for complete? is false.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### target cluster out

A copy of target cluster in. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node merges an ECU with all Tx/Rx frames to the target cluster. It does not merge the frames itself, but only the transmitting or receiving information. This happens based on frame names. If the source cluster defines new frames not contained in the destination cluster, they should be merged before merging the ECU; otherwise, the Tx/Rx information is removed.

If the source ECU name was not used in the target cluster, this node copies the source ECU to the target. If an ECU with the same name exists in the target cluster, you can avoid name collisions by specifying the prefix to be added to the name.

If an ECU with the same name exists in the target cluster, the merge behavior depends on the 
 copy mode input:

- Copy using source: The target ECU with all Tx/Rx information is removed from the target cluster and replaced by the source objects.
- Copy using destination: The source ECU is ignored (the target cluster ECU with child objects remains unchanged).
- Merge using source: This adds Tx/Rx frames from the source ECU to Tx/Rx from the destination ECU. The source ECU properties (for example, comment) replace the target ECU properties.
- Merge using destination: This adds Tx/Rx frames from the source ECU to Tx/Rx from the destination ECU. The target ECU properties remain unchanged (for example, comment).

Example

Target ECU Ecu1(v1) has Tx frames F1 and F2. Source ECU Ecu1(v2) has Tx frames F2 and F3.

(v1) and (v2) are two versions of one object with same name but with different properties.

- Result of 
 Copy using source : Ecu1(v2), F2, F3.
- Result of 
 Copy using destination : Ecu1(v1), F1, F2.
- Result of 
 Merge using source : Ecu1(v2), F1, F2, F3.
- Result of 
 Merge using destination : Ecu1(v1), F1, F2, F3.

Parent topic:

XNET Database Merge

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge-frame.html language=enus -->
## TOPIC 00077: XNET Database Merge (Frame)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge-frame.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge-frame.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges a frame object with all child objects into the destination cluster. wait for complete? An input used to split the merging process into parts (for example, to display a progress bar). target cluster in The I/O name of the cluster where the source cluster is merged. source frame The I/O name of

XNET Database Merge (Frame)

Merges a frame object with all child objects into the destination cluster.

[IMAGE alt='1378' src='XNET_Database_Merge_(Frame).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input used to split the merging process into parts (for example, to display a progress bar).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### target cluster in

The I/O name of the cluster where the source cluster is merged.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source frame

The I/O name of the frame to be merged into the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### copy mode

An input that defines the merging behavior if the target cluster already contains elements with the same name.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### prefix

An input added to the source cluster name if an element with the same name exists in the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output used when wait for complete? is false.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### target cluster out

A copy of target cluster in. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node merges a frame with all dependent child objects (PDUs, subframes, and signals) to the target cluster.

If the source frame name was not used in the target cluster, this node copies the source frame with the child objects to the target. If a frame with the same name exists in the target cluster, you can avoid name collisions by specifying the prefix to be added to the name.

If a frame with the same name exists in the target cluster, the merge behavior depends on the 
 copy mode input:

- Copy using source: The target frame with all dependent child objects is removed from the target cluster and replaced by the source objects.
- Copy using destination: The source frame is ignored (the target cluster frame with child objects remains unchanged).
- Merge using source: This adds child objects from the source frame to child objects from the destination frame. If the target frame contains a child object with the same name, it is replaced by the child object from the source frame. The source frame properties (for example, payload length) replace the target frame properties.
- Merge using destination: This adds child objects from the source frame to child objects from the destination frame. If the target frame contains a child object with the same name, it remains unchanged. The target frame properties remain unchanged (for example, payload length).

Example

Target frame F1(v1) has signals S1 and S2(v1). Source frame F1(v2) has signals S2(v2) and S3.

(v1) and (v2) are two versions of one object with same name, but with different properties.

- Result of 
 Copy using source : F1(v2), S2(v2), S3.
- Result of 
 Copy using destination : F1(v1), S1, S2(v1).
- Result of 
 Merge using source : F1(v2), S1, S2(v2), S3.
- Result of 
 Merge using destination : F1(v1), S1, S2(v1), S3.

Parent topic:

XNET Database Merge

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge-lin-schedule.html language=enus -->
## TOPIC 00078: XNET Database Merge (LIN Schedule)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge-lin-schedule.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge-lin-schedule.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges a LIN schedule object with all child objects into the destination cluster. wait for complete? An input used to split the merging process into parts (for example, to display a progress bar). target cluster in The I/O name of the cluster where the source cluster is merged. source LIN schedule T

XNET Database Merge (LIN Schedule)

Merges a LIN schedule object with all child objects into the destination cluster.

[IMAGE alt='1378' src='XNET_Database_Merge_(LIN_Schedule).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input used to split the merging process into parts (for example, to display a progress bar).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### target cluster in

The I/O name of the cluster where the source cluster is merged.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source LIN schedule

The I/O name of the LIN schedule to be merged into the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### copy mode

An input that defines the merging behavior if the target cluster already contains elements with the same name.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### prefix

An input added to the source cluster name if an element with the same name exists in the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output used when wait for complete? is false.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### target cluster out

A copy of target cluster in. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node merges a LIN schedule with all schedule entries to the target cluster. Frames referenced in the schedule entries should be merged before merging the LIN schedule; otherwise, the reference get lost.

If the source LIN schedule name was not used in the target cluster, this node copies the source LIN schedule with the entries to the target. If a LIN schedule with the same name exists in the target cluster, you can avoid name collisions by specifying the prefix to be added to the name.

If a LIN schedule with the same name exists in the target cluster, the merge behavior depends on the 
 copy mode input:

- Copy using source: The target LIN schedule with entries is removed from the target cluster and replaced by the source objects.
- Copy using destination: The source LIN schedule is ignored (the target cluster schedule with entries remains unchanged).
- Merge using source: This adds schedule entries from the source schedule at the end of the destination schedule table. The copied entries become new names, so all entry names in the schedule are unique. The source schedule properties replace the target schedule properties (comment, priority, run mode).
- Merge using destination: This adds schedule entries from the source schedule at the end of the destination schedule table. The copied entries become new names, so all entry names in the schedule are unique. The target schedule properties (comment, priority, run mode) remain unchanged.

Example

Target LIN schedule LS1(v1) has entries e1, e2. Source LIN schedule LS1(v2) has entries e3, e4.

(v1) and (v2) are two versions of one object with same name but with different properties.

- Result of 
 Copy using source : LS1(v1), e1, e2.
- Result of 
 Copy using destination : LS1(v2), e3, e4.
- Result of 
 Merge using source : LS1(v2),e1, e2, e3, e4.
- Result of 
 Merge using destination : LS1(v1), e1, e2, e3, e4.

Parent topic:

XNET Database Merge

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge-pdu.html language=enus -->
## TOPIC 00079: XNET Database Merge (PDU)

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge-pdu.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge-pdu.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges a PDU object with all child objects into the destination cluster. wait for complete? An input used to split the merging process into parts (for example, to display a progress bar). target cluster in The I/O name of the cluster where the source cluster is merged. source PDU The I/O name of the

XNET Database Merge (PDU)

Merges a PDU object with all child objects into the destination cluster.

[IMAGE alt='1378' src='XNET_Database_Merge_(PDU).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for complete?

An input used to split the merging process into parts (for example, to display a progress bar).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### target cluster in

The I/O name of the cluster where the source cluster is merged.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source PDU

The I/O name of the PDU to be merged into the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### copy mode

An input that defines the merging behavior if the target cluster already contains elements with the same name.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### prefix

An input added to the source cluster name if an element with the same name exists in the target cluster.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### percent complete

An output used when wait for complete? is false.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### target cluster out

A copy of target cluster in. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node merges a PDU with all dependent child objects (subframes and signals) to the target cluster.

If the source PDU name was not used in the target cluster, this node copies the source PDU with the child objects to the target. If a PDU with the same name exists in the target cluster, you can avoid name collisions by specifying the prefix to be added to the name.

If a PDU with the same name exists in the target cluster, the merge behavior depends on the 
 copy mode input:

- Copy using source: The target PDU with all dependent child objects is removed from the target cluster and replaced by the source objects.
- Copy using destination: The source PDU is ignored (the target cluster PDU with child objects remains unchanged).
- Merge using source: This adds child objects from the source PDU to child objects from the destination PDU. If the target PDU contains a child object with the same name, it is replaced by the child object from the source PDU. The source PDU properties (for example, payload length) replace the target PDU properties.
- Merge using destination: This adds child objects from the source PDU to child objects from the destination PDU. If the target PDU contains a child object with the same name, it remains unchanged. The target PDU properties remain unchanged (for example, payload length).

Example

Target PDU Pdu1(v1) has signals S1 and S2(v1). Source PDU Pdu1(v2) has signals S2(v2) and S3.

(v1) and (v2) are two versions of one object with same name but with different properties.

- Result of 
 Copy using source : Pdu1(v2), S2(v2), S3.
- Result of 
 Copy using destination : Pdu1(v1), S1, S2(v1).
- Result of 
 Merge using source : Pdu1(v2), S1, S2(v2), S3.
- Result of 
 Merge using destination : Pdu1(v1), S1, S2(v1), S3.

Parent topic:

XNET Database Merge

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-merge.html language=enus -->
## TOPIC 00080: XNET Database Merge

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-merge.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-merge.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merges database objects and related child objects from the source to the destination cluster.

XNET Database Merge

Merges database objects and related child objects from the source to the destination cluster.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

XNET Database Merge (Frame)

Merges a frame object with all child objects into the destination cluster.

XNET Database Merge (PDU)

Merges a PDU object with all child objects into the destination cluster.

XNET Database Merge (ECU)

Merges an ECU object with Tx/Rx frames into the destination cluster.

XNET Database Merge (LIN Schedule)

Merges a LIN schedule object with all child objects into the destination cluster.

XNET Database Merge (Cluster)

Merges all objects of the source cluster into the target cluster.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-remove-alias.html language=enus -->
## TOPIC 00081: XNET Database Remove Alias

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-remove-alias.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-remove-alias.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a database alias from the system. alias The name of the alias to delete. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node pro

XNET Database Remove Alias

Removes a database alias from the system.

[IMAGE alt='1378' src='XNET_Database_Remove_Alias.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### alias

The name of the alias to delete.

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

#### Description

This node removes the alias from NI-XNET, but does not affect the database text file. It just removes the alias association to the database filepath.

This node is supported on Windows only, and the alias is removed from Windows only.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-save.html language=enus -->
## TOPIC 00082: XNET Database Save

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-save.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-save.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the open database to a FIBEX 3.1.1 file. database in The I/O name of the database. filepath An input that contains the pathname to the FIBEX file or is empty (saves to the original filepath). error in Error conditions that occur before this node runs. The node responds to this input according

XNET Database Save

Saves the open database to a FIBEX 3.1.1 file.

[IMAGE alt='1378' src='XNET_Database_Save.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### database in

The I/O name of the database.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### filepath

An input that contains the pathname to the FIBEX file or is empty (saves to the original filepath).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### database out

A copy of the database in parameter. You can use this output to wire the node to subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node saves the XNET database current state to a FIBEX 3.1.1 file. The file extension must be 
 .xml. If the target file exists, it is overwritten.

XNET saves to the FIBEX file only features that XNET sessions use to communicate on the network. If the original file was created using non-XNET software, the target file may be missing details from the original file. For example, NI-XNET supports only linear scaling. If the original FIBEX file used a rational equation that cannot be expressed as a linear scaling, XNET converts this to a linear scaling with factor 1.0 and offset 0.0.

If filepath is empty, the file is saved to the same FIBEX file specified when opened. If opened as a file path, it uses that file path. If opened as an alias, it uses the file path registered for that alias.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-database-undeploy.html language=enus -->
## TOPIC 00083: XNET Database Undeploy

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-database-undeploy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-database-undeploy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys a database from a remote LabVIEW Real-Time (RT) target. IP address The target IP address. alias The database alias name. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value:

XNET Database Undeploy

Undeploys a database from a remote LabVIEW Real-Time (RT) target.

[IMAGE alt='1378' src='XNET_Database_Undeploy.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### IP address

The target IP address.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### alias

The database alias name.

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

#### Description

This node completely deletes the database file and its alias from the LabVIEW RT target.

This node is supported on Windows only. LabVIEW RT database deployments are managed remotely from Windows.

This node must access the remote LabVIEW RT target from Windows, so IP address must specify a valid IP address for the LabVIEW RT target. You can find this IP address using MAX or nodes in the LabVIEW Real-Time palettes.

If the LabVIEW RT target access is password protected, you can use the following syntax for the IP address to deploy an alias: 
 *[user:password@]IPaddress.*

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-disconnect-terminals.html language=enus -->
## TOPIC 00084: XNET Disconnect Terminals

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-disconnect-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-disconnect-terminals.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects terminals on the XNET interface. session in The session to use for the connection. This session is selected from the LabVIEW project or returned from XNET Create Session. source terminal The connection source. destination terminal The connection destination. error in Error conditions tha

XNET Disconnect Terminals

Disconnects terminals on the XNET interface.

[IMAGE alt='1378' src='XNET_Disconnect_Terminals.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for the connection. This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### source terminal

The connection source.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### destination terminal

The connection destination.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A duplicate of session in, provided for simpler wiring.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This node disconnects a specific pair of source/destination terminals previously connected with XNET Connect Terminals.

When the final session for a given interface is cleared (either by the node going idle or by explicit calls to XNET Clear), NI-XNET automatically disconnects all terminal connections for that interface. Therefore, XNET Disconnect Terminals is not required for most applications.

This node typically is used to change terminal connections dynamically while an application is running. To disconnect a terminal, you first must stop the interface using XNET Stop node with the Interface Only scope. Then you can call XNET Disconnect Terminals and XNET Connect Terminals to adjust terminal connections. Finally, you can call XNET Start with the Interface Only scope to restart the interface.

You can disconnect only a terminal that has been previously connected. Attempting to disconnect a nonconnected terminal results in an error.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-flush.html language=enus -->
## TOPIC 00085: XNET Flush

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-flush.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-flush.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flushes (empties) all XNET session queues. session in The session to flush. This session is selected from the LabVIEW project or returned from XNET Create Session.vi. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Sta

XNET Flush

Flushes (empties) all XNET session queues.

[IMAGE alt='1378' src='XNET_Flush.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to flush. This session is selected from the LabVIEW project or returned from XNET Create Session.vi.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

With the exception of single-point modes, all sessions use queues to store frames. For input modes, the queues store frame values (or corresponding signal values) that have been received, but not obtained by calling XNET Read. For output sessions, the queues store frame values provided to XNET Write, but not transmitted successfully.

XNET Start and XNET Stop have no effect on these queues. Use XNET Flush to discard all values in the session's queues.

For example, if you call XNET Write to write three frames, then immediately call XNET Stop, then call XNET Start a few seconds later, the three frames transmit. If you call XNET Flush between XNET Stop and XNET Start, no frames transmit.

As another example, if you receive three frames, then call XNET Stop, the three frames remains in the queue. If you call XNET Start a few seconds later, then call XNET Read, you obtain the three frames received earlier, potentially followed by other frames received after calling XNET Start. If you call XNET Flush between XNET Stop and XNET Start, XNET Read returns only frames received after the calling XNET Start.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-future-time-trigger.html language=enus -->
## TOPIC 00086: XNET Future Time Trigger

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-future-time-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-future-time-trigger.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the future timestamp for an exported Time Trigger. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point. when when provides the fut

XNET Future Time Trigger

Provides the future timestamp for an exported Time Trigger.

[IMAGE alt='1378' src='XNET_Future_Time_Trigger.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### when

when provides the future timestamp at which the exported Time
 Trigger terminal will transition from low to high.

timescale

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### timescale

timescale specifies the timescale that is used with the Time
 Trigger.

The default value is Local Time (0).

| Local Time | 0 | This is the local timescale of the XNET hardware (such as the PXI backplane clock). |
| --- | --- | --- |
| Network Time | 1 | This is the network timescale (time sync protocol such as IEEE Std 802.11AS). |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

When you use the [XNET Connect Terminals](xnet-connect-terminals.html)
 with source terminal of TimeTrigger (i.e., exported), the
 destination terminal is set low. This XNET Future Time Trigger VI provides a future
 timestamp for the exported Time Trigger to generate a pulse (low to high followed by high
 to low).

If you provide a *when* timestamp that cannot be generated (e.g., in the past,
 or too soon in the future for XNET to handle), this VI returns an error.

If you invoke the XNET Future Time Trigger VI while a previous invocation of the XNET
 Future Time Trigger VI is pending, an error is returned; future timestamps are not
 queued.

An invocation of XNET Future Time Trigger VI is canceled if you disconnect the exported
 Time Trigger (for example, by using [XNET Disconnect Terminals](xnet-disconnect-terminals.html) or [XNET Close](xnet-close.html), or by stopping
 execution of your top-level VI).

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-frame-can.html language=enus -->
## TOPIC 00087: CAN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-frame-can.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-frame-can.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session as an array of CAN frames. The session must use a CAN interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The ses

CAN

Reads data from a session as an array of CAN frames. The session must use a CAN interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='1378' src='XNET_Read_(Frame_CAN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of frame values desired.

number to read

data

If number to read is negative (typically -1), all available frame values are returned. If number to read is negative, you must use a timeout of 0.

This input is optional. The default value is -1.

If the session mode is Frame Input Single-Point, set number to read to either -1 or the number of frames in the sessions list. This ensures that XNET Read (Frame CAN) can return the current value of all session frames.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read frame values to become available.

timeout

If timeout is positive, XNET Read (Frame CAN) waits for number to read frame values, then returns that number. If the values do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Frame CAN) waits indefinitely for number to read frame values.

If timeout is zero, XNET Read (Frame CAN) does not wait and immediately returns all available frame values up to the limit number to read specifies.

This input is optional. The default value is 0.0.

If the session mode is Frame Input Single-Point, you must leave timeout unwired (0.0). Because this mode reads the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

This output returns an array of LabVIEW clusters.

For a Frame Input Single-Point session mode, the order of frames in the array corresponds to the order in the session list.

The elements of each cluster are specific to the CAN protocol.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### identifier

The CAN frame arbitration identifier.

extended?

If extended? is true, the identifier uses extended format, so 29 bits of this identifier are valid.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### extended?

A Boolean value that determines whether the identifier uses extended format (true) or standard format (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false).

This value is true only when you enable echo of transmitted frames by setting the XNET Session Interface:Echo Transmit? property to True.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type (decimal value in parentheses).

| CAN Data (0) | The CAN data frame contains payload data. This is the most commonly used frame type for CAN. In ISO CAN FD mode, the CAN data type is more specific and is one of the types listed below. |
| --- | --- |
| CAN 2.0 Data (8) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the CAN 2.0 standard. |
| CAN FD Data (16) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the ISO CAN FD standard. |
| CAN FD+BRS Data (24) | The frame contains payload data and has been transmitted in an ISO CAN FD session using the CAN FD+BRS standard. |
| CAN Remote (1) | A CAN remote frame. An ECU transmits a CAN remote frame to request data for the corresponding identifier. Your application can respond by writing a CAN data frame for the identifier. |
| Log Trigger (225) | A Log Trigger frame. This frame is generated when a trigger occurs on an external connection (for example, PXI_Trig0). |
| Start Trigger (226) | A Start Trigger frame is generated when the interface is started . |
| CAN Bus Error (2) | A CAN Bus Error frame is generated when a bus error is detected on the CAN bus. |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

This parameter represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for the CAN data frame.

For a received remote frame (type of CAN Remote), the payload length in the frame value specifies the number of payload bytes requested. This payload length is provided to your application by filling payload with the requested number of bytes. Your application can use the payload array size, but you must ignore the actual values in the payload bytes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of CAN frames. Each CAN frame uses a LabVIEW cluster with CAN-specific elements.

The CAN frames are associated to the session's list of frames as follows:

- Frame Input Stream: Array of all frame values received (list ignored).
- Frame Input Queued: Array of frame values received for the single frame specified in the list.
- Frame Input Single-Point: Array of single frame values, one for each frame specified in the list.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-frame-ethernet.html language=enus -->
## TOPIC 00088: Ethernet

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-frame-ethernet.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-frame-ethernet.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session as an array of Ethernet frames. The session must use an Ethernet interface and a mode of Frame Input Stream. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream.

Ethernet

Reads data from a session as an array of Ethernet frames. The session must use an
 Ethernet interface and a mode of Frame Input Stream.

[IMAGE alt='1378' src='XNET_Read_(Frame_Ethernet).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

XNET Create Session

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of frame values desired.

number to
 read

data

If number to read is negative (typically
 -1), all available frame values are returned. If number to read is
 negative, you must use a timeout of 0.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read frame values to
 become available.

The timeout is a LabVIEW relative time, represented as 64-bit
 floating-point in units of seconds.

If timeout is positive, XNET Read (Frame Ethernet) waits for
 number to read frame values, then returns that number. If the
 values do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Frame Ethernet) waits
 indefinitely for number to read frame values.

If timeout is zero, XNET Read (Frame Ethernet) does not wait and
 immediately returns all available frame values up to the limit specified by number
 to read.

This input is optional. The default value is 0.0.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The error cluster created by this node.

error in

error out

error in

error out

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

This output returns an array of LabVIEW clusters.

Each array element corresponds to a frame that the session receives. The elements of each
 cluster are specific to the Ethernet protocol.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The type of Ethernet frame (decimal value in parentheses).

| Ethernet Data (0) | Ethernet frame received or transmitted. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### local timestamp

A timestamp using XNET local time. The timestamp uses the LabVIEW absolute
 timestamp type.

The timestamp point in the Ethernet frame occurs at the beginning of the first symbol
 following the start of frame delimiter.

The location of the timestamp point depends on the Port Mode of the session interface. When
 Port Mode is Direct, the location of the timestamp point corresponds to time synchronization
 protocols, using the reference plane marking the boundary between the port's connector (copper
 wire) and PHY. When Port Mode is Tap, the location of the timestamp point is the midpoint
 between the connector/PHY reference plane of this session's interface and the connector/PHY
 reference plane of the tap partner.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### network timestamp

A timestamp using network time (clock of the network's time synchronization protocol,
 such as IEEE Std 802.1AS). The timestamp uses the LabVIEW absolute timestamp type.

The timestamp point in the Ethernet frame occurs at the beginning of the first symbol
 following the start of frame delimiter.

The location of the timestamp point depends on the Port Mode of the session interface.
 When Port Mode is Direct, the location of the timestamp point corresponds to time
 synchronization protocols, using the reference plane marking the boundary between the
 port's connector (copper wire) and PHY. When Port Mode is Tap, the location of the
 timestamp point is the midpoint between the connector/PHY reference plane of this
 session's interface and the connector/PHY reference plane of the tap partner.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### network synced?

Contains the value of the Synced property at the time that both timestamps are
 acquired, to specify whether the network timestamp is synchronized to the network (true)
 or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### receive?

A Boolean value that indicates whether the frame occurred due to receive (true) or
 not (false).

- When Port Mode of this session's interface is Direct, this flag is true when a frame is
 received on the interface.
- When Port Mode of this session's interface is Tap, the value true indicates that the
 frame was received by this interface, and will be transmitted on the tap partner.

For XNET Read on the endpoint path, this flag is always true.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### transmit?

A Boolean value that indicates whether the frame occurred due to transmit (true) or
 not (false).

- When Port Mode of this session's interface is Direct, the monitor path echoes each
 transmit that was submitted to XNET Write on the endpoint path.
- When Port Mode of this session's interface is Tap, the value true indicates that the
 frame was received by the tap partner and transmitted on this interface (i.e., not an echo
 of Write).

For XNET Read on the endpoint path, this flag is always false.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### error?

A Boolean that indicates whether an error occurred during the
 reception/transmission of the frame (false = good frame, true = bad
 frame).

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### frame data

An array of bytes that provides the data of the Ethernet frame.

Using the terminology from IEEE Std 802.3, the frame
 data begins with the first byte of the destination MAC
 address, and ends with the last byte of the mac_service_data_unit
 (MSDU).

In order to obtain the payload data that is contained in the frame, your code
 must decode the layered headers in frame data. For
 example, for an IPv4 UDP packet, you decode the Ethernet header, including
 the EtherType, to determine that the remaining data is an IPv4 packet; then
 you decode the IPv4 header, including the Protocol, to determine that the
 remaining data is a UDP packet; and then you decode the UDP header and its
 payload data.

The maximum length of this array is provided in the Payload Length Maximum
 property.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### fcs

The IEEE Std 802.3 Frame Check Sequence (FCS) that was received with the
 frame.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

#### Description

The data represents an array of Ethernet frames. Each Ethernet frame uses a LabVIEW
 cluster with Ethernet-specific elements.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-frame-flexray.html language=enus -->
## TOPIC 00089: FlexRay

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-frame-flexray.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-frame-flexray.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session as an array of FlexRay frames. The session must use a FlexRay interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session.

FlexRay

Reads data from a session as an array of FlexRay frames. The session must use a FlexRay interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='1378' src='XNET_Read_(Frame_FlexRay).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of frame values desired.

number to read

data

If number to read is negative (typically -1), all available frame values are returned. If number to read is negative, you must use a timeout of 0.

This input is optional. The default value is -1.

If the session mode is Frame Input Single-Point, set number to read to either -1 or the number of frames in the sessions list. This ensures that XNET Read (Frame FlexRay) can return the current value of all session frames.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read frame values to become available.

timeout

If timeout is positive, XNET Read (Frame FlexRay) waits for number to read frame values, then returns that number. If the values do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Frame FlexRay) waits indefinitely for number to read frame values.

If timeout is zero, XNET Read (Frame FlexRay) does not wait and immediately returns all available frame values up to the limit number to read specifies.

This input is optional. The default value is 0.0.

If the session mode is Frame Input Single-Point, you must leave timeout unwired (0.0). Because this mode reads the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

This output returns an array of LabVIEW clusters.

Each array element corresponds to a frame the session receives.

For the Frame Input Single-Point and PDU Input Single-Point session modes, the order of frames/payload in the array corresponds to the order in the session list.

The elements of each cluster are specific to the FlexRay protocol. For more information, refer to 
 the FlexRay protocol specification.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### Slot

This element specifies the slot number within the FlexRay cycle.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### cycle count

This parameter specifies the cycle number.

The FlexRay cycle count increments from 0 to 63, then rolls over back to 0.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### startup?

A Boolean value that specifies whether the frame is a startup frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sync?

A Boolean value that specifies whether the frame is a sync frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### preamble?

A Boolean value that specifies the value of the payload preamble indicator in the frame header.

preamble?

If the frame is in the dynamic segment, preamble? being true indicates the presence of a message ID at the beginning of the payload. The message ID is always 2 bytes in length.

If preamble? is false, the payload does not contain a network management vector or a message ID.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### chA

A Boolean value that specifies whether the frame was received on channel A (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ChB

A Boolean value that specifies whether the frame was received on channel B (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false).

This value is true only when you enable echo of transmitted frames by setting the XNET Session Interface:Echo Transmit? property to True. Frames are echoed only to a session with the Frame Input Stream Mode.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type (decimal value in parentheses).

| FlexRay Data (32) | FlexRay data frame. The frame contains payload data. This is the most commonly used frame type for FlexRay. All elements in the frame are applicable. |
| --- | --- |
| FlexRay Null (33) | FlexRay null frame. When a FlexRay null frame is received, it indicates that the transmitting ECU did not have new data for the current cycle. Null frames occur in the static segment only. This frame type does not apply to frames in the dynamic segment. This frame type occurs only when you set the XNET Session Interface:FlexRay:Null Frames To Input Stream? property to true. This property enables logging of received null frames to a session with the Frame Input Stream Mode. Other sessions are not affected. For this frame type, the payload array is empty (size 0), and preamble? and echo? are false. The remaining elements in the frame reflect the data in the received null frame and the timestamp when it was received. |
| FlexRay Symbol (34) | FlexRay symbol frame. The frame contains a symbol received on the FlexRay bus. For this frame type, the first payload byte (offset 0) specifies the type of symbol: 0 for MTS, 1 for wakeup. The frame payload length is 1 or higher, with bytes beyond the first byte reserved for future use. The frame timestamp specifies when the symbol window occurred. The cycle count, channel A indicator, and channel B indicator are encoded the same as FlexRay data frames. All other fields in the frame are unused (0). |
| Log Trigger (225) | A Log Trigger frame. This frame is generated when a trigger occurs on an external connection (for example, PXI_Trig0). |
| Start Trigger (226) | A Start Trigger frame is generated when the interface is started . |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

This parameter represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

While the NI-XNET FlexRay interface is communicating (integrated), this timestamp is normally derived from FlexRay global time, the FlexRay network timebase. Under this configuration, the timestamp does not drift as compared to the FlexRay global time (XNET Read (State FlexRay Cycle Macrotick).vi), but it may drift relative to other NI hardware products and the LabVIEW absolute timebase. If you prefer to synchronize this timestamp to other sources, you can use XNET Connect Terminals.vi to change the source of the Master Timebase terminal.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for FlexRay frames of type FlexRay Data or FlexRay Null.

For PDU session modes, only the payload for the particular PDU is returned, not the entire frame.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of FlexRay frames. Each FlexRay frame uses a LabVIEW cluster with FlexRay-specific elements.

The FlexRay frames are associated to the session list of frames as follows:

- Frame Input Stream: Array of all frame values received (list ignored).
- Frame Input Queued: Array of frame values received for the single frame specified in the list.
- Frame Input Single-Point: Array of single frame values, one for each frame specified in the list.
- PDU Input Queued: Array of frame (PDU payload) values received for the single PDU specified in the list. This mode is similar to Frame Input Queued.
- PDU Input Single-Point: Array of single frame (PDU payload) values, one for each PDU specified in the list. This mode is similar to Frame Input Single-Point.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-frame-lin.html language=enus -->
## TOPIC 00090: LIN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-frame-lin.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-frame-lin.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session as an array of LIN frames. The session must use a LIN interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The ses

LIN

Reads data from a session as an array of LIN frames. The session must use a LIN interface and a mode of Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='1378' src='XNET_Read_(Frame_LIN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of frame values desired.

number to read

data

If number to read is negative (typically -1), all available frame values are returned. If number to read is negative, you must use a timeout of 0.

This input is optional. The default value is -1.

If the session mode is Frame Input Single-Point, set number to read to either -1 or the number of frames in the sessions list. This ensures that XNET Read (Frame LIN) can return the current value of all session frames.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read frame values to become available.

timeout

If timeout is positive, XNET Read (Frame LIN) waits for number to read frame values, then returns that number. If the values do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Frame LIN) waits indefinitely for number to read frame values.

If timeout is zero, XNET Read (Frame LIN) does not wait and immediately returns all available frame values up to the limit number to read specifies.

This input is optional. The default value is 0.0.

If the session mode is Frame Input Single-Point, you must leave timeout unwired (0.0). Because this mode reads the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

This output returns an array of LabVIEW clusters.

For a Frame Input Single-Point session mode, the order of frames in the array corresponds to the order in the session list.

The elements of each cluster are specific to the LIN protocol.

For the Frame Input Stream session mode, LIN frames are read in their raw form, without interpretation of their elements using the database. For the Frame Input Single-point and Frame Input Queued session modes, information from the database is used to interpret the LIN frames for ease of use.

The following cluster description applies to session modes Frame Input Single-point and Frame Input Queued.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### identifier

The LIN frame identifier.

payload.

The location of this ID within the frame depends on the value of event slot?. If event slot? is false, this ID is taken from the frame's header. If event slot? is true, this ID is taken from the first payload byte. This ensures that the number identifies the payload, regardless of how it was scheduled.

Regardless of its location, this is the unprotected ID, without parity applied.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### event slot?

A Boolean value that specifies whether the frame was received within an event-triggered schedule entry (slot).

When this value is true, event ID contains the ID from the frame’s header.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### event ID

The identifier for an event-triggered slot (event slot? true).

event slot?

event ID

event ID

When event slot? is false, this value does not apply (it is 0).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

A Boolean value that determines whether the frame was an echo of a successful transmit (true), or received from the network (false).

This value is true only when you enable echo of transmitted frames by setting the XNET Session Interface:Echo Transmit? property to True.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

The frame type (decimal value in parentheses).

| LIN Data (64) | The LIN data frame contains payload data. |
| --- | --- |
| Log Trigger (225) | A Log Trigger frame. This frame is generated when a trigger occurs on an external connection (for example, PXI_Trig0). |
| Start Trigger (226) | A Start Trigger frame is generated when the interface is started . |
| LIN Bus Error (65) | A LIN Bus Error frame is generated when a bus error is detected on the LIN bus. |
| LIN No Response (66) | A LIN No Response frame is generated when a header with no response is detected on the LIN bus. |

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

This parameter represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

The array of data bytes for the LIN data frame.

If the frame payload is used within an event-triggered schedule entry (slot), the first byte of payload is the identifier of the frame in its protected form (checksum applied). This is required by the LIN standard even if the frame transmits in an unconditional or sporadic slot. For this type of LIN frame, the actual data (for example, signal values) is limited to 7 bytes.

For example, assume that frame ID 5 is received in an unconditional slot and an event-triggered slot of ID 9. When you receive from the unconditional slot, identifier is 5, event slot? is false, event ID is 0, and the first payload byte contains 5 with checksum applied. When you receive from the event-triggered slot, identifier is 5, event slot? is true, event ID is 9, and the first payload byte contains 5 with checksum applied. Regardless of how the frame is received, you can use the identifier to determine the contents of the actual payload data contents in bytes 2-8.

The following cluster description applies to session mode Frame Input Stream.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### identifier

The identifier received within the frame's header.

If the schedule entry (slot) is unconditional or sporadic, this identifies the payload data (LIN frame). If the schedule entry is event triggered, this identifies the schedule entry itself, and the protected ID contained in the first payload byte identifies the payload.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### event slot?

This element is not used. This element is false.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### event ID

This element is not used. This element is 0.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### echo?

This parameter uses the same semantics as the previous description for Frame Input Queued.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### type

This parameter uses the same semantics as the previous description for Frame Input Queued.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

This parameter uses the same semantics as the previous description for Frame Input Queued.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### payload

This parameter uses the same semantics as the previous description for Frame Input Queued.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### unused payloads

This parameter is empty. No user input is needed.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of LIN frames. Each LIN frame uses a LabVIEW cluster with LIN-specific elements.

The LIN frames are associated to the session's list of frames as follows:

- Frame Input Stream: Array of all frame values received (list ignored).
- Frame Input Queued: Array of frame values received for the single frame specified in the list.
- Frame Input Single-Point: Array of single frame values, one for each frame specified in the list.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-frame-raw.html language=enus -->
## TOPIC 00091: Raw

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-frame-raw.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-frame-raw.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session as an array of raw bytes. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point. number to read The number of bytes

Raw

Reads data from a session as an array of raw bytes.

[IMAGE alt='1378' src='XNET_Read_(Frame_Raw).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Input Stream, Frame Input Queued, or Frame Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of bytes (U8) desired.

Standard CAN and LIN frames are always 24 bytes in length. If you want to read a specific number of frames, multiply that number by 24.

CAN FD and FlexRay frames vary in length. For example, if you pass number to read of 91, the data might return 80 bytes, within which the first 24 bytes encode the first frame, and the next 56 bytes encode the second frame.

If number to read is positive (or 0), the data array size is no greater than this number. The minimum size for a single frame is 24 bytes.

If number to read is negative (typically -1), all available raw data is returned. If number to read is negative, you must use a timeout of 0.

This input is optional. The default value is -1.

If the session mode is Frame Input Single-Point, set number to read to -1. This ensures that XNET Read (Frame Raw) can return the current value of all session frames.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read frame bytes to become available.

number to read

data

number to read

timeout

The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds.

If timeout is positive, XNET Read (Frame Raw) waits for number to read frame bytes to be received, then returns complete frames up to that number. If the bytes do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Frame Raw) waits indefinitely for number to read frame bytes.

If timeout is zero, XNET Read (Frame Raw) does not wait and immediately returns all available frame bytes up to the limit number to read specifies.

This input is optional. The default value is 0.0.

If the session mode is Frame Input Single-Point, you must leave timeout unwired (0.0). Because this mode reads the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### data

This output returns an array of bytes.

The data always returns complete frames.

For information about which elements of the raw frame are applicable, refer to the frame read for the protocol in use (XNET Read (Frame CAN), XNET Read (Frame FlexRay), or XNET Read (Frame LIN)). For example, when you read FlexRay frames for a Frame Input Queued session, the only frame type is FlexRay Data (other types apply to Frame Input Stream only).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The raw bytes encode one or more frames using the Raw Frame Format. The session must use a mode of Frame Input Stream, Frame Input Queued, Frame Input Single-Point, PDU Input Queued (similar to Frame Input Queued), or PDU Input Single-Point (similar to Frame Input Single-Point). The raw frame format is protocol independent, so the session can use either a CAN, FlexRay, or LIN interface.

The raw frame format matches the format of data transferred to/from the XNET hardware. Because it is not converted to/from LabVIEW clusters for ease of use, it is more efficient with regard to performance. This XNET Read instance typically is used to read raw frame data from the interface and log the data to a file for later analysis. The NI-XNET examples provide code to read the raw frame data from the log file and convert the raw data into protocol-specific LabVIEW clusters.

The raw frames are associated to the session's list of frames as follows:

- Frame Input Stream: Array of all frame values received (list ignored).
- Frame Input Queued: Array of frame values received for the single frame specified in the list.
- Frame Input Single-Point: Array of single frame values, one for each frame specified in the list.
- PDU Input Queued: Array of frame (PDU payload) values received for the single PDU specified in the list. This mode is similar to Frame Input Queued.
- PDU Input Single-Point: Array of single frame (PDU payload) values, one for each PDU specified in the list. This mode is similar to Frame Input Single-Point.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-signal-single-point.html language=enus -->
## TOPIC 00092: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-signal-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-signal-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session of Signal Input Single-Point mode. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Input Single-Point. error in Error conditions that occur before this node runs. The nod

Single-Point

Reads data from a session of Signal Input Single-Point mode.

[IMAGE alt='1378' src='XNET_Read_(Signal_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Input Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### data

This output returns a one-dimensional array of signal values.

Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list.

The data returns the most recent value received for each signal. If multiple frames for a signal are received since the previous call to XNET Read (Signal Single-Point) (or session start), only signal data from the most recent frame is returned.

If no frame is received for the corresponding signals since you started the session, the XNET Signal Default Value is returned.

A trigger signal returns a value of 1.0 or 0.0, depending on whether its frame arrived since the last Read (or Start) or not.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-signal-waveform.html language=enus -->
## TOPIC 00093: Waveform

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-signal-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-signal-waveform.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session of Signal Input Waveform mode. The data represents a waveform of resampled values for each signal in the session. You can wire the data directly to a LabVIEW Waveform Graph for display. session in The session to read. This session is selected from the LabVIEW project or ret

Waveform

Reads data from a session of Signal Input Waveform mode. The data represents a waveform of resampled values for each signal in the session. You can wire the data directly to a LabVIEW Waveform Graph for display.

[IMAGE alt='1378' src='XNET_Read_(Signal_Waveform)_.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Input Waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of samples desired.

number to read

Y

timeout

If number to read is negative (typically -1), the maximum number of samples is returned. If number to read is negative, you must use a timeout of zero.

This input is optional. The default value is -1.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for number to read samples to become available.

If timeout is positive, XNET Read (Signal Waveform) waits for number to read samples, then returns that number. If the samples do not arrive prior to the timeout, an error is returned.

If timeout is negative, XNET Read (Signal Waveform) waits indefinitely for number to read samples.

If timeout is zero, XNET Read (Signal Waveform) does not wait and immediately returns all available samples up to the limit number to read specifies.

Because time determines sample availability, typical values for this timeout are 0 (return available) or a large positive value such as 100.0 (wait for a specific number to read). This input is optional. The default value is 0.0.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

##### data

An output that returns a one-dimensional array of LabVIEW waveforms.

Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### t0

The waveform start time.

Y

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

The waveform delta time.

Y

dt

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### Y

The array of resampled signal values.

The Y array size is the same for all waveforms returned, because it is determined based on time, and not the number of frames received.

If no frame is received for the corresponding signals since you started the session, the XNET Signal Default Value is returned.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-signal-xy.html language=enus -->
## TOPIC 00094: XY

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-signal-xy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-signal-xy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a session of Signal Input XY mode. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Input XY. number to read The number of values desired. If number to read is positive (or 0), the

XY

Reads data from a session of Signal Input XY mode.

[IMAGE alt='1378' src='XNET_Read_(Signal_XY).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Input XY.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number to read

The number of values desired.

If number to read is positive (or 0), the size of value arrays is no greater than this number.

If number to read is negative (typically -1), the maximum number of values is returned.

This input is optional. The default value is -1.

If number to read values are received for any signal, XNET Read (Signal XY) returns those values, even if the time limit has not occurred. Therefore, to read values up to the time limit, leave number to read unwired (-1).

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### time limit

The timestamp to wait for before returning signal values.

time limit

number to read

time limit

If time limit is unwired (invalid), XNET Read (Signal XY) returns immediately all available values up to the current time (up to number to read).

This input is optional. The default value is an invalid timestamp.

The timeout of other XNET Read instances specifies the maximum amount time to wait for a specific number to read values. The time limit of XNET Read (Signal XY) does not specify a worst-case timeout value, but rather a specific absolute timestamp to wait for.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

An output that returns an array of LabVIEW clusters.

Each cluster contains two arrays, one for timestamp and one for value. For each signal, the size of the timestamp and value arrays always is the same, such that it represents a single array of timestamp/value pairs.

Each timestamp/value pair represents a value from a received frame. When signals exist in different frames, the array sizes may be different from one cluster (signal) to another.

When you use this instance with a session of Signal Input Single-Point Mode, time limit and number to read are ignored, and the timestamp and value arrays always contain only one element per signal. This effectively returns a single pair of timestamp and value for every signal.

[IMAGE alt='datatype_icon' src='/assets/img/i1dtimestamp.png']

##### timestamp

The array of LabVIEW timestamps, one for each frame received that contains the signal.

Each timestamp represents the absolute time when the XNET interface received the frame (end of frame), accurate to microseconds.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### value

The array of signal values, one for each frame received that contains the signal.

The value array size is the same as the timestamp array size.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You also can use this instance to read data from a session of Signal Input Single-Point mode, although XNET Read (Signal Single-Point) is more common for that mode.

The data represents an XY plot of timestamp/value pairs for each signal in the session. You can wire the data directly to a LabVIEW XY Graph for display.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-can-comm.html language=enus -->
## TOPIC 00095: CAN Comm

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-can-comm.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-can-comm.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the state of CAN communication using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error

CAN Comm

Reads the state of CAN communication using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_CAN_Comm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### CAN comm

An output that returns a LabVIEW cluster containing the communication elements.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### communication state

A parameter that specifies the CAN interface state with respect to error confinement.

| Error Active (0) | This state reflects normal communication, with few errors detected. The CAN interface remains in this state as long as receive error counter and transmit error counter are both below 128. |
| --- | --- |
| Error Passive (1) | If either the receive error counter or transmit error counter increment above 127, the CAN interface transitions into this state. Although communication proceeds, the CAN device generally is assumed to have problems with receiving frames. When a CAN interface is in error passive state, acknowledgment errors do not increment the transmit error counter. Therefore, if the CAN interface transmits a frame with no other device (ECU) connected, it eventually enters error passive state due to retransmissions, but does not enter bus off state. |
| Bus Off (2) | If the transmit error counter increments above 255, the CAN interface transitions into this state. Communication immediately stops under the assumption that the CAN interface must be isolated from other devices. When a CAN interface transitions to the bus off state, communication stops for the interface. All NI-XNET sessions for the interface no longer receive or transmit frame values. To restart the CAN interface and all its sessions, call XNET Start. |
| Init (3) | This is the CAN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the CAN interface, it transitions from the Init state to the Error Active state. When the interface stops due to a call to XNET Stop, the CAN interface transitions from either Error Active or Error Passive to the Init state. When the interface stops due to the Bus Off state, it remains in that state until you restart. |

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### transceiver error?

A parameter that indicates whether an error condition exists on the physical transceiver.

This is typically referred to as the transceiver chip NERR pin. False indicates normal operation (no error), and true indicates an error.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sleep?

A parameter that indicates whether the transceiver and communication controller are in their sleep state.

False indicates normal operation (awake), and true indicates sleep.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### last error

A parameter that specifies the status of the last attempt to receive or transmit a frame.

| None (0) | The last receive or transmit was successful. |
| --- | --- |
| Stuff (1) | More than 5 equal bits have occurred in sequence, which the CAN specification does not allow. |
| Form (2) | A fixed format part of the received frame used the wrong format. |
| Ack (3) | Another node (ECU) did not acknowledge the frame transmit. If you call XNET Write and do not have a cable connected, or the cable is connected to a node that is not communicating, you see this error repeatedly. The CAN communication state eventually transitions to Error Passive, and the frame transmit retries indefinitely. |
| Bit 1 (4) | During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a recessive bit (logical 1), but the monitored bus value was dominant (logical 0). |
| Bit 0 (5) | During a frame transmit (with the exception of the arbitration ID field), the interface wanted to send a dominant bit (logical 0), but the monitored bus value was recessive (logical 1). |
| CRC (6) | The CRC contained within a received frame does not match the CRC calculated for the incoming bits. |

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### receive error counter

A parameter that counts errors for received frames.

receive error counter

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### transmit error counter

A parameter that counts errors for transmitted frames.

transmit error counter

When communication state transitions to Bus Off, the transmit error counter no longer is valid.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### fault?

A parameter that indicates that a fault occurred, and its code is available as fault code.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### fault code

A parameter that returns a numeric code you can use to obtain a description of the fault.

fault?

A fault is an error that occurs asynchronously to the NI-XNET nodes your application calls. The fault cause may be related to CAN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, XNET Read (State CAN Comm) provides a detection method distinct from the error out of NI-XNET nodes, yet easy to use alongside the common practice of checking the communication state.

To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State CAN Comm) with any XNET session mode, as long as the session interface is CAN. Because the state reflects the CAN interface, it can apply to multiple sessions.

Your application can use XNET Read (State CAN Comm) to check for problems on the CAN network independently from other aspects of your application. For example, you intentionally may introduce noise into the CAN cables to test how your ECU behaves under these conditions. When you do this, you do not want the error out of NI-XNET nodes to return errors, because this may cause your application to stop. Your application can use XNET Read (State CAN Comm) to read the CAN network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW nodes.

Alternately, to log bus errors, you can set the Interface:Bus Error Frames to Input Stream? property to cause CAN bus errors to be logged as a special frame into a Frame Stream Input queue.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-flexray-comm.html language=enus -->
## TOPIC 00096: Comm

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-flexray-comm.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-flexray-comm.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the state of FlexRay communication using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

Comm

Reads the state of FlexRay communication using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_FlexRay_Comm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### FlexRay comm

An output that returns a LabVIEW cluster containing the communication elements.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### POC state

A parameter that specifies the FlexRay interface state.

| Default Config (0) | This is the FlexRay interface initial state on power-up. The interface is essentially off, in that it is not configured and is not attempting to communicate with other nodes (ECUs). |
| --- | --- |
| Ready (1) | When the interface starts, it first enters Config state to validate the FlexRay cluster and interface properties. Assuming the properties are valid, the interface transitions to this Ready state. In the Ready state, the FlexRay interface attempts to integrate (synchronize) with other nodes in the network cluster. This integration process can take several FlexRay cycles, up to 200 ms. If the integration succeeds, the interface transitions to Normal Active. You can use XNET Read (State Time Start) to read the time when the FlexRay interface entered Ready. If integration succeeds, you can use XNET Read (State Time Comm) to read the time when the FlexRay entered Normal Active. |
| Normal Active (2) | This is the normal operation state. The NI-XNET interface is adequately synchronized to the cluster to allow continued frame transmission without disrupting the transmissions of other nodes (ECUs). If synchronization problems occur, the interface can transition from this state to Normal Passive. |
| Normal Passive (3) | Frame reception is allowed, but frame transmission is disabled due to degraded synchronization with the cluster remainder. If synchronization improves, the interface can transition to Normal Active. If synchronization continues to degrade, the interface transitions to Halt. |
| Halt (4) | Communication halted due to synchronization problems. When the FlexRay interface is in Halt state, all NI-XNET sessions for the interface stop, and no frame values are received or transmitted. To restart the FlexRay interface, you must restart the NI-XNET sessions. If you clear (close) all NI-XNET sessions for the interface, it transitions from Halt to Default Config state. |
| Config (15) | This state is transitional when configuration is valid. If you detect this state after starting the interface, it typically indicates a problem with the configuration. Check the fault? output for a fault. If no fault is returned, check your FlexRay cluster and interface properties. You can check the validity of these properties using the NI-XNET Database Editor, which displays invalid configuration properties. |

In the FlexRay specification, this value is referred to as the Protocol Operation Control (POC) state.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### clock correction failed

A parameter that returns the number of consecutive even/odd cycle pairs that have occurred without successful clock synchronization.

In the FlexRay specification, this value is referred to as 
 *vClockCorrectionFailed*.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### passive to active count

A parametert that returns the number of consecutive even/odd cycle pairs that have occurred with successful clock synchronization.

In the FlexRay specification, this value is referred to as 
 *vAllowPassiveToActive*.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### fault?

A parameter that indicates that a fault occurred, and its code is available as fault code.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### fault code

A parameter that returns a numeric code you can use to obtain a fault description.

fault?

A fault is an error that occurs asynchronously to the NI-XNET nodes your application calls. The fault cause may be related to FlexRay communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, XNET Read (State FlexRay Comm) provides a detection method distinct from the error out of NI-XNET nodes, yet easy to use alongside the common practice of checking the communication state.

To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### channel A sleep?

A parameter that indicates whether channel A currently is asleep.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### channel B sleep?

A parameter that indicates whether channel B currently is asleep.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State FlexRay Comm) with any XNET session mode, as long as the session interface is FlexRay. Because the state reflects the FlexRay interface, it can apply to multiple sessions.

Your application can use XNET Read (State FlexRay Comm) to check for problems on the FlexRay network independently from the other aspects of your application. For example, you intentionally may introduce noise into the FlexRay cables to test how your ECU behaves under these conditions. When you do this, you do not want the error out of NI-XNET nodes to return errors, because this may cause your application to stop. Your application can use XNET Read (State FlexRay Comm) to read the FlexRay network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW nodes.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-flexray-cycle-macrotick.html language=enus -->
## TOPIC 00097: Cycle Macrotick

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-flexray-cycle-macrotick.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-flexray-cycle-macrotick.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current FlexRay global time using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error

Cycle Macrotick

Reads the current FlexRay global time using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_FlexRay_Cycle_Macrotick).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### cycle

An output that returns the current FlexRay cycle counter.

vCycleCounter

The XNET Cluster FlexRay:Cycle property returns the cycle length in microseconds.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### macrotick

An output that returns the current FlexRay macrotick.

vMacrotick

The XNET Cluster FlexRay:Macro Per Cycle property returns the number of macroticks in the cycle. The current macrotick returned from this XNET Read instance ranges from 0 to (FlexRay:Macro Per Cycle - 1).

The XNET Cluster FlexRay:Macrotick property returns the macrotick length in floating-point seconds.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Global time represents the timebase that all ECUs on the FlexRay network cluster share. You use sync frames to synchronize the global time. The global time components are the current cycle counter and macrotick within the cycle.

You can use this XNET Read instance with any XNET session mode, as long as the session interface is FlexRay. Because the state reflects the FlexRay interface, it can apply to multiple sessions.

For this node to operate properly, you must connect FlexRay global time as the FlexRay interface timebase source. To do this, you must call XNET Connect Terminals with a source of FlexRay Macrotick and destination of Master Timebase. If the terminals are not connected in this manner, this XNET Read instance returns an error.

When using LabVIEW Real-Time, this node often is useful in conjunction with XNET Create Timing Source (FlexRay Cycle). The FlexRay Cycle timing source enables a LabVIEW timed loop to execute at a specific macrotick within the cycle. Only one FlexRay Cycle timing source is allowed within the cycle. Within the timed loop, you can read the current FlexRay global time to measure performance or synchronize LabVIEW code to additional macroticks in the cycle.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-flexray-statistics.html language=enus -->
## TOPIC 00098: Statistics

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-flexray-statistics.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-flexray-statistics.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads statistics for FlexRay communication using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard

Statistics

Reads statistics for FlexRay communication using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_FlexRay_Stats).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### FlexRay statistics

An output that returns a LabVIEW cluster that contains the statistical elements.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num syntax error ch A

The number of syntax errors that have occurred on channel A since communication started.

- A node starts transmitting while the channel is not in the idle state.
- There is a decoding error.
- A frame is decoded in the symbol window or in the network idle time.
- A symbol is decoded in the static segment, dynamic segment, or network idle time.
- A frame is received within the slot after reception of a semantically correct frame (two frames in one slot).
- Two or more symbols are received within the symbol window.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num syntax error ch B

The number of syntax errors that have occurred on channel B since communication started.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num content error ch A

The number of content errors that have occurred on channel A since communication started.

- In a static segment, the payload length of a frame does not match the global cluster property.
- In a static segment, the Startup indicator (bit) is 1 while the Sync indicator is 0.
- A frame ID encoded in the frame header does not match the current slot.
- A cycle count encoded in the frame’s header does not match the current cycle count.
- In a dynamic segment, the Sync indicator is 1.
- In a dynamic segment, the Startup indicator is 1.
- In a dynamic segment, the Null indicator is 0.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num content error ch B

The number of content errors that have occurred on channel B since communication started.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num slot boundary violation ch A

The number of slot boundary violations that have occurred on channel A since communication started.

A slot boundary violation error occurs if the interface does not consider the channel to be idle at the boundary of a slot (either beginning or end).

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### num slot boundary violation ch B

The number of slot boundary violations that have occurred on channel B since communication started.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use this XNET Read instance with any XNET session mode, as long as the session's interface is FlexRay. Because the state reflects the FlexRay interface, it can apply to multiple sessions.

Like other XNET Read instances, this node executes quickly, so it is appropriate for real-time loops. The statistical information is updated during the Network Idle Time (NIT) of each FlexRay cycle.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-j1939-comm.html language=enus -->
## TOPIC 00099: J1939 Comm

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-j1939-comm.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-j1939-comm.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the state of J1939 communication using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface. error in Error conditions that occur before this node runs. The node responds to

J1939 Comm

Reads the state of J1939 communication using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_J1939_Comm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### J1939 comm

An output that returns a LabVIEW cluster containing the communication elements.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### PGN

A parameter that specifies the J1939 PGN that occurred the last error. You cannot assign a PGN to every error.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### src address

A parameter that specifies the source address that occurred the last error. You cannot assign a source address to every error.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### dest addr

A parameter that specifies the destination address that occurred the last error. You cannot assign a destination address to every error or warning.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### transmit error

A parameter that indicates a transmit-related error occurred.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### receive error

A parameter that indicates a receive-related error occurred.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### fault?

A parameter that indicates that a fault occurred, and its code is available as fault code.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### fault code

A parameter that returns a numeric code you can use to obtain a description of the fault. If fault? is false, the fault code is 0.

A fault is an error that occurs asynchronously to the NI-XNET nodes your application calls. The fault cause may be related to CAN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, XNET Read (State J1939 Comm) provides a detection method distinct from the error out of NI-XNET nodes, yet easy to use alongside the common practice of checking the communication state.

To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State J1939 Comm) with any XNET session mode, as long as the session interface is CAN. Because the state reflects the CAN interface, it can apply to multiple sessions.

Your application can use XNET Read (State J1939 Comm) to check for problems on the J1939 network independently from other aspects of your application. For example, you intentionally may introduce noise into the CAN cables to test how your ECU behaves under these conditions. When you do this, you do not want the error out of NI-XNET nodes to return errors, because this may cause your application to stop. Your application can use XNET Read (State J1939 Comm) to read the J1939 network state quickly as data, so it does not introduce errors into the flow of your LabVIEW nodes.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-lin-comm.html language=enus -->
## TOPIC 00100: LIN Comm

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-lin-comm.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-lin-comm.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the state of LIN communication using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface. error in Error conditions that occur before this node runs. The node responds to t

LIN Comm

Reads the state of LIN communication using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_LIN_Comm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### LIN comm

An output that returns a LabVIEW cluster containing the communication elements.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### communication state

A parameter that specifies the LIN interface state.

| Idle (0) | This is the LIN interface initial state on power-up. The interface is essentially off, in that it is not attempting to communicate with other nodes (ECUs). When the start trigger occurs for the LIN interface, it transitions from the Idle state to the Active state. When the interface stops due to a call to XNET Stop, the LIN interface transitions from either Active or Inactive to the Idle state. |
| --- | --- |
| Active (1) | This state reflects normal communication. The LIN interface remains in this state as long as bus activity is detected (frame headers received or transmitted). |
| Inactive (2) | This state indicates that no bus activity has been detected in the past four seconds. Regardless of whether the interface acts as a master or slave, it transitions to this state after four seconds of bus inactivity. As soon as bus activity is detected (break or frame header), the interface transitions to the Active state. The LIN interface does not go to sleep automatically when it transitions to Inactive. To place the interface into sleep mode, set the XNET Session Interface:LIN:Sleep property when you detect the Inactive state. |

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sleep?

A parameter that indicates whether the transceiver and communication controller are in their sleep state.

This Boolean value changes from false to true only when you set the XNET Session Interface:LIN:Sleep property to Remote Sleep or Local Sleep.

This Boolean value changes from true to false when one of the following occurs:

- You set the XNET Session Interface:LIN:Sleep property to Remote Wake or Local Wake .
- The interface receives a remote wakeup pattern (break). In addition to this XNET Read node, you can wait for a remote wakeup event using XNET Wait (LIN Remote Wakeup).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### transceiver ready?

A parameter that indicates whether the LIN transceiver is powered from the bus.

If this value is false, you cannot start communication successfully. Wire power to the LIN transceiver and run your application again.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### last error

A parameter that specifies the status of the last attempt to receive or transmit a frame.

last error

Details

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### last received

A parameter that returns the value received from the network when last error occurred.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### last expected

A parameter that returns the value that the LIN interface expected to see (instead of last received).

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### last identifier

A parameter that returns the frame identifier in which the last error occurred.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### fault?

A parameter that indicates that a fault occurred, and its code is available as fault code.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### fault code

A parameter that returns a numeric code you can use to obtain a fault description.

fault?

A fault is an error that occurs asynchronously to the NI-XNET nodes your application calls. The fault cause may be related to LIN communication, but it also can be related to XNET hardware, such as a fault in the onboard processor. Although faults are extremely rare, XNET Read (State LIN Comm) provides a detection method distinct from the error out of NI-XNET nodes, yet easy to use alongside the common practice of checking the communication state.

To obtain a fault description, wire the fault code into the LabVIEW Simple Error Handler error code input and view the resulting message. You also can bundle the fault code into a LabVIEW error cluster as the code element and use front panel features to view the error description.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### schedule index

A parameter that indicates the LIN schedule that the interface is currently running.

This index applies only when the LIN interface is running as a master. If the LIN interface is running as a slave only, this element should be ignored.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State LIN Comm) with any XNET session mode, as long as the session interface is LIN. Because the state reflects the LIN interface, it can apply to multiple sessions.

Your application can use XNET Read (State LIN Comm) to check for problems on the LIN network independently from other aspects of your application. For example, you intentionally may introduce noise into the LIN cables to test how your ECU behaves under these conditions. When you do this, you do not want the 
 error out of NI-XNET nodes to return errors, because this may cause your application to stop. Your application can use XNET Read (State LIN Comm) to read the LIN network state quickly as data, so that it does not introduce errors into the flow of your LabVIEW nodes.

The following table lists each value for 
 last error, along with a description, and applicable use of 
 last received, 
 last expected, and 
 last identifier. In the 
 last error column, the decimal value is shown in parentheses after the string name.

| Last Error | Description | Last Received | Last Expected | Last Identifier |
| --- | --- | --- | --- | --- |
| None (0) | No bus error has occurred since the previous communication state read. | 0 (N/A) | 0 (N/A) | 0 (N/A) |
| Unknown ID (1) | Received a frame identifier that is not valid (0–63). | 0 (N/A) | 0 (N/A) | 0 (N/A) |
| Form (2) | The form of a received frame is incorrect. For example, the database specifies 8 bytes of payload, but you receive only 4 bytes. | 0 (N/A) | 0 (N/A) | Received frame ID |
| Framing (3) | The byte framing is incorrect (for example, a missing stop bit). | 0 (N/A) | 0 (N/A) | Received frame ID |
| Readback (4) | The interface transmitted a byte, but the value read back from the transceiver was different. This often is caused by a cabling problem, such as noise. | Value read back | Value transmitted | Received frame ID |
| Timeout (5) | Receiving the frame took longer than the LIN-specified timeout. | 0 (N/A) | 0 (N/A) | Received frame ID |
| Checksum (6) | The received checksum was different than the expected checksum. | Received checksum | Calculated checksum | Received frame ID |

If the bus error is detected at time when no frame ID is received (such as wakeup), 
 last identifier uses the special value 64.

Alternately, to log bus errors, you can set the Interface:Bus Error Frames to Input Stream? property to cause LIN bus errors to be logged as a special frame into a Frame Stream Input queue.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-session-info.html language=enus -->
## TOPIC 00101: Session Info

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-session-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-session-info.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current state for the session provided. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior

Session Info

Returns the current state for the session provided.

[IMAGE alt='1378' src='XNET_Read_(State_Session_Info).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### session info state

An output that returns the state of the provided session.

Stopped (0)

Started (1) All frames in the session are started.

Mix (2) Some frames in the session are started while other frames are stopped.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State Session Info) with any XNET session mode.

XNET Read (State Session Info) returns the state of the session's objects. A mixed state may occur when using XNET Start or XNET Stop with the Session Only option. By reading this state, your application can ensure that all frames in the session have started or stopped.

If the session is started with any option other than Session Only, the state is known, so this node may not be useful.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-time-comm.html language=enus -->
## TOPIC 00102: Comm

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-time-comm.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-time-comm.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the time at which the session's interface completed its integration with the network cluster. This represents the time at which communication began. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions

Comm

Reads the time at which the session's interface completed its integration with the network cluster. This represents the time at which communication began.

[IMAGE alt='1378' src='XNET_Read_(State_Time_Comm).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time communicating

An output that returns the communication time of the interface as a LabVIEW absolute timestamp.

time communicating

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use this XNET Read node with any XNET session mode. Because the time is associated with the interface, it can apply to multiple sessions.

This XNET Read node returns time as a LabVIEW absolute timestamp data type.

After your application starts the XNET interface hardware, the communication controller begins to integrate with ECUs in the network. The timestamp at which this integration starts is available using XNET Read (State Time Start). Once the XNET interface is fully integrated and communicating on the network (transmitting and receiving frames), this node captures and returns the time. For the CAN protocol, the time difference between Start and Communicating is very small. For the FlexRay protocol, the time difference can be many milliseconds due to factors such as clock synchronization and cycle length.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-time-current.html language=enus -->
## TOPIC 00103: Current

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-time-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-time-current.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current interface timestamp using an XNET session. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error

Current

Reads the current interface timestamp using an XNET session.

[IMAGE alt='1378' src='XNET_Read_(State_Time_Current).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time current

An output that returns the current interface timestamp as a LabVIEW absolute time.

time current

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State Time Current) with any XNET session mode. Because the time is associated with the interface, it can apply to multiple sessions.

XNET Read (State Time Current) returns time as a LabVIEW absolute timestamp data type. The timestamp represents absolute time that the interface timebase source drives. You use the timebase source to timestamp frames the interface receives. For a CAN interface, you use the timebase source to schedule cyclic frame transmit.

The interface timebase source is not necessarily connected to the LabVIEW CPU clock, so this timestamp can drift relative to the LabVIEW time used for internally sourced timed loops and LabVIEW Get Date/Time in Seconds.

For more information about the interface timebase source, refer to XNET Connect Terminals.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-time-start.html language=enus -->
## TOPIC 00104: Start

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-time-start.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-time-start.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the time when the session interface started its integration. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard

Start

Reads the time when the session interface started its integration.

[IMAGE alt='1378' src='XNET_Read_(State_Time_Start).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time start

An output that returns the interface start time as a LabVIEW absolute timestamp.

time start

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Read (State Time Start) with any XNET session mode. Because the time is associated with the interface, it can apply to multiple sessions.

XNET Read (State Time Start) returns time as a LabVIEW absolute timestamp data type.

Your application typically starts the interface simply by calling XNET Read or XNET Write, because the XNET Session Auto Start? property is true by default. If you set Auto Start? to false, you start the interface using XNET Start. If you use XNET Connect Terminals to import a start trigger for the interface, all sessions for that interface wait for the trigger to occur before starting the interface.

Once the interface starts, this node captures and returns the time. Unless you connect a start trigger, this time generally is known, so this node may not be useful.

After the XNET interface starts, the communication controller begins to integrate with ECUs in the network. After this integration is complete, the time is captured and available using XNET Read (State Time Comm). That time often is useful for FlexRay, because it indicates the time when true communication began.

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read-state-time-trigger.html language=enus -->
## TOPIC 00105: Trigger

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read-state-time-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read-state-time-trigger.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the captured timestamp for an imported Time Trigger. session in The session to read. This session is selected from the LabVIEW project or returned from XNET Create Session. error in Error conditions that occur before this node runs. The node responds to this input according to standard error b

Trigger

Reads the captured timestamp for an imported Time Trigger.

[IMAGE alt='1378' src='XNET_Read_(State_Time_Trigger).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to read.

This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the rising edge of Time Trigger. The timeout is a LabVIEW
 relative time, represented as 64-bit floating-point in units of seconds.

If timeout is positive, XNET Read (State Time Trigger) waits for the
 rising edge of Time Trigger, then returns the timestamps for that edge. If the edge does not
 occur prior to the timeout, an error is returned.

If timeout is negative, XNET Read (State Time Trigger) waits
 indefinitely for the rising edge of Time Trigger.

If timeout is zero, XNET Read (State Time Trigger) does not wait and
 immediately returns the timestamps, which are zero (invalid) if the rising edge of Time
 Trigger has not occurred.

This input is optional. The default value is 10.0 (10 seconds).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### local time trigger

Returns the timestamp of first rising edge of the imported Time Trigger since it was
 armed.

The timestamp is a LabVIEW absolute time, using the local timescale. If Time Trigger has
 not encountered a rising edge since it was armed, local time
 trigger returns zero (an invalid timestamp).

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### network time trigger

Returns the timestamp of first rising edge of the imported Time Trigger since it was
 armed.

The timestamp is a LabVIEW absolute time, using the network timescale. If Time Trigger has not
 encountered a rising edge since it was armed, local time
 trigger returns zero (an invalid timestamp).

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### network synced?

Contains the value of the Synced property at the time that both timestamps are
 acquired, to specify whether the network timestamp is synchronized to the network (true)
 or not (false).

#### Description

When you use [XNET
 Connect Terminals](xnet-connect-terminals.html) with destination terminal of TimeTrigger (i.e., imported), the
 Time Trigger captures absolute timestamps on the rising edge, and you read those
 timestamps using this node.

The imported Time Trigger is armed when you invoke XNET Connect Terminals, and Time
 Trigger is armed again on each subsequent invocation of XNET Read (State Time Trigger).
 After the Time Trigger is armed, the first rising edge after arming is captured for the
 subsequent XNET Read (State Time Trigger).

Parent topic:

XNET Read

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-read.html language=enus -->
## TOPIC 00106: XNET Read

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-read.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from the network using an XNET session.

XNET Read

Reads data from the network using an XNET session.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-start.html language=enus -->
## TOPIC 00107: XNET Start

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-start.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-start.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts communication for the specified XNET session. session in The session to start. This session is selected from the LabVIEW project or returned from XNET Create Session. scope An input that describes the impact of this operation on the underlying state models for the session and its interface. N

XNET Start

Starts communication for the specified XNET session.

[IMAGE alt='1378' src='XNET_Start.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to start. This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### scope

An input that describes the impact of this operation on the underlying state models for the session and its interface.

| Normal (0) | The session is started followed by starting the interface. This is equivalent to calling XNET Start with the Session Only scope followed by calling XNET Start with the Interface Only scope. This is the default value for scope if it is unwired. |
| --- | --- |
| Session Only (1) | The session is placed into the Started state . If the interface is in the Stopped state before this node runs, the interface remains in the Stopped state, and no communication occurs with the bus. To have multiple sessions start at exactly the same time, start each session with the Session Only scope. When you are ready for all sessions to start communicating on the associated interface, call XNET Start with the Interface Only scope. Starting a previously started session is considered a no-op. This operation sends the command to start the session, but does not wait for the session to be started. It is ideal for a real-time application where performance is critical. |
| Interface Only (2) | If the underlying interface is not previously started, the interface is placed into the Started state . After the interface starts communicating, all previously started sessions can transfer data to and from the bus. Starting a previously started interface is considered a no-op. |
| Session Only Blocking (3) | The session is placed into the Started state . If the interface is in the Stopped state before this node runs, the interface remains in the Stopped state, and no communication occurs with the bus. To have multiple sessions start at exactly the same time, start each session with the Session Only scope. When you are ready for all sessions to start communicating on the associated interface, call XNET Start with the Interface Only scope. Starting a previously started session is considered a no-op. This operation waits for the session to start before completing. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Because the session is started automatically by default, this node is optional. This node is for more advanced applications to start multiple sessions in a specific order. For more information about the automatic start feature, refer to the Auto Start? property.

For each physical interface, the NI-XNET hardware is divided into two logical units:

- Sessions: You can create one or more sessions, each of which contains frames or signals to be transmitted (or received) on the bus.
- Interface: The interface physically connects to the bus and transmits (or receives) data for the sessions.

You can start each logical unit separately. When a session is started, all contained frames or signals are placed in a state where they are ready to communicate. When the interface is started, it takes data from all started sessions to communicate with other nodes on the bus.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-stop.html language=enus -->
## TOPIC 00108: XNET Stop

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-stop.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops communication for the specified XNET session. session in The session to stop. This session is selected from the LabVIEW project or returned from XNET Create Session. scope An input that describes the impact of this operation on the underlying state models for the session and its interface. Nor

XNET Stop

Stops communication for the specified XNET session.

[IMAGE alt='1378' src='XNET_Stop.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to stop. This session is selected from the LabVIEW project or returned from XNET Create Session.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### scope

An input that describes the impact of this operation on the underlying state models for the session and its interface.

| Normal (0) | The session is stopped. If this is the last session stopped on the interface, the interface is also stopped. If any other sessions are running on the interface, this call is treated just like the Session Only scope, to avoid disruption of communication on the other sessions. This is the default value for scope if it is unwired. |
| --- | --- |
| Session Only (1) | The session is placed in the Stopped state . If the interface was in the Started or Running state before this node is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope only stops the interface if there are no other running sessions. This operation sends the command to stop the session, but does not wait for the session to be stopped. It is ideal for a real-time application where performance is critical. |
| Interface Only (2) | The underlying interface is placed in the Stopped state . This prevents all communication on the bus, for all sessions. This allows you to modify certain properties that require the interface to be stopped (for example, CAN baud rate). All sessions remain in the Started state. To have multiple sessions stop at exactly the same time, first stop the interface with the Interface Only scope and then stop each session with either the Normal or Session Only scope. |
| Session Only Blocking (3) | The session is placed in the Stopped state . If the interface was in the Started or Running state before this node is called, the interface remains in that state and communication continues, but data from this session does not transfer. This scope generally is not necessary, as the Normal scope stops the interface only if there are no other running sessions. This operation waits for the session to stop before completing. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Because the session is stopped automatically when cleared (closed), this node is optional.

For each physical interface, the NI-XNET hardware is divided into two logical units:

- Sessions: You can create one or more sessions, each of which contains frames or signals to be transmitted (or received) on the bus.
- Interface: The interface physically connects to the bus and transmits (or receives) data for the sessions.

You can stop each logical unit separately. When a session is stopped, all contained frames or signals are placed in a state where they are no longer ready to communicate. When the interface is stopped, it no longer takes data from sessions to communicate with other nodes on the bus.

Parent topic:

NI-XNET Nodes

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-wait-can-remote-wakeup.html language=enus -->
## TOPIC 00109: CAN Remote Wakeup

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-wait-can-remote-wakeup.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-wait-can-remote-wakeup.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the CAN interface to wake up due to activity by a remote ECU on the network. session in The session to apply the wait. timeout An input that specifies the maximum amount of time in seconds to wait. error in Error conditions that occur before this node runs. The node responds to this input

CAN Remote Wakeup

Waits for the CAN interface to wake up due to activity by a remote ECU on the network.

[IMAGE alt='1378' src='XNET_Wait_(CAN_Remote_Wakeup).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to apply the wait.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

An input that specifies the maximum amount of time in seconds to wait.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This wait is used when you set the XNET Session Interface:CAN:Transceiver State property to Sleep. When asleep, the interface and transceiver go into a low-powered mode. If a remote CAN ECU transmits a frame, the transceiver detects this transmission, and both the controller and transceiver wake up. This wait detects that remote wakeup.

Note

The timeout parameter provides the maximum number of seconds to wait. This value must be 1.0 (one second) or greater. The default value is 10 (10 seconds).

Parent topic:

XNET Wait

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-wait-ethernet-synced.html language=enus -->
## TOPIC 00110: Ethernet Synced

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-wait-ethernet-synced.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-wait-ethernet-synced.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the Ethernet interface to synchronize time on the network. session in The session to apply the wait. timeout An input that specifies the maximum amount of time in seconds to wait. error in Error conditions that occur before this node runs. The node responds to this input according to stand

Ethernet Synced

Waits for the Ethernet interface to synchronize time on the network.

[IMAGE alt='1378' src='XNET_Wait_(Ethernet_Synced).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to apply the wait.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

An input that specifies the maximum amount of time in seconds to wait.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Waits for the clock of the Ethernet interface to successfully synchronize to other clocks in
 the network. This wait returns when the time synchronization protocol's Synced property
 becomes true.

Note

The timeout parameter provides the maximum number of seconds to wait. The default value is 10 seconds.

Parent topic:

XNET Wait

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-wait-interface-communicating.html language=enus -->
## TOPIC 00111: Interface Communicating

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-wait-interface-communicating.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-wait-interface-communicating.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the interface to begin communication on the cluster. session in The session to apply the wait. timeout An input that specifies the maximum amount of time in seconds to wait. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

Interface Communicating

Waits for the interface to begin communication on the cluster.

[IMAGE alt='1378' src='XNET_Wait_(Interface_Communicating).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to apply the wait.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

An input that specifies the maximum amount of time in seconds to wait.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Waits for the interface to begin communication on the cluster. After the interface is started, the controller connects to the cluster and starts communication. This wait returns after communication with the cluster has been established.

Note

Note

The timeout parameter provides the maximum number of seconds to wait. The default value is 10 (10 seconds).

Parent topic:

XNET Wait

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-wait-lin-remote-wakeup.html language=enus -->
## TOPIC 00112: LIN Remote Wakeup

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-wait-lin-remote-wakeup.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-wait-lin-remote-wakeup.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the LIN interface to wake up due to activity by a remote ECU on the network. session in The session to apply the wait. The wait applies to the LIN interface, so you can use any session. timeout An input that specifies the maximum amount of time in seconds to wait. error in Error conditions

LIN Remote Wakeup

Waits for the LIN interface to wake up due to activity by a remote ECU on the network.

[IMAGE alt='1378' src='XNET_Wait_(LIN_Remote_Wakeup).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to apply the wait. The wait applies to the LIN interface, so you can use any session.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

An input that specifies the maximum amount of time in seconds to wait.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

This wait is used when you set the XNET Session Interface:LIN:Sleep property to Remote Sleep or Local Sleep. When asleep, if a remote LIN ECU transmits the wakeup pattern (break), the XNET LIN interface detects this transmission and wakes up. This wait detects that remote wakeup.

The timeout parameter provides the maximum number of seconds to wait. This value must be 1.0 (one second) or greater. The default value is 10 (10 seconds).

Parent topic:

XNET Wait

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-wait-transmit-complete.html language=enus -->
## TOPIC 00113: Transmit Complete

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-wait-transmit-complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-wait-transmit-complete.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for previously written data to be transmitted on the cluster. session in The session to apply the wait. timeout An input that specifies the maximum amount of time in seconds to wait. error in Error conditions that occur before this node runs. The node responds to this input according to standa

Transmit Complete

Waits for previously written data to be transmitted on the cluster.

[IMAGE alt='1378' src='XNET_Wait_(Transmit_Complete).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to apply the wait.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

An input that specifies the maximum amount of time in seconds to wait.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

Waits for all data provided to XNET Write before this XNET Wait call to be transmitted on the CAN, FlexRay, or LIN network. Depending on the bus or configuration properties such as Interface:CAN:Single Shot Transmit?, the data may or may not have been successfully transmitted; however, if this wait returns successfully, it indicates that the session is making no more attempts to transmit the data. This wait applies to only the current XNET session, and not other sessions used for the same interface.

After using XNET Write to provide data for this session, you can use this node to wait for that data to transmit to remote ECUs. You can use this node to guarantee that all frames have been transmitted before stopping this session.

The timeout parameter provides the maximum number of seconds to wait. The default value is 10 (10 seconds).

Parent topic:

XNET Wait

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-frame-can.html language=enus -->
## TOPIC 00114: CAN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-frame-can.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-frame-can.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session as an array of CAN frames. The session must use a CAN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The

CAN

Writes data to a session as an array of CAN frames. The session must use a CAN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='1378' src='XNET_Write_(Frame_CAN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### data

An input that provides the array of LabVIEW clusters.

For a Frame Output Single-Point session mode, the order of frames in the array corresponds to the order in the session list.

The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write.

Additionally, XNET Write (Frame CAN) can be called on any signal or frame input session if it contains one or more Event Remote frames (refer to CAN:Timing Type). In this case, it signals an event to transmit those remote frames. The data parameter is ignored in this case, and you can set it to an empty array.

The elements of each cluster are specific to the CAN protocol. For more information, refer to 
 the CAN protocol specification.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### identifier

The CAN frame arbitration identifier.

extended?

If extended? is true, the identifier uses extended format, so 29 bits of this identifier are valid.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### extended?

A Boolean value that determines whether the identifier uses extended format (true) or standard format (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

A parameter not used for transmit. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### type

The frame type (decimal value in parentheses).

| CAN Data (0) | The CAN data frame contains payload data. This is the most commonly used frame type for CAN. In ISO CAN FD interface mode, this transmits a frame according to the interface setting (FD or FD+BRS). ISO CAN FD mode allows transmitting CAN 2.0, CAN FD, or CAN FD+BRS frames using the frame type (refer to the types listed below). |
| --- | --- |
| CAN 2.0 Data (8) | The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN 2.0 frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN FD Data (16) | The CAN data frame contains payload data. In ISO CAN FD interface mode, this frame is transmitted as a CAN FD (no BRS) frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN FD+BRS Data (24) | The CAN data frame contains payload data. In ISO CAN FD+BRS mode, this frame is transmitted as a CAN FD+BRS frame. When the interface is not in ISO CAN FD mode, this type is treated like CAN Data (0). |
| CAN Remote (1) | A CAN remote frame. Your application transmits a CAN remote frame to request data for the corresponding identifier. A remote ECU should respond with a CAN data frame for the identifier, which you can obtain using XNET Read. |

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

A parameter that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for the CAN data frame.

When the session mode is Frame Output Single-Point or Frame Output Queued, the number of bytes in the payload array must be less than or equal to the Payload Length property of the corresponding frame. You can leave all other CAN frame cluster elements uninitialized. For more information, refer to the section for each mode.

For a transmitted remote frame (CAN Remote type), the payload length in the frame value specifies the number of payload bytes requested. Your application provides this payload length by filling payload with the requested number of bytes. This enables your application to specify the frame payload length, but the actual values in the payload bytes are ignored (not contained in the transmitted frame).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the CAN frame data to be queued up for transmit.

If timeout is positive, XNET Write (Frame CAN) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Frame CAN) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Frame CAN) does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Frame CAN) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of CAN frames. Each CAN frame uses a LabVIEW cluster with CAN-specific elements.

The CAN frames are associated to the session's list of frames as follows:

- Frame Output Stream: Array of all frame values for transmit (list ignored).
- Frame Output Queued: Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point: Array of single frame values, one for each frame specified in the list.
- Any signal or frame input mode: The data parameter is ignored, and you can set it to an empty array. The node transmits an event remote frame.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-frame-ethernet.html language=enus -->
## TOPIC 00115: Ethernet

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-frame-ethernet.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-frame-ethernet.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session as an array of Ethernet frames. The session must use an Ethernet interface and a mode of Frame Output Stream. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream

Ethernet

Writes data to a session as an array of Ethernet frames. The session must use an
 Ethernet interface and a mode of Frame Output Stream.

[IMAGE alt='1378' src='XNET_Write_(Frame_Ethernet).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

XNET Create Session

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### data

Provides an array of LabVIEW clusters.

Each array element corresponds to a frame value to transmit. The elements of each cluster are
 specific to the Ethernet protocol.

The data you write is queued up for transmit on the network. Using the default queue
 configuration for this mode, you can safely write 64 frames if you have a sufficiently long
 timeout. To write more data, refer to the XNET Session Number of Values Unused property to
 determine the actual amount of queue space available for write.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### local timestamp

A timestamp using XNET local time. The timestamp uses the LabVIEW absolute
 timestamp type.

The timestamp point in the Ethernet frame occurs at the beginning of the first symbol
 following the start of frame delimiter.

local timestamp is not used for XNET Write (Frame Ethernet). Refer
 to [XNET Read (Frame
 Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### network timestamp

A timestamp using network time (clock of the network's time synchronization protocol,
 such as IEEE Std 802.1AS). The timestamp uses the LabVIEW absolute timestamp type.

The timestamp point in the Ethernet frame occurs at the beginning of the first symbol
 following the start of frame delimiter.

network timestamp is not used for XNET Write (Frame Ethernet).
 Refer to [XNET Read
 (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### frame data

An array of bytes that provides the data of the Ethernet frame.

Using the terminology from IEEE Std 802.3, the frame
 data begins with the first byte of the destination MAC
 address, and ends with the last byte of the mac_service_data_unit
 (MSDU).

In order to obtain the payload data that is contained in the frame, your code
 must decode the layered headers in frame data. For
 example, for an IPv4 UDP packet, you decode the Ethernet header, including
 the EtherType, to determine that the remaining data is an IPv4 packet; then
 you decode the IPv4 header, including the Protocol, to determine that the
 remaining data is a UDP packet; and then you decode the UDP header and its
 payload data.

The Source MAC Address Auto property specifies automatic handling of the source
 MAC address in frame data (i.e., offset 6 through 11). If Source Address MAC
 Auto is true (default), XNET automatically replaces the source MAC address
 bytes with its own MAC Address. If Source Address MAC Auto is false, XNET
 does not alter the source MAC address, so that you can specify this address
 in frame data.

The maximum length of this array is provided in the Payload Length Maximum
 property.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### fcs

The IEEE Std 802.3 Frame Check Sequence (FCS) that was received with the
 frame.

fcs is not used for XNET Write (Frame
 Ethernet). Refer to [XNET Read (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### type

The type of Ethernet frame (decimal value in parentheses).

| Ethernet Data (0) | Ethernet frame received or transmitted. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### network synced?

Contains the value of the Synced property at the time that both timestamps are
 acquired, to specify whether the network timestamp is synchronized to the network (true)
 or not (false).

network synced? is not used for XNET Write (Frame Ethernet).
 Refer to [XNET Read
 (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### receive?

A Boolean value that indicates whether the frame occurred due to receive (true) or
 not (false).

receive? is not used for XNET Write (Frame
 Ethernet). Refer to [XNET Read (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### transmit?

A Boolean value that indicates whether the frame occurred due to transmit (true) or
 not (false).

transmit? is not used for XNET Write (Frame
 Ethernet). Refer to [XNET Read (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### error?

A Boolean that indicates whether an error occurred during the
 reception/transmission of the frame (false = good frame, true = bad
 frame).

error? is not used for XNET Write (Frame
 Ethernet). Refer to [XNET Read (Frame Ethernet)](xnet-read-frame-ethernet.html).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the Ethernet frame data to be queued up for
 transmit.

The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of
 seconds.

If timeout is positive, XNET Write (Frame Ethernet) waits up to that
 timeout for space to become available in queues. If the space is not available prior to the
 timeout, an error is returned.

If timeout is negative, XNET Write (Frame Ethernet) waits
 indefinitely for space to become available in queues.

If timeout is zero, XNET Write (Frame Ethernet) does not wait and
 immediately returns with a timeout error if all data cannot be queued. Regardless of the
 timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to
 call the XNET Write (Frame Ethernet) VI again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of Ethernet frames. Each Ethernet frame uses a LabVIEW
 cluster with Ethernet-specific elements.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-frame-flexray.html language=enus -->
## TOPIC 00116: FlexRay

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-frame-flexray.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-frame-flexray.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session as an array of FlexRay frames. The session must use a FlexRay interface and a mode of Frame Output Queued or Frame Output Single-Point. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode m

FlexRay

Writes data to a session as an array of FlexRay frames. The session must use a FlexRay interface and a mode of Frame Output Queued or Frame Output Single-Point.

[IMAGE alt='1378' src='XNET_Write_(Frame_FlexRay).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### data

Provides the array of LabVIEW clusters.

For a Frame Input Single-Point session mode, the order of frames in the array corresponds to the order in the session list.

The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, and assuming frames with 8 bytes of payload, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write.

The elements of each cluster are specific to the FlexRay protocol.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### Slot

A parameter that specifies the slot number within the FlexRay cycle.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### cycle count

A parameter that specifies the cycle number.

The FlexRay cycle count increments from 0 to 63, then rolls over back to 0.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### startup?

A Boolean value that specifies whether the frame is a startup frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### sync?

A Boolean value that specifies whether the frame is a sync frame (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### preamble?

A Boolean value that specifies the value of the payload preamble indicator in the frame header.

preamble?

If the frame is in the dynamic segment, preamble? being true indicates the presence of a message ID at the beginning of the payload. The message ID is always 2 bytes in length.

If preamble? is false, the payload does not contain a network management vector or a message ID.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### chA

A Boolean value that specifies whether to transmit the frame on channel A (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### chB

A Boolean value that specifies whether to transmit the frame on channel B (true) or not (false).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

A parameter not used for transmit. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### type

The frame type.

type

FlexRay Data

FlexRay Data

The FlexRay Null type is not transmitted based on this type. As specified in the XNET Frame FlexRay:Timing Type property, the FlexRay null frame is transmitted when a cyclically timed frame does not have new data.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

A parameter that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

The slot and cycle count specify when the frame transmits in FlexRay global time.

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for FlexRay frames of type FlexRay Data.

For PDU output session mode, the payload is the array of data bytes for the specific PDU, not the entire frame.

When the session mode is Frame Output Single-Point, Frame Output Queued, PDU Output Single-Point, or PDU Output Queued, the number of bytes in the payload array must match the Payload Length property of the corresponding frame. You can leave all other FlexRay frame cluster elements uninitialized. For more information, refer to the section for each mode.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the FlexRay frame data to be queued up for transmit.

If timeout is positive, XNET Write (Frame FlexRay) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Frame FlexRay) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Frame FlexRay) does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Frame FlexRay) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of FlexRay frames. Each FlexRay frame uses a LabVIEW cluster with FlexRay-specific elements.

The FlexRay frames are associated to the session's list of frames as follows:

- Frame Output Queued: Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point: Array of single frame values, one for each frame specified in the list.
- PDU Output Queued: Array of frame (PDU payload) values to transmit for the single PDU specified in the list. This mode is similar to Frame Output Queued.
- PDU Output Single-Point: Array of single frame (PDU payload) values, one for each PDU specified in the list. This mode is similar to a Frame Output Single-Point.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-frame-lin.html language=enus -->
## TOPIC 00117: LIN

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-frame-lin.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-frame-lin.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session as an array of LIN frames. The session must use a LIN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The

LIN

Writes data to a session as an array of LIN frames. The session must use a LIN interface and a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='1378' src='XNET_Write_(Frame_LIN).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### data

An input that provides the array of LabVIEW clusters.

For a Frame Input Single-Point session mode, the order of frames in the array corresponds to the order in the session list.

For Frame Output Queued session mode, the data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for write.

The elements of each cluster are specific to the LIN protocol.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### identifier

A parameter not used for transmit. You must set this element to 0.

identifier

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### event slot?

A parameter not used for transmit. You must set this element to false.

The currently running schedule is used to map the specific frame to a corresponding schedule entry (slot). The schedule entry itself determines whether the slot is unconditional, sporadic, or event triggered.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### event ID

A parameter not used for transmit. You must set this element to 0.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### echo?

A parameter not used for transmit. You must set this element to false.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### type

The frame type (decimal value in parentheses).

| LIN Data (64) | The LIN data frame contains payload data. This is currently the only frame type for LIN. |
| --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

A parameter that represents absolute time using the LabVIEW absolute timestamp type.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### payload

The array of data bytes for a LIN data frame.

The number of bytes in the payload array must match the Payload Length property of the corresponding frame. You can leave all other LIN frame cluster elements uninitialized. For more information, refer to the topic for each mode.

If you use the frame payload within an event-triggered schedule entry (slot), the first byte of data on the network is the frame’s payload identifier. The LIN standard requires this even if the frame transmits in an unconditional or sporadic slot. For this type of LIN frame, the actual data (for example, signal values) is limited to 7 bytes. For this type of frame, you must write the first byte (payload of 8 bytes even if only the last 7 are used), but NI-XNET ignores the value and fills in the first byte for you, using the known frame ID from the session’s configuration.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the LIN frame data to be queued up for transmit.

If timeout is positive, XNET Write (Frame LIN) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Frame LIN) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Frame LIN) does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Frame LIN) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The data represents an array of LIN frames. Each LIN frame uses a LabVIEW cluster with LIN-specific elements.

The LIN frames are associated to the session's list of frames as follows:

- Frame Output Stream Mode: Array of all frame values for transmit (list ignored). If the payload is an empty array, only the header part of the LIN frame is transmitted. If the payload is not an empty array, the header and response parts of the LIN frame are transmitted.
- Frame Output Queued: Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point: Array of single frame values, one for each frame specified in the list.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-frame-raw.html language=enus -->
## TOPIC 00118: Raw

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-frame-raw.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-frame-raw.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session as an array of raw bytes. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. data An input that provides the

Raw

Writes data to a session as an array of raw bytes.

[IMAGE alt='1378' src='XNET_Write_(Frame_Raw).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Frame Output Stream, Frame Output Queued, or Frame Output Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### data

An input that provides the array of bytes, representing frames to transmit.

If needed, you can write data for a partial frame. For example, if a complete raw frame is 24 bytes, you can write 12 bytes, then write the next 12 bytes. You typically do this when you are reading raw frame data from a logfile and want to avoid iterating through the data to detect the start and end of each frame.

For information about which elements of the raw frame are applicable, refer to the XNET Write node for the protocol in use (XNET Write (Frame CAN), XNET Write (Frame FlexRay), or XNET Write (Frame LIN)).

The data you write is queued up for transmit on the network. Using

the default queue configuration for this mode, you can safely write 1536 frames if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for writing.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the raw data to be queued up for transmit.

If timeout is positive, XNET Write (Frame Raw) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Frame Raw) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Frame Raw) does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Frame Raw) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

If the session mode is Frame Output Single-Point, you must set timeout to 0.0. Because this mode writes the most recent value of each frame, timeout does not apply.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

The raw bytes encode one or more frames using the Raw Frame Format. The session must use a mode of Frame Output Stream, Frame Output Queued, or Frame Output Single-Point. The raw frame format is protocol independent, so the session can use either a CAN, FlexRay, or LIN interface.

The raw frame format matches the format of data transferred to/from the XNET hardware. Because it is not converted to/from LabVIEW clusters for ease of use, it is more efficient with regard to performance. This instance typically is used to read raw frame data from a log file and write the data to the interface for transmit (replay).

The raw frames are associated to the session's list of frames as follows:

- Frame Output Stream: Array of all frame values for transmit (list ignored). For LIN, if the payload element is an empty array, only the header part of the LIN frame is transmitted. If the payload element is not an empty array, the header and response parts of the LIN frame are transmitted.
- Frame Output Queued: Array of frame values to transmit for the single frame specified in the list.
- Frame Output Single-Point: Array of single frame values, one for each frame specified in the list.
- PDU Output Queued: Array of frame (PDU payload) values to transmit for the single PDU specified in the list. This mode is similar to 
 Frame Output Queued .
- PDU Output Single-Point: Array of single frame (PDU payload) values, one for each PDU specified in the list. This mode is similar to 
 Frame Output Single-Point .

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-signal-single-point.html language=enus -->
## TOPIC 00119: Single-Point

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-signal-single-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-signal-single-point.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session of Signal Output Single-Point mode. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Output Single-Point. data An input that provides a one-dimensional array of signal val

Single-Point

Writes data to a session of Signal Output Single-Point mode.

[IMAGE alt='1378' src='XNET_Write_(Signal_Single-point).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Output Single-Point.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### data

An input that provides a one-dimensional array of signal values.

Each signal value is scaled, 64-bit floating point.

Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list.

The data provides the value for the next transmit of each signal. If XNET Write (Signal Single-Point) is called twice before the next transmit, the transmitted frame uses signal values from the second call to XNET Write (Signal Single-Point).

A trigger signal written a value of 0.0 suppresses writing of its frame’s data; writing a value not equal to 0.0 enables it.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-signal-waveform.html language=enus -->
## TOPIC 00120: Waveform

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-signal-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-signal-waveform.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session of Signal Output Waveform mode. The data represents a waveform of resampled values for each signal in the session. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Output

Waveform

Writes data to a session of Signal Output Waveform mode. The data represents a waveform of resampled values for each signal in the session.

[IMAGE alt='1378' src='XNET_Write_(Signal_Waveform)_.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Output Waveform.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### data

An input that provides a one-dimensional array of LabVIEW waveforms.

Each array element corresponds to a signal configured for the session. The order of signals in the array corresponds to the order in the session list.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### t0

The waveform start time.

This start time is unused (reserved) for Signal Output Waveform mode. If you change it from its default value of 0 (invalid), XNET Write (Signal Waveform) returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

The waveform delta time.

Y

LabVIEW relative time is represented as 64-bit floating point in units of seconds.

This delta time is unused (reserved) for Signal Output Waveform mode. If you change it from its default value of 0, XNET Write (Signal Waveform) returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### Y

The array of resampled signal values.

The Y array size must be the same for all waveforms, because the size determines the total timeline for XNET Write (Signal Waveform). If the Y array sizes are not the same, XNET Write (Signal Waveform) returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the data to be queued for transmit.

The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds.

If timeout is positive, XNET Write (Signal Waveform) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Signal Waveform) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Signal Waveform) does not wait and immediately returns an error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Signal Waveform) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-signal-xy.html language=enus -->
## TOPIC 00121: XY

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-signal-xy.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-signal-xy.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a session of Signal Output XY mode. The data represents a sequence of signal values for transmit using each frame's timing as the database specifies. session in The session to write. This session is selected from the LabVIEW project or returned from XNET Create Session. The session mo

XY

Writes data to a session of Signal Output XY mode. The data represents a sequence of signal values for transmit using each frame's timing as the database specifies.

[IMAGE alt='1378' src='XNET_Write_(Signal_XY).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session mode must be Signal Output XY.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### data

An input that provides an array of LabVIEW clusters.

The data you write is queued up for transmit on the network. Using the default queue configuration for this mode, you can safely write 64 elements if you have a sufficiently long timeout. To write more data, refer to the XNET Session Number of Values Unused property to determine the actual amount of queue space available for writing.

Each cluster contains two arrays, one for value, and one for timestamp. Each value is mapped to a frame for transmit. When signals exist in different frames, the array sizes may be different from one cluster (signal) to another.

[IMAGE alt='datatype_icon' src='/assets/img/c1dtimestamp.png']

##### timestamp

The array of LabVIEW timestamps.

timestamp

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### value

The array of signal values, one for each frame that contains the signal.

Each signal value is scaled, 64-bit floating point.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time to wait for the data to be queued for transmit.

The timeout is a LabVIEW relative time, represented as 64-bit floating-point in units of seconds.

If timeout is positive, XNET Write (Signal XY) waits up to that timeout for space to become available in queues. If the space is not available prior to the timeout, a timeout error is returned.

If timeout is negative, XNET Write (Signal XY) waits indefinitely for space to become available in queues.

If timeout is 0, XNET Write (Signal XY) does not wait and immediately returns with a timeout error if all data cannot be queued. Regardless of the timeout used, if a timeout error occurs, none of the data is queued, so you can attempt to call XNET Write (Signal XY) again at a later time with the same data.

This input is optional. The default value is 10.0 (10 seconds).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-state-flexray-symbol.html language=enus -->
## TOPIC 00122: FlexRay Symbol

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-state-flexray-symbol.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-state-flexray-symbol.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a request for the FlexRay interface to transmit a symbol on the FlexRay bus. You can use this XNET Write node with any input or output session for FlexRay. session in The session to use for the symbol write. This session is selected from the LabVIEW project or returned from XNET Create Sessio

FlexRay Symbol

Writes a request for the FlexRay interface to transmit a symbol on the FlexRay bus. You can use this XNET Write node with any input or output session for FlexRay.

[IMAGE alt='1378' src='XNET_Write_(State_FlexRay_Symbol).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for the symbol write.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a FlexRay interface.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Write (State FlexRay Symbol) with any XNET session mode, as long as the session interface is FlexRay. Because the symbol write applies to the FlexRay interface, it can apply to multiple sessions.

After calling XNET Write (State FlexRay Symbol), the XNET interface transmits the symbol during the symbol window of the FlexRay cycle following the currently executing cycle. If you call XNET Write (State FlexRay Symbol) multiple times, only the most recent symbol is transmitted.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-state-lin-diagnostic-schedule-change.html language=enus -->
## TOPIC 00123: Diagnostic Schedule Change

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-state-lin-diagnostic-schedule-change.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-state-lin-diagnostic-schedule-change.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write a request for the LIN interface to change the diagnostic schedule. You can use this XNET Write node with any input or output session for LIN. session in The session to use for the diagnostic schedule change. This session is selected from the LabVIEW project or returned from XNET Create Session

Diagnostic Schedule Change

Write a request for the LIN interface to change the diagnostic schedule. You can use this XNET Write node with any input or output session for LIN.

[IMAGE alt='1378' src='XNET_Write_(State_LIN_Diagnostic_Schedule_Change).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for the diagnostic schedule change.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### diagnostics schedule

A ring (enumerated list) that specifies which diagnostic schedule the master executes.

| String | Value |
| --- | --- |
| Null | 0 |
| Master Request | 1 |
| Slave Response | 2 |

This specifies which diagnostic schedule the master executes:

- Null: The master does not execute any diagnostic schedule. No master request or slave response headers are transmitted on the LIN.
- Master Request: The master executes a diagnostic master request schedule (transmits a master request header onto the LIN) if it can. First, a master request schedule must be defined for the LIN cluster in the imported or in-memory database. Otherwise, error nxErrDiagnosticScheduleNotDefined is returned when attempting to set this value. Second, the master must have a frame output queued session created for the master request frame, and there must be one or more new master request frames pending in the queue. If no new frames are pending in the output queue, no master request header is transmitted. This allows the timing of master request header transmission to be controlled by the timing of master request frame writes to the output queue. If there are no normal schedules pending, the master is effectively in diagnostics-only mode, and master request headers are transmitted at a rate determined by the slot delay defined for the master request frame slot in the master request schedule or the nxPropSession_IntfLINDiagSTmin time, whichever is greater, and the state of the master request frame output queue as described above. If there are normal schedules pending, the master is effectively in diagnostics-interleaved mode, and a master request header transmission is inserted between each complete execution of a run-once or run-continuous schedule. This happens as long as the nxPropSession_IntfLINDiagSTmin time has been met, and there are one or more new master request frames pending in the master request frame output queue.
- Slave Response: The master executes a diagnostic slave response schedule (transmits a slave response header onto the LIN) if it can. A slave response schedule must be defined for the LIN cluster in the imported or in-memory database. Otherwise, error nxErrDiagnosticScheduleNotDefined is returned when attempting to set this value. If there are no normal schedules pending, the master is effectively in diagnostics-only mode, and slave response headers are transmitted at the rate of the slot delay defined for the slave response frame slot in the slave response schedule. The addressed slave may or may not respond to each header, depending on its specified P2min and STmin timings. If there are normal schedules pending, the master is effectively in diagnostics-interleaved mode, and a slave response header transmission is inserted between each complete execution of a run-once or run-continuous schedule. Here again, the addressed slave may or may not respond to each header, depending on its specified P2min and STmin timings.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Write (State LIN Diagnostic Schedule Change) with any XNET session mode, as long as the session interface is LIN. Because the schedule change applies to the LIN interface, it can apply to multiple sessions.

According to the LIN protocol, only the master executes schedules, not slaves. If the XNET Session Interface:LIN:Master? property is false (slave), this write function implicitly sets that property to true (master). If the interface currently is running as a slave, this write returns an error, because it cannot change to master while running.

Use XNET Write (State LIN Diagnostic Schedule Change) to transmit master request messages and query for slave response messages after node configuration has been performed. Node configuration should be handled using XNET Write (State LIN Schedule Change). Wire the node configuration schedule defined for the LIN cluster into that node so that it is the first schedule executed for the LIN. Refer to the description for XNET Write (State LIN Schedule Change) for more information about using it to perform node configuration.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write-state-lin-schedule-change.html language=enus -->
## TOPIC 00124: Schedule Change

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write-state-lin-schedule-change.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write-state-lin-schedule-change.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a request for the LIN interface to change the running schedule. You can use this XNET Write node with any input or output session for LIN. session in The session to use for the schedule change. This session is selected from the LabVIEW project or returned from XNET Create Session. The session

Schedule Change

Writes a request for the LIN interface to change the running schedule. You can use this XNET Write node with any input or output session for LIN.

[IMAGE alt='1378' src='XNET_Write_(State_LIN_Schedule_Change).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session to use for the schedule change.

This session is selected from the LabVIEW project or returned from XNET Create Session. The session must use a LIN interface.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### data

The XNET LIN schedule.

data

- XNET LIN Schedule I/O Name: You can use the complete I/O name. This provides features such as the ability to choose from LIN schedules in a selected database.
- String with XNET LIN short name: If you prefer to use the XNET LIN Schedule Name (Short) property, you can wire in the property as a string.
- String with decimal number: This is interpreted as an index into the XNET Cluster LIN:Schedules property used for this session. If you are editing your database file to add/remove LIN schedules, this index may change, in which case the name is the recommended option.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

An output that is the same as session in, provided for use with subsequent nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Description

You can use XNET Write (State LIN Schedule Change) with any XNET session mode, as long as the session interface is LIN. Because the schedule change applies to the LIN interface, it can apply to multiple sessions.

According to the LIN protocol, only the master executes schedules, not slaves. If the XNET Session Interface:LIN:Master? property is false (slave), this write function implicitly sets that property to true (master). If the interface currently is running as a slave, this write returns an error, because it cannot change to master while running.

XNET Write (State LIN Schedule Change) behavior depends on the Run Mode property of the XNET LIN schedule that you wire in as data:

- Continuous: This mode changes the single run-continuous schedule for the interface. The single run-continuous schedule executes all its entries (slots) repetitively, starting over with the first entry after running the last entry. 
 The run-continuous schedule is handled as if it is lowest priority. If you write a run-once schedule in the middle of a run-continuous execution, the run-continuous schedule is interrupted after the current slot finishes. The scheduler switches to the run-once schedule, and when all run-once schedules are done, the scheduler returns to the slot in the run-continuous schedule where it left off. For example, if run-continuous schedule A has 4 slots, and it is executing slot 2 when a run-once schedule B is written, slot 2 of A finishes, then all slots of schedule B run, then the scheduler returns to slot 3 of schedule A. Only one run-continuous schedule exists at a time. If you change from one run-continuous schedule to another in the middle of a run, the current schedule completes all of its slots, then the scheduler changes to the new run-continuous schedule.
- Once: This mode writes a request for a run-once schedule. Multiple run-once schedules can be pending for execution. Each run-once schedule executes all its entries (slots), and then it is considered done. 
 Each run-once schedule has a priority from 1 to 254. Lower values correspond to higher priority (1 is highest). The LIN interface's scheduler maintains a priority queue of run-once schedule requests. This means the highest-priority run-once schedule executes first, followed by the next run-once in priority, and when no run-once schedules are pending, the interface returns to the run-continuous schedule. A run-once schedule cannot interrupt another run-once schedule. For example, if run-once schedule X has 3 slots and is executing slot 0 when a run-once schedule Y with higher priority is written, slots 0, 1, and 2 of X finish, then all slots of schedule Y run.
- Null: This mode stops scheduler execution after the current slot is finished. The queue of run-once schedules is flushed (all elements discarded). 
 The null schedule is considered the highest priority schedule. It overrides the single run-continuous schedule, thus acting as the default scheduling behavior. For example, if you write a null schedule, then write a run-once schedule, the run-once schedule executes all its slots, then communication stops (returns to null schedule). XNET Write (State LIN Schedule Change) does not wait for the requested schedule to finish execution prior to return. The node does not wait for the schedule to begin execution, because in the case of run-once schedules, that may take a long time (depending on priority). Because this node simply writes a schedule request and returns, it is safe to use within a high-priority loop in LabVIEW Real-Time.

Node configuration is handled using XNET Write (State LIN Schedule Change) instead of XNET Write (State LIN Diagnostic Schedule Change). Wire the node configuration schedule defined for the LIN cluster into XNET Write (State LIN Schedule Change) so that it is the first schedule executed for the LIN, with a run mode of once. The data for each node configuration service request entry in the node configuration schedule is automatically transmitted by the master. After the node configuration schedule has completed, use XNET Write (State LIN Diagnostic Schedule Change) to write master request messages and query for slave response messages, or XNET Write (State LIN Schedule Change) to run normal schedules.

Parent topic:

XNET Write

<!--NI_TOPIC bundle=ni-xnet-lvnxg-api-ref path=xnet-write.html language=enus -->
## TOPIC 00125: XNET Write

- bundle_id: `ni-xnet-lvnxg-api-ref`
- source_path: `xnet-write.html`
- source_url: https://docs-be.ni.com/bundle/ni-xnet-lvnxg-api-ref/raw/resource/enus/xnet-write.html
- document_id: `ni-xnet-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the network using an XNET session.

XNET Write

Writes data to the network using an XNET session.

NI-XNET Nodes

These topics describe the NI-XNET nodes.

Parent topic:

NI-XNET Nodes
